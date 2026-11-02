---
name: "Gallery design"
description: "Style 3 card news. Warm paper, cropped oxblood circle, high-contrast serif. Pair with references/style.html. Cormorant Garamond and Outfit."
aliases:
  - "design 3"
  - "style 3"
  - "gallery"
  - "poster"
  - "serif"
---

# Gallery design

Style 3 is a gallery poster. The master file is `references/style.html`. Copy that file for every slide. Replace the words. Keep the warm paper, the cropped oxblood circle, and the small plate at the lower left.

Use this pair only. Do not mix it with `post-style-index`, `post-style-nocturne`, or `post-style-paper`.

## Colors

| Token | Value | Used for |
|---|---|---|
| `paper` | `#F6F0E6` | Card background |
| `box` | `#FBF7F1` | Text that sits on the oxblood circle |
| `ink` | `#1A1612` | Title and plate text |
| `muted` | `#6A5C50` | Footer |
| `accent` | `#7A2E2A` | The circle and the small labels |
| `night` | `#1A1612` | A closing field, only when the circle expands to the whole card |
| `line` | `rgba(26,22,18,.18)` | The plate rule |

| Text / background | Contrast | Verdict |
|---|---|---|
| `ink` / `paper` | 15.9:1 | OK at any size |
| `muted` / `paper` | 5.7:1 | OK at any size |
| `accent` / `paper` | 8.2:1 | OK at any size |
| `box` / `accent` | 8.7:1 | OK at any size |

Words on the circle are `box`. Words on paper are `ink`. Do not put `ink` on the circle or `box` on the paper. No tape, no shadow, no second bright color.

## Type

Load Cormorant Garamond and Outfit. The title and the word inside the circle are Cormorant. Labels, the plate, and the footer are Outfit.

| Role | Face | Size |
|---|---|---|
| Title | Cormorant Garamond 600 | 104–120px, line-height 0.88 |
| Word on the circle | Cormorant Garamond italic 500 | 120–148px |
| Plate | Outfit 500 | 30px |
| Labels | Outfit 500 | 16–18px, uppercase, tracked |

The title on paper is two short lines. The italic word on the circle is one word.

## Composition

- The circle is 780px, starts near the horizontal center, and runs off the right edge.
- The title stays in the left 470px so it never crosses into the circle.
- The italic word and its small label sit inside the visible part of the circle.
- A narrow plate at the lower left has a hairline, a label, and one sentence. It stays left of the circle.
- The footer is a quiet uppercase row. It does not box the poster in.

## Other slides from this file

Keep the circle and the left plate.

| Slide | Change |
|---|---|
| Text | The plate holds the explanation. The circle keeps one italic word |
| Score | The circle carries the number in italic `box`. The plate says what changed |
| Steps | The plate becomes three short lines. The circle keeps the step count |
| Screen | Crop the image into the circle. The plate is the caption |
| Closing | Fill the card with `accent` and set the whole title in `box` |

No periods at the end of card sentences. A fact slide adds `.source` above the footer, in the left column only, so it does not cross the circle.
