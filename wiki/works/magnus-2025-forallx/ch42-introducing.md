---
id: magnus-2025-forallx/ch42-introducing
work: magnus-2025-forallx
unit: 42 Introducing modal logic
pages: 337-340
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
# Introducing modal logic

## L0 — One line
Modal logic adds the operators □ and ◇ to sentential logic; their readings vary (necessity, knowledge, obligation…), and rules are added to fit each reading.

## L1 — The gist (≤ 120 words)
The chapter asks what modal logic is and how its sentences are built. Modal logic studies modalities, the ways in which a statement can be true, such as necessarily or possibly. It is flexible: □ and ◇ can also mean provable, known, believed or obligatory. Which formulas count as valid depends on the reading. For example, □A → A is valid for necessity and knowledge but not for belief or obligation. The book will present systems K, T, S4 and S5, with S5 the strongest. The language is TFL plus two formation rules, one for □ and one for ◇. This matters because it shows one formal tool covering many concepts.

**Prerequisites:** TFL (sentential logic) connectives and the idea of building sentences by recursive rules; the meaning of "valid".

## L2 — Key ideas (5–10 bullets)
- Modal logic studies modalities, ways a statement can be true; □ and ◇ are the operators for necessity and possibility (p. 337).
- There are several kinds of necessity (human, physical, logical), and modal logic is meant to handle all of them (pp. 337–338).
- □ and ◇ need not mean necessity and possibility. They can be read as provability, knowledge, belief or moral obligation (p. 338).
- Whether a modal formula is valid depends on how □ is read. □A → A is valid for necessity and knowledge, not for belief or obligation (p. 338).
- The systems K, T, S4 and S5 differ in their proof rules and semantics. K is the basic one, and everything provable in K is provable in the others (p. 338).
- K does not prove □A → A, so it does not suit necessity. T proves it. S5 is the strongest system and the most widely accepted for necessity and possibility (pp. 338–339).
- The language of ML is TFL plus two formation rules for □ and ◇. Quantified modal logic (from FOL) is more powerful but much more complicated, so the book starts with TFL instead (p. 339).
- Sentences are defined by nine clauses: atoms, the TFL connectives, the two modal operators, and a closing clause that excludes everything else (p. 340).

## L3 — Walkthrough

**Opening: what ML is (p. 337).** Modal logic (ML) is the logic of modalities, ways in which a statement can be true. A statement can be true, and it can also be *necessarily* true, meaning true no matter how the world might have been. Logical truths are not just true because of some accidental feature of the world, but true come what may. A possible statement may not actually be true, but it might have been true. □A reads *It is necessarily the case that A*; ◇A reads *It is possibly the case that A* (p. 337).

**Kinds of necessity (pp. 337–338).** The author's example is running at 100 mph.
- It is humanly impossible, given the sort of creatures we are, but not physically impossible. Swapping my biological legs for robotic ones is physically possible (p. 337).
- Running faster than light is physically impossible, since the laws of physics forbid it. It is still not logically impossible, because it is no contradiction to imagine that the laws might have been different (pp. 337–338).

*Intuition note:* "Impossible" has layers. Something can be impossible in one sense (human) and still be possible in another (physical), and even something physically impossible need not be a contradiction. Modal logic gives one framework for all these layers.

**Other readings of □ and ◇ (p. 338).** ML deals with all kinds of modality. We start with a basic set of rules for □ and ◇ and add rules to fit the modality we want. The readings the text lists are:
- Provability: □A is *It is provable that A*; ◇A is *It is not refutable that A*.
- Knowledge or belief: □A is *S knows that A* or *S believes that A*.
- Obligation: □A is *It is morally obligatory that A*; ◇A is *It is morally permissible that A*.

All we would need to do is cook up the right rules for these readings (p. 338).

**Modal formulas and validity (p. 338).** A modal formula is one that includes modal operators such as □ and ◇. Which modal formulas are provable or valid depends on the interpretation of □ and ◇. Take □A → A:
- Necessity (it might say "if A is necessary, it is true"): valid, because necessary propositions are true come what may, so true in the actual world.
- Known truth (it might say "if A is known, then it is true"): valid, because one cannot know something false.
- Belief: not valid, because we can believe false propositions.
- *It ought to be the case that*: not valid. Not every proposition that ought to be true is in fact true. The example is *Every murderer will be brought to justice*, which ought to be true but isn't (p. 338).

*Intuition note:* The same symbols can mean different things, so validity is relative to a reading. The formula says that if A holds in the modal sense, then A is true. That fits knowing and necessity, but not believing or obligation.

**The systems (pp. 338–339).** The systems K, T, S4 and S5 differ in their proof rules and in the semantics used to define logical notions (p. 338).
- K is the basic system. Everything valid or provable in K is also provable in the others (p. 338).
- K does not prove □A → A for sentence letter A, so it is not appropriate for necessity and possibility, where □A → A should be provable (pp. 338–339).
- T proves it. T is therefore more appropriate for necessity and possibility, but less appropriate for belief or obligation, where □A → A should not (always) be provable (p. 339).
- S5 is the strongest system considered. It is perhaps the best for necessity and possibility, and in any case the most widely accepted (p. 339).

**42.1 The Language of ML (pp. 339–340).** The aims are to learn to prove things in ML and to construct interpretations for ML. Both first need an account of how to build sentences (p. 339).

ML is an extension of TFL. Starting from FOL would have given Quantified Modal Logic (QML), which is much more powerful than ML but also much, much more complicated. So the book keeps things simple and starts with TFL (p. 339).

ML has an infinite stock of atoms: capital letters, with or without numerical subscripts (A, B, …, A₁, B₁, …) (p. 339). The formation rules are those of TFL plus two more (p. 340):
1. Every atom of ML is a sentence of ML.
2. If 𝒜 is a sentence, so is ¬𝒜.
3. If 𝒜 and ℬ are sentences, so is (𝒜 ∧ ℬ).
4. If 𝒜 and ℬ are sentences, so is (𝒜 ∨ ℬ).
5. If 𝒜 and ℬ are sentences, so is (𝒜 → ℬ).
6. If 𝒜 and ℬ are sentences, so is (𝒜 ↔ ℬ).
7. If 𝒜 is a sentence, so is □𝒜.
8. If 𝒜 is a sentence, so is ◇𝒜.
9. Nothing else is a sentence of ML.

The author's example sentences: A; P ∨ Q; □A; C ∨ □D; □□(A → R); □◇(S ∧ (Z ↔ (□W ∨ ◇Q))) (p. 340).

*Intuition note:* In the formation rules, □ and ◇ work like ¬: each takes any sentence and gives a new sentence. So they can be stacked and nested, as in □□(A → R) and □◇(…) (p. 340).

## Toy example (ours)
Build □(A → ◇B) with the rules:
1. A and B are atoms, so sentences (rule 1).
2. ◇B is a sentence (rule 8, from B).
3. (A → ◇B) is a sentence (rule 5, from A and ◇B).
4. □(A → ◇B) is a sentence (rule 7, from step 3).

By rule 9, "□" alone or "A□" is not a sentence, because no rule produces them.

Validity of □A → A under two readings, for a sample statement A:
- Knowledge: let A be "2+2=5". If S knows A, A must be true. It is not true, so nobody knows it; the antecedent is false and the conditional holds.
- Belief: suppose S believes A. Then □A is true and A is false, so □A → A fails.

## Concepts
- [[modal-operator]] (new) — □ and ◇, which attach to sentences to say how they are true (p. 337)
- [[necessity-possibility]] (new) — □A: true no matter how the world might have been; ◇A: might have been true (p. 337)
- [[kinds-of-modality]] (new) — human, physical and logical necessity are different kinds of necessity (pp. 337–338)
- [[modal-formula]] (new) — a formula containing modal operators; its validity depends on the reading of □ and ◇ (p. 338)
- [[modal-systems-K-T-S4-S5]] (new) — systems differing in proof rules and semantics; K is basic, S5 is strongest (p. 338)
- [[validity]] — here applied to modal formulas, relative to an interpretation of □ (p. 338)
- [[language-of-ML]] (new) — TFL plus the rules for □ and ◇, with atoms and a closure clause (pp. 339–340)

## Canonical instances
- [[running-100mph-example]] (new) — human, physical and logical impossibility come apart (pp. 337–338)
- [[murderer-justice-example]] (new) — what ought to be true need not be true, so □A → A fails for obligation (p. 338)

## Bridges (candidates)
- [structural-analogy] ML formation rules 1–9 ↔ analytic-philosophy: recursive definition of sentences in TFL — same recursive pattern with two extra clauses.
- [structural-analogy] □A → A for knowledge ↔ analytic-philosophy: knowledge as factive (cannot know a falsehood) — the validity of □A → A mirrors the factivity of knowing.
- [metaphor] ML's reading-relative validity ↔ analytic-philosophy: different senses of "must" in ordinary language — different necessities need different rules.

## Questions this raises
- What exactly are the extra rules of T, S4 and S5, and what semantics define them?
- Why is S5 perhaps best for necessity and possibility? What does S4 miss or add?
- Which formulas besides □A → A separate the readings (knowledge, belief, obligation)?
- What does QML add, and why is it so much more complicated?

## Reading notes
- Printed page = pdf − 10 (pdf 347–350 are printed 337–340).
- Misprint on p. 339: "possibiliity" for "possibility".
- In the page images, the script letters 𝒜 and ℬ (pp. 338, 340) stand for any sentence, while ordinary italic letters stand for specific sentence letters and example sentences. The text layer renders the script letters as garbled glyphs.
- The example sentences (e.g. P ∨ Q) omit the outer parentheses that rules 3–6 would literally give. The text does not comment on this on these pages (p. 340).
- On these pages, 42.1 is the only numbered section, and the chapter introduction has no heading.
