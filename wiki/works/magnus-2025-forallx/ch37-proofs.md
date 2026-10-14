---
id: magnus-2025-forallx/ch37-proofs
work: magnus-2025-forallx
unit: "37 Proofs with quantifiers"
pages: 316–322
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Proofs with quantifiers

## L0 — One line
Quantifier proofs are built with the same backward/forward strategy as TFL proofs; the key choice is which name to use: a new name for ∀I and for the ∃E assumption, a well-chosen name for ∃I (in general one already in the proof) and for ∀E.

## L1 — The gist (≤ 120 words)
The chapter asks how to find natural-deduction proofs once quantifiers are added. Answer: keep the strategies of chapter 18 (work backward from the goal, forward from the premises) and add the quantifier rules. Backward from ∀x A(x) means aiming for A(c) with a new name c. Forward from ∃x A(x) means a subproof assuming A(c) with a new c. Working backward from ∃ and forward from ∀ needs a well-chosen name, so do these last. Two worked proofs (a quantifier equivalence in both directions) show the method. Practice sets follow.

**Prerequisites:** TFL natural deduction rules (→I, →E, subproofs); the quantifier rules ∀I, ∀E, ∃I, ∃E and their name restrictions; substitution instance A(c). (TFL is the truth-functional language of the earlier chapters; an assumption is undischarged while its subproof is still open.)

## L2 — Key ideas (5–10 bullets)
- Backward from ∀x A(x): write A(c) above it, justify by ∀I; c must not occur in any undischarged assumption (p. 316–317).
- Safe way to meet that condition: pick a name that does not yet occur in the proof (p. 317).
- Backward from ∃x A(x): write A(c) above it, justify by ∃I; here c may, and usually must, already occur in the proof (p. 317).
- Because the right c is often unclear, work backward from ∃ only after all other strategies (p. 317).
- Forward from ∃x A(x): a subproof assuming A(c), ending in the goal B, closed by ∃E; choose a new c. This generally works without backtracking (pp. 317–318).
- Forward from ∀x A(x): ∀E gives A(c) for any c, but do this last, choosing a useful c (p. 318).
- Order of strategies: backward from →, ¬, ∧, ∀; forward from ∨, ∃; only then →E, ¬E, ∨I, ∀E, ∃I (pp. 318–319).

## L3 — Walkthrough

**Setting (p. 316).** The principles of chapter 18 carry over. To prove a quantified sentence, work backward by ∀I or ∃I. To use one, work forward by ∀E or ∃E (p. 316).

**Backward from ∀x A(x) (pp. 316–317).**
Write A(c) on line $n$ and ∀x A(x) on line $n+1$, justified "∀I, n" (p. 316). A(c) is A(x) with every free occurrence of x replaced by c (p. 317). The condition: c must not occur in any undischarged assumption. Choosing a name not yet in the proof guarantees this. The name may occur in the finished proof, just not in an assumption undischarged at line $n+1$ (p. 317).

**Backward from ∃x A(x) (p. 317).**
Write A(c) above it; justify by "∃I, n". The layout looks the same as for ∀, but c may and in general must already occur in the proof. As with ∨I, it is often unclear which c works, so do this only when all other strategies are used up (p. 317).

*Intuition note:* For ∀I, the name must not occur in any undischarged assumption, so a name not yet in the proof is a safe choice. For ∃I, the name may and in general must already occur in the proof, and it is often unclear which one works. That is why the first choice is easy and the second often needs guessing (p. 317).

**Forward from ∃x A(x) (pp. 317–318).**
Take line $m$: ∃x A(x), and goal B. Open a subproof at line $n$ with assumption A(c) (AS), work to B at line $k$, then write B at line $k+1$ by "∃E, m, n–k" (p. 318). Choose c not already in the proof so that the ∃E condition holds (p. 317). This generally always works, with no backtracking (p. 317). Inside the subproof you continue to aim at B, now with A(c) available (p. 318).

**Forward from ∀x A(x) (p. 318).**
You can always write A(c) by ∀E for any c. Only some names help, so, like backward from ∃, do it only after other strategies (p. 318).

**Order of strategies (pp. 318–319).** Same order as for TFL: backward from conditionals, negations, conjunctions, now also universal quantifiers; then forward from disjunctions, now also existentials; only then try →E, ¬E, ∨I, ∀E, ∃I (pp. 318–319).

**Example 1: ∀x(A(x) → B) ∴ ∃x A(x) → B (pp. 318–320).**
1. Premise on line 1; goal ∃x A(x) → B at the bottom (p. 318).
2. Work backward from the conditional: assume ∃x A(x) (line 2), aim for B, close by →I (p. 319).
3. Work forward from ∃x A(x): no names occur yet, so pick d. Assume A(d) (line 3), aim for B, close by ∃E (p. 319).
4. Last, work forward from the premise: ∀E gives A(d) → B; choose d because it matches line 3. Then →E gives B (p. 319).

Final proof (p. 320):

| line | sentence | rule |
|---|---|---|
| 1 | ∀x(A(x) → B) | PR |
| 2 | ∃x A(x) | AS |
| 3 | A(d) | AS |
| 4 | A(d) → B | ∀E, 1 |
| 5 | B | →E, 4, 3 |
| 6 | B | ∃E, 2, 3–5 |
| 7 | ∃x A(x) → B | →I, 2–6 |

**Example 2: the converse, ∃x A(x) → B ∴ ∀x(A(x) → B) (pp. 320–321).**
1. The premise is a conditional, not an existential, so do not work forward from it yet (p. 320).
2. Work backward from ∀x(A(x) → B): aim for A(d) → B by ∀I (p. 320).
3. Work backward from A(d) → B: assume A(d), aim for B (p. 321).
4. Work forward from the premise. Its consequent is B, our goal, so we need its antecedent ∃x A(x). That follows from line 2 by ∃I (p. 321).

Final proof (p. 321):

| line | sentence | rule |
|---|---|---|
| 1 | ∃x A(x) → B | PR |
| 2 | A(d) | AS |
| 3 | ∃x A(x) | ∃I, 2 |
| 4 | B | →E, 1, 3 |
| 5 | A(d) → B | →I, 2–4 |
| 6 | ∀x(A(x) → B) | ∀I, 5 |

*Intuition note:* In both proofs we first work backward from the goal and use the premise last. In Example 1 the name d is chosen new for the ∃E assumption and reused in ∀E. In Example 2 d is chosen new for ∀I and reused in ∃I.

## Toy example (ours)
Prove ∀x(A(x) ∧ B(x)) ∴ ∀x A(x).
1. Line 1: ∀x(A(x) ∧ B(x)), PR.
2. Goal ∀x A(x). Work backward: aim for A(d), with d new (it occurs in no assumption). Finish by ∀I.
3. Line 2: A(d) ∧ B(d), ∀E, 1 (the premise is used last, with the name d).
4. Line 3: A(d), ∧E, 2.
5. Line 4: ∀x A(x), ∀I, 3. d occurs in lines 2–3 but not in the premise (line 1), which is the only undischarged assumption, so the ∀I condition holds.

## Concepts
- [[backward-forward-proof-strategy]] (new) — build a proof by justifying the goal from above, and using premises from below, in a fixed order of rule types (p. 316–319)
- [[universal-introduction]] (new) — from A(c), with c not in any undischarged assumption, infer ∀x A(x) (p. 316)
- [[existential-introduction]] (new) — from A(c), for a usually already-present name c, infer ∃x A(x) (p. 317)
- [[existential-elimination]] (new) — from ∃x A(x) and a subproof A(c) … B with c new, infer B (p. 318)
- [[substitution-instance]] (new) — A(c): A(x) with every free x replaced by c (p. 317)

## Canonical instances
- [[quantifier-conditional-equivalence]] (new) — ∀x(A(x) → B) and ∃x A(x) → B are proved from each other (pp. 318–321)

## Bridges (candidates)
- [structural-analogy] fresh name for ∀I ↔ mathematics: "let n be an arbitrary integer" in a general proof — the name carries no special assumptions.
- [structural-analogy] ∃E subproof ↔ mathematics: "suppose such an object exists, call it c" — you reason about a witness without knowing which one.

## Questions this raises
- What exactly goes wrong if c does occur in an undischarged assumption when ∀I is applied?
- Why does working forward from ∃ generally not need backtracking, while backward from ∃ does?
- Why does the book say the arguments in exercise set C require IP (p. 322)?

## Exercises worth doing
- Ex. A.1–A.2 (p. 321) — moving a quantifier past a conditional: easy
- Ex. A.3–A.4 (p. 321) — ∀ with ∧ and ∃ with ∨ as equivalences: medium
- Ex. A.6 (p. 322) — the main example's argument (done in the text, repeat it unaided): easy
- Ex. A.7 (p. 322) — ∃x(A(x) → B) ∴ ∀x A(x) → B: medium
- Ex. B.2 (p. 322) — nested quantifiers, with transitivity of R: medium
- Ex. C.1–C.5 (p. 322) — require IP: hard

## Reading notes
- Printed = pdf − 10.
- Text layer is clean; the page images match it.
- The wording "choose" appears as "chose" on p. 317 (typo in source).
- Exercise A.5 on p. 321 has an unmatched bracket: "A ∨ ∀x B(x))"; also C.3 on p. 322. The source prints it so.
- In the images the schematic sentence letters appear as script letters; the text layer renders them as plain A and B.
