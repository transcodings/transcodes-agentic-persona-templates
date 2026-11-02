---
name: "Nocturne design"
description: "Style 2 card news. Warm black field, ivory serif, antique gold. Pair with references/style.html. Fraunces and Outfit."
aliases:
  - "design 2"
  - "style 2"
  - "nocturne"
  - "dark"
  - "serif"
---

# Nocturne design

Style 2 is a dark editorial card. The master file is `references/style.html`. Copy that file for every slide. Replace the words. Keep the warm black field, the cropped folio number, the serif title, and the gold rule in the lower third.

Use this pair only. Do not mix it with `post-style-index`, `post-style-gallery`, or `post-style-paper`.

## Colors

| Token | Value | Used for |
|---|---|---|
| `paper` | `#100E0C` | Card background |
| `box` | `#1B1815` | A panel only when a slide needs a second surface |
| `ink` | `#F6F1E8` | Main text |
| `muted` | `#C8B8A6` | Header, footer, and secondary text |
| `accent` | `#E0C27A` | One italic word, the lower rule, and the small labels |
| `night` | `#100E0C` | Same field. This style does not switch to a light closing slide |
| `line` | `rgba(246,241,232,.24)` | The top hairline |

| Text / background | Contrast | Verdict |
|---|---|---|
| `ink` / `paper` | 17.1:1 | OK at any size |
| `muted` / `paper` | 10.0:1 | OK at any size |
| `accent` / `paper` | 11.2:1 | OK at any size |

Gold appears three times at most: the italic word, the full-width rule, and the spec labels. No glow, no grid, no neon, no second accent.

## Type

Load Fraunces and Outfit. The title is Fraunces 560. The italic gold word is Fraunces italic 560. Labels and specs are Outfit.

| Role | Face | Size |
|---|---|---|
| Title | Fraunces 560 | 96–112px, line-height 0.96 |
| Gold word | Fraunces italic 560 | Same size as the title |
| Folio | Fraunces 560 | About 340px, ivory at 7% opacity |
| Specs | Outfit 500 | 30px |
| Labels | Outfit 500 | 16–18px, uppercase, tracked |

The title is three lines. One word inside it is italic gold. That word is the claim.

## Composition

- The field stays dark from the cover through the closing slide.
- A huge folio number sits behind the upper right and is cropped by the edge.
- The title is left, in the upper half, with a wide empty pause beneath it.
- A 2px gold rule crosses the full width in the lower third.
- Three specs sit under that rule. Each has a gold label and one short value.
- The footer is small, uppercase, and quiet. It does not repeat the gold rule.

## Other slides from this file

Keep the folio, the dark field, and the gold rule.

| Slide | Change |
|---|---|
| Text | Keep the three-line serif. The standfirst replaces the spec row |
| Score | Two specs become the numbers. The later number is gold |
| Steps | Three specs become the steps. Labels are 01, 02, 03 |
| Screen | Place the crop above the gold rule, inset 80px. One caption stays below it |
| Closing | The gold word becomes the whole last line. Remove the spec row |

No periods at the end of card sentences. A fact slide adds `.source` just above the footer with the full URL.
