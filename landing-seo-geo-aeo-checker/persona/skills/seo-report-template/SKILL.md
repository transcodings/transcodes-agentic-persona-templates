---
name: seo-report-template
description: "Use when writing the SEO, GEO, and AEO report PDF. The blank layout is references/report-template.pdf. scripts/write_report_pdf.py scores the audit JSON and writes the customer PDF. Do not edit the files in this skill."
---

# seo-report-template

Open this skill when the audit needs a PDF. This skill holds the blank template and the script that fills it. Do not edit either file in this skill.

1. Read `references/report-template.md` for the description line and the keywords. `references/report-template.pdf` is the blank layout.
2. From this skill folder, run `python3 scripts/write_report_pdf.py <audit.json> --out <customer>-seo-geo-aeo-report.pdf`. Install `fpdf2` if the script asks for it. Pass `--font` only when it cannot find a Korean-capable font. The script owns the score.
3. Save that finished PDF, and the same description and keywords, into the linked Knowledge Base. A layer the script did not score is `0`. Do not replace `references/report-template.pdf`.
