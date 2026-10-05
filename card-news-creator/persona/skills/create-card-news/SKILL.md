---
name: create-card-news
description: "Use when asked to plan, design, or produce a card news carousel for Instagram or LinkedIn."
---

# Prerequisites
- Confirm the topic, audience, goal, platform, brand (name, handle, accent color, theme), CTA, and slide count. If a missing detail changes the core message or structure, ask first. For minor details, use a default and say which one you chose.
- With no brand given, keep the neutral defaults: "Brand Name", "@yourhandle", accent #5B7CFF, dark theme.
- Any slide built on a fact, statistic, or quote needs a verified source link. If you cannot find one, ask the user for a source or drop the claim.
- Read the Knowledge Base references "Card news design system" and "Card news layouts" before you design.

# Steps
1. Summarize the brief: topic, audience, goal, platform, brand, CTA, slide count, and every claim that needs a source. Ask about any gap that would change the direction before you write.
2. Pick one specific problem the reader faces, and write the core message in one sentence.
3. Research every fact in primary sources. Open each page, confirm it supports the claim, and record the full URL.
4. Write the page-by-page plan with the plan template below. Use this flow: cover → problem → cause or key explanation → solution → example or takeaway → CTA. Fill every cell. Never write "TBD".
5. Read the takeaway sentences in order. They must tell one story from the hook to the CTA. Cut or merge any page that adds nothing. Then share the plan and wait for approval. Do not write any HTML until the user approves. Apply every change to the plan first.
6. Build one HTML file per slide (slide-01.html, slide-02.html, …) from the layouts. Set the brand tokens, name, and handle once. Change only the copy, and follow card-news-style and clear-message. Each slide must match its approved plan row. For a full carousel, generate the files from a small build script with the shared CSS so edits stay easy.
7. Render every slide with the html-to-png skill and create the preview sheet. Add `--pdf` when the carousel is for LinkedIn.
8. Check the preview yourself: no title longer than two lines, no single word left alone on a line, no overlapping elements, no source block touching the footer, and no text running off the card. Fix the HTML and render again until it is clean.
9. Do a final check: one core message, a cover hook that matches the body, no periods at the end of card sentences, every slide says its takeaway clearly, and a working source link for every fact. If any product or brand claim is unconfirmed, ask the user to confirm it.
10. Deliver the HTML and PNG paths, the preview sheet, the PDF when needed, and a caption for each platform that lists the source links. Publish, schedule, or upload only when the user explicitly asks.

# Plan template
**Brief** — Core message (one sentence) · Audience · Goal · Platform · Brand (name, handle, accent, theme) · CTA · Slide count

| # | Role | Takeaway (one sentence) | Layout | Title | Body | Visual and emphasis | Source URL |
|---|---|---|---|---|---|---|---|
| 1 | Cover | What the reader gets from swiping | cover | … | Subtitle | Chip or none, which words use the accent | none |
| 2 | Problem | … | text | … | … | … | Full URL or none |
| … | … | … | … | … | … | … | … |
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
