---
name: html-to-png
description: "Use when HTML files such as card news slides need to be converted to PNG images or a LinkedIn PDF, or when an HTML design needs to be rendered and previewed as an image."
---

# Prerequisites
- Confirm the path to the HTML file or the folder that holds the HTML files.
- Confirm the output size. If none is given, use the card news default of 1080×1350.
- Python 3, Pillow (`pip install pillow`), and Google Chrome or Chromium must be installed. The templates load Google Fonts, so an internet connection is required.

# Steps
1. Run scripts/render.py from this skill's folder.
   - Whole folder: `python3 scripts/render.py <folder> --sheet`
   - Selected files: `python3 scripts/render.py slide-01.html slide-02.html`
   - LinkedIn PDF: add `--pdf` to also write carousel.pdf, one page per slide in file name order
   - Save to another folder: `--out <folder>` · Different size: `--size 1080x1080`
2. The script writes a PNG with the same name next to each HTML file (or into the --out folder) and prints whether each image matches the requested size. With --sheet, it also writes preview-all.png.
3. If the output shows a WARNING, check that the html and body size in the HTML matches the output size.
4. Open preview-all.png or the individual PNGs and check that the fonts loaded and that no text overflows or overlaps.
5. If anything is wrong, fix the HTML and run the same command again.

# Gotchas
- If the text renders in a default font, the web fonts failed to load. Check the internet connection and run the script again.
- The HTML must use a fixed px layout. Responsive layouts render differently from what you intended.
- Name slides so they sort in order (slide-01, slide-02, …). The PDF and the preview sheet follow file name order.
- The script overwrites files with the same name. Use --out to write to a different folder when you need to keep earlier images.

# Output
**Deliverable** — One PNG per HTML file, the preview-all.png sheet and carousel.pdf when requested, and the list of generated file paths.
**Done when** — Every PNG matches the requested size, and the preview shows no font, line break, or overlap problems.
