---
name: make-deck
description: 'Build a presentation from the Deck Kit Knowledge Base. Use for a deck, slides, a pitch, a PDF deck, or a PowerPoint'
---

# Prerequisites

- The Knowledge Base documents `deck-kit` and `design`, plus the content files `starter.html` and `catalog.html`. If they are missing, say so and stop.
- The audience, the one message of the deck, and whether the user wants a PDF, a PowerPoint, or both.
- Google Chrome for `scripts/build-pdf.sh`. Node.js 18+ and Chrome for `scripts/build-pptx.sh`. The PowerPoint script installs its packages into `scripts/tools/` on the first run.

# Steps

1. Read `design`, `deck-kit`, `starter.html`, and `catalog.html`. List the color roles, page types, and components those files actually define. Do not design from memory, and do not assume a filename.
2. Write a short page plan: page number, the page type named in `deck-kit`, the one job of that page, and the components you will snap in. Build when the brief is enough. Ask first when the message or the page count would change the deck.
3. If the user gave a reference image, build the deck HTML the way preview-from-sample describes in its steps 1–4. Otherwise copy `starter.html` to a new file name the user gave, or a new deck file in the folder they chose. Do not overwrite `starter.html`. Do not show index.html until step 6.
4. Set brand, URL, company, and logo the way `starter.html` already does. Add a logo only for a logo file the user supplied.
5. Keep the pages the plan needs. Duplicate a page section for each extra page. Put components in the region that page type uses. Copy the markup from `catalog.html`.
6. Show index.html with the preview-from-sample skill and wait for yes. Do not print in this turn.
7. On yes, from this skill's folder, run `scripts/build-pdf.sh <deck.html> <deck.pdf>`. Pass absolute paths. Open the PDF and check every page for overflow, overlap, and cut-off text. Fix the HTML, show index.html again, and print again only after the next yes.
8. When the user wants PowerPoint, run `scripts/build-pptx.sh <deck.html> <deck.pptx>` from this skill's folder in the same turn as the PDF. Follow the font and tool notes printed in that script.

# Gotchas

- A deck copied from `starter.html` keeps its own design block. Replacing that block with the current `starter.html` design is how you refresh an old deck. Do not do it unless the user asks.
- Follow the print rules in `deck-kit`. If a script says a tool or a font is missing, say so and stop.
- A first-run install belongs to `scripts/tools/`, not to the deck file.
- Read `scripts/build-pptx.sh` for what stays editable and what becomes a picture.

# Output

**Deliverable** — The deck HTML, the PDF, the PowerPoint when requested, and the page plan you built.
**Done when** — The user said yes to index.html, every page uses a page type from `deck-kit`, the PDF has been checked page by page, no page overflows, and no deck sentence ends with a period.
