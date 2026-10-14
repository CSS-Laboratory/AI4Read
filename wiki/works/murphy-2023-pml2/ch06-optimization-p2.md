---
id: murphy-2023-pml2/ch06-optimization-p2
work: murphy-2023-pml2
unit: "6 Optimization (part 2/3): §6.5 Bound optimization (MM), §6.6 Bayesian optimization, §6.7 Derivative-free optimization (up to §6.7.6.3)"
pages: 287–313
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Optimization, part 2: bound optimization (MM/EM), Bayesian optimization, derivative-free optimization

## L0 — One line
When the true objective is hard to optimize directly, optimize something easier instead: a lower bound that is refitted each step (MM, EM), a probabilistic surrogate of an expensive function (Bayesian optimization), or a search over candidates or distributions that needs only function values (derivative-free methods).

## L1 — The gist (≤ 120 words)
This part of Chapter 6 presents optimization strategies beyond plain gradient descent. Bound optimization (MM) maximizes a surrogate lower bound that touches the objective at the current point, so the objective can never decrease. EM (expectation maximization) is the main example of MM in this part. It is worked out for missing Gaussian data and for robust regression with a Student likelihood. Bayesian optimization builds a probabilistic surrogate of an expensive black-box function and chooses queries with an acquisition function. Derivative-free methods need only function values: local search, random search, evolutionary algorithms, estimation-of-distribution methods, the cross-entropy method and evolution strategies. The part stops inside §6.7.6.3.

**Prerequisites:** Hessians and negative definiteness; Jensen's inequality; KL divergence and entropy; Gaussian conditioning; exponential-family sufficient statistics; basic Gaussian-process idea; expectation and argmax; score-function (REINFORCE) gradient.

## L2 — Key ideas
- **MM (minorize-maximize) principle.** A surrogate $Q(\theta,\theta^t)\le\ell(\theta)$ that is tight at $\theta^t$, maximized each step, gives monotonically increasing $\ell$. Non-monotone behaviour therefore signals a bug in math or code (p. 287).
- **Fixed curvature bound.** For concave $\ell$ with $\mathbf H\succ\mathbf B$, the update $\theta^{t+1}=\theta^t-\mathbf B^{-1}g$ is Newton-like but uses a constant matrix. In binary logistic regression $\mathbf B=-\tfrac14\mathbf X^\top\mathbf X$, whose inverse $(\mathbf X^\top\mathbf X)^{-1}$ can be precomputed (pp. 288–289).
- **EM is MM.** In EM (expectation maximization), Jensen's inequality gives the ELBO (evidence lower bound). The E step sets $q_n$ to the posterior and makes the bound tight. The M step maximizes the expected complete-data log likelihood. For exponential families, only expected sufficient statistics are needed (pp. 290–291).
- **EM in practice.** For a multivariate normal (MVN) with missing data, plug expected sufficient statistics (not expected values) into the MLE formulas. For Student-likelihood regression, EM becomes weighted least squares with weights $(\nu+1)/(\nu+\delta_n)$, which downweight outliers (pp. 292–294).
- **EM variants.** Variational, hard, Monte Carlo, generalized, ECM/ECME and online EM relax the E step, the M step or the data handling. Variational EM increases the bound but not necessarily the likelihood (pp. 295–297).
- **Bayesian optimization.** Alternate between updating a surrogate $p(f|\mathcal D_n)$ and querying the maximizer of an acquisition function. This trades exploration against exploitation when $f$ is expensive (pp. 297–299).
- **Acquisition functions.** Probability of improvement (PI), expected improvement (EI), upper confidence bound (UCB), Thompson sampling, entropy search and knowledge gradient are different ways to score a candidate query; PI, EI, entropy search and knowledge gradient are expected utilities. Maximizing the acquisition function is itself a hard multimodal problem (pp. 300–303).
- **Derivative-free search.** Hill climbing, random restarts, tabu search and random search are simple methods (the author says random search should always be tried as a baseline). Evolutionary algorithms keep a population. Estimation-of-distribution algorithms (EDA), the cross-entropy method (CEM) and evolution strategies replace the population by a fitted or gradient-updated distribution (pp. 304–313).

## L3 — Walkthrough

### 6.5 Bound optimization (MM) algorithms
MM means *majorize-minimize* for minimization and *minorize-maximize* for maximization. Examples named: EM, proximal gradient methods, mean shift (p. 287).

**6.5.1 The general algorithm (p. 287).** Goal: maximize $\ell(\theta)$. Build a surrogate $Q(\theta,\theta^t)$ with $Q(\theta,\theta^t)\le\ell(\theta)$ and $Q(\theta^t,\theta^t)=\ell(\theta^t)$; then $Q$ *minorizes* $\ell$. Update:
$$\theta^{t+1}=\arg\max_\theta Q(\theta,\theta^t)\tag{6.123}$$
$$\ell(\theta^{t+1})\ge Q(\theta^{t+1},\theta^t)\ge Q(\theta^t,\theta^t)=\ell(\theta^t)\tag{6.124}$$
First inequality: $Q$ is a lower bound. Second: the argmax in (6.123). Equality: tightness. Hence, if the objective does not increase monotonically, there is an error in math or code (p. 287). Fig. 6.7: the bound touches $\ell$ at $\theta^t$; its maximum gives $\theta^{t+1}$, where a new bound is fitted (p. 287).

*Intuition note.* Each step climbs on a bowl that sits under the true curve and touches it. Going to the top of the bowl cannot lower the true curve, because the curve is above the bowl.

**6.5.2 Example: logistic regression (pp. 288–289).** If $\ell$ is concave, find a negative definite $\mathbf B$ with $\mathbf H(\theta)\succ\mathbf B$. Then (shown in [BCN18, App. B]):
$$\ell(\theta)\ge\ell(\theta^t)+(\theta-\theta^t)^\top g(\theta^t)+\tfrac12(\theta-\theta^t)^\top\mathbf B(\theta-\theta^t)\tag{6.125}$$
with $g=\nabla\ell$. A valid lower bound and its update:
$$Q(\theta,\theta^t)=\theta^\top(g(\theta^t)-\mathbf B\theta^t)+\tfrac12\theta^\top\mathbf B\theta\tag{6.126}$$
$$\theta^{t+1}=\theta^t-\mathbf B^{-1}g(\theta^t)\tag{6.127}$$
(added step: $\nabla_\theta Q=g-\mathbf B\theta^t+\mathbf B\theta=0$ gives (6.127).) This resembles Newton's update but uses a fixed $\mathbf B$ instead of $\mathbf H(\theta^t)$. It can give some advantages of second-order methods at lower cost (p. 288).

Multiclass model with $C$ classes, $x_n\in\mathbb R^D$:
$$p(y_n=c|x_n,w)=\frac{\exp(w_c^\top x_n)}{\sum_{i=1}^C\exp(w_i^\top x_n)}\tag{6.128}$$
Set $w_C=0$ by normalization, so $\theta$ is a weight matrix of size $D(C-1)$. With $p_n(w)=[p(y_n=1|\cdot),\dots,p(y_n=C-1|\cdot)]$ and $y_n=[\mathbb I(y_n=1),\dots,\mathbb I(y_n=C-1)]$:
$$\ell(w)=\sum_{n=1}^N\Big[\sum_{c=1}^{C-1}y_{nc}w_c^\top x_n-\log\sum_{c=1}^C\exp(w_c^\top x_n)\Big]\tag{6.129}$$
$$g(w)=\sum_n(y_n-p_n(w))\otimes x_n\tag{6.130}$$
$$\mathbf H(w)=-\sum_n(\mathrm{diag}(p_n(w))-p_n(w)p_n(w)^\top)\otimes(x_nx_n^\top)\tag{6.131}$$
Here $\otimes$ is the Kronecker product (an outer product in this case) (p. 288). A Hessian bound from [Boh92]:
$$\mathbf H(w)\succ-\tfrac12[\mathbf I-\mathbf 1\mathbf 1^\top/C]\otimes\Big(\sum_n x_nx_n^\top\Big)\triangleq\mathbf B\tag{6.132}$$
with $\mathbf I$ the $(C-1)$-dimensional identity and $\mathbf 1$ a $(C-1)$-vector of ones. So $\mathbf B$ has shape $D(C-1)\times D(C-1)$ (added step). Binary case:
$$\mathbf H(w)\succ-\tfrac12\big(1-\tfrac12\big)\Big(\sum_n x_n^\top x_n\Big)=-\tfrac14\mathbf X^\top\mathbf X\tag{6.133}$$
The author's reason: $p_n\le0.5$, so $-(p_n-p_n^2)\ge-0.25$ (p. 289). The MM update is $w^{t+1}=w^t-\mathbf B^{-1}g(w^t)$ (6.134). In the binary case $g^t=\mathbf X^\top(y-\mu^t)$ with $\mu^t=[p_n(w^t)]_n$ and, as printed,
$$w^{t+1}=w^t-4(\mathbf X^\top\mathbf X)^{-1}g^t\tag{6.135}$$
Newton/IRLS, as printed:
$$w^{t+1}=w^t-\mathbf H^{-1}g(w^t)=w^t-(\mathbf X^\top\mathbf S^t\mathbf X)^{-1}g^t\tag{6.136}$$
with $\mathbf S^t=\mathrm{diag}(\mu^t\odot(1-\mu^t))$. (6.135) is faster per step because $(\mathbf X^\top\mathbf X)^{-1}$ can be precomputed (p. 289). See Reading notes on the signs.

*Intuition note.* The logistic curvature $p(1-p)$ never exceeds 1/4. So one constant, pessimistic curvature matrix serves at every iterate, and the expensive matrix inverse is done once.

**6.5.3 The EM algorithm (p. 289).** EM computes the MLE or MAP estimate for models with missing data or hidden variables. It is a special case of MM. The E step estimates hidden variables (or missing values). The M step computes the MLE from the "completed" data. The two are iterated because each depends on the other. Because EM is a bound optimizer, the author says the procedure will converge to a local maximum of the log likelihood. Speed depends on the amount of missing data, which affects the tightness of the bound. Notation: $y_n$ visible, $z_n$ hidden (p. 289).

**6.5.3.1 Lower bound (p. 290).**
$$\ell(\theta)=\sum_n\log p(y_n|\theta)=\sum_n\log\Big[\sum_{z_n}p(y_n,z_n|\theta)\Big]\tag{6.137}$$
This is hard to optimize because the log cannot be pushed inside the sum. Introduce arbitrary distributions $q_n(z_n)$:
$$\ell(\theta)=\sum_n\log\Big[\sum_{z_n}q_n(z_n)\frac{p(y_n,z_n|\theta)}{q_n(z_n)}\Big]\tag{6.138}$$
Jensen's inequality (log is concave) gives
$$\ell(\theta)\ge\sum_n\sum_{z_n}q_n(z_n)\log\frac{p(y_n,z_n|\theta)}{q_n(z_n)}\tag{6.139}$$
$$=\sum_n\underbrace{\mathbb E_{q_n}[\log p(y_n,z_n|\theta)]+\mathbb H(q_n)}_{\mathcal L(\theta,q_n|y_n)}\tag{6.140}$$
$$=\sum_n\mathcal L(\theta,q_n|y_n)\triangleq\mathcal L(\theta,\{q_n\}|\mathcal D)\tag{6.141}$$
$\mathbb H$ is entropy. $\mathcal L$ is the *evidence lower bound* (ELBO), a lower bound on the log marginal likelihood (evidence). Optimizing it is the basis of variational inference (Section 10.1) (p. 290).

**6.5.3.2 E step (pp. 290–291).** Each term:
$$\mathcal L(\theta,q_n|y_n)=\sum_{z_n}q_n\log\frac{p(y_n,z_n|\theta)}{q_n}\tag{6.142}$$
$$=\sum_{z_n}q_n\log\frac{p(z_n|y_n,\theta)p(y_n|\theta)}{q_n}\tag{6.143}$$
$$=\sum_{z_n}q_n\log\frac{p(z_n|y_n,\theta)}{q_n}+\sum_{z_n}q_n\log p(y_n|\theta)\tag{6.144}$$
$$=-D_{\mathrm{KL}}(q_n(z_n)\,\|\,p(z_n|y_n,\theta))+\log p(y_n|\theta)\tag{6.145}$$
where $D_{\mathrm{KL}}(q\|p)=\sum_zq(z)\log\frac{q(z)}{p(z)}$. Key property: $D_{\mathrm{KL}}\ge0$, with equality iff $q=p$. So the bound is maximized over $\{q_n\}$ by $q_n^*=p(z_n|y_n,\theta)$ (the E step), which makes it tight:
$$\mathcal L(\theta,\{q_n^*\}|\mathcal D)=\sum_n\log p(y_n|\theta)=\ell(\theta|\mathcal D)\tag{6.146}$$
Connection to MM: $Q(\theta,\theta^t)=\mathcal L(\theta,\{p(z_n|y_n;\theta^t)\})$ (6.147). Then $Q\le\ell$ and $Q(\theta^t,\theta^t)=\ell(\theta^t)$. If the exact posterior is not computable, an approximate $q(z_n|y_n;\theta^t)$ gives a non-tight bound; this is *variational EM* (p. 291).

**6.5.3.3 M step (p. 291).** Entropy terms do not depend on $\theta$ and are dropped, leaving the *expected complete data log likelihood*:
$$\ell^t(\theta)=\sum_n\mathbb E_{q_n^t(z_n)}[\log p(y_n,z_n|\theta)]\tag{6.148}$$
If the joint is in the exponential family:
$$\ell^t(\theta)=\sum_n\mathbb E[\mathcal T(y_n,z_n)^\top\theta-A(\theta)]=\sum_n(\mathbb E[\mathcal T(y_n,z_n)]^\top\theta-A(\theta))\tag{6.149}$$
$\mathbb E[\mathcal T]$ are the *expected sufficient statistics*. The M step is
$$\theta^{t+1}=\arg\max_\theta\sum_n\mathbb E_{q_n^t}[\log p(y_n,z_n|\theta)]\tag{6.150}$$
For exponential families, this is solved in closed form by moment matching of the expected sufficient statistics. The E step then only needs to return $\sum_n\mathbb E_{q(z_n)}[\mathcal T(y_n,z_n)]$ (p. 291).

*Intuition note.* The E step makes the bound exact at the current parameters by "filling in" hidden variables with their posterior. The M step then fits parameters to the filled-in data, weighted by that posterior. Neither step can lower the likelihood, by (6.124).

**6.5.4 Example: EM for an MVN with missing data (pp. 291–293).** With fully observed data the MLE is the sample mean and covariance. Now assume missing at random (MAR). $x_n$ are the visible and $z_n$ the hidden entries of $y_n=(z_n,x_n)\in\mathbb R^D$:
$$\log p(\mathbf X|\theta)=\sum_n\log\Big[\int p(x_n,z_n|\theta)dz_n\Big]\tag{6.151}$$
This is hard to maximize directly (p. 292).

*E step (p. 292).*
$$Q(\theta,\theta^{t-1})=\mathbb E\Big[\sum_n\log\mathcal N(y_n|\mu,\Sigma)\,\Big|\,\mathcal D,\theta^{t-1}\Big]\tag{6.152}$$
$$=-\tfrac N2\log|2\pi\Sigma|-\tfrac12\sum_n\mathbb E[(y_n-\mu)^\top\Sigma^{-1}(y_n-\mu)]\tag{6.153}$$
$$=-\tfrac N2\log|2\pi\Sigma|-\tfrac12\mathrm{tr}\Big(\Sigma^{-1}\sum_n\mathbb E[(y_n-\mu)(y_n-\mu)^\top]\Big)\tag{6.154}$$
$$=-\tfrac N2\log|\Sigma|-\tfrac{ND}2\log(2\pi)-\tfrac12\mathrm{tr}(\Sigma^{-1}\mathbb E[\mathbf S(\mu)])\tag{6.155}$$
$$\mathbb E[\mathbf S(\mu)]\triangleq\sum_n\big(\mathbb E[y_ny_n^\top]+\mu\mu^\top-2\mu\mathbb E[y_n]^\top\big)\tag{6.156}$$
So the expected sufficient statistics are $\sum_n\mathbb E[y_n]$ and $\sum_n\mathbb E[y_ny_n^\top]$. Using Section 2.3.1.3, with $\mu,\Sigma$ partitioned into hidden ($h$) and visible ($v$) blocks:
$$p(z_n|x_n,\theta)=\mathcal N(z_n|m_n,\mathbf V_n)\tag{6.157}$$
$$m_n\triangleq\mu_h+\Sigma_{hv}\Sigma_{vv}^{-1}(x_n-\mu_v)\tag{6.158}$$
$$\mathbf V_n\triangleq\Sigma_{hh}-\Sigma_{hv}\Sigma_{vv}^{-1}\Sigma_{vh}\tag{6.159}$$
Shapes: $m_n$ has $|h|$ entries; $\mathbf V_n$ is $|h|\times|h|$ (added step). Then $\mathbb E[y_n]=(\mathbb E[z_n];x_n)=(m_n;x_n)$ (6.160), and, via $\mathrm{Cov}[y]=\mathbb E[yy^\top]-\mathbb E[y]\mathbb E[y]^\top$ (p. 293):
$$\mathbb E[y_ny_n^\top]=\begin{pmatrix}\mathbb E[z_nz_n^\top]&\mathbb E[z_n]x_n^\top\\x_n\mathbb E[z_n]^\top&x_nx_n^\top\end{pmatrix}\tag{6.161}$$
$$\mathbb E[z_nz_n^\top]=\mathbb E[z_n]\mathbb E[z_n]^\top+\mathbf V_n\tag{6.162}$$

*M step (p. 293).* Solving $\nabla Q(\theta,\theta^{(t-1)})=0$, the M step equals plugging these statistics into the usual MLE equations:
$$\mu^t=\frac1N\sum_n\mathbb E[y_n]\tag{6.163}$$
$$\Sigma^t=\frac1N\sum_n\mathbb E[y_ny_n^\top]-\mu^t(\mu^t)^\top\tag{6.164}$$
EM is *not* the same as replacing variables by their expectations and applying the standard MLE. That would ignore the posterior variance and give an incorrect estimate (p. 293).

*Initialization (p. 293).* Compute the MLE on the fully observed rows. If there are none, estimate the diagonal of $\Sigma$ from observed marginal statistics.

*Example (p. 293).* Imputation with $N=100$ ten-dimensional cases, 50% of entries missing at random. Fit by EM to get $\hat\theta$, then impute with $\mathbb E[z_n|x_n,\hat\theta]$. The author says (Fig. 6.8) the results are almost as good as with the true parameters. Performance improves with more data or less missing data.

*Intuition note.* The term $\mathbf V_n$ in (6.162) is the part that "mean imputation" misses. Missing entries are uncertain, so their second moments are larger than the squared imputed means.

**6.5.5 Example: robust linear regression with a Student likelihood (pp. 293–295).** Likelihood:
$$p(y|x,w,\sigma^2,\nu)=\mathcal T(y|w^\top x,\sigma^2,\nu)\tag{6.165}$$
There is no missing data, but "artificial" hidden variables can be introduced, a common trick. The Student distribution is a Gaussian scale mixture (Section 28.2.3.1). Attach a latent scale $z_n\in\mathbb R_+$ to each example (p. 294):
$$\log p(y,z|\mathbf X,w,\sigma^2,\nu)=\sum_n-\tfrac12\log(2\pi z_n\sigma^2)-\tfrac1{2z_n\sigma^2}(y_i-w^\top x_i)^2\tag{6.166}$$
$$\qquad+\big(\tfrac\nu2-1\big)\log z_n-z_n\tfrac\nu2+\text{const}\tag{6.167}$$
Keeping only terms with $w$ and taking expectations:
$$Q(\theta,\theta^t)=-\sum_n\frac{\lambda_n}{2\sigma^2}(y_n-w^\top x_n)^2\tag{6.168}$$
with $\lambda_n^t\triangleq\mathbb E[1/z_n|y_n,x_n,w^t]$. This is a weighted least squares objective with weight $\lambda_n^t$ per datapoint. Using Section 2.2.3.4:
$$p(z_n|y_n,x_n,\theta)=\mathrm{IG}\Big(\frac{\nu+1}2,\frac{\nu+\delta_n}2\Big)\tag{6.169}$$
where $\delta_n$ is the standardized residual $(y_n-w^\top x_n)^2/\sigma^2$ (see Reading notes). Hence
$$\lambda_n=\mathbb E[1/z_n]=\frac{\nu^t+1}{\nu^t+\delta_n^t}\tag{6.170}$$
A large residual gives a low weight, which makes sense since that point is probably an outlier (p. 295).

*Intuition note.* Each E step asks "how outlying is this point under the current fit?" and answers with a weight. Each M step then does ordinary weighted least squares with those weights.

**6.5.6 Extensions to EM (pp. 295–297).**
- *Variational EM (§6.5.6.1, p. 295).* In the E step choose $q_n^*=\arg\min_{q_n\in\mathcal Q}D_{\mathrm{KL}}(q_n\|p(z_n|x_n,\theta))$. If $\mathcal Q$ contains the true posterior, the KL can be made zero. A restricted family, e.g. $\mathcal N(z_n|\mu_n,\mathrm{diag}(\sigma_n))$ for a correlated posterior, is used for computational reasons. Unlike regular EM, variational EM is not guaranteed to increase the actual log likelihood (Fig. 6.9), but it does monotonically increase the variational lower bound. With $q_n=p_n$ (exact inference) we recover regular EM.
- *Hard EM (§6.5.6.2, pp. 295–296).* A point-mass posterior $q(z|x_n)=\delta_{\hat z_n}(z)$ with $\hat z_n=\arg\max_zp(z|x_n)$ ignores uncertainty about $z_n$. It is very prone to overfitting, since the number of latent variables grows with the number of datacases.
- *Monte Carlo EM (§6.5.6.3, p. 296).* Draw $z_n^s\sim p(z_n|x_n,\theta^t)$, compute sufficient statistics of each completed vector $(x_n,z_n^s)$, and average. Using MCMC to convergence inside each E step is slow. *Stochastic approximation EM* uses brief sampling and a partial parameter update, and tends to work better.
- *Generalized EM (§6.5.6.4, p. 296).* If the E step can be done exactly but the M step cannot, a partial M step that merely increases the expected complete-data log likelihood can still monotonically increase the log likelihood. Example (Lange): one Newton–Raphson step
$$\theta_{t+1}=\theta_t-\eta_t\mathbf H_t^{-1}g_t,\quad 0<\eta_t\le1\tag{6.171}$$
$$g_t=\frac{\partial}{\partial\theta}Q(\theta,\theta_t)\Big|_{\theta=\theta_t}\tag{6.172}$$
$$\mathbf H_t=\frac{\partial^2}{\partial\theta\partial\theta^\top}Q(\theta,\theta_t)\Big|_{\theta=\theta_t}\tag{6.173}$$
With $\eta_t=1$ this is *gradient EM*. Larger steps and a BFGS approximation in place of the Hessian, which may not be negative definite, give the quasi-Newton EM. When the M step is not closed-form, EM loses some appeal versus directly optimizing the marginal likelihood with a gradient-based solver.
- *ECM / ECME (§6.5.6.5, pp. 296–297).* ECM optimizes the M-step parameters sequentially when they are dependent. ECME, in some conditional-maximization steps, maximizes the observed-data log likelihood instead of $Q$, which can be much faster. Example: Student fit. For fixed $\nu$, update $\Sigma$ as usual; update $\nu$ by $\arg\max_\nu\log p(\mathcal D|\mu^{t+1},\Sigma^{t+1},\nu)$ instead of maximizing $Q$.
- *Online EM (§6.5.6.6, p. 297).* *Incremental EM* optimizes the bound one $q_n$ at a time but must store expected sufficient statistics for each case. *Stepwise EM* is based on stochastic gradient descent; the text says it optimizes a local upper bound on $\ell_n(\theta)=\log p(x_n|\theta)$ at each step.

### 6.6 Bayesian optimization (pp. 297–304)
BayesOpt is model-based optimization of a black-box $f:\mathcal X\to\mathbb R$ that is expensive to evaluate. We want few queries. We build a *surrogate* (response surface model) from $\mathcal D_n=\{(x_i,y_i)\}_{i=1}^n$ and use it to pick the next query. There is a tradeoff between querying where $f(x)$ is believed large (exploitation) and where uncertainty is high (exploration). We maximize by convention. On a finite domain $\{1,\dots,A\}$ the problem resembles best-arm identification in bandits, but bandits care about cumulative regret and optimization usually only about simple (final) regret. Active learning wants the whole function; BayesOpt wants only its maximum (p. 297).

**6.6.1 Sequential model-based optimization (p. 298).** BayesOpt is an instance of SMBO. Data: $y_i=f(x_i)+\epsilon_i$ (noise optional). Estimate $p(f|\mathcal D_n)$, then choose $x_{n+1}$ by an acquisition function $\alpha(x;\mathcal D_n)$, the expected utility of querying $x$. Algorithm 6.5:
1. Collect $\mathcal D_0$ from random queries or a space-filling design.
2. Compute $p(f|\mathcal D_0)$.
3. For $n=1,2,\dots$ until convergence: $x_{n+1}=\arg\max_{x\in\mathcal X}\alpha(x;\mathcal D_n)$; measure $y_{n+1}=f(x_{n+1})+\epsilon$; set $\mathcal D_{n+1}=\{\mathcal D_n,(x_{n+1},y_{n+1})\}$; recompute $p(f|\mathcal D_{n+1})$.

Fig. 6.10 (noise-free): at queried points the credible interval is "pinched" and the acquisition value is 0. The next query is the acquisition maximum. The process repeats until time runs out or no better unexplored point is believed to exist. Two ingredients are needed: a representation of $p(f|\mathcal D_n)$ and an acquisition function (p. 298).

**6.6.2 Surrogate functions (pp. 298–300).**
- *Gaussian processes (pp. 298–299).* A GP represents $p(f(x)|\mathcal D_n)=\mathcal N(f|\mu_n(x),\sigma_n^2(x))$, with $\mu_n,\sigma_n$ from closed-form equations. It needs a kernel $\mathcal K_\theta(x,x')$; similar inputs (large kernel) have positively correlated values, which allows interpolation and sometimes extrapolation. GPs work well with little data and support closed-form updating. Exact updating costs $O(N^3)$; approximations reach $O(NM^2)$ (Section 18.5.3) but sacrifice accuracy. Performance depends heavily on the kernel. Kernel parameters $\theta$ can be set by maximizing the marginal likelihood, but with small samples marginalizing out $\theta$ approximately can often do better.
- *Bayesian neural networks (pp. 299–300).* A parametric alternative. Linear regression allows exact Bayesian inference (Section 15.2); nonlinear models such as DNNs need approximate inference (Chapter 17).
- *Other models (p. 300).* Ensembles of random forests [HHLB11] handle conditional parameter spaces easily, but the bootstrapping needed for uncertainty can be slow.

**6.6.3 Acquisition functions (pp. 300–303).** General form: $\alpha(x|\mathcal D_n)=\mathbb E_{p(y|x,\mathcal D_n)}[U(x,y;\mathcal D_n)]$ with utility $U$. Utilities are usually chosen so that already-queried points have small (0 if noise-free) value, which encourages exploration (p. 300).

*PI (p. 300).* Let $M_n=\max_{i\le n}y_i$ be the incumbent (with noisy data, the highest posterior mean is a reasonable alternative). $U=\mathbb I(y>M_n)$ gives $\alpha_{PI}=p(f(x)>M_n|\mathcal D_n)$. For a GP:
$$\alpha_{PI}(x;\mathcal D_n)=\Phi(\gamma_n(x,M_n)),\qquad\gamma_n(x,\tau)=\frac{\mu_n(x)-\tau}{\sigma_n(x)}\tag{6.174, 6.175}$$
with $\Phi$ the standard normal cdf.

*EI (pp. 300–301).* PI counts all improvements as equally good and so tends to exploit aggressively. EI uses $U=(y-M_n)\mathbb I(y>M_n)$:
$$\alpha_{EI}(x;\mathcal D_n)=\mathbb E[(f(x)-M_n)\mathbb I(f(x)>M_n)]\tag{6.176}$$
For a GP, with $\phi$ the standard normal pdf and $\gamma=\gamma_n(x,M_n)$:
$$\alpha_{EI}=(\mu_n(x)-M_n)\Phi(\gamma)+\sigma_n(x)\phi(\gamma)=\sigma_n(x)[\gamma_n\Phi(\gamma)+\phi(\gamma)]\tag{6.177}$$
The first term encourages exploitation (high mean), the second exploration (high variance). With posterior samples instead of an analytic variance, a Monte Carlo estimate (as printed, with $\mu_n^s(x)$ the $s$-th sample):
$$\alpha_{EI}(x;\mathcal D_n)\approx\frac1S\sum_{s=1}^S\max(\mu_n^s(x)-M_n,0)\tag{6.178}$$

*UCB (p. 301).* $\alpha_{UCB}(x;\mathcal D_n)=\mu_n(x)+\beta_n\sigma_n(x)$. This is the contextual-bandit idea (Section 34.4.5), but over $x\in\mathcal X$ instead of a finite set of arms. With a GP it is GP-UCB.

*Thompson sampling (p. 302).* Generalizing the bandit case ("probability arm $a$ is best"):
$$\alpha(x;\mathcal D_n)=\mathbb E_{p(\theta|\mathcal D_n)}\Big[\mathbb I\Big(x=\arg\max_{x'}f_\theta(x')\Big)\Big]\tag{6.179}$$
A single-sample approximation draws $\tilde\theta\sim p(\theta|\mathcal D_n)$:
$$x_{n+1}=\arg\max_x\alpha(x;\mathcal D_n)=\arg\max_x\mathbb I\Big(x=\arg\max_{x'}f_{\tilde\theta}(x')\Big)=\arg\max_xf_{\tilde\theta}(x)\tag{6.180}$$
That is, greedily maximize the sampled surrogate. In continuous spaces this is harder than in the bandit case. With GPs there are subtle difficulties in sampling a function rather than parameters.

*Entropy search (p. 302).* Let $p_*(x|\mathcal D_n)$ be the posterior over the optimum's location $x^*$. The information-gain utility is
$$U(x,y;\mathcal D_n)=\mathbb H(x^*|\mathcal D_n)-\mathbb H(x^*|\mathcal D_n\cup\{(x,y)\})\tag{6.181}$$
(differing from active learning, which wants information about $f$ everywhere), with
$$\alpha_{ES}(x;\mathcal D_n)=\mathbb H(x^*|\mathcal D_n)-\mathbb E_{p(y|x,\mathcal D_n)}[\mathbb H(x^*|\mathcal D_n\cup\{(x,y)\})]\tag{6.182}$$
Computing $\mathbb H(x^*|\mathcal D_n)$ is hard. Using the symmetry of mutual information,
$$\alpha_{PES}(x;\mathcal D_n)=\mathbb H(y|\mathcal D_n,x)-\mathbb E_{x^*|\mathcal D_n}[\mathbb H(y|\mathcal D_n,x,x^*)]\tag{6.183}$$
where the expectation over $p(x^*|\mathcal D_n)$ can be approximated by Thompson sampling. This is *predictive entropy search*, which only needs uncertainty about the output $y$.

*Knowledge gradient (p. 303).* The previous criteria are greedy (one step ahead). KG [FPD09] considers querying $x$, updating the posterior, then exploiting by maximizing the new posterior mean:
$$V_{n+1}(x,y)=\max_{x'}\mathbb E_{p(f|x,y,\mathcal D_n)}[f(x')]\tag{6.184}$$
$$V_{n+1}(x)=\mathbb E_{p(y|x,\mathcal D_n)}[V_{n+1}(x,y)]\tag{6.185}$$
$$\alpha_{KG}(x;\mathcal D_n)=\mathbb E_{\mathcal D_n}[(V_{n+1}(x)-M_n)\mathbb I(V_{n+1}(x)>M_n)]\tag{6.186}$$
We pick the point whose observation gives knowledge we can exploit, rather than directly trying to find a better $f$ value.

*Optimizing the acquisition function (p. 303).* $\alpha$ is often multimodal (Fig. 6.11), since it is 0 at previously queried points when noise-free; consequently maximizing it can be a hard subproblem. Continuous case: multirestart BFGS or grid search; the cross-entropy method with Gaussian mixtures or VAEs. Discrete case: regularized evolution, or proximal policy optimization.

*Intuition note.* Acquisition functions such as PI, EI and UCB turn "mean" and "uncertainty" into one score. EI's two terms in (6.177) show this most clearly: a high mean or a high standard deviation can each make a point attractive.

**6.6.4 Other issues (pp. 303–304).**
- *Batch queries (p. 303):* query several points in parallel; one must optimize over a set of queries, which is computationally harder.
- *Conditional parameters (pp. 303–304):* some hyperparameters exist only if others take certain values (e.g. layers/units for a neural net, tree depth for a decision tree). The search space is formalized as a tree or DAG. GPs then need non-standard kernels; random-forest ensembles handle this easily.
- *Multifidelity (p. 304):* $f(x,s)$ approximates the true function at fidelity $s$; the goal is $\max_xf(x,0)$ with total cost $\sum_ic(s_i)$ under a budget. Expensive trials can be terminated early, or aborted runs resumed (freeze-thaw).
- *Constraints (p. 304):* known constraints can be built into the acquisition function. For unknown constraints, weighted EI is $\alpha_{wEI}=\alpha_{EI}(x;\mathcal D_n)h(x;\mathcal D_n)$, where $h$ is a GP with a Bernoulli observation model for feasibility.

### 6.7 Derivative-free optimization (DFO) (pp. 304–313)
DFO optimizes without derivatives, for black-box or discrete problems. Expensive functions: use BayesOpt. Cheap functions: stochastic local search or evolutionary search (p. 304).

**6.7.1 Local search (pp. 304–306).** For a discrete unstructured space, replace the gradient step by
$$x_{t+1}=\arg\max_{x\in\mathrm{nbr}(x_t)}\mathcal L(x)\tag{6.187}$$
This is *hill climbing*, steepest ascent or greedy search (p. 305). A neighborhood equal to the whole space returns the global optimum in one step but is usually too large to search. *8-queens example (p. 305):* the state space is $64^8$, but only $8^8\approx17$M states are feasible. Neighbors: move one queen within its column, giving $8\times7=56$ neighbors. From a random start, steepest ascent gets stuck at a local maximum 86% of the time (solving 14%), taking on average 4 steps when it succeeds and 3 when stuck [RN10, p. 123].

*6.7.1.1 Stochastic local search (p. 305).* *Stochastic hill climbing* samples among uphill neighbors with probability proportional to improvement. Gradually decreasing the entropy of that distribution gives *simulated annealing* (Section 12.9.1). *Random restart hill climbing* restarts from a new random point at each local maximum. With success probability $p\approx0.14$ per run, the expected number of runs is $R=1/p\approx7$. With $N_1=4$ steps per success and $N_0=3$ per failure, the expected total is $N_1+(R-1)N_0=4+6\times3=22$ steps. It can solve $n$-queens with $n=1$M in under a minute. Such stochastic local search (SLS) works surprisingly well on real boolean satisfiability problems.

*6.7.1.2 Tabu search (pp. 305–306).* Like hill climbing, but moves that decrease (or do not increase) the score are allowed if they go to a state not seen recently. A tabu list tracks the $\tau$ most recent states. Algorithm 6.6: set $t=0$, $c=0$, $x^*=x_0$; while $c<c_{\max}$: $x_{t+1}=\arg\max_{x\in\mathrm{nbr}(x_t)\setminus\{x_{t-\tau},\dots,x_{t-1}\}}f(x)$; if $f(x_{t+1})>f(x^*)$ then $x^*=x_{t+1}$ and $c=0$, else $c=c+1$; $t=t+1$. Setting $c_{\max}=1$ gives greedy hill climbing. At a peak the search is forced to "circle" it, possibly moving to lower level sets, until it finds a ridge to a new peak or exceeds the allowed number of non-improving moves. On 8-queens it raises the solved fraction from 14% to 94%, at an average of 21 steps for successes and 64 for failures [RN10].

*6.7.1.3 Random search (pp. 306–307).* Choose each iterate uniformly from $\mathcal X$; the author says to always try it as a baseline. In [BB12], hyperparameter search over $\Theta=[0,1]^D$: random search outperformed grid search; the intuitive reason given is that many hyperparameters matter little, so a fine grid along them wastes evaluations (Fig. 6.12). Random search was also used for MDP policy parameters $f(x)=\mathbb E_{\tau\sim\pi_x}[R(\tau)]$. For policies with few parameters it can outperform more sophisticated RL methods. For many parameters one may optimize in a random low-dimensional subspace.

**6.7.2 Simulated annealing (p. 307).** An SLS method for the global minimum of an energy $\mathcal E(x)$. It defines the unnormalized $p(x)=\exp(-\mathcal E(x))$ and uses a Metropolis–Hastings variant to sample from a sequence of distributions, designed so the final step samples from a mode (a lowest-energy state). It works for discrete and continuous problems (details in Section 12.9.1).

**6.7.3 Evolutionary algorithms (pp. 307–310).** SLS keeps one guess; $K$ restarts for $T$ steps cost $TK$. An *evolutionary algorithm* (EA) keeps a *population* of $K$ candidates $\mathcal S_t$, also at cost $TK$. It can often do better than multi-restart SLS, because it explores in parallel and members share information (p. 307). Terminology: *fitness* = objective value; next-generation members are *offspring*, made by mutating one parent (asexual) or by *recombination* of two parents, often followed by mutation (p. 308). *Selection functions:*
- truncation: parents from the fittest $K$ (the elite set);
- tournament: each parent is the fittest of $K$ random members;
- fitness-proportionate (roulette wheel): probability proportional to relative fitness;
- regularized evolution: kill the oldest members, then select by fitness.

Variants (pp. 308–310):
- *Genetic algorithm (GA):* mutation plus crossover on integer/binary vectors: pick a split point in each parent and swap strings. Fig. 6.13 (8-queens): fitness is the number of non-attacking pairs, maximum 28. Selection probability is $\mathcal L(\theta)/Z$ with total fitness $Z=78$, so the first individual (fitness 24) gets $24/78=0.31$ and the second (23) gets $23/78=0.29$. In the example the first is picked once, the second twice, the third once, and the last not at all. Fig. 6.14 shows the parents and child as board states.
- *Genetic programming:* individuals are trees, so all crossovers give valid children (Fig. 6.15: parents $\sin(x)+(x+y)^2$ and $\sin(x)+\sqrt{x^2+y}$). It can evolve programs or neural networks. In *evolutionary programming* the tree structure is fixed and only numerical parameters evolve.
- *Surrogate-assisted EA:* a cheap surrogate $\hat f$ replaces $f$, similar to BayesOpt response surfaces but without the explore–exploit tradeoff.
- *Memetic algorithm:* mutation and recombination combined with standard local search.

EAs are also used to train neural networks (neuroevolution).

**6.7.4 Estimation of distribution (EDA) algorithms (pp. 310–312).** The EA population is an implicit nonparametric density over high-fitness states. [BC95] proposed to "remove the genetics from GAs" (p. 310): explicitly learn a probabilistic model $p(x|\theta_t)$ that puts mass on good solutions. Procedure:
1. Sample $K'>K$ candidates $\mathcal S_t=\{x_k\sim p(x|\theta_t)\}$.
2. Rank by fitness and keep the best $K$ (truncation selection), $\mathcal S_t^*$.
3. Fit $p(x|\theta_{t+1})$ to $\mathcal S_t^*$ by MLE.

This is equivalent to minimizing cross entropy between the empirical distribution of $\mathcal S_t^*$ and the model. It is therefore related to the cross-entropy method (which usually assumes $p=\mathcal N(\mu,\Sigma)$) and also to EM (p. 310).

*One-max example (p. 310):* bit strings of length $D$, $f(x)=\sum_dx_d$, factored model $p(x|\theta)=\prod_d\mathrm{Ber}(x_d|\theta_d)$. This is the *univariate marginal distribution algorithm* (UMDA). Set $\theta_d$ to the fraction of $\mathcal S_t^*$ with bit $d$ on. Alternatively, *PBIL* updates incrementally:
$$\hat\theta_{d,t+1}=(1-\eta_t)\hat\theta_{d,t}+\eta_t\bar\theta_{d,t}\tag{6.188}$$
with $\bar\theta_{d,t}$ the MLE from the $K=|\mathcal S_t^*|$ elite samples (as printed: $\frac1{N_t}\sum_{k=1}^K\mathbb I(x_{k,d}=1)$) and $\eta_t$ a learning rate.

*Richer models (pp. 311–312):* a multivariate Gaussian gives EMNA. For discrete variables, graphical models capture dependencies: tree-structured models via Chow–Liu [BD97]; Bayes nets, which allow ancestral sampling, give the Bayesian optimization algorithm (BOA, Fig. 6.16). hBOA uses decision trees/graphs for the local CPTs. Learning the model structure is *linkage learning*. Footnote 5: BOA is not the BayesOpt of §6.6, which models $p(f(x))$ rather than $p(x^*)$. Deep generative models (denoising autoencoders, NADE, RBMs, VAEs, or an inverted DNN regressor) can also be used. They might need more function calls, but can potentially model the landscape more faithfully; whether that gives better optimization is not clear (p. 312).

**6.7.5 Cross-entropy method (p. 312).** CEM is the EDA special case with a multivariate Gaussian: set $\mu_{t+1},\Sigma_{t+1}$ to the empirical mean and covariance of the top $K$ samples. It is closely related to the SMC rare-event algorithm (Section 13.6.4). It is used for model-predictive-control action sequences and inside BayesOpt to optimize the acquisition function.

*6.7.5.1 Differentiable CEM (p. 312).* Replace the top-$K$ operator by a soft, differentiable one [AY20], so the optimizer can sit inside an end-to-end differentiable pipeline (e.g. differentiable MPC). Let the population have fitness $v_{t,i}=f(x_{t,i})$. In CEM, $\mathcal S_t^*=\{i:v_{t,i}\ge v^*_{t,K}\}$ and $\theta_{t+1}=\arg\max_\theta\sum_{i\in\mathcal S_t}p_t(i)\log p(x_{t,i}|\theta)$, with $p_t(i)=\mathbb I(i\in\mathcal S_t^*)/|\mathcal S_t^*|$. The soft version uses $q_t=\Pi(p_t;\tau,K)$:
$$\Pi(p;\tau,K)=\arg\min_{0\le q\le1}-p^\top q-\tau\mathbb H(q)\ \ \text{s.t.}\ \mathbf 1^\top q=K\tag{6.189}$$
This projects $p$ onto the polytope of vectors summing to $K$. Here $\mathbb H$ is the binary entropy summed over entries and $\tau>0$ a temperature. The projection can be backpropagated through by implicit differentiation.

**6.7.6 Evolutionary strategies (pp. 312–313).** A distribution-based method with a Gaussian $p(x|\theta_t)$. Unlike CEM, parameters are updated by gradient ascent on the smoothed objective $\mathcal L(\theta)=\mathbb E_{p(x|\theta)}[f(x)]$, not by MLE on elites. The REINFORCE estimator (Section 6.3.4) gives
$$\nabla_\theta\mathcal L(\theta)=\mathbb E_{p(x|\theta)}[f(x)\nabla_\theta\log p(x|\theta)]\tag{6.190}$$
with update $\theta_{k+1}=\theta_k+\eta\nabla_\theta\mathcal L(\theta_k)$, and the expectation approximated by Monte Carlo (p. 312). For a Gaussian (p. 313):
$$\nabla_\mu\log p(x|\mu,\Sigma)=\Sigma^{-1}(x-\mu)$$
$$\nabla_\Sigma\log p(x|\mu,\Sigma)=\tfrac12\Sigma^{-1}(x-\mu)(x-\mu)^\top\Sigma^{-1}-\tfrac12\Sigma^{-1}$$
A gradient step on $\Sigma$ may not keep it positive definite, so use a Cholesky factor $\Sigma=\mathbf A^\top\mathbf A$ with
$$\nabla_{\mathbf A}\log p(x|\mu,\mathbf A)=\mathbf A\big[\nabla_\Sigma\log p(x|\mu,\Sigma)+\nabla_\Sigma\log p(x|\mu,\Sigma)^\top\big]$$

*6.7.6.1 Natural evolution strategies (p. 313).* If the model is in the exponential family, use the natural gradient (Section 6.4) instead of the vanilla gradient, which can converge faster.

*6.7.6.2 CMA-ES (p. 313).* A kind of NES, very similar to CEM except for how parameters are updated. Elite samples get rank-based weights, and the new mean is the weighted MLE of the elite set. The covariance update is more complex and uses "evolutionary paths" accumulated across generations. The resulting updates approximate the natural gradient of $\mathcal L(\theta)$ without explicitly modeling the Fisher information matrix [Oll+17].

*6.7.6.3 Isotropic evolutionary strategies (p. 313, part ends here).* With fixed spherical covariance $p(x|\theta)=\mathcal N(x|\mu,\sigma^2\mathbf I)$ and $\theta=\mu$, define $\epsilon=x-\mu$ (as printed):
$$\nabla_\mu\mathcal L(\mu)=\mathbb E_{\mathcal N(x|\mu,\sigma^2\mathbf I)}\big[f(x)\nabla_\mu\log\mathcal N(x|\mu,\sigma^2\mathbf I)\big]=\mathbb E\Big[f(x)\tfrac1{\sigma^2}(x-\mu)\Big]$$
$$=\mathbb E_{\mathcal N(\epsilon|0,\mathbf I)}\Big[f(x+\sigma\epsilon)\tfrac1{\sigma^2}(\sigma\epsilon)\Big]=\tfrac1\sigma\mathbb E_{\mathcal N(\epsilon|0,\mathbf I)}[f(x+\sigma\epsilon)\epsilon]$$
Variance can be reduced by *mirror sampling*: draw $m/2$ samples of $\epsilon$ and use $-\epsilon$ for the other $m/2$. This is related to antithetic sampling (Section 11.6.4).

*Intuition note.* Evolution strategies treat the optimizer as a search distribution. They estimate how moving its mean changes the average fitness, using only function values and the score-function trick. Samples with higher $f$ get more weight in the update, so the mean moves toward them.

## Toy example (ours, not from the text)
Binary logistic regression with two data points: $x_1=x_2=1$, $y_1=1$, $y_2=0$, one weight $w$. Then $\ell(w)=w-2\log(1+e^w)$, $g(w)=(1-p)+(0-p)=1-2p$ with $p=\sigma(w)$. The maximum is at $p=\tfrac12$, i.e. $w=0$.

Bound: $\mathbf H=-\sum_np_n(1-p_n)\ge-(\tfrac14+\tfrac14)=-\tfrac12$, so $B=-\tfrac14\mathbf X^\top\mathbf X=-\tfrac14(1+1)=-\tfrac12$. By (6.127), $w^{t+1}=w^t-B^{-1}g=w^t+2g(w^t)$.

| $t$ | $w^t$ | $p=\sigma(w^t)$ | $g=1-2p$ | $w^{t+1}=w^t+2g$ | $\ell(w^t)$ |
|---|---|---|---|---|---|
| 0 | 1 | 0.7311 | −0.4621 | 1 − 0.9242 = 0.0758 | 1 − 2(1.3133) = −1.6265 |
| 1 | 0.0758 | 0.5189 | −0.0379 | 0.0758 − 0.0758 ≈ 0.00004 | 0.0758 − 2(0.7317) = −1.3877 |
| 2 | ≈0 | 0.5 | ≈0 | ≈0 | −2 ln 2 = −1.3863 |

The objective increases at each step ($-1.6265<-1.3877<-1.3863$), as (6.124) guarantees. Each step used the same constant $B$, never recomputing the Hessian.

## Concepts
- [[bound-optimization-mm]] (new) — maximize a surrogate $Q\le\ell$ that is tight at the current point; gives monotone improvement (p. 287)
- [[surrogate-function]] (new) — in MM, the lower bound $Q$; in BayesOpt, a probabilistic model of $f$ built from queries so far (pp. 287, 297)
- [[em-algorithm]] (new) — alternate E step (posterior over hidden variables) and M step (maximize expected complete-data log likelihood); a case of MM (p. 289)
- [[expected-complete-data-log-likelihood]] (new) — $\sum_n\mathbb E_{q_n^t}[\log p(y_n,z_n|\theta)]$, the M-step objective (p. 291)
- Variational inference & ELBO — $\mathcal L(\theta,\{q_n\}|\mathcal D)$ from Jensen; lower bound on the log evidence (p. 290)
- KL divergence — $D_{\mathrm{KL}}(q\|p)\ge0$, zero iff $q=p$; the E step sets it to zero (p. 291)
- [[variational-em]] (new) — EM with a restricted $q$ family in the E step; raises the bound, not necessarily the likelihood (p. 295)
- [[hard-em]] (new) — EM with a point-mass posterior; prone to overfitting (pp. 295–296)
- [[monte-carlo-em]] (new) — sample the E step's expected sufficient statistics (p. 296)
- [[generalized-em]] (new) — partial M step that only increases $Q$ (p. 296)
- [[bayesian-optimization]] (new) — SMBO for expensive black-box $f$: surrogate $p(f|\mathcal D_n)$ plus acquisition function (pp. 297–298)
- [[acquisition-function]] (new) — expected utility of querying $x$, maximized to choose the next query (p. 300)
- [[expected-improvement]] (new) — $\mathbb E[(f(x)-M_n)\mathbb I(f(x)>M_n)]$; closed form for a GP (p. 300)
- [[thompson-sampling]] (new) — sample a surrogate and greedily maximize the sample (p. 302)
- [[entropy-search]] (new) — pick the query that most reduces entropy over the optimum's location (p. 302)
- [[knowledge-gradient]] (new) — value of the best posterior-mean point after one more query (p. 303)
- [[hill-climbing-local-search]] (new) — move to the best neighbor; random restart and tabu variants escape local maxima (pp. 304–306)
- [[random-search]] (new) — uniform sampling over $\mathcal X$; a baseline that beat grid search for hyperparameters in [BB12] (p. 306)
- [[evolutionary-algorithm]] (new) — population-based search with selection, recombination, mutation (p. 307)
- [[estimation-of-distribution-algorithm]] (new) — repeatedly fit a generative model to elite samples and resample (p. 310)
- [[cross-entropy-method]] (new) — EDA with a Gaussian fitted to the top $K$ samples (p. 312)
- [[evolution-strategies]] (new) — gradient ascent on $\mathbb E_{p(x|\theta)}[f(x)]$ via REINFORCE (p. 312)
- Monte Carlo integration — used in MCEM, the EI estimate (6.178) and ES gradients (pp. 296, 301, 313)
- Metropolis–Hastings — simulated annealing uses a variant to sample $\exp(-\mathcal E)$ (p. 307)

## Canonical instances
- [[mm-logistic-regression]] — fixed Hessian bound $-\tfrac14\mathbf X^\top\mathbf X$ yields a cheaper-than-IRLS update (pp. 288–289)
- [[em-mvn-missing-data]] — EM with Gaussian conditioning; imputation on $N=100$, $D=10$, 50% missing (pp. 291–293)
- [[em-student-regression]] — scale-mixture latent variables turn robust regression into weighted least squares (pp. 293–295)
- [[branin-bayesopt]] — GP posterior and PI/EI/GP-UCB acquisition maps on the Branin function (p. 301)
- [[eight-queens]] — hill climbing 14% vs tabu 94% success; restart expectation of 22 steps; GA crossover example (pp. 305–309)
- [[one-max-umda-pbil]] — EDA with a factored Bernoulli model on bit strings (p. 310)

## Bridges (candidates)
- [same-math] EM's ELBO (6.140–6.145) ↔ Bayesian inference: variational ELBO and KL to the posterior — the text itself says this bound is the basis of variational inference.
- [same-math] Random restart hill climbing: $R=1/p$ expected restarts ↔ probability: mean of a geometric waiting time until the first success.
- [same-math] Evolution-strategies gradient (6.190) ↔ machine learning: score-function (REINFORCE) estimator, cited as Section 6.3.4.
- [structural-analogy] EM's latent scales $z_n$ and weights $\lambda_n$ ↔ hierarchical models: a per-observation latent variable controls how much each point influences the fit.
- [structural-analogy] Thompson sampling for BayesOpt ↔ bandits: posterior sampling over arms generalized to continuous inputs.
- [structural-analogy] EDA/CEM ↔ EM: both alternate "sample or infer, then refit by MLE"; the text calls EDA "closely related" to EM.
- [structural-analogy] Simulated annealing ↔ MCMC: Metropolis–Hastings sampling from $\exp(-\mathcal E)$ with decreasing entropy.
- [metaphor] Tabu list "circling" a peak ↔ basin flooding.

## Questions this raises
- When the E step is only approximate (variational EM), how loose can the bound get before the likelihood moves in the wrong direction (Fig. 6.9b)?
- How much does GP-based BayesOpt degrade in high dimensions or with many evaluations, given the $O(N^3)$ cost?
- Under what conditions does an EDA with a richer model (BOA, deep generative models) beat a simple factored model, given the extra function calls?
- How do natural-gradient evolution strategies (and CMA-ES) compare with REINFORCE-based vanilla gradients in practice?

## Reading notes
- **Scope.** This part starts at §6.5 (printed p. 287, with Fig. 6.7 at the top) and ends on printed p. 313, in the middle of §6.7.6.3 (after the mirror-sampling paragraph). Fig. 6.17 is cited on p. 313 but is not in these pages. Page offset: printed = pdf − 34. Footer: "Online version. December 10, 2025"; CC-BY-NC-ND.
- **Signs in (6.135)–(6.136).** With $\mathbf B=-\tfrac14\mathbf X^\top\mathbf X$, (6.127) gives $w^{t+1}=w^t+4(\mathbf X^\top\mathbf X)^{-1}g^t$. Likewise $\mathbf H=-\mathbf X^\top\mathbf S\mathbf X$ gives $w-\mathbf H^{-1}g=w+(\mathbf X^\top\mathbf S\mathbf X)^{-1}g$. The printed minus signs seem to treat the matrices as positive definite ($-\mathbf B$, $-\mathbf H$). I kept the equations as printed.
- **(6.133).** The printed form is $\sum x_n^\top x_n$; it should be $x_nx_n^\top$ (matrix, as in (6.132)). The inequality $p-p^2\le0.25$ holds for all $p\in[0,1]$; the printed reason "$p_n\le0.5$" is stated as is.
- **(6.169).** The image shows $\delta_n=(y_n-x^\top x_n)^2/\sigma^2$, with $w$ missing; context ((6.168)) implies $w^\top x_n$. I wrote it that way.
- **Fig. 6.8.** The $R^2$ values in the image are (a) true parameters: 0.411, 0.443, 0.597, 0.390; (b) EM parameters: 0.247, 0.438, 0.238, 0.263. EM values are lower in all four panels. "Almost as good" is the author's description.
- **Notation slips.** Algorithm 6.5 line 5 writes $\epsilon_n$ (text: $\epsilon_{n+1}$). $Q(\theta,\theta^{t-1})$ in (6.152) versus $Q(\theta,\theta^t)$ in (6.147). In (6.178) $\mu_n^s$ is undefined; I read it as the $s$-th posterior sample. In (6.188) $N_t$ is undefined (presumably $K$). §6.7.4 says "DBO" where EDA is meant. In §6.7.5.1, "$K$'th smallest value" sits oddly with $v_{t,i}\ge v^*_{t,K}$ selecting the top $K$. In (6.189) the entropy is printed without brackets; I read it as the binary entropy. In §6.7.6.3 the printed $f(x+\sigma\epsilon)$ should read $f(\mu+\sigma\epsilon)$, given $x=\mu+\sigma\epsilon$, and $\epsilon$ is standardized.
- **Stepwise EM (p. 297).** The text says "local upper bound" for a maximization-oriented bound; I report it as printed.
- No equation was unreadable in the page images.
