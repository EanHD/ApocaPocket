# ApocaPocket Database Audit & Visual Enhancement Plan
**Mission: Transform 347 text entries into an elegant, diagram-enhanced, perfectly navigable survival database**

---

## Project Scope

### Goals
1. **Audit all 347 entries** for completeness, clarity, and navigation flow
2. **Design optimal 5-button navigation schema** (Up/Down/Left/Right/Select + combos)
3. **Identify which entries need diagrams** (estimate: 150-200 entries)
4. **Generate consistent, minimal diagrams** using nano-banana-pro
5. **Integrate images** into firmware and entry display system
6. **Prepare for multi-lingual support** (future-proof structure)

### Visual Style Guide

**Diagram Aesthetic:**
- **Colors:** Maximum 2-3 colors per diagram
  - Primary: White/Light gray (#E0E0E0) for main elements
  - Accent 1: Cyan (#00CCFF) for highlights, arrows, important parts
  - Accent 2: Red (#FF3333) for warnings, critical points, danger zones
  - Background: Black (#000000) or dark gray (#1A1A1A) for OLED efficiency
- **Style:** Clean, minimal, technical illustration
- **Typography:** Sans-serif, legible at small sizes
- **Arrows:** Thick, clear directional indicators
- **Labels:** Numbered steps, brief text, high contrast
- **Resolution:** 240x240 pixels (fits 240×280 display with room for text)

**Diagram Types:**
1. **Anatomical** (medical procedures, body parts, pressure points)
2. **Process Flow** (step-by-step sequences, decision trees)
3. **Technique Diagrams** (knot tying, fire starting, shelter building)
4. **Plant/Animal ID** (visual identification, key features labeled)
5. **Safety Zones** (lightning positions, avalanche terrain, snake bite warnings)
6. **Tool/Equipment Diagrams** (construction, assembly, usage)
7. **Maps/Navigation** (star patterns, terrain reading, wayfinding)

---

## Navigation Schema Design

### Current Hierarchy
```
[HOME]
  ├─ Browse
  │   ├─ L1: Immediate Survival (77)
  │   │   ├─ Medical Emergencies (28)
  │   │   ├─ Water & Hydration (15)
  │   │   ├─ Fire & Warmth (13)
  │   │   ├─ Shelter (12)
  │   │   └─ Navigation (9)
  │   ├─ L2: Food & Biology (67)
  │   │   ├─ Plants (25)
  │   │   ├─ Animals (15)
  │   │   ├─ Mushrooms (12)
  │   │   ├─ Fishing (8)
  │   │   └─ Nutrition (7)
  │   ├─ L3: Materials & Chemistry (37)
  │   ├─ L4: Agriculture & Tools (36)
  │   └─ L5: Community Knowledge (60)
  ├─ Search
  ├─ Bookmarks
  └─ Emergency Quick Access
```

### Button Gesture System

**Single Press:**
- `UP` → Move cursor up / Scroll up
- `DOWN` → Move cursor down / Scroll down
- `LEFT` → Go back / Previous image
- `RIGHT` → Context action / Next image
- `SELECT` → Confirm / Enter / Toggle bookmark

**Long Press (1 second):**
- `UP` → Jump to top of list/page
- `DOWN` → Jump to bottom of list/page
- `LEFT` → Return to home screen
- `RIGHT` → Show related entries
- `SELECT` → Quick bookmark (with flash confirmation)

**Double Press (<0.5s between):**
- `UP+UP` → Previous category
- `DOWN+DOWN` → Next category
- `SELECT+SELECT` → Toggle image view (text → diagram → text)

**Combo Gestures:**
- `LEFT + SELECT` → Toggle info panel (battery, stats, current location)
- `RIGHT + SELECT` → Jump to related entry (if viewing entry with links)
- `UP + DOWN` (simultaneous) → Emergency mode (show critical L1 list)

**Image Navigation (when viewing diagram):**
- `LEFT/RIGHT` → Cycle through images in entry
- `UP/DOWN` → Zoom in/out (if supported)
- `SELECT` → Return to text

---

## Folder Structure

```
apocalypse-field-node/
├── assets/
│   ├── diagrams/           # All approved, production-ready diagrams
│   │   ├── L1/
│   │   │   ├── medical/
│   │   │   │   ├── cpr-sequence.png
│   │   │   │   ├── bleeding-pressure-points.png
│   │   │   │   ├── fracture-splinting.png
│   │   │   │   └── ...
│   │   │   ├── water/
│   │   │   ├── fire/
│   │   │   └── shelter/
│   │   ├── L2/
│   │   │   ├── plants/
│   │   │   ├── animals/
│   │   │   └── ...
│   │   ├── L3/
│   │   ├── L4/
│   │   └── L5/
│   ├── rejected/           # Failed/ugly diagrams for review
│   │   └── (same structure as diagrams/)
│   └── templates/          # Reference images, style guides
│       ├── arrow-style.png
│       ├── color-palette.png
│       └── diagram-grid.png
├── tools/
│   └── generate_diagrams.py   # Batch diagram generator
└── VISUAL_AUDIT_LOG.md         # Entry-by-entry audit log
```

---

## Audit Process

### Phase 1: Critical Medical Entries (Priority 1)
**Target: 28 L1 medical entries**

These are life-or-death situations where diagrams are ESSENTIAL:

1. **l1-medical-cpr-basics.md**
   - Diagram: Hand position, compression depth, head tilt
   - Type: Anatomical + Technique
   
2. **l1-medical-severe-bleeding.md**
   - Diagram: Pressure points, tourniquet placement, wound packing
   - Type: Anatomical + Technique
   
3. **l1-medical-hypothermia.md**
   - Diagram: Rewarming zones, safe positions
   - Type: Anatomical + Safety
   
4. **l1-medical-fracture-stabilization.md**
   - Diagram: Splinting techniques for different bones
   - Type: Technique (6-8 variations)
   
5. **l1-medical-choking-airway.md**
   - Diagram: Heimlich position, infant vs adult
   - Type: Anatomical + Technique
   
6. **l1-medical-snake-bites.md**
   - Diagram: DO NOT cut, DO NOT tourniquet, safe positioning
   - Type: Safety + Technique
   
7. **l1-medical-burns.md**
   - Diagram: Burn depth (1st/2nd/3rd degree), rule of nines
   - Type: Anatomical
   
8. **l1-medical-chest-seal.md**
   - Diagram: 3-sided seal technique, burping procedure
   - Type: Technique

... (continue for all 28 medical entries)

### Phase 2: Survival Skills (Priority 2)
**Target: 30-40 L1 fire/water/shelter entries**

Critical techniques that are hard to describe in text alone:

9. **l1-fire-bow-drill-detailed.md**
   - Diagram: Bow drill setup, hand position, spindle angle
   - Type: Technique + Tool diagram
   
10. **l1-fire-ferro-rod-technique.md**
    - Diagram: Grip, angle, spark direction
    - Type: Technique
    
11. **l1-shelter-tarp-configurations.md**
    - Diagram: 8-10 tarp shelter designs (A-frame, lean-to, etc.)
    - Type: Construction
    
12. **l1-water-solar-distillation.md**
    - Diagram: Still construction, condensation flow
    - Type: Process + Construction
    
13. **l1-knots-comprehensive.md**
    - Diagram: 10-15 critical knots step-by-step
    - Type: Technique (multi-step sequences)

### Phase 3: Plant & Animal ID (Priority 3)
**Target: 40-50 L2 identification entries**

Visual ID is CRITICAL to avoid poisoning:

14. **l2-plants-poisonous.md**
    - Diagram: Death camas vs edible camas, hemlock vs wild carrot
    - Type: Visual comparison (side-by-side)
    
15. **l2-plants-pnw-salal.md**
    - Diagram: Leaf shape, berry cluster, growth habit
    - Type: Plant ID
    
16. **l2-mushrooms-deadly-lookalikes.md**
    - Diagram: Death cap vs edibles, destroying angel comparison
    - Type: Visual comparison (WARNING HEAVY)

... (continue for all plant/mushroom/fish/game bird entries)

### Phase 4: Technical Skills (Priority 4)
**Target: 50-60 L3/L4 materials & tool entries**

Complex processes benefit from visual flow:

17. **l3-wood-bow-making.md**
    - Diagram: Wood selection, tillering, stringing
    - Type: Construction sequence
    
18. **l4-tool-pottery-basics.md**
    - Diagram: Coil method, pinch pot, firing setup
    - Type: Technique + Process
    
19. **l3-clay-identification.md**
    - Diagram: Clay testing (ribbon test, water drop test)
    - Type: Technique

### Phase 5: Community & Civilization (Priority 5)
**Target: 20-30 L5 entries that benefit from diagrams**

Abstract concepts made concrete:

20. **l5-nav-star-identification.md**
    - Diagram: Major constellations, North Star finding
    - Type: Map + Navigation
    
21. **l5-structural-truss-design.md**
    - Diagram: Load paths, truss types (king post, queen post, etc.)
    - Type: Engineering diagram

---

## Nano-Banana-Pro Prompt Template

### Base Prompt Structure
```
Technical survival diagram: [SPECIFIC SUBJECT]

Style: Clean minimal line art, 1-2 colors (cyan/white on black), technical illustration
Layout: [portrait/landscape/square]
Elements: [numbered steps/labeled parts/arrows showing direction]
Focus: Clarity and recognizability at small sizes (240px)
Avoid: Realistic shading, gradients, complex backgrounds

Specific requirements:
- [Detail 1]
- [Detail 2]
- [Detail 3]
```

### Example Prompts

**CPR Diagram:**
```
Technical survival diagram: CPR hand position and compression technique

Style: Clean minimal line art, cyan and white on black background, medical illustration
Layout: Portrait, 240x240px optimized
Elements: 
- Top view of torso showing hand placement
- Side view showing compression depth (2 inches / 5cm)
- Numbered steps (1, 2, 3)
- Arrows showing downward pressure direction
Focus: Hand position precision, compression depth measurement
Avoid: Realistic shading, facial details, complex anatomy

Specific requirements:
- Show both hands overlapped, fingers interlaced
- Clear sternum landmark
- Depth measurement with scale bar
- Bold arrows indicating force direction
- Large numbers for step sequence
```

**Bow Drill Diagram:**
```
Technical survival diagram: Bow drill fire starting technique

Style: Clean minimal line art, cyan and white on black background, technical illustration
Layout: Landscape, 240x240px optimized
Elements:
- Bow drill assembly (bow, spindle, bearing block, fireboard)
- Hand positions and posture
- Arrows showing motion direction
- Labels for key parts
Focus: Tool setup, proper form, motion direction
Avoid: Realistic wood texture, complex backgrounds, unnecessary detail

Specific requirements:
- Show spindle vertical, 90° angle
- Hand pressing down on bearing block
- Bow motion arrows (back and forth)
- Foot position on fireboard
- Ember catch location circled
```

**Poisonous Plant Comparison:**
```
Technical survival diagram: Death camas vs edible camas identification

Style: Clean minimal line art, RED for poison (death camas), CYAN for safe (edible camas), white labels on black background
Layout: Square, 240x240px optimized, split screen comparison
Elements:
- Side-by-side plant illustrations
- Key differences labeled with arrows
- WARNING symbol on poisonous side
- Safe symbol on edible side
Focus: Clear visual differences, easy field identification
Avoid: Realistic rendering, complex backgrounds, small text

Specific requirements:
- Death camas: cream/white flowers, narrow leaves, V-shaped seed pod
- Edible camas: blue/purple flowers, grass-like leaves, oval seed pod
- Large text: "POISONOUS" vs "EDIBLE"
- Arrows pointing to distinguishing features
- High contrast for field visibility
```

---

## Audit Log Template

For each entry, document:

```markdown
### [Entry ID] — [Title]

**Category:** L[X] / [Subtopic]
**Diagram Needed:** YES / NO / MAYBE
**Diagram Type:** [Anatomical/Process/Technique/ID/Safety/Tool/Map]
**Priority:** [1-5] (1=life-critical, 5=nice-to-have)
**Complexity:** [Simple/Medium/Complex] (affects generation time)

**Diagram Description:**
[What should the diagram show?]

**Key Elements:**
- Element 1
- Element 2
- Element 3

**Notes:**
[Any special considerations, warnings, multi-image needs]

**Status:** 
- [ ] Audited
- [ ] Diagram spec written
- [ ] Generated
- [ ] Approved
- [ ] Integrated

---
```

---

## Batch Generation Workflow

### Step 1: Audit Batch (10-20 entries)
- Read each entry
- Fill out audit log
- Write nano-banana prompts
- Prioritize generation order

### Step 2: Generate Diagrams
```bash
cd /home/eanhd/.openclaw/workspace-work/apocalypse-field-node

# Generate one diagram
uv run ~/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "$(cat prompts/l1-medical-cpr.txt)" \
  --filename "assets/diagrams/L1/medical/cpr-sequence.png" \
  --resolution 1K

# Batch generate (10 at a time)
bash tools/batch_generate_diagrams.sh prompts/batch_01.txt
```

### Step 3: User Review
- User reviews all generated images
- Moves failed/ugly ones to `assets/rejected/[category]/[filename]`
- Keeps good ones in `assets/diagrams/`

### Step 4: Regen Rejected
- I audit `assets/rejected/`
- Identify issues (wrong style, unclear, too complex, etc.)
- Revise prompts
- Regenerate
- Repeat until approved

### Step 5: Integration
- Update entry metadata to link diagrams:
  ```yaml
  diagrams:
    - path: assets/diagrams/L1/medical/cpr-sequence.png
      caption: "CPR hand position and compression depth"
      order: 1
  ```
- Update firmware to display images
- Export to RP2040 format (resize to 240x240, optimize)

---

## Estimation

### Diagram Count (Projected)
- L1 Medical: 28 entries → 28-35 diagrams (some multi-diagram)
- L1 Fire/Water/Shelter: 40 entries → 50-60 diagrams
- L2 Plants/Animals: 50 entries → 60-80 diagrams (ID critical)
- L2 Mushrooms: 12 entries → 15-20 diagrams (safety critical)
- L3 Materials: 20 entries → 25-30 diagrams
- L4 Tools: 25 entries → 30-40 diagrams
- L5 Navigation/Structure: 30 entries → 35-50 diagrams

**Total: 243-345 diagrams** (average 1.2 diagrams per entry that needs visuals)

### Time Estimation
- Audit 10 entries: 1 hour
- Write 10 prompts: 30 minutes
- Generate 10 diagrams: 30 minutes (API time)
- Review & revise: 30 minutes per batch

**Per batch (10 entries):** 2.5-3 hours
**Total project:** 87 hours (35 batches × 2.5 hours)

**Realistic timeline:** 3-4 weeks working 3-4 hours/day

---

## Success Metrics

### Quality Checks
- [ ] Diagram is recognizable at 240x240px
- [ ] Key elements are labeled clearly
- [ ] Colors follow style guide (max 2-3 colors)
- [ ] High contrast for field visibility
- [ ] Arrows/numbers guide the eye
- [ ] No unnecessary detail
- [ ] Matches entry content exactly
- [ ] Could save a life if used correctly

### Integration Checks
- [ ] Diagram linked in entry metadata
- [ ] Displays correctly on RP2040
- [ ] Navigation between text/image works
- [ ] File size optimized (<50KB per image)
- [ ] Loads in <500ms from SD card

---

## Multi-Lingual Preparation

### Structure for Future Translation
```
assets/
  ├── diagrams/
  │   ├── en/          # English (default)
  │   ├── es/          # Spanish
  │   ├── fr/          # French
  │   └── zh/          # Chinese
  └── ...
```

**Diagram Design for Translation:**
- Minimize text labels (use numbers + legend instead)
- Use universal symbols where possible
- Keep text in separate layer for easy replacement
- Generate base diagrams now, add translation layer later

**Entry Structure:**
```yaml
title: CPR Fundamentals
lang: en
translations:
  es: l1-medical-cpr-basics-es.md
  fr: l1-medical-cpr-basics-fr.md
diagrams:
  - path: assets/diagrams/en/L1/medical/cpr-sequence.png
    caption: "CPR hand position and compression depth"
    translations:
      es: assets/diagrams/es/L1/medical/cpr-sequence.png
      fr: assets/diagrams/fr/L1/medical/cpr-sequence.png
```

---

## Next Steps

### Immediate Actions (Tonight/Tomorrow)
1. ✅ Create folder structure (`assets/diagrams/`, `assets/rejected/`, `assets/templates/`)
2. ✅ Create `VISUAL_AUDIT_LOG.md` with template
3. ✅ Create `tools/batch_generate_diagrams.sh` script
4. ⬜ Start Priority 1 audit: 10 critical L1 medical entries
5. ⬜ Write 10 nano-banana prompts
6. ⬜ Generate pilot batch
7. ⬜ User reviews pilot batch
8. ⬜ Revise and establish final style guide

### Week 1 Goals
- Complete L1 Medical (28 entries, ~35 diagrams)
- Establish approved visual style
- Refine generation workflow
- Test integration on sample entries

### Week 2-3 Goals
- Complete L1 Survival (40 entries, ~60 diagrams)
- Complete L2 Plants & Animals (62 entries, ~100 diagrams)
- Begin L3 Materials

### Week 4 Goals
- Complete remaining L3/L4/L5 entries
- Final review and approval
- Integration testing
- Firmware update for image display

---

**This is the roadmap to transform ApocaPocket from a text database into a visual, elegant, life-saving tool.**
