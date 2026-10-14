---
id: magnus-2025-forallx/ch41-proofs
work: magnus-2025-forallx
unit: "40 Derived rules; 41 Proofs and semantics"
pages: 330–335
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
# Derived rules; Proofs and semantics

## L0 — One line
Provability (⊢) and semantic entailment (⊨) are different notions, but they agree, so for a given task you may use whichever method is easier.

## L1 — The gist (≤ 120 words)
Chapter 40 argues that the quantifier-conversion (CQ) rules are derived: it derives two of them from the basic rules of chapter 36 and says similar proofs work for the others. Chapter 41 asks how the two turnstiles relate. ⊢ means a proof exists; ⊨ means no interpretation makes the premises true and the conclusion false. The text says they are different notions but extensionally equivalent (they hold for exactly the same arguments): $A_1,\dots,A_n \vdash B$ iff $A_1,\dots,A_n \vDash B$. So to show validity, find a proof; to refute validity, build a counter-interpretation. A table lists which method is (usually) easier for each question. Proving that the two notions agree is where introductory logic becomes intermediate logic.

**Prerequisites:** natural-deduction proofs in FOL (∀E, ∃E, ¬E, ¬I, ⊥); truth values and interpretations; the idea of a valid argument.

## L2 — Key ideas
- The CQ rules are not basic. They can be derived from the chapter 36 rules (p. 330).
- ⊢ is proof-theoretic: some proof ends in C and its only undischarged assumptions are among the listed ones (p. 332).
- ⊨ is semantic: no valuation makes all premises true and C false (p. 332).
- Showing a theorem is easier than showing a validity; showing a non-validity is easier than showing a non-theorem (p. 333). (A theorem is a sentence with a proof from no assumptions; a validity is a sentence that no interpretation makes false.)
- Both notions agree: $A_1,\dots,A_n \vdash B$ iff $A_1,\dots,A_n \vDash B$. They are different notions but extensionally equivalent (p. 333).
- Four pairings follow: valid argument/provable conclusion, validity/theorem, equivalence/interderivability, joint satisfiability/joint consistency (p. 334).
- The table says which method is (usually) easier for each question (p. 335).
- The agreement is not an easy result; proving it marks the step to intermediate logic (p. 334).

## L3 — Walkthrough

### Chapter 40: Derived rules (pp. 330–331)
The CQ rules (chapter 38) should be regarded as derived. They can be derived from the basic rules of chapter 36, as with TFL in chapter 21 (p. 330).

**First CQ rule:** from $\forall x\,\neg A(x)$ infer $\neg\exists x\,A(x)$. The proof (p. 330):
1. $m$: $\forall x\,\neg A(x)$
2. $m+1$: assume $\exists x\,A(x)$ (AS)
3. $m+2$: assume $A(c)$ (AS)
4. $m+3$: $\neg A(c)$ by ∀E, $m$
5. $m+4$: $\bot$ by ¬E, $m+3$, $m+2$
6. $m+5$: $\bot$ by ∃E, $m+1$, $(m+2)$–$(m+4)$
7. $m+6$: $\neg\exists x\,A(x)$ by ¬I, $(m+1)$–$(m+5)$

**Third CQ rule:** from $\exists x\,\neg A(x)$ infer $\neg\forall x\,A(x)$. The proof (p. 331):
1. $m$: $\exists x\,\neg A(x)$
2. $m+1$: assume $\forall x\,A(x)$ (AS)
3. $m+2$: assume $\neg A(c)$ (AS)
4. $m+3$: $A(c)$ by ∀E, $m+1$
5. $m+4$: $\bot$ by ¬E, $m+2$, $m+3$
6. $m+5$: $\bot$ by ∃E, $m$, $(m+2)$–$(m+4)$
7. $m+6$: $\neg\forall x\,A(x)$ by ¬I, $(m+1)$–$(m+5)$

The text says similar justifications work for the other two CQ rules (p. 331).

*Intuition note:* A derived rule is one whose use can be justified by a proof from the basic rules, as the two proofs above do for two of the CQ rules.

### Chapter 41: Proofs and semantics (pp. 332–335)
**Two turnstiles (p. 332).**
- $A_1,\dots,A_n \vdash C$: some proof ends with C and its only undischarged assumptions are among the $A_i$. This is proof-theoretic.
- $A_1,\dots,A_n \vDash C$: no valuation (or interpretation) makes all $A_i$ true and C false. This is semantic.

The authors stress that these are different notions (p. 332). They are nevertheless deeply connected.

**Theorems versus validities (p. 333).**
- To show a sentence is a theorem, you only need to produce a proof and check each line. To show it is a validity, you must reason about all interpretations. So a theorem is easier to establish.
- To show a sentence is not a theorem, you must reason about all possible proofs, which is very hard. To show it is not a validity, you need only construct one interpretation making it false. So a non-validity is easier to establish.

**The agreement result (p. 333).** A sentence is a theorem iff it is a validity. So a proof of $\vdash A$ lets us infer $\vDash A$. A counter-interpretation showing $\nvDash A$ lets us infer $\nvdash A$. More generally:

$$A_1, A_2, \dots, A_n \vdash B \iff A_1, A_2, \dots, A_n \vDash B$$

Provability and entailment are different notions but extensionally equivalent (p. 333).

*Intuition note:* "Extensionally equivalent" means the two notions pick out exactly the same arguments. They are still defined in different ways: one by proofs, one by truth values.

**Consequences (p. 334).**
- An argument is valid iff its conclusion can be proved from its premises.
- A sentence is a validity iff it is a theorem.
- Two sentences are equivalent iff they are interderivable.
- Sentences are jointly satisfiable iff they are jointly consistent.

So you can pick whichever method is easier. The authors warn against being fooled by the similar symbols. The agreement is "not an easy result to come by", and proving it is where introductory logic becomes intermediate logic (p. 334).

**Table (p. 335).**

| Question | Yes: | No: |
|---|---|---|
| Is A a validity? | proof of $\vdash A$ | interpretation making A false |
| Is A a contradiction? | proof of $A\vdash\bot$ | interpretation making A true |
| Are A, B equivalent? | two proofs, $A\vdash B$ and $B\vdash A$ | interpretation giving A, B different truth values |
| Are $A_1,\dots,A_n$ jointly satisfiable? | interpretation making all true | proof of a contradiction from them |
| Is $A_1,\dots,A_n \therefore C$ valid? | proof from the $A_i$ to C | interpretation with all $A_i$ true, C false |

## Toy example (ours, not from the text)
Question 1: is $P \to Q$ a validity? Use the interpretation with $P$ true and $Q$ false. Then $P \to Q$ is false, so $\nvDash P\to Q$. By the equivalence, $\nvdash P \to Q$ as well, with no search through proofs.

Question 2: is $P \therefore P$ valid? The one-line proof (assume $P$, conclude $P$) gives $P \vdash P$. So $P \vDash P$. Check: with $P$ true, premise and conclusion are both true. With $P$ false, the premise is false. No valuation has a true premise and a false conclusion.

## Concepts
- [[derived-rule]] (new) — a rule whose use can be replaced by a proof from the basic rules (p. 330)
- [[proof-theoretic-consequence]] (new) — $\vdash$: a proof exists from the listed assumptions to the conclusion (p. 332)
- [[semantic-entailment]] (new) — $\vDash$: no interpretation makes the premises true and the conclusion false (p. 332)
- [[theorem-vs-validity]] (new) — a theorem is provable on no assumptions; a validity is true on every interpretation (p. 333)
- [[extensional-equivalence-of-⊢-and-⊨]] (new) — the two notions hold for exactly the same arguments, though defined differently (p. 333)
- [[validity / soundness]] — the text states, as a consequence of the agreement of ⊢ and ⊨, that an argument is valid iff its conclusion can be proved from its premises (p. 334)

## Canonical instances
- [[CQ-rule-derivation]] — the first and third CQ rules derived from basic rules (pp. 330–331)
- [[easier-method-table]] — which of proof or interpretation answers each logical question (p. 335)

## Bridges (candidates)
- [structural-analogy] Proof vs. counter-interpretation ↔ computer science: certificate checking (a witness is easy to check, hard to find) — the text says each method is easy to check once found (p. 333).

## Questions this raises
- How is the agreement of ⊢ and ⊨ actually proved?
- Why is it easy to check a proof but hard to find one?
- Does the agreement depend on the particular proof rules chosen?

## Exercises worth doing
- Ex. A (p. 331) — prove the second and fourth CQ rules from basic rules, following the pattern of the two given proofs — difficulty: medium

## Reading notes
- Printed = pdf − 10. This unit covers all of ch. 40 and ch. 41.
- The text layer of the p. 335 table was readable; no page image was provided for it, so the table is taken from the text layer.
- The text says "validities" and "theorems" for sentences, and writes "valuation (or interpretation)" (p. 332) and "valuations/interpretations" (p. 334).
- No misprints noticed.
