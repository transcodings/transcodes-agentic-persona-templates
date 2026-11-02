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

Colors for a deck live here. Every starter implements the same token roles in `:root`; its skin changes typography, geometry, and page treatment. A slide uses the token names, not a one-off hex.

Text needs 4.5:1. Large text, 24px and up, needs 3:1. A pair that fails is for shapes, not for words.

## Built-in styles

| Skill | Files in that skill | Direction | Core palette |
|---|---|---|---|
| `ppt-style-swiss` | `references/starter.html`, `references/catalog.html` | Swiss Grid. Strict grid, uppercase display type, square cards, heavy rules | paper `#F4F1E8`, ink `#101010`, signal red `#E63B2E` |
| `ppt-style-night` | `references/starter.html`, `references/catalog.html` | Night Console. Dark data room, monospace labels, thin borders, technical grid | paper `#07111F`, ink `#F1F6FF`, signal cyan `#35D8C0` |
| `ppt-style-atelier` | `references/starter.html`, `references/catalog.html` | Paper Atelier. Warm editorial paper, serif display type, organic corners | paper `#F2EADC`, ink `#29251F`, brick `#A33F2B` |
| `ppt-style-neutral` | `references/starter.html`, `references/catalog.html` | Original neutral pair | paper `#FAF7F2`, ink `#17131F`, brand `#6D4DFF` |

Open one template skill and use only the starter and catalog in that skill. The skins change more than color: typography, border weight, radius, spacing, cover treatment, decoration, and catalog chrome are intentionally different.

## Neutrals

The following values describe the original neutral compatibility pair. Numbered pairs override the values in their own skin block.

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
- Change a palette in the deck file's own `:root`. Leave every template skill unchanged unless the user asks to change the kit.

## When a sample sets the colors

Before the deck HTML, write a `design.md` next to that deck and fill the roles from the sample. Start from the structurally closest built-in style. The deck's `:root` and skin adjustments are a copy of that file.

| Role | Take from the sample |
|---|---|
| `paper`, `ink`, `muted`, `line` | Background, main text, secondary text, and hairline |
| `brand`, `brand-deep`, `brand-soft` | The main accent, a darker shade for words, and a light tint |
| Next hues | Only hues the sample actually has, assigned in order to `coral`, `sun`, `mint`, `sky` |

Each assigned hue still needs `base`, `deep`, and `soft`. A tone you do not assign keeps the selected style's default, and this deck does not use that `.tone-*` class. Record the contrast for every text pair, and name any sample color you dropped. If the sample names no font that can be loaded, keep the selected style's fonts and say so.
