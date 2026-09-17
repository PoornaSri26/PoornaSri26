#!/usr/bin/env python3

"""
Generate an animated GIF GitHub profile banner.

Design language:
- High-end developer / AI engineer
- Minimal dark interface
- Glassmorphism
- Terminal-inspired identity
- Circuit architecture
- Orbital system visualization
- Animated GIF for GitHub compatibility
- No emojis

Output:
    assets/banner.gif
"""

import os
from PIL import Image, ImageDraw, ImageFont
import math


def create_animated_banner():

    # ============================================================
    # CONFIGURATION
    # ============================================================

    config = {
        "name": "POORNA SRI",
        "headline": "FULL STACK ENGINEER / AI/ML ENTHUSIAST / SYSTEMS BUILDER",
        "stack": "React · TypeScript · Python · Node.js · PyTorch · Docker",
        "location": "Hyderabad, India",
        "status": "BUILDING THE FUTURE",
        
        # Colors
        "background": "#070A0F",
        "background_2": "#0B1018",
        "cyan": "#00E5FF",
        "blue": "#4D7CFE",
        "purple": "#8B5CF6",
        "pink": "#FF69B4",
        "hot_pink": "#FF1493",
        "white": "#F5F7FA",
        "muted": "#7F8A9A",
        "dim": "#394351",
        "green": "#2DD4BF",
        
        # Dimensions
        "width": 1280,
        "height": 430,
        "frames": 30,
        "duration": 100,  # ms per frame
    }

    # ============================================================
    # HELPER FUNCTIONS
    # ============================================================

    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def draw_gradient(draw, x1, y1, x2, y2, color1, color2):
        """Draw a vertical gradient"""
        for y in range(y1, y2):
            ratio = (y - y1) / (y2 - y1)
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(x1, y), (x2, y)], fill=(r, g, b))

    def draw_orbital(draw, cx, cy, radius, color, angle):
        """Draw an orbital ring with rotation"""
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=color)

    # ============================================================
    # CREATE FRAMES
    # ============================================================

    frames = []
    
    # Color conversion
    bg = hex_to_rgb(config["background"])
    bg2 = hex_to_rgb(config["background_2"])
    cyan = hex_to_rgb(config["cyan"])
    blue = hex_to_rgb(config["blue"])
    purple = hex_to_rgb(config["purple"])
    pink = hex_to_rgb(config["pink"])
    hot_pink = hex_to_rgb(config["hot_pink"])
    white = hex_to_rgb(config["white"])
    muted = hex_to_rgb(config["muted"])
    dim = hex_to_rgb(config["dim"])
    green = hex_to_rgb(config["green"])

    for frame_num in range(config["frames"]):
        # Create image
        img = Image.new('RGB', (config["width"], config["height"]), bg)
        draw = ImageDraw.Draw(img)

        # Background gradient
        draw_gradient(draw, 0, 0, config["width"], config["height"], bg, bg2)

        # Grid pattern (simplified)
        for x in range(0, config["width"], 42):
            draw.line([(x, 0), (x, config["height"])], fill=(20, 25, 35))
        for y in range(0, config["height"], 42):
            draw.line([(0, y), (config["width"], y)], fill=(20, 25, 35))

        # Outer frame
        draw.rectangle([24, 24, config["width"] - 24, config["height"] - 24], 
                       outline=(40, 45, 55), width=2)

        # Top system bar
        draw.line([58, 72, config["width"] - 58, 72], fill=(60, 65, 75))
        draw.ellipse([58, 47, 70, 59], fill=green)
        
        # Try to use system font, fallback to default
        try:
            font_small = ImageFont.truetype("arial.ttf", 11)
            font_medium = ImageFont.truetype("arial.ttf", 14)
            font_large = ImageFont.truetype("arial.ttf", 57)
            font_mono = ImageFont.truetype("consolas.ttf", 13)
        except:
            font_small = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_large = ImageFont.load_default()
            font_mono = ImageFont.load_default()

        draw.text((76, 51), "SYSTEM ONLINE", fill=muted, font=font_small)
        draw.text((config["width"] - 195, 51), "PORTFOLIO / 2026", fill=dim, font=font_small)

        # Left content - Identity label
        draw.text((78, 116), "SOFTWARE ENGINEER", fill=pink, font=font_small)

        # Name with pulsing effect
        pulse = 1 + 0.1 * math.sin(frame_num * 0.3)
        name_size = int(57 * pulse)
        try:
            font_name = ImageFont.truetype("arial.ttf", name_size)
        except:
            font_name = font_large
        draw.text((75, 176), config["name"], fill=white, font=font_name)

        # Accent line with growing animation
        line_width = 90 + (frame_num / config["frames"]) * 160
        draw.rectangle([78, 193, 78 + line_width, 195], fill=pink)

        # Headline
        draw.text((78, 225), config["headline"], fill=muted, font=font_medium)

        # Terminal window
        draw.rectangle([78, 253, 768, 337], fill=(15, 20, 30), outline=pink, width=2)
        draw.line([78, 280, 768, 280], fill=(40, 45, 55))
        
        # Terminal dots
        draw.ellipse([92, 263, 100, 271], fill=(255, 95, 86))
        draw.ellipse([107, 263, 115, 271], fill=(255, 189, 46))
        draw.ellipse([122, 263, 130, 271], fill=(39, 201, 63))
        
        draw.text((150, 271), "developer@poornasri:~", fill=dim, font=font_small)

        # Typing animation for stack
        chars_to_show = int((frame_num / config["frames"]) * len(config["stack"]))
        visible_stack = config["stack"][:chars_to_show] + ("_" if frame_num % 2 < 1 else "")
        draw.text((103, 307), f"> stack: {visible_stack}", fill=cyan, font=font_mono)

        # Cursor blinking
        if frame_num % 4 < 2:
            cursor_x = 103 + len(f"> stack: {visible_stack}") * 8
            draw.rectangle([cursor_x, 294, cursor_x + 7, 310], fill=pink)

        # Right side - Orbital system
        cx, cy = 1030, 215
        
        # Orbitals with rotation
        for i, (radius, color) in enumerate([(132, cyan), (98, pink), (58, purple)]):
            angle = (frame_num * 0.05) + (i * 2)
            draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], 
                        outline=color, width=1)
            # Dashed effect
            for j in range(0, 360, 15):
                rad = math.radians(angle + j)
                if j % 30 < 15:
                    ox = cx + radius * math.cos(rad)
                    oy = cy + radius * math.sin(rad)
                    draw.ellipse([ox - 2, oy - 2, ox + 2, oy + 2], fill=color)

        # Architecture lines
        draw.line([cx - 132, cy, cx - 50, cy], fill=cyan)
        draw.line([cx + 50, cy, cx + 132, cy], fill=cyan)
        draw.line([cx, cy - 132, cx, cy - 50], fill=cyan)
        draw.line([cx, cy + 50, cx, cy + 132], fill=cyan)

        # Rotating nodes
        node_angle = frame_num * 0.1
        draw_orbital(draw, cx, cy, 98, hot_pink, node_angle)
        draw_orbital(draw, cx, cy, 98, cyan, node_angle + math.pi)
        draw_orbital(draw, cx, cy, 132, blue, node_angle + math.pi/2)

        # Core
        draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=(11, 17, 26), outline=pink, width=2)
        core_pulse = 9 + 2 * math.sin(frame_num * 0.4)
        draw.ellipse([cx - core_pulse, cy - core_pulse, cx + core_pulse, cy + core_pulse], fill=pink)

        # Lower information bar
        draw.line([78, 360, config["width"] - 78, 360], fill=(60, 65, 75))
        
        draw.ellipse([81, 380, 87, 386], fill=green)
        draw.text((97, 387), "STATUS:", fill=muted, font=font_small)
        draw.text((150, 387), config["status"], fill=green, font=font_small)
        
        draw.text((490, 387), "LOCATION", fill=dim, font=font_small)
        draw.text((555, 387), config["location"], fill=muted, font=font_small)
        
        draw.text((config["width"] - 230, 387), "BUILD", fill=dim, font=font_small)
        draw.text((config["width"] - 182, 387), "ACTIVE", fill=pink, font=font_small)

        # Corner details
        draw.line([24, 65, 24, 42], fill=pink, width=2)
        draw.line([24, 42, 65, 42], fill=pink, width=2)
        draw.line([config["width"] - 65, config["height"] - 42, config["width"] - 24, config["height"] - 42], fill=purple, width=2)
        draw.line([config["width"] - 24, config["height"] - 42, config["width"] - 24, config["height"] - 65], fill=purple, width=2)

        frames.append(img)

    # ============================================================
    # SAVE GIF
    # ============================================================

    os.makedirs("assets", exist_ok=True)
    output_path = os.path.join("assets", "banner.gif")
    
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=config["duration"],
        loop=0,
        optimize=True
    )

    print(f"Animated GIF banner generated: {output_path}")
    return output_path


if __name__ == "__main__":
    create_animated_banner()