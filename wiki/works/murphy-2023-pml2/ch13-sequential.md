---
id: murphy-2023-pml2/ch13-sequential
work: murphy-2023-pml2
unit: "13 Sequential Monte Carlo"
pages: 543-572
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
# Sequential Monte Carlo (Murphy, Ch. 13)

## L0 — One line
Sequential Monte Carlo grows weighted samples ("particles") through a sequence of related distributions, using resampling to stop the weights collapsing, and the same machinery serves both state-space filtering and sampling from static targets.

## L1 — The gist (≤ 120 words)
How can we sample from a sequence of related distributions when plain importance sampling in a growing state space fails? The chapter builds the particle filter: sequential importance sampling, then resampling (adaptive, triggered by the effective sample size), then better proposals and Rao-Blackwellization for state-space models. It then reuses the same machinery as "SMC samplers" for static targets, via likelihood or data tempering, rare-event thresholds, ABC and variational lower bounds. SMC also estimates the normalizing constant and can handle multimodal targets where HMC (Hamiltonian Monte Carlo) stalls, so it is an alternative to MCMC.

**Prerequisites:** importance sampling; state-space models and the Kalman filter; MCMC (Metropolis–Hastings); KL divergence; Gaussian conditioning.

## L2 — Key ideas (5–10 bullets)
- SMC samples a sequence $\pi_t(z_{1:t})=\tilde\gamma_t/Z_t$. It is called particle filtering when each marginal matters, and an SMC sampler when only the final distribution matters (p. 543).
- Sequential importance sampling (SIS) updates each particle's weight recursively by multiplying it by an incremental weight. It suffers weight degeneracy: nearly all the weight ends up on one particle (p. 547).
- Resampling (SIS with resampling, SISR) does not suffer weight degeneracy but does suffer path degeneracy, a loss of diversity about the past. Adaptive resampling, done only when the effective sample size (ESS: how many equally weighted particles the weighted set is worth) falls below a threshold, is the compromise (pp. 548–553).
- The bootstrap filter proposes from the dynamics prior. The locally optimal proposal conditions on the current observation. Approximations use extended/unscented Kalman filters (EKF/UKF), a Laplace (Gaussian) approximation of the likelihood, or an inner SMC run (nested SMC) (pp. 549, 554–557).
- Rao-Blackwellized PF samples only the part of the state that cannot be integrated analytically and handles the rest exactly, e.g. mixture of Kalman filters and FastSLAM (pp. 557–563).
- An SMC sampler needs a forward kernel (proposes new samples) and a backward kernel (defines the distribution over the past variables). With the time-reversed MCMC kernel as backward kernel, the incremental weight is $\tilde\gamma_t(z_{t-1})/\tilde\gamma_{t-1}(z_{t-1})$ (pp. 564–565).
- Likelihood tempering, data tempering (IBIS, iterated batch importance sampling), rare-event thresholds and ABC (approximate Bayesian computation) are different choices of intermediate targets, and SMC succeeds on a bimodal target where the gradient-based samplers HMC and NUTS get stuck (pp. 565–569).
- Training with $\mathbb E[\log\hat Z_T]$, a lower bound on the log evidence, gives variational SMC (FIVO, filtering variational objective). Smoothing targets with a learned lookahead ("twisting") function (SIXO) give a bound that the authors of that method prove tight under stated conditions (pp. 569–571).

## L3 — Walkthrough

### 13.1 Introduction (pp. 543–545)
**Problem (13.1.1).** SMC targets a sequence
$$\pi_t(z_{1:t})=\frac{1}{Z_t}\tilde\gamma_t(z_{1:t}),\quad t=1{:}T \tag{13.1}$$
with $\tilde\gamma_t$ the unnormalized target and $Z_t$ its normalizer. If each marginal $\pi_t(z_t)$ matters (e.g. filtering in a state-space model, SSM), this is **particle filtering** ("particle" = sample). If only $\pi_T$ matters and intermediate steps are computational devices, it is an **SMC sampler** (p. 543). The presentation follows [NLS19], stressing that we sample sequences of related variables (p. 543).

**Filtering in SSMs (13.1.2).** For a Markov SSM,
$$\pi_T(z_{1:T})\propto p(z_{1:T},y_{1:T})=p(z_1)p(y_1|z_1)\prod_{t}p(z_t|z_{t-1})p(y_t|z_t) \tag{13.2}$$
and a common target is $\tilde\gamma_t(z_{1:t})=p(z_{1:t},y_{1:t})$ (13.3). It is a distribution over an ever-growing sequence, but often only $\tilde\gamma_t(z_t)$ is needed, which avoids storing history (p. 544).

*Example (p. 544).* 2d nonlinear tracking:
$$p(z_t|z_{t-1})=\mathcal N(z_t|f(z_{t-1}),q\mathbf I),\ p(y_t|z_t)=\mathcal N(y_t|z_t,r\mathbf I),\ f(z)=(z_1+\Delta\sin z_2,\ z_2+\Delta\cos z_1) \tag{13.4}$$
Here $\Delta, q, r$ are fixed constants. A bootstrap filter with 2000 samples estimates the posterior mean (Fig. 13.1b) (p. 544).

*Non-Markovian models.* If $z_t$ depends on all past states, the target is
$$\tilde\gamma_t(z_{1:t})=p(z_1)p(y_1|z_1)\prod_{s}p(z_s|z_{1:s-1})p(y_s|z_{1:s}) \tag{13.5}$$
Example (from [NLS19]): $p(z_t|z_{1:t-1})=\mathcal N(z_t|\phi z_{t-1},q)$ and $p(y_t|z_{1:t})=\mathcal N(y_t|\sum_{s=1}^t\beta^{t-s}z_s,r)$ (13.6). With $\beta=0$ this is a linear-Gaussian SSM. Larger $\beta$ means more dependence on the past and a harder problem (p. 545).

**Static problems (13.1.3).** For a fixed iid dataset $\mathcal D$, $p(z|\mathcal D)\propto p(z)\prod_n p(y_n|z)$. Two ways to make a sequence (p. 545):
- *Data tempering:* $\tilde\gamma_t(z_t)=p(z_t)p(y_{1:t}|z_t)$, so $T=N$ data points.
- *Likelihood tempering:* $\tilde\gamma_t(z_t)=p(z_t)p(\mathcal D|z_t)^{\tau_t}$, with temperature $\tau_t$ rising from 0 to 1.

These marginal targets are then expanded to joint targets over sequences (Section 13.6) so that particle filtering applies (p. 545).

### 13.2 Particle filtering (pp. 545–553)

**13.2.1 Importance sampling.** Self-normalized importance sampling (SNIS) estimates $\pi_t(\varphi)=\mathbb E_{\pi_t}[\varphi_t]$ using samples $z^i_{1:t}\sim q_t$, $i=1{:}N_s$ (p. 546):
$$\pi_t(\varphi)\approx\frac1{\hat Z_t}\frac1{N_s}\sum_i\tilde w_t(z^i_{1:t})\varphi_t(z^i_{1:t}),\quad \tilde w^i_t=\frac{\tilde\gamma_t(z^i_{1:t})}{q_t(z^i_{1:t})},\quad \hat Z_t=\frac1{N_s}\sum_i\tilde w^i_t \tag{13.8–13.10}$$
With normalized weights $W^i_t=\tilde w^i_t/\sum_j\tilde w^j_t$ (13.11) this is $\mathbb E_{\pi_t}[\varphi_t]\approx\sum_iW^i_t\varphi_t(z^i_{1:t})$ (13.12). The target itself is approximated by $\hat\pi_t=\sum_iW^i_t\delta(z_{1:t}-z^i_{1:t})$ (13.13).
Problem: the state space is high-dimensional and grows with $t$, so a good proposal is hard to find and most samples get negligible weight (p. 546).

**13.2.2 Sequential importance sampling (SIS).** Use an autoregressive proposal $q_t(z_{1:t})=q_{t-1}(z_{1:t-1})q_t(z_t|z_{1:t-1})$ (13.14), i.e. reuse old samples and extend each by one step ("growing the chain") (p. 547). Weights are recursive:
$$\tilde w_t=\frac{\tilde\gamma_t}{q_t}=\frac{\tilde\gamma_{t-1}(z_{1:t-1})}{\tilde\gamma_{t-1}(z_{1:t-1})}\frac{\tilde\gamma_t(z_{1:t})}{q_t(z_t|z_{1:t-1})q_{t-1}(z_{1:t-1})}=\tilde w_{t-1}(z_{1:t-1})\,\alpha_t(z_{1:t}) \tag{13.15–13.17}$$
$$\alpha_t(z_{1:t})=\frac{\tilde\gamma_t(z_{1:t})}{\tilde\gamma_{t-1}(z_{1:t-1})\,q_t(z_t|z_{1:t-1})}\quad\text{(incremental importance weight)} \tag{13.18}$$
In practice weights are computed in log space with the log-sum-exp trick. Algorithm 13.1 is the loop: sample $z_t^i$, compute $\alpha^i_t$, set $\tilde w^i_t=\tilde w^i_{t-1}\alpha^i_t$, normalize (p. 548).
For SSMs, $\tilde\gamma_t=p(y_t|z_{1:t})p(z_t|z_{1:t-1})\tilde\gamma_{t-1}$ (13.19–13.20), so
$$\alpha_t=\frac{p(y_t|z_{1:t})p(z_t|z_{1:t-1})}{q_t(z_t|z_{1:t-1})} \tag{13.21}$$
(p. 547).

*Weight degeneracy / particle impoverishment.* Most weights become near zero, so the posterior is approximated by one particle. The reason given: each particle must explain the whole observation sequence, and the product of likelihood terms makes weight differences grow exponentially. Fig. 13.2a shows this for (13.6) with $(\phi,q,\beta,r)=(0.9,10,0.5,1.0)$, $N_s=5$ (pp. 547–548).

> **Intuition note.** SIS never discards bad guesses, so errors multiply over time. After a while one lucky trajectory carries essentially all the weight.

**13.2.3 SIS with resampling (SISR).** Idea: first select the $N_s$ "fittest" particles by sampling from the old posterior, then let survivors grow one step. The proposal is
$$q^{\rm SISR}_t(z_{1:t})=\hat\pi_{t-1}(z_{1:t-1})\,q_t(z_t|z_{1:t-1}) \tag{13.22}$$
instead of SIS's $q^{\rm SIS}_{t-1}q_t$ (13.23) (p. 548). Algorithm 13.2: compute ancestors by resampling, permute particles, reset old weights to $1/N_s$, extend, and set $\tilde w^i_t=\alpha^i_t$. Weights are computed as if the proposal were $\tilde\gamma_{t-1}(z^i_{1:t-1})q_t(z^i_t|z^i_{1:t-1})$ although $\hat\pi_{t-1}$ was used. The text gives an "intuitive reason" for validity: $\hat\pi_{t-1}$ was an unbiased estimate of the previous target (p. 549).

*13.2.3.1 Bootstrap filter.* Take $q_t(z_t|z_{1:t-1})=p(z_t|z_{1:t-1})$ (13.24). Then (13.21) gives
$$\alpha_t=\frac{p(y_t|z_t)p(z_t|z_{t-1})}{p(z_t|z_{t-1})}=p(y_t|z_{1:t}) \tag{13.25}$$
(the source's last step; for a Markov SSM this is $p(y_t|z_t)$). Other names: survival of the fittest, condensation (p. 549). It is useful when one can sample from the dynamics but cannot evaluate the transition pointwise (e.g. implicit models defined by differential equations). In general, proposals using $y_t$ are far more efficient (p. 550).

*13.2.3.2 Path degeneracy.* With resampling, diversity of active particles is much better (Fig. 13.3a). But the number of surviving ancestral lineages may drop quickly, so the distribution over the past loses diversity. In Fig. 13.3b all $N_s=5$ final sequences share one ancestor $z^1_1$. The time at which all paths meet when traced backwards is the *coalescence time* (p. 550).

*13.2.3.3 Normalizing constant.* $Z_T=p(y_{1:T})=\prod_tp(y_t|y_{1:t-1})$ is estimated by
$$\hat Z_T=\prod_t\hat Z_t,\quad\hat Z_t=\frac1{N_s}\sum_i\tilde w^i_t=\hat Z_{t-1}\widehat{(Z_t/Z_{t-1})},\quad \widehat{Z_t/Z_{t-1}}=\frac{\sum_i\tilde w^i_t}{\sum_i\tilde w^i_{t-1}} \tag{13.26–13.28}$$
This marginal-likelihood estimate is "very useful" for parameter estimation (pp. 550–551).

**13.2.4 Resampling methods.** Sampling an index $A$ with probabilities $W^i_t$ gives $\mathbb E[f(z_t^A)|y_{1:t}]=\sum_iW^i_tf(z_t^i)$ (13.30). For $N$ independent indices,
$$\mathbb E_{A_{1:N}}\Big[\frac1N\sum_if(z_t^{A_i})\Big]=\sum_iW^i_tf(z^i_t) \tag{13.32}$$
So resampling (dropping low-weight, duplicating high-weight particles) gives the same result in expectation. Variance depends on the method (p. 551).

- *Inverse cdf:* form the cdf of the weights. Uniform $U^i$ maps to index $a$ if $\sum_{j<a}W^j\le U^i<\sum_{j\le a}W^j$ (13.33). With $U^i$ sorted this costs $O(N)$ rather than $O(N^2)$. Notation: $A_{1:N}=\mathrm{icdf}(W^{1:N},U^{1:N})$ (pp. 551–552). In Fig. 13.4, $A^{1:3}=(1,2,2)$ (p. 552).
- *Multinomial:* $U$ is an ordered set of $N$ uniform draws. With equal weights the number of offspring $\mathcal W^n\sim\mathrm{Bin}(N,1/N)$, so $P(\mathcal W^n=0)=(1-1/N)^N\approx e^{-1}\approx0.37$. A given particle disappears with ~37% chance despite equal weights (p. 552).
- *Stratified:* $U^i\sim\mathrm{Unif}((i-1)/N_s,\,i/N_s)$ (13.34) (p. 552).
- *Systematic:* one shared $u\sim\mathrm{Unif}(0,1)$, $U^i=\frac{i-1}{N_s}+\frac u{N_s}$ (13.35) (p. 553).
- *Comparison:* all are unbiased. Systematic seems empirically lower variance. Stratified and a more complex method [GCW19] have better theoretical properties. Multinomial is not recommended because it has provably higher variance (p. 553).

**13.2.5 Adaptive resampling.** Never resampling gives SIS (weight degeneracy). Resampling can cause loss of diversity (path degeneracy). Compromise: resample when the effective sample size drops below a minimum such as $N/2$ (p. 553):
$$\mathrm{ESS}(W^{1:N})=\frac1{\sum_n(W^n)^2},\qquad \mathrm{ESS}(\tilde w^{1:N})=\frac{(\sum_n\tilde w^n)^2}{\sum_n(\tilde w^n)^2} \tag{13.36–13.37}$$
With $k$ weights equal to 1 and $N-k$ equal to 0, ESS $=k$, so ESS lies between 1 and $N$. This ESS differs from the MCMC ESS, which accounts for autocorrelation (p. 553). Algorithm 13.3 (generic SMC): extend, compute $\alpha$, update weights and $\hat Z_t$, resample if ESS is below ESS$_{\min}$, normalize (p. 554).

> **Intuition note.** ESS counts how many equally weighted particles the current weighted set is "worth". Resampling only when ESS is low avoids needless loss of diversity.

### 13.3 Proposal distributions (pp. 554–557)
**13.3.1 Locally optimal proposal.** Define $q_t^*$ as the minimizer of
$$D_{KL}(\pi_{t-1}(z_{1:t-1})q_t(z_t|z_{1:t-1})\,\|\,\pi_t(z_{1:t}))=\mathbb E_{\pi_{t-1}q_t}[\log q_t(z_t|z_{1:t-1})-\log\pi_t(z_t|z_{1:t-1})]+\text{const}=\mathbb E_{\pi_{t-1}q_t}\big[D_{KL}(q_t(z_t|z_{1:t-1})\|\pi_t(z_t|z_{1:t-1}))\big]+\text{const} \tag{13.38–13.41}$$
(the terms not involving $q_t$ are constants — added step). The minimum is
$$q^*_t(z_t|z_{1:t-1})=\pi_t(z_t|z_{1:t-1})=\frac{\tilde\gamma_t(z_{1:t})}{\tilde\gamma_t(z_{1:t-1})},\ \ \tilde\gamma_t(z_{1:t-1})=\int\tilde\gamma_t(z_{1:t})dz_t \tag{13.42}$$
In SSMs this is $p(z_t|z_{1:t-1},y_{1:t})$: propose using all data including $y_t$ (a **guided particle filter**), which "will be better" than the bootstrap filter. In general it is intractable (p. 554).

> **Intuition note.** The best next step is the one that already knows the newest observation. The bootstrap filter ignores $y_t$ while proposing and only corrects afterwards through weights.

**13.3.2 EKF/UKF proposals.** (Extended/unscented Kalman filters linearize or sigma-point-approximate nonlinear models.) Assume $z_t=f(z_{t-1})+q_t$, $y_t=h(z_t)+r_t$. For each particle $i$, approximate the joint of $(z_t,y_t)$ given its history as Gaussian:
$$p(z_t,y_t|z^i_{1:t-1})\approx\mathcal N\Big(\binom{z_t}{y_t}\Big|\hat\mu^i,\hat\Sigma^i\Big),\ \hat\mu^i=\binom{\hat\mu^i_z}{\hat\mu^i_y},\ \hat\Sigma^i=\begin{pmatrix}\hat\Sigma^i_{zz}&\hat\Sigma^i_{zy}\\\hat\Sigma^i_{yz}&\hat\Sigma^i_{yy}\end{pmatrix} \tag{13.43–13.44}$$
(Shapes, added: with $z_t\in\mathbb R^{d_z},y_t\in\mathbb R^{d_y}$, $\hat\mu^i\in\mathbb R^{d_z+d_y}$ and $\hat\Sigma^i$ is square of that size.) The EKF linearizes $f,h$. The UKF propagates sigma points and may be more accurate. Gaussian conditioning gives the proposal
$$q(z_t|z^i_{1:t-1},y_t)\approx\mathcal N(z_t|\mu^i_t,\Sigma^i_t),\ \mu^i_t=\hat\mu^i_z+\hat\Sigma^i_{zy}(\hat\Sigma^i_{yy})^{-1}(y_t-\hat\mu^i_y),\ \Sigma^i_t=\hat\Sigma^i_{zz}-\hat\Sigma^i_{zy}(\hat\Sigma^i_{yy})^{-1}\hat\Sigma^i_{yz} \tag{13.45–13.47}$$
The approximation must be redone for each particle (p. 555). Names: extended and unscented particle filter.

**13.3.3 Laplace proposals.** For linear-Gaussian dynamics with a GLM likelihood, find $z_t^*=\arg\max\log p(y_t|z_t)$ (e.g. Newton–Raphson) and use $p(y_t|z_t)\approx\mathcal N(z_t|z_t^*,-\mathbf H_t^*)$ (13.48), $\mathbf H^*_t$ the Hessian of the log-likelihood at the mode. Then a Kalman update gives $p(z_t|z^i_{t-1},y_t)$: the *Laplace Gaussian filter* (p. 555).

*Example: neural decoding (13.3.3.1).* $z_t\in\mathbb R^6$ is 3d hand position and velocity, and each coordinate pair follows a Brownian random walk:
$$\binom{z_t(i)}{z_t(i+3)}\Big|z_{t-1}\sim\mathcal N_2\Big(\begin{pmatrix}1&\Delta\\0&1\end{pmatrix}\binom{z_{t-1}(i)}{z_{t-1}(i+3)},\sigma^2\mathbf Q\Big),\ \mathbf Q=\begin{pmatrix}\Delta^3/3&\Delta^2/2\\\Delta^2/2&\Delta\end{pmatrix},\ i=1{:}3 \tag{13.49–13.50}$$
Spike counts: $p(y_t(k)|z_t)=\mathrm{Poi}(\lambda_k(z_t))$, $\log\lambda_k=\alpha_k+\beta_k^\top z_t$ (13.51–13.52). A synthetic run has $T=25$, $K=50$ neurons. With the true model, the guided (Laplace) filter's ESS is much higher than the bootstrap filter's (Fig. 13.5) (p. 556).

**13.3.4 Nested SMC.** For each particle and step, run an inner SMC targeting the optimal proposal $p(z_t|z^i_{1:t-1},y_{1:t})$. It can approximate the optimal proposal arbitrarily well (no parametric assumption) but can be slow, though the inner runs can be parallelized (p. 557).

### 13.4 Rao-Blackwellized particle filtering (pp. 557–563)
**Idea.** If hidden variables split into $m_t$ and $z_t$ such that $z_t$ can be integrated out analytically given $m_{1:t}$, sample only $m_{1:t}$ and represent $p(z_t|m_{1:t},y_{1:t})$ parametrically ("distributional" or "collapsed" particles). This lowers the sampling dimension and reduces variance (p. 557).

**13.4.1 Mixture of Kalman filters (switching linear dynamical system).**
$$p(z_t|z_{t-1},m_t=k)=\mathcal N(z_t|\mathbf F_kz_{t-1},\mathbf Q_k),\ p(y_t|z_t,m_t=k)=\mathcal N(y_t|\mathbf H_kz_t,\mathbf R_k),\ p(m_t=k|m_{t-1}=j)=A_{jk} \tag{13.53–13.55}$$
Exact inference is intractable. Sampling discrete trajectories $m^n_{1:t}$ and running a Kalman filter per particle gives
$$p(z_t,m_t|y_{1:t})\approx\sum_nW^n_t\delta(m_t-m^n_t)\mathcal N(z_t|\mu^n_t,\Sigma^n_t) \tag{13.56}$$
Derivation: $p(m_{1:t},z_{1:t}|y_{1:t})=p(z_{1:t}|m_{1:t},y_{1:t})p(m_{1:t}|y_{1:t})$ (13.57), and
$$p(m_{1:t}|y_{1:t})\propto p(y_t|m_{1:t},y_{1:t-1})p(m_t|m_{t-1})p(m_{1:t-1}|y_{1:t-1}) \tag{13.58–13.60}$$
Here $p(y_t|m_{1:t},y_{1:t-1})\neq p(y_t|m_t)$, because $m_t$ does not d-separate past observations from $y_t$. With a recursive proposal $q(m_{1:t}|y_{1:t})=q(m_t|m_{1:t-1},y_{1:t})q(m_{1:t-1}|y_{1:t})$ (13.61):
$$\tilde w^n_t\propto\frac{p(y_t|m^n_t,m^n_{1:t-1},y_{1:t-1})\,p(m^n_t|m^n_{t-1})}{q(m^n_t|m^n_{1:t-1},y_{1:t})}\tilde w^n_{t-1} \tag{13.62}$$
If the proposal is the prior $p(m_t|m^n_{t-1})$ and state $k$ is sampled, then $\tilde w^n_t\propto\tilde w^n_{t-1}L^n_{tk}$ with
$$L^n_{tk}=\int p(y_t|m_t=k,z_t)\,p(z_t|m_t=k,y_{1:t-1},m^n_{1:t-1})dz_t \tag{13.63–13.64}$$
the predictive density of $y_t$. In an SLDS it is the Kalman filter's normalization constant (Eq. 8.35). Algorithm 13.4 per particle: sample $k\sim p(m_t|m^n_{t-1})$, run KFupdate to get $(\mu^n_t,\Sigma^n_t,L^n_{tk})$, set $\tilde w^n_t=\tilde w^n_{t-1}L^n_{tk}$. Then resample if ESS < ESS$_{\min}$ (pp. 557–558).

> **Intuition note.** Wherever an exact calculation is available (a Kalman filter given the discrete mode path), do it exactly and sample only what is left. Less is sampled, so there is less variance.

*13.4.1.1 Improvement.* Because $m_t$ is discrete, propagate each of $N$ particles through all $K$ models, weigh all $NK$ candidates, then select $N$ with the optimal resampling of [FC03]. It stochastically favours large weights, is unbiased, and avoids duplicate particles (p. 559).

**13.4.2 Example: maneuvering object.** (From [DGK01].) $p(z_t|z_{t-1},m_t=k)=\mathcal N(z_t|\mathbf Fz_{t-1}+b_k,\mathbf Q)$, $z_t=(x_{1t},\dot x_{1t},x_{2t},\dot x_{2t})$ (13.65), $\mathbf H=\mathbf I$, $\mathbf R=10\,\mathrm{diag}(2,1,2,1)$, $\mathbf F=\begin{pmatrix}1&\Delta&0&0\\0&1&0&0\\0&0&1&\Delta\\0&0&0&1\end{pmatrix}$ with $\Delta=0.1$ (13.66), $\mathbf Q=0.2\mathbf I$, $b_1=0$, $b_2=(-1.225,-0.35,1.225,0.35)$, $b_3=(1.225,0.35,-1.225,-0.35)$, and
$$\mathbf A=\begin{pmatrix}0.8&0.1&0.1\\0.1&0.8&0.1\\0.1&0.1&0.8\end{pmatrix} \tag{13.67}$$
For 100 steps, RBPF (optimal proposal, 1000 particles) gives the estimate in Fig. 13.6b. The bootstrap filter "does much worse"; the figure titles show MSE 7.66 vs 10.95. Discrete-state classification error is 29%, but isolated misclassifications do not seem to hurt the continuous estimates much (pp. 559–560).

**13.4.3 FastSLAM.** SLAM = simultaneous localization and mapping: a robot tracks its pose $r_t$ while learning landmark locations $l^1,\dots,l^K\in\mathbb R^2$. State $z_t=(r_t,l_t^{1:K})$ and
$$p(z_t|z_{t-1},u_t)=p(r_t|r_{t-1},l^{1:K}_{t-1},u_t)\prod_kp(l^k_t|l^k_{t-1}) \tag{13.68}$$
Static landmarks use $p(l_t^k|l^k_{t-1})=\delta(l^k_t-l^k_{t-1})$ (map as a shared unknown parameter). Controls $u_{1:t}$ are given (p. 560). If everything is linear-Gaussian, a Kalman filter keeps the belief. Pose uncertainty grows, then shrinks on revisiting a place ("closing the loop", Fig. 13.9a) (p. 561). Landmarks become correlated through the robot's path: $l^1,l^2$ are not d-separated by $y_{1:t}$, the precision matrix gets denser, and each step costs $O(K^3)$ (p. 563). Given the robot path $r_{1:t}$, landmarks are independent: $p(l_t|r_{1:t},y_{1:t})=\prod_kp(l^k_t|r_{1:t},y_{1:t})$. So sample paths and run a 2d Kalman filter per landmark (RBPF), costing $O(NK)$ per step. Since $N$ needed is "quite small", it is essentially linear in $K$. Introduced in [Mur00a] (occupancy grids, HMM filter per particle) and extended in [Thr+04] as FastSLAM (p. 563).

### 13.5 Extensions (p. 563)
- Resample-move: apply MCMC steps at each PF step with target $\pi_t(z_t)$ to add diversity (SMC can be used instead of MCMC).
- Particle smoothing: offline inference.
- Particle BP: PF combined with loopy belief propagation for general graphs.
- Static models: Section 13.6.

### 13.6 SMC samplers (pp. 563–571)
Goal: sample from a generic $\pi(z)=\tilde\gamma(z)/Z$, no SSM needed; SMC is thus an alternative to MCMC. Stated advantages over MCMC: estimates $Z$; adaptive tuning of kernels from current samples is easier; easier to parallelize. Method: define intermediate $\pi_t(z_t)$, expand each to a distribution $\bar\pi_t(z_{1:t})$ over past variables, run particle filtering, and marginalize to the final state (pp. 563–564).

**13.6.1 Ingredients.** (p. 564)
- Targets $\pi_t(z_t)=\tilde\gamma_t(z_t)/Z_t$ on a common state space.
- Forward kernel $M_t(z_t|z_{t-1})$ (sums to 1 over $z_t$), used to propose.
- Backward kernel $L_t(z_t|z_{t+1})$ (sums to 1 over $z_t$), defining
$$\bar\pi_t(z_{1:t})=\pi_t(z_t)\prod_{s=1}^{t-1}L_s(z_s|z_{s+1}) \tag{13.69}$$
which satisfies $\sum_{z_{1:t-1}}\bar\pi_t=\pi_t(z_t)$, so samples from the end of sequences follow $\pi_t$.

Incremental weight:
$$\alpha_t=\frac{\bar\pi_t(z_{1:t})}{\bar\pi_{t-1}(z_{1:t-1})M_t(z_t|z_{t-1})}\propto\frac{\tilde\gamma_t(z_t)}{\tilde\gamma_{t-1}(z_{t-1})}\frac{L_{t-1}(z_{t-1}|z_t)}{M_t(z_t|z_{t-1})} \tag{13.70}$$
Choose $M_t$ an MCMC kernel leaving $\pi_t$ invariant, and $L_{t-1}$ its time reversal:
$$\pi_t(z_t)L_{t-1}(z_{t-1}|z_t)=\pi_t(z_{t-1})M_t(z_t|z_{t-1}) \tag{13.71}$$
Then
$$\alpha_t=\frac{Z_t\pi_t(z_t)L_{t-1}(z_{t-1}|z_t)}{Z_{t-1}\pi_{t-1}(z_{t-1})M_t(z_t|z_{t-1})}=\frac{Z_t\pi_t(z_{t-1})M_t(z_t|z_{t-1})}{Z_{t-1}\pi_{t-1}(z_{t-1})M_t(z_t|z_{t-1})}=\frac{\tilde\gamma_t(z_{t-1})}{\tilde\gamma_{t-1}(z_{t-1})} \tag{13.72–13.74}$$
(p. 564). Kernel choice (p. 565): $K$ steps of random-walk Metropolis–Hastings with proposal covariance $\delta^2\hat\Sigma_{t-1}$ ($\hat\Sigma_{t-1}$ = weighted empirical covariance of previous samples, $\delta=2.38D^{-3/2}$ as printed, "optimal" for RWMH), or HMC/NUTS in high dimension (p. 565).

> **Intuition note.** The weight only asks "how much more does the new target like the old point than the old target did?" Moving the particle with a kernel that preserves the target costs nothing in the weight.

**13.6.2 Likelihood tempering (geometric path).** $\tilde\gamma_t(z)=\tilde\gamma_0(z)^{1-\lambda_t}\tilde\gamma(z)^{\lambda_t}$, $0=\lambda_0<\dots<\lambda_T=1$ (13.75). With resampling turned off this equals annealed importance sampling. For Bayesian inference: $\tilde\gamma_0=\pi_0(\theta)$ (prior), $\tilde\gamma=\pi_0(\theta)p(\mathcal D|\theta)$,
$$\tilde\gamma_t(\theta)=\pi_0(\theta)^{1-\lambda_t}\exp[-\lambda_t\mathcal E(\theta)],\ \ \mathcal E(\theta)=-\log p(\mathcal D,\theta) \tag{13.76}$$
$$\alpha_t(\theta)=\exp[-\delta_t\mathcal E(\theta)],\ \lambda_t=\lambda_{t-1}+\delta_t \tag{13.77}$$
(p. 565; see Reading notes on (13.77)). Successive distributions should be "equidistant" (adaptive tempering). For Gaussian prior and Gaussian energy, [CP20b] show $\lambda_t=(1+\gamma)^{t+1}-1$, $\gamma>0$ achieves it: increase $\lambda$ slowly, then in bigger steps. In practice
$$\delta_t=\operatorname*{argmin}_{\delta\in[0,1-\lambda_{t-1}]}\big(\mathrm{ESSLW}(\{-\delta\mathcal E(\theta^n_t)\})-\mathrm{ESS}_{\min}\big) \tag{13.78}$$
with ESSLW the ESS (13.37) computed from log weights. This keeps ESS near the target (typically $0.5N$); if no solution exists, $\delta_t=1-\lambda_{t-1}$ (p. 565). Algorithm 13.5: initialize from the prior; each step resample, move with $M_{\lambda_{t-1}}$, compute $\delta_t$, weigh by $\exp[-\delta\mathcal E]$, normalize (p. 566).

*Example: 1d bimodal (13.6.2.1).* $p(\theta)\propto\mathcal N(\theta|0,\mathbf I)\exp(-\mathcal E(\theta))$, $\mathcal E=c(\|\theta\|^2-1)^2$, $c=5$: low energy where the norm is near 1, hence two modes (Fig. 13.10a). HMC and NUTS started at $\theta_0=1$ get stuck near it (Fig. 13.11a,b). The tempered family goes from the Gaussian prior ($\lambda=0$) to the target. Adaptive tempered SMC with an HMC kernel recovers both modes (Fig. 13.11c). The schedule is small at first, then increases exponentially, taking 8 steps (Fig. 13.11d) (p. 566). The text says such multimodal targets can be provably hard for other methods including HMC, because gradients give only local information (p. 566).

**13.6.3 Data tempering and IBIS.** For iid data, $\tilde\gamma_t(\theta)=p(\theta)p(y_{1:t}|\theta)$ (13.80), and by (13.74)
$$\alpha_t(\theta)=\frac{p(\theta)p(y_{1:t}|\theta)}{p(\theta)p(y_{1:t-1}|\theta)}=p(y_t|y_{1:t-1},\theta) \tag{13.81}$$
An MCMC move costs $O(t)$ (the accept step touches all $t$ likelihood terms), so total cost is $O(T^2)$. To cut this, move parameters only when ESS drops below a level, otherwise repeat the old value: iterated batch importance sampling (IBIS) [Cho02] (p. 567).
*Example (p. 567–568).* $y_t\sim\mathcal N(3.14,1)$, $t=1{:}30$; $\theta=(\mu,\sigma)$; prior $\mathcal N(\mu|0,1)\mathrm{Ga}(\sigma|a{=}1,b{=}1)$; adaptive RWMH; the text says $N=20$ particles × $K=50$ MCMC steps = 1000 samples per step. The posterior concentrates on the true values by $t=29$ (Fig. 13.12a). Resampling/moves trigger when ESS < 500 of 1000, and only 3 MCMC updates are needed (p. 568).

**13.6.4 Rare events and extrema.** To sample $\pi_0(\theta)$ given $S(\theta)>\lambda^*$ with $\lambda^*$ in the tail, use
$$\pi_t(\theta)=\frac1{Z_t}\mathbb I(S(\theta)\ge\lambda_t)\pi_0(\theta),\ \ \lambda_0<\dots<\lambda_T=\lambda^*,\ \ G_t(\theta_t)=\mathbb I(S(\theta_t)\ge\lambda_t) \tag{13.82–13.83}$$
and $Z_T=p(S(\theta)\ge\lambda_T)$ under $\pi_0$ (13.84). Thresholds can be set adaptively as the $\alpha$-th quantile of scores (e.g. $\alpha=0.5$ keeps the top 50%), which keeps ESS at the minimum [Cér+12]. This is very similar to the cross-entropy method, which fits a parametric distribution to the particles instead of using a Markov kernel (pp. 568–569).

**13.6.5 SMC-ABC / likelihood-free inference.** If we can simulate $y\sim p(\cdot|\theta)$ but cannot evaluate $p(y|\theta)$, approximate Bayesian computation (ABC) accepts $(\theta,y)$ with $d(y,y^*)<\epsilon$ (summary statistics $s(y)$ in high dimension). SMC-ABC shrinks $\epsilon$:
$$\pi_t(\theta,y)=\frac1{Z_t}\pi_0(\theta)p(y|\theta)\mathbb I(d(y,y^*)<\epsilon_t),\ \ \epsilon_0>\epsilon_1>\cdots \tag{13.85}$$
It resembles rare-event SMC, except that quality must be judged in data space. The method is popular in genetics and epidemiology but slow and not scalable to high dimension. An alternative is to train a tractable generative model to emulate the simulator (p. 569).

**13.6.6 SMC².** When likelihood ratios $\gamma_t/\gamma_{t-1}$ cannot be evaluated efficiently (e.g. latent variable models), use SMC with the estimate $\hat Z_t$ (13.10) as a subroutine (p. 569).

**13.6.7 Variational filtering SMC.** Learn a proposal (parameters $\phi$; model parameters $\theta$) so $\hat\pi_T$ is close to $\pi_T$. [Nae+18] show
$$0\le D_{KL}(\mathbb E[\hat\pi_T]\,\|\,\pi_T)\le-\mathbb E\Big[\log\frac{\hat Z_T}{Z_T}\Big],\quad Z_T(\theta)=\int p_\theta(z_{1:T},y_{1:T})dz_{1:T} \tag{13.86–13.87}$$
$$\mathbb E[\log\hat Z_T(\theta,\phi)]\le\mathbb E[\log Z_T(\theta)]=\log Z_T(\theta) \tag{13.88}$$
So SMC gives an unbiased approximation to $\mathbb E[\log\hat Z_T]$, a lower bound on the log evidence (log marginal likelihood). The bound's step uses that $\hat Z_T$ is unbiased and that $\log$ is concave (added step; not spelled out in the source). Maximize it by SGD over $\theta,\phi$. The resampling step is non-differentiable, so one may ignore its parameter dependence or use differentiable approximations. Independent proposals of the idea: FIVO, variational SMC, auto-encoding SMC (p. 570).

**13.6.8 Variational smoothing SMC (SIXO).** Filtering SMC targets $p_\theta(z_{1:t}|y_{1:t})$ and ignores future observations, which for offline data can cause particle impoverishment and high-variance bounds (p. 570). SIXO [Law+22] targets smoothing distributions $p_\theta(z_{1:t}|y_{1:T})$ via twisted particle filters:
$$p_\theta(z_{1:t},y_{1:T})=p_\theta(z_{1:t},y_{1:t})\,p_\theta(y_{t+1:T}|z_t)\approx p_\theta(z_{1:t},y_{1:t})\,r_\psi(y_{t+1:T},z_t) \tag{13.89–13.91}$$
where $r_\psi$ is the twisting ("lookahead") function. Since $p_\theta(y_{t+1:T}|z_t)\propto p_\theta(z_t|y_{t+1:T})/p_\theta(z_t)$ (13.92) (p. 570), learn this density ratio with a binary classifier: positives $(z_t,y_{t+1:T})$ marginalized from an ancestral sample $(z_{1:T},y_{1:T})\sim p_\theta$ (distributed as $p_1=p_\theta(z_t,y_{t+1:T})$), negatives $(\tilde z_t,\tilde y_{t+1:T})$ marginalized from a fresh sample $(\tilde z_{1:T},\tilde y_{1:T})\sim p_\theta$, which the text says is distributed as $p_2=p_\theta(z_t)p_\theta(y_{t+1:T})$ (p. 571). Then rerun SMC for a tighter bound, in a variational-EM-like loop on
$$\mathcal L_{\rm SIXO}=\mathbb E[\log\hat Z_{\rm SIXO}]\le\log\mathbb E[\hat Z_{\rm SIXO}]=\log p_\theta(y_{1:T}) \tag{13.93–13.94}$$
**Result [Law+22]:** if the true model is an SSM whose optimal proposal lies in class $\mathcal Q$ and optimal lookahead lies in class $\mathcal R$, and the SIXO objective has a unique maximizer, then at the optimum the learned proposal and twisting function equal the optimal ones, and the bound is tight for any number of samples $N_s\ge1$ and any such SSM. This contrasts with FIVO, whose bound usually does not become tight (p. 571).

> **Intuition note.** A filtering objective cannot see the future, so a particle may look fine now and be ruined later. A learned lookahead lets particles be judged by how well they explain later data too.

## Toy example (ours, not from the text)
One bootstrap-filter step with $N=4$ particles. After propagating through the dynamics the particles are $z=(0,1,2,3)$. The observation is $y=2$ and the likelihood is $\propto\exp(-(y-z)^2/2)$.

1. Unnormalized weights (proposal = prior, so $\tilde w=p(y|z)$ up to a constant): $e^{-2}=0.1353$, $e^{-0.5}=0.6065$, $e^{0}=1$, $e^{-0.5}=0.6065$. Sum $=2.3484$.
2. Normalized weights $W=(0.0576,\,0.2583,\,0.4258,\,0.2583)$, found by dividing each by 2.3484.
3. Estimate of $\hat Z_t/\hat Z_{t-1}$ (13.28 with old weights all equal) $\propto 2.3484/4=0.5871$.
4. Posterior mean before resampling: $0(0.0576)+1(0.2583)+2(0.4258)+3(0.2583)=1.885$.
5. ESS (13.36): $\sum W^2=0.0033+0.0667+0.1813+0.0667=0.3180$, so ESS $=1/0.3180\approx3.14$. This is above $N/2=2$, so adaptive resampling would not trigger. We resample anyway to show the mechanics.
6. Systematic resampling (13.35) with $u=0.4$: $U^i=(i-1)/4+0.4/4=(0.10,\,0.35,\,0.60,\,0.85)$. Cumulative weights: $0.0576,\ 0.3159,\ 0.7417,\ 1$. So $U^1=0.10$ falls in bin 2, $U^2=0.35$ and $U^3=0.60$ in bin 3, $U^4=0.85$ in bin 4. Ancestors $(2,3,3,4)$, new particles $z=(1,2,2,3)$, all with weight $1/4$.
7. Mean after resampling: $(1+2+2+3)/4=2.0$. The particle at $z=0$ (weight 0.058) died and the best one ($z=2$) was duplicated. The weighted and resampled estimates differ in this one draw, but agree in expectation (13.32).

## Concepts
- [[sequential-monte-carlo]] (new) — sample a sequence of related distributions with weighted particles plus resampling (p. 543)
- [[particle-filter]] (new) — SMC where each marginal $\pi_t(z_t)$ matters, e.g. filtering in SSMs (p. 543)
- [[smc-sampler]] (new) — SMC where only the final target matters; intermediate targets are computational devices (p. 543)
- [[importance-sampling-snis]] (new) — self-normalized importance sampling, the base of the particle filter (p. 546)
- [[sequential-importance-sampling]] (new) — importance sampling with recursive proposals and weights via incremental weights (p. 547)
- [[weight-degeneracy]] (new) — nearly all weight ends on one particle (p. 547)
- [[resampling-methods]] (new) — multinomial, stratified, systematic via inverse cdf (pp. 551–553)
- [[effective-sample-size]] (new) — $1/\sum W^2$; used to trigger resampling (p. 553); differs from the MCMC ESS
- [[path-degeneracy]] (new) — resampling collapses ancestry, losing diversity about the past (p. 550)
- [[bootstrap-filter]] (new) — SISR with dynamics prior as proposal (p. 549)
- [[locally-optimal-proposal]] (new) — $\pi_t(z_t|z_{1:t-1})$, which conditions on the newest observation (p. 554)
- [[rao-blackwellized-pf]] (new) — sample part of the state, integrate the rest analytically (p. 557)
- [[likelihood-tempering]] (new) — geometric path from prior to posterior; adaptive step chosen by ESS (p. 565)
- [[data-tempering-ibis]] (new) — add observations one at a time; iterated batch importance sampling (p. 567)
- [[approximate-bayesian-computation]] (new) — accept parameters whose simulated data are within $\epsilon$ of the observed (p. 569)
- [[marginal-likelihood-evidence]] — SMC gives estimate $\hat Z_T$; log of it is a lower bound in variational SMC (pp. 550, 570)
- [[metropolis-hastings]] and [[hamiltonian-monte-carlo]] — used as SMC moves; HMC alone gets stuck on the bimodal example (pp. 565–566)
- [[kl-divergence]] — defines the locally optimal proposal (p. 554) and bounds SMC quality (p. 570)

## Canonical instances
- [[spiral-tracking-2d]] (new) — nonlinear 2d tracking filtered by a bootstrap filter (p. 544)
- [[non-markovian-gaussian-sequence]] (new) — model (13.6) showing weight and path degeneracy (pp. 545, 547)
- [[neural-decoding-poisson]] (new) — guided vs bootstrap filter, ESS (p. 556)
- [[maneuvering-object-slds]] (new) — RBPF with 3 discrete modes (p. 559)
- [[fastslam]] (new) — RBPF for simultaneous localization and mapping (p. 563)
- [[bimodal-1d-tempering]] (new) — SMC succeeds where HMC/NUTS stall (p. 566)
- [[ibis-1d-gaussian]] (new) — IBIS on 30 data points (p. 567)

## Bridges (candidates)
- [same-math] SMC with likelihood tempering and no resampling ↔ Monte Carlo: annealed importance sampling — the text states the equivalence (p. 565).
- [structural-analogy] Data tempering weight $p(y_t|y_{1:t-1},\theta)$ ↔ Bayesian canon: sequential updating — each datum's weight is its predictive probability under the current posterior.
- [structural-analogy] Rare-event thresholding in SMC ↔ cross-entropy method — same stepwise-threshold idea, different move mechanism (p. 569).
- [structural-analogy] Rao-Blackwellization ↔ variance reduction by analytic integration — replace sampling with a conditional expectation where possible (p. 557).
- [metaphor] Resampling as "survival of the fittest" ↔ evolutionary selection — the source uses this name (p. 549).

## Questions this raises
- How does the variance of $\hat Z_T$ grow with $T$ and with the number of particles, and what does that mean for using it in parameter estimation?
- When does tempering with more intermediate steps help, versus costing more MCMC moves?
- How should the number of MCMC steps in each SMC move be chosen?
- Why is the SIXO bound tight for any $N_s\ge1$ under the stated conditions, and how realistic are those conditions?

## Reading notes
- Printed page = pdf − 34 (pdf 577–605 = printed 543–571); the last pdf page (606, printed 572) is blank.
- Eqs. (13.2)–(13.3) as printed start the product at $t=1$ (resp. $s=1$) after $p(z_1)p(y_1|z_1)$; the product presumably should start at 2. In 13.1.3, "$0=\tau_t<\dots$" should presumably read $\tau_1$ (or $\tau_0$).
- Section 13.3.2 refers to the UKF as "Section 13.3.2" (self-reference); later references say Section 8.4/8.4.2.
- (13.48): the printed covariance is $-\mathbf H^*_t$; a covariance would normally be its inverse (my check; not stated in the text).
- (13.61) as printed conditions the old path on $y_{1:t}$ rather than $y_{1:t-1}$; (13.62) is consistent with the recursion.
- (13.77): the printed denominator has $\pi_0(\theta)^{1-\lambda_t}$ (not $1-\lambda_{t-1}$) and $\exp[-\lambda_{t-1}\mathcal E]$; with $\mathcal E=-\log p(\mathcal D,\theta)$ the $\pi_0$ factors would not strictly cancel unless $\mathcal E=-\log p(\mathcal D|\theta)$ (my check). Eq. (13.78) has no absolute value around the argmin objective; likely intended. Algorithm 13.5 line 11 uses $\delta$, not $\delta_t$.
- Algorithm 13.3 line 8 tests ESS of $\tilde w_{t-1}$, while line 9 resamples using $\tilde w_t$; probably an index slip. Eqs. (13.26)–(13.27) use $\hat Z_t$ for both the per-step mean weight and the cumulative estimate.
- IBIS example (p. 568): $N=20$ particles × $K=50$ steps = 1000 samples per step, but Fig. 13.12b text then says "number of particles is 1000".
- The theorem on p. 571 writes $\mathcal L_{\rm SIXO}(\theta^*,\phi^*,\psi^*)=p^*(y_{1:T})$ without a log, whereas (13.94) has $\log p_\theta(y_{1:T})$; presumably $\log p^*$ is meant.
- The text states $\delta=2.38D^{-3/2}$ (p. 565); copied as printed.
- The unit has no exercises. Figures were read from the page images; digest values taken from figure titles (MSE 7.66, 10.95) are marked as such.
- p. 571: the text says a fresh sample's $(\tilde z_t,\tilde y_{t+1:T})$ follows $p_2=p_\theta(z_t)p_\theta(y_{t+1:T})$; if both come from one joint sample they would follow $p_1$ instead (my check; not stated in the text).
