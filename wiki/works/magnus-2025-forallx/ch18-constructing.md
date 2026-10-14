---
id: magnus-2025-forallx/ch18-constructing
work: magnus-2025-forallx
unit: "18 Constructing proofs"
pages: 142-161
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Constructing proofs

## L0 — One line
Proofs can be found with rules of thumb: work backward from the goal's main operator, work forward from premises and assumptions, and use indirect proof (IP) as a last resort.

## L1 — The gist (≤ 120 words)
The chapter asks how to find a proof when no simple recipe exists. Its answer is a set of rules of thumb. Work backward: look at the introduction rule for the goal's main operator and set up the sentences or subproofs it needs. Work forward: apply elimination rules to premises and assumptions. Treat ⊥ as a wildcard, since explosion gives anything from it. If these fail, assume the negation of the goal and aim for ⊥ (IP). Worked examples show each strategy, including a proof of excluded middle. The authors say that practice remains essential.

**Prerequisites:** the natural-deduction rules ∧I/E, ∨I/E, →I/E, ¬I/E, IP, explosion (X) and reiteration (R); the idea of a subproof.

## L2 — Key ideas (5–10 bullets)
- No simple recipe exists for finding proofs, but rules of thumb help (p. 142).
- Working backward: for a goal with main operator ∧, →, or ¬, set up what its introduction rule needs, and repeat on the new goals (pp. 142–144).
- A disjunction goal: ∨I needs one disjunct, and a wrong pick means backtracking, so work forward first and use the ∨I strategy only when other work no longer helps (p. 145).
- Working forward: use the elimination rule of the main operator of a premise or assumption. ∨E needs two subproofs ending in the goal; →E needs the antecedent as a subgoal; ¬E gives ⊥ (pp. 145–148).
- Once ⊥ is derivable, the explosion rule gives any goal (p. 155).
- If direct strategies fail, use IP: assume ¬A, aim for ⊥. Inside the subproof the goal looks the same, but the extra assumption ¬A is available (pp. 157–158).
- For excluded middle A ∨ ¬A, the authors say that backward and forward work fail, so the only option is indirect proof (p. 158); the proof is on pp. 158–160.

## L3 — Walkthrough

**Opening (p. 142).** There is no simple recipe and no substitute for practice. The authors offer rules of thumb and strategies.

**18.1 Working backward from what we want (pp. 142–145).**
- Look at the goal C, the last line. Find the introduction rule for its main operator. Write down the sentences or subproofs that rule needs, and treat them as new goals (p. 142).
- *Conjunction.* To prove $A\land B$, prove $A$ (line $n$), then $B$ (line $m$), then infer $A\land B$ by ∧I, $n, m$. The line numbers are placeholders until the proof is complete (p. 143).
- *Conditional.* To prove $A\to B$, open a subproof assuming $A$ and ending in $B$. Cite it with →I, $n$–$m$ (p. 144).
- *Negation.* To prove $\neg A$, open a subproof assuming $A$ and ending in $\bot$. Cite it with ¬I, $n$–$m$ (p. 144).
- Keep working backward as long as you can, e.g. if the subproof's goal $B$ is a conjunction (p. 144).
- *Disjunction.* To prove $A\lor B$ by ∨I, pick one disjunct and try to prove it. If you cannot, backtrack: delete everything and try the other disjunct (p. 145). Since backtracking is frustrating, do not start by working backward from a disjunction. Work forward first. Use the ∨I strategy only when forward work and backward work using ∧I, →I and ¬I no longer work (p. 145).

*Intuition note:* The introduction rule of the goal's main operator gives you an idea of what must happen before the last line. It names the sentences or subproofs needed, and these become smaller goals. For a disjunction goal this is less helpful, because you must guess a disjunct (p. 145).

**18.2 Working forward from what we have (pp. 145–148).** Premises and subproof assumptions are things to work forward from, using the elimination rule for their main operator (pp. 145–146).
- *Conjunction.* From $A\land B$, ∧E gives $A$ and/or $B$. Writing both does no harm (p. 146).
- *Disjunction.* To use $A\lor B$ you must keep the goal $C$ in mind. Set up two subproofs, one assuming $A$ and one assuming $B$, each ending in $C$. Then infer $C$ by ∨E, citing the disjunction and both subproofs (pp. 146–147).
- *Conditional.* To use $A\to B$, derive $B$ by →E. This sets $A$ as a new subgoal (p. 147).
- *Negation.* To use $\neg A$, apply ¬E, which needs $A$ as well. The result is always $\bot$. So set $A$ as a new subgoal. This works especially well inside subproofs used for ¬I or IP, where $\bot$ is the goal (p. 148).

*Intuition note:* Elimination rules say what a sentence lets you conclude. A disjunction and a conditional each need something extra: a goal to reach from both cases, or the antecedent. A negation needs the unnegated sentence.

**18.3 Strategies at work (pp. 148–155).**

*Example 1: $(A\land B)\lor(A\land C)\ \therefore\ A\land(B\lor C)$.* There are two options, working backward from the conclusion or forward from the premise. The authors choose forward (p. 148).
1. Use the disjunction on line 1. Set up two ∨E subproofs, assuming $A\land B$ and $A\land C$, each ending in $A\land(B\lor C)$ (pp. 148–149).
2. In the first subproof, work backward from the conjunction. The subgoals are $A$ and $B\lor C$, joined by ∧I (p. 149).
3. $A$ comes from line 2 by ∧E (line 3). For $B\lor C$, either disjunct could be chosen. Picking $C$ would not work and would force backtracking. Picking $B$ works, because $B$ comes from line 2 by ∧E (p. 150).
4. The first subproof is complete (p. 151):

| line | sentence | justification |
|---|---|---|
| 1 | $(A\land B)\lor(A\land C)$ | PR |
| 2 | $A\land B$ | AS |
| 3 | $A$ | ∧E, 2 |
| 4 | $B$ | ∧E, 2 |
| 5 | $B\lor C$ | ∨I, 4 |
| 6 | $A\land(B\lor C)$ | ∧I, 3, 5 |
| 7 | $A\land C$ | AS |
| … | … | … |
| $m$ | $A\land(B\lor C)$ | |
| $m+1$ | $A\land(B\lor C)$ | ∨E, 1, 2–6, 7–$m$ |

5. The second subproof is "almost exactly the same" and is left as an exercise (p. 151).
6. Starting backward from the conclusion also leads to a proof, but it looks different. Set up subgoals $A$ and $B\lor C$, then work forward from the premise to prove them; the example layout proves each by ∨E from line 1. The pieces are left to the reader (pp. 151–152).

*Example 2: $(A\to B)\to(\neg B\to\neg A)$, a tautology, from no premises.* Nothing exists to work forward from, so work backward (p. 152).
1. →I: assume $A\to B$, aim for $\neg B\to\neg A$ (p. 153).
2. →I again: assume $\neg B$, aim for $\neg A$ (p. 153).
3. ¬I: assume $A$, aim for $\bot$ (p. 153).
4. For $\bot$, work forward from the negated sentence $\neg B$ (line 2). ¬E needs $B$. $B$ comes from $A\to B$ by →E, since the antecedent $A$ is available (line 3) (p. 154).
5. The finished proof (p. 155):

| line | sentence | justification |
|---|---|---|
| 1 | $A\to B$ | AS |
| 2 | $\neg B$ | AS |
| 3 | $A$ | (no label printed; it opens the innermost subproof) |
| 4 | $B$ | →E, 1, 3 |
| 5 | $\bot$ | ¬E, 2, 4 |
| 6 | $\neg A$ | ¬I, 3–5 |
| 7 | $\neg B\to\neg A$ | →I, 2–6 |
| 8 | $(A\to B)\to(\neg B\to\neg A)$ | →I, 1–7 |

*Intuition note:* Each conditional or negation goal is peeled off by an assumption. Then the assumptions already made are used to reach ⊥.

**18.4 Working forward from ⊥ (pp. 155–156).** If you can justify ⊥, explosion lets you justify anything, so ⊥ works like a wildcard (p. 155).

*Example: $A\lor B,\ \neg A\ \therefore\ B$.* $B$ has no main connective, so you cannot work backward from it; work forward from $A\lor B$ with two subproofs (p. 155). In the first subproof, $A$ and $\neg A$ (line 2) give $\bot$ by ¬E, then $B$ by X. In the second, $B$ is assumed and repeated by R (p. 156):

| line | sentence | justification |
|---|---|---|
| 1 | $A\lor B$ | PR |
| 2 | $\neg A$ | PR |
| 3 | $A$ | AS |
| 4 | $\bot$ | ¬E, 2, 3 |
| 5 | $B$ | X, 4 |
| 6 | $B$ | AS |
| 7 | $B$ | R, 6 |
| 8 | $B$ | ∨E, 1, 3–5, 6–7 |

**18.5 Proceed indirectly (pp. 157–158).** The forward and backward strategies often succeed, but not always. If you cannot find a way to show $A$ directly using those strategies, use IP: assume $\neg A$ and look for $\bot$ inside that subproof, then infer $A$ by IP, $n$–$m$ (p. 157). A good candidate for getting $\bot$ is a negated sentence, since ¬E always yields $\bot$. Here that is the assumption $\neg A$, which means setting $A$ as a goal inside the subproof (p. 157). This looks circular, since we again seek $A$ after using IP as a last resort. But now we are inside a subproof with the extra assumption $\neg A$ that we did not have before (p. 158).

**18.6 Indirect proof of excluded middle (pp. 158–160).** $A\lor\neg A$ is a tautology, the law of excluded middle (LEM). The idea is that $A$ may be true or $\neg A$ may be true, with no middle way where neither is true (p. 158). Footnote: "tertium non datur" ("no third way") names the same principle, and logicians with qualms about indirect proof also have qualms about LEM (p. 158).
1. Backward by ∨I fails at the start. We would need to prove $A$ or $\neg A$ from no premises, and neither is a tautology. Forward work is impossible, as there is nothing to work from. So the only option is indirect proof (p. 158).
2. Assume $\neg(A\lor\neg A)$ (line 1) and aim for $\bot$ by ¬E, which needs $A\lor\neg A$ inside the subproof (pp. 158–159).
3. Go back to the basic strategies for this new goal. Pick the disjunct $\neg A$ and use ∨I. To prove $\neg A$, use ¬I: assume $A$ and aim for $\bot$ (p. 159).
4. For that $\bot$, work forward from $\neg(A\lor\neg A)$ on line 1, the only negated sentence available. Its unnegated partner $A\lor\neg A$ follows from $A$ (line 2) by ∨I (pp. 159–160).
5. Complete proof (p. 160):

| line | sentence | justification |
|---|---|---|
| 1 | $\neg(A\lor\neg A)$ | AS |
| 2 | $A$ | AS |
| 3 | $A\lor\neg A$ | ∨I, 2 |
| 4 | $\bot$ | ¬E, 1, 3 |
| 5 | $\neg A$ | ¬I, 2–4 |
| 6 | $A\lor\neg A$ | ∨I, 5 |
| 7 | $\bot$ | ¬E, 1, 6 |
| 8 | $A\lor\neg A$ | IP, 1–7 |

*Intuition note:* Assume the excluded-middle sentence is false (line 1). Then assume the first disjunct, $A$: that would make the whole disjunction true by ∨I, which clashes with line 1, so $\neg A$ follows. But $\neg A$ again gives the disjunction by ∨I, which clashes with line 1 once more. So the assumption fails.

## Toy example (ours)
Prove $P\land Q\ \therefore\ Q\land P$ with the strategies.
1. Goal $Q\land P$ is a conjunction, so work backward. Subgoals are $Q$ and $P$, joined by ∧I.
2. Work forward from line 1 by ∧E:

| line | sentence | justification |
|---|---|---|
| 1 | $P\land Q$ | PR |
| 2 | $P$ | ∧E, 1 |
| 3 | $Q$ | ∧E, 1 |
| 4 | $Q\land P$ | ∧I, 3, 2 |

Backward work fixed the last line and the subgoals. Forward work supplied them.

## Concepts
- [[working-backward]] (new) — start from the goal's main operator and plan what its introduction rule needs (p. 142)
- [[working-forward]] (new) — apply elimination rules to premises and assumptions to fill gaps (p. 145)
- [[subproof-goal]] (new) — a sentence you plan to prove, such as an end line of a subproof (p. 142)
- [[backtracking]] (new) — deleting a failed attempt (e.g. a wrong disjunct) and trying again (p. 145)
- [[explosion-wildcard]] (new) — once ⊥ is justified, X gives any sentence (p. 155)
- [[indirect-proof]] (new) — assume ¬A, derive ⊥, conclude A by IP (p. 157)
- [[law-of-excluded-middle]] (new) — $A\lor\neg A$, a tautology; here proved indirectly (p. 158)
- [[validity]] — the chapter treats finding a proof as the way to show that an argument is valid (p. 148)

## Canonical instances
- [[proof-distribution-and-or]] (new) — $(A\land B)\lor(A\land C)\ \therefore\ A\land(B\lor C)$ (p. 148)
- [[proof-contraposition-tautology]] (new) — $(A\to B)\to(\neg B\to\neg A)$ (p. 152)
- [[proof-disjunctive-syllogism]] (new) — $A\lor B,\neg A\ \therefore\ B$ (p. 155)
- [[proof-excluded-middle]] (new) — $A\lor\neg A$ via IP (p. 158)

## Bridges (candidates)
- [structural-analogy] working backward from a goal ↔ problem solving: breaking a goal into subgoals — each rule says what must hold just before
- [metaphor] ⊥ as a wildcard ↔ philosophy of logic: contradiction makes everything derivable — explosion lets ⊥ justify any sentence

## Questions this raises
- Why do some logicians doubt indirect proof and LEM (p. 158)?
- Is there a mechanical procedure that always finds a proof when one exists, or is practice always needed?
- What strategies suit $A\leftrightarrow B$ (Exercise B, p. 160)?

## Exercises worth doing
- Ex. A.1–8 (p. 160) — drill the basic strategies on arguments — medium
- Ex. A.5 (p. 160) — the same argument as Example 1; compare your proof with the text's (p. 151) — easy
- Ex. B (p. 160) — invent strategies for ↔ — medium
- Ex. C.1–5 (pp. 160–161) — prove sentences from no premises — medium
- Ex. D.1–7 (p. 161) — all need IP; the last three are called quite hard — hard

## Reading notes
- printed = pdf − 10.
- Formulas were checked against the page images.
- Proof diagrams use vertical lines for subproofs; the tables above transcribe them without the lines.
- On p. 146 the prose "Suppose we want to prove C, and we have A ∨ B to work with" prints the B of A ∨ B in a different (italic) font from the script letters used elsewhere; I read it as the same sentence as the one in the diagram on p. 147.
- The line "A" in the innermost subproof (p. 155, line 3) has no justification printed; it opens the subproof cited as 3–5.
- Small typo in the source: "from a disjunctions" (p. 150).
