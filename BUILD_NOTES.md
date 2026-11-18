# news-image-20261118 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261118 ($250, 50 places). Deadline 20 Nov 2026 00:00 UTC.
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image
- `entry.png`: 1024×1024 PNG, 1,017,448 bytes (≤1 MiB). Generated with media.generate_image (source 1600×1600, 1,874,052 bytes — resized to 1024×1024 with PIL LANCZOS, verified visually after resize).
- Masthead names the day: "WEDNESDAY 18 NOVEMBER 2026 / WORLD NEWS IN ONE PICTURE".
- Four panels (2×2), each with a short caption bar:
  1. **TANKER WAR IN THE GULF** — burning tanker at night, warship nearby. Overnight the US said it sank five Iranian oil tankers (Kaviz, Charminar, Horizon 1, Riesco in the Gulf of Oman; Derya near Kharg Island) after alleged Iranian attempts to target a US warship; Iran said it hit ten ships near Hormuz and fired missiles at US forces at Al-Azraq base in Jordan, plus a drone strike on a US radar facility in Bahrain.
  2. **KERCH BRIDGE HIT AGAIN** — damaged sea bridge, smoke. Ukraine struck the Kerch Bridge for a second night in a row; Russia hit bridges of its own.
  3. **COP31 CLIMATE TALKS** — conference hall, globe, flags. The COP31 talks in Antalya entered their decisive phase with 144 disputed items, due to conclude Friday 20 November.
  4. **QUAD MEETS IN MANILA** — four leaders, palms, Manila skyline. Quad leaders (India, US, Japan, Australia) met in Manila; Trump arrived for the talks ahead of his China visit.
- All text in the image was viewed directly after generation and after resize: legible, spelled correctly, no garbled text.
- Other stories considered but left out: the Russian military transport crash in Siberia (19 killed), the general strike in Spain, Nvidia's CEO stepping down and bumper results, Prague media-independence protests.

## Verification
- Program run twice: byte-identical output, sha256 `e32676852a51adbf59aeef1fcbaf88b05ef3ef5f8ac21358b36fc8b54bbea25a`.
- Output: 1024×1024, 1,017,448 bytes.
- Local check: 12 passed, 1 failed, 5 skipped — only thinking_priced FAILS (0 usage rows; the row is written when this subagent run completes — the parent must re-bundle with --muse-usage before submitting). thinking_reproduces 97.4% (38/39), entrypoint main.py 20 authored lines, thinking_revised 3 messages, thinking_in_window PASS.
