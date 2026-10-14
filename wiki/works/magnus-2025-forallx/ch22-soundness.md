---
id: magnus-2025-forallx/ch22-soundness
work: magnus-2025-forallx
unit: 22 Soundness and completeness
pages: 182-188
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
audited: 2026-10-14
audit_fixes: 3
---
# Soundness and completeness

## L0 — One line
For TFL (truth-functional logic, the book's logic of sentence letters and connectives), the truth-table notion of validity and the derivation notion of validity coincide (⊢ implies ⊨, and ⊨ implies ⊢), so we may use whichever method suits the task.

## L1 — The gist (≤ 120 words)
Chapter 20 started using ⊢ (derivations) like ⊨ (truth tables). This chapter asks whether the two always agree. The author first defines each logical concept twice: semantically (truth tables) and proof-theoretically (derivations). Then he states two properties. Soundness means anything derivable is semantically valid. Completeness means every semantically valid argument is derivable. Full proofs are beyond the book; only the idea of the soundness proof is sketched. TFL's proof system has both properties, though not every system does. So the choice of method is practical. Derivations can show, for example, that a sentence is a theorem or that two sentences are equivalent. But they cannot practically show that no proof exists, so truth tables are needed for non-equivalence or contingency.

**Prerequisites:** truth tables and valuations; natural-deduction derivations in TFL; the symbols ⊨, ⊢, ⊥; tautology, contradiction, contingency, equivalence, consistency, validity.

## L2 — Key ideas (5–10 bullets)
- The question: do ⊨ and ⊢ always work the same way? The answer given is yes, for TFL (pp. 182–183).
- Every logical concept gets a semantic and a proof-theoretic definition (Table 22.1). Concepts with no direct derivation test are defined in terms of ones that have one; contingency and consistency are defined negatively (pp. 183–184).
- Contingency and consistency are defined negatively on the proof side: "neither a theorem nor an inconsistent sentence" (contingency) and "not inconsistent" (consistency). There is no practical finite derivation test for them (p. 183).
- Soundness (⊢ implies ⊨) means the derivation rules never prove an invalid argument. The sketch is that each rule preserves entailment (truth of the premises guaranteeing truth of the conclusion) by the premises plus open assumptions (p. 185).
- Completeness (⊨ implies ⊢) means the rules are enough for every semantically valid argument. It is generally harder to prove than soundness (p. 185).
- TFL's proof system is sound and complete. This is not true of all proof systems or formal languages (pp. 185–186).
- Truth tables grow impossibly large after a few sentence letters. Derivations cannot practically prove negative claims (pp. 186–187).
- Table 22.2 says which method to use to show a property present and to show it absent (p. 187).

## L3 — Walkthrough

**Opening (p. 182–183).** In chapter 20 the single turnstile was used like the double turnstile. If a truth table shows A is a tautology, we write ⊨ A. If a derivation shows it, we write ⊢ A (p. 182). The author says the reader may have wondered whether the two always agree, for tautologies/theorems, valid arguments and equivalent sentences. His answer is yes. He says we can show this by proving the table-based and derivation-based concepts equivalent, e.g. ⊨ A iff ⊢ A for any sentence A (pp. 182–183).

**Defining the concepts twice (pp. 183–184).**
- Truth-table definitions come from chapter 12. A theorem is a sentence derivable without premises (p. 183).
- An *inconsistent sentence in TFL* is one from which ⊥ can be derived. Footnote: A ⊢ ⊥ iff ¬A is a theorem (p. 183).
- *Proof-theoretically contingent*: neither a theorem nor inconsistent. It is defined negatively because there is no practical finite derivation method for contingency (p. 183).
- A collection is *inconsistent in TFL* iff ⊥ can be derived from it. It is *consistent* iff it is not inconsistent (p. 183).
- An argument is *provably valid in TFL* iff there is a derivation of its conclusion from its premises (p. 183).

Table 22.1 (p. 184) pairs the definitions (the main connective is the one that governs the whole sentence):

| Concept | Truth table | Derivation |
|---|---|---|
| Tautology / theorem | only Ts under main connective | derivable with no premises |
| Contradiction / inconsistent sentence | only Fs | ⊥ derivable from it |
| Contingent | both Ts and Fs | not a theorem or inconsistent |
| Equivalent / interderivable | identical main-connective columns | each derivable from the other |
| Unsatisfiable / inconsistent set | no line where all are true | ⊥ derivable |
| Satisfiable / consistent set | at least one line where all are true | ⊥ not derivable |
| Valid argument | no line with all premises T and conclusion F | conclusion derivable from premises |

*Intuition note:* Each idea is defined by a test on truth tables and by a test on derivations. The chapter asks whether the two tests always give the same verdict.

**The two directions (p. 185).** A full proof is beyond the book's scope. The author sketches it for validity only, and says the other concepts follow quickly. Two directions are needed: ⊢ implies ⊨, and ⊨ implies ⊢ (p. 185).

*Soundness.* This is the argument from ⊢ to ⊨. A proof system is sound if there are no derivations of arguments that truth tables show invalid. Showing it requires showing that any possible proof is a proof of a valid argument. Succeeding on many valid arguments and failing on invalid ones is not enough. In a nutshell, one shows that every inference rule preserves the property that the conclusion is entailed by the premises of the proof together with the open assumptions. Details are in chapter 48 (p. 185). The text writes this as: A ⊢ B implies A ⊨ B (p. 185).

*Completeness.* A system is complete iff there is a derivation of every semantically valid argument. Proving it is generally harder than proving soundness. Soundness shows the rules work as intended. Completeness shows that no needed rule was left out. This proof is beyond the book's scope (p. 185).

**Result.** The proof system for TFL is both sound and complete. This is not so for all proof systems or formal languages. Because it holds for TFL, we can give proofs or truth tables, whichever is easier (pp. 185–186).

*Intuition note:* Soundness means the rules never prove too much. Completeness means they never prove too little. Together, derivations and truth tables give the same answers.

**Choosing a method (p. 186–187).**
- Students often prefer truth tables because they are mechanical. But tables become impossibly large after a few sentence letters (p. 186).
- Proofs cannot practically show contingency. That would need showing there is no proof that the sentence is a tautology or a contradiction, and we can never know that no such proof has just been missed (p. 186).
- Likewise, derivations can show equivalence but cannot show non-equivalence, so we use truth tables (p. 186).

Table 22.2 (p. 187): to prove a property present / absent.
- Tautology: derive it / find a false line.
- Contradiction: derive ⊥ from it / find a true line.
- Contingency: find a false line and a true line / prove the sentence or its negation.
- Equivalence: derive each from the other / find a line where the values differ.
- Consistency: find a line where all are true / derive ⊥ from the sentences.
- Validity: derive the conclusion from the premises / find a line with true premises and false conclusion.

*Intuition note:* A derivation settles a claim by one success. Truth tables settle the claims that would need "no derivation exists": one line for a non-tautology or non-equivalence, two lines (one true, one false) for contingency. A search for derivations cannot check that nothing was missed.

**Practice exercises (pp. 186–188).** Two sets of 12 problems each. Each asks you to show, by derivation or truth table, that something is or is not a theorem, contradiction, contingent, equivalent, consistent or valid.

## Toy example (ours, not from the text)
Take P ∧ Q and Q ∧ P.
- Truth table, lines (P,Q) = TT, TF, FT, FF.
  - P ∧ Q: T, F, F, F.
  - Q ∧ P: T, F, F, F.
  - The columns are identical, so they are semantically equivalent.
- Derivation: assume P ∧ Q, take out P and Q, rebuild Q ∧ P, and do the same in reverse. Each is derivable from the other, so they are interderivable. The two verdicts agree, as soundness and completeness predict.
- Now P ∧ Q versus P ∨ Q. At (P,Q) = (T,F), P ∧ Q is F and P ∨ Q is T. That one line shows they are not equivalent. A derivation is no practical way to show this, because a failed search for a proof proves nothing (p. 186; Table 22.2).

## Concepts
- [[validity / soundness]] — here "sound" describes a proof system: no derivation of an argument that truth tables show invalid. This differs from the canon's soundness of an argument (valid with true premises) (p. 185)
- [[completeness]] (new) — a proof system is complete iff every semantically valid argument has a derivation (p. 185)
- [[semantic vs. proof-theoretic definition]] (new) — a concept defined by truth tables (⊨) vs. by derivations (⊢) (pp. 183–184)
- [[provably valid]] (new) — argument whose conclusion is derivable from its premises (p. 183)
- [[proof-theoretic contingency / consistency]] (new) — defined negatively: not a theorem or inconsistent; not inconsistent (p. 183)

## Canonical instances
- [[truth-table-vs-derivation-choice]] — Table 22.2 shows when each method is best (p. 187)

## Bridges (candidates)
- [structural-analogy] Soundness/completeness ↔ analytic-philosophy: validity — it links a syntactic test for validity to the semantic definition of validity (cannot have true premises and a false conclusion).
- [metaphor] Failed search for a proof ↔ epistemology: absence of evidence — not finding a proof does not show none exists.

## Questions this raises
- What exactly must each inference rule preserve in the soundness proof? Chapter 48 is cited for the details.
- Why is completeness harder than soundness, and what would it mean for a rule to be "left out"?
- Which proof systems or formal languages are not both sound and complete?
- Why do claims that no derivation exists (e.g. non-equivalence, contingency) force a switch to truth tables?

## Exercises worth doing
- Ex. A.2 (p. 186) — show a non-theorem; the truth table finds a false line — easy
- Ex. A.5 (p. 186) — show contingency; needs both a true and a false line — easy
- Ex. A.8 (p. 187) — show non-equivalence by a differing line — easy
- Ex. A.9 (p. 187) — show inconsistency of a set by derivation of ⊥ or by table — medium
- Ex. A.12 (p. 187) — show invalidity by counterexample line — easy
- Ex. B.7 (p. 188) — show equivalence of ((¬X ↔ X) ∨ X) and X — medium

## Reading notes
- Printed = pdf − 10 (pdf 192 = p. 182).
- Misprints and slips in the pages: Ex. B.12 on p. 188 has unbalanced parentheses, "(C → ¬L) → C)". The text has "can chose" (p. 186). The sentence "⊨ implies ⊢" lacks a final full stop (p. 185). The first paragraph has "Not only could show" (p. 182).
- Table 22.1 (p. 184) is printed rotated sideways. The text layer is readable.
- Only the soundness idea is sketched; the author gives no proof of completeness and points to chapter 48 for soundness (p. 185).
- The summary sentence at p. 185, "A ⊢ B implies A ⊨ B", is written loosely for a single premise.
