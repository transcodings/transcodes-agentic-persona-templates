---
name: preview-from-sample
description: "Use when the user gives a sample image (PNG, JPEG, WebP, or GIF) to turn into an HTML template, or when slide HTML is ready and must be shown in index.html before any PNG or PDF."
---

# Prerequisites
- A reference image, or slide HTML that is already written.
- For a carousel, the approved page-by-page plan from create-card-news. A template made only from a sample does not need that plan.
- `scripts/build-preview.py` needs Python 3 and no other packages. Python is not guaranteed to be installed. Check, and install it first when it is missing.

# Steps
1. If the user gave one or more sample images, open each image. Record its pixel size, the regions (header, title, body, figures, footer), alignment, gaps, colors, and type sizes relative to the canvas.
2. Compare the sample with the four template skills. Start from the closest one and name it. Paper is `post-style-paper`, Index is `post-style-index`, Nocturne is `post-style-nocturne`, and Gallery is `post-style-gallery`. Write `design.md` before the HTML, using that skill's color roles in `references/design.md`. Record the contrast and name any color you dropped. Then write one self-contained HTML file per distinct layout, copied from that skill's `references/style.html`. The canvas is the sample's pixel size. A card sample with no clear size uses 1080×1350. The `:root` block is a copy of that `design.md`. Text is real HTML text, with line breaks that match the sample. Keep the chosen composition. Do not paste the sample in as a background of the whole card. Do not put a hex on a slide outside `:root`.
3. Save that file as the reusable template. Placeholder words sit in the same places, and at about the same length, as the sample. Leave the template skills unchanged.
4. When a carousel plan is approved, fill `slide-01.html`, `slide-02.html`, and the rest from that template. Change the words. Keep the layout taken from the sample.
5. Check Python before the preview script. Run `python3 --version`. If that fails, try `python --version` and use it only when it reports Python 3. If neither exists, install Python 3 and check again before you continue. macOS with Homebrew: `brew install python`. Windows: `winget install Python.Python.3.12`. Otherwise install Python 3 from python.org and say which installer you used. Then, from this skill's folder, write the preview. Pass absolute paths. Use the real canvas for `--frame` when it is not 1080×1350.
   `python3 scripts/build-preview.py <slide or template html> --frame 1080x1350 --out <folder>/index.html --lang <user language> --note "<one line in the user's language: this is a preview, reply yes to render>" --produces "<what yes will create>"`
   For a LinkedIn carousel, `--produces` names the PNG files, `preview-all.png`, and `carousel.pdf`. Otherwise name the PNG files and `preview-all.png`.
6. Give the user the `index.html` path and stop. Do not run the html-to-png skill in this turn. Do not render `index.html` itself.
7. A change request updates the slide HTML, runs the same preview command again, and waits.
8. When the user says yes, render immediately with the html-to-png skill. Same HTML, no redesign. Add `--sheet`. Add `--pdf` when the carousel is for LinkedIn.

# Gotchas
- `index.html` is the approval screen. It is not a slide, and it is not a Knowledge Base file.
- Words painted inside the sample become placeholder copy in the template. They are not carousel claims unless the user asked to keep them.
- If the browser shows blank frames, it blocked local iframes. Say so and open the slide HTML files directly. Still wait for yes.

# Output
**Deliverable** — On the preview turn: `design.md`, the template HTML, the slide HTML, and `index.html`. After yes: the PNGs, `preview-all.png`, and `carousel.pdf` when the carousel is for LinkedIn.
**Done when** — The user has seen `index.html`, said yes, and the rendered files match that HTML.
