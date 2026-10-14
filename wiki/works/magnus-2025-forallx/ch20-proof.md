---
id: magnus-2025-forallx/ch20-proof
work: magnus-2025-forallx
unit: "20 Proof-theoretic concepts"
pages: 170-173
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Proof-theoretic concepts

## L0 — One line
The single turnstile "⊢" (there is a proof) defines theorem, interderivable and jointly inconsistent; for theorem, inconsistent and interderivable, showing "yes" needs only one or two proofs, but showing "no" needs reasoning about all possible proofs; for consistent, the two are reversed.

## L1 — The gist (≤ 120 words)
The chapter gives proof-based vocabulary. "A₁,…,Aₙ ⊢ C" says a proof of C exists whose undischarged assumptions are among the A's. From this the authors define theorem (a proof with no undischarged assumptions), interderivable sentences (proofs both ways) and jointly inconsistent sentences (⊥ can be proved from them). Each is relatively easy to establish: you only need to produce one or two proofs. The opposite claims (not a theorem, not interderivable, consistent) are typically much harder, because you must show that no proof is possible. A table summarises this. The single turnstile is different from the double turnstile "⊨", which concerns valuations.

**Prerequisites:** Natural-deduction proofs with assumptions, subproofs, and the rules ∧E, ¬E, ¬I; the symbol ⊥; entailment "⊨" from ch. 12.

## L2 — Key ideas (5–10 bullets)
- "⊢" means a proof exists; "⊨" means valuations (interpretations in FOL) exist. They are different notions (p. 170).
- A theorem is a sentence provable with no undischarged assumptions: ⊢ A (pp. 170–171).
- ¬(A ∧ ¬A) is a theorem, proved by a subproof assuming A ∧ ¬A (p. 171).
- Showing that a sentence is a theorem needs one proof; showing it is not needs all possible proofs (p. 171).
- Two sentences are interderivable iff each is provable from the other (p. 171).
- Sentences are jointly inconsistent iff they prove ⊥; otherwise they are jointly consistent (p. 172).
- The table: theorem, inconsistent, equivalent need one or two proofs for "yes"; consistent needs one proof for "no"; the opposite answers need all possible proofs (p. 172).

## L3 — Walkthrough

**Turnstile (p. 170).** "A₁, A₂, …, Aₙ ⊢ C" means there is some proof ending with C whose undischarged assumptions are among A₁,…,Aₙ. "A₁,…,Aₙ ⊬ C" means there is no such proof (p. 170). "⊢" (single turnstile) concerns the existence of proofs. "⊨" (double turnstile, entailment, ch. 12) concerns the existence of valuations, or interpretations in FOL (p. 170).

**Theorem (pp. 170–171).** If there is a proof of A with no undischarged assumptions, we write ⊢ A, and A is a theorem: A is a theorem iff ⊢ A (pp. 170–171).

*Example (p. 171).* To show ¬(A ∧ ¬A) is a theorem, start a subproof assuming A ∧ ¬A, since the main operator is negation:

1. A ∧ ¬A — AS
2. A — ∧E, 1
3. ¬A — ∧E, 1
4. ⊥ — ¬E, 3, 2
5. ¬(A ∧ ¬A) — ¬I, 1–4

No assumption stays undischarged. This theorem is an instance of the law of non-contradiction (p. 171).

*Intuition note.* A theorem is a sentence that can be proved from no premises. To show that a sentence is one, you only need to find one proof.

**Difficulty of "not a theorem" (p. 171).** Showing a sentence is not a theorem is typically much harder. You must show that no proof is possible, not just that some strategies fail. Failing a thousand times could mean the proof is too long to see, or that you did not try hard enough (p. 171).

**Interderivable (pp. 171–172).** A and B are interderivable iff each can be proved from the other, i.e. A ⊢ B and B ⊢ A (p. 171). Showing this needs a pair of proofs. Showing non-interderivability is as hard as showing a sentence is not a theorem (p. 172).

**Jointly inconsistent (p. 172).** A₁,…,Aₙ are jointly inconsistent iff A₁,…,Aₙ ⊢ ⊥. If not, they are jointly consistent. Showing inconsistency: prove ⊥ with all the sentences as premises. Showing consistency is much harder: it needs showing that no proof of a certain kind is possible (p. 172).

**Summary table (p. 172).**

| | Yes | No |
|---|---|---|
| theorem? | one proof | all possible proofs |
| inconsistent? | one proof | all possible proofs |
| equivalent? | two proofs | all possible proofs |
| consistent? | all possible proofs | one proof |

*Intuition note.* "There is a proof" is an existence claim, so one example proves it. A claim that none exists covers every possible proof. Consistency is the negation of "proves ⊥", so its answers are flipped.

**Practice exercises (pp. 172–173).** Sets A–E are listed under Exercises below.

## Toy example (ours)
Show P ∧ Q and Q ∧ P are interderivable (two proofs, as in the table).
- Proof 1, P ∧ Q ⊢ Q ∧ P: assume P ∧ Q (line 1); ∧E gives P (2) and Q (3); ∧I on 3, 2 gives Q ∧ P (4). The only undischarged assumption is P ∧ Q.
- Proof 2, Q ∧ P ⊢ P ∧ Q: the same with P and Q swapped.
Both A ⊢ B and B ⊢ A hold, so they are interderivable. (Uses ∧I, which this unit does not state.)

## Concepts
- [[turnstile-single]] (new) — "⊢": a proof exists from the listed assumptions to the conclusion (p. 170)
- [[entailment-double-turnstile]] (new) — "⊨": concerns valuations, not proofs (p. 170)
- [[theorem]] (new) — a sentence with a proof on no undischarged assumptions (p. 171)
- [[interderivable]] (new) — A ⊢ B and B ⊢ A (p. 171)
- [[joint-inconsistency]] (new) — the sentences prove ⊥; otherwise consistent (p. 172)

## Canonical instances
- [[law-of-non-contradiction]] — ¬(A ∧ ¬A) is a theorem (p. 171)

## Bridges (candidates)
- [structural-analogy] Existence of a proof (⊢) ↔ computer science: certificates for NP-style "yes" answers — one witness shows "yes"; "no" needs a search over all candidates.
- [metaphor] Failing to find a proof in a thousand tries ↔ philosophy of science: failing to refute a theory does not show it true.

## Questions this raises
- How can one show that no proof exists, e.g. that a sentence is not a theorem?
- How are ⊢ and ⊨ related, so that proofs and valuations agree?
- Does the "easy yes / hard no" asymmetry hold for valuation-based notions?

## Exercises worth doing
- Ex. A.2 (p. 172) — show that N ∨ ¬N is a theorem — difficulty: medium
- Ex. A.4 (p. 172) — show that ((A → B) → A) → A is a theorem — difficulty: hard
- Ex. C.3 (p. 173) — show that T → S and ¬S → ¬T are interderivable — difficulty: medium
- Ex. D (p. 173) — what A ⊢ B implies for (A∧C) ⊢ B and (A∨C) ⊢ B — difficulty: medium
- Ex. E (p. 173) — why non-interderivability is as hard as non-theoremhood — difficulty: medium

## Reading notes
- Printed = pdf − 10.
- No misprints noticed in the page images. The table's "equivalent?" row seems to correspond to what the text calls interderivable (the two-proofs row); the text does not say so explicitly.
- In exercise A.1 the sentence letter is the italic letter O (not zero).
