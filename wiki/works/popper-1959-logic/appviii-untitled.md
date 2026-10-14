---
id: popper-1959-logic/appviii-untitled
work: popper-1959-logic
unit: "Appendix *viii — Content, Simplicity, and Dimension"
pages: 392-401
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Content, Simplicity, and Dimension

## L0 — One line
Popper argues that a theory with fewer parameters (a simpler one) is never more probable than one with more, so a "simplicity postulate" that links simplicity to high probability contradicts the probability calculus.

## L1 — The gist (≤ 120 words)
Popper asks how to measure the content and simplicity of theories without artificial languages or "atomic" statements. He uses statements that are atomic only relative to a field of application, and he measures formal simplicity by paucity of parameters (not counting merely formal reductions). In a large finite universe, fewer parameters means fewer favourable possibilities, so lower or equal probability. Wrinch and Jeffreys' "simplicity postulate" gives simpler theories higher probability, so it must contradict the probability calculus. Popper suggests they may have confused probability with corroboration; for him simple theories are improbable yet highly testable and corroborable. A 1967 addendum gives a measure of content.

**Prerequisites:** classical probability as favourable/possible cases; negation rule $p(\bar a)=1-p(a)$; convergent series; curves with parameters (e.g. $y=ax$); the idea of a falsifier.

## L2 — Key ideas (5–10 bullets)
- Popper rejects artificial "language systems" and absolutely atomic predicates; scientists treat even "blue" or "warm" as complex when a problem needs it (pp. 392–393).
- He uses statements that are atomic only relative to a field of application $F$; the fewer such statements are needed to refute a theory, the greater its content (pp. 393–394).
- Formal simplicity can be measured by paucity of parameters (not merely formal reductions), and the number of parameters equals the dimension of the theory's favourable possibilities (p. 394).
- Theorem (1): if $d(a_1)<d(a_2)$, then $p(a_1)>p(a_2)$ is impossible. This is shown first in finite universes, then in the limit (pp. 394–396).
- A second route to the same theorem runs through the minimum of $d(a)+1$ relative-atomic statements needed to refute $a$ (p. 396).
- Using Wrinch and Jeffreys' own idea, the theorem entails zero probability for all theories (pp. 397–398).
- Wrinch and Jeffreys' simplicity postulate cannot be made consistent with any adequate probability axiom system, because it violates (1) (p. 399).
- They may have confused probability with corroboration; simplicity goes with improbability and with high corroborability (pp. 400–401).
- Addendum 1967: $Ct_F(a)=1/(d_F(a)+1)$ measures fine structure of content. Simplicity should always be regarded as relative to a given problem and, as Popper added in 1972, to some degree also to the historical problem-situation (p. 401).

## L3 — Walkthrough

**Opening: against artificial languages (p. 392).** Popper does not want to stop scientists from freely using new ideas, predicates or "occult" concepts. He therefore rejects attempts to model the "language of science" by artificial calculi. He thinks they have contributed to obscurity and confusion (p. 392).

**Content and atomic statements (pp. 392–393).** (Our gloss, not in the text: atomic = not analysable into simpler statements.) If absolutely atomic statements existed, the content of a theory could be measured by the reciprocal of the minimum number of atomic statements needed to refute it. Content equals testability, so the more easily refuted theory has more content (pp. 392–393). But Popper holds that there are no "natural" atomic predicates in science. Carnap's examples "blue" and "warm" may be treated as complex: blue as the sky's colour explained by atomic theory, or as a character of visual images correlated with physiological stimuli (p. 393). Tying science to a fixed language "would, if successful, be the end of science" (p. 393).

*Intuition note.* Content can be measured by how few atomic statements are needed to refute a theory. What counts as atomic depends on the problem under consideration, so the measure is made relative to a field of application.

**Relative-atomic statements (pp. 393–394).** Instead Popper uses statements that are atomic relative to a field $F$ of application. Example: $a_1$ = "All planets move in circles", $a_2$ = "All planets move in ellipses". The field consists of statements "At the time $x$ the planet $y$ was in the position $z$". If the track is a plane curve, each statement is an entry on graph paper, or a pin in 3-D whose length is the time and whose colour is the planet (pp. 393–394). From sections 40–46 and appendix i: the minimum number of relative-atomic statements needed for refutation measures complexity. Formal simplicity might be measured by the paucity of parameters, in so far as the paucity is not the result of a "formal" rather than a "material" reduction (p. 394). All such comparisons concern the fine-structure of content, because absolute probabilities are all equal, namely zero (p. 394).

**The aim: parameters measure fine-structure (p. 394).** Popper wants to show: for a sufficiently large finite universe, the theory with more parameters will always be more probable (classical sense) than the one with fewer (p. 394).

**Derivation (pp. 394–396).**
- In a continuous field the universe of events is infinite. Theories are compared by the dimension of their favourable possibilities, which equals the number of parameters (p. 394).
- Make the universe finite. Each relative-atomic statement refers to a small non-overlapping square of side $\varepsilon$. Curves become "quasi curves", chains of squares of width about $\varepsilon$, so the number of possible theories is finite (pp. 394–395). Footnote 3 says partly overlapping squares, or overlapping circles, could be used instead; circles would be a little closer to reading positions as never absolutely sharp measurement results (p. 395).
- A theory with $d$ parameters is represented by a $d$-dimensional arrangement of $d$-dimensional "cubes" of side $\varepsilon$. Each chain of cubes is one quasi curve, one favourable possibility (p. 395).
- A theory with fewer parameters has fewer dimensions and also fewer cubes, i.e. fewer favourable possibilities. So if $a_1$ has fewer parameters than $a_2$, in a large enough finite universe $p(a_1)<p(a_2)$, and hence
$$p(a_1)\preceq p(a_2)\tag{*}$$
(sign read from the image; see Reading notes) (p. 395).
- (\*) stays valid as $\varepsilon\to0$, which replaces the finite universe by an infinite one (p. 396).

**Theorem (1) (p. 396).** If the number of parameters of $a_1$ is smaller than that of $a_2$, then $p(a_1)>p(a_2)$ contradicts the laws of the probability calculus. With $d(a)=d_F(a)$ the dimension relative to $F$:
$$\text{If } d(a_1)<d(a_2) \text{ then } p(a_1)\preceq p(a_2);\tag{1}$$
so $p(a_1)>p(a_2)$ is incompatible with $d(a_1)<d(a_2)$.

**Second argument (p. 396).** A theory $a$ needs at least $d(a)+1$ relative-atomic statements for refutation. Its "weakest falsifiers" are conjunctions of $d(a)+1$ such statements. If $n\le d(a)$, no conjunction of $n$ of them is strong enough to derive $\bar a$, the negation of $a$. So the content of $\bar a$ is measured by $d(a)+1$. Since $p(\bar a)=1-p(a)$, a theory's probability falls as its negation's probability rises, and the same holds for contents. Hence $d(a_1)<d(a_2)$ means $a_1$ has greater content, so $p(a_1)\preceq p(a_2)$. This is theorem (1) again (p. 396).

*Intuition note.* A theory with few free parameters leaves fewer possibilities open (fewer favourable possibilities), so its probability is lower than or equal to that of a theory with more. In Popper's words, simplicity is linked with improbability rather than probability, and with high testability.

**Link to $p(a)=p(a,e)=0$ (p. 397).** The theorem was derived by considering finite universes and is quite independent of the transition to infinite universes. It is therefore independent of formulae (1) and (2) of the preceding appendix, which says that in an infinite universe, for any universal law $a$ and finite evidence $e$,
$$p(a)=p(a,e)=0.\tag{2}$$
Theorem (1) can then be used to derive (2) again, with an idea from Wrinch and Jeffreys (p. 397).

**Derivation of (2) from (1) (pp. 397–398).**
- Wrinch and Jeffreys observed that infinitely many mutually exclusive theories have probabilities summing to at most 1. So almost all are zero, unless the theories are ordered in a sequence with probabilities from a convergent series with sum at most 1. Examples: $1/2^n$ for the $n$th theory; or $1/50=1/(2\cdot25)$ for each of the first 25 and $1/400=1/(2^2\cdot100)$ for each of the next 100 (p. 397).
- Any such assignment has a greatest value $P$, given to at most $n$ theories with $nP<1$. Let $D$ be the largest dimension among these $n$ theories and $a_1$ one with $d(a_1)=D$. Take $a_2$ with $d(a_2)>D$ (p. 397). Then
$$d(a_1)<d(a_2)\ \text{ and }\ p(a_1)>p(a_2),\tag{$-$}$$
which violates (1) (p. 398).
- Such an assignment is unavoidable unless all theories get probability zero. So (1) entails that all theories get zero probability (p. 398).

**Wrinch and Jeffreys' view (pp. 398–399).**
- **Their view (Popper's report):** empirical knowledge requires that evidence can raise a law's probability. So (2) must be false, and a method must exist for giving non-zero probabilities to an infinite sequence of theories. This is the "transcendental" argument (p. 398).
- **Popper's reply:** they overlooked that we may learn more and more about laws, corroborating them better, without raising their probability, which stays zero (p. 398).
- Popper says Jeffreys and Wrinch never described the sequence and the assignment of probabilities clearly enough. Their main idea, the "simplicity postulate", orders theories so that parameters increase while probabilities decrease. Any two theories of such a sequence would violate (1) (p. 398). Footnote 6: Jeffreys calls it an application of his rule 5, which Popper says contains only a very vague form of the transcendental principle, so his argument is unaffected (p. 398).
- Popper says the ordering cannot be carried through, as Jeffreys noticed: theories may share a parameter count. Jeffreys says same-count laws can have the same prior probability, e.g. $y=ax$ and $y=ax^2$. But there are infinitely many ($y=ax^n$, $n\to\infty$), so the problem recurs for each parameter count (pp. 398–399).
- Jeffreys also admits that if $a_1$ arises from $a_2$ by setting one extra parameter to zero, then $p(a_1)<p(a_2)$, since $a_1$ is a special case. This agrees with (1), but he does not comment on the possible contradiction with his postulate and gives no consistency proof (p. 399). Footnote 9: his remark about "half the prior probability" seems to mean $p(a_1)=p(a_2)/2$, which may lead to contradictions if $a_2$ has more than 2 parameters (p. 399).
- **Popper's conclusion:** no consistency proof can be given; the postulate must contradict every adequate axiom system for probability, because it violates (1) (p. 399).

**Why they thought it harmless (pp. 399–401).**
- Popper says they were first to identify simplicity with paucity of parameters and that his own theory agrees on this point, though he does not simply identify the two and distinguishes formal from material reduction, that scientists prefer simpler theories and try them first, and that simple theories are few and complex ones many (pp. 399–400).
- **Popper's conjecture:** they may have inferred that complex theories are less probable, because probability is "divided" among many. They also assumed high probability is a scientific aim. So they may have thought it intuitively evident that "simple" is to be identified with "probable"; the postulate then appeared necessary on intuitive grounds and therefore a fortiori consistent (p. 400).
- But the scientist does not and cannot aim at high probability. The opposite impression comes from mistaking probability for corroboration. So simplicity goes with improbability, and with high corroboration, since high testability equals high prior improbability or simplicity (pp. 400–401).
- Footnote 10: after $n$ severe tests of a statistical hypothesis "$p(a,b)=1$", corroboration is $n/(n+2)=1-2/(n+2)$. Laplace's rule of succession gives $(n+1)/(n+2)=1-1/(n+2)$. Popper thinks Laplace's assumptions do not apply to the cases he meant, though they apply to the probability of a report on a statistical sample. The numerical similarity may explain why Laplace's result felt right (p. 400).

**Addendum 1967 (p. 401).** With $d_F(a)$ the dimension of $a$ relative to $F$, a measure of simplicity or content is
$$Ct_F(a)=\frac{1}{d_F(a)+1}.$$
It measures the fine structure of content and may apply where probabilities are indistinguishable because $p(a)=0$. Simplicity is relative to a given problem of explanation (p. 401).

**Addendum 1972 (p. 401).** If the simplicity of a theory is relative to the problems it tries to solve, then it is, to some degree, also relative to the historical problem-situation. Content and simplicity may therefore change as a science develops (p. 401).

## Toy example (ours, not from the text)
Universe: times $x=1,2,3$; at each time a position $y\in\{0,1,2,3\}$. Possible histories: $4^3=64$ (equally likely, classical probability).
- $a_1$: "$y=c$", one parameter, integer $c$. Histories: 4 (constant 0, 1, 2 or 3). $p(a_1)=4/64=1/16$.
- $a_2$: "$y=c+kx$", two parameters, integers. $k=0$ gives the same 4 histories. $k=1$: $c=-1$ gives $(0,1,2)$, $c=0$ gives $(1,2,3)$. $k=-1$: $c=3$ gives $(2,1,0)$, $c=4$ gives $(3,2,1)$. $|k|\ge2$ would need a range of at least 4, which is impossible. Total $4+2+2=8$ histories. $p(a_2)=8/64=1/8$.

So $p(a_1)=1/16<1/8=p(a_2)$. The theory with fewer parameters allows fewer histories, so it is less probable. This is the special-case nesting Jeffreys admitted, and it shows the direction of theorem (1).

## Concepts
- [[falsifiability]] — content equals testability, measured by how few statements can refute a theory (p. 392)
- [[corroboration]] — record of severe tests; it can rise while probability stays zero; distinct from probability (p. 398)
- [[relative-atomic-statements]] (new) — statements atomic only relative to a theory's field of application $F$ (p. 393)
- [[dimension-of-a-theory]] (new) — $d_F(a)$, the number of parameters, equal to the dimension of the favourable possibilities (p. 394)
- [[weakest-falsifier]] (new) — a conjunction of $d(a)+1$ relative-atomic statements, the smallest refuting set (p. 396)
- [[simplicity-as-paucity-of-parameters]] (new) — formal simplicity can be measured by paucity of parameters, in so far as this is not the result of a merely formal reduction (p. 394)
- [[fine-structure-of-content]] (new) — differences in content when absolute probabilities are all zero (p. 394)
- [[simplicity-postulate]] (new) — Wrinch–Jeffreys' ordering of theories by increasing parameters and decreasing probability; Popper says it is inconsistent (p. 398)

## Canonical instances
- [[planets-circles-vs-ellipses]] — $a_1$ and $a_2$ with the field "at time $x$ planet $y$ was at $z$" (p. 393)
- [[quasi-curves-chessboard]] — finite universe of squares of side $\varepsilon$ and chains of cubes as theories (p. 395)
- [[jeffreys-powers-of-x]] — $y=ax^n$: infinitely many same-parameter laws (p. 399)
- [[laplace-rule-of-succession]] — $(n+1)/(n+2)$ compared with corroboration $n/(n+2)$ (p. 400)

## Bridges (candidates)
- [structural-analogy] Dimension $d$ of a theory = number of parameters ↔ statistics: model complexity and the number of free parameters (the text does not mention statistics) — both count a model's freedom.
- [structural-analogy] Probabilities of infinitely many exclusive theories must sum to ≤ 1 ↔ Bayesian confirmation: priors over a countable hypothesis space — same constraint on priors.
- [metaphor] Simple = bold, improbable, highly testable ↔ Popper's falsifiability: more content, less probability.

## Questions this raises
- Does the argument for zero probability need the "classical" counting of possibilities, or does it hold for any probability axioms?
- If simplicity goes with improbability, what exactly does corroboration add that probability cannot express?
- How is a "field of application" chosen, and can a different choice reverse a content comparison?
- Is the difference between "formal" and "material" reduction of parameters sharp enough to keep $d(a)$ well defined?

## Reading notes
- Printed page = pdf page − 29 (pdf 421 = p. 392). Labels give printed numbers.
- The text layer drops the inequality sign in (\*) and (1) on pp. 395–396. The image of p. 396 shows a ≺-like sign with a tail. I transcribe it as $\preceq$ ("less than or equal"), since the theorem rules out only $>$. The glyph looks different from the ≤ printed in "n ≤ d(a)" on the same page, so the transcription is an inference from context, not a certain reading.
- Text-layer "1/(2.25)", "n.P" are $1/(2\cdot25)$, $n\cdot P$. The text layer shows the label "(−)" on p. 398 (that page image was not checked).
- Equation (2) and "(1) and (2) of the preceding appendix" refer to appendix *vii, not included here.
