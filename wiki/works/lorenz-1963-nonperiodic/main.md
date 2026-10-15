---
id: lorenz-1963-nonperiodic/main
work: lorenz-1963-nonperiodic
unit: paper
pages: 130–141
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
audited: 2026-10-15
audit_fixes: 11
---
# Deterministic Nonperiodic Flow (Lorenz 1963)

## L0 — One line
Bounded, dissipative, forced deterministic systems can have solutions that never repeat, and such nonperiodic solutions are ordinarily unstable, so if the results apply to the atmosphere (ostensibly nonperiodic), very-long-range prediction would be impossible by any method unless the present state is known exactly.

## L1 — The gist (≤ 120 words)
Can a deterministic system under steady forcing show irregular, never-repeating behaviour? Lorenz studies finite sets of nonlinear ordinary differential equations that mimic forced dissipative flow. A typical forced dissipative form has bounded solutions; for bounded systems, nonperiodic solutions are ordinarily unstable. He integrates a three-variable convection model numerically. Its solution crosses irregularly between two spirals, and all solutions are found to be unstable. A one-dimensional map read off the numerics suggests why: nearby states separate. The result matters because, if it applies to the atmosphere (ostensibly nonperiodic), prediction of the distant future is impossible by any method unless present conditions are known exactly; an exception may exist if no "analogues" (past states matching within observation error) have occurred.

**Prerequisites:** ordinary differential equations; phase space; linearization and eigenvalues; divergence of a vector field; rational vs irrational numbers; countable vs uncountable sets.

## L2 — Key ideas (5–10 bullets)
- Nonperiodic flow need not come from random forcing: in dissipative linear systems constant forcing ultimately gives constant response, but nonlinear (advective) terms can let constant forcing give variable response. (p. 131)
- In systems of the form (4), dissipation that outweighs forcing at large values of the energy-like quantity $Q$ ultimately traps every trajectory in a bounded region. (pp. 131–132)
- Central trajectories (those that return arbitrarily close to their own past) are unstable if nonperiodic; noncentral nonperiodic ones are not uniformly stable. For practical prediction, all nonperiodic trajectories are effectively unstable. (pp. 132–133)
- If a forward-difference scheme with small $\Delta t$ is bounded, the double-approximation scheme (14) (a two-stage numerical step) also does not blow up, for forced dissipative systems of form (4). (p. 134)
- The three-variable convection system (25)–(27) has volume contraction at the rate $\sigma+b+1$, an onset of convection at $r=1$, and three steady states when $r>1$. (pp. 135–136)
- At $\sigma=10$, $b=8/3$, $r=28$ the numerical solution is irregular. Within the accuracy of the printed values, it lies on a pair of surfaces that appear to merge. (pp. 136–138)
- Successive maxima of $Z$ fall, within round-off, on a one-dimensional curve (a two-to-one relation). In an idealised piecewise-linear map (a tent map), all periodic sequences are unstable and all but a measure-zero set are nonperiodic; Lorenz infers the same for the real curve, whose slope apparently exceeds unity in magnitude. (pp. 138–140)
- The conclusions are drawn from a finite numerical run, not a proof. (p. 140)
- For the atmosphere, Lorenz says the results indicate that prediction of the sufficiently distant future is impossible by any method unless present conditions are known exactly. If two analogues (states matching within observation error) have occurred, no scheme could have been right both times; if none has, an accurate scheme may exist. The length of "very-long-range" is left open. (p. 141)

## L3 — Walkthrough

### 1. Introduction (pp. 130–131)
Hydrodynamical systems can show steady, periodic or irregular flow, as in rotating-basin experiments. Irregular flow is typical of turbulence. A short-range weather forecaster is forced to predict the details of the large-scale eddies (cyclones and anticyclones), so there are occasions when more than the statistics of irregular flow matter (p. 130).

Lorenz studies **nonperiodic** solutions, which never repeat exactly. He studies their ultimate behaviour, not transients. Ordinarily, nonperiodic solutions cannot readily be determined except by numerical procedures (p. 130).

He works with finite deterministic ordinary differential equations that are dissipative (viscous and thermal losses) and forced (to avoid decay to rest). For the system to be deterministic, forcing that is not constant must itself vary by a deterministic rule (p. 131).

For dissipative systems governed by finite sets of linear equations, constant forcing leads ultimately to a constant response and periodic forcing to a periodic response, so nonperiodic flow has sometimes been attributed to nonperiodic or random forcing; this reasoning does not apply to nonlinear equations. With nonlinear advection (transport of a fluid property by the fluid's own motion), constant forcing can give a variable response. Both periodic and nonperiodic flow appear in rotating-basin experiments with constant heating (p. 131).

### 2. Phase space (p. 131–132)
The system is
$$dX_i/dt=F_i(X_1,\dots,X_M),\quad i=1,\dots,M, \tag{1}$$
with continuous first partial derivatives $\partial F_i/\partial X_j$. The state is a point in $M$-dimensional space $\Gamma$. A solution is a trajectory. Existence and uniqueness (valid throughout some time interval containing $t_0$) give
$$X_i=f_i(X_{10},\dots,X_{M0},t),\tag{2}$$
$$f_i(X_{10},\dots,X_{M0},t_0)=X_{i0}.\tag{3}$$
So exactly one trajectory passes through each point, and time continuously deforms regions of $\Gamma$ (p. 131).

For a conservative system, a positive definite $Q$ is invariant and trajectories lie on surfaces of constant $Q$. With dissipation and forcing, suppose that whenever $Q\ge Q_1$ the dissipation exceeds the forcing's effect. Then $-dQ/dt$ has a positive lower bound for $Q\ge Q_1$, and trajectories become trapped where $Q<Q_1$ (p. 131).

The typical forced dissipative system is
$$dX_i/dt=\sum_{j,k}a_{ijk}X_jX_k-\sum_j b_{ij}X_j+c_i, \tag{4}$$
where $\sum a_{ijk}X_iX_jX_k$ vanishes identically, $\sum b_{ij}X_iX_j$ is positive definite, and the $c_i$ are constants. With
$$Q=\tfrac12\sum_i X_i^2, \tag{5}$$
and $e_i$ the roots of
$$\sum_j (b_{ij}+b_{ji})e_j=c_i, \tag{6}$$
it follows from (4) that
$$dQ/dt=\sum_{i,j}b_{ij}e_ie_j-\sum_{i,j}b_{ij}(X_i-e_i)(X_j-e_j). \tag{7}$$
The right side of (7) vanishes only on the surface of an ellipsoid $E$ and is positive only inside it. The surfaces of constant $Q$ are concentric spheres. If a sphere $S$ bounds a region $R$ containing $E$, every trajectory is eventually trapped in $R$ (p. 132).

*Intuition note:* Forcing pushes the state outward only up to a limit, and dissipation pulls it back beyond that limit. So every trajectory ends up trapped inside a bounded ball (the region $R$) and does not leave it.

### 3. Instability of nonperiodic flow (pp. 132–133)
Assume a unique trajectory through each point, continuous deformation, and uniform boundedness: there is a bounded region $R$ within which every trajectory ultimately remains (p. 132).

**Definitions (p. 132).**
- A **limit point** $P_0$ of $P(t)$ is approached arbitrarily closely arbitrarily often. The set of limit points forms the **limiting trajectories**.
- A trajectory is **central** if it is among its own limiting trajectories. Otherwise it is **noncentral**.
- $P(t)$ is **stable at a point** $P(t_1)$ if, for any $\epsilon>0$, there is $\delta(\epsilon,t_1)>0$ such that $|P_1(t_1)-P(t_1)|<\delta$ implies $|P_1(t_2)-P(t_2)|<\epsilon$ for all $t_2>t_1$. Otherwise it is **unstable** there.
- A trajectory stable at one point is stable at every point. It is then simply "stable".
- It is **uniformly stable** if $\delta$ has a positive lower bound as $t_1\to\infty$.
- A trajectory is **quasi-periodic** if, for arbitrarily large intervals $\tau$, $P(t+\tau)$ ultimately stays arbitrarily close to $P(t)$.
- Periodic trajectories are special cases of quasi-periodic ones.
- A trajectory that is not quasi-periodic is **nonperiodic**. For a nonperiodic $P(t)$, $P(t_1+\tau)$ may come arbitrarily close to $P(t_1)$ for some large $\tau$, but then $P(t+\tau)$ cannot stay arbitrarily close to $P(t)$ as $t\to\infty$ (p. 133).
- Periodic trajectories are obviously central. Quasi-periodic central trajectories include multiple periodic ones with incommensurable periods; quasi-periodic noncentral ones include those that approach periodic trajectories asymptotically. Nonperiodic trajectories may be central or noncentral (p. 133).

**Theorems (pp. 132–133).**
- A trajectory with a stable limiting trajectory is quasi-periodic.
- Hence a stable central trajectory is quasi-periodic. Equivalently, a nonperiodic central trajectory is unstable.
- A uniformly stable noncentral trajectory is quasi-periodic. Equivalently, a nonperiodic noncentral trajectory is not uniformly stable.
- Lorenz thinks a stable but non-uniformly-stable nonperiodic noncentral trajectory is possible on paper but not characteristic of real flows. Its very stability would be one of its transient properties, which tends to die out as time progresses.
- For an observable nonperiodic system, two states differing by imperceptible amounts may eventually evolve into two considerably different states. If there is any error in observing the present state, an acceptable prediction of an instantaneous state in the distant future may well be impossible (p. 133).
- Since initial conditions cannot be measured precisely, central and nearby noncentral trajectories cannot be told apart. So all nonperiodic trajectories are effectively unstable for practical prediction (p. 133).

*Intuition note:* A central trajectory that never repeats cannot be stable, because a stable one would keep close to its own past and so would be quasi-periodic; for noncentral trajectories only the weaker result (not uniformly stable) holds. Two states that differ by an unmeasurable amount can therefore end up far apart.

### 4. Numerical integration (pp. 133–134)
Let $X_{i,n}=X_i(t_0+n\Delta t)$ with auxiliary approximations
$$X_{i(n+1)}=X_{i,n}+F_i(P_n)\Delta t,\tag{9}$$
$$X_{i((n+2))}=X_{i(n+1)}+F_i(P_{(n+1)})\Delta t.\tag{10}$$
The forward-difference scheme is $X_{i,n+1}=X_{i(n+1)}$ (11). The centered scheme is $X_{i,n+1}=X_{i,n-1}+2F_i(P_n)\Delta t$ (12). It is unsuitable for determinism because $X_{\cdot,n}$ does not fix $X_{\cdot,n+1}$ (p. 133).

The **double-approximation** scheme used throughout is
$$X_{i,n+1}=X_{i,n}+\tfrac12[F_i(P_n)+F_i(P_{(n+1)})]\Delta t,\tag{13}$$
which by (9) and (10) equals
$$X_{i,n+1}=\tfrac12(X_{i,n}+X_{i((n+2))}).\tag{14}$$
Strictly, a finite-precision bounded numerical solution must repeat. In practice this is ignored if the number of possible states far exceeds the number of iterations (p. 134).

For forward difference applied to (4):
$$Q_{n+1}=Q_n+(dQ/dt)_n\Delta t+\tfrac12\sum_iF_i^2(P_n)\Delta t^2.\tag{15}$$
Take $S'$ with interior $R'\supset E$ and $S\supset S'$ with interior $R$. In $R'$, $\sum F_i^2$ and $dQ/dt$ are bounded above, so small $\Delta t$ keeps $P_{n+1}$ in $R$. In $R-R'$, $dQ/dt$ has a negative upper bound, so $Q_{n+1}<Q_n$ for small $\Delta t$. Then a particle that enters $R$ stays in $R$, although a blow-up may still occur if the particle starts outside $R$. Because $R$ is convex, the double-approximation scheme (14) is bounded too. For a conservative system, forward difference gives
$$Q_{n+1}=Q_n+\tfrac12\sum_iF_i^2(P_n)\Delta t^2,\tag{16}$$
which grows without limit unless the solution approaches a steady state asymptotically (p. 134). A similar result holds when the double-approximation scheme (14) is applied to a conservative system (p. 134).

### 5. The convection equations of Saltzman (pp. 134–135)
For two-dimensional convection in a layer of depth $H$ with temperature difference $\Delta T$ (here $\psi$ is a stream function, a function whose derivatives give the 2-d flow velocity, and $\theta$ the departure of temperature from the no-convection state; $g,\alpha,\nu,\kappa$ are gravity, the thermal expansion coefficient, kinematic viscosity and thermal conductivity; $\partial(\cdot,\cdot)/\partial(x,z)$ is a Jacobian, the advection term):
$$\frac{\partial}{\partial t}\nabla^2\psi=-\frac{\partial(\psi,\nabla^2\psi)}{\partial(x,z)}+\nu\nabla^4\psi+g\alpha\frac{\partial\theta}{\partial x},\tag{17}$$
$$\frac{\partial}{\partial t}\theta=-\frac{\partial(\psi,\theta)}{\partial(x,z)}+\frac{\Delta T}{H}\frac{\partial\psi}{\partial x}+\kappa\nabla^2\theta.\tag{18}$$
The problem is most tractable with free upper and lower boundaries, where $\psi$ and $\nabla^2\psi$ vanish (p. 134). Rayleigh found that fields of motion of the form
$$\psi=\psi_0\sin(\pi aH^{-1}x)\sin(\pi H^{-1}z),\tag{19}$$
$$\theta=\theta_0\cos(\pi aH^{-1}x)\sin(\pi H^{-1}z)\tag{20}$$
would develop (here $a$ sets the horizontal scale of the cells relative to $H$) if the Rayleigh number (a dimensionless measure of the thermal driving)
$$R_a=g\alpha H^3\Delta T\nu^{-1}\kappa^{-1}\tag{21}$$
exceeds
$$R_c=\pi^4a^{-2}(1+a^2)^3.\tag{22}$$
The minimum is $27\pi^4/4$ at $a^2=\tfrac12$ (p. 134).

Lorenz truncates Saltzman's Fourier series to three terms:
$$a(1+a^2)^{-1}\kappa^{-1}\psi=X\sqrt2\sin(\pi aH^{-1}x)\sin(\pi H^{-1}z),\tag{23}$$
$$\pi R_c^{-1}R_a\Delta T^{-1}\theta=Y\sqrt2\cos(\pi aH^{-1}x)\sin(\pi H^{-1}z)-Z\sin(2\pi H^{-1}z).\tag{24}$$
This gives
$$\dot X=-\sigma X+\sigma Y,\tag{25}$$
$$\dot Y=-XZ+rX-Y,\tag{26}$$
$$\dot Z=XY-bZ.\tag{27}$$
Here the dot is $d/d\tau$ with $\tau=\pi^2H^{-2}(1+a^2)\kappa t$, $\sigma=\kappa^{-1}\nu$ (Prandtl number), $r=R_c^{-1}R_a$ and $b=4(1+a^2)^{-1}$. $X$ is proportional to convective intensity, $Y$ to the temperature difference between ascending and descending currents, and $Z$ to the distortion of the vertical temperature profile. The equations may be realistic for slightly supercritical $R_a$, but not for strong convection, given the extreme truncation (p. 135).

### 6. Applications of linear theory (pp. 135–136)
The transformation
$$X'=X,\quad Y'=Y,\quad Z'=Z-r-\sigma\tag{28}$$
puts (25)–(27) into the form (4), so solutions stay bounded and Sections 2–4 apply (p. 135).

Small perturbations $(x_0,y_0,z_0)$ obey
$$\begin{bmatrix}\dot x_0\\ \dot y_0\\ \dot z_0\end{bmatrix}=\begin{bmatrix}-\sigma&\sigma&0\\ r-Z&-1&-X\\ Y&X&-b\end{bmatrix}\begin{bmatrix}x_0\\ y_0\\ z_0\end{bmatrix}.\tag{29}$$
The matrix is $3\times3$ and its coefficients vary with time unless the base state is steady. A small volume $V_0$ changes at the rate given by the trace:
$$\dot V_0=-(\sigma+b+1)V_0,\tag{30}$$
which is the divergence of the flow:
$$\frac{\partial\dot X}{\partial X}+\frac{\partial\dot Y}{\partial Y}+\frac{\partial\dot Z}{\partial Z}=-(\sigma+b+1).\tag{31}$$
Every small volume shrinks to zero at this rate, independent of $X,Y,Z$. This need not mean it shrinks to a point, because it may flatten into a surface. All trajectories are therefore confined ultimately to a subspace of zero volume, which contains all central trajectories (p. 135).

At the no-convection state $X=Y=Z=0$ the characteristic equation is
$$[\lambda+b][\lambda^2+(\sigma+1)\lambda+\sigma(1-r)]=0.\tag{32}$$
For $r>0$ it has three real roots. All are negative for $r<1$ and one is positive for $r>1$. So convection starts at $r=1$, i.e. $R_a=R_c$, as Rayleigh found. For $r>1$ there are two more steady states, $X=Y=\pm\sqrt{b(r-1)}$, $Z=r-1$ (pp. 135–136). Their characteristic equation is
$$\lambda^3+(\sigma+b+1)\lambda^2+(r+\sigma)b\lambda+2\sigma b(r-1)=0.\tag{33}$$
It has one real negative root and two complex conjugate roots when $r>1$. The complex pair is pure imaginary when
$$r=\sigma(\sigma+b+3)(\sigma-b-1)^{-1}.\tag{34}$$
If $\sigma<b+1$, no positive $r$ satisfies (34), so steady convection is always stable. If $\sigma>b+1$, steady convection is unstable for sufficiently high Rayleigh numbers. This applies only to the idealised convection of (25)–(27), not to the partial differential equations (17)–(18). The complex roots show that a disturbed unstable steady convection oscillates in intensity. Linear theory cannot say what happens at large amplitude (p. 136).

*Intuition note:* The flow contracts every phase-space volume at a fixed rate, but this does not mean a volume shrinks to a point; it may flatten into a surface. Steady convection can also be unstable (when $\sigma>b+1$ at high enough $r$). Linear theory describes small disturbances only; it does not reveal what happens at large amplitude.

### 7. Numerical integration of the convection equations (pp. 136–140)
**Setup.** Parameters are $\sigma=10$, $a^2=\tfrac12$ (so $b=8/3$), giving critical $r=470/19=24.74$. Lorenz chose $r=28$. The steady-convection points are $(6\sqrt2,6\sqrt2,27)$ and $(-6\sqrt2,-6\sqrt2,27)$. He used scheme (14), $\Delta\tau=0.01$, on a Royal McBee LGP-30, about one second per iteration. The start was $(0,1,0)$. In Tables 1–2, values are printed ×10 and truncated at the decimal point (pp. 136–137).

**Trajectory (pp. 137–138).**
- All variables grow rapidly. Convection exceeds steady strength by step 35.
- The flow reverses near step 60 and reaches a state near steady convection by step 85.
- From then on, amplified oscillations grow until near step 1650 (Fig. 1).
- After step 1650, $Y$ changes sign irregularly.
- Fig. 2 shows a spiral outward from $C'$. Near step 1650 the trajectory crosses to the neighbourhood of $C$, spirals there, then returns to $C'$.
- Fig. 3, built from printed values, shows $X$ as a single-valued function over part of the $(Y,Z)$ plane, and as two values elsewhere.
- Within the accuracy of the printed values, the trajectory lies on a pair of surfaces that appear to merge.
- Other trajectories from far away soon meet these surfaces, so they seem formed of limiting trajectories. The origin is a steady state, so no trajectory can pass through it; however, two trajectories emanate from it (approach it as $\tau\to-\infty$), and the heavy curve they form in Fig. 3 is a natural boundary that trajectories tend to follow but not cross. The holes near $C$ and $C'$ are also regions that cannot be occupied once abandoned (p. 138).
- The trajectory seems to leave a spiral only after exceeding a critical distance from the centre. How far this distance is exceeded appears to determine where the next spiral is entered, which in turn seems to fix the number of circuits there. So some single feature of one circuit should predict the same feature of the next; Lorenz picks the maximum of $Z$ (p. 138).

**First-return map (pp. 138–139).** Let $M_n$ be the $n$th maximum of $Z$ (Table 2). Fig. 4 plots $M_{n+1}$ against $M_n$. Within round-off, the relation is single-valued and two-to-one. $X$ and $Y$ change sign after a maximum above about 385. Maxima near 385 are followed by close approaches to the origin and then exceptionally large maxima, so the initial $M_1=483$ is shown as following 385. An investigator unaware of the governing equations could therefore build an empirical prediction scheme from Figs. 2 and 4. Its accuracy would be limited by the exactness of the figures and by the accuracy with which the initial $X,Y,Z$ are observed (pp. 138–139).

Lorenz idealises Fig. 4 by Fig. 5, for $M_n\in[0,1]$:
$$M_{n+1}=2M_n \ (M_n<\tfrac12);\quad M_{n+1}\ \text{undefined}\ (M_n=\tfrac12);\quad M_{n+1}=2-2M_n\ (M_n>\tfrac12).\tag{35}$$
Repeated application gives
$$M_n=m_n\pm2^nM_0,\quad m_n\text{ an even integer}.\tag{36}$$
Classes of sequences (p. 139):
- $M_0=u/2^p$ with $u$ odd: $M_{p-1}=\tfrac12$ and the sequence terminates. This is a denumerable set, corresponding to trajectories that hit the no-convection state directly.
- $M_0=u/2^pv$ with $u,v$ relatively prime odd: $M_{p+1+k}=u_k/v$ with $u_k$ even. The finite number of proper fractions forces repetition, so the sequence is periodic. This is a denumerable set, corresponding to periodic trajectories. Examples: $2/3$; $2/5, 4/5$; $2/7,4/7,6/7$; $2/9,4/9,8/9$. The two three-phase sequences differ: the first has two numbers above $\tfrac12$ (two circuits about $C$, then one about $C'$, or vice versa), the second only one (three circuits about $C$, then three about $C'$, so only $Z$ varies in three phases while $X$ and $Y$ vary in six).
- $M_0$ irrational: by (36) $M_{n+k}\ne M_n$ for $k>0$, so there is no repetition. These form a nondenumerable set. They may conceivably approach periodic sequences asymptotically (and be quasi-periodic), or may be nonperiodic (p. 140).

**Instability (p. 140).** If $M_0'=M_0+\epsilon$ with $\epsilon$ sufficiently small, then $M_k'=M_k\pm2^k\epsilon$. All periodic sequences are unstable. No other sequence can approach them asymptotically. All sequences except a set of measure zero are nonperiodic. In Fig. 4, periodic sequences approximately analogous to those above are $398$; $377,410$; $369,391,414$; $362,380,419$. The numerical solution temporarily approaches them from iterations 5340, 4881, 3625 and 3926, and eventually departs from each, so each is presumably unstable. Generally, $M'_{n+k}=M_{n+k}+\Lambda\epsilon$, with $\Lambda$ the product of the curve's slopes at $M_n,\dots,M_{n+k-1}$. The curve apparently has slope of magnitude above unity everywhere, so all trajectories are unstable (p. 140).

Lorenz says these conclusions rest on a finite numerical segment, cannot be regarded as mathematically proven, and the evidence is strong (p. 140).

**Apparent contradiction (p. 140).** Two trajectories cannot merge, yet the two surfaces appear to. At times $\tau_0,\tau_1$, volumes obey
$$V_0(\tau_1)=e^{-(\sigma+b+1)(\tau_1-\tau_0)}V_0(\tau_0),\tag{37}$$
by (30). A circuit about $C$ or $C'$ takes about 70 iterations, so, as printed, $\tau_2=\tau_1+0.7$ (the times there are named $\tau_0,\tau_1$, so this is presumably a misprint for $\tau_1=\tau_0+0.7$). Since $\sigma+b+1=41/3$,
$$V_0(\tau_1)=0.00007\,V_0(\tau_0).\tag{38}$$
Particles in suitable directions come together very rapidly and appear to merge. Following the surfaces round a circuit, each "surface" is really a pair, so there are four where they appear to merge, then eight, and so on. Lorenz concludes there is an infinite complex of surfaces, each extremely close to one of two merging surfaces. The values at which a line parallel to the $X$-axis meets the surfaces may be likened to the numbers in $[0,1]$ whose expansions contain only zeros and ones. That set is nondenumerable but has measure zero (total length zero on the line). Repeating expansions, which are rational, correspond to periodic or quasi-periodic trajectories and form a denumerable set (p. 140).

### 8. Conclusion (pp. 140–141)
- Forced dissipative systems may show periodic or irregular behaviour without matching forcing, and constant forcing can give either (p. 140).
- A nonperiodic solution with no transient component must be unstable, in the sense that solutions temporarily approximating it do not continue to do so. One with a transient component is sometimes stable, but then its stability is one of its transient properties, which tends to die out (pp. 140–141).
- The three-variable system has three steady-state solutions and a denumerably infinite set of periodic solutions. All solutions, and in particular the periodic ones, are found to be unstable, so the remaining solutions cannot in general approach the periodic ones asymptotically and are nonperiodic (p. 141).
- Applied to the atmosphere, which is ostensibly nonperiodic, the results indicate that prediction of the sufficiently distant future is impossible by any method, unless the present conditions are known exactly. In view of the inevitable inaccuracy and incompleteness of weather observations, precise very-long-range forecasting would seem to be non-existent (p. 141).
- **Caveat (Lorenz):** the atmosphere is not usually regarded as deterministic or finite, and the lack of periodicity is not a mathematical certainty (p. 141).
- The foundation of the principal result is that any bounded system of finite dimensionality must eventually come arbitrarily close to a state it has previously assumed; if the system is stable, its future then stays arbitrarily close to its past and is quasi-periodic (p. 141).
- The crucial point for the atmosphere is whether **analogues** must have occurred since the atmosphere's state was first observed. Analogues are two or more states of the atmosphere, with its environment, that resemble each other so closely that the differences may be ascribed to observation errors (if unobserved features matter, two successions of states must be nearly alike). If two analogues have occurred, then, since the atmosphere has not been observed to be periodic, the successions that followed must eventually have differed, and no forecasting scheme could have given correct results both times. If analogues have not occurred in this period, some accurate very-long-range scheme may exist; if it does exist, the atmosphere will acquire quasi-periodic behaviour, never to be lost once an analogue occurs. This quasi-periodic behaviour need not be established, even if very-long-range forecasting is feasible, if the variety of possible atmospheric states is so immense that analogues need never occur. These conclusions do not depend on whether the atmosphere is deterministic (p. 141).
- How long "very-long-range" is remains open; the results do not answer it for the atmosphere, and it could conceivably be "a few days or a few centuries". In an idealised system the answer may be obtained by comparing pairs of numerical solutions with nearly identical initial conditions; for the real atmosphere, if all other methods fail, one can wait for an analogue (p. 141).

## Toy example (ours, not from the text)
Take the tent map (35) with two starts that differ by $\epsilon=0.01$: $M_0=0.30$ and $M_0'=0.31$.

| n | $M_n$ (from 0.30) | $M_n'$ (from 0.31) | $|M_n-M_n'|$ |
|---|---|---|---|
| 0 | 0.30 | 0.31 | 0.01 |
| 1 | 0.60 | 0.62 | 0.02 |
| 2 | $2-1.20=0.80$ | $2-1.24=0.76$ | 0.04 |
| 3 | $2-1.60=0.40$ | $2-1.52=0.48$ | 0.08 |
| 4 | $2(0.40)=0.80$ | $2(0.48)=0.96$ | 0.16 |
| 5 | $2-1.60=0.40$ | $2-1.92=0.08$ | 0.32 |

From $n=2$ the first sequence alternates $0.8, 0.4, 0.8, 0.4$; this periodic pair is $4/5, 2/5$, the tabulated two-phase sequence. The gap doubles each step, as in $M_k'=M_k\pm2^k\epsilon$ (p. 140). By $n=5$ the nearby start has left the cycle: $0.08$ versus $0.40$.

## Concepts
- [[deterministic chaos]] — bounded, nonperiodic deterministic solutions that are unstable. Lorenz does not use the word "chaos" (p. 133).
- [[state space / phase space]] — $M$-dimensional space whose points are states and whose curves are trajectories (p. 131).
- [[attractor / basin of attraction]] — the ultimate set approached by trajectories. Here it is a zero-volume subspace holding all central trajectories; Lorenz does not use the word "attractor" (canon link; not stated in this unit) (p. 135).
- [[strange attractor / fractal]] — Lorenz describes an infinite complex of surfaces, but does not use this term (p. 140).
- [[fixed point and stability]] — steady states of (25)–(27) and the definitions of stable and unstable trajectories (pp. 132, 135).
- [[linear stability analysis]] — eigenvalues of (29) at steady states give $r=1$ and (34) (pp. 135–136).
- [[nonlinearity]] — advection terms let constant forcing yield variable response (p. 131).
- [[bifurcation]] — onset of convection at $r=1$ and the instability of steady convection at (34), without the word "bifurcation" (pp. 135–136).
- [[dissipative-trapping-region]] (new) — dissipation beating forcing outside an ellipsoid, so trajectories are trapped in a bounded region (p. 132).
- [[volume-contraction]] (new) — phase-space volume shrinks at the rate $\sigma+b+1$ (p. 135).
- [[first-return-map-of-maxima]] (new) — mapping each maximum of $Z$ to the next, idealised as (35) (p. 139).
- [[analogue-forecasting]] (new) — analogues: two or more atmospheric states (with environment) so alike that differences may be ascribed to observation errors; Lorenz asks whether they have occurred (p. 141).

## Canonical instances
- [[lorenz-system]] — equations (25)–(27) at $\sigma=10$, $b=8/3$, $r=28$ (pp. 135, 136).
- [[rayleigh-benard-convection]] — the physical background for the three-variable truncation (p. 134).
- [[tent-map]] — idealisation (35) of the Fig. 4 return map (p. 139).
- [[atmospheric-predictability]] — if the results apply to the (ostensibly nonperiodic) atmosphere, prediction of the sufficiently distant future is impossible unless the present state is known exactly; with the open question of analogues (p. 141).

## Bridges (candidates)
- [structural-analogy] Instability of nonperiodic trajectories ↔ Lyapunov exponent: the slope product $\Lambda$ with $|\text{slope}|>1$ is a local growth rate of separation.
- [same-math] Tent map (35) ↔ one-dimensional chaotic maps: the doubling of $\epsilon$ is the same iterated piecewise-linear map.
- [structural-analogy] Volume contraction (30)–(31) ↔ dissipative dynamics and attractors: shrinking volume with unstable motion needs a thin attractor set.
- [metaphor] Analogue forecasting ↔ nearest-neighbour methods: both rely on repeated similar states.

## Questions this raises
- How can a solution be unstable and stay in a bounded region of zero volume at once?
- What would show that the apparent slope $>1$ of the Fig. 4 curve holds everywhere, beyond finite numerics?
- Do the claims hold when the full PDEs (17)–(18) replace the three-mode truncation, which Lorenz says is unreliable for strong convection?
- How long is "very-long-range" for the real atmosphere?

## Reading notes
- The page labels give no printed numbers, but the images show them: printed = pdf + 129 (pdf 1 = p. 130 … pdf 12 = p. 141). References use printed pages.
- Running header: Journal of the Atmospheric Sciences, Vol. 20, March 1963. The manuscript was received 18 November 1962, revised 7 January 1963 (p. 130).
- The equations were checked against the images; no unreadable passages.
- The numbers in Tables 1 and 2 are printed as ×10 truncated integers, as Lorenz explains (p. 137). I did not copy the tables.
- Lorenz says rigorous proofs of some of Section 3's theorems are to be found in Nemytskii and Stepanov (p. 132); the arguments given here are brief. Of the numerical conclusions he says they "cannot be regarded as mathematically proven" (p. 140). The source prints $\tau_2=\tau_1+0.7$ in the passage leading to (38), although the times there are named $\tau_0,\tau_1$ (p. 140).
