#!/bin/zsh
# Usage: ./build-pptx.sh [html file] [pptx file]
# Default: starter.html → <html name>.pptx
#
# Makes an editable PowerPoint file:
#   boxes, cards, table cells, lines  → PowerPoint shapes
#   all text                          → PowerPoint text boxes (same line breaks as the HTML)
#   check marks, step numbers, SVG    → one transparent image layer per slide
#
# Fonts: install General Sans, Pretendard and JetBrains Mono on the computer that opens the file,
# or pick fallbacks:  PPTX_KOREAN_FONT="Apple SD Gothic Neo" PPTX_LATIN_FONT="Arial" ./build-pptx.sh deck.html
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
HTML="${1:-starter.html}"
[[ "$HTML" = /* ]] || HTML="$PWD/$HTML"
[[ -f "$HTML" ]] || HTML="$DIR/${1:-starter.html}"
PPTX="${2:-${HTML:r}.pptx}"
[[ "$PPTX" = /* ]] || PPTX="$PWD/$PPTX"

if [[ ! -f "$HTML" ]]; then
  echo "Cannot find $1" >&2
  exit 1
fi
if [[ ! -x "$CHROME" ]]; then
  echo "Google Chrome is required (or set CHROME=/path/to/chrome)" >&2
  exit 1
fi
if ! command -v node >/dev/null; then
  echo "Node.js 18+ is required" >&2
  exit 1
fi

# first run: install the converter's packages
if [[ ! -d "$DIR/tools/node_modules/pptxgenjs" || ! -d "$DIR/tools/node_modules/puppeteer-core" ]]; then
  echo "Installing converter packages (first run only)…"
  (cd "$DIR/tools" && npm install --silent --no-audit --no-fund)
fi

CHROME="$CHROME" node "$DIR/tools/html2pptx.mjs" "$HTML" "$PPTX"
ls -lh "$PPTX"
