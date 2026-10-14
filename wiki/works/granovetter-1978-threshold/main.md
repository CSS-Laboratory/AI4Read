---
id: granovetter-1978-threshold/main
work: granovetter-1978-threshold
unit: paper
pages: 1420–1443
fields: [complex-systems]
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
# Threshold Models of Collective Behavior (Granovetter 1978)

## L0 — One line
Each person acts once the share of others already acting reaches a personal threshold, so the final collective outcome depends on the exact distribution of thresholds, and two groups with almost the same average preferences can end up in very different places.

## L1 — The gist (≤ 120 words)
Granovetter asks how individual preferences add up to a collective outcome when each person's choice depends on how many others have chosen. He gives each actor a "threshold", the proportion of others who must act first. He tracks the share acting over time with $r(t+1)=F[r(t)]$ and finds the equilibrium where $F(r)=r$. Tiny changes in the threshold distribution can flip an outcome from one rioter to everyone. So outcomes cannot be read off average preferences, and it is hazardous to infer individual dispositions from aggregate results. He also examines friendship structure, sampling variability, links to game theory, misperception, measurement, and one empirical test.

**Prerequisites:** cumulative distribution function (c.d.f.); iterating a function (difference equation); the normal distribution; basic binomial probability.

## L2 — Key ideas
- A threshold is the proportion (or number) of others who must act before a given person does. It is the point where that person's perceived benefits start to exceed costs, and it is a behavioral, not a normative, quantity (pp. 1420, 1422, 1435).
- Dynamics: $r(t+1)=F[r(t)]$. The equilibrium is where the c.d.f. meets the 45° line, $F(r)=r$. In the simple model an equilibrium is always reached (pp. 1425–1427).
- Two crowds that look nearly identical can give very different outcomes. Uniform thresholds 0,1,…,99 give 100 rioters. Replacing the threshold-1 person by a second threshold-2 person gives 1 (pp. 1424–1425).
- With normal thresholds (mean 25) the equilibrium jumps from about 6 to nearly 100 as the standard deviation passes about 12.2, so average preferences are a poor guide (p. 1427).
- Stability matters. The perturbed-uniform equilibrium (1 rioter) is relatively stable against social-structure effects. The true-uniform one (100) is unstable against almost any kind. If crowds are random samples of 100 from a population with uniform thresholds, 0 or 1 rioter results in over half of cases (pp. 1430–1431).
- Threshold models treat heterogeneity and sequential interdependence as central, which game theory handles only with difficulty. From thresholds alone they cannot say whether an equilibrium is optimal for anyone (pp. 1434–1435).
- The model is of little interest, in effect falsified, where all or most thresholds are 0% or 100%. It needs each net-benefit curve to cross zero at most once. Measurement is hard, and one village test suggests the threshold model predicts better than standard methods only when regressions explain more than about 50% of threshold variance (pp. 1437–1441).

## L3 — Walkthrough

### Abstract and Background (pp. 1420–1421)
The models cover binary choices where costs and benefits depend on how many others choose each way. The key concept is the threshold. From a frequency distribution of thresholds one computes an "equilibrium" outcome. Groups with similar average preferences may get very different results, so it is hazardous to infer individual dispositions from aggregate outcomes (p. 1420).

Granovetter's complaint is that norm-oriented theory implicitly assumes: if most members make the same decision, most share the same norm or belief (p. 1421). He argues that knowing norms, preferences, motives, and beliefs can, in most cases, only provide a necessary but not a sufficient condition for explaining outcomes. One also needs a model of how preferences interact and aggregate (p. 1421). He takes the variation of preferences within the group as the most important causal influence on outcomes (p. 1421). The models do not explain where preferences come from. They start from preferences and aggregate them (p. 1421). Applications reach beyond "collective behavior": voting, segregation, innovation diffusion, education, strikes, migration, markets (p. 1421).

### Model setup (pp. 1422–1424)
- **Binary decision:** two mutually exclusive alternatives. The costs and benefits of each depend partly on how many others choose each (p. 1422). Example: the cost of joining a riot falls as riot size rises, because arrest is less likely (p. 1422).
- **Actors** are assumed rational: given goals, preferences, and perceived situation, they maximize utility. Individuals differ (p. 1422).
- **Threshold:** the proportion of the group a person must see join before joining. A "radical" has a low threshold. Threshold 0% marks an "instigator". Threshold 100% marks someone who would never join (p. 1422).
- Equal thresholds need not mean identical people, since a threshold is the result of some possibly complex mix of costs and benefits (p. 1422).
- Footnote 2: the idea is adapted from Schelling's segregation models. Wheeler's "behavioral contagion" differs because it ignores how many people one must observe and cumulative effects (p. 1422).
- **Catalogue of applications** (p. 1423–1424): diffusion of innovations; rumors and diseases (credulity or vulnerability = threshold); strikes (non-tenured teachers expected to have higher thresholds); voting (bandwagon effects); college attendance; leaving social occasions; migration (chain migration); experimental social psychology (conformity, risky shift, bystander helping thresholds).

### Equilibrium outcomes in simple threshold models (pp. 1424–1428)

**Uniform example.** 100 people have thresholds 0,1,…,99, one each. The instigator (0) acts, which activates threshold 1, then 2, and so on. This is a "bandwagon" or "domino" effect, and the equilibrium is 100 (pp. 1424–1425). Footnote 3: thresholds may be proportions or absolute numbers, and the mathematics is the same (p. 1424).

**Perturbation.** Remove the threshold-1 person and replace him with a second threshold-2 person. The crowds look essentially identical, but now no one has threshold 1. The riot stops at one rioter (p. 1425). Newspapers would call the first "a crowd of radicals" and the second "a demented troublemaker" with "solid citizens" watching, though the compositions are nearly identical. The difference comes only from aggregation, specifically the gap in the distribution (p. 1425). Threshold models may be of particular value where average preferences clearly favour an action but it is not taken (p. 1425).

> Intuition note: A single missing threshold value breaks the chain. Everyone above the gap waits for someone who never acts. A reporter looking only at the outcome would misjudge the crowd's character.

**Formalization** (pp. 1425–1427; analysis due to Winship, fn. 4).
- $x$ = threshold, $f(x)$ = frequency distribution, $F(x)$ = c.d.f. (proportion with threshold $\le x$). $r(t)$ = proportion who have joined by discrete time $t$ (p. 1425).
- If 60% have joined at $t=2$, those rioting at $t=3$ are exactly those with thresholds $\le 60\%$. Hence
$$r(t+1)=F[r(t)] \tag{difference equation, p. 1425}$$
- Setting $r(t+1)=r(t)$ gives the equilibrium $r_e$, with $F(r_e)=r_e$ (p. 1427). If $F$ is not simple, the equilibrium can be computed by forward recursion (p. 1426).
- With no provision for "removal" of participants, oscillation of $r(t)$ is not possible and an equilibrium is always reached (p. 1426).
- **Graphical method (fig. 1).** Plot $F(x)$ against $x$ with the 45° line $F(x)=x$. From $r(t)$ go up to the c.d.f. to get $F[r(t)]=r(t+1)$. Then go horizontally to the 45° line, and repeat. In the drawn case the arrows shrink to zero and $r(t)\to r_e$. That limit is where the c.d.f. first crosses the 45° line from above (pp. 1426–1427).

> Intuition note: The c.d.f. is a "next-step" map: given the share acting now, it says the share acting next. Equilibrium is where the map returns its own input. The staircase of arrows shows the bandwagon stopping.

**Normal distributions** (analysis due to Phillips, fn. 5; p. 1427). $N=100$, thresholds normal with mean 25. Thresholds below 0 act like 0, and thresholds above 100 act like 100. The author varies the standard deviation $\sigma$ with the mean fixed (fig. 2):
- Up to a critical $\sigma_c\approx 12.2$, equilibrium rioters rise gradually to about 6.
- Past $\sigma_c$, $r_e$ jumps to nearly 100, then declines.
- As $\sigma\to\infty$ the limit is 50, because all area right of the mean counts as beyond 100 and all area left as below 0 (p. 1427).

*Mathematical explanation:* the normal c.d.f. may meet the 45° line three, two, or one times. Below $\sigma_c$ the first intersection from above is at a low point, followed by one from below and another from above. At $\sigma_c$ the first two merge in a tangent point, with one more intersection above. Beyond it the only intersection is near 100 (p. 1427).

The author says there is no obvious sociological reason why a slight perturbation near $\sigma_c$ should have a wholly discontinuous effect. Such a cause could be a minor fluctuation in crowd composition, too small for anyone to attribute the effect to it. Sociological theory focuses on averages, not exact distributions (pp. 1427–1428). Two crowds with nearly identical average preferences could generate entirely different results (p. 1428).

> Intuition note: Near $\sigma_c$ a small widening of the spread makes the low intersections of the c.d.f. with the 45° line merge and vanish, leaving only the high one. This is a sudden switch, not a slow drift. The jump comes from the shape of the distribution, not from any change in "mood".

### The stability of equilibrium outcomes (pp. 1428–1433)
Because real distributions may change, for instance as people enter or leave, one needs the stability of equilibria against perturbation. The true uniform distribution and the normal near $\sigma_c$ have highly unstable equilibria (pp. 1428–1429). "Stability" here means robustness to changes in the threshold distribution. Two factors are examined: social structure and spatial/temporal dispersion (p. 1429).

**Friendship and influence** (pp. 1429–1430). Assume friends count twice as much as strangers, and thresholds are stated for strangers. Take a person with threshold 50% in a crowd of 100 where 48 have rioted. He knows 20 people, 15 of whom have joined.
- He "sees" rioters: $(15\times2)+(33\times1)=63$.
- He "sees" nonrioters: $(5\times2)+(47\times1)=57$.
- Perceived proportion: $63/120=.525>.50$, so he joins. Without social structure he would not (p. 1429).

Computation needs the threshold distribution, a sociomatrix (who knows whom), and a weight per cell. Then forward recursion applies (p. 1429). For fixed friendship density the number of possible sociomatrices is almost limitless. Analytic derivation of the distribution of equilibria failed (unmanageable convolutions); some partial results are available if friendship need not be symmetric (pp. 1429–1430).

*Perturbed uniform* (one person at 0, two at 2, one each at 3,…,99). Null hypothesis: social structure makes no difference, so the equilibrium stays 1. It becomes increasingly improbable as friends' weight increases. Surprisingly, the largest effects occur when people know about one-quarter of the rest of the group. The author says the explanation is not obvious and needs further study (p. 1430).

*Simulations* (Danforth, fn. 6). Results are close to the analytic ones, and tie symmetry has little effect. For the perturbed uniform, even when the null is false the equilibrium rarely exceeds five to 10 rioters, so the outcome of 1 is relatively stable. For the true uniform, the equilibrium of 100 is unstable against almost any social-structural influence. For most weight and acquaintance combinations tested, the modal equilibrium is one rioter (p. 1430).

Author's conclusion: when equilibria are very stable, social structure may matter little. When they are unstable, its effects may overwhelm those of individual preferences (p. 1430).

> Intuition note: Friendship changes who "counts" for whom, so it can rescue or break a chain. A chain that is already fragile (true uniform) is easily cut by a little network structure. One with a robust small outcome barely moves.

**Spatial and temporal effects** (pp. 1431–1433). The simple model assumes complete connectedness. Stark et al. report that the 1965 Watts riot consisted of more than 1,850 separate riot actions over five days (p. 1431).

*Sampling example.* Take a large city population with uniform thresholds (1% at each of 0%,…,99%). Each crowd is a random sample of size 100. A uniform crowd would give everyone rioting, but sampling changes this.
- Draw each member as a Bernoulli trial with success (a zero percenter) probability $.01$. Probability of no instigator: $(1-P)^{100}=.37$, giving equilibrium 0.
- Probability of exactly one zero percenter and no one-percenters: $\left[\binom{100}{1}(.01)(.99)^{99}\right]\times(.99)^{100}=.14$, giving equilibrium 1.
- So in over half of cases ($.37+.14=.51$) the equilibrium is 0 or 1 (p. 1431).

Two crowds, or two cities, with the same underlying distribution may differ radically for reasons that reflect only sampling variability. This happens if the underlying equilibrium is easily disrupted (pp. 1431–1432).

*Spilerman's finding* (pp. 1432). In regressions on racial disorders 1961–68, the only important city characteristics were absolute size of the black population and, much less so, region (South vs. non-South). Spilerman read this as an aggregate of individual attributes. Granovetter offers a mechanism with more than "personal attributes": suppose each crowd that gathers has the same probability, say .10, of reaching an equilibrium big enough to count as a "riot", and larger black populations mean more incidents. Then the expected number of large riots is the number of incidents times .10. A town with one incident has a 90% chance of no large riot. With 10 incidents the chance of none is $(.90)^{10}=.35$ with the same threshold distribution (p. 1432).

*Spatial clusters and movement* (p. 1433). Multiple samples can stand for separate clusters of people. If the equilibrium is unstable, local outcomes diverge widely. Movement among clusters can have a "reverse bandwagon" effect: too much movement out of a high-equilibrium cluster may deactivate some rioters, which deactivates others, until a lower equilibrium is reached. For some distributions small movements among clusters may therefore have greater effects than large ones, but "much more mathematical work is needed" (p. 1433).

Applications: Korean villages with some intervillage migration, and spread of a party such as Nazi membership in Weimar Germany. Threshold distributions, friendship structures, and migration patterns could have more impact on adoption level than features of the programmes themselves. This could explain why the same family-planning programme has different outcomes where average preferences are nearly identical (p. 1433).

### Some theoretical and empirical considerations (pp. 1433–1441)

**Thresholds, game theory, and norms** (pp. 1433–1435).
- Threshold models share with game theory the assumption of rational actors with complete information (p. 1433).
- *Game-theory limits* (author's view): Brown reduced collective episodes to a two-person Prisoners' Dilemma against "everyone else". That is possible only if all actors are homogeneous in preferences. $n$-person games make outcomes hard to characterize without arbitrary assumptions. Game theory typically assumes simultaneous decisions (p. 1434).
- *Berk's riot game* (p. 1434–1435). Berk's simultaneity forces him to explain outcomes by events before any riot action begins. He therefore needs a convergence of assessments reminiscent of "emergent norms" (pp. 1434–1435).
- *Threshold advantage:* it puts heterogeneity and interdependence over time at the centre. The $n$-dimensional payoff matrix becomes a one-dimensional vector of thresholds, which simplifies the analysis (p. 1435).
- *Cost:* threshold analysis cannot say whether an equilibrium maximizes anyone's utility or is Pareto optimal. Thresholds carry no information about the utility of each possible equilibrium (p. 1435).
- *Matza's delinquent boys:* most did not think illegal acts right, but none could say so without status loss. Their threshold for stealing cars is low because reluctance risks being labelled a sissy. Bandwagon effects follow. The suboptimality for most boys would not be known from thresholds alone, but needs Matza's interviews (p. 1435).
- Thresholds are therefore different from norms. The boys act against norms they actually hold. This shows norms are only one causal influence and not always decisive. A threshold is purely behavioral (p. 1435).

**Nature and determinants of thresholds** (pp. 1436–1437).
- Thresholds result partly from norms, background, class, education, and so on, which explains moderate correlations with behavior. Correlational studies miss the aggregation dynamics. If two nearly identical threshold distributions give very different outcomes, regression-based predictions will predict the same outcome for both (p. 1436).
- Thresholds are situation-specific, not fixed traits. The author argues only that in many situations they stay constant long enough for a predictable equilibrium to be reached (p. 1436).
- Large changes in behavior should not be confused with changes in threshold. In a lynch mob the model suggests continuity of contingent dispositions, while behavior changes (p. 1436). Thresholds may change through emotional shocks (conversion meetings, though bandwagon effects are suggested there) or situational changes (arrival of "law and order" forces). This does not invalidate the model, but makes stability analysis important. Persistence of behavior despite changes may reflect an equilibrium unusually resistant to perturbation (pp. 1436–1437).

**Falsification** (pp. 1437–1439).
- *Weber's umbrella case:* people may all react to rain, not to each other (Weber's view, p. 1437). Granovetter replies that some umbrella behavior is partly determined by others. A threshold of $x\%$ only says the person acts once $x\%$ of others have. Others' behavior may be a marginal influence, and non-social influences enter the threshold itself (p. 1437).
- The model is of little interest, "in effect falsified", where all or most thresholds are 0% or 100%, meaning most behavior is not contingent on others (p. 1437).
- *Misperception* (p. 1438), three cases: (1) Systematic misperception. If the same for all, the model is unchanged. If it varies systematically with threshold, adjustment is not difficult. If more random, the situation is more complex and the equilibrium's stability becomes important. (2) Actions hidden: "pluralistic ignorance" (Merton), where many thresholds may be passed but actors do not know it. The model is then not falsified and guides policymakers. (3) Limited discrimination: someone with a 17% threshold may not distinguish 15% to 20%, so the operational threshold becomes 15% (p. 1438).
- *Single-crossing requirement (fig. 3):* an individual's net benefit (benefits minus costs) against group participation may be non-monotonic, but the models require that it not cross the x-axis more than once. The threshold is where net benefit first becomes positive. Restaurant example: a nearly empty restaurant is a bad sign, but a very crowded one means unbearable waiting, so two crossings. With two crossings, results can be computed by forward recursion but equilibria cannot be guaranteed, and a different analytical apparatus would be needed. Persistent oscillation in a stable situation might indicate such curves (pp. 1438–1439).

**Measurement and verification** (pp. 1440–1441).
- Thresholds are behavioral dispositions, hard to measure before behavior occurs. The author compares this to demand and supply schedules in microeconomics, which are rarely observed directly. Economics copes because schedules can be inferred from characteristics and aggregate outcomes, and because the most important thing is the level of change in price and the range over which the equilibrium is stable (p. 1440).
- *Proposed method:* index a threshold by the number of others who adopted before the person did. A full distribution follows from the exact time sequence of adoptions. This is tautological but allows regressing thresholds on background variables, then predicting distributions and outcomes in unexposed villages. Two error sources: thresholds imperfectly measured by adoption order, and low $R^2$ giving wrong predicted distributions. Villages with highly stable equilibria might nevertheless be predicted well (p. 1440).
- After-the-fact distributions could show whether villages' results were impervious to change or sensitive to small differences, with policy implications (p. 1441).
- *Dozier (1977):* 23 Korean villages, month of first family-planning adoption, 1964–73. 18 villages gave regression equations for thresholds. Five villages used the equations to predict threshold distributions and, by forward recursion, outcomes. These were compared with simple regression predictions without a threshold model. When the regression explained less than 50% of threshold variance, predictions were worse than the standard methods. As variance explained "edges over" 50%, accuracy improves dramatically, and many predictions approach 100% accuracy. Caution: some regression variables could not have been measured beforehand and correlate with thresholds in ways that remove true explanatory power (p. 1441).

### Summary (pp. 1441–1442)
Aggregation of thresholds explains collective outcomes. The models are most valuable where outcomes are not intuitively consistent with individual preferences. Such paradoxes may be more frequent than we realize, since we see mainly outcomes and assume the preferences matched them (p. 1441). The models move the "strangeness" of collective behavior from the heads of actors into the dynamics of situations. They hold the most promise where many actors behave contingently and there is little institutional precedent. The author presents them as tools linking micro to macro levels (p. 1442).

## Toy example (ours, not from the text)
Five people, thresholds counted as numbers of others who must already be acting. Let $n(t)$ be the number acting at step $t$, and $n(t+1)=\#\{\text{thresholds}\le n(t)\}$ (the counts version of $r(t+1)=F[r(t)]$). Start at $n(0)=0$.

- **Group A:** thresholds {0,1,2,3,4}. $n(1)=1$ (only the 0). $n(2)=\#\{\le1\}=2$. $n(3)=3$. $n(4)=4$. $n(5)=5$. Then $\#\{\le5\}=5$. Equilibrium: 5.
- **Group B:** replace the 1 by a 2, giving {0,2,2,3,4}. $n(1)=\#\{\le0\}=1$. $n(2)=\#\{\le1\}=1$ (nobody has threshold 1). Then $n$ stays at 1. Equilibrium: 1.

The mean thresholds are 2 (A) and 2.2 (B), nearly the same, but the outcomes are 5 and 1.

## Concepts
- [[threshold-model]] (new) — each actor acts once the share (or number) of others acting reaches a personal threshold; outcome follows from the threshold distribution (p. 1422)
- [[fixed-point-and-stability]] — here the equilibrium $r_e$ solves $F(r)=r$. The author's "stability" is the resistance of the equilibrium to changes in the threshold distribution (pp. 1420, 1428–1429)
- [[cascade]] — "bandwagon" or "domino" chain in which each adopter activates the next threshold (p. 1424)
- [[bifurcation]] — author notes a discontinuous jump of $r_e$ at $\sigma_c\approx12.2$. He does not use the term (p. 1427)
- [[micromotives-vs-macrobehavior]] — collective outcomes can be intuitively inconsistent with individual intentions. The paper cites Schelling as the source of thresholds but does not use this phrase (pp. 1421, 1422)
- [[heterogeneity-of-thresholds]] (new) — the exact distribution of individual differences, not just the average, is stressed as what matters for outcomes (pp. 1420–1421, 1428)
- [[sampling-variability-of-crowds]] (new) — crowds as random samples from a fixed distribution can yield very different equilibria (p. 1431)
- [[social-structure-weights]] (new) — friends' actions counted with extra weight in the perceived proportion (p. 1429)
- [[pluralistic-ignorance]] (new) — people who have already acted keep it private, so others whose thresholds have in fact been passed do not know this and do not act (p. 1438)
- [[simple-vs-complex-contagion]] — author says "contagion" seems inappropriate for threshold models, since much more than imitation of the last person is involved (pp. 1422–1423, fn. 2)

## Canonical instances
- [[uniform-threshold-riot]] — thresholds 0..99 give 100 rioters. The perturbed version gives 1 (pp. 1424–1425)
- [[normal-threshold-jump]] — mean 25 normal thresholds, equilibrium jumps near $\sigma\approx12.2$ (p. 1427)
- [[spilerman-riot-sampling]] — repeated incidents with equal riot probability could explain the size correlation, $(.90)^{10}=.35$ (p. 1432)
- [[matza-delinquent-boys]] — status pressure produces bandwagon against held norms (p. 1435)
- [[dozier-korean-villages]] — thresholds inferred from adoption timing, prediction test (p. 1441)
- [[weber-umbrella]] — test case for when behavior is not contingent on others (p. 1437)

## Bridges (candidates)
- [structural-analogy] threshold-model equilibrium $F(r)=r$ ↔ complex-systems: fixed point of a one-dimensional map — the same iteration on the c.d.f.; author does not frame it as dynamics theory.
- [structural-analogy] jump at $\sigma_c$ ↔ saddle-node (fold) bifurcation — two intersections merging into a tangent point and vanishing.
- [structural-analogy] Granovetter's riot thresholds ↔ Schelling's segregation tipping — the paper says the thresholds idea is adapted from Schelling (p. 1422).
- [metaphor] pluralistic ignorance ↔ hidden information in network adoption — hidden actions block cascades.

## Questions this raises
- How does equilibrium change if the path of $r(t)$ can oscillate once individuals can "remove" themselves (net-benefit curves crossing zero twice)?
- Why are social-structure effects largest at about one-quarter acquaintance density? The author says this needs further study (p. 1430).
- How could one measure thresholds before the behavior happens, rather than inferring them from adoption order?
- When is an unstable high equilibrium (such as 100) likely to be observed at all, given sampling variability?

## Reading notes
- Page offset: printed = pdf + 1419.
- OCR problems: in the text layer, $\sigma$ appears as "o-" or "a-"; $\sigma_c$ is "u." or "o-". I read $\sigma$ from context, and the text states the value 12.2. Figure 2 (pdf 9) is garbled in the text layer and I had no page image for it. Axis labels are as given in the text.
- Misprint: "Bernouilli" for Bernoulli is printed that way (image, p. 1431). "onlv", "douglas Danforth" in footnote 6, and "?" for the copyright symbol appear in the text layer and are probably OCR artefacts.
- Footnotes 4–6 assign contributions: Winship (fig. 1), Phillips (normal distribution), Danforth (social-structure results and simulations).
- The author calls the .14 figure "the product of the two probabilities": P(exactly one zero percenter) times (.99)^100 for no one-percenters, as printed. The text does not discuss dependence between the draws, and I report it as given.
- Figures 1 and 3 are garbled in the text layer. The fig. 1 procedure and the 38% threshold of fig. 3 are taken from the running text and captions (pp. 1426, 1438–1439).
- The paper contains no exercises, so that section is omitted.
