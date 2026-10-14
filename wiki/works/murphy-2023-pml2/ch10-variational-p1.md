---
id: murphy-2023-pml2/ch10-variational-p1
work: murphy-2023-pml2
unit: "10 Variational inference (part 1/2): §10.1 Introduction, §10.2 Gradient-based VI up to the start of §10.2.3.1"
pages: 439–454
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Variational inference: objective, forms of q, and gradient-based VI

## L0 — One line
Variational inference turns intractable posterior inference into optimization: maximize the ELBO, a lower bound on log evidence, over a family of simple distributions q, using reparameterized gradients, minibatches and inference networks.

## L1 — The gist (≤ 120 words)
The exact posterior p(z|x) needs the intractable constant p(x). Variational inference (VI) instead picks a family q_ψ(z) and minimizes KL(q ‖ p(z|x)). This is equivalent to maximizing the evidence lower bound (ELBO), which can be computed without p(x). The chapter shows two readings of the ELBO, different choices of q (fixed-form or mean field), parameter learning (variational EM, empirical Bayes), scaling (SVI, amortization), and gradient estimators. The reparameterization trick lets gradients flow through sampled continuous z. ADVI extends it to constrained parameters. Blackbox VI, based on REINFORCE, is introduced where this part ends. This matters because it makes Bayesian-style inference scale to large models and datasets.

**Prerequisites:** KL divergence, entropy, Gaussian densities, change of variables with Jacobians, gradients and SGD, Monte Carlo averages, basic latent-variable models (e.g., a Gaussian mixture).

## L2 — Key ideas (5–10 bullets)
- VI replaces posterior computation with $\min_\psi D_{KL}(q_\psi \,\|\, p(z|x))$. The intractable $\log p(x)$ is constant in ψ and is dropped, leaving the loss $\mathcal L$ (p. 439).
- The same objective is read two ways: variational free energy (expected energy − entropy) and the ELBO (expected log joint + entropy, or expected log likelihood − KL to prior) (pp. 440–441).
- Fixed-form VI picks a family such as a Gaussian. Mean-field (free-form) VI assumes q factorizes. A diagonal Gaussian is over-confident; low-rank-plus-diagonal is much closer to the exact posterior in the 2D example (pp. 441–442).
- The ELBO also gives a lower bound on log p(D|θ). Maximizing it over ψ and θ gives variational EM (alternate maximizing over ψ in an E step and over θ in an M step); with prior hyper-parameters ξ, maximizing over ψ and ξ is a variational version of empirical Bayes (estimating ξ by maximizing log p(D|ξ)) (pp. 442–444).
- SVI uses minibatches (scaled by N/B) for scale. Amortized VI predicts local variational parameters with an inference network, at the risk of an "amortization gap" (a suboptimal choice of the local variational parameters) (pp. 444–445).
- The gradient wrt θ is easy. The gradient wrt ϕ is not, because ϕ defines the expectation (pp. 445–446).
- The reparameterization trick writes z = g(ϕ, x, ε) with ε independent of ϕ, so gradients pass through z. The transformation is designed so that the Jacobian determinant in the log-density is tractable (pp. 446–449).
- ADVI maps constrained parameters to ℝ^D by a bijection and uses a Gaussian in the unconstrained space (pp. 452–453).
- Blackbox VI assumes only that the ELBO integrand can be evaluated pointwise (no gradients of it are assumed) and uses the score-function (REINFORCE) estimator, which writes the ELBO gradient as an expectation of the integrand times $\nabla_\psi\log q$ (p. 454).

## L3 — Walkthrough

### 10.1.1 The variational objective (p. 439)
Setting: latent variables z, known x, fixed parameters θ. Prior $p_\theta(z)$, likelihood $p_\theta(x|z)$, posterior $p_\theta(z|x)=p_\theta(x,z)/p_\theta(x)$. The constant $p_\theta(x)=\int p_\theta(x,z)dz$ is assumed intractable. We seek q minimizing

$$q=\arg\min_{q\in\mathcal Q} D_{KL}(q(z)\,\|\,p_\theta(z|x)) \tag{10.1}$$

Minimizing over functions is called a *variational method*. In practice $q_\psi$ has *variational parameters* ψ (p. 439):

$$\psi^*=\arg\min_\psi D_{KL}(q_\psi(z)\,\|\,p_\theta(z|x)) \tag{10.2}$$
$$=\arg\min_\psi \mathbb E_{q_\psi}\Big[\log q_\psi(z)-\log\frac{p_\theta(x|z)p_\theta(z)}{p_\theta(x)}\Big] \tag{10.3}$$
$$=\arg\min_\psi \underbrace{\mathbb E_{q_\psi}[\log q_\psi(z)-\log p_\theta(x|z)-\log p_\theta(z)]}_{\mathcal L(\theta,\psi|x)}+\log p_\theta(x) \tag{10.4}$$

$\log p_\theta(x)$ does not depend on ψ, so it is dropped:

$$\mathcal L(\theta,\psi|x)=\mathbb E_{q_\psi}[-\log p_\theta(x,z)+\log q_\psi(z)] \tag{10.5}$$

Figure 10.1: the true posterior is assumed to lie outside the family $\mathcal Q$. Optimization starts from a random $\psi^{init}$ and ends at the closest point $\psi^*$ in KL (p. 440).

**10.1.1.1 Physics view (p. 440).** Define energy $\mathcal E_\theta(z)=-\log p_\theta(z,x)$. Then

$$\mathcal L=\mathbb E_{q_\psi}[\mathcal E_\theta(z)]-\mathbb H(q_\psi)=\text{expected energy}-\text{entropy} \tag{10.6}$$

(entropy $\mathbb H$ measures how spread out q is). This is the *variational free energy* (VFE). It upper-bounds the free energy $-\log p_\theta(x)$:

$$D_{KL}(q_\psi\|p_\theta(z|x))=\mathcal L+\log p_\theta(x)\ge0 \tag{10.7}$$
$$\mathcal L(\theta,\psi|x)\ge-\log p_\theta(x) \tag{10.8}$$

VI is equivalent to minimizing the VFE. If the bound reaches $-\log p_\theta(x)$, the KL is 0 and the approximate posterior is exact (p. 440).

**10.1.1.2 Statistics view (pp. 440–441).** The negative VFE is the *ELBO* (written Ł so that Ł is maximized while $\mathcal L$ is minimized):

$$Ł(\theta,\psi|x)\triangleq\mathbb E_{q_\psi}[\log p_\theta(x,z)-\log q_\psi(z)] \tag{10.9}$$
$$Ł\le\log p_\theta(x) \tag{10.10}$$

The log p(x) is the "evidence". Maximizing the ELBO wrt ψ minimizes the KL, because log p(x) is constant in ψ. Rewrites:

$$Ł=\mathbb E_{q_\psi}[\log p_\theta(x,z)]+\mathbb H(q_\psi)=\text{expected log joint}+\text{entropy} \tag{10.11–10.12}$$

The entropy term encourages q to be maximum entropy; the first term encourages a joint MAP configuration (p. 441).

$$Ł=\mathbb E_{q_\psi}[\log p_\theta(x|z)+\log p_\theta(z)-\log q_\psi(z)] \tag{10.13}$$
$$=\mathbb E_{q_\psi}[\log p_\theta(x|z)]-D_{KL}(q_\psi\|p_\theta(z)) \tag{10.14}$$

That is, expected log likelihood − KL from posterior to prior (10.15). The KL acts as a regularizer that keeps q from moving too far from the prior (p. 441).

*Intuition note.* The loss never needs p(x). The gap between the ELBO and log p(x) is exactly the KL we care about, so pushing the bound up pulls q toward the posterior.

### 10.1.2 Form of the variational posterior (pp. 441–442)
- **Fixed-form VI:** choose a convenient form (e.g., multivariate Gaussian) and optimize the ELBO by gradient methods (§10.2).
- **Mean field (free-form VI):** assume $q_\psi(z)=\prod_{j=1}^J q_j(z_j)$ (10.16). No functional form is specified for each $q_j$. The optimal form is derived by maximizing the ELBO over one group at a time (coordinate ascent) (§10.3).

Example: z is the 2D mean of a Gaussian. Prior $\mathcal N(z|\breve m,\breve V)$, likelihood $p(D|z)=\prod_n\mathcal N(x_n|z,\Sigma)\propto\mathcal N(\bar x|z,\tfrac1N\Sigma)$ (10.17). The exact posterior is Gaussian. Figure 10.2 compares three Gaussian q's:
- Full covariance: matches the exact posterior, but is intractable in high dimensions.
- Diagonal (mean field): over-confident, a known VI flaw linked to the mode-seeking nature of minimizing $D_{KL}(q\|p)$.
- Rank-1 plus diagonal: much better, and computable efficiently (§10.2.1.3).

### 10.1.3 Parameter estimation by variational EM (pp. 442–444)
Parameters θ can be estimated by maximizing $\log p(D|\theta)=\sum_n\log p(x_n|\theta)$ (10.18), generally intractable.

**10.1.3.1 MLE for latent variable models.** Model $p(D,z_{1:N}|\theta)=\prod_n p(z_n|\theta)p(x_n|z_n,\theta)$ (10.19). The local log marginal likelihood $\log p(x_n|\theta)=\log\int p(x_n|z_n,\theta)p(z_n|\theta)dz_n$ (10.20) is usually intractable. The ELBO bounds it:

$$Ł(\theta,\psi_n|x_n)\le\log p(x_n|\theta) \tag{10.21}$$
$$Ł(\theta,\psi_{1:N}|D)\triangleq\sum_{n=1}^N Ł(\theta,\psi_n|x_n)\le\log p(D|\theta) \tag{10.22}$$

This is *variational EM*: the E step maximizes the ELBO wrt $\{\psi_n\}$, giving $q_{\psi_n}(z_n)$. The M step maximizes it wrt θ using the new $\psi_n$ (p. 443).

**10.1.3.2 Empirical Bayes for fully observed models.** Model $p(D,\theta|\xi)=p(\theta|\xi)\prod_n p(x_n|\theta)$ (10.23); posterior $p(\theta|D,\xi)=p(D|\theta)p(\theta|\xi)/p(D|\xi)$ (10.24). If hyper-parameters ξ are unknown, estimate $\hat\xi=\arg\max_\xi\log p(D|\xi)$ (10.25). With θ as the latent variable and D as the observation, variational EM gives

$$\log p(D|\xi)\ge Ł(\xi,\psi|D)=\mathbb E_{q_\psi(\theta)}\Big[\sum_n\log p(x_n|\theta)\Big]-D_{KL}(q_\psi(\theta)\|p(\theta|\xi)) \tag{10.26}$$

optimized wrt ψ and ξ (p. 444). If ξ is fixed, only ψ is optimized to get $q_\psi(\theta|D)$; this is *variational Bayes* (§10.3.3).

### 10.1.4 Stochastic VI (p. 444)
The dataset ELBO is a sum over N examples and can be slow. With a random minibatch $\mathcal B$ of size B, the approximation is unbiased and fast:

$$Ł(\theta,\psi_{1:N}|D)\approx\frac NB\sum_{x_n\in\mathcal B}\mathbb E_{q_{\psi_n}}[\log p_\theta(x_n|z_n)+\log p_\theta(z_n)-\log q_{\psi_n}(z_n)] \tag{10.27}$$

Used inside SGD, this is *stochastic VI* (SVI), which lets VI scale to large datasets.

### 10.1.5 Amortized VI (pp. 444–445)
In SVI each minibatch example needs its own inner optimization of $\psi_n$, which can be slow. *Amortized VI* trains an *inference (recognition) network* $\psi_n=f^{inf}_\phi(x_n)$ shared across examples, so per-example cost falls. Write $q(z_n|\psi_n)=q_\phi(z_n|x_n)$ (10.28). The ELBO is

$$Ł(\theta,\phi|D)=\sum_n\mathbb E_{q_\phi(z_n|x_n)}[\log p_\theta(x_n,z_n)-\log q_\phi(z_n|x_n)] \tag{10.29}$$

and with minibatch size 1, $Ł\approx N\,\mathbb E_{q_\phi}[\log p_\theta(x_n,z_n)-\log q_\phi(z_n|x_n)]$ (10.30). Algorithm 10.1 (amortized stochastic variational EM): initialize θ, ϕ; repeat: sample $x_n\sim p_D$; E step $\phi=\arg\max_\phi Ł(\theta,\phi|x_n)$; M step $\theta=\arg\max_\theta Ł(\theta,\phi|x_n)$; until converged (p. 445). The θ step is usually a gradient update. The ϕ step is trickier, because ϕ defines the expectation, so we cannot necessarily push the gradient inside.

### 10.1.6 Semi-amortized inference (p. 445)
Amortized SVI is widely used (VAEs, topic models, probabilistic programming, CRFs). An inference network can give a suboptimal $\psi_n$: the *amortization gap*. Using the network to warm-start an optimizer for $\psi_n$ closes the gap (*semi-amortized VI*). Alternatively, the network can act as a proposal: with importance sampling this gives the IWAE bound (§10.5.1); with Metropolis–Hastings, a VI–MCMC hybrid (§10.4.5).

### 10.2 Gradient-based VI (pp. 445–446)
Choose a convenient $q_\psi$ (Gaussian for continuous z, product of categoricals for discrete z) and optimize the ELBO by gradients. The gradient wrt generative parameters θ is easy, since gradients go inside the expectation and one sample suffices:

$$\nabla_\theta Ł=\nabla_\theta\mathbb E_{q_\phi}[\log p_\theta(x,z)-\log q_\phi(z|x)]=\mathbb E_{q_\phi}[\nabla_\theta\{\cdots\}]\approx\nabla_\theta\log p_\theta(x,z^s) \tag{10.31–10.33}$$

with $z^s\sim q_\phi(z|x)$ (the $\log q_\phi$ term drops since it does not depend on θ, (added step)). This is unbiased, so SGD applies. The gradient wrt the inference parameters ϕ is harder, because

$$\nabla_\phi\mathbb E_{q_\phi}[\cdots]\neq\mathbb E_{q_\phi}[\nabla_\phi\{\cdots\}] \tag{10.34–10.35}$$

The reparameterization trick (§10.2.1) often fixes this. If not, use blackbox VI (§10.2.3).

### 10.2.1 Reparameterized VI (pp. 446–449)
For continuous z, write z as a differentiable, invertible transform of noise ε with a distribution not depending on ϕ (Figure 10.4):

$$z=g(\phi,x,\epsilon),\ \epsilon\sim p(\epsilon) \tag{10.36}$$

Example: $z\sim\mathcal N(\mu,\mathrm{diag}(\sigma))\iff z=\mu+\epsilon\odot\sigma,\ \epsilon\sim\mathcal N(0,I)$ (10.37). Then, with $f_{\theta,\phi}(z)=\log p_\theta(x,z)-\log q_\phi(z|x)$ (10.39):

$$\mathbb E_{q_\phi(z|x)}[f(z)]=\mathbb E_{p(\epsilon)}[f(z)]\ \text{s.t. }z=g(\phi,x,\epsilon) \tag{10.38}$$
$$\nabla_\phi\mathbb E_{q_\phi}[f(z)]=\nabla_\phi\mathbb E_{p(\epsilon)}[f(z)]=\mathbb E_{p(\epsilon)}[\nabla_\phi f(z)] \tag{10.40}$$

This can be approximated with a single Monte Carlo sample and backpropagated through f. It is called *reparameterized VI* (RVI). Evaluating $\log q_\phi$ needs the change of variables formula, where $\partial z/\partial\epsilon$ is the Jacobian (matrix of partial derivatives $\partial z_i/\partial\epsilon_j$, 10.42):

$$\log q_\phi(z|x)=\log p(\epsilon)-\log\Big|\det\Big(\frac{\partial z}{\partial\epsilon}\Big)\Big| \tag{10.41}$$

g is designed so that this Jacobian is tractable.

*Intuition note.* Moving the randomness into ε turns "gradient of an expectation under a ϕ-dependent distribution" into "expectation of a gradient". ϕ then only enters through a deterministic function.

**10.2.1.1 Diagonal Gaussian (mean field) (p. 447–448).** $\epsilon\sim\mathcal N(0,I)$, $z=\mu+\sigma\odot\epsilon$ (10.43–10.44), with $(\mu,\log\sigma)=f^{inf}_\phi(x)$ (10.45). The ELBO integrand is $f(z)=\log p_\theta(x|z)+\log p_\theta(z)-\log q_\phi(z|x)$ (10.46). The likelihood term is evaluated by plugging in z. With Jacobian $\mathrm{diag}(\sigma)$:

$$\log q_\phi(z|x)=\sum_{k=1}^K[\log\mathcal N(\epsilon_k|0,1)-\log\sigma_k]=-\sum_k\Big[\tfrac12\log(2\pi)+\tfrac12\epsilon_k^2+\log\sigma_k\Big] \tag{10.47}$$

For the prior, use $z=0+1\odot\epsilon$ (identity Jacobian): $\log p(z)=-\sum_k[\tfrac12z_k^2+\tfrac12\log(2\pi)]$ (10.48). Alternative objective:

$$f'(z)=\log p_\theta(x|z)+D_{KL}(q_\phi(Z|x)\|p_\theta(Z)) \tag{10.49}$$

(as printed, the sign of the KL term is "+"). For prior $\mathcal N(0,I)$ and posterior $\mathcal N(\mu,\mathrm{diag}(\sigma))$ the KL is closed form (using Eq. 5.78 of the book):

$$D_{KL}(q\|p)=\sum_{k=1}^K\Big[-\log\sigma_k+\tfrac12\sigma_k^2+\tfrac12\mu_k^2\Big] \tag{10.50}$$

$f'$ is often lower variance than f since the KL is analytic, but it is harder to generalize beyond Gaussians (p. 448).

**10.2.1.2 Full covariance (pp. 448–449).** Cholesky decomposition $\Sigma=LL^T$ (L lower triangular, non-zero diagonal): $\epsilon\sim\mathcal N(0,I)$, $z=\mu+L\epsilon$ (10.51–10.52). The Jacobian is L, triangular, so its determinant is the product of the diagonal:

$$\log|\det\partial z/\partial\epsilon|=\sum_k\log|L_{kk}| \tag{10.53}$$

Construct $L=M\odot L'+\mathrm{diag}(\sigma)$ (10.54), where M has 0s on and above the diagonal and 1s below, and $(\mu,\log\sigma,L')$ come from the inference network. Then the diagonal of L is σ and $\log|\det|=\sum_k\log\sigma_k$ (10.55).

**10.2.1.3 Low-rank plus diagonal (p. 449).** Factor form $\Sigma=BB^T+C^2$ (10.56). B is the $d\times f$ factor loading matrix, $f\ll d$ factors, $C=\mathrm{diag}(c_1,\dots,c_d)$. The variational parameters drop from $d+d(d+1)/2$ to $(f+2)d$ (called VAFC in [ONS18]). For $f=1$: $\Sigma=bb^T+\mathrm{diag}(c^2)$ (10.57). Then the natural gradient of the ELBO is available in closed form in $O(d)$ time (NAGVAC-1), which can give much faster convergence than the ordinary gradient. §10.1.2 shows this beats a diagonal approximation.

**10.2.1.4 Other posteriors (p. 449).** Many other distributions are reparameterizable, including gamma, Dirichlet and inverse autoregressive flows (§10.4.3).

**10.2.1.5 Example: Bayesian parameter inference (pp. 450–451).** Infer the posterior of GMM parameters θ. The discrete latents are marginalized out ("collapsed" model: Figure 10.5b becomes 10.5a), so only $p(\theta|D)$ is approximated. The likelihood for one datapoint $x\in\mathbb R^D$ with diagonal precisions:

$$p(x|\theta)=\sum_{k=1}^K\pi_k\mathcal N(x|\mu_k,\mathrm{diag}(\lambda_k)^{-1}) \tag{10.58}$$

Prior (ξ are hyperparameters) and mean-field posterior (conjugate to the likelihood, yet reparameterizable):

$$p_\xi(\theta)=\Big[\prod_{k=1}^K\prod_{d=1}^D\mathcal N(\mu_{kd}|0,1)\,\mathrm{Ga}(\lambda_{kd}|5,5)\Big]\mathrm{Dir}(\pi|\mathbf 1) \tag{10.59}$$
$$q_\psi(\theta)=\Big[\prod_{k=1}^K\prod_{d=1}^D\mathcal N(\mu_{kd}|m_{kd},s_{kd})\,\mathrm{Ga}(\lambda_{kd}|\alpha_{kd},\beta_{kd})\Big]\mathrm{Dir}(\pi|c) \tag{10.60}$$
$$Ł(\xi,\psi|D)=\mathbb E_{q_\psi}[\log p(D|\theta)+\log p_\xi(\theta)-\log q_\psi(\theta)] \tag{10.61}$$

Use one posterior sample for the expectation and minibatches for the likelihood. Algorithm 10.2: each iteration samples a minibatch, $\epsilon\sim q_0$, $\tilde\theta=g(\psi,\epsilon)$, computes $\mathcal L=-\tfrac NB\sum_{x_n\in\mathcal B}\log p(x_n|\tilde\theta)-\log p_\xi(\tilde\theta)+\log q_\psi(\tilde\theta)$, then takes gradient steps on ξ and ψ with rate η (p. 451).

Experiment (Figure 10.6): 3000 points from 3 Gaussians in 2D, $\mu_1^*=[2,0]$, $\mu_2^*=[-2,-4]$, $\mu_3^*=[-2,4]$, precisions 1, weights 1/3 each. SVI used batch size 500, 1000 epochs, Adam. The posterior mean $\mathbb E[\mu_1]\approx[-2,-4]$, which matches $\mu_2^*$ rather than $\mu_1^*$ because of label-switching unidentifiability (p. 451).

**10.2.1.6 Example: MLE for LVMs (p. 452).** For continuous-latent LVMs such as VAEs, local latents cannot be marginalized analytically, so use amortized inference. Algorithm 10.3 per iteration: sample $x_n$, $\epsilon_n\sim q_0$; $z_n=g(\phi,x_n,\epsilon_n)$; $\mathcal L=-\log p_\theta(x_n,z_n)+\log q_\phi(z_n|x_n)$; gradient steps on θ and ϕ.

### 10.2.2 Automatic differentiation VI (ADVI) (pp. 452–453)
Gaussian VI needs unconstrained parameters in $\mathbb R^D$. For any distribution with a bijection to $\mathbb R^D$ this works; the approach is called ADVI.

**10.2.2.1 Basic idea.** Target $p(\theta|D)\propto p(\theta)p(D|\theta)$, $\theta\in\Theta$ (constrained). Let $T:\Theta\to\mathbb R^D$ be a bijection, $u=T(\theta)$, and $q_\psi(u)=\mathcal N(u|\mu,\Sigma)$, $\psi=(\mu,\Sigma)$. By change of variables:

$$p(u)=p(T^{-1}(u))\,|\det J_{T^{-1}}(u)| \tag{10.62}$$
$$Ł(\psi)=\mathbb E_{u\sim q_\psi}\big[\log p(D|T^{-1}(u))+\log p(T^{-1}(u))+\log|\det J_{T^{-1}}(u)|\big]+\mathbb H(\psi) \tag{10.63}$$

This is tractable if the Jacobian is: the entropy is closed form and the expectation is Monte Carlo. SGD applies. [Ing20] propose *deterministic ADVI*: hold the samples $\epsilon_s\sim\mathcal N(0,I)$ fixed (common random numbers trick), so the objective is deterministic and second-order optimizers such as BFGS can be used. Minibatching, for large data, reintroduces stochasticity (p. 453).

**10.2.2.2 Beta-binomial.** Prior Beta(θ|a,b) with $a=b=1$, Bernoulli likelihood with $N_1=10$, $N_0=1$. Use $\theta=T^{-1}(z)=\sigma(z)$ and SGD. The Gaussian fit is a good approximation despite the skewed posterior (Figure 7.4, outside this unit) (p. 453).

**10.2.2.3 GMMs.** Differs from VBEM (§10.3.6) by using a Gaussian q over unconstrained parameters instead of a product of conjugate distributions. Discrete $m_n\in\{1..K\}$ are marginalized: $p(D|\theta)=\prod_n[\sum_k\pi_k\mathcal N(y_n|\mu_k,\mathrm{diag}(\Sigma_k))]$ (10.64). Priors: uninformative Gaussian on $\mu_k$, uniform LKJ on $L_k$, log-normal on $\sigma_k$, uniform Dirichlet on π. The posterior is block-diagonal Gaussian. On Old Faithful with K = 10 (Figure 10.7): the MAP special case ($\psi_\Sigma=0$) shows no sparsity, since there is no Bayesian "Occam factor". Posterior samples strongly prefer 2 components, with small support for others (faint ellipses) (p. 453).

**10.2.2.4.** ADVI can be combined with richer posteriors from §10.4 (Gaussian mixtures, normalizing flows) (p. 453).

### 10.2.3 Blackbox VI and REINFORCE (start; p. 454)
Assume $\tilde{\mathcal L}(\psi,z)=\log p(z,x)-\log q_\psi(z)$ can be evaluated pointwise, but its gradient is not assumed available (e.g., z has discrete variables). This is BBVI. Write $Ł(\psi)=\mathbb E_{q(z|\psi)}[\tilde{\mathcal L}(\psi,z)]$ (10.65). The score function (REINFORCE) estimator from Eq. 6.58 gives

$$\nabla_\psi Ł(\psi)=\mathbb E_{q(z|\psi)}[\tilde{\mathcal L}(\psi,z)\,\nabla_\psi\log q(z|\psi)] \tag{10.66}$$

The unit stops here.

## Toy example (ours)
Binary latent z ∈ {0,1}, one observation x. Prior p(z=1)=0.5. Likelihood p(x|z=1)=0.8, p(x|z=0)=0.2.
- Joint: p(x,z=1)=0.4, p(x,z=0)=0.1. Evidence p(x)=0.5, so log p(x)=−0.6931. Posterior p(z=1|x)=0.8.
- Take q(z=1)=0.5. ELBO = 0.5(log0.4−log0.5)+0.5(log0.1−log0.5) = 0.5·log0.8+0.5·log0.2 = 0.5(−0.2231)+0.5(−1.6094) = −0.9163.
- Gap to evidence: −0.6931−(−0.9163)=0.2232.
- KL(q‖posterior) = 0.5·log(0.5/0.8)+0.5·log(0.5/0.2) = 0.5(−0.4700)+0.5(0.9163)=0.2231 (equal up to rounding), as in (10.7).
- Eq. (10.14) check: q equals the prior, so KL to prior = 0, and the ELBO equals the expected log likelihood 0.5·log0.8+0.5·log0.2 = −0.9163.
- Take q(z=1)=0.8 (the exact posterior): ELBO = 0.8·log(0.4/0.8)+0.2·log(0.1/0.2) = log0.5 = −0.6931 = log p(x). The gap is 0.

## Concepts
- [[variational-inference-elbo]] — approximate the posterior by maximizing the ELBO over a family $q_\psi$ (pp. 439–441)
- [[kl-divergence]] — $D_{KL}(q\|p)$ is the loss; the gap between log p(x) and the ELBO (p. 439)
- [[marginal-likelihood-evidence]] — $\log p_\theta(x)$, the intractable "evidence" that upper-bounds the ELBO (p. 440)
- [[posterior-distribution]] — target $p_\theta(z|x)$, assumed unnormalizable (p. 439)
- [[variational-free-energy]] (new) — expected energy minus entropy, the negative ELBO (p. 440)
- [[mean-field-assumption]] (new) — q factorizes over groups of latents; optimized by coordinate ascent (p. 441)
- [[variational-em]] (new) — alternate ELBO maximization over ψ (E) and θ (M) (p. 443)
- [[stochastic-variational-inference]] (new) — minibatch estimate of the ELBO, scaled by N/B (p. 444)
- [[amortized-inference]] (new) — an inference network predicts local variational parameters from x (p. 444)
- [[reparameterization-trick]] (new) — write z = g(ϕ,x,ε) so gradients flow through z (p. 447)
- [[advi]] (new) — Gaussian VI on parameters transformed to $\mathbb R^D$ by a bijection (p. 452)
- [[score-function-estimator]] (new) — REINFORCE gradient of an expectation, for blackbox VI (p. 454)
- [[monte-carlo-integration]] — single-sample estimates of ELBO expectations/gradients (p. 446)

## Canonical instances
- [[gaussian-mean-2d-vi]] — full vs diagonal vs low-rank Gaussian q for a 2D Gaussian mean; diagonal is over-confident (pp. 441–442)
- [[svi-gmm-3-components]] — reparameterized SVI on a 3-component 2D mixture, with label switching (p. 451)
- [[advi-beta-binomial]] — Gaussian in logit-like space approximates a skewed Beta posterior (p. 453)
- [[advi-gmm-old-faithful]] — K=10 mixture, Bayesian fit prefers 2 components, MAP shows no sparsity (p. 453)

## Bridges (candidates)
- [structural-analogy] ELBO = expected energy − entropy ↔ statistical physics: free energy = energy − entropy — the text itself names the VFE (p. 440).
- [metaphor] Amortized inference network ↔ learning to learn: one shared model replaces per-example optimization.
- [same-math] Reparameterized gradient $\mathbb E_{p(\epsilon)}[\nabla_\phi f(g(\phi,\epsilon))]$ ↔ Monte Carlo integration: a single-sample Monte Carlo estimate of an expectation of a gradient.

## Questions this raises
- Why is minimizing $D_{KL}(q\|p)$ mode-seeking and over-confident for a diagonal q, and how severe can this be?
- When is the closed-form-KL objective $f'$ worth its loss of generality compared with the sampled $f$?
- How large can the amortization gap be, and does warm-starting always remove it?
- How high is the variance of the REINFORCE estimator (10.66) compared with reparameterized gradients?

## Reading notes
- Printed = pdf − 34 (pdf 473–488 = printed 439–454).
- The part starts at §10.1 (chapter opening) and ends on printed p. 454 at Eq. (10.66), the start of §10.2.3.1 (REINFORCE). The rest of §10.2.3, §10.3 onward are not covered.
- Eq. (10.50) as printed has no constant −½ per dimension: for K=1, μ=0, σ=1 it gives ½, though both distributions are then identical (KL = 0). The missing constant does not affect gradients.
- Eq. (10.49) is printed with "+ D_KL"; the sign is as printed, but a loss to be minimized would be expected to combine the terms with opposite signs. Not resolved in these pages.
- Typos in the source: "pseudcode", "reparamterizable", "maximing"; in §10.2.2.1 "$\mu_d$" is printed for the mean.
- Cross-references (Sections 3.4.4.1, 5.1.4.3, 6.3.4–6.3.5, 6.5.6.1, 7.4.4, 10.3, 10.4, 10.5, Figure 10.12, Figure 7.4) point outside this unit. The unit has no exercises.
