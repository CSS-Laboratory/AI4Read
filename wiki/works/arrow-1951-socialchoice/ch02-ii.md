---
id: arrow-1951-socialchoice/ch02-ii
work: arrow-1951-socialchoice
unit: "Chapter II. The Nature of Preference and Choice"
pages: 9-21
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# The Nature of Preference and Choice

## L0 — One line
Arrow sets the formal basis of his book: each person has only an ordinal "preferred-or-indifferent" relation $R$ (connected and transitive) over social states, with no cardinal or interpersonal utility, and choices follow from it.

## L1 — The gist (≤ 120 words)
Arrow asks what formal picture of individual choice his social-choice problem should use. He rejects measurable or interpersonally comparable utility as meaningless for welfare comparisons. He assumes instead that each individual has only a weak ordering $R$ of social states (connected and transitive). From $R$ he defines preference, indifference and a choice function, and shows that choice from any set is fixed by choices from pairs. Individuals are assumed rational in this sense, and society's ordering is to be rational too. He ends by noting that the pairwise model of rationality does not seem to suit zero-sum game theory well, and that there seems to be no logical necessity for rationality-as-ordering.

**Prerequisites:** sets and binary relations; basic indifference-curve consumer theory; the idea of expected utility.

## L2 — Key ideas (5–10 bullets)
- Arrow holds that the only meaning utility can be said to have is as an indicator of behavior, so any strictly increasing transform of a utility function explains behavior equally well. Interpersonal comparison therefore has no meaning (p. 9).
- The von Neumann–Morgenstern scale is, in Arrow's view, a convenient tool for describing behavior under risk, with no special ethical significance for social choice, as far as he can see (p. 10).
- Even if individual utility were measurable, aggregating would need extra value judgments. The book therefore assumes preference scales with no cardinal significance, individual or interpersonal (p. 11).
- Preference is formalised by one relation $R$ obeying Axiom I (connectedness) and Axiom II (transitivity). Strict preference $P$ and indifference $I$ are defined from $R$ (pp. 13–14).
- The choice function $C(S)$ is defined from $R$. Rational choice in any environment is determined by choices in two-element environments (pp. 15–16).
- Social states are complete descriptions that include collective activities. Individual orderings may rest on whatever standards the person deems relevant; Arrow contrasts orderings by tastes with orderings by values. Which preferences count is itself a value judgment (pp. 17–18).
- Rationality is assumed for individuals and wanted for society (p. 19).
- Pairwise rationality seems not to suit zero-sum game theory well, and there seems to be no logical necessity for ordering in economic theory (pp. 20–21).

## L3 — Walkthrough

### 1. Measurability and interpersonal comparability of utility (pp. 9–11)
**Author's position.** Interpersonal comparison of utilities has no meaning, and there is no meaning relevant to welfare comparisons in the measurability of individual utility (p. 9).
- Arrow says the proponents of measurable utility have produced no proposition of economic behavior that their hypothesis explains and the indifference-curve theorists' hypothesis does not (p. 9).
- The only meaning the concepts of utility can be said to have is as an indication of actual behavior. Behavior explained by one utility function is equally well explained by any strictly increasing function of it (p. 9).
- Hence, if utility is not measurable in this sense, it cannot be interpersonally comparable "a fortiori" (p. 9).

**Von Neumann–Morgenstern (vNM).** They consider preferences among probability distributions over alternatives. Under plausible assumptions there is a utility indicator, unique up to a linear transformation, whose value for any probability distribution is the mathematical expectation of the utility. Behavior is then described as maximising expected utility (pp. 9–10).
- Arrow says that, as far as he can see, the theorem gives no special ethical significance to that scale. Squaring the scale gives behavior described as maximising the expected square root of utility (p. 10).
- He does not deny its usefulness for descriptive theory under random events. But, he says, it has nothing to do with welfare considerations, especially for a social choice among policies with no random elements. Otherwise the distribution of social income would be governed by tastes for gambling (p. 10).

**Temperature analogy.** Temperature is operationally the volume of a unit mass of a perfect gas. The volume scale is chosen only because the gas equation is then simple, and there is no deeper significance. Arrow asks whether it makes any sense to say a rise from 0° to 1° is as intense as one from 100° to 101°; no more, he says, is there any meaning in comparing marginal utilities at different levels of well-being (p. 10).

**Aggregation.** Even if individual utility were measurable, one must still pick one indicator from an infinite family for each person, and the aggregate (say a sum) depends on that choice. In general, there seems to be no method intrinsic to utility measurement that makes the choices compatible. He adds that it seems to make no sense to add one person's utility, a psychic magnitude in his mind, to another's. Doing so takes a value judgment, and aggregating by a formula takes another (pp. 10–11).
- Footnote 3: if it is assumed to begin with that all individuals have the same preference scales (the same tastes), one could choose the same utility function for all. But if interpersonal comparison is taken seriously, of two people with the same indifference map, one might be twice as sensitive as the other (p. 11).
- Footnote 4 quotes Bentham's doubts about adding one man's happiness to another's (p. 11).

**Decision:** the book assumes individual choice is describable by a preference scale without cardinal significance, individual or interpersonal (p. 11).

*Intuition note.* If only the order of preferences is observable, any order-preserving relabelling of numbers fits the data equally well. Adding or comparing such numbers across people then has no meaning on this view.

### 2. A notation for preferences and choice (pp. 11–17)
**Set-up.** Alternatives are mutually exclusive and are written $x, y, z, \dots$ (p. 12).
- In consumer theory an alternative is a commodity bundle; in the theory of the firm, a complete decision on inputs and outputs; in welfare economics, a distribution of commodities and labor requirements. In general it is a vector. In elections it is a candidate (pp. 11–12).
- On a given occasion the chooser has a subset $S$ of all alternatives (the opportunity set, a generalisation of the opportunity curve; in consumer theory under perfect competition it is the budget plane) and must choose from it (p. 12).

**The choice process.** Before knowing $S$, the chooser considers every pair $x, y$ and makes one and only one of three decisions: $x$ preferred, indifferent, or $y$ preferred. Decisions on different pairs are assumed consistent (if $xPy$ and $yPz$ then $xPz$; if $xIy$ and $yIz$ then $xIz$). Then, for a given $S$ (p. 12):
- If one alternative is preferred to all others, it is chosen.
- If a subset is each preferred to everything outside it and indifferent within, the choice is the whole subset.
- Since the types of sets allowed are not restricted, there may be no alternative preferred or indifferent to all others, i.e. every alternative has a better one. Arrow says there cannot really be said to be any rational choice in that case. Examples: integral dollars when more is preferred to less; the sequence $\tfrac12, \tfrac23, \tfrac34, \dots, 1-\tfrac1n, \dots$ dollars. Arrow says this point plays no part in the work (p. 12).

**Single relation.** The one relation "preferred or indifferent" is written $xRy$. Since any two alternatives are assumed comparable (footnote 5 calls this the heart of the integrability controversy), Arrow states:

> **Axiom I:** For all $x$ and $y$, either $xRy$ or $yRx$.

$R$ is then *connected*. This covers $x=y$, so $xRx$. The "or" does not exclude both holding (p. 13). Footnote 6: strictly, "connected" applies to $x\neq y$ and "reflexive" to $xRx$. The text uses "connected" for both.

> **Axiom II:** For all $x, y, z$: $xRy$ and $yRz$ imply $xRz$.

$R$ is then *transitive*. A relation with both axioms is a **weak ordering** (or "ordering"). "Weak" means ties are allowed. A *strong ordering* allows no ties. Weak ordering generalises "$\ge$" on the reals, strong ordering generalises "$>$" (pp. 13–14). Here "ordering" without a modifier means weak ordering (footnote 8).

**Definitions (p. 14).**
- Definition 1: $xPy$ means not $yRx$ ("$x$ is preferred to $y$").
- Definition 2: $xIy$ means $xRy$ and $yRx$ ("indifferent").

**Lemma 1** (pp. 14–15). (a) $xRx$. (b) $xPy \Rightarrow xRy$. (c) $xPy$ and $yPz \Rightarrow xPz$. (d) $xIy$ and $yIz \Rightarrow xIz$. (e) For all $x,y$: $xRy$ or $yPx$. (f) $xPy$ and $yRz \Rightarrow xPz$.

Proof sketches (Arrow's):
- (a) Put $y=x$ in Axiom I.
- (b) From Definition 1 and Axiom I.
- (c) By (b), $xRy$. Suppose $zRx$. Then $zRx$ and $xRy$ give $zRy$ (Axiom II). But $yPz$ gives not $zRy$ (Def. 1). Contradiction, so not $zRx$, i.e. $xPz$.
- (d) From Def. 2, $xRy$, $yRz$, so $xRz$ (Axiom II). Also $zRy$ and $yRx$, so $zRx$. Hence $xIz$.
- (e) Directly from Def. 1.
- (f) Suppose $zRx$. With $yRz$, Axiom II gives $yRx$. But $xPy$ means not $yRx$. Contradiction, so not $zRx$, i.e. $xPz$.

Terminology: $R$ is called the "ordering relation". "Preference relation" is reserved for $P$ (p. 15).

*Intuition note.* Two plain axioms (everything comparable, and consistency across pairs, i.e. transitivity) already give all the properties we expect from strict preference and indifference. Strict preference and indifference are both transitive, and $P$ followed by $R$ gives $P$.

**Choice function.** The set of available alternatives $S$ is called the *environment* (Marschak's term, footnote 10). $C(S)$ is the set of alternatives chosen from $S$ (p. 15).

> **Definition 3:** $C(S)$ is the set of all $x$ in $S$ such that, for every $y$ in $S$, $xRy$.

- $C(S)$ assigns a choice to each environment, so Arrow calls it the choice function. It generalises the demand function, with budget planes as the sets $S$ (p. 15).
- With $[x,y]$ the two-element set: if $xPy$, then $xRy$ (Lemma 1b) and $xRx$, so $x\in C([x,y])$. By Def. 1, not $yRx$, so $y\notin C([x,y])$. Conversely, if $C([x,y])=\{x\}$, then not $yRx$, hence $xPy$ (pp. 15–16).

> **Lemma 2:** A necessary and sufficient condition that $xPy$ is that $x$ be the sole element of $C([x,y])$ (p. 16).

- If neither $xPy$ nor $yPx$, then $xIy$, which is equivalent to $C([x,y])$ containing both. Knowing $C$ on all two-element sets defines $P$, $I$ and $R$. By Def. 3, $R$ determines $C(S)$ for all $S$ (p. 16).
- Consequence: under the assumptions of rational choice, choice in any environment is determined by choices in two-element environments (p. 16).
- Footnote 11 says one could instead impose axioms directly on the choice function. It is "not hard" to find plausible axioms from which a generating weak ordering follows, so the two approaches are logically equivalent (p. 16).

*Intuition note.* Under the assumptions of rational choice, once the chooser's pairwise verdicts are known, everything else about choice is fixed. Larger menus add no new information.

**Why ordering relations rather than indifference maps or utility functions** (pp. 16–17):
- Unlike indifference maps, ordering relations can handle alternatives that are vectors with more than two components. Indifference maps also rest largely on the assumption that more of each component is preferred to less, which suits a social state badly, since its components may be desirable in some circumstances and undesirable in others (p. 16).
- Indifference maps assume continuity, which is unnecessarily restrictive. Handling indivisibilities needs some discrete components (pp. 16–17).
- With insufficient continuity, there may be no real-number utility assignment. In any case one would only replace $xRy$ by $U(x)\ge U(y)$, leaving the proofs unchanged. $U$ would be superfluous, because only its ordinal properties matter (p. 17).

### 3. The ordering of social states (pp. 17–19)
- The objects of choice are social states: complete descriptions of the commodities held by each individual, labor supplied, productive resources used, and collective activities such as municipal services, diplomacy and statues (p. 17).
- Each individual is assumed to have a definite ordering of all conceivable social states by desirability to him. This ordering need not depend only on his own commodity bundle. He orders by whatever standards he deems relevant, for example relative income standing (a Veblen leisure-class member) or income equality (an egalitarian) (p. 17).
- Since collective activities are components, purely individualistic assumptions are useless for problems like dividing national income between public and private expenditure. The notation allows perfect generality, but at a price: more information would be available if the orderings were restricted by prior knowledge (pp. 17–18).

**Tastes and values.** The ordering by direct consumption reflects the individual's *tastes*. The ordering that adds his general standards of equity (or perhaps his standards of pecuniary emulation) reflects his *values* (p. 18).
- The line between them is not clear-cut. Psychologically, pleasure in a neighbor's well-tended lawn differs only slightly from pleasure in one's own (p. 18).
- Without challenging the intuition that not all possible preferences ought to count, Arrow stresses that which preferences are relevant is itself a value judgment and cannot be settled a priori. From a formal point of view one cannot distinguish dislike of factory smoke ruining one's grounds from distaste for heathenism in Central Africa (p. 18).
- The ordering by values includes all desires, including socializing ones, and is primarily relevant for a social maximum. The market takes account only of tastes. Arrow calls this the consumption-side analogue of Pigou's divergence between social and private costs in production (p. 18).

**Notation (p. 19).** $R_i$, $P_i$, $I_i$ are individual $i$'s ordering, preference and indifference. Primes or superscripts distinguish several orderings of one person. Society has $R$, $P$, $I$ (provisionally). Individuals are assumed rational: each $R_i$ satisfies Axioms I and II. The problem is to build a social $R$ that also satisfies them (p. 19).

### 4. A digression on rationality and choice (pp. 19–21)
Rationality is at the heart of modern economics and intuitively appealing, but closer analysis shows difficulties, illustrated by zero-sum two-person games (p. 19). Footnote 16 says that for such games there can be little doubt that the theory of rational play has been completely solved, at least under certain restrictive assumptions (risk-neutral players; complete information about the rules). It affords some sort of check on rationality concepts derived by analogy with the firm under perfect competition (p. 19). It adds that the n-person and non-zero-sum theories are still in a dubious state (p. 19).

**Argument** (pp. 20–21):
- Rationality implies that choice from any set is determined by pairwise choices. In consumer theory the actual environment is always a whole line or plane, never a pair. Under plausible conditions, though, actual choices can be explained as if derived from pairs, so, at least conceptually, it makes sense to imagine choices actually being made from pairs (p. 20).
- In the zero-sum game, one could superficially have each player order his strategies by minimum profit and pick the best. The only reason this is regarded as truly rational is that, if both follow it, neither has an incentive to change even on learning the other's strategy. That is the min-max (saddle-point) theorem (p. 20).
- That theorem is valid because admitting a set of pure strategies also admits all their probability mixtures. An environment with more than one strategy thus contains infinitely many. One cannot even conceptually imagine a choice between just two strategies. Otherwise a saddle point would exist only in special cases, and ordering by minimum profit would not give a stable solution (p. 20).
- Arrow's conclusion: the pairwise model does not seem to suit this case well. It seems that the essential point, which is of general bearing, is that when we imagine a choice between two alternatives, we cannot exclude any probability distribution over them as a possible alternative. The shape of a reformulated rationality and its consequences cannot be foreseen. But it is at least a possibility, to which attention should be drawn, that the paradox to be discussed below might be resolved by a broader concept of rationality (pp. 20–21).

**Rothschild's view (reported).** Many writers feel that rationality, as a one-dimensional ordering of all alternatives, is absolutely necessary for economic theorizing. Rothschild: "Unless economic units act in conformity with some rational pattern no general theory about what would follow from certain premises would be possible." (p. 21)
- **Arrow replies:** there seems to be no logical necessity here. Theory could be built on other assumptions about the structure of choice functions if the facts seemed to call for it. The institutionalist school may be seen in part as such an attempt, though no systematic treatment has emerged (p. 21).
- Choice functions not built from orderings seem to match Rothschild's "real irrationality". But they need not result from impulsive behavior and may arise from full reflection, as in game theory (p. 21).
- Footnote 17: Rothschild attributes the view to Lange, but this seems a misinterpretation. Lange regards rationality (identified with ordering) as a highly convenient postulate if true, but not necessary. Footnote 18: Arrow, like Lange, sees economics as an attempt to discover uniformities in part of reality. Simplified theory-building is an absolute necessity for empirical analysis, but a means, not an end (p. 21).

## Toy example (ours, not from the text)
Alternatives $\{x,y,z\}$. Let $R$ contain exactly: $xRx, yRy, zRz, xRy, yRx, xRz, yRz$. (So $zRx$ and $zRy$ are false.)

1. **Axiom I:** $x,y$: both $xRy$ and $yRx$ hold. $x,z$: $xRz$ holds. $y,z$: $yRz$ holds. ✓
2. **Axiom II:** the only pairs with $zR\cdot$ are $zRz$. Any chain $aRb, bRc$ has $a\in\{x,y\}$ or $a=b=c=z$, and $x$ and $y$ are $R$-related to everything, so $aRc$ holds. ✓ Hence $R$ is a weak ordering.
3. **Definitions:**
   - $xIy$, since $xRy$ and $yRx$.
   - $xPz$, since not $zRx$.
   - $yPz$, since not $zRy$.
   - $xPy$ fails, because $yRx$ holds.
4. **Pair choices:** $C([x,y])=\{x,y\}$; $C([x,z])=\{x\}$; $C([y,z])=\{y\}$. Lemma 2 checks: $C([x,z])=\{x\}$ iff $xPz$ ✓.
5. **Choice from the triple (Def. 3):** $x\in C$ since $xRx, xRy, xRz$; $y\in C$ likewise; $z\notin C$ since $zRx$ fails. So $C(\{x,y,z\})=\{x,y\}$. It is determined by pair choices: $z$ loses its pair against $x$, and $x,y$ tie.

## Concepts
- [[interpersonal-comparison-of-utility]] (new) — comparing utilities across persons. Arrow holds it has no meaning, since the only meaning utility can be said to have is as an indication of behavior (p. 9)
- [[ordinal-preference]] (new) — preference without cardinal or interpersonal significance, assumed throughout (p. 11)
- [[von-neumann-morgenstern-utility]] (new) — a utility scale (unique up to linear transformation) whose value for a probability distribution is its expected utility; Arrow sees no special ethical significance in it, as far as he can see (pp. 9–10)
- [[weak-ordering]] (new) — a relation $R$ that is connected (Axiom I) and transitive (Axiom II), allowing ties (pp. 13–14)
- [[strong-ordering]] (new) — an ordering in which no ties are possible (pp. 13–14)
- [[choice-function]] (new) — $C(S)$ = elements $x\in S$ with $xRy$ for all $y\in S$. Here it is derived from $R$ (p. 15)
- [[tastes-vs-values]] (new) — ordering by direct consumption versus ordering that adds ethical standards. The boundary is unclear (p. 18)
- [[rationality-as-ordering]] (new) — individuals are "rational" if their $R_i$ satisfy Axioms I and II. Arrow says there seems to be no logical necessity for requiring it (pp. 19, 21)

## Canonical instances
- [[temperature-analogy]] (new) — measuring temperature by gas volume: a convenient scale, with no meaning for comparing intensity of changes (p. 10)
- [[zero-sum-minmax-case]] (new) — the saddle-point theorem's validity rests on admitting mixtures, so Arrow says a pairwise-built model does not seem to suit this case well (p. 20)
- [[unbounded-money-sequence]] (new) — the sequence $1-1/n$ dollars shows a case where no best alternative exists (p. 12)
- [[factory-smoke-vs-heathenism]] (new) — from a formal point of view, dislike of factory smoke and distaste for heathenism cannot be told apart as relevant or irrelevant (p. 18)

## Bridges (candidates)
- [structural-analogy] Tastes vs values ↔ welfare economics: private vs social cost (Pigou) — Arrow himself calls it the consumption-side analogue (p. 18).
- [same-math] Weak ordering ($R$ connected and transitive) ↔ order theory: a total preorder — the same axioms.
- [structural-analogy] Choice determined by pairwise choices ↔ political-science models that reduce collective decisions to pairwise majority votes (candidate; to be confirmed).
- [metaphor] Ordinal utility ↔ measurement scales: only the order, not differences, carries meaning (cf. the temperature analogy).

## Questions this raises
- Given that the social $R$ must also satisfy Axioms I and II, which rules for building it from individual $R_i$ exist? Arrow says a "paradox" is to follow (p. 21).
- If the chooser's environment includes probability distributions, how should rationality be redefined (p. 20)?
- Can the distinction between tastes and values be operationalised, or must it stay a value judgment (p. 18)?
- Are there choice functions that satisfy plausible axioms but are not generated by any weak ordering (cf. footnote 11, p. 16, and p. 21)?

## Reading notes
- No equations were garbled.
- Printed page = pdf page − 11 (pdf 20 = p. 9).
- Footnotes 1–18 are only partly summarised here, mostly the ones that add logical content (3, 5, 6, 11, 16–18).
- Section 4 of the unit refers (p. 20) to Chapter II, Section 2. A paradox to be discussed below (p. 21) and "Chapter VII, Section 2" (footnote 9) are not part of this unit.
- Footnote 2 uses "Op. cit.", referring to an earlier citation outside these pages.
- No misprints were noticed.
