---
name: card-news-style
description: Build every slide from the matching Knowledge Base layout, design tokens, and the linked design document.
---
# Must
- Choose one visual system for the whole carousel. The default is Paper: `style-4.html` with `design-4.md`. Index is `style-1.html` with `design-1.md`. Nocturne is `style-2.html` with `design-2.md`. Gallery is `style-3.html` with `design-3.md`. Use the system the user names. When they ask for another look, choose the closest of Index, Nocturne, or Gallery and say which one.
- Build every slide by copying the Knowledge Base HTML from that one system. Keep the 1080×1350 size. Colors and the font come from its paired design document. When the user gives a reference image, follow preview-from-sample: start from the closest system, write `design.md` with that system's roles filled from the sample, then match the image. If that image is not 1080×1350, use its size and say so.
- Set the brand once through the tokens and the brand name in the header. On style 4, use the paper background unless the slide is the CTA. On styles 1–3, follow that design document's closing treatment.
- On style 4, put the dotted line and page number at the top of every slide except the cover. On styles 1–3, keep the chrome that its design document describes. Keep the footer the same on every slide in the carousel.
- On any slide that states a fact or quotes a source, put the full source URL in the SOURCE block above the footer.
- Keep each carousel to 10 slides or fewer unless the user asks for more.
- On style 4, keep titles to two lines at 96px. On styles 1–3, follow the line count and size in that design document. Shorten the copy when a title runs past that limit.

# Never
- Never add chips or decorative labels that carry no meaning. Use a chip only when it tells the reader something, such as "Beginner".
- Never introduce colors, fonts, or layouts outside the chosen system's tokens and template, except to match a reference image the user supplied for this job.
- Never mix paper, Index, Nocturne, and Gallery in one carousel.
