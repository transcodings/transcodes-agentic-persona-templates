#!/usr/bin/env python3
"""Write index.html that shows slide HTML before any image or PDF is rendered.

Usage:
  python3 build-preview.py slide-01.html slide-02.html --frame 1080x1350 --out index.html
  python3 build-preview.py deck.html --frame 1920x1080 --note "Reply yes to print." --produces "the PDF"

One input file with several sections becomes one tall frame.
Several input files become one frame each, in the order given.
"""
import argparse
import os
import pathlib
import re
import sys
from urllib.parse import quote


SLIDE_CLASS = re.compile(r"""class\s*=\s*["']slide(?:\s|["'])""")
CARD_CLASS = re.compile(r"""class\s*=\s*["']card(?:\s|["'])""")


def die(message):
    sys.exit(message)


def slide_count(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", "", text, flags=re.I | re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    slides = len(SLIDE_CLASS.findall(text))
    if slides:
        return slides
    cards = len(CARD_CLASS.findall(text))
    return cards or 1


def esc(value):
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def src_for(html, out_dir):
    relative = os.path.relpath(html.resolve(), out_dir.resolve())
    return quote(pathlib.Path(relative).as_posix(), safe="/")


def parse_frame(value):
    parts = value.lower().split("x")
    if len(parts) != 2:
        die("--frame must look like 1080x1350")
    width, height = int(parts[0]), int(parts[1])
    if width < 1 or height < 1:
        die("--frame width and height must be at least 1")
    return width, height


def frames(files):
    blocks = []
    for path in files:
        count = slide_count(path)
        blocks.append((path, count))
    return blocks


PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview</title>
<style>
  :root {{ color-scheme: light; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: #14120f;
    color: #f4f0e8;
    font: 16px/1.45 ui-sans-serif, system-ui, sans-serif;
  }}
  header {{
    position: sticky;
    top: 0;
    z-index: 1;
    padding: 20px 24px 16px;
    background: #14120f;
    border-bottom: 1px solid rgba(244, 240, 232, 0.16);
  }}
  header p {{ margin: 0; }}
  header p + p {{ margin-top: 6px; color: #c9c2b6; }}
  main {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 28px;
    padding: 28px 16px 64px;
  }}
  figure {{ margin: 0; width: min(920px, calc(100vw - 32px)); }}
  figcaption {{ margin-top: 8px; color: #c9c2b6; font-size: 13px; }}
  .frame {{
    --fit: min(920px, calc(100vw - 32px));
    width: var(--fit);
    height: calc(var(--fit) * var(--h) * var(--n) / var(--w));
    overflow: hidden;
    background: #fff;
  }}
  iframe {{
    width: calc(var(--w) * 1px);
    height: calc(var(--h) * var(--n) * 1px);
    border: 0;
    transform-origin: top left;
    transform: scale(calc(var(--fit) / (var(--w) * 1px)));
  }}
</style>
</head>
<body>
<header>
  <p>{note}</p>
  <p>{produces}</p>
</header>
<main>
{figures}
</main>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Write an index.html preview of slide HTML.")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--frame", default="1080x1350", help="WIDTHxHEIGHT of one slide")
    parser.add_argument("--out", default="index.html")
    parser.add_argument("--note", default="Preview only. Nothing has been rendered yet. Reply yes to create the files.")
    parser.add_argument("--produces", default="the rendered files from this HTML")
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()

    width, height = parse_frame(args.frame)
    files = []
    for raw in args.inputs:
        path = pathlib.Path(raw).expanduser().resolve()
        if not path.is_file():
            die(f"Not a file: {raw}")
        files.append(path)

    out = pathlib.Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    figures = []
    for path, count in frames(files):
        label = path.name if count == 1 else f"{path.name} · {count} slides"
        figures.append(
            "  <figure>\n"
            f'    <div class="frame" style="--w:{width};--h:{height};--n:{count}">\n'
            f'      <iframe src="{src_for(path, out.parent)}" title="{esc(path.name)}"></iframe>\n'
            "    </div>\n"
            f"    <figcaption>{esc(label)}</figcaption>\n"
            "  </figure>"
        )

    page = PAGE.format(
        lang=esc(args.lang),
        note=esc(args.note),
        produces=esc(args.produces),
        figures="\n".join(figures),
    )
    out.write_text(page, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
