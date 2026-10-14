---
id: hernan-2020-whatif/ch17-causal
work: hernan-2020-whatif
unit: "17 Causal survival analysis"
pages: 227-240
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Causal survival analysis (Hernán & Robins, ch. 17)

## L0 — One line
For a time-fixed treatment, causal survival curves can be built from estimated discrete-time hazards, chained into survival by a product and adjusted for confounding with IP weighting or the parametric g-formula; structural AFT models are fitted here by g-estimation modified with "artificial censoring".

## L1 — The gist (≤ 120 words)
How can we estimate the causal effect of a treatment on time to an event when many event times are never observed because follow-up ends? The chapter converts hazards (event probability among those still event-free) into survival curves by multiplying one minus hazard over time, using person-time data. Confounding is handled by IP weighting of marginal structural models or by the parametric g-formula. A third route, g-estimation of structural accelerated failure time models, must also censor some individuals whose event was observed, otherwise it creates selection bias. Hazard ratios are discouraged because they can be biased even when treatment helps no one. The NHEFS smoking-cessation example shows little evidence of an effect on mortality.

**Prerequisites:** conditional probability; counterfactuals and exchangeability; logistic regression; IP weighting, standardization and g-estimation as in earlier chapters (12–14); colliders and selection bias (Chapter 8).

## L2 — Key ideas (5–10 bullets)
- Survival, risk and hazard are different quantities. The hazard is conditional on being event-free, so unlike the risk it can rise or fall (p. 229).
- Survival at $k$ is the product over $m=1..k$ of one minus the hazard. Hazards can be estimated by logistic regression on person-time data. The fit is straightforward with person-time data (p. 230–231).
- Hazard ratios are problematic. A single reported ratio is a weighted average. Conditioning on survival can induce collider selection bias even if treatment helps no one (p. 231).
- With individual-specific censoring, survival is estimated through the hazards among the uncensored (with a common censoring time k_end simple fractions suffice). Counting uncensored survivors estimates a joint probability, not the survival we want (p. 233–234).
- IP weighting of a marginal structural hazards model and the parametric g-formula both give marginal causal survival curves under exchangeability, positivity and consistency, but with different modelling assumptions (p. 235–237).
- Structural nested models cannot give survival or hazards directly. Structural AFT models target survival-time ratios (p. 237).
- G-estimation of AFT models needs artificial censoring: excluding some individuals with observed death times, to avoid selection bias (p. 239–240).

## L3 — Walkthrough

### Intro and 17.1 Hazards and risks (p. 227–229)
**Setting.** Survival analysis studies time $T$ to an event (death, marriage, flu, …). Many event times are unknown because follow-up ends. The chapter covers only time-fixed treatments (p. 227).

**Example.** NHEFS: 1629 smokers aged 25–74 and alive through 1982. Follow-up starts 1 Jan 1983 and administratively ends 31 Dec 1992, so the administrative censoring time is 120 months for everyone. Only 318 died (102 treated/quitters, 216 untreated), so 1311 are administratively censored: we only know $T>120$ (p. 227–228).
- *Administrative censoring* = survival time cut off by the end of the study's data. With staggered entry, censoring times differ across people (p. 227).
- Other censoring (loss to follow-up, competing events) can be handled by standardization or IP weighting. It is deferred to Part III because it is usually time-varying (p. 228).
- Because of censoring we cannot compute mean survival $E[T]$ and use other measures (p. 228).

**Fine Point 17.1 (competing events, p. 228).** A competing event (e.g., death from other causes when studying stroke) prevents the event of interest.
- Treating it as censoring tries to simulate a world without it. The estimand is hard to interpret and censoring may introduce selection bias needing adjustment.
- Not treating it as censoring effectively sets the event time to infinity. A non-null estimate may then come from a direct effect on death.
- A composite event changes the causal question. Restricting to the principal stratum (those who would not die under any treatment) is a local average effect, hard to interpret and estimate.
- None of these is satisfactory; statistical techniques cannot bypass the logical questions about the estimand.

**Definitions (p. 228–229).**
- Survival $\Pr[T>k]$: proportion surviving through $k$. The survival curve starts at $\Pr[T>0]=1$ and never increases.
- Risk (cumulative incidence) $=1-\Pr[T>k]=\Pr[T\le k]$. It starts at 0 and never decreases.
- Discrete-time hazard $=\Pr[T=k\mid T>k-1]$: the proportion with the event among those still event-free before $k$.
- Risk has a constant denominator (everyone at baseline) and a cumulative numerator, so it stays flat or increases. Hazard has a shrinking denominator (those alive) and a numerator of recent events only, so it may rise or fall (p. 229).

**Example numbers.** The observed 120-month survival was 76.2% in quitters ($A=1$) vs 82.0% in non-quitters, and the 120-month risk was 23.8% vs 18.0%. Reading this contrast causally would require quitters and non-quitters to be marginally exchangeable, assumed only until 17.4. The log-rank test gives $P=0.005$ (Fig. 17.1). The hazard at 120 months is 0% in quitters (last death at month 113) and $1/986=0.10\%$ in non-quitters. The hazard curves look roughly like an M (p. 229).

The hazard ratio is discouraged (Fine Point 17.2), so the book favours survival/risk. Hazards are still a useful intermediate step (p. 229).

*Intuition note.* Risk is "how many have had the event so far". Hazard is "of those still at risk now, how many have it now". The hazard is the building block, the survival curve is what we report.

### 17.2 From hazards to risks (p. 229–232)
**Data formats.** The "wide" format has one row per person (1629 rows). The person-time ("long") format has one row per person-month (176,764 rows). The long format is used for most of the chapter and for all of Part III (p. 230).

**Event indicator.** $D_k=1$ if $T\le k$ and $D_k=0$ if $T>k$. Everyone has $D_0=0$. The row for person at time $k$ carries $D_{k+1}$. The last row is the first with $D_{k+1}=1$ or month 119 (p. 230). Figure 17.2: $A\to D_1\to D_2$, $A\to D_2$, and $U$ (unmeasured susceptibility) $\to D_1, D_2$ (p. 230).

Survival at $k$ is $\Pr[D_k=0]$. Risk is $\Pr[D_k=1]$. Hazard is $\Pr[D_k=1\mid D_{k-1}=0]$ and equals the risk at $k=1$ (p. 230).

**Survival from hazards (p. 230):**
$$\Pr[D_k=0]=\prod_{m=1}^{k}\Pr[D_m=0\mid D_{m-1}=0]$$
So survival is the product of one minus the hazard at all earlier times, and risk is one minus that.

**Kaplan–Meier (p. 230–231).** Estimate each hazard nonparametrically as cases in interval $k$ divided by individuals alive at the end of interval $k-1$. Plugging into the product gives the Kaplan–Meier (product-limit) estimator, used for Fig. 17.1. It is an excellent estimator of the survival curve if the total number of failures is reasonably large. Per-interval hazard estimates are very unstable, so smoothing by a parametric model may be needed (p. 231).

**Fine Point 17.2: the hazards of hazard ratios (p. 231).**
1. The hazard ratio generally varies with time. A single reported ratio (usually from a Cox proportional hazards model) is a weighted average of time-specific ratios, so it may be 1 even if the survival curves differ. If risk is rare and censoring occurs only at a common $k_{end}$, the weight at $k$ is proportional to the number of events among the untreated at $k$.
2. Even time-specific ratios are not straightforwardly causal. Suppose treatment kills all high-risk individuals by $k$ and has no effect on others. At $k+1$ treated survivors are all low-risk, while untreated survivors are a mix. The hazard ratio is then below 1 though treatment benefits nobody. This is selection bias from conditioning on a post-treatment variable (being alive), a collider: conditioning on $D_1$ will generally open $A\to D_1\leftarrow U\to D_2$ (Fig. 17.3). It does not happen if there are no arrows from $A$ into the event indicators.
Ratios and differences of survival or risk refer to a fixed time (e.g., the 120-month risk ratio).

*Intuition note.* Treatment can change who is left in the risk set. Comparing hazards compares groups that are no longer alike, even if they started alike.

**Parametric hazards (p. 231–232).** Fit a logistic model on person-time rows restricted to those alive at $k$:
$$\operatorname{logit}\Pr[D_{k+1}=1\mid D_k=0,A]=\theta_{0,k}+\theta_1A+\theta_2A\times k+\theta_3A\times k^2$$
with a flexible intercept such as $\theta_{0,k}=\theta_0+\theta_4k+\theta_5k^2$. The intercept allows a time-varying hazard. The product terms with $A$ let the hazard ratio vary over time. Standard errors from a routine logistic program are correct if the hazards model is correct, although people appear in many rows (p. 231). Other link functions (e.g., probit) can be used (p. 231).

**Technical Point 17.1 (p. 233).** Suppose the hazards model $\Pr[D_{k+1}=1\mid D_k=0,A]=\Pr[D_{k+1}=1\mid D_k=0,A=0]\times\exp(\alpha_1A)$, so the discrete-time hazard ratio is $\exp(\alpha_1)$ at all times. Taking logs gives $\log\Pr[\cdot\mid A]=\alpha_{0,k}+\alpha_1A$ with $\alpha_{0,k}=\log\Pr[D_{k+1}=1\mid D_k=0,A=0]$. If the hazard is near 0, it is approximately the odds $\Pr[D_{k+1}=1\mid\cdot]/\Pr[D_{k+1}=0\mid\cdot]$, so $\operatorname{logit}\Pr[D_{k+1}=1\mid D_k=0,A]\approx\alpha_{0,k}+\alpha_1A$. Thus $\theta_1$ approximates the log hazard ratio $\alpha_1$. Rule of thumb: the approximation is often considered accurate enough when the hazard is $<0.1$ for all $k$. This can almost always be ensured by choosing a short enough time unit (years for lung cancer, days for colds), at the cost of more rows.

**Fine Point 17.3 (p. 232).** Nonparametric methods (Kaplan–Meier) make no assumption about unobserved failure times. Parametric models assume a distribution (exponential, Weibull); the logistic hazards model is parametric. Cox and AFT models leave the baseline hazard (all covariates zero) unspecified but restrict how other covariate values change it, so they are semiparametric.

**Result (p. 232).** Multiply one minus the fitted hazards, separately by $A$, to get smooth survival curves (Fig. 17.4). Validity needs no misspecification of the hazards model. Here this seems plausible because the estimates are essentially those from Kaplan–Meier. A 95% CI can be obtained by bootstrapping individuals.

### 17.3 Why censoring matters (p. 232–234)
With only a common censoring time $k_{end}=120$, the above is overkill. One can simply take the fraction of treatment group $a$ surviving to $k+1$, or fit logistic models for $\Pr[D_{k+1}=0\mid A]$ at each time (p. 232).

**Staggered entry.** Censoring times then differ across people. Define $C_k=0$ if the administrative end of follow-up is later than $k$, else 1. The row at $k$ carries $C_{k+1}$ (p. 232). The goal is the survival that would have been observed if nobody were censored before $k_{end}$ (the maximum administrative censoring time): $\Pr[D_k^{\bar c=\bar 0}=0\mid A=a]$. Suppose start date is as if randomly assigned, so the censoring time is independent of treatment and death time (p. 233).

**Why the naive fraction fails.** The fraction treated with level $a$ who survived and were uncensored estimates the joint $\Pr[C_{k+1}=0,D_{k+1}=0\mid A=a]$, not what we want. Author's example with $k_{end}=2$: $\Pr[C_1=0]=1$; $\Pr[D_1=0\mid C_0=0]=0.9$; $\Pr[C_2=0\mid D_1=0,C_1=0]=0.5$; $\Pr[D_2=0\mid C_2=0,D_1=0,C_1=0]=0.9$. Uncensored survivors: $1\times0.9\times0.5\times0.9=0.405$. With no censoring: $1\times0.9\times1\times0.9=0.81$ (p. 233–234).

**Correct estimator (as-if random censoring):**
$$\prod_{m=1}^{k}\Pr[D_m=0\mid D_{m-1}=0,C_m=0,A=a]\quad\text{for }k<k_{end}$$
using a nonparametric estimate of, or a logistic model for, the cause-specific hazard $\Pr[D_{k+1}=1\mid D_k=0,C_{k+1}=0,A=a]$ (p. 234).

If censoring is not as-if random, adjust for baseline calendar time, because later entrants have shorter $k_{end}$ and calendar time may relate to the outcome. Adjust also for other unbalanced baseline prognostic factors, via the g-methods below (p. 234).

*Intuition note.* Censored people are not dead. The hazards use only people who are still observed at each step, which is how the 0.5 "lost" at censoring is not counted as an event.

### 17.4 IP weighting of marginal structural models (p. 234–235)
Quitters are older on average and older people die more, so the crude contrast (76.2% vs 82.0%) is confounded by age (p. 234).

**Counterfactual.** $D_k^{a,\bar c=\bar0}$ is the death indicator at $k$ under treatment $a$ and no censoring, written $D_k^a$. $C_k=0$ is omitted from conditioning from now on, as if censoring were common (p. 234). The causal contrast is $\Pr[D^{a=1}_{k+1}=0]$ vs. $\Pr[D^{a=0}_{k+1}=0]$ for $k=0,\dots,k_{end}-1$. (The text prints "$k=0,2,\dots$", apparently a misprint.)

**Assumptions:** exchangeability within levels of $L$ (Fig. 17.5; $L$ = sex, age, race, education, smoking intensity and duration, physical activity, recreational exercise, weight), positivity, consistency (p. 235).

**Step 1.** Estimate stabilized weights $SW^A$ as in Chapter 12.
- Denominator: $\widehat{\Pr}[A=1\mid L]$ for the treated and $1-\widehat{\Pr}[A=1\mid L]$ for the untreated, from a logistic model.
- Numerator: $\widehat{\Pr}[A=1]$ for the treated and $1-\widehat{\Pr}[A=1]$ for the untreated.
The weights create a pseudo-population in which $L$ is independent of $A$. Here the weights had mean 1 and range 0.33–4.21 (p. 235).

**Step 2.** Fit the hazards model on person-time data with each row weighted by $SW^A$. It estimates the parameters of the marginal structural logistic model (as printed, p. 235):
$$\operatorname{logit}\Pr[D^a_{k+1}=0\mid D^a_k=0]=\beta_{0,k}+\beta_1a+\beta_2a\times k+\beta_3a\times k^2$$
These are the hazards that would be observed if everyone were treated, or everyone untreated. Multiplying over time gives $\Pr[D^a_{k+1}=0]$ (Fig. 17.6).

**Results.** 120-month survival 80.7% (cessation) vs 80.5% (none), difference 0.2% (95% CI −4.1% to 3.7%, 500 bootstrap samples). Curve under treatment was lower for most of follow-up. The maximum difference never exceeded −1.4% (95% CI −3.4% to 0.7%). So there is little evidence of an effect on mortality at any time. Validity needs no misspecification of both the treatment model and the marginal hazards model (p. 235).

*Intuition note.* Weighting makes quitters and non-quitters look alike on $L$, so age no longer makes quitting look deadly. The crude 5.8-point gap (quitters lower) becomes a 0.2-point difference after IP weighting (80.7% vs 80.5%).

### 17.5 The parametric g-formula (p. 236–237)
Under exchangeability, positivity and consistency, the survival under $a$ is the standardized survival (proof in Section 2.3):
$$\Pr[D^a_{k+1}=0]=\sum_l\Pr[D_{k+1}=0\mid L=l,A=a]\Pr[L=l]$$
**Step 1.** Fit a parametric hazards model like 17.2 with $L$ as covariates. If correct, the product
$$\prod_{m=0}^{k}\Pr[D_{m+1}=0\mid D_m=0,L=l,A=a]=\Pr[D_{k+1}=0\mid L=l,A=a]$$
By conditional exchangeability, $\Pr[D_{k+1}=0\mid L=l,A=a]=\Pr[D^a_{k+1}=0\mid L=l]$. This gives conditional curves (e.g., for white men aged 61, college educated, low exercise), but the goal is marginal curves (p. 236).

**Step 2.** Standardize: average the conditional survival over the distribution of $L$, using the Section 13.3 method (expand dataset, outcome model, predict, average), which also works for continuous $L$ (an integral). Result: Fig. 17.7 (p. 236).

**Results.** Curve under treatment lower throughout; maximum difference −2.0% (95% CI −5.6% to 1.8%). 120-month survival 80.4% (cessation) vs 80.6% (none); difference 0.2% (95% CI −4.6% to 4.1%). Little evidence of an effect. IP weighting and g-formula curves are similar but not identical, since they rely on different models: IP weighting needs no misspecification of the treatment model and the unconditional hazards model; the g-formula needs no misspecification of the conditional hazards model (p. 237).

*Intuition note.* IP weighting reshapes the population; the g-formula models the outcome for every covariate pattern and then averages. Both aim at the same causal quantity.

### 17.6 G-estimation of structural nested models (p. 237–240)
**Why different.** Structural nested models model conditional causal contrasts, not the separate means, so they give neither survival nor hazards (p. 237). Options named:
- Structural nested cumulative failure time (CFT) models: log-linear, ratio of risks. Best for rare failure since log-linear models do not cap risk at 1.
- Structural nested cumulative survival time (CST) models: ratio of survival probabilities. Best when survival is rare.
- The more general choice: a structural nested model for the ratio of survival times, the accelerated failure time (AFT) model (p. 237).

**Technical Point 17.2 (p. 238).** For a time-fixed treatment, the (non-nested) structural CFT model is
$$\frac{\Pr[D_k^a=1\mid L,A]}{\Pr[D_k^{a=0}=1\mid L,A]}=\exp[\gamma_k(L,A;\psi)]$$
and CST replaces $D=1$ by $D=0$. The exponent must be 1 (i.e., $\gamma_k=0$) when $A=0$, and when treatment has no effect. Example: $\gamma_k=\psi A$, so $\psi=0$ is no effect, $\psi<0$ benefit, $\psi>0$ harm. A multiplicative model for risk is not one for survival when the effect is non-null, so $\gamma_k$ has a different meaning in each. With continuous time, a CST model is equivalent to a structural additive hazards model. CFT models need a rare-failure assumption for all $L$ values; there they give differentiable, easily solved estimating equations (an advantage over AFT).

**Structural AFT.** $T^a_i$ is individual $i$'s counterfactual survival time. The ratio $T^{a=1}_i/T^{a=0}_i$ is above 1 if treatment is beneficial, below 1 if harmful, and 1 for no effect (p. 237). Assuming the same effect for everyone:
$$T_i^a/T_i^{a=0}=\exp(-\psi_1a)$$
$\psi_1<0$ increases survival time, $\psi_1>0$ decreases it, $\psi_1=0$ means no effect. (The minus sign keeps positive = harm.) With covariate dependence: $T_i^a/T_i^{a=0}=\exp(-\psi_1a-\psi_2aL_i)$, i.e.
$$T_i^{a=0}=T_i^a\exp(\psi_1a+\psi_2aL_i)$$
By consistency, $T_i^{a=0}=T_i\exp(\psi_1A_i+\psi_2A_iL_i)$ (p. 238).

**Limits.** The model is deterministic ($T^{a=0}$ computed without error from $T,A,L$) and rank-preserving (if $T^{a=0}_i<T^{a=0}_j$ then $T^{a=1}_i<T^{a=1}_j$). Rank preservation is implausible, so one should not generally rely on it. It is used here because g-estimation is easier to explain and the procedure is the same for non-rank-preserving models (p. 238–239).

**Without censoring** (model $T_i^{a=0}=T_i\exp(\psi A_i)$): compute candidates $H_i(\psi^\dagger)=T_i\exp(\psi^\dagger A_i)$. Find the $\psi^\dagger$ for which $H_i(\psi^\dagger)$ is independent of $A$ in a logistic model for $\Pr[A=1]$ with $H_i(\psi^\dagger)$ and $L$ as covariates. That is the g-estimate (as in Section 14.5). Directed search methods (e.g., Nelder–Mead) can reduce computation (p. 239).

**With censoring at $K$.** $H_i(\psi^\dagger)$ cannot be computed when $T_i$ is unknown. Restricting to $T_i\le K$ produces selection bias.

**Author's three-type example (60-month randomized experiment, $K=60$; Table 17.1, p. 239).**

| Type | 1 | 2 | 3 |
|---|---|---|---|
| $T^{a=0}$ | 36 | 72 | 108 |
| $T^{a=1}$ | 24 | 48 | 72 |

Randomization makes the groups exchangeable in expectation. Type 1 death is observed under both arms, and type 3 is censored under both. Type 2 death is observed only if $A=1$ (48 < 60 < 72). Using all observed deaths, $A=1$ has types 1 and 2 and $A=0$ has type 1 only. The untreated then have worse prognosis, so treatment looks better than it is. This bias arises when treatment has a non-null effect on survival time (p. 239).

**Fix: artificial censoring (p. 240).** Keep only individuals whose death would have been observed under both treatments ($T^{a=0}_i\le K$ and $T^{a=1}_i\le K$). Here type 2 is excluded. So we exclude those censored ($T_i>K$) and also some with known $T_i\le K$ whose time would exceed $K$ under another treatment. Define $\Delta(\psi)=0$ if excluded, 1 if not, and replace $H(\psi^\dagger)$ by $\Delta(\psi^\dagger)$.

**Technical Point 17.3 (p. 240).** Let $K(\psi)$ be the minimum untreated survival time that could correspond to an individual who died at $K$: $K(\psi)=\inf\{K\exp(\psi A)\}$. For dichotomous $A$: $K(\psi)=K$ if $\psi>0$ or $\psi=0$; $K(\psi)=K\exp(\psi)$ if $\psi<0$. All administratively censored individuals have $\Delta(\psi)=0$ since $H(\psi)\ge K(\psi)$. Some with $T\le K$ also get $\Delta(\psi)=0$. $\Delta(\psi)$ is a function of $H(\psi)$ and $K$. Under conditional exchangeability given $L$, at the true $\psi$ it is conditionally independent of $A$ given $L$. So g-estimation can use $\Delta(\psi)$ in the estimating equation of Technical Point 14.2 (details in Hernán et al 2005).

**Result.** $\hat\psi=-0.047$ (95% CI −0.223 to 0.333). $\exp(-\hat\psi)=1.05$ is interpreted by the author as the ratio of median survival under $a=1$ to that under $a=0$, suggesting little effect of cessation on time to death (p. 240).

**Practical status.** Structural nested (including AFT) models are rarely used. Reasons: little user-friendly software, and search algorithms may not find a unique solution, worse with two or more $\psi$. Published applications use simple AFTs with no effect modification. This is unfortunate because biological knowledge is easier to translate into AFT parameters than into hazards-model parameters, especially for non-deterministic, non-rank-preserving AFTs (p. 240).

## Toy example (ours, not from the text)
100 people, all alive at month 0, no censoring. Deaths: 10 in month 1; 18 in month 2 among the 90 alive; 7 in month 3 among the 72 alive.
- Hazards: $h_1=10/100=0.10$; $h_2=18/90=0.20$; $h_3=7/72\approx0.0972$.
- Survival: $S_1=0.90$; $S_2=0.90\times0.80=0.72$; $S_3=0.72\times(1-0.0972)=0.72\times0.9028=0.65$. Check: $65/100=0.65$. Risk at 3 = $1-0.65=0.35$.
- The hazard rose (0.10 → 0.20) then fell (0.0972) while risk only rose (0.10, 0.28, 0.35).

Now make 36 of the 72 survivors alive at the start of month 3 administratively censored at random. Among the 36 remaining, 3 die, so $h_3=3/36=0.0833$.
- Correct survival: $0.72\times(1-0.0833)=0.72\times0.9167=0.66$.
- Naive fraction of uncensored survivors: $(36-3)/100=0.33$, a joint probability, wrong for survival. The hazard-based answer stays near 0.65 because censored people only drop out of the denominator.

## Concepts
- [[survival-analysis]] (new) — analysis of time to an event, where many event times are unobserved because follow-up ends (p. 227)
- [[administrative-censoring]] (new) — survival time unknown beyond the common end-of-data date; known only to exceed it (p. 227)
- [[hazard-discrete-time]] (new) — $\Pr[T=k\mid T>k-1]$, event probability among those event-free just before $k$ (p. 229)
- [[survival-risk-curves]] (new) — survival $\Pr[T>k]$ and risk $=1-$survival; fixed-time contrasts preferred to hazard ratios (p. 229)
- [[person-time-data]] (new) — "long" format, one row per person-month, with event indicator $D_{k+1}$ (p. 230)
- [[kaplan-meier-estimator]] (new) — nonparametric product of one minus estimated hazards; good when failures are many (p. 230–231)
- [[hazard-ratio-selection-bias]] (new) — time-specific hazard ratios condition on a collider (being alive), so can be non-null with no benefit (p. 231)
- [[competing-events]] (new) — events (e.g., other-cause death) that prevent the event of interest; no handling is fully satisfactory (p. 228)
- [[marginal-structural-model]] (new) — model for counterfactual hazards, fitted here by IP-weighted logistic regression (p. 235)
- [[parametric-g-formula]] (new) — conditional survival from a hazards model, averaged over the distribution of $L$ (p. 236)
- [[structural-nested-aft-model]] (new) — model for ratio of counterfactual survival times, $T^a/T^{a=0}=\exp(-\psi a)$ (p. 237)
- [[rank-preservation]] (new) — ordering of individuals' survival times is the same under both treatments; implausible (p. 238)
- [[artificial-censoring]] (new) — excluding some uncensored individuals so the analysed set is exchangeable (p. 239–240)
- [[assignment-mechanism-ignorability]] — here exchangeability given $L$, positivity, consistency (p. 235)
- [[fork-chain-collider]] — conditioning on $D_1$ opens a path in Fig. 17.3 (p. 231)
- [[confounding-vs-selection-bias]] — age confounds crude quit/death contrast; conditioning on survival or on observed death times causes selection bias (p. 231, 234, 239)

## Canonical instances
- [[nhefs-smoking-cessation]] — 1629 smokers, 120-month follow-up; crude survival 76.2% vs 82.0%, IP-weighted adjusted 80.7% vs 80.5% (g-formula 80.4% vs 80.6%) (p. 227, 229, 235)
- [[naive-censoring-example]] — $1\times0.9\times0.5\times0.9=0.405$ vs $0.81$ (p. 233–234)
- [[three-types-aft-example]] — Table 17.1; dropping unobserved deaths biases the comparison (p. 239)
- [[high-risk-killed-example]] — treatment kills high-risk people; the hazard ratio is below 1 with no benefit for anyone (p. 231)

## Bridges (candidates)
- [same-math] Survival as product of conditional survivals ↔ probability: chain rule of conditional probability — the hazard product is that rule applied to $D_1,D_2,\dots$
- [structural-analogy] Stabilized IP weights ↔ bayesian: reweighting samples from one distribution to represent another (importance weighting) — here treated and untreated reweighted to the covariate distribution.
- [structural-analogy] Parametric g-formula ↔ bayesian: posterior predictive averaging — model outcome given covariates, then average over the covariate distribution.
- [structural-analogy] Hazard-ratio selection bias ↔ survivorship bias (collider conditioning) — conditioning on being alive.

## Questions this raises
- If competing events cannot be handled satisfactorily by any of the listed strategies, what causal estimand should be targeted (the chapter points to separable effects, p. 228)?
- How do these methods change when treatment and confounders vary over time (Part III)?
- How can non-rank-preserving AFT models be estimated when search algorithms may lack a unique solution?
- How sensitive are the IP-weighted and g-formula curves to misspecification of their different models?

## Reading notes
- Printed = pdf − 9 (pdf 236 = printed 227).
- Source notes: the PDF is the online revision dated 2026-08-19, not the 2020 print; chapter lists may differ from older citations.
- Page 235 prints the marginal structural logistic model with $\Pr[D^a_{k+1}=0\mid D^a_k=0]$ on the left, while 17.2 models $\Pr[D_{k+1}=1\mid\cdot]$ (hazard). Reproduced as printed.
- Page 234 prints "$k=0,2,\ldots k_{end}-1$"; probably should read $0,1,2,\ldots$.
- Survival differences at 120 months are printed as "0.2%" in both IP weighting (80.7 vs 80.5) and g-formula (80.4 vs 80.6) results; the sign convention is not stated.
- Technical Point 17.3 text is dense; the "estimating equation" is only referenced to Technical Point 14.2 and not given here.
- Figures were seen but only described by the author's text; numeric curve values are not read off.
- The unit has no exercises.
