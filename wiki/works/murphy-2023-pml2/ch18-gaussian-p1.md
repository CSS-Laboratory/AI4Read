---
id: murphy-2023-pml2/ch18-gaussian-p1
work: murphy-2023-pml2
unit: "18 Gaussian processes (part 1/2): 18.1–18.4.3 (start)"
pages: 681–703
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Gaussian processes, part 1: kernels, GP regression, non-Gaussian likelihoods

## L0 — One line
A Gaussian process puts a prior directly on functions, defined by a mean function and a kernel. With Gaussian noise the posterior is another GP in closed form, and its mean equals kernel ridge regression (when the penalty λ equals the noise variance).

## L1 — The gist (≤ 120 words)
Fixed-size parametric models can overfit or underfit, so the chapter builds a Bayesian nonparametric model: a prior over functions, updated by data. The kernel encodes which inputs are similar and so controls generalization. With a Gaussian likelihood, prediction is exact linear algebra costing O(N³). A GP with kernel $\phi^\top\Sigma_w\phi$ gives the same predictions as Bayesian linear regression, and its posterior mean equals kernel ridge regression when $\lambda=\sigma_y^2$. The marginal likelihood trades fit against complexity and tunes kernel hyperparameters. Non-Gaussian likelihoods (classification, counts) need approximations such as Laplace or variational inference. The unit stops inside the Cox-process section (18.4.3).

**Prerequisites:** multivariate Gaussians (conditioning, marginals); matrix inverse, Cholesky and eigendecomposition; Bayesian linear regression; Fourier transform (light); Laplace approximation.

## L2 — Key ideas
- A GP is defined by a mean function and a kernel: every finite set of function values is jointly Gaussian, so it is a prior over functions (p. 681–682).
- The kernel must be a symmetric positive definite (Mercer) kernel. Common families are SE, ARD, Matérn, periodic, rational quadratic and polynomial; new kernels come from sums, products and other operations (p. 683–691).
- Mercer's theorem writes a kernel as an eigenfunction sum, i.e. an inner product of (possibly infinite) features. This gives the kernel trick. Random Fourier features approximate it cheaply (p. 692–693).
- With a Gaussian likelihood, the posterior over test values is Gaussian with closed-form mean and covariance. Cost is dominated by the O(N³) Cholesky factorization (p. 694–698).
- A GP with kernel $\phi(x)^\top\Sigma_w\phi(x')$ reproduces Bayesian linear regression. Adding a linear mean gives semiparametric GPs (p. 695–697).
- The log marginal likelihood is a data-fit term plus a log-determinant complexity term. It is used to learn kernel hyperparameters (p. 697).
- Kernel ridge regression in an RKHS (squared loss, $\lambda=\sigma_y^2$) has the same predictions as the GP posterior mean; the representer theorem is used to show this (p. 698–701).
- Non-Gaussian likelihoods give no exact posterior. The chapter uses Laplace or variational approximations, e.g. for binary classification (p. 701–703).

## L3 — Walkthrough

### 18.1 Introduction (pp. 681–683)
- Neural networks $f(x;\theta)$ have a fixed number of parameters. They can overfit when N is small and underfit when N is large. Nonparametric models let capacity adapt to the data (p. 681).
- Here a GP is the prior $p(f)$; Bayes' rule gives $p(f\mid\mathcal D)$, which is again a GP (p. 681).

**18.1.1 What and why.**
- Take a function $f:\mathcal X\to\mathbb R$ and inputs $X=\{x_n\}_{n=1}^N$. If $f_X=[f(x_1),\dots,f(x_N)]$ is jointly Gaussian for any set of $N\ge1$ points, $f$ is a GP. It is defined by a mean function $m(x)$ and a covariance function $\mathcal K(x,x')\ge0$, any positive definite Mercer kernel (p. 681).
- $$f(x)\sim GP(m(x),\mathcal K(x,x'))\tag{18.1}$$
$$m(x)=\mathbb E[f(x)]\tag{18.2}$$
$$\mathcal K(x,x')=\mathbb E\big[(f(x)-m(x))(f(x')-m(x'))^{\mathsf T}\big]\tag{18.3}$$
- For any finite $X$: $p(f_X\mid X)=\mathcal N(f_X\mid\mu_X,\mathbf K_{X,X})$, with $\mu_X=(m(x_1),\dots,m(x_N))$ and $\mathbf K_{X,X}(i,j)=\mathcal K(x_i,x_j)$ (18.4) (p. 682).
- Data: N iid observations with $y_i\sim p(y\mid f(x_i))$. A Gaussian likelihood gives the posterior in closed form (Sec. 18.3). Other likelihoods need approximate inference (Sec. 18.4) (p. 682).
- Figure 18.1: a test point similar to training points gets a similar $f_*$, hence a similar $y_*$ (p. 682).
- GPs began in spatial analysis with 2d inputs (kriging). The author says essentially exact inference can now reach millions of points (Sec. 18.5). GPs can also learn representations, and are described as complementary to neural networks (p. 682–683).
- Reasons to use a GP (p. 683):
  - typically well-calibrated predictive distributions with good epistemic (model) uncertainty;
  - often state of the art for continuous, spatiotemporal regression, with closed-form inference;
  - the marginal likelihood supports flexible kernel learning;
  - they serve as surrogates in Bayesian optimization.

*Intuition note.* A GP says: pick any points, and the function values there are one big Gaussian whose covariances come from the kernel. Nearby inputs get correlated outputs, so data at one point informs predictions at its neighbours.

### 18.2 Mercer kernels (pp. 683–693)
- A Mercer (positive definite) kernel is a symmetric $\mathcal K:\mathcal X\times\mathcal X\to\mathbb R^+$ such that
$$\sum_{i=1}^N\sum_{j=1}^N\mathcal K(x_i,x_j)c_ic_j\ge0\tag{18.5}$$
  for any N distinct points and any real $c_i$ (p. 683). The author assumes $\mathcal K>0$, so equality holds only if all $c_i=0$ (p. 683).
- The Gram matrix is $\mathbf K=[\mathcal K(x_i,x_j)]_{ij}$, $N\times N$ (18.6). The author says $\mathcal K$ is Mercer iff $\mathbf K$ is positive definite for any set of distinct inputs (p. 684).

**18.2.1 Stationary kernels** (functions of $r=x-x'$, also called shift-invariant). Often only the magnitude matters: $r=\|x-x'\|$ (18.7) (p. 684).
- *SE / RBF:* $\mathcal K(r;\ell)=\exp(-r^2/2\ell^2)$ (18.8), equivalently $\exp(-\|x-x'\|^2/2\ell^2)$ (18.9). $\ell$ is the length-scale, the distance over which differences matter (p. 684).
- *ARD:* replace Euclidean by Mahalanobis distance, $\mathcal K(r;\Sigma,\sigma^2)=\sigma^2\exp(-\tfrac12 r^{\mathsf T}\Sigma^{-1}r)$ (18.10). For diagonal $\Sigma$:
$$\mathcal K(r;\ell,\sigma^2)=\sigma^2\exp\Big(-\tfrac12\sum_{d=1}^D\tfrac1{\ell_d^2}r_d^2\Big)=\prod_{d=1}^D\mathcal K(r_d;\ell_d,\sigma^{2/d})\tag{18.11}$$
  with 1d factor $\tau^2\exp(-\tfrac12\ell^{-2}r^2)$ (18.12). $\sigma^2$ is the overall variance and $\ell_d$ the length scale of dimension d. Setting $\ell_d=\infty$ ignores an irrelevant dimension (automatic relevance determination). Fig. 18.2 contrasts $\ell=(1,1)$ with $\ell=(1,5)$, where dimension 2 is essentially ignored (pp. 684–685).
- *Matérn:* SE samples are infinitely differentiable, so very smooth. Matérn gives rougher functions that fit local wiggles without a tiny global length scale (p. 685).
$$\mathcal K(r;\nu,\ell)=\frac{2^{1-\nu}}{\Gamma(\nu)}\Big(\frac{\sqrt{2\nu}r}{\ell}\Big)^{\nu}K_\nu\Big(\frac{\sqrt{2\nu}r}{\ell}\Big)\tag{18.13}$$
  Here $K_\nu$ is a modified Bessel function. Samples are k-times differentiable iff $\nu>k$; as $\nu\to\infty$ it approaches SE (p. 685). Special cases (pp. 686):
$$\mathcal K(r;\tfrac12,\ell)=\exp(-r/\ell)\tag{18.14}$$
$$\mathcal K(r;\tfrac32,\ell)=\Big(1+\tfrac{\sqrt3 r}{\ell}\Big)\exp\Big(-\tfrac{\sqrt3r}{\ell}\Big)\tag{18.15}$$
$$\mathcal K(r;\tfrac52,\ell)=\Big(1+\tfrac{\sqrt5r}{\ell}+\tfrac{5r^2}{3\ell^2}\Big)\exp\Big(-\tfrac{\sqrt5r}{\ell}\Big)\tag{18.16}$$
  $\nu=\tfrac12$ is the Ornstein–Uhlenbeck process (velocity of a Brownian particle); its functions are continuous but not differentiable, hence "jagged" (p. 686).
- *Periodic:* map $x\mapsto u(x)=(\cos x,\sin x)$ and use SE in u-space. This holds since $(\cos x-\cos x')^2+(\sin x-\sin x')^2=4\sin^2((x-x')/2)$:
$$\mathcal K(x,x')=\exp\Big(-\frac{2\sin^2((x-x')/2)}{\ell^2}\Big)\tag{18.17}$$
  With period p: $\mathcal K_{per}(r;\ell,p)=\exp\big(-\tfrac{2}{\ell^2}\sin^2(\pi\tfrac rp)\big)$ (18.18). The cosine kernel is $\cos(2\pi r/p)$ (18.19) (p. 687).
- *Rational quadratic:* $\mathcal K_{RQ}(r;\ell,\alpha)=(1+\tfrac{r^2}{2\alpha\ell^2})^{-\alpha}$ (18.20). It is proportional to a Student t density, so it can be interpreted as a scale mixture of SE kernels. With $\tau=1/\ell^2$ and $\tau\sim\mathrm{Ga}(\alpha,\ell^2)$ (as printed), "one can show" $\mathcal K_{RQ}(r)=\int p(\tau\mid\alpha,\ell^2)\mathcal K_{SE}(r\mid\tau)d\tau$ (18.21). As $\alpha\to\infty$ it reduces to SE (p. 688).
- *Spectral densities.* For a stationary positive definite $\mathcal K(\delta)$, $\delta=x-x'$, Bochner's theorem gives
$$\mathcal K(\delta)=\int_{\mathbb R^d}p(\omega)e^{j\omega^{\mathsf T}\delta}d\omega\tag{18.22}$$
  with $p(\omega)$ the spectral density (p. 688).
  - For RBF the spectral density is Gaussian, $p(\omega)=\sqrt{2\pi\ell^2}\exp(-2\pi^2\omega^2\ell^2)$, with bandwidth inversely proportional to $\ell$. Large $\ell$ means smooth, low-frequency functions. Gaussian tails are light, so RBF kernels won't generally support high frequencies (p. 688).
  - A heavy-tailed Student t spectral density gives the Matérn kernel, with $\nu$ equal to its degrees of freedom. Smaller $\nu$ gives less smooth, higher-frequency fits (p. 688).
  - Modelling $p(\omega)$ as a scale-location mixture of Gaussians gives spectral mixture kernels. These are dense, so they can approximate any stationary kernel to arbitrary precision (p. 688).

*Intuition note.* The length-scale says how far apart two inputs can be and still be correlated. Smoothness (SE versus Matérn) says how jagged samples are. In frequency terms, a heavier-tailed spectrum allows faster wiggles.

**18.2.2 Nonstationary kernels** (similarity depends on location; p. 689).
- *Polynomial (dot-product) kernel of order M:* $\mathcal K(x,x')=(x^{\mathsf T}x')^M$ (18.23). For $M=2$ in 2d: $(x_1x_1'+x_2x_2')^2=(x_1x_1')^2+(x_2x_2')^2+2(x_1x_1')(x_2x_2')$ (18.24). The inhomogeneous version $(x^{\mathsf T}x'+c)^M$ (18.25) contains all terms up to degree M; its $M=2$, $c=1$ expansion is (18.26) (p. 689).
- *Gibbs kernel:* RBF with input-dependent length scale and variance,
$$\mathcal K(x,x')=\sigma(x)\sigma(x')\sqrt{\frac{2\ell(x)\ell(x')}{\ell(x)^2+\ell(x')^2}}\exp\Big(-\frac{\|x-x'\|^2}{\ell(x)^2+\ell(x')^2}\Big)\tag{18.27}$$
  With constant $\ell,\sigma$ it reduces to RBF. $\ell(x),\sigma(x)$ can themselves be modelled by a GP (p. 689).
- Other routes: neural-network kernel, nonstationary spectral kernels, deep GP (p. 689).

**18.2.3 Structured inputs.** Kernels help when inputs are strings or graphs, which are hard to featurize. Examples: a string kernel counting shared n-grams, and a random-walk graph kernel counting paths produced by both walks (p. 690).

**18.2.4 New kernels from old.** For valid $\mathcal K_1,\mathcal K_2$ (p. 690):
$$c\mathcal K_1\ (c>0)\tag{18.28}$$
$$f(x)\mathcal K_1(x,x')f(x')\ \text{for any }f\tag{18.29}$$
$$q(\mathcal K_1)\ \text{for polynomial }q\text{ with nonnegative coefficients}\tag{18.30}$$
$$\exp(\mathcal K_1)\tag{18.31}$$
$$x^{\mathsf T}\mathbf Ax'\ \text{for psd }\mathbf A\tag{18.32}$$
- The linear kernel is valid since its Gram matrix is the (scaled) data covariance matrix. By the rules above, $(x^{\mathsf T}x')^M$ is valid (p. 690).
- Gaussian kernel: $\|x-x'\|^2=x^{\mathsf T}x+x'^{\mathsf T}x'-2x^{\mathsf T}x'$ (18.33), so
$$\exp(-\|x-x'\|^2/2\sigma^2)=\exp(-x^{\mathsf T}x/2\sigma^2)\exp(x^{\mathsf T}x'/\sigma^2)\exp(-x'^{\mathsf T}x'/2\sigma^2)\tag{18.34}$$
  is valid (p. 690).
- Sums (18.35) and products (18.36) of positive definite kernels are always positive definite. A product gives a conjunction of properties (Fig. 18.5, e.g. SE×Per is locally periodic). A sum gives a disjunction (Fig. 18.6, e.g. Lin+Per is periodic plus trend) (pp. 690–691).

**18.2.5 Mercer's theorem.** A positive definite matrix has eigendecomposition $\mathbf K=\mathbf U^{\mathsf T}\mathbf\Lambda\mathbf U$ with $\lambda_i>0$. Then
$$k_{ij}=(\mathbf\Lambda^{1/2}\mathbf U_{:i})^{\mathsf T}(\mathbf\Lambda^{1/2}\mathbf U_{:j})\tag{18.37}$$
With $\phi(x_i)=\mathbf U_{:i}$: $k_{ij}=\sum_{m=1}^M\lambda_m\phi_m(x_i)\phi_m(x_j)$ (18.38), where M is the rank (pp. 691–692).
- An eigenfunction $\phi$ of $\mathcal K$ with eigenvalue $\lambda$ w.r.t. measure $\mu$ satisfies $\int\mathcal K(x,x')\phi(x)d\mu(x)=\lambda\phi(x')$ (18.39). Eigenfunctions are sorted by decreasing eigenvalue and are orthogonal, $\int\phi_i\phi_jd\mu=\delta_{ij}$ (18.40) (p. 692).
- Mercer's theorem (stated informally): any positive definite kernel can be written
$$\mathcal K(x,x')=\sum_{m=1}^\infty\lambda_m\phi_m(x)\phi_m(x')\tag{18.41}$$
- A degenerate kernel has finitely many non-zero eigenvalues. Example: the quadratic kernel $\langle x,x'\rangle^2$ equals $\phi(x)^{\mathsf T}\phi(x')$ with $\phi(x_1,x_2)=[x_1^2,\sqrt2x_1x_2,x_2^2]\in\mathbb R^3$. The RBF kernel's feature representation is infinite-dimensional (p. 692).
- *Kernel trick:* replace an explicit inner product $\phi(x)^{\mathsf T}\phi(x')$ by a kernel call $\mathcal K(x,x')$ (p. 692).

*Intuition note.* A kernel is a dot product between feature vectors you never have to write down. That lets you work with possibly infinitely many features at the cost of evaluating one function.

**18.2.6 Random features.** Kernel methods invert the N×N Gram matrix, $O(N^3)$. Using M random basis functions reduces this to $O(NM+M^3)$ (pp. 692–693).
- For shift-invariant kernels, Bochner's integral (18.22) can be Monte Carlo approximated by sampling frequencies. For RBF the spectral density is Gaussian, so one samples Gaussian vectors. This gives $\mathcal K(x,x')\approx\phi(x)^{\mathsf T}\phi(x')$ (printed with $x$ twice, a typo for $x'$) with
$$\phi(x)=\sqrt{\tfrac1D}\,[\sin(\mathbf z_1^{\mathsf T}x),\dots,\sin(\mathbf z_D^{\mathsf T}x),\cos(\mathbf z_1^{\mathsf T}x),\dots,\cos(\mathbf z_D^{\mathsf T}x)]\tag{18.42}$$
$$=\sqrt{\tfrac1D}\,[\sin(\mathbf Z^{\mathsf T}x),\cos(\mathbf Z^{\mathsf T}x)]\tag{18.43}$$
  where $\mathbf Z=(1/\sigma)\mathbf G$ and $\mathbf G\in\mathbb R^{d\times D}$ has iid $\mathcal N(0,1)$ entries. These are random Fourier features (RFF). Making the rows of $\mathbf Z$ orthogonal gives orthogonal random features (p. 693).
- For supervised learning, $f(x;\theta)=\mathbf W\varphi(\mathbf Zx)+b$ is a one-hidden-layer MLP with random input weights. Only $\theta=(\mathbf W,b)$ is trained, so it is a linear model on fixed random features. With enough features it approximates the kernel method, at cost $O(N)$ rather than $O(N^2)$ (p. 693).
- Random features can perform worse than a non-degenerate kernel because they have less expressive power (p. 693).

### 18.3 GPs with Gaussian likelihoods (pp. 693–701)

**18.3.1 Noise-free observations.** Observe $y_n=f(x_n)$ exactly, so the GP should act as an interpolator of the training data (p. 693). For a test set $\mathbf X_*$ ($N_*\times D$) the joint prior is
$$\begin{pmatrix}f_X\\f_*\end{pmatrix}\sim\mathcal N\Big(\begin{pmatrix}\mu_X\\\mu_*\end{pmatrix},\begin{pmatrix}\mathbf K_{X,X}&\mathbf K_{X,*}\\\mathbf K_{X,*}^{\mathsf T}&\mathbf K_{*,*}\end{pmatrix}\Big)\tag{18.44}$$
with $\mathbf K_{X,X}$ $N\times N$, $\mathbf K_{X,*}$ $N\times N_*$, $\mathbf K_{*,*}$ $N_*\times N_*$ (pp. 693–694). Conditioning Gaussians gives
$$p(f_*\mid\mathbf X_*,\mathcal D)=\mathcal N(f_*\mid\mu_{*|X},\Sigma_{*|X})\tag{18.45}$$
$$\mu_{*|X}=\mu_*+\mathbf K_{X,*}^{\mathsf T}\mathbf K_{X,X}^{-1}(f_X-\mu_X)\tag{18.46}$$
$$\Sigma_{*|X}=\mathbf K_{*,*}-\mathbf K_{X,*}^{\mathsf T}\mathbf K^{-1}\mathbf K_{X,*}\tag{18.47}$$
- Fig. 18.7: posterior samples pass through the training data, and uncertainty grows away from it. Sampling $N_*$ points costs $O(N_*^3)$, reducible to $O(N_*)$ with methods cited by the author (p. 694).

**18.3.2 Noisy observations.** Now $y_n=f(x_n)+\epsilon_n$, $\epsilon_n\sim\mathcal N(0,\sigma_y^2)$. The model need not interpolate but must come "close" (p. 694).
$$\mathrm{Cov}[y_i,y_j]=\mathcal K(x_i,x_j)+\sigma_y^2\delta_{ij}\tag{18.48}$$
$$\mathrm{Cov}[y\mid X]=\mathbf K_{X,X}+\sigma_y^2\mathbf I_N\tag{18.49}$$
Joint of $y$ and the noise-free $f_*$: as (18.44) with $\mathbf K_{X,X}$ replaced by $\mathbf K_{X,X}+\sigma_y^2\mathbf I$ (18.50) (p. 695). Posterior predictive:
$$p(f_*\mid\mathcal D,\mathbf X_*)=\mathcal N(f_*\mid\mu_{*|X},\Sigma_{*|X})\tag{18.51}$$
$$\mu_{*|X}=\mu_*+\mathbf K_{X,*}^{\mathsf T}(\mathbf K_{X,X}+\sigma_y^2\mathbf I)^{-1}(y-\mu_X)\tag{18.52}$$
$$\Sigma_{*|X}=\mathbf K_{*,*}-\mathbf K_{X,*}^{\mathsf T}(\mathbf K_{X,X}+\sigma_y^2\mathbf I)^{-1}\mathbf K_{X,*}\tag{18.53}$$
- For one test input, with $k_*=[\mathcal K(x_*,x_1),\dots,\mathcal K(x_*,x_N)]$ and $k_{**}=\mathcal K(x_*,x_*)$: mean $m_*+k_*^{\mathsf T}(\mathbf K_{X,X}+\sigma_y^2\mathbf I)^{-1}(y-\mu_X)$, variance $k_{**}-k_*^{\mathsf T}(\cdot)^{-1}k_*$ (18.54) (p. 695).
- With zero mean, set $\mathbf K_\sigma=\mathbf K_{X,X}+\sigma_y^2\mathbf I$ (18.56) and $\alpha=\mathbf K_\sigma^{-1}y$ (18.57). Then
$$\mu_{*|X}=k_*^{\mathsf T}\mathbf K_\sigma^{-1}y=\sum_{n=1}^N\mathcal K(x_*,x_n)\alpha_n\tag{18.55}$$
  Fitting means computing $\alpha$. Afterwards each prediction costs $O(N)$ for the mean and $O(N^2)$ for the variance (p. 695).

*Intuition note.* The posterior mean is a weighted sum of kernel bumps centred on the training points. With the noise term $\sigma_y^2\mathbf I$ the fit is not required to pass exactly through the points. The variance is reduced below the prior variance by a term that depends on $k_*$, i.e. on how strongly the training inputs are correlated with the test point.

**18.3.3 Weight space vs function space.** Take linear regression $y=w^{\mathsf T}\phi(x)+\epsilon$ with prior $w\sim\mathcal N(0,\Sigma_w)$. The posterior (derivation in Sec. 15.2.2, not given here) is
$$p(w\mid\mathcal D)=\mathcal N\Big(w\,\Big|\,\tfrac1{\sigma_y^2}\mathbf A^{-1}\Phi^{\mathsf T}y,\ \mathbf A^{-1}\Big),\qquad \mathbf A=\sigma_y^{-2}\Phi^{\mathsf T}\Phi+\Sigma_w^{-1}\tag{18.58–18.59}$$
with $\Phi$ the $N\times D$ design matrix (p. 695). The predictive distribution is
$$p(f_*\mid\mathcal D,x_*)=\mathcal N\Big(f_*\,\Big|\,\tfrac1{\sigma_y^2}\phi_*^{\mathsf T}\mathbf A^{-1}\Phi^{\mathsf T}y,\ \phi_*^{\mathsf T}\mathbf A^{-1}\phi_*\Big)\tag{18.60}$$
This is inference in weight space (p. 696).
- Let $\mathcal K(x,x')=\phi(x)^{\mathsf T}\Sigma_w\phi(x')$, with $\mathbf K=\Phi\Sigma_w\Phi^{\mathsf T}$, $k_*=\Phi\Sigma_w\phi_*$, $k_{**}=\phi_*^{\mathsf T}\Sigma_w\phi_*$. By the matrix inversion lemma, (18.60) becomes
$$\mu_{*|X}=\phi_*^{\mathsf T}\Sigma_w\Phi^{\mathsf T}(\mathbf K+\sigma_y^2\mathbf I)^{-1}y=k_*^{\mathsf T}(\mathbf K_{X,X}+\sigma_y^2\mathbf I)^{-1}y\tag{18.62}$$
$$\Sigma_{*|X}=\phi_*^{\mathsf T}\Sigma_w\phi_*-\phi_*^{\mathsf T}\Sigma_w\Phi^{\mathsf T}(\mathbf K+\sigma_y^2\mathbf I)^{-1}\Phi\Sigma_w\phi_*=k_{**}-k_*^{\mathsf T}(\mathbf K_{X,X}+\sigma_y^2\mathbf I)^{-1}k_*\tag{18.63}$$
  This matches (18.54) when $m(x)=0$. A non-zero mean can be captured by adding a constant feature 1 to $\phi$ (p. 696).
- Linear regression needs a finite-length $\phi$. A GP works with kernels directly, possibly with infinite features: it works in function space (p. 696).

**18.3.4 Semiparametric GPs.** Model $g(x)=f(x)+\beta^{\mathsf T}\phi(x)$ with $f\sim GP(0,\mathcal K)$ and fixed basis functions $\phi$ (18.64). With $\beta\sim\mathcal N(b,\mathbf B)$, integrating $\beta$ out gives the GP
$$g(x)\sim GP\big(\phi(x)^{\mathsf T}b,\ \mathcal K(x,x')+\phi(x)^{\mathsf T}\mathbf B\phi(x')\big)\tag{18.65}$$
Let $\mathbf H_X=\phi(\mathbf X)^{\mathsf T}$ ($D\times N$) and $\mathbf H_*=\phi(\mathbf X_*)^{\mathsf T}$ ($D\times N_*$). The predictive form (cited by the author from the RW06 book) is (p. 696):
$$\mathbb E[g(\mathbf X_*)\mid\mathcal D]=\mathbf H_*^{\mathsf T}\bar\beta+\mathbf K_{X,*}^{\mathsf T}\mathbf K_\sigma^{-1}(y-\mathbf H_X^{\mathsf T}\bar\beta)=\mathbb E[f(\mathbf X_*)\mid\mathcal D]+\mathbf R^{\mathsf T}\bar\beta\tag{18.66}$$
$$\mathrm{Cov}[g(\mathbf X_*)\mid\mathcal D]=\mathrm{Cov}[f(\mathbf X_*)\mid\mathcal D]+\mathbf R^{\mathsf T}(\mathbf B^{-1}+\mathbf H_X\mathbf K_\sigma^{-1}\mathbf H_X^{\mathsf T})^{-1}\mathbf R\tag{18.67}$$
$$\bar\beta=(\mathbf B^{-1}+\mathbf H_X\mathbf K_\sigma^{-1}\mathbf H_X^{\mathsf T})^{-1}(\mathbf H_X\mathbf K_\sigma^{-1}y+\mathbf B^{-1}b)\tag{18.68}$$
$$\mathbf R=\mathbf H_*-\mathbf H_X\mathbf K_\sigma^{-1}\mathbf K_{X,*}\tag{18.69}$$
The mean is the usual GP mean plus a global offset from the linear part. The covariance is the usual one plus a positive term from uncertainty in $\beta$ (p. 696). For an uninformative prior, $\mathbf B\to\infty\mathbf I$, (18.66) and (18.67) become (18.70) and (18.71): $\bar\beta$ is replaced by $(\mathbf H_X\mathbf K_\sigma^{-1}\mathbf H_X^{\mathsf T})^{-1}\mathbf H_X\mathbf K_\sigma^{-1}y$, and the $\mathbf B^{-1}$ terms drop (p. 697).

**18.3.5 Marginal likelihood.** Kernel parameters (e.g. $\ell_d$ in (18.72), the RBF-ARD form) and noise variance are collected in $\theta$. Integrating out $f$:
$$p(y\mid\mathbf X,\theta)=p(\mathcal D\mid\theta)=\int p(y\mid f_X,\theta)p(f_X\mid\mathbf X,\theta)df_X\tag{18.73}$$
Because $f$ is integrated out, $\theta$ are called hyperparameters and $p(\mathcal D\mid\theta)$ is the marginal likelihood (p. 697). Since $f$ is a GP,
$$\log p(\mathcal D\mid\theta)=-\tfrac12(y-\mu_X)^{\mathsf T}\mathbf K_\sigma^{-1}(y-\mu_X)-\tfrac12\log|\mathbf K_\sigma|-\tfrac N2\log(2\pi)\tag{18.74}$$
The first term is a squared Mahalanobis distance (better fits are smaller). The second is a log-determinant measuring complexity: smoother functions have smaller determinants, so $-\log|\mathbf K_\sigma|$ is larger for simpler functions. The marginal likelihood trades off fit and complexity. Hyperparameters can be learned by maximizing it (Sec. 18.6.1, outside this unit) (p. 697).

**18.3.6 Computation** (zero prior mean). Do not invert $\mathbf K_\sigma$ directly. Use the Cholesky factor $\mathbf K_\sigma=\mathbf L\mathbf L^{\mathsf T}$, $O(N^3)$ (p. 697):
$$\mu_*=k_*^{\mathsf T}\mathbf K_\sigma^{-1}y=k_*^{\mathsf T}\mathbf L^{-\mathsf T}(\mathbf L^{-1}y)=k_*^{\mathsf T}\alpha,\quad\alpha=\mathbf L^{\mathsf T}\backslash(\mathbf L\backslash y)\tag{18.75}$$
(backslash = back-substitution). Variance, $O(N^2)$ per test case: $\sigma_*^2=k_{**}-k_*^{\mathsf T}\mathbf L^{-\mathsf T}\mathbf L^{-1}k_*=k_{**}-v^{\mathsf T}v$ with $v=\mathbf L\backslash k_*$ (18.76). Log marginal likelihood:
$$\log p(y\mid\mathbf X)=-\tfrac12y^{\mathsf T}\alpha-\sum_{n=1}^N\log L_{nn}-\tfrac N2\log(2\pi)\tag{18.77}$$
Overall cost is dominated by $O(N^3)$ (p. 698).

**18.3.7 Kernel ridge regression (KRR).**
- Ridge regression: $w^*=\arg\min_w\sum_n(y_n-f(x_n;w))^2+\lambda\|w\|_2^2$ (18.78), with $f=w^{\mathsf T}x$. Solution $w^*=(\mathbf X^{\mathsf T}\mathbf X+\lambda\mathbf I)^{-1}\mathbf X^{\mathsf T}y$ (18.79) (p. 698).
- Function-space version: $f^*=\arg\min_{f\in\mathcal F}\sum_n(y_n-f(x_n))^2+\lambda\|f\|^2$ (18.80). If $\mathcal F$ comes from a positive definite kernel, this is KRR; the author says the estimate will be shown to be equivalent to a GP posterior mean (derived below for $\lambda=\sigma_y^2$) (p. 698).

*18.3.7.1 RKHS.* Functions can be added and scaled like vectors. An inner product $\langle f,g\rangle$ is linear (18.81), symmetric (18.82), $\langle f,f\rangle\ge0$ (18.83), and $\langle f,f\rangle=0$ iff $f(x)=0$ for all x (18.84). Norm: $\|f\|=\sqrt{\langle f,f\rangle}$ (18.85) (p. 698–699).
- A Hilbert space is a complete function space with an inner product. Complete means every Cauchy sequence in it has its limit in it (p. 699).
- Example: $L^2(\mathcal X,\mu)$ with $\mu(A)=\int_Aw(x)dx$ (18.86). It holds functions with $\int f^2w\,dx<\infty$ (18.87) and inner product $\int fgw\,dx$ (18.88) (p. 699).
- An RKHS is a Hilbert space $\mathcal H$ with a symmetric kernel such that $\mathcal K(x,\cdot)\in\mathcal H$ for all x, and the reproducing property holds: $\langle f(\cdot),\mathcal K(\cdot,x')\rangle=f(x')$ (18.89). Hence $\langle\mathcal K(x,\cdot),\mathcal K(\cdot,x')\rangle=\mathcal K(x,x')$ (18.90) (p. 699).

*18.3.7.2 Complexity.* With Mercer's expansion, take $f=\sum_if_i\phi_i$ with $\sum_if_i^2/\lambda_i<\infty$. Then
$$\langle f,g\rangle_{\mathcal H}=\sum_i\frac{f_ig_i}{\lambda_i}\tag{18.91}$$
$$\|f\|_{\mathcal H}^2=\sum_i\frac{f_i^2}{\lambda_i}\tag{18.92}$$
This is analogous to the quadratic form $f^{\mathsf T}\mathbf K^{-1}f$ in GP objectives (18.101). So the function's smoothness is controlled by the kernel's properties (pp. 699–700).

*18.3.7.3 Representer theorem.* Consider $f^*=\arg\min_{f\in\mathcal H_{\mathcal K}}\sum_n\ell(y_n,f(x_n))+\tfrac\lambda2\|f\|_{\mathcal H}^2$ (18.93). One can show (cited, not proved) that
$$f^*(x)=\sum_{n=1}^N\alpha_n\mathcal K(x,x_n)\tag{18.94}$$
Special case: squared loss and $\lambda=\sigma_y^2$, so
$$\mathcal L(f)=\tfrac1{2\sigma_y^2}\sum_n(y_n-f(x_n))^2+\tfrac12\|f\|_{\mathcal H}^2\tag{18.95}$$
Substituting (18.94) and using $\langle\mathcal K(\cdot,x_i),\mathcal K(\cdot,x_j)\rangle=\mathcal K(x_i,x_j)$:
$$\mathcal L=\tfrac12\alpha^{\mathsf T}\mathbf K\alpha+\tfrac1{2\sigma_y^2}\|y-\mathbf K\alpha\|^2\tag{18.96}$$
$$=\tfrac12\alpha^{\mathsf T}(\mathbf K+\tfrac1{\sigma_y^2}\mathbf K^2)\alpha-\tfrac1{\sigma_y^2}y^{\mathsf T}\mathbf K\alpha+\tfrac1{2\sigma_y^2}y^{\mathsf T}y\tag{18.97}$$
Minimizing over $\alpha$ gives $\hat\alpha=(\mathbf K+\sigma_y^2\mathbf I)^{-1}y$, the same as (18.57). (Added step: the gradient is $(\mathbf K+\mathbf K^2/\sigma_y^2)\alpha-\mathbf Ky/\sigma_y^2$. Setting it to zero gives $\mathbf K(\mathbf K+\sigma_y^2\mathbf I)\alpha=\mathbf Ky$, which this $\hat\alpha$ satisfies.) The prediction is
$$\hat f(x_*)=k_*^{\mathsf T}\alpha=k_*^{\mathsf T}(\mathbf K+\sigma_y^2\mathbf I)^{-1}y\tag{18.98}$$
which matches the GP posterior mean (18.55) (p. 700).

*Intuition note.* The RKHS norm is analogous to the quadratic form $f^{\mathsf T}\mathbf K^{-1}f$ that appears in GP objectives. With squared loss and the penalty set to the noise variance ($\lambda=\sigma_y^2$), the KRR solution and the GP posterior mean coincide. The text compares only the means.

*18.3.7.4 KRR vs GPR example.* On a 1d problem believed periodic, the author uses the periodic kernel (18.18) plus a white-noise kernel $\sigma_y^2\delta(x-x')$ (18.99). Both methods have 3 hyperparameters ($\ell,p,\sigma_y^2$, with $\lambda=\sigma_y^2$ for KRR). The GP optimizes them by maximizing the marginal likelihood with gradient descent. KRR uses grid search with cross-validation, which is generally slower. The fits (Fig. 18.8) are very similar, "as is to be expected" (p. 701).

### 18.4 GPs with non-Gaussian likelihoods (pp. 701–703)
- With a non-Gaussian likelihood the posterior can no longer be computed exactly. Table 18.1 lists models by likelihood: regression $\mathcal N(f_i,\sigma_y^2)$; robust regression $\mathcal T_\nu(f_i,\sigma_y^2)$; binary classification $\mathrm{Ber}(\sigma(f_i))$; multiclass $\mathrm{Cat}(\mathrm{softmax}(f_i))$; Poisson regression $\mathrm{Poi}(\exp(f_i))$ (p. 701).

**18.4.1 Binary classification.** With labels $y_n\in\{-1,+1\}$ and sigmoid link, $p(y_n\mid x_n)=\sigma(y_nf_n)$, since $\sigma(-z)=1-\sigma(z)$. The probit link uses $\Phi(y_nf(x_n))$, with $\Phi$ the standard normal cdf (p. 702). Log joint:
$$\mathcal L(f_X)=\log p(y\mid f_X)+\log p(f_X\mid\mathbf X)\tag{18.100}$$
$$=\log p(y\mid f_X)-\tfrac12f_X^{\mathsf T}\mathbf K_{X,X}^{-1}f_X-\tfrac12\log|\mathbf K_{X,X}|-\tfrac N2\log2\pi\tag{18.101}$$
- Laplace approximation. Gradient and Hessian:
$$\nabla\mathcal L=\nabla\log p(y\mid f_X)-\mathbf K_{X,X}^{-1}f_X\tag{18.102}$$
$$\nabla^2\mathcal L=\nabla^2\log p(y\mid f_X)-\mathbf K_{X,X}^{-1}=-\mathbf\Lambda-\mathbf K_{X,X}^{-1}\tag{18.103}$$
  where $\mathbf\Lambda=-\nabla^2\log p(y\mid f_X)$ is diagonal because the likelihood factorizes over examples. Table 18.2 gives per-example derivatives. For logistic, with $t_i=(y_i+1)/2$ and $\pi_i=\sigma(f_i)$, the gradient is $t_i-\pi_i$ and the second derivative is $-\pi_i(1-\pi_i)$. For probit, the gradient is $y_i\phi(f_i)/\Phi(y_if_i)$ and the second derivative is $-\phi_i^2/\Phi(y_if_i)^2-y_if_i\phi(f_i)/\Phi(y_if_i)$. At convergence:
$$p(f_X\mid\mathcal D)\approx q(f_X)=\mathcal N\big(\hat f,(\mathbf K_{X,X}^{-1}+\mathbf\Lambda)^{-1}\big)\tag{18.104}$$
  with $\hat f$ the MAP estimate (p. 702).
- Variational alternative: $q(f_X)=\mathcal N(m,\mathbf S)$ with $m,\mathbf S$ optimized by (stochastic) gradient descent, rather than taking $\mathbf S$ as the Hessian at the mode (details in Sec. 18.5.4, outside this unit) (p. 702).
- Prediction: with a Gaussian $q$, standard GP prediction gives $q(f_*\mid x_*,\mathcal D)$. Then
$$\pi_*=p(y_*=1\mid x_*,\mathcal D)=\int p(y_*=1\mid f_*)q(f_*\mid x_*,\mathcal D)df_*\tag{18.105}$$
  The probit approximation gives $\pi_*\approx\sigma(\kappa(v)\mathbb E[f_*])$ with $v=\mathbb V[f_*]$ and $\kappa^2(v)=(1+\pi v/8)^{-1}$ (p. 702).
- Fig. 18.9 (2d, SE kernel): hand-set short length scale $\ell=0.5$ gives very sharp turns in the decision boundary. Learned hyperparameters ($\ell=1.19$) give a more parsimonious explanation (p. 703).

**18.4.2 Multiclass.** The function returns C logits, $p(y_n\mid x_n)=\mathrm{Cat}(y_n\mid\mathrm{softmax}(f_n))$. It is standard to take $f^c\sim GP(0,\mathcal K_c)$: one latent function per class, a priori independent, possibly with different kernels (p. 703). Approximations listed: Laplace [RW06, Sec. 3.5]; local variational bounds; data-augmentation variational methods; and closed-form Gaussian variational approximations. In the moment-matching version of [Mil+18], with $\omega_k=\exp(\psi_k)\sim\mathrm{Ga}(\alpha,\beta)$, the likelihood is replaced by $\mathcal N(\psi_k\mid m_k,v_k)$ with $m_k=\log(\alpha/\beta)-0.5\sigma^2$ and $v_k=\sigma^2=\log(1+\beta/\alpha)$ (p. 703).

**18.4.3 Poisson regression (Cox process)** *(unit ends mid-section).* The log rate is modelled by a GP, called a Cox process. Inference can use Laplace, MCMC or SVI. Fig. 18.10 (not among these pages) is a 1d example with a Matérn-5/2 kernel (p. 703).

## Toy example (ours, not from the text)
One training point, zero mean, RBF kernel with $\ell=1$: $\mathcal K(x,x')=\exp(-(x-x')^2/2)$. Training: $x_1=0$, $y_1=1$. Test: $x_*=1$.

- $\mathbf K_{X,X}=\mathcal K(0,0)=1$; $k_*=\exp(-1/2)=0.6065$; $k_{**}=1$.
- **Noise-free (18.46–18.47):** mean $=0.6065\times1/1=0.6065$. Variance $=1-0.6065^2=1-0.3679=0.6321$. The mean is pulled toward $y_1$ and the variance is smaller than the prior's 1.
- **Noisy, $\sigma_y^2=0.25$ (18.52–18.53):** $\mathbf K_\sigma=1.25$, so $\alpha=1/1.25=0.8$. Mean $=0.6065\times0.8=0.4852$. Variance $=1-0.3679/1.25=1-0.2943=0.7057$. Noise shrinks the mean and leaves more uncertainty.
- **Cholesky check (18.75–18.76):** $L=\sqrt{1.25}=1.1180$, $v=0.6065/1.1180=0.5425$, $v^2=0.2943$, so variance $=1-0.2943$ (matches).
- **KRR check (18.98):** $\hat f=k_*^{\mathsf T}(\mathbf K+\sigma_y^2)^{-1}y=0.6065\times0.8=0.4852$, the same as the GP mean.

## Concepts
- [[gaussian-process]] (new) — prior over functions: any finite set of values is jointly Gaussian; set by mean and kernel (p. 681)
- [[mercer-kernel]] (new) — symmetric positive definite function giving similarity; Gram matrix is positive definite (p. 683)
- [[stationary-kernel]] (new) — kernel depending only on $x-x'$ (p. 684)
- [[matern-kernel]] (new) — kernel with smoothness parameter $\nu$; k-times differentiable samples iff $\nu>k$ (p. 685)
- [[ard-kernel]] (new) — RBF with a length scale per dimension; $\ell_d=\infty$ ignores dimension d (p. 685)
- [[bochner-spectral-density]] (new) — stationary positive definite kernel as Fourier transform of a spectral density (p. 688)
- [[mercer-theorem]] (new) — kernel as eigenfunction sum, the functional form of a feature inner product (p. 692)
- [[kernel-trick]] (new) — replace feature inner products by kernel evaluations (p. 692)
- [[random-fourier-features]] (new) — Monte Carlo approximation of a shift-invariant kernel by random sin/cos features (p. 693)
- [[posterior-predictive-distribution]] — GP predictive $\mathcal N(\mu_{*|X},\Sigma_{*|X})$ at test inputs (p. 695)
- [[marginal-likelihood]] — $p(\mathcal D\mid\theta)$ with $f$ integrated out; fit plus complexity (p. 697)
- [[weight-space-vs-function-space]] (new) — Bayesian linear regression equals a GP with kernel $\phi^{\mathsf T}\Sigma_w\phi$ (p. 696)
- [[rkhs]] (new) — Hilbert space with kernel satisfying the reproducing property (p. 699)
- [[representer-theorem]] (new) — regularized RKHS minimizer is $\sum_n\alpha_n\mathcal K(x,x_n)$ (p. 700)
- [[kernel-ridge-regression]] (new) — squared-loss RKHS-penalized fit; same mean as the GP posterior when $\lambda=\sigma_y^2$ (p. 698–700)
- [[laplace-approximation-gp]] (new) — Gaussian posterior at the MAP with covariance $(\mathbf K^{-1}+\mathbf\Lambda)^{-1}$ (p. 702)

## Canonical instances
- [[gp-prior-posterior-samples]] — samples from a GP prior, a noise-free posterior and a noisy posterior (Fig. 18.7) (p. 694)
- [[krr-vs-gpr-periodic]] — periodic kernel; KRR and GPR fits very similar (Fig. 18.8) (p. 701)
- [[gp-binary-classification-2d]] — SE-kernel GP classifier with hand-set vs learned length scale (Fig. 18.9) (p. 703)
- [[kernel-sum-product-examples]] — structures from products and sums of kernels (Figs. 18.5–18.6) (p. 691)

## Bridges (candidates)
- [same-math] GP posterior mean (18.55) ↔ kernel ridge regression: equal when loss is squared and $\lambda=\sigma_y^2$ (p. 700).
- [same-math] Bayesian linear regression with prior $\mathcal N(0,\Sigma_w)$ ↔ GP with kernel $\phi^{\mathsf T}\Sigma_w\phi$: identical predictive mean and variance (p. 696).
- [structural-analogy] Fit-plus-complexity split of the log marginal likelihood (18.74) ↔ bayesian-occam-razor (canon link; the text does not use that name).
- [structural-analogy] Rational quadratic kernel as a gamma mixture of SE length scales ↔ hierarchical model: a hyperprior over a scale parameter (p. 688).

## Questions this raises
- How can the $O(N^3)$ cost be cut while keeping inference close to exact (promised in Sec. 18.5)?
- How are kernel hyperparameters learned by maximizing the marginal likelihood, and can it overfit (Sec. 18.6.1)?
- How accurate is the Laplace approximation compared with variational inference for GP classifiers?
- Which kernel structures (sum vs product) suit a given real data set, e.g. a time series (Sec. 18.8.1)?

## Reading notes
- This is part 1 of Chapter 18. It starts at 18.1 (p. 681) and ends on p. 703, mid-sentence inside 18.4.3 (Cox process). Printed = pdf − 34.
- Edition as printed: "Probabilistic Machine Learning: Advanced Topics", online version, December 10, 2025; author line Kevin P. Murphy, MIT Press, CC-BY-NC-ND. The chapter says it is coauthored with Andrew Wilson.
- Slips seen in the page images:
  - (18.26) lacks primes in one term.
  - The approximation printed in the prose just before (18.42) reads $\mathcal K(x,x')\approx\phi(x)^{\mathsf T}\phi(x)$, where $\phi(x')$ is meant.
  - (18.62) prints $\sigma_y\mathbf I$ without the square in its second form.
  - In 18.3.7.2 the text writes $f_i\phi(x)$ where $f_i\phi_i(x)$ is meant.
  - In 18.4.1, the text prints $p(y_n=1\mid x_n)=\sigma(y_nf(x_n))$, with $y_n$ inside $\sigma$ although the left side already fixes $y_n=1$; I keep it as printed.
  - In 18.2.1.2, the text after (18.12) interprets $\sigma^2$ while (18.12) uses $\tau^2$.
- Equation (18.5) says $\ge0$, while the prose says equality only when all $c_i=0$ (assumes $\mathcal K>0$). I report both as printed.
- The unit's equations are readable in the page images.
