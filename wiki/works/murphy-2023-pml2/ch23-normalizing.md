---
id: murphy-2023-pml2/ch23-normalizing
work: murphy-2023-pml2
unit: "23 Normalizing flows"
pages: 829-847
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Normalizing flows

## L0 — One line
A normalizing flow turns a simple base distribution into a complex one through an invertible map whose Jacobian determinant is cheap to compute, giving easy sampling and an exact likelihood (p. 829).

## L1 — The gist (≤ 120 words)
The chapter asks how to build flexible density models that are easy to sample from and have an exact, efficiently computable likelihood. The answer is to push a simple base distribution through an invertible map and use the change-of-variables formula. The work lies in designing invertible maps with cheap Jacobian determinants. The chapter covers affine, elementwise, coupling, autoregressive, residual and continuous-time constructions. Each has different costs for the forward map, the inverse and the determinant. Density estimation needs a fast inverse; variational inference needs fast sampling. So different flows suit different tasks. The chapter ends with applications to density estimation, generation and inference.

**Prerequisites:** change of variables for densities; Jacobian matrices and determinants; triangular matrices; ELBO and the reparameterization trick; inverse-transform sampling; basic ODEs.

## L2 — Key ideas (5–10 bullets)
- A flow is $x=f(u)$ with $u\sim p(u)$ and $f$ invertible. The density follows from the change-of-variables formula. Sampling needs $f$; likelihood needs $f^{-1}$ and a Jacobian determinant (pp. 829–830).
- Composing bijections multiplies their Jacobian determinants. The log determinants add, so complex flows can be built from simple parts (p. 830).
- Training for density estimation needs fast $f^{-1}$ and its determinant. Variational inference needs fast sampling and density of those samples. So the two tasks put different demands on a flow (pp. 831–832).
- Coupling layers (transform one block, conditioned on the other) and autoregressive bijections both give (block-)triangular Jacobians, and the conditioner can be an arbitrary function such as a deep network. For autoregressive bijections the determinant costs $O(D)$; for a coupling layer it equals $\det\mathbf J(\hat f)$, which is cheap when $\hat f$ is elementwise (pp. 835–837).
- Autoregressive flows are asymmetric. MAF has a fast inverse (good for density estimation). IAF has a fast forward map (good for variational posteriors and distillation) (pp. 837, 840–841).
- Residual flows $f(u)=u+\mathbf F(u)$ are invertible under certain conditions on $\mathbf F$. Contractive blocks guarantee invertibility (inverse by fixed-point iteration, log-determinant by power series and stochastic trace estimates). Low-rank (bottleneck) blocks give a cheap determinant, but invertibility is not guaranteed and must be checked case by case (pp. 842–844).
- Continuous-time flows define $f$ by an ODE. The inverse is the reversed ODE. The log-determinant solves another ODE driven by the Jacobian trace (pp. 844–845).
- Flows are applied to density estimation, generative modelling and inference, including variational posteriors, importance sampling, HMC and simulation-based inference (pp. 846–847).

## L3 — Walkthrough

### 23.1 Introduction
Normalizing flows are flexible density models that are easy to sample and have an exact likelihood that is efficient to compute (p. 829).

#### 23.1.1 Preliminaries
- **Definition.** Draw $u\in\mathbb R^D$ from a simple base distribution $p(u)$ (e.g. standard Gaussian or uniform). Pass it through an invertible nonlinear map $f:\mathbb R^D\to\mathbb R^D$ (p. 829):
$$x=f(u),\quad u\sim p(u)\tag{23.1}$$
- Sampling: draw $u$, compute $f(u)$. For the density, let $g=f^{-1}$ be the inverse, which "normalizes" the data back to the base distribution. The change-of-variables formula gives (p. 829):
$$p_x(x)=p_u(g(x))\,|\det \mathbf J(g)(x)|=p_u(u)\,|\det \mathbf J(f)(u)|^{-1}\tag{23.2}$$
where $\mathbf J(f)(u)=\partial f/\partial u|_u$. Taking logs (p. 829):
$$\log p_x(x)=\log p_u(u)-\log|\det \mathbf J(f)(u)|\tag{23.3}$$
- So flexible invertible $f$ with an efficient Jacobian determinant give complex densities with exact sampling and exact likelihood. This contrasts with latent-variable models, which need methods like variational inference to lower-bound the likelihood (p. 830).
- **Expressiveness (sketch, not a full proof).** Take a one-dimensional uniform base. Inverse-transform sampling uses the inverse cdf. If $f$ is powerful enough to model the inverse cdf, any one-dimensional density can be sampled. This is reasonable for well-behaved densities with invertible, differentiable cdf. In several dimensions, write $p(x)$ as a product of 1-D conditionals by the chain rule and apply the argument to each. The result is a flow from a product of uniforms to any desired $p(x)$. The authors refer to [Pap+19] for a detailed proof (p. 830).
- **Two ways to get flexible invertible maps** (details in 23.2): (i) simple bijections with easy Jacobian determinant, e.g. triangular Jacobian; (ii) composition. If $f=f_N\circ\cdots\circ f_1$ with each $f_i$ invertible, then $f$ is invertible with $g=g_1\circ\cdots\circ g_N$ and (p. 830)
$$\log|\det \mathbf J(g)(x)|=\sum_{i=1}^N\log|\det \mathbf J(g_i)(u_i)|\tag{23.4}$$
where $u_i=f_i\circ\cdots\circ f_1(u)$ is the $i$-th intermediate output.
- **Terminology.** Bijection = invertible map. Diffeomorphism = differentiable bijection with differentiable inverse; flow maps are diffeomorphisms, but the chapter says "bijection". The density $p_x$ is the *pushforward* $f_*p_u$. In mathematics a "flow" is a family of diffeomorphisms $f_t$ with $f_0$ the identity and $f_{t_1+t_2}=f_{t_2}\circ f_{t_1}$. ML uses the word by analogy, with $t$ like the number of composed maps (p. 830).

*Intuition note:* Think of $u$ as clay and $f$ as a reshaping that never tears or folds. Density gets diluted where the map stretches space and concentrated where it squeezes, and the Jacobian determinant measures that stretch.

#### 23.1.2 How to train a flow model
Two common uses: density estimation, and variational inference. They optimize different objectives and put different computational constraints on the flow (p. 831).

**23.1.2.1 Density estimation.** Maximize the likelihood (23.2). This needs efficient evaluation of $u=f^{-1}(x)$ and $\det \mathbf J(f^{-1})(x)$ for any datapoint $x$. Generating new data afterwards needs a tractable forward map $f$ (p. 831).

**23.1.2.2 Variational inference.** Approximate the true posterior $p^*(z|x)$ of a latent-variable model (continuous $z$, model parameters fixed) with a flow $q_\theta(z|x)$. Maximize the ELBO (p. 831):
$$L(\theta)=\mathbb E_{q_\theta(z|x)}[\log p(x|z)+\log p(z)-\log q_\theta(z|x)]\tag{23.5}$$
Dropping $x$, this is $L(\theta)=\mathbb E_{q_\theta(z)}[\ell_\theta(z)]$ (23.6) (added step: $\ell_\theta$ is the bracketed integrand of 23.5). With base $q(u)$ and $z=f_\theta(u)$, the reparameterization trick gives (p. 831)
$$L(\theta)=\mathbb E_{q(u)}[\ell_\theta(f_\theta(u))]\tag{23.7}$$
Since $q(u)$ does not depend on $\theta$,
$$\nabla_\theta L(\theta)=\mathbb E_{q(u)}[\nabla_\theta\ell_\theta(f_\theta(u))]\approx\frac1N\sum_{n=1}^N\nabla_\theta\ell_\theta(f_\theta(u_n)),\quad u_n\sim q(u)\tag{23.8}$$
So optimization needs efficient sampling from $q_\theta(z|x)$ and evaluation of the density of those samples. This is in contrast to MLE, which needs the density of arbitrary training points but no samples during optimization (p. 832).

*Intuition note:* MLE asks "how likely is this given datapoint?", which needs the inverse direction. The ELBO asks "how likely are my own samples?", which needs the forward direction.

### 23.2 Constructing flows
The goal is flows that are invertible by design with efficient Jacobian determinants (p. 832).

#### 23.2.1 Affine flows
- $x=f(u)=\mathbf Au+b$ is a bijection if and only if $\mathbf A$ is an invertible square matrix. $\det \mathbf J(f)=\det\mathbf A$; $u=\mathbf A^{-1}(x-b)$. Called an affine flow (linear flow if $b$ is ignored) (p. 832).
- On their own, affine flows are limited in expressive power. With Gaussian base $\mathcal N(u|\mu,\Sigma)$ the result is still Gaussian, $\mathcal N(x|\mathbf A\mu+b,\mathbf A\Sigma\mathbf A^\top)$. But affine maps are useful with non-affine maps because they "mix" dimensions (p. 832).
- Costs: general $\det\mathbf A$ and $\mathbf A^{-1}$ take $O(D^3)$. Diagonal $\mathbf A$: $O(D)$. Triangular $\mathbf A$: determinant is the product of diagonal entries, $O(D)$. Inversion is back-substitution, $O(D^2)$ (p. 832).
- Triangular maps depend on the dimension ordering. Multiplying by a permutation matrix (absolute determinant 1) reduces this and mixes dimensions. Permutations are usually fixed, not learned (p. 832).
- For images, $\mathbf A$ can be a convolution matrix. GLOW uses $1\times1$ convolution. [HBW19] give two general $d\times d$ convolution methods (p. 832).

#### 23.2.2 Elementwise flows
Apply a scalar bijection $h$ to each coordinate, $f(u)=(h(u_1),\dots,h(u_D))$. The determinant is $\prod_i dh/du_i$. On their own these flows are limited because they model no dependence between coordinates. They are building blocks for coupling and autoregressive flows (pp. 832–833).

- **23.2.2.1 Affine scalar bijection.** $h(u;\theta)=au+b$, $\theta=(a,b)$, $dh/du=a$. Invertible iff $a\ne0$. Usually $a$ is made positive (exponential or softplus of a free parameter). $a=1$ gives the additive bijection (p. 833).
- **23.2.2.2 Higher-order perturbations.** Non-linear squared flow (NLSq) [ZR19b] (p. 833):
$$h(u;\theta)=au+b+\frac{c}{1+(du+e)^2}\tag{23.9}$$
with $\theta=(a,b,c,d,e)$. $c=0$ gives the affine case; $c\neq0$ adds an inverse-quadratic perturbation that can induce multimodality (Fig. 23.1). Under $a>\frac{9}{8\sqrt3}cd$ and $d>0$ it is invertible, with an analytic inverse from solving a quadratic polynomial (p. 833).
- **23.2.2.3 Monotonic combinations.** Strictly monotonic functions are invertible (e.g. logistic sigmoid). If $h_1,\dots,h_K$ are strictly increasing, so are $a_1h_1+\dots+a_Kh_K+b$ with $a_k>0$ (conical combination) and $h_1\circ\cdots\circ h_K$. A composition of conical combinations of sigmoids is an MLP with all weights positive. The derivative comes from the chain rule (autodiff). The inverse is usually not closed-form, so use bisection search (pp. 833–834).
- **23.2.2.4 Integration.** Make $h'=dh/du$ positive and integrate. Wehenkel and Louppe parameterize $h'$ by a network with output made positive by ELU shifted up by 1, and integrate numerically (p. 834):
$$h(u)=\int_0^u h'(t)\,dt+b\tag{23.10}$$
Jaini et al. take $h'$ as a sum of $K$ squared polynomials of degree $L$, which is integrable analytically. Then $h$ is an increasing polynomial of degree $2L+1$; $L=0$ gives an affine bijection (p. 834):
$$h'(u)=\sum_{k=1}^K\Big(\sum_{\ell=0}^L a_{k\ell}u^\ell\Big)^2\tag{23.11}$$
The derivative is read off, but the inverse is generally computed by bisection (p. 834).
- **23.2.2.5 Splines.** Piecewise polynomial or rational functions through $K+1$ knots $(u_k,x_k)$ with $h(u_k)=x_k$. Linear interpolation gives discontinuous derivatives at knots. Quadratic gives continuous derivatives. Cubic, ratios of linear, or ratios of quadratic polynomials let knot derivatives be free parameters. Strictly increasing if $u_{k-1}<u_k$, $x_{k-1}<x_k$ and the interpolation is increasing. If the pieces are low-degree polynomials, inversion is analytic: binary search for the interval, then solve the polynomial (pp. 834–835).

#### 23.2.3 Coupling flows
Split $u=(u^A,u^B)\in\mathbb R^d\times\mathbb R^{D-d}$, $1\le d\le D-1$. Let $\hat f(\cdot;\theta)$ be a bijection on $\mathbb R^d$ (p. 835):
$$x^A=\hat f(u^A;\Theta(u^B))\tag{23.12}$$
$$x^B=u^B\tag{23.13}$$
$\Theta$ is an arbitrary function (the *conditioner*), typically a deep network. Unlike affine flows (linear mixing) and elementwise flows (no mixing), coupling flows mix dimensions with a flexible nonlinear conditioner (p. 836). The inverse just replaces $\hat f$ by $\hat f^{-1}$ (p. 836):
$$u^A=\hat f^{-1}(x^A;\Theta(x^B)),\qquad u^B=x^B\tag{23.14, 23.15}$$
Because $x^B$ does not depend on $u^A$, the Jacobian is block triangular (p. 836):
$$\mathbf J(f)=\begin{pmatrix}\partial x^A/\partial u^A&\partial x^A/\partial u^B\\ \partial x^B/\partial u^A&\partial x^B/\partial u^B\end{pmatrix}=\begin{pmatrix}\mathbf J(\hat f)&\partial x^A/\partial u^B\\ \mathbf 0&\mathbf I\end{pmatrix}\tag{23.16}$$
so $\det\mathbf J(f)=\det\mathbf J(\hat f)$. Usually $\hat f$ is elementwise, $\hat f(u^A;\theta)=(h(u_1^A;\theta_1),\dots,h(u_d^A;\theta_d))$ (23.17), with $h$ any bijection of 23.2.2. A simple partition is into two halves; for images a checkerboard pattern can be used. In practice different partitions are typically employed along a coupling flow, so that all variables get transformed and can interact. With a binary mask $b$ (0 = transformed, 1 = unchanged) (p. 836):
$$x=b\odot u+(1-b)\odot\hat f(u;\Theta(b\odot u))\tag{23.18}$$
Example: a masked coupling flow of piecewise rational quadratic splines fit to two moons (Fig. 23.3) (p. 836).

*Intuition note:* Half the variables pass through unchanged, so the map is trivially invertible. The unchanged half can steer the transform of the other half through any network, since the network never needs inverting.

#### 23.2.4 Autoregressive flows
For $u=(u_1,\dots,u_D)$ the autoregressive bijection is (p. 837)
$$x_i=h(u_i;\Theta_i(x_{1:i-1})),\quad i=1,\dots,D\tag{23.19}$$
with $h$ a scalar bijection and $\Theta_i$ an arbitrary conditioner. Inverse (p. 837):
$$u_i=h^{-1}(x_i;\Theta_i(x_{1:i-1}))\tag{23.20}$$
$x_i$ depends on $u_{1:i}$ but not $u_{i+1:D}$, so $\partial x_i/\partial u_j=0$ for $j>i$. The Jacobian is triangular (p. 837):
$$\det\mathbf J(f)=\prod_{i=1}^D\frac{\partial x_i}{\partial u_i}=\prod_{i=1}^D\frac{dh}{du_i}\tag{23.21}$$
which costs $O(D)$. **Asymmetry:** computing $f$ is inherently sequential (needs $x_{1:i-1}$ first). Computing $f^{-1}$ is inherently parallel, because $u$ does not appear on the right of (23.20). So $f^{-1}$ is often faster, if $h$ and $h^{-1}$ cost about the same (pp. 837–838).

*Intuition note:* Each coordinate is generated by a rule that looks only at earlier coordinates. Given a full $x$, all the rules can be checked at once. Producing $x$ from scratch has to go one coordinate at a time.

**23.2.4.1 Affine autoregressive flows.** Take $h$ affine with log-scale $\alpha_i$ and bias $\mu_i$ (p. 838):
$$x_i=u_i\exp(\alpha_i(x_{1:i-1}))+\mu_i(x_{1:i-1})\tag{23.22}$$
$$u_i=(x_i-\mu_i(x_{1:i-1}))\exp(-\alpha_i(x_{1:i-1}))\tag{23.23}$$
$$\log|\det\mathbf J(f)|=\log\Big|\prod_{i=1}^D\exp\alpha_i\Big|=\sum_{i=1}^D\alpha_i(x_{1:i-1})\tag{23.24}$$
In 2D with $u\sim\mathcal N(0,\mathbf I)$ and one layer, $x_1$ is Gaussian (mean $\mu_1$, sd $\sigma_1=e^{\alpha_1}$) and $x_2$ given $x_1$ is Gaussian (mean $\mu_2(x_1)$, sd $\sigma_2(x_1)=e^{\alpha_2(x_1)}$). So a single affine autoregressive bijection always gives Gaussian conditionals (p. 839):
$$p(x_1,x_2)=\mathcal N(x_1|\mu_1,\sigma_1^2)\,\mathcal N(x_2|\mu_2(x_1),\sigma_2(x_1)^2)\tag{23.25}$$
This generalizes to $D$ dimensions. One layer is weak however flexible $\alpha_2,\mu_2$ are: the maximum-likelihood fit to a cross-shaped density fails (Fig. 23.5b). Composing 5 layers and reversing the variable order after each layer matches the density and the Gaussian base (Fig. 23.5c). A more flexible $h$ (monotonic MLP or spline) is another remedy (p. 839).

**23.2.4.2 Masked autoregressive flows (MAF).** Separate networks per $\Theta_i$ are parameter-inefficient for large $D$. Instead share parameters in one network $\Theta$ outputting $(\theta_1,\dots,\theta_D)$, with connections dropped so $\theta_i$ depends only on $x_{1:i-1}$. MAF [PPM17] is an affine autoregressive flow with permutation layers. Its conditioner is an MLP whose weight matrices are multiplied elementwise by binary masks (built by the method of [Ger+15]). This zeroes all paths from $x_j$ to $\theta_i$ when $j\ge i$ and costs the same as the unmasked MLP (pp. 839–840). Given $x$, one network evaluation gives all parameters, so $f^{-1}$ and the density are fast. Computing $f$ needs $D$ conditioner calls, so sampling is $D$ times more expensive than density evaluation. MAF suits density estimation, less so generation (p. 840).

**23.2.4.3 Inverse autoregressive flows (IAF).** Make $\theta_i$ depend on previous *inputs* instead (p. 840):
$$x_i=h(u_i;\Theta_i(u_{1:i-1}))\tag{23.26}$$
The Jacobian is again triangular with $\det=\prod_i dh/du_i$. Swapping $u\leftrightarrow x$ and $h\leftrightarrow h^{-1}$ turns (23.26) into (23.20). So this is a direct parameterization of the inverse of an autoregressive bijection, and the speeds swap: $f$ is parallel and fast, $f^{-1}$ is sequential and slow (p. 841). The IAF model [Kin+16] (affine $h$, masked conditioners, permutations) is precisely the inverse of MAF. It generates $x$ in parallel. Evaluating $p(x)$ at an external $x$ is slow. The likelihood of its own samples costs nothing extra, since the $u_i$ are already computed (p. 841).
- Uses: (a) variational posteriors, since the ELBO needs only samples and their densities. (b) Mimicking models that have a fast density but slow sampling. Example: parallel WaveNet [Oor+18], an IAF $p_s$ trained to mimic a pretrained WaveNet $p_t$ by minimizing $D_{\mathbb{KL}}(p_s\|p_t)$. This KL is estimated by sampling from $p_s$ and evaluating $\log p_s$ and $\log p_t$ there. The result generates audio of similar quality, much faster (p. 841).

**23.2.4.4 Connection with autoregressive models.** A continuous autoregressive model $p(x)=\prod_i p_i(x_i|\theta_i)$, $\theta_i=\Theta_i(x_{1:i-1})$ (23.27) is sampled by $x_i\sim p_i(x_i|\Theta_i(x_{1:i-1}))$ (23.28). By inverse-transform sampling (p. 842):
$$x_i=\mathrm{CDF}_i^{-1}(u_i|\Theta_i(x_{1:i-1})),\quad u_i\sim U(0,1)\tag{23.29}$$
This is a one-layer autoregressive flow with base uniform on $[0,1]^D$ and scalar bijections equal to inverse conditional cdfs. Advantage: its flexibility can be raised by composing several, without losing tractability (p. 842).

#### 23.2.5 Residual flows
A residual connection is $f(u)=u+\mathbf F(u)$, with residual block $\mathbf F:\mathbb R^D\to\mathbb R^D$. Under certain conditions on $\mathbf F$ it is invertible; flows of such connections are residual flows (p. 842).

**23.2.5.1 Contractive residual blocks.** $\mathbf F$ is a contraction if there is $0\le L<1$ with (p. 842)
$$\|\mathbf F(u_1)-\mathbf F(u_2)\|\le L\|u_1-u_2\|\tag{23.30}$$
*Invertibility:* $g(u)=x-\mathbf F(u)$ is also a contraction, so by Banach's fixed-point theorem it has a unique fixed point $u_*$ (p. 842):
$$u_*=x-\mathbf F(u_*)\ \Rightarrow\ u_*+\mathbf F(u_*)=x\ \Rightarrow\ f(u_*)=x\tag{23.31–23.33}$$
By uniqueness $u_*=f^{-1}(x)$. iResNet [Beh+19] uses convolutional residual blocks. A composition's Lipschitz constant is at most the product of its parts' constants. So it suffices to make convolutions contractive (spectral normalization of weights) and use increasing activations with slope $\le1$ (pp. 842–843).
- *Inverse:* no closed form, but iterate $u_n=g(u_{n-1})=x-\mathbf F(u_{n-1})$ (23.34). It converges to $f^{-1}(x)$ from any $u_0$, at rate $O(L^n)$. Choosing $u_0=x$ is convenient (p. 843).
- *Determinant:* exact cost is $O(D^3)$. Use the power series (p. 843):
$$\log|\det\mathbf J(f)|=\log|\det(\mathbf I+\mathbf J(\mathbf F))|=\sum_{k=1}^\infty\frac{(-1)^{k+1}}{k}\mathrm{tr}\big[\mathbf J(\mathbf F)^k\big]\tag{23.35}$$
It converges when the matrix norm of $\mathbf J(\mathbf F)$ is below 1, which is guaranteed here because $\mathbf F$ is a contraction. Traces are estimated by the Hutchinson estimator, using Jacobian-vector products, with $v$ of zero mean and unit covariance, e.g. $\mathcal N(0,\mathbf I)$ (p. 843):
$$\mathrm{tr}\big[\mathbf J(\mathbf F)^k\big]\approx v^\top\mathbf J(\mathbf F)^kv\tag{23.36}$$
The infinite series is cut by truncation (biased) or by the Russian-roulette estimator (unbiased) (p. 843).

**23.2.5.2 Low-rank Jacobian blocks.** For $\mathbf A$ ($D\times M$) and $\mathbf B$ ($M\times D$), the Weinstein–Aronszajn identity (a special case of the matrix determinant lemma) is (p. 843)
$$\det(\mathbf I_D+\mathbf A\mathbf B)=\det(\mathbf I_M+\mathbf B\mathbf A)\tag{23.37}$$
It turns an $O(D^3)$ determinant into an $O(M^3)$ one, which saves work if $M<D$. Build a bottleneck $\mathbf F=\mathbf F_2\circ\mathbf F_1$, $\mathbf F_1:\mathbb R^D\to\mathbb R^M$, $\mathbf F_2:\mathbb R^M\to\mathbb R^D$, $M\ll D$. Then $\mathbf J(\mathbf F)=\mathbf J(\mathbf F_2)\mathbf J(\mathbf F_1)$ ($D\times M$ times $M\times D$) and (p. 844)
$$\det\mathbf J(f)=\det(\mathbf I_D+\mathbf J(\mathbf F_2)\mathbf J(\mathbf F_1))=\det(\mathbf I_M+\mathbf J(\mathbf F_1)\mathbf J(\mathbf F_2))\tag{23.38}$$
*Planar flow* [RM15]: one hidden layer, one hidden unit (p. 844):
$$f(u)=u+v\,\sigma(w^\top u+b)\tag{23.39}$$
with $v,w\in\mathbb R^D$, $b\in\mathbb R$. Here $\mathbf F_1(u)=w^\top u+b$, $\mathbf F_2(z)=v\sigma(z)$, $M=1$, $\mathbf J(\mathbf F_1)=w^\top$, $\mathbf J(\mathbf F_2)=v\sigma'(z)$. So
$$\det\mathbf J(f)(u)=1+w^\top v\,\sigma'(w^\top u+b)\tag{23.40}$$
computable in $O(D)$. Other examples: circular flow [RM15], Sylvester flow [Ber+18]. Invertibility is not guaranteed in general and must be checked case by case. The planar flow is invertible when $\sigma=\tanh$ and $w^\top v>-1$, but otherwise it may not be (p. 844).

#### 23.2.6 Continuous-time flows
Instead of a finite sequence of bijections, let $x(t)$, $t\in[0,T]$, solve the ODE (p. 844)
$$\frac{dx}{dt}(t)=\mathbf F(x(t),t)\tag{23.41}$$
with $\mathbf F:\mathbb R^D\times[0,T]\to\mathbb R^D$ a time-dependent vector field (the velocity of a particle). The flow $f$ maps $x_0=x(0)$ to $x(T)$. It is a well-defined bijection if the ODE solution exists and is unique for all $t\in[0,T]$. This holds if $\mathbf F(\cdot,t)$ is Lipschitz with a constant independent of $t$ (Picard–Lindelöf) (pp. 844–845):
$$\|\mathbf F(x_1,t)-\mathbf F(x_2,t)\|\le L\|x_1-x_2\|\tag{23.42}$$
- *Solving:* usually numerically. Euler's method with step $\epsilon>0$ is $x(t+\epsilon)=x(t)+\epsilon\mathbf F(x(t),t)$ (23.43). This is a residual connection with block $\epsilon\mathbf F(\cdot,t)$, i.e. a residual net with $O(T/\epsilon)$ layers. Smaller steps are more accurate but cost more. Runge–Kutta methods are alternatives (p. 845).
- *Inverse:* solve the ODE in reverse from $x(T)=x_T$ and return $x(0)$. The cost is the same in both directions (p. 845).
- *Determinant:* let $f_t$ be the flow for time $t$ and $L(t)=\log|\det\mathbf J(f_t)(x_0)|$. Then $L(0)=0$ and $L(T)$ is the quantity needed. It can be shown that (p. 845)
$$\frac{dL}{dt}(t)=\mathrm{tr}\big[\mathbf J(\mathbf F(\cdot,t))(x(t))\big]\tag{23.44}$$
$x(T)$ and $L(T)$ can be computed together by one ODE on the extended space $(x,L)$.
- *Examples:* neural ODE [Che+18c] parameterizes $\mathbf F$ by a network and uses the adjoint sensitivity method (the gradient's evolution as another ODE) to avoid backpropagating through the solver. FFJORD [Gra+19] additionally uses the Hutchinson estimator for the Jacobian trace, a stochastic but unbiased estimate (pp. 845–846). The authors call these approaches slow and complicated and point to flow matching (Section 25.4.7) as a simpler training route (p. 846).

*Intuition note:* A continuous-time flow is a residual network with infinitely many infinitesimal layers. The log-determinant is the accumulated divergence of the velocity field along the path: how much the flow expands volume near the particle.

### 23.3 Applications
- **23.3.1 Density estimation.** Flows give exact density computation and fit multimodal densities (Fig. 23.3). History as told: Gaussianization [CG00]; modern flows and the term "normalizing flows" from [TVE10; TT13]; deep density models [RA13]; NICE [DKB15] and Real NVP [DSDB17] (NVP = non-volume-preserving, i.e. Jacobian not unity); MAF improved results. Hybrid models of $p(x,y)$ [Nal+19b] allow efficient joint density, useful for anomaly detection, semi-supervised learning and selective classification. They are memory-efficient because the invertible representation is shared. Residual flows improve hybrid modelling. Flows have also been fit to embeddings for anomaly detection (p. 846).
- **23.3.2 Generative modelling.** Applied to images (GLOW, extended to video; residual flows give sharp images), audio (IAF distillation of WaveNet [Oor+18]; WaveFlow and FlowWaveNet speed up WaveNet with coupling layers), and text (a discrete flow over a vocabulary [Tra+19]; flows in the latent space of a latent-variable language model [ZR19a]) (pp. 846–847).
- **23.3.3 Inference.** Variational posteriors: [RM15] popularized flows in ML. Householder, inverse autoregressive, multiplicative and Sylvester flows were proposed for latent-variable models and Bayesian neural nets. Proposals for importance sampling (neural importance sampling, Boltzmann generators). Improving HMC by transforming variables to simpler distributions and running HMC there [Hof+19]. Simulation-based inference: train a flow on simulated data to approximate the posterior or likelihood, or guide simulations. Used in cosmology and computational neuroscience (p. 847).

## Toy example
*(Ours, not from the text.)* A 2D affine autoregressive flow, $u\sim\mathcal N(0,\mathbf I)$. Choose $\alpha_1=\ln2$, $\mu_1=1$, $\alpha_2(x_1)=(x_1-1)\ln 2$, $\mu_2(x_1)=x_1$.

Forward, with $u=(0.5,-1)$ and (23.22):
- $x_1=0.5\cdot e^{\ln2}+1=0.5\cdot2+1=2$.
- $\alpha_2(2)=\ln2$, so $x_2=-1\cdot2+2=0$. Thus $x=(2,0)$.

Inverse with (23.23), using only $x$ (both coordinates could be computed in parallel):
- $u_1=(2-1)e^{-\ln2}=0.5$.
- $u_2=(0-2)e^{-\ln2}=-1$. ✓

Log density with (23.3) and (23.24):
- $\log\mathcal N(u;0,\mathbf I)=-\log(2\pi)-\tfrac12(0.25+1)=-1.8379-0.625=-2.4629$.
- $\sum\alpha_i=\ln2+\ln2=1.3863$.
- $\log p(x)=-2.4629-1.3863=-3.8492$.

Check via (23.25):
- $x_1\sim\mathcal N(1,2^2)$: $\log p(x_1)=-\tfrac12(1.8379+1.3863)-\tfrac{1}{8}=-1.6121-0.125=-1.7371$.
- $x_2|x_1\sim\mathcal N(2,2^2)$ at $x_2=0$: $-0.9189-0.6931-\tfrac48=-2.1121$.
- Sum $=-3.8492$ ✓.

Generating $x$ from a fresh $u$ needs $x_1$ before $\alpha_2(x_1)$ can be computed: sequential. This is the MAF-type asymmetry.

## Concepts
- [[normalizing-flow]] (new) — density model $x=f(u)$ with simple base $p(u)$ and invertible $f$; sampling and exact likelihood (p. 829)
- [[change-of-variables-formula]] (new) — $p_x(x)=p_u(u)|\det\mathbf J(f)(u)|^{-1}$; log form (23.3) (p. 829)
- [[jacobian-determinant-tractability]] (new) — design target: invertible $f$ with cheap $\det\mathbf J$; composition adds log-determinants (p. 830)
- [[variational-inference-and-elbo]] — here, ELBO (23.5) maximized with a flow as $q_\theta(z|x)$ via reparameterization (p. 831)
- [[kl-divergence]] — $D_{\mathbb{KL}}(p_s\|p_t)$ used to distill WaveNet into an IAF (p. 841)
- [[coupling-layer]] (new) — transform one block conditioned on the other, which is copied; block-triangular Jacobian (p. 835)
- [[autoregressive-flow]] (new) — $x_i=h(u_i;\Theta_i(x_{1:i-1}))$; triangular Jacobian; sequential $f$, parallel $f^{-1}$ (p. 837)
- [[inverse-autoregressive-flow]] (new) — conditioner depends on previous inputs; fast $f$, slow $f^{-1}$ (p. 840)
- [[masked-autoregressive-flow]] (new) — shared masked conditioner; fast density, slow sampling (p. 840)
- [[monotonic-scalar-bijection]] (new) — affine, NLSq, monotonic MLP, integrated-positive-derivative, spline bijections (pp. 833–835)
- [[residual-flow]] (new) — $f(u)=u+\mathbf F(u)$ invertible under conditions on $\mathbf F$, e.g. $\mathbf F$ contractive (guaranteed invertible), or with a low-rank Jacobian for a cheap determinant (pp. 842–844)
- [[hutchinson-trace-estimator]] (new) — $\mathrm{tr}(\mathbf M)\approx v^\top\mathbf Mv$, $v$ zero-mean unit-covariance (p. 843)
- [[continuous-time-flow]] (new) — $f$ is the time-$T$ map of an ODE; log-determinant obeys (23.44) (p. 844)
- [[inverse-transform-sampling]] — used to argue flow expressiveness and to view autoregressive models as flows (pp. 830, 842)

## Canonical instances
- [[two-moons-spline-coupling-flow]] — masked coupling flow of rational quadratic splines fit to two moons (p. 836)
- [[cross-density-affine-ar-flow]] — one affine autoregressive layer fails on a cross-shaped density; 5 layers with reversed order succeed (p. 839)
- [[planar-flow]] — $M=1$ low-rank residual flow; $\det=1+w^\top v\sigma'(\cdot)$ (p. 844)
- [[parallel-wavenet]] — IAF distilled from WaveNet by minimizing $D_{\mathbb{KL}}(p_s\|p_t)$ (p. 841)
- [[iresnet]] — contractive residual flow with spectrally normalized convolutions (p. 842)
- [[neural-ode-ffjord]] — continuous-time flows with adjoint method; Hutchinson trace (p. 845)

## Bridges (candidates)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant.
- [same-math] Autoregressive model as one-layer flow with inverse conditional cdfs ↔ sampling: inverse-transform sampling applied conditional by conditional (p. 842).
- [same-math] Euler discretization of a neural ODE ↔ deep learning: a residual network with step-size-scaled residual blocks (p. 845).
- [structural-analogy] Composing simple bijections ↔ graphical models: building complex joints from simple conditionals (p. 830).
- [structural-analogy] IAF vs MAF speed swap ↔ ELBO vs MLE needs: fast sampling-plus-density versus fast arbitrary-point density.

## Questions this raises
- How expressive is a flow of finitely many layers with a restricted bijection family, compared with the idealised "any smooth density" argument?
- When the base and data dimension must match ($f:\mathbb R^D\to\mathbb R^D$), how do flows cope with data on low-dimensional manifolds?
- How do the biased (truncated) and unbiased (Russian-roulette) log-determinant estimators affect the training of residual flows?
- Does flow matching (Section 25.4.7, not in this unit) really replace ODE-solver training of continuous flows?

## Reading notes
- Printed page = pdf page − 34 (pdf 863 = p. 829). The last page (printed 848) is blank in this extraction.
- The Fig. 23.3 caption reads "(a) Two moons dataset. (b) Samples from a normalizing flow fit to this dataset", but the image has eight panels (a)–(h) labelled "Layer 1/8" … "Layer 8/8". The text (p. 836) says they are samples from each layer.
- Typo in source (p. 841): "an IAF $p_s$ that it trained". The text layer garbles $f^{-1}$ as $f$ near (23.34); the image shows $f^{-1}(x)$.
- Section 23.1.2.2 refers forward to Section 23.2.4.3 for sampling and density of flow posteriors. The text introduces $\ell_\theta$ in (23.6) without defining it explicitly.
- The Jacobian-determinant formula for flows is stated here for the inverse mapping $g$ in (23.4). In (23.2)–(23.3) the author uses $f$ with $|\det\mathbf J(f)|^{-1}$.
- No exercises in this unit. The chapter is written by Papamakarios and Lakshminarayanan (p. 829).
