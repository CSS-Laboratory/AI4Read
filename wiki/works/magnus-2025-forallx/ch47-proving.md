---
id: magnus-2025-forallx/ch47-proving
work: magnus-2025-forallx
unit: "47 Proving equivalences"
pages: 381-389
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Proving equivalences

## L0 — One line
Because equivalent parts can be swapped inside a sentence and sentence letters can be replaced by any sentence, a small table of basic equivalences lets you prove equivalences, and find normal forms, by chains of rewriting steps.

## L1 — The gist (≤ 120 words)
The chapter asks how to show that two TFL sentences are equivalent without a truth table or a full natural deduction proof. Answer: two facts about replacement (swapping equivalent parts, and substituting sentences for sentence letters) justify a chain of equivalences, each step using a law from a short list (Table 47.1). The same method finds a sentence in disjunctive normal form (DNF), which in the chapter's example is much shorter than the one built from a truth table in chapter 45; the truth-table method gets hard for more than a handful of letters because a table for n letters has 2^n lines. The chapter ends with exercises asking for chains leading to DNF and to conjunctive normal form (CNF).

**Prerequisites:** truth tables; equivalence and entailment in TFL; DNF and CNF (chapter 45); De Morgan's laws.

## L2 — Key ideas (5–10 bullets)
- Replacing a part of a sentence by an equivalent sentence gives an equivalent sentence, because truth values are computed from the inside out (pp. 381–382).
- If two sentences are equivalent, then replacing a sentence letter in both by the same sentence keeps them equivalent (p. 383).
- A truth table for ‘¬¬A’ and ‘A’ does not itself cover instances such as ‘¬¬(B → C)’; the substitution fact does (p. 383).
- A chain of equivalences moves from one sentence to another by replacing parts, citing a law at each step (pp. 383–385).
- Table 47.1 lists the basic laws: DN, Cond, Bicond, DeM, Comm, Dist, Assoc, Id, Abs, Simp (p. 386).
- DNF can be reached by chains: remove → and ↔, push negations inward, then distribute ∧ over ∨ (pp. 387–388).
- The chain method gave a shorter DNF than the truth-table method for the same sentence (p. 389).

## L3 — Walkthrough

### 47.1 Substitutability of equivalents
- P and Q are equivalent iff their truth values agree on every valuation. Equivalent sentences are not identical: ‘¬¬A’ begins with ‘¬’, ‘A’ does not (p. 381).
- Example: ‘¬¬A → B’ and ‘A → B’ are equivalent; the second comes from the first by replacing ‘¬¬A’ with ‘A’ (p. 381).
- Why: a truth value is computed from the inside out. The value of ‘¬¬A → B’ depends only on the value of ‘¬¬A’, the value of ‘B’ and the table for ‘→’. Equivalent parts always have the same value, so swapping them cannot change the whole (p. 382). Any other sentence equivalent to ‘¬¬A’, e.g. ‘A ∧ (A ∨ A)’, works the same way (p. 382).
- Notation: $\mathcal{R}(\mathcal{P})$ is a sentence containing $\mathcal{P}$ as a part; $\mathcal{R}(\mathcal{Q})$ is the result of replacing that occurrence by $\mathcal{Q}$ (p. 382).

**Fact 1:** If $\mathcal{P}$ and $\mathcal{Q}$ are equivalent, then so are $\mathcal{R}(\mathcal{P})$ and $\mathcal{R}(\mathcal{Q})$ (p. 382).

- So $\mathcal{R}(\mathcal{P}) \leftrightarrow \mathcal{R}(\mathcal{Q})$ is a tautology. But natural deduction proofs differ "wildly" for different $\mathcal{R}$. Exercise suggested: prove $\vdash (\neg\neg P \to Q) \leftrightarrow (P \to Q)$ and $\vdash (\neg\neg P \land Q) \leftrightarrow (P \land Q)$ and compare (p. 382).

**Fact 2:** If $\mathcal{P}(A)$ and $\mathcal{Q}(A)$ both contain the sentence letter ‘A’ and are equivalent, then $\mathcal{P}(\mathcal{R})$ and $\mathcal{Q}(\mathcal{R})$ (‘A’ replaced by $\mathcal{R}$ in both) are equivalent (p. 383).

- Example: replacing ‘A’ by ‘¬C’ in ‘A ∧ B’ and ‘B ∧ A’ gives ‘¬C ∧ B’ and ‘B ∧ ¬C’, still equivalent (p. 382).
- A truth table for ‘¬¬A’ and ‘A’ has 2 lines. It does not itself show ‘¬¬(B → C)’ ≡ ‘B → C’, which needs 4 lines (p. 383).

*Intuition note:* Fact 1 says you can edit inside a sentence. Fact 2 says a law proved for letters holds for any sentences put in their place. Together, once two sentences are shown equivalent, all their common instances are equivalent too.

### 47.2 Chains of equivalences
- Method: keep a catalog of simple equivalences; replace parts of the first sentence by equivalent parts until you reach the second (p. 383).
- Fact 2 gives: for any $\mathcal{P}$, $\neg\neg\mathcal{P}$ and $\mathcal{P}$ are equivalent (from the truth table for ‘A’). Fact 1 then lets us use that inside larger sentences (p. 383).
- De Morgan's Laws: $\neg(A \land B) \Leftrightarrow (\neg A \lor \neg B)$ and $\neg(A \lor B) \Leftrightarrow (\neg A \land \neg B)$. They can be checked by two truth tables or four natural deduction proofs. By Fact 2, they hold for any $\mathcal{P}, \mathcal{Q}$ (p. 384).
- Worked example: push negations inward in ‘¬(R ∨ (S ∧ T))’ (pp. 384–385).
  1. Second DeM, with $\mathcal{P}$ = ‘R’ and $\mathcal{Q}$ = ‘(S ∧ T)’: ‘(¬R ∧ ¬(S ∧ T))’.
  2. First DeM on the part ‘¬(S ∧ T)’: ‘(¬R ∧ (¬S ∨ ¬T))’.
  3. Now every ‘¬’ attaches directly to a sentence letter.
- Each step is written down with the name of the law used (p. 385).
- Table 47.1 (p. 386) lists, for any $\mathcal{P},\mathcal{Q},\mathcal{R}$:
  - DN: $\neg\neg P \Leftrightarrow P$.
  - Cond: $(P \to Q) \Leftrightarrow (\neg P \lor Q)$; $\neg(P \to Q) \Leftrightarrow (P \land \neg Q)$.
  - Bicond: $(P \leftrightarrow Q) \Leftrightarrow ((P \to Q) \land (Q \to P))$.
  - DeM: the two laws above.
  - Comm: for ∨ and ∧.
  - Dist: $P \land (Q \lor R) \Leftrightarrow (P \land Q) \lor (P \land R)$; $P \lor (Q \land R) \Leftrightarrow (P \lor Q) \land (P \lor R)$.
  - Assoc: for ∨ and ∧.
  - Id: $(P \lor P) \Leftrightarrow P$; $(P \land P) \Leftrightarrow P$.
  - Abs: $P \land (P \lor Q) \Leftrightarrow P$; $P \lor (P \land Q) \Leftrightarrow P$.
  - Simp: $P \land (Q \lor \neg Q) \Leftrightarrow P$; $P \lor (Q \land \neg Q) \Leftrightarrow P$; $P \lor (Q \lor \neg Q) \Leftrightarrow (Q \lor \neg Q)$; $P \land (Q \land \neg Q) \Leftrightarrow (Q \land \neg Q)$.

### 47.3 Finding equivalent normal forms
- The chapter 45 method (truth table, then read off DNF/CNF) has two drawbacks. The result is not always shortest. And a table for $n$ letters has $2^n$ lines, so it is hard for more than a handful of letters (p. 385).
- Alternative: apply basic equivalences until the sentence is in DNF. DNF conditions (p. 387):
  - (dnf1) only ¬, ∧, ∨;
  - (dnf2) every ¬ is immediately followed by an atomic sentence;
  - (dnf3) no ∨ within the scope of any ∧.
- Worked example, start: $\neg(A \land \neg C) \land (\neg A \to \neg B)$ (pp. 387–388).
  1. Cond: $\neg(A \land \neg C) \land (\neg\neg A \lor \neg B)$.
  2. DN: $\neg(A \land \neg C) \land (A \lor \neg B)$. Now (dnf1) holds.
  3. DeM: $(\neg A \lor \neg\neg C) \land (A \lor \neg B)$.
  4. DN: $(\neg A \lor C) \land (A \lor \neg B)$. This is in CNF; (dnf2) holds, (dnf3) does not.
  5. Dist (with $\mathcal{P}$ = ‘(¬A ∨ C)’, $\mathcal{Q}$ = ‘A’, $\mathcal{R}$ = ‘¬B’): $((\neg A \lor C) \land A) \lor ((\neg A \lor C) \land \neg B)$.
  6. Comm on the left disjunct: $(A \land (\neg A \lor C)) \lor ((\neg A \lor C) \land \neg B)$.
  7. Dist: $((A \land \neg A) \lor (A \land C)) \lor ((\neg A \lor C) \land \neg B)$.
  8. Comm on the right part: $((A \land \neg A) \lor (A \land C)) \lor (\neg B \land (\neg A \lor C))$.
  9. Dist: $((A \land \neg A) \lor (A \land C)) \lor ((\neg B \land \neg A) \lor (\neg B \land C))$. This is in DNF.
  10. Simplify: ‘(A ∧ ¬A)’ is a contradiction, and a contradiction ∨ P is equivalent to P (Simp). Comm: $((A \land C) \lor (A \land \neg A)) \lor ((\neg B \land \neg A) \lor (\neg B \land C))$.
  11. Simp: $(A \land C) \lor ((\neg B \land \neg A) \lor (\neg B \land C))$.
- This is much simpler than the chapter 45 DNF. The starting sentence has exactly the truth table used there for $\mathcal{S}$ (section 45.2); the earlier result had four disjuncts: $((((A\land B)\land C)\lor((A\land\neg B)\land C))\lor((\neg A\land\neg B)\land C))\lor((\neg A\land\neg B)\land\neg C)$ (p. 389).

*Intuition note:* Rewriting by laws is like simplifying algebra: each step keeps the truth conditions and changes the shape. Here the goal shape is DNF, and the path was shorter than building from a truth table.

## Toy example (ours)
Show ‘¬(A → B)’ ≡ ‘A ∧ ¬B’ by a chain from ‘¬(A → B)’:
1. Cond on the inside: ¬(¬A ∨ B).
2. DeM: (¬¬A ∧ ¬B).
3. DN: (A ∧ ¬B).

Check on A = T, B = F: the start is ¬(F) = T and the end is T ∧ T = T. On A = T, B = T: the start is ¬(T) = F and the end is T ∧ F = F. ✓.

## Concepts
- [[logical equivalence]] (new) — same truth value on every valuation (p. 381)
- [[substitutability of equivalents]] (new) — replacing a part by an equivalent gives an equivalent sentence (p. 382)
- [[substitution for sentence letters]] (new) — equivalence is preserved when a letter is replaced by the same sentence in both (p. 383)
- [[chain of equivalences]] (new) — a sequence of replacements, each justified by a basic law (p. 383)
- [[normal forms DNF/CNF]] (new) — sentences of a restricted shape; DNF is conditions dnf1–dnf3 (p. 387)
- [[validity / soundness]] — not used directly here; the text notes that if two sentences are equivalent, either one entails the other (p. 381)

## Canonical instances
- [[de-morgan-pushing-negations]] — ¬(R ∨ (S ∧ T)) becomes (¬R ∧ (¬S ∨ ¬T)) (pp. 384–385)
- [[dnf-by-chain]] — DNF of ¬(A ∧ ¬C) ∧ (¬A → ¬B) by a chain, shorter than the truth-table DNF (pp. 387–389)

## Bridges (candidates)
- [structural-analogy] Chains of equivalences ↔ algebra: simplifying an expression by replacing sub-expressions with equal ones.
- [same-math] Normal-form rewriting ↔ Boolean algebra: the same laws (De Morgan, distribution, absorption).

## Questions this raises
- Does the chain method always terminate in DNF if the laws are applied in a sensible order?
- Can a chain ever be longer than the corresponding truth table?
- What guarantees that the laws in Table 47.1 are enough to reach any equivalent sentence?

## Exercises worth doing
- Ex. A (p. 389) — find DNF and CNF chains for six sentences, simplifying with Id, Abs, Simp — difficulty: medium
- Ex. (p. 382, in text) — prove ⊢ (¬¬P → Q) ↔ (P → Q) and ⊢ (¬¬P ∧ Q) ↔ (P ∧ Q), then compare — difficulty: medium

## Reading notes
- Printed = pdf − 10.
- On p. 385 the chain display marks boxes in the image; the text layer garbles it. The final line there is shown in the image as ‘(¬(R ∧ (¬S ∨ ¬T))’, with an extra opening bracket after ‘¬’ (so the brackets do not balance) compared with the prose result ‘(¬R ∧ (¬S ∨ ¬T))’.
- The p. 388 line after the first Dist has an unbalanced bracket in the source: ‘((¬A ∨ C) ∧ A))’.
- The "Questions this raises" items are our own, not from the text.
