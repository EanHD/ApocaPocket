#!/usr/bin/env python3
"""
ApocaPocket Content Audit Tool
Scans all 484 MD entries and flags content that won't render correctly on device.

Usage:
    python tools/audit_content.py
    python tools/audit_content.py --csv        # write audit_results.csv
    python tools/audit_content.py --worst 20   # show top N worst offenders

Device constraints (from compiled firmware):
    Section title (##) max: 22 chars bold
    Entry title (#)    max: 25 chars regular
    Lines per card:        11 clean, 13 scrollable
    Tables:                NOT supported (renders as raw pipes)
    Italic (*text*):       NOT supported (no italic font loaded)
    Nested bullets:        Rendered flat (indent ignored)
"""

import glob, re, csv, os, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Weights — tuned to device impact severity
SECTION_TITLE_MAX  = 22   # bold px budget ~224px
ENTRY_TITLE_MAX    = 25   # regular px budget ~174px header + menus
MAX_CONTENT_LINES  = 150  # >150 = navigation fatigue (>12 cards)
SCORE_TABLE        = 5    # renders as garbage
SCORE_LONG_SECTION = 3    # truncated on card header
SCORE_LONG_ENTRY   = 3    # too many (cont.) cards
SCORE_LONG_TITLE   = 2    # truncated in menus
SCORE_ITALIC       = 2    # shows as *asterisks*
SCORE_NESTED       = 1    # rendered flat but not broken


def strip_frontmatter(lines):
    if lines and lines[0].strip() == '---':
        for i, l in enumerate(lines[1:], 1):
            if l.strip() == '---':
                return lines[i + 1:]
    return lines


def audit_entry(path):
    fname = os.path.relpath(path, REPO_ROOT)
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            raw = f.read().splitlines()
    except Exception as e:
        return {'score': 99, 'file': fname, 'issues': [f'read error: {e}'], 'path': path}

    lines = strip_frontmatter(raw)
    issues = []
    score  = 0

    # Entry title (first # heading that isn't ##)
    h1 = next((l[2:].strip() for l in lines
               if l.startswith('# ') and not l.startswith('## ')), '')
    if h1 and len(h1) > ENTRY_TITLE_MAX:
        issues.append(f'title {len(h1)} chars (max {ENTRY_TITLE_MAX}): "{h1[:40]}"')
        score += SCORE_LONG_TITLE

    # Section titles ## — the most common failure
    for l in lines:
        if l.startswith('## '):
            title = l[3:].strip()
            if len(title) > SECTION_TITLE_MAX:
                issues.append(f'## too long ({len(title)}ch): "{title[:35]}"')
                score += SCORE_LONG_SECTION

    # Tables — critical, renders as raw pipes
    # Skip pipe chars inside ``` code blocks (they're legitimate)
    in_code = False
    table_lines = 0
    for l in lines:
        if l.startswith('```'):
            in_code = not in_code
        if not in_code and l.startswith('|'):
            table_lines += 1
    if table_lines:
        issues.append(f'{table_lines} table lines (renders as pipe characters)')
        score += SCORE_TABLE

    # Italic-only (* but not **) — shows as asterisks
    italic_count = sum(1 for l in lines if re.search(r'(?<!\*)\*(?!\*)\w', l))
    if italic_count:
        issues.append(f'{italic_count} lines with italic (*text* — no italic font)')
        score += SCORE_ITALIC

    # Nested bullets — indent is ignored by renderer
    nested = sum(1 for l in lines if re.match(r'^  +- ', l))
    if nested:
        issues.append(f'{nested} nested bullet lines (rendered flat)')
        score += SCORE_NESTED

    # Entry length — too many (cont.) cards
    content_lines = len([l for l in lines if l.strip()])
    if content_lines > MAX_CONTENT_LINES:
        excess = content_lines - MAX_CONTENT_LINES
        issues.append(f'{content_lines} content lines (max {MAX_CONTENT_LINES}, ~{content_lines//11} cards)')
        score += SCORE_LONG_ENTRY + (excess // 50)  # extra points for very long entries

    return {
        'score':  score,
        'file':   fname,
        'issues': issues,
        'path':   path,
    }


def main():
    write_csv = '--csv' in sys.argv
    worst_n   = 10
    for i, arg in enumerate(sys.argv):
        if arg == '--worst' and i + 1 < len(sys.argv):
            worst_n = int(sys.argv[i + 1])

    entries = sorted(glob.glob(os.path.join(REPO_ROOT, 'data/entries/**/*.md'), recursive=True))
    if not entries:
        print('No entries found. Run from repo root or ensure data/entries/ exists.')
        sys.exit(1)

    results = [audit_entry(p) for p in entries]
    broken  = [r for r in results if r['issues']]
    broken.sort(key=lambda r: -r['score'])
    clean   = len(results) - len(broken)

    # Summary
    print(f'\nApocaPocket Content Audit')
    print(f'─────────────────────────')
    print(f'Entries scanned: {len(results)}')
    print(f'Clean:           {clean} ({clean*100//len(results)}%)')
    print(f'Issues found:    {len(broken)} ({len(broken)*100//len(results)}%)')
    print()

    # Category breakdown
    cats = {
        'Long section title (##)': 0,
        'Long entry title (#)':    0,
        'Table':                   0,
        'Italic (*text*)':         0,
        'Nested bullets':          0,
        'Entry too long':          0,
    }
    for r in broken:
        for issue in r['issues']:
            if issue.startswith('## too long'): cats['Long section title (##)'] += 1
            elif issue.startswith('title '): cats['Long entry title (#)'] += 1
            elif 'table lines' in issue: cats['Table'] += 1
            elif 'italic' in issue: cats['Italic (*text*)'] += 1
            elif 'nested bullet' in issue: cats['Nested bullets'] += 1
            elif 'content lines' in issue: cats['Entry too long'] += 1
    for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
        if n: print(f'  {n:4d}  {cat}')
    print()

    # Top offenders
    print(f'Top {worst_n} entries needing fixes (by severity score):')
    print()
    for r in broken[:worst_n]:
        print(f'  [{r["score"]:3d}]  {r["file"]}')
        for issue in r['issues']:
            print(f'          - {issue}')
        print()

    # CSV export
    if write_csv:
        out = os.path.join(REPO_ROOT, 'audit_results.csv')
        with open(out, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['score', 'file', 'issues', 'path'])
            for r in broken:
                w.writerow([r['score'], r['file'], ' | '.join(r['issues']), r['path']])
        print(f'Full results written to: {out}')
        print(f'({len(broken)} rows)')


if __name__ == '__main__':
    main()
