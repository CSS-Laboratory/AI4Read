---
id: magnus-2025-forallx/ch03-truth-p2
work: magnus-2025-forallx
unit: "III Truth tables, part 2/2 (chs. 12–15: Semantic concepts; Limitations of TFL; Truth table shortcuts; Partial truth tables)"
pages: 85–108
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Semantic concepts, limits of TFL, and shortcut truth tables

## L0 — One line
Truth tables turn logical notions (tautology, equivalence, entailment, satisfiability) into checks over valuations, and for each notion either a complete table or one line suffices, depending on the question.

## L1 — The gist (≤ 120 words)
Once we can compute a sentence's truth value on any valuation, we can define TFL versions of necessary truth, necessary falsity, equivalence, joint possibility and validity, and test each with a truth table. The symbol ⊨ abbreviates entailment and belongs to the metalanguage, unlike the connective →. Chapter 13 shows where TFL fails: it cannot validate the Daisy argument (four legs, so more than two legs), it handles borderline vagueness badly, and it does not properly capture the if…then of the God examples. Chapters 14–15 give shortcuts: skip lines that cannot be "bad", and use one-line partial tables when a single valuation settles the answer. This matters because it makes logical testing fast and shows what a test can and cannot prove.

**Prerequisites:** TFL connectives (¬, ∧, ∨, →, ↔) and their truth tables; building a complete truth table; valuation = an assignment of T/F to sentence letters (chapter 11); main logical operator.

## L2 — Key ideas (5–10 bullets)
- TFL versions of logical notions are defined by saying whether every, some or no valuation behaves a certain way: tautology, contradiction, equivalence, joint satisfiability, entailment (pp. 85–88).
- Truth tables decide all of these, since a complete table lists every valuation (pp. 85–88).
- "⊨" is a metalanguage abbreviation for entailment; "→" is a TFL connective. A → C is a tautology iff A ⊨ C, but the two symbols are different kinds of thing (pp. 89–90).
- ⊭ means that some valuation makes the premises true and the conclusion false. It does not give an entailment of the negation (p. 89).
- TFL has real limits: it cannot capture some valid English arguments, borderline cases, or the intended meaning of some "if…then" sentences (pp. 94–96).
- Shortcuts rest on three facts: a true disjunct makes a disjunction true, a false conjunct makes a conjunction false, and a true consequent or false antecedent makes a conditional true (p. 97–98).
- When testing validity, a line is bad exactly when all premises are true and the conclusion is false; lines with a true conclusion or a false premise can be dropped (pp. 98–99).
- Proving a universal claim needs a complete table; refuting it needs one line. Satisfiability is the reverse (pp. 102–105).

## L3 — Walkthrough

### Chapter 12 — Semantic concepts

**12.1 Tautologies and contradictions.** *Surrogate* = a TFL stand-in for an informal notion.
- A is a **tautology** iff it is true on every valuation. Test: it is true on every line of its complete truth table. Example from chapter 11: (H ∧ I) → H (p. 85).
- This is only a surrogate for necessary truth. "2+2 = 4" must be true, but the best TFL symbolization is a sentence letter, and no sentence letter is a tautology. Still, if an English sentence is adequately symbolized by a TFL tautology, it expresses a necessary truth (p. 86).
- A is a **contradiction** iff it is false on every valuation. Test: false on every line. Example from chapter 11: [(C ↔ C) → C] ∧ ¬(C → C) (p. 86).

**12.2 Equivalence.** A and B are **equivalent** iff on every valuation their truth values agree, i.e. no valuation gives them opposite values (p. 86). Example: ¬(P ∨ Q) and ¬P ∧ ¬Q. Compare the columns of the main operators (negation, conjunction).

| P | Q | ¬(P∨Q) | ¬P∧¬Q |
|---|---|---|---|
| T | T | F | F |
| T | F | F | F |
| F | T | F | F |
| F | F | T | T |

They match on all four rows, so they are equivalent (pp. 86–87).

**12.3 Satisfiability.** A₁,…,Aₙ are **jointly satisfiable** iff some valuation makes them all true. They are **jointly unsatisfiable** iff no valuation does. This is the surrogate for "jointly possible" (p. 87).

**12.4 Entailment and validity.** A₁,…,Aₙ **entail** C iff no valuation of the relevant sentence letters makes all the Aᵢ true and C false (p. 87). Example: do ¬L → (J ∨ L) and ¬L entail J?

| J | L | ¬L→(J∨L) | ¬L | J |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | T | T |
| F | T | T | F | F |
| F | F | F | T | F |

Only row 2 makes both premises true, and J is true there. So the entailment holds (pp. 87–88).

*Intuition note.* Each notion asks "every", "some" or "no" valuation. A truth table lists all valuations, so it answers every one of these questions.

**12.5 The double turnstile.** Write A₁,…,Aₙ ⊨ C for "A₁,…,Aₙ entail C". "⊨" is not a TFL symbol. It belongs to the metalanguage (augmented English; the object-language/metalanguage distinction is from chapter 8). So A, A → B ⊨ B abbreviates "The TFL sentences A and A → B entail B" (p. 88).
- Limiting case ⊨ C: no sentences on the left, so no valuation makes C false, so C is a tautology. A ⊨ (nothing on the right) says no valuation makes A true, so A is a contradiction (p. 89).
- A₁,…,Aₙ ⊭ C means some valuation makes all Aᵢ true and C false. It does *not* follow that A₁,…,Aₙ ⊨ ¬C, because another valuation might make them all true and C true. Example: P ⊭ Q and also P ⊭ ¬Q (p. 89).

**12.6 ‘⊨’ versus ‘→’.** Two observations (p. 89):
1. A ⊨ C iff no valuation makes A true and C false.
2. A → C is a tautology iff no valuation makes A → C false. A conditional is false only when its antecedent is true and its consequent false. So A → C is a tautology iff no valuation makes A true and C false.

Hence A → C is a tautology iff A ⊨ C. The difference is one of kind: "→" is a connective of TFL, and flanking it with two TFL sentences gives a longer TFL sentence. "⊨" is a symbol of augmented English, and it forms a metalanguage sentence that *mentions* the TFL sentences (p. 90). The English word implies is often used as a synonym for entails (⊨), and some logicians also use it for the conditional (→). Because this invites confusion, the authors avoid it as much as possible; whenever it is used, it means entails (p. 90).

*Intuition note.* "→" builds a new sentence that may be true or false. "⊨" is a claim *about* sentences, namely that no valuation separates premises from conclusion.

**Exercises** (pp.

### Chapter 13 — Limitations of TFL (pp. 94–96)
The authors say a validity test is a milestone, but its limits must be understood. They give four examples.

1. **Daisy.** "Daisy has four legs ∴ Daisy has more than two legs." TFL needs two different sentence letters, F and T, and F does not entail T. Yet the English argument is surely valid (p. 94). Later (chapter 26) the more expressive language FOL can symbolize "Daisy has four legs" properly, and its test will give the right answer (p. 95).
2. **Jan.** "Jan is neither bald nor not bald" would be symbolized ¬J ∧ ¬¬J, a contradiction. But the English sentence does not seem contradictory, since one might add that Jan is borderline bald (p. 94). Using a new letter N for "Jan is not bald" does not help. "Jan is both bald and isn't" is arguably self-contradictory, yet J ∧ N is not (p. 95). Some logicians propose letting sentence letters for vague sentences take values other than T and F. This is not universally accepted (pp. 95–96).
3. **Sentence 2:** "It's not the case that, if God exists, She answers malevolent prayers." Symbolized ¬(G → M), it entails G, so the symbolization seems to entail that God exists. That is strange, since surely even an atheist can accept sentence 2 without contradicting herself. The authors take this to show the symbolization does not express what is intended (p. 95).
4. **Sentence 3:** "If God exists, She does not answer malevolent prayers," symbolized G → ¬M. If G is false, G → ¬M is true, so the puzzle disappears. But then G → M is also true when G is false (p. 95). This is one of the **paradoxes of the material conditional**. Both conditionals come out true whenever G is false, though intuitively they should not both be true. The authors say this indicates that the if…then in these two examples is not properly captured by →, and they call the truth-functionality of TFL here a real limitation. The authors suggest treating it as a subjunctive conditional (section 10.3), which TFL cannot capture. Footnote: logicians have devised logics, called conditional logics or logics of counterfactuals, that deal with subjunctive conditionals better (p. 96).

Vagueness and the paradoxes of the material conditional are questions of philosophical logic. The authors say we must become proficient in TFL before we can discuss its limits (p. 96).

*Intuition note.* A truth table only sees which letters are true or false. If a symbolization loses the meaning that makes an English argument valid or a sentence consistent, the table gives a wrong verdict about the English.

### Chapter 14 — Truth table shortcuts

**14.1 Working through truth tables (p. 97–98).** You need not copy each sentence letter's value; you can refer back to it. Three shortcuts (p. 97–98):
- A disjunction is true whenever a disjunct is true, so once you find a true disjunct you need not evaluate the other.
- A conjunction is false whenever a conjunct is false.
- A conditional is true if its consequent is true or its antecedent is false.

Examples (p. 97–98):
- (P ∨ Q) ↔ ¬P gives F, F, T, F on the four rows (p. 97).
- (¬P ∨ ¬Q) ∨ ¬P: on rows with P false, ¬P is true, so the whole is true without computing ¬Q (p. 98).
- ¬(P ∧ ¬Q) ∧ ¬P: with P true, ¬P is false, so the whole is false (p. 98).
- ((P → Q) → P) → P: when P is true the consequent is true. When P is false, P → Q is true, so (P → Q) → P is T → F = false, and the whole conditional has a false antecedent. So it is true on all rows and is a tautology. It is an instance of Peirce's Law (p. 98).

**14.2 Testing for validity and entailment (pp. 98–101).** A **bad line** is a line where all premises are true and the conclusion is false. An argument is valid iff the table has no bad line (p. 98). So:
- If the conclusion is true on a line, the line is not bad.
- If any premise is false on a line, the line is not bad (p. 98–99).

Strategy: evaluate the conclusion first and ignore lines where it is true. Then evaluate the easiest premise, and ignore lines where it is false. Only the remaining lines need full work (p. 99).

*Example 1:* ¬L → (J ∨ L), ¬L ∴ J. J is true on rows 1–2. On row 3 (J = F, L = T), ¬L is false. Only row 4 remains (J = F, L = F). There ¬L is true, J ∨ L is false, so ¬L → (J ∨ L) is false. No bad lines, so the argument is valid (pp. 99–100).

*Example 2:* A ∨ B, ¬(B ∧ C) ∴ A ∨ ¬C. The conclusion is false only when A is false and C is true, i.e. on rows FTT and FFT. On FTT: A ∨ B is true but ¬(B ∧ C) is false. On FFT: A ∨ B is false. No bad lines, so the entailment holds (pp. 100–101).

The same shortcuts work for testing entailment (p. 101).

*Intuition note.* You are hunting for one row where the premises are all true and the conclusion false. Any row that already fails one of those requirements can be skipped.

### Chapter 15 — Partial truth tables (pp. 102–105)
A **partial truth table** has only some rows, used when one valuation settles the question.

- **Tautology.** Showing yes needs a complete table. Showing no needs one line where the sentence is false (p. 102).
- Worked example: show (U ∧ T) → (S ∧ W) is not a tautology. Set up one row with the whole sentence F. A conditional is false only if the antecedent is true and the consequent false. So U ∧ T is true (U = T, T = T) and S ∧ W is false, which needs at least one of S, W false. Choosing arbitrarily S = F, W = F gives a valuation (S F, T T, U T, W F) that falsifies it (p. 103).
- **Contradiction.** Yes needs a complete table; no needs one line where the sentence is true. For the same sentence, make U false, so the antecedent and hence the conditional are true. Example valuation: S F, T T, U F, W F (pp. 103–104).
- **Equivalence.** Yes needs a complete table; no needs one line with one sentence true and the other false (p. 104).
- **Joint satisfiability.** Yes needs one line making all sentences true; no (unsatisfiable) needs a complete table showing at least one sentence false on every row (p. 104).
- **Validity and entailment.** Yes needs a complete table. No (invalid, or failed entailment) needs one line with all premises true and the conclusion false (p. 104).

Summary table (p. 105):

| Question | If answer is Yes | If answer is No |
|---|---|---|
| tautology? | complete | one-line partial |
| contradiction? | complete | one-line partial |
| equivalent? | complete | one-line partial |
| satisfiable? | one-line partial | complete |
| valid? | complete | one-line partial |
| entailment? | complete | one-line partial |

*Intuition note.* Claims about *every* valuation need all rows. Claims about *some* valuation need one example. Satisfiability is an "exists" claim, so its pattern is the reverse of the others.

## Toy example (ours, not from the text)
**Does P ∨ Q entail P ∧ Q? Does P ∧ Q entail P ∨ Q?**

*Direction 1 (one-line partial table).* Try P = T, Q = F. P ∨ Q = T ∨ F = T. P ∧ Q = T ∧ F = F. This is a bad line (premise true, conclusion false), so P ∨ Q ⊭ P ∧ Q.

*Direction 2 (complete table).*

| P | Q | P∧Q | P∨Q |
|---|---|---|---|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

The only row with P ∧ Q true is row 1, and P ∨ Q is true there. No bad line, so P ∧ Q ⊨ P ∨ Q.

*Link to 12.6.* (P ∧ Q) → (P ∨ Q) has values T→T = T, F→T = T, F→T = T, F→F = T, so it is a tautology, as the iff in 12.6 predicts.

*Link to ⊭ vs ⊨ ¬.* On row 1 (T, T), P ∨ Q is true and ¬(P ∧ Q) is false, so P ∨ Q ⊭ ¬(P ∧ Q) as well. Both ⊭ claims hold together.

## Concepts
- [[tautology]] (new) — TFL sentence true on every valuation; surrogate for necessary truth (p. 85)
- [[contradiction]] (new) — TFL sentence false on every valuation; surrogate for necessary falsity (p. 86)
- [[logical-equivalence]] (new) — two sentences with the same truth value on every valuation (p. 86)
- [[joint-satisfiability]] (new) — some valuation makes all the sentences true; surrogate for "jointly possible" (p. 87)
- [[entailment]] (new) — no valuation makes all premises true and the conclusion false (p. 87)
- [[double-turnstile]] (new) — ⊨, a metalanguage abbreviation for entailment, not a TFL symbol (p. 88)
- [[validity / soundness]] — here the validity test is the absence of bad lines in a truth table (p. 98)
- [[use vs. mention]] — "⊨" forms sentences that mention TFL sentences; "→" is used inside TFL (p. 90)
- [[bad-line]] (new) — a row with all premises true and conclusion false (p. 98)
- [[partial-truth-table]] (new) — a table with only the row(s) needed to settle a question (p. 102)
- [[paradoxes-of-material-conditional]] (new) — "→" is true whenever the antecedent is false, so G → M and G → ¬M can both be true (p. 96)
- [[truth-functionality-limit]] (new) — the truth-functionality of TFL is a real limitation in the God examples, and TFL cannot capture subjunctive conditionals (p. 96)

## Canonical instances
- [[de-morgan-style-equivalence]] (new) — ¬(P ∨ Q) and ¬P ∧ ¬Q are equivalent (p. 86)
- [[peirce-law]] (new) — ((P → Q) → P) → P is a tautology (p. 98)
- [[daisy-four-legs]] (new) — valid English argument that TFL cannot validate (p. 94)
- [[jan-bald]] (new) — borderline vagueness vs. TFL's two truth values (p. 94)
- [[atheist-malevolent-prayers]] (new) — ¬(G → M) entails G; paradox of the material conditional (p. 95)

## Bridges (candidates)
- [structural-analogy] One-line partial table refutes a universal claim, while verification needs the complete table ↔ analytic-philosophy: falsifiability — one counter-instance refutes a universal claim, while no finite set of confirmations proves it (here a complete table does).
- [structural-analogy] Entailment ⊨ (no valuation with true premises and false conclusion) ↔ analytic-philosophy: validity (conclusion cannot be false if premises true) — this unit's version is a precise surrogate for the informal notion.
- [metaphor] Paradoxes of the material conditional ↔ analytic-philosophy: conditional and counterfactual talk — English "if" may behave unlike a truth function.

## Questions this raises
- If TFL cannot symbolize "Daisy has four legs" so that it entails "more than two legs", what extra structure does FOL add (chapter 26)?
- Should sentence letters for vague sentences be allowed values other than T and F, and what would a "validity" test look like then?
- Why is "if…then" in "if God exists, She does not answer malevolent prayers" not truth-functional, and how do conditional logics handle it?
- How many rows does a complete table need for n sentence letters, and how much do shortcuts save in the worst case?

## Exercises worth doing
- Ex. 12.C (p. 90) — basic validity tests using complete tables, including A → (A ∧ ¬A) ∴ ¬A — easy
- Ex. 12.K (pp. 92–93) — reason about how equivalence, tautology, unsatisfiability and entailment interlock — medium
- Ex. 12.L (p. 93) — is replacing a sentence by an equivalent one always safe for validity? — medium
- Ex. 14.A (p. 101) — practice the disjunction/conjunction/conditional shortcuts — easy
- Ex. 15.G (p. 107) — choose between complete and partial tables for satisfiability — medium
- Ex. 15.F (p. 107, items 6–7) — equivalence of longer sentences with repeated letters — hard

## Reading notes
- This unit is the second part of chapter-group III (Truth tables). It starts at section 12.1 (printed p. 85, the start of chapter 12) and ends at the end of chapter 15's exercises (printed p. 108). The split is at a chapter/section boundary; the previous chapter (11), which this unit refers back to, is not part of this unit.
- Printed numbers are given on each page label; printed = pdf − 10.
- Chapters 14 and 15 are structured as: 14.1–14.2 plus exercises; chapter 15 has no numbered sections.
- The text layer is garbled in tables; I rebuilt the tables from the page images and checked values by recomputation.
- Exercise 12.K items 3, 6 and 7 (pp. 92–93) show "(A ∧ B ∧ C)", "(A ∨ B)" and "(A ∨ B)" in the image, with no negation or other operator visible. I report them as printed. Exercise 15.I item 1 (p. 108) repeats an argument (A ↔ ¬(B ↔ A) ∴ A) that also appears in 15.C item 2 (p. 106).
- Chapter 13 says "four examples"; I took them as Daisy, sentence 1 (Jan), sentence 2 and the rephrased sentence 3 (pp. 94–95).
