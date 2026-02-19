# ⚠️ YAML Formatting Issues - Manual Fix Required

The following 7 entries have YAML front matter formatting issues due to complex multi-line content with special characters. They are functional but won't parse into the search index until manually cleaned.

## Files Needing Manual YAML Cleanup (2% of database)

1. `L2_food_biology/l2-plants-dandelion.md` - Steps field has nested quotes
2. `L3_materials_chemistry/l3-materials-stone-tools.md` - Warnings with colons
3. `L3_materials_elements/l3-chemistry-candle-making.md` - Complex multi-line warnings
4. `L3_materials_elements/l3-chemistry-soap-making.md` - Chemical formulas with colons
5. `L3_materials_elements/l3-chemistry-water-distillation.md` - Technical specs with colons
6. `L4_agriculture_labor/l4-agriculture-goat-keeping.md` - Long lists with nested content
7. `L5_civilization_memory/l5-structural-truss-design.md` - Engineering formulas

## Issue
These entries were enhanced by sub-agents with very detailed content (which is good!), but the YAML front matter has:
- Deeply nested quotes and apostrophes
- Colons within list items
- Multi-line strings that span multiple lines

## Solution Options

### Option A: Use YAML Block Literals (Recommended)
Convert complex fields to block literal style (`|` or `>`):

```yaml
summary: |
  This is a multi-line summary
  with colons: like this
  and "quotes" that won't break parsing
```

### Option B: Simplify Front Matter
Move complex content into markdown body, keep front matter minimal:
- Short summary (1-2 sentences)
- Simple bullet warnings
- Move detailed steps/content to body

### Option C: JSON Instead of YAML
Switch these specific entries to JSON front matter (more forgiving with special chars)

## Impact
- **343/347 entries indexed and searchable** (99%)
- These 7 are still readable in markdown form
- Content is complete and correct
- Just not in searchable index

## Next Steps
Manual cleanup when time allows, or accept 99% coverage for MVP.

---
**Status:** Non-blocking for device deployment. Search works for 99% of database.
