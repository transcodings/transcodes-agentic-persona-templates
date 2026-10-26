#!/bin/zsh
# Usage: ./build-pdf.sh [html file] [pdf file]
# Default: starter.html → <folder name>.pdf
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HTML="${1:-starter.html}"
PDF="${2:-$(basename "$DIR").pdf}"
[[ "$HTML" = /* ]] || HTML="$DIR/$HTML"
[[ "$PDF" = /* ]] || PDF="$DIR/$PDF"

if [[ ! -x "$CHROME" ]]; then
  echo "Google Chrome is required" >&2
  exit 1
fi

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --hide-scrollbars \
  --force-prefers-color-scheme=light \
  --virtual-time-budget=15000 \
  --print-to-pdf="$PDF" \
  "file://$HTML" 2>/dev/null

ls -lh "$PDF"
