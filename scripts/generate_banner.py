#!/usr/bin/env python3
"""
Generate personalized Barbie-themed banner for GitHub profile
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_barbie_banner():
    """Create a personalized Barbie-themed banner"""
    
    # Image dimensions
    width, height = 1200, 400
    
    # Barbie theme colors
    colors = {
        'primary': '#E91E63',      # Hot pink
        'secondary': '#F48FB1',    # Light pink
        'accent': '#CE93D8',       # Purple
        'background': '#FFFFFF',   # White
        'text': '#880E4F',         # Dark pink
        'dark': '#4A148C'          # Purple
    }
    
    # Create image with white background
    img = Image.new('RGB', (width, height), colors['background'])
    draw = ImageDraw.Draw(img)
    
    # Draw gradient background
    for y in range(height):
        # Create gradient from white to light pink
        ratio = y / height
        r = int(255 * (1 - ratio) + 244 * ratio)
        g = int(255 * (1 - ratio) + 143 * ratio)
        b = int(255 * (1 - ratio) + 177 * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))
    
    # Add decorative elements
    # Pink circles
    draw.ellipse([50, 50, 150, 150], fill=colors['secondary'])
    draw.ellipse([1050, 250, 1150, 350], fill=colors['accent'])
    draw.ellipse([100, 300, 200, 400], fill=colors['primary'])
    
    # Try to load fonts, fall back to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        subtitle_font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # User information
    name = "POORNA SRI"
    role = "Full Stack Engineer / AI/ML Enthusiast / Tech Innovator"
    focus = "Focus: Gamified Productivity & AI Systems"
    current_project = "Current: Solo Quest (RPG Productivity App)"
    tech_stack = "Stack: React, TypeScript, Python, Node.js, AI/ML"
    status = "SYS_STATUS: ACTIVE"
    location = "[Hyderabad, India]"
    
    # Draw name
    draw.text((50, 80), name, fill=colors['dark'], font=title_font)
    
    # Draw role
    draw.text((50, 150), role, fill=colors['text'], font=subtitle_font)
    
    # Draw decorative line
    draw.line([(50, 190), (400, 190)], fill=colors['primary'], width=3)
    
    # Draw focus area
    draw.text((50, 210), focus, fill=colors['dark'], font=small_font)
    
    # Draw current project
    draw.text((50, 240), current_project, fill=colors['text'], font=small_font)
    
    # Draw tech stack
    draw.text((50, 270), tech_stack, fill=colors['text'], font=small_font)
    
    # Draw status indicator (radar-like circle)
    center_x, center_y = 1000, 200
    radius = 80
    
    # Draw radar circles
    for r in range(20, radius + 1, 20):
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], 
                    outline=colors['secondary'], width=1)
    
    # Draw radar lines
    for angle in range(0, 360, 45):
        import math
        rad = angle * math.pi / 180
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        draw.line([(center_x, center_y), (x, y)], fill=colors['accent'], width=1)
    
    # Draw center point
    draw.ellipse([center_x - 5, center_y - 5, center_x + 5, center_y + 5], 
                fill=colors['primary'])
    
    # Draw status text
    draw.text((850, 300), status, fill=colors['dark'], font=small_font)
    draw.text((950, 320), location, fill=colors['text'], font=small_font)
    
    # Add SYS_ACTIVE indicator
    draw.text((50, 320), "SYS_ACTIVE", fill=colors['primary'], font=small_font)
    
    # Ensure assets directory exists
    os.makedirs('assets', exist_ok=True)
    
    # Save image
    img.save('assets/banner.png')
    print("Barbie-themed banner generated successfully!")
    
    return 'assets/banner.png'

if __name__ == '__main__':
    create_barbie_banner()