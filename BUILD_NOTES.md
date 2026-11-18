# news-image-20261118 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261118 ($250, 50 places). Deadline 20 Nov 2026 00:00 UTC.
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image (v2 — resubmit)
- v1 was not yet on the leaderboard when checked; the 17 Nov sister entry ranked 3,835/3,903 (judge win rate 88.7%) with the same 4-story style, while the winners show 30–43 stories. v2 rebuilds the image in the winners' style.
- `entry.png`: 1024×1024 PNG, 145,226 bytes (≤1 MiB). Drawn programmatically with PIL by `../news-image-20261117/draw_v2.py` (DejaVu fonts, flat vector panels, dotted world map from a hand-coded land mask) — every headline is typeset, nothing is AI-generated, so no garbled text.
- Dense front page, 33 stories: masthead "Wednesday 18 November 2026", three illustrated panels (Gulf tanker, Kerch Bridge hit, US/India/Japan/Australia Quad flags), three featured stories (US and Iran trade fire over Bahrain; Ukraine drops a span of the Crimea bridge; Trump in Manila for first Quad in two years), six medium stories with icons (Nvidia revenue, Cyclone Akvan, Knesset elects Kahana, EU €45bn loan, Britain sanctions, China tariff cuts), a dotted world map with numbered pins, and an "ALSO ON WEDNESDAY 18 NOVEMBER — 24 MORE STORIES" list.
- All text viewed directly after generation: legible, spelled correctly, no truncated list items.

## Verification
- Program run twice: byte-identical output, sha256 `9defa5c69a59d2ebeade1b4beaa6f7a5303ff9d428f3d391c41034ff396a362e`.
- Output: 1024×1024, 145,226 bytes.
- Local check (v2 files, v1 transcripts bundle): 13 passed, 0 failed, 5 skipped (thinking_reproduces 65.5%). Parent re-bundles with the v2 session before submitting.
