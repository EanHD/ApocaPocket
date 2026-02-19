#!/usr/bin/env python3
"""
Best-effort snapshot fetcher for source registry URLs.
For Pi Zero use --limit to download in batches.
"""
from pathlib import Path
import argparse
import hashlib
import urllib.request
import urllib.parse

try:
    import yaml
except Exception:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    raise

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "sources" / "source_registry.yaml"


def guess_ext(url: str) -> str:
    p = urllib.parse.urlparse(url).path.lower()
    if p.endswith(".pdf"):
        return ".pdf"
    if p.endswith(".json"):
        return ".json"
    return ".html"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="max sources to fetch this run")
    ap.add_argument("--timeout", type=int, default=30)
    args = ap.parse_args()

    data = yaml.safe_load(REGISTRY.read_text())
    sources = data.get("sources", [])
    done = 0

    for s in sources:
        if args.limit and done >= args.limit:
            break
        url = s.get("url")
        out = ROOT / s.get("local_snapshot_path")
        out.parent.mkdir(parents=True, exist_ok=True)

        if out.exists() and out.stat().st_size > 0:
            s["sha256"] = sha256_file(out)
            continue

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "apocalypse-field-node/1.0"})
            with urllib.request.urlopen(req, timeout=args.timeout) as r:
                body = r.read()
            if not out.suffix:
                out = out.with_suffix(guess_ext(url))
                s["local_snapshot_path"] = str(out.relative_to(ROOT))
            out.write_bytes(body)
            s["sha256"] = sha256_file(out)
            done += 1
            print(f"[OK] {s['source_id']} -> {out}")
        except Exception as e:
            print(f"[WARN] {s.get('source_id')}: {e}")

    REGISTRY.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    print("Registry updated.")


if __name__ == "__main__":
    main()
