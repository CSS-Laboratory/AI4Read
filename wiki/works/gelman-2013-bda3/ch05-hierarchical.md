---
id: gelman-2013-bda3/ch05-hierarchical
work: gelman-2013-bda3
unit: "Chapter 5 — Hierarchical models"
pages: 101–138
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Hierarchical models (BDA3, ch. 5)

## L0 — One line
When many parameters are related, treat them as exchangeable draws from a population distribution with unknown hyperparameters, and do a full Bayesian analysis of everything jointly; this gives partial pooling that fits the data without overfitting.

## L1 — The gist (≤ 120 words)
How should we model many related parameters, such as effects in several schools or trials? The chapter treats them as draws from a common population distribution whose hyperparameters are themselves unknown and given a hyperprior. The full joint posterior then gives partial pooling: group estimates shrink toward the population mean, between the extremes of separate and fully pooled estimates, while uncertainty about the hyperparameters is kept. Worked examples are rat tumors, eight coaching experiments and beta-blocker trials. The chapter ends on choosing weakly informative priors for the group-level standard deviation, which matters when there are few groups.

**Prerequisites:** Bayes' theorem; beta–binomial and normal–normal conjugacy; conditional/marginal densities; grid and inverse-cdf sampling; gamma function; basic ANOVA vocabulary.

## L2 — Key ideas (5–10 bullets)
- Simple nonhierarchical models are usually inappropriate for hierarchical data: with few parameters they generally cannot fit large datasets accurately, and with many parameters they tend to overfit. Hierarchical models can have many parameters and still avoid overfitting, because a population distribution ties the parameters together (p. 101).
- Estimating a prior from the data with a point estimate (the "empirical Bayes" idea) is only a starting point. If the estimated prior were reused for the same groups, the data would be used twice and precision would seem overstated, and any point estimate ignores some uncertainty in the hyperparameters, so the authors prefer a probability model on the whole set (pp. 103–104).
- The standard way to say "no information distinguishes the units" is exchangeability. A mixture of i.i.d. distributions (5.2) is usually all that is needed to capture exchangeability in practice. Information that does distinguish units should go into covariates (pp. 104–107).
- Full Bayes: put a hyperprior $p(\phi)$ on the hyperparameters and sample $\phi\sim p(\phi|y)$, then $\theta\sim p(\theta|\phi,y)$, then $\tilde y$. In the conjugate rat-tumor example the marginal $p(\phi|y)$ is computed on a grid (pp. 107–109, 112).
- In the normal model, given $(\mu,\tau)$, $\hat\theta_j$ is a precision-weighted average of the group mean and the population mean (5.17). The marginal posterior of $\tau$ is a one-dimensional function (5.21) (pp. 116–117).
- In the eight-schools example, separate and pooled estimates are both unsatisfactory. The hierarchical posterior partially pools, and conditioning on a modal $\tau=0$ would over-pool (pp. 119–123).
- In the beta-blocker meta-analysis, complete pooling gives a narrower interval that an earlier discussion called unusually narrow; the hierarchical analysis suggests this was because the model implicitly claimed all studies identical, i.e. $\tau=0$ exactly. A predicted effect in a new study is more uncertain than the overall mean (pp. 125–128).
- Priors for $\tau$ matter, especially for small $J$. Uniform on $\tau$ works for $J=8$ but gives a long tail for $J=3$, where a half-Cauchy weakly informative prior works better. Inverse-gamma$(\epsilon,\epsilon)$ and uniform on $\log\tau$ are problematic (pp. 128–132).

## L3 — Walkthrough

### Chapter introduction (p. 101)
- Parameters can be related by the structure of the problem, so a joint model should reflect their dependence. Example: hospital $j$ has survival probability $\theta_j$, and the $\theta_j$'s are viewed as a sample from a common **population distribution** (p. 101).
- Data $y_{ij}$ (unit $i$ in group $j$) can inform the population distribution even though the $\theta_j$ are not observed. Observables are modelled given parameters, which are given a probabilistic specification via further parameters called **hyperparameters** (p. 101).
- Simple nonhierarchical models usually fail for hierarchical data. With few parameters they cannot fit large datasets well. With many parameters they overfit, meaning they fit existing data but predict new data worse. Hierarchical models can have enough parameters to fit well while avoiding overfitting. It is often sensible to fit more parameters than data points (p. 101).
- Plan: 5.1 builds a prior with hierarchical ideas but only a point estimate of the hyperparameters. 5.2 gives the fully Bayesian version. 5.3–5.4 give conjugate computation. 5.5–5.6 give two examples. 5.7 covers weakly informative priors (p. 101).

### 5.1 Constructing a parameterized prior distribution (pp. 102–104)

**Rat tumor example.** Aim: estimate $\theta$, the probability of endometrial stromal polyps in control female F344 rats. The current data are 4 tumors out of 14 rats. Model: binomial likelihood with conjugate prior $\theta\sim\text{Beta}(\alpha,\beta)$ (p. 102).

- *Fixed prior.* If the population mean and standard deviation of tumor probabilities were known, one could solve for $(\alpha,\beta)$ from the beta mean and variance. The posterior would then be $\text{Beta}(\alpha+4,\beta+10)$ (p. 102).
- *Estimated prior.* Historical data are 70 earlier groups (Table 5.1). Group $j$ has $y_j$ tumors out of $n_j$, with $y_j$ independent binomial given $\theta_j$ and the $\theta_j$ taken as Beta$(\alpha,\beta)$ draws. The current experiment is $j=71$ (Figure 5.1) (p. 102).
- The 70 values $y_j/n_j$ have sample mean 0.136 and standard deviation 0.103. Setting the beta mean and sd to these values gives $(\alpha,\beta)=(1.4,8.6)$. The authors say this is *not* a Bayesian calculation, since no full probability model is specified (pp. 102–103).
- Using this as prior gives posterior Beta(5.4, 18.6) for $\theta_{71}$: mean 0.223, sd 0.083. This is well below the crude $4/14=0.286$, because experience suggests the current count is unusually high (p. 103).
- The analysis assumes $\theta_{71}$ and $\theta_1,\dots,\theta_{70}$ are a random sample from one distribution. This assumption would be invalidated if, for example, the historical experiments were all in lab A and the current one in lab B, or if there were time trends (p. 103).
- A simple but arbitrary fix is to inflate the historical variance. In the beta model this means decreasing $\alpha+\beta$ while holding $\alpha/\beta$ constant (p. 103).

**Problems with directly estimating the prior from existing data** (pp. 103–104):
1. Using the estimated prior for the first 70 experiments uses the data twice, which seems to overstate precision.
2. A point estimate of $(\alpha,\beta)$ is arbitrary and ignores posterior uncertainty.
3. The authors also ask whether $(\alpha,\beta)$ should be "estimated" at all, noting that they are part of the prior and asking whether they should be known before the data are gathered, according to the logic of Bayesian inference (posed as a question, not a conclusion).

**Logic of combining information (p. 104).** It still makes more sense to estimate the population distribution from all data than to estimate all 71 $\theta_j$ separately.
- Thought experiment: $\theta_{26}$ and $\theta_{27}$ each have 2 tumors out of 20 rats, and the prior for both is centred near 0.15. If told $\theta_{26}=0.1$ exactly, you would probably lower your estimate of $\theta_{27}$, since the data for the two parameters are identical and the postulated 0.1 is lower than you expected for $\theta_{26}$ from the prior. So the two are dependent in the posterior and should not be analysed separately (p. 104).
- The remedy is a probability model on the whole set of parameters and experiments, followed by Bayesian analysis of the joint distribution (Section 5.3). The point-estimate approach, sometimes called **empirical Bayes**, can be viewed as an approximation to the full hierarchical analysis. The authors avoid the term because it suggests that full Bayes is not "empirical" (p. 104).

> **Intuition note.** If groups come from one population, learning about one group tells you something about the others. A fixed prior estimated once from the same data hides this dependence and hides the uncertainty about the prior.

### 5.2 Exchangeability and hierarchical models (pp. 104–108)

Setup: experiments $j=1,\dots,J$ with data (vector) $y_j$, parameter (vector) $\theta_j$ and likelihood $p(y_j|\theta_j)$. Parameters may overlap, e.g. $\theta_j=(\mu_j,\sigma^2)$ (p. 104).

**Exchangeability.** If no information other than $y$ distinguishes the $\theta_j$'s and no ordering or grouping can be made, one must assume symmetry. The $\theta_j$ are *exchangeable* if $p(\theta_1,\dots,\theta_J)$ is invariant under permutations of the indexes (p. 104). In the rat example, apart from the sample sizes $n_j$ (presumably unrelated to $\theta_j$), nothing distinguishes the 71 experiments (p. 104). "Ignorance implies exchangeability": the less we know, the more confidently we can claim exchangeability. The die analogy: weighing a die may reveal imperfections that remove the symmetry (pp. 104–105).

The simplest exchangeable form has the $\theta_j$ independent given an unknown $\phi$:
$$p(\theta|\phi)=\prod_{j=1}^J p(\theta_j|\phi). \tag{5.1}$$
Averaging over uncertainty in $\phi$:
$$p(\theta)=\int\Big(\prod_{j=1}^J p(\theta_j|\phi)\Big)p(\phi)\,d\phi. \tag{5.2}$$
This mixture of independent identical distributions is usually all that is needed in practice (p. 105).

- **de Finetti's theorem:** as $J\to\infty$, any suitably well-behaved exchangeable distribution on $(\theta_1,\dots,\theta_J)$ can be written as (5.2). It does not hold for finite $J$ (Exercises 5.1, 5.2, 5.4) (p. 105).
- Counterexample for finite $J$: the six face probabilities of a die are exchangeable but constrained to sum to 1, so they cannot be a mixture of independent identical distributions (p. 105).

**Example: exchangeability and sampling (divorce rates, pp. 105–106).** Eight US states are chosen and their 1981 divorce rates $y_1,\dots,y_8$ recorded. The exchangeability is at the level of $y$, not $\theta$.
- With no information on which state is which, model them exchangeably, with a fairly vague distribution (p. 105).
- Seven randomly chosen values are revealed: 5.8, 6.6, 7.8, 5.6, 7.0, 7.1, 5.4. A reasonable posterior predictive for $y_8$ would probably be centred near 6.5, with most mass between 5.0 and 8.0. The $y_j$ are exchangeable but not independent (p. 105–106).
- If you are also told the eight are the Mountain states (unordered), the prior is still exchangeable but should change. Utah is expected low and Nevada high, so the prior needs wide tails. The posterior for $y_8$ might be bimodal or trimodal, since the missing state might be Nevada or Utah (p. 106).
- If told the unsampled state is Nevada, exchangeability is lost even before seeing the data, and $p(y_8>\max(y_1..y_7)|y_1..y_7)$ should be large. Nevada's 1981 rate was 13.9 per 1000 (p. 106).

**Partial or conditional exchangeability (pp. 106–107).**
- If observations can be grouped, we may build a hierarchical model with one submodel per group. If the group properties are exchangeable, they get a common prior (p. 106).
- If $y_i$ has extra information $x_i$ so that $y_i$ are not exchangeable but $(y_i,x_i)$ are, model $(y_i,x_i)$ jointly or $y_i|x_i$ (p. 106).
- Rat example: if we knew that specific batches were made in different laboratories, we could assume partial exchangeability and use a two-level model for variation within and between labs (p. 106).
- Usual form with covariates: $p(\theta_1,\dots,\theta_J|x)=\int[\prod_j p(\theta_j|\phi,x_j)]p(\phi|x)d\phi$ (p. 107). Exchangeable models are thus "almost universally applicable", since distinguishing information should be encoded in $x$ and $y$ (p. 107).
- The sample sizes $n_j$ are the only distinguishing information in the rat data. A plot of $y_j/n_j$ against $n_j$ (not shown) shows no apparent relation (p. 107).

**Objections to exchangeable models (p. 107).** Units really do differ, but this does not invalidate exchangeability. Differences imply the $\theta_j$ differ, yet they may be treated as drawn from a common distribution. With no distinguishing information there is "no logical choice" but exchangeability. The authors compare objecting to it with objecting to i.i.d. models, to regression in general, or to unlabelled scatterplots. The valid concern is about encoding relevant knowledge as explanatory variables (p. 107).

**Full Bayesian treatment (p. 107).** The hyperparameters $\phi$ are unknown, so they get a prior $p(\phi)$. The target is the posterior of $(\phi,\theta)$:
$$p(\phi,\theta)=p(\phi)p(\theta|\phi),$$
$$p(\phi,\theta|y)\propto p(\phi,\theta)p(y|\phi,\theta)=p(\phi,\theta)p(y|\theta). \tag{5.3}$$
The simplification holds because $\phi$ affects $y$ only through $\theta$ (p. 107).

**Hyperprior (pp. 107–108).** A diffuse prior on $\phi$ is possible. With an improper prior, check that the posterior is proper and assess sensitivity. In most real problems there should be enough knowledge to constrain $\phi$ to a finite region. It is often practical to start with a simple, relatively noninformative prior and add information if the posterior varies too much (pp. 107–108).

**Posterior predictive distributions (p. 108).** Two kinds exist: (1) future $\tilde y$ for an existing $\theta_j$, (2) $\tilde y$ for future $\tilde\theta_j$ drawn from the same superpopulation. For (1), use posterior draws of $\theta_j$. For (2), first draw $\tilde\theta$ from the population distribution given draws of $\phi$, then draw $\tilde y$ given $\tilde\theta$ (p. 108).

> **Intuition note.** Exchangeability does not say the units are equal. It says that, as far as you know, you cannot tell which unit is which. The hyperprior then lets the data say how alike the units are.

### 5.3 Bayesian analysis of conjugate hierarchical models (pp. 108–113)

The strategy extends Section 3.8, but one cannot generally plot the joint posterior of $(\theta,\phi)$. The section uses the beta–binomial rat model, where $p(\theta|\phi)$ is conjugate to $p(y|\theta)$. Nonconjugate models need Part III methods. The conjugate approach is still useful for approximations and starting points (p. 108).

**Three analytic steps (p. 108).**
1. Write the unnormalized joint posterior as hyperprior × population distribution × likelihood: $p(\phi)\,p(\theta|\phi)\,p(y|\theta)$.
2. Find the conditional posterior $p(\theta|\phi,y)$. This is easy for conjugate models because it is a product of conjugate posteriors for the $\theta_j$ (pp. 108–109).
3. Get the marginal posterior $p(\phi|y)$, either by brute-force integration
$$p(\phi|y)=\int p(\theta,\phi|y)\,d\theta \tag{5.4}$$
or, for many standard models including the normal, via the conditional probability formula
$$p(\phi|y)=\frac{p(\theta,\phi|y)}{p(\theta|\phi,y)}. \tag{5.5}$$
The numerator is (5.3). The denominator is the posterior of $\theta$ if $\phi$ were known. The difficulty beyond a few standard conjugate models is that the denominator's normalizing factor depends on $\phi$ as well as $y$. Care is needed that the proportionality "constant" really is constant. Exercise 5.11 gives a nonconjugate case where (5.4) has no closed form and (5.5) does not help (p. 109).

**Simulation strategy (p. 109).**
1. Draw $\phi\sim p(\phi|y)$ (Chapter 3 methods if $\phi$ is low-dimensional, Part III otherwise).
2. Draw $\theta\sim p(\theta|\phi,y)$. In this chapter $p(\theta|\phi,y)=\prod_jp(\theta_j|\phi,y)$, so components are drawn independently.
3. If wanted, draw $\tilde y$ given $\theta$ (first a new $\tilde\theta$ given $\phi$ if needed).
Repeat $L$ times (p. 109).

**Rat tumor model (pp. 109–113).** $y_j\sim\text{Bin}(n_j,\theta_j)$ with $n_j$ known, $\theta_j\sim\text{Beta}(\alpha,\beta)$ independently, $J=71$, and a noninformative hyperprior. "Noninformative" describes the authors' attitude, not special properties. If the hyperprior is crucial, report it. If it is improper, check the posterior is proper (p. 110).

Joint posterior:
$$p(\theta,\alpha,\beta|y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\prod_{j=1}^J\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}. \tag{5.6}$$
Given $(\alpha,\beta)$, the $\theta_j$ are independent beta:
$$p(\theta|\alpha,\beta,y)=\prod_{j=1}^J\frac{\Gamma(\alpha+\beta+n_j)}{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}. \tag{5.7}$$
Dividing (5.6) by (5.7), as in (5.5) (added step: per $j$, the $\theta_j$ factors cancel, leaving the gamma-function ratio):
$$p(\alpha,\beta|y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)}. \tag{5.8}$$
It cannot be simplified analytically but is easy to evaluate for given $(\alpha,\beta)$ with a gamma-function routine (p. 110).

**Hyperprior choice (pp. 110–111).**
- Reparameterize as $\text{logit}\big(\tfrac{\alpha}{\alpha+\beta}\big)=\log\tfrac{\alpha}{\beta}$ (logit of the mean) and $\log(\alpha+\beta)$ (log of the "sample size"). Uniform priors on these give an *improper posterior*, with an infinite integral as $(\alpha+\beta)\to\infty$ (p. 110).
- With a lot of data, a diffuse hyperprior dominated by the likelihood is possible. The choice is uniform on $\big(\tfrac{\alpha}{\alpha+\beta},(\alpha+\beta)^{-1/2}\big)$, which with the Jacobian gives
$$p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}, \tag{5.9}$$
$$p\Big(\log\tfrac{\alpha}{\beta},\log(\alpha+\beta)\Big)\propto\alpha\beta(\alpha+\beta)^{-5/2}. \tag{5.10}$$
See Exercise 5.9 (pp. 110–111).
- As another approach, tentatively using a flat prior would show posterior contours drifting off to infinity, indicating nonintegrability, and the prior would then have to be altered. A uniform prior on $[-10^{10},10^{10}]^2$ on the log scale is *not* acceptable. Almost all posterior mass would sit near "infinity", which means a beta variance of zero, so all $\theta_j$ nearly equal. A faraway finite cutoff does not necessarily fix a non-integrable likelihood (p. 111).

**Computing the marginal posterior (pp. 111–112).**
- Compute $\log$ of (5.8) with prior (5.9), multiply by the Jacobian, subtract the maximum log density, and exponentiate (to avoid overflow).
- First grid: $[-2.5,-1]\times[1.5,3]$, centred near the earlier estimate $(-1.8,2.3)$, i.e. $(\alpha,\beta)=(1.4,8.6)$ (Figure 5.2). The mode is near the point estimate, and important parts of the posterior lie outside the graph (p. 111).
- Second grid: $[-2.3,-1.3]\times[1,5]$ (Figure 5.3a), which shows essentially all the mass. The posterior is roughly symmetric about its mode, about $(-1.75,2.8)$, corresponding to $(\alpha,\beta)\approx(2.4,14.0)$. This differs somewhat from the crude estimate (p. 112).
- Normalize by treating the density as a step function on the grid. Moments are grid sums, e.g. $E(\alpha|y)\approx\sum\alpha\,p(\log\tfrac{\alpha}{\beta},\log(\alpha+\beta)|y)$. Result: $E(\alpha|y)=2.4$, $E(\beta|y)=14.3$. Averaging over the grid also accounts for the uncertainty in $(\alpha,\beta)$ that a point estimate misses (p. 112).

**Sampling 1000 joint draws (p. 112).** (1) Draw 1000 pairs $(\log\tfrac{\alpha}{\beta},\log(\alpha+\beta))$ from the grid, using the discrete-grid procedure from the bioassay example of Section 3.8. (2) For each draw: transform to $(\alpha,\beta)$, then draw $\theta_j|\alpha,\beta,y\sim\text{Beta}(\alpha+y_j,\beta+n_j-y_j)$ for each $j$ (p. 112).

**Results (pp. 112–113).** Figure 5.4 shows posterior medians and 95% intervals of $\theta_j$ against $y_j/n_j$. The $\theta_j$ are shrunk toward the population distribution (approximate mean 0.14). Experiments with fewer observations are shrunk more and have higher posterior variance. The results are superficially like those from a point estimate of the hyperparameters, which makes sense with so many experiments. But posterior variability is higher in the full analysis, reflecting hyperparameter uncertainty (p. 113).

> **Intuition note.** The chain is: sample the hyperparameters from their posterior, then sample each group parameter given them. Each draw of the hyperparameters shifts all group estimates together. This is why uncertainty in the hyperparameters widens the group intervals.

### 5.4 Normal model with exchangeable parameters (pp. 113–119)

This is the one-way normal random-effects model with known data variance (p. 113).

**Data structure.** $J$ independent experiments, with $n_j$ observations each:
$$y_{ij}|\theta_j\sim\text{N}(\theta_j,\sigma^2),\quad i=1..n_j,\ j=1..J. \tag{5.11}$$
Group mean $\bar y_{.j}=\frac1{n_j}\sum_i y_{ij}$, sampling variance $\sigma_j^2=\sigma^2/n_j$. Then with sufficient statistics
$$\bar y_{.j}|\theta_j\sim\text{N}(\theta_j,\sigma_j^2). \tag{5.12}$$
All expressions are conditional on known $\sigma_j^2$. This is rarely strictly true but often an adequate approximation. (5.12) also appears when group means are approximately normal (large $n_j$) even if $y_{ij}$ are not (pp. 113–114).

**Pragmatic prior construction (pp. 114–115).** Example: $J=20$ groups of $n_j=2$ assays from the same rat strain. Two estimates are possible. The unpooled estimate is $\bar y_{.j}$. The pooled estimate is
$$\bar y_{..}=\frac{\sum_j\sigma_j^{-2}\bar y_{.j}}{\sum_j\sigma_j^{-2}}. \tag{5.13}$$
Classically, an ANOVA $F$ test chooses between them. The table for a balanced design ($n_j=n$), with $\tau^2$ the variance of the $\theta_j$:

| | df | SS | MS | $E(\text{MS}|\sigma^2,\tau)$ |
|---|---|---|---|---|
| Between groups | $J-1$ | $\sum_i\sum_j(\bar y_{.j}-\bar y_{..})^2$ | SS/$(J-1)$ | $n\tau^2+\sigma^2$ |
| Within groups | $J(n-1)$ | $\sum_i\sum_j(y_{ij}-\bar y_{.j})^2$ | SS/$(J(n-1))$ | $\sigma^2$ |
| Total | $Jn-1$ | $\sum_i\sum_j(y_{ij}-\bar y_{..})^2$ | SS/$(Jn-1)$ | |

If the between/within ratio is significantly above 1, use separate estimates. Otherwise the test cannot "reject" $\tau=0$ and pooling is reasonable (p. 114).

We are not forced to choose. A weighted combination is $\hat\theta_j=\lambda_j\bar y_{.j}+(1-\lambda_j)\bar y_{..}$ with $0\le\lambda_j\le1$. Which priors give which estimates (p. 115):
1. Unpooled $\hat\theta_j=\bar y_{.j}$ is the posterior mean if the $\theta_j$ have independent uniform priors on $(-\infty,\infty)$.
2. Pooled $\bar y_{..}$ is the posterior mean if the $\theta_j$ are restricted to be equal, with a uniform prior on the common value.
3. The weighted combination is the posterior mean if the $\theta_j$ have i.i.d. normal priors.
All three are exchangeable, and 1 and 2 are special cases of 3: no pooling is $\lambda_j\equiv1$ with infinite prior variance, and complete pooling is $\lambda_j\equiv0$ with zero prior variance (p. 115).

**Hierarchical model (p. 115).** For partial conjugacy:
$$p(\theta_1,\dots,\theta_J|\mu,\tau)=\prod_{j=1}^J\text{N}(\theta_j|\mu,\tau^2),\qquad p(\theta_1,\dots,\theta_J)=\int\prod_{j=1}^J\big[\text{N}(\theta_j|\mu,\tau^2)\big]p(\mu,\tau)\,d(\mu,\tau). \tag{5.14}$$
Hyperprior: uniform on $\mu$ given $\tau$,
$$p(\mu,\tau)=p(\mu|\tau)p(\tau)\propto p(\tau). \tag{5.15}$$
Vagueness about $\mu$ is affordable because the combined data are generally highly informative about $\mu$ (p. 115).

**Joint posterior (pp. 115–116).**
$$p(\theta,\mu,\tau|y)\propto p(\mu,\tau)\,p(\theta|\mu,\tau)\,p(y|\theta)\propto p(\mu,\tau)\prod_{j=1}^J\text{N}(\theta_j|\mu,\tau^2)\prod_{j=1}^J\text{N}(\bar y_{.j}|\theta_j,\sigma_j^2). \tag{5.16}$$

**Conditional posterior of $\theta$ given $(\mu,\tau)$ (p. 116).** The $\theta_j$ are independent, with $\theta_j|\mu,\tau,y\sim\text{N}(\hat\theta_j,V_j)$ (Section 2.5 methods applied per $j$):
$$\hat\theta_j=\frac{\frac1{\sigma_j^2}\bar y_{.j}+\frac1{\tau^2}\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\qquad V_j=\frac1{\frac1{\sigma_j^2}+\frac1{\tau^2}}. \tag{5.17}$$
The posterior mean is a precision-weighted average of the prior population mean and the group sample mean (p. 116).

> **Intuition note.** The weight on the group's own mean is $\frac{1/\sigma_j^2}{1/\sigma_j^2+1/\tau^2}$. Noisy groups (large $\sigma_j$) and similar groups (small $\tau$) are pulled harder toward $\mu$.

**Marginal posterior of the hyperparameters (p. 116).** Directly, $p(\mu,\tau|y)\propto p(\mu,\tau)p(y|\mu,\tau)$. For the normal model the marginal likelihood is simple: averaging over $\theta$, the $\bar y_{.j}$ are independent (not identically distributed) with $\bar y_{.j}|\mu,\tau\sim\text{N}(\mu,\sigma_j^2+\tau^2)$. Hence
$$p(\mu,\tau|y)\propto p(\mu,\tau)\prod_{j=1}^J\text{N}(\bar y_{.j}|\mu,\sigma_j^2+\tau^2). \tag{5.18}$$
Factor as
$$p(\mu,\tau|y)=p(\mu|\tau,y)\,p(\tau|y). \tag{5.19}$$

*$\mu$ given $\tau$.* With uniform $p(\mu|\tau)$ the log posterior is quadratic in $\mu$, so $\mu|\tau,y\sim\text{N}(\hat\mu,V_\mu)$. It treats the $\bar y_{.j}$ as $J$ independent estimates of $\mu$ with variances $\sigma_j^2+\tau^2$:
$$\hat\mu=\frac{\sum_j\frac1{\sigma_j^2+\tau^2}\bar y_{.j}}{\sum_j\frac1{\sigma_j^2+\tau^2}},\qquad V_\mu^{-1}=\sum_{j=1}^J\frac1{\sigma_j^2+\tau^2}. \tag{5.20}$$
This is a proper density (pp. 116–117).

*$\tau$.* From (5.19), (5.18) and (5.20):
$$p(\tau|y)=\frac{p(\mu,\tau|y)}{p(\mu|\tau,y)}\propto\frac{p(\tau)\prod_j\text{N}(\bar y_{.j}|\mu,\sigma_j^2+\tau^2)}{\text{N}(\mu|\hat\mu,V_\mu)}.$$
This must hold for any $\mu$, so set $\mu=\hat\mu$. Since $\text{N}(\hat\mu|\hat\mu,V_\mu)\propto V_\mu^{-1/2}$ (added step):
$$p(\tau|y)\propto p(\tau)\,V_\mu^{1/2}\prod_{j=1}^J(\sigma_j^2+\tau^2)^{-1/2}\exp\!\Big(-\frac{(\bar y_{.j}-\hat\mu)^2}{2(\sigma_j^2+\tau^2)}\Big), \tag{5.21}$$
with $\hat\mu,V_\mu$ from (5.20). It is a complicated function of $\tau$ (p. 117).

*Prior for $\tau$ (p. 117).* The illustrative choice is uniform, $p(\tau)\propto1$. The authors leave as an exercise that this gives a proper posterior, whereas $p(\log\tau)\propto1$ gives an improper one. Alternatively, elicit a "best guess" and an upper bound (e.g. 99th percentile) for $\tau$ and match them to a scaled inverse-$\chi^2$ prior. After an initial analysis, a sensitivity analysis with a more realistic prior is often desirable (p. 117).

**Computation (p. 118).** Use $p(\theta,\mu,\tau|y)=p(\tau|y)\,p(\mu|\tau,y)\,p(\theta|\mu,\tau,y)$. (1) Draw $\tau$ by the inverse-cdf method on a uniform grid using (5.21). (2) Draw $\mu$ from (5.20). (3) Draw each $\theta_j$ independently from (5.17) (p. 118).

**Posterior predictive (p. 118).** For new data from the *current* batches, draw $(\theta,\mu,\tau)$ and then $\tilde y$ from (5.11). For $\tilde J$ *new* groups (with specified $\tilde n_j$), draw $(\mu,\tau)$, then $\tilde\theta_j\sim p(\tilde\theta_j|\mu,\tau)$ from (5.14), then $\tilde y$ from (5.11) (p. 118).

**Problem with the non-Bayesian point estimate (pp. 118–119).** Unbiased ANOVA-based estimates:
$$\hat\mu=\bar y_{..},\qquad\hat\tau^2=(\text{MS}_B-\text{MS}_W)/n. \tag{5.22}$$
Inference for $\theta$ then uses $p(\theta|\hat\mu,\hat\tau)$. Problems:
- It ignores uncertainty in the hyperparameters, so the result is not a Bayesian posterior summary.
- $\hat\tau^2$ can be negative. Setting it to zero when $\text{MS}_W>\text{MS}_B$ claims $\tau^2=0$, which says all $\theta_j$ are absolutely identical. But $\text{MS}_W>\text{MS}_B$ only means the sample is too small to distinguish $\tau^2$ from zero, which is not the same as knowing $\tau^2=0$.
- A point estimate avoiding negativity could be built, but it would still ignore uncertainty (pp. 118–119).

### 5.5 Example: parallel experiments in eight schools (pp. 119–123)

**Data.** Separate randomized experiments in eight high schools measured the effect of SAT-V coaching (Educational Testing Service study). SAT-V scores run 200–800 with mean about 500 and sd about 100. In each school, the estimated effect $y_j$ and its standard error $\sigma_j$ come from a covariance-adjusted regression (PSAT-M and PSAT-V as controls). There are over thirty students per school, so $\sigma_j$ is treated as known. About 8 points on SAT-V corresponds to about one more test item correct. There was no prior reason to rank the programs (p. 119).

| School | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| $y_j$ | 28 | 8 | −3 | 7 | −1 | 1 | 18 | 12 |
| $\sigma_j$ | 15 | 10 | 16 | 11 | 9 | 11 | 10 | 18 |

(Table 5.2, p. 120)

**Separate estimates.** The 95% posterior intervals from separate analyses all overlap substantially, so it is hard to distinguish the experiments (p. 119).

**Pooled estimate** (flat prior, common effect): posterior mean $\bar y_{..}=7.7$ (5.13 with $y_j$), variance $(\sum_j\sigma_j^{-2})^{-1}=16.6$, standard error $\sqrt{16.6}=4.1$, 95% interval $[-0.5,15.9]$ ($\approx8\pm8$). Supporting this, $\sum_j(y_j-\bar y_{..})^2/\sigma_j^2=4.6$ is below its 7 degrees of freedom, and $\hat\tau^2$ from (5.22) is negative (p. 120).
- If all effects were equal, eight draws from N(8, 13²) (13 = square root of the mean of the $\sigma_j^2$) would have expected order statistics of about 26, 19, 14, 10, 6, 2, −3, −9. These are consistent with Table 5.2, so it would appear imprudent to believe school A's effect is 28 (p. 120).

**Why both extremes fail (p. 120).** For school A, separate analysis gives 28.4 (se 14.9), pooled gives 7.7 (se 4.1). The separate analysis implies "probability ½ that the true effect in A exceeds 28.4", which is doubtful given the other schools. The pooled model implies "probability ½ that the effect in A is below 7.7" and "probability ½ that A's effect is below C's", also hard to justify. A compromise is wanted (pp. 120–121).

**Posterior simulation (p. 121).** Use the model of Section 5.4 with $\sigma_j$ as in Table 5.2 and independent uniform priors on $\mu$ and $\tau$. Simulate $\tau$, then $\mu$, then $\theta$ (p. 121).

**Results (pp. 121–122).**
- $p(\tau|y)$ (Figure 5.5): $\tau=0$ is the most likely value, $\tau>10$ is less than half as likely as $\tau=0$, and $\Pr(\tau>25)\approx0$ (p. 121).
- $E(\theta_j|\tau,y)$ against $\tau$ (Figure 5.6): for likely $\tau$ the estimates are close together. As $\tau$ grows they approach the raw effects. School C's line crosses E's and F's because C has larger measurement error and is shrunk more (pp. 121–122).
- $\text{sd}(\theta_j|\tau,y)$ (Figure 5.7) increases with $\tau$, approaching the $\sigma_j$ of Table 5.2 as $\tau\to\infty$. Formulas are via (2.7), (2.8) averaging over $\mu$ (Exercise 5.12) (p. 121).
- Conclusion: an effect as large as 28.4 in any school is unlikely. At $\tau=10$, $\Pr(\theta_A<28)=\Phi[(28-14.5)/9.1]=93\%$. For the other schools the probabilities are 99.5, 99.2, 98.5, 99.96, 99.8, 97 and 98% (pp. 121–122).
- Conditioning on the posterior mode of $\tau$ (here $\tau=0$) would give 7.7 points and se 4.1 for all schools, which is too much pulling together. The problem is acute because the mode is on the boundary. Joint modal estimates of $(\theta,\mu,\tau)$ are generally worse (p. 122).

**Discussion: 200 simulations (Table 5.3, p. 123).**

| School | 2.5% | 25% | median | 75% | 97.5% |
|---|---|---|---|---|---|
| A | −2 | 7 | 10 | 16 | 31 |
| B | −5 | 3 | 8 | 12 | 23 |
| C | −11 | 2 | 7 | 11 | 19 |
| D | −7 | 4 | 8 | 11 | 21 |
| E | −9 | 1 | 5 | 10 | 18 |
| F | −7 | 2 | 6 | 10 | 28 |
| G | −1 | 7 | 10 | 15 | 26 |
| H | −6 | 3 | 8 | 13 | 33 |

- Like the pooled interval, the eight 95% intervals overlap and are median-centred between 5 and 10. Unlike it, they are each almost twice as wide as the common interval, with greater probability of effects above 16 (especially A) and of negative effects (especially C) (p. 123).
- The ordering of schools is essentially that of the separate estimates. But the probability that A's effect is as large as 28 is under 10%, against 50% from A's separate estimate (p. 123).
- From simulations: only 22 of 200 draws of $\max_j\theta_j$ exceed 28.4, so $\Pr(\max\theta_j>28.4)\approx22/200$. $\Pr(\theta_1>\theta_3|y)\approx141/200=0.705$ (the share of draws with $\theta_1>\theta_3$) (p. 123).

> **Intuition note.** The hierarchical model lets the data decide how much the schools resemble each other. In our words, the data suggest the schools are alike to a fair degree, though not shown to be identical. The result is estimates that are less extreme than the separate ones and intervals that are wider than the pooled one.

### 5.6 Hierarchical modeling applied to a meta-analysis (pp. 124–128)

**Meta-analysis** summarizes and integrates findings of several studies. Data (Table 5.4, p. 124): 22 randomized trials of beta-blockers after myocardial infarction (Yusuf et al. 1985). Mortality varies from 3% to 21%, and most trials show a modest, not "statistically significant", benefit. It is important to apply rigorous criteria in deciding which studies are included (p. 124).

**Parameter per study (p. 125).** Trial $j$ has $n_{0j}$ control and $n_{1j}$ treated subjects, with $y_{0j},y_{1j}$ deaths, and independent binomials with death probabilities $p_{0j},p_{1j}$. Possible estimands are $p_{1j}-p_{0j}$, the risk ratio $p_{1j}/p_{0j}$, and the odds ratio $\rho_j=\frac{p_{1j}}{1-p_{1j}}/\frac{p_{0j}}{1-p_{0j}}$. The authors focus on $\theta_j=\log\rho_j$, because of interpretability across designs and near-normality of its posterior even in small samples (p. 125).

**Normal approximation (p. 125).** Empirical logits:
$$y_j=\log\Big(\frac{y_{1j}}{n_{1j}-y_{1j}}\Big)-\log\Big(\frac{y_{0j}}{n_{0j}-y_{0j}}\Big), \tag{5.23}$$
$$\sigma_j^2=\frac1{y_{1j}}+\frac1{n_{1j}-y_{1j}}+\frac1{y_{0j}}+\frac1{n_{0j}-y_{0j}}. \tag{5.24}$$
Refinements exist (e.g. adding 0.5 to each count) but do not matter when sample sizes are moderately large (p. 125).

**Goals (pp. 125–126).** Three views, given that the studies are comparable broadly: (1) identical replications from a common population, (2) so different that one tells nothing about another, (3) exchangeable but not necessarily identical or unrelated. The third is a continuum between the extremes and is the basis here. Exchangeability does not dictate the form of the distribution of effects. A normal is assumed for convenience and should be checked with Chapter 6 techniques. Estimands include the mean of the effect distribution, the effect in an observed study, and the effect in a new exchangeable study (p. 126).

**If exchangeability is inappropriate.** Assuming it means assuming no important covariates, which is "perhaps misguidedly" widely adopted in meta-analysis. If other information distinguishes studies, expand to a hierarchical regression (Chapter 15), possibly to estimate a response surface (p. 126).

**Model (p. 126).** $y_j|\theta_j,\sigma_j\sim\text{N}(\theta_j,\sigma_j^2)$, with $\sigma_j$ from (5.24) treated as known. Known variances matter little here because there are more than 50 persons per arm in nearly all studies. The second stage is exchangeable normal with unknown $(\mu,\tau)$. The hyperprior is locally uniform on $\mu$ (justified because even 5 or 10 studies are quite informative about the centre) and locally uniform on $\tau$ (for convenience) (p. 126).

**Results (pp. 127–128).** Table 5.5 (log-odds scale, p. 127):

| Estimand | 2.5% | 25% | median | 75% | 97.5% |
|---|---|---|---|---|---|
| $\mu$ | −0.37 | −0.29 | −0.25 | −0.20 | −0.11 |
| $\tau$ | 0.02 | 0.08 | 0.13 | 0.18 | 0.31 |
| predicted $\tilde\theta_j$ | −0.58 | −0.34 | −0.25 | −0.17 | 0.11 |

- $p(\tau|y)$ peaks at a nonzero value, but zero has a density only about 25% lower than the mode (p. 127).
- The posterior median of $\tau$ (0.13) is small compared with the $\sigma_j$, so there is considerable shrinkage, especially for imprecise studies (e.g. 1, 6, 18), and large reductions in posterior variance. Fixing $\tau$ would give standard deviations too small. Individual-effect posteriors are skewed away from the overall mean, and imprecise studies (2, 18) have longer tails than precise ones (7, 14) (p. 127).
- $E(\mu|\tau,y)$ ranges only from about −0.26 to just over −0.24 over plausible $\tau$. But $\text{sd}(\mu|\tau,y)$ varies by a factor of more than 2. At $\tau=0.13$ it is 0.060, whereas averaging over $\tau$ gives $\text{sd}(\mu|y)=0.071$ (p. 127).
- 95% highest-posterior-density interval for $\mu$ is $[-0.37,-0.11]$, or $[0.69,0.90]$ as an odds ratio. Complete pooling ($\tau=0$) gives the narrower $[0.70,0.85]$. The original discussion called that an "unusually narrow range of uncertainty". The hierarchical analysis suggests this was due to an inappropriate model that implicitly claimed all studies were identical. The data suggest $\tau$ near zero but plausibly up to about 0.3 (p. 127).
- For a population where no study was done, a new-study effect (exchangeable with the others) might be more reasonably targeted than the overall mean; in that case uncertainty is even greater (Table 5.5). Uncertainty for an individual patient adds another component. There is just over 10% posterior probability that a new study's true effect is positive (p. 128).

> **Intuition note.** The overall mean is estimated well, but the effect in a new study carries both uncertainty about $\mu$ and real between-study variation $\tau$. Assuming $\tau=0$ would hide the second part.

### 5.7 Weakly informative priors for variance parameters (pp. 128–132)

The choice of "noninformative" prior for $\tau$ can have a big effect, especially when the number of groups $J$ is small or $\tau$ is small (p. 128).

**Concepts (p. 128).**
- *Improper prior as a limit of proper ones.* Improper priors can, but do not necessarily, give proper posteriors. Two common examples are uniform$(0,A)$ on $\tau$ as $A\to\infty$, and inverse-gamma$(\epsilon,\epsilon)$ on $\tau^2$ as $\epsilon\to0$. The uniform$(0,A)$ model has a proper limiting posterior as $A\to\infty$ provided $J\ge3$, so inferences are insensitive to large finite $A$. The inverse-gamma$(\epsilon,\epsilon)$ model has no proper limiting posterior, so inferences are sensitive to $\epsilon$ and it "cannot simply be comfortably set to a low value such as 0.001" (p. 128).
- *Calibration* of the posterior mean (Bayesian analogue of bias). With $\hat\theta=E(\theta|y)$, the **miscalibration** is $E(\theta|\hat\theta)-\hat\theta$. If the prior is true (data made by drawing $\theta\sim p(\theta)$, then $y\sim p(y|\theta)$), the posterior mean is calibrated: miscalibration is 0 for all $\hat\theta$. Classical bias conditions on the true $\theta$. Bayesian calibration conditions on the data $y$ (and so on $\hat\theta$). For improper priors one must posit a "true prior" and an "inferential prior" (p. 128).
- For the 8 schools, treat the improper uniform on $\tau$ as the limit of uniform$(0,A)$. For any finite $A$ it yields positive miscalibration, i.e. overestimates $\tau$ on average. Argument: if both true and inferential priors are U$(0,A)$, miscalibration is zero. Keeping the true prior U$(0,A)$ and moving the inferential prior to U$(0,\infty)$ necessarily raises $\hat\theta$ for any $y$ without changing the true $\theta$, so average miscalibration becomes positive (pp. 128–129).

**General view (p. 129).** Any noninformative or weakly informative prior is "inherently provisional". After fitting, check whether the posterior makes sense. If not, extra knowledge exists that contradicts the prior, and the prior should be changed.

**Uniform priors (p. 129).**
- *Uniform on $\log\tau$* gives an improper posterior. A compact range $[-A,A]$ makes the posterior depend strongly on the lower bound $-A$. The reason is that the marginal likelihood $p(y|\tau)$ approaches a finite nonzero value as $\tau\to0$, so the posterior has infinite mass as $\log\tau\to-\infty$. In a hierarchical model the data can never rule out a group-level variance of zero.
- *Uniform on $\tau$* has a finite integral near zero and is the authors' usual choice (Section 5.5). But it has slight miscalibration toward positive values, from infinite prior mass as $\tau\to\infty$. With $J=1$ or $2$ the posterior is improper (essentially concluding $\tau=\infty$, no pooling). The authors find this reasonable in a sense but awkward because the data have no say. For small $J$ such as 4 or 5, the heavy right tail may overestimate $\tau$ and under-pool.
- *Equivalences:* uniform on $\log\tau$ equals $p(\tau)\propto\tau^{-1}$ or $p(\tau^2)\propto\tau^{-2}$, an inverse-$\chi^2$ with 0 degrees of freedom (a limit of proper inverse-gamma priors). Uniform on $\tau$ equals $p(\tau^2)\propto\tau^{-1}$, an inverse-$\chi^2$ with $-1$ df. It is not easily a limit of inverse-$\chi^2$ densities, but can be a limit of the half-$t$ family on $\tau$ as the scale $\to\infty$ (any $\nu$).
- *Uniform on $\tau^2$*: not recommended, with larger miscalibration toward high values, and it needs $J\ge4$ for a proper posterior (pp. 129–130).

**Inverse-gamma$(\epsilon,\epsilon)$ (p. 130).** $\tau$'s marginal likelihood has no simple conjugate family, but inverse-gamma for $\tau^2$ is *conditionally conjugate* given the other parameters. Inverse-gamma$(\alpha,\beta)$ equals scaled inverse-$\chi^2$ with $s^2=\beta/\alpha$ and $\nu=2\alpha$. As $\epsilon\to0$ the posterior is improper, so $\epsilon$ must be chosen reasonably. When low $\tau$ is possible, inferences are very sensitive to $\epsilon$ and the prior hardly looks noninformative (p. 130).

**Half-Cauchy (p. 130).** The half-$t$ family (half because $\tau>0$) includes the half-normal and half-Cauchy as edge cases. The half-Cauchy has a broad peak at zero and one scale parameter $A$, and as $A\to\infty$ becomes uniform on $\tau$. Large finite $A$ is weakly informative: the tail slopes gently (unlike a half-normal), so the data can dominate if the likelihood is strong there (p. 130).

**8 schools (pp. 130–131).** Effects are in test points, so a realistic upper limit on $\tau$ is about 100 (p. 130). Figure 5.9:
- (a) Uniform on $\tau$: data support values below about 20 with a slight tail ($J=8$ is not much above the required 3) (p. 130).
- (b) Inverse-gamma(1,1) on $\tau^2$: lower posterior mean and median of $\tau$ and more shrinkage. The prior is concentrated in $[0.5,5]$, where the likelihood is nearly flat, and the posterior simulations match the prior (p. 131).
- (c) Inverse-gamma(0.001,0.001): even more sharply peaked near zero, further distorting inference, because the marginal likelihood for $\tau$ stays high near zero (p. 131).
- Not considered: uniform on $\log\tau$ (improper, spike at 0, like (c) but more so) and uniform on $\tau^2$ (like (a) with a slightly higher right tail). The simple uniform on $\tau$ performs well. The plots' appearance depends on plotting on the $\tau$ scale. On the $\log\tau$ scale the inverse-gamma(0.001,0.001) would look flattest, yet it is not noninformative because the likelihood does not constrain $\log\tau\to-\infty$ (p. 131).

**3 schools (pp. 131–132).** Using only the first three schools (Figure 5.10):
- Uniform on $\tau$ gives an extremely long right tail. This is expected since $J$ is so low (any lower and the tail integral would be infinite), and it will under-pool.
- Half-Cauchy with scale $A=25$ (a bit above the expected sd of the $\theta_j$) is high over plausible $\tau<50$ and falls off gradually. It keeps the low-end likelihood and removes much of the unrealistic upper tail.
- A weakly informative prior is "not intended to represent our actual prior state of knowledge about $\tau$ but rather to constrain the posterior distribution, to an extent allowed by the data" (p. 132). It would also work for 8 schools but was unnecessary.

> **Intuition note.** The data can never rule out $\tau=0$, but with few groups they also cannot rule out huge $\tau$. A weakly informative prior only trims the absurd upper tail and leaves the likelihood in charge elsewhere.

### 5.8 Bibliographic note (pp. 132–133)
A literature survey. Named threads: Stein and James–Stein shrinkage work; Efron–Morris; Robbins; de Finetti (1974); Good (1965); Mosteller and Wallace (1964); empirical Bayes papers; full Bayesian normal-means treatments (Hill, Tiao–Tan, Lindley); Box and Tiao (1973); small-area estimation; connections to graphical models and the Bugs package; the rat data (Tarone 1982; Dempster, Selwyn and Weeks 1983); Rubin (1981a) as source for 5.4–5.5; Gelman (2006a) for the half-Cauchy prior; Carlin (1992) and Yusuf et al. (1985) for 5.6 (pp. 132–133).

### 5.9 Exercises (pp. 134–137)
Seventeen exercises: exchangeability with known and unknown parameters (1–2), multiple comparisons in the eight schools (3), exchangeable priors and de Finetti (4–5), the divorce example (6), mixture models (7–8), hyperprior integrability (9–10), nonconjugate models (11), conditional posterior moments (12), Berkeley bicycle data with hierarchical binomial and Poisson models (13–14), meta-analysis computations and "equivalent data" (15–16), and priors for a free-throw training study (17) (pp. 134–137).

## Toy example (ours, not from the text)
Take the normal model (5.11)–(5.17) with $J=2$ groups and known hyperparameters $\mu=6$, $\tau^2=4$. Group 1: $\bar y_{.1}=10$, $\sigma_1^2=4$. Group 2: $\bar y_{.2}=4$, $\sigma_2^2=16$.

- Group 1: precisions $1/\sigma_1^2=0.25$, $1/\tau^2=0.25$. $\hat\theta_1=(0.25\cdot10+0.25\cdot6)/0.5=(2.5+1.5)/0.5=8$, $V_1=1/0.5=2$. The weight on its own mean is $0.25/0.5=0.5$.
- Group 2: $1/\sigma_2^2=0.0625$. $\hat\theta_2=(0.0625\cdot4+0.25\cdot6)/0.3125=(0.25+1.5)/0.3125=5.6$, $V_2=1/0.3125=3.2$. Weight on own mean $=0.0625/0.3125=0.2$. Equivalently, $0.2\cdot4+0.8\cdot6=5.6$.
- The noisier group 2 is shrunk more. If $\tau^2\to0$ both weights go to 0 (complete pooling at $\mu$). If $\tau^2\to\infty$ both go to 1 (no pooling).
- If $\mu$ were unknown, (5.20) with $\tau^2=4$ uses variances $\sigma_j^2+\tau^2=8$ and $20$: $\hat\mu=(10/8+4/20)/(1/8+1/20)=1.45/0.175\approx8.29$, and $V_\mu^{-1}=0.175$, so $V_\mu\approx5.71$.

## Concepts
- [[hierarchical-model]] — observables given parameters, parameters given hyperparameters; here a population distribution on the $\theta_j$ with hyperprior on $\phi$ (p. 101)
- [[hyperparameters-and-hyperprior]] (new) — parameters $\phi$ of the population distribution, and the prior $p(\phi)$ placed on them (pp. 101, 107)
- [[exchangeability]] — joint density invariant to permuting indexes; the form of "no information distinguishes units" (p. 104)
- [[de-finetti-theorem]] (new) — as $J\to\infty$, suitably well-behaved exchangeable distributions are mixtures of i.i.d. ones; false for finite $J$ (p. 105)
- [[partial-pooling-shrinkage]] — estimates are weighted combinations of group and overall means, shrunk more for noisier groups (pp. 115–116, 112–113)
- [[conjugate-prior]] — here, conditional/partial conjugacy makes $p(\theta|\phi,y)$ a product of known densities (pp. 108–109, 115)
- [[marginal-likelihood]] — $p(y|\mu,\tau)$ with $\theta$ integrated out, e.g. $\bar y_{.j}\sim\text{N}(\mu,\sigma_j^2+\tau^2)$ (p. 116)
- [[posterior-predictive-distribution]] — two kinds: for existing $\theta_j$ or for new $\tilde\theta_j$ from the population (p. 108)
- [[empirical-bayes]] (new) — estimating prior parameters from the data by a point estimate; viewed as approximating full hierarchical Bayes (p. 104)
- [[improper-prior-posterior-propriety]] (new) — improper priors as limits of proper ones; the posterior must be checked for integrability (pp. 107, 110, 128)
- [[weakly-informative-prior]] (new) — a proper prior that only mildly constrains the posterior, not meant as real prior knowledge (p. 132)
- [[posterior-calibration]] (new) — miscalibration $E(\theta|\hat\theta)-\hat\theta$, the Bayesian analogue of bias (p. 128)
- [[meta-analysis]] (new) — combining parallel studies via an exchangeable hierarchical model on study effects (p. 124)
- [[monte-carlo-integration]] — posterior simulation by drawing hyperparameters, then parameters, then predictions (p. 109)

## Canonical instances
- [[rat-tumor-example]] — beta–binomial hierarchy, 70 historical groups; point-estimate vs full Bayes (pp. 102–113)
- [[divorce-rates-exchangeability]] — how information about states breaks or preserves exchangeability (pp. 105–106)
- [[eight-schools]] — SAT coaching; separate vs pooled vs hierarchical (pp. 119–123, 130–131)
- [[three-schools-half-cauchy]] — weakly informative prior needed for $J=3$ (pp. 131–132)
- [[beta-blocker-meta-analysis]] — 22 trials, log-odds ratios, predicted effect in a new study (pp. 124–128)
- [[die-face-probabilities]] — exchangeable but not an i.i.d. mixture (p. 105)

## Bridges (candidates)
- [same-math] (5.17) precision-weighted posterior mean ↔ conjugate normal–normal updating: the same formula applied per group given $(\mu,\tau)$.
- [structural-analogy] de Finetti mixture (5.2) ↔ exchangeability in the canon: (5.2) is an exchangeable form, and de Finetti's theorem gives the converse only as $J\to\infty$, not for finite $J$.
- [structural-analogy] Partial pooling toward a mean ↔ ensemble or regularized estimators: both trade group-specific fit for stability.
- [structural-analogy] Posterior calibration ↔ frequentist bias: conditions on data instead of on the true parameter.
- [metaphor] Using a population to inform a unit ↔ borrowing strength across studies in evidence synthesis (the text's phrase for the beta-blocker case).

## Questions this raises
- How do these conclusions change if the normal population distribution is wrong (heavy tails, outliers)? The text points to Chapter 6 checks (p. 126).
- When should covariates replace exchangeability, e.g. a hierarchical regression for study-level predictors (pp. 106, 126)?
- How would one sample from the posterior when the model is nonconjugate, e.g. a normal population on the logit scale (p. 109; Exercise 11)?
- How should a weakly informative prior's scale be chosen when $J$ is small, and how sensitive are the results to it (p. 132)?

## Exercises worth doing
- Ex. 2 (p. 134) — exchangeable vs independent vs "as if independent" with unknown parameters; difficulty: easy
- Ex. 4 (p. 134) — a finite exchangeable prior that is not an i.i.d. mixture, and why $J\to\infty$ does not give a counterexample to de Finetti; difficulty: medium
- Ex. 5 (p. 134) — mixtures of i.i.d. components have nonnegative covariances; difficulty: medium
- Ex. 10 (p. 136) — integrability of the normal-model posterior under $p(\tau)\propto\tau^{-1}$ vs uniform; difficulty: hard
- Ex. 12 (p. 136) — derive $E(\theta_j|\tau,y)$ and $\text{var}(\theta_j|\tau,y)$ behind Figures 5.6–5.7; difficulty: medium
- Ex. 3 (p. 134) — multiple-comparison probabilities from eight-schools simulations, under hierarchical, $\tau=\infty$ and $\tau=0$ models; difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 111 = printed 101). In the text layer, pdf 148 (printed 138) contains only the running header line.
- The extracted text layer garbles symbols: $\theta$ appears as "ω", "∼" and "−" as "→", and fractions and gamma functions are broken (e.g. "5/2" exponents shown as "→5/2"). Page images show $\theta$, $\sim$, $-$.
- Figure 5.1 text is garbled in the layer. The image shows $\alpha,\beta$ pointing to $\theta_1\dots\theta_{71}$, each pointing to $y_j$.
- $5.4/24=0.225$, but the page prints posterior mean 0.223; presumably the printed (1.4, 8.6) are rounded (our inference, not stated on the page).
- On p. 120 the $\chi^2$ formula uses $\sigma_i^2$ in the denominator where $\sigma_j^2$ is evidently meant (the image shows an $i$).
- Several results are described as "not shown" (the $y_j/n_j$ vs $n_j$ plot on p. 107; the $p(\tau|y)$ plot, individual-effect histograms and $\mu|\tau$ graphs on p. 127). Table 5.4's posterior quantile columns and Table 5.1 are not reproduced here, and the Bibliographic note is summarized only.
- On p. 130 the text says "model (5.21)" for the $\tau$ marginal; (5.21) is the marginal density of $\tau$ in the normal model.
