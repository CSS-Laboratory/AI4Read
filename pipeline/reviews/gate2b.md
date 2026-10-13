# Gate 2b review — quality lead (2026-10-14)

**Verdict: pass — start wave 1 after the two small changes below.** No new regression gate.

## Why pass although Part A failed
Part A tested the *verifier alone* on old v1 digests. What reaches the wiki is the *pair* (v2 digest + v2 verifier), and Part B shows that pair removes nearly all audited errors: C1, C3, J1, J2, J3, W1, W2, W3, W5, W6 and all citation problems are gone. The digest prompt now prevents most voice errors at the source. Remaining: **W4** (§272 private-linguist view reported as a finding) and **D2** (Dennett footnote, partly muddled) — both in dialogic philosophy. The generic Cover line "content and numbering may differ from the second edition" is acceptable (a caution, not a claim).

## Changes (prompts v2.1 — already pushed)
1. **Length target** (`digest.md` rule 12). v2 digests got longer than useful: Wittgenstein 7.3k words for a 7.0k-word source; Dennett 8.4k. Pass `{{SOURCE_WORDS}}` (words in the unit's text layer; for scans estimate 450/page) and `{{TARGET_WORDS}}` = round(0.40 × SOURCE_WORDS) for prose-dominant units, round(0.55 × SOURCE_WORDS) when ≥ 40% of pages are image pages (math/figures); clamp to [1,200, 6,000]. Deterministic check: **warn** (not fail) if a digest exceeds 1.5 × target; report the distribution per wave.
2. **Mandatory items extended** (`verify.md` item 3). Add to `{{MANDATORY_ITEMS}}`:
   - every sentence of **Reading notes** (all units);
   - for **argumentative units** — works in `analytic-philosophy`, plus `dennett-1987-intentional-stance`, `habermas-1989-publicsphere`, `carey-1989-cultural`, `popper-1959-logic`, `kuhn-1962-structure`, `lippmann-1922-publicopinion` — every L3 sentence that contains a quotation mark, a bold voice tag (`**…:**`), "objection", "reply", "replies", "interlocutor", "asks", or ends with "?". Cap the list at 80 items per unit (keep L0–L2 items first).
   Label each item with its kind (`strength` / `voice` / `reading-notes`).

## Then
- Set `spec_version` 1.2 + `prompt_version` v2.1 on all new records.
- **Smoke (non-blocking, ≈ $0.5):** re-run P1+P2 v2.1 on `wittgenstein-1953-investigations/ch04-private`. Report: digest words vs target, whether W4 is now tagged or flagged. Put it in STATUS.md; do not wait for me.
- **Wave 1:** run the proposed 107 units. `review_each_wave: true` stays on — stop after wave 1 for `reviews/wave-1.md`.
- **Pilot units:** do not re-run them separately. They will be digested again with v2.1 in their normal waves (their v1 files stay as drafts until then).
- **Forecast:** after wave 1, report measured v2.1 cost per text page / image page and the re-forecast for core, deep, reference. I expect the length target to cut P1 output substantially; we decide the reference tier then.
