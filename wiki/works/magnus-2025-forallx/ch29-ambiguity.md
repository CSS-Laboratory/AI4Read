---
id: magnus-2025-forallx/ch29-ambiguity
work: magnus-2025-forallx
unit: 29 Ambiguity
pages: 253-256
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
# Ambiguity

## L0 — One line
An ambiguous English sentence can have several readings; different FOL symbolizations can separate them, and in FOL every connective and quantifier has a well-determined scope.

## L1 — The gist (≤ 120 words)
English sentences can be ambiguous, while FOL sentences are not. The chapter asks how different symbolizations can separate the readings of one English sentence. A common source of ambiguity is scope: English does not show which logical word lies inside the scope of which other, but each FOL formula does. Four cases are shown: negation with *every* (*Everything that glitters is not gold*), *only* (*Only young cats are playful*), *every* with *a* (*Everyone went to see a movie*), and a definite description with negation (*The King of France is not bald*). Each reading is written out in FOL so the readings can be compared.

**Prerequisites:** FOL quantifiers ∀ and ∃, connectives, identity; the "only" schema (ch. 24); quantifier order (ch. 25); Russell's definite descriptions (ch. 28).

## L2 — Key ideas
- English can leave scope unclear. In FOL every connective and quantifier has a well-determined scope (p. 253).
- Two readings of *Everything that glitters is not gold* differ in whether ¬ is in the scope of ∀ or ∀ is in the scope of ¬ (p. 254).
- The first symbolization (∀ outside ¬) is the one we would use for *Nothing that glitters is gold*. The author says the idiom does not mean that, but means *Not everything that glitters is gold* (pp. 253–254).
- *Only young cats are playful* has three readings. The author says the schema reading is probably not what is intended. Stress can make the last two readings salient and can indicate the first (pp. 254–255).
- *Everyone went to see a movie* has two readings, depending on whether ∃ or ∀ has wide scope (p. 255).
- *The King of France is not bald* has two readings, depending on whether the description has wide or narrow scope relative to "not" (p. 256).

## L3 — Walkthrough

**Opening (p. 253).** Chapter 7 said English sentences can be ambiguous, but TFL sentences are not. Structural ambiguity can often be straightened out with different symbolizations. In *scope ambiguity* the English does not make clear which logical word is in the scope of which other. In FOL, whether one connective or quantifier occurs in the scope of another is always determined.

**Example 1: *Everything that glitters is not gold.*** Let $F(x)$: *x glitters*; $G(x)$: *x is gold* (p. 253).
- Reading by the form "every F is not G":
$$\forall x\,(F(x) \to \neg G(x))$$
This is how we would symbolize *Nothing that glitters is gold*. The author says the idiom does not mean that (p. 253).
- The idiom means one should not assume that whatever glitters is gold. It is symbolized as for *Not everything that glitters is gold*:
$$\neg\forall x\,(F(x) \to G(x))$$
- The difference: in the first, ¬ is in the scope of ∀. In the second, ∀ is in the scope of ¬ (p. 254).
- Existential versions of the two readings (p. 254):
$$\neg\exists x\,(F(x) \wedge G(x)) \qquad \exists x\,(F(x) \wedge \neg G(x))$$
(In order: the first matches the "nothing" reading, the second the "not everything" reading. This pairing is implied by the equivalences, not stated by the author.)

*Intuition note:* Moving "not" from inside "every" to outside it changes the meaning from "none" to "not all".

**Example 2: *Only young cats are playful.*** Key: $P$ playful, $Y$ young, $C$ cat (p. 254).
- By the ch. 24 schema: $\forall x\,(P(x) \to (Y(x) \wedge C(x)))$. The author says this means something like *If an animal is playful, it is a young cat* (domain: animals), and that this is probably not what is intended (p. 254).
- More likely intended reading: old cats are not playful, i.e. if something is a playful cat it must be young:
$$\forall x\,((C(x) \wedge P(x)) \to Y(x))$$
- Third reading: of the young animals, only the cats are playful (pp. 254–255):
$$\forall x\,((Y(x) \wedge P(x)) \to C(x))$$
- Stress (p. 255): the last two readings can be made salient by stress. Stress on *cats* suggests the last reading. Stress on *young* suggests the other one, the middle reading. The first reading can be indicated by stressing both *young* and *cats* (not old cats, nor dogs of any age).

*Intuition note (our gloss):* The three formulas differ in the condition on the left of the arrow: playful alone, playful cat, or playful young animal.

**Example 3: *Everyone went to see a movie.*** Key: $P(y)$: *y is a person*; $M(x)$: *x is a movie*; $S(y,x)$: *y went to see x*. The domain contains at least people and movies (p. 255).
- One single movie that everyone saw:
$$\exists x\,(M(x) \wedge \forall y\,(P(y) \to S(y,x)))$$
- Everyone saw some movie or other, not necessarily the same one:
$$\forall y\,(P(y) \to \exists x\,(M(x) \wedge S(y,x)))$$
- In the first, ∃ has *wide scope* and ∀ has *narrow scope*. In the second it is the other way round (p. 255).

*Intuition note (our gloss):* In each formula, the outermost quantifier is the one whose scope contains the other. Swapping the order changes whether one movie is chosen for everyone or a movie for each person.

**Example 4: *The King of France is not bald.*** (Russell's example, p. 256.) Key: $K$: *is King of France*; $B$: *is bald*.
- Wide-scope description, with "not" as inner negation: it asserts the existence of a single King of France and ascribes non-baldness to him:
$$\exists x\,[(K(x) \wedge \forall y\,(K(y) \to x = y)) \wedge \neg B(x)]$$
- Narrow-scope description: "not" denies the sentence *The King of France is bald*:
$$\neg\exists x\,[(K(x) \wedge \forall y\,(K(y) \to x = y)) \wedge B(x)]$$
- The first reading has the description with wide scope. The second has it with narrow scope (p. 256).

*Intuition note (our gloss):* In the wide-scope reading a King of France must exist. In the narrow-scope reading the sentence only denies a claim, so it can be true if there is no such king. The text states only the wide-scope existence claim.

## Toy example (ours)
Domain: two people, $a$ and $b$. Let $L(y,x)$: *y likes x*. Suppose only $L(a,b)$ and $L(b,a)$ are true.
- $\forall y\,\exists x\,L(y,x)$: for $y=a$ pick $x=b$; for $y=b$ pick $x=a$. True.
- $\exists x\,\forall y\,L(y,x)$: try $x=a$, then $L(a,a)$ is false. Try $x=b$, then $L(b,b)$ is false. So it is false.

Same pattern, different quantifier order, different truth value. So the readings really differ.

## Concepts
- [[scope-ambiguity]] (new) — one sentence with several readings that differ in which logical word lies within another's scope (p. 253).
- [[wide-narrow-scope]] (new) — a quantifier has wide scope if its scope contains the other quantifier, narrow if contained (p. 255).
- [[logical form vs. grammatical form]] — one English surface form may map to several different FOL forms (p. 253).
- [[theory of descriptions]] — *The King of France* symbolized with ∃ and uniqueness (∀y…x = y); scope relative to ¬ matters (p. 256).

## Canonical instances
- [[glitters-not-gold]] — *every* and *not*: none vs. not all (pp. 253–254).
- [[only-young-cats]] — three readings of *only*; stress can make readings salient (pp. 254–255).
- [[everyone-saw-a-movie]] — ∃∀ vs. ∀∃ readings (p. 255).
- [[king-of-france-not-bald]] — description scope with negation (p. 256).

## Bridges (candidates)
- [same-math] Quantifier order and scope ↔ mathematics: ∀x∃y vs. ∃y∀x — the same quantifier-order issue.
- [structural-analogy] Stress making a reading of *only* salient ↔ linguistics: intonation signalling what a word focuses on.

## Questions this raises
- When more than one reading is plausible, how do we choose the one the speaker means?
- Is each ambiguity just scope, or are there other sources (the text says scope is one common source)?
- Do the two King-of-France readings have different truth values if no king exists?

## Exercises worth doing
- Ex. A (p. 256) — symbolize all readings of *No one likes a quitter*, *CSI found only red hair at the scene*, *Smith's murderer hasn't been arrested* — difficulty: medium
- Ex. B (p. 256) — explain what is going on in Russell's yacht example — difficulty: medium

## Reading notes
- Printed = pdf − 10.
- In the King of France formulas on p. 256, the image shows unbalanced brackets (`[K(x) ∧ ∀y(K(y) → x = y)) ∧ …`). I wrote them with balanced brackets.
- p. 255 has the typo "can be indicate". The italic stress in *Only young cats are playful* is visible only in the image.
- The "only" schema (ch. 24) and chapters 25 and 28 are referenced but not included here.
