#!/usr/bin/env python3
"""
Export Apocalypse Field Node database to RP2040-Zero compact format.

Converts markdown+YAML entries → compact .txt files + binary index + trigram search index.
Designed for 264KB RAM constraint of RP2040.

Usage:
    python tools/export_rp2040.py --output /path/to/sd/
    python tools/export_rp2040.py --output exports/rp2040_sd/
"""

import argparse
import struct
import json
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("pip install pyyaml")
    raise

ROOT = Path(__file__).resolve().parents[1]
ENTRY_ROOT = ROOT / "data" / "entries"

CATEGORY_MAP = {
    "L1_immediate_survival": 0,
    "L2_food_biology": 1,
    "L3_materials_elements": 2,
    "L4_tools_rebuilding": 3,
    "L5_civilization_memory": 4,
}

CATEGORY_DIRS = {0: "L1", 1: "L2", 2: "L3", 3: "L4", 4: "L5"}

# Collect all subtopics dynamically
SUBTOPIC_MAP = {}
_subtopic_counter = 0


def get_subtopic_id(subtopic):
    global _subtopic_counter
    if subtopic not in SUBTOPIC_MAP:
        SUBTOPIC_MAP[subtopic] = _subtopic_counter
        _subtopic_counter += 1
    return SUBTOPIC_MAP[subtopic]


CONFIDENCE_MAP = {"high": 0, "medium": 1, "low": 2}

# Tag universe — top 128 tags get bitfield positions
TAG_UNIVERSE = {}
_tag_counter = 0


def register_tags(tags):
    global _tag_counter
    for t in tags:
        if t not in TAG_UNIVERSE and _tag_counter < 128:
            TAG_UNIVERSE[t] = _tag_counter
            _tag_counter += 1


def tags_to_bitfield(tags):
    """Convert tag list to 16-byte (128-bit) bitfield."""
    bf = bytearray(16)
    for t in tags:
        idx = TAG_UNIVERSE.get(t)
        if idx is not None:
            byte_pos = idx // 8
            bit_pos = idx % 8
            bf[byte_pos] |= (1 << bit_pos)
    return bytes(bf)


def parse_front_matter(md_text):
    if not md_text.startswith("---\n"):
        return None, md_text
    end = md_text.find("\n---\n", 4)
    if end == -1:
        return None, md_text
    block = md_text[4:end]
    body = md_text[end + 5:]
    return yaml.safe_load(block), body.strip()


def entry_to_compact_txt(meta, body):
    """Convert to RP2040-friendly compact text format."""
    lines = []
    lines.append(f"TITLE: {meta['title']}")
    lines.append(f"CAT: {meta['category'][:2]}")
    lines.append(f"SUB: {meta['subtopic']}")
    lines.append(f"TAGS: {','.join(meta.get('tags', []))}")
    lines.append(f"REGION: {','.join(meta.get('region_relevance', []))}")
    lines.append(f"CONFIDENCE: {meta.get('confidence', 'medium')}")
    lines.append("---")
    lines.append("")
    lines.append("[SUMMARY]")
    lines.append(meta.get("summary", ""))
    lines.append("")
    lines.append("[STEPS]")
    for i, step in enumerate(meta.get("steps", []), 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    lines.append("[WARNINGS]")
    for w in meta.get("warnings", []):
        lines.append(f"! {w}")
    lines.append("")

    related = meta.get("related_entries", [])
    if related:
        lines.append("[RELATED]")
        for r in related:
            lines.append(f"> {r}")
        lines.append("")

    sources = meta.get("sources", [])
    if sources:
        lines.append("[SOURCES]")
        for s in sources:
            lines.append(f"@ {s}")

    return "\n".join(lines)


def build_trigram_index(entries):
    """Build trigram → entry indices mapping."""
    trigram_map = defaultdict(set)
    for idx, (eid, meta) in enumerate(entries):
        # Index title + tags + summary
        text = (
            meta.get("title", "").lower() + " " +
            " ".join(meta.get("tags", [])).lower() + " " +
            meta.get("summary", "").lower()
        )
        for i in range(len(text) - 2):
            tri = text[i:i+3]
            if tri.strip():  # skip whitespace-only trigrams
                trigram_map[tri].add(idx)
    return trigram_map


def write_binary_index(entries, out_dir):
    """Write entries.idx — fixed-record binary index."""
    idx_path = out_dir / "index" / "entries.idx"
    idx_path.parent.mkdir(parents=True, exist_ok=True)

    with idx_path.open("wb") as f:
        # Header: entry count
        f.write(struct.pack("<H", len(entries)))

        for i, (eid, meta) in enumerate(entries):
            # 32 bytes: entry ID
            id_bytes = eid.encode("utf-8")[:32].ljust(32, b"\x00")
            f.write(id_bytes)

            # 64 bytes: title
            title_bytes = meta["title"].encode("utf-8")[:64].ljust(64, b"\x00")
            f.write(title_bytes)

            # 1 byte: category
            cat_id = CATEGORY_MAP.get(meta["category"], 0)
            f.write(struct.pack("B", cat_id))

            # 1 byte: subtopic
            sub_id = get_subtopic_id(meta.get("subtopic", ""))
            f.write(struct.pack("B", sub_id))

            # 2 bytes: entry index (for file lookup)
            f.write(struct.pack("<H", i))

            # 1 byte: confidence
            conf = CONFIDENCE_MAP.get(meta.get("confidence", "medium"), 1)
            f.write(struct.pack("B", conf))

            # 16 bytes: tag bitfield
            f.write(tags_to_bitfield(meta.get("tags", [])))

    print(f"  entries.idx: {len(entries)} entries, {idx_path.stat().st_size} bytes")


def write_trigram_index(trigram_map, out_dir):
    """Write fts.idx — trigram search index."""
    fts_path = out_dir / "index" / "fts.idx"

    with fts_path.open("wb") as f:
        # Header: trigram count
        f.write(struct.pack("<I", len(trigram_map)))

        for tri, entry_indices in sorted(trigram_map.items()):
            # 3 bytes: trigram
            tri_bytes = tri.encode("utf-8")[:3].ljust(3, b"\x00")
            f.write(tri_bytes)

            # 2 bytes: count
            indices = sorted(entry_indices)[:255]  # cap at 255 matches
            f.write(struct.pack("<H", len(indices)))

            # N × 2 bytes: entry indices
            for idx in indices:
                f.write(struct.pack("<H", idx))

    print(f"  fts.idx: {len(trigram_map)} trigrams, {fts_path.stat().st_size} bytes")


def write_metadata(out_dir):
    """Write subtopic and tag maps for firmware reference."""
    meta = {
        "subtopics": {v: k for k, v in SUBTOPIC_MAP.items()},
        "tags": {v: k for k, v in TAG_UNIVERSE.items()},
        "categories": {v: k for k, v in CATEGORY_MAP.items()},
    }
    (out_dir / "index" / "metadata.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )


def main():
    ap = argparse.ArgumentParser(description="Export database to RP2040 format")
    ap.add_argument("--output", required=True, help="Output directory (SD card root)")
    args = ap.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    # Collect all entries
    entries = []
    md_files = sorted(ENTRY_ROOT.rglob("*.md"))

    # First pass: register all tags
    for f in md_files:
        meta, body = parse_front_matter(f.read_text())
        if not isinstance(meta, dict):
            continue
        register_tags(meta.get("tags", []))

    # Second pass: convert and write
    for f in md_files:
        meta, body = parse_front_matter(f.read_text())
        if not isinstance(meta, dict):
            continue

        eid = meta["id"]
        cat_id = CATEGORY_MAP.get(meta["category"], 0)
        cat_dir = CATEGORY_DIRS[cat_id]

        # Write compact .txt
        data_dir = out / "data" / cat_dir
        data_dir.mkdir(parents=True, exist_ok=True)
        txt = entry_to_compact_txt(meta, body)
        (data_dir / f"{eid}.txt").write_text(txt, encoding="utf-8")

        entries.append((eid, meta))

    print(f"Exported {len(entries)} entries to compact text format")

    # Build indices
    write_binary_index(entries, out)
    trigram_map = build_trigram_index(entries)
    write_trigram_index(trigram_map, out)
    write_metadata(out)

    # Stats
    total_size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    print(f"\nTotal SD card usage: {total_size / 1024:.0f} KB ({total_size / 1024 / 1024:.1f} MB)")
    print(f"Tags registered: {len(TAG_UNIVERSE)}")
    print(f"Subtopics: {len(SUBTOPIC_MAP)}")
    print(f"\nReady for RP2040-Zero deployment!")


if __name__ == "__main__":
    main()
