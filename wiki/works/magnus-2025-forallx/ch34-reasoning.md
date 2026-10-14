---
id: magnus-2025-forallx/ch34-reasoning
work: magnus-2025-forallx
unit: "34 Reasoning about interpretations"
pages: 289-292
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Reasoning about interpretations

## L0 — One line
To show that a sentence of FOL is a validity (or that an entailment holds), one must reason in the metalanguage about all interpretations, while one counter-interpretation is enough to refute the claim.

## L1 — The gist (≤ 120 words)
How can we show that an FOL sentence is true in every interpretation, when there are infinitely many interpretations? We cannot check them one by one. Instead we reason in English about an arbitrary interpretation, using the fact that the connectives also apply to satisfaction. The same holds for contradiction, equivalence, unsatisfiability, valid arguments and entailment. By the summary table, one interpretation (or counter-interpretation) is enough for the negative claims (not a validity, and so on) and for the positive claim of satisfiability. This differs from TFL, where every truth table has finitely many lines. The unit shows why such reasoning is hard with the tools so far.

**Prerequisites:** FOL interpretations and domains; satisfaction of a formula by an object; validity, entailment and equivalence; truth tables (TFL, the earlier logic of truth tables).

## L2 — Key ideas (5–10 bullets)
- One interpretation in which a sentence is false shows it is not a validity (p. 289).
- To show a validity, we must reason about all interpretations; checking many is never enough, since there are infinitely many (p. 289).
- Such reasoning is done in the metalanguage (English about FOL), not in FOL (p. 290).
- For quantified sentences we reason about an arbitrary object satisfying an open formula, because a formula such as $R(x,x)\lor\lnot R(x,x)$ is not a sentence of FOL ($x$ is a variable, not a name), so we cannot say it is true in an interpretation (p. 290).
- The same demand applies to contradiction, equivalence, unsatisfiability, argument validity and entailment (p. 291).
- Entailments such as $\forall x(H(x)\land J(x))\vDash\forall x\,H(x)$ are obvious, yet establishing them takes somewhat complicated reasoning about all interpretations (pp. 291–292).
- A table sums up when one interpretation suffices and when all are needed (p. 292).
- FOL differs from TFL because truth tables are finite and interpretations are infinitely many (p. 292).

## L3 — Walkthrough

### 34.1 Validities and contradictions
- One carefully specified interpretation that makes a sentence false shows it is not a validity (p. 289).
- Many true interpretations (ten, a hundred, a thousand) do not show validity. A validity is true in every interpretation, there are infinitely many, and we cannot deal with them one by one (p. 289).

**Example 1, no quantifiers:** $R(a,a)\lor\lnot R(a,a)$. The argument (p. 289–290):
1. Any relevant interpretation gives $R(a,a)$ a truth value.
2. If $R(a,a)$ is true, the disjunction is true.
3. If $R(a,a)$ is false, $\lnot R(a,a)$ is true, so the disjunction is true.
4. These are the only alternatives, so the sentence is true in every interpretation, hence a validity.

- This argument is not in FOL. It is in English about FOL, i.e. in the **metalanguage** (the language used to talk about FOL) (p. 290).
- Because there are no quantifiers, we need not think about how $a$ and $R$ are interpreted. Whatever the interpretation, $R(a,a)$ has some truth value. The same argument would work for TFL sentences (p. 290).

**Example 2, with a quantifier:** $\forall x\,(R(x,x)\lor\lnot R(x,x))$.
- We cannot say that $R(x,x)\lor\lnot R(x,x)$ is true in every interpretation. It is not a sentence of FOL, since $x$ is a variable, not a name (p. 290).
- Instead (pp. 290–291):
  1. Take an arbitrary interpretation. The sentence is true in it iff $R(x,x)\lor\lnot R(x,x)$ is satisfied by every object of the domain.
  2. Take an arbitrary object, called Fred. Either Fred satisfies $R(x,x)$ or not.
  3. If it does, Fred satisfies the disjunction. If not, Fred satisfies $\lnot R(x,x)$, and so the disjunction.
  4. Nothing was special about Fred, so every object satisfies the disjunction.
  5. So the sentence is true in the arbitrary interpretation, hence in every interpretation: it is a validity.
- Footnote: this uses the fact that connective truth conditions also apply to satisfaction: $a$ satisfies $\mathcal A(x)\lor\mathcal B(x)$ iff $a$ satisfies $\mathcal A(x)$ or $\mathcal B(x)$ (p. 290).
- The author calls this long-winded, but says that as things stand there is no alternative (p. 291).

*Intuition note:* We cannot test every interpretation, so we take an arbitrary interpretation and an arbitrary object and show the result holds for it. Since nothing about them was special, it holds for all.

### 34.2 Other cases
We must reason about all interpretations to show (p. 291):
- a contradiction (false in every interpretation);
- logical equivalence (same truth value in every interpretation);
- joint unsatisfiability (no interpretation makes all the sentences true; in every interpretation at least one is false);
- a valid argument (conclusion true in every interpretation where the premises are true);
- that some sentences entail another.

With the tools so far this is "a serious challenge" (p. 291).

**Example 3:** $\forall x(H(x)\land J(x))\vDash\forall x\,H(x)$. The reasoning (p. 292):
1. Take an arbitrary interpretation where the premise is true.
2. Then $H(x)\land J(x)$ is satisfied by every object.
3. So $H(x)$ is satisfied by every object (footnote: an object satisfying $\mathcal A(x)\land\mathcal B(x)$ must satisfy both).
4. So $\forall x\,H(x)$ is true in it.
5. We assumed nothing else about the interpretation, so any interpretation making the premise true makes the conclusion true.

Even this simple entailment needs somewhat complicated reasoning. For harder ones it can be "extremely torturous" (p. 292).

**Summary table** (p. 292):

| Question | Yes | No |
|---|---|---|
| validity? | all interpretations | one counter-interpretation |
| contradiction? | all interpretations | one counter-interpretation |
| equivalent? | all interpretations | one counter-interpretation |
| satisfiable? | one interpretation | all interpretations |
| valid? | all interpretations | one counter-interpretation |
| entailment? | all interpretations | one counter-interpretation |

**Comparison with TFL** (compare the table at the end of chapter 15): a truth table has finitely many lines, so a complete one is a "relatively tractable object". There are infinitely many interpretations for any given sentence(s), so reasoning about all of them can be "deeply tricky" (p. 292).

*Intuition note:* A truth table can be finished; the set of interpretations cannot be listed. So FOL needs general arguments, not a finite check.

## Toy example (ours)
Claim: $\forall x\,(P(x)\lor\lnot P(x))$ is a validity.
- Take any interpretation, with domain, say, $\{1,2\}$. The extension of $P$ may be $\{1\}$.
- Object 1 satisfies $P(x)$, so it satisfies the disjunction. Object 2 does not satisfy $P(x)$, so it satisfies $\lnot P(x)$, hence the disjunction.
- This used a particular domain. The general argument takes an arbitrary object $o$: it satisfies $P(x)$ or not, and either way satisfies the disjunction. So the sentence is true in every interpretation.
- Counter-case: $\forall x\,P(x)$ is not a validity. One interpretation with domain $\{1,2\}$ and $P$ true only of 1 makes it false, since 2 fails.

## Concepts
- [[validity / soundness]] — here: a sentence true in every interpretation (validity); an argument is valid if the conclusion is true wherever the premises are (pp. 289, 291)
- [[metalanguage]] (new) — English used to reason about FOL, rather than FOL itself (p. 290)
- [[interpretation]] (new) — a way of interpreting the names and predicates over a domain of objects; the text says there are infinitely many (pp. 289–290)
- [[satisfaction]] (new) — an object satisfies an open formula; connective rules apply to satisfaction (p. 290)
- [[counter-interpretation]] (new) — one interpretation that refutes a claim of validity, entailment, etc. (p. 292)
- [[arbitrary-instance reasoning]] (new) — reasoning about an arbitrary interpretation or object ("Fred") to cover all (pp. 290–291)

## Canonical instances
- [[excluded-middle-instance]] — $R(a,a)\lor\lnot R(a,a)$ is a validity (p. 289)
- [[universal-validity-instance]] — $\forall x(R(x,x)\lor\lnot R(x,x))$ is a validity (p. 290)
- [[conjunction-elimination-entailment]] — $\forall x(H(x)\land J(x))\vDash\forall x\,H(x)$ (p. 291)

## Bridges (candidates)
- [structural-analogy] arbitrary interpretation / arbitrary Fred ↔ mathematics: proving "for all" by treating an arbitrary element — the same proof pattern.
- [structural-analogy] finite truth tables vs. infinitely many interpretations ↔ computation: a finite check (decidable) against an unbounded search.

## Questions this raises
- What proof system would let us avoid reasoning about all interpretations directly?
- Is there any mechanical method to decide validity in FOL, as truth tables do in TFL?
- Why does satisfiability need only one interpretation, while its negation needs all?

## Reading notes
- Printed = pdf − 10. Text layer was readable; checked against the images for pdf 300–302.
- No misprints found. The table is as printed (its first column has no header in the source; "Question" is added here). The row label "valid?" appears as printed; presumably it refers to arguments, but the page does not say so.
