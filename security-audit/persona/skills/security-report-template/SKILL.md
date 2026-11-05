---
name: security-report-template
description: "Use when a security audit needs its PDF. The blank layout is references/report-template.pdf. scripts/write_report_pdf.py reads findings.json and writes the customer PDF. Do not edit the files in this skill."
---

# security-report-template

Open this skill after `findings.json` is final. This skill holds the blank security-audit report and the script that fills it. Do not edit either file in this skill.

1. Read `references/report-template.md` for the description line and the keywords. `references/report-template.pdf` is the blank layout.
2. From this skill folder, run `python3 scripts/write_report_pdf.py <findings.json> --out <target>-security-audit-report.pdf`. Install `fpdf2` if the script asks for it. Pass `--font` only when it cannot find a font. The PDF is English. Write finding text in English before running it.
3. Use the counts the script prints. Confirmed findings keep the severity already in `findings.json`. Needs-validation items stay without a severity. Rejected records are counts only, not findings. Do not invent a score.
4. Save that finished PDF in the linked Knowledge Base with the description and keywords from the script. Do not replace `references/report-template.pdf`.
