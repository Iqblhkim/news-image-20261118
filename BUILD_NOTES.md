# news-image-20261118 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261118 ($250, 50 places). Deadline 20 Nov 2026 00:00 UTC.
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image (v3 — resubmit, rank push)
- v2 ranked **131/3,354 (win rate 98.1243%)**; the prize cutoff (rank 50) is 98.5330% — v3 must gain +0.41 points. Rank 1 (calm-badger-15, 98.9981%, 35 stories) and rank 50 (cosmodnx, 98.5330%, 35 stories) were studied side by side with v2; v3 combines their winning devices and adds more.
- `entry.png`: 1024×1024 PNG, 161,740 bytes (≤1 MiB). Drawn programmatically with PIL by `../news-image-20261117/draw_v3.py` (reuses draw_v2's land mask, icons and panel art; DejaVu fonts) — every headline is typeset, nothing is AI-generated, so no garbled text.
- Dense front page, **38 stories** (more than either rival's 35): dark navy masthead with gold kicker ("38 STORIES · 6 CONTINENTS · ONE PAGE"), three captioned illustrated panels (Gulf tanker, Kerch Bridge hit, US/India/Japan/Australia Quad flags), eleven featured stories with visuals (the top 3 plus 8 illustrated tiles: Nvidia revenue, Cyclone Akvan, Knesset elects Kahana, EU €45bn loan, Britain sanctions, China tariff cuts, Dhoni ends IPL career, Russian plane crash in Siberia), a "BY THE NUMBERS" strip (66–52, $115.8bn, 145 km/h, 200,000), a dotted world map with numbered pins 1–11, and an "ALSO ON WEDNESDAY 18 NOVEMBER — 27 MORE STORIES" list.
- Fixes vs the first v3 render: featured decks no longer overlap the medium tiles (tighter leading, rule moved down); every ALSO item now uses the "Place: rest" form so the truncation logic applies (items without ": " used to overflow the right margin — caught by viewing the render).
- All text viewed directly after generation: legible, spelled correctly, all 38 items present and numbered, nothing overflows the margins.

## Verification
- Program run twice: byte-identical output, sha256 `67940aba6e6d4248ec64e1a22ecbaf4f8f7c4e33afe37337340849faf38eb1c1`.
- Output: 1024×1024, 161,740 bytes.
- Local check (v3 files, v2 transcripts bundle): 12 passed, 1 failed, 5 skipped, 5 checked at submission. The 1 failure is thinking_reproduces (34/65 lines unwritten, 52.3%) — expected with the v2 bundle, because the v3 edits to main.py (6 lines) and BUILD_NOTES.md (9 lines) exist only in the v3 session, which is not in that bundle. With the v3 session bundled, only README.md's 19 lines stay unwritten (written via browser upload, never in a session — same as v2) = 19/65 = 29.2% unwritten, inside the 40% allowance. Parent re-bundles with the v3 session before submitting.

## Image (v2 — resubmit)
- v1 was not yet on the leaderboard when checked; the 17 Nov sister entry ranked 3,835/3,903 (judge win rate 88.7%) with the same 4-story style, while the winners show 30–43 stories. v2 rebuilds the image in the winners' style.
- `entry.png`: 1024×1024 PNG, 145,226 bytes (≤1 MiB). Drawn programmatically with PIL by `../news-image-20261117/draw_v2.py` (DejaVu fonts, flat vector panels, dotted world map from a hand-coded land mask) — every headline is typeset, nothing is AI-generated, so no garbled text.
- Dense front page, 33 stories: masthead "Wednesday 18 November 2026", three illustrated panels (Gulf tanker, Kerch Bridge hit, US/India/Japan/Australia Quad flags), three featured stories (US and Iran trade fire over Bahrain; Ukraine drops a span of the Crimea bridge; Trump in Manila for first Quad in two years), six medium stories with icons (Nvidia revenue, Cyclone Akvan, Knesset elects Kahana, EU €45bn loan, Britain sanctions, China tariff cuts), a dotted world map with numbered pins, and an "ALSO ON WEDNESDAY 18 NOVEMBER — 24 MORE STORIES" list.
- All text viewed directly after generation: legible, spelled correctly, no truncated list items.

## Verification
- Program run twice: byte-identical output, sha256 `9defa5c69a59d2ebeade1b4beaa6f7a5303ff9d428f3d391c41034ff396a362e`.
- Output: 1024×1024, 145,226 bytes.
- Local check (v2 files, v1 transcripts bundle): 13 passed, 0 failed, 5 skipped (thinking_reproduces 65.5%). Parent re-bundles with the v2 session before submitting.
