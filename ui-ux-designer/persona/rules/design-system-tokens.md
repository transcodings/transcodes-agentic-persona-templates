---
description: Load when styling components or adjusting spacing, colour, or typography
---

# Must
- Use design tokens for colour, spacing, radius, and typography so themes and density changes propagate.
- Compose from the shared component library, and extend a component in one place when it falls short.
- Keep spacing on the defined scale so vertical rhythm stays consistent across screens.
- Support both light and dark themes whenever the product ships both.

# Never
- Never hardcode a hex colour, pixel spacing value, or font size that a token already covers.
- Never fork a shared component to change one detail — add the variant to the component itself.
- Never convey state through colour alone; pair it with an icon, label, or text.
