---
name: make-deck
description: 'Build a presentation with the Deck Kit. Use for a deck, slides, a pitch, a PDF deck, or a PowerPoint'
---

# Prerequisites

- The Deck Kit folder. If you cannot find it, ask for the path and stop.
- The audience, the one message of the deck, and whether the user wants a PDF, a PowerPoint, or both.
- The tools named by the kit's own print scripts.

# Steps

1. Read the kit folder, including its readme. Identify the component catalog, the blank deck, and the print scripts from their contents. List the page types and components those files actually define. Do not design from memory, and do not assume a filename.
2. Write a short page plan: page number, the page type named in the kit, the one job of that page, and the components you will snap in. Build when the brief is enough. Ask first when the message or the page count would change the deck.
3. Copy the blank deck to a new file name the user gave, or a new deck file in the folder they chose. Do not overwrite the blank deck.
4. Set brand, URL, company, and logo the way the blank deck already does. Add a logo only for a logo file the user supplied.
5. Keep the pages the plan needs. Duplicate a page section for each extra page. Put components in the region that page type uses in the kit.
6. Run the kit's PDF script. Open the PDF and check every page for overflow, overlap, and cut-off text. Fix the HTML and print again until each page fits.
7. When the user wants PowerPoint, run the kit's PowerPoint script. Follow the font and tool notes printed in that script.

# Gotchas

- A deck copied from the blank deck keeps its own design block. Replacing that block with the current blank deck's design is how you refresh an old deck. Do not do it unless the user asks.
- Follow the kit's print rules. If a script says a tool or a font is missing, say so and stop.
- A first-run install belongs to the kit's converter, not to the deck file.
- Read the PowerPoint script for what stays editable and what becomes a picture.

# Output

**Deliverable** — The deck HTML, the PDF, the PowerPoint when requested, and the page plan you built.
**Done when** — Every page uses a page type from the kit you read, the PDF has been checked page by page, no page overflows, and no deck sentence ends with a period.
