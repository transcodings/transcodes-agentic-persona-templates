#!/usr/bin/env python3
"""Write a security-audit PDF from final findings.json.

Usage:
  python3 write_report_pdf.py findings.json --out report.pdf [--font PATH]
  python3 write_report_pdf.py --blank --out report-template.pdf [--font PATH]

findings.json is either the validator's array or an object with a "findings"
array plus target, sourceRef, profile, scope, auditedAt, posture, and coverage.
The PDF is English. This script prints counts. It does not invent a score, and
it does not assign severity to needs-validation records.
"""
import argparse
import json
import pathlib
import sys

VERDICTS = ("confirmed", "needs_validation", "rejected")
SEVERITIES = ("critical", "high", "medium", "low", "informational")
SEVERITY_RANK = {name: index for index, name in enumerate(SEVERITIES)}

COPY = {
    "title": "Security audit report",
    "blank": "Blank report layout",
    "target": "Target",
    "ref": "Source",
    "date": "Audited",
    "profile": "Profile",
    "scope": "Scope",
    "countsTitle": "Recorded results",
    "severityTitle": "Confirmed severity",
    "confirmedTitle": "Confirmed findings",
    "validationTitle": "Needs validation",
    "coverageTitle": "Coverage",
    "confirmed": "Confirmed",
    "needs": "Needs validation",
    "rejected": "Rejected",
    "none": "None.",
    "evidence": "Evidence",
    "result": "Observed result",
    "fix": "Smallest fix",
    "blocker": "Blocker",
    "local": "Local check",
    "owner": "Owner check",
    "rejectedNote": "Rejected records are not findings.",
    "partial": "This is a partial pass. It does not clear the rest of the codebase.",
    "disclaimer": "This report copies the final source-backed records. It is not a live-site test, a penetration test, or a guarantee that unreviewed code is safe. Needs-validation items have no severity.",
    "severity": {
        "critical": "Critical",
        "high": "High",
        "medium": "Medium",
        "low": "Low",
        "informational": "Informational",
    },
    "coverage": {
        "covered": "Covered",
        "candidate": "Candidate",
        "blocked": "Blocked",
        "deferred": "Deferred",
    },
}


def die(message):
    sys.exit(message)


def clean(value):
    if value is None:
        return ""
    return " ".join(str(value).split())


def text(value):
    return clean(value) or "-"


def load_report(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        die(f"Could not read findings JSON: {error}")
    if isinstance(data, list):
        report = {"findings": data}
    elif isinstance(data, dict) and isinstance(data.get("findings"), list):
        report = data
    elif isinstance(data, dict) and isinstance(data.get("records"), list):
        report = {**data, "findings": data["records"]}
    else:
        die('Findings JSON must be an array, or an object with a "findings" array.')
    report["findings"] = [normalize(item, index) for index, item in enumerate(report["findings"], 1)]
    return report


def normalize(item, index):
    if not isinstance(item, dict):
        die(f"Record {index} must be an object.")
    verdict = clean(item.get("verdict")).lower()
    title = clean(item.get("title"))
    if verdict not in VERDICTS or not title:
        die(f"Record {index} needs verdict and title.")
    record = {**item, "verdict": verdict, "title": title, "_index": index}
    if verdict == "confirmed":
        severity = item.get("severity") if isinstance(item.get("severity"), dict) else {}
        overall = clean(severity.get("overall_severity")).lower()
        if overall not in SEVERITIES:
            die(f"Confirmed record {index} needs severity.overall_severity.")
        record["severity_name"] = overall
    return record


def blank_report():
    return {
        "target": "—",
        "sourceRef": "—",
        "profile": "—",
        "scope": "—",
        "auditedAt": "—",
        "posture": "—",
        "blank": True,
        "coverage": {"covered": "—", "candidate": "—", "blocked": "—", "deferred": "—"},
        "findings": [],
    }


def font_candidates(explicit):
    if explicit:
        path = pathlib.Path(explicit)
        if not path.is_file():
            die(f"Font not found: {path}")
        return [path]
    names = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    found = [pathlib.Path(name) for name in names if pathlib.Path(name).is_file()]
    if not found:
        die("No font found. Pass --font with a .ttf, .otf, or .ttc path.")
    return found


INK = (17, 24, 39)
MUTED = (107, 114, 128)
TRACK = (237, 233, 254)
GREEN = (22, 163, 74)
AMBER = (217, 119, 6)
RED = (220, 38, 38)
SLATE = (156, 163, 175)
PURPLE = (123, 97, 255)
BLUE = (37, 99, 235)

COUNT_COLORS = {"confirmed": RED, "needs_validation": AMBER, "rejected": SLATE}
SEVERITY_COLORS = {
    "critical": RED,
    "high": (185, 28, 28),
    "medium": AMBER,
    "low": BLUE,
    "informational": SLATE,
}


def pill(pdf, x, y, width, height, color):
    if width <= 0.4 or height <= 0:
        return
    pdf.set_fill_color(*color)
    if width < height:
        radius = width / 2
        pdf.circle(x + radius, y + height / 2, radius, "F")
        return
    radius = height / 2
    pdf.circle(x + radius, y + radius, radius, "F")
    pdf.rect(x + radius, y, width - height, height, "F")
    pdf.circle(x + width - radius, y + radius, radius, "F")


def ensure_room(pdf, needed):
    if pdf.get_y() > pdf.h - needed:
        pdf.add_page()
        pdf.set_y(16)


def line(pdf, content, height):
    from fpdf.enums import XPos, YPos

    pdf.multi_cell(0, height, content, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def draw_bar(pdf, label, value, maximum, color):
    from fpdf.enums import XPos, YPos

    height = 7
    width = 112
    ensure_room(pdf, 16)
    y = pdf.get_y()
    pdf.set_font("Report", size=10)
    pdf.set_text_color(*INK)
    pdf.set_xy(pdf.l_margin, y)
    pdf.cell(40, height, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
    track_x = pdf.get_x()
    pill(pdf, track_x, y, width, height, TRACK)
    if maximum > 0 and value > 0:
        pill(pdf, track_x, y, width * min(value, maximum) / maximum, height, color)
    pdf.set_xy(track_x + width + 3, y)
    pdf.set_text_color(*color)
    pdf.cell(16, height, str(value), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(*INK)
    pdf.ln(2.2)


def use_font(pdf, candidates):
    errors = []
    for path in candidates:
        try:
            pdf.add_font("Report", fname=str(path))
            return path
        except Exception as error:
            errors.append(f"{path}: {error}")
    die("Could not load a font.\n" + "\n".join(errors))


def evidence_line(item):
    rows = item.get("evidence") if isinstance(item.get("evidence"), list) else []
    parts = []
    for row in rows[:3]:
        if not isinstance(row, dict):
            continue
        location = clean(row.get("file"))
        line_number = row.get("line")
        if location and isinstance(line_number, int):
            location = f"{location}:{line_number}"
        description = clean(row.get("description"))
        parts.append(f"{location} {description}".strip())
    return "; ".join(part for part in parts if part)


def fix_line(item):
    remediation = item.get("remediation") if isinstance(item.get("remediation"), dict) else {}
    strategy = clean(remediation.get("strategy"))
    files = []
    for change in remediation.get("code_changes") or []:
        if isinstance(change, dict) and clean(change.get("file_name")):
            files.append(clean(change.get("file_name")))
    if files:
        suffix = ", ".join(files[:4])
        return f"{strategy} ({suffix})" if strategy else suffix
    return strategy


def counts_for(findings):
    counts = {name: 0 for name in VERDICTS}
    severity = {name: 0 for name in SEVERITIES}
    for item in findings:
        counts[item["verdict"]] += 1
        if item["verdict"] == "confirmed":
            severity[item["severity_name"]] += 1
    return counts, severity


def write_pdf(report, destination, fonts):
    try:
        from fpdf import FPDF
    except ImportError:
        die("Install fpdf2 first: python3 -m pip install fpdf2")

    copy = COPY
    findings = report["findings"]
    counts, severity = counts_for(findings)
    confirmed = [item for item in findings if item["verdict"] == "confirmed"]
    confirmed.sort(key=lambda item: (SEVERITY_RANK[item["severity_name"]], item["_index"]))
    pending = [item for item in findings if item["verdict"] == "needs_validation"]
    maximum = max(1, counts["confirmed"], counts["needs_validation"], counts["rejected"])
    severity_max = max([1, *severity.values()])
    profile = clean(report.get("profile")).lower()
    partial = bool(report.get("blank")) or profile in {"quick", "scoped"} or clean(report.get("runStatus")).lower() == "incomplete"

    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=18)
    use_font(pdf, fonts)
    pdf.add_page()
    pdf.set_fill_color(*PURPLE)
    pdf.rect(0, 0, pdf.w, 4, "F")
    pdf.set_y(14)
    pdf.set_text_color(*INK)
    pdf.set_font("Report", size=20)
    line(pdf, copy["title"], 10)
    if report.get("blank"):
        pdf.set_font("Report", size=11)
        pdf.set_text_color(*MUTED)
        line(pdf, copy["blank"], 6)
    pdf.ln(1)
    pdf.set_font("Report", size=10)
    pdf.set_text_color(*MUTED)
    meta = [
        (copy["target"], report.get("target")),
        (copy["ref"], report.get("sourceRef")),
        (copy["date"], report.get("auditedAt")),
        (copy["profile"], report.get("profile")),
        (copy["scope"], report.get("scope")),
    ]
    for label, value in meta:
        line(pdf, f"{label}: {text(value)}", 5.5)
    pdf.ln(3)
    pdf.set_text_color(*INK)
    pdf.set_font("Report", size=14)
    line(pdf, copy["countsTitle"], 8)
    draw_bar(pdf, copy["confirmed"], counts["confirmed"], maximum, COUNT_COLORS["confirmed"])
    draw_bar(pdf, copy["needs"], counts["needs_validation"], maximum, COUNT_COLORS["needs_validation"])
    draw_bar(pdf, copy["rejected"], counts["rejected"], maximum, COUNT_COLORS["rejected"])
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["severityTitle"], 8)
    for name in SEVERITIES:
        draw_bar(pdf, copy["severity"][name], severity[name], severity_max, SEVERITY_COLORS[name])
    if clean(report.get("posture")):
        pdf.ln(1)
        pdf.set_font("Report", size=11)
        line(pdf, text(report.get("posture")), 6)
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["confirmedTitle"], 8)
    pdf.set_font("Report", size=11)
    if report.get("blank"):
        line(pdf, "1. [—] —", 6)
        line(pdf, "—", 6)
        line(pdf, f"{copy['evidence']}: —", 6)
        line(pdf, f"{copy['result']}: —", 6)
        line(pdf, f"{copy['fix']}: —", 6)
    elif not confirmed:
        line(pdf, copy["none"], 6)
    for number, item in enumerate(confirmed, 1):
        ensure_room(pdf, 28)
        severity_name = copy["severity"][item["severity_name"]]
        line(pdf, f"{number}. [{severity_name}] {item['title']}", 6)
        if clean(item.get("description")):
            line(pdf, text(item.get("description")), 6)
        line(pdf, f"{copy['evidence']}: {text(evidence_line(item))}", 6)
        observed = ""
        if isinstance(item.get("execution"), dict):
            observed = item["execution"].get("observed_result")
        line(pdf, f"{copy['result']}: {text(observed)}", 6)
        line(pdf, f"{copy['fix']}: {text(fix_line(item))}", 6)
        pdf.ln(1)
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["validationTitle"], 8)
    pdf.set_font("Report", size=11)
    if report.get("blank"):
        line(pdf, "1. —", 6)
        line(pdf, f"{copy['blocker']}: —", 6)
        line(pdf, f"{copy['local']}: —", 6)
        line(pdf, f"{copy['owner']}: —", 6)
    elif not pending:
        line(pdf, copy["none"], 6)
    for number, item in enumerate(pending, 1):
        ensure_room(pdf, 24)
        line(pdf, f"{number}. {item['title']}", 6)
        blockers = item.get("blockers") if isinstance(item.get("blockers"), list) else []
        blocker = "; ".join(clean(row) for row in blockers if clean(row))
        line(pdf, f"{copy['blocker']}: {text(blocker)}", 6)
        plan = item.get("validation_plan") if isinstance(item.get("validation_plan"), dict) else {}
        if clean(plan.get("local")):
            line(pdf, f"{copy['local']}: {text(plan.get('local'))}", 6)
        if clean(plan.get("deployment")):
            line(pdf, f"{copy['owner']}: {text(plan.get('deployment'))}", 6)
        pdf.ln(1)
    coverage = report.get("coverage") if isinstance(report.get("coverage"), dict) else {}
    if any(clean(coverage.get(key)) for key in copy["coverage"]):
        pdf.ln(2)
        pdf.set_font("Report", size=14)
        line(pdf, copy["coverageTitle"], 8)
        pdf.set_font("Report", size=11)
        for key, label in copy["coverage"].items():
            line(pdf, f"{label}: {text(coverage.get(key))}", 6)
    pdf.ln(2)
    pdf.set_font("Report", size=10)
    line(pdf, copy["rejectedNote"], 5)
    if partial:
        line(pdf, copy["partial"], 5)
    pdf.ln(2)
    pdf.set_font("Report", size=9)
    line(pdf, copy["disclaimer"], 5)
    destination.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(destination))
    return counts, severity


def print_summary(counts, severity, destination):
    print(f"confirmed: {counts['confirmed']}")
    print(f"needs_validation: {counts['needs_validation']}")
    print(f"rejected: {counts['rejected']}")
    for name in SEVERITIES:
        print(f"{name}: {severity[name]}")
    print(f"pdf: {destination}")


def main():
    parser = argparse.ArgumentParser(description="Write a security-audit PDF from findings.json.")
    parser.add_argument("findings", nargs="?", type=pathlib.Path)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--font")
    parser.add_argument("--blank", action="store_true")
    args = parser.parse_args()
    if args.blank == bool(args.findings):
        die("Pass findings.json, or pass --blank with no findings file.")
    report = blank_report() if args.blank else load_report(args.findings)
    counts, severity = write_pdf(report, args.out, font_candidates(args.font))
    print_summary(counts, severity, args.out)


if __name__ == "__main__":
    main()
