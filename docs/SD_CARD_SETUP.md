# SD Card Setup Guide
**ApocaPocket v1.4**

This guide covers formatting the SD card, copying the database, and generating
the binary index. Do this once. The card works in the device until you add new entries.

---

## Requirements

- MicroSD card, 4GB–32GB (Class 10 recommended)
- FAT32 formatted (NOT exFAT — the firmware uses SDFS which requires FAT32)
- A computer with a card reader
- Python 3.8+ (for index generation)

---

## Step 1: Format the SD Card

**Windows:**
```
Right-click the SD drive → Format
File system: FAT32
Allocation unit size: Default
Check "Quick Format"
Click Start
```

**macOS:**
```bash
diskutil list                       # find your SD card (e.g., /dev/disk4)
diskutil eraseDisk FAT32 APOCA /dev/disk4
```

**Linux:**
```bash
lsblk                               # find your SD card (e.g., /dev/sdb)
sudo mkfs.fat -F 32 /dev/sdb1
```

---

## Step 2: Create the Folder Structure

Create these folders on the root of the SD card:

```
/
├── index/                          ← generated index + bookmarks go here
└── data/
    └── data/
        ├── entries/
        │   ├── L1_immediate_survival/
        │   ├── L2_food_biology/
        │   ├── L3_materials_chemistry/
        │   ├── L3_materials_elements/
        │   ├── L3_materials_technology/
        │   ├── L4_agriculture_labor/
        │   ├── L4_tools_rebuilding/
        │   ├── L5_civilization_memory/
        │   └── L5_community_knowledge/
        └── diagrams/               ← BMP diagram files go here (v1.4+)
```

> **Why the double `data/`?** The workspace `data/` directory is copied
> into a `data/` folder on the SD card, so the path on SD becomes `/data/data/`.
> This is intentional — don't flatten it.

**Quick way (Linux/macOS):**
```bash
SD=/Volumes/APOCA    # or /media/youruser/APOCA

mkdir -p $SD/index
mkdir -p $SD/data/data/entries/L1_immediate_survival
mkdir -p $SD/data/data/entries/L2_food_biology
mkdir -p $SD/data/data/entries/L3_materials_chemistry
mkdir -p $SD/data/data/entries/L3_materials_elements
mkdir -p $SD/data/data/entries/L3_materials_technology
mkdir -p $SD/data/data/entries/L4_agriculture_labor
mkdir -p $SD/data/data/entries/L4_tools_rebuilding
mkdir -p $SD/data/data/entries/L5_civilization_memory
mkdir -p $SD/data/data/entries/L5_community_knowledge
mkdir -p $SD/data/data/diagrams
```

---

## Step 3: Copy Entry Files

From the project workspace, copy markdown entries to the SD card:

```bash
# From project root (apocalypse-field-node/)
SD=/Volumes/APOCA

cp data/entries/L1_immediate_survival/*.md  $SD/data/data/entries/L1_immediate_survival/
cp data/entries/L2_food_biology/*.md        $SD/data/data/entries/L2_food_biology/
cp data/entries/L3_materials_chemistry/*.md $SD/data/data/entries/L3_materials_chemistry/
cp data/entries/L3_materials_elements/*.md  $SD/data/data/entries/L3_materials_elements/
cp data/entries/L3_materials_technology/*.md $SD/data/data/entries/L3_materials_technology/
cp data/entries/L4_agriculture_labor/*.md   $SD/data/data/entries/L4_agriculture_labor/
cp data/entries/L4_tools_rebuilding/*.md    $SD/data/data/entries/L4_tools_rebuilding/
cp data/entries/L5_civilization_memory/*.md $SD/data/data/entries/L5_civilization_memory/
cp data/entries/L5_community_knowledge/*.md $SD/data/data/entries/L5_community_knowledge/

echo "Entries copied:"
find $SD/data/data/entries -name "*.md" | wc -l
```

Expected: **483 files** (as of v1.3 database)

---

## Step 4: Generate the Binary Index

The firmware reads a compact binary index (`entries.idx`), not the markdown files
directly. Generate it with the Python tool:

```bash
# From project root, activate the venv first
source .venv/bin/activate

# Generate index — point it at your SD card
python tools/build_index.py \
    --entries-dir data/entries \
    --output-dir /tmp/index_out

# Copy to SD card
cp /tmp/index_out/entries.idx $SD/index/
cp /tmp/index_out/metadata.json $SD/index/
```

If the index tool isn't available, copy a pre-built index:
```bash
cp exports/entries.idx $SD/index/
cp exports/metadata.json $SD/index/
```

> **Index format:** 2-byte entry count + 117-byte records (EID[32] + Title[64] + Cat[1] + Folder[1] + padding[19])

---

## Step 5: (Optional) Add Diagrams

Diagrams must be 24-bit uncompressed BMP files. See `docs/DIAGRAM_PREPARATION.md`
for full conversion instructions.

```bash
# After converting SVGs to BMP (see DIAGRAM_PREPARATION.md)
cp data/diagrams/*.bmp $SD/data/data/diagrams/
```

---

## Step 6: Verify

Your SD card should look like this:

```
/
├── index/
│   ├── entries.idx          (required)
│   ├── metadata.json        (required)
│   └── bookmarks.txt        (auto-created by firmware on first bookmark)
└── data/
    └── data/
        ├── entries/
        │   ├── L1_immediate_survival/   (~142 .md files)
        │   ├── L2_food_biology/         (~135 .md files)
        │   ├── L3_materials_chemistry/  (subset of ~70)
        │   ├── ...
        │   └── L5_community_knowledge/
        └── diagrams/
            └── (optional .bmp files)
```

Quick check:
```bash
echo "Index:" && ls -lh $SD/index/
echo "Entries:" && find $SD/data/data/entries -name "*.md" | wc -l
echo "Diagrams:" && ls $SD/data/data/diagrams/ 2>/dev/null | wc -l
```

---

## Step 7: Boot the Device

1. Insert the SD card into the device
2. Power on (hold BOOT + plug USB if first time, then drag UF2)
3. Watch for:
   - **Blue LED** → booting
   - **Green LED** → ready
   - **Red LED blink** → error (check serial output at 115200 baud)
4. Splash screen shows `483 entries loaded` ✅

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| "SD card error" on boot | Card not detected / not FAT32 | Reformat as FAT32, reinsert |
| "Index error!" on boot | `entries.idx` missing or corrupt | Re-run `build_index.py`, copy again |
| Browse shows 0 entries | Wrong folder path on SD | Check `/data/data/entries/` exists |
| Subfolders show "Folder 0" | `metadata.json` missing or truncated | Re-copy metadata.json |
| Diagram not loading | BMP not found or wrong format | See `DIAGRAM_PREPARATION.md` |

For detailed diagnostics, connect serial monitor (115200 baud) and read the boot log.

---

## metadata.json Format

The firmware expects exactly this format for subfolder name lookup:

```json
{
  "subtopics": {
    "0": "Immediate Survival",
    "1": "Medical",
    "2": "Water & Fire",
    "3": "Food & Foraging",
    "4": "Navigation",
    "5": "Shelter",
    "6": "Tools & Materials",
    "7": "Long-Term",
    "8": "Civilization"
  }
}
```

> Keep the file under 2KB. The firmware buffers the entire file into RAM.
> Do not add nested objects or arrays.
