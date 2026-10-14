---
id: murphy-2023-pml2/ch15-generalized
work: murphy-2023-pml2
unit: "15 Generalized linear models"
pages: 591–629
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Generalized linear models (Murphy, PML2, ch. 15)

## L0 — One line
A GLM models a response with an exponential-family distribution whose mean is a function of a linear predictor $w^\top x$, and the chapter shows how to do Bayesian inference, choose priors and share information across groups for the main GLMs.

## L1 — The gist (≤ 120 words)
How can we model real, binary, count, ordered or grouped responses as a linear function of inputs, and still measure uncertainty about the weights? A GLM puts an exponential-family distribution on $y$, with mean $\ell^{-1}(w^\top x)$. The chapter gives exact conjugate Bayesian results for linear regression, and then discusses informative, uninformative and sparsity-promoting priors. For logistic and probit regression it gives approximations: Laplace, probit-moderated predictions, MCMC and latent-variable Gibbs. It then covers hierarchical GLMs that pool information across groups. Two lessons recur: check priors on the outcome scale, and do not read causal conclusions from a predictive fit (the Berkeley example).

**Prerequisites:** exponential families (log-normalizer, mean $=A'$); Gaussian conditioning and conjugacy; MAP vs MLE; Newton/gradient methods; Bernoulli/binomial/Poisson distributions; basic DAGs (collider).

## L2 — Key ideas (5–10 bullets)
- A GLM is a conditional exponential family with natural parameter $\eta=w^\top x$; the link $\ell$ ties mean and $\eta$. With the canonical link the gradient is $(y-\mu)x$ and the negative log-likelihood (NLL) is convex (pp. 591, 595).
- Linear regression has closed-form Bayesian answers. A Gaussian prior gives ridge regression as MAP. Normal-inverse-gamma gives Student posterior and predictive distributions. Jeffreys prior reproduces the frequentist $t$ results numerically (pp. 597–600).
- Priors should be judged by what they imply for outcomes. Prior predictive samples exposed a bad $\mathcal N(0,10)$ slope prior; a large logit-scale variance piles mass near 0 and 1 (pp. 602, 613).
- Sparsity priors form a ladder: spike-and-slab (sparse samples, hard to compute), Laplace/lasso (sparse MAP, non-sparse samples), horseshoe (continuous, both), ARD, automatic relevance determination (empirical Bayes, sparse via marginal likelihood) (pp. 603–608).
- Logistic regression has no conjugate prior. Laplace approximation plus a Monte Carlo or probit-moderated predictive gives uncertainty that grows away from the data (pp. 613–617).
- Probit regression is a thresholded latent Gaussian. This gives EM and a simple Gibbs sampler, and extends to ordinal and multinomial responses (pp. 621–625).
- Class imbalance: minimizing balanced error needs $p(x\mid y)$; logit adjustment subtracts $\tau\log\pi_y$ from logits (p. 612).
- Hierarchical GLMs partially pool groups. The radon example shows better fit; non-centering reduces the funnel problem (Neal's funnel) (pp. 625–629).
- Berkeley admissions: a gender-only model suggests bias; adding department makes the apparent bias disappear; an unobserved confounder would invalidate that again (pp. 619–620).

## L3 — Walkthrough

### 15.1 Introduction (pp. 591–596)
**Definition (p. 591).** A GLM is a conditional exponential-family model:
$$p(y_n\mid x_n,w,\sigma^2)=\exp\!\Big[\frac{y_n\eta_n-A(\eta_n)}{\sigma^2}+\log h(y_n,\sigma^2)\Big]\tag{15.1}$$
Here $\eta_n=w^\top x_n$ is the natural parameter, $A$ the log normalizer, $\mathcal T(y_n)=y_n$ the sufficient statistic and $\sigma^2$ the dispersion. Then
$$\mu_n=\mathbb E[y_n\mid x_n,w,\sigma^2]=A'(\eta_n)=\ell^{-1}(\eta_n),\tag{15.2}$$
$$\mathbb V[y_n\mid x_n,w,\sigma^2]=A''(\eta_n)\sigma^2,\tag{15.3}$$
$$\ell(\mu_n)=\eta_n=w^\top x_n.\tag{15.4}$$
$\ell$ is the link function and $\ell^{-1}$ the mean function (p. 591). Linearity limits predictive power, but basis expansion helps. The main statistical use of GLMs is hypothesis testing, which needs the posterior $p(w\mid\mathcal D)$ (p. 591).

**Examples (pp. 591–594).**
- *Linear regression.* $\log p=\frac{y\eta-\eta^2/2}{\sigma^2}-\frac12\big(\frac{y^2}{\sigma^2}+\log(2\pi\sigma^2)\big)$ (15.7), so $A=\eta^2/2$, $\mathbb E[y]=w^\top x$, $\mathbb V[y]=\sigma^2$ (pp. 591–592).
- *Binomial regression.* $y_n\in\{0,\dots,N_n\}$, $p=\mathrm{Bin}(y_n\mid\sigma(w^\top x_n),N_n)$. Logistic regression is $N_n=1$. With $\mu_n=\sigma(\eta_n)$, $\eta_n=\log\frac{\mu_n}{1-\mu_n}=w^\top x_n$ (15.13). Then $h(y)=\log\binom{N_n}{y_n}$ and $A(\eta)=-N_n\log(1-\mu_n)=N_n\log(1+e^{\eta})$ (15.15). So $\mathbb E[y_n]=A'=N_n\mu_n$ (15.16) and $\mathbb V[y_n]=A''=N_n\mu_n(1-\mu_n)$ (15.17) (pp. 592–593).
- *Poisson regression.* $p=\mathrm{Poi}(y_n\mid e^{w^\top x_n})$. Then $\eta_n=\log\mu_n$, $A(\eta)=e^{\eta}$, $h(y)=-\log(y!)$, and mean and variance both equal $\mu_n$ (15.20–15.23, p. 593).
- *Zero-inflated Poisson (ZIP).* For count data with excess zeros (e.g. zero sales because unpopular, or sold out), mix a spike at 0 with a Poisson (p. 594):
$$\mathrm{ZIP}(y\mid\rho,\lambda)=\begin{cases}\rho+(1-\rho)e^{-\lambda}&y=0\\(1-\rho)\frac{\lambda^y e^{-\lambda}}{y!}&y>0\end{cases}\tag{15.24}$$
$\rho$ is the prior probability of choosing the spike. A zero can come from the spike, or (probability $1-\rho$) from the Poisson with probability $e^{-\lambda}$ (p. 594).

**15.1.2 Noncanonical links (p. 594).** The canonical link satisfies $\theta=\ell(\mu)$, so $\theta=\ell(\ell^{-1}(\eta))=\eta$ (15.25). For the Bernoulli this is the logit $\ell(\mu)=\log\frac{\mu}{1-\mu}$ with sigmoid inverse. Other links are allowed:
- Probit: $\eta=\Phi^{-1}(\mu)$, $\mu=\Phi(\eta)$ (15.28–15.29).
- Complementary log-log: $\eta=\log(-\log(1-\mu))$ (15.30). Suppose $y=1$ means "one or more events" with events Poisson($\lambda$). Then $p(y=0)=1-\mu=e^{-\lambda}$ (15.31). Taking $\lambda=e^{\eta}$ to keep it positive gives $\eta=\log(-\log(1-\mu))$ (15.32).

**15.1.3 Maximum likelihood (p. 595).** Ignoring constants, $\mathrm{NLL}(w)=-\frac1{\sigma^2}\sum_n\ell_n$ with $\ell_n=\eta_ny_n-A(\eta_n)$ (15.33–15.34). Set $\sigma^2=1$. Gradient of one term:
$$g_n=\frac{\partial\ell_n}{\partial\eta_n}\frac{\partial\eta_n}{\partial w}=(y_n-A'(\eta_n))x_n=(y_n-\mu_n)x_n\tag{15.35}$$
with $\mu_n=f(w^\top x_n)$ and $f$ the inverse link. Hessian: $H=-\sum_n\partial g_n/\partial w^\top$ (15.36), with $\partial g_n/\partial w^\top=-x_nf'(w^\top x_n)x_n^\top$ (15.37). Hence
$$H=\sum_n f'(\eta_n)x_nx_n^\top.\tag{15.38}$$
For logistic regression $f'=\mu_n(1-\mu_n)$. Since $f'(\eta_n)>0$, the author concludes $H$ is positive definite, the NLL is convex and the MLE is unique (p. 595). Fit with IRLS (a Newton method) for small data or SGD for large data (p. 595).

*Intuition note.* With the canonical link, the gradient is just "residual times input", and the curvature is a positive-weighted sum of $xx^\top$. That is why fitting is a convex problem.

**15.1.4 Bayesian inference (p. 596).** MLE gives no uncertainty, which hypothesis testing needs. Priors depend on the link: a flat prior on an offset $\alpha\in\mathbb R$ is not flat on the probability scale after a sigmoid (see 15.3.4). For small data, HMC is the easiest method: write the log likelihood and log prior and use autodiff. Packages named: Bambi, RStanARM, BRMS (formula syntax). For large data, HMC is slow (full batch); use variational Bayes, expectation propagation or specialised methods (p. 596).

### 15.2 Linear regression (pp. 596–611)
Model: $p(y\mid x,\theta)=\mathcal N(y\mid w_0+w^\top x,\sigma^2)$ (15.39).

**15.2.1 OLS (pp. 596–597).** $\mathrm{NLL}=\frac1{2\sigma^2}\sum_n(y_n-\hat y_n)^2+\frac N2\log(2\pi\sigma^2)$ (15.41). The MLE is $\hat w_{\rm mle}=(X^\top X)^{-1}X^\top y$ (15.42). The noise MLE is the mean squared residual, $\hat\sigma^2=\frac1N\sum(y_n-x_n^\top\hat w)^2$ (15.43).

**15.2.2 Conjugate priors (pp. 597–599).**

*Known noise variance.* Prior $p(w)=\mathcal N(w\mid\breve w,\breve\Sigma)$ (15.44); typical choice $\breve w=0$, $\breve\Sigma=\tau^2I_D$ (bias often given a weaker prior). Likelihood: $\mathcal N(y\mid Xw,\sigma^2I_N)$ (15.45). By Bayes' rule for Gaussians (eq. 2.121c):
$$p(w\mid X,y,\sigma^2)=\mathcal N(w\mid\hat w,\hat\Sigma),\quad \hat w=\hat\Sigma\big(\breve\Sigma^{-1}\breve w+\tfrac1{\sigma^2}X^\top y\big),\quad\hat\Sigma=\big(\breve\Sigma^{-1}+\tfrac1{\sigma^2}X^\top X\big)^{-1}\tag{15.46–15.48}$$
With $\breve w=0,\breve\Sigma=\tau^2I$: $\hat w=\frac1{\sigma^2}\hat\Sigma X^\top y=(\frac{\sigma^2}{\tau^2}I+X^\top X)^{-1}X^\top y$ (15.49). With $\lambda=\sigma^2/\tau^2$ this is ridge regression, minimizing $\mathrm{RSS}(w)+\lambda\|w\|^2$ (15.50), where $\mathrm{RSS}=\frac12\|Xw-y\|_2^2$ (15.51) (p. 597; see Reading notes on the factor $\tfrac12$).

*Unknown noise variance.* Likelihood $\propto(\sigma^2)^{-N/2}\exp(-\frac1{2\sigma^2}\sum(y_n-w^\top x_n)^2)$ (15.52). The conjugate prior is $p(w\mid\sigma^2)=\mathcal N(w\mid\breve w,\sigma^2\breve\Sigma)$ (15.53), times an inverse gamma on $\sigma^2$:
$$\mathrm{IG}(\sigma^2\mid\breve a,\breve b)=\frac{\breve b^{\breve a}}{\Gamma(\breve a)}(\sigma^2)^{-(\breve a+1)}\exp(-\breve b/\sigma^2).\tag{15.54}$$
The product is the normal inverse gamma (NIG), $\mathrm{NIG}(w,\sigma^2\mid\breve w,\breve\Sigma,\breve a,\breve b)\triangleq\mathcal N(w\mid\breve w,\sigma^2\breve\Sigma)\mathrm{IG}(\sigma^2\mid\breve a,\breve b)$ (15.55–15.56). The posterior is NIG with
$$\hat w=\hat\Sigma(\breve\Sigma^{-1}\breve w+X^\top y),\ \hat\Sigma=(\breve\Sigma^{-1}+X^\top X)^{-1},\ \hat a=\breve a+N/2,$$
$$\hat b=\breve b+\tfrac12\big(\breve w^\top\breve\Sigma^{-1}\breve w+y^\top y-\hat w^\top\hat\Sigma^{-1}\hat w\big)\tag{15.57–15.61}$$
$\hat a$ updates counts. $\hat b$ is the prior sum of squares, plus the empirical sum of squares $y^\top y$, plus a term for the error in the prior on $w$ (p. 598). Marginals: $p(\sigma^2\mid\mathcal D)=\mathrm{IG}(\sigma^2\mid\hat a,\hat b)$ (15.62) and $p(w\mid\mathcal D)=\mathcal T(w\mid\hat w,\frac{\hat b}{\hat a}\hat\Sigma,2\hat a)$ (15.63) (p. 598).

*Posterior predictive (p. 599).* For $N'$ new inputs $\tilde X$:
$$p(\tilde y\mid\tilde X,\mathcal D)=\iint\mathcal N(\tilde y\mid\tilde Xw,\sigma^2I_{N'})\,\mathrm{NIG}(w,\sigma^2\mid\hat w,\hat\Sigma,\hat a,\hat b)\,dw\,d\sigma^2=\mathcal T\!\big(\tilde y\mid\tilde X\hat w,\tfrac{\hat b}{\hat a}(I_{N'}+\tilde X\hat\Sigma\tilde X^\top),2\hat a\big)\tag{15.64–15.66}$$
The mean equals ordinary regression with $\mathbb E[w\mid\mathcal D]$ plugged in. The variance has a noise part $\frac{\hat b}{\hat a}I_{N'}$ and a weight-uncertainty part $\frac{\hat b}{\hat a}\tilde X\hat\Sigma\tilde X^\top$, which depends on how close test inputs are to the training data. If a point estimate of $\sigma^2$ is plugged in and only $w$ is integrated out, the result is $\mathcal N(\tilde y\mid\tilde X\hat w,\hat\sigma^2I_{N'}+\tilde X\hat\Sigma\tilde X^\top)$, with narrower variance than the Student (p. 599).

*Intuition note.* The posterior mean is a precision-weighted compromise between prior mean and data. Predictive uncertainty is noise plus "how unsure am I about $w$ in the direction of this test input".

**15.2.3 Uninformative priors (pp. 599–600).**

*Jeffreys prior.* Jeffreys priors are $p(w)\propto1$ (location) and $p(\sigma)\propto\sigma^{-1}$ (scale). They can be emulated by an improper NIG with $\breve w=0$, $\breve\Sigma=\infty I$, $\breve a=-D/2$, $\breve b=0$. The posterior is NIG with
$$\hat w=\hat w_{\rm mle},\ \hat\Sigma=(X^\top X)^{-1}\triangleq C,\ \hat a=\nu/2,\ \hat b=s^2\nu/2,\ s^2=\|y-\hat y\|^2/\nu,\ \nu=N-D\tag{15.67–15.73}$$
So $p(w\mid\mathcal D)=\mathcal T(w\mid\hat w,s^2C,\nu)$ (15.74) and $p(w_d\mid\mathcal D)=\mathcal T(w_d\mid\hat w_d,s^2C_{dd},\nu)$ (15.75).

*Connection to frequentist statistics (p. 600).* This posterior is formally equivalent to the frequentist sampling distribution of the MLE, $p(\hat w_d\mid\mathcal D^*)=\mathcal T(\hat w_d\mid w_d,s^2C_{dd},\nu)$ (15.76). Here $\mathcal D^*=(X,y^*)$ is hypothetical data from the true model with fixed $X$. Equivalently $\frac{\hat w_d-w_d}{s\sqrt{C_{dd}}}\sim t_{N-D}$ (15.77). They are numerically the same because $\mathcal T(w\mid\mu,\sigma^2,\nu)=\mathcal T(\mu\mid w,\sigma^2,\nu)$, but semantically different: the sampling distribution does not condition on the observed data (p. 600).

*Zellner's g-prior (pp. 600–601).* An uninformative prior on $\sigma^2$ is often reasonable, but a flat prior on $w$ can be dangerous since prior strength controls regularization. Compromise: NIG with $\breve a=-D/2$, $\breve b=0$, $\breve w=0$, $\breve\Sigma=g(X^\top X)^{-1}$, $g>0$ analogous to $1/\lambda$ in ridge. Because the covariance is proportional to $(X^\top X)^{-1}$ rather than $I$, the posterior is invariant to rescaling the inputs. Posterior (15.78–15.82):
$$V_N=\tfrac g{g+1}(X^\top X)^{-1},\ w_N=\tfrac g{g+1}\hat w_{\rm mle},\ a_N=N/2,\ b_N=\tfrac{s^2}2+\tfrac1{2(g+1)}\hat w_{\rm mle}^\top X^\top X\hat w_{\rm mle}.$$
Ways to set $g$: cross-validation, empirical Bayes, hierarchical Bayes (p. 601). The prior conditions on $X$ but not $y$, which is valid in a conditional model (footnote, p. 600).

**15.2.4 Informative priors (pp. 601–603).** Example (from McE20): height $y_i$ (cm) from weight $x_i$ (kg), Kalahari foragers (Howell). Model $y_i\sim\mathcal N(\mu_i,\sigma)$, $\mu_i=\alpha+\beta(x_i-\bar x)$ (15.83–15.84); $\alpha$ is the prediction at mean weight. Priors, to be set before seeing data (p. 602):
- $\alpha\sim\mathcal N(178,20)$, i.e. 95% mass on $178\pm40$.
- A vague $\beta\sim\mathcal N(0,10)$ was tested by prior predictive samples (draw $(\alpha_s,\beta_s)\sim p(\alpha)p(\beta)$, plot lines). Fig. 15.1a shows it is poor: height is as likely to fall as rise with weight, and heights exceed the tallest person (272 cm) or fall below an embryo (0).
- Forcing $\beta>0$ with $\beta\sim\mathcal{LN}(0,1)$ (log-normal) is much more reasonable (Fig. 15.1b).
- For $\sigma$, McElreath uses $\mathrm{Unif}(0,50)$. An easier alternative is $\sigma\sim\mathrm{Expon}(\lambda)$ with $\mathbb E[\sigma]=1/\lambda$ set to the expected standard deviation, e.g. the empirical one.

These priors are not conjugate. A quadratic (Laplace) approximation suffices here (Fig. 15.1c) (p. 602). With children included, the relation is nonlinear (Fig. 15.2a). A quadratic term $\mu_i=\alpha+\beta_1x_i+\beta_2x_i^2$ (15.85) with a log-Gaussian prior on $\beta_2$ underfits: an inverted quadratic needs a negative coefficient, which the prior forbids ($\mathbb E[\beta_2\mid\mathcal D]\approx0.08$). A Gaussian prior on $\beta_2$ avoids this (Fig. 15.2). Lesson: think about the functional form when specifying priors (p. 603).

**15.2.5 Spike and slab (p. 603).** Sparse $w$ (many zeros) gives feature selection. The spike-and-slab prior is a two-component mixture per weight:
$$p(w)=\prod_{d=1}^D(1-\pi)\delta(w_d)+\pi\,\mathrm{Unif}(w_d\mid-a,a),\tag{15.86}$$
where $\pi$ is the prior probability of a non-zero coefficient. The log prior is $\|w\|_0\log(1-\pi)+(D-\|w\|_0)\log\pi=-\lambda\|w\|_0+\text{const}$ with $\lambda=\log\frac\pi{1-\pi}$ (15.87), as printed (see Reading notes). So MAP with this prior is $\ell_0$ regularization, and posterior samples are also sparse. By contrast, lasso (Laplace prior, MAP) is sparse but its posterior samples are not. [EY09] show theoretically, and [SPZ09] confirm experimentally, that the posterior mean under spike-and-slab predicts better than the posterior mode under a Laplace prior. In practice the slab is a broad Gaussian: $\prod_d(1-\pi)\delta(w_d)+\pi\mathcal N(w_d\mid0,\sigma_w^2)$ (15.88), implemented with binary indicators $s_d\sim\mathrm{Ber}(\pi)$. MAP and full inference with such discrete mixtures are computationally hard; approximations are greedy search or MCMC (p. 604).

**15.2.6 Laplace prior / Bayesian lasso (pp. 604–605).** Lasso is MAP under a Laplace prior: $\mathrm{PNLL}(w)=\|Xw-y\|_2^2+\lambda\|w\|_1+\text{const}$ (15.89). The Bayesian lasso assumes $p(w\mid\sigma^2)=\prod_j\frac{\gamma}{2\sqrt{\sigma^2}}e^{-\gamma|w_j|/\sqrt{\sigma^2}}$ (15.90). Conditioning on $\sigma^2$ ensures a unimodal full posterior. The Laplace is a Gaussian scale mixture:
$$\mathrm{Laplace}(w\mid0,\gamma)=\int\mathcal N(w\mid0,\tau^2)\,\mathrm{Ga}(\tau^2\mid1,\gamma^2/2)\,d\tau^2\tag{15.91}$$
This gives the hierarchical model (Fig. 15.3a), with joint $p(y,w,\tau,\sigma^2\mid X)=\mathcal N(y\mid Xw,\sigma^2I_N)\big[\prod_j\mathcal N(w_j\mid0,\sigma^2\tau_j^2)\mathrm{Ga}(\tau_j^2\mid1,\gamma^2/2)\big]p(\sigma^2)$ (15.92). The group lasso, which zeroes several coefficients together, uses $w_g\mid\sigma^2,\tau_g^2\sim\mathcal N(0,\sigma^2\tau_g^2I_{d_g})$, $\tau_g^2\sim\mathrm{Ga}(\frac{d_g+1}2,\frac{\gamma^2}2)$ (15.93–15.94). If $w_{1,1}$ is small, $\tau_1^2$ is estimated small, forcing $w_{1,2}$ small; if large, $w_{1,2}$ may be large (Fig. 15.3b) (p. 605). A Gibbs sampler is easy, but samples are not sparse even though the MAP is, because the prior gives infinitesimal probability to a coefficient being exactly zero (p. 605).

**15.2.7 Horseshoe prior (pp. 605–606).** Continuous prior that is both sparse and efficient (named for its density shape):
$$w_j\sim\mathcal N(0,\gamma_j^2\tau^2),\quad\gamma_j\sim\mathcal C_+(0,1),\quad\tau^2\sim\mathcal C_+(0,1)\tag{15.95–15.97}$$
($\mathcal C_+$ is half-Cauchy.) $\gamma_j$ is a local, $\tau$ a global shrinkage factor. Fat Cauchy tails make $w_j$ likely either near 0 or very far from 0, emulating spike-and-slab continuously (p. 606).

**15.2.8 Automatic relevancy determination (ARD) (pp. 606–608).** Use a Gaussian prior $w_j\sim\mathcal N(0,1/\alpha_j)$ and optimize precisions by empirical Bayes: $\hat\alpha=\arg\max_\alpha p(y\mid X,\alpha)$, then $\hat w$ given $\hat\alpha$. Perhaps surprisingly the result is sparse (also called sparse Bayesian learning, NUV estimation) (p. 606).

*15.2.8.1 ARD for linear models.* Likelihood $\mathcal N(y\mid w^\top x,1/\beta)$, $\beta=1/\sigma^2$; prior $\mathcal N(w\mid0,A^{-1})$, $A=\mathrm{diag}(\alpha)$. The marginal likelihood is
$$p(y\mid X,\alpha,\beta)=\int\mathcal N(y\mid Xw,\beta^{-1}I_N)\mathcal N(w\mid0,A^{-1})dw=\mathcal N(y\mid0,C_\alpha),\quad C_\alpha=\beta^{-1}I_N+XA^{-1}X^\top\tag{15.98–15.100}$$
This resembles the spike-and-slab marginal likelihood $\mathcal N(y\mid0,C_s)$ with $C_s=\sigma_y^2I_N+\sigma_w^2X_sX_s^\top$ (15.101), where $X_s$ keeps columns with $s_d=1$. The difference is that the binary $s_j$ are replaced by continuous $\alpha_j\in\mathbb R^+$, which eases optimization. Objective:
$$\ell(\alpha,\beta)=-2\log p(y\mid X,\alpha,\beta)=\log|C_\alpha|+y^\top C_\alpha^{-1}y\tag{15.102}$$
The ARD objective is not convex but tends to give much sparser results than $\ell_1$ [WW12]. It has many fewer local optima than the $\ell_0$ objective [WRN10] (p. 606).

*15.2.8.2 Why sparse? (pp. 607–608).* With $\hat\alpha,\hat\beta$: $p(w\mid\mathcal D,\hat\alpha,\hat\beta)=\mathcal N(\hat w,\hat\Sigma)$, $\hat\Sigma^{-1}=\hat\beta X^\top X+A$, $\hat w=\hat\beta\hat\Sigma X^\top y$. If $\hat\alpha_d\approx\infty$ then $\hat w_d\approx0$ (p. 607). Intuitive argument (after [Tip01], $\beta$ fixed): take 1-d regression with 2 examples, so $x$ and $y$ are vectors in the plane (Fig. 15.4). If the feature is irrelevant, $x$ is nearly orthogonal to $y$. Here $C_\alpha=\frac1\beta I+\frac1\alpha xx^\top$. For finite $\alpha$ the density is elongated along $x$; at $\alpha=\infty$ it is spherical. If $|C_\alpha|$ is held constant, the spherical one gives higher density to the observed $y$, so it is preferred. The marginal likelihood punishes small $\alpha_d$ with irrelevant $X_{:,d}$ because they waste probability mass, which is more parsimonious from the viewpoint of Bayesian Occam's razor (p. 607). Two further views:
- *Hierarchical/VB view* [BT00]: put $\alpha_d\sim\mathrm{Ga}(a,b)$ and $\beta\sim\mathrm{Ga}(c,d)$ and use variational Bayes with $q(w,\alpha)=q(w)q(\alpha)\approx\mathcal N(w\mid\mu,\Sigma)\prod_d\mathrm{Ga}(\alpha_d\mid\hat a_d,\hat b_d)$ (15.103). ARD approximates $q(\alpha)$ by a point estimate, whereas VB integrates $\alpha$ out. The resulting $q(w)=\int\mathcal N(w\mid0,\mathrm{diag}(\alpha)^{-1})\prod\mathrm{Ga}\,d\alpha$ (15.104) is a Gaussian scale mixture equal to a multivariate Student with non-diagonal covariance. The Student's large spike at 0 explains why its mean (equal to its mode) is sparse (p. 608).
- *MAP with a non-factorial prior* [WN07]: the dependence between $w_j$ arises because $\alpha_j$ is estimated after marginalizing all $w$. [WRN10] prove that MAP with non-factorial priors is strictly better than with any factorial prior in this sense: fewer local minima, while the global optimum still matches the $\ell_0$ global optimum. $\ell_1$ has no local minima but lacks the second property (p. 608).

*Intuition note.* ARD lets each feature "vote" on its own prior precision through the evidence. In the author's 2-example argument, an irrelevant feature spreads probability mass in a useless direction, so the evidence prefers a spherical density, i.e. switching the feature off.

*15.2.8.3 Algorithms (p. 608).* Options: EM (E step $p(w\mid\mathcal D,\alpha)$, M step maximize $\alpha$); variational Bayes for $w$ and $\alpha$; iteratively reweighted $\ell_1$ [WN10]. [HXW17] showed an RNN can emulate these nested iterations, with much faster convergence.

*15.2.8.4 Relevance vector machines (p. 608).* Take $p(y\mid x)=\mathcal N(y\mid w^\top\phi(x),\sigma^2)$ with $\phi(x)=[\mathcal K(x,x_1),\dots,\mathcal K(x,x_N)]$ (kernel basis expansion, $O(N)$ parameters). ARD then selects a small subset of exemplars: the relevance vector machine.

**15.2.9 Multivariate linear regression (pp. 608–610; section by Xinglong Li).** Model $Y=WX+E$ with $W\in\mathbb R^{N_y\times N_x}$, $X\in\mathbb R^{N_x\times N}$, $Y\in\mathbb R^{N_y\times N}$ (columns are observations), $E=[e_1,\dots,e_N]$, $e_i\overset{iid}\sim\mathcal N(0,\Sigma)$ (15.105). Likelihood:
$$p(Y\mid W,X,\Sigma)=\frac{\exp\!\big(-\tfrac12\mathrm{tr}[(Y-WX)^\top\Sigma^{-1}(Y-WX)]\big)}{(2\pi)^{N_y\times N}|\Sigma|^{N/2}}=\mathcal{MN}(Y\mid WX,\Sigma,I_{N\times N})\tag{15.106–15.108}$$
Conjugate prior: matrix normal inverse Wishart, $W,\Sigma\sim\mathrm{MNIW}(M_0,V_0,\nu_0,\Psi_0)$, i.e. $W\mid\Sigma\sim\mathcal{MN}(M_0,\Sigma,V_0)$ (printed with $\Sigma_0$) and $\Sigma\sim\mathrm{IW}(\nu_0,\Psi_0)$, with $V_0\in\mathbb R_{++}^{N_x\times N_x}$, $\Psi_0\in\mathbb R_{++}^{N_y\times N_y}$, $\nu_0>N_x-1$ (15.109–15.111). Joint density:
$$p(Y,W,\Sigma)\propto|\Sigma|^{-(\nu_0+N_y+1+N_x+N)/2}\exp\{-\tfrac12\mathrm{tr}(\Omega_0)\},$$
$$\Omega_0\triangleq\Psi_0\Sigma^{-1}+(Y-WX)^\top\Sigma^{-1}(Y-WX)+(W-M_0)^\top\Sigma^{-1}(W-M_0)V_0\tag{15.112–15.113}$$
Complete the square in $W$ (as in Section 3.4.4.3):
$$\mathrm{tr}[(Y-WX)^\top\Sigma^{-1}(Y-WX)+(W-M_0)^\top\Sigma^{-1}(W-M_0)V_0]=\mathrm{tr}(\Sigma^{-1}[(Y-WX)(Y-WX)^\top+(W-M_0)V_0(W-M_0)^\top])\tag{15.114–15.115}$$
$$=\mathrm{tr}(\Sigma^{-1}[WS_{xx}W^\top-2S_{yx}W^\top+S_{yy}])=\mathrm{tr}(\Sigma^{-1}[(W-S_{yx}S_{xx}^{-1})S_{xx}(W-S_{yx}S_{xx}^{-1})^\top+S_{y|x}])\tag{15.116–15.117}$$
with $S_{xx}=XX^\top+V_0$, $S_{yx}=YX^\top+M_0V_0$, $S_{yy}=YY^\top+M_0V_0M_0^\top$, $S_{y|x}=S_{yy}-S_{yx}S_{xx}^{-1}S_{yx}^\top$ (15.118–15.119). (Added step: expanding the two products gives cross terms $-YX^\top W^\top-WXY^\top-M_0V_0W^\top-WV_0M_0^\top$. Under the trace with symmetric $\Sigma^{-1}$ each pair gives $-2S_{yx}W^\top$.) Hence $W\mid\Sigma,X,Y\sim\mathcal{MN}(S_{yx}S_{xx}^{-1},\Sigma,S_{xx})$ (15.120) (p. 610). Integrating out $W$ leaves $\Sigma^{-1}\Psi_0$ and $\Sigma^{-1}S_{y|x}$ terms, so the posterior of $\Sigma$ is inverse Wishart with scale $\Psi_0+S_{y|x}$. Joint posterior:
$$\mathrm{MNIW}(M_1,V_1,\nu_1,\Psi_1):\ M_1=S_{yx}S_{xx}^{-1},\ V_1=S_{xx},\ \nu_1=N+\nu_0,\ \Psi_1=\Psi_0+S_{y|x}\tag{15.121–15.125}$$
MAP: $W$ appears only in the matrix-normal factor, so $\hat W=M_1=S_{yx}S_{xx}^{-1}$ for any $\Sigma$. Plugging in $\hat W$ and differentiating in $\Sigma$ gives the maximizer $(\nu_1+N_y+N_x+1)^{-1}\Psi_1$:
$$\hat W=S_{yx}S_{xx}^{-1},\qquad\hat\Sigma=\frac1{\nu_1+N_y+N_x+1}(\Psi_0+S_{y|x})\tag{15.126–15.127}$$

### 15.3 Logistic regression (pp. 610–620)
**15.3.1 Binary (pp. 610–611).** $p(y\mid x;\theta)=\mathrm{Ber}(y\mid\sigma(w^\top x+b))$, $\sigma(a)=1/(1+e^{-a})$ (15.128–15.129). With logits $\eta_n=w^\top x_n+b$, $\mu_n=\sigma(\eta_n)$, the log likelihood is a negative cross entropy:
$$\log p(\mathcal D\mid\theta)=\sum_n y_n\log\mu_n+(1-y_n)\log(1-\mu_n)\tag{15.130}$$
Using $\mu_n=\frac{e^{\eta_n}}{1+e^{\eta_n}}$, $1-\mu_n=\frac1{1+e^{\eta_n}}$ (15.131), this becomes $\sum_n y_n\eta_n-\sum_n\log(1+e^{\eta_n})$ (15.132–15.134). Implement $\log(1+e^a)$ as `np.log1p(np.exp(a))`.

**15.3.2 Multinomial (p. 611).** $p(y\mid x;\theta)=\mathrm{Cat}(y\mid\mathrm{softmax}(Wx+b))$, $W$ is $C\times D$, $b$ is $C$-dimensional, $\mathrm{softmax}(a)=[e^{a_c}/\sum_{c'}e^{a_{c'}}]_c$ (15.135–15.136). With $\eta_n=Wx_n+b$, $\mu_n=\mathrm{softmax}(\eta_n)$ and one-hot $y_n$: $\log p(\mathcal D\mid\theta)=\sum_n\sum_c y_{nc}\log\mu_{nc}$ (15.137).

**15.3.3 Class imbalance and the long tail (p. 612).** Maximum likelihood minimizes (a bound on) the 0-1 loss, which can be dominated by frequent classes. Alternative: balanced error rate
$$\mathrm{BER}(f)=\frac1C\sum_{y=1}^C p^*_{x|y}\big(y\notin\arg\max_{y'}f_{y'}(x)\big)\tag{15.138}$$
The optimal $f^*$ satisfies $\arg\max_yf^*_y(x)=\arg\max_yp^*_{\rm bal}(y\mid x)=\arg\max_yp^*(x\mid y)$ with $p^*_{\rm bal}(y\mid x)\propto\frac1Cp^*(x\mid y)$ (15.139). So we should use the class-conditional likelihood $p(x\mid y)$, not the posterior $p(y\mid x)$. *Logit adjustment* [Men+21] achieves this. With logits $f_y(x)=w_y^\top\phi(x)$, post-hoc training is normal and prediction uses
$$\arg\max_yp(x\mid y)=\arg\max_y\frac{p(y\mid x)p(x)}{p(y)}=\arg\max_y\frac{\exp(w_y^\top\phi(x))}{\pi_y}\tag{15.140}$$
with $\pi_y=p(y)$ the empirical label prior. (Added step: the softmax normalizer and $p(x)$ do not depend on $y$ and drop out.) In practice add a tuning parameter $\tau>0$: $\hat f(x)=\arg\max_yf_y(x)-\tau\log\pi_y$ (15.141). Alternatively train with the logit-adjusted loss
$$\ell(y,f(x))=-\log\frac{e^{f_y(x)+\tau\log\pi_y}}{\sum_{y'}e^{f_{y'}(x)+\tau\log\pi_{y'}}}\tag{15.142}$$
(training $g_y=f_y+\tau\log\pi_y$, testing with $g_y-\tau\log\pi_y$). It can be combined with a prior (generalized Bayesian inference, Section 14.1.3).

**15.3.4 Parameter priors (p. 613).** Gaussian priors with mean 0 are standard (output may go up or down). Large variance is a bad idea. Offset-only model: $p(y\mid\theta)=\mathrm{Ber}(y\mid\sigma(\alpha))$, $p(\alpha)=\mathcal N(\alpha\mid0,\omega)$ (15.143–15.144). With $\omega=10$ the implied prior on $\sigma(\alpha)$ is extreme, with most density near 0 or 1; with $\omega=1.5$ it is flatter (Fig. 15.5a). With features, the logit magnitude depends on the number and distribution of inputs. Experiment: $x_{nd}\sim\mathrm{Ber}(0.8)$, $\beta\sim\mathcal N(0,1.5I)$, $p(y_n=1\mid x_n)=\sigma(\beta^\top x_n)$. Sample $\beta$ and labels, and look at the fraction of positive labels $f_s$. As $D$ grows, the induced prior is initially flat but becomes skewed to 0 and 1 (Fig. 15.5b). Remedy: standardize inputs and scale the prior variance by $1/\sqrt D$ (as printed). Heavier-tailed priors (Cauchy, Student) are another option.

*Intuition note.* A prior that looks "uninformative" on the logit scale is very informative on the probability scale. Always look at what the prior implies for outcomes.

**15.3.5 Laplace approximation (pp. 613–615).** No conjugate prior exists, so approximate. The Laplace approximation is a Gaussian centred at the MAP with covariance the inverse Hessian at the MAP:
$$p(w\mid\mathcal D)\approx\mathcal N(w\mid\hat w,H^{-1}),\ \hat w=\arg\min-\log p(w,\mathcal D),\ H=-\nabla_w^2\log p(w,\mathcal D)|_{\hat w}\tag{15.145}$$
Example (Fig. 15.6): separable 2-d data. Four separating lines correspond to $w_1=(3,1)$, $w_2=(4,2)$, $w_3=(5,3)$, $w_4=(7,3)$, with norms 3.16, 4.47, 5.83, 7.62, all roughly in the MLE direction. The unconstrained MLE has $\|w\|=\infty$. To get a unique solution, use $\mathcal N(w\mid0,\sigma^2I)$. As printed: $\sigma^2=\infty$ forces MAP $w=0$ (all predictions $0.5$), and $\sigma^2=0$ gives the MLE (see Reading notes). The author picks $\sigma^2=100$. The Laplace approximation (Fig. 15.6d) has the right mode but a somewhat distorted shape. Its SW–NE axis captures uncertainty in the magnitude of $w$, and its SE–NW axis captures uncertainty in the boundary orientation (p. 615).

**15.3.6 Posterior predictive (pp. 615–617).** $p(y\mid x,\mathcal D)=\int p(y\mid x,w)p(w\mid\mathcal D)dw$ (15.146). Monte Carlo: $p(y=1\mid x,\mathcal D)\approx\frac1S\sum_s\sigma(w_s^\top x)$ with $w_s\sim p(w\mid\mathcal D)$ (15.147). Deterministic alternative: if $p(w\mid\mathcal D)=\mathcal N(\mu,\Sigma)$, the logits $f_*$ are Gaussian, $\mathcal N(f_*\mid\mu^\top x_*,x_*^\top\Sigma x_*)\triangleq\mathcal N(\mu_*,\Sigma_*)$ (15.148). Approximating the sigmoid by the probit $\Phi$ allows an analytic integral, the *probit approximation* [SL90]:
$$p(y_*\mid x_*)\approx\int\Phi(f_*)\mathcal N(f_*\mid\mu_*,\sigma_*^2)df_*=\sigma\!\Big(\frac{\mu_*}{\sqrt{1+\frac\pi8\sigma_*^2}}\Big)\tag{15.149}$$
The multiclass generalized probit approximation [Gib97] is $\mathrm{softmax}\big(\{\mu_{*,c}/\sqrt{1+\frac\pi8\Sigma_{*,cc}}\}\big)$ (15.150). It ignores logit correlations (uses only diagonal entries) but can work well, even for neural nets. The Laplace bridge is in Section 17.3.10.2. In Fig. 15.7, the MAP plug-in shows no uncertainty about the boundary location. Sampled boundaries show large uncertainty in orientation. Their average (MC) shows uncertainty "splaying out" away from the data, and the probit approximation is very similar (pp. 616–617).

*Intuition note.* Dividing the logit mean by $\sqrt{1+\frac\pi8\sigma_*^2}$ pulls predictions toward 0.5 when the logit is uncertain. This is "moderated output": less confident where weight uncertainty is large.

**15.3.7 MCMC (pp. 617–618).** MCMC makes no assumption about the posterior form; samples give $q(\theta\mid\mathcal D)\approx\frac1S\sum_s\delta(\theta-\theta^s)$ (15.151), which can be plugged into (15.147). Example with HMC: iris data, two features (sepal length, width), two classes (text: Virginica vs non-Virginica; the Fig. 15.8 caption says setosa vs versicolor). The boundary is the line $x_2^*=-\frac b{w_2}+(-\frac{w_1}{w_2})x_1^*$ (15.152); sampling $(w_1,w_2,b)$ gives a posterior over boundaries (Fig. 15.8a: mean line and 95% credible band, wider away from the data). With imbalanced classes (Fig. 15.8b) uncertainty increases and the posterior mean boundary shifts toward the class with less data. The author links this to linear discriminant analysis, where changing the class prior moves the boundary so more of the input space goes to the a-priori more likely class (p. 618).

**15.3.8 Other methods (p. 618).** Variational inference: choose $q(w;\psi)$ and maximize the ELBO (making KL small), via a stochastic ELBO estimate, conditionally conjugate VI, or a local quadratic bound on the logistic function. For online data, assumed density filtering recursively gives a Gaussian $p(w\mid\mathcal D_{1:t})$.

**15.3.9 Case study: Berkeley admissions (pp. 618–620).** Data from [BHO75]: 6 departments (A–F) × 2 genders (Table 15.1, 12 rows), total $N=4526$ applicants. Question: does gender "cause" imbalanced admission rates?

*Model 1 (asymmetric).* $A_i\sim\mathrm{Bin}(N_i,\mu_i)$, $\mathrm{logit}(\mu_i)=\alpha+\beta\,\mathrm{MALE}[i]$, $\alpha\sim\mathcal N(0,10)$, $\beta\sim\mathcal N(0,1.5)$ (15.153–15.156). It is asymmetric (male log odds have two random variables, so are more uncertain a priori). *Symmetric version:* $\mathrm{logit}(\mu_i)=\alpha_{\rm GENDER[i]}$, $\alpha_j\sim\mathcal N(0,1.5)$ (15.157–15.159). With HMC, the 89% credible interval is $[-0.29,0.16]$ for $\alpha_1$ (male) and $[-0.91,0.75]$ for $\alpha_2$ (female), as printed. The difference $\sigma(\alpha_1)-\sigma(\alpha_2)$ has interval $[0.12,0.16]$, mean 0.14. This suggests Berkeley favours men (p. 619). A footnote says McElreath uses 89% to stress arbitrariness of such cut-offs.

*Model check.* The posterior predictive (Fig. 15.9a) fits badly. Empirical admission rates for women are higher in all departments except C and E, yet the model says women have 14% lower chance. The reason: women applied more to departments with low admission rates (e.g. F) and less to those with high rates (A, B). So overall fewer women are accepted, but within departments rates are about equal (p. 619).

*Model 2 (add department).* The DAG in Fig. 15.10a has $G\to D\to A$ and $G\to A$. To estimate the direct effect $G\to A$, condition on $D$ to close the indirect path:
$$\mathrm{logit}(\mu_i)=\alpha_{\rm GENDER[i]}+\gamma_{\rm DEPT[i]},\quad\alpha_j\sim\mathcal N(0,1.5),\ \gamma_k\sim\mathcal N(0,1.5),\ k=1..6\tag{15.160–15.163}$$
Fit is much better (Fig. 15.9b). The 89% intervals are $\alpha_1\in[-1.38,0.35]$, $\alpha_2\in[-1.31,0.42]$, and $\sigma(\alpha_1)-\sigma(\alpha_2)\in[-0.05,0.01]$: apparently no bias. *Caveat:* if an unobserved confounder $U$ (e.g. academic ability) affects both $D$ and $A$ (Fig. 15.10b), conditioning on the collider $D$ opens the non-causal path $G\to D\leftarrow U\to A$, invalidating causal conclusions. The example is a cautionary tale on drawing causal conclusions from predictive models (p. 620; see Chapter 36).

### 15.4 Probit regression (pp. 621–625)
Probit regression uses $\mu_n=\Phi(a_n)$, $a_n=w^\top x_n$, with link $a_n=\Phi^{-1}(\mu_n)$ (the probit function). $\Phi$ is close to the logistic (Fig. 15.11, $\Phi(\lambda x)$ with $\lambda=\sqrt{\pi/8}$, chosen so derivatives match at 0), so the two behave similarly. Probit has a latent-variable reading (from choice theory in economics) and simplifies Bayesian inference (p. 621).

**15.4.1 Latent variable interpretation (p. 622).** Let $z_n=w^\top x_n+\epsilon_n$, $\epsilon_n\sim\mathcal N(0,1)$, and $y_n=\mathbb I(z_n\ge0)$ (15.164). Marginalizing $z_n$:
$$p(y_n=1\mid x_n,w)=\int\mathbb I(z_n\ge0)\mathcal N(z_n\mid w^\top x_n,1)dz_n=p(\epsilon_n\ge-w^\top x_n)=1-\Phi(-w^\top x_n)=\Phi(w^\top x_n)\tag{15.165–15.167}$$
So probit is a threshold function applied to noisy input. Logistic regression is the same with logistic noise, density $f(y\mid\mu,s)=\frac{e^{-(y-\mu)/s}}{s(1+e^{-(y-\mu)/s})^2}$ (15.168), variance $s^2\pi^2/3$, cdf $F=\frac1{1+e^{-(y-\mu)/s}}$ (15.169). $\mu=0,s=1$ recovers logistic regression. Gaussian noise is computationally easier.

**15.4.2 MLE (pp. 622–623).**
- *SGD.* With $\mu_n=w^\top x_n$ and $\tilde y_n\in\{-1,+1\}$:
$$g_n=x_n\frac{\tilde y_n\phi(\mu_n)}{\Phi(\tilde y_n\mu_n)},\quad H_n=-x_n\Big(\frac{\phi(\mu_n)^2}{\Phi(\tilde y_n\mu_n)^2}+\frac{\tilde y_n\mu_n\phi(\mu_n)}{\Phi(\tilde y_n\mu_n)}\Big)x_n^\top\tag{15.170–15.171}$$
where $\phi$ is the standard normal pdf.
- *EM.* Complete-data log likelihood with a $\mathcal N(0,V_0)$ prior on $w$: $\ell(z,w\mid V_0)=\sum_n\log p(y_n\mid z_n)-\frac12(z-Xw)^\top(z-Xw)-\frac12w^\top V_0^{-1}w$ (15.172–15.173). The E-step posterior is a truncated Gaussian: $\mathcal N(z_n\mid w^\top x_n,1)\mathbb I(z_n>0)$ if $y_n=1$, with $\mathbb I(z_n<0)$ if $y_n=0$ (15.174). Since $w$ depends linearly on $z$, only the mean is needed:
$$\mathbb E[z_n\mid w,x_n]=\begin{cases}\mu_n+\frac{\phi(\mu_n)}{1-\Phi(-\mu_n)}=\mu_n+\frac{\phi(\mu_n)}{\Phi(\mu_n)}&y_n=1\\ \mu_n-\frac{\phi(\mu_n)}{\Phi(-\mu_n)}=\mu_n-\frac{\phi(\mu_n)}{1-\Phi(\mu_n)}&y_n=0\end{cases}\tag{15.175}$$
The M step is ridge regression on $\mu=\mathbb E[z]$: $\hat w=(V_0^{-1}+X^\top X)^{-1}X^\top\mu$ (15.176). EM is simple but can be much slower than direct gradient methods (Fig. 15.12), because the E-step posterior entropy is high: we only learn the sign of $z$, not its magnitude. A stronger regularizer or data augmentation can speed it up (p. 623).

**15.4.3 Bayesian inference (p. 624).** Gibbs sampling with auxiliary $z$ makes the model conjugate linear-Gaussian. Full conditional of $z_i$: the truncated Gaussian (15.177). A truncated $\mathcal N(\mu,\sigma)$ on $[a,b]$ can be sampled by drawing $u\sim U(\Phi(\frac{a-\mu}\sigma),\Phi(\frac{b-\mu}\sigma))$ and setting $z=\mu+\sigma\Phi^{-1}(u)$. Full conditional of the weights: $\mathcal N(w_N,V_N)$ with $V_N=(V_0^{-1}+X^\top X)^{-1}$, $w_N=V_N(V_0^{-1}w_0+X^\top z)$ (15.178–15.180). Variational Bayes is typically much faster.

**15.4.4 Ordinal probit (p. 624).** For ordered outputs (low/medium/high) with $C$ values, use $C+1$ thresholds: $y_n=j$ if $\gamma_{j-1}<z_n\le\gamma_j$ (15.181), with $\gamma_0\le\dots\le\gamma_C$ and, for identifiability, $\gamma_0=-\infty$, $\gamma_1=0$, $\gamma_C=\infty$. $C=2$ gives binary probit. For $C=3$ the intervals are $(-\infty,0],(0,\gamma_2],(\gamma_2,\infty)$, and $\gamma_2$ is tuned to match class frequencies. MLE is trickier (must also optimize ordered $\gamma$; an EM approach exists); a simple Gibbs sampler exists.

**15.4.5 Multinomial probit (p. 625).** For unordered $y_n\in\{1..C\}$: $z_{nc}=w_c^\top x_{nc}+\epsilon_{nc}$, $\epsilon\sim\mathcal N(0,R)$, $y_n=\arg\max_cz_{nc}$ (15.182–15.184). If instead $y_{nc}=\mathbb I(z_{nc}>0)$, this is *multivariate probit*, modelling $C$ correlated binary outcomes.

### 15.5 Multilevel (hierarchical) GLMs (pp. 625–629)
With $J$ related datasets $\mathcal D_j$ there are three options (p. 625): fit $J$ separate models (may overfit small $\mathcal D_j$); pool everything (may underfit); or fit a hierarchical Bayesian (multilevel, partially pooled) model, where each group has $\theta^j$ drawn from a shared prior $p(\theta^0)$:
$$p(\theta^{0:J},\mathcal D)=p(\theta^0)\prod_{j=1}^J\Big[p(\theta^j\mid\theta^0)\prod_{n=1}^{N_j}p(y_n^j\mid x_n^j,\theta^j)\Big]\tag{15.185}$$
Fig. 15.13a uses nested plates. Fig. 15.13b uses a group indicator $g_n\in\{1..J\}$: $p(\theta^{0:J},\mathcal D)=p(\theta^0)[\prod_jp(\theta^j\mid\theta^0)][\prod_np(y_n\mid x_n,g_n,\theta)]$ with $p(y_n\mid x_n,g_n,\theta)=\prod_jp(y_n\mid x_n,\theta^j)^{\mathbb I(g_n=j)}$ (15.186–15.187). With a GLM likelihood this is a hierarchical GLM (p. 626).

**15.5.1 GLMMs (p. 626).** If $p(\theta^j\mid\theta^0)=\mathcal N(\theta^j\mid\theta^0,\Sigma^j)$ and the likelihood is a GLM, then $p(y_n\mid x_n,g_n=j,\theta)=p(y_n\mid\ell(\eta_n))$ with
$$\eta_n=x_n^\top\theta^j=x_n^\top(\theta^0+\epsilon^j)=x_n^\top\theta^0+x_n^\top\epsilon^j,\quad\epsilon^j\sim\mathcal N(0,\Sigma)\tag{15.188–15.189}$$
This is a generalized linear mixed model. The shared $\theta^0$ are *fixed effects*; the group offsets $\epsilon^j$ are *random effects* (definitions of these terms vary; footnote 3). Random effects model group-specific deviations and are correlated, capturing dependencies a standard GLM would not. Fit with the methods of 15.1.4.

**15.5.2 Radon regression (pp. 626–629).** Simplified radon example [Gel+14a, Sec 9.4]: predict log radon level from county (categorical) and a binary floor feature, in $J=85$ Minnesota counties with 2–80 measurements each. Likelihood: $p(y_n\mid x_n,g_n=j,\theta)=\mathcal N(y_n\mid\alpha_j+\beta_jx_n,\sigma_y^2)$ (15.190), with $x_n\in\{0,1\}$ for basement (level 0) or above ground (level 1). Hierarchical prior $\alpha_j\sim\mathcal N(\mu_\alpha,\sigma_\alpha^2)$, $\beta_j\sim\mathcal N(\mu_\beta,\sigma_\beta^2)$; weak priors $\mu_\alpha,\mu_\beta\sim\mathcal N(0,1)$, $\sigma_\alpha,\sigma_\beta,\sigma_y\sim\mathcal C_+(1)$ (Fig. 15.14, p. 627).
- *Posterior (Figs. 15.15–15.16).* $\mu_\beta$ is close to $-0.6$ with high probability, supporting the suspicion that $x=1$ lowers radon. The $\alpha_j$ vary a lot across counties. Hierarchical predictions are more consistent across counties and work even when a county has no examples of some feature combination (e.g. no basement-free houses in Cass county). Posterior-predictive RMSE: 0.13 for the non-hierarchical model, 0.08 for the hierarchical (p. 627).
- *Non-centered parameterization (pp. 628–629).* Hierarchical parameters are often strongly correlated, which hurts inference. Plotting $p(\beta_j,\sigma_\beta\mid\mathcal D)$ gives Neal's funnel (Fig. 15.17a): large $\sigma_\beta$ lets $\beta_j$ vary widely (top), small $\sigma_\beta$ pins $\beta_j$ near $\mu_\beta$ (narrow bottom). Sampling algorithms struggle at the bottom; the marginal posterior of $\sigma_\beta$ excludes $[0,0.1]$, ruling out shrinking $\beta_j$ to 0. Fix: replace $\beta_j\sim\mathcal N(\mu_\beta,\sigma_\beta^2)$ by $\beta_j=\mu_\beta+\tilde\beta_j\sigma_\beta$ with $\tilde\beta_j\sim\mathcal N(0,1)$. Correlation between $\tilde\beta_j$ and $\sigma_\beta$ is much smaller (Fig. 15.17b); see Section 12.6.5.

*Intuition note.* The author uses a hierarchical prior because some counties have very few datapoints, and the hierarchical model fits better (RMSE 0.08 vs 0.13). Non-centering writes $\beta_j$ as $\mu_\beta+\tilde\beta_j\sigma_\beta$ with a standard-normal $\tilde\beta_j$, and the correlation with $\sigma_\beta$ is then much smaller (p. 629).

## Toy example (ours; not from the text)
Binomial regression (15.10–15.17) with a bias and one binary feature, $N_n=10$ trials each. Data: $x=0$: $y=3$ successes; $x=1$: $y=6$. Features $\phi_n=(1,x_n)$, $w=(w_0,w_1)$, $\eta_n=w^\top\phi_n$.

1. At $w=(0,0)$: $\eta_n=0$, $\mu_n=\sigma(0)=0.5$, $\mathbb E[y_n]=N\mu=5$, $\mathbb V[y_n]=10\cdot0.5\cdot0.5=2.5$.
2. Gradient of the log likelihood (15.35, with $A'=N\mu$): $g=\sum_n(y_n-N\mu_n)\phi_n=(3-5)(1,0)+(6-5)(1,1)=(-2,0)+(1,1)=(-1,1)$.
3. Hessian of NLL (15.38, with weight $\mathbb V[y_n]$): $H=2.5\begin{pmatrix}1&0\\0&0\end{pmatrix}+2.5\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}5&2.5\\2.5&2.5\end{pmatrix}$. Its determinant is $12.5-6.25=6.25>0$ with positive diagonal, so it is positive definite and the NLL is convex.
4. Newton step (one IRLS step): $H^{-1}=\frac1{6.25}\begin{pmatrix}2.5&-2.5\\-2.5&5\end{pmatrix}=\begin{pmatrix}0.4&-0.4\\-0.4&0.8\end{pmatrix}$, so $w^{(1)}=0+H^{-1}g=(0.4(-1)-0.4(1),\ -0.4(-1)+0.8(1))=(-0.8,\ 1.2)$.
5. Exact MLE: the model is saturated, so $\sigma(w_0)=0.3$ and $\sigma(w_0+w_1)=0.6$. Then $w_0=\ln(3/7)\approx-0.847$ and $w_0+w_1=\ln(6/4)\approx0.405$, so $w_1\approx1.253$. One Newton step $(-0.8,1.2)$ is already close.

## Concepts
- [[generalized-linear-model]] (new) — conditional exponential family with natural parameter $w^\top x$ and mean $\ell^{-1}(\eta)$ (p. 591)
- [[link-function]] (new) — $\ell$ with $\ell(\mu)=w^\top x$; canonical link makes $\ell(\mu)=$ natural parameter (pp. 591, 594)
- [[conjugate-prior]] — Gaussian (known $\sigma^2$) and NIG (unknown $\sigma^2$) priors give closed-form linear-regression posteriors (pp. 597–598)
- [[normal-inverse-gamma-prior]] (new) — joint conjugate prior $\mathcal N(w\mid\breve w,\sigma^2\breve\Sigma)\mathrm{IG}(\sigma^2\mid\breve a,\breve b)$ (p. 598)
- [[g-prior]] (new) — prior covariance $g(X^\top X)^{-1}$; posterior invariant to input scaling (p. 600)
- [[prior-predictive-check]] — simulate regression lines/outcomes from the prior to judge it (p. 602)
- [[posterior-predictive-distribution]] — Student for NIG linear regression; MC or probit-moderated for logistic (pp. 599, 615)
- [[spike-and-slab-prior]] (new) — mixture of a point mass at 0 and a broad slab; MAP equals $\ell_0$ penalty (p. 603)
- [[bayesian-lasso]] (new) — Laplace prior as Gaussian scale mixture; MAP sparse, samples not (pp. 604–605)
- [[horseshoe-prior]] (new) — Gaussian scale mixture with half-Cauchy local/global scales (p. 605)
- [[automatic-relevance-determination]] (new) — empirical-Bayes per-weight precisions; sparse via marginal likelihood (p. 606)
- [[bayesian-occams-razor]] — evidence penalizes irrelevant features that waste probability mass (p. 607)
- [[marginal-likelihood]] — $\mathcal N(y\mid0,C_\alpha)$, the ARD objective (p. 606)
- [[laplace-approximation]] (new) — Gaussian at the MAP with inverse-Hessian covariance (p. 614)
- [[probit-approximation]] (new) — $\sigma(\mu_*/\sqrt{1+\pi\sigma_*^2/8})$ for Gaussian logits (p. 615)
- [[logit-adjustment]] (new) — subtract $\tau\log\pi_y$ from logits to target balanced error (p. 612)
- [[probit-regression]] (new) — thresholded latent Gaussian; gives EM and Gibbs samplers (pp. 621–624)
- [[gibbs-sampling]] — alternate truncated-normal $z$ and Gaussian $w$ draws (p. 624)
- [[hierarchical-model]] — group parameters drawn from a shared prior (p. 625)
- [[partial-pooling]] — compromise between separate and pooled fits (p. 625)
- [[glmm]] (new) — fixed effects $\theta^0$ plus correlated random effects $\epsilon^j$ (p. 626)
- [[non-centered-parameterization]] (new) — $\beta_j=\mu_\beta+\tilde\beta_j\sigma_\beta$ to avoid Neal's funnel (p. 629)
- [[fork-chain-collider]] — conditioning on collider $D$ opens $G\to D\leftarrow U\to A$ (p. 620)
- [[causal-dag]] — Fig. 15.10 models of admissions (p. 620)
- [[credible-interval]] — 89%/95% intervals for weights and differences (pp. 602, 619)

## Canonical instances
- [[kalahari-height-weight]] (new) — prior predictive checking of slope priors; log-normal vs Gaussian $\beta_2$ (pp. 601–603)
- [[berkeley-admissions]] (new) — gender-only model suggests bias; department conditioning makes the apparent bias disappear ("it seems", p. 620); hidden confounder caveat (pp. 618–620)
- [[minnesota-radon]] (new) — hierarchical regression over 85 counties; Neal's funnel and non-centering (pp. 626–629)
- [[iris-logistic-hmc]] (new) — posterior over decision boundaries; imbalance shifts the boundary (pp. 617–618)
- [[separable-2d-logistic-laplace]] (new) — Laplace approximation, MC vs probit predictive (pp. 614–616)

## Bridges (candidates)
- [same-math] Gaussian prior MAP in linear regression ↔ ridge regression: $\lambda=\sigma^2/\tau^2$ in (15.49–15.50), up to the factor-of-2 noted in Reading notes.
- [same-math] Spike-and-slab MAP ↔ $\ell_0$ regularization: log prior $=-\lambda\|w\|_0$ + const (15.87).
- [structural-analogy] ARD evidence maximization ↔ Bayesian Occam's razor: irrelevant features waste predictive mass.
- [structural-analogy] Berkeley admissions ↔ Simpson's paradox / collider bias: the aggregate rate and the within-department rates disagree, and conditioning on $D$ is valid only if no hidden confounder exists.
- [structural-analogy] Probit latent-variable model ↔ economic choice theory: threshold on a latent utility plus noise (p. 621).
- [structural-analogy] Neal's funnel ↔ sampler geometry problems: sampling algorithms struggle at the narrow bottom of the funnel (p. 628).
- [metaphor] Logit adjustment ↔ Bayes' rule with changed priors: dividing by $\pi_y$ removes the label prior.

## Questions this raises
- When the true noise is not Gaussian or the link is wrong, how reliable are the Student/NIG results, and how does posterior predictive checking (as done for Berkeley) generalize?
- How much does ARD's sparsity depend on the Gaussian scale-mixture structure versus the empirical-Bayes point estimate of $\alpha$?
- How does the Laplace approximation behave when the posterior is strongly skewed, e.g. with separable data and a weak prior?
- Which causal assumptions (beyond the DAG in Fig. 15.10) would let the department-adjusted Berkeley estimate be read causally?

## Reading notes
- Printed page numbers are visible on every page except the blank last one. Printed = pdf − 34 (pdf 625 = p. 591). Source pdf 664 (printed 630) is blank. Even-numbered pages carry the footer "Online version. December 10, 2025"; odd-numbered pages carry an author/licence line.
- Eq. (15.50)–(15.51): RSS carries a factor $\tfrac12$, yet the ridge equivalence is stated with $\lambda=\sigma^2/\tau^2$. By my own check, minimizing $\tfrac12\|Xw-y\|^2+\lambda\|w\|^2$ gives $(2\lambda I+X^\top X)^{-1}X^\top y$, so the match to (15.49) seems to need $\lambda=\sigma^2/(2\tau^2)$ or an RSS without $\tfrac12$.
- Eq. (15.87): with $\pi$ defined as the probability of a non-zero coefficient (15.86), the log prior would be $\|w\|_0\log\pi+(D-\|w\|_0)\log(1-\pi)$. The printed expression has $\pi$ and $1-\pi$ swapped, so $\lambda$ would be $\log\frac{1-\pi}\pi$ by my check. I report it as printed.
- Section 15.3.5: "σ² = ∞ forces MAP $w=0$; σ² = 0 gives the MLE" is, by my check, reversed for a $\mathcal N(0,\sigma^2I)$ prior (large variance approaches the MLE; zero variance forces $w=0$). Reported as printed.
- (15.81) $a_N=N/2$ does not follow from (15.60) with $\breve a=-D/2$ ($\hat a=(N-D)/2$ in the Jeffreys case, 15.70); (15.82) has $s^2/2$ where (15.71) has $s^2\nu/2$. Reported as printed; $s^2$ is not defined for the $g$-prior case.
- Eq. (15.113) adds matrices of different sizes ($N_y\times N_y$, $N\times N$, $N_x\times N_x$); the trace manipulation (15.114–15.115) makes sense as a sum of traces. (15.110) prints $\Sigma_0$ where $\Sigma$ is presumably meant.
- Text says "where $\gamma\propto\gamma$" after (15.90) and writes $\tau^2\sim\mathcal C_+(0,1)$ in (15.97); both look like small misprints. The text calls the gamma variable a "precision" for (15.91) though it multiplies the variance $\tau^2$.
- Fig. 15.5a legend says "variance=1.50/10.00", while the text uses $\mathcal N(0,\omega)$ and the panel titles in 15.5b say "std=1.50". Whether $\omega$ is variance or standard deviation is not clear from the pages.
- Text in 15.3.7 describes Virginica vs non-Virginica for iris; Fig. 15.8's caption says setosa vs versicolor.
- Berkeley: the printed 89% interval for $\alpha_2$ ($[-0.91,0.75]$) is much wider than that for $\alpha_1$ and sits oddly beside the narrow difference interval; reported as printed.
- (15.175) last line has $\Phi(\mu_i)$ (index $i$) where $\mu_n$ is meant. "Positive definite" in 15.1.3 is stated without a rank condition on the inputs, and the parenthetical reads "$f(\eta_n)>0$" where $f'$ seems meant.
- The text-layer symbols for hats/breves in Section 15.2 were garbled; I used the page images (breve = prior, hat = posterior).
