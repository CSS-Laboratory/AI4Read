# Gate 2 — pilot wave report (2026-10-13)

**Result:** 11 / 11 units accepted. **Pilot cost $3.90.** **Projected full run ≈ $280–295 → over the $270 stop line** (reviews/gate0.md). Runner paused; no wave started.

Batch runs in **`us-east5`** (the `us` multi-region accepts Claude batch jobs but fails them with `INTERNAL`; see NOTES.md). Turnaround: P1 for 11 units 22 min; P2 12 min.

## Per unit
Tokens: in = all input incl. images and cache; out includes thinking. Costs in USD (batch `us-east5`).

| Unit | pp | img | P1 in / out (think) | P2 in / out (think) | loops | issues | $ |
|---|---|---|---|---|---|---|---|
| akerlof-1970-lemons/main | 14 | 3 | 22k / 14.0k (3.9k) | 30k / 6.7k (5.7k) | 0 | 4 | 0.17 |
| cover-2006-elements/ch02-entropy | 38 | 35 | 110k / 27.7k (4.2k) | 132k / 7.0k (6.3k) | 0 | 4 | 0.45 |
| dennett-1987-intentional-stance/ch02-true | 15 | 30 halves | 64k / 20.2k (4.0k) | 78k / 26.5k (9.3k) | 0 (full rewrite) | 6 | 0.41 |
| kahneman-2011-thinking/ch03-lazy | 11 | 0 | 13k / 9.6k (1.1k) | 20k / 3.9k (3.2k) | 0 | 3 | 0.11 |
| wittgenstein-1953-investigations/ch04-private | 16 | 0 | 56k / 47.0k (12.7k) | 82k / 25.9k (19.2k) | 2 ⚠ | 8 | 0.56 |
| jaynes-2003-probability/ch02-quantitative | 27 | 21 | 144k / 41.5k (8.1k) | 173k / 15.8k (13.2k) | 1 ⚠ | 4 | 0.66 |
| mackay-2003-information/ch02-probability | 25 | 24 | 87k / 23.2k (2.8k) | 211k / 38.5k (15.4k) | 0 + online fix | 7 | 0.88 |
| ostrom-1990-commons/ch02-institutional | 29 | 3 | 37k / 15.4k (2.0k) | 48k / 4.6k (4.0k) | 0 | 3 | 0.20 |
| lippmann-1922-publicopinion/ch06-stereotypes (HTML) | 11 | 0 | 13k / 11.8k (1.9k) | 21k / 5.5k (4.2k) | 0 | 6 | 0.13 |
| shepsle-2010-analyzing/ch03-getting | 12 | 0 | 12k / 7.7k (1.3k) | 16k / 3.9k (3.3k) | 0 | 2 | 0.09 |
| vaswani-2017-transformer/main | 15 | 11 | 46k / 16.9k (3.1k) | 58k / 5.6k (4.9k) | 0 | 3 | 0.24 |

⚠ Loops: Wittgenstein (2) and Jaynes (1) were sent back by **my checker's false positives** ("I cannot" flagged as model chatter; a citation of another book's pages flagged as out of range). Fixed; cost ≈ $0.55. MacKay: verifier edits did not match exactly (LaTeX) → online full-rewrite fix, $0.48 (online = 2× batch).

Outputs: `wiki/works/<work>/<unit>.md`; the two reference units as `*.pipeline.md` next to the agent-made references. Raw P1/P2 texts: `pipeline/_work/out/` (local) and GCS.

## Cost model (measured)
- First pass (P1 + one P2): **$0.0086 per text page, $0.0149 per image page** (least-squares on the 11 units).
- Split: P1 ≈ 52%, P2 ≈ 48% of first-pass cost.
- **Thinking:** 17% of P1 output, **71% of P2 output** (P2 visible output is short; most P2 spend is thinking). Above the 15% flag.
- Image ≈ **2,280 input tokens** each (1500 px long side), not 1,550 as planned.
- P1 output ≈ 8–47k tokens per unit (mean ≈ 21k); planner assumed 1.5k + 200/page.
- Prompt caching: system prompt cache reads appear (12k read tokens on P1) but are negligible in cost.

## Forecast (1,197 units · 11,131 text pages · 10,798 image pages)
| | core | deep | reference | total |
|---|---|---|---|---|
| First pass (P1+P2) | $192 | $21 | $43 | **$256** |
| + retries/fixes (est. +10–15% now the checker is fixed) | | | | **$280–295** |
| + work maps (P4, ~60 books) | | | | + ~$3 |

**→ Over the $270 line. Not starting waves.**

## Levers (engineer's estimates; quality lead decides)
1. **P2 effort / thinking.** Sonnet 5.5 accepts `output_config.effort` (`low`/`medium`/`high`, default `high`) and `thinking: {type: "between_tools"}` (no extended thinking). P2 at `medium` could cut P2 thinking substantially (P2 thinking ≈ 30% of first-pass cost → maybe −$30–50). Needs a quality check: re-run P2 on 4 pilot units at `medium` (≈ $0.4).
2. **Image resolution 1500 → 1200 px.** ≈ −35% image tokens; images ≈ 55% of input tokens → ≈ −$25–35. Risk: small subscripts. Test on Cover ch02 + MacKay ch02 (≈ $0.6).
3. **Shorter P1 output** (prompt): cap L3 length / avoid restating every derivation line twice. Each −20% of P1 output ≈ −$20.
4. **Defer the reference tier** (−$43 + its retries).
5. **Edit tolerance:** apply verifier edits with whitespace-normalised matching; route remaining failures to a batch fix pass instead of online (saves ~2× on fixes).
6. P1 effort `medium` (less likely to be safe for math chapters; test only if 1–3 are not enough).

Suggested next step (≈ $1–2): A/B on 4 pilot units — {P2 effort medium} × {images 1200 px} — compare verdicts/issues against the current pilot outputs, then re-forecast.

## Other findings
- **Dennett (scanned spreads):** model used printed numbers inside `(pdf N)` in a few places, then wrote a correct printed↔pdf map in Reading notes. Fix on my side: label each half with its printed page (from `toc/dennett-….json`: pdf = ⌊printed/2⌋ + 6).
- **L1 > 120 words** in 3/11 P1 digests (121–124) and **L2 = 12 bullets** once; the verifier fixed them. Prompt could stress the hard limits.
- **HTML units** have no page numbers; checker now exempts them from page-ref rules. The spec might say what to cite instead (e.g. section/paragraph).
- All 11 verifier verdicts were `pass` or `repair` (no `fail`); every unit got at least 2 edits.
