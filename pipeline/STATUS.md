# Digest pipeline — status

- **Stage:** ✅ Wave 3 done — 373/375 accepted (2 needs_human) · **waiting for `reviews/wave-3.md`**
- **Mode:** pause
- **Spent:** $227 of $325 cap (wave 3 $107.16)
- **⚠ Remaining core ≈ $105–116 → ≈ $332–342 total, over the $325 cap**

### wave3 measured (prompts v2.2)
- Units: 375 (373 accepted) · text pages 2901 · image pages 2532
- Cost: all-in $107.16 (first pass P1+P2 $102.10; retries/fixes +5%)
- **Per page (all-in, least squares): text $0.0151 · image $0.0211**
- Length vs target (accepted): median 1.34× · 10–90%: 0.87–1.82× · > 1.5×: 137/373
- Verifier issues (375 units): critical 1655 · major 1289 · minor 2005 — by check: faithfulness 880 (163c/191M) · math 79 (7c/17M) · pages 140 (0c/23M) · coverage 131 (0c/28M) · numbers 79 (13c/3M) · labels 48 (0c/5M) · format/level 446 (0c/210M) · strength/voice 3144 (1471c/811M)
- h_checks: 22061 items checked, 5532 not ok (25.1%)
- **Re-forecast (remaining units, all-in rates):** core 338 units $116 · deep 145 units $44 · reference 162 units $71
- Total remaining ≈ $231 + spent $227 = **$457** vs $325 cap
- **Core + deep: spent $227 + $160 = $387** ❌ **EXCEEDS** the $325 cap · core only: $342

**⚠ Remaining core (wave 4: 336 units + 2 needs_human) ≈ $105–116** (wave-2 vs wave-3 rates) → total ≈ **$332–342, over the $325 cap**. At the cap the runner stops with ≈ 25–50 core units left; per the wave-2 review they join the Claude Code route. Deep + reference are already planned for that route.
- Per-page cost keeps rising (text $0.0118 → 0.0136 → 0.0151; image $0.0156 → 0.0194 → 0.0211): wave 3 was philosophy-heavy (120 mandatory items, ~50k verifier thinking on spread scans).
- Length: median 1.34× target, 137/373 > 1.5× — the explicit length budget has not brought lengths down yet.
- needs_human (2): meadows-2008-thinking/ch02-note (checks fail after 2 loops: L2 without page refs), popper-1959-logic/front-preface-2 (fix pass did not clear the checks).

### Engineering fixes during wave 3
- Batch rows of 22–26 MB (Dennett spreads, P2 at 1500 px) came back empty → P2 falls back to 1200 / 1000 px when images exceed 14 MB.
- Verifier hit 64k output on spread scans (~50k thinking) → P2 max_tokens 128k; a truncated verifier output now reruns P2 instead of re-digesting.
- False alarms fixed: leak phrases match whole words ("as an air-conditioner"); planner drops implausible printed ranges (23 bogus labels, e.g. "1-10" for 20-page arXiv papers).
- One Google-side "Failed to import data" job failure; re-submitted automatically.

### Claude Code route
- Built, not run: `python -m pipeline cc-run`; launchd job in `pipeline/launchd/` (not installed). **Waiting for Kunhao to start the Gate CC parity test.**
- GCP budget alert: ¥53,000.
