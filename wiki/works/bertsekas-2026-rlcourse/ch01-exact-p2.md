---
id: bertsekas-2026-rlcourse/ch01-exact-p2
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 2/6): §1.3 Stochastic DP, §1.4 Infinite horizon problems (start)"
pages: 28-55
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Stochastic and infinite-horizon DP, and approximation in value and policy space

## L0 — One line
The DP recursion carries over to random disturbances and infinite horizons, and because exact solutions are rare, one replaces the optimal cost-to-go by an approximation (lookahead, rollout) or replaces the optimal policy by a trained parametric one.

## L1 — The gist (≤ 120 words)
How do we extend dynamic programming (DP) from deterministic to stochastic problems, and then to infinite horizons? The recursion keeps its form if we optimize over policies (feedback laws) instead of control sequences and take expectations. Exact solutions are rare; linear-quadratic problems are one case. So the unit introduces approximation in value space (one-step or ℓ-step lookahead, rollout), approximation in policy space (fitted parametric policies), and, for infinite horizons, Bellman's equation, value iteration and policy iteration. It matters because these are the building blocks of the RL methods developed later in the book.

**Prerequisites:** expectation and variance; minimizing a quadratic by setting the derivative to zero; deterministic finite-horizon DP and the cost-to-go (from §1.1–1.2); least-squares regression; limits of sums; Newton's method for solving equations (only mentioned here).

## L2 — Key ideas
- In stochastic problems the unknown is a *policy* (a function from state to control), not a control sequence, because feedback can use the observed state. The DP recursion then takes the expectation over the disturbance (p. 29, p. 30).
- Exact DP yields closed forms only in special cases. For a linear system with quadratic cost the optimal policy is linear in the state, and it does not depend on the disturbance variance (certainty equivalence) (pp. 31–33).
- Approximation in value space replaces $J^*_{k+1}$ by $\tilde J_{k+1}$ in a one-step minimization (one-step lookahead: stage cost plus the approximate cost-to-go of the next state), so minimization is needed only at the states actually visited. It has three approximations that may be designed largely independently: cost-to-go, expected value, and minimization (pp. 34–35).
- Rollout uses the cost of a base policy (a given policy, however obtained) as $\tilde J$; truncated rollout adds a terminal cost approximation after $m$ simulated steps (pp. 35–36).
- Cost-based and Q-factor-based lookahead (a Q-factor is the expression minimized in the DP equation, for a state-control pair) trade off differently: cost-based allows on-line replanning but needs on-line expectations, Q-factor-based is faster on-line but cannot replan (pp. 37–38).
- Approximation in policy space fits a parametric policy off-line (regression or classification), which often makes on-line use much easier but is less well suited to replanning (pp. 38–42).
- Infinite-horizon problems (stochastic shortest path, discounted, deterministic nonnegative cost) are analysed through Bellman's equation, value iteration and policy iteration (stochastic shortest path means no discounting plus a cost-free termination state). Pure rollout is a single policy iteration step (pp. 43–49).
- Longer lookahead $\ell$ may allow a less accurate $\tilde J$; the lookahead policy's cost $J_{\tilde\mu}$ is announced as one Newton step applied to Bellman's equation (pp. 50, 55).

## L3 — Walkthrough

### 1.3 Stochastic exact and approximate DP (p. 28)
The unit extends DP and approximation in value space to stochastic uncertainty in the system equation and cost, first for finite horizons, then for infinite ones (p. 28).

### 1.3.1 Finite horizon problems
**Problem.** The state evolves by $x_{k+1}=f_k(x_k,u_k,w_k)$, $k=0,\dots,N-1$. The random disturbance $w_k$ has distribution $P_k(\cdot\mid x_k,u_k)$. This may depend on $x_k,u_k$ but not on earlier disturbances $w_{k-1},\dots,w_0$. Stage cost is $g_k(x_k,u_k,w_k)$, and $u_k\in U_k(x_k)$ (pp. 28–29).

A footnote says the system-equation form and the transition-probability form $p(s,a,s')$ are mathematically equivalent. The author prefers $x$-$u$-$w$ because deterministic and continuous-state problems fit it better (p. 28).

**Cost of a policy.** For $\pi=\{\mu_0,\dots,\mu_{N-1}\}$ with $\mu_k(x_k)\in U_k(x_k)$:
$$J_\pi(x_0)=\mathop{E}_{\substack{w_k\\ k=0,\dots,N-1}}\Big\{g_N(x_N)+\sum_{k=0}^{N-1}g_k\big(x_k,\mu_k(x_k),w_k\big)\Big\}.$$
The optimal cost is $J^*(x_0)=\min_{\pi\in\Pi}J_\pi(x_0)$, with $\Pi$ the set of all policies (pp. 29–30).

**Key difference from the deterministic case.** We optimize over policies (closed-loop control laws, feedback policies), not over control sequences. Policies are more general. Under stochastic uncertainty they can give lower cost, because they let $u_k$ use knowledge of $x_k$. Without it the controller cannot adapt to unexpected states. The author calls this a fundamental distinction (p. 29).

**DP algorithm (1.15).** Start with $J^*_N(x_N)=g_N(x_N)$. For $k=0,\dots,N-1$:
$$J_k^*(x_k)=\min_{u_k\in U_k(x_k)}E_{w_k}\Big\{g_k(x_k,u_k,w_k)+J^*_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big\}.\tag{1.15}$$
Let $\mu^*_k(x_k)=u^*_k$ be a minimizer. Then $\pi^*=\{\mu^*_0,\dots,\mu^*_{N-1}\}$ is optimal (p. 30).

Four shared features with the deterministic case (p. 30):
- tail subproblems reduce multistage minimization to single-stage minimizations;
- $J_k^*(x_k)$ is generated backwards, as the optimal cost-to-go from $x_k$ at stage $k$;
- an optimal policy comes from the minimization;
- the structure suits approximation in value space, replacing $J_k^*$ by $\tilde J_k$.

The optimal cost from $x_0$ is $J_0^*(x_0)$. The proof is by induction as in the deterministic case; it is omitted and has "mathematical fine points" (p. 30). The policy can be stored off-line and looked up on-line, or $\mu_k^*(x_k)$ can be computed on-line by the minimization (pp. 30–31).

*Intuition note.* The recursion looks the same as in the deterministic case, except that the "next cost-to-go" is averaged over what the disturbance might do. Policies can use the observed state, so they can give lower cost than a fixed list of controls; this is why the optimization is over rules (p. 29).

**Example 1.3.1 (linear quadratic).** Scalar system $x_{k+1}=ax_k+bu_k+w_k$, with $E\{w_k\}=0$ and $E\{w_k^2\}=\sigma^2$. Cost: $qx_N^2+\sum_{k=0}^{N-1}(qx_k^2+ru_k^2)$ with $q,r>0$. No constraints (they are neglected at first and checked later) (p. 31).

Illustration: a vehicle with velocity $v_k$, $v_{k+1}=v_k+bu_k+w_k$ (1.16), where $u_k$ is a force. With $x_k=v_k-\bar v$ (deviation from the target velocity) we get $x_{k+1}=x_k+bu_k+w_k$. Here $b$ relates to vehicle weight, road conditions and so on (p. 31).

Derivation. $J^*_N(x_N)=qx_N^2$. Applying (1.15) (p. 32):
$$J^*_{N-1}(x_{N-1})=\min_{u_{N-1}}E\{qx_{N-1}^2+ru_{N-1}^2+q(ax_{N-1}+bu_{N-1}+w_{N-1})^2\}.$$
Expanding the square, with $E\{w\}=0$, $E\{w^2\}=\sigma^2$, and taking out terms that do not depend on $u_{N-1}$:
$$J^*_{N-1}(x_{N-1})=qx_{N-1}^2+q\sigma^2+\min_{u_{N-1}}\big[ru_{N-1}^2+q(ax_{N-1}+bu_{N-1})^2\big].\tag{1.17}$$
The bracket is convex quadratic in $u_{N-1}$. Setting its derivative to zero, $0=2ru_{N-1}+2qb(ax_{N-1}+bu_{N-1})$, gives
$$\mu^*_{N-1}(x_{N-1})=-\frac{abq}{r+b^2q}\,x_{N-1}.$$
Substituting gives $J^*_{N-1}(x_{N-1})=K_{N-1}x_{N-1}^2+q\sigma^2$ with $K_{N-1}=\frac{a^2rq}{r+b^2q}+q$.

(added step) Check: with this $u$, $ax+bu=\frac{arx}{r+b^2q}$. Then $ru^2+q(ax+bu)^2=\frac{a^2rq\,x^2\,(b^2q+r)}{(r+b^2q)^2}=\frac{a^2rq}{r+b^2q}x^2$, which gives $K_{N-1}$.

Since $J^*_{N-1}$ is quadratic plus a constant, the same steps continue backwards. By induction, for all $k$:
$$\mu^*_k(x_k)=L_kx_k,\qquad J_k^*(x_k)=K_kx_k^2+\sigma^2\sum_{t=k}^{N-1}K_{t+1},$$
$$L_k=-\frac{abK_{k+1}}{r+b^2K_{k+1}}\tag{1.18}$$
$$K_k=\frac{a^2rK_{k+1}}{r+b^2K_{k+1}}+q,\quad K_N=q.\tag{1.19}$$
(pp. 32–33).

The author attributes the closed form to the linear system and quadratic cost. In general, for linear-quadratic problems (also multidimensional) the optimal policy is linear in the state and the cost is quadratic plus a constant (p. 33).

**Certainty equivalence.** The optimal policy does not depend on the variance of $w_k$ and is unchanged if $w_k$ is replaced by its mean. This holds for several linear-quadratic problem types, and the author says it holds even for nonzero-mean $w_k$. For other problems it can serve as a basis for problem approximation: replace stochastic quantities by typical values (such as expected values) and apply exact DP to the resulting deterministic problem (p. 33). Linear-quadratic problems are exceptional; most DP problems need computational solutions (p. 33).

*Intuition note.* In the linear-quadratic case, noise adds only a constant to the cost, $\sigma^2\sum K_{t+1}$, but never changes the best action. So you can plan as if the noise were zero. This works here because of the linear-quadratic structure, not in general.

**Q-factors (stochastic).** Define the expression minimized in (1.15):
$$Q^*_k(x_k,u_k)=E_{w_k}\Big\{g_k(x_k,u_k,w_k)+J^*_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big\}.\tag{1.20}$$
Then $J_k^*(x_k)=\min_{u_k\in U_k(x_k)}Q^*_k(x_k,u_k)$, and the DP algorithm in Q-form is
$$Q^*_k(x_k,u_k)=E_{w_k}\Big\{g_k(x_k,u_k,w_k)+\min_{u_{k+1}\in U_{k+1}(f_k(x_k,u_k,w_k))}Q^*_{k+1}\big(f_k(x_k,u_k,w_k),u_{k+1}\big)\Big\}.$$
Approximate Q-factors replace $J^*_{k+1}$ by $\tilde J_{k+1}$ (pp. 33–34).

### 1.3.2 Approximation in value space for stochastic DP
Computing $J_k^*$ can be very time-consuming or impossible. Approximation in value space uses $\tilde J_k$ in place of $J_k^*$. At any state $x_k$ encountered at stage $k$:
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}E_{w_k}\Big\{g_k(x_k,u_k,w_k)+\tilde J_{k+1}\big(f_k(x_k,u_k,w_k)\big)\Big\}.\tag{1.21}$$
This minimization is performed only at the $N$ states $x_0,\dots,x_{N-1}$ met on-line, whereas exact DP needs it at every state and stage (p. 34).

**Three approximations** (Fig. 1.3.2; they "may be designed largely independently") (pp. 34–35):
1. *Cost-to-go approximation* $\tilde J_{k+1}$.
2. *Simplified minimization.* Restrict $U_k(x_k)$ to a promising subset. For multiagent controls $u_k=(u_k^1,\dots,u_k^m)$, do $m$ single-component minimizations in sequence, with potentially enormous savings (Section 1.6.7).
3. *Expected value approximation.* Use limited Monte Carlo simulation (e.g. Monte Carlo Tree Search, Ch. 2) or certainty equivalence: replace future $w_{k+1},\dots,w_{k+m}$ by deterministic values $\overline w$, such as expected values. The author calls this one of the most effective techniques for tractability, particularly with multistep lookahead (p. 35).

Problem approximation: obtain $\tilde J_{k+1}$ as the optimal or near-optimal cost of a simpler problem (exploiting decomposable structure, ignoring uncertainties, shrinking the state space). Aggregation is one major approach (Section 3.6). Problem approximation gets little attention in this book (p. 35).

**Rollout and truncated rollout.** In rollout, $\tilde J_{k+1}$ is the cost function of a base policy (perhaps approximate). Any policy can serve as base, including one trained off-line. Rollout has a cost improvement property relative to its base policy; the conditions are deferred to Chapter 2 (pp. 35–36).

Truncated rollout: one-step minimization, then simulation of the base policy for $m$ steps, then an added terminal approximation $\tilde J_{k+m+1}(x_{k+m+1})$. With $m=0$ it reduces to (1.21) (Fig. 1.3.3). The terminal cost approximation is necessary in infinite horizon problems, since an infinite number of base-policy stages cannot be simulated; even for finite horizons, artificially truncating the rollout may be necessary and/or beneficial. Generally, a large combined number of multistep lookahead and rollout steps is "likely to be beneficial" (p. 36).

**Cost versus Q-factor approximations** (pp. 36–38). Q-based policy: $\tilde\mu_k(x_k)\in\arg\min_{u_k}\tilde Q_k(x_k,u_k)$ (1.22). Cost-based policy: the expectation form
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}E_{w_k}\{g_k+\tilde J_{k+1}(f_k)\}\tag{1.23}$$
- *Disadvantage of (1.23):* the expectation must be computed on-line for all $u_k\in U_k(x_k)$.
- *Advantage of (1.23):* if $f_k$, $g_k$ or $U_k(x_k)$ change during operation and the new ones become known at time $k$, on-line replanning is possible and may substantially improve robustness.
- *Q-factor scheme (1.22):* does not allow on-line replanning. Where replanning is not needed, it may avoid on-line expectations and allow much faster on-line computation.
- *Further disadvantage of Q-factors:* the Newton's-method synergy between off-line training and on-line play (Section 1.5) tends to be negatively affected. The cost of the lookahead policy is interpreted there as one Newton step for the Bellman equation, starting from $\{\tilde J_1,\dots,\tilde J_N\}$ (p. 38).

### 1.3.3 Approximation in policy space
Instead of approximating values, select a policy from a parametric class $\tilde\mu_k(x_k,r_k)$, $k=0,\dots,N-1$, and fit $r_k$ by training. The scheme is off-line, possibly with off-line-collected data. On-line improvement of parametric policies (policy gradient) is beyond scope (p. 38). Neural networks are often used, with $r_k$ the weights (p. 38).

**Training by regression.** Take a training set $(x_k^s,u_k^s)$, $s=1,\dots,q$, where $u_k^s$ is a "good" control at $x_k^s$. Solve
$$\min_{r_k}\sum_{s=1}^q\big\|u_k^s-\tilde\mu_k(x_k^s,r_k)\big\|^2\tag{1.24}$$
possibly with a regularization term (a positive multiple of $\|r-\hat r\|^2$). Controls are assumed to be in a Euclidean space. The data may come from a human or software "expert", so $\tilde\mu_k$ is trained to match the expert; this is supervised learning (pp. 38–39).

Training data can also come from value space: $u_k^s\in\arg\min_{u\in U_k(x_k^s)}E\{g_k(x_k^s,u,w_k)+\tilde J_{k+1}(f_k(x_k^s,u,w_k))\}$, or the same with a Q-factor approximation. This is "approximation in policy space built on top of approximation in value space" (pp. 39–40).

*Advantages and limits.* Once $\tilde\mu_k$ is trained, computing $u_k=\tilde\mu_k(x_k,r_k)$ on-line is often much easier than the lookahead minimization (1.23). So a major use is an approximate implementation of a known policy, however obtained. It is less well suited for on-line replanning (p. 40).

**Model-free approximation in policy space.** With $(r_0,\dots,r_{N-1})$ parametrizing $\pi$, the cost $J_\pi(x_0)$ becomes a function of $r$. It can be optimized by gradient-like or random search. In principle no mathematical model is needed; a simulator or the real system suffices. This is "model-free", and the advisability of purely simulation-based implementations is "hotly debated" (p. 40). A footnote says there is always a model in DP/RL formulations: mathematical, computer-based (simulation or trained network), or hybrid (p. 40).

**Value space versus policy space.** The former is primarily an on-line method, with optional off-line training for $\tilde J$. The latter is primarily off-line training, whose result can be used for on-line play or for on-line rollout (p. 41).

### 1.3.4 Training of cost function and policy approximations
Parametric approximation (feature-based architectures, neural networks; Ch. 3). Target function $J(x)$; approximating class $\tilde J(x,r)$; training data $(x^s,J(x^s))$, $s=1,\dots,q$. Choose $\hat r$ so that errors $J(x^s)-\tilde J(x^s,\hat r)$ are small in some sense (Fig. 1.3.5) (pp. 41–42). A footnote: a network approximating costs or Q-factors is a *value network* (also "critic"); one representing a policy is a *policy network* ("actor") (p. 41).

The same ideas apply to approximating a target policy $\mu$ by $\tilde\mu(x,r)$. Data may come from rollout calculations, giving value and policy networks usable in a perpetual rollout scheme (p. 42). Difference: $\tilde J$ values are real numbers; $\tilde\mu$ values lie in $U$. If $U$ consists of $m$-dimensional vectors, both problems are fairly similar continuous approximations (p. 42).

If $U=\{u^1,\dots,u^m\}$ is finite, $\tilde\mu$ is a classifier assigning $x$ to a category. Many classifiers output a probability distribution $\{\tilde\mu^1(x,r),\dots,\tilde\mu^m(x,r)\}$ (1.25), i.e. a randomized policy, because optimization methods such as least squares need continuous variables. It is converted to a nonrandomized policy by
$$\tilde\mu(x,r)\in\arg\max_{i=1,\dots,m}\tilde\mu^i(x,r).\tag{1.26}$$
(Fig. 1.3.6; classification methods in Section 3.4) (p. 42).

### 1.4 Infinite horizon problems — an overview
**Cost (1.27).** With stationary $f$, $g$ and disturbances sharing a distribution $P(\cdot\mid x_k,u_k)$:
$$J_\pi(x_0)=\lim_{N\to\infty}\mathop{E}_{\substack{w_k\\k=0,1,\dots}}\Big\{\sum_{k=0}^{N-1}\alpha^kg\big(x_k,\mu_k(x_k),w_k\big)\Big\},\quad\alpha\in(0,1].$$
For $\alpha<1$ ($\alpha$ is the discount factor), future costs matter less than present ones. A discount factor guarantees that the limit exists and is finite if $g$ is bounded, which makes discounted problems tractable. The infinite-horizon cost is, by definition, the limit of finite-horizon costs (p. 43).

Three problem types (pp. 43–44):
- (a) *Stochastic shortest path (SSP).* $\alpha=1$, with a cost-free absorbing termination state. It may be a goal to reach or a state to avoid. Mostly termination is assumed inevitable under all policies, so the horizon is effectively finite but random. A harder type, discussed selectively, has termination guaranteed only for a subset of policies that includes all optimal ones (this includes deterministic shortest path problems with cycles).
- (b) *Discounted problems.* $\alpha<1$. A finite-state discounted problem can be converted to an SSP problem by adding an artificial termination state reached with probability $1-\alpha$ at every state and stage.
- (c) *Deterministic nonnegative cost problems.* $x_{k+1}=f(x_k,u_k)$ (1.28), $J_\pi(x_0)=\lim_{N\to\infty}\sum_{k=0}^{N-1}\alpha^kg(x_k,\mu_k(x_k))$ (1.29). There is a cost-free absorbing termination state $t$, with
$$g(x,u)\ge0\ \ \text{for all }x\ne t,\ u\in U(x),\tag{1.30}$$
and $g(t,u)=0$.

**Is discounted MDP a universal model?** *Widespread view (not the author's):* any problem can be painlessly converted to a discounted MDP with $\alpha$ close enough to 1. The author calls this questionable, for three reasons (p. 45):
- (a) Deterministic models are common and natural (including discrete optimization), so converting them to MDP makes no sense.
- (b) Discretizing continuous states involves subtleties. The optimal solution's character may be seriously distorted "regardless of how fine the discretization is".
- (c) When reaching the termination state is essential, introducing $\alpha$ may fundamentally alter the problem; the threshold $\alpha$ may be very close to 1 and unknown. *Example:* states 1, 2 and termination $t$. From 1 go to 2 at cost 0; from 2 go to 1 at small cost $\epsilon>0$ or to $t$ at substantial cost $C>0$. The undiscounted optimal policy goes $1\to2\to t$. With discount $\alpha\in(0,1)$, the text states that if $\alpha<1-\epsilon/C$ it is optimal to cycle $1\to2\to1\to2\cdots$ forever, while for $\alpha>1-\epsilon/C$ the shortest path is obtained. So the solution changes discontinuously with $\alpha$ (p. 45).

Finite-state deterministic problems with many states include hard discrete optimization problems. A finite-horizon version can be turned into an infinite-horizon SSP problem with a termination state at the horizon's end (p. 45).

### 1.4.1 Infinite horizon methodology
**Value iteration (VI).** Let $J_N(x)$ be the optimal $N$-stage cost with zero terminal cost, generated by
$$J_{k+1}(x)=\min_{u\in U(x)}E_w\Big\{g(x,u,w)+\alpha J_k\big(f(x,u,w)\big)\Big\},\quad J_0\equiv0.\tag{1.31}$$
A footnote derives it from the finite-horizon DP: with $V_{N-k}(x)$ the cost-to-go with $k$ stages to go, $V_{N-k}(x)=\min_uE_w\{\alpha^{N-k}g+V_{N-k+1}(f)\}$, $V_N=0$. Defining $J_k=V_{N-k}/\alpha^{N-k}$ gives (1.31) (p. 46).

It is "natural to speculate" that (pp. 46–47):
- (a) $J^*(x)=\lim_{N\to\infty}J_N(x)$ for all $x$ (1.32).
- (b) *Bellman's equation* holds, obtained by taking the limit in (1.31) using (1.32); it is a system with one equation per state:
$$J^*(x)=\min_{u\in U(x)}E_w\Big\{g(x,u,w)+\alpha J^*\big(f(x,u,w)\big)\Big\}.\tag{1.33}$$
- (c) If $\mu(x)$ attains the minimum in (1.33) for each $x$, the stationary policy $\{\mu,\mu,\dots\}$ should be optimal.
- (d) $J_\mu(x)=E_w\{g(x,\mu(x),w)+\alpha J_\mu(f(x,\mu(x),w))\}$ (1.34). This is Bellman's equation for a problem whose constraint set has the single control $\mu(x)$. $J_\mu$ is expected to be the limit of VI for $\mu$: $J_\mu(x)=\lim_{N\to\infty}J_{\mu,N}(x)$, with $J_{\mu,k+1}(x)=E_w\{g(x,\mu(x),w)+\alpha J_{\mu,k}(f(x,\mu(x),w))\}$ (1.35), starting from $J_{\mu,0}\equiv0$ or another initial condition.

**When these hold.** All four hold for finite-state discounted problems, and for finite-state SSP problems "under reasonable assumptions". They also hold for infinite-state discounted problems if $g$ is bounded over $(x,u,w)$. In that case $J^*$ is the unique solution of Bellman's equation, and VI converges ($J_k\to J^*$) even from nonzero $J_0$. A $J_0$ closer to $J^*$ generally gives faster convergence (p. 47). A footnote: for undiscounted problems and discounted problems with unbounded cost, the four results are a working hypothesis. Exceptional behavior is possible, such as nonunique solutions of Bellman's equation and VI nonconvergence from some initial conditions (p. 47).

Other algorithms exist for approximation in value space (approximate policy iteration, Q-learning, temporal difference methods, linear programming). The book discusses only approximate forms and variations of policy iteration (p. 47).

**Policy iteration (PI).** The author says he will argue that PI and its variations form the foundation for *self-learning* (learning from self-generated data). Each iteration (Fig. 1.4.2) has two phases (p. 48):
- *Policy evaluation:* compute $J_\mu$ of the current (base) policy, by solving its Bellman equation or by Monte Carlo averaging of trajectory costs.
- *Policy improvement:* $\tilde\mu(x)\in\arg\min_{u\in U(x)}E_w\{g(x,u,w)+\alpha J_\mu(f(x,u,w))\}$.

One can generally prove $J_{\tilde\mu}(x)\le J_\mu(x)$ for all $x$ (shown in Section 2.7). This can be used to show that PI produces an optimal policy in finitely many iterations under favorable conditions (e.g. finite-state discounted) (p. 48).

Pure rollout is a single PI iteration: one-step lookahead with $J_\mu$ as terminal cost approximation. It can be applied on-line by simulation, unlike approximate PI with neural network training, which can be done only off-line (p. 49).

*Intuition note.* Value iteration repeats the "one more stage" DP step; under suitable conditions the costs converge to $J^*$ (p. 47). Policy iteration alternates between "score the current rule" and "improve the rule by looking one step ahead at that score". The first step is policy evaluation of a fixed rule; the second is one-step lookahead using that score, which is what pure rollout does once.

### 1.4.2 Approximation in value space — infinite horizon
**One-step lookahead (1.36).**
$$\tilde\mu(x)\in\arg\min_{u\in U(x)}E\Big\{g(x,u,w)+\alpha\tilde J\big(f(x,u,w)\big)\Big\}.$$
This gives a stationary policy $\{\tilde\mu,\tilde\mu,\dots\}$ with cost $J_{\tilde\mu}$. If $\tilde J=J^*$, the policy attains the minimum in (1.33) and is expected to be optimal, which suggests using $\tilde J$ close to $J^*$ (p. 49).

**Stability.** For classical control problems (steering the state near a reference, with a cost-free absorbing terminal state and positive cost elsewhere), stability of $\tilde\mu$ may be a principal objective. $\tilde\mu$ is called stable if $J_{\tilde\mu}(x)<\infty$ for all $x$. Choosing $\tilde J$ for stability matters in model predictive and adaptive control, and is discussed later for linear quadratic problems (p. 49).

**$\ell$-step lookahead (Fig. 1.4.3).** At $x_k$, minimize the cost of the first $\ell>1$ stages, with future costs approximated by $\tilde J$:
$$\min_{u_k,\mu_{k+1},\dots,\mu_{k+\ell-1}}E\Big\{g(x_k,u_k,w_k)+\sum_{i=k+1}^{k+\ell-1}\alpha^{i-k}g\big(x_i,\mu_i(x_i),w_i\big)+\alpha^\ell\tilde J(x_{k+\ell})\Big\}.$$
This yields $\tilde u_k$ and $\tilde\mu_{k+1},\dots,\tilde\mu_{k+\ell-1}$. Only $\tilde u_k$ is applied; the rest is discarded. It equals one-step lookahead with a lookahead function equal to the optimal cost of an $(\ell-1)$-stage problem with terminal cost $\tilde J(x_{k+\ell})$ (p. 50).

Motivation: "by increasing the value of $\ell$, we may require a less accurate approximation $\tilde J$ to obtain good performance". This is to be explained via Newton's method (Section 1.5). Long multistep lookahead is critical for AlphaZero chess. It may also enhance stability of the on-line policy, but costs more computation (pp. 50–51).

**Three approximations (Fig. 1.4.4)** (p. 51):
- (a) one terminal cost approximation $\tilde J$, rather than the $N$ functions $\tilde J_1,\dots,\tilde J_N$ of the finite case;
- (b) expected value approximation, e.g. certainty equivalence, replacing some $w_k,\dots,w_{k+\ell-1}$ by deterministic values;
- (c) simplified minimization, e.g. one agent at a time in multiagent problems with $u=(u^1,\dots,u^m)$ (Section 1.6.7, Section 2.9).

**Constructing $\tilde J$ for on-line play** (pp. 52–53). $\tilde J$ may come from off-line training, or on-line from truncated rollout. Four broad types:
- (a) *Off-line problem approximation:* $\tilde J$ is the cost of a simplified problem (decomposition, smaller state space, neglected constraints, ignored uncertainty, e.g. a related deterministic problem by certainty equivalence). *Aggregation* groups states into aggregate states, solves the aggregate problem by exact DP, and interpolates to get $\tilde J$.
- (b) *On-line simulation:* in rollout for stochastic problems, Monte Carlo and a base policy $\mu$ give $\tilde J(x)\approx J_\mu(x)$ when needed. Simulation suits parallel computation and can be simplified by certainty equivalence.
- (c) *On-line approximate optimization:* solve a shorter-horizon problem with a simple terminal cost. This is multistep lookahead or rollout, and is often used in model predictive control (MPC).
- (d) *Parametric cost approximation* $\tilde J(x,r)$ from a class using features of $x$, e.g. through approximate PI (policy evaluation by a neural network, or by stochastic iterative algorithms TD($\lambda$), LSPE($\lambda$), LSTD($\lambda$), which are peripheral to the course). Approximate PI also yields a suboptimal policy, which can be improved by rollout. Q-learning, linear programming and aggregation can also produce $\tilde J(x,r)$.

For special structure, the lookahead minimization may be closed-form: e.g. a nonlinear system with control entering linearly in the system equation and quadratically in the cost, with quadratic $\tilde J$. Then the minimized function is quadratic in $u$ (p. 53).

**From off-line training to on-line play** (pp. 54–55). Off-line training yields a cost approximation (TD-Gammon), a policy (policy gradient), or both (AlphaZero). Three main ways to combine them on-line:
- (a) Given a policy $\mu$, use $\tilde J=J_\mu$ as terminal cost. For one-step lookahead, compute on-line (maybe by simulation) the values $E\{J_\mu(f(x_k,u_k,w_k))\}$ needed. For $\ell$-step lookahead, compute $E\{J_\mu(x_{k+\ell})\}$ for all states reachable in $\ell$ steps. This is the simplest rollout.
- (b) Given an off-line $\tilde J$, compute on-line the lookahead policy $\tilde\mu$ quickly. $\tilde\mu$ can then be used for rollout as in (a). In a truncated variant, $\tilde J$ approximates the tail of the rollout (as in rollout-based TD-Gammon).
- (c) Given both $\mu$ and $\tilde J$, use truncated rollout with $\mu$ and $\tilde J$ for the tail; here $\mu$ is computed off-line.

In MPC, a target tube may additionally be computed off-line so that state constraints can be satisfied on-line (Section 1.6.9).

**Q-factor form (1.37).** With $\tilde Q(x,u)\approx E\{g(x,u,w)+\alpha J^*(f(x,u,w))\}$:
$$\tilde\mu(x)\in\arg\min_{u\in U(x)}E\Big\{g(x,u,w)+\alpha\min_{u'\in U(f(x,u,w))}\tilde Q\big(f(x,u,w),u'\big)\Big\}.$$
The inner minimum plays the role of $\tilde J(f(x,u,w))$. Q-factors are common in the "model-free" case, where a simulator generates samples of $w$, $g$ and $f$; the minimization (1.37) must then be done on-line with the simulator (p. 55).

### 1.4.3 Understanding approximation in value space (start; unit ends mid-section)
Aims: make $\tilde J$ close to $J^*$, and understand the relation between $\tilde J$ and $J_{\tilde\mu}$. Question (a): how does off-line training quality affect the lookahead policy? The key fact the author announces: $J_{\tilde\mu}$ is the result of one step of Newton's method applied to Bellman's equation (1.33), starting at $\tilde J$. With multistep lookahead, it is one Newton step starting at the function obtained by applying multiple value iterations to $\tilde J$. The details are in Section 1.5 (p. 55).

## Toy example (ours, not from the text)
Use Example 1.3.1 with $a=b=q=r=1$, $N=2$, and noise variance $\sigma^2$.

*Exact DP via (1.19), (1.18).* $K_2=q=1$.
- $K_1=\frac{1\cdot1\cdot1}{1+1\cdot1}+1=0.5+1=1.5$, $L_1=-\frac{1\cdot1\cdot1}{1+1}=-0.5$.
- $K_0=\frac{1\cdot1.5}{1+1.5}+1=0.6+1=1.6$, $L_0=-\frac{1.5}{1+1.5}=-0.6$.
- $J^*_0(x_0)=1.6x_0^2+\sigma^2(K_1+K_2)=1.6x_0^2+2.5\sigma^2$, and $J_1^*(x)=1.5x^2+\sigma^2$.

*One-step lookahead with a crude $\tilde J_1(x)=x^2$ (i.e. $\tilde K=1$ instead of 1.5).* At stage 0 minimize $E\{x^2+u^2+(x+u+w)^2\}=x^2+u^2+(x+u)^2+\sigma^2$. The derivative $2u+2(x+u)=0$ gives $\tilde\mu_0(x)=-0.5x$, versus the optimal $-0.6x$. The variance $\sigma^2$ does not enter the minimizer (certainty equivalence).

*Cost of the lookahead choice from $x_0=1$, using the optimal policy at stage 1.*
- $u=-0.5$: stage cost $1+0.25=1.25$; $x_1=0.5+w$; $E\{J_1^*(x_1)\}=1.5(0.25+\sigma^2)+\sigma^2=0.375+2.5\sigma^2$. Total $1.625+2.5\sigma^2$.
- $u=-0.6$ (check): stage cost $1+0.36=1.36$; $x_1=0.4+w$; $E\{J_1^*\}=1.5(0.16+\sigma^2)+\sigma^2=0.24+2.5\sigma^2$. Total $1.6+2.5\sigma^2$, matching $J_0^*(1)$.

So the cruder $\tilde J$ gives a slightly worse policy (extra cost 0.025). The error in $\tilde J$ (1 vs 1.5) turns into a smaller error in cost, because the cost is flat near the minimizer.

## Concepts
- [[principle-of-optimality]] — the stochastic DP recursion (1.15) uses tail subproblems to reduce multistage minimization to single-stage minimizations (p. 30; the principle itself is only named on p. 28)
- [[policy]] — here a sequence of functions $\mu_k$ (feedback law) mapping state to a constrained control; stationary if the same $\mu$ is used each stage (pp. 29, 46)
- [[bellman-equation-value-function]] — $J^*$ solves (1.33); $J_k^*$ is the cost-to-go; $J_\mu$ solves (1.34) (pp. 30, 46–47)
- [[markov-decision-process]] — finite-state stochastic problem; the author uses the system-equation form, equivalent to transition probabilities (p. 28)
- [[model-based-vs-model-free-rl]] — author's "model-free" means a simulator or real system replaces the equations; a model always exists (p. 40)
- [[model-predictive-control]] — mentioned as on-line multistep optimization with a prediction interval; stability and target tubes noted (pp. 50, 53–55)
- [[lqr]] — scalar finite-horizon linear-quadratic problem with linear optimal policy and quadratic cost-to-go (pp. 31–33)
- [[approximation-in-value-space]] (new) — replace $J^*$ by $\tilde J$ in a lookahead minimization, giving a suboptimal policy (pp. 34, 49)
- [[approximation-in-policy-space]] (new) — choose a policy from a parametric class $\tilde\mu(x,r)$ by off-line training (p. 38)
- [[q-factor]] (new) — expression minimized in the DP equation; $J=\min_uQ$ (p. 33)
- [[certainty-equivalence]] (new) — two meanings: the LQ property that the policy ignores noise variance (p. 33); an approximation that replaces random quantities by typical values (p. 35)
- [[rollout]] (new) — one-step lookahead whose terminal cost is the cost of a base policy; truncated rollout adds a terminal approximation after $m$ steps (pp. 35–36, 49)
- [[value-iteration]] (new) — algorithm (1.31), starting from $J_0\equiv0$ or another $J_0$ (p. 46)
- [[policy-iteration]] (new) — alternate policy evaluation and policy improvement; viewed as repeated rollout (p. 48)
- [[stochastic-shortest-path]] (new) — undiscounted problem with a cost-free absorbing termination state (p. 43)
- [[discount-factor]] (new) — $\alpha<1$ weights future costs less and makes the infinite sum finite for bounded $g$ (p. 43)
- [[multistep-lookahead]] (new) — $\ell$-step minimization, apply only the first control; may allow a less accurate $\tilde J$ (p. 50)
- [[stability-of-lookahead-policy]] (new) — policy $\tilde\mu$ is stable if $J_{\tilde\mu}(x)<\infty$ for all $x$ (p. 49)

## Canonical instances
- [[lq-cruise-control]] — vehicle velocity deviation $x_{k+1}=x_k+bu_k+w_k$; closed-form $L_k,K_k$ (pp. 31–33)
- [[two-state-discount-threshold]] — shortest path with states 1, 2, $t$; discounting changes the solution discontinuously at a threshold $\alpha$ (p. 45)
- [[alphazero-td-gammon]] — mentioned as examples of off-line training yielding a cost approximation (TD-Gammon) or both cost and policy (AlphaZero); long multistep lookahead critical for AlphaZero chess (pp. 50, 54)

## Bridges (candidates)
- [structural-analogy] Certainty equivalence in the LQ example ↔ control-theory: separation of estimation and control under Gaussian noise — in both, noise does not change the control law (not stated in this unit).
- [structural-analogy] $\ell$-step lookahead applying only the first control ↔ model predictive control: receding-horizon re-optimization at every step (the text links them, pp. 50, 53).
- [structural-analogy] One lookahead step as a Newton step on Bellman's equation ↔ numerical analysis: Newton's method for fixed-point equations (announced p. 55; details not in this unit).
- [metaphor] Training $\tilde\mu(x,r)$ to imitate an expert ↔ supervised learning/imitation: regression onto good actions (p. 39).
- [same-math] Value iteration (1.31) ↔ finite-horizon backward DP recursion with time reversed (footnote, p. 46).

## Questions this raises
- Why is $J_{\tilde\mu}$ a Newton step from $\tilde J$, and what does that imply about how much accuracy in $\tilde J$ we need?
- Under what conditions does rollout (policy improvement) guarantee $J_{\tilde\mu}\le J_\mu$, and what happens to this with truncation?
- How does one pick $\tilde J$ so that the lookahead policy is stable, e.g. in linear quadratic problems?
- When is the loss of on-line replanning in Q-factor and policy-space schemes acceptable?

## Reading notes
- This part starts at §1.3 (p. 28, first line "1.3 Stochastic Exact and Approximate Dynamic Programming") and ends on p. 55, in the middle of §1.4.3 after item (a) of the list of questions. The rest of §1.4.3 is in the next part. Split at an even boundary.
- Page offset: printed = pdf − 20 (pdf 48 = p. 28).
- The text layer is garbled in places (e.g. "→" for "−" and "↓" for "∈", missing braces in displays). I checked the equations against the page images.
- Footnote on p. 28 cites Sections 1.7.1 and 1.7.2. From p. 45 on, the odd-page running header changes (p. 43 still shows "Sec. 1.3") to "Sec. 1.4".
- p. 45, example (c): the text says that for $\alpha>1-\epsilon/C$ "the shortest path $2\to1\to t$" is obtained. This conflicts with the stated transitions (from state 1 only to state 2, then 2 to $t$), so $1\to2\to t$ is presumably meant. I report it as printed. My own quick check, with costs discounted as $\alpha^k$ per (1.27), compares cycling cost $\epsilon/(1-\alpha^2)$ to $C$, which gives a threshold $\alpha^2=1-\epsilon/C$ rather than $1-\epsilon/C$. I did not resolve this; the qualitative point (a threshold near 1, with a discontinuous change) is unaffected.
- The proof of the stochastic DP algorithm and the cost improvement property of rollout are not given in this unit.
