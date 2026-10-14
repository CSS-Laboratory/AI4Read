---
id: gelman-2013-bda3/ch04-asymptotics
work: gelman-2013-bda3
unit: "4 Asymptotics and connections to non-Bayesian approaches"
pages: 83-100
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Asymptotics and connections to non-Bayesian approaches

## L0 — One line
With plenty of data from a well-behaved fixed model, the posterior is approximately normal and the prior matters little, which explains why Bayesian and classical answers often agree, but the chapter also lists where this breaks down and where classical ideas mislead.

## L1 — The gist (≤ 120 words)
When is a posterior approximately normal, and how do Bayesian answers relate to classical ones? The chapter builds a normal approximation centred at the posterior mode. It states asymptotic normality and consistency for large n, and lists counterexamples where the prior still matters in the limit. It then shows that Bayesian intervals have the matching frequentist coverage in large samples. The authors reinterpret classical tools (maximum likelihood, unbiasedness, confidence intervals, p-values, multiple comparisons, rank tests) and criticise several. The large-sample results are not needed to do Bayesian analysis; they are useful approximations and aids to understanding.

**Prerequisites:** Taylor expansion, Hessian matrix, multivariate normal and χ² distributions, posterior mode, Fisher information (BDA §2.8), Bayesian basics from Chapters 1–3.

## L2 — Key ideas (5–10 bullets)
- A posterior that is unimodal and roughly symmetric can be approximated by $\mathrm N(\hat\theta,[I(\hat\theta)]^{-1})$, where $\hat\theta$ is the posterior mode and $I(\hat\theta)$ is the observed information (minus the second derivative of the log posterior at the mode). This comes from a quadratic Taylor expansion of the log posterior at the mode (p. 83–84).
- In the normal approximation, the log density is a constant plus a χ² variable (with d degrees of freedom) divided by −2. This gives a benchmark for contour plots: the 0.05 contour holds about 95% of the mass for d = 2 (p. 85).
- Normal approximations are typically more accurate for marginal and conditional distributions than for the full joint, and closeness can often be improved by a suitable transformation. In the small-sample bioassay example the approximation is close to the exact posterior but with important differences (p. 85–87).
- Under regularity conditions the posterior approaches a normal with mean $\theta_0$ and variance $(nJ(\theta_0))^{-1}$, where $J$ is the Fisher information (BDA §2.8). If the model contains the truth it also converges to a point mass at $\theta_0$. The likelihood eventually dominates the prior (p. 88).
- Counterexamples, where the prior still matters in the limit, include nonidentified parameters, growing parameter counts, aliasing, unbounded likelihoods, improper posteriors, priors excluding the truth, boundary truth, and tails (p. 89–91). Nonidentified means the likelihood is equal over a range of parameter values; aliasing means the same likelihood repeats at discrete points; an improper posterior means the unnormalised posterior integrates to infinity.
- If the true distribution is in the model family, then in large samples a central posterior interval has the matching coverage under repeated sampling. When the truth is in the fitted family, the posterior mode, mean and median are consistent under mild regularity conditions, and under mild regularity conditions the centre of the posterior is asymptotically efficient (p. 91–92).
- In the authors' view, unbiasedness is reasonable in large samples but otherwise potentially misleading, and coverage alone is not a sufficient basis for inference. Examples are the mother–daughter height regression and the interval that is empty 5% of the time (p. 94–95).
- The authors' perspective gives little role to point-null hypothesis tests. They prefer to handle multiple comparisons with hierarchical models, which partially pool estimates toward each other (p. 95–96).
- The Wilcoxon rank test can be formulated as a transformation of the data followed by a comparison of means, which is approximately normal, so normal-theory intervals can be read as Bayesian statements. The authors see more flexibility in the Bayesian framework (p. 97).

## L3 — Walkthrough

### Introduction (p. 83)
Many simple Bayesian analyses with noninformative priors resemble standard non-Bayesian ones (for example the posterior t interval for a normal mean). As the sample size n grows, the prior's influence on posterior inference decreases (p. 83). These facts are "asymptotic theory", meaning properties in the limit of large n. The authors say large-sample results are not necessary for Bayesian data analysis but are often useful as approximations and tools for understanding (p. 83).

### 4.1 Normal approximations to the posterior distribution

**Joint posterior (p. 83–84).** If $p(\theta|y)$ is unimodal and roughly symmetric, the log posterior can be approximated by a quadratic function of $\theta$. The expansion is centred at the posterior mode $\hat\theta$, which is easy to compute with off-the-shelf optimisation. $\hat\theta$ is assumed to be in the interior of the parameter space; $\theta$ may be a vector.

$$\log p(\theta|y)=\log p(\hat\theta|y)+\tfrac12(\theta-\hat\theta)^T\Big[\tfrac{d^2}{d\theta^2}\log p(\theta|y)\Big]_{\theta=\hat\theta}(\theta-\hat\theta)+\cdots \tag{4.1}$$

- The linear term is zero because the log posterior has zero derivative at its mode (p. 83).
- Viewed as a function of $\theta$, the first term is constant and the second is proportional to a log normal density (p. 84). This gives

$$p(\theta|y)\approx \mathrm N\big(\hat\theta,[I(\hat\theta)]^{-1}\big),\tag{4.2}$$

with observed information $I(\theta)=-\frac{d^2}{d\theta^2}\log p(\theta|y)$. For a $d$-dimensional $\theta$, $I(\hat\theta)$ is a $d\times d$ matrix, positive definite if the mode is in the interior (p. 84). Higher-order terms fade relative to the quadratic one when $\theta$ is near $\hat\theta$ and n is large (p. 83). Chapter 13 gives more elaborate approximations for cases where mode-based ones fail (p. 83).

**Example: normal with unknown mean and variance (p. 84).** Take $y_1,\dots,y_n$ independent $\mathrm N(\mu,\sigma^2)$ with uniform prior on $(\mu,\log\sigma)$. Working with $\log\sigma$ restricts $\sigma$ to positive values.

$$\log p(\mu,\log\sigma|y)=\text{const}-n\log\sigma-\frac1{2\sigma^2}\big((n-1)s^2+n(\bar y-\mu)^2\big).$$

First derivatives:

$$\frac{d}{d\mu}\log p=\frac{n(\bar y-\mu)}{\sigma^2},\qquad \frac{d}{d(\log\sigma)}\log p=-n+\frac{(n-1)s^2+n(\bar y-\mu)^2}{\sigma^2}.$$

Setting both to zero gives the mode $(\hat\mu,\log\hat\sigma)=\big(\bar y,\ \log(\sqrt{(n-1)/n}\,s)\big)$.

Second derivatives:

$$\frac{d^2}{d\mu^2}\log p=-\frac n{\sigma^2},\quad \frac{d^2}{d\mu\,d(\log\sigma)}\log p=-2n\frac{\bar y-\mu}{\sigma^2},\quad \frac{d^2}{d(\log\sigma)^2}\log p=-\frac2{\sigma^2}\big((n-1)s^2+n(\bar y-\mu)^2\big).$$

At the mode the matrix of second derivatives is $\begin{pmatrix}-n/\hat\sigma^2&0\\0&-2n\end{pmatrix}$. By (4.2),

$$p(\mu,\log\sigma|y)\approx \mathrm N\!\left(\begin{pmatrix}\mu\\ \log\sigma\end{pmatrix}\Big|\begin{pmatrix}\bar y\\ \log\hat\sigma\end{pmatrix},\begin{pmatrix}\hat\sigma^2/n&0\\0&1/(2n)\end{pmatrix}\right).$$

Working with $(\mu,\sigma^2)$ instead, the second-derivative matrix is multiplied by the Jacobian of the transformation from $\log\sigma$ to $\sigma^2$. The mode changes slightly, to $\tilde\sigma^2=\frac n{n+2}\hat\sigma^2$. The components stay independent in the approximation, and $p(\sigma^2|y)\approx\mathrm N(\sigma^2|\tilde\sigma^2,2\tilde\sigma^4/(n+2))$ (p. 84).

*Intuition note.* Near an interior peak, a smooth log posterior looks like a downward parabola, and a parabola in the log is a normal density. The curvature at the peak sets the width. Different parameterisations ($\log\sigma$ versus $\sigma^2$) give different approximations (in this example the mode shifts slightly).

**Interpreting the density relative to its maximum (p. 85).** In a $d$-dimensional normal, the log density equals a constant plus a $\chi^2_d$ variable divided by $-2$. The 95th percentile of $\chi^2_{10}$ is 18.31. So with $d=10$, about 95% of posterior mass lies where $p(\theta|y)$ is at least $\exp(-18.31/2)=1.1\times10^{-4}$ times the mode density. With $d=2$ the cutoff is $\exp(-5.99/2)=0.05$, so the 0.05 contour of a 2-D posterior plot includes about 95% of the mass (p. 85).

**Point estimates and standard errors (p. 85).** A standard summary is the 95% interval "estimate ± two standard errors", with the standard error taken from $I(\hat\theta)$. The estimate may be the maximum likelihood estimate, which is the posterior mode under a uniform prior. A different asymptotic argument gives this a frequentist interpretation, and in many simple situations both interpretations hold. General guidance on when the normal approximation is adequate is hard to give. From the Bayesian view, accuracy can be checked by inspecting the posterior. Convergence to normality can often be improved dramatically by a continuous transformation $\phi$ of $\theta$. Both $p(\phi|y)$ and $p(\theta|y)$ approach normality, but finite-n closeness can vary a lot with the transformation (p. 85).

**Data reduction (p. 85).** Under the normal approximation, the mode and the curvature $I(\hat\theta)$ are, asymptotically, sufficient statistics. Summarising each source by such statistics makes hierarchical modelling easy; Section 5.5 summarises eight experiments this way. It is most reasonable when posteriors are near normal and can otherwise discard important information and give erroneous inferences (p. 85).

**Lower-dimensional approximations (p. 85–86).**
- For finite n the approximation is typically more accurate for conditional and marginal distributions of components than for the full joint. A multivariate normal has normal margins, but the converse is not true.
- Marginalising means averaging over other components, and averaging generally moves distributions toward normality, by the logic of the central limit theorem (p. 85–86).
- For high-dimensional $\theta$, two situations are common: (i) many individual marginals are approximately normal, so each can be summarised by an estimate and a standard error; (ii) $\theta=(\theta_1,\theta_2)$ with $p(\theta_2|y)$ not necessarily near normal, but $p(\theta_1|\theta_2,y)$ near normal with mean and variance depending on $\theta_2$. Section 13.5 treats this further (p. 86).
- Normal approximations are also useful for debugging code or checking a more elaborate approximation (p. 86).

**Example: bioassay (continued) (p. 86–87).** There are only twenty animals. The posterior mode of $(\alpha,\beta)$ equals the maximum likelihood estimate (uniform prior) and was computed with a logistic regression program (p. 86).
- Figure 4.1 shows contours and 1000 draws from the bivariate normal approximation. It resembles Figure 3.3 but lacks the skewness in the upper right. The mean of the approximation is $(\alpha,\beta)=(0.8,7.7)$ versus $(1.4,11.9)$ for the actual posterior (p. 86).
- Of 1000 draws, 950 had $\beta>0$, so the approximation gives $\Pr(\beta>0)=0.95$. The exact distribution gives $\Pr(\beta>0)>0.999$ (p. 87).
- LD50 is computed as $-\alpha/\beta$ for the 950 draws with $\beta>0$. Their range is $[-12.4,5.4]$ (Figure 4.2 caption). The histograms are centred about where Figure 3.4 is but have substantially more variation, because $\beta$ may be close to zero (p. 87).
- Summary: the normal approximation is roughly similar to the exact results. The actual joint posterior is substantially more skewed, and the actual LD50 posterior has much shorter tails than the joint normal approximation implies. Whether this makes the approximation inadequate depends on the aim of the analysis (p. 87).

### 4.2 Large-sample theory (p. 87–88)

**Setup.** Asymptotic normality of the posterior is the basic tool. As more data arrive from the same underlying process, the posterior of the parameter vector approaches multivariate normality, even if the true data distribution is not in the parametric family (p. 87). The results apply most directly to $y_1,\dots,y_n$ independent draws from a common distribution $f(y)$. A "true" $f(y)$ is often hard to interpret, but the theory needs it (p. 87–88). The model is $p(y|\theta)$ with prior $p(\theta)$.
- If $f(y)=p(y|\theta_0)$ for some $\theta_0$, then consistency also holds: the posterior converges to a point mass at $\theta_0$ as $n\to\infty$ (p. 88).
- If the truth is outside the family, $\theta_0$ is replaced by the value that makes $p(y|\theta)$ closest to $f(y)$ in a sense involving Kullback–Leibler divergence (Appendix B) (p. 88).
- Fisher information $J(\theta)$, introduced as (2.20), plays an important role (p. 88).

**Asymptotic normality and consistency (p. 88).** Under regularity conditions (notably, the likelihood is continuous in $\theta$ and $\theta_0$ is not on the boundary), the posterior approaches normality with mean $\theta_0$ and variance $(nJ(\theta_0))^{-1}$ as $n\to\infty$. The simplest understanding uses the expansion (4.1). A preliminary result shows the posterior mode is consistent for $\theta_0$, so posterior mass concentrates in ever smaller neighbourhoods of $\theta_0$ and $|\hat\theta-\theta_0|\to0$. The quadratic coefficient splits into a prior term and $n$ likelihood terms:

$$\Big[\tfrac{d^2}{d\theta^2}\log p(\theta|y)\Big]_{\theta=\hat\theta}=\Big[\tfrac{d^2}{d\theta^2}\log p(\theta)\Big]_{\theta=\hat\theta}+\sum_{i=1}^n\Big[\tfrac{d^2}{d\theta^2}\log p(y_i|\theta)\Big]_{\theta=\hat\theta}.$$

Each likelihood term has expected value, under $p(y|\theta_0)$, approximately $-J(\theta_0)$ when $\hat\theta$ is close to $\theta_0$ (assuming $f(y)=p(y|\theta_0)$). So for large n the curvature is approximated by the Fisher information at $\hat\theta$ or $\theta_0$ (only $\hat\theta$ is available in practice). In the limit, the curvature approaches $nJ(\hat\theta)$ or $nJ(\theta_0)$, and the likelihood dominates the prior, so the likelihood alone gives mode and curvature (p. 88). Precise theorems and proof sketches are in Appendix B (p. 88).

*Intuition note.* Each observation adds one more curvature term, while the prior adds only one in total. So the total curvature grows like n and the posterior spread shrinks like $1/\sqrt n$. The prior's single term is eventually negligible.

**Likelihood dominating the prior (p. 88).** The importance of the prior diminishes with sample size. With large samples we need not work hard to encode all information in the prior; with small samples the prior is a critical part of the model (p. 88).

### 4.3 Counterexamples to the theorems (p. 89–91)
The failures generally correspond to situations in which the prior still affects the posterior in the limit of infinite data (p. 89).

- **Underidentified models / nonidentified parameters.** The likelihood $p(y|\theta)$ is equal over a range of $\theta$ (a "flat likelihood"; the term is sometimes also used for weakly identified parameters). There is then no single $\theta_0$ for the posterior to converge to. Example: $(u,v)\sim\mathrm N\big((0,0),\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\big)$ with only one of $u,v$ observed per pair. The data say nothing about $\rho$, so its posterior equals its prior however large the dataset. The only remedy is to recognise the problem and, if wanted, gather more information from new data or from external information in a prior (p. 89).
- **Number of parameters increasing with n.** If the model grows with n, the fixed-model results of 4.1–4.2 do not apply. Example: $y_i\sim\mathrm N(\theta_i,\sigma^2)$, one parameter per unit. The $\theta_i$ generally cannot be estimated consistently unless data per unit grow with the number of units. Gaussian processes (Chapter 21) can have a new latent parameter per data point. The posterior need not converge to a point in the expanding space, and the marginal posterior of a given $\theta_i$ need not converge either (p. 89).
- **Aliasing.** A special case of underidentification in which the same likelihood repeats at a discrete set of points. Normal mixture, $\theta=(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\lambda)$:
$$p(y_i|\theta)=\lambda\tfrac1{\sqrt{2\pi}\sigma_1}e^{-\frac1{2\sigma_1^2}(y_i-\mu_1)^2}+(1-\lambda)\tfrac1{\sqrt{2\pi}\sigma_2}e^{-\frac1{2\sigma_2^2}(y_i-\mu_2)^2}.$$
Interchanging $(\mu_1,\mu_2)$ and $(\sigma_1^2,\sigma_2^2)$ and replacing $\lambda$ by $1-\lambda$ leaves the likelihood unchanged. The posterior generally has at least two modes, a (50%, 50%) mixture of mirror images, with no convergence to a single point. Restricting the parameter space removes aliasing, e.g. $\mu_1\le\mu_2$ (p. 89–90).
- **Unbounded likelihoods.** There may be no posterior mode in the parameter space, which invalidates consistency and the normal approximation. In the mixture with $\lambda$ known and not 0 or 1, set $\mu_1=y_i$ for any $y_i$ and let $\sigma_1^2\to0$; the likelihood goes to infinity. The number of likelihood modes increases with n. With a prior uniform on $\sigma_1^2,\sigma_2^2$ near zero, posterior modes likewise increase, with no corresponding normal approximations. A prior proportional to $\sigma_1^{-2}\sigma_2^{-2}$ makes this worse. The authors say this should rarely arise in practice, because the poles correspond to unrealistic model conditions. Remedies include restricting to plausible distributions, a prior declining to zero at the boundary, or an informative prior on the ratio of variances (p. 90).
- **Improper posterior distributions.** If likelihood times an improper prior integrates to infinity, the asymptotic results, which rely on probabilities summing to 1, do not follow. An improper posterior cannot occur except with an improper prior. Simple example: a Beta(0,0) prior for a binomial proportion with n successes and 0 failures. Subtler cases appear in Sections 5.3 and 5.4. The remedy is a proper prior, or at least an improper prior whose product with the likelihood has a finite integral (p. 90).
- **Prior excludes the point of convergence.** If $p(\theta_0)=0$ (discrete space), or $p(\theta)=0$ in a neighbourhood of $\theta_0$ (continuous space), convergence results based on the likelihood dominating the prior fail. Give positive density to all values that are even remotely plausible (p. 90).
- **Convergence to the edge of parameter space.** If $\theta_0$ is on the boundary, the Taylor expansion must be truncated in some directions and the normal need not be appropriate even in the limit. Take $y_i\sim\mathrm N(\theta,1)$ with $\theta\ge0$. If the true $\theta=0$, the posterior is normal centred at $\bar y$, truncated to be positive, and in the limit is half a normal centred at 0. If the true $\theta=-1$ (outside the space), the limiting posterior is a sharp spike at 0, nothing like a normal (p. 90). In practice, be wary of the normal approximation near the edge, and give positive prior density to all remotely possible values (p. 91).
- **Tails.** The approximation can hold for essentially all the mass yet be inaccurate in the tails. If $p(\theta|y)\propto e^{-c|\theta|}$ as $|\theta|\to\infty$, while the normal is $\propto e^{-c\theta^2}$, the distribution function still converges to normality, but for finite n the approximation fails far out. For a positive-constrained parameter, the normal approximation always gives some mass to negative values, but that point moves farther into the tail as n grows (p. 91).

*Intuition note.* Several of these failures are ways for the data to stay silent or ambiguous about the parameter, or for the prior to forbid the truth. The authors say the counterexamples generally correspond to cases where the prior still affects the posterior even with infinite data (p. 89).

### 4.4 Frequency evaluations of Bayesian inferences (p. 91–92)
Frequentist methods can evaluate the operating characteristics of Bayesian inferences when these are embedded in repeated samples. "Stable estimation" says that for a fixed model the posterior approaches a point as data arrive. It is appealing that if the model family contains the true distribution and gives it nonzero prior density, the posterior converges to the true $\theta$ (p. 91).

**Large-sample correspondence (p. 91).** If (4.2) holds, then with $[I(\hat\theta)]^{1/2}$ any matrix square root of $I(\hat\theta)$,

$$[I(\hat\theta)]^{1/2}(\theta-\hat\theta)\,|\,y\sim\mathrm N(0,I).\tag{4.3}$$

Since $\hat\theta\to\theta_0$, one could write the approximation with $I(\theta_0)$. If $f(y)\equiv p(y|\theta)$ for some $\theta$, then in repeated sampling with fixed $\theta$, as $n\to\infty$ it can be proved that

$$[I(\hat\theta)]^{1/2}(\theta-\hat\theta)\,|\,\theta\sim\mathrm N(0,I).\tag{4.4}$$

This is classical theory, generally proved for $\hat\theta$ the maximum likelihood estimate, and easily extended to the posterior mode (p. 91). So, for any function of $(\theta-\hat\theta)$, the posterior distribution from (4.3) is asymptotically the same as the repeated-sampling distribution from (4.4). Example: a 95% central posterior interval covers the true value 95% of the time under repeated sampling with any fixed true $\theta$ (p. 91).

*Intuition note.* In (4.3) $\theta$ is random and $\hat\theta$ fixed; in (4.4) $\hat\theta$ is random and $\theta$ fixed. Under the stated conditions (for (4.4), the truth is in the model family), both give the same standard normal in large samples, so the same interval has asymptotically the same probability read either way.

**Point estimation, consistency, efficiency (p. 91–92).**
- Single-number estimates make most sense in large samples, when the mode is the obvious centre and $I(\hat\theta)$ conveys negligible uncertainty. In smaller samples, especially with variable or asymmetric posteriors, one value is inappropriate. Loss functions can define optimal point estimates (Section 9.1, Exercise 9.6), but the authors believe the full posterior (e.g. 50% and 95% central intervals) is more useful. A point estimate plus standard error is an inferential summary, not the solution to a decision problem (p. 91–92).
- *Consistent* (sampling-theory sense): if $f(y)\equiv p(y|\theta_0)$, $\hat\theta$ is consistent if its sampling distribution converges to a point mass at $\theta_0$ as n grows. *Asymptotic unbiasedness*: $(\mathrm E(\hat\theta|\theta_0)-\theta_0)/\mathrm{sd}(\hat\theta|\theta_0)\to0$. When the truth is in the fitted family, the posterior mode, mean and median are consistent and asymptotically unbiased under mild regularity conditions (p. 92).
- *Efficient*: no other function of $y$ has lower mean squared error $\mathrm E((\hat\theta-\theta_0)^2|\theta_0)$. Efficiency is the optimal MSE divided by that of $\hat\theta$. Asymptotically efficient means efficiency $\to1$ as $n\to\infty$. Under mild regularity conditions, the posterior mean, median or mode is asymptotically efficient (p. 92).

**Confidence coverage (p. 92).** A region $C(y)$ that includes $\theta_0$ at least $100(1-\alpha)\%$ of the time in repeated samples, for any $\theta_0$, is a $100(1-\alpha)\%$ confidence region. The word "confidence" signals a behavioural meaning: for small $\alpha$ one should act as if the truth is in the region in each application. Asymptotically, a $100(1-\alpha)\%$ central posterior interval has this coverage property (p. 92).

### 4.5 Bayesian interpretations of other statistical methods (p. 92–97)
Three levels of comparison: (1) similar results in large samples from a fixed model; (2) even in small samples, many methods approximate Bayesian inference under some implicit prior; (3) some classical methods, notably hypothesis testing, can differ greatly (p. 92).

**Crude procedures as implicit models (p. 93).**
- *Ratio estimation* in surveys: estimating $R=\bar y/\bar x$ by $\bar y_{\rm obs}/\bar x_{\rm obs}$ corresponds to a summary of Bayesian inference given independent $y_i|x_i\sim\mathrm N(Rx_i,\sigma^2x_i)$ and a noninformative prior. It can be useful when this model fails, but generally is not appropriate when data deviate greatly from it.
- *Selecting regression predictors by significance* corresponds roughly to Bayesian analyses with exchangeable priors on coefficients, each a mixture of a peak at zero and a widely spread distribution (Section 14.6). Such procedures can often be improved with extra information, e.g. clustering likely-similar coefficients into batches.

**Maximum likelihood and other point estimates (p. 93–94).**
- In the large-n limit (regularity assumed), the maximum likelihood estimate is a sufficient statistic, and so is the posterior mode, mean or median. This gives a theoretical Bayesian justification for classical ML inference. The asymptotic irrelevance of the prior can justify convenient noninformative priors (p. 93).
- In repeated sampling with $\theta=\theta_0$: $p(\hat\theta(y)|\theta=\theta_0)\approx\mathrm N(\hat\theta(y)|\theta_0,(nJ(\theta_0))^{-1})$.
- Assuming a prior locally uniform (or continuous and nonzero) near the true $\theta$, the normal-mean analysis of Section 3.5 gives $p(\theta|\hat\theta)\approx\mathrm N(\theta|\hat\theta,(nJ(\hat\theta))^{-1})$. This also follows directly from asymptotic normality, but the indirect route gives a Bayesian rationale for classical point estimate plus standard error inference (p. 93).
- For finite n this is wasteful to the extent that $\hat\theta$ is not sufficient. With many parameters, consistency is often unhelpful and noninformative priors are hard to justify; hierarchical models (Chapter 5) are preferable. Any likelihood-only method can be improved if real prior information is strong enough to add substantially to the likelihood (p. 93–94).

**Unbiased estimates (p. 94–95).**
- $\hat\theta(y)$ is unbiased if $\mathrm E(\hat\theta(y)|\theta)=\theta$ for every $\theta$, the expectation over $p(y|\theta)$. From the Bayesian view this is reasonable for large samples but otherwise potentially misleading. With many parameters, partial knowledge of some is relevant to others, and requiring unbiasedness ignores it (Chapter 5). In sampling terms, minimising bias often leads to counterproductive increases in variance (p. 94).
- It is often impossible to estimate several parameters at once in an even approximately unbiased manner. Unbiased estimates of $\theta_1,\dots,\theta_J$ yield an upwardly biased estimate of the variance of the $\theta_j$, except when they are known exactly (p. 94).
- **Example: prediction using regression (p. 94).** Estimate a daughter's height $\theta$ from her mother's height $y$. Assume joint normality, known equal means of 160 cm, equal variances, correlation 0.5. Conditioning on $y$ (Bayesian inference):
$$\mathrm E(\theta|y)=160+0.5(y-160).\tag{4.5}$$
Given $\theta$, $\mathrm E(y|\theta)=160+0.5(\theta-160)$. So under repeated sampling of $y$ with $\theta$ fixed, the posterior mean (4.5) has expectation $160+0.25(\theta-160)$ and is biased toward 160. The estimate $\hat\theta=160+2(y-160)$ is unbiased in that sense but absurd: a mother 10 cm above average gives a daughter estimated 20 cm above average (p. 94).
- Here a sensible non-Bayesian would call this "prediction" and not evaluate procedures conditional on the random $\theta$. The example shows unbiasedness forces a parameter-versus-prediction split with no clear substantive basis (p. 94).
- *Regression to the mean:* a daughter's expected height lies between her mother's height and the population mean. The authors call Bayesian analysis in many ways a logical extension of this principle, weighting information from different sources properly (p. 95).

**Confidence intervals (p. 95).** Even in small samples, Bayesian $(1-\alpha)$ posterior intervals often have close to $(1-\alpha)$ confidence coverage conditional on $\theta$. But some purely sampling-theory intervals differ considerably from Bayesian ones, and the authors regard them as of doubtful value. A general theory based on unconditional behaviour can give counterintuitive results such as intervals of zero or infinite length. Example: an interval that is empty 5% of the time and is the whole real line 95% of the time covers the truth in 95% of repeated samples. This shows that coverage alone is not a sufficient basis for reasonable inference, not that coverage is worthless (p. 95).

**Hypothesis testing (p. 95).**
- The book's perspective gives little role to hypothesis tests, especially point nulls $\theta=\theta_0$. A Bayesian analysis gives a point null nonzero posterior probability only if it starts with nonzero prior probability. For a continuous parameter, a prior with a discrete mass (say 0.5) at $\theta_0$ mixed with a continuous density usually seems contrived. Most difficulties come from the artificial dichotomy $\theta=\theta_0$ versus $\theta\ne\theta_0$.
- For a continuous parameter, "Does $\theta$ equal 0?" can generally be rephrased more usefully as "What is the posterior distribution for $\theta$?" (p. 95).
- One-sided p-values may correspond to posterior probabilities under noninformative priors. Example: observe $y=1$ from $\mathrm N(\theta,1)$ with uniform prior. One-sided p-value 0.16, two-sided 0.32, both above 0.05, so one cannot "reject" $\theta=0$. The posterior probability that $\theta>0$ is 84%, a more informative conclusion than "reject/do not reject" (p. 95).
- A form of test is useful for checking a model's goodness of fit, by comparing observed data to predictive outcomes (Chapter 6) (p. 95).

**Multiple comparisons and multilevel modeling (p. 96).** Take independent $y_j\sim\mathrm N(\theta_j,1)$ for $J$ parameters, with the goal of detecting differences and ordering.
- Classical procedures declare which $\theta_j$ are "significantly different". The Bayesian approach gives a joint posterior and can give the posterior probability of each of the $J!$ orderings. If there is posterior uncertainty in the ordering, several permutations will have substantial probabilities, which is a more reasonable conclusion than a list of "different" $\theta_j$, which falsely implies the others may be exactly equal. For large $J$, a posterior median and interval for each $\theta_j$'s quantile in the population may be more reasonable (p. 96).
- The authors prefer hierarchical models (Section 5.5, eight schools; Exercise 5.3). They automatically partially pool estimates toward each other when there is little evidence of real variation, which addresses the classical concern about large differences arising from searching many comparisons. In the eight-schools example there are $8\cdot7/2=28$ comparisons and none is close to "significant" (zero lies within all 95% intervals for pairwise differences). This makes sense because the between-school variation $\tau$ is estimated to be low (p. 96).

**Nonparametric methods, permutation tests, jackknife, bootstrap (p. 96–97).**
- Methods avoiding complete probability models are hard to evaluate from a Bayesian view. Rank-based tests comparing medians have no direct Bayesian counterpart. There is often arbitrariness in what to jackknife or bootstrap. Without a probability model it is hard to test a method's assumptions. The authors prefer constructing a joint distribution and checking it against data (Chapter 6). They use nonparametric methods as tools for data summary and description (p. 96).
- **Hypothetical critic (the authors say "one might well say"):** Bayesian methods involve arbitrary choices of models and are difficult to evaluate because in practice there will always be important aspects of a model that are impossible to check. The authors state their aim is not to disparage nonparametric methods but to put them in a Bayesian context as far as possible (p. 96).
- Permutation tests for experiments and sampling-theory inference for surveys give results similar to Bayesian inference with noninformative priors in simple problems (balanced designs, no missing data, simple random sampling), if the Bayesian model fits reasonably. With several parameters, explanatory variables or prior information, these methods give no direct answer, which is a practical incentive to move to a model-based Bayesian approach (p. 96–97).
- **Example: Wilcoxon rank test (p. 97).** Samples $(y_1,\dots,y_{n_y})$, $(z_1,\dots,z_{n_z})$ are ranked jointly from 1 to $n=n_y+n_z$. One computes the difference of average ranks and a p-value against a tabulated distribution assuming random assignment of ranks. This equals a nonlinear transformation (data point → rank) followed by comparing two sample means. Using quantiles $\frac1{2n},\frac3{2n},\dots,\frac{2n-1}{2n}$ instead of ranks makes the mean difference an average distance on the quantile scale of the combined distribution. By the central limit theorem, the mean difference is approximately normal, so classical normal-theory intervals can be read as Bayesian posterior statements.
- Two advantages of this view: more flexibility for regression predictors and censored or truncated data, and a reminder that any appropriate transformation may be used, with combined quantiles a convenient default (p. 97).

### 4.6 Bibliographic note (p. 97–98)
Relatively little has been written on the practical implications of asymptotics for Bayesian analysis. Edwards, Lindman and Savage (1963) is called one of the best overviews and covers "stable estimation". Further sources cover frequency evaluation of Bayesian procedures (Morris 1983, Rubin 1984), p-values (Krantz 1999, Berger and Sellke 1987), multiple comparisons in hierarchical models, and Bayesian sequential analysis of clinical trials. Stigler (1983, 1986) is cited for Bayesian inference as regression prediction and Galton's use of regression (p. 97–98).

### 4.7 Exercises (p. 98–100)
Fifteen exercises: normal approximation for a Cauchy location and for the bioassay model, the delta method for LD50, loss functions and Bayes estimates, unbiasedness, regression to the mean, non-Bayesian analysis of the bioassay, Bayesian readings of significance-based estimators, discussion of criticisms of Bayesianism, and coverage of posterior intervals (p. 98–100).

## Toy example (ours, not from the text)
Data: $y=2$ successes in $n=10$ trials, uniform prior on $\theta\in(0,1)$. The posterior is Beta(3, 9).

*Normal approximation.*
- Log posterior: $2\log\theta+8\log(1-\theta)$ + const. Setting the derivative $2/\theta-8/(1-\theta)=0$ gives mode $\hat\theta=2/10=0.2$.
- Second derivative: $-2/\theta^2-8/(1-\theta)^2$. At 0.2 this is $-2/0.04-8/0.64=-50-12.5=-62.5$. So $I(\hat\theta)=62.5$, variance $1/62.5=0.016$, sd $=0.1265$.
- Check against Fisher information: $J(\theta)=1/(\theta(1-\theta))=1/0.16=6.25$, and $nJ=62.5$. This matches.
- Exact Beta(3,9): mean $3/12=0.25$, sd $=\sqrt{27/(144\cdot13)}=\sqrt{0.01442}=0.120$. The normal approximation has mean 0.2, and $0.2/0.1265=1.58$ sd from zero, so it gives about $\Phi(-1.58)\approx0.057$ mass to $\theta<0$.

*Ten times the data*, $y=20$, $n=100$: the posterior is Beta(21, 81).
- Mode 0.2; $I=20/0.04+80/0.64=500+125=625$; sd $=1/25=0.04$.
- Exact mean $21/102=0.206$; exact sd $=\sqrt{1701/1071612}=0.0398$.
- Now the mode is $0.2/0.04=5$ sd from zero, and the mean and sd are close to the exact ones (0.200 vs 0.206 for the mean, 0.040 vs 0.0398 for the sd). This is the chapter's claim in miniature: the approximation improves with n, and the curvature grows like n (62.5 → 625).

## Concepts
- [[normal-approximation-posterior]] (new) — approximate $p(\theta|y)$ by $\mathrm N(\hat\theta,[I(\hat\theta)]^{-1})$ from a quadratic expansion at the mode (p. 84)
- [[observed-information]] (new) — $I(\theta)=-\frac{d^2}{d\theta^2}\log p(\theta|y)$, the curvature of the log posterior (p. 84)
- [[fisher-information]] (new) — $J(\theta)$ from BDA (2.20); each likelihood term's second derivative has expected value about $-J(\theta_0)$, so the curvature is about $nJ$ (p. 88)
- [[asymptotic-normality-consistency]] (new) — posterior → normal with variance $(nJ(\theta_0))^{-1}$; if the truth is in the family, also a point mass at $\theta_0$ (p. 88)
- [[posterior-distribution]] — here used as the full inferential summary, preferred over a single point estimate (p. 92)
- [[prior-distribution]] — its influence fades as n grows, except in the listed counterexamples (p. 88–89)
- [[likelihood]] — dominates the prior for large n; flat for nonidentified parameters (p. 88–89)
- [[underidentification-aliasing]] (new) — likelihood equal over a range (underidentified) or repeating at discrete points (aliasing); no convergence (p. 89)
- [[improper-posterior]] (new) — likelihood × improper prior integrates to infinity; asymptotic results fail (p. 90)
- [[kl-divergence]] — when the truth is outside the family, $\theta_0$ is the value making the model closest to the truth in a sense involving KL divergence (p. 88)
- [[frequentist-vs-bayesian-inference]] — large-sample correspondence of (4.3) and (4.4); methods compared in 4.5 (p. 91–97)
- [[confidence-region]] (new) — region covering $\theta_0$ at least $100(1-\alpha)\%$ of the time in repeated samples for any $\theta_0$ (p. 92)
- [[credible-interval]] — central posterior interval; asymptotically has the matching confidence coverage (p. 91)
- [[unbiased-estimator]] (new) — $\mathrm E(\hat\theta|\theta)=\theta$ for all $\theta$; from the Bayesian view reasonable in the limit of large samples but otherwise potentially misleading (p. 94)
- [[regression-to-the-mean]] (new) — expected daughter height lies between mother's height and the population mean (p. 95)
- [[efficiency-estimator]] (new) — optimal MSE divided by the estimator's MSE (p. 92)
- [[partial-pooling-shrinkage]] — hierarchical models shrink $\theta_j$ estimates together, handling multiple comparisons (p. 96)
- [[hierarchical-model]] — preferred for many parameters and multiple comparisons (p. 93, 96)

## Canonical instances
- [[normal-unknown-mean-variance-approx]] — normal approximation for $(\mu,\log\sigma)$ with diagonal covariance $\mathrm{diag}(\hat\sigma^2/n,1/(2n))$ (p. 84)
- [[bioassay-normal-approximation]] — small-sample differences: mean $(0.8,7.7)$ vs $(1.4,11.9)$; $\Pr(\beta>0)$ 0.95 vs >0.999 (p. 86–87)
- [[mother-daughter-heights]] — posterior mean biased but sensible; unbiased estimate absurd (p. 94)
- [[p-value-y1-example]] — $y=1$, $\mathrm N(\theta,1)$: p-values 0.16/0.32 but posterior $\Pr(\theta>0)=84\%$ (p. 95)
- [[eight-schools-multiple-comparisons]] — 28 pairwise comparisons, none significant, $\tau$ estimated low (p. 96)
- [[wilcoxon-as-transformed-normal]] — ranks → quantiles, then normal-theory mean difference (p. 97)
- [[ratio-estimation-implicit-model]] — ratio estimate as summary of posterior under $y_i|x_i\sim\mathrm N(Rx_i,\sigma^2x_i)$ (p. 93)

## Bridges (candidates)
- [structural-analogy] Quadratic expansion of the log posterior at the mode ↔ the more elaborate approximations of Chapter 13, which the text says can work where simple mode-based ones fail (p. 83): both approximate the posterior by a simpler density.
- [same-math] Posterior $\mathrm N(\hat\theta,I^{-1})$ in (4.3) ↔ frequentist sampling distribution of the MLE in (4.4): the same standardised normal, read with $\theta$ random or $\hat\theta$ random.
- [structural-analogy] Posterior mean shrinks toward the population mean in the mother–daughter example ↔ partial pooling in hierarchical models: both weight own data against the population distribution.
- [structural-analogy] Nonidentified $\rho$ with posterior = prior ↔ any parameter with a flat likelihood: data add no information, so the prior carries all inference.

## Questions this raises
- How can one tell, for a given dataset, whether n is large enough for the normal approximation, beyond inspecting the posterior? The text offers no general guideline (p. 85).
- Which parameterisation of a parameter gives the best finite-n normal approximation? The text only says it can vary substantially (p. 85).
- If $\phi=f(\theta)$ is a nonlinear transformation, both $p(\theta|y)$ and $p(\phi|y)$ approach normality (p. 85). How can both limits be valid? This is Exercise 4 (p. 99).
- What does an implicit prior look like for a significance-thresholded estimator (Exercises 11–12, p. 100)?

## Exercises worth doing
- Ex. 1 (p. 98) — normal approximation for a Cauchy location with a bounded prior, compared to the exact density — difficulty: medium
- Ex. 3 (p. 99) — delta method for the LD50 $=-\alpha/\beta$; compare with Figure 4.2 — difficulty: medium
- Ex. 4 (p. 99) — why normality of $p(\theta|y)$ and of $p(f(\theta)|y)$ are both valid limits — difficulty: medium
- Ex. 6 (p. 99) — mean, median and quantiles as Bayes estimates under squared, absolute and asymmetric linear loss — difficulty: medium
- Ex. 8 (p. 99) — work through the mother–daughter regression to the mean with sketches — difficulty: easy
- Ex. 15 (p. 100) — coverage of posterior intervals averaged over the prior versus at a fixed true value — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 93 = printed 83). All citations use printed pages.
- The text layer renders θ as ω and "−1" as "→1" in places, and parts of the equations are garbled. I checked all equations against the page images, which show θ throughout.
- The chapter's proofs are in Appendix B, which is not in this unit. Statements about asymptotic theory here are the chapter's own sketches.
- Section 4.6 lists many references; only the points relevant to this unit's content are noted. Page 97 contains the end of 4.5 and the start of 4.6.
