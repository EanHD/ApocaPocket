#!/usr/bin/env python3
"""Fix remaining YAML issues in enhanced entries."""
from pathlib import Path
import yaml

ROOT = Path(".")
ENTRY_ROOT = ROOT / "data" / "entries"

# Remaining problematic files
FILES_TO_FIX = [
    "L2_food_biology/l2-plants-dandelion.md",
    "L3_materials_chemistry/l3-materials-stone-tools.md",
    "L3_materials_elements/l3-chemistry-candle-making.md",
    "L3_materials_elements/l3-chemistry-soap-making.md",
    "L3_materials_elements/l3-chemistry-water-distillation.md",
    "L4_agriculture_labor/l4-agriculture-goat-keeping.md",
    "L5_civilization_memory/l5-structural-truss-design.md",
]

def extract_and_fix_front_matter(text: str) -> tuple[dict, str]:
    """Extract front matter and body, return parsed dict and body."""
    if not text.startswith("---\n"):
        return {}, text
    
    # Find closing ---
    end = text.find("\n---\n", 4)
    if end == -1:
        # Try finding ## header instead
        import re
        match = re.search(r'\n## ', text)
        if match:
            end = match.start()
        else:
            return {}, text
    
    fm_text = text[4:end]
    body = text[end + 5:] if end != text.find("\n---\n", 4) else text[text.find("\n## "):]
    
    # Try to parse as-is first
    try:
        meta = yaml.safe_load(fm_text)
        return meta, body.strip()
    except:
        # Parsing failed - this is expected, we'll rebuild it
        pass
    
    # Manual parsing - extract key-value pairs
    meta = {}
    current_key = None
    current_value = []
    
    for line in fm_text.split('\n'):
        if line and not line[0].isspace() and ': ' in line:
            # New key
            if current_key:
                meta[current_key] = current_value
            
            key, val = line.split(': ', 1)
            current_key = key.strip()
            current_value = [val] if val else []
        elif line.startswith('- ') and current_key:
            # List item
            current_value.append(line)
        elif line.strip() and current_key:
            # Continuation
            if current_value:
                current_value[-1] += ' ' + line.strip()
            else:
                current_value.append(line.strip())
    
    if current_key:
        meta[current_key] = current_value
    
    # Clean up values
    for key, val in meta.items():
        if isinstance(val, list):
            if len(val) == 1 and not val[0].startswith('- '):
                meta[key] = val[0].strip().strip('"').strip("'")
            else:
                # Clean list items
                cleaned = []
                for item in val:
                    item = item.strip()
                    if item.startswith('- '):
                        item = item[2:].strip()
                    # Remove quotes if fully quoted
                    if (item.startswith('"') and item.endswith('"')) or \
                       (item.startswith("'") and item.endswith("'")):
                        item = item[1:-1]
                    cleaned.append(item)
                meta[key] = cleaned
    
    return meta, body.strip()

def rebuild_front_matter(meta: dict) -> str:
    """Rebuild YAML front matter with proper escaping."""
    lines = []
    for key, val in meta.items():
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                # Properly escape strings with colons or quotes
                if isinstance(item, str) and (':' in item or '"' in item or "'" in item):
                    # Use block literal style for complex strings
                    item_clean = item.replace('\\', '\\\\').replace('"', '\\"')
                    lines.append(f'- "{item_clean}"')
                else:
                    lines.append(f"- {item}")
        else:
            # Single value
            if isinstance(val, str) and (':' in val or '\n' in val):
                val_clean = val.replace('\\', '\\\\').replace('"', '\\"')
                lines.append(f'{key}: "{val_clean}"')
            else:
                lines.append(f"{key}: {val}")
    
    return '\n'.join(lines)

def main():
    fixed = 0
    for rel_path in FILES_TO_FIX:
        file_path = ENTRY_ROOT / rel_path
        if not file_path.exists():
            print(f"⚠️  Not found: {rel_path}")
            continue
        
        try:
            text = file_path.read_text(encoding="utf-8")
            meta, body = extract_and_fix_front_matter(text)
            
            if meta:
                new_fm = rebuild_front_matter(meta)
                new_text = f"---\n{new_fm}\n---\n\n{body}"
                file_path.write_text(new_text, encoding="utf-8")
                fixed += 1
                print(f"✅ Fixed: {rel_path}")
            else:
                print(f"⚠️  Could not parse: {rel_path}")
        except Exception as e:
            print(f"❌ Error in {rel_path}: {e}")
    
    print(f"\n✅ Fixed {fixed}/{len(FILES_TO_FIX)} files")

if __name__ == "__main__":
    main()
