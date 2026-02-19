#!/usr/bin/env python3
"""Fix YAML front matter by quoting strings that contain colons."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRY_ROOT = ROOT / "data" / "entries"

# Files that had errors
ERROR_FILES = [
    "L1_immediate_survival/l1-fire-tinder-identification.md",
    "L1_immediate_survival/l1-strategy-first-24-hours.md",
    "L2_food_biology/l2-plants-dandelion.md",
    "L3_materials_chemistry/l3-materials-stone-tools.md",
    "L3_materials_elements/l3-chemistry-candle-making.md",
    "L3_materials_elements/l3-chemistry-soap-making.md",
    "L3_materials_elements/l3-chemistry-water-distillation.md",
    "L4_agriculture_labor/l4-agriculture-goat-keeping.md",
    "L5_civilization_memory/l5-structural-truss-design.md",
]

def fix_yaml_front_matter(text: str) -> str:
    """Quote summary field if it contains colons."""
    if not text.startswith("---\n"):
        return text
    
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    
    front_matter = text[4:end]
    body = text[end + 5:]
    
    # Fix summary: line (quote if contains colon and not already quoted)
    front_matter = re.sub(
        r'^summary: (?!["\'])(.+:.+)$',
        r'summary: "\1"',
        front_matter,
        flags=re.MULTILINE
    )
    
    return f"---\n{front_matter}\n---\n{body}"

def main():
    fixed_count = 0
    for rel_path in ERROR_FILES:
        file_path = ENTRY_ROOT / rel_path
        if not file_path.exists():
            print(f"⚠️  Not found: {rel_path}")
            continue
        
        text = file_path.read_text(encoding="utf-8")
        fixed_text = fix_yaml_front_matter(text)
        
        if fixed_text != text:
            file_path.write_text(fixed_text, encoding="utf-8")
            fixed_count += 1
            print(f"✅ Fixed: {rel_path}")
        else:
            print(f"⏭️  Skipped (no change): {rel_path}")
    
    print(f"\n✅ Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
