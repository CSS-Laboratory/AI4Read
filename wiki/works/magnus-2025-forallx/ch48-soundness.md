---
id: magnus-2025-forallx/ch48-soundness
work: magnus-2025-forallx
unit: "48 Soundness"
pages: 390–397
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Soundness (TFL natural deduction is sound)

## L0 — One line
If a sentence C can be proved in TFL from assumptions Γ, then Γ really entails C, because every proof line is "shiny" and each rule keeps shininess.

## L1 — The gist (≤ 120 words)
The chapter asks whether TFL's natural deduction system can ever lead us astray, that is, prove a conclusion from premises that do not entail it. The answer is no. A line is "shiny" if the assumptions it depends on entail its sentence. The author shows that premises and assumptions are shiny, and that each rule, when all earlier lines are shiny, gives a shiny line (some cases are left as exercises). Since a proof is a sequence of such steps, every line is shiny. The last line is therefore entailed by the undischarged assumptions, which gives the Soundness Theorem. This matters because, as the author says, an unsound proof system could not be trusted.

**Prerequisites:** truth-table valuations; entailment (Γ ⊨ C: every valuation making all of Γ true makes C true); TFL natural deduction rules and subproofs; reasoning "line by line".

## L2 — Key ideas (5–10 bullets)
- Soundness means: if Γ ⊢ C (a proof exists), then Γ ⊨ C (entailment holds) (p. 390).
- "Shiny" = the assumptions a line depends on entail that line's sentence; this makes "leading us astray" precise (p. 391).
- The Shininess Lemma (every line of every proof is shiny) immediately gives the Soundness Theorem (p. 391).
- Premises and assumptions are shiny, since each is among the sentences it depends on (pp. 392–393).
- A rule is "rule-sound" if, whenever every earlier line is shiny, the line it produces is shiny. Checking this rule by rule, plus going through the proof line by line, proves the lemma (p. 392).
- Each check is a valuation argument: take any valuation making Δₙ true, and show it makes the new line true (pp. 393–396).
- ¬E relies on the fact that no valuation makes both A and ¬A true, so its entailment holds vacuously; ¬I relies on the fact that no valuation makes ⊥ true, which forces A to be false (pp. 395–396).
- Derived rules are covered because each can be replaced by basic rules (p. 396).

## L3 — Walkthrough

**Aim and statement (p. 390).** A proof system is *sound* (relative to a semantics) iff whenever C is proved from assumptions among Γ, then Γ genuinely entails C. Γ is a list of sentences. Intuitively, a sound system never lets you prove an invalid argument.

> **Soundness Theorem.** For any sentences Γ and C: if Γ ⊢ C, then Γ ⊨ C.

The plan is to check each rule individually (p. 390).

**Shiny lines and the lemma (p. 391).** A line is **shiny** iff the assumptions on which it depends entail the sentence on it. The author's example proof is:

1. F → (G ∧ H) (PR)
2. F (AS)
3. G ∧ H (→E, 1, 2)
4. G (∧E, 3)
5. F → G (→I, 2–4)

Line 1 is shiny iff $F\to(G\wedge H)\vDash F\to(G\wedge H)$. Line 4 is shiny iff $F\to(G\wedge H), F\vDash G$. Every line of this proof is shiny (p. 391).

> **Shininess Lemma.** Every line of every TFL-proof is shiny.

*Proof of the Soundness Theorem from the lemma (p. 391).* Suppose Γ ⊢ C. Then there is a proof with C on its last line, whose only undischarged assumptions are among Γ. By the lemma the last line is shiny, so Γ ⊨ C. QED

**Reduction to rules (p. 392).** Every line is a premise, an assumption, or the result of a rule. A premise A is in Γ, so Γ ⊨ A trivially. An assumption depends on itself, and A ⊨ A (p. 392). A rule is **rule-sound** iff, for all proofs, if a line is obtained by that rule and every earlier line is shiny, then the new line is shiny (p. 392).

*Proof of the lemma from rule-soundness (p. 392).* Go through any proof from line 1 onward. Line 1 must be a premise or an assumption, so it is shiny. Suppose all lines before line n are shiny. Then line n is either a premise or assumption (shiny), or it comes from a rule-sound rule applied to shiny lines (so shiny). Hence all lines are shiny.

**Notation (pp. 392–393).** $\Delta_i$ is the set of assumptions on which line $i$ depends. It includes all premises and the assumptions of subproofs still open at line $i$. *Premises and assumptions are shiny*: such an A is among $\Delta_n$, so $\Delta_n\vDash A$ (p. 393).

*Intuition note:* "Shiny" says that the line follows from the assumptions it depends on, so it cannot be false when they are all true. The proof works like a chain: premises and assumptions are shiny, and each rule keeps lines shiny, so the last line is shiny.

**Rule-by-rule checks.** In each case, assume all earlier lines are shiny and let $v$ be any valuation making all of $\Delta_n$ true.

- **∧I** (p. 393). From A (line i) and B (line j) infer A∧B (line n). All of $\Delta_i$ are among $\Delta_n$ and line $i$ is shiny, so $v$ makes A true. Likewise B. So $v$ makes A∧B true; hence $\Delta_n\vDash A\wedge B$. The author says the other lemmas have essentially this structure (p. 394).
- **∧E** (p. 394). From A∧B (line i) infer A (or B). $\Delta_i\subseteq\Delta_n$ and line i is shiny, so $v$ makes A∧B true, hence A true. So $\Delta_n\vDash A$.
- **∨I**: left as an exercise (p. 394).
- **∨E** (pp. 394–395). Lines: A∨B (m); subproof A (AS, i) … C (j); subproof B (AS, k) … C (l); C (n). Since line m is shiny, $v$ makes A∨B true, so it makes A true or B true.
  - *Case 1:* $v$ makes A true. All of $\Delta_i$ are among $\Delta_n$, except possibly A, which $v$ also makes true. So $v$ makes all of $\Delta_i$ true. Line j is shiny and $\Delta_j$ are just $\Delta_i$, so $\Delta_i\vDash C$. So $v$ makes C true.
  - *Case 2:* B is true; the same reasoning with lines k, l.
  - Either way $v$ makes C true, so $\Delta_n\vDash C$.
  - The page's proof says "∧E is used on line n"; this is a misprint for ∨E (see Reading notes).
- **¬E** (p. 395). From A (line i) and ¬A (line j) infer ⊥ (line n). $\Delta_i,\Delta_j\subseteq\Delta_n$ and both lines are shiny. So any valuation making $\Delta_n$ true would make both A and ¬A true. No valuation does that, so none makes $\Delta_n$ true, and $\Delta_n\vDash\bot$ *vacuously*.
- **X**: left as an exercise (pp. 395–396).
- **¬I** (p. 396). Subproof: A (AS, line i) … ⊥ (line j); infer ¬A (line n). Line j is shiny, and no valuation makes ⊥ true. So no valuation makes all of $\Delta_j$ true, and $\Delta_j$ are just $\Delta_i$. Since $v$ makes all of $\Delta_n$ true, it must make A false, so ¬A true. So $\Delta_n\vDash\neg A$.
- **IP, →I, →E, ↔I, ↔E**: left as exercises (p. 396).

*Intuition note:* In ¬E the argument runs by contradiction: the assumptions cannot all be true at once, so "entails ⊥" holds trivially. In ¬I a similar fact (no valuation makes ⊥ true, so none makes all of Δᵢ true) forces A to be false whenever all of Δₙ are true.

**Derived rules (pp. 396–397).** Suppose a derived rule gives A on line n and every earlier line is shiny. The derived rule's use can be replaced by several basic-rule steps, without further assumptions, so that A appears on some line $n+k$. Applying basic rule-soundness $k+1$ times shows line $n+k$ is shiny. Hence the derived rule is rule-sound (pp. 396–397).

**Conclusion (p. 397).** Every rule is rule-sound, so the Shininess Lemma holds, and so does the Soundness Theorem. A formal proof is a sequence of rule applications. No single application leads astray, so no proof does (p. 397).

## Toy example (ours)
Check ∧E by hand on the one-line proof: 1. A∧B (PR); 2. A (∧E, 1). Here $\Delta_2=\{A\wedge B\}$.

| A | B | A∧B | A |
|---|---|-----|---|
| T | T | T | T |
| T | F | F | T |
| F | T | F | F |
| F | F | F | F |

Only row 1 makes A∧B true, and A is true there. So $A\wedge B\vDash A$: line 2 is shiny.

Contrast with a bad rule "from A∨B infer A". With premise A∨B, take A = F, B = T. Then A∨B is true and A is false. So that line is not shiny and the rule is not rule-sound.

## Concepts
- [[validity / soundness]] — here a *proof system* is sound iff Γ ⊢ C implies Γ ⊨ C (p. 390).
- [[soundness-theorem]] (new) — for any Γ and C: if Γ ⊢ C then Γ ⊨ C (p. 390).
- [[shiny-line]] (new) — a line whose dependency assumptions entail its sentence; the author notes the word is not standard (p. 391).
- [[shininess-lemma]] (new) — every line of every TFL-proof is shiny (p. 391).
- [[rule-soundness]] (new) — a rule that, applied with all earlier lines shiny, yields a shiny line (p. 392).
- [[vacuous-entailment]] (new) — if no valuation makes all of Δₙ true, then Δₙ ⊨ ⊥ holds vacuously, as in the ¬E check (p. 395).

## Canonical instances
- [[shiny-proof-example]] — the proof of F → G from F → (G ∧ H), every line shiny (p. 391).
- [[derived-rules-reduction]] — derived rules replaced by basic rules to inherit rule-soundness (p. 396).

## Bridges (candidates)
- [structural-analogy] Line-by-line argument that every line is shiny ↔ mathematical induction: base case (premises, assumptions) plus step (rules preserve the property) — the author only says "and so on" (p. 392).
- [metaphor] Rule-soundness ↔ truth-preserving inference: a rule never takes you from truth to falsity.

## Questions this raises
- Is the converse true: if Γ ⊨ C, is there always a proof Γ ⊢ C? (This chapter proves only one direction.)
- Which step of the argument would fail if a rule like "from A∨B infer A" were added?
- How does the proof change if more connectives or rules are added to the system?

## Exercises worth doing
- Ex. A1 (p. 397) — ∨I is rule-sound (hint: like ∧E) — easy
- Ex. A2 (p. 397) — X is rule-sound (hint: like ¬E) — easy
- Ex. A3 (p. 397) — →I is rule-sound (hint: like ∨E) — medium
- Ex. A4 (p. 397) — →E is rule-sound — easy
- Ex. A5 (p. 397) — IP is rule-sound (hint: like ¬I) — medium

## Reading notes
- Printed page = pdf page − 10 (pdf 400 = p. 390).
- Misprint, p. 394: the ∨E proof says "∧E is used on line n"; the displayed proof shows ∨E.
- p. 392 has a typo: "since the any assumption Adepends on itself".
- p. 396, ¬I: the page says "all of Δₙ are among Δᵢ, with the possible exception of A itself". The natural reading is that $\Delta_i$ is $\Delta_n$ plus A. The argument works either way.
- Footnote p. 391: "shiny" is not standard among logicians.
- Not covered here: the exercise cases (∨I, X, →I, →E, IP, ↔I, ↔E). The text proves only ∧I, ∧E, ∨E, ¬E, ¬I.
