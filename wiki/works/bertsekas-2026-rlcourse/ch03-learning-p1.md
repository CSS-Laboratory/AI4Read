---
id: bertsekas-2026-rlcourse/ch03-learning-p1
work: bertsekas-2026-rlcourse
unit: "3 Learning Values and Policies (part 1/5): chapter opening, 3.1 Parametric Approximation Architectures (up to Diagonal Scaling)"
pages: 349-371
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Parametric Approximation Architectures and Their Training (Sec. 3.1)

## L0 — One line
Off-line, a cost-to-go or policy is fitted from sampled data by a parametric architecture, often a linear weighting of features, trained by least squares or, for nonlinear architectures, by incremental gradient steps.

## L1 — The gist (≤ 120 words)
Approximation in value space needs a good lookahead function $\tilde J_k$. This section asks how to build one off-line from a parametric class $\tilde J(x,r)$ and sample data. The answer: choose an architecture, often a linear weighting of hand-made or learned features, and most commonly fit $r$ by least squares. For linear architectures the fit has a closed form. For nonlinear ones, such as neural networks, the problem is nonconvex, and incremental (stochastic) gradient methods are used. Incremental methods can be much faster far from the solution but need a diminishing stepsize to converge near it. Policy approximation is largely similar. With a finite control set it connects to classification.

**Prerequisites:** gradients and partial derivatives; least squares; matrix inverse; dynamic programming notation ($J_k^*$, cost-to-go, policy); the idea of one-step lookahead.

## L2 — Key ideas
- Fit a target cost $J(x)$ with $\tilde J(x,r)$ from training pairs $(x^s,J(x^s))$ by making the errors small (p. 351).
- Policy approximation $\tilde\mu(x,r)$ is largely similar. With a finite control set it connects to classification; classifiers often produce randomized policies, which an arg max (pick the control of highest probability) converts to a single control (p. 352).
- If features $\phi(x)$ encode much of the nonlinearity of $J^*$, a relatively simple architecture, often a linear one $r'\phi(x)$, may suffice (p. 354).
- Examples of feature-based architectures: piecewise constant, polynomial, radial basis, tetris and chess features, aggregation, state partitioning, local-global (pp. 355–363); several are linear in the features.
- Features can also be learned from data (kernels, i.e. data-dependent basis functions; neural networks). One option is to mix them with hand-made features in a linear architecture trained in a second stage (pp. 359, 364).
- Linear least squares has the closed form (3.7), with a regularization term if the matrix is not invertible. Nonlinear architectures such as neural networks give a nonquadratic, nonconvex training problem, for which incremental gradient algorithms have worked in practice (pp. 364–365).
- Incremental gradient (3.10) is much cheaper per step and can progress much faster far from the optimum, but it needs a diminishing stepsize and can be much slower near it (pp. 366–370).
- Stepsize choice (constant-then-decrease, diminishing, adaptive) plays an important role. Diagonal scaling (a separate stepsize per parameter component) is another remedy, though the text calls it inconvenient for least squares training (pp. 370–371).

## L3 — Walkthrough

### Chapter opening (pp. 349–351)
The chapter treats off-line training with parametric architectures such as neural networks. Section 3.1 covers architectures and training, 3.2 neural networks, 3.3 finite-horizon approximate DP, 3.4–3.5 policy training, 3.6 aggregation (p. 351).

### 3.1 Parametric approximation architectures (pp. 351–352)
For approximation in value space it is important to choose a class of lookahead functions $\tilde J_k$ that suits the problem. Earlier chapters used mostly rollout. Now $\tilde J_k$ comes from a parametric class with "optimized" parameters (p. 351).

- Setup (Fig. 3.1.1): target $J(x)$. Training data $(x^s,J(x^s))$, $s=1,\dots,q$. An optimization finds $\hat r$ that makes the errors $J(x^s)-\tilde J(x^s,\hat r)$ small (p. 351).
- Policy approximation by $\tilde\mu(x,r)$ is "largely similar". Training data may come from rollout, so value and policy networks can be combined in a perpetual rollout scheme (p. 351).
- Difference: $\tilde J$ values are real numbers, while $\tilde\mu$ values are controls in $U$. If $U$ consists of vectors, the two problems are fairly similar (continuous-space approximations) (p. 352).
- If $U=\{u^1,\dots,u^m\}$ is finite, $\tilde\mu(\cdot,r)$ is a classifier: it assigns each $x$ one of $m$ categories (p. 352).
- Many classifiers output a probability distribution
$$\{\tilde\mu^1(x,r),\dots,\tilde\mu^m(x,r)\}, \tag{3.1}$$
a randomized policy. This is done for convenience, since methods such as least squares regression need continuous variables. It is converted to a nonrandomized policy by
$$\tilde\mu(x,r)\in\arg\max_{i=1,\dots,m}\tilde\mu^i(x,r). \tag{3.2}$$
(Fig. 3.1.2, p. 352.) Section 3.4 returns to this.

**Intuition note.** A value approximator outputs a number. A policy approximator over finitely many controls outputs a choice among $m$ labels, so it is a classifier. Probabilities are often used for convenience, since many optimization methods, including least squares regression, need continuous variables.

### 3.1.1 Cost function approximation (pp. 352–353)
- Architecture: $\tilde J_k(x_k,r_k)$ with $r_k=(r_{1,k},\dots,r_{m_k,k})$ tunable scalars. Targets are typically $J_k^*$ or $J_{k,\pi}$. Choosing $r_k$ is training or tuning (p. 353).
- Simplest training: semi-exhaustive or semi-random search over parameters, judged by the performance of the resulting one-step lookahead controller. This is mainly practical when parameters are few (p. 353).
- Random search and Bayesian optimization have been used for hyperparameters, e.g. the number of layers or clusters (p. 353).
- More systematic training: numerical optimization, such as a least squares fit to a training set of sampled state–cost pairs. Sections 3.1–3.3 focus on this (p. 353).

### 3.1.2 Feature-based architectures (pp. 353–364)
**Features.** Feature extraction maps $x_k$ to a vector $\phi_k(x_k)$ with components $\phi_{1,k},\dots,\phi_{m_k,k}$ (the features). A feature-based approximation is $\tilde J_k(x_k,r_k)=\hat J_k(\phi_k(x_k),r_k)$, so it depends on $x_k$ only through $\phi_k(x_k)$ (p. 353).

- Features and parameters may differ by stage $k$. This is needed for nonstationary problems and to capture closeness to the horizon end. For stationary problems with long or infinite horizons, where the state space stays constant over $k$, it is common to use the same features and parameter vectors for all $k$ (p. 354).
- Features are often hand-designed, but can also be built from data and neural networks (p. 354).
- Rationale: $J_k^*$ can be complex and nonlinear. If features encode much of its nonlinearity, a relatively simple $\hat J_k$ may approximate it (p. 354). A well-chosen $\phi_k$ often makes linear weighting good:
$$\tilde J_k(x_k,r_k)=\hat J_k(\phi_k(x_k),r_k)=\sum_{\ell=1}^{m_k} r_{\ell,k}\,\phi_{\ell,k}(x_k)=r_k'\phi_k(x_k), \tag{3.3}$$
where $r_k'\phi_k$ is an inner product in $\Re^{m_k}$ (prime = transpose). This is a linear feature-based architecture, and the $r_{\ell,k}$ are weights. Such architectures admit simpler training algorithms than nonlinear ones (p. 354).
- $\tilde J_k$ lies in the subspace spanned by the features, so the features are also called basis functions (pp. 354–355).

**Intuition note.** Features do the nonlinear work of describing a state. If the features capture much of the nonlinearity, a plain weighted sum of them may then give a good value estimate (the text says this is often the case).

**Example 3.1.1 (piecewise constant).** Partition the state space into $S_1,\dots,S_m$. Let $\phi_\ell(x)=1$ if $x\in S_\ell$, else $0$. Then $\tilde J(x,r)=\sum_\ell r_\ell\phi_\ell(x)$ equals $r_\ell$ on $S_\ell$ (Fig. 3.1.4, p. 355). This is a linear architecture with exclusively local features: each is nonzero on few states, so one weight changes $\tilde J$ on few states. Global features are nonzero on many states (p. 356).

**Example 3.1.2 (polynomial).** State $x=(x^1,\dots,x^n)$ (e.g. queue lengths). A quadratic architecture uses $1+n+n^2$ basis functions $\phi_0=1$, $\phi_i=x^i$, $\phi_{ij}=x^ix^j$, so
$$\tilde J(x,r)=r_0+\sum_{i=1}^n r_ix^i+\sum_{i=1}^n\sum_{j=1}^n r_{ij}x^ix^j .$$
More generally, start from features $\phi(x)=(\phi_1,\dots,\phi_m)'$ and use $\tilde J(x,r)=r_0+\sum_i r_i\phi_i+\sum_{i,j}r_{ij}\phi_i\phi_j$. This is linear in the basis $w_0=1$, $w_i=\phi_i$, $w_{ij}=\phi_i\phi_j$ (p. 356).

**Example 3.1.3 (Tetris).** Formulated earlier (Ex. 1.6.2) as a stochastic shortest path problem. State: board position $x$ and current block shape $y$. There are $2^{200}$ board positions on a standard $10\times20$ board. Features proposed by Bertsekas and Ioffe [BeI96]: column heights, height differences of adjacent columns, wall height (maximum column height), number of holes, and the constant 1 (allows a constant shift). A standard board has 22 features. The $2^{200}\times22$ feature matrix cannot be stored, but one row can be generated for any board, which is sufficient for implementing the associated approximate DP algorithms (p. 358). Footnote: Tsitsiklis and Van Roy [TsV96] first suggested feature-based approximate DP for tetris, with the constant plus two features, wall height and holes (p. 357). Shapes are assumed independent in the cited works. With correlated shapes, state estimation and extra features may be needed (p. 358).

**Example 3.1.4 (computer chess).** Programs use approximate DP for minimax problems, a feature-based architecture, and multistep lookahead. Shannon [Sha50] proposed multistep lookahead with a "scoring function" of recognizable features (material balance, mobility, pawn structure, …); this plays the role of a cost approximation (p. 358). Weights are usually linear (3.3). Often they were set manually by trial and error. In some programs they were set by supervised learning from grandmaster play (pp. 358–359). AlphaZero (Silver et al. [SHS17]) abandoned human-designed features and discovers features by self-play and neural networks. It is based on approximate policy iteration and multistep lookahead with Monte Carlo tree search (p. 359).

**Example 3.1.5 (features from data).** Given anchor states $x(\ell)$, $\ell=1,\dots,m$, define Gaussian radial basis functions
$$\phi_\ell(x)=e^{-\frac{\|x-x(\ell)\|^2}{2\sigma^2}},\qquad \ell=1,\dots,m, \tag{3.4}$$
with scalar $\sigma$ and Euclidean norm. Each is concentrated around $x(\ell)$ and weighted by $r_\ell$, giving a trainable linear architecture. Other data-dependent bases (support vector machines) are called kernels. The set of basis functions may also grow as data arrive, since quality may increase with more of them. This underlies kernel (nonparametric) methods. The author does not pursue them and focuses on parametric architectures with a given feature vector (pp. 359–360).

**Example 3.1.6 (features from sufficient statistics).** Under partial information, the information vector is $I_k=(z_0,\dots,z_k,u_0,\dots,u_{k-1})$ and $u_k$ may depend only on $I_k$. $S_k(I_k)$ is a sufficient statistic if $\mu_k^*(I_k)=\hat\mu_k(S_k(I_k))$ for some $\hat\mu_k$, with $\mu_k^*$ optimal. Examples: $I_k$ itself, or the belief state $b_k$, the conditional distribution of $x_k$ given $I_k$ (p. 360). Features of it may be an alarm-like event, a partial history (last few measurements and controls, or a finite-state controller), or, for $b_k$, a point estimate and its variance (pp. 360–361). Bhattacharya et al. [BBW20] use a statistic $y_k$ from which $b_k$ can be computed exactly. It has the same information as $b_k$ for exact optimization, but a $y_k$ designed for the problem may perform better under cost and policy approximations. A statistic may also be enriched with features of other sufficient statistics, which in problem-specific contexts, and in the presence of approximations, may yield improved results (p. 361).

**Example 3.1.7 (dimensionality reduction by aggregation).** If $\phi$ takes finitely many values, define aggregate states $S_v=\{x\mid\phi(x)=v\}$. They partition the state space, and $\tilde J(\phi(x),r)$ is piecewise constant on this partition. In an aggregate DP problem whose states are feature values, if it can be solved exactly with optimal cost-to-go $\hat J(v)$, then $\hat J(\phi(x))$ is an architecture for the original problem (pp. 361–362). Details are in Section 3.6.

**Example 3.1.8 (feature-based state partitioning).** Partition the state space and fit a separate approximation (linear, quadratic, or neural) on each subset. Regular grid partitions may give very many subsets. Alternatively, partition the feature space regularly, which induces a possibly irregular partition of the states with "similar features" (Fig. 3.1.7). Chess is the illustration: opening, middlegame and endgame types call for different strategies, and some programs partition this way (pp. 362–363). Discontinuities at boundaries can be smoothed by soft partitioning: subsets overlap and the overlap uses a smoothly varying linear combination of the subset approximations (p. 363).

**Example 3.1.9 (local-global).** With a partition $S_1,\dots,S_M$,
$$\tilde J(x,r)=\hat J(x,\hat r)+\sum_{m=1}^M\sum_{k=1}^{K_m}r_m(k)\phi_{k,m}(x), \tag{3.5}$$
where each $\phi_{k,m}$ is local (zero for $x\notin S_m$). The part $\hat J(x,\hat r)$ captures global aspects and each inner sum captures aspects local to $S_m$. Specialized training algorithms may help ([BeT96], Sec. 3.1.3) (p. 363).

**Automatic feature construction (pp. 363–364).** Identifying features is hard, so kernel methods and neural networks (Sec. 3.2) construct them. Some architectures train features $\phi(x)$ and weights $r$ simultaneously. Such architectures can still take hand-crafted features as extra inputs. Alternatively, a second-stage linear architecture can combine learned and known features, with weights from a separate training step after the nonlinear first stage (p. 364).

### 3.1.3 Training of linear and nonlinear architectures (pp. 364–371)
**Least squares training.** With training set $(x^s,\beta^s)$, $s=1,\dots,q$ (sample cost $\beta^s$ is $J(x^s)$ plus perhaps noise), solve
$$\min_r\sum_{s=1}^q\big(\tilde J(x^s,r)-\beta^s\big)^2. \tag{3.6}$$
In general this is nonconvex and may have multiple local minima. For a linear architecture $\tilde J(x,r)=r'\phi(x)$ it is a convex quadratic with a closed-form solution (p. 364).

Derivation (added step on shapes: $\phi(x^s)\in\Re^{m}$, $r\in\Re^{m}$, $\sum_s\phi\phi'$ is $m\times m$):
- Problem: $\min_r\sum_{s=1}^q\big(r'\phi(x^s)-\beta^s\big)^2$.
- Setting the gradient to 0 gives $\sum_s\phi(x^s)\big(r'\phi(x^s)-\beta^s\big)=0$ (added step: the exact gradient is 2 times this expression; the factor 2 is irrelevant when setting it to 0).
- Equivalently $\sum_s\phi(x^s)\phi(x^s)'\,r=\sum_s\phi(x^s)\beta^s$.
- Matrix inversion gives
$$\hat r=\Big(\sum_{s=1}^q\phi(x^s)\phi(x^s)'\Big)^{-1}\sum_{s=1}^q\phi(x^s)\beta^s. \tag{3.7}$$
(p. 365)

If the inverse does not exist, a quadratic regularization term in $r$ is added to the objective, or singular value decomposition is used. Iterative linear least squares algorithms also work. For nonlinear architectures (e.g. neural networks) the problem is nonquadratic and nonconvex, hard in principle. Yet incremental gradient algorithms with large computing resources have succeeded in practice (p. 365).

**Intuition note.** With a linear architecture, least squares is a bowl-shaped (convex quadratic) problem solved by linear equations; the answer is unique when the matrix is invertible, otherwise regularization is added. A nonlinear architecture can have many local minima, so one walks downhill by gradients.

**Incremental gradient methods (pp. 365–367).** The author notes this is generic nonlinear programming and may be skipped by readers who know it (p. 365). View (3.6) as minimizing a sum of components
$$f(y)=\sum_{i=1}^m f_i(y), \tag{3.8}$$
with $y$ the $n$-dimensional parameter vector and each $f_i$ differentiable scalar (here $f_i=(\tilde J(x^s,r)-\beta^s)^2$). The ordinary gradient method is
$$y^{k+1}=y^k-\gamma^k\nabla f(y^k)=y^k-\gamma^k\sum_{i=1}^m\nabla f_i(y^k), \tag{3.9}$$
with positive stepsize $\gamma^k$. The incremental gradient method uses one component per iteration:
$$y^{k+1}=y^k-\gamma^k\nabla f_{i_k}(y^k), \tag{3.10}$$
with $i_k\in\{1,\dots,m\}$ chosen by a deterministic or randomized rule. It saves much gradient computation, especially for large $m$, and "performs surprisingly well" despite large approximation error. The aim is faster convergence far from the solution (p. 366).

Index rules (pp. 366–367):
1. Cyclic order $1,\dots,m$, so $i_k=(k \bmod m)+1$. A contiguous block of iterations using $f_1,\dots,f_m$ in this order, each exactly once, is a cycle.
2. Uniform random order, independent of the past. It may perform better than cyclic in some circumstances.
3. Cyclic with random reshuffling after each cycle. Widely used, particularly when $m$ is modest.

In the cyclic cases all components must be included in each cycle, and in the random case the sampling must be uniform. Otherwise some components are sampled more, causing bias. A footnote (attached to the remark that the last two rules involve randomization) says that with these rules the method is often called stochastic gradient or stochastic gradient descent (p. 366).

Two complementary performance issues (p. 367):
- (a) Far from convergence, the incremental method can be much faster. Extreme case: $m$ large and all $f_i$ identical. An incremental iteration costs $m$ times less but gives exactly the same result when its stepsize is $m$ times larger. A single component gradient points "more or less" in the right direction, at least most of the time.
- (b) Near convergence, it can be inferior. The ordinary method converges with a constant stepsize under reasonable assumptions. The incremental method needs a diminishing stepsize, and its ultimate convergence rate can be much slower.

**Example 3.1.10 (pp. 368–369).** Scalar $y$, $f(y)=\tfrac12\sum_{i=1}^m(c_iy-b_i)^2$, $c_i\neq0$.
- Component minima: $y_i^*=b_i/c_i$. Overall minimum: $y^*=\dfrac{\sum_i c_ib_i}{\sum_i c_i^2}$.
- $y^*$ lies in $R=[\min_iy_i^*,\max_iy_i^*]$. For $y$ outside $R$, $\nabla f_i(y)=c_i(c_iy-b_i)$ has the same sign as $\nabla f(y)$.
- Hence outside $R$, the incremental iteration $y^{k+1}=y^k-\gamma^kc_{i_k}(c_{i_k}y^k-b_{i_k})$ approaches $y^*$ at each step if $\gamma^k$ is small enough. It suffices that $\gamma^k\le\min_i 1/c_i^2$.
- Inside $R$, the $i$th step need not make progress. It approaches $y^*$ (for small stepsize) only if $y^k$ is not in the interval joining $y_i^*$ and $y^*$. This gives oscillation inside $R$ ("region of confusion", Fig. 3.1.8), so the method typically does not converge to $y^*$ unless $\gamma^k\to0$.
- The ordinary method $y^{k+1}=y^k-\gamma\sum_ic_i(c_iy^k-b_i)$ converges for any constant $\gamma$ with $0<\gamma\le 1/\sum_ic_i^2$. Outside $R$, a full ordinary iteration need not progress more than one incremental step. With comparably intelligent stepsizes, far from the solution one incremental pass is roughly as effective as $m$ ordinary passes.

**Example 3.1.11 (p. 370).** $f_i(y)=a_ie^{b_iy}$, $a_i>0$, $b_i\ne0$. Let $I^+=\{i\mid b_i>0\}$ and $I^-=\{i\mid b_i<0\}$, with roughly equal sizes. Here $y^*$ is the minimum of $\sum f_i$. Iteration: $y^{k+1}=y^k-\alpha^k\nabla f_{i_k}(y^k)$. If $y^k\gg y^*$, the step is substantially closer to $y^*$ for $i\in I^+$ and negligibly further away for $i\in I^-$. On average an incremental iteration makes roughly half the progress of a full gradient iteration, with $m$ times less gradient overhead. The same holds for $y^k\ll y^*$. Nearer $y^*$ the advantage shrinks. Convergence requires a diminishing stepsize, which ultimately makes it slower than the nonincremental method with constant stepsize.

In several dimensions, the same qualitative behavior can be seen. A component step makes progress where $\nabla f_{i_k}(y^k)$ makes an angle under 90° with $\nabla f(y^k)$. If components are not "too dissimilar", this is likely far from the optimal set. This has been validated in practice, including neural network training, where incremental gradient methods are often called backpropagation methods (p. 370).

**Intuition note.** Far from the minimum, a single term's gradient points more or less the right way, at least most of the time, so using one term at a time wastes little. Near the minimum, the terms may disagree, so single-term steps typically keep bouncing unless the steps shrink.

**Stepsize choice (pp. 370–371).** The stepsize $\gamma^k$ is the learning rate. Practice: keep a constant stepsize for a (possibly prespecified) number of iterations, cut it by a factor, repeat until a prespecified floor. Alternative diminishing rule
$$\gamma^k=\min\Big\{\gamma,\ \frac{\beta_1}{k+\beta_2}\Big\},$$
with positive scalars $\gamma,\beta_1,\beta_2$. Constant-stepsize variants exist that converge to a stationary point of $f$ under reasonable assumptions. In one, the degree of incrementalism gradually diminishes [Ber97a]. The aggregated gradient method has similar aims. The incremental method must use a much larger stepsize than the nonincremental one (as much as $m$ times larger). Adaptive rules reduce or increase the stepsize when progress indicates oscillation or not, with sound convergence properties proposed by Tseng [Tse98] and Moriyama et al. [MYF03] (p. 371).

**Diagonal scaling (p. 371, start).** Use a different stepsize per component $y_j$. The classical choice is $\gamma_j^k=\gamma\big(\partial^2f(y^k)/\partial^2y_j\big)^{-1}$, with $\gamma$ nearly 1 (second derivatives may be approximated by differences). For least squares training, the author says this is inconvenient because $f$ is a sum of many components (3.8). The part ends here.

## Toy example (ours, not from the text)
**Closed-form fit (3.7).** Piecewise constant architecture with $S_1=\{1,2\}$, $S_2=\{3\}$. Then $\phi(1)=\phi(2)=(1,0)'$ and $\phi(3)=(0,1)'$. Data: $(x^s,\beta^s)=(1,4),(2,6),(3,10)$.
- $\sum_s\phi\phi'=\begin{pmatrix}2&0\\0&1\end{pmatrix}$, because two states have $\phi=(1,0)'$ and one has $(0,1)'$.
- $\sum_s\phi\beta^s=(4+6,\,10)'=(10,10)'$.
- $\hat r=\begin{pmatrix}1/2&0\\0&1\end{pmatrix}(10,10)'=(5,10)'$, the average cost in each set.

**Incremental vs. ordinary gradient (as in Ex. 3.1.10).** Take $m=2$, $c_1=c_2=1$, $b=(1,3)$. Then $y^*=(1+3)/2=2$, and $R=[1,3]$. Use $\gamma=0.5$ ($\le\min 1/c_i^2=1$).
- Far away: start $y^0=10$. Component 1: $10-0.5(10-1)=5.5$. Component 2: $5.5-0.5(5.5-3)=4.25$. The point moves toward 2.
- Inside $R$: start exactly at $y^*=2$. Component 1: $2-0.5(2-1)=1.5$. Component 2: $1.5-0.5(1.5-3)=2.25$. The cycle ends at $2.25\ne2$, so a constant stepsize keeps it oscillating.
- Ordinary gradient at $y=2$: the total gradient is $(2-1)+(2-3)=0$, so it stays at $y^*$.

## Concepts
- [[parametric-approximation-architecture]] (new) — a class $\tilde J(x,r)$ or $\tilde\mu(x,r)$ with tunable parameters $r$, fitted to a target; training or tuning picks $r$ (p. 353)
- [[feature-based-architecture]] (new) — $\tilde J$ depends on $x$ only through a feature vector $\phi(x)$; linear case $r'\phi(x)$ (pp. 353–354)
- [[policy]] — here approximated by $\tilde\mu(x,r)$; with finite controls it acts as a classifier (p. 352)
- [[least-squares-training]] (new) — choose $r$ to minimize the sum of squared errors between sample costs and predictions; closed form (3.7) if linear (pp. 364–365)
- [[incremental-gradient-method]] (new) — gradient step on one component $f_{i_k}$ at a time, as in (3.10); often called stochastic gradient with the randomized index rules (footnote, p. 366)
- [[sufficient-statistic]] (new) — a function $S_k(I_k)$ through which the optimal control depends on the information vector (p. 360)
- [[stepsize-learning-rate]] (new) — the scalar $\gamma^k$ in gradient iterations; constant, diminishing, adaptive rules (pp. 370–371)
- [[state]] — in this unit, board position (tetris, chess), queue lengths, or information-vector summaries; features give a compact description (pp. 356–361)

## Canonical instances
- [[piecewise-constant-approximation]] — local-feature linear architecture, one weight per partition set (p. 355)
- [[polynomial-basis-approximation]] — global quadratic features, $1+n+n^2$ basis functions (p. 356)
- [[tetris-features]] — 22 features give a low-dimensional linear approximation of $J^*$ on $2^{200}$ boards (pp. 357–358)
- [[computer-chess-scoring-function]] — Shannon's feature scoring function; AlphaZero learns features instead (pp. 358–359)
- [[radial-basis-functions]] — Gaussian features around anchor states, as in (3.4) (p. 359)
- [[incremental-gradient-region-of-confusion]] — scalar least squares example showing fast far-field progress, oscillation inside $R$ (pp. 368–369)

## Bridges (candidates)
- [same-math] Linear least squares fit (3.7) ↔ statistics: ordinary least squares normal equations $\sum\phi\phi'\,r=\sum\phi\beta$.
- [same-math] Incremental gradient (3.10) ↔ machine learning: stochastic gradient descent with random index choice (the text itself makes this link, p. 366).
- [structural-analogy] Sufficient statistic for control (Ex. 3.1.6) ↔ statistics: sufficient statistic in inference; the text says the concept originated there (p. 360).
- [structural-analogy] Feature-space partitioning (Ex. 3.1.7–3.1.8) ↔ clustering: grouping states by similar features, like clusters in a feature space.

## Questions this raises
- When do the features fail to encode enough of the nonlinearity of $J^*$, and how does the approximation error then affect the quality of the lookahead policy?
- How should $\gamma$, $\beta_1$, $\beta_2$ be chosen in practice, and how does the best choice depend on $m$ and on the similarity of the components $f_i$?
- How do neural networks (Sec. 3.2) construct features automatically, and how does training them differ from linear least squares?
- How is a sample cost $\beta^s$ actually produced in DP, and what noise does it carry?

## Reading notes
- This is part 1 of 5 of Chapter 3. It starts at the chapter opening (printed p. 349, the chapter contents pages 349–350 included) and ends in the middle of Sec. 3.1.3 at the start of the "Diagonal Scaling" subsection (printed p. 371). Section 3.2 and later are not covered. The split is at a section boundary according to the source notes, but the text on p. 371 stops mid-subsection.
- Page offset: printed = pdf − 20.
- No exercises appear in this part.
- The text layer is garbled in places ("→" for minus signs, "&" for $\Re$, "2200" for $2^{200}$ on pp. 357–358). The page images confirm $2^{200}$.
- Fig. 3.1.8 (p. 369): the axis labels show "$c_i/b_i$" and the curve label uses $x$, while the text defines $y_i^*=b_i/c_i$ and uses $y$. Note that $c_i/b_i$ is the reciprocal of $y_i^*=b_i/c_i$; I read this as a labelling slip in the figure.
- Example 3.1.11 uses $\alpha^k$ for the stepsize, while the rest of the section uses $\gamma^k$.
- The footnote on p. 366 says "With these stepsize rules"; context suggests it refers to the index-selection rules (2) and (3).
- The text's feature count for tetris is 22 as printed. The breakdown of components of the count is not given in the pages, so I give none.
- The "Architectures with Automatic Feature Construction" heading on p. 363 is unnumbered in the source.
