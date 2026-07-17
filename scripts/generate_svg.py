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

            <!-- Main Content -->
    <rect
        x="430"
        y="120"
        width="1110"
        height="980"
        rx="12"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="1.5"/>

        <!-- Greeting -->
    <text
        x="470"
        y="170"
        fill="#8b949e"
        font-size="28"
        font-family="JetBrains Mono, Consolas, monospace">

        Hi there! 👋 I'm

    </text>

    <!-- Name -->
    <text
        x="470"
        y="245"
        fill="#f0f6fc"
        font-size="72"
        font-weight="700"
        font-family="JetBrains Mono, Consolas, monospace">

        RITIK

    </text>

    <text
        x="760"
        y="245"
        fill="#3fb950"
        font-size="72"
        font-weight="700"
        font-family="JetBrains Mono, Consolas, monospace">

        SINGH

    </text>

    <!-- Subtitle -->
    <text
        x="470"
        y="295"
        fill="#c9d1d9"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        Full Stack Ai Engineer • AI/ML

    </text>

    <!-- Command Box -->
    <rect
        x="470"
        y="330"
        width="650"
        height="70"
        rx="10"
        fill="#0d1117"
        stroke="#58a6ff"
        stroke-width="1.5"/>

    <!-- Prompt -->
    <text
        x="495"
        y="375"
        fill="#3fb950"
        font-size="28"
        font-family="JetBrains Mono, Consolas, monospace">

        $

    </text>

    <!-- Command -->
    <text
        x="525"
        y="375"
        fill="#f0f6fc"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        Building scalable web apps and AI powered tools

    </text>


    <!-- Cursor -->
    <rect
        x="1075"
        y="350"
        width="8"
        height="30"
        fill="#3fb950"/>
 <!-- Quick Stats -->

    <!-- Row 1 -->
    <text
        x="470"
        y="455"
        fill="#f0f6fc"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        🚀 50+ Projects

    </text>

    <text
        x="760"
        y="455"
        fill="#f0f6fc"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        ⭐ 230+ Contributions

    </text>

    <!-- Row 2 -->
    <text
        x="470"
        y="500"
        fill="#f0f6fc"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        🏆 10+ Achievements

    </text>

    <text
        x="760"
        y="500"
        fill="#f0f6fc"
        font-size="26"
        font-family="JetBrains Mono, Consolas, monospace">

        👥 100+ Followers

    </text>

      <!-- Current Focus Heading -->
    <text
        x="470"
        y="570"
        fill="#3fb950"
        font-size="28"
        font-weight="700"
        font-family="JetBrains Mono, Consolas, monospace">

        CURRENT FOCUS

    </text>

    <!-- Heading Line -->
    <line
        x1="710"
        y1="560"
        x2="1120"
        y2="560"
        stroke="#3fb950"
        stroke-width="1"
        opacity="0.4"/>

            <!-- Focus Item 1 -->
    <text
        x="470"
        y="620"
        fill="#c9d1d9"
        font-size="24"
        font-family="JetBrains Mono, Consolas, monospace">

        🤖 Building AI Apps

    </text>

    <!-- Focus Item 2 -->
    <text
        x="470"
        y="665"
        fill="#c9d1d9"
        font-size="24"
        font-family="JetBrains Mono, Consolas, monospace">

        💻 Creating full stack products that solve real problems

    </text>

    <!-- Focus Item 3 -->
    <text
        x="470"
        y="710"
        fill="#c9d1d9"
        font-size="24"
        font-family="JetBrains Mono, Consolas, monospace">

        📚 Learning Agentic AI &amp; Advanced System Design

    </text>

    <!-- Focus Item 4 -->
    <text
        x="470"
        y="755"
        fill="#c9d1d9"
        font-size="24"
        font-family="JetBrains Mono, Consolas, monospace">

        🌍 Contributing to Open Source

    </text>

</svg>"""




def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    svg = build_svg()

    OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print("✅ SVG Generated Successfully!")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()