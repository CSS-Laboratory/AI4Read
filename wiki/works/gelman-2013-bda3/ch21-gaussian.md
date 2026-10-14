---
id: gelman-2013-bda3/ch21-gaussian
work: gelman-2013-bda3
unit: 21 Gaussian process models
pages: 501-518
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
# Gaussian process models

## L0 — One line
A Gaussian process puts a prior directly on an unknown function, and, with a chosen covariance function (which sets smoothness and structure), the same idea supports smooth nonlinear regression and time-series decomposition through multivariate-normal formulas, and density estimation via a transformation.

## L1 — The gist (≤ 120 words)
Chapter 20's basis-function methods typically require choosing a somewhat arbitrary set of knots. This chapter sets up a prior on the regression function itself and shows how to compute with it. A Gaussian process (GP) is defined by a mean function and a covariance function. With Gaussian noise the conditional posterior (given the covariance parameters) is again a GP, with explicit mean and covariance formulas, but computing them costs O(n³). Covariance functions can be added or multiplied to encode structure such as smoothness, periodicity and multiple scales. For non-Gaussian data the GP sits on a latent function, handled by MCMC or by Laplace and other approximations. Examples: US birthdays, leukemia survival, density estimation. The chapter shows one modelling tool applied to several problems.

**Prerequisites:** multivariate normal conditioning (BDA §3.5); marginal likelihood; Laplace/normal approximation; generalized linear model link functions; basic MCMC.

## L2 — Key ideas (5–10 bullets)
- A GP prior $\mu\sim\mathrm{GP}(m,k)$ means any finite set of function values is multivariate normal. Smoothness and scale are controlled by the covariance function, e.g. the squared exponential with amplitude $\tau$ and length scale $l$ (pp. 501–502).
- A basis-function model with a Gaussian prior on the coefficients induces a GP. Conversely, typical GPs have infinite-basis representations (p. 502).
- With Gaussian noise the GP is conditionally conjugate, so the predictive mean and covariance have explicit formulas (given the covariance parameters; the GP prior stays Gaussian after the data). The cost is $O(n^3)$; fitting becomes challenging when $n$ exceeds a few thousand and there are more than about 3 predictors or about 15 hyperparameters (p. 503). Sparse, reduced-rank, Markov-random-field and additive approximations can reduce it (p. 504).
- Per-predictor length scales $l_j$ with hyperpriors can let unneeded predictors drop out (p. 503). Sums and products of covariance functions build structured models (pp. 502–503).
- The birthday example decomposes a 20-year series into trend, weekly, seasonal and holiday components by summing GPs. Leave-one-out predictive accuracy (lppd) improves from 2074 to 2477 with the improved model (pp. 505–510).
- For non-Gaussian likelihoods the GP is latent. Inference uses GP-specific MCMC samplers or Gaussian (Laplace), expectation propagation (EP) or variational approximations; the leukemia example finds nonlinearities and an interaction without specifying them (pp. 510–512).
- GPs also give functional data analysis, and nonparametric density estimation or regression via the logistic GP and the latent-variable regression (pp. 512–515).

## L3 — Walkthrough

### Introduction (p. 501)
- Chapter 20's splines and kernel regressions typically require choosing a somewhat arbitrary set of knots. A fine grid is costly, a coarse grid may be inflexible (p. 501).
- Alternative: a prior on the regression function through a *Gaussian process*. It is a class of models in which any finite-dimensional marginal is Gaussian, viewed as a possibly infinite-dimensional generalization of the Gaussian distribution (p. 501).

### 21.1 Gaussian process regression
**Definition (p. 501).** $\mu\sim\mathrm{GP}(m,k)$, with mean function $m$ and covariance function $k$. At any $n$ prespecified points,
$$\mu(x_1),\dots,\mu(x_n)\sim \mathrm N\big((m(x_1),\dots,m(x_n)),\,K(x_1,\dots,x_n)\big).$$
- $K$ is the $n\times n$ matrix with entry $(p,q)=k(x_p,x_q)$ (p. 501).
- The model is nonparametric: infinitely many parameters, the values of $\mu(x)$ at all $x\in\mathcal X$ (p. 501).
- The mean is an initial guess. A linear model $m(x)=X\beta$ is a convenient special case, possibly with a hyperprior on $\beta$ (p. 501).
- Centering on a linear model addresses the curse of dimensionality, because the posterior can stay close to the linear model as far as the data support. It also helps interpolation across sparse data regions (p. 501).
- The covariance function controls smoothness and the degree of shrinkage towards the mean (p. 501).

**Squared exponential covariance (p. 502):**
$$k(x,x')=\tau^2\exp\!\Big(-\frac{|x-x'|^2}{2l^2}\Big).$$
- $\tau$ controls magnitude and $l$ controls smoothness. Footnote: some literature uses $\alpha=1/(2l^2)$ (p. 502).
- Figure 21.1 shows prior draws for $(\tau,l)=(1/2,2),(1/4,1/2),(1/2,1/2)$ (p. 502).

**Link to basis expansions (p. 502).** Let $\mu(x)=\sum_{h=1}^H\beta_h b_h(x)$ with $\beta\sim \mathrm N(\beta_0,\Sigma_\beta)$. Then $(\mu(x_1),\dots,\mu(x_n))$ is $n$-variate normal, with
$$m(x)=b(x)\beta_0,\qquad k(x,x')=b(x)^{T}\Sigma_\beta b(x'),\qquad b(x)=(b_1(x),\dots,b_H(x)).$$
- The converse also holds: GPs with typical covariances, such as the squared exponential, have infinite basis-expansion representations. Truncated expansions can speed computation (p. 502).

*Intuition note.* A basis model with a Gaussian prior on its coefficients already induces a GP, and conversely typical GPs such as the squared exponential can be written as infinite basis expansions (p. 502). The covariance function gives the covariance of the process at any two points (p. 501); more similar $x,x'$ imply more similar $f,f'$ (p. 513).

**Covariance functions (pp. 502–503).**
- Different covariance functions encode smoothness, nonstationarity, periodicity and multiscale or hierarchical structure. Sums and products of GPs are GPs, so covariance functions combine easily (p. 502).
- A linear model can be presented as a GP with a dot-product covariance. This is not typically the computationally most efficient form, but it makes it easy to extend hierarchical GLMs with nonlinear effects and implicit interactions (p. 502).
- With several predictors a single $l$ (isotropic GP) is typically not ideal when the response changes faster in some predictors than others. A subset of predictors may also predict as well (p. 503).
- Anisotropic version (p. 503):
$$k(x,x')=\mathrm{cov}(\mu(x),\mu(x'))=\tau^2\exp\Big(-\sum_{j=1}^p\frac{(x_j-x_j')^2}{2l_j^2}\Big).$$
- Hyperpriors on the $l_j$ give nonparametric variable selection: unneeded predictors drop out with large $l_j$ (p. 503).

**Inference (p. 503).** Observation model $y_i\sim \mathrm N(\mu_i,\sigma^2)$. The GP prior is conditionally conjugate given $\tau,l,\sigma$, so the conditional posterior of $\mu$ is again a GP with updated mean and covariance (p. 503).
- In practice one works with $\mu$ at the data points $x=(x_1,\dots,x_n)$ and at new points $\tilde x$ (p. 503).
- For prior $\mathrm{GP}(0,k)$, $y$ and $\tilde\mu$ are jointly Gaussian; noise variance $\sigma^2$ is added to the diagonal for $y$:
$$\begin{pmatrix}y\\ \tilde\mu\end{pmatrix}\sim \mathrm N\left(\begin{pmatrix}0\\0\end{pmatrix},\begin{pmatrix}K(x,x)+\sigma^2I & K(\tilde x,x)\\ K(x,\tilde x)& K(\tilde x,\tilde x)\end{pmatrix}\right).$$
- Conditioning (as in the known-variance multivariate normal model, §3.5) gives, for zero prior mean (p. 503):
$$\tilde\mu\mid x,y,\tau,l,\sigma\sim \mathrm N(\mathrm E(\tilde\mu),\mathrm{cov}(\tilde\mu)),$$
$$\mathrm E(\tilde\mu)=K(\tilde x,x)(K(x,x)+\sigma^2I)^{-1}y,$$
$$\mathrm{cov}(\tilde\mu)=K(\tilde x,\tilde x)-K(\tilde x,x)(K(x,x)+\sigma^2I)^{-1}K(x,\tilde x).$$
- Shapes (added step): $K(x,x)$ is $n\times n$, $K(\tilde x,x)$ is $\tilde n\times n$, $y$ is $n\times1$.
- Figure 21.2 shows posterior draws given ten data points, $\sigma=0.1$ and the same three $(\tau,l)$ settings as Figure 21.1. In usual analysis $\tau,l$ get priors and are inferred jointly (pp. 503–504).

*Intuition note.* The posterior mean is a weighted sum of the observed $y$'s, with weights from the covariance between the new point and the data. The posterior variance is the prior variance minus what the data explain.

**Hurdle: cost (p. 503).** The matrix inversion is $O(n^3)$ and must be repeated, for example at each MCMC step with changing hyperparameters. Fitting becomes challenging when $n$ is greater than a few thousand and the number of predictors is greater than 3 or the number of hyperparameters is greater than 15 or so (p. 503).

**Covariance function approximations (p. 504).**
- Some GPs can be written as Markov random fields. With three or fewer predictors, conditional independence gives a sparse precision matrix. Univariate: $O(n)$ by sequential inference, fine for $n$ over a million. Spatial: $O(n^{3/2})$ with specific algorithms (p. 504).
- In low dimensions, basis approximations with $m\ll n$ basis functions are possible. Choosing basis functions gets harder as dimension grows (p. 504; see §20.3).
- For many predictors, model the latent function as additive (a sum of low-dimensional parts). Interactions of 2 or 3 predictors can be included in each component. Implicit interactions between arbitrary predictors cannot easily be computed (p. 504).
- Rapid change means a short length scale. Then compact-support covariance functions give sparse matrices, even with tens of predictors (p. 504).
- Smooth functions mean a long length scale. Then reduced-rank approximations cut the inversion time to $O(mn^2)$ with $m\ll n$. They can be used for high-dimensional data, but small error everywhere may be harder to achieve (p. 504).
- Approximations can be combined in additive models, for short and long length scales (p. 504).

**Marginal likelihood and posterior (pp. 504–505).** With a Gaussian data model one integrates out $\mu$:
$$\log p(y\mid\tau,l,\sigma^2)=-\frac n2\log(2\pi)-\frac12\log|K(x,x)+\sigma^2I|-\frac12y^{T}(K(x,x)+\sigma^2I)^{-1}y.\tag{21.1}$$
- Combined with the prior it gives the unnormalized marginal posterior of the hyperparameters, and inference follows Chapters 10–13 (p. 504).
- Figure 21.3 (same ten points): marginal posteriors of $\tau,l,\sigma$ and posterior mean with pointwise 90% bands for $\mu(x)$. Slice sampling, priors $t_4^+(0,1)$ for $\tau$ and $l$, log-uniform for $\sigma$ (p. 505).

### 21.2 Example: birthdays and birthdates
**Data and aim (p. 505).** Records of all US births per day, 1969–1988. The authors had read of fewer births on Halloween and more on Valentine's Day, and wanted day-of-week, within-year and long-term patterns too (p. 505).

**First model** (additive; $t$ = day, $t=1$ is 1 Jan 1969) (pp. 505–506):
$$y_t(t)=f_1(t)+f_2(t)+f_3(t)+f_4(t)+f_5(t)+\epsilon_t.$$
1. $f_1\sim\mathrm{GP}(0,k_1)$, long-term trend: $k_1(t,t')=\sigma_1^2\exp(-|t-t'|^2/2l_1^2)$ (p. 505).
2. $f_2$: shorter-term variation, same form with other amplitude and scale $\sigma_2,l_2$ (p. 505).
3. $f_3$: weekly quasi-periodic pattern allowed to change over time, product of periodic and squared exponential kernels (p. 505):
$$k_3(t,t')=\sigma_3^2\exp\Big(-\frac{2\sin^2(\pi(t-t')/7)}{l_{3,1}^2}\Big)\exp\Big(-\frac{|t-t'|^2}{2l_{3,2}^2}\Big).$$
4. $f_4$: yearly smooth seasonal pattern, period 365.25, with $s=t \bmod 365.25$ (aligns with the calendar every four years) (p. 506):
$$k_4(s,s')=\sigma_4^2\exp\Big(-\frac{2\sin^2(\pi(s-s')/365.25)}{l_{4,1}^2}\Big)\exp\Big(-\frac{|s-s'|^2}{2l_{4,2}^2}\Big).$$
5. $f_5(t)=I_{\text{special day}}(t)\beta_a+I_{\text{weekend}}(t)I_{\text{special day}}(t)\beta_b$. Here $I_{\text{special day}}(t)$ is a row of 13 indicators (New Year's Day, Valentine's Day, Leap Day, April Fool's Day, Independence Day, Halloween, Christmas, days between Christmas and New Year's). $I_{\text{weekend}}=1$ on Saturday/Sunday. $\beta_a,\beta_b$ (length 13) are the effects on weekdays and weekends (p. 506).
6. $\epsilon_t\sim \mathrm N(0,\sigma^2)$ (p. 506).

- Priors: weakly informative log-$t$ priors on the time scales $l$ (to improve identifiability), log-uniform on other hyperparameters. $y$ normalized to mean 0, sd 1 (p. 506).
- The sum of GPs is a GP: $k=k_1+\dots+k_5$, so inference uses the basic GP equations (p. 506).
- Computation: marginal likelihood and gradients analytically via (21.1); marginal posterior mode for hyperparameters. This was fine for $n\approx20\cdot365.25$. CCD integration gave visually indistinguishable plots; MCMC would have been too slow. $O(n^3)$ is not optimal for one-dimensional data, but time was reasonable (p. 506).
- Component predictions use only one component's covariance between training and test points (p. 506):
$$\mathrm E(\tilde f_1)=K_1(\tilde x,x)(K(x,x)+\sigma^2I)^{-1}y.\tag{21.2}$$
- Figure 21.4 shows the components on one scale, relative to a baseline of 100. Interpretations offered: the seasonal effect is inversely related to daylight or average temperature nine months before; fewer weekend births and smaller or larger numbers on special days may be explained by selective c-sections and induced births; day-of-week patterns grow over time (p. 506).

**Improved model (pp. 507–510).** Problems noticed: choosing only some special days makes it impossible to find other days with large effects. A "ringing" pattern around special days is also expected. Residuals were slightly autocorrelated (p. 507).
$$y_t(t)=f_1+\dots+f_8+\epsilon_t.$$
- $f_1,f_2,f_3$ as before (p. 508).
- $f_4$: as in the first model but with period 365 and a modified time $s$, where time before and after leap day is incremented by 0.5 day so that the year has length 365 also in leap years (p. 508).
- $f_5$: yearly fast-changing weekday day-of-year effect, $k_5(t,t')=I_{\text{weekday}}(t,t')\sigma_5^2\exp(-2\sin^2(\pi(s-s')/365)/l_5^2)$. The indicator is 1 if both $t,t'$ are weekdays (p. 508).
- $f_6$: the same for weekends, with $I_{\text{weekend}}(t,t')$ equal to 1 if both are Saturday/Sunday (p. 508).
- $f_7=I_{\text{special day}}(t)\beta$ with 4 indicators for floating holidays: Leap Day, Memorial Day, Labor Day, Thanksgiving (p. 508).
- $f_8$: short-term squared exponential GP. $\epsilon_t\sim\mathrm N(0,\sigma^2)$ (pp. 508–509).
- Same priors and normalization (p. 509).
- Leave-one-out predictions are computable in about the cost of posterior predictions. lppd$_{\text{loo-cv}}=2074$ (first model) and $2477$ (improved), "clear improvement" (p. 509).
- Figure 21.5: trends and day-of-week effect indistinguishable from the first model. The seasonal component is smoother, since pre- and post-holiday effects and year-end effects now sit in the day-of-year component (pp. 509–510).
- The authors say the model is not perfect. For example, local positive and negative effects could be constrained to average about zero, so extra babies are "borrowed" from neighbouring days. They believe the decomposition identifies the major patterns at different time scales (p. 510).

*Intuition note.* Each GP term gets its own length scale, so slow trends, weekly cycles and day-of-year effects are modelled together at different scales. The authors say they could keep adding terms without losing control of the estimation (p. 510).

### 21.3 Latent Gaussian process models
- For non-Gaussian likelihoods the GP prior is placed on a latent $f$, linked to the likelihood $p(y|f,\phi)$ as in GLMs (Ch. 16). $\phi$ is typically a scalar shape parameter. A separate latent GP could model it, e.g. to let the scale depend on predictors (p. 510).
- Conditional posterior: $p(f|x,y,\theta,\phi)\propto p(y|f,\phi)p(f|x,\theta)$ (p. 510).
- GP-specific samplers exploit the Gaussian prior in the proposal or in scaling the latent variables: elliptic slice sampler, scaled Metropolis–Hastings, scaled HMC/NUTS. Sampling typically alternates between $f$ and the parameters $\theta,\phi$. Dependence between latent values and (hyper)parameters can make mixing slow for larger datasets (p. 510).
- Because the prior is Gaussian, the latent posterior is often close to Gaussian. Normal approximation (Ch. 4), as printed on p. 510:
$$p(f|x,y,\theta,\phi)\approx\mathrm N(f|\hat f,\Sigma),\qquad \Sigma^{-1}=K(x,x)+W,$$
where $\hat f$ is the posterior mode and $W$ is diagonal with $W_{ii}=\frac{d^2}{df^2}\log p(y|f_i,\phi)\big|_{f_i=\hat f_i}$ (p. 510).
- The approximate predictive density $p(\tilde y_i|\tilde x_i,x,y,\theta,\phi)\approx\int p(\tilde y_i|\tilde f_i,\phi)\,\mathrm N(\tilde f_i|\cdot)\,d\tilde f_i$ can be evaluated by quadrature (p. 510).
- Laplace approximation to the log marginal likelihood (§13.3):
$$\log p(y|x,\theta,\phi)\approx\log g(y|x,\theta,\phi)\propto\log p(y|\hat f,\phi)-\tfrac12\hat f^{T}K(x,x)^{-1}\hat f-\tfrac12\log|B|,\tag{21.3}$$
with $|B|=|I+W^{1/2}K(x,x)W^{1/2}|$ (p. 510).
- If the likelihood contribution is heavily skewed (as can happen with the logistic model), expectation propagation (§13.8) can be used. Variational approximation (§13.7) has been used but in many cases is slower than the normal approximation and less accurate than EP (p. 510).
- With an analytic latent approximation, the marginal posterior of hyperparameters and its gradients are analytic. One can find its mode (§13.1) or integrate by MCMC, grid or CCD (pp. 510–511).

**Example: leukemia survival times (pp. 511–512).**
- Data: survival time $t$ and censoring indicator $z$ (0 observed, 1 censored) for 1043 acute myeloid leukemia cases, North West Leukemia Register (UK), 1982–1998. 16% censored. Predictors: age, sex, white blood cell count (WBC; 1 unit $=50\times10^9/$L), Townsend deprivation score (p. 511).
- WBC is strictly positive and skewed, so its logarithm is used. With finite $n$ sensible transformations help even though a GP could in theory learn a link. Continuous predictors standardized; log survival time centred (p. 511).
- Models tried: proportional hazard, Weibull, log-Gaussian, log-logistic. Log-logistic gave the best results. It is considered more robust than log-Gaussian. There is no model for the censoring process, so no full observation model (p. 511).
- Likelihood, as printed (shape $r$, censoring $z_i$; see §8.7):
$$p(y|-)=\prod_{i=1}^n\Big(\frac{r y^{r-1}}{\exp(f(X_i))}\Big)^{1-z_i}\Big(1+\Big(\frac{y}{\exp(f(X_i))}\Big)^r\Big)^{z_i-2}.$$
- Latent model centred on a linear model: $f_i(X_i)=\alpha+X_i\beta+\mu(X_i)$, with $\mu\sim\mathrm{GP}(0,k)$, $k(x,x')=\sigma_g^2\exp(-\sum_{j=1}^p|x_j-x_j'|^2/2l_j^2)$ (p. 511).
- Priors: uniform on $\log r$; $\alpha\sim\mathrm N(0,\sigma_\alpha^2)$; $\beta\sim\mathrm N(0,\sigma_\beta^2)$; independent Inv-$\chi^2(1,1)$ on $\sigma_\alpha^2,\sigma_\beta^2,\sigma_g^2$; $l_j\sim\text{Cauchy}^+(0,1)$ (p. 511).
- Laplace for latent values, CCD for hyperparameters. EP gave similar results but was an order of magnitude slower. LOO predictions (linear response and importance weighting) took three times the posterior inference (p. 511).
- lppd$_{\text{loo-cv}}=-1662$ for constant plus linear components; $-1629$ with nonlinear components, a clear improvement (p. 511).
- Figure 21.6 shows conditional comparisons, with the thick line the posterior median and thin lines pointwise 90% intervals. The model finds clear nonlinear patterns and an interaction of WBC with the Townsend index, without explicit parametric forms or interaction terms (pp. 511–512).
- Previous studies did not log-transform WBC and so did not find the decrease in expected lifetime at small WBC. They considered only additive models and so missed the interaction. An added spatial component explained some variation but had no significant effect when added to the model here (p. 512).

### 21.4 Functional data analysis (pp. 512–513)
- Functional data analysis treats a subject's response as a random function observed at finitely many points. Observations $y_i=(y_{i1},\dots,y_{in_i})$ on function $f_i$ at $t_{ij}\in\mathcal T$ (example: blood pressure or body weight against age). With measurement error, $y_{ij}\sim\mathrm N(f_i(t_{ij}),\sigma^2)$ (p. 512).
- The question is how to model $\{f_i\}_{i=1}^n$ with flexible individual functions while borrowing information (p. 512).
- With subject predictors $x_i$: $y_{ij}\sim\mathrm N(f(x_i,t_{ij}),\sigma^2)$, $f\sim\mathrm{GP}(m,k)$. Add time as a dimension (p. 513):
$$\tau^2\exp\Big(-\Big[\sum_{j=1}^p\frac{(x_j-x_j')^2}{2l_j^2}+\frac{(t-t')^2}{2l_{p+1}^2}\Big]\Big).$$
- More similar $x,x'$ imply more similar $f,f'$. No additional computational methods are needed (p. 513).

### 21.5 Density estimation and regression (pp. 513–515)
Aim: make the observation model nonparametric too. One way is the logistic Gaussian process (LGP); Dirichlet-process alternatives come in later chapters (p. 513).

**Density estimation (iid case) (p. 513).** Draw a random function from a GP, then transform it to a density by the continuous logistic transformation:
$$p(y|f)=\frac{e^{f(y)}}{\int e^{f(y')}dy'},\qquad f\sim\mathrm{GP}(m,k).$$
- It is appealing to take $m$ as the log density of an elicited parametric distribution such as Student's $t$, with parameters chosen empirically or integrated out. $k$ can be squared exponential, $k(y,y')=\tau^2\exp(-|y-y'|^2/2l^2)$ (p. 513).
- Alternative: zero-mean GP $W(t)$ on $[0,1]$ and
$$p(y)=g_0(y)\frac{e^{W(G_0(y))}}{\int e^{W(v)}dv},$$
with $g_0$ an elicited parametric density with cdf $G_0$. This compactification maps a GP from $[0,1]\to\Re$ and makes the prior smoother on the tails of $g_0$, sometimes desirable (p. 513).
- Challenge: the integral in the denominator, computed via a finite basis representation or a discretization of a finite region. Inference uses Markov chain simulation, or Laplace for $f$ with quadrature for parameters. Compared with mixture density estimation (Chs. 22–23), the LGP has a computational advantage: the posterior of $f$ is unimodal given hyperparameters and a fixed finite representation (pp. 513–514).

**Example: galaxies and lakes (p. 514).**
- 82 speeds of galaxies diverging from ours; acidity of 155 lakes in north-central Wisconsin.
- Matérn ($\nu=5/2$) covariance, centred on a Gaussian. Laplace for $f$, marginal posterior mode for hyperparameters. A prior constraint forcing decreasing tails is implemented by rejection sampling.
- Versus the Gaussian-mixture estimate in Figure 22.4, the LGP gives a more flexible density form (Figure 21.7).

**Density regression (pp. 514–515).**
$$p(y|x)=\frac{e^{f(x,y)}}{\int e^{f(x,y')}dy'},$$
with $f$ a GP and, for example,
$$k((x,y),(x',y'))=\tau^2\exp\Big(-\Big[\sum_{j=1}^p\frac{(x_j-x_j')^2}{2l_j}+\frac{(y-y')^2}{2l_{p+1}}\Big]\Big).\tag{21.4}$$
(printed as such; see Reading notes). Hyperpriors on the $l_j$ can let some predictors drop out (p. 514).
- Compactified version: $s\in[-1,1]^p$, $t\in[0,1]$, monotone continuous $F_j:\Re\to[-1,1]$, $F(x)=(F_1(x_1),\dots,F_p(x_p))$:
$$p(y|x)=g_0(y)\frac{e^{W(F(x),G_0(y))}}{\int e^{W(F(x),v)}dv},$$
with $W$ a GP. Inference is like the unconditional case, with extra difficulty when many predictors need approximations (p. 515).

**Latent-variable regression (p. 515).** A simple alternative that induces a prior on densities in a fundamentally different way:
$$y_i\sim\mathrm N(\mu(u_i),\sigma^2),\qquad u_i\sim\mathrm U(0,1),\tag{21.5}$$
with $\mu:[0,1]\to\Re$ unknown. The prior on $(\mu,\sigma)$ induces a prior $f\sim\Pi$ on the density of $y_i$ (p. 515).
- Intuition: one can sample $y_i\sim f_0$ for any strictly positive density $f_0$ by drawing uniform $u_i$ and setting $y_i=F_0^{-1}(u_i)$. This suggests (21.5) is flexible given a flexible prior on $\mu$ and a prior on $\sigma^2$ with positive probability near zero (p. 515).
- Practical choice: $\mu$ a GP centred at $\mu_0$ with squared exponential kernel. To centre on a guess $g_0$, take $\mu_0\equiv G_0^{-1}$, which helps if $g_0$ is a decent approximation (p. 515).
- Computation by data augmentation: given the $u_i$, (21.5) is a standard GP regression, updating $\mu$ at the unique $u_i$ from a multivariate Gaussian conditional. Approximating $\mathrm U(0,1)$ by a discrete uniform on a fine grid enables conjugate updating of the $u_i$ and reduces the cost of updating $\mu$ (p. 515).
- Density regression: $y_i\sim\mathrm N(\mu(u_i,x_i),\sigma^2)$, $u_i\sim\mathrm U(0,1)$, with $\mu:\Re^{p+1}\to\Re$ a GP surface. The covariance can have a separate range parameter per dimension as in (21.4), so unneeded predictors can drop out (p. 515).

### 21.6 Bibliographic note (p. 516)
- Key references named: O'Hagan (1978), Neal (1998), Rasmussen and Williams (2006). Software accompanies the last and Vanhatalo et al. (2013b) (p. 516).
- Data sources: birthday data from the National Vital Statistics System natality data; leukemia example from Henderson, Shimakura and Gorst (2002). LGP introduced by Leonard (1978). The latent-variable regression comes from Kundu and Dunson (2014) (p. 516).

### 21.7 Exercises (pp. 516–518)
Nine exercises, listed under "Exercises worth doing".

## Toy example (ours; not from the text)
Zero-mean GP, squared exponential kernel with $\tau=1$, $l=1$, noise $\sigma=0.5$ so $\sigma^2=0.25$. One observation: $x_1=0$, $y_1=1$. Predict at $\tilde x=0,1,3$.
- $K(x,x)+\sigma^2I=1+0.25=1.25$ (a $1\times1$ matrix).
- $\tilde x=0$: $K(\tilde x,x)=1$. Mean $=1\cdot1/1.25=0.8$. Variance $=1-1^2/1.25=0.2$.
- $\tilde x=1$: $K(\tilde x,x)=e^{-1/2}=0.6065$. Mean $=0.6065/1.25=0.4852$. Variance $=1-0.6065^2/1.25=1-0.36788/1.25=1-0.29430=0.7057$.
- $\tilde x=3$: $K=e^{-9/2}=0.011109$. Mean $=0.011109/1.25=0.00889$. Variance $=1-0.00012341/1.25=1-0.0000987=0.99990$.
- Log marginal likelihood (21.1), $n=1$: $-\tfrac12\log(2\pi)-\tfrac12\log1.25-\tfrac12(1^2/1.25)=-0.9189-0.1116-0.4000=-1.4305$.

Reading: the mean is pulled toward 0 (0.8 instead of 1, because of noise), and the pull grows with distance. At the data point the variance drops from 1 to 0.2. Far away, mean and variance return to the prior values 0 and 1.

## Concepts
- [[gaussian-process]] (new) — random function whose values at any finite set of points are multivariate normal; defined by mean function $m$ and covariance function $k$ (p. 501)
- [[covariance-function]] (new) — $k(x,x')$, controls smoothness and shrinkage; sums and products are again covariance functions (pp. 501–502)
- [[length-scale-amplitude]] (new) — $l$ sets smoothness, $\tau$ sets magnitude in the squared exponential kernel; per-predictor $l_j$ for anisotropy and variable selection (pp. 502–503)
- [[prior-distribution]] — here a GP prior on the unknown function $\mu(x)$ (p. 501)
- [[posterior-distribution]] — with Gaussian noise the conditional posterior of $\mu$ is again a GP (p. 503)
- [[conjugate-prior]] — GP is conditionally conjugate given $\tau,l,\sigma$ under a Gaussian observation model (p. 503)
- [[marginal-likelihood-evidence]] — (21.1), $\mu$ integrated out analytically; used for hyperparameter inference (p. 504)
- [[additive-gp-model]] (new) — sum of GPs with different covariance functions, one per scale or structure (pp. 505–506)
- [[latent-gaussian-process-model]] (new) — GP on latent $f$ linked to a non-Gaussian likelihood; inference by GP-specific MCMC or Laplace/EP/VI (p. 510)
- [[laplace-approximation]] (new) — normal approximation at the latent posterior mode; also approximates the log marginal likelihood (21.3) (p. 510)
- [[cross-validation-loo-waic]] — lppd$_{\text{loo-cv}}$ used to compare GP models (pp. 509, 511)
- [[markov-chain-monte-carlo]] — slice sampler, elliptic slice, scaled MH, scaled HMC/NUTS for GPs (pp. 505, 510)
- [[logistic-gaussian-process]] (new) — density prior from exponentiating and normalizing a GP draw (p. 513)
- [[latent-variable-regression-density]] (new) — $y_i\sim\mathrm N(\mu(u_i),\sigma^2)$, $u_i$ uniform, GP prior on $\mu$ (p. 515)
- [[functional-data-analysis]] (new) — modelling subjects' responses as random functions, with time as an extra GP input dimension (pp. 512–513)

## Canonical instances
- [[birthdays-gp-decomposition]] — US daily births 1969–1988 as a sum of GPs; lppd 2074 → 2477 (pp. 505–510)
- [[leukemia-aml-loglogistic-gp]] — latent GP on a log-logistic survival model; finds nonlinearity and WBC×deprivation interaction (pp. 511–512)
- [[galaxy-acidity-lgp-density]] — LGP density estimates for 82 galaxy speeds and 155 lake acidities (p. 514)

## Bridges (candidates)
- [same-math] GP posterior mean/covariance ↔ multivariate normal conditioning (BDA §3.5): the formulas on p. 503 are Gaussian conditioning.
- [same-math] Basis model with Gaussian coefficient prior ↔ GP with $k=b(x)^T\Sigma_\beta b(x')$ (p. 502).
- [structural-analogy] Hyperpriors on per-predictor $l_j$ ↔ variable selection/shrinkage: large $l_j$ removes a predictor.
- [structural-analogy] Sum of GP components ↔ iterative model building (Bayesian workflow): adding terms after seeing misfit (pp. 507–510).
- [structural-analogy] Latent-variable regression via $y=F_0^{-1}(u)$ ↔ inverse-CDF sampling (p. 515).

## Questions this raises
- How do the 365-day and 365.25-day period choices, and the leap-day handling, change the fitted seasonal component?
- When does the Laplace approximation to the latent posterior fail, and how would one detect that without running EP?
- How sensitive are the fitted curves to the $t_4^+$/log-$t$ hyperpriors on $l$ when data are sparse?
- Which approximations in the reduced-rank/sparse family are most reliable when there are many predictors?

## Exercises worth doing
- Ex. 1 (p. 516) — sample from the GP prior as in Fig. 21.1, invent data, compute and sample the posterior; builds basic intuition — difficulty: easy
- Ex. 2 (pp. 516–517) — full Bayesian GP fit of the proportion who know someone gay as a function of age, including coding the hyperparameter log posterior from (21.1) — difficulty: medium
- Ex. 3 (p. 517) — repeat with a binomial likelihood (latent GP) and compare — difficulty: hard
- Ex. 6 (p. 517) — replicate the birthday model by adding covariance functions one by one, then let day-of-year effects grow over time — difficulty: hard
- Ex. 8 (p. 517) — can a prior on basis coefficients with $b_h(x)=\exp(\psi(x-\tau_h)^2)$ give a GP? Find $m,k$ and compare to the squared exponential — difficulty: medium
- Ex. 9 (pp. 517–518) — does a Gaussian prior on $\beta_1,\beta_2$ in $\mu=\beta_1+\beta_2x$ induce a GP, and can it capture nonlinear functions? — difficulty: easy

## Reading notes
- Printed page = pdf − 10 (pdf 511 = printed 501). Pages 501–518 (pdf 511–528).
- The text layer shows $\sim$ as "→" and some symbols garbled. On p.
- p. 505: the sentence "Based on the structural knowledge of the calendar and, we started…" is garbled as printed.
- Cross-references: pp. 506 and 516 call the posterior prediction equation "(21.1)", but (21.1) is the log marginal likelihood; the posterior mean/covariance formulas on p. 503 are unnumbered. Likely misreferences.
- p. 510, as printed: $\Sigma^{-1}=K(x,x)+W$, with $W_{ii}$ the second derivative of the log likelihood (no minus sign). (21.3) uses $K^{-1}$ and $|I+W^{1/2}KW^{1/2}|$, which suggests $K^{-1}+W$ may have been intended. The printed form is copied here.
- (21.4), p. 514: denominators printed as $2l_j$ and $2l_{p+1}$ without squares, unlike the $2l_j^2$ and $2l_{p+1}^2$ on p. 513. The image shows no squares.
- The leukemia likelihood is copied as printed (p. 511). The $r y^{r-1}$ numerator and denominator $\exp(f(X_i))$ appear as printed in the image.
- Exercise 1 (p. 516) also refers to "(21.1)" for the posterior mean and covariance.
- p. 503 announces "two main hurdles" but only the first (the $O(n^3)$ matrix inversion) is described on these pages.
