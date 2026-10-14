---
id: liberzon-2012-calculus/ch03-calculus
work: liberzon-2012-calculus
unit: "Chapter 3 — From Calculus of Variations to Optimal Control"
pages: 57-80
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
# From Calculus of Variations to Optimal Control

## L0 — One line
Perturbing the control instead of the curve, and using the Hamiltonian with an adjoint vector, gives conditions that look like the maximum principle. The same chapter shows why that variational route is too narrow.

## L1 — The gist (≤ 120 words)
Chapter 2 gave conditions mainly for weak minima of smooth ($\mathcal C^1$) curves. Control problems need strong minima, rough controls and constrained controls. The chapter first derives two strong-minimum conditions (corner conditions, Weierstrass E-function). It then recasts calculus of variations as optimal control (system, Bolza cost, target set). For the fixed-time, free-endpoint problem it perturbs the control and finds canonical equations, an adjoint (costate) vector, and $H_u=0$ with $H_{uu}\le 0$. It conjectures (without proof) that, for each $t$, $H$ has a local maximum in $u$ at the optimal control. It ends by listing four limits of this approach (control set, final state, differentiability, perturbation size). Those limits motivate the maximum principle.

**Prerequisites:** Euler–Lagrange equation, momentum and Hamiltonian from calculus of variations; first and second variation; integration by parts; Jacobian matrix; basic ODEs. Terms used above: a weak minimum beats nearby curves whose values and slopes are both close, a strong minimum only those whose values are close; a Bolza cost is a running-cost integral plus a terminal cost; the target set is the set the final point must reach; the canonical equations are $\dot x=H_p$, $\dot p=-H_x$.

## L2 — Key ideas (5–10 bullets)
- At a corner of a strong extremum, $L_{y'}$ and $y'L_{y'}-L$ (momentum and Hamiltonian) must be continuous. This comes from perturbing the corner's position and both pieces of the curve (pp. 58–61).
- The Weierstrass E-function must be $\ge 0$ along a strong minimum. Equivalently, $L(x,y,\cdot)$ lies above its tangent line at $y'(x)$. The proof uses a perturbation with a large slope on a short interval, not the first variation (pp. 61–64).
- In Hamiltonian form, the E-condition says $H(x,y(x),\cdot,p(x))$ is maximal at $y'(x)$. This connects the E-condition to the Hamiltonian maximisation property, and so to the maximum principle (p. 65).
- Optimal control treats the slope as a control, $y'=u$ or $y'=f(x,y,u)$, with a control set and time as the independent variable. The brachistochrone becomes a time-optimal problem (pp. 65–66).
- The general problem is a control system (3.18), a Bolza cost (3.21) and a closed target set $S$. The Lagrange and Mayer forms are special cases that can be converted to and from it by simple transformations (one of them adds a state variable) (pp. 67–71).
- Perturbing the control gives a linearised state perturbation $\dot\eta=A_*\eta+B_*\xi$. At an optimum the first variation must vanish for all $\xi$; when $p^*$ solves the adjoint equation with $p^*(t_1)=-K_x$, this implies $H_u|_*\equiv0$ (pp. 72–74).
- The second variation gives the Legendre–Clebsch condition $H_{uu}\le0$. The text then conjectures, without proof, that $H$ has a local maximum in $u$ at $u^*(t)$ (pp. 76–77).
- Four shortcomings of the variational approach (bounded control set, constrained final state, differentiability, only small perturbations) motivate the maximum principle (pp. 78–79).

## L3 — Walkthrough

### 3.1 Necessary conditions for strong extrema (p. 57)
Chapter 2 mostly covers weak minima over $\mathcal C^1$ curves. Optimal control needs stronger notions of local optimality over less regular curves. This chapter is a bridge to the maximum principle. Its first two results use a new kind of perturbation instead of the family (2.10) (p. 57).

#### 3.1.1 Weierstrass–Erdmann corner conditions (pp. 57–61)
A *corner point* $c$ of a piecewise $\mathcal C^1$ curve is a point where $y$ is continuous, and the one-sided limits $y'(c^-)$ and $y'(c^+)$ exist but differ. Examples: a catenary hung too close to the ground, with two corners (Figure 3.1, pp. 57–58). Also Example 3.1: minimise $J(y)=\int_{-1}^1 y^2(y'-1)^2dx$ with $y(-1)=0$, $y(1)=1$. Here $J\ge0$. $\mathcal C^1$ curves give $J$ arbitrarily close to $0$ but never $0$. The curve $y=0$ on $[-1,0)$, $y=x$ on $[0,1]$ gives $J=0$ and has a corner at $x=0$ (pp. 57–58).

A strong extremum is also a weak extremum for the generalised 1-norm
$$\|y\|_1:=\max_{a\le x\le b}|y(x)|+\max_{a\le x\le b}\max\{|y'(x^-)|,|y'(x^+)|\}.\tag{3.1}$$
So it satisfies the integral Euler–Lagrange equation (2.23) at noncorner points. Piecewise $\mathcal C^1$ solutions of (2.23) are *extremals* (also "broken extremals"). The question is what extra conditions hold at corners (p. 58).

*Setup (one corner at $c$).* Write the two pieces as $y_1:[a,c]\to\mathbb R$ and $y_2:[c,b]\to\mathbb R$. The perturbed pieces are $y_1+\alpha\eta_1$ and $y_2+\alpha\eta_2$, with $\eta_1(a)=\eta_2(b)=0$. The corner may move to $c+\alpha\Delta x$. Both $\eta_i$ are $\mathcal C^1$ (p. 58). To make the domains match, extend $y_1$ beyond $c$ (linearly, for instance) so that
$$y_1(c)=y(c),\qquad y_1'(c)=y'(c^-),\tag{3.2}$$
and extend $y_2$ similarly to the left of $c$ (p. 59). Split $J(y)=J_1(y_1)+J_2(y_2)$ with $J_1=\int_a^c L\,dx$ and $J_2=\int_c^b L\,dx$. After perturbation $J_1(y_1+\alpha\eta_1)=\int_a^{c+\alpha\Delta x}L(x,y_1+\alpha\eta_1,y_1'+\alpha\eta_1')dx$ (p. 59).

*First variations.* Differentiating at $\alpha=0$ and integrating by parts (p. 59):
$$\delta J_1|_{y_1}(\eta_1)=\int_a^c\Big(L_y-\tfrac{d}{dx}L_{y'}\Big)\eta_1dx+L_{y'}(c,y(c),y'(c^-))\eta_1(c)+L(c,y(c),y'(c^-))\Delta x.$$
Similarly (p. 60):
$$\delta J_2|_{y_2}(\eta_2)=\int_c^b\Big(L_y-\tfrac{d}{dx}L_{y'}\Big)\eta_2dx-L_{y'}(c,y(c),y'(c^+))\eta_2(c)-L(c,y(c),y'(c^+))\Delta x.$$
Since $J(y(\cdot,\alpha))$ is minimal at $\alpha=0$ (0-norm closeness), $0=\delta J_1(\eta_1)+\delta J_2(\eta_2)$. Taking $\eta_i(c)=0$ and $\Delta x=0$ shows each $y_i$ is an extremal, so the integrals vanish. What remains is
$$L_{y'}(c^-)\eta_1(c)-L_{y'}(c^+)\eta_2(c)+L(c^-)\Delta x-L(c^+)\Delta x=0,\tag{3.3}$$
where $L(c^\pm)$ means $L(c,y(c),y'(c^\pm))$ (p. 60).

*Continuity link.* The perturbed curve must stay continuous at $c+\alpha\Delta x$:
$$y_1(c+\alpha\Delta x)+\alpha\eta_1(c+\alpha\Delta x)=y_2(c+\alpha\Delta x)+\alpha\eta_2(c+\alpha\Delta x)=:y(c)+\alpha\Delta y+o(\alpha).\tag{3.4}$$
Here $\Delta y$ is the first-order vertical displacement of the corner, independent of $\Delta x$. First-order terms and (3.2) give
$$y'(c^-)\Delta x+\eta_1(c)=y'(c^+)\Delta x+\eta_2(c)=\Delta y.\tag{3.5}$$
Eliminating $\eta_1(c),\eta_2(c)$ from (3.3) (p. 60):
$$-\big[L_{y'}\big]_{c^-}^{c^+}\Delta y+\big[y'L_{y'}-L\big]_{c^-}^{c^+}\Delta x=0.$$
$\Delta x,\Delta y$ are independent and arbitrary, so both brackets vanish (p. 60).

**Weierstrass–Erdmann corner conditions.** If $y$ is a strong extremum, then $L_{y'}$ and $y'L_{y'}-L$ must be continuous at each corner. More precisely, their discontinuities must be removable. These are the momentum and the Hamiltonian from Chapter 2. Weierstrass presented them in 1865 lectures without publishing; Erdmann derived and published them in 1877 (p. 61).

*Intuition note.* At a corner the curve cannot "jump" in momentum or in the Hamiltonian-like quantity. Moving the corner sideways and up or down are two independent tests. Each forces one quantity to match across the corner.

*Counting.* One corner plus two boundary conditions give four relations, which fixes two second-order pieces. In general $m$ portions need $2m$ conditions: $2(m-1)$ corner conditions plus 2 boundary conditions (p. 61). Exercises 3.1 and 3.2 are on p. 61.

#### 3.1.2 Weierstrass excess function (pp. 61–65)
For $L=L(x,y,z)$ the *E-function* is
$$E(x,y,z,w):=L(x,y,w)-L(x,y,z)-(w-z)L_z(x,y,z).\tag{3.6}$$
$L(x,y,z)+(w-z)L_z$ is the first-order Taylor approximation of $L(x,y,w)$ in $w$ around $z$. So $E$ is the gap between $L$ and this tangent line (Figure 3.3, p. 62). The text works in the single-degree-of-freedom case (p. 61).

**Weierstrass necessary condition.** If $y(\cdot)$ is a strong minimum, then
$$E(x,y(x),y'(x),w)\ge0\tag{3.7}$$
for all noncorner $x\in[a,b]$ and all $w\in\mathbb R$. Geometrically, $L(x,y(x),\cdot)$ lies above its tangent line at $y'(x)$ (a local convexity property) (p. 61).

*Proof.* Take a noncorner $\bar x$, $d\in(\bar x,b]$ with no corners in $[\bar x,d]$, and $w\in\mathbb R$. Define, for $\varepsilon\in[0,d-\bar x)$ (p. 62):
$$y(x,\varepsilon):=\begin{cases}y(x)&a\le x\le\bar x\ \text{or}\ d\le x\le b\\ y(\bar x)+w(x-\bar x)&\bar x\le x\le\bar x+\varepsilon\\ y(x)+\dfrac{d-x}{d-(\bar x+\varepsilon)}\big(y(\bar x)+w\varepsilon-y(\bar x+\varepsilon)\big)&\bar x+\varepsilon\le x\le d\end{cases}\tag{3.8}$$
So $y(\cdot,0)=y$ (3.9). This curve is close to $y$ in the 0-norm, so $\varepsilon\mapsto J(y(\cdot,\varepsilon))$ has a minimum at $0$. The plan is to show its right derivative at $0$ equals $E(\bar x,y(\bar x),y'(\bar x),w)$, which must therefore be $\ge0$ (p. 62). Split
$$\tfrac{d}{d\varepsilon}J=\tfrac{d}{d\varepsilon}\Big(\int_{\bar x}^{\bar x+\varepsilon}L(x,y(x,\varepsilon),y_x)dx+\int_{\bar x+\varepsilon}^{d}L(x,y(x,\varepsilon),y_x)dx\Big).\tag{3.10}$$
The first integrand is $L(x,y(\bar x)+w(x-\bar x),w)$, so its derivative is $L(\bar x+\varepsilon,y(\bar x)+w\varepsilon,w)$ (3.11). The second gives
$$-L(\bar x+\varepsilon,y(\bar x+\varepsilon,\varepsilon),y_x(\bar x+\varepsilon,\varepsilon))+\int_{\bar x+\varepsilon}^dL_y\,y_\varepsilon\,dx\tag{3.12}$$
$$+\int_{\bar x+\varepsilon}^dL_{y'}\,y_{x\varepsilon}\,dx.\tag{3.13}$$
Since $y_{x\varepsilon}=\frac{d}{dx}y_\varepsilon$, integration by parts turns (3.13) into
$$L_{y'}y_\varepsilon\Big|_{\bar x+\varepsilon}^{d}-\int_{\bar x+\varepsilon}^d\tfrac{d}{dx}\big(L_{y'}\big)y_\varepsilon dx.\tag{3.14}$$
The boundary term is $L_{y'}(d,\dots)y_\varepsilon(d,\varepsilon)-L_{y'}(\bar x+\varepsilon,\dots)y_\varepsilon(\bar x+\varepsilon,\varepsilon)$ (3.15). The first part is $0$ because $y(d,\varepsilon)=y(d)$ for all $\varepsilon$. From $y(\bar x+\varepsilon,\varepsilon)=y(\bar x)+w\varepsilon$, differentiating in $\varepsilon$ gives $y_x+y_\varepsilon=w$, i.e. $y_\varepsilon(\bar x+\varepsilon,\varepsilon)=w-y_x(\bar x+\varepsilon,\varepsilon)$. So the second part becomes
$$-L_{y'}(\bar x+\varepsilon,y(\bar x+\varepsilon,\varepsilon),y_x(\bar x+\varepsilon,\varepsilon))\big(w-y_x(\bar x+\varepsilon,\varepsilon)\big).\tag{3.16}$$
Sum (3.11), (3.12), minus-integral in (3.14), and (3.16), and set $\varepsilon=0^+$ (using $y_x(\cdot,0)=y'$):
$$\frac{d}{d\varepsilon}\Big|_{0^+}J=L(\bar x,y(\bar x),w)-L(\bar x,y(\bar x),y'(\bar x))-L_{y'}(\bar x,\dots)(w-y'(\bar x))+\int_{\bar x}^d\Big(L_y-\tfrac d{dx}L_{y'}\Big)y_\varepsilon(x,0)dx.$$
The integral is $0$ because a strong (hence weak) minimum satisfies Euler–Lagrange. What remains is $E(\bar x,y(\bar x),y'(\bar x),w)$ (p. 63). $\square$

*Intuition note.* The perturbation puts a short stretch of slope $w$ at $\bar x$ and repairs the curve linearly. For every $w$ the cost must not drop to first order. Large derivative changes are allowed here because the comparison is with a strong minimum.

*Remarks (pp. 63–64).* The condition for a strong *maximum* reverses the inequality. It extends to corner points (by refining the proof or by a limit; cf. Exercise 3.3). Weierstrass introduced it in 1879 lectures. His original proof used an extra assumption (normality), which McShane removed in 1939. $y(\cdot,\varepsilon)$ is 0-norm close to $y$ but not necessarily 1-norm close: $\|y(\cdot,\varepsilon)-y\|_1\ge|w-y'(\bar x)|$ for all $\varepsilon>0$. So the condition applies only to strong minima, unless $w$ is restricted to be near $y'(\bar x)$. The first variation was not used. The condition yields the corner conditions of 3.1.1 and Legendre's condition (Section 2.6.1) as corollaries. Exercise 3.3 asks for this, with hints: the first corner condition already holds for weak extrema (Exercise 3.1); the second needs the full condition; Legendre's follows from the local version, and at a corner it reads $L_{y'y'}(x,y(x),y'(x^\pm))\ge0$ (p. 64). The perturbation is "already quite close" to those used later for the maximum principle. There, the perturbed curve is not brought back to the original, and the effect of a small-interval perturbation is followed to the terminal point (p. 64).

*Hamiltonian reformulation.* With $H(x,y,z,p)=zp-L(x,y,z)$ and $p(x)=L_z(x,y(x),y'(x))$:
$$E=\big(y'L_z-L(\cdot,y')\big)-\big(wL_z-L(\cdot,w)\big)=H(x,y(x),y'(x),p(x))-H(x,y(x),w,p(x))\ge0.$$
So the Weierstrass condition says: for every $x$, $H(x,y(x),\cdot,p(x))$ (the function $H^*$ of (2.32)) has a maximum at $y'(x)$. This escaped Weierstrass because it needs the Hamiltonian and treating $z$ and $p$ as independent arguments (p. 65).

Combining the Weierstrass condition with the weak-minimum sufficient condition of Section 2.6.2 gives a sufficient condition for a strong minimum. It needs the concept of a *field*, which the text does not develop. Sufficient conditions tend to be less practical than necessary ones (p. 65).

### 3.2 Calculus of variations versus optimal control (pp. 65–66)
Optimal control takes a dynamic view: a particle draws a trace, and the slope $y'(x)$ at each point is an infinitesimal decision or control, so $y'=u$. Optimal decisions must be taken everywhere along the curve (p. 65). Velocity constraints $M(x,y,y')=0$, solved for $y'$ with free variables $u$, give $y'=f(x,y,u)$ (Section 2.5.2). Bounds on $u$ are natural to put in a control set, but make the space of admissible curves cumbersome in calculus of variations (p. 65). Parameterising by time $t$ instead of $x$ is more intuitive. It distinguishes identical curves traversed at different speeds, and curves need not be graphs of functions of $x$ (p. 66).

**Example 3.2 (brachistochrone revisited).** The old form (Section 2.1.4) minimises (2.6), whose Lagrangian is arclength over speed. In time parameterisation, with the particle at rest at $(a,0)$ at $t_0$, the speed constraint (2.5) is $\dot x^2+\dot y^2=y$. Set $u_1=\dot x/\sqrt y$, $u_2=\dot y/\sqrt y$:
$$\dot x=u_1\sqrt y,\qquad \dot y=u_2\sqrt y,\qquad u_1^2+u_2^2=1,$$
so the control set is the unit circle. The cost is the arrival time at $(b,y_1)$:
$$J=t_1-t_0=\int_{t_0}^{t_1}1\,dt,\tag{3.17}$$
so $L\equiv1$ and $J=J(u_1,u_2)$. The formulation is equivalent but more general. The burden moves from the cost functional to the right-hand side of the control system (p. 66).

From now on the independent variable is $t$; state $x\in\mathbb R^n$, control $u\in\mathbb R^m$. A problem with $L\equiv 1$ is time-optimal (p. 66).

### 3.3 Optimal control problem formulation and assumptions (pp. 67–71)

#### 3.3.1 Control system (pp. 67–69)
$$\dot x=f(t,x,u),\qquad x(t_0)=x_0,\tag{3.18}$$
with $u\in U\subset\mathbb R^m$ (usually closed, possibly all of $\mathbb R^m$, taken fixed in time) (p. 67). The system is *well posed* if for every initial datum and admissible control there is a unique solution on some $[t_0,t_1]$ (p. 67).

*No controls:* $\dot x=f(t,x)$ (3.19). Assume $f(\cdot,x)$ is piecewise continuous (finitely many discontinuities per bounded interval, one-sided limits, value equal to one of them). This can be relaxed to locally bounded or locally integrable. Assume $f$ is locally Lipschitz in $x$ uniformly in $t$: $|f(t,x_1)-f(t,x_2)|\le L|x_1-x_2|$ near each $(t_0,x_0)$. This holds if $f_x$ (Jacobian) exists and is locally bounded, by the Mean Value Theorem (p. 67). Then a unique local solution exists. A solution means a continuous, a.e. $\mathcal C^1$ function with $x(t)=x_0+\int_{t_0}^tf(s,x(s))ds$. Such functions are *absolutely continuous*. This class generalises piecewise $\mathcal C^1$: the derivative may be discontinuous on a measure-zero set and unbounded near it. If the derivative is locally bounded, one gets the smaller class of locally Lipschitz functions (p. 68).

*With controls:* use $\bar f(t,x):=f(t,x,u(t))$ (3.20). One adequate set of assumptions: $f$ continuous in $t,u$ and $\mathcal C^1$ in $x$; $f_x$ continuous in $t,u$; $u(\cdot)$ piecewise continuous. A weaker set replaces the $f_x$ assumptions by a Lipschitz bound on every bounded $D\subset\mathbb R\times\mathbb R^n\times U$. Differentiability in $u$ is not assumed (p. 68). Exercise 3.4 (p. 68). For $f=f(x,u)$, local Lipschitz suffices. Time can be removed with $x_{n+1}:=t$, $\dot x_{n+1}=1$; then $f$ must be $\mathcal C^1$ in $t$ (or Lipschitz) (p. 68). Admissible controls could be extended to measurable locally bounded functions, but piecewise continuous suffice mostly (exceptions in Sections 4.4–4.5). A solution of (3.18) is absolutely continuous with $x(t)=x_0+\int_{t_0}^tf(s,x(s),u(s))ds$. Only local existence is assumed. Existence on the same interval then holds for trajectories near a candidate optimal one (p. 69).

#### 3.3.2 Cost functional (pp. 69–70)
$$J(u):=\int_{t_0}^{t_f}L(t,x(t),u(t))dt+K(t_f,x_f)\tag{3.21}$$
with running cost (Lagrangian) $L$, terminal cost $K$, $x_f=x(t_f)$. $L$ takes $u$ as argument, which is more general than $L(t,x,\dot x)$ because $\dot x=f(t,x,u)$ can be substituted but not conversely. No regularity is assumed a priori on $L$ and $K$ (p. 69). This is the *Bolza* form. The *Lagrange* problem has $K\equiv0$. The *Mayer* problem has $L\equiv0$ (p. 70).

*Conversions (p. 70).* Terminal to running cost:
$$K(t_f,x_f)=K(t_0,x_0)+\int_{t_0}^{t_f}\tfrac{d}{dt}K(t,x(t))dt=K(t_0,x_0)+\int_{t_0}^{t_f}\big(K_t+K_x\cdot f\big)dt.$$
$K(t_0,x_0)$ is constant, so this is a Lagrange problem with $K_t+K_x\cdot f$ added to $L$. Running to terminal cost: add a state $\dot x^0=L(t,x,u)$, $x^0(t_0)=0$, so $\int L\,dt=x^0(t_f)$ (Mayer form). Adding $x_{n+1}:=t$ removes explicit time dependence.

#### 3.3.3 Target set (pp. 70–71)
Take a closed $S\subset[t_0,\infty)\times\mathbb R^n$. Let $t_f$ be the smallest time with $(t_f,x_f)\in S$. If the trajectory never reaches $S$, the cost is infinite or undefined. $t_f=\infty$ is not allowed here (infinite horizon comes in Chapters 5–6) (p. 70). Examples:
- $S=[t_0,\infty)\times\{x_1\}$: free time, fixed endpoint. More generally $[t_0,\infty)\times S_1$ with $S_1$ a surface.
- $S=\{t_1\}\times\mathbb R^n$: fixed time, free endpoint. With $x_{n+1}=t$ this becomes the previous type with $S_1=\{x_{n+1}=t_1\}$ (pp. 70–71).
- $S=T\times S_1$ covers all these. $\{t_1\}\times\{x_1\}$ is fixed time, fixed endpoint. $[t_0,\infty)\times\mathbb R^n$ is free time, free endpoint.
- A moving target $\{(t,g(t))\}$ is reduced by adding time as a state (p. 71).

In the free-free case, e.g. the Mayer problem, $(t_f,x_f)$ is where the terminal cost is minimised, and "cost" may be a negative "profit" (p. 71). **Refined problem:** given (3.18), (3.21) and $S$, find $u(\cdot)$ minimising the cost, usually in the global sense. The maximum principle also covers local optimality with an appropriate norm (Section 4.3) (p. 71).

### 3.4 Variational approach to the fixed-time, free-endpoint problem (pp. 71–80)

#### 3.4.1 Preliminaries (pp. 71–73)
Specialise: $S=\{t_1\}\times\mathbb R^n$, $U=\mathbb R^m$, $K=K(x_f)$:
$$J(u)=\int_{t_0}^{t_1}L(t,x(t),u(t))dt+K(x(t_1)).\tag{3.22}$$
Let $u^*$ be globally optimal ($J(u^*)\le J(u)$ for all piecewise continuous $u$), with trajectory $x^*$ (pp. 71–72). Perturbing the state as $x=x^*+\alpha\eta$ (3.23) is hard, because admissible $\eta$ are hard to characterise. So perturb the control:
$$u=u^*+\alpha\xi,\tag{3.24}$$
$\xi$ piecewise continuous. The state then has the expansion
$$x=x^*+\alpha\eta+o(\alpha),\tag{3.25}$$
with $\eta(t_0)=0$ and $x_\alpha(t,0)=\eta(t)$ (3.26). Differentiating in $t$ and swapping the order of derivatives (existence of $x_\alpha$ is assumed here; cf. Section 4.2.4):
$$\dot\eta=\tfrac{d}{d\alpha}\Big|_0f(t,x(t,\alpha),u^*+\alpha\xi)=f_x x_\alpha+f_u\xi,$$
$$\dot\eta=f_x(t,x^*,u^*)\eta+f_u(t,x^*,u^*)\xi=:f_x|_*\eta+f_u|_*\xi,\tag{3.27}$$
which with $A_*(t):=f_x|_*$, $B_*(t):=f_u|_*$ reads $\dot\eta=A_*(t)\eta+B_*(t)\xi$ (3.28). This linear time-varying system is the linearisation of (3.18) along the optimal trajectory (p. 72). (added step) Shapes: $\eta\in\mathbb R^n$, $\xi\in\mathbb R^m$, $A_*\in\mathbb R^{n\times n}$, $B_*\in\mathbb R^{n\times m}$ (from $f_x$, $f_u$ Jacobians).

*Augmented cost.* Following Lagrange's idea for pointwise constraints, with a $\mathcal C^1$ function $p:[t_0,t_1]\to\mathbb R^n$:
$$J(u)=\int_{t_0}^{t_1}\big(L+p\cdot(\dot x-f)\big)dt+K(x(t_1)).$$
The extra term does not change $J$. With the Hamiltonian
$$H(t,x,u,p):=\langle p,f(t,x,u)\rangle-L(t,x,u),\tag{3.29}$$
which matches the earlier $H=\langle p,y'\rangle-L$ after renaming ($x\to t$, $y\to x$, $y'\to\dot x=f$, third argument of $L$ now $u$), the cost is
$$J(u)=\int_{t_0}^{t_1}\big(\langle p,\dot x\rangle-H(t,x,u,p)\big)dt+K(x(t_1)).\tag{3.30}$$
Exercise 3.6 will clarify the relation of $p$ to Lagrange multipliers (p. 73).

#### 3.4.2 First variation (pp. 73–75)
$$J(u)-J(u^*)=\delta J|_{u^*}(\xi)\alpha+o(\alpha).\tag{3.31}$$
With $\approx$ meaning equality up to $o(\alpha)$, the three pieces of (3.30) give:
$$K(x(t_1))-K(x^*(t_1))\approx\langle K_x(x^*(t_1)),\alpha\eta(t_1)\rangle,\tag{3.32}$$
$$H(t,x,u,p)-H(t,x^*,u^*,p)\approx\langle H_x,\alpha\eta\rangle+\langle H_u,\alpha\xi\rangle,\tag{3.33}$$
$$\int_{t_0}^{t_1}\langle p,\dot x-\dot x^*\rangle dt=\langle p,x-x^*\rangle\Big|_{t_0}^{t_1}-\int\langle\dot p,x-x^*\rangle dt\approx\langle p(t_1),\alpha\eta(t_1)\rangle-\int_{t_0}^{t_1}\langle\dot p,\alpha\eta\rangle dt,\tag{3.34}$$
using $x(t_0)=x^*(t_0)$ (p. 73). Combining:
$$\delta J|_{u^*}(\xi)=-\int_{t_0}^{t_1}\big(\langle\dot p+H_x(t,x^*,u^*,p),\eta\rangle+\langle H_u(t,x^*,u^*,p),\xi\rangle\big)dt+\langle K_x(x^*(t_1))+p(t_1),\eta(t_1)\rangle,\tag{3.35}$$
with $\eta$ tied to $\xi$ by (3.27) and $\eta(t_0)=0$ (p. 74).

The first-order condition $\delta J|_{u^*}(\xi)=0$ for all $\xi$ holds for every $p$. Choose $p$ as the solution of
$$\dot p=-H_x(t,x^*,u^*,p),\qquad p(t_1)=-K_x(x^*(t_1)),\tag{3.36–3.37}$$
a *terminal* condition ($p(t_1)=0$ if there is no terminal cost). Call it $p^*$. Then (3.35) reduces to
$$\delta J|_{u^*}(\xi)=-\int_{t_0}^{t_1}\langle H_u|_*,\xi\rangle dt=0\ \ \forall\xi,\tag{3.38}$$
and by Lemma 2.1 (piecewise continuity suffices, per the footnote; the text layer prints "2.13", the page image shows "2.1" plus footnote mark 3):
$$H_u(t,x^*(t),u^*(t),p^*(t))=0\quad\forall t\in[t_0,t_1].\tag{3.39}$$
So $H(t,x^*(t),\cdot,p^*(t))$ has a stationary point at $u^*(t)$ (p. 74).

Since $\dot x=H_p(t,x,u)$, the pair satisfies Hamilton's canonical equations (2.30):
$$\dot x^*=H_p|_*,\qquad \dot p^*=-H_x|_*.\tag{3.40}$$
Expanded, $\dot p^*=-(f_x)^T|_*p^*+L_x|_*=-A_*^T(t)p^*+L_x|_*$. Two systems $\dot x=Ax$ and $\dot z=-A^Tz$ are *adjoint*, so $p$ is the *adjoint vector*. It acts on state velocities inside $\langle p,\dot x\rangle$, so it is also called the *costate* (pp. 74–75).

*Intuition note.* $p^*$ is a bookkeeping vector that cancels the effect of the state perturbation $\eta$ on the cost. Once $\eta$ is eliminated, only the direct effect of changing $u$ remains, and it must vanish.

Exercise 3.5 (recover Euler–Lagrange for $\dot x_i=u_i$) and Exercise 3.6 (recover the Lagrange multiplier condition for $k<n$ constraints) are on p. 75. The text warns that $H$ must not depend on $\dot x$, and the multipliers $\lambda_i^*$ are related to, but not the same as, the components of $p^*$ (p. 75).

#### 3.4.3 Second variation (pp. 76–77)
Expand $x=x^*+\alpha\eta+\alpha^2\zeta+o(\alpha^2)$. With $p=p^*$ the $\zeta$-terms drop out, and (Exercise 3.7 asks to verify):
$$\delta^2J|_{u^*}(\xi)=-\frac12\int_{t_0}^{t_1}\begin{pmatrix}\eta^T&\xi^T\end{pmatrix}\begin{pmatrix}H_{xx}&H_{xu}\\H_{xu}&H_{uu}\end{pmatrix}\Big|_*\begin{pmatrix}\eta\\\xi\end{pmatrix}dt+\frac12\eta^TK_{xx}(x^*(t_1))\eta.\tag{3.41}$$
The second-order necessary condition requires $\delta^2J\ge0$. The $\xi^TH_{uu}\xi$ term dominates, since a large $\xi$ can produce a small $\eta$ (Figure 3.5) but not conversely. This parallels the argument for (2.61), though here $\xi$ is not simply the derivative of $\eta$. So $\xi^TH_{uu}|_*\xi\le0$ for all $\xi$:
$$H_{uu}(t,x^*(t),u^*(t),p^*(t))\le0\quad\forall t\in[t_0,t_1],\tag{3.42}$$
the **Legendre–Clebsch condition** (Hamiltonian form) (p. 76). Here "$\le0$" means negative semidefinite.

With (3.39): if the stationary point is an extremum, it is a maximum. The extremum property is not proved. The text conjectures (**not yet proved**): if $u^*$ is optimal with trajectory $x^*$, there is an adjoint $p^*$ with (1) canonical equations (3.40), $x^*(t_0)=x_0$, $p^*(t_1)=-K_x(x^*(t_1))$; (2) for each $t$, $H(t,x^*(t),u^*(t),p^*(t))\ge H(t,x^*(t),u,p^*(t))$ for all $u$ near $u^*(t)$ (p. 77).

*Intuition note.* Stationarity in $u$ plus negative curvature in $u$ says that if the stationary point is an extremum, it is a maximum; the extremum property itself is not proved. This is the same pattern as the E-function result of 3.1.2.

#### 3.4.4 Some comments (pp. 77–78)
*Sign convention.* With $\hat H:=\langle p,f\rangle+L$ and $\hat p:=-p^*$, $\hat H(t,x^*,\cdot,\hat p)=-H(t,x^*,\cdot,p^*)$ has a *minimum* at $u^*(t)$. Moreover $\dot x^*=\hat H_p$ and $\dot{\hat p}=-\hat H_x$ still hold. Minimum vs maximum principle depends only on sign convention, because minimising $J$ equals maximising $-J$. The book's convention matches its Hamiltonian in calculus of variations (total energy). The literature has no consensus (p. 77).

*Existence form.* The conditions assert existence of $p^*$ solving (3.40), rather than defining $p$ by a formula first as in Section 2.4.1. For $\dot x=u$, (3.29) and (3.39) give $p^*=L_u(t,x^*,u^*)$, recovering the momentum. So the Weierstrass condition must also hold (via the end of 3.1.2) (pp. 77–78).

*Hamiltonian along the optimum:*
$$\frac{d}{dt}H|_*=H_t|_*+\langle H_x|_*,\dot x^*\rangle+\langle H_p|_*,\dot p^*\rangle+\langle H_u|_*,\dot u^*\rangle=H_t|_*,\tag{3.43}$$
because (3.40) makes the first two inner products cancel and (3.39) zeroes the third. If $f$ and $L$ do not depend on $t$, then $H(x^*,u^*,p^*)$ is constant ("energy conserved") (p. 78).

*Sufficiency.* In principle a second-order sufficient condition can be obtained if the assumptions ensure that $\delta^2J$ is positive definite and dominates the $o(\alpha^2)$ terms. Exercise 3.8 treats a linear system with quadratic cost (studied in Chapter 6), where this is easy (p. 78).

#### 3.4.5 Critique of the variational approach and preview of the maximum principle (pp. 78–80)
Four limits (pp. 78–79):
1. **Control set.** Perturbations (3.24) make sense when $u^*$ is interior to $U$. With a boundary (bounded or finite $U$ is common), $H_u|_*$ need not be $0$. The text says the maximum property holds there too, and globally, as Chapter 4 will show; the variational approach cannot establish it.
2. **Final state.** For a fixed endpoint $\eta(t_1)=0$ is required, so admissible $\xi$ must satisfy $\int_{t_0}^{t_1}\Phi_*(t_1,t)B(t)\xi(t)dt=0$ ($\Phi_*$ the transition matrix of $A_*$). Then (3.38) need hold only for admissible $\xi$, which is no longer strong enough to conclude $H_u|_*\equiv0$.
3. **Differentiability.** It needs $f$ and $L$ differentiable in $u$, which the well-posedness assumptions of 3.3.1 did not give. It rules out costs like $\int|u|dt$. The second variation needs second derivatives of $H$ in $u$.
4. **Control perturbations.** Only small deviations in $x$ and $u$ are allowed; for $\dot x=u$ this is exactly a weak minimum. One wants optimality against large control perturbations that keep the state close (Figure 3.6, p. 80: a two-valued control switching at $\tau-\varepsilon$ instead of $\tau$).

A less restrictive notion of closeness of controls is the key. The text describes the task as "the cutting of the umbilical cord between the calculus of variations and optimal control theory" (p. 79, borrowed from [PB94]). The maximum principle was developed many years later and its proof is much more geometric (pp. 79–80).

### 3.5 Notes and references (p. 80)
Sources named for each part: [GF63] for corner conditions, with the caveat that it does not correctly separate weak and strong minima ([Mac05, Ch. 11] is more accurate); McShane [McS39] and Bliss [Bli30] for the E-function; [AF66] (the first optimal control textbook) as the main source from Section 3.3.2 on; the variational approach follows [AF66, Section 5-7], whose sign convention is the opposite of this book's.

## Toy example (ours, not from the text)
Problem: $\dot x=u$, $x(0)=1$, fixed time $t_1=1$, free endpoint, $L=u^2$, $K=x(1)^2$.

1. Hamiltonian (3.29): $H=pu-u^2$ (here $f=u$). So $H_x=0$, $H_u=p-2u$, $H_{uu}=-2$.
2. (3.36): $\dot p=-H_x=0$, so $p$ is constant.
3. (3.39): $p-2u=0$, so $u=p/2$, constant. Then $x(t)=1+(p/2)t$ and $x(1)=1+p/2$.
4. (3.37): $p(1)=-K_x=-2x(1)=-2-p$. So $2p=-2$ and $p^*=-1$.
5. Result: $u^*=-1/2$, $x^*(t)=1-t/2$, $x^*(1)=1/2$, $J=\int_0^1\tfrac14dt+\tfrac14=\tfrac12$.
6. Checks: $H_{uu}=-2<0$, so (3.42) holds and $u^*$ is a maximiser of $H$ in $u$. $H|_*=pu-u^2=\tfrac12-\tfrac14=\tfrac14$ is constant, as (3.43) predicts for time-invariant data. Among constant controls $u=c$, $J(c)=c^2+(1+c)^2$ gives $J(0)=1$, $J(-1)=1$, $J(-1/2)=\tfrac14+\tfrac14=\tfrac12$. The minimum over $c$ is at $2c+2(1+c)=0$, i.e. $c=-1/2$. This only confirms that $u^*$ is best among constants.

## Concepts
- [[strong-vs-weak-minimum]] (new) — weak: close in $\|\cdot\|_1$; strong: close in the 0-norm, allowing large derivative changes (pp. 57–58, 64)
- [[weierstrass-erdmann-corner-conditions]] (new) — $L_{y'}$ and $y'L_{y'}-L$ continuous at corners of a strong extremum (p. 60)
- [[weierstrass-excess-function]] (new) — $E=L(w)-L(z)-(w-z)L_z$; $E\ge0$ along a strong minimum (pp. 61–62)
- [[legendre-clebsch-condition]] (new) — $H_{uu}|_*\le0$, from the second variation (p. 76)
- [[adjoint-vector-costate]] (new) — $p^*$ solving $\dot p=-H_x$ with $p(t_1)=-K_x$; adjoint to the linearisation (pp. 74–75)
- [[bolza-lagrange-mayer-problems]] (new) — cost with running and terminal parts, with convertible special cases (pp. 69–70)
- [[target-set]] (new) — closed set $S$ defining the final time as the first hitting time (p. 70)
- [[linearization]] — $\dot\eta=A_*\eta+B_*\xi$ along the optimal trajectory (p. 72)
- [[pontryagin-maximum-principle]] — only previewed; Hamiltonian maximisation conjectured here (pp. 77, 79)
- [[state-space-model]] — control system $\dot x=f(t,x,u)$ (p. 67)

## Canonical instances
- [[catenary-with-corners]] — extremal touching the ground with two corners (p. 57)
- [[example-3-1-corner-extremal]] — minimiser with $J=0$ and a corner at $x=0$ (p. 58)
- [[brachistochrone]] — recast as a time-optimal control problem on the unit circle (p. 66)
- [[linear-quadratic-problem]] — Exercise 3.8 setting, studied in Chapter 6 (p. 78)

## Bridges (candidates)
- [structural-analogy] adjoint vector $p^*$ ↔ Lagrange multipliers: both enforce a dynamic constraint inside the cost, and the text says $p$ is "reminiscent of" $\lambda$ but not identical (pp. 73, 75)
- [same-math] linearised perturbation $\dot\eta=A_*\eta+B_*\xi$ ↔ control-theory linearization: Jacobian linearisation along a trajectory (p. 72)
- [structural-analogy] $H|_*$ constant when $f,L$ are time-invariant ↔ energy conservation in mechanics: the text itself uses this reading (p. 78)
- [structural-analogy] Exercise 3.8 (linear system, quadratic cost) ↔ LQR: the text points to Chapter 6 for this class (p. 78)

## Questions this raises
- Can the maximisation of $H$ over $u$ be proved with large control perturbations on short intervals, without derivatives in $u$ (in the spirit of the E-function proof, p. 64)?
- How should the conditions change when $u^*$ lies on the boundary of $U$, or when the endpoint is fixed?
- Why does the adjoint equation use $-A_*^T$, and what does this duality mean system-theoretically (Section 4.2.8)?
- How do the strong-minimum conditions of 3.1 come out of the maximum principle, as promised on p. 57?

## Exercises worth doing
- Ex. 3.1 (p. 61) — shows where the corner proof needs strong minima; first corner condition still holds for weak extrema — medium
- Ex. 3.2 (p. 61) — corner conditions applied to $\int(y')^3dx$; weak vs strong minimality — medium
- Ex. 3.3 (p. 64) — derive the corner conditions and Legendre's condition from the Weierstrass condition — hard
- Ex. 3.5 (p. 75) — recover Euler–Lagrange from (3.39)–(3.40) — medium
- Ex. 3.6 (p. 75) — recover the Lagrange multiplier condition; relation of $\lambda^*$ and $p^*$ — hard
- Ex. 3.8 (p. 78) — linear–quadratic case: canonical equations, control formula, sufficiency — medium

## Reading notes
- Printed page = pdf page − 10 (pdf 67 = printed 57).
- Page 74: the text layer reads "Lemma 2.13"; the page image shows "Lemma 2.1" followed by footnote mark 3. I used Lemma 2.1.
- Garbled extraction on pdf 80 ("Section R3.3.1"): it is "Section 3.3.1".
- Equations were checked against the page images. Exercise 3.4, 3.7 and the exercises listed above are only described, not solved.
- Section 3.4.3's conjecture (Hamiltonian maximisation) is explicitly "not yet proved" in the source.
