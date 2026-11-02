---
name: card-news-style
description: Build every slide from the matching Knowledge Base layout, design tokens, and the linked design document.
---
# Must
- Build every slide by copying the Knowledge Base HTML whose description and keywords match the slide. Keep the 1080×1350 size. Colors and the font come from the linked document "card news design". When the user gives a reference image, follow preview-from-sample: write `design.md` with those same roles filled from the sample, then match the image. If that image is not 1080×1350, use its size and say so.
- Set the brand once through the tokens (`--accent`, `--accent-text`) and the brand name in the header. Use the paper background unless the slide is the CTA, which is the black cover.
- Put the dotted line and page number at the top of every slide except the cover. Keep the footer the same on every slide.
- On any slide that states a fact or quotes a source, put the full source URL in the SOURCE block above the footer.
- Keep each carousel to 10 slides or fewer unless the user asks for more.
- Keep titles to two lines at 96px. Shorten the copy or move the line break when a title runs longer.

# Never
- Never add chips or decorative labels that carry no meaning. Use a chip only when it tells the reader something, such as "Beginner".
- Never introduce colors, fonts, or layouts outside the tokens and templates, except to match a reference image the user supplied for this job.
