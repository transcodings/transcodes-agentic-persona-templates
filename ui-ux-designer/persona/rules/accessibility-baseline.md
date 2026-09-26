---
description: Load when building or reviewing interactive UI, forms, dialogs, and menus
---

# Must
- Use the native element for the job — `button`, `a`, `label`, `dialog` — before reaching for ARIA.
- Keep every interaction reachable by keyboard, with a visible focus style and a logical tab order.
- Give each control an accessible name, and tie helper text and errors to it with `aria-describedby`.
- Keep text contrast at 4.5:1 and large text and interactive boundaries at 3:1.
- Trap focus inside a modal while it is open, and return focus to the trigger when it closes.

# Never
- Never attach a click handler to a `div` or `span` that behaves like a button.
- Never remove focus outlines without shipping an equally visible replacement.
- Never announce an error only through colour or only through a toast that disappears.
- Never set a positive `tabindex` — fix the DOM order instead.
