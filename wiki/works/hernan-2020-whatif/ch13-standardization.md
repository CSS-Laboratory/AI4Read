---
id: hernan-2020-whatif/ch13-standardization
work: hernan-2020-whatif
unit: "13 Standardization and the parametric g-formula"
pages: 175-186
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Standardization and the parametric g-formula

## L0 — One line
Standardization with a fitted outcome model (the parametric g-formula) estimates an average causal effect under the same identifiability conditions as IP weighting, but with different modeling assumptions, so comparing the two methods is a useful check.

## L1 — The gist (≤ 120 words)
How can we estimate the average effect of quitting smoking on weight gain when there are too many confounder strata to estimate means nonparametrically? Fit an outcome model for E[Y | A, C=0, L], predict each person's outcome under A=1 and under A=0, and average the predictions over the observed confounders. This gives 5.18 − 1.66 = 3.5 kg, the same as IP weighting to one decimal. The two methods need different correct models (outcome versus treatment), so a small difference is reassuring and a large one is a warning. Doubly robust estimators combine both models. Any estimate is only as credible as exchangeability, positivity, consistency, correct measurement and correct models.

**Prerequisites:** conditional expectation; regression; exchangeability, positivity and consistency (Ch. 3); IP weighting (Ch. 12); Chapter 2 standardization. Terms used below: a stratum is a group of people with the same values of $L$; a consistent estimator converges to the true value in large samples; a plug-in estimator puts fitted estimates into a formula; model misspecification means the assumed model form is wrong; the g-formula is the general method of which standardization is a case (p. 181).

## L2 — Key ideas (5–10 bullets)
- Standardization averages stratum-specific outcome means E[Y|A=a,C=0,L=l] over the distribution of L. Under conditional exchangeability, positivity and consistency, this estimates E[Y^{a,c=0}] (p. 176).
- With high-dimensional L, meaningful nonparametric stratum means cannot be obtained (403 treated, millions of strata), so an outcome regression is used (p. 177).
- We need not estimate Pr[L=l]. The weighted sum equals E[E[Y|A=a,C=0,L]], so we average predictions over the observed individuals (p. 178).
- A four-step recipe does this: expand the dataset (three copies), fit the outcome model, predict, average. It reproduced Chapter 2's answers and gave 3.5 kg for smoking cessation (pp. 178–179).
- IP weighting and standardization are exactly equal only when no models are used. With models, they differ, and the size of the difference signals possible misspecification (pp. 179–180).
- Both methods estimate the g-formula. Standardization is the plug-in estimator, and the parametric g-formula when the plug-in uses parametric models (p. 181).
- Under exchangeability and positivity given $L$, doubly robust estimators are consistent if either the treatment model or the outcome model is correct. Their bias depends on the product of the two models' errors (pp. 182, 184).
- Credibility depends on three groups of conditions: identifiability, correct measurement, correct models. They are untestable, so sensitivity analyses are advised (pp. 182–183).

## L3 — Walkthrough

### 13.1 Standardization as an alternative to IP weighting
- **Setting.** Same NHEFS data as Chapter 12: 1629 smokers aged 25–74 with baseline and ~10-year follow-up visits. 1566 had weight measured at follow-up (uncensored, $C=0$) (p. 175).
- **Target.** $E[Y^{a=1,c=0}] - E[Y^{a=0,c=0}]$: mean weight gain if everybody were treated and uncensored versus untreated and uncensored. The observed associational difference is $E[Y|A=1,C=0]-E[Y|A=0,C=0]=2.5$, expected to differ from the causal one (p. 175).
- **Assumption.** The vector $L$ is sufficient to adjust for confounding and selection bias. It has 9 baseline variables: sex, age, race, education, smoking intensity, smoking duration, daily physical activity, recreational exercise, weight. The components of $L$ needed to adjust for $C$ are assumed unaffected by $A$ (p. 175).
- **IP weighting versus standardization.** IP weighting builds a pseudo-population where $L$ has the same distribution in treated and untreated. It requires modeling the joint distribution of treatment and censoring, $\Pr[A=a,C=0|L]$ (pp. 175–176).
- **Standardization.** Under exchangeability and positivity given $L$, the standardized mean in the uncensored treated is a consistent estimator of $E[Y^{a=1,c=0}]$, and likewise for $a=0$. Technical Point 2.3 gives the proof for the case without censoring. For censoring, replace $A=a$ by $(A=a,C=0)$ (p. 176).
- **Recipe.** First compute the conditional means in each stratum $l$ of $L$. Then take their weighted average, with weights equal to the prevalence $\Pr[L=l]$ (p. 176):
$$\sum_l E[Y|A=a,C=0,L=l]\times \Pr[L=l]$$
- **Continuous covariates.** If some variables in $L$ are continuous, replace $\Pr[L=l]$ by the pdf $f_L[l]$ and the sum becomes an integral (pp. 176–177). The general form is $\int E[Y|A=a,C=0,L=l]\,dF_L(l)$ (margin, p. 177).
- **Effect in the treated.** Replace $\Pr[L=l]$ by $\Pr[L=l|A=1]$ (margin, Technical Point 4.1; p. 176).
- **Fine Point 13.1 (structural positivity).** Positivity is needed for standardization too: if $\Pr[A=a|L=l]=0$ and $\Pr[L=l]\neq0$, then $E[Y|A=a,L=l]$ is undefined (p. 176).
  - A parametric outcome model can smooth over strata with structural zeroes. This extrapolation introduces bias, so nominal 95% intervals cover the truth less than 95% of the time (p. 176).
  - Modeling here is not for lack of data. The quantity cannot be identified even with infinite data, because of structural non-positivity (p. 176).
  - With violations or near-violations of positivity, the standard error is generally smaller for standardization than for IP weighting. That does not mean standardization is preferred, because bias differences may swamp it (p. 176).

*Intuition note.* Standardization asks: "in each kind of person, what is the average outcome with treatment $a$, and what is the average if we mix those kinds in the population's real proportions?" It needs a good outcome estimate for every kind of person, and positivity says every kind of person must be observable under each treatment (unless a model extrapolates).

### 13.2 Estimating the mean outcome via modeling
- Ideally the stratum means would be estimated nonparametrically, as in Section 2.3 with Table 2.2. Here that is "out of the question": only 403 treated individuals are spread over millions of strata. The same holds for the untreated (p. 177).
- **Model used.** A linear regression for mean weight gain with $A$ and all 9 confounders as covariates (p. 177).
  - Linear and quadratic terms for age, weight, smoking intensity and smoking duration. This restricts each continuous covariate's relation to the mean to a parabola (p. 177).
  - One product term between $A$ and smoking intensity. Otherwise each covariate's contribution to the mean does not depend on the others, and the contribution of quitting varies linearly with prior intensity (p. 177).
- This gives $\widehat E[Y|A=a,C=0,L=l]$ for each of the 403 uncensored treated and 1163 uncensored untreated. Example: a male non-quitter with the listed covariates (age 26, 15 cigarettes/day, weight 112 kg, etc.) had predicted mean gain 0.34 kg (p. 177).
- The mean of the estimated weight gain was 2.6 kg, equal to the observed mean. The observed gain ranged from −41.3 to 48.5 kg (p. 177).

### 13.3 Standardizing the mean outcome to the confounder distribution
- With discrete $L$, each conditional mean gets weight $\Pr[L=l]$. These proportions could be counted directly (as in Section 2.3), but that is tedious for high-dimensional $L$ (p. 178).
- **Key simplification.** We do not need to estimate $\Pr[L=l]$. It suffices to estimate $E[Y|A=a,C=0,L=l]$ at each individual's own $l$ and average (p. 178):
$$\frac1n\sum_{i=1}^n \widehat E[Y|A=a,C=0,L_i]$$
  This works because $\sum_l E[Y|A=a,C=0,L=l]\Pr[L=l]=E\big[E[Y|A=a,C=0,L]\big]$ (p. 178).
- **Four steps** (expansion, modeling, prediction, averaging), shown first on Table 2.2: 20 individuals, no censoring, one binary $L$, binary $Y$, so $E[Y|A,L]$ is a risk (p. 178).
  1. **Expansion.** Copy the 20 rows three times (60 rows). Block 1 is the real data. In block 2, set $A=0$ for all and set $Y$ to missing. In block 3, set $A=1$ for all and set $Y$ to missing (p. 178).
  2. **Outcome modeling.** Fit a model for the mean outcome given $A$ and $L$ on all 60 rows, with product term $A\times L$ (saturated). Only block 1 contributes to the fit, since $Y$ is missing elsewhere (p. 178).
  3. **Prediction.** Use the fitted parameters to impute $Y$ in blocks 2 and 3, i.e. the estimated means at each $L$ with $A=0$ (block 2) and $A=1$ (block 3) (p. 179).
  4. **Averaging.** The average of the block-2 predictions is the standardized mean in the untreated; the average of the block-3 predictions is the standardized mean in the treated. Since 60% of rows have $L=1$ and 40% have $L=0$, rows with $L=1$ get more weight (p. 179).
- On Table 2.2 this gives 0.5 for both standardized means, exactly the direct Section 2.3 calculation. Both are completely nonparametric. The empirical distribution of $L$ was used instead of an estimated one (p. 179).
- **Smoking data.** Same procedure with the model of Section 13.2. Average prediction in block 2 (untreated): 1.66. In block 3 (treated): 5.18. Effect estimate $5.18-1.66=3.5$ kg, with 95% CI (2.6, 4.5) from the bootstrap (Technical Point 13.1) (p. 179).

*Intuition note.* The three-block trick is a way to ask the fitted model: "what would each person's outcome be if untreated, and if treated?" Averaging over everyone in the study automatically weights the strata by how common they are.

### Technical Point 13.1: Bootstrapping
- Standard errors often rely on large-sample approximations, which can be too complicated to compute (p. 180).
- **Nonparametric bootstrap.** Draw a sample of 1629 individuals with replacement from the study population (a "bootstrap sample"). Compute the effect estimate with the same method. Repeat for many samples (say 1000). The standard deviation of the estimates consistently estimates the standard error. The 95% CI is the estimate $\pm1.96\times$ this standard error (p. 180).
- When an estimator's limiting distribution is normal, 95% Wald intervals with bootstrap standard errors are calibrated in large samples. For IP-weighted marginal structural models this interval will often be narrower than one based on the robust variance estimator, which is often conservative and wider (p. 180).
- Published work often uses 200–500 samples. This would have given an almost identical interval here, but not always. The "bag of little bootstraps" eases the computing burden (p. 180).

### 13.4 IP weighting or standardization?
- In the example both give almost the same estimate. Technical Point 2.3 proved the standardized mean equals the IP weighted mean (p. 179).
- That equality is exact only when no models are used. With models they are expected to differ (p. 179).
  - IP weighting models $\Pr[A=a,C=0|L]$ (here with logistic models for $\Pr[A=a|L]$ and $\Pr[C=0|A=a,L]$).
  - Standardization models $E[Y|A=a,C=0,L=l]$ (here a linear model) (p. 179).
- Some misspecification is inescapable. Misspecifying the treatment model and misspecifying the outcome model will not generally produce bias of the same size and direction. So the two estimates generally differ (pp. 179–180).
- Large differences alert us to serious misspecification in at least one estimate. Small differences do not guarantee its absence but are reassuring: logically possible, but unlikely that badly misspecified models give bias of similar magnitude and direction in both (p. 180).
- Here both gave 3.5 kg to one decimal. Neither needed a model for $L$ (p. 180).
- **g-formula terminology.** IP weighting and standardization are both estimators of the g-formula, first described in 1986 (p. 181).
  - Standardization is a plug-in g-formula estimator: it replaces the conditional mean outcome by its estimate. When the estimates come from parametric models, it is the *parametric g-formula* (p. 181).
  - For a full distribution, the parametric g-formula needs the conditional distribution of the outcome given $A$ and $L$. Without time-varying confounders it does not need a parametric model for the confounder distribution (p. 181).
  - This book uses "g-formula", not "g-computation", to avoid confusion with g-estimation (Chapter 14) (margin, p. 181).
- **Advice.** When both methods can be used, use both. Where possible, use doubly robust methods. Under exchangeability and positivity given $L$, such an estimator consistently estimates the average causal effect if either the treatment model or the outcome model is correct, without knowing which (p. 181).
- Calculations may be restricted to a subset of the population, for example men and women separately, to study effect modification. Both methods allow this (p. 181).

### Fine Point 13.2: A doubly robust plug-in estimator
- Doubly robust estimators give "two chances to get it right". Here is one (Bang and Robins, 2005) for a dichotomous $A$, without censoring (p. 182):
  1. Estimate the IP weight $W^A=1/f(A|L)$.
  2. Fit a generalized linear outcome model with canonical link for $E[Y|A,L,R]$, adding covariate $R$, where $R=W^A$ if $A=1$ and $R=-W^A$ if $A=0$.
  3. Predict with $A$ set to 1 for everybody, and then with $A$ set to 0, and average each set of predictions.
  4. The difference of the two averages is the doubly robust plug-in estimator of the average causal effect.

### 13.5 How seriously do we take our estimates?
- Both methods estimated mean weight gain 5.2 kg if everybody quit versus 1.7 kg if nobody quit, a difference of 3.5 kg (95% CI: 2.5, 4.5) (p. 181). Agreement across methods is reassuring because each rests on different modeling assumptions (pp. 181–182).
- Observational estimates remain open to criticism. Their validity for the target population requires three groups of conditions (p. 182):
  1. **Identifiability.** Exchangeability, positivity, consistency must hold so that the study resembles the target trial.
     - Unmeasured confounding or selection bias would prevent conditional exchangeability.
     - Positivity requires the covariates $L$ among quitters to fully overlap with those of non-quitters. Outcome-regression methods (including doubly robust ones) can be used without positivity under the assumption that the outcome model is correctly specified to extrapolate beyond the data (margin, p. 182).
     - Consistency is questionable because there are multiple versions of quitting and of not quitting. The estimate corresponds to a somewhat vague intervention that assigns versions with their actual study frequencies (p. 182).
  2. **Measurement.** All variables must be correctly measured. Error in $A$, $Y$ or $L$ will generally cause bias (p. 182).
  3. **Models.** All models must be correctly specified. For example, if age needs a complex polynomial in the treatment model rather than a parabola, IP weighting would not fully adjust for confounding even with $L$ fully measured. Misspecification acts like measurement error in confounders (pp. 182–183).
- One cannot expect these conditions to hold perfectly. They are not empirically testable, because data on counterfactual outcomes are missing. We assume they hold approximately, supported by expert knowledge, which is itself incomplete (p. 183).
- **Sensitivity analyses** are therefore advised. The text names negative outcome controls and g-estimation for confounding, methods for selection bias, model-specification checks (Section 11.5), quantitative bias analysis, and, sometimes, alternative unverifiable conditions such as instrumental variables. With unmeasured confounders, proximal causal inference and the front door criterion give alternative identifiability conditions (p. 183).
- Conclusion: "We only take our effect estimates as seriously as we take the conditions that are needed to endow them with a causal interpretation." (p. 183)

*Intuition note.* The 3.5 kg is a number plus a list of promises. If a promise (e.g. no unmeasured confounding) is broken, the number can be wrong, and the data alone cannot tell us.

### Technical Point 13.2: Augmented IP weighted estimator
- **Setting.** Binary $A$, positivity, exchangeability, consistency. Target $E[Y^{a=1}]$ (p. 184). It equals either of
$$E[b(L)],\ b(L)=E[Y|A=1,L];\qquad E\!\left[\frac{AY}{\pi(L)}\right],\ \pi(L)=\Pr[A=1|L].$$
- **Two estimators** (p. 184):
  - Plug-in g-formula: $\frac1n\sum_{i=1}^n \hat b(L_i)$. Its bias is large if $\hat b$ is far from $b$.
  - Horvitz–Thompson IP weighted: $\frac1n\sum_{i=1}^n \frac{A_iY_i}{\hat\pi(L_i)}$. Its bias is large if $\hat\pi$ is far from $\pi$.
- **Doubly robust estimator.** The outcome regression is corrected by a function involving the treatment model (p. 184):
$$\widehat E[Y^{a=1}]_{DR}=\frac1n\sum_{i=1}^n\left[\hat b(L_i)+\frac{A_i}{\hat\pi(L_i)}\big(Y_i-\hat b(L_i)\big)\right]$$
  It can also be written $\frac1n\sum_i\Big[\frac{A_iY_i}{\hat\pi(L_i)}-\Big(\frac{A_i}{\hat\pi(L_i)}-1\Big)\hat b(L_i)\Big]$, and is called the *augmented IP weighted estimator* (p. 184).
- **Bias.** Under exchangeability and positivity, $\widehat E[Y^{a=1}]_{DR}-E[Y^{a=1}]$ converges in probability to
$$E\!\left[\pi(L)\left(\frac1{\pi(L)}-\frac1{\pi^*(L)}\right)\big(b(L)-b^*(L)\big)\right],$$
  where $\pi^*$ and $b^*$ are the probability limits of $\hat\pi$ and $\hat b$ (p. 184).
- It is (asymptotically) unbiased if $b^*=b$ or $\pi^*=\pi$, without knowing which. With very high-dimensional $L$, no parametric model is expected to be correct, so even this bias may be large (p. 184).
- **Second-order bias.** The bias depends on the *product* of the error in $1/\pi$ and the error in $b$. This allows doubly robust estimators that may have small bias while using machine learning for $\pi$ and $b$ in high-dimensional settings with large data (Chapter 18) (p. 184).

*Intuition note.* The correction term $\frac{A}{\hat\pi}(Y-\hat b)$ adds to the outcome model's prediction a correction built from its residual $Y-\hat b$, weighted using the treatment model. The text says the resulting estimator has small bias if either $\hat b$ is close to $b$ or $\hat\pi$ is close to $\pi$ (p. 184).

### Technical Point 13.3: AIPW and the doubly robust plug-in estimator
- **Setting.** $\psi_a\equiv E[Y^a]=E[b(a,L)]$ with $b(a,L)=E[Y|A=a,L]$, and $\psi_a=E[I(A=a)Y/f(a|L)]$. With $P_n[H]\equiv\frac1n\sum_iH_i$, the AIPW estimator is (p. 185)
$$P_n\!\left[\frac{I(A=a)Y}{\hat f(A|L)}-\left(\frac{I(A=a)}{\hat f(A|L)}-1\right)\hat b(a,L)\right]=P_n\!\left[\hat b(a,L)+I(A=a)\big\{Y-\hat b(A,L)\big\}/\hat f(A|L)\right]$$
  (Added step: when $I(A=a)=1$, $\hat b(A,L)=\hat b(a,L)$, so the two sides agree algebraically.)
- **Double robustness.** (i) If $\hat f(a|L)$ is consistent, the left-hand side converges to $\psi_a$. (ii) If $\hat b(a,L)$ is consistent, the right-hand side converges to $\psi_a$ (p. 185).
- So $\hat\psi_{1,AIPW}-\hat\psi_{0,AIPW}$ is consistent if either (i) $\hat f(a=1|L)=1-\hat f(a=0|L)$ is consistent, or (ii) both $\hat b(1,L)$ and $\hat b(0,L)$ are consistent (p. 185).
- **Link to the plug-in estimator.** From the right-hand side, the difference equals
$$P_n[\hat b(1,L)]-P_n[\hat b(0,L)]-P_n\!\left[\frac{Y-\hat b(A,L)}{\hat f(A|L)}\{I(A=1)-I(A=0)\}\right].$$
  For the plug-in difference $P_n[\hat b(1,L)]-P_n[\hat b(0,L)]$ to be doubly robust, the last term must be zero in every sample (p. 185):
$$P_n\!\left[\frac{Y-\hat b(A,L)}{\hat f(A|L)}\{I(A=1)-I(A=0)\}\right]=0$$
- This holds if $\hat b(A,L)=b(A,L;\hat\beta,\hat\theta)$ is the iteratively reweighted least squares (IRLS) estimate of
$$E[Y|A,L]=b(A,L;\beta,\theta)=\phi\!\left[m(A,L;\beta)+\theta\,\frac{\{I(A=1)-I(A=0)\}}{\hat f(A|L)}\right],$$
  with $\phi$ the inverse of a canonical link (log, logit, linear). The equation is then the score equation for $\theta$ (p. 185).
- The result is the estimator of Fine Point 13.2. It is a targeted minimum loss-based estimator (TMLE, also "targeted maximum likelihood"). The "clever covariate" is $\frac{\{I(A=1)-I(A=0)\}}{\hat f(A|L)}=\frac{A}{\hat\pi(L)}-\frac{1-A}{1-\hat\pi(L)}$ (p. 185).
- **Alternative.** Replace the $\theta$ term by $\theta_1\frac{A}{\hat\pi(L)}+\theta_2\frac{1-A}{1-\hat\pi(L)}$ (two clever covariates). Then $P_n[\hat b(1,L)]$ and $P_n[\hat b(0,L)]$ are each doubly robust plug-in estimators of $E[Y^{a=1}]$ and $E[Y^{a=0}]$, and their difference remains doubly robust for the average treatment effect (p. 185).

## Toy example (ours, not from the text)
Ten people, binary confounder $L$: 4 have $L=0$, 6 have $L=1$. Suppose a fitted outcome model gives these predicted means:

| | $L=0$ | $L=1$ |
|---|---|---|
| $A=0$ | 1 | 3 |
| $A=1$ | 2 | 6 |

*Three-block recipe.* Block 2 (all $A=0$) has 10 rows with predictions 1,1,1,1,3,3,3,3,3,3. Average: $(4\cdot1+6\cdot3)/10=22/10=2.2$.
Block 3 (all $A=1$) has predictions 2,2,2,2,6,6,6,6,6,6. Average: $(4\cdot2+6\cdot6)/10=44/10=4.4$.
Estimated effect: $4.4-2.2=2.2$.

*Check with the weighted sum.* $\Pr[L=0]=0.4$, $\Pr[L=1]=0.6$. Untreated: $1(0.4)+3(0.6)=0.4+1.8=2.2$. Treated: $2(0.4)+6(0.6)=0.8+3.6=4.4$. Same numbers: averaging over rows equals weighting by $\Pr[L=l]$, and we never estimated $\Pr[L]$ separately.

## Concepts
- [[standardization]] (new) — weighted average of stratum-specific outcome means, with weights equal to the distribution of $L$; estimates $E[Y^a]$ under identifiability conditions (p. 176)
- [[parametric-g-formula]] (new) — plug-in g-formula estimator that uses parametric models for the conditional outcome (p. 181)
- [[ip-weighting]] (new) — pseudo-population method needing a model for treatment (and censoring) given $L$ (p. 175)
- [[positivity]] (new) — every needed treatment level has positive probability in every stratum with $\Pr[L=l]\ne0$; needed for standardization too (p. 176)
- [[model-misspecification]] (new) — the assumed functional form is wrong; causes bias that may differ between treatment and outcome models (p. 179)
- [[doubly-robust-estimation]] (new) — consistent if either the treatment model or the outcome model is correct (pp. 181, 182)
- [[bootstrap]] (new) — resample the study population with replacement and use the spread of estimates as standard error (p. 180)
- [[empirical-distribution]] (new) — averaging over the observed $L_i$ instead of modeling $\Pr[L]$ (p. 179)
- [[sensitivity-analysis]] (new) — re-analysis under varied assumptions to see how estimates change (p. 183)
- Target trial emulation (see canon list) — analysis is sharper when it explicitly emulates a hypothetical randomized trial (p. 181)
- Assignment mechanism / ignorability (see canon list) — here called conditional exchangeability given $L$ (p. 175)

## Canonical instances
- [[smoking-cessation-weight-gain]] (new) — NHEFS example: IP weighting and standardization both give 3.5 kg (pp. 175, 179)
- [[table-2-2-standardization]] (new) — 20-person example, three-block recipe gives 0.5 and 0.5 (pp. 178–179)

## Bridges (candidates)
- [structural-analogy] Three-block dataset with missing $Y$ imputed by a model ↔ Potential outcomes: filling in the unobserved outcome under each treatment (the missing-data view of causal inference).
- [structural-analogy] Averaging predictions over the observed $L_i$ ↔ Monte Carlo integration: replacing an expectation over $L$ by a sample average.
- [structural-analogy] Bootstrap standard errors ↔ Bayesian posterior sampling: both use many simulated draws to describe uncertainty, though they target different things.
- [metaphor] "Two chances to get it right" (doubly robust) ↔ Model averaging or ensembling: hedging between two fallible models.

## Questions this raises
- Under what conditions do IP weighting and standardization agree exactly when models are used (e.g., both models saturated)?
- How does the parametric g-formula change when confounders are time-varying and affected by earlier treatment (Part III)?
- How large must the difference between IP-weighted and standardized estimates be before we should distrust both?
- How well do machine-learning estimates of $\pi$ and $b$ work inside doubly robust estimators (Chapter 18)?

## Reading notes
- Printed page = pdf − 9 (pdf 184 = printed 175). Printed page 186 is blank except for its header.
- Per the source notes supplied with this unit (not visible on the pages), the PDF is the online revision dated 2026-08-19, not the 2020 print version, so chapter references may differ from older citations.
- Inconsistency in the source: the 95% CI for the effect is "2.6, 4.5" on p. 179 but "2.5, 4.5" on p. 181. Both are reported as printed.
- The text layer for Technical Points 13.2 and 13.3 is garbled; equations were checked against the page images.
- Possible sign misprint in Technical Point 13.3 (p. 185): the printed difference ends with a minus before the last $P_n[\cdot]$ term, but expanding the printed AIPW identity gives a plus sign there. The digest copies the printed form. The zero condition that follows is unaffected.
- The chapter has no exercises. Code references (Programs 13.1–13.4) appear in the margins, but the code itself is not in these pages.
