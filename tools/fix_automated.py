#!/usr/bin/env python3
"""
ApocaPocket Phase 1 Automated Fixer
Handles mechanical, safe transformations:
  - Italic (*text*) → plain text
  - Nested bullets → flattened
  - Simple key/value tables → bold bullets (Pattern A only)
  - Flags complex tables for manual review

Usage:
    python tools/fix_automated.py --dry-run
    python tools/fix_automated.py --apply
    python tools/fix_automated.py --apply --category L1_medical
    python tools/fix_automated.py --apply --worst 50  (uses audit scores)
"""

import glob, re, os, sys, json
from copy import deepcopy

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRIES_DIR = os.path.join(REPO_ROOT, 'data', 'entries')

# ─── Italic fix ────────────────────────────────────────────────────────────────
def fix_italics(line):
    """Remove *italic* markers (not **bold**). Returns fixed line."""
    # Match *text* but not **text**
    return re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\1', line)

# ─── Nested bullet fix ─────────────────────────────────────────────────────────
def fix_nested_bullets(lines):
    """Flatten nested bullets (  - item → - item)."""
    out = []
    for line in lines:
        # Detect nested bullet: 2+ spaces followed by -
        if re.match(r'^  +- ', line):
            # Flatten: strip leading spaces before the dash
            line = re.sub(r'^  +(-)', r'\1', line)
        out.append(line)
    return out

# ─── Table detection and conversion ───────────────────────────────────────────
def classify_table(table_lines):
    """
    Classify a table block as:
      'kv'      → simple 2-col key/value (safe to auto-convert)
      'complex' → 3+ cols or comparison table (flag for manual)
    """
    data_rows = [l for l in table_lines
                 if l.startswith('|') and not re.match(r'^\|[-| ]+\|$', l)]
    if not data_rows:
        return 'complex'

    # Check column count from header row
    header = data_rows[0] if data_rows else ''
    cols = len([c for c in header.split('|') if c.strip()]) if header else 0

    if cols == 2:
        return 'kv'
    return 'complex'


def convert_kv_table(table_lines):
    """Convert a 2-column key/value table to bold bullet list."""
    result = []
    for line in table_lines:
        # Skip separator rows (|---|---|)
        if re.match(r'^\|[-| ]+\|$', line):
            continue
        if not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) == 2:
            key, val = parts
            # Skip header row if it looks like a header (all caps or title-cased with no real value)
            if re.match(r'^[A-Z][a-z]+$', val) and re.match(r'^[A-Z][a-z]+$', key):
                # Probably a header row — skip
                continue
            result.append(f'**{key}:** {val}')
        elif len(parts) == 1:
            result.append(f'- {parts[0]}')
    return result


def process_tables(lines):
    """
    Find table blocks in lines.
    Convert Pattern A (2-col KV) automatically.
    Add MANUAL_REVIEW comment for complex tables.
    Returns (new_lines, stats)
    """
    out = []
    stats = {'auto_converted': 0, 'manual_flagged': 0}
    i = 0
    while i < len(lines):
        line = lines[i]
        # Start of a table block
        if line.startswith('|'):
            table_block = []
            while i < len(lines) and lines[i].startswith('|'):
                table_block.append(lines[i])
                i += 1
            table_type = classify_table(table_block)
            if table_type == 'kv':
                converted = convert_kv_table(table_block)
                out.extend(converted)
                stats['auto_converted'] += 1
            else:
                # Flag for manual review
                out.append('<!-- MANUAL_REVIEW: complex table below — convert to bullets -->')
                out.extend(table_block)
                stats['manual_flagged'] += 1
        else:
            out.append(line)
            i += 1
    return out, stats


# ─── Main fixer ───────────────────────────────────────────────────────────────
def fix_entry(path, dry_run=True):
    """
    Apply all Phase 1 fixes to a single MD file.
    Returns (changed: bool, summary: str, new_content: str)
    """
    with open(path, encoding='utf-8', errors='replace') as f:
        original = f.read()

    lines = original.splitlines()
    changes = []

    # Fix italics line by line
    fixed_lines = []
    italic_count = 0
    for line in lines:
        fixed = fix_italics(line)
        if fixed != line:
            italic_count += 1
        fixed_lines.append(fixed)
    if italic_count:
        changes.append(f'fixed {italic_count} italic lines')

    # Flatten nested bullets
    pre_nested = fixed_lines[:]
    fixed_lines = fix_nested_bullets(fixed_lines)
    nested_fixed = sum(1 for a, b in zip(pre_nested, fixed_lines) if a != b)
    if nested_fixed:
        changes.append(f'flattened {nested_fixed} nested bullets')

    # Convert tables
    fixed_lines, table_stats = process_tables(fixed_lines)
    if table_stats['auto_converted']:
        changes.append(f"converted {table_stats['auto_converted']} KV table(s) to bullets")
    if table_stats['manual_flagged']:
        changes.append(f"flagged {table_stats['manual_flagged']} complex table(s) for manual review")

    new_content = '\n'.join(fixed_lines)
    # Normalize trailing newline
    if original.endswith('\n') and not new_content.endswith('\n'):
        new_content += '\n'

    changed = new_content != original
    summary = ', '.join(changes) if changes else 'no changes'

    if not dry_run and changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changed, summary, new_content


# ─── CLI ──────────────────────────────────────────────────────────────────────
def main():
    dry_run = '--apply' not in sys.argv
    category_filter = None
    worst_n = None

    for i, arg in enumerate(sys.argv):
        if arg == '--category' and i + 1 < len(sys.argv):
            category_filter = sys.argv[i + 1]
        if arg == '--worst' and i + 1 < len(sys.argv):
            worst_n = int(sys.argv[i + 1])

    if dry_run:
        print('DRY RUN — no files will be modified. Use --apply to write changes.\n')

    # Collect entries
    pattern = os.path.join(ENTRIES_DIR, '**', '*.md')
    all_entries = sorted(glob.glob(pattern, recursive=True))

    if category_filter:
        all_entries = [p for p in all_entries if category_filter in p]
        print(f'Filtered to category: {category_filter} ({len(all_entries)} entries)\n')

    if worst_n:
        # Use audit scores to prioritize
        try:
            sys.path.insert(0, os.path.join(REPO_ROOT, 'tools'))
            from audit_content import audit_entry
            scored = sorted(
                [audit_entry(p) for p in all_entries],
                key=lambda r: -r['score']
            )
            all_entries = [r['path'] for r in scored[:worst_n]]
            print(f'Processing worst {worst_n} entries by audit score\n')
        except Exception as e:
            print(f'Warning: could not load audit scores ({e}), processing all\n')

    total = len(all_entries)
    changed_count = 0
    skipped = 0

    print(f'Processing {total} entries...\n')

    for path in all_entries:
        rel = os.path.relpath(path, REPO_ROOT)
        try:
            changed, summary, _ = fix_entry(path, dry_run=dry_run)
            if changed:
                action = 'WOULD FIX' if dry_run else 'FIXED'
                print(f'  [{action}] {rel}')
                print(f'           {summary}')
                changed_count += 1
            else:
                skipped += 1
        except Exception as e:
            print(f'  [ERROR]  {rel}: {e}')

    print(f'\n{"─"*50}')
    print(f'Total entries:   {total}')
    print(f'{"Would fix" if dry_run else "Fixed"}:       {changed_count}')
    print(f'Already clean:   {skipped}')
    if dry_run and changed_count:
        print(f'\nRun with --apply to write {changed_count} changes.')


if __name__ == '__main__':
    main()
