---
name: print-safe-pages
description: Keep every page printable. Check the PDF before delivery.
---
# Must
- Show index.html from the preview-from-sample skill and wait for yes before printing.
- Print with `scripts/build-pdf.sh` from the `make-deck` skill and inspect every page before you deliver the deck.
- Shorten or split a page whose copy overflows the frame size the kit uses.
- Keep the header, footer, and page number that the kit page script adds, unless that kit shows how to turn a part off for one page.

# Never
- Never use a style the selected template skill's `references/deck-kit.md` or `references/starter.html` says will print badly.
- Never run `build-pdf.sh` or `build-pptx.sh` in the same turn as the first index.html preview.
- Never deliver the HTML alone and call the deck finished. index.html is a preview.
- Never claim a page fits without looking at the printed PDF.
