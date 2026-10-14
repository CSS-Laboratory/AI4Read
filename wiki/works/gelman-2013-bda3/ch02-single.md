---
id: gelman-2013-bda3/ch02-single
work: gelman-2013-bda3
unit: "Chapter 2 — Single-parameter models"
pages: 29–62
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Single-parameter models (BDA3, Chapter 2)

## L0 — One line
With one unknown parameter, conjugate priors (beta–binomial, normal–normal, gamma–Poisson, and others) give closed-form posteriors that act as a compromise between prior and data, and vague priors need careful handling.

## L1 — The gist (≤ 120 words)
How do we do Bayesian inference when only one scalar parameter is unknown? The chapter works through the binomial, normal, Poisson and exponential models. With conjugate priors the posterior stays in the prior's family, and the prior acts like extra data. In the normal model the posterior mean is a precision-weighted compromise between prior and data (precision = 1/variance). The cancer-rate example shows why small samples produce extreme raw rates and how an informative prior shrinks them. The chapter then asks how to choose priors: noninformative, improper, Jeffreys, and weakly informative. Its message is that conjugate models are good starting points, and that improper priors (those that do not integrate to 1) need checks.

**Prerequisites:** Bayes' rule and densities; beta, normal, gamma and Poisson distributions; completing the square; change of variables for densities; conditional mean and variance identities.

## L2 — Key ideas (5–10 bullets)
- With a uniform prior, binomial data give a Beta(y+1, n−y+1) posterior, so the predictive probability of success is (y+1)/(n+2), "Laplace's law of succession" (pp. 30–32).
- The prior mean equals the average of posterior means over possible data. The posterior variance is on average smaller than the prior variance, but not necessarily in a particular case (p. 32).
- Conjugacy means the posterior is in the prior's family. Beta, normal, scaled inverse-χ² and gamma priors can be read as prior pseudo-observations, and exponential families (densities of the form $f(y)g(\theta)e^{\phi(\theta)^Tu(y)}$) have natural conjugate priors, i.e. priors with the same functional form as the likelihood (pp. 34–37, 43–46).
- Normal known-variance model: posterior precision (precision = 1/variance) = prior precision + data precision, and the posterior mean is a precision-weighted average. The posterior predictive variance is σ² + τ₁² (pp. 40–42).
- Posterior inference can use exact summaries, simulation, normal approximation (better on the logit scale) or a grid. The placenta previa example shows all of these (pp. 37–39).
- Kidney-cancer maps show extreme rates concentrating in small counties. A gamma prior shrinks small counties strongly and large counties hardly at all (pp. 47–51).
- Noninformative priors (flat, 1/σ², Jeffreys' √J with $J$ the Fisher information, pivotal-quantity rules for location and scale) may be improper (not integrate to 1). A prior flat in one parameterization is not flat in another, whereas Jeffreys' rule is built to be invariant. Posterior propriety must be checked (pp. 51–54).
- Weakly informative priors are proper and deliberately weaker than real knowledge; the authors prefer them in most problems to trying to model complete ignorance (pp. 55–56).

## L3 — Walkthrough

Chapter intro (p. 29). The chapter treats four one-dimensional models (binomial, normal, Poisson, exponential) and introduces concepts and computing methods along the way. Estimand = the quantity being estimated.

### 2.1 Estimating a probability from binomial data (pp. 29–32)

**Model.** Data $y_1,\dots,y_n\in\{0,1\}$ are exchangeable (their joint distribution does not depend on order). They are summarized by $y$ = number of successes. Letting $\theta$ be the population proportion turns exchangeable trials into i.i.d. trials given $\theta$ (p. 29). $n$ is treated as fixed design.
$$p(y|\theta)=\mathrm{Bin}(y|n,\theta)=\binom{n}{y}\theta^y(1-\theta)^{n-y}.\tag{2.1}$$

**Example: probability of a female birth** (pp. 29–30). $\theta$ is the proportion of female births. The accepted value in large European-race populations is 0.485 (p. 29). The ratio $\phi=(1-\theta)/\theta$ is an alternative parameter. Binomial sampling assumes births are conditionally independent given $\theta$, which is motivated by exchangeability when there is no explanatory information, such as multiple births or births in the same family (p. 30).

**Uniform prior.** With a uniform prior on $[0,1]$, the factor $\binom ny$ is constant in $\theta$, so
$$p(\theta|y)\propto\theta^y(1-\theta)^{n-y},\tag{2.2}$$
$$\theta|y\sim\mathrm{Beta}(y+1,\,n-y+1).\tag{2.3}$$
Figure 2.1 plots (2.2) for four experiments with the same proportion of successes but different $n$ (5, 20, 100, 1000). The posterior narrows as $n$ grows (p. 30).

**Historical note (pp. 30–31).**
- Early work (Bernoulli's weak law of large numbers) answered the "pre-data" question: given $\theta$, what is the distribution of $y$? Bayes and Laplace independently get credit for inverting this, to give probability statements about $\theta$ given $y$.
- Bayes' billiard-table analogy: a ball W is thrown uniformly, and its horizontal position is $\theta$ (the prior). Ball O is thrown $n$ times, and $y$ counts landings to the right of W (the likelihood).
- Bayes obtained
$$\Pr(\theta\in(\theta_1,\theta_2)|y)=\frac{\Pr(\theta\in(\theta_1,\theta_2),y)}{p(y)}=\frac{\int_{\theta_1}^{\theta_2}p(y|\theta)p(\theta)d\theta}{p(y)}=\frac{\int_{\theta_1}^{\theta_2}\binom ny\theta^y(1-\theta)^{n-y}d\theta}{p(y)}.\tag{2.4}$$
- He evaluated the denominator:
$$p(y)=\int_0^1\binom ny\theta^y(1-\theta)^{n-y}d\theta=\frac1{n+1},\quad y=0,\dots,n.\tag{2.5}$$
So all values of $y$ are equally likely a priori.
- The numerator is an incomplete beta integral with no closed form for large $y$ and $n-y$, which apparently troubled Bayes.
- Laplace also used the uniform prior and expanded $\theta^y(1-\theta)^{n-y}$ around its maximum $\theta=y/n$, which is the normal approximation. His first serious application: 241,945 girls and 251,527 boys born in Paris, 1745–1770. He found $\Pr(\theta\ge0.5|y=241{,}945,\,n=251{,}527+241{,}945)\approx1.15\times10^{-42}$, so he was "morally certain" that $\theta<0.5$ (p. 31).

**Prediction (pp. 31–32).** The prior predictive under the uniform prior is (2.5). For one new exchangeable trial $\tilde y$:
$$\Pr(\tilde y=1|y)=\int_0^1\Pr(\tilde y=1|\theta,y)p(\theta|y)d\theta=\int_0^1\theta\,p(\theta|y)d\theta=E(\theta|y)=\frac{y+1}{n+2}.\tag{2.6}$$
The last step uses beta properties. This is "Laplace's law of succession". At $y=0$ and $y=n$ it predicts $\frac1{n+2}$ and $\frac{n+1}{n+2}$ (p. 32).

*Intuition note.* Compared with the improper Beta(0, 0) prior, the uniform prior is equivalent to one extra success and one extra failure (p. 53), which is why (2.6) gives $(y+1)/(n+2)$. (Under the $\alpha-1$, $\beta-1$ counting of p. 34, Beta(1, 1) itself counts as 0 prior successes and failures.) So a run of $n$ failures gives probability $1/(n+2)$, not exactly 0, for the next success.

### 2.2 Posterior as compromise between data and prior information (p. 32)
From (1.8) and (1.9) of Chapter 1, with $(\theta,y)$ in place of $(u,v)$:
$$E(\theta)=E(E(\theta|y)),\tag{2.7}$$
$$\mathrm{var}(\theta)=E(\mathrm{var}(\theta|y))+\mathrm{var}(E(\theta|y)).\tag{2.8}$$
- (2.7): the prior mean is the average of all possible posterior means over the distribution of possible data.
- (2.8): the posterior variance is on average smaller than the prior variance, by an amount depending on the variation of posterior means over possible data. This describes expectations only. In particular situations the posterior variance can be similar to or even larger than the prior variance, which can indicate conflict between sampling model and prior.
- Uniform-prior binomial: prior mean $\tfrac12$, prior variance $\tfrac1{12}$. The posterior mean $\frac{y+1}{n+2}$ is a compromise between the prior mean and $y/n$, with the prior mattering less as $n$ grows. This is a general feature of Bayesian inference.

### 2.3 Summarizing posterior inference (pp. 32–34)
- The posterior contains all current information about $\theta$. A graph is ideal. Simulation gives flexibility in summarizing, even after complicated transformations (pp. 32–33).
- Location summaries are the mean, median and mode. Spread summaries are the SD, the interquartile range and other quantiles. The mode is often easier to compute in complex problems. For Beta(y+1, n−y+1) the mean is $\frac{y+1}{n+2}$ and the mode is $y/n$, which is the maximum likelihood estimate and the (minimum variance) unbiased estimate (p. 33).
- **Central posterior interval** (100(1−α)%): exactly 100(α/2)% of posterior probability lies above and below it. It can be computed from CDFs or from posterior simulations (p. 33).
- **Highest posterior density (HPD) region**: the set containing 100(1−α)% of posterior probability whose density is never lower inside than outside. It equals the central interval for a unimodal symmetric posterior. The central interval is in common use because it is the α/2 and 1−α/2 quantiles and is easy to compute from simulations (p. 33).
- Figure 2.2: for a bimodal density, the 95% central interval includes a zero-density gap, while the HPD region is two disjoint intervals. The HPD region is more cumbersome but more informative, though it is probably better not to summarize such a density by a single interval. The two also differ substantially for highly skewed posteriors (pp. 33–34).

### 2.4 Informative prior distributions (pp. 34–39)

**Interpretations (p. 34).** In the *population* interpretation, the prior represents a population of parameter values from which the current $\theta$ was drawn. In the *state of knowledge* interpretation, we express our knowledge and uncertainty as if $\theta$ were a random draw from the prior. The prior should include all plausible values but need not be tightly concentrated, because data often outweigh any reasonable prior. Bayes' justification for the uniform prior appears to rest on the uniform prior predictive for $y$ (observable quantities). Laplace's rationale was less clear. Later interpretations ascribe to him the "principle of insufficient reason", whose weaknesses are discussed in 2.8 (p. 34).

**Beta prior.** The likelihood has the form $\theta^a(1-\theta)^b$. Take $p(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$, i.e. $\theta\sim\mathrm{Beta}(\alpha,\beta)$. This is like $\alpha-1$ prior successes and $\beta-1$ prior failures. $\alpha,\beta$ are *hyperparameters*. Two hyperparameters can be set by fixing, for example, mean and variance (pp. 34–35). Then
$$p(\theta|y)\propto\theta^{y}(1-\theta)^{n-y}\theta^{\alpha-1}(1-\theta)^{\beta-1}\propto\theta^{y+\alpha-1}(1-\theta)^{n-y+\beta-1}=\mathrm{Beta}(\theta|\alpha+y,\beta+n-y).$$
- Posterior mean: $E(\theta|y)=\frac{\alpha+y}{\alpha+\beta+n}$. It always lies between $y/n$ and the prior mean $\alpha/(\alpha+\beta)$ (Exercise 2.5b).
- Posterior variance: $\mathrm{var}(\theta|y)=\frac{(\alpha+y)(\beta+n-y)}{(\alpha+\beta+n)^2(\alpha+\beta+n+1)}=\frac{E(\theta|y)[1-E(\theta|y)]}{\alpha+\beta+n+1}$.
- As $y$ and $n-y$ grow with $\alpha,\beta$ fixed, $E(\theta|y)\approx y/n$ and $\mathrm{var}(\theta|y)\approx\frac1n\frac yn(1-\frac yn)$. This goes to zero at rate $1/n$, and in the limit the prior has no influence (p. 35).
- A Bayesian central limit theorem (Chapter 4) gives $\left(\frac{\theta-E(\theta|y)}{\sqrt{\mathrm{var}(\theta|y)}}\Big|y\right)\to N(0,1)$. For a proportion, the normal approximation is more accurate on the logit scale $\log(\theta/(1-\theta))$, which maps $[0,1]$ to $(-\infty,\infty)$ (p. 35).

**Conjugate priors (pp. 35–36).** If $\mathcal F$ is a class of sampling distributions and $\mathcal P$ a class of priors, then $\mathcal P$ is *conjugate* for $\mathcal F$ if
$$p(\theta|y)\in\mathcal P\ \text{ for all }p(\cdot|\theta)\in\mathcal F\text{ and }p(\cdot)\in\mathcal P.$$
This is formally vague, since the class of all distributions is always conjugate. The interest is in *natural* conjugate families: all densities with the same functional form as the likelihood. Advantages: computational convenience, and interpretation as additional data (p. 36).

**Nonconjugate priors (p. 36).** Reasons to use conjugate models: results are easy to understand and often analytic, they are often good approximations, they simplify computation, and they serve as building blocks. Mixtures of conjugate families can help (Exercise 2.4). Nonconjugate priors make interpretation less transparent and computation harder but "do not pose any new conceptual problems". In complicated models conjugacy may be impossible.

**Exponential families and sufficient statistics (pp. 36–37).** Readers unfamiliar with these concepts can skip. $\theta$ and $y_i$ may be multidimensional. $\mathcal F$ is an exponential family if
$$p(y_i|\theta)=f(y_i)g(\theta)e^{\phi(\theta)^Tu(y_i)}.$$
$\phi(\theta)$ is the "natural parameter". For i.i.d. $y=(y_1,\dots,y_n)$:
$$p(y|\theta)=\Big(\prod_i f(y_i)\Big)g(\theta)^n\exp\Big(\phi(\theta)^T\sum_i u(y_i)\Big)\propto g(\theta)^ne^{\phi(\theta)^Tt(y)},\quad t(y)=\sum_{i=1}^nu(y_i).$$
$t(y)$ is a *sufficient statistic*: the likelihood depends on $y$ only through $t(y)$. With prior $p(\theta)\propto g(\theta)^\eta e^{\phi(\theta)^T\nu}$,
$$p(\theta|y)\propto g(\theta)^{\eta+n}e^{\phi(\theta)^T(\nu+t(y))},$$
so this prior is conjugate. The text says it has been shown that, in general, exponential families are the only classes with natural conjugate priors, since, apart from certain irregular cases, the only distributions with a fixed number of sufficient statistics for all $n$ are of exponential type (p. 37). The binomial is an exponential family with natural parameter logit(θ) (left as an exercise).

**Example: placenta previa (pp. 37–39).** Of 980 births in a German study, 437 were female. The question is how much evidence this gives that the female proportion for placenta previa births is below 0.485.
- *Uniform prior.* The posterior is Beta(438, 544). Posterior mean 0.446, SD 0.016, median 0.446, central 95% interval [0.415, 0.477]. The normal approximation with that mean and SD matches the interval to three decimals (p. 37).
- *Simulation.* 1000 draws from Beta(438, 544): 95% interval from the 25th and 976th ordered draws is [0.415, 0.476]. Median 0.446, mean 0.445, SD 0.016. The normal-approximation interval is $0.445\pm1.96\cdot0.016=[0.414,0.476]$ (p. 37).
- *Logit scale.* Draws on the logit scale have mean −0.220 and SD 0.065. The interval $[-0.220\pm1.96\cdot0.065]$ inverted to the $\theta$ scale is [0.414, 0.477]. The logit improvement is most noticeable for small samples or $\theta$ near 0 or 1 (p. 37).
- *Sex ratio* $(1-\theta)/\theta$: posterior median 1.24, 95% interval [1.10, 1.41]. This is far above the usual European-race ratio of 1.06, implying a lower female birth probability under placenta previa than in the general population (p. 38; Figure 2.3).
- *Different conjugate priors* (Table 2.1, p. 38). $\alpha+\beta$ indexes prior information, and $\alpha+\beta-2$ is "in some sense" the number of prior observations.

| prior mean α/(α+β) | α+β | posterior median | 95% interval |
|---|---|---|---|
| 0.500 | 2 | 0.446 | [0.415, 0.477] |
| 0.485 | 2 | 0.446 | [0.415, 0.477] |
| 0.485 | 5 | 0.446 | [0.415, 0.477] |
| 0.485 | 10 | 0.446 | [0.415, 0.477] |
| 0.485 | 20 | 0.447 | [0.416, 0.478] |
| 0.485 | 100 | 0.450 | [0.420, 0.479] |
| 0.485 | 200 | 0.453 | [0.424, 0.481] |

Only for priors equivalent to 100 or 200 births are the intervals pulled noticeably toward the prior, and even then they still exclude the prior mean (p. 38).
- *Nonconjugate prior* (Fig. 2.4a). It is piecewise linear, centered at 0.485 and flat far away. 40% of its mass lies outside [0.385, 0.585]. Its mean is 0.493 and its SD 0.21, similar to a beta with $\alpha+\beta=5$. The unnormalized posterior is computed on the grid $\theta=0.000,0.001,\dots,1.000$ by multiplying prior by binomial likelihood. Normalizing on the grid gives 1000 draws. The posterior median is 0.448 and the 95% interval [0.419, 0.480], matching Table 2.1 because the data overwhelm the prior. It is important to avoid grids that are too coarse and distort a significant portion of the posterior mass (p. 39).

*Intuition note.* The prior's strength is indexed by $\alpha+\beta$ ($\alpha+\beta-2$ is, in some sense, the number of prior observations), and 980 real observations dwarf priors with $\alpha+\beta$ from 2 to 20. Only priors with information equivalent to 100 or 200 births pull the intervals noticeably toward the prior (p. 38).

### 2.5 Normal distribution with known variance (pp. 39–42)
Normal likelihood is justified by the CLT as an approximation, and is useful as a component of richer models (t, finite mixtures) (p. 39).

**One observation.** $p(y|\theta)=\frac1{\sqrt{2\pi}\sigma}e^{-\frac1{2\sigma^2}(y-\theta)^2}$, with $\sigma^2$ known. In $\theta$ the likelihood is the exponential of a quadratic, so the conjugate family is $p(\theta)=e^{A\theta^2+B\theta+C}$. Parameterize it as $\theta\sim N(\mu_0,\tau_0^2)$ with known hyperparameters (pp. 39–40).

**Posterior.** Treating everything but $\theta$ as constant,
$$p(\theta|y)\propto\exp\Big(-\tfrac12\Big(\tfrac{(y-\theta)^2}{\sigma^2}+\tfrac{(\theta-\mu_0)^2}{\tau_0^2}\Big)\Big).$$
Expanding, collecting terms and completing the square in $\theta$ (details in Exercise 2.14a) gives
$$p(\theta|y)\propto\exp\Big(-\tfrac1{2\tau_1^2}(\theta-\mu_1)^2\Big),\quad\theta|y\sim N(\mu_1,\tau_1^2),\tag{2.9}$$
$$\mu_1=\frac{\frac1{\tau_0^2}\mu_0+\frac1{\sigma^2}y}{\frac1{\tau_0^2}+\frac1{\sigma^2}},\qquad\frac1{\tau_1^2}=\frac1{\tau_0^2}+\frac1{\sigma^2}.\tag{2.10}$$

**Precision** = inverse variance. For normal data and normal prior (each with known precision), posterior precision = prior precision + data precision. The posterior mean is a precision-weighted average of $\mu_0$ and $y$. Equivalent forms (p. 40):
$$\mu_1=\mu_0+(y-\mu_0)\frac{\tau_0^2}{\sigma^2+\tau_0^2}\ \text{(prior adjusted toward }y),\qquad\mu_1=y-(y-\mu_0)\frac{\sigma^2}{\sigma^2+\tau_0^2}\ \text{(data shrunk toward prior mean)}.$$
Extremes as printed: $\mu_1=\mu_0$ if $y=\mu_0$ or $\tau_0^2=0$, and $\mu_1=y$ if $y=\mu_0$ or $\sigma^2=0$. If $\tau_0^2=0$, the prior is infinitely more precise than the data and the posterior equals the prior. If $\sigma^2=0$, the data are perfectly precise and the posterior is concentrated at $y$ (p. 40).

*Intuition note.* Each source of information is weighted by how precise it is. Adding precisions mirrors the fact that two independent noisy measurements are more informative together than either alone.

**Posterior predictive.** Since $\tilde y$ given $\theta$ does not depend on past data, $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta\propto\int\exp(-\frac1{2\sigma^2}(\tilde y-\theta)^2)\exp(-\frac1{2\tau_1^2}(\theta-\mu_1)^2)d\theta$. The integrand is the exponential of a quadratic in $(\tilde y,\theta)$, so they are jointly normal and $\tilde y$ is marginally normal (p. 41). Using $E(\tilde y|\theta)=\theta$, $\mathrm{var}(\tilde y|\theta)=\sigma^2$ and (2.7), (2.8):
$$E(\tilde y|y)=E(E(\tilde y|\theta,y)|y)=E(\theta|y)=\mu_1,$$
$$\mathrm{var}(\tilde y|y)=E(\mathrm{var}(\tilde y|\theta,y)|y)+\mathrm{var}(E(\tilde y|\theta,y)|y)=E(\sigma^2|y)+\mathrm{var}(\theta|y)=\sigma^2+\tau_1^2.$$
The predictive variance has two parts: model variance $\sigma^2$ and posterior uncertainty $\tau_1^2$ (p. 41).

**Multiple observations.** For i.i.d. $y=(y_1,\dots,y_n)$, $p(\theta|y)\propto\exp\big(-\tfrac12\big(\tfrac1{\tau_0^2}(\theta-\mu_0)^2+\tfrac1{\sigma^2}\sum_i(y_i-\theta)^2\big)\big)$. Algebra (Exercise 2.14b) shows the posterior depends on $y$ only through $\bar y$, a sufficient statistic. Since $\bar y|\theta,\sigma^2\sim N(\theta,\sigma^2/n)$, the single-observation results apply with $\bar y$ as the observation (p. 41):
$$p(\theta|y_1,\dots,y_n)=p(\theta|\bar y)=N(\theta|\mu_n,\tau_n^2),\tag{2.11}$$
$$\mu_n=\frac{\frac1{\tau_0^2}\mu_0+\frac n{\sigma^2}\bar y}{\frac1{\tau_0^2}+\frac n{\sigma^2}},\qquad\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2}.\tag{2.12}$$
The same result is obtained by adding data points one at a time, with each posterior as the next prior (Exercise 2.14c). Prior precision $1/\tau_0^2$ and data precision $n/\sigma^2$ play equivalent roles. If $\tau_0^2=\sigma^2$, the prior has the weight of one extra observation with value $\mu_0$. As $\tau_0\to\infty$ with $n$ fixed, or $n\to\infty$ with $\tau_0^2$ fixed,
$$p(\theta|y)\approx N(\theta|\bar y,\sigma^2/n),\tag{2.13}$$
which is a good approximation in practice whenever prior beliefs are relatively diffuse over the range of $\theta$ where the likelihood is substantial (p. 42).

### 2.6 Other standard single-parameter models (pp. 42–46)
Closed forms are the exception, because the normalizing constant $p(y)$ is often hard to compute. Such models can be unrealistic but are useful starting points (p. 42).

Motivations for the standard distributions (p. 42):
- Binomial: counting exchangeable outcomes.
- Normal: a sum of many exchangeable or independent terms. On the log scale it fits positive data that are products of many independent factors.
- Poisson (counts) and exponential (waiting times): events occurring exchangeably in all time intervals, i.e. independently in time with a constant rate.

Realistic models are built by combining these.

**Normal, known mean, unknown variance** (pp. 42–43). Likelihood for $n$ i.i.d. observations:
$$p(y|\sigma^2)\propto\sigma^{-n}\exp\Big(-\frac1{2\sigma^2}\sum(y_i-\theta)^2\Big)=(\sigma^2)^{-n/2}\exp\Big(-\frac n{2\sigma^2}v\Big),\quad v=\frac1n\sum(y_i-\theta)^2,$$
with $v$ the sufficient statistic. The conjugate prior is inverse-gamma, $p(\sigma^2)\propto(\sigma^2)^{-(\alpha+1)}e^{-\beta/\sigma^2}$. A convenient parameterization is the scaled inverse-χ²: $\sigma^2\sim\text{Inv-}\chi^2(\nu_0,\sigma_0^2)$ means $\sigma^2$ is distributed as $\sigma_0^2\nu_0/X$ with $X\sim\chi^2_{\nu_0}$. Posterior:
$$p(\sigma^2|y)\propto\Big(\frac{\sigma_0^2}{\sigma^2}\Big)^{\nu_0/2+1}\exp\Big(-\frac{\nu_0\sigma_0^2}{2\sigma^2}\Big)(\sigma^2)^{-n/2}\exp\Big(-\frac{nv}{2\sigma^2}\Big)\propto(\sigma^2)^{-((n+\nu_0)/2+1)}\exp\Big(-\frac{\nu_0\sigma_0^2+nv}{2\sigma^2}\Big),$$
$$\sigma^2|y\sim\text{Inv-}\chi^2\Big(\nu_0+n,\ \frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\Big).$$
The scale is the degrees-of-freedom-weighted average of prior and data scales, and the degrees of freedom add. The prior is equivalent to $\nu_0$ observations with average squared deviation $\sigma_0^2$ (p. 43).

**Poisson** (pp. 43–44). $p(y|\theta)=\theta^ye^{-\theta}/y!$. For i.i.d. data, $p(y|\theta)\propto\theta^{t(y)}e^{-n\theta}$ with $t(y)=\sum y_i$. In exponential-family form, $p(y|\theta)\propto e^{-n\theta}e^{t(y)\log\theta}$, so the natural parameter is $\log\theta$. The conjugate prior $p(\theta)\propto e^{-\beta\theta}\theta^{\alpha-1}$ is Gamma(α, β), equivalent in some sense to a total count of $\alpha-1$ in $\beta$ prior observations. Posterior: $\theta|y\sim\mathrm{Gamma}(\alpha+n\bar y,\beta+n)$ (p. 44).

**Negative binomial** (p. 44). With conjugacy, $p(y)=p(y|\theta)p(\theta)/p(\theta|y)$. For one Poisson observation:
$$p(y)=\frac{\mathrm{Poisson}(y|\theta)\mathrm{Gamma}(\theta|\alpha,\beta)}{\mathrm{Gamma}(\theta|\alpha+y,1+\beta)}=\frac{\Gamma(\alpha+y)\beta^\alpha}{\Gamma(\alpha)y!(1+\beta)^{\alpha+y}}=\binom{\alpha+y-1}{y}\Big(\frac\beta{\beta+1}\Big)^\alpha\Big(\frac1{\beta+1}\Big)^y.$$
This is the negative binomial, $y\sim\text{Neg-bin}(\alpha,\beta)$. It is a gamma mixture of Poissons: $\text{Neg-bin}(y|\alpha,\beta)=\int\mathrm{Poisson}(y|\theta)\mathrm{Gamma}(\theta|\alpha,\beta)d\theta$.

**Rate and exposure** (pp. 44–45). $y_i\sim\mathrm{Poisson}(x_i\theta)$, with known positive exposures $x_i$ (2.14). The model is not exchangeable in the $y_i$ but is exchangeable in pairs $(x,y)_i$. The likelihood is $\propto\theta^{\sum y_i}e^{-(\sum x_i)\theta}$, so with prior Gamma(α, β):
$$\theta|y\sim\mathrm{Gamma}\Big(\alpha+\sum y_i,\ \beta+\sum x_i\Big).\tag{2.15}$$

**Example: asthma mortality** (p. 45). 3 deaths in a city of 200,000 in one year give a crude rate of 1.5 per 100,000. The model is $y\sim\mathrm{Poisson}(2.0\theta)$ with $\theta$ in cases per 100,000 per year, so $y=3$ and $x=2.0$. Reviews suggest rates above 1.5 per 100,000 are rare in Western countries and the typical rate is about 0.6. By trial and error, Gamma(3.0, 5.0) is a plausible prior (assuming exchangeability across cities and years). Its mean is 0.6 and mode 0.4, and 97.5% of its mass lies below 1.44. Specifying the mean sets the ratio of the gamma parameters, and the shape is then tuned to the tail.
- Posterior: Gamma(6.0, 7.0), mean 0.86, so substantial shrinkage toward the prior. $\Pr(\theta>1.0)=0.30$.
- With 30 deaths in 10 years (same rate, constant population): Gamma(33.0, 25.0), mean 1.32, $\Pr(\theta>1.0)=0.93$. The posterior is much more concentrated and still lies between prior and data.

**Exponential** (p. 46). $p(y|\theta)=\theta\exp(-y\theta)$ for $y>0$, with rate $\theta=1/E(y|\theta)$. It is the gamma with $(\alpha,\beta)=(1,\theta)$, used here as a sampling distribution. Memoryless: $\Pr(y>t+s|y>s,\theta)=\Pr(y>t|\theta)$, a natural property for lifetime data. The conjugate prior is Gamma(α, β), with posterior Gamma(α+1, β+y) for one observation. For $n$ observations, $p(y|\theta)=\theta^n\exp(-n\bar y\theta)$, which as a likelihood is proportional to Gamma(n+1, nȳ). So a Gamma(α, β) prior is like $\alpha-1$ exponential observations with total waiting time $\beta$ (Exercise 2.19).

### 2.7 Example: informative prior for cancer rates (pp. 46–51)
This example uses many inferences with a common prior, and introduces hierarchical modeling (Chapter 5) (p. 46).

**Puzzling maps** (pp. 47–48). Figure 2.6 shows counties with the highest 10% kidney cancer death rates (white males, 1980–1989, age-adjusted). Many are in the Great Plains. Proposed explanations include pollution, late detection and diet. These are not needed, because Figure 2.7 (the lowest 10%) is also mostly in the middle of the country. The issue is sample size. A county of 1000 people will probably have zero deaths in ten years (lowest rate), but one death gives 1 per 10,000 per year, which is in the top 10%. The Great Plains has many low-population counties, so it is overrepresented in both maps. The maps give no evidence of especially high rates there (p. 48).

**Model** (p. 48). For county $j$:
$$y_j\sim\mathrm{Poisson}(10n_j\theta_j),\tag{2.16}$$
where $y_j$ is the number of deaths 1980–1989, $n_j$ the population, and $\theta_j$ the rate in deaths per person per year. The maps plot the raw rate $y_j/(10n_j)$. Age-standardization is ignored. This differs from (2.14) because $\theta_j$ varies by county, so (2.16) is a separate model for each county. A prior Gamma(α=20, β=430,000) has mean $\alpha/\beta=4.65\times10^{-5}$ and SD $\sqrt\alpha/\beta=1.04\times10^{-5}$. It is justified later in the section. Posterior:
$$\theta_j|y_j\sim\mathrm{Gamma}(20+y_j,\ 430{,}000+10n_j),$$
$$E(\theta_j|y_j)=\frac{20+y_j}{430{,}000+10n_j},\qquad\mathrm{var}(\theta_j|y_j)=\frac{20+y_j}{(430{,}000+10n_j)^2}.$$
The posterior mean is a weighted average of the raw rate and the prior mean (p. 48).

**Small county, $n_j=1000$** (pp. 48–49). The posterior mean is $\frac{20+y_j}{440{,}000}$:
- $y_j=0$: raw rate 0, posterior mean $4.55\times10^{-5}$.
- $y_j=1$: raw rate $10^{-4}$ (about twice the national mean), posterior mean $4.77\times10^{-5}$.
- $y_j=2$: raw rate $2\times10^{-4}$, posterior mean $5.00\times10^{-5}$.

The data are dominated by the prior. The predictive distribution is $y_j\sim\text{Neg-bin}(\alpha,\frac\beta{10n_j})$. By simulation (draw 500 $\theta_j$ from Gamma(20, 430,000), then $y_j\sim\mathrm{Poisson}(10{,}000\theta_j)$), there were 319 zeros, 141 ones, 33 twos and 5 threes (p. 49).

**Large county, $n_j=10^6$** (p. 49). Simulating 500 values from Poisson($10^7\theta_j$) gives a median of 473 deaths and a 50% interval [393, 545]. The raw rate is as likely as not to fall in $[3.93,5.45]\times10^{-5}$. If $y_j=393$, the posterior mean is $\frac{20+393}{10^7+430{,}000}=3.96\times10^{-5}$. If $y_j=545$, it is $5.41\times10^{-5}$. The data dominate.

**Comparing counties** (pp. 49–50). The variance of $y_j/(10n_j)$ is inversely proportional to $n_j$, which acts as a sample size. Figure 2.8: all extreme raw rates are in low-population counties. Figure 2.9a: the Bayes-estimated rates are much less variable. Figure 2.9b: smaller counties have wider 50% posterior intervals.

**Constructing the prior** (pp. 50–51). Under the model, $y_j$ has the negative binomial predictive, with
$$E(y_j)=10n_j\frac\alpha\beta,\qquad\mathrm{var}(y_j)=10n_j\frac\alpha\beta+(10n_j)^2\frac\alpha{\beta^2}.\tag{2.17}$$
These also follow from (1.8) and (1.9) (Exercise 2.6). For the rates:
$$E\Big(\frac{y_j}{10n_j}\Big)=\frac\alpha\beta,\qquad\mathrm{var}\Big(\frac{y_j}{10n_j}\Big)=\frac1{10n_j}\frac\alpha\beta+\frac\alpha{\beta^2}.\tag{2.18}$$
After age-adjustment, the sample mean of the rates is set equal to $\alpha/\beta$. The sample variance of the rates is set equal to $E(\frac1{10n_j})\frac\alpha\beta+\frac\alpha{\beta^2}$, using the sample average of $\frac1{10n_j}$ in place of the expectation. This yields Gamma(20, 430,000). The authors see it as an approximation to the hierarchical approach of Chapter 5, in which $\alpha,\beta$ are unknowns to be estimated. Figure 2.10: the raw rates are much broader than the prior, since they include Poisson variability as well as between-county variation. Moment matching is "somewhat sloppy" and hard to apply in general. A more important improvement would be county-level predictors (hierarchical Poisson regression, Chapter 16) (p. 51).

*Intuition note.* A rare-event rate from a small population is mostly noise, so the extremes appear there. The prior acts like roughly 430,000 person-years of earlier information per county, which dominates when a county supplies only 10,000 person-years but is small when it supplies 10 million.

### 2.8 Noninformative prior distributions (pp. 51–54)
Priors with no population basis are hard to construct. "Reference", vague, flat, diffuse or *noninformative* priors are meant to play a minimal role. The rationale is often said to be to "let the data speak for themselves". A *weakly informative* prior holds enough information to "regularize" the posterior, keeping it within reasonable bounds, without capturing all scientific knowledge (p. 51).

**Proper and improper priors** (pp. 51–52). In the normal-mean model, if the prior precision $1/\tau_0^2$ is small relative to the data precision $n/\sigma^2$, then $p(\theta|y)\approx N(\theta|\bar y,\sigma^2/n)$. This is as if $p(\theta)\propto$ constant on $(-\infty,\infty)$, which integrates to infinity and is *improper*. A prior is *proper* if it does not depend on data and integrates to 1. A positive finite integral is an unnormalized density that can be renormalized. Here the posterior is proper given at least one data point. Second example: in the known-mean normal model, if $\nu_0$ is small relative to $n$, then $p(\sigma^2|y)\approx\text{Inv-}\chi^2(\sigma^2|n,v)$, as if $\nu_0=0$. This also follows from the improper prior $p(\sigma^2)\propto1/\sigma^2$.

**Improper prior, proper posterior** (p. 52). We can still define the unnormalized posterior $p(\theta|y)\propto p(y|\theta)p(\theta)$. In the above examples "(but not always!)" $\int p(\theta|y)d\theta$ is finite for all $y$. Such posteriors must be interpreted with great care: always check that the integral is finite and the form sensible. Their most reasonable interpretation is as approximations where the likelihood dominates the prior (Chapter 4).

**Jeffreys' invariance principle** (pp. 52–53). For a one-to-one transformation $\phi=h(\theta)$, the equivalent prior is
$$p(\phi)=p(\theta)\Big|\frac{d\theta}{d\phi}\Big|=p(\theta)|h'(\theta)|^{-1}.\tag{2.19}$$
Principle: any rule for determining $p(\theta)$ should give an equivalent result when applied to the transformed parameter. That is, $p(\phi)$ computed via (2.19) should match $p(\phi)$ determined directly from the transformed model. This leads to $p(\theta)\propto[J(\theta)]^{1/2}$, with Fisher information
$$J(\theta)=E\Big(\Big(\frac{d\log p(y|\theta)}{d\theta}\Big)^2\Big|\theta\Big)=-E\Big(\frac{d^2\log p(y|\theta)}{d\theta^2}\Big|\theta\Big).\tag{2.20}$$
Invariance check (p. 53), evaluating at $\theta=h^{-1}(\phi)$:
$$J(\phi)=-E\Big(\frac{d^2\log p(y|\phi)}{d\phi^2}\Big)=-E\Big(\frac{d^2\log p(y|\theta=h^{-1}(\phi))}{d\theta^2}\Big|\frac{d\theta}{d\phi}\Big|^2\Big)=J(\theta)\Big|\frac{d\theta}{d\phi}\Big|^2,$$
so $J(\phi)^{1/2}=J(\theta)^{1/2}|d\theta/d\phi|$, as required. (Added step: the second equality as printed drops a term in $\frac{d^2\theta}{d\phi^2}$ that multiplies the score, which has expectation zero; the text does not discuss this.) The principle extends to multiparameter models, but results are more controversial. Independent noninformative priors on components can differ from Jeffreys' result. With many parameters the authors prefer hierarchical models (Chapter 5).

**Binomial** (p. 53). $\log p(y|\theta)=\text{const}+y\log\theta+(n-y)\log(1-\theta)$, and substituting $E(y|\theta)=n\theta$ gives $J(\theta)=\frac n{\theta(1-\theta)}$. Jeffreys' prior is $p(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}$, i.e. Beta(½, ½). Alternatives: Bayes–Laplace Beta(1, 1), and the prior uniform in logit(θ), $p(\mathrm{logit}(\theta))\propto$ constant (Exercise 2.7), which corresponds to the improper Beta(0, 0). Going from Beta(0, 0) to Beta(1, 1) equals one more success and one more failure, which is usually a small fraction of the data. But with Beta(0, 0), if $y=0$ or $n$ the posterior is improper.

**Pivotal quantities** (pp. 53–54). For location and scale parameters "all principles seem to agree".
1. *Location.* If $p(y-\theta|\theta)=f(u)$ with $u=y-\theta$, free of $\theta$ and $y$, then $y-\theta$ is pivotal and $\theta$ is a pure location parameter. Requiring $y-\theta$ to keep distribution $f$ under the posterior, with $p(y-\theta|y)\propto p(\theta)p(y-\theta|\theta)$, implies $p(\theta)\propto$ constant on $(-\infty,\infty)$.
2. *Scale.* If $p(\frac y\theta|\theta)=g(u)$ with $u=y/\theta$, then $\theta$ is a pure scale parameter. By change of variables, $p(y|\theta)=\frac1\theta p(u|\theta)$ and $p(\theta|y)=\frac y{\theta^2}p(u|y)$. Setting both $p(u|\theta)$ and $p(u|y)$ equal to $g(u)$ gives $p(\theta|y)=\frac y\theta p(y|\theta)$. So the reference prior is $p(\theta)\propto1/\theta$, equivalently $p(\log\theta)\propto1$ or $p(\theta^2)\propto1/\theta^2$.

The sampling distribution of the pivot is used as its posterior distribution. This can be applied to sufficient statistics in more complicated examples such as hierarchical normal models. Even these principles can mislead: the uniform prior on the log of a hierarchical variance parameter does not work (Section 5.4) (p. 54).

**Difficulties** (p. 54).
1. Searching for an always-vague prior seems misguided. If the likelihood dominates, the choice among flat priors cannot matter, and a fixed reference prior encourages automatic, possibly inappropriate, use.
2. Flat in one parameterization is not flat in another. This is the essential difficulty with Laplace's principle of insufficient reason: on what scale should it apply? Example: uniform for the normal mean $\theta$ and $p(\sigma^2)\propto1/\sigma^2$ both seem reasonable. For $\phi=\log\sigma^2$, $p(\phi)=p(\sigma^2)|d\sigma^2/d\phi|\propto\frac1{\sigma^2}\sigma^2=1$, i.e. uniform on $\log\sigma^2$. Discrete cases have the analogous problem of dividing outcomes into equal-probability "atoms".
3. Averaging over competing models with improper priors is difficult (Section 7.3).

Even so, noninformative priors are often useful when quantifying real prior knowledge is not worth the effort, provided one checks that the posterior is proper and checks sensitivity to modelling assumptions of convenience.

### 2.9 Weakly informative prior distributions (pp. 55–56)
A weakly informative prior is proper but intentionally weaker than the actual prior knowledge available. Natural constraints often allow one. For log or logistic regression with binary or unit-SD predictors, effect sizes are less than 10 in most applications: a difference of 10 on the log scale multiplies the expected value by $\exp(10)=20{,}000$, and on the logit scale shifts a probability from $\mathrm{logit}^{-1}(-5)=0.01$ to $\mathrm{logit}^{-1}(5)=0.99$ (p. 55). Examples: for the sex-ratio problem, a prior concentrated between 0.4 and 0.6, such as a normal with mean 0.5 and SD 0.1, or the conjugate Beta(20, 20), which puts 80% of its mass between 0.4 and 0.6 (footnote, p. 55). For a normal mean, $N(0,A^2)$ with $A$ large depending on context.

Data analysts nearly always have more information than the model includes, for both likelihood and prior. Reasons for compromise include convenience, difficulty of expressing knowledge probabilistically, simplifying computation, and avoiding an unreliable source. Except for the last, these are arguments for convenience, justified if the answer would not change much. If so few data are available that the choice of noninformative prior matters, relevant information should go into the prior, perhaps via a hierarchical model (p. 55).

**Constructing one** (pp. 55–56). One might argue that virtually all statistical models are weakly informative, since a model always conveys some information, but it is not possible or perhaps even desirable to encode all of one's prior beliefs. Two routes: (i) start from a noninformative prior and add enough information to make inferences reasonable; (ii) start from a strong prior and broaden it for uncertainty about prior beliefs and applicability to new data. Neither is pure. A U(0, 1) prior on a rare-disease probability can be too strong. With $y=0$ cases in $n=100$ and the true prevalence known to be below 1 in 10,000, the probability is grossly overestimated, and a suitable weakly informative prior would concentrate the posterior in the low range. A believed-strong prior may be too weak along some direction. This does not mean priors should be tightened whenever posteriors are vague, since often the best strategy is to acknowledge the posterior uncertainty (p. 56).

**Fairness and symmetry** (p. 56). Sometimes it is recommended not to use relevant information, expressed as a symmetry principle that the prior should not pull inferences in a predetermined direction. Example: a scientist fairly sure an effect is positive has a $N(0.5,0.5)$ prior. This may be reasonable but seems risky when analysing an experiment designed to test her theory. One might prefer a prior that leans against her hypothesis. Such concerns should ultimately be subsumed into decision analysis and a model of the whole scientific process. Meanwhile, requiring constraints such as symmetry about 0 for a single treatment effect's prior can make sense.

### 2.10 Bibliographic note (pp. 56–57)
Not digested in detail. It credits Stigler (1986) for the historical accounts, Raiffa and Schlaifer (1961) for conjugate theory, and various works on noninformative priors. It says the placenta previa data come from a 1922 study reported in James (1987), and that the cancer example is adapted from Manton et al. (1989) (p. 57).

### 2.11 Exercises (pp. 57–62)
Twenty-two exercises. See "Exercises worth doing".

## Toy example (ours)
**Beta–binomial.** Prior $\theta\sim\mathrm{Beta}(2,2)$: pseudo-counts $\alpha-1=1$ success and $\beta-1=1$ failure. Data: $n=4$, $y=3$, so $y/n=0.75$.
- Posterior: Beta(2+3, 2+4−3) = Beta(5, 3).
- Mean: $5/8=0.625$. Check as a weighted average: prior mean 0.5 with weight $\frac{\alpha+\beta}{\alpha+\beta+n}=\frac48$, sample proportion 0.75 with weight $\frac48$. Then $0.5\cdot0.5+0.5\cdot0.75=0.25+0.375=0.625$. ✓. It lies between 0.5 and 0.75.
- Variance: $\frac{5\cdot3}{8^2\cdot9}=\frac{15}{576}\approx0.0260$. The prior variance is $\frac{2\cdot2}{4^2\cdot5}=0.05$, so here it shrank.
- Probability the next trial is a success: $E(\theta|y)=0.625$ (same argument as (2.6), with Beta(5, 3) in place of the uniform-prior posterior).

**Normal–normal.** Take $\sigma^2=1$, $\mu_0=0$, $\tau_0^2=4$, one observation $y=2$.
- Precisions: prior 0.25, data 1, posterior 1.25, so $\tau_1^2=0.8$.
- $\mu_1=\frac{0.25\cdot0+1\cdot2}{1.25}=1.6$. Check with the adjusted form: $0+2\cdot\frac4{1+4}=1.6$ ✓.
- Posterior predictive: mean 1.6, variance $\sigma^2+\tau_1^2=1.8$.

## Concepts
- [[conjugate-prior]] — a prior family whose posterior stays in the same family; "natural" ones copy the likelihood's functional form (pp. 35–36)
- [[prior-distribution]] — read either as a population of parameter values or as a state of knowledge (p. 34)
- [[posterior-distribution]] — all current information about the parameter; compromise between prior and data (pp. 32–33)
- [[likelihood]] — as a function of θ, e.g. $\theta^a(1-\theta)^b$ in the binomial case (p. 34)
- [[posterior-predictive-distribution]] — $p(\tilde y|y)=\int p(\tilde y|\theta)p(\theta|y)d\theta$; normal case has variance $\sigma^2+\tau_1^2$ (pp. 32, 41)
- [[exchangeability]] — trial order irrelevant, so data reduce to counts; i.i.d. given θ (p. 29)
- [[credible-interval]] — here the central posterior interval, with α/2 posterior probability in each tail (p. 33)
- [[highest-posterior-density-region]] (new) — set with 100(1−α)% mass and density never lower inside than outside (p. 33)
- [[partial-pooling-shrinkage]] — gamma prior pulls small-county raw rates toward the prior mean (pp. 45, 48–49)
- [[hierarchical-model]] — only previewed: α, β treated as unknowns (Chapter 5) (pp. 46, 50)
- [[principle-of-indifference-max-entropy]] — Laplace's "insufficient reason"; its weakness is parameterization dependence (pp. 34, 54)
- [[precision]] (new) — inverse variance; posterior precision = prior + data precision in the normal model (p. 40)
- [[sufficient-statistic]] (new) — $t(y)$ such that the likelihood depends on data only through $t(y)$ (p. 36)
- [[exponential-family]] (new) — densities $f(y)g(\theta)e^{\phi(\theta)^Tu(y)}$; these have natural conjugate priors (pp. 36–37)
- [[improper-prior]] (new) — prior with infinite integral; may still give a proper posterior, which must be checked (p. 52)
- [[jeffreys-prior]] (new) — $p(\theta)\propto J(\theta)^{1/2}$, invariant to reparameterization (pp. 52–53)
- [[pivotal-quantity]] (new) — a function of $y$ and θ with θ-free distribution, e.g. $y-\theta$ or $y/\theta$ (p. 53)
- [[weakly-informative-prior]] (new) — proper prior intentionally weaker than real knowledge, to regularize (pp. 51, 55)
- [[negative-binomial-mixture]] (new) — gamma mixture of Poissons; prior predictive of the gamma–Poisson model (p. 44)
- [[grid-approximation]] (new) — evaluate the unnormalized posterior on a grid and normalize (pp. 38–39)
- [[marginal-likelihood]] — computed as $p(y)=p(y|\theta)p(\theta)/p(\theta|y)$ under conjugacy (p. 44)
- [[sequential-updating]] — the same posterior results from adding data one point at a time (p. 42)

## Canonical instances
- [[bayes-billiard-table]] (new) — Bayes' uniform-prior construction of the binomial problem; $p(y)=1/(n+1)$ (p. 31)
- [[laplace-paris-births]] (new) — 241,945 girls vs 251,527 boys gives $\Pr(\theta\ge0.5|y)\approx1.15\times10^{-42}$ (p. 31)
- [[placenta-previa-sex-ratio]] (new) — 437 girls of 980 births; Beta(438, 544); prior sensitivity table (pp. 37–38)
- [[asthma-mortality-poisson]] (new) — Gamma(3.0, 5.0) prior, y=3, x=2.0 gives Gamma(6.0, 7.0) (p. 45)
- [[kidney-cancer-county-maps]] (new) — extreme raw rates in small counties; Gamma(20, 430,000) shrinkage (pp. 47–51)

## Bridges (candidates)
- [structural-analogy] Conjugate pseudo-observations (prior = α−1 successes, β−1 failures) ↔ regularization: a prior acts like extra data pulling estimates toward a default.
- [structural-analogy] Precision-weighted posterior mean ↔ inverse-variance weighting of independent noisy measurements.
- [structural-analogy] Small-county extremes ↔ small-sample noise in rankings generally: extreme values concentrate where the sample size is small.
- [same-math] Fisher information $J(\theta)$ in Jeffreys' prior ↔ frequentist asymptotics: the same quantity as in (2.20).
- [metaphor] Weakly informative prior as "regularization" ↔ penalized estimation: shared intent of keeping estimates in a sensible range.

## Questions this raises
- When hyperparameters like α, β are estimated from the same data (as in the cancer example), how should the uncertainty in them be handled? (The chapter defers this to hierarchical models, Chapter 5.)
- How much can an improper prior be trusted when the likelihood does not clearly dominate, and what checks establish a proper posterior?
- Which scale should a "noninformative" prior be flat on when Jeffreys, logit-uniform and uniform priors differ?
- How can a prior be set responsibly in multiparameter problems, where Jeffreys' principle is "more controversial"?

## Exercises worth doing
- Ex. 2.5 (p. 58) — posterior mean lies between prior mean and sample proportion; posterior variance versus prior variance with a uniform prior, and a counterexample with a beta prior — difficulty: medium
- Ex. 2.8 (p. 58) — normal posterior and posterior predictive for weights as functions of $n$, with intervals at $n=10$ and $n=100$ — difficulty: easy
- Ex. 2.11 (p. 59) — grid approximation and simulation for a nonconjugate Cauchy-location model — difficulty: medium
- Ex. 2.14 (p. 60) — fill in the algebra of (2.9)–(2.12) and show sequential updating gives the same result — difficulty: medium
- Ex. 2.20 (p. 61) — censored versus exact exponential data; why the posterior variance can rise with more information without contradicting (2.8) — difficulty: hard
- Ex. 2.21 (p. 61) — binomial–beta shrinkage of state-level proportions, following the Section 2.7 procedure — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 10.
- The text layer renders θ as ω and many symbols (→ for −, ! for ∫) in garbled form. I used θ and the symbols shown in the page images.
- Page images were supplied only for pdf 39–64 and 67–71 pages, not for pdf 65–66 (printed 55–56) and 72 (printed 62). For 55–56 I relied on the text layer. There the text layer prints the weakly informative normal prior as "N(0.5, 0.12)", which I read as $N(0.5,0.1^2)$ (superscript lost). This is my reading, not visible in an image.
- Page 40 prints "μ₁ = μ₀ if y = μ₀ or τ₀² = 0"; the first condition is a coincidence case that the author's accompanying sentence also explains. I reproduced it as printed.
- Section 2.4's "Nonconjugate" paragraph refers to "Section 2.4" for nonconjugate computation; this is the placenta previa example on pp. 38–39.
- Section 2.10 and the exercise text are only summarized.
