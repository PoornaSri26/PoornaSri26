#!/usr/bin/env python3
"""
Generate an animated GIF GitHub profile banner.

Design language:
- High-end developer / AI engineer
- Minimal dark interface
- Cyberpunk & Glassmorphic accents
- Terminal-inspired identity with typewriter animation
- Smooth-looping orbital system visualization
- Optimized GIF generation for GitHub README compatibility

Output:
    assets/banner.gif
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont


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
        
        # Colors (RGB Tuple format for Pillow performance)
        "background": (7, 10, 15),
        "background_2": (11, 16, 24),
        "background_3": (15, 22, 32),
        "cyan": (0, 229, 255),
        "blue": (77, 124, 254),
        "purple": (139, 92, 246),
        "pink": (255, 105, 180),
        "hot_pink": (255, 20, 147),
        "white": (245, 247, 250),
        "muted": (127, 138, 154),
        "dim": (57, 67, 81),
        "green": (45, 212, 191),
        "yellow": (255, 189, 70),
        "red": (255, 95, 86),
        
        # Rendering Parameters (optimized for GitHub)
        "width": 1280,
        "height": 430,
        "frames": 30,  # Reduced for smaller file size
        "duration": 100,  # 100ms per frame (10 FPS)
    }

    # ============================================================
    # FONT ENGINE & FALLBACKS
    # ============================================================

    def load_font(font_names, size):
        for font_name in font_names:
            try:
                return ImageFont.truetype(font_name, size)
            except OSError:
                continue
        return ImageFont.load_default()

    fonts = {
        "small": load_font(["DejaVuSans.ttf", "arial.ttf", "Helvetica"], 11),
        "medium": load_font(["DejaVuSans.ttf", "arial.ttf", "Helvetica"], 14),
        "large": load_font(["DejaVuSans-Bold.ttf", "arialbd.ttf", "Helvetica-Bold"], 56),
        "mono": load_font(["DejaVuSansMono.ttf", "consolas.ttf", "Courier"], 13),
        "mono_small": load_font(["DejaVuSansMono.ttf", "consolas.ttf", "Courier"], 10),
        "mono_bold": load_font(["DejaVuSansMono-Bold.ttf", "consolab.ttf", "Courier-Bold"], 13),
    }

    # ============================================================
    # ADVANCED DRAWING FUNCTIONS
    # ============================================================

    def draw_multi_gradient_bg(image, colors):
        """Draw multi-stop gradient background"""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        num_colors = len(colors)
        
        for y in range(height):
            ratio = y / height
            # Determine which color segment we're in
            segment_size = 1.0 / (num_colors - 1)
            segment = int(ratio / segment_size)
            segment = min(segment, num_colors - 2)
            
            # Interpolate between two colors
            local_ratio = (ratio - segment * segment_size) / segment_size
            c1 = colors[segment]
            c2 = colors[segment + 1]
            
            r = int(c1[0] * (1 - local_ratio) + c2[0] * local_ratio)
            g = int(c1[1] * (1 - local_ratio) + c2[1] * local_ratio)
            b = int(c1[2] * (1 - local_ratio) + c2[2] * local_ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))

    def draw_glow_ellipse(draw, bbox, color, glow_radius=10):
        """Draw ellipse with glow effect"""
        # Draw multiple layers for glow
        for i in range(glow_radius, 0, -2):
            alpha = int(30 * (1 - i / glow_radius))
            glow_color = (*color, alpha)
            expanded_bbox = [bbox[0] - i, bbox[1] - i, bbox[2] + i, bbox[3] + i]
            # Note: PIL doesn't support alpha directly in draw, so we simulate with darker colors
            glow_color = tuple(max(0, c - i * 2) for c in color)
            draw.ellipse(expanded_bbox, fill=glow_color)
        
        # Main ellipse
        draw.ellipse(bbox, fill=color)

    def draw_dashed_ellipse(draw, bbox, color, dash_length=8, gap_length=4):
        """Draw dashed ellipse"""
        cx = (bbox[0] + bbox[2]) / 2
        cy = (bbox[1] + bbox[3]) / 2
        rx = (bbox[2] - bbox[0]) / 2
        ry = (bbox[3] - bbox[1]) / 2
        
        total = dash_length + gap_length
        num_dashes = int(2 * math.pi * max(rx, ry) / total)
        
        for i in range(num_dashes):
            start_angle = (i * total) / max(rx, ry)
            end_angle = ((i * total) + dash_length) / max(rx, ry)
            
            x1 = cx + rx * math.cos(start_angle)
            y1 = cy + ry * math.sin(start_angle)
            x2 = cx + rx * math.cos(end_angle)
            y2 = cy + ry * math.sin(end_angle)
            
            draw.line([(x1, y1), (x2, y2)], fill=color, width=2)

    # ============================================================
    # GENERATE ANIMATION FRAMES
    # ============================================================

    frames = []

    for frame_num in range(config["frames"]):
        frame_ratio = frame_num / config["frames"]

        # Base Image Canvas
        img = Image.new('RGB', (config["width"], config["height"]), config["background"])
        draw = ImageDraw.Draw(img)

        # Multi-stop Background Gradient
        draw_multi_gradient_bg(img, [
            config["background"],
            config["background_2"],
            config["background_3"],
            config["background_2"],
            config["background"]
        ])

        # Enhanced Grid Pattern
        for x in range(0, config["width"], 42):
            alpha = int(20 + 10 * math.sin(frame_ratio * 2 * math.pi + x * 0.01))
            grid_color = (alpha, alpha + 5, alpha + 10)
            draw.line([(x, 0), (x, config["height"])], fill=grid_color)
        for y in range(0, config["height"], 42):
            alpha = int(20 + 10 * math.cos(frame_ratio * 2 * math.pi + y * 0.01))
            grid_color = (alpha, alpha + 5, alpha + 10)
            draw.line([(0, y), (config["width"], y)], fill=grid_color)

        # Micro-grid overlay
        for x in range(0, config["width"], 10):
            draw.line([(x, 0), (x, config["height"])], fill=(12, 18, 26))
        for y in range(0, config["height"], 10):
            draw.line([(0, y), (config["width"], y)], fill=(12, 18, 26))

        # Outer Frame with rounded corners effect
        draw.rectangle([24, 24, config["width"] - 24, config["height"] - 24], 
                      outline=(52, 62, 78), width=2)
        draw.rectangle([26, 26, config["width"] - 26, config["height"] - 26], 
                      outline=(32, 42, 58), width=1)

        # Top System Bar
        draw.line([58, 72, config["width"] - 58, 72], fill=(55, 65, 80), width=2)
        
        # Animated system indicator
        indicator_pulse = 1.0 + 0.15 * math.sin(frame_ratio * 4 * math.pi)
        indicator_radius = int(4 * indicator_pulse)
        draw.ellipse([62 - indicator_radius, 51 - indicator_radius, 
                     62 + indicator_radius, 51 + indicator_radius], 
                    fill=config["green"])

        draw.text((76, 48), "SYSTEM ONLINE", fill=config["muted"], font=fonts["small"])
        draw.text((config["width"] - 180, 48), "PORTFOLIO / 2026", 
                 fill=config["dim"], font=fonts["mono_small"])

        # Profile Identity Section
        draw.text((78, 116), "SOFTWARE ENGINEER", fill=config["pink"], 
                 font=fonts["mono_small"])

        # Enhanced Pulsing Name Header with shadow
        shadow_offset = 2
        draw.text((75 + shadow_offset, 138 + shadow_offset), config["name"], 
                 fill=(30, 40, 50), font=fonts["large"])
        draw.text((75, 138), config["name"], fill=config["white"], 
                 font=fonts["large"])

        # Dynamic Expanding Accent Bar with gradient effect
        line_length = 120 + int(160 * (0.5 + 0.5 * math.sin(frame_ratio * 2 * math.pi)))
        for i in range(line_length):
            ratio = i / line_length
            r = int(config["cyan"][0] * (1 - ratio) + config["pink"][0] * ratio)
            g = int(config["cyan"][1] * (1 - ratio) + config["pink"][1] * ratio)
            b = int(config["cyan"][2] * (1 - ratio) + config["pink"][2] * ratio)
            draw.rectangle([78 + i, 204, 78 + i + 1, 206], fill=(r, g, b))

        # Headline with better spacing
        draw.text((78, 222), config["headline"], fill=config["muted"], 
                 font=fonts["medium"])

        # Enhanced Terminal Box UI
        draw.rectangle([78, 253, 768, 337], fill=(14, 19, 28), 
                      outline=config["pink"], width=2)
        draw.rectangle([80, 255, 766, 335], fill=(10, 15, 22))
        draw.line([78, 280, 768, 280], fill=(45, 55, 70), width=2)

        # Terminal Control Dots with glow
        draw_glow_ellipse(draw, [92, 263, 100, 271], config["red"], glow_radius=6)
        draw_glow_ellipse(draw, [107, 263, 115, 271], config["yellow"], glow_radius=6)
        draw_glow_ellipse(draw, [122, 263, 130, 271], config["green"], glow_radius=6)
        
        draw.text((145, 261), "developer@poornasri:~", fill=config["dim"], 
                 font=fonts["mono_small"])

        # Enhanced Typewriter Text Logic
        stack_text = config["stack"]
        # More sophisticated typing animation with pauses
        if frame_ratio < 0.3:
            typed_len = int((frame_ratio / 0.3) * len(stack_text))
        elif frame_ratio < 0.5:
            typed_len = len(stack_text)  # Pause
        elif frame_ratio < 0.8:
            typed_len = len(stack_text)  # Stay
        else:
            typed_len = int(len(stack_text) * (1 - (frame_ratio - 0.8) / 0.2))  # Fade out
        
        visible_stack = stack_text[:max(0, min(len(stack_text), typed_len))]
        
        prompt_str = "> stack: "
        draw.text((98, 298), prompt_str, fill=config["cyan"], font=fonts["mono_bold"])
        
        prompt_bbox = fonts["mono_bold"].getbbox(prompt_str)
        prompt_width = prompt_bbox[2] - prompt_bbox[0] if prompt_bbox else 70
        
        draw.text((98 + prompt_width, 298), visible_stack, fill=config["white"], 
                 font=fonts["mono"])

        # Enhanced Blinking Terminal Cursor
        cursor_blink = math.sin(frame_ratio * 10 * math.pi) > 0
        if cursor_blink:
            stack_bbox = fonts["mono"].getbbox(visible_stack) if visible_stack else (0, 0, 0, 0)
            stack_width = stack_bbox[2] - stack_bbox[0]
            cursor_x = 98 + prompt_width + stack_width + 2
            # Cursor with glow
            for i in range(3):
                glow_alpha = 255 - i * 80
                cursor_color = tuple(max(0, c - i * 30) for c in config["pink"])
                draw.rectangle([cursor_x - i, 297 - i, cursor_x + 7 + i, 313 + i], 
                              fill=cursor_color)

        # Enhanced Orbital Visualizer System
        cx, cy = 1030, 215

        # Background glow
        glow_radius = 150 + 20 * math.sin(frame_ratio * 2 * math.pi)
        draw.ellipse([cx - glow_radius, cy - glow_radius, 
                     cx + glow_radius, cy + glow_radius], 
                    fill=(config["cyan"][0] // 4, config["cyan"][1] // 4, config["cyan"][2] // 4))

        # Multiple orbital layers with different rotation speeds
        orbital_configs = [
            (150, config["cyan"], 1.0, 20),
            (120, config["blue"], -0.8, 15),
            (90, config["purple"], 1.2, 12),
            (60, config["pink"], -1.5, 8),
        ]

        for radius, color, speed, node_size in orbital_configs:
            # Dashed orbital ring
            draw_dashed_ellipse(draw, [cx - radius, cy - radius, 
                                    cx + radius, cy + radius], 
                              color, dash_length=10, gap_length=5)
            
            # Multiple orbiting nodes
            for i in range(3):
                angle = (frame_ratio * 2 * math.pi * speed) + (i * 2 * math.pi / 3)
                ox = cx + radius * math.cos(angle)
                oy = cy + radius * math.sin(angle)
                draw_glow_ellipse(draw, [ox - node_size, oy - node_size, 
                                       ox + node_size, oy + node_size], 
                                color, glow_radius=8)

        # Enhanced Crosshair Guidelines
        for i in range(3):
            alpha = 100 - i * 30
            line_color = tuple(max(0, c - i * 10) for c in config["dim"])
            offset = i * 8
            draw.line([cx - 132 - offset, cy, cx - 50 - offset, cy], 
                     fill=line_color, width=1)
            draw.line([cx + 50 + offset, cy, cx + 132 + offset, cy], 
                     fill=line_color, width=1)
            draw.line([cx, cy - 132 - offset, cx, cy - 50 - offset], 
                     fill=line_color, width=1)
            draw.line([cx, cy + 50 + offset, cx, cy + 132 + offset], 
                     fill=line_color, width=1)

        # Enhanced Core Pulsing Radar Center
        draw.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], 
                    fill=(11, 17, 26), outline=config["pink"], width=3)
        
        # Multiple pulsing rings
        for i in range(3):
            ring_offset = i * 4
            ring_pulse = 1.0 + 0.3 * math.sin(frame_ratio * 3 * math.pi + i)
            ring_r = int((8 + ring_offset) * ring_pulse)
            ring_alpha = int(150 * (1 - i / 3))
            ring_color = tuple(max(0, c - i * 20) for c in config["pink"])
            draw.ellipse([cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r], 
                        outline=ring_color, width=2)

        # Core center
        core_r = 9 + int(4 * math.sin(frame_ratio * 4 * math.pi))
        draw_glow_ellipse(draw, [cx - core_r, cy - core_r, cx + core_r, cy + core_r], 
                         config["hot_pink"], glow_radius=12)

        # Enhanced Bottom System Info Footer
        draw.line([78, 360, config["width"] - 78, 360], fill=(55, 65, 80), width=2)
        
        # Status indicator with pulse
        status_pulse = 1.0 + 0.2 * math.sin(frame_ratio * 3 * math.pi)
        status_radius = int(3 * status_pulse)
        draw.ellipse([81 - status_radius, 381 - status_radius, 
                     87 + status_radius, 387 + status_radius], 
                    fill=config["green"])
        
        draw.text((97, 378), "STATUS:", fill=config["muted"], font=fonts["mono_small"])
        draw.text((150, 378), config["status"], fill=config["green"], 
                 font=fonts["mono_small"])

        draw.text((480, 378), "LOCATION:", fill=config["dim"], font=fonts["mono_small"])
        draw.text((550, 378), config["location"], fill=config["muted"], 
                 font=fonts["mono_small"])

        draw.text((config["width"] - 210, 378), "BUILD:", fill=config["dim"], 
                 font=fonts["mono_small"])
        draw.text((config["width"] - 165, 378), "ACTIVE", fill=config["pink"], 
                 font=fonts["mono_small"])

        # Enhanced Corner Details with animated glow
        corner_pulse = 1.0 + 0.1 * math.sin(frame_ratio * 2 * math.pi)
        
        # Top-left corner
        draw.line([24, 65, 24, 42], fill=config["pink"], width=3)
        draw.line([24, 42, 65, 42], fill=config["pink"], width=3)
        draw.ellipse([24, 42, 24 + int(10 * corner_pulse), 42 + int(10 * corner_pulse)], 
                    fill=config["pink"])
        
        # Bottom-right corner
        draw.line([config["width"] - 65, config["height"] - 42, 
                  config["width"] - 24, config["height"] - 42], 
                 fill=config["purple"], width=3)
        draw.line([config["width"] - 24, config["height"] - 42, 
                  config["width"] - 24, config["height"] - 65], 
                 fill=config["purple"], width=3)
        draw.ellipse([config["width"] - 24 - int(8 * corner_pulse), 
                     config["height"] - 42 - int(8 * corner_pulse), 
                     config["width"] - 24, config["height"] - 42], 
                    fill=config["purple"])

        # Ambient floating particles
        for i in range(8):
            particle_x = 100 + i * 140 + 20 * math.sin(frame_ratio * 2 * math.pi + i)
            particle_y = 100 + 50 * math.sin(frame_ratio * 3 * math.pi + i * 0.5)
            particle_size = 2 + int(2 * math.sin(frame_ratio * 4 * math.pi + i))
            particle_color = config["cyan"] if i % 2 == 0 else config["pink"]
            draw.ellipse([particle_x - particle_size, particle_y - particle_size,
                        particle_x + particle_size, particle_y + particle_size],
                       fill=particle_color)

        frames.append(img)

    # ============================================================
    # SAVE OPTIMIZED GIF
    # ============================================================

    os.makedirs("assets", exist_ok=True)
    output_path = os.path.join("assets", "banner.gif")

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=config["duration"],
        loop=0,
        optimize=True,
        quality=85,  # Balance quality and file size
        method=6  # Maximum compression
    )

    print(f"Enhanced animated GIF banner generated: {output_path}")
    print(f"Frames: {config['frames']}, Duration: {config['duration']}ms per frame")
    return output_path


if __name__ == "__main__":
    create_animated_banner()