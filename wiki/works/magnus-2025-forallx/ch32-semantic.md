---
id: magnus-2025-forallx/ch32-semantic
work: magnus-2025-forallx
unit: "32 Semantic concepts"
pages: 277-280
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Semantic concepts (FOL entailment, validity, expressibility)

## L0 — One line
In FOL, the logical notions (entailment, validity, equivalence, satisfiability) are defined by quantifying over interpretations (all of them, or some), and formulas with free variables can express relations that have no predicate symbol of their own.

## L1 — The gist (≤ 120 words)
Once truth in FOL is defined, the logical notions of TFL can be restated with interpretations in place of valuations. A sentence is a validity if it is true in every interpretation, and a contradiction if it is false in every one. An argument is valid if no interpretation makes the premises true and the conclusion false. The chapter then extends satisfaction to pairs of objects. This shows that formulas with two free variables can express relations, such as having a teacher in common, that the symbolization key does not list. In some cases such a formula can be used to symbolize English sentences that use the missing predicate.

**Prerequisites:** FOL = first-order logic, TFL = truth-functional logic; FOL syntax (predicates, quantifiers, free variables, i.e. variables not bound by a quantifier); an interpretation fixes a domain and the meanings of names and predicates (see the example on p. 279); an object satisfies a formula with one free variable (section 31.3); "interpretation" and truth in FOL (ch. 31); TFL notions of entailment and tautology (ch. 12).

## L2 — Key ideas (5–10 bullets)
- Entailment in FOL, $A_1,\dots,A_n \vDash C$, means no interpretation makes all premises true and $C$ false (p. 277).
- $\vDash A$ means $A$ is true in every interpretation (p. 277).
- Validity, contradiction, valid argument, equivalence and joint satisfiability are all defined by quantifying over interpretations (p. 278).
- Validities are to FOL what tautologies are to TFL (p. 278).
- Satisfaction extends from one object to pairs of objects, via a formula with two free variables (p. 278).
- Satisfaction applies to atomic, non-atomic and quantified formulas (p. 279).
- Swapping variables or adding quantifiers yields new relations, e.g. born after, having a teacher in common (p. 279).
- Sometimes such a formula can symbolize English sentences that use a predicate with no dedicated symbol (p. 280).

## L3 — Walkthrough

### 32.1 Validities, entailment, etc. (pp. 277–278)
The definitions look like those for TFL (chapter 12), but they concern interpretations, not valuations (p. 277).

- **Entailment:** $A_1, A_2, \dots, A_n \vDash C$ iff there is no interpretation in which all of $A_1,\dots,A_n$ are true and $C$ is false (p. 277).
- $\vDash A$ means $A$ is true in every interpretation (p. 277).
- **Validity** (of a sentence): $A$ is true in every interpretation, i.e. $\vDash A$ (p. 278).
- **Contradiction:** $A$ is false in every interpretation, i.e. $\vDash \neg A$ (p. 278).
- **Valid argument:** $A_1,\dots,A_n \therefore C$ is valid in FOL iff no interpretation makes all premises true and the conclusion false, i.e. $A_1,\dots,A_n \vDash C$. Otherwise it is invalid in FOL (p. 278).
- **Equivalence:** $A$ and $B$ are equivalent iff they are true in exactly the same interpretations, i.e. $A \vDash B$ and $B \vDash A$ (p. 278).
- **Joint satisfiability:** $A_1,\dots,A_n$ are jointly satisfiable iff some interpretation makes all of them true. They are jointly unsatisfiable iff there is no such interpretation (p. 278).

The authors note that "validity" is the standard term here. Validities are to FOL what tautologies are to TFL (p. 278).

*Intuition note:* For TFL the notions concern valuations; for FOL they concern interpretations. Validity, contradiction, entailment and equivalence talk about all interpretations; joint satisfiability talks about some interpretation.

### 32.2 Expressibility (pp. 278–280)
**Satisfaction by pairs.** Take a formula $A(x,y)$ with two free variables. A pair $\langle a,b\rangle$ satisfies it iff $A(c,d)$ is true in the interpretation extended by two names $c$, $d$, where $c$ names $a$ and $d$ names $b$ (p. 278).

Example: $\langle$Socrates, Plato$\rangle$ satisfies $R(x,y)$, because $R(c,d)$ is true in this interpretation (pp. 278–279):

- domain: all people born before 2000 CE
- $a$: Aristotle; $b$: Beyoncé; $c$: Socrates; $d$: Plato
- $P(x)$: $x$ is a philosopher
- $R(x,y)$: $x$ was born before $y$

For atomic formulas, what satisfies them is exactly the extension (the set of objects or tuples the predicate applies to) given in the interpretation (p. 279). Satisfaction also applies to:

- non-atomic formulas: $P(x)\land R(x,b)$ is satisfied by all philosophers born before Beyoncé (p. 279);
- quantified formulas: $P(x)\land\neg\exists y\,(P(y)\land R(y,x))$ is satisfied by philosophers for whom no philosopher was born before them, i.e. the first philosopher (p. 279).

**Expressing relations.**
- $R(x,y)$ expresses "$x$ was born before $y$", since that is how its extension was specified (p. 279).
- $R(y,x)$: the pair $\langle y,x\rangle$ satisfies $R(y,x)$ iff the reverse pair $\langle x,y\rangle$ satisfies $R(x,y)$. So $R(y,x)$ expresses "$x$ was born after $y$" (p. 279).
- Add $T(x,y)$: $x$ was a teacher of $y$. Then $\exists z\,(T(z,x)\land T(z,y))$ is satisfied by $x$ and $y$ iff some person $z$ taught both. It expresses "$x$ and $y$ have a teacher in common" (p. 279).
- $\forall z\,(T(x,z)\leftrightarrow T(y,z))$ expresses "$x$ and $y$ taught the same people" (p. 279).

**Take-home message:** some English predicates can sometimes be expressed in an interpretation even with no predicate symbol for them. If so, a formula that expresses them, such as $\exists z\,(T(z,x)\land T(z,y))$, can symbolize English sentences using the predicate (pp. 279–280).

*Intuition note:* A formula with free variables is like a blank-filled sentence "___x … ___y". Any pair that makes it true satisfies it. Combining basic predicates with connectives and quantifiers builds new relations.

## Toy example (ours)
Domain: $\{1,2,3\}$; $L(x,y)$: $x$ is less than $y$.
- Formula $\exists z\,(L(x,z)\land L(z,y))$ (something lies strictly between $x$ and $y$).
- Pair $\langle1,3\rangle$: take $z=2$; $L(1,2)$ and $L(2,3)$ are both true, so the pair satisfies it.
- Pair $\langle1,2\rangle$: $z=1$ fails ($L(1,1)$ false), $z=2$ fails ($L(2,2)$ false), $z=3$ fails ($L(3,2)$ false). So the pair does not satisfy it.
- Contradiction check: $\exists x\,L(x,x)$ is false in this interpretation, but true in another (e.g. $L$ read as equality on the same domain), so it is not false in every interpretation, hence not a contradiction.

## Concepts
- [[validity / soundness]] — here a *sentence* is a validity if true in every interpretation; an argument is valid if no interpretation makes premises true and conclusion false (p. 278)
- [[entailment-fol]] (new) — $A_1,\dots,A_n \vDash C$: no interpretation makes all premises true and $C$ false (p. 277)
- [[contradiction-fol]] (new) — a sentence false in every interpretation (p. 278)
- [[logical-equivalence-fol]] (new) — true in exactly the same interpretations (p. 278)
- [[joint-satisfiability]] (new) — some interpretation makes all the sentences true (p. 278)
- [[satisfaction-by-tuples]] (new) — a pair (or tuple) of objects satisfies a formula via added names for them (p. 278)
- [[expressibility]] (new) — a formula with free variables can express a relation lacking its own predicate symbol (p. 279)

## Canonical instances
- [[teacher-in-common]] — $\exists z(T(z,x)\land T(z,y))$ expresses having a teacher in common (p. 279)
- [[first-philosopher]] — $P(x)\land\neg\exists y(P(y)\land R(y,x))$ is satisfied by the first philosopher (p. 279)

## Bridges (candidates)
- [structural-analogy] FOL validity (true in every interpretation) ↔ TFL: tautology (true in every valuation) — same role, different semantic base.
- [structural-analogy] formula with free variables expressing a relation ↔ database queries (not in this unit): a query defines a relation from base tables.

## Questions this raises
- Can we check "true in every interpretation" mechanically, given infinitely many interpretations?
- Are there relations that no FOL formula can express in a given interpretation?
- How does symbolizing with a complex formula differ from adding a new predicate symbol?

## Exercises worth doing
- Ex. A.1–A.4 (p. 280) — express "older than", "mother of", "siblings", "brother of" using $Y,O,W,M$ — difficulty: medium
- Ex. B.1 (p. 280) — "Alex and Dana are sisters" — difficulty: medium
- Ex. B.2 (p. 280) — "Fathers are older than their children" — difficulty: medium
- Ex. B.3 (p. 280) — "Alex's parents are the same age" — difficulty: hard

## Reading notes
- Printed page = pdf − 10.
- In the page images, the blanks in predicates are underlined spaces with subscripts $x$, $y$; the text layer shows only spaces.
- The Toy example and the two intuition notes are the digest's own glosses, not source text.
