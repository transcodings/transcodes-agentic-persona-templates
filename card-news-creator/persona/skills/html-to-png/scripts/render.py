#!/usr/bin/env python3
"""Render card news HTML files to PNG with headless Chrome.

Usage:
  python3 render.py <html file or folder> [...] [--out DIR] [--size 1080x1350] [--sheet] [--pdf]

- A folder renders every *.html inside it (sorted by name).
- PNGs are written next to each HTML file unless --out is given.
- --sheet also writes preview-all.png (needs Pillow).
- --pdf also writes carousel.pdf, one page per slide, for LinkedIn document posts (needs Pillow).
"""
import argparse
import pathlib
import shutil
import subprocess
import sys

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
]


def find_chrome():
    for c in CANDIDATES:
        if pathlib.Path(c).exists() or shutil.which(c):
            return c
    sys.exit("Chrome/Chromium not found. Install Google Chrome or add chromium to PATH")


def collect(inputs):
    files = []
    for raw in inputs:
        p = pathlib.Path(raw).expanduser().resolve()
        if p.is_dir():
            files += sorted(p.glob("*.html"))
        elif p.suffix == ".html" and p.exists():
            files.append(p)
        else:
            sys.exit(f"Not an HTML file or folder: {raw}")
    if not files:
        sys.exit("No HTML files found")
    return files


def render(chrome, html, png, w, h):
    # virtual-time-budget gives web fonts (Google Fonts) time to load before the screenshot
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={w},{h}",
                    "--virtual-time-budget=8000", f"--screenshot={png}", html.as_uri()],
                   check=True, capture_output=True)


def check_size(png, w, h):
    try:
        from PIL import Image
    except ImportError:
        return "size not checked (Pillow missing)"
    size = Image.open(png).size
    if size != (w, h):
        return f"WARNING size {size[0]}x{size[1]}, expected {w}x{h}"
    return f"{w}x{h} ok"


def sheet(pngs, out):
    from PIL import Image
    tw, th, gap, cols = 360, 450, 14, 5
    rows = (len(pngs) + cols - 1) // cols
    canvas = Image.new("RGB", (gap + min(len(pngs), cols) * (tw + gap), gap + rows * (th + gap)), (236, 236, 236))
    for i, p in enumerate(pngs):
        canvas.paste(Image.open(p).convert("RGB").resize((tw, th)), (gap + (i % cols) * (tw + gap), gap + (i // cols) * (th + gap)))
    canvas.save(out)
    return out


def pdf(pngs, out):
    from PIL import Image
    pages = [Image.open(p).convert("RGB") for p in pngs]
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=72)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", help="output folder (default: next to each HTML)")
    ap.add_argument("--size", default="1080x1350", help="WIDTHxHEIGHT (default 1080x1350)")
    ap.add_argument("--sheet", action="store_true", help="also write preview-all.png")
    ap.add_argument("--pdf", action="store_true", help="also write carousel.pdf for LinkedIn")
    a = ap.parse_args()

    w, h = (int(v) for v in a.size.lower().split("x"))
    chrome = find_chrome()
    files = collect(a.inputs)
    out_dir = pathlib.Path(a.out).expanduser().resolve() if a.out else None
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)

    pngs = []
    for html in files:
        png = (out_dir or html.parent) / f"{html.stem}.png"
        render(chrome, html, png, w, h)
        pngs.append(png)
        print(f"{png}  {check_size(png, w, h)}")

    target = out_dir or files[0].parent
    if a.sheet:
        print("sheet:", sheet(pngs, target / "preview-all.png"))
    if a.pdf:
        print("pdf:", pdf(pngs, target / "carousel.pdf"))


if __name__ == "__main__":
    main()
