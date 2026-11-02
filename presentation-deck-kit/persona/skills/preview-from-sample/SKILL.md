---
name: preview-from-sample
description: "Use when the user gives a sample image (PNG, JPEG, WebP, or GIF) to turn into deck HTML, or when the deck HTML is ready and must be shown in index.html before any PDF or PowerPoint."
---

# Prerequisites
- A reference image, or a deck HTML file that is already written.
- The Knowledge Base documents `deck-kit` and `design`, plus the matching starter/catalog pairs they list. If a sample is given and the selected pair is missing, say so and stop.
- The audience, the one message, and whether yes should also make a PowerPoint. PDF is the default.
- `scripts/build-preview.py` needs Python 3 and no other packages. Python is not guaranteed to be installed. Check, and install it first when it is missing. Chrome is for the later print, not for this preview.

# Steps
1. If the user gave one or more sample images, open each image. Record the canvas, regions, alignment, type sizes, and colors. A deck sample with no clear size uses 1920×1080.
2. Read `design` and `deck-kit`, compare the sample with all built-in styles, and choose the structurally closest complete pair. Then read that starter and its same-numbered catalog. List the chosen style, color roles, page types, and components those files actually define. Never mix pairs.
3. Write `design.md` next to the new deck before the HTML. Record the selected base style and why it is closest. Fill the neutrals and the `brand` triple from the sample. Assign further hues only when the sample has them, in the order `coral`, `sun`, `mint`, `sky`. Record the contrast and name any color you dropped. Then rebuild the sample as a new deck file copied from the selected starter, and set its `:root` and skin adjustments from that `design.md`. Use a page type and components from the selected catalog wherever they reproduce the sample. Custom CSS is only for a part those components cannot match, and it stays in that deck file. Do not edit any source starter or catalog. Do not paste the sample in as a full-page background. Do not put a hex on a slide outside `:root` or its skin block.
4. Placeholder words sit where the sample has text, at about the same length. When the user already supplied the deck's real copy, use that copy instead.
5. Check Python before the preview script. Run `python3 --version`. If that fails, try `python --version` and use it only when it reports Python 3. If neither exists, install Python 3 and check again before you continue. macOS with Homebrew: `brew install python`. Windows: `winget install Python.Python.3.12`. Otherwise install Python 3 from python.org and say which installer you used. Then, from this skill's folder, write the preview. Pass absolute paths.
   `python3 scripts/build-preview.py <deck.html> --frame 1920x1080 --out <folder>/index.html --lang <user language> --note "<one line in the user's language: this is a preview, reply yes to print>" --produces "<the PDF, and the PowerPoint if they asked for one>"`
6. Give the user the `index.html` path and stop. Do not run `build-pdf.sh` or `build-pptx.sh` in this turn. Do not render `index.html` itself.
7. A change request updates the deck HTML, runs the same preview command again, and waits.
8. When the user says yes, print immediately with `scripts/build-pdf.sh` from the make-deck skill. Same HTML, no redesign. Run `scripts/build-pptx.sh` in that same turn only when the user already asked for PowerPoint.

# Gotchas
- `index.html` is the approval screen. It is not a finished deck. The deck is finished after the PDF has been checked page by page.
- A part the kit can already express does not get a one-off layout. Match the sample by choosing the closest page and component, then adjust copy and tone.
- If the browser shows a blank frame, it blocked local iframes. Say so and open the deck HTML directly. Still wait for yes.
- Follow the print rules in `deck-kit`. No `box-shadow` on a slide.

# Output
**Deliverable** — On the preview turn: `design.md`, the deck HTML, and `index.html`. After yes: the PDF, and the PowerPoint when the user already asked for it.
**Done when** — The user has seen `index.html`, said yes, and the PDF matches that HTML with no overflow.
