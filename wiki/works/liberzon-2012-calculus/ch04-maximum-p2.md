---
id: liberzon-2012-calculus/ch04-maximum-p2
work: liberzon-2012-calculus
unit: "Chapter 4 (part 2/2): end of the proof, 4.3 Discussion, 4.4 Time-optimal control, 4.5 Existence, 4.6 Notes"
pages: 102-124
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# The Maximum Principle (part 2/2): discussion, time-optimal control, existence

## L0 — One line
The maximum principle gives only necessary conditions; in time-optimal problems it gives bang-bang controls for the double integrator and for normal linear systems, nonlinear systems can have singular arcs that are detected through Lie brackets, and existence of an optimal control is tied to (compact) reachable sets.

## L1 — The gist (≤ 120 words)
How should the maximum principle be read, extended and applied? Its proof needs only a local optimality notion, between weak and strong minima. Changes of variables give versions for fixed time, time-dependent data, terminal cost and initial sets. For time-optimal problems, the double integrator and normal linear systems have bang-bang controls (only extreme values). Nonlinear systems may have singular arcs (u not fixed by a sign rule), detected through Lie brackets. Fuller's problem has infinitely many switches. Since a necessary condition can be useless if no optimum exists, Filippov's theorem (compact reachable sets) and a proof of existence for linear time-optimal problems are given. Candidates from the principle can mislead if no solution exists.

**Prerequisites:** the maximum principle for the basic fixed- and variable-endpoint problems (Hamiltonian, costate, adjoint equation, H ≡ 0, transversality); linear ODEs and the matrix exponential; Jacobian matrices; compact and convex sets.

## L2 — Key ideas
- The principle gives only necessary conditions; global optimality is not used in the proof, and the conditions stay necessary for local optimality (0-norm on x, $\mathcal L_1$ norm on u; the Hamiltonian maximization stays global) (pp. 102–103).
- Nontriviality $(p_0^*,p^*)\neq(0,0)$ holds for all t or for none. In time-optimal problems it forces $p^*(t)\ne0$ for all t (p. 103).
- Fixed time, time-dependent data, terminal cost and initial sets are handled by changes of variables (e.g. $x_{n+1}=t$). Each case changes only how H behaves, whether $p_0^*$ appears, or the transversality condition (pp. 104–107).
- Double integrator: the optimal control is bang-bang with at most one switch and can be written as state feedback via a switching curve Γ (pp. 107–109).
- For a hypercube U, normal linear systems (each input channel controllable) have bang-bang time-optimal controls with finitely many switches (pp. 110–111).
- For nonlinear affine systems, a singular arc is a stretch where the switching function vanishes identically, so the sign rule gives no information. For one input, its derivatives are expressed through iterated Lie brackets (pp. 113–116).
- Fuller's problem: optimal control with infinitely many switches (Zeno behavior) (pp. 116–117).
- Compact reachable sets are the author's 'refined guess' for when optimal controls exist; Filippov's theorem gives them under compact convex velocity sets (pp. 118–119). Existence is proved for linear time-optimal problems with compact convex U, if some control achieves the transfer (pp. 118–121).

## L3 — Walkthrough

### End of the proof for variable endpoints (p. 102)
For $d\in T_{x^*(t^*)}S_1$, also $-d\in T_{x^*(t^*)}S_1$. Combined with the separation inequality (4.38) (from the earlier part of the proof), this gives $\langle p^*(t^*),d\rangle=0$ for all such d. This is the transversality condition (4.3) (p. 102).

If $S_1=\mathbb R^n$ (free time, free endpoint), the separating hyperplane must be horizontal, so its normal is vertical and $p^*(t^*)=0$. This agrees with (4.3) since the tangent space is all of $\mathbb R^n$ (p. 102).

### 4.3 Discussion of the maximum principle
**Necessary, not sufficient.** The principle only singles out candidates, and an optimal control may not exist (Section 4.5). For many problems where an optimum does exist, the conditions are strong enough to help identify it, directly or after a routine elimination (p. 102).

**Local optimality.** The statement assumed a globally optimal $u^*$, but the proof does not use this (p. 103).
- The control perturbations differ from $u^*$ on a set of length of order ε, so the $\mathcal L_1$ distance is small.
- The perturbed trajectory is 0-norm close to $x^*$.
- The author says it can be shown that the conditions are necessary for local optimality when closeness is measured by the 0-norm for x and the $\mathcal L_1$ norm for u. The Hamiltonian maximization remains global.
- This notion lies between weak minima (0-norm for x and u) and strong minima (0-norm for x, no constraint on u).
- The conditions remain valid for strong minima. They are not valid for weak minima, because there the value w in a needle perturbation is no longer arbitrary: it must be close to $u^*(b)$ (p. 103).

*Intuition note.* Needle perturbations change u a lot on a tiny set of times. The state barely moves. So the principle stays valid for a minimum that is optimal only against such nearby controls (it fails for weak minima, where w must stay close to $u^*(b)$).

**Nontriviality.** The origin of $\mathbb R^{n+1}$ is an equilibrium of the linear adjoint equation (4.31). So if $(p_0^*,p^*)$ vanishes at one t it vanishes for all t. Thus "$\neq(0,0)$ for all t" is equivalent to "for some t". It is called nontriviality because $(p_0^*,p^*)\equiv(0,0)$ satisfies all statements trivially (p. 103).

If the running cost L is nowhere zero (e.g. time-optimal, $L\equiv1$), then $H|_*=\langle p^*,f|_*\rangle+p_0^*L|_*\equiv0$. If $p^*(t)=0$ at some t, then $p_0^*L|_*(t)=0$, so $p_0^*=0$, contradicting nontriviality. Hence $p^*(t)\ne0$ for all t (p. 103). Exercise 4.7 gives another case with terminal cost.

**Abnormal multiplier.** $p_0^*=0$ means the separating hyperplane is vertical. Its projection to x-space is a hyperplane in $\mathbb R^n$, and all perturbed controls must bring x to the same side of it. In a majority of problems this does not happen and $p_0^*=-1$ can be set. In the free-endpoint case $p_0^*\neq0$ (p. 104).

### 4.3.1 Changes of variables (p. 104)
Problems outside the two basic ones can be reduced to them by the changes of variables of Section 3.3, or one can adapt the proof. The text says this is why it is called a "principle" rather than a theorem: versions differ but share basic features (p. 104).

**Fixed terminal time $t_1$.** Temporal perturbations are inadmissible, so the line $\vec\rho$ of directions $\delta(\tau)$ is not used for the terminal cone. These were used only to show $H|_*(t^*)=0$. So H is constant along the optimal trajectory but not necessarily 0; all other conditions are unchanged (p. 104).

Check by reduction: add $x_{n+1}:=t$,
$$\dot x=f(x,u),\ x(t_0)=x_0;\qquad \dot x_{n+1}=1,\ x_{n+1}(t_0)=t_0 \tag{4.39}$$
with target set $[t_0,\infty)\times S_1\times\{t_1\}$ (original target $\{t_1\}\times S_1$). The new Hamiltonian is $\overline H=\langle p,f\rangle+p_{n+1}+p_0L=H+p_{n+1}$. The adjoint equation for $p^*$ is unchanged, and maximizing $\overline H$ implies maximizing H. Also $\overline H|_*=H|_*+p^*_{n+1}\equiv0$ and $\dot p^*_{n+1}=-\overline H_{x_{n+1}}|_*=-H_t|_*=0$, since H does not depend on t. So $H|_*=-p^*_{n+1}$ is constant. It need not be 0, since the final value of $x_{n+1}$ is fixed and transversality says nothing about $p^*_{n+1}$. This is consistent with Section 3.4.4 (p. 104).

**Time-dependent system and cost.** The same trick applies if f and/or L depend on t, with
$$H(t,x,u,p,p_0):=\langle p,f(t,x,u)\rangle+p_0L(t,x,u). \tag{4.40}$$
Everything above holds up to $\dot p^*_{n+1}=-H_t|_*$, which is no longer 0. So $H|_*=-p^*_{n+1}$ is not constant:
$$\frac{d}{dt}H|_*=H_t|_* \tag{4.41}$$
with $H|_*(t_f)=-p^*_{n+1}(t_f)$. If $t_f$ is free, then $x_{n+1}(t_f)$ is free, transversality gives $p^*_{n+1}(t_f)=0$, so $H|_*(t_f)=0$ and, integrating, $H|_*(t)=-\int_t^{t_f}H_t|_*(s)\,ds$. This agrees with (3.43) of the variational approach (its middle portion does not apply here). Following the original proof instead, the claim of Exercise 4.6 fails and only (4.41) holds; the author finds changing variables simpler and more reliable (p. 105).

**Terminal cost.** Take a free-time, free-endpoint Mayer problem ($L\equiv0$) with cost $K(x_f)$, K smooth. The terminal cone $C_{t^*}$ lives in $\mathbb R^n$. By optimality K should not decrease along any direction of the cone:
$$\langle -K_x(x^*(t^*)),\delta\rangle\le0\quad\forall\,\delta:\ x^*(t^*)+\delta\in C_{t^*}. \tag{4.42}$$
So $C_{t^*}$ lies on one side of the hyperplane with normal $-K_x(x^*(t^*))$, assumed nonzero. Comparing with the earlier inequality (4.29) suggests
$$p^*(t^*):=-K_x(x^*(t^*)). \tag{4.43}$$
In a free-endpoint problem the final costate must be fully determined, to give the right number of boundary conditions (pp. 105–106). The adjoint equation and Hamiltonian analysis then proceed as before, with
$$H(x,u,p)=\langle p,f(x,u)\rangle. \tag{4.44}$$
The inequality (4.30), which was used only to show $p_0^*\le0$, is not needed because there is no $p_0^*$ (p. 106).

This argument is not rigorous, so the author validates it by reduction. Write $K(x_f)=K(x_0)+\int_{t_0}^{t_f}\langle K_x(x),f(x,u)\rangle dt$. Dropping the constant $K(x_0)$ gives a Lagrange problem with $L=\langle K_x,f\rangle$. Its Hamiltonian is $\overline H=\langle\bar p,f\rangle+p_0\langle K_x,f\rangle=\langle\bar p+p_0K_x,f\rangle$. The maximum principle gives
$$\dot{\bar p}^*=-\overline H_x|_*=-(f_x)^T|_*\bar p^*-p_0^*K_{xx}|_*f|_*-p_0^*(f_x)^T|_*K_x|_*,\qquad \bar p^*(t_f)=0.$$
This final value shows $p_0^*\ne0$; normalize $p_0^*=-1$. Define
$$p^*(t):=\bar p^*(t)-K_x(x^*(t)), \tag{4.45}$$
whose final value matches (4.43) (p. 106). Exercise 4.7: verify $\dot p^*=-H_x|_*$ for (4.44) and that $p^*\ne0$.

Conclusion: H is maximized and equals 0 along the optimal trajectory. The statement for terminal cost is that of the Basic Variable-Endpoint problem with $p_0^*$ eliminated and transversality replaced by $p^*(t_f)=-K_x(x^*(t_f))$ (cf. (3.37)) (p. 106). Exercise 4.8 asks for the general case with $L(t,x,u)$, $K(x_f)$ and a k-dimensional surface $S_1$.

*Intuition note.* A terminal cost acts like a final "price" on the state. The costate at the end is just minus the slope of that cost, so the boundary condition for $p^*$ is fully determined.

**Initial sets.** Let $\binom{x_0}{x_f}$ belong to a surface $S_2\subset\mathbb R^{2n}$. This captures joint constraints; for a closed trajectory, $S_2$ is the diagonal. The transversality condition becomes
$$\Big\langle\begin{pmatrix}p^*(t_0)\\-p^*(t_f)\end{pmatrix},d\Big\rangle=0\quad\forall\,d\in T_{\binom{x^*(t_0)}{x^*(t_f)}}S_2. \tag{4.46}$$
There are still 2n boundary conditions in total, since each extra freedom in $x^*(t_0)$ adds one constraint on $p^*(t_0)$ (p. 107). Exercise 4.9 asks for a heuristic proof.

### 4.4 Time-optimal control problems (p. 107)
These illustrate the principle and bring in bang-bang controls and Lie brackets.

#### 4.4.1 Example: double integrator
The system is $\ddot x=u$, $u\in[-1,1]$ (4.47), a car with bounded acceleration. Goal: bring it to rest at $x=0$ in minimal time. In state form
$$\dot x_1=x_2,\quad\dot x_2=u \tag{4.48}$$
with $L\equiv1$ and $H=p_1x_2+p_2u+p_0$. The adjoint equation is
$$\begin{pmatrix}\dot p_1^*\\\dot p_2^*\end{pmatrix}=\begin{pmatrix}-H_{x_1}|_*\\-H_{x_2}|_*\end{pmatrix}=\begin{pmatrix}0\\-p_1^*\end{pmatrix}\tag{4.49}$$
So $p_1^*\equiv c_1$ and $p_2^*(t)=-c_1t+c_2$ (p. 108). Maximizing H over $U=[-1,1]$ gives
$$u^*(t)=\operatorname{sgn}(p_2^*(t))=\begin{cases}1&p_2^*>0\\-1&p_2^*<0\\?&p_2^*=0\end{cases}\tag{4.50}$$
If $p_2^*\equiv0$ on an interval, then $\dot p_2^*=-p_1^*\equiv0$ there too. But $p^*$ cannot vanish in a time-optimal problem (p. 103), so zeros of $p_2^*$ are isolated. Since $p_2^*$ is linear in t, it crosses 0 at most once. So $u^*$ takes only the values ±1 and switches at most once: it is bang-bang (p. 108).

*Intuition note.* The costate $p_2^*$ is a straight line. Its sign tells you whether to apply full acceleration or full braking, so the optimal strategy uses only these two extremes, with at most one switch (the initial sign depends on the initial state).

**Switching curve.** For $u\equiv1$: $\dot x=t+a$, $x=\tfrac12t^2+at+b$, hence $x=\tfrac12\dot x^2+c$ with $c=b-a^2/2$. For $u\equiv-1$: $x=-\tfrac12\dot x^2+c$ (parabola families, Figure 4.15 (a,b)). Only two of these trajectories reach the origin; their union is the switching curve $\Gamma$: $x=-\tfrac12|\dot x|\dot x$ (p. 109). The optimal strategy applies $u=1$ or $u=-1$ depending on whether the initial point is below or above Γ, switches on Γ, then follows Γ to the origin; no switching is needed if the start is on Γ. If the car moves away from the origin, it brakes, turns around and accelerates (a "false" switch, u stays constant), then u switches and it brakes again (p. 109).

The law is bang-bang and is a state feedback law. This is notable because in general the principle gives only an open-loop description, since $u^*(t)$ depends on the costate $p^*(t)$. Here that dependence disappears. State feedback representation in general is not treated, except in the exercises (p. 109). Exercise 4.10: hit the origin with arbitrary speed. Exercise 4.11: forced oscillator $\ddot x+x=u$ (p. 109).

#### 4.4.2 Bang-bang principle for linear systems
Let $\dot x=Ax+Bu$ (4.51), $x\in\mathbb R^n$, $u\in U=\{u\in\mathbb R^m:u_i\in[-1,1]\}$ (4.52). The aim is to steer $x_0\to x_1$ in minimal time. Assume some control achieves the transfer; Theorem 4.3 then guarantees a time-optimal $u^*:[t_0,t^*]\to U$ exists (p. 110). With $H=\langle p,Ax+Bu\rangle+p_0$, maximization gives
$$\langle p^*(t),Bu^*(t)\rangle=\max_{u\in U}\langle p^*(t),Bu\rangle\tag{4.53}$$
With $b_1,\dots,b_m$ the columns of B, the components of u can be chosen independently, so each term is maximized separately and
$$u_i^*(t)=\operatorname{sgn}\langle p^*(t),b_i\rangle=\begin{cases}1&\langle p^*,b_i\rangle>0\\-1&<0\\?&=0\end{cases}\tag{4.54}$$
The adjoint equation $\dot p^*=-A^Tp^*$ gives $p^*(t)=e^{A^T(t^*-t)}p^*(t^*)$, so $\langle p^*(t),b_i\rangle=\langle p^*(t^*),e^{A(t^*-t)}b_i\rangle$. This is real analytic in t. If it vanishes on an interval, it vanishes everywhere with all derivatives. At $t=t^*$:
$$\langle p^*(t^*),b_i\rangle=\langle p^*(t^*),Ab_i\rangle=\dots=\langle p^*(t^*),A^{n-1}b_i\rangle=0\tag{4.55}$$
Since $p^*(t^*)\ne0$ (p. 103), (4.55) is ruled out if $(A,b_i)$ is a controllable pair. If this holds for every i, the system is called **normal** (p. 111).

Under normality, each $\langle p^*(\cdot),b_i\rangle$ has finitely many zeros. So $u^*$ takes values only at vertices of the hypercube, has finitely many switches, and is uniquely determined elsewhere by (4.54). Controls with values in the set of vertices are called bang-bang. This is the **bang-bang principle for linear systems** (p. 111).

*Intuition note.* Analytic functions cannot vanish on an interval without vanishing identically. Controllability of each channel, together with $p^*(t^*)\ne0$, excludes that. So the sign of each switching function is decisive almost everywhere.

**Self-contained argument (p. 111–112).** The solution is $x(t)=e^{A(t-t_0)}x_0+\int_{t_0}^te^{A(t-s)}Bu(s)ds$. Define the reachable set
$$R^t(x_0):=\Big\{e^{A(t-t_0)}x_0+\int_{t_0}^te^{A(t-s)}Bu(s)ds:\ u(s)\in U\Big\}\tag{4.56}$$
Then
$$x_1=e^{A(t^*-t_0)}x_0+\int_{t_0}^{t^*}e^{A(t^*-s)}Bu^*(s)ds\in R^{t^*}(x_0)\tag{4.57}$$
and $t^*$ is the smallest t with $x_1\in R^t(x_0)$. So $x_1$ is a boundary point of $R^{t^*}(x_0)$; otherwise it could be reached sooner. The set is compact and convex (shown in Section 4.5), so a supporting hyperplane through $x_1$ exists. With a suitably chosen normal vector $p^*(t^*)$ to the supporting hyperplane: $\langle p^*(t^*),x_1\rangle\ge\langle p^*(t^*),x\rangle$ for all x in the set. Using (4.56)–(4.57) and $e^{A^T(t^*-s)}p^*(t^*)=p^*(s)$:
$$\int_{t_0}^{t^*}\langle p^*(s),Bu^*(s)\rangle ds\ge\int_{t_0}^{t^*}\langle p^*(s),Bu(s)\rangle ds\quad\forall u:[t_0,t^*]\to U.$$
From this, (4.53) can be recovered for (almost) all t (p. 112). Exercise 4.12: U the Euclidean unit ball, (A,B) controllable.

**Weaker bang-bang principle.** Normality is a strong assumption. A weaker version asks whether every state reachable by some control is reachable in the same time by a bang-bang control, i.e. reachable sets for bang-bang controls coincide with those for all controls. This holds for every linear system (no controllability assumption) and every U that is a convex polyhedron; the proof is in [Sus83, Section 8.1] and is not given here (p. 112).

#### 4.4.3 Nonlinear systems, singular controls, and Lie brackets
**Example 4.1.** $\dot x_1=x_2^2-1$, $\dot x_2=u$, $u\in[-1,1]$, from $\binom10$ to $\binom00$ in minimal time. The unique optimal control is $u^*\equiv0$: it reaches the origin along the $x_1$-axis in time 1, and any other control makes $x_2$ deviate and slows the decrease of $x_1$. Since 0 is interior to U, $u^*$ is not bang-bang (p. 112). Check with the principle: $H=p_1(x_2^2-1)+p_2u+p_0$, so (4.50) holds, and for $u^*$ to take the value 0, $p_2^*$ must vanish. $\dot p_1^*=0$ and $\dot p_2^*=-2p_1^*x_2^*$. Since $x_2^*\equiv0$, $p_2^*$ is constant. In a fixed-endpoint problem $p^*(1)$ is unconstrained, so $p_2^*(1)=0$ is allowed, giving $p_2^*\equiv0$ while $p_1^*$ may be nonzero. No contradiction (pp. 112–113).

When the function whose sign determines $u^*$ vanishes on an interval, the optimal control there is called **singular**, and that piece of trajectory a **singular arc** (p. 113).

**Affine systems.** Take
$$\dot x=f(x)+G(x)u=f(x)+\sum_{i=1}^mg_i(x)u_i\tag{4.59}$$
with $G$ an $n\times m$ matrix with columns $g_i$ and U the hypercube. As in 4.4.2, $u_i^*$ is determined by the sign of the **switching function** $\varphi_i(t):=\langle p^*(t),g_i(x^*(t))\rangle$. Assume $m=1$:
$$\varphi(t)=\langle p^*(t),g(x^*(t))\rangle,\qquad u^*=\operatorname{sgn}\varphi\ \text{(as in (4.50))}\tag{4.60, 4.61}$$
The canonical equations are $\dot x^*=f(x^*)+g(x^*)u^*$ and $\dot p^*=-H_x|_*=-(f_x)^T|_*p^*-(g_x)^T|_*p^*u^*$ (pp. 113–114). Then
$$\dot\varphi=\langle\dot p^*,g\rangle+\langle p^*,g_x\dot x^*\rangle=-\langle(f_x)^Tp^*,g\rangle|_*-\langle(g_x)^Tp^*,g\rangle|_*u^*+\langle p^*,g_xf\rangle|_*+\langle p^*,g_xg\rangle|_*u^*=\langle p^*,g_xf-f_xg\rangle|_*\tag{4.62}$$
(the u-terms cancel; added step: $\langle(f_x)^Tp,g\rangle=\langle p,f_xg\rangle$) (p. 114).

**Lie bracket.** For differentiable vector fields,
$$[f,g](x):=g_x(x)f(x)-f_x(x)g(x).$$
Example 4.2: for $f=Ax$, $g=Bx$ the system $\dot x=Ax+Bxu$ is bilinear (not linear), and $g_xf-f_xg=BAx-ABx=[B,A]x$ with matrix commutator $[B,A]:=BA-AB$. The sign conventions for matrices and for vector fields are usually opposite (p. 114).

Geometric meaning (Figure 4.16): flow along f for ε time units, then g, then −f, then −g. For small ε the net motion is approximately $\varepsilon^2[f,g](x_0)$, up to higher-order terms. If $[f,g]\equiv0$ near $x_0$, we return to $x_0$ and f, g **commute** (p. 114). Thus
$$\dot\varphi(t)=\langle p^*(t),[f,g](x^*(t))\rangle\tag{4.63}$$
Exercise 4.13: compute $\dot\varphi_i$ for the multi-input case (p. 115).

**Ruling out singularity.** For $\varphi\equiv0$ on an interval, $p^*$ must stay orthogonal to both g and $[f,g]$ along $x^*$. Since $p^*\neq0$ in time-optimal problems, singularity is ruled out for planar systems if g and $[f,g]$ are linearly independent along the optimal trajectory (p. 115). Otherwise (n > 2, or dependence) look at higher derivatives. For any differentiable $h:\mathbb R^n\to\mathbb R^n$, the same computation gives
$$\frac d{dt}\langle p^*,h(x^*)\rangle=\langle p^*,[f,h](x^*)\rangle+\langle p^*,[g,h](x^*)\rangle u^*\tag{4.64}$$
Setting $h=g$ gives (4.63), since $[g,g]=0$. Setting $h=[f,g]$:
$$\ddot\varphi=\langle p^*,[f,[f,g]](x^*)\rangle+\langle p^*,[g,[f,g]](x^*)\rangle u^*\tag{4.65}$$
A singular control must make $\ddot\varphi$ vanish. The candidate
$$u^*=-\frac{\langle p^*,[f,[f,g]](x^*)\rangle}{\langle p^*,[g,[f,g]](x^*)\rangle}\tag{4.66}$$
can potentially be singular if $\langle p^*,g\rangle=\langle p^*,[f,g]\rangle\equiv0$, but must satisfy $|u^*|\le1$. If, e.g., $[g,[f,g]]=\alpha g+\beta[f,g]+\gamma[f,[f,g]]$ with $|\gamma(x)|<1$ for all x, then (4.66) is inadmissible unless $\langle p^*,[f,[f,g]](x^*)\rangle\equiv0$; then one considers its derivative via (4.64) with $h=[f,[f,g]]$, and so on (p. 115). Exercise 4.14: continue this, using $(\mathrm{ad}f)^k(g)$ with $(\mathrm{ad}f)^0(g)=g$, $(\mathrm{ad}f)^k(g)=[f,(\mathrm{ad}f)^{k-1}(g)]$.

**Linear single-input case** ($f=Ax$, $g=b$): $[f,g]=-Ab$, $[f,[f,g]]=A^2b$, $[g,[f,g]]=0$, $[f,[f,[f,g]]]=-A^3b$, $[g,[f,[f,g]]]=0$. Brackets with two g's vanish, so the derivatives of φ do not depend on u. φ cannot vanish if $b,Ab,\dots,A^{n-1}b$ span $\mathbb R^n$, which is the controllability condition (pp. 115–116).

**Example 4.1 revisited.** $f=\binom{x_2^2-1}{0}$, $g=\binom01$, so
$$[f,g]=-\begin{pmatrix}0&2x_2\\0&0\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}-2x_2\\0\end{pmatrix}.$$
On the $x_1$-axis, $[f,g]=0$, so g and $[f,g]$ do not span $\mathbb R^2$. Next,
$$[f,[f,g]]=\begin{pmatrix}0&-2\\0&0\end{pmatrix}\begin{pmatrix}x_2^2-1\\0\end{pmatrix}-\begin{pmatrix}0&2x_2\\0&0\end{pmatrix}\begin{pmatrix}-2x_2\\0\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$
With $u\equiv0$, (4.65) gives $\ddot\varphi\equiv0$; all higher brackets vanish, so $\varphi\equiv0$ (p. 116).

Singular controls need not be complex. For single-input planar analytic systems $\dot x=f+gu$, $u\in[-1,1]$, time-optimal trajectories are said to be finite concatenations of bang pieces and analytic singular arcs ("it can be shown"). The author asks whether a similar finite-concatenation claim holds for other planar optimal control problems or for time-optimal problems in $\mathbb R^3$, and says the answer to both is negative (p. 116).

#### 4.4.4 Fuller's problem
Take the double integrator (4.48), $u\in[-1,1]$, cost $J=\int_{t_0}^{t_f}x_1^2dt$ (4.67), target $[t_0,\infty)\times\{0\}$ (free final time, final state the origin). Then $H=p_1x_2+p_2u+p_0x_1^2$, the switching function is $\varphi=p_2^*$, and
$$\dot p_1^*=-2p_0^*x_1^*,\qquad\dot p_2^*=-p_1^*\tag{4.68}$$
Singular arcs are ruled out: $p_2^*\equiv0$ forces $p_1^*$, $x_1^*$, $x_2^*$ to vanish, leaving only the trivial equilibrium (p. 116). So all optimal controls are bang-bang, with switches where $p_2^*=0$. Now $p_2^*$ is no longer linear in t, so one switch is not implied. Stated without proof (p. 116–117):
1. Optimal controls are bang-bang with infinitely many switches.
2. Switching occurs on $\{x_1+\gamma|x_2|x_2=0\}$, $\gamma\approx0.445$.
3. Time intervals between consecutive switches decrease in geometric progression.

This is consistent with finite final time (the origin is reachable in finite time, e.g. by the time-optimal control). Such switch times accumulating near the final time are called **Fuller's phenomenon** or **Zeno behavior**. The control is measurable but not piecewise constant (p. 117; Figure 4.17 is a sketch with slightly distorted curve, per the footnote).

The time-optimal problem has the same switching-curve formula but $\gamma=1/2$. Both embed in $J=\int|x_1|^\nu dt$: $\nu=0$ is time-optimal, $\nu=2$ is Fuller's. There is a bifurcation value $\bar\nu\approx0.35$: for $\nu\in[0,\bar\nu]$ the control is bang-bang with at most one switch, for $\nu>\bar\nu$ Fuller's phenomenon occurs (p. 117). Exercise 4.15 asks for a 3-dimensional time-optimal example with infinitely many switches.

*Intuition note.* With an integral cost on position, the costate is no longer a straight line, so the sign can flip repeatedly. Each switch is shorter than the last, and infinitely many fit before the finite arrival time.

### 4.5 Existence of optimal controls
**Perron's paradox (a farcical claim, not the author's).** "The largest positive integer is 1": let N be the largest; if $N\ne1$, $N^2>N$, contradiction; so $N=1$. The reasoning does show that $N=1$ is a necessary condition for optimality, but no solution exists. A necessary condition can be useless or misleading unless existence is known (p. 118).

For a problem as in Section 3.3, we must assume that at least one control drives $(t,x(t))$ from $(t_0,x_0)$ to S (a controllability-type assumption); otherwise the problem is ill posed (infinite cost). This is not enough (p. 118):
- **Example 4.3:** $\dot x=u$, $U=\mathbb R$, from 0 to 1 in minimal time. Arbitrarily small positive times are achievable, time 0 is not, so there is no optimum.
- **Example 4.4:** same with $U=[0,1)$. Any time larger than 1 works, time 1 does not (U not closed).

So compactness is the guess, applied to reachable sets $R^t(x_0)$ rather than to U. If $t^*$ is the fastest time, $x_1\in\partial R^{t^*}(x_0)$ (Figure 4.18). In Example 4.3, $R^t(x_0)=\mathbb R$ is unbounded. In Example 4.4, $R^1(x_0)=[0,1)$ is not closed, and for $t>1$ the point 1 is interior (p. 119).

**Filippov's theorem (p. 119).** Given a system in the standard form (3.18), assume solutions exist on $[t_0,t_f]$ for all controls and that $\{f(t,x,u):u\in U\}$ is compact and convex for every $(t,x)$. Then $R^t(x_0)$ is compact for each $t\in[t_0,t_f]$. Comments (p. 119):
- Controls are understood as measurable functions.
- The existence hypothesis is not implied by the second: $\dot x=x^2+u$ blows up in finite time even for $U=\{0\}$.
- The stronger statement is that the set of all trajectories is compact in $\mathcal C^0([t_0,t_f],\mathbb R^n)$ with the topology of uniform convergence.
- Boundedness holds without convexity. Convexity is crucial for closedness (via the separating hyperplane theorem).

Exercise 4.16: $\dot x_1=u$, $\dot x_2=x_1^2$, $U=\{-1,1\}$, shows non-closed reachable sets and the role of convexification.

For affine systems (4.59) with compact convex U, $\{f(x)+G(x)u\}$ is the affine image of U, hence compact and convex. For linear systems, global existence of solutions is automatic and $R^t(x_0)$ is also convex, from convexity of U and the variation-of-constants formula (p. 120).

**Mayer problems.** For $J=K(x_f)$ with K continuous, Filippov's hypotheses and target $\{t_1\}\times\mathbb R^n$: by the Weierstrass theorem K has a global minimum on the compact $R^{t_1}(x_0)$, and any control reaching it is optimal. Some Bolza problems can use compactness of trajectories plus the infinite-dimensional Weierstrass theorem, or be reduced to Mayer form (p. 120).

**Theorem 4.3 (existence of time-optimal controls, linear systems).** Let (4.51) have compact convex U, steer $x_0\to x_1$ in minimal time, and assume $x_1\in R^t(x_0)$ for some $t\ge t_0$. Then a time-optimal control exists (p. 120).

*Proof (key steps, pp. 120–121).*
1. $t^*:=\inf\{t\ge t_0:x_1\in R^t(x_0)\}$ is well defined (the set is nonempty). It suffices to show $x_1\in R^{t^*}(x_0)$.
2. Choose $t_k\searrow t^*$ and controls $u_k$ with $x_1=e^{A(t_k-t_0)}x_0+\int_{t_0}^{t_k}e^{A(t_k-s)}Bu_k(s)ds$.
3. Truncate at $t^*$ so the points lie in one reachable set:
$$x^k:=e^{A(t^*-t_0)}x_0+\int_{t_0}^{t^*}e^{A(t^*-s)}Bu_k(s)ds\in R^{t^*}(x_0)\tag{4.69}$$
4. With $\varepsilon_k:=t_k-t^*$ and $s=t^*+\tau$:
$$x_1-x^k=(e^{A\varepsilon_k}-I)x^k+\int_0^{\varepsilon_k}e^{A(\varepsilon_k-\tau)}Bu_k(t^*+\tau)d\tau$$
so
$$|x_1-x^k|\le\|e^{A\varepsilon_k}-I\||x^k|+\varepsilon_k\max\{|e^{A\delta}Bu|:\delta\in[0,\varepsilon_k],u\in U\}\tag{4.70}$$
5. From (4.69), $|x^k|\le\|e^{A(t^*-t_0)}\||x_0|+(t^*-t_0)\max\{|e^{A\delta}Bu|:\delta\in[0,t^*-t_0],u\in U\}$, independent of k. Since $\varepsilon_k\to0$ and $\|e^{A\varepsilon_k}-I\|\to0$, $|x_1-x^k|\to0$.
6. Closedness of $R^{t^*}(x_0)$ then gives $x_1\in R^{t^*}(x_0)$. ∎

Existence proofs are usually not constructive, but knowing a solution exists removes the risk of Perron's paradox and justifies applying the principle (p. 121).

### 4.6 Notes and references (pp. 121–123)
Bibliographic notes. Items mentioned in the notes (with references, not proved here): with all eigenvalues of A real, each control component switches at most $n-1$ times; the weaker bang-bang principle holds for time-varying linear systems and compact convex U (bang-bang meaning values in extreme points), with less elementary proofs; convexity of U in Theorem 4.3 can be dropped; the book's basic setting (piecewise continuous controls, $C^1$ systems, first-order analysis) is not the most general (pp. 122–123).

## Toy example (ours)
**Scalar normal linear system.** $\dot x=-x+u$, $u\in[-1,1]$, $x_0=0$. Steer to $x_1=0.5$ in minimal time ($n=m=1$, $A=-1$, $B=1$).
- Controllability: $(A,b)=(-1,1)$ is a controllable pair, so the system is normal.
- Adjoint: $\dot p=-A^Tp=p$, so $p^*(t)=e^{t-t^*}p^*(t^*)$, never zero and of constant sign. So $u^*=\operatorname{sgn}p^*(t^*)$ is constant: bang-bang with no switch.
- Reachable set: $x(t)=\int_0^te^{-(t-s)}u(s)ds\le\int_0^te^{-(t-s)}ds=1-e^{-t}$. So $R^t(0)=[-(1-e^{-t}),\,1-e^{-t}]$.
- Time: the target 0.5 is on the boundary when $1-e^{-t}=0.5$, i.e. $t^*=\ln2\approx0.693$. At $t=0.5$ the bound is $1-0.6065=0.3935<0.5$, so it is too early.
- Hence $u^*\equiv1$ (so $p^*(t^*)>0$, an outward normal of the reachable set at $x_1$).

**Double-integrator check of Γ.** Start at $(x,\dot x)=(1,0)$. Use $u=-1$: $x=1-t^2/2$, $\dot x=-t$. On Γ with $\dot x<0$: $x=-\tfrac12|\dot x|\dot x=\tfrac12\dot x^2$. So $1-t^2/2=t^2/2$, giving $t=1$, point $(\tfrac12,-1)$. Then $u=+1$: $\dot x=-1+s$ vanishes at $s=1$, and $x=\tfrac12-s+s^2/2=0$ at $s=1$. Total time 2, one switch.

## Concepts
- [[pontryagin-maximum-principle]] — necessary conditions via H maximization, costate, transversality; here extended and applied (p. 102)
- [[nontriviality-condition]] (new) — $(p_0^*,p^*)\neq(0,0)$; holds for all t iff for some t (p. 103)
- [[transversality-condition]] (new) — costate orthogonal to the tangent space of the target set; modified for terminal cost and initial sets (pp. 102, 106–107)
- [[abnormal-multiplier]] (new) — $p_0^*=0$, vertical separating hyperplane; usually $p_0^*=-1$ (p. 104)
- [[costate]] (new) — adjoint vector $p^*$ of the Hamiltonian system (p. 108)
- [[bang-bang-control]] (new) — control taking values only at vertices (extremes) of U (pp. 108, 111)
- [[switching-function]] (new) — $\varphi=\langle p^*,g(x^*)\rangle$ whose sign determines $u^*$ (p. 113)
- [[singular-control]] (new) — $u^*$ on an interval where the switching function vanishes identically (p. 113)
- [[lie-bracket]] (new) — $[f,g]=g_xf-f_xg$; its iterates govern the derivatives of φ (p. 114)
- [[normal-linear-system]] (new) — each pair $(A,b_i)$ controllable (p. 111)
- [[controllability]] — here: some control achieves the transfer (existence) and $(A,b_i)$ controllable (normality) (pp. 111, 118)
- [[reachable-set]] (new) — $R^t(x_0)$, states reachable at time t; the time-optimal endpoint lies on its boundary (pp. 111, 118)
- [[filippov-theorem]] (new) — compact convex velocity sets give compact reachable sets, given that solutions exist on the interval (p. 119)
- [[fuller-phenomenon]] (new) — infinitely many switches accumulating near the final time (Zeno behavior) (p. 117)
- [[open-loop-vs-closed-loop]] — the principle gives open-loop controls; the double-integrator solution is state feedback (p. 109)
- [[state-feedback]] — here: $u^*$ expressed via Γ as a function of state (p. 109)

## Canonical instances
- [[double-integrator-time-optimal]] — bang-bang, one switch, switching curve Γ (pp. 107–109)
- [[example-4-1-singular-arc]] — optimal $u^*\equiv0$ in the interior of U; singularity encoded in Lie brackets (pp. 112–116)
- [[fullers-problem]] — infinitely many switches, γ ≈ 0.445 (pp. 116–117)
- [[perrons-paradox]] — "largest integer is 1": necessary condition without existence (p. 118)
- [[integrator-nonexistence-examples]] — Examples 4.3, 4.4: unbounded and non-closed U (p. 118)

## Bridges (candidates)
- [structural-analogy] Zeno behavior in Fuller's problem ↔ hybrid systems: infinitely many switches in finite time.
- [structural-analogy] Costate as normal of a supporting hyperplane of the reachable set ↔ economics: shadow price on a constrained set.
- [structural-analogy] Switching curve Γ as a state-feedback policy ↔ dynamic programming: optimal policy as a function of state.
- [structural-analogy] Lie bracket as non-commutativity of flows ↔ controllability theory: brackets generate new reachable directions.

## Questions this raises
- When can the state-feedback form seen for the double integrator be obtained for time-optimal controls in general (pp. 109, 122)?
- Is there a nonlinear counterpart of normality that guarantees bang-bang optimal controls for affine systems (p. 113)?
- How does the "bifurcation" between one switch and Zeno behavior arise as ν grows (p. 117)?
- Can existence be shown for more general Bolza problems and target sets (pp. 120, 122)?

## Exercises worth doing
- Ex. 4.7 (p. 106) — verify the terminal-cost costate (4.45) satisfies the canonical equation; $p^*\neq0$ — medium
- Ex. 4.10 (p. 109) — "slam into a wall" variant of the double integrator; feedback form — medium
- Ex. 4.11 (p. 109) — time-optimal control of the forced harmonic oscillator — hard
- Ex. 4.14 (p. 115) — conditions via $(\mathrm{ad}f)^k$ that rule out singular controls — hard
- Ex. 4.15 (p. 117) — 3D time-optimal example with Fuller's phenomenon — hard
- Ex. 4.16 (p. 119) — non-closed reachable sets and the role of convexity — medium

## Reading notes
- This unit is part 2 of Chapter 4. It starts mid-proof (last lines of the proof of Lemma 4.2 / the variable-endpoint principle, printed p. 102) and ends with Section 4.6 on p. 123. Printed p. 124 contains only a running header. Section 4.3 starts on p. 102, so the unit begins inside the proof that precedes it.
- Printed = pdf − 10 (the labels give printed numbers directly).
- References such as (4.29), (4.30), (4.31), (4.38), Lemma 4.2, Exercise 4.6 refer to the earlier part of the chapter and are not restated in these pages. I flag them as such.
- The sentence in Section 4.6 that a necessary condition for controllability of linear systems with bounded controls is that A has purely imaginary eigenvalues is reported as printed (p. 123); I did not verify it.
- In the double-integrator text (p. 108) the printed sign function $\operatorname{sgn}$ is written with "?" for the zero case. Part of Figure 4.17 is described as slightly distorted by the author's footnote (p. 117).
- Section 4.6 is condensed here, since it is bibliographic.
