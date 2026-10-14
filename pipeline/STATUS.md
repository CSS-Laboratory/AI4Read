# Digest pipeline — status

- **Stage:** ✅ Wave 2 done — 226/226 accepted · **waiting for `reviews/wave-2.md`**
- **Mode:** pause
- **Spent:** $124 of $305 cap (wave 2 $88.50)
- **⚠ Core + deep forecast ≈ $355 → over the $305 cap** (core alone ≈ $315)

### wave2 measured (prompts v2.2)
- Units: 226 (226 accepted) · text pages 2590 · image pages 2469
- Cost: all-in $88.50 (first pass P1+P2 $84.60; retries/fixes +5%)
- **Per page (all-in, least squares): text $0.0136 · image $0.0194**
- Length vs target (accepted): median 1.11× · 10–90%: 0.77–1.69× · > 1.5×: 37/226
- Verifier issues (226 units): critical 1162 · major 809 · minor 1227 — by check: faithfulness 607 (115c/136M) · math 60 (14c/11M) · pages 109 (2c/16M) · coverage 46 (0c/11M) · numbers 40 (7c/1M) · labels 36 (0c/1M) · format/level 277 (0c/150M) · strength/voice 2022 (1024c/482M)
- h_checks: 14880 items checked, 3879 not ok (26.1%)
- **Re-forecast (remaining units, all-in rates):** core 699 units $191 · deep 145 units $40 · reference 162 units $65
- Total remaining ≈ $297 + spent $124 = **$420** vs $305 cap
- **Core + deep: spent $124 + $232 = $355** ❌ **EXCEEDS** the $305 cap · core only: $315

**⚠ Budget: the forecast for core + deep (≈ $355) EXCEEDS the $305 cap by ≈ $50.** Even core alone (≈ $315) is ≈ $10 over: at current v2.2 rates the hard stop would leave ≈ 35 of the remaining 699 core units undone. Deep (145 units, ≈ $40) does not fit; per the wave-1 review it would go to the Claude Code route.
- Why: v2.2 costs ≈ +15% (text) / +24% (image) per page vs v2.1 — the verifier checks ≤ 120 mandatory items and thinks more.
- Decision needed (Kunhao / quality lead): raise the cap to ≈ $320 to finish core in the pipeline; or finish core until the stop and move the tail + deep to Claude Code; or lighten P2 for non-argumentative units.

### Notes
- Verifier is strict: ≈ 5 critical issues found and fixed per unit, mostly strength/voice (H); 26% of h_checks needed a fix. Accepted digests contain the fixes.
- Engineering fixes during wave 2: `{{`-leak false positive (LaTeX `y_{{\rm obs}}`) fixed before it caused re-digests; abbreviated page ranges ("1170–71") parsed correctly now.
- Ashby: its 13 units ran in wave 1 before spread splitting; 12 non-audited units still cite pages possibly a page off. Re-run ≈ $3 if wanted.
- PDF units without printed labels: 121 / 1,283 (ebooks without page numbers, text-less scans, preprints).
