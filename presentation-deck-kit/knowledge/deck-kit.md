---
name: "Deck kit"
description: "Page types, components, and tokens for a 16:9 deck. Copy starter.html, then snap catalog.html components into it."
aliases:
  - "deck kit"
  - "page template"
  - "components"
  - "starter"
  - "catalog"
---

# Deck kit

A 16:9 deck is one HTML file at 1920×1080. Pick a page template, then snap components into it.

| File | What it is |
| --- | --- |
| `starter.html` | Blank deck with one of each page type. Copy it to begin. It holds the master design |
| `catalog.html` | Every page template and component, with the markup to copy |

The print scripts live in the `make-deck` skill, not in this Knowledge Base.

## Page templates

Every page is a `<section class="slide">` with `data-page`. The page script at the bottom of the file gives every page the same header, footer, and page number.

| `data-page` | Use | You write |
| --- | --- | --- |
| `cover` | First page | `.cover-main` → `.cover-copy` (hero, lead, chips) + any component |
| `content` | Most pages | `.page-title` (title, lead) + `.slide-body` (components) |
| `split` | Copy + visual | `.split` → `.split-copy` + any component. `.split.reverse` flips it |
| `divider` | Section break | `.hero` + `.lead`. The big number is automatic |
| `statement` | One big message | `.statement` + optional `.lead`. Add `class="slide ink"` for dark |
| `closing` | Next steps | `.title` + `.slide-body` (glass cards, CTA) |

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

**Color:** add `.tone-brand / .tone-coral / .tone-sun / .tone-mint / .tone-sky / .tone-ink` to any component. Change the palette in `:root` inside the `<style id="deck-kit">` block.

## Rules

- Use components and tokens, not one-off styles. If something is missing, add it to the style block of `starter.html` and `catalog.html` so the next deck gets it too.
- No `box-shadow`. Chrome prints it as gray rectangles in the PDF.
- No periods at the end of sentences.
- Check every page in the PDF. Shorten copy if it overflows.

## Adding a component

1. Add the styles to the `<style id="deck-kit">` block in both `starter.html` and `catalog.html` under Components, using `var(--c)`, `var(--c-soft)`, `var(--c-deep)` for color so tones work.
2. Add a `<figure class="demo">` to `catalog.html` with the markup. The code panel and Copy button appear by themselves.

## Changing the design

`starter.html` holds the master copy of the design. A new deck copied from it carries its own copy, so later design changes do not touch finished decks. To update an existing deck, replace its `<style id="deck-kit">` block with the one from `starter.html`. Keep `catalog.html` in step the same way.
