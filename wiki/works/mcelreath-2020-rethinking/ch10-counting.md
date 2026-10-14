---
id: mcelreath-2020-rethinking/ch10-counting
work: mcelreath-2020-rethinking
unit: Chapter 10. Counting and Classification
pages: 291-330
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Counting and Classification (binomial, Poisson and other count regressions)

## L0 — One line
Model the counts you actually observed with a binomial or Poisson likelihood and a link function, and then interpret the fitted parameters on the outcome scale through implied predictions, because the parameters themselves sit on a different scale.

## L1 — The gist (≤ 120 words)
Counts, not proportions, are what we observe, and converting them to proportions discards sample size. This chapter shows binomial regression (logit link; known number of trials) and Poisson regression (log link; no known maximum), worked on chimpanzee, UC Berkeley admissions and Oceanic tool data. Because parameters live on the log-odds or log-rate scale, not the outcome scale, the author stresses computing implied predictions, checking absolute as well as relative effects, and comparing models. The chapter also sketches multinomial, geometric, negative-binomial and beta-binomial models.

**Prerequisites:** Gaussian linear regression and priors; the idea of a link function (logit, log); binomial and Poisson distributions; WAIC and model comparison; quadratic (MAP) approximation versus MCMC; odds and log-odds.

## L2 — Key ideas (5–10 bullets)
- Analysing proportions destroys sample size (10/20 and 1/2 are both one-half), so binomial and Poisson regressions model the counts instead (p. 291).
- Binomial GLMs use the logit link; logistic regression (0/1 rows) and aggregated binomial (counts out of $n$) give the same inference, but the log-likelihood value differs (pp. 292, 303, 310).
- Exponentiated logistic coefficients are *relative* effects (proportional odds). They can mislead because the change in probability also depends on the intercept and other predictors (ceiling and floor effects) (pp. 296–297).
- In the UC Berkeley data, the overall "male advantage" (bm = 0.61) changes sign once department intercepts are added (bm = −0.10, interval −0.23 to 0.03, so the interval includes zero). A posterior predictive check, not the posterior itself, exposed the problem (pp. 306–308).
- Poisson GLMs use the log link. An offset, $\log\tau_i$ with $\tau_i$ the exposure, lets counts over different time spans share one model (pp. 312–313, 322).
- Marginal intervals can hide joint effects. In the Oceanic tools model, `bc` and `bpc` each overlap zero, yet their strong negative correlation gives a 95% plausibility of more tools under high contact at log-population 8 (p. 316).
- Centering predictors reduces posterior correlations and makes MCMC more efficient. MAP is not guaranteed to be safe for GLMs, and glm's flat priors can give nonsense under near-perfect separation (pp. 311, 320–321).
- Multinomial models need $K-1$ linear models and are hard to interpret. A multinomial can be refit as Poisson models, and over-dispersed counts call for mixtures (pp. 323–328).

## L3 — Walkthrough

### Introduction (p. 291)
- Converting counts to proportions destroys information about sample size. 10/20 and 1/2 are the same proportion but have very different sample sizes (p. 291).
- The author's remedy is to model the counts, since "No one has ever observed a proportion" (p. 291).
- Parameters in these models are not on the outcome's scale, so interpretation needs extra care (p. 291).
- Two models are worked fully (p. 291):
  - **Binomial regression:** a binary classification where the total of both categories is known.
  - **Poisson regression:** a count with no known maximum. It can be seen as a binomial with a very large maximum and a very small probability per trial.
- Other count regressions are only described at the end of the chapter (p. 291).

### 10.1 Binomial regression (p. 292)
- Notation: $y \sim \text{Binomial}(n,p)$. Here $y$ is a count, $p$ is the probability of success in a trial and $n$ is the number of trials (p. 292).
- Two flavours (p. 292):
  - *Logistic regression*: single-trial rows, outcome 0 or 1.
  - *Aggregated binomial regression*: trials with the same covariates are aggregated, outcome 0 to $n$.
- Both use the logit link, and each can be converted to the other by aggregating or "exploding" the outcome (p. 292).
- A GLM is not guaranteed to have a Gaussian posterior. So each example is fit with `map` (quadratic approximation) and checked against MCMC via `map2stan` (p. 292).

#### 10.1.1 Logistic regression: Prosocial chimpanzees (pp. 292–302)
**Experiment** (pp. 292–293)
- A focal chimpanzee sits at a table with a left and a right lever. Each lever is attached to the two dishes on its own side of the table (one near the focal animal, one at the far end). Pulling it slides them towards opposite ends of the table, delivering their contents to the focal animal and to the far end.
- Both near dishes always hold food. Only one far dish holds food. So both levers feed the focal animal, but only one lever (the *prosocial* option) also feeds the other side.
- Conditions: *partner* (another chimpanzee at the far end) or *control* (empty far end). Counterbalancing treatments alternate which side has the far-end food, to detect handedness.
- The question is whether the focal animal picks the prosocial option more often when a partner is present, i.e. the interaction of condition and option (p. 293).

**Variables** (p. 293)
- `pulled_left` ($L$): 1 if the left lever was pulled.
- `prosoc_left` ($P$): 1 if the left lever was the prosocial option.
- `condition` ($C$): 1 for partner, 0 for control.

**Model m10.3** (p. 293)
$$
\begin{aligned}
L_i &\sim \text{Binomial}(1,p_i)\\
\text{logit}(p_i) &= \alpha + (\beta_P + \beta_{PC} C_i)P_i\\
\alpha,\beta_P,\beta_{PC} &\sim \text{Normal}(0,10)
\end{aligned}
$$
- There is no main effect of $C$. That assumes the main effect of condition is exactly zero, since there is no reason to expect the partner's presence to create a left-pulling tendency (pp. 293–294).
- The priors are very gently regularizing and will be overwhelmed by moderate evidence, so some overfitting is expected (p. 294).
- Two comparison models: intercept only (m10.1, $\text{logit}(p_i)=\alpha$) and prosoc_left only (m10.2, $\text{logit}(p_i)=\alpha+\beta_P P_i$) (p. 294).

**Intercept-only model, interpretation** (p. 294)
- Estimate: $a = 0.32$ (SD 0.09; 5.5% to 94.5%: 0.18 to 0.46), on the log-odds scale.
- Back on the probability scale with the inverse link (the logistic function): $\text{logistic}(0.32)\approx 0.58$, 89% interval 0.54 to 0.61. The chimpanzees had an overall left-lever preference. The author warns that individuals vary a lot in handedness, so this average is misleading (p. 294).

**WAIC comparison** (p. 295)

| model | WAIC | pWAIC | dWAIC | weight |
|---|---|---|---|---|
| m10.2 | 680.6 | 2 | 0.0 | 0.70 |
| m10.3 | 682.4 | 3 | 1.8 | 0.28 |
| m10.1 | 688.0 | 1 | 7.4 | 0.02 |

- The dSE between m10.2 and m10.3 is 0.81, so doubling it would not change their order (p. 295).
- m10.3 fits the sample better but not enough to overcome expected overfitting. The author still does not ignore it, because it reflects the structure of the experiment (p. 295).

**Estimates of m10.3** (p. 296)

| par | mean | SD | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 0.05 | 0.13 | −0.15 | 0.25 |
| bp | 0.61 | 0.23 | 0.25 | 0.97 |
| bpC | −0.10 | 0.26 | −0.53 | 0.32 |

- The interaction is negative with a wide posterior on both sides of zero. So the estimates suggest the chimpanzees did not care much about the partner's presence, but they did prefer the prosocial option (p. 296).

**Relative versus absolute effect** (pp. 296–297)
- *Absolute effect*: the change in the probability of the outcome. It depends on all parameters.
- *Relative effect*: a proportional change. The customary measure for logistic models is the proportional change in odds, $\exp(\text{coefficient})$. Here $\exp(0.61)\approx 1.84$, i.e. odds increase by 84% (p. 296).
- The actual change in probability also depends on the intercept and other predictors. GLMs induce interactions among all variables through ceiling and floor effects (p. 296).
- Example (p. 296): if $\alpha=4$, then $\text{logistic}(4)=0.982$. Adding 0.61 gives $\text{logistic}(4.61)=0.990$. That is under 1% on the absolute scale, despite an 84% increase in odds.
- If the intercept is very negative, probability is near zero, and an 84% odds increase may not lift it off the floor (pp. 296–297).
- The author advises always considering absolute effects, the prediction scale, alongside relative ones (p. 297).

> **Intuition note.** An odds ratio says how much the *odds* are multiplied, but the same multiplication moves a probability a lot near 0.5 and almost nothing near 0 or 1. So a coefficient alone does not tell you how much behaviour changes.

**Model-averaged posterior predictions** (pp. 297–298)
- `ensemble(m10.1, m10.2, m10.3)` mixes predictions weighted by WAIC. Predictions are made for four treatments: prosoc_left/condition = 0/0, 1/0, 0/1, 1/1 (p. 297).
- Figure 10.2: the average predicted probability zig-zags, with more left pulls when the prosocial option is on the left. The partner treatments (last two) are no higher than the control ones. So presence of another animal made little difference (pp. 297–298).
- Individual chimpanzees vary a lot. Four show the same zig-zag, offset towards the right lever. Three prefer left overall, but only one of them pulls left more when the prosocial option is on the left and a partner is present (p. 298).

**Checking the quadratic approximation** (pp. 298–299)
- MCMC (`map2stan`, `iter=1e4`, `warmup=1000`) on m10.3: a 0.05, bp 0.62, bpC −0.11. These are almost exactly the MAP numbers, with n_eff above 3000 and Rhat = 1. The pairs plot is said to confirm a multivariate Gaussian posterior (pp. 298–299).

**Individual intercepts, model m10.4** (pp. 299–302)
- Handedness is a masking variable: four individuals tend to pull right, three pull left, and actor 2 always pulled left (p. 299).
- The model uses a vector of intercepts, one per actor. This is equivalent to dummy variables but more compact, and mirrors later multilevel models (p. 299):
$$
\begin{aligned}
L_i &\sim \text{Binomial}(1,p_i)\\
\text{logit}(p_i) &= \alpha_{\text{actor}[i]} + (\beta_P+\beta_{PC}C_i)P_i\\
\alpha_{\text{actor}},\beta_P,\beta_{PC} &\sim \text{Normal}(0,10)
\end{aligned}
$$
- `actor[i]` means "the value of actor for case $i$". Every element of $\alpha$ gets the same prior (p. 299). It is fit by MCMC because the posterior turns out skewed (p. 299).
- Posterior samples for `a` form a matrix of 2000 rows (samples) × 7 columns (actors) (p. 300).
- Estimates (p. 300): a[1] −0.74, a[2] 10.91 (SD 5.42; 3.45 to 18.37), a[3] −1.05, a[4] −1.05, a[5] −0.74, a[6] 0.21, a[7] 1.83, bp 0.84, bpC −0.13.
- The posterior for a[2] is strongly skewed (Figure 10.3). Actor 2 always pulled left, so any sufficiently large log-odds gives probability near 1, and the data cannot discriminate among them. Only the weak regularizing prior makes the density fall off (pp. 300–301).
- Figure 10.4 (actors 3, 5, 6, 7): the individual intercepts fit each chimpanzee's overall level but do not change the zig-zag pattern across treatments (p. 302).
- The author leaves two loose ends to the practice problems: WAIC for m10.4 and its MAP fit (p. 302).
- Overthinking box: `by(x, list(...), mean)` computes the mean of `pulled_left` for each combination of the three listed variables and returns a 3-dimensional array (pp. 302–303).

> **Intuition note.** Giving each animal its own baseline removes "who is left-handed" from the comparison, but here it did not change the answer about the partner. When data are all one outcome (actor 2), the likelihood is flat over big values, so the prior alone limits the posterior.

#### 10.1.2 Aggregated binomial: Chimpanzees again, condensed (p. 303)
- If the order of pulls does not matter, the data can be condensed to a count of left pulls for each combination of `prosoc_left`, `condition` and `actor` (`aggregate(..., sum)`) (p. 303).
- Actor 1's counts for the four treatments are 6, 9, 5, 10. Actor 2's are all 18, since each animal had 18 trials per treatment (p. 303).
- With `x ~ dbinom(18, p)` and the same linear model as m10.3 (m10.5), the posterior is the same as m10.3's (p. 303).

#### 10.1.3 Aggregated binomial: Graduate school admissions (pp. 304–310)
**Data** (p. 304)
- UCBadmit: 12 rows (6 departments × 2 genders) representing 4526 applications. Counting rows is no longer a sensible measure of sample size.
- Columns: `admit`, `reject`, `applications` (their sum). Here $n_i$ varies by row.

**Model m10.6** (p. 304)
$$
\begin{aligned}
n_{\text{admit},i} &\sim \text{Binomial}(n_i,p_i)\\
\text{logit}(p_i) &= \alpha + \beta_m m_i\\
\alpha,\beta_m &\sim \text{Normal}(0,10)
\end{aligned}
$$
- $m_i$ is a male dummy. m10.7 is the intercept-only comparison (pp. 304–305).
- WAIC: m10.6 = 5954.9 vs m10.7 = 6046.3 (dWAIC 91.5, weight 1 vs 0). The author reads this as "gender matters a lot" (p. 305).
- Estimates: a = −0.83 (0.05), bm = 0.61 (0.06) (p. 305).
- Relative: $\exp(0.61)\approx1.84$ (the author says a male applicant's odds were 184% of a female applicant's).
- Absolute (p. 305): $p_{\text{male}}=\text{logistic}(\alpha+\beta_m)$ and $p_{\text{female}}=\text{logistic}(\alpha)$ were computed from posterior samples. The median difference is 0.141 (95% interval 0.113 to 0.169), i.e. about 14% (pp. 305–306).

**Posterior validation check** (pp. 306–307)
- Figure 10.5 shows poor predictions. Females had a lower admission rate only in departments C and E, yet the model says females should expect a 14% lower chance (p. 306).
- The fit is not a coding mistake. The model answered the question asked: what are the average admission probabilities for females and males across all departments? Males and females apply to different departments, and departments differ in admission rates, so that answer is misleading (pp. 306–307).
- Admission probability declines from department A to F for both genders. Females applied less to A and B (high admission rates) and in large numbers to F (under 10% admitted) (p. 307).
- Inspecting the posterior alone would never have revealed this. A check "outside the fit model" did (p. 307).

**Better question and models** (p. 307)
- New question: what is the average difference in admission probability between females and males *within* departments?
$$
\begin{aligned}
n_{\text{admit},i} &\sim \text{Binomial}(n_i,p_i)\\
\text{logit}(p_i) &= \alpha_{\text{dept}[i]} + \beta_m m_i\\
\alpha_{\text{dept}} &\sim \text{Normal}(0,10),\quad \beta_m \sim \text{Normal}(0,10)
\end{aligned}
$$
- Each department gets its own log-odds $\alpha_{\text{dept}}$, with one common male adjustment $\beta_m$. The code builds a department index 1–6 with `coerce_index`. m10.8 omits `male` and m10.9 includes it (p. 307).

**WAIC with all four models** (p. 308)

| model | WAIC | pWAIC | dWAIC | weight |
|---|---|---|---|---|
| m10.8 | 5200.9 | 6 | 0.0 | 0.56 |
| m10.9 | 5201.4 | 7 | 0.5 | 0.44 |
| m10.6 | 5954.8 | 2 | 753.9 | 0.00 |
| m10.7 | 6046.3 | 1 | 845.4 | 0.00 |

- The author calls m10.8 vs m10.9 "a tie", which gives modest support for some gender effect, even if overfit a little (p. 308).
- m10.9 estimates (p. 308): a[1..6] = 0.68, 0.64, −0.58, −0.61, −1.06, −2.62; bm = −0.10 (SD 0.08; −0.23 to 0.03).
- $\exp(-0.1)\approx 0.9$. A male in this sample has about 90% of a female's odds of admission, comparing within departments (p. 308).
- Figure 10.6: department intercepts capture the variation in overall admission rates (pp. 308–309).
- MCMC (m10.9stan) gives practically identical estimates (e.g. bm −0.10, a[6] −2.64). The author says the quadratic approximation is typically accurate for binomial regression "as long as none of the intercepts are very far from zero" and "none of the predictors are strongly associated with the outcome". It is still worth checking (pp. 308–309).

> **Intuition note.** The first model compared average female and male rates over a mix of departments with very different difficulty. Adding a department intercept compares like with like, and the estimated sign of the gender effect flipped (to −0.10, with an interval that includes zero).

**Rethinking box: Simpson's paradox** (p. 309)
- The author says it is not a paradox: there is no violation of logic, only of the intuition that a population-wide positive association should hold within each department.
- The association between an outcome and a predictor can be nullified or reversed when another predictor is added, and this can repeat indefinitely in a sample. The remedy is to stay skeptical of models. Thinking causally sometimes helps (p. 309).

**Overthinking box: WAIC with aggregated binomials** (pp. 309–310)
- `WAIC` in rethinking splits aggregated binomials into 0/1 trials, because WAIC is computed point by point and the definition of a "point" affects its value.
- DIC and WAIC for an aggregated binomial therefore look very different, though they give similar rankings. The aggregated binomial has a leading coefficient, the multiplicity (number of reorderings of the 0/1 outcomes). It is not a function of the parameters, so it does not change inference, but it changes the log-likelihood and deviance (p. 310).

#### 10.1.4 Fitting binomial regressions with glm (pp. 310–311)
- `glm` fits binomial models, but the author says to be cautious of its flat priors. An aggregated binomial uses `cbind(admit, reject)` as the outcome (p. 310).
- For 0/1 data with the chimpanzee model, `- condition` removes the main effect: `pulled_left ~ as.factor(actor) + prosoc_left * condition - condition` (p. 310).
- `glimmer` turns a formula into a `map`-style model with weakly regularizing default priors (p. 310).
- **Failure example** (pp. 310–311): `y` is 10 zeros then 10 ones, `x` is −1 (nine times) then +1 (eleven times), so they are almost perfectly associated.
  - `glm` returns Intercept −9.13 and slope 11.43, each with SD ≈ 2955. Read naively, this suggests no association.
  - The slope tries to grow very large, where almost any value is as good as any other. The uncertainty is asymmetric and the flat prior does nothing on the high end.
  - `map` with Normal(0,10) priors gives a = −1.73 (2.78) and b = 4.02 (2.78). The uncertainty is still not symmetric, so the quadratic assumption misleads. MCMC samples (pairs plot) are better (p. 311).
- The author's conclusion: "How you fit the model is part of the model", and in principle no GLM is safe for MAP estimation (p. 311).

### 10.2 Poisson regression (pp. 311–322)
**The distribution** (pp. 311–312)
- A binomial with large $n$ and small $p$ has mean $np$ and variance $np(1-p)$, which are approximately equal.
- Example: 1000 monks, each with $p=0.001$ per day of finishing a manuscript. Variance $=1000(0.001)(0.999)\approx 1$.
- Simulation `rbinom(1e5, 1000, 1/1000)` gave mean 0.9968 and variance 0.9928. This special shape is the Poisson distribution. It is useful when the number of trials $n$ is unknown or uncountably large (p. 312).
- For a monastery with an unknown number of monks but an average of 2 manuscripts per day, this single number determines the whole distribution of daily counts (p. 312).

**GLM form** (p. 312)
- $y\sim\text{Poisson}(\lambda)$, with $\lambda$ the expected value. The conventional link is the log:
$$
\begin{aligned}
y_i &\sim \text{Poisson}(\lambda_i)\\
\log(\lambda_i) &= \alpha+\beta x_i
\end{aligned}
$$
- The log link keeps $\lambda_i$ positive. It also implies an exponential relationship between predictors and expected value. Few natural phenomena stay exponential for long, so the author says to check that this makes sense over all ranges of the predictors (p. 312).

**Exposure and offset** (pp. 312–313)
- $\lambda$ is also a rate: $\lambda=\mu/\tau$, with $\mu$ the expected number of events per unit of time or distance and $\tau$ the exposure.
$$
\log\lambda_i = \log\frac{\mu_i}{\tau_i} = \log\mu_i - \log\tau_i = \alpha+\beta x_i
$$
- Rearranging gives $\log\mu_i = \log\tau_i + \alpha + \beta x_i$, so the model is
$$
\begin{aligned}
y_i &\sim \text{Poisson}(\mu_i)\\
\log\mu_i &= \log\tau_i + \alpha + \beta x_i
\end{aligned}
$$
- When $\tau_i=1$, $\log\tau_i=0$. The offset is like adding the log exposure as a predictor without a parameter for it (p. 313).

> **Intuition note.** A longer observation window gives more events in proportion to its length. Adding $\log\tau_i$ lets one rate parameter explain daily and weekly totals together.

#### 10.2.1 Example: Oceanic tool complexity (pp. 313–319)
**Data and hypotheses** (pp. 313–314)
- Kline: 10 Oceanic societies with `population`, `contact` (low/high), `total_tools` (the outcome) and `mean_TU`. Rows are few, so regularization is wanted (p. 313).
- Three ideas (p. 314):
  1. Tools increase with *log* population, because theory says the order of magnitude matters.
  2. Tools increase with contact rate.
  3. The population effect is increased by high contact, i.e. a positive interaction.
- Model m10.10 (`contact_high`: $C$; $P$: population) (p. 314):
$$
\begin{aligned}
T_i &\sim \text{Poisson}(\lambda_i)\\
\log\lambda_i &= \alpha + \beta_P\log P_i + \beta_C C_i + \beta_{PC} C_i\log P_i\\
\alpha &\sim \text{Normal}(0,100),\quad \beta_P,\beta_C,\beta_{PC}\sim\text{Normal}(0,1)
\end{aligned}
$$
- The author notes the Normal(0,1) priors are probably not conservative enough. $\alpha$ gets an essentially flat prior because the predictors are not centered (p. 314).

**Estimates** (p. 315)

| par | mean | SD | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 0.94 | 0.36 | 0.37 | 1.52 |
| bp | 0.26 | 0.03 | 0.21 | 0.32 |
| bc | −0.09 | 0.84 | −1.43 | 1.25 |
| bpc | 0.04 | 0.09 | −0.10 | 0.19 |

- Correlations: a–bp −0.98; bc–bpc −0.99 (p. 315).
- Read naively, `bp` is positive and precise while `bc` and `bpc` overlap zero, which would suggest contact has no effect. The author says this reading is wrong (p. 315).

**Counterfactual check** (pp. 315–316)
- Two islands both at log-population 8, with high versus low contact. Using posterior samples (shapes: each `post$…` is a vector of samples):
  - $\lambda_{\text{high}}=\exp(a+b_c+(b_p+b_{pc})\cdot 8)$
  - $\lambda_{\text{low}}=\exp(a+b_p\cdot 8)$
- Proportion of samples where $\lambda_{\text{high}}-\lambda_{\text{low}}>0$ is 0.9527. That is a 95% plausibility that the high-contact island has more tools (p. 316).
- The reason is correlated uncertainty. `bc` and `bpc` have a strongly negative joint posterior (Figure 10.8), so marginal intervals do not show their joint effect on prediction (p. 316).

> **Intuition note.** A table of marginal intervals treats each parameter as if it moved alone. When two parameters trade off, as `bc` and `bpc` do, predictions (or model comparison) that use both together are needed to see what the data say.

**Model comparison** (pp. 316–318)
- Five models: m10.10 (interaction), m10.11 (no interaction), m10.12 (log-pop only), m10.13 (contact only), m10.14 (intercept only). Compared with `n=1e4` for stable WAIC (p. 317).

| model | WAIC | pWAIC | dWAIC | weight |
|---|---|---|---|---|
| m10.11 | 79.0 | 4.2 | 0.0 | 0.62 |
| m10.10 | 80.1 | 4.9 | 1.2 | 0.35 |
| m10.12 | 84.6 | 3.8 | 5.6 | 0.04 |
| m10.14 | 141.5 | 8.2 | 62.5 | 0.00 |
| m10.13 | 149.8 | 16.7 | 70.8 | 0.00 |

- Interpretation: both top models include both predictors, and the interaction estimate is probably overfit. The set is "decent evidence" that contact rate matters, though much less than log-population. The author warns that model comparison is not divination (p. 318).
- Figure 10.9 (ensemble of the top three models): both trends curve up with log-population. The high- and low-contact predictions overlap, especially at low and high log-population, where no high-contact islands exist (p. 319).

#### 10.2.2 MCMC islands (pp. 319–321)
- MCMC on m10.10 gives the same estimates (e.g. bp 0.27, bc −0.08, bpc 0.04), so the posterior is approximately Gaussian. But the pairs plot shows very strong correlations between two pairs of parameters (Figure 10.10, left). HMC copes, but is less efficient with strong correlations (p. 320).
- **Centering:** `log_pop_c = log_pop − mean(log_pop)` (with prior $\alpha\sim\text{Normal}(0,10)$). New estimates (p. 321):
  - a 3.31 (0.09)
  - bp 0.26 (0.04)
  - bc 0.28 (0.12; 0.09 to 0.47)
  - bcp 0.07 (0.18)
- Estimates change because of centering, but predictions do not. The strong correlations disappear (Figure 10.10, right) and n_eff rises (about 2.1–2.2 thousand before; 2.6–3.8 thousand after). Fewer samples are then needed, which matters for bigger models (pp. 320–321).

#### 10.2.3 Example: Exposure and the offset (pp. 321–322)
- Simulation (pp. 321–322):
  - Old monastery: 30 daily counts, `rpois(30, 1.5)`.
  - New monastery: 4 weekly counts, `rpois(4, 0.5*7)` (true daily rate 0.5, exposure 7).
  - Data frame columns: `y`, `days` (exposure 1 or 7), `monastery` (0 or 1).
- Model m10.15 (p. 322): `log(lambda) <- log_days + a + b*monastery`, with $a\sim\text{Normal}(0,100)$ and $b\sim\text{Normal}(0,1)$.
- Predictions drop the offset, since the parameters are already on the daily scale: $\lambda_{\text{old}}=\exp(a)$, $\lambda_{\text{new}}=\exp(a+b)$.
- Result for the author's simulation: $\lambda_{\text{old}}$ = 1.61 (SD 0.23; 1.26 to 1.99) and $\lambda_{\text{new}}$ = 0.59 (SD 0.14; 0.37 to 0.81). The new monastery produces about half as many per day (p. 322).

### 10.3 Other count regressions (pp. 322–328)
Overview: multinomial, geometric, negative-binomial and beta-binomial. The first two are maximum entropy distributions under their own constraints. The last two are mixtures (treated in the next chapter). The author says full examples are not worked in this section (p. 322).

#### 10.3.1 Multinomial (pp. 323–327)
- Used when more than two unordered event types can occur and each type's probability is constant across trials; it is then the maximum entropy distribution. The binomial is a special case (p. 323). With $K$ types, probabilities $p_1,\dots,p_K$ and $n$ trials:
$$
\Pr(y_1,\dots,y_K\mid n,p_1,\dots,p_K)=\frac{n!}{\prod_i y_i!}\prod_{i=1}^K p_i^{y_i}
$$
- The fraction counts the orderings that give the same counts (p. 323).
- Names: *categorical regression* (one event per row); in machine learning, *maximum entropy classifier* (p. 323).
- Two likelihood approaches: the *explicit* approach (below) and the Poisson transformation (p. 323).

**Explicit models** (pp. 323–325)
- The link is the *multinomial logit*, provided as `softmax`, which maps scores $s_1,\dots,s_K$ to probabilities:
$$
\Pr(k\mid s_1,\dots,s_K)=\frac{\exp(s_k)}{\sum_{i=1}^K\exp(s_i)}
$$
- You need $K-1$ linear models for $K$ event types. They may use different predictors and parameters. With two types there is one linear model, which is why the binomial is easier (pp. 323–324).
- Two basic cases (p. 324):
  1. Predictors differ across event types (traits of each type), with one shared parameter.
  2. Parameters differ across event types (features of the entity producing the event).
- **Case 1** (career choice, simulated, N = 500): `income <- 1:3`, `score <- 0.5*income`, probabilities from `softmax`. Fit (m10.16): `career ~ dcategorical(softmax(0,s2,s3))`, `s2 <- b*2`, `s3 <- b*3`, `b ~ dnorm(0,5)`. The first type is the reference, with constant score 0, and there are no intercepts (pp. 324–325).
- **Case 2** (family income, N = 100): the same predictor appears in each linear model, with a unique coefficient per type. Simulation uses `b <- (1:-1)` (that is, 1, 0, −1) and `score = 0.5*(1:3) + b*family_income[i]`. Fit (m10.17): `s2 <- a2 + b2*family_income`, `s3 <- a3 + b3*family_income`, all priors Normal(0,5) (p. 325).
- Estimates are "extraordinarily difficult to interpret" and swing wildly depending on which type is the reference. Different references give different estimates but the same predictions, so convert to probabilities (p. 325).

**Multinomial in disguise as Poisson** (pp. 325–327)
- A multinomial likelihood can be refactored into a series of Poisson likelihoods. It is justified by the mathematics and is computationally easier (pp. 325–326).
- Example with UCBadmit: `m_binom` has `admit ~ dbinom(applications, p)`, `logit(p) <- a`. `m_pois` has `admit ~ dpois(lambda1)`, `rej ~ dpois(lambda2)`, `log(lambda1) <- a1`, `log(lambda2) <- a2` (p. 326).
- Binomial: $\text{logistic}(a)=0.3878$. Poisson implied probability:
$$
p_{\text{admit}}=\frac{\lambda_1}{\lambda_1+\lambda_2}=\frac{\exp(a_1)}{\exp(a_1)+\exp(a_2)}=0.3880
$$
- The inference is the same (pp. 326–327).

**Overthinking: Multinomial-Poisson transformation** (p. 327). Start from $\Pr(y_1,y_2\mid n,p_1,p_2)=\frac{n!}{y_1!y_2!}p_1^{y_1}p_2^{y_2}$. Let $\Lambda=\lambda_1+\lambda_2$, $p_1=\lambda_1/\Lambda$, $p_2=\lambda_2/\Lambda$:
$$
\Pr(y_1,y_2\mid n,\lambda_1,\lambda_2)=\frac{n!}{y_1!y_2!}\left(\frac{\lambda_1}{\Lambda}\right)^{y_1}\left(\frac{\lambda_2}{\Lambda}\right)^{y_2}=\frac{n!}{\Lambda^{y_1}\Lambda^{y_2}}\frac{\lambda_1^{y_1}}{y_1!}\frac{\lambda_2^{y_2}}{y_2!}=\frac{n!}{\Lambda^n}\frac{\lambda_1^{y_1}}{y_1!}\frac{\lambda_2^{y_2}}{y_2!}
$$
(the last equality uses $y_1+y_2=n$; added step). Multiply and divide by $e^{-\lambda_1}$ and $e^{-\lambda_2}$:
$$
=\frac{n!}{\Lambda^n e^{-\lambda_1}e^{-\lambda_2}}\,\frac{e^{-\lambda_1}\lambda_1^{y_1}}{y_1!}\,\frac{e^{-\lambda_2}\lambda_2^{y_2}}{y_2!}
=\underbrace{\frac{n!}{e^{-\Lambda}\Lambda^n}}_{\Pr(n)^{-1}}\underbrace{\frac{e^{-\lambda_1}\lambda_1^{y_1}}{y_1!}}_{\Pr(y_1)}\underbrace{\frac{e^{-\lambda_2}\lambda_2^{y_2}}{y_2!}}_{\Pr(y_2)}
$$
- The result is the product of the Poisson probabilities $\Pr(y_1)$ and $\Pr(y_2)$ divided by the Poisson probability of $n$. This makes sense because it is a conditional probability. With $k$ types, model $p_1,\dots,p_k$ via Poisson rates and recover $p_i=\lambda_i/\sum_j\lambda_j$ (p. 327).

> **Intuition note.** Independent Poisson counts, once you condition on their total, behave like a multinomial with probabilities proportional to the rates. That is why fitting one rate per category recovers the category probabilities.

#### 10.3.2 Geometric (p. 328)
- Used when the count is the number of events until a terminating event (event history or survival analysis). The probability of that event is constant and the time units are discrete:
$$
\Pr(y\mid p)=p(1-p)^{y-1}
$$
- Here $y$ is the number of time steps until the terminating event and $p$ is its probability per step. It has maximum entropy for unbounded counts with constant expected value (p. 328).
- Simulation: `y <- rgeom(N, prob=logistic(-1 + 2*x))`, with $N=100$. Fit (m10.18): `y ~ dgeom(p)`, `logit(p) <- a + b*x`, $a\sim\text{Normal}(0,10)$, $b\sim\text{Normal}(0,1)$. Estimates: a = −1.00 (0.22), b = 1.75 (0.43) (p. 328).

#### 10.3.3 Negative-binomial and beta-binomial (p. 328)
- If several bags of marbles have different compositions and each set of draws comes from one bag, the blue-marble counts vary more than with a single bag.
- Such processes are *mixtures* of maximum entropy distributions. The two most common generalizations of count GLMs, the beta-binomial and negative-binomial, are mixtures used for *over-dispersed* counts, where variation exceeds what a pure binomial or Poisson process predicts. Details are left to the next chapter (p. 328).

### 10.4 Summary (pp. 328–329)
- Never convert counts to proportions before analysis, because this destroys sample size information. Parameters are on a different scale (log-odds for binomial, log-rate for Poisson), so computing implied predictions is even more important (pp. 328–329).

## Toy example (ours, not from the text)
**1. Proportions hide sample size.** Compare data A = 1 success in 2 trials and data B = 10 successes in 20 trials. Both have proportion 0.5. Likelihood ratio of $p=0.5$ against $p=0.7$ (binomial coefficients cancel in the ratio):
- A: $\dfrac{0.5^1\,0.5^1}{0.7^1\,0.3^1}=\dfrac{0.25}{0.21}\approx 1.19$.
- B: $\left(\dfrac{0.25}{0.21}\right)^{10}$. Since $\ln 1.1905\approx 0.1743$, ten times that is 1.743 and $e^{1.743}\approx 5.7$.
- Data B's likelihood ratio (about 5.7) is far larger than A's (about 1.19), so B is much stronger evidence for 0.5 over 0.7. A regression on proportions would treat A and B alike.

**2. Same odds ratio, different probability change.** Take $\beta=\ln 2\approx 0.693$, so odds double.
- If $\alpha=0$: odds 1 → 2, so $p$ goes from $1/2=0.500$ to $2/3\approx0.667$, a change of 0.167.
- If $\alpha=\ln 9$: odds 9 → 18, so $p$ goes from $9/10=0.900$ to $18/19\approx0.947$, a change of 0.047.
- Doubling the odds is the same relative effect, but the absolute effect is about 3.5 times smaller near the ceiling.

**3. Offset.** A weekly record of 10 manuscripts ($\tau=7$ days) with $\log\mu=\log\tau+a$ and $\mu=10$ gives $a=\log(10/7)$. So $\exp(a)=1.43$ per day, which is directly comparable with a daily rate.

## Concepts
- [[binomial-regression]] (new) — GLM with binomial likelihood for counts out of a known $n$, usually logit link; includes logistic (0/1 rows) and aggregated forms (p. 292)
- [[logit-link-log-odds]] (new) — link mapping probability to log-odds. The inverse link, the logistic, returns probabilities (pp. 292, 294)
- [[proportional-odds-relative-effect]] (new) — $\exp(\text{coef})$ as multiplicative change in odds. It is a relative effect and can mislead without the absolute effect (p. 296)
- [[absolute-vs-relative-effect]] (new) — absolute = change in outcome probability, depends on all parameters; relative = proportional change (p. 296)
- [[aggregated-binomial]] (new) — outcome is a count out of $n_i$ trials per row. Same inference as the exploded 0/1 form, but different likelihood value (pp. 303, 310)
- [[poisson-regression]] (new) — GLM for counts with no known maximum, log link; $\lambda$ is both expected count and rate (p. 312)
- [[log-link-exposure-offset]] (new) — adding $\log\tau_i$ to the linear model so different exposures share one rate parameter (pp. 312–313)
- [[index-variable-vector-of-intercepts]] (new) — one intercept per category via `a[actor]`; equivalent to dummies, precursor of multilevel models (p. 299)
- [[simpsons-paradox]] — association reversed within strata (department); the author says the intuition, not the logic, is violated (p. 309)
- [[quadratic-approximation-map]] (new) — Gaussian approximation to the posterior. Not guaranteed to work for GLMs, so check with MCMC (pp. 292, 298)
- [[centering-predictors]] (new) — subtracting the mean reduces posterior correlations and improves MCMC efficiency (pp. 320–321)
- [[multinomial-softmax-link]] (new) — maps $K$ scores to probabilities $\exp(s_k)/\sum\exp(s_i)$; needs $K-1$ linear models (p. 323)
- [[multinomial-poisson-transformation]] (new) — fitting multinomial probabilities through Poisson rates, $p_i=\lambda_i/\sum_j\lambda_j$ (p. 327)
- [[geometric-distribution]] (new) — $\Pr(y\mid p)=p(1-p)^{y-1}$, events until a terminating event (p. 328)
- [[overdispersion-mixture-counts]] (new) — beta-binomial and negative-binomial as mixtures for variation beyond binomial or Poisson (p. 328)
- Cross-validation / LOO / WAIC — used with ensemble weights to compare models, with the caveat that it is not divination (pp. 295, 318)
- Convergence diagnostics (R-hat, ESS, divergences) — n_eff and Rhat used to check MCMC fits (pp. 298, 321)
- Principle of indifference / maximum entropy — binomial, multinomial and geometric are described as maximum entropy under stated constraints (pp. 292, 323, 328)
- Posterior predictive check — the postcheck of m10.6 revealed the department problem (pp. 306–307)
- Hamiltonian Monte Carlo (HMC/NUTS) — handles correlated posteriors but is less efficient with them (p. 320)

## Canonical instances
- [[chimpanzee-prosociality-experiment]] — logistic regression with interaction and actor intercepts; handedness as a masking variable (pp. 292–302)
- [[ucb-admissions]] — aggregated binomial; department intercepts flip the sign of the estimated gender effect, from +0.61 to −0.10 with an interval that includes zero (pp. 304–309)
- [[oceanic-tool-kits-kline]] — Poisson regression with log population and contact; counterfactual and WAIC analysis (pp. 313–319)
- [[monastery-manuscripts]] — Poisson from binomial; exposure and offset simulation (pp. 311–312, 321–322)
- [[career-choice-simulation]] — multinomial logit with trait predictors and family income (pp. 324–325)
- [[perfect-separation-glm-failure]] — `glm` flat priors give uninformative estimates for near-perfectly associated data (pp. 310–311)

## Bridges (candidates)
- [structural-analogy] Department intercepts and the within-department comparison ↔ causal inference: adjusting for a confounder that changes the sign of an association (Simpson's paradox; the author points to causal thinking, p. 309)
- [same-math] Multinomial = conditioned independent Poissons ↔ probability theory: conditioning independent Poisson counts on their total gives a multinomial (derivation on p. 327)
- [structural-analogy] Vector of intercepts `a[actor]` ↔ hierarchical models: the same indexing structure that multilevel models will use (p. 299)
- [structural-analogy] Marginal intervals overlapping zero but a joint effect on prediction ↔ multicollinearity: correlated parameters (pp. 315–316)

## Questions this raises
- How do the parameters behave when the individual intercepts are partially pooled instead of estimated freely? The author says Chapter 12 builds multilevel models from this structure (p. 299).
- How do the beta-binomial and negative-binomial models handle over-dispersion in practice? The author defers this to the next chapter (p. 328).
- Is the exponential growth implied by the log link plausible for the tool counts at very large populations, such as Hawaii's? (cf. p. 312)
- When do causal assumptions, not just a posterior check, tell us which gender comparison to trust (the author points to causal thinking in the Simpson's paradox box, p. 309)?

## Exercises worth doing
- Ex. 10E3 (p. 329) — turning a logistic coefficient into a proportional change in odds — difficulty: easy
- Ex. 10E4 (p. 329) — why and when Poisson models need an offset — difficulty: easy
- Ex. 10M1 (p. 329) — why the likelihood differs between aggregated and disaggregated binomial data although inference is the same — difficulty: medium
- Ex. 10M5 (p. 329) — what a logit link on a Poisson mean would imply, and when it might make sense — difficulty: hard
- Ex. 10H1 (p. 329) — quadratic approximation versus MCMC for m10.4 (differences and similarities) — difficulty: medium
- Ex. 10H3 (p. 330) — binomial GLM for eagle piracy: interpret, plot predictions as probabilities and counts, test an interaction by WAIC — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 14 (pdf 305 = printed 291). Citations use printed numbers.
- Code uses the `rethinking` interface (`map`, `map2stan`, `precis`, `compare`, `ensemble`, `postcheck`). Output numbers are as printed.
- Misprint: the text says "over 10,000 (1e5) days" (p. 312), but `1e5` is 100,000.
- Table values for m10.6 differ slightly between pages: WAIC 5954.9 on p. 305 and 5954.8 on p. 308.
- The ensemble of "top three models" is said to hold "all of the Akaike weight" (p. 318). The printed weights are 0.62, 0.35 and 0.04, which sum to 1.01 by rounding.
- The centered model uses a parameter named `bcp` while the uncentered one is `bpc`, and its prior on `a` is Normal(0,10), not Normal(0,100) (p. 320).
- The unit contains no chapter-end solutions. Practice problems are at pp. 329–330.
