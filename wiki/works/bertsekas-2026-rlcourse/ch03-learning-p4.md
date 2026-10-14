---
id: bertsekas-2026-rlcourse/ch03-learning-p4
work: bertsekas-2026-rlcourse
unit: "3 Learning Values and Policies (part 4/5): end of Sec. 3.4 example; Sec. 3.5 Policy Gradient and Related Methods (3.5.1–3.5.5, start of 3.5.6)"
pages: 408–428
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Policy Gradient and Related Methods (Sec. 3.5)

## L0 — One line
Instead of fitting a fixed policy, one can parametrize policies by a vector $r$ and minimize the expected cost over $r$ directly, using sampling-based gradient, scaled-gradient, random-direction or random-search methods; the last two need only simulated cost values, and the likelihood-ratio gradient additionally needs $\nabla\log p$.

## L1 — The gist (≤ 120 words)
How can we train a parametrized policy to be (nearly) optimal, directly, off-line? The section minimizes $E\{J_{\tilde\mu(r)}(i_0)\}$ over $r$. Because the cost may be non-differentiable or only simulable, the author randomizes the problem and uses the likelihood-ratio gradient, which needs no model of the cost. He then covers baselines, scaled and natural gradients (Fisher matrix, trust regions, PPO), a projected natural gradient for $r\ge 0$ with a cost-improvement guarantee under stated conditions, random-direction methods, and cross-entropy random search. He warns that an off-line policy used alone lacks the Newton-step power of lookahead minimization.

**Prerequisites:** gradients and Hessians; expected value and sums over a finite set; Newton's method; positive definite matrices; Bellman/policy ideas of earlier chapters.

## L2 — Key ideas (5–10 bullets)
- Direct policy optimization minimizes $E\{J_{\tilde\mu(r)}(i_0)\}$ over $r$, aiming at an optimal policy rather than a fixed one (p. 408).
- An off-line trained policy used alone will not perform nearly as well as the same policy combined with lookahead minimization (a one-step minimization over controls using a cost estimate), because lookahead supplies the exact Newton step (p. 409).
- Non-differentiability can be smoothed by the soft-max approximation (a smooth log-sum-exp stand-in for a max), and probability constraints can be removed by a soft-max (exponential-normalization) reparametrization of randomized policies. Probability-1 controls then correspond to infinite parameters (pp. 410–412).
- Optimization over $z\in Z$ becomes optimization over distributions $p(z;r)$. The likelihood-ratio formula (3.47) writes the gradient as an expectation of $\nabla\log p\cdot F$, so it can be sampled; the resulting iteration (3.48) is called model-free by the author and needs $\nabla\log p$ and simulated costs $F(z)$ (pp. 412–414).
- A baseline $b$ (a scalar subtracted from the cost $F$) leaves the true gradient unchanged but changes the sampled gradient, so optimizing it can improve performance (pp. 416–417).
- Multiplying the gradient by a positive definite scaling matrix (Newton, diagonal, Fisher information) is a principal technique against slow convergence. The natural gradient scales by the inverse Fisher matrix $E\{\nabla\log p\,\nabla\log p'\}$, and PPO combines such scaling with forms of trust region (a constraint that keeps each step small) (pp. 417–421).
- For constraints $r\ge0$, naive clipping with the full Fisher matrix can fail. If the positive definite matrix is diagonal with respect to $I^+(r)=\{i: r_i=0,\ g_i(r)>0\}$, then at a nonstationary $r$ a small enough stepsize guarantees cost improvement (Prop. 3.5.1) (pp. 422–424).
- Random-direction methods use two function values per iteration. Cross-entropy random search needs no gradients, no differentiability and no model, only a simulator (pp. 425–428).

## L3 — Walkthrough

### End of the Sec. 3.4 example (p. 408)
This unit starts inside a linear-quadratic example, so its set-up is not on these pages. The optimal gain is $L^*\approx -0.4$ and the optimal cost is $J^*(x)=K^*x^2$ with $K^*\approx 1.1$. For the policy $\mu_L(x)=Lx$ with $L\ne L^*$, the cost is $J_\mu(x)=K_Lx^2$. Using $J_\mu$ as cost approximation in a one-step lookahead (Newton) step gives a policy $\tilde\mu(x)=\tilde Lx$ with cost $K_{\tilde L}x^2$. When $L-L^*$ is substantial, the degradation $K_{\tilde L}-K^*$ is negligible, while $K_L-K^*$ is substantial (p. 408).

*Intuition note:* In this example, even when the gain $L$ is far from $L^*$, one lookahead step applied to $\mu_L$ gives a policy whose cost $K_{\tilde L}x^2$ is almost optimal.

### 3.5 Policy gradient and related methods (pp. 408–409)
- Infinite horizon problems. Policies are parametrized by $\tilde\mu(r)$ and $r$ is found from
$$\min_r E\{J_{\tilde\mu(r)}(i_0)\},\tag{3.39}$$
  with $i_0$ drawn from a suitable distribution (Fig. 3.5.1). This is contrasted with the classification approach, which learns a fixed policy (p. 408).
- If $i_0$ is known and fixed, one just minimizes $J_{\tilde\mu(r)}(i_0)$. This is simpler, especially for deterministic problems (p. 408).
- The section focuses on off-line training. On-line training, where a controller learns while interacting (e.g. in robotics), is beyond scope (pp. 408–409).
- Warning: an off-line trained policy used without value-space approximation will not perform nearly as well as the same policy with lookahead minimization, because it lacks the exact Newton step (p. 409).

### 3.5.1 Gradient methods for parametric cost optimization (pp. 409–412)
Assume $i_0$ known and $J_{\tilde\mu(r)}(i_0)$ differentiable in $r$, with positive stepsize $\gamma^k$:
$$r^{k+1}=r^k-\gamma^k\nabla J_{\tilde\mu(r^k)}(i_0),\qquad k=0,1,\dots \tag{3.40}$$
- Gradients may be unavailable, so finite differences of cost values are used. In stochastic problems the cost values may be computable only by Monte Carlo simulation. This may bring a lot of noise, so many samples will likely need to be averaged, making the method inefficient. For deterministic problems this difficulty does not arise, and gradient-free methods such as coordinate descent are easier to use (p. 410).
- The rest of the section treats gradient-like, sampling-based methods for stochastic problems (p. 410).

**Soft-max smoothing.** A term $f(r)=\max\{f_1(r),\dots,f_m(r)\}$ can be approximated by
$$\frac1c\ln\Big\{\sum_{i=1}^m\lambda_i e^{c f_i(r)}\Big\},\quad c>0,\ \sum_i\lambda_i=1,\ \lambda_i>0 .$$
Larger $c$ gives a better approximation but a more ill-conditioned problem, harder for gradient methods. The $\lambda_i$ can be seen as Lagrange multipliers, which when chosen properly improve the approximation near an optimal solution (pp. 410–411).

**Constraints by reparametrization.** For finite states $i=1,\dots,n$ and controls $u\in U(i)$, replace an ordinary policy by a randomized one that applies $u$ at state $i$ with probability $r_u(i)$, subject to
$$\sum_{u\in U(i)} r_u(i)=1,\quad r_u(i)\ge0 .\tag{3.41}$$
The randomized-policy set is continuous, hence suited to gradient methods, but needs simplex constraints. One can remove them with the transformation
$$r_u(i)\approx\frac{e^{\theta_u(i)\phi(i)}}{\sum_{v\in U(i)}e^{\theta_v(i)\phi(i)}},\tag{3.42}$$
where $\phi(i)$ are scalars depending on $i$ (p. 412). Serious difficulty: a control applied with probability 1 maps to $\theta_u(i)=\infty$. The transformation is nonetheless widely used (p. 412).

*Intuition note:* Soft-max turns unconstrained numbers into valid probabilities. The price is that a control applied with probability 1 corresponds to an infinite parameter.

### 3.5.2 Policy gradient-like methods (pp. 412–417)
**Randomization.** Take the generic problem $\min_{z\in Z}F(z)$ (3.43), where $F$ may be non-differentiable and $Z$ discrete. Convert it to
$$\min_{p\in\mathcal P_Z}E_p\{F(z)\},\tag{3.44}$$
with $\mathcal P_Z$ the distributions over $Z$. This enlarges the search space but enables randomized, simulation-based methods and may give differentiability that (3.43) lacks (p. 412). In the DP context this requires randomized policies (p. 413). Restricting to distributions $p(z;r)$ with continuous parameter $r$ gives
$$\min_r E_{p(z;r)}\{F(z)\},\tag{3.45}$$
$$r^{k+1}=r^k-\gamma^k\nabla\big(E_{p(z;r^k)}\{F(z)\}\big).\tag{3.46}$$
The parametrization must be differentiable in $r$, e.g. $p(z;r)=e^{r'\phi(z)}/\sum_{y\in Z}e^{r'\phi(y)}$ (footnote, p. 413).

**Likelihood-ratio (log-likelihood) trick.** Interchange gradient and expectation and use $\nabla\log p=\nabla p/p$ (p. 413):
$$\nabla E_{p(z;r)}\{F(z)\}=\nabla\Big(\sum_{z\in Z}p(z;r)F(z)\Big)=\sum_z\nabla p(z;r)F(z)=\sum_z p(z;r)\frac{\nabla p(z;r)}{p(z;r)}F(z)=\sum_z p(z;r)\nabla\big(\log p(z;r)\big)F(z).$$
$$\nabla E_{p(z;r)}\{F(z)\}=E_{p(z;r)}\big\{\nabla\big(\log p(z;r)\big)F(z)\big\}\tag{3.47}$$

**Sample-based method** (p. 414): (a) sample $z^k\sim p(z;r^k)$; (b) compute $\nabla(\log p(z^k;r^k))$; (c) iterate
$$r^{k+1}=r^k-\gamma^k\nabla\big(\log p(z^k;r^k)\big)F(z^k).\tag{3.48}$$
It is simple and general, going beyond DP, provided $\log p(z;r)$ is differentiable and $z$ can be sampled. The direction does not involve the gradient of $F$ at all. The iteration is "model-free": one need not know the form of $F$, only have a simulator giving $F(z)$ (besides being able to compute $\nabla\log p$) (p. 414).

*Intuition note:* The expectation depends on $r$ only through how likely each $z$ is. So we nudge $r$ to make low-cost samples more probable and high-cost ones less probable.

**Example 3.5.1 (discounted DP, p. 415–416).** Let $z=\{i_0,u_0,i_1,u_1,\dots\}$ with randomized policy $p(u\mid i;r)$, so $z$ has distribution $p(z;r)$, and
$$F(z)=\sum_{m=0}^\infty\alpha^m g(i_m,u_m,i_{m+1}).\tag{3.49}$$
Method (3.48) needs a sampled trajectory $z^k$, its cost $F(z^k)$ and the sampled gradient
$$\nabla\big(\log p(z^k;r^k)\big).\tag{3.50}$$
Assume $\log p(u\mid i;r)$ is differentiable in $r$ (soft-max is often recommended). Then
$$\log p(z^k;r^k)=\log\prod_{m=0}^\infty p_{i^k_mi^k_{m+1}}(u^k_m)\,p(u^k_m\mid i^k_m;r^k)=\sum_m\log p_{i^k_mi^k_{m+1}}(u^k_m)+\sum_m\log p(u^k_m\mid i^k_m;r^k).$$
(added step) The first sum does not depend on $r$, so
$$\nabla\big(\log p(z^k;r^k)\big)=\sum_{m=0}^\infty\nabla\big(\log p(u^k_m\mid i^k_m;r^k)\big).\tag{3.51}$$
This gradient involves the policy but not the transition probabilities or stage costs (p. 415). With a horizon cut-off at $N$ steps the method becomes
$$r^{k+1}=r^k-\gamma^k\sum_{m=0}^{N-1}\nabla\log p(u^k_m\mid i^k_m;r^k)\,F_N(z^k_N),$$
where $z^k_N$ is the generated $N$-step trajectory. The initial state is chosen randomly, with due regard to exploration (p. 416).

Variants that parametrize both policy and cost (e.g. lower-variance estimates of $F$, baselines) give actor-critic methods, which differ from the earlier PI-type methods. The policy gradient methods above are sometimes called actor-only, since they involve only policy parametrizations (p. 416).

**Implementation issues** (pp. 416–417).
- *Extracting a solution.* If the limit $\bar r$ gives a non-atomic $p(z;\bar r)$, a solution $\bar z$ must be extracted. In SSP and discounted problems the parametric family typically contains the atomic distributions, and randomization does not improve the optimal cost, so the difficulty does not arise (p. 416).
- *Baseline.* For any scalar $b$,
$$\nabla E_{p(z;r)}\{F(z)\}=E_{p(z;r)}\big\{\nabla\big(\log p(z;r)\big)\big(F(z)-b\big)\big\}.\tag{3.52}$$
  This holds because
$$E\{\nabla\log p(z;r)\}=\sum_z p(z;r)\frac{\nabla p(z;r)}{p(z;r)}=\sum_z\nabla p(z;r)=\nabla\Big(\sum_zp(z;r)\Big)=0,$$
  since $\sum_zp(z;r)\equiv1$ does not depend on $r$ (pp. 416–417). The modified iteration is
$$r^{k+1}=r^k-\gamma^k\nabla\big(\log p(z^k;r^k)\big)\big(F(z^k)-b\big).\tag{3.53}$$
  The baseline $b$ does not change the true gradient but changes the sampled gradient. So optimizing $b$, empirically or by calculation, can improve performance. State-dependent baselines are used for discounted and SSP problems (p. 417).

*Intuition note:* Subtracting a constant from the cost does not change the average direction, because the score has mean zero. It does change each sampled direction, so a well-chosen constant can improve performance.

### 3.5.3 Scaling and proximal policy optimization methods (pp. 417–424)
Gradient-like methods are notorious for slow convergence, worsened by noise. One remedy is a positive definite scaling. For $\min_{r\in\Re^m}f(r)$, $f$ twice continuously differentiable (p. 417):
$$r^{k+1}=r^k-(D^k)^{-1}\nabla f(r^k),\tag{3.54}$$
with $D^k$ positive definite symmetric $m\times m$. Two extremes (p. 418):
- (a) $D^k$ = Hessian: Newton's method. It converges superlinearly when started sufficiently close to a strong local minimum (positive definite Hessian). For least squares $f=\sum_{i=1}^N\|g_i\|^2$, Gauss-Newton neglects second derivatives of $g_i$.
- (b) $D^k$ = diagonal approximation of the Hessian. It converges under appropriate conditions ($D^k$ not too "small"), at a linear rate, typically much slower than Newton's superlinear rate. It is much simpler, admits incremental implementation, and has worked well for neural-network training (cf. ADAM, Sec. 3.1.3).

Equivalent quadratic form (p. 418):
$$r^{k+1}\in\arg\min_{r\in\Re^m}\Big\{\nabla f(r^k)'(r-r^k)+\tfrac12(r-r^k)'D^k(r-r^k)\Big\}.\tag{3.55}$$
Setting the derivative to zero gives $0=\nabla f(r^k)+D^k(r^{k+1}-r^k)$, which is (3.54).

**Gradient projection.** For $\min_{r\in C}f(r)$ (3.56), $C$ closed convex:
$$r^{k+1}\in\arg\min_{r\in C}\Big\{\nabla f(r^k)'(r-r^k)+\tfrac12(r-r^k)'D^k(r-r^k)\Big\}\tag{3.57}$$
$$r^{k+1}=P_{D^k}\big(r^k-\nabla f(r^k)\big),\tag{3.58}$$
where $P_{D^k}$ is projection onto $C$ in the norm defined by $D^k$. Equivalence follows by writing $P_{D^k}(\cdot)=\arg\min_{r\in C}\{(r-r^k+\nabla f(r^k))'D^k(r-r^k+\nabla f(r^k))\}$ and expanding the quadratic. For $C=\Re^m$, (3.57) equals (3.54)–(3.55) (pp. 418–419).

**Proximal minimization** (p. 419):
$$r^{k+1}\in\arg\min_{r\in C}\Big\{f(r)+\tfrac12(r-r^k)'D^k(r-r^k)\Big\}.\tag{3.59}$$
It coincides with gradient projection when $f$ is linear. The two may be combined.

**Trust region** (p. 419):
$$r^{k+1}\in\arg\min_{(r-r^k)'D^k(r-r^k)\le\beta^k}\nabla f(r^k)'(r-r^k),\tag{3.60}$$
$\beta^k>0$. It is equivalent to (3.55) for an appropriate $\beta^k$. $\beta^k$ keeps the increment small, guarding against oscillations that may lead to divergence.

**Natural gradient** (pp. 419–421). For stochastic gradient methods over parametrized distributions, alternative scalings use the Fisher Information Matrix (FIM) instead of an inverse Hessian. For problem (3.61), $\min_rE_{p(z;r)}\{F(z)\}$:
$$M(r)=E_{p(z;r)}\Big\{\nabla\big(\log p(z;r)\big)\nabla\big(\log p(z;r)\big)'\Big\}\tag{3.62}$$
with the gradient a column vector, computed as in Example 3.5.1. The scaled method is
$$r^{k+1}=r^k-\gamma^k\big(M(r^k)\big)^{-1}\nabla\big(E_{p(z;r^k)}\{F(z)\}\big),\tag{3.63}$$
with the gradient given by (3.47). The direction $(M(r^k))^{-1}E\{\nabla\log p(z;r^k)F(z)\}$ is the *natural gradient*. Sampled versions are possible, using (3.51) in discounted DP. Motivation: the FIM defines a norm on distributions that captures the sensitivity of $p(\cdot;r)$ to $r$ more effectively than the norms from the $D^k$. The FIM is the Hessian of the Kullback-Leibler divergence (pp. 420–421). The trust-region analog is
$$r^{k+1}\in\arg\min_{(r-r^k)'M(r^k)(r-r^k)\le\beta^k}\nabla\big(E_{p(z;r^k)}\{F(z)\}\big)'(r-r^k).\tag{3.64}$$
Proximal policy optimization (PPO) of Shulman et al. provides FIM scaling with trust-region forms. The author states it has been used widely, including for training large language models (p. 421).

**Constrained natural gradient** (pp. 421–424). Problem $\min_{r\in C}E_{p(z;r)}\{F(z)\}$ (3.65), $C$ closed convex, e.g. the orthant $C=\{r\mid r\ge0\}$ (3.66). Notation: $g(r)=\nabla(E_{p(z;r)}\{F(z)\})$, $g_i=\partial E\{F\}/\partial r_i$. The unconstrained method is
$$r^{k+1}=r^k-\gamma^k\big(M(r^k)\big)^{-1}g(r^k),\tag{3.67}$$
and its projected analog is
$$r^{k+1}\in\arg\min_{r\in C}\Big\{g(r^k)'(r-r^k)+\frac1{2\gamma^k}(r-r^k)'M(r^k)(r-r^k)\Big\}.\tag{3.68}$$
This has strong convergence guarantees, but the quadratic minimization may be much harder than the inversion in (3.67), even for an orthant (p. 422). A simpler candidate is clipping:
$$r^{k+1}=\big[r^k-\gamma^k\tilde M(r^k)^{-1}g(r^k)\big]^+,\tag{3.69}$$
where $[r]^+_i=\max\{0,r_i\}$ and $\tilde M$ is the FIM or an approximation.

With $\tilde M=M$ (the full FIM) the algorithm does not work. When $r^k$ is on the boundary, the iteration may fail to reduce cost however small $\gamma^k$ is: the unprojected point may improve cost but not the projected one (Fig. 3.5.2(a)). It is even possible that $r^k$ is optimal and the iteration moves away from it (Fig. 3.5.2(b)) (p. 422).

Fix: a symmetric $D$ is *diagonal with respect to* an index set $I$ if $d_{ij}=0$ for all $i\in I$ and $j\ne i$. Define, for $r\ge0$,
$$I^+(r)=\{i\mid r_i=0,\ g_i(r)>0\}.\tag{3.70}$$

**Proposition 3.5.1** (the author's works [Ber82b], [Ber82c]). Let $r\ge0$ and let $\tilde M(r)$ be positive definite symmetric and diagonal with respect to $I^+(r)$. Let $r(\gamma)=[r-\gamma\tilde M(r)^{-1}g(r)]^+$. Suppose $r$ is nonstationary, i.e. violates "$g_i(r)\ge0$ for $r_i=0$, and $g_i(r)=0$ for $r_i>0$". Then there is $\bar\gamma>0$ such that
$$E_{p(z;r(\gamma))}\{F(z)\}<E_{p(z;r)}\{F(z)\}\quad\text{for all }0<\gamma\le\bar\gamma .$$
(Statement only; no proof is given on these pages.) (p. 423)

Consequences (p. 424): in (3.69), $\tilde M(r^k)$ should be diagonal with respect to an index set containing $I^+(r^k)$, with $\gamma^k$ small enough. For convergence one must be more careful, since $I^+$ is discontinuous at the boundary: for interior $r^k\to\bar r$ on the boundary, $I^+(r^k)$ may be strictly smaller than $I^+(\bar r)$. A remedy is to add indices with $g_i(r^k)>0$ and $0\le r^k_i\le\epsilon$, $\epsilon$ small. The method is called the "two-metric projection method" (first proposed in [Ber82c]). The author states its theory is solid and that extensive computational practice has established superior performance over other gradient-type methods. It tends to identify the active constraints quickly and then act as unconstrained natural gradient on that subspace, so it can preserve the FIM scaling and is well-suited to incremental implementation (p. 424).

### 3.5.4 Random direction methods (pp. 424–426)
Incremental versions of $r^{k+1}=r^k-\gamma^k\nabla(E_{p(z;r^k)}\{F(z)\})$ (3.71) using a random direction and two function values per iteration. They are generally faster than finite differences of the whole gradient. They need no derivative of the sampling distribution, but have not been applied widely to policy training in RL (p. 425).

*Scalar case.* $p(z;r)$ is symmetric, with probability $p_i$ at each of $r\pm\epsilon_i$ (Fig. 3.5.3), so $E\{F\}=\sum_{i=1}^mp_i(F(r+\epsilon_i)+F(r-\epsilon_i))$. The gradient iteration is
$$r^{k+1}=r^k-\gamma^k\sum_ip_i\big(\nabla F(r^k+\epsilon_i)+\nabla F(r^k-\epsilon_i)\big).\tag{3.72}$$
Using $\nabla F(r+\epsilon_i)\approx\frac{F(r+\epsilon_i)-F(r)}{\epsilon_i}$ and $\nabla F(r-\epsilon_i)\approx\frac{F(r)-F(r-\epsilon_i)}{\epsilon_i}$:
$$r^{k+1}=r^k-\gamma^k\sum_{i=1}^mp_i\frac{F(r^k+\epsilon_i)-F(r^k-\epsilon_i)}{\epsilon_i}.\tag{3.73}$$
A sampled version uses one term, with $i^k$ drawn with probabilities proportional to $p_{i^k}$ (p. 426):
$$r^{k+1}=r^k-\gamma^k\frac{F(r^k+\epsilon_{i^k})-F(r^k-\epsilon_{i^k})}{\epsilon_{i^k}}.\tag{3.74}$$

*Multidimensional case.* $z=r+\epsilon d$, with $d$ random on the unit sphere and $\epsilon$ independent and symmetric around 0:
$$r^{k+1}=r^k-\gamma^k\frac{F(r^k+\epsilon^kd^k)-F(r^k-\epsilon^kd^k)}{\epsilon^k}d^k.\tag{3.75}$$
For a nonsymmetric distribution ($\epsilon$ zero mean), the analog still needs two function values:
$$r^{k+1}=r^k-\gamma^k\frac{F(r^k+\epsilon^kd^k)-F(r^k)}{\epsilon^k}d^k.\tag{3.76}$$
For symmetric sampling, (3.75) tends to be more accurate and is often preferred. The direction $d^k$ need not be related to the gradient of $F$. Choosing $\gamma^k$ and the distribution of $\epsilon$ can be tricky when $F$ is noisy (p. 426).

### 3.5.5 Random search and cross-entropy methods (pp. 426–428)
Drawbacks of policy gradient methods: unreliability from noisy gradients, slow convergence, local minima. Random search methods need not use randomized policies, need no differentiability, and offer some global convergence guarantees (p. 427). The cross-entropy method (Fig. 3.5.4) for $\min_rE\{J_{\tilde\mu(r)}(i_0)\}$ (p. 427–428):
1. Around $r^k$ draw random sample parameters (in an ellipsoid $E_k$) and generate their cost samples with policy $\tilde\mu$.
2. Accept the samples with "low" cost and reject the rest.
3. Set $r^{k+1}$ to the sample mean of the accepted samples. Form a sample "covariance" matrix of them and a new ellipsoid $E_{k+1}$ with a suitably enlarged radius. Repeat.

It is simple, needs no gradients, differentiability, randomized policies or model (a simulator suffices), and relies on some supportive theory. Its convergence guarantees are limited and success depends on domain-specific insight and heuristics. It was used with impressive success in tetris (p. 428).

### 3.5.6 Refining and retraining parametric policies (start, p. 428)
Given a pre-trained parametric policy (e.g. a neural network), one may want to refine it, e.g. to correct a bias or poor or unsafe responses at sensitive states. A common way is to modify the cost function to penalize undesirable behavior. This needs a domain-specific dataset of input–output pairs from human or machine feedback, possibly with instructions for critical situations. The section continues beyond these pages (p. 428).

## Toy example (ours, not from the text)
Illustrates the likelihood-ratio gradient (3.47) and baseline (3.52)–(3.53).

Let $Z=\{0,1\}$, $F(0)=2$, $F(1)=0$. Let $p(1;r)=\sigma(r)=e^r/(1+e^r)$ and $p(0;r)=1-\sigma(r)$.
- True gradient: $E\{F\}=2(1-\sigma(r))$, so $\nabla E\{F\}=-2\sigma(r)(1-\sigma(r))$. At $r=0$, $\sigma=0.5$, giving $-2(0.25)=-0.5$.
- Scores: $\nabla\log p(1;r)=1-\sigma=0.5$ and $\nabla\log p(0;r)=-\sigma=-0.5$.
- Formula (3.47): $0.5\cdot(-0.5)(2)+0.5\cdot(0.5)(0)=-0.5$. ✓
- Single-sample estimates with $b=0$: $z=0$ gives $(-0.5)(2)=-1$; $z=1$ gives $0$. Their mean is $-0.5$, but each sample is noisy.
- Baseline $b=1$ (3.52): $z=0$ gives $(-0.5)(2-1)=-0.5$; $z=1$ gives $(0.5)(0-1)=-0.5$. Every sample equals $-0.5$, so the mean is unchanged and the noise is gone here.
- Update (3.53) with $\gamma=0.1$ and $b=1$: $r^{1}=0-0.1(-0.5)=0.05$ for either sample. With $b=0$: $r^1=0.1$ if $z=0$, $r^1=0$ if $z=1$.

## Concepts
- [[policy-gradient]] (new) — minimize expected cost over policy parameters $r$ by gradient steps on $E\{J_{\tilde\mu(r)}(i_0)\}$ (p. 408).
- [[likelihood-ratio-gradient]] (new) — $\nabla E_{p}\{F\}=E_p\{\nabla\log p\cdot F\}$, estimated by one sample (pp. 413–414).
- [[baseline-variance-reduction]] (new) — subtracting a scalar $b$ from $F$ leaves the true gradient unchanged but alters the sampled one (p. 417).
- [[policy]] — here a map $\tilde\mu(i,r)$ from states to controls (or to control probabilities), parametrized by $r$ (p. 408).
- [[model-based vs model-free RL]] — the author calls (3.48) "model-free" because only simulated $F(z)$ is needed, not the form of $F$ (p. 414).
- [[soft-max-parametrization]] (new) — exponential-normalization map giving probabilities from unconstrained parameters (3.42); also smooths a max (pp. 410–412).
- [[scaled-gradient-method]] (new) — $r^{k+1}=r^k-(D^k)^{-1}\nabla f(r^k)$, with Newton and diagonal scalings as extremes (p. 417).
- [[natural-gradient]] (new) — gradient scaled by the inverse Fisher information matrix (3.62)–(3.63) (p. 420).
- [[proximal-policy-optimization]] (new) — FIM scaling plus trust-region-type step control (p. 421).
- [[two-metric-projection]] (new) — clipped natural gradient with $\tilde M$ diagonal on $I^+(r)$ (3.69), Prop. 3.5.1 (pp. 422–424).
- [[random-direction-method]] (new) — update along a random direction using two cost values (3.75)–(3.76) (p. 426).
- [[cross-entropy-method]] (new) — random search that re-centres on accepted low-cost samples (pp. 427–428).
- [[exploration vs exploitation]] — only touched: initial states are chosen randomly "with due regard to exploration issues" (p. 416).

## Canonical instances
- [[lq-one-step-lookahead-example]] — one lookahead step from a suboptimal linear policy gives a near-optimal one ($K_{\tilde L}\approx K^*$) (p. 408).
- [[policy-gradient-discounted-dp]] — Example 3.5.1, trajectory score $\sum_m\nabla\log p(u_m\mid i_m;r)$ with no transition model (p. 415).
- [[orthant-clipping-failure]] — Fig. 3.5.2, the clipped full-FIM iteration fails at the boundary (p. 423).
- [[tetris-cross-entropy]] — cross-entropy method used with impressive success (p. 428).

## Bridges (candidates)
- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity.
- [same-math] soft-max smoothing $\frac1c\ln\sum\lambda_ie^{cf_i}$ ↔ optimization: log-sum-exp smoothing of a max.
- [structural-analogy] FIM scaling ↔ Newton's method: both rescale the gradient by curvature, in different norms.
- [structural-analogy] trust-region/proximal steps ↔ control: small-step policy updates that avoid divergence from large changes.
- [structural-analogy] cross-entropy method ↔ evolutionary search: a population is resampled around the best members.

## Questions this raises
- When is a policy gradient method preferable to approximation in value space with lookahead, given the warning about the missing Newton step (p. 409)?
- How should the baseline $b$ (or a state-dependent baseline) be chosen to minimize variance?
- Why does a diagonal block on $I^+(r)$ restore descent, and can its proof be seen geometrically?
- How do actor-critic methods combine the policy gradient with a learned cost estimate?

## Reading notes
- Part boundaries: starts mid-example at the top of p. 408 (end of the Sec. 3.4 linear-quadratic example, set-up not included). Ends mid-Sec. 3.5.6 at the foot of p. 428.
- Printed = pdf − 20.
- Exercise 3.2 is cited several times (pp. 412–413) but its text is not in these pages, so no exercises are listed.
- Proposition 3.5.1's proof is not given here (the proposition is attributed to the author's works [Ber82b], [Ber82c]).
- Misprints visible in the images: p. 422 "$I\subset\{1,\dots,n\}$" where $m$ is the dimension (indices elsewhere run to $m$); p. 422 text says "for $g^k$ sufficiently small" where $\gamma^k$ is evidently meant; p. 418 (a),(b) use $x^k$ for the iterate where (3.54) uses $r^k$.
- The text layer of equations was garbled (arrows for minus signs, "ǫ" for $\epsilon$). All equations were checked against the page images.
