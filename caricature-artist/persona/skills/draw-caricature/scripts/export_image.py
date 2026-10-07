#!/usr/bin/env python3
"""Export one image as PNG and JPEG at an exact width and height.

Usage:
  python3 export_image.py <image> --width 1080 --height 1350
  python3 export_image.py <image> --size 1080x1350 [--out DIR]

Omit --width/--height or --size to keep the source image's own size.
The picture is scaled to cover the frame and center-cropped, so the
output is exactly that size and the face is not stretched.
PNG and JPEG are written next to the source unless --out is given.
"""
import argparse
import pathlib
import sys


def parse_size(width, height, size):
    if size and (width is not None or height is not None):
        sys.exit("Pass --size or --width with --height, not both.")
    if size:
        parts = size.lower().split("x")
        if len(parts) != 2:
            sys.exit("--size must look like 1080x1350")
        width, height = parts
    if (width is None) != (height is None):
        sys.exit("Pass both --width and --height.")
    if width is None:
        return None
    w, h = int(width), int(height)
    if w < 1 or h < 1:
        sys.exit("Width and height must be at least 1.")
    return w, h


def cover(image, width, height):
    from PIL import Image

    scale = max(width / image.width, height / image.height)
    resized = image.resize(
        (max(1, round(image.width * scale)), max(1, round(image.height * scale))),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def flatten(image):
    from PIL import Image

    if image.mode == "RGB":
        return image
    rgba = image.convert("RGBA")
    background = Image.new("RGB", rgba.size, (255, 255, 255))
    background.paste(rgba, mask=rgba.getchannel("A"))
    return background


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--size", help="WIDTHxHEIGHT, for example 1080x1350")
    parser.add_argument("--out", help="output folder (default: next to the image)")
    args = parser.parse_args()

    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is required. Install it with: pip install pillow")

    source = pathlib.Path(args.image).expanduser().resolve()
    if not source.is_file():
        sys.exit(f"Not an image file: {args.image}")

    target = parse_size(args.width, args.height, args.size)
    out_dir = pathlib.Path(args.out).expanduser().resolve() if args.out else source.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as opened:
        image = flatten(opened)
        width, height = target or (image.width, image.height)
        if (image.width, image.height) != (width, height):
            image = cover(image, width, height)
        png = out_dir / f"{source.stem}.png"
        jpeg = out_dir / f"{source.stem}.jpg"
        image.save(png, format="PNG")
        image.save(jpeg, format="JPEG", quality=95)
        print(f"{png}  {width}x{height}")
        print(f"{jpeg}  {width}x{height}")


if __name__ == "__main__":
    main()
