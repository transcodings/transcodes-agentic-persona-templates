---
name: use-the-deck-kit
description: Build every deck from one matching starter/catalog style pair in the Knowledge Base. Do not mix styles or invent a second slide system.
---
# Must
- Read the Knowledge Base documents `deck-kit` and `design` first. Choose a style, then read and copy that style's starter and use its matching catalog.
- Use the style the user names. Otherwise choose the closest fit and state it. A sample image takes priority: choose the structurally closest built-in style before adapting its tokens.
- Copy the complete page composition from the selected style. The numbered styles intentionally use different markup, information hierarchy, and decorative placement; do not reduce them to one shared layout with different colors.
- Reuse the page templates, markup, attributes, and components that those files actually use.
- Color components with the roles in `design`. Read the token names from that document. Do not substitute a remembered name.
- When the user gives a reference image, match it through preview-from-sample. Write `design.md` for that deck before the HTML. Prefer the kit page and component that reproduce it. Custom CSS stays in the new deck file.

# Never
- Never mix `starter-1.html` with `catalog-2.html` or any other mismatched pair.
- Never write a one-off slide layout when a page and component in the selected catalog already fit.
- Never treat a filename, class, attribute, page type, or color name from memory as the current kit.
- Never edit a source starter or catalog while making one deck. Add a missing component to a matching pair only when the user asks to extend the kit.
- Never replace the kit with another deck framework.
