# ApocaPocket Diagrams

All 79 diagrams for the ApocaPocket device, consolidated into one place.

## Structure

```
diagrams/
  source/    ← Edit these (SVG + PNG originals)
  bmp/       ← SD card ready (200x200px, 24-bit BMP)
  README.md  ← This file
```

## SD Card Setup

Copy the entire `bmp/` folder to your SD card:

```bash
cp diagrams/bmp/*.bmp /YOUR/SD/CARD/data/diagrams/
```

SD card path expected by firmware: `/data/diagrams/*.bmp`

## Inventory (79 diagrams)

### Medical (L1) — 40 diagrams
- Antibiotic selection, resistance cycle, spectrum chart
- CPR technique, choking response, chest seal
- Burns, fracture stabilization, heat stroke
- IV insertion, flow rates, vein anatomy, troubleshooting
- NPA sizing, insertion anatomy/angle, NPA vs OPA
- Gunshot wound entry/exit, wound packing, body regions
- Shock recognition, shock classification chart
- Tourniquet application, pressure points, skull fracture
- Pain scales, pain assessment flowchart
- Naloxone administration, opioid equianalgesic chart
- Medication storage zones, degradation guide, zeer pot
- Suture depth, wound closure patterns, instrument tie
- Pediatric antibiotic dosing, WHO analgesic ladder
- Bacterial vs viral comparison, expired medication tree
- Abscess drainage, insect stings, suturing basics
- Anatomical suture removal timing

### Fire (L1) — 3 diagrams
- Bow drill technique
- Ferro rod technique
- Tinder types

### Navigation (L1) — 1 diagram
- Natural navigation

### Shelter (L1) — 2 diagrams
- Tarp configurations
- Essential knots

### Water (L1) — 1 diagram
- Boiling process

### Plants/Food (L2) — 8 diagrams
- Cattail plant year-round, cattail vs iris comparison
- Dandelion plant diagram
- Death camas vs camas comparison
- Deathcap vs button mushroom
- False morel vs true morel
- Hemlock vs wild carrot comparison
- Trout identification species

### Technology/Materials (L3) — 1 diagram
- Stone tool knapping

### Agriculture (L4) — 1 diagram
- Companion planting

### Community/Civilization (L5) — 9 diagrams
- First 24hr decision tree
- Start triage protocol
- Mental health crisis triage
- Resource assessment matrix
- EMP/grid-down timeline
- Pandemic response timeline
- Composting toilet workflow
- Snow melting efficiency
- Tornado shelter priority
- Truss types
- Vehicle breakdown decision flow

## Regenerating BMPs

If you edit source files, regenerate BMPs:

```bash
# Requires: imagemagick, librsvg2-bin
# sudo apt install imagemagick librsvg2-bin

for f in diagrams/source/*.svg diagrams/source/*.png; do
  base=$(basename "${f%.*}")
  out="diagrams/bmp/${base}.bmp"
  if [[ "$f" == *.svg ]]; then
    tmp="/tmp/${base}_tmp.png"
    rsvg-convert -w 200 -h 200 --keep-aspect-ratio "$f" -o "$tmp"
    convert "$tmp" -background black -flatten -resize 200x200 -gravity center \
      -extent 200x200 -type TrueColor "BMP3:$out"
    rm -f "$tmp"
  else
    convert "$f" -background black -flatten -resize 200x200 -gravity center \
      -extent 200x200 -type TrueColor "BMP3:$out"
  fi
done
```

## Integration Status
- [ ] Firmware: diagram rendering on device (Copilot task)
- [ ] SD card: copy bmp/ to /data/diagrams/
- [ ] Entries: audit which entries reference diagrams, standardize path format
- [ ] Design: define when/where diagrams appear in the UX flow
