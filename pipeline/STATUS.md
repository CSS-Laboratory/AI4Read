# Digest pipeline — status

- **Stage:** ✅ Wave 4 done — **core tier complete (1,031 units)** · waiting for `reviews/wave-4.md`
- **Mode:** pause
- **Spent:** **$322.95** of $340 cap (wave 4 $96.09)
- **Next:** quality-lead review → Gate CC parity test → deep + reference on the Claude Code route

### wave4 measured (prompts v2.2)
- Units: 336 (336 accepted) · text pages 4274 · image pages 2410
- Cost: all-in $96.09 (first pass P1+P2 $92.61; retries/fixes +4%)
- **Per page (all-in, least squares): text $0.0121 · image $0.0153**
- Length vs target (accepted): median 1.40× · 10–90%: 0.93–2.12× · > 1.5×: 140/336
- Verifier issues (336 units): critical 1771 · major 1140 · minor 1750 — by check: faithfulness 789 (155c/162M) · math 58 (11c/9M) · pages 165 (0c/34M) · coverage 128 (0c/29M) · numbers 71 (16c/4M) · labels 38 (2c/2M) · format/level 385 (0c/182M) · strength/voice 3027 (1587c/718M)
- h_checks: 20445 items checked, 5668 not ok (27.7%)
- **Re-forecast (remaining units, all-in rates):** core 0 units $0 · deep 145 units $33 · reference 162 units $52

### ✅ Core tier complete on Vertex
- **1,031 / 1,031 core units accepted** (1,029 verified, 2 `needs-review` → re-checked first in the Claude Code route, `pipeline/waves/cc_recheck.txt`).
- **Total Vertex spend: $322.95** of the $340 cap (waves 1–4: $31.13 · $88.50 · $107.16 · $96.09; pilot, gates and tests ≈ $10).
- Length with the recalibrated target: digests are **0.46× the source** (wave 3: 0.61×); vs the old target the median fell from 1.35× to **1.07×** — the model still overshoots its stated target (median 1.40× of the new one, 140/336 above 1.5×), but the actual length is now close to the originally intended 0.40/0.55.
- Per-page cost fell with the shorter digests: text $0.0151 → **$0.0121**, image $0.0211 → **$0.0153**.
- Verifier quality signal is unchanged: ≈ 5 critical findings fixed per unit, mostly strength/voice (H); 27.7% of h_checks needed a fix.

### Next
- **Deep (145) + reference (162) → Claude Code route** (`python -m pipeline cc-run`, built, not run). At Vertex rates they would cost ≈ $85 — not affordable under the cap.
- **Gate CC parity test waits for the quality lead's wave-4 review** (`pipeline/reviews/wave-4.md`).
