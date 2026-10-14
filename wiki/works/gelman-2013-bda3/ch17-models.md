---
id: gelman-2013-bda3/ch17-models
work: gelman-2013-bda3
unit: "17 Models for robust inference"
pages: 435–448
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
# Models for robust inference

## L0 — One line
Replacing normal, binomial and Poisson models by longer-tailed or overdispersed mixture versions (such as the t) lets outliers have less influence, and the effect of such a choice can be checked by sensitivity analysis computed with Gibbs sampling, importance weighting or EM.

## L1 — The gist (≤ 120 words)
Normal-based models can let one extreme observation affect inferences for all parameters. The chapter asks how posterior inference depends on extreme data and on unassessable model assumptions, and how to reduce outlier influence without leaving Bayesian principles. The answer is to expand the model with a hyperparameter φ: t instead of normal, negative binomial instead of Poisson, beta-binomial instead of binomial, robit instead of logit or probit. Each expansion is a mixture and can be fitted by Gibbs sampling, EM or importance resampling. In the eight-schools example, the inferences barely change under t distributions. Robustness is relative to the estimand, and checking it shows which conclusions rest on the tails.

**Prerequisites:** hierarchical normal model (eight schools); Gibbs sampling and Metropolis steps; importance sampling and resampling; EM algorithm; weighted least squares; scaled inverse-χ² and gamma/beta distributions. Terms used early: outlier (extreme observation); estimand (quantity being estimated); hyperparameter (parameter of the model family or prior); shrinkage (pulling estimates toward a common mean); overdispersed (variance larger than the standard model gives); robit (binary regression with $t$-distributed latent errors).

## L2 — Key ideas (5–10 bullets)
- Normal-based models are nonrobust: one aberrant point can affect all parameters. A longer-tailed exchangeable prior (t, Cauchy, mixture) reduces its influence without changing Bayesian principles. (p. 435–436)
- Searching for outliers and robust procedures are not separate in the Bayesian view. A mixture model labels extreme points as coming from a high-variance component, which also gives them less influence. (p. 436)
- Each standard model has a one-parameter overdispersed extension that is a mixture: t (normal), negative binomial (Poisson), beta-binomial (binomial), robit (logit/probit). These can never be underdispersed. (p. 437–438)
- The t equals a normal scale mixture (17.1), so the mixture variables $V_i$ become auxiliary variables for Gibbs and EM. (p. 437, 438, 440, 444)
- Sensitivity analysis can reuse draws from the original posterior: the average importance ratio (17.3) gives $p(\phi\mid y)$ up to a constant, and importance resampling approximates $p(\theta\mid\phi,y)$. Highly variable ratios signal sensitivity or unreliable approximation. (p. 440–441)
- Eight schools: with a $t_4$ population model, inferences are essentially unchanged from the normal model, with slightly less shrinkage for school A. Varying $\nu$ shows no apparent systematic sensitivity. (p. 441–443)
- Robustness depends on the estimand: in the SAT example, medians and 50%/95% intervals are insensitive to the normal assumption (at least compared with the t family), while 99.9% intervals may not be. (p. 444)
- In t regression, EM is iteratively reweighted least squares, with weights $E(1/V_i)$ that are small for large residuals. Low-$\nu$ posteriors can be multimodal. (p. 444–445)

## L3 — Walkthrough

### Chapter introduction (p. 435)
Normal, binomial, Poisson and their hierarchical combinations give a limited class of inferences. Models should fit the science and data, not convenience. If simple models are used, one should ask how posterior inference depends on extreme data and on unassessable assumptions. The second part is sensitivity analysis (Chapter 6), revisited here with stronger computation. (p. 435)

### 17.1 Aspects of robustness
**Outliers.** Normal models are "nonrobust": a single aberrant point can strongly affect inference for all parameters, even ones with little connection to it. (p. 435)

*Hypothetical example (eight schools).* The estimates shrink each school mean toward the grand mean. The shrinkage for school $j$ depends only on $\sigma_j$ and $\tau$. Suppose $y_8$ were 100 instead of 12, so the data are 28, 8, −3, 7, −1, 1, 18, 100, with the same standard errors. The hierarchical normal model would then give $\tau$ a high value, and each $\hat\theta_j$ would be essentially $y_j$. The author doubts this makes sense: school 8 may truly be extreme, or 100 may be a recording error. Either way, $y_8$ should not so strongly affect $\theta_1,\dots,\theta_7$. (p. 435)

*Remedy.* Replace the normal population model by a **long-tailed** family. Long-tailed means relatively high probability far from the center, where "far" is judged against the width of the central 50% region. Examples are the t family (the Cauchy is $t_1$) and finite mixtures. A mixture uses a simple distribution (e.g. normal) for most values, plus a discrete probability of values from an alternative with different center and generally much larger spread. (p. 435–436)

With a long-tailed prior, 100 is read as an extreme draw rather than as evidence that the effects have large variance. The eighth observation is shrunk somewhat toward the others, but much less (relative to its distance from the mean) than the first seven. The author says $\Pr(\theta_8>100\mid y)$ should presumably be somewhat below 0.5, which justifies some shrinkage. (p. 436)

A Cauchy or two-component mixture is still an exchangeable prior, appropriate when nothing distinguishes the schools beforehand. The prior changes how shrinkage works, so outlier influence is reduced without a different treatment of the outlier. This does not replace checking the data for recording errors. In the Bayesian framework, "searching for outliers" and "robust procedures" should not be distinguished. Mixture models (finite mixtures, Chapter 22, or overdispersed standard models) classify extreme points as high-variance components and also reduce their influence on estimands such as means and medians. (p. 436)

*Intuition note.* A normal prior says "big effects are almost impossible", so a big observation pushes $\tau$ high. A heavy-tailed prior says "big effects happen sometimes", so the same observation is read as one rare case: $\tau$ is not pushed high, and the other schools are still shrunk toward each other.

**Sensitivity analysis.** Robust models also assess sensitivity: e.g. use a t in place of the normal and vary the degrees of freedom from large to small. The general idea is to try different likelihood and prior distributions and see how posterior inferences for estimands and predictions vary. After drawing from one model's posterior, draws from alternatives can often be obtained by importance resampling accurately enough to detect major differences (Section 17.3). If inferences are highly sensitive, iterative simulation may be needed. In a sense, much of the SAT analysis (Figures 5.6, 5.7) is a sensitivity analysis in which $\tau$ varies from 0 to ∞. The data are consistent with $\tau=0$, but that makes no substantive sense, so $\tau$ is allowed to be any positive value. (p. 436)

### 17.2 Overdispersed versions of standard models
Sometimes a standard model fits except that the data are too dispersed. For example, the normal should not fit a large sample where 10% of points lie more than 1.5 interquartile ranges from the median. Each standard model has an extension with one added parameter for overdispersion, and each has a mixture interpretation. These extensions can never be underdispersed: the mean equals that of the base family and the variance is higher (cf. (2.7), (2.8)). For underdispersed data, use different models. (p. 437)

**t instead of normal.** The $t_\nu(\mu,\sigma^2)$ has center $\mu$, scale $\sigma$ and degrees of freedom $\nu\in(0,\infty)$. It is symmetric. At $\nu=1$ it is the Cauchy, with infinite mean and variance. As $\nu\to\infty$ it approaches the normal. It can handle (1) occasional unusual observations in the data or (2) occasional extreme parameters in a prior or hierarchy. If the t is meant to fit a long-tailed distribution well from a reasonably large amount of data, $\nu$ should generally be unknown. If the t is only a robust alternative to the normal, $\nu$ can be fixed small, but no smaller than prior understanding allows. $t_1$ and $t_2$ have infinite variance and are not usually realistic in the far tails. (p. 437)

*Mixture interpretation.* $y_i\sim t_\nu(\mu,\sigma^2)$ is equivalent to
$$y_i\mid V_i\sim \mathrm{N}(\mu,V_i),\qquad V_i\sim \text{Inv-}\chi^2(\nu,\sigma^2).\tag{17.1}$$
Observations with large $V_i$ are the outliers. The same holds for exchangeable parameters $\theta_j$. (p. 437)

**Negative binomial instead of Poisson.** The Poisson requires variance = mean, but counts are often overdispersed. The negative binomial has two parameters, so mean and variance fit separately, with variance at least the mean. Data $y_i\sim$ Neg-bin$(\alpha,\beta)$ are Poisson with means $\lambda_i\sim\text{Gamma}(\alpha,\beta)$. The variance is $\frac{\beta+1}{\beta}\frac{\alpha}{\beta}$, always above the mean $\alpha/\beta$. As $\beta\to\infty$ with $\alpha/\beta$ constant, the gamma becomes a spike and the negative binomial approaches the Poisson. (p. 437–438)

**Beta-binomial instead of binomial.** The binomial has one free parameter, so the variance is set by the mean. The beta-binomial is a beta mixture of binomials. Example: educational testing, where individuals differ greatly in probability of a correct response. Data $y_i\sim$ Beta-bin$(m,\alpha,\beta)$ are binomial with common $m$ and probabilities $\pi_i\sim\text{Beta}(\alpha,\beta)$. For the same mean probability $\alpha/(\alpha+\beta)$, the variance is larger than the binomial's by the factor $\frac{\alpha+\beta+m}{\alpha+\beta+1}$. For $m=1$ the variances are equal, since beta and binomial variation cannot be told apart. (p. 438)

**t instead of logistic/probit (robit).** For large $|X\beta|$, logit and probit give probabilities near 0 or 1. Robustness here concerns the predictors $X$, not $y$: the model should fit most data but allow isolated errors. In the latent-variable form (p. 408), replace the logistic or normal latent $u_i$ by $u_i\sim t_\nu((X\beta)_i,1)$. In realistic settings estimating $\nu$ is impractical because $u_i$ is never directly observed, so $\nu$ is set low. $\nu=4$ gives a distribution close to the logistic, and $\nu\to\infty$ approaches the probit. Computation uses EM and Gibbs sampling with the mixture form (17.1), treating $u_i$ and each variance as missing data. (p. 438)

**Why ever use a nonrobust model?** Standard models have logical status: binomial/multinomial for i.i.d. counts with fixed total; Poisson/exponential for events and waiting times of a Poisson process; normal, by the central limit theorem, for sums of many independent components. In the schools, each $y_j$ is based on about 60 students, so $y_j\mid\theta_j,\sigma_j^2\sim\mathrm N(\theta_j,\sigma_j^2)$ is accurate. Standard models are also computationally convenient (conjugate priors), e.g. normal models for logs or logits. Such arbitrary choices should be checked with the posterior predictive distribution (Chapter 6). If non-robustness is a worry, do a sensitivity analysis with a larger family such as the t. (p. 438–439)

### 17.3 Posterior inference and computation
Methods of Part III apply. Draws from the original posterior can serve as a less time-consuming starting point for expanded models. (p. 439)

**Notation.** $p_0(\theta\mid y)$ is the posterior of the original model (already fitted). $\phi$ is the hyperparameter(s) of the expanded model. The goal is to sample from
$$p(\theta\mid\phi,y)\propto p(\theta\mid\phi)\,p(y\mid\theta,\phi),\tag{17.2}$$
for fixed $\phi$ (e.g. $\nu=4$) or a range of $\phi$, in which case we also want $p(\phi\mid y)$. The robust family can enter through $p(\theta\mid\phi)$ or $p(y\mid\theta,\phi)$. A joint prior $p(\theta,\phi)$ is needed and requires care, since it captures prior dependence. (p. 439)

**Gibbs sampling with the mixture form.** Sample jointly the parameters and the extra unobserved scale variables ($V_i$ in the t, $\lambda_i$ in the negative binomial, $\pi_i$ in the beta-binomial). For $t_\nu(\mu,\sigma^2)$ with $\nu$ known, the sampler is as in Section 12.1. If $\nu$ is unknown, add a step for its conditional posterior. No simple method exists, so use a Metropolis step. Such posteriors are commonly multimodal, with modes corresponding to different observations in the tails. Extra work (e.g. simulated tempering, Section 12.3) is then needed to find and jump between modes. (p. 440)

**Posterior predictive draws.** Draw $\theta\sim p(\theta\mid\phi,y)$, then $\tilde y\sim p(\tilde y\mid\phi,\theta)$. For mixtures, first draw the mixture indicators, then $\tilde y$. For the t: draw $V\sim\text{Inv-}\chi^2(\nu,\sigma^2)$, then $\tilde y\sim\mathrm N(\mu,V)$. (p. 440)

**Marginal posterior of $\phi$ by importance weighting.** Assume draws $\theta^s$, $s=1,\dots,S$, from $p_0(\theta\mid y)$. Using identity (13.11):
$$p(\phi\mid y)\propto p(\phi)\int\frac{p(\theta\mid\phi)p(y\mid\theta,\phi)}{p_0(\theta)p_0(y\mid\theta)}\,p_0(\theta)p_0(y\mid\theta)\,d\theta
\propto p(\phi)\int\frac{p(\theta\mid\phi)p(y\mid\theta,\phi)}{p_0(\theta)p_0(y\mid\theta)}\,p_0(\theta\mid y)\,d\theta .$$
The proportionality constant is $1/p(y)$ in the first line and $p_0(y)/p(y)$ in the second. Up to a constant, $p(\phi\mid y)$ is estimated by the average importance ratio
$$p(\phi)\,\frac1S\sum_{s=1}^S\frac{p(\theta^s\mid\phi)\,p(y\mid\theta^s,\phi)}{p_0(\theta^s)\,p_0(y\mid\theta^s)},\tag{17.3}$$
evaluated with the same $S$ draws over a grid of $\phi$ and graphed. (p. 440)

**Importance resampling.** Start with large $S$ (say 5000) draws from $p_0(\theta\mid y)$. For each $\phi$, draw a subsample of $k$ (say 500) without replacement, each drawn with probability proportional to
$$\frac{p(\theta\mid\phi,y)}{p_0(\theta\mid y)}=\frac{p(\theta\mid\phi)p(y\mid\theta,\phi)}{p_0(\theta)p_0(y\mid\theta)}.$$
New subsamples are drawn for each $\phi$ from the same $S$ draws (details in Section 10.4). This works if the largest ratios are plentiful and not too variable. If they vary greatly, this indicates potential sensitivity, because $p(\theta\mid\phi,y)/p_0(\theta\mid y)$ depends strongly on the drawn $\theta$. If accurate robust inference is wanted anyway, use Markov chain simulation. (p. 441)

*Intuition note.* Re-weighting old draws is cheap, and it works when the largest importance ratios are plentiful and not too variable. If the ratios vary greatly, the inference is potentially sensitive to the model, which is itself a warning.

### 17.4 Robust inference for the eight schools
The data model $y_j\sim\mathrm N(\theta_j,\sigma_j^2)$, $\sigma_j$ known, needs little defence given the large samples. The normal population model $\theta_j\sim\mathrm N(\mu,\tau^2)$ is harder to justify, although Section 6.5 checks suggest it is adequate for posterior intervals. Posterior inferences can be highly sensitive to the model even when it fits. The alternative is
$$\theta_j\mid\nu,\mu,\tau\sim t_\nu(\mu,\tau^2),\quad j=1,\dots,8.\tag{17.4}$$
Notation: $p(\theta,\mu,\tau\mid\nu,y)$ under the $t_\nu$ model; $p_0(\theta,\mu,\tau\mid y)\equiv p(\theta,\mu,\tau\mid\nu=\infty,y)$ under the normal model. (p. 441)

**Robust inference with $t_4$.** Concerns: the normal model may pull extreme effects too far toward the grand mean (school A may differ from the others), and the largest effect (school A) may unduly influence $\tau^2$ and so the other estimates. Programs vary greatly, so a long-tailed population may fit better. The analysis uses $\nu=4$, with likelihood $\prod_j \mathrm N(y_j\mid\theta_j,\sigma_j^2)$ and hyperprior $p(\mu,\tau\mid\nu)\propto1$ unchanged. (p. 441)

*Gibbs.* Section 12.1 approach with $\nu=4$; 2500 draws (last halves of five chains of length 1000). Table 17.1 gives posterior quantiles; the results are essentially identical, for practical purposes, to the normal model of Table 5.3, with slightly less shrinkage for extreme schools such as A. (p. 441–442)

| School | 2.5% | 25% | median | 75% | 97.5% |
|---|---|---|---|---|---|
| A | −2 | 6 | 11 | 16 | 34 |
| B | −5 | 4 | 8 | 12 | 21 |
| C | −14 | 2 | 7 | 11 | 21 |
| D | −6 | 4 | 8 | 12 | 21 |
| E | −9 | 1 | 6 | 9 | 17 |
| F | −9 | 3 | 7 | 10 | 19 |
| G | −1 | 6 | 10 | 15 | 26 |
| H | −8 | 4 | 8 | 13 | 26 |

*Importance resampling.* Draw 5000 $(\theta,\mu,\tau)$ from $p_0$. The importance ratio is
$$\frac{p(\theta,\mu,\tau\mid\nu,y)}{p_0(\theta,\mu,\tau\mid y)}\propto\frac{p(\mu,\tau\mid\nu)p(\theta\mid\mu,\tau,\nu)p(y\mid\theta,\mu,\tau,\nu)}{p_0(\mu,\tau)p_0(\theta\mid\mu,\tau)p_0(y\mid\theta,\mu,\tau)}=\prod_{j=1}^8\frac{t_\nu(\theta_j\mid\mu,\tau^2)}{\mathrm N(\theta_j\mid\mu,\tau^2)}.\tag{17.5}$$
Likelihood and hyperprior factors cancel. Resample 500 without replacement. The approximation is probably sufficient to assess robustness, but the long tail of the log importance ratios (not shown) indicates serious problems for accurate inference by importance resampling. (p. 442)

**Sensitivity to $\nu$.** Fit $\nu=1,2,3,5,10,30$ by Markov chain simulation (with $\nu=\infty$ and $\nu=4$ already done). Figure 17.1 plots posterior means and standard deviations of the $\theta_j$ against $1/\nu$. This scale includes the normal at $1/\nu=0$ and covers normal to Cauchy in $[0,1]$. There is some variation but no apparent systematic sensitivity to $\nu$. Much scatter is simulation variability. (p. 442–443)

**Treating $\nu$ as unknown.** Averaging over $\nu$ is generally a key step, since we care mainly about sensitivity to models the data support. Here inferences are so insensitive that it is unnecessary, and it is shown as an illustration. (p. 443)

*Prior.* Uniform on $1/\nu\in[0,1]$ (normal to Cauchy). This favors long tails: half the prior probability lies between $t_1$ and $t_2$. The conditional prior $p(\mu,\tau\mid\nu)\propto g(\nu)$ is improper, so its dependence on $\nu$ must be specified. In the t family, $\mu$ and $\tau$ describe the median and the curvature (second derivative) at the median, not mean and variance. $\mu$ seems to have a reasonable invariant meaning (equal to the mean except for the Cauchy). The interquartile range would perhaps be a better basis for a prior than curvature, but variance cannot be used because it is infinite for $\nu\le2$. The interquartile range varies mildly with $\nu$, so for simplicity $g(\nu)\propto1$, giving an improper uniform prior on $(\mu,\tau,1/\nu)$. If inferences depended strongly on $\nu$, this prior should be refined. (p. 443)

*Posterior.* Add a Metropolis step for $1/\nu$ to the Gibbs sampler (Appendix C); Figure 17.2 shows a histogram of $1/\nu$ draws. Alternatively approximate $p(\phi\mid y)$ with importance sampling and (17.3). Since Figure 17.1 shows only minor effects, the Section 5.5 results are not strongly dependent on the normal assumption. Had there been strong dependence, as Figures 5.5–5.7 showed for $\tau$, one might include $\nu$ as a hyperparameter after thinking more seriously about a joint noninformative prior for $(\mu,\tau,\nu)$. (p. 443–444)

**Discussion.** Robustness depends on the estimand. Posterior medians, 50% and 95% intervals for the school effects are insensitive to the normal assumption (compared with the t family). 99.9% intervals may well depend strongly on tails and on $\nu$, but such extreme tails are unlikely to be of substantive interest here. (p. 444)

### 17.5 Robust regression using t-distributed errors
Normal linear regression (Chapter 14) is sensitive to outliers. With a t error distribution having few degrees of freedom, far-off observations are treated as high-variance, which resembles downweighting outliers (weights in weighted regression are inverse variances). (p. 444)

**Iterative weighted regression and EM.** Model: $p(y_i\mid X_i\beta,\sigma^2)=t_\nu(y_i\mid X_i\beta,\sigma^2)$, $\nu$ fixed, written as the mixture (17.1) with mean $X_i\beta$. Prior $p(\mu,\log\sigma\mid\nu)\propto1$ (as printed). The posterior mode of $p(\beta,\log\sigma\mid\nu,y)$ can be found by Newton's method (Section 13.1) or other mode-finding. Alternatively use EM with $\gamma=(V_1,\dots,V_n)$ as missing data (Section 13.4). The E-step computes the expected normal-model sufficient statistics $(\sum y_i^2/V_i,\ \sum y_i/V_i,\ \sum 1/V_i)$ given $(\beta^{\rm old},\sigma^{\rm old})$. It is enough to note that
$$V_i\mid y_i,\beta^{\rm old},\sigma^{\rm old},\nu\sim\text{Inv-}\chi^2\!\left(\nu+1,\ \frac{\nu(\sigma^{\rm old})^2+(y_i-X_i\beta^{\rm old})^2}{\nu+1}\right)\tag{17.6}$$
and
$$\mathrm E\!\left(\frac1{V_i}\,\Big|\,y_i,\beta^{\rm old},\sigma^{\rm old},\nu\right)=\frac{\nu+1}{\nu(\sigma^{\rm old})^2+(y_i-X_i\beta^{\rm old})^2}.$$
M-step: weighted regression with diagonal $n\times n$ matrix $W$ holding these expectations,
$$\hat\beta^{\rm new}=(X^TWX)^{-1}X^TWy,\qquad(\hat\sigma^{\rm new})^2=\tfrac1n(y-X\hat\beta^{\rm new})^TW(y-X\hat\beta^{\rm new}),$$
with $X$ the $n\times p$ matrix of predictors ($y$ is $n\times1$, $\beta$ is $p\times1$). The iterations equal iterative weighted least squares: cases with large residuals get less weight. If $\nu$ is unknown, ECME adds a step updating $\nu$. (p. 445)

*Intuition note.* The weight $(\nu+1)/(\nu\sigma^2+r_i^2)$ falls as the residual $r_i$ grows. EM therefore refits the line with less weight on points that the current line fits badly, and repeats.

**Other robust models.** Changing the model for the $V_i$ gives other robust models, e.g. a two-point distribution for contaminated errors. The computations are the same except that the E-step uses the appropriate conditional mean. (p. 445)

**Gibbs and Metropolis.** Draw $p(\beta,\sigma^2,V_1,\dots,V_n\mid\nu,y)$ by alternating: $(\beta,\sigma^2)\mid V,\nu,y$ from the usual weighted-regression posterior, and $V\mid\beta,\sigma^2,\nu,y$ as independent scaled inverse-χ² draws (17.6). Parameter expansion (Section 12.1) can be even more effective. If $\nu$ is unknown, add a Metropolis step. With low $\nu$ the posterior can have many modes and the samplers can get stuck, so run many simulations from overdispersed starting points. (p. 445)

### 17.6 Bibliographic note (p. 445–446)
Cited early robustness work: Mosteller and Wallace (1964, negative binomial in place of Poisson, with sensitivity study); Box and Tiao (1968); Smith (1983, t family with inverse degrees of freedom). Berger and coworkers studied theoretical Bayesian robustness. Computation: Dempster, Laird and Rubin (1977, EM for t models); faster EM extensions (Liu and Rubin, Meng and van Dyk); Raghunathan and Rubin (1990, importance resampling). Liu (2004) presents the robit. Taplin and Raftery (1994) use a finite mixture for agricultural experiments.

### 17.7 Exercises (p. 446–447)
Listed under "Exercises worth doing".

## Toy example (ours, not from the text)
One EM step for a $t_4$ location model with intercept only ($X_i=1$, $n=4$, $p=1$). Data $y=(1,2,3,30)$. Current values $\beta^{\rm old}=2$, $\sigma^{\rm old}=1$, $\nu=4$.

Weights $w_i=(\nu+1)/(\nu\sigma^2+r_i^2)=5/(4+r_i^2)$, with residuals $r=(-1,0,1,28)$:
- $w_1=5/5=1$
- $w_2=5/4=1.25$
- $w_3=5/5=1$
- $w_4=5/(4+784)=5/788\approx0.00635$

M-step: $\hat\beta^{\rm new}=\sum w_iy_i/\sum w_i$.
- Numerator: $1(1)+1.25(2)+1(3)+0.00635(30)=1+2.5+3+0.190=6.690$.
- Denominator: $1+1.25+1+0.00635=3.2563$.
- $\hat\beta^{\rm new}\approx2.055$.

The plain mean is $36/4=9$, so the outlier 30 is almost ignored. For the variance, $(y_i-2.055)^2=(1.112,\,0.003,\,0.894,\,780.9)$. Weighted sum $=1.112+0.004+0.894+4.955=6.965$. Dividing by $n=4$ gives $(\hat\sigma^{\rm new})^2\approx1.74$.

## Concepts
- [[robust-inference]] (new) — inference whose conclusions depend little on outliers or on untestable model assumptions; here reached by expanding the model, so outliers need no fundamentally different treatment (p. 435–436)
- [[heavy-tailed-prior]] (new) — long-tailed (t, Cauchy, mixture) exchangeable population model; an extreme observation is shrunk somewhat but proportionally much less than the others are shrunk toward each other (p. 436)
- [[overdispersion]] (new) — variance exceeding what the standard model implies; the extensions here can never be underdispersed (p. 437)
- [[scale-mixture-of-normals]] (new) — $t_\nu$ as normal with variance $V_i\sim$ Inv-$\chi^2$; basis for Gibbs and EM (p. 437)
- [[negative-binomial-beta-binomial]] (new) — gamma mixture of Poissons and beta mixture of binomials as overdispersed count models (p. 437–438)
- [[robit-regression]] (new) — binary regression with latent $t_\nu$ errors, $\nu$ fixed low (p. 438)
- [[sensitivity-analysis]] (new) — varying distributional assumptions (via a hyperparameter $\phi$) and tracking posterior changes in estimands (p. 436, 439)
- [[importance-weighting-for-model-expansion]] (new) — average importance ratio (17.3) estimating $p(\phi\mid y)$; importance resampling approximates $p(\theta\mid\phi,y)$ (p. 440–441)
- [[em-iteratively-reweighted-least-squares]] (new) — EM for $t$ regression equals IRLS with weights $E(1/V_i)$ (p. 445)
- [[exchangeability]] — a Cauchy or mixture prior is still exchangeable, so robust models stay Bayesian (p. 436)
- [[partial-pooling-shrinkage]] — shrinkage of school estimates, whose amount depends on the prior's tails (p. 435–436)
- [[posterior-predictive-check]] — recommended for arbitrarily assigned models (p. 439)
- [[hierarchical-multilevel-model]] — t population model for the eight schools (p. 441)
- [[gibbs-sampling]] and [[metropolis-hastings]] — Gibbs with mixture variables; Metropolis step for $\nu$ (p. 440)

## Canonical instances
- [[eight-schools]] — hypothetical $y_8=100$ motivates robustness; $t_4$ and varying-$\nu$ analyses show insensitivity for the real data (p. 435, 441–444)
- [[federalist-word-counts]] — Table 17.2: 'may' counts per 200-word block for Hamilton and Madison, used for Poisson vs negative binomial exercises (p. 446–447)
- [[newcomb-speed-of-light]] — dataset for robust-model and contamination exercises (p. 447)

## Bridges (candidates)
- [same-math] t as normal scale mixture ↔ Bayesian linear regression: weighted regression with weights $1/V_i$, so robust regression is IRLS (p. 444–445)
- [structural-analogy] Heavy-tailed prior on group effects ↔ Hierarchical models: tail shape of the population distribution sets how strongly extreme groups are shrunk
- [structural-analogy] Importance reweighting of old draws for model expansion ↔ Bayesian workflow: cheap model comparison without refitting
- [same-math] Gamma–Poisson and beta–binomial mixtures ↔ Hierarchical models: unit-level rates drawn from a population distribution

## Questions this raises
- When the importance ratios are heavy-tailed, as for $t_4$ vs normal here, how can one tell whether resampling is trustworthy?
- If $p(\mu,\tau\mid\nu)$ is improper, how should one choose $g(\nu)$ when inferences do depend on $\nu$ (as the $y_8=100$ case in Exercise 8 is said to be)?
- Which estimands (e.g. extreme-tail intervals) stay sensitive to tail shape even when medians do not?
- How should one handle multimodality of $t$ posteriors with low $\nu$ when $\nu$ is unknown?

## Exercises worth doing
- Ex. 1 (p. 446) — two-component mixture prior for school effects; compute posterior and graph $\theta_8$ for $y_8=0,25,50,100$ to see how shrinkage changes — difficulty: medium
- Ex. 2 (p. 446–447) — Poisson vs negative binomial fits to Hamilton/Madison 'may' counts — difficulty: medium
- Ex. 3 (p. 447) — posterior predictive checks of those two models — difficulty: medium
- Ex. 7 (p. 447) — derive EM and Gibbs for the iid $t_\nu$ model with the $V_i$ mixture; apply to speed-of-light data with $t_2$ — difficulty: hard
- Ex. 8 (p. 447) — redo Section 17.4 with $y_8=100$; check sensitivity to $\nu$ and find the best-supported $\nu$ — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 445–458 = printed 435–448). Printed 448 is blank apart from the running header.
- The text layer garbles some symbols: $\theta$ appears as ω, "∼" as "→", and "ν = 4" as "ν =64" on p. 441.
- The M-step equation uses "−1" correctly in the image (the text layer shows "→1").
- The prior in 17.5 is printed as $p(\mu,\log\sigma\mid\nu)\propto1$ although the regression parameter is $\beta$ (probably a misprint for $\beta$); I report it as printed.
- Exercise 8 asserts that inferences are sensitive to $\nu$ when $y_8=100$; this is the book's claim for the reader to verify, not a result shown here.
- Running header at the top of each page: "This electronic edition is for non-commercial purposes only."
