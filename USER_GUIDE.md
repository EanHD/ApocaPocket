# 📱 ApocaPocket User Guide

**Complete walkthrough with visual diagrams**

---

## 📋 Table of Contents

1. [Quick Reference](#quick-reference)
2. [Power On/Off](#power-onoff)
3. [Home Screen](#home-screen)
4. [Browsing Entries](#browsing-entries)
5. [Reading Content](#reading-content)
6. [Viewing Diagrams](#viewing-diagrams)
7. [Search Mode](#search-mode)
8. [Bookmarks](#bookmarks)
9. [Emergency Mode](#emergency-mode)
10. [Settings](#settings)
11. [Gestures & Shortcuts](#gestures--shortcuts)
12. [Tips & Tricks](#tips--tricks)

---

## ⚡ Quick Reference

### Button Layout
```
        ┌─────────────────┐
        │                 │
        │    🖥️ Display   │
        │    240 × 240    │
        │                 │
        └─────────────────┘
              ▲   UP
              │
    LEFT  ◄───●───► RIGHT
              │
              ▼  DOWN
           
           ● CENTER
         (SELECT)
```

### Essential Gestures
| Gesture | Action |
|---------|--------|
| `UP` / `DOWN` | Scroll, navigate lists |
| `LEFT` | Back, cancel |
| `RIGHT` / `SELECT` | Confirm, open |
| `Long-press LEFT` (1s) | Jump to home screen |
| `Long-press SELECT` (1s) | Bookmark current entry |
| `Double-tap SELECT` | View diagram (if available) |
| `Triple-tap SELECT` | Search mode |
| `UP + DOWN` together | Emergency medical index |
| `LEFT + RIGHT` together | Bookmarks |
| `Long-press SELECT` (3s) | Power menu / settings |

---

## 🔌 Power On/Off

### Startup Sequence
```
Step 1: Press & hold RIGHT button (1 second)

┌─────────────────────────┐
│                         │
│                         │
│     APOCAPOCKET         │
│     ═══════════         │
│                         │
│     Loading...          │
│                         │
│                         │
│                         │
└─────────────────────────┘

Step 2: Boot completes (2 seconds)

┌─────────────────────────┐
│ 🔋85% 🌡️-2°C 💧45% 08:42│ ← Status bar appears
├─────────────────────────┤
│                         │
│  READY                  │
│                         │
│  347 entries loaded     │
│  31 diagrams available  │
│                         │
│  Press any button...    │
│                         │
├─────────────────────────┤
│                         │
└─────────────────────────┘
```

### Shutdown
```
From home screen: Long-press SELECT (3 seconds)
→ Settings menu appears
→ Navigate to "POWER OFF"
→ Press SELECT

┌─────────────────────────┐
│ ⚠️  Power Off?          │
├─────────────────────────┤
│                         │
│  Shutting down safely   │
│  preserves bookmarks    │
│  and settings.          │
│                         │
│  Continue?              │
│                         │
│  → YES                  │
│    NO                   │
│                         │
├─────────────────────────┤
│ ◀ Cancel    SELECT: OK  │
└─────────────────────────┘
```

---

## 🏠 Home Screen

**Default view after boot:**

```
┌─────────────────────────┐
│ 🔋85% 🌡️-2°C 💧45% 08:42│ ← Status bar
├─────────────────────────┤  ├─ Battery %
│ ApocaPocket             │  ├─ Temperature (if BME280)
│ 347 Survival Entries    │  ├─ Humidity (if BME280)
│                         │  └─ Time (if RTC)
│ [L1] 🚑 Medical (91)    │
│                         │
│ → Immediate Survival    │ ← Current selection (cyan)
│   Fire & Warmth (12)    │
│   Water (8)             │
│   Shelter (10)          │
│   Navigation (6)        │
│   Crisis Management(14) │
│                         │
│ [L2] 🍄 Food (100)      │
│ [L3] 🔨 Materials (46)  │
│                         │
├─────────────────────────┤
│ 🔍 Search  📖 Bookmarks │ ← Footer actions
└─────────────────────────┘

Actions:
  UP/DOWN   → Move selection
  RIGHT     → Expand category
  SELECT    → Enter subcategory
  Triple-●  → Search
  L+R       → Bookmarks
  U+D       → Emergency
```

### Category Structure
```
HOME
 │
 ├─ [L1] Immediate Survival (91)
 │   ├─ Medical First Aid (28)
 │   ├─ Fire & Warmth (12)
 │   ├─ Water (8)
 │   ├─ Shelter (10)
 │   ├─ Navigation (6)
 │   ├─ Crisis Management (14)
 │   └─ Strategic Planning (13)
 │
 ├─ [L2] Food & Biology (100)
 │   ├─ Plants - Edible (24)
 │   ├─ Plants - Regional (14)
 │   ├─ Plants - Poisonous (3)
 │   ├─ Mushrooms (5)
 │   ├─ Fish & Seafood (8)
 │   ├─ Animals & Hunting (12)
 │   ├─ Food Preservation (8)
 │   └─ Nutrition (6)
 │
 ├─ [L3] Materials & Chemistry (46)
 │   ├─ Stone & Clay (8)
 │   ├─ Metals (6)
 │   ├─ Chemistry (10)
 │   └─ Crafting (12)
 │
 ├─ [L4] Agriculture & Tools (50)
 │   ├─ Crops (12)
 │   ├─ Animals (8)
 │   ├─ Tools (15)
 │   └─ Construction (15)
 │
 └─ [L5] Civilization (60)
     ├─ Governance (8)
     ├─ Education (6)
     ├─ Engineering (18)
     └─ Advanced Tech (18)
```

---

## 📋 Browsing Entries

### Entry List View
```
After selecting a category:

┌─────────────────────────┐
│ ◀ Fire & Warmth    (12) │ ← Back button + count
├─────────────────────────┤
│                         │
│ → Ferro Rod Technique   │ ← Selected (cyan)
│   Bow Drill Method      │
│   Hand Drill Method     │
│   Flint & Steel         │
│   Tinder Identification │
│   Fire in Wet Weather   │
│   Wood Selection        │
│   Signal Fires          │
│   Cooking Methods       │
│   Safety & Ventilation  │
│                         │
│ ↓ More (2)              │ ← Scroll indicator
├─────────────────────────┤
│ 📖 Bookmark  ? Preview  │
└─────────────────────────┘

Actions:
  UP/DOWN       → Scroll list
  SELECT        → Open entry
  LEFT          → Back to categories
  Long-press →  → Quick peek (first 3 lines)
  Double-●      → Add to bookmarks
```

### Quick Peek
```
Long-press RIGHT on any entry:

┌─────────────────────────┐
│ Ferro Rod Technique     │
├─────────────────────────┤
│ 📝 Preview:             │
│                         │
│ Ferrocerium rods spark  │
│ at 3000°C (5400°F).     │
│ Works when wet. Lasts   │
│ 3000+ strikes.          │
│                         │
│ [Full entry available]  │
│                         │
│ Release to close        │
│ Press SELECT to open    │
└─────────────────────────┘
```

---

## 📖 Reading Content

### Reading Mode
```
┌─────────────────────────┐
│ ◀ Ferro Rod       📖 ▼  │ ← Back, bookmark status, menu
├─────────────────────────┤
│                         │
│ ## Overview             │ ← Markdown headers (bold)
│ Ferrocerium rods create │
│ sparks at 3000°C by     │
│ friction. Works wet/dry.│
│                         │
│ ## Technique            │
│ 1. Hold rod stable      │ ← Numbered steps
│ 2. Position striker at  │
│    45° angle            │
│ 3. Fast, firm scrape    │
│    toward tinder bundle │
│                         │
│ ⚠️ SAFETY:              │ ← Red warnings
│ Keep face and hands     │
│ clear of spark path.    │
│                         │
├─────────────────────────┤
│ ↓ Page 1/3  [IMG] [?]   │ ← Scroll progress, actions
└─────────────────────────┘

Actions:
  UP/DOWN       → Scroll content
  Hold UP/DOWN  → Fast scroll
  LEFT          → Back to list
  Double-●      → View diagram
  Long-●        → Bookmark
  SELECT + ▲▼   → Jump to next header
```

### Content Formatting
```
Markdown Rendering:

# Header 1          →  BOLD YELLOW 16px
## Header 2         →  BOLD WHITE 14px
### Header 3        →  BOLD WHITE 12px

**bold text**       →  WHITE BOLD
*italic text*       →  WHITE (no actual italic)
- List item         →  WHITE with • bullet
1. Numbered         →  WHITE with 1. 2. 3.

[link text]         →  CYAN underlined
→ Cross-reference   →  CYAN with arrow

⚠️ WARNING          →  RED BOLD
✓ Success           →  GREEN
✗ Failure           →  RED

Tables:
┌─────────┬─────────┐
│ Header  │ Header  │
├─────────┼─────────┤
│ Data    │ Data    │
└─────────┴─────────┘
```

### Measurements & Data
```
Example: CPR entry

┌─────────────────────────┐
│ ◀ CPR Basics      📖    │
├─────────────────────────┤
│                         │
│ ## Protocol             │
│                         │
│ ┌─ COMPRESSION ─────┐   │
│ │ Depth: 2-2.4"     │   │ ← Exact measurements
│ │        (5-6 cm)   │   │
│ │ Rate:  100-120/min│   │
│ │ Ratio: 30:2       │   │
│ └───────────────────┘   │
│                         │
│ ### Adult (>8 years)    │
│ • Two hands, center     │
│ • Full depth            │
│ • Allow recoil          │
│                         │
│ ### Child (1-8 years)   │
│ • One hand              │
│ • Depth: 2" (5 cm)      │
│ • Same rate             │
│                         │
│ ### Infant (<1 year)    │
│ • Two fingers           │
│ • Depth: 1.5" (4 cm)    │
│ • Center of chest       │
│                         │
├─────────────────────────┤
│ ↓ 2/5  [IMG] Related(3) │
└─────────────────────────┘
```

---

## 🖼️ Viewing Diagrams

### Diagram View
```
Double-tap SELECT while reading:

┌─────────────────────────┐
│ ◀ CPR Hand Position     │
├─────────────────────────┤
│                         │
│   ┌─────────────────┐   │
│   │                 │   │
│   │   [DIAGRAM]     │   │
│   │                 │   │
│   │  Two hands      │   │
│   │  interlocked    │   │
│   │                 │   │
│   │  Arrows show    │   │
│   │  2-2.4" depth   │   │
│   │                 │   │
│   │  Center chest   │   │
│   │  lower half of  │   │
│   │  sternum        │   │
│   │                 │   │
│   └─────────────────┘   │
│                         │
├─────────────────────────┤
│ ◀ Back to text     1/2  │ ← Multiple diagrams
└─────────────────────────┘

Actions:
  LEFT or SELECT → Back to text
  UP/DOWN        → Previous/next diagram
```

### Diagram Types
```
Medical Procedures:
┌────────────────────┐
│  High contrast     │
│  Clear labels      │
│  Measurement marks │
│  Step-by-step      │
│  Do's & Don'ts     │
└────────────────────┘

Plant/Food ID:
┌────────────────────┐
│  Side-by-side      │
│  RED = danger      │
│  CYAN = safe       │
│  Key features      │
│  labeled clearly   │
└────────────────────┘

Survival Techniques:
┌────────────────────┐
│  Tool positioning  │
│  Angles marked     │
│  Hand placement    │
│  Material labels   │
│  Safety zones      │
└────────────────────┘
```

---

## 🔍 Search Mode

### Character Picker
```
Triple-tap SELECT from anywhere:

┌─────────────────────────┐
│ 🔍 Search: _            │ ← Input field with cursor
├─────────────────────────┤
│                         │
│  → A  B  C  D  E  F  G  │ ← Character grid
│    H  I  J  K  L  M  N  │   Navigate with arrows
│    O  P  Q  R  S  T  U  │   SELECT to choose
│    V  W  X  Y  Z  0-9   │
│    [SPACE] [.] [-] [_]  │
│                         │
│  [← DELETE] [× CANCEL]  │
│                         │
├─────────────────────────┤
│ Type to search...       │
└─────────────────────────┘

After typing "CPR":

┌─────────────────────────┐
│ 🔍 Search: cpr_         │
├─────────────────────────┤
│  Character grid         │
│  (collapsed)            │
├─────────────────────────┤
│ Results (updating...):  │
│                         │
│ → CPR - Basics          │ ← Live results
│   Chest Seal (CPR ref)  │   appear as you type
│   Drowning (CPR steps)  │
│                         │
├─────────────────────────┤
│ 3 results   ↑ Edit  →OK │
└─────────────────────────┘

Actions:
  Arrows        → Navigate characters/results
  SELECT        → Choose character or open result
  DOWN from grid→ Jump to results
  UP from list  → Jump back to edit
  Delete key    → Backspace
  Cancel        → Close search
```

### Search Tips
```
FAST SEARCH TECHNIQUES:

1. Type partial words:
   "ble" → finds "bleeding", "edible"
   
2. Multiple keywords:
   "fire wet" → "fire in wet weather"
   
3. Numbers:
   "24" → "first 24 hours"
   
4. Abbreviations work:
   "cpr" → CPR entries
   "emg" → emergency entries
   
5. Fuzzy matching:
   "hypo" → "hypothermia"
   (1 character off still works)
```

---

## 📖 Bookmarks

### Access Bookmarks
```
Press LEFT + RIGHT together from anywhere:

┌─────────────────────────┐
│ 📖 Bookmarks (5/20)     │ ← Current / max
├─────────────────────────┤
│                         │
│ → CPR Basics            │ ← Most recently bookmarked
│   Severe Bleeding       │   appears at top
│   Water Boiling         │
│   Edible Plants Guide   │
│   Shelter Construction  │
│                         │
│   [Empty]               │
│   [Empty]               │
│                         │
├─────────────────────────┤
│ ◀ Close  Long-● Remove  │
└─────────────────────────┘

Actions:
  UP/DOWN    → Select bookmark
  SELECT     → Open entry instantly
  Long-●     → Remove this bookmark
  LEFT       → Close bookmarks
```

### Adding Bookmarks
```
While reading any entry:

Step 1: Long-press SELECT (1 second)

┌─────────────────────────┐
│ ◀ Ferro Rod       📖    │ ← Bookmark icon appears
├─────────────────────────┤
│                         │
│  ✓ Bookmarked!          │
│                         │
│  [entry content...]     │
│                         │
└─────────────────────────┘

Step 2: Icon stays filled in title bar

To remove: Long-press SELECT again
→ Icon becomes outline, bookmark removed
```

---

## 🚨 Emergency Mode

### Quick Access to Critical Info
```
Press UP + DOWN together from anywhere:

┌─────────────────────────┐
│ 🚨 EMERGENCY MEDICAL    │ ← Red banner
├─────────────────────────┤
│                         │
│ → CPR / No Breathing    │ ← Large text
│   Severe Bleeding       │   High contrast
│   Choking / Airway      │   No scrolling needed
│   Shock                 │   (all 6-8 visible)
│   Unconscious Person    │
│   Heat Stroke           │
│   Hypothermia           │
│   Fractures             │
│                         │
├─────────────────────────┤
│ SELECT to open   ◀ Exit │
└─────────────────────────┘

Design for stress:
  ✓ No categories to navigate
  ✓ Only most critical entries
  ✓ Sorted by frequency of need
  ✓ Large text, high contrast
  ✓ Instant access (2-3 seconds)

Actions:
  UP/DOWN  → Select entry
  SELECT   → Open immediately
  LEFT     → Exit emergency mode
  U+D again→ Also exits
```

---

## ⚙️ Settings

### Access Settings
```
Long-press SELECT (3 seconds) from home screen:

┌─────────────────────────┐
│ ⚙️ Settings             │
├─────────────────────────┤
│                         │
│ → Display               │
│   Power                 │
│   Storage               │
│   About                 │
│   Power Off             │
│                         │
└─────────────────────────┘

Press SELECT on "Display":

┌─────────────────────────┐
│ ◀ Display Settings      │
├─────────────────────────┤
│                         │
│ → Brightness: ████░░    │ ← 80%
│   Auto-dim: 30 sec      │   Use ◀▶ to adjust
│   Font size: Medium     │
│   Contrast: High        │
│                         │
│ ✓ Changes saved         │
│                         │
├─────────────────────────┤
│ ◀ Back                  │
└─────────────────────────┘

Press SELECT on "Power":

┌─────────────────────────┐
│ ◀ Power Settings        │
├─────────────────────────┤
│                         │
│ → Auto-dim: 30 sec      │
│   Auto-sleep: 5 min     │
│   Low power mode: OFF   │
│   Wake on button: ON    │
│                         │
│ ┌─ Battery ──────────┐  │
│ │ 🔋 85% (42 hrs)    │  │ ← Estimated runtime
│ │ State: Discharging │  │
│ │ Voltage: 3.87V     │  │
│ └────────────────────┘  │
│                         │
├─────────────────────────┤
│ ◀ Back                  │
└─────────────────────────┘

Press SELECT on "About":

┌─────────────────────────┐
│ ◀ About ApocaPocket     │
├─────────────────────────┤
│                         │
│ Version: 1.0            │
│ Build: 2026-02-19       │
│                         │
│ Database:               │
│ • 347 entries           │
│ • 343 indexed (99%)     │
│ • 31 diagrams           │
│                         │
│ Hardware:               │
│ • RP2040-Zero           │
│ • 240×240 display       │
│ • 8GB SD card           │
│ • BME280 sensor ✓       │ ← If present
│ • DS3231 RTC ✓          │
│                         │
│ Uptime: 2h 34m          │
│                         │
├─────────────────────────┤
│ ◀ Back                  │
└─────────────────────────┘
```

---

## 🎮 Gestures & Shortcuts

### Complete Gesture Reference

| Gesture | Context | Action | Time |
|---------|---------|--------|------|
| **Single Press** |
| `UP` | Any list | Scroll up, previous item | Instant |
| `DOWN` | Any list | Scroll down, next item | Instant |
| `LEFT` | Any screen | Back, cancel | Instant |
| `RIGHT` | Any list | Expand, forward | Instant |
| `SELECT` | Any item | Open, confirm, toggle | Instant |
| **Long Press (1s)** |
| `Long LEFT` | Anywhere | Jump to home screen | 1 sec |
| `Long RIGHT` | Entry list | Quick peek (first 3 lines) | 1 sec |
| `Long SELECT` | Reading | Bookmark toggle | 1 sec |
| `Long SELECT` (3s) | Home | Settings menu | 3 sec |
| **Double Tap** |
| `Double SELECT` | Reading | View diagram (if available) | <0.5s |
| `Double SELECT` | Entry list | Add to bookmarks | <0.5s |
| **Triple Tap** |
| `Triple SELECT` | Anywhere | Search mode | <1s |
| **Combos** |
| `UP + DOWN` | Anywhere | Emergency medical index | Hold both |
| `LEFT + RIGHT` | Anywhere | Bookmarks | Hold both |
| `SELECT + UP/DOWN` | Reading | Jump to next section header | Hold SELECT |

### Muscle Memory Shortcuts

**5 shortcuts to memorize:**
1. `Triple ●` = Search anything
2. `Long ◄` = Home screen
3. `▲ + ▼` = Emergency medical
4. `◄ + ►` = Bookmarks
5. `Long ●` = Bookmark this

**These 5 gestures make 90% of use cases instant.**

---

## 💡 Tips & Tricks

### Efficient Navigation

**📌 Bookmark your "kit"**
- Bookmark 5-10 entries you check often
- E.g.: CPR, water, fire, edible plants, shelter
- Access with `LEFT+RIGHT` in 2 seconds

**🔍 Search shortcuts**
- Type partial words: "ble" finds "bleeding"
- Use numbers: "24" finds "first 24 hours"
- Abbreviations work: "cpr", "emg"

**📖 Reading tips**
- Use `SELECT + UP/DOWN` to jump between sections
- Double-tap `●` to view diagram quickly
- Long-press `◄` to jump home without backing out

**🚨 Emergency mode is your panic button**
- `UP+DOWN` from anywhere = instant medical protocols
- Practice this gesture until it's muscle memory
- No menus, no navigation - just life-saving info

### Battery Optimization

**Extend battery life:**
1. Lower brightness (Settings → Display → 50%)
2. Reduce auto-dim time (15s instead of 30s)
3. Enable low power mode (Settings → Power)
4. Close diagrams when done (they use more power)
5. Let screen sleep when not actively reading

**40-60 hour runtime = weekend trip + safety buffer**

### Power Management States
```
┌──────────────────────────────────────┐
│           POWER STATES               │
└──────────────────────────────────────┘

ACTIVE (80-120mA)
├─ Display full brightness
├─ Actively scrolling/reading
└─ All sensors active
   │ Auto-dim after 30s ▼
   
IDLE (30-50mA)
├─ Display dimmed 50%
├─ No input detected
└─ Sensors active
   │ Auto-sleep after 5min ▼
   
SLEEP (5-10mA)
├─ Display off
├─ Only RTC + button detection
└─ Wake on any button press
   │ Power off after 24hr ▼
   
DEEP SLEEP (<1mA)
├─ Manual shutdown
├─ RTC keeps time
└─ Press POWER to boot
```

### Maintenance

**Keep your device healthy:**
- **Clean screen:** Soft cloth, no liquids
- **Charge regularly:** Don't let it hit 0%
- **Update database:** Swap SD card when new versions release
- **Backup bookmarks:** Copy `bookmarks.json` from SD card
- **Test emergency mode:** Practice `UP+DOWN` gesture monthly

### Customization

**SD card file structure:**
```
/SD_CARD/
├─ entries/           (347 markdown files)
├─ diagrams/          (31 PNG/SVG files)
├─ index.db           (search database)
├─ bookmarks.json     (your bookmarks)
├─ settings.json      (brightness, timing, etc.)
└─ custom/            (add your own notes here)
   └─ my-notes.md
```

**You can:**
- Add custom markdown files to `custom/`
- Edit entries directly on computer
- Rebuild index: Device auto-detects changes on boot

---

## 🆘 Troubleshooting

### Common Issues

**Screen won't turn on:**
1. Check battery (plug in charger)
2. Hold POWER (RIGHT) button for 3 seconds
3. If still dark, check connections

**Search not finding entries:**
1. Rebuild index: Settings → Storage → Rebuild Index
2. Check spelling (fuzzy match works for 1 char off)
3. Try partial words: "ble" instead of "bleeding"

**Diagram won't display:**
1. Check if entry has diagram (footer shows [IMG])
2. Verify diagrams/ folder on SD card not empty
3. Re-copy diagrams from GitHub if missing

**Bookmarks disappeared:**
1. Check `bookmarks.json` on SD card
2. Restore from backup if you made one
3. Sorry - bookmarks aren't synced to cloud (offline device)

**Battery draining fast:**
1. Lower brightness (Settings → Display)
2. Reduce auto-dim time (Settings → Power)
3. Close diagram view when done (uses more power)
4. Check for bad battery (voltage <3.2V when "full")

**Device freezing:**
1. Hold POWER button 10 seconds (force shutdown)
2. Wait 5 seconds, power back on
3. If persists, re-flash firmware from GitHub

---

## 📖 Appendix: Entry ID Reference

### Quick Entry ID List

**Most Frequently Accessed (Top 20):**
```
Emergency Medical:
• CPR / No Breathing
• Severe Bleeding / Tourniquet
• Choking / Airway Obstruction
• Shock Recognition
• Hypothermia Treatment
• Heat Stroke vs Exhaustion
• Fracture Stabilization
• Burns Assessment

Immediate Survival:
• Ferro Rod Fire Starting
• Water Boiling / Purification
• Tarp Shelter Configurations
• Edible Plant Identification
• Signal Fire Construction
• Compass-less Navigation

Food Safety:
• Poisonous Plant Lookalikes
• Mushroom Identification
• Fish Species ID
• Water Sources & Treatment
```

**Entry Naming Convention:**
```
Format: [layer]-[category]-[topic]-[detail].md

Examples:
l1-medical-cpr-basics.md
l1-fire-ferro-rod-technique.md
l2-plants-pnw-salal.md
l3-chemistry-soap-making.md
l4-agriculture-goat-keeping.md
l5-structural-truss-design.md
```

---

## 🌟 Final Thoughts

This device is simple by design. **5 buttons. No wifi. No apps. Just knowledge.**

When you need it, you pull it out, find what you need in seconds, and put it back.

**Practice the muscle memory:**
- `Triple ●` for search
- `▲ + ▼` for emergency
- `Long ●` to bookmark
- `◄ + ►` for quick access

**That's it. You're ready to survive.**

---

**Last Updated:** 2026-02-19  
**Version:** 1.0  
**Feedback:** Open an issue on GitHub or add to `custom/feedback.md` on SD card
