---
id: sarkka-2023-bayesianfiltering/ch16-parameter
work: sarkka-2023-bayesianfiltering
unit: 16 Parameter Estimation
pages: 319-348
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Parameter Estimation in State Space Models

## L0 — One line
The parameters of a state space model can be estimated by running a filter for each fixed parameter value to get the marginal likelihood or the "energy function" (the unnormalised negative log-posterior), then using it in optimization or MCMC (EM instead works with smoother output).

## L1 — The gist (≤ 120 words)
Earlier chapters assumed the model parameters were known. This chapter asks how to estimate unknown parameters θ from measurements. Marginalising the states out of the joint posterior of states and parameters is hard. The answer is to work with the marginal posterior p(θ | y_{1:T}). Its likelihood factorises into one-step prediction terms, which a filter supplies recursively. This gives an energy function (the unnormalised negative log-posterior) usable in MAP/ML optimization (maximum a posteriori / maximum likelihood) and Metropolis–Hastings sampling. When direct optimization is awkward, EM (expectation–maximization) uses smoother output instead. Kalman filters give exact results in linear models. Gaussian filters and particle filters give approximations. Augmenting the state with θ and Rao–Blackwellization (marginalising parameters analytically) are alternatives.

**Prerequisites:** Bayes' rule; Kalman filter and RTS smoother equations; Gaussian filters and particle filters (SIR); basic MCMC ideas; matrix trace.

## L2 — Key ideas (5–10 bullets)
- The marginal likelihood factorises as a product of one-step predictive densities (prediction error decomposition). A filter computes them recursively, which avoids the hard integral over the whole state history (pp. 320–321).
- The energy function φ_T(θ) = −log p(y_{1:T}|θ) − log p(θ) is the unnormalised negative log-posterior. It obeys an additive recursion, and gradient-free MAP optimization and MCMC need only this function, while gradient-based optimization also needs derivatives (pp. 322–324).
- Metropolis–Hastings needs the energy only through differences (plus the proposal ratio), so the normalisation constant is not needed. Proposal choice is crucial; adaptive variants (RAM) tune the proposal covariance (pp. 324–326).
- EM maximizes a lower bound on the marginal likelihood. The E-step needs only smoothing and pairwise smoothing distributions (pp. 327–329).
- For linear Gaussian models the energy comes from the Kalman filter, and EM has closed-form M-steps in terms of RTS smoother output (pp. 332–336).
- With Gaussian filters the energy is approximate. Estimates are then biased and posterior uncertainty is typically underestimated (p. 338).
- A particle-filter likelihood estimate inside Metropolis–Hastings (PMMH) (asymptotically) samples from the exact parameter posterior. The estimate is not continuous in θ even with a fixed random number sequence, so optimization with it may be hard (pp. 342–343).
- State augmentation is simple, but its zero-noise parameter dynamics cause problems with approximate filters, and it can also fail sometimes. Rao–Blackwellization can marginalize conjugate static parameters analytically (pp. 330–331, 345–347).

## L3 — Walkthrough

### 16.1 Bayesian estimation of parameters (pp. 319–320)
Unknown parameters θ ∈ ℝ^d get a prior p(θ). The model is (p. 319)
$$\theta\sim p(\theta),\quad x_0\sim p(x_0\mid\theta),\quad x_k\sim p(x_k\mid x_{k-1},\theta),\quad y_k\sim p(y_k\mid x_k,\theta).\tag{16.1}$$
The straightforward route is the full posterior (p. 319)
$$p(x_{0:T},\theta\mid y_{1:T})=\frac{p(y_{1:T}\mid x_{0:T},\theta)\,p(x_{0:T}\mid\theta)\,p(\theta)}{p(y_{1:T})}.\tag{16.2}$$
Here $p(x_{0:T}\mid\theta)=p(x_0\mid\theta)\prod_{k=1}^T p(x_k\mid x_{k-1},\theta)$ and $p(y_{1:T}\mid x_{0:T},\theta)=\prod_{k=1}^T p(y_k\mid x_k,\theta)$ (p. 320).

If only θ matters, integrate out the states (p. 320):
$$p(\theta\mid y_{1:T})=\int p(x_{0:T},\theta\mid y_{1:T})\,dx_{0:T}.\tag{16.3}$$
The authors call this high-dimensional integral hard, and it gets harder as data accumulate. This is the same problem as in Sections 1.3 and 6.1, so recursive filtering/smoothing solutions are preferred (p. 320). The chapter therefore approximates
$$p(\theta\mid y_{1:T})\propto p(y_{1:T}\mid\theta)\,p(\theta)\tag{16.4}$$
without forming the joint posterior (p. 320). The unit has three families of method:
- Exact in linear models, approximate (Gaussian or particle filters) in non-linear/non-Gaussian ones.
- Once (16.4) can be evaluated: MAP, or MCMC sampling.
- If direct evaluation is not feasible: EM for the ML or MAP estimate (p. 320).

#### 16.1.1 Parameter posterior and energy function (pp. 320–322)
The hard part of (16.4) is the marginal likelihood. The prior can usually be chosen to be easy to evaluate, and the posterior's normalisation constant is usually avoided by Bayesian computation (pp. 320–321). Key factorisation (prediction error decomposition), with $p(y_1\mid y_{1:0},\theta)\triangleq p(y_1\mid\theta)$ (p. 321):
$$p(y_{1:T}\mid\theta)=\prod_{k=1}^T p(y_k\mid y_{1:k-1},\theta).\tag{16.5}$$

**Theorem 16.1 (recursion for marginal likelihood).** The terms of (16.5) are (p. 321)
$$p(y_k\mid y_{1:k-1},\theta)=\int p(y_k\mid x_k,\theta)\,p(x_k\mid y_{1:k-1},\theta)\,dx_k,\tag{16.6}$$
where the predictive state density obeys
$$p(x_k\mid y_{1:k-1},\theta)=\int p(x_k\mid x_{k-1},\theta)\,p(x_{k-1}\mid y_{1:k-1},\theta)\,dx_{k-1},\qquad p(x_k\mid y_{1:k},\theta)=\frac{p(y_k\mid x_k,\theta)\,p(x_k\mid y_{1:k-1},\theta)}{p(y_k\mid y_{1:k-1},\theta)}.\tag{16.7}$$
These are the Bayesian filtering equations (6.11), (6.12) with θ written explicitly.

*Proof.* By conditional independence of measurements (Property 6.3) (p. 321),
$$p(y_k,x_k\mid y_{1:k-1},\theta)=p(y_k\mid x_k,y_{1:k-1},\theta)\,p(x_k\mid y_{1:k-1},\theta)=p(y_k\mid x_k,\theta)\,p(x_k\mid y_{1:k-1},\theta).\tag{16.8}$$
Integrating over $x_k$ gives (16.6).

*Intuition note.* The likelihood of all data is built from "how surprising was each new measurement given the past". A filter already computes exactly that for a fixed θ, so parameters can be scored while filtering.

**Definition 16.2 (energy function)** (p. 322):
$$\varphi_T(\theta)=-\log p(y_{1:T}\mid\theta)-\log p(\theta).\tag{16.9}$$
Remark 16.3: $p(\theta\mid y_{1:T})\propto\exp(-\varphi_T(\theta))$ (16.10).

**Theorem 16.4 (recursion).** Start from $\varphi_0(\theta)=-\log p(\theta)$. For $k=1,\dots,T$ (p. 322):
$$\varphi_k(\theta)=\varphi_{k-1}(\theta)-\log p(y_k\mid y_{1:k-1},\theta),\tag{16.11}$$
with the terms from Theorem 16.1. The proof substitutes (16.5) into (16.9) and identifies the $\varphi_{k-1}$ terms.

### 16.2 Computational methods (p. 322)
The authors cover ML/MAP by direct optimization, EM, and MCMC. They say other methods exist but these are the most widely used probabilistic ones in the state space context (p. 322).

#### 16.2.1 MAP and Laplace approximations (pp. 323–324)
$$\hat\theta^{\rm MAP}=\arg\max_\theta\,p(\theta\mid y_{1:T})\tag{16.12}$$
$$\hat\theta^{\rm MAP}=\arg\min_\theta\,\varphi_T(\theta)\tag{16.13}$$
The minimisation form is usually numerically more stable and easier (p. 323). ML is MAP with a formally uniform prior $p(\theta)\propto1$ (p. 323).

Gradient-based optimization needs derivatives of the energy. Two ways (p. 323):
1. Formally differentiate the energy recursion for the chosen filter. This gives *sensitivity equations*, computed alongside the filter.
2. Use *Fisher's identity*, which writes the gradient as an expectation of the derivative of the complete-data log-likelihood over the smoothing distribution. It needs no additional recursion.

MAP approximates the posterior by a Dirac delta, so it ignores the posterior's spread (p. 323):
$$p(\theta\mid y_{1:T})\simeq\delta(\theta-\hat\theta^{\rm MAP}).\tag{16.14}$$
The Laplace approximation uses the Hessian $\mathbf H$ of the energy at the MAP point (pp. 323–324):
$$p(\theta\mid y_{1:T})\simeq \mathrm N\big(\theta\mid\hat\theta^{\rm MAP},[\mathbf H(\hat\theta^{\rm MAP})]^{-1}\big).\tag{16.15}$$
It needs a way to compute or approximate second derivatives of the energy (p. 324).

#### 16.2.2 MCMC (pp. 324–326)
MCMC draws samples by simulating a Markov chain whose stationary distribution is the target. It needs only the unnormalised posterior $\tilde p(\theta\mid y_{1:T})=p(y_{1:T}\mid\theta)p(\theta)$, or equivalently the energy (p. 324).

**Algorithm 16.5 (Metropolis–Hastings).** Draw $\theta^{(0)}$ from an arbitrary initial distribution. For $i=1,\dots,N$ (p. 324):
1. Sample a candidate $\theta^*\sim q(\theta^*\mid\theta^{(i-1)})$ (16.16).
2. Acceptance probability
$$\alpha_i=\min\Big\{1,\exp\big(\varphi_T(\theta^{(i-1)})-\varphi_T(\theta^*)\big)\frac{q(\theta^{(i-1)}\mid\theta^*)}{q(\theta^*\mid\theta^{(i-1)})}\Big\}.\tag{16.17}$$
3. Draw $u\sim U(0,1)$. Set $\theta^{(i)}=\theta^*$ if $u\le\alpha_i$, otherwise $\theta^{(i)}=\theta^{(i-1)}$ (16.18).

*Metropolis algorithm*: symmetric proposal, so (p. 325)
$$\alpha_i=\min\{1,\exp(\varphi_T(\theta^{(i-1)})-\varphi_T(\theta^*))\}.\tag{16.19}$$
Proposal choice is crucial and hard: some choices give highly correlated samples, others a too-high rejection rate (p. 325). *Random walk Metropolis* uses $q(\theta^{(i)}\mid\theta^{(i-1)})=\mathrm N(\theta^{(i)}\mid\theta^{(i-1)},\Sigma_{i-1})$ (16.20); the challenge is choosing $\Sigma_{i-1}$ (p. 325). Adaptive MCMC adapts it during the run, typically using the covariance of earlier samples. For random walk Metropolis, the optimal acceptance rate under certain ideal conditions is $\bar\alpha^*=0.234$ (p. 325).

**Algorithm 16.6 (RAM, robust adaptive Metropolis; Vihola, 2012)** (p. 326):
1. Draw $\theta^{(0)}$ from $p_0(\theta)$. Set $S_0$ = lower-triangular Cholesky factor of $\Sigma_0$.
2. Candidate $\theta^*=\theta_{i-1}+S_{i-1}r_i$, $r_i\sim\mathrm N(0,I)$.
3. $\alpha_i=\min\{1,\exp(\varphi_T(\theta_{i-1})-\varphi_T(\theta^*))\}$ (16.21).
4. Draw $u\sim U(0,1)$.
5. If $u\le\alpha_i$ set $\theta^{(i)}=\theta^*$, else $\theta^{(i)}=\theta^{(i-1)}$.
6. Find lower-triangular $S_i$ with positive diagonal such that
$$S_iS_i^{\mathsf T}=S_{i-1}\Big(I+\eta_i(\alpha_i-\bar\alpha^*)\frac{r_ir_i^{\mathsf T}}{\|r_i\|^2}\Big)S_{i-1}^{\mathsf T},\tag{16.22}$$
where $\{\eta_i\}\subset(0,1]$ decays to zero. Any such sequence will do; Vihola suggests $\eta_i=i^{-\gamma}$, $\gamma\in(1/2,1]$.
7. Set $i\leftarrow i+1$ and return to step 2.

Other methods (p. 326):
- *Hamiltonian Monte Carlo* builds proposals by simulating particles moving in a potential (the energy) plus a heat bath. The energy gradient enters as the force.
- *Gibbs sampling* draws components one at a time from their conditionals. No rejections are needed (acceptance probability is identically one). It is possible only in a restricted class of models, where the conditionals can be sampled.

#### 16.2.3 Expectation maximization (pp. 327–330)
EM iteratively finds an ML estimate when direct optimization is not feasible. It is easily modified for MAP (p. 327). For any density $q(x_{0:T})$ over the states (p. 327):
$$\log p(y_{1:T}\mid\theta)\ge F[q(x_{0:T}),\theta],\qquad F[q,\theta]=\int q(x_{0:T})\log\frac{p(x_{0:T},y_{1:T}\mid\theta)}{q(x_{0:T})}\,dx_{0:T}.\tag{16.23, 16.24}$$
The idea is to maximize the left side by iteratively maximizing this lower bound.

**Algorithm 16.7 (abstract EM; coordinate ascent).** From $q^{(0)},\theta^{(0)}$, for $n=0,1,\dots$: E-step $q^{(n+1)}=\arg\max_q F[q,\theta^{(n)}]$; M-step $\theta^{(n+1)}=\arg\max_\theta F[q^{(n+1)},\theta]$ (p. 327).

It can be shown (Neal and Hinton, 1999) that the E-step result is (p. 327)
$$q^{(n+1)}(x_{0:T})=p(x_{0:T}\mid y_{1:T},\theta^{(n)}).\tag{16.25}$$
Plugging in (p. 328):
$$F[q^{(n+1)},\theta]=\int p(x_{0:T}\mid y_{1:T},\theta^{(n)})\log p(x_{0:T},y_{1:T}\mid\theta)\,dx_{0:T}-\int p(x_{0:T}\mid y_{1:T},\theta^{(n)})\log p(x_{0:T}\mid y_{1:T},\theta^{(n)})\,dx_{0:T}.\tag{16.26}$$
The second term does not depend on θ. So maximizing F over θ is equivalent to maximizing the first term, denoted
$$\mathcal Q(\theta,\theta^{(n)})=\int p(x_{0:T}\mid y_{1:T},\theta^{(n)})\log p(x_{0:T},y_{1:T}\mid\theta)\,dx_{0:T}.\tag{16.27}$$
This is the expected complete-data log-likelihood under the posterior of the states given $\theta^{(n)}$.

**Algorithm 16.8 (EM).** From $\theta^{(0)}$; for $n=0,1,\dots$: E-step compute $\mathcal Q(\theta,\theta^{(n)})$; M-step $\theta^{(n+1)}=\arg\max_\theta\mathcal Q(\theta,\theta^{(n)})$ (p. 328).

By the Markov structure (p. 328):
$$\log p(x_{0:T},y_{1:T}\mid\theta)=\log p(x_0\mid\theta)+\sum_{k=1}^T\log p(x_k\mid x_{k-1},\theta)+\sum_{k=1}^T\log p(y_k\mid x_k,\theta).\tag{16.28}$$
So $\mathcal Q=I_1+I_2+I_3$ (16.29), with (p. 329)
$$I_1=\int p(x_0\mid y_{1:T},\theta^{(n)})\log p(x_0\mid\theta)\,dx_0,$$
$$I_2=\sum_{k=1}^T\int p(x_k,x_{k-1}\mid y_{1:T},\theta^{(n)})\log p(x_k\mid x_{k-1},\theta)\,dx_k\,dx_{k-1},$$
$$I_3=\sum_{k=1}^T\int p(x_k\mid y_{1:T},\theta^{(n)})\log p(y_k\mid x_k,\theta)\,dx_k.\tag{16.30}$$
Only smoothing and pairwise smoothing distributions are needed, not the full posterior. Linear models give closed forms via RTS smoothers; non-linear models use Gaussian smoothers; general models use particle smoothers (p. 329).

The M-step is most useful when the maximum is found analytically by $\partial\mathcal Q(\theta,\theta^{(n)})/\partial\theta=0$ (16.31). This happens for linear state space models and some non-linear classes (p. 329). A MAP version results from maximizing $\mathcal Q(\theta,\theta^{(n)})+\log p(\theta)$ in the M-step (p. 329).

**Fisher's identity.** The gradient of $\mathcal Q$ at $\theta^{(n)}=\theta$ gives exactly the gradient of the marginal log-likelihood. Hence (p. 330)
$$\frac{\partial\varphi_T(\theta)}{\partial\theta}=-\frac{\partial\log p(\theta)}{\partial\theta}-\frac{\partial\mathcal Q(\theta,\theta^{(n)})}{\partial\theta}\Big|_{\theta^{(n)}=\theta}.\tag{16.32}$$
The authors note that the original identity relates log marginal likelihood and $\mathcal Q$, not log posterior and $\mathcal Q$ (p. 330). It is useful in linear models, where it is often easier and computationally lighter. In non-linear models the filtering/smoothing approximations can make the gradient inconsistent with the energy approximation from the same method. For particle filters it is a feasible way to approximate the energy gradient (p. 330).

*Intuition note.* EM replaces the unavailable likelihood by an average of the complete-data log-likelihood over states, estimated with the current θ. Each iteration then re-fits θ as if those state estimates were data. Fisher's identity says the slope of the true likelihood equals the slope of this average at the current θ.

### 16.3 Practical estimation (p. 330)

#### 16.3.1 State augmentation (pp. 330–331)
For $x_k=f(x_{k-1},\theta)+q_{k-1}$, $y_k=h(x_k,\theta)+r_k$ (16.33), add $\theta_k=\theta_{k-1}$ (constant parameter) and define $\tilde x_k=(x_k,\theta_k)$ (16.34). This gives $\tilde x_k=\tilde f(\tilde x_{k-1})+\tilde q_{k-1}$, $y_k=h(\tilde x_k)+r_k$ (16.35), with no unknown parameter left (p. 331).

The problem is the singular (zero-noise) parameter dynamics. Claims on p. 331:
- It works well when the whole system is linear and the estimator has no approximation errors.
- If the parameters appear linearly, including them in the state is sometimes a good idea, but it can also fail sometimes.
- With non-linear Kalman filters the Gaussian approximation tends to become singular and the filter diverges.
- Particle filters suffer sample impoverishment, which is worst with exactly zero dynamic noise.

A common fix is artificial noise, $\theta_k=\theta_{k-1}+\varepsilon_{k-1}$ (16.36). It changes the problem to one with a time-varying parameter, but it is sometimes applicable and worth trying before more complex methods (p. 331). Section 16.3.6 offers a Rao–Blackwellization alternative: use a closed-form solution for the static parameter and sample only the state, which works if the parameter enters in a suitable conjugate form (p. 331).

#### 16.3.2 Linear Gaussian models (pp. 332–337)
Model (p. 332): $x_k=A(\theta)x_{k-1}+q_{k-1}$, $y_k=H(\theta)x_k+r_k$, with $q_{k-1}\sim\mathrm N(0,Q(\theta))$, $r_k\sim\mathrm N(0,R(\theta))$, $x_0\sim\mathrm N(m_0(\theta),P_0(\theta))$ (16.37).

**Theorem 16.9 (energy function).** (p. 332)
$$\varphi_k(\theta)=\varphi_{k-1}(\theta)+\tfrac12\log|2\pi S_k(\theta)|+\tfrac12 v_k^{\mathsf T}(\theta)S_k^{-1}(\theta)v_k(\theta),\tag{16.38}$$
with $v_k,S_k$ from the Kalman filter run with θ fixed.

Prediction (16.39): $m_k^-=A m_{k-1}$, $P_k^-=AP_{k-1}A^{\mathsf T}+Q$.
Update (16.40): $v_k=y_k-Hm_k^-$, $S_k=HP_k^-H^{\mathsf T}+R$, $K_k=P_k^-H^{\mathsf T}S_k^{-1}$, $m_k=m_k^-+K_kv_k$, $P_k=P_k^--K_kS_kK_k^{\mathsf T}$. All matrices are evaluated at θ.

*Proof.* The Kalman filter gives $p(x_k\mid y_{1:k-1},\theta)=\mathrm N(x_k\mid m_k^-,P_k^-)$. By Theorem 16.1 (p. 332),
$$p(y_k\mid y_{1:k-1},\theta)=\int\mathrm N(y_k\mid Hx_k,R)\,\mathrm N(x_k\mid m_k^-,P_k^-)\,dx_k=\mathrm N(y_k\mid Hm_k^-,HP_k^-H^{\mathsf T}+R).\tag{16.41}$$
The rest follows from Theorem 16.4.

Starting at $\varphi_0=-\log p(\theta)$ and running to $k=T$ gives $\varphi_T(\theta)$, so $p(\theta\mid y_{1:T})\propto\exp(-\varphi_T(\theta))$ at that θ. This can be used in Metropolis–Hastings or in gradient-free optimization (p. 333).

**Example 16.10 (Gaussian random walk).** The posterior of the noise variance $p(R\mid y_{1:T})$ in the model of Example 6.4 is shown in Figure 16.1, with a formally uniform prior $p(R)\propto1$. The true value lies well within the high-density region. The MAP (equivalently ML) estimate would be smaller than the true value (p. 333).

Gradients: differentiate (16.38) and each Kalman filter equation to get sensitivity equations (Theorem A.10, Section A.10), or use Fisher's identity (p. 334).

*EM for linear models.* The smoothing distributions are (from (12.5), (12.12)) (p. 334)
$$p(x_k\mid y_{1:T},\theta^{(n)})=\mathrm N(x_k\mid m_k^s,P_k^s),$$
$$p(x_k,x_{k-1}\mid y_{1:T},\theta^{(n)})=\mathrm N\!\left(\begin{bmatrix}x_k\\x_{k-1}\end{bmatrix}\Big|\begin{bmatrix}m_k^s\\m_{k-1}^s\end{bmatrix},\begin{bmatrix}P_k^s&P_k^sG_{k-1}^{\mathsf T}\\G_{k-1}P_k^s&P_{k-1}^s\end{bmatrix}\right).\tag{16.42}$$
The cross term $P_k^sG_{k-1}^{\mathsf T}$ needs no separate recursion, though the literature sometimes uses one (p. 334).

**Theorem 16.11 (Q for the linear Gaussian model)** (p. 335):
$$\begin{aligned}\mathcal Q(\theta,\theta^{(n)})=&-\tfrac12\log|2\pi P_0|-\tfrac T2\log|2\pi Q|-\tfrac T2\log|2\pi R|\\&-\tfrac12\mathrm{tr}\big\{P_0^{-1}[P_0^s+(m_0^s-m_0)(m_0^s-m_0)^{\mathsf T}]\big\}\\&-\tfrac T2\mathrm{tr}\big\{Q^{-1}[\Sigma-CA^{\mathsf T}-AC^{\mathsf T}+A\Phi A^{\mathsf T}]\big\}\\&-\tfrac T2\mathrm{tr}\big\{R^{-1}[D-BH^{\mathsf T}-HB^{\mathsf T}+H\Sigma H^{\mathsf T}]\big\},\end{aligned}\tag{16.43}$$
where all model matrices are functions of θ and, from RTS smoothers run with $\theta^{(n)}$,
$$\Sigma=\tfrac1T\sum_{k=1}^T\big(P_k^s+m_k^s[m_k^s]^{\mathsf T}\big),\quad \Phi=\tfrac1T\sum_{k=1}^T\big(P_{k-1}^s+m_{k-1}^s[m_{k-1}^s]^{\mathsf T}\big),\quad B=\tfrac1T\sum_{k=1}^Ty_k[m_k^s]^{\mathsf T},$$
$$C=\tfrac1T\sum_{k=1}^T\big(P_k^sG_{k-1}^{\mathsf T}+m_k^s[m_{k-1}^s]^{\mathsf T}\big),\quad D=\tfrac1T\sum_{k=1}^Ty_ky_k^{\mathsf T}.\tag{16.44}$$
(Added step, shapes in our notation; the unit does not state dimensions: if $x_k\in\mathbb R^n$, $y_k\in\mathbb R^m$, then $\Sigma,\Phi,C,A,Q$ are $n\times n$, $B,H$ are $m\times n$, and $D,R$ are $m\times m$.)

The M-step is closed-form when θ is some of the full model matrices or the initial mean, or when parameters appear linearly in a matrix. Full-matrix estimation is the classical case (pp. 335–336).

**Theorem 16.12 (maximization of Q)** (p. 336). Setting $\partial\mathcal Q/\partial\theta=0$ separately for each of $\{A,H,Q,R,P_0,m_0\}$:
$$P_0^*=P_0^s+(m_0^s-m_0)(m_0^s-m_0)^{\mathsf T}\tag{16.45}$$
$$A^*=C\Phi^{-1}\tag{16.46}$$
$$Q^*=\Sigma-CA^{\mathsf T}-AC^{\mathsf T}+A\Phi A^{\mathsf T}\tag{16.47}$$
$$H^*=B\Sigma^{-1}\tag{16.48}$$
$$R^*=D-HB^{\mathsf T}-BH^{\mathsf T}+H\Sigma H^{\mathsf T}\tag{16.49}$$
$$m_0^*=m_0^s\tag{16.50}$$
For any subset of matrices, solve the resulting equations jointly (p. 336).

**Algorithm 16.13 (EM for linear state space models).** From $\theta^{(0)}$, for $n=0,1,\dots$: E-step: run the RTS smoother with $\theta^{(n)}$ and compute (16.44). M-step: new values from (16.45)–(16.50) go into $\theta^{(n+1)}$ (p. 336).

The expression for $\mathcal Q$ also gives an "easy gradient recipe" via Fisher's identity, with no sensitivity equations (Theorem A.11) (p. 337).

*Intuition note.* In the linear Gaussian case the E-step is "run a smoother", and the M-step is a regression-like formula. For example $A^*=C\Phi^{-1}$ is a least-squares fit of $x_k$ on $x_{k-1}$ using smoothed second moments.

#### 16.3.3 Gaussian filtering and smoothing (pp. 337–340)
Model (16.51): $x_k=f(x_{k-1},\theta)+q_{k-1}$, $y_k=h(x_k,\theta)+r_k$, with Gaussian noises and initial state as in (16.37) (p. 337).

**Algorithm 16.14 (Gaussian-filter energy).** The recursion is (16.38) with "$\simeq$": $\varphi_k\simeq\varphi_{k-1}+\frac12\log|2\pi S_k|+\frac12v_k^{\mathsf T}S_k^{-1}v_k$ (16.52), with $v_k,S_k$ from a Gaussian filter with θ fixed (pp. 337–338). Prediction (16.53), with $N=\mathrm N(x_{k-1}\mid m_{k-1},P_{k-1})$:
$$m_k^-=\int f(x_{k-1},\theta)\,N\,dx_{k-1},\quad P_k^-=\int(f-m_k^-)(f-m_k^-)^{\mathsf T}N\,dx_{k-1}+Q_{k-1}.$$
Update (16.54), with $N=\mathrm N(x_k\mid m_k^-,P_k^-)$:
$$\mu_k=\int h(x_k,\theta)N\,dx_k,\quad v_k=y_k-\mu_k,\quad S_k=\int(h-\mu_k)(h-\mu_k)^{\mathsf T}N\,dx_k+R_k,$$
$$C_k=\int(x_k-m_k^-)(h-\mu_k)^{\mathsf T}N\,dx_k,\quad K_k=C_kS_k^{-1},\quad m_k=m_k^-+K_kv_k,\quad P_k=P_k^--K_kS_kK_k^{\mathsf T}.$$
The derivation is the same as Theorem 16.9, with Gaussian moment-matching approximations in place of exact Gaussians (p. 338).

The energy can go into MCMC or gradient-free optimization. Because it is Gaussian-approximate, the implied posterior is approximate and estimates will be biased. The approximate posterior is also typically thinner than the true one, so parameter uncertainty is underestimated (p. 338). Derivatives: for the EKF, differentiate its equations formally (Mbalawata et al., 2013). For sigma-point filters, extra care is needed for the derivative of the matrix square root; see Algorithm A.12 (p. 338).

**Algorithm 16.15 (Q via Gaussian smoothing)** (p. 339):
$$\begin{aligned}\mathcal Q\simeq&-\tfrac12\log|2\pi P_0|-\tfrac T2\log|2\pi Q|-\tfrac T2\log|2\pi R|-\tfrac12\mathrm{tr}\{P_0^{-1}[P_0^s+(m_0^s-m_0)(m_0^s-m_0)^{\mathsf T}]\}\\&-\tfrac12\sum_{k=1}^T\mathrm{tr}\{Q^{-1}\mathrm E[(x_k-f(x_{k-1},\theta))(x_k-f(x_{k-1},\theta))^{\mathsf T}\mid y_{1:T}]\}\\&-\tfrac12\sum_{k=1}^T\mathrm{tr}\{R^{-1}\mathrm E[(y_k-h(x_k,\theta))(y_k-h(x_k,\theta))^{\mathsf T}\mid y_{1:T}]\},\end{aligned}\tag{16.55}$$
with expectations over the Gaussian smoother's counterparts of (16.42). The integrals can be approximated by Taylor series (EKF/ERTSS) or sigma points (Gauss–Hermite, cubature, unscented). The M-step for noise covariances is (16.56), with expectations as in (16.55):
$$Q^*=\tfrac1T\sum_{k=1}^T\mathrm E[(x_k-f)(x_k-f)^{\mathsf T}\mid y_{1:T}],\qquad R^*=\tfrac1T\sum_{k=1}^T\mathrm E[(y_k-h)(y_k-h)^{\mathsf T}\mid y_{1:T}].$$
Other parameters depend on the form of f and h. If parameters appear linearly, closed forms like Theorem 16.12 are possible. If iterative optimization is needed anyway, one may as well minimise the energy directly (p. 339). Fisher's identity gives gradients in principle, but the approximations may not match (p. 340; Exercise 16.6).

#### 16.3.4 Iterated filtering and smoothing (p. 340)
Iterated filters/smoothers can approximate the energy like Gaussian filters, taking the final iterate. Catch: the iterated linearization depends on θ in a complicated way. The energy is still easy to evaluate, but the gradient then also depends on the derivative of the linearization result with respect to θ, so sensitivity equations no longer suffice (Christianson, 1994).

#### 16.3.5 Particle filtering and smoothing (pp. 340–344)
For the generic model (16.57) (same as (16.1)), the marginal likelihood is estimated inside the SIR filter.

**Algorithm 16.16 (SIR-based energy approximation)** (p. 341). Draw $x_0^{(i)}\sim p(x_0\mid\theta)$ (16.58), set $w_0^{(i)}=1/N$. For $k=1,\dots,T$:
1. $x_k^{(i)}\sim\pi(x_k\mid x_{k-1}^{(i)},y_{1:k},\theta)$ (16.59).
2. Weights $v_k^{(i)}=\dfrac{p(y_k\mid x_k^{(i)},\theta)\,p(x_k^{(i)}\mid x_{k-1}^{(i)},\theta)}{\pi(x_k^{(i)}\mid x_{k-1}^{(i)},y_{1:k},\theta)}$ (16.60), and $\hat p(y_k\mid y_{1:k-1},\theta)=\sum_iw_{k-1}^{(i)}v_k^{(i)}$ (16.61).
3. Normalised weights $w_k^{(i)}\propto w_{k-1}^{(i)}v_k^{(i)}$ (16.62).
4. Resample if the effective number of particles (11.31) is too low.

Then (p. 342)
$$p(y_{1:T}\mid\theta)\approx\prod_k\hat p(y_k\mid y_{1:k-1},\theta),\qquad \varphi_T(\theta)\approx-\log p(\theta)-\sum_{k=1}^T\log\hat p(y_k\mid y_{1:k-1},\theta).\tag{16.63, 16.64}$$
Used in Metropolis–Hastings, this gives *particle MCMC* (PMCMC), specifically the particle marginal Metropolis–Hastings (PMMH) variant. It is exact in the sense that it samples from the right distribution (Andrieu et al., 2010), so the result is (asymptotically) the same as with the exact energy (p. 342).

**Example 16.17 (pendulum model, noise variance).** Figure 16.2 compares the posterior of $R$ from a fifth-order Gauss–Hermite filter with a PMCMC histogram, which should approach the true posterior. The Gaussian-filter posterior is a good approximation here (pp. 342–343).

For optimization, the particle-filter likelihood is not continuous in θ even with a fixed random number sequence, so gradient-free optimization may be hard and gradient-based optimization is impossible (p. 343). For the Rao–Blackwellized particle filter (Algorithm 11.13), set the weight to (p. 343)
$$v_k^{(i)}=\frac{p(y_k\mid u_{0:k}^{(i)},y_{1:k-1},\theta)\,p(u_k^{(i)}\mid u_{k-1}^{(i)},\theta)}{\pi(u_k^{(i)}\mid u_{0:k-1}^{(i)},y_{1:k},\theta)},\tag{16.65}$$
with the likelihood estimate still given by (16.61).

*Particle EM.* **Algorithm 16.18 (backward-simulation smoother)**: with $S$ trajectories $\{\tilde x_{0:T}^{(i)}\}$ simulated using $\theta^{(n)}$ (Algorithm 15.2) (p. 344),
$$I_1\approx\tfrac1S\sum_i\log p(\tilde x_0^{(i)}\mid\theta),\quad I_2\approx\sum_{k=0}^{T-1}\tfrac1S\sum_i\log p(\tilde x_{k+1}^{(i)}\mid\tilde x_k^{(i)},\theta),\quad I_3\approx\sum_{k=1}^T\tfrac1S\sum_i\log p(y_k\mid\tilde x_k^{(i)},\theta).\tag{16.66}$$
**Algorithm 16.19 (reweighting smoother, Algorithm 15.7)**, with smoothing weights $w_{k|T}^{(i)}$ (p. 344):
$$I_1\approx\sum_iw_{0|T}^{(i)}\log p(x_0^{(i)}\mid\theta),\quad I_3\approx\sum_{k=1}^T\sum_iw_{k|T}^{(i)}\log p(y_k\mid x_k^{(i)},\theta),$$
$$I_2\approx\sum_{k=0}^{T-1}\sum_i\sum_j\frac{w_{k+1|T}^{(j)}w_k^{(i)}p(x_{k+1}^{(j)}\mid x_k^{(i)},\theta^{(n)})}{\sum_lw_k^{(l)}p(x_{k+1}^{(j)}\mid x_k^{(l)},\theta^{(n)})}\log p(x_{k+1}^{(j)}\mid x_k^{(i)},\theta).\tag{16.67}$$
Differentiating these in θ gives approximations of $\partial\mathcal Q/\partial\theta$, usable in Fisher's identity for energy gradients (p. 344).

#### 16.3.6 Rao–Blackwellization of parameters (pp. 345–347)
Model (16.68): $x_k=f(x_{k-1})+q_{k-1}$, $y_k=h(x_k)+r_k$, $r_k\sim\mathrm N(0,R)$, $R\sim\text{Inv-}\chi^2(\nu_0,R_0)$, $q_{k-1}\sim\mathrm N(0,Q)$ (p. 345). Only states are sampled; the distribution of $R$ is carried through its parameters (p. 345).
1. Assume histories $\{w_{k-1}^{(i)},x_{0:k-1}^{(i)}\}$ with $p(x_{0:k-1}\mid y_{1:k-1})\approx\sum_iw_{k-1}^{(i)}\delta(x_{0:k-1}-x_{0:k-1}^{(i)})$ (16.69), and $p(R\mid x_{0:k-1}^{(i)},y_{1:k-1})=\text{Inv-}\chi^2(R\mid\nu_{k-1}^{(i)},R_{k-1}^{(i)})$ (16.70). Then (16.71): $p(x_{0:k-1},R\mid y_{1:k-1})\approx\sum_iw_{k-1}^{(i)}\text{Inv-}\chi^2(R\mid\nu_{k-1}^{(i)},R_{k-1}^{(i)})\delta(x_{0:k-1}-x_{0:k-1}^{(i)})$ (p. 345).
2. Draw $x_k^{(i)}\sim\pi(x_k^{(i)}\mid x_{k-1}^{(i)},y_k)$ (16.72) (p. 346).
3. Integrating $R$ out gives a Student's t predictive (16.73):
$$p(y_k\mid x_k^{(i)},y_{1:k-1})=\int\mathrm N(y_k\mid h(x_k^{(i)}),R)\,\text{Inv-}\chi^2(R\mid\nu_{k-1}^{(i)},R_{k-1}^{(i)})\,dR=t_{\nu_k^{(i)}}(y_k\mid h(x_k^{(i)}),R_k^{(i)}),$$
$$\nu_k^{(i)}=\nu_{k-1}^{(i)}+1,\qquad R_k^{(i)}=\frac{\nu_{k-1}^{(i)}R_{k-1}^{(i)}+(y_k-h(x_k^{(i)}))^2}{\nu_{k-1}^{(i)}+1}.\tag{16.74}$$
Weights: $w_k^{(i)}\propto\dfrac{p(y_k\mid x_k^{(i)},y_{1:k-1})\,\mathrm N(x_k^{(i)}\mid f(x_{k-1}^{(i)}),Q)}{\pi(x_k^{(i)}\mid x_{k-1}^{(i)},y_k)}$ (16.75).
4. Update $p(R\mid x_{0:k}^{(i)},y_{1:k})=\text{Inv-}\chi^2(R\mid\nu_k^{(i)},R_k^{(i)})$ (16.76).
5. Set $k\leftarrow k+1$, optionally resampling jointly the histories and $(\nu_k^{(i)},R_k^{(i)})$.

The whole state histories need not be carried, although the parameters are conditioned on them in theory. The procedure is a Rao–Blackwellized particle filter in which $R$ is carried via sufficient statistics $\nu_k^{(i)},R_k^{(i)}$ (p. 346). The same idea has been used for an unknown population size in a Poisson measurement model (pp. 346–347).

General form (16.77): $x_k\sim p(x_k\mid x_{k-1},\theta)$, $y_k\sim p(y_k\mid x_k,\theta)$, $\theta\sim p(\theta)$. If the posterior of θ depends only on sufficient statistics $T_k=T_k(x_{1:k},y_{1:k})$ (16.78) that are easy to update recursively ($T_k\leftarrow T_{k-1}$), then states and parameters can be sampled by carrying $T_k$ along each sampled history (p. 347). The original idea seems to have appeared quite independently in Storvik (2002), Fearnhead (2002) and Djuric and Miguez (2002) (p. 347). A particularly useful case: the dynamic model does not depend on θ. If, conditionally on $x_k$, the prior $p(\theta)$ is in the conjugate family of the likelihood $p(y_k\mid x_k,\theta)$, then θ can be marginalized out and only states sampled (p. 347). With parameters appearing linearly, it reduces to a noise-free version of conditionally Gaussian Rao–Blackwellization (Section 11.7) (p. 347).

*Intuition note.* If given the sampled states the parameter's posterior has a known closed form, there is no need to sample the parameter. Each particle just stores a few numbers (here ν, R) that summarise what its state history says about the parameter. The text presents this as an alternative to state augmentation (p. 331).

### 16.4 Exercises (p. 348)
Ten implementation/derivation exercises; a selection is given in "Exercises worth doing" below.

## Toy example (ours, not from the text)
Scalar model: $x_0\sim\mathrm N(0,1)$, $x_1=x_0+q_0$ with known $Q=1$, $y_1=x_1+r_1$, $r_1\sim\mathrm N(0,R)$, unknown $R$, prior $p(R)\propto1$. One measurement: $y_1=1$. Aim: compare $R=1$ and $R^*=2$ with a Metropolis step.

Kalman filter with $R$ fixed (Theorem 16.9, $A=H=1$, $T=1$; for $k=1$, $\varphi_0=0$ up to a constant):
- $m_1^-=1\cdot0=0$ and $P_1^-=1\cdot1\cdot1+1=2$.
- $v_1=1-0=1$ and $S_1=2+R$.
- $\varphi_1(R)=\tfrac12\log(2\pi(2+R))+\tfrac12\cdot\frac{1}{2+R}$.

At $R=1$: $S=3$, $\varphi_1=\tfrac12\log(6\pi)+\tfrac16$.
At $R^*=2$: $S=4$, $\varphi_1=\tfrac12\log(8\pi)+\tfrac18$.

Difference: $\varphi(1)-\varphi(2)=\tfrac12\log\frac{6\pi}{8\pi}+\tfrac16-\tfrac18=\tfrac12(-0.28768)+0.04167=-0.14384+0.04167=-0.10217$.

Symmetric proposal, so by (16.19) $\alpha=\min\{1,e^{-0.10217}\}=0.9029$. Check with likelihoods: $\sqrt{3/4}\;e^{-1/8+1/6}=0.8660\times1.0425=0.9029$. So the move from $R=1$ to $R^*=2$ is accepted with probability about 0.90 (accepted if $u\le0.9029$). With more measurements, each step adds one further term $\tfrac12\log|2\pi S_k|+\tfrac12v_k^2/S_k$ to the energy.

## Concepts
- [[state-space-model]] — dynamics and measurement model, here with unknown parameters θ (p. 319)
- [[kalman-filter]] — gives exact $v_k,S_k$, hence the exact energy in linear Gaussian models (p. 332)
- [[observer-state-estimator]] — filters/smoothers are the engines used to score parameters (p. 320)
- [[marginal-likelihood]] (new) — $p(y_{1:T}\mid\theta)$, states integrated out; computed as product of one-step predictive densities (p. 321)
- [[prediction-error-decomposition]] (new) — factorisation (16.5) of the marginal likelihood (p. 321)
- [[energy-function]] (new) — $\varphi_T(\theta)=-\log p(y_{1:T}\mid\theta)-\log p(\theta)$, with $p(\theta\mid y_{1:T})\propto e^{-\varphi_T}$ (p. 322)
- [[map-ml-estimation]] (new) — minimising the energy; ML is MAP with formally uniform prior (p. 323)
- [[laplace-approximation]] (new) — Gaussian around the MAP, covariance = inverse Hessian of the energy (p. 323)
- [[metropolis-hastings]] (new) — MCMC using only energy differences; adaptive (RAM) and Hamiltonian variants (pp. 324–326)
- [[em-algorithm]] (new) — alternate E-step (smoother, $\mathcal Q$) and M-step (maximize $\mathcal Q$) (p. 327)
- [[fishers-identity]] (new) — gradient of $\mathcal Q$ at $\theta^{(n)}=\theta$ gives gradient of the log marginal likelihood (p. 330)
- [[state-augmentation]] (new) — treat θ as a constant extra state; fragile with approximate filters (p. 330)
- [[rao-blackwellization-of-parameters]] (new) — marginalize conjugate static parameters, carry sufficient statistics (p. 345)
- [[particle-mcmc]] (new) — Metropolis–Hastings with particle-filter likelihood estimate; samples the exact posterior (p. 342)

## Canonical instances
- [[gaussian-random-walk-noise-variance]] — posterior of $R$ (Example 16.10); MAP lies below the true value (p. 333)
- [[pendulum-noise-variance]] — Gaussian-filter posterior vs PMCMC histogram (Example 16.17) (p. 343)
- [[inverse-chi-squared-measurement-noise]] — Rao–Blackwellized particle filter with Student's t predictive (p. 345)

## Bridges (candidates)
- [same-math] Kalman innovations $v_k,S_k$ in the energy (16.38) ↔ control-theory: Kalman filter innovation and its covariance — same quantities, here used to score θ.
- [structural-analogy] State augmentation (θ as constant state) ↔ control-theory: joint state and parameter estimation in adaptive estimation — both turn unknown parameters into states to be estimated online.
- [structural-analogy] Energy function and Metropolis acceptance $e^{\Delta\varphi}$ ↔ statistical physics: Boltzmann weights; the text itself uses a physical potential in HMC.
- [structural-analogy] EM (E-step: smooth; M-step: re-fit) ↔ control-theory: alternating state estimation and model identification.

## Questions this raises
- How does the particle-filter likelihood variance (number of particles N) affect PMMH mixing, even though the target is exact?
- When the Gaussian-filter energy underestimates posterior spread, can this be diagnosed without a PMCMC reference?
- How large may the artificial noise ε in (16.36) be before the estimated parameter is meaningfully time-varying rather than static?
- Can EM be used when the iterated-smoother linearization depends on θ (Section 16.3.4)?

## Exercises worth doing
- Ex. 16.1 (p. 348) — EM for the measurement noise variance of the Gaussian random walk; applies Theorem 16.12 in the simplest case — difficulty: easy
- Ex. 16.2 (p. 348) — energy function and its sensitivity-equation gradient, then gradient-based ML — difficulty: medium
- Ex. 16.3 (p. 348) — Fisher's identity derivative; check against sensitivity equations — difficulty: medium
- Ex. 16.4 (p. 348) — random walk Metropolis with Kalman filter energy — difficulty: easy
- Ex. 16.9 (p. 348) — PMCMC with a bootstrap filter on the random walk model — difficulty: medium

## Reading notes
- Printed pages 319–348 (pdf 349–378); printed = pdf − 30.
- The text layer drops most minus signs, and Greek letters (θ, φ, ν, δ) are garbled. Pages 351, 354, 358, 359, 362, 363, 365, 366, 369, 371–376 were checked against images. Page 330 (Fisher's identity) had no image; its minus signs in (16.32) are restored from the definition (16.9), not read from an image.
- Misprint on p. 329: "On the E-step of Algorithm 16.8, we need to maximize …" — the maximization is the M-step.
- (16.46)–(16.49) and the M-step in Algorithm 16.13 contain other model matrices (e.g. A in (16.47), H in (16.49)); the text does not spell out which values (old or new) are used for them when several matrices are estimated jointly ("solving the resulting equations jointly", p. 336).
- Appendix material (Theorems A.10, A.11, Algorithm A.12) is referenced but not included in this unit.
- The sentence on p. 336 in Theorem 16.12 header uses "$\theta^*=\arg\max_\theta\mathcal Q$"; no discrepancy found.
- The shape remark in the Theorem 16.11 walkthrough is ours; the chapter does not give dimensions.
