# Button Guide
**ApocaPocket v2.0 — 5-Way Navigation Switch**

```
         [ UP ]
    [LEFT] [OK] [RIGHT]
        [ DOWN ]
```

One thumb. Five buttons. No dead ends.

---

## Universal Rules (Every Screen)

| Button | Action |
|--------|--------|
| **LEFT** (tap) | Go back one level |
| **LEFT** (hold 500ms) | Go home (main menu) |
| **UP + DOWN** (hold 400ms) | 🚨 Emergency — jumps straight to L1 Immediate Survival |
| **LEFT + RIGHT** (hold) | 🔖 Bookmarks — jumps directly to Bookmarks screen |

---

## Main Menu

Single-column fluid list: Emergency, categories, Search, History, Bookmarks.

| Button | Action |
|--------|--------|
| UP / DOWN | Move selection (wraps) |
| OK | Open selected item |
| — | No back (already home) |

---

## Browse Menu (Category → Subfolder → Entry Lists)

Two sequential menus: first subfolders, then entries within the chosen subfolder.

| Button | Action |
|--------|--------|
| UP / DOWN | Move selection |
| OK | Open selected item |
| LEFT | Back one level (subfolder list → home, entry list → subfolder list) |
| LEFT (hold) | Go home |

> Header shows `< Category Name   sel/total   87%` at all times.
> A scroll indicator appears on the right edge when the list overflows.
> Two-line item display: long titles wrap to a second line rather than clipping.

---

## Card Reader (Primary Entry View)

Entries are split into swipeable cards at every `##` heading. LEFT/RIGHT flip between them.

| Button | Action |
|--------|--------|
| RIGHT | Next card |
| LEFT | Previous card |
| LEFT (at card 1) | Back to entry list |
| LEFT (hold) | Go home |
| UP / DOWN | Scroll within card *(only on long cards)* |
| **OK (hold 500ms)** | Open **context menu** |

**Header:** `< Entry Title   2/5   87%`  
- `*` prefix on fraction = entry is bookmarked (e.g. `* 2/5`)
- Card title shown inside content area (bold, red accent bar for warnings)

---

## Context Menu (long-press OK in Card Reader or Scroll View)

| Option | Action |
|--------|--------|
| Add Bookmark / Remove Bookmark | Toggle bookmark for this entry |
| View Diagram | Display diagram fullscreen *(only if diagram exists)* |
| Entry Info | Show ID, line count, bookmark status |
| Close | Return to entry |

Navigate with UP/DOWN, select with OK, cancel with LEFT.

---

## Scroll View (History Resume / Fallback)

Used when resuming from History or when card parsing falls back.

| Button | Action |
|--------|--------|
| UP (tap) | Scroll up one line |
| DOWN (tap) | Scroll down one line |
| UP (hold) | Jump to **previous** `#` heading |
| DOWN (hold) | Jump to **next** `#` heading |
| RIGHT (tap) | Page down (~13 lines) |
| LEFT (tap) | Back to list |
| LEFT (hold) | Go home |
| **OK (hold 500ms)** | Context menu |

**Header:** `< Entry Title   1/4   87%` (page fraction based on scroll position)

---

## Search Screen (Alphabet Grid)

6-column grid of characters: `a–z`, `_` (space), `DEL`.

```
  a  b  c  d  e  f
  g  h  i  j  k  l
  m  n  o  p  q  r
  s  t  u  v  w  x
  y  z  _  DEL
```

| Button | Action |
|--------|--------|
| UP / DOWN | Move between rows |
| RIGHT | Move to next character (wraps row) |
| OK | Add selected character to query |
| BACK (tap) | Delete last character |
| BACK (tap, empty query) | Cancel / done |
| BACK (hold) | Go home |

Query displays with `_` cursor above the grid. Results shown after returning.

---

## Diagram Viewer

| Button | Action |
|--------|--------|
| LEFT | Return to entry |
| OK | Return to entry |

> Diagrams load from SD as 24-bit BMP files. Progress shown during load.
> Images streamed row-by-row — no full image held in RAM.
> See `docs/DIAGRAM_PREPARATION.md` for sizing guidance.

---

## Shortcut Summary Card

```
╔══════════════════════════════╗
║  ApocaPocket  Quick Guide    ║
╠══════════════════════════════╣
║  ANYWHERE:                   ║
║    LEFT        → Back        ║
║    HOLD LEFT   → Home        ║
║    UP+DN 0.4s  → EMERGENCY   ║
║    LT+RT hold  → Bookmarks   ║
╠══════════════════════════════╣
║  READING (CARDS):            ║
║    LEFT / RIGHT → Flip card  ║
║    UP / DN      → Scroll     ║
║    HOLD OK      → Options    ║
╠══════════════════════════════╣
║  LED STATUS:                 ║
║    Blue  → Booting           ║
║    Green → Ready             ║
║    Red   → Error             ║
╠══════════════════════════════╣
║  BATTERY:                    ║
║    ≤10%  → Warning shown     ║
║    30s dim · 5min sleep      ║
╚══════════════════════════════╝
```

---

## LED Status Reference

| Color | Meaning |
|-------|---------|
| 🔵 Blue (dim) | Booting — initializing hardware |
| 🟢 Green | Ready — firmware loaded, splash showing |
| 🔴 Red (continuous) | Fatal error — check serial monitor (115200) |
| 🔴 Red (2 blinks) | Index load error |
| 🔴 Red (5 blinks) | Index file not found |
| Off | Normal operation (turns off after splash) |

---

## Power Management

| State | Trigger | Backlight |
|-------|---------|-----------|
| Active | Any button pressed | Full (200/255) |
| Dim | 30 seconds no input | 40/255 (~20%) |
| Sleep | 5 minutes no input | Off |
| Wake | Any button press | Full (instantly) |

> Sleep mode: display off, RP2040 still running. Power draw ~15mA.
> Battery life: ~40-60 hours from 2000mAh at normal use.


```
         [ UP ]
    [LEFT] [OK] [RIGHT]
        [ DOWN ]
```

One thumb. Five buttons. No dead ends.

---

## Universal Rules (Every Screen)

| Button | Action |
|--------|--------|
| **LEFT** (tap) | Go back one level |
| **LEFT** (hold 500ms) | Go home (main menu) |
| **UP + DOWN** (hold 400ms) | 🚨 Emergency — jumps straight to L1 Immediate Survival |

---

## Main Menu

| Button | Action |
|--------|--------|
| UP / DOWN | Move selection |
| OK or RIGHT | Open selected option |
| — | No back (already home) |

**Menu options:**
- **Browse** — Category → Subfolder → Entry
- **Search** — Type keywords, pick from results
- **Bookmarks (N)** — Your saved entries
- **History (N)** — Recently read entries

---

## Browse Menu (Category / Subfolder / Entry Lists)

| Button | Action |
|--------|--------|
| UP | Move up the list |
| DOWN | Move down the list |
| OK | Open selected item |
| RIGHT | Open selected item (same as OK) |
| LEFT | Go back one level |
| LEFT (hold) | Go home |

> Lists auto-show count in title e.g. "Results (12)".
> A scroll indicator appears on the right edge when the list is longer than 9 items.

---

## Reading an Entry

| Button | Action |
|--------|--------|
| UP (tap) | Scroll up one line (animated) |
| DOWN (tap) | Scroll down one line (animated) |
| UP (hold) | Jump to **previous heading** (lines starting with `#`) |
| DOWN (hold) | Jump to **next heading** |
| RIGHT (tap) | Page down (10 lines) |
| LEFT (tap) | Back to entry list |
| LEFT (hold) | Go home |
| **OK (hold 500ms)** | Open **context menu** |

**Status bar (bottom):**
- Left: Battery percentage
- Right: `75%*` = scroll position 75%, `*` = bookmarked, `[D]` = diagram available

---

## Context Menu (long-press OK in Entry)

| Option | Action |
|--------|--------|
| Add Bookmark / Remove Bookmark | Toggle bookmark for this entry |
| View Diagram | Display diagram fullscreen *(only appears if diagram exists)* |
| Entry Info | Show ID, line count, bookmark status |
| Close | Return to entry text |

Navigate context menu with UP/DOWN, select with OK or RIGHT, cancel with LEFT.

---

## Diagram Viewer

| Button | Action |
|--------|--------|
| BACK (LEFT) | Return to entry text |
| OK | Return to entry text |

> Diagrams load from SD card as 24-bit BMP files. A progress bar shows during load.
> Images are centered horizontally. No zoom — see `docs/DIAGRAM_PREPARATION.md` for sizing.

---

## Search Screen (Character Wheel)

| Button | Action |
|--------|--------|
| UP | Cycle to next character |
| DOWN | Cycle to previous character |
| OK | Add current character to query |
| RIGHT | Delete last character (backspace) |
| LEFT | Done — run search (or cancel if empty) |

**Characters available:** `a-z`, space, `0-9`, `.`, `-`, `_`  
**Max query length:** 23 characters

---

## Shortcut Summary Card

```
╔══════════════════════════════╗
║  ApocaPocket  Quick Guide    ║
╠══════════════════════════════╣
║  ANYWHERE:                   ║
║    LEFT      → Back          ║
║    HOLD LEFT → Home          ║
║    UP+DN 0.4s→ EMERGENCY     ║
╠══════════════════════════════╣
║  READING ENTRY:              ║
║    UP / DN   → Scroll line   ║
║    HOLD UP   → Prev heading  ║
║    HOLD DN   → Next heading  ║
║    RIGHT     → Page down     ║
║    HOLD OK   → Options menu  ║
╠══════════════════════════════╣
║  LED STATUS:                 ║
║    Blue  → Booting           ║
║    Green → Ready             ║
║    Red   → Error             ║
╠══════════════════════════════╣
║  BATTERY:                    ║
║    ≤10%  → Warning shown     ║
║    30min dim, 5min sleep     ║
╚══════════════════════════════╝
```

---

## LED Status Reference

| Color | Meaning |
|-------|---------|
| 🔵 Blue (dim) | Booting — initializing hardware |
| 🟢 Green | Ready — firmware loaded, splash showing |
| 🔴 Red (continuous) | Fatal error — check serial monitor (115200) |
| 🔴 Red (2 blinks) | Index load error |
| 🔴 Red (5 blinks) | Index file not found |
| Off | Normal operation (LED turns off after splash dismissed) |

---

## Power Management

| State | Trigger | Backlight |
|-------|---------|-----------|
| Active | Any button pressed | Full (200/255) |
| Dim | 30 seconds no input | 40/255 (~20%) |
| Sleep | 5 minutes no input | Off |
| Wake | Any button press | Full (instantly) |

> Sleep mode: display off, RP2040 still running (no deep sleep yet).
> Power draw in sleep: ~15mA (LED off, display off, MCU idle).
> Battery life: ~40-60 hours from 2000mAh at normal use.
