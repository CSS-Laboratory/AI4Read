---
id: liberzon-2012-calculus/ch04-maximum-p1
work: liberzon-2012-calculus
unit: "Chapter 4 — The Maximum Principle (part 1/2): §4.1 statement, §4.2 proof up to inequality (4.38) in Step 10"
pages: 81–101
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# The Maximum Principle (part 1/2): statement and proof

## L0 — One line
If a control is optimal, then a costate (adjoint vector) exists such that the state and costate obey the canonical equations and the Hamiltonian is maximized over the controls at every time. The proof builds a cone of possible terminal perturbations and separates it from the cost-decreasing direction.

## L1 — The gist (≤ 120 words)
Which conditions must an optimal control satisfy when controls take values in a given set $U$ and may be discontinuous (piecewise continuous)? Pontryagin's maximum principle: along an optimal trajectory there are a costate and a constant $p_0^*\le 0$ such that state and costate obey the canonical equations, the Hamiltonian is maximized over the control set at every time and equals 0, and, for a surface target, the costate is orthogonal to the surface. The proof perturbs the optimal control in time and with short needle pulses, builds a convex cone of reachable terminal directions, uses optimality to keep it off the cost-decreasing ray, and separates the two by a hyperplane whose normal gives the costate.

**Prerequisites:** ODEs and linearization; linear time-varying systems and the transition matrix; Taylor expansion with $o(\varepsilon)$; convex sets and cones; inner products; tangent spaces of surfaces.

## L2 — Key ideas
- The principle is stated for two problems: fixed endpoint and endpoint on a surface $S_1$. Both are free-time, time-independent, with no terminal cost. Other cases are deduced later (§4.3.1) (pp. 81–83).
- Conclusions: the canonical equations (4.1) (the state equation $\dot x^*=H_p$ and the costate equation $\dot p^*=-H_x$, with Hamiltonian $H=\langle p,f\rangle+p_0L$), maximization of $H$ over $U$, $H\equiv 0$, and a nonzero pair $(p_0^*,p^*)$ with $p_0^*\le0$ (pp. 81–82).
- Variable endpoint adds transversality: $p^*(t_f)\perp T_{x^*(t_f)}S_1$ (the costate at the final time is orthogonal to the tangent space of $S_1$ at the final state). The freer the final state, the less free the costate (p. 83).
- Proof strategy: pass to Mayer form (add a state $x^0$ so that the cost becomes a terminal value), perturb the optimal control (time stretch plus short "needle" pulses of a different constant control), and propagate the perturbations with the variational equation (the linear equation for first-order deviations from the optimal trajectory) (pp. 84–91).
- Perturbations "add" by concatenation because the variational equation is linear. This gives a convex terminal cone $C_{t^*}$ (pp. 91–93).
- Optimality implies the downward ray $\vec\mu$ misses the interior of $C_{t^*}$ (Lemma 4.1). A separating hyperplane's normal gives $(p_0^*,p^*(t^*))$, which is propagated backward by the adjoint equation (pp. 93–97).
- Hamiltonian maximization comes from the sign of the inner product with needle perturbations. $H\equiv0$ comes from the temporal perturbation plus continuity and zero derivative of $m(x^*,p^*)$ (pp. 98–100).
- For the variable-endpoint case, Lemma 4.2 separates $C_{t^*}$ from a larger set $T$. This yields the inequality (4.38), the first step to transversality (pp. 100–101).

## L3 — Walkthrough

### 4.1 Statement (pp. 81–83)
Standing assumptions are those of §3.3. Two special problems are stated; §4.3.1 deduces other cases from them (p. 81).

**4.1.1 Basic Fixed-Endpoint Control Problem.** Here $f=f(x,u)$, $L=L(x,u)$, with $f,f_x,L,L_x$ continuous. The target is $S=[t_0,\infty)\times\{x_1\}$ (free time, fixed endpoint) and $K\equiv0$ (p. 81).

**Theorem.** Let $u^*:[t_0,t_f]\to U$ be globally optimal, with trajectory $x^*$. Then there exist $p^*:[t_0,t_f]\to\mathbb R^n$ and a constant $p_0^*\le0$ with $(p_0^*,p^*(t))\ne(0,0)$ for all $t$, such that (pp. 81–82):

1. The canonical equations hold, with $x^*(t_0)=x_0$, $x^*(t_f)=x_1$:
$$\dot x^*=H_p(x^*,u^*,p^*,p_0^*),\qquad \dot p^*=-H_x(x^*,u^*,p^*,p_0^*)\tag{4.1}$$
$$H(x,u,p,p_0):=\langle p,f(x,u)\rangle+p_0L(x,u).\tag{4.2}$$
2. For each $t$, $u\mapsto H(x^*(t),u,p^*(t),p_0^*)$ has a global maximum at $u^*(t)$: $H(x^*,u^*,p^*,p_0^*)\ge H(x^*,u,p^*,p_0^*)$ for all $t$ and all $u\in U$.
3. $H(x^*(t),u^*(t),p^*(t),p_0^*)=0$ for all $t\in[t_0,t_f]$.

Clarifications (p. 82):
- The conditions are necessary for global optimality. The proof will show they are also necessary for local optimality in the sense of §3.4.5; this is postponed to §4.3.
- $p_0^*$ is the *abnormal multiplier*. It equals 0 in degenerate cases. Otherwise $p_0^*\neq0$, and scaling to $p_0^*=-1$ recovers the earlier Hamiltonian (3.29). Unwritten $p_0$ means $-1$.
- $H\equiv0$ is said to be a special feature of free-time problems (explained in §4.3.1).
- Time-dependence and terminal cost cause no loss of generality. One adds the state $x_{n+1}:=t$ and uses $\hat L:=L+K_t+K_x\cdot f$ (this needs stronger regularity in $t$) (p. 82).

**4.1.2 Basic Variable-Endpoint Control Problem.** The target is $S=[t_0,\infty)\times S_1$, where $S_1=\{x: h_1(x)=\dots=h_{n-k}(x)=0\}$ is a $k$-dimensional surface, $h_i\in C^1$, and every point of $S_1$ is regular (pp. 82–83). The extremes are $k=n$ ($S_1=\mathbb R^n$, free endpoint) and $k=0$ (a point or isolated points). The conclusions are as above, with $x^*(t_f)\in S_1$ and one extra condition (p. 83):

4. **Transversality:**
$$\langle p^*(t_f),d\rangle=0\quad\forall d\in T_{x^*(t_f)}S_1,\tag{4.3}$$
$$T_{x^*(t_f)}S_1=\{d:\langle\nabla h_i(x^*(t_f)),d\rangle=0,\ i=1,\dots,n-k\}.\tag{4.4}$$
- (4.3) is equivalent to $p^*(t_f)$ being a linear combination of the $\nabla h_i(x^*(t_f))$.
- For $k=n$ it reduces to $p^*(t_f)=0$. For $S_1=\{x_1\}$ the tangent space is $0$, so the fixed-endpoint theorem is a special case.
- Boundary-condition count: $n$ at $t_0$ and $n$ at $t_f$ for the $2n$-dimensional system (4.1). Each extra degree of freedom of $x^*(t_f)$ removes one for $p^*(t_f)$.
- The principle came from the Pontryagin school in the late 1950s (book [PBGM62]); its origins trace to the calculus of variations (p. 83).

*Intuition note.* If the final state may lie anywhere on a surface $S_1$, the costate $p^*(t_f)$ must be perpendicular to the tangent space of $S_1$ there (4.3); when $S_1=\mathbb R^n$ this means $p^*(t_f)=0$ (p. 83). The proof of this is finished in part 2.

### 4.2 Proof: overview (p. 84)
The ten steps are: (1) Lagrange to Mayer form; (2) temporal perturbation; (3) spatial (needle) perturbation; (4) variational equation; (5) terminal cone; (6) key topological lemma; (7) separating hyperplane; (8) adjoint equation; (9) Hamiltonian properties; (10) transversality. Until Step 10, the problem is the fixed-endpoint one (p. 84). Exercise 4.2 (double integrator, time-optimal, $u^*\equiv1$ on $[0,2]$) is to be worked in parallel (p. 85).

**4.2.1 Lagrange to Mayer.** Add the state $x^0$ with $\dot x^0=L(x,u)$, $x^0(t_0)=0$, so that (p. 85):
$$\dot x^0=L(x,u),\quad \dot x=f(x,u)\tag{4.5}$$
$$J(u)=\int_{t_0}^{t_f}\dot x^0\,dt=x^0(t_f)\tag{4.6}$$
Cost is now a terminal cost. The target is $[t_0,\infty)\times S'$, where $S'$ is the line through $(0,x_1)$ parallel to the $x^0$-axis. Write $y:=(x^0,x)\in\mathbb R^{n+1}$, so that
$$\dot y=\begin{pmatrix}L(x,u)\\f(x,u)\end{pmatrix}=:g(y,u)\tag{4.7}$$
($g$ does not depend on $x^0$.) The optimal $y^*$ projects to $x^*$; $L$ need not be positive, so $x^{0,*}$ need not increase (p. 85). Write $t^*$ for the terminal time.
- Exercise 4.3: no trajectory from $y^*(t_1)$ can meet the vertical line through $y^*(t_2)$ below $y^*(t_2)$ (p. 86).
- For $t_2=t^*$ this is the *principle of optimality*: a final portion of an optimal trajectory is optimal for its own starting point (p. 86).
- The Hamiltonian is an inner product in $\mathbb R^{n+1}$:
$$H(x,u,p,p_0)=\Big\langle\begin{pmatrix}p_0\\p\end{pmatrix},\begin{pmatrix}L(x,u)\\f(x,u)\end{pmatrix}\Big\rangle.\tag{4.8}$$

**4.2.2 Temporal perturbation.** For $\tau\in\mathbb R$ and small $\varepsilon>0$, let $u_\tau(t):=u^*(\min\{t,t^*\})$ on $[t_0,t^*+\varepsilon\tau]$. For $\tau>0$ the control is held at its last value; for $\tau<0$ it is cut short (p. 87). By Taylor expansion,
$$y(t^*+\varepsilon\tau)=y^*(t^*)+\dot y(t^*)\varepsilon\tau+o(\varepsilon)=y^*(t^*)+g(y^*(t^*),u^*(t^*))\varepsilon\tau+o(\varepsilon)=:y^*(t^*)+\varepsilon\delta(\tau)+o(\varepsilon).\tag{4.9}$$
For $\tau<0$ the expansion of $y^*$ gives the same result. $\delta(\tau)$ is linear in $\tau$, and the points $y^*(t^*)+\varepsilon\delta(\tau)$ form a line $\vec\rho$ through $y^*(t^*)$. $\delta(\tau)$ gives only the direction, not the magnitude, of the terminal deviation (p. 87).

**4.2.3 Spatial (needle, Pontryagin–McShane) perturbation.** Take $w\in U$, $I=(b-\varepsilon a,b]\subset(t_0,t^*)$, with $a>0$ and $b\ne t^*$ a point of continuity of $u^*$. Define $u_{w,I}=w$ on $I$ and $u^*$ elsewhere (p. 87–88). Let $\approx$ mean equality up to $o(\varepsilon)$. Then:
- $y^*(b-\varepsilon a)\approx y^*(b)-\dot y^*(b)\varepsilon a$ (4.10), hence $y^*(b)\approx y^*(b-\varepsilon a)+g(y^*(b),u^*(b))\varepsilon a$ (4.11).
- $y(b)\approx y^*(b-\varepsilon a)+g(y^*(b-\varepsilon a),w)\varepsilon a$ (4.12), since $y(b-\varepsilon a)=y^*(b-\varepsilon a)$.
- Expanding the last term:
$$g(y^*(b-\varepsilon a),w)\varepsilon a\approx g(y^*(b),w)\varepsilon a+g_y(y^*(b),w)(y^*(b-\varepsilon a)-y^*(b))\varepsilon a\tag{4.13}$$
The second term is $O(\varepsilon^2)$ by (4.10), so it is dropped. Comparing with (4.11) (p. 89):
$$y(b)\approx y^*(b)+\nu_b(w)\varepsilon a\tag{4.14}$$
$$\nu_b(w):=g(y^*(b),w)-g(y^*(b),u^*(b)).\tag{4.15}$$
Meaning: the state difference is the velocity difference times the duration $\varepsilon a$.

**4.2.4 Variational equation.** For $b\le t\le t^*$ write $y(t)=y^*(t)+\varepsilon\psi(t)+o(\varepsilon)=:y(t,\varepsilon)$ (4.16). Then $\psi(b)=\nu_b(w)a$ (4.17) and $\psi(t)=y_\varepsilon(t,0)$ (4.18) (p. 89). Starting from $y(t,\varepsilon)=y(b,\varepsilon)+\int_b^tg(y(s,\varepsilon),u^*(s))ds$, differentiate in $\varepsilon$ at $\varepsilon=0$:
$$\psi(t)=\nu_b(w)a+\int_b^tg_y(y^*(s),u^*(s))\psi(s)\,ds.$$
Differentiating in $t$ (pp. 89–90):
$$\dot\psi=g_y(y^*,u^*)\psi=g_y|_*\psi\tag{4.19}$$
$$\dot\psi=A_*(t)\psi,\quad A_*(t):=g_y|_*(t)\tag{4.20}$$
This is the linearization of (4.7) around $y^*$. With $\psi=(\eta^0,\eta)$, $\dot\eta^0=(L_x)^T|_*\eta$ and $\dot\eta=f_x|_*\eta$. Shapes: $A_*$ is $(n{+}1)\times(n{+}1)$; $(L_x)^T$ is a $1\times n$ row; $f_x$ is $n\times n$:
$$A_*(t)=\begin{pmatrix}0&(L_x)^T|_*\\0&f_x|_*\end{pmatrix}.\tag{4.21}$$
Compared with (3.27): there, a perturbed control acts on a given trajectory; here, two trajectories share the same control. $\varepsilon$ plays the role of $\alpha$ in the variational approach (pp. 90–91).

With $\Phi_*(\cdot,\cdot)$ the transition matrix of (4.20) (p. 91):
$$y(t^*)=y^*(t^*)+\varepsilon\psi(t^*)+o(\varepsilon)\tag{4.22}$$
$$y(t^*)=y^*(t^*)+\varepsilon\Phi_*(t^*,b)\nu_b(w)a+o(\varepsilon)\tag{4.23}$$
$$\delta(w,I):=\Phi_*(t^*,b)\nu_b(w)a\tag{4.24}$$
so $y(t^*)=y^*(t^*)+\varepsilon\delta(w,I)+o(\varepsilon)$.

*Intuition note.* A short burst of a different control displaces the state by (velocity difference) × (duration). After that the displacement is carried to the end by the linearized dynamics along the optimal path.

*Skip path (Steps 2–4):* carry forward $\delta(\tau)$ from (4.9), $\delta(w,I)$ from (4.24), and the linearity of (4.19).

**4.2.5 Terminal cone.** The direction of $\delta(w,I)$ depends on $w,b$ but not on $a$. Let $\vec\rho(w,b)$ be the ray from $y^*(t^*)$ in that direction (unidirectional, since $a,\varepsilon>0$). Let $\vec P$ be the union of these rays over all $w,b$. $\vec P$ is a cone but not convex; for finite $U$ it is in general a union of isolated rays (p. 91).

*Adding needles.* For $b_1<b_2$ the intervals $I_1,I_2$ do not overlap for small $\varepsilon$. Perturb $u^*$ on both. By the formulas above, $y(b_1)=y^*(b_1)+\nu_{b_1}(w_1)\varepsilon a_1+o(\varepsilon)$ and
$$y(b_2)=y^*(b_2)+\varepsilon\big(\Phi_*(b_2,b_1)\nu_{b_1}(w_1)a_1+\nu_{b_2}(w_2)a_2\big)+o(\varepsilon).$$
Using the semigroup property $\Phi_*(t^*,b_2)\Phi_*(b_2,b_1)=\Phi_*(t^*,b_1)$ (p. 92):
$$y(t^*)=y^*(t^*)+\varepsilon\delta(w_1,I_1)+\varepsilon\delta(w_2,I_2)+o(\varepsilon).$$
To get weights $\beta_1,\beta_2>0$, use the intervals $\bar I_j=(b_j-\varepsilon\beta_ja_j,b_j]$. The construction extends to any positive linear combination. (Exercise 4.4 asks how to add two needles with $b_1=b_2$.) Concatenation therefore generates exactly the convex combinations of points of $\vec P$, i.e. the convex cone $\mathrm{co}(\vec P)$ (p. 92).

Adding the temporal line $\vec\rho$, the **terminal cone** $C_{t^*}$ is the set of points
$$y=y^*(t^*)+\varepsilon\Big(\beta_0\delta(\tau)+\sum_{i=1}^m\beta_i\delta(w_i,I_i)\Big),\tag{4.25}$$
with $\varepsilon>0$, $\beta_j\ge0$. It is a convex cone with vertex $y^*(t^*)$ (p. 93). For each $y\in C_{t^*}$ there is a control perturbation (concatenated needles, then a time shift of $\beta_0\varepsilon\tau$) with terminal point $y(t_f)=y+o(\varepsilon)$. This uses linearity of the variational equation and of $\delta(\tau)$ in $\tau$ (p. 93).

**4.2.6 Key topological lemma.** Optimality has not been used so far. It means no trajectory reaches $S'$ below $y^*(t^*)$ (p. 93). Let
$$\mu:=(-1\ \ 0\ \cdots\ 0)^T\in\mathbb R^{n+1}\tag{4.26}$$
and let $\vec\mu$ be the downward ray from $y^*(t^*)$.

**Lemma 4.1.** $\vec\mu$ does not intersect the interior of $C_{t^*}$ (p. 94).

Proof idea (pp. 94–95):
- Suppose it did. Then for some $\beta>0$ the terminal point would be $y^*(t^*)+\varepsilon\beta\mu+o(\varepsilon)$, i.e. $J(u)=J(u^*)-\varepsilon\beta+o(\varepsilon)$ and $x(t_f)=x_1+o(\varepsilon)$.
- This is not yet a contradiction, because $x(t_f)$ need not equal $x_1$.
- So take $\hat y=y^*(t^*)+\varepsilon\beta\mu$ with a ball $B_\varepsilon$ of radius $\varepsilon$ in $C_{t^*}$. Its points are $y^*(t^*)+\varepsilon\nu$, and the actual terminal points $y^*(t^*)+\varepsilon\nu+o(\varepsilon)$ form a "warped ball" $\tilde B_\varepsilon$ (4.27).
- Since the warping is $o(\varepsilon)$, for small $\varepsilon$ the set $\tilde B_\varepsilon$ still meets $\vec\mu$ below $y^*(t^*)$. Then some perturbed trajectory hits $x_1$ at lower cost, contradicting optimality.
- Why $\tilde B_\varepsilon$ has no "hole" the ray could go through: it is the image of the ball under a continuous warping map. It contains a ball around $\hat y_\varepsilon$ of radius of order $\varepsilon-o(\varepsilon)$. Brouwer's fixed point theorem gives a quick proof (Exercise 4.5). [PBGM62] calls this obvious and adds a footnote with a topological proof.

**4.2.7 Separating hyperplane.** The Separating Hyperplane Theorem says that two nonempty disjoint convex sets can be separated by a hyperplane, each lying in one closed half-space. $\vec\mu$ is convex, the interior of $C_{t^*}$ is convex, and by Lemma 4.1 they are disjoint. So a hyperplane separates $\vec\mu$ from $C_{t^*}$. It passes through $y^*(t^*)$ and need not be unique (p. 96). (Footnote 3: if the interior of $C_{t^*}$ is empty, a hyperplane containing $C_{t^*}$ works.) Let its nonzero normal be
$$\begin{pmatrix}p_0^*\\p^*(t^*)\end{pmatrix}\tag{4.28}$$
The separation reads
$$\Big\langle\begin{pmatrix}p_0^*\\p^*(t^*)\end{pmatrix},\delta\Big\rangle\le0\quad\forall\delta:\ y^*(t^*)+\delta\in C_{t^*}\tag{4.29}$$
$$\Big\langle\begin{pmatrix}p_0^*\\p^*(t^*)\end{pmatrix},\mu\Big\rangle\ge0.\tag{4.30}$$
The sign is a convention (flipping the normal reverses both). By (4.26), (4.30) says exactly $p_0^*\le0$, its only use. (4.28) is the terminal condition for the adjoint system (p. 96).

**4.2.8 Adjoint equation.** Systems $\dot x=Ax$ and $\dot z=-A^Tz$ are *adjoint*. Their inner product is constant: $\frac{d}{dt}\langle z,x\rangle=\langle\dot z,x\rangle+\langle z,\dot x\rangle=(-A^Tz)^Tx+z^TAx=0$ (p. 97). Take the variational equation as the $x$-system. The adjoint system is
$$\dot z=-A_*^T(t)z=\begin{pmatrix}0&0\\-L_x|_*&-(f_x)^T|_*\end{pmatrix}z.\tag{4.31}$$
With $z=(p_0,p)$: $\dot p_0=0$ and $\dot p=-L_x|_*p_0-(f_x)^T|_*p=-H_x(x^*,u^*,p,p_0)$. Set $z(t^*)$ equal to (4.28) and call the $p$-component $p^*$. Then $p_0(t)\equiv p_0^*$ and $\dot p^*=-H_x(x^*,u^*,p^*,p_0^*)$, the second canonical equation. The first holds by definition of $H$, which proves statement 1 (p. 97). The conserved product gives
$$\Big\langle\begin{pmatrix}p_0^*\\p^*(t)\end{pmatrix},\psi(t)\Big\rangle=\Big\langle\begin{pmatrix}p_0^*\\p^*(t^*)\end{pmatrix},\psi(t^*)\Big\rangle\quad\forall t\in[t_0,t^*]\tag{4.32}$$
for every solution $\psi$ of (4.19). Since (4.31) is homogeneous linear and (4.28) is nonzero,
$$\begin{pmatrix}p_0^*\\p^*(t)\end{pmatrix}\ne0\quad\forall t\in[t_0,t^*].\tag{4.33}$$

*Intuition note.* The costate is the normal of the separating hyperplane carried backward in time. The conserved inner product means a perturbation that ends on a given side of the hyperplane at $t^*$ was on that same side of the corresponding hyperplane at every earlier time (p. 97).

**4.2.9 Hamiltonian properties.**

*Statement 2 (maximization).* By (4.23) and (4.29), with $\varepsilon,a>0$: $\langle(p_0^*,p^*(t^*)),\Phi_*(t^*,b)\nu_b(w)\rangle\le0$. Applying (4.32) to the solution of (4.19) that equals $\nu_b(w)$ at time $b$ gives
$$\Big\langle\begin{pmatrix}p_0^*\\p^*(b)\end{pmatrix},\nu_b(w)\Big\rangle\le0.\tag{4.34}$$
Here $\nu_b(w)=(L(x^*(b),w)-L(x^*(b),u^*(b)),\ f(x^*(b),w)-f(x^*(b),u^*(b)))$. Expanding and using (4.8) (p. 98):
$$H(x^*(b),w,p^*(b),p_0^*)\le H(x^*(b),u^*(b),p^*(b),p_0^*).\tag{4.35}$$
This holds for all $w\in U$ and all continuity points $b\in(t_0,t^*)$. At discontinuities and at the endpoints, take limits of $b$ from the appropriate side. This uses the convention that $u^*$ equals a one-sided limit there, continuity of $x^*,p^*$, and continuity of $H$. So maximization holds everywhere (p. 98).

*Intuition note.* $H$ is the inner product of the augmented costate with the velocity of $y$. A needle perturbation moves the state in a direction with nonpositive inner product with the costate, so it can only lower $H$.

*Statement 3 ($H|_*\equiv0$).*
- *At $t^*$.* The temporal perturbation gives $\delta(\tau)=(L(x^*(t^*),u^*(t^*)),f(x^*(t^*),u^*(t^*)))\,\tau$. Since $\tau$ can have either sign, (4.29) forces the inner product with $(p_0^*,p^*(t^*))$ to be $0$. By (4.8), $H(x^*(t^*),u^*(t^*),p^*(t^*),p_0^*)=0$ (p. 99).
- *Continuity in time.* At a discontinuity $t$ of $u^*$, apply (4.35) with $b<t$, $w=u^*(t^+)$ and $b\uparrow t$: $H(\cdot,u^*(t^+),\cdot)\le H(\cdot,u^*(t^-),\cdot)$. Apply it with $b>t$, $w=u^*(t^-)$ and $b\downarrow t$: the reverse inequality. So the two values are equal (p. 99).
- *Constancy.* $H_u$ is not assumed to exist, so write $H|_*=m(x^*(t),p^*(t))$ with $m(x,p):=\max_{u\in U}H(x,u,p,p_0^*)$. For any $t,t'$ (4.36):
$$H(x^*(t'),u^*(t),p^*(t'),p_0^*)-H(x^*(t),u^*(t),p^*(t),p_0^*)\le m(x^*(t'),p^*(t'))-m(x^*(t),p^*(t))\le H(x^*(t'),u^*(t'),p^*(t'),p_0^*)-H(x^*(t),u^*(t'),p^*(t),p_0^*).$$
- By the standing assumptions and (4.1), $t\mapsto H(x^*(t),u^*(\bar t),p^*(t),p_0^*)$ is $C^1$ with derivative bounded independently of $\bar t$. With (4.36), $m(x^*,p^*)$ is locally Lipschitz, hence absolutely continuous and differentiable almost everywhere (p. 100).
- Exercise 4.6: its derivative is zero where it exists.
- $H|_*$ is $0$ at $t^*$, continuous, and has zero derivative almost everywhere, so it is identically $0$. This completes the fixed-endpoint proof (p. 100).

**4.2.10 Transversality (partial).** For the surface target, hitting a point with $x^0<x^{0,*}(t^*)$ and $x\in S_1$ (not necessarily $x^*(t^*)$) would contradict optimality. Let $D$ be the set of such points. Its linear approximation is
$$T:=\Big\{y\in\mathbb R^{n+1}:y=y^*(t^*)+\begin{pmatrix}0\\d\end{pmatrix}+\beta\mu,\ d\in T_{x^*(t^*)}S_1,\ \beta\ge0\Big\}.\tag{4.37}$$
$T$ is tangent to $D$ along $\vec\mu$; both extend infinitely downward, and $T$ contains its upper boundary while $D$ does not (p. 100).

**Lemma 4.2.** $T$ does not intersect the interior of $C_{t^*}$ (p. 100).

Proof, by generalizing Lemma 4.1 (pp. 100–101):
- Suppose not. Then a ball $B_\varepsilon$ around $\hat y_\varepsilon=y^*(t^*)+\varepsilon(0,d)+\varepsilon\beta\mu\in T$ lies in $C_{t^*}$. Move $\hat y_\varepsilon$ slightly down so it is not on the upper boundary.
- Its warped image $\tilde B_\varepsilon$ contains a ball around $\hat y_\varepsilon$ of radius of order $\varepsilon-o(\varepsilon)$.
- $T$ and $D$ are tangent along $\vec\mu$, so $\hat y_\varepsilon$ is within $o(\varepsilon)$ of $D$. Hence $\tilde B_\varepsilon$ meets $D$, contradicting optimality.

By Lemma 4.2 and the separating hyperplane theorem, a hyperplane separates $T$ from $C_{t^*}$. Its normal is again (4.28). Since $d=0\in T_{x^*(t^*)}S_1$, (4.29) and (4.30) still hold, so the proofs of statements 1–3 carry over. Taking vectors of $T$ with $\beta=0$ gives the new inequality
$$\Big\langle\begin{pmatrix}p_0^*\\p^*(t^*)\end{pmatrix},\begin{pmatrix}0\\d\end{pmatrix}\Big\rangle=\langle p^*(t^*),d\rangle\ge0\quad\forall d\in T_{x^*(t^*)}S_1.\tag{4.38}$$
(added step) Since the tangent space is a linear subspace, $-d$ also belongs to it, and applying (4.38) to $-d$ gives $\langle p^*(t^*),d\rangle\le0$; together this is (4.3). The text on these pages ends at (4.38).

## Toy example (ours, not from the text)
Problem: $n=1$, $\dot x=u$, $U=[-1,1]$, $L\equiv1$ (time-optimal), $x(0)=0$, target $x_1=1$. The optimal control is $u^*\equiv1$, $t^*=1$.

1. Augmented system: $y=(x^0,x)$, $g(y,u)=(1,u)$. Then $L_x=0$ and $f_x=0$, so $A_*=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ and $\Phi_*=I_2$.
2. Needle: $\nu_b(w)=g(y^*,w)-g(y^*,1)=(1,w)-(1,1)=(0,w-1)$. So $\delta(w,I)=(0,(w-1)a)$. For $w\in[-1,1]$ the second component is $-c$ with $c\ge0$.
3. Temporal: $\delta(\tau)=(1,1)\tau$.
4. Terminal cone (shifted to the origin): points $(s,\,s-c)$ with $s\in\mathbb R$, $c\ge0$, i.e. the half-plane $\{(\alpha,\gamma):\gamma\le\alpha\}$.
5. $\mu=(-1,0)$ has $\gamma=0>\alpha=-1$, so it lies outside the interior, as Lemma 4.1 says.
6. Separation (4.29): $p_0s+p(s-c)\le0$ for all $s\in\mathbb R$, $c\ge0$. This needs $p_0+p=0$ and $p\ge0$. (4.30): $-p_0\ge0$. Normalize $p_0^*=-1$, so $p^*(t^*)=1$.
7. Adjoint: $\dot p=-H_x=0$, so $p^*\equiv1$.
8. Check: $H=pu+p_0\cdot1=u-1$. On $[-1,1]$ this is maximized at $u=1=u^*$, and $H|_*=0$ ✓. Also (4.34): $\langle(-1,1),(0,w-1)\rangle=w-1\le0$ ✓.

## Concepts
- [[pontryagin-maximum-principle]] — necessary conditions for optimal control: canonical equations, $H$ maximized over $U$, $H\equiv0$ in free-time problems, transversality at a surface target (pp. 81–83)
- [[hamiltonian]] (new) — $H=\langle p,f\rangle+p_0L$, equivalently an inner product in $\mathbb R^{n+1}$ (pp. 81, 86)
- [[costate-adjoint-vector]] (new) — $p^*$ solving $\dot p=-H_x$, the normal of the separating hyperplane carried backward (pp. 96–97)
- [[abnormal-multiplier]] (new) — $p_0^*\le0$; if $\neq0$, normalize to $-1$ (p. 82)
- [[transversality-condition]] (new) — $p^*(t_f)\perp T_{x^*(t_f)}S_1$ (p. 83)
- [[needle-perturbation]] (new) — replace $u^*$ by a constant $w\in U$ on a short interval $(b-\varepsilon a,b]$ (p. 87)
- [[variational-equation]] (new) — $\dot\psi=g_y|_*\psi$, the linearization along $y^*$ (pp. 89–90)
- [[terminal-cone]] (new) — convex cone of first-order terminal perturbations from temporal plus needle perturbations (p. 93)
- [[separating-hyperplane-theorem]] (new) — disjoint nonempty convex sets can be separated by a hyperplane (p. 95)
- [[lagrange-to-mayer-form]] (new) — add $x^0$ with $\dot x^0=L$ so the cost is $x^0(t_f)$ (p. 85)
- [[principle-of-optimality]] — a final portion of an optimal trajectory is optimal for its own starting point (p. 86)
- [[linearization]] — the variational equation is the linearization of (4.7) around $y^*$ (p. 90)

## Canonical instances
- [[brachistochrone]] — Exercise 4.1: recover cycloids from the maximum principle (p. 82)
- [[double-integrator-time-optimal]] — Exercise 4.2: $\dot x_1=x_2,\dot x_2=u$, $u^*=1$, to be used to follow the proof (p. 85)

## Bridges (candidates)
- [structural-analogy] Costate $p^*$ and abnormal multiplier $p_0^*$ ↔ calculus of variations: Lagrange multipliers and $\lambda_0^*$ (§2.5), which the author points to (p. 82).
- [structural-analogy] Principle of optimality (Fig. 4.2) ↔ dynamic programming: the tail of an optimal plan is optimal.
- [same-math] Adjoint systems $\dot x=Ax$, $\dot z=-A^Tz$ with $\langle z,x\rangle$ constant ↔ linear systems theory: transposed dynamics. The calculation is general linear algebra.
- [metaphor] Needle perturbation: "try a different action briefly" ↔ exploration in reinforcement learning.

## Questions this raises
- Under what extra assumptions are these necessary conditions also sufficient?
- How is the principle adapted to fixed final time, non-autonomous problems, or a terminal cost (§4.3.1)?
- How can the proof be made rigorous with the warped ball and Brouwer's theorem (Exercise 4.5)?
- What does the local-optimality remark of §4.3 add to global necessity?

## Exercises worth doing
- Ex. 4.1 (p. 82) — use the principle on the brachistochrone; confirms cycloids — difficulty: medium
- Ex. 4.2 (p. 85) — specialize every proof step to the time-optimal double integrator, with numbers and figures — difficulty: medium
- Ex. 4.3 (p. 86) — geometric form of the principle of optimality — difficulty: easy
- Ex. 4.4 (p. 92) — add two needles with the same right endpoint $b$ — difficulty: medium
- Ex. 4.5 (p. 95) — rigorous intersection of the warped ball with $\vec\mu$ — difficulty: hard
- Ex. 4.6 (p. 100) — $m(x^*,p^*)$ has zero derivative — difficulty: medium

## Reading notes
- This unit is part 1 of Chapter 4. It starts at §4.1 (printed p. 81) and ends on printed p. 101, in the middle of §4.2.10, right after inequality (4.38). The conclusion of the transversality proof and §4.3 are in part 2. The final step "(4.38) ⇒ (4.3)" in L3 is marked as our added step.
- Page offset: printed = pdf − 10.
- The text layer is garbled in several places: the initial and final states of Exercise 4.2, the matrices in (4.21) and (4.31), and the figure labels (PSfrag residue). The page images were used to check these.
- Figures 4.1–4.12 are described only through their captions and text. Figure 4.13 is referenced on p. 101 but not shown on these pages.
