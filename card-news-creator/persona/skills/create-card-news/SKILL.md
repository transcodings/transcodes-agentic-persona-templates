---
name: create-card-news
description: "Use when asked to plan, design, or produce a card news carousel for Instagram or LinkedIn."
---

# Prerequisites
- Confirm the topic, audience, goal, platform, brand (name, handle, accent color, theme), CTA, and slide count. If a missing detail changes the core message or structure, ask first. For minor details, use a default and say which one you chose.
- With no brand and no named style, use Paper: the `post-style-paper` skill. If the user names Index, Nocturne, or Gallery, or asks for a different look, use `post-style-index`, `post-style-nocturne`, or `post-style-gallery`. Do not mix skills.
- Any slide built on a fact, statistic, or quote needs a verified source link. If you cannot find one, ask the user for a source or drop the claim.
- Read `references/design.md` in the chosen template skill. Copy that skill's HTML, then change the words. For `post-style-index`, `post-style-nocturne`, and `post-style-gallery`, use the slide recipes in `references/design.md`. For `post-style-paper`, copy the `.card` in `references/style.html` whose `data-layout` matches the slide.

# Steps
1. Summarize the brief: topic, audience, goal, platform, brand, CTA, slide count, and every claim that needs a source. Ask about any gap that would change the direction before you write.
2. Pick one specific problem the reader faces, and write the core message in one sentence.
3. Research every fact in primary sources. Open each page, confirm it supports the claim, and record the full URL.
4. Write the page-by-page plan with the plan template below. Use this flow: cover → problem → cause or key explanation → solution → example or takeaway → CTA. Fill every cell. Never write "TBD".
5. Read the takeaway sentences in order. They must tell one story from the hook to the CTA. Cut or merge any page that adds nothing. Then share the plan and wait for approval. Do not write any HTML until the user approves. Apply every change to the plan first.
6. Build one HTML file per slide (slide-01.html, slide-02.html, …), fixed at 1080×1350. If the user gave a reference image, build the HTML the way preview-from-sample describes in its steps 1–4. Otherwise copy the chosen template skill's HTML and change only the words. `post-style-paper` copies one `.card` from `references/style.html`, the one whose `data-layout` matches that row, plus its style block. The other three post styles copy `references/style.html` and follow the slide recipe in `references/design.md`. Each slide must match its approved plan row. Do not show index.html until step 7.
7. Show index.html with the preview-from-sample skill and wait for yes. Do not render in this turn.
8. On yes, render every slide with the html-to-png skill and create the preview sheet. Add `--pdf` when the carousel is for LinkedIn. Use the HTML the user just approved.
9. Check the preview yourself: a `post-style-paper` title is no longer than two lines, the other post styles stay inside their design document, no single word is left alone on a line, nothing overlaps by accident, the source block does not touch the footer, and no text runs off the card. Fix the HTML, show index.html again, and render again only after the next yes.
10. Do a final check: one core message, a cover hook that matches the body, no periods at the end of card sentences, every slide says its takeaway clearly, and a working source link for every fact. If any product or brand claim is unconfirmed, ask the user to confirm it.
11. Deliver the HTML and PNG paths, the preview sheet, the PDF when needed, and a caption for each platform that lists the source links. Publish, schedule, or upload only when the user explicitly asks.

# Plan template
**Brief** — Core message (one sentence) · Audience · Goal · Platform · Brand (name, handle, accent, theme) · Template (`post-style-index` Index, `post-style-nocturne` Nocturne, `post-style-gallery` Gallery, or `post-style-paper` Paper) · CTA · Slide count

**Layouts** — Use one of these keywords in the Layout column. In `post-style-paper`, copy the `.card` in `references/style.html` with that `data-layout`.

| Layout | Use when |
|---|---|
| cover | The opening hook |
| text | A problem, cause, or explanation |
| score | A before-and-after number |
| steps | A short how-to |
| screen | A real screen |
| cta | The last slide: what the reader should do next |

| # | Role | Takeaway (one sentence) | Layout | Title | Body | Visual and emphasis | Source URL |
|---|---|---|---|---|---|---|---|
| 1 | Cover | What the reader gets from swiping | cover | … | Subtitle | Chip or none, which words use the accent | none |
| 2 | Problem | … | text | … | … | … | Full URL or none |
| … | Score, steps, or screen | … | score, steps, or screen | … | … | … | Full URL or none |
| N | CTA | What the reader should do next | cta | … | … | … | none |

**Flow check** — The takeaways in order, joined with →, in one line.

# Gotchas
- Too many points turn the carousel into a manual. Keep only what supports the one core message.
- Links in Instagram captions are not clickable. Still write each source as a full URL so readers can copy it. On LinkedIn, put the sources in the post text.
- Platform limits on slide count and file size change over time. Check the platform's current help page before you promise a number.
- Signed or temporary image URLs expire. If a scheduler needs image URLs, make sure they stay valid until the post goes live.

# Output
**Deliverable** — The approved page-by-page plan, one HTML file per slide, the rendered PNGs, the preview sheet (preview-all.png), carousel.pdf for LinkedIn when needed, and a caption with the source links. Every fact slide shows its full source URL.
**Done when** — The carousel keeps one core message, flows from the cover hook to the CTA, matches the approved plan, follows the templates, card-news-style, and clear-message, renders with no line break, overlap, or overflow problems, and every fact carries a verified link or has been removed.
