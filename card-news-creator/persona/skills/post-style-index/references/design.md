---
name: "Index design"
description: "Style 1 card news. Cream paper, black rail, red signal. Pair with references/style.html. Instrument Sans and IBM Plex Mono."
aliases:
  - "design 1"
  - "style 1"
  - "index"
  - "editorial"
  - "swiss"
---

# Index design

Style 1 is an editorial index, not the paper-desk look. The master file is `references/style.html`. Copy that file for every slide in the carousel. Replace the words. Keep the black rail, the top rule, the red signal, and the three-column index.

Use this pair only. Do not mix it with `post-style-nocturne`, `post-style-gallery`, or `post-style-paper`.

## Colors

| Token | Value | Used for |
|---|---|---|
| `paper` | `#F4F0E6` | Card background |
| `box` | `#FBFAF6` | A fact panel, when a slide needs one |
| `ink` | `#161616` | Rail, rules, and main text |
| `muted` | `#5E594F` | Standfirst and secondary text |
| `accent` | `#C5362B` | One signal: a word, a short bar, or index labels |
| `night` | `#161616` | The closing slide, when the field inverts |
| `line` | `rgba(22,22,22,.22)` | The footer rule |

| Text / background | Contrast | Verdict |
|---|---|---|
| `ink` / `paper` | 15.9:1 | OK at any size |
| `muted` / `paper` | 6.1:1 | OK at any size |
| `accent` / `paper` | 4.7:1 | OK at any size |
| `paper` / `night` | 15.9:1 | OK at any size |

One red moment per card. The rail and the rules stay black. No tape, no tilted paper, no dot texture, no shadow, no second hue.

## Type

Load Instrument Sans and IBM Plex Mono. Display words are Instrument Sans 700. Labels are IBM Plex Mono 500 or 600, uppercase, tracked out.

| Role | Face | Size |
|---|---|---|
| Title | Instrument Sans 700 | 96–124px, line-height 0.9 |
| Standfirst | Instrument Sans 500 | 36px |
| Index value | Instrument Sans 650 | 32px |
| Kicker and labels | IBM Plex Mono | 16–20px |

A title is three lines or fewer. The red word is the last line, or the one word that carries the claim.

## Composition

- A 72px black rail on the left carries the brand vertically.
- Content starts at 120px. The right margin is 72px.
- The header is one row: section name left, slide number right, then a 2px black rule.
- The title sits high. A 168×16px red bar sits under it. It is a signal, not an underline that runs the full width.
- The bottom index is three columns under a 2px rule: a mono label in red, then one short value.
- The footer is mono, uppercase, and separated by a hairline.

## Other slides from this file

Keep the rail, header, rule, and footer. Change the middle.

| Slide | Replace the title block with |
|---|---|
| Text | A two-line title and one standfirst. The red word is the claim |
| Score | Two figures in the index row. Before stays `ink`. After is `accent` |
| Steps | Three numbered rows. The number is mono and red. The action is one line |
| Screen | A square crop on the right half. Caption stays in the index row |
| Closing | Invert the card to `night`, keep the rail, and set the title in `paper` with one red word |

No periods at the end of card sentences. A fact slide adds `.source` above the footer with the full URL.
