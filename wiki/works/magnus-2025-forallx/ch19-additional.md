---
id: magnus-2025-forallx/ch19-additional
work: magnus-2025-forallx
unit: 19 Additional rules for TFL
pages: 162-169
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
# Additional rules for TFL

## L0 — One line
The chapter adds extra rules (DS, MT, DNE, LEM, De Morgan) to the TFL proof system, which makes it "a bit easier to work with"; chapter 21 will show they are not strictly speaking necessary (p. 162).

## L1 — The gist (≤ 120 words)
Chapter 17 gave the basic proof rules for TFL. This chapter adds five groups of extra rules to make the system "a bit easier to work with": disjunctive syllogism, modus tollens, double-negation elimination, excluded middle (a case-split on A and ¬A), and four De Morgan rules. DS, MT and LEM are motivated by natural-language examples, DNE by how double negations tend to cancel in English, LEM also as ∨E applied to A ∨ ¬A, and the De Morgan rules by their shape being familiar from truth tables. The authors say that chapter 21 will show these rules are not strictly necessary (p. 162). The chapter ends with exercises: adding citations to proofs, and building proofs.

**Prerequisites:** TFL connectives (∧, ∨, ¬, →, ↔, ⊥); the basic rules of chapter 17 (PR, AS, ∧I, ∨I, →E, ∨E, R); subproofs.

## L2 — Key ideas (5–10 bullets)
- The extended system is easier to use; chapter 21 will show the new rules are not strictly necessary (p. 162).
- DS: from a disjunction and the negation of one disjunct, infer the other disjunct (p. 163).
- MT: from A → B and ¬B, infer ¬A (p. 164).
- DNE: from ¬¬A, infer A. English double negations can fail to cancel, and TFL drops that nuance (p. 164).
- LEM: if B follows from A and also from ¬A, then B follows. It can be thought of as ∨E applied to A ∨ ¬A (p. 165).
- Four De Morgan rules move negation across ∧ and ∨ in both directions (p. 167).
- In DS the disjunction and the negation may come in either order and need not be adjacent; in MT the premises may come in either order. In both, the disjunction (DS) or conditional (MT) is cited first (pp. 163–164).

## L3 — Walkthrough

**Intro.** Chapter 17 gave the basic rules. This chapter adds rules that make the system "a bit easier to work with", though chapter 21 will show they are not strictly speaking necessary (p. 162).

**19.1 Disjunctive syllogism (DS).** Example: "Elizabeth is in Massachusetts or in DC; she is not in DC; so she is in Massachusetts" (p. 162). Two forms (p. 163):
- from $\mathcal{A}\lor\mathcal{B}$ (line m) and $\neg\mathcal{A}$ (line n), infer $\mathcal{B}$ by DS, m, n;
- from $\mathcal{A}\lor\mathcal{B}$ and $\neg\mathcal{B}$, infer $\mathcal{A}$.

The disjunction and the negation may come in either order and need not be adjacent. The disjunction is always cited first (p. 163).

*Intuition note:* If one of two options is ruled out, the other must hold. DS just writes this down as one step.

**19.2 Modus tollens (MT).** Example: "If Hilary has won, she is in the White House; she is not there; so she has not won" (p. 163). Rule: from $\mathcal{A}\to\mathcal{B}$ (m) and $\neg\mathcal{B}$ (n), infer $\neg\mathcal{A}$ by MT, m, n. The premises may be in either order; the conditional is cited first (p. 164).

*Intuition note:* If A would guarantee B, but B is false, then A cannot be true.

**19.3 Double-negation elimination (DNE).** From $\neg\neg\mathcal{A}$ (m), infer $\mathcal{A}$ by DNE, m (p. 164). Justification: in natural language, double negations tend to cancel out. Caveat: context and emphasis can block this. "Jane is not *not* happy" — arguably one cannot infer "Jane is happy", since the sentence should be understood as meaning "Jane is not *un*happy", which is compatible with "Jane is in a state of profound indifference". Moving to TFL sacrifices such nuances (p. 164).

**19.4 Excluded middle (LEM).** Motivating case: if it is sunny, Bill brought an umbrella; if it is not sunny, Bill brought an umbrella; there is no third weather, so he brought one whatever the weather (pp. 164–165). Rule (p. 165):
- subproof 1: assume $\mathcal{A}$ (AS) and derive $\mathcal{B}$ (lines i–j);
- subproof 2: assume $\neg\mathcal{A}$ (AS) and derive $\mathcal{B}$ (lines k–l);
- conclude $\mathcal{B}$ by LEM, i–j, k–l.

It can be seen as ∨E applied to $\mathcal{A}\lor\neg\mathcal{A}$. Each subproof may have any number of lines. The subproofs may come in either order, and the second need not follow the first immediately (p. 165).

Example 1: $P \therefore (P\land D)\lor(P\land\neg D)$ (pp. 165–166).
1. $P$ PR
2. $D$ AS
3. $P\land D$ ∧I, 1, 2
4. $(P\land D)\lor(P\land\neg D)$ ∨I, 3
5. $\neg D$ AS
6. $P\land\neg D$ ∧I, 1, 5
7. $(P\land D)\lor(P\land\neg D)$ ∨I, 6
8. $(P\land D)\lor(P\land\neg D)$ LEM, 2–4, 5–7

Example 2: $A\to\neg A \therefore \neg A$ (p. 166).
1. $A\to\neg A$ PR
2. $A$ AS
3. $\neg A$ →E, 1, 2
4. $\neg A$ AS
5. $\neg A$ R, 4
6. $\neg A$ LEM, 2–3, 4–5

*Intuition note:* A or not-A always covers every case. If the same result follows in both cases, it follows outright.

**19.5 De Morgan rules (DeM).** Named after Augustus De Morgan; their shape "should be familiar from truth tables" (p. 166). All four take one line m and cite DeM, m (p. 167):
1. $\neg(\mathcal{A}\land\mathcal{B}) \Rightarrow \neg\mathcal{A}\lor\neg\mathcal{B}$
2. $\neg\mathcal{A}\lor\neg\mathcal{B} \Rightarrow \neg(\mathcal{A}\land\mathcal{B})$ (reverse of 1)
3. $\neg(\mathcal{A}\lor\mathcal{B}) \Rightarrow \neg\mathcal{A}\land\neg\mathcal{B}$ (the dual of 1)
4. $\neg\mathcal{A}\land\neg\mathcal{B} \Rightarrow \neg(\mathcal{A}\lor\mathcal{B})$ (reverse of 3)

These are all the additional rules (p. 167).

*Intuition note:* Negating "both" is the same as "at least one fails". Negating "either" is the same as "both fail".

**Practice exercises (pp. 167–169).** A: add missing citations to three given proofs. B: prove four arguments (listed below).

## Toy example (ours)
Argument: $P\lor Q,\ \neg P\to R,\ \neg R \therefore Q$.
1. $P\lor Q$ PR
2. $\neg P\to R$ PR
3. $\neg R$ PR
4. $\neg\neg P$ MT, 2, 3 (from $\neg P\to R$ and $\neg R$)
5. $P$ DNE, 4
6. Q cannot be obtained from $P$ alone, so this is a bad path: DS needs $\neg P$, not $P$.

Result: this argument is not valid. Check with the truth table: let $P$ = T, $Q$ = F, $R$ = F. Premise 1 is T (P is T). Premise 2, $\neg P\to R$, has a false antecedent (¬P is F), so it is T. Premise 3, ¬R, is T. The conclusion Q is F. All premises are true and the conclusion is false, so the argument is invalid. The lesson is that DS removes a disjunct only when you have its negation.

## Concepts

- [[disjunctive-syllogism]] (new) — from A ∨ B and the negation of one disjunct, infer the other (p. 163)
- [[modus-tollens]] (new) — from A → B and ¬B, infer ¬A (p. 164)
- [[double-negation-elimination]] (new) — from ¬¬A infer A; English double negation may not always cancel (p. 164)
- [[excluded-middle-rule]] (new) — derive B from subproofs assuming A and assuming ¬A (p. 165)
- [[de-morgan-rules]] (new) — four rules relating ¬(A∧B) to ¬A∨¬B and ¬(A∨B) to ¬A∧¬B (p. 167)

## Canonical instances
- [[elizabeth-massachusetts-dc]] — example of disjunctive syllogism (p. 162)
- [[hilary-white-house]] — example of modus tollens (p. 163)
- [[jane-not-not-happy]] — double negation not cancelling in English (p. 164)
- [[bill-umbrella]] — case reasoning behind excluded middle (pp. 164–165)

## Bridges (candidates)
- [same-math] De Morgan rules ↔ Boolean algebra / set theory: complement of an intersection equals the union of complements — same laws for ∧/∨ and ∩/∪ (the text only says the shape is "familiar from truth tables", p. 166).
- [structural-analogy] LEM subproofs ↔ proof by cases in mathematics: same shape, split into exhaustive cases and show the same result in each.

## Questions this raises
- Why are these rules "not strictly speaking necessary" (chapter 21)? How are they derived from the basic rules?
- When English "not not" differs from "is", what is lost in translating to TFL?
- Is LEM acceptable if one doubts that every sentence is either true or false?

## Exercises worth doing
- Ex. A.1–A.3 (pp. 168–169) — cite rules and lines in given proofs; builds fluency in DS, DNE, DeM, ⊥ steps — easy
- Ex. B.1 (p. 169) — $E\lor F, F\lor G, \neg F \therefore E\land G$; practice with DS — easy
- Ex. B.2 (p. 169) — $M\lor(N\to M)\therefore \neg M\to\neg N$; combining DS/MT or LEM — medium
- Ex. B.3 (p. 169) — $(M\lor N)\land(O\lor P), N\to P, \neg P\therefore M\land O$; MT then DS — medium
- Ex. B.4 (p. 169) — $(X\land Y)\lor(X\land Z), \neg(X\land D), D\lor M\therefore M$; De Morgan and DS — medium

## Reading notes
- Printed page = pdf − 10.
- Exercise A proofs on pp. 168–169 are printed without citations; line 6 in A.2 is ⊥, as shown in the images. The page layout of A.3 (nested subproofs) is clear in the image.
- The toy example above is ours; it shows an invalid argument on purpose and is not from the source.
