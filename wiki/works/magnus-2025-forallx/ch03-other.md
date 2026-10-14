---
id: magnus-2025-forallx/ch03-other
work: magnus-2025-forallx
unit: 3 Other logical notions
pages: 18-25
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Other logical notions

## L0 — One line
Like validity, the notions of joint possibility, necessary truth, necessary falsehood, contingency and necessary equivalence are all defined by asking which sentences are true in which cases (conceivable scenarios).

## L1 — The gist (≤ 120 words)
Chapter 2 defined validity using "cases". This chapter uses the same idea to define five more notions. Sentences are jointly possible exactly when some case makes them all true. A sentence is a necessary truth if it is true in every case, and a necessary falsehood if it is false in every case. It is contingent if it is true in some case and false in another. Two sentences are necessarily equivalent if they have the same truth value in every case. The authors call these ideas similarly important to validity. One consequence of the definitions: an argument with jointly impossible premises counts as valid.

**Prerequisites:** the definition of validity from chapter 2; the idea of a "case" as a conceivable scenario.

## L2 — Key ideas (5–10 bullets)
- All the notions rest on truth *in cases*. Here a case is a conceivable scenario. A different notion of "case" would give different notions (p. 18).
- Sentences are jointly possible iff some case makes them all true. Otherwise they are jointly impossible (pp. 19, 21).
- Adding a sentence to an already jointly impossible collection cannot make it jointly possible (p. 19).
- Any argument with jointly impossible premises is automatically valid. So validity does not require jointly possible premises (pp. 19–20).
- A sentence is necessarily true, necessarily false or contingent. Contingent means true in some case and false in another (pp. 20–21).
- A sentence can be true at all times and still be contingent (p. 20).
- Two sentences are necessarily equivalent if they have the same truth value in every case. They can both be contingent (p. 21).
- A summary box gives all the definitions in one place (p. 21).

## L3 — Walkthrough

**Opening (p. 18).** Chapter 2 introduced consequence, that is, the validity of arguments. The new notions "all rely, as did validity, on the idea that sentences are true (or not) in cases" (p. 18). Here "case" means conceivable scenario, as in the definition of conceptual validity. Using a different idea of "case" would give different notions. The authors say that, as logicians, they will eventually consider a more permissive definition of case than the one used here (p. 18).

**3.1 Joint possibility (pp. 18–20).**
- Example sentences: B1 "Jane's only brother is shorter than her" and B2 "Jane's only brother is taller than her." Logic alone cannot tell us which, if either, is true. But if B1 is true, B2 must be false, and the other way round. No possible scenario makes both true, so they are incompatible (p. 19).
- **Definition:** sentences are jointly possible if and only if there is a case where they are all true together (p. 19).
- B1 and B2 are jointly impossible. B1 and B3 ("Jane's only brother is younger than her") are jointly possible (p. 19).
- The notion applies to any number of sentences. Take G1 (at least four giraffes at the park), G2 (exactly seven gorillas), G3 (not more than two Martians) and G4 (every giraffe at the park is a Martian) (p. 19).
  - G1 and G4 together entail at least four Martian giraffes. G3 implies there are at most two Martian giraffes. So G1–G4 are jointly impossible (p. 19).
  - G1, G3 and G4 are already jointly impossible by themselves. Adding a sentence to a jointly impossible collection cannot make it jointly possible (p. 19).
- A warning: one might think an argument makes sense only if its premises are jointly possible. Neither the definition of argument nor that of validity requires this. By the authors' definitions, any argument with jointly impossible premises is automatically valid. The reader is asked to convince themselves of this (pp. 19–20).

*Intuition note:* "Jointly possible" asks whether you can imagine one scenario that makes all the sentences true at once. If you cannot, there is no case where the premises are true, so no case where they are true and the conclusion false. That is why such arguments count as valid.

**3.2 Necessary truths, necessary falsehoods, and contingency (p. 20).**
- Three sentences: (1) "It is raining." (2) "Either it is raining here, or it is not." (3) "It is both raining here and not raining here." (p. 20)
- Sentence 1 can be true or false, depending on the weather. A sentence capable of being true and capable of being false, in different circumstances, is **contingent** (p. 20).
- Sentence 2 is true whatever the weather is like. It is a **necessary truth** (p. 20).
- Sentence 3 cannot be true. It cannot be both raining and not raining in the same place at the same time. It is a **necessary falsehood** (p. 20).
- A sentence can be always true and still be contingent. Suppose the universe never contained fewer than seven things. Then "At least seven things exist" would always be true. Yet it is contingent, because the world could have been much smaller, and then the sentence would be false (p. 20).

*Intuition note:* Necessary does not mean merely that a sentence happens to hold at all times. It means that the sentence holds in every case, that is, in every conceivable scenario. The seven-things example shows that being always true is not the same as being necessary.

**3.3 Necessary equivalence (p. 21).**
- Example: "John went to the store after he washed the dishes" and "John washed the dishes before he went to the store" (p. 21).
- Both are contingent, since John might never have done either thing. Yet they must have the same truth value. If either is true, both are. If either is false, both are (p. 21).
- When two sentences have the same truth value in every case, they are **necessarily equivalent** (p. 21).

*Intuition note:* Equivalence is about matching truth values across all cases, not about being true. Two sentences can be equivalent and both contingent.

**Summary of logical notions (p. 21).**
- Valid argument: there is no case where all premises are true and the conclusion is not.
- Necessary truth: true in every case.
- Necessary falsehood: false in every case.
- Contingent: neither of those; true in some case and false in some other case.
- Necessarily equivalent: in every case, both true or both false.
- Jointly possible: there is a case where all are true together. Jointly impossible otherwise.

**Practice exercises (pp. 22–25).** Exercises A–H ask the reader to classify sentences, test pairs for equivalence, test collections for joint possibility, and decide which combinations of notions are possible (pp. 22–25).

## Toy example (ours)
Let a toy world have two yes/no facts: R = "it is raining" and C = "it is cold". Take four cases. This is a simplification of "conceivable scenarios".

| Case | R | C |
|---|---|---|
| 1 | T | T |
| 2 | T | F |
| 3 | F | T |
| 4 | F | F |

- S1 = *It is raining and cold*: true only in case 1.
- S2 = *It is not raining*: true in cases 3 and 4.
- S1 and S2 have no case in common (case 1 is not among {3, 4}), so they are jointly impossible.
- Argument: premises S1, S2; conclusion "It is cold". There is no case with both premises true, so no case with true premises and a false conclusion. The argument is valid.
- S3 = *It is raining or it is not*: true in cases 1, 2, 3, 4, so it is a necessary truth.
- "It is raining" is true in case 1 and false in case 3, so it is contingent.
- *It is not the case that it is not raining* has the same truth value as "It is raining" in all four cases. They are necessarily equivalent, and both are contingent.

## Concepts
- [[case]] (new) — a conceivable scenario in which sentences are true or false; the basis of all notions here (p. 18)
- [[validity / soundness]] — valid: no case has all premises true and the conclusion not; only validity is treated here (p. 21)
- [[joint-possibility]] (new) — some case makes all the sentences true together; otherwise jointly impossible (p. 19)
- [[necessary-truth]] (new) — a sentence true in every case (p. 21)
- [[necessary-falsehood]] (new) — a sentence false in every case (p. 21)
- [[contingent-sentence]] (new) — a sentence true in some case and false in some other case (pp. 20–21)
- [[necessary-equivalence]] (new) — two sentences with the same truth value in every case (p. 21)

## Canonical instances
- [[jane-brother-sentences]] (new) — B1 and B2 are jointly impossible; B1 and B3 are jointly possible (p. 19)
- [[giraffes-gorillas-martians]] (new) — G1–G4 are jointly impossible; G1, G3, G4 already are (p. 19)
- [[raining-sentences]] (new) — contingent, necessarily true and necessarily false sentences about rain (p. 20)
- [[at-least-seven-things]] (new) — always true yet contingent (p. 20)
- [[john-store-dishes]] (new) — two contingent sentences that are necessarily equivalent (p. 21)

## Bridges (candidates)
- [same-math] joint possibility, necessary truth, equivalence ↔ set theory: if each sentence is modelled as the set of cases where it is true, these become non-empty intersection, the full set, and equal sets.
- [structural-analogy] necessary truth ↔ propositional logic: tautology, true under every truth-value assignment.
- [structural-analogy] jointly impossible premises making an argument valid ↔ a universal claim over an empty set being true "vacuously".

## Questions this raises
- If a different, more permissive notion of "case" is used (p. 18), which sentences change from necessary to contingent?
- Is it reasonable that an argument with jointly impossible premises counts as valid? What would we lose by requiring jointly possible premises?
- Can a sentence be necessarily true in one sense of "case" and contingent in another?
- How can we tell whether two sentences are necessarily equivalent without listing all cases?

## Exercises worth doing
- Ex. A (p. 22) — classify sentences about Caesar and the Rubicon as necessary truth, necessary falsehood or contingent — difficulty: easy
- Ex. C (p. 22) — decide which pairs are necessarily equivalent, which tests the difference between agreeing in truth value in fact and in every case — difficulty: medium
- Ex. E (p. 23) — test the giraffe/gorilla/Martian sentences in subsets for joint possibility — difficulty: medium
- Ex. F (pp. 23–24) — test combinations of the Socrates sentences M1–M4 — difficulty: medium
- Ex. G (p. 24) — which combinations of notions are possible (for example, a valid argument with a false conclusion)? — difficulty: hard
- Ex. H (pp. 24–25) — more possible/impossible combinations, including an argument with true premises and a false conclusion — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 28–35 are printed 18–25).
- The text layer is clean. The only odd wording: the chapter opening says "In this section", though it opens a chapter (p. 18).
- Solutions to the exercises are not printed in these pages.
- The definition of "conceptual validity" is not given in these pages. The chapter refers back to it and to chapter 2, which is not in this unit.
