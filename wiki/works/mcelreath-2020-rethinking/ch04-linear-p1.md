---
id: mcelreath-2020-rethinking/ch04-linear-p1
work: mcelreath-2020-rethinking
unit: "Chapter 4. Linear Models (part 1/2): intro, 4.1 Why normal distributions are normal, 4.2 A language for describing models, 4.3 A Gaussian model of height"
pages: 71-91
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Linear Models (part 1/2): Gaussian skeletons, model notation, and a Gaussian model of height

## L0 — One line
Normal distributions tend to arise when many fluctuations are added together, so a Gaussian likelihood with unknown mean and spread, written in a standard model notation and updated by Bayes, is a sensible first "golem" (the book's word for a statistical model that does what it is told) for measurements.

## L1 — The gist (≤ 120 words)
How can we model a measurement by its mean and spread, and get a Bayesian posterior for both? McElreath shows that Gaussian shapes arise from adding fluctuations, from multiplying small ones, and from multiplying large ones on the log scale. He also presents the Gaussian as the least-committal choice when only mean and variance are assumed. He then introduces a notation for models (likelihood plus priors) and fits a Gaussian model to adult !Kung heights. He uses grid approximation, then quadratic approximation with `map`, and samples from the posterior. This matters because later regressions reuse this scaffold, and because a model's assumptions belong to the golem (the model), not necessarily to the world.

**Prerequisites:** Bayes' theorem and grid approximation from the globe-tossing chapters; sampling from a posterior; mean, variance, standard deviation; basic R syntax; logarithms and exp.

## L2 — Key ideas (5–10 bullets)
- Sums of many fluctuations from the same distribution tend to a Gaussian. Small multiplicative effects behave like sums, and large ones become Gaussian on the log scale (pp. 73–75).
- Two justifications for the Gaussian: it is a widespread natural pattern (ontological, about the world), and it is the least-committal shape given only mean and variance (epistemological, about our knowledge). Using a model is not the same as swearing an oath to believe it; the golem serves us (pp. 75–76).
- A model is described in five steps: outcome, likelihood, predictors, link of predictors to the likelihood's shape, and priors for all parameters. The notation exposes assumptions such as independence (pp. 77–78).
- The height model is $h_i \sim \text{Normal}(\mu,\sigma)$ with priors on $\mu$ and $\sigma$. The i.i.d. (independent and identically distributed) assumption is about the golem's uncertainty, not about physical independence (pp. 81–82).
- Priors imply a distribution of individual heights. Simulating from the priors shows what they assume (pp. 82–83).
- With two parameters the posterior is a distribution over $(\mu,\sigma)$ pairs. Grid approximation computes it by brute force on a grid of values, and samples summarize it (pp. 83–85).
- Quadratic approximation (a Gaussian fit at the posterior peak, done with `map`) gives a multivariate Gaussian described by a mean vector and a variance-covariance matrix (a table of variances and covariances). Sampling from it is sampling from a multivariate Gaussian (pp. 86–91).
- The posterior of $\sigma$ has a longer right tail, which is clearer with little data. Estimating $\log\sigma$ often helps (pp. 85–86, 91).

## L3 — Walkthrough

### Chapter opening (pp. 71–72)
- Ptolemy's geocentric model used epicycles (circles on circles). It was used for over a thousand years and was very accurate in its domain, although its structure is wrong (p. 71). The author says that with enough epicycles it is the same as a Fourier series, a general approximation device (p. 71).
- **Analogy:** linear regression is "the geocentric model of applied statistics". It is a family of simple models for the mean and variance of a measurement using an additive combination of other measurements. It is descriptive and corresponds to many different process models, so reading its structure too literally risks mistakes (p. 71).
- Under a probability interpretation, linear regression uses a Gaussian distribution to describe the golem's uncertainty about a measurement. Once you can build and interpret it, you can quickly move on to other regressions that are "less normal" (pp. 71–72).

### 4.1 Why normal distributions are normal (pp. 72–76)
**Soccer-field thought experiment (p. 72).** 1000 people flip a coin 16 times each. Heads is one step left, tails one step right. Final distances from the halfway line are approximately Gaussian even though the underlying distribution is binomial. The reason: there are many more step sequences that sum to zero than to a far-off position, and the number of sequences declines in the bell-curve pattern (p. 72).

**4.1.1 Normal by addition (pp. 72–74).**
- Simulation with steps that are random distances in $[-1,1]$ rather than coin steps. R code 4.1: `pos <- replicate(1000, sum(runif(16,-1,1)))` (p. 73).
- Figure 4.2 shows that the distribution of positions after 4, 8 and 16 steps looks increasingly like a Gaussian. Squaring or otherwise transforming step sizes does not change this (p. 73).
- Author's claim: any process that adds together random values from the same distribution converges to a normal (p. 73).
- Conceptual explanation: each draw is a fluctuation around the average. In a sum, large positive and negative fluctuations cancel. The most likely sum, the one realizable in the most ways, is the one where everything cancels, i.e. zero relative to the mean (pp. 73–74).
- The shape of the source distribution can be uniform or (nearly) anything else. Convergence may be slow, but it will be inevitable (p. 74).

*Intuition note.* Adding many random pushes lets them cancel each other. The cancelling outcome can happen in the most ways, so the sums pile up in a bell shape.

**4.1.2 Normal by multiplication (p. 74).**
- Example: growth rate affected by 12 interacting loci, each multiplying growth by a factor between 1.0 and 1.1. R code 4.2: `prod(1 + runif(12,0,0.1))`. R code 4.3 generates 10,000 such products, and the distribution is approximately normal (p. 74).
- Reason: multiplying small numbers is approximately addition. $1.1 \times 1.1 = 1.21$, while $(1+0.1)(1+0.1) = 1 + 0.2 + 0.01 \approx 1.2$, off by only 0.01 (p. 74). The smaller each effect, the better the additive approximation.
- R code 4.4 compares `big` (factors up to 1.5) with `small` (factors up to 1.01) (p. 74). Interacting deviations converge to a Gaussian as long as they are sufficiently small (p. 74).

**4.1.3 Normal by log-multiplication (p. 75).**
- Large multiplied deviates do not give Gaussians, but they tend to give Gaussians on the log scale. R code 4.5: `log(prod(1 + runif(12,0,0.5)))`. Adding logs is equivalent to multiplying the original numbers (p. 75).
- Measurement scales are arbitrary. Sound, earthquakes and information are naturally measured on log scales (p. 75).

**4.1.4 Using Gaussian distributions (pp. 75–76).** The author gives two kinds of justification.
- *Ontological* (about the world). Gaussian patterns appear approximately and widely: measurement errors, growth variation, molecular velocities. These processes add fluctuations. Repeatedly adding finite fluctuations yields sums that shed all information about the process except mean and spread (p. 75). Consequence: Gaussian-based models cannot reliably identify micro-process, but can still do useful work (p. 75). The Gaussian is not universal. It belongs to the exponential family, and later chapters introduce other patterns (p. 75).
- *Epistemological* (about our knowledge). When all we know or will say about a continuous measure is its mean and variance, the Gaussian is the most consistent with those assumptions. If all we assume is finite variance, it is the shape realizable in the most ways and adds no new assumptions (p. 75). The author says this rests on information theory and maximum entropy, treated later (Chapters 6 and 9 as printed) (p. 76). If you think the distribution should not be Gaussian, you know something you should tell the golem (p. 76).
- "The golem is your servant, not the other way around." We need not believe our models' assumptions; they need only be useful (p. 76).

*Intuition note.* The Gaussian is not only common; it is also the default choice when you commit only to a centre and a spread. Choosing it does not mean claiming the world is exactly Gaussian.

**Overthinking: Gaussian distribution (p. 76).**
$$p(y\mid\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(y-\mu)^2}{2\sigma^2}\right)$$
- The $(y-\mu)^2$ term gives the quadratic shape. The rest scales the density so it sums to one (p. 76).
- Continuous distributions have probability *density* functions, which can exceed 1. Example: `dnorm(0,0,0.1)` is about 4. The area under a density never exceeds 1 (p. 76). Discrete ones have probability *mass* functions, written $\Pr$ (p. 76).
- Precision form, with $\tau = 1/\sigma^2$ (substitute $\sigma = 1/\sqrt{\tau}$):
$$p(y\mid\mu,\tau) = \sqrt{\frac{\tau}{2\pi}}\exp\!\left(-\tfrac12 \tau (y-\mu)^2\right)$$
This form is common in Bayesian data analysis. Software such as BUGS or JAGS sometimes requires it (p. 76).

### 4.2 A language for describing models (p. 77)
The author says this language is standard in many statistical texts and nearly all journals, and is general to Bayesian and non-Bayesian modeling (p. 77). Five choices go into a model description (p. 77):
1. Name the *outcome* variable(s).
2. Define a likelihood distribution for each outcome. In linear regression it is always Gaussian.
3. Name the *predictor* variables.
4. Relate the likelihood's location, variance and other shape aspects to the predictors. This forces us to name all parameters.
5. Choose priors for all parameters, the model's information state before the data.

Abstract summary example (p. 77):
$$\begin{aligned}
\text{outcome}_i &\sim \text{Normal}(\mu_i,\sigma)\\
\mu_i &= \beta \times \text{predictor}_i\\
\beta &\sim \text{Normal}(0,10)\\
\sigma &\sim \text{HalfCauchy}(0,1)
\end{aligned}$$
- The notation is used for communication, not for algebraic manipulation (p. 77).
- Benefit: conditions such as homoscedasticity (constant variance) can be read off the definition. Regression, ANOVA and ANCOVA are the same kind of model, mappings of some variables through a probability distribution onto others (p. 77).

**4.2.1 Re-describing the globe-tossing model (p. 78).**
$$w \sim \text{Binomial}(n,p), \qquad p \sim \text{Uniform}(0,1)$$
- Reading: the count $w$ is binomial with sample size $n$ and probability $p$, and the prior for $p$ is uniform on $[0,1]$. The binomial assumes independent tosses (p. 78).
- First line = likelihood used in Bayes' theorem. Other lines = priors. Both are *stochastic* ($\sim$): a mapping of a variable onto a distribution, with no single value known for certain. Later models will include deterministic lines (p. 78).
- Overthinking: the posterior is
$$\Pr(p\mid w,n) = \frac{\text{Binomial}(w\mid n,p)\,\text{Uniform}(p\mid 0,1)}{\int \text{Binomial}(w\mid n,p)\,\text{Uniform}(p\mid 0,1)\,dp}$$
The denominator is the average likelihood. The numerator, likelihood times prior, is where the action is (p. 78). R code 4.6: `w <- 6; n <- 9`, a 100-point `p_grid`, `posterior <- dbinom(w,n,p_grid)*dunif(p_grid,0,1)`, then divide by the sum (p. 78).

### 4.3 A Gaussian model of height (pp. 78–91)
**Setup (pp. 78–79).** Two parameters, $\mu$ and $\sigma$. Bayesian updating scores every combination of $(\mu,\sigma)$ by its relative plausibility, its posterior probability. The "estimate" is the whole posterior, so the posterior is a "distribution of Gaussian distributions". In practice approximations are used (p. 79).

**4.3.1 The data (pp. 79–80).**
- `data(Howell1)`: partial census data of Dobe area !Kung San, from interviews by Nancy Howell in the late 1960s (p. 79). R code 4.7–4.8: data frame `d` with 544 rows and columns height (cm), weight (kg), age (years), male (0/1) (p. 79).
- `d$height` extracts the height column (p. 80). Only adults are kept, because height is strongly correlated with age before adulthood. R code 4.10: `d2 <- d[ d$age >= 18 , ]` gives 352 rows (p. 80).
- Overthinking boxes explain data frames (all columns same length) and index notation `d[row, col]` (p. 80).

**4.3.2 The model (pp. 80–83).**
- Adult heights look Gaussian. The author suggests this may be because height is a sum of many small growth factors (pp. 80–81). Caution: do not choose a Gaussian likelihood just because the raw outcome looks Gaussian. The data could be a mixture of Gaussians, and the empirical distribution need not be Gaussian to justify a Gaussian likelihood (p. 81).
- Likelihood: $h_i \sim \text{Normal}(\mu,\sigma)$. The index $i$ runs over rows, 1 to 352. All the golem knows about each height is the same normal distribution. The $i$ will matter once predictors appear on the right-hand side (p. 81).
- **Rethinking, i.i.d. (pp. 81–82).** The model is sometimes described as assuming the $h_i$ are independent and identically distributed. Physically this is hardly ever true (e.g., heights within families are correlated). But the assumption is about how the golem represents its uncertainty (epistemological). It is not a physical (ontological) assumption about the world, unless you insist that it is. Confusing the two is the mind projection fallacy (Jaynes). In ignorance of correlations, i.i.d. is the most conservative choice (p. 81). De Finetti's theorem says exchangeable values (values that can be reordered) can be approximated by mixtures of i.i.d. distributions, so i.i.d. should not be read too literally (p. 81). Many types of correlation do little or nothing to the overall shape of a distribution and only affect the sequence in which values appear, e.g. sisters' heights. In such cases i.i.d. remains useful. MCMC can use correlated sequential samples to estimate most any iid distribution (p. 82).
- Priors, assuming independent priors so that $\Pr(\mu,\sigma) = \Pr(\mu)\Pr(\sigma)$ (p. 82):
$$\begin{aligned}
h_i &\sim \text{Normal}(\mu,\sigma) &&\text{[likelihood]}\\
\mu &\sim \text{Normal}(178,20) &&[\mu\text{ prior}]\\
\sigma &\sim \text{Uniform}(0,50) &&[\sigma\text{ prior}]
\end{aligned}$$
- The $\mu$ prior is broad, centred on 178 cm (the author's height), with 95% of probability within $178 \pm 40$, i.e. 138 to 218 cm. Domain knowledge went into it (p. 82). R code 4.11 plots it: the average height is almost certainly between 140 and 220 cm, so the prior carries a little information (p. 82).
- The $\sigma$ prior is flat on 0 to 50 cm. A standard deviation of 50 cm would put 95% of individual heights within 100 cm of the average, a very large range (p. 82).
- **Prior predictive simulation** (the author does not give it this name). R code 4.13: sample `mu` from Normal(178,20), `sigma` from Uniform(0,50), then `rnorm(1e4, sample_mu, sample_sigma)`. The result is vaguely bell-shaped with thick tails, so the prior distribution of height is not itself Gaussian. It shows relative plausibilities of heights before seeing data (p. 83).
- **Rethinking, "farewell to epsilon":** the form $h_i = \mu + \epsilon_i$, $\epsilon_i\sim\text{Normal}(0,\sigma)$ is equivalent, but poor form because it does not usually generalize to non-Gaussian models (p. 83).
- **Overthinking: posterior in full** (p. 83):
$$\Pr(\mu,\sigma\mid h) = \frac{\prod_i \text{Normal}(h_i\mid\mu,\sigma)\,\text{Normal}(\mu\mid 178,20)\,\text{Uniform}(\sigma\mid 0,50)}{\int\!\!\int \prod_i \text{Normal}(h_i\mid\mu,\sigma)\,\text{Normal}(\mu\mid 178,20)\,\text{Uniform}(\sigma\mid 0,50)\,d\mu\,d\sigma}$$
The product over $i$ gives the joint likelihood across observations. The two priors just stack up. The code works on the log scale, so multiplication becomes addition (p. 83).

**4.3.3 Grid approximation (pp. 83–84).**
- Brute force is laborious and usually impractical, but worth doing once to see the target before using approximations (p. 83). R code 4.14 (explained only in an endnote) does the following (p. 84):
  - `mu.list`: 200 values from 140 to 160. `sigma.list`: 200 values from 4 to 9. `expand.grid` makes all pairs (added step: $200\times200=40{,}000$ rows).
  - `post$LL`: for each pair, the sum over the data of `dnorm(height, mu, sigma, log=TRUE)`, i.e. the log-likelihood.
  - `post$prod`: `LL` plus the log prior of $\mu$ (`dnorm(mu,178,20,TRUE)`) plus the log prior of $\sigma$ (`dunif(sigma,0,50,TRUE)`).
  - `post$prob <- exp(post$prod - max(post$prod))`, the relative posterior (added step: the largest value becomes 1).
- R code 4.15–4.16: `contour_xyz` and `image_xyz` plot the result (p. 84).

**4.3.4 Sampling from the posterior (pp. 84–85).**
- Sample row numbers of `post` with probability proportional to `post$prob`, then pull out `mu` and `sigma` for those rows (R code 4.17, 10,000 samples with replacement) (p. 84). Figure 4.3 shows the cloud of samples; its axes run roughly 153–156 for $\mu$ and 7.0–9.0 for $\sigma$, and the points are densest in the centre (axis ranges read from the image) (p. 85).
- Marginal posterior means averaging over the other parameters. `dens(sample.mu)` and `dens(sample.sigma)` are very close to normal. As sample size increases, posterior densities approach the normal distribution. The $\sigma$ density has a longer right tail (p. 85). `HPDI()` summarizes widths (p. 85).
- **Overthinking: sample size and normality of $\sigma$'s posterior (pp. 85–86).**
  - For a Gaussian likelihood with a Gaussian prior on $\mu$, the posterior of $\mu$ is always Gaussian, regardless of sample size (author's statement). $\sigma$ is the problem (p. 86).
  - The author says the deep reasons are complex, but a useful way to think about it is that variances must be positive, so there must be more uncertainty about how big $\sigma$ is than how small. If it is near zero, it cannot be much smaller but could be a lot bigger (p. 86).
  - Demonstration: 20 random heights `d3`, with grids $\mu\in[150,170]$, $\sigma\in[4,20]$ (R code 4.21–4.23). The scatter shows a distinctly longer upper tail, and the marginal density of $\sigma$ is visibly not Gaussian (p. 86).

*Intuition note.* The cloud of $(\mu,\sigma)$ samples is the answer: each point is one plausible Gaussian curve. In the 20-height demonstration the cloud stretches toward big $\sigma$, which fits the author's picture that a spread near zero cannot shrink much but could be much larger.

**4.3.5 Fitting the model with `map` (pp. 86–89).**
- The quadratic approximation is a quick way to see the posterior's shape. The posterior peak is the maximum a posteriori estimate (MAP), and the approximation is taken at that peak (p. 86). `map` converts each line of the model definition into R code, defines the posterior, and climbs it to find the peak (p. 87).
- The author's margin shows the prior as `mu ~ dnorm(156,10)`, which does not match the model line Normal(178,20) (see Reading notes). The `alist` actually used (R code 4.25) is `height ~ dnorm(mu,sigma)`, `mu ~ dnorm(178,20)`, `sigma ~ dunif(0,50)`. The fit is `m4.1 <- map(flist, data=d2)` (p. 87).
- `precis(m4.1)` output (p. 87):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| mu | 154.61 | 0.41 | 153.95 | 155.27 |
| sigma | 7.73 | 0.29 | 7.27 | 8.20 |

- These are Gaussian approximations of each marginal distribution. The 5.5% and 94.5% quantiles bound an 89% interval. The author says 89% is just the default. He avoids 95% because readers will have a hard time not viewing such intervals as significance tests (pp. 87–88). They are almost identical to the grid HPDIs, as expected when the posterior is approximately Gaussian (p. 88).
- Overthinking, start values: `map` climbs the posterior, starting by default from random values sampled from the prior. One can supply `start <- list(mu=mean(d2$height), sigma=sd(d2$height))`. Use `list` (evaluates code) for starts and `alist` (does not evaluate) for formulas (p. 88).
- **Narrow prior (R code 4.29).** With `mu ~ dnorm(178, 0.1)` (p. 88):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| mu | 177.86 | 0.10 | 177.70 | 178.02 |
| sigma | 24.52 | 0.93 | 23.03 | 26.00 |

  $\mu$ hardly leaves the prior. $\sigma$ changes a lot though its prior was unchanged. Once the golem is sure $\mu$ is near 178, it must estimate $\sigma$ conditional on that fact (pp. 88–89). With this much data and so simple a model, only fairly extreme priors affect inference. The author notes that most non-Bayesian estimates implicitly use flat priors, and says perfectly flat priors are hardly ever the best choice (p. 89).
- **Overthinking: how strong is a prior?** A prior can usually be interpreted as a former posterior from earlier data. For a Gaussian posterior for $\mu$: $\sigma_{\text{post}} = 1/\sqrt{n}$, so the implied amount of data is $n = 1/\sigma_{\text{post}}^2$. Normal(178, 0.1) gives $n = 1/0.01 = 100$ heights with mean 178. Normal(178, 20) gives $n = 1/20^2 = 0.0025$ of an observation. How strong or weak either prior is depends on how much data is used to update it (p. 89).

*Intuition note.* A prior's width can be translated into an equivalent amount of earlier data. Normal(178, 0.1) is like 100 earlier heights, a pretty strong prior. Normal(178, 20) is like 0.0025 of an observation, extremely weak. How much either matters still depends on how much new data updates it.

**4.3.6 Sampling from a `map` fit (pp. 89–91).**
- A quadratic approximation with several parameters is a multivariate Gaussian. It is described by a vector of means and a matrix of variances and covariances (p. 89). R code 4.30, `vcov(m4.1)`:

| | mu | sigma |
|---|---|---|
| mu | 0.1697395865 | 0.0002180593 |
| sigma | 0.0002180593 | 0.0849057933 |

- The matrix factors into a vector of variances and a correlation matrix (pp. 89–90). R code 4.31: `diag(vcov(m4.1))` gives 0.16973959 ($\mu$) and 0.08490579 ($\sigma$). Square roots give the `precis` standard deviations. `cov2cor(vcov(m4.1))` has off-diagonal 0.001816412 (p. 90).
- Correlation near zero means that learning $\mu$ tells us nothing about $\sigma$, and vice versa. The author says this is typical of simple Gaussian models of this kind but quite rare more generally (p. 90).
- Sampling: `post <- extract.samples(m4.1, n=1e4)` returns 10,000 rows with columns `mu` and `sigma` (R code 4.32) (p. 90). `precis(post)`: $\mu$ mean 154.61, sd 0.42, 89% HPDI 153.95–155.27; $\sigma$ mean 7.73, sd 0.29, HPDI 7.26–8.19 (R code 4.33) (p. 90). The samples preserve covariance between $\mu$ and $\sigma$. This hardly matters now, but the author says it will matter a lot once a predictor is added (p. 91).
- Overthinking: `extract.samples` runs `mvrnorm`, a multivariate `rnorm`: `post <- mvrnorm(n=1e4, mu=coef(m4.1), Sigma=vcov(m4.1))` (R code 4.34) (p. 91).
- **Overthinking: getting $\sigma$ right (p. 91).** The quadratic assumption for $\sigma$ can be problematic. A conventional fix is to estimate $\log\sigma$, whose posterior can be much closer to Gaussian. R code 4.35:
  `height ~ dnorm(mu, exp(log_sigma))`, `mu ~ dnorm(178,20)`, `log_sigma ~ dnorm(2,10)`.
  `exp(x) > 0` for any real $x$, so $\sigma = \exp(\texttt{log\_sigma})$ is strictly positive and `log_sigma` can have a Gaussian prior. After extracting samples, `sigma <- exp(post$log_sigma)` (R code 4.36). With a lot of data it makes no noticeable difference. The author says this relates to link functions in generalized linear models (Chapter 9 as printed) (p. 91).

## Toy example (ours, not from the text)
Tiny grid posterior for a Gaussian model. Data: $y=\{4,6\}$. Grid: $\mu\in\{4,5,6\}$, $\sigma\in\{1,2\}$. Flat prior on all six pairs, so only the likelihood matters.

Joint likelihood of both observations: $\frac{1}{2\pi\sigma^2}\exp\!\big(-S/(2\sigma^2)\big)$, with $S=\sum (y-\mu)^2$. Drop the common $1/2\pi$.
- $S$: $\mu=4$: $0+4=4$. $\mu=5$: $1+1=2$. $\mu=6$: $4+0=4$.
- $\sigma=1$ (weight $1/\sigma^2=1$): $e^{-2}=0.1353$, $e^{-1}=0.3679$, $e^{-2}=0.1353$ for $\mu=4,5,6$.
- $\sigma=2$ (weight $1/4$): $0.25e^{-0.5}=0.1516$, $0.25e^{-0.25}=0.1947$, $0.1516$.
- Total $=0.6386+0.4980=1.1365$. Dividing each by the total gives the posterior:

| | μ=4 | μ=5 | μ=6 | row sum |
|---|---|---|---|---|
| σ=1 | 0.119 | 0.324 | 0.119 | 0.562 |
| σ=2 | 0.133 | 0.171 | 0.133 | 0.438 |

- Marginal for $\mu$ (sum over $\sigma$): $0.252, 0.495, 0.252$. Marginal for $\sigma$: $0.562, 0.438$.
- Sampling rows with these probabilities and reading off the pair is exactly the book's `sample(..., prob=post$prob)` step. Each sampled row is one plausible Gaussian.

## Concepts
- [[gaussian-by-addition]] (new) — sums of many fluctuations from one distribution tend toward a normal; (nearly) any source shape works (pp. 73–74)
- [[gaussian-by-multiplication]] (new) — small multiplicative effects are approximately additive, so products also tend toward normal; large ones do so on the log scale (pp. 74–75)
- [[principle-of-indifference-maximum-entropy]] — Gaussian as the least-committal choice given only mean and variance; the author postpones the formal argument (pp. 75–76)
- [[likelihood]] — the first line of a model definition; here $h_i\sim\text{Normal}(\mu,\sigma)$ (pp. 77–78, 81)
- [[prior-distribution]] — the initial information state of the model; here $\mu\sim\text{Normal}(178,20)$, $\sigma\sim\text{Uniform}(0,50)$ (pp. 77, 82)
- [[posterior-distribution]] — over $(\mu,\sigma)$ pairs; the "estimate" is the whole distribution, "a distribution of Gaussian distributions" (p. 79)
- [[model-definition-notation]] (new) — the standard stochastic-line notation for outcomes, likelihood, predictors and priors (p. 77)
- [[iid-assumption]] (new) — independent, identically distributed values; here an epistemological assumption about the golem's uncertainty, not a physical claim unless one insists (p. 81)
- [[exchangeability]] — values that can be reordered; de Finetti's theorem links them to mixtures of i.i.d. distributions (p. 81)
- [[prior-predictive-check]] — simulating individual heights from the priors to see what they imply (author gives no name) (p. 83)
- [[grid-approximation]] (new) — compute the posterior on a grid of parameter pairs; brute force, rarely practical (p. 83)
- [[quadratic-approximation]] (new) — Gaussian approximation to the posterior at its MAP peak, fit with `map` (p. 86)
- [[variance-covariance-matrix]] (new) — variances and covariances of the parameters; with the means it is sufficient to describe a multivariate Gaussian (pp. 89–90)
- [[credible-interval]] — HPDI and percentile intervals computed from samples (here 89%) (pp. 85, 87)
- [[prior-strength-as-implied-data]] (new) — a prior's width read as the amount of data that would give the same posterior from a flat start, $n=1/\sigma_{\text{post}}^2$ (p. 89)

## Canonical instances
- [[ptolemy-epicycles]] — a wrong but predictive descriptive model, analogy for linear regression (pp. 71–72)
- [[soccer-field-random-walk]] — summing random steps gives a Gaussian (pp. 72–73)
- [[growth-loci-multiplication]] — products of small growth factors are approximately normal (p. 74)
- [[globe-tossing-model-notation]] — the water-proportion model rewritten as $w\sim\text{Binomial}(n,p)$, $p\sim\text{Uniform}(0,1)$ (p. 78)
- [[howell-kung-heights]] — 352 adult heights, the running example, giving $\mu\approx154.6$, $\sigma\approx7.7$ (pp. 79–87)
- [[narrow-prior-m4-2]] — $\text{Normal}(178,0.1)$ prior drags $\mu$ to 177.86 and changes $\sigma$ to 24.52 (p. 88)
- [[sigma-posterior-skew-20-heights]] — with 20 heights the posterior of $\sigma$ has a long right tail (p. 86)

## Bridges (candidates)
- [structural-analogy] Gaussian by addition ↔ probability theory: the central limit theorem (not named in this unit); same qualitative statement, but the unit gives only simulations and a cancellation argument, not a theorem.
- [structural-analogy] Prior strength as $n=1/\sigma^2_{\text{post}}$ ↔ Bayesian inference: conjugate priors act like pseudo-observations (Beta–Binomial).
- [structural-analogy] Gaussian as the least-committal shape given mean and variance ↔ Bayesian inference: maximum entropy (developed later in the book).
- [metaphor] Linear regression as geocentric model ↔ philosophy of modelling: a descriptive model can predict well while its structure is not the true process.

## Questions this raises
- Why can an approximation to the posterior at its peak describe the whole posterior well, and when does it fail (the $\sigma$ tail suggests one case)?
- If $\mu$ and $\sigma$ are uncorrelated here, what changes in the posterior once a predictor variable is added (the author says covariance will matter a lot then)?
- What exactly does the prior imply about data in more complex models, where parameters lack clear physical meaning (p. 82)?
- How does the maximum-entropy argument pick other distributions (exponential, Poisson, gamma) as most consistent under other constraints?

## Reading notes
- This is part 1 of Chapter 4. It starts at the chapter opening (printed p. 71) and ends at the end of printed p. 91, within section 4.3.6 (the Overthinking boxes). Sections after 4.3 (e.g., predictors) are not in this part.
- Printed = pdf − 14 (pdf 85 = printed 71). The page labels give printed numbers directly.
- Apparent misprint in the source (p. 87): the margin code next to the model definition reads `mu ~ dnorm(156,10)`, while the model line and the actual code (R code 4.25) use Normal(178, 20) / `dnorm(178,20)`.
- Typos in the source: "You're computer already knows it" (p. 76), "a peak at the motor" (p. 91). Both are harmless.
- The code uses `map` and `precis` as printed. Output tables are copied from the page images. Chapter cross-references (Chapters 6, 8, 9) are as printed. Footnote numbers (e.g., 61–67) point to endnotes not included here.
- Figure 4.3's axis ranges in the walkthrough were read from the image.
