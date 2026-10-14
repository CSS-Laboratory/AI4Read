---
id: gelman-2013-bda3/ch05-hierarchical
work: gelman-2013-bda3
unit: "5 Hierarchical models"
pages: "101-138"
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: "2026-10-14"
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# 5. Hierarchical models

## L0 — One line
When several related groups each need their own parameter, a hierarchical model ties the group parameters together through a shared population distribution with unknown hyperparameters, so each group's estimate is pulled ("shrunk") toward the others by an amount the data themselves determine.

## L1 — The gist (≤ 120 words)
When you have many related experiments or groups (hospitals, schools, rat colonies, clinical trials), should you analyze each separately, or pool them into one? Both extremes are usually wrong: separate analysis overfits noisy small samples; full pooling denies real differences. Gelman et al. treat the group parameters as *exchangeable* draws from a common population distribution with unknown hyperparameters, then do full Bayesian inference over both levels at once. The result is automatic **partial pooling**: noisy, small, or extreme groups shrink more toward the overall mean than precise ones, and the degree of shrinkage — and its uncertainty — is learned from the data, not fixed in advance.

**Prerequisites:** Bayes' theorem; conjugate priors (beta-binomial, normal-normal); basic multiparameter Bayesian computation (Ch. 3); grid approximation; normal and beta distributions.

## L2 — Key ideas
- **Exchangeability, not independence, justifies a common prior.** If nothing but the data distinguishes the groups, their parameters must be modeled symmetrically — exchangeably — which licenses treating them as a sample from a shared population distribution (p. 104–105).
- **A hierarchical model has (at least) two levels**: a sampling model for data given group parameters $\theta_j$, and a population (prior) model for the $\theta_j$'s given hyperparameters $\phi$, which itself gets a hyperprior $p(\phi)$ (p. 107).
- **Point-estimating the hyperparameters (quasi-"empirical Bayes") understates uncertainty**; a full Bayesian treatment of $\phi$ gives larger, more honest posterior variance for each group (p. 103–104, 112).
- **Computation factors as $p(\phi\mid y)$, then $p(\theta\mid\phi,y)$**, via the identity $p(\phi\mid y) = p(\theta,\phi\mid y)/p(\theta\mid\phi,y)$, usable in closed form for the conjugate beta-binomial and normal cases treated here (p. 109).
- **The eight-schools example** shows that neither separate estimates nor complete pooling is defensible, and that conditioning on a single point estimate of the between-group variance $\tau$ (e.g. its mode, often 0) over-pools (p. 119–122).
- **Meta-analysis is a hierarchical model** across studies: the overall mean, an observed study's effect, and the effect in a hypothetical new study are three different estimands with different, increasing uncertainty (p. 125–128).
- **"Noninformative" priors for a variance parameter $\tau$ are not innocuous**: the choice can dominate the posterior, especially when the number of groups $J$ is small; weakly informative priors (e.g. half-Cauchy) are proposed as a practical remedy (p. 128–132).

## L3 — Walkthrough

### 5.1 Constructing a parameterized prior distribution
**Example: tumor risk in rats.** The goal is to estimate $\theta$, the probability of tumor in control-group rats, from a current experiment (4 tumors out of 14 rats) plus historical data from 70 similar experiments (Table 5.1). With a conjugate $\text{Beta}(\alpha,\beta)$ prior, the binomial likelihood gives a $\text{Beta}(\alpha+4,\beta+10)$ posterior (p. 102).

If $(\alpha,\beta)$ were known from historical information this would be immediate; in practice they must be estimated. The sample mean and SD of the 70 historical ratios $y_j/n_j$ are $0.136$ and $0.103$; matching these to beta moments (Appendix A, eq. A.3) gives the point estimate $(\alpha,\beta)=(1.4,8.6)$ — "not a Bayesian calculation because it is not based on any specified full probability model" (p. 103). Using this as a fixed prior for the current experiment gives a $\text{Beta}(5.4,18.6)$ posterior, mean $0.223$, SD $0.083$ — substantially lower than the crude ratio $4/14=0.286$, because the historical experience "indicates that the number of tumors in the current experiment is unusually high" (p. 103).

The author lists logical problems with this two-step procedure: (1) if the same prior were then used to analyze the 70 historical experiments too, the data would be used twice, seemingly overstating precision; (2) a point estimate of $(\alpha,\beta)$ ignores posterior uncertainty about them; (3) one may ask whether it even makes sense to "estimate" prior parameters at all — since they are part of the prior distribution, should they not be known before the data are gathered, according to the logic of Bayesian inference? (p. 103–104).

**Logic of combining information.** A thought experiment: two experiments ($j{=}26,27$) each show 2/20 tumors, prior centered at 0.15. Learning that $\theta_{26}=0.1$ should lower your estimate of $\theta_{27}$ too, because they share the same data pattern — so $\theta_{26}$ and $\theta_{27}$ should be dependent in the posterior, not analyzed separately (p. 104). The resolution: put a full probability model on *all* parameters and experiments jointly and do one Bayesian analysis. The author calls the point-estimate shortcut "empirical Bayes" but prefers to avoid that term, since it misleadingly implies the full hierarchical method is not itself "empirical" (p. 104).

*Intuition note:* Historical data from similar experiments is not wasted information — it tells you how spread out tumor risks typically are, which lets a single extreme result (4/14) be read with appropriate skepticism.

### 5.2 Exchangeability and hierarchical models
General setup: experiments $j=1,\dots,J$, data $y_j$, parameters $\theta_j$, likelihood $p(y_j\mid\theta_j)$ (p. 104).

**Definition (exchangeability).** $(\theta_1,\dots,\theta_J)$ are exchangeable if $p(\theta_1,\dots,\theta_J)$ is invariant to permuting the indices $(1,\dots,J)$ (p. 104). If nothing but the data distinguishes the $\theta_j$'s, one "must assume symmetry" — i.e. exchangeability — in their prior (p. 104). The author stresses: "ignorance implies exchangeability," but this is not a license to stay ignorant (p. 104–105).

The simplest exchangeable form treats the $\theta_j$'s as conditionally i.i.d. given unknown $\phi$:
$$p(\theta\mid\phi)=\prod_{j=1}^{J}p(\theta_j\mid\phi)\tag{5.1}$$
$$p(\theta)=\int\Big(\prod_{j=1}^{J}p(\theta_j\mid\phi)\Big)p(\phi)\,d\phi\tag{5.2}$$
**De Finetti's theorem** (stated, not proved here): as $J\to\infty$, any suitably well-behaved exchangeable distribution on $(\theta_1,\dots,\theta_J)$ can be written as such a mixture (5.2). This does *not* hold for finite $J$ (p. 105). Counterexample: six exchangeable die-face probabilities $\theta_1,\dots,\theta_6$ sum to 1, so they cannot be independent given any $\phi$, yet they can still be modeled exchangeably (p. 105).

**Example: exchangeability and sampling (divorce rates).** Eight unlabeled states' divorce rates $y_1,\dots,y_8$: with no distinguishing information they must be modeled exchangeably (not necessarily independently) — seeing seven values (5.8, 6.6, 7.8, 5.6, 7.0, 7.1, 5.4) lets you predict $y_8$ is "probably similar," centered near 6.5 (p. 105). If told (without knowing which index is which) that the eight states are specific named Mountain states, the prior should allow for an outlier high (Nevada) and low (Utah) value, while remaining exchangeable, since the index-to-state mapping is still unknown — this could make the posterior for $y_8$ bimodal or trimodal (p. 106). But once told that the *unobserved* state ($y_8$) specifically is Nevada, exchangeability is broken, since that information distinguishes $y_8$ from the rest; the actual 1981 Nevada rate was 13.9 (p. 106).

**Partial and conditional exchangeability.** If observations can be grouped (e.g. by laboratory), one may build a hierarchical model with an exchangeable prior across group-level properties — "partial exchangeability." If a covariate $x_i$ distinguishes units so that $y_i$ alone isn't exchangeable but $(y_i,x_i)$ is, one models $y_i\mid x_i$ conditionally. In general:
$$p(\theta_1,\dots,\theta_J\mid x_1,\dots,x_J)=\int\Big[\prod_{j=1}^{J}p(\theta_j\mid\phi,x_j)\Big]p(\phi\mid x)\,d\phi \tag{p.107}$$
making exchangeable models "almost universally applicable" once relevant information is encoded as covariates (p. 107). In the rat tumor data, sample sizes $n_j$ are the only distinguishing variable, and a plot (not shown) of $y_j/n_j$ against $n_j$ shows no relation, so plain exchangeability across the 71 experiments is used (p. 107).

**Objection (common statistical intuition):** the 71 rat experiments really were done at different times, on different rats, "presumably in different laboratories" — so how can they be treated as exchangeable? **Author's reply:** that the experiments differ does not invalidate exchangeability; with no information to distinguish them it is the only logical choice, no more objectionable than treating i.i.d. samples, regression models, or unlabeled scatterplot points as exchangeable. The real issue is not exchangeability itself but whether relevant knowledge has been encoded as covariates (p. 107).

**Full Bayesian treatment.** Since $\phi$ is unknown, it gets its own prior $p(\phi)$. Joint prior: $p(\phi,\theta)=p(\phi)p(\theta\mid\phi)$. Joint posterior:
$$p(\phi,\theta\mid y)\propto p(\phi,\theta)p(y\mid\phi,\theta) = p(\phi,\theta)p(y\mid\theta) \tag{5.3}$$
the simplification holding because $y$ depends on $\phi$ only through $\theta$ (p. 107). The **hyperprior** $p(\phi)$ can often be diffuse, but if improper, one must check the posterior is still proper (p. 107–108).

**Posterior predictive distributions.** Two kinds are distinguished: (1) future data $\tilde y$ for an *existing* $\theta_j$ (e.g. more rats in an ongoing experiment); (2) data $\tilde y$ for a *future* group $\tilde\theta$ drawn from the population distribution given posterior draws of $\phi$ (e.g. a wholly new experiment) (p. 108).

*Intuition note:* Exchangeability is a formal way of saying "I have no reason to treat these groups differently" — it does not say the groups are identical, only that their differences aren't predictable in advance from what you know.

### 5.3 Bayesian analysis of conjugate hierarchical models
**Three analytic steps** for $p(\theta,\phi\mid y)$ (p. 108):
1. Write the unnormalized joint posterior $p(\theta,\phi\mid y)\propto p(\phi)\,p(\theta\mid\phi)\,p(y\mid\theta)$.
2. Find the conditional posterior $p(\theta\mid\phi,y)$ — easy for conjugate models, since given $\phi$ the $\theta_j$'s are independent with conjugate posteriors.
3. Obtain the marginal posterior $p(\phi\mid y)$, either by brute-force integration
$$p(\phi\mid y)=\int p(\theta,\phi\mid y)\,d\theta \tag{5.4}$$
or, when closed forms exist, via
$$p(\phi\mid y)=\frac{p(\theta,\phi\mid y)}{p(\theta\mid\phi,y)} \tag{5.5}$$
Caution: the denominator's normalizing "constant" depends on $\phi$ as well as $y$, so care is needed (p. 109).

**Simulation strategy** (general, for simple hierarchical models): (1) draw $\phi$ from $p(\phi\mid y)$ (grid methods if low-dimensional); (2) draw $\theta$ from $p(\theta\mid\phi,y)=\prod_j p(\theta_j\mid\phi,y)$, componentwise; (3) optionally draw predictive $\tilde y$, drawing a new $\tilde\theta$ first if needed. Repeat $L$ times (p. 109).

**Application to rat tumors.** $y_j\sim\text{Bin}(n_j,\theta_j)$, $\theta_j\sim\text{Beta}(\alpha,\beta)$ i.i.d., $J=71$. Joint posterior:
$$p(\theta,\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^{J}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\prod_{j=1}^{J}\theta_j^{y_j}(1-\theta_j)^{n_j-y_j} \tag{5.6}$$
Conditional posterior (independent beta densities):
$$p(\theta\mid\alpha,\beta,y)=\prod_{j=1}^{J}\frac{\Gamma(\alpha+\beta+n_j)}{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1} \tag{5.7}$$
Marginal posterior of hyperparameters, via (5.5):
$$p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^{J}\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\cdot\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)} \tag{5.8}$$
This has no closed-form simplification but is cheap to evaluate numerically (p. 110).

**Choosing a hyperprior.** The author reparameterizes to $\big(\log(\alpha/\beta),\log(\alpha+\beta)\big)$ — the logit of the population mean and the log of the "sample size" — and notes a *uniform* prior on this scale yields an **improper posterior**, infinite as $\alpha+\beta\to\infty$ (p. 110). Instead, taking a diffuse density uniform on $\big(\alpha/(\alpha+\beta),(\alpha+\beta)^{-1/2}\big)$ and applying the Jacobian gives
$$p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2} \tag{5.9}$$
$$p\big(\log(\alpha/\beta),\log(\alpha+\beta)\big)\propto\alpha\beta(\alpha+\beta)^{-5/2} \tag{5.10}$$
A warning: even setting the earlier (problematic) uniform prior to a huge but finite range like $[-10^{10},10^{10}]^2$ would *not* fix things — almost all posterior mass would sit near "infinity," implying a Beta distribution with zero variance, i.e. all $\theta_j$ essentially equal (p. 111).

**Computing and sampling.** A grid over $\big(\log(\alpha/\beta),\log(\alpha+\beta)\big)$ is used to compute (5.8) with prior (5.9) (Figure 5.2, first range too narrow; Figure 5.3, wider range captures the mode at roughly $(-1.75,2.8)$, i.e. $(\alpha,\beta)\approx(2.4,14.0)$, noticeably different from the earlier point estimate (1.4, 8.6)) (p. 111–112). Posterior means from grid-averaging: $E(\alpha\mid y)=2.4$, $E(\beta\mid y)=14.3$ (p. 112). 1000 joint draws are obtained by: (1) drawing $(\log(\alpha/\beta),\log(\alpha+\beta))$ from the grid; (2) transforming to $(\alpha,\beta)$; (3) for each $j$, drawing $\theta_j\sim\text{Beta}(\alpha+y_j,\beta+n_j-y_j)$ (p. 112).

**Results (Figure 5.4):** posterior medians of $\theta_j$ are shrunk from the raw ratios $y_j/n_j$ toward the population mean ($\approx 0.14$); experiments with fewer observations shrink more and have higher posterior variance. Results resemble a point-hyperparameter approach (because $J$ is large here), but the fully Bayesian posterior variability is higher, reflecting genuine uncertainty about $(\alpha,\beta)$ (p. 113).

*Skip path (digest note):* if you just want the conclusion, it is enough to remember: conditional-conjugate step (5.7) + grid-based marginal step (5.8) → draw $(\alpha,\beta)$, then draw each $\theta_j\sim\text{Beta}(\alpha+y_j,\beta+n_j-y_j)$; the "Results" paragraph above gives the qualitative payoff.

*Intuition note:* The hyperparameters $(\alpha,\beta)$ say how tightly the different experiments' true risks cluster together; because we're honestly uncertain about $(\alpha,\beta)$ too, the final uncertainty about each $\theta_j$ is larger than if we had just plugged in a best guess.

### 5.4 Normal model with exchangeable parameters
This is the "one-way normal random-effects model with known data variance." Data: $y_{ij}\mid\theta_j\sim N(\theta_j,\sigma^2)$, $i=1,\dots,n_j$; $j=1,\dots,J$ (5.11), with group mean $\bar y_{\cdot j}=\frac1{n_j}\sum_i y_{ij}$, $\sigma_j^2=\sigma^2/n_j$. Sufficient-statistic likelihood:
$$\bar y_{\cdot j}\mid\theta_j\sim N(\theta_j,\sigma_j^2) \tag{5.12}$$
(All later expressions implicitly condition on known $\sigma_j^2$; unknown-variance versions appear in Sections 11.6 and 13.6 — p. 114.) The model also applies more generally whenever (5.12) is a good approximation, even if the within-group data aren't normal (p. 114).

**Pragmatic motivation.** With $J=20$ groups of $n_j=2$ observations from the "same strain of rat," separate means $\bar y_{\cdot j}$ are too noisy; a fully pooled estimate
$$\bar y_{\cdot\cdot}=\frac{\sum_{j=1}^{J}\frac1{\sigma_j^2}\bar y_{\cdot j}}{\sum_{j=1}^{J}\frac1{\sigma_j^2}} \tag{5.13}$$
might seem preferable — classically decided via an ANOVA $F$-test comparing between- and within-group mean squares (table below, balanced case $n_j=n$, $\sigma_j^2=\sigma^2/n$) (p. 114):

| | df | SS | MS | $E(\text{MS}\mid\sigma^2,\tau)$ |
|---|---|---|---|---|
| Between groups | $J-1$ | $\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$ | SS/(J-1) | $n\tau^2+\sigma^2$ |
| Within groups | $J(n-1)$ | $\sum_i\sum_j(y_{ij}-\bar y_{\cdot j})^2$ | SS/(J(n-1)) | $\sigma^2$ |
| Total | $Jn-1$ | $\sum_i\sum_j(y_{ij}-\bar y_{\cdot\cdot})^2$ | SS/(Jn-1) | |

But a weighted compromise $\hat\theta_j=\lambda_j\bar y_{\cdot j}+(1-\lambda_j)\bar y_{\cdot\cdot}$, $0\le\lambda_j\le1$, is also possible (p. 114–115). The author shows which priors generate each estimate as the posterior mean: (1) unpooled $\hat\theta_j=\bar y_{\cdot j}$ ⟵ independent uniform priors on $(-\infty,\infty)$; (2) pooled $\hat\theta=\bar y_{\cdot\cdot}$ ⟵ all $\theta_j$ forced equal, uniform prior on the common value; (3) weighted ⟵ independent, identically distributed *normal* priors — of which (1) and (2) are limiting special cases ($\lambda_j\equiv1$, infinite prior variance; $\lambda_j\equiv0$, zero prior variance) (p. 115).

**The hierarchical model.** For conjugacy, $\theta_j\mid\mu,\tau\sim N(\mu,\tau^2)$ i.i.d.:
$$p(\theta_1,\dots,\theta_J\mid\mu,\tau)=\prod_{j=1}^{J}N(\theta_j\mid\mu,\tau^2) \tag{5.14}$$
with a noninformative uniform hyperprior for $\mu$ given $\tau$:
$$p(\mu,\tau)=p(\mu\mid\tau)p(\tau)\propto p(\tau) \tag{5.15}$$
reasonable because combined data across $J$ experiments are typically very informative about $\mu$ (p. 115).

**Joint posterior:**
$$p(\theta,\mu,\tau\mid y)\propto p(\mu,\tau)\prod_{j=1}^{J}N(\theta_j\mid\mu,\tau^2)\prod_{j=1}^{J}N(\bar y_{\cdot j}\mid\theta_j,\sigma_j^2) \tag{5.16}$$
**Conditional posterior of $\theta$ given hyperparameters** (combining a normal likelihood and normal prior for each $\theta_j$, Section 2.5 methods):
$$\theta_j\mid\mu,\tau,y\sim N(\hat\theta_j,V_j),\qquad \hat\theta_j=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{\tau^2}\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\quad V_j=\frac{1}{\frac1{\sigma_j^2}+\frac1{\tau^2}} \tag{5.17}$$
— a precision-weighted average of the group mean and population mean (p. 116).

**Marginal posterior of hyperparameters.** Since $\bar y_{\cdot j}\mid\mu,\tau\sim N(\mu,\sigma_j^2+\tau^2)$ (independent but not identical), the marginal likelihood has closed form:
$$p(\mu,\tau\mid y)\propto p(\mu,\tau)\prod_{j=1}^{J}N(\bar y_{\cdot j}\mid\mu,\sigma_j^2+\tau^2) \tag{5.18}$$
Factor $p(\mu,\tau\mid y)=p(\mu\mid\tau,y)p(\tau\mid y)$ (5.19). With $\tau$ known, $p(\mu\mid\tau,y)$ is normal (quadratic log-posterior in $\mu$) with
$$\hat\mu=\frac{\sum_j\frac1{\sigma_j^2+\tau^2}\bar y_{\cdot j}}{\sum_j\frac1{\sigma_j^2+\tau^2}},\qquad V_\mu^{-1}=\sum_{j=1}^{J}\frac1{\sigma_j^2+\tau^2} \tag{5.20}$$
Then, since (5.19) must hold for any $\mu$, setting $\mu=\hat\mu$ gives
$$p(\tau\mid y)\propto p(\tau)\,V_\mu^{1/2}\prod_{j=1}^{J}(\sigma_j^2+\tau^2)^{-1/2}\exp\!\Big(-\frac{(\bar y_{\cdot j}-\hat\mu)^2}{2(\sigma_j^2+\tau^2)}\Big) \tag{5.21}$$
with $\hat\mu, V_\mu$ as in (5.20) (p. 117).

**Prior for $\tau$.** The author adopts $p(\tau)\propto1$ (uniform), leaving as an exercise that this yields a proper posterior, while the seemingly natural $p(\log\tau)\propto1$ yields an *improper* posterior (p. 117). A scaled inverse-$\chi^2$ prior calibrated to a "best guess" and an upper percentile is offered as an alternative when more care is wanted (p. 117).

**Computation.** Factorization $p(\theta,\mu,\tau\mid y)=p(\tau\mid y)p(\mu\mid\tau,y)p(\theta\mid\mu,\tau,y)$: simulate $\tau$ via inverse-cdf on a grid from (5.21); then $\mu$ from (5.20); then each $\theta_j$ from (5.17) (p. 118).

**Posterior predictive distributions.** For new data $\tilde y$ from the *current* batches, draw $(\theta,\mu,\tau\mid y)$, then $\tilde y$ from (5.11). For $\tilde J$ *new* batches, draw $(\mu,\tau)$, then new $\tilde\theta_j\mid\mu,\tau$ from (5.14), then $\tilde y$ given $\tilde\theta$ (p. 118).

**Difficulty with the non-Bayesian point estimate.** Classical unbiased estimates: $\hat\mu=\bar y_{\cdot\cdot}$, $\hat\tau^2=(\text{MSB}-\text{MSW})/n$ (5.22). This $\hat\tau^2$ **can be negative**; forcing it to zero when $\text{MSW}>\text{MSB}$ implicitly claims $\tau^2=0$ exactly — i.e. that all group means are *identical* — which the author argues is too strong a claim, since a non-significant F-test only shows the sample is too small to distinguish $\tau^2$ from zero, not that $\tau^2$ is known to be zero. Any point estimate of $(\mu,\tau)$ shares the generic flaw of ignoring uncertainty (p. 118–119).

*Skip path (digest note):* equations (5.17), (5.20), (5.21) are the three formulas actually used in computation; everything else in this section motivates or justifies them.

*Intuition note:* Each group's final estimate (5.17) is a weighted average of "what this group's own data say" and "what all groups together say," with the weight on the group's own data growing as its own measurement gets more precise relative to the between-group spread $\tau$.

### 5.5 Example: parallel experiments in eight schools
Eight randomized experiments (ETS study) estimate the effect of SAT-V coaching; $y_j$ = estimated effect (from an analysis-of-covariance adjustment), $\sigma_j$ = its standard error, both treated as known given the large samples ($>30$ per school) (p. 119). Observed effects range from $-3$ to $28$ points, standard errors $9$–$18$ (Table 5.2).

**Separate estimates:** 95% intervals for all eight schools overlap substantially — individually, differences are statistically hard to pin down (p. 119).

**Pooled estimate:** treating all schools as sharing one true effect gives $\bar y_{\cdot\cdot}=7.7$, posterior variance $\big(\sum_j 1/\sigma_j^2\big)^{-1}=16.6$, SD $=4.1$, 95% interval $[-0.5,15.9]\approx[8\pm8]$; the classical $\chi^2$ statistic ($4.6$, df$=7$) is non-significant, equivalently $\hat\tau^2$ from (5.22) is negative (p. 120). A thought experiment: if the true common effect were $8$ with between-school SD $13$ (the RMS of the $\sigma_j$'s), expected order statistics across 8 draws would be roughly $26,19,14,10,6,2,-3,-9$ — close to the observed pattern — "it would appear imprudent to believe that school A really has an effect as large as 28 points" (p. 120).

**Why both extremes fail (School A, $y=28.4$, $\sigma=14.9$):** the separate analysis implies "the probability is $\tfrac12$ that the true effect in A is more than 28.4" — doubtful, given the other seven schools. The pooled model implies "the probability is $\tfrac12$ that the true effect in A is less than 7.7," and also that P(A's effect < C's effect) $=\tfrac12$ — both hard to justify from Table 5.2 (p. 120–121). A compromise combining all eight experiments without assuming equal effects is wanted; the hierarchical model "provides exactly that" (p. 121).

**Posterior simulation.** $\tau,\mu,\theta$ are drawn in that order as in Section 5.4, with independent uniform priors on $\mu,\tau$ (p. 121).

**Results.** $p(\tau\mid y)$ (Figure 5.5): $\tau$ near $0$ is most plausible (mode at $0$); $\tau>10$ less than half as likely as $\tau=0$; $\Pr(\tau>25)\approx0$ (p. 121). Conditional means $E(\theta_j\mid\tau,y)$ (Figure 5.6) stay close together for the likely range of $\tau$, diverging toward the raw values as $\tau$ grows; school C (higher $\sigma$) shrinks more strongly than E or F, crossing their lines (p. 121–122). Conditional SDs $\text{sd}(\theta_j\mid\tau,y)$ (Figure 5.7) grow with $\tau$, approaching the raw $\sigma_j$'s as $\tau\to\infty$ (p. 121–122). Example: at $\tau=10$, $\Pr(\theta_A<28)=\Phi[(28-14.5)/9.1]=93\%$; the other schools' corresponding probabilities range $97\%$–$99.96\%$ (p. 122).

Conditioning on the *posterior mode* of $\tau$ (here $\tau=0$, on the boundary of its parameter space) would give all schools the identical estimate $7.7\pm4.1$ — "too much pulling together," and a joint modal estimate of all $J{+}2$ parameters together would be even worse (p. 122).

**Discussion.** Table 5.3 (200 simulations): 95% intervals are roughly twice as wide as the single pooled interval, median-centered $5$–$10$, but shifted toward the separate answers in allowing larger School-A effects and more-negative School-C effects than pure pooling would (p. 122–123). The Bayesian probability that School A's effect is $\ge28$ is under 10%, versus 50% under the separate analysis (p. 123). From the 200 draws: $\Pr(\max_j\theta_j > 28.4)\approx22/200\approx0.11$ (Figure 5.8), and $\Pr(\theta_1>\theta_3\mid y)=141/200=0.705$ — i.e. School A beats School C with posterior probability 0.705 (p. 123).

*Intuition note:* "Shrinkage" here literally means: because the data cannot rule out that schools' true effects are nearly equal (small $\tau$), each school's estimate gets pulled toward the group as a whole, and that pull is itself uncertain, which is why the Bayesian intervals end up wider than the naive pooled interval but narrower and more defensible than treating each school alone.

### 5.6 Hierarchical modeling applied to a meta-analysis
22 clinical trials of beta-blockers after myocardial infarction (Table 5.4): $n_{0j},n_{1j}$ control/treatment sample sizes, $y_{0j},y_{1j}$ deaths. Estimands considered: risk difference $p_{1j}-p_{0j}$, risk ratio $p_{1j}/p_{0j}$, odds ratio $\rho_j=\frac{p_{1j}/(1-p_{1j})}{p_{0j}/(1-p_{0j})}$; the chapter works with $\theta_j=\log\rho_j$ for interpretability across study designs and near-normal small-sample behavior (p. 124–125).

**Normal approximation to the likelihood.** Empirical-logit estimate:
$$y_j=\log\!\Big(\frac{y_{1j}}{n_{1j}-y_{1j}}\Big)-\log\!\Big(\frac{y_{0j}}{n_{0j}-y_{0j}}\Big) \tag{5.23}$$
$$\sigma_j^2=\frac1{y_{1j}}+\frac1{n_{1j}-y_{1j}}+\frac1{y_{0j}}+\frac1{n_{0j}-y_{0j}} \tag{5.24}$$
(a half-count correction is sometimes recommended but "does not concern us" for moderately large studies here) (p. 125).

**Goals of inference.** Three possibilities for treating the $J$ studies: (1) identical replications (one shared population, pooled); (2) so different that one study tells us nothing about another; (3) exchangeable but not identical — the stance adopted here, as "a continuum between the two extremes" (p. 125–126). Note: exchangeability itself does not force a normal population distribution — that is a convenient added assumption, to be checked later (Chapter 6) (p. 126). Three distinct estimands follow: the population mean effect $\mu$, the effect in an *observed* study, and the effect in a hypothetical new exchangeable study (p. 126).

**If exchangeability fails:** if covariates distinguish the studies, one can extend to a hierarchical regression model (Chapter 15) estimating how effect varies with covariates (p. 126).

**The model** mirrors Section 5.4 exactly: $y_j\mid\theta_j,\sigma_j\sim N(\theta_j,\sigma_j^2)$ (known $\sigma_j$), $\theta_j\mid\mu,\tau\sim N(\mu,\tau^2)$, locally uniform priors on $\mu,\tau$ (p. 126).

**Results.** The marginal posterior of $\tau$ peaks at a *nonzero* value, though $\tau=0$ remains plausible (density only about 25% lower than at the mode) (p. 127). Posterior median $\tau=0.13$ is small relative to most $\sigma_j$'s, so shrinkage is considerable, especially for low-precision studies 1, 6, 18 (p. 127); individual posteriors are skewed, more so for imprecise studies (2, 18) than precise ones (7, 14) (p. 127). Averaging over the posterior for $\tau$ matters: $\text{sd}(\mu\mid\tau,y)=0.060$ at $\tau=0.13$ but $\text{sd}(\mu\mid y)=0.071$ once $\tau$-uncertainty is included (p. 127).

Table 5.5 gives: $\mu$'s 95% interval $[-0.37,-0.11]$, i.e. odds ratio $[0.69,0.90]$; $\tau$'s 95% interval $[0.02,0.31]$; and the wider "predicted effect" $\tilde\theta_j$ interval $[-0.58,0.11]$ for a hypothetical new study (p. 127). By contrast, complete pooling ($\tau=0$) gives a narrower $[0.70,0.85]$, which the original published discussion of these data called an "unusually narrow range of uncertainty" (p. 127) — the hierarchical analysis attributes this to an inappropriate model that effectively claimed all studies were identical. With the beta-blocker data, there is "just over 10%" posterior probability that the true effect $\tilde\theta_j$ in a new study would be *positive* — i.e. the treatment increasing death risk (p. 128).

*Intuition note:* Meta-analysis asks three different questions that are often conflated: "what's the average effect across these studies?", "what was the true effect in this particular study?", and "what would the effect be in a brand-new, as-yet-unstudied population?" — and the third is always the most uncertain.

### 5.7 Weakly informative priors for variance parameters
The choice of prior for the group-level scale $\tau$ can strongly affect inference, especially when $J$ is small or $\tau$ is small (p. 128).

**Improper limit of a prior distribution.** To avoid confusion, improper densities are defined as limits of proper ones: $\text{uniform}(0,A)$ on $\tau$ as $A\to\infty$, or inverse-gamma$(\epsilon,\epsilon)$ on $\tau^2$ as $\epsilon\to0$. The uniform$(0,A)$ family yields a proper limiting posterior as $A\to\infty$ provided $J\ge3$; the inverse-gamma$(\epsilon,\epsilon)$ family has *no* proper limit, so posterior inferences stay sensitive to $\epsilon$ (p. 128).

**Calibration.** Defined as the Bayesian analogue of classical bias: with $\hat\theta=E(\theta\mid y)$, *miscalibration* is $E(\theta\mid\hat\theta)-\hat\theta$; this is zero for all $\hat\theta$ if the prior used really is the one that generated $\theta$ (p. 128). Unlike classical bias (which conditions on the true $\theta$ and studies the sampling distribution of $\hat\theta$), Bayesian calibration conditions on the data $y$ (hence on $\hat\theta$) and studies the distribution of $\theta$ that could have produced it (p. 128). With improper models one must posit a "true" and an "inferential" prior to even define calibration. Demonstration: if both true and inferential priors for $\tau$ are $U(0,A)$, miscalibration is trivially zero; letting only the *inferential* prior go to $U(0,\infty)$ increases $\hat\theta$ on average (because mass is now spread into $[A,\infty)$) without changing the true $\theta$, so miscalibration becomes positive — i.e. $\tau$ is overestimated on average (p. 128–129).

**Classes of priors for $\tau$:**
- *Uniform on $\log\tau$* seems natural but gives an **improper posterior**, because the marginal likelihood $p(y\mid\tau)$ approaches a finite nonzero value as $\tau\to0$ — "the data can never rule out a group-level variance of zero," so an infinite-mass prior near there is fatal (p. 129).
- *Uniform on $\tau$* has finite mass near $0$ and is the density the authors "generally used" in their applied work, but it has "a slightly disagreeable miscalibration toward positive values" from its infinite right-tail mass; with $J=1$ or $2$ groups it gives an improper posterior (effectively $\tau=\infty$, no pooling); for small $J$ (4–5) the heavy right tail risks overestimating $\tau$ and under-pooling (p. 129).
- *Uniform on $\tau^2$* is **not recommended** — worse miscalibration, and needs $J\ge4$ for propriety (p. 130).
- These improper uniform priors can be seen as limits of conditionally-conjugate families: $p(\tau)\propto\tau^{-1}$ (uniform on $\log\tau$) is an inverse-$\chi^2$ with 0 degrees of freedom; $p(\tau^2)\propto\tau^{-1}$ (uniform on $\tau$) is inverse-$\chi^2$ with $-1$ degrees of freedom, or a limit of half-$t$ with scale $\to\infty$ (p. 129).
- *Inverse-gamma$(\epsilon,\epsilon)$* on $\tau^2$ is conditionally conjugate (equivalent to inverse-$\chi^2$ with scale $s^2=\beta/\alpha$, df $=2\alpha$), an attempt at noninformativeness with small $\epsilon$ (e.g. $1$, $0.01$, $0.001$); as $\epsilon\to0$ the posterior becomes improper, and for moderate $\epsilon$ inference is highly sensitive to it — "hardly looks noninformative" (p. 130).
- *Half-Cauchy* (a half-$t$ family case) has a broad peak at zero and one scale parameter $A$; $A\to\infty$ recovers the uniform prior. Finite large $A$ is called "weakly informative" because its tail has a gentle slope and "can let the data dominate if the likelihood is strong in that region," useful when $\tau$ is estimated from few groups (p. 130).

**Application, 8 schools (Figure 5.9).** Three priors compared: (a) uniform on $\tau$: posterior supports values mostly below $\tau=20$ with a slight tail, reflecting that $J=8$ is "not much more than the $J=3$ required" for propriety; (b) inverse-gamma$(1,1)$ on $\tau^2$: lower posterior mean/median, more shrinkage, posterior nearly matches the concentrated prior range $[0.5,5]$, where the likelihood is "close to flat" — i.e. the prior, not the data, is doing the work; (c) inverse-gamma$(0.001,0.001)$: even more sharply concentrated near zero, further distorting inference, because the marginal likelihood for $\tau$ "remains high near zero" (p. 130–131). On a log-$\tau$ scale, (c) would *look* flattest, but it is still not noninformative, since its posterior remains sensitive to $\epsilon$ — "the simplest approach — the uniform prior density on $\tau$ — seems to perform well" in this example (p. 131).

**3-schools reanalysis (Figure 5.10).** Using only the first three schools, the uniform$(0,\infty)$ prior on $\tau$ produces an "extremely long right tail" of implausibly large $\tau$ values, under-pooling the school effects, as expected since $J$ is at the edge of propriety (p. 132). A half-Cauchy prior with scale $A=25$ (chosen a bit above the expected SD of the school effects) performs better: high over the plausible range $\tau<50$, falling off gradually, without visibly distorting the region of high likelihood (p. 132). The half-Cauchy would also have worked for 8 schools but was unnecessary there; with only 3 schools, it was used precisely *because* it is not meant to represent real prior belief but rather to constrain the posterior only as far as the data demand (p. 132).

*Intuition note:* Flat-looking "noninformative" priors on a variance parameter are a trap: because variances are bounded below by zero, a prior that looks flat on one scale (e.g. $\log\tau$) can hide infinite mass right where the data are least informative (near $\tau=0$), silently overriding what the data can say.

### 5.8 Bibliographic note
This section is a literature review (Stein, James–Stein, Efron–Morris, Robbins, de Finetti, Mosteller–Wallace, Laird–Ware, and others) tracing the history of shrinkage estimation, empirical/hierarchical Bayes, and meta-analysis methods, plus sources for the rat-tumor, eight-schools, and beta-blocker datasets used in the chapter (p. 132–133). No new analytic content is given; omitted from the walkthrough above since the digest reports only arguments made on these pages, not citation lists.

## Toy example (ours)
Illustrating the partial-pooling formula (5.17), with hyperparameters *assumed known* for hand computation (the chapter's own worked examples require numerical integration over $\tau$, which cannot be done by hand).

Three groups, with observed means $y_j$ and known sampling variances $\sigma_j^2$:

| Group | $y_j$ | $\sigma_j^2$ |
|---|---|---|
| 1 | 16 | 4 |
| 2 | 8 | 1 |
| 3 | 14 | 16 |

Assume (for this toy example only) that the population distribution is known to be $\theta_j\sim N(\mu{=}10,\ \tau^2{=}4)$. Apply (5.17): $\hat\theta_j=\dfrac{y_j/\sigma_j^2+\mu/\tau^2}{1/\sigma_j^2+1/\tau^2}$, $V_j=\dfrac1{1/\sigma_j^2+1/\tau^2}$.

**Group 1** ($\sigma_1^2=4=\tau^2$, equal precision): $1/\sigma_1^2=0.25$, $1/\tau^2=0.25$. Numerator $=16(0.25)+10(0.25)=4+2.5=6.5$. Denominator $=0.5$. $\hat\theta_1=6.5/0.5=13$ — exactly halfway between the raw value (16) and the population mean (10): 50% shrinkage, since the two precisions are equal. $V_1=1/0.5=2$.

**Group 2** ($\sigma_2^2=1$, very precise): $1/\sigma_2^2=1$, $1/\tau^2=0.25$. Numerator $=8(1)+10(0.25)=8+2.5=10.5$. Denominator $=1.25$. $\hat\theta_2=10.5/1.25=8.4$ — close to the raw value 8: little shrinkage, because this group's own data are far more precise than the population spread. $V_2=1/1.25=0.8$.

**Group 3** ($\sigma_3^2=16$, imprecise): $1/\sigma_3^2=0.0625$, $1/\tau^2=0.25$. Numerator $=14(0.0625)+10(0.25)=0.875+2.5=3.375$. Denominator $=0.3125$. $\hat\theta_3=3.375/0.3125=10.8$ — close to the population mean 10: strong shrinkage, because this group's own data are much less precise than the population. $V_3=1/0.3125=3.2$.

This reproduces, by hand, exactly the pattern the book reports for the rat-tumor and eight-schools examples: groups with less precise data ($\sigma_j^2$ large relative to $\tau^2$) are pulled further toward the population mean, and have larger posterior variance, than groups with precise data.

## Concepts
- [[hierarchical-multilevel-model]] — in this chapter: data modeled given group parameters $\theta_j$, which are themselves given a population distribution governed by hyperparameters $\phi$ that get their own hyperprior (p. 101).
- [[exchangeability]] — joint distribution of the $\theta_j$'s (or $y_j$'s) unchanged under permutation of indices; used here to justify a common population prior when nothing else distinguishes the groups (p. 104).
- [[hyperprior-distribution]] (new) — the prior distribution $p(\phi)$ placed on the hyperparameters $\phi$ of the population distribution, itself possibly diffuse or noninformative (p. 107).
- [[conjugate-prior]] — used twice in this chapter: Beta($\alpha,\beta$) conjugate to binomial for the rat-tumor model, and Normal($\mu,\tau^2$) conjugate to normal for the schools/meta-analysis model (p. 102, 115).
- [[partial-pooling-shrinkage]] — group estimates pulled toward the population mean, with less-precise or less-informative groups pulled more (p. 112–113, 121–122).
- [[posterior-predictive-distribution]] — here split into two distinct kinds: prediction for a new observation within an existing group vs. for a new, future group drawn from the population distribution (p. 108).
- [[marginal-likelihood (evidence)]] — denoted $p(y\mid\phi)$ or $p(y\mid\mu,\tau)$; used as a factor in the marginal posterior of the hyperparameters, computed in closed form here because the models are conjugate (p. 109, 116).
- [[empirical-bayes]] (new) — the practice of estimating hyperparameters from the data by a point estimate and then conditioning on that estimate; the authors treat it as an approximation to full hierarchical Bayes and avoid the term because it wrongly implies the full method is not "empirical" (p. 104).
- [[credible-interval]] — called "posterior interval" in this text; e.g. the 95% posterior intervals for school effects or for $\mu$ in the meta-analysis, interpreted as direct probability statements about the parameter (p. 120, 127).
- [[weakly-informative-prior]] (new) — a prior (e.g. half-Cauchy with large scale $A$) chosen not to represent actual prior belief but to constrain the posterior only as far as the data allow, used when $J$ is too small for a fully noninformative prior to behave well (p. 130, 132).
- [[calibration-bayesian]] (new) — Bayesian analogue of classical bias: miscalibration of a posterior mean $\hat\theta$ is $E(\theta\mid\hat\theta)-\hat\theta$, zero if the prior used matches the (hypothetical) true generating prior (p. 128).

## Canonical instances
- [[rat-tumor-hierarchical-example]] (new) — 71 binomial experiments (70 historical + 1 current) on tumor incidence, modeled with a Beta-Binomial hierarchical model; the chapter's running example for Sections 5.1 and 5.3 (p. 102, 109–113).
- [[eight-schools]] (new) — eight parallel randomized SAT-coaching experiments; the chapter's main illustration of the normal hierarchical model and of why neither separate nor pooled analysis is adequate (p. 119–123).
- [[beta-blocker-meta-analysis]] (new) — 22 clinical trials of beta-blockers after heart attack, analyzed as a hierarchical normal model on the log-odds-ratio scale (p. 124–128).
- [[divorce-rate-exchangeability-example]] (new) — thought experiment with 8 states' divorce rates used purely to illustrate exchangeability versus independence and how added information can break exchangeability (p. 105–106).
- [[three-schools-weakly-informative]] (new) — reanalysis of the first three of the eight schools, used to show that a uniform prior on $\tau$ becomes inadequate for small $J$ and a half-Cauchy prior performs better (p. 131–132).

## Bridges (candidates)
- [structural-analogy] The precision-weighted shrinkage formula (5.17), $\hat\theta_j = \frac{y_j/\sigma_j^2+\mu/\tau^2}{1/\sigma_j^2+1/\tau^2}$ ↔ inverse-variance weighting used generally whenever combining estimates of differing precision — same weighting logic appears outside hierarchical Bayes wherever precisions are summed.
- [structural-analogy] The weighted-combination estimator $\hat\theta_j=\lambda_j\bar y_{\cdot j}+(1-\lambda_j)\bar y_{\cdot\cdot}$ (p. 114) ↔ the classical James–Stein shrinkage estimator, which the chapter's own bibliographic note (p. 132) credits as historically influential for hierarchical normal models — a similar weighted-average form, but derived from a frequentist rather than Bayesian argument, so not literally the same mathematics.
- [metaphor] "Borrowing strength" from other studies via partial pooling (p. 127) ↔ general statistical metaphor for combining weak signals across related sources, used in many fields beyond Bayesian hierarchical modeling.
- [structural-analogy] Checking integrability of an "noninformative" hyperprior before trusting it (Sections 5.3, 5.4, 5.7) ↔ the general Bayesian practice of verifying any improper prior yields a proper posterior before interpreting results — a caution that recurs whenever diffuse priors are used.

## Questions this raises
- How does the choice between a normal, beta, or other population distribution for $\theta_j$ get checked against the data once fitted (the text defers this to Chapter 6)?
- For non-conjugate hierarchical models (e.g. a normal population distribution on the logit scale for the rat-tumor problem, Exercise 5.11), what replaces the closed-form grid/analytic computation used here?
- How sensitive are the eight-schools conclusions to the assumption of known, fixed $\sigma_j$ rather than estimated sampling variances?
- When $J$ is very small (2 or 3 groups), how should an analyst decide how much weakly-informative prior information to add, beyond picking a scale like $A=25$ by rough judgment?

## Exercises worth doing
- Ex. 1–2 (p. 134) — distinguishes exchangeability from independence using simple ball-in-box examples; builds the core intuition before the formal treatment — difficulty: easy.
- Ex. 3 (p. 134) — reproduces the eight-schools computations and compares "probability of being best" and pairwise comparison probabilities across the hierarchical, separate ($\tau=\infty$), and pooled ($\tau=0$) models — difficulty: medium.
- Ex. 5 (p. 134) — proves that any exchangeable mixture-of-i.i.d. model (5.2) implies nonnegative covariances between parameters, the formal reason why learning about one group informs another — difficulty: medium.
- Ex. 9 (p. 135–136) — works through why a uniform prior on $(\log(\alpha/\beta),\log(\alpha+\beta))$ gives an improper posterior in the rat-tumor model, and why (5.10) and $0<y_j<n_j$ for some $j$ fix this — directly underpins Section 5.3's hyperprior choice — difficulty: hard.
- Ex. 12 (p. 136) — derive $E(\theta_j\mid\tau,y)$ and $\text{var}(\theta_j\mid\tau,y)$ (the formulas behind Figures 5.6–5.7) by averaging (5.17) over $\mu$ — difficulty: medium.

## Reading notes
- **OCR issue (important):** the extracted text layer in these pages systematically renders the Greek letter $\theta$ (theta) as "$\omega$" throughout Sections 5.1–5.7 (equations, prose, figure labels). The page images confirm the correct symbol is $\theta_j$ for group-level parameters, with $\phi$ (and specifically $\alpha,\beta$ or $\mu,\tau$) for hyperparameters. 102, 104, 107, 109, 110, 114–119, 121, 125, 128–129, 131).
- Minus signs in exponents were OCR'd as arrows (e.g. "$\theta_j^{\alpha\to1}$" for $\theta_j^{\alpha-1}$); corrected throughout by checking page images (e.g. p. 110).
- Printed page numbers equal pdf page numbers minus 10 for this unit (e.g. pdf 111 = printed 101), consistent throughout the supplied range (pdf 111–148, printed 101–138).
- Figures 5.1–5.10 and Tables 5.1–5.5 are described in L3 from their captions and the surrounding discussion; exact pixel-level data from scatterplots/histograms are not reproduced since the image resolution does not permit precise reading of individual points.
- Section 5.9 (Exercises, p. 134–137) is reflected only in the "Exercises worth doing" section above, per digest convention of not reproducing full exercise sets in the walkthrough.
