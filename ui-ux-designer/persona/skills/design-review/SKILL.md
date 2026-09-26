---
name: design-review
description: Review a screen or component against the design system and accessibility baseline — use when asked to "review this UI", "polish this screen", or "check the design".
---

# Prerequisites
- The screen, route, or component to review, and the flow it belongs to.
- The design tokens and component library available in this repo.
- The intended breakpoints and whether dark mode is in scope.

# Steps
1. Read the component and note every hardcoded value that a token already covers.
2. Walk the state set — empty, loading, partial, error, permission-denied — and list the ones that are missing or unstyled.
3. Check hierarchy and rhythm: is the primary action obvious, and does spacing follow the scale?
4. Run the accessibility pass: keyboard traversal, focus visibility, accessible names, contrast, and focus handling in overlays.
5. Review the interface copy for labels and error messages that tell the user what to do next.
6. Report findings grouped as blocking, should-fix, and polish, each with the concrete change to make.

# Gotchas
- A component can look correct and still be unreachable by keyboard — always traverse it with Tab and Enter.
- Contrast measured on the design mock can fail in dark mode; check both themes.
- Truncation hides real content: test with the longest realistic string, not the placeholder.

# Output
**Deliverable** — A findings list grouped by severity, each item naming the file, the problem, and the specific fix.
**Done when** — Every blocking item has a concrete fix, all states are accounted for, and no hardcoded value remains where a token exists.
