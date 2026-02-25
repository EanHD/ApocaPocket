# ApocaPocket Content Standard
**Database writing guide for device-compatible markdown entries**

> This standard is derived from actual firmware constraints — not estimates.
> All numbers come directly from the compiled code.
>
> Before applying any rule here, ask: does this support the **North Star**?
> See [`docs/NORTH_STAR.md`](NORTH_STAR.md) for the full product vision.

---

## Why This Exists

The device is a field instrument. Content written for a web browser or PDF
does not translate. Tables render as raw pipe characters. Italic shows as
asterisks. A 900-line entry creates dozens of (cont.) cards that nobody
will navigate through under stress.

**Current database audit (484 entries):**
| Issue | Count | % |
|-------|-------|---|
| Contains tables | 110 | 22% |
| Section title > 22 chars (gets truncated) | 598 headings | — |
| Entry title > 25 chars (clipped in menus) | 232 | 47% |
| Over 200 lines (creates navigation fatigue) | 139 | 28% |
| Nested bullets (rendered flat) | 121 | 25% |
| Italic-only text (shows as asterisks) | 64 | 13% |

This standard fixes all of those.

---

## Device Reality

### Screen dimensions

```
┌────────────────────────────────────┐
│ < Title                  2/5  87% │  ← 28px header (not your content)
├────────────────────────────────────┤
│                                    │  ← 244px content area
│  [section title]                   │  ← 20px card header
│  ─────────────────────────────     │
│  13 lines of body text             │  ← 18px per line
│  max ~35–42 chars per line         │
│                                    │
└────────────────────────────────────┘
  240px wide · 280px tall · 16px safe margin both sides
```

### Hard limits (from compiled code)

| Constraint | Value | What happens if exceeded |
|-----------|-------|--------------------------|
| **Line wrap budget** | 214px (~35–42 chars depending on letters) | Auto word-wrapped — no data lost |
| **Lines per page (content)** | 13 | Scrollable if >11 lines on a card |
| **Card max lines (clean)** | 11 | Fits without scroll |
| **Card scroll max** | 13 | Scrollable, then splits into (cont.) |
| **Section title (##)** | ~22 chars bold | Truncated to "Title.." |
| **Entry title (#)** | ~25 chars | Truncated in menus |
| **Menu items visible** | 6 | Scrollable beyond that |

### What renders correctly

| Markdown | Renders as |
|----------|-----------|
| `# Entry Title` | Accent-colored bold heading |
| `## Section Name` | Card title (bold, accent bar left) |
| `### Sub-heading` | Dim regular-weight heading |
| `**bold**` | Bold inline text |
| `- bullet item` | Dot + indented text |
| `1. numbered step` | Number (dim) + indented text |
| `> blockquote` | Dim, indented — red if warning keyword |
| `---` | Thin horizontal divider line |
| blank line | Spacing between paragraphs |

### What does NOT render

| Markdown | What appears on device | Fix |
|----------|----------------------|-----|
| `\| table \| row \|` | Raw `\|` pipe characters | Convert to bullets or numbered list |
| `*italic*` | Raw asterisks | Remove or use `**bold**` instead |
| Nested bullets (`  - sub`) | Flat — indent ignored | Rewrite as flat list or numbered steps |
| `![image]()` | Nothing | Use a separate BMP diagram file |
| `[link](url)` | Raw link text and URL | Remove or paraphrase |
| HTML tags | Raw tag text | Never use HTML |
| YAML frontmatter | Stripped silently | Fine to keep, just ignored |

---

## Section Title Rules

Section titles become **card titles** — displayed in bold in the card header row.
They are the most space-constrained element on the device.

### Budget: ~22 characters in bold

```
✅ Good (fits clean)
## Signs & Symptoms       (18 chars)
## Protocol               (8 chars)
## Equipment Needed       (16 chars)
## Warning                (7 chars)

⚠️ Borderline (may truncate on some letters)
## Signs and Symptoms of Shock  → "Signs and Symptoms of.."
## Lifting & Transfer Methods   → "Lifting & Transfer Met.."

❌ Too long (will truncate)
## Body Mechanics (Prevent Injury)   → "Body Mechanics (Preve.."
## Stand-Pivot Transfer (Person Can Bear Some Weight)
```

**Rule:** Count characters. If over 22, shorten. Abbreviate where possible.

```
## Stand-Pivot Transfer      ✅ (not "Stand-Pivot Transfer (Person Can Bear Some Weight)")
## Pressure Sore Prevention  ✅ (not "Preventing Pressure Sores in Bedridden Patients")
## Non-Verbal Cues           ✅ (not "Reading Non-Verbal Communication Cues")
```

---

## Entry Title Rules

Entry titles appear in menus and the topStrip header. They are pixel-truncated
by the firmware, so longer titles become "Long Titl.." in navigation.

### Budget: ~25 characters

```
✅ Good
# Wound Closure Basics    (20 chars)
# CPR Protocol            (12 chars)
# Shelter: Snow & Ice     (18 chars)

⚠️ Will be truncated in menus
# Caregiver Support: Techniques & Sustainability  → "Caregiver Support: Te.."
# Chronic Conditions: Survival Management         → "Chronic Conditions: S.."
```

**Rule:** Entry titles should be short enough to be scannable in a 6-item list.
If the title needs a subtitle, that's a sign the content belongs in a `## Overview`
card, not the title itself.

---

## Entry Length Rules

### Target: 8–12 cards per entry (~80–130 lines of content)

Each `##` section becomes one card. Cards over 13 lines are scrollable.
Cards over 13 lines get split with "(cont.)" cards.

**Why this matters:**
- 8–12 cards = comfortable, purposeful navigation
- 20+ cards = navigation fatigue, user skips sections
- 1–2 cards = probably not enough information to justify the entry

### (cont.) cards are a signal, not a solution

If your entry generates "(cont.)" cards constantly, the sections are too long.
Break the section into two named `##` headings instead.

```
❌ One giant section
## Feeding Techniques
(40 lines — splits into "Feeding Techniques" + "Feeding Techniques (cont.)")

✅ Two purposeful cards
## Feeding: Positioning
## Feeding: Texture & Pace
```

---

## Formatting Rules

### Bullets

Use flat bullets only. No nested sub-bullets.

```
✅ Correct
- Bend knees, not back
- Keep load close to body
- Wide stance for stability

❌ Will render flat (no indentation)
- Safe Lifting Principles:
  - Bend knees, not back
  - Keep load close
```

If you need hierarchy, use a `###` sub-heading before the flat list.

### Numbered steps

Use for sequential procedures where order matters.

```
1. Position wheelchair at 45° angle
2. Lock wheels
3. Person scoots to edge of seat
```

Long step text wraps automatically and indents correctly. Keep each step to
one clear action.

### Bold

Use `**bold**` to highlight the most critical word or phrase in a line.
Use sparingly — if everything is bold, nothing is.

```
✅ **Do NOT** lay the patient flat.
✅ Rate: **100–120 compressions/min**
❌ **Safe Lifting Principles:** **Bend knees**, **not back**, **keep load close**
```

### Warnings

Trigger red text by using warning keywords in a blockquote:

```
> **Warning:** Do not attempt if you have back pain.
> **Caution:** Aspiration risk — stay upright after feeding.
> **Danger:** Stage 3+ pressure sores require evacuation.
```

Keywords that trigger red: `warning`, `danger`, `caution`, `critical`, `emergency`

The firmware also red-highlights any body line containing these keywords inline.

### Tables → convert to bullets or numbered lists

Tables are the #1 rendering problem. Every table shows as garbage on device.

```
❌ Table (renders as raw pipe characters)
| Level | Texture | Examples |
|-------|---------|----------|
| Soft  | Fork-mashable | Cooked vegetables |

✅ Bullet list
- **Soft:** Fork-mashable — cooked vegetables, ripe banana, scrambled eggs
- **Minced:** Small pieces with sauce — ground meat, mashed potato
- **Pureed:** Smooth — applesauce, pureed soup, mashed banana

✅ Numbered list (if order matters)
1. **Regular:** All normal foods
2. **Soft:** Fork-mashable — cooked vegetables, banana
3. **Pureed:** Smooth — applesauce, soup
```

---

## Entry Structure Template

```markdown
# Entry Title (max ~25 chars)

## Overview
2–4 sentence summary of the topic. Answer: what is this, why does it matter
in a survival context, and what is the one thing someone must remember.

## [Most Critical Section]
Lead with the most important information. Answer-first writing.
A panicked person reads the first card and acts. Make it count.

- Key point one
- Key point two
- Key point three

> **Warning:** Critical safety note goes here.

## [Step-by-Step Section]
1. First action
2. Second action
3. Third action

## [Reference Section]
- Spec: **Value** — explanation
- Spec: **Value** — explanation

## Signs to Evacuate
When this situation requires escalation or professional help.

> **Critical:** Evacuate immediately if [condition].
```

---

## What NOT to Use

| Don't use | Reason |
|-----------|--------|
| Tables | Renders as raw pipes — unusable |
| `*italic*` | No italic font loaded — shows as `*asterisks*` |
| Nested bullets (`  -`) | Indent ignored — renders flat |
| `# Heading` inside sections | Top-level headings are entry titles only |
| More than one `#` heading | Entry has exactly one title |
| More than ~12 `##` sections | Navigation fatigue |
| Cross-reference links | Render as raw markdown — not navigable |
| Footnotes | Not supported |
| Blockquotes for non-warnings | Reserve `>` for actual warnings/cautions |
| Long overview paragraphs | Break into bullets after the first 2–3 sentences |
| YAML frontmatter data users need | It's stripped — use `## Overview` instead |

---

## Quick Checklist (per entry)

Before adding or editing an entry, verify:

- [ ] Entry title `#` is ≤ 25 characters
- [ ] All section titles `##` are ≤ 22 characters
- [ ] No tables — converted to bullets or numbered lists
- [ ] No `*italic*` — use `**bold**` or plain text
- [ ] No nested bullets (`  -`) — use flat bullets or sub-headings
- [ ] Total line count is under ~150 (aim for 8–12 cards)
- [ ] Most critical information is in the first or second card
- [ ] Every `##` section has at least 4 meaningful lines
- [ ] Warning/danger notes use `> **Warning:**` format
- [ ] No cross-reference links (write the info directly or note "see: [entry title]")

---

## Phase 1 Triage Script

Run this to get a prioritized list of all entries that violate the standard.
Outputs a CSV sorted by severity score.

```python
#!/usr/bin/env python3
# tools/audit_content.py
# Usage: python tools/audit_content.py
# Output: audit_results.csv sorted by severity score

import glob, re, csv, os

SECTION_TITLE_MAX = 22
ENTRY_TITLE_MAX   = 25
LINE_MAX_CHARS    = 80   # soft warn — device wraps, but very long = hard to review
MAX_LINES         = 150

results = []

for path in sorted(glob.glob('data/entries/**/*.md', recursive=True)):
    fname = os.path.basename(path)
    with open(path) as f:
        lines = f.read().splitlines()

    issues = []
    score  = 0

    # Strip YAML frontmatter
    body_start = 0
    if lines and lines[0] == '---':
        for i, l in enumerate(lines[1:], 1):
            if l == '---':
                body_start = i + 1
                break

    body = lines[body_start:]

    # Entry title
    h1 = next((l[2:] for l in body if l.startswith('# ') and not l.startswith('## ')), '')
    if len(h1) > ENTRY_TITLE_MAX:
        issues.append(f'title too long ({len(h1)} chars): "{h1}"')
        score += 2

    # Section titles
    long_sections = [l[3:] for l in body if l.startswith('## ') and len(l[3:]) > SECTION_TITLE_MAX]
    if long_sections:
        for s in long_sections:
            issues.append(f'## too long ({len(s)}): "{s}"')
        score += len(long_sections) * 3  # highest weight — truncates on device

    # Tables
    table_lines = sum(1 for l in body if l.startswith('|'))
    if table_lines > 0:
        issues.append(f'has {table_lines} table lines (renders as garbage)')
        score += 5

    # Italic
    italic_lines = [l for l in body if re.search(r'(?<!\*)\*(?!\*)\w', l)]
    if italic_lines:
        issues.append(f'has {len(italic_lines)} italic lines (shows as asterisks)')
        score += 2

    # Nested bullets
    nested = [l for l in body if re.match(r'^  +- ', l)]
    if nested:
        issues.append(f'has {len(nested)} nested bullet lines (renders flat)')
        score += 1

    # Length
    content_lines = len([l for l in body if l.strip()])
    if content_lines > MAX_LINES:
        issues.append(f'entry too long ({content_lines} content lines, max {MAX_LINES})')
        score += 3

    if issues:
        results.append({
            'score':    score,
            'file':     fname,
            'path':     path,
            'issues':   ' | '.join(issues),
        })

results.sort(key=lambda r: -r['score'])

with open('audit_results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['score', 'file', 'issues', 'path'])
    w.writeheader()
    w.writerows(results)

print(f'Audited {len(list(glob.glob("data/entries/**/*.md", recursive=True)))} entries')
print(f'Found {len(results)} entries with issues')
print(f'Results written to audit_results.csv')
print()
print('Top 10 worst offenders:')
for r in results[:10]:
    print(f'  [{r["score"]:3d}] {r["file"]}')
    for issue in r["issues"].split(" | "):
        print(f'         - {issue}')
```

Run from repo root:
```bash
cd /path/to/field-node-firmware
python tools/audit_content.py
```

---

## Severity Score Guide

The triage script assigns a score to each entry. Higher = more broken on device.

| Score | Priority | Typical cause |
|-------|----------|---------------|
| 15+   | Fix immediately | Tables + long sections + oversized entry |
| 8–14  | Fix before release | Multiple long section titles or tables |
| 4–7   | Fix when possible | Long title + italic or nested bullets |
| 1–3   | Low priority | Minor formatting issues |

---

## The 10-Second Rule

Every entry should pass this test: **can someone find the critical action within 10 seconds?**

That means:
1. The entry title makes it clear what problem this solves
2. The first card (`## Overview` or equivalent) has the key answer
3. Section titles are scan-friendly — no jargon, no filler words
4. The most critical warning is visible without flipping more than 2 cards

If an entry fails the 10-second test, restructure it — don't just format it.
