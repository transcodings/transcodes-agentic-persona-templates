---
name: "Paper design"
description: "Style 4 card news. Paper desk and Hanken Grotesk. Accent #E8762A, accent text #C9581C, paper #F3EEE4. Pair with references/style.html."
aliases:
  - "design 4"
  - "style 4"
  - "paper"
  - "hanken grotesk"
  - "accent"
---

# Paper design

Style 4 is the paper-desk card news. The look comes from the Shorts videos (SEO · AEO Shorts v7). The master file is `references/style.html`. It holds six slides. Copy the `.card` whose `data-layout` matches the slide, together with the style block, into a file fixed at 1080×1350. When no brand is given, keep these values. When a brand is given, change only `--accent`, `--accent-text`, and the brand name in the header.

Use this pair only. Do not mix it with `post-style-index`, `post-style-nocturne`, or `post-style-gallery`.

## Layouts

| `data-layout` | Slide |
|---|---|
| `cover` | Opening hook |
| `text` | A problem, cause, or explanation |
| `score` | A before-and-after number |
| `steps` | A short how-to |
| `screen` | A real screen |
| `cta` | The last slide, on the black cover |

## Colors

| Token | Value | Used for |
|---|---|---|
| `paper` | `#F3EEE4` | Background of every card, with a faint dot texture |
| `paper-shade` | `#E9E1D3` | Browser bar on screenshot boxes |
| `box` | `#FFFDF8` | White boxes, score boxes, chip fill, pill text |
| `ink` | `#23201C` | All main text, chip borders, pill and step-number fill, code blocks |
| `ink-soft` | `#6A6358` | Subtitles, secondary text, "/100", sources, footer tagline |
| `accent` | `#E8762A` | Lines, stamp borders, rings, dashed arrows, check marks, keyword on the black cover |
| `accent-text` | `#C9581C` | Orange text on paper or a white box (24px and up only) |
| `tape` | `#F2DFAE` | Masking-tape labels |
| `night` | `#0B0A09` | Black cover background |

**Contrast** (WCAG: normal text 4.5:1, large text 24px and up 3:1)

| Text / background | Contrast | Verdict |
|---|---|---|
| `ink` / `paper` | 14.0:1 | OK at any size |
| `ink` / `box` | 16.0:1 | OK at any size |
| `ink` / `tape` | 12.3:1 | OK at any size |
| `ink-soft` / `paper` | 5.1:1 | OK at any size |
| `accent-text` / `paper` | 3.7:1 | 24px and up only |
| `accent-text` / `box` | 4.2:1 | 24px and up only |
| `accent` / `night` | 6.6:1 | OK at any size |
| `box` / `night` | 19.5:1 | OK at any size |
| `accent` / `paper` | 2.6:1 | Never for text. Lines and shapes only |

**Color rules**

- Main text is always `ink`. Backgrounds are only `paper`, `box`, or `tape`.
- Use orange in one place per card: one keyword, one ring, or one stamp.
- Orange text on paper uses `accent-text`, and only at 24px and up.
- No gradients, glow, or neon.
- No peach or sky-blue paper shapes in the background.
- The only dark elements allowed are code blocks and the black cover.

## When a sample sets the colors

A reference image does not add new color names. Before the HTML template, write a `design.md` next to that template and fill this same role list from the sample. The template's `:root` is a copy of that file. A slide does not get its own hex.

| Role | Take from the sample |
|---|---|
| `paper` | The largest background |
| `box` | The panel. Use white when the sample has no panel |
| `ink` | The main text. Darken it until it is at least 4.5:1 on `paper` and on `box` |
| `ink-soft` | Secondary text. 4.5:1 on `paper`, or 3:1 when it is only used at 24px and up. Record which |
| `accent` | The one highlight for lines, marks, and stamps |
| `accent-text` | A darker shade of that highlight for words, 24px and up, at least 3:1 on `paper` |
| `tape` | The label fill, and only when `ink` on it is at least 4.5:1. Otherwise keep `#F2DFAE` |
| `night` | The dark cover, or `#0B0A09` when the sample has no dark slide |
| `line` | `ink` at low opacity |

Keep one accent moment per card. If the sample has more hues, drop them and name the dropped colors in `design.md`. A gradient becomes the flat token closest to its main stop. No glow or neon. When the sample names no font that can be loaded, keep Hanken Grotesk and say so.

## Type

Use one font only: **Hanken Grotesk**. Code blocks are the one exception and use the system monospace font.

Load it with:

`@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&display=block');`

| Role | Weight | Size | Letter spacing |
|---|---|---|---|
| Cover title | 800 | 118px | -0.035em |
| Cover subtitle | 700 | 58px | -0.02em |
| Black cover line / keyword | 800 | 84px / 190px | -0.025em / -0.045em |
| Card title | 800 | 92px (80px on the screenshot card) | -0.035em |
| Body | 500 | 40px, line height 1.32 | 0 |
| Small note | 500 | 30px | 0 |
| Tape label | 600 | 28px | 0.02em |
| Kicker (WEBSITE SCORE, etc.) | 700 | 24px, uppercase | 0.22em |
| Score number / "/100" | 800 / 700 | 168px / 58px | -0.04em |
| Chip | 700 | 36px | 0 |
| Pill | 700 | 32px | 0 |
| Stamp | 800 | 46px | 0.02em |
| Step title / detail | 600 / 500 | 40px / 28px | 0 |
| Table (key / value / tag) | 800 / 500 / 600 | 36px / 34px / 26px | 0 |
| Brand name (header) | 700 | 29px | 0.12em |
| Page number | 800 | 50px | 0.04em |
| Source | 500 (heading 800) | 20px (heading 17px) | 0.14em (heading) |
| Footer left / right | 800 / 600 | 28px / 22px, right is uppercase | 0.06em / 0.14em |

## CSS tokens

```css
:root {
  --paper: #F3EEE4;
  --paper-shade: #E9E1D3;
  --box: #FFFDF8;
  --ink: #23201C;
  --ink-soft: #6A6358;
  --accent: #E8762A;       /* lines, stamps, rings, checks; keyword on the black cover */
  --accent-text: #C9581C;  /* orange text, 24px and up only */
  --tape: #F2DFAE;
  --night: #0B0A09;
  --line: rgba(35,32,28,.14);
  --shadow: 0 30px 60px rgba(35,32,28,.16), 0 4px 10px rgba(35,32,28,.10);
}
```
