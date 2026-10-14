---
id: strogatz-2024-nonlinear/ch06-phase-p1
work: strogatz-2024-nonlinear
unit: "6 Phase Plane (part 1/2): 6.0–6.7 (ends inside Section 6.7, at the damping energy computation)"
pages: 146–173
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Phase Plane (part 1): fixed points, linearization, conservative and reversible systems

## L0 — One line
Near a fixed point of a 2-D system, the Jacobian's eigenvalues give the local picture, except in marginal cases such as centers, which conservation or reversibility can protect.

## L1 — The gist (≤ 120 words)
Nonlinear 2-D systems rarely have explicit solutions, so the chapter finds the qualitative phase portrait from the vector field. Uniqueness means trajectories never cross. Linearizing at a fixed point gives the correct type (saddle, node, spiral) when the fixed point is not marginal; centers are fragile. Examples: rabbits vs. sheep (basins, stable manifolds, competitive exclusion), conservative systems (energy contours, homoclinic orbits that start and end at one fixed point), reversible systems (twin trajectories), and the pendulum (librations = small oscillations, rotations = full turns over the top, cylinder phase space). Basins and their boundaries partition the phase plane into regions of different long-term behavior.

**Prerequisites:** 1-D flows and linearization (Ch. 2); eigenvalues, trace τ and determinant Δ, linear 2-D classification (Ch. 5); partial derivatives; chain rule.

## L2 — Key ideas (5–10 bullets)
- Phase portraits are built from fixed points, closed orbits, the flow near them, and their stability; nullclines (curves where $\dot x=0$ or $\dot y=0$) and direction fields (short segments showing flow direction) help sketch them (pp. 147–149).
- If $\dot{\mathbf x}=\mathbf f(\mathbf x)$ is continuously differentiable, solutions exist and are unique, so trajectories never intersect (p. 150).
- The linearization by the Jacobian matrix (partial derivatives of the vector field at the fixed point) is correct for saddles, nodes and spirals but can fail for centers, stars, degenerate nodes and non-isolated fixed points (p. 152). Hyperbolic means Re λ ≠ 0 (p. 156).
- Rabbits vs. sheep: two stable nodes and a saddle. The saddle's stable manifold (the trajectories flowing into it) is the basin boundary (it separates the starting points that go to each node), and one species generally drives the other to extinction (pp. 157–160).
- Conservative systems have a conserved energy-like quantity. They cannot have attracting fixed points, and an isolated fixed point that is a local minimum of $E$ is a center (pp. 160–164).
- Reversible systems ($t\to-t$, $y\to-y$) also keep centers robust. Homoclinic orbits (start and end at the same fixed point) and heteroclinic orbits (join two different fixed points) are much more common in conservative and reversible systems than in other systems (pp. 165–168).
- The pendulum is both reversible and conservative. Its natural phase space is a cylinder. Small linear damping turns centers into stable spirals and makes energy fall (pp. 169–173).

## L3 — Walkthrough

### 6.0 Introduction (p. 146)
The chapter studies 2-D nonlinear systems: general properties, classification of fixed points using Chapter 5, examples (biology and physics), and index theory at the end. This part covers 6.0–6.7. The chapter is mainly about fixed points; closed orbits and bifurcations come in later chapters (p. 146).

### 6.1 Phase Portraits (pp. 146–149)
The system is $\dot x_1=f_1(x_1,x_2)$, $\dot x_2=f_2(x_1,x_2)$, or $\dot{\mathbf x}=\mathbf f(\mathbf x)$. A phase point flows along the vector field and traces a trajectory. The plane is filled with trajectories because every point can be an initial condition (pp. 146–147).

For nonlinear systems there is typically no hope of finding trajectories analytically. The goal is the qualitative phase portrait from the properties of $\mathbf f$ (p. 147). Its main features (p. 147):
1. Fixed points: $\mathbf f(\mathbf x^*)=\mathbf 0$ (steady states).
2. Closed orbits: periodic solutions, $\mathbf x(t+T)=\mathbf x(t)$ for some $T>0$.
3. The arrangement of trajectories near them.
4. Their stability. In Fig. 6.1.2, A, B, C are unstable and the closed orbit D is stable.

**Numerics.** The Section 2.8 methods work with numbers replaced by vectors. The author always uses vector Runge–Kutta (p. 148):
$$\mathbf x_{n+1}=\mathbf x_n+\tfrac16(\mathbf k_1+2\mathbf k_2+2\mathbf k_3+\mathbf k_4),$$
$$\mathbf k_1=\mathbf f(\mathbf x_n)\Delta t,\ \mathbf k_2=\mathbf f(\mathbf x_n+\tfrac12\mathbf k_1)\Delta t,\ \mathbf k_3=\mathbf f(\mathbf x_n+\tfrac12\mathbf k_2)\Delta t,\ \mathbf k_4=\mathbf f(\mathbf x_n+\mathbf k_3)\Delta t.$$
A step $\Delta t=0.1$ usually suffices. A direction field (short segments showing flow direction) is clearer than a grid of arrows (p. 148).

**Example 6.1.1:** $\dot x=x+e^{-y}$, $\dot y=-y$ (pp. 148–149).
- The only fixed point is $(-1,0)$.
- $y(t)=y_0e^{-t}\to0$, so $e^{-y}\to1$ and $\dot x\approx x+1$ grows exponentially. On the x-axis ($y_0=0$), $\dot x=x+1$ exactly, so the fixed point is unstable.
- Nullclines are curves where $\dot x=0$ or $\dot y=0$, so the flow is vertical or horizontal there. Here $\dot y=0$ on $y=0$, with flow to the right where $x>-1$. $\dot x=0$ on the curve $x+e^{-y}=0$, with flow downward where $y>0$.
- The nullclines split the plane into sign regions. The computer plot shows a nonlinear version of a saddle point (p. 149).

*Intuition note:* You can learn a lot about a portrait without solving anything. Find fixed points, test stability, and use nullclines to see where the arrows point.

### 6.2 Existence, Uniqueness, and Topological Consequences (p. 150)
**Theorem (existence and uniqueness).** Take $\dot{\mathbf x}=\mathbf f(\mathbf x)$, $\mathbf x(0)=\mathbf x_0$. Suppose $\mathbf f$ and all $\partial f_i/\partial x_j$ are continuous on an open connected set $D\subset\mathbb R^n$. Then for $\mathbf x_0\in D$ there is a solution on some interval $(-\tau,\tau)$, and it is unique (p. 150). So continuous differentiability suffices; stronger versions exist (p. 150). From here on the author assumes smooth enough fields.

**Corollary:** different trajectories never intersect, since a crossing would give two solutions from one point (p. 150). So portraits do not become snarls of crossing curves.

In 2-D this has strong topological consequences. A trajectory starting inside a closed orbit C stays trapped inside. By the Poincaré–Bendixson theorem (discussed in Section 7.3), a trajectory confined to a closed, bounded region with no fixed points must eventually approach a closed orbit (p. 150).

*Intuition note:* A trajectory cannot move in two directions at once. In the plane, trajectories that cannot cross are also trapped inside a closed orbit.

### 6.3 Fixed Points and Linearization (pp. 151–156)
Take $\dot x=f(x,y)$, $\dot y=g(x,y)$ with fixed point $(x^*,y^*)$. Let $u=x-x^*$, $v=y-y^*$. Then (p. 151):
$$\dot u=\dot x=f(x^*+u,y^*+v)=f(x^*,y^*)+u\frac{\partial f}{\partial x}+v\frac{\partial f}{\partial y}+O(u^2,v^2,uv)=u\frac{\partial f}{\partial x}+v\frac{\partial f}{\partial y}+O(u^2,v^2,uv).$$
The partial derivatives are numbers evaluated at the fixed point. The same holds for $\dot v$ with $g$. Hence (p. 152):
$$\begin{pmatrix}\dot u\\ \dot v\end{pmatrix}=\begin{pmatrix}\partial f/\partial x&\partial f/\partial y\\ \partial g/\partial x&\partial g/\partial y\end{pmatrix}\begin{pmatrix}u\\ v\end{pmatrix}+\text{quadratic terms}\tag{1}$$
The matrix $A$, evaluated at $(x^*,y^*)$, is the **Jacobian matrix**, the analog of $f'(x^*)$. Dropping the quadratic terms gives the **linearized system**
$$\begin{pmatrix}\dot u\\ \dot v\end{pmatrix}=A\begin{pmatrix}u\\ v\end{pmatrix}\tag{2}$$
Shapes: $A$ is $2\times2$; $(u,v)^T$ is $2\times1$.

**When is this safe?** Yes, as long as the linearized fixed point is not a borderline case from Section 5.2. If the linearization predicts a saddle, node or spiral, the nonlinear fixed point really is one (proof cited: Andronov et al. 1973). Borderline cases (centers, degenerate nodes, stars, non-isolated fixed points) can be altered by small nonlinear terms (p. 152).

**Example 6.3.1:** $\dot x=-x+x^3$, $\dot y=-2y$ (p. 153).
- Fixed points: $(0,0)$, $(1,0)$, $(-1,0)$.
- Jacobian: $A=\begin{pmatrix}-1+3x^2&0\\0&-2\end{pmatrix}$.
- At $(0,0)$, $A=\mathrm{diag}(-1,-2)$: stable node. At $(\pm1,0)$, $A=\mathrm{diag}(2,-2)$: saddles.
- Check: the equations are uncoupled. Lines $x=0,\pm1$ and $y=0$ are invariant. The portrait is symmetric under $x\to-x$ and $y\to-y$ (Fig. 6.3.1). This confirms the linearization.

**Example 6.3.2:** $\dot x=-y+ax(x^2+y^2)$, $\dot y=x+ay(x^2+y^2)$ (p. 154).
- Linearization at the origin: $\dot x=-y$, $\dot y=x$, so $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\tau=0$, $\Delta=1>0$. The linearization predicts a center at the origin for every $a$ (incorrectly, as the polar form below shows).
- Polar coordinates: from $x\dot x+y\dot y=r\dot r$, $r\dot r=a(x^2+y^2)^2=ar^4$, so $\dot r=ar^3$. The author leaves $\dot\theta=(x\dot y-y\dot x)/r^2$ to Exercise 6.3.12. Substitution gives $\dot\theta=1$.
- Result (p. 155): if $a<0$, $r\to0$ monotonically: stable spiral (decay extremely slow). If $a=0$: center. If $a>0$, $r\to\infty$: unstable spiral. Centers are delicate because trajectories must close perfectly after one cycle.

Stars and degenerate nodes can also be altered, but their stability does not change. For example, a stable star may become a stable spiral but not an unstable spiral (Exercise 6.3.11). They live squarely in the stable or unstable region of Fig. 5.2.8, whereas centers sit on the edge (p. 155).

**Coarse classification by stability (p. 155):**
- Robust: repellers/sources (both Re λ > 0); attractors/sinks (both Re λ < 0); saddles (one positive, one negative eigenvalue).
- Marginal: centers (both eigenvalues pure imaginary); higher-order and non-isolated fixed points (at least one eigenvalue zero). So marginal cases have at least one eigenvalue with Re λ = 0.

**Hyperbolic fixed points, topological equivalence, structural stability (p. 156).**
- A fixed point is *hyperbolic* (the author calls the name unfortunate) if Re λ ≠ 0 for both eigenvalues. Hyperbolic fixed points keep their stability type under small nonlinear terms. This is the analog of $f'(x^*)\ne0$ in 1-D.
- For an nth-order system, hyperbolic means Re λ_i ≠ 0 for all i. The **Hartman–Grobman theorem** says the local portrait near a hyperbolic fixed point is topologically equivalent to that of the linearization.
- *Topologically equivalent* means a homeomorphism (continuous deformation with continuous inverse) maps trajectories onto trajectories and preserves the direction of time. Bending is allowed, ripping is not: closed orbits stay closed and saddle connections stay unbroken.
- A portrait is *structurally stable* if an arbitrarily small perturbation of the vector field cannot change its topology. A saddle is structurally stable; a center is not, since arbitrarily small damping makes it a spiral.

*Intuition note:* Linearization is trustworthy for the stability type unless some eigenvalue has zero real part. In that marginal case small nonlinear terms can change the outcome (a center may become a spiral).

### 6.4 Rabbits versus Sheep (pp. 156–160)
Lotka–Volterra competition for one limited food supply, ignoring predators and seasons. Two assumptions (pp. 156–157): each species would grow logistically to its carrying capacity alone (rabbits with a higher intrinsic growth rate). Encounters occur at a rate proportional to the size of each population and reduce both growth rates, rabbits' more severely. The model, with $x,y\ge0$ (p. 157):
$$\dot x=x(3-x-2y),\qquad \dot y=y(2-x-y)$$
$x$ = rabbits, $y$ = sheep. The coefficients are chosen to fit the story but are otherwise arbitrary (p. 157).

Fixed points: $(0,0),(0,2),(3,0),(1,1)$. Jacobian:
$$A=\begin{pmatrix}3-2x-2y&-2x\\-y&2-x-2y\end{pmatrix}$$
- $(0,0)$: $A=\mathrm{diag}(3,2)$, an unstable node. Trajectories leave tangent to the slow eigendirection, the one with the smallest $|\lambda|$ ($\lambda=2$, $\mathbf v=(0,1)$) (p. 157).
- $(0,2)$: $A=\begin{pmatrix}-1&0\\-2&-2\end{pmatrix}$, $\lambda=-1,-2$ (triangular matrix). Stable node; approach along the $\lambda=-1$ direction $\mathbf v=(1,-2)$ (p. 158).
- $(3,0)$: $A=\begin{pmatrix}-3&-6\\0&-1\end{pmatrix}$, $\lambda=-3,-1$. Stable node; approach along the slow direction $\mathbf v=(3,-1)$ (p. 158).
- $(1,1)$: $A=\begin{pmatrix}-1&-2\\-1&-1\end{pmatrix}$, $\tau=-2$, $\Delta=-1$, $\lambda=-1\pm\sqrt2$. Saddle (p. 158).

The axes contain straight-line trajectories ($\dot x=0$ when $x=0$; $\dot y=0$ when $y=0$). By common sense (p. 158): some trajectories from near the origin go to each stable node, and between them one trajectory "can't decide" and dives into the saddle. It is part of the **stable manifold** of the saddle. The other branch comes in from infinity. A computer plot confirms this (Fig. 6.4.7).

**Interpretation (p. 159).** One species generally drives the other to extinction. Starting below the stable manifold leads to extinction of the sheep; above it, extinction of the rabbits. This dichotomy occurs in other competition models and led to the **principle of competitive exclusion**: two species competing for the same limited resource typically cannot coexist.

**Basin of attraction** of an attracting fixed point $\mathbf x^*$: the set of $\mathbf x_0$ with $\mathbf x(t)\to\mathbf x^*$ as $t\to\infty$. The basin of $(3,0)$ is all points below the saddle's stable manifold (Fig. 6.4.8). The stable manifold separates the two basins, so it is the **basin boundary**; its two trajectories are the **separatrices** (pp. 159–160). Basins and boundaries partition phase space into regions of different long-term behavior (p. 160).

*Intuition note:* Small differences in the starting populations near the boundary decide which species survives. The saddle's stable manifold is the knife-edge between two futures.

### 6.5 Conservative Systems (pp. 160–164)
Take $m\ddot x=F(x)$, with $F$ independent of $\dot x$ and $t$ (no damping or driving). Let $V$ be the potential energy, $F=-dV/dx$, so
$$m\ddot x+\frac{dV}{dx}=0\tag{1}$$
Multiplying by $\dot x$ makes the left side an exact derivative (chain rule $\frac{d}{dt}V(x(t))=\frac{dV}{dx}\dot x$ in reverse):
$$m\dot x\ddot x+\frac{dV}{dx}\dot x=0\ \Rightarrow\ \frac{d}{dt}\Big[\tfrac12m\dot x^2+V(x)\Big]=0$$
So $E=\tfrac12m\dot x^2+V(x)$ is constant along each solution: a conserved quantity, constant of motion, or first integral (p. 160).

**General definition.** For $\dot{\mathbf x}=\mathbf f(\mathbf x)$, a *conserved quantity* is a real-valued continuous function $E(\mathbf x)$ with $dE/dt=0$ along trajectories and nonconstant on every open set. Otherwise $E\equiv0$ would make every system conservative. Systems with such a quantity are *conservative* (p. 160).

**Example 6.5.1: a conservative system cannot have an attracting fixed point.** If $\mathbf x^*$ attracted, all points in its basin would have energy $E(\mathbf x^*)$. Then $E$ would be constant on an open set, contradicting the definition (p. 161).

**Example 6.5.2: double well** $V=-\tfrac12x^2+\tfrac14x^4$, $m=1$ (pp. 161–162).
- Force $-dV/dx=x-x^3$, so $\dot x=y$, $\dot y=x-x^3$.
- Equilibria: $(0,0)$ and $(\pm1,0)$. Jacobian $A=\begin{pmatrix}0&1\\1-3x^2&0\end{pmatrix}$.
- At $(0,0)$, $\Delta=-1$: saddle. At $(\pm1,0)$, $\tau=0$, $\Delta=2$: predicted centers.
- Small nonlinear terms could destroy centers, but not here because of energy conservation. Trajectories lie on contours of $E=\tfrac12y^2-\tfrac12x^2+\tfrac14x^4$ (Fig. 6.5.1). Arrow directions come from evaluating $(\dot x,\dot y)$ at a few points; for example, on the positive y-axis $\dot x>0$, $\dot y=0$.
- Each center is surrounded by small closed orbits. Large closed orbits encircle all three fixed points. Solutions are typically periodic, except for equilibria and two special trajectories that approach the origin as $t\to\pm\infty$. These start and end at the same fixed point and are **homoclinic orbits**. They are common in conservative systems but rare otherwise. They are not periodic, since reaching the fixed point takes forever (p. 162).
- Physically: centers are the particle at rest at the bottom of a well; small orbits are small oscillations; large orbits are energetic oscillations over the hump (p. 162). The author leaves the meaning of the saddle and homoclinic orbits as a question to the reader.

**Example 6.5.3: the energy surface** ($E$ plotted above the $(x,y)$ plane, Fig. 6.5.3). Local minima of $E$ project to centers. Slightly higher contours give small orbits. The saddle and homoclinic orbits lie higher, and the large orbits highest. Trajectories stay at constant height, so they run around the surface, not down it (p. 163).

**Theorem 6.5.1 (nonlinear centers for conservative systems).** Let $\dot{\mathbf x}=\mathbf f(\mathbf x)$, $\mathbf x\in\mathbb R^2$, $\mathbf f$ continuously differentiable. Suppose there is a conserved quantity $E(\mathbf x)$ and $\mathbf x^*$ is an isolated fixed point. If $\mathbf x^*$ is a local minimum of $E$, then all trajectories sufficiently close to $\mathbf x^*$ are closed (p. 163).

*Ideas behind the proof (p. 163–164):* Each trajectory lies in a contour of $E$. Near a local extremum the contours are closed (not proved). A trajectory could only fail to go all the way round if it stopped at a fixed point on the contour. Isolation rules this out nearby. Remarks (p. 164): the theorem also holds for local maxima (replace $E$ by $-E$). Isolation is needed: without it there are counterexamples (Exercise 6.5.12).

*Intuition note:* In a conservative system, motion is stuck on a level curve of energy. Near an energy minimum these level curves are small loops, so an isolated equilibrium there is a center that survives the nonlinear terms.

### 6.6 Reversible Systems (pp. 164–168)
Mechanical systems $m\ddot x=F(x)$ are symmetric under $t\to-t$ ($\ddot x$ unchanged, $\dot x$ reversed). In the phase plane, $\dot x=y$, $\dot y=\tfrac1mF(x)$ is unchanged under $t\to-t$, $y\to-y$. So if $(x(t),y(t))$ is a solution, so is $(x(-t),-y(-t))$. Every trajectory has a twin: its reflection in the x-axis with the arrows reversed (p. 164).

**Definition.** A *reversible system* is any second-order system invariant under $t\to-t$, $y\to-y$. For example, $\dot x=f(x,y)$, $\dot y=g(x,y)$ with $f$ odd in $y$ and $g$ even in $y$ is reversible (p. 165). Reversible systems differ from conservative ones but share many properties.

**Theorem 6.6.1 (nonlinear centers for reversible systems).** Suppose the origin is a linear center of the continuously differentiable system $\dot x=f(x,y)$, $\dot y=g(x,y)$, and the system is reversible. Then sufficiently close to the origin all trajectories are closed curves (p. 165).

*Ideas behind the proof:* Start on the positive x-axis near the origin. Near a linear center the flow swirls around, so the trajectory reaches the negative x-axis (the step the author admits lacks rigor). Reflect it across the x-axis and reverse $t$. The twin has the same endpoints with reversed arrow, and the two together form a closed orbit (p. 165).

**Example 6.6.1:** $\dot x=y-y^3$, $\dot y=-x-y^2$ (p. 166).
- At the origin $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $\tau=0$, $\Delta>0$: linear center. The system is reversible ($t\to-t$, $y\to-y$). By Theorem 6.6.1 it is a nonlinear center.
- Other fixed points: $(-1,1)$ and $(-1,-1)$, saddles. They are joined by a pair of **heteroclinic trajectories** (saddle connections), which are, like homoclinic orbits, much more common in reversible or conservative systems than elsewhere. Their existence can be shown with reversibility arguments (Exercise 6.6.6).

**Example 6.6.2:** $\dot x=y$, $\dot y=x-x^2$ has a homoclinic orbit in $x\ge0$, by reversibility alone (p. 167).
- The unstable manifold of the saddle at the origin leaves along $(1,1)$, so part of it lies in $x,y>0$.
- On it, $\dot x=y>0$ and $\dot y=x-x^2>0$ for small $x$. The point moves up and right with increasing horizontal velocity, so it crosses $x=1$. There $\dot y<0$, so $y$ decreases and reaches $y=0$.
- The twin trajectory has the same endpoints with the arrow reversed. Together they form the homoclinic orbit.

**General reversibility (p. 167).** Take a map $R(\mathbf x)$ of phase space with $R^2(\mathbf x)=\mathbf x$ (for example, a reflection about an axis through the origin). Then $\dot{\mathbf x}=\mathbf f(\mathbf x)$ is reversible if it is invariant under $t\to-t$, $\mathbf x\to R(\mathbf x)$.

**Example 6.6.3:** $\dot x=-2\cos x-\cos y$, $\dot y=-2\cos y-\cos x$ is reversible but not conservative (pp. 167–168).
- It is invariant under $t\to-t$, $x\to-x$, $y\to-y$, so $R(x,y)=(-x,-y)$.
- Fixed points: $2\cos x=-\cos y$ and $2\cos y=-\cos x$ give $\cos x^*=\cos y^*=0$, so $(\pm\pi/2,\pm\pi/2)$.
- At $(-\pi/2,-\pi/2)$: $A=\begin{pmatrix}2\sin x^*&\sin y^*\\\sin x^*&2\sin y^*\end{pmatrix}=\begin{pmatrix}-2&-1\\-1&-2\end{pmatrix}$, $\tau=-4$, $\Delta=3$, $\tau^2-4\Delta=4$: stable node. An attracting fixed point rules out a conservative system (Example 6.5.1).
- The other three are an unstable node and two saddles (stated without derivation). The stable node at $(-\pi/2,-\pi/2)$ is the twin of the unstable node at $(\pi/2,\pi/2)$ (Fig. 6.6.7).
- Related to a model of two Josephson junctions coupled through a resistive load (Tsang et al. 1991); see Exercise 6.6.9 and Example 8.7.4.

*Intuition note:* Reversibility gives a mirror-with-reversed-arrows symmetry. In the proof of Theorem 6.6.1, a closed orbit is formed from a trajectory and its twin. Unlike conservation, reversibility allows attractors; in Example 6.6.3 the stable node is the twin of an unstable node.

### 6.7 Pendulum (pp. 168–173)
Undamped pendulum, $\theta$ measured from the downward vertical (p. 169):
$$\frac{d^2\theta}{dt^2}+\frac gL\sin\theta=0\tag{1}$$
Nondimensionalize with $\omega=\sqrt{g/L}$, $\tau=\omega t$:
$$\ddot\theta+\sin\theta=0\tag{2}$$
(overdot is $d/d\tau$), or
$$\dot\theta=v\tag{3a}$$
$$\dot v=-\sin\theta\tag{3b}$$
with $v$ the dimensionless angular velocity. Fixed points: $(k\pi,0)$, $k$ any integer; angles differing by $2\pi$ are physically the same, so study $(0,0)$ and $(\pi,0)$.

**At $(0,0)$:** $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, a linear center. It is a nonlinear center for two reasons (pp. 169–170):
1. The system is reversible ($\tau\to-\tau$, $v\to-v$), so Theorem 6.6.1 applies.
2. It is conservative. Multiplying (2) by $\dot\theta$ gives $\dot\theta(\ddot\theta+\sin\theta)=0\Rightarrow\tfrac12\dot\theta^2-\cos\theta=\text{const}$, so
$$E(\theta,v)=\tfrac12v^2-\cos\theta\tag{4}$$
$E\approx\tfrac12(v^2+\theta^2)-1$ for small $(\theta,v)$, a local minimum at the origin. Theorem 6.5.1 gives a second proof; orbits are approximately circular, $\theta^2+v^2\approx2(E+1)$.

**At $(\pi,0)$:** $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\lambda^2-1=0$, $\lambda_{1,2}=-1,+1$: saddle, with eigenvectors $\mathbf v_1=(1,-1)$, $\mathbf v_2=(1,1)$ (p. 170). Adding the energy contours gives Fig. 6.7.3, periodic in $\theta$.

**Physical meaning (pp. 170–171).**
- The center is neutrally stable equilibrium (hanging at rest), the lowest energy state $E=-1$.
- Small orbits are oscillations about equilibrium, called *librations*.
- $E=1$ gives the heteroclinic trajectories joining saddles. The saddles are an inverted pendulum at rest, so these are delicate motions in which the pendulum slows to a halt exactly as it reaches the inverted position.
- For $E>1$ the pendulum whirls over the top repeatedly (*rotations*). These count as periodic solutions, since $\theta=\pm\pi$ are the same position.

**Cylindrical phase space (pp. 171–172).** A cylinder is the natural phase space because $v$ is a real number but $\theta$ is an angle. Advantages: whirling motions appear as closed orbits around the cylinder for $E>1$. All saddles are visibly one physical state. The heteroclinic trajectories become homoclinic orbits. Plotting $E$ vertically bends the cylinder into a U-tube (Fig. 6.7.5). The two arms are clockwise and counterclockwise whirling, and the homoclinic orbits at $E=1$ separate librations from rotations. The apparent arrow reversal on one arm is explained by the coordinate system: the direction of increasing $\theta$ reverses when the cylinder is bent (Fig. 6.7.6).

**Damping (p. 173).** Add a small amount of linear damping, $b>0$: $\ddot\theta+b\dot\theta+\sin\theta=0$. Then centers become stable spirals and saddles remain saddles (Fig. 6.7.7). On the U-tube every trajectory loses altitude except the fixed points. Along trajectories:
$$\frac{dE}{d\tau}=\frac{d}{d\tau}\Big(\tfrac12\dot\theta^2-\cos\theta\Big)=\dot\theta(\ddot\theta+\sin\theta)=-b\dot\theta^2\le0.$$
This is where this part of the chapter ends (p. 173).

*Intuition note:* Energy level separates the pendulum's behaviors: rocking below $E=1$, whirling above it, and a knife-edge at the saddle. With friction, energy only decreases, so the center no longer survives.

## Toy example (ours, not from the text)
System: $\dot x=2x+y^2$, $\dot y=-3y$.
- Fixed point: $\dot y=0\Rightarrow y=0$, then $\dot x=0\Rightarrow x=0$. Only $(0,0)$.
- Jacobian: $\begin{pmatrix}2&2y\\0&-3\end{pmatrix}$. At the origin, $A=\mathrm{diag}(2,-3)$: eigenvalues $2$ and $-3$, real parts nonzero, so it is hyperbolic. The linearization predicts a saddle; the nonlinear term $y^2$ cannot change this.
- Exact solution: $y=y_0e^{-3t}$, so $\dot x-2x=y_0^2e^{-6t}$. Try $x_p=Ae^{-6t}$: $-6A=2A+y_0^2$, so $A=-y_0^2/8$. Hence $x(t)=(x_0+y_0^2/8)e^{2t}-(y_0^2/8)e^{-6t}$.
- If $x_0=-y_0^2/8$, the growing term vanishes and $x=-(y_0^2/8)e^{-6t}=-y^2/8$ (since $y^2=y_0^2e^{-6t}$). The stable manifold is the curve $x=-y^2/8$. It is curved, but tangent at the origin to the linear stable direction $(0,1)$.
- Example numbers: $(x_0,y_0)=(0,2)$ gives $x(t)=0.5(e^{2t}-e^{-6t})$, which grows without bound. The point $(-0.5,2)$ has $-y^2/8=-0.5$, so it lies on the manifold and decays to the origin.
- Contrast with a marginal case: $\dot r=-r^3$ gives $r^{-2}=r_0^{-2}+2t$. With $r_0=1$ and $t=4.5$, $r=1/\sqrt{10}\approx0.316$: slow decay, the kind of effect the linearization (a center) cannot see.

## Concepts
- [[phase-space]] — here the phase plane: points $(x_1,x_2)$ with $\dot{\mathbf x}$ as the velocity vector; trajectories fill it (p. 146)
- [[fixed-point-and-stability]] — $\mathbf f(\mathbf x^*)=\mathbf 0$; steady state whose stability depends on nearby flow (p. 147)
- [[linear-stability-analysis]] — classify a fixed point from the Jacobian eigenvalues; valid if not marginal (p. 152)
- [[jacobian-matrix]] (new) — matrix of partial derivatives of $(f,g)$ at the fixed point; multivariable analog of $f'(x^*)$ (p. 152)
- [[nullcline]] (new) — curve where $\dot x=0$ or $\dot y=0$; flow there is vertical or horizontal (p. 148)
- [[hyperbolic-fixed-point]] (new) — all eigenvalues have Re λ ≠ 0; robust to small nonlinear terms; not the same as "saddle" (p. 156)
- [[topological-equivalence]] (new) — a homeomorphism maps one portrait onto another, trajectories to trajectories, time direction preserved (p. 156)
- [[structural-stability]] (new) — topology of a portrait unchanged by arbitrarily small perturbations of the vector field (p. 156)
- [[attractor-basin-of-attraction]] — here basin of an attracting fixed point: the set of initial conditions flowing to it (p. 159)
- [[stable-manifold-separatrix]] (new) — trajectories flowing into a saddle; they form the basin boundary between two basins (pp. 158–160)
- [[competitive-exclusion]] (new) — competing for one limited resource, two species typically cannot coexist (p. 159)
- [[conservative-system]] (new) — has a continuous conserved quantity $E$, nonconstant on every open set; no attracting fixed points (pp. 160–161)
- [[homoclinic-heteroclinic-orbit]] (new) — a trajectory that starts and ends at the same fixed point (homoclinic) or at two different ones (heteroclinic) (pp. 162, 166)
- [[reversible-system]] (new) — invariant under $t\to-t$, $y\to-y$ (or $\mathbf x\to R(\mathbf x)$ with $R^2=\mathrm{id}$); trajectories have time-reversed twins (pp. 165, 167)

## Canonical instances
- [[rabbits-vs-sheep]] (new) — two stable nodes, a saddle, a basin boundary, competitive exclusion (pp. 157–160)
- [[double-well-potential]] (new) — saddle and two centers in a conservative system; homoclinic orbits (pp. 161–163)
- [[pendulum]] (new) — undamped: librations, rotations, cylindrical phase space; damped: spirals and falling energy (pp. 169–173)
- [[weakly-nonlinear-spiral]] (new) — Example 6.3.2: $\dot r=ar^3$, $\dot\theta=1$; a center destroyed by small nonlinearity (pp. 154–155)

## Bridges (candidates)
- [structural-analogy] Basin boundary (stable manifold of a saddle) ↔ complex-systems: tipping point/threshold — a thin set separates starting states with very different long-term outcomes.
- [structural-analogy] Hyperbolic (robust) vs. marginal (fragile) fixed points ↔ complex-systems: robustness and fragility — some structures survive small perturbations and others do not.
- [structural-analogy] Competitive exclusion via two stable nodes and a saddle ↔ complex-systems: path dependence — initial conditions determine which stable outcome is reached.

## Questions this raises
- What does the Poincaré–Bendixson theorem need, and can closed orbits appear without conservation or reversibility (Section 7.3 is promised, p. 150)?
- How do the rabbits–sheep portraits change if the competition coefficients change (the author sets this as exercises, p. 157)?
- What do the global index-theory results (announced in 6.0) say about which fixed-point arrangements are possible?
- Why does a damped pendulum, with its energy-decreasing spirals, have a basin structure for each stable spiral?

## Reading notes
- This is part 1 of Chapter 6. It starts at 6.0 (p. 146) and ends on p. 173 at the damping energy computation $dE/d\tau=-b\dot\theta^2\le0$, inside Section 6.7. The pages given do not show whether 6.7 continues. Index theory (announced on p. 146) is in the unseen part.
- Page offset: printed = pdf − 15.
- No exercise lists appear in these pages (only references to exercises), so there is no "Exercises worth doing" section.
- The text layer lost many minus signs, ± signs and Greek letters (e.g., ω, λ, τ, Δ). Equations were checked against the page images. All formulas used here match the images, including the Jacobian on p. 157 and $(-1,\pm1)$ on p. 166.
- The author uses the same symbol τ for the trace (Section 6.3, 6.6) and for dimensionless time (Section 6.7); context separates them.
