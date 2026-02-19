#!/usr/bin/env python3
import sqlite3
from pathlib import Path

try:
    import yaml
except Exception:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    raise

ROOT = Path(__file__).resolve().parents[1]
ENTRY_ROOT = ROOT / "data" / "entries"
DB_PATH = ROOT / "index" / "fieldnode.db"


def parse_front_matter(md_text: str):
    if not md_text.startswith("---\n"):
        return None, md_text
    end = md_text.find("\n---\n", 4)
    if end == -1:
        return None, md_text
    block = md_text[4:end]
    body = md_text[end + 5 :]
    return yaml.safe_load(block), body.strip()


def init_db(conn):
    conn.executescript(
        """
        PRAGMA journal_mode=WAL;
        PRAGMA synchronous=NORMAL;

        DROP TABLE IF EXISTS entries;
        DROP TABLE IF EXISTS relations;
        DROP TABLE IF EXISTS entry_sources;
        DROP TABLE IF EXISTS entries_fts;

        CREATE TABLE entries (
          id TEXT PRIMARY KEY,
          title TEXT NOT NULL,
          category TEXT NOT NULL,
          subtopic TEXT NOT NULL,
          tags TEXT NOT NULL,
          region_relevance TEXT NOT NULL,
          summary TEXT NOT NULL,
          steps TEXT NOT NULL,
          warnings TEXT NOT NULL,
          last_verified TEXT NOT NULL,
          confidence TEXT NOT NULL,
          body TEXT NOT NULL,
          path TEXT NOT NULL
        );

        CREATE TABLE relations (
          entry_id TEXT NOT NULL,
          related_id TEXT NOT NULL,
          relation_type TEXT DEFAULT 'related'
        );

        CREATE TABLE entry_sources (
          entry_id TEXT NOT NULL,
          source_id TEXT NOT NULL
        );

        CREATE VIRTUAL TABLE entries_fts USING fts5(
          id UNINDEXED,
          title,
          summary,
          steps,
          warnings,
          tags,
          body,
          tokenize='porter unicode61'
        );
        """
    )


def main():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    errors = []
    for f in sorted(ENTRY_ROOT.rglob("*.md")):
        try:
            text = f.read_text(encoding="utf-8")
            meta, body = parse_front_matter(text)
            if not isinstance(meta, dict):
                continue

            tags = ",".join(meta.get("tags", []))
            regions = ",".join(meta.get("region_relevance", []))
            steps = "\n".join(str(s) for s in meta.get("steps", []))
            warnings = "\n".join(str(w) for w in meta.get("warnings", []))

            conn.execute(
                """
                INSERT INTO entries (id,title,category,subtopic,tags,region_relevance,summary,steps,warnings,last_verified,confidence,body,path)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    meta.get("id"),
                    meta.get("title"),
                    meta.get("category"),
                    meta.get("subtopic"),
                    tags,
                    regions,
                    meta.get("summary"),
                    steps,
                    warnings,
                    meta.get("last_verified"),
                    meta.get("confidence"),
                    body,
                    str(f.relative_to(ROOT)),
                ),
            )

            conn.execute(
                "INSERT INTO entries_fts (id,title,summary,steps,warnings,tags,body) VALUES (?,?,?,?,?,?,?)",
                (meta.get("id"), meta.get("title"), meta.get("summary"), steps, warnings, tags, body),
            )

            for rid in meta.get("related_entries", []):
                conn.execute("INSERT INTO relations (entry_id, related_id, relation_type) VALUES (?,?,?)", (meta.get("id"), rid, "related"))

            for sid in meta.get("sources", []):
                conn.execute("INSERT INTO entry_sources (entry_id, source_id) VALUES (?,?)", (meta.get("id"), sid))
        
        except Exception as e:
            errors.append(f"{f.relative_to(ROOT)}: {e}")
            continue

    conn.commit()

    n_entries = conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    print(f"Built index at {DB_PATH} with {n_entries} entries.")
    
    if errors:
        print(f"\n⚠️  {len(errors)} entries had errors and were skipped:")
        for err in errors[:10]:  # Show first 10
            print(f"  - {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    
    conn.close()


if __name__ == "__main__":
    main()
