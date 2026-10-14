---
id: gelman-2013-bda3/ch09-decision
work: gelman-2013-bda3
unit: "9 Decision analysis"
pages: 237-258
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Decision analysis (BDA3, Chapter 9)

## L0 — One line
Bayesian posterior and predictive distributions become decisions when you compute the expected utility of each option, including the value of information from later data, and pick the best option.

## L1 — The gist (≤ 120 words)
What do you do with inferences after the model is fitted and checked? The chapter first lays out four steps of Bayesian decision analysis: list decisions and outcomes, get p(x|d), define a utility, maximize expected utility. It then gives three cases. (1) A survey-incentive meta-analysis (a combined analysis of many earlier experiments) gives costs and benefits but no final choice. (2) A cancer example shows a test can be worthless because it cannot change the treatment. (3) A hierarchical radon model feeds a full measure-or-remediate analysis, from single homes up to national policy. The chapter ends by contrasting personal and institutional decision analysis.

**Prerequisites:** expected value; Bayes' rule for discrete events; normal and lognormal distributions; hierarchical regression (random effects); posterior simulation.

## L2 — Key ideas (5–10 bullets)
- Bayesian decision analysis has four steps: enumerate decisions and outcomes, get p(x|d), define utility U(x) (a number scoring how good an outcome is), maximize expected utility E(U(x)|d). Decisions have no probability distribution; all probabilities are conditional on d (p. 238).
- Inference enters decisions in two ways: predictions that depend on uncertain parameters, and updating after information gained from an earlier decision (p. 238).
- Coefficients that are not "statistically significant" still matter for a decision, so they cannot simply be set to zero. In the incentives example, interactions are kept for cost estimation (pp. 237, 239, 241).
- In multistage problems, Bayes' rule gives the probability to use at each later decision node. The bronchoscopy test (a diagnostic test for lung cancer) is rejected because radiotherapy is best after either result, and the test also carries a 5% risk of death (pp. 245–246).
- In the radon problem the hierarchical model's predictive distribution plays the role of the homeowner's prior. The author says it is not subjective, because it is determined by national data (p. 248). A measurement updates it by a weighted average of the prior mean and the measurement, with weights equal to precision (1/variance) (p. 251).
- Under the chapter's simplifying assumptions, measuring is the preferred option only for intermediate prior radon levels. With an action level R_action = 4 pCi/L (the radon level, in picocuries per liter, above which remediation pays if the level is known), most homes (68% under those assumptions) should do nothing (pp. 253–254).
- Strategies can be compared in aggregate (lives saved vs. cost). At R_action = 4, the model-based strategy costs $7.3 billion for about 83,000 lives saved; the uncorrected short-term strategy would need about $12 billion for the same (pp. 255–256).
- Under the subjective view of probability, personal decision analysis has an element of circular reasoning, because one can typically reach any desired decision by tuning the inputs. "Institutional" analysis (transparent model, utility and inference) has a role in clarifying how assumptions lead to cost estimates and recommendations (p. 256).

## L3 — Walkthrough

### Chapter introduction (p. 237)
The chapter asks what is done with inferences after modelling. Chapter 8 already argued that a model must extend to the target population (p. 237). Here the question is how inferences feed decisions, typically through predictive distributions (p. 237). Three examples follow: survey incentives (9.2), cancer screening (9.3), radon (9.4) (p. 237).

### 9.1 Bayesian decision theory in different contexts (pp. 237–239)
Many if not most analyses aim at decisions, though the rest of the book leaves this implicit (p. 238).

Bayesian inference is used in two ways (p. 238):
1. To summarize uncertainty about parameters, and so about the predictions entering the decision (Sections 9.2, 9.4).
2. Inside the analysis, to compute conditional distributions given information from an earlier decision. This arises in multistage trees and in the expected value of information (Sections 9.3, 9.4).

Decision analysis is harder than inference because it optimizes over decisions as well as averaging over uncertainty (p. 238). The steps are (p. 238):
1. Enumerate the decisions $d$ and outcomes $x$. Outcomes may be vectors (dollars, lives, response rates). $x$ can include observables $\tilde y$ and unknown parameters.
2. Find the distribution of $x$ for each option: the conditional posterior $p(x\mid d)$. The decision $d$ has no probability distribution, so we cannot speak of $p(d)$ or $p(x)$.
3. Define a utility $U(x)$ mapping outcomes to real numbers. With several attributes it must trade them off, e.g. quality-adjusted life-years.
4. Compute $E(U(x)\mid d)$ and choose the decision with the highest value. In a tree, compute it at each decision point, conditional on all information available then.

Many applications do only steps 1–2 and leave the balancing to decision makers (p. 238). The three case studies go progressively further: 9.2 stops halfway, 9.3 adds conditional probability and value of information, and 9.4 does full utility maximization (pp. 238–239).

*Summarizing inference and model selection (p. 239).* Choosing how to summarize a posterior can itself be a decision problem. Scoring functions (for point predictions) and scoring rules (for probabilistic predictions) are the utilities. Under the logarithmic score used in Chapter 7, the optimal summary is the entire posterior (predictive) distribution (p. 239). Model selection can be a decision too, for example when data-collection costs for less relevant variables may outweigh predictive gains (p. 239).

*Intuition note.* A decision analysis is a posterior predictive calculation with one extra layer: a "score" for each possible outcome, then an average of that score for each option. The new ingredients are the utility and the optimization over decisions; the inputs $p(x\mid d)$ come from the Bayesian inference of earlier chapters.

### 9.2 Using regression predictions: survey incentives (pp. 239–244)

**Setting.** The New York City Social Indicators Survey is a telephone study, run every two years, with response rate below 50% (p. 239). Two steps: a meta-analysis of incentive effects, then costs and benefits for this survey (p. 239). The factors are Value (tens of 1999 dollars), Timing (pre- or postpaid), Form (cash or gift), Mode (face-to-face or telephone) and Burden (high if over one hour with sensitive or difficult questions) (pp. 239–240).

**Data.** There are 39 surveys with embedded experiments, giving 101 conditions $i$ with response rate $y_i$ (p. 240). Differences $z_i=y_i-y_i^0$ are taken against the lowest-valued incentive condition in the same survey (usually no incentive). This gives 62 differences and removes between-survey baseline variation (p. 240). Figure 9.1 shows incentives generally help. Prepaid incentives tend to be smaller in dollar value. Some negative differences are expected from sampling variability (p. 241).

**Why not a classical regression.** Interactions are hard to estimate from sparse data. The 62 differences are clustered in 39 surveys. Sample sizes range from under 100 to over 2000, and weighting proportional to sample size is not appropriate because residuals include model error as well as binomial error (p. 241). The authors need interactions (e.g. timing × value) for cost estimation "even if these are not statistically significant" (p. 241).

**Model** (pp. 241–242). Let $n_i$ be respondents among $N_i$ contacted, and $\pi_i$ the response probability:
$$n_i\sim \mathrm{Bin}(N_i,\pi_i)\tag{9.1}$$
$$\pi_i\sim \mathrm N(X_i\beta+\alpha_{j(i)},\sigma^2)\tag{9.2}$$
$$\alpha_j\sim \mathrm N(0,\tau^2)\tag{9.3}$$
Here $X_i\beta$ is the linear predictor, $\alpha_{j(i)}$ is the random effect of survey $j$ (conditions are nested in surveys), and $\sigma$ is the lack of fit. The linear (untransformed) scale is acceptable because response probabilities are far from 0 and 1. It is also a choice for interpretability; a logistic form would not change conclusions in practice (p. 241). The zero mean in (9.3) loses no generality if $X$ includes a constant (pp. 241–242). Priors: uniform on $\sigma$, $\tau$ and $\beta$. $\sigma$ and $\tau$ are estimated precisely enough that this choice does not matter (p. 242).

**Predictors and findings** (p. 242). There are 36 possible predictors, since Value, Timing and Form are defined only if Incentive = 1. Models were fitted from simple to richer, stopping where data could no longer estimate interactions. The chosen model has:
- Main effects for Mode, Burden and Mode × Burden.
- Incentive (about +3 percentage points on average).
- All two-way interactions of Incentive with other factors.
- Three-way interactions Incentive × Value with Timing and with Burden.

Some findings:
- An extra \$10 raises response by 3–4 points.
- Cash beats non-cash by about 1 point.
- Prepaid beats postpaid by 1–2 points.
- Incentives matter about 5 points more for high-burden surveys.

The within-survey SD $\sigma$ is about 3–4 points. The between-survey SD $\tau$ is about 18 points (p. 242). Residual plots (Figure 9.2) show no apparent problems, though other models could fit equally well (p. 242).

**Costs for the Social Indicators Survey** (p. 243). It is a low-burden phone survey; if incentives are used at all, cash would be used, since it appears more effective than gifts. Prepaid is better per dollar of incentive. But prepaid incentives go to everyone contacted, including non-respondents, and postpaid only to respondents. So the per-dollar comparison does not settle the decision; the comparison has to be made in total dollars (p. 243). The survey had 750 respondents in an "individual survey" and 1500 in a "caregiver survey", which starts with a screening question (p. 243). Method: predict the response-rate increase, work backward to the number of calls needed for the same number of respondents, and net the incentive cost against savings from fewer contacts. The incentive costs its value plus \$1.25 for processing and mailing (p. 243).

*Worked example: \$5 postpaid, caregiver survey* (pp. 243–244):
- Predicted increase 1.5 points: 38.9% → 40.4%.
- Cost: $1500\times\$6.25=\$9375$.
- Households needed: $1500/0.404=3715$, versus 3856 actually contacted.
- Propagating to screening: 3377 fewer calls, saving \$2634.
- Net cost $\$9375-\$2634=\$6741$; per interview $\$6741/1500=\$4.49$ for the 1.5-point gain.

Figure 9.3 repeats this for incentives up to \$20 per respondent. Response gains are only a few points. Prepaid is slightly better for the individual survey and postpaid for the larger caregiver survey. For logistical reasons one form is used for both, and the authors recommend postpaid. Choosing the level is left to the survey operators (p. 244).

**Loose ends** (p. 244). Individual coefficients are highly uncertain, and the choice of interactions is arbitrary; adding more made standard errors larger. The authors blame the flat prior and say that shrinking higher-order interactions with prior information would be better. Letting incentive effects vary across surveys would also be reasonable. The linear model implies undiminishing effects, but extrapolation beyond the data range (prepaid up to \$20, postpaid up to \$60 or \$100) is not intended (p. 244).

*Intuition note.* The decision depends on a combination of coefficients (effect per dollar × amount × who receives it), so every coefficient feeds the answer, including uncertain ones. Dropping an "insignificant" interaction would silently fix it at zero, which is itself a strong claim.

### 9.3 Multistage decision making: medical screening (pp. 245–246)
Multistage problems are trees alternating decision and uncertainty nodes. Bayesian inference updates knowledge at each step (p. 245). The example is simplified from the medical literature (p. 245).

**Single decision point.** A 95-year-old man has an apparently malignant lung tumor. Options: radiotherapy, surgery, no treatment. Assumptions (p. 245):
- 90% chance the tumor is malignant.
- If no cancer: life expectancy 34.8 months.
- If cancer: radiotherapy 16.7 months; surgery has a 35% chance of immediate death and otherwise 20.3 months; no treatment 5.6 months.
- Utility is quality-adjusted life expectancy: expected survival minus one month if he undergoes a treatment.

Results (p. 245):
1. Radiotherapy: $0.9\cdot16.7+0.1\cdot34.8-1=17.5$ months.
2. Surgery: $0.35\cdot0+0.65(0.9\cdot20.3+0.1\cdot34.8-1)=13.5$ months.
3. No treatment: $0.9\cdot5.6+0.1\cdot34.8=8.5$ months.

Radiotherapy is preferred.

**Second decision point: bronchoscopy** (p. 245). The test detects cancer with probability 0.70 if malignant and gives a false positive with probability 0.02 if benign. It kills the patient with probability 5%. First find what he would do after the test, using Bayes' rule:
$$\Pr(\text{cancer}\mid T)=\frac{\Pr(\text{cancer})\,p(T\mid\text{cancer})}{\Pr(\text{cancer})\,p(T\mid\text{cancer})+\Pr(\text{no cancer})\,p(T\mid\text{no cancer})}$$
This replaces the prior 0.9 in the calculations above (p. 245).

- **Positive test** (p. 246): $\Pr(\text{cancer}\mid T^+)=\frac{0.9\cdot0.7}{0.9\cdot0.7+0.1\cdot0.02}=0.997$. Radiotherapy: $0.997\cdot16.7+0.003\cdot34.8-1=15.8$. Surgery: 12.6. No treatment: 5.7. Radiotherapy is best.
- **Negative test** (p. 246): $\Pr(\text{cancer}\mid T^-)=\frac{0.9\cdot0.3}{0.9\cdot0.3+0.1\cdot0.98}=0.734$. Radiotherapy: $0.734\cdot16.7+0.266\cdot34.8-1=20.5$. Surgery: 15.1. No treatment: 13.4. Radiotherapy is best again.

Since the best treatment is the same either way, the test cannot change the decision (p. 246). To complete the analysis (p. 246):
- $\Pr(T^+)=0.9\cdot0.7+0.1\cdot0.02=0.632$, value $0.95\cdot15.8=15.0$.
- $\Pr(T^-)=0.9\cdot0.3+0.1\cdot0.98=0.368$, value $0.95\cdot20.5=19.5$.
- Total: $0.632\cdot15.0+0.368\cdot19.5=16.6$ months, less than the 17.5 months for radiotherapy without the test.

So he should not take bronchoscopy. The authors state that any other test-contingent plan (e.g. radiotherapy if positive, no treatment if negative) would be worse still (p. 246).

*Intuition note.* Information is valuable only if it could change the action. Here both test results lead to radiotherapy, so the test only adds a 5% death risk.

### 9.4 Hierarchical decision analysis for home radon (pp. 246–256)
**General structure** (p. 246): remediate, do nothing, or measure and then decide. The hierarchy (people in households in counties) motivates a hierarchical model for risks (p. 246).

**Background** (p. 247). Radon is a naturally occurring radioactive carcinogen. Figure 9.4 shows the added lifetime lung-cancer risk against exposure for male and female smokers and non-smokers. Home concentrations in the U.S. are approximately lognormal, with geometric mean (GM) 0.67 pCi/L and geometric SD (GSD) 3.1; the median is 0.67 and the mean 1.3. About 84% of houses are under 2 pCi/L and 90% under 3. Between 50,000 and 100,000 homes exceed 20 pCi/L (p. 247).
- **Short-term screening measurement:** 2–7 days, lowest level of the home, \$15–20. It is biased upward for the annual living-area average. After bias correction its GSD is roughly 1.8.
- **Long-term measurement:** 12 months, directly measures the annual living-area average, GSD about 1.2, about \$50. The authors later find it more cost-effective than short-term (p. 247).
- **Remediation** ("sub-slab depressurization"): about \$2000. Studies suggest almost all homes can get below 4 pCi/L, while reductions under 1 are rarely attained with conventional methods (pp. 247–248). Assumption: remediation brings the level to $R_{\rm remed}=2$ pCi/L, and has no effect if the level is already below 2 (p. 248).

**The individual decision problem** (p. 248). Three options: (1) remediate without monitoring (\$2000); (2) do nothing; (3) take a long-term measurement (\$50), then remediate or not. Two challenges: decide whether to remediate if the exposure were known, and whether measuring is worth it given the homeowner's prior. The authors say this prior is not subjective but is determined by a hierarchical analysis of national data (p. 248).

**Decision under certainty** (pp. 248–249). Three equivalent quantities (under a linear no-threshold dose–response):
- $D_d$: dollar value of a $10^{-6}$ reduction in death probability (a "microlife").
- $D_r$: dollar value of a 1 pCi/L reduction for 30 years.
- $R_{\rm action}$: level above which to remediate if the level is known.

For a typical U.S. household $D_r=4800\,D_d$ (p. 248). The action level sets the benefit of remediation equal to its cost:
$$R_{\rm action}=\frac{\$2000}{D_r}+R_{\rm remed}\tag{9.4}$$
The U.S., English, Swedish and Canadian governments recommend $R_{\rm action}=4,5,10,20$ pCi/L. These correspond to $D_r=\$1000,\$670,\$250,\$111$ and $D_d=\$0.21,\$0.14,\$0.05,\$0.02$ (p. 249). Typical $D_d$ in medical risk assessment is \$0.10–0.50. So the U.S. and English levels are at the low end of acceptable spending, and the Swedish and Canadian ones are "relatively cavalier" (p. 249). Households differ:
- Two non-smokers with $D_d=\$0.21$ should spend \$370 per pCi/L, giving $R_{\rm action}=7.4$.
- Two smokers should spend \$1900 per pCi/L, giving $R_{\rm action}=3.1$ (p. 249).

Preferences, beliefs and perceived dollar values also vary. The analysis uses $R_{\rm action}=4$ as an example (p. 249).

**Bayesian inference for county radon levels** (pp. 249–250). Data: long-term measurements from about 5000 houses in 125 randomly selected counties, and short-term measurements from about 80,000 houses sampled from all counties. The task is to use the accurate data to calibrate the biased, imprecise data (pp. 249–250). The model is fitted separately in each of 10 regions. With $y_i$ the log measurement of house $i$ in county $j(i)$ (p. 250):
$$y_i\sim \mathrm N(X_i\beta+\alpha_{j(i)},\sigma_i^2)$$
$$\alpha_j\sim \mathrm N(W_j\gamma+\delta_{k(j)},\tau^2)$$
$$\delta_k\sim \mathrm N(0,\kappa^2),\quad k=1,\dots,K=19$$
- $X_i$ (row vector): basement indicator, basement-is-living-area indicator, and a short-term-measurement indicator that corrects bias.
- $\sigma_i$ takes two values (long- or short-term).
- $W_j$: county predictors, including climate and soil uranium.
- $\delta_k$: effect of geological type $k$.
- $\tau$ and $\kappa$ are estimated from the data.

Individual homes in a given county can be predicted only to within a GSD of about 1.9 at best, and 2.3 typically, versus 3.1 with no information. Even this is enough to find counties where high-radon homes are very common or very rare. In some mid-Atlantic counties more than half of houses exceed 4 pCi/L, in others fewer than 0.5% do (p. 250).

**Inference for a single house** (pp. 250–251). Let $R_i$ be the radon concentration and $\theta_i=\log R_i$. The posterior predictive distribution of $\theta_i$ is approximately normal, because the variance components are well estimated:
$$\theta_i\sim \mathrm N(M_i,S_i^2)\tag{9.5}$$
- $M_i=X_i\hat\beta+\hat\alpha_{j(i)}$, from posterior means (a scalar; $X_i$ is a row vector times a coefficient vector).
- $S_i^2$ includes uncertainty in $\alpha,\beta$ and in $\tau^2,\kappa^2$. It excludes $\sigma^2$, since true levels, not measurements, are predicted.
- $e^{S}$ ranges from 2.1 to 3.0 (mostly 2.1–2.5). Values above 2.5 occur in small-population counties.
- $e^{M}$ ranges from 0.1 to 14.6 pCi/L, with 95% in [0.3, 3.7] and 50% in [0.6, 1.6].

(9.5) serves as the homeowner's "prior". The authors use this term for the predictive distribution that conditions on survey data but precedes any measurement of the house (p. 251). Suppose an unbiased measurement $y\sim\mathrm N(\theta,\sigma^2)$ is taken (short-term values would first be bias-corrected). Then
$$\theta\mid M,y\sim \mathrm N(\Lambda,V)\tag{9.6}$$
$$\Lambda=\frac{\frac{M}{S^2}+\frac{y}{\sigma^2}}{\frac1{S^2}+\frac1{\sigma^2}},\qquad V=\frac{1}{\frac1{S^2}+\frac1{\sigma^2}}\tag{9.7}$$
(p. 251). The normal facts used are: for $z\sim\mathrm N(\mu,s^2)$, $E(e^z)=e^{\mu+s^2/2}$, and a formula for $E(e^z\mid z>a)\Pr(z>a)$ involving $\Phi$ (the standard normal CDF) (p. 251). See Reading notes for a problem with the printed form of the second formula.

*Intuition note.* (9.7) is a weighted average of the prior mean $M$ and the measurement $y$. Each is weighted by its precision (1/variance). A precise long-term measurement ($\sigma=\log 1.2$) pulls the estimate toward $y$ much more than a noisy one would.

**Decision analysis for individual homeowners** (pp. 251–253). The decision to measure uses the prior (9.5). The decision to remediate uses (9.6) if measured, otherwise (9.5) (p. 251). Losses are in dollars over 30 years, with $D_r=\$2000/(R_{\rm action}-R_{\rm remed})$ and $R=e^\theta$ (p. 252).

1. **Remediate without monitoring:**
$$L_1=\$2000+D_rE(\min(R,R_{\rm remed}))=\$2000+D_r\big[R_{\rm remed}\Pr(R\ge R_{\rm remed})+E(R\mid R<R_{\rm remed})\Pr(R<R_{\rm remed})\big]$$
$$=\$2000+D_r\Big[R_{\rm remed}\,\Phi\!\Big(\tfrac{M-\log R_{\rm remed}}{S}\Big)+e^{M+\frac12S^2}\Big(1-\Phi\Big(\tfrac{M+S^2-\log R_{\rm remed}}{S}\Big)\Big)\Big]\tag{9.8}$$
2. **Do nothing:**
$$L_2=D_rE(R)=D_re^{M+\frac12S^2}\tag{9.9}$$
3. **Measure.** The immediate loss is \$50 plus exposure during the measurement year, $\frac1{30}$ of (9.9). The inner decision has two branches:
 - (a) Remediate (as in 1, but with the posterior):
$$L_{3a}=\$50+D_r\tfrac1{30}e^{M+\frac12S^2}+\$2000+D_r\Big[R_{\rm remed}\Phi\Big(\tfrac{\Lambda-\log R_{\rm remed}}{\sqrt V}\Big)+e^{\Lambda+\frac12V}\Big(1-\Phi\Big(\tfrac{\Lambda+V-\log R_{\rm remed}}{\sqrt V}\Big)\Big)\Big]\tag{9.10}$$
 - (b) Do not remediate:
$$L_{3b}=\$50+D_r\tfrac1{30}e^{M+\frac12S^2}+D_re^{\Lambda+\frac12V}\tag{9.11}$$

**Inner decision.** Let $y_0$ be the log-scale measurement above which you remediate. Because of measurement error, $y_0\neq\log R_{\rm action}$. It depends on $M,S,\sigma$ and is found numerically from
$$L_{3a}=L_{3b}\ \text{ at } y=y_0\tag{9.12}$$
(details not given, p. 252).

**Outer decision.** $L_1$ and $L_2$ are direct. For branch 3,
$$L_3=E(\min(L_{3a},L_{3b}))\tag{9.13}$$
is computed by simulation (p. 253):
1. Draw 5000 values of $y\sim\mathrm N(M,S^2+\sigma^2)$.
2. Compute $\min(L_{3a},L_{3b})$ for each, from (9.10) and (9.11).
3. Average the 5000 values.

This is valid only if the optimal decision is made after the measurement. The recommended decision is the one with the lowest of $L_1,L_2,L_3$. A homeowner can specify $R_{\rm action}$, look up $(M,S)$, and read off the answer. Extra information, such as a neighbor's measurement, can be folded into $M$ and $S$ (p. 253).

**Simplified rule.** With $\sigma=\log 1.2$ and $S=\log 2.3$ for all counties, there are thresholds $M_{\rm low}<M_{\rm high}$. Remediate if $M>M_{\rm high}$, do nothing if $M<M_{\rm low}$, measure if $M\in[M_{\rm low},M_{\rm high}]$ (Figure 9.5, p. 253). For $R_{\rm action}=4$ pCi/L (p. 253):
- $e^M<1.0$ pCi/L (68% of U.S. houses): do nothing.
- $e^M$ between 1.0 and 3.5 (27%): take a long-term measurement.
- $e^M>3.5$ (5%): remediate immediately. Short-term monitoring might then be barely cost-effective, but this is ignored.

*Intuition note.* Measuring is preferred only at intermediate prior levels (under the simplified assumptions); a plausible reason (our reading, not an author statement) is that measuring helps when you are unsure which action is right. Very low prior radon makes "do nothing" nearly certain, and very high makes "remediate" nearly certain, so a \$50 test adds little in either case.

**Aggregate consequences** (pp. 254–256). Figure 9.6 maps, by county, the fraction of houses for which measurement is recommended, and the expected fraction for which remediation is then recommended, at $R_{\rm action}=4$. The maps reflect parameter uncertainty and may change with better predictions (p. 254). Even if the EPA level of 4 is accepted, monitoring is not recommended for most homes: only 28% would monitor. At $R_{\rm action}=8$, about 5% would monitor (p. 254).

Four national strategies are compared on cost and lives saved over 30 years, with the same $R_{\rm action}$ for all houses and average U.S. household composition (pp. 254–255):
1. The model-based recommended strategy (measure only homes with high enough prior, remediate if the measurement is high).
2. Long-term measurement of all houses, remediate if the measurement exceeds $R_{\rm action}$.
3. Short-term measurement of all, bias-corrected.
4. Short-term measurement of all, uncorrected.

Only three house types × 3078 counties need to be considered (p. 255). For strategy 1 at $R_{\rm action}=4$ (p. 255):
- About 26% of 70 million ground-contact houses monitor and about 4.5% remediate.
- Remediation covers 2.8 million homes above 4 pCi/L (74% of them) and 840,000 above 8 pCi/L (91% of them).
- Cost: \$7.3 billion (\$1B measurement + \$6.3B remediation).
- Expected lives saved: 49,000 smokers and 35,000 nonsmokers.

Figure 9.7 shows the trade-off. At \$7.3B, strategy 1 saves an expected 83,000 lives and the EPA-style uncorrected short-term strategy saves only 64,000. To save 83,000 lives, the latter would cost about \$12B (pp. 255–256).

### 9.5 Personal vs. institutional decision analysis (p. 256)
- **Authors' view of the subjective approach.** The authors "do not generally find" the subjective view of probability useful (see Sections 1.5–1.7). Used for personal decisions, it has drawbacks. Defining utility and subjective probabilities can be harder than choosing, and one can typically reach any desired decision by tuning the inputs, which is a form of circularity (p. 256).
- **When personal analysis helps.** It is most useful when inputs are well defined, as in the cancer example. There the utility is noncontroversial and the probabilities come from the literature (p. 256).
- **Institutional decision analysis** (term introduced by the authors): transparently setting up a probability model, utility function and inferential framework that lead to cost estimates and recommendations. It can be formalized to different degrees (p. 256).
 - The incentives analysis gives open-ended recommendations. A single one would be too sensitive to the relative utility of dollars and response rate.
 - The cancer analysis gives a direct recommendation and can be taken apart to test each assumption.
 - The radon analysis rests on a cost-benefit assumption ($R_{\rm action}=4$), which allows county-level recommendations. It would be "silly" to believe all households share it, but the maps show what a uniform government recommendation could look like.
- **The "objective" or "institutional" approach:** identify assumptions and data, check fit and reasonableness of predictions (including decision recommendations), and expand the model. The most useful expansions let more information into the inferences (p. 256).

### 9.6 Bibliographic note (p. 257)
The note lists decision-theory texts (Berger; DeGroot; Luce and Raiffa; Savage). It also lists scoring-rule reviews, applied-decision-analysis and medical-decision books, and psychology references. The incentive analysis is from Gelman, Stevens and Chan (2003), with data from Singer et al. (1999). The cancer example is adapted from Moroff and Pauker (1983). The radon problem is described by Lin et al. (1999), with computational details in Boscardin and Gelman (1996) (p. 257).

### 9.7 Exercises (pp. 257–258)
Three exercises, listed under "Exercises worth doing". No solutions are printed.

## Toy example (ours, not from the text)
**Problem.** A machine has a hidden fault with prior probability 0.3. Repairing costs \$100. If you do not repair and the fault exists, you lose \$400. A test costs \$5. It flags a fault with probability 0.9 if there is one and 0.1 if there is none. Should you test?

**No test.**
- Repair: loss 100.
- Do nothing: $0.3\cdot400=120$.
- Best: repair, loss 100.

**Test.**
- $\Pr(T^+)=0.3\cdot0.9+0.7\cdot0.1=0.27+0.07=0.34$; $\Pr(T^-)=0.66$.
- $\Pr(\text{fault}\mid T^+)=0.27/0.34=0.794$. Repair costs 100, doing nothing costs $0.794\cdot400=317.6$. Repair.
- $\Pr(\text{fault}\mid T^-)=0.03/0.66=0.0455$. Repair costs 100, doing nothing costs $0.0455\cdot400=18.2$. Do nothing.
- Expected loss: $5+0.34\cdot100+0.66\cdot18.18=5+34+12=51$.

**Result.** Testing (51) beats not testing (100), because the test changes the action after a negative result. In the chapter's bronchoscopy example, both results lead to the same action. The test then has no value and only adds its own risk (pp. 246, 252–253).

## Concepts
- [[bayesian-decision-analysis]] (new) — four steps: decisions/outcomes, p(x|d), utility, maximize expected utility; d has no probability distribution (p. 238)
- [[expected-utility]] (new) — E(U(x)|d), computed at each decision point given the information then available (p. 238)
- [[value-of-information]] (new) — worth of a test or measurement, found by comparing the expected utility of acting with and without it; pointless if it cannot change the decision (pp. 238, 246)
- [[decision-tree]] (new) — alternating decision and uncertainty nodes; later decisions are worked out first, using conditional probabilities given the information then available (pp. 238, 245)
- [[bayes-theorem]] — used to update Pr(cancer) after a test result (p. 245)
- [[posterior-predictive-distribution]] — the source of decision-relevant predictions, e.g. (9.5) for radon (pp. 238, 250)
- [[prior-distribution]] — here the author uses "prior" for the predictive distribution from a hierarchical model before the house is measured, and says it is not subjective (pp. 248, 251)
- [[hierarchical-model]] — used for incentives (surveys → conditions) and radon (houses → counties → geological types) (pp. 241, 250)
- [[monte-carlo-integration]] — 5000 simulated measurements to estimate $L_3$ (p. 253)
- [[scoring-rule]] (new) — utility for probabilistic predictions; the log score is optimized by reporting the full posterior predictive distribution (p. 239)
- [[action-level]] (new) — $R_{\rm action}=\$2000/D_r+R_{\rm remed}$, the radon level above which remediation pays under certainty (p. 249)
- [[institutional-decision-analysis]] (new) — transparent model, utility and inference leading to cost estimates and recommendations (p. 256)
- [[subjective-probability]] — the authors do not generally find this view useful, and note that decision analysis built on it can be circular (p. 256)

## Canonical instances
- [[survey-incentives-meta-analysis]] — hierarchical regression of 39 experiments used to cost incentives; stops short of choosing a level (pp. 239–244)
- [[lung-tumor-bronchoscopy]] — a test that cannot change the treatment has no value (pp. 245–246)
- [[home-radon-decision]] — hierarchical model plus measure/remediate tree, from single homes to national strategy comparison (pp. 246–256)

## Bridges (candidates)
- [same-math] Normal–normal update (9.7) ↔ hierarchical models: precision-weighted average, as in partial pooling/shrinkage — the same weighted average of a group-level mean and noisy data.
- [structural-analogy] Discrete Bayes update after a test (p. 245) ↔ base-rate neglect: the prior (0.9) and the test's error rates combine by Bayes' theorem.
- [structural-analogy] Predicting outcomes under each candidate incentive (p. 243) ↔ potential outcomes: the decision problem needs outcomes under each option, though only one is ever realized.
- [structural-analogy] Choosing the best of decisions with $p(x\mid d)$ ↔ do-operator: both treat the action as fixed rather than random.
- [structural-analogy] Model selection as a decision with data-collection costs (p. 239) ↔ cross-validation/LOO: both frame model choice by predictive utility.

## Questions this raises
- How sensitive are the radon recommendations to $R_{\rm action}$, the assumed $D_r=4800D_d$, and the assumption that remediation brings every high home to 2 pCi/L?
- Incentive effects were uncertain and the interaction choice arbitrary (p. 244). How would informative priors that shrink higher-order interactions change the cost curves?
- The radon "prior" is not subjective (p. 248). What happens to the decision rule if a homeowner has strong, differing beliefs about the risk?
- How would the bronchoscopy conclusion change if the test's error rates or the treatment values were changed (p. 256 says it can be "taken apart" for this)?

## Exercises worth doing
- Ex. 1 (p. 257) — widgets with normal demand; choose production quantity to maximize expected profit; the basic expected-utility optimization — difficulty: easy
- Ex. 2(a)–(c) (pp. 257–258) — Oscar's dog search over days; Bayesian updating of the dog's location after failed searches — difficulty: medium
- Ex. 2(d) (p. 258) — expected value of knowing which forest the dog is in; value of perfect information — difficulty: medium
- Ex. 3 (p. 258) — recast an earlier book example (bioassay or meta-analysis) as a decision problem with costs, utility and a sensitivity analysis — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 247 = printed 237).
- The text layer replaces "~" with "→", "≠" with "-=", and $10^{-6}$ with "10→6". I read these from the images where available.
- Page images were not supplied for pp. 237–239, 248, 257 and 258 (pdf 247–249, 258, 267–268), which had the text layer only; images were given for pp. 240–247 and 249–256. For those, the "→" and symbol readings rely on the text layer.
- On p. 238 the text layer writes the unknown-parameter symbol as ω. On pp. 250–252 the images show θ for log radon, while the text layer prints ω there. I used θ for the radon sections.
- Printed formula on p. 251 for $E(e^z\mid z>a)\Pr(z>a)$: the image shows $e^{\mu+\frac12s^2}\big(1-\Phi(\frac{\mu+s^2-a}{s})\big)$. By my own check, this expression equals $E(e^z\mid z<a)\Pr(z<a)$. For $z>a$ the factor would be $\Phi\big(\frac{\mu+s^2-a}{s}\big)$. Equation (9.8) is consistent with the "z < a" version, so (9.8) looks right. This is my reading, not an author statement.
- Numerical inconsistencies as printed: the share of homes that monitor is 28% (p. 254), 27% for the middle band in the recommendation list that follows Figure 9.5 (simplified assumptions) (p. 253), and 26% (p. 255). Lives saved at $R_{\rm action}=4$ are given as 49,000 + 35,000 = 84,000 (p. 255) but as "83,000" in the comparison (p. 255).
- The text on p. 242 says dotted lines for postpaid in Figure 9.1, while the caption (p. 240) says dashed.
- The text of 9.2 says "Figure 9.1 on page 240 displays the model fit". Figure 9.1 shows observed data and fitted lines.
- The running header "This electronic edition is for non-commercial purposes only." appears on every page.
