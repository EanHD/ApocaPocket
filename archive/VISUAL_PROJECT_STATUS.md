# Visual Enhancement Project - Ready to Start! 🎨

## What's Been Prepared

### 📋 Planning Documents
- ✅ **VISUAL_ENHANCEMENT_PLAN.md** - Complete roadmap (15KB)
  - Visual style guide
  - Navigation schema with button gestures
  - Folder structure
  - Audit process
  - Nano-banana prompt templates
  - Multi-lingual preparation
  - Timeline & estimation (3-4 weeks)

- ✅ **VISUAL_AUDIT_LOG.md** - Entry-by-entry tracking
  - First 10 critical L1 medical entries documented
  - 15-18 diagrams needed for this batch
  - Priority/complexity ratings
  - Detailed diagram specifications

### 🗂️ Folder Structure
```
assets/
├── diagrams/          # Approved production images
│   ├── L1/
│   │   ├── medical/
│   │   ├── water/
│   │   ├── fire/
│   │   ├── shelter/
│   │   └── navigation/
│   ├── L2/ ... L5/
├── rejected/          # Images for review/regeneration
└── templates/         # Style guides, reference images

prompts/
└── batch_01_medical.txt    # First 10 diagrams ready to generate
```

### 🔧 Tools Created
- ✅ **tools/batch_generate_diagrams.sh** - Automated batch generation
  - Parses prompt files
  - Calls nano-banana-pro for each diagram
  - Saves to correct folders
  - Progress reporting

### 🎯 First Batch Ready (Pilot)

**10 Critical L1 Medical Diagrams:**
1. CPR hand position (top view)
2. CPR compression depth (side view)
3. Bleeding pressure points (full body map)
4. Tourniquet placement
5. Hypothermia rewarming zones
6. Forearm fracture splinting
7. Heimlich maneuver (adult)
8. Snake bite dos/don'ts
9. Burn depth classification
10. Chest seal (3-sided)

**All prompts written** in `prompts/batch_01_medical.txt`

---

## Next Steps (Your Decision)

### Option 1: Generate Pilot Batch Now
```bash
cd /home/eanhd/.openclaw/workspace-work/apocalypse-field-node

# Generate all 10 diagrams
bash tools/batch_generate_diagrams.sh prompts/batch_01_medical.txt

# Takes ~10-15 minutes (API calls)
# Results saved to: assets/diagrams/L1/medical/
```

Then you:
1. Review all 10 images
2. Move any ugly/failed ones to `assets/rejected/L1/medical/`
3. Tell me which ones need regeneration
4. I revise prompts and regenerate

### Option 2: Generate One Test First
```bash
# Test single diagram generation
cd /home/eanhd/.openclaw/workspace-work/apocalypse-field-node

uv run ~/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Technical survival diagram: CPR hand position (top view)

Style: Clean minimal line art, cyan and white on black background, medical illustration
Layout: Square, 240x240px optimized
Elements: Top-down view of torso, two hands overlapped on sternum, fingers interlaced
Focus: Precise hand position, sternum landmark
Avoid: Realistic shading, complex anatomy

Specific: Show hands clearly, simple ribcage outline, high contrast cyan hands on black" \
  --filename "assets/diagrams/L1/medical/test-cpr.png" \
  --resolution 1K
```

This generates one image to verify style/quality before batching.

### Option 3: Adjust Style First
If you want different colors, style, or approach, we can:
- Modify the visual style guide
- Rewrite prompt templates
- Test 2-3 variations before committing

---

## Full Project Scope

### By The Numbers
- **347 entries** in database
- **~250 entries** need diagrams (estimated)
- **~300-350 total diagrams** (some entries need multiple)
- **10 entries audited** so far (first batch)
- **337 entries** remaining to audit

### Timeline Estimate
- **Batch 1 (tonight/tomorrow):** 10 diagrams, test workflow
- **Week 1:** Complete L1 Medical (28 entries, ~35 diagrams)
- **Week 2:** L1 Survival + L2 Plants/Animals (~160 diagrams)
- **Week 3:** L3/L4 Materials & Tools (~80 diagrams)
- **Week 4:** L5 + final review (~50 diagrams)

**Total: 3-4 weeks working 3-4 hours/day**

### What Makes This Awesome
1. **Consistent visual style** - All diagrams look like they belong together
2. **Field-optimized** - High contrast, readable at 240px, works in poor light
3. **Life-saving clarity** - Medical diagrams could literally save lives
4. **Easy navigation** - Visual + text reinforces learning
5. **Professional quality** - Looks like a real survival manual, not a text dump
6. **Multi-lingual ready** - Structure supports future translations

---

## What You Need to Do

1. **Decide on pilot batch:**
   - Generate all 10 now? (Option 1)
   - Generate 1 test first? (Option 2)
   - Adjust style first? (Option 3)

2. **Review workflow:**
   - When diagrams generate, review them
   - Move bad ones to `assets/rejected/`
   - Tell me what's wrong (too complex, wrong colors, unclear, etc.)
   - I'll regenerate with revised prompts

3. **Approve style:**
   - Once we nail the style with first batch, rest will be consistent
   - This is the foundation for 300+ more diagrams

---

## Questions to Consider

1. **Color preference:** Happy with cyan/white/red on black? Or want different accent color?
2. **Detail level:** Current prompts aim for "minimal clean" - want more or less detail?
3. **Text size:** Should labels be bigger/bolder for tiny screen?
4. **Icon style:** Medical diagrams use anatomical, want more icon-based/simplified?

---

## Ready When You Are! 🚀

Say the word and I'll:
- Generate the pilot batch
- Wait for your review
- Regenerate rejects
- Continue with next 10 entries
- Build momentum toward 347 fully visual entries

This is going to transform ApocaPocket from "good" to "holy shit this is professional." 💪
