---
id: magnus-2025-forallx/ch43-symbolic
work: magnus-2025-forallx
unit: Appendix A (unit ch43) — Symbolic notation
pages: 399-403
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
# A Symbolic notation

## L0 — One line
Other logic texts use different names and symbols for the same ideas, and Polish notation writes connectives first so that no parentheses are needed.

## L1 — The gist (≤ 120 words)
Logic books are not uniform. This appendix lists other names for the book's terms (for example "propositional logic" and "predicate logic"). It also lists other symbols for negation, conjunction, disjunction, the conditional, the biconditional and the quantifiers, so that a reader can recognise them in other books. Finally it describes Polish notation, from the late 1920s. In it each connective is written before the sentences it connects. Parentheses are then never needed, and the left-most connective is always the main one. A sentence can then be evaluated by moving through it from right to left. This is one reason variants of it are used in computer languages.

**Prerequisites:** the TFL connectives (¬, ∧, ∨, →, ↔), the idea of a main connective, and truth tables; the FOL quantifiers ∀ and ∃.

## L2 — Key ideas
- Other texts call TFL (truth-functional logic, the book's logic of sentences and connectives) sentential or propositional logic, and FOL (first-order logic, the book's logic with predicates and quantifiers) predicate or quantified logic. The authors keep the name truth-functional to stress that it deals only with assignments of truth and falsity to sentences (p. 399).
- Other texts use other terms for the same things: wff for formula, truth-assignment for valuation, monadic/dyadic or unary/binary for one-/two-place predicates, constants for names, and universe of discourse for domain (pp. 399–400).
- Many symbol variants exist; in the history of logic, authors were often forced to use notation their printers could typeset (p. 400).
- Conjunction is often written with the ampersand (&), but many logicians use another symbol. The ampersand is also common in ordinary English writing, and they want to avoid confusing the object language (the formal language) with the metalanguage (the language used to talk about it) (p. 401).
- Systems that use the arrow → for the conditional use ↔ for the biconditional; systems that use the horseshoe ⊃ typically use the triple bar ≡ (p. 401).
- Many programming languages write disjunction with a vertical bar (or two). This invites confusion with the Sheffer stroke of chapter 46, which is standardly written as a single vertical bar (p. 401).
- Polish notation uses N, A, K, C, E for ¬, ∨, ∧, →, ↔ and puts binary connectives first, so ¬A → B is C N ab and ¬(A → B) is N C ab (pp. 402–403).
- Because the order of operations can be specified more mechanically in Polish notation, variants of it are used as the internal structure of many programming languages (p. 403).

## L3 — Walkthrough

### A.1 Alternative nomenclature
- **TFL** is also called sentential logic (it deals with sentences) or propositional logic (it deals with propositions). The authors prefer "truth-functional" to stress that it deals only with assignments of truth and falsity, and that all its connectives are truth-functional (p. 399).
- **FOL** is also called predicate logic (predicates apply to objects) or quantified logic (it uses quantifiers) (p. 399).
- **Formulas**: some texts say "well-formed formula", abbreviated "wff". The authors call this both barbarous and unnecessary, adding that such texts do not countenance ill-formed formulas. They keep "formula" (p. 399).
- In TFL, unlike FOL, a formula and a sentence are not distinguished, so TFL sentences are sometimes also called formulas (p. 400).
- **Valuations** are sometimes called truth-assignments or truth-value assignments (p. 400).
- **n-place predicates**: other texts say monadic/dyadic/triadic, or unary/binary/ternary (p. 400).
- **Names** (a, b, c): some texts call them "constants". Others do not mark any syntactic difference between names and variables. They look only at whether a symbol occurs bound or unbound (p. 400).
- **Domains** are sometimes called "domain of discourse" or "universe of discourse" (p. 400).

### A.2 Alternative symbols
Notation differed across history and authors, and authors were often limited to what their printers could typeset (p. 400).
- **Negation**: "¬" (the hoe) and "∼" (the tilde or swung dash). In some more advanced systems two kinds of negation must be distinguished, and this is sometimes shown by using both symbols. Older texts use a line over the formula (e.g. an overlined A ∧ B) or a minus sign "−". Many texts write x ≠ y for ¬x = y (pp. 400–401).
- **Disjunction**: "∨" typically means inclusive disjunction. Some "algebraic tradition" texts write "+". Many programming languages use "|" or "||", which can be confused with the Sheffer stroke ("|") of chapter 46 (p. 401).
- **Conjunction**: "&" (from Latin *et*) is often used. It is common in ordinary English ("Smith & Sons"). Many logicians therefore use a different symbol, to avoid confusing object language and metalanguage; as a formal symbol, "&" is not the English word. The most common choice now is "∧", a counterpart of "∨". Some use a dot "•". Some older texts have no symbol, writing AB for "A and B" (p. 401).
- **Conditional**: arrow "→" or horseshoe "⊃" (p. 401).
- **Biconditional**: "↔" goes with the arrow, and "≡" (triple bar) typically goes with the horseshoe (p. 401).
- **Quantifiers**: the universal quantifier is typically a rotated "A", and the existential quantifier a rotated "E". Some texts write the variable in parentheses, e.g. $(x)P(x)$ for $\forall x\,P(x)$. Some texts use large $\bigwedge$ and $\bigvee$ for universal and existential quantifiers, with the variable as a subscript or underneath (p. 402).

Summary table (p. 402):

| Notion | Symbols |
|---|---|
| negation | ¬, ∼, −, overline |
| conjunction | ∧, &, • |
| disjunction | ∨, +, \|, \|\| |
| conditional | →, ⊃ |
| biconditional | ↔, ≡ |
| universal quantifier | ∀x, (x), $\bigwedge_x$ |
| existential quantifier | ∃x, $\bigvee_x$ |

*Intuition note:* The symbols differ, but the connectives are the same. Learn the table so you can translate when you meet another book.

### A.3 Polish notation
- It was introduced in the late 1920s by the Polish logician Jan Łukasiewicz, and it is a notation for sentential logic (p. 402).
- Sentence letters are lower case. N is negation, A disjunction ("alternation"), K conjunction, C the conditional, E the biconditional ("equivalence") (p. 402).
- A binary connective is written *before* the two sentences it connects: $A \land B$ becomes $K\,ab$ (p. 402).
- ¬A → B has the conditional as main operator, while ¬(A → B) has negation as main connective. In TFL, this is shown by putting parentheses around the conditional in the second sentence (pp. 402–403).
- In Polish notation parentheses are never required, and the left-most connective is always the main one. So the first is $C\,N\,ab$ and the second is $N\,C\,ab$ (p. 403).
- A sentence can be evaluated by working through the symbols right to left. For $N\,K\,ab$: take the values of b and a, then their conjunction, then negate the result (p. 403).
- In TFL the truth table for ¬(A ∧ B) requires looking at A and B, then at the conjunction in the middle, then at the negation at the beginning. The authors say the general rule for what to evaluate next in TFL is not nearly so simple as in Polish notation (p. 403).
- Because the order of operations can be specified more mechanically, variants of Polish notation are the internal structure of many programming languages (p. 403).

*Intuition note:* Position replaces parentheses. The first symbol is the main connective, and everything after it is its input.

## Toy example (ours)
Translate $\neg(A \land B) \to C$ into Polish notation and evaluate it for $A=T$, $B=F$, $C=F$.
1. The main connective is "→", so it comes first: C, then the antecedent, then the consequent.
2. The antecedent is ¬(A ∧ B). This is N followed by K ab, so it gives N K ab.
3. The consequent is c. The result is **C N K a b c**.
4. Evaluate right to left. c = F, b = F, a = T.
5. K ab: T ∧ F = F.
6. N: ¬F = T.
7. C with antecedent T and consequent c = F: T → F = F. The sentence is false.

## Concepts
- [[polish-notation]] (new) — notation with the connective before its sentences, so parentheses are never needed (p. 402)
- [[main-connective]] (new) — the operator that governs the whole sentence; in Polish notation it is the left-most connective (p. 403)
- [[use-vs-mention]] — related idea: the text says many logicians avoid & to avoid confusing object language and metalanguage; as a formal symbol it is not the English word (p. 401)
- [[logical-notation-variants]] (new) — different symbol sets for the same connectives and quantifiers (p. 402)

## Canonical instances
- [[polish-notation-examples]] (new) — ¬A → B is C N ab and ¬(A → B) is N C ab (p. 403)
- [[sheffer-stroke-confusion]] (new) — "|" for disjunction in programming vs. the Sheffer stroke (p. 401)

## Bridges (candidates)
- [structural-analogy] Polish notation ↔ computer science: right-to-left evaluation of a parenthesis-free expression — the text says variants are used inside programming languages (p. 403).
- [metaphor] Ampersand and the object/metalanguage worry ↔ use vs. mention: avoid using a symbol that also works as an English word (p. 401).

## Questions this raises
- Why is the order of evaluation in Polish notation more "mechanical" than in notation with parentheses?
- Does the choice of symbols (e.g. "→" vs. "⊃") ever change which sentences are logically valid, or is it only notation?
- What are the "two kinds of negation" that some advanced systems distinguish (p. 400)?

## Reading notes
- Printed page = pdf − 10 (pdf 409–413 are printed 399–403).
- The overlined "A ∧ B" (p. 401) and the large ⋀/⋁ symbols (p. 402) are garbled in the text layer; I checked the images.
- The unit gives no exercises.
- The text refers to chapter 6 and chapter 46, which are not part of this unit.
