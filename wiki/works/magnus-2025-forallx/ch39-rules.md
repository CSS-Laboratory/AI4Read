---
id: magnus-2025-forallx/ch39-rules
work: magnus-2025-forallx
unit: "38 Conversion of quantifiers; 39 Rules for identity"
pages: 323-329
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Conversion of quantifiers (ch. 38) and Rules for identity (ch. 39)

## L0 — One line
The proof system gets rules linking quantifiers with negation (CQ), plus an introduction rule (=I) and an elimination rule (=E, Leibniz's Law) for identity.

## L1 — The gist (≤ 120 words)
How can proofs handle negated quantifiers and identity? Chapter 38 adds four CQ rules that swap a negation and a quantifier. Chapter 39 adds =I, which lets you write c = c on any line with no premises. It also adds =E, which lets you swap names between identical objects. No identity-free sentences can justify an identity between two different names, so =I allows only c = c. From these rules the book proves that identity is symmetric and transitive. The exercises then ask for proofs about identity-based symbolizations of "Nick is the F" and "there is exactly one F".

**Prerequisites:** the basic proof rules for connectives and quantifiers (∀I, ∃I, →I, ∧E); symbolizing with FOL; ¬∃ and ∀¬ equivalence (ch. 23).

## L2 — Key ideas (5–10 bullets)
- Four CQ rules convert between ∀x¬A and ¬∃xA, and between ∃x¬A and ¬∀xA, in both directions (pp. 323–324).
- Prenex normal form means all quantifiers stand at the start of a sentence; the quantifier-moving equivalences are sometimes called prenexing rules (p. 325).
- No sentence without the identity predicate can justify an inference to "a = b" (p. 326).
- So =I is premise-free and only gives c = c (pp. 326–327).
- =E (Leibniz's Law) lets you replace some or all occurrences of one name by an identical name; the identity line is cited first (p. 327).
- Symmetry of identity is proved by assuming a = b, writing a = a with =I, then applying =E (p. 328).
- Transitivity is proved by assuming a = b ∧ b = c and applying =E to the two conjuncts (p. 328).
- Exercises ask for proofs involving identity, including a proof that three symbolizations of "there is exactly one F" can each be derived from the others (p. 329).

## L3 — Walkthrough

### Chapter 38: Conversion of quantifiers
- The chapter adds rules to the basic rules, governing how quantifiers interact with negation. It builds on the equivalence of ¬∃xA and ∀x¬A noted in chapter 23 (p. 323).
- Four rules are added, each justified "CQ, m" (a single line m as premise). The rules are: from ∀x¬A infer ¬∃xA; from ¬∃xA infer ∀x¬A (p. 323); from ∃x¬A infer ¬∀xA; from ¬∀xA infer ∃x¬A (p. 324).
- **Intuition note:** "Nothing is A" and "everything is not-A" say the same. "Something is not-A" and "not everything is A" also say the same. The rules let a proof move between these forms in one step.
- Note on chapter 24 equivalences: the variable x does not occur in G(a). When all quantifiers are at the start of a sentence, it is in *prenex normal form*. The equivalences of ch. 24 are sometimes called prenexing rules because they let us put any sentence into that form (p. 325).
- Practice (p. 324): A. Show four sets inconsistent. B. Show two pairs interderivable (derivable from each other). C. Show six pairs interderivable, for example ∀x(F(x) ∧ G(a)) and ∀xF(x) ∧ G(a).

### Chapter 39: Rules for identity
- **Why =I is limited.** The identity of indiscernibles says that objects indiscernible in every way are identical. The book does not subscribe to it (p. 326). So however much you learn about two objects, you cannot prove them identical. The exception is learning that they are identical, which gives a hardly illuminating proof (p. 326).
- The general point: no sentences lacking the identity predicate could justify an inference to "a = b". So =I cannot yield an identity with two different names (p. 326).
- **=I.** Every object is identical to itself, so no premises are needed. For any name c, you may write c = c on any line, justified only by =I, with no reference to earlier lines (pp. 326–327).
- **=E.** If a = b is established, anything true of the object named by a is true of the object named by b. So in a sentence containing a, you can replace some or all occurrences of a with b and get an equivalent sentence. Example: from R(a,a) and a = b you may infer R(a,b), R(b,a) or R(b,b) (p. 327).
- Rule form: from m: a = b and n: A(…a…a…), infer A(…b…a…), with =E, m, n. The notation is as for ∃I. Lines m and n may come in either order and need not be adjacent, but the identity statement is always cited first (p. 327).
- The symmetric form: from m: a = b and n: A(…b…b…), infer A(…a…b…) (p. 327). This rule is sometimes called *Leibniz's Law* (p. 327).
- **Intuition note:** If two names point to one object, anything said with one name stays true when you use the other. That is all =E does. =I only records that a thing is itself.

**Proof that identity is symmetric** (p. 328):

| line | formula | justification |
|---|---|---|
| 1 | a = b | AS |
| 2 | a = a | =I |
| 3 | b = a | =E, 1, 2 |
| 4 | a = b → b = a | →I, 1–3 |
| 5 | ∀y(a = y → y = a) | ∀I, 4 |
| 6 | ∀x∀y(x = y → y = x) | ∀I, 5 |

Line 3 comes from replacing one instance of a in line 2 by b, which a = b allows (p. 328).

**Proof that identity is transitive** (p. 328):

| line | formula | justification |
|---|---|---|
| 1 | a = b ∧ b = c | AS |
| 2 | a = b | ∧E, 1 |
| 3 | b = c | ∧E, 1 |
| 4 | a = c | =E, 2, 3 |
| 5 | (a = b ∧ b = c) → a = c | →I, 1–4 |
| 6 | ∀z((a = b ∧ b = z) → a = z) | ∀I, 5 |
| 7 | ∀y∀z((a = y ∧ y = z) → a = z) | ∀I, 6 |
| 8 | ∀x∀y∀z((x = y ∧ y = z) → x = z) | ∀I, 7 |

Line 4 comes from replacing b in line 3 by a, which a = b allows (p. 328).
- **Intuition note:** In both proofs one assumes the identity for named objects, derives the conclusion, and then generalizes. The assumption is discharged with →I and the names are generalized with ∀I (p. 328).

### Practice (p. 329, with p. 328)
- A. Ten proofs, from P(a) ∨ Q(b), Q(b) → b = c, ¬P(a) ⊢ Q(c) up to ⊢ P(a) → ∀x(P(x) ∨ ¬x = a).
- B. Show ∃x([F(x) ∧ ∀y(F(y) → x = y)] ∧ x = n) and F(n) ∧ ∀y(F(y) → n = y) are interderivable. The exercise also asks students to conclude from this that both have a decent claim to symbolize "Nick is the F".
- C. Show the three symbolizations of "there is exactly one F" from chapter 26 are interderivable. Hint: it suffices to show 1 proves 2, 2 proves 3, 3 proves 1.
- D. Symbolize and prove: exactly one F; exactly one G; nothing is both; therefore exactly two things are F or G.

## Toy example (ours)
Premises: 1. a = b; 2. R(a,a). Goal: R(b,b).
- 3. R(b,a): from line 2, replace the first a with b (=E, 1, 2).
- 4. R(b,b): from line 3, replace the remaining a with b (=E, 1, 3).
Each step replaces one occurrence, which the rule allows. Line 1 is cited first each time.

## Concepts
- [[prenex-normal-form]] (new) — all quantifiers at the start of a sentence (p. 325)
- [[quantifier-conversion-CQ]] (new) — rules swapping negation and quantifier: ¬∃ ↔ ∀¬, ¬∀ ↔ ∃¬ (pp. 323–324)
- [[identity-introduction]] (new) — premise-free rule giving c = c (p. 326)
- [[identity-elimination-leibniz-law]] (new) — if a = b, swap names in a sentence (p. 327)
- [[identity-of-indiscernibles]] (new) — the thesis that objects indiscernible in every way are identical; the book does not subscribe to it (p. 326)
- [[interderivable]] (new) — each of two sentences can be proved from the other (term used in exercises B and C, not defined on these pages; p. 324)

## Canonical instances
- [[identity-symmetry-proof]] — a = b ⊢ b = a, then generalized (p. 328)
- [[identity-transitivity-proof]] — proved with =E on two conjuncts (p. 328)
- [[nick-is-the-F]] — identity-based symbolization of the English sentence "Nick is the F" (p. 329)

## Bridges (candidates)
- [structural-analogy] =E (replacing identical names) ↔ analytic-philosophy: the substitution of co-referring names, as in Frege's puzzle — both turn on which substitutions keep truth.
- [same-math] CQ rules ↔ logic: duality of ∀ and ∃ — ¬∃ ≡ ∀¬ is the same equivalence.

## Questions this raises
- If =I only gives c = c, how can any proof ever establish an identity between different names?
- Why is the three-way hint (1⊢2, 2⊢3, 3⊢1) enough to show interderivability?
- Why must replacements keep the identity line cited first, and what goes wrong if names are replaced in a quantified formula?

## Exercises worth doing
- Ch. 38 B.1 (p. 324) — links ∀→¬ with ¬∃∧ using CQ — difficulty: easy
- Ch. 38 C.4 (p. 324) — ∀(F→G(a)) vs ∃F→G(a), moving quantifiers across a conditional — difficulty: medium
- Ch. 39 A.1 (p. 328) — a basic =E proof with disjunction — difficulty: easy
- Ch. 39 A.6 (p. 329) — derive that two things differ from J and ¬J — difficulty: medium
- Ch. 39 C (p. 329) — "exactly one F" forms are interderivable — difficulty: hard
- Ch. 39 D (p. 329) — symbolize and prove an "exactly two" argument — difficulty: hard

## Reading notes
- Printed = pdf − 10. The source unit includes ch. 38 (printed 323–325) and ch. 39 (printed 326–329).
- Exercise lists in the text layer are garbled in places (A.8 and A.9 of ch. 39, and the bracket placement in B and C); I followed the page images.
- The unit's proofs use the tags AS, =I, =E, ∀I, →I, ∧E as printed. No solutions appear on these pages.
