---
id: murphy-2023-pml2/ch07-inference
work: murphy-2023-pml2
unit: "7 Inference algorithms: an overview"
pages: 345–357
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 0
pipeline_version: 0.1
---
# Inference algorithms: an overview

## L0 — One line
Bayesian inference means computing posterior expectations (integrals), which is exact only in special cases; otherwise we choose among approximations (the MAP point estimate, grid, Laplace, variational inference (VI), Markov chain Monte Carlo (MCMC), sequential Monte Carlo (SMC)) that trade off speed, accuracy and generality.

## L1 — The gist (≤ 120 words)
The chapter asks how to compute a posterior $p(\theta|\mathcal D)$ and expectations under it. The hard part is the normalising integral $p(\mathcal D)$. Exact answers exist for conjugate exponential-family models and for discrete models, using dynamic programming when a graphical model gives structure. Otherwise one approximates. The chapter sorts models by where the latent variables sit (global, local, or both). It compares them on a beta-Bernoulli example. The maximum a posteriori (MAP) point estimate is the simplest and has clear flaws. Grid, Laplace and variational methods approximate the posterior with a simple form. Markov chain Monte Carlo (MCMC) uses samples; sequential Monte Carlo (SMC) moves through a sequence of distributions. The chapter ends with ways to evaluate approximations.

**Prerequisites:** Bayes' rule; integrals as expectations; Taylor expansion, gradient and Hessian; KL divergence; exponential families (basic); Gaussian density.

## L2 — Key ideas (5–10 bullets)
- Integration is at the heart of Bayesian inference: posterior means, covariances, marginals, predictions and expected losses are posterior expectations $\mathbb E[g(\theta)|\mathcal D]$, and the marginal likelihood is an expectation under the prior. The bottleneck is the normalising integral $p(\mathcal D)$ (pp. 345–346).
- Three patterns of latent structure (global, local, global+local) lead to different algorithms (pp. 346–348).
- Exact inference is available for conjugate exponential-family models (add natural parameters) and for discrete models with probabilistic graphical model (PGM) structure (dynamic programming) (p. 348).
- MAP gives no uncertainty, is often atypical of the posterior, and depends on the parameterisation (pp. 349–350).
- Grid approximation is simple but does not scale beyond 2–3 dimensions. Laplace fits a Gaussian at the mode, using the Hessian; it was a poor fit on the skewed, constrained 1-d example, and a change of variable can fix the constraint problem (pp. 351–352).
- VI maximises the evidence lower bound (ELBO) to fit a tractable $q$. Automatic differentiation VI (ADVI) makes it "turn-key" by moving to unconstrained space (pp. 352–354).
- MCMC avoids computing $p(\mathcal D)$: Metropolis–Hastings (MH) needs only unnormalised density ratios, Gibbs sampling uses full conditionals, and Hamiltonian Monte Carlo (HMC) uses the gradient of the log joint. SMC moves through a sequence of distributions; a common use is online (sequential) inference (pp. 354–355).
- Approximations are judged by distance to a reference posterior, or by predictive loss, since the true posterior is usually unavailable (p. 356).

## L3 — Walkthrough

### 7.1 Introduction (pp. 345–346)
Everything unknown (predictions, hidden states, parameters) is a random variable, and inference means computing its posterior given the data (p. 345). With unknowns $\theta$ and data $\mathcal D$:

$$p(\theta|\mathcal D)=\frac{p(\theta)p(\mathcal D|\theta)}{p(\mathcal D)}\tag{7.1}$$
$$p(\mathcal D)=\int p(\mathcal D|\theta)p(\theta)\,d\theta\tag{7.2}$$

Computing (7.2), a high-dimensional integral, is the main bottleneck. It turns the unnormalised joint $p(\theta,\mathcal D)$ into a normalised posterior (p. 345). Posterior expectations are

$$\mathbb E[g(\theta)|\mathcal D]=\int g(\theta)p(\theta|\mathcal D)\,d\theta\tag{7.3}$$

Choices of $g$ (pp. 345–346):
- mean: $g=\theta$ (7.4)
- covariance: $g=(\theta-\mathbb E[\theta|\mathcal D])(\theta-\mathbb E[\theta|\mathcal D])^{\mathsf T}$ (7.5)
- marginals: $g=p(\theta_1=\theta_1^*|\theta_{2:D})$ (7.6)
- predictive: $g=p(y_{N+1}|\theta)$ (7.7)
- expected loss: $g=\ell(\theta,a)$ (7.8)

Setting $g(\theta)=p(\mathcal D|\theta,M)$ gives the marginal likelihood as an expectation under the prior:

$$\mathbb E[g(\theta)|M]=\int p(\mathcal D|\theta,M)p(\theta|M)\,d\theta=p(\mathcal D|M)\tag{7.9}$$

Integration is at the heart of Bayesian inference, differentiation at the heart of optimisation (p. 346). Most of these methods are model-independent. Modellers can build the best model and let an inference engine do the rest, "turning the Bayesian crank" (p. 346).

*Intuition note:* Many Bayesian outputs (means, predictions, expected losses) are averages over the posterior. So much of the work is computing averages when the normaliser is unknown.

### 7.2 Common inference patterns (pp. 346–348)
**7.2.1 Global latents.** Parameters $\theta$ are shared by all $N$ cases (Fig. 7.1a), the usual supervised setting:
$$p(y_{1:N},\theta|x_{1:N})=p(\theta)\Big[\prod_{n=1}^N p(y_n|x_n,\theta)\Big]\tag{7.10}$$
The goal is $p(\theta|x_{1:N},y_{1:N})$ (p. 347).

**7.2.2 Local latents.** Hidden states $z_{1:N}$, with $\theta$ known (Fig. 7.1b):
$$p(x_{1:N},z_{1:N}|\theta)=\Big[\prod_{n=1}^N p(x_n|z_n,\theta_x)p(z_n|\theta_z)\Big]\tag{7.11}$$
The goal is $p(z_n|x_n,\theta)$ for each $n$ (p. 347). If $\theta$ is unknown, one may plug in a point estimate such as the maximum-likelihood one. Given $\theta$ the latents are conditionally independent, so inference can run in parallel. This lets us use methods such as expectation maximisation (EM): infer $p(z_n|x_n,\theta_t)$ for all $n$ in the E step, then update $\theta_t$ in the M step. If $z_n$ cannot be inferred exactly, one can use variational inference inside EM, a combination known as variational EM (p. 347).

With a minibatch $\mathcal D_t$, marginalise out $z_n$:
$$\log p(\mathcal D_t|\theta_t)=\sum_{n\in\mathcal D_t}\log\Big[\sum_{z_n}p(x_n,z_n|\theta_t)\Big]\tag{7.12}$$
If the sum cannot be done exactly, one can use variational inference, a combination known as stochastic variational inference (SVI). Learning an inference network $q_\phi(z|x;\theta)$ amortises the cost across batches (amortised SVI) (p. 347).

**7.2.3 Global and local.** Both kinds are uncertain (Fig. 7.1c):
$$p(x_{1:N},z_{1:N},\theta)=p(\theta_x)p(\theta_z)\Big[\prod_{n=1}^N p(x_n|z_n,\theta_x)p(z_n|\theta_z)\Big]\tag{7.13}$$
This is less common in ML. Parameter uncertainty is often assumed negligible next to local uncertainty, because $\theta$ is informed by all $N$ cases while each $z_n$ is informed only by $x_n$. The author says there are still advantages to being "fully Bayesian" (p. 348).

### 7.3 Exact inference (p. 348)
If the prior is conjugate to the likelihood, the posterior is analytically tractable. In general this holds when both come from the same exponential family. Let $\mathcal T(\theta)$ be the sufficient statistics and $\lambda$ the natural parameters:
$$p(\theta)\propto\exp(\lambda_0^{\mathsf T}\mathcal T(\theta))\tag{7.14}$$
$$p(y_i|\theta)\propto\exp(\tilde\lambda_i(y_i)^{\mathsf T}\mathcal T(\theta))\tag{7.15}$$
$$p(\theta|y_{1:N})\propto\exp(\lambda_*^{\mathsf T}\mathcal T(\theta)),\qquad \lambda_*=\lambda_0+\sum_{n=1}^N\tilde\lambda_n(y_n)\tag{7.16, 7.17}$$
So the posterior comes from adding natural parameters (details in Section 3.4, not in this unit) (p. 348).

Second case: $D$ discrete unknowns with $K$ states each. The normaliser is a sum of $K^D$ terms, often too many. If the distribution has conditional independence structure expressed by a PGM, the joint factorises into local terms. Then dynamic programming makes it tractable (Chapter 9) (p. 348).

### 7.4 Approximate inference (pp. 348–356)
For most models exact posteriors are out of reach. The methods trade off speed, accuracy, simplicity and generality (p. 348).

**7.4.1 MAP and its problems (pp. 349–350).**
$$\hat\theta=\arg\max p(\theta|\mathcal D)=\arg\max\ \log p(\theta)+\log p(\mathcal D|\theta)\tag{7.18}$$
$$p(\theta|\mathcal D)\approx\delta(\theta-\hat\theta)\tag{7.19}$$
Its advantage is that optimisation algorithms (Chapter 6) can compute it (p. 349). Drawbacks:
- *No uncertainty (7.4.1.1).* A point estimate carries none. Frequentist uncertainty can be derived from it, but the author argues it is arguably more natural to compute the posterior. Plugging in a point estimate can underestimate predictive uncertainty, giving predictions that are "confidently wrong" (p. 349).
- *Atypical (7.4.1.2).* The mode is often a poor summary. In Fig. 7.2a, for $0.5\mathcal N(x|0,2)+0.5\mathcal N(x|2,0.05)$, the mode is an isolated peak far from most of the mass, and the mean is near the middle. In Fig. 7.2b, for Gamma(1,1), the mode is 0 but the mean is non-zero. Such skewed shapes often arise when inferring variance parameters, especially in hierarchical models. There the MAP (and hence the MLE) is "obviously a very bad estimate" (pp. 349–350).
- *Not invariant to reparameterisation (7.4.1.3).* Beliefs should not change if we use probability or logit for a Bernoulli. But in general $\hat y=\arg\max p_y(y)$ is not $f(\hat x)$. Example: $x\sim\mathcal N(6,1)$, $y=f(x)=1/(1+\exp(-x+5))$. By change of variables $p_y(y)=p_x(f^{-1}(y))\,|df^{-1}(y)/dy|$, or by Monte Carlo. The Gaussian is "squashed", and the mode of $y$ is not the transform of the mode of $x$ (Fig. 2.12, cited, not in this unit). The MLE avoids this because the likelihood is a function, not a density. Full Bayesian inference avoids it because the change of measure is accounted for when integrating (p. 350).

*Intuition note:* A mode is just the highest point of a density. Stretching the axis changes the density's height pattern, so the highest point moves. Bayesian inference integrates over probability mass and accounts for the change of measure, so the source says it does not suffer from this problem.

**7.4.2 Grid approximation (pp. 350–351).** Partition parameter space into regions $r_1,\dots,r_K$, each of volume $\Delta$ centred on $\theta_k$. Then $p(\theta\in r_k|\mathcal D)\approx p_k\Delta$ with
$$p_k=\frac{\tilde p_k}{\sum_{k'=1}^K\tilde p_{k'}},\qquad \tilde p_k=p(\mathcal D|\theta_k)p(\theta_k)\tag{7.20, 7.21}$$
The denominator numerically approximates the normaliser:
$$p(\mathcal D)=\int p(\mathcal D|\theta)p(\theta)\,d\theta\approx\sum_{k=1}^K\Delta\tilde p_k\tag{7.22}$$
Example: beta-Bernoulli, 10 heads and 1 tail ($N=11$), uniform prior:
$$p(\theta|\mathcal D)\propto\Big[\prod_{n=1}^N\mathrm{Ber}(y_n|\theta)\Big]\mathrm{Beta}(1,1)\tag{7.23}$$
With 20 grid points (Fig. 7.3a) the grid captures the skewed posterior. It does not scale beyond 2–3 dimensions, because the number of grid points grows exponentially with dimension (p. 351).

**7.4.3 Laplace (quadratic) approximation (pp. 351–352).** Write $p(\theta|\mathcal D)=\frac1Z e^{-\mathcal E(\theta)}$, with energy $\mathcal E(\theta)=-\log p(\theta,\mathcal D)$ and $Z=p(\mathcal D)$ (7.24). Taylor-expand around the mode $\hat\theta$, with $g$ the gradient and $\mathbf H$ the Hessian at the mode:
$$\mathcal E(\theta)\approx\mathcal E(\hat\theta)+(\theta-\hat\theta)^{\mathsf T}g+\tfrac12(\theta-\hat\theta)^{\mathsf T}\mathbf H(\theta-\hat\theta)\tag{7.25}$$
Since $\hat\theta$ is the mode, $g=0$, so
$$\hat p(\theta,\mathcal D)=e^{-\mathcal E(\hat\theta)}\exp\!\Big[-\tfrac12(\theta-\hat\theta)^{\mathsf T}\mathbf H(\theta-\hat\theta)\Big]\tag{7.26}$$
$$\hat p(\theta|\mathcal D)=\tfrac1Z\hat p(\theta,\mathcal D)=\mathcal N(\theta|\hat\theta,\mathbf H^{-1})\tag{7.27}$$
$$Z=e^{-\mathcal E(\hat\theta)}(2\pi)^{D/2}|\mathbf H|^{-1/2}\tag{7.28}$$
The last line follows from the Gaussian normaliser (p. 352). It is easy to apply: use existing optimisers for the MAP, then compute the Hessian (a diagonal approximation is possible in high dimensions). On the 1-d example (Fig. 7.3b) it is "not a particularly good approximation". The posterior is skewed but a Gaussian is symmetric, and $\theta\in[0,1]$ while the Gaussian lives on $\mathbb R^D$. The second problem can be fixed by a change of variable, e.g. applying Laplace to $\alpha=\mathrm{logit}(\theta)$ (p. 352).

*Intuition note:* Laplace fits a bell curve that matches the posterior's peak and its curvature there. In the source's 1-d example it fits poorly because the posterior is skewed (a Gaussian is symmetric) and constrained to $[0,1]$; a change of variable can fix the constraint problem.

**7.4.4 Variational inference (pp. 352–354).** VI (also called variational Bayes) is another optimisation-based method with much more modelling flexibility. It picks the tractable $q\in\mathcal Q$ closest to $p(\theta|\mathcal D)$:
$$q^*=\arg\min_{q\in\mathcal Q}D(q,p)\tag{7.29}$$
One usually optimises variational parameters $\psi$ of $q$. With the KL divergence:
$$D(q,p)=D_{\mathrm{KL}}(q(\theta|\psi)\,\|\,p(\theta|\mathcal D))=\int q(\theta|\psi)\log\frac{q(\theta|\psi)}{p(\theta|\mathcal D)}d\theta\tag{7.30}$$
$$\psi^*=\arg\min_\psi D_{\mathrm{KL}}(q(\theta|\psi)\|p(\theta|\mathcal D))\tag{7.31}$$
$$=\arg\min_\psi\mathbb E_{q(\theta|\psi)}\Big[\log q(\theta|\psi)-\log\frac{p(\mathcal D|\theta)p(\theta)}{p(\mathcal D)}\Big]\tag{7.32}$$
$$=\arg\min_\psi\underbrace{\mathbb E_{q(\theta|\psi)}[-\log p(\mathcal D|\theta)-\log p(\theta)+\log q(\theta|\psi)]}_{-\text{Ł}(\psi)}+\log p(\mathcal D)\tag{7.33}$$
Since $\log p(\mathcal D)$ does not depend on $\psi$, one maximises
$$\text{Ł}(\psi)\triangleq\mathbb E_{q(\theta|\psi)}[\log p(\mathcal D|\theta)+\log p(\theta)-\log q(\theta|\psi)]\tag{7.34}$$
From (7.33), $D_{\mathrm{KL}}=\log p(\mathcal D)-\text{Ł}(\psi)$ (added step). Because $D_{\mathrm{KL}}\ge0$, $\text{Ł}(\psi)\le\log p(\mathcal D)$. This is the evidence lower bound (ELBO). The log marginal likelihood is called the evidence. Maximising the ELBO makes $q$ closer to the true posterior (p. 353).

$q$ can be any form, e.g. $\mathcal N(\theta|\mu,\Sigma)$. This differs from Laplace because $\Sigma$ is optimised rather than set to the Hessian. A diagonal $\Sigma$ means a fully factorised posterior, the mean field approximation (pp. 353–354). For $\theta\in[0,1]$ one could use $\mathrm{Beta}(\theta|a,b)$, but choosing a form takes expertise. ADVI (automatic differentiation VI) is turn-key. It changes variables to an unconstrained space, fits a Gaussian, and uses automatic differentiation for the Jacobian term. On the example, $\theta=\sigma(z)$ and $q(z|\psi)=\mathcal N(z|\mu,\sigma)$, with the ELBO optimised stochastically by SGD. The author says the results in Fig. 7.4 "seem reasonable" (p. 354).

*Intuition note:* VI turns inference into optimisation over a restricted family. The ELBO can be computed without knowing $p(\mathcal D)$, because $p(\mathcal D)$ only shifts the objective by a constant.

**7.4.5 MCMC (pp. 354–355).** VI is fast but can be biased, because $q$ is restricted to $\mathcal Q$. A more flexible option is a sample-based (non-parametric) Monte Carlo approximation $q(\theta)\approx\frac1S\sum_{s=1}^S\delta(\theta-\theta^s)$. The key issue is drawing $\theta^s\sim p(\theta|\mathcal D)$ without evaluating $p(\mathcal D)$. Importance sampling suits low dimensions (Section 11.5). In high dimensions MCMC is more common (p. 354).

Metropolis–Hastings (MH): start at a random point and random-walk via a proposal $q(\theta'|\theta)$. If $q$ is well chosen, the fraction of time spent at each point is proportional to its posterior probability (pp. 354–355). To accept or reject a move one needs only the unnormalised ratio:
$$\frac{p(\theta|\mathcal D)}{p(\theta'|\mathcal D)}=\frac{p(\mathcal D|\theta)p(\theta)/p(\mathcal D)}{p(\mathcal D|\theta')p(\theta')/p(\mathcal D)}=\frac{p(\mathcal D,\theta)}{p(\mathcal D,\theta')}\tag{7.35}$$
So $p(\mathcal D)$ is avoided. In practice log probabilities are used. Inputs are the log joint and a proposal. Random walk Metropolis uses $q(\theta'|\theta)=\mathcal N(\theta'|\theta,\sigma\mathbf I)$ and can be inefficient (blind walking) (p. 355).
- **Gibbs sampling:** in models with conditional independence structure it is often easy to compute the full conditionals $p(\theta_d|\theta_{-d},\mathcal D)$ one variable at a time and sample from them. It is a stochastic analogue of coordinate ascent (Section 12.3) (p. 355).
- **HMC:** if all unknowns are continuous, one can often compute the gradient $\nabla_\theta\log p(\theta,\mathcal D)$ and use it to guide proposals into regions of higher probability. It is one of the most widely used MCMC algorithms due to its speed (Section 12.5) (p. 355).

On the beta-Bernoulli model (logit parameter), HMC with 4 chains oscillates around the true posterior. The kernel density estimate is a good approximation (Fig. 7.5) (p. 355).

**7.4.6 Sequential Monte Carlo (p. 355).** MCMC resembles stochastic local search. SMC instead moves through a sequence of distributions from simpler to more complex, the last being the target posterior. The author likens it to tree search. A common use is sequential Bayesian inference: recursively compute $p(\theta_t|\mathcal D_{1:t})$, with $\mathcal D_{1:t}=\{(x_n,y_n):n=1{:}t\}$. This converges to the batch posterior $p(\theta|\mathcal D)$ once all data are seen. It also works for unending data streams, as in state-space models. SMC applied to dynamical models is particle filtering (Section 13.2) (p. 355).

**7.4.7 Challenging posteriors (p. 356).** Posteriors can be high-dimensional and multimodal. In the 2-d example (Fig. 7.6), MAP gives no uncertainty, and a Gaussian (Laplace or VI) is a parametric approximation. MCMC samples are serially correlated and may explore only one mode. Ideally one draws independent samples from the whole support. A local parametric fit around each sample gives a semi-parametric approximation (Section 17.3.9.1, cited) (p. 356).

### 7.5 Evaluating approximate inference (pp. 356–357)
Algorithms trade speed, accuracy, generality and simplicity, so they are hard to compare directly (p. 356). Options:
- Compare to a "true" posterior computed offline by an "exact" method, via $D_{\mathrm{KL}}(p(\theta|\mathcal D)\|q_t(\theta))$, where $q_t$ is the approximation after $t$ units of compute time. Other distances, e.g. Wasserstein, also work. The true posterior is usually impossible to compute (p. 356).
- Judge predictions on out-of-sample data, or compare Bayesian risk (as proposed in [KPS98; KPS99]):
$$R=\mathbb E_{p^*(x,y)}[\ell(y,q(y|x,\mathcal D))],\quad q(y|x,\mathcal D)=\int p(y|x,\theta)q(\theta|\mathcal D)d\theta\tag{7.36}$$
with $\ell$ e.g. log-loss.
- Measure performance on a downstream task such as continual or active learning ([Far22]) (p. 356).

Specialised assessments are cited: for VI [Yao+18b; Hug+20], for Monte Carlo [CGR06; CTM17; GAR16] (p. 357).

## Toy example (ours)
Grid approximation and the MH ratio on a tiny problem. Data: 2 heads and 1 tail ($N=3$). Grid: $\theta_k\in\{0.25,0.5,0.75\}$ with prior $1/3$ each. The grid is discrete, so the sum below plays the role of (7.22), and $\Delta$ cancels in (7.20).

$\tilde p_k=\theta_k^2(1-\theta_k)\cdot\frac13$:
- $\theta=0.25$: $0.0625\cdot0.75=0.046875$; $/3=0.015625$
- $\theta=0.5$: $0.25\cdot0.5=0.125$; $/3=0.041667$
- $\theta=0.75$: $0.5625\cdot0.25=0.140625$; $/3=0.046875$

Sum: $\sum\tilde p_k=0.104167=5/48$. This is the evidence $p(\mathcal D)$ under this discrete prior. Then $p_k=\tilde p_k/0.104167=0.15,\ 0.40,\ 0.45$, which sum to 1. Posterior mean $=0.25(0.15)+0.5(0.40)+0.75(0.45)=0.0375+0.2+0.3375=0.575$. For MH, comparing $0.75$ with $0.5$ needs only $\tilde p(0.75)/\tilde p(0.5)=0.046875/0.041667=1.125$. This equals $0.45/0.40$, and no normaliser appears, as in (7.35).

## Concepts
- [[bayes-theorem]] — posterior = prior × likelihood / $p(\mathcal D)$; $p(\mathcal D)$ is the bottleneck (p. 345)
- [[posterior-distribution]] — target of inference; used via expectations $\mathbb E[g(\theta)|\mathcal D]$ (p. 345)
- [[marginal-likelihood]] — $p(\mathcal D|M)$ as the prior expectation of the likelihood; also called the evidence (pp. 346, 353)
- [[conjugate-prior]] — a prior conjugate to the likelihood gives a tractable posterior; in general this is the case when both are in the same exponential family, so natural parameters add (p. 348)
- [[posterior-predictive-distribution]] — $g(\theta)=p(y_{N+1}|\theta)$ averaged over the posterior (pp. 346, 356)
- [[variational-inference-elbo]] — fit tractable $q$ by minimising KL to the posterior, i.e. maximising Ł (pp. 352–353)
- [[kl-divergence]] — discrepancy used by VI, $D_{\mathrm{KL}}(q\|p)$; the evaluation measure is $D_{\mathrm{KL}}(p\|q_t)$ (pp. 352, 356)
- [[monte-carlo-integration]] — approximate the posterior by $S$ samples (p. 354)
- [[markov-chain-monte-carlo]] — random walk whose visit frequencies are proportional to the posterior probability if the proposal is chosen carefully (pp. 354–355)
- [[metropolis-hastings]] — accept moves using the unnormalised ratio (7.35) (pp. 354–355)
- [[gibbs-sampling]] — sample each variable from its full conditional (p. 355)
- [[hamiltonian-monte-carlo]] — gradient-guided proposals (p. 355)
- [[map-estimate]] (new) — posterior mode, treated as a delta distribution (p. 349)
- [[grid-approximation]] (new) — discretise parameter space, normalise numerically (p. 351)
- [[laplace-approximation]] (new) — Gaussian $\mathcal N(\hat\theta,\mathbf H^{-1})$ at the mode (p. 352)
- [[mean-field-approximation]] (new) — Gaussian $q$ with diagonal $\Sigma$, i.e. fully factorised (p. 354)
- [[advi]] (new) — VI after mapping to unconstrained space, with automatic differentiation (p. 354)
- [[sequential-monte-carlo]] (new) — inference through a sequence of distributions ending at the posterior; particle filtering in dynamical models (p. 355)
- [[global-vs-local-latents]] (new) — parameters shared by all data versus per-datapoint hidden variables (pp. 346–348)

## Canonical instances
- [[beta-bernoulli-10-heads-1-tail]] — running example used for grid, Laplace, ADVI and HMC (pp. 351–355)
- [[bimodal-mixture-mode-vs-mean]] — shows the mode is untypical (p. 349)
- [[gamma-1-1-mode-zero]] — skewed distribution, mode 0 (pp. 349–350)
- [[sigmoid-transform-of-gaussian]] — MAP is not reparameterisation-invariant (p. 350)
- [[bimodal-2d-approximations]] — MAP, Gaussian, correlated and independent samples (p. 356)

## Bridges (candidates)
- [structural-analogy] ELBO maximisation ↔ MCMC: both avoid $p(\mathcal D)$, one by a constant offset and one by density ratios — they differ in mechanism.
- [structural-analogy] Gibbs sampling ↔ optimisation: stochastic analogue of coordinate ascent (p. 355).
- [same-math] Laplace approximation ↔ second-order Taylor expansion of a log-density at its maximum — the Gaussian is exactly the quadratic expansion.

## Questions this raises
- When is a Gaussian $q$ in VI better than a Laplace Gaussian for the same posterior, and why?
- How does one tell, in practice, that MCMC samples cover all modes rather than one (Fig. 7.6c vs d)?
- Why does the reverse KL ($q\|p$) used in VI differ from the forward KL ($p\|q_t$) used for evaluation?
- How much does ignoring global-parameter uncertainty (7.2.3) hurt in small-data settings?

## Reading notes
- Printed pages 345–357; printed 358 is blank. Printed = pdf − 34.
- Text-layer equations were garbled in places (7.25–7.28, 7.36). I checked them against the page images.
- Likely typos in the source: "There are kinds of posterior" (p. 346, a word seems missing); "use perform inference" (p. 355); "explore a local model" (p. 356, probably "mode"). Equation 7.29 uses $D$ for discrepancy, while $D$ also denotes dimension elsewhere.
- Fig. 2.12, Sections 3.x, 5.1, 10.x–13.x and 17.x are cited but not in this unit, so their content is not summarised.
