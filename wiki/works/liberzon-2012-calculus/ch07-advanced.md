---
id: liberzon-2012-calculus/ch07-advanced
work: liberzon-2012-calculus
unit: "Chapter 7 — Advanced Topics"
pages: 161-180
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Advanced Topics (Liberzon, Ch. 7)

## L0 — One line
Four independent extensions of the maximum principle and HJB theory: the costate is really a covector on a manifold, canonical equations are the HJB characteristics, Riccati inequalities give $\mathcal L_2$-gain and $\mathcal H_\infty$ bounds, and the maximum principle extends to hybrid systems.

## L1 — The gist (≤ 120 words)
Chapters 4–6 gave the maximum principle, the HJB equation and LQR. This chapter asks what happens when their assumptions are relaxed or their meaning is probed. If the state lives on a manifold, the costate is a covector, which explains the adjoint equation and its terminal conditions. The canonical equations are the characteristics of the HJB PDE. If the LQR cost weight has the "wrong" sign, the Riccati equation bounds the worst-case disturbance gain, which leads to $\mathcal H_\infty$ control and LMIs. If dynamics switch between modes, a hybrid maximum principle gives switching conditions; applied to light reflection it yields the law of reflection. The author says the treatment is introductory, not fully rigorous.

**Prerequisites:** maximum principle and costate (Ch. 4); HJB equation (Ch. 5); algebraic Riccati equation and LQR (Ch. 6); Jacobians and the Implicit Function Theorem; Hurwitz matrices; positive semidefinite matrices; $\mathcal L_2$ norm.

## L2 — Key ideas
- On a manifold, states live in $M$ and velocities in the tangent bundle $TM$ (all tangent spaces together). The costate is a covector (a linear function on tangent vectors), so $H=p(f(x,u))$ needs no inner product (p. 163–165).
- Covectors are pulled back along a flow, so they propagate backward. This is why the costate has terminal conditions, and why $p(\xi)$ is constant along the trajectory (p. 165).
- The adjoint equation says an optimal trajectory lifts to an integral curve of the Hamiltonian vector field on $T^*M$ (the space of covectors). That field is defined through the symplectic form, a skew-symmetric bilinear form on tangent vectors to $T^*M$ (p. 166–167).
- For a quasi-linear PDE (linear in $\nabla v$), the solution surface is tangent to $(a,b,c)^T$. Solutions follow from ODEs (characteristics) plus an initial curve; if a transversality condition holds, the problem is locally uniquely solvable, at least in principle (p. 167–169).
- The canonical equations are the characteristic strips of the HJB equation (ODE systems for $x$, $V$ and $V_x$ along curves). They also give $V$ by integration along a characteristic (p. 170).
- With the opposite sign pattern in the LQR cost, a solution $P$ of the algebraic Riccati equation (ARE) with properties 1–3 ($P\ge0$, the ARE, Hurwitz closed loop) certifies $\mathcal L_2$ gain $\le\gamma$ (the induced norm from input to output energy). The Riccati inequality (7.26) is enough for this (p. 171–173).
- State-feedback $\mathcal H_\infty$ design reduces to a Riccati equation (7.29). The Riccati inequality (7.30) can be shown to be equivalent to a linear matrix inequality (LMI), which is a convex feasibility problem (p. 175–176).
- The hybrid maximum principle adds a costate that may jump, switching conditions, and a constant Hamiltonian. It recovers the law of reflection (p. 177–179).

## L3 — Walkthrough

### 7.1 Maximum principle on manifolds (p. 161)
Motivation: $\mathbb R^n$ is often not the right state space. The pendulum angle lives on a circle, so the state lives on a cylinder (p. 161). Casting the maximum principle on manifolds also clarifies what the costate is, even in $\mathbb R^n$ (p. 161). State spaces defined by inequality constraints are not covered (p. 161).

#### 7.1.1 Differentiable manifolds (p. 162–163)
- A $k$-dimensional manifold embedded in $\mathbb R^n$:
$$M=\{x\in\mathbb R^n: h_1(x)=\dots=h_{n-k}(x)=0\}\tag{7.1}$$
with $h_i\in C^1$ and $\nabla h_i(x)$ linearly independent for each $x\in M$ (all points regular) (p. 162).
- Local coordinates: the $(n-k)\times n$ Jacobian has rank $n-k$. After reordering variables, the Implicit Function Theorem solves for $x_{k+1},\dots,x_n$ in terms of $x_1,\dots,x_k$ near $x$. So $x_1,\dots,x_k$ are a local chart (p. 162).
- Tangent space $T_xM$: $k$-dimensional, spanned by $\dot x(0)$ for curves in $M$ through $x$. The tangent bundle $TM=\bigcup_x T_xM$ has dimension $2k$ (p. 162). In general it is not globally diffeomorphic to $M\times\mathbb R^k$ (e.g. sphere, Möbius band) (p. 162). Vector fields are sections $f:M\to TM$ with $f(x)\in T_xM$ (p. 162).
- Cotangent space $T^*_xM$: the dual space, i.e. linear real functions on $T_xM$. Its elements are covectors. Basic example: for $g\in C^1$, $dg|_x(\xi):=\frac{d}{d\alpha}\big|_{\alpha=0}g(x(\alpha))$ with $\dot x(0)=\xi$. In coordinates $dg|_x(\xi)=\sum_i g_{x_i}\xi_i$, independent of the curve (p. 163).
- $dx_1,\dots,dx_k$ form a basis of $T_x^*M$. The cotangent bundle $T^*M$ has dimension $2k$ and canonical coordinates (p. 163).

*Intuition note:* A tangent vector is a velocity; a covector is a "measuring device" that turns a velocity into a number. The differential of a function is the simplest example of a covector.

#### 7.1.2 Re-interpreting the maximum principle (p. 163–165)
- For $\dot x=f(x,u)$ on $M$, $f(x,u)$ must be tangent to $M$. States live in $M$, velocities in $TM$. In $\mathbb R^n$ this difference is hidden (p. 163).
- Assume Mayer form (terminal cost only); running costs are handled by adding a state $x^0$ (p. 163). In $\mathbb R^n$, $H=\langle p,f(x,u)\rangle$ (p. 164).
- Liberzon considers candidate homes for $p$. As a tangent vector: no geometric reason, and $H$ would need a Riemannian metric (inner product), which is "neither necessary nor relevant" here. In $M$ itself: even less natural (p. 164). The clue is that $p$ always appears inside inner products with velocities, so it acts on velocity vectors, which suggests a covector (p. 164).
- Propagation. Let $\Phi_\tau:M\to M$ be the $C^1$ flow map for time $\tau$ along (7.2) with a fixed control. Tangent vectors move forward: $d\Phi_\tau|_x(\xi):=\frac{d}{d\alpha}\big|_{\alpha=0}\Phi_\tau(x(\alpha))$, a linear map $T_xM\to T_{\Phi_\tau(x)}M$. Infinitesimally this is the variational equation
$$\dot\xi=f_x|_*\,\xi\tag{7.3}$$
Objects that propagate forward are *contravariant* (p. 164).
- There is no apparent way to push covectors forward, because the preimage under $\Phi_\tau$ is not well defined unless $\Phi_\tau$ is invertible. They are pulled back:
$$p|_x(\xi):=p|_{\Phi_\tau(x)}\big(d\Phi_\tau|_x(\xi)\big)\tag{7.4}$$
(p. 165).
- (7.4) is the coordinate-free form of the adjoint property of Sec. 4.2.8: $p(\xi)$ stays constant along the trajectory. The adjoint equation $\dot p=-(f_x)^T|_*p$ is its infinitesimal version in local coordinates. Covectors are *covariant*: they propagate backward. This is why the costate has terminal rather than initial conditions (p. 165).
- Hamiltonian on a manifold:
$$H(x,u,p)=p(f(x,u))\tag{7.5}$$
The maximum principle postulates $p^*(t)\in T^*_{x^*(t)}M$. The value $p^*(t_f)$ determines $p^*$ on $[t_0,t_f]$. Hamiltonian maximization is as in Chapter 4 (p. 165). The formal statement is in the references (p. 165).

*Intuition note:* Perturbations of the state move forward in time; the costate is a covector acting on those perturbations, with $p(\xi)$ constant along the trajectory. So it is fixed by its terminal value and propagated backward.

#### 7.1.3 Symplectic geometry and Hamiltonian flows (p. 166–167)
- On $T^*M$ (dimension $2k$) there is a symplectic form $\omega^2:=dx_1\wedge dp_1+\dots+dx_k\wedge dp_k$. It is bilinear, skew-symmetric, and acts on pairs of tangent vectors to $T^*M$ (p. 166). Here $(\omega_1\wedge\omega_2)(\xi_1,\xi_2):=\omega_1(\xi_1)\omega_2(\xi_2)-\omega_2(\xi_1)\omega_1(\xi_2)$ (p. 166).
- For tangent vectors $(y,q)$ and $(z,r)$:
$$\omega^2\big((y,q),(z,r)\big)=\sum_{i=1}^k(y_ir_i-q_iz_i)\tag{7.6}$$
(p. 166).
- Tangent vector $\xi\mapsto$ covector $\omega^1_\xi(\eta):=\omega^2(\xi,\eta)$ (7.7). This is linear and one-to-one, with matrix $\begin{pmatrix}0&-I\\ I&0\end{pmatrix}$ in canonical coordinates (p. 166).
- $H$ viewed as a function of $(x,p)$, with $u$ as a parameter, has a differential $dH$ (a covector). Applying the inverse of the map above gives the Hamiltonian vector field $\vec H$, whose flow is
$$\dot x=H_p,\qquad \dot p=-H_x\tag{7.8}$$
(p. 166).
- Check: for $\eta=(z,r)$, (7.6) gives $\omega^2(\vec H,\eta)=\sum_i(H_{x_i}z_i+H_{p_i}r_i)=dH(\eta)$ (p. 167).
- Consequence: the maximum principle's claim that a costate satisfying the adjoint equation exists says an optimal trajectory can be lifted to an integral curve of $\vec H$ (with $u^*$ plugged in) (p. 167).

### 7.2 HJB equation, canonical equations, characteristics (p. 167)
Sec. 5.2 showed that solving HJB formally yields canonical equations via $p:=-V_x$. Here the direction is reversed: canonical equations arise as characteristics of HJB (p. 167).

#### 7.2.1 Method of characteristics (p. 167–170)
- PDE $F(x,v(x),\nabla v(x))=0$ (7.9), with $v$ classically differentiable. Quasi-linear means $F$ is linear in $\nabla v$. For $n=2$:
$$a\,v_{x_1}+b\,v_{x_2}=c,\quad a,b,c\ \text{functions of}\ (x_1,x_2,v)\tag{7.10}$$
(p. 167).
- The graph $h:=v(x_1,x_2)-v=0$ has normal $\nabla h=(v_{x_1},v_{x_2},-1)^T$. (7.10) says $\langle(a,b,c)^T,\nabla h\rangle=0$, so $(a,b,c)^T$ is tangent to the solution surface (p. 167–168). Characteristic ODEs:
$$\frac{dx_1}{ds}=a,\quad\frac{dx_2}{ds}=b,\quad\frac{dv}{ds}=c\tag{7.11}$$
Their solution curves are the characteristics (p. 168).
- Example $c\equiv0$: $v$ is constant along $\dot x_1=a,\ \dot x_2=b$; characteristics are horizontal slices (p. 168).
- Characteristics pass through every point of $(x_1,x_2,v)$-space, so an initial curve $x_1(r),x_2(r),v(r)$ is needed (Cauchy problem). Characteristics started on it give $x_1(r,s),x_2(r,s),v(r,s)$ (7.12) (p. 168–169).
- To write $v=v(x_1,x_2)$ we must invert $(r,s)\mapsto(x_1,x_2)$. The Inverse Function Theorem guarantees this near the initial curve if $\begin{pmatrix}(x_1)_r&(x_1)_s\\(x_2)_r&(x_2)_s\end{pmatrix}$ is nonsingular there, i.e. projections of the initial curve and the characteristic are transversal. Then the Cauchy problem is locally uniquely solvable, at least in principle (p. 169).
- General PDE $F(x_1,x_2,v,v_{x_1},v_{x_2})=0$ (7.13) needs five equations, the characteristic strips. With $\xi_i:=v_{x_i}$:
$$\dot x_1=F_{\xi_1},\ \dot x_2=F_{\xi_2},\ \dot v=\xi_1F_{\xi_1}+\xi_2F_{\xi_2},\ \dot\xi_1=-F_{x_1}-\xi_1F_v,\ \dot\xi_2=-F_{x_2}-\xi_2F_v\tag{7.14}$$
(derivatives w.r.t. $s$). Sketch of the 4th equation: $\frac{d\xi_1}{ds}=(\xi_1)_{x_1}\frac{dx_1}{ds}+(\xi_1)_{x_2}\frac{dx_2}{ds}$. Insert the first two equations, then use $F_{x_1}+F_v\xi_1+F_{\xi_1}(\xi_1)_{x_1}+F_{\xi_2}(\xi_2)_{x_1}=0$ (differentiating (7.13) in $x_1$). The author does not give a full derivation (p. 169). For general $n\ge2$, replace indices $1,2$ by $i\in\{1,\dots,n\}$ (p. 170).

#### 7.2.2 Canonical equations as characteristics of HJB (p. 170)
- Write HJB (control already maximized out) as
$$V_t(t,x)-H(t,x,-V_x(t,x))=0\tag{7.15}$$
Add $x_{n+1}:=t$ to get the form (7.9); use $t$ as independent variable; set $p_i:=-\xi_i=-V_{x_i}$ (p. 170).
- Then (7.14) gives $\dot x_i=H_{p_i}$, $i=1..n$ (and the redundant $\dot x_{n+1}=1$), and $\dot p_i=-H_{x_i}$, $i=1..n+1$. The $F_v$ term vanishes because $H$ does not depend on $V$ (p. 170).
- Value equation, using (7.15) again for the second equality:
$$\dot V=\sum_{i=1}^n\xi_i\dot x_i+\xi_{n+1}=H-\sum_{i=1}^np_iH_{p_i}\tag{7.16}$$
(also directly from $\dot V=V_t+\langle V_x,\dot x\rangle$) (p. 170).
- Solving HJB: the Cauchy data are $V(t_1,x)=K(x)$ (flowing backward). To get $V(t,x)$, find $\bar x$ such that $x=x(t)$ for the canonical solution with $x(t_1)=\bar x$, $p(t_1)=-K_x(\bar x)$. Then
$$V(t,x(t))=K(\bar x)-\int_t^{t_1}\Big(H(s,x(s),p(s))-\sum_ip_i(s)H_{p_i}(s,x(s),p(s))\Big)ds.$$
Figure 7.3 illustrates this (p. 170).

*Intuition note:* HJB is a PDE for the whole value function. Along a single optimal trajectory it collapses to ODEs, and the costate is the slope of $V$ (up to sign) along it. Integrating (7.16) along that path gives $V$ without solving the PDE everywhere.

### 7.3 Riccati equations and inequalities in robust control (p. 171)

#### 7.3.1 $\mathcal L_2$ gain (p. 171–174)
Shapes (added step, standard): $A$ is $n\times n$; $P$ is $n\times n$.
- System $\dot x=Ax+Bu,\ y=Cx$ (7.17). Cost, with $\gamma>0$:
$$J(u)=\int_{t_0}^\infty\Big(\gamma u^Tu-\tfrac1\gamma y^Ty\Big)dt\tag{7.18}$$
The weights have opposite signs and product $-1$. The optimal cost is nonpositive (take $u\equiv0$) (p. 171).
- **Claim.** Suppose $P$ satisfies (1) $P=P^T\ge0$; (2) the ARE
$$PA+A^TP+\tfrac1\gamma C^TC+\tfrac1\gamma PBB^TP=0\tag{7.19}$$
(3) $A+\frac1\gamma BB^TP$ is Hurwitz (all eigenvalues have negative real part). Then
$$V(x_0)=-x_0^TPx_0\tag{7.20}$$ $$u^*(t)=\tfrac1\gamma B^TPx^*(t)\tag{7.21}$$
Signs are "wrong" relative to Sec. 6.2; this could be reconciled using $-P$ (p. 171–172).
- *Proof.* Let $\hat V(x):=x^TPx$. Then $\frac d{dt}\hat V=x^T(PA+A^TP)x+2x^TPBu$, which is equivalent to
$$\tfrac d{dt}\hat V=x^T\big(PA+A^TP+\tfrac1\gamma C^TC+\tfrac1\gamma PBB^TP\big)x-\gamma\big(u-\tfrac1\gamma B^TPx\big)^T\big(u-\tfrac1\gamma B^TPx\big)+\gamma u^Tu-\tfrac1\gamma y^Ty\tag{7.22}$$
(p. 172). Define the finite-horizon cost
$$\bar J^{t_1}(u):=\int_{t_0}^{t_1}\Big(\gamma u^Tu-\tfrac1\gamma y^Ty\Big)dt-x^T(t_1)Px(t_1)\tag{7.23}$$
By (7.22) and (7.19), $\bar J^{t_1}(u)=\int_{t_0}^{t_1}\gamma\,|u-\tfrac1\gamma B^TPx|^2dt+x^TPx\big|_{t_0}^{t_1}-x^T(t_1)Px(t_1)=\int_{t_0}^{t_1}\gamma|u-\tfrac1\gamma B^TPx|^2dt-x_0^TPx_0$. So (7.20)–(7.21) are optimal for (7.23) (p. 172). For all $u$, since $P\ge0$: $J(u)=\lim\int\ge\lim\big(\int-x^T(t_1)Px(t_1)\big)=\lim\bar J^{t_1}(u)\ge-x_0^TPx_0$. For $u^*$, $\bar J^{t_1}(u^*)=-x_0^TPx_0$. The closed loop $\dot x^*=(A+\frac1\gamma BB^TP)x^*$ is exponentially stable, so $J(u^*)=-x_0^TPx_0$ (p. 172–173).
- *Skip path:* carry forward (7.20)–(7.21) and the completed-square identity (7.22).
- **Meaning.** The cost is small when $y$ is large relative to $u$. So $u$ acts as a disturbance trying to enlarge the output; $u^*$ is in some sense the worst-case disturbance (p. 173). The optimality implies
$$-x_0^TPx_0\le\int_{t_0}^\infty\Big(\gamma|u|^2-\tfrac1\gamma|y|^2\Big)dt\tag{7.24}$$
For all $u$, with equality at $u^*$. For $x_0=0$, after "simple manipulations" (added step: $0\le\gamma\|u\|^2-\frac1\gamma\|y\|^2$, rearranged),
$$\sup_{u\in\mathcal L_2\setminus\{0\}}\frac{\sqrt{\int|y|^2}}{\sqrt{\int|u|^2}}\le\gamma\tag{7.25}$$
The left side is the induced norm of the input/output operator $\mathcal L_2\to\mathcal L_2$ with zero initial state: the $\mathcal L_2$ gain (p. 173).
- So a $P$ with properties 1–3 shows gain $\le\gamma$. It is not known whether $\gamma$ is attained; $u^*\equiv0$ when $x_0=0$ is excluded from (7.25). A converse holds: if the $\mathcal L_2$ gain is less than $\gamma$, such a $P$ exists (p. 173).
- For sufficiency alone, the conditions relax to a symmetric $P\ge0$ solving the algebraic Riccati *inequality*
$$PA+A^TP+\tfrac1\gamma C^TC+\tfrac1\gamma PBB^TP\le0\tag{7.26}$$
Then (7.22) gives $\frac d{dt}\hat V\le\gamma|u|^2-\frac1\gamma|y|^2$. Integrating from $t_0$ to $T$ and using $P\ge0$ gives $\frac1\gamma\int_{t_0}^T|y|^2\le\gamma\int_{t_0}^T|u|^2+\hat V(0)-\hat V(x(t))\le\gamma\int_{t_0}^T|u|^2$. Let $T\to\infty$ to get (7.25) (p. 173–174).
- Frequency domain: with $G(s)=C(Is-A)^{-1}B$, Parseval's theorem shows (stated as "it can be shown") that the $\mathcal L_2$ gain equals the largest singular value of $G(j\omega)$ maximized over $\omega\in\mathbb R$. For scalar systems, $\sup_\omega|g(j\omega)|$. Hence it is also called the $\mathcal H_\infty$ norm (p. 174).

*Intuition note:* Flip a sign in LQR and the "controller" becomes an adversary. A suitable Riccati solution $P$ (properties 1–3, or the relaxed inequality (7.26)) gives an upper bound on the amplification from disturbance energy to output energy: if such a $P\ge0$ exists, the amplification cannot exceed $\gamma$.

#### 7.3.2 $\mathcal H_\infty$ control problem (p. 174–175)
- Robust control: design for desired behavior despite uncertainty. Control and disturbance can be viewed as two players in a differential game (p. 174). System: $\dot x=Ax+Bu+Dw,\ y=Cx,\ z=Ex$, with control $u$, disturbance $w$, measured output $y$, controlled output $z$, no feedthrough terms (p. 174).
- Static state feedback case: $C=I$, $u=Kx$. Goals: (1) $A_{cl}:=A+BK$ is Hurwitz; (2) the $\mathcal L_2$ gain from $w$ to $z$ (the $\mathcal H_\infty$ norm of $E(Is-A_{cl})^{-1}D$) is at most a prespecified $\gamma>0$ (p. 174–175). This is suboptimal control: $\gamma$ is not minimized (p. 175).
- By Sec. 7.3.1 with renamed data, a $P\ge0$ with
$$PA_{cl}+A_{cl}^TP+\tfrac1\gamma E^TE+\tfrac1\gamma PDD^TP\le0\tag{7.27}$$
is sufficient for goal 2. Goal 1 as well needs a slightly stronger condition: $P>0$ and strict inequality. This is encoded by
$$PA_{cl}+A_{cl}^TP+\tfrac1\gamma E^TE+\tfrac1\gamma PDD^TP+\varepsilon Q=0\tag{7.28}$$
with $Q=Q^T>0,\ \varepsilon>0$; it implies $PA_{cl}+A_{cl}^TP<0$, the Lyapunov condition (p. 175).
- In terms of open-loop data, with $R=R^T>0$ as another design parameter, suppose $P>0$ solves
$$PA+A^TP+\tfrac1\gamma E^TE+\tfrac1\gamma PDD^TP-\tfrac1\varepsilon PBR^{-1}B^TP+\varepsilon Q=0\tag{7.29}$$
Then $K:=-\frac1{2\varepsilon}R^{-1}B^TP$ gives $u=Kx$ enforcing (7.28), hence both objectives. (Added step: $PA_{cl}+A_{cl}^TP=PA+A^TP+PBK+K^TB^TP=PA+A^TP-\frac1\varepsilon PBR^{-1}B^TP$.) Conversely, it can be shown that if the system is stabilizable with $\mathcal L_2$ gain less than $\gamma$, then (7.29) is solvable for $P>0$ (p. 175).
- Output feedback (dynamic controller): a complete solution exists; necessary and sufficient conditions use (1) a solution $P_1$ of the state-feedback Riccati equation; (2) a solution $P_2$ of a second Riccati equation, from substitutions $B\to C$ and $D\leftrightarrow E$; (3) largest singular value of $P_1P_2$ less than $\gamma^2$. The controller is interpretable as state feedback plus an estimator (observer). Details are not given (p. 175).

#### 7.3.3 Riccati inequalities and LMIs (p. 176)
- Example (7.26) with $\gamma=1$: $PA+A^TP+C^TC+PBB^TP\le0$ (7.30). It is quadratic in $P$, but it can be shown to be equivalent to the linear matrix inequality
$$\begin{pmatrix}PA+A^TP+C^TC&PB\\B^TP&-I\end{pmatrix}\le0\tag{7.31}$$
The left-hand-side matrix of (7.31) is called the Schur complement of the one in (7.30); $P\ge0$ can be incorporated in the LMI (p. 176). LMIs are convex feasibility problems, efficiently solvable numerically; dedicated software exists (p. 176).

### 7.4 Maximum principle for hybrid control systems (p. 176)
Hybrid systems mix continuous flow with discrete jumps. They violate the assumptions of the Chapter 4 maximum principle, so an extended version is needed (p. 176).

#### 7.4.1 Hybrid optimal control problem (p. 176–177)
- Modes: $\dot x=f_q(x,u),\ q\in Q$ (7.32), $Q$ finite, common state space $\mathbb R^n$ and control set $U\subset\mathbb R^m$. Guards: switching surfaces $S_{q,q'}\subset\mathbb R^{2n}$ (p. 176).
- Admissible trajectory: there exist $t_0<t_1<\dots<t_k<t_{k+1}:=t_f$ and $q_0,\dots,q_k$ with $\dot x=f_{q_i}(x,u)$ on $(t_i,t_{i+1})$ (7.33) and $\binom{x(t_i^-)}{x(t_i^+)}\in S_{q_{i-1},q_i}$, $i=1..k$ (p. 176–177). $q(t):=q_i$ on $[t_i,t_{i+1})$ is the discrete state (p. 177).
- Cost with running cost $L_q$ and switching cost $\Phi_{q,q'}$:
$$J=\sum_{i=0}^k\int_{t_i}^{t_{i+1}}L_{q_i}(x,u)dt+\sum_{i=1}^k\Phi_{q_{i-1},q_i}(x(t_i^-),x(t_i^+))\tag{7.34}$$
No terminal cost, without loss of generality. Endpoint constraint $\binom{x(t_0)}{x(t_f)}\in E_{q_0,q_k}$ (7.35). Control, time sequence $\{t_i\}$ and switching sequence $\{q_i\}$ are all chosen (p. 177).

#### 7.4.2 Hybrid maximum principle (p. 177–178)
Necessary conditions for local optimality among trajectories with the same switching sequence and close to $x^*$ on each subinterval; technical assumptions are assumed (p. 177). With $H_q(x,u,p,p_0):=\langle p,f_q(x,u)\rangle+p_0L_q(x,u)$ (p. 177):
- $p_0^*\le0$. The costate may be discontinuous at switching times; between them $\dot p^*=-(H_{q_i})_x|_*$ (p. 178).
- Transversality: $\binom{p^*(t_0)}{-p^*(t_f)}\perp T_{\binom{x^*(t_0)}{x^*(t_f)}}E_{q_0,q_k}$ (7.36) (p. 178).
- Switching conditions, $i=1..k$:
$$\binom{-p^*(t_i^-)}{p^*(t_i^+)}+p_0^*\nabla\Phi_{q_{i-1},q_i}\big(x^*(t_i^-),x^*(t_i^+)\big)\perp T_{\binom{x^*(t_i^-)}{x^*(t_i^+)}}S_{q_{i-1},q_i}\tag{7.37}$$
(p. 178).
- Nontriviality: $p_0^*\ne0$ or $p^*\not\equiv0$. Hamiltonian maximization on each interval. The Hamiltonian is constant along the optimal trajectory, unaffected by switching. For free-time problems it is 0 (p. 178).
- Intuition: reparameterize time on each piece to a common interval $[s_0,s_f]$ and "stack" the pieces. Then (7.36)–(7.37) form one aggregate transversality condition; the switching-cost gradient appears because the switching cost acts like a combination of terminal and initial costs (p. 178).

#### 7.4.3 Example: light reflection (p. 178–179)
- Model $\dot x=c(x)u,\ |u|=1$ (7.38), $c:\mathbb R^n\to(0,\infty)$ of class $C^1$. Mirror $S=\{x_n=0\}$; start and end points lie in the same open half-space (p. 178). Goal: necessary condition for a locally time-optimal path from $x_0$ that reflects off $S$ at $t_1$ and reaches $x_f$ (p. 178–179).
- Hybrid formulation: $Q=\{q\}$, guard $S_{q,q}=\{(x,x')^T: x=x'\in S\}$, switching sequence $\{q,q\}$. The dynamics do not change and the trajectory stays continuous. This forces the path to touch $S$, which the classical principle cannot express (p. 179).
- $H=\langle p,c(x)u\rangle+p_0$. Maximization: $u^*=p^*/|p^*|$, $H|_*=c(x^*)|p^*|+p_0^*$. Free final time gives $H\equiv0$; with nontriviality, $p_0^*\ne0$ and $p^*(t)\ne0$. Normalize $p_0^*=-1$: $c(x^*)|p^*|\equiv1$, so $u^*=p^*c(x^*)$ (p. 179).
- No switching cost, so $\binom{-p^*(t_1^-)}{p^*(t_1^+)}\perp S_{q,q}$. Tangent vectors there have the form $(x_1,\dots,x_{n-1},0,x_1,\dots,x_{n-1},0)^T$, so $p_i^*(t_1^+)=p_i^*(t_1^-)$ for $i<n$. Hence $u_1^*,\dots,u_{n-1}^*$ are continuous. Since $|u^*|=1$, $u_n^*(t_1^+)=\pm u_n^*(t_1^-)$. The sign must flip because the ray cannot pass through $S$. So only the normal component of velocity changes, by a minus sign: the law of reflection (p. 179).

*Intuition note:* Making the "touch the mirror" requirement part of the hybrid formulation (a guard; the dynamics do not change) lets the costate's jump rule do the work. The tangential part of the costate cannot jump on a flat mirror; only the normal part can.

## Toy example (ours): $\mathcal L_2$ gain via the Riccati equation
Scalar system $\dot x=-x+u,\ y=x$, so $A=-1,\ B=1,\ C=1$. Take $\gamma=2$.
- (7.19) becomes $-2P+\tfrac12+\tfrac12P^2=0$, i.e. $P^2-4P+1=0$, so $P=2\pm\sqrt3$.
- Property 3: $A+\frac1\gamma BB^TP=-1+P/2$. For $P=2-\sqrt3\approx0.268$ this is $\approx-0.866<0$ (Hurwitz). For $2+\sqrt3$ it is $\approx+0.866$, rejected.
- Check (7.19): $P^2=7-4\sqrt3$. Then $-2P+0.5+P^2/2=(-4+2\sqrt3)+0.5+(3.5-2\sqrt3)=0$. ✓
- So gain $\le2$ by (7.25). Optimal cost for $x_0=1$ is $-P=-(2-\sqrt3)\approx-0.268$ by (7.20). Direct check: $u^*=\frac P\gamma x\approx0.134x$, closed loop $\dot x=-0.866x$, so $\int x^2=1/(2\cdot0.866)\approx0.577$. $J=(2\cdot0.134^2-0.5)\cdot0.577\approx(0.0359-0.5)\cdot0.577\approx-0.268$. ✓
- Actual gain: $|g(j\omega)|=1/\sqrt{1+\omega^2}$, maximum $1$ at $\omega=0$. With $\gamma=1$ the inequality (7.26) is $P^2-2P+1\le0$, solved by $P=1\ge0$, giving gain $\le1$, which is tight here. (At $\gamma=1$, $A+P/\gamma=0$ is not Hurwitz, so properties 1–3 fail; only the relaxed (7.26) argument applies.)

## Concepts
- [[costate-as-covector]] (new) — the costate $p$ is a linear function on tangent vectors; $H=p(f)$ (p. 164–165)
- [[manifold-state-space]] (new) — $k$-dim surface in $\mathbb R^n$ given by $h_i(x)=0$ with independent gradients (p. 162)
- [[symplectic-form]] (new) — $\omega^2=\sum dx_i\wedge dp_i$ on $T^*M$; links $dH$ to the Hamiltonian vector field (p. 166)
- [[pontryagin maximum principle]] — here recast with covector costate; also hybrid version (p. 165, 177)
- [[method-of-characteristics]] (new) — solve a first-order PDE through ODEs along curves tangent to $(a,b,c)$ (p. 168)
- [[Hamilton–Jacobi–Bellman equation]] — its characteristic strips are Hamilton's canonical equations (p. 170)
- [[L2-gain]] (new) — induced $\mathcal L_2\to\mathcal L_2$ norm of a system; equals the $\mathcal H_\infty$ norm (p. 173–174)
- [[riccati-inequality-LMI]] (new) — Riccati inequality equivalent to a linear matrix inequality (p. 173, 176)
- [[robustness]] — $\mathcal H_\infty$ design keeps disturbance-to-output gain bounded (p. 174)
- [[observer (state estimator)]] — the output-feedback $\mathcal H_\infty$ controller can be interpreted as state feedback combined with an estimator (observer) (p. 175)
- [[hybrid-optimal-control]] (new) — modes, guards, switching costs, time and switching sequences (p. 176–177)

## Canonical instances
- [[pendulum-on-cylinder]] — angle on a circle plus angular velocity gives a cylinder state space (p. 161)
- [[unit-circle-manifold]] — 1-dim manifold in $\mathbb R^2$ used to illustrate local charts (p. 162)
- [[light-reflection-hybrid]] — hybrid maximum principle yields the law of reflection (p. 178–179)

## Bridges (candidates)
- [same-math] Hamiltonian vector field flow (7.8) ↔ classical mechanics (Sec. 2.4): Hamilton's canonical equations — same equations, now read as a symplectic flow.
- [same-math] Characteristic strips of HJB ↔ Pontryagin canonical equations — equations (7.14) reduce to $\dot x=H_p,\ \dot p=-H_x$.
- [structural-analogy] ARE (7.19) ↔ LQR ARE of Ch. 6 — similar matrix form with sign changes, but the author stresses that the meanings differ.
- [structural-analogy] Covariant costate propagating backward ↔ backpropagation of gradients (canon link; not stated in this unit).
- [structural-analogy] Control vs. disturbance as two players ↔ differential games (the text only mentions this view).

## Questions this raises
- What exactly are the "suitable technical assumptions" behind the hybrid maximum principle, and when can jumps in the costate occur?
- How does the output-feedback $\mathcal H_\infty$ controller arise from the two coupled Riccati equations, and why do the singular values of $P_1P_2$ enter?
- For nonlinear systems, how do Hamilton–Jacobi inequalities replace Riccati inequalities (the notes mention this only briefly)?
- When is the transversality condition for the characteristics' initial curve violated, and what then happens to the HJB solution?

## Reading notes
- Printed page = pdf − 10 (pdf 171–190 ↔ printed 161–180).
- Misprint-like items: on p. 173 the text calls (7.25) "the ratio of the $\mathcal L_2$ norms of the input and the output"; the displayed fraction is output over input. In the $J(u)$ bound chain on p. 172, the image shows $J^{t_1}(u)$ without the bar, where $\bar J^{t_1}$ of (7.23) is evidently meant.
- Asymmetry as printed (p. 173): properties 1–3 give gain $\le\gamma$; the converse is stated for gain $<\gamma$.
- The text layer was readable; equations were checked against page images. Figures 7.1–7.4 are described only in captions and surrounding text.
- This chapter is explicitly less rigorous than earlier ones (p. 161). Many results are stated without proof (the (7.14) derivation, converses, output feedback).
- The unit has no exercises.
