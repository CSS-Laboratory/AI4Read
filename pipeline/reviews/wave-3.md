# Wave 3 review — quality lead (2026-10-14)

**Verdict: accepted.** Quality is stable or slightly better; cost and length are the issues now.

## Audit (10 units ≈ 2.7%; reports `pipeline/reviews/audit/wave3-*.md`)
| Unit | Crit | Major | Minor |
|---|---|---|---|
| MacKay ch. 4 | 1 | 3 | 5 |
| Shannon 1948 p1 | 0 | 2 | 7 |
| Frank & Goodman 2012 | 0 | 2 | 6 |
| Hernán & Robins ch. 7 | 1 | 1 | 5 |
| Magnus forall x ch. 22 | 0 | 0 | 6 |
| Popper ch. 4 | 1 | 3 | 9 |
| Lycan ch. 13 | 0 | 4 | 8 |
| Kahneman ch. 26 | 0 | 0 | 10 |
| Keynes ch. 12 | 0 | 5 | 11 |
| Ashby ch. 10 | 0 | 3 | 6 |

≈ 0.3 critical per unit (down from ≈ 0.5), every equation / toy example / added step correct. All criticals are dropped conditions in short summary lines or the toy example. All critical + major errors fixed by hand (84 fixes; `audit/wave3-fixes.md`).

## Length → cost
Median length is **1.34× target** and every audited digest was 1.45–1.85×. The model treats the target as a floor. Since P1 output is the largest cost driver, **recalibrate the target for wave 4**: `target = min(max(1000, 0.30·sw), 0.70·sw)`, 0.42 for image-heavy units (instead of 0.40 / 0.55). Expected result: actual lengths near the originally intended 0.40 / 0.55, and ≈ 8–12% lower cost. No re-digests for length.

## needs_human (2)
- `meadows-2008-thinking/ch02-note` and `popper-1959-logic/front-preface-2`: accept the best version with `verified: needs-review` in frontmatter; they go to the Claude Code route's first run for a re-check. Don't spend more Vertex money on them.

## Budget decision for wave 4 (Kunhao)
Spent $227; remaining core ≈ $105–116 at wave-3 rates, ≈ $95–105 with the new length target → total ≈ $322–332 vs the $325 cap. Either:
- **(a) keep $325**: the runner stops at the cap; the last ≈ 10–30 core units join the Claude Code route; or
- **(b) raise to $340** to finish core on Vertex.
Kunhao decides; set `control.json` accordingly.
