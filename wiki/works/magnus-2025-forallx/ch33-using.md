---
id: magnus-2025-forallx/ch33-using
work: magnus-2025-forallx
unit: "33 Using interpretations"
pages: 281-288
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
# Using interpretations

## L0 — One line
To show that a first-order sentence or argument fails a logical test, build one interpretation (a counter-model) in which the right sentences are true or false.

## L1 — The gist (≤ 120 words)
The chapter asks how to show that a sentence of first-order logic (FOL) is not a validity, not a contradiction, or not equivalent to another sentence, and how to show that an argument is invalid. The answer is the same each time: find a single suitable interpretation. Start with a small domain, then choose names and predicates so that the required sentences get the required truth values. Such an interpretation is a counter-model. The method shows that an FOL entailment fails. It shows that an English argument is invalid only if one can argue that nothing important is lost in the FOL symbolization. This matters because each "not a validity", "not equivalent" or "invalid" claim can be backed by one small, checkable interpretation.

**Prerequisites:** FOL syntax (quantifiers, names, predicates, identity); the idea of an interpretation (domain, referents, extensions); validity, entailment, equivalence and joint satisfiability.

## L2 — Key ideas
- To show A is not a validity, find an interpretation where A is false (p. 282).
- To show A is not a contradiction, find an interpretation where A is true (p. 282).
- To show A and B are not logically equivalent, find an interpretation where one is true and the other false (p. 283).
- Keep the domain small, because that makes extensions easy to specify (pp. 281, 283). For ∀x S(x) versus ∃x S(x), at least two objects are needed (p. 283).
- Entailment, validity and satisfiability tests typically need an interpretation that fixes the truth values of several sentences at once (p. 284).
- One counter-model gives three results: the argument is invalid, entailment fails, and premises plus the negated conclusion are jointly satisfiable (p. 286).
- Diagram interpretations (arrows for a relation) can show many sentences jointly satisfiable (pp. 285–286).
- A counter-model to an FOL entailment does not by itself show the English argument invalid; one must argue that nothing important is lost in the symbolization (p. 287).

## L3 — Walkthrough

### 33.1 Validities and contradictions
- **Goal:** show ‘∃x A(x,x) → B(d)’ is not a validity, i.e. false in some interpretation (p. 281).
- A conditional is false when its antecedent is true and its consequent false (p. 281).
- **Construction:**
  - Domain: Paris only (a small domain makes extensions easy to specify). Then d: Paris is forced (pp. 281–282).
  - A(x,y): x is identical with y. So A(d,d) is true, hence ∃x A(x,x) is true (p. 282).
  - B(x): x is in Germany. So B(d) is false (p. 282).
  - So the conditional is false here, and is not a validity (p. 282).
- **Not a contradiction:** keep everything but change B(x) to "x is in France". Then B(d) is true, so the conditional is true (p. 282).
- Rules: to show A is not a validity, it suffices to find an interpretation where A is false. To show A is not a contradiction, it suffices to find one where A is true (p. 282).

*Intuition note:* "Always true" can be refuted by one false case. "Never true" can be refuted by one true case.

### 33.2 Logical equivalence
- **Goal:** show ∀x S(x) and ∃x S(x) are not equivalent. We need an interpretation giving them different truth values (p. 283).
- A one-member domain gives them the same truth value, so at least two objects are needed (p. 283).
- **Construction:** domain: Ornette Coleman, Miles Davis. S(x): x plays saxophone (p. 283).
  - ∃x S(x) is true. Extend the interpretation with c naming Coleman. S(c) is true there, so ∃x S(x) was true in the original (p. 283).
  - ∀x S(x) is false. Extend it with d naming Davis. S(d) is false there, so ∀x S(x) was false in the original (p. 283).
- This is a counter-interpretation to the claim of equivalence (p. 283).
- Rule: to show A and B are not logically equivalent, it suffices to find an interpretation where one is true and the other false (p. 283).

### 33.3 Validity, entailment and satisfiability
**Example 1:** ∃x(G(x) → G(a)) ∴ ∃x G(x) → G(a) (p. 284).
- We need the premise true and the conclusion false. The conclusion is false when ∃x G(x) is true and G(a) is false, so two objects are needed (p. 284).
- Interpretation: domain Karl Marx, Ludwig von Mises; G(x): x hated communism; a: Marx (p. 284).
  - G(a) is false. ∃x G(x) is true, because of von Mises. So the conclusion is false (p. 284).
  - G(a) → G(a) is true (indeed a validity), so ∃x(G(x) → G(a)) is true. The premise is true (p. 284).
- Hence the argument is invalid. Also ∃x(G(x) → G(a)) ⊭ ∃x G(x) → G(a), and ∃x(G(x) → G(a)) and ¬(∃x G(x) → G(a)) are jointly satisfiable (p. 284).

**Example 2:** ∀x∃y L(x,y) ∴ ∃y∀x L(x,y) (p. 284).
- Domain: Canadian citizens currently in a domestic partnership with another Canadian citizen. L(x,y): x is in a domestic partnership with y (p. 285).
- The premise is true: each member's partner is also in the domain (p. 285).
- The conclusion is false: it would need one person partnered with everyone in the domain, and there is none (p. 285).
- So the argument is invalid. ∀x∃y L(x,y) does not entail ∃y∀x L(x,y). ∀x∃y L(x,y) and ¬∃y∀x L(x,y) are jointly satisfiable (p. 285).

**Example 3 (diagram, using chapter 30's conventions):** domain {1,2,3}. R(x,y) is true iff the diagram has an arrow from x to y. The arrows are 1→1 (a loop), 1→2, 1→3 and 2→3 (p. 285).
Six sentences are true, with witnesses (pp. 285–286):
- ∀x∃y R(y,x)
- ∃x∀y R(x,y) (witness 1)
- ∃x∀y(R(y,x) ↔ x = y) (witness 1)
- ∃x∃y∃z((¬y = z ∧ R(x,y)) ∧ R(z,x)) (witness 2)
- ∃x∀y¬R(x,y) (witness 3)
- ∃x(∃y R(y,x) ∧ ¬∃y R(x,y)) (witness 3)

So these six are jointly satisfiable. This generates invalid arguments, e.g. ∀x∃y R(y,x), ∃x∀y R(x,y) ∴ ∀x∃y R(x,y) (p. 286). The author also lists ∃x∀y R(x,y), ∃x∀y¬R(x,y) ∴ ¬∃x∃y∃z(¬y = z ∧ (R(x,y) ∧ R(z,x))) (p. 286).

**Summary box:** if some interpretation makes A₁,…,Aₙ true and C false, then (1) A₁,…,Aₙ ∴ C is invalid; (2) A₁,…,Aₙ ⊭ C; (3) A₁,…,Aₙ, ¬C are jointly satisfiable (p. 286). An interpretation that refutes a claim is a *counter-interpretation* or *counter-model* (p. 286).

*Intuition note:* One picture of the world with true premises and a false conclusion refutes the argument form. It also shows that "premises plus denied conclusion" can be true together.

**Caution (pp. 286–287):**
- FOL is extensional, ignores vagueness, and cannot handle validity for "special reasons" (p. 286).
- "Every fox is cute. ∴ All vixens are cute." is conceptually valid: necessarily every vixen is a fox (p. 286).
- A sensible symbolization is ∀x(F(x) → C(x)) ∴ ∀x(V(x) → C(x)). Counter-models to its entailment are easy to find (the author leaves this as an exercise) (p. 287).
- So it would be wrong to infer that the English argument is invalid. To infer invalidity from a missing FOL entailment, one must argue that nothing important is lost in the symbolization (p. 287).

*Intuition note:* A counter-model refutes the symbolized argument. Whether it refutes the English one depends on the symbolization.

## Toy example (ours, not from the text)
Show ∃x P(x), ∃x Q(x) ∴ ∃x(P(x) ∧ Q(x)) is invalid.
- Domain: {1, 2}. P(x): x is odd. Q(x): x is even.
- ∃x P(x): P(1) is true, so true. ∃x Q(x): Q(2) is true, so true. Both premises are true.
- Conclusion: for x = 1, Q(1) is false, so P(1) ∧ Q(1) is false. For x = 2, P(2) is false, so P(2) ∧ Q(2) is false. No member satisfies both, so the conclusion is false.
- One interpretation makes the premises true and the conclusion false, so the argument is invalid.

## Concepts
- [[interpretation]] (new) — a domain, referents for names and extensions for predicates; it fixes truth values (p. 281).
- [[counter-model]] (new) — an interpretation that refutes a claim of validity or entailment (p. 286).
- [[validity / soundness]] — an argument is invalid if some interpretation makes premises true and conclusion false (p. 286).
- [[entailment]] (new) — A₁,…,Aₙ ⊨ C; refuted by one counter-model (p. 286).
- [[joint satisfiability]] (new) — some interpretation makes all the sentences true together (p. 284).
- [[logical equivalence]] (new) — refuted by an interpretation where the sentences differ in truth value (p. 283).
- [[logical form vs. grammatical form]] — the English argument and its FOL symbolization can come apart (p. 287).

## Canonical instances
- [[paris-interpretation]] — refutes validity and contradiction of ∃x A(x,x) → B(d) (p. 282).
- [[coleman-davis-saxophone]] — shows ∀x S(x) and ∃x S(x) are not equivalent (p. 283).
- [[marx-mises-argument]] — counter-model to ∃x(G(x) → G(a)) ∴ ∃x G(x) → G(a) (p. 284).
- [[fox-vixen-argument]] — the English argument is conceptually valid though its symbolization has no FOL entailment (pp. 286–287).

## Bridges (candidates)
- [structural-analogy] counter-model ↔ falsifiability: one counter-instance refutes a universal claim.
- [structural-analogy] the symbolization caution ↔ analysis: a formal paraphrase may lose something of the original.

## Questions this raises
- When is a symbolization good enough that "nothing important is lost"?
- Can failure to find a counter-model ever show validity, or does that need another method?
- How can we be sure a small domain is never enough for a given non-equivalence?

## Exercises worth doing
- Ex. A.3 (p. 287) — show P(m) ∧ ¬∀x P(x) is neither a validity nor a contradiction — easy
- Ex. B.4 (p. 287) — two conditionals with ∃ placed differently are not equivalent — medium
- Ex. B.8 (p. 287) — ∀∃ versus ∃∀ non-equivalence — medium
- Ex. C.10 (p. 288) — ¬∃x∀y R(x,y) and ∀x∃y R(x,y) jointly satisfiable — medium
- Ex. D.7 (p. 288) — ∀x O(x,c), ∀x O(c,x) ∴ ∀x O(x,x) is invalid — medium
- The fox/vixen exercise (p. 287) — find a counter-model to the symbolization — easy

## Reading notes
- Printed page = pdf page − 10 (pdf 291–298 = printed 281–288).
- The text layer garbles the brackets in practice exercises C.5 and C.6 on p. 288; I read them from the image. The arrow diagram on p. 285 is not in the text layer; I read it from the image.
- Section 33.3's third example refers back to chapter 30, which is not in these pages.
- No solutions are printed in this unit.
