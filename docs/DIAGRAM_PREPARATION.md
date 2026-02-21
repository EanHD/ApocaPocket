# Diagram Preparation Guide
**ApocaPocket v1.4**

The firmware displays **24-bit uncompressed BMP** images only. The 173 workspace
diagrams are SVG files and must be converted before loading onto the device.

---

## Format Requirements

| Property | Requirement |
|----------|-------------|
| Format | BMP (Windows BMP3, 24-bit color) |
| Size | 200×200px recommended (up to 200×232 for full content area) |
| Color depth | 24-bit RGB (not indexed, not 16-bit, not 32-bit) |
| Compression | None (uncompressed) |
| File naming | `{eid}.bmp` — exact entry ID, e.g., `l1-medical-cpr-basics.bmp` |
| SD path | `/data/data/diagrams/{eid}.bmp` |

> **Why BMP?** The firmware streams BMP row-by-row from SD to display using
> only ~1KB RAM. PNG/JPEG require decoders that don't fit on the RP2040 alongside
> the database. BMP is trivially decodable in hardware.

> **Why 200px wide?** Content area is 200px wide (240px display minus 20px margins
> each side). Images wider than 200px are cropped. Images narrower are centered.

---

## Converting SVGs → BMP

### Option A: ImageMagick (recommended, fastest)

```bash
# Install: brew install imagemagick  OR  sudo apt install imagemagick

# Convert one file
convert -background white \
    -resize 200x200 \
    -gravity center \
    -extent 200x200 \
    -type TrueColor \
    input.svg BMP3:output.bmp

# Batch convert all workspace SVGs
cd data/diagrams/
for svg in *.svg; do
    eid="${svg%.svg}"
    convert -background white \
        -resize 200x200 \
        -gravity center \
        -extent 200x200 \
        -type TrueColor \
        "$svg" "BMP3:${eid}.bmp"
    echo "Converted: $eid"
done
```

### Option B: rsvg-convert + convert (best SVG rendering)

```bash
# Install: brew install librsvg imagemagick  OR  sudo apt install librsvg2-bin

# Render SVG to PNG then convert to BMP
for svg in data/diagrams/*.svg; do
    eid="$(basename "${svg%.svg}")"
    rsvg-convert -w 200 -h 200 "$svg" -o "/tmp/${eid}.png"
    convert "/tmp/${eid}.png" \
        -type TrueColor \
        "BMP3:data/diagrams/${eid}.bmp"
    rm "/tmp/${eid}.png"
    echo "Done: $eid"
done
```

### Option C: Inkscape (highest quality, slowest)

```bash
# Install: brew install inkscape  OR  sudo apt install inkscape

for svg in data/diagrams/*.svg; do
    eid="$(basename "${svg%.svg}")"
    # Export to PNG at 2x then resize for quality
    inkscape "$svg" \
        --export-width=400 \
        --export-filename="/tmp/${eid}_2x.png"
    convert "/tmp/${eid}_2x.png" \
        -resize 200x200 \
        -type TrueColor \
        "BMP3:data/diagrams/${eid}.bmp"
    rm "/tmp/${eid}_2x.png"
    echo "Done: $eid"
done
```

### Option D: Windows (Paint / IrfanView)

1. Open SVG in a browser (Chrome/Edge)
2. Right-click → Save as PNG
3. Open PNG in **Paint**
4. Resize to 200×200 (Image → Resize → Pixels → 200×200)
5. File → Save as → **24-bit Bitmap (.bmp)**
6. Rename file to `{eid}.bmp`

---

## Batch Convert (All 13 Current Diagrams)

Run this from the project root:

```bash
#!/bin/bash
# Run from: apocalypse-field-node/

SD=${1:-/Volumes/APOCA}     # SD card mount point (arg 1 or default)
DIAG_SRC=data/diagrams
DIAG_DST=$SD/data/data/diagrams

mkdir -p "$DIAG_DST"
mkdir -p /tmp/apocapocket_diagrams

echo "Converting SVG diagrams to BMP..."
converted=0
failed=0

for svg in "$DIAG_SRC"/*.svg; do
    eid="$(basename "${svg%.svg}")"
    out="/tmp/apocapocket_diagrams/${eid}.bmp"

    if convert -background white \
        -resize 200x200 \
        -gravity center \
        -extent 200x200 \
        -type TrueColor \
        "$svg" "BMP3:$out" 2>/dev/null; then
        cp "$out" "$DIAG_DST/${eid}.bmp"
        ((converted++))
        echo "  ✅ $eid"
    else
        ((failed++))
        echo "  ❌ FAILED: $eid"
    fi
done

echo ""
echo "Results: $converted converted, $failed failed"
echo "BMPs on SD: $(ls "$DIAG_DST"/*.bmp 2>/dev/null | wc -l)"
```

Save as `tools/convert_diagrams.sh`, then:
```bash
chmod +x tools/convert_diagrams.sh
./tools/convert_diagrams.sh /Volumes/APOCA
```

---

## Verifying BMP Files

Check a converted file is valid:
```bash
# Should show: Windows BMP, 200 x 200 x 24
file data/diagrams/l1-medical-cpr-basics.bmp

# Should show byte count: 200*200*3 + 54 header = 120,054 bytes
ls -la data/diagrams/l1-medical-cpr-basics.bmp

# View it (macOS)
open data/diagrams/l1-medical-cpr-basics.bmp

# View it (Linux)
eog data/diagrams/l1-medical-cpr-basics.bmp
```

Expected output:
```
l1-medical-cpr-basics.bmp: PC bitmap, Windows 3.x format,
  200 x 200 x 24, image size 120000, resolution 3937 x 3937 px/m,
  cbSize 120054, bits offset 54
```

---

## Naming Reference

File name must match the entry ID exactly (case-sensitive, no spaces):

| Entry | Diagram filename |
|-------|-----------------|
| `l1-medical-cpr-basics` | `l1-medical-cpr-basics.bmp` |
| `l1-medical-severe-bleeding` | `l1-medical-severe-bleeding.bmp` |
| `l1-wildlife-bear-encounters` | `l1-wildlife-bear-encounters.bmp` |

Find an entry's ID from its filename (drop the `.md` extension):
```bash
ls data/entries/L1_immediate_survival/
# l1-medical-cpr-basics.md → ID is: l1-medical-cpr-basics
```

---

## Current Diagrams (13 SVGs to Convert)

| Diagram | Entry ID | Status |
|---------|----------|--------|
| resource-assessment-matrix.svg | `l1-strategy-resource-assessment` | ⏳ Need convert |
| first-24hr-decision-tree.svg | `l1-strategy-first-24-hours` | ⏳ Need convert |
| emp-grid-down-timeline.svg | `l1-strategy-emp-grid-down` | ⏳ Need convert |
| l3-stone-tool-knapping.svg | `l3-tools-stone-knapping` | ⏳ Need convert |
| mental-health-crisis-triage.svg | `l1-mental-health-crisis` | ⏳ Need convert |
| start-triage-protocol.svg | `l1-medical-triage-start` | ⏳ Need convert |
| composting-toilet-workflow.svg | `l3-sanitation-composting-toilet` | ⏳ Need convert |
| tornado-shelter-priority.svg | `l1-weather-tornado` | ⏳ Need convert |
| l4-companion-planting.svg | `l4-agriculture-companion-planting` | ⏳ Need convert |
| pandemic-response-timeline.svg | `l1-pandemic-response` | ⏳ Need convert |
| snow-melting-efficiency.svg | `l1-water-snow-melting` | ⏳ Need convert |
| l5-truss-types.svg | `l5-construction-trusses` | ⏳ Need convert |
| vehicle-breakdown-decision-flow.svg | `l1-vehicle-breakdown-remote` | ⏳ Need convert |

> **Note:** Entry ID must be verified against actual filename in `data/entries/`.
> The IDs above are approximate — check exact filenames before converting.

---

## Design Tips for New Diagrams

If creating new diagrams specifically for the device:
- **Canvas:** 200×200px (exact device content area width)
- **Background:** Black `#000000` (matches device iOS Dark Mode background)
- **Text:** White `#FFFFFF` minimum, use cyan `#0A84FF` for headers
- **Line weight:** 2–3px minimum (visible on 240px display)
- **Font size:** 14px minimum for readable text on device
- **Avoid:** Gradients, transparency, complex shadows (waste on small display)
- **Test:** Shrink in browser to 200×200 before exporting — what you see is what device shows
