---
description: Load when adding assets, scripts, fonts, or third-party embeds to a public page
---

# Must
- Serve images through the framework image component with explicit dimensions, and prefer AVIF or WebP.
- Keep Largest Contentful Paint under 2.5s and Cumulative Layout Shift under 0.1 on a throttled mobile profile.
- Self-host fonts with `font-display: swap` and subset them to the character sets actually rendered.
- Load anything non-critical — chat widgets, analytics, video players — lazily or after interaction.

# Never
- Never add a third-party script to the critical path without measuring its effect on LCP first.
- Never render above-the-fold content only on the client when it can be server-rendered.
- Never ship an unoptimized hero image; resize and compress it before committing.
