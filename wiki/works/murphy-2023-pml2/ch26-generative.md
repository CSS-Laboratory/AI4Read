---
id: murphy-2023-pml2/ch26-generative
work: murphy-2023-pml2
unit: "26 Generative adversarial networks"
pages: 893-924
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
# Generative adversarial networks (Rosca, Mohamed, Lakshminarayanan; in Murphy 2023)

## L0 — One line
Implicit generative models have no usable likelihood, so GANs train a critic from samples to approximate a divergence or distance between data and model, and train the generator to shrink that approximation.

## L1 — The gist (≤ 120 words)
Implicit generative models can produce samples but have no computable likelihood, so maximum likelihood cannot train them. The chapter asks how to learn from samples alone. Answer: train a critic (discriminator) to approximate a divergence or distance between data and model distributions, using only sample averages, then train the generator to reduce that approximation. This gives the GAN min-max game, with several variants (class probability, f-divergence bounds, integral probability metrics, moment matching). The chapter also covers training difficulties, convergence analysis, conditional and inference-capable GANs, architectures, and applications. It matters because in practice the critic acts as a learned loss, and theory guarantees hold only under idealised assumptions.

**Prerequisites:** KL divergence; Bayes' rule for a two-class classifier; Monte Carlo averages; gradient descent; Jacobian eigenvalues (for the stability part); basic convex conjugates and kernels (for the f-divergence and MMD parts).

## L2 — Key ideas (5–10 bullets)
- An implicit model is a sampler $x=G_\theta(z)$ with no explicit likelihood, so training needs objectives that use only samples (p. 893, p. 895).
- Learning by comparison replaces an intractable divergence by an optimisation over a critic. The objective has the form $\mathbb E_{p^*}f+\mathbb E_{q_\theta}g$, estimated by Monte Carlo (p. 895–896).
- With Bernoulli log-loss the optimal critic is $D^*=p^*/(p^*+q_\theta)$, and the objective evaluated at this optimal critic equals $\mathrm{JSD}(p^*,q_\theta)-\log 2$. This gives the original GAN game (p. 897–898).
- The same recipe covers other scoring rules, lower bounds on f-divergences (f-GAN), IPMs (Wasserstein, MMD) and learned moments, each with a different critic (p. 898–902).
- Ratio-based divergences fail on non-overlapping supports, but smooth learned critics still give gradients. Generators minimise only a lower bound, so there is no guarantee the divergence falls (p. 903–904).
- Training alternates critic and generator updates. Mode collapse and mode hopping occur. Global guarantees need optimal critics and infinite capacity, while DiracGAN shows alternating gradient descent circling an equilibrium (p. 905–912).
- Conditional GANs, BiGAN/ALI inference, architecture choices (DCGAN, SAGAN, progressive growing, regularisation, scale) and applications build on the same game (p. 912–924).

## L3 — Walkthrough

### 26.1 Introduction (p. 893–894)
- **Prescribed (explicit)** models give a parametric log-likelihood $\log q_\theta(x)$. **Implicit** models define a stochastic procedure that generates data directly, natural for climate, population genetics and ecology (p. 893). Fig. 26.1: prescribed models expose a density, implicit ones only a simulator (p. 894).
- Implicit model with latent $z\in\mathbb R^m$ and deterministic $G_\theta:\mathbb R^m\to\mathbb R^d$ (p. 893):
$$x=G_\theta(z'),\quad z'\sim q(z)\tag{26.1}$$
$$q_\theta(x)=\frac{\partial}{\partial x_1}\cdots\frac{\partial}{\partial x_d}\int_{\{G_\theta(z)\le x\}}q(z)\,dz\tag{26.2}$$
- (26.2) is the derivative of a CDF. If $m=d$ and $G_\theta$ is invertible (or has easily characterised roots), it reduces to the change-of-variables rule, as in normalizing flows (p. 894).
- For deep nonlinear $G$ with $d>m$ ("generator networks", "differentiable simulators"), (26.2) is intractable and the set $\{G_\theta(z)\le x\}$ may not even be computable. With no likelihood term, learning is harder than for VAEs. This is *likelihood-free* or *simulation-based inference*; ABC (Sec. 13.6.5) is the other framework. Both compare real and simulated data (p. 894).

### 26.2 Learning by comparison (p. 894–904)
Maximum likelihood minimises $D_{\mathrm{KL}}$ between $q_\theta$ and the unknown $p^*$, but $q_\theta(x)$ cannot be evaluated. We need principles using only samples, a two-sample comparison (p. 895). Fig. 26.2 splits them into ratios (class-probability estimation, f-divergences) and differences (IPMs, moment matching).

**26.2.1 Guiding principles (p. 895–896).** Want $\mathcal D(p^*,q)$ that (1) satisfies $\arg\min_q\mathcal D(p^*,q)=p^*$, (2) can be evaluated from samples only, (3) is cheap. Many divergences satisfy (1) via
$$\mathcal D(p^*,q)\ge0;\qquad \mathcal D(p^*,q)=0\iff p^*=q\tag{26.3}$$
but KL fails (2) and Wasserstein fails (3). Remedy: a critic $D$,
$$\mathcal D(p^*,q)=\arg\max_D\mathcal F(D,p^*,q)\tag{26.4}$$
Model and critic are parametric ($\theta$, $\phi$). The generator uses the tractable approximation given by $D_\phi$. Taking $\mathcal F$ as a sum of expectations,
$$\mathcal F(D_\phi,p^*,q_\theta)=\mathbb E_{p^*(x)}f(x,\phi)+\mathbb E_{q_\theta(x)}g(x,\phi)\tag{26.5}$$
$$=\mathbb E_{p^*(x)}f(x,\phi)+\mathbb E_{q(z)}g(G_\theta(z),\phi)\tag{26.6}$$
$$\approx\frac1N\sum_{i=1}^Nf(\hat x_i,\phi)+\frac1M\sum_{i=1}^Mg(G_\theta(\hat z_i),\phi),\quad \hat x_i\sim p^*,\ \hat z_i\sim q(z)\tag{26.7}$$
Each following subsection picks $f,g$.

**26.2.2 Density ratio estimation by binary classifiers (p. 896–898).**
- Density ratio $r(x)=p^*(x)/q_\theta(x)$. The distributions are the same iff $r=1$ everywhere on the support of $q_\theta$ (p. 896). A classifier $D$ trained on $p^*$ vs $q_\theta$ samples gives
$$\frac{p^*(x)}{q_\theta(x)}=\frac{D(x)}{1-D(x)}\tag{26.8}$$
- Train $D_\phi\in[0,1]$ with any proper scoring rule (Table 26.1 lists Bernoulli, Brier, exponential, misclassification, hinge, spherical). For Bernoulli log-loss, with the two class priors equal to $\tfrac12$ (added step: this is where the $\tfrac12$'s come from):
$$V(q_\theta,p^*)=\arg\max_\phi\mathbb E_{p(x|y)p(y)}[y\log D_\phi+(1-y)\log(1-D_\phi)]\tag{26.9}$$
$$=\arg\max_\phi\tfrac12\mathbb E_{p^*}\log D_\phi(x)+\tfrac12\mathbb E_{q_\theta}\log(1-D_\phi(x))\tag{26.10}$$
(26.9) as printed has an intermediate line $\mathbb E_{p(x|y=1)p(y=1)}\log D_\phi+\mathbb E_{p(x|y=0)p(y=0)}\log(1-D_\phi)$ (p. 896).
- Optimal discriminator (p. 897):
$$\frac{p^*}{q_\theta}=\frac{D^*}{1-D^*}\implies D^*(x)=\frac{p^*(x)}{p^*(x)+q_\theta(x)}\tag{26.11}$$
- Substituting $D^*$ (using $1-\frac{p^*}{p^*+q_\theta}=\frac{q_\theta}{p^*+q_\theta}$, added step, and $\log\frac{a}{a+b}=\log\frac{a}{(a+b)/2}-\log2$):
$$V^*=\tfrac12\mathbb E_{p^*}\Big[\log\tfrac{p^*}{p^*+q_\theta}\Big]+\tfrac12\mathbb E_{q_\theta}\Big[\log\Big(1-\tfrac{p^*}{p^*+q_\theta}\Big)\Big]\tag{26.12}$$
$$=\tfrac12\mathbb E_{p^*}\Big[\log\tfrac{p^*}{(p^*+q_\theta)/2}\Big]+\tfrac12\mathbb E_{q_\theta}\Big[\log\tfrac{q_\theta}{(p^*+q_\theta)/2}\Big]-\log2\tag{26.13}$$
$$=\tfrac12D_{\mathrm{KL}}\Big(p^*\,\Big\|\,\tfrac{p^*+q_\theta}{2}\Big)+\tfrac12D_{\mathrm{KL}}\Big(q_\theta\,\Big\|\,\tfrac{p^*+q_\theta}{2}\Big)-\log2\tag{26.14}$$
$$=\mathrm{JSD}(p^*,q_\theta)-\log2\tag{26.15}$$
$$\mathrm{JSD}(p^*,q_\theta)=\tfrac12D_{\mathrm{KL}}\Big(p^*\,\Big\|\,\tfrac{p^*+q_\theta}{2}\Big)+\tfrac12D_{\mathrm{KL}}\Big(q_\theta\,\Big\|\,\tfrac{p^*+q_\theta}{2}\Big)\tag{26.16}$$
- Optimal classification thus gives a divergence computed from samples: an intractable estimation problem became an optimisation problem (p. 897). The generator minimises it:
$$\min_\theta\mathrm{JSD}(p^*,q_\theta)=\min_\theta V^*(q_\theta,p^*)+\log2=\min_\theta\tfrac12\mathbb E_{p^*}\log D^*+\tfrac12\mathbb E_{q_\theta}\log(1-D^*)+\log2\tag{26.17–26.18}$$
- Since $D^*$ is unavailable, use $D_\phi$ (p. 898):
$$\min_\theta\max_\phi\tfrac12\mathbb E_{p^*}[\log D_\phi(x)]+\tfrac12\mathbb E_{q_\theta}[\log(1-D_\phi(x))]\tag{26.19}$$
$$\min_\theta\max_\phi\tfrac12\mathbb E_{p^*}[\log D_\phi(x)]+\tfrac12\mathbb E_{q(z)}[\log(1-D_\phi(G_\theta(z)))]\tag{26.20}$$
(26.20) is the original GAN definition (p. 898).
- Other rules: Brier gives, under discriminator optimality, the Pearson $\chi^2$ divergence (LS-GAN). Hinge corresponds to total variation distance (p. 898).
- **Guarantee, with conditions:** if the discriminator is optimal and the generator has enough capacity, it will learn the data distribution (by 26.3). In practice discriminators are rarely optimal (p. 898).

*Intuition note.* A classifier that separates real from fake samples secretly estimates the density ratio. Plugging the best classifier into the log-loss yields a known divergence (JSD up to a constant), so the generator can reduce a divergence it never computes directly.

**26.2.3 Bounds on f-divergences (p. 898–900).**
- $D_f[p^*\|q_\theta]=\int q_\theta(x)f\big(\tfrac{p^*(x)}{q_\theta(x)}\big)dx$ with $f$ convex, $f(1)=0$ (26.21). Choices of $f$ give KL, reverse KL, JSD, Pearson $\chi^2$ (Table 26.2: e.g. KL $f=u\log u$, $f^\dagger=e^{u-1}$, optimal critic $1+\log r$; Pearson $f=(u-1)^2$, $f^\dagger=\tfrac14u^2+u$, critic $2(r-1)$; here $r=p^*/q_\theta$, p. 899).
- Variational form, using $f(u)=\sup_t\,ut-f^\dagger(t)$ ($f^\dagger$ = convex conjugate) with $t$ made a function $t(x)$ (p. 899):
$$D_f=\int q_\theta f\Big(\tfrac{p^*}{q_\theta}\Big)dx\tag{26.22}$$
$$=\int q_\theta(x)\sup_{t:\mathcal X\to\mathbb R}\Big[t(x)\tfrac{p^*(x)}{q_\theta(x)}-f^\dagger(t(x))\Big]dx\tag{26.23}$$
$$=\int\sup_{t:\mathcal X\to\mathbb R}p^*(x)t(x)-q_\theta(x)f^\dagger(t(x))\,dx\tag{26.24}$$
$$\ge\sup_{t\in\mathcal T}\mathbb E_{p^*}[t(x)]-\mathbb E_{q_\theta}[f^\dagger(t(x))]\tag{26.25}$$
The inequality arises because the family $\mathcal T$ (e.g. a neural network class) may not contain the true supremum. $t$ plays the critic. (26.25) has the form (26.5), so it is Monte Carlo estimable.
- f-GAN (p. 899):
$$\min_\theta D_f(p^*,q_\theta)\ge\min_\theta\max_\phi\mathbb E_{p^*}[D_\phi(x)]-\mathbb E_{q_\theta}[f^\dagger(D_\phi(x))]\tag{26.26}$$
$$=\min_\theta\max_\phi\mathbb E_{p^*}[D_\phi(x)]-\mathbb E_{q(z)}[f^\dagger(D_\phi(G_\theta(z)))]\tag{26.27}$$
- Each scoring rule corresponds to some f-divergence giving the same min-max game [RW11]. In both, the optimal critic is tied to the density ratio (p. 900).

*Intuition note.* A convex function is the upper envelope of its tangent lines. Replacing the divergence by a tangent-line (conjugate) form turns an integral over unknown densities into two sample averages. Restricting to a neural family can only lower the value.

**26.2.4 Integral probability metrics (p. 900–902).**
- Differences instead of ratios (p. 900):
$$I_{\mathcal F}(p^*,q_\theta)=\sup_{f\in\mathcal F}\big|\mathbb E_{p^*}f(x)-\mathbb E_{q_\theta}f(x)\big|\tag{26.28}$$
$f$ is a test/witness function (the critic). IPMs satisfy (26.3), are symmetric and obey the triangle inequality, but only for suitable $\mathcal F$. Counterexample: $\mathcal F=\{z\}$ with $z(x)=0$ always gives 0.
- 1-Lipschitz functions give the Wasserstein distance:
$$W_1=\sup_{\|f\|_{\rm Lip}\le1}\mathbb E_{p^*}f-\mathbb E_{q_\theta}f\tag{26.29}$$
$$\ge\max_{\phi:\|D_\phi\|_{\rm Lip}\le1}\mathbb E_{p^*}D_\phi-\mathbb E_{q_\theta}D_\phi\tag{26.30–26.31}$$
The critic must be regularised to be 1-Lipschitz (gradient penalty, spectral normalisation) (p. 900).
- WassersteinGAN (p. 901):
$$\min_\theta\max_{\phi:\|D_\phi\|_{\rm Lip}\le1}\mathbb E_{p^*}D_\phi(x)-\mathbb E_{q(z)}D_\phi(G_\theta(z))\tag{26.32–26.33}$$
- RKHS functions of norm one give MMD (26.34). Squared MMD with kernel $\mathcal K$:
$$\mathrm{MMD}^2=\mathbb E_{p^*}\mathbb E_{p^*}\mathcal K(x,x')-2\mathbb E_{p^*}\mathbb E_{q_\theta}\mathcal K(x,y)+\mathbb E_{q_\theta}\mathbb E_{q_\theta}\mathcal K(y,y')\tag{26.35}$$
and with $y=G_\theta(z)$ in (26.36). $\min_\theta\mathrm{MMD}^2$ is a generative matching network (26.37).
- A fixed kernel (e.g. RBF) may suit images poorly. For characteristic $\mathcal K$ and injective $\zeta$, $\mathcal K(\zeta(x),\zeta(x'))$ is again characteristic. To make features sensitive to differences, the kernel parameters are trained to *maximise* $\mathrm{MMD}^2$, giving a min-max game (p. 901–902):
$$\min_\theta\max_\phi\ \mathbb E_{p^*}\mathbb E_{p^*}\mathcal K(\zeta_\phi(x),\zeta_\phi(x'))-2\mathbb E_{p^*}\mathbb E_{q_\theta}\mathcal K(\zeta_\phi(x),\zeta_\phi(y))+\mathbb E_{q_\theta}\mathbb E_{q_\theta}\mathcal K(\zeta_\phi(y),\zeta_\phi(y'))\tag{26.38–26.39}$$
$\zeta_\phi$ is regularised to be injective (sometimes relaxed). Unlike Wasserstein and f-divergences, (26.39) is Monte Carlo estimable without a lower bound (p. 902).

**26.2.5 Moment matching (p. 902).**
$$\min_\theta\big\|\mathbb E_{p^*}s(x)-\mathbb E_{q_\theta}s(x)\big\|_2^2\tag{26.40}$$
with $m(\theta)=\mathbb E_{q_\theta}s(x)$ the moment function. The statistic $s$ is crucial: $s(x)=x$ matches means but not variance. The likelihood-based score $s=\nabla_x\log q_\theta(x)$ gives a consistent estimator but is unavailable for implicit models. MMD is moment matching in an RKHS feature space. Ravuri et al. use $s_\phi(x)=[\nabla_\phi D_\phi(x),h_1(x),\dots,h_n(x)]$ (critic gradients plus hidden activations). The gradients are needed for consistency, since the number of moments must exceed the number of parameters $\theta$. The activations are added because they empirically improve performance (p. 902).

**26.2.6 Ratios versus differences (p. 902–904).**
- **Commonly stated downside** of ratio-based divergences: with non-overlapping supports the ratio is $\infty$ where $p^*>0=q_\theta$ and 0 elsewhere. Then $D_{\mathrm{KL}}(p^*\|q_\theta)=\infty$ and $\mathrm{JSD}=\log2$ whatever $\theta$ is, so they cannot tell models apart (Fig. 26.4a). IPMs have smoothness built in via critic norm constraints and give useful signal (Fig. 26.3) (p. 903).
- **Author's qualification:** if the critic family (used via the bound or class-probability estimation) contains only smooth functions, it cannot represent the sharp jump from 0 to $\infty$ but can give a smooth approximation, e.g. an MLP trained with (26.25) (Fig. 26.4b). That provides a gradient while the exact KL gives zero gradient almost everywhere. So the theoretical difference is less significant in practice, since smooth critics are used (p. 903–904).
- Bounds (26.25), (26.31) are lower bounds, so the generator minimises a lower bound. Minimising gives no guarantee the divergence decreases: the right-hand side of (26.26) can fall arbitrarily without the left-hand side decreasing. This differs from the variational *upper* bound used in VAEs (p. 904).

*Intuition note.* A hard ratio between disjoint distributions is like a cliff with no slope to follow. A smooth learned critic replaces the cliff by a ramp, so the generator knows which way to move. The price is that the ramp is only a lower-bound proxy.

### 26.3 Generative adversarial networks (p. 904–912)

**26.3.1 From principles to losses (p. 904–905).**
- Many objectives are zero-sum: $\min_\theta\max_\phi V(\phi,\theta)$ (26.41). Original GAN: $V=\tfrac12\mathbb E_{p^*}\log D_\phi+\tfrac12\mathbb E_{q_\theta}\log(1-D_\phi)$ (26.42). This arises because the critic maximises an approximation to a divergence that the model minimises. It need not be so (p. 904).
- **Non-saturating loss:** instead of minimising $\mathbb E_{q_\theta}\log(1-D_\phi)$, the generator minimises $\mathbb E_{q_\theta}[-\log D_\phi(x)]$, i.e. maximises the probability of being classified real. It gives a stronger gradient when $D(G(z))$ is low (Fig. 26.5) (p. 905).
- General form (26.43): $\min_\phi L_D(\phi,\theta)$; $\min_\theta L_G(\phi,\theta)$. Zero-sum if $-L_D=L_G=V$ (p. 905). Most losses are
$$L_D=\mathbb E_{p^*}g(D_\phi(x))+\mathbb E_{q(z)}h(D_\phi(G_\theta(z)))\tag{26.44}$$
$$L_G=\mathbb E_{q(z)}l(D_\phi(G_\theta(z)))\tag{26.45}$$
Original GAN: $g=-\log t$, $h=-\log(1-t)$, $l=\log(1-t)$. Non-saturating: same $g,h$, $l=-\log t$. Wasserstein: $g=t,h=-t,l=t$. f-divergences: $g=t,h=-f^\dagger,l=f^\dagger$ (p. 905).

**26.3.2 Gradient descent (p. 905–907).**
- Ideally the critic is solved fully, $\phi^*=\arg\min_\phi L_D$, before each generator step $\nabla_\theta L_G(\phi^*,\theta)$. That is too costly, so updates alternate: a few critic steps ($K$), one generator step, each with the other player fixed (Alg. 26.1, p. 906).
- Critic gradient: $\nabla_\phi L_D=\mathbb E_{p^*}\nabla_\phi g(D_\phi(x))+\mathbb E_{q_\theta}\nabla_\phi h(D_\phi(x))$ (26.46–26.47), by backpropagation and Monte Carlo.
- Generator gradient: the order of $\nabla_\theta$ and expectation cannot be swapped under $q_\theta(x)$, but the reparameterization trick gives
$$\nabla_\theta L_G=\nabla_\theta\mathbb E_{q_\theta(x)}l(D_\phi(x))=\nabla_\theta\mathbb E_{q(z)}l(D_\phi(G_\theta(z)))=\mathbb E_{q(z)}\nabla_\theta l(D_\phi(G_\theta(z)))\tag{26.49}$$
- Alg. 26.2 (p. 907): per iteration, $K$ times sample minibatches $z_m\sim q(z)$, $x_m\sim p^*$ and take an SGD step on the critic with the average of $g(D_\phi(x_m))+h(D_\phi(G_\theta(z_m)))$. Then sample fresh $z_m$ and take an SGD step on $\theta$ with the average of $l(D_\phi(G_\theta(z_m)))$.

**26.3.3 Challenges (p. 907–908).** Dynamics are hard to analyse and stabilise. **Mode collapse:** the generator covers only some modes of the data (Fig. 26.6: 16-Gaussian mixture in 2D, model ends on a few modes). **Mode hopping:** the generator jumps between modes. The author's intuitive explanation: if the discriminator cannot separate real from generated data in a mode the generator is good at, the generator has no incentive to spread out. When the discriminator catches up, the generator can move to a new mode (p. 907). Large batches, bigger discriminators, regularisation and better optimisers have made these behaviours rarer (p. 907).

**26.3.4 Improving optimisation (p. 908).** Lower momentum than in supervised learning is preferred. Adam helps. Other methods: variance reduction, backpropagating through gradient steps, local bilinear approximation of the game. They tend to cost more computation.

**26.3.5 Convergence (p. 908–912).**
- *Global:* under optimal discriminator, infinite capacity and perfect optimisation, the generator can learn the data distribution. For (26.19), $q_\theta=p^*$ with $D_\phi=\tfrac12$ is a global Nash equilibrium: for a given $q_\theta$, $p^*/(p^*+q_\theta)$ is the best discriminator (26.11), and given it, $p^*$ minimises JSD (p. 909).
- Limits: these results ignore optimisation trajectories and finite neural capacity. GANs do not decrease a divergence at every step [Fed+18]. The focus shifts to *local Nash equilibria*: stationary points ($\nabla_\phi L_D=0$, $\nabla_\theta L_G=0$) where the Hessians $\nabla_\phi\nabla_\phi L_D$ and $\nabla_\theta\nabla_\theta L_G$ have non-negative eigenvalues. Existence of a local Nash equilibrium is not guaranteed in the general GAN game [FO20] (p. 909).
- **DiracGAN** (p. 909). $p^*$ is a Dirac mass at 0; $G_\theta(z)=\theta$; $D_\phi(x)=\phi x$; $g=h=-l$ (e.g. $l(z)=-\log(1+e^{-z})$). Then
$$L_D=-l(0)-l(\theta\phi),\qquad L_G=l(0)+l(\theta\phi)\tag{26.50–26.51}$$
with unique equilibrium $\theta=\phi=0$. Alternating gradient descent circles it rather than converging (Fig. 26.7).
- Discrete updates with rates $\alpha h,\lambda h$ (p. 910). Alternating: $\phi_t=\phi_{t-1}-\alpha h\nabla_\phi L_D(\phi_{t-1},\theta_{t-1})$ (26.52), $\theta_t=\theta_{t-1}-\lambda h\nabla_\theta L_G(\phi_t,\theta_{t-1})$ (26.53). Simultaneous: same $\phi$ update (26.54), $\theta_t=\theta_{t-1}-\lambda h\nabla_\theta L_G(\phi_{t-1},\theta_{t-1})$ (26.55). These are Euler discretisations of the ODEs
$$\dot\phi=-\nabla_\phi L_D(\phi,\theta),\qquad\dot\theta=-\nabla_\theta L_G(\phi,\theta)\tag{26.56–26.57}$$
- Stability analysis uses the game Jacobian at a stationary point:
$$J=\begin{bmatrix}-\nabla_\phi\nabla_\phi L_D&-\nabla_\theta\nabla_\phi L_D\\-\nabla_\phi\nabla_\theta L_G&-\nabla_\theta\nabla_\theta L_G\end{bmatrix}\tag{26.58}$$
All eigenvalues with negative real part: asymptotically stable. At least one with positive real part: unstable (p. 910).
- For DiracGAN at $\theta=\phi=0$:
$$J=\begin{bmatrix}0&l'(0)\\-l'(0)&0\end{bmatrix},\quad\lambda_\pm=\pm i\,l'(0)\tag{26.59}$$
Real parts are 0, so no asymptotic convergence (the author adds that linear convergence could still occur). Here convergence fails because $\theta^2+\phi^2$ is conserved (p. 911):
$$\frac{d(\theta^2+\phi^2)}{dt}=2\theta\dot\theta+2\phi\dot\phi=-2\theta l'(\theta\phi)\phi+2\phi l'(\theta\phi)\theta=0$$
- Continuous-time stability analysis has been used to show explicit regularisation can help. For simultaneous gradient descent, [MNG17b] prove under certain conditions convergence to a local Nash equilibrium, with results depending on the learning rate $h$ (via iterates $F^k(x)$, $F(x)=x+hG(x)$) (p. 911).
- Both approaches leave a gap to practice (alternating descent, Adam) and can disagree: with a large enough learning rate, simultaneous descent and the continuous dynamics behave differently on DiracGAN (Fig. 26.8). The discretisation error makes the continuous analysis reach the wrong conclusion about DiracGAN [Ros+21]. This motivates higher-order integrators such as RungeKutta4 (p. 911–912).
- Convergence to an equilibrium does not ensure a good fit to the data distribution. Equilibria may not capture it, so convergence analysis must be complemented by work on the learned distribution (p. 912).

*Intuition note.* In DiracGAN the two players chase each other round an equilibrium, like a cat and mouse, and the continuous-time game never shrinks the radius. Taking discrete steps changes the picture, so the numerical method is part of the story, not only the loss.

### 26.4 Conditional GANs (p. 912–913)
- Needs paired data $\mathcal D=\{(x_n,y_n)\}$; $y$ may be discrete (label) or continuous (embedding). It is important for the critic to penalise a generator whose samples are realistic but ignore $y$ (p. 912).
- Giving $y$ to both players (p. 912):
$$\min_\theta\max_\phi\tfrac12\mathbb E_{p(y)}\mathbb E_{p^*(x|y)}[\log D_\phi(x,y)]+\tfrac12\mathbb E_{p(y)}\mathbb E_{q_\theta(x|y)}[\log(1-D_\phi(x,y))]\tag{26.60}$$
and for latent-variable generators $G_\theta(z,y)$ in (26.61).
- For discrete labels with $K$ classes, add a classification loss with a critic that also classifies (data and samples), where $\mathcal L$ is the objective (26.61):
$$\mathcal L_c=-\big[\tfrac12\mathbb E_{p(y)}\mathbb E_{p^*(x|y)}\log D_\phi(y|x)+\tfrac12\mathbb E_{p(y)}\mathbb E_{q_\theta(x|y)}\log D_\phi(y|x)\big]\tag{26.62}$$
Both players want to minimise $\mathcal L_c$, so: $\max_\phi\mathcal L-\mathcal L_c$ and $\min_\theta\mathcal L+\mathcal L_c$ (26.63) (p. 913). In practice one critic is used for both tasks.
- The latent variable controls variability inside the mode chosen by $y$. Later work supplies $y$ at several layers or uses a projection discriminator (p. 913).

### 26.5 Inference with GANs (p. 913–914)
GANs define no inference procedure for $p(z|x)$. Options include hybrids with VAEs and inference methods for implicit models (p. 913). **BiGAN/ALI** trains an encoder $E_\zeta:x\mapsto z$ with a discriminator that sees pairs: $(x,E_\zeta(x))$, $x\sim p^*$, as real and $(G_\theta(z),z)$, $z\sim q(z)$, as fake (Fig. 26.9). This matches joint distributions, so $q_\theta(x)$ should learn $p^*(x)$ and $p_\zeta(z|x)$ should learn $q_\theta(z|x)=q_\theta(x,z)/q_\theta(x)\propto q_\theta(x|z)q(z)$. No reconstruction loss is needed, yet under global optimality encoder and generator are inverses (p. 914).

### 26.6 Neural architectures (p. 914–918)
- **26.6.1 Critic design.** Since the critic is rarely optimal, GANs do not minimise a divergence in practice. The critic acts as a *learned loss function* that changes every time it is updated, unlike maximum likelihood, whose loss stays fixed. Convolutional critics for images penalise blur and encourage sharp edges. Critic architecture and regularisation affect the generator's gradients and have been main drivers of improvement (p. 914).
- **26.6.2 DCGAN** (Figs. 26.10–26.11): convolutional generator and critic, BatchNorm in both, strided convolutions instead of pooling, ReLU in the generator, LeakyReLU in the discriminator. Residual convolutions became standard; recurrent nets are used for sequences (p. 915).
- **26.6.3 SAGAN (self-attention).** Gives both players a global view of a layer. For features $h\in\mathbb R^{C\times N}$ (p. 916): $f=W_fh$, $g=W_gh$ with $W_f,W_g\in\mathbb R^{C'\times C}$, $C'\le C$; $S=f^Tg\in\mathbb R^{N\times N}$; $\beta$ = row-wise softmax of $S$; $o=W_o(W_hh)\beta^T\in\mathbb R^{C\times N}$ with $W_h\in\mathbb R^{C'\times C}$, $W_o\in\mathbb R^{C\times C'}$; output $y=\gamma o+h$, $\gamma\in\mathbb R$ learned. Because $\gamma$ can be learned to ignore attention, adding it does not restrict the model class. Each layer adds 4 matrices; more parameters has been observed to help (p. 916).
- **26.6.4 Progressive generation.** LapGAN: upsample a low-resolution sample, add a residual from a conditional generator, repeat; separate generator and critic per block (Fig. 26.13). ProgressiveGAN: lower-resolution networks are "grown" by adding layers. A residual connection to the upscaled lower sample is annealed from 0 to 1 during training (Fig. 26.14) (p. 916–917).
- **26.6.5 Regularisation.** Justified theoretically (tied to convergence analysis), empirically and as protection against overfitting. Methods: input noise, hidden-feature noise, BatchNorm, dropout in the discriminator, spectral normalisation, gradient penalties $\|\nabla_xD_\phi(x)\|^2$. Too much regularisation can make training stable but reduce performance (p. 918).
- **26.6.6 Scale.** BigGAN, StyleGAN and alias-free GAN combine large residual nets, self-attention, spectral normalisation, BatchNorm in the generator and large batches. Losses, parameterisation and optimiser must be viewed collectively (p. 918).

### 26.7 Applications (p. 918–924)
- **Images (p. 918–921).** Fig. 26.15 shows face quality progress 2014–2018. Risks (synthetic media, deep fakes) are noted (p. 918). *Conditional:* BigGAN (class-conditional ImageNet); StyleGAN (style vector, style mixing, p. 919). *Paired translation:* pix2pix, a conditional GAN with U-net generator, instance normalisation, and a patchGAN discriminator that classifies local patches (faster, denser feedback) (p. 919–920). *Unpaired translation:* ill-posed, since many joints share the same marginals $p(x),p(y)$. CycleGAN adds constraints with $G:\mathcal X\to\mathcal Y$, $F:\mathcal Y\to\mathcal X$ (p. 920–921):
$$\mathcal L_{\rm cycle}=\mathbb E_{p(x)}\|F(G(x))-x\|_1+\mathbb E_{p(y)}\|G(F(y))-y\|_1\tag{26.64}$$
$$\mathcal L_{\rm identity}=\mathbb E_{p(x)}\|x-F(x)\|_1+\mathbb E_{p(y)}\|y-G(y)\|_1\tag{26.65}$$
$$\mathcal L=\mathcal L_{\rm GAN}+\lambda_1\mathcal L_{\rm cycle}+\lambda_2\mathcal L_{\rm identity}\tag{26.66}$$
with discriminators $D_X,D_Y$ for the GAN term (Fig. 26.17).
- **Video (p. 921–922).** Spatio-temporal consistency comes from a discriminator seeing ordered sequences. A second discriminator can check frames; generators have recurrent parts.
- **Audio (p. 922).** GANs offer parallel, faster generation than autoregressive WaveNet/WaveRNN (GANSynth, WaveGAN, GAN-TTS). GAN-TTS matches the best autoregressive models on mean opinion scores.
- **Text (p. 922–923).** Discrete outputs mean GAN text models are explicit and the reparameterization trick (26.49) is unavailable. The score function estimator has high variance, so Sequence GAN, MaliGAN and RankGAN pre-train by maximum likelihood and fine-tune briefly, staying close to the maximum-likelihood solution. ScratchGAN uses large batches and discriminator regularisation. Another model avoids the score function via continuous relaxations and curriculum learning.
- **Imitation learning (p. 923).** GAIL learns a stochastic-policy generator and a discriminator acting as reward; it extends to other f-divergences (f-GAIL learns the divergence).
- **Domain adaptation (p. 924).** Pixel-level (pix2pix, CycleGAN) and feature-level (domain-adversarial training, ADDA; CyCADA adds cycle and semantic consistency).
- **Art and design (p. 924).** Aim is appealing output rather than generalisation; examples in style transfer, fashion, music, voice, dance, typography.

## Toy example (ours, not from the text)
**A. Optimal critic and the JSD identity.** Two outcomes $\{a,b\}$ with $p^*=(0.8,0.2)$, $q_\theta=(0.4,0.6)$. By (26.11), $D^*(a)=0.8/1.2=2/3$ and $D^*(b)=0.2/0.8=0.25$.
- $\mathbb E_{p^*}\ln D^*=0.8\ln(2/3)+0.2\ln(0.25)=0.8(-0.4055)+0.2(-1.3863)=-0.6016$.
- $\mathbb E_{q_\theta}\ln(1-D^*)=0.4\ln(1/3)+0.6\ln(0.75)=0.4(-1.0986)+0.6(-0.2877)=-0.6121$.
- $V^*=\tfrac12(-0.6016-0.6121)=-0.6068$.
- Check with (26.15). The mixture is $m=(0.6,0.4)$. $D_{\mathrm{KL}}(p^*\|m)=0.8\ln\frac{0.8}{0.6}+0.2\ln\frac{0.2}{0.4}=0.2301-0.1386=0.0915$. $D_{\mathrm{KL}}(q_\theta\|m)=0.4\ln\frac{0.4}{0.6}+0.6\ln\frac{0.6}{0.4}=0.2(0.4055)=0.0811$. So $\mathrm{JSD}=\tfrac12(0.0915+0.0811)=0.0863$ and $\mathrm{JSD}-\ln2=0.0863-0.6931=-0.6068$. ✓.
- Non-overlap: on three outcomes take $p^*=(1,0,0)$, $q_1=(0,1,0)$, $q_2=(0,0,1)$. Each mixture puts 0.5 on two points, so each KL term is $\ln2$ and $\mathrm{JSD}=\ln 2=0.6931$ for both $q_1$ and $q_2$. The divergence cannot tell them apart.

**B. DiracGAN-style cycling.** Take $l(z)=z$ (our choice; $l'(0)=1$). Then $\dot\phi=\theta$, $\dot\theta=-\phi$ and $\theta^2+\phi^2$ is conserved. Simultaneous Euler with $h=0.1$ from $(\theta,\phi)=(1,0)$: $\phi_1=0+0.1\cdot1=0.1$, $\theta_1=1-0.1\cdot0=1$, so $\theta_1^2+\phi_1^2=1.01$. Next: $\phi_2=0.1+0.1\cdot1=0.2$, $\theta_2=1-0.1\cdot0.1=0.99$, so the sum is $0.0400+0.9801=1.0201$. In general $(\theta',\phi')=(\theta-h\phi,\phi+h\theta)$ gives $\theta'^2+\phi'^2=(1+h^2)(\theta^2+\phi^2)$ (added step). The discrete radius grows while the continuous one is constant, a small instance of discretisation error.

## Concepts
- [[implicit-generative-model]] (new) — sampler $x=G_\theta(z)$ whose density (26.2) is defined but not evaluable (p. 893)
- [[likelihood-free-inference]] (new) — learning when the likelihood cannot be evaluated; also called simulation-based inference; ABC is the other framework (p. 894)
- [[gan]] (new) — generator and critic trained in a game; critic approximates a divergence/distance, generator minimises it (p. 898)
- [[proper-scoring-rule]] (new) — classification loss whose optimal discriminator relates to the density ratio; Table 26.1 (p. 896–897)
- [[density-ratio-estimation]] (new) — get $p^*/q_\theta=D/(1-D)$ from a real-vs-fake classifier (p. 896)
- [[jensen-shannon-divergence]] (new) — (26.16); the optimal-critic value of the original GAN loss is $\mathrm{JSD}-\log2$ (p. 897)
- [[f-divergence]] (new) — $\int q f(p/q)$, convex $f$, $f(1)=0$; lower-bounded through convex conjugates (p. 898–899)
- [[kl-divergence]] — reused id; here infinite for non-overlapping supports (p. 903)
- [[integral-probability-metric]] (new) — sup of mean differences over a function class (26.28) (p. 900)
- [[wasserstein-distance-mmd]] (new) — IPMs from 1-Lipschitz functions (26.29) and unit-norm RKHS functions (26.34) (p. 900–901)
- [[moment-matching]] (new) — match expectations of test statistics $s$ (26.40) (p. 902)
- [[nonsaturating-loss]] (new) — generator minimises $-\log D(G(z))$, stronger gradients early (p. 905)
- [[reparameterization-gradient]] (new) — move $\nabla_\theta$ inside via $x=G_\theta(z)$ (26.49) (p. 906–907)
- [[mode-collapse]] (new) — generator misses modes of the data; mode hopping is its moving variant (p. 907)
- [[nash-equilibrium-gan]] (new) — stationary point where each player's Hessian has non-negative eigenvalues (local); global one at $q=p^*$, $D=\tfrac12$ (p. 909)
- [[learned-loss-function]] (new) — in practice the critic is a changing loss for the generator (p. 914)
- [[cycle-consistency]] (new) — require $F(G(x))=x$, $G(F(y))=y$ for unpaired translation (p. 920)
- [[monte-carlo-integration]] — reused id; the GAN objectives discussed are estimated by sample averages (26.7) (p. 896)

## Canonical instances
- [[original-gan-minmax]] — Bernoulli-loss game (26.20) (p. 898)
- [[f-gan]] — f-divergence lower bound game (26.27) (p. 899)
- [[wasserstein-gan]] — Lipschitz critic game (26.33) (p. 901)
- [[ls-gan-hinge-gan]] — Brier and hinge rules as GAN losses (p. 898)
- [[dirac-gan]] — GAN with one scalar parameter per player ($\theta$, $\phi$) that cycles under alternating descent (p. 909–911)
- [[gaussian-mixture-16-modes]] — mode collapse demo (Fig. 26.6) (p. 908)
- [[non-overlapping-support-example]] — KL fails, smooth critic works (Fig. 26.4) (p. 903)
- [[bigan-ali]] — adversarial encoder-generator joint matching (p. 913–914)
- [[dcgan-sagan-progressivegan]] — architecture milestones (p. 915–917)
- [[cyclegan-pix2pix]] — unpaired/paired image translation (p. 919–921)
- [[gail]] — GAN for imitation learning (p. 923)

## Bridges (candidates)
- [same-math] Optimal discriminator $D^*=p^*/(p^*+q_\theta)$ ↔ Bayes' theorem: posterior class probability with equal class priors $\tfrac12$.
- [structural-analogy] f-GAN lower bound (26.25) ↔ variational inference: both replace an intractable divergence by an optimised bound. The chapter notes the generator uses a *lower* bound, unlike the VAE's upper bound (p. 904).
- [structural-analogy] ABC ↔ GAN: both learn implicit models by comparing real and simulated data (p. 894).
- [same-math] MMD with learned kernel ↔ kernel two-sample testing: the same squared-MMD statistic (26.35).
- [structural-analogy] GAN training ↔ game theory/dynamical systems: Nash equilibria and Jacobian eigenvalues, as in the DiracGAN analysis.
- [structural-analogy] Score-function estimator for text GANs ↔ REINFORCE-style gradient estimators for discrete variables, also relevant to GAIL (p. 923).

## Questions this raises
- When the critic is far from optimal, what objective is the generator really minimising, and can that be characterised?
- Can a method keep the sample-only property but give an *upper* bound on the divergence, so progress is guaranteed?
- Which equilibria of the GAN game fit the data distribution poorly, and how do gradient dynamics select among them?
- How can inference methods such as BiGAN be evaluated against explicit posteriors, given the chapter says GANs have no built-in inference?

## Reading notes
- Printed page = pdf − 34 (pdf 927 = printed 893). Footer: "Online version. December 10, 2025"; CC-BY-NC-ND. The chapter's authors are Rosca, Mohamed, Lakshminarayanan.
- Source misprints seen in page images: (26.9) and (26.10) write "arg max" on the left although $V$ is then used as a value; (26.48) lacks $\nabla_\theta$ on the left side ($L_G=\nabla_\theta\mathbb E\ldots$); Alg. 26.2 line 6 has an extra $\nabla_\phi$ inside the sum; in Sec. 26.5 the identities are written $E_\theta(G_\zeta(z))=z$ with swapped subscripts (encoder is $E_\zeta$, generator $G_\theta$); (26.38) writes $p_{\mathcal D}$ where $p^*$ is meant; "RHKS", "equilibruim", "adversarialy" appear.
- Possible sign inconsistency, as printed: for Wasserstein and f-divergences the listed $g,h,l$ (p. 905), used with $L_D$ *minimised*, have the opposite sign to the critic maximisation in (26.27) and (26.33). Likewise "$-L_D=L_G=V$" appears, with the $g,h,l$ listed on p. 905, to hold only up to terms not involving $\theta$ (and, for the original GAN, the factor $\tfrac12$ in (26.42)). Treat them as informal conventions.
- Table 26.1 and Table 26.2 were checked in the images. Only the names and the Bernoulli entry of Table 26.1 are used above.
- Many cited works appear only as bracketed keys; no bibliography is in these pages. No exercises in this unit.
