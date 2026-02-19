#!/usr/bin/env python3
import datetime as dt
import json
import re
from pathlib import Path

try:
    import yaml
except Exception:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    raise

ROOT = Path(__file__).resolve().parents[1]
ENTRY_ROOT = ROOT / "data" / "entries"
SOURCE_FILE = ROOT / "data" / "sources" / "source_registry.yaml"
ALLOWED_SOURCE_TYPES = {"gov", "academic", "official_manual", "peer_reviewed"}
FORBIDDEN_TAGS = {"blog", "hack", "anecdotal"}
HAZARD_SUBTOPICS = {"medical_first_aid", "water", "fire", "basic_chemistry", "electricity_basics"}


def parse_front_matter(md_text: str):
    if not md_text.startswith("---\n"):
        return None
    end = md_text.find("\n---\n", 4)
    if end == -1:
        return None
    block = md_text[4:end]
    return yaml.safe_load(block)


def load_sources():
    obj = yaml.safe_load(SOURCE_FILE.read_text())
    sources = {s["source_id"]: s for s in obj.get("sources", [])}
    return sources


def valid_date(s):
    try:
        dt.date.fromisoformat(s)
        return True
    except Exception:
        return False


def validate_entry(meta, path, source_map):
    errs = []
    req = ["id", "title", "category", "subtopic", "tags", "region_relevance", "summary", "steps", "warnings", "related_entries", "sources", "last_verified", "confidence"]
    for k in req:
        if k not in meta:
            errs.append(f"missing field: {k}")

    if "id" in meta and not re.match(r"^[a-z0-9][a-z0-9-]{2,80}$", str(meta["id"])):
        errs.append("invalid id format")

    if "sources" in meta:
        for sid in meta.get("sources", []):
            if sid not in source_map:
                errs.append(f"unknown source: {sid}")
            else:
                st = source_map[sid].get("type")
                if st not in ALLOWED_SOURCE_TYPES:
                    errs.append(f"source {sid} has disallowed type: {st}")

    tags = set(meta.get("tags", []))
    bad_tags = tags & FORBIDDEN_TAGS
    if bad_tags:
        errs.append(f"forbidden tags present: {sorted(bad_tags)}")

    if meta.get("subtopic") in HAZARD_SUBTOPICS and not meta.get("warnings"):
        errs.append("hazard topic requires warnings")

    if not meta.get("related_entries"):
        errs.append("requires at least 1 related entry")

    if not valid_date(str(meta.get("last_verified", ""))):
        errs.append("last_verified must be ISO date YYYY-MM-DD")

    if meta.get("confidence") not in {"high", "medium", "low"}:
        errs.append("confidence must be high|medium|low")

    return errs


def main():
    source_map = load_sources()
    files = sorted(ENTRY_ROOT.rglob("*.md"))
    total_errors = 0
    for f in files:
        meta = parse_front_matter(f.read_text())
        if not isinstance(meta, dict):
            print(f"[ERR] {f}: missing/invalid YAML front matter")
            total_errors += 1
            continue
        errs = validate_entry(meta, f, source_map)
        if errs:
            print(f"[ERR] {f}")
            for e in errs:
                print(f"  - {e}")
            total_errors += len(errs)

    if total_errors:
        print(f"\nValidation failed with {total_errors} error(s).")
        raise SystemExit(1)

    print(f"Validation OK: {len(files)} entries, {len(source_map)} registered sources.")


if __name__ == "__main__":
    main()
