# Gate 2 review — quality lead (2026-10-13)

**Verdict: not yet. Pass after one regression test (≈ $3–5).** The engineering is excellent (11/11 accepted, A/B well designed, decisions sound: keep P2 at `high`, P1 at 1200 px). But an independent audit of the *accepted* digests found errors that survive verification. Prompts are now v2 (spec v1.2). Run the regression test below; if it passes, start wave 1 without waiting for me.

## Independent audit (Opus, against page images; reports in `pipeline/reviews/audit/`)
| Unit | Checks | Critical | Major | Minor |
|---|---|---|---|---|
| Akerlof 1970 | 45 | 0 | 0 | 12 |
| Cover ch. 2 | 66 | 2 | 1 | 7 |
| Dennett ch. 2 | 52 | 0 | 2 | 4 |
| Wittgenstein §§243–315 | 58 | 1 | 6 | 8 |
| Kahneman ch. 3 | 47 | 0 | 0 | 3 |
| Jaynes ch. 2 | ~140 | 1 | 2 | 6 |
| MacKay ch. 2 | ~160 | 0 | 1 | 3 |
| Vaswani 2017 | ~200 | 0 | 0 | 3 |

Equations, tables and toy-example numbers are almost perfect (≈ 500 math items, one sign error in an added step). The surviving errors are of four kinds, and the v1 verifier did not check for any of them:
1. **Logical strength** — "if" became "only if" (Cover L2 + intuition note); dropped hedges (Jaynes on Gödel; Dennett modals).
2. **Voice** — a rhetorical question turned into a statement that reverses its point (Wittgenstein §249); interlocutor vs Wittgenstein confused (§§263, 264, 272); an imported slogan ("meaning is use").
3. **Outside knowledge** outside L3 — Reading notes describing the 2nd edition from memory (Cover).
4. **Citations** — pdf numbers where printed numbers are visible (MacKay: printed = pdf − 12; Dennett halves; Wittgenstein printed pages `95e–110e` exist but were reported as unknown).

## Changes made by the quality lead
- `pipeline/prompts/digest.md` **v2**: rules for logical strength, voice tags, "summaries never go beyond L3", no outside knowledge in any section, page-citation rules (printed > pdf; § for section-numbered texts; headings for HTML), true added steps, definitions at first use, Prerequisites line, skip path, tensor shapes, no full exercise solutions, hard limits.
- `pipeline/prompts/verify.md` **v2**: check A covers every section; new **check H (logical strength & voice)** with critical severity; added steps checked numerically (E); undefined terms (G); citation problems (C). New output block `<h_checks>`. New placeholder `{{MANDATORY_ITEMS}}`.
- `DIGEST_SPEC.md` **v1.2**: Prerequisites line; ground rules for strength, voice, and summaries.

## Engineering requests
1. **`{{MANDATORY_ITEMS}}`**: deterministic pre-check that extracts every sentence from L0, L1, L2 and every intuition note containing `only|always|never|iff|exactly|all|every|must|cannot|proves|shows` (word-boundary, case-insensitive) and passes them as a JSON list. Parse `<h_checks>`; a missing `<h_checks>` block = rerun P2.
2. **Printed page labels**: when PDF labels are missing, infer printed numbers from running headers/footers (constant offset detection) — MacKay (−12), Wittgenstein (`NNe` labels), and every other work with blank `printed_pages` in `units.csv`. Report how many units still lack printed labels.
3. **Multi-field works**: pass *all* catalog fields of a work and all their concept spines into `{{CONCEPT_SPINE}}`.
4. **Strip verifier residue** from accepted digests (stray tags, JSON fragments).
5. **Deterministic check**: Prerequisites line present; no `(pdf N)` refs when the unit has printed labels.

## Regression test (Gate 2b) — run before wave 1
A. **Verifier v2 on the old v1 digests** of Cover ch. 2, Wittgenstein ch. 4, Jaynes ch. 2, Dennett ch. 2 (P2 only). Pass criterion: it flags **all 4 criticals** and **≥ 8 of the 11 majors** listed in the audit files (IDs C*, W*, J*, D*).
B. **Full v2 run (P1 + P2 + fixes)** on the same 4 units + MacKay ch. 2. Pass criterion: the audit's critical errors do not appear in the accepted outputs; citations use printed pages; Prerequisites present.
C. Record cost per page for v2 (thinking may rise in P2) and re-forecast.
If A and B pass: **start wave 1** (your proposed list is fine) and re-plan/repair the 11 pilot digests with v2 (re-run P2 v2 on them; replace accepted files). If either fails: stop, write results to `pipeline/GATE2b.md`, and wait for me.

## Scope and budget
- Keep the order core → deep → reference and the $280 hard stop. Do **not** decide the reference tier now; decide after waves 1–2 with measured v2 costs. Reference-tier works can also be digested later, just in time, when a post needs them.

## Budget update (2026-10-13, Kunhao)
Hard stop raised from $280 to **$300** (`control.json` → `max_spend_usd: 300`; please also set `config.yaml`). The GCP budget is ¥48,000 ≈ $300 at 160 JPY/USD — keep the runner's USD cap as the binding limit and watch the yen alerts.
