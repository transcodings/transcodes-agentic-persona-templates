---
name: card-news-style
description: Build every slide from one template skill, using the HTML and design file in its references folder.
---
# Must
- Choose one template skill for the whole carousel. The default is Paper: `post-style-paper`. Index is `post-style-index`. Nocturne is `post-style-nocturne`. Gallery is `post-style-gallery`. Use the skill the user names. When they ask for another look, choose the closest of Index, Nocturne, or Gallery and say which one.
- Build every slide by copying the HTML in that skill's `references/` folder. Keep the 1080×1350 size. Colors and the font come from that skill's `references/design.md`. When the user gives a reference image, follow preview-from-sample: start from the closest template skill, write `design.md` with that skill's roles filled from the sample, then match the image. If that image is not 1080×1350, use its size and say so.
- Set the brand once through the tokens and the brand name in the header. On `post-style-paper`, use the paper background unless the slide is the CTA. On the other post styles, follow that design document's closing treatment.
- On `post-style-paper`, put the dotted line and page number at the top of every slide except the cover. On the other post styles, keep the chrome that its design document describes. Keep the footer the same on every slide in the carousel.
- On any slide that states a fact or quotes a source, put the full source URL in the SOURCE block above the footer.
- Keep each carousel to 10 slides or fewer unless the user asks for more.
- On `post-style-paper`, keep titles to two lines at 96px. On the other post styles, follow the line count and size in that design document. Shorten the copy when a title runs past that limit.

# Never
- Never add chips or decorative labels that carry no meaning. Use a chip only when it tells the reader something, such as "Beginner".
- Never introduce colors, fonts, or layouts outside the chosen system's tokens and template, except to match a reference image the user supplied for this job.
- Never mix paper, Index, Nocturne, and Gallery in one carousel.
