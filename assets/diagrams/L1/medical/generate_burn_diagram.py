#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create 240x240 image with black background
img = Image.new('RGB', (240, 240), color='black')
draw = ImageDraw.Draw(img)

# Colors
CYAN = '#00FFFF'
WHITE = '#FFFFFF'
RED = '#FF0000'
ORANGE = '#FF6600'

# Try to use a basic font, fall back to default if not available
try:
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
    font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 7)
except:
    font_small = ImageFont.load_default()
    font_tiny = ImageFont.load_default()

# Title
draw.text((120, 5), "BURN DEPTH", fill=WHITE, anchor="mt", font=font_small)

# Draw 4 cross-sections side by side
sections = [
    {"x": 30, "label": "1st°", "depth": 1, "color": RED},
    {"x": 85, "label": "2nd°", "depth": 2, "color": ORANGE},
    {"x": 140, "label": "3rd°", "depth": 3, "color": WHITE},
    {"x": 195, "label": "4th°", "depth": 4, "color": RED}
]

for sec in sections:
    x = sec["x"]
    
    # Epidermis (thin top layer)
    draw.rectangle([x-15, 40, x+15, 45], outline=CYAN, width=1)
    
    # Dermis (thicker middle layer)
    draw.rectangle([x-15, 45, x+15, 75], outline=CYAN, width=1)
    # Nerve endings in dermis (small dots)
    for i in range(3):
        for j in range(2):
            draw.ellipse([x-10+i*10, 50+j*10, x-8+i*10, 52+j*10], fill=CYAN)
    
    # Subcutaneous (fat layer)
    draw.rectangle([x-15, 75, x+15, 100], outline=CYAN, width=1)
    # Fat cells (small circles)
    for i in range(2):
        for j in range(2):
            draw.ellipse([x-10+i*12, 80+j*10, x-5+i*12, 85+j*10], outline=CYAN)
    
    # Muscle (bottom layer with lines)
    draw.rectangle([x-15, 100, x+15, 115], outline=CYAN, width=1)
    for i in range(3):
        draw.line([x-15, 105+i*5, x+15, 105+i*5], fill=CYAN, width=1)
    
    # Draw burn depth indicator
    if sec["depth"] == 1:
        # Superficial - just surface
        draw.line([x-18, 42, x-15, 42], fill=sec["color"], width=2)
        draw.line([x+15, 42, x+18, 42], fill=sec["color"], width=2)
    elif sec["depth"] == 2:
        # Partial thickness - into dermis
        draw.line([x-18, 42, x-18, 60], fill=sec["color"], width=2)
        draw.line([x+18, 42, x+18, 60], fill=sec["color"], width=2)
    elif sec["depth"] == 3:
        # Full thickness - through all skin
        draw.line([x-18, 42, x-18, 75], fill=sec["color"], width=2)
        draw.line([x+18, 42, x+18, 75], fill=sec["color"], width=2)
    elif sec["depth"] == 4:
        # 4th degree - into muscle
        draw.line([x-18, 42, x-18, 110], fill=sec["color"], width=2)
        draw.line([x+18, 42, x+18, 110], fill=sec["color"], width=2)
    
    # Label
    draw.text((x, 125), sec["label"], fill=WHITE, anchor="mt", font=font_small)

# Layer labels on left side
draw.text((5, 42), "Epi", fill=CYAN, font=font_tiny)
draw.text((5, 60), "Der", fill=CYAN, font=font_tiny)
draw.text((5, 87), "Sub", fill=CYAN, font=font_tiny)
draw.text((5, 107), "Mus", fill=CYAN, font=font_tiny)

# Legend at bottom
draw.text((120, 140), "Red/Orange = Burn damage", fill=ORANGE, anchor="mt", font=font_tiny)
draw.text((120, 150), "White = Full thickness", fill=WHITE, anchor="mt", font=font_tiny)
draw.text((120, 160), "Cyan = Normal tissue", fill=CYAN, anchor="mt", font=font_tiny)

# Pain indicator
draw.text((120, 180), "PAIN LEVEL:", fill=WHITE, anchor="mt", font=font_tiny)
draw.text((30, 195), "1st: HIGH", fill=RED, anchor="mt", font=font_tiny)
draw.text((85, 195), "2nd: HIGHEST", fill=ORANGE, anchor="mt", font=font_tiny)
draw.text((140, 195), "3rd: LOW", fill=WHITE, anchor="mt", font=font_tiny)
draw.text((195, 195), "4th: NONE", fill=RED, anchor="mt", font=font_tiny)

# Rule of 9s reference
draw.text((120, 215), "Rule of 9s: Palm = 1% BSA", fill=CYAN, anchor="mt", font=font_tiny)

# Save
output_path = "burns.png"
img.save(output_path)
print(f"Saved: {output_path}")
