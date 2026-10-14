---
id: gelman-2013-bda3/ch20-basis
work: gelman-2013-bda3
unit: "20 Basis function models"
pages: 487-500
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Basis function models

## L0 — One line
A smooth unknown regression curve can be written as a weighted sum of fixed basis functions, which makes the model linear in the weights, so selection or shrinkage priors on the weights give flexible Bayesian regression, with computation by Gibbs sampling or related MCMC.

## L1 — The gist (≤ 120 words)
How do we fit a regression mean μ(x) of unknown shape without a parametric form? Write μ(x) = Σ β_h b_h(x) with fixed basis functions (Gaussian bumps or B-splines). Given the basis, the model is linear in β, so conjugate and Gibbs methods apply. With many basis functions and limited data, over-fitting is a risk, so the prior on β needs care. Variable-selection priors allow coefficients to be exactly zero. Continuous shrinkage priors (t, Laplace, generalized double Pareto) have computational advantages. The chapter extends this to heavy-tailed errors, generalized linear models, additive and tensor-product surfaces, and monotone curves. Examples are chloride concentration and DDE and preterm birth.

**Prerequisites:** Bayesian linear regression and conjugate normal-inverse-gamma priors; Gibbs sampling; scale mixtures of normals; probit models; matrix notation.

## L2 — Key ideas (5–10 bullets)
- Nonparametric regression with a prespecified basis is a linear model in β with design matrix W (row i = (b_1(x_i),…,b_H(x_i))). Conjugate linear-regression machinery applies directly (p. 488).
- Local bases (Gaussian radial, cubic B-spline) look alike. B-splines have compact support (each is zero outside a short interval), so W is sparse (mostly zeros); the Gaussian is smoother (pp. 487–488).
- With few data per coefficient, one option is to centre the prior on a parametric curve. The posterior mean is then shrunk toward that curve (p. 490).
- The variable-selection mixture prior (20.3) (each coefficient is zero with some probability, otherwise normal) gives analytic posterior model probabilities (20.4) when π and κ_h are fixed (κ_h = κ). There are 2^H models, so the sum is infeasible unless H is small; approximations such as Gibbs sampling or stochastic search are used. Model averaging is preferred to one selected model (pp. 491–492).
- Scale-mixture shrinkage priors (normals whose variance is itself random; t/Cauchy, Laplace, generalized double Pareto) pull small coefficients toward zero without setting posterior draws exactly to zero. The generalized double Pareto has a simple block Gibbs sampler and, with the default α=η=1, Cauchy-like tails (pp. 493–494).
- A t residual density, written as a scale mixture, downweights the influence of outliers. In the chloride example, a very large outlier (100 times the residual SD) ruined the Gaussian-error fit, while t errors with ν fixed at 4 gave results close to the uncontaminated analysis (pp. 494–495).
- For several predictors, the curse of dimensionality (needed basis functions and data grow rapidly with the number of predictors) motivates additive (20.5) or tensor-product (products of one-dimensional bases) models, with shrinkage or selection priors. Shape constraints such as monotonicity can be built into the prior (pp. 495–498).

## L3 — Walkthrough

### 20.1 Splines and weighted sums of basis functions
Chapter 19 used a prespecified parametric nonlinear mean μ(X_i, φ). Here μ itself is unknown a priori (p. 487). Replace $X_i\beta$ by $\mu(X_i)$. In one dimension:
$$\mu(x)=\sum_{h=1}^{H}\beta_h b_h(x),$$
with $b=\{b_h\}$ prespecified **basis functions** and $\beta=(\beta_1,\dots,\beta_H)$ the **basis coefficients** (p. 487).

- Taylor series are one example (polynomials of increasing degree). The author says they can require a huge number of terms globally and typically have "horrible properties" near the boundary. A finite set of well-chosen, **local** basis functions should do better. A local basis function has a centre $x_h$ and goes to zero far from it (p. 487).
- **Gaussian radial basis functions** (p. 487):
$$b_h(x)=\exp\!\Big(-\frac{|x-x_h|^2}{l^2}\Big)\tag{20.1}$$
  Here $x_h$ are centres and $l$ is a common width. The number of basis functions and $l$ control the scale at which μ can vary.
- **Cubic B-spline**: a piecewise cubic defined from knots. With uniform knots $x_{h+k}=x_h+\delta k$ (p. 488):
$$
b_h(x)=\begin{cases}
\tfrac16 u^3 & x\in(x_h,x_{h+1}),\ u=(x-x_h)/\delta\\
\tfrac16(1+3u+3u^2-3u^3) & x\in(x_{h+1},x_{h+2}),\ u=(x-x_{h+1})/\delta\\
\tfrac16(4-6u^2+3u^3) & x\in(x_{h+2},x_{h+3}),\ u=(x-x_{h+2})/\delta\\
\tfrac16(1-3u+3u^2-u^3) & x\in(x_{h+3},x_{h+4}),\ u=(x-x_{h+3})/\delta\\
0 & \text{otherwise.}
\end{cases}\tag{20.2}
$$
  The width is set by the knot spacing δ. Maximum flexibility is set by the number of knots in the data range. Knots may also be nonuniform. Each B-spline has **compact support** (is zero outside a finite interval), so the design matrix is sparse, which helps computation (p. 488).
- Figure 20.1 shows both shapes as smooth bells. Weighted sums with positive, negative or zero weights model smooth functions. The text says the Gaussian gives smoother functions because it is infinitely differentiable, while the cubic B-spline is "only three times differentiable" (p. 488).
- Figure 20.2: prior draws of μ(x) come from sampling β_h from a Gaussian prior. H limits flexibility: a spike narrower than the basis functions will be oversmoothed (p. 488).
- **Linearity.** Given b, write $y_i=\mu(x_i)+\epsilon_i=w_i\beta+\epsilon_i$, with $w_i=(b_1(x_i),\dots,b_H(x_i))$. Fitting proceeds as in linear regression. A multivariate normal-inverse-χ² prior for (β, σ²) is conjugate (p. 488). It is often useful to centre the model on a linear model:
$$\mu(x)=\beta_1+\beta_2x+\sum_{h=3}^{H+2}\beta_hb_h(x).$$

*Intuition note.* Once you fix the bumps, only their heights are unknown. That is ordinary regression with a clever set of columns. Flexibility is limited by H (and the width of the bumps), and a prior on the heights helps limit over-fitting.

**Example: chloride concentration** (pp. 489–490). There are 54 measurements of chloride over a short time (Figure 20.3). The data are close to linear with local deviations. There are 21 coefficients, so prior information is needed. One strategy is to centre the prior on a parametric curve. Let $\beta|\sigma\sim N(\beta_0,\sigma^2\lambda^{-1}I_H)$ and $\sigma^2\sim\text{Inv-gamma}(a_0,b_0)$. The prior mean curve is $\mu_0(x)=\sum_h\beta_{0h}b_h(x)$ (p. 489).

- If $\mu_0(x)=\alpha+\psi x$, least squares can choose $\beta_0$ so that $\mu_0$ is as close as possible to the line. For H = 21 here, $\mu_0$ is indistinguishable from the line. Plug in least-squares α, ψ. The posterior mean is
$$\hat\mu(x)=\mathrm E\big(\mu(x)\mid (x_1,y_1),\dots,(x_n,y_n)\big)=(W^TW+\lambda I_H)^{-1}\big(W^Ty+\lambda\hat\mu_0(x)\big),$$
  with $\hat\mu_0$ the least-squares line and $W=(w_1,\dots,w_n)^T$ (p. 490). It is shrunk toward the linear fit but allows nonparametric deviations.
- For a fuller analysis: hyperpriors on α, ψ, or a smoothing prior favouring similar adjacent coefficients. First-order autoregressive priors of this kind give Bayesian penalized (P) splines (p. 490).

**Choosing knots** (p. 490). Often it works well to take many knots (e.g. H = 21) and choose the coefficient prior carefully. Two Bayesian ways to handle uncertainty in the basis:
1. **Free-knot** approach: a prior on the number and locations of knots, with reversible jump MCMC (Section 12.3). It gives model averaging, but efficient algorithms are hard to design.
2. Priors that shrink many coefficients to near zero with heavy tails, a "continuous analogue" of variable selection. They have conceptual and computational advantages because there is no jumping between zero and nonzero.

### 20.2 Basis selection and shrinkage of coefficients
Model: $y_i\sim N(w_i\beta,\sigma^2)$, $w_i=(b_1(x_i),\dots,b_H(x_i))$, from a prespecified collection of *potential* bases (p. 490). Introduce the inclusion indicators $\gamma=(\gamma_1,\dots,\gamma_H)\in\Gamma$, with $\gamma_h=1$ meaning $b_h$ is included. The space Γ has $2^H$ elements, from $\gamma=0_H$ to $\gamma=1_H$ (p. 490).

**Variable selection mixture prior** (p. 491):
$$\beta_h\sim\pi_h\delta_0+(1-\pi_h)N(0,\kappa_h^{-1}\sigma^2),\qquad \sigma^2\sim\text{Inv-gamma}(a,b)\tag{20.3}$$
Here $\delta_0$ is a point mass at zero. This implies $\gamma_h\sim\text{Bernoulli}(1-\pi_h)$ independently and $\beta_\gamma\sim N_{p_\gamma}(0,V_\gamma\sigma^2)$, with $p_\gamma=\sum_h\gamma_h$ and $V_\gamma=\text{diag}(\kappa_h:\gamma_h=1)$ (as printed).

- With no prior knowledge, set $\pi_h=\pi$ and $\pi\sim\text{Beta}(a_\pi,b_\pi)$. This induces an automatic **multiplicity adjustment**: the more unnecessary basis coefficients are added, the stronger the tendency to set coefficients to zero. This is visible in the full conditional $\pi|-\sim\text{Beta}\big(a_\pi+\sum_h(1-\gamma_h),\,b_\pi+\sum_h\gamma_h\big)$ (p. 491).
- Heavy-tailed Cauchy prior for included coefficients: $\kappa_h\sim\text{Gamma}(0.5,0.5)$ independently. This uses the t distribution as a scale mixture of normals with an inverse-gamma mixing prior on the variance (p. 491).
- Do not use an improper prior on the nonzero coefficients: it puts high posterior probability on the null model (Section 7.4). An improper noninformative prior on σ² (a, b → 0) is fine, since σ is common to all models (p. 491).
- **Posterior model probabilities.** Assume fixed π and $\kappa_h=\kappa$. The joint posterior is conjugate and (p. 491):
$$\Pr(\gamma|y,X)=\frac{\pi^{k-p_\gamma}(1-\pi)^{p_\gamma}\,p(y|X,\gamma)}{\sum_{\gamma^*\in\Gamma}\pi^{k-p_{\gamma^*}}(1-\pi)^{p_{\gamma^*}}\,p(y|X,\gamma^*)}\quad\forall\gamma\in\Gamma\tag{20.4}$$
  with the marginal likelihood
$$p(y|X,\gamma)=\int\prod_{i=1}^nN(y_i|w_{i,\gamma}\beta_\gamma,\sigma^2)\,N(\beta_\gamma|0,V_\gamma\sigma^2)\,\text{Inv-gamma}(\sigma^2|a,b)\,d\beta_\gamma\,d\sigma^2,$$
  $w_{i,\gamma}=(w_{ih}:\gamma_h=1)$. This is the marginal likelihood of a normal linear regression under a jointly conjugate normal-gamma prior, so it has an analytic form. Given γ, $(\beta_\gamma,\sigma^2)$ is multivariate normal-inverse-gamma (p. 491).
- **Computation.** The sum in (20.4) is over $2^H$ models and is infeasible unless H is small. For H = 50 there are $2^{50}=1.1\times10^{15}$ models. Options: MCMC stochastic search plus model averaging, or Gibbs sampling of each $\gamma_h$ from its Bernoulli full conditional (pp. 491–492):
$$\Pr(\gamma_h=1\mid\gamma_{(-h)},\pi)=\Big(1+\frac{\pi}{1-\pi}\,\frac{p(y|X,\gamma_h=0,\gamma_{(-h)})}{p(y|X,\gamma_h=1,\gamma_{(-h)})}\Big)^{-1}$$
  One cycle updates $\gamma_1,\dots,\gamma_H$ in turn. After warm-up the draws represent the posterior over Γ (p. 492).
- **Selection versus averaging** (p. 492). Under 0-1 loss, the Bayes optimal model is the γ with the highest posterior probability. Unless H is small, it tends to be the case that many models have posterior probability similar to the best one, so it is misleading to base inference on any one selected model. **Model averaging** over the posterior on γ is preferred for summaries of μ and for prediction. If a single model is wanted, the **median probability model** (include basis $h$ if $\Pr(\gamma_h=1|\text{data})>0.5$) may be a better alternative than the maximum-posterior model. It is the best single-model approximation to Bayes model averaging for orthogonal basis functions.

*Intuition note.* Each of the $2^H$ subsets of bumps is a model. The prior says each bump is in with probability $1-\pi$, and the data reweight the subsets. Averaging over many near-tied subsets is more honest than picking one.

**Example: chloride (continued)** (p. 492).
- All 21 basis functions with a weakly informative N(0, I) or N(0, 2²I) prior gave an extremely poor fit: the posterior mean curve was shifted far down toward zero, the prior centre.
- With inclusion probability 0.5 per basis function, N(0, 2²) priors on included coefficients and σ² ~ Inv-gamma(1, 1), a Gibbs sampler ran in a few seconds in R.
- The posterior mean number of included bases is 12.0 (95% interval [8.0, 16.0]). The posterior mean of σ is 0.27 (95% interval [0.23, 0.33]), suggesting small measurement error.

**Sensitivity to the basis** (p. 492). Using H = 21 cubic B-splines implicitly says the curve is quite smooth. If spikes are expected, one may use wavelets or another basis, or include several basis types and let variable selection choose. Prior information should inform the basis and coefficient prior whenever possible.

**Shrinkage priors** (pp. 492–494).
- *Why.* When $2^H$ is enormous, MCMC cannot realistically be said to converge: only a small percentage of models are visited even in several hundreds of thousands of iterations. Mixing can be slow with one-at-a-time updates, and block sizes are limited. Nonconjugate priors make it worse. None of this arose in the chloride data, but it may with multiple predictors (pp. 492–493).
- *Idea.* Avoid setting any coefficient exactly to zero. Use a prior with high density at zero and heavy tails (to avoid over-shrinking the signal) (p. 493). Most useful shrinkage priors are scale mixtures of Gaussians:
$$\beta_h\sim N(0,\sigma_h^2),\qquad\sigma_h^2\sim G.$$
- **t prior:** $G=\text{Inv-gamma}(\nu/2,\nu/2)$ gives a t with ν degrees of freedom. The machine-learning limit ν → 0 is a normal-Jeffreys prior. The posterior is improper, so Bayesian inference is meaningless, but the posterior mode can have $\sigma_h=0$. This gives a type of basis selection without uncertainty. A small ν such as $10^{-6}$ gives a proper posterior and still allows $\beta_h$ concentrated at zero for unnecessary bases if ν is small enough. The default ν = 1 (Cauchy) often performs well for estimating μ and prediction (p. 493).
- **Laplace (double exponential)** prior, related to the lasso. The posterior mode can have $\hat\beta_h=0$. It is the prior with the heaviest tails that still gives a computationally convenient unimodal posterior (assuming a log-concave likelihood). No posterior draw is exactly zero, and in many cases its tails are not heavy enough to avoid over-shrinking nonzero coefficients (p. 493).
- **Generalized double Pareto (gdP)**: resembles the double exponential near the origin but has arbitrarily heavy tails (p. 493):
$$\text{gdP}(\beta|\xi,\alpha)=\frac1{2\xi}\Big(1+\frac{|\beta|}{\alpha\xi}\Big)^{-(\alpha+1)},\quad\xi>0\text{ scale},\ \alpha>0\text{ shape}.$$
  A draw is obtained by $\beta\sim N(0,\sigma^2)$, $\sigma^2\sim\text{Expon}(\lambda^2/2)$, $\lambda\sim\text{Gamma}(\alpha,\eta)$, with $\xi=\eta/\alpha$. So it is a scale mixture of normals. A typical default is α = η = 1 (Cauchy-like tails) (pp. 493–494).
- **Regression prior and sampler** (p. 494):
$$p(\beta|\sigma)=\prod_{h=1}^H\frac{\alpha}{2\sigma\eta}\Big(1+\frac{|\beta_h|}{\sigma\eta}\Big)^{-(\alpha+1)},$$
  equivalent to $\beta_h\sim N(0,\sigma^2\tau_h)$, $\tau_h\sim\text{Expon}(\lambda_h^2/2)$, $\lambda_h\sim\text{Gamma}(\alpha,\eta)$. With $p(\sigma)\propto1/\sigma$, a block Gibbs sampler has conditionals:
  - $\beta|-\sim N\big((W^TW+T^{-1})^{-1}W^Ty,\ \sigma^2(W^TW+T^{-1})^{-1}\big)$
  - $\sigma^2|-\sim\text{Inv-gamma}\big((n+k)/2,\ (y-W\beta)^T(y-X\beta)/2+\beta^TT^{-1}\beta/2\big)$
  - $\lambda_h|-\sim\text{Gamma}(\alpha+1,\ |\beta_h|/\sigma+\eta)$
  - $\tau_h^{-1}|-\sim\text{Inv-Gaussian}(\mu=|\lambda_h\sigma/\beta_h|,\ \rho=\lambda_h^2)$

  with $W=(w_1,\dots,w_n)$ and $T=\text{Diag}(\tau_1,\dots,\tau_H)$. The author's experience is good convergence and mixing, perhaps largely due to the block update of β. With many candidate bases, many coefficients go near zero while important ones are barely shrunk. For nonorthogonal (redundant) bases, which coefficients are away from zero may vary across iterations (p. 494).

*Intuition note.* A shrinkage prior is a smooth version of "keep or drop". It pulls small, unneeded coefficients to near zero but lets big ones stay big. Writing it as a scale mixture of normals keeps the conditionals simple.

### 20.3 Non-normal models and regression surfaces
**Other error distributions** (p. 494). For outliers, use a scale mixture of normals:
$$y_i\sim N(\mu(x_i),\phi_i\sigma^2),\qquad\phi_i\sim\text{Inv-gamma}(\nu/2,\nu/2),$$
which gives $t_\nu$ residuals. For low ν, the t is heavier-tailed and automatically downweights outliers without discarding them. In the sampler, add a step for $\phi_i$ and replace σ² by $\phi_i\sigma^2$ elsewhere. A Metropolis-Hastings step can allow unknown ν, or ν can be fixed at an elicited value.

**Example: chloride, robustness to outliers** (pp. 494–495).
- One observation was contaminated by adding a normal variable with 10 times the estimated residual standard deviation ($y_{47}=32.4$). With Gaussian residuals, the posterior mean of σ went from 0.27 to 0.61 and the curve intervals were wider, but the curve estimate did not change appreciably.
- With 100 times the standard deviation ($y_{40}=46.3$ as printed), results were poor: $\hat\sigma=22.4$ and the curve was pulled toward zero and away from the data.
- With t residuals and ν fixed at 4, results were close to the Gaussian analysis of uncontaminated data. The curve was only slightly pulled up and intervals only slightly wider.

**Exponential-family outcomes** (p. 495). Use the same framework with $\eta_i=w_i\beta$ as the linear predictor of a GLM (Chapter 16). Marginal likelihoods are generally not analytic, so Laplace approximations are common. For categorical responses in probit models, data augmentation with a latent Gaussian response gives closed-form augmented-data marginal likelihoods. It adds an MCMC step sampling the latent Gaussians from their full conditionals.

**Multivariate regression surfaces** (pp. 495–496). Multiple predictors bring the **curse of dimensionality** in two ways:
1. Methods that work for one or a few predictors may not scale. The number of basis functions needed for an unconstrained surface may grow rapidly and become prohibitive.
2. Even ignoring computation, it may be necessary to have enormous data to estimate a nonparametric surface reliably without parametric assumptions, substantial prior information or some restrictions. As p grows for fixed n, observations are sparse across $\mathcal X\subset\Re^p$, and some subregions have few.

So the prior for μ is crucial for interpolating across sparse regions. A common choice is **additivity**:
$$\mu(x)=\mu_0+\sum_{j=1}^p\beta_j(x_j),\qquad\beta_j(x_j)=\sum_{h=1}^{H_j}\theta_{jh}b_{jh}(x_j)\tag{20.5}$$
Here $\beta_j(\cdot)$ is an unknown coefficient function for predictor $j$, built from a prespecified basis $b_j$ (e.g. B-splines). Variable selection or shrinkage priors apply as in the p = 1 case. MCMC permits a divide-and-conquer approach: update predictor $j$'s unknowns using a modified response $y_i^*$ that subtracts the intercept and the other predictors' contributions (pp. 495–496).

**Shape constraints** (p. 496). Additive models can reduce the curse of dimensionality, and prior information improves efficiency further. If the response mean is believed nondecreasing in a predictor, use piecewise linear or monotone splines $b_j$ and constrain the coefficients to be nonnegative. A prior mixing a point mass at zero with a truncated normal on the $\theta_{jh}$ encourages sparsity and gives nondecreasing $\beta_j$ that can be flat across regions. Flat regions reduce bias from overestimating the slope and allow inference on regions where the predictor has no impact. Because the Bayesian approach gives uncertainty about flat regions, one can estimate the posterior of a threshold: the first predictor level at which the response mean increases. Unimodality and convexity can also be imposed through the prior.

**Example: DDE and preterm birth, with a nondecreasing curve** (pp. 496–497).
- Data come from the U.S. Collaborative Perinatal Project: 2380 pregnancies, 361 preterm births. Serum DDE (a metabolite of DDT) was measured in mg/L. Confounders: cholesterol, triglycerides, age, BMI, smoking.
- Aim: impose a nondecreasing dose–response to gain efficiency. Without the constraint one "relies too much on the data" and may get artefactual bumps. A strictly increasing curve is not imposed, since there may be no effect at low doses or even across the whole observed range (p. 496).
- Semiparametric probit additive model, with $\Phi$ the standard normal CDF:
$$\Pr(y_i=1|\theta,x_i,z_i)=\Phi\Big(\alpha_0+\sum_{l=1}^5z_{il}\alpha_l+f(x_i)\Big)=\Phi\big(z_i\alpha+f(x_i)\big)$$
  Here $y_i$ is the preterm indicator, $x_i$ the DDE level and $z_i=(1,z_{i2},\dots,z_{i5})$. Priors for the α are independent diffuse N(0, 10²). The function $f$ is piecewise linear with a dense set of knots, and $\beta_j$ is the slope within interval $j$. A prior disallowing negative $\beta_j$ enforces the constraint (p. 496).
- **Latent threshold prior** (p. 497): latent slopes follow a first-order normal random walk, $\beta_j^*\sim N(\beta^*_{j-1},\sigma_\beta^2)$, with an inverse-gamma hyperprior on $\sigma_\beta^2$. The link is $\beta_j=1_{\beta_j^*\ge\delta}\,\beta_j^*$ with δ a small positive threshold with a gamma hyperprior. Larger δ makes $\beta_j=0$ more likely and gives more flat regions.
- Results (Figure 20.4, p. 497): estimated posterior probability of the global null ($f\equiv0$ over the observed DDE range) was < 0.01. The same model fitted classically without constraints gave p = 0.23. The posterior mean of the first dose with an increasing slope is $\hat\tau=7$, 95% interval [3, 21]. The author notes such thresholds are approximations, since the true function is presumably continuous and always increasing to some extent.

**Beyond additivity** (pp. 497–498). Additivity fails when predictors interact. A **tensor product** specification is
$$\mu(x)=\sum_{h_1=1}^H\cdots\sum_{h_p=1}^H\theta_{h_1\cdots h_p}\prod_{j=1}^pb_{jh_j}(x_j),$$
with $H_j=H$ and θ a p-way array of unknown coefficients. It can be large, but selection or shrinkage priors favour many elements near zero, collapsing to a lower-dimensional representation (dropping predictors or interactions). Given the basis, the model is linear, so Gibbs sampling is efficient (p. 498).

### 20.4 Bibliographic note (p. 498)
The chapter points to Bishop (2006) as a review of basis function models. Reversible-jump basis selection is cited to Biller (2000) and DiMatteo et al. (2001); Bayesian variable selection to Smith and Kohn (1996); median probability models to Barbieri and Berger (2004); Laplace-prior inference to Park and Casella (2008); generalized double Pareto to Armagan et al.; monotone regression to Neelon and Dunson (2004) and others. The chloride example is from Bates and Watts (1988) and the DDE study from Neelon and Dunson (2004).

### 20.5 Exercises (pp. 498–499)
Six exercises: a basis function model for survey proportions by age (normal approximation, then binomial, then three predictors); a binomial basis model for golf putting data with posterior predictive checks; hierarchical modelling and splines for 2012 poll data; and prior properties under a generalized double Pareto prior on B-spline coefficients.

## Toy example (ours, not from the text)
Take two "hat" basis functions on [0, 1] (our own choice, local like the chapter's bases): $b_1(x)=1-x$, $b_2(x)=x$. Data: $(x,y)=(0,1),(0.5,2),(1,4)$. Then
$$W=\begin{pmatrix}1&0\\0.5&0.5\\0&1\end{pmatrix}.$$

- $W^TW=\begin{pmatrix}1+0.25&0.25\\0.25&0.25+1\end{pmatrix}=\begin{pmatrix}1.25&0.25\\0.25&1.25\end{pmatrix}$.
- $W^Ty=(1\cdot1+0.5\cdot2+0,\ 0+0.5\cdot2+1\cdot4)=(2,5)$.
- **No prior (λ = 0):** the determinant of $W^TW$ is $1.5625-0.0625=1.5$. Then $\hat\beta=\frac1{1.5}\big(1.25\cdot2-0.25\cdot5,\ -0.25\cdot2+1.25\cdot5\big)=\frac1{1.5}(1.25,5.75)=(0.833,3.833)$.
- **Prior centred on the line α = 1, ψ = 2:** $\beta_0=(\mu_0(0),\mu_0(1))=(1,3)$. Take λ = 1 and use the p. 490 form $(W^TW+\lambda I)^{-1}(W^Ty+\lambda\beta_0)$.
  - $W^TW+I=\begin{pmatrix}2.25&0.25\\0.25&2.25\end{pmatrix}$, with determinant $5.0625-0.0625=5$.
  - $W^Ty+\beta_0=(3,8)$.
  - $\hat\beta=\frac15\big(2.25\cdot3-0.25\cdot8,\ -0.25\cdot3+2.25\cdot8\big)=\frac15(4.75,17.25)=(0.95,3.45)$.
- Check: $0.95$ lies between $0.833$ (data only) and $1$ (prior), and $3.45$ lies between $3$ and $3.833$. So the posterior mean is pulled toward the prior curve. The fitted curve at $x=0.5$ is $0.5\cdot0.95+0.5\cdot3.45=2.2$.

## Concepts
- [[basis-function-expansion]] (new) — μ(x) written as a weighted sum Σβ_h b_h(x) of prespecified functions; linear in β given the basis (p. 487)
- [[gaussian-radial-basis]] (new) — local bump $\exp(-|x-x_h|^2/l^2)$ with common width $l$ (p. 487)
- [[b-spline]] (new) — piecewise cubic bump with compact support defined by knots, giving a sparse design matrix (p. 488)
- [[conjugate-prior]] — normal-inverse-χ² (or normal-gamma) prior for (β, σ²) keeps the posterior in the same family, given the basis (p. 488)
- [[partial-pooling-shrinkage]] — here, the posterior mean curve is shrunk toward a prior-centred parametric curve, and coefficients are shrunk toward zero (pp. 490, 493–494)
- [[variable-selection-mixture-prior]] (new) — spike-and-slab prior (20.3): β_h = 0 with probability π_h, else normal (p. 491)
- [[marginal-likelihood]] — p(y|X,γ), analytic for each basis subset; drives posterior model probabilities (20.4) (p. 491)
- [[gibbs-sampling]] — used to update inclusion indicators γ_h and, in the gdP model, block updates of β (pp. 492, 494)
- [[median-probability-model]] (new) — the model including bases with marginal inclusion probability > 0.5; best single-model approximation to averaging for orthogonal bases (p. 492)
- [[scale-mixture-of-normals]] (new) — β_h ~ N(0, σ_h²), σ_h² ~ G; gives t, Laplace and gdP priors (p. 493)
- [[generalized-double-pareto-prior]] (new) — Laplace-like near zero, arbitrarily heavy tails; scale-mixture form allows simple Gibbs sampling (p. 493)
- [[curse-of-dimensionality]] (new) — basis count and data needs grow rapidly with the number of predictors (p. 495)
- [[additive-model]] (new) — μ(x) = μ_0 + Σ β_j(x_j), each β_j a basis expansion (20.5) (p. 495)
- [[shape-constrained-regression]] (new) — priors that enforce monotonicity, etc. (nonnegative coefficients on monotone splines) (p. 496)
- [[latent-threshold-prior]] (new) — random-walk latent slopes thresholded at δ so slopes can be exactly zero (p. 497)
- [[tensor-product-regression]] (new) — products of univariate bases with a p-way coefficient array; shrinkage collapses it (pp. 497–498)

## Canonical instances
- [[chloride-concentration]] — 54 points, 21 B-spline coefficients; shrinkage toward a line, variable selection, robustness to outliers (pp. 489–495)
- [[ddt-dde-preterm-birth]] — probit additive model with a nondecreasing f via a latent threshold prior (pp. 496–497)
- [[naes-2004-gay-attitudes]] — survey proportions by age for exercises (pp. 498–499)

## Bridges (candidates)
- [structural-analogy] Shrinkage of basis coefficients ↔ Bayesian partial pooling: coefficients are pulled toward a common centre by a prior scale learned from data.
- [same-math] Posterior mean (WᵀW + λI)⁻¹(Wᵀy + λμ̂₀) ↔ ridge regression with a nonzero penalty centre: same estimating equation.
- [structural-analogy] Spike-and-slab inclusion indicators ↔ Bayesian model averaging over regressors: each γ indexes a model.
- [metaphor] Curse of dimensionality for surfaces ↔ sparse data in cells of a high-dimensional contingency table.

## Questions this raises
- How does the choice of l, δ or the number of knots interact with the shrinkage prior? Is a dense knot set always safe?
- How does inference on a threshold (like τ = 7 for DDE) depend on the latent-threshold prior, given the author's remark that the true curve is presumably continuous?
- When do variable selection and continuous shrinkage priors give different posterior curves in the same dataset?
- Could the Gaussian-process alternative mentioned on p. 490 avoid choosing a basis?

## Exercises worth doing
- Ex. 1 (p. 498) — build a full Bayesian basis model (prior, unnormalized posterior, log-density in R, fit, plot) for survey proportions by age — difficulty: medium
- Ex. 2 (p. 498) — repeat with a binomial likelihood and compare with the normal approximation — difficulty: medium
- Ex. 4 (p. 499) — binomial basis model for golf putting, with posterior predictive checks — difficulty: medium
- Ex. 5 (p. 499) — splines combined with hierarchical pollster effects for time-series smoothing — difficulty: hard
- Ex. 6 (p. 499) — prior mean, variance and rescaling for a spline model with gdP shrinkage — difficulty: hard

## Reading notes
- Printed pages 487–500; printed = pdf − 10. Page 500 (pdf 510) is blank apart from the running header.
- In (20.4), k is not defined on the page; it presumably means H, the total number of basis functions.
- $V_\gamma$ is printed as $\text{diag}(\kappa_h:\gamma_h=1)$ although (20.3) gives variance $\kappa_h^{-1}\sigma^2$. I copied it as printed.
- In the gdP Gibbs sampler, the σ² conditional shows $(y-W\beta)^T(y-X\beta)$ (X looks like a typo for W) and uses k without defining it (p. 494).
- The outlier example names the contaminated point $y_{47}$ in the first case and $y_{40}$ in the second (pp. 494–495). The second looks inconsistent and may be a misprint.
- The (20.5) coefficients appear as θ_jh in the page image; the text layer shows garbled symbols. In the posterior-mean formula, $\hat\mu_0(x)$ stands where a coefficient vector is needed. I copied it as printed.
- The text calls the cubic B-spline "only three times differentiable" (p. 488). I reported it as stated.
