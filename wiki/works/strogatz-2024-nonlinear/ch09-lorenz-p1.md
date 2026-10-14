---
id: strogatz-2024-nonlinear/ch09-lorenz-p1
work: strogatz-2024-nonlinear
unit: "9 Lorenz Equations (part 1/2): §§9.0–9.3"
pages: 309–332
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Lorenz Equations, part 1: waterwheel, simple properties, chaos on a strange attractor

## L0 — One line
A simple three-variable deterministic system, which a chaotic waterwheel reproduces exactly, has, over a range of parameters, apparently no stable fixed point or stable cycle, yet stays bounded, and so ends on a strange attractor with exponential divergence of nearby trajectories.

## L1 — The gist (≤ 120 words)
Strogatz asks where the chaos in the Lorenz equations comes from. He first derives an equivalent system from a leaky waterwheel. Then he follows Lorenz's elimination of the usual long-term behaviours. Volume in phase space shrinks, so repellers (sets that push all nearby trajectories away) are impossible. The origin is globally stable for r < 1. The fixed points C± lose stability in a subcritical Hopf bifurcation. Trajectories stay bounded and end on a zero-volume set, which turns out to be a fractal: the strange attractor. Numerically, nearby trajectories separate like e^{λt}. This limits the prediction time to about (1/λ) ln(tolerance/error). The unit ends with working definitions of chaos and attractor.

**Prerequisites:** ODEs in 2D/3D; fixed points and linearization (trace, determinant); Fourier series and orthogonality; divergence theorem; Hopf bifurcation; logarithms.

## L2 — Key ideas
- The waterwheel is a physical model of the Lorenz equations. Its mass-conservation and torque equations reduce, via Fourier modes, to a closed 3D system (p. 317).
- Steady rotation (a fixed point with ω ≠ 0) exists if and only if the Rayleigh number πgrq₁/(K²ν), a dimensionless ratio of driving to dissipation, exceeds 1 (pp. 318–319).
- Lorenz system: ∇·f = −σ−1−b, so phase-space volumes shrink as e^{−(σ+1+b)t}. This rules out quasiperiodic solutions and repellers (pp. 321–322).
- For r < 1 the origin is globally stable (every trajectory approaches it), shown with a Liapunov function (a positive function that decreases along trajectories). So there is no chaos for r < 1 (pp. 323–324).
- For r > r_H, C± are not stable. The Hopf bifurcation at r_H is subcritical. Trajectories are bounded and no attractor is nearby, so they must fly to a distant, unusual attractor (pp. 324–325).
- The strange attractor has zero volume and is called a fractal (numerical experiments suggest dimension about 2.05). Motion on it is aperiodic and switches between left and right lobes (pp. 326–328).
- Sensitive dependence (found numerically; λ is the separation growth rate): ‖δ(t)‖ ~ ‖δ₀‖e^{λt}, λ ≈ 0.9. Prediction time grows only logarithmically as the initial error shrinks (pp. 328–330).
- Working definitions: chaos, attractor (invariant, attracts an open set, minimal) (pp. 331–332).

## L3 — Walkthrough

### 9.0 Introduction (p. 309)
The Lorenz equations are
$$\dot x=\sigma(y-x),\qquad \dot y=rx-y-xz,\qquad \dot z=xy-bz,$$
with parameters $\sigma,r,b>0$. Lorenz derived them from a drastically simplified model of convection rolls. They also arise in models of lasers and dynamos, and they describe a certain waterwheel exactly (p. 309). Over a wide parameter range solutions oscillate irregularly, never repeat, and stay in a bounded region. They settle onto a *strange attractor*. This is a fractal with a fractional dimension between 2 and 3 (p. 309).

### 9.1 A Chaotic Waterwheel (pp. 310–319)
**Set-up.** Leaky paper cups hang from a wheel rim and water is poured in at the top (Fig. 9.1.1). At a slow inflow the wheel stays still, because friction wins. At faster inflow it rotates steadily in one direction or the other, chosen by initial conditions. At still faster inflow the rotation becomes chaotic, with irregular reversals (p. 310). Malkus's lab version has a wheel tilted slightly from horizontal, so the tilt changes the effective gravity. A brake adds friction. Water is sprayed into transparent chambers with small holes, collected, and pumped back (pp. 311–312). A sensor records the angular velocity ω(t) (Fig. 9.1.3, p. 312). The goal is to understand the bifurcations from rest to steady rotation to irregular reversals (p. 312).

**Notation (p. 313).**
- θ: angle in the lab frame, with θ = 0 at 12:00.
- ω(t): angular velocity, increasing counterclockwise.
- m(θ,t): mass per unit angle, so the mass in [θ₁,θ₂] is $M=\int_{\theta_1}^{\theta_2} m\,d\theta$.
- Q(θ): inflow.
- r: wheel radius. K: leakage rate. ν: rotational damping rate. I: moment of inertia.

The unknowns are m(θ,t) and ω(t).

**Conservation of mass (pp. 313–314).** For a sector [θ₁,θ₂] fixed in space, ΔM has four contributions (p. 313–314):
1. Inflow: $\Delta t\int Q\,d\theta$.
2. Leakage: $-\Delta t\int Km\,d\theta$. Leakage proportional to m is justified because it agrees well with measurements on the wheel. Thin tubes on the holes give essentially Poiseuille flow (p. 314).
3. Water carried in: $m(\theta_1)\,\omega\Delta t$.
4. Water carried out: $-m(\theta_2)\,\omega\Delta t$.

Hence
$$\Delta M=\Delta t\Big[\int_{\theta_1}^{\theta_2}Q\,d\theta-\int_{\theta_1}^{\theta_2}Km\,d\theta\Big]+m(\theta_1)\omega\Delta t-m(\theta_2)\omega\Delta t.\tag{1}$$
Use $m(\theta_1)-m(\theta_2)=-\int_{\theta_1}^{\theta_2}\frac{\partial m}{\partial\theta}d\theta$, divide by Δt and let Δt → 0:
$$\frac{dM}{dt}=\int_{\theta_1}^{\theta_2}\Big(Q-Km-\omega\frac{\partial m}{\partial\theta}\Big)d\theta .$$
By definition $dM/dt=\int \partial m/\partial t\,d\theta$. Since this holds for all θ₁, θ₂:
$$\frac{\partial m}{\partial t}=Q-Km-\omega\frac{\partial m}{\partial\theta}.\tag{2}$$
This is the continuity equation, a partial differential equation (p. 314).

**Torque balance (pp. 315–316).** I depends on t because the water distribution does. But as $t\to\infty$, I(t) tends to a constant (Exercise 9.1.1, not printed here). After transients, $I\dot\omega$ = damping torque + gravitational torque (p. 315).
- Damping comes from viscous oil in the brake and from "inertial" spin-up of incoming water. Both are proportional to ω, so the damping torque is $-\nu\omega$ with ν > 0 (p. 315).
- Gravity acts like an inverted pendulum. A mass element dM = m dθ gives $d\tau=(dM)\,gr\sin\theta=mgr\sin\theta\,d\theta$. For sin θ > 0 it increases ω, which checks the sign. Here $g=g_0\sin\alpha$, where α is the tilt (p. 315).

Integrating over the rim gives
$$I\dot\omega=-\nu\omega+gr\int_0^{2\pi}m(\theta,t)\sin\theta\,d\theta.\tag{3}$$
This is an integro-differential equation (p. 316).

**Amplitude equations (pp. 316–317).** Equations (2) and (3) completely specify the evolution (p. 316). Expand in Fourier series:
$$m(\theta,t)=\sum_{n=0}^\infty[a_n(t)\sin n\theta+b_n(t)\cos n\theta],\tag{4}$$
$$Q(\theta)=\sum_{n=0}^\infty q_n\cos n\theta.\tag{5}$$
Q has no sine terms because water is added symmetrically at the top (p. 316). Substitute into (2). Orthogonality lets us equate coefficients of each harmonic. For sin nθ the left side gives $\dot a_n$ and the right gives $n\omega b_n-Ka_n$. Matching cos nθ gives the other equation (p. 317):
$$\dot a_n=n\omega b_n-Ka_n,\tag{6}$$
$$\dot b_n=-n\omega a_n-Kb_n+q_n.\tag{7}$$
Both hold for all n = 0, 1, …. Substituting (4) into (3), orthogonality leaves one term:
$$I\dot\omega=-\nu\omega+gr\int_0^{2\pi}a_1\sin^2\theta\,d\theta=-\nu\omega+\pi gr\,a_1.\tag{8}$$
So only $a_1$ enters the ω equation. By (6)–(7), $(a_1,b_1,\omega)$ is closed and decoupled from all $a_n,b_n$ with n ≠ 1:
$$\dot a_1=\omega b_1-Ka_1,\quad \dot b_1=-\omega a_1-Kb_1+q_1,\quad \dot\omega=(-\nu\omega+\pi gr\,a_1)/I.\tag{9}$$
This is a 3D state $(a_1,b_1,\omega)$ with two quadratic terms, $\omega b_1$ and $\omega a_1$. It is equivalent to the Lorenz equations (Exercise 9.1.3, not printed here). Its behaviour is "fantastically complex" and has never been fully understood (p. 317).

*Skip path:* carry forward system (9) and the results (16)–(17) below.

*Intuition note:* The huge original problem (a PDE plus an integral equation) collapses to three ODEs, because only the coefficient $a_1$ enters the ω equation, and (6)–(7) do not couple mode 1 to the other modes. The rest of the water pattern plays no role in the ω equation.

**Fixed points (pp. 317–318).** Set all derivatives of (9) to zero:
$$a_1=\omega b_1/K\tag{10}$$
$$\omega a_1=q_1-Kb_1\tag{11}$$
$$a_1=\nu\omega/\pi gr\tag{12}$$
Eliminating $a_1$ from (10) and (11) (added step: $\omega^2b_1/K=q_1-Kb_1$) gives
$$b_1=\frac{Kq_1}{\omega^2+K^2}.\tag{13}$$
(The printed page shows this equation without a tag.) Equating (10) and (12): $\omega b_1/K=\nu\omega/\pi gr$, so ω = 0 or
$$b_1=K\nu/\pi gr.\tag{14}$$
1. If ω = 0, then $a_1=0$ and $b_1=q_1/K$. The fixed point is
$$(a_1^*,b_1^*,\omega^*)=(0,\,q_1/K,\,0).\tag{15}$$
 The wheel is at rest, with inflow balanced by leakage. Stability is not claimed here (p. 318).
2. If ω ≠ 0, (13) and (14) give $Kq_1/(\omega^2+K^2)=K\nu/\pi gr$. Since K ≠ 0, $q_1/(\omega^2+K^2)=\nu/\pi gr$, so
$$(\omega^*)^2=\frac{\pi gr\,q_1}{\nu}-K^2.\tag{16}$$
 If the right side is positive there are two solutions ±ω*, steady rotation in either direction. They exist if and only if
$$\frac{\pi gr\,q_1}{K^2\nu}>1.\tag{17}$$

The group in (17) is the **Rayleigh number**. It measures how hard the system is driven relative to dissipation. Gravity and inflow (g, q₁) spin the wheel. Leakage and damping (K, ν) stop it. So steady rotation is possible only if it is large enough (p. 318).

*Intuition note:* The wheel starts turning only when driving beats dissipation by a margin. This is the same threshold structure as the onset of convection rolls.

**Analogy with convection (pp. 318–319).** In a fluid layer heated from below, the Rayleigh number is proportional to the temperature difference. For small values heat is conducted and the fluid stays still. Past a critical value, rolls form, analogous to steady rotation. With further increase the rolls become wavy and then chaotic. The analogy breaks down at still higher values, when turbulence appears. The waterwheel instead settles into a pendulum-like pattern of reversals (see Example 9.5.2, not in this part) (p. 319).

### 9.2 Simple Properties of the Lorenz Equations (pp. 319–325)
**Context.** Lorenz eliminated the known possibilities for long-term behaviour. In some parameter range he showed there were no stable fixed points and no stable limit cycles. He also showed all trajectories are bounded and attracted to a set of zero volume. This seemed paradoxical (p. 319). In (1), σ is the Prandtl number and r is the Rayleigh number. The parameter b has no name; in convection it is related to the aspect ratio of the rolls (p. 319).

**Nonlinearity.** The only nonlinearities are the quadratic terms xy and xz (p. 319).

**Symmetry.** Replacing (x,y) → (−x,−y) leaves the equations unchanged. So if (x,y,z)(t) is a solution, so is (−x,−y,z)(t). Every solution is either symmetric itself or has a symmetric partner (p. 320).

**Volume contraction (pp. 320–321).** For any 3D system $\dot{\mathbf x}=\mathbf f(\mathbf x)$, take a closed surface S(t) enclosing volume V(t), with outward normal n. In time dt a surface patch dA sweeps out volume $(\mathbf f\cdot\mathbf n\,dt)\,dA$ (p. 320). So
$$V(t+dt)=V(t)+\int_S(\mathbf f\cdot\mathbf n\,dt)\,dA,\qquad \dot V=\int_S\mathbf f\cdot\mathbf n\,dA=\int_V\nabla\!\cdot\mathbf f\,dV.\tag{2}$$
The last step is the divergence theorem. For Lorenz:
$$\nabla\!\cdot\mathbf f=\frac{\partial}{\partial x}[\sigma(y-x)]+\frac{\partial}{\partial y}[rx-y-xz]+\frac{\partial}{\partial z}[xy-bz]=-\sigma-1-b<0.$$
The divergence is constant, so $\dot V=-(\sigma+1+b)V$ and $V(t)=V(0)e^{-(\sigma+1+b)t}$. Volumes shrink exponentially fast. A solid blob of initial conditions shrinks to a limiting set of zero volume. Later it is said to consist of fixed points, limit cycles, or for some parameters a strange attractor (p. 321).

*Intuition note:* The flow squeezes every blob of states toward a set with no volume, like air leaving a balloon. Each trajectory can still wander on that set.

**Example 9.2.1 (p. 321).** There are no quasiperiodic solutions. Such a solution would lie on an invariant torus, whose enclosed volume would then be constant. This contradicts exponential shrinking.

**Example 9.2.2 (p. 322).** There are no repelling fixed points or closed orbits. A small closed surface around a repeller would expand, so its volume would grow. This is a contradiction.

By elimination, all fixed points must be sinks or saddles. Closed orbits, if any, must be stable or saddle-like (p. 322).

**Fixed points (p. 322).** The origin is a fixed point for all parameters. For r > 1 there is a symmetric pair $C^\pm$:
$$x^*=y^*=\pm\sqrt{b(r-1)},\qquad z^*=r-1.$$
These represent left- or right-turning convection rolls. As r → 1⁺, $C^\pm$ merge with the origin in a pitchfork bifurcation (p. 322).

**Linear stability of the origin (p. 322).** Dropping xy and xz gives $\dot z=-bz$, so z decays exponentially. In the (x,y) plane the matrix is $\begin{pmatrix}-\sigma&\sigma\\ r&-1\end{pmatrix}$ (shape 2×2), with trace $\tau=-\sigma-1<0$ and determinant $\Delta=\sigma(1-r)$.
- If r > 1, Δ < 0 and the origin is a saddle. In 3D it has one outgoing and two incoming directions.
- If r < 1, all directions are incoming and the origin is a sink. Since $\tau^2-4\Delta=(\sigma+1)^2-4\sigma(1-r)=(\sigma-1)^2+4\sigma r>0$, it is a stable node.

**Global stability of the origin for r < 1 (pp. 323–324).** Every trajectory approaches the origin, so there are no limit cycles or chaos for r < 1. The proof uses a Liapunov function: a smooth, positive definite function that decreases along trajectories. There is no systematic recipe, but sums of squares are worth trying (p. 323). Take $V=\frac1\sigma x^2+y^2+z^2$, whose level sets are concentric ellipsoids. Then
$$\tfrac12\dot V=\tfrac1\sigma x\dot x+y\dot y+z\dot z=(yx-x^2)+(ryx-y^2-xyz)+(zxy-bz^2)=(r+1)xy-x^2-y^2-bz^2 .$$
Completing the square:
$$\tfrac12\dot V=-\Big[x-\tfrac{r+1}{2}y\Big]^2-\Big[1-\big(\tfrac{r+1}{2}\big)^2\Big]y^2-bz^2 .$$
This is a negative sum of squares. It is zero only if y = 0 and z = 0 (the y² coefficient is nonzero because r < 1) and then x = 0. So $\dot V<0$ unless (x,y,z) = (0,0,0). V is bounded below by 0, so V → 0 and x(t) → 0 (pp. 323–324).

**Stability of C± (p. 324).** The calculation is Exercise 9.2.1 (not printed here). $C^\pm$ are linearly stable for
$$1<r<r_H=\frac{\sigma(\sigma+b+3)}{\sigma-b-1},$$
assuming also σ − b − 1 > 0. They lose stability in a Hopf bifurcation at r = r_H. The bifurcation is *subcritical*: the limit cycles are unstable and exist only for r < r_H. This needs a difficult calculation, which the text cites rather than gives (p. 324). For r < r_H, near $C^+$ there is a stable fixed point encircled by a **saddle cycle**. This is an unstable limit cycle, possible only in 3D or more. It has a 2D unstable manifold and a 2D stable manifold (Fig. 9.2.4). As r → r_H⁻ the cycle shrinks onto the fixed point. At the bifurcation the fixed point absorbs the cycle and becomes a saddle point. For r > r_H there are no attractors nearby (pp. 324–325).

**The puzzle (p. 325).** For r > r_H trajectories must fly to a distant attractor, yet the partial bifurcation diagram (Fig. 9.2.5) shows no stable object. They cannot escape to infinity: all trajectories eventually enter and stay in a large ellipsoid (Exercise 9.2.2, not printed here). Stable limit cycles are not strictly excluded. But Lorenz gave a persuasive argument that for r slightly above r_H any limit cycles would be unstable (Section 9.4, not in this part). So trajectories are repelled from one unstable object after another, like pinball balls. They are confined to a bounded set of zero volume and move on it forever without intersecting themselves or others (p. 325).

### 9.3 Chaos on a Strange Attractor (pp. 325–332)
**Lorenz's numerics (pp. 325–326).** Lorenz used σ = 10, b = 8/3, r = 28, which is just above $r_H\approx24.74$. He started at (0,1,0), near the saddle at the origin. The electromechanical computers of the time were unreliable, so he interpreted results with caution (p. 325). After a transient, y(t) oscillates irregularly and never repeats exactly: the motion is *aperiodic* (Fig. 9.3.1, p. 326).

**The attractor (pp. 326–328).** Plotting x against z gives a butterfly pattern (Fig. 9.3.2). Apparent self-crossings are only projection artifacts. In 3D there are none (p. 327). The trajectory spirals several times around one lobe, then jumps to the other. The number of circuits varies unpredictably, and this sequence has many characteristics of a random sequence. Left/right switches correspond to the waterwheel's irregular reversals (p. 327). The limiting set is the zero-volume attracting set deduced in 9.2. Ruelle and Takens coined "strange attractor" (p. 327). Fig. 9.3.3 suggests two surfaces merging, but the uniqueness theorem forbids merging.
- **Lorenz's explanation:** the surfaces only appear to merge, because of strong contraction and limited numerical resolution. Following them around C⁺ and C⁻ shows that each surface is really a pair, then four, then eight surfaces, and so on, finally "an infinite complex of surfaces" (pp. 327–328).
- **Author's gloss:** today this is called a fractal. It has zero volume but infinite surface area. Numerical experiments suggest a dimension of about 2.05 (Example 11.5.1, not in this part) (p. 328).

**Exponential divergence (pp. 328–330).** The motion shows *sensitive dependence on initial conditions*: trajectories that start close together diverge rapidly and then have totally different futures. In Color Plate 2, a blob of 10,000 nearby initial conditions spreads over the whole attractor. Long-term prediction then becomes impossible (p. 328). Take x(t) on the attractor and a nearby point x(t) + δ(t) with $\|\delta_0\|=10^{-15}$, say. Numerically
$$\|\delta(t)\|\sim\|\delta_0\|e^{\lambda t},\qquad \lambda\approx0.9 .$$
So ln‖δ‖ versus t is close to a line of slope λ (Fig. 9.3.5). Qualifications (p. 329):
1. The line has wiggles, because the divergence strength varies along the attractor.
2. Divergence saturates when the separation is comparable to the attractor's diameter.
3. "Liapunov exponent" is a sloppy name for λ. An n-dimensional system has n exponents λ_k, defined by the principal axes of an ellipsoid grown from an infinitesimal sphere: $\delta_k(t)\sim\delta_k(0)e^{\lambda_kt}$. For large t the most positive λ_k dominates, so λ here is the *largest* exponent. Also λ depends slightly on the trajectory, so one should average over many points.

**Time horizon.** The error grows as $\|\delta_0\|e^{\lambda t}$. Let a be the tolerance. Prediction fails when $\|\delta(t)\|\ge a$, i.e. (added step) $t\ge\frac1\lambda\ln\frac{a}{\|\delta_0\|}$. So
$$t_{\text{horizon}}\sim O\Big(\frac1\lambda\ln\frac{a}{\|\delta_0\|}\Big).$$
The logarithm hurts: however much we reduce the measurement error, we cannot predict longer than a few multiples of 1/λ (p. 330).

*Intuition note:* Each factor of 10 in measurement precision buys only a fixed extra amount of time, ln10/λ. This is why even a millionfold improvement in instruments extends forecasts only modestly (2.5 times in Example 9.3.1).

**Example 9.3.1 (p. 330).** Tolerance $a=10^{-3}$.
- With $\|\delta_0\|=10^{-7}$: $t_{\text{horizon}}\approx\frac1\lambda\ln(10^4)=\frac{4\ln10}{\lambda}$.
- With $\|\delta_0\|=10^{-13}$ (a millionfold better): $\frac1\lambda\ln(10^{10})=\frac{10\ln10}{\lambda}$.
- So we can predict only 10/4 = 2.5 times longer.

Lorenz suggested this is why long-term weather prediction is so difficult (p. 331).

**Defining chaos (p. 331).** No universally accepted definition exists. The working definition: *chaos is aperiodic long-term behavior in a deterministic system that exhibits sensitive dependence on initial conditions.*
1. Aperiodic: some trajectories do not settle to fixed points, periodic orbits or quasiperiodic orbits. They should not be too rare, e.g. an open set of initial conditions, or nonzero probability for a random initial condition.
2. Deterministic: no random or noisy inputs or parameters. The irregularity comes from nonlinearity.
3. Sensitive dependence: nearby trajectories separate exponentially fast, i.e. there is a positive Liapunov exponent.

**Example 9.3.2 (p. 331).** $\dot x=x$ is deterministic and nearby trajectories separate exponentially. It is not chaotic. Trajectories go to infinity, which acts like an attracting fixed point, and chaotic behavior should be aperiodic, which excludes fixed points as well as periodic behavior.

**Defining attractor (pp. 331–332).** Loosely, an attractor is a set to which all neighbouring trajectories converge. Precisely, it is a closed set A with three properties (the author notes disagreement about the exact definition; p. 331):
1. *Invariant:* a trajectory that starts in A stays in A.
2. *Attracts an open set of initial conditions:* there is an open set U ⊃ A such that x(0) ∈ U implies dist(x(t),A) → 0. The largest such U is the *basin of attraction*.
3. *Minimal:* no proper subset of A satisfies 1 and 2.

**Example 9.3.3 (p. 332).** $\dot x=x-x^3$, $\dot y=-y$. Let I be the segment −1 ≤ x ≤ 1, y = 0. Then I is invariant (the whole x-axis is) and attracts all trajectories in the plane. But it is not minimal: the stable fixed points (±1,0) are proper subsets satisfying 1 and 2. They are the only attractors.

## Toy example (ours, not from the text)
*Volume shrinking.* With σ = 10, b = 8/3, the divergence is −(σ+1+b) = −(10 + 1 + 2.667) = −41/3 ≈ −13.67. Volume obeys V(t) = V(0)e^{−13.67t}. It halves when e^{−13.67t} = 1/2, i.e. t = ln 2/13.67 = 0.693/13.67 ≈ 0.051. After t = 1 it is e^{−13.67} ≈ 1.2×10⁻⁶ of the original.

*Divergence at the same time.* Take λ = 0.9 and an initial error 10⁻⁶. The error reaches size 1 when 10⁻⁶e^{0.9t} = 1, so t = ln(10⁶)/0.9 = 13.82/0.9 ≈ 15.4. Volumes collapse in a few hundredths of a time unit, yet two nearby points separate to order 1 within about 15 time units. Shrinking in some directions and stretching in another are compatible.

*Waterwheel fixed point (formula check).* Let K = 1, ν = 2, πgr q₁ = 6. The Rayleigh number is 6/(1·2) = 3 > 1, so rotation exists. By (16), (ω*)² = 6/2 − 1 = 2, so ω* = ±√2. Check with (13) and (14): b₁ = q₁/(2+1) = q₁/3 and b₁ = Kν/πgr = 2/πgr. These agree because q₁/3 = 2/πgr ⇔ πgr q₁ = 6.

## Concepts
- [[complex system]] — here, a simple deterministic 3D system (Lorenz, waterwheel) with very erratic dynamics (p. 309)
- [[nonlinearity]] — Lorenz has only two quadratic terms, xy and xz, yet is chaotic (p. 319)
- [[state space / phase space]] — space in which trajectories and volume evolution are studied (p. 309, p. 320)
- [[fixed point and stability]] — origin and C± classified as sinks, saddles; stability conditions on r (pp. 322–324)
- [[linear stability analysis]] — trace and determinant of the 2×2 matrix at the origin (p. 322)
- [[bifurcation]] — pitchfork at r = 1, subcritical Hopf at r = r_H (pp. 322–324)
- [[attractor / basin of attraction]] — closed, invariant, attracts an open set, minimal (pp. 331–332)
- [[deterministic chaos]] — aperiodic, deterministic, sensitive to initial conditions (p. 331)
- [[strange attractor / fractal]] — zero-volume "infinite complex of surfaces", dimension ≈ 2.05 as suggested by numerical experiments (pp. 327–328)
- [[Lyapunov exponent]] — growth rate of separation; here the largest of n exponents, λ ≈ 0.9 (p. 329)
- [[lorenz-system]] (new) — the equations above, σ, r, b > 0 (p. 309)
- [[dissipative-system / volume contraction]] (new) — ∇·f < 0, volumes shrink as e^{−(σ+1+b)t} (p. 321)
- [[liapunov-function]] (new) — positive definite function decreasing along trajectories; proves global stability of origin for r < 1 (p. 323)
- [[hopf-bifurcation-subcritical]] (new) — C± lose stability at r_H with an unstable surrounding cycle (p. 324)
- [[saddle-cycle]] (new) — unstable limit cycle with 2D stable and unstable manifolds, possible only in ≥ 3D (p. 324)
- [[rayleigh-number]] (new) — dimensionless drive-to-dissipation ratio; rotation if πgrq₁/(K²ν) > 1 (p. 318)
- [[prediction-time-horizon]] (new) — t ~ (1/λ) ln(a/‖δ₀‖) (p. 330)

## Canonical instances
- [[lorenz-system]] — chaotic flow at σ = 10, b = 8/3, r = 28 (p. 325)
- [[chaotic-waterwheel]] — mechanical model whose reversals mirror lobe-switching on the attractor (pp. 310, 327)
- [[convection-rolls]] — Rayleigh number analogy for onset of steady rotation and chaos (pp. 318–319)
- [[lorenz-weather-prediction]] — long-term weather prediction is hard because of exponential error growth (p. 331)

## Bridges (candidates)
- [same-math] Waterwheel amplitude equations (9) ↔ Lorenz equations: the text states the change of variables exists (Exercise 9.1.3, not printed here).
- [structural-analogy] Waterwheel steady rotation vs. convection rolls ↔ fluid mechanics: both appear when the Rayleigh number passes a threshold.
- [structural-analogy] Time horizon ln(a/‖δ₀‖)/λ ↔ forecasting in complex systems: noise-free models can still be unpredictable beyond a few 1/λ.
- [structural-analogy] Volume contraction plus bounded motion ↔ attractors and basins in dynamical models: dissipation forces long-run behaviour onto a small set.

## Questions this raises
- Why does the sequence of lobe circuits look random if the system has no noise?
- How is the fractal dimension of the attractor measured, and why is it about 2.05?
- If stable limit cycles can exist at some r > r_H, how do they coexist with the strange attractor?
- Can all n Liapunov exponents be computed from data, and what do they sum to?

## Reading notes
- **Part boundaries:** this part starts at §9.0 (printed p. 309) and ends at the end of Example 9.3.3 (p. 332). The unit metadata says it was split at a section boundary, but on these pages §9.3 does not visibly end: the heading 'Defining Attractor and Strange Attractor' (p. 331) is followed only by a definition of attractor, with no separate definition of strange attractor. The chapter continues beyond p. 332 (Section 9.4 and later are referenced as "next" but not given).
- **Page offset:** printed = pdf − 19.
- **Text-layer problems:** Greek letters are garbled (θ, ω, σ, λ, ν, τ, Δ appear as R, X, T, M, v, U, %). I used the page images. The tag of the b₁ formula, printed between (12) and (14), is missing in the image. I labelled it (13), as the text itself does later (p. 318).
- **Cross-references:** Exercises 9.1.1–9.1.3, 9.2.1, 9.2.2, Example 9.5.2, Section 9.4 and Example 11.5.1 are cited but not printed in this part. The text says "In the next section" at the end of §9.2, which is §9.3, so the numbering is consistent.
- **Not claimed:** the proof that the Hopf bifurcation is subcritical and the 2.05 dimension are cited, not derived here.
