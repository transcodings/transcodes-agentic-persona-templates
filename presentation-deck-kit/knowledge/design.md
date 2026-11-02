---
name: "Deck design"
description: "Color roles for a 16:9 deck. Paper #FAF7F2, ink #17131F, brand #6D4DFF. A sample fills these roles before the HTML."
aliases:
  - "design"
  - "color"
  - "palette"
  - "tokens"
  - "tone"
---

# Deck design

Colors for a deck live here. `starter.html` implements this palette in `:root`. A slide uses the token names, not a one-off hex.

Text needs 4.5:1. Large text, 24px and up, needs 3:1. A pair that fails is for shapes, not for words.

## Neutrals

| Token | Value | Used for |
|---|---|---|
| `paper` | `#FAF7F2` | Page background |
| `white` | `#FFFFFF` | Cards and text on a dark fill |
| `ink` | `#17131F` | Main text |
| `muted` | `#5E5870` | Leads and secondary text |
| `soft` | `#948DA3` | Labels and footer, 24px and up only |
| `line` | `#E7E1D8` | Rules and dividers, not text |

| Text / background | Contrast | Verdict |
|---|---|---|
| `ink` / `paper` | 17.1:1 | OK at any size |
| `ink` / `white` | 18.3:1 | OK at any size |
| `muted` / `paper` | 6.3:1 | OK at any size |
| `soft` / `paper` | 3.0:1 | 24px and up only |
| `white` / `ink` | 18.3:1 | OK at any size |

## Tones

Each hue is a triple. `base` fills a shape. `deep` is the text and the darker mark. `soft` is the tint behind `ink`. On a component, `.tone-*` sets `--c`, `--c-deep`, `--c-soft`, and `--c-on`.

| Tone | base | deep | soft | White text on base |
|---|---|---|---|---|
| `brand` | `#6D4DFF` | `#4A2FD6` | `#ECE7FF` | 5.1:1, OK |
| `coral` | `#FF7A59` | `#C2410C` | `#FFE6DE` | 2.6:1, never. Use `deep` for words |
| `sun` | `#FFC53D` | `#8A5A00` | `#FFF2CC` | 1.6:1, never. Words are `ink` or `deep` |
| `mint` | `#14A37F` | `#0C7D61` | `#DAF5EC` | 3.2:1, 24px and up only |
| `sky` | `#3B82F6` | `#1D5FCF` | `#E0ECFF` | 3.7:1, 24px and up only |

`ink` on every `soft` is at least 15:1. The default component tone is `brand`.

## Color rules

- One tone per page, set with `data-tone`. A second tone is a chip or a decoration, not a second text color.
- Body text stays `ink` on `paper` or `white`. Do not recolor a sentence per component.
- `sun` and `coral` are shapes and highlights. Their words use `ink` or `deep`.
- `soft` is a footer or label color. It is not body text.
- No `box-shadow`. No gradient text, glow, or neon.
- Change a palette in the deck file's own `:root`. Leave `starter.html` and `catalog.html` unchanged unless the user asks to change the kit.

## When a sample sets the colors

Before the deck HTML, write a `design.md` next to that deck and fill the roles from the sample. The deck's `:root` is a copy of that file.

| Role | Take from the sample |
|---|---|
| `paper`, `ink`, `muted`, `line` | Background, main text, secondary text, and hairline |
| `brand`, `brand-deep`, `brand-soft` | The main accent, a darker shade for words, and a light tint |
| Next hues | Only hues the sample actually has, assigned in order to `coral`, `sun`, `mint`, `sky` |

Each assigned hue still needs `base`, `deep`, and `soft`. A tone you do not assign keeps the kit default, and this deck does not use that `.tone-*` class. Record the contrast for every text pair, and name any sample color you dropped. If the sample names no font that can be loaded, keep General Sans and Pretendard and say so.
