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

</svg>"""




def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    svg = build_svg()

    OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print("✅ SVG Generated Successfully!")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()