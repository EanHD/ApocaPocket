#!/usr/bin/env python3
"""
ApocaPocket Index Builder
Generates entries.idx and metadata.json from the database markdown files.

Usage:
    python tools/build_index.py

Output files (in exports/):
    entries.idx    -- binary index for firmware
    metadata.json  -- subfolder display name map for firmware

Then copy to SD card:
    cp exports/entries.idx  /your/sd/card/index/
    cp exports/metadata.json /your/sd/card/index/

Index binary format:
    [2 bytes] entry count (little-endian uint16)
    [N x 128 bytes] records:
        [ 0-47]  EID string, null-padded     (48 bytes)
        [48-111] Title string, null-padded   (64 bytes)
        [112]    Category (0-4)              ( 1 byte)
        [113]    FolderIdx (0-20)            ( 1 byte)
        [114-127] Padding, zeroed            (14 bytes)
"""

import os
import re
import json
import struct
import sys
from pathlib import Path

# ── Folder list: MUST be sorted alphabetically, MUST match FOLDERS[] in sdcard.cpp ──
FOLDERS = [
    "L1_disaster",              # 0
    "L1_fire",                  # 1
    "L1_medical",               # 2
    "L1_navigation",            # 3
    "L1_shelter",               # 4
    "L1_strategy",              # 5
    "L1_urban",                 # 6
    "L1_water",                 # 7
    "L1_wilderness",            # 8
    "L2_food_biology",          # 9
    "L2_hunting",               # 10
    "L2_mushrooms",             # 11
    "L2_nutrition",             # 12
    "L2_plants",                # 13
    "L2_regional",              # 14
    "L3_materials_chemistry",   # 15
    "L3_materials_elements",    # 16
    "L3_materials_technology",  # 17
    "L3_water",                 # 18
    "L4_agriculture",           # 19
    "L4_agriculture_labor",     # 20
    "L4_tools_rebuilding",      # 21
    "L5_civilization_memory",   # 22
    "L5_community_knowledge",   # 23
    "L5_sanitation",            # 24
]

# Category: determined by folder prefix (L1=0, L2=1, L3=2, L4=3, L5=4)
def folder_category(folder_name):
    tier = folder_name[1]  # '1'..'5'
    return int(tier) - 1

# Human-readable display names for each folder (shown in browse menu)
SUBFOLDER_NAMES = {
    0:  "Disaster Response",
    1:  "Fire",
    2:  "Medical",
    3:  "Navigation",
    4:  "Shelter",
    5:  "Strategy & Prep",
    6:  "Urban Survival",
    7:  "Water",
    8:  "Wilderness",
    9:  "Food Prep",
    10: "Hunting & Fishing",
    11: "Mushrooms",
    12: "Nutrition",
    13: "Plants",
    14: "Regional Guides",
    15: "Chemistry",
    16: "Elements",
    17: "Technology",
    18: "Water Treatment",
    19: "Agriculture",
    20: "Agri. Labor",
    21: "Tools & Rebuild",
    22: "Civilization",
    23: "Community",
    24: "Sanitation",
}

RECORD_SIZE    = 128  # EID[48] + Title[64] + Cat[1] + FolderIdx[1] + Padding[14]
EID_SIZE       = 48
TITLE_SIZE     = 64
TITLE_DISP_LEN = 26  # Must match TITLE_DISPLAY_LEN in config.h


def extract_title(md_path, eid):
    """Extract display title from a markdown file.
    Priority: YAML frontmatter 'title:', then first '# heading', then EID."""
    try:
        with open(md_path, encoding="utf-8", errors="replace") as f:
            in_front = False
            front_done = False
            for i, line in enumerate(f):
                line = line.rstrip("\r\n")
                if i == 0 and line == "---":
                    in_front = True
                    continue
                if in_front:
                    if line == "---":
                        in_front = False
                        front_done = True
                        continue
                    m = re.match(r'^title:\s*["\']?(.*?)["\']?\s*$', line)
                    if m:
                        return m.group(1).strip()
                    continue
                # Outside frontmatter — look for first # heading
                if line.startswith("# "):
                    return line[2:].strip()
                # Skip blank lines but stop after a few non-blank lines
                if i > 20:
                    break
    except OSError:
        pass
    # Fallback: format the EID as a title
    return eid.replace("-", " ").replace("_", " ").title()


def to_ascii(s, maxlen):
    """Truncate to maxlen and strip non-ASCII printable characters."""
    out = ""
    for c in s:
        if 32 <= ord(c) <= 126:
            out += c
        if len(out) >= maxlen:
            break
    return out


def build_index(entries_dir, output_dir):
    entries_dir = Path(entries_dir)
    output_dir  = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    missing_folders = []

    for folder_idx, folder_name in enumerate(FOLDERS):
        folder_path = entries_dir / folder_name
        if not folder_path.exists():
            missing_folders.append(folder_name)
            print(f"  ⚠️  Folder not found: {folder_path}")
            continue

        cat = folder_category(folder_name)
        md_files = sorted(folder_path.glob("*.md"))

        for md_path in md_files:
            eid = md_path.stem  # filename without .md

            # Sanitize EID to ASCII printable, max EID_SIZE-1 chars
            eid_clean = to_ascii(eid, EID_SIZE - 1)
            if not eid_clean:
                print(f"  ⚠️  Skipping bad EID: {md_path}")
                continue

            raw_title = extract_title(md_path, eid)
            title_full = to_ascii(raw_title, TITLE_SIZE - 1)
            title_disp = to_ascii(raw_title, TITLE_DISP_LEN)

            records.append({
                "eid":       eid_clean,
                "title":     title_full,
                "title_disp": title_disp,
                "category":  cat,
                "folder_idx": folder_idx,
            })

    total = len(records)
    print(f"\n  Total entries: {total}")

    if total > 65535:
        print("ERROR: Too many entries (max 65535)")
        sys.exit(1)

    # Write entries.idx
    idx_path = output_dir / "entries.idx"
    with open(idx_path, "wb") as f:
        # 2-byte header: entry count (little-endian)
        f.write(struct.pack("<H", total))

        for r in records:
            rec = bytearray(RECORD_SIZE)
            # [0-47] EID (48 bytes)
            eid_bytes = r["eid"].encode("ascii")[:EID_SIZE - 1]
            rec[0:len(eid_bytes)] = eid_bytes
            # [48-111] Title (64 bytes)
            title_bytes = r["title"].encode("ascii")[:TITLE_SIZE - 1]
            rec[EID_SIZE:EID_SIZE + len(title_bytes)] = title_bytes
            # [112] Category
            rec[EID_SIZE + TITLE_SIZE] = r["category"]
            # [113] FolderIdx
            rec[EID_SIZE + TITLE_SIZE + 1] = r["folder_idx"]
            # [114-127] Padding — already zero from bytearray init
            f.write(rec)

    print(f"  Written: {idx_path}  ({idx_path.stat().st_size} bytes)")

    # Write metadata.json
    meta_path = output_dir / "metadata.json"
    subtopics = {str(k): v for k, v in SUBFOLDER_NAMES.items()}
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({"subtopics": subtopics}, f, indent=2)
    print(f"  Written: {meta_path}")

    if missing_folders:
        print(f"\n  ⚠️  {len(missing_folders)} folders missing — "
              f"index will not contain their entries")
        for m in missing_folders:
            print(f"     - {m}")

    # Stats by category
    cats = ["Immediate Survival", "Food & Biology", "Materials & Water",
            "Tools & Rebuild", "Civilization"]
    print("\n  Entries by category:")
    for ci, cname in enumerate(cats):
        count = sum(1 for r in records if r["category"] == ci)
        print(f"    [{ci}] {cname}: {count}")

    return total


if __name__ == "__main__":
    script_dir  = Path(__file__).parent
    project_dir = script_dir.parent
    entries_dir = project_dir / "data" / "entries"
    output_dir  = project_dir / "data" / "index"

    print("=== ApocaPocket Index Builder ===")
    print(f"Entries dir: {entries_dir}")
    print(f"Output dir:  {output_dir}")
    print()

    if not entries_dir.exists():
        print(f"ERROR: entries dir not found: {entries_dir}")
        sys.exit(1)

    total = build_index(entries_dir, output_dir)

    print(f"\n✅ Done — {total} entries indexed")
    print("\nNext steps:")
    print("  1. Drag the repo's data/ folder to your SD card root")
    print("  2. SD card should have: data/entries/, data/diagrams/, data/index/")
    print("  3. Flash firmware and boot the device")
