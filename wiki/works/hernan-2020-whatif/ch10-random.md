---
id: hernan-2020-whatif/ch10-random
work: hernan-2020-whatif
unit: "10 Random variability"
pages: 137-150
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Random variability

## L0 — One line
Even with no systematic bias, finite samples make causal estimates vary by chance. Confidence intervals quantify this only in a frequentist, super-population sense, and the tempting rule "condition on observed covariate imbalance" breaks down when there are many covariates.

## L1 — The gist (≤ 120 words)
Chapters 1–9 assumed study populations of near-infinite size, so only systematic bias (confounding, selection, measurement) mattered. This chapter adds random variability. Estimates change from sample to sample, and Wald confidence intervals (estimate ± 1.96 standard errors) describe this through repeated sampling from an imagined super-population. In a randomized trial, chance can still unbalance a measured covariate. With one covariate, adjusting for it is better, an example of the conditionality principle (infer conditional on ancillary statistics, such as the observed covariate–treatment association). With 100 covariates, the adjusted estimator becomes uninformative and the unadjusted one stays biased conditionally. So conditionality cannot be a universal principle. Technical Point 10.7 adds that, in finite samples, causal discovery needs prior subject-matter knowledge.

**Prerequisites:** proportions and binomial variance; normal quantiles (1.96); risk difference; exchangeability and randomization (earlier chapters); conditional vs marginal association; the idea of repeated sampling.

## L2 — Key ideas
- Two kinds of error: systematic bias and random variability. Earlier chapters treated only the first, as an *identification* problem; real studies also need *estimation* (pp. 137–138).
- A 95% Wald interval is $\hat\theta \pm 1.96\,\widehat{se}$. Its level is a frequency over repeated samples, not the probability that the estimand (the parameter being estimated) lies in this one interval (p. 139).
- "Valid" means coverage at least 95%. The Wald interval is guaranteed only in large samples, and "honest" intervals demand this uniformly over the true parameter (pp. 139–140).
- Under Scenario 1 (the study sample is drawn at random from a near-infinite super-population) the count is binomial. Scenario 2 (no super-population; the same risk $p$ for every treated person) is untenable because individual risks almost certainly differ. So an investigator who reports a binomial interval and admits risk differences implicitly assumes Scenario 1, and, since the super-population is a fiction, such intervals are "what-if" statements (pp. 143–144).
- Randomization gives exchangeability in the super-population, but we do not expect it to hold exactly in a given sample (pp. 140–141). In the example trial, a strong chance association between a measured covariate $L$ and treatment makes the adjusted estimator (which stratifies on $L$) preferable, conditionally and unconditionally (p. 146).
- The conditionality principle says to infer conditional on ancillary statistics (here, the observed association between $L$ and $A$). It matches how researchers treat observed information, but the principle fails for many covariates (pp. 147–149).
- Curse of dimensionality: with $2^{100}$ strata the adjusted interval can be $(-1,1)$, while the unadjusted estimator is still conditionally biased (p. 149).
- Confidence intervals cover random error only. Systematic bias is not shrunk by a larger sample (p. 142). In causal discovery from observational data, finite samples mean validity relies heavily on prior subject-matter knowledge (p. 150).

## L3 — Walkthrough

### Introduction (p. 137)
- Example: a randomized experiment asks whether one person looking up makes pedestrians look up. It has 4 pedestrians, 2 per group. By chance, 1 of the 2 in the "looking up" group is blind and neither in the other group is. The estimated effect is diluted (p. 137).
- Causal inference can go wrong through systematic bias (selection, measurement, unmeasured confounding) or through random variability. Earlier chapters assumed huge study populations and so ignored the second (p. 137).

### 10.1 Identification versus estimation (pp. 137–140)
- Chapters 1–9 treated problems where the study population is effectively infinite, e.g. the 20-person heart transplant study with each person standing for 1 billion identical individuals. Statisticians call these **identification problems**. The identifying conditions are exchangeability, positivity and consistency (p. 137).
- Now suppose the 20 people are a random sample from a **super-population** (a population so large it is effectively infinite) (p. 138).
  - **Estimand:** the super-population parameter of interest, e.g. $\Pr[Y=1|A=a]$.
  - **Estimator:** a rule mapping a sample to a number.
  - **Estimate:** the number for a particular sample. Here $\widehat{\Pr}[Y=1|A=1]=7/13$, a **point estimate**.
  - An estimator is **consistent** if estimates get arbitrarily close to the estimand as the sample size grows. The sample proportion is consistent (p. 138).
- Consistent estimators can still miss badly in small samples. In the absence of systematic biases, statistical theory expresses confidence by a confidence interval, which gets narrower as the study population grows (p. 138).
- **95% Wald interval** (p. 138–139):
  1. Estimate the standard error assuming a random sample from a large super-population.
  2. Add and subtract $1.96\times$ the standard error. 1.96 is the upper 97.5% quantile of the standard normal.
  - For $p=\Pr[Y=1|A=a]$, the standard error is $\sqrt{p(1-p)/n}$, estimated by
$$\widehat{se}=\sqrt{\frac{\hat p(1-\hat p)}{n}}=\sqrt{\frac{(7/13)(6/13)}{13}}=0.138 .$$
  - The interval is $\hat\theta\pm1.96\,\widehat{se}(\hat\theta)$, here 0.27 to 0.81. Its centre and length vary from sample to sample (p. 139).
- **Coverage vocabulary** (p. 139):
  - *Calibrated:* the estimand is inside the interval in 95% of random samples.
  - *Conservative:* it is inside in more than 95%.
  - *Anticonservative:* otherwise.
  - *Valid:* calibrated or conservative for any true parameter value. Among valid intervals, we want the narrowest.
- **Interpretation (frequentist).** If we construct valid 95% intervals in all studies of our lives, the parameters are covered in at least 95% of them, but we cannot tell which studies failed. A single interval does *not* mean a 95% probability that the estimand lies in it, because the estimand is fixed and is either in (0.27, 0.81) or not, so that probability is 0 or 1. The authors adopt the frequency definition of probability. They note that a Bayesian credible interval can be read as "95% probability the estimand is in the interval", with probability meaning degree of belief (p. 139, margin).
- **Small- vs large-sample intervals** (p. 139):
  - A *small-sample valid* interval is valid at all sample sizes for which it is defined. If calibrated, it is "exact".
  - A *large-sample* (asymptotic) valid interval is valid only in large samples.
  - The Wald interval for $p$ is large-sample calibrated but not small-sample valid. It can be badly anticonservative in small samples (Brown et al. 2001, cited in the margin).
  - In this book "95% confidence interval" means a large-sample valid interval unless stated otherwise.
- **Fine Point 10.1 (honest intervals)** (p. 140). The smallest sample size at which a large-sample valid interval actually covers $\ge 95\%$ may depend on the unknown true parameter. An interval is *uniform* or *honest* if some $n$ guarantees coverage $\ge 95\%$ whatever the true parameter. Without uniformity, at any finite $n$ some data-generating distributions may give coverage far below 95%. That smallest $n$ is generally unknown and hard to find even by simulation. Later "valid" means large-sample honest.
- **Bias** (pp. 139–140). Most users call an estimator unbiased if it can center a valid Wald interval and biased if it cannot. For now the book equates bias with that inability. Not all consistent estimators can center a valid Wald interval, even in large samples.
- Confidence intervals quantify only random error. Confidence in them may be excessive when systematic bias is present (p. 140).

**Intuition note.** A confidence interval is a property of the *procedure*. Over many repeated studies a valid 95% procedure captures the truth at least 95% of the time. It does not say how likely the truth is to sit inside your one interval.

**Technical Point 10.1 (bias and consistency)** (p. 141). Observe $n$ i.i.d. copies of a vector whose distribution $P$ lies in a model $\mathcal M$.
- $\hat\theta_n$ is **consistent** for $\theta=\theta(P)$ in $\mathcal M$ if
$$\Pr{}_P\left[|\hat\theta_n-\theta(P)|>\varepsilon\right]\to0\ \text{ as } n\to\infty \text{ for every } \varepsilon>0,\ P\in\mathcal M .$$
- $\hat\theta_n$ is **exactly unbiased** in $\mathcal M$ if $\mathrm E_P[\hat\theta_n]=\theta(P)$ for every $P\in\mathcal M$. The exact bias is $\mathrm E_P[\hat\theta_n]-\theta(P)$. For many parameters, e.g. the risk ratio, no exactly unbiased estimator exists.
- A systematically biased estimator is neither consistent nor exactly unbiased.
- Robins and Morgenstern (1987) argue that most applied researchers call an estimator unbiased only if it can center a valid Wald interval. They show that only **UANU** estimators (uniformly asymptotically normal and unbiased) can do so. $\hat\theta_n$ is UANU in $\mathcal M$ if there exist $\sigma_n(P)$ with, for $t\in\mathbb R$,
$$\sup_{P\in\mathcal M}\left|\Pr{}_P\left[n^{1/2}\left(\hat\theta_n-\theta(P)\right)/\sigma_n(P)<t\right]-\Phi(t)\right|\to0\ \text{ as } n\to\infty,$$
  where $\Phi$ is the standard normal cdf.
- All inconsistent estimators and some consistent ones are biased under this definition. "Unbiased" in the book means UANU.

**Fine Point 10.2 (uncertainty from systematic bias)** (p. 142). Wald interval width reflects only random error. The larger the study population, the smaller the random error as a share of total uncertainty, so the usual interval understates uncertainty more. The stated 95% becomes overconfidence because systematic biases do not shrink with sample size. Some authors therefore call such intervals "compatibility intervals", which is a weaker concept. Quantitative bias analysis aims to give intervals combining random and systematic uncertainty. Bayesian alternatives are cited.

### 10.2 Estimation of causal effects (pp. 140–142)
- Suppose the heart transplant study was a marginally randomized experiment, the 20 people were a random sample of a near-infinite super-population, and everyone in the super-population was randomized and adhered. Then exchangeability holds there: $\Pr[Y^a=1]=\Pr[Y=1|A=a]$. So the causal risk difference equals the associational one in the super-population (p. 140).
- The sample proportion $\widehat{\Pr}[Y=1|A=a]$ is then an unbiased estimator of $\Pr[Y=1|A=a]$ and also of $\Pr[Y^a=1]$ (p. 140).
- "Testing" the causal null $\Pr[Y^{a=1}=1]=\Pr[Y^{a=0}=1]$ becomes comparing $7/13$ and $3/7$. The causal risk difference and risk ratio are estimated by $(7/13)-(3/7)$ and $(7/13)/(3/7)$. Standard methods give intervals for them. Slightly more involved methods do the same for standardized, IP weighted or stratified measures in observational studies (p. 140).
- **Alternative view.** Suppose only the 20 study individuals are randomized. We do not expect exchangeability to hold exactly in the sample. Example: the groups are exchangeable if they contain exactly the same proportion with bad prognosis. By chance, 2 of 13 in $A=1$ and 3 of 7 in $A=0$ may have bad prognosis. With a larger sample the relative imbalance is likely to shrink (p. 141).
- Two inference targets (pp. 141–142):
  1. The sample actually randomized (*randomization-based inference*), which involves technicalities beyond the book.
  2. The super-population the sample was drawn from.
- The second target is mathematically equivalent to the conceptualization at the start of 10.2, in which the whole super-population is randomized: randomization followed by random sampling is equivalent to random sampling followed by randomization (p. 142).
- The first target often does not interest us. The study's purpose is to guide treatment for a larger group similar to the sample, not the participants themselves (p. 142).

### 10.3 The myth of the super-population (pp. 142–144)
- Two sources of randomness: sampling variability and nondeterministic counterfactuals (p. 142).
- Nearly all investigators would report $\hat p\pm1.96\sqrt{\hat p(1-\hat p)/n}$. It is valid only if $\hat p$ has a binomial sampling distribution. This happens in two scenarios (pp. 142–143):
  - **Scenario 1.** The study population is a random sample from an essentially infinite super-population, and the estimand is $p=\Pr[Y=1|A=1]$ there. In repeated samples of 13 treated, the number with the outcome is binomial with success probability $\Pr[Y=1|A=1]$. The Wald interval is then asymptotically calibrated (p. 143).
  - **Scenario 2.** There is no super-population. Each of the 13 treated individuals $i$ has a stochastic counterfactual probability $p_i^{a=1}$, and the observed $Y_i=Y_i^{a=1}$ occurs with that probability. If $p_i^{a=1}$ equals the same $p$ for all 13, the count is binomial($13,p$) and the interval is asymptotically calibrated for $p$ (p. 143).
- Scenario 2 is untenable because $p_i^{a=1}$ will almost certainly vary between individuals (e.g. with genetic make-up). If it varies, the estimand is the average $p$ of the 13 values. The count is then not binomial with success probability $p$, and the interval is conservative rather than calibrated (p. 143).
- Hence an investigator who reports a binomial interval and admits between-individual variation in risk must implicitly assume Scenario 1. Under Scenario 1 the count is binomial whether counterfactuals are deterministic or stochastic (p. 143).
- Why the "myth" endures:
  - (An advantage of the super-population scenario, not given as a reason it endures:) nothing hinges on whether the world is deterministic (p. 143).
  - It leads to simple statistical methods (p. 143).
  - It is the simplest way to generalize findings from the study population to a large target population (p. 143).
- Since the super-population is generally a fiction, a Scenario 1 interval should be read as covering the super-population parameter *had* (often contrary to fact) the study individuals been sampled from it. They are "what-if statements" (p. 144).
- An investigator might reject Scenario 1 if the pool of potential recipients is not much larger than the study population, or if the target population differs from the study population by more than sampling variability can explain. The chapter accepts the super-population from here on (p. 144).

### 10.4 The conditionality "principle" (pp. 144–148)
- **Data (Table 10.1).** Randomized trial of $A$ on 1-year death $Y$; 240 individuals, 120 per arm. Deaths: 24 of 120 treated, 42 of 120 untreated (96 and 78 survivors). Associational risk difference $=\frac{24}{120}-\frac{42}{120}=-0.15$ (p. 144).
- Estimated variance of the unadjusted estimator:
$$\frac{\frac{24}{120}\frac{96}{120}}{120}+\frac{\frac{42}{120}\frac{78}{120}}{120}=\frac{31}{9600}.$$
  The Wald interval is $-0.15\pm(31/9600)^{1/2}\times1.96=(-0.26,-0.04)$, of length 0.22. The investigators publish that treatment is beneficial (p. 144).
- Randomization does not guarantee exact exchangeability in 240 people. It only guarantees that departures are due to random variability, not systematic bias. The uncertainty about chance correlation between unmeasured risk factors and $A$ contributes to the interval's length (p. 144).
- **Smoking data (Table 10.2).** Later the investigators find smoking $L$ was recorded. Treatment frequency is 80/120 among smokers and 40/120 among nonsmokers (twice as high), so the groups are not exchangeable (p. 144).

| | $Y=1$ | $Y=0$ |
|---|---|---|
| $L=1,A=1$ | 4 | 76 |
| $L=1,A=0$ | 2 | 38 |
| $L=0,A=1$ | 20 | 20 |
| $L=0,A=0$ | 40 | 40 |

  The risk difference is 0 in smokers ($4/80=2/40$) and 0 in nonsmokers ($20/40=40/80$). The adjusted analysis suggests no effect, while the marginal $-0.15$ suggested benefit. The Wald interval for the adjusted estimator is $(-0.076,0.076)$ (p. 145, margin; variance in Technical Point 10.5).
- The investigators exclude malfeasance (non-random assignment), so the $L$–$A$ association is bad luck. Two views are argued (p. 145):
  - **First investigator:** do not retract. He says it is likely that imbalances on unmeasured factors $U$ cancelled the effect of the chance imbalance on $L$, so that the unadjusted estimator is still the closer to the true value.
  - **Second investigator:** retract. $L$–$A$ association creates confounding. Within levels of $L$ there are mini randomized trials, and the intervals reflect uncertainty from possible $U$–$A$ associations given $L$.
- **The author's resolution** (pp. 145–146). Suppose the true causal risk difference is constant across strata of $L$, and imagine running the experiment trillions of times. Condition on runs where $L$ and $A$ are as strongly positively associated as observed.
  - Within each level of $L$, the share of runs where any pre-treatment risk factor $U$ is positively associated with $A$ essentially equals the share where it is negatively associated (even if $U$ and $L$ are highly correlated).
  - So over these runs the adjusted estimate is unbiased and the unadjusted estimate is greatly biased.
  - Over *all* runs both are unbiased, but the adjusted has smaller variance. (Margin: adjusted is the maximum likelihood estimator when $L$ data are available.)
  - So from either the conditional or unconditional view the Wald interval centred on the adjusted estimator is better, the article needs retraction, and the second investigator is correct (p. 146).

**Intuition note.** Once you know the groups happen to differ on smoking, the lucky cancellation hoped for by the first investigator is no more likely than the opposite. Adjusting uses the information you actually have.

**Technical Point 10.2 (formal conditionality principle)** (p. 145). Take one dichotomous $L$, exchangeability $Y^a\perp\!\!\!\perp A|L$, and a stratum-specific risk difference $sRD=\Pr(Y=1|L=l,A=1)-\Pr(Y=1|L=l,A=0)$ known to be constant across strata and equal to the parameter of interest. The likelihood is
$$\prod_{i=1}^n f(Y_i|L_i,A_i;sRD,p_0)\,f(A_i|L_i;\alpha)\,f(L_i;\rho),$$
where $p_0=(p_{01},p_{02})$, $p_{0l}=\Pr(Y=1|L=l,A=0)$, and $\alpha,\rho$ are nuisance parameters (parameters not of interest) of the $A|L$ and $L$ densities.
- The data on $A$ and $L$ are **S-ancillary** for the parameter of interest when the conditional distribution of the data given them depends on that parameter, but the joint density of $A,L$ shares no parameters with $f(Y_i|L_i,A_i;sRD,p_0)$.
- The **conditionality principle** states one should always infer about the parameter conditional on any S-ancillary statistic. Here, condition on $\{A_i,L_i;i=1,\dots,n\}$. The same holds if the risk ratio is constant instead.
- An **exact ancillary** is an S-ancillary statistic with known marginal distribution. Here that would require $\alpha$ and $\rho$ known.

**Technical Point 10.3 (approximate ancillarity)** (p. 146). If $sRD_l$ varies over strata, the causal risk difference is identified by
$$RD_{std}=\sum_l\left[\Pr(Y=1|L=l,A=1;\upsilon)-\Pr(Y=1|L=l,A=0;\upsilon)\right]f(l;\rho),$$
with $\upsilon=\{sRD_l,p_{0,l};l=0,1\}$. In unconditionally randomized experiments $RD_{std}$ equals the associational RD because $A\perp\!\!\!\perp L$ in the super-population. Since $RD_{std}$ depends on $\rho$, $\{A_i,L_i\}$ is no longer exactly ancillary, and no exact ancillary exists.
- Let
$$OR_{AL}(\alpha)=\frac{\Pr(A=1|L=1;\alpha)\Pr(A=0|L=0;\alpha)}{\Pr(A=1|L=0;\alpha)\Pr(A=0|L=1;\alpha)},$$
  let $\widehat{OR}_{AL}$ be the same with empirical sample proportions, and
$$\widetilde S=\widehat{OR}_{AL}-OR_{AL},\qquad \widehat S=\widetilde S/\widehat{se}(\widetilde S).$$
  $\widetilde S$ is asymptotically normal with mean 0 given the $L_i$, so its distribution depends on $\alpha$. $\widehat S$ converges to a standard normal and measures the $A$–$L$ association on a standardized scale (e.g. $\widehat S=2$ is two standard deviations above 0).
- When the true $OR_{AL}$ is known, $\widehat S$ is an **approximate (large-sample) ancillary**. For a randomized experiment with $OR_{AL}=1$: (i) $\widehat S$ is computable from data, i.e. $(\widehat{OR}_{AL}-1)/\widehat{se}(\widetilde S)$; (ii) its distribution is approximately known; (iii) the likelihood factors into $f(A|L;\alpha)$ and a term not depending on $\alpha$; (iv) given $\widehat S$, the adjusted estimate of $RD_{std}$ is unbiased and the unadjusted is biased. Any other statistic of $A$–$L$ association, e.g. $\widehat{\Pr}(A=1|L=1)/\widehat{\Pr}(A=1|L=0)-1$, can replace $\widetilde S$.
- **Continuity principle** (Buehler 1982): inferences should not change discontinuously after an arbitrarily small known change in the data-generating distribution. Accepting both principles implies conditioning on an approximate ancillary. Otherwise, with $OR_{AL}=1$ known, one would call the unadjusted estimate biased when $sRD_l$ is constant but unbiased when it is almost constant. A researcher who always conditions on exact and approximate ancillaries follows the **extended conditionality principle**.

**Technical Point 10.4 (adjusted vs unadjusted)** (p. 147). The adjusted estimator is the parametric MLE $\widehat{RD}_{MLE}$ (population proportions in $RD_{std}$ replaced by sample proportions). The unadjusted one is $\widehat{RD}_{UN}=\widehat{\Pr}(Y=1|A=1)-\widehat{\Pr}(Y=1|A=0)$. Unconditionally both are asymptotically normal and unbiased for $RD_{std}$, with asymptotic variances $aVar$.
- Robins and Morgenstern (1987): $\widehat{RD}_{MLE}$ has the same asymptotic distribution given $\widehat S$ as unconditionally, so $aVar(\widehat{RD}_{MLE})=aVar(\widehat{RD}_{MLE}|\widehat S)$. Also
$$aVar(\widehat{RD}_{MLE})=aVar(\widehat{RD}_{UN})-\left[aCov(\widehat S,\widehat{RD}_{UN})\right]^2 .$$
- So $\widehat{RD}_{UN}$ is unconditionally inefficient iff $aCov(\widehat S,\widehat{RD}_{UN})\neq0$. Its conditional asymptotic bias is $a\mathrm E[\widehat{RD}_{UN}|\widehat S]-RD_{std}=aCov(\widehat S,\widehat{RD}_{UN})\,\widehat S$. Hence it is conditionally biased iff it is unconditionally inefficient.
- $aCov(\widehat S,\widehat{RD}_{UN})=0$ iff $L\perp\!\!\!\perp Y|A$. So when data on a measured risk factor for $Y$ exist, $\widehat{RD}_{MLE}$ is preferred. The estimator $\widehat{RD}_{UN}-aCov(\widehat S,\widehat{RD}_{UN})\widehat S$ corrects the bias and has the same asymptotic distribution as $\widehat{RD}_{MLE}$ given $\widehat S$.

**Technical Point 10.5 (researchers follow extended conditionality)** (p. 148). With $sRD$ constant over strata of dichotomous $L$, the estimated variance of the MLE of $sRD$ is $\widehat V_0\widehat V_1/(\widehat V_0+\widehat V_1)$, where $\widehat V_l$ estimates the variance of $\widehat{RD}_l$. Two choices for $\widehat V_1$ from Table 10.2:
$$\widehat V_1^{obs}=\frac{\frac{4}{80}\frac{76}{80}}{80}+\frac{\frac{2}{40}\frac{38}{40}}{40}=1.78\times10^{-3},\qquad \widehat V_1^{exp}=\frac{\frac{4}{80}\frac{76}{80}}{60}+\frac{\frac{2}{40}\frac{38}{40}}{60}=1.58\times10^{-3}.$$
- They differ only in the denominators: the observed counts (80 and 40) versus the expected count 60 given $A\perp\!\!\!\perp L$. $\widehat V_1^{obs}$ is based on observed information, $\widehat V_1^{exp}$ on expected information.
- The authors say nearly all researchers choose $\widehat V_1^{obs}$. By results of Efron–Hinkley (1978) and Robins–Morgenstern (1987), conditional and unconditional variance of $\widehat{RD}_l$ differ by order $n^{-3/2}$. The observed-information estimator is within less than $n^{-3/2}$ of the conditional variance, and the expected-information one is within less than $n^{-3/2}$ of the unconditional variance. So preferring $\widehat V_1^{obs}$ implies preferring conditional inference (p. 148).
- (Added step, checked: with $\widehat V_0=0.25/40+0.25/80=0.009375$ for $L=0$ and $\widehat V_1^{obs}=0.001781$, $\widehat V_0\widehat V_1/(\widehat V_0+\widehat V_1)\approx1.50\times10^{-3}$, so $1.96\sqrt{\cdot}\approx0.076$, matching the margin interval on p. 145.)

- **Back in the text** (p. 147). The idea of conditioning on the observed $L$–$A$ association is the **conditionality principle**. The observed association is an ancillary statistic for the causal risk difference. Some investigators followed it intuitively. They call an estimator biased if it cannot center a valid Wald interval *conditional on ancillary statistics*, which is stricter than the earlier definition.
- **Frequentist objection:** "Adjustment for L is unnecessary because unconditionally... the unadjusted estimate is unbiased." **Reply of conditionality followers:** "Why should the various L-A associations in other hypothetical studies affect what I do in my study?" The text says this is convincing for randomized and observational studies as long as the number of measured confounders is not large. When it is large, strictly following the principle is no longer wise (p. 147).

**Intuition note.** Conditioning means judging the estimator only among studies that look like yours (same observed imbalance). With one covariate, this gives a clear verdict: adjust.

### 10.5 The curse of dimensionality (pp. 148–149)
- Earlier derivations assume few strata of $L$ relative to the sample size. Now suppose 100 binary pre-treatment variables, so $L=(L_1,\dots,L_{100})$ has $2^{100}$ strata ("high dimensionality"). Assume no additive effect modification: the super-population risk difference given $L=l$ is constant across strata, and equals 0 (p. 148).
- The investigators now agree to follow conditionality, since the unadjusted $-0.15$ is conditionally biased. But the adjusted interval is much wider than the unadjusted one, the opposite of the two-strata case, and may be completely uninformative (p. 148).
- Reason: $2^{100}\gg240$, so at most a few strata contain both a treated and an untreated person. Suppose just one stratum contains one treated and one untreated individual. The empirical risk difference there could be $-1$, $0$ or $1$, so the adjusted 95% interval is $(-1,1)$. The unadjusted interval stays $(-0.26,-0.04)$ because its width is unaffected by covariates measured (p. 149).
- The adjusted estimator is only guaranteed more efficient than the unadjusted when the ratio of individuals to unknown parameters is large. A frequently used rule of thumb is a ratio of at least 10, but the minimum depends on the data (p. 149).
- **Curse of dimensionality:** conditional on all 100 covariates, the marginal estimator is still biased and the conditional estimator is uninformative. Since conditionality cannot be carried through for high-dimensional models, it should not be raised to a principle. The same applies to observational studies. Chapter 18 reviews research on solutions and Chapters 11–17 give background (p. 149).

**Technical Point 10.6 (can it be reversed?)** (p. 149).
- Given the exact ancillary $\{A_i,L_i\}$, informative conditional inference for the common risk difference is impossible with high-dimensional $L$ whatever the estimator.
- Unconditionally in marginally randomized experiments, $\widehat{RD}_{UN}$ is unaffected by the dimension of $L$. It stays unbiased and its Wald interval width is proportional to $1/n^{1/2}$. It relies on prior information the MLE does not use, so it is unbiased for the common risk difference only if it is known that $A\perp\!\!\!\perp L$ in the super-population.
- Even unconditionally, intervals from the MLE stay uninformative. Whether data on $L$ can yield an unconditionally unbiased estimator more efficient than the unadjusted is left open. Chapter 18 shows this is sometimes possible.

**Intuition note.** An adjusted estimate needs many people within each stratum. With more strata than people, almost every stratum has only one arm, and the adjusted comparison has almost no data to learn from.

### Technical Point 10.7: Random variability and causal discovery (p. 150)
- Setting: variables $Z$, then $A$, then $Y$ in time order. The empirical odds ratio of $Y$ and $Z$ is 1 at every level of $A$, and all other odds ratios are far from 1. By Fine Point 6.3 (not in this unit), if $Z\perp\!\!\!\perp Y|A$ in the super-population (requiring infinite data) and faithfulness holds, the only possible diagram is $Z\to A\to Y$, possibly with a common cause $U$ of $Z$ and $A$. Then $\mathrm E[Y|A=1]-\mathrm E[Y|A=0]$ is the average causal effect of $A$ on $Y$ (p. 150).
- **Frequentist result** (Robins et al. 2003): inference based on faithfulness is *non-uniform*. For any $n$, even if the empirical odds ratios are 1 at every level of $A$, faithful distributions exist where (a) the true conditional odds ratios are so close to 1 that empirical ones of 1 are unsurprising, and (b) the average causal effect of $A$ on $Y$ is zero. So no honest 95% frequentist interval can exclude 0, even when the empirical risk difference is large (say 0.2, 30 standard errors) (p. 150).
- **Advocates of causal discovery** may reply that a Bayesian with priors not depending on sample size who believes in faithfulness will generally get a 95% highest-posterior-density credible interval nearly centred on the empirical risk difference. Its width is not much greater than the standard error, so it excludes 0 whenever graphs with $Z$ and $Y$ d-separated by $A$ get non-negligible prior probability (p. 150).
- **Authors' view:** the gap arises because Bayesian inference here can be very sensitive to the prior. Many epidemiologists, including the authors, would give essentially zero prior to any diagram lacking a common cause of $A$ and $Y$ in an observational study. A Bayesian sharing this belief may get (depending on other prior aspects) a much wider interval centred much closer to 0.
- Conclusion: in finite samples, even under faithfulness, data alone cannot distinguish $Z\to A\to Y$ (with $Z\perp\!\!\!\perp Y|A$ in the super-population) from a diagram where $Z$ is almost independent of $Y$ given $A$. Causal discovery from observational data depends heavily on prior subject-matter knowledge about plausible diagrams (p. 150).

## Toy example (ours, not from the text)
Aim: show that a Wald interval is a statement about repeated samples, and can fail in small samples.

Suppose the true $p=0.5$ and $n=10$. Each sample gives $k$ successes, $\hat p=k/10$, and interval $\hat p\pm1.96\sqrt{\hat p(1-\hat p)/10}$.
- If $k=4$: $\hat p=0.4$, $\widehat{se}=\sqrt{0.24/10}=\sqrt{0.024}=0.1549$, half-width $=1.96\times0.1549=0.3036$, interval $(0.096,0.704)$. It happens to contain 0.5, but the 95% is not the probability for this interval.
- Which $k$ give intervals containing 0.5?
  - $k=3$: $\hat p=0.3$, $\widehat{se}=\sqrt{0.21/10}=0.1449$, half-width 0.284. $|0.3-0.5|=0.2\le0.284$: covers.
  - $k=2$: $\hat p=0.2$, $\widehat{se}=\sqrt{0.16/10}=0.1265$, half-width 0.248. $0.3>0.248$: misses.
  - $k=0,1,9,10$ also miss, by the same kind of calculation. $k=0$ and $k=10$ give $\widehat{se}=0$. By symmetry $k=7$ covers and $k=8$ misses.
  - Covering values: $k=3,\dots,7$.
- Probability of coverage: $\frac{\binom{10}{3}+\binom{10}{4}+\binom{10}{5}+\binom{10}{6}+\binom{10}{7}}{2^{10}}=\frac{120+210+252+210+120}{1024}=\frac{912}{1024}=0.891$.

So at $n=10$ the "95%" interval covers only about 89% of the time (anticonservative). Coverage approaches 95% only as $n$ grows, which is what "large-sample calibrated" means (pp. 138–139).

## Concepts
- [[identification-vs-estimation]] (new) — identification: effects computable if the population were infinite; estimation: dealing with finite-sample random variability (p. 137)
- [[estimand-estimator-estimate]] (new) — parameter of interest; rule mapping data to a number; the number for one sample (p. 138)
- [[consistent-estimator]] (new) — estimates get arbitrarily close to the estimand as $n$ grows; formal definition in Technical Point 10.1 (pp. 138, 141)
- [[confidence-interval]] (new) — interval whose level is coverage frequency over repeated samples; Wald form $\hat\theta\pm1.96\,\widehat{se}$ (pp. 138–139)
- [[valid-honest-interval]] (new) — valid: coverage ≥ 95%; honest: guaranteed uniformly over true parameter values (pp. 139–140)
- [[bias-as-uanu]] (new) — "unbiased" means able to center a valid Wald interval (UANU) (pp. 139–141)
- [[super-population]] (new) — imagined near-infinite population from which the study sample is randomly drawn; the author calls it a fiction (pp. 138, 143–144)
- [[frequentist-vs-bayesian-inference]] — here: a frequentist interval's level is a long-run coverage frequency; a Bayesian credible interval would mean degree of belief (p. 139)
- [[credible-interval]] — mentioned as an interval with "95% probability the estimand is in it" for a Bayesian (p. 139); highest posterior density intervals in Technical Point 10.7 (p. 150)
- [[assignment-mechanism-ignorability]] — randomization yields exchangeability in the super-population, but only approximate exchangeability in a sample (pp. 140–141)
- [[conditionality-principle]] (new) — infer conditional on (S-)ancillary statistics such as the observed $A$–$L$ association (pp. 145, 147)
- [[ancillary-statistic]] (new) — S-ancillary: the data's distribution given the statistic depends on the parameter of interest, while the statistic's own density shares no parameters with it; exact (known marginal distribution) vs approximate (pp. 145–146)
- [[curse-of-dimensionality]] (new) — with many strata, conditional estimators become uninformative while marginal ones stay conditionally biased (p. 149)

## Canonical instances
- [[pedestrians-looking-up]] — small randomized study where chance puts the blind pedestrian in one arm; illustrates random variability (p. 137)
- [[heart-transplant-20-person-study]] — 7/13 treated died; point estimate and Wald interval 0.27–0.81 (pp. 138–139)
- [[randomized-trial-tables-10-1-10-2]] — marginal risk difference $-0.15$ vs stratum-specific 0; motivates adjustment (p. 144)
- [[100-covariate-trial]] — $2^{100}$ strata; adjusted interval $(-1,1)$ (p. 149)

## Bridges (candidates)
- [structural-analogy] Wald confidence interval (coverage over repeated samples) ↔ Bayesian: credible interval (probability statement given data and prior) — same-looking intervals with different meanings, as the chapter itself notes (p. 139).
- [structural-analogy] Sensitivity of Bayesian causal-discovery intervals to the prior (Technical Point 10.7) ↔ Bayesian: prior sensitivity / prior predictive checks — prior choice drives conclusions when data cannot discriminate.
- [metaphor] Adjusted estimator with too many strata ↔ Bayesian: partial pooling/shrinkage — the problem of sparse strata is what pooling addresses, but the chapter does not discuss it.
- [structural-analogy] Conditioning on observed covariate imbalance (conditionality) ↔ Bayesian: conditioning on observed data — both judge procedures by what was actually observed.

## Questions this raises
- If the super-population is a fiction, what exactly does a confidence interval from a real study tell its users, beyond a "what-if" statement?
- Where is the line between a small number of covariates (where conditionality helps) and a large number (where it fails)?
- Can an estimator use data on $L$ and still be unconditionally unbiased and more efficient than the unadjusted one? (Chapter 18 is said to show this is sometimes possible.)
- How could a Bayesian analysis handle both random error and the systematic biases that confidence intervals ignore (Fine Point 10.2)?

## Reading notes
- Source is the online revision dated 2026-08-19, not the 2020 print version. Chapter cross-references may differ from older citations.
- Printed page = pdf page − 9 (pdf 146 = p. 137).
- Page images were consulted for all equations. The text layer garbles the math in Technical Points 10.1–10.5; I followed the images.
- Technical Point 10.3 prints $\widehat S=(\widehat{OR}_{AL}-1)/\widehat{se}(\widetilde S)$ in the text layer with a stray symbol. I followed the image.
- Margin note on p. 144 gives the unadjusted variance; the adjusted interval $(-0.076,0.076)$ appears only as a margin note on p. 145. The (added step) calculation in Technical Point 10.5 is ours.
- The unit has no exercises.
