---
id: hernan-2020-whatif/ch12-ip
work: hernan-2020-whatif
unit: "12 IP weighting and marginal structural models"
pages: 163-174
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# IP weighting and marginal structural models

## L0 — One line
With a model for the probability of treatment given confounders, IP (inverse-probability) weighting builds a pseudo-population without confounding, and a marginal structural model (a model for the mean of the counterfactual outcome) can then be fitted by weighted regression.

## L1 — The gist (≤ 120 words)
How can we estimate the average causal effect of quitting smoking on weight gain from observational data with many confounders? Estimate each person's probability of the treatment they received, using a logistic model. Weight each person by the inverse of that probability (or a "stabilized" version). In the weighted data, treatment is independent of the measured confounders. Then fit a simple weighted regression. Under exchangeability, positivity, consistency and a correct treatment model, the fitted parameters estimate causal effects. The estimated effect is 3.4 kg (unadjusted difference: 2.5 kg). The chapter extends this to continuous treatments, effect modification, binary outcomes, and censoring.

**Prerequisites:** conditional probability; logistic and linear regression; weighted least squares; counterfactual notation $Y^a$; exchangeability, positivity, consistency (Chapters 2–3).

## L2 — Key ideas (5–10 bullets)
- IP weights $W^A=1/f(A|L)$ create a pseudo-population in which $A$ and $L$ are independent. If $Y^a\perp\!\!\!\perp A|L$ holds, association there equals causation (p. 164–165).
- Nonparametric estimation of $\Pr[A=1|L]$ is impossible with many confounders (millions of strata, 1566 people), so a parametric logistic model is used. This gave $\hat\theta_1=3.4$ kg (p. 165–166).
- Stabilized weights $SW^A=f(A)/f(A|L)$ give the same point estimate with a narrower weight range, mean about 1. They typically give narrower confidence intervals, but this advantage can occur only when the weighted model is not saturated (i.e., has fewer parameters than the quantities it estimates) (p. 167–168).
- Positivity violations are structural or random. Parametric models smooth over random zeros, which implicitly assumes random nonpositivity (p. 169).
- A marginal structural model (MSM) is a model for $\mathrm E[Y^a]$. Its treatment parameters correspond to average causal effects, and they are estimated by fitting the corresponding associational model to the weighted data (p. 169–170).
- Continuous treatments need an estimate of a density $f(A|L)$. Effect estimates can be exquisitely sensitive to that model, so this is often dangerous (p. 170–171).
- Covariates $V$ can enter an MSM to assess effect modification. Using $f[A|V]$ in the numerator generally narrows confidence intervals (p. 171–172).
- Censoring is handled by multiplying treatment weights by censoring weights, giving $W^{A,C}$ or $SW^{A,C}$ (p. 172–173).

## L3 — Walkthrough

### Introduction and 12.1 The causal question (p. 163–164)
- Part II asks: what is the average causal effect of smoking cessation on weight gain? Chapter 2 presented IP weighting only nonparametrically. This chapter adds models, which under extra assumptions allow many covariates and non-dichotomous treatments (p. 163).
- Data are from the NHEFS (a US survey with follow-up). The sample is 1566 smokers aged 25–74 with a baseline visit (1971–75) and a follow-up visit about 10 years later (p. 163).
- Treatment: $A=1$ if the person reported quitting before follow-up, else $A=0$. Outcome $Y$ = weight at follow-up minus weight at baseline, in kg (p. 163).
- Associational estimates: $\hat{\mathrm E}[Y|A=1]=4.5$, $\hat{\mathrm E}[Y|A=0]=2.0$. The difference is 2.5 (95% CI 1.7 to 3.4) (p. 163).
- Causal contrast (additive scale): $\mathrm E[Y^{a=1}]-\mathrm E[Y^{a=0}]$, the mean weight difference if everybody were treated versus untreated (p. 163).
- The associational difference generally differs from the causal one. Quitters were on average 4 years older, and older people gained less weight whatever their smoking status. So age is a (surrogate) confounder, and the unadjusted 2.5 might underestimate the causal effect (p. 163–164).
- Table 12.1 shows other baseline differences (e.g., men 54.6% vs 46.6%; cigarettes/day 18.6 vs 21.2 for quitters vs non-quitters) (p. 163).
- The authors assume 9 baseline variables $L$ are sufficient to adjust for confounding: sex, age, race, education (5 categories), cigarettes per day, years smoking, daily-life activity (3 categories), recreational exercise (3 categories), weight (p. 164). Confounder selection is deferred to Chapter 18 (p. 164).
- **Fine Point 12.1 (p. 164).** The example has potential selection bias.
  - Being classified as treated requires answering the 1982 survey, an event after treatment started.
  - If treatment affects selection into the study, selection bias may arise (Chapter 8).
  - A randomized experiment would not have this problem, because assignment happens at baseline. Here the missing data concern the treatment itself, which differs from the outcome censoring in 12.6.
  - $A$ is actually time-varying, which Part II ignores. The authors say this selection bias "can be handled through sensitivity analysis".
  - The authors name this a misalignment of treatment assignment and eligibility at start of follow-up. They ignore it for simplicity and say convenience is no excuse in real life.

### 12.2 Estimating IP weights via modeling (p. 164–166)
- The pseudo-population has two properties: $A$ and $L$ are independent, and $\mathrm E_{ps}[Y|A=a]=\sum_l \mathrm E[Y|A=a,L=l]\Pr[L=l]$ (the standardized mean in the actual population). Both hold even if conditional exchangeability fails (p. 164–165).
- If $Y^a\perp\!\!\!\perp A|L$ does hold, then: (i) $\mathrm E[Y^a]$ is the same in both populations; (ii) unconditional exchangeability holds in the pseudo-population; (iii) $\mathrm E[Y^a]=\mathrm E_{ps}[Y|A=a]$; (iv) association is causation there (p. 165).
- Weights: $W^A = 1/f(A|L)$ (inverse of the probability of the treatment actually received). For binary $A$, the denominator is $\Pr[A=1|L]$ for quitters and $1-\Pr[A=1|L]$ for non-quitters. $\Pr[A=1|L]$ is the propensity score (Chapter 15) (p. 165).
- Section 2.4 estimated $\Pr[A=1|L]$ by counting within strata. Here that fails. Even with at most 6 categories for 8 of the 9 confounders (age left continuous), the tree would have over 2 million branches, and there are only 1566 people (p. 165).
- Model used: logistic regression of quitting on all 9 confounders, with linear and quadratic terms for age, weight, intensity and duration of smoking, and no product terms. This restricts $\Pr[A=1|L]$: on the logit scale each continuous covariate acts through a parabola, and covariate contributions are independent of each other (p. 165). The estimated weights ranged from 1.05 to 16.7, mean 2.00 (p. 165).
- Then fit the saturated model $\mathrm E[Y|A]=\theta_0+\theta_1A$ by weighted least squares, i.e. minimize $\sum_i \widehat W_i[Y_i-(\theta_0+\theta_1A_i)]^2$. With all $\widehat W_i=1$ this is ordinary least squares (p. 165–166). Here $\theta_1=\mathrm E[Y|A=1]-\mathrm E[Y|A=0]$ because the model has 2 parameters for 2 quantities (p. 165).
- If there is no confounding in the pseudo-population and the model for $\Pr[A=1|L]$ is correct, an unbiased estimator of the pseudo-population associational difference is also an unbiased estimator of $\mathrm E[Y^{a=1}]-\mathrm E[Y^{a=0}]$ (p. 165).
- Result: $\hat\theta_1=3.4$ kg (p. 166).
- Confidence intervals must account for the weighting. Three options: derive an analytic variance (needs custom programming); nonparametric bootstrap (computationally heavy); robust variance estimator (standard in software). The robust interval is valid but conservative, meaning it covers the super-population parameter more than 95% of the time. It gave (2.4, 4.5). All IP-weighted intervals in the chapter are conservative (p. 166–167).
- If the model for $\Pr[A=1|L]$ is misspecified, estimates are biased and intervals may cover less than 95% (p. 167).

*Intuition note.* Weighting each person by 1/(probability of the treatment they got) makes under-represented people count more. In the weighted data, who gets treated no longer depends on $L$. A simple weighted comparison then answers the causal question, if the treatment model is right and $L$ is enough.

**Technical Point 12.1 (p. 166).**
- The IP-weighted mean is $\mathrm E\!\left[\frac{I(A=a)Y}{f(A|L)}\right]$. It equals $\mathrm E[Y^a]$ under positivity and exchangeability. The original Horvitz–Thompson estimator is $\hat{\mathrm E}\!\left[\frac{I(A=a)Y}{f(A|L)}\right]$, with $f(A|L)$ assumed known.
- The weighted least squares estimate $\hat\theta_0+\hat\theta_1a$ (binary $A$) is a modified version, the Hajek estimator:
$$\frac{\hat{\mathrm E}\!\left[\frac{I(A=a)Y}{f(A|L)}\right]}{\hat{\mathrm E}\!\left[\frac{I(A=a)}{f(A|L)}\right]}$$
- It is an (asymptotically) unbiased estimator of the corresponding ratio of expectations. Under positivity that ratio equals $\mathrm E\!\left[\frac{I(A=a)Y}{f(A|L)}\right]$, because $\mathrm E\!\left[\frac{I(A=a)}{f(A|L)}\right]=1$.
- It is preferred because, for dichotomous $Y$, it is guaranteed to lie between 0 and 1 even when $f(A|L)$ is replaced by a misspecified model's prediction.
- Without positivity, the ratio equals $\sum_l \mathrm E[Y|A=a,L=l,L\in Q(a)]\Pr[L=l|L\in Q(a)]$. With exchangeability it equals $\mathrm E[Y^a|L\in Q(a)]$, where $Q(a)=\{l;\Pr(A=a|L=l)>0\}$. So the difference of Hajek estimators for $a=1$ vs $a=0$ has no causal interpretation without positivity.
- Under nonpositivity, the ratio of the limits of the Horvitz–Thompson and Hajek estimators is $\Pr[Q(a)]$, not 1.

### 12.3 Stabilized IP weights (p. 167–168)
- The goal is a pseudo-population with no association between $L$ and $A$. With $W^A=1/f(A|L)$ the pseudo-population is twice the study size (mean weight 2), like two copies of the study population, one treated and one untreated (p. 167).
- Weights $0.5/f(A|L)$ give a pseudo-population with $\Pr[A=1]=\Pr[A=0]=0.5$ for everyone. It has the same size as the study population, and is algebraically the previous one with all weights halved. The effect estimate is the same. Likewise for $p/f(A|L)$ with $0<p\le1$ (Technical Point 12.2 has a proof) (p. 167).
- What is required is that the probability of treatment in the pseudo-population does not depend on $L$. People may have different treatment probabilities, as long as these do not depend on $L$ (p. 167).
- Common choice: numerator $\Pr[A=1]$ for the treated and $\Pr[A=0]$ for the untreated, i.e. $SW^A=f(A)/f(A|L)$. These are the **stabilized weights**. $W^A=1/f(A|L)$ are the **nonstabilized weights** (p. 167–168).
- Figure 12.1 applies this to the Chapter 2 data with $\Pr[A=1]=13/20=0.65$, $\Pr[A=0]=7/20=0.35$. Under the identifiability conditions of Chapter 3, the pseudo-population resembles a randomized experiment with 65% assigned $A=1$. To preserve the 65/35 ratio, the number of individuals in each branch cannot be integers (p. 167).
- The mean of $SW^A$ is expected to be 1, because the pseudo-population has the study population's size. Analysts should check that the estimated mean is 1. Deviations indicate model misspecification or violations (or near-violations) of positivity (p. 168).
- Smoking example: $SW^A$ ranged 0.33–4.30 (mean 1.00); $W^A$ ranged 1.05–16.7. The numerator $f(A)$ explains the narrower range (p. 167–168).
- Estimation: denominator from the same logistic model; numerator $\Pr[A=1]$ estimated as 403/1566 (equivalently, a saturated logistic model with intercept only). Fit $\mathrm E[Y|A]=\theta_0+\theta_1A$ weighted by $\widehat\Pr[A=1]/\widehat\Pr[A=1|L]$ (quitters) and $(1-\widehat\Pr[A=1])/(1-\widehat\Pr[A=1|L])$ (non-quitters). Result: $\hat\theta_1=3.4$ kg (95% CI 2.4, 4.5), the same as with $W^A$ (p. 168).
- Why use stabilized weights? They typically give narrower 95% intervals. This advantage can occur only when the weighted model is not saturated. Here the 2-parameter model is saturated because $A$ takes 2 values. In many settings (e.g., time-varying or continuous treatments) the weighted model cannot possibly be saturated, and therefore stabilized weights are used (p. 168–169).

*Intuition note.* Both weights remove the dependence of treatment on $L$. They differ in the size of the pseudo-population and in how extreme the weights are. Stabilized weights are less extreme, which usually means less noisy estimates when the outcome model is not saturated.

**Fine Point 12.2 — Checking positivity (p. 169).**
- In the data, 4 white women aged 66 all did not quit, so $\Pr[A=1|\text{subset of }L]=0$ empirically.
- *Structural violations:* some $L$ values make treatment (or non-treatment) impossible. Example: being off work, when exposure to a workplace chemical is the treatment. In that example, zero cells will always be found when conditioning on being off work.
- *Random violations:* zero cells due to a finite sample after stratifying on several confounders, although the true probability is not 0. Example: 0 treated among white women aged 66 and 67, but some among those aged 65 and 69.
- Consequences: with structural violations, causal inference on the whole population is impossible with IP weighting or standardization. Inference must be restricted to strata where structural positivity holds (see Technical Point 12.1). With random violations, a parametric model smooths over the zeros. The logistic model estimated quitting for white women aged 66 by interpolating from other individuals. Using parametric weights with zero cells, as for $\hat\theta_1=3.4$, effectively assumes random nonpositivity.

### 12.4 Marginal structural models (p. 169–171)
- Model: $\mathrm E[Y^a]=\beta_0+\beta_1a$. Its outcome is counterfactual and generally unobserved, so it cannot be fitted directly to real data. Models for the marginal mean of a counterfactual outcome are **marginal structural mean models** (p. 169).
- Here $\beta_1=\mathrm E[Y^{a=1}]-\mathrm E[Y^{a=0}]$, because $\mathrm E[Y^a]=\beta_0$ at $a=0$ and $\beta_0+\beta_1$ at $a=1$. So earlier sections estimated $\beta_1$ of an MSM (p. 169–170).
- Link: under the assumptions, association is causation in the pseudo-population. So $\theta_1$ of the IP-weighted associational model $\mathrm E[Y|A]=\theta_0+\theta_1A$ has the same causal interpretation as $\beta_1$. A consistent $\hat\theta_1$ is a consistent estimator of $\beta_1$ (p. 170).
- This MSM is saturated: 2 unknowns on each side ($\mathrm E[Y^{a=1}],\mathrm E[Y^{a=0}]$ and $\beta_0,\beta_1$) (p. 170).
- Margin note: MSMs have null preservation (Chapter 9). When the null of no average causal effect is true, an MSM is never misspecified. For example $\mathrm E[Y^a]=\beta_0+\beta_1a+\beta_2a^2$ is then correct with $\beta_1=\beta_2=0$ (p. 170).
- **Continuous treatment.** New treatment $A$ = cigarettes/day in 1982 minus at baseline (values such as −25 or 40). Analysis is restricted to the 1162 individuals who smoked 25 or fewer cigarettes/day at baseline. Goal: $\mathrm E[Y^a]-\mathrm E[Y^{a'}]$ for any $a,a'$. A saturated model is impractical, so a parabola is proposed (p. 170):
$$\mathrm E[Y^a]=\beta_0+\beta_1a+\beta_2a^2$$
- $\mathrm E[Y^{a=0}]=\beta_0$. For $a=20$: $\mathrm E[Y^{a=20}]=\beta_0+20\beta_1+400\beta_2$, so $\mathrm E[Y^{a=20}]-\mathrm E[Y^{a=0}]=20\beta_1+400\beta_2$ (p. 170).
- Procedure: estimate $SW^A$, then fit $\mathrm E[Y|A]=\theta_0+\theta_1A+\theta_2A^2$ in the pseudo-population (p. 170). $SW^A$ ranged 0.19–5.10, mean 1.00 (p. 170).
- Weights need $f(A|L)$, a probability density function (pdf). Pdfs are hard to estimate, especially with high-dimensional continuous $L$, so IP weighting for continuous treatments is often dangerous (p. 170).
- Here: $f(A|L)$ assumed normal with mean $\mu_L=\mathrm E[A|L]$ (linear regression) and constant variance $\sigma^2$ (residual plot looked reasonable). The numerator $f(A)$ was also assumed normal. Other choices (e.g., truncated normal with heteroscedasticity) gave similar estimates (p. 170–171). Effect estimates may be exquisitely sensitive to the density model (p. 171).
- Estimates: $\hat\beta_0=2.005$, $\hat\beta_1=-0.109$, $\hat\beta_2=0.003$. Mean weight gain would be 2.0 kg (1.4, 2.6) with constant smoking intensity and 0.9 kg (−1.7, 3.5) with +20 cigarettes/day. The difference is $0.9-2.0=-1.1$ kg (p. 171).
- **Binary outcome.** For death $D$ by 1992, use the marginal structural logistic model $\operatorname{logit}\Pr[D^a=1]=\alpha_0+\alpha_1a$, where $\exp(\alpha_1)$ is the causal odds ratio. Fit $\operatorname{logit}\Pr[D=1|A]=\theta_0+\theta_1A$ in the IP-weighted pseudo-population. Result: $\exp(\hat\theta_1)=1.0$ (95% CI 0.8, 1.4) (p. 171).

*Intuition note.* An MSM states in one equation how the average outcome would change with treatment level for the whole population. Weighting lets us fit an ordinary regression whose coefficients carry that causal meaning.

### 12.5 Effect modification and marginal structural models (p. 171–172)
- Covariates $V$ (which may be non-confounders) can be added to assess effect modification. For sex $V$ (0 male, 1 female):
$$\mathrm E[Y^a|V]=\beta_0+\beta_1a+\beta_2Va+\beta_3V$$
- Additive effect modification is present if $\beta_2\neq0$. The model is technically no longer marginal, since it conditions on $V$, but is still called an MSM. $\beta_3$ generally lacks a causal interpretation, because exchangeability, positivity and consistency are assumed for $A$, not for $V$ (p. 171).
- Fit $\mathrm E[Y|A,V]=\theta_0+\theta_1A+\theta_2VA+\theta_3V$ by weighted least squares with $W^A$ or $SW^A$. In most settings $L$ should include $V$. Even if $V$ is not needed for exchangeability, including it in $L$ generally increases efficiency (p. 171).
- With a model within levels of $V$, the numerator can be $f[A]$ or $f[A|V]$. The weights $SW^A(V)=f[A|V]/f[A|L]$ generally give narrower intervals. Intuition given: their variance is less than that of $SW^A$. Estimate by adding $V$ to the logistic model for the numerator (p. 171–172).
- Which $V$ to include should only reflect the investigator's substantive interest. For example, $V$ should be included if the investigator both believes $V$ may be an effect modifier and has greater substantive interest in the effect within levels of $V$ than in the entire population (p. 172).
- Example: no strong evidence of modification by sex; the 95% CI for $\hat\theta_2$ was (−2.2, 1.9) (p. 172).
- If all of $L$ is included in the MSM, $SW^A(L)=1$ and IP weighting is unnecessary. Under conditional exchangeability, the MSM is then the unweighted outcome regression (Chapter 15). The authors call this a "faux marginal structural model" (p. 172).
- Teaching remark: in MSMs, confounder adjustment (IP weighting) is separate from effect-modification detection (treatment–covariate product terms), which may help students distinguish the two (p. 172).
- Margin note: for interaction between two treatments $A$ and $B$, include parameters for both and use the joint probability of both treatments in the weight denominator, assuming exchangeability, positivity and consistency for $A$ and $B$ (p. 172).

### 12.6 Censoring and missing data (p. 172–174)
- 63 further eligible individuals lacked a 1982 weight and were excluded, which may introduce selection bias (Chapter 8). Let $C=1$ if weight is unmeasured (censored), $C=0$ otherwise. The analysis really fitted $\mathrm E[Y|A,C=0]=\theta_0+\theta_1A$ (p. 172).
- Even under the null, restricting to $C=0$ is expected to induce bias if $C$ is a collider on a pathway between $A$ and $Y$, or a descendant of one (Figures 8.3–8.6). The data fit this structure: 5.8% of quitters vs 3.2% of non-quitters were censored; mean baseline weight was 76.6 kg in the censored vs 70.8 in the uncensored (p. 172–173).
- Target: the effect had nobody been censored, $\mathrm E[Y^{a=1,c=0}]-\mathrm E[Y^{a=0,c=0}]$, a joint effect of $A$ and $C$ (p. 173).
- Weights: $W^{A,C}=W^A\times W^C$, with $W^C=1/\Pr[C=0|L,A]$ for the uncensored and $W^C=0$ for the censored. Equivalently $W^{A,C}=1/f(A,C=0|L)$, with $f(A,C=0|L)=f(A|L)\times\Pr[C=0|L,A]$ (p. 173).
- Conditions: exchangeability for the joint treatment, $Y^{a,c=0}\perp\!\!\!\perp(A,C)|L$; joint positivity for $(A=a,C=0)$; consistency. If some variables in $L$ are affected by treatment (Figure 8.4), the independence will not generally hold. Part III gives alternative conditions (p. 173).
- $W^C$ creates a pseudo-population of the pre-censoring size, about $1566+63=1629$, with no arrow from $L$ or $A$ into $C$. There is no selection, hence no selection bias. Fit $\mathrm E[Y|A,C=0]=\theta_0+\theta_1A$ with weights $W^{A,C}$ to estimate $\mathrm E[Y^{a,c=0}]=\beta_0+\beta_1a$ (p. 173).
- Stabilized alternative: $SW^{A,C}=SW^A\times SW^C$, with $SW^C=\Pr[C=0|A]/\Pr[C=0|L,A]$. The pseudo-population has the post-censoring size (about 1566 uncensored). Censoring is not removed. It occurs at random with respect to $L$, so there is selection but no selection bias, under conditional exchangeability of censored and uncensored given $L$ (and $A$) (p. 173).
- Estimation: logistic model for $\Pr[C=0|L,A]$ on the 1629 individuals with the same covariates as the treatment model. The estimated $SW^{A,C}$ ranged 0.35–4.09, mean 1.00 (p. 173–174).
- Result: $\hat\theta_1=3.5$ kg (95% CI 2.5, 4.5). It is almost the same as with $SW^A$, which suggests either no selection bias by censoring or that the measured covariates cannot eliminate it (p. 174).
- Margin note: in large samples it is always more efficient to keep all variables independently predicting the outcome in both models. $SW^C$ has mean 1 when the model for $\Pr[C=0|A]$ is correct (p. 173).
- The chapter ends by announcing standardization as an alternative (p. 174).

**Technical Point 12.2 — More on stabilized weights (p. 174).**
- $SW^A=f[A]/f[A|L]$ belongs to the class $g[A]/f[A|L]$, where $g[A]$ is any function of $A$ that is not a function of $L$.
- With unsaturated structural models, $g[A]/f[A|L]$ is preferable to $1/f[A|L]$, because some $g[A]$ (often $f[A]$) give more efficient estimators.
- $\mathrm E\!\left[\frac{g(A)I(A=a)Y}{f(A|L)}\right]$ is no longer $\mathrm E[Y^a]$. But the Hajek version $\mathrm E\!\left[\frac{g(A)I(A=a)Y}{f(A|L)}\right]/\mathrm E\!\left[\frac{g(A)I(A=a)}{f(A|L)}\right]$ does equal $\mathrm E[Y^a]$. Numerator: $g(a)\mathrm E\!\left[\frac{I(A=a)Y}{f(A|L)}\right]=g(a)\mathrm E[Y^a]$. Denominator: $g(a)$.
- The Hajek mean is the solution $u$ of $\mathrm E\!\left[\frac{g[A]}{f[A|L]}(Y-u)\right]=0$.
- In the simplest MSM $\mathrm E[Y^a]=\beta_0+\beta_1a$, the weighted least squares estimators with weights $g[A]/f[A|L]$ solve
$$\hat{\mathrm E}\left\{\frac{g[A]}{f[A|L]}\,[Y-(\beta_0+\beta_1A)]\begin{pmatrix}1\\A\end{pmatrix}\right\}=0.$$
- $\hat\beta_0$ estimates $\mathrm E[Y^0]$ and $\hat\beta_0+\hat\beta_1$ estimates $\mathrm E[Y^1]$. They are the Hajek versions with expectations replaced by sample averages.
- Arguing as in Technical Point 2.2, in the pseudo-population made with $g[A]/f[A|L]$ the mean of $Y$ given $A=a$ still equals $\mathrm E[Y^a]$.

## Toy example (ours, not from the text)
Binary confounder $L$, binary treatment $A$. 200 people: 100 with $L=0$ and 100 with $L=1$. Suppose each person's outcome is $Y=1+2A+4L$, so the true effect is 2.

| Cell | $n$ | $Y$ |
|---|---|---|
| $L=0,A=1$ | 20 | 3 |
| $L=0,A=0$ | 80 | 1 |
| $L=1,A=1$ | 80 | 7 |
| $L=1,A=0$ | 20 | 5 |

- **Crude:** $\mathrm E[Y|A=1]=(20\cdot3+80\cdot7)/100=6.2$. $\mathrm E[Y|A=0]=(80\cdot1+20\cdot5)/100=1.8$. Difference $=4.4$, which is confounded.
- **Propensity scores:** $\Pr[A=1|L=0]=20/100=0.2$ and $\Pr[A=1|L=1]=80/100=0.8$.
- **Nonstabilized weights** $1/f(A|L)$: $L=0,A=1$: $1/0.2=5$. $L=0,A=0$: $1/0.8=1.25$. $L=1,A=1$: $1/0.8=1.25$. $L=1,A=0$: $1/0.2=5$.
- **Pseudo-population cell sizes:** $20\cdot5=100$, $80\cdot1.25=100$, $80\cdot1.25=100$, $20\cdot5=100$. The total is 400, twice 200, so the mean weight is 2. Within each $L$ stratum, treated and untreated are now 50/50, so $A\perp L$.
- **Weighted means:** treated $=(100\cdot3+100\cdot7)/200=5$. Untreated $=(100\cdot1+100\cdot5)/200=3$. Difference $=2$, the true effect.
- **Stabilized weights:** $f(A=1)=100/200=0.5$, so $SW=0.5\times$ the weights above: 2.5, 0.625, 0.625, 2.5. Cell sizes are $50$ each, total 200 and mean weight 1. The weighted means are again 5 and 3, so the difference is again 2.

## Concepts
- [[ip-weighting]] (new) — weight each person by 1/(probability of the treatment received given $L$) to create a pseudo-population where $A\perp L$ (p. 164–165)
- [[pseudo-population]] (new) — the weighted copy of the data in which treatment no longer depends on $L$; association is causation there if conditional exchangeability holds (p. 164–165)
- [[stabilized-ip-weights]] (new) — $f(A)/f(A|L)$, or more generally $g[A]/f[A|L]$; mean expected to be 1; narrower range than $1/f(A|L)$ in the smoking example (p. 167–168, 174)
- [[marginal-structural-model]] (new) — model for the marginal mean of a counterfactual outcome, e.g. $\mathrm E[Y^a]=\beta_0+\beta_1a$; fitted via IP-weighted associational model (p. 169–170)
- [[propensity-score]] — $\Pr[A=1|L]$, the denominator of the weight for binary treatment (p. 165)
- [[assignment-mechanism-ignorability]] — here conditional exchangeability $Y^a\perp\!\!\!\perp A|L$ is what lets association in the pseudo-population be causal (p. 165)
- [[positivity]] (new) — probability of each treatment level is positive within every $L$ stratum; may fail structurally or randomly (p. 169, 166)
- [[hajek-estimator]] (new) — ratio-form weighted mean (what weighted least squares gives for binary $A$), preferred to Horvitz–Thompson (p. 166)
- [[saturated-model]] (new) — model with as many parameters as the quantities estimated (p. 165, 170)
- [[effect-modification]] (new) — treatment effect varying across levels of $V$; in an MSM, tested by a product term (p. 171–172)
- [[censoring-weights]] (new) — $W^C$ or $SW^C$ multiplying treatment weights to remove selection bias from censoring (p. 173)
- [[confounding-vs-selection-bias]] — confounding is handled by treatment weights, selection bias from censoring by censoring weights (p. 172–173)
- [[fork-chain-collider]] — censoring $C$ as a collider (or its descendant) makes restricting to $C=0$ biasing (p. 172)
- [[potential-outcomes]] — $Y^a$ and $Y^{a,c=0}$ as the target quantities (p. 163, 173)
- [[target-trial-emulation]] — mentioned in Fine Point 12.1 for misalignment of assignment and eligibility (p. 164)

## Canonical instances
- [[nhefs-smoking-cessation]] — quitting smoking and 10-year weight gain: 2.5 unadjusted, 3.4 IP-weighted (p. 163, 166)
- [[nhefs-smoking-intensity-msm]] — parabolic MSM for change in cigarettes/day; effect of +20 cigarettes/day is −1.1 kg (p. 170–171)
- [[figure-12-1-stabilized-tree]] — stabilized weights applied to Chapter 2's 20-person data (p. 168)

## Bridges (candidates)
- [structural-analogy] IP weights $1/f(A|L)$ and Hajek ratio ↔ importance sampling: reweighting draws from one distribution to mimic another; the Hajek ratio resembles the self-normalized estimator — the source does not make this link.
- [structural-analogy] Stabilized weights with mean 1 ↔ normalizing constant: dividing by $\mathrm E[g(A)I/f]$ keeps pseudo-population size fixed, like normalizing weights.
- [metaphor] Parametric smoothing over zero cells (random nonpositivity) ↔ partial pooling/shrinkage: sparse strata borrow strength from the model.

## Questions this raises
- How can we tell from data whether the logistic model for $\Pr[A=1|L]$ is adequate, beyond checking that the mean of $SW^A$ is 1?
- How does standardization (the next topic, p. 174) compare to IP weighting in efficiency and in sensitivity to model misspecification?
- If $\mathrm E[Y|A=a]$ in the pseudo-population is only as good as the density estimate $f(A|L)$, what stable alternatives exist (the margin note cites active research, p. 171)?
- What should be done if $L$ includes variables affected by treatment (p. 173, Part III)?

## Reading notes
- Printed page = pdf page − 9 (pdf 172 = printed 163). Pages 163–174 are all covered.
- The metadata says the PDF is an online revision dated 2026-08-19, not the 2020 print version. Chapter numbering and citations may differ from older editions. This was not checked here, as no other edition was given.
- The text layer garbles some math and margin notes, e.g. the "P mean Eps" fragment on p. 164, and the Technical Point equations. Technical Points 12.1 and 12.2 were transcribed from the page images.
- Code references (Programs 12.1–12.7) are only named in margin notes. Program output is not reproduced except the ranges and means quoted.
- The source gives no exercises in this unit, so no exercise list is included.
- Figure 12.1 (p. 168) is a tree diagram. Its branch weights are not transcribed beyond the stabilizing numerators and the proportions stated in the text.
