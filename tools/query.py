#!/usr/bin/env python3
import argparse
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "index" / "fieldnode.db"


def main():
    ap = argparse.ArgumentParser(description="Search Apocalypse Field Node")
    ap.add_argument("q", help="FTS query")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--category", default="")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    where = ""
    params = [args.q]
    if args.category:
        where = " AND e.category = ?"
        params.append(args.category)
    params.append(args.limit)

    sql = f"""
      SELECT e.id, e.title, e.category, snippet(entries_fts, 2, '[', ']', ' … ', 16) AS snip
      FROM entries_fts
      JOIN entries e ON e.id = entries_fts.id
      WHERE entries_fts MATCH ? {where}
      LIMIT ?
    """
    for row in conn.execute(sql, params):
        print(f"- {row[0]} | {row[1]} | {row[2]}\n  {row[3]}\n")


if __name__ == "__main__":
    main()
