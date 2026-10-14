---
id: deisenroth-2020-mml/ch07-continuous
work: deisenroth-2020-mml
unit: 7 Continuous Optimization
pages: 225-248
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Continuous Optimization

## L0 — One line
Training a model often means minimising a differentiable objective by following negative gradients (gradient descent), and for constrained convex problems Lagrange duality and the convex conjugate give a second, dual way to solve the same problem.

## L1 — The gist (≤ 120 words)
Training a machine-learning model often means minimising an objective function over parameters. The chapter asks how to do this numerically. Without constraints, the answer is gradient descent: step against the gradient, with choices about step-size (step length), momentum (memory of past steps) and mini-batch (random-subset, stochastic) gradients. With constraints, Lagrange multipliers produce a dual problem (a second problem in the multipliers). For convex problems, every local minimum is global and strong duality (equal primal and dual optima) holds. The chapter treats linear and quadratic programs. It also treats the convex conjugate (Legendre–Fenchel transform), another route to dual problems. The chapter calls stochastic gradient descent the current workhorse of large-scale machine learning.

**Prerequisites:** gradients and Hessians (Ch. 5); row-vector gradient convention; matrices, positive (semi)definiteness, singular values; expectation and sample means (Ch. 6); the idea of a supremum.

## L2 — Key ideas
- Gradient descent moves against the gradient: $x_{i+1}=x_i-\gamma_i(\nabla f(x_i))^\top$. For suitable step-sizes the sequence of function values does not increase and converges to a local minimum. The start point can matter when $f$ is non-convex, whereas convex functions do not show this dependence (pp. 226–228).
- Step-size (the step length), condition number (ratio of largest to smallest singular value of $A$ in $Ax=b$) and momentum (memory of past updates) affect speed. Poorly conditioned problems (long thin valleys) make gradient descent zigzag, and momentum adds memory to damp this (pp. 229–231).
- SGD replaces the full gradient by an unbiased estimate from a subset of the data. This is cheaper, and small mini-batches add noise (pp. 231–232).
- Lagrange multipliers replace an infinite penalty by a linear one. This gives the dual function $\mathfrak D(\lambda)$, which is concave, and weak duality (primal ≥ dual) follows from the minimax inequality (maximin ≤ minimax) (pp. 233–235).
- Convex sets and convex functions are defined by the line-segment inequalities (7.29), (7.30). Convexity can also be tested with the gradient (7.31) or the Hessian. Nonnegative weighted sums preserve convexity (pp. 236–238).
- Convex problems have strong duality (the optimal dual and primal solutions coincide). Linear programs (7.39) and quadratic programs (7.45) have explicit duals (7.43), (7.52) (pp. 236, 239–242).
- The convex conjugate $f^*(s)=\sup_x(\langle s,x\rangle-f(x))$ describes a function by its tangent slopes. It gives dual problems without constraints, e.g. (7.68) (pp. 242–246).

## L3 — Walkthrough

### Chapter introduction (pp. 225–227)
- Training usually means finding good parameters. "Good" is set by the objective function or the probabilistic model. The chapter assumes a differentiable objective, so a gradient is available everywhere (p. 225).
- By convention objectives are minimised. The gradient points uphill, so we move opposite to it (p. 225).
- Unconstrained optimisation needs only this idea, plus design choices (Sec. 7.1). Constrained optimisation needs more concepts (Sec. 7.2). Convex problems (Sec. 7.3) allow statements about reaching the global optimum (p. 225).
- Running example, Figure 7.2:
$$\ell(x)=x^4+7x^3+5x^2-17x+3\tag{7.1}$$
$$\frac{d\ell}{dx}=4x^3+21x^2+10x-17\tag{7.2}$$
$$\frac{d^2\ell}{dx^2}=12x^2+42x+10\tag{7.3}$$
- Stationary points are the real roots of the derivative. This cubic has three: minima near $x=-4.5$ (global, value about $-47$) and $x=0.7$ (local), and a maximum near $x=-1.4$. A stationary point is a maximum if the second derivative there is negative (pp. 225–226).
- In general we cannot solve analytically (p. 226). Marginal note: by the Abel–Ruffini theorem there is in general no algebraic solution for polynomials of degree 5 or more (p. 227).
- So we start at some $x_0$, e.g. $-6$, and follow the negative gradient. It gives the direction but not the distance (the step-size). Starting at $x_0=0$ leads to the wrong (right-hand) minimum, which has a larger objective value (p. 227).
- Convex functions (Sec. 7.3) do not have this start-point problem: all local minima are global. Many ML objectives are designed to be convex (p. 227).
- Concepts are visualised in 1-D, but some do not generalise directly to higher dimensions (p. 227).

### 7.1 Optimization using gradient descent (pp. 227–232)
**Problem.** $\min_x f(x)$ with $f:\mathbb R^d\to\mathbb R$ differentiable, no closed-form solution (7.4) (pp. 227–228).

**Gradient descent** is a first-order method: steps proportional to the negative gradient (p. 228).
- The gradient points in the direction of steepest ascent. It is orthogonal to the contour lines $\{x: f(x)=c\}$. Gradients are row vectors, so the update uses a transpose (p. 228).
- If $\gamma\ge0$ is small, then
$$x_1=x_0-\gamma((\nabla f)(x_0))^\top\tag{7.5}$$
gives $f(x_1)\le f(x_0)$ (p. 228).
- Iterating from an initial guess $x_0$:
$$x_{i+1}=x_i-\gamma_i((\nabla f)(x_i))^\top\tag{7.6}$$
For suitable $\gamma_i$, $f(x_0)\ge f(x_1)\ge\dots$ converges to a local minimum (p. 228).

**Example 7.1.** The quadratic
$$f\!\left(\begin{bmatrix}x_1\\x_2\end{bmatrix}\right)=\tfrac12\begin{bmatrix}x_1\\x_2\end{bmatrix}^{\!\top}\begin{bmatrix}2&1\\1&20\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}-\begin{bmatrix}5\\3\end{bmatrix}^{\!\top}\begin{bmatrix}x_1\\x_2\end{bmatrix}\tag{7.7}$$
has gradient
$$\nabla f=\begin{bmatrix}x_1\\x_2\end{bmatrix}^{\!\top}\begin{bmatrix}2&1\\1&20\end{bmatrix}-\begin{bmatrix}5\\3\end{bmatrix}^{\!\top}\tag{7.8}$$
From $x_0=[-3,-1]^\top$ with $\gamma=0.085$: $x_1=[-1.98,1.21]^\top$, $x_2=[-1.32,-0.42]^\top$ (Figure 7.3) (pp. 228–229).

*Intuition note.* Gradient descent is a ball rolling downhill in small steps. A small enough step is guaranteed not to raise $f$; a large step may overshoot.

**Remark (slow near the minimum).** The asymptotic convergence rate is inferior to many other methods. For a long thin valley the problem is poorly conditioned. For poorly conditioned convex problems gradient descent increasingly zigzags, because gradients point nearly orthogonally to the shortest direction to the minimum (p. 229).

#### 7.1.1 Step-size (p. 229–230)
- Too small a step-size is slow. Too large can overshoot, fail to converge or diverge. The step-size is also called the learning rate (p. 229).
- Adaptive methods rescale the step-size using local properties. Two simple heuristics (Toussaint, 2012):
  - If $f$ increases after a step, the step was too large: undo the step and decrease the step-size.
  - If $f$ decreases, the step could have been larger: try to increase it (p. 229).
- The "undo" step looks wasteful, but the heuristic guarantees monotonic convergence (p. 230).

**Example 7.2 (linear systems).** To solve $Ax=b$ in practice we minimise the squared error
$$\|Ax-b\|^2=(Ax-b)^\top(Ax-b)\tag{7.9}$$
$$\nabla_x=2(Ax-b)^\top A\tag{7.10}$$
This gradient can be used in gradient descent. Here an analytic solution exists (set the gradient to zero; see Ch. 9) (p. 230).

**Remark (conditioning).** For $Ax=b$, the speed of gradient descent depends on the condition number $\kappa=\sigma(A)_{\max}/\sigma(A)_{\min}$, the ratio of the largest to smallest singular value. This essentially measures the ratio of the most to the least curved direction. One may instead solve $P^{-1}(Ax-b)=0$ with a *preconditioner* $P$. The goal is that $P^{-1}A$ has a better condition number while $P^{-1}$ is easy to compute (p. 230).

#### 7.1.2 Gradient descent with momentum (pp. 230–231)
- With poorly scaled curvature, steps hop between the valley walls and approach the optimum in small steps. The fix is to give gradient descent memory, like a heavy ball reluctant to change direction (Rumelhart et al., 1986) (p. 230).
- The update remembers $\Delta x_i$ and uses a linear combination of the current and previous gradients:
$$x_{i+1}=x_i-\gamma_i((\nabla f)(x_i))^\top+\alpha\Delta x_i\tag{7.11}$$
$$\Delta x_i=x_i-x_{i-1}=\alpha\Delta x_{i-1}-\gamma_{i-1}((\nabla f)(x_{i-1}))^\top\tag{7.12}$$
with $\alpha\in[0,1]$ (p. 231).
- Momentum is also useful when the gradient is only known approximately, because it averages noisy estimates (p. 231).

*Intuition note.* Momentum is a moving average of past updates (a heavy ball reluctant to change direction). This memory damps oscillations and smooths the updates.

#### 7.1.3 Stochastic gradient descent (pp. 231–232)
- A cheap approximation of the gradient is still useful if it points in roughly the same direction as the true one. SGD is a stochastic approximation of gradient descent for objectives written as a sum of differentiable functions. "Stochastic" means the gradient is known only as a noisy approximation. By constraining the distribution of the approximate gradients, convergence can still be theoretically guaranteed (p. 231).
- Typical ML objective over $N$ data points, with an example from regression (negative log-likelihood):
$$L(\theta)=\sum_{n=1}^N L_n(\theta)\tag{7.13}$$
$$L(\theta)=-\sum_{n=1}^N\log p(y_n\mid x_n,\theta)\tag{7.14}$$
- Batch gradient descent uses the full training set:
$$\theta_{i+1}=\theta_i-\gamma_i(\nabla L(\theta_i))^\top=\theta_i-\gamma_i\sum_{n=1}^N(\nabla L_n(\theta_i))^\top\tag{7.15}$$
This is expensive when the data set is enormous or no simple formulas exist (pp. 231–232).
- Mini-batch gradient descent sums over a randomly chosen subset of the $L_n$. The extreme case uses a single $L_n$ (p. 232).
- Why this is sensible (author's argument): for gradient descent to converge we only require an unbiased estimate of the true gradient. The sum in (7.15) is itself an empirical estimate of an expected value, so any other unbiased empirical estimate, e.g. from a subsample, would suffice (p. 232).
- **Remark.** If the learning rate decreases at an appropriate rate, and subject to relatively mild assumptions, SGD converges almost surely to a local minimum (Bottou, 1998) (p. 232).
- Trade-off: large mini-batches give accurate gradients with lower variance, use optimised matrix operations and give more stable convergence, but each step costs more. Small mini-batches are quick, and their noise may help escape some bad local optima. The real goal is generalisation (Ch. 8), so a precise minimum is not necessarily needed. SGD is effective in large-scale problems (pp. 232–233).

*Intuition note.* The full gradient is a sum over data points (an empirical estimate of an expected value). A random subset gives a noisy but unbiased estimate, and is cheaper to compute.

### 7.2 Constrained optimization and Lagrange multipliers (pp. 233–236)
**Problem.** With $g_i:\mathbb R^D\to\mathbb R$ ($i=1,\dots,m$):
$$\min_x f(x)\quad\text{subject to}\quad g_i(x)\le0\ \ \forall i\tag{7.17}$$
$f$ and $g_i$ may be non-convex here (p. 233).

**Indicator-function conversion.** An obvious but impractical way to remove the constraints:
$$J(x)=f(x)+\sum_{i=1}^m\mathbf 1(g_i(x)),\qquad \mathbf 1(z)=\begin{cases}0&z\le0\\\infty&\text{otherwise}\end{cases}\tag{7.18, 7.19}$$
It gives the same solution but is equally hard to optimise. Lagrange multipliers replace the step function by a linear function (pp. 233–234).

**Lagrangian** with multipliers $\lambda_i\ge0$:
$$\mathfrak L(x,\lambda)=f(x)+\sum_{i=1}^m\lambda_ig_i(x)=f(x)+\lambda^\top g(x)\tag{7.20a,b}$$
where $g(x)\in\mathbb R^m$ stacks the constraints and $\lambda\in\mathbb R^m$ (p. 234).

**Duality.** Duality converts a problem in primal variables $x$ into one in dual variables $\lambda$ (p. 234).

**Definition 7.1.** The problem (7.17) is the *primal problem*. The *Lagrangian dual problem* is
$$\max_{\lambda\in\mathbb R^m}\ \mathfrak D(\lambda)\quad\text{s.t. }\lambda\ge0,\qquad \mathfrak D(\lambda)=\min_{x\in\mathbb R^d}\mathfrak L(x,\lambda)\tag{7.22}$$
(p. 234).

**Minimax inequality** (for any $\varphi(x,y)$):
$$\max_y\min_x\varphi(x,y)\le\min_x\max_y\varphi(x,y)\tag{7.23}$$
Proof: for all $x,y$, $\min_x\varphi(x,y)\le\max_y\varphi(x,y)$ (7.24). Taking the max over $y$ on the left keeps the inequality, since it holds for all $y$. Taking the min over $x$ on the right gives (7.23) (pp. 234–235).

**Weak duality.**
- For $\lambda\ge0$, $\mathfrak L(x,\lambda)$ is a lower bound of $J(x)$, because the indicator is relaxed to a linear function. Hence
$$J(x)=\max_{\lambda\ge0}\mathfrak L(x,\lambda)\tag{7.25}$$
and the original problem is $\min_x\max_{\lambda\ge0}\mathfrak L$ (7.26) (p. 235).
- By (7.23), swapping min and max gives a smaller value:
$$\min_x\max_{\lambda\ge0}\mathfrak L(x,\lambda)\ \ge\ \max_{\lambda\ge0}\min_x\mathfrak L(x,\lambda)\tag{7.27}$$
This is weak duality: primal values are always at least dual values. The inner part of the right side is $\mathfrak D(\lambda)$ (p. 235).

**Why the dual is convenient.**
- For fixed $\lambda$, $\min_x\mathfrak L(x,\lambda)$ is unconstrained. If it is easy, the whole problem is easy (p. 235).
- $\mathfrak L$ is affine in $\lambda$, so $\mathfrak D(\lambda)$ is a pointwise minimum of affine functions. It is therefore concave even if $f$ and $g_i$ are non-convex. Maximising a concave function can be done efficiently (p. 235).
- For differentiable $f,g_i$: differentiate $\mathfrak L$ in $x$, set to zero, solve (p. 235).

*Intuition note.* The dual swaps "choose $x$ and obey the constraints" for "choose prices $\lambda$ on violations". Any prices $\lambda\ge0$ give a lower bound on the primal optimum. The dual looks for the best such bound.

**Remark (equality constraints).** For (7.28), with extra $h_j(x)=0$, replace each equality by $h_j\le0$ and $h_j\ge0$. The resulting multipliers are then unconstrained. So multipliers of the inequality constraints are constrained non-negative, and those of the equality constraints are left free (pp. 235–236).

### 7.3 Convex optimization (pp. 236–245)
- When $f$ is a convex function and the constraints involving $g$ and $h$ are convex sets, the problem is a *convex optimization problem*. Global optimality can be guaranteed, and *strong duality* holds: the optimal dual solution equals the optimal primal solution (p. 236).
- ML literature often does not strictly distinguish convex functions from convex sets (p. 236).

**Definition 7.2 (convex set).** $\mathcal C$ is convex if for any $x,y\in\mathcal C$ and $0\le\theta\le1$:
$$\theta x+(1-\theta)y\in\mathcal C\tag{7.29}$$
The line between any two elements lies inside the set (Figures 7.5, 7.6) (p. 236).

**Definition 7.3 (convex function).** $f:\mathbb R^D\to\mathbb R$ with convex domain is convex if for all $x,y$ in the domain and $0\le\theta\le1$:
$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\tag{7.30}$$
A straight line between two points of the function lies above the function. A concave function is the negative of a convex one (p. 236).

- Constraints truncate functions at a scalar value, giving sets. Filling in a convex function ("pouring water into the bowl") gives its *epigraph*, which is a convex set (p. 236).
- **Gradient test.** A differentiable $f$ is convex if and only if for all $x,y$
$$f(y)\ge f(x)+\nabla_xf(x)^\top(y-x)\tag{7.31}$$
A twice-differentiable $f$ is convex if and only if the Hessian $\nabla_x^2f(x)$ is positive semidefinite (pp. 236–237).

**Example 7.3 (negative entropy).** $f(x)=x\log_2x$ is convex for $x>0$. The author checks only the points $x=2,4$ and notes that a proof would need all points (p. 237).
- Definition 7.3 with $\theta=0.5$: left side $f(3)=3\log_23\approx4.75$. Right side $0.5(2\log_22)+0.5(4\log_24)=1+4=5$. Satisfied (p. 237).
- Gradient test: $\nabla_x(x\log_2x)=\log_2x+\frac1{\log_e2}$ (7.32). Left side of (7.31) is $f(4)=8$. Right side is $f(2)+\nabla f(2)(4-2)=2+(1+\frac1{\log_e2})\cdot2\approx6.9$ (7.33). Satisfied (p. 237).

**Closure operations.** In practice, convexity is checked with operations that preserve it, an idea of closure like that for vector spaces (Ch. 2) (p. 238).

**Example 7.4 (nonnegative sums).**
- If $f$ is convex and $\alpha\ge0$, then $\alpha f$ is convex: multiply (7.30) by $\alpha$; a nonnegative factor does not change the inequality.
- For convex $f_1,f_2$, add the two inequalities (7.34), (7.35):
$$f_1(\theta x+(1-\theta)y)+f_2(\theta x+(1-\theta)y)\le\theta f_1(x)+(1-\theta)f_1(y)+\theta f_2(x)+(1-\theta)f_2(y)\tag{7.36}$$
The right side equals $\theta(f_1(x)+f_2(x))+(1-\theta)(f_1(y)+f_2(y))$ (7.37). So $f_1+f_2$ is convex.
- Hence $\alpha f_1+\beta f_2$ is convex for $\alpha,\beta\ge0$, and this extends to more functions (p. 238).

**Remark.** (7.30) is sometimes called Jensen's inequality, and a whole class of inequalities for nonnegative weighted sums of convex functions share this name (p. 239).

**Summary form** (7.38): the problem is convex if $f$ and all $g_i$ are convex functions and all $h_j(x)=0$ are convex sets (p. 239).

*Intuition note.* In a convex problem the objective is a single bowl and the feasible region has no dents. So every local minimum is global and the start-point dependence of Figure 7.2 does not arise; strong duality also holds.

#### 7.3.1 Linear programming (p. 239)
$$\min_{x\in\mathbb R^d}c^\top x\quad\text{s.t. }Ax\le b\tag{7.39}$$
with $A\in\mathbb R^{m\times d}$, $b\in\mathbb R^m$, $c\in\mathbb R^d$: $d$ variables, $m$ constraints.
- Lagrangian with $\lambda\in\mathbb R^m$, $\lambda\ge0$:
$$\mathfrak L(x,\lambda)=c^\top x+\lambda^\top(Ax-b)\tag{7.40}$$
$$=(c+A^\top\lambda)^\top x-\lambda^\top b\tag{7.41}$$
- Derivative in $x$ set to zero: $c+A^\top\lambda=0$ (7.42). So $\mathfrak D(\lambda)=-\lambda^\top b$.
- Dual problem:
$$\max_{\lambda\in\mathbb R^m}-b^\top\lambda\quad\text{s.t. }c+A^\top\lambda=0,\ \lambda\ge0\tag{7.43}$$
This is a linear program with $m$ variables. We may solve primal or dual, depending on whether $m$ or $d$ is larger (pp. 239–240).

**Example 7.5.** Minimise $-[5,3]x$ subject to rows $(2,2)\le33$, $(2,-4)\le8$, $(-2,1)\le5$, $(0,-1)\le-1$, $(0,1)\le8$ (7.44). The optimum lies in the feasible region in Figure 7.9 (p. 240).

#### 7.3.2 Quadratic programming (pp. 241–242)
$$\min_{x\in\mathbb R^d}\tfrac12x^\top Qx+c^\top x\quad\text{s.t. }Ax\le b\tag{7.45}$$
with $Q\in\mathbb R^{d\times d}$ symmetric positive definite (so the objective is convex), $A\in\mathbb R^{m\times d}$, $b\in\mathbb R^m$, $c\in\mathbb R^d$ (p. 241).

**Example 7.6.** $Q=\begin{bmatrix}2&1\\1&4\end{bmatrix}$, $c=[5,3]^\top$ (7.46), with the box constraints $x_1\le1$, $-x_1\le1$, $x_2\le1$, $-x_2\le1$ (7.47) (Figure 7.4) (p. 241).

**Derivation of the dual.**
$$\mathfrak L(x,\lambda)=\tfrac12x^\top Qx+c^\top x+\lambda^\top(Ax-b)=\tfrac12x^\top Qx+(c+A^\top\lambda)^\top x-\lambda^\top b\tag{7.48a,b}$$
$$Qx+(c+A^\top\lambda)=0\tag{7.49}$$
$$x=-Q^{-1}(c+A^\top\lambda)\tag{7.50}$$
($Q$ is positive definite, hence invertible). Substituting into $\mathfrak L$:
$$\mathfrak D(\lambda)=-\tfrac12(c+A^\top\lambda)^\top Q^{-1}(c+A^\top\lambda)-\lambda^\top b\tag{7.51}$$
$$\max_{\lambda\in\mathbb R^m}-\tfrac12(c+A^\top\lambda)^\top Q^{-1}(c+A^\top\lambda)-\lambda^\top b\quad\text{s.t. }\lambda\ge0\tag{7.52}$$
(pp. 241–242). Chapter 12 gives an ML application (p. 242).

#### 7.3.3 Legendre–Fenchel transform and convex conjugate (pp. 242–245)
**Motivation** (author's chain of ideas):
- A convex set can be described by its supporting hyperplanes. A hyperplane is supporting if it intersects the set and the set lies on one side of it.
- A convex function's epigraph is a convex set, so the function is described by its supporting hyperplanes. These are tangents, determined by the gradient.
- So a convex function can be described by a function of its gradient. The Legendre transform formalises this (p. 242).
- The Legendre–Fenchel transform (convex conjugate) maps a convex differentiable $f(x)$ to a function of the tangent slopes $s=\nabla_xf(x)$. It transforms the function $f(\cdot)$, not the variable $x$ (p. 242). Marginal note: physics students meet the Legendre transform as relating the Lagrangian and the Hamiltonian.

**Definition 7.4.** The convex conjugate of $f:\mathbb R^D\to\mathbb R$ is
$$f^*(s)=\sup_{x\in\mathbb R^D}\big(\langle s,x\rangle-f(x)\big)\tag{7.53}$$
The definition does not need $f$ to be convex or differentiable. The text uses $\langle s,x\rangle=s^\top x$ from here on (pp. 242–243).

**Geometric derivation** (for $f(x)=x^2$, 1-D):
- Fix a slope $s$. The line through $(x_0,f(x_0))$ with slope $s$ is $y-f(x_0)=s(x-x_0)$ (7.54). Its intercept is $-sx_0+f(x_0)$.
- The smallest $c$ with $y=sx+c$ touching the graph is $\inf_{x_0}\,-sx_0+f(x_0)$ (7.55).
- The conjugate is by convention the negative of this. The author says the reasoning does not rely on the 1-D, convex, differentiable choice (p. 243).

**Remark (smooth convex case).**
- At $x_0$ the tangent touches: $f(x_0)=sx_0+c$ (7.56), with $s=\nabla_xf(x_0)$.
- So $-c=sx_0-f(x_0)$ (7.57). Since $-c$ varies with $x_0$ and hence with $s$, define
$$f^*(s):=sx_0-f(x_0)\tag{7.58}$$
This is Definition 7.4 without the supremum, and is one-to-one with $f$ (p. 243).

For convex $f$, applying the transform again returns $f$. The slope of $f$ is $s$ and the slope of $f^*(s)$ is $x$ (pp. 243–244).

*Intuition note.* Describe a curve not by points $(x,f(x))$ but by "for each slope $s$, how low can a line of that slope sit under the curve". The negated intercept, as a function of $s$, is $f^*$.

**Example 7.7.** For $f(y)=\frac\lambda2y^\top K^{-1}y$ with $K\in\mathbb R^{n\times n}$ positive definite, primal $y\in\mathbb R^n$, dual $\alpha\in\mathbb R^n$:
$$f^*(\alpha)=\sup_y\langle y,\alpha\rangle-\tfrac\lambda2y^\top K^{-1}y\tag{7.60}$$
$$\frac{\partial[\dots]}{\partial y}=(\alpha-\lambda K^{-1}y)^\top\tag{7.61}$$
Setting to zero gives $y=\frac1\lambda K\alpha$. Substituting:
$$f^*(\alpha)=\tfrac1\lambda\alpha^\top K\alpha-\tfrac\lambda2\left(\tfrac1\lambda K\alpha\right)^{\!\top}K^{-1}\left(\tfrac1\lambda K\alpha\right)=\tfrac1{2\lambda}\alpha^\top K\alpha\tag{7.62}$$
(p. 244).

**Example 7.8 (sum of separable losses).** For $\mathcal L(t)=\sum_{i=1}^n\ell_i(t_i)$:
$$\mathcal L^*(z)=\sup_t\langle z,t\rangle-\sum_i\ell_i(t_i)=\sup_t\sum_iz_it_i-\ell_i(t_i)=\sum_i\sup_{t_i}\,z_it_i-\ell_i(t_i)=\sum_i\ell_i^*(z_i)\tag{7.63a–d}$$
The author writes the supremum in (7.63c) over $t\in\mathbb R^n$. (added step) Because each term depends only on $t_i$, the supremum splits into $n$ one-variable suprema (pp. 244–245).

**Link to Lagrange duality.** For convex problems we have strong duality. The Legendre–Fenchel transform can also derive a dual problem. For convex differentiable functions the supremum is unique (p. 245).

**Example 7.9.** Let $f(y)$, $g(x)$ be convex and $Ax=y$. Then
$$\min_xf(Ax)+g(x)=\min_{Ax=y}f(y)+g(x)\tag{7.64}$$
Introduce a multiplier $u$ for $Ax=y$:
$$\min_{Ax=y}f(y)+g(x)=\min_{x,y}\max_uf(y)+g(x)+(Ax-y)^\top u=\max_u\min_{x,y}f(y)+g(x)+(Ax-y)^\top u\tag{7.65a,b}$$
The swap of max and min is justified by convexity of $f$ and $g$ (author's statement). Split the dot-product term and collect $x$ and $y$:
$$=\max_u\Big[\min_y-y^\top u+f(y)\Big]+\Big[\min_xx^\top A^\top u+g(x)\Big]\tag{7.66}$$
By Definition 7.4, $\min_y(-y^\top u+f(y))=-f^*(u)$ and $\min_x(x^\top A^\top u+g(x))=-g^*(-A^\top u)$ (added step: signs from negating the supremum). So
$$\max_u-f^*(u)-g^*(-A^\top u)\tag{7.67b}$$
$$\min_xf(Ax)+g(x)=\max_u-f^*(u)-g^*(-A^\top u)\tag{7.68}$$
For general inner products, $A^\top$ is replaced by the adjoint $A^*$ (marginal note) (p. 245).

**Use in ML** (author's closing claim). The conjugate is useful for ML problems that are convex optimisation problems. For convex losses applied independently to each example, the conjugate loss is a convenient way to derive a dual problem (p. 246).

### 7.4 Further reading (p. 246–247)
Pointers only, as listed by the authors:
- Two weaknesses of gradient descent. (1) It is first-order and ignores curvature. Remedies named: acceleration methods (Nesterov), conjugate gradient, Newton methods (Hessian), quasi-Newton such as L-BFGS, mirror descent, natural gradient. (2) It needs differentiability. Subgradient methods are named for functions with kinks.
- SGD is "the current workhorse of large-scale machine learning methods" (p. 246).
- For duality and convex optimisation: Boyd and Vandenberghe (2004), Bertsekas (2009), Nesterov (2018). For convex analysis: Rockafellar (1970) and others. A beginner-friendly Legendre–Fenchel text: Zia et al. (2009) (pp. 246–247).

## Toy example
*(Ours, not from the text.)*

**(a) Gradient descent and step-size.** Minimise $f(x)=x^2$, so $f'(x)=2x$ and $x_{i+1}=x_i-\gamma\,2x_i$. Start at $x_0=3$.
- $\gamma=0.25$: gradient $6$, so $x_1=3-0.25\cdot6=1.5$. Gradient $3$, so $x_2=1.5-0.75=0.75$. Values: $f=9,\ 2.25,\ 0.5625$. Decreasing, as (7.5) promises.
- $\gamma=1.25$: $x_1=3-1.25\cdot6=-4.5$, $f=20.25>9$. The next gradient is $-9$, so $x_2=-4.5+11.25=6.75$, $f=45.56$. The iterates overshoot and diverge. By the first heuristic of Sec. 7.1.1 we would undo the step and shrink $\gamma$.

**(b) Lagrangian dual.** Minimise $x^2$ subject to $g(x)=1-x\le0$. The primal optimum is $x=1$, value $1$.
- $\mathfrak L(x,\lambda)=x^2+\lambda(1-x)$. Setting $\partial_x\mathfrak L=2x-\lambda=0$ gives $x=\lambda/2$.
- $\mathfrak D(\lambda)=\lambda^2/4+\lambda-\lambda^2/2=\lambda-\lambda^2/4$. This is concave.
- Weak duality check at $\lambda=1$: $\mathfrak D=0.75\le1$.
- Maximise: $1-\lambda/2=0$ gives $\lambda=2$, $\mathfrak D(2)=2-1=1$. This equals the primal value, as strong duality predicts for this convex problem.

## Concepts
- [[gradient-descent]] (new) — iterate $x_{i+1}=x_i-\gamma_i(\nabla f(x_i))^\top$ to reach a local minimum (p. 228)
- [[step-size]] (new) — the factor $\gamma$ (learning rate); too small is slow, too large may diverge (p. 229)
- [[momentum]] (new) — gradient update with memory, $\alpha\Delta x_i$ added, dampening oscillations (p. 231)
- [[stochastic-gradient-descent]] (new) — gradient descent with an unbiased estimate from a data subset (pp. 231–232)
- [[condition-number]] — here $\sigma_{\max}/\sigma_{\min}$ of $A$, governs gradient-descent speed on $Ax=b$ (p. 230)
- [[preconditioner]] (new) — a matrix $P$ chosen so that $P^{-1}A$ is better conditioned (p. 230)
- [[lagrangian-and-multipliers]] (new) — $\mathfrak L=f+\lambda^\top g$ with $\lambda\ge0$ for inequality constraints (p. 234)
- [[lagrangian-duality]] (new) — primal $\min_x$ versus dual $\max_{\lambda\ge0}\min_x\mathfrak L$ (p. 234)
- [[weak-strong-duality]] (new) — primal ≥ dual in general (7.27); equal for convex problems (pp. 235–236)
- [[minimax-inequality]] (new) — $\max_y\min_x\varphi\le\min_x\max_y\varphi$ (p. 234)
- [[convex-set-function]] (new) — segment conditions (7.29), (7.30); also gradient and Hessian tests (pp. 236–237)
- [[linear-and-quadratic-program]] (new) — convex problems with affine constraints and linear or quadratic objective (pp. 239, 241)
- [[convex-conjugate]] (new) — $f^*(s)=\sup_x(\langle s,x\rangle-f(x))$; Legendre–Fenchel transform (p. 242)
- [[positive (semi)definite matrix]] — Hessian psd iff $f$ convex; $Q$ pd in QPs (pp. 237, 241)
- [[dot (inner) product]] — used in conjugate definition (p. 243)

## Canonical instances
- [[quartic-1d-example]] — $\ell(x)=x^4+7x^3+5x^2-17x+3$: local versus global minimum, start-point dependence (p. 225–227)
- [[quadratic-gd-example]] — Example 7.1: gradient descent on a 2-D quadratic, zigzag (pp. 228–229)
- [[least-squares-via-gd]] — Example 7.2: solving $Ax=b$ by minimising $\|Ax-b\|^2$ (p. 230)
- [[negative-entropy-convexity]] — Example 7.3: $x\log_2x$ checked against (7.30) and (7.31) (p. 237)
- [[lp-example]] / [[qp-example]] — Examples 7.5, 7.6 with Figures 7.9, 7.4 (pp. 240–241)
- [[quadratic-conjugate]] — Example 7.7: $f^*(\alpha)=\frac1{2\lambda}\alpha^\top K\alpha$ (p. 244)

## Bridges (candidates)
- [same-math] condition number $\sigma_{\max}/\sigma_{\min}$ ↔ linear-algebra: condition number from the SVD — same quantity, here controlling gradient-descent speed.
- [same-math] QP dual via $x=-Q^{-1}(c+A^\top\lambda)$ ↔ linear-algebra: solving a positive-definite linear system from a quadratic form.
- [structural-analogy] momentum as moving average ↔ time-series: exponential smoothing of past updates.
- [structural-analogy] closure of convexity under nonnegative sums ↔ linear-algebra: closure of vector spaces (the author draws this parallel, p. 238).
- [metaphor] convex conjugate as "transform of a function" ↔ signal analysis: Fourier transform (author's "in the sense of a Fourier transform", p. 242).

## Questions this raises
- How do second-order methods (Newton, L-BFGS) use curvature to avoid zigzagging, and when is their extra cost worth it?
- When does strong duality fail, if the problem is not convex? (The chapter only states the convex case.)
- What exactly does "appropriate rate" of decreasing learning rate mean for SGD convergence?
- How does the preconditioner $P$ relate to the Hessian's eigenvalues?

## Exercises worth doing
- Ex. 7.1 (p. 247) — stationary points of a cubic and second-derivative test — difficulty: easy
- Ex. 7.3 (p. 247) — which set operations preserve convexity — difficulty: easy
- Ex. 7.4 (p. 247) — which function operations preserve convexity — difficulty: medium
- Ex. 7.6 (p. 247) — dual of the LP of Figure 7.9 via Lagrange duality — difficulty: medium
- Ex. 7.8 (p. 248) — Lagrangian dual of a minimum-norm problem — difficulty: medium
- Ex. 7.10 (p. 248) — convex conjugate of a general quadratic — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 6 (pdf 231 = printed 225). Page labels give printed numbers directly.
- Footer shows "©2024 … Published by Cambridge University Press (2020)" and "Draft (2024-01-15)" on alternating pages.
- Example 7.6 (p. 241) calls $Q$ "positive semidefinite", while the text above it requires $Q$ positive definite. The given $Q=\begin{bmatrix}2&1\\1&4\end{bmatrix}$ has $\det=7>0$ and positive trace, so it is positive definite. The word "semidefinite" appears to be loose wording.
- (7.63c) in the extracted text puts the supremum over $t\in\mathbb R^n$ for each $i$. In our reading it is effectively over $t_i$ alone, since each term depends only on $t_i$.
- In (7.66b) the image shows "min$(Ax)^\top u+g(x)$", then (7.66c) rewrites it as $x^\top A^\top u$. This is consistent.
- Figures 7.1–7.9 are images. Only their captions and visible axes were used.
- The chapter's exercise solutions are not printed in these pages.
