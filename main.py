"""Entry for news-image-20261118: place the bundled picture at the output.

The bundled picture (entry.png, 1024 by 1024, 1,017,448 bytes) is a
front-page collage of Wednesday 18 November 2026: the tanker war in the
Gulf, the Kerch Bridge hit for a second night, the COP31 climate talks
in Antalya, and the Quad meeting in Manila. This program only copies
those exact bytes to the output path. It uses no network and no
randomness, so every run produces the same file.
"""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
IMAGE = ROOT / "entry.png"


def run() -> int:
    # A plain copy keeps the PNG whole, header to end marker.
    target_dir = Path(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, target_dir / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
