#!/usr/bin/env python3
"""Score a landing SEO / AEO audit and write a client PDF.

Usage:
  python3 write_report_pdf.py audit.json --out report.pdf [--font PATH]

The JSON lists checks. This script owns the score. Pass counts, Fail does not,
and Unknown or Not applicable stays out of the percentage.

Weights: Tier 1 40, Tier 2 25, Tier 3 20, AEO 15.
A layer with no scored checks drops out and the remaining weights are rescaled.
"""
import argparse
import json
import pathlib
import sys

LAYERS = ("tier1", "tier2", "tier3", "aeo")
WEIGHTS = {"tier1": 40, "tier2": 25, "tier3": 20, "aeo": 15}
RESULTS = {"pass", "fail", "unknown", "na"}
IMPACT = {"high": 3, "높음": 3, "medium": 2, "중간": 2, "low": 1, "낮음": 1}

COPY = {
    "en": {
        "title": "Landing SEO / AEO report",
        "customer": "Customer",
        "url": "URL",
        "date": "Audited",
        "scope": "Scope",
        "score": "Readiness score",
        "coverage": "Scored coverage",
        "scoreChart": "Score graph",
        "countChart": "Pass, fail, and unknown",
        "pass": "Pass",
        "fail": "Fail",
        "unknown": "Unknown",
        "layers": "Layer scores",
        "fixes": "What to fix",
        "unknowns": "Needs more evidence",
        "plan": "30 / 60 / 90 days",
        "none": "None.",
        "disclaimer": "This score measures the checked items only. It is not a ranking, traffic, or answer-engine citation guarantee. Unknown items are excluded from the percentage.",
        "layer": {
            "tier1": "SEO Tier 1",
            "tier2": "SEO Tier 2",
            "tier3": "SEO Tier 3",
            "aeo": "AEO",
        },
        "grade": [(90, "Strong"), (75, "Good, with fixes"), (60, "Needs work"), (0, "Not ready")],
        "counts": "{score}/100 · {passed} pass · {failed} fail · {unknown} unknown",
        "days": (("d30", "0–30 days"), ("d60", "31–60 days"), ("d90", "61–90 days")),
    },
    "ko": {
        "title": "랜딩 SEO / AEO 보고서",
        "customer": "고객",
        "url": "URL",
        "date": "점검일",
        "scope": "범위",
        "score": "준비 점수",
        "coverage": "채점 범위",
        "scoreChart": "점수 그래프",
        "countChart": "통과 · 실패 · 미확인",
        "pass": "통과",
        "fail": "실패",
        "unknown": "미확인",
        "layers": "계층 점수",
        "fixes": "고칠 곳",
        "unknowns": "증거가 더 필요한 항목",
        "plan": "30 / 60 / 90일",
        "none": "없음",
        "disclaimer": "이 점수는 채점한 항목만 반영합니다. 검색 순위, 트래픽, 답변 엔진 인용을 보장하지 않습니다. 확인되지 않은 항목은 점수에서 뺍니다.",
        "layer": {
            "tier1": "SEO Tier 1",
            "tier2": "SEO Tier 2",
            "tier3": "SEO Tier 3",
            "aeo": "AEO",
        },
        "grade": [(90, "양호"), (75, "보완하면 좋음"), (60, "개선 필요"), (0, "준비 부족")],
        "counts": "{score}/100 · 통과 {passed} · 실패 {failed} · 미확인 {unknown}",
        "days": (("d30", "0–30일"), ("d60", "31–60일"), ("d90", "61–90일")),
    },
}


def die(message):
    sys.exit(message)


def load_audit(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        die(f"Could not read audit JSON: {error}")
    if not isinstance(data, dict) or not isinstance(data.get("checks"), list):
        die('Audit JSON needs a "checks" array.')
    checks = []
    for index, item in enumerate(data["checks"], 1):
        if not isinstance(item, dict):
            die(f"Check {index} must be an object.")
        layer = str(item.get("layer", "")).strip().lower()
        result = str(item.get("result", "")).strip().lower()
        name = str(item.get("check", "")).strip()
        if layer not in LAYERS or result not in RESULTS or not name:
            die(f"Check {index} needs layer, result, and check.")
        checks.append({**item, "layer": layer, "result": result, "check": name, "_index": index})
    data["checks"] = checks
    return data


def layer_stats(checks):
    stats = {}
    for layer in LAYERS:
        rows = [item for item in checks if item["layer"] == layer]
        passed = sum(item["result"] == "pass" for item in rows)
        failed = sum(item["result"] == "fail" for item in rows)
        unknown = sum(item["result"] == "unknown" for item in rows)
        scored = passed + failed
        score = round(100 * passed / scored) if scored else None
        applicable = scored + unknown
        coverage = round(100 * scored / applicable) if applicable else None
        stats[layer] = {
            "score": score,
            "passed": passed,
            "failed": failed,
            "unknown": unknown,
            "coverage": coverage,
        }
    return stats


def overall(stats):
    weighted = [(stats[layer]["score"], WEIGHTS[layer]) for layer in LAYERS if stats[layer]["score"] is not None]
    if not weighted:
        return None, 0
    total_weight = sum(weight for _, weight in weighted)
    score = round(sum(score * weight for score, weight in weighted) / total_weight)
    applicable = sum(
        stats[layer]["passed"] + stats[layer]["failed"] + stats[layer]["unknown"] for layer in LAYERS
    )
    scored = sum(stats[layer]["passed"] + stats[layer]["failed"] for layer in LAYERS)
    coverage = round(100 * scored / applicable) if applicable else 0
    return score, coverage


def grade_for(score, labels):
    if score is None:
        return "-"
    return next(label for threshold, label in labels if score >= threshold)


def fix_rows(checks):
    fails = [item for item in checks if item["result"] == "fail"]
    return sorted(
        fails,
        key=lambda item: (
            LAYERS.index(item["layer"]),
            -IMPACT.get(str(item.get("impact", "")).strip().lower(), 2),
            item["_index"],
        ),
    )


def font_candidates(explicit):
    if explicit:
        path = pathlib.Path(explicit)
        if not path.is_file():
            die(f"Font not found: {path}")
        return [path]
    names = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "C:/Windows/Fonts/malgun.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]
    found = [pathlib.Path(name) for name in names if pathlib.Path(name).is_file()]
    if not found:
        die("No Korean-capable font found. Pass --font with a .ttf, .otf, or .ttc path.")
    return found


def text(value):
    cleaned = " ".join(str(value or "").split())
    return cleaned or "-"


def draw_bar(pdf, label, value):
    from fpdf.enums import XPos, YPos

    height = 5
    width = 110
    y = pdf.get_y()
    if y > pdf.h - 28:
        pdf.add_page()
        y = pdf.get_y()
    pdf.set_font("Report", size=9)
    pdf.set_xy(pdf.l_margin, y)
    pdf.cell(36, height, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
    track_x = pdf.get_x()
    pdf.set_fill_color(229, 231, 235)
    pdf.rect(track_x, y, width, height, "F")
    if value is not None:
        pdf.set_fill_color(37, 99, 235)
        pdf.rect(track_x, y, width * max(0, min(value, 100)) / 100, height, "F")
        caption = str(value)
    else:
        caption = "-"
    pdf.set_xy(track_x + width + 2, y)
    pdf.cell(18, height, caption, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1.5)


def draw_counts(pdf, label, passed, failed, unknown):
    from fpdf.enums import XPos, YPos

    height = 5
    width = 110
    y = pdf.get_y()
    if y > pdf.h - 28:
        pdf.add_page()
        y = pdf.get_y()
    pdf.set_font("Report", size=9)
    pdf.set_xy(pdf.l_margin, y)
    pdf.cell(36, height, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
    track_x = pdf.get_x()
    total = passed + failed + unknown
    pdf.set_fill_color(229, 231, 235)
    pdf.rect(track_x, y, width, height, "F")
    cursor = track_x
    if total:
        for count, color in (
            (passed, (22, 163, 74)),
            (failed, (220, 38, 38)),
            (unknown, (156, 163, 175)),
        ):
            part = width * count / total
            pdf.set_fill_color(*color)
            pdf.rect(cursor, y, part, height, "F")
            cursor += part
    pdf.set_xy(track_x + width + 2, y)
    pdf.cell(28, height, f"{passed}/{failed}/{unknown}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1.5)


def line(pdf, content, height):
    from fpdf.enums import XPos, YPos

    pdf.multi_cell(0, height, content, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def use_font(pdf, candidates):
    errors = []
    for path in candidates:
        try:
            pdf.add_font("Report", fname=str(path))
            return path
        except Exception as error:
            errors.append(f"{path}: {error}")
    die("Could not load a font.\n" + "\n".join(errors))


def write_pdf(audit, destination, fonts):
    try:
        from fpdf import FPDF
    except ImportError:
        die("Install fpdf2 first: python3 -m pip install fpdf2")

    language = "ko" if str(audit.get("language", "en")).lower().startswith("ko") else "en"
    copy = COPY[language]
    stats = layer_stats(audit["checks"])
    score, coverage = overall(stats)
    grade = grade_for(score, copy["grade"])
    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=16)
    use_font(pdf, fonts)
    pdf.add_page()
    pdf.set_font("Report", size=18)
    line(pdf, copy["title"], 9)
    pdf.ln(2)
    pdf.set_font("Report", size=11)
    meta = [
        (copy["customer"], audit.get("customer")),
        (copy["url"], audit.get("url")),
        (copy["date"], audit.get("auditedAt")),
        (copy["scope"], audit.get("scope")),
    ]
    for label, value in meta:
        line(pdf, f"{label}: {text(value)}", 6)
    pdf.ln(2)
    shown = "-" if score is None else f"{score}/100 · {grade}"
    pdf.set_font("Report", size=14)
    line(pdf, f"{copy['score']}: {shown}", 8)
    pdf.set_font("Report", size=11)
    line(pdf, f"{copy['coverage']}: {coverage}%", 6)
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["scoreChart"], 8)
    draw_bar(pdf, copy["score"], score)
    for layer in LAYERS:
        draw_bar(pdf, copy["layer"][layer], stats[layer]["score"])
    if audit.get("verdict"):
        pdf.ln(1)
        pdf.set_font("Report", size=11)
        line(pdf, text(audit.get("verdict")), 6)
    pdf.ln(3)
    pdf.set_font("Report", size=14)
    line(pdf, copy["layers"], 8)
    pdf.set_font("Report", size=11)
    for layer in LAYERS:
        row = stats[layer]
        layer_score = "-" if row["score"] is None else row["score"]
        counts = copy["counts"].format(
            score=layer_score,
            passed=row["passed"],
            failed=row["failed"],
            unknown=row["unknown"],
        )
        line(pdf, f"{copy['layer'][layer]} · {counts}", 6)
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["countChart"], 8)
    pdf.set_font("Report", size=9)
    line(pdf, f"{copy['pass']} / {copy['fail']} / {copy['unknown']}", 5)
    for layer in LAYERS:
        row = stats[layer]
        draw_counts(pdf, copy["layer"][layer], row["passed"], row["failed"], row["unknown"])
    pdf.ln(3)
    pdf.set_font("Report", size=14)
    line(pdf, copy["fixes"], 8)
    pdf.set_font("Report", size=11)
    fixes = fix_rows(audit["checks"])
    if not fixes:
        line(pdf, copy["none"], 6)
    for number, item in enumerate(fixes, 1):
        impact = text(item.get("impact"))
        line(pdf, f"{number}. [{copy['layer'][item['layer']]}] {item['check']} ({impact})", 6)
        line(pdf, f"   {text(item.get('fix'))}", 6)
        line(pdf, f"   {text(item.get('evidence'))}", 6)
        pdf.ln(1)
    unknowns = [item for item in audit["checks"] if item["result"] == "unknown"]
    pdf.ln(2)
    pdf.set_font("Report", size=14)
    line(pdf, copy["unknowns"], 8)
    pdf.set_font("Report", size=11)
    if not unknowns:
        line(pdf, copy["none"], 6)
    for item in unknowns:
        line(pdf, f"- [{copy['layer'][item['layer']]}] {item['check']}: {text(item.get('evidence'))}", 6)
    plan = audit.get("plan") if isinstance(audit.get("plan"), dict) else {}
    if any(plan.get(key) for key, _ in copy["days"]):
        pdf.ln(3)
        pdf.set_font("Report", size=14)
        line(pdf, copy["plan"], 8)
        pdf.set_font("Report", size=11)
        for key, label in copy["days"]:
            items = plan.get(key) or []
            body = "; ".join(text(item) for item in items) if isinstance(items, list) and items else copy["none"]
            line(pdf, f"{label}: {body}", 6)
    pdf.ln(4)
    pdf.set_font("Report", size=9)
    line(pdf, copy["disclaimer"], 5)
    destination.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(destination))
    return score, grade, coverage, len(fixes), len(unknowns)


def main():
    parser = argparse.ArgumentParser(description="Write a scored landing SEO / AEO PDF report.")
    parser.add_argument("audit", type=pathlib.Path)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--font")
    args = parser.parse_args()
    audit = load_audit(args.audit)
    score, grade, coverage, fixes, unknowns = write_pdf(audit, args.out, font_candidates(args.font))
    print(f"score: {score if score is not None else '-'}")
    print(f"grade: {grade}")
    print(f"coverage: {coverage}%")
    print(f"fixes: {fixes}")
    print(f"unknowns: {unknowns}")
    print(f"pdf: {args.out}")


if __name__ == "__main__":
    main()
