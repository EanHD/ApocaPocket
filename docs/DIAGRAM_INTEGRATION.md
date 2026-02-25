# ApocaPocket — Diagram Integration Design

**Status:** Design brief for Copilot  
**Date:** 2026-02-24  
**Goal:** Make diagrams feel native, not bolted-on

---

## Current State (what's already built)

The diagram engine is **complete and working**:

- `diagram.cpp` — full BMP loader, row-by-row SD stream, RGB565 conversion, progress bar
- `hasDiagram(eid)` — checks if `/data/data/diagrams/{eid}.bmp` exists on SD
- `showDiagram(eid, title)` — renders full-screen, waits for OK/BK to exit
- **Already wired in both viewers** (card reader + scroll fallback)

**How it's accessed today:**  
OK long-press → context menu → "View Diagram" (only appears if diagram exists)

**The problem:**  
Nobody knows it's there. It's invisible until you accidentally long-press OK. Zero affordance. Zero discoverability.

---

## The Three Questions

### 1. WHERE does the diagram live in the UX?

**Decision: Diagram = a card, not a menu item.**

Insert a diagram card automatically as **card 0** (before text) for entries that have one. This makes the diagram the first thing you see — not a hidden feature.

Why card 0, not last card:
- High-value diagrams (CPR steps, tarp config, bow drill) are reference visuals — you want them first
- "See it, then read the detail" is the natural flow
- Last-card placement = still discoverable only by scrolling through everything

**Exception:** For entries where the diagram is supplementary context (timelines, anatomy charts), keep it as card 0 but let the user immediately RIGHT-swipe past it to the text. Fast path if they don't need it.

### 2. WHEN does it show?

**On open, automatically — no menu required.**

The diagram card renders like any other card. If the entry has a diagram, card 0 = diagram. RIGHT moves to card 1 (text). That's it.

Remove "View Diagram" from the context menu — it's redundant once the card exists.  
Keep "Entry Info" in the context menu (it already shows "Diagram: Yes/No" which is useful for debugging).

### 3. HOW is it indicated?

Two signals:

**A) Header indicator (top strip)**  
When on a diagram card, replace the card fraction (`1/4`) with `📷 1/4` or just use a different accent color for the card header bar (cyan instead of the usual color). Simple, no new UI components.

**B) Diagram badge on menu**  
In the entry list/menu, add a small `[D]` or `◈` suffix to entries that have a diagram. This signals before you even open the entry that there's a visual available. One character, right-aligned or after the title.

---

## Implementation Plan (Copilot tasks)

### Phase A — Card injection (core change, ~30 min)

In `cards.cpp` → `parseCards()`:
1. Accept a `bool hasDiag` parameter
2. If `hasDiag == true`, prepend a synthetic card at index 0:
   - `card.title = "Diagram"`
   - `card.lineStart = -1` (sentinel — not a text card)
   - `card.lineCount = 0`
   - `card.isDiagram = true` (new field on Card struct)

In `ui.cpp` → card reader render loop:
1. Check `if (cur.isDiagram)` → call `showDiagram()` inline instead of rendering text
2. On RIGHT from diagram card → go to card 1 (text starts) — already works via existing card nav
3. Remove diagram from context menu

**Card struct change needed:**
```cpp
struct Card {
    // existing fields...
    bool isDiagram;   // true = render via showDiagram(), not text
};
```

### Phase B — Menu badge (nice-to-have, ~15 min)

In `ui.cpp` → menu item rendering for the entry list:
1. After building the menu item string, check `hasDiagram(eid)`
2. If true, append ` ◈` to the display string (or `[D]` if special chars are risky)
3. Cap total display length to avoid overflow

### Phase C — Diagram card header (polish, ~10 min)

When rendering a diagram card in the card reader:
1. Top strip: show entry title + `Diagram` as the card section label
2. Accent bar color: use `COL_ACCENT` (cyan) instead of the default section color
3. This visually distinguishes diagram cards from text cards

---

## SD Card Path

Firmware expects: `/data/data/diagrams/{eid}.bmp`

The `eid` is the filename without extension (e.g., `l1-strategy-first-24-hours`).

Diagram files are in: `diagrams/bmp/` in the repo (79 BMPs, 200×200, 24-bit).

**To deploy:**
```bash
cp diagrams/bmp/*.bmp /YOUR/SD/CARD/data/data/diagrams/
```

Note: the path has `data/data/` — this is intentional (SD root `/data/` mirrors workspace `data/` structure).

---

## Entry ↔ Diagram Mapping

The filename convention is the key. Entry `l1-strategy-first-24-hours.md` → diagram `l1-strategy-first-24-hours.bmp`.

**Currently matched (diagram file exists AND entry exists):**
- `first-24hr-decision-tree` — maps to `l1-strategy-first-24-hours`  
  ⚠️ Name mismatch — needs rename or alias logic
- `emp-grid-down-timeline` — maps to `l5-crisis-emp-grid-down`  
  ⚠️ Name mismatch
- `start-triage-protocol` — maps to `l5-crisis-mass-casualty-triage`  
  ⚠️ Name mismatch
- Most medical diagrams (`cpr-technique`, `tourniquet-application`, etc.) — need matching entry files

**The naming problem:**  
Diagram filenames don't match entry EIDs. Two options:

**Option 1 (easy):** Rename BMPs to match EIDs exactly. One-time rename. Zero code change.  
**Option 2 (flexible):** Add `diagram:` frontmatter field to entries. Parse it in `hasDiagram()` — look up by frontmatter value, not just EID.

**Recommendation: Option 2.** Entries already have `diagram:` fields in their frontmatter — the parser just doesn't read them. Small sdcard.cpp change, much more flexible long-term.

---

## Frontmatter Parsing (Option 2 detail)

Currently `sdcard.cpp` skips all YAML frontmatter. Change:

```cpp
// In loadEntry() or a new hasDiagramFromFrontmatter():
// Parse "diagram:" line from frontmatter
// Store the value stripped of path prefix and .svg extension
// Pass to hasDiagram() / showDiagram() as override eid
```

This lets entries say `diagram: diagrams/cpr-technique.svg` and the firmware resolves it to `/data/data/diagrams/cpr-technique.bmp`.

---

## What NOT to do

- ❌ Don't put diagrams in a separate menu section — breaks the reading flow
- ❌ Don't require navigation to a "diagrams library" — diagrams are per-entry, not standalone
- ❌ Don't show diagram on every card — once per entry (card 0) is enough
- ❌ Don't auto-advance past the diagram — let the user control it
- ❌ Don't add a loading spinner animation — the progress bar in `showDiagram()` is already perfect

---

## Priority Order

1. **Option 2 frontmatter parsing** — makes existing `diagram:` fields work  
2. **Card injection (Phase A)** — diagrams as card 0, no menu hunting  
3. **Menu badge (Phase B)** — discoverability from the list  
4. **Header accent (Phase C)** — polish

Phase A + B together is ~45 min of Copilot work. This is the right scope for one focused session.

---

## Files to touch

| File | Change |
|---|---|
| `src/cards.h` | Add `isDiagram` bool to Card struct |
| `src/cards.cpp` | Accept `hasDiag` param, prepend diagram card |
| `src/sdcard.cpp` | Parse `diagram:` frontmatter field |
| `src/diagram.h` | Update `hasDiagram()` signature to accept override path |
| `src/diagram.cpp` | Support override path in `hasDiagram()` / `showDiagram()` |
| `src/ui.cpp` | Render diagram card inline; add menu badge; remove context menu item |
