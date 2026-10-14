---
id: murphy-2023-pml2/ch12-markov-p1
work: murphy-2023-pml2
unit: "12 Markov chain Monte Carlo (part 1/2): §12.1–12.5.8 (start)"
pages: 499–523
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
# Markov chain Monte Carlo (part 1): Metropolis–Hastings, Gibbs, auxiliary variables, HMC

## L0 — One line
MCMC samples from a hard, high-dimensional target by running a Markov chain whose stationary distribution is that target (via accept/reject moves, conditional resampling, auxiliary variables, or simulated Hamiltonian dynamics).

## L1 — The gist (≤ 120 words)
How can we draw samples from a high-dimensional distribution that we know only up to a normalizing constant? MCMC builds a Markov chain whose stationary distribution is the target. This part presents Metropolis–Hastings (propose a move, accept it with a ratio in which the constant cancels), Gibbs sampling (resample each variable from its full conditional; every move is accepted), auxiliary-variable methods (slice sampling, Swendsen–Wang), and Hamiltonian Monte Carlo (gradient-guided moves from simulated physics). It also links Langevin sampling to SGD. These samplers are widely used for Bayesian posteriors. The samples are correlated, though, and mixing speed depends on proposals and tuning.

**Prerequisites:** Markov chains (stationary distribution, detailed balance, ergodicity); conditional distributions and Bayes' rule; gradients; Gaussian, Dirichlet and conjugate-prior updates; graphical-model Markov blankets.

## L2 — Key ideas
- MCMC makes a random walk whose long-run time in each state is proportional to $p^*(x)$. Samples are correlated and early ones (burn-in) are discarded (p. 499).
- Metropolis–Hastings (MH) proposes $x'\sim q(x'|x)$ and accepts with $A=\min(1,\alpha)$. The normalizer cancels, so an unnormalized $\tilde p$ suffices (pp. 500–501).
- MH satisfies detailed balance with respect to $p^*$. Hence $p^*$ is stationary, and it is the unique limiting distribution if the chain is ergodic and irreducible (p. 502).
- Proposal scale matters. In random-walk Metropolis, too small a $\tau$ traps the chain and too large a $\tau$ makes it sticky (p. 503).
- Gibbs sampling is MH with full-conditional proposals, so its acceptance probability is 1. It can still mix slowly for correlated variables. Blocking and collapsing (integrating out variables) help (pp. 506, 511–513).
- Auxiliary variables can decorrelate moves. Slice sampling adds a height variable, and Swendsen–Wang adds edge "bond" variables (pp. 513–516).
- HMC adds momentum and simulates Hamiltonian dynamics with a leapfrog integrator. An MH accept/reject step is then applied to the trajectory's endpoint (rejecting if the energy has not stayed the same). It needs gradients and continuous, unconstrained variables (pp. 517–520, 523).
- With $L=1$, HMC becomes the Langevin algorithm (MALA). Minibatch SGD behaves like a Langevin sampler whose "temperature" is $\eta/B$ (pp. 521–523).

## L3 — Walkthrough

### 12.1 Introduction (p. 499)
Non-iterative Monte Carlo (Ch. 11: rejection and importance sampling) gives independent samples but often does not work well in high dimensions (p. 499). MCMC builds a Markov chain on the state space $\mathcal X$ whose stationary distribution is the target $p^*(x)$. In a Bayesian setting $p^*(x)\propto p(x|\mathcal D)$. The fraction of time spent in state $x$ is proportional to $p^*(x)$, so averaging over the correlated samples $x^0,x^1,\dots$ gives Monte Carlo integration with respect to $p^*$ (p. 499). The first samples are not from the stationary distribution and should be discarded. The time to reach stationarity is the *mixing* or *burn-in* time, and reducing it is one of the most important factors in making the algorithm fast (p. 499). History as given: invented at Los Alamos, first published in [Met+53]; Gibbs sampling was invented independently in [GG84]; the method became well known to statisticians with [GS90] (p. 499).

### 12.2 Metropolis–Hastings

**12.2.1 Basic idea (pp. 500–501).** At each step, propose $x'$ from the current $x$ with probability $q(x'|x)$ (the *proposal distribution* or *kernel*). Accept it with some probability. If rejected, the new state is the old state, i.e. the sample is repeated (p. 500).

Symmetric proposal, $q(x'|x)=q(x|x')$:
$$A=\min\!\Big(1,\frac{p^*(x')}{p^*(x)}\Big)\tag{12.1}$$
A more probable $x'$ is always accepted. A less probable $x'$ may still be accepted, so "downhill" moves occur (p. 500).

Asymmetric proposal needs the Hastings correction:
$$A=\min(1,\alpha)\tag{12.2}$$
$$\alpha=\frac{p^*(x')\,q(x|x')}{p^*(x)\,q(x'|x)}=\frac{p^*(x')/q(x'|x)}{p^*(x)/q(x|x')}\tag{12.3}$$
It compensates for the proposal itself favouring some states. An exploratory step into a low-probability region is more likely if $q(x|x')$ is large, i.e. the chain can easily return (p. 500).

If $p^*(x)=\tilde p(x)/Z$, then
$$\alpha=\frac{(\tilde p(x')/Z)\,q(x|x')}{(\tilde p(x)/Z)\,q(x'|x)}\tag{12.4}$$
and the $Z$'s cancel, so $Z$ need not be known (p. 500).

A proposal is *valid/admissible* if it covers the support of the target:
$$\forall x.\; x'\in\mathrm{supp}(p^*)\Rightarrow q(x'|x)>0\tag{12.5}$$
Algorithm 12.1: initialize $x^0$; for $s=0,1,\dots$ set $x=x^s$; sample $x'\sim q(x'|x)$; compute $\alpha=\tilde p(x')q(x|x')/(\tilde p(x)q(x'|x))$ and $A=\min(1,\alpha)$; sample $u\sim U(0,1)$; set $x^{s+1}=x'$ if $u\le A$, else $x^{s+1}=x^s$ (p. 501).

*Intuition note.* The accept/reject rule favours high-probability states without ever needing the normalizer. Rejected moves are counted as a repeated sample (p. 500), and the accept/reject formula is what ensures the long-run fraction of time in each state is proportional to $p^*$.

**12.2.2 Why MH works (pp. 501–502).** The MH chain has transition probabilities
$$p(x'|x)=\begin{cases}q(x'|x)A(x'|x)& x'\neq x\\ q(x|x)+\sum_{x'\neq x}q(x'|x)\,(1-A(x'|x))&\text{otherwise}\end{cases}\tag{12.6}$$
A move to $x'$ requires a proposal and an acceptance. Staying put happens either because $x$ itself was proposed or because another state was proposed and rejected (p. 501). Detailed balance:
$$p(x'|x)\,p^*(x)=p(x|x')\,p^*(x')\tag{12.7}$$
(in-flow equals out-flow between each pair of states). The text recalls that detailed balance implies $p^*$ is stationary (p. 501). If (12.7) holds, $p^*$ is called *invariant* for the kernel (p. 502).

**Theorem 12.2.1.** If the MH transition matrix (12.6) is ergodic and irreducible, then $p^*$ is its unique limiting distribution (p. 502).

*Proof (as given).* Either $p^*(x)q(x'|x)<p^*(x')q(x|x')$ (12.8) or $\ge$ (12.9). Without loss of generality assume $p^*(x)q(x'|x)>p^*(x')q(x|x')$. Then
$$\alpha(x'|x)=\frac{p^*(x')q(x|x')}{p^*(x)q(x'|x)}<1\tag{12.10}$$
so $A(x'|x)=\alpha(x'|x)$ and $A(x|x')=1$. Moving $x\to x'$ needs a proposal and an acceptance:
$$p(x'|x)=q(x'|x)A(x'|x)=q(x'|x)\frac{p^*(x')q(x|x')}{p^*(x)q(x'|x)}=\frac{p^*(x')}{p^*(x)}q(x|x')\tag{12.11}$$
$$p^*(x)\,p(x'|x)=p^*(x')\,q(x|x')\tag{12.12}$$
Backwards: $p(x|x')=q(x|x')A(x|x')=q(x|x')$ (12.13). Inserting this in (12.12):
$$p^*(x)\,p(x'|x)=p^*(x')\,p(x|x')\tag{12.14}$$
So detailed balance holds and $p^*$ is stationary (Theorem 2.6.3). It is unique since the chain is ergodic and irreducible (Theorem 2.6.2) (p. 502).

*Intuition note.* Rescaling the acceptance by the ratio $p^*(x')q(x|x')\,/\,p^*(x)q(x'|x)$ is exactly what makes the flow $x\to x'$ equal the flow $x'\to x$. The theorem needs ergodicity and irreducibility as hypotheses; they are not shown to hold automatically.

**12.2.3 Proposal distributions (pp. 502–504).** Good proposal design often depends on the form of the target (p. 502).
- *Independence sampler* (12.2.3.1): $q(x'|x)=q(x')$, similar to importance sampling. A Gaussian is valid for any unconstrained continuous space (p. 502).
- *Random walk Metropolis* (12.2.3.2): $q(x'|x)=\mathcal N(x'|x,\tau^2\mathbf I)$ (12.15). For a Gaussian posterior, [RR01b] prove the asymptotically optimal choice is $\tau^2=2.38^2/D$ ($D$ = dimension), giving acceptance rate 0.234, which "in this case" is the optimal trade-off between exploring widely and rejecting too often (p. 503).
- *Example (Fig. 12.1, p. 503):* target is a mixture of two 1D Gaussians, $\mu=(-20,20)$, $\pi=(0.3,0.7)$, variances $(100,100)$. With proposal std $\tau=1$ the chain stays near its start and misses the mode at $-20$. With $\tau=500$ most moves are rejected and the chain is "sticky", with low effective sample size. With $\tau=8$ it approximates the target well (p. 503).
- *Mixture proposal* (12.2.3.3): $q(x'|x)=\sum_{k=1}^K w_k q_k(x'|x)$ (12.16), with weights summing to one. It is valid if each $q_k$ is valid and each $w_k>0$. If each $q_k$ is reversible (satisfies detailed balance), so is the mixture (p. 504). *Chaining*: $q(x'|x)=\sum_{x_1}\cdots\sum_{x_{K-1}}q_1(x_1|x)q_2(x_2|x_1)\cdots q_K(x|x_{K-1})$ (12.17). A common case is base proposals that each update a subset of variables (p. 504).
- *Data-driven MCMC* (12.2.3.4): for a posterior target, use $q(x'|x,\mathcal D)$, e.g. a trained recognition network or per-component "experts". Example mixture: $q(x'|x,\mathcal D)=\pi_0q_0(x'|x)+\sum_k\pi_kq_k(x'_k|f_k(\mathcal D))$ (12.18), with $q_0$ data-independent. This is "generate and test": proposals generate hypotheses and the ratio $p(x'|\mathcal D)/p(x|\mathcal D)$ tests them (p. 504).
- *Adaptive MCMC* (12.2.3.5): change proposal parameters while running (e.g. broad covariance first, then narrower). The parameters should not depend on the entire chain history, to keep the Markov property. A sufficient condition is that adaptation is gradually "faded out" (p. 504).

**12.2.4 Initialization (p. 505).** Start in a state with non-zero probability. Starting at a local mode is natural, but gradients of the log joint vanish there, which can hurt gradient-based methods such as HMC. It can be better to start "close" to a MAP estimate (p. 505).

### 12.3 Gibbs sampling

**12.3.1 Basic idea (p. 505).** Problems of MH: choosing $q$, and possibly low acceptance. Gibbs sampling uses conditional independence to build a proposal with acceptance probability 1. It is the MCMC analogue of coordinate descent (p. 505). Sample each variable in turn given all others. For $D=3$:
$x_1^{s+1}\sim p(x_1|x_2^s,x_3^s)$, $x_2^{s+1}\sim p(x_2|x_1^{s+1},x_3^s)$, $x_3^{s+1}\sim p(x_3|x_1^{s+1},x_2^{s+1})$ (p. 505). Known variables are not sampled but may be inputs. $p(x_i|x_{-i})$ is the *full conditional*. In a graphical model it depends only on the Markov blanket (neighbours):
$$x_i^{s+1}\sim p(x_i|x^s_{-i})=p(x_i|x^s_{\mathrm{mb}(i)})\tag{12.19}$$
Nodes of the same colour in a colouring of the moralized graph (no neighbours share a colour) can be sampled in parallel. Optimal colouring is NP-complete, but heuristics exist (p. 505).

**12.3.2 Gibbs is a special case of MH (p. 506).** Use the proposals
$$q_i(x'|x)=p(x'_i|x_{-i})\,\mathbb I(x'_{-i}=x_{-i})\tag{12.20}$$
Acceptance ratio, using $x'_{-i}=x_{-i}$:
$$\alpha=\frac{p(x')q_i(x|x')}{p(x)q_i(x'|x)}=\frac{p(x'_i|x'_{-i})p(x'_{-i})p(x_i|x'_{-i})}{p(x_i|x_{-i})p(x_{-i})p(x'_i|x_{-i})}\tag{12.21}$$
$$=\frac{p(x'_i|x_{-i})p(x_{-i})p(x_i|x_{-i})}{p(x_i|x_{-i})p(x_{-i})p(x'_i|x_{-i})}=1\tag{12.22}$$
A 100% acceptance rate does not necessarily mean fast convergence, since one coordinate is updated at a time. Grouping correlated variables and sampling them together can help mixing significantly (p. 506).

**12.3.3 Ising models (pp. 506–508).** Pairwise MRF: $p(x)=\frac1Z\prod_{i\sim j}\psi_{ij}(x_i,x_j|\theta)$ (12.23). Full conditional: $p(x_i|x_{-i})\propto\prod_{j\in\mathrm{nbr}(i)}\psi_{ij}(x_i,x_j)$ (12.24). On a 2D grid a checkerboard colouring (Fig. 12.2) lets all black nodes be sampled in parallel, then all white nodes (p. 506). With $\psi(x_i,x_j)=\exp(Jx_ix_j)$, $x_i\in\{-1,+1\}$, and $\eta_i\triangleq\sum_{j\in\mathrm{nbr}(i)}x_j$:
$$p(x_i{=}{+}1|x_{-i})=\frac{\exp[J\eta_i]}{\exp[J\eta_i]+\exp[-J\eta_i]}=\sigma(2J\eta_i)\tag{12.25–12.27}$$
where $\sigma(u)=1/(1+e^{-u})$ (p. 507). Also $\eta_i=x_i(a_i-d_i)$, with $a_i$ neighbours agreeing and $d_i$ disagreeing; if $a_i=d_i$ the conditional is uniform (p. 507).

*Denoising:* with Ising prior $p(x)$ and per-site Gaussian likelihood, $\psi_i(x_i)=\mathcal N(y_i|x_i,\sigma^2)$:
$$p(x_i{=}{+}1|x_{-i},y)=\frac{\exp[J\eta_i]\psi_i(+1)}{\exp[J\eta_i]\psi_i(+1)+\exp[-J\eta_i]\psi_i(-1)}=\sigma\!\Big(2J\eta_i+\log\frac{\psi_i(+1)}{\psi_i(-1)}\Big)\tag{12.28–12.29}$$
Neighbours (prior) and data (likelihood) both influence the update (p. 507). Fig. 12.3 ($J=1$, noise $\sigma=2$): samples after 1 and 5 sweeps, and a posterior mean over 15 sweeps; results are similar to mean-field (p. 508).

**12.3.4 Potts models (p. 508).** $p(x)=\frac1Z\exp(-\mathcal E(x))$, $\mathcal E(x)=-J\sum_{i\sim j}\mathbb I(x_i=x_j)$ (12.30–12.31). Full conditional:
$$p(x_i=k|x_{-i})=\frac{\exp(J\sum_{n\in\mathrm{nbr}(i)}\mathbb I(x_n=k))}{\sum_{k'}\exp(J\sum_{n\in\mathrm{nbr}(i)}\mathbb I(x_n=k'))}\tag{12.32}$$
$J>0$ ("attractive") favours agreeing with neighbours. $J<0$ ("repulsive") favours differing (p. 508).

**12.3.5 Bayesian GMM (pp. 508–510).** Model: $p(z=k,x|\theta)=\pi_k\mathcal N(x|\mu_k,\Sigma_k)$ (12.33); prior $p(\theta)=\mathrm{Dir}(\pi|\alpha)\prod_k\mathcal N(\mu_k|m_0,V_0)\mathrm{IW}(\Sigma_k,S_0,\nu_0)$ (12.34) (p. 508).

*Known parameters (12.3.5.1).* Ancestral sampling would give independent samples, but for illustration use Gibbs. $p(x|z=k,\theta)=\mathcal N(x|\mu_k,\Sigma_k)$ and
$$p(z=k|x,\theta)=\frac{\pi_k\mathcal N(x|\mu_k,\Sigma_k)}{\sum_{k'}\pi_{k'}\mathcal N(x|\mu_{k'},\Sigma_{k'})}\tag{12.35}$$
Fig. 12.4 (means $-20$, $+20$): samples are autocorrelated. The chain stays in one component for a while, then jumps; independent samples from the joint would be uncorrelated (p. 509).

*Unknown parameters (12.3.5.2).* With a conditionally conjugate factored prior, the joint is (12.36–12.38) $=\big(\prod_{i}\prod_k(\pi_k\mathcal N(x_i|\mu_k,\Sigma_k))^{\mathbb I(z_i=k)}\big)\,\mathrm{Dir}(\pi|\alpha)\prod_k\mathcal N(\mu_k|m_0,V_0)\mathrm{IW}(\Sigma_k|S_0,\nu_0)$. Full conditionals (p. 510):
- $p(z_i=k|x_i,\mu,\Sigma,\pi)\propto\pi_k\mathcal N(x_i|\mu_k,\Sigma_k)$ (12.39)
- $p(\pi|z)=\mathrm{Dir}\big(\{\alpha_k+\sum_i\mathbb I(z_i=k)\}_{k=1}^K\big)$ (12.40)
- $p(\mu_k|\Sigma_k,z,x)=\mathcal N(\mu_k|m_k,V_k)$ (12.41), with $V_k^{-1}=V_0^{-1}+N_k\Sigma_k^{-1}$ (12.42), $m_k=V_k(\Sigma_k^{-1}N_k\bar x_k+V_0^{-1}m_0)$ (12.43), $N_k\triangleq\sum_i\mathbb I(z_i=k)$ (12.44), $\bar x_k\triangleq\sum_i\mathbb I(z_i=k)x_i/N_k$ (12.45)
- $p(\Sigma_k|\mu_k,z,x)=\mathrm{IW}(\Sigma_k|S_k,\nu_k)$ (12.46), with $S_k=S_0+\sum_i\mathbb I(z_i=k)(x_i-\mu_k)(x_i-\mu_k)^\top$ (12.47), $\nu_k=\nu_0+N_k$ (12.48)

**12.3.6 Metropolis within Gibbs (p. 511).** If a full conditional cannot be sampled directly, use an MH step for that coordinate: propose $x_i'\sim q(x'_i|x_i^s)$; compute $A_i=\min(1,\alpha_i)$ with
$$\alpha_i=\frac{p(x^{s+1}_{1:i-1},x_i',x^s_{i+1:D})/q(x_i'|x_i^s)}{p(x^{s+1}_{1:i-1},x_i^s,x^s_{i+1:D})/q(x_i^s|x_i')}\tag{12.49}$$
then draw $u\sim U(0,1)$ and set $x_i^{s+1}=x_i'$ if $u<A_i$, else $x_i^s$ (p. 511).

**12.3.7 Blocked Gibbs (p. 511).** Single-site updating is slow for highly correlated variables (Fig. 12.5, skewed 2D Gaussian). Move size is set by the conditional variance $\ell$. If the support has length $L$, about $O((L/\ell)^2)$ steps are needed for an independent sample. Blocked Gibbs samples groups of variables at once, making bigger moves. Example, state-space model: $p(\theta,z|x)\propto p(\theta)\prod_{t=1}^Tp(x_t|z_t,\theta)p(z_t|z_{t-1},\theta)$ (12.50). Alternate $p(\theta|z,x)$ (easy with conjugate priors, since everything is observed) and $p(z|x,\theta)$ (forwards-filtering backwards-sampling) (p. 511).

*Intuition note.* Gibbs never rejects, but a coordinate-wise walk in a narrow, tilted ridge takes tiny steps. Grouping correlated variables and sampling them jointly can make much bigger moves (p. 511).

**12.3.8 Collapsed Gibbs (pp. 512–513).** Analytically integrate out some unknowns; the sampler works in a lower-dimensional space, which tends to be more efficient and can lower variance (Section 11.6.2) (p. 512). For a GMM with a fully conjugate prior, integrate out $\mu_k,\Sigma_k,\pi$, leaving the indicators $z$. Integrating out $\pi$ makes the $z_i$ interdependent, and integrating out $\theta_k$ makes the $x_i$ interdependent (Fig. 12.6b), but the full conditionals are still computable (p. 512):
$$p(z_i=k|z_{-i},x,\alpha,\beta)\propto p(z_i=k|z_{-i},\alpha)\,p(x_i|x_{-i},z_i=k,z_{-i},\beta)\tag{12.51–12.53}$$
($\beta=(m_0,V_0,S_0,\nu_0)$.) With symmetric prior $\alpha_k=\alpha/K$:
$$p(z_{1:N}|\alpha)=\frac{\Gamma(\alpha)}{\Gamma(N+\alpha)}\prod_{k=1}^K\frac{\Gamma(N_k+\alpha/K)}{\Gamma(\alpha/K)}\tag{12.54}$$
$$p(z_i=k|z_{-i},\alpha)=\frac{p(z_{1:N}|\alpha)}{p(z_{-i}|\alpha)}=\frac{\Gamma(N+\alpha-1)}{\Gamma(N+\alpha)}\frac{\Gamma(N_{k,-i}+1+\alpha/K)}{\Gamma(N_{k,-i}+\alpha/K)}=\frac{N_{k,-i}+\alpha}{N+\alpha-1}\tag{12.55–12.56}$$
with $N_{k,-i}=N_k-1$ and $\Gamma(x+1)=x\Gamma(x)$ (p. 513). (The numerator is printed with $\alpha$; the Gamma ratio gives $N_{k,-i}+\alpha/K$ (added step), as Algorithm 12.2 uses. See Reading notes.) The second term is a posterior predictive $p(x_i|\mathcal D_{-i,k},\beta)$ (12.57), where $\mathcal D_{-i,k}$ is the data in cluster $k$ without $x_i$. It is closed-form under a conjugate prior and updated by caching sufficient statistics (p. 513).

Algorithm 12.2, for each $i$ in random order: remove $x_i$'s statistics from its cluster; for each $k$ compute $p_k(x_i|\beta)$; set $p(z_i=k|z_{-i},\alpha)\propto(N_{k,-i}+\alpha/K)\,p_k(x_i)$; sample $z_i$; add $x_i$'s statistics to the new cluster (p. 513). Naive and collapsed samplers both cost $O(NKD)$ per step. The main advantage is that it extends to infinitely many components (Dirichlet process mixture) (p. 513).

### 12.4 Auxiliary variable MCMC (p. 513)
Introduce auxiliary variables $v$ so that the augmented $p(x,v)$ is easier to sample from, reducing correlation. Draw $(x^s,v^s)\sim p(x,v)$ and discard $v^s$; then $x^s\sim\sum_vp(x,v)$ (p. 513).

**12.4.1 Slice sampling (pp. 514–515).** For $p(x)=\tilde p(x)/Z_p$, add uniform $v$:
$$\hat p(x,v)=\begin{cases}1/Z_p&0\le v\le\tilde p(x)\\0&\text{otherwise}\end{cases}\tag{12.58}$$
$$\int\hat p(x,v)dv=\int_0^{\tilde p(x)}\frac1{Z_p}dv=\frac{\tilde p(x)}{Z_p}=p(x)\tag{12.59}$$
Given $x^i$: sample $v^{i+1}\sim U_{[0,\tilde p(x^i)]}$ (12.60); form the slice $A^{i+1}=\{x:\tilde p(x)\ge v^{i+1}\}$; sample $x^{i+1}$ uniformly from it (Fig. 12.7a) (p. 515). The slice can be found by *stepping out*: grow an interval until its endpoints leave the slice, then use rejection sampling in it (details in [Nea03]) (p. 515). For $D$ dimensions, add one auxiliary variable per dimension, so $2D$ sampling operations per joint sample. Advantage over Gibbs on the original distribution: it needs only the unnormalized joint, not full conditionals (p. 515). Fig. 12.8: binomial logistic regression $y_i\sim\mathrm{Bin}(n_i,\mathrm{logit}(\beta_1+\beta_2x_i))$ with a vague Gaussian prior; the slice-sampling posterior closely matches a grid approximation (p. 515).

**12.4.2 Swendsen–Wang (pp. 515–517).** Ising model $p(x)=\frac1Z\prod_e\Psi(x_e)$, edge potential $\begin{pmatrix}e^J&e^{-J}\\e^{-J}&e^J\end{pmatrix}$, $x_i\in\{\pm1\}$. Gibbs is slow for large $|J|$ because neighbours are strongly correlated. Swendsen–Wang mixes much faster, at least for attractive models ($J>0$) (p. 515). Add a binary *bond variable* $v_e\in\{0,1\}$ per edge, with $p(x,v)=\frac1{Z'}\prod_e\Psi(x_e,v_e)$ and
$$\Psi(x_e,v_e{=}0)=\begin{pmatrix}e^{-J}&e^{-J}\\e^{-J}&e^{-J}\end{pmatrix},\quad\Psi(x_e,v_e{=}1)=\begin{pmatrix}e^J-e^{-J}&0\\0&e^J-e^{-J}\end{pmatrix}\tag{12.61}$$
Then $\sum_{v_e}\Psi(x_e,v_e)=\Psi(x_e)$, so $\sum_vp(x,v)=p(x)$ (p. 515). Gibbs on the extended model: $p(v|x)$ factorizes over edges. If $x_i=x_j$, set $v_e=1$ with probability $1-e^{-2J}$, else $v_e=0$ (p. 516). (Added check: with equal ends, $P(v_e{=}1)=(e^J-e^{-J})/e^J=1-e^{-2J}$.) To sample $p(x|v)$: find connected components of the graph of "on" bonds (a component may be a single node), pick one uniformly at random, pick a state $\pm1$ uniformly, and set the whole component to it (Fig. 12.9) (p. 516).

Performance, as stated: write edge strength as $J/T$. For large $T$ nodes are roughly independent and both methods work. As $T\to T_c$ (critical temperature), correlation lengths grow and Gibbs needs very long to give independent samples. At low temperature the typical states are all-on or all-off, and Gibbs switches between them with exponentially small frequency; SW "mixes rapidly at all temperatures" (p. 516). If any $J<0$ the system is *frustrated*, with exponentially many modes even at low temperature. SW works poorly there, and sampling such systems is provably hard for any algorithm (pp. 516–517).

*Intuition note.* Bonds glue same-coloured neighbours into clusters, and a whole cluster flips at once. That is a far bigger move than flipping one site against its aligned neighbours.

### 12.5 Hamiltonian Monte Carlo (HMC)
Many MCMC methods do poorly in high dimensions because they rely on local random perturbations. HMC uses gradient information; it is an auxiliary-variable method derived from physics (p. 517).

**12.5.1 Hamiltonian mechanics (pp. 517–518).** Position $\theta\in\mathbb R^D$, momentum $v\in\mathbb R^D$; $(\theta,v)$ lives in *phase space*. The Hamiltonian (total energy) is
$$\mathcal H(\theta,v)\triangleq\mathcal E(\theta)+\mathcal K(v)\tag{12.62}$$
with potential energy $\mathcal E(\theta)=-\log\tilde p(\theta)$ (12.63), where $\tilde p$ may be unnormalized, e.g. $p(\theta,\mathcal D)$, and kinetic energy $\mathcal K(v)=\frac12v^\top\Sigma^{-1}v$ (12.64), with $\Sigma$ positive definite, the *inverse mass matrix* (p. 517). Trajectories of constant energy solve Hamilton's equations:
$$\frac{d\theta}{dt}=\frac{\partial\mathcal H}{\partial v}=\frac{\partial\mathcal K}{\partial v},\qquad\frac{dv}{dt}=-\frac{\partial\mathcal H}{\partial\theta}=-\frac{\partial\mathcal E}{\partial\theta}\tag{12.65}$$
Energy is conserved:
$$\frac{d\mathcal H}{dt}=\sum_{i=1}^D\Big[\frac{\partial\mathcal H}{\partial\theta_i}\frac{d\theta_i}{dt}+\frac{\partial\mathcal H}{\partial v_i}\frac{dv_i}{dt}\Big]=\sum_{i=1}^D\Big[\frac{\partial\mathcal H}{\partial\theta_i}\frac{\partial\mathcal H}{\partial v_i}-\frac{\partial\mathcal H}{\partial\theta_i}\frac{\partial\mathcal H}{\partial v_i}\Big]=0\tag{12.66}$$
For small enough time steps the map $(\theta(t),v(t))\mapsto(\theta(t+s),v(t+s))$ is invertible and volume preserving (Jacobian determinant 1; proof in [BZ20]). These facts matter later for the MCMC algorithm (p. 518).

**12.5.2 Integrating Hamilton's equations (pp. 518–519).** With step size $\eta$:
- *Euler:* $v_{t+1}=v_t-\eta\,\partial\mathcal E(\theta_t)/\partial\theta$ (12.67); $\theta_{t+1}=\theta_t+\eta\,\partial\mathcal K(v_t)/\partial v$ (12.68). With (12.64) the text writes the second as $\theta_{t+1}=\theta_t+\eta\Sigma^{-1}v_{t+1}$ (12.69) (p. 518; see Reading notes).
- *Modified Euler:* update momentum first, $v_{t+1}=v_t-\eta\,\partial\mathcal E(\theta_t)/\partial\theta$ (12.70), then position with the new momentum, $\theta_{t+1}=\theta_t+\eta\,\partial\mathcal K(v_{t+1})/\partial v$ (12.71). Slightly more accurate, but its asymmetry causes theoretical problems (p. 518).
- *Leapfrog* (symmetrized modified Euler): half momentum step, full position step, half momentum step:
$$v_{t+1/2}=v_t-\frac\eta2\frac{\partial\mathcal E(\theta_t)}{\partial\theta}\tag{12.72}$$
$$\theta_{t+1}=\theta_t+\eta\frac{\partial\mathcal K(v_{t+1/2})}{\partial v}\tag{12.73}$$
$$v_{t+1}=v_{t+1/2}-\frac\eta2\frac{\partial\mathcal E(\theta_{t+1})}{\partial\theta}\tag{12.74}$$
Many leapfrog steps equal a half-step of $v$ at each end, with alternating full steps in between (p. 519). Higher-order integrators exist; they are more accurate but take more steps (p. 519).

**12.5.3 The HMC algorithm (pp. 519–520).** Target on the expanded space $(\theta,v)$:
$$p(\theta,v)=\frac1Z\exp[-\mathcal H(\theta,v)]=\frac1Z\exp\Big[-\mathcal E(\theta)-\tfrac12v^\top\Sigma v\Big]\tag{12.75}$$
and $p(\theta)=\int p(\theta,v)dv=\frac1{Z_q}e^{-\mathcal E(\theta)}$ (12.76), so discarding $v$ leaves the desired marginal (p. 519). One iteration from $(\theta_{t-1},v_{t-1})$:
1. Set $\theta'_0=\theta_{t-1}$ and sample $v'_0\sim\mathcal N(0,\Sigma)$.
2. Run $L$ leapfrog steps to the proposal $(\theta^*,v^*)=(\theta'_L,v'_L)$.
3. If the energy has not stayed the same, the run has *diverged*; reject. Otherwise accept with
$$\alpha=\min\Big(1,\frac{p(\theta^*,v^*)}{p(\theta_{t-1},v_{t-1})}\Big)=\min\big(1,\exp[-\mathcal H(\theta^*,v^*)+\mathcal H(\theta_{t-1},v_{t-1})]\big)\tag{12.77}$$
The transition probabilities cancel because the proposal is reversible. The momentum need not be kept after the step (p. 519).

Algorithm 12.3: for $t=1{:}T$: draw $v_{t-1}\sim\mathcal N(0,\Sigma)$; $(\theta'_0,v'_0)=(\theta_{t-1},v_{t-1})$; $v'_{1/2}=v'_0-\frac\eta2\nabla\mathcal E(\theta'_0)$; for $l=1{:}L-1$: $\theta'_l=\theta'_{l-1}+\eta\Sigma^{-1}v'_{l-1/2}$, $v'_{l+1/2}=v'_{l-1/2}-\eta\nabla\mathcal E(\theta'_l)$; then $\theta'_L=\theta'_{L-1}+\eta\Sigma^{-1}v'_{L-1/2}$, $v'_L=v'_{L-1/2}-\frac\eta2\nabla\mathcal E(\theta'_L)$; propose $(\theta^*,v^*)=(\theta'_L,v'_L)$; compute $\alpha$ as in (12.77); set $\theta_t=\theta^*$ with probability $\alpha$, else $\theta_{t-1}$ (p. 520).

*Why resample momentum (p. 520):* $\mathcal H$ stays approximately constant along a trajectory. With $\mathcal H=\mathcal E(\theta)+\frac12v^\top\Sigma v=h$, we have $\mathcal E(\theta)\le h$ along it, so states with $\mathcal E(\theta)>h$ are unreachable. A fresh random momentum each iteration is needed to explore the whole space (ergodicity).

*Intuition note.* Gradient information turns the proposal into a long, smooth glide along a constant-energy path instead of a blind local step. The MH acceptance test is then applied to the proposed endpoint, and the proposal is rejected if the energy has not stayed the same (p. 519).

**12.5.4 Tuning (pp. 520–521).** Three hyperparameters: number of leapfrog steps $L$, step size $\eta$, covariance $\Sigma$.
- *$L$:* large enough to explore the energy level set but not double back (wasted, correlated). The no-U-turn sampler (NUTS) [HG14] chooses $L$ adaptively (p. 520).
- *$\eta$:* with $\Sigma=\mathbf I$, roughly the width of $\mathcal E$ in its most constrained direction; for a locally quadratic potential, the square root of the smallest marginal standard deviation of the local covariance. Too large: moves are likely to be rejected (potential energy rises too much). Too small: very slow (p. 520). Heuristic from [BZ20]: $\Sigma=\mathbf I$, $L=1$, vary $\eta$ until acceptance is 40%–80%. Cyclical learning-rate schedules can handle different scales in different regions (p. 521).
- *$\Sigma$:* run with $\Sigma=\mathbf I$ during warm-up until burned in, then estimate $\Sigma=\mathbb E[(\theta-\bar\theta)(\theta-\bar\theta)^\top]$. NeuTra HMC [Hof+19] learns an inverse autoregressive flow to map the warped target to an isotropic Gaussian, "often an order of magnitude faster" than vanilla HMC (p. 521).

**12.5.5 Riemann manifold HMC (p. 521).** If $\Sigma$ depends on $\theta$, the method is RM-HMC. Choices: the Hessian $\Sigma(\theta)=\nabla^2\mathcal E(\theta)$ (12.78), which is not always positive definite, or the Fisher information $\Sigma(\theta)=-\mathbb E_{p(x|\theta)}[\nabla^2\log p(x|\theta)]$ (12.79). Kinetic energy: $\mathcal K(\theta,v)=\frac12\log((2\pi)^D|\Sigma(\theta)|)+\frac12v^\top\Sigma(\theta)v$ (12.80). The $\theta$ and $v$ updates are no longer separable, so it is harder to implement and not widely used (p. 521).

**12.5.6 Langevin Monte Carlo / MALA (pp. 521–522).** HMC with $L=1$ is Langevin Monte Carlo (LMC), or the Metropolis adjusted Langevin algorithm (MALA) (Algorithm 12.4, p. 522). Dropping the MH step gives
$$\theta_t=\theta_{t-1}-\frac{\eta^2}2\Sigma^{-1}\nabla\mathcal E(\theta_{t-1})+\eta\Sigma^{-1}v_{t-1}=\theta_{t-1}-\frac{\eta^2}2\Sigma^{-1}\nabla\mathcal E(\theta_{t-1})+\eta\sqrt{\Sigma^{-1}}\,\epsilon_{t-1}\tag{12.81–12.82}$$
with $v_{t-1}\sim\mathcal N(0,\Sigma)$, $\epsilon_{t-1}\sim\mathcal N(0,\mathbf I)$. This is gradient descent plus noise. With $\Sigma$ = Fisher matrix it is natural gradient descent plus noise. With stochastic gradients it is SGLD (Section 12.7.1) (p. 522). With $\Sigma=\mathbf I$, $\eta=\sqrt2$, the continuous-time limit is Langevin diffusion
$$d\theta_t=-\nabla\mathcal E(\theta_t)dt+\sqrt2\,dB_t\tag{12.83}$$
($B_t$ is $D$-dimensional Brownian motion). Sampling with it is the unadjusted Langevin algorithm (ULA) (p. 522).

**12.5.7 SGD and Langevin sampling (pp. 522–523).** Loss $\mathcal L(\theta)=\sum_{n=1}^N\mathcal L_n(\theta)$ (12.84), minibatch gradient $\nabla_B\mathcal L(\theta)=\frac1B\sum_{n\in\mathcal S}\nabla\mathcal L_n(\theta)$ (12.85), indices drawn with replacement. Define the scaled minibatch error $v_t\triangleq\sqrt\eta(\nabla\mathcal L(\theta_t)-\nabla_B\mathcal L(\theta_t))$ (12.86), the *diffusion term*. Then
$$\theta_{t+1}=\theta_t-\eta\nabla_B\mathcal L(\theta_t)=\theta_t-\eta\nabla\mathcal L(\theta_t)+\sqrt\eta\,v_t\tag{12.87}$$
Mean: $\mathbb E[\nabla_B\mathcal L]=\frac1B\sum_j\mathbb E[\nabla\mathcal L_{i_j}]=\nabla\mathcal L(\theta)$ (12.88), so $v_t$ has mean 0. Variance: $\mathbb V[\nabla_B\mathcal L]=\frac1{B^2}\sum_j\mathbb V[\nabla\mathcal L_{i_j}]$ (12.89), where
$$\mathbb V[\nabla\mathcal L_{i_j}]=\mathbb E[\nabla\mathcal L_{i_j}\nabla\mathcal L_{i_j}^\top]-\mathbb E[\nabla\mathcal L_{i_j}]\mathbb E[\nabla\mathcal L_{i_j}]^\top=\Big(\frac1N\sum_n\nabla\mathcal L_n\nabla\mathcal L_n^\top\Big)-\nabla\mathcal L\nabla\mathcal L^\top\triangleq\mathbf D(\theta)\tag{12.90–12.91}$$
($\mathbf D$ = *diffusion matrix*). Hence $\mathbb V[v_t]=\frac\eta B\mathbf D(\theta_t)$ (p. 523). [LTW15] prove (assuming a Lipschitz continuous loss) that
$$d\theta(t)=-\nabla\mathcal L(\theta(t))dt+\sqrt{\tfrac\eta B\mathbf D(\theta_t)}\,dB(t)\tag{12.92}$$
is a first-order approximation of minibatch SGD. So minibatch noise makes SGD act like a Langevin sampler. The noise scale $\tau=\eta/B$ plays the role of *temperature*. A smaller batch is like a higher temperature; the text says the added noise helps SGD avoid narrow ravines and spend time in flat minima with better generalization [Kes+17] (p. 523).

**12.5.8 Constrained parameters (start, p. 523).** HMC needs all latent quantities continuous and unconstrained ($\theta\in\mathbb R^D$), so discrete latents must be marginalized out (some recent work relaxes this). Example: write the GMM likelihood without discrete latents, $p(x_n|\theta)=\sum_{k=1}^K\pi_k\mathcal N(x_n|\mu_k,\Sigma_k)$ (12.93), the "collapsed" model of Fig. 12.10(b). This is the opposite of §12.3.8, which integrated out continuous parameters (p. 523). The unit's pages end mid-sentence here.

## Toy example (ours, not from the text)
Target on states $\{1,2,3\}$ with unnormalized $\tilde p=(1,2,1)$, so $Z=4$ and $p^*=(0.25,0.5,0.25)$. Proposal: from any state, propose each *other* state with probability $\tfrac12$. It is symmetric, so $A=\min(1,\tilde p(x')/\tilde p(x))$ (12.1), and $Z$ is never used.
- From 1: $P(1\to2)=\tfrac12\min(1,2/1)=0.5$; $P(1\to3)=\tfrac12\min(1,1/1)=0.5$; $P(1\to1)=0$.
- From 2: $P(2\to1)=\tfrac12\min(1,1/2)=0.25$; $P(2\to3)=0.25$; $P(2\to2)=1-0.5=0.5$.
- From 3: $P(3\to1)=0.5$; $P(3\to2)=\tfrac12\min(1,2)=0.5$; $P(3\to3)=0$.

Detailed balance (12.7): $p^*(1)P(1\to2)=0.25\cdot0.5=0.125=0.5\cdot0.25=p^*(2)P(2\to1)$. Likewise $p^*(2)P(2\to3)=0.125=0.25\cdot0.5=p^*(3)P(3\to2)$ and $p^*(1)P(1\to3)=0.125=p^*(3)P(3\to1)$. Stationarity at state 1: $0.25\cdot0+0.5\cdot0.25+0.25\cdot0.5=0.25=p^*(1)$ ✓. The chain visits state 2 half the time even though it never "knew" $Z$, and downhill moves ($2\to1$, accepted w.p. 0.5) occur.

## Concepts
- [[metropolis-hastings]] — propose from $q$, accept with $\min(1,\alpha)$; normalizer cancels (pp. 500–501)
- [[markov-chain-monte-carlo]] — random walk whose stationary distribution is the target; correlated samples (p. 499)
- [[detailed-balance]] (new) — $p(x'|x)p^*(x)=p(x|x')p^*(x')$; implies $p^*$ is stationary (p. 501)
- [[proposal-distribution]] (new) — kernel $q(x'|x)$; valid if it covers the target's support (pp. 500–501)
- [[random-walk-metropolis]] (new) — MH with $\mathcal N(x,\tau^2\mathbf I)$ proposal; $\tau$ sets mixing (p. 503)
- [[gibbs-sampling]] — resample each variable from its full conditional; MH with acceptance 1 (pp. 505–506)
- [[blocked-gibbs]] (new) — update groups of variables jointly to speed mixing (p. 511)
- [[collapsed-gibbs-sampler]] (new) — Gibbs after analytically integrating out some unknowns (p. 512)
- [[auxiliary-variable-mcmc]] (new) — sample augmented $p(x,v)$, discard $v$ (p. 513)
- [[slice-sampling]] (new) — uniform height variable $v$; sample $x$ from $\{x:\tilde p(x)\ge v\}$ (pp. 514–515)
- [[swendsen-wang]] (new) — bond variables on Ising edges; flip whole clusters (pp. 515–516)
- [[hamiltonian-monte-carlo]] — momentum auxiliary variable; leapfrog trajectory plus MH correction (pp. 517–520)
- [[leapfrog-integrator]] (new) — symmetric half-full-half integrator for Hamilton's equations (p. 519)
- [[langevin-monte-carlo]] (new) — HMC with $L=1$ (MALA); dropping the MH step gives an unadjusted update, and with $\Sigma=\mathbf I$, $\eta=\sqrt2$ the continuous-time limit is Langevin diffusion (ULA) (pp. 521–522)
- [[sgd-langevin-connection]] (new) — minibatch SGD ≈ Langevin SDE with temperature $\eta/B$ (p. 523)

## Canonical instances
- [[gmm-1d-two-mode-sampling]] — RWM vs Gibbs on a two-component 1D mixture (pp. 503, 509)
- [[ising-image-denoising]] — Gibbs with Ising prior and Gaussian local evidence (p. 507)
- [[bayesian-gmm-gibbs]] — full conditionals for $z,\pi,\mu,\Sigma$ (p. 510)
- [[binomial-logistic-regression-slice]] — slice sampling vs grid posterior (p. 515)

## Bridges (candidates)
- [structural-analogy] Gibbs sampling ↔ optimization: coordinate descent (author's own comparison, p. 505).
- [structural-analogy] Collapsed Gibbs ↔ Monte Carlo variance reduction: lower-dimensional sampling lowers variance (p. 512).
- [structural-analogy] Noisy SGD ↔ Langevin sampling: both are gradient steps plus noise; temperature $\eta/B$ (p. 523).
- [structural-analogy] Ising conditional $\sigma(2J\eta_i)$ ↔ logistic regression: the same sigmoid of a linear score (p. 507).
- [metaphor] HMC's rolling particle ↔ physics orbits: energy conservation guides the proposal (p. 518).

## Questions this raises
- When is an MH chain guaranteed ergodic and irreducible, and how is mixing time measured? (The text defers diagnostics to §12.6.)
- The 0.234 acceptance rate is proved for Gaussian posteriors (p. 503); what happens for other targets?
- How does adapting proposals (HMC warm-up, adaptive MCMC) keep the correct stationary distribution?
- If SGD is a Langevin sampler, how far can minibatch noise be treated as a posterior-sampling noise?

## Reading notes
- This is part 1/2 of Chapter 12. It starts at §12.1 (printed p. 499) and ends at printed p. 523, mid-way through §12.5.8, in the middle of a sentence ("For…"). Later sections (the rest of §12.5.8, and §12.6 and §12.7, which this part only cross-references for burn-in, autocorrelation and SGLD) are not covered here.
- Printed page = PDF page − 34.
- Eq. (12.25) as printed has a typo in the denominator ("$\psi(x_i{=}{-}1,x_i)$", meant $x_j$). The text after (12.27) writes "$d_t$" for $d_i$.
- Eq. (12.56) as printed shows numerator $N_{k,-i}+\alpha$. The preceding Gamma ratio gives $N_{k,-i}+\alpha/K$, which Algorithm 12.2 uses.
- Eq. (12.69) is stated for Euler's method with $v_{t+1}$, while (12.68) uses $v_t$; the text writes it this way.
- Eqs. (12.75) and (12.80) use $v^\top\Sigma v$ while (12.64) uses $\Sigma^{-1}$ (reproduced as printed). Algorithm 12.3 samples $v\sim\mathcal N(0,\Sigma)$ and updates with $\Sigma^{-1}v$.
- In the proof of Thm 12.2.1, the cases are stated as $<$ / $\ge$, then the proof assumes strict $>$ ("without loss of generality").
- Eqs. (12.51)–(12.52) show struck-out terms in the image; I followed the final form (12.53).
- Equations were checked against the page images.
