from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = ROOT / "generated"
OUTPUT_FILE = OUTPUT_DIR / "dashboard.svg"


def build_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg"
    width="1600"
    height="1200"
    viewBox="0 0 1600 1200">

    <!-- Background -->
    <rect width="1600" height="1200" fill="#0d1117"/>

    <!-- Terminal Window -->
    <rect
        x="20"
        y="20"
        width="1560"
        height="1160"
        rx="16"
        fill="#0b0f14"
        stroke="#30363d"
        stroke-width="2"/>

          <!-- Terminal Header -->
    <rect
        x="20"
        y="20"
        width="1560"
        height="60"
        rx="16"
        fill="#161b22"/>

    <!-- Bottom Border -->
    <line
        x1="20"
        y1="80"
        x2="1580"
        y2="80"
        stroke="#30363d"
        stroke-width="2"/>

          <!-- Window Buttons -->
    <circle
        cx="45"
        cy="50"
        r="8"
        fill="#ff5f57"/>

    <circle
        cx="70"
        cy="50"
        r="8"
        fill="#febc2e"/>

    <circle
        cx="95"
        cy="50"
        r="8"
        fill="#28c840"/>

            <!-- Terminal Title -->
    <text
        x="130"
        y="56"
        fill="#8b949e"
        font-size="22"
        font-family="JetBrains Mono, Consolas, monospace">

        ~/ritiksingh » cat README.md

    </text>

     <!-- Last Updated -->
    <text
        x="1245"
        y="56"
        fill="#c9d1d9"
        font-size="20"
        font-family="JetBrains Mono, Consolas, monospace">

        Last updated: Jul 18, 2026

    </text>

    <!-- Online Dot -->
    <circle
        cx="1555"
        cy="49"
        r="7"
        fill="#3fb950"/>
        <!-- Header Accent Line -->
        
    <line
        x1="40"
        y1="95"
        x2="1560"
        y2="95"
        stroke="#58a6ff"
        stroke-width="1"
        opacity="0.35"/>

          <!-- Left Panel -->
    <rect
        x="40"
        y="120"
        width="360"
        height="980"
        rx="12"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="1.5"/>

</svg>"""




def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    svg = build_svg()

    OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print("✅ SVG Generated Successfully!")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()