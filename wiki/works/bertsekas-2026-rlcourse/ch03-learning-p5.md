---
id: bertsekas-2026-rlcourse/ch03-learning-p5
work: bertsekas-2026-rlcourse
unit: "3 Learning Values and Policies (part 5/5): end of 3.5, 3.6 Aggregation, 3.7 Notes, Sources, and Exercises"
pages: 429-462
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Aggregation: solving a small "aggregate" DP problem to approximate a large one

## L0 — One line
Aggregation builds a much smaller DP problem on "aggregate states", solves it exactly, and interpolates its optimal costs into a cost approximation for the original problem, with an error that is small when $J^*$ varies little inside each aggregate's footprint.

## L1 — The gist (≤ 120 words)
How can we get a good cost-to-go approximation for a discounted DP problem with a huge state space? Aggregation groups states into aggregate states, defines transition probabilities between them through disaggregation and aggregation probabilities, and solves the small problem exactly. The aggregate optimal costs are interpolated back to all original states and used in lookahead. A max-norm contraction guarantees a unique solution. Under the condition $I_x\subset S_x$ (3.91), the error is bounded by $\epsilon/(1-\alpha)$, where $\epsilon$ is the largest variation of $J^*$ inside a footprint. The unit covers continuous spaces, POMDP belief discretization, feature-based and biased aggregation, and asynchronous distributed solution. It starts with the end of the retraining discussion (Section 3.5) and closes the chapter with notes and exercises.

**Prerequisites:** discounted infinite-horizon DP and the Bellman equation; max norm and contraction mappings; probability distributions and convex combinations; belief states of POMDPs (basic idea).

## L2 — Key ideas
- Aggregation is problem approximation: solve a small aggregate DP problem exactly, then use its optimal costs as the terminal cost of one-step or multistep lookahead. Its optimal policy may serve as a base policy for truncated rollout (p. 430).
- Representative-state aggregation uses aggregation probabilities $\phi_{jy}$ to define $\hat p_{xy}(u)$; the expected cost $\hat g(x,u)$ is computed from $p_{xj}(u)$ and $g$. The interpolation $\tilde J(j)=\sum_y\phi_{jy}r_y^*$ gives a linear architecture whose basis functions are the $\phi_{jy}$ (pp. 433–434).
- Hard aggregation gives a piecewise constant $\tilde J$ over disjoint footprints. The error is at most $\epsilon/(1-\alpha)$, with $\epsilon$ the maximum variation of $J^*$ within footprints (pp. 435–436, 444).
- General aggregation adds disaggregation probabilities $d_{xi}$ and sets $I_x$. The composite Bellman operator $H$ is a max-norm contraction of modulus $\alpha$, with dimension equal to the number of aggregate states (pp. 440–443).
- With continuous state and control spaces, discretizing only the state may fail to approximate the fastest route arbitrarily closely (Example 3.6.2). With a finite control space, representative-state aggregation is very well suited, notably for POMDP belief discretization (pp. 437–439).
- Features can define footprints, giving a nonlinear piecewise constant architecture. Biased aggregation (cost $g-V(i)+\alpha V(j)$) gives $\tilde J=\hat J+V$; the modified-cost problem has the same optimal policies as the original, assuming it is solved exactly (pp. 446–449).
- Aggregation can be solved by asynchronous distributed value iteration, with convergence from sup-norm contraction (pp. 449–451).
- Retraining a policy on a new dataset, adversarial training, knowledge distillation and mixture-of-experts switching are options discussed for retraining after changes and for limited computing resources (p. 429).

## L3 — Walkthrough

### End of 3.5: retraining and mixture of experts (p. 429)
**Retraining.** After a dataset is chosen, the policy can be retrained by policy approximation with parametric comparison training (Section 2.3.6, as in imitating an expert). Another option is adversarial training: expose the policy to adversarial examples (states designed to trigger bad behavior) and fine-tune with a policy gradient or random search method (p. 429).

**Knowledge distillation.** A smaller "student" policy is trained to mimic a larger "teacher" policy when computing resources are limited. One possibility is to use the teacher as an expert that generates the training dataset (p. 429).

**Mixture of experts.** The system may change structurally after transitions to special states (e.g., parts disabled or repurposed). The scheme keeps multiple policies ("experts") and switches among them. The change must be detected on line, and a gating mechanism enables the most relevant policy. The policies may be trained off line, possibly by refining a pre-trained policy. Examples named: multiple model control design (Section 1.6.8) and a scheme used in DeepSeek (p. 429).

### 3.6 Aggregation: setting (pp. 429–430)
- Create special subsets of states ("aggregate states"), solve the aggregate problem exactly by DP (off-line training), then use its optimal cost-to-go (or an approximation) as a terminal cost approximation in one-step or multistep lookahead. The aggregate policy may also be a base policy for truncated rollout (p. 430).
- Aggregation often yields a piecewise constant approximation. This is a linear feature-based parametrization whose features are 0-1 membership functions (Example 3.1.1) (p. 430).
- Setting: discounted infinite-horizon problem, states $1,\dots,n$, transition probabilities $p_{ij}(u)$, cost $\alpha^k g(i,u,j)$ at time $k$, $\alpha\in(0,1)$. Policies are stationary and deterministic, with $\mu(i)\in U(i)$, $U(i)$ finite. $J_\mu$ and $J^*$ are $n$-vectors (p. 430).

### 3.6.1 Aggregation with representative states (pp. 430–436)
**Example 3.6.1 (coarse grid).** States are grid points in the plane. A subset of "representative" states $x$ forms a coarse grid. A representative $x$ may have $p_{xj}(u)>0$ for non-representative $j$. To handle this, introduce artificial aggregation probabilities $\phi_{jy}$ from non-representative $j$ to representative $y$: a transition $x\to j$ is followed by $j\to y$ with probability $\phi_{jy}$ (p. 431). Then (p. 432):
$$\hat p_{xy}(u)=\sum_{j=1}^n p_{xj}(u)\phi_{jy},\qquad \hat g(x,u)=\sum_{j=1}^n p_{xj}(u)g(x,u,j). \tag{3.77}$$
With $\mathcal A$ the set of representative states and $r_x^*$ the optimal aggregate costs,
$$\tilde J(j)=\sum_{y\in\mathcal A}\phi_{jy}r_y^*,\quad j=1,\dots,n. \tag{3.78}$$
$\phi_{jy}$ should measure proximity of $j$ to $y$. Setting $\phi_{jy_j}=1$ for the closest $y_j$ gives a piecewise constant $\tilde J$ (p. 432).

**Framework (p. 433).** Choose a finite $\mathcal A\subset\{1,\dots,n\}$.
(a) Aggregation probabilities satisfy $\sum_{y\in\mathcal A}\phi_{jy}=1$, $\phi_{jy}\ge0$, $\phi_{yy}=1$.
(b) $\hat p_{xy}(u)=\sum_j p_{xj}(u)\phi_{jy}$ (3.79).
(c) $\hat g(x,u)=\sum_j p_{xj}(u)g(x,u,j)$ (3.80).
Solve for $r_y^*$, then interpolate: $\tilde J(j)=\sum_y\phi_{jy}r_y^*$ (3.81).
Shapes (our bookkeeping, added): with $m=|\mathcal A|$, $\Phi$ is $n\times m$ and $\hat p(u)$ is $m\times m$. The vector $\tilde J=\Phi r^*$ lies in $\mathbb R^n$.

The $\phi_{jy}$ can be arbitrary nonnegative weights summing to 1; they express "strength of relation". The vectors $\{\phi_{jy}\mid j\}$ act as basis functions for a linear approximation via (3.81) (p. 434).

**Hard aggregation and error bound.** For each $j$, $\phi_{jy}=0$ except one $y_j$ with $\phi_{jy_j}=1$ (and $\phi_{yy}=1$). Then $\tilde J$ is constant, equal to $r_y^*$, on the footprint $S_y=\{j\mid\phi_{jy}=1\}$. Footprints are disjoint and partition the state space (p. 435). The text states that it can be shown that
$$|J^*(j)-\tilde J(j)|\le\frac{\epsilon}{1-\alpha},\qquad \epsilon=\max_{y\in\mathcal A}\max_{i,j\in S_y}|J^*(i)-J^*(j)|,$$
the maximum variation of $J^*$ within footprints. It is extended to the general framework in the next sections. Message: the error is small if $J^*$ varies little within each $S_y$ (pp. 435–436). Nearest-neighbor aggregation in the grid context is a hard-aggregation case (p. 436).

*Intuition note.* If every state in a group has nearly the same optimal cost, one number per group describes $J^*$ well. (Our reading, not stated in the text: the factor $1/(1-\alpha)$ plausibly reflects errors accumulating over the discounted horizon.)

**Solving the aggregate problem (p. 436).** Compute $\hat p_{xy}(u)$ and $\hat g(x,u)$ algebraically or by simulation, then use VI or PI. This is plausible if there are few representative states. Alternatively, use simulation-based VI/PI, since a simulator of the original problem can build a simulator of the aggregate problem. If the original problem is deterministic and hard aggregation is used, the aggregate problem is deterministic and solvable by shortest-path-like methods. For undiscounted shortest-path problems, the termination state must then be a representative state. Without hard aggregation the aggregate problem is stochastic (p. 436).

### 3.6.2 Continuous control space discretization (pp. 437–438)
With a continuous state space and finite controls, the aggregate problem is a finite discounted problem. If the disturbance space is also infinite, the aggregate transition probabilities and expected costs need integration. If both state and control are continuous, both must be discretized with representative state-control pairs (p. 437).

**Example 3.6.2 (continuous shortest path).** A car moves at 1 m/s from A to B at opposite corners of a 1000 m square, avoiding obstacles, and may drive in any direction. Discretize with a square grid and allow only horizontal and vertical moves to adjacent grid points. The author asks whether a fine grid approximates the fastest route arbitrarily well. The answer is no. The discretized optimal time is 2000 s however fine the grid is. In the continuous problem it can be as little as $\sqrt2\cdot1000$ s, when the straight line meets no obstacle (pp. 437–438).

The difficulty is that the state space is finely discretized but the control space is not. The remedy is to discretize the controls too ("representative controls"). The resulting discretized problem is a stochastic infinite-horizon problem, even if the original is deterministic. Under reasonable assumptions the author states consistency: the discretized optimal cost converges to the original as both discretizations refine. Details are outside the scope (p. 438).

### 3.6.3 Continuous state space — POMDP discretization (pp. 438–439)
Let the state space be a bounded convex set $B$ (e.g., the unit simplex), with finite control set $U$. States are written $b$, to recall POMDP belief states. The Bellman operator is
$$(TJ)(b)=\min_{u\in U}E_w\{g(b,u,w)+\alpha J(f(b,u,w))\},\ b\in B.$$
Choose representative states $x_1,\dots,x_m\in B$ whose convex hull is $B$, so $b=\sum_{i=1}^m\phi_{bx_i}x_i$ with $\phi_{bx_i}\ge0$, $\sum_i\phi_{bx_i}=1$ (aggregation probabilities) (p. 439). For $r=(r_{x_1},\dots,r_{x_m})$ define
$$(\hat Tr)(x_i)=\min_{u\in U}E_w\Big\{g(x_i,u,w)+\alpha\sum_{j=1}^m\phi_{f(x_i,u,w)x_j}r_{x_j}\Big\}.$$
It can be shown that $\hat T$ is a max-norm contraction (the proof for a similar result is in 3.6.4), so $r_{x_i}=(\hat Tr)(x_i)$ has a unique solution. The dynamics: from $x_i$ under $u$, move to $f(x_i,u,w)$ at cost $g(x_i,u,w)$, then to $x_j$ with probability $\phi_{f(x_i,u,w)x_j}$. Approximate $\tilde J(b)=\sum_i\phi_{bx_i}r^*_{x_i}$ for all $b\in B$. The author "reasonably expects" convergence as the number of representative states grows (p. 439).

For a POMDP belief space, the result is a finite-state perfect-information discounted problem. It can be solved exactly if aggregate probabilities and costs are available analytically or the number of representative beliefs is small enough for simulation. It can also be approached by certainty equivalence-type problem approximation or by rollout (on-line). [LHB25] develops a belief-feature POMDP aggregation (p. 439).

### 3.6.4 General aggregation (pp. 440–443)
Replace representative states by subsets $I_x\subset\{1,\dots,n\}$ (p. 440). Framework: finite $\mathcal A$ of aggregate states; (a) subsets $I_x$; (b) disaggregation probabilities $\{d_{xi}\}$ for each $x$, with
$$d_{xi}=0\quad\text{for all }i\notin I_x,\ x\in\mathcal A; \tag{3.82}$$
(c) aggregation probabilities $\{\phi_{jy}\mid y\in\mathcal A\}$ for each $j$. The dynamics are: (i) from aggregate $x$, generate $i\in I_x$ by $d_{xi}$; (ii) transition $i\to j$ by $p_{ij}(u)$ with cost $g(i,u,j)$; (iii) from $j$, generate aggregate $y$ by $\phi_{jy}$. Then $\tilde J(j)=\sum_y\phi_{jy}r_y^*$ (3.83) (p. 440).

If each $I_x$ is a single state, $d_{xi}$ is atomic and we recover representative states (p. 441).

The aggregate problem has two copies of $\{1,\dots,n\}$ plus $\mathcal A$. Define $r^*_x$ (optimal cost-to-go from aggregate $x$), $\tilde J_0(i)$ (from an original state just generated from an aggregate state) and $\tilde J_1(j)$ (from an original state just generated from an original state). They differ because of the intermediate aggregate transitions (p. 441). The Bellman equations are
$$r_x^*=\sum_{i\in I_x}d_{xi}\tilde J_0(i),\ x\in\mathcal A, \tag{3.84}$$
$$\tilde J_0(i)=\min_{u\in U(i)}\sum_{j=1}^np_{ij}(u)\big(g(i,u,j)+\alpha\tilde J_1(j)\big),\ i=1,\dots,n, \tag{3.85}$$
$$\tilde J_1(j)=\sum_{y\in\mathcal A}\phi_{jy}r^*_y,\ j=1,\dots,n. \tag{3.86}$$
Substituting gives $r^*=Hr^*$ with
$$r_x^*=\sum_{i\in I_x}d_{xi}\min_{u\in U(i)}\sum_{j=1}^np_{ij}(u)\Big(g(i,u,j)+\alpha\sum_{y\in\mathcal A}\phi_{jy}r_y^*\Big),\ x\in\mathcal A, \tag{3.87}$$
$$(Hr)(x)=\sum_{i\in I_x}d_{xi}\min_{u\in U(i)}\sum_{j=1}^np_{ij}(u)\Big(g(i,u,j)+\alpha\sum_{y\in\mathcal A}\phi_{jy}r_y\Big). \tag{3.88}$$
(p. 442).

**$H$ is a max-norm contraction.** For vectors $r,r'$, with $\|\cdot\|$ the max norm (p. 442):
$$(Hr)(x)\le\sum_{i}d_{xi}\min_u\sum_jp_{ij}(u)\Big(g+\alpha\sum_y\phi_{jy}\big(r'_y+\|r-r'\|\big)\Big)=(Hr')(x)+\alpha\|r-r'\|.$$
The equality uses that $d_{xi}$, $p_{ij}(u)$, $\phi_{jy}$ are probabilities. Hence $(Hr)(x)-(Hr')(x)\le\alpha\|r-r'\|$. Reversing roles gives the same bound for $(Hr')(x)-(Hr)(x)$. Taking the maximum over $x$:
$$\|Hr-Hr'\|\le\alpha\|r-r'\|. \tag{3.89}$$
So (3.87) has the unique solution $r^*$ (pp. 442–443).

The composite equation has dimension $|\mathcal A|$, potentially much smaller than $n$. It can be solved by simulation-based analogs of VI and PI, with strong convergence properties from (3.89) (p. 443).

*Intuition note.* Because each step averages with probabilities and then discounts, differences between two cost guesses shrink by at least a factor $\alpha$ per application. That is why iterating $H$ converges to one answer.

### 3.6.5 Types of aggregation and error bounds (pp. 443–445)
Footprint: $S_y=\{j\mid\phi_{jy}>0\}$ (3.90). Natural assumption: $I_x\subset S_x$ for all $x$ (3.91): a state related to $x$ in disaggregation is also related in aggregation (p. 443). Under hard aggregation the footprints partition the state space, and (3.91) says $\phi_{ix}=1$ if $d_{xi}>0$ (p. 444).

Other special cases (p. 444): (a) *soft aggregation*: footprints overlap partially, $\phi$ positive on the overlap, so $\tilde J$ is piecewise constant except that it changes "smoothly" on overlaps [SJJ95]. (b) *Aggregation with representative features*: aggregate states are nonempty subsets of original states that need not form a partition, e.g., the states sharing one of a chosen set of feature vectors.

**Proposition 3.6.1 (error bound for general aggregation).** Let (3.91) hold. Then
$$|J^*(j)-\tilde J(j)|\le\frac{\epsilon}{1-\alpha}\quad\text{for all }j\text{ such that }j\in S_y,\ y\in\mathcal A,$$
where $\epsilon=\max_{y\in\mathcal A}\max_{i,j\in S_y}|J^*(i)-J^*(j)|$. First given by Tsitsiklis and Van Roy for hard aggregation, extended to the case where only (3.91) holds by Li and Bertsekas (p. 444). A counterexample where the bound fails because (3.91) is violated is Exercise 3.3 (p. 445).

**Selecting aggregate states.** There is no mathematical theory at present. Intuition and problem insight suggest choices, which are then tuned by experiment. If $J^*$ is piecewise constant on a partition $\{S_y\}$ ($J^*(j)=r_y^*$ on $S_y$), then by Prop. 3.6.1 hard aggregation with $I_x=S_x$ is exact. This suggests that states in a footprint should have roughly equal optimal cost. If known features "predict well" $J^*$ through some architecture, form aggregates of states with similar features: feature-based aggregation [BeT96] (p. 445).

### 3.6.6 Aggregation using features (p. 446)
Guideline: $\max_{i,j\in S_y}|J^*(i)-J^*(j)|\approx0$. Use a feature mapping $F$ taking state $i$ to an $m$-dimensional feature vector $F(i)$. If states with nearly equal features have nearly equal $J^*$, partition the feature space more or less regularly. This induces possibly irregular subsets of the state space, each used as a footprint (Fig. 3.6.7). The number of aggregate states may be very large. The advantage over the linear architectures of Section 3.1 (one weight per feature) is that a weight is assigned to each subset of the feature-space partition. This is a nonlinear (piecewise constant) architecture that "may be much more powerful" than the linear one. Features can come from a neural network [Ber18a] or any automatic feature-generating method (p. 446).

### 3.6.7 Biased aggregation (pp. 446–449)
Introduce a bias vector $V=(V(1),\dots,V(n))$, which should be cheap to compute (e.g., from neural-network approximate PI, rollout or problem approximation). With $V=0$ we recover Section 3.6.4. Otherwise $\tilde J$ is $V$ plus a local correction $\hat J$ (Fig. 3.6.8) (p. 447). The method replaces the stage cost by
$$g(i,u,j)-V(i)+\alpha V(j), \tag{3.92}$$
applies aggregation of 3.6.4 to the modified problem to get $\hat J$, and sets $\tilde J(i)=\hat J(i)+V(i)$ (p. 447).

**Justification.** $\hat J$, the optimal cost of the modified problem, satisfies
$$\hat J(i)=\min_{u}\sum_jp_{ij}(u)\big(g(i,u,j)-V(i)+\alpha V(j)+\alpha\hat J(j)\big),$$
or equivalently
$$\hat J(i)+V(i)=\min_{u}\sum_jp_{ij}(u)\Big(g(i,u,j)+\alpha\big(\hat J(j)+V(j)\big)\Big).$$
(Added step: $V(i)$ does not depend on $u$ or $j$ and $\sum_jp_{ij}(u)=1$, so it moves to the left side.) Comparing with the original Bellman equation gives $J^*(i)=\hat J(i)+V(i)$, and both problems have the same optimal policies. This assumes the modified problem is solved exactly. If it is solved approximately by (unbiased) aggregation, the choice of $V$ and the architecture may substantially affect the quality of the resulting approximation and policies (pp. 447–448).

Interpretation (Fig. 3.6.9): the transitions are the same as in Fig. 3.6.6, with cost $-V(i)$ attached to disaggregation to $i$ and $V(j)$ to aggregation from $j$. Key insight: biased aggregation is unbiased aggregation applied to a modified, equivalent problem. So results, algorithms and intuition carry over, including simulation-based policy evaluation, policy improvement and Q-learning, as long as $V(i)$ is available when needed (pp. 448–449). Footnote: this relates to a classical DP scheme called cost shaping in the RL literature (p. 447).

Choice of $V$: it should capture much of the nonlinearity or "shape" of $J^*$. For hard aggregation, by Prop. 3.6.1, $V$ should make the variation of $J^*-V$ small within footprints, so $V$ should approximate $J^*$ up to a constant (p. 449).

*Intuition note.* $V$ supplies the overall shape of the cost function, and aggregation only needs to represent what is left, which is hopefully nearly flat inside each footprint.

### 3.6.8 Asynchronous distributed aggregation (pp. 449–451)
Setting: large discounted DP, hard aggregation, partition into subsets $x_1,\dots,x_m$, one processor per subset. Each processor $\ell$ keeps local costs $J(i)$ for $i\in x_\ell$ and an aggregate cost $R(\ell)=\sum_{i\in x_\ell}d_{x_\ell i}J(i)$, which it communicates to others (pp. 449–450). Synchronous iteration:
$$J_{k+1}(i)=\min_{u\in U(i)}H_\ell(i,u,J_k,R_k),\ i\in x_\ell, \tag{3.93}$$
$$R_k(\ell)=\sum_{i\in x_\ell}d_{x_\ell i}J_k(i), \tag{3.94}$$
$$H_\ell(i,u,J,R)=\sum_{j=1}^np_{ij}(u)g(i,u,j)+\alpha\sum_{j\in x_\ell}p_{ij}(u)J(j)+\alpha\sum_{j\notin x_\ell}p_{ij}(u)R\big(x(j)\big), \tag{3.95}$$
where $x(j)$ is the subset containing $j$. Shapes (added): $J\in\mathbb R^n$, $R\in\mathbb R^m$. This is ordinary VI except that states updated by other processors are represented by aggregate costs $R(x(j))$ (p. 450).

The iteration is a sup-norm contraction of modulus $\alpha$ (it follows because $\{d_{x_\ell i}\}$ is a probability distribution). It converges to the unique solution of
$$J(i)=\min_uH_\ell(i,u,J,R),\quad R(\ell)=\sum_{i\in x_\ell}d_{x_\ell i}J(i), \tag{3.96}$$
which are Bellman equations of an aggregate problem. They differ from (3.84)–(3.86) in that (3.95) uses $J(j)$, not $R(x(j))$, for $j\in x_\ell$ (p. 450).

**Asynchronous version.** Aggregate costs may be outdated by communication delays, and only a (possibly empty) subset $I_{\ell,k}\subset x_\ell$ is updated at time $k$:
$$J_{k+1}(i)=\min_uH_\ell\big(i,u,J_k,R_{\tau_{1,k}}(1),\dots,R_{\tau_{m,k}}(m)\big),\ i\in I_{\ell,k}, \tag{3.97}$$
with $0\le\tau_{\ell,k}\le k$ and $R_\tau(\ell)=\sum_{i\in x_\ell}d_{x_\ell i}J_\tau(i)$. Convergence needs every $i\in x_\ell$ to be in $I_{\ell,k}$ for infinitely many $k$, and $\lim_{k\to\infty}\tau_{\ell,k}=\infty$. The proof uses the author's asynchronous convergence theory [Ber82a] and the sup-norm contraction of the mapping behind (3.96). The monotonicity property is also sufficient, which is useful for related undiscounted aggregation algorithms [BeY10] (p. 451).

### 3.7 Notes, sources, and exercises (pp. 451–462)
**Notes (compressed, author's views).**
- *3.1–3.2 (pp. 451–453).* The chapter's treatment of architectures and neural networks is limited and meant to connect with approximate DP. Linear feature architectures can also be trained by TD($\lambda$), LSTD($\lambda$), LSPE($\lambda$), which this book does not discuss. Open questions mentioned: whether more layers add approximation power at a fixed number of weights, and, with more weights than data, how to pick among the infinitely many perfect fits one that works on test data.
- *3.3 (pp. 453–454).* Fitted VI is old and can be unstable through error accumulation over long horizons. DQN (Mnih et al.) was tested on 49 Atari games. The author says implementing approximate VI/PI is hard and its difficulty tends to be underestimated, because the literature emphasizes successes. Long multistep lookahead with a simple terminal cost approximation, and rollout, are "typically much easier" and often succeed reliably. Truncated rollout with a trained terminal cost is an intermediate approach that often works well.
- *3.4 (pp. 454–455).* Policy approximation as classification is due to Lagoudakis and Parr. Other classifiers (nearest neighbor, SVMs, neural networks) may be used.
- *3.5 (pp. 455–457).* The likelihood-ratio policy gradient (Williams) is commonly called REINFORCE. Challenges: slow convergence and noise (baselines, variance reduction, second-order information) and local minima (Exercise 3.2). A policy gradient may also yield a randomized policy that must be converted. The natural gradient comes from information geometry (Amari). The constrained natural gradient of Section 3.5.2 is "presented here for the first time" and not tested extensively. Actor-critic methods are not covered. The cross-entropy method is thought effective primarily for low-dimensional parameter spaces (tetris examples). The author argues policy gradient and random search, though different in mechanism, are quite similar in RL practice (shared stochastic exploration and cost-driven improvement), and hybrids exist.
- *3.6 (pp. 457–458).* Aggregation is sometimes called "state abstraction" in the RL literature. Options (macro-actions) are a formalization of temporal abstraction and can be seen as problem approximation. POMDP discretization is from Yu and Bertsekas. Biased aggregation is from [Ber18b]. That paper shows the bound of Prop. 3.6.1 holds with $J^*$ replaced by $J^*-V$. Distributed asynchronous aggregation is from Bertsekas and Yu. Compared with temporal difference methods, aggregation has stronger theoretical properties (Bellman operator monotonicity, resilience to policy oscillations, better error bounds) but is more restrictive in its use of linear architectures.

**Exercises (statements only).**
- *3.1* (p. 459): completes a proof of Prop. 3.4.1 (not in this unit). For fixed $c$, $z(c,c')$ is 1 with probability $p(c\mid x)$ and 0 otherwise. Then $E\{(z-y)^2\mid x\}=p(c|x)(y-1)^2+(1-p(c|x))y^2$ is minimized at $y^*=p(c\mid x)$. Setting $y=h(c,x)$ and summing with weights $\xi(x)$ gives Eq. (3.35) for all $h$ and $c$.
- *3.2* (pp. 459–461): two-state deterministic problem (L, R), costs L→R 2, R→L 2, L→L 1, R→R 0. From R, staying is optimal. From L, staying is optimal if $\alpha<1/2$ and moving is optimal if $\alpha>1/2$. (a) For the policy "move to R with probability $r$", compute $J_\alpha(r)$ from the Bellman equations, verify concavity and that $r=0$ and $r=1$ are local minima, and that policy gradient converges to either one if started close enough. (b) The soft-max parametrization $(r_1,r_2)$: compute $J_\alpha(r_1,r_2)$ and explain the observation. (c) With rewards instead of costs, the maximizer of $J_\alpha(r)$ is unique and strictly between 0 and 1, so policy gradient tends to produce a randomized policy.
- *3.3* (p. 462): two absorbing states with $g(1,1)=0$, $g(2,2)=1$, so $J^*(1)=0$, $J^*(2)=1/(1-\alpha)$. Aggregates $x_1,x_2$ disaggregate to states 1, 2 but aggregate states 2, 1 respectively, so (3.91) is violated, even though $\epsilon=0$. The task is to show the aggregation error is positive.

## Toy example (ours, not from the text)
Chain of 4 states, one control (no decisions), $\alpha=0.5$. Deterministic moves $1\to2\to3\to4\to4$. Costs: $g(1,2)=g(2,3)=g(3,4)=1$, $g(4,4)=0$.

*Exact costs:* $J^*(4)=0$; $J^*(3)=1$; $J^*(2)=1+0.5\cdot1=1.5$; $J^*(1)=1+0.5\cdot1.5=1.75$.

*Hard aggregation (general framework):* aggregate $x$ with $I_x=\{1,2\}$, $d_{x1}=d_{x2}=\tfrac12$; aggregate $y$ with $I_y=\{3,4\}$, $d_{y3}=d_{y4}=\tfrac12$; $\phi_{jx}=1$ for $j=1,2$ and $\phi_{jy}=1$ for $j=3,4$. Then $I_x=S_x$, $I_y=S_y$, so (3.91) holds. Per footprint, the variation is $|1.75-1.5|=0.25$ in $S_x$ and $|1-0|=1$ in $S_y$, so $\epsilon=1$ and the bound is $\epsilon/(1-\alpha)=2$.

*Aggregate equations* (3.84)–(3.86), with $\tilde J_1(j)=r$ of the aggregate containing $j$:
- $\tilde J_0(1)=1+0.5r_x$ (successor 2 is in $S_x$), $\tilde J_0(2)=1+0.5r_y$, $\tilde J_0(3)=1+0.5r_y$, $\tilde J_0(4)=0+0.5r_y$.
- $r_y=\tfrac12(1+0.5r_y)+\tfrac12(0.5r_y)=0.5+0.5r_y\Rightarrow r_y=1$.
- $r_x=\tfrac12(1+0.5r_x)+\tfrac12(1+0.5r_y)=1+0.25r_x+0.25\Rightarrow0.75r_x=1.25\Rightarrow r_x=5/3\approx1.667$.

*Result:* $\tilde J=(1.667,1.667,1,1)$ against $J^*=(1.75,1.5,1,0)$. Errors are $0.083,\,0.167,\,0,\,1$; the largest, $1$, is $\le2$.

*Biased version:* take $V=J^*=(1.75,1.5,1,0)$. Modified costs $g-V(i)+\alpha V(j)$ are $1-1.75+0.75=0$, $1-1.5+0.5=0$, $1-1+0=0$, $0-0+0=0$. So $\hat J\equiv0$ and $\tilde J=\hat J+V=J^*$ exactly. This shows that a good $V$ leaves little for aggregation to do.

## Concepts
- [[aggregation]] (new) — build a smaller DP problem on aggregate states, solve it exactly, and interpolate its costs into an approximation for the original problem (p. 430)
- [[aggregation-probabilities]] (new) — weights $\phi_{jy}\ge0$, $\sum_y\phi_{jy}=1$, relating an original state $j$ to aggregate states $y$ (p. 433)
- [[disaggregation-probabilities]] (new) — distribution $d_{xi}$ over original states, concentrated on $I_x$, used when leaving aggregate state $x$ (p. 440)
- [[footprint]] (new) — $S_y=\{j\mid\phi_{jy}>0\}$ (hard aggregation: $\{j\mid\phi_{jy}=1\}$); the states "related" to aggregate $y$ (pp. 435, 443)
- [[hard-aggregation]] (new) — each state has a single aggregate, giving disjoint footprints and a piecewise constant $\tilde J$ (p. 435)
- [[feature-based-aggregation]] (new) — footprints defined by partitioning a feature space; a nonlinear piecewise constant architecture (pp. 445–446)
- [[biased-aggregation]] (new) — aggregation applied to stage cost $g-V(i)+\alpha V(j)$; $\tilde J=\hat J+V$; the modified problem has the same optimal policies as the original (pp. 447–448)
- [[contraction-mapping]] (new) — operator with $\|Hr-Hr'\|\le\alpha\|r-r'\|$ in max norm; gives a unique fixed point (p. 443)
- [[mixture-of-experts]] (new) — several policies plus on-line change detection and gating to select among them (p. 429)
- [[knowledge-distillation]] (new) — train a small student policy to mimic a large teacher (p. 429)
- Bellman equation / value function — the aggregate problem satisfies (3.84)–(3.88); the unit's $\tilde J$ approximates $J^*$ (p. 441)
- policy — rule mapping states to controls; aggregate policy may serve as rollout base policy (p. 430)

## Canonical instances
- [[coarse-grid-approximation]] — representative states on a coarse grid with proximity-based $\phi_{jy}$ (p. 431)
- [[continuous-shortest-path-discretization]] — state-only grid discretization gives 2000 s versus $\sqrt2\cdot1000$ s (p. 438)
- [[pomdp-belief-discretization]] — representative beliefs and convex-combination weights give a finite aggregate problem (p. 439)
- [[two-state-policy-gradient-local-minima]] — $J_\alpha(r)$ with local minima at $r=0,1$ (pp. 460–461)
- [[aggregation-bound-counterexample]] — absorbing-state example violating (3.91) (p. 462)

## Bridges (candidates)
- [structural-analogy] Aggregation interpolation $\tilde J=\Phi r$ ↔ control-theory: linearization or gridding of a nonlinear value function — both replace a large problem by a small one and map back
- [same-math] Max-norm contraction of $H$ ↔ standard Bellman-operator contraction in discounted DP — the same argument ($\alpha$-discounting plus averaging by probabilities)
- [structural-analogy] Mixture of experts with gating ↔ control-theory: multiple-model adaptive control — switch among controllers when the plant changes
- [structural-analogy] Biased aggregation ($J^*=\hat J+V$) ↔ cost shaping with a potential: the stage-cost change telescopes along trajectories and keeps optimal policies (the text names "cost shaping" in a footnote)

## Questions this raises
- How should aggregate states be chosen when $J^*$ is unknown and no theory exists (p. 445)? Can learned features (neural networks) make footprints approximately "flat" in $J^*$?
- What exactly goes wrong when (3.91) fails, and can a weaker condition still give a bound (Exercise 3.3)?
- How does the quality of $V$ trade off with the aggregation architecture in biased aggregation when the modified problem is solved only approximately?
- How is the bound on the lookahead policy's performance, rather than on $\tilde J$, related to $\epsilon/(1-\alpha)$? (The unit bounds only $|J^*-\tilde J|$.)

## Exercises worth doing
- Ex. 3.1 (p. 459) — why the optimal predictor of a 0–1 indicator under squared error is the conditional probability — difficulty: easy
- Ex. 3.2(a) (p. 460) — computing $J_\alpha(r)$, seeing concavity and local minima of a policy-gradient objective — difficulty: medium
- Ex. 3.2(b) (p. 461) — how soft-max reparametrization changes the landscape (see Figs. 3.7.2–3.7.3) — difficulty: hard
- Ex. 3.2(c) (p. 461) — why maximization yields a randomized optimum — difficulty: medium
- Ex. 3.3 (p. 462) — why condition (3.91) is needed for the error bound — difficulty: medium

## Reading notes
- **Unit boundaries.** The unit starts on p. 429, in the middle of Section 3.5 (the retraining discussion; the first sentence refers to a dataset chosen earlier). It ends on p. 462, with Exercise 3.3, the last item on the last page given. It covers the end of 3.5, all of 3.6 (3.6.1–3.6.8), and 3.7 (notes and Exercises 3.1–3.3). Page offset: printed = pdf − 20.
- **OCR problems.** The text layer renders "−" as "→", "ε" as "+", "∪" as "∞", and "∈" as "→" in places (e.g., "$u\to U(x)$" on p. 432, "$J^*(i)\to J^*(j)$" on p. 436). The page images show the correct symbols. Equations were checked against the images.
- **Index order.** On p. 444 the text writes "$\phi_{ix}=1$ if $d_{xi}>0$", with $i$ and $x$ in the order of the framework's $\phi_{jy}$; I kept it as printed.
- **Exercise 3.2(b).** The printed sentence "Verify that $J_\alpha(r_1,r_2)$ has no local minima if started close enough to it" is awkwardly phrased in the source. I reported it as the author's request to inspect the landscape (Fig. 3.7.3).
- **Figures.** Figs. 3.7.2 and 3.7.3 are plots; I did not read numerical values from them.
- **Cross-references.** Several results are referenced to parts outside this unit (Prop. 3.4.1, Eq. (3.35), Examples 3.1.1/3.1.7, Section 3.5.2); nothing from them is used beyond what is printed here.
