# Prompt proposals (engineer → quality lead)

Suggestions only; the quality lead owns `DIGEST_SPEC.md` and `pipeline/prompts/`.

## 2026-10-13 (from the Gate 2 pilot, see `pipeline/GATE2.md`)
1. **Hard limits.** 3/11 L1 sections were 121–124 words and one L2 had 12 bullets. Suggest: "L1: at most 120 words — count them" and "L2: 5–10 bullets, never more".
2. **Output length.** P1 output averaged ~21k tokens (up to 47k). If cost needs cutting: ask L3 to give each derivation once (no restating), and keep intuition notes to 2–3 sentences.
3. **HTML sources** have no pages. Suggest a rule for what to cite instead (e.g. `(§ heading)` or `(para. N)`), or allow no page refs for HTML units.
4. **Verifier edits.** One verifier edit failed to match exactly (LaTeX whitespace). Suggest: "copy `find` exactly, including spaces inside LaTeX; prefer short unique `find` strings".
5. **Scanned spreads (Dennett).** I will label each half-image with its printed page; the prompt could add "use the printed page shown in the image label, not the pdf number, when both are given".
