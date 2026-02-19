# ApocaPocket UX Design Master Plan
**Creating a Modern, Sleek, Reliable Survival Reference Device**

---

## Design Philosophy

### Core Principles

1. **One-Thumb Operation** — You should be able to use this with gloves, in the dark, or with one hand injured
2. **Information Density** — Every pixel counts on a 1.69" screen (240×280)
3. **Stress-Safe Navigation** — If you're hypothermic or panicking, the UI should still work
4. **Zero Learning Curve** — Someone should be able to pick this up and use it immediately
5. **Instant Response** — Every action should feel responsive (<100ms feedback)
6. **Power Efficiency** — Every design choice should consider battery life

### Design Constraints

**Hardware:**
- Display: 240×280 pixels (1.69" diagonal) — 140 DPI
- Input: 5 buttons only (Up/Down/Left/Right/Select)
- Memory: 264KB RAM total (need to keep <200KB free for app)
- Storage: SD card (slow, minimize reads)
- Battery: 40-60 hours target runtime

**Content:**
- 347 entries (and growing)
- Multi-page entries with diagrams, tables, step-by-step instructions
- Need to support search, browse, bookmarks, quick access

---

## Visual Design System

### Color Palette

**Core Colors:**
```python
# Background & UI
BLACK       = 0x000000  # Background (saves power on IPS)
DARK_BG     = 0x0A0A0A  # Slightly lighter for panels
GRAY_DARK   = 0x333333  # Dividers
GRAY_MED    = 0x666666  # Secondary text
GRAY_LIGHT  = 0x999999  # Disabled state

# Primary Actions
GREEN       = 0x00FF88  # Primary action, success, L1
CYAN        = 0x00CCFF  # Secondary action, links, navigation
YELLOW      = 0xFFCC00  # Warning, selected state
WHITE       = 0xFFFFFF  # Primary text

# Semantic Colors
RED         = 0xFF3333  # Critical warnings, danger, medical emergency
ORANGE      = 0xFF8800  # Caution, moderate warning
BLUE        = 0x3366FF  # Information, water-related

# Category Colors (for visual scanning)
L1_COLOR    = 0xFF4444  # Immediate survival (red — urgent)
L2_COLOR    = 0x44FF44  # Food & biology (green — life)
L3_COLOR    = 0x8844FF  # Materials (purple — transformation)
L4_COLOR    = 0xFF8844  # Tools (orange — building)
L5_COLOR    = 0x4488FF  # Civilization (blue — knowledge)
```

### Typography

**Font System:**
```python
# Built-in terminalio.FONT (6×8 monospace)
SCALE_TITLE = 2    # 12×16 pixels per char → ~20 chars/line
SCALE_BODY  = 1    # 6×8 pixels per char → ~40 chars/line
SCALE_SMALL = 1    # For metadata, footnotes

# Line Heights
LINE_HEIGHT_TITLE = 20  # 16px + 4px spacing
LINE_HEIGHT_BODY  = 12  # 8px + 4px spacing
LINE_HEIGHT_DENSE = 10  # 8px + 2px (for lists)
```

**Max Characters Per Line:**
- Scale 2 (titles): **20 chars**
- Scale 1 (body): **38 chars** (with 4px margins)
- Compact mode: **40 chars** (no margins)

### Layout Grid

**Screen Zones:**
```
┌─────────────────────────┐ ← 0px
│  [STATUS BAR]           │ ← 0-16px (battery, icons)
├─────────────────────────┤ ← 16px
│                         │
│  [CONTENT AREA]         │ ← 16-256px (240px height)
│                         │
│                         │
├─────────────────────────┤ ← 256px
│  [NAV HINT]             │ ← 256-280px (24px for hints)
└─────────────────────────┘ ← 280px

Margins: 4px left/right (232px usable width)
```

**Content Zone Layouts:**

1. **List View** (menus, search results)
   - Item height: 18px
   - Max visible items: 13
   - Selection indicator: `>` prefix + color change
   - Scroll indicator: right edge bar

2. **Detail View** (entry content)
   - Title: 2 lines max @ scale 2
   - Body: ~22 lines @ scale 1
   - Automatic word wrap at 38 chars

3. **Input View** (search, filters)
   - Prompt: 1 line @ scale 1
   - Input field: 2 lines @ scale 2
   - Instructions: 1 line @ scale 1 at bottom

---

## Navigation Patterns

### Button Mapping Philosophy

**Consistent Across All Screens:**
```
UP     → Move cursor/selection up (or scroll up in content)
DOWN   → Move cursor/selection down (or scroll down in content)
SELECT → Confirm/Enter (or toggle bookmark in content view)
BACK   → Go back one level (or exit search input)
POWER  → Long press = sleep/wake, Short press = context action
```

**Advanced Patterns:**
- **Long Press UP** (1s) → Jump to top
- **Long Press DOWN** (1s) → Jump to bottom
- **Long Press SELECT** (1s) → Add to bookmarks (confirmation flash)
- **Long Press BACK** (1s) → Return to home screen
- **POWER Short** → Toggle info panel (battery, time, entry count)

### Screen Hierarchy

```
[SPLASH]
    ↓ any button
[HOME] ← Main hub, always return here
    ├→ Browse → Categories → Subtopics → Entries → Detail
    ├→ Search → Input → Results → Detail
    ├→ Bookmarks → Detail
    ├→ Quick Access (POWER menu) → Emergency protocols
    └→ Info → Stats, battery, about
```

### Home Screen Design

**Option 1: Classic Menu**
```
┌─────────────────────────┐
│ ⚡ 87%      [ 🔖 5 ]   │ ← Status bar
├─────────────────────────┤
│  APOCALYPSE FIELD NODE  │ ← Title (scale 1, centered)
│                         │
│  > Browse Knowledge     │ ← Selected (yellow)
│    Search Database      │
│    Bookmarks            │
│    Emergency Protocols  │ ← Quick access to L1 critical
│    Info & Settings      │
│                         │
│                         │
│ U/D Select  BACK Sleep  │ ← Nav hints
└─────────────────────────┘
```

**Option 2: Dashboard (more modern)**
```
┌─────────────────────────┐
│ ⚡ 87%  347 entries     │
├─────────────────────────┤
│                         │
│  ┌─────┐  ┌─────┐      │
│  │  !  │  │  ~  │      │ ← Category icons
│  │ L1  │  │ L2  │      │   (large, colorful)
│  └─────┘  └─────┘      │
│  ┌─────┐  ┌─────┐      │
│  │  #  │  │  *  │      │
│  │ L3  │  │ L4  │      │
│  └─────┘  └─────┘      │
│  ┌─────┐  ┌─────┐      │
│  │  =  │  │  🔍 │      │
│  │ L5  │  │ SRCH│      │
│  └─────┘  └─────┘      │
│                         │
│ U/D/L/R  SEL open       │
└─────────────────────────┘
```

**Recommendation:** Start with **Option 1** (simpler to implement, better for stress situations), evolve to **Option 2** if you want to sell it as more modern.

---

## Information Architecture

### How to Fit 347 Entries Efficiently

**Challenge:** With 5 categories, variable subtopics, and 347 entries, how do you make navigation not feel like a slog?

#### Three-Level Browse Strategy

**Level 1: Categories (5 items)**
```
Immediate Survival (77 entries)
Food & Biology (67 entries)
Materials & Chemistry (37 entries)
Agriculture & Tools (36 entries)
Community Knowledge (60 entries)
```

**Level 2: Subtopics (dynamic per category)**
```
Example: Immediate Survival → 
  Medical Emergencies (28)
  Water & Hydration (15)
  Fire & Warmth (13)
  Shelter & Protection (12)
  Navigation & Signaling (9)
```

**Level 3: Entries (scrollable list)**
```
Medical Emergencies → 
  > CPR Fundamentals
    Severe Bleeding Control
    Hypothermia Treatment
    Fracture Stabilization
    ...
    [scroll indicator: 5/28]
```

#### Smart Filtering & Search

**Search Optimization:**
1. **Trigram search** works but is slow on 347 entries
2. **Progressive disclosure:** Show results as you type (after 3 chars)
3. **Category filter in search:** Search within L1 only, or all

**Character Input Improvement:**
```
Current: Cycle through alphabet with UP/DOWN
Problem: Takes forever to type "water" (w=23 presses)

Better: T9-style predictive grouping
  Button 1 → abc
  Button 2 → def
  Button 3 → ghi
  Button 4 → jkl
  Button 5 → mno
  Button 6 → pqrs
  Button 7 → tuv
  Button 8 → wxyz
  Button 9 → space
  Button 0 → numbers

NO WAIT — We only have 5 buttons.

Alternative: Smart char groups
  Group 1: vowels (aeiou)
  Group 2: common (nrst)
  Group 3: frequent (ldhc)
  Group 4: less common (bgmpw)
  Group 5: rare (fjkvxyzq)

Navigate groups with LEFT/RIGHT
Cycle within group with UP/DOWN
SELECT to add char
```

**Or even better:** Quick search shortcuts
```
Instead of typing:
  Pre-defined common searches accessible via POWER menu
  - "water"
  - "fire"
  - "bleeding"
  - "shelter"
  - "snake bite"
  - "hypothermia"
  - "cpr"
```

---

## Entry Display Optimization

### Content Parsing & Display

**Entry Structure (from .txt files):**
```
TITLE: CPR Fundamentals
CAT: L1
SUB: medical_first_aid
TAGS: cpr,resuscitation,airway
---
[SUMMARY]
Core CPR sequence...

[STEPS]
1. Confirm scene safety
2. Check responsiveness
...

[WARNINGS]
! Do not delay
! Technique varies by age

[RELATED]
> l1-medical-severe-bleeding
> l1-medical-heat-stroke

[SOURCES]
@ red-cross-cpr-2020
```

**Display Strategy:**

1. **Smart Section Rendering**
   - Parse sections on-the-fly (don't load entire entry into RAM)
   - Render visible portion only
   - Cache last 3 entries for BACK navigation

2. **Visual Hierarchy**
   ```
   ┌─────────────────────────┐
   │ CPR Fundamentals    [BM]│ ← Title (green, scale 2) + bookmark status
   ├─────────────────────────┤
   │                         │
   │ SUMMARY                 │ ← Section header (yellow, scale 1)
   │ Core CPR sequence for   │
   │ lay responders. Check   │
   │ scene safety, call for  │
   │ help, then begin chest  │
   │ compressions.           │
   │                         │
   │ STEPS                   │ ← Section header
   │ 1. Confirm scene safety │ ← Numbered list
   │ 2. Check responsiveness │
   │ 3. Call emergency...    │
   │                         │
   │ ! Do not delay EMS call │ ← Warning (red)
   │                         │
   │ Related: Severe Bleed → │ ← Link (cyan)
   │                         │
   │ SEL:Bookmark  70% ↓     │ ← Nav hint + scroll %
   └─────────────────────────┘
   ```

3. **Auto-Scroll for Long Entries**
   - UP/DOWN scrolls 1 line at a time
   - Long-press UP/DOWN scrolls 5 lines (fast scroll)
   - SELECT when on a `> related-entry` link → jumps to that entry
   - BACK → returns to previous entry or category list

4. **Special Formatting**
   - **Tables:** Convert to simplified ASCII tables (RP2040 can't render complex layouts)
   - **Dosing tables:** Critical for medical entries
     ```
     IBUPROFEN DOSING (mg)
     Age    | Dose  | Freq
     -------|-------|------
     0-5mo  | 50mg  | 6-8h
     6-11mo | 50mg  | 6-8h
     1-3yr  | 100mg | 6-8h
     ```
   - **Lists:** Bullets (`•`), numbers (`1.`), or dashes (`-`)
   - **Warnings:** Always red, always prefixed with `!`

---

## Performance Optimizations

### Memory Management

**Current Problem:** 264KB RAM, CircuitPython uses ~100KB, leaves 164KB for app

**Strategies:**
1. **Lazy Load Everything**
   - Don't load search index until first search
   - Don't load entry content until viewing
   - Clear display group between screens (no caching)

2. **Aggressive Garbage Collection**
   ```python
   import gc
   gc.collect()  # Call before every major operation
   ```

3. **Streaming Entry Reader**
   - Read entries in 512-byte chunks
   - Render one page at a time
   - Don't load entire 5KB entry into memory

4. **Index Optimization**
   - Current: 117 bytes per entry × 347 = 40KB (acceptable)
   - Trigram index: ~66KB (load only when searching)
   - Total index RAM: 106KB (fits!)

### Display Performance

**Current Problem:** `displayio.Group` operations can be slow

**Optimizations:**
1. **Dirty Region Updates**
   - Don't clear entire screen for small changes
   - For scrolling, only redraw changed lines

2. **Pre-render Common Elements**
   - Status bar (battery, icons) as a static sprite
   - Category icons as bitmap sprites

3. **Limit Redraws**
   - Only redraw on button press (not polling loop)
   - 20Hz update rate maximum (50ms loop)

### SD Card Access

**Current Problem:** SD card reads are SLOW (~100ms per file open)

**Optimizations:**
1. **Read Sequentially**
   - Keep file handle open while scrolling entry
   - Close only when navigating away

2. **Pre-fetch Next Entry**
   - When viewing entry #5, pre-load entry #6 in background
   - Requires careful memory management

3. **Cache Recently Viewed**
   - Keep last 2-3 entries in a circular buffer
   - Speeds up BACK navigation

---

## Reliability & Edge Cases

### Power Management

**Battery States:**
```
100-50%: Green indicator, full brightness
49-30%:  Yellow indicator, normal brightness
29-15%:  Yellow indicator, warn every 10 min
14-5%:   Red indicator, dim screen, warn every 5 min
<5%:     Auto-save bookmarks, show shutdown warning
0%:      Safe shutdown (write marker to SD, close files)
```

**Power Saving Mode (optional):**
- Dim backlight to 30% after 60s idle
- Full shutdown after 10 min idle (wake on any button)
- Aggressive GC and sleep cycles

### Error Handling

**Graceful Degradation:**
1. **Corrupted SD card**
   - Show error: "SD CARD ERROR / Check card"
   - Boot into minimal mode: Show built-in help text
   - Allow USB connection to repair

2. **Missing index files**
   - Rebuild index on first boot (takes 30s)
   - Show progress bar

3. **Low memory**
   - Clear search index
   - Show warning: "Low memory, some features disabled"
   - Basic browse still works

4. **Button stuck**
   - Detect if button held >10s
   - Ignore that button, show "Button 3 stuck, disabled"

### Field Durability

**Software:**
- Auto-save bookmarks after every change
- Write marker file on clean shutdown
- Detect unclean shutdown → offer recovery mode

**Hardware Recommendations:**
- Conformal coating on PCB (moisture protection)
- Silicone gasket around display
- Button dust covers
- IP54 rating achievable with good case design

---

## Quick Access & Emergency Features

### POWER Button Menu

**Long-press POWER → Emergency Quick Menu:**
```
┌─────────────────────────┐
│  EMERGENCY PROTOCOLS    │
├─────────────────────────┤
│  > CPR                  │ ← Pre-selected shortcuts
│    Severe Bleeding      │   to critical L1 entries
│    Hypothermia          │
│    Snake Bite           │
│    Water Purification   │
│    Fire Starting        │
│    Shock Treatment      │
│                         │
│  SEL:Open  BACK:Cancel  │
└─────────────────────────┘
```

**Benefit:** In a panic, hold POWER → instant access to life-saving protocols

### First 24 Hours Mode

**Idea:** New users or high-stress situations → guided mode

```
┌─────────────────────────┐
│  FIRST 24 HOURS         │
├─────────────────────────┤
│ You're in a survival    │
│ situation. Let's focus  │
│ on immediate needs.     │
│                         │
│ ✓ Assess threats        │ ← Checklist mode
│ ✓ Find/purify water     │
│ ○ Build shelter         │ ← Current step
│ ○ Start fire            │
│ ○ Signal for help       │
│                         │
│ SEL:Next  BACK:Skip     │
└─────────────────────────┘
```

**Implementation:**
- Lives in `/sd/guides/first24.txt`
- Step-by-step wizard
- Links to relevant entries at each step

---

## Hardware Refinements

### Button Ergonomics

**Current Design:** 5 tactile buttons on front panel

**Improvement Ideas:**
1. **Raised Button Caps**
   - 3D print taller caps (3mm height)
   - Different shapes: UP/DOWN round, SELECT square, BACK/POWER textured

2. **Button Layout V2**
   ```
   Option A (D-pad style):
        [UP]
   [BACK][SELECT][POWER]
       [DOWN]

   Option B (Row layout):
   [UP] [DOWN] [SELECT] [BACK] [POWER]

   Option C (Cluster):
   [UP]    [SELECT]
   [DOWN]  [BACK]    [POWER]
   ```

   **Recommendation:** Option C (cluster) — Most ergonomic for one-thumb use

3. **Haptic Feedback (optional)**
   - Tiny vibration motor on each press
   - Confirms input without looking
   - Costs $0.50 + 1 GPIO

### Display Enhancements

**Current:** ST7789 1.69" IPS (240×280)

**Future-Proofing:**
1. **Brightness Control**
   - PWM backlight already implemented
   - Add auto-dim based on battery level
   - Manual brightness control in settings

2. **Display Timeout**
   - Dim after 30s idle
   - Sleep after 5 min idle
   - Wake on any button

3. **Alternative Displays**
   - For "Pro" version: 2.0" IPS (320×240) — more screen real estate
   - For "Ultra" version: ePaper (low power, readable in sunlight) — terrible UX but great battery

### Case Design

**Requirements:**
- Palm-sized (70×45×18mm)
- Lanyard hole
- USB-C port access
- microSD slot access (for updates)
- Button cutouts with dust seals

**Materials:**
- **Budget:** 3D printed PLA ($.50)
- **Mid-tier:** Injection molded ABS ($5 at scale)
- **Premium:** CNC aluminum + silicone gasket ($20)

**Features:**
- Belt clip (optional)
- Waterproof rating: IP54 minimum, IP67 aspirational
- Drop-resistant: 1.5m onto concrete

---

## Testing & Validation

### UX Testing Protocol

**Lab Testing:**
1. **Button Response Time**
   - Measure debounce delay
   - Target: <100ms from press to visual feedback

2. **Search Performance**
   - 347 entries, 3-char search
   - Target: <1 second to results

3. **Battery Drain**
   - Active use: 30mA (60+ hours on 2000mAh)
   - Idle (screen dim): 10mA (200 hours)
   - Sleep: <1mA (2000+ hours)

**Field Testing:**
1. **Cold Weather**
   - -10°C to -20°C operation
   - Button responsiveness with gloves
   - Battery performance in cold

2. **Hot Weather**
   - 40°C+ operation
   - Screen visibility in direct sunlight
   - Battery thermal management

3. **Wet Conditions**
   - Light rain exposure (IP54)
   - Humid environment (90%+ RH)
   - Drying time after exposure

4. **Stress Testing**
   - Can a hypothermic person use it?
   - Can someone in shock find "CPR" quickly?
   - Is it usable with one hand injured?

### Usability Metrics

**Success Criteria:**
- **Time to find entry:** <30 seconds (browse) or <20 seconds (search)
- **Learning curve:** <5 minutes to master navigation
- **Error rate:** <1% wrong button presses (good tactile feedback)
- **Stress usability:** 80% success rate for critical tasks under simulated stress

---

## Implementation Roadmap

### Phase 1: Core UX (MVP)
- [x] Basic menu navigation (done)
- [x] Entry display with scrolling (done)
- [x] Search with character input (done)
- [ ] Status bar with battery indicator
- [ ] Bookmarks persistence
- [ ] BACK button navigation stack

**Deliverable:** Usable device, not pretty but functional

### Phase 2: Polish & Reliability
- [ ] Improved color scheme (semantic colors)
- [ ] Section-aware entry rendering ([SUMMARY], [STEPS], [WARNINGS])
- [ ] Long-press button actions
- [ ] Power menu with emergency shortcuts
- [ ] Auto-save & recovery mode
- [ ] Performance profiling & optimization

**Deliverable:** Production-ready device

### Phase 3: Advanced Features
- [ ] Dashboard home screen (modern look)
- [ ] Smart search with category filtering
- [ ] "First 24 Hours" guided mode
- [ ] Haptic feedback (if hardware added)
- [ ] Settings screen (brightness, sleep timeout)
- [ ] Usage stats (most viewed entries, time spent)

**Deliverable:** Premium device with "wow" factor

### Phase 4: Hardware V2
- [ ] Custom PCB design (integrate RP2040 + display + buttons)
- [ ] Improved case with IP54 rating
- [ ] Optional sensors (BME280, GPS) for "Pro" model
- [ ] Injection-molded case tooling

**Deliverable:** Scalable product for manufacturing

---

## Summary: What Makes This UX Awesome?

1. **Instant On** — No boot wait, press button and you're reading
2. **One-Thumb** — Designed for worst-case scenarios (gloves, injury, panic)
3. **Beautiful** — Modern color scheme, clean typography, intuitive icons
4. **Fast** — Search in <1s, navigate in <5 button presses
5. **Smart** — Emergency shortcuts, related links, smart filtering
6. **Reliable** — Auto-save, recovery mode, graceful degradation
7. **Long Battery** — 40-60 hours of actual use
8. **Durable** — IP54 rating, drop-resistant, field-tested

### The "10-Second Rule"

**Can someone pick this up and find "How to purify water" in 10 seconds?**

**Path 1 (Browse):**
1. Press any button (wake from splash) — 1s
2. UP to "Browse Knowledge" → SELECT — 2s
3. SELECT on "Immediate Survival" — 1s
4. DOWN to "Water & Hydration" → SELECT — 2s
5. DOWN to "Water Purification" → SELECT — 2s
6. Reading entry — 2s

**Total: 10 seconds ✓**

**Path 2 (Search):**
1. Press any button (wake from splash) — 1s
2. DOWN to "Search" → SELECT — 2s
3. Type "water" (5 chars × 0.5s) — 2.5s
4. BACK to finish input — 1s
5. SELECT on "Water Purification" — 1.5s
6. Reading entry — 2s

**Total: 10 seconds ✓**

**Path 3 (Emergency):**
1. Long-press POWER → Emergency menu — 2s
2. DOWN to "Water Purification" → SELECT — 2s
3. Reading entry — 6s

**Total: 10 seconds ✓**

---

## Final Thoughts

This is a **survivor's tool**, not a phone. Every design decision should ask:

- **"Would this work if I'm hypothermic?"**
- **"Would this work if I'm wearing gloves?"**
- **"Would this work if my battery is at 5%?"**
- **"Would this work if I've never seen this device before?"**

If the answer is yes to all four, you've got great UX.

The magic is in the constraints — 5 buttons, 1.69" screen, 264KB RAM — these limitations force clarity, focus, and reliability. That's what makes it awesome.

---

**Built with care for people who might actually need this someday.**
