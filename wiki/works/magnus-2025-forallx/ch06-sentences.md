---
id: magnus-2025-forallx/ch06-sentences
work: magnus-2025-forallx
unit: "6 Sentences of TFL"
pages: 49-55
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
# Sentences of TFL

## L0 — One line
TFL defines "sentence" exactly, by an inductive definition: sentence letters are sentences, and connectives build bigger sentences from smaller ones.

## L1 — The gist (≤ 120 words)
English has no formal definition of "sentence". TFL does. The chapter asks which strings of TFL symbols count as sentences. Answer: an inductive definition with a base clause (sentence letters), one clause per connective, and a closing clause ("nothing else"). Every sentence can be taken apart step by step down to sentence letters. This gives the idea of a main logical operator (the connective added last) and of the scope of a connective. The chapter also allows two relaxed bracket conventions for readability. The structure matters later, because the truth of a sentence is worked out through it.

**Prerequisites:** the TFL symbols and connectives from earlier chapters (negation, conjunction, disjunction, conditional, biconditional); the idea of a subsentence.

## L2 — Key ideas (5–10 bullets)
- An expression is any string of TFL symbols. Some expressions are gibberish, so rules are needed to pick out sentences (p. 50).
- There is no point in listing sentences one by one, so the definition describes how they are constructed (p. 50).
- The definition has seven clauses: sentence letters; one clause each for ¬, ∧, ∨, →, ↔; and "nothing else" (p. 51).
- Such definitions are inductive: base elements plus ways to build more (p. 51).
- To test a string, apply the clauses backwards until you reach sentence letters (p. 52).
- The main logical operator is the connective introduced last. A bracket-counting method finds it (pp. 52–53).
- The scope of a connective is the subsentence whose main logical operator it is (p. 53).
- Strictly, brackets are part of the sentence; the two relaxed conventions make working with TFL easier (p. 54).

## L3 — Walkthrough

**Intro.** "Sentence of English" has no formal definition. "Sentence of TFL" will be defined exactly; this is one respect in which TFL is more precise than English (p. 49).

**6.1 Expressions.** TFL has three kinds of symbols: atomic sentences (A, B, C, …, with subscripts as needed, e.g. $A_1$, $J_{375}$), the connectives ¬, ∧, ∨, →, ↔, and the brackets ( and ) (p. 49). An *expression of TFL* is any string of these symbols, in any order (p. 50). A footnote says that section 17.8 will add the symbol ⊥, which will also count as an atomic sentence (p. 50).

**6.2 Sentences.**
- '(A ∧ B)' is a sentence. '¬) (∨() ∧ (¬¬())((B' is an expression but gibberish (p. 50).
- Sentence letters are also called *atomic* sentences. There are infinitely many letters, and combinations are endless, so listing is pointless (p. 50).
- The text therefore describes the construction process. The clauses are stated using script letters for any sentences (p. 50).

Definition of *sentence of TFL* (p. 51):
1. Every sentence letter is a sentence.
2. If $\mathscr{A}$ is a sentence, then $\neg\mathscr{A}$ is a sentence.
3. If $\mathscr{A}$ and $\mathscr{B}$ are sentences, then $(\mathscr{A}\land\mathscr{B})$ is a sentence.
4. Likewise $(\mathscr{A}\lor\mathscr{B})$.
5. Likewise $(\mathscr{A}\to\mathscr{B})$.
6. Likewise $(\mathscr{A}\leftrightarrow\mathscr{B})$.
7. Nothing else is a sentence.

*Inductive definition:* it begins with specifiable base elements and generates indefinitely many more by compounding earlier ones (p. 51). Analogy: *ancestor of mine*. Base: my parents are ancestors. Step: if $x$ is an ancestor, so are $x$'s parents. Closing: nothing else is (p. 51). The same definition lets us decompose a sentence into simpler parts. Once we reach sentence letters, "we are ok" (pp. 51–52).

*Intuition note.* The definition is like a recipe with a base ingredient and repeatable steps. To check a string, run the recipe backwards. If you reach only sentence letters, it is a sentence.

Worked examples (p. 52):
- '¬¬¬D': a sentence if '¬¬D' is (clause 2); that if '¬D' is; that if 'D' is. 'D' is a sentence letter, so clause 1 applies.
- '¬(P ∧ ¬(¬Q ∨ R))': a sentence if '(P ∧ ¬(¬Q ∨ R))' is. That is a sentence if both 'P' and '¬(¬Q ∨ R)' are. 'P' is a letter. '¬(¬Q ∨ R)' is a sentence if '(¬Q ∨ R)' is. By clause 4 that needs '¬Q' and 'R', and both are sentences.

**Main logical operator.** In any sentence that is not a sentence letter, some connective was introduced last. This is the main logical operator (p. 52). Examples (p. 52):
- '¬¬¬D': the first '¬'.
- '(P ∧ ¬(¬Q ∨ R))': '∧'.
- '((¬E ∨ F) → ¬¬G)': '→'.

Method (pp. 52–53):
- If the first symbol is '¬', it is the main logical operator.
- Otherwise count brackets: +1 for each '(', −1 for each ')'. When the count is exactly 1, the first operator you meet (apart from '¬') is the main logical operator.
- Use the fully bracketed sentence, not the relaxed conventions of 6.3 (p. 53).

**Why structure matters.** Truth conditions follow the structure. '¬¬¬D' is true if and only if '¬¬D' is false, and so on down to atomic components. The text returns to this in part III (p. 53).

**Scope.** The scope of a connective in a sentence is the subsentence for which that connective is the main logical operator (p. 53). Example: $(P \land (\neg(R \land B) \leftrightarrow Q))$ is built by conjoining 'P' with '(¬(R ∧ B) ↔ Q)'. That is built by a biconditional between '¬(R ∧ B)' and 'Q'. So the scope of the negation is just '¬(R ∧ B)' (p. 53).

*Intuition note.* Scope is how much of the sentence a connective governs. In the example, the negation covers only the piece '¬(R ∧ B)', not the whole sentence.

**6.3 Bracketing conventions.** Strictly, the brackets in '(Q ∧ R)' are indispensable. To negate it we need '¬(Q ∧ R)'. Without brackets, '¬Q ∧ R' is most naturally read as '(¬Q ∧ R)', which is very different (section 5.2). So strictly 'Q ∧ R' is not a sentence but a mere expression (p. 54). Two conventions (p. 54):
1. Outermost brackets may be omitted. They must be restored when the sentence is embedded in a larger one.
2. Square brackets '[ ]' may replace round ones. There is no logical difference.

Example: $(((H \to I) \lor (I \to H)) \land (J \lor K))$ becomes $[(H \to I) \lor (I \to H)] \land (J \lor K)$ (p. 54).

## Toy example (ours)
Is '((A ∧ B) → ¬C)' a sentence, and what is its main operator?
- 'A', 'B', 'C' are sentence letters (clause 1).
- '(A ∧ B)' is a sentence (clause 3). '¬C' is a sentence (clause 2).
- So '((A ∧ B) → ¬C)' is a sentence (clause 5).
- Bracket count, left to right: '(' → 1, '(' → 2, A, '∧' at count 2 (not 1), B, ')' → 1. Next symbol '→' is at count 1 and is not '¬'. So '→' is the main operator.
- Scope of '∧' is '(A ∧ B)'. Scope of '¬' is '¬C'.

## Concepts
- [[expression-of-tfl]] (new) — any string of TFL symbols (p. 50)
- [[sentence-of-tfl]] (new) — a string built by the seven-clause inductive definition (p. 51)
- [[atomic-sentence]] (new) — a sentence letter, the base clause (p. 50)
- [[inductive-definition]] (new) — base elements plus generating clauses plus "nothing else" (p. 51)
- [[main-logical-operator]] (new) — the connective introduced last in building a sentence (p. 52)
- [[scope-of-connective]] (new) — the subsentence whose main operator the connective is (p. 53)

## Canonical instances
- [[ancestor-of-mine]] — inductive definition illustrated with ancestors (p. 51)
- [[negation-scope-example]] — scope of ¬ in $(P \land (\neg(R \land B) \leftrightarrow Q))$ (p. 53)

## Bridges (candidates)
- [structural-analogy] inductive definition of sentence ↔ recursion in programming: base case plus recursive step.
- [structural-analogy] checking a sentence by decomposition ↔ parsing of grammar rules in linguistics.

## Questions this raises
- Why does "nothing else is a sentence" matter for the definition?
- Do the relaxed bracket conventions ever create ambiguity?
- How exactly does truth of a sentence follow its inductive structure (part III)?

## Exercises worth doing
- Ex. A (pp. 54–55) — apply the definition strictly versus with the relaxed conventions to eight strings — difficulty: easy
- Ex. B (p. 55) — can a sentence contain no sentence letters? — difficulty: medium
- Ex. C (p. 55) — find the scope of each connective in a bracketed sentence — difficulty: easy

## Reading notes
- Printed = pdf − 10.
- Script letters for $\mathscr{A}$, $\mathscr{B}$ are rendered differently in the text layer; the images show them clearly.
- Practice item A.4 reads '¬ ∧ S' in the image.
- The text says "the funny fonts" are explained in section 8.3 (p. 50).
