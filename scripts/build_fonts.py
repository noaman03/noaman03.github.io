"""Build the self-hosted web font.

Downloads the Archivo variable font from the Google Fonts repository, narrows its
axes to the range the site actually uses, subsets it to Latin plus the punctuation
that appears on the pages, and writes a single WOFF2 to public/fonts/.

Archivo (Omnibus-Type, SIL Open Font License 1.1) was drawn for highlights and
signage -- type meant to be read from further away than a book. That is the
subject of this site, so it is the one family used, at two widths: the expanded
cut carries the display lines, the normal cut carries everything else.

Run it only when the font needs rebuilding; the output is committed.

    python scripts/build_fonts.py

Requires fonttools and brotli, which are development-only tools and are not part
of the site's runtime or of npm:

    python -m pip install fonttools brotli
"""

from __future__ import annotations

import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "public" / "fonts"
BUILD_DIR = ROOT / "tmp" / "fonts"

SOURCE_URL = (
    "https://github.com/google/fonts/raw/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf"
)
LICENSE_URL = "https://github.com/google/fonts/raw/main/ofl/archivo/OFL.txt"

# Weight 400-700 covers body through display; width 100-125 covers text through
# the expanded display cut. Narrowing both axes is most of the size saving.
AXES = ["wght=400:700", "wdth=100:125"]

# Latin-1, general punctuation (dashes, curly quotes, ellipsis), the euro, the
# trademark sign and the true minus. Everything the ten pages actually render.
UNICODES = "U+0000-00FF,U+2010-2027,U+2030-205E,U+20AC,U+2122,U+2212"

# kern and liga for text quality; calt for Archivo's contextual alternates; tnum
# so the figure columns in the project tables line up.
LAYOUT_FEATURES = "kern,liga,calt,tnum"

OUTPUT = FONT_DIR / "archivo-var.woff2"
BUDGET_BYTES = 120 * 1024


def fetch(url: str, target: Path) -> None:
    if target.exists():
        print(f"  have {target.name} ({target.stat().st_size:,} bytes)")
        return
    print(f"  fetching {target.name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, target.open("wb") as handle:
        handle.write(response.read())
    print(f"  wrote {target.name} ({target.stat().st_size:,} bytes)")


def run(module: str, *args: str) -> None:
    subprocess.run([sys.executable, "-m", module, *args], check=True)


def main() -> int:
    try:
        import fontTools  # noqa: F401
    except ImportError:
        print(
            "fonttools is not installed. Run: python -m pip install fonttools brotli",
            file=sys.stderr,
        )
        return 1

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    FONT_DIR.mkdir(parents=True, exist_ok=True)

    source = BUILD_DIR / "Archivo-source.ttf"
    instanced = BUILD_DIR / "Archivo-instanced.ttf"

    print("Archivo")
    fetch(SOURCE_URL, source)
    fetch(LICENSE_URL, FONT_DIR / "Archivo-OFL.txt")

    print(f"  instancing {' '.join(AXES)}")
    run("fontTools.varLib.instancer", str(source), *AXES, "-o", str(instanced))
    print(f"  instanced ({instanced.stat().st_size:,} bytes)")

    print("  subsetting to Latin + punctuation")
    run(
        "fontTools.subset",
        str(instanced),
        f"--unicodes={UNICODES}",
        f"--layout-features={LAYOUT_FEATURES}",
        "--flavor=woff2",
        f"--output-file={OUTPUT}",
    )

    size = OUTPUT.stat().st_size
    print(f"\n  {OUTPUT.relative_to(ROOT)}  {size:,} bytes")
    if size > BUDGET_BYTES:
        print(
            f"  OVER BUDGET: {size:,} > {BUDGET_BYTES:,}. Narrow the axes or the subset.",
            file=sys.stderr,
        )
        return 1
    print(f"  within the {BUDGET_BYTES // 1024} KB budget.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
