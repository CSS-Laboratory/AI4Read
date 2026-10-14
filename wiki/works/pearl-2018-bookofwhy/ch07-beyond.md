---
id: pearl-2018-bookofwhy/ch07-beyond
work: pearl-2018-bookofwhy
unit: "Chapter 7 — Beyond Adjustment: The Conquest of Mount Intervention"
pages: pdf 203–235 (no printed page numbers visible)
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Beyond Adjustment: The Conquest of Mount Intervention

## L0 — One line
When a confounder cannot be measured, causal effects can sometimes still be computed from observational data, using the front-door formula, instrumental variables, or the general do-calculus.

## L1 — The gist (≤ 120 words)
Back-door adjustment needs data on enough variables to block every back-door path. This chapter asks what to do when that is impossible. Pearl shows three further routes: front-door adjustment (a shielded mediator), instrumental variables (e.g. Snow's water companies, a randomized assignment, a gene), and the do-calculus. The do-calculus is a three-rule system for rewriting "do" expressions into "see" expressions. It is complete: if the rules cannot remove the do, no observational answer exists for that causal model. The assumptions that make each route valid are causal, and they come from the diagram, not from the data.

**Prerequisites:** do-operator vs. conditioning; back-door criterion and paths; colliders; linear regression slope and correlation; Ladder of Causation (rung 1 seeing, rung 2 doing).

## L2 — Key ideas
- Back-door adjustment averages stratum-specific effects, weighted by prevalence. Numerical variables and many covariates cause the "curse of dimensionality" (many empty strata). (pdf 204–205)
- In a linear model, a partial regression coefficient performs back-door adjustment automatically. It is causal only if the diagram is plausible and Z satisfies the back-door criterion. (pdf 205–206)
- Front-door adjustment (Eq. 7.1) removes an unmeasured confounder of X and Y when a mediator M carries X's whole effect and is shielded from the confounder. Glynn and Kashin's JTPA study suggests it can give reasonably good estimates even when the shield is only weakly violated (weak C→M). (pdf 207–213)
- The do-calculus has three rules (insert/delete observations, swap action and observation, insert/delete actions). The front-door formula follows from them in seven lines. (pdf 215–217)
- The rules are complete: if the do cannot be eliminated with them, no estimate exists from that data and model. They verify proofs well but do not tell you where to search. Shpitser's algorithm decides in polynomial time whether an elimination exists. (pdf 218–219)
- The do-calculus also handles surrogate experiments, transportability, the "napkin" puzzle of Fig. 7.5, and time-varying treatments (Wermuth–Cox). (pdf 219–221)
- An instrumental variable Z gives b = r_ZY / r_ZX in linear models. Snow's cholera study and Philip Wright's flaxseed study are examples. (pdf 226–229)
- With binary variables and noncompliance, monotonicity can often replace linearity. The result is bounds (39%–78% in the cholestyramine trial), not a point estimate. Mendelian randomization uses genes as instruments. (pdf 230–234)

## L3 — Walkthrough

### Chapter opening (pdf 203)
This chapter climbs the second rung of the Ladder of Causation, intervention: predicting the effects of actions not yet tried. Confounding was the main obstacle to telling "seeing" from "doing". Having removed it with path blocking and the back-door criterion, Pearl maps "routes": back-door adjustment, front-door adjustment, instrumental variables, and a "universal mapping tool", the do-calculus (pdf 203).

### The simplest route: the back-door adjustment formula (pdf 204–207)
**The procedure.** If you have data on a set of deconfounders (variables whose adjustment blocks all back-door paths from the treatment to the outcome), estimate the effect in each stratum (level) of the deconfounder. Then average, weighting each stratum by its share of the population. Example: for gender with a two-thirds male / one-third female population, weight 2/3 and 1/3 (pdf 204). The back-door criterion guarantees that the causal effect within each stratum equals the observed trend in that stratum. Without it, nothing guarantees that the adjustment is legitimate (pdf 204).

**Curse of dimensionality.** Numerical variables (income, height) have too many values for a table. Binning is arbitrary. With more than a handful of adjusted variables the number of categories grows exponentially, and many strata have no samples at all. Most remedies fit a smooth function and extrapolate into the empty strata (pdf 204–205).

**Linear case.** In Wright's path-diagram setting every causal effect is a single number, and adjustment is simple (pdf 205).
- With one treatment X and one outcome Y, the regression line is $Y = aX + b$. Here $a$ ($r_{YX}$) is the average observed trend. If nothing confounds X and Y, it estimates the effect of raising X by one unit (pdf 205).
- With a confounder Z, $r_{YX}$ is only the observed trend. Wright's guinea-pig example: the apparent 5.66-gram benefit of an extra gestation day was biased by litter size (pdf 205).
- Fit a regression plane instead: $Y = aX + bZ + c$. The coefficient $a$ is the partial regression coefficient $r_{YX.Z}$, the regression of Y on X already adjusted for Z. The author credits Pearson and Yule, not Galton, with realizing this (pdf 205).
- "Nature already does all the averaging for us" (pdf 206). If Z is the only confounder, $a$ is the average causal effect. If a set Z satisfies the back-door condition, the coefficient of X is the average causal effect of X on Y (pdf 206).

**Warning.** Regression coefficients, adjusted or not, are only statistical trends. $r_{YX.Z}$ is causal and $r_{YX}$ is not "exclusively" because the diagram shows Z as a confounder (pdf 206). Two ingredients are needed: a plausible path diagram and an adjustment set that satisfies the back-door criterion (pdf 206). Pearl says Wright could have obtained path coefficients from partial correlations, had he known the adjusting set can be read off the diagram (pdf 206). Regression adjustment works only for linear models and loses interactions (the effect of X depending on Z). The back-door formula needs no assumption about the functions behind the arrows, but then other extrapolation methods are needed for high dimensions (pdf 206–207).

**Summary image.** The back-door criterion says which variables to use; the adjustment formula does the deconfounding, like two sides of a coin (pdf 207). Adjustment fails if a back-door path cannot be blocked for lack of data (pdf 207).

*Intuition note.* Adjusting means comparing like with like inside each group, then averaging. In a linear model the fitted plane does that comparison automatically. The data cannot tell you that Z is a confounder rather than something else; the diagram does.

### The front-door criterion (pdf 207–213)
**Setup (Fig. 7.1).** The hypothetical diagram has Smoking Gene → Smoking, Smoking Gene → Cancer, and Smoking → Tar → Cancer. Two assumptions are supposed valid (pdf 208):
1. The gene does not affect tar (no arrow; random factors unrelated to the gene are allowed).
2. Smoking affects Cancer only through tar: no direct arrow, no other indirect pathways.

The gene is unmeasured, so the back-door path Smoking ← Gene → Cancer cannot be blocked (pdf 208).

**Idea: go in the front door** (pdf 208–209).
1. *Smoking → Tar.* The path Smoking ← Gene → Cancer ← Tar is already blocked by the collider at Cancer. So $P(\text{tar}\mid\text{smoking})$ minus $P(\text{tar}\mid\text{no smoking})$ is the average causal effect of smoking on tar (pdf 208).
2. *Tar → Cancer.* The back-door path Tar ← Smoking ← Gene → Cancer is blocked by adjusting for Smoking. The back-door formula gives $P(\text{cancer}\mid do(\text{tar}))$ and $P(\text{cancer}\mid do(\text{no tar}))$ (pdf 208).
3. *Combine.* Cancer arises with or without tar. Under $do(\text{smoking})$ the two states have probabilities $P(\text{tar}\mid do(\text{smoking}))$ and $P(\text{no tar}\mid do(\text{smoking}))$ (see Reading notes). Their cancer likelihoods are $P(\text{cancer}\mid do(\text{tar}))$ and $P(\text{cancer}\mid do(\text{no tar}))$. Weight the two by these probabilities. Repeat for $do(\text{no smoking})$ and take the difference (pdf 209).

**Formula** (X = Smoking, Y = Cancer, Z = Tar, U = Gene, absent from the formula) (pdf 209):
$$P(Y\mid do(X)) = \sum_z P(Z=z\mid X)\sum_{x'} P(Y\mid X=x', Z=z)\,P(X=x') \tag{7.1}$$
Compare the back-door formula (pdf 209):
$$P(Y\mid do(X)) = \sum_z P(Y\mid X, Z=z)\,P(Z=z) \tag{7.2}$$
(The source writes the inner sum's dummy variable as $x$; I write $x'$ to avoid clashing with $X$. See Reading notes for $P(Z=z\mid X)$.)

The front-door adjustment adjusts for two variables (Smoking and Tar) on the front-door path. U does not appear, so the confounder is eliminated without data on it. Equations 7.1 and 7.2 are estimands: recipes for answering the query on the left. They contain only "sees" (vertical bars), no "do"s, so they can be estimated from data (pdf 209–210). The result holds provided the assumptions hold (pdf 209).

*Intuition note.* Split the long path into two short links, each of which can be measured without the hidden confounder. Then chain the links together by weighting. The hidden gene never enters because each link is protected: by a collider for the first, by adjusting for Smoking for the second.

**Objections (Freedman) and reply (Pearl)** (pdf 210).
- **Freedman:** (1) a smoking gene might also affect how the lungs clear foreign matter, which means an arrow from Gene to Tar, and then the front-door formula is invalid; (2) smoking may harm via other mechanisms, e.g. chronic inflammation; (3) tar in living lungs cannot be measured accurately enough.
- **Pearl:** no quarrel in this example; he defers to experts. The point is that diagrams make assumptions transparent for debate. The example shows that, in the right situation, mathematics can remove a confounder's effect without data on it (pdf 210–211).

**General recognition rule (Fig. 7.2).** If the effect of X on Y is confounded by a set C and mediated by a set M, and M is shielded from C, then X's effect can be estimated from observational data. Pearl advises looking for shielded mediators when confounders are incurable (pdf 211).

**Empirical test: JTPA study** (Glynn and Kashin, 2014) (pdf 211–213).
- JTPA (1987–1989) included both an RCT and an observational study of a job-training program, with earnings over eighteen months (pdf 211).
- Pearl's diagram (Fig. 7.3; the authors drew none): Motivation → Signed Up, Motivation → Showed Up, Motivation → Earnings; Signed Up → Showed Up → Earnings. There is no direct arrow Signed Up → Earnings (pdf 211–212).
- The front-door criterion would apply if the arrow Motivation → Showed Up were absent, as would be justified if services were by appointment and missed only by chance events. In the real study that is hard to argue, so Glynn and Kashin used the method anyway, as a sensitivity test. If the middle arrow is weak, the bias from treating it as absent may be small (pdf 212).
- They derived inequalities on the direction and size of the bias and compared against the RCT. Back-door estimates (controlling Age, Race, Site) were off by hundreds or thousands of dollars, as expected with an unobserved confounder like Motivation. Front-door estimates removed almost all of the Motivation effect. For males they were within experimental error, with a small positive bias as predicted. For females they matched almost perfectly (pdf 212).
- Pearl's conclusion: as long as the effect of C on M is weak, front-door adjustment can give a reasonably good estimate, much better than not controlling for C. He says he would not be surprised if it became a serious competitor to RCTs (pdf 213).

### The do-calculus, or mind over matter (pdf 213–221)
**The question.** Both adjustments aim to turn $P(Y\mid do(X))$ into do-free terms like $P(Y\mid X,A,B,Z,\dots)$. Can we decide in advance whether a causal model allows this? If not, the model's assumptions are insufficient and an interventional experiment is unavoidable (pdf 213).

**Analogy with Euclid.** Axioms (self-evident truths) plus mechanical symbol manipulation license auxiliary constructions, which yield theorems such as the 180° angle sum of a triangle. Likewise, start from the target $P(Y\mid do(X))$ and apply meaning-preserving rewrites licensed by axioms and the model, until no do remains. Meaning-preserving means only the format changes, like $y = ax+b$ becoming $ax = y-b$ (pdf 214–215).

**The three rules** (pdf 215–216):
- **Rule 1** (insert/delete observations). Irrelevant observations can be dropped:
$$P(Y\mid do(X), Z, W) = P(Y\mid do(X), Z)$$
This holds provided Z blocks all paths from W to Y after deleting all arrows leading into X. Example: in Fire → Smoke → Alarm, with W = Fire, Z = Smoke, Y = Alarm (no X), Smoke blocks the path (pdf 215).
- **Rule 2** (swap action and observation). If Z satisfies the back-door criterion:
$$P(Y\mid do(X), Z) = P(Y\mid X, Z)$$
In the simplest cases this is Reichenbach's common-cause principle, amended so colliders are not mistaken for confounders (pdf 215).
- **Rule 3** (insert/delete actions). If there is no path from X to Y with only forward-directed arrows:
$$P(Y\mid do(X)) = P(Y)$$
Doing something that does not affect Y leaves Y's distribution unchanged. Auxiliary variables are omitted from Rule 3 for simplicity (pdf 216).

The rules can be proven from the arrow-deleting definition of do and basic probability. Rules 1 and 2 may carry context variables Z. The conditions of each permit must be checked in the causal diagram (pdf 216).

**Derivation of the front-door formula (Fig. 7.4)** (S = smoking, T = tar, C = cancer, s' a dummy summation index) (pdf 217, figure). Pearl says one need not follow every step.

| Step | Expression | Licence |
|---|---|---|
| 1 | $P(c\mid do(s)) = \sum_t P(c\mid do(s),t)\,P(t\mid do(s))$ | probability axioms |
| 2 | $= \sum_t P(c\mid do(s),do(t))\,P(t\mid do(s))$ | Rule 2 |
| 3 | $= \sum_t P(c\mid do(s),do(t))\,P(t\mid s)$ | Rule 2 |
| 4 | $= \sum_t P(c\mid do(t))\,P(t\mid s)$ | Rule 3 |
| 5 | $= \sum_{s'}\sum_t P(c\mid do(t),s')\,P(s'\mid do(t))\,P(t\mid s)$ | probability axioms |
| 6 | $= \sum_{s'}\sum_t P(c\mid t,s')\,P(s'\mid do(t))\,P(t\mid s)$ | Rule 2 |
| 7 | $= \sum_{s'}\sum_t P(c\mid t,s')\,P(s')\,P(t\mid s)$ | Rule 3 |

Step 7 is the estimand (Eq. 7.1). Each licence is read from the diagram or a subdiagram with arrows erased.

*Intuition note.* Each rule says when a do can be traded for a see, or dropped, because the diagram shows no causal route that would make the two differ. Chaining legal trades is a proof. If the chain ends without a do, the effect is computable from observation.

**Anecdotes** (pdf 216–217). Pearl presented the front-door derivation as a $100-prize challenge at a Berkeley seminar in 1993. Paul Holland reportedly gave a long solution in 1995. Heckman and Pinto proved it in 2015 using "standard tools" at the cost of eight pages. Pearl wrote the proof on a napkin for David Freedman. Freedman lost it, which led to Jamie Robins's visit to Pearl and, Pearl believes, to Robins's acceptance of causal diagrams.

**Completeness** (pdf 218). Pearl proposed the rules in 1994 and conjectured that whenever a causal effect is estimable from data, these rules suffice to eliminate the do. In logic this property is "completeness": the axioms derive every true statement of the language. Some good systems are incomplete (Dawid's axioms for conditional independence). Huang and Valtorta, and (independently) Shpitser, proved completeness. Both teams won best student paper at UAI 2006. Consequence: if the three rules cannot produce an estimate from the model, none exists, and there is no alternative to an interventional experiment such as an RCT. The result also indicates what extra assumptions or experiments might help (pdf 218).

**Verifier, not searcher** (pdf 218–219). The calculus checks a proof but does not say which transformation to try next (like choosing a geometry construction). This is the "decision problem" (cf. tiling a square with dominoes: hard to decide, easy to verify). Shpitser, building on Jin Tian's work, found an algorithm that decides in polynomial time whether a solution exists (pdf 219).

**Why the do-calculus is still needed** (pdf 219–221):
1. *Surrogate experiments.* If the model does not allow $P(Y\mid do(X))$ to be estimated from observations alone, and perhaps X cannot be randomized, can we randomize another variable Z (e.g. diet instead of cholesterol)? This asks whether $P(Y\mid do(X))$ can be written with a do on Z but not X. Shpitser's algorithm does not cover this. A complete algorithm by Bareinboim (2012) does (pdf 219).
2. *Transportability.* Bareinboim and Pearl (2015, NAS paper) solved this problem, provided assumptions about both environments are expressed in a causal diagram. The rules then give a systematic method to decide whether effects found in the study environment help estimate effects in the target environment (pdf 219–220).
3. *Transparency (Fig. 7.5).* Bareinboim's puzzle has observed X, Y, Z, W and unobserved U₁, U₂. The effect of X on Y has no blockable back-door path and no front-door condition. Pearl could not solve it by intuition, but "Try the do-calculus" made every step clear. It is the simplest known model needing more than front- or back-door adjustment (pdf 220).
4. *Sequential treatments (Wermuth and Cox, Fig. 7.6).* Treatment 1 (X) is randomized. Treatment 2 (Z) is given in response to the intermediate outcome (W), which depends on X. U is unobserved health status. The target is $P(Y\mid do(X), do(Z))$, with data $P(Y\mid do(X), Z, W)$ and $P(W\mid do(X))$, where Z follows W by an unknown protocol. Wermuth and Cox called it "indirect confounding" and used linear approximations, not solvable by standard regression. Pearl and Robins had earlier derived a general sequential back-door formula. Pearl says one application of the three rules solves it in three lines (pdf 220–221).

### The tapestry of science (pdf 222–224)
Pearl credits many hands over twenty years:
- Thomas Verma proved d-separation (path blocking gives the independencies). His legacy is visible in Rule 1 (pdf 222).
- Dan Geiger proved that no other independencies follow from a diagram (pdf 222).
- Jin Tian (2001) gave a graphical criterion generalizing front-door and back-door; his c-decomposition enabled Shpitser's complete algorithm (pdf 222–223).
- Shpitser proved completeness, despite Pearl's discouragement (pdf 223).
- Peter Spirtes: interventions as deleting arrows. Strotz and Wold (1960) had essentially the same idea for structural equations, deleting an equation. Haavelmo (1943) advocated equation modification (pdf 223).
- Pearl says Spirtes's translation into diagrams led first to the back-door criterion and then to the do-calculus, and new results continue (counterfactuals, generalizability, missing data, machine learning) (pdf 224).

### The curious case(s) of Dr. Snow (pdf 224–228)
**Context.** In the 1853–54 cholera epidemic, the "miasma" theory held that bad air caused cholera. Snow suspected a pathogen entering through the gut but could not see it (pdf 224).

**Hollywood chapter.** The Broad Street pump handle was removed on September 8. According to Pearl this "hardly made a dent" in an epidemic that killed nearly 3,000 (pdf 225).

**Non-Hollywood chapter.** Southwark and Vauxhall drew water downstream of London's sewers. Lambeth had moved its intake upstream. Districts served by Southwark and Vauxhall had a death rate eight times higher (pdf 225). A miasma defender could still claim that miasma was strongest there (Fig. 7.7: Miasma/Poverty → Water Purity and → Cholera; Water Purity → Cholera). Confounders are unobserved, so back-door adjustment is impossible (pdf 225).

**Snow's idea.** In districts served by both companies, households receiving Southwark water still died more, though pipes of both ran down the same streets and the households did not differ in condition or occupation (pdf 225–226). Snow called this a ready-made experiment on about 300,000 people divided into two groups "without their choice" (pdf 226).

**Instrumental variable.** Fig. 7.8 adds Water Company → Water Purity. Snow's detective work showed (1) no arrow between Miasma and Water Company, (2) an arrow from Water Company to Water Purity. A third assumption, left unstated by Snow, is (3) no direct arrow from Water Company to Cholera. A variable with these three properties is an instrumental variable. Water Company and Cholera are unconfounded, so their association is causal. The effect of Water Company runs through Water Purity, so the Purity–Cholera association is causal too. Snow concluded that over 1,000 lives would have been saved had the intake moved upstream. His pamphlet sold 56 copies (pdf 226–227).

**The linear computation (Fig. 7.9).** Z = instrument, X = treatment, Y = outcome, U = unobserved confounder of X and Y. Path coefficients: $a$ on Z→X, $b$ on X→Y, $c$ on U→X, $d$ on U→Y. Linear functions and numerical variables are assumed (pdf 227).
- Z and X are unconfounded, so $a = r_{ZX}$ (the regression slope between them) (pdf 227–228).
- Z and Y are unconfounded: the path Z → X ← U → Y is blocked by the collider at X. So $ab = r_{ZY}$ (pdf 227–228).
- Dividing:
$$b = \frac{r_{ZY}}{r_{ZX}}$$
(pdf 228). This finds X's effect on Y without data on U. Rung-one information (correlations) yields rung-two information (b), because of the causal assumption of no arrow between U and Z. If Z were instead a confounder of X and Y, the formula would fail, and the two models cannot be told apart by any statistical method, however big the data (pdf 228).

*Intuition note.* Z moves X "from outside", unrelated to U. How much Y moves per unit of Z, divided by how much X moves per unit of Z, is how much Y moves per unit of X. U cannot distort this ratio because it is unrelated to Z.

**Philip Wright** (pdf 228–229). Snow used an instrument implicitly, and Sewall Wright could derive the formula from path coefficients. Pearl says it seems that the first other person to use instruments deliberately was Sewall's father Philip, an economist. Philip Wright's 1928 monograph on the elasticity of supply of flaxseed oil used a path diagram in an appendix (Fig. 7.10), while also checking by traditional methods. Yield per Acre is the instrument: it directly affects supply but has no correlation to demand. Pearl's view (not a settled fact): Philip borrowed path coefficients from his son, who invented the recipe of going from regression to causal coefficients. He also reports that stylometric analysis shows Philip wrote the appendix (pdf 229).

### Good and bad cholesterol (pdf 229–234)
**Noncompliance in an RCT.** The cholestyramine trial (Coronary Primary Prevention Trial, 1973–1984) showed a 12.6% cholesterol reduction in men given the drug and a 19% reduction in heart-attack risk (pdf 230). Noncompliance (assigned patients not taking the drug) lowers apparent effectiveness. It also brings confounding if noncompliers differ from compliers, e.g. sicker (pdf 230). Fig. 7.11: Assigned (Z) → Received (X) → Cholesterol (Y), with an unobserved Confounder U → X and → Y. Variables are binary, so the linear IV formula does not apply. Linearity can often be replaced by the weaker monotonicity (pdf 230).

**Three IV questions** (pdf 231): Is Z independent of the confounder? Yes, by randomization. Is there a direct path Z → Y? No, by common sense. Is Z strongly associated with X? Yes, by the data. These answers use causal intuition that the diagram preserves.

**Table 7.1** (pdf 231; proportions):

| Outcome | Z = 0 | Z = 1 |
|---|---|---|
| X=0, Y=0 | 0.919 | 0.315 |
| X=1, Y=0 | 0.000 | 0.139 |
| X=0, Y=1 | 0.081 | 0.073 |
| X=1, Y=1 | 0.000 | 0.473 |

The zeros (nobody with Z = 0 and X = 1) express **monotonicity**: no one takes the drug without being assigned it (pdf 231).

**Bounds** (pdf 231–232):
- *Worst case* (no noncomplier would have improved): compliers who improved are 47.3%. Subtract the placebo effect (8.1% improved among those on placebo): 47.3 − 8.1 = 39.2%.
- *Best case* (all noncompliers would have improved): add the noncompliers' 31.5% + 7.3% to 39.2%, giving 78.0%.
- Even in the worst case the drug helps about 39% of the population. The bounds are wide because of many noncompliers, but the drug is "categorically" effective for its purpose.
- Point estimates are sometimes possible. For the complying subpopulation (those who take X if and only if assigned), a point estimate known as the Local Average Treatment Effect (LATE) can be derived (pdf 232).

**Mendelian randomization** (pdf 232–234). Observational studies (Framingham, late 1970s) suggested HDL ("good" cholesterol) protects against heart attacks. But high HDL often goes with low LDL. Suppose a gene raises HDL without affecting LDL. Fig. 7.12: HDL Gene → HDL Levels → Heart Attack, with Lifestyle confounding the last two (pdf 232). A gene is a randomized instrument, assigned at conception, so no arrows point into it. An arrow HDL Gene → Lifestyle would need people to know their version, and until 2008 no such genes were known, so the arrow is highly likely absent (pdf 233).

Results (pdf 233):
- A 2012 collaborative study (Kathiresan): no observable benefit from higher HDL. LDL has a very large effect: lowering LDL by 34 mg/dl would cut heart-attack chances by about 50%.
- Caveat from a second 2012 study: the gene variant lowers LDL for a whole lifetime, but statins only from the day treatment starts. Mendelian randomization therefore very likely overestimates the true benefits of statins (the source's example is a sixty-year-old), though starting to reduce cholesterol young will have big effects later.
- Lesson: ask whether the variable you actually manipulate (lifetime LDL) is the one you think you manipulate (current LDL) (pdf 233–234).

**Comparing tools** (pdf 234). IV methods yield inequalities where the do-calculus, which insists on point estimates, gives up (as in Fig. 7.12). But the do-calculus is more flexible: it assumes nothing about the functions. If linearity or monotonicity is justified, IV is worth considering. Carlos Brito showed how a noninstrumental variable can become instrumental after conditioning on auxiliary variables that block paths to the confounder, and studied sets of variables serving as instruments (pdf 234).

## Toy example (ours, not from the text)
Linear model: $Z$ and $U$ are independent with variance 1 and mean 0. $X = 2Z + U$ and $Y = 3X + 4U$. So $a=2$, $c=1$, $b=3$, $d=4$ in the notation of Fig. 7.9. The true causal effect of X on Y is $b=3$.

Compute the covariances.
- $\mathrm{Var}(X) = 4\cdot 1 + 1\cdot 1 = 5$.
- $\mathrm{Cov}(Z,X) = 2\cdot\mathrm{Var}(Z) = 2$.
- $Y = 3(2Z+U)+4U = 6Z + 7U$, so $\mathrm{Cov}(Z,Y) = 6$.
- $\mathrm{Cov}(X,Y) = \mathrm{Cov}(2Z+U,\ 6Z+7U) = 12 + 7 = 19$.

Naive regression slope of Y on X: $19/5 = 3.8$, which is wrong because U confounds. Instrument slopes (Z has variance 1): Y on Z is 6/1 = 6; X on Z is 2/1 = 2. Ratio: $6/2 = 3 = b$. ✔.

U was never measured, yet the instrument recovers $b$. If Z had also affected Y directly (violating the exclusion assumption), the ratio would no longer equal $b$, just as the formula fails when Z confounds X and Y (pdf 228); the absence of a direct arrow Z → Y is the third IV assumption (pdf 226).

## Concepts
- [[back-door-front-door-criterion]] — Back-door: adjust for a set blocking all back-door paths. Front-door: use a shielded mediator when the confounder is unmeasured (pdf 207–209).
- [[do-operator]] — $P(Y\mid do(X))$: distribution under intervention, as opposed to seeing; defined here by deleting arrows into X (pdf 213–216).
- [[ladder-of-causation]] — Eliminating do-expressions moves a query from rung one (seeing) to rung two (doing) (pdf 213, 228).
- [[causal-dag]] — Diagram whose absent arrows encode the assumptions licensing each method (pdf 210, 231).
- [[fork-chain-collider]] — A collider blocks a path (used in the front-door and IV arguments) (pdf 208, 227).
- [[d-separation]] — Rule that path blocking tells which independencies hold; credited to Verma (pdf 222).
- [[do-calculus]] (new) — Three rewrite rules for eliminating do from expressions. Rules 1–3 can be proven from the arrow-deleting definition of do (pdf 216); Pearl proposed them in 1994, and Huang–Valtorta and Shpitser proved them complete (pdf 215–218).
- [[estimand]] (new) — A do-free recipe for answering a causal query (pdf 210).
- [[instrumental-variable]] (new) — Z with no confounder in common with the outcome, an effect on X, and no direct arrow to Y. Gives $b=r_{ZY}/r_{ZX}$ in linear models (pdf 226–228).
- [[mendelian-randomization]] (new) — IV in which a gene serves as the randomized instrument (pdf 232–233).
- [[monotonicity-noncompliance]] (new) — Assumption that nobody with Z = 0 has X = 1. It can often replace linearity for binary IV; the worst/best-case argument then gives bounds (pdf 230–232).
- [[partial-regression-coefficient]] (new) — Coefficient of X in a regression on X and Z. Causal only given the diagram and back-door set (pdf 205–206).
- [[curse-of-dimensionality]] (new) — Strata multiply exponentially with covariates, leaving many empty (pdf 204–205).
- [[completeness-do-calculus]] (new) — Rules 1–3 suffice to eliminate the do whenever the effect is estimable from the data and model (pdf 218).
- [[transportability]] (new) — Judging whether effects from one environment hold in another, using diagrams (pdf 219–220).
- [[local-average-treatment-effect]] (new) — Point estimate for the complying subpopulation (pdf 232).

## Canonical instances
- [[smoking-tar-cancer-front-door]] — Hypothetical front-door example with unmeasured smoking gene (pdf 207–210).
- [[jtpa-front-door]] — Glynn–Kashin test of front-door against an RCT (pdf 211–213).
- [[snow-cholera-iv]] — Water company as an instrument for water purity (pdf 224–228).
- [[wright-flaxseed-iv]] — Philip Wright's yield per acre as an instrument for supply elasticity (pdf 228–229).
- [[cholestyramine-noncompliance]] — Bounds from an RCT with noncompliance (pdf 230–232).
- [[hdl-ldl-mendelian-randomization]] — Genes as instruments for HDL and LDL (pdf 232–234).
- [[wermuth-cox-sequential]] — Time-varying treatment solved with the do-calculus (pdf 220–221).

## Bridges (candidates)
- [structural-analogy] Do-calculus proof as symbol manipulation ↔ Bayesian inference: both turn one kind of probability into another by licensed rewrites (conditioning, Bayes' theorem) — different rules, same "format change" spirit.
- [metaphor] Front-door chaining of $P(t\mid s)$ and $P(c\mid do(t))$ ↔ sequential updating: composing two measured links to get an end-to-end quantity.
- [structural-analogy] Instrument as natural experiment ↔ potential outcomes/assignment mechanism: Z behaves like random assignment to X (Snow's "ready-made" experiment).
- [same-math] Back-door formula (Eq. 7.2) ↔ standardization over covariate strata in potential-outcomes adjustment: a weighted average of stratum-specific conditional probabilities by the covariate distribution.

## Questions this raises
- How can one judge whether an assumed missing arrow (e.g. Motivation → Showed Up) is weak enough? Glynn–Kashin used bounds and an RCT benchmark; what other checks exist?
- Why is the do-calculus a good verifier but a hard searcher, and how does Shpitser's algorithm avoid blind search?
- When the IV bounds are wide (39%–78%), what additional assumptions would narrow them (e.g. LATE)?
- How does the lifetime-versus-current LDL issue show up in other instrument-based studies?

## Reading notes
- No printed page numbers are visible in the page labels or images, so all references use (pdf N). The chapter starts at pdf 203 and runs to pdf 235.
- pdf 209 has no page image. I could only check the text layer there. It prints Eq. 7.1 as $P(Z=z, X)$ with a comma. I read this as $P(Z=z\mid X)$, because the Fig. 7.4 derivation (pdf 217 image) ends in $P(t\mid s)$; the comma is probably a transcription error. The same pdf-209 text layer prints the second weight as $P(\text{no tar}\mid do(\text{no smoking}))$; I gave it as $do(\text{smoking})$, which is what the argument ("If we force a person to smoke") requires. This may be a slip in the source or in the text layer; I could not check an image.
- The author uses $r_{XZ}$ and $r_{ZX}$ interchangeably, and says "regression line of Z on Y" (pdf 227). I read these as the slopes between the instrument and the other variable.
- Figure 7.6's arrows were read from the small image; I did not describe unlabeled arrows in detail.
- pdf 235 holds only a Robert Frost illustration caption ("The Road Not Taken") about counterfactuals; it is not part of the argument.
- The unit contains no exercises, so the Exercises section is omitted.
