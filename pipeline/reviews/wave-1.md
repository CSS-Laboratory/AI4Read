# Wave 1 review — quality lead (2026-10-14)

**Verdict: accepted. Continue with prompts v2.2 and the engineering changes below.**

## Audit (12 units, one per work, ≈ 11%; Opus against page images)
Reports: `pipeline/reviews/audit/wave1-{argumentative,math,social}.md`.

| Unit | Crit | Major | Minor |
|---|---|---|---|
| Gettier 1963 | 0 | 0 | 3 |
| Godfrey-Smith ch. 5 | 1 | 2 | 6 |
| Carey ch. 1 | 0 | 4 | 10 |
| Apperly & Butterfill p1 | 2 | 1 | 8 |
| Axler ch. 5 p1 | 0 | 0 | 5 |
| Cover ch. 8 p1 | 0 | 1 | 5 |
| Blei 2017 p1 | 0 | 1 | 3 |
| Ashby ch. 11 | 2 | 2 | 2 |
| Achen & Bartels ch. 4 | 1 | 3 | 11 |
| Axelrod ch. 2 | 0 | 1 | 8 |
| Argyle 2023 p1 | 0 | 1 | 6 |
| Anderson 1972 | 0 | 3 | 7 |

- **Math, numbers, tables, toy examples: essentially perfect** (hundreds of checks; every toy example and added step recomputed).
- **Residual errors ≈ 0.5 critical per unit**, almost all of one kind: **hedges, comparatives and voice in summary lines and index lines** (L1/L2, Concepts, Instances): necessary↔sufficient flip, "more X than Y" → "X, not Y", a commentator's complaint reported as the author's view, dropped "±" and dropped conditions in worked examples.
- Other: "partly legible" equations that were legible (Cover), `(pdf N)` in papers without page labels (Anderson), spread scans cited a page off (Ashby), quote overuse (Carey: 153 quotes), short papers longer than the source (Gettier 1.8×).
- All critical/major errors in the 12 audited digests were **fixed by hand** against the page images (93 fixes; `audit/wave1-fixes.md`; frontmatter `audited: 2026-10-14`). Do not overwrite these files.

## Prompts v2.2 (pushed)
- `verify.md`: mandatory items now include **every L0–L2 sentence**, every intuition note, **every Concepts/Instances line**, L3 sentences with logical words (incl. necessary, sufficient, unless, alone, merely, condition) and worked-example conditions, voice sentences in argumentative texts, and every Reading-notes sentence. New H5 "hedge survival" (incl. comparative → exclusive). B: re-check symbols (±, minus, subscripts) in the image; "unreadable/partly legible" claims must be verified in the image.
- `digest.md`: comparatives and hedges also in Concepts/Instances; necessary ≠ sufficient; look at the image before calling anything unreadable; at most 10 quotes.

## Engineering requests (before wave 2)
1. **Mandatory items v2.2**: build the list as above. Priority order when over the cap: L0–L2 sentences → Concepts/Instances lines → intuition notes → strength/condition sentences in L3 → Reading notes → voice sentences. **Cap 120.** Label kinds.
2. **Length target**: `target = min(max(1200, 0.40·sw), 0.80·sw)` (0.55 instead of 0.40 for image-heavy units); keep "warn" above 1.5×.
3. **Quote budget check**: count quoted spans (≥ 4 words inside quotation marks); > 10 → add one mandatory item "Reduce quotations to ≤ 10; paraphrase the rest" for the verifier.
4. **Printed pages**: backfill `printed_pages` for every `kind=paper` row (footer/header detection); **split two-page spread scans into half-images with their own printed labels** for all remaining spread scans (Ashby: re-check the remaining units if they were not split).
5. Your wave-1 change "L1 121–138 words = warning" is **accepted**.

## Policy note (added to CHARTER)
Digests are verified maps, not guaranteed truth: residual risk ≈ 0.5 subtle error per unit (hedges/voice). Every claim used in a post is re-checked against the source page at post-writing time.

## Scope, budget, waves
- Kunhao: core + deep may go **≈ $5 over** $300 → hard stop now **$305** (`control.json`). Reference tier: decide after core + deep (extra budget, or Claude Code's own Sonnet agents).
- **Wave 2 onward:** larger waves are fine — ~200–250 core units per wave, core first, then deep. Keep `review_each_wave: true`; I will audit ~5% per wave (stratified).
- The 11 pilot units are redone with v2.2 in their natural waves.
- v2.2 will add some verifier thinking; report the measured cost per page after wave 2 and re-forecast core + deep. If the forecast exceeds $305, finish core first and stop; the rest of deep can go to the Claude Code route.
