---
id: hernan-2020-whatif/ch14-g
work: hernan-2020-whatif
unit: "14 G-estimation of structural nested models"
pages: 187-198
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
# G-estimation of structural nested models

## L0 — One line
G-estimation finds the causal-effect parameter as the trial value that turns the observed outcome into a "candidate untreated outcome" that, under conditional exchangeability, no longer predicts treatment given the covariates.

## L1 — The gist (≤ 120 words)
How can we estimate the effect of treatment within strata of covariates L without modelling the untreated outcome's dependence on L? The chapter specifies a structural nested mean model for $E[Y^a-Y^{a=0}\mid A,L]$. For each trial parameter value, it builds a candidate untreated outcome $H(\psi^\dagger)=Y-\psi^\dagger A$. Under conditional exchangeability, only the true value gives a candidate that is unrelated to $A$ given $L$. This yields 3.4 kg (95% CI 2.5, 4.5) for smoking cessation in NHEFS. The method adjusts for confounding, not selection bias, and does not need rank preservation. It matters because it makes fewer modelling assumptions than the parametric g-formula.

**Prerequisites:** potential outcomes; conditional exchangeability; logistic regression and Wald tests; IP weighting and standardization (Ch. 12–13); IP weights for censoring (Ch. 12); basic matrix notation.

## L2 — Key ideas
- G-estimation, IP weighting (inverse-probability weighting) and standardization are the "g-methods". They were designed for treatments that vary over time, so for time-fixed treatment they may be overkill, since simpler alternatives exist (p. 187).
- Conditional exchangeability can be written $\Pr[A=1\mid Y^{a=0},L]=\Pr[A=1\mid L]$. If we could fit a correct logistic model for $A$ that includes $Y^{a=0}$, the expected value of the estimate of $\alpha_1$ would be zero (pp. 188–189).
- A structural nested mean model models only the effect $E[Y^a-Y^{a=0}\mid A=a,L]$ and leaves the intercept and the main effect of $L$ unspecified. It is semiparametric (part of the model is left unspecified) and can be more robust than the parametric g-formula (p. 189).
- G-estimation tries trial values $\psi^\dagger$ and keeps the one whose $H(\psi^\dagger)=Y-\psi^\dagger A$ has $\alpha_1=0$. A 95% CI comes from inverting the test of $\alpha_1=0$ (pp. 193–195).
- The procedure is explained with the rank-preserving model (the same effect for everyone with the same $L$), which the text calls implausible. It still gives a consistent estimate of the mean-model parameter when the mean model is correct, without rank preservation (pp. 192–195).
- G-estimation adjusts only for confounding. Selection bias from censoring generally has to be handled first with IP weights $W^C$ (p. 190).
- If unmeasured confounding makes $\alpha_1$ a known non-zero value, one tests that value instead. This supports a sensitivity analysis (p. 195).
- Omitting needed product terms (effect modification) makes the model misspecified. With product terms, the estimate has a direct formula (closed form) in linear models, and in general it solves an estimating equation (pp. 196, 198).

## L3 — Walkthrough

### Introduction (p. 187)
G-estimation is the third g-method, after IP weighting and standardization. The "g" stands for "generalized" treatment contrasts with treatments that vary over time. For time-fixed treatment (Part II), simpler alternatives exist. The book still uses this setting to show the main features without Part III's complications (p. 187).

G-estimation was left until Part II because it is easier to explain through a structural model. Models fitted by g-estimation are called *structural nested models*. The three g-methods rest on different modelling assumptions (p. 187).

### 14.1 The causal question revisited (pp. 187–188)
- Data: 1566 smokers aged 25–74. $A=1$ means quit smoking, $Y$ is weight gain. Exchangeability is assumed conditional on $L$ (sex, age, race, education, smoking intensity and duration, activity, exercise, weight) (p. 187).
- Earlier chapters estimated the population effect $E[Y^{a=1,c=0}]-E[Y^{a=0,c=0}]$. Effects in subsets can use marginal structural models with product terms or standardization within the subset (p. 187).
- This chapter targets the effect within every stratum of $L$: $E[Y^{a=1,c=0}\mid L]-E[Y^{a=0,c=0}\mid L]$ (p. 188).
- An alternative is to put all of $L$ and the products $A\times L$ into the marginal structural model. Then $SW^A(L)=1$, and an unweighted outcome regression, if correct, fully adjusts for confounding by $L$ (p. 188).

### 14.2 Exchangeability revisited (pp. 188–189)
- Conditional exchangeability means $Y^a\perp\!\!\!\perp A\mid L$ for $a=0,1$. Equivalently, knowing $Y^{a=0}$ does not change the probability of quitting within a level of $L$ (p. 188):
$$\Pr[A=1\mid Y^{a=0},L]=\Pr[A=1\mid L]$$
- Suppose we proposed the logistic model (p. 188), where $\alpha_2L=\sum_{j=1}^p\alpha_{2j}L_j$:
$$\operatorname{logit}\Pr[A=1\mid Y^{a=0},L]=\alpha_0+\alpha_1Y^{a=0}+\alpha_2L$$
- It cannot be fitted to real data because $Y^{a=0}$ is unknown for everyone. If it could be fitted, with exchangeability and a correct model, the expected value of $\hat\alpha_1$ is zero, because $Y^{a=0}$ does not predict $A$ given $L$ (p. 189). The text calls this half of g-estimation.

*Intuition note:* Within a stratum of $L$, who gets treated is unrelated to how much they would have gained without treatment. So a coefficient on the true $Y^{a=0}$ must be zero. G-estimation turns this into a way of recognising the right counterfactual.

### 14.3 Structural nested mean models (pp. 189–191)
- The conditional effect equals $E[Y^{a=1}-Y^{a=0}\mid L]$. With no effect modification, the structural model is $E[Y^a-Y^{a=0}\mid L]=\beta_1a$. A model for differences has no intercept $\beta_0$ and no $\beta_2L$ term, because these cancel in the difference (p. 189).
- With effect modification, add a product term: $E[Y^a-Y^{a=0}\mid L]=\beta_1a+\beta_2aL$. Under $Y^a\perp\!\!\!\perp A\mid L$ the effect is the same in treated and untreated within levels of $L$. So the model can be written as the *structural nested mean model* (p. 189):
$$E[Y^a-Y^{a=0}\mid A=a,L]=\beta_1a+\beta_2aL$$
- Robins (1994) first described these models. They are "nested" when treatment is time-varying (margin note, p. 189).
- Unlike the parametric outcome models of Chapter 13, this model is semiparametric. It has no $\beta_0$ and no $\beta_3L$, so it makes fewer assumptions and can be more robust to misspecification than the parametric g-formula (p. 189).
- **Fine Point 14.1 (p. 190).** Take the marginal structural mean model $E[Y^a\mid V]=\beta_0+\beta_1a+\beta_2aV+\beta_3V$ for a continuous covariate $V$, a component of $L$.
  - Then $\beta_1+\beta_2v$ is the effect at $V=v$, and $\beta_0+\beta_3v$ is $E[Y^{a=0}\mid V=v]$.
  - If only the effect matters, write $E[Y^a-Y^{a=0}\mid V]=\beta_1a+\beta_2aV$. This is a *semiparametric marginal structural mean model* that leaves $E[Y^{a=0}\mid V]$ unspecified.
  - If one is interested only in conditional effects given $V$, it is more robust than parametric ones when $V$ is continuous or high-dimensional. A wrong model $\beta_0+\beta_3V$ may bias the effect estimate even if $\beta_1a+\beta_2aV$ is correct, because the estimates of $(\beta_0,\beta_3)$ can be correlated with those of $(\beta_1,\beta_2)$.
  - If $V$ is a strict subset of the confounders $L$, this model equals a structural nested model for a treatment blip given $V$. To estimate it without censoring, first weight by $SW^A(V)=f(A\mid V)/f(A\mid L)$, then use g-estimation with $V$ replaced by $L$ and each contribution weighted by $SW^A(V)$.
  - If $V=L$, the weights are 1. This "faux" semiparametric marginal structural model is, under conditional exchangeability, the structural nested mean model used in this chapter.
- **Censoring (pp. 189–191).** With censoring the target is $E[Y^{a=1,c=0}-Y^{a=0,c=0}\mid A,L]$, which needs adjustment for confounding and for selection bias. G-estimation can adjust only for confounding. So first create a pseudo-population with nonstabilized weights $W^C=1/\Pr[C=0\mid L,A]$ (from Ch. 12), then apply g-estimation. This assumes $L$ suffices for both biases. All analyses in this chapter use these weights. In that pseudo-population the model is a structural model without censoring (p. 191):
$$E[Y^{a,c=0}-Y^{a=0,c=0}\mid A=a,L]=\beta_1a+\beta_2aL$$
  The superscript $c=0$ is then dropped (p. 191).
  - Margin note (p. 190): technically, IP weights are unnecessary if the treatment is time-fixed, does not affect any variable in $L$, the outcome is measured at one time, and $Y^a\perp\!\!\!\perp(A,C)\mid L$. Then g-estimation can use the uncensored subjects alone.
- For continuous treatment, the model must specify a dose-response function, e.g. $E[Y^a-Y^{a=0}\mid A=a,L]=\beta_1a+\beta_2a^2+\beta_3aL+\beta_4a^2L$, or a spline (p. 191).
- **Technical Point 14.1 (p. 191).** The text treats only additive models. For positive outcomes, a multiplicative model is often preferred: $\log\left(E[Y^a\mid A=a,L]/E[Y^{a=0}\mid A=a,L]\right)=\beta_1a+\beta_2aL$. It is fitted with $H(\psi^\dagger)=Y\exp[-\psi_1^\dagger a-\psi_2^\dagger aL]$ (as printed, with lowercase $a$).
  - Originally it was usable for a binary $Y$ only if $\Pr[Y=1]$ was small in all strata. Richardson, Robins and Wang (2017) removed this restriction, and Wang et al. (2022) extended it to time-varying treatments with doubly robust estimators.
  - A structural nested logistic model had been suggested for non-rare binary outcomes. It has two drawbacks: it is not collapsible, and it does not generalize easily to time-varying treatments.

### 14.4 Rank preservation (pp. 191–193)
- Imagine ranking everyone by $Y^{a=1}$ and by $Y^{a=0}$. If both lists are in identical order, there is *rank preservation* (p. 192).
- *Additive rank preservation*: the effect is exactly the same, on the additive scale, for all individuals. The sharp null (no effect on anyone) is a special case. *Conditional* additive rank preservation: the effect is the same for all with the same $L$ (p. 192). An example model (p. 192):
$$Y^a_i-Y^{a=0}_i=\psi_1a+\psi_2aL_i\quad\text{for all individuals }i$$
  So $Y_i^{a=1}=Y_i^{a=0}+\psi_1+\psi_2l$ for all $i$ with $L=l$. Figures 14.1 and 14.2 show the same shift for every person within a stratum, with different distributions in different strata (p. 192).
- The text calls rank preservation scientifically implausible. Individual effects vary even given $L$, because some people are more susceptible. Figure 14.3 shows individual shifts that vary and ranks that change (pp. 192–193).
- None of the book's methods require it. The marginal structural model from Chapter 12 gave an average effect of 3.5 kg (95% CI 2.5, 4.5) without it. The structural nested mean model of Section 14.3 also makes no such assumption (p. 193).
- The rank-preserving model is nevertheless used next because g-estimation is easier to understand for it, and the procedure is the same for both kinds of model. The rank-preserving structural model is a structural mean model (p. 193).

*Intuition note:* "Rank preserving" means treatment moves everyone with the same $L$ by the same amount. The text uses it in this chapter to explain g-estimation, but calls it unrealistic; the mean model does not require it.

### 14.5 G-estimation (pp. 193–196)
**Setup (p. 193).** Take the one-parameter model $E[Y^a-Y^{a=0}\mid A=a,L]=\beta_1a$ (no additive effect modification by $L$). Also assume the rank-preserving model $Y^a_i-Y^{a=0}_i=\psi_1a$ for all $i$, so $\psi_1=\beta_1$. Rewrite it as
$$Y^{a=0}=Y^a-\psi_1a$$
**Link to data (pp. 193–194).** By consistency, $Y^A=Y$. Replacing $a$ by each person's $A$ gives
$$Y^{a=0}=Y-\psi_1A$$
If $\psi_1$ were known, $Y^{a=0}$ could be computed for everyone.

**The game (p. 194).** A friend says $\psi_1\in\{-20,0,10\}$. For each candidate $\psi^\dagger$ compute
$$H(\psi^\dagger)=Y-\psi^\dagger A$$
$H(\psi^\dagger)=Y^{a=0}$ if $\psi^\dagger=\psi_1$, and only one candidate is the true counterfactual. Fit, for each candidate, the logistic model
$$\operatorname{logit}\Pr[A=1\mid H(\psi^\dagger),L]=\alpha_0+\alpha_1H(\psi^\dagger)+\alpha_2L$$
The candidate with $\alpha_1=0$ is the counterfactual $Y^{a=0}$, and its $\psi^\dagger$ is the estimate. For example, if $H(10)$ is unassociated with $A$ given $L$, then $\hat\psi_1=10$ (p. 194).

Margin note: g-estimation does not test conditional exchangeability; it assumes it. Rosenbaum (1987) proposed a version for non-time-varying treatments (p. 194).

**Search (p. 194).** Without a friend, search over $\psi^\dagger$, e.g. from $-20$ to $20$ in steps of 0.01. A finer grid gets closer to the estimate but costs more computation.

**NHEFS result (p. 194).** The authors computed 31 candidates $H(2.0),H(2.1),\dots,H(5.0)$ and fitted 31 logistic models. These were the Chapter 12 denominator models plus one $H(\psi^\dagger)$. $\hat\alpha_1$ was closest to zero at $H(3.4)$ and $H(3.5)$. A finer search put the minimum, essentially zero, at $H(3.446)$. The g-estimate is 3.4 kg.

**Confidence interval (pp. 194–195).**
- The authors used the Wald test P-value for $\alpha_1=0$ in each model. It was 0.998 at $\psi^\dagger=3.446$. It was above 0.05 for $\psi^\dagger$ from about 2.5 to 4.5, so the CI limits are 2.5 and 4.5 (p. 195).
- In general, the 95% CI is the set of $\psi^\dagger$ with P-value $>0.05$ when testing $\alpha_1=0$ (inversion of the test). Bootstrapping is another option. Other valid tests may be used; a Score test avoids fitting multiple models and, in large samples, is essentially equivalent to a Wald test (margin, p. 195).
- Under censoring, the logistic models use only uncensored individuals, each weighted by $W^C$ (margin note, p. 195). The test used a robust variance, so the CI is conservative in large samples (it traps the truth at least 95% of the time). Bootstrapping would give a non-conservative, possibly narrower CI (p. 195).

**Fine Point 14.2 — sensitivity analysis (p. 195).**
- Suppose quitting is less likely when the spouse smokes, and spouse smoking is linked to determinants of weight gain not in $L$. Then $A$ and $Y^{a=0}$ are associated given $L$, so $\alpha_1\neq0$ and g-estimation as described cannot be applied.
- But g-estimation does not require exchangeability; it requires that the size of non-exchangeability, $\alpha_1$, is known. If $\alpha_1$ is expected to be 0.1, test $\alpha_1=0.1$ instead.
- Repeating the analysis over a range of $\alpha_1$ values and plotting the estimates shows sensitivity to unmeasured confounding. A practical problem is how to judge whether 0.1 is a lot. Robins, Rotnitzky and Scharfstein (1999) give details.

**Non-rank-preserving case (pp. 195–196).** The g-estimation algorithm gives a consistent estimate of $\beta_1$ of the mean model, if the mean model is correct (the average effect is equal at all levels of $L$). This holds whether or not individual effects are constant. The algorithm does not need $H(\beta_1)=Y^{a=0}$ for everyone. It only needs $H(\beta_1)$ and $Y^{a=0}$ to have the same conditional mean given $L$ (pp. 195–196).

*Intuition note:* G-estimation asks which "undo the treatment effect" subtraction leaves treatment unassociated with the result given $L$. The CI is every trial value that the data cannot reject.

### 14.6 Structural nested models with two or more parameters (pp. 196–197)
- A one-parameter model assumes no effect modification. If there is effect modification by some $V$ in $L$ and the product term $\beta_2aV$ is omitted, the structural nested model is misspecified and inferences will be wrong. A saturated marginal structural model $E[Y^a]=\beta_0+\beta_1a$ is not misspecified when $\beta_2aV$ and $\beta_3V$ are omitted. Structural nested models estimate effects within levels of $L$ by definition, so omitting product terms when there is effect modification will generally cause bias (p. 196).
- Margin note: marginal structural models are null-preserving, meaning the model is never misspecified when the average causal null is true. Structural nested models also preserve the null. The parametric g-formula does so for time-fixed treatments but loses it in the time-varying setting (p. 196).
- Example: $E[Y^a-Y^{a=0}\mid A=a,L]=\beta_1a+\beta_2aV$ with $V$ baseline smoking intensity. Let $\beta^\dagger=(\beta_1^\dagger,\beta_2^\dagger)$ and $H(\beta^\dagger)=Y-\beta_1^\dagger A-\beta_2^\dagger AV$. Fit (p. 196)
$$\operatorname{logit}\Pr[A=1\mid H(\beta^\dagger),L]=\alpha_0+\alpha_1H(\beta^\dagger)+\alpha_2H(\beta^\dagger)V+\alpha_3L$$
  and find $(\beta_1^\dagger,\beta_2^\dagger)$ making both $\alpha_1$ and $\alpha_2$ zero. The search is two-dimensional, so brute force is more involved.
- A search is not generally necessary. For linear mean models the estimator has closed form. For nonlinear models, standard derivative-based optimization such as Newton-Raphson works, because g-estimation solves an estimating equation (Technical Point 14.2). For certain structural nested models for survival analysis, a search is needed because the estimating equation is not differentiable (Chapter 17) (p. 196).
- NHEFS: $\hat\beta_1=2.86$ and $\hat\beta_2=0.03$. The 95% CIs are most easily obtained by bootstrapping (p. 197).
- General linear model for dichotomous treatment, with $p$ components of $L$ (p. 197):
$$E[Y^a-Y^{a=0}]=\beta_1a+a\sum_{j=1}^p\beta_{2j}L_j$$
  This has $p+1$ parameters. The average effect in the study population is $\beta_1+\frac1n\sum_i\sum_{j=1}^p\beta_{2j}L_{ij}$, with $n$ individuals (p. 197).
- The chapter ends by pointing to outcome regression and propensity scores as the next topics (p. 197).

### Technical Point 14.2 — G-estimation of structural nested mean models (p. 198)
Model: $E[Y-Y^{a=0}\mid A,L]=A\gamma(L;\beta)$, with $\gamma$ a known function and $\gamma(L;\beta^\dagger=0)=0$. Under the text's assumptions, including a correct parametric model for $E[A\mid L]$, g-estimation gives an asymptotically unbiased, normally distributed estimate of $\beta$. It is the $\beta^\dagger$ that minimizes the association between $H(\beta^\dagger)=Y-A\gamma(L;\beta^\dagger)$ and $A$ given $L$. Using the score test, this means solving
$$\sum_{i=1}^n I[C_i=0]\,W_i^C\,H_i(\beta^\dagger)\,(A_i-E[A\mid L_i])\,q(L_i)=0$$
- $q(L_i)$ is a user-chosen vector function with the same dimension as $\beta$. $I[C_i=0]$ is the uncensored indicator. $W_i^C$ and $E[A\mid L_i]=\Pr[A=1\mid L_i]$ are replaced by estimates.
- $E[A\mid L_i]$ can come from a logistic model for $A$ given $L$ weighted by $W_i^C$ (zero for the censored). Alternatively, because $A$ and $L$ are observed for everyone, an unweighted logistic regression on all individuals works.
- The choice of $q$ affects efficiency (CI length), not consistency. Robins (1994) derived the $q$ that minimizes CI length.
- **Closed form.** If $\gamma(L;\beta^\dagger)=\beta^{\dagger,T}d(L)$ for a known vector function $d(L)$ with the dimension of $\beta$ (say $k$), and $q=d$, then $\hat\beta$ is a $k\times k$ inverse times a $k\times1$ vector:
$$\hat\beta=\left(\sum_{i=1}^nI[C_i=0]W_i^CA_i(A_i-E[A\mid L_i])d(L_i)d(L_i)^T\right)^{-1}\sum_{i=1}^nI[C_i=0]W_i^CY_i(A_i-E[A\mid L_i])d(L_i)$$
- Efficiency question: can $H_i(\beta^\dagger)$ be replaced by a nonlinear function, such as $[H_i(\beta^\dagger)]^3$? Not for models that impose only mean independence, $E[H(\beta_1)\mid A,L]=E[H(\beta_1)\mid L]$, like the models here. It can be done for models that impose $H(\beta_1)\perp\!\!\!\perp A\mid L$, such as structural nested distribution models (not described here).
- The estimator is consistent only if the models for $E[A\mid L]$ and $\Pr[C=1\mid A,L]$ are both correct. A more robust version replaces $H(\beta^\dagger)$ by $H(\beta^\dagger)-E[H(\beta^\dagger)\mid L]$. Here $E[H(\beta^\dagger)\mid L]=E[Y^{a=0}\mid L]$ is fitted by an unweighted linear model among the uncensored. The estimate is consistent if either (i) that model is correct, or (ii) both models for $E[A\mid L]$ and $\Pr[C=1\mid A,L]$ are correct. This is *doubly robust* (p. 198).

*Intuition note:* The estimating equation asks that the leftover part of $H$ be uncorrelated with the part of $A$ not explained by $L$. With $d(L)=1$ and no $L$, the closed form reduces to a simple ratio (see Toy example).

## Toy example (ours, not from the text)
No covariates $L$ and no censoring, so $E[A\mid L]=\Pr[A=1]=4/8=0.5$. Assume "no confounding", i.e. the treated and untreated are exchangeable. Data: treated ($A=1$) have $Y=5,7,6,6$ (mean 6). Untreated ($A=0$) have $Y=2,4,3,3$ (mean 3).

With no $L$, we use the difference in mean $H$ between treated and untreated as a stand-in for $\alpha_1$ (our simplification; the text uses a logistic coefficient). Candidates $H(\psi^\dagger)=Y-\psi^\dagger A$:

| $\psi^\dagger$ | $H$ among treated | mean treated | mean untreated | difference |
|---|---|---|---|---|
| 0 | 5, 7, 6, 6 | 6 | 3 | 3 |
| 3 | 2, 4, 3, 3 | 3 | 3 | 0 |
| 5 | 0, 2, 1, 1 | 1 | 3 | −2 |

Only $\psi^\dagger=3$ makes $H$ unrelated to $A$. It gives $\hat\psi_1=3$. Here $H(3)$ among the treated is exactly the untreated list $\{2,4,3,3\}$.

Check with the closed form of Technical Point 14.2, $d(L)=1$, $W^C=1$:
- $\sum_iA_i(A_i-0.5)=4\times0.5=2$.
- $\sum_iY_i(A_i-0.5)=0.5\times(5+7+6+6)-0.5\times(2+4+3+3)=0.5\times24-0.5\times12=6$.
- $\hat\beta=2^{-1}\times6=3$. ✓.

## Concepts
- [[g-estimation]] (new) — find the structural parameter whose candidate untreated outcome $H(\psi^\dagger)$ has $\alpha_1=0$ given $L$ (p. 194).
- [[structural-nested-mean-model]] (new) — model for $E[Y^a-Y^{a=0}\mid A=a,L]$ that leaves the untreated-outcome mean unspecified (p. 189).
- [[g-methods]] (new) — IP weighting, standardization and g-estimation; built for generalized, time-varying treatment contrasts (p. 187).
- [[rank-preservation]] (new) — individual effects are identical on the additive scale given $L$; used in the chapter to explain the method, though the text calls it implausible (pp. 192–193).
- [[assignment-mechanism-ignorability]] — here written as $\Pr[A=1\mid Y^{a=0},L]=\Pr[A=1\mid L]$, which is the form used by g-estimation (p. 188).
- [[potential-outcomes]] — $Y^{a=1}$ and $Y^{a=0}$; $H(\psi^\dagger)$ is a candidate for $Y^{a=0}$ (p. 194).
- [[confounding-vs-selection-bias]] — g-estimation adjusts only for confounding; selection bias from censoring needs IP weights (p. 190).
- [[confidence-interval-by-test-inversion]] (new) — CI is the set of $\psi^\dagger$ not rejected in the test of $\alpha_1=0$ (p. 195).
- [[doubly-robust-estimator]] (new) — consistent if either the model for $E[H\mid L]$ or both treatment and censoring models are correct (p. 198).
- [[propensity-score]] — the model for $\Pr[A=1\mid L]$ is the Chapter 12 IP-weight denominator model plus $H(\psi^\dagger)$ (p. 194; the term itself is not used on these pages).

## Canonical instances
- [[nhefs-smoking-cessation]] (new) — g-estimate 3.4 kg (95% CI 2.5, 4.5) in the one-parameter model; $\hat\beta_1=2.86$, $\hat\beta_2=0.03$ with a smoking-intensity product term (pp. 194–197).
- [[spouse-smoking-unmeasured-confounding]] (new) — example where $\alpha_1\ne0$, motivating the sensitivity analysis (p. 195).

## Bridges (candidates)
- [same-math] CI by inverting the test of $\alpha_1=0$ ↔ frequentist inference: confidence set as all parameter values a test does not reject — same construction.
- [structural-analogy] Testing a known non-zero $\alpha_1$ for sensitivity analysis ↔ Bayesian inference: a prior or fixed value for a bias parameter, with results shown across its range.
- [structural-analogy] Estimating equation with $(A-E[A\mid L])$ ↔ residualizing treatment on covariates, then relating it to the transformed outcome.
- [metaphor] Searching $\psi^\dagger$ until $H$ looks unrelated to $A$ ↔ posterior predictive checking: tune a parameter until a data-based diagnostic shows no leftover structure.

## Questions this raises
- How can we judge whether a given value of $\alpha_1$, such as 0.1, is a lot of unmeasured confounding (p. 195)?
- Why does the text say g-estimation does not need rank preservation when it uses it to explain the method? How is "same conditional mean" enough (p. 196)?
- What is "nested" about the models when treatment varies over time (Part III) (p. 189)?
- What are the trade-offs between this semiparametric approach and the parametric g-formula, given the same $L$ (p. 189)?

## Reading notes
- Printed page = pdf page − 9 (pdf 196 = printed 187). The source note says the PDF is the online revision dated 2026-08-19. Chapter references (e.g. Technical Point 21.6) may differ from older editions.
- Source units cite programs (Program 14.1–14.3) but their code is not on these pages.
- The margin note on p. 195 writes the censoring weight as $SW^C$, while the main text (p. 190) and Technical Point 14.2 use $W^C$; this digest uses $W^C$.
- Misprints seen in the images: Section 14.6 writes $E[Y^a-Y^{a=0}]$ for the general model, omitting "$\mid A=a,L$", and "$\beta_{21,\dots}$" for $\beta_{21},\dots,\beta_{2p}$. Technical Point 14.1 uses lowercase $a$ in $H(\psi^\dagger)$ where the text elsewhere uses $A$. "Each strata" appears in 14.1.
- No exercises in this unit. Equations were checked against the page images; none were unreadable.
