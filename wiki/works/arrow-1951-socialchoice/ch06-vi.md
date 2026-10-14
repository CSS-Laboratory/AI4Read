---
id: arrow-1951-socialchoice/ch06-vi
work: arrow-1951-socialchoice
unit: "Chapter VI. The Individualistic Assumptions"
pages: 61-73
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Individualistic Assumptions

## L0 — One line
Requiring each person's preferences to depend only on his own commodity bundle (and to favour more of everything) does not remove the impossibility of a satisfactory social welfare function when there is more than one commodity.

## L1 — The gist (≤ 120 words)
Can the usual "individualistic" restrictions on tastes rescue the possibility of a social welfare function (a rule mapping everyone's rankings into one social ranking)? Arrow says no. Such restrictions only fix some pairwise comparisons in advance. For some sets of three alternatives they fix nothing, so every ordering of those alternatives stays admissible. The earlier impossibility result (Theorem 2) therefore still applies (Theorem 3). One commodity, game theory, and Bergson's distributional ethics are discussed in turn. Bergson's scheme is shown to be mathematically the same problem (if tastes are restricted only to refer to own consumption), so it fails too. This matters because it undercuts the new welfare economics' hope of getting social judgments from individualism alone.

**Prerequisites:** weak orderings (complete, transitive "preferred or indifferent"); the earlier Conditions 1–5 and Theorem 2 of Arrow's book (restated only briefly here); basic consumer theory (commodity bundles, indifference curves). The terms "imposed", "dictatorial", "maximal states" and Conditions 2 and 3 come from earlier chapters and are not defined on these pages.

## L2 — Key ideas (5–10 bullets)
- The two individualistic assumptions yield only a partial "known preference or indifference" relation Q_i (a quasi-ordering) for each person; the true ordering R_i must be compatible with it (it must at least copy every known preference or indifference, cf. (23), p. 67) (pp. 61–62).
- Condition 1′ replaces Condition 1: admissible profiles are exactly those with every R_i compatible with Q_i (p. 62).
- Theorem 3 and its Corollary: if there is more than one commodity and every set of individual orderings satisfying the individualistic assumptions is admissible, any social welfare function satisfying Conditions 2 and 3 is imposed or dictatorial (p. 63).
- Hence, if the individualistic assumptions are the only restrictions on tastes, the customary study of maximal states is pointless as a preliminary to a social welfare function. Extra restrictions might still make one possible, and then the social maximum lies among the individualistic maximal states (pp. 63–64).
- The key tool is Lemma 4, proved from Szpilrajn's theorem (every quasi-ordering has a compatible weak ordering). It says a preassigned partial ordering gives no indirect information about choices inside a set it says nothing about (pp. 64–68).
- The difficulty persists even if all men have the same tastes, even with convex indifference curves. Social judgments need similar attitudes toward social alternatives (pp. 68–69).
- With one commodity, Conditions 1 and 2 of §1 fix each individual's ordering, so a social welfare function exists, but this case is qualitatively different (pp. 69–70).
- If tastes are not restricted a priori (beyond referring to own consumption), the Bergson scheme (unanimous value judgments plus tastes as input) is mathematically isomorphic (it has the same form) to the individualistic case, so it fails too (p. 72).

## L3 — Walkthrough

### 1. Statement of the assumptions (pp. 61–62)
Arrow notes two conditions almost always assumed in welfare economics (p. 61):
1. An individual compares social states only by the commodities he receives (and labour he expends). He is indifferent between states in which his own consumption–leisure–saving situation is the same or indifferent to him.
2. If one personal situation gives at least as much of every commodity (leisure and saving count as commodities) and more of at least one, he prefers it.

With more than one commodity, these do not suffice to remove the paradox (p. 61).

**Formalisation.** Some but not all of an individual's choices are known in advance. "x is known to be preferred or indifferent to y" is the relation in question (p. 61).
- If x is known preferred-or-indifferent to y but x is not known indifferent to y, then x is known to be preferred to y (p. 61).
- The relation is transitive and every alternative stands in it to itself, so it is a quasi-ordering (Definition 7, not reproduced here). It is not connected: it says nothing about two alternatives where each gives more of a different commodity (pp. 61–62).
- If Q_i is this quasi-ordering and R_i the individual's true ordering, R_i must be compatible with Q_i (Definition 8) (p. 62).
- The Q_i differ across individuals. More of each commodity for one person may be less for another (p. 62).

There are n quasi-orderings Q_1,…,Q_n, and it is known that R_i is compatible with Q_i. Arrow says that, if this knowledge is available beforehand, one might feel it superfluous to require the social welfare function to cover profiles where some R_i is incompatible with Q_i. Hence Condition 1 can be replaced by (p. 62):

**Condition 1′:** The admissible sets of individual orderings R_1,…,R_n are precisely those for which R_i is compatible with Q_i for each i.

*Intuition note:* Instead of allowing every possible ranking, we allow only rankings that agree with the "more is better" comparisons everyone already accepts. The question is whether that cut is big enough to escape the impossibility result.

### 2. The possibility theorem under individualistic assumptions (pp. 62–64)
By Theorem 2, Condition 1′ will be inconsistent with Conditions 2–5 if it does not restrict the admissible sets more sharply than Condition 1 does (p. 62). Take a set S of three alternatives such that for each i and each pair of distinct x, y in S, not x Q_i y. An example is three distributions of fixed commodity stocks where, for each pair, one gives an individual more of one commodity and the other more of another (p. 62).

Arrow thinks it intuitively clear that compatibility with Q_i is, as far as S is concerned, no restriction, and supports this with Lemma 4. Let T_1,…,T_n be any n orderings of S. Lemma 4 (§3) gives, for each i, an ordering R_i compatible with Q_i that coincides with T_i on S. Such sets are admissible under Condition 1′, so Condition 1 is satisfied and Theorem 2 applies. Conditions 2–5 cannot all hold (pp. 62–63).

**Theorem 3:** If Q_1,…,Q_n are quasi-orderings for which there exists a set S of at least three alternatives such that, for all i and all distinct x, y in S, not x Q_i y, then every social welfare function satisfying Condition 1′ and Conditions 2 and 3 is either imposed or dictatorial (p. 63).

**Corollary (Possibility Theorem for Individualistic Assumptions):** If there is more than one commodity, and every set of individual orderings each satisfying the individualistic assumptions is admissible, then every social welfare function satisfying Conditions 2 and 3 is imposed or dictatorial (p. 63).

The result applies to any attempt to restrict individual orderings by preassigned partial orderings. Example: suppose that between two bundles equal for the individual he chooses by some measure of income equality, but still prefers any bundle with at least as much of everything and more of one. S can still be formed, so the negative conclusion stands (p. 63).

**Maximal states.** If individual desires are formed individualistically and the only restrictions on tastes are the individualistic ones, the customary study of maximal states (Chapter IV) is pointless. Its only purpose is as a preliminary to social welfare functions, and none is then possible (p. 63). Arrow adds a qualification:
- Further restrictions might make a social welfare function possible. An example is promised in Chapter VII, Section 2 (p. 63).
- A state maximal under the combined restrictions is maximal under the individualistic ones alone. So the social maximum would be among the individualistic maximal elements, and the new welfare economics may still help narrow the search (pp. 63–64).

*Intuition note:* Telling people "more is better" fixes no comparison among bundles that trade one good for another. Individual rankings of such bundles stay as unrestricted as before, so the impossibility result still applies.

### 3. Quasi-orderings and compatible weak orderings (pp. 64–68)
**Szpilrajn's theorem:** If Q is a quasi-ordering, there is a weak ordering R compatible with Q (p. 64). In demand theory: "all components larger" is a quasi-ordering. The theorem lets us draw a complete indifference map respecting it, i.e. with downward-sloping curves. This is trivial in any particular application but not in full generality (p. 64).

**Lemma 4:** Let Q be a quasi-ordering and S a set of alternatives such that, for distinct x, y in S, not x Q y. Let T be a relation that is a weak ordering on S. Then there is a weak ordering R of all alternatives, compatible with Q, such that x R y iff x T y for x, y in S (p. 64).

Meaning: if the known choices give no direct information within S, they give no indirect information either. Any ordering of S is compatible with them (p. 65). In demand theory, positive marginal utilities say nothing about the choice among bundles on one budget plane. They do say that the choice lies on the plane, not below it (p. 65).

**Proof (key steps).**
- Let Q″ be any quasi-ordering with
 (1) x Q y implies x Q″ y; (2) for x, y in S, x T y implies x Q″ y.
 Universal indifference satisfies both, so at least one such Q″ exists (p. 65).
- (3) Define x Q′ y iff x Q″ y for all Q″ satisfying (1) and (2). Then (4) Q′ is a quasi-ordering, and (5) x Q y implies x Q′ y, and (6) for x, y in S, x T y implies x Q′ y (p. 65).
- **Claim (13): for x, y in S, not x T y implies not x Q′ y.** Take x′, y′ in S with not x′ T y′. Let X_1 be the set of x such that either (7) x in S and x T y′, or (8) for some z in S, x Q z and z T y′. Define (9) x Q_1 y iff x in X_1 or y not in X_1. Then (10) Q_1 is a quasi-ordering (p. 66).
 - (11) x Q y implies x Q_1 y. If x Q y and y in X_1, then either y T y′, giving x in X_1 by (8), or y Q z with z T y′, so x Q z by transitivity and x is in X_1 by (8) (p. 66).
 - (12) For x, y in S, x T y implies x Q_1 y. If y is in X_1 then x is in X_1, using that T is a weak ordering and that, for y, z in S, y Q z can hold only with y = z by hypothesis (p. 66).
 - So Q_1 satisfies (1) and (2). But y′ is in X_1 by (7), since y′ T y′. If x′ were in X_1, (7) would give x′ T y′, and (8) would force z = x′, so again x′ T y′, contrary to assumption. So not x′ Q_1 y′, hence not x′ Q′ y′ by (3). This is (13) (p. 66).
- **Claim (21): x Q y and not y Q x imply not y Q′ x.** Take x′ Q y′ and not y′ Q x′. Let X_2 be the set of x such that (14) x Q x′, or (15) x in S and, for some z in S, x T z and z Q x′, or (16) for some z_1, z_2 in S, x Q z_1, z_1 T z_2, z_2 Q x′. Define (17) x Q_2 y iff x in X_2 or y not in X_2. Then (18) Q_2 is a quasi-ordering, (19) x Q y implies x Q_2 y, and (20) x T y in S implies x Q_2 y (pp. 66–67). Now y′ is not in X_2, because each of (14)–(16) leads to a contradiction. For (14) this is not y′ Q x′; the other two cases reduce to it using the hypothesis on S. But x′ is in X_2 by (14). So not y′ Q_2 x′ by (17), hence not y′ Q′ x′ (p. 67).
- By (4) and Szpilrajn's theorem there is a weak ordering R with (22) R compatible with Q′ (p. 67).
- (23) x Q y implies x R y, by (5), (22) and Definition 8(c). Using (5), (21), (22) and Definition 8(d), the strictly-known-preferred case gives (24); see Reading notes for a misprint in (24). From (23), (24) and Definition 8, (25) R is compatible with Q (pp. 67–68).
- (26) For x, y in S, x T y implies x R y, by (6), (22), Definition 8(c). If not x T y, then y T x (T is a weak ordering). From (6) and (13), y Q′ x and not x Q′ y. By (22) and Definition 8(d), not x R y. So (27): for x, y in S, x R y iff x T y. (25) and (27) prove the lemma (p. 68).

*Intuition note:* The proof builds a smallest "forced" relation Q′ from everything compatible with Q and T. It then shows Q′ forces nothing extra inside S. Szpilrajn's theorem finishes the ordering.

### 4. An example (pp. 68–69)
Two individuals, ten units of each of two commodities, three distributions (p. 68):

| Alt. | Ind. 1 (c1, c2) | Ind. 2 (c1, c2) |
|---|---|---|
| 1 | 5, 1 | 5, 9 |
| 2 | 4, 2 | 6, 8 |
| 3 | 3, 3 | 7, 7 |

No individual gets at least as much of both commodities in any alternative as in any other. The individualistic restrictions tell nothing about either person's ordering, so all preferences are permitted and the paradox holds (p. 68).

Further restrictions sometimes used do not suffice either. Suppose all men have the same preferences over individual situations. Given any ordering of the three social alternatives by the two individuals, build a scale for the six individual situations. Rank the three available to individual 2 by his preferences and put all of them above the three available to individual 1, which are ranked by individual 1's tastes (pp. 68–69). If each allocation of each commodity in alternative 2 is reduced by .5, this scale can even be embedded in an indifference map with convex curves. So even convexity is not enough (p. 69).

Arrow says the results suggest strongly that the difficulties arise from the differing social attitudes that follow from individualism, especially when tastes for individual consumption are similar. The possibility of social welfare judgments rests on similarity of attitudes toward social alternatives (p. 69).

### 5. A one-commodity world (pp. 69–70)
With one commodity, Conditions 1 and 2 of §1 leave each individual one possible ordering: by the amount he gets. Individual orderings are no longer variables, so Conditions 2, 3 and 4 become irrelevant. Condition 5 (nondictatorship) is much weaker but not irrelevant (p. 69).

Any social ordering not coinciding with one individual's ordering is a permissible social welfare function. Example: for each fixed total output, set an arbitrary ordering of distributions. Order states with different totals by total output, and same-total states by the arbitrary ordering. Let x, y have totals s, t and apportionments s′, t′ to the given individual. If s > t but s′ < t′, society prefers x while the individual prefers y (pp. 69–70).

The qualitative difference makes welfare arguments resting on an implicit single commodity dubious for real situations. The difficulty is that of the Kaldor compensation principle (Chapter IV, §2): with several commodities we need a common standard of value (p. 70).

### 6. Group choice in the theory of games (p. 70)
In multi-person game theory each coalition ranks strategies by the sum of payments to its members. Why is there no paradox? Individualism is assumed there (each plays for his own interest), but §2 showed this is insufficient (p. 70). The game world is a one-commodity world, with complications:
- Individuals also rank probability distributions of money payments. Left unrestricted, outcomes would act like different commodities and §2's situation would appear (p. 70).
- Von Neumann and Morgenstern assume individuals rank distributions by expected money value, which is implicit in assuming transferable utility. So each individual's ranking is prescribed in advance, as in §5 (p. 70).

### 7. Distributional ethics combined with individualism (pp. 71–73)
Many who think the new welfare economics applies directly assume (p. 71):
1. an accepted (say unanimously) judgment: if everybody is at least as well off, and one person better off, according to his tastes, in state 1 than state 2, state 1 is preferred;
2. a universally accepted ordering of welfare distributions, usually egalitarian.

This ethic is explicit in Bergson (the second judgment in his Propositions of Relative Shares) and underlies the Kaldor–Hicks compensation principle. It also seems to underlie Johnson's and Modigliani's food proposal. That proposal pairs an excise tax on food with a per capita subsidy to consumers. With completely inelastic agricultural supply, the farmers absorb the tax, and the subsidy has no marginal substitution effects, so the first judgment is met (p. 71).

Arrow distinguishes values from tastes (Chapter II, §3). Here all individuals share the same values at any instant, but the values held vary with everyone's tastes. Question posed: do the earlier arguments from diversity of values carry over to this unanimity (pp. 71–72)?

**Arrow's analysis (p. 72):**
- The distribution dictated by judgment (2) cannot be stated simply in money terms. Samuelson says such a judgment is not consistent with any well-defined social ordering. Real income distribution varies with tastes.
- Given tastes and a distribution of purchasing power, competitive exchange proceeds to an optimum. So the ethical system is a rule giving the social state chosen from an environment as a function of tastes. If the environment varies, choices are expected to be consistent, derivable from a social weak ordering.
- The "Bergson social welfare function" therefore assigns a social ordering to each set of individual taste-orderings. It has the same mathematical form as the earlier function. The differences are that the orderings represent tastes, not values, and that it comes from unanimously held values rather than from reconciling divergent ones.
- If tastes are not restricted a priori (they must only refer to own consumption), it is mathematically isomorphic to the social welfare function under individualistic assumptions. So the Corollary applies: no Bergson social welfare function satisfies judgments (1), (2) and Conditions 2–5 and yields a true social ordering for every set of tastes.
- The two judgments amount to erecting individualistic behaviour into a value judgment. It is not surprising that this does no better.

**Meaning of Conditions 2–5 has changed** (p. 73). Their earlier defence assumed orderings represent values. Arrow says it seems obvious that Conditions 2, 4 and 5 have the same intrinsic desirability under either reading. Condition 3 is perhaps more doubtful. Example: bread and wine, with wine-lovers deemed (by all) to get more wine and less bread than abstainers. If all the wine is destroyed, are wine-lovers entitled to more than an equal bread share? This is a value judgment. Arrow's own feeling: tastes for unattainable alternatives should not affect decisions among attainable ones, so Condition 3 reinterpreted for tastes is valid, "to me at least" (p. 73).

*Intuition note:* Making everyone agree on the ethics does not escape the problem, if tastes are not restricted beyond referring to own consumption. The social ranking must still be computed from tastes that can differ, and that is the same mathematical task as before.

## Toy example (ours, not from the text)
Use Arrow's bundles in his §4 style: A = (5,1), B = (4,2), C = (3,3) (commodity 1, commodity 2) for one person. No bundle has at least as much of both goods as another, so "more of everything is better" gives no comparison among A, B, C.
- Taste u = 3c₁ + c₂: A = 15 + 1 = 16, B = 12 + 2 = 14, C = 9 + 3 = 12. Ranking A > B > C.
- Taste u = c₁ + 3c₂: A = 5 + 3 = 8, B = 4 + 6 = 10, C = 3 + 9 = 12. Ranking C > B > A.
Both tastes increase in both goods, so both satisfy the individualistic assumptions yet rank the three in opposite order. By Lemma 4, every ordering of A, B, C is possible. So the set of admissible profiles contains all profiles on {A, B, C}, and Theorem 2 bites. With one commodity the amounts 5, 4, 3 force the ranking, so no such freedom exists (cf. §5).

## Concepts
- [[social choice function / social welfare function]] — here a rule assigning a social ordering to each admissible set of individual orderings (p. 62)
- [[arrow-impossibility-theorem]] — Theorem 2 (not on these pages) and Theorem 3 show Conditions 2–5 cannot all hold with Condition 1, or with Condition 1′ when a set S as in Theorem 3 exists (pp. 62–63)
- [[individualistic-assumptions]] (new) — an individual's ranking depends only on his own commodities, and "more of everything" is preferred (p. 61)
- [[quasi-ordering]] (new) — a relation covered by Definition 7 (not shown); here the "known preferred or indifferent" relation is transitive, relates each alternative to itself, and is not connected (pp. 61–62)
- [[compatible-ordering]] (new) — a weak ordering R compatible with Q is used in the proof as: x Q y implies x R y, with strict known preference preserved (pp. 62, 67–68)
- [[szpilrajn-extension]] (new) — every quasi-ordering has a compatible weak ordering (p. 64)
- [[bergson-social-welfare-function]] (new) — a rule from individual taste-orderings to a social ordering, built on unanimous value judgments (p. 72)
- [[values-vs-tastes]] (new) — tastes are orderings that must refer only to an individual's own consumption; values are what the value judgments express and are assumed shared (the distinction is from Chapter II, not on these pages) (pp. 71–72)

## Canonical instances
- [[three-alternative-two-commodity-table]] — three distributions of two commodities that no individual can compare by dominance (p. 68)
- [[bread-and-wine]] — tests Condition 3 read in terms of tastes (p. 73)
- [[food-tax-and-subsidy]] — Johnson–Modigliani proposal as a case of the two value judgments (p. 71)
- [[game-theory-coalition-sum]] — one-commodity world with transferable utility, so no paradox (p. 70)

## Bridges (candidates)
- [structural-analogy] Individualistic restriction leaves S unrestricted ↔ single-peaked preferences: a domain restriction removes cycles only if it actually cuts the admissible profiles on the alternatives at issue.
- [structural-analogy] Szpilrajn extension of a partial order ↔ order theory: extending a partial order to a complete one is used here to show a restriction is vacuous on S.
- [metaphor] Bergson's unanimous ethics ↔ folk theory of democracy: agreeing on principles does not by itself yield a consistent aggregate ranking.

## Questions this raises
- Which additional restrictions on tastes would make a social welfare function possible? The text promises an example in Chapter VII, §2 (p. 63).
- Arrow says possibility rests on similarity of attitudes toward social alternatives. How should that similarity be measured (p. 69)?
- Is Arrow's view that tastes for unattainable alternatives should be ignored (Condition 3) defensible against rival value judgments (p. 73)?

## Reading notes
- Printed page = pdf page − 11 (pdf 72–84 = printed 61–73).
- Definitions 7 and 8, Conditions 1–5, Theorem 2 and Chapters II, IV, VII are referred to but not in these pages. Their content is taken only as the text uses it.
- Misprint, as printed: equation (24) reads "x Q y and not y Q x imply not x R y" (p. 67), and the sentence just before the display says the same. From the argument (strict known preference in Q should rule out the reverse preference in R) it presumably should be "not y R x". This is an inference, since Definition 8(d) is not shown.
- p. 62 prints "R_i is not compatible with Q" without a subscript, presumably Q_i.
- The table (p. 68) was read from the page image. Arrow calls Szpilrajn's theorem as stated here "equivalent to one of" Szpilrajn's (p. 64).
