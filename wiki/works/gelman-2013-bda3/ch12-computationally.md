---
id: gelman-2013-bda3/ch12-computationally
work: gelman-2013-bda3
unit: "12 Computationally efficient Markov chain simulation"
pages: 293-310
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Computationally efficient Markov chain simulation

## L0 — One line
Gibbs and Metropolis samplers can be made much more efficient by reparameterizing, tuning, adding auxiliary variables, and by Hamiltonian Monte Carlo, which uses gradients and momentum to suppress random-walk behaviour.

## L1 — The gist (≤ 120 words)
Basic Gibbs and Metropolis samplers can move slowly, with random-walk behaviour that remains especially for high-dimensional targets. This chapter asks how to speed them up. Cheap fixes are reparameterization, auxiliary variables, parameter expansion, and Metropolis jumping rules tuned to a target acceptance rate. Tempering helps with multiple modes, reversible jump with changing dimension, and slice sampling is a general tool, especially for one-dimensional conditionals. The chapter's central method is Hamiltonian Monte Carlo (HMC). It adds momentum variables and uses the gradient of the log posterior so that each iteration can move farther. The chapter gives its algorithm and tuning rules, an eight-schools example, and Stan, which automates HMC with the no-U-turn sampler.

**Prerequisites:** Gibbs sampler and Metropolis–Hastings (Ch. 11); detailed balance; Jacobians of transformations; gradients of log densities; $\hat R$ and effective sample size; the eight-schools hierarchical model (Ch. 5).

## L2 — Key ideas (5–10 bullets)
- Gibbs works best with independent components. Auxiliary variables (data augmentation) and parameter expansion (adding an extra parameter that the data cannot identify) can simplify or speed it; the t model becomes a normal mixture with variances $V_i$ (pp. 293–295).
- For a multivariate normal target, among random-walk Metropolis rules with a normal kernel shaped like the target (covariance $c^2\Sigma$), scale $c\approx 2.4/\sqrt d$ is the most efficient. Its efficiency is about $0.3/d$, and its optimal acceptance rate is 0.44 in 1-D, about 0.23 for roughly $d>5$ (p. 296).
- A rule that adapts while the chain runs generally converges to the wrong distribution. So tune in an adaptive phase and keep only a later fixed phase (p. 297).
- Reversible jump handles models with different dimensions by adding auxiliary variables so dimensions match. Tempering (sampling from flattened versions of the target) and other methods help with multimodality (pp. 297–300).
- HMC adds momentum $\phi$ with $p(\phi)=\mathrm N(0,M)$ and simulates leapfrog dynamics (a discrete mimic of physical motion). It then applies a Metropolis accept/reject on the joint density. It needs the gradient of the log posterior (pp. 300–302).
- HMC tuning: momentum scales, step size $\epsilon$, steps $L$. Heuristics are $\epsilon L\approx1$ and about 65% acceptance. Except in some special cases, adapting from earlier iterations breaks convergence, so tuning is done in warm-up (early iterations that are discarded); completely random variation of $\epsilon, L$ causes no convergence problems (pp. 303–304).
- The no-U-turn sampler (NUTS, which ends each trajectory when it turns back) and Riemannian adaptation (the mass matrix follows local curvature) adapt HMC without losing detailed balance. Neither solves every problem (pp. 304–305).
- Eight-schools worked example: gradients, mass matrix, jittered $\epsilon, L$, and a log τ transformation. Stan automates HMC with automatic differentiation and NUTS (pp. 305–308).

## L3 — Walkthrough

### Chapter introduction (p. 293)
Gibbs and Metropolis are building blocks for more advanced simulation. Sections 12.1–12.2 cover reparameterization and tuning. Section 12.4 presents HMC, a Metropolis generalization with "momentum" variables that allow farther moves and faster mixing, especially in high dimensions. Sections 12.5–12.6 give a hierarchical application and the program Stan (p. 293).

### 12.1 Efficient Gibbs samplers

**Transformations and reparameterization (p. 293).** Gibbs is most efficient when parameterized in independent components. Figure 11.2 shows slow convergence with dependent components. The simplest fix is a linear transformation. Posteriors that are not approximately normal may need special methods. The same holds for Metropolis: in a (near-)normal setting the jumping kernel should ideally have the target's covariance structure. This can be estimated from the normal approximation at the mode (Chapter 13). For multimodal targets, allowing jumps between modes helps greatly.

**Auxiliary variables (p. 293).** Adding auxiliary variables, such as mixture indicators, can simplify Gibbs computations or speed convergence. This is also called *data augmentation*.

**Example: t distribution as a mixture of normals (pp. 293–294).** Data $y_1,\dots,y_n$ are independent $t_\nu(\mu,\sigma^2)$ with $\nu$ known and a uniform prior on $\mu,\log\sigma$. The t likelihood is equivalent to

$$y_i\sim \mathrm N(\mu,V_i),\qquad V_i\sim \text{Inv-}\chi^2(\nu,\sigma^2),\tag{12.1}$$

where the $V_i$ are unobserved auxiliary variables. Simulating from $p(\mu,\sigma^2,V\mid y)$ and keeping only $\mu,\sigma$ gives the posterior under the original t model. The authors say there is no direct way to sample $\mu,\sigma^2$ in the t model, but Gibbs on $(V,\mu,\sigma^2)$ is straightforward (p. 294):

1. Each $V_i$ is a normal variance with a scaled inverse-$\chi^2$ prior, so (Section 2.6)
$$V_i\mid\mu,\sigma^2,\nu,y\sim\text{Inv-}\chi^2\!\Big(\nu+1,\ \frac{\nu\sigma^2+(y_i-\mu)^2}{\nu+1}\Big).$$
The $V_i$ are conditionally independent.
2. With the uniform prior on $\mu$,
$$\mu\mid\sigma^2,V,\nu,y\sim\mathrm N\!\Big(\frac{\sum_i y_i/V_i}{\sum_i 1/V_i},\ \frac{1}{\sum_i 1/V_i}\Big).$$
3. All information about $\sigma$ comes from the $V_i$:
$$p(\sigma^2\mid\mu,V,\nu,y)\propto\sigma^{-2}\prod_{i=1}^n\sigma^{\nu}e^{-\nu\sigma^2/(2V_i)}=(\sigma^2)^{n\nu/2-1}\exp\Big(-\frac\nu2\sum_i\frac1{V_i}\sigma^2\Big)\propto\text{Gamma}\Big(\sigma^2\Big|\frac{n\nu}2,\frac\nu2\sum_i\frac1{V_i}\Big).$$

*Intuition note:* The t distribution is a normal whose variance is random. If we also sample the variances, every conditional distribution becomes a standard one. Throwing away the $V_i$ at the end leaves exactly the t-model posterior for $\mu,\sigma$.

**Parameter expansion (pp. 294–295).** Some Gibbs samplers are slow because of posterior dependence that no linear transformation resolves. The authors say, paradoxically, that adding a parameter (a larger space) can improve convergence. In form (12.1), convergence is slow if $\sigma$ is near zero. Then the $V_i$ are drawn near zero, which keeps $\sigma$ near zero, and so on. The expanded model is

$$y_i\sim\mathrm N(\mu,\alpha^2U_i),\qquad U_i\sim\text{Inv-}\chi^2(\nu,\tau^2),$$

with $\alpha>0$ an extra scale and a uniform prior on $\log\alpha$. Here $\alpha^2U_i$ plays the role of $V_i$ and $\alpha\tau$ the role of $\sigma$. The four Gibbs steps (p. 295):

1. $U_i\mid\cdot\sim\text{Inv-}\chi^2\Big(\nu+1,\ \dfrac{\nu\tau^2+((y_i-\mu)/\alpha)^2}{\nu+1}\Big)$.
2. $\mu\mid\cdot\sim\mathrm N\Big(\dfrac{\sum_i y_i/(\alpha^2U_i)}{\sum_i 1/(\alpha^2U_i)},\ \dfrac{1}{\sum_i 1/(\alpha^2U_i)}\Big)$.
3. $\tau^2\mid\cdot\sim\text{Gamma}\Big(\dfrac{n\nu}2,\ \dfrac\nu2\sum_i\dfrac1{U_i}\Big)$.
4. $\alpha^2\mid\cdot\sim\text{Inv-}\chi^2\Big(n,\ \dfrac1n\sum_i\dfrac{(y_i-\mu)^2}{U_i}\Big)$.

$\alpha^2,U,\tau$ are not identified, but the model as a whole is if we monitor $\mu$, $\sigma=\alpha\tau$ and $V_i=\alpha^2U_i$ (or just save $\mu,\sigma$). The sampler converges more reliably because $\alpha$ breaks the dependence between $\tau$ and the $V_i$ (p. 295). Parameter expansion for hierarchical models is in Section 15.5 (p. 295).

*Intuition note:* The chain can get stuck when $\sigma$ and the $V_i$ are both near zero and keep each other there. The extra scale $\alpha$ lets the $V_i$ move as a group without changing $\tau$, so the chain has more directions to escape.

### 12.2 Efficient Metropolis jumping rules (pp. 295–296)
Metropolis–Hastings can be implemented in infinitely many ways. With conjugate families, Gibbs can often be used; it is generally easy to program but not always efficient. Nonconjugate models need Metropolis–Hastings, within Gibbs or directly. There are two main classes of simple jumping rules (p. 296):
- Random walks, typically normal kernels centred at the current value, with variance set for efficiency.
- Proposals built to approximate the target closely, so that most draws are accepted and the accept step mainly corrects the approximation.

The authors see no natural advantage in altering one parameter at a time, except potential computational savings from evaluating only part of the density (p. 296).

**Optimal scale (p. 296).** Suppose the posterior of $\theta=(\theta_1,\dots,\theta_d)$ is, after transformation, multivariate normal with known variance $\Sigma$. Take Metropolis draws with kernel $J(\theta^*\mid\theta^{t-1})=\mathrm N(\theta^*\mid\theta^{t-1},c^2\Sigma)$. Among this class the most efficient has $c\approx 2.4/\sqrt d$, with efficiency defined relative to independent sampling. Its efficiency can be shown to be about $0.3/d$. By comparison, if the $d$ parameters were independent, Gibbs would have efficiency $1/d$, because every $d$ iterations give a new independent draw. Which algorithm is best also depends on the computation time per iteration (p. 296).

**Acceptance rate (p. 296).** For the same normal setting, the optimal acceptance rate is about 0.44 in one dimension, declining to about 0.23 in high dimensions (roughly $d>5$). This suggests an adaptive algorithm:
1. Start parallel simulations with a fixed algorithm, for example Gibbs, or Metropolis with a normal random walk shaped like an estimate of the target. That estimate is the covariance at the joint or marginal posterior mode, scaled by $2.4/\sqrt d$.
2. After some simulations: (a) set the jumping covariance proportional to the posterior covariance estimated from the simulations; (b) raise or lower the scale if the acceptance rate is much too high or low, aiming at about 0.44 (one dimension) or 0.23 (vector jumping).

The authors found even this simple form useful for $d$ from 1 to 50 (p. 296).

*Intuition note (our gloss, not stated on these pages):* Tiny jumps are almost always accepted but barely move. Huge jumps are mostly rejected. The best step is in between, and the acceptance rate tells you where you are.

**Adaptive algorithms (p. 297).** If the tuning rule depends on previous steps, the transition probabilities are more complicated than in Metropolis–Hastings, and in general the iterations will not converge to the target. Example: an adaptation that moves quickly through flat regions and slowly where the density changes quickly. It would spend disproportionately less time in flat parts, so the draws would not match the target unless corrected. To be safe, run two phases: an adaptive phase, then a fixed phase long enough for approximate convergence. Only fixed-phase draws are used for inference (p. 297).

### 12.3 Further extensions to Gibbs and Metropolis

**Slice sampling (p. 297).** Sampling $\theta$ from $p(\theta\mid y)$ is equivalent to sampling uniformly from the area under it. Formally, sample $(\theta,u)$ with $p(\theta,u\mid y)\propto1$ for $u\in[0,p(\theta\mid y)]$ and 0 otherwise. Slice sampling is iterative simulation on this uniform distribution. It is general and especially useful for one-dimensional conditionals in Gibbs.

**Reversible jump (pp. 297–299).** This handles trans-dimensional chains, where the dimension of the parameter space changes between iterations. Examples are model averaging over regressions with different predictors, and finite mixtures with a variable number of components. Let $M_k$, $k=1,\dots,K$, be the candidate models and $\theta_k$ the parameters of model $k$, with dimension $d_k$. A move $k\to k^*$ generates an auxiliary $u\sim J(u\mid k,k^*,\theta_k)$. A one-to-one deterministic function gives $(\theta_{k^*},u^*)=g_{k,k^*}(\theta_k,u)$ with $d_k+\dim(u)=d_{k^*}+\dim(u^*)$. Dimension matching ensures the balance condition from Chapter 11 still holds (pp. 297–298). Let $\pi_k$ be the prior model probability. The algorithm samples $p(k,\theta_k\mid y)$ (p. 298):
1. From $(k,\theta_k)$, propose model $k^*$ with probability $J_{k,k^*}$ and draw $u$.
2. Set $(\theta_{k^*},u^*)=g_{k,k^*}(\theta_k,u)$.
3. Compute
$$r=\frac{p(y\mid\theta_{k^*},M_{k^*})p(\theta_{k^*}\mid M_{k^*})\pi_{k^*}}{p(y\mid\theta_k,M_k)p(\theta_k\mid M_k)\pi_k}\cdot\frac{J_{k^*,k}J(u^*\mid k^*,k,\theta_{k^*})}{J_{k,k^*}J(u\mid k,k^*,\theta_k)}\left|\frac{\nabla g_{k,k^*}(\theta_k,u)}{\nabla(\theta_k,u)}\right|\tag{12.2}$$
and accept with probability $\min(r,1)$.

The draws give posterior model probabilities and within-model parameters.

*Example: variance component in a turtle survival regression (p. 298–299).* Turtle $i$ in family $j$ has $\Pr(y_{ij}=1)=p_{ij}=\Phi(\alpha_0+\alpha_1x_{ij}+b_j)$, with exchangeable family effects $b_j\sim\mathrm N(0,\tau^2)$. The authors say they prefer fitting the model with $\tau$ and examining its posterior (Chapters 6–7). They say it might be of interest to allow $\tau=0$ as a discrete possibility, and they choose this example to illustrate the algorithm. $M_0$ has $\tau=0$; $M_1$ includes the variance component. The marginal likelihood $p(y\mid\alpha_0,\alpha_1,\tau)$ for $M_1$ is computed by numerical integration, so the $b_j$ are not simulated. Take $\pi_0=\pi_1=0.5$ and all $J_{k,k'}=0.5$. Each step is either a Metropolis step within the model (probability 0.5) or a proposed jump. For $0\to1$: draw $u\sim J(u)$ (scaled inverse-$\chi^2$), set $\tau^2=u$, and keep $\alpha_0,\alpha_1$. Then

$$r=\frac{p(y\mid\alpha_0,\alpha_1,\tau^2,M_1)p(\tau^2)}{p(y\mid\alpha_0,\alpha_1,M_0)J(\tau^2)},$$

because the priors on $\alpha$ and on the models cancel and the Jacobian is 1. For $1\to0$ there is no auxiliary variable; set $\tau=0$, and the acceptance probability is the reciprocal of the above. $J(\tau^2)$ was an inverse-$\chi^2$ matching the posterior mean and variance from a pilot analysis of $M_1$ (p. 299).

*Intuition note:* To compare a model with a variance parameter to one without, the chain must move between spaces of different size. The auxiliary draw $u$ fills the missing coordinate so the proposal is a one-to-one map and the usual accept ratio, with a Jacobian, still applies.

**Simulated and parallel tempering (pp. 299–300).** Multimodal posteriors are hard, mainly when modes are separated by regions of extremely low density, so Metropolis jumps between them are rejected (p. 299). Simulated tempering uses $K+1$ distributions $p_k(\theta\mid y)$ with $p_0=$ the target. Each has its own sampler and only needs an unnormalized density $q_k$. One choice is

$$q_k(\theta)=p(\theta\mid y)^{1/T_k}\,p_0(\theta)^{1-1/T_k},\qquad T_k>0,$$

where $T_k=1$ gives the original density and large $T_k$ flattens the modes towards a high-variance base measure $p_0$. Set $T_0=1$. The state is $(\theta^t,s^t)$, where $s^t$ indexes the distribution in use. Each iteration (p. 299):
1. Draw $\theta^{t+1}$ using a Markov chain with stationary distribution $q_{s^t}$.
2. Propose a jump from $s^t$ to $j$ with probability $J_{s^t,j}$ and accept with probability $\min(r,1)$, where
$$r=\frac{c_jq_j(\theta^{t+1})J_{j,s^t}}{c_{s^t}q_{s^t}(\theta^{t+1})J_{s^t,j}}.$$

The constants $c_k$ are set adaptively to approximate the inverses of the normalizing constants of the $q_k$. The chain then spends about equal time in each sampler. Only draws from the target sampler ($q_0$) are used for inference. Parallel tempering runs $K+1$ parallel chains, one per $q_k$, with occasional state flips between chains under a similar Metropolis rule. At convergence, chain 0 gives target draws (p. 300). Multigrid sampling, for highly correlated variables such as in spatial statistics, alternates computation on the original scale and coarser scales (p. 300).

**Particle filtering, weighting, genetic algorithms (p. 300).**
- *Particle filtering:* parallel chains are periodically allowed to die, live or split. Chains in lower-probability areas are more likely to die and those in higher-probability areas to split. The step probabilities are set so that the whole process has the posterior as stationary distribution.
- *Weighting:* simulate from a specified but wrong distribution $g(\theta)$, then weight the draws by $p(\theta\mid y)/g(\theta)$. This can be done throughout the simulation, and can be combined with particle filtering by using the weights in the die/live/split probabilities.
- *Genetic algorithms:* like particle filtering, but the updating algorithms themselves can mutate and combine.

### 12.4 Hamiltonian Monte Carlo (pp. 300–305)

**Motivation (p. 300).** Gibbs and Metropolis have inherent random-walk behaviour (zigzagging, Figures 11.1–11.2). Reparameterization and good jumping rules help, but the local random walk remains for complicated, high-dimensional targets. HMC borrows an idea from physics. It adds a momentum variable $\phi_j$ for each component $\theta_j$. Both are updated in a new Metropolis algorithm in which the jump for $\theta$ is determined largely by $\phi$. Trajectories can move rapidly and turn corners to preserve total "energy". HMC is also called hybrid Monte Carlo (p. 300).

**Set-up (p. 301).** The joint distribution is $p(\theta,\phi\mid y)=p(\phi)p(\theta\mid y)$. Only $\theta$ is of interest; $\phi$ is auxiliary. HMC needs $p(\theta\mid y)$ up to a constant and the gradient $\frac{d\log p(\theta\mid y)}{d\theta}=\Big(\frac{d\log p}{d\theta_1},\dots,\frac{d\log p}{d\theta_d}\Big)$. In practice the gradient must be analytic, because numerical differentiation needs too many function evaluations. The authors recommend also programming a finite-difference gradient to check the analytic one. If the two do not agree to several decimal places, there is likely a mistake (p. 301).

**Momentum distribution (p. 301).** Usually $\phi\sim\mathrm N(0,M)$ with a prespecified "mass matrix" $M$, commonly diagonal, so $\phi_j\sim\mathrm N(0,M_{jj})$ independently. It can help for $M$ to roughly scale with $(\mathrm{var}(\theta\mid y))^{-1}$, but the algorithm works in any case. Better scaling only makes it more efficient.

**One iteration (pp. 301–302).**
1. Draw $\phi\sim\mathrm N(0,M)$ (its posterior equals its prior).
2. Repeat $L$ times these leapfrog steps with step scale $\epsilon$:
 - (a) $\phi\leftarrow\phi+\tfrac12\epsilon\,\dfrac{d\log p(\theta\mid y)}{d\theta}$
 - (b) $\theta\leftarrow\theta+\epsilon M^{-1}\phi$
 - (c) $\phi\leftarrow\phi+\tfrac12\epsilon\,\dfrac{d\log p(\theta\mid y)}{d\theta}$

 Updates (c) and (a) can be merged except at the first and last step. The stepping thus starts with a half-step of $\phi$, alternates $L-1$ full steps of $\theta$ and $\phi$, and ends with a half-step of $\phi$. The authors keep $\epsilon$ separate from $M$ because it is convenient to alter $\epsilon$ while holding $M$ fixed (p. 301). The algorithm is a discrete approximation to continuous Hamiltonian dynamics (p. 302).
3. With $\theta^{t-1},\phi^{t-1}$ at the start and $\theta^*,\phi^*$ after $L$ steps, compute
$$r=\frac{p(\theta^*\mid y)p(\phi^*)}{p(\theta^{t-1}\mid y)p(\phi^{t-1})}.\tag{12.3}$$
4. Set $\theta^t=\theta^*$ with probability $\min(r,1)$, otherwise $\theta^t=\theta^{t-1}$. There is no need to store $\phi^t$, as it is redrawn at step 1 (p. 302).

Convergence is judged as usual by $\hat R$ near 1 and enough effective sample size (Section 11.4) (p. 302).

**Why it works (intuition only; no proof given, p. 302).** In the limit $\epsilon\to0$ the leapfrog algorithm preserves the joint density $p(\theta,\phi\mid y)$.
- On a flat part of the posterior the gradient is zero, so momentum stays constant and the trajectory skates at constant velocity.
- Heading into lower density, the gradient is negative along the motion, so momentum falls. The drop in $\log p(\theta\mid y)$ is matched (exactly, as $\epsilon\to0$) by a drop in "kinetic energy" $\log p(\phi)$. The trajectory may slow, back down or curve around.
- Heading into higher density, momentum grows until the path passes the mode.
- For finite $\epsilon$ the joint density varies only slowly if $\epsilon$ is small. The authors say errors from $L$ steps do not add up to $L\delta$, because they tend to weave around the exact value. Low discretization error matters for the accept/reject step.

*Intuition note:* In the limit $\epsilon\to0$ the leapfrog path preserves the joint density $p(\theta,\phi\mid y)=p(\phi)p(\theta\mid y)$ (p. 302), and for small $\epsilon$ it changes only slowly. The ratio $r$ in (12.3) compares exactly this joint density at the end and the start of the path. So a far-away proposal can still have $r$ near 1 (our reading).

**Restricted parameters (p. 303).** HMC needs positive densities. At a point of zero density (for example a positive-only parameter stepping below zero), stop and spend the iteration at the previous $\theta$; this preserves detailed balance. Alternatively, "bounce": flip the sign of the momentum, which also preserves detailed balance and is typically more efficient. A third way is to transform (log, logit, or joint transformations for constraints like $\theta_1<\theta_2<\theta_3$ or $\alpha_1+\dots+\alpha_4=1$). Then use the Jacobian in the log posterior and its gradient (p. 303).

**Tuning (pp. 303–304).** There are three places: the momentum scales (diagonal of $M$), the step factor $\epsilon$, and the number of steps $L$. Tuning can be fixed in advance or varied completely at random. But adaptive updating from previous iterations generally breaks convergence, so tune during warm-up, discard those iterations, and save only iterations after the last tuning. The recipe:
- Set momentum scales to a crude estimate of the target scale (default: identity matrix).
- Set $\epsilon L=1$, so $L$ steps should roughly cross the distribution. A default start is $\epsilon=0.1$, $L=10$.
- Theory suggests optimal efficiency near 65% acceptance. This is based on an analysis like the one giving 23% for multidimensional Metropolis, with many assumptions, but the authors call it a reasonable guideline. If acceptance is lower, steps are too ambitious: lower $\epsilon$ and raise $L$ (keep the product 1). If it is much higher, raise $\epsilon$ and lower $L$ ($L$ an integer) (pp. 303–304).

**Varying during the run (p. 304).** Adapting $\epsilon$ during inference runs, for example raising it after high-probability jumps and lowering it after low acceptance, would destroy detailed balance. Detailed balance means probability flow from A to B equals that from B to A. Completely random variation of $\epsilon$ and $L$ within specified ranges causes no convergence problems. It allows long tours when possible and short moves where cramped. The price is some loss of optimality.

**Locally adaptive HMC (pp. 304–305).** Ideally $M$ would follow local curvature, $\epsilon$ would shrink where curvature is high, and $L$ would be long but not circling. Researchers have developed extensions that adapt without losing detailed balance; two are described, without details:
- *No-U-turn sampler (NUTS):* the trajectory continues until the dot product of momentum $\phi$ and the displacement from the starting position becomes negative. Alone this rule does not converge to the target; the full sampler goes backward and forward along the trajectory to satisfy detailed balance. $M$ and $\epsilon$ are tuned in warm-up and then fixed.
- *Riemannian adaptation:* $M$ follows the local curvature of the log posterior at each step. It can be combined with NUTS.

Neither solves everything. NUTS, like plain HMC, has difficulties with very short-tailed and long-tailed distributions, in transitioning from centre to tails, even in one dimension. Riemannian adaptation handles varying curvature and non-exponential tails but is impractical in high dimensions (p. 305).

**Combining HMC with Gibbs (p. 305).** (1) Block updating: in a hierarchical model $\theta=(\eta^{(1)},\dots,\eta^{(J)},\phi)$ with $p(\theta\mid y)\propto p(\phi)\prod_jp(\eta^{(j)}\mid\phi)p(y^{(j)}\mid\eta^{(j)})$, it may be better to cycle through $J+1$ updates, each touching at most one likelihood factor, even if HMC could update all at once. Parameter expansion may help mixing. (2) Discrete parameters: Hamiltonian dynamics are defined only for continuous distributions. Discrete components can be updated by Gibbs, Metropolis or slice steps, alternating with HMC on the continuous part.

### 12.5 HMC for a hierarchical model: eight schools (pp. 305–307)
HMC is unnecessary here (Gibbs works well, especially with parameter expansion), but this is a simple illustration. The school effects are called $\alpha_j$, so $\theta=(\alpha_1,\dots,\alpha_8,\mu,\tau)$ has $d=10$ (p. 305). The code is in Section C.4 (p. 305).

**Gradients (pp. 305–306).**
$$\frac{d\log p(\theta\mid y)}{d\alpha_j}=-\frac{\alpha_j-y_j}{\sigma_j^2}-\frac{\alpha_j-\mu}{\tau^2},\ j=1,\dots,8;\qquad \frac{d\log p}{d\mu}=-\sum_{j=1}^J\frac{\mu-\alpha_j}{\tau^2};\qquad \frac{d\log p}{d\tau}=-\frac J\tau+\sum_{j=1}^J\frac{(\mu-\alpha_j)^2}{\tau^3}.$$
They check these against finite differences of $\pm0.0001$ and then use the analytic version, which is faster (p. 306).

**Set-up (p. 306).** Mass matrix: the authors look at Table 5.2, assign a rough scale of 15 to each parameter, and set $M=\mathrm{Diag}(15^{-2},\dots,15^{-2})$. Four chains start from independent $\mathrm N(0,15^2)$ draws. They do not fix $\epsilon$ and $L$: they choose centres $\epsilon_0,L_0$ and each step draw $\epsilon\sim\mathrm U(0,2\epsilon_0)$ and $L$ discrete uniform on $[1,2L_0]$. The authors say they have no reason to think this jitter is ideal. Start with $\epsilon_0L_0=1$, $L_0=10$.

**Tuning sequence (p. 306).**
| Run | $\epsilon_0, L_0$ | Result |
|---|---|---|
| 4 chains, 20 iterations | 0.1, 10 | check the program runs |
| 4 chains, 100 iterations | 0.1, 10 | several $\hat R>2$; acceptance 0.23, 0.59, 0.02, 0.57 (well below 65%, step size suspected too large) |
| 4 chains, 100 iterations | 0.05, 20 | acceptance 0.72, 0.87, 0.33, 0.55; chains still not mixing |
| 1000 iterations | 0.05, 20 | $\hat R<1.2$ for all parameters; acceptance 0.52, 0.68, 0.75, 0.51 |
| 10,000 iterations | 0.05, 20 | approximate convergence, $\hat R<1.1$ |

**Transforming to $\log\tau$ (pp. 306–307).** To avoid leaving the boundary $\tau>0$, redefine $\theta=(\alpha_1,\dots,\alpha_8,\mu,\log\tau)$ and:
1. Do all jumping in the new space.
2. Multiply the posterior by the Jacobian $\tau$, adding $\log\tau$ to the log posterior.
3. The gradient for the last component becomes $\dfrac{d\log p(\theta\mid y)}{d\log\tau}=-(J-1)+\sum_{j=1}^J\dfrac{(\mu-\alpha_j)^2}{\tau^2}$.
4. Mass: 15 for $\alpha_1,\dots,\alpha_8,\mu$ and 1 for $\log\tau$.
5. Initial values: first nine from $\mathrm N(0,15^2)$, $\log\tau\sim\mathrm N(0,1)$.

HMC then runs as before, starting at $\epsilon=0.1$, $L=10$ (p. 307).

*(added step)* The gradient in item 3 follows from the chain rule: $\tau\cdot(-J/\tau+\sum(\mu-\alpha_j)^2/\tau^3)+1=-J+1+\sum(\mu-\alpha_j)^2/\tau^2$.

### 12.6 Stan (pp. 307–308)
Stan ("Sampling through adaptive neighborhoods") applies HMC automatically to a Bayesian model. The authors found HMC faster and more reliable in more complicated settings (p. 307). The steps are:
- **Data and model input.** The model is coded as a log density. Standard distributions are preprogrammed and arbitrary log densities can be entered. All of this is sent to C++. Gradients are computed by automatic analytic differentiation. Special scalar classes evaluate the function while building the expression tree. A reverse pass propagates partial derivatives by the chain rule, implicitly using dynamic programming. This is typically much faster than finite differences (pp. 307–308).
- **Warm-up.** NUTS removes the need to set $L$. During a prespecified warm-up, Stan adapts $M$ and $\epsilon$ using ideas from stochastic optimization. This will not always work: for distributions with varying curvature there is in general no single good set. Inspecting $M$ and $\epsilon$ across chains can help diagnosis, and reparameterization can help. Riemannian adaptation was being incorporated at the time of writing (p. 308).
- **Sampling.** Stan transforms bounded variables to an unconstrained scale where possible. For complicated constraints the user may need to reparameterize. It tracks acceptance probabilities (p. 308).
- **Postprocessing.** Warm-up iterations are discarded but saved for diagnostics. $\hat R$ and $n_{\rm eff}$ are computed (Section 11.4) (p. 308).

### 12.7 Bibliographic note (pp. 308–309)
A list of references for each topic: auxiliary variables, parameterization, acceptance-rate results (Gelman, Roberts and Gilks 1995), adaptive MCMC, slice sampling, tempering, reversible jump (Green 1995), HMC (Duane et al. 1987; Neal 1994, 2011), NUTS (Hoffman and Gelman 2014), Riemannian updating (Girolami and Calderhead 2011), and algorithmic differentiation (Griewank and Walther 2008). Not digested further.

### 12.8 Exercises (pp. 309–310)
Four exercises (see below).

## Toy example (ours, not from the text)
One leapfrog trajectory (L = 1) of HMC on a standard normal target, so $\log p(\theta)=-\theta^2/2$ and the gradient is $-\theta$. Take $M=1$, so $p(\phi)\propto e^{-\phi^2/2}$. Take $\epsilon=0.5$, start at $\theta=1$, and suppose the momentum draw is $\phi=0.5$.
- (a) Half-step of momentum: $\phi=0.5+\tfrac12(0.5)(-1)=0.5-0.25=0.25$.
- (b) Position: $\theta=1+0.5\cdot1\cdot0.25=1.125$.
- (c) Half-step of momentum, gradient $-1.125$: $\phi=0.25+0.25(-1.125)=0.25-0.28125=-0.03125$.
- Energy before: $(1^2+0.5^2)/2=0.625$. After: $(1.125^2+0.03125^2)/2=(1.265625+0.0009765625)/2=0.63330078$.
- $\log r=0.625-0.63330078=-0.00830078$, so $r=e^{-0.0083}\approx0.9917$. The jump from 1 to 1.125 is accepted with probability about 0.99.

A random-walk Metropolis step of the same size would have ratio $e^{-(1.125^2-1)/2}=e^{-0.1328}\approx0.876$. HMC follows the gradient, so the move keeps nearly the same joint density.

## Concepts
- [[markov-chain-monte-carlo]] — random walk whose long-run distribution is the posterior; this chapter is about making it efficient (p. 293)
- [[gibbs-sampling]] — cycle through conditional draws; most efficient with independent components (p. 293)
- [[metropolis-hastings]] — propose and accept/reject; many possible jumping rules $J_t$ (p. 295)
- [[hamiltonian-monte-carlo]] — Metropolis on $(\theta,\phi)$ with leapfrog trajectories using $\nabla\log p$; "hybrid Monte Carlo" (pp. 300–302)
- [[convergence-diagnostics]] — $\hat R$ near 1 and large effective sample size judge HMC convergence (p. 302)
- [[data-augmentation]] (new) — adding auxiliary variables (e.g., mixture indicators, the $V_i$) to simplify Gibbs or speed convergence (p. 293)
- [[parameter-expansion]] (new) — adding an unidentified parameter (e.g., $\alpha$) to break dependence and speed Gibbs (p. 294)
- [[optimal-acceptance-rate]] (new) — about 0.44 (1-D) to 0.23 (high-$d$) for random-walk Metropolis with the target's shape; about 65% suggested for HMC (pp. 296, 303)
- [[adaptive-mcmc-and-warm-up]] (new) — tune only in an adaptive/warm-up phase and discard it; adaptation during inference generally breaks convergence (pp. 297, 303)
- [[reversible-jump-mcmc]] (new) — Metropolis between models of different dimension, using auxiliary $u$ and a Jacobian (p. 297)
- [[slice-sampling]] (new) — iterative sampling from the uniform distribution under the density curve (p. 297)
- [[simulated-tempering]] (new) — chain moves across tempered densities $q_k$ to cross between modes; parallel tempering uses parallel chains (p. 299)
- [[leapfrog-integrator]] (new) — discrete half-step/full-step update of $\phi$ and $\theta$ approximating Hamiltonian dynamics (p. 301)
- [[mass-matrix]] (new) — covariance $M$ of the momentum distribution in HMC (p. 301)
- [[detailed-balance]] (new) — flow of probability from A to B equals that from B to A; used to prove the target is stationary (p. 304)
- [[no-u-turn-sampler]] (new) — HMC that stops each trajectory when it starts to turn back, with $L$ chosen adaptively (p. 304)
- [[automatic-differentiation]] (new) — Stan's expression-tree reverse pass for exact gradients (p. 307)

## Canonical instances
- [[t-model-as-normal-mixture]] — t likelihood written with auxiliary variances $V_i$; Gibbs steps, then parameter expansion with $\alpha$ (pp. 293–295)
- [[turtle-probit-reversible-jump]] — jump between a model with and without variance component $\tau$ (pp. 298–299)
- [[eight-schools-hmc]] — HMC tuning on the educational-testing model, with a log τ transformation (pp. 305–307)
- [[stan]] — software implementing NUTS with autodiff and warm-up (pp. 307–308)

## Bridges (candidates)
- [structural-analogy] HMC's energy $-\log p(\theta)-\log p(\phi)$ conserved along a trajectory ↔ physics: Hamiltonian dynamics conserve total energy — the chapter says HMC imitates this, with the accept step correcting discretization error.
- [same-math] Weighting draws by $p(\theta\mid y)/g(\theta)$ (p. 300) ↔ importance sampling: same ratio of target to proposal density.
- [structural-analogy] Tempering temperature $T_k$ flattening modes ↔ statistical physics "thermal noise": high temperature makes barriers between modes passable.
- [structural-analogy] Parameter expansion (extra unidentified scale) ↔ hierarchical models: the chapter points to Section 15.5 for the hierarchical use.

## Questions this raises
- Why would the optimal acceptance rate for HMC (about 65%) exceed that of random-walk Metropolis (about 23%)? The chapter says only that the theory has many assumptions.
- When the posterior has varying curvature, no single $(M,\epsilon)$ works. How do NUTS and Riemannian adaptation diagnose or fix this in practice?
- Which tuning rules that adapt on the fly preserve detailed balance? The chapter says they exist but gives no details.
- How should one choose between a Gibbs sampler with parameter expansion and HMC for a hierarchical model, given the eight-schools example where both work?

## Exercises worth doing
- Ex. 1 (p. 309) — apply the adaptive jumping-rule algorithm of Section 12.2 to the Exercise 11.2 problem; shows how acceptance-rate tuning behaves — difficulty: medium
- Ex. 2 (p. 309) — Cauchy model with two distant observations (1.3 and 15.0): compare Metropolis with simulated tempering using 10 inverse temperatures — difficulty: hard
- Ex. 3 (p. 309) — program HMC in R for the bioassay logistic regression: check analytic vs numerical gradients, tune to about 65% acceptance, compare with Chapter 3 — difficulty: hard
- Ex. 4 (pp. 309–310) — simulate data from a logistic regression with $t_4$ priors, fit with Stan, check 50% interval coverage, then use rejection sampling for independent draws — difficulty: medium

## Reading notes
- Printed page numbers are given on every page; printed = pdf − 10.
- The text layer shows garbled symbols (θ appears as ω, ∼ as →, ← as ∝). All math here was checked against the page images, which show θ, ∼ and ←.
- The turtle example heading says "logistic regression" but the model in the text is a probit regression, $\Phi(\cdot)$ (p. 298).
- On p. 299, $p_0$ denotes both the target $p_0(\theta\mid y)=p(\theta\mid y)$ and the "base measure" $p_0(\theta)$ in $q_k$, as printed.
- p. 306: the mass matrix is written $\mathrm{Diag}(15^{-2},\dots)$. Later on p. 307 the masses are described as "15" for the same parameters and 1 for $\log\tau$. Whether this means a variance, an inverse variance, or a scale is not clarified in these pages.
- p. 306: the acceptance rates for the second 100-iteration run are printed "0.72,, 0.87, 0.33, and 0.55" with a doubled comma, so I read them as four values.
- Exercise 4 (p. 309) prints "U(1,1)" for the distribution of $x_j$, which is a degenerate interval; a different lower bound was presumably intended. The text does not say so.
- Section 12.7 (bibliography) was only summarized; no references were checked.
- Section 12.8 refers to Exercise 11.2, which is not in this unit.
- p. 302: the text says the decrease in $\log p(\theta\mid y)$ is matched by a decrease in the "kinetic energy" $\log p(\phi)$. The same page says the joint density $p(\theta,\phi\mid y)$ is preserved as $\epsilon\to0$. Read literally, the two logs would then move in opposite directions, so the wording is loose. The digest reports it as printed.
