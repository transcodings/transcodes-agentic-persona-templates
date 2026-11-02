---
name: "Deck kit"
description: "Page types, components, tokens, and three visual styles for a 16:9 deck. Always use a matching starter/catalog pair."
aliases:
  - "deck kit"
  - "page template"
  - "components"
  - "starter"
  - "catalog"
---

# Deck kit

A 16:9 deck is one HTML file at 1920×1080. Pick a page template, then snap components into it.

| Skill | What it is |
| --- | --- |
| `ppt-style-neutral` | Original neutral kit. `references/starter.html` and `references/catalog.html` |
| `ppt-style-swiss` | **Swiss Grid** — strict black rules, red signal color, square editorial geometry |
| `ppt-style-night` | **Night Console** — dark technical surfaces, cyan signals, compact data-room geometry |
| `ppt-style-atelier` | **Paper Atelier** — warm paper, serif display type, soft organic editorial forms |

Choose one template skill before planning pages. Use the style the user names. If they do not name one, choose the closest fit and state the choice. A reference sample takes priority: pick the structurally closest skill, then adapt its tokens in the new deck. Never copy components from a different template skill.

The print scripts live in the `make-deck` skill.

## Page templates

Every page is a `<section class="slide">` with `data-page`. The page script at the bottom of the file gives every page the same header, footer, and page number. The six page purposes are shared, but their internal markup and composition are deliberately different in each numbered catalog. Copy the complete page composition from the selected catalog; do not rebuild it from a generic remembered structure.

| `data-page` | Use | Composition |
| --- | --- | --- |
| `cover` | First page | Signature opening composition from the selected style |
| `content` | Most pages | Style-specific information architecture for evidence and metrics |
| `split` | Copy + visual | Style-specific relationship between narrative and visual content |
| `divider` | Section break | Signature chapter geometry; number may be automatic or placed by the composition |
| `statement` | One big message | A single point of view in the selected style's framing device |
| `closing` | Next steps | Style-specific invitation, actions, and contact |

Page attributes:

- `data-section="Persona"` top-left label
- `data-tag="Setup"` top-right tag
- `data-tone="mint"` color for the tag, `<em>`, and components. On dividers it sets the background (`brand`, `mint`, `coral`, `sky`, `sun`, `ink`)
- `data-no-head`, `data-no-foot`, `data-no-deco` turn a part off for one page
- On `<html>`: `data-brand`, `data-url`, `data-company` change the header and footer text for the whole deck. Add `data-logo="path/to/logo.svg"` to show a logo image next to the brand name

## Components

| Group | Classes |
| --- | --- |
| Layout | `.grid .c2 .c3 .c4 .c5`, `style="--cols: 1.4fr 1fr"`, `.span-2`, `.stack`, `.row`, `.between`, `.fill`, `.to-bottom`, `.gap-s/m/l/xl`, `.mt-s/m/l` |
| Text | `.hero .title .h3 .lead .text .small .eyebrow`, `<em>` for highlight |
| Basics | `.tag`, `.chip` (`.on`, optional `<img>`), `.ico`, `.logo-tile`, `.dot` |
| Cards | `.card` (`.soft .solid .dash .glass .tight`), `.card-kicker .card-title .card-text .card-big .card-foot` |
| Numbers | `.stat`, `.bars > .bar`, `.meter` |
| Tables | `table.table` (`.compact .zebra`), `.hl` column, marks `.yes .no .part` |
| Lists | `ul.checks` (`.x`), `ul.bullets`, `dl.kv` |
| Flows | `ol.steps` (`.v`), `.flow`, `ol.timeline` (`li.next`) |
| Story | `.quote`, `.callout`, `.chat .bubble.q/.a .source`, `.vs`, `.card.plan`, `.person`, `.sticker` |
| Screens | `.window` (side nav, fields, rows, buttons), `.shot` for real screenshots |
| Decoration | `i.deco` (`.circle .square .ring`, `.tl .tr .bl .br`, `--size`, `--turn`) |

**Color:** the roles, the contrast, and how a sample fills them are in `references/design.md`. On a component, add `.tone-brand / .tone-coral / .tone-sun / .tone-mint / .tone-sky / .tone-ink`. The values live in `:root` inside the `<style id="deck-kit">` block.

## Rules

- Use components and tokens, not one-off styles. If something is missing, add it to this skill's starter and catalog so the next deck in that style gets it too.
- No `box-shadow`. Chrome prints it as gray rectangles in the PDF.
- No periods at the end of sentences.
- Check every page in the PDF. Shorten copy if it overflows.

## Adding a component

1. Add the styles to the `<style id="deck-kit">` block in this skill's `references/starter.html` and `references/catalog.html` under Components, using `var(--c)`, `var(--c-soft)`, `var(--c-deep)` for color so tones work.
2. Add a `<figure class="demo">` to this skill's `references/catalog.html` with the markup. The code panel and Copy button appear by themselves.

## Changing the design

Each starter holds the master copy of one design. A new deck copied from it carries its own copy, so later kit changes do not touch finished decks. To update an existing deck, replace its `<style id="deck-kit">` and `<style id="deck-skin-*">` blocks from this skill's `references/starter.html`. Keep `references/catalog.html` in step.
