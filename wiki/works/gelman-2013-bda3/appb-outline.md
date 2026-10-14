---
id: gelman-2013-bda3/appb-outline
work: gelman-2013-bda3
unit: Appendix B — Outline of proofs of limit theorems
pages: 587–590
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Outline of proofs of limit theorems (BDA3, Appendix B)

## L0 — One line
With iid data (independent, identically distributed) and suitable regularity conditions, the posterior concentrates at the parameter value $\theta_0$ that minimizes Kullback–Leibler (KL) divergence (a measure of how far the model is from the truth), and it approaches a normal distribution with mean $\theta_0$ and variance $(nJ(\theta_0))^{-1}$.

## L1 — The gist (≤ 120 words)
Why does the posterior look normal for large samples, and where is it centered? The appendix outlines three steps. (1) For a finite parameter space, the posterior mass goes to the KL-minimizing point $\theta_0$ if the prior gives it positive mass. (2) For a compact continuous space, mass goes into any neighborhood of $\theta_0$ that has nonzero prior probability. (3) A Taylor expansion of the log posterior about the posterior mode (its peak) shows that the quadratic term dominates, so the posterior approaches a normal distribution. If the model is correct, $\theta_0$ is the true value. The results hold only "in probability" over the true data distribution, and they need conditions on prior, likelihood and parameter space.

**Prerequisites:** law of large numbers; Taylor expansion; Jensen's inequality; expectation of log-ratios; compactness (finite subcover); Fisher information.

## L2 — Key ideas (5–10 bullets)
- The setting is iid data from a true density $f$, analysed with a model $p(\cdot|\theta)$ that may be wrong. Theorems are "in probability" with respect to $f$ and need conditions on prior, likelihood and $\Theta$ (p. 587).
- $\theta_0$ is the minimizer of $\mathrm{KL}(\theta)$, the discrepancy between model and truth; it is assumed to be unique. If the model is correct, $\theta_0$ is the true parameter (pp. 587–588).
- Discrete case: if $\Theta$ is finite and $\Pr(\theta=\theta_0)>0$, then $\Pr(\theta=\theta_0|y)\to1$. The log posterior odds against any other $\theta$ drift to $-\infty$ by the law of large numbers (p. 588).
- Continuous case: the point mass argument fails, so the result is stated for neighborhoods. On a compact $\Theta$, a finite cover lets the discrete argument be adapted (p. 588).
- Normality needs consistency of the posterior mode and some regularity conditions, notably that $\theta_0$ is not on the boundary of $\Theta$ (p. 589).
- In the Taylor expansion at the mode, the quadratic coefficient grows of order $n$ and higher-order coefficients grow no faster. Because the posterior shrinks to $\theta_0$, the higher-order terms fade relative to the quadratic one (p. 589).
- Limit: normal with mean $\theta_0$ and variance $(nJ(\theta_0))^{-1}$. In the vector case the second derivative is a matrix whose expectation is minus a positive definite matrix (p. 589).
- The results hold more generally than iid data; the key condition is "replication" at some level (p. 590).

## L3 — Walkthrough

### Overview and mathematical framework (pp. 587–588)
Three steps (p. 587):
1. Convergence to a point for a discrete $\Theta$.
2. Concentration in shrinking neighborhoods for a continuous $\Theta$.
3. Accuracy of the normal approximation near the posterior mode.

Set-up (p. 587):
- Data $y=(y_1,\dots,y_n)$ are iid with true density $\prod_{i} f(y_i)$.
- The model has prior $p(\theta)$ and likelihood $p(y|\theta)=\prod_i p(y_i|\theta)$.
- Section 4.3 counterexamples show that conditions on the prior, likelihood and $\Theta$ are needed.
- A true distribution must be assumed because the theorems hold only in probability. For almost every problem one can construct data sequences for which the posterior lacks the limit. "Probability" refers to $f(y)$ (p. 587).

Kullback–Leibler divergence (p. 587):
$$\mathrm{KL}(\theta)=\mathrm E\!\left(\log\frac{f(y_i)}{p(y_i|\theta)}\right)=\int \log\!\left(\frac{f(y_i)}{p(y_i|\theta)}\right) f(y_i)\,dy_i. \tag{B.1}$$
- $\theta_0$ is the value of $\theta$ minimizing $\mathrm{KL}(\theta)$. It is assumed to be the unique minimizer (p. 587).
- If the model is correct, i.e. $f(y_i)=p(y_i|\theta)$ for some true $\theta$, then Jensen's inequality easily shows (B.1) is minimized at the true value, which is then called $\theta_0$ (p. 588).

*Intuition note:* KL measures how far the model is from the truth. Even a wrong model has a "closest" parameter, and the posterior ends up there. If the model is right, closest means true.

### Discrete parameter space (p. 588)
**Theorem.** If $\Theta$ is finite and $\Pr(\theta=\theta_0)>0$, then $\Pr(\theta=\theta_0|y)\to1$ as $n\to\infty$ (p. 588).

**Proof.** Show $p(\theta|y)\to0$ for every $\theta\ne\theta_0$. The log posterior odds relative to $\theta_0$ are
$$\log\frac{p(\theta|y)}{p(\theta_0|y)}=\log\frac{p(\theta)}{p(\theta_0)}+\sum_{i=1}^n\log\frac{p(y_i|\theta)}{p(y_i|\theta_0)}. \tag{B.2}$$
- With $\theta,\theta_0$ fixed and $y_i\sim f$, the sum has $n$ iid terms, each with mean $\mathrm E\log\frac{p(y_i|\theta)}{p(y_i|\theta_0)}=\mathrm{KL}(\theta_0)-\mathrm{KL}(\theta)$.
- This is zero if $\theta=\theta_0$ and negative otherwise, because $\theta_0$ is the unique minimizer (p. 588).
- By the law of large numbers the sum tends to $-\infty$ for $\theta\ne\theta_0$.
- The first term is finite as long as $p(\theta_0)>0$, so the whole expression tends to $-\infty$.
- Hence $p(\theta|y)/p(\theta_0|y)\to0$ and $p(\theta|y)\to0$. Probabilities sum to 1, so $p(\theta_0|y)\to1$ (p. 588).

*Intuition note:* Each observation adds a small negative amount, on average, to the log odds against a wrong $\theta$. The prior contributes only a fixed amount, so the data eventually win. The prior must not rule out $\theta_0$.

### Continuous parameter space (p. 588)
- If $\theta$ is continuous, $p(\theta_0|y)=0$ for any finite sample, so the discrete theorem does not apply.
- A neighborhood of $\theta_0$ is the open set of points in $\Theta$ within a fixed nonzero distance of $\theta_0$.

**Theorem.** If $\Theta$ is compact and $A$ is a neighborhood of $\theta_0$ with nonzero prior probability, then $\Pr(\theta\in A|y)\to1$ (p. 588).

**Proof sketch.**
- Put a small neighborhood around each point of $\Theta$, with $A$ the only one containing $\theta_0$.
- Compactness gives a finite subcover.
- The discrete-case argument is adapted to show every neighborhood except $A$ gets posterior probability $\to0$. So $\Pr(\theta\in A|y)\to1$ (p. 588).

### Convergence to normality (pp. 588–589)
The first two steps put as much mass as we like in any neighborhood of $\theta_0$. Two further steps remain: show the posterior mode is consistent, then use a normal approximation centered at the mode (p. 588).

**Theorem.** Under some regularity conditions, notably that $\theta_0$ not be on the boundary of $\Theta$, the posterior of $\theta$ approaches normality with mean $\theta_0$ and variance $(nJ(\theta_0))^{-1}$. Here $J$ is the Fisher information (2.20) (p. 589).

**Proof (scalar $\theta$).**
1. Let $\hat\theta$ be the posterior mode. The consistency proof for the maximum likelihood estimate (cited to the bibliographic note) can be mimicked to show $\hat\theta\to\theta_0$ (p. 589).
2. Expand the log posterior about $\hat\theta$ (p. 589):
$$\log p(\theta|y)=\log p(\hat\theta|y)+\tfrac12(\theta-\hat\theta)^2\frac{d^2}{d\theta^2}[\log p(\theta|y)]_{\theta=\hat\theta}+\tfrac16(\theta-\hat\theta)^3\frac{d^3}{d\theta^3}[\log p(\theta|y)]_{\theta=\hat\theta}+\cdots$$
The linear term is zero because the derivative vanishes at an interior mode (p. 589).
3. The first term is constant. The quadratic coefficient is
$$\frac{d^2}{d\theta^2}[\log p(\theta|y)]_{\theta=\hat\theta}=\frac{d^2}{d\theta^2}\log p(\hat\theta)+\sum_{i=1}^n\frac{d^2}{d\theta^2}[\log p(y_i|\theta)]_{\theta=\hat\theta}.$$
This is a constant plus a sum of $n$ iid terms with negative mean, where the $y_i$ are random (p. 589).
4. Each term has mean $-J(\theta_0)$ if $f(y)\equiv p(y|\theta_0)$ for some $\theta_0$. If $f$ is not in the model class, the mean is $\mathrm E_f\!\left(\frac{d^2}{d\theta^2}\log p(y|\theta)\right)$ at $\theta=\theta_0$. This is the negative second derivative of $\mathrm{KL}(\theta_0)$, and it is negative because $\theta_0$ minimizes KL (p. 589).
5. So the quadratic coefficient grows with order $n$. A similar argument shows third- and higher-order coefficients grow no faster than order $n$ (p. 589).
6. The posterior concentrates near $\theta_0$ and $|\hat\theta-\theta_0|\to0$. We can therefore focus on shrinking neighborhoods of $\hat\theta$. As $|\theta-\hat\theta|\to0$ the cubic and higher terms fade relative to the quadratic term. The quadratic approximation to the log posterior then becomes increasingly accurate, which is the normal approximation (p. 589).

*Intuition note:* A log density that is a quadratic in $\theta$ is a normal density. With more data the posterior is a narrow bump, and on a narrow bump a smooth log density looks like a parabola. The curvature grows like $n$, so the variance shrinks like $1/n$. The page does not spell out the step from curvature to the variance $(nJ(\theta_0))^{-1}$.

**Multivariate form.** For vector $\theta$ (p. 589):
$$\log p(\theta|y)=\log p(\hat\theta|y)+\tfrac12(\theta-\hat\theta)^T\frac{d^2}{d\theta^2}[\log p(\theta|y)]_{\theta=\hat\theta}(\theta-\hat\theta)+\cdots$$
The second derivative is now a matrix. Its expectation is the negative of a positive definite matrix, which is the Fisher information matrix (2.20) if $f(y)\equiv p(y|\theta_0)$ for some $\theta_0$ (p. 589).

### B.1 Bibliographic note (p. 590)
- Asymptotic normality of the posterior was known to Laplace (1810) and first proved rigorously by Le Cam (1953) (p. 590).
- Consistency and asymptotic normality hold under far more general conditions than iid data. The key condition is "replication" at some level, e.g. a time series whose correlations decay to zero (p. 590).
- Other references given: Kullback and Leibler (1951); Chernoff (1972); DeGroot (1970, Ch. 10); Shen and Wasserman (2001). The MLE proofs in Chernoff can be adapted to the posterior (p. 590).

## Toy example (ours)
Let $\theta$ be the probability of heads, with $\Theta=\{0.5,\,0.8\}$ and prior $\tfrac12,\tfrac12$. Let the data be iid coin flips from the true $f=\text{Bernoulli}(0.8)$, so the model is correct and $\theta_0=0.8$.

Mean of one term in (B.2) for $\theta=0.5$:
$$0.8\ln\tfrac{0.5}{0.8}+0.2\ln\tfrac{0.5}{0.2}=0.8(-0.4700)+0.2(0.9163)=-0.3760+0.1833=-0.1927.$$
Check via KL: $\mathrm{KL}(0.8)=0$ and $\mathrm{KL}(0.5)=0.8\ln\tfrac{0.8}{0.5}+0.2\ln\tfrac{0.2}{0.5}=0.3760-0.1833=0.1927$, so $\mathrm{KL}(\theta_0)-\mathrm{KL}(0.5)=-0.1927$.

The log prior odds are $\ln 1=0$. At the average, the log posterior odds after $n=50$ flips are $50\times(-0.1927)\approx-9.64$. The odds of $0.5$ against $0.8$ are then about $e^{-9.64}\approx6.5\times10^{-5}$. So $\Pr(\theta=0.8|y)\approx1/(1+6.5\times10^{-5})\approx0.99994$. Individual samples vary around this average, but the law of large numbers drives the sum to $-\infty$.

## Concepts
- [[posterior-consistency]] (new) — posterior mass concentrates at $\theta_0$, the KL minimizer (true value if the model is correct), as $n\to\infty$; holds in probability under $f$ (pp. 587–588)
- [[posterior-asymptotic-normality]] (new) — posterior approaches $N(\theta_0,(nJ(\theta_0))^{-1})$ under regularity conditions (p. 589)
- [[kl-divergence]] — here $\mathrm{KL}(\theta)=\mathrm E_f\log[f/p(\cdot|\theta)]$, a model–truth discrepancy; $\theta_0$ is its minimizer, assumed unique (p. 587)
- [[fisher-information]] (new) — $J(\theta_0)$, with $(nJ(\theta_0))^{-1}$ the limiting posterior variance; $-J$ is the mean of the second derivative of the log likelihood if the model is correct (p. 589)
- [[posterior-distribution]] — the object whose large-sample limit is studied (p. 587)
- [[prior-distribution]] — the limit results need conditions on the prior; in particular $p(\theta_0)>0$ in the discrete case, and nonzero prior probability of the neighborhood $A$ in the continuous case (pp. 587–588)

## Canonical instances
- (none; the unit has no worked data example. Counterexamples are referred to in Section 4.3 but not given here, p. 587.)

## Bridges (candidates)
- [structural-analogy] Posterior asymptotic normality ↔ frequentist inference: the MLE's consistency and asymptotic normality. The author says the MLE proofs can be mimicked or adapted for the posterior (pp. 589–590).
- [structural-analogy] Posterior concentrating on the KL-minimizing $\theta_0$ ↔ model misspecification: a wrong model still has a best-approximating parameter. KL here is $\mathrm{KL}(f\|p_\theta)$.
- [structural-analogy] Posterior asymptotic normality ↔ the central limit theorem: the author compares only the generality of conditions, saying that like the CLT the result holds far beyond iid data (p. 590).

## Questions this raises
- When the model is misspecified, is the variance $(nJ(\theta_0))^{-1}$ still right? The page states the mean as $-J(\theta_0)$ only for the correct-model case, and as the KL curvature otherwise.
- What happens when $\theta_0$ lies on the boundary of $\Theta$, or when $p(\theta_0)=0$?
- How large must $n$ be before the normal approximation is useful in practice? (The text defers this to Chapter 4.)
- How do the proofs extend beyond iid data, e.g. to time series with decaying correlations?

## Reading notes
- Page offset: printed = pdf − 10 (pdf 597–600 = printed 587–590).
- The text layer shows $\omega$ for the parameter. The page images show $\theta$, so I use $\theta$. The text layer also garbles "$(nJ(\theta_0))^{-1}$" as "→1"; the image shows $-1$.
- The subsection heading "B.1 Bibliographic note" shares its number with equation (B.1). The note refers to "the end of the chapter", though this is an appendix.
- The proofs are outlines. The continuous-space proof, the consistency of the posterior mode and the regularity conditions are only sketched or cited. The link from the quadratic coefficient (order $n$) to the variance $(nJ(\theta_0))^{-1}$ is not written out.
