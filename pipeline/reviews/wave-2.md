# Wave 2 review — quality lead (2026-10-14)

**Verdict: accepted. Finish the core tier on Vertex (cap raised to $325). Deep + reference move to the Claude Code route (`pipeline/CLAUDE_CODE_ROUTE.md`).**

## Audit (13 units ≈ 5.8%; reports `pipeline/reviews/audit/wave2-*.md`)
| Unit | Crit | Major | Minor |
|---|---|---|---|
| Cover ch. 2 (re-run) | 0 | 1 | 3 |
| Wittgenstein §§243–315 (re-run) | 0 | 1 | 6 |
| Jaynes ch. 2 (re-run) | 0 | 1 | 3 |
| Dennett ch. 2 (re-run) | 0 | 1 | 2 |
| Kripke Lecture II | 0 | 4 | 6 |
| Kuhn ch. IX | 0 | 5 | 7 |
| Habermas ch. V | 1 | 2 | 12 |
| Grice 1975 (scan) | 1 | 2 | 8 |
| Clark et al. ch. 12 p1 | 1 | 1 | 9 |
| Gelman BDA3 ch. 5 | 0 | 2 | 6 |
| Åström & Murray ch. 7 | 0 | 2 | 3 |
| Bellman ch. III (scan) | 1 | 1 | 4 |
| Kalman 1960 | 3 | 2 | 3 |

- **Regression:** 14 of the 15 critical/major errors from the first audit are gone (all 4 criticals). v2.2 works.
- **Residual:** ≈ 0.5 critical per unit (Kalman is the outlier; without it ≈ 0.33), ≈ 1.8 major per unit — mostly dropped hedges in L0–L2 and undefined terms. Math remains near-perfect. This is the plateau for this prompt family; further tightening costs more than it saves. The post-writing check (CHARTER §9) is the final safeguard.
- All critical/major errors in the 13 audited digests were **fixed by hand** (99 fixes; `audit/wave2-fixes.md`). Do not overwrite files with `audited:` in frontmatter.

## Changes
- `digest.md`: length budget made explicit (L0–L2 ≈ 15%, L3 ≈ 60%, rest ≈ 25%; > 1.3× target is too long). Overshoots seen: Wittgenstein 2.1×, Grice 1.75×, Kuhn 1.6×. Keep the 1.5× warning; no re-digest for length alone.
- Your wave-2 engineering fixes are accepted.

## Budget and scope (Kunhao, 2026-10-14)
- **Cap raised to $325** (`control.json`) to finish the **core tier** on Vertex. Please also raise the GCP budget alert to ≈ ¥53,000 (with approval).
- **Re-run the 12 non-audited Ashby units** with spread splitting (≈ $3) as part of the next wave.
- **Deep + reference tiers → Claude Code route**: build per `pipeline/CLAUDE_CODE_ROUTE.md` after the core tier is done; parity test (Gate CC) before the first Thursday run.

## Waves 3+
Remaining core ≈ 699 units. Run as **two waves of ≈ 350**. Keep `review_each_wave: true`; I will audit ≈ 3% per wave. If the measured spend projects beyond $325, stop at the cap and report the leftover core units — they join the Claude Code route.
