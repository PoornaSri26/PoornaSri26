#!/usr/bin/env python3

"""
Generate a premium static SVG GitHub profile banner.

Design language:
- High-end developer / AI engineer
- Minimal dark interface
- Glassmorphism
- Terminal-inspired identity
- Circuit architecture
- Orbital system visualization
- Static (no animations for GitHub compatibility)
- No emojis

Output:
    assets/banner.svg
"""

import os
from html import escape


def create_animated_banner():

    # ============================================================
    # PROFILE CONFIGURATION
    # ============================================================

    config = {
        "name": "POORNA SRI",

        "headline": (
            "FULL STACK ENGINEER  /  AI/ML ENTHUSIAST  /  "
            "SYSTEMS BUILDER"
        ),

        "stack": (
            "React  ·  TypeScript  ·  Python  ·  Node.js  ·  "
            "PyTorch  ·  Docker"
        ),

        "location": "Hyderabad, India",

        "status": "BUILDING THE FUTURE",

        # Core palette
        "background": "#070A0F",
        "background_2": "#0B1018",
        "panel": "#0D131D",

        "cyan": "#00E5FF",
        "blue": "#4D7CFE",
        "purple": "#8B5CF6",

        "white": "#F5F7FA",
        "muted": "#7F8A9A",
        "dim": "#394351",

        "green": "#2DD4BF",
        
        # Enhanced with pink for personal touch
        "pink": "#FF69B4",
        "hot_pink": "#FF1493",
    }

    # ============================================================
    # ESCAPED TEXT
    # ============================================================

    name = escape(config["name"])
    headline = escape(config["headline"])
    stack = escape(config["stack"])
    location = escape(config["location"])
    status = escape(config["status"])

    # ============================================================
    # SVG (Static version for GitHub compatibility)
    # ============================================================

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
    width="1280"
    height="430"
    viewBox="0 0 1280 430"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>

<defs>

    <!-- ========================================================
         BACKGROUND
         ======================================================== -->

    <linearGradient
        id="backgroundGradient"
        x1="0"
        y1="0"
        x2="1280"
        y2="430"
        gradientUnits="userSpaceOnUse"
    >
        <stop offset="0" stop-color="{config['background']}"/>
        <stop offset="0.5" stop-color="{config['background_2']}"/>
        <stop offset="1" stop-color="{config['background']}"/>
    </linearGradient>


    <!-- ========================================================
         MAIN ACCENT (Enhanced with pink touch)
         ======================================================== -->

    <linearGradient
        id="accentGradient"
        x1="0"
        y1="0"
        x2="600"
        y2="0"
        gradientUnits="userSpaceOnUse"
    >
        <stop offset="0" stop-color="{config['cyan']}"/>
        <stop offset="0.35" stop-color="{config['blue']}"/>
        <stop offset="0.65" stop-color="{config['purple']}"/>
        <stop offset="1" stop-color="{config['pink']}"/>
    </linearGradient>


    <linearGradient
        id="terminalGradient"
        x1="80"
        y1="270"
        x2="760"
        y2="270"
        gradientUnits="userSpaceOnUse"
    >
        <stop offset="0" stop-color="{config['cyan']}" stop-opacity="0.08"/>
        <stop offset="0.5" stop-color="{config['pink']}" stop-opacity="0.05"/>
        <stop offset="1" stop-color="{config['purple']}" stop-opacity="0.03"/>
    </linearGradient>


    <!-- ========================================================
         GRID
         ======================================================== -->

    <pattern
        id="grid"
        width="42"
        height="42"
        patternUnits="userSpaceOnUse"
    >
        <path
            d="M42 0H0V42"
            stroke="{config['white']}"
            stroke-opacity="0.035"
            stroke-width="1"
        />
    </pattern>


    <pattern
        id="microGrid"
        width="10"
        height="10"
        patternUnits="userSpaceOnUse"
    >
        <path
            d="M10 0H0V10"
            stroke="{config['white']}"
            stroke-opacity="0.012"
            stroke-width="1"
        />
    </pattern>


    <!-- ========================================================
         GLOWS
         ======================================================== -->

    <filter
        id="glowCyan"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%"
    >
        <feGaussianBlur
            stdDeviation="7"
            result="blur"
        />

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>


    <filter
        id="glowPink"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%"
    >
        <feGaussianBlur
            stdDeviation="8"
            result="blur"
        />

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>


    <filter
        id="glowSoft"
        x="-100%"
        y="-100%"
        width="300%"
        height="300%"
    >
        <feGaussianBlur
            stdDeviation="3"
            result="blur"
        />

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>


    <!-- ========================================================
         RADIAL GLOW (Enhanced with pink)
         ======================================================== -->

    <radialGradient
        id="cyanAura"
        cx="0"
        cy="0"
        r="1"
        gradientUnits="userSpaceOnUse"
        gradientTransform="translate(1050 210) rotate(90) scale(190)"
    >

        <stop
            offset="0"
            stop-color="{config['cyan']}"
            stop-opacity="0.12"
        />

        <stop
            offset="0.35"
            stop-color="{config['pink']}"
            stop-opacity="0.08"
        />

        <stop
            offset="0.65"
            stop-color="{config['blue']}"
            stop-opacity="0.05"
        />

        <stop
            offset="1"
            stop-color="{config['cyan']}"
            stop-opacity="0"
        />

    </radialGradient>

</defs>


<!-- ============================================================
     BACKGROUND
     ============================================================ -->

<rect
    width="1280"
    height="430"
    fill="url(#backgroundGradient)"
/>


<rect
    width="1280"
    height="430"
    fill="url(#microGrid)"
/>


<rect
    width="1280"
    height="430"
    fill="url(#grid)"
/>


<!-- ============================================================
     AMBIENT LIGHT
     ============================================================ -->

<ellipse
    cx="1040"
    cy="215"
    rx="270"
    ry="210"
    fill="url(#cyanAura)"
/>


<circle
    cx="160"
    cy="70"
    r="110"
    fill="{config['purple']}"
    opacity="0.025"
/>


<!-- ============================================================
     OUTER FRAME
     ============================================================ -->

<rect
    x="24"
    y="24"
    width="1232"
    height="382"
    rx="18"
    fill="#FFFFFF"
    fill-opacity="0.012"
    stroke="#FFFFFF"
    stroke-opacity="0.08"
/>


<!-- ============================================================
     TOP SYSTEM BAR
     ============================================================ -->

<g>

    <line
        x1="58"
        y1="72"
        x2="1222"
        y2="72"
        stroke="{config['white']}"
        stroke-opacity="0.06"
    />


    <!-- System indicator -->

    <circle
        cx="62"
        cy="51"
        r="4"
        fill="{config['green']}"
        filter="url(#glowSoft)"
    />


    <text
        x="76"
        y="55"
        fill="{config['muted']}"
        font-family="Inter, Segoe UI, Arial, sans-serif"
        font-size="11"
        font-weight="600"
        letter-spacing="2"
    >
        SYSTEM ONLINE
    </text>


    <text
        x="1085"
        y="55"
        fill="{config['dim']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="10"
        letter-spacing="1"
    >
        PORTFOLIO / 2026
    </text>

</g>


<!-- ============================================================
     LEFT CONTENT
     ============================================================ -->

<g>

    <!-- Small identity label -->

    <text
        x="78"
        y="116"
        fill="{config['pink']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="11"
        font-weight="600"
        letter-spacing="3"
    >
        SOFTWARE ENGINEER
    </text>


    <!-- NAME -->

    <text
        x="75"
        y="176"
        fill="{config['white']}"
        font-family="Inter, Segoe UI, Arial, sans-serif"
        font-size="57"
        font-weight="900"
        letter-spacing="1"
    >
        {name}
    </text>


    <!-- Accent line -->

    <rect
        x="78"
        y="193"
        width="250"
        height="2"
        rx="1"
        fill="url(#accentGradient)"
    />


    <!-- HEADLINE -->

    <text
        x="78"
        y="225"
        fill="{config['muted']}"
        font-family="Inter, Segoe UI, Arial, sans-serif"
        font-size="14"
        font-weight="500"
        letter-spacing="0.8"
    >
        {headline}
    </text>


    <!-- ========================================================
         TERMINAL
         ======================================================== -->

    <rect
        x="78"
        y="253"
        width="690"
        height="84"
        rx="10"
        fill="url(#terminalGradient)"
        stroke="{config['pink']}"
        stroke-opacity="0.14"
    />


    <!-- Terminal header -->

    <line
        x1="78"
        y1="280"
        x2="768"
        y2="280"
        stroke="{config['white']}"
        stroke-opacity="0.06"
    />


    <circle
        cx="96"
        cy="267"
        r="4"
        fill="#FF5F56"
    />

    <circle
        cx="111"
        cy="267"
        r="4"
        fill="#FFBD2E"
    />

    <circle
        cx="126"
        cy="267"
        r="4"
        fill="#27C93F"
    />


    <text
        x="150"
        y="271"
        fill="{config['dim']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="9"
        letter-spacing="1"
    >
        developer@poornasri:~
    </text>


    <!-- Terminal command -->

    <text
        x="103"
        y="307"
        fill="{config['cyan']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="13"
        font-weight="600"
    >

        &gt; stack:
        <tspan fill="{config['white']}">
            {stack}
        </tspan>

    </text>


    <!-- Cursor -->

    <rect
        x="570"
        y="294"
        width="7"
        height="16"
        fill="{config['pink']}"
    />

</g>


<!-- ============================================================
     RIGHT SYSTEM ARCHITECTURE
     ============================================================ -->

<g transform="translate(1030 215)">

    <!-- Central aura -->

    <circle
        cx="0"
        cy="0"
        r="150"
        fill="{config['cyan']}"
        opacity="0.025"
    />


    <!-- Outer orbital -->

    <circle
        cx="0"
        cy="0"
        r="132"
        fill="none"
        stroke="{config['cyan']}"
        stroke-opacity="0.10"
        stroke-width="1"
        stroke-dasharray="2 10"
    />


    <!-- Middle orbital -->

    <circle
        cx="0"
        cy="0"
        r="98"
        fill="none"
        stroke="{config['pink']}"
        stroke-opacity="0.20"
        stroke-width="1"
        stroke-dasharray="6 7"
    />


    <!-- Inner orbital -->

    <circle
        cx="0"
        cy="0"
        r="58"
        fill="none"
        stroke="{config['purple']}"
        stroke-opacity="0.20"
        stroke-width="1"
    />


    <!-- Architecture lines -->

    <g
        stroke="{config['cyan']}"
        stroke-opacity="0.12"
        stroke-width="1"
    >

        <line x1="-132" y1="0" x2="-50" y2="0"/>
        <line x1="50" y1="0" x2="132" y2="0"/>

        <line x1="0" y1="-132" x2="0" y2="-50"/>
        <line x1="0" y1="50" x2="0" y2="132"/>

        <line x1="-92" y1="-92" x2="-35" y2="-35"/>
        <line x1="35" y1="35" x2="92" y2="92"/>

    </g>


    <!-- Data nodes -->

    <circle
        cx="98"
        cy="0"
        r="5"
        fill="{config['cyan']}"
        filter="url(#glowSoft)"
    />

    <circle
        cx="-98"
        cy="0"
        r="4"
        fill="{config['hot_pink']}"
        filter="url(#glowPink)"
    />

    <circle
        cx="0"
        cy="-132"
        r="4"
        fill="{config['blue']}"
        filter="url(#glowSoft)"
    />


    <!-- Core -->

    <circle
        cx="0"
        cy="0"
        r="26"
        fill="#0B111A"
        stroke="{config['pink']}"
        stroke-opacity="0.25"
    />


    <circle
        cx="0"
        cy="0"
        r="9"
        fill="{config['pink']}"
        filter="url(#glowPink)"
    />


    <!-- Core rings -->

    <circle
        cx="0"
        cy="0"
        r="38"
        fill="none"
        stroke="{config['pink']}"
        stroke-opacity="0.15"
    />

</g>


<!-- ============================================================
     LOWER INFORMATION BAR
     ============================================================ -->

<g>

    <line
        x1="78"
        y1="360"
        x2="1202"
        y2="360"
        stroke="{config['white']}"
        stroke-opacity="0.06"
    />


    <!-- Status -->

    <circle
        cx="84"
        cy="383"
        r="3"
        fill="{config['green']}"
        filter="url(#glowSoft)"
    />


    <text
        x="97"
        y="387"
        fill="{config['muted']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="10"
        letter-spacing="1.2"
    >
        STATUS:
    </text>


    <text
        x="150"
        y="387"
        fill="{config['green']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="10"
        font-weight="600"
        letter-spacing="1.2"
    >
        {status}
    </text>


    <!-- Location -->

    <text
        x="490"
        y="387"
        fill="{config['dim']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="10"
        letter-spacing="1"
    >
        LOCATION
    </text>


    <text
        x="555"
        y="387"
        fill="{config['muted']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="10"
        letter-spacing="1"
    >
        {location}
    </text>


    <!-- Right-side system metric -->

    <text
        x="1050"
        y="387"
        fill="{config['dim']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="9"
        letter-spacing="1"
    >
        BUILD
    </text>


    <text
        x="1098"
        y="387"
        fill="{config['pink']}"
        font-family="JetBrains Mono, Fira Code, monospace"
        font-size="9"
        letter-spacing="1"
    >
        ACTIVE
    </text>

</g>


<!-- ============================================================
     CORNER DETAILS
     ============================================================ -->

<path
    d="M24 65V42C24 32 32 24 42 24H65"
    stroke="{config['pink']}"
    stroke-opacity="0.35"
    stroke-width="1"
/>


<path
    d="M1215 406H1238C1248 406 1256 398 1256 388V365"
    stroke="{config['purple']}"
    stroke-opacity="0.30"
    stroke-width="1"
/>

</svg>
"""

    # ============================================================
    # WRITE FILE
    # ============================================================

    os.makedirs("assets", exist_ok=True)

    output_path = os.path.join("assets", "banner.svg")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(svg)

    print(f"Static banner generated: {output_path}")

    return output_path


if __name__ == "__main__":
    create_animated_banner()