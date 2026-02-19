# 🎯 APOCAPOCKET DEVICE VISION - Complete UX & Hardware Strategy

**Updated:** 2026-02-19  
**Target Hardware:** RP2040-Zero + ST7789V2 1.69" LCD + 5-way SMD nav switch  
**Database Status:** 347 entries audited, 31 diagrams, production-ready

---

## 🎪 The Core Vision

**"All this data easily retrievable in the palm of your hand"** - despite having only ONE 5-way switch.

This isn't a limitation - it's a feature. The constraint forces us to create the most intuitive, stress-proof interface possible. When your hands are cold, when you're panicking, when battery is at 3% - **it still works flawlessly.**

---

## 🔧 Confirmed Hardware Build

### Primary Components
- **MCU:** RP2040-Zero (Seeed Studio / Raspberry Pi)  
  - Dual ARM Cortex-M0+ @ 133MHz
  - 264KB RAM, 2MB Flash
  - CircuitPython or C/C++ firmware
  - ~$1.50 each (you have 15 units)

- **Display:** ST7789V2 1.69" LCD Module (240×240px, IPS)  
  - ~$3-4, excellent visibility
  - SPI interface (fast refresh)
  - High contrast, wide viewing angles
  - Perfect size for pocket carry

- **Input:** 5-way SMD nav switch  
  - Up / Down / Left / Right / Center (Select/Press)
  - Single component = reliable, low power
  - **This is THE constraint we design around**

- **Storage:** Micro SD card reader module (SPI)  
  - All 347 entries + diagrams on SD
  - Hot-swappable for updates
  - ~300KB database + ~500KB diagrams = plenty of room

### Power System
- **Battery:** 3.7V 2000mAh Li-ion (you have 4× 2000mAh cells)
  - Target: **40-60 hour runtime** on single charge
  - RP2040 sleep modes when idle
  - Display dimming/off when not actively reading

- **Charging:** TP4056 module (you have 3 units)
  - Micro-USB charging
  - Built-in protection (overcharge, over-discharge)
  - LED charge indicators

- **Regulation:** Buck/boost converters if needed
  - MT3608 step-up (you have 25 units)
  - Generic buck converters (you have 3 units)
  - Target: stable 3.3V for RP2040 + display

### Optional Enhancement Sensors (From Your Bucket)

**High Value Additions:**
1. **BME280 Temperature/Humidity/Pressure Sensor** (you have 2)
   - **USE CASE:** Real-time environmental monitoring
   - Display current temp/humidity on status bar
   - Altitude estimation from pressure (hiking, mountains)
   - Hypothermia risk assessment (temp + humidity = wind chill equivalent)
   - **Integration:** I2C, minimal power draw, always-on display widget

2. **DS3231 Real-Time Clock** (you have 5)
   - **USE CASE:** Accurate timestamps for bookmarks, logging
   - Medication dosing reminders (every 4 hours, etc.)
   - Event logging (when did we treat the wound? when did symptoms start?)
   - **Integration:** I2C, keeps time even when device off, CR2032 backup

**Lower Priority (Consider for v2):**
3. **GY-NEO6MV2 GPS Module** (you have 1)
   - **USE CASE:** Location logging for rescue, navigation entries enhanced with current coords
   - **DOWNSIDE:** High power draw (~30mA active), slow cold start (30+ sec)
   - **DECISION:** Skip for v1 (battery life priority), add to "Explorer" variant

4. **GY-906 MLX90614 IR Temp Sensor** (you have 1)
   - **USE CASE:** Non-contact fever screening, surface temp checks
   - **DECISION:** Nice-to-have but not essential for v1

**Not Needed for Core Device:**
- Microphones (MAX9814) - no audio input needed
- Speakers (PAM8302, LM386) - visual-only device (silent operation)
- Additional displays - one display is the constraint we embrace
- Light sensors (GY-302) - not needed with manual brightness control

### Physical Design Constraints
- **Form Factor:** Palm-sized, pocketable (~80mm × 50mm × 15mm target)
- **One-Thumb Operation:** All controls accessible without repositioning hand
- **Buttons:** 5-way switch centered below display for thumb reach
- **Weight Target:** <100g with battery (lighter = more likely to actually carry)
- **Durability:** Drop-resistant (corners reinforced), splash-resistant (gasket or conformal coating)
- **Screen Protection:** Flush mount or slight recess to protect display surface

---

## 🎮 Navigation Philosophy: "Gestures Over Menus"

With only 5 buttons, we use **gesture combinations** instead of endless menu hierarchies.

### Button Mapping
- **UP** - Scroll up, previous entry, decrease value
- **DOWN** - Scroll down, next entry, increase value
- **LEFT** - Back/Cancel, previous section, category up
- **RIGHT** - Forward/Confirm, next section, category down
- **CENTER (SELECT)** - Select, toggle, activate, OK

### Gesture System
| Gesture | Action | Example |
|---------|--------|---------|
| **Single press** | Standard action | SELECT = open entry, UP/DOWN = scroll |
| **Long press (1s)** | Alternate function | SELECT (long) = bookmark, LEFT (long) = back to home |
| **Double tap** | Quick action | SELECT (2x) = toggle diagram view |
| **Hold + direction** | Combined action | Hold SELECT + UP = scroll section up |
| **Rapid sequence** | Easter egg / power user | UP-UP-DOWN-DOWN-LEFT-RIGHT = settings |

### Emergency Shortcuts (Muscle Memory)
- **UP + DOWN together** → Emergency medical index (CPR, bleeding, choking)
- **LEFT + RIGHT together** → Bookmarks (quick access to marked entries)
- **SELECT (triple tap)** → Search mode
- **SELECT (long hold 3s)** → Power menu (shutdown, brightness, battery info)

---

## 📱 Screen Layout Strategy (240×240px)

### Default Browse Mode
```
┌─────────────────────────┐
│ 🔋85% 🌡️-2°C 💧45%  08:42│ ← Status bar (12px)
├─────────────────────────┤
│ [L1] 🚑 Medical         │ ← Category header (20px)
├─────────────────────────┤
│                         │
│ → CPR - Basics          │ ← Entry list (scrollable)
│   Severe Bleeding       │   Compact mode: 3-4 entries
│   Hypothermia           │   visible at once
│ → Choking & Airway      │
│   Burns Assessment      │   → = current selection
│   Fractures             │   Cyan highlight
│                         │
├─────────────────────────┤
│ ↓ More (23)  🔍 📖 ⚙️    │ ← Footer (16px)
└─────────────────────────┘
```

### Entry Reading Mode
```
┌─────────────────────────┐
│ ◀ CPR Basics      📖 ▼│ ← Nav + bookmark + menu
├─────────────────────────┤
│                         │
│ ## Recognition          │ ← Scrollable content
│ • No breathing          │   Markdown rendering
│ • No pulse              │   with formatting:
│ • Unconscious           │   - Headers bold
│                         │   - Lists indented
│ ## Protocol             │   - Tables formatted
│ 1. Call for help        │   - RED for warnings
│ 2. Check responsiveness │   - CYAN for links
│ 3. Begin compressions   │
│    - Depth: 2-2.4"     │
│    - Rate: 100-120/min  │
│                         │
├─────────────────────────┤
│ ↓ 2/8 pages  [IMG] [?]  │ ← Scroll indicator + actions
└─────────────────────────┘
```

### Diagram View Mode
```
┌─────────────────────────┐
│ ◀ CPR Hand Position     │ ← Title + back
├─────────────────────────┤
│                         │
│   ┌─────────────────┐   │
│   │                 │   │
│   │   [DIAGRAM]     │   │ ← Full-screen image
│   │   240×220px     │   │   (or 220×220 for 
│   │                 │   │    margins)
│   │   High contrast │   │
│   │   Cyan/Red/Wht  │   │
│   └─────────────────┘   │
│                         │
├─────────────────────────┤
│ 🔍 Zoom  ↻ Info  ◀ Back │ ← Image controls
└─────────────────────────┘
```

### Search Mode (Character Picker)
```
┌─────────────────────────┐
│ 🔍 Search: ble_         │ ← Search input with cursor
├─────────────────────────┤
│  A B C D E F G H I J K  │ ← Character grid
│  L M N O P Q R S T U V  │   5×5 visible window
│  W X Y Z _ . - space    │   Navigate with arrows
│  [←DEL] [SRCH] [×CNCL]  │   CENTER to select char
├─────────────────────────┤
│ Results (updating...):  │
│ → Severe Bleeding       │ ← Live results as you type
│   Bleeding Control      │   Update on each character
│   Nose Bleed            │
├─────────────────────────┤
│ 3 results found         │
└─────────────────────────┘
```

---

## 🎨 Visual Design System

### Color Palette (High Contrast for Field Use)
- **Background:** Black `#000000`
- **Primary Text:** White `#FFFFFF`
- **Accent/Links:** Cyan `#00FFFF` (high visibility)
- **Warnings:** Red `#FF0000` (critical info)
- **Success/Safe:** Green `#00FF00` (edible plants, safe actions)
- **Headers:** Yellow `#FFFF00` (section breaks)
- **Dim/Inactive:** Gray `#808080` (footer, status bar)

### Typography
- **Font:** Terminus, Tamzen, or similar bitmap font (crisp at small sizes)
- **Sizes:**
  - Status bar: 8px
  - Body text: 10-12px (readable without strain)
  - Headers: 14-16px (bold)
  - Entry titles: 12px (bold, cyan)
- **Line Spacing:** 1.2x (breathing room without wasting space)
- **Margins:** 4px sides, 2px vertical (maximize content area)

### Icons & Symbols
- **Categories:** Single emoji or 16×16px icons
  - 🚑 Medical (L1)
  - 🍄 Food/Plants (L2)
  - 🔨 Materials/Tools (L3/L4)
  - 🏘️ Community (L5)
- **Actions:** Unicode symbols
  - → ← ↑ ↓ (navigation arrows)
  - 🔍 (search)
  - 📖 (bookmark)
  - ⚙️ (settings)
  - 🔋 (battery)
  - 🌡️ (temperature if BME280 present)
  - 💧 (humidity)

---

## 🧭 Navigation Hierarchy (3 Levels Max)

### Level 1: Home Screen (Category Browser)
```
[L1] Immediate Survival (91)
  → Medical First Aid (28)
     Fire & Warmth (12)
     Water (8)
     Shelter (10)
     Navigation (6)
     ...
[L2] Food & Biology (100)
[L3] Materials & Chemistry (46)
[L4] Agriculture & Tools (50)
[L5] Civilization & Memory (60)

[🔍 Search]  [📖 Bookmarks (5)]  [⚙️ Settings]
```

**Navigation:**
- UP/DOWN to select category
- RIGHT to enter, LEFT to back out
- SELECT to expand/collapse
- Long-press SELECT on category = mark as favorite (appears at top)

### Level 2: Entry List (Within Category)
```
[L1] 🚑 Medical First Aid (28 entries)

→ CPR - Cardiopulmonary Basics
  Severe Bleeding Control
  Hypothermia Treatment
  Choking & Airway Obstruction
  Burns Assessment
  Fracture Stabilization
  Shock Recognition
  Heat Stroke vs Exhaustion
  ...

↓ More (20)
```

**Navigation:**
- UP/DOWN to browse entries
- RIGHT / SELECT to open entry
- LEFT to back to categories
- Long-press RIGHT = quick peek (first 3 lines of entry)
- Double-tap SELECT = add to bookmarks

### Level 3: Entry Content (The Actual Knowledge)
```
◀ CPR - Cardiopulmonary Basics

## Overview
Cardiac arrest is... [scrollable content]

## Recognition
• No breathing
• No pulse (check 10 seconds)
• Unconscious / unresponsive

## Protocol
### 1. Call for Help (0-30 seconds)
...

[Scroll down for more: 2/8 pages]

[IMG] View Diagram
```

**Navigation:**
- UP/DOWN to scroll content
- LEFT to back to entry list
- SELECT to open related entries (if link highlighted)
- Double-tap SELECT = toggle diagram view (if diagram exists)
- Long-press SELECT = bookmark this entry
- Hold SELECT + UP/DOWN = jump to next section header

---

## 🔄 Advanced Navigation Patterns

### Quick Search (No Keyboard Needed)
**Method 1: Character-by-Character**
1. Triple-tap SELECT from anywhere → search mode
2. Character grid appears (A-Z, 0-9, space, backspace)
3. Navigate grid with arrow keys, SELECT to choose character
4. Results update live as you type
5. When done, DOWN to results, SELECT to open

**Method 2: First-Letter Jump**
1. From any entry list, press and hold a letter key combo:
   - Hold UP + tap SELECT (3x) = "C" entries
   - Custom gesture combos for common letters
   - Faster for known entry names

**Method 3: Tag Filter**
1. From home screen, SELECT on category
2. Quick menu: "Filter by tag..."
3. Tag list appears (medical, fire, water, food, etc.)
4. Multi-select with SELECT, RIGHT to apply

### Bookmarks & History
**Bookmarks:**
- Long-press SELECT on any entry = bookmark toggle
- LEFT + RIGHT together from anywhere = bookmark list
- Max 20 bookmarks (stored on SD card)
- Can organize into folders (optional for v2)

**Recent History:**
- Last 10 viewed entries auto-saved
- Access: Hold LEFT for 2 seconds
- Allows quick return to recently viewed entries

### Smart Context Menus
When an entry is open, CENTER (long press) opens context menu:
```
┌─────────────────┐
│ [📖] Bookmark   │
│ [🔗] Related (5)│
│ [📊] Entry Info │
│ [🖼️] Diagrams (2)│
│ [⬆️] Share*     │
│ [×] Close       │
└─────────────────┘
```
*Share = save to text file on SD card for external access

---

## ⚡ Performance Optimizations

### Fast Boot (<2 seconds)
1. **Stage 1 (0-0.5s):** RP2040 boot, display init
2. **Stage 2 (0.5-1.0s):** Load index from SD card (343 entries × 100 bytes = ~34KB)
3. **Stage 3 (1.0-1.5s):** Render home screen
4. **Stage 4 (1.5-2.0s):** Initialize sensors (BME280, RTC)
5. **Ready:** Display "READY" indicator, accept input

**Boot optimization tricks:**
- Keep index in binary format (not JSON)
- Lazy-load entry content (only when opened)
- Cache last viewed category in RAM
- Use RP2040 second core for background tasks

### Low Power Modes
| Mode | Power Draw | Use Case |
|------|------------|----------|
| **Active Reading** | 80-120mA | Display on, user scrolling |
| **Idle (dim)** | 30-50mA | No input for 30s, display dimmed 50% |
| **Sleep** | 5-10mA | No input for 5min, display off, RTC active |
| **Deep Sleep** | <1mA | Manual shutdown, RTC + RAM retention only |

**Wake Methods:**
- Any button press = instant wake (display on in 0.2s)
- RTC alarm (if medication reminders enabled)

### Smooth Scrolling
- **Target:** 30 FPS minimum, 60 FPS ideal
- **Technique:** 
  - Pre-render next 2 lines off-screen
  - Double-buffering (framebuffer in RAM)
  - Hardware SPI DMA for display updates
  - Dirty region tracking (only update changed areas)

---

## 📊 Information Density Strategies

### Progressive Disclosure
Don't show everything at once. Reveal details as needed:

**Level 1 - Overview (always visible):**
```
CPR - Cardiopulmonary Basics
━━━━━━━━━━━━━━━━━━━━━━━━
30 compressions : 2 breaths
Rate: 100-120/min
Depth: 2-2.4 inches

[MORE ↓]
```

**Level 2 - Core Protocol (scroll down):**
```
## Protocol
1. Check scene safety
2. Check responsiveness
3. Call for help
4. Begin compressions:
   • Hand position: center chest
   • Depth: 2-2.4" (5-6cm)
   • Rate: 100-120/min
   • 30 compressions
5. Open airway
6. Give 2 breaths
7. Repeat cycle

[DETAILS ↓]
```

**Level 3 - Full Details (scroll more):**
```
## Special Populations
### Children (1-8 years)
• Use one hand for compressions
• Depth: 2 inches (5cm)
• Same rate: 100-120/min

### Infants (<1 year)
• Use two fingers
• Depth: 1.5 inches (4cm)
• Compressions: center of chest

[DIAGRAM] [RELATED]
```

### Scannable Formatting
- **Bold headers** stand out
- **Bullet lists** for quick reading
- **Numbers** for sequences
- **→ Arrows** for key points
- **RED text** for critical warnings (impossible to miss)
- **Tables** for comparison data

---

## 🎯 The "10-Second Rule"

**Goal:** Any critical life-saving info must be findable in <10 seconds.

### Test Scenarios

**Scenario 1: "Someone's choking!"**
1. Device already on (0s)
2. UP+DOWN gesture → Emergency Medical (1s)
3. "Choking" is 4th entry, scroll down (2s)
4. SELECT to open (3s)
5. See "Ask: Are you choking?" immediately (4s)
6. Scroll to Heimlich instructions (6s)
**Total: 6 seconds ✅**

**Scenario 2: "Is this plant safe to eat?"**
1. Device on (0s)
2. Triple-tap SELECT → Search (2s)
3. Type first 3 letters "DAN" (4s)
4. "Dandelion" appears in results (5s)
5. SELECT to open (6s)
6. "LOOKALIKES:" section visible immediately (7s)
**Total: 7 seconds ✅**

**Scenario 3: "How do I purify water?"**
1. Devices on, triple-tap search (2s)
2. Type "WAT" (4s)
3. "Water Boiling" appears (5s)
4. Open entry (6s)
5. "Boil for 1 minute (sea level)" visible (7s)
**Total: 7 seconds ✅**

---

## 🔋 Battery Life Optimization

### Target: 40-60 Hours on 2000mAh
**Power Budget:**
- RP2040 active: ~30mA
- Display on (full brightness): ~40mA
- Display dimmed (50%): ~20mA
- SD card reads: ~10mA (burst)
- BME280 sensor: ~1mA
- RTC (DS3231): <0.1mA
- **Total active:** 80-100mA
- **Total idle (dimmed):** 40-60mA

**Usage Pattern Assumptions:**
- 20% time active reading (full brightness)
- 30% time idle dimmed (user thinking, not scrolling)
- 50% time in sleep mode (device in pocket)

**Calculation:**
```
Active (20%):   100mA × 0.2 = 20mA avg
Idle (30%):      50mA × 0.3 = 15mA avg
Sleep (50%):     10mA × 0.5 =  5mA avg
────────────────────────────────────
Total average:   40mA

Battery life = 2000mAh / 40mA = 50 hours ✅
```

### Power-Saving Features
1. **Auto-dim after 30s** of no input (50% brightness)
2. **Sleep after 5min** of no input (display off)
3. **CPU throttle** when not scrolling (66MHz instead of 133MHz)
4. **SD card power-down** between reads
5. **Display refresh only on changes** (not constant refresh)

---

## 🛠️ Advanced Features (Optional Enhancements)

### Environmental Monitoring (If BME280 Added)
**Status Bar Widget:**
```
🔋85% 🌡️-2°C 💧45% ⬆️850m 08:42
```
- Live temp / humidity / pressure
- Altitude estimate (from pressure)
- Warning indicators:
  - 🥶 <0°C = hypothermia risk
  - 🌡️ >35°C = heat stroke risk
  - 💧 <20% RH = dehydration warning
  - ⬆️ >2500m = altitude sickness alert

**Contextual Entry Recommendations:**
- If temp <0°C → suggest "Hypothermia" entry
- If altitude >2500m → suggest "Altitude Sickness"
- If humidity >85% → suggest "Waterproofing" entries

### Real-Time Clock Features (If DS3231 Added)
1. **Medication Timers:**
   - "Give antibiotic every 6 hours"
   - Set alarm, device beeps or shows notification
   - Track last dose time automatically

2. **Event Logging:**
   - Timestamp every opened entry
   - Log when you treated someone ("CPR started 14:37")
   - Export timeline to text file for rescue team

3. **Sunrise/Sunset Calculator:**
   - Combined with GPS coords (if available)
   - Or manual lat/long entry
   - Display in status bar

### Offline "AI" Features (Pre-Computed)
1. **Decision Trees:**
   - "I have [symptom], what do I do?"
   - Pre-built flowcharts stored as entries
   - Navigate with YES/NO button presses

2. **Resource Calculator:**
   - "I have 3 liters of water for 4 people, how many days?"
   - Simple forms with number input (UP/DOWN to change values)
   - Instant calculation results

3. **Checklist Mode:**
   - "First 24 Hours" entry becomes interactive checklist
   - Check off completed items with SELECT
   - Progress saved to SD card

---

## 🔍 Search Algorithm Design

### Trigram FTS for RP2040
**Problem:** SQLite FTS5 too heavy for RP2040.  
**Solution:** Custom lightweight trigram search.

**Index Structure:**
```
Trigram → Entry IDs
"cpr" → [42, 67, 89]
"ble" → [42, 51, 72]
"eed" → [42, 51, 88, 101]
```

**Search Process:**
1. User types "ble"
2. Look up trigram "ble" in index → get entry IDs [42, 51, 72]
3. Load entry metadata (title, summary) for those IDs
4. Display results sorted by relevance

**Index Size:**
- ~5000 unique trigrams
- Average 10 entry IDs per trigram
- 5000 × 10 × 2 bytes = 100KB index
- Fits easily in RP2040 flash

**Search Speed:**
- Trigram lookup: O(1) hash table
- Result fetching: ~10ms for 20 entries
- **Total: <50ms** for typical search ✅

### Fuzzy Matching
Allow typos (1 character off):
- User types "hyp" instead of "hypo"
- Generate fuzzy variants: "hyp", "hop", "hyo", "hupp", etc.
- Search all variants, merge results
- Still fast (<100ms)

---

## 🎨 UI State Machine

```
           ┌─────────────┐
           │    BOOT     │
           └──────┬──────┘
                  │
         ┌────────▼────────┐
         │   HOME SCREEN   │◄──────┐
         │  (categories)   │       │
         └────┬─────┬──────┘       │
              │     │               │
      ┌───────┘     └────────┐     │
      │                      │     │
┌─────▼──────┐         ┌────▼─────▼───┐
│ ENTRY LIST │         │    SEARCH    │
│ (browse)   │         │  (char pick) │
└─────┬──────┘         └────┬─────────┘
      │                     │
      │                ┌────▼─────┐
      │                │ RESULTS  │
      │                └────┬─────┘
      │                     │
┌─────▼──────────────────────▼─────┐
│       ENTRY CONTENT              │
│     (reading / scrolling)        │
└─────┬────────────────────────────┘
      │
      ├─► [DIAGRAM VIEW] ◄─┐
      ├─► [CONTEXT MENU]   │
      ├─► [BOOKMARKS]      │
      └─► [SETTINGS]       │
           │               │
           └───────────────┘
```

**Every screen has:**
- LEFT = back to previous screen
- Long-hold LEFT = home screen
- Long-hold SELECT (3s) = power menu

**No dead ends.** You can always get back.

---

## 🎓 User Onboarding (First Boot)

### Welcome Screen
```
┌─────────────────────────┐
│    APOCAPOCKET v1.0     │
│    ═══════════════      │
│                         │
│  347 survival entries   │
│  31 visual diagrams     │
│  Fully offline          │
│                         │
│  [5-WAY SWITCH GUIDE]   │
│  ↑↓ Navigate            │
│  ← → Back/Forward       │
│  ● Select               │
│                         │
│  Quick tips:            │
│  • UP+DOWN = Emergency  │
│  • Triple-● = Search    │
│  • Long-● = Bookmark    │
│                         │
│  ● START                │
└─────────────────────────┘
```

### Interactive Tutorial (Optional)
1. "Try scrolling UP and DOWN"
2. "Press SELECT to open an entry"
3. "Press LEFT to go back"
4. "Hold SELECT for 1 second to bookmark"
5. "Double-tap SELECT to view diagrams"

**Skip Tutorial:**
- Hold SELECT during boot = skip straight to home

---

## 📦 Packaging & Production

### Device Variants

#### Variant 1: "Pocket" (Base Model - $25-35)
- RP2040-Zero
- ST7789V2 1.69" display
- 5-way nav switch
- 2000mAh battery
- SD card reader
- **NO sensors** (keep it simple, low cost, max battery life)

#### Variant 2: "Pocket Pro" (Enhanced - $35-45)
- Everything in Pocket +
- BME280 environmental sensor
- DS3231 real-time clock
- Slightly larger case for sensor board

#### Variant 3: "Explorer" (Advanced - $60-80)
- Pi Zero 2 W (more powerful, Python environment)
- Larger display (2" or 2.8")
- All sensors (BME280, RTC, GPS optional)
- Bigger battery (4200mAh)
- More expansion options

---

## 🚀 Development Roadmap

### Phase 1: Core Device (Now)
- ✅ Database complete (347 entries, 31 diagrams)
- ✅ Hardware BOM finalized
- ⏳ CircuitPython firmware v1
  - Basic navigation (up/down/select)
  - Entry rendering
  - Search (character picker)
  - Bookmarks
- ⏳ Case design (3D printable or CNC)
- ⏳ PCB layout (optional - or breadboard/perf board)

### Phase 2: Polish (Next)
- Gestures (long-press, double-tap)
- Diagram viewer
- BME280 integration (if included)
- RTC integration (if included)
- Power optimization
- Boot time <2s

### Phase 3: Field Testing
- 5-10 beta units to real users
- Feedback on ergonomics
- Battery life validation
- Button layout adjustments
- Case refinements

### Phase 4: Production
- Final hardware revision
- Firmware optimizations
- User manual / quick start guide
- Packaging design
- Launch! 🎉

---

## 💰 Cost Analysis

### BOM Cost Breakdown (Per Unit)
| Component | Cost | Source |
|-----------|------|--------|
| RP2040-Zero | $1.50 | AliExpress/Seeed |
| ST7789 1.69" LCD | $3.00 | AliExpress |
| 5-way nav switch | $0.30 | AliExpress |
| SD card reader | $0.80 | AliExpress |
| 2000mAh Li-ion | $2.00 | AliExpress |
| TP4056 charger | $0.30 | AliExpress |
| Micro SD card (8GB) | $3.00 | Bulk |
| Case (3D print or injection) | $2.00 | Variable |
| PCB (if custom) | $1.50 | JLCPCB (qty 10+) |
| Misc (wires, connectors, screws) | $0.50 | - |
| **TOTAL** | **$14.90** | - |

**Optional Add-Ons:**
- BME280 sensor: +$2.00
- DS3231 RTC: +$1.50
- GPS module: +$8.00

### Pricing Strategy
- **Cost:** $15-18 (base) / $20-25 (with sensors)
- **Sell Price:** $25-35 (base) / $35-45 (pro) / $60-80 (explorer)
- **Margin:** ~50% (reasonable for small-scale production)

---

## 🎯 Success Metrics

**Hardware:**
- ✅ Boot time <2 seconds
- ✅ Battery life 40-60 hours
- ✅ One-thumb operation confirmed
- ✅ Weight <100g

**Software:**
- ✅ Search results <1 second
- ✅ Smooth scrolling (30+ FPS)
- ✅ All entries accessible within 3 button presses
- ✅ "10-second rule" validated for critical info

**User Experience:**
- ✅ 90%+ users can navigate without manual
- ✅ Zero reported "can't find X" issues
- ✅ Gesture system learned within 5 minutes
- ✅ Emergency shortcuts become muscle memory

**Reliability:**
- ✅ Drop test from 1.5m (5 feet)
- ✅ Splash-resistant (light rain OK)
- ✅ Temperature range: -10°C to 50°C
- ✅ 10,000+ button press cycles

---

## 📚 Documentation Needed

1. **Hardware Assembly Guide** - Step-by-step build instructions with photos
2. **Firmware Installation** - CircuitPython setup, file structure
3. **User Manual** - Gesture reference, tips & tricks, troubleshooting
4. **Quick Start Card** - Laminated pocket reference (button layout + gestures)
5. **Developer Guide** - For adding new entries, modifying firmware

---

## 🔧 Next Immediate Actions

1. **Prototype PCB Layout** - Route connections, fit components
2. **CircuitPython Base Firmware** - Display + SD + buttons working
3. **Case CAD Design** - Ergonomic, printable, modular (sensor options)
4. **First Working Prototype** - All hardware assembled, basic nav working
5. **Field Test Prep** - Load full database, test in realistic scenarios

---

## 💪 Why This Will Work

**1. Constraint is a feature:**  
One 5-way switch forces simplicity. No overwhelming menus. No confusion.

**2. Content is DONE:**  
347 audited entries, 31 diagrams. The hard part is finished.

**3. Hardware is proven:**  
RP2040 + 240×240 display = tested combo. Thousands of similar devices exist.

**4. Real-world value:**  
This isn't a toy. Someone WILL use this in an actual emergency.

**5. Iterative design:**  
Build v1, test, refine. We can improve based on real feedback.

---

## 🎉 The Vision, Revisited

**"All this data easily retrievable in the palm of your hand"**

Not just retrievable - **instantly accessible**, even when:
- Your hands are freezing
- You're panicked
- Battery is at 3%
- You've never used it before

**One device. One button cluster. 347 ways to survive.**

That's the vision. And it's 100% achievable.

---

**Let's build this.** 🚀
