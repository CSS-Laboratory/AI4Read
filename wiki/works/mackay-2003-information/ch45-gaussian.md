---
id: mackay-2003-information/ch45-gaussian
work: mackay-2003-information
unit: "45 Gaussian Processes"
pages: 534-548
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
# Gaussian Processes

## L0 — One line
A Gaussian process puts a prior directly on functions, so that any finite set of function values is jointly Gaussian and regression becomes matrix algebra with a covariance function.

## L1 — The gist (≤ 120 words)
A Bayesian neural network defines a prior over functions. Chapter 45 asks whether we can drop the parameters and place that prior directly on functions. The answer is the Gaussian process: any finite set of function values is jointly Gaussian, fixed by a mean and a covariance function. Prediction then needs only the inverse of the N×N data covariance matrix, at cost of order N³. Hyperparameters (covariance and noise settings such as lengthscales) are set by maximizing the evidence (probability of the data) times a prior, or by Monte Carlo. Classification works by giving a latent variable a Gaussian process prior. MacKay concludes that Gaussian processes are simple smoothers that solve many real-world problems but not feature discovery.

**Prerequisites:** multivariate Gaussians and covariance matrices; Bayes' theorem; matrix inverse and determinant; basic Fourier series; marginalization.

## L2 — Key ideas
- Prediction depends only on the prior over functions and the noise model. The parameterization of $y(x;w)$ is irrelevant for prediction (p. 535, p. 539).
- Spline smoothing can be read as Bayesian MAP (most probable function) estimation under a Gaussian-process prior. So, in terms of the prior over functions, there is no fundamental difference between "nonparametric" splines and parametric approaches (pp. 538–539).
- With fixed basis functions and a Gaussian prior on the weights, the function values at any points are Gaussian with covariance $\sigma_w^2\mathbf{RR}^T$. That is the defining property of a Gaussian process (p. 540). In the infinite-basis limit (uniformly spaced radial basis functions, prior variance scaled with their density), they give a Gaussian covariance function (p. 541).
- The predictive mean $\hat t_{N+1}=\mathbf k^T\mathbf C_N^{-1}\mathbf t_N$ and variance $\kappa-\mathbf k^T\mathbf C_N^{-1}\mathbf k$ need only $\mathbf C_N^{-1}$. The cost is order $N^3$, independent of the number of basis functions $H$ (p. 543).
- The covariance function encodes smoothness, lengthscales, periodicity, linear trends and irrelevant inputs. Its only constraint is that it must give non-negative-definite matrices ($\mathbf v^T\mathbf C\mathbf v\ge0$ for every vector $\mathbf v$) (pp. 543–545).
- Hyperparameters are set to their most probable values (evidence, i.e. the probability of the data given $\boldsymbol\theta$, times a prior), using the evidence gradient (45.55), or by Monte Carlo integration over $\boldsymbol\theta$ (averaging over random samples). The evidence can be multimodal, and each gradient needs $\mathbf C_N^{-1}$ (pp. 545–546).
- Classification puts a Gaussian process prior on a hidden (latent) $a(x)$ passed through a logistic function $1/(1+e^{-a})$. The posterior is no longer Gaussian, so approximations are needed (p. 547).
- MacKay's verdict: Gaussian processes are simple smoothing devices. They do not appear to sacrifice performance for that simplicity, many real-world problems are well solved by smoothing, and direct inversion becomes prohibitive above about 1000 points (pp. 547–548).

## L3 — Walkthrough

### About the chapter and introduction (pp. 534–536)
- A neural network model defines a prior over nonlinear functions. Learning is inference of the posterior over the function (p. 534).
- Neal (1996) showed that for large but otherwise standard networks the prior falls in the class of Gaussian processes. The network hyperparameters set the characteristic lengthscales (p. 534).
- This motivates discarding parameterized networks. Parameter optimization is replaced by simple matrix operations on the covariance matrix (p. 534).
- The notation is data $\{x^{(n)},t_n\}_{n=1}^N$, inputs $\mathbf X_N$, targets $\mathbf t_N$. The posterior over the function is (p. 535):

$$P(y(x)\mid \mathbf t_N,\mathbf X_N)=\frac{P(\mathbf t_N\mid y(x),\mathbf X_N)\,P(y(x))}{P(\mathbf t_N\mid \mathbf X_N)}\tag{45.1}$$

- The first factor is often a separable Gaussian in regression. The prior $P(y(x))$ is implicit in the choice of parametric model and regularizers (p. 535).
- For predicting future $t$, only the prior and the noise model matter. The parameterization is irrelevant (p. 535).
- A Gaussian process generalizes a Gaussian over a finite vector space to an infinite-dimensional function space. It is specified by a mean function (often zero) and a covariance function $C(x,x')$. The data function is assumed to be a single sample (p. 535).
- Brownian, Langevin and Wiener processes, Kalman filters and kriging are Gaussian-process models (pp. 535–536).
- **MacKay's anticipated reservations:** (i) something as simple as a Gaussian may seem unable to reproduce neural-network interpolation. He replies that many popular nonlinear interpolation methods are equivalent to particular Gaussian processes. (ii) Infinite-dimensional priors may seem to cost infinite computation. He replies that by working with the joint distribution of observed data and predicted quantities, cost scales polynomially in $N$ (p. 536).
- "Interpolation" covers both regression (a curve through noisy data) and exact interpolation (p. 536).

### 45.1 Standard methods for nonlinear regression (pp. 536–539)
**Problem.** The inputs $\mathbf x$ have dimension $I$. Targets are real (regression) or categorical (classification). The chapter first treats regression (p. 536).

**Parametric approaches.**
- *Fixed basis functions* (Example 45.2): $y(\mathbf x;\mathbf w)=\sum_{h=1}^H w_h\phi_h(\mathbf x)$ (45.2), for example with radial basis functions $\phi_h(\mathbf x)=\exp\!\left[-\frac{(\mathbf x-\mathbf c_h)^2}{2r^2}\right]$ (45.3). This is linear in $\mathbf w$. In network terms it has fixed input-to-hidden connections (p. 536).
- *Adaptive basis functions* (Example 45.3): a two-layer network, nonlinear in $\mathbf w$ (p. 537):
$$y(\mathbf x;\mathbf w)=\sum_{h=1}^H w^{(2)}_h\tanh\!\Big(\sum_{i=1}^I w^{(1)}_{hi}x_i+w^{(1)}_{h0}\Big)+w^{(2)}_0\tag{45.4}$$
- Posterior of the parameters (p. 537):
$$P(\mathbf w\mid\mathbf t_N,\mathbf X_N)=\frac{P(\mathbf t_N\mid\mathbf w,\mathbf X_N)P(\mathbf w)}{P(\mathbf t_N\mid\mathbf X_N)}\tag{45.5}$$
Likelihood and prior are often separable Gaussians. If $y$ depends nonlinearly on $\mathbf w$, the posterior is in general not Gaussian (p. 537).
- *Laplace method*: minimize $M(\mathbf w)=-\ln[P(\mathbf t_N\mid\mathbf w,\mathbf X_N)P(\mathbf w)]$ (45.6). Then use the curvature $\partial^2M/\partial w_i\partial w_j$ for error bars. The alternative is MCMC samples (p. 537).
- Predictions marginalize over $\mathbf w$ (p. 537):
$$P(t_{N+1}\mid\mathbf t_N,\mathbf X_{N+1})=\int \mathrm d^H\mathbf w\,P(t_{N+1}\mid\mathbf w,\mathbf x^{(N+1)})P(\mathbf w\mid\mathbf t_N,\mathbf X_N)\tag{45.7}$$
With $R$ posterior samples $\mathbf w^{(r)}$:
$$P(t_{N+1}\mid\mathbf t_N,\mathbf X_{N+1})\simeq\frac1R\sum_{r=1}^R P(t_{N+1}\mid\mathbf w^{(r)},\mathbf x^{(N+1)})\tag{45.8}$$

**Nonparametric approach: splines** (p. 538).
- The spline estimator $\hat y$ minimizes ($y^{(p)}$ is the $p$th derivative):
$$M(y(x))=\tfrac12\beta\sum_{n=1}^N\big(y(x^{(n)})-t_n\big)^2+\tfrac12\alpha\int \mathrm dx\,[y^{(p)}(x)]^2\tag{45.9}$$
For $p=2$, $\hat y$ is a cubic spline, a piecewise cubic with knots at the data points (p. 538).
- Bayesian reading, with independent Gaussian noise (p. 538):
$$\ln P(y(x)\mid\alpha)=-\tfrac12\alpha\int \mathrm dx\,[y^{(p)}(x)]^2+\text{const}\tag{45.10}$$
$$\ln P(\mathbf t_N\mid y(x),\beta)=-\tfrac12\beta\sum_{n=1}^N(y(x^{(n)})-t_n)^2+\text{const}\tag{45.11}$$
The constants depend on $\alpha$ and $\beta$ respectively. Strictly, (45.10) is improper, because adding a polynomial of degree $p-1$ is unconstrained. Adding $p-1$ terms fixes this (p. 538).
- Then $M(y)$ equals minus the log posterior up to a constant, so splines give a Bayesian MAP estimate. The Bayesian view also gives error bars, posterior samples and an automatic way to infer $\alpha,\beta$ (p. 538).

**Splines priors are Gaussian processes.** Loosely, a Gaussian process is a distribution on functions of the form (p. 538)
$$P(y(x)\mid\mu(x),A)=\frac1Z\exp\!\Big[-\tfrac12(y-\mu)^TA(y-\mu)\Big]\tag{45.12}$$
Here $A$ is a linear operator and inner products are, for example, $\int \mathrm dx\,y(x)z(x)$. Let $D$ be the derivative operator. Then (p. 539)
$$\ln P(y(x)\mid\alpha)=-\tfrac12\alpha\int \mathrm dx\,[D^py(x)]^2+\text{const}=-\tfrac12 y^TAy+\text{const}\tag{45.13}$$
This has the form (45.12) with $\mu=0$ and $A\equiv[D^p]^TD^p$. For a proper prior, $A$ must be positive definite: $y^TAy>0$ for all $y\neq0$ (p. 539).

**Splines as parametric models** (p. 539). Rescale $x$ so that $(0,2\pi)$ is much wider than the range of interest, and use the Fourier basis:
$$y(x)=\sum_{h=0}^\infty w_{h(\cos)}\cos(hx)+\sum_{h=1}^\infty w_{h(\sin)}\sin(hx)\tag{45.14}$$
$$E_W(\mathbf w)=\sum_{h=0}^\infty\tfrac12h^{p/2}w_{h(\cos)}^2+\sum_{h=1}^\infty\tfrac12h^{p/2}w_{h(\sin)}^2\tag{45.15}$$
$$P(\mathbf w\mid\alpha)=\frac1{Z_W(\alpha)}\exp(-\alpha E_W)\tag{45.16}$$
For $p=2$ MacKay says this is the cubic-spline regularizer $\int y^{(2)}(x)^2\mathrm dx$; for $p=1$ it is $\int y^{(1)}(x)^2\mathrm dx$. An extra regularizer on $w_{0(\cos)}$ makes the prior proper. Hence there is no fundamental difference in the prior between "nonparametric" splines and parametric approaches (p. 539).

**Representation is irrelevant for prediction.** The two quantities of interest are the predictive distribution (45.7) and the evidence $P(\mathbf t_N\mid\mathbf X_N)$. Neither refers to the representation of $y(x)$ (p. 539). MacKay announces that for standard models with fixed basis functions and Gaussian priors on the parameters, $P(\mathbf t_N\mid\mathbf X_N)$ is a zero-mean multivariate Gaussian. The conditional $P(t_{N+1}\mid\mathbf t_N,\mathbf X_{N+1})$ is then Gaussian, with mean linear in $\mathbf t_N$ (p. 539).

*Intuition note.* Two models with different parameters but the same prior over functions and the same noise model make identical predictions. So the useful object is the prior over functions, and the parameters are only a way to write it down.

### 45.2 From parametric models to Gaussian processes (pp. 540–542)
**Linear models.** Define the $N\times H$ matrix $\mathbf R$ and the vector $\mathbf y$ of function values (p. 540):
$$R_{nh}\equiv\phi_h(\mathbf x^{(n)})\tag{45.17}$$
$$y_n\equiv\sum_hR_{nh}w_h\tag{45.18}$$
Prior $P(\mathbf w)=\text{Normal}(\mathbf w;\mathbf 0,\sigma_w^2\mathbf I)$ (45.19). Then $\mathbf y$ is linear in $\mathbf w$, so it is Gaussian with mean zero and covariance (shape $N\times N$):
$$\mathbf Q=\langle\mathbf{yy}^T\rangle=\langle\mathbf{Rww}^T\mathbf R^T\rangle=\mathbf R\langle\mathbf{ww}^T\rangle\mathbf R^T\tag{45.20}$$
$$=\sigma_w^2\mathbf{RR}^T\tag{45.21}$$
$$P(\mathbf y)=\text{Normal}(\mathbf y;\mathbf 0,\mathbf Q)=\text{Normal}(\mathbf y;\mathbf 0,\sigma_w^2\mathbf{RR}^T)\tag{45.22}$$
This holds for any selected points $\mathbf X_N$. **Definition (p. 540):** the distribution of $y(x)$ is a Gaussian process if, for any finite selection of points $x^{(1)},\dots,x^{(N)}$, the density $P(y(x^{(1)}),\dots,y(x^{(N)}))$ is Gaussian.
- If $H<N$, $\mathbf Q$ lacks full rank. The distribution of $\mathbf y$ is then a flat elliptical pancake confined to an $H$-dimensional subspace of $\mathbb R^N$ (p. 540).
- With additive Gaussian noise of variance $\sigma_\nu^2$ on each target (p. 540):
$$P(\mathbf t)=\text{Normal}(\mathbf t;\mathbf 0,\mathbf Q+\sigma_\nu^2\mathbf I)\tag{45.23}$$
$$\mathbf C=\mathbf Q+\sigma_\nu^2\mathbf I=\sigma_w^2\mathbf{RR}^T+\sigma_\nu^2\mathbf I\tag{45.24}$$
$\mathbf C$ always has full rank, because $\sigma_\nu^2\mathbf I$ does. Entries (pp. 540–541):
$$Q_{nn'}=\sigma_w^2\sum_h\phi_h(\mathbf x^{(n)})\phi_h(\mathbf x^{(n')})\tag{45.25}$$
$$C_{nn'}=\sigma_w^2\sum_h\phi_h(\mathbf x^{(n)})\phi_h(\mathbf x^{(n')})+\delta_{nn'}\sigma_\nu^2\tag{45.26}$$

**Example 45.4** (p. 541). Take one dimension, with radial basis functions centred at $x=h$, uniformly spaced, and let $H\to\infty$. To keep the covariance finite, let $\sigma_w^2$ scale as $S/(\Delta H)$. Here $\Delta H$ is the number of basis functions per unit length and $S$ is a constant. Then the sum becomes an integral:
$$Q_{nn'}=S\int_{h_{\min}}^{h_{\max}}\mathrm dh\,\phi_h(x^{(n)})\phi_h(x^{(n')})\tag{45.27}$$
$$=S\int_{h_{\min}}^{h_{\max}}\mathrm dh\,\exp\!\Big[-\tfrac{(x^{(n)}-h)^2}{2r^2}\Big]\exp\!\Big[-\tfrac{(x^{(n')}-h)^2}{2r^2}\Big]\tag{45.28}$$
With limits $\pm\infty$ the integral is solvable:
$$Q_{nn'}=\sqrt{\pi r^2}\,S\exp\!\Big[-\tfrac{(x^{(n')}-x^{(n)})^2}{4r^2}\Big]\tag{45.29}$$
The prior is thus summarized by a covariance function, with the constant renamed $\theta_1$:
$$C(x^{(n)},x^{(n')})\equiv\theta_1\exp\!\Big[-\tfrac{(x^{(n')}-x^{(n)})^2}{4r^2}\Big]\tag{45.30}$$

**Generalization.** For any valid covariance function $C(\mathbf x,\mathbf x')$ (p. 541):
$$Q_{nn'}=C(\mathbf x^{(n)},\mathbf x^{(n')})\tag{45.31}$$
$$C_{nn'}=C(\mathbf x^{(n)},\mathbf x^{(n')})+\sigma_\nu^2\delta_{nn'}\tag{45.32}$$
$$P(\mathbf t)=\text{Normal}(\mathbf t;\mathbf 0,\mathbf C)=\frac1Ze^{-\frac12\mathbf t^T\mathbf C^{-1}\mathbf t}\tag{45.33}$$

*Intuition note.* We can stop choosing basis functions and just say how strongly the function values at two inputs co-vary. A Gaussian bump basis with infinitely many bumps turns into a covariance that falls off smoothly with distance.

**Figure 45.1** (p. 542) shows samples from four priors:
- (a) $2\exp[-(x-x')^2/(2(1.5)^2)]$.
- (b) the same with lengthscale $0.35$, which gives more rapidly fluctuating functions.
- (c) a periodic covariance, $2\exp[-\sin^2(\pi(x-x')/3.0)/(2(0.5)^2)]$.
- (d) the form of (a) plus $xx'$, which gives linear trends.

**Multilayer networks.** Neal (1996) showed that a network with one hidden layer (45.4) converges to a Gaussian process as the number of hidden neurons tends to infinity, if standard weight-decay priors are assumed. The covariance function depends on the weight priors and the hidden-unit activation functions (p. 542).

### 45.3 Using a given Gaussian process model in regression (pp. 542–543)
The joint density $P(t_{N+1},\mathbf t_N)$ is Gaussian, so the conditional is Gaussian (p. 542):
$$P(t_{N+1}\mid\mathbf t_N)=\frac{P(t_{N+1},\mathbf t_N)}{P(\mathbf t_N)}\tag{45.34}$$
Partition the $(N+1)\times(N+1)$ covariance matrix, with $\mathbf k$ of shape $N\times1$ and $\kappa$ a scalar (p. 543):
$$\mathbf C_{N+1}\equiv\begin{bmatrix}\mathbf C_N&\mathbf k\\ \mathbf k^T&\kappa\end{bmatrix}\tag{45.35}$$
$$P(t_{N+1}\mid\mathbf t_N)\propto\exp\!\Big(-\tfrac12[\mathbf t_N\;t_{N+1}]\,\mathbf C_{N+1}^{-1}\begin{bmatrix}\mathbf t_N\\t_{N+1}\end{bmatrix}\Big)\tag{45.36}$$
Brute-force inversion of $\mathbf C_{N+1}$ would work. A better route, useful when predicting at several new points, uses the partitioned inverse (Barnett, 1979), with scalar $m$ and vector $\mathbf m$:
$$\mathbf C_{N+1}^{-1}=\begin{bmatrix}\mathbf M&\mathbf m\\ \mathbf m^T&m\end{bmatrix}\tag{45.37}$$
$$m=(\kappa-\mathbf k^T\mathbf C_N^{-1}\mathbf k)^{-1}\tag{45.38}$$
$$\mathbf m=-m\,\mathbf C_N^{-1}\mathbf k\tag{45.39}$$
$$\mathbf M=\mathbf C_N^{-1}+\tfrac1m\mathbf m\mathbf m^T\tag{45.40}$$
Substituting into (45.36) gives (p. 543)
$$P(t_{N+1}\mid\mathbf t_N)=\frac1Z\exp\!\Big[-\frac{(t_{N+1}-\hat t_{N+1})^2}{2\sigma^2_{\hat t_{N+1}}}\Big]\tag{45.41}$$
$$\hat t_{N+1}=\mathbf k^T\mathbf C_N^{-1}\mathbf t_N\tag{45.42}$$
$$\sigma^2_{\hat t_{N+1}}=\kappa-\mathbf k^T\mathbf C_N^{-1}\mathbf k\tag{45.43}$$
$\hat t_{N+1}$ is the predictive mean and $\sigma_{\hat t_{N+1}}$ gives the error bars. Only $\mathbf C_N$ needs inverting. A model with $H\gg N$ basis functions can therefore be run at cost of order $N^3$, independent of $H$ (p. 543).

*Intuition note.* The prediction is a weighted sum of the observed targets. The weights $\mathbf k^T\mathbf C_N^{-1}$ come from how strongly the new point co-varies with each data point. The variance starts at the prior variance $\kappa$ and shrinks by an amount that depends on how much the data covary with the new point.

### 45.4 Examples of covariance functions (pp. 543–545)
- The only constraint is that $C$ must give a non-negative-definite matrix for any set of points (p. 543). With parameters $\boldsymbol\theta$ and a noise model $\mathcal N$ (p. 544):
$$C_{mn}=C(\mathbf x^{(m)},\mathbf x^{(n)};\boldsymbol\theta)+\delta_{mn}\mathcal N(\mathbf x^{(n)};\boldsymbol\theta)\tag{45.44}$$
$$\mathcal N(\mathbf x;\boldsymbol\theta)=\begin{cases}\theta_3&\text{input-independent noise}\\ \exp\!\big(\sum_{j=1}^J\beta_j\phi_j(\mathbf x)\big)&\text{input-dependent noise}\end{cases}\tag{45.45}$$
- The continuity properties of $C$ determine those of typical prior samples (p. 544).

**Stationary covariance functions** (p. 544).
- *Definition:* translation invariant, $C(\mathbf x,\mathbf x';\boldsymbol\theta)=D(\mathbf x-\mathbf x';\boldsymbol\theta)$ (45.46). $D$ is also called the autocovariance function. If additionally $C$ depends only on the magnitude of the distance, it is *homogeneous*.
- The Fourier transform of $D$ is the *power spectrum*, necessarily positive. To build a valid stationary covariance, invent a positive function of frequency and take its inverse Fourier transform.
- Example 45.5: a Gaussian power spectrum gives a Gaussian autocovariance, rederiving (45.30).
- A popular form, with $\boldsymbol\theta=(\theta_1,\theta_2,\{r_i\})$:
$$C(\mathbf x,\mathbf x';\boldsymbol\theta)=\theta_1\exp\!\Big[-\tfrac12\sum_{i=1}^I\frac{(x_i-x_i')^2}{r_i^2}\Big]+\theta_2\tag{45.47}$$
Here $r_i$ is the lengthscale in direction $i$. A very large $r_i$ means $y$ is essentially constant in that input, so the input is irrelevant (as in automatic relevance determination). $\theta_1$ sets the vertical scale. $\theta_2$ allows a constant offset (consider $\phi(\mathbf x)=1$ in (45.25)).
- Another: $C(x,x')=\exp(-|x-x'|^\nu)$, $0<\nu\le2$ (45.48). For $\nu=2$ it is a special case of (45.47). For $\nu\in(1,2)$, typical functions are smooth but not analytic. For $\nu\le1$ they are continuous but not smooth (p. 545).
- Periodic with known period $\lambda_i$ in direction $i$ (p. 545):
$$C(\mathbf x,\mathbf x';\boldsymbol\theta)=\theta_1\exp\!\Big[-\tfrac12\sum_i\Big(\frac{\sin\big(\frac\pi{\lambda_i}(x_i-x_i')\big)}{r_i}\Big)^2\Big]\tag{45.49}$$

**Nonstationary: linear trend** (p. 545). For the plane $y(\mathbf x)=\sum_iw_ix_i+c$, with zero-mean Gaussian $w_i$ (variance $\sigma_w^2$) and $c$ (variance $\sigma_c^2$):
$$C_{\text{lin}}(\mathbf x,\mathbf x';\{\sigma_w,\sigma_c\})=\sum_{i=1}^I\sigma_w^2x_ix_i'+\sigma_c^2\tag{45.50}$$

### 45.5 Adaptation of Gaussian process models (pp. 545–546)
- Learning the hyperparameters $\boldsymbol\theta$ is a complexity-control problem, solved nicely by the Bayesian Occam's razor. It is equivalent to inferring, for example, weight-decay hyperparameters (p. 546).
- Ideal prediction integrates over $\boldsymbol\theta$ (p. 546):
$$P(t_{N+1}\mid\mathbf x_{N+1},\mathcal D)=\int P(t_{N+1}\mid\mathbf x_{N+1},\boldsymbol\theta,\mathcal D)P(\boldsymbol\theta\mid\mathcal D)\,\mathrm d\boldsymbol\theta\tag{45.51}$$
This is usually intractable. Option 1: use the most probable values (45.52), $P(t_{N+1}\mid\mathbf x_{N+1},\mathcal D)\simeq P(t_{N+1}\mid\mathbf x_{N+1},\mathcal D,\boldsymbol\theta_{\rm MP})$. Option 2: integrate numerically by Monte Carlo. Either is most efficient if the gradient of the posterior of $\boldsymbol\theta$ is available.
- Gradient: $P(\boldsymbol\theta\mid\mathcal D)\propto P(\mathbf t_N\mid\mathbf X_N,\boldsymbol\theta)P(\boldsymbol\theta)$ (45.53). The log evidence for the hyperparameters is
$$\ln P(\mathbf t_N\mid\mathbf X_N,\boldsymbol\theta)=-\tfrac12\ln\det\mathbf C_N-\tfrac12\mathbf t_N^T\mathbf C_N^{-1}\mathbf t_N-\tfrac N2\ln2\pi\tag{45.54}$$
$$\frac{\partial}{\partial\theta}\ln P(\mathbf t_N\mid\mathbf X_N,\boldsymbol\theta)=-\tfrac12\text{Trace}\!\Big(\mathbf C_N^{-1}\frac{\partial\mathbf C_N}{\partial\theta}\Big)+\tfrac12\mathbf t_N^T\mathbf C_N^{-1}\frac{\partial\mathbf C_N}{\partial\theta}\mathbf C_N^{-1}\mathbf t_N\tag{45.55}$$
- **Two problems** (p. 546). (1) The evidence may be multimodal (Figure 45.2). Suitable priors and sensible optimization often eliminate poor optima. (2) The gradient needs $\mathbf C_N^{-1}$. Exact inversion (Cholesky, LU, Gauss–Jordan) costs order $N^3$. One approach based on Skilling's ideas approximates $\mathbf C^{-1}\mathbf t$ and $\text{Trace}\,\mathbf C^{-1}$ iteratively at cost $O(N^2)$ (Gibbs and MacKay).
- **Figure 45.2** (p. 545): five data points are modelled with (45.47), with $\theta_3$ controlling noise. Two local likelihood maxima are shown: (a) $r_1=0.95$, $\theta_3=0.0$; (b) $r_1=3.5$, $\theta_3=3.0$.

*Intuition note.* In our reading (the page does not spell this out), the evidence trades data fit (the $\mathbf t^T\mathbf C^{-1}\mathbf t$ term) against model complexity (the $\ln\det\mathbf C$ term). Because the evidence can have several peaks, the optimizer can land on a different story about the data, such as wiggly and almost noise-free versus smooth and noisy.

### 45.6 Classification (p. 547)
- For binary targets define $a_n\equiv a(x^{(n)})$ with
$$P(t_n=1\mid a_n)=\frac1{1+e^{-a_n}}\tag{45.56}$$
Large positive $a$ gives probabilities near one, and large negative $a$ gives probabilities near zero. To say that $P(t=1)$ varies smoothly with $x$, give $a(x)$ a Gaussian process prior.
- Inference is harder than in regression because (45.56) is not Gaussian in $a_n$. The posterior over $a$ is not Gaussian, and $P(\mathbf t_N\mid\mathbf X_N)$ has no analytic form.
- Implementations: Laplace approximations (Barber and Williams, 1997); Monte Carlo (Neal, 1997b); a variational classifier (Gibbs and MacKay, 2000). The variational one uses Jaakkola–Jordan methods. It gets tractable upper and lower bounds on the unnormalized posterior $P(\mathbf t_N\mid\mathbf a)P(\mathbf a)$, with variational parameters adjusted for the tightest fit. Normalized versions of the bounds give approximate predictive distributions. Multi-class problems use Monte Carlo or variational methods.

### 45.7 Discussion (pp. 547–548)
- Gaussian processes are moderately simple to use. Few model parameters need hand-tuning, generally only priors on hyperparameters. MacKay writes that "We do not appear to sacrifice any performance for this simplicity." (p. 547). Desired properties, such as automatic relevance determination, are easy to build in (p. 547).
- Main drawback: inverting an $N\times N$ matrix. Direct inversion becomes prohibitive when $N$ exceeds about 1000 (p. 547).
- **MacKay's view:** neural networks were over-hyped in 1987 as feature-discovering models, whereas Gaussian processes are simply smoothing devices. He thinks both "over-hyped" and "smoothing is stronger than we assumed" are true. Many real-world problems are well solved by sensible smoothing. Feature discovery is not something Gaussian processes will solve, "but maybe multilayer perceptrons can't solve them either". He suggests a fresh paradigm may be needed (p. 548).

### Further reading (p. 548)
- History: Thiele used Gaussian processes for time series in 1880. Wiener–Kolmogorov prediction theory came in the 1940s. Matheron (1963) proposed "kriging", which MacKay says is identical to the Gaussian-process approach to regression. Geostatistics has focused on low-dimensional problems and largely ignored the probabilistic interpretation.
- Kalman filters implement inference for stationary one-dimensional Gaussian processes. Generalized radial basis functions, ARMA models and variable-metric kernel methods are closely related.
- Williams and Rasmussen (1996) and Neal (1997b) first explored replacing supervised networks by Gaussian processes. Rasmussen (1996) made a thorough comparison with other methods.
- Support vector machines and Gaussian processes are both kernel-based predictors, where the kernel is another name for the covariance function.

## Toy example (ours, not from the text)
One datum, $x_1=0$, $t_1=2$. Use $C(x,x')=\exp[-(x-x')^2]$ (that is (45.30) with $\theta_1=1$, $4r^2=1$) and noise $\sigma_\nu^2=0.25$.

- $\mathbf C_N=[1+0.25]=[1.25]$, so $\mathbf C_N^{-1}=0.8$.
- **New point $x=1$.** $k=C(0,1)=e^{-1}=0.3679$. $\kappa=C(1,1)+0.25=1.25$.
  - Mean (45.42): $\hat t=0.3679\times0.8\times2=0.5886$.
  - Variance (45.43): $1.25-0.3679^2\times0.8=1.25-0.1353\times0.8=1.25-0.1083=1.1417$.
- **New point $x=0$.** $k=1$, $\kappa=1.25$. Mean $=1\times0.8\times2=1.6$. Variance $=1.25-1\times0.8=0.45$.

Reading the result: near the datum the prediction is pulled toward $t_1=2$, but only to 1.6, because of noise. Far from it the mean falls toward the prior mean 0 and the variance rises toward the prior value 1.25. At $x=1$ the mean is 0.59, so the correlation 0.37 decays the influence.

## Concepts
- [[gaussian-process]] (new) — a distribution over functions such that any finite set of function values is jointly Gaussian; given by mean and covariance function (pp. 535, 540)
- [[covariance-function]] (new) — $C(x,x')$, the expected covariance of $y$ at two points; its only constraint is non-negative-definiteness (pp. 535, 543)
- [[stationary-covariance-function]] (new) — depends only on $x-x'$; its Fourier transform is the power spectrum (p. 544)
- [[lengthscale-ard]] (new) — $r_i$ in (45.47); a very large $r_i$ marks input $i$ as irrelevant (p. 544)
- [[hyperparameter]] (new) — parameter $\boldsymbol\theta$ of covariance or noise model, learned from data (p. 546)
- [[spline-smoothing-prior]] (new) — penalty on the $p$th derivative read as a Gaussian prior; MAP estimate (pp. 538–539)
- [[prior-distribution]] — here a prior over functions $P(y(x))$, not over parameters (p. 535)
- [[likelihood]] — $P(\mathbf t_N\mid y(x),\mathbf X_N)$, often separable Gaussian noise (p. 535)
- [[posterior-distribution]] — (45.1) over functions, (45.5) over parameters (pp. 535, 537)
- [[marginal-likelihood]] — the evidence $P(\mathbf t_N\mid\mathbf X_N,\boldsymbol\theta)$; used to adapt hyperparameters (pp. 539, 546)
- [[posterior-predictive-distribution]] — (45.7); for a GP, Gaussian with mean (45.42) and variance (45.43) (pp. 537, 543)
- [[bayesian-occams-razor]] — handles the complexity-control problem of choosing hyperparameters (p. 546)
- [[monte-carlo-integration]] — averaging over posterior samples, (45.8), or over $\boldsymbol\theta$ (pp. 537, 546)
- [[variational-inference-elbo]] — bounds on the unnormalized posterior for GP classification, not an ELBO as such (p. 547)
- [[gp-classification]] (new) — Gaussian process prior on latent $a(x)$ passed through the logistic function (p. 547)

## Canonical instances
- [[spline-prior-as-gp]] — cubic-spline smoothing is MAP under a Gaussian-process prior (pp. 538–539)
- [[rbf-infinite-limit-to-gaussian-kernel]] — infinitely many radial basis functions give a Gaussian covariance (p. 541)
- [[neal-infinite-network-gp]] — one-hidden-layer network converges to a Gaussian process (p. 542)
- [[gp-evidence-multimodality]] — Figure 45.2, two local maxima of the likelihood (p. 545)
- [[kriging]] — identical, per MacKay, to Gaussian-process regression (p. 548)

## Bridges (candidates)
- [same-math] GP predictive mean/variance (45.42–45.43) ↔ bayesian: conditioning a multivariate Gaussian on observed components — the same partitioned-inverse algebra.
- [same-math] Kriging ↔ geostatistics: MacKay says it is identical to GP regression.
- [structural-analogy] ln det C + tᵀC⁻¹t evidence (45.54) ↔ information-theory: the model-plus-data code-length trade-off in MDL.
- [structural-analogy] GP covariance function ↔ kernel methods: the kernel in SVMs, which MacKay says is another name for it (p. 548).
- [structural-analogy] Large $r_i$ marks an irrelevant input ↔ ARD in neural networks (p. 544).
- [metaphor] Prior over functions ↔ choosing the least-committal distribution under smoothness constraints (maximum entropy).

## Questions this raises
- When is a function $C(x,x')$ a valid covariance, beyond the examples given? What does non-negative-definiteness rule out?
- How much does the hyperparameter point estimate $\boldsymbol\theta_{\rm MP}$ matter compared with integrating over $\boldsymbol\theta$, given multimodal evidence?
- Which approximations beat the $O(N^3)$ cost without damaging the error bars?
- How good are the Laplace and variational approximations in GP classification compared with Monte Carlo?

## Exercises worth doing
- Ex. 45.1 (p. 534) — draw pictures to explain the chapter's ideas (for example prior samples, posterior mean and error bars, a multimodal evidence); builds intuition for covariance functions and prediction — difficulty: medium (marked [3] in the source).

## Reading notes
- Printed page = pdf page − 12 (pdf 546 = p. 534). The page labels give the printed numbers.
- The text layer is garbled for eq. (45.15); in the image the exponent on $h$ is the small fraction $p/2$, which I transcribed as $h^{p/2}$.
- In (45.37)–(45.40), the scalar $m$ and the vector $\mathbf m$ differ only by boldface. Read the scalar in (45.38) as $m$, a scalar.
- Printed "superceded" (p. 534) is a misspelling of "superseded".
- The text refers to Figures 44.2 and 44.3 (p. 542) and Chapter 27, section 33.8 (p. 547). Those are outside this unit.
- The chapter has no worked numbers. Figure 45.2 gives only parameter values. The toy example is ours.
