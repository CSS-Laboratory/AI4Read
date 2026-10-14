---
id: mackay-2003-information/ch24-exact
work: mackay-2003-information
unit: 24 Exact Marginalization
pages: 319-323
fields: [information-theory, bayesian]
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
# Exact Marginalization

## L0 — One line
Integrating out a nuisance parameter (here the Gaussian mean μ) exactly gives the Bayesian answer for σ, and it explains why the divisor is N−1 rather than N.

## L1 — The gist (≤ 120 words)
How can we avoid enumerating all hypotheses? This chapter treats exact marginalization (integrating out unwanted parameters) for continuous variables. The worked case is inferring a Gaussian's mean μ and standard deviation σ from N samples, with conjugate or noninformative priors. Fixing μ at x̄ gives a most probable σ of σ_N. Marginalizing over μ gives an evidence for σ containing an Occam factor, and its peak moves to σ_{N−1}. The marginal posterior of μ is a Student-t distribution (Exercise 24.2). This shows that sampling-theory estimators can emerge as modes of Bayesian posteriors, and why marginalizing differs from plugging in a best-fit value.

**Prerequisites:** Gaussian density; Bayes' theorem (posterior ∝ likelihood × prior); Gaussian integrals; change of variables for densities (Jacobian); logarithms and derivatives.

## L2 — Key ideas
- Exact marginalization has two routes: integrals over continuous variables and message-passing over discrete ones. This unit covers only the integral route. (p. 319)
- Conjugate priors (priors whose form combines naturally with the likelihood) give inferences a convenient form. The mean gets a Gaussian prior and the precision β = 1/σ² gets a gamma prior. (pp. 319–320)
- The noninformative priors are flat in μ and flat in ln σ (the 1/σ prior). Both are improper (not normalizable), and the author uses them for readability. (pp. 319–320)
- Bayesian inference is mechanical once the hypothesis space is fixed. Sampling-theory estimators often appear as modes or means of posteriors. (p. 320)
- With σ fixed, $P(\mu\mid D,\sigma)=\mathrm{Normal}(\mu;\bar x,\sigma^2/N)$, which gives the familiar $\sigma/\sqrt N$ error bars. (p. 322)
- Marginalizing μ gives the evidence for σ, with an Occam factor. This shifts the most probable σ from $\sigma_N$ to $\sigma_{N-1}$. (p. 322)
- N−1 counts the effective noise measurements, because estimating μ uses up one dimension of noise. (p. 322)
- Exercises ask for the Student-t marginal of μ and a Bayesian treatment of scientists with unequal noise levels. (p. 323)

## L3 — Walkthrough

**Chapter opening (p. 319).** Question: how to avoid the exponential cost of complete enumeration of hypotheses? Two exact approaches: (1) integrals over continuous nuisance parameters (parameters we must include but do not care about); (2) summation over discrete variables by message-passing. The chapter treats (1). It uses gamma distributions, which are like Gaussians but live on $0$ to $\infty$.

### 24.1 Inferring the mean and variance of a Gaussian (pp. 319–323)

$$P(x\mid\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)\equiv \mathrm{Normal}(x;\mu,\sigma^2)\tag{24.1}$$

**Conjugate priors (pp. 319–320).** A conjugate prior is one whose functional form combines naturally with the likelihood, so inferences have a convenient form (p. 319).
- For μ: a Gaussian with hyperparameters (parameters of the prior) $\mu_0,\sigma_\mu$: $P(\mu\mid\mu_0,\sigma_\mu)=\mathrm{Normal}(\mu;\mu_0,\sigma_\mu^2)$. In the limit $\mu_0=0$, $\sigma_\mu\to\infty$ we get the flat prior, noninformative for a location parameter because it is invariant under $\mu'=\mu+c$. It is improper (p. 319).
- For σ: a gamma prior on the precision $\beta=1/\sigma^2$:
$$P(\beta)=\Gamma(\beta;b_\beta,c_\beta)=\frac{1}{\Gamma(c_\beta)}\frac{\beta^{c_\beta-1}}{b_\beta^{c_\beta}}\exp\!\Big(-\frac{\beta}{b_\beta}\Big),\quad 0\le\beta<\infty\tag{24.2}$$
Its mean is $b_\beta c_\beta$ and its variance is $b_\beta^2 c_\beta$. In the limit $b_\beta c_\beta=1$, $c_\beta\to0$ we get the $1/\sigma$ prior, noninformative for a scale parameter because it is invariant under $\sigma'=c\sigma$. It is flat in $\ln\sigma$ and $\ln\beta$, and also improper (p. 320).
- Density change of variables: $P_l(l)=P_\sigma(\sigma)\,|\partial\sigma/\partial l|$, and $|\partial\sigma/\partial\ln\sigma|=\sigma$ (margin note, p. 320).
- The examples use these improper priors for readability. With proper priors the calculation is still possible but extra parameters would obscure the key points (p. 320).

*Intuition note:* A flat prior on $\ln\sigma$ says "σ could be 10, or 1, or 0.1" with equal weight per factor of 10. The author adds that scale variables such as σ are usually best represented in terms of their logarithm (p. 320).

**σ_N and σ_{N−1} (p. 320).** Given $D=\{x_n\}_{n=1}^N$:
$$\bar x\equiv\sum_n x_n/N\tag{24.3}$$
$$\sigma_N\equiv\sqrt{\tfrac{\sum_n(x_n-\bar x)^2}{N}},\qquad \sigma_{N-1}\equiv\sqrt{\tfrac{\sum_n(x_n-\bar x)^2}{N-1}}\tag{24.4}$$

*Two paradigms (p. 320).*
- In sampling theory, one invents estimators and chooses among them by a sampling-properties criterion. There is no clear principle for choosing the criterion, and for most criteria no systematic way to build optimal estimators.
- In Bayesian inference, once the model and data assumptions are explicit, the rules of probability give a unique answer. Human input enters only in designing the hypothesis space and in doing the computations. The answers are probability distributions.
- The author says we often find sampling-theory estimators emerge as modes or means of posteriors when we choose a simple hypothesis space.

*Sampling-theory view (p. 321).*
- $\bar x$ is an unbiased estimator of μ with the smallest variance among unbiased estimators. The variance is computed over imaginary experiments with data from an unknown Gaussian.
- $(\bar x,\sigma_N)$ is the maximum likelihood estimator of $(\mu,\sigma)$, but $\sigma_N$ is biased: its expectation given σ is not σ.
- This bias motivated $\sigma_{N-1}$. To be precise, $\sigma_{N-1}^2$ is an unbiased estimator of $\sigma^2$.
- Solution to Ex. 24.1 (p. 323), conclusion only: the expected mean squared deviation from the sample mean is necessarily smaller than $\sigma^2$.

**Bayesian inference with noninformative priors (pp. 321–322).** Log likelihood, with $S\equiv\sum_n(x_n-\bar x)^2$:
$$\ln P(\{x_n\}\mid\mu,\sigma)=-N\ln(\sqrt{2\pi}\sigma)-\sum_n(x_n-\mu)^2/(2\sigma^2)\tag{24.5}$$
$$=-N\ln(\sqrt{2\pi}\sigma)-[N(\mu-\bar x)^2+S]/(2\sigma^2)\tag{24.6}$$
$\bar x$ and $S$ are the "sufficient statistics": given the Gaussian model, the likelihood can be expressed in terms of these two functions of the data (p. 321). The joint posterior is
$$P(\mu,\sigma\mid\{x_n\})=\frac{P(\{x_n\}\mid\mu,\sigma)P(\mu,\sigma)}{P(\{x_n\})}\tag{24.7}$$
$$=\frac{\frac{1}{(2\pi\sigma^2)^{N/2}}\exp\!\big(-\frac{N(\mu-\bar x)^2+S}{2\sigma^2}\big)\frac{1}{\sigma_\mu}\frac{1}{\sigma}}{P(\{x_n\})}\tag{24.8}$$

*Mode.* Posterior maxima have no fundamental status, because their location depends on the choice of basis. In the basis $(\mu,\ln\sigma)$ the prior is flat, so the posterior maximum equals the likelihood maximum: $\{\mu,\sigma\}_{ML}=\{\bar x,\sigma_N=\sqrt{S/N}\}$ (p. 322, citing exercise 22.4).

*Shape (p. 322).* The likelihood peak is skew (Fig. 24.1a). The width of the conditional distribution of μ grows with σ. If μ is fixed at values moving away from $\bar x$, the maxima of the conditional distributions over σ move to larger σ (Fig. 24.1c). Figure data: $N=5$, $\bar x=1.0$, $S=1.0$, $\sigma_N=0.45$, $\sigma_{N-1}=0.50$ (p. 321).

**Posterior of μ given σ (p. 322).**
$$P(\mu\mid\{x_n\},\sigma)=\frac{P(\{x_n\}\mid\mu,\sigma)P(\mu)}{P(\{x_n\}\mid\sigma)}\tag{24.9}$$
$$\propto\exp(-N(\mu-\bar x)^2/(2\sigma^2))\tag{24.10}$$
$$=\mathrm{Normal}(\mu;\bar x,\sigma^2/N)\tag{24.11}$$
This is the familiar $\sigma/\sqrt N$ scaling of the error bars.

**Posterior of σ, marginalizing μ (p. 322).**
$$P(\sigma\mid\{x_n\})=\frac{P(\{x_n\}\mid\sigma)P(\sigma)}{P(\{x_n\})}\tag{24.12}$$
$P(\{x_n\}\mid\sigma)$ is the evidence (marginal likelihood) for σ. It is obtained by integrating out μ, with $P(\mu)=1/\sigma_\mu$ viewed as a top-hat prior of width $\sigma_\mu$. The Gaussian integral $\int P(\{x_n\}\mid\mu,\sigma)P(\mu)\,d\mu$ gives
$$\ln P(\{x_n\}\mid\sigma)=-N\ln(\sqrt{2\pi}\sigma)-\frac{S}{2\sigma^2}+\ln\frac{\sqrt{2\pi}\sigma/\sqrt N}{\sigma_\mu}\tag{24.13}$$
- The first two terms are the best-fit log likelihood (μ = x̄).
- The last term is the log of the Occam factor, which penalizes smaller values of σ (Occam factors are discussed in Chapter 28).
- Differentiating with respect to $\ln\sigma$, the extra volume factor $\sigma/\sqrt N$ shifts the maximum from $\sigma_N$ to
$$\sigma_{N-1}=\sqrt{S/(N-1)}\tag{24.14}$$

*Intuition note:* Plugging in the best-fit μ ignores that μ itself was fitted to the same data. Integrating over μ adds a volume factor (the Occam factor), which moves the most probable σ from $\sigma_N$ to $\sigma_{N-1}$.

*Why N−1 (pp. 322–323).* The sum S has N squared residuals, but only N−1 effective noise measurements. Determining μ from the data gobbles up one dimension of noise in unavoidable overfitting. In classical terms, the Bayesian's best guess for σ sets $\chi^2\equiv\sum_n(x_n-\hat\mu)^2/\hat\sigma^2$ equal to the degrees of freedom $N-1$ (p. 323).

*Figures (p. 323).* Fig. 24.1d shows $P(\sigma\mid D)$, proportional to the marginal likelihood. Its maximum is at $\sigma_{N-1}$. Compare $P(\sigma\mid D,\mu=\bar x)$, whose maximum is at $\sigma_N$ (captions, p. 321).

**Posterior of μ (p. 323).** Exercise 24.2 asks to marginalize σ to get a Student-t distribution:
$$P(\mu\mid D)\propto 1/\big(N(\mu-\bar x)^2+S\big)^{N/2}\tag{24.15}$$
Further reading: The author calls Bretthorst's (1988) book on Bayesian spectrum analysis and parameter estimation "a bible of exact marginalization".

### 24.2 Exercises (p. 323)
Exercise 24.3 asks for a Bayesian solution to the seven-scientists problem (exercise 22.15). Each scientist n has an unknown personal noise level $\sigma_n$ and measures μ. The prior on each $\sigma_n$ is broad, e.g. gamma with $(s,c)=(10,0.1)$. Hint: find $P(\sigma_n\mid x_n,\mu)$, whose normalizer is $P(x_n\mid\mu)$. Marginalize $\sigma_n$ to get that normalizer, then apply Bayes' theorem again to get $P(\mu\mid\{x_n\})$. The exercise also asks to plot the posterior and explore it for several data sets, including the one in the figure and $\{x_n\}=\{13.01, 7.39\}$.

### 24.3 Solutions (p. 323)
Only the solution to Ex. 24.1 is printed. Its argument: (1) the data points have mean squared deviation $\sigma^2$ about the true mean; (2) the sample mean is unlikely to equal the true mean exactly; (3) the sample mean is the μ that minimizes the sum of squared deviations, so any other μ (including the true one) gives a larger sum. Hence the expected mean squared deviation from the sample mean is necessarily smaller than $\sigma^2$.

## Toy example (ours)
Take $N=2$, data $\{0,2\}$. Then $\bar x=1$ and $S=(0-1)^2+(2-1)^2=2$.
- $\sigma_N=\sqrt{2/2}=1$; $\sigma_{N-1}=\sqrt{2/1}\approx1.414$.
- Fixed μ = x̄: up to a constant, $g(\sigma)=-2\ln\sigma-1/\sigma^2$ (from $-N\ln\sigma-S/(2\sigma^2)$). $g(1)=-1$; $g(1.414)=-0.693-0.5=-1.193$; $g(0.8)=0.446-1.5625=-1.116$. The maximum is near σ = 1.
- Marginalized μ (24.13, $\sigma$-dependent terms): $f(\sigma)=-2\ln\sigma+\ln\sigma-1/\sigma^2=-\ln\sigma-1/\sigma^2$. (added step) $f(1)=-1$; $f(1.2)=-0.182-0.694=-0.877$; $f(1.414)=-0.347-0.5=-0.847$; $f(1.6)=-0.470-0.391=-0.861$. The peak is near 1.414.
- (added step) Setting $df/d\ln\sigma=-(N-1)+S/\sigma^2=0$ gives $\sigma^2=S/(N-1)=2$.

The extra $+\ln\sigma$ from the Occam factor moves the peak from 1 to about 1.414.

## Concepts
- [[marginalization]] (new) — summing or integrating out unwanted variables to get the distribution of the rest (p. 319)
- [[nuisance-parameter]] (new) — a continuous parameter we must model but do not want to infer (p. 319)
- [[conjugate-prior]] — a prior whose form combines naturally with the likelihood, giving convenient inferences (p. 319)
- [[noninformative-prior]] (new) — a prior invariant under a natural reparameterization: flat for location, 1/σ for scale (pp. 319–320)
- [[improper-prior]] (new) — a prior that cannot be normalized, e.g. P(μ) = const. (p. 319)
- [[gamma-distribution]] (new) — a peaked density on $0\le\beta<\infty$, here the prior for precision (p. 320)
- [[sufficient-statistic]] (new) — functions of the data (here $\bar x$, S) through which the likelihood depends on the data (p. 321)
- [[marginal-likelihood]] — the evidence $P(D\mid\sigma)$ obtained by integrating out μ (p. 322)
- [[bayesian-occam-razor]] — the Occam factor in (24.13), a volume factor from integrating out μ (p. 322)
- [[frequentist-vs-bayesian]] — sampling theory chooses estimators by sampling criteria; Bayesian answers are posterior distributions (p. 320)
- [[estimator-bias]] (new) — an estimator is biased if its expectation over imagined experiments differs from the true value (p. 321)
- [[posterior-distribution]] — joint posterior (24.8) and its conditionals and marginals (p. 321)

## Canonical instances
- [[gaussian-mean-variance-inference]] (new) — joint, conditional and marginal posteriors of (μ, σ) with σ_N versus σ_{N−1} (pp. 320–323)
- [[seven-scientists]] (new) — varying noise levels σ_n; posed as a marginalization exercise (p. 323)

## Bridges (candidates)
- [structural-analogy] Occam factor in (24.13) ↔ bayesian: the volume factor from integrating out a fitted parameter, as in model comparison (Chapter 28, mentioned p. 322).
- [structural-analogy] σ_{N−1} (effective noise measurements) ↔ classical statistics: degrees of freedom, χ² set equal to N−1 (p. 323).
- [same-math] Flat prior on ln σ ↔ probability theory: change-of-variables rule for densities, with $|\partial\sigma/\partial\ln\sigma|=\sigma$ — a flat density in ln σ is a $1/\sigma$ density in σ (p. 320).

## Questions this raises
- Does the Occam-factor shift generalize when several parameters (not just μ) are integrated out?
- How do results change with proper priors instead of improper ones?
- When is a posterior mode a reasonable summary, given that its location depends on the basis?
- What happens when integrals are not available in closed form (the "approximate methods" the chapter defers)?

## Exercises worth doing
- Ex. 24.1 (p. 321) — intuition for why σ_N is biased — difficulty: easy
- Ex. 24.2 (p. 323) — marginalize σ to obtain the Student-t posterior of μ — difficulty: medium
- Ex. 24.3 (p. 323) — Bayesian version of the seven-scientists problem, with two Bayes steps — difficulty: hard

## Reading notes
- Printed page = pdf page − 12 (pdf 331 = p. 319).
- Pages given: pp. 319–323 only. Figures 24.1c–d are described from captions.
- The text layer is garbled in places (e.g. "exercisen 22.4"). I checked the equations against the page images.
- Caption of Fig. 24.1 has the typo "shows" for "shown". The Solution to 24.1 says "larger value of the sum-squared deviation that µ = x̄", where "than" is meant.
- Only the solution to Ex. 24.1 is printed. Exercises 24.2 and 24.3 have no solutions here.
- The note "$b_\beta c_\beta=1$" in the noninformative limit is copied as printed (p. 320).
