#!/usr/bin/env bash
# ApocaPocket Diagram Converter
# Converts workspace SVG diagrams to 24-bit BMP for the RP2040 device
#
# Usage:
#   ./tools/convert_diagrams.sh                     # convert only
#   ./tools/convert_diagrams.sh /Volumes/APOCA      # convert + copy to SD
#
# Requirements:
#   - ImageMagick: brew install imagemagick  OR  sudo apt install imagemagick
#   - (Optional) rsvg-convert: brew install librsvg  OR  sudo apt install librsvg2-bin

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DIAG_SRC="$PROJECT_DIR/data/diagrams"
OUT_DIR="/tmp/apocapocket_diagrams"
SD_MOUNT="${1:-}"   # optional SD card mount point

# Verify ImageMagick is available
if ! command -v convert &>/dev/null; then
    echo "ERROR: ImageMagick 'convert' not found."
    echo "Install: brew install imagemagick  OR  sudo apt install imagemagick"
    exit 1
fi

mkdir -p "$OUT_DIR"

echo "=== ApocaPocket Diagram Converter ==="
echo "Source: $DIAG_SRC"
echo "Output: $OUT_DIR"
[ -n "$SD_MOUNT" ] && echo "SD card: $SD_MOUNT"
echo ""

converted=0
failed=0

# Check for rsvg-convert (better SVG rendering)
USE_RSVG=0
if command -v rsvg-convert &>/dev/null; then
    USE_RSVG=1
    echo "Using rsvg-convert for SVG rendering (better quality)"
else
    echo "Using ImageMagick for SVG rendering (rsvg-convert not found)"
fi
echo ""

for svg in "$DIAG_SRC"/*.svg; do
    [ -f "$svg" ] || continue
    eid="$(basename "${svg%.svg}")"
    out="$OUT_DIR/${eid}.bmp"

    if [ $USE_RSVG -eq 1 ]; then
        # Two-step: SVG → PNG → BMP (best quality)
        tmp_png="/tmp/${eid}_apoca.png"
        if rsvg-convert -w 200 -h 200 --keep-aspect-ratio "$svg" -o "$tmp_png" 2>/dev/null && \
           convert "$tmp_png" \
               -background white \
               -flatten \
               -resize 200x200 \
               -gravity center \
               -extent 200x200 \
               -type TrueColor \
               "BMP3:$out" 2>/dev/null; then
            rm -f "$tmp_png"
            ((converted++))
            printf "  ✅ %-50s %s\n" "$eid" "$(ls -sh "$out" | cut -d' ' -f1)"
        else
            rm -f "$tmp_png"
            ((failed++))
            printf "  ❌ FAILED: %s\n" "$eid"
        fi
    else
        # Single-step: SVG → BMP via ImageMagick
        if convert -background white \
            -resize 200x200 \
            -gravity center \
            -extent 200x200 \
            -type TrueColor \
            "$svg" "BMP3:$out" 2>/dev/null; then
            ((converted++))
            printf "  ✅ %-50s %s\n" "$eid" "$(ls -sh "$out" | cut -d' ' -f1)"
        else
            ((failed++))
            printf "  ❌ FAILED: %s\n" "$eid"
        fi
    fi
done

echo ""
echo "Results: $converted converted, $failed failed"

# Verify BMP format
echo ""
echo "Verifying output files..."
for bmp in "$OUT_DIR"/*.bmp; do
    [ -f "$bmp" ] || continue
    info=$(file "$bmp" 2>/dev/null)
    if echo "$info" | grep -q "24"; then
        printf "  ✅ %s\n" "$(basename "$bmp")"
    else
        printf "  ⚠️  Wrong format: %s\n" "$(basename "$bmp")"
        printf "     %s\n" "$info"
    fi
done

# Copy to SD card if mount point provided
if [ -n "$SD_MOUNT" ]; then
    echo ""
    SD_DIAG="$SD_MOUNT/data/data/diagrams"
    if [ -d "$SD_MOUNT" ]; then
        mkdir -p "$SD_DIAG"
        cp "$OUT_DIR"/*.bmp "$SD_DIAG/" 2>/dev/null || true
        echo "Copied to SD: $(ls "$SD_DIAG"/*.bmp 2>/dev/null | wc -l) files"
        echo "SD path: $SD_DIAG"
    else
        echo "WARNING: SD card not found at $SD_MOUNT"
        echo "Files are in: $OUT_DIR"
    fi
else
    echo ""
    echo "Files saved to: $OUT_DIR"
    echo "To copy to SD card, run:"
    echo "  cp $OUT_DIR/*.bmp /YOUR/SD/CARD/data/data/diagrams/"
fi

echo ""
echo "Done!"
