#!/bin/bash
# ApocaPocket SD Card Populator (run from WSL)
# Usage: bash tools/copy_to_sd.sh E   (replace E with your SD drive letter)

set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"

if [ -z "$1" ]; then
    echo "Usage: $0 <drive_letter>"
    echo "  Example: $0 E"
    echo ""
    echo "Available drives:"
    ls /mnt/ | grep -v '^[a-z][a-z]' | tr '\n' ' '
    echo ""
    exit 1
fi

DRIVE=$(echo "$1" | tr '[:upper:]' '[:lower:]')
SD="/mnt/$DRIVE"

if [ ! -d "$SD" ]; then
    echo "Drive $SD not found. Attempting to mount..."
    sudo mkdir -p "$SD"
    if sudo mount -t drvfs "${1^^}:" "$SD" 2>/dev/null; then
        echo "  [OK] Mounted ${1^^}: at $SD"
    else
        echo ""
        echo "ERROR: Could not mount ${1^^}: drive."
        echo "Make sure the SD card is inserted, then run:"
        echo "  sudo mkdir -p $SD && sudo mount -t drvfs ${1^^}: $SD"
        echo "Then run this script again."
        exit 1
    fi
fi

echo "=== ApocaPocket SD Card Setup ==="
echo "Target: $SD"
echo ""

# Create required directory structure
echo "Creating folder structure..."
mkdir -p "$SD/index"
mkdir -p "$SD/data/data/entries"

# Copy index files
echo "Copying index files..."
cp "$REPO/exports/entries.idx"    "$SD/index/entries.idx"
cp "$REPO/exports/metadata.json"  "$SD/index/metadata.json"
echo "  [OK] /index/entries.idx  ($(du -sh "$SD/index/entries.idx" | cut -f1))"
echo "  [OK] /index/metadata.json"

# Count and copy entry files
echo ""
echo "Copying markdown entry files..."
TOTAL=0
for folder in "$REPO/data/entries"/*/; do
    fname=$(basename "$folder")
    count=$(ls "$folder"*.md 2>/dev/null | wc -l)
    if [ "$count" -gt 0 ]; then
        mkdir -p "$SD/data/data/entries/$fname"
        cp "$folder"*.md "$SD/data/data/entries/$fname/"
        TOTAL=$((TOTAL + count))
        echo "  [OK] $fname ($count files)"
    fi
done

echo ""
echo "=== Done! ==="
echo "  Entries copied: $TOTAL"
echo "  SD ready for ApocaPocket firmware"
echo ""
echo "Now flash firmware/main.uf2:"
echo "  Hold BOOT button + tap RESET → drag main.uf2 to RPI-RP2 drive"
