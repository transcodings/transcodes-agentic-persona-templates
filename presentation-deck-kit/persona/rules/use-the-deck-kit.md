---
name: use-the-deck-kit
description: Build every deck from starter.html and catalog.html in the Knowledge Base. Do not invent a new slide stylesheet or assume their names.
---
# Must
- Read the Knowledge Base documents `deck-kit` and `design` first, then `starter.html` and `catalog.html`. Start from a copy of `starter.html`.
- Reuse the page templates, markup, attributes, and components that those files actually use.
- Color components with the roles in `design`. Read the token names from that document. Do not substitute a remembered name.
- When the user gives a reference image, match it through preview-from-sample. Write `design.md` for that deck before the HTML. Prefer the kit page and component that reproduce it. Custom CSS stays in the new deck file.

# Never
- Never write a one-off slide layout when a page and component in `catalog.html` already fit.
- Never treat a filename, class, attribute, page type, or color name from memory as the current kit.
- Never edit `starter.html` or `catalog.html` while making one deck. Add a missing component to those files only when the user asks to extend the kit.
- Never replace the kit with another deck framework.
