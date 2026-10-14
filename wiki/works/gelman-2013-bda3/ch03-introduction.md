---
id: gelman-2013-bda3/ch03-introduction
work: gelman-2013-bda3
unit: "3 Introduction to multiparameter models"
pages: 63–82
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Introduction to multiparameter models (BDA3, ch. 3)

## L0 — One line
With several unknowns, get the joint posterior of all of them, then integrate out (or ignore, in simulation) the nuisance parameters. In practice: draw the nuisance parameter from its marginal posterior, then the parameter of interest from its conditional posterior.

## L1 — The gist (≤ 120 words)
How do we do Bayesian inference when a model has several unknowns but we care about only some? The chapter's answer: build the joint posterior, then average over the nuisance parameters, usually by marginal-then-conditional simulation. It works this out in closed form for the normal model with unknown mean and variance (noninformative and conjugate priors), for the multinomial–Dirichlet model, and for the multivariate normal. For models without closed forms, it shows grid computation on a two-parameter logistic bioassay. It ends with a five-step recipe for simple Bayesian computation. This matters because most real models have more than one parameter.

**Prerequisites:** Bayes' rule; conjugate priors from Ch. 2 (normal with known variance, beta–binomial); marginal and conditional densities; basic matrix notation (inverse, determinant, trace); the idea of drawing random samples.

## L2 — Key ideas (5–10 bullets)
- The marginal posterior of the parameter of interest is a mixture of conditional posteriors, weighted by the posterior of the nuisance parameter, $p(\theta_1|y)=\int p(\theta_1|\theta_2,y)p(\theta_2|y)\,d\theta_2$. This justifies "draw $\theta_2$, then $\theta_1$" simulation (pp. 63–64).
- Normal data, prior uniform on $(\mu,\log\sigma)$: $\sigma^2|y\sim\text{Inv-}\chi^2(n-1,s^2)$, $\mu|\sigma^2,y\sim N(\bar y,\sigma^2/n)$, and marginally $\mu$ has a $t_{n-1}$ posterior. Its pivotal quantity matches the sampling-theory $t$ (pp. 64–66).
- The conjugate prior for the normal with unknown $(\mu,\sigma^2)$ is normal-inverse-$\chi^2$. The posterior updates $(\mu_0,\kappa_0,\nu_0,\sigma_0^2)$ to $(\mu_n,\kappa_n,\nu_n,\sigma_n^2)$ by weighted averages and added sums of squares (pp. 67–69).
- Multinomial data with a Dirichlet prior give a Dirichlet posterior with parameters $\alpha_j+y_j$. Functions such as $\theta_1-\theta_2$ are simpler to study by drawing simulations than by integration, as in the 1988 poll (pp. 69–70).
- The multivariate normal results parallel the univariate ones: precisions add, the posterior mean is precision-weighted, and the inverse-Wishart plays the role of the scaled inverse-$\chi^2$. Several noninformative priors are discussed (pp. 70–74).
- For a nonconjugate two-parameter model (logistic bioassay), posterior simulation from a grid works. Any function of the draws, such as the LD50, can then be summarized directly (pp. 74–77).
- The posterior mean is not always a good summary: the LD50 is meaningless when $\beta\le0$, so it is reported conditional on $\beta>0$ (pp. 77–78).
- A five-step strategy (likelihood, posterior, crude estimate, simulate, predictive simulation) summarizes the chapter and foreshadows Part III (p. 78).

## L3 — Walkthrough

### Chapter introduction (p. 63)
Most problems have several unknowns, but conclusions are often drawn about one or a few. The aim is then the marginal posterior of those parameters. In principle: get the joint posterior of all unknowns and integrate out the rest. Equivalently, in simulation: draw from the joint posterior and ignore the other unknowns (p. 63). Parameters needed for a realistic model but not of interest are **nuisance parameters**, for example the scale of random errors in a measurement problem (p. 63).

### 3.1 Averaging over 'nuisance parameters' (pp. 63–64)
Let $\theta=(\theta_1,\theta_2)$ (each may be a vector), with interest in $\theta_1$. Example: $y|\mu,\sigma^2\sim N(\mu,\sigma^2)$, with $\mu=\theta_1$ and $\sigma^2=\theta_2$ (p. 63). The joint posterior is
$$p(\theta_1,\theta_2|y)\propto p(y|\theta_1,\theta_2)\,p(\theta_1,\theta_2),$$
and averaging over $\theta_2$ gives $p(\theta_1|y)=\int p(\theta_1,\theta_2|y)\,d\theta_2$ (p. 63). Factoring the joint posterior gives
$$p(\theta_1|y)=\int p(\theta_1|\theta_2,y)\,p(\theta_2|y)\,d\theta_2. \tag{3.1}$$
- So $p(\theta_1|y)$ is a **mixture** of conditional posteriors given $\theta_2$, with $p(\theta_2|y)$ as weights. The weights combine evidence from data and prior (p. 64).
- $\theta_2$ may include a discrete component representing different sub-models (p. 64).
- The integral is rarely evaluated explicitly. Instead, draw $\theta_2$ from its marginal posterior, then $\theta_1$ from its conditional posterior given the drawn $\theta_2$. This does the integration indirectly (p. 64).

*Intuition note:* Each possible value of the nuisance parameter gives its own answer for the parameter of interest. The final answer averages those answers, weighting each by how plausible that nuisance value is after seeing the data.

### 3.2 Normal data with a noninformative prior (pp. 64–67)
**Setup.** $y$ is a vector of $n$ independent observations from $N(\mu,\sigma^2)$ (p. 64). The noninformative prior is a convenient assumption for exposition, easily extended to informative priors (p. 64). From Chapter 2, a sensible vague prior, assuming prior independence of location and scale, is uniform on $(\mu,\log\sigma)$, i.e. $p(\mu,\sigma^2)\propto(\sigma^2)^{-1}$ (p. 64).

**Joint posterior.** The posterior is the likelihood times $1/\sigma^2$ (p. 64):
$$p(\mu,\sigma^2|y)\propto\sigma^{-n-2}\exp\Big(-\tfrac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big)
=\sigma^{-n-2}\exp\Big(-\tfrac{1}{2\sigma^2}\Big[\sum_{i=1}^n(y_i-\bar y)^2+n(\bar y-\mu)^2\Big]\Big)$$
$$=\sigma^{-n-2}\exp\Big(-\tfrac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big]\Big),\tag{3.2}$$
with $s^2=\frac1{n-1}\sum_{i=1}^n(y_i-\bar y)^2$. The sufficient statistics are $\bar y$ and $s^2$ (p. 64).

**Conditional posterior.** From the known-variance, uniform-prior result of Section 2.5 (p. 65):
$$\mu|\sigma^2,y\sim N(\bar y,\sigma^2/n).\tag{3.3}$$

**Marginal posterior of $\sigma^2$.** Average (3.2) over $\mu$. The $\mu$-integral is a simple normal integral, giving the factor $\sqrt{2\pi\sigma^2/n}$ (p. 65):
$$p(\sigma^2|y)\propto\sigma^{-n-2}\exp\Big(-\tfrac{1}{2\sigma^2}(n-1)s^2\Big)\sqrt{2\pi\sigma^2/n}\propto(\sigma^2)^{-(n+1)/2}\exp\Big(-\tfrac{(n-1)s^2}{2\sigma^2}\Big),\tag{3.4}$$
which is a scaled inverse-$\chi^2$ density:
$$\sigma^2|y\sim\text{Inv-}\chi^2(n-1,s^2).\tag{3.5}$$
So $p(\mu,\sigma^2|y)=p(\mu|\sigma^2,y)\,p(\sigma^2|y)$ (p. 65). This resembles the sampling-theory result that $(n-1)s^2/\sigma^2$ given $\sigma^2$ is $\chi^2_{n-1}$. The author says this is not surprising, given the reference prior for scale derived in Section 2.8 (p. 65).

**Sampling.** Draw $\sigma^2$ from (3.5), then $\mu$ from (3.3) (p. 65). This is one of the few multiparameter problems simple enough to solve in closed form (p. 65).

**Marginal posterior of $\mu$.** By (3.1), $\mu|y$ is a mixture of normals, mixed over the scaled inverse-$\chi^2$ for $\sigma^2$ (p. 65). Integrate $\sigma^2$ out of the joint posterior, using the substitution $z=A/(2\sigma^2)$ with $A=(n-1)s^2+n(\mu-\bar y)^2$. The integral becomes an unnormalized gamma integral (p. 66):
$$p(\mu|y)\propto A^{-n/2}\int_0^\infty z^{(n-2)/2}e^{-z}\,dz\propto[(n-1)s^2+n(\mu-\bar y)^2]^{-n/2}\propto\Big[1+\tfrac{n(\mu-\bar y)^2}{(n-1)s^2}\Big]^{-n/2}.$$
This is the $t_{n-1}(\bar y,s^2/n)$ density. Equivalently, with $t_{n-1}$ the standard $t$ (location 0, scale 1) (p. 66):
$$\frac{\mu-\bar y}{s/\sqrt n}\Big|\,y\sim t_{n-1}.$$

**Comparison with sampling theory.** Under the sampling distribution, $\frac{\bar y-\mu}{s/\sqrt n}\big|\,\mu,\sigma^2\sim t_{n-1}$ (p. 66). The author defines a **pivotal quantity** as a nontrivial function of the data and the estimand whose sampling distribution is independent of all parameters and data (p. 66). Here the sampling distribution of $(\bar y-\mu)/(s/\sqrt n)$ does not depend on the nuisance parameter $\sigma^2$, and its posterior distribution does not depend on the data (p. 66).

*Intuition note:* Not knowing $\sigma$ makes the posterior of $\mu$ heavier-tailed than a normal. The $t$ is exactly the mixture of normals with different variances, weighted by how plausible each variance is.

**Posterior predictive for a new $\tilde y$** (p. 66).
- It is a mixture: $p(\tilde y|y)=\iint p(\tilde y|\mu,\sigma^2,y)\,p(\mu,\sigma^2|y)\,d\mu\,d\sigma^2$. The first factor is just $N(\mu,\sigma^2)$ and does not depend on $y$ (p. 66).
- To simulate: draw $(\mu,\sigma^2)$ from the joint posterior, then $\tilde y\sim N(\mu,\sigma^2)$ (p. 66).
- Analytically, $\tilde y|y$ is a $t$ with location $\bar y$, scale $(1+\tfrac1n)^{1/2}s$ and $n-1$ degrees of freedom (p. 66).
- It follows from $p(\tilde y|\sigma^2,y)=N(\tilde y|\bar y,(1+\tfrac1n)\sigma^2)$, which equals the distribution of $\mu|\sigma^2,y$ up to a changed scale (p. 66).

**Example: speed of light (pp. 66–67).**
- Newcomb (1882) measured the time for light to travel 7442 meters. There are 66 measurements, with two unusually low values and a roughly symmetric cluster (Figure 3.1; data are deviations from 24,800 nanoseconds). The normal model is "inappropriately" applied, assuming independent draws from $N(\mu,\sigma^2)$ (pp. 66–67).
- The outliers do not fit; lack of fit is treated in Section 6.3 (p. 67).
- Data summaries: $\bar y=26.2$, $s=10.8$. With the prior $(\sigma^2)^{-1}$, the 95% central posterior interval from $t_{65}$ is $\bar y\pm1.997\,s/\sqrt{66}=[23.6,28.8]$ (p. 67).
- Simulation: draw $\sigma^2\sim\text{Inv-}\chi^2(65,s^2)$ as $65s^2$ divided by a $\chi^2_{65}$ draw, then $\mu\sim N(26.2,\sigma^2/66)$. From 1000 draws, the posterior median is 26.2 and the 95% interval is $[23.6,28.9]$, close to the analytic interval (p. 67).
- The currently accepted "true value" for $\mu$ is 33.0, outside the 95% interval. This reinforces the point that posterior inferences are only as good as the model and the experiment (p. 67).

### 3.3 Normal data with a conjugate prior (pp. 67–69)
**Prior family.** The likelihood (3.2) shows that a conjugate prior must have the form $p(\sigma^2)p(\mu|\sigma^2)$, with $\sigma^2$ scaled inverse-$\chi^2$ and $\mu|\sigma^2$ normal (so marginally $\mu$ is $t$) (p. 67). Parameterization:
$$\mu|\sigma^2\sim N(\mu_0,\sigma^2/\kappa_0),\qquad\sigma^2\sim\text{Inv-}\chi^2(\nu_0,\sigma_0^2),$$
$$p(\mu,\sigma^2)\propto\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\tfrac1{2\sigma^2}[\nu_0\sigma_0^2+\kappa_0(\mu_0-\mu)^2]\Big).\tag{3.6}$$
This is labelled N-Inv-$\chi^2(\mu,\sigma^2|\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$. Its four parameters are the location and scale of $\mu$ and the degrees of freedom and scale of $\sigma^2$ (p. 67). Because $\sigma^2$ appears in $\mu|\sigma^2$, $\mu$ and $\sigma^2$ are necessarily dependent a priori. The author argues it often makes sense to tie the prior variance of the mean to $\sigma^2$: prior belief about $\mu$ is then calibrated by the scale of measurement and is equivalent to $\kappa_0$ prior measurements on that scale (p. 68).

**Joint posterior.** Multiply (3.6) by the normal likelihood (p. 68):
$$p(\mu,\sigma^2|y)\propto\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\tfrac{1}{2\sigma^2}[\nu_0\sigma_0^2+\kappa_0(\mu-\mu_0)^2]\Big)\times(\sigma^2)^{-n/2}\exp\Big(-\tfrac1{2\sigma^2}[(n-1)s^2+n(\bar y-\mu)^2]\Big)\tag{3.7}$$
$$=\text{N-Inv-}\chi^2(\mu,\sigma^2|\mu_n,\sigma_n^2/\kappa_n;\nu_n,\sigma_n^2),$$
where, after algebra (left as Exercise 3.9; not shown in the text):
$$\mu_n=\frac{\kappa_0}{\kappa_0+n}\mu_0+\frac{n}{\kappa_0+n}\bar y,\quad\kappa_n=\kappa_0+n,\quad\nu_n=\nu_0+n,$$
$$\nu_n\sigma_n^2=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0 n}{\kappa_0+n}(\bar y-\mu_0)^2.$$
- $\mu_n$ is a weighted average of prior and sample means, with weights set by relative precision.
- $\nu_n$ is prior degrees of freedom plus sample size.
- $\nu_n\sigma_n^2$ combines the prior sum of squares, the sample sum of squares, and extra uncertainty from the gap between sample and prior means (p. 68).

**Conditional and marginal posteriors** (pp. 68–69):
$$\mu|\sigma^2,y\sim N(\mu_n,\sigma^2/\kappa_n)=N\Big(\frac{\frac{\kappa_0}{\sigma^2}\mu_0+\frac n{\sigma^2}\bar y}{\frac{\kappa_0}{\sigma^2}+\frac n{\sigma^2}},\ \frac1{\frac{\kappa_0}{\sigma^2}+\frac n{\sigma^2}}\Big),\tag{3.8}$$
which agrees with Section 2.5 for fixed $\sigma$ (p. 68). Also
$$\sigma^2|y\sim\text{Inv-}\chi^2(\nu_n,\sigma_n^2).\tag{3.9}$$
Sampling: draw $\sigma^2$ from (3.9), then $\mu$ from (3.8) (p. 69). Integrating out $\sigma^2$ "in a precisely analogous way" gives (p. 69)
$$p(\mu|y)\propto\Big(1+\frac{\kappa_n(\mu-\mu_n)^2}{\nu_n\sigma_n^2}\Big)^{-(\nu_n+1)/2}=t_{\nu_n}(\mu|\mu_n,\sigma_n^2/\kappa_n).$$

*Intuition note:* The prior acts like $\kappa_0$ extra observations of the mean and $\nu_0$ extra degrees of freedom for the variance. Updating just adds the real $n$ to each and pools the means and sums of squares.

### 3.4 Multinomial model for categorical data (pp. 69–70)
Each observation is one of $k$ outcomes; $y$ is the vector of counts, and $\sum_j\theta_j=1$. The sampling distribution is $p(y|\theta)\propto\prod_{j=1}^k\theta_j^{y_j}$, implicitly conditioning on $\sum_jy_j=n$ (p. 69). The conjugate prior is the Dirichlet, $p(\theta|\alpha)\propto\prod_j\theta_j^{\alpha_j-1}$, on nonnegative $\theta_j$ with $\sum\theta_j=1$. The posterior is Dirichlet with parameters $\alpha_j+y_j$ (p. 69).
- The prior is equivalent to a likelihood from $\sum_j(\alpha_j-1)$ observations, with $\alpha_j-1$ in category $j$ (p. 69).
- $\alpha_j=1$ for all $j$ gives a uniform density over the simplex (the set of probability vectors).
- $\alpha_j=0$ for all $j$ gives an improper prior, uniform in the $\log\theta_j$. Its posterior is proper if each of the $k$ counts is positive (p. 69).
- Other suggested noninformative priors are pointed to in the bibliographic note (p. 69).

**Example: pre-election poll (pp. 69–70).**
- CBS News, late October 1988: of 1447 adults, $y_1=727$ Bush, $y_2=583$ Dukakis, $y_3=137$ other or no opinion (pp. 69–70).
- Under exchangeability and simple random sampling, the data are multinomial. The estimand is $\theta_1-\theta_2$ (p. 70).
- With $\alpha_1=\alpha_2=\alpha_3=1$, the posterior is Dirichlet(728, 584, 138) (p. 70).
- Rather than integrating, draw 1000 points from the Dirichlet and compute $\theta_1-\theta_2$ for each (Figure 3.2). All 1000 had $\theta_1>\theta_2$, so the estimated posterior probability that Bush had more support is over 99.9% (p. 70).
- The survey actually used a stratified plan; an improved analysis is in Section 8.3 (p. 70).

For problems with very many categories, extra structure is needed, through an informative prior (hierarchical modeling, Chapter 5) or loglinear models (Section 16.7) (p. 70).

### 3.5 Multivariate normal model with known variance (pp. 70–72)
This section is reference material for later chapters on linear models (p. 70).

**Likelihood** ($y$ is $d\times1$, $\mu$ is $d\times1$, $\Sigma$ is $d\times d$, symmetric positive definite) (p. 71):
$$y|\mu,\Sigma\sim N(\mu,\Sigma),\tag{3.10}$$
$$p(y_1,\dots,y_n|\mu,\Sigma)\propto|\Sigma|^{-n/2}\exp\Big(-\tfrac12\sum_{i=1}^n(y_i-\mu)^T\Sigma^{-1}(y_i-\mu)\Big).\tag{3.11}$$

**Conjugate analysis, known $\Sigma$** (p. 71). The log-likelihood is quadratic in $\mu$, so the conjugate prior is $\mu\sim N(\mu_0,\Lambda_0)$. The posterior is
$$p(\mu|y,\Sigma)\propto\exp\Big(-\tfrac12\Big[(\mu-\mu_0)^T\Lambda_0^{-1}(\mu-\mu_0)+\sum_i(y_i-\mu)^T\Sigma^{-1}(y_i-\mu)\Big]\Big).$$
Completing the quadratic form (Exercise 3.13) gives $N(\mu|\mu_n,\Lambda_n)$ with
$$\mu_n=(\Lambda_0^{-1}+n\Sigma^{-1})^{-1}(\Lambda_0^{-1}\mu_0+n\Sigma^{-1}\bar y),\qquad\Lambda_n^{-1}=\Lambda_0^{-1}+n\Sigma^{-1}.\tag{3.12}$$
The posterior mean is a weighted average of prior mean and data, with weights the precision matrices $\Lambda_0^{-1}$ and $n\Sigma^{-1}$. The posterior precision is the sum of prior and data precisions (p. 71).

**Subvectors** (pp. 71–72). Marginals of a subset $\mu^{(1)}$ are normal, using the matching subvector of $\mu_n$ and submatrix of $\Lambda_n$. The conditional is
$$\mu^{(1)}|\mu^{(2)},y\sim N\big(\mu_n^{(1)}+\beta^{1|2}(\mu^{(2)}-\mu_n^{(2)}),\ \Lambda^{1|2}\big),\tag{3.13}$$
$$\beta^{1|2}=\Lambda_n^{(12)}\big(\Lambda_n^{(22)}\big)^{-1},\qquad\Lambda^{1|2}=\Lambda_n^{(11)}-\Lambda_n^{(12)}\big(\Lambda_n^{(22)}\big)^{-1}\Lambda_n^{(21)}.$$

**Posterior predictive, known $\Sigma$** (p. 72). $p(\tilde y,\mu|y)=N(\tilde y|\mu,\Sigma)N(\mu|\mu_n,\Lambda_n)$ is the exponential of a quadratic form in $(\tilde y,\mu)$, so $\tilde y|y$ is multivariate normal. Using (2.7) and (2.8):
$$E(\tilde y|y)=E(E(\tilde y|\mu,y)|y)=E(\mu|y)=\mu_n,$$
$$\text{var}(\tilde y|y)=E(\text{var}(\tilde y|\mu,y)|y)+\text{var}(E(\tilde y|\mu,y)|y)=E(\Sigma|y)+\text{var}(\mu|y)=\Sigma+\Lambda_n.$$

**Noninformative prior** (p. 72). $p(\mu)\propto$ constant arises as the limit where prior precision tends to zero, $|\Lambda_0^{-1}|\to0$; the prior mean is then irrelevant. This does not give a proper joint model, but the posterior is proper: $\mu|\Sigma,y\sim N(\bar y,\Sigma/n)$.

### 3.6 Multivariate normal with unknown mean and variance (pp. 72–74)
**Normal-inverse-Wishart prior** (hyperparameters $(\mu_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$). The inverse-Wishart is a multivariate generalization of the scaled inverse-$\chi^2$ (p. 72):
$$\Sigma\sim\text{Inv-Wishart}_{\nu_0}(\Lambda_0^{-1}),\qquad\mu|\Sigma\sim N(\mu_0,\Sigma/\kappa_0),$$
$$p(\mu,\Sigma)\propto|\Sigma|^{-((\nu_0+d)/2+1)}\exp\Big(-\tfrac12\text{tr}(\Lambda_0\Sigma^{-1})-\tfrac{\kappa_0}2(\mu-\mu_0)^T\Sigma^{-1}(\mu-\mu_0)\Big).$$
Here $\nu_0$, $\Lambda_0$ are the degrees of freedom and scale matrix for $\Sigma$. $\mu_0$ and $\kappa_0$ are the prior mean and the number of prior measurements on the $\Sigma$ scale (p. 73).

**Posterior** (same family) (p. 73):
$$\mu_n=\frac{\kappa_0}{\kappa_0+n}\mu_0+\frac{n}{\kappa_0+n}\bar y,\quad\kappa_n=\kappa_0+n,\quad\nu_n=\nu_0+n,$$
$$\Lambda_n=\Lambda_0+S+\frac{\kappa_0n}{\kappa_0+n}(\bar y-\mu_0)(\bar y-\mu_0)^T,\qquad S=\sum_{i=1}^n(y_i-\bar y)(y_i-\bar y)^T.$$
- The marginal posterior of $\mu$ is multivariate $t_{\nu_n-d+1}\big(\mu_n,\Lambda_n/(\kappa_n(\nu_n-d+1))\big)$.
- The posterior predictive of $\tilde y$ is also multivariate $t$, with an additional factor $\kappa_n+1$ in the numerator of the scale matrix (p. 73).
- Sampling: draw $\Sigma|y\sim\text{Inv-Wishart}_{\nu_n}(\Lambda_n^{-1})$, then $\mu|\Sigma,y\sim N(\mu_n,\Sigma/\kappa_n)$. For predictive draws, then $\tilde y\sim N(\mu,\Sigma)$ (p. 73).

**Noninformative priors** (p. 73).
- $\Sigma\sim\text{Inv-Wishart}_{d+1}(I)$: each correlation in $\Sigma$ has a marginally uniform prior. The joint is not uniform, because the correlation matrix must be positive definite.
- Multivariate Jeffreys prior $p(\mu,\Sigma)\propto|\Sigma|^{-(d+1)/2}$, the limit of the conjugate prior as $\kappa_0\to0$, $\nu_0\to-1$, $|\Lambda_0|\to0$. Posterior: $\Sigma|y\sim\text{Inv-Wishart}_{n-1}(S^{-1})$, $\mu|\Sigma,y\sim N(\bar y,\Sigma/n)$. The marginal posterior of $\mu$ is $t_{n-d}(\bar y,S/(n(n-d)))$, assuming the posterior is proper.

**Scaled inverse-Wishart** (p. 74). $\Sigma=\text{Diag}(\xi)\,\Sigma_\eta\,\text{Diag}(\xi)$. Here $\Sigma_\eta$ gets an inverse-Wishart prior (one choice is Inv-Wishart$_{d+1}(I)$, giving uniform marginal correlations) and the scale parameters $\xi$ get weakly informative priors. This allows a uniform or weak prior on correlations without overly constraining the variances. It is developed further in Section 15.4 (p. 74).

### 3.7 Example: analysis of a bioassay experiment (pp. 74–78)
Beyond the normal, few multiparameter models give simple explicit posteriors. This section gives a nonconjugate two-parameter generalized linear model, solved by a discrete approximation on a two-dimensional grid (p. 74).

**Data.** Doses $x_i$ (often on a log scale) given to $n_i$ animals, of which $y_i$ respond, $i=1,\dots,k$. Table 3.1 (Racine et al., 1986), 5 animals per dose (p. 74):

| Dose $x_i$ (log g/ml) | $n_i$ | deaths $y_i$ |
|---|---|---|
| −0.86 | 5 | 0 |
| −0.30 | 5 | 1 |
| −0.05 | 5 | 3 |
| 0.73 | 5 | 5 |

**Model** (pp. 74–75).
- Animals within group $i$ are exchangeable and modeled as independent with equal probabilities, so $y_i|\theta_i\sim\text{Bin}(n_i,\theta_i)$. Independence and the binomial would not be appropriate if deaths were caused by a contagious disease. Groups are independent given $\theta_1,\dots,\theta_4$ (p. 75).
- An exchangeable prior on the $\theta_i$ (e.g. $p\propto1$, giving independent beta posteriors) has a serious flaw: the dose is known and the death probability should vary systematically with dose (p. 75).
- A linear $\theta_i=\alpha+\beta x_i$ fails because $\theta_i$ must lie in $[0,1]$ while $x_i$ can approach $\pm\infty$. The standard fix is the logistic regression model
$$\text{logit}(\theta_i)=\alpha+\beta x_i,\tag{3.14}$$
with $\text{logit}(\theta_i)=\log(\theta_i/(1-\theta_i))$ (p. 75).

**Likelihood and posterior** (p. 75):
$$p(y_i|\alpha,\beta,n_i,x_i)\propto[\text{logit}^{-1}(\alpha+\beta x_i)]^{y_i}[1-\text{logit}^{-1}(\alpha+\beta x_i)]^{n_i-y_i},$$
$$p(\alpha,\beta|y,n,x)\propto p(\alpha,\beta|n,x)\,p(y|\alpha,\beta,n,x)\propto p(\alpha,\beta)\prod_{i=1}^kp(y_i|\alpha,\beta,n_i,x_i).\tag{3.15}$$
$n_i$ and $x_i$ are treated as fixed. The prior is independent and locally uniform, $p(\alpha,\beta)\propto1$. This may be used if there is really no prior knowledge or for a simple analysis of this experiment alone. If it is too imprecise, informative priors from other experiments could be built (p. 75).

**Computation** (p. 76).
- *Rough estimate.* A maximum-likelihood logistic regression gives $(\hat\alpha,\hat\beta)=(0.8,7.7)$ with standard errors 1.0 and 4.9. This shows where to look.
- *Grid.* After experimentation the range is $(\alpha,\beta)\in[-5,10]\times[-10,40]$, which captures almost all the posterior mass. Figure 3.3a shows contours at 0.05, 0.15, …, 0.95 times the mode's density. A justification for the lowest level 0.05 is in Section 4.1.
- *Normalize.* Treat the distribution as a step function over the grid, with total probability 1.
- *Draw 1000 samples:*
  1. Compute the marginal $p(\alpha|y)$ by numerically summing over $\beta$ on the grid.
  2. For $s=1,\dots,1000$: (a) draw $\alpha^s$ from the discrete $p(\alpha|y)$ (a discrete inverse-cdf method, Section 1.9); (b) draw $\beta^s$ from the discrete $p(\beta|\alpha^s,y)$; (c) add uniform jitter centered at zero, with width equal to the grid spacing, so the draws are continuous.
  The draws are shown in Figure 3.3b (pp. 76–77).

**Practical cautions** (p. 77). A grid over too small an area may miss posterior features outside it. A large, coarse grid may miss features between points. To avoid overflow and underflow, compute the log of the unnormalized posterior, subtract its maximum, then exponentiate. This gives an unnormalized approximation with maximum 1, which is then normalized.

**LD50** (pp. 77–78). The LD50 is the dose at which the death probability is 50%. In the logistic model, $E(y_i/n_i)=\text{logit}^{-1}(\alpha+\beta x_i)=0.5$, so $\alpha+\beta x_i=\text{logit}(0.5)=0$ and LD50 $=-\alpha/\beta$ (p. 77). Computing it for each of the 1000 draws $(\alpha^s,\beta^s)$ gives its posterior (Figure 3.4) (p. 77).
- The LD50 is meaningless when $\beta\le0$, since dose then does not increase death probability. The author prefers to allow $\beta\le0$ and note that the LD50 is hard to interpret then, rather than constrain the space (the author says we should constrain it if we were certain the drug could not cause the tumor rate to decrease) (p. 77).
- Reported: (1) $\Pr(\beta>0)$, here roughly estimated to exceed 0.999, since all 1000 draws had $\beta>0$; (2) the LD50 posterior conditional on $\beta>0$ (all 1000 draws here) (p. 77).
- Lesson: the marginal posterior mean is not always a good summary. The posterior mean of the LD50 would include cases with a negative dose–response relation (p. 78).

*Intuition note:* With two parameters, one can evaluate the unnormalized posterior at many grid points, turn it into a discrete distribution, and sample from it. Any derived quantity (here $-\alpha/\beta$) is then computed draw by draw, with no new calculus.

### 3.8 Summary of elementary modeling and computation (p. 78)
Lack of easy multiparameter models is not a major handicap, for three reasons (p. 78):
1. With few parameters, simple simulation handles nonconjugate models (as in the bioassay).
2. Sophisticated models can often be represented hierarchically or conditionally (Chapter 5; Part III).
3. A normal approximation to the posterior can often be applied (Chapter 4), so the normal model's conjugate structure matters beyond explicitly normal models.

The author's strategy ("not truly a general approach", but a foreshadowing of Part III) (p. 78):
1. Write the likelihood $p(y|\theta)$, ignoring factors free of $\theta$.
2. Write $p(\theta|y)\propto p(\theta)p(y|\theta)$. Use a well-formulated prior if available; otherwise a weakly informative prior or temporarily $p(\theta)\propto$ constant.
3. Make a crude estimate of $\theta$ as a starting point and a comparison.
4. Draw $\theta^1,\dots,\theta^S$ from the posterior and compute posterior summaries of any functions of $\theta$.
5. For predictions, draw $\tilde y^s$ from $p(\tilde y|\theta^s)$ (model checking is in Chapter 6).

Step 4 can be difficult for nonconjugate models. Grid computation is possible when $\theta$ has one or two components (p. 78).

### 3.9 Bibliographic note (pp. 78–79)
- Box and Tiao (1973, Ch. 2) treat the normal problems thoroughly, including differences of means and ratios of variances. Authors of that period restricted themselves to conjugate families because simulation was less convenient (p. 78).
- Mardia, Kent and Bibby (1979) are cited for multivariate normal properties, and Stigler (1977) for Newcomb's data. Good (1965) and Fienberg (1977) cover the multinomial model and its priors. Racine et al. (1986) is the source of the bioassay data and model (p. 79).

### 3.10 Exercises (pp. 79–82)
Fifteen exercises are given; six are picked in "Exercises worth doing". Their content is not worked here.

## Toy example (ours, not from the text)
Data: $n=3$, $y=(1,2,3)$. Then $\bar y=(1+2+3)/3=2$ and $s^2=\frac{(1-2)^2+0+(3-2)^2}{2}=1$.

*Noninformative prior (Section 3.2).* $\sigma^2|y\sim\text{Inv-}\chi^2(2,1)$, i.e. $\sigma^2=(n-1)s^2/\chi^2_2=2/\chi^2_2$. Suppose one draw is $\chi^2_2=1.0$. Then $\sigma^2=2/1.0=2.0$, and $\mu|\sigma^2,y\sim N(2,2/3)$. Repeating this many times gives draws from $t_2(2,\,1/3)$ for $\mu$. A predictive draw is $\tilde y\sim N(\mu,\sigma^2)$. Analytically, $\tilde y|y$ has location 2 and scale $(1+\tfrac13)^{1/2}\cdot1\approx1.155$ with 2 degrees of freedom.

*Conjugate prior (Section 3.3).* Take $\mu_0=0$, $\kappa_0=1$, $\nu_0=2$, $\sigma_0^2=1$.
- $\mu_n=\frac{1}{1+3}\cdot0+\frac{3}{4}\cdot2=1.5$.
- $\kappa_n=1+3=4$, $\nu_n=2+3=5$.
- $\nu_n\sigma_n^2=2\cdot1+2\cdot1+\frac{1\cdot3}{4}(2-0)^2=2+2+3=7$, so $\sigma_n^2=1.4$.
- Posterior: $\sigma^2|y\sim\text{Inv-}\chi^2(5,1.4)$ and $\mu|y\sim t_5(1.5,\,1.4/4=0.35)$.

The posterior mean 1.5 lies between the prior mean 0 and the sample mean 2, closer to the data because $n=3>\kappa_0=1$.

## Concepts
- [[nuisance-parameter]] (new) — a parameter needed for the model but not of inferential interest, e.g. the error scale (p. 63)
- [[marginal-posterior-via-mixture]] (new) — $p(\theta_1|y)$ as a $p(\theta_2|y)$-weighted mixture of conditionals; basis of marginal-then-conditional simulation (p. 64)
- [[posterior-distribution]] — here the joint posterior of all unknowns, then marginalized to the parameters of interest (p. 63)
- [[noninformative-prior]] (new) — vague prior used for exposition, e.g. uniform on $(\mu,\log\sigma)$ or $p(\theta)\propto1$; may be improper (pp. 64, 75)
- [[conjugate-prior]] — a family closed under updating; for the normal it is N-Inv-$\chi^2$, for the multinomial Dirichlet, for the multivariate normal normal-inverse-Wishart (pp. 67, 69, 72)
- [[normal-inverse-chi-squared]] (new) — joint prior/posterior for $(\mu,\sigma^2)$: $\sigma^2$ scaled inverse-$\chi^2$, $\mu|\sigma^2$ normal; $\kappa_0$ acts as prior sample size (pp. 67–68)
- [[pivotal-quantity]] (new) — nontrivial function of data and estimand whose sampling distribution is independent of all parameters and data (p. 66)
- [[posterior-predictive-distribution]] — for normal data, a $t$ with scale $(1+1/n)^{1/2}s$; simulated by drawing parameters, then $\tilde y$ (p. 66)
- [[dirichlet-multinomial]] (new) — Dirichlet prior with multinomial likelihood gives Dirichlet($\alpha_j+y_j$) posterior (p. 69)
- [[inverse-wishart]] (new) — multivariate generalization of the scaled inverse-$\chi^2$, prior for a covariance matrix (p. 72)
- [[logistic-regression]] (new) — $\text{logit}(\theta_i)=\alpha+\beta x_i$; here a nonconjugate two-parameter model (p. 75)
- [[grid-approximation]] (new) — discrete approximation of the posterior on a grid, sampled via marginal-then-conditional draws with jitter (p. 76)
- [[monte-carlo-integration]] — summaries (e.g. $\theta_1-\theta_2$, LD50) computed from posterior draws (pp. 70, 77)
- [[exchangeability]] — used to justify the multinomial and binomial models (pp. 70, 75)

## Canonical instances
- [[newcomb-speed-of-light]] — normal model with unknown $\mu,\sigma^2$: $t_{65}$ interval $[23.6,28.8]$ misses the accepted value 33.0; outliers show misfit (pp. 66–67)
- [[cbs-1988-poll]] — Dirichlet(728, 584, 138) posterior; $\Pr(\theta_1>\theta_2)>99.9\%$ by simulation (pp. 69–70)
- [[bioassay-racine-1986]] — logistic dose–response, grid posterior, LD50 summary conditional on $\beta>0$ (pp. 74–78)

## Bridges (candidates)
- [structural-analogy] Draw $\theta_2\sim p(\theta_2|y)$, then $\theta_1\sim p(\theta_1|\theta_2,y)$ ↔ sampling in general: sampling a joint distribution by factoring it into a marginal and a conditional (as in a Gibbs-type split) — same factorization idea, but here the draws are exact and independent.
- [same-math] Dirichlet–multinomial (k = 2) ↔ Beta–binomial from Ch. 2: the Dirichlet generalizes the beta, and $\alpha_j-1$ plays the role of prior counts.
- [structural-analogy] Precision-weighted posterior mean $\mu_n$ (3.8, 3.12) ↔ partial pooling/shrinkage: an estimate pulled from the data mean toward a prior mean in proportion to relative precision.
- [structural-analogy] Posterior of $(\bar y-\mu)/(s/\sqrt n)$ is $t_{n-1}$ ↔ frequentist inference: the same $t$ appears as a sampling distribution, so intervals coincide numerically, though the interpretation differs.
- [metaphor] LD50 summarized conditional on $\beta>0$ ↔ causal/estimand definition: a quantity is only defined in part of parameter space, so report the probability of that region plus the conditional distribution.

## Questions this raises
- When the noninformative prior is improper, how can we be sure the posterior is proper? (Exercise 14 asks this for the bioassay posterior.)
- The Newcomb 95% interval misses the accepted value 33.0, and the normal model fits the outliers poorly. How should one check and repair such misfit (Section 6.3 is cited)?
- A grid works for two parameters. How do the Part III methods replace it when $\theta$ has many components?
- How do different noninformative priors for $\Sigma$ (Inv-Wishart$_{d+1}(I)$ versus Jeffreys) change conclusions for small $n$ relative to $d$?

## Exercises worth doing
- Ex. 1 (p. 79) — show the marginal posterior of $\theta_1/(\theta_1+\theta_2)$ from a multinomial–Dirichlet model equals the binomial posterior using only $y_1,y_2$ — difficulty: medium
- Ex. 2 (p. 79) — compare two multinomial polls (pre/post debate) by simulating $\alpha_2-\alpha_1$ — difficulty: easy
- Ex. 3 (pp. 79–80) — two independent normal experiments (Behrens–Fisher): sample from two $t$ posteriors for $\mu_t-\mu_c$ — difficulty: medium
- Ex. 9 (p. 82) — derive the N-Inv-$\chi^2$ posterior parameters (the algebra behind (3.7)) — difficulty: medium
- Ex. 11 (p. 82) — redo the bioassay with a normal prior on $(\alpha,\beta)$ and see the compromise between prior and likelihood — difficulty: medium
- Ex. 14 (p. 82) — prove the bioassay posterior (3.15) is proper — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 73 = printed 63). All page references are printed numbers.
- The text layer is garbled: it renders the parameter symbol as ω (the page images show θ) and renders "∼" and "−" as "→". Quotations of equations here follow the images, with θ throughout (including the chapter intro and Section 3.1).
- The chapter intro says Sections 3.4 and 3.5 treat the multinomial and multivariate normal. In the printed headings, 3.4 is multinomial, 3.5 is multivariate normal with known variance, and 3.6 is multivariate normal with unknown mean and variance.
- Algebra for the posterior parameters in (3.7) and for (3.12) is not shown in the text (Exercises 9 and 13), so it is not derived here. The (2.7), (2.8) identities used on p. 72 are cited, not restated.
- The text's "Inverse-Wishart with d−1 degrees of freedom" heading (p. 73) introduces the Jeffreys prior, whose posterior is Inv-Wishart$_{n-1}$.
- The speed-of-light interval is $[23.6,28.8]$ analytically and $[23.6,28.9]$ by simulation, as printed.
- Of the fifteen Section 3.10 exercises, only six are listed (by topic); Table 3.2 (ABC polls) and Table 3.3 (Berkeley traffic) are exercise data and are not reproduced.
