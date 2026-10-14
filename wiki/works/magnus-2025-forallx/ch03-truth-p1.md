---
id: magnus-2025-forallx/ch03-truth-p1
work: magnus-2025-forallx
unit: "Part III, Chapters 9–11 (up to the end of Ch. 11): Characteristic truth tables; Truth-functional connectives; Complete truth tables"
pages: 68-84
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
# III Truth tables (part 1/2)

## L0 — One line
In TFL the truth value of a compound sentence depends only on the truth values of its parts, so a table listing every assignment of True/False to the sentence letters shows when any sentence is true.

## L1 — The gist (≤ 120 words)
How can we calculate whether a sentence of TFL is true? The authors give each connective a characteristic truth table. They define "truth-functional" (the parts' values uniquely fix the whole's value) and stipulate the material conditional (→ is false exactly when its first part is true and its second false). They argue that TFL only symbolizes English sentences, keeping their truth values, not their meanings, and that → cannot capture subjunctive ("would have") conditionals. A complete truth table lists every valuation (assignment of truth values to the sentence letters), so $2^n$ rows for $n$ letters. The column under the main logical operator (the connective that builds the whole sentence) gives the whole sentence's value on each row.

**Prerequisites:** the five TFL connectives (¬, ∧, ∨, →, ↔) and sentence letters from chapter 5; the idea of a main logical operator; powers of 2.

## L2 — Key ideas (5–10 bullets)
- Each connective has a characteristic truth table, which says how it maps truth values of parts to the truth value of the whole (pp. 69–71).
- ∧, ∨ and ↔ are commutative; → is not (pp. 70–71).
- A connective is truth-functional iff the truth values of its constituents uniquely determine the truth value of the whole. Every TFL connective is; "It is necessarily the case that…" is not (pp. 72–73).
- TFL "symbolizes" rather than "translates". A symbolization key only stipulates that a TFL letter takes the same truth value as an English sentence (pp. 73–74).
- The table for → is justified with Edgington's shapes example. → is the best candidate for a truth-functional conditional (the best TFL can provide), but it cannot handle subjunctive conditionals (pp. 75–76).
- A valuation assigns truth values to sentence letters. A complete truth table has one row per valuation, so $2^n$ rows for $n$ letters (pp. 77, 81).
- The column under the main logical operator gives the truth value of the whole sentence on each valuation (pp. 79–80).
- Brackets must not be dropped, except the outermost pair. Grouping matters for → and for mixed ∨/∧ (p. 82).

## L3 — Walkthrough

### Chapter 9. Characteristic truth tables
- Any TFL sentence is built from sentence letters, possibly joined by connectives. Its truth value depends only on the truth values of its letters. For example, to know the value of ‘(D ∧ E)’ you only need the values of ‘D’ and ‘E’ (p. 69).
- ‘T’ and ‘F’ abbreviate the truth values True and False. The truth values are not letters (p. 69).
- **Negation:** if $\mathscr A$ is true, ¬$\mathscr A$ is false, and if ¬$\mathscr A$ is true, $\mathscr A$ is false (p. 69).
- **Conjunction:** $\mathscr A\land\mathscr B$ is true iff both are true. **Disjunction:** ∨ is always inclusive "or", and $\mathscr A\lor\mathscr B$ is true iff at least one of the two is true (p. 70).

| $\mathscr A$ | $\mathscr B$ | $\mathscr A\land\mathscr B$ | $\mathscr A\lor\mathscr B$ | $\mathscr A\to\mathscr B$ | $\mathscr A\leftrightarrow\mathscr B$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | F | T | T | F |
| F | F | F | F | T | T |

(Rows from pp. 70–71; negation is the two-row table T↦F, F↦T.)
- A connective is **commutative** if swapping its two inputs never changes the output's truth value. ∧ and ∨ are commutative (p. 70).
- **Conditional:** the authors admit "Conditionals are a mess" and its philosophy is contentious. They stipulate that $\mathscr A\to\mathscr B$ is false iff $\mathscr A$ is true and $\mathscr B$ is false. This is the **material conditional** (p. 70). It is not commutative: $\mathscr A\to\mathscr B$ and $\mathscr B\to\mathscr A$ have different tables (p. 71).
- **Biconditional:** since it should be the same as the conjunction of the conditionals in both directions, its table is as above. It is the material biconditional and is commutative (p. 71).

*Intuition note:* Each connective is a small machine that takes truth values in and gives one truth value out. Nothing else about the sentences matters.

### Chapter 10. Truth-functional connectives
**10.1 Truth-functionality.** A connective is truth-functional iff the truth value of a sentence with that connective as main logical operator is uniquely determined by the truth value(s) of its constituent sentence(s) (p. 72). Every TFL connective is truth-functional, which is why TFL is "truth-functional logic" (pp. 72–73).
- Counterexample: the English prefix "It is necessarily the case that…". Both "2 + 2 = 4" and "Shostakovich wrote fifteen string quartets" are true. The first is necessarily true. The second is not, since, the authors say, had he died earlier he would have failed to finish Quartet no. 15, and had he lived longer he might have written more. The same input value (true) gives different outputs, so the prefix is not truth-functional (p. 73).

**10.2 Symbolizing versus translating.** TFL ignores everything except the contribution of truth values (sarcasm, poetry, implicature, emphasis) (p. 73).
- Five English sentences about Dana (the "and", "although", "despite", "but also" and "notwithstanding" versions) are all symbolized by the same sentence, perhaps ‘L ∧ N’ (pp. 73–74).
- A good translation should preserve certain facets of meaning, and TFL cannot do that, so the authors say "symbolizing" (p. 74).
- A symbolization key such as "L: Dana is a logician" only stipulates that the TFL sentence takes the same truth value as the English sentence (p. 74). Other textbooks (the authors' contrast) read it as giving the TFL sentence that meaning.

**10.3 Indicative versus subjunctive conditionals.** The authors justify the table for → following Edgington (p. 75).
- Claim, made without seeing the drawing: "If any shape is grey, then that shape is also circular." Lara draws A (grey, circular), C and D (not grey).
  - The claim has no counterexample, so it is true. Hence its instances are true:
    - A: true antecedent, true consequent → true.
    - C: false antecedent, true consequent → true.
    - D: false antecedent, false consequent → true (p. 75).
- If Lara also draws B (grey, not circular), the claim is false. So "If B is grey, then it is circular" (true antecedent, false consequent) is false (p. 75).
- Since TFL connectives must be truth-functional, these four cases fix the whole table of → (p. 76).
- The authors conclude that → is the best candidate for a truth-functional conditional, "the best conditional that TFL can provide" (p. 76).
- Limit: two Hillary Clinton conditionals have false antecedents and false consequents. Sentence 1 ("…first woman president") is true. Sentence 2 ("…helium-filled balloon") is false. So the whole's truth value is not determined by its parts (p. 76).
- These are **subjunctive** conditionals: they ask us to imagine something contrary to fact and evaluate what *would* have happened. → cannot handle that. The authors defer more to chapter 13 and call TFL "an intrinsically limited language" (p. 76).

*Intuition note:* In the shapes example, the general claim is true when it has no counterexample and false once a counterexample is drawn. "Would have" conditionals depend on more than the actual truth values, so a truth table cannot capture them.

### Chapter 11. Complete truth tables
- A **valuation** is any assignment of truth values to particular sentence letters. Each row of a truth table is a possible valuation, and the complete table covers all of them (p. 77).

**11.1 A worked example: ‘(H ∧ I) → H’** (pp. 78–79)
1. Four valuations of H, I: TT, TF, FT, FF (p. 78).
2. Copy the letters' values under the letters (p. 78).
3. The subsentence (H ∧ I) is a conjunction. It is true only on row 1: T, F, F, F (p. 78).
4. The whole is a conditional with antecedent (H ∧ I) and consequent H. Row by row: T→T = T, F→T = T, F→F = T, F→F = T (p. 79).

The main logical operator's column is all T. So the sentence is true on every valuation (p. 79). On paper the steps share one table. The column under the main operator matters most (the other columns are bookkeeping), so the authors put it in bold and advise emphasizing it (pp. 79–80).

**11.2 Building complete truth tables** (pp. 80–81)
- One letter gives 2 rows, even if repeated. ‘[(C ↔ C) → C] ∧ ¬(C → C)’ has main-operator column F, F, so it is false on every valuation (p. 80).
- For ‘M ∧ (N ∨ P)’ there are 8 rows. The main column is T, T, T, F, F, F, F, F, so the sentence can be true or false (p. 81).
- With $n$ different letters the table has $2^n$ lines (16, 32, 64 for 4, 5, 6 letters) (p. 81).
- Filling rule: right-most letter alternates T, F; the next column left uses blocks of two; then four; then eight, and so on (p. 81).

*Intuition note:* Each extra letter doubles the rows, because each earlier row splits into "new letter true" and "new letter false". Truth tables grow fast.

**11.3 More about brackets** (p. 82)
- ((A ∧ B) ∧ C) and (A ∧ (B ∧ C)) are truth-functionally equivalent, and likewise for ∨. Still, ‘A ∧ B ∧ C’ and ‘A ∨ B ∨ C’ are ambiguous, so brackets should not be dropped (p. 82).
- The authors say the bracket-independence is guaranteed by the tables of ∧ and ∨ and holds only for conjunctions, disjunctions and biconditionals (p. 82).
- ((A → B) → C) and (A → (B → C)) have different tables. ((A ∨ B) ∧ C) and (A ∨ (B ∧ C)) also differ. So ‘A → B → C’ and ‘A ∨ B ∧ C’ are "dangerously ambiguous". The moral: never drop brackets except the outermost ones (p. 82).

## Toy example (ours)
Sentence: ‘¬(A ∧ B) → A’. There are two letters, so $2^2 = 4$ rows.

| A | B | A ∧ B | ¬(A ∧ B) | ¬(A ∧ B) → A |
|---|---|---|---|---|
| T | T | T | F | F→T = **T** |
| T | F | F | T | T→T = **T** |
| F | T | F | T | T→F = **F** |
| F | F | F | T | T→F = **F** |

The main-operator column is T, T, F, F. It is true on some valuations and false on others. It is false exactly where the antecedent is true and A is false, as the → rule says.

## Concepts
- [[characteristic-truth-table]] (new) — the table giving a connective's output for every input combination (p. 69)
- [[truth-functional-connective]] (new) — connective whose compound's truth value is uniquely fixed by its constituents' truth values (p. 72)
- [[commutative-connective]] (new) — connective whose compound keeps its truth value when the two inputs are swapped (p. 70)
- [[material-conditional]] (new) — → stipulated false iff antecedent true and consequent false (p. 70)
- [[symbolizing-vs-translating]] (new) — TFL symbolization matches truth values only, not meaning (p. 74)
- [[indicative-vs-subjunctive-conditional]] (new) — subjunctive conditionals ask us to imagine something contrary to fact and evaluate what *would* have happened, unlike indicative ones; the authors say such considerations cannot be tackled with → (p. 76)
- [[valuation]] (new) — an assignment of truth values to sentence letters (p. 77)
- [[complete-truth-table]] (new) — table with one line per valuation of the relevant letters, $2^n$ lines for $n$ letters (pp. 80–81)
- [[main-logical-operator]] (new) — the connective whose column gives the whole sentence's value (p. 79)

## Canonical instances
- [[shostakovich-quartets-necessity]] (new) — a non-truth-functional English operator (p. 73)
- [[dana-logician-nice]] (new) — five English sentences symbolized the same way (p. 73)
- [[lara-shapes-conditional]] (new) — Edgington-style derivation of the → table (p. 75)
- [[hillary-subjunctive-conditionals]] (new) — same truth values for parts, different values for wholes (p. 76)

## Bridges (candidates)
- [structural-analogy] TFL ignoring "snide implicature" and emphasis ↔ analytic-philosophy: Grice's conversational implicature — the text names implicature as something TFL drops.
- [structural-analogy] Truth-functionality ↔ Frege-style reference: the truth value of a whole depends only on the truth values of its parts (a canon link; not stated in this unit).
- [metaphor] Truth table as exhaustive check of all "possible worlds" ↔ necessity: a row stands for a possible valuation.

## Questions this raises
- What exactly goes wrong when → is used for subjunctive conditionals (chapter 13)?
- How can truth tables test whether two sentences are equivalent or an argument is valid?
- Is ↔ really bracket-independent? Ex. B.5 asks us to check.
- Can a table with $2^n$ rows be shortened when $n$ is large?

## Exercises worth doing
- Ex. A.4 (p. 83) — build a table for ‘(A → B) ∨ (B → A)’ and compare rows — difficulty: easy
- Ex. A.1–A.2 (p. 83) — one-letter tables (two rows each); compare a sentence true on both rows with one that is not — difficulty: easy
- Ex. B.3–B.4 (p. 83) — shows that bracket placement changes truth tables for mixed ∨/∧ and for → — difficulty: medium
- Ex. B.5 (p. 83) — tests whether ↔ is bracket-independent — difficulty: medium
- Ex. C.2 or C.5 (p. 83) — mark the main-operator column in larger tables — difficulty: medium
- Ex. D.5 (p. 84) — three letters, nested ↔ and →, 8 rows — difficulty: hard

## Reading notes
- This part starts at the Part III title page (printed p. 68) and ends at the end of Chapter 11's exercises (printed p. 84). It was split at a section boundary, and the rest of Part III is not covered.
- Printed page labels were given on every page, so I cite them (printed = pdf − 10).
- The text layer misaligns the truth-table columns and loses the bold marking of the main-operator column (for example the ‘M ∧ (N ∨ P)’ table). I read the values from the page images.
- The authors say bracket-independence holds for biconditionals (p. 82), yet Exercise B.5 (p. 83) asks the reader to "check whether" the two ↔ sentences match. I record both as printed.
