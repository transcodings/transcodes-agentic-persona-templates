---
name: use-the-deck-kit
description: Build every deck from one template skill. Do not mix template skills or invent a second slide system.
---
# Must
- Read the Knowledge Base document `sample` first. Choose one template skill, then read its `references/deck-kit.md` and `references/design.md`, and copy its `references/starter.html` and `references/catalog.html`.
- Use the style the user names. Otherwise choose the closest template skill and state it. A sample image takes priority: choose the structurally closest template skill before adapting its tokens.
- Copy the complete page composition from the selected skill. The template skills intentionally use different markup, information hierarchy, and decorative placement; do not reduce them to one shared layout with different colors.
- Reuse the page templates, markup, attributes, and components that those files actually use.
- Color components with the roles in `design`. Read the token names from that document. Do not substitute a remembered name.
- When the user gives a reference image, match it through preview-from-sample. Write `design.md` for that deck before the HTML. Prefer the kit page and component that reproduce it. Custom CSS stays in the new deck file.

# Never
- Never mix `ppt-style-swiss` with `ppt-style-night` or any other template skill.
- Never write a one-off slide layout when a page and component in the selected catalog already fit.
- Never treat a filename, class, attribute, page type, or color name from memory as the current kit.
- Never edit a template skill while making one deck. Add a missing component to that skill only when the user asks to extend the kit.
- Never replace the kit with another deck framework.
