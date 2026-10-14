---
id: murphy-2023-pml2/ch06-optimization-p3
work: murphy-2023-pml2
unit: "6 Optimization (part 3/3): §6.7.7, §6.8 Optimal transport, §6.9 Submodular optimization"
pages: 314–342
fields: [bayesian]
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
# Optimal transport and submodular optimization (end of Chapter 6)

## L0 — One line
Optimal transport compares distributions by the cheapest way to move mass from one to the other, and submodular (diminishing-returns) set functions can be minimized exactly in polynomial time, while monotone ones (polymatroid functions) can be maximized approximately by greedy search under a cardinality constraint.

## L1 — The gist (≤ 120 words)
This part ends the optimization chapter with two topics. Optimal transport (Cuturi) generalizes optimal matching to the Kantorovich and Monge problems and to Wasserstein distances. It covers duality, Brenier's theorem, closed forms for 1-D and Gaussian cases, and the entropic regularization solved by Sinkhorn iterations. Submodular optimization (Bilmes) studies set functions with diminishing returns. It covers examples, greedy maximization with a 1−1/e guarantee, constraints, polynomial-time minimization, and uses in summarization, clustering, active learning, probabilistic models and structured norms. A short note on LLMs for derivative-free optimization opens the part.

**Prerequisites:** linear programming and duality; convex functions and gradients; matrices and traces; probability measures, cdf and quantile function; set notation and power sets; KL divergence.

## L2 — Key ideas (5–10 bullets)
- Optimal matching (a permutation) cannot split mass or handle unequal sizes. The Kantorovich problem fixes this with a coupling matrix $P$ (a table of how much mass goes from each source point to each target point) with given row and column sums, and it stays a linear program in the continuous case (p. 316, p. 317).
- The Monge problem seeks a transport map $T$ with $T_\sharp\mu=\nu$ (the map pushes the distribution $\mu$ forward onto $\nu$). It is non-convex, which is why Kantorovich's relaxation is preferred (p. 317).
- Duality with $c$-transforms (which remove one dual variable) gives $W_1$ (the Wasserstein distance for cost $d$) as a supremum over 1-Lipschitz functions (functions that change by at most the distance between points) and, for squared Euclidean cost, shows the optimal map is the gradient of a convex function (Brenier) (p. 318–p. 320).
- Closed forms exist: 1-D via quantile functions (for suitable costs), and Gaussians via the Bures metric (a distance between covariance matrices) with an affine optimal map (when the first covariance is invertible) (p. 320, p. 321).
- Exact LP solving is cubic and suffers from a curse of dimensionality in sample complexity. Entropic regularization gives a strongly convex problem solved by Sinkhorn updates (alternating updates of the two dual vectors), at the price of slower convergence as $\gamma$ shrinks (p. 321, p. 322).
- A submodular function has diminishing returns, $f(X)+f(Y)\ge f(X\cup Y)+f(X\cap Y)$. Many useful functions are built from concave-of-modular pieces (p. 325–p. 329).
- Greedy gives a $1-1/e$ approximation for cardinality-constrained maximization of polymatroid functions (monotone submodular functions with $f(\emptyset)=0$). Submodular minimization is polynomial-time, unlike maximization (p. 330, p. 331, p. 333).
- Submodularity serves as a diversity or information model in summarization, clustering, active learning, log-submodular models (distributions whose log-probability is submodular) and structured norms (p. 334–p. 342).

## L3 — Walkthrough

### 6.7.7 LLMs for DFO (p. 314)
- LLMs are used to help optimize black-box functions written in a domain-specific language (e.g. symbolic expressions) or as Python code (p. 314).
- Zero-shot: give $(x,y)$ pairs and prompt the LLM to generate $f$. In-context learning (the author's term for the iterated version): feed incorrect predictions back and ask for an improved output (p. 314).
- An LLM can also act as the mutation operator in an evolutionary search, as in FunSearch (p. 314).
- Figure 6.17 shows CMA-ES on a 2-D function: a population (dots) and a dashed ellipse for the multivariate Gaussian, over generations 1–6 (p. 314).

### 6.8 Optimal transport (Marco Cuturi) (p. 314)
Optimal transport (OT) is a set of tools, starting with [Mon81], for comparing two probability distributions. The section starts from matchings and extends them (p. 314).

#### 6.8.1 Warm-up: matching two families of points (p. 314–p. 315)
- Two families $(x_1..x_n)$, $(y_1..y_n)$ of $n>1$ distinct points. A matching is a bijection, encoded by a permutation $\sigma\in\mathcal S_n$: $x_i\mapsto y_{\sigma_i}$ (p. 314).
- A cost $C_{ij}=c(x_i,y_j)$ comes from a cost function $c:\mathcal X\times\mathcal X\to\mathbb R$. Examples: taxi driver $i$ to user $j$; job-seeker skills to job requirements. Often $c$ is a distance (p. 315).
- Optimal matching (printed with index $\sigma_j$; (p. 315)):
$$\min_\sigma E(\sigma)=\sum_{i=1}^n c(x_i,y_{\sigma_j}).\tag{6.191}$$
- Naive enumeration needs $n!$ evaluations. The Hungarian algorithm solves it in polynomial time, $O(n^3)$ in the worst case (p. 315).

#### 6.8.2 From matchings to Kantorovich and Monge (p. 316–p. 317)
Two limits of matching: the two families may differ in size, and one may want to match continuous densities (p. 316).

**6.8.2.1 Mass splitting (p. 316).**
- Permutations are one-to-one, so tasks and workers cannot be partly assigned. Kantorovich allows splitting.
- Worker $i$ is a weighted Dirac $a_i\delta_{x_i}$ with time $a_i>0$. Task $j$ is $b_j\delta_{y_j}$ with time needed $b_j>0$ ($n\ne m$ allowed). Assume balance, $\sum_i a_i=\sum_j b_j$.
- Shapes: $P\in\mathbb R_+^{n\times m}$, $a\in\mathbb R^n$, $b\in\mathbb R^m$, $C\in\mathbb R^{n\times m}$. As printed:
$$\mathrm{OT}_C(a,b)\triangleq\min_{P\in\mathbb R_+^{n\times m},\,P\mathbf 1_n=a,\,P^T\mathbf 1_m=b}\langle P,C\rangle\triangleq\sum_{i,j}P_{ij}C_{ij}.\tag{6.192}$$
- $P_{ij}$ is the time worker $i$ spends on task $j$. Row $i$ sums to $a_i$ and column $j$ sums to $b_j$ (p. 316).

**6.8.2.2 Monge formulation (p. 316–p. 317).**
- Mass splitting loses the unique partner $y_j$ for each $x_i$. This is recovered in the density limit, loosely on the condition that $\mu$ has a density (p. 316).
- A push-forward map $T$ satisfies $\mu(T^{-1}(A))=\nu(A)$ for all measurable $A$. If $T$ is differentiable and $\mu,\nu$ have densities $p,q$ w.r.t. Lebesgue measure on $\mathbb R^d$, this is equivalent, by the change-of-variables formula and almost everywhere, to
$$q(T(x))=p(x)\,|J_T(x)|,\tag{6.193}$$
with $|J_T(x)|$ the Jacobian determinant (p. 317).
- Writing $T_\sharp\mu=\nu$, the Monge problem is
$$\inf_{T:T_\sharp\mu=\nu}\int_{\mathcal X}c(x,T(x))\,\mu(dx).\tag{6.194}$$
- It is non-convex: the constraint set $\{T_\sharp\mu=\nu\}$ is not convex, since two valid maps can have an average $(\tfrac12T+\tfrac12T')_\sharp\mu\ne\nu$. Kantorovich's approach also works for continuous measures and gives a much simpler linear program (p. 317).

**6.8.2.3 Kantorovich, continuous (p. 317).**
$$\Pi(\mu,\nu)\triangleq\{\pi\in\mathcal P(\mathcal X^2):\forall A\subset\mathcal X,\ \pi(A\times\mathcal X)=\mu(A),\ \pi(\mathcal X\times A)=\nu(A)\}\tag{6.195}$$
$$\mathrm{OT}_c(\mu,\nu)\triangleq\inf_{\pi\in\Pi(\mu,\nu)}\int_{\mathcal X^2}c\,d\pi\tag{6.196}$$
$\Pi(\mu,\nu)$ is never empty because it contains the product measure $\mu\otimes\nu$. (6.196) coincides with (6.192) for discrete measures (p. 317).

**6.8.2.4 Wasserstein distances (p. 317).** If $c$ is a metric $d$ raised to an integer power $p$, the optimum is
$$W_p(\mu,\nu)\triangleq\Big(\inf_{\pi\in\Pi(\mu,\nu)}\int_{\mathcal X^2}d(x,y)^p\,d\pi(x,y)\Big)^{1/p}.\tag{6.197}$$
Symmetry and $W_p=0\Rightarrow\mu=\nu$ are relatively easy when $d$ is a metric. The triangle inequality is harder and uses the gluing lemma (p. 317).

> **Intuition note.** Matching is the special case where every point carries equal mass and no splitting is allowed. Letting mass split replaces a search over permutations with a linear program over couplings. The distance $W_p$ is then the $1/p$ power of the cost of the cheapest coupling (for cost $d^p$).

#### 6.8.3 Solving optimal transport (p. 318–p. 322)

**6.8.3.1 Duality and cost concavity (p. 318).**
- Both (6.192) and (6.196) are linear programs. With $\oplus$ the tensor sum, $f\oplus g=[f_i+g_j]_{ij}$, or $f(x)+g(y)$ for functions, the duals are
$$\max_{f\in\mathbb R^n,g\in\mathbb R^m,\ f\oplus g\le C}f^Ta+g^Tb\tag{6.198}$$
$$\sup_{f\oplus g\le c}\int f\,d\mu+\int g\,d\nu\tag{6.199}$$
- Given $f$, the best $g$ must satisfy $g(y)\le c(x,y)-f(x)$ for all $x,y$. This gives the $c$-transform
$$\forall y,\ \overline f(y)\triangleq\inf_x c(x,y)-f(x),\tag{6.200}$$
and, starting from $g$, the other transform
$$\forall x,\ \widetilde g(x)\triangleq\inf_y c(x,y)-g(y).\tag{6.201}$$
- Applying the transforms alternately gains nothing further:
$$\overline{\widetilde{\overline f}}=\overline f.\tag{6.202}$$
- The $c$-concave functions are $\mathcal F_c\triangleq\{f\mid\exists g,\ f=\widetilde g\}$, equivalently those with $f=\widetilde{\overline f}$. The semi-dual is
$$\sup_{f\in\mathcal F_c}\int f\,d\mu+\int\overline f\,d\nu.\tag{6.203}$$
- Cost of the reformulation: one dual variable is removed and the feasible set is narrowed, but the highly non-linear transform $\overline f$ enters. It is useful for distance costs and squared-Euclidean costs (p. 318).

**6.8.3.2 Kantorovich–Rubinstein duality (p. 319).**
- When $c=d$ (so $p=1$), a $d$-concave $f$ is 1-Lipschitz and $\overline f=-f$ (using the triangle inequality). Hence
$$W_1(\mu,\nu)=\sup_{f\ 1\text{-Lipschitz}}\int_{\mathcal X}f\,(d\mu-d\nu).\tag{6.204}$$
- The supremum can be approximated with wavelet coefficients in low dimension, or heuristically by training neural networks constrained to be 1-Lipschitz (ReLU activations, bounded weight-matrix entries) (p. 319).

**6.8.3.3 Brenier theorem (p. 319–p. 320).**
- For $c(x,y)=\tfrac12\|x-y\|^2$ (up to the factor $\tfrac12$, the squared $W_2$), assume $\mu$ has a density. Then the Monge map
$$T^\star=\arg\min_{T:T_\sharp\mu=\nu}\int\tfrac12\|x-T(x)\|_2^2\,\mu(dx)\tag{6.205}$$
exists and is the gradient of a convex function $u$: $T^\star=\nabla u$. Conversely, for any convex $u$, the optimal map between $\mu$ and $\nabla u_\sharp\mu$ is $\nabla u$ (p. 319).
- **Proof sketch (author's).** Take an optimal coupling $P^\star$ and an optimal $c$-concave $f^\star$, so $(f^\star,\overline{f^\star})$ is optimal for (6.199). Complementary slackness: if $(x_0,y_0)\in\operatorname{supp}P^\star$, then $f^\star(x_0)+\overline{f^\star}(y_0)=c(x_0,y_0)$ (necessary and sufficient). So $\overline{f^\star}(y_0)=c(x_0,y_0)-f^\star(x_0)$. By definition $\overline{f^\star}(y_0)=\inf_x c(x,y_0)-f^\star(x)$, so $x_0$ minimizes that function. With the squared cost (p. 319):
$$x_0\in\arg\min_x\tfrac12\|x-y_0\|^2-f^\star(x).\tag{6.206}$$
- $f^\star$ is differentiable (provable by $c$-concavity). The first-order condition is $x_0-y_0-\nabla f^\star(x_0)=0$ (added step; the page prints $y_0-x_0-\nabla f^\star(x_0)=0$, a sign slip). Hence
$$y_0=x_0-\nabla f^\star(x_0)=\nabla\big(\tfrac12\|\cdot\|^2-f^\star\big)(x_0).\tag{6.207}$$
- So $y_0$ is uniquely determined by $x_0$, and $P^\star$ is a Monge map "disguised" as a coupling:
$$P^\star=\big(\mathrm{Id},\nabla(\tfrac12\|\cdot\|^2-f^\star)\big)_\sharp\mu.\tag{6.208}$$
- End of proof: using the $c$-transform and the Legendre transform, $\tfrac12\|\cdot\|^2-h$ is convex if and only if $h$ is $c$-concave. So $\tfrac12\|\cdot\|^2-f^\star$ is convex and the optimal map is the gradient of a convex function (p. 320).
- Use: restrict the search in (6.203) to gradients of input-convex neural networks, or to convex functions with chosen smoothness and strong-convexity constants (p. 320).

> **Intuition note.** For squared-distance cost, the optimal map is the gradient of a convex potential. So the search for the map can be restricted to gradients of convex functions, for example input-convex neural networks.

**6.8.3.4 Closed forms (p. 320–p. 321).**
- *Univariate.* If the cost is a convex function of $x-y$, or $\partial c/\partial x\partial y<0$ a.e., then with quantile functions $Q_\rho$ (generalized inverse of the cdf $F_\rho$):
$$\mathrm{OT}_c(\mu,\nu)=\int_{[0,1]}c\big(Q_\mu(u),Q_\nu(u)\big)\,du.\tag{6.209}$$
For $c=|x-y|$ this is the Kolmogorov–Smirnov statistic (area between the cdfs, as the author says). For $c=(x-y)^2$ it is the squared Euclidean norm between quantile functions. The Monge map is $Q_\nu\circ F_\mu$ (p. 320).
- *Gaussians* (elliptically contoured family):
$$W_2^2\big(\mathcal N(m_1,\Sigma_1),\mathcal N(m_2,\Sigma_2)\big)=\|m_1-m_2\|^2+\mathcal B^2(\Sigma_1,\Sigma_2)\tag{6.210}$$
$$\mathcal B^2(\Sigma_1,\Sigma_2)=\operatorname{tr}\Big(\Sigma_1+\Sigma_2-2\big(\Sigma_1^{1/2}\Sigma_2\Sigma_1^{1/2}\big)^{1/2}\Big)\tag{6.211}$$
These are well defined even for non-invertible covariances and reduce to the distance between means as both covariances go to 0 (p. 320).
- If $\Sigma_1$ is invertible, the optimal Monge map is
$$T:x\mapsto A(x-m_1)+m_2,\quad A\triangleq\Sigma_1^{-1/2}\big(\Sigma_1^{1/2}\Sigma_2\Sigma_1^{1/2}\big)^{1/2}\Sigma_1^{-1/2}.\tag{6.212}$$
- Proof (author's): an affine push-forward of a Gaussian is Gaussian, and $A$ is designed to turn variance $\Sigma_1$ into $\Sigma_2$. $T$ is the gradient of a convex quadratic because $A$ is positive definite, so Brenier gives optimality (p. 321).

**6.8.3.5 Exact evaluation with LP solvers (p. 321).**
- Neural-network approaches (1-Lipschitz or convex nets) are non-convex and reach only local optima. Beyond those and the closed forms, the reliable route is the discrete problem (6.192) or its dual (6.198) (p. 321).
- The primal is a network-flow problem, solvable by network simplex in $O(nm(n+m)\log(n+m))$ or by the auction algorithm. Limits: cubic cost, and combinatorial structure that is hard to parallelize across problems sharing a cost matrix $C$ (p. 321).
- Statistical issue: in practice one has only i.i.d. samples $\hat\mu_n,\hat\nu_n$ of continuous measures in $\mathbb R^q$. The sample complexity of using (6.192) to approximate (6.196) is of order $1/n^{1/q}$ [FG15], so the gap between $W_2(\mu,\nu)$ and $W_2(\hat\mu_n,\hat\nu_n)$ shrinks extremely slowly in high dimension. Exact solving between samples is mostly wasted overfitting, so regularization is needed (p. 321).

**6.8.3.6 Entropic regularization (p. 321–p. 322).**
- Regularize by the KL divergence of the coupling to the product measure:
$$W_{c,\gamma}(\mu,\nu)\triangleq\inf_{\pi\in\Pi(\mu,\nu)}\int_{\mathcal X^2}d(x,y)^p\,d\pi+\gamma D_{\mathrm{KL}}(\pi\|\mu\otimes\nu).\tag{6.213}$$
- For discrete measures this is a $\gamma$-strongly convex problem (the page writes the constraints as $P\mathbf 1_m=a$, $P^T\mathbf 1_n=b$; $\mathbb H$ is entropy, not defined on these pages):
$$\mathrm{OT}_{C,\gamma}(a,b)=\min_{P\in\mathbb R_+^{n\times m},\,P\mathbf 1_m=a,\,P^T\mathbf 1_n=b}\langle P,C\rangle-\gamma\mathbb H(P)+\gamma(\mathbb H(a)+\mathbb H(b)),\tag{6.214}$$
with dual, where $K\triangleq e^{-C/\gamma}$ elementwise,
$$\mathrm{OT}_{C,\gamma}(a,b)=\max_{f\in\mathbb R^n,g\in\mathbb R^m}f^Ta+g^Tb-\gamma(e^{f/\gamma})^TKe^{g/\gamma}+\gamma(1+\mathbb H(a)+\mathbb H(b)).\tag{6.215}$$
- The unique primal solution links to the optimal dual pair:
$$P^\star_\gamma=\operatorname{diag}(e^{f/\gamma})\,K\,\operatorname{diag}(e^{g/\gamma}).\tag{6.216}$$
- Block-coordinate ascent on $f$ then $g$ is the Sinkhorn algorithm, written with log-sum-exp, starting from arbitrary $g$ and repeating until convergence:
$$f\leftarrow\gamma\log a-\gamma\log Ke^{g/\gamma},\qquad g\leftarrow\gamma\log b-\gamma\log K^Te^{f/\gamma}.\tag{6.217}$$
- Convergence is slower as $\gamma$ decreases (harder to approach LP solutions). Statistically, [Gen+19] argue the sample complexity becomes $O(1/\sqrt n)$, but with a constant of order $1/\gamma^{q/2}$ that worsens with dimension (p. 322). The intro to the section calls the method convex, simple, embarrassingly parallel and quadratic in cost (p. 321).

> **Intuition note.** The KL term makes the problem strongly convex. This gives a unique solution with a simple scaling form (6.216), and two alternating updates find it. Convergence is slower as $\gamma$ decreases, reflecting the difficulty of approaching the LP solution.

### 6.9 Submodular optimization (Jeff Bilmes) (p. 322–p. 342)

#### Opening (p. 322–p. 323)
- A submodular function is defined on subsets of a finite ground set $V$. Finding a guaranteed-good subset would ordinarily need exponential computation, but submodularity makes optimization tractable or approximable (p. 322, p. 323).
- Core property: diminishing returns, i.e. adding an element to a smaller set helps more than adding it to a larger one. Unlike convexity, submodular functions can be both minimized and (approximately) maximized, with very different algorithms and applications (p. 323).
- The author says "discrete convexity" is not quite right. Submodular functions share properties with both convex and concave functions, but some properties resemble neither. They cannot be conveyed by a univariate function (p. 323).

#### 6.9.1 Intuition, examples, background (p. 323–p. 325)
- A set function $f:2^V\to\mathbb R$ assigns a value to each subset. $X+v\equiv X\cup\{v\}$. Gains: $f(v|X)=f(X+v)-f(X)$ and $f(X|Y)=f(X\cup Y)-f(Y)$ (p. 323).
- **Coffee, lemon, milk, tea (Fig. 6.19).** $V=\{c,l,m,t\}$, $f$ = average price a typical person would pay. Values at the vertices of the 4-D hypercube, read from the page image (p. 324):

| Set | value | Set | value | Set | value |
|---|---|---|---|---|---|
| ∅ | 0 | {c,l} | 4 | {c,l,m} | 6 |
| {c} | 3 | {c,m} | 5 | {c,l,t} | 7 |
| {l} | 1 | {c,t} | 4 | {c,m,t} | 8 |
| {m} | 1 | {l,m} | 2 | {l,m,t} | 7 |
| {t} | 2 | {l,t} | 5 | {c,l,m,t} | 9 |
| | | {m,t} | 5 | | |

- Relations described (p. 323–p. 324): $f$ is strictly monotone. Coffee and tea substitute: $f(c,t)<f(c)+f(t)$ (subadditive). Milk and coffee complement: $f(m,c)>f(m)+f(c)$ (superadditive). Lemon and milk are additive (modular): $f(l,m)=f(l)+f(m)$.
- Given tea, lemon and milk are substitutes: $f(l|m,t)<f(l|t)$ and $f(m|l,t)<f(m|t)$, so $f(l,t)+f(m,t)>f(l,m,t)+f(t)$ (submodular). Given milk, tea and lemon complement: $f(t|l,m)>f(t|m)$, $f(l|t,m)>f(l|m)$, so $f(l,m)+f(m,t)<f(l,m,t)+f(m)$ (supermodular) (p. 324).
- The one function $f$ of Fig. 6.19 contains submodular, supermodular and modular relations, so it is globally none of the three. Combinatorial auctions may want such mixes (handled by differences of submodular functions or a submodular plus supermodular sum). In machine learning one usually wants functions that are submodular (or modular, or supermodular) everywhere (p. 325).

#### 6.9.2 Basic definitions (p. 325–p. 326)
**Definition 6.9.1.** $f:2^V\to\mathbb R$ is submodular if for all $X,Y\subseteq V$:
$$f(X)+f(Y)\ge f(X\cup Y)+f(X\cap Y).\tag{6.218}$$
**Definition 6.9.2 (diminishing returns).** $f$ is submodular if for all $X\subseteq Y\subseteq V$ and $v\notin Y$:
$$f(X+v)-f(X)\ge f(Y+v)-f(Y).\tag{6.219}$$
The author says these are equivalent (other equivalent definitions exist, [Bil22]). Lemon example: (6.218) with $X=\{m,t\}$, $Y=\{l,t\}$; (6.219) with $X=\{t\}$, $Y=\{m,t\}$, $v=l$ (p. 326).

- Shannon entropy of subsets of random variables is submodular. There are non-negative, monotone non-decreasing submodular functions that are not entropic, so submodular does not just restate entropy functions (p. 326).
- **Polymatroid function:** monotone non-decreasing, submodular, normalized $f(\emptyset)=0$. Entropy is one, but not all polymatroids are entropic (p. 326).
- $f$ is supermodular iff $-f$ is submodular. Both submodular and supermodular means modular: $m(A)=c+\sum_{v\in A}m_v$. If normalized, $c=0$ and $m$ is a vector in $\mathbb R^V$ (p. 326).
- Any set function is a function on vertices of the unit hypercube $[0,1]^n$. The characteristic vector $\mathbf 1_X\in\{0,1\}^V$ maps sets to binary vectors (p. 326).
- Closure: non-negative weighted (conical) combinations $f=\sum_{i=1}^k\omega_if_i$, $\omega_i\ge0$, of submodular functions are submodular, by Def. 6.9.1. Submodular functions form a cone in $2^n$ dimensions, an intersection of exponentially many half-spaces (p. 326).

> **Intuition note.** Submodularity is "the more you have, the less a new thing adds". The cone view says the inequalities are linear in $f$. So adding submodular functions or scaling them by non-negative numbers cannot break them.

#### 6.9.3 Example submodular functions (p. 327–p. 329)
- **Concave of cardinality:** $f(A)=\sqrt{|A|}$. If $|A|=k$, the gain is $\sqrt{k+1}-\sqrt k$, decreasing in $k$. Any concave $\phi$ gives submodular $\phi(|A|)$ (for convex $\phi$ it is supermodular, footnote 8) (p. 327).
- **Concave of modular:** $f(A)=\phi(m(A))$ with $m(a)\ge0$. Sums plus an arbitrary modular term give *feature-based* functions
$$f(A)=\sum_{u\in U}\phi_u(m_u(A))+m_\pm(A),$$
with $\phi_u$ concave, $m_u\ge0$, $m_\pm$ arbitrary. $U$ is a set of non-negative features ("bag-of-words" sense). They tend to reward diversity because each $\phi_u$ is concave, so a larger valuation needs a feature not yet diminished (p. 327).
- **Facility location:** $f(A)=\sum_{v\in V}\max_{a\in A}\mathrm{sim}(a,v)$, with $\mathrm{sim}\ge0$. Every $v$ is represented by its most similar element of $A$. It is monotone and needs only an affinity matrix. The author nicknames it the "k-means of submodular functions" (p. 327).
- Facility location is feature-based. For sorted $0\le x_1\le\dots\le x_n$, $y_i=x_i-x_{i-1}$, $x_0=0$:
$$\max_{a\in A}x_a=\sum_{i=1}^ny_i\min\big(|A\cap\{i,\dots,n\}|,1\big),$$
a weighted sum of concave-of-modular terms (p. 327).
- **Set cover:** $f(X)=|\bigcup_{v\in X}U_v|=\sum_{u\in U}\min(1,m_u(X))$, with $m_u(v)=1$ iff $u\in U_v$. Vertex cover: $U=V$ is the vertex set and $m_u(v)=1$ iff $u,v$ are adjacent. Edge cover: $V$ = edges, $U$ = vertices, $m_u(v)=1$ iff edge $v$ is incident to $u$ (p. 328).
- **Probabilistic coverage:** $f(X)=\sum_{u}\omega_uf_u(X)$, $\omega_u\ge0$, with $f_u(X)=1-\prod_{v\in X}(1-P[B_{u,v}=1])=1-\exp(-m_u(X))$, where $m_u(X)=\sum_{v\in X}\log\frac1{1-P[B_{u,v}=1]}$. Since $\phi(z)=1-e^{-z}$ is concave, it is feature-based. Set cover is the case $P\in\{0,1\}$ (p. 328).
- **Graph cut:** for an undirected graph with weights $w_{i,j}=w_{j,i}\ge0$, $f(X)=\sum_{i\in X,j\in\bar X}w_{i,j}$. Then
$$f(X)=\sum_{i,j\in V}w_{i,j}\mathbf 1\{i\in X,j\in\bar X\}\tag{6.220}$$
$$=\tfrac12\sum_{i,j}w_{i,j}\min(|X\cap\{i,j\}|,1)+\tfrac12\sum_{i,j}w_{i,j}\min(|(V\setminus X)\cap\{i,j\}|,1)-\tfrac12\sum_{i,j}w_{i,j}\tag{6.221}$$
$$=\tilde f(X)+\tilde f(V\setminus X)-\tilde f(V),\quad\tilde f(X)=\tfrac12\sum_{i,j}w_{i,j}\min(|X\cap\{i,j\}|,1).\tag{6.222}$$
$\tilde f$ is submodular (concave of modular), so is $\tilde f(V\setminus X)$ in $X$. The cut is a sum of non-normalized feature-based functions; the constant $\tilde f(V)$ is subtracted for equality (p. 328, p. 329).
- **Cooperative cut:** view the cut as a map from node sets to edge sets, weighed by a modular $w$. Replace $w$ by a polymatroid $g$ on edge sets: $h(X)=g(\text{cut edges})$. $h$ is in general neither submodular nor supermodular, but there are practical algorithms exploiting its internal submodular structure (p. 329).
- **Deep submodular functions (DSF):** nested concave compositions, e.g. two-layer $f(A)=\phi\big(\sum_u\omega_u\phi_u(\sum_{a\in A}m_u(a))\big)$, and a three-layer version. DSFs strictly expand the class beyond feature-based functions (p. 329).

#### 6.9.4 Submodular optimization (p. 329–p. 333)
- **Maximize** a submodular $f$ to encourage diversity, information, coverage, dispersion: $\max_{A\in\mathcal C}f(A)$ for a constraint set $\mathcal C\subseteq2^V$. Reason: elements similar to what you hold lose value, so good sets are jointly dissimilar (p. 329).
- Fig. 6.20: 10 points from 1000 in 2-D chosen by facility location with Gaussian kernel $\mathrm{sim}(a,v)=\exp(-d(a,v))$ tend to cover the space better than random 10-subsets, which miss large regions and/or pick points near each other. The function must be instantiated appropriately (p. 330).
- **Minimize** a submodular function for homogeneity or coherence: $\min_{A\in\mathcal C}f(A)$, e.g. choosing a homogeneous pixel set for image segmentation (p. 330).

**6.9.4.1 Maximization (p. 330–p. 331).**
- Cardinality-constrained maximization is NP-complete, but the greedy algorithm, from $X_0=\emptyset$, for $i=0..k-1$:
$$X_{i+1}=X_i\cup\Big(\arg\max_{v\in V\setminus X_i}f(X_i\cup\{v\})\Big)\tag{6.223}$$
gives $f(\tilde X)\ge(1-1/e)f(X^*)\approx0.63\,f(X^*)$ for a polymatroid $f$ [NWF78; FNW78]. This ratio is the best achievable in polynomial time if $P\ne NP$ [Fei98]. It holds regardless of $|V|$ and of which polymatroid is optimized, and can be accelerated (p. 330, p. 331).
- **Total curvature** (for $f(v)>0$): $\kappa=1-\min_{v}f(v|V-v)/f(v)\in[0,1]$. Greedy guarantees $\frac1\kappa(1-e^{-\kappa})\ge1-1/e$. This equals $1-1/e$ when $\kappa=1$ and improves as $\kappa$ falls. $\kappa=0$ iff $f$ is modular, where greedy is optimal (p. 331).
- For $h=f+g$ ($f$ submodular, $g$ supermodular; a "BP function", which exists only sometimes) with supermodular curvature $\kappa^g=1-\min_vg(v)/g(v|V-v)$, greedy has ratio $\frac1\kappa(1-e^{-\kappa(1-\kappa^g)})$ (p. 331).

**6.9.4.2 Discrete constraints (p. 331–p. 332).**
- *Knapsack:* modular costs $m(v)\ge0$, $\max_{m(X)\le b}f(X)$. Plain greedy does not solve it, but a cost-scaled variant does. Used in multi-document summarization (p. 331).
- *Matroids:* independent sets of a matroid as constraint. Partition matroid: blocks $V_1..V_m$ with limits $\ell_i$:
$$\mathcal I_p=\{X:\forall i\in[m],\ |V_i\cap X|\le\ell_i\}.\tag{6.224}$$
$(V,\mathcal I_p)$ is a matroid. It generalizes a cardinality limit to per-group limits, useful for fairness (p. 332).
- For any matroid, $\max_{X\in\mathcal I}f(X)$ is solved with a $1/2$ approximation by the same greedy algorithm. Intersections of matroids, matroids plus knapsack (knapsacks are not matroid constraints), and level sets of another submodular function (SCSK: $\max_{g(X)\le\alpha}f$; SCSC: $\min_{g(X)\ge\alpha}f$) are also possible. Covering and cut constraints are mentioned too (p. 332).
- *Non-monotone case:* graph cut, and $f(X)=\log\det(\mathbf M_X)$ for an SPD matrix $\mathbf M$ with row-column submatrix $\mathbf M_X$, are submodular but not necessarily monotone. This underlies determinantal point processes (DPPs), which give high probability to diverse sets. Diversity is the volume (determinant) of the parallelepiped, and the log makes it submodular. A DPP is log-submodular (p. 332).

**6.9.4.3 Minimization (p. 333).**
- Unconstrained maximization is NP-hard (but approximable). Minimization is not NP-hard: polynomial-time algorithms exist, a property shared with convex functions (p. 333).
- History: [GLS81] gave a polynomial but impractical ellipsoid-based algorithm. Queyranne showed an algorithm [NI92] works for symmetric $f$ ($f(X)=f(V\setminus X)$) in $O(n^3)$. Combinatorial algorithms around 2000 [IFF00; Sch00] had very high degree, e.g. $\tilde O(|V|^7\gamma)$. Later results: $\tilde O(|V|^5\gamma+|V|^6)$ [IO09]; strongly polynomial $O(|V|^3\log^2|V|)$ [LSW15], improved to $O(|V|^3)$ [Jia21]. Practical methods: Fujishige–Wolfe and Frank–Wolfe, minimizing a 2-norm on a polyhedron $B_f$ (p. 333).

> **Intuition note.** Maximizing a submodular function is hard (NP-hard) but forgiving: for a polymatroid function under a cardinality constraint, greedy gets within a fixed fraction ($1-1/e$). Minimizing a submodular function is solvable exactly in polynomial time, a property shared with convex functions, although the first polynomial algorithms were impractical.

#### 6.9.5–6.9.6 Applications; summarization, coresets (p. 333–p. 337)
- Submodularity of entropy is less explored in ML than entropy itself; the survey is brief, not exhaustive (p. 333, p. 334).
- Summary types: sketches, coresets (small weighted subset giving about the same answer, e.g. diameter, k-center), extractive vs abstractive document summaries, data distillation (synthetic pseudosamples). Compression differs: its output need only be usable by the decoder (p. 334, p. 335).
- The author contends that summarization, coresets, sketching and distillation are analogous, possibly synonymous, and differ from compression. What matters is the design choices (p. 335).
- Treat $f(X)$ as the information in $X$. Maximizing $f(X)$ under $|X|\le k$ is a coreset computation. Since $f(V)=f(V\setminus X|X)+f(X)$, it minimizes the residual $f(V\setminus X|X)$. The same greedy algorithm applies to every submodular $f$ with its guarantee for that $f$ (p. 335).
- Three ways to get $f$ (p. 335): (1) hand-crafted, e.g. facility location or a convex combination of several, as in [KKT03] (influential social-network nodes), [LB09] (speech selection with Fisher kernels), and others for documents, translation data, active learning, video (p. 336); (2) learned; (3) a mathematical coreset guarantee.
- *Learnability:* with polynomially many queries, a monotone submodular $f$ cannot be approximated better than $\tilde\Omega(\sqrt n)$ multiplicatively [SF08; Goe+09]. The PAC and PMAC models and additive-error norms $\mathrm{err}_p$ are described. The gist: hard to learn everywhere and accurately (p. 336).
- In practice one learns mixture weights $\alpha_i$ of fixed components $f(A)=\sum_i\alpha_if_i(A)$ by linear regression or max-margin, or by reinforcement learning. These do better than hand-crafting but lack guarantees (p. 336, p. 337).
- *Submodular coresets with guarantees:* training accuracy of certain naive Bayes and k-NN classifiers is submodular [WIB15]. For gradient-matching, a bound by a supermodular function converts to facility location [MBL20]. Other cases are bi-level (train/validation) objectives (p. 337).
- Transposing the design matrix: extractive summarization or subset selection corresponds to feature selection, and abstractive or sketching methods to dimensionality reduction (p. 337).

#### 6.9.7 Combinatorial information functions (p. 337–p. 338)
- Entropy $H(X_1..X_n)=-\sum p\log p$; set-argument mutual information $I_H(A;B|C)=I(X_A;X_B|X_C)$ (p. 337, p. 338).
- A polymatroid is normalized, non-negative, monotone, and "conditioning reduces valuation": $f(A|B)\ge f(A|B,C)$ (identical to submodularity). Shannon deemed these natural for entropy. This justifies viewing polymatroids as information functions and as summarization objectives (p. 338).
- **Combinatorial conditional mutual information (CCMI):**
$$I_f(A;B|C)=f(A+C)+f(B+C)-f(C)-f(A+B+C),$$
also called the connectivity function. For entropy it gives standard mutual information. It scores $A,B$ similarity while discounting what is due to $C$ (p. 338).
- $C=\emptyset$: $g(A)=I_f(A;V\setminus A)$ is symmetric submodular. [GKS05] optimized it greedily, with a guarantee if $g$ is monotone up to $2k$ elements for summaries of size $k$. $g_C(A)=I_f(A;C)$ is not submodular in general ([KG05], entropy), but is if elements of $V$ are independent given $C$: then $I_f(A;C)=f(A)-\sum_{a\in A}f(a|C)$, submodular minus modular (p. 338).
- With $f(i,j|S)\triangleq f(j|S+i)-f(j|S)$: if this is monotone non-decreasing in $S$, then $I_f(A;B|C)$ is submodular in $A$ for fixed $B,C$. This holds for several common functions [Iye+21], e.g. facility location, where
$$I_f(A;B|C)=\sum_{v\in V}\max\Big(\min\big(\textstyle\sum_{a\in A}\mathrm{sim}(v,a),\max_{b\in B}\mathrm{sim}(v,b)\big)-\max_{c\in C}\mathrm{sim}(v,c),\,0\Big).$$
It was used [Kot+22] to make summaries relevant to a query $B$ while neglecting "private" $C$ (p. 338).

#### 6.9.8 Clustering, partitioning, parallel ML (p. 339)
- $g(A)=I_f(A;V\setminus A)$ is symmetric submodular, so Queyranne's algorithm can minimize it. The minimizer $A$ is least similar to $V\setminus A$ and gives a 2-clustering. Recursing on $A$ and $V\setminus A$ with $g_A(B)=I_f(B;A\setminus B)$ and $g_{V\setminus A}(B)=I_f(B;(V\setminus A)\setminus B)$ yields top-down recursive bisection (Q-clustering). Multiway graph cut is a related case (p. 339).
- Cardinality-constrained maximization with facility location resembles k-medoids. Applications named: brain parcellation, distributed-training data partitioning, mini-batch construction (p. 339).

#### 6.9.9 Active and semi-supervised learning (p. 339–p. 340)
- Unlabeled samples get scores $s_t(x_i)$ (e.g. output entropy or top-two-posterior margin). This is modular: $m_t(A)=\sum_{a\in A}s(x_a)$. Mini-batch active learning picks $A_t\in\arg\max_{A\subseteq U_t,|A|=k}m_t(A)$, labels it, updates scores, repeats (p. 339).
- Problem: $A_t$ may be redundant, since uncertainty may share one cause. Fix: add a submodular diversity term, $A_t\in\arg\max_{A\subseteq U_t,|A|=k}m_t(A)+f_t(A)$, combining uncertainty and diversity [WIB15; Kau+19] (p. 340).
- *Batch semi-supervised version [GB11]:* graph nodes with labels $y\in\{0,1\}^V$, $V(y)=\{v:y_v=1\}$, $I_f(A)\triangleq I_f(A;V\setminus A)$ (always submodular). $I_f(V(y))$ measures the "smoothness" of a labeling. Define $\Psi(L)\triangleq\min_{T\subseteq V\setminus L,T\ne\emptyset}I_f(T)/|T|$. If $y'=\arg\min_{\hat y:\hat y_L=y_L}I_f(V(\hat y))$, then
$$\|y-y'\|^2\le2I_f(V(y))/\Psi(L),$$
suggesting one can find a good $L$ by maximizing $\Psi(L)$; the author says this holds for any submodular $f$ (p. 340).

#### 6.9.10 Probabilistic modeling (p. 340–p. 341)
- Take $p(x)\propto\exp(-E(x))$. Finding $\max_xp(x)$ equals $\min_xE(x)$, doable in polynomial time if $E(x)=f(V(x))$ is submodular, even for high tree-width (e.g. $\sqrt{|A|}-m(A)$ has tree-width $n-1$) (p. 340).
- This restricts *how* variables interact rather than *who* interacts, and can be combined with graph restrictions. In vision it underlies graph-cut and move-making algorithms ($\alpha$–$\beta$ swap, $\alpha$-expansion); [KZ02] rediscovered submodularity (the "regular" property) as what makes MRFs solvable by graph cut (p. 341).
- Submodular $E$ gives a log-supermodular distribution, with high probability on homogeneous configurations (segmentation). DPPs are log-submodular, with high probability on diverse sets (p. 341).
- General inference (marginals, partition function $Z=\sum_{A\subseteq V}\exp(f(A))$, constrained maximization) often lacks polynomial algorithms even for submodular or supermodular objectives. Variational methods use semi-gradients: for submodular or supermodular $f$ and set $A$, one can build in linear time modular bounds $m_A\le f\le m^A$, tight at $A$ [IB15]. A modular function gives a product-form $p(\mathbf 1_A)=\prod_{a\in A}\sigma(m(a))\prod_{a\notin A}\sigma(-m(a))$ ($\sigma$ logistic; the page writes $\exp(E)$, see Reading notes). This is like a mean-field approximation with independent variables, giving bounds on $Z$ (p. 341).

#### 6.9.11 Structured norms and losses (p. 341–p. 342)
- $\|x\|_0$ is intractable and non-differentiable; its closest convex relaxation is $\|x\|_1$ (lasso), which treats entries independently. Group norms (group lasso) penalize groups together (p. 341, p. 342).
- $\|x\|_0=|V(x)|$ with $|A|$ modular. Replace it by $f(V(x))$ for submodular $f$, giving cooperative penalties, but this stays combinatorial. Use the Lovász extension $\breve f$ (convex, not a norm): $\|x\|_f=\breve f(|x|)$ satisfies all norm properties for all non-trivial submodular $f$ (normalized, $f(v)>0$) [PG98; Bac+13]. Group lasso is the special case of a sum of min-truncated cardinality functions (p. 342).

#### 6.9.12 Conclusions (p. 342)
Only the surface is touched; the simple submodular inequality, like convexity's definition, hides much complexity (p. 342).

## Toy example (ours, not from the text)
Ground set $V=\{1,2,3\}$. Facility location $f(A)=\sum_{v\in V}\max_{a\in A}\mathrm{sim}(a,v)$, with $\mathrm{sim}(i,i)=1$, $\mathrm{sim}(1,2)=0.8$, $\mathrm{sim}(1,3)=0.1$, $\mathrm{sim}(2,3)=0.2$ (symmetric).

Singletons:
- $f(\{1\})=1+0.8+0.1=1.9$.
- $f(\{2\})=0.8+1+0.2=2.0$.
- $f(\{3\})=0.1+0.2+1=1.3$.

Pairs:
- $f(\{1,2\})=\max(1,0.8)+\max(0.8,1)+\max(0.1,0.2)=1+1+0.2=2.2$.
- $f(\{2,3\})=\max(0.8,0.1)+1+\max(0.2,1)=0.8+1+1=2.8$.
- $f(\{1,3\})=1+\max(0.8,0.2)+1=2.8$.
- $f(V)=3$.

**Greedy, $k=2$ (6.223).** Step 1: the best singleton is $\{2\}$ (2.0). Step 2: adding 1 gives 2.2, adding 3 gives 2.8, so it picks 3 and ends at $\{2,3\}$ with $f=2.8$. The optimum over pairs is also 2.8, so here greedy is optimal. This is consistent with $f(\tilde X)\ge(1-1/e)f(X^*)\approx0.63\cdot2.8=1.77$.

**Diminishing returns (6.219).** Take $X=\emptyset\subseteq Y=\{2\}$, $v=3$. Then $f(3|\emptyset)=1.3\ge f(3|\{2\})=2.8-2.0=0.8$. ✓.

**Submodular inequality (6.218).** Take $X=\{1\}$, $Y=\{3\}$. Then $f(X)+f(Y)=1.9+1.3=3.2\ge f(\{1,3\})+f(\emptyset)=2.8+0=2.8$. ✓.

## Concepts
- [[optimal-transport]] (new) — cheapest way to move mass from one distribution to another; compares distributions (p. 314)
- [[optimal-matching]] (new) — minimize $\sum_ic(x_i,y_{\sigma_i})$ over permutations; Hungarian algorithm $O(n^3)$ (p. 315)
- [[kantorovich-formulation]] (new) — LP over couplings $P$ (or $\pi\in\Pi(\mu,\nu)$) with fixed marginals; allows mass splitting (p. 316, p. 317)
- [[monge-formulation]] (new) — minimize average cost over maps with $T_\sharp\mu=\nu$; non-convex (p. 317)
- [[wasserstein-distance]] (new) — $W_p$: optimal Kantorovich value for cost $d^p$, then the $1/p$ power (p. 317)
- [[c-transform-duality]] (new) — $\overline f(y)=\inf_xc(x,y)-f(x)$; $c$-concave functions give the semi-dual (p. 318)
- [[brenier-theorem]] (new) — for squared-Euclidean cost, the optimal Monge map is the gradient of a convex function (p. 319)
- [[entropic-regularization-sinkhorn]] (new) — add $\gamma D_{\mathrm{KL}}(\pi\|\mu\otimes\nu)$; solve by alternating log-sum-exp updates (p. 322)
- [[kl-divergence]] — used here as the regularizer of the coupling (p. 322)
- [[submodular-function]] (new) — set function with $f(X)+f(Y)\ge f(X\cup Y)+f(X\cap Y)$, equivalently diminishing returns (p. 325)
- [[polymatroid-function]] (new) — monotone non-decreasing, submodular, $f(\emptyset)=0$ (p. 326)
- [[modular-function]] (new) — both sub- and supermodular: $c+\sum_{v\in A}m_v$ (p. 326)
- [[feature-based-submodular-function]] (new) — $\sum_u\phi_u(m_u(A))+m_\pm(A)$ with concave $\phi_u$, non-negative modular $m_u$ (p. 327)
- [[facility-location]] (new) — $\sum_v\max_{a\in A}\mathrm{sim}(a,v)$; diversity or representative-selection function (p. 327)
- [[graph-cut-function]] (new) — weight of edges crossing between $X$ and its complement; submodular; not monotone (p. 328, p. 332)
- [[greedy-submodular-maximization]] (new) — repeatedly add the best-gain element; $1-1/e$ guarantee for polymatroids (p. 330, p. 331)
- [[submodular-curvature]] (new) — $\kappa=1-\min_vf(v|V-v)/f(v)$; sharpens the greedy bound (p. 331)
- [[matroid-constraint]] (new) — independent-set constraint, e.g. partition matroid; greedy gives $1/2$ (p. 331, p. 332)
- [[submodular-function-minimization]] (new) — polynomial-time minimization of submodular $f$ (p. 333)
- [[combinatorial-mutual-information]] (new) — $I_f(A;B|C)=f(A+C)+f(B+C)-f(C)-f(A+B+C)$ for any submodular $f$ (p. 338)
- [[log-submodular-model]] (new) — distributions whose log-density is submodular (e.g. DPP); the opposite sign gives log-supermodular (p. 341)
- [[submodular-structured-norm]] (new) — $\|x\|_f=\breve f(|x|)$, Lovász extension of $f$ on $|x|$; includes group lasso (p. 342)

## Canonical instances
- [[coffee-lemon-milk-tea]] — a 4-item set function mixing sub-, super- and modular relations (p. 324)
- [[facility-location-diversity-fig-6-20]] — facility-location-selected points tend to cover the space better than random subsets (p. 330)
- [[gaussian-w2-bures]] — closed-form $W_2$ and affine Monge map between Gaussians (p. 320, p. 321)
- [[taxi-and-job-matching]] — motivating applications of optimal matching (p. 315)
- [[dpp-log-det]] — $\log\det\mathbf M_X$ as submodular diversity function (p. 332)
- [[cma-es-population]] — Gaussian-search illustration of derivative-free optimization (p. 314)

## Bridges (candidates)
- [structural-analogy] Entropic OT regularization with $D_{\mathrm{KL}}(\pi\|\mu\otimes\nu)$ ↔ bayesian: KL divergence as a regularizer or objective in variational inference — both use KL to turn a hard problem into a smooth one.
- [structural-analogy] Modular approximation of a log-submodular distribution ↔ bayesian: mean-field variational inference — the author says it is "like a mean-field approximation" with independent variables (p. 341).
- [structural-analogy] Submodular active-learning objective $m_t(A)+f_t(A)$ ↔ bayesian: batch experiment design — uncertainty plus diversity to avoid redundant queries.
- [structural-analogy] Greedy maximization with a $1-1/e$ guarantee ↔ convex optimization: polynomial-time guarantees — the author compares submodularity with convexity (p. 323).
- [metaphor] DPP (diverse subsets with high probability) ↔ bayesian: a prior that encodes repulsion between samples.

## Questions this raises
- How does the choice of $\gamma$ trade bias against speed in Sinkhorn, and how should it scale with dimension $q$ given the $1/\gamma^{q/2}$ constant?
- When is a practical objective (such as model accuracy on a subset) submodular, and when must one fall back on a difference-of-submodular decomposition?
- How tight are the $1/2$ matroid and $1-1/e$ cardinality guarantees in practice, and how much does curvature help on real data?
- Can the Brenier structure (convex potentials) be exploited with learned input-convex networks to estimate OT maps reliably in high dimension?

## Reading notes
- This is part 3 of Chapter 6 (split at a section boundary). It starts at §6.7.7 (after the Fig. 6.17 caption, p. 314) and ends with §6.9.12 (p. 342). The earlier parts are not covered.
- Page offset: printed = pdf − 34. The footer reads "Online version. December 10, 2025". §6.8 is by Marco Cuturi and §6.9 by Jeff Bilmes, as stated in the text.
- Misprints and inconsistencies seen in the page images:
  - (6.191) is printed with $c(x_i,y_{\sigma_j})$; the text says $y_{\sigma_i}$.
  - In (6.192) the constraint is printed $P\mathbf 1_n=a$, $P^T\mathbf 1_m=b$, which does not match the shapes ($P$ is $n\times m$). (6.214) prints $P\mathbf 1_m=a$, $P^T\mathbf 1_n=b$.
  - p. 317 counterexample reads "$T_\sharp\mu=\nu$ and $T'_\sharp\nu$"; presumably $T'_\sharp\mu=\nu$ is meant.
  - (6.207) prints $y_0-x_0-\nabla f^\star(x_0)=0$, but the stated conclusion needs $x_0-y_0-\nabla f^\star(x_0)=0$ (corrected in L3, marked as an added step).
  - In (6.203) the text layer drops the bar on $f$ in the second integral; the image shows $\overline f$.
  - p. 328: the weighted coverage sum is printed with $f_u(X)$ on the left side.
  - p. 329: the cut set is printed with "$X\setminus X$" where $\bar X$ is meant.
  - p. 341: $p(\mathbf 1_A)=1/Z\exp(E(\mathbf 1_A))$ conflicts with $p\propto\exp(-E)$ used on p. 340.
  - p. 331: "total curvature if the polymatroid" should read "of".
- The values in the coffee/lemon/milk/tea table were read from the Fig. 6.19 image; the text layer of that figure is garbled. The values satisfy all relations the text states.
- Several citations and complexity results (p. 333, p. 336) were compressed; only a selection is reported here. The claim on p. 331 that "any set function can be written as a difference of submodular functions" is the author's, deferred to "below"; no proof appears in these pages.
