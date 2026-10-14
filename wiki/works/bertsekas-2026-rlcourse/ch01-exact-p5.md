---
id: bertsekas-2026-rlcourse/ch01-exact-p5
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 5/6): end of Sec. 1.6.8, Sec. 1.6.9, Sec. 1.7 (to start of 1.7.6)"
pages: 109-139
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Adaptive control, model predictive control, and RL versus decision/control

## L0 — One line
When parameters change or constraints bind, re-solve a short lookahead problem on-line (rollout, MPC); this is a Newton step on Bellman's equation, and it can be shown to be stable when the base policy is stable or the terminal cost is suitably chosen.

## L1 — The gist (≤ 120 words)
This part asks how to control a system whose parameters are unknown or changing, and how to handle continuous states with constraints. Bertsekas answers with on-line replanning. Rollout with a fixed base policy copes with changing parameters. Model predictive control (MPC) repeats a short-horizon optimization; he reads it as rollout and as a Newton step on Bellman's equation. A terminal cost satisfying a Lyapunov condition addresses stability, and invariant sets address feasibility under state constraints. The unit then compares RL and optimal-control terminology and notation. It also discusses how DP relates to RL, large language models, machine learning and optimization.

**Prerequisites:** dynamic programming (cost-to-go, Bellman operator $T$, value iteration), rollout and base policy, the Newton-step view of approximation in value space (Sec. 1.5), linear-quadratic problems, basic probability (conditional probability).

## L2 — Key ideas
- Sequential estimate-then-control can fail: under feedback $\gamma x_k$ only $a+b\gamma$ is identifiable, not $a$ and $b$ separately (pp. 110–111).
- With changed parameters, rollout using the old policy as base policy needs no retraining. In a linear-quadratic test its cost lies between optimal and base-policy cost, much closer to optimal (pp. 112–116).
- Adaptive control can be recast as a POMDP (a decision problem where part of the state is not observed): the unknown parameter $\theta$ is a hidden constant state, and the belief state is $(x_k,b_k)$ (pp. 115–117).
- Classical MPC is rollout: one-step lookahead on $u_k$, with the $(\ell-1)$-stage "drive to 0" problem as base heuristic. The author concludes it is stable, because rollout with a stable base policy can be shown to be stable under very general conditions (pp. 120–122).
- With a terminal cost $G$ (a cost placed on the last lookahead state) and nonnegative stage costs, MPC can be proved stable if $TG\le G$ (the Lyapunov condition). The author expects longer lookahead to improve stability, and longer truncated rollout enlarges the stability region (pp. 122–125).
- State constraints require an invariant set (a set the state can be kept inside for all future times, so that the lookahead problem stays feasible). The largest one is the limit of a value-iteration-like recursion, computed off-line (pp. 126–128).
- Extensions: certainty equivalence for stochastic problems, data-driven models, estimators for imperfect state information, and disturbance estimation via state augmentation (pp. 128–131).
- Sec. 1.7 gives a glossary of AI/RL versus optimal-control terms and notation, and compares DP, RL, machine learning and optimization (pp. 131–139).

## L3 — Walkthrough

### 1.6.8 (end): Adaptive control (pp. 109–118)
**PID control.** The author mentions PID control for continuous-state problems without a known model. It aims to keep the output of a single-input single-output system at a set point, or on a trajectory, while parameters change within a fairly broad range. In simplest form it has three scalar parameters, set by various methods, some manual or heuristic. Its range of application is mainly single-input single-output, continuous-state systems (p. 109).

**System identification.** A different approach splits control into two phases (p. 109):
- phase 1 estimates the unknown parameters, and the control ignores the interim estimates;
- phase 2 uses the final estimates to apply an optimal or suboptimal policy.

The phases may be repeated, or run simultaneously (Fig. 1.6.11, p. 110). Two drawbacks: it is hard to decide when to switch phases, and the control may make some parameters invisible to the estimator. This second problem is *parameter identifiability* (p. 109).

**Example 1.6.6 (identifiability).**
- System $x_{k+1}=ax_k+bu_k$, cost $\sum_{k=1}^N (x_k)^2$ (p. 110).
- With $a,b$ known and perfect state information, the optimal law is $\mu^*_k(x_k)=-\tfrac{a}{b}x_k$, which sets all future states to 0 (p. 110).
- In phase 1 the law $\tilde\mu_k(x_k)=\gamma x_k$ is used \tag{1.79}. Here $\gamma$ is some scalar, e.g. $-\bar a/\bar b$ from a priori estimates. In phase 2 the law is $-(\hat a/\hat b)x_k$ with the estimated $\hat a,\hat b$ (p. 110).
- Under (1.79) the closed loop is $x_{k+1}=(a+b\gamma)x_k$. Estimation can at best give $a+b\gamma$, so it cannot tell apart pairs with $a_1+b_1\gamma=a_2+b_2\gamma$. Hence $a,b$ are not identifiable under feedback of the form (1.79) (pp. 110–111).

*Intuition note.* If the controller makes the system behave in one fixed way, the data only show that one behaviour. Many $(a,b)$ pairs produce the same data, so more data cannot separate them.

The author says on-line estimation algorithms that address identifiability are complex and beyond scope. A further difficulty is that recomputing an optimal policy on-line may be hard, e.g. with neural-network training or integer constraints. One simpler option is rollout (p. 111). A footnote gives another: precompute a controller for each of a known finite set of parameter values and switch among them (multiple model control, gain scheduling) (p. 111).

**Adaptive control by rollout and on-line replanning.**
- Assume the controller learns of parameter changes "instantly". How it learns is immaterial for the discussion (p. 111).
- The current policy is the base policy for rollout, and controls at the current state are compared by one-step or multistep minimization (Fig. 1.6.12, p. 113).
- Advantage: it is simple and reliable, and needs no training to revise the policy. No new policy is explicitly computed (p. 112).
- The base policy may also change over time. This is necessary in particular when constraints change (p. 112).
- Main requirement: the rollout computation must be fast enough to run between stages. Truncated rollout and parallel computation can help (p. 112).
- The approach makes sense when rollout controls are faster or more convenient to compute than optimal controls, e.g. for nonlinear systems or integer constraints (p. 112).

**Example 1.6.7 (replanning for linear quadratic problems).** The example shows analytically how rollout from a nominal-optimal policy behaves when parameters change. It is not practically useful here, because the new optimal policy is available in closed form. It is indicative of rollout's robustness elsewhere (p. 112).
- System $x_{k+1}=x_k+bu_k$, cost $\lim_{N\to\infty}\sum_{k=0}^{N-1}(x_k^2+ru_k^2)$ (pp. 112–113).
- Optimal cost $J^*(x)=K^*x^2$, with $K^*$ the unique positive solution of the Riccati equation
$$K=\frac{rK}{r+b^2K}+1 \tag{1.80}$$
- Optimal policy $\mu^*(x)=L^*x$ \tag{1.81}, with $L^*=-\dfrac{bK^*}{r+b^2K^*}$ \tag{1.82} (pp. 113–114).
- Nominal parameters $b=2$, $r=0.5$: $K=\frac{2+\sqrt6}{4}$ and
$$L=-\frac{2+\sqrt6}{5+2\sqrt6} \tag{1.83}$$
- Now $b$ and $r$ vary while $L$ stays fixed. Three cost coefficients are compared (p. 114):
  - (a) optimal: $K^*x^2$;
  - (b) base policy $\mu_L(x)=Lx$: $K_L=\dfrac{1+rL^2}{1-(1+bL)^2}$;
  - (c) rollout policy $\tilde\mu_L(x)=\tilde Lx$ with base $\mu_L$: $\tilde L=-\dfrac{bK_L}{r+b^2K_L}$, $\tilde K_L=\dfrac{1+r\tilde L^2}{1-(1+b\tilde L)^2}$.
- Fig. 1.6.13 shows $K^*\le\tilde K_L\le K_L$ over a range of $r$ and $b$ (p. 115).
  - $K_L-K^*$ indicates the robustness of $\mu_L$, i.e. the loss from ignoring the new $b,r$.
  - $\tilde K_L-K^*$ indicates the loss from replanning by rollout instead of optimally.
  - $K_L-\tilde K_L$ indicates the gain from rollout replanning over keeping $\mu_L$ (p. 115).
- The figure shows rollout very close to exactly reoptimized, base policy much worse. The author attributes this to the quadratic convergence of Newton's method underlying rollout: $\lim_{J\to J^*}(\tilde J-J^*)/(J-J^*)=0$, where $\tilde J$, $J^*$, $J$ are the rollout, optimal and base-policy performance (pp. 115–116).

*Intuition note.* The old policy is a rough guess at the new problem's cost. One lookahead step on that guess lands much nearer the optimum than the guess itself, and the gain is proportionally larger the better the guess is.

**Adaptive control as POMDP (pp. 115–118).** The two-phase scheme strictly separates estimation and control. The alternative does both simultaneously, and part of the control effort may go to improving future estimation. The author calls this more principled (p. 115).
- State has two parts: a perfectly observed $x_k$, and an unobserved constant $\theta$, a parameter in the system equation (p. 115):
$$x_{k+1}=f_k(x_k,\theta,u_k,w_k) \tag{1.84}$$
- $u_k\in U_k(x_k)$, and $w_k$ is a random disturbance whose distribution depends on $(x_k,\theta,u_k)$. For convenience $\theta$ takes one of $m$ known values $\theta^1,\dots,\theta^m$, with a given prior (p. 117).
- Information vector $I_k=\{x_0,\dots,x_k,u_0,\dots,u_{k-1}\}$. Conditional probabilities $b_{k,i}=P\{\theta=\theta^i\mid I_k\}$ form $b_k=(b_{k,1},\dots,b_{k,m})$. The pair $(x_k,b_k)$ is the *belief state* (Fig. 1.6.14) (p. 117).
- An exact DP algorithm exists for this POMDP (Sec. 1.6.6) and suits approximation in value space and rollout. Sections 2.11 and 2.10 treat this later (p. 117).
- For a deterministic system $x_{k+1}=f_k(x_k,\theta,u_k)$ one can typically expect the true $\theta^*$ to be identified in a finite number of stages, because each $x_k$ is a noiseless observation relating to $\theta$. After that the problem has perfect state information (p. 118).

### 1.6.9 Model predictive control (pp. 118–131)
**Setting.** MPC is summarized for the regulation problem, keeping the state of a deterministic system near the origin (Fig. 1.6.15: the cart-pole). Following a trajectory is also possible but not covered (p. 118). The linear-quadratic formulation is often unsatisfactory for two reasons (p. 118):
- (a) the system may be nonlinear, so linearizing is inappropriate, or some controls may be discrete;
- (b) there may be state and control constraints. Quadratic penalties treat them "softly" and may produce trajectories that violate them (Fig. 1.6.16, car with obstacles, p. 120).

MPC combines multistep lookahead, rollout with a base policy and certainty equivalence. It is well suited to on-line replanning (pp. 118–119). It was developed independently of approximate DP/RL. The continuous (infinite) state and control spaces are a major difference from finite-state RL problems, but the author calls this inconsequential at a fundamental level. The reason is that the framework based on Newton's method holds for both (p. 119).

**Problem.** Undiscounted infinite-horizon deterministic: $x_{k+1}=f(x_k,u_k)$, finite-dimensional vectors, cost per stage $g(x_k,u_k)\ge0$, control constraints $u_k\in U(x_k)$, no state constraints at first. The origin can be held at zero cost: $f(0,\bar u_k)=0$, $g(0,\bar u_k)=0$ for some $\bar u_k\in U(0)$ (pp. 119–120).

**Classical form, viewed as rollout** (as in Keerthi–Gilbert; Fig. 1.6.17). At each state $x_k$ (pp. 121–122):
- (a) Solve the $\ell$-stage problem
$$\min_{u_t,\ t=k,\dots,k+\ell-1}\ \sum_{t=k}^{k+\ell-1} g(x_t,u_t) \tag{1.85}$$
subject to
$$x_{t+1}=f(x_t,u_t),\quad t=k,\dots,k+\ell-1 \tag{1.86}$$
$$u_t\in U(x_t),\quad t=k,\dots,k+\ell-1 \tag{1.87}$$
$$x_{k+\ell}=0 \tag{1.88}$$
with $\ell>1$ chosen in a largely empirical way (p. 121).
- (b) Apply the first control $\tilde u_k$ of the optimal sequence and discard the others.
- (c) Repeat at the next state $x_{k+1}$ (p. 122).

*Rollout view* (first discussed in the author's papers [Ber05a], [Ber05b]; p. 122):
- The lookahead function $\tilde J$ implicitly used by MPC is the cost function of a certain stable base policy.
- That policy drives the state to 0 after $\ell-1$ stages (not $\ell$) and keeps it at 0, observing constraints and minimizing the $(\ell-1)$-stage cost.
- The minimization over $u_k$ is the one-step lookahead. The minimization over $u_{k+1},\dots,u_{k+\ell-1}$ is the base heuristic (Fig. 1.6.17 caption, p. 121).
- Consequence: the MPC policy is stable, since rollout with a stable base policy can be shown to yield a stable policy under very general conditions (noted for linear-quadratic problems in Sec. 1.5) (p. 122).

**Terminal cost approximation and stability.** In a common variant the requirement $x_{k+\ell}=0$ is replaced by a terminal cost $G(x_{k+\ell})$, positive everywhere except at 0 (p. 122):
$$\min_{u_t,\ t=k,\dots,k+\ell-1}\left[G(x_{k+\ell})+\sum_{t=k}^{k+\ell-1} g(x_t,u_t)\right] \tag{1.89}$$
This can be seen as rollout with one-step lookahead. At $x_{k+1}$ the base policy applies the first control of the sequence minimizing $G(x_{k+\ell})+\sum_{t=k+1}^{k+\ell-1}g(x_t,u_t)$. It can also be seen as approximation in value space with $\ell$-step lookahead and terminal cost approximation $G$, which is a Newton step (Figs. 1.5.7, 1.5.8) (p. 122).

Bellman operator: $(TJ)(x)=\min_{u\in U(x)}\{g(x,u)+J(f(x,u))\}$. Under the nonnegative-cost assumption, the MPC controller can be proved stable if one value iteration from $G$ gives uniformly smaller values than $G$:
$$\min_{u\in U(x)}\{g(x,u)+G(f(x,u))\}\le G(x)\quad\text{for all }x \tag{1.90}$$
i.e. $(TG)(x)\le G(x)$. This is the *Lyapunov condition* in MPC. Fig. 1.6.18 shows that it puts the value iterates, implemented through multistep lookahead, inside the stability region (pp. 123).

*Intuition note.* If one more step of optimal lookahead from $G$ never raises the cost estimate, then, as Fig. 1.6.18 illustrates, the value iterates stay inside the stability region, so the MPC policy is stable.

Further statements (pp. 123–125):
- The author expects stability to improve with the lookahead length $\ell$. Given $G\ge0$, the MPC controller is *likely* stable for $\ell$ sufficiently large, since value iteration ordinarily converges to $J^*$, which lies inside the stability region. Results of this type are known under various conditions (p. 124).
- Another variant adds *truncated rollout* with a stable base policy $\mu$ for $m$ steps. Fig. 1.6.19: $T_\mu^mG$ is the truncated rollout result. Then $\ell-1$ value iterations give $T^{\ell-1}(T_\mu^mG)$, and the Newton step yields the MPC policy cost, defined by $T_{\tilde\mu}T^{\ell-1}(T_\mu^mG)=T^\ell(T_\mu^mG)$. Here $(T_\mu J)(x)=g(x,\mu(x))+J(f(x,\mu(x)))$ (p. 125).
- Increasing $m$ enlarges the stability region, because it moves the Newton step's starting point toward $J_\mu$, which lies inside the stability region. The lookahead minimization may become complicated when the control space is infinite (p. 124).
- With changing parameters, new estimates go straight into the $\ell$-stage problem. The author calls this an important and often decisive advantage over approximation in policy space (p. 124).

**State constraints and invariant sets.**
- With constraints $x_k\in X$ for all $k$, and $x_k\in X$ at the current stage, the problem becomes (1.91): the cost of (1.89) minimized subject to the control constraints (1.92) $u_t\in U(x_t)$, $t=k,\dots,k+\ell-1$ and the state constraints (1.93) $x_t\in X$, $t=k+1,\dots,k+\ell$ (pp. 124–125).
- The trajectory then stays in $X$ if the initial state does. But there is no guarantee that (1.91)–(1.93) is feasible for every $x_k\in X$ (p. 126).

**Example 1.6.8.** Scalar system $x_{k+1}=2x_k+u_k$, $|u_k|\le1$, $X=\{x_k\mid|x_k|\le\beta\}$ \tag{1.94} (p. 126).
- If $\beta>1$, the constraint cannot hold for all initial $x_0\in X$. Take $x_0=\beta$: then $2x_0>2$, and $x_1=2x_0+u_0>x_0=\beta$ for any feasible $u_0$.
- Then $x_{k+1}>x_k$ for all $k$ and $x_k\to\infty$.
- The constraint can be met only from $\hat X=\{x\mid|x|\le1\}$. Fig. 1.6.20 shows MPC trajectories from $|x_0|>1$ (unstable) and from $|x_0|<1$ (stable) (pp. 126–127).

*Invariance.* $X$ must be *invariant*: for every $x\in X$ there is $u\in U(x)$ with $f(x,u)\in X$. The set (1.94) is invariant if and only if $\beta\le1$ (p. 126). If $X$ is not invariant, replace it by an invariant subset $\hat X\subset X$. Then the MPC problem is feasible if $x_0\in\hat X$ (p. 127).

*Computing the largest invariant subset.* This is an off-line calculation. Start with $X_0=X$ and set
$$X_{k+1}=\{x\in X_k\mid f(x,u)\text{ belongs to }X_k\text{ for some }u\in U(x)\},\quad k\ge0 \tag{1.95}$$
Then $X_{k+1}\subset X_k$, and under mild conditions $\hat X=\cap_{k=0}^\infty X_k$ is the largest invariant subset of $X$ (author's thesis [Ber71] and paper [Ber72a]; there called reachability of a target tube) (p. 127).

For Example 1.6.8 with $X_0=\{|x|\le\beta\}$, $\beta>1$: $X_k=\{|x|\le\beta_k\}$ with $\beta_0=\beta$, $\beta_{k+1}=\frac{\beta_k+1}{2}$. (Added step: $|2x+u|\le\beta_k$ is feasible for some $|u|\le1$ iff $2|x|-1\le\beta_k$.) Then $\beta_{k+1}<\beta_k$ and $\beta_k\downarrow1$, so $\hat X=\{|x|\le1\}$ (pp. 127–128).

**Suboptimal invariant subsets** (p. 128). The largest invariant subset is often computationally intractable. Alternatives:
- an invariant subset for a nominal policy $\hat\mu$ (i.e. $f(x,\hat\mu(x))\in\hat X$ for $x\in\hat X$), found by simulation; $\hat\mu$ can also serve for truncated rollout and terminal cost;
- for a linear system with ellipsoid-bounded disturbances, an ellipsoidal invariant subset (algorithm in [Ber71]).

This computation is off-line, part of training along with $G$. For partially unknown models, robust tube-based MPC has been suggested. Another route replaces state constraints by penalty or barrier functions (control barrier / control Lyapunov functions) (p. 128).

**Stochastic MPC by certainty equivalence.** At $x_k$, replace $w_{k+1},w_{k+2},\dots$ by deterministic values $\bar w_{k+1},\bar w_{k+2},\dots$ while keeping the stochastic character of $w_k$ at the current stage only. Only the first step is stochastic, so per-stage work is not much harder than the deterministic case, and a Newton step for the Bellman equation is still implemented (pp. 128–129).

**Data-driven MPC.** The aim is to avoid the need for a mathematical model (p. 129).
- The system is represented implicitly by observed trajectories, i.e. triplets $(x_k,u_k,x_{k+1})$ (an approach pioneered by Willems).
- A parametric model (e.g. a neural network, possibly a transformer, or another identification method) or a nonparametric model (e.g. Bayesian process regression) is fitted off-line. It is then used on-line to predict and optimize over a finite horizon, applying the first control.
- Challenges: the choice of state, a learned model that may be inaccurate outside the training set, and, in adaptive settings, on-line model updating from data (p. 129).

**Imperfect state information.** MPC as described requires full state feedback (p. 129). If the state is unavailable, one may estimate it with a Kalman filter or observer. This is possible when the state is continuous and the model is known. Some non-continuous problems allow some inference method for a state estimate. Otherwise one needs belief states and POMDP-like methods, which are much more demanding computationally (pp. 129–130). The alternative is approximation in policy space, whose drawbacks the author lists (p. 130):
- (a) training can be complicated and unreliable (local minima);
- (b) on-line retraining may be very sample-inefficient or practically impossible;
- (c) a policy depending on only part of the information limits performance;
- (d) the MPC policy comes from a Newton step, so its error $J_{\tilde\mu}-J^*$ obeys a superlinear relation and is negligible if $\tilde J-J^*$ is small.

**Model mismatch and disturbance estimation.** Unmodeled dynamics, parameter drift or varying workloads can make the true system differ from the predictions. Ignoring this may cause long-term deviations from targets or degraded constraint handling (p. 130). In chemical process control, modeling errors are often viewed as a constant or slowly varying disturbance. The controller infers it from measurements and compensates (the internal model principle, Francis–Wonham). The integral term of PID is the simplest instance: by accumulating output error it acts as a dynamic estimator of the unknown average disturbance (pp. 130–131). In MPC the same idea uses state augmentation (p. 131):
- Replace $x_{k+1}=f(x_k,u_k)$ by $x_{k+1}=f(x_k,u_k)+w_k$ with $w_{k+1}=w_k$, and use the augmented state $\tilde x_k=(x_k,w_k)$.
- If $x_k$ is observed perfectly, so is $\tilde x_k$, since $w_k=x_k-f(x_{k-1},u_{k-1})$.
- Generalization: $x_{k+1}=f(x_k,u_k)+Ew_k$ with $E$ a known matrix. With inexact state measurement, MPC is combined with a Kalman filter or related estimator that updates state and disturbance estimates. The MPC optimization then treats these estimates as exact.
- For many chemical-process systems, the author says this captures the main benefits of more elaborate adaptive or robust MPC. Larger or faster-varying uncertainty may need more sophisticated formulations (p. 131).

### 1.7 RL and decision/control (pp. 131–139)
Ideas from decision/control/DP (principle of optimality, MDPs, POMDP, policy and value iteration) and AI/RL (learning from data, simulation, model-free methods, feature-based representations, A\*/games/heuristics) are described as complementary, with a synergy from the late 80s–early 90s (Fig. 1.7.1, p. 132). Cultural differences remain: decision/control relies traditionally on mathematical analysis, AI emphasizes challenging implementations (p. 132).

**1.7.1 Terminology (AI/RL = optimal control)** (pp. 132–133):
- environment = system; agent = decision maker or controller; action = decision or control;
- reward of a stage = (opposite of) cost of a stage; state value = (opposite of) cost from a state; value (reward) function = (opposite of) cost function; maximizing the value function = minimizing the cost function;
- action (state-action) value = Q-factor (Q-value);
- planning = solving a DP problem with a known model (often related to MPC and approximation in value space);
- learning = solving a DP problem without a known model (the principal meaning in AI/RL);
- self-learning (self-play) = solving a DP problem with some form of policy iteration;
- deep RL = approximate DP with deep neural networks for value and/or policy;
- prediction = policy evaluation; generalized policy iteration = optimistic policy iteration;
- state abstraction = state aggregation; temporal abstraction = time aggregation;
- learning a model = system identification;
- episodic task = finite-step trajectory; continuing task = infinite-step trajectory;
- experience replay = reuse of samples in simulation;
- Bellman operator = DP mapping; backup = applying it at one state; sweep = at all states;
- greedy policy w.r.t. $J$ = minimizing policy in the DP expression defined by $J$;
- afterstate = post-decision state; ground truth = empirical evidence from direct observation.

**1.7.2 Notation** (p. 134). The book keeps the "standard" notation of the Bellman/Pontryagin era (consistent with the author's other DP books):
- $x$ state ($i$ for finite-state), $u$ control, $w$ disturbance, $J$ cost function;
- $f$ system function: $x_{k+1}=f(x_k,u_k)$, or $f(x_k,u_k,w_k)$ if stochastic; $g$ cost per stage; $p_{xy}(u)$ (also $p_{ij}(u)$) transition probability; $\alpha$ discount factor.

AI literature mostly uses $s$, $a$, $r(s,a,s')$, $p(s'\mid s,a)$, $\gamma$. The author says this suits finite-state problems but not continuous spaces, where it needs transition distributions over continuous spaces and gives "more complex and less intuitive mathematics". It is also cumbersome for deterministic problems (p. 134).

**1.7.3 DP and RL** (p. 135). They are connected by their focus on sequential decision making, so any DP problem can in principle be addressed by RL and vice versa. The author notes that one may argue RL's algorithmic toolbox is broader (gradient descent, random search, simulation, statistics, neural networks), though DP research has also used such tools less intensively. In the AI view a machine learns by trial and error from an environment. In decision and control, adaptive control is the only problem type where uncertainty and exploration arise significantly. The author says RL brought a fresh and ambitious spirit; before the DP–RL connections were recognized, high-dimensional Euclidean-state and POMDP problems were considered totally intractable for DP (p. 135).

**1.7.4 LLMs and DP/RL** (p. 136). RL optimizes policies for sequential control. LLMs handle language and code. The author argues that they are complementary. RL, especially policy-space approximation (Sec. 3.5), has refined pre-trained transformers off-line. LLMs help RL by injecting domain knowledge, improving interpretability, and assisting with formulation, algorithm selection and code. The author's conclusion is that the interaction is "not merely additive, it is multiplicative" (p. 136).

**1.7.5 Machine learning and optimization** (pp. 136–139).
- *Supervised learning:* labeled input-output pairs, a parametrized function fitted by (typically gradient-type) minimization of a loss.
- *Unsupervised learning:* unlabeled data, finding structure (clustering, etc.). The author says some methods can be related to DP but the connection is not strong, and that it does not seem to align well with this book's sequential decision applications.
- *RL:* it does not start from a dataset. It generates data on-line or off-line, as its optimization algorithm needs, and the data depend on the policy used. Ideally data would come from an optimal policy, which is unlikely to be available. One collects data with a sequence of (hopefully) improving policies, the essence of approximate policy iteration, which is therefore a focal point of the book (p. 137). Offline/batch RL starts from a historical dataset (footnote, p. 137).
- *Semi-supervised learning* augments labeled data with unlabeled data. It is related to active learning, where DP-like methods are used (p. 138).
- *Optimization:* it may or may not involve data. Problems are categorized by structure, e.g. static (single decision) versus dynamic (sequential decisions with feedback). Stochastic problems are dynamic unless open-loop. Deterministic problems can be formulated either way, sometimes artificially staged for algorithmic expediency (p. 138). Discrete problems (integer, combinatorial) are hard and often handled by heuristics. Continuous ones use calculus and convexity (Lagrange multipliers, duality, linear/nonlinear/convex programming). Some graph problems use continuous network optimization; hybrid problems usually need discrete techniques (p. 138).
- *DP:* it applies to just about any optimization problem formulated as a sequential decision problem (Secs. 1.2–1.4). It handles discrete and continuous problems, "is not concerned with local minima", and focuses on global minima (p. 139).
- The author contrasts optimization (organized around mathematical structure and algorithm analysis) with machine learning (organized around how data are collected, used and analyzed, with strong statistical emphasis) (p. 139).

**1.7.6 Mathematics in ML and optimization** (p. 139, start only). Optimization emphasizes general methods with rigorous guarantees. The author notes that machine learning has strongly mathematical lines of work but also useful structures (neural networks, LLMs, image generators) that are not well understood mathematically. This can feed a perception that rigorous mathematics is a low-payoff investment in many practical ML contexts. A footnote cites He et al. (2016; two equations) and Vaswani et al. (2017; six equations), with citation counts as of November 2025 (p. 139).

## Toy example (ours, not from the text)
**Goal:** classical MPC with $\ell=2$ as rollout, on a scalar system.

System $x_{k+1}=x_k+u_k$, cost per stage $g=x^2+u^2$, no constraints (so $u=0$, $x=0$ is the zero-cost point). Take $x_k=4$.

1. The 2-stage problem with $x_{k+2}=0$: $x_{k+1}=4+u_k$ and the last control must be $u_{k+1}=-x_{k+1}$ (so that $x_{k+2}=x_{k+1}+u_{k+1}=0$).
2. Cost: $4^2+u_k^2+x_{k+1}^2+u_{k+1}^2=16+u_k^2+2(4+u_k)^2$. Derivative: $2u_k+4(4+u_k)=0\Rightarrow u_k=-16/6=-8/3$.
3. Then $x_{k+1}=4-8/3=4/3$ and the cost is $16+64/9+2\cdot16/9=16+96/9=80/3\approx26.67$.
4. Check other choices: $u_k=-4$ (the base policy $u=-x$) gives $16+16+0=32$; $u_k=-2$ gives $16+4+2\cdot4=28$. Both exceed 26.67.
5. Rollout view: the base policy "reach 0 in $\ell-1=1$ stage" has cost-to-go $\tilde J(y)=y^2+y^2=2y^2$. One-step lookahead minimizes $x^2+u^2+2(x+u)^2$, the same function as in step 2.
6. In general the minimizer is $u=-2x/3$, so the closed loop is $x_{k+1}=x_k/3$: $4,\ 4/3,\ 4/9,\dots$ This is stable.
7. Lyapunov condition (1.90) with $G(x)=2x^2$ (no constraints): $(TG)(x)=x^2+(2x/3)^2+2(x/3)^2=(1+4/9+2/9)x^2=\tfrac53x^2\le2x^2=G(x)$. ✓

## Concepts
- [[model predictive control]] — at each state solve an $\ell$-stage deterministic problem, apply only the first control, repeat; read here as rollout and as a Newton step (pp. 118–122)
- [[PID control]] — three-parameter controller holding a single-input single-output system at a set point (p. 109)
- [[integral action]] — in PID, the integral term acts as a dynamic estimator of an unknown average disturbance (p. 131)
- [[stability]] — here: MPC/rollout policy is stable if the base policy or terminal cost $G$ satisfies the stated conditions (pp. 122–123)
- [[observer (state estimator)]] — with Kalman filter, used to reconstruct the state for MPC when it is not measured (pp. 129, 131)
- [[Kalman filter]] — updates state and disturbance estimates in MPC with mismatch (p. 131)
- [[robustness]] — here: the loss $K_L-K^*$ from keeping the nominal policy when parameters change (p. 115)
- [[Bellman equation / value function]] — MPC and rollout are Newton steps for solving it (pp. 119, 122)
- [[policy]] — here also "base policy" and "MPC policy" (pp. 112, 122)
- [[model-based vs model-free RL]] — "planning" vs "learning" in the AI/RL glossary; data-driven MPC replaces the model by data (pp. 129, 133)
- [[Markov decision process]] — notation for finite-state MDPs, $p_{ij}(u)$ vs $p(s'\mid s,a)$ (p. 134)
- [[exploration vs exploitation]] — in the author's account, uncertainty and exploration arise significantly only in adaptive control among decision/control problems (p. 135)
- [[rollout]] (new) — one-step or multistep lookahead with cost-to-go approximated by a base policy; here used for replanning (pp. 112, 122)
- [[parameter identifiability]] (new) — whether the closed-loop data determine the unknown parameters (p. 109)
- [[belief state]] (new) — pair $(x_k,b_k)$ of observed state and posterior over $\theta$ (p. 117)
- [[certainty equivalence]] (new) — replace future uncertain quantities by fixed values, keep current-stage randomness (p. 128)
- [[terminal cost approximation]] (new) — $G(x_{k+\ell})$ in (1.89) (p. 122)
- [[Lyapunov condition (MPC)]] (new) — $TG\le G$, (1.90) (p. 123)
- [[invariant set]] (new) — $X$ with $\forall x\in X\ \exists u\in U(x): f(x,u)\in X$ (p. 126)
- [[state augmentation for disturbance estimation]] (new) — treat a constant modeling error $w_k$ as extra state (p. 131)
- [[gain scheduling]] (new) — precompute a controller per known parameter value and switch (footnote, p. 111)

## Canonical instances
- [[identifiability under closed loop]] — scalar system under $\gamma x_k$: only $a+b\gamma$ identifiable (pp. 110–111)
- [[LQ rollout replanning]] — $b=2$, $r=0.5$ nominal; $K^*\le\tilde K_L\le K_L$ (pp. 113–116)
- [[cart-pole regulation]] — inverted pendulum regulation problem (p. 119)
- [[car with obstacles]] — constrained motion A to B, needs on-line replanning (p. 120)
- [[unstable scalar system with state constraint]] — $x_{k+1}=2x_k+u_k$, $|u|\le1$, largest invariant set $|x|\le1$ (pp. 126–128)

## Bridges (candidates)
- [structural-analogy] Integral term of PID ↔ control-theory: disturbance observer on an augmented state $(x,w)$ with $w_{k+1}=w_k$ — the author calls the integral term the simplest instance of the idea of inferring a constant disturbance, and calls the MPC version "a similar strategy" (pp. 130–131).
- [structural-analogy] Belief state $(x_k,b_k)$ ↔ Kalman filter state estimate: both summarize the information history in a recursively updated quantity (pp. 117, 131).
- [structural-analogy] Recursion (1.95) for the largest invariant set ↔ value iteration: the author says it resembles value iteration (p. 127).
- [structural-analogy] MPC "apply the first control, then replan" ↔ rollout/approximation in value space: both are one Newton step on the Bellman equation (pp. 119–122).
- [metaphor] Invariant set ↔ homeostasis: staying inside a viable range for all future times.

## Questions this raises
- How does the Newton-step argument give conditions beyond $TG\le G$ for stability when $G$ is only an approximation? (Secs. 1.5 and 1.6.9 refer back to this.)
- When is approximating $J^*$ by a base-policy cost (rollout) good enough that the error ratio $(\tilde J-J^*)/(J-J^*)$ is small outside LQ problems?
- How should one trade off exploration (probing to improve estimates) against control in the POMDP view of adaptive control?
- How much accuracy does a data-driven model need, and how can it be updated on-line safely?

## Reading notes
- Part 5 of 6. It begins mid Sec. 1.6.8 (printed p. 109, at PID control and system identification). It ends on printed p. 139 in the middle of Sec. 1.7.6, with the footnote about citation counts. Sec. 1.7.6 is cut off at the end of this part; its remainder is not in these pages.
- Page offset: printed = pdf − 20.
- The text layer garbles symbols: ∈ appears as ↓, "−" as →, ∞ as ↑, and sums as "!". I checked the equations against the page images.
- The formula for $K_L$ and the rollout formulas in Ex. 1.6.7 are said to come from "earlier discussion" in the chapter, which is not in this part. I report them as printed (p. 114).
- Figs. 1.6.11–1.6.20 have text-layer clutter. I read them from the images.
- Section references to later chapters (Secs. 2.5.3, 2.10, 2.11, 3.5) are only pointers in these pages. Their content is not in this unit.
