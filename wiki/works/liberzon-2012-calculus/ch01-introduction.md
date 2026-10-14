---
id: liberzon-2012-calculus/ch01-introduction
work: liberzon-2012-calculus
unit: Chapter 1 — Introduction
pages: 1-20
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Introduction (optimal control problem; finite-dimensional optimization; preview of infinite-dimensional optimization)

## L0 — One line
Optimal control means minimizing a cost functional over control functions; this chapter prepares for it by showing, first for $f:\mathbb R^n\to\mathbb R$ and then for functionals, how perturbing a candidate minimum along a one-parameter family reduces the question to ordinary calculus on a scalar function $g(\alpha)$.

## L1 — The gist (≤ 120 words)
This chapter states the problem the book will solve: choose a control function $u$ that minimizes a cost functional $J(u)$ (a number assigned to each function) for a system $\dot x=f(t,x,u)$. It then reviews finite-dimensional optimization: first- and second-order conditions (using the gradient and Hessian), Lagrange multipliers for equality constraints, and convexity. Finally it previews the same ideas for functionals on infinite-dimensional function spaces, through the first and second variation (derivatives of a functional). Two differences appear: the choice of norm (a measure of distance) matters, and the unit sphere is not compact. With this chapter's definitions, no general second-order sufficient condition follows. Later chapters return to some of these ideas.

**Prerequisites:** multivariable calculus (gradient, Hessian, chain rule, Taylor expansion); linear independence; positive (semi)definite matrices; basic compactness; ODE notation.

## L2 — Key ideas (5–10 bullets)
- An optimal control problem has two ingredients: an ODE control system (1.1) and a cost functional $J$ (1.2) that assigns a cost to each admissible control. The task is to minimize $J$ (pp. 1–2).
- The book follows history: calculus of variations (infinite-dimensional, not dynamic) first, then optimal control built on the maximum principle and dynamic programming (p. 3).
- Unconstrained local minimum of $C^1$ $f$ at an interior point $\Rightarrow$ $\nabla f(x^*)=0$. If $f\in C^2$, also $\nabla^2f(x^*)\ge0$. $\nabla f=0$ together with $\nabla^2 f>0$ is sufficient for a strict local minimum (pp. 3–6).
- With equality constraints and a regular point, $\nabla f(x^*)+\sum\lambda_i^*\nabla h_i(x^*)=0$ (1.25). The augmented cost $\ell$ turns this into an unconstrained stationary-point condition, though there is no quick way to derive (1.25) from the augmented cost, which Lagrange originally attempted (pp. 9–13).
- For convex $D$ and convex $f$, a local minimum is global and the first-order condition is sufficient (p. 8). The same holds for convex functionals (p. 19).
- In function spaces, "close" depends on the norm, and different norms give very different notions of closeness (p. 14). Local minima are defined with $\varepsilon$-balls in a chosen norm (p. 15).
- The first variation $\delta J|_y$ (Gateaux derivative) is defined by (1.33). If the first variation exists, a local minimum forces $\delta J|_{y^*}(\eta)=0$ for admissible $\eta$ (1.37); with the second variation, also $\delta^2J|_{y^*}(\eta)\ge0$ (1.40) (pp. 16–18).
- The finite-dimensional sufficiency proof breaks down in infinite dimensions, because the unit sphere is not compact. With the chapter's definitions there is no general second-order sufficient condition (pp. 18–19).

## L3 — Walkthrough

### 1.1 Optimal control problem (pp. 1–3)
- Control system: $\dot x=f(t,x,u),\ x(t_0)=x_0$ (1.1). Here $x\in\mathbb R^n$ is the state, $u\in U\subset\mathbb R^m$ is the control input, $t_0$ is the initial time, $x_0$ the initial state (p. 1).
- Cost functional (a real-valued function on a space of functions):
$$J(u):=\int_{t_0}^{t_f}L(t,x(t),u(t))\,dt+K(t_f,x_f)\tag{1.2}$$
$L$ is the running cost, $K$ the terminal cost. $t_f$ may be free or fixed; $x_f=x(t_f)$ may be free, fixed or in a target set (p. 1).
- Problem: find a control $u$ minimizing $J(u)$ over all admissible controls, or at least over nearby controls. Regularity conditions and precise versions come later (Section 3.3) (p. 1).
- The author says it "can be argued" that optimality is a universal principle of life, in the sense that many—if not most—processes in nature are governed by solutions to optimization problems (although we may never know what is optimized). Applications listed: rocket to the moon with minimal fuel; chemical production in minimal time or catalyst; advertising cost for a sales target; throughput or accuracy of a communication channel (p. 2).
- **Example 1.1 (car).** Position $x\in\mathbb R$, acceleration $u$ as control, $U=[-1,1]$, dynamics $\ddot x=u$. Put $x_1=x$, $x_2=\dot x$, so $\dot x_1=x_2,\ \dot x_2=u$ with state in $\mathbb R^2$. "Park" the car at the origin (at rest) in minimal time: $L\equiv1$, $K\equiv0$, fixed final state $(0,0)^T$. It is solved in Section 4.4.1 (p. 2).
- The problem can be seen as choosing the best path among feasible paths. It is infinite-dimensional (the space of paths is a function space) and dynamic (it involves a dynamical system and time). Hence first recall static finite-dimensional optimization (p. 2).
- Plan: calculus of variations first (infinite-dimensional, not dynamic), then optimal control, based on the maximum principle and dynamic programming. These were initially independent and are ultimately closely related and complementary (p. 3).

### 1.2 Finite-dimensional optimization (pp. 3–14)
**Definitions (p. 3).** $f:\mathbb R^n\to\mathbb R$, $D\subset\mathbb R^n$, $|\cdot|$ the Euclidean norm.
- $x^*\in D$ is a *local minimum* of $f$ over $D$ if there is $\varepsilon>0$ with $f(x^*)\le f(x)$ for all $x\in D$ with $|x-x^*|<\varepsilon$ (1.3). Only points of $D$ matter.
- *Strict* if the inequality is strict for $x\ne x^*$. *Global* if (1.3) holds for all $x\in D$. "Minimum" by default means local minimum. A minimum need not be unique unless it is both strict and global.
- Maxima of $f$ are minima of $-f$, so only minima are treated. A point that is a maximum or a minimum is an *extremum*.

**1.2.1 Unconstrained optimization (pp. 3–8).** Here $x^*$ is an interior point of $D$ (automatic if $D$ is open). Then $x^*+\alpha d\in D$ for all $d$ and all $\alpha$ near 0 (p. 3).

*First-order necessary condition.* Let $f\in C^1$ and $x^*$ a local minimum.
1. Define $g(\alpha):=f(x^*+\alpha d)$ (1.4). Then $0$ is a minimum of $g$ (p. 4).
2. Taylor: $g(\alpha)=g(0)+g'(0)\alpha+o(\alpha)$ (1.5), with $\lim_{\alpha\to0}o(\alpha)/\alpha=0$ (1.6) (p. 4).
3. Claim $g'(0)=0$ (1.7). Suppose $g'(0)\ne0$. By (1.6) there is $\varepsilon>0$ such that $|\alpha|<\varepsilon\Rightarrow|o(\alpha)|<|g'(0)\alpha|$. Then $g(\alpha)-g(0)<g'(0)\alpha+|g'(0)\alpha|$ (1.8). For $\alpha$ of sign opposite to $g'(0)$ the right side is 0, so $g(\alpha)<g(0)$, a contradiction (p. 4).
4. Chain rule: $g'(\alpha)=\nabla f(x^*+\alpha d)\cdot d$ (1.9), with $\nabla f=(f_{x_1},\dots,f_{x_n})^T$ (a column vector by the author's convention). So $g'(0)=\nabla f(x^*)\cdot d=0$ (1.10) (p. 4).
5. Since $d$ is arbitrary:
$$\nabla f(x^*)=0\tag{1.11}$$
A point satisfying it is *stationary*. Valid for $f\in C^1$ and $x^*$ interior (p. 4).

> **Intuition note.** If the slope along a line through $x^*$ were nonzero, one could step downhill on one side. So a minimum has zero slope in every direction, i.e. zero gradient. The same argument applies to maxima.

*Second-order conditions* ($f\in C^2$; pp. 5–6).
1. Expand further: $g(\alpha)=g(0)+g'(0)\alpha+\tfrac12g''(0)\alpha^2+o(\alpha^2)$ (1.12), with $o(\alpha^2)/\alpha^2\to0$ (1.13). Here $g'(0)=0$ by (1.11) (p. 5).
2. Claim $g''(0)\ge0$ (1.14). If $g''(0)<0$, for small $|\alpha|$ we have $|o(\alpha^2)|<\tfrac12|g''(0)|\alpha^2$, so $g(\alpha)-g(0)<0$, a contradiction (p. 5).
3. Differentiate $g'(\alpha)=\sum_i f_{x_i}(x^*+\alpha d)d_i$ to get $g''(\alpha)=\sum_{i,j}f_{x_ix_j}(x^*+\alpha d)d_id_j$. At $\alpha=0$: $g''(0)=d^T\nabla^2f(x^*)d$ (1.15), with $\nabla^2f=(f_{x_ix_j})$ the $n\times n$ Hessian (pp. 5–6).
4. Since $d$ is arbitrary, $\nabla^2f(x^*)\ge0$ (positive semidefinite) is the **second-order necessary condition**. It needs $f\in C^2$. Unlike the first-order condition it distinguishes minima from maxima (at a maximum the Hessian is negative semidefinite) (p. 6).
5. **Second-order sufficient condition:** if $f\in C^2$, $x^*$ is interior and
$$\nabla f(x^*)=0\quad\text{and}\quad\nabla^2f(x^*)>0\ \text{(positive definite)}\tag{1.16}$$
then $x^*$ is a strict local minimum. Proof: (1.12) gives $f(x^*+\alpha d)=f(x^*)+\tfrac12d^T\nabla^2f(x^*)d\,\alpha^2+o(\alpha^2)$ (1.17). Pick $\varepsilon$ so that $|\alpha|<\varepsilon,\alpha\ne0\Rightarrow|o(\alpha^2)|<\tfrac12d^T\nabla^2f(x^*)d\,\alpha^2$. Then $f(x^*+\alpha d)>f(x^*)$ (p. 6).
6. Technical step: $\varepsilon$ depends on $d$ (continuously). Restrict $d$ to unit length and take the minimum of $\varepsilon$ over the unit sphere. This is well defined because the sphere is compact (Weierstrass Theorem). That minimum is the radius of the required ball (p. 6).

> **Intuition note.** With zero slope, the curvature decides: if the Hessian is positive definite, the quadratic term beats the leftover terms and the point is a bowl bottom. Compactness is what lets one choose one ball that works for all directions at once; this is the step that fails later in infinite dimensions.

*Feasible directions (pp. 6–7).* If $x^*$ is on the boundary of $D$, $d$ is a *feasible direction* at $x^*$ if $x^*+\alpha d\in D$ for small enough $\alpha>0$ (Fig. 1.1). Then $\nabla f(x^*)=0$ is no longer necessary, and the proof of (1.7) fails because $\alpha\ge0$. The reader is left to show that a local minimum has $\nabla f(x^*)\cdot d\ge0$ for every feasible direction. If $g'(0)=0$ then (1.14) still holds, so $d^T\nabla^2f(x^*)d\ge0$ for feasible $d$ with $\nabla f(x^*)\cdot d=0$ (p. 7). The approach suits convex $D$; for nonconvex $D$ these conditions are conservative (p. 7). With equality constraints there may be no feasible directions, so the conditions are vacuous (p. 7).

*Global minima (pp. 7–9).*
- **Weierstrass Theorem:** if $f$ is continuous and $D$ compact, a global minimum of $f$ over $D$ exists. In $\mathbb R^n$, compactness has three equivalent definitions: (1) closed and bounded; (2) every open cover has a finite subcover; (3) every sequence has a subsequence converging in $D$ (pp. 7–8).
- Search procedure: find interior stationary points; add points where $\nabla f$ does not exist (together, the *critical points*); find boundary points with $\nabla f\cdot d\ge0$ for all feasible $d$; compare values and take the smallest. Second-order conditions can refine this (p. 8).
- If $D$ and $f$ are convex: a local minimum is automatically global; the first-order condition (for $f\in C^1$) is also sufficient, so interior $\nabla f(x^*)=0$ gives a global minimum. This follows because the graph of a convex $f$ lies above its linear approximation $f(x^*)+\nabla f(x^*)\cdot(x-x^*)$ (Fig. 1.3) (p. 8). Steepest descent converges to stationary points, and to global minima for convex problems (pp. 8–9).

**1.2.2 Constrained optimization (pp. 9–14).** $D=\{x:h_1(x)=\dots=h_m(x)=0\}$ (1.18), $h_i\in C^1$, $f\in C^1$ (p. 9).

*First-order necessary condition (Lagrange multipliers), geometric proof.* Let $x^*$ be a local minimum over $D$ and a *regular point* (the $\nabla h_i(x^*)$ are linearly independent).
1. Use $C^1$ curves $x(\alpha)\in D$ with $x(0)=x^*$ and $g(\alpha):=f(x(\alpha))$. As before $g'(0)=0$, and $g'(0)=\nabla f(x^*)\cdot x'(0)=0$ (1.19). $x'(0)$ is a tangent vector, living in the tangent space $T_{x^*}D$ (p. 9).
2. From $h_i(x(\alpha))=0$, differentiating gives $\nabla h_i(x^*)\cdot x'(0)=0$ for all $i$ (p. 9).
3. The converse (not proved here; relies on regularity): every $d$ with $\nabla h_i(x^*)\cdot d=0$ for all $i$ (1.20) is a tangent vector for some curve. So $T_{x^*}D$ is exactly the set of such $d$, a subspace of $\mathbb R^n$ (p. 10).
4. Hence (1.21): $\nabla f(x^*)\cdot d=0$ for all $d$ with $\nabla h_i(x^*)\cdot d=0$, $i=1,\dots,m$ (p. 10).
5. **Claim (1.22):** $\nabla f(x^*)\in\mathrm{span}\{\nabla h_i(x^*)\}$. Proof by contradiction: otherwise there is $d\ne0$ with $\nabla h_i(x^*)\cdot d=0$ (1.23) and $\nabla f(x^*)=d-\sum_i\lambda_i^*\nabla h_i(x^*)$ (1.24). Taking the inner product with $d$ gives $\nabla f(x^*)\cdot d=d\cdot d\ne0$, contradicting (1.21) (pp. 10–11).
6. Equivalently, there are $\lambda_i^*$ with
$$\nabla f(x^*)+\lambda_1^*\nabla h_1(x^*)+\dots+\lambda_m^*\nabla h_m(x^*)=0\tag{1.25}$$
The $\lambda_i^*$ are *Lagrange multipliers* (p. 11). Geometrically, $\nabla f(x^*)$ is normal to $D$ at $x^*$ (Fig. 1.5) (p. 11).

> **Intuition note.** At a constrained minimum, $f$ cannot decrease along any direction that stays on the surface. So the gradient of $f$ must point entirely "off the surface", i.e. be a combination of the constraint gradients.

*Alternative analytic proof ($m=1$; pp. 12).* Given $d_1,d_2$, define $F:\mathbb R^2\to\mathbb R^2$, $F(\alpha_1,\alpha_2)=\big(f(x^*+\alpha_1d_1+\alpha_2d_2),\,h(x^*+\alpha_1d_1+\alpha_2d_2)\big)$. Its Jacobian at $(0,0)$ is the $2\times2$ matrix
$$\begin{pmatrix}\nabla f(x^*)\cdot d_1&\nabla f(x^*)\cdot d_2\\ \nabla h(x^*)\cdot d_1&\nabla h(x^*)\cdot d_2\end{pmatrix}\tag{1.26}$$
If it were nonsingular, the Inverse Function Theorem would make $F$ a bijection near $(0,0)$, giving points with $h(x)=0$ and $f(x)<f(x^*)$ arbitrarily near $x^*$. That contradicts local minimality, so (1.26) is singular. Regularity means $\nabla h(x^*)\ne0$. Choose $d_1$ with $\nabla h(x^*)\cdot d_1\ne0$ and set $\lambda^*:=-(\nabla f(x^*)\cdot d_1)/(\nabla h(x^*)\cdot d_1)$. Since (1.26) must be singular for every choice of $d_2$, and its second row is nonzero by the choice of $d_1$, the first row is a constant multiple of the second, so $(\nabla f(x^*)+\lambda^*\nabla h(x^*))\cdot d_2=0$ for all $d_2$. Hence $\nabla f(x^*)+\lambda^*\nabla h(x^*)=0$ (p. 12). (1.25) plus (1.18) are $n+m$ equations in $n+m$ unknowns ($x^*$ and $\lambda^*$). For $m=0$ this is (1.11) (p. 12).

*Augmented cost (pp. 13).* $\ell(x,\lambda):=f(x)+\sum_{i=1}^m\lambda_ih_i(x)$ (1.27). If $x^*$ is a constrained local minimum and $\lambda^*$ satisfies (1.25), then
$$\nabla\ell(x^*,\lambda^*)=\begin{pmatrix}\ell_x\\ \ell_\lambda\end{pmatrix}=\begin{pmatrix}\nabla f(x^*)+\sum_i\lambda_i^*\nabla h_i(x^*)\\ h(x^*)\end{pmatrix}=0\tag{1.28}$$
So $(x^*,\lambda^*)$ is an ordinary stationary point of $\ell$. Lagrange's idea was to minimize $\ell$ without constraints. If $(x^*,\lambda^*)$ minimizes $\ell$, then $h(x^*)=0$ and $x^*$ minimizes $f$ on $D$. However, it does *not* follow that (1.28) is necessary for a constrained minimum, and there is no quick way to derive (1.25) from the augmented cost, which Lagrange originally attempted (p. 13). The Lagrange-multiplier condition (1.25) is only necessary, not sufficient, but useful for narrowing candidates (p. 13).

*Second-order conditions (stated for completeness, not used later; pp. 13–14).* With $f\in C^2$ and $\ell_{xx}(x^*,\lambda^*)=\nabla^2f(x^*)+\sum_i\lambda_i^*\nabla^2h_i(x^*)$:
- Necessary (regular point, local minimum): $d^T\ell_{xx}d\ge0$ for all $d\in T_{x^*}D$. This is weaker than positive semidefiniteness on all of $\mathbb R^n$.
- Sufficient: if (1.25) holds and
$$d^T\ell_{xx}(x^*,\lambda^*)d>0\quad\forall d\ \text{with}\ \nabla h_i(x^*)\cdot d=0,\ i=1,\dots,m\tag{1.29}$$
then $x^*\in D$ is a strict constrained local minimum. Regularity is not needed here. If $x^*$ is regular, (1.29) says $\ell_{xx}$ is positive definite on $T_{x^*}D$.

### 1.3 Preview of infinite-dimensional optimization (pp. 14–19)
Replace $\mathbb R^n$ by a vector space $V$ of functions. A generic element is $y$, its argument is $x$ (unrelated to the earlier $x\in\mathbb R^n$). The real-valued function $J:V\to\mathbb R$ is a *functional*. There is no universal function space, so $V$ is part of the problem. Local minima need a norm to define closeness, and in function spaces different norms give drastically different notions of closeness, while in $\mathbb R^n$ all norms are equivalent (p. 14).

**1.3.1 Function spaces, norms, local minima (pp. 14–15).**
- Spaces of functions $[a,b]\to\mathbb R^n$: $C^k$ ($k$ times continuously differentiable; $C^0$ = continuous), piecewise continuous, measurable, $C^\infty$, real analytic. They are infinite-dimensional vector spaces: for example the monomials $1,x,x^2,\dots$ are linearly independent (p. 15).
- A *norm* $\|\cdot\|$ is positive definite ($\|y\|>0$ if $y\not\equiv0$), homogeneous ($\|\lambda y\|=|\lambda|\|y\|$) and satisfies the triangle inequality. It gives the metric $d(y,z)=\|y-z\|$ (p. 15).
- Norms: $\|y\|_0:=\max_{a\le x\le b}|y(x)|$ (1.30), extended by sup; $\|y\|_1:=\max|y(x)|+\max|y'(x)|$ (1.31) on $C^1$; $\|y\|_{L_p}:=\big(\int_a^b|y(x)|^p dx\big)^{1/p}$ (1.32), $p$ a positive integer; the 0-norm is also the $L_\infty$ norm (p. 15).
- **Local minimum of a functional:** $y^*\in A\subset V$ is a local minimum of $J$ over $A$ if there is $\varepsilon>0$ such that $J(y^*)\le J(y)$ for all $y\in A$ with $\|y-y^*\|<\varepsilon$. Analogy: $x\mapsto y$, $D\mapsto A$, $f\mapsto J$, $|\cdot|\mapsto\|\cdot\|$ (p. 15).
- Typically the 0-norm on $C^0$ or the 1-norm on $C^1$ is used. Later results will differ for these two cases (p. 16).

**1.3.2 First variation (pp. 16–17).**
- A linear functional $\delta J|_y:V\to\mathbb R$ is the *first variation* of $J$ at $y$ if for all $\eta$ and all $\alpha$
$$J(y+\alpha\eta)=J(y)+\delta J|_y(\eta)\alpha+o(\alpha)\tag{1.33}$$
with $o(\alpha)$ as in (1.6) (p. 16).
- It is the Gateaux derivative: $\delta J|_y(\eta)=\lim_{\alpha\to0}\frac{J(y+\alpha\eta)-J(y)}{\alpha}$ (1.34). With $g(\alpha):=J(y+\alpha\eta)$ (1.35), $\delta J|_y(\eta)=g'(0)$ (1.36), and (1.33) is exactly (1.5) (p. 16).
- A perturbation $\eta$ is *admissible* (w.r.t. $A$) if $y^*+\alpha\eta\in A$ for all $\alpha$ near 0. If $y^*$ is a local minimum over $A$ and $\delta J|_{y^*}$ exists (not always the case), the same argument as for (1.7) gives the **first-order necessary condition**: for all admissible $\eta$
$$\delta J|_{y^*}(\eta)=0\tag{1.37}$$
It applies to minima and maxima alike (pp. 16–17).
- Unlike (1.11), (1.37) is much less constructive: one must learn to compute first variations (next chapter) (p. 17).
- Definition (1.33) does not depend on the norm, so (1.37) holds for every norm. An alternative is $J(y+\eta)=J(y)+\delta J|_y(\eta)+o(\|\eta\|)$ (1.38): the Fréchet derivative, stronger than Gateaux. It captures all $\eta$ at once and allows more general perturbations (curves, as in 1.2.2). The book keeps (1.33) as simpler and adequate at least through Chapter 2 (p. 17).

> **Intuition note.** The first variation is the slope of the cost when we nudge the function $y$ in direction $\eta$. A minimum must have zero slope for every allowed nudge. What is missing so far is a way to compute that slope for real functionals.

**1.3.3 Second variation (pp. 17–19).**
- A *bilinear* functional $B$ on $V\times V$ is linear in each argument; $Q(y)=B(y,y)$ is a quadratic form (p. 17).
- The quadratic form $\delta^2J|_y$ is the *second variation* if
$$J(y+\alpha\eta)=J(y)+\delta J|_y(\eta)\alpha+\delta^2J|_y(\eta)\alpha^2+o(\alpha^2)\tag{1.39}$$
This corresponds to (1.12) for $g$ in (1.35) (p. 18). (Added step: comparing with (1.12), $\delta^2J|_y(\eta)=\tfrac12g''(0)$.)
- **Second-order necessary condition:** if $y^*$ is a local minimum over $A$, then for all admissible $\eta$
$$\delta^2J|_{y^*}(\eta)\ge0\tag{1.40}$$
i.e. positive semidefinite on admissible perturbations. For maxima the inequality is reversed (p. 18).
- **The sufficiency argument does not go through.** Guess: (1.37) plus $\delta^2J|_{y^*}(\eta)>0$ (1.41). For each $\eta$ we get $J(y^*+\alpha\eta)>J(y^*)$ for small nonzero $\alpha$, but $\varepsilon$ depends on $\eta$. The finite-dimensional fix (minimum of $\varepsilon$ over unit-length directions) is unavailable, since the unit sphere in infinite-dimensional $V$ is not compact (p. 18).
- A possible resolution: strengthen (1.41) to $\delta^2J|_{y^*}(\eta)\ge\lambda\|\eta\|^2$ for some $\lambda>0$ (1.42), which does not follow from (1.41) here ("uniformly positive definite"). Also redefine the variations with uniformly decaying higher-order terms: (1.38) and $J(y+\eta)=J(y)+\delta J|_y(\eta)+\delta^2J|_y(\eta)+o(\|\eta\|^2)$ (1.43). Adopting these alternative definitions and assuming (1.37) and (1.42), the author says the sufficiency proof could easily be completed, since $|o(\|\eta\|^2)|<\lambda\|\eta\|^2$ for small $\|\eta\|$ (pp. 18–19).
- With the current definitions (1.33), (1.39) there is no general second-order sufficient condition. Specific functional forms in later chapters will allow conditions where second-order terms dominate. This discussion is illustrative and not used later (p. 19).

> **Intuition note.** In $\mathbb R^n$, compactness of the unit sphere gives one safe radius. In function space, safe radii may shrink with direction, so positivity in each direction does not give a ball. The author notes that requiring uniform positivity (1.42), together with variations whose higher-order terms decay uniformly in $\|\eta\|$, would allow the argument to be completed.

**1.3.4 Global minima and convexity (p. 19).**
- The Weierstrass Theorem remains valid if compactness of $A$ means finite subcovers or sequential compactness (equivalent in normed spaces). Closed and bounded subsets of an infinite-dimensional space need not be compact, so the theorem does not apply to them (see Exercise 1.7). Continuity, convergence, closedness, boundedness and openness are defined via the norm as in $\mathbb R^n$ (p. 19).
- If $J$ is convex and $A$ is convex, a local minimum is global and the first-order condition is sufficient. The book does not assume convexity, since that would severely restrict the problems studied, but finite-dimensional convex analysis will matter for the maximum principle (p. 19).

### 1.4 Notes and references (p. 20)
Section 1.2 is in standard optimization texts; the inverse-function-theorem argument is adapted from [Mac05]; Farkas' lemma gives another derivation, with similar reasoning in the maximum-principle proof (Chapter 4). Section 1.3 is largely based on [GF63]. [GF63] and [Mac05] define the variations via (1.38) and (1.43); other sources, e.g. [You80], use (1.33) and (1.39) (p. 20).

## Toy example (ours, not from the text)
Minimize $f(x_1,x_2)=x_1^2+x_2^2$ over $D=\{h(x)=x_1+x_2-2=0\}$.
- $\nabla f=(2x_1,2x_2)^T$, $\nabla h=(1,1)^T\ne0$, so every point of $D$ is regular.
- (1.25) plus the constraint: $2x_1+\lambda=0$, $2x_2+\lambda=0$, $x_1+x_2=2$. So $x_1=x_2=-\lambda/2$, and $-\lambda=2$ gives $\lambda^*=-2$, $x^*=(1,1)$.
- Check (1.28) with $\ell=x_1^2+x_2^2+\lambda(x_1+x_2-2)$: $\ell_x=(2+\lambda,\,2+\lambda)=(0,0)$ and $\ell_\lambda=1+1-2=0$ at $(1,1,-2)$.
- Along the curve $x(\alpha)=(1+\alpha,1-\alpha)\in D$: $g(\alpha)=(1+\alpha)^2+(1-\alpha)^2=2+2\alpha^2$. So $g'(0)=0$ (1.19) and $g''(0)=4\ge0$.
- Second-order sufficient test (1.29): $\ell_{xx}=2I$, and for nonzero tangent $d$ ($d_1+d_2=0$) $d^T2Id=2(d_1^2+d_2^2)>0$. So $(1,1)$ is a strict constrained local minimum, with $f=2$.

## Concepts
- [[optimal-control-problem]] (new) — minimize cost functional $J(u)$ over admissible controls $u$ for the ODE system (1.1) (p. 1)
- [[cost-functional]] (new) — real-valued function of a control (or path): running cost integral plus terminal cost, (1.2) (p. 1)
- [[state]] — the vector $x\in\mathbb R^n$ in $\dot x=f(t,x,u)$ (p. 1)
- [[state-space-model]] — here the control system $\dot x=f(t,x,u)$, $x(t_0)=x_0$ (p. 1)
- [[pontryagin-maximum-principle]] — only named here as one of two key developments, treated later (p. 3)
- [[principle-of-optimality]] — "dynamic programming" is named as the other development, not explained here (p. 3)
- [[first-order-necessary-condition]] (new) — $\nabla f(x^*)=0$ (1.11); in function spaces $\delta J|_{y^*}(\eta)=0$ (1.37) (pp. 4, 16)
- [[second-order-conditions]] (new) — necessary: Hessian (second variation) positive semidefinite; sufficient (finite-dim): $\nabla f=0$, Hessian positive definite (pp. 6, 18)
- [[lagrange-multipliers]] (new) — coefficients $\lambda_i^*$ in (1.25); regular point assumed (p. 11)
- [[augmented-cost]] (new) — $\ell(x,\lambda)=f+\sum\lambda_ih_i$ (1.27); (1.28) holds at a constrained minimum with multipliers satisfying (1.25); the author stresses it does not follow that (1.28) is a necessary condition for constrained minimality, and there is no quick derivation of (1.25) from $\ell$ (p. 13)
- [[first-variation]] (new) — Gateaux-type derivative of a functional, (1.33)–(1.36) (p. 16)
- [[second-variation]] (new) — quadratic form in (1.39) (p. 18)
- [[function-space-norm]] (new) — norms ($0$-, $1$-, $L_p$) defining closeness; choice of norm matters (pp. 14–15)
- [[convexity-and-global-minima]] (new) — convex problems: local = global, first-order condition sufficient (pp. 8, 19)

## Canonical instances
- [[car-parking-min-time]] — double integrator $\ddot x=u$, $|u|\le1$, parked at the origin in minimal time (Example 1.1; solved in Section 4.4.1) (p. 2)
- [[fermat-reflection-problem]] — Exercise 1.4: shortest light path via a reflecting curve implies the law of reflection (via 1.25) (p. 13)
- [[functional-integral-of-g-of-y]] — $J(y)=\int_0^1g(y(x))dx$, used for first and second variation exercises (pp. 17–18)

## Bridges (candidates)
- [structural-analogy] Perturbation $x^*+\alpha d$ ↔ $y^*+\alpha\eta$ — reduce to scalar $g(\alpha)$ in both settings (pp. 4, 16)
- [structural-analogy] Lagrange multiplier / augmented cost $\ell$ ↔ control theory: costates (shadow prices) in the maximum principle — the book says $\ell$ "will reappear in various forms" (p. 13); the costate link is canon, not stated in this unit
- [metaphor] "Closeness depends on the norm" ↔ robustness: which perturbations count as small depends on the chosen measure (not stated in this unit)

## Questions this raises
- How do we compute $\delta J|_y(\eta)$ for integral functionals, and what concrete condition does (1.37) give (next chapter)?
- Why do the results differ between the $0$-norm on $C^0$ and the $1$-norm on $C^1$ (p. 16)?
- Which structure of $J$ makes second-order terms dominate higher-order terms, giving sufficiency (p. 19)?
- How will the maximum principle and dynamic programming relate to each other (p. 3)?

## Exercises worth doing
- Ex. 1.1 (p. 7) — whether first- and second-order feasible-direction conditions suffice for a local minimum — difficulty: medium
- Ex. 1.2 (p. 11) — why regularity is needed for the Lagrange condition — difficulty: easy
- Ex. 1.3 (p. 12) — extend the Jacobian proof to $m$ constraints — difficulty: medium
- Ex. 1.4 (p. 13) — derive the law of reflection from Fermat's principle with (1.25) — difficulty: medium
- Ex. 1.5 (p. 17) — compute the first variation of $\int_0^1 g(y)dx$ — difficulty: easy
- Ex. 1.7 (p. 19) — closed bounded set with no global minimum (noncompactness) — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 11–30 = printed 1–20).
- The text layer of printed p. 2 (Example 1.1) is garbled; the image was used.
- Misprint: Exercise 1.3 reads "constrains" for "constraints" (p. 12).
- In the displayed Taylor expansions the digest follows the page images: (1.39) has no explicit $\tfrac12$ factor, unlike (1.12).
- Concept ids marked (new) are proposals; "maximum principle" and "dynamic programming" appear here only by name.
