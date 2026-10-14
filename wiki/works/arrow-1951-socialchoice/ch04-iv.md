---
id: arrow-1951-socialchoice/ch04-iv
work: arrow-1951-socialchoice
unit: "Chapter IV. The Compensation Principle"
pages: 34-45
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# The Compensation Principle (Arrow 1951, ch. IV)

## L0 — One line
Arrow argues that the compensation principle with compensation actually paid only restates unanimity comparison, and that the version with compensation merely possible (Kaldor, Scitovsky) does not give a consistent social ordering meeting his conditions.

## L1 — The gist (≤ 120 words)
Can the welfare-economics "compensation principle" serve as a social welfare function? Arrow separates two versions. If compensations are actually paid, the principle only restates unanimity comparison (everyone weakly prefers x to y), which leaves some pairs of alternatives incomparable. If compensation is only possible (Kaldor), the ranking depends on other alternatives, can say both "x better than y" and "y better than x" (Scitovsky), and rests on an arbitrary rule and an unclear measure of total output. Scitovsky's repair gives a weak ordering for two alternatives but is intransitive for three; Arrow's numerical example shows this. So, in Arrow's argument, the Kaldor and Scitovsky forms do not give a consistent social ordering.

**Prerequisites:** weak ordering (complete, transitive preference R, with strict P and indifference I); indifference curves; Arrow's Conditions 1–3 as named in this unit.

## L2 — Key ideas (5–10 bullets)
- Compensation actually paid reduces to a unanimity rule: x Q y means everyone weakly prefers x to y. Q is only a quasi-ordering (reflexive and transitive, but some pairs may be incomparable), and a social ordering R should be compatible with it (pp. 34–36).
- Studying "maximal alternatives" (the new welfare economics) is a possibly useful preliminary, but Arrow finds it hard to see how a policy recommendation can rest merely on it: it does not say which maximal state to pick or which state to move to (p. 37).
- Arrow doubts that maximal-state analysis helps even for consumer-choice questions. If individuals order states only by their own commodities, Chapter VI will show that no social welfare function satisfying Conditions 1–5 exists (p. 37).
- The Kaldor principle (compensation possible, not paid) has an arbitrary utility rule behind it. For several commodities, "total output" has no meaning independent of income distribution (pp. 38–40).
- As stated, Kaldor's principle violates Condition 3 (the x–y choice should not depend on individual orderings of alternatives outside the pair). Restricting Condition 3 to admissible alternatives (one state chosen from each class of states derivable from one another by compensation) repairs this, but not Condition 1 (the social ordering must be a consistent ranking satisfying Axioms I and II) (pp. 40–42).
- Scitovsky showed Kaldor can give both x P y and y P x. His double test (use the Kaldor test where it gives no contradiction; otherwise call the states indifferent) gives a weak ordering for two admissible alternatives, given the usual assumption (6) (pp. 42–43).
- With three alternatives, Scitovsky indifference is not transitive (numerical example, pp. 44–45). Unaccomplished redistributions also seem irrelevant (p. 45).

## L3 — Walkthrough

### 1. The payment of compensation (pp. 34–37)
**Dictum.** If there is a method of paying compensations such that, after changing from y to x and paying them, each person prefers the resulting state to y (or is indifferent, and at least one actually prefers it), the community ought to prefer x to y *if the compensations are made* (p. 34). Arrow says this is not debatable, except perhaps on a philosophy of systematically denying people whatever they want (p. 34).

It is "roundabout": what matters is the *resulting* state, so call it x. Then $x P y$ if $x R_i y$ for all $i$ and $x P_i y$ for at least one $i$. Adding $x I y$ if $x I_i y$ for all $i$ gives Bergson's Fundamental Value Propositions of Individual Preference (p. 34).

**Unanimity relation.** Define
$$x\,Q\,y \text{ means that, for all } i,\ x R_i y. \tag{1}$$
Each $R_i$ is a weak ordering, so Lemma 1(a) and Axiom II give:
$$\text{for all } i,\ x R_i x \tag{2}$$
$$\text{for all } i,\ x R_i y \text{ and } y R_i z \text{ imply } x R_i z \tag{3}$$
From (2) and (1): $\text{for all } x,\ x Q x$ (4). If $xQy$ and $yQz$, then for each $i$, $xR_iy$ and $yR_iz$, so $xR_iz$ by (3), so $xQz$ by (1):
$$\text{for all } x,y,z,\ x Q y \text{ and } y Q z \text{ imply } x Q z \tag{5}$$
(pp. 34–35).

**Definition 7.** $Q$ is a *quasi-ordering* if (a) $xQx$ for all $x$ and (b) $xQy$ and $yQz$ imply $xQz$. Some pairs may be incomparable (neither $xQy$ nor $yQx$) (p. 35).

**Link to R.** If $xQy$, we can assert $xRy$ but not $xPy$ (e.g. $xI_iy$ for every $i$). If $xQy$ and not $yQx$, then $xR_iy$ for all $i$ and, for at least one $i$, not $yR_ix$, i.e. $xP_iy$ (Lemma 1(e)). This is the original compensation principle, so we should require $xPy$ (p. 35).

**Definition 8.** $R$ is *compatible with* $Q$ if (a) $R$ is a weak ordering; (b) $Q$ is a quasi-ordering; (c) $xQy$ implies $xRy$; (d) $xQy$ and not $yQx$ imply not $yRx$ (p. 35).

Call Q the *unanimity quasi-ordering*. The principle becomes: for any set of individual orderings, the social ordering is compatible with the unanimity quasi-ordering. It is not deducible from Conditions 1–5 as they stand, but would be if Condition 2 were slightly modified (p. 36).

*Intuition note:* Paying the compensation turns the principle into plain unanimity. It rules out options that everyone weakly dislikes and some strictly dislike. It puts no requirement on pairs that Q cannot compare.

**Maximal alternatives.** If $xQy$ but not $yQx$, then $xPy$, so by Definition 3 $y\notin C(S)$ (the chosen set). One could therefore eliminate such $y$, or find all *maximal* alternatives $x$ (no $y$ with $yQx$ but not $xQy$), since $C(S)$ must be contained among them. Studying this problem, under particular assumptions about $S$ and the individual orderings, has been the main content of what is sometimes called the "new welfare economics" (p. 36).

**Arrow's criticism.**
- Maximal alternatives may be a useful preliminary to analysing particular social welfare functions, but it is hard to see how any policy recommendation can be based merely on knowing them. There is no way of determining which maximal alternative to choose. Even from a nonmaximal state there is no way to know which better state to move to, so the community is in Buridan's ass's position (p. 37).
- Arrow goes beyond Samuelson. The doctrine that marginal rates of substitution are equal for all consumers assumes each person orders social states solely by the commodities he receives. Chapter VI will show that no social welfare function consistent with Conditions 1–5 can be formed if individual orderings are formed in that individualistic way, because then valuations of alternative income distributions conflict most sharply (p. 37).
- Hence the analysis of maximal states applies precisely when it cannot serve as a preliminary to a complete social ordering. This is "somewhat qualified" in Chapter VI, Section 3 (p. 37).
- The argument does not hold against optimum conditions on the production side. Resources there matter to members of the community only indirectly, through productivity in different uses. Only this assumption distinguishes production conditions from exchange conditions (p. 37).

### 2. The possibility of compensation (pp. 38–45)
**Kaldor principle.** If there is a method of compensation under x such that everybody can be made better off than in y (or at least as well off, with one better off), x should be chosen above y *even if the compensation is not paid*. Kaldor does not claim ethical optimality (the distribution under x might be very unjust). He claims x is better from the viewpoint of aggregate production (p. 38).

**Baumol's objections** (Hicks endorsed the principle) (p. 38):
1. It implies an interpersonal comparison, since compensations are measured in money.
2. Even in the seemingly innocuous case where everyone is actually better off, saying x is better would be valid only in some sort of utilitarian scheme of ethics.

Arrow's reply to (2): no doubt formally valid, in that some value judgment is involved, but the value judgment is so generalized that we would all be well content to assume it. "Better off" may also depend on others' consumption and social structure (p. 38).

Arrow's reply to (1): the objection "seems to be somewhat vague". The results of the Kaldor principle would be the same as summation of utilities when the marginal utility of real income is constant and the same across individuals (assuming that proviso makes any sense). That is not the same as assuming interpersonal comparison. The principle chooses utility indicators by a rule that gives marginal utility of income certain properties (Ch. III §6). This is arbitrary: another rule asks what *fraction* of income each person would need under x to match y, and calls x better if the fractions sum to a positive number (tentatively Modigliani). That rule relates to the Bernoulli assumption (marginal utility inversely proportional to income) as Kaldor's rule relates to constant marginal utility. So Baumol's objection is essentially to the arbitrariness (p. 39).

**Further objections (Arrow's).** Even among equally "reasonable" rules, why separate production from distribution? Any choice depends on both, and it is unclear how a production ordering would help (p. 39). More deeply, with several commodities, comparing total production requires a standard of value that makes commodities commensurable, and that standard usually depends on income distribution. So total output has no meaning independent of distribution. Only in a one-commodity world does the ambiguity vanish (p. 40). In general it would appear that replacing y by x as Kaldor's principle instructs changes the standard of value, so that we have, as Baumol says, "a measuring rod which bends, stretches, and ultimately falls to pieces in our hands" (Baumol, p. 40).

**Formal treatment.** Let $xCy$ mean "x is derivable from y by compensation payments". Kaldor: $xPy$ if there is $x'$ with $x'Cx$, $x'Qy$ and not $yQx'$. As stated, this violates Condition 3: if we do not have both $xQy$ and not $yQx$, the choice between x and y depends on Q between alternatives outside $[x,y]$, hence on individual orderings of those alternatives (p. 40).

Arrow's restatement uses three properties of C:
$$\text{(1) } xCx;\quad \text{(2) } xCy \Rightarrow yCx;\quad \text{(3) } xCy \wedge yCz \Rightarrow xCz.$$
Reasons: zero payments; reversing a payment $c_i$ to $-c_i$; payments add, $c_i+c_i'$ (pp. 40–41). So C is an equivalence relation. It splits social states into mutually exclusive *compensatory-equivalent classes*. Footnote 13 proves this by defining the class generated by x as $\{x' : x'Cx\}$ and checking (a)–(d) with properties (1)–(3) (p. 41).

Kaldor–Hicks spirit: states in one class are at the same production level, and choosing among them is an ethical question about distribution. We may imagine a preliminary value judgment that picks one *admissible* state per class, and the principle only ranks admissible states. If Condition 3 is read as requiring invariance only to changes in the orderings of other admissible alternatives, the restricted Kaldor principle satisfies it (pp. 41–42).

**Condition 1 still fails.** Scitovsky showed that, under Kaldor's principle, some individual orderings give both $xPy$ and $yPx$. That is incompatible with a social ordering, since $xPy$ implies not $yRx$ (Def. 1, Axiom I) (p. 42).

**Scitovsky principle (two alternatives).** $xRy$ iff there is $x'$ with
$$x'Cx \tag{4}$$
$$x'Qy \tag{5}$$
Assume that for any $x,y$ either compensation under x makes all as well off as under y, or the reverse (Arrow says this will usually be the case; fn. 17 notes that some orderings based partly on jealousy violate (6)):
$$\text{for all } x,y,\ xRy \text{ or } yRx \tag{6}$$
By Def. 7(a), $xQx$ (7). Taking $x'=y=x$ satisfies (4) and (5), so
$$\text{for all } x,\ xRx \tag{8}$$
Transitivity with only two alternatives: if $xRy$ and $yRz$, two of $x,y,z$ coincide. If $x=y$, then $yRz$ gives $xRz$. If $y=z$, then $xRy$ gives $xRz$. If $x=z$, $xRz$ is $xRx$, true by (8). So
$$\text{for all } x,y,z,\ xRy \text{ and } yRz \text{ imply } xRz \tag{9}$$
With (6) and (9), R is a weak ordering for two admissible alternatives. This is Scitovsky's *double test*, accepted by Kaldor: apply Kaldor where it is consistent, otherwise say indifferent (p. 43).

The real force of Scitovsky's argument is felt with more than two admissible alternatives, e.g. ranking many possible tariff schedules rather than choosing between free trade and one tariff (p. 43). If R were a weak ordering, the indifference relation formed from it would be transitive (Lemma 1(d), Def. 2); the example below shows Scitovsky indifference is not (p. 44).

**Three alternatives (example).** Scitovsky indifference between x and y means: some redistribution of x's goods leaves everyone at least as well off as in y, and some redistribution of y's goods does the same for x. Two commodities, two individuals, three states (holdings):

| State | Ind. 1 (c1, c2) | Ind. 2 (c1, c2) |
|---|---|---|
| x | 2.0, 1.0 | 2.0, 1.0 |
| y | 1.7, 1.3 | 1.8, 1.1 |
| z | 1.0, 2.0 | 1.0, 2.0 |

Each person orders states by his own bundle (p. 44). Individual 1 ranks bundles (best to worst): (2.1,1.0), (1.0,2.0), (2.4,.7), (1.7,1.3), (2.0,1.0). The curve through (1.0,2.0) has no bundle with second quantity below .9. Individual 2 ranks: (1.4,1.4), (1.0,2.0), (1.6,1.3), (1.8,1.1), (2.0,1.0). The curve through (1.0,2.0) has no point with second coordinate below 1.2. Such maps can have continuous, convex, downward-sloping curves (p. 44).
- **x vs y:** y is at least as good as x for both, so trivially some redistribution of y's goods leaves everyone no worse off than in x. State x has 4 units of c1 and 2 of c2. Give (2.4,.7) to 1 and (1.6,1.3) to 2. Both are then better off than in y. So $xIy$ (pp. 44–45).
- **y vs z:** both prefer z. State y has 3.5 of c1 and 2.4 of c2. Give (2.1,1.0) to 1 and (1.4,1.4) to 2. Both are better off than in z. So $yIz$ (p. 45).
- **x vs z:** both prefer z. To match z, individual 1 needs at least .9 of c2 and individual 2 at least 1.2, a total of at least 2.1. State x has only 2. So x and z are not indifferent: Scitovsky indifference is not transitive, and the principle does not satisfy Condition 1 (p. 45).

*Intuition note:* "Indifferent" must be transitive in a true ordering. Here x~y and y~z, yet z is clearly better than x. With two alternatives this problem cannot appear. With three it does.

**Closing points.** The x–y comparison shows a further problem for any form without actual payment: everyone may be better off in y than x, yet x can be redistributed so everyone is no worse off than in y. This suggests strongly that unaccomplished redistributions are irrelevant (p. 45). These arguments do not depend on the charge that the principle sanctifies the status quo. The last argument is an ethical objection to an implicit value judgment. The earlier ones argue that the defining value judgments are inconsistent with rational community choice (p. 45).

## Toy example (ours, not from the text)
Two people, two goods A and B, 3 units of each in each state. Person 1 cares only about A held, person 2 only about B held. Holdings (A, B):
- State x: person 1 = (1,0), person 2 = (2,3). Utilities (1, 3).
- State y: person 1 = (3,3), person 2 = (0,0). Utilities (3, 0).

Kaldor test for x over y: redistribute x's totals (3,3) as person 1 = (3,0), person 2 = (0,3). Utilities (3,3) vs y's (3,0): nobody worse, person 2 better. So x beats y.
Kaldor test for y over x: redistribute y's totals the same way. Utilities (3,3) vs x's (1,3): nobody worse, person 1 better. So y beats x.
Both $xPy$ and $yPx$, which is impossible for a social ordering. Scitovsky's double test says both redistributions exist, so x and y are indifferent. With only these two states, that is consistent.

## Concepts
- [[compensation-principle]] (new) — rule that x is socially better if compensations could make everyone at least as well off, and one better off (pp. 34, 38)
- [[unanimity-quasi-ordering]] (new) — relation Q: x Q y iff everyone weakly prefers x to y. It is reflexive and transitive, but not necessarily complete (pp. 34–36)
- [[quasi-ordering]] (new) — reflexive, transitive relation, not necessarily complete (Def. 7, p. 35)
- [[compatible-with-Q]] (new) — R is a weak ordering agreeing with Q, as in Def. 8 (p. 35)
- [[maximal-alternative]] (new) — x with no y such that y Q x and not x Q y (p. 36)
- [[kaldor-compensation-principle]] (new) — x preferred if compensation is possible, even if unpaid (p. 38)
- [[scitovsky-double-test]] (new) — x R y iff there is $x'$ with $x'Cx$ and $x'Qy$. Kaldor where consistent, otherwise indifference (pp. 42–43)
- [[compensatory-equivalent-class]] (new) — set of states derivable from one another by compensation payments; C is an equivalence relation (p. 41)
- [[social choice function / social welfare function]] — here, the compensation principle proposed as one, in the sense of Definition 4 (p. 40)
- [[independence of irrelevant alternatives (IIA)]] — Arrow's Condition 3 as used here: x–y choice should not depend on orderings of alternatives outside $[x,y]$ (p. 40) (canon link; name not used in this unit)

## Canonical instances
- [[buridans-ass-welfare]] — many maximal states, no way to choose among them (p. 37)
- [[tariff-schedules]] — ranking many tariffs, not just free trade vs one tariff (p. 43)
- [[scitovsky-three-state-example]] — two goods, two people, x I y, y I z, but not x I z (pp. 44–45)

## Bridges (candidates)
- [structural-analogy] Scitovsky intransitive indifference ↔ cycling/intransitivity: both give a collective relation that fails transitivity.
- [same-math] Unanimity quasi-ordering Q ↔ Pareto weak dominance (everyone at least as well off): the relation is "everyone weakly prefers".
- [structural-analogy] Restricting Condition 3 to admissible alternatives ↔ agenda control: ranking only a pre-selected menu.

## Questions this raises
- What exactly would the modification of Condition 2 be that makes compatibility with Q deducible (p. 36)?
- Chapter VI, Section 3 qualifies the claim about maximal states. What does it add (p. 37)?
- If actual compensation is paid, is the resulting state of the world still the one being ranked, as Arrow assumes (p. 34)?
- Does a different standard of value, rather than the Kaldor rule, make total output meaningful (p. 40)?

## Reading notes
- Printed page = pdf − 11. The text layer was empty, so everything is read from the page images.
- Definition 8(c) on p. 35 has a stray mark above the word "implies", which is still readable.
- Condition 3, Definitions 1, 3 and 4, Axioms I–II, Lemma 1 and Conditions 1–5 are used here but not stated on these pages (the text points to Chapter III and earlier material).
- Footnote 4 (p. 36, literature on the new welfare economics) is not summarised; footnote 13 (p. 41) is compressed to its main points.
- Equation numbers restart: (1)–(5) in Section 1; in Section 2, (1)–(3) are the properties of C and (4)–(9) belong to the Scitovsky argument.
