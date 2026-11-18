# news-image-20261118 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261118 ($250, 50 places). Deadline 20 Nov 2026 00:00 UTC.
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image (v4 — resubmit, rank push)
- v3 ranked **114/3,574 (win rate 98.2873%)**; the prize cutoff (rank 50) is now 98.5483% (ethan-cole) — v4 must gain +0.26 points. The user first asked "why not 60 stories", then settled on **50 first** (60 risks unreadable text; if v4 still misses Top 50, the next round goes to 60). Rank 1 (calm-badger-15, 98.9981%, 35 stories) and the new rank 50 (ethan-cole, 98.5483%, 32 stories) were studied side by side with v3; the v3 builder's hypothesis was that panel scene art, not story count, separates 98.5% from 99.0%.
- `entry.png`: 1024×1024 PNG, 180,073 bytes (≤1 MiB). Drawn programmatically with PIL by `../news-image-20261117/draw_v4.py` (reuses draw_v2's land mask and icons; DejaVu fonts) — every headline is typeset, nothing is AI-generated, so no garbled text.
- Dense front page, **50 stories** (more than either rival's 35/32): dark navy masthead with gold kicker ("50 STORIES · 6 CONTINENTS · ONE PAGE"), three RICH night/dusk panels (Bahrain night: jets + radar dome + moon + blast glow; Kerch dusk: broken arch + big explosion + smoke; Manila sunset: orange-purple sky, sun, skyline with lit windows, four flags), three featured stories with 3-line decks, eleven featured stories with visuals, a "BY THE NUMBERS" strip (66–52, $115.8bn, 145 km/h, 200,000), a dotted world map with all-red numbered pins 1–11 (no legend, rank-1 style), and an "ALSO ON WEDNESDAY 18 NOVEMBER — 39 MORE STORIES" list.
- Fixes vs v3: (a) all three panels redrawn as rich night/dusk scenes with gradients, stars, glows, smoke and silhouettes; (b) featured decks grown to 3 lines with one more factual clause each; (c) every ALSO item rewritten short enough to fit its column whole — the generator now FAILS LOUDLY if any item would need an ellipsis (v3 had 11 truncated items); (d) map pins all red r=9, legend removed; (e) 12 new briefs (items 39–50: Pope Leo, Ebola, Zelensky peace plan, MINURSO pull-out, Google geothermal, Spain polls, Dow −849, APEC opening, US chip block, India GDP, Sudan UN complaint, BNP leader killed) taken from the rank-1 / rank-50 front pages for the same day — nothing invented.
- All text viewed directly after generation: legible, spelled correctly, all 50 items present and numbered, nothing overflows the margins, no truncated list items.

## Verification
- Program run twice: byte-identical output, sha256 `c3849fca38a49f8ddcf7c1441ab225f76217fd49fc871670ec6358667daa512b`.
- Output: 1024×1024, 180,073 bytes.
- Local check (v4 files, v3 transcripts bundle): 12 passed, 1 failed, 5 skipped, 5 checked at submission. The 1 failure is thinking_reproduces (33/75 lines unwritten, 44.0%) — expected with the v3 bundle, because the v4 edits to main.py (5 lines) and BUILD_NOTES.md (9 lines) exist only in the v4 session. With the v4 session bundled, only README.md's 19 lines stay unwritten (written via browser upload, never in a session — same as v3) = 19/75 = 25.3% unwritten, inside the 40% allowance. Parent re-bundles with the v4 session before submitting.

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
