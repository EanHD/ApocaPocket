#!/bin/bash
# Batch diagram generator for ApocaPocket
# Usage: bash tools/batch_generate_diagrams.sh prompts/batch_01.txt

PROMPT_FILE="$1"
SKILL_PATH="$HOME/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py"

if [ -z "$PROMPT_FILE" ]; then
    echo "Usage: $0 <prompt_file>"
    echo "Example: $0 prompts/batch_01.txt"
    exit 1
fi

if [ ! -f "$PROMPT_FILE" ]; then
    echo "Error: Prompt file not found: $PROMPT_FILE"
    exit 1
fi

echo "═══════════════════════════════════════════"
echo " ApocaPocket Diagram Batch Generator"
echo "═══════════════════════════════════════════"
echo ""
echo "Prompt file: $PROMPT_FILE"
echo ""

# Parse prompt file format:
# --- DIAGRAM: <output_path>
# <prompt text>
# --- END

current_output=""
current_prompt=""
line_count=0

while IFS= read -r line || [ -n "$line" ]; do
    line_count=$((line_count + 1))
    
    if [[ $line == "--- DIAGRAM:"* ]]; then
        # Save previous diagram if exists
        if [ -n "$current_output" ] && [ -n "$current_prompt" ]; then
            echo "→ Generating: $current_output"
            uv run "$SKILL_PATH" \
                --prompt "$current_prompt" \
                --filename "$current_output" \
                --resolution 1K
            echo "  ✓ Saved"
            echo ""
        fi
        
        # Start new diagram
        current_output=$(echo "$line" | sed 's/^--- DIAGRAM: //')
        current_prompt=""
    elif [[ $line == "--- END" ]]; then
        # Generate current diagram
        if [ -n "$current_output" ] && [ -n "$current_prompt" ]; then
            echo "→ Generating: $current_output"
            uv run "$SKILL_PATH" \
                --prompt "$current_prompt" \
                --filename "$current_output" \
                --resolution 1K
            echo "  ✓ Saved"
            echo ""
        fi
        current_output=""
        current_prompt=""
    else
        # Accumulate prompt text
        if [ -n "$current_output" ]; then
            if [ -n "$current_prompt" ]; then
                current_prompt="$current_prompt
$line"
            else
                current_prompt="$line"
            fi
        fi
    fi
done < "$PROMPT_FILE"

# Handle last diagram if file doesn't end with --- END
if [ -n "$current_output" ] && [ -n "$current_prompt" ]; then
    echo "→ Generating: $current_output"
    uv run "$SKILL_PATH" \
        --prompt "$current_prompt" \
        --filename "$current_output" \
        --resolution 1K
    echo "  ✓ Saved"
    echo ""
fi

echo "═══════════════════════════════════════════"
echo " Batch complete!"
echo "═══════════════════════════════════════════"
echo ""
echo "Review images in: assets/diagrams/"
echo "Move rejected images to: assets/rejected/"
