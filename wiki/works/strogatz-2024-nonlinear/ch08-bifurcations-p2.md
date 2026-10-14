---
id: strogatz-2024-nonlinear/ch08-bifurcations-p2
work: strogatz-2024-nonlinear
unit: "8 Bifurcations Revisited (part 2/3): 8.4 Global Bifurcations of Cycles, 8.5 Hysteresis in the Driven Pendulum and Josephson Junction, 8.6 Coupled Oscillators and Quasiperiodicity, 8.7 Poincaré Maps (to the start of Example 8.7.4)"
pages: 264–286
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Global bifurcations of cycles, the driven pendulum, coupled oscillators, Poincaré maps

## L0 — One line
Limit cycles can appear or vanish through four routes, three of them global. Each route has its own amplitude and period scaling, and the Poincaré (first-return) map turns questions about closed orbits into questions about fixed points of a map.

## L1 — The gist (≤ 120 words)
How are limit cycles born and destroyed in two-dimensional flows, and how can we prove that cycles exist and are stable? Besides the Hopf bifurcation there are three global bifurcations: saddle-node of cycles, infinite-period, and homoclinic. Their amplitude and period scale differently near the bifurcation, which can help experimenters learn about the mechanism. The driven pendulum / Josephson junction shows two of them and explains hysteresis. Two coupled oscillators live on a torus, where the flow can be phase-locked, rational, or quasiperiodic. A Poincaré map proves cycle existence and gives stability through Floquet multipliers (eigenvalues of the linearized return map). A homoclinic bifurcation is one where a cycle touches a saddle point.

**Prerequisites:** one-dimensional flows and saddle-node bifurcation; Hopf bifurcation; Jacobian eigenvalues; polar coordinates; vector fields on the circle (nonuniform oscillator); intermediate value theorem.

## L2 — Key ideas (5–10 bullets)
- Besides Hopf there are three common global bifurcations of cycles in 2D: saddle-node of cycles, infinite-period, and homoclinic. They involve large regions of the phase plane, so they are harder to detect (p. 264).
- Generic scaling laws separate the four types by the amplitude and period of the stable cycle near the bifurcation (Table 8.4.1). An exception, the van der Pol oscillator at ε = 0, is nongeneric, and a rescaling restores the Hopf law (pp. 267–268).
- For the driven pendulum / Josephson junction with I > 1, a Poincaré-map argument proves one closed orbit exists. An energy argument proves no second rotation exists (pp. 270–273).
- For small damping α, decreasing I destroys the rotating cycle in a homoclinic bifurcation. For large α an infinite-period bifurcation occurs instead. Together with the saddle-node of fixed points at I = 1 these give the stability diagram (pp. 273–275).
- The hysteretic I–V curve follows: the voltage jumps up at I = 1, but returns to zero like [ln(I − I_c)]⁻¹, which looks like a jump (p. 276).
- Uncoupled oscillators on a torus give closed orbits (p:q torus knots when p, q ≥ 2 have no common factors) if ω₁/ω₂ is rational and dense quasiperiodic orbits if irrational (pp. 278–279).
- Coupled oscillators phase-lock if |ω₁ − ω₂| < K₁ + K₂, at the compromise frequency ω*. The lock is destroyed by a saddle-node of cycles (pp. 280–281).
- A closed orbit is linearly stable iff all Floquet multipliers of the linearized Poincaré map have modulus below 1 (pp. 282–285).

## L3 — Walkthrough

### 8.4 Global bifurcations of cycles
In 2D there are four common ways to create or destroy limit cycles. Hopf is the most famous. The other three are global bifurcations (p. 264).

**Saddle-node bifurcation of cycles (fold of cycles).** Two limit cycles coalesce and annihilate (p. 264). Example, from Section 8.2:
$$\dot r=\mu r+r^3-r^5,\qquad \dot\theta=\omega+br^2 .$$
The radial equation is a 1D system with a saddle-node of fixed points at $\mu_c=-1/4$ (the author says "as you should check"). These fixed points are circular cycles (p. 264, Fig. 8.4.1).
- At $\mu_c$ a half-stable cycle appears.
- For $0>\mu>\mu_c$ it splits into a stable and an unstable cycle.
- The origin stays stable throughout (p. 265).
- The cycle is born with $O(1)$ amplitude, unlike Hopf, where amplitude is proportional to $(\mu-\mu_c)^{1/2}$ (p. 265).

**Infinite-period bifurcation.** System, with $\mu\ge 0$ (p. 265):
$$\dot r=r(1-r^2),\qquad \dot\theta=\mu-\sin\theta .$$
- Radially, all trajectories except $r^*=0$ approach the unit circle.
- Angularly, motion is counterclockwise everywhere if $\mu>1$. For $\mu<1$ there are two invariant rays with $\sin\theta=\mu$.
- As $\mu\to1^+$ a bottleneck at $\theta=\pi/2$ lengthens the period. At $\mu_c=1$ a fixed point appears on the circle and the period is infinite. For $\mu<1$ it splits into a saddle and a node.
- Amplitude stays $O(1)$. The period grows like $(\mu-\mu_c)^{-1/2}$ (Section 4.3) (p. 265).

**Homoclinic (saddle-loop) bifurcation.** Part of a limit cycle approaches a saddle. At the bifurcation the cycle touches it and becomes a homoclinic orbit (a trajectory leaving a saddle and returning to it). No transparent analytic example exists, so the author uses a computer (p. 266):
$$\dot x=y,\qquad \dot y=\mu y+x-x^2+xy .$$
- The bifurcation occurs numerically at $\mu_c\approx-0.8645$.
- For $\mu<\mu_c$ (e.g. $-0.92$) a stable cycle passes close to the saddle at the origin. As $\mu$ rises it swells and hits the saddle, forming a homoclinic orbit. For $\mu>\mu_c$ the connection breaks and the loop is destroyed (p. 266, Fig. 8.4.3).
- The key is the branch of the saddle's unstable manifold leaving to the northeast. After looping it hits the origin (at $\mu_c$) or veers off to one side (p. 266–267).

**Scaling laws (Table 8.4.1, generic, $\mu\ll1$; the page text calls it "Table 7.4.1").** The homoclinic entry is as printed.

| Bifurcation | Amplitude of stable cycle | Period |
|---|---|---|
| Supercritical Hopf | $O(\mu^{1/2})$ | $O(1)$ |
| Saddle-node of cycles | $O(1)$ | $O(1)$ |
| Infinite-period | $O(1)$ | $O(\mu^{-1/2})$ |
| Homoclinic | $O(1)$ | $O(\ln\mu)$ |

All but the homoclinic law were explained earlier. The homoclinic period law comes from estimating the passage time near a saddle (Exercise 8.4.12, Gaspard 1990) (p. 267). Exceptions occur only if the problem is nongeneric (symmetry or other special feature) (p. 267).

**Example 8.4.1 (van der Pol).** For $\ddot x+\varepsilon\dot x(x^2-1)+x=0$ the eigenvalues at the origin are $\pm i$ at $\varepsilon=0$, suggesting Hopf. But for $0<\varepsilon\ll1$ the cycle has amplitude $r\approx2$, not $O(\varepsilon^{1/2})$ (p. 267).
- Explanation: the bifurcation is degenerate. The nonlinear term $\varepsilon\dot x x^2$ vanishes at the same parameter value where the eigenvalues cross the imaginary axis (p. 267).
- Rewrite as $\ddot x+x+\varepsilon x^2\dot x-\varepsilon\dot x=0$. Let $u^2=\varepsilon x^2$, so $u=\varepsilon^{1/2}x$:
$$\ddot u+u+u^2\dot u-\varepsilon\dot u=0 .$$
- Now the nonlinear term survives. From $x\approx2\cos t$, $u\approx2\varepsilon^{1/2}\cos t$, so amplitude grows like $\varepsilon^{1/2}$, as Hopf predicts (p. 268).

**Higher dimensions and why it matters.** The same scaling laws hold, with two caveats: more bifurcations of cycles become possible, and the homoclinic bifurcation is subtler and often creates chaos afterwards (p. 268). Experimentally, if an oscillation stops when a control parameter changes, the scaling of period and amplitude can support or eliminate candidate models (p. 268).

*Intuition note.* Each way of losing a cycle leaves a fingerprint: small growing amplitude (Hopf), a sudden finite jump (fold), or a diverging period (infinite-period or homoclinic). Measuring amplitude and period near the transition can tell you something about which mechanism is at work, even when the equations are not precisely known, so candidate models can be supported or eliminated (p. 268).

### 8.5 Hysteresis in the driven pendulum and Josephson junction
**Governing equations.** The junction obeys (p. 269)
$$\frac{\hbar C}{2e}\ddot\phi+\frac{\hbar}{2eR}\dot\phi+I_c\sin\phi=I_B .\tag{1}$$
Rescaling
$$\tilde t=\Big(\frac{2eI_c}{\hbar C}\Big)^{1/2}t,\quad I=\frac{I_B}{I_c},\quad \alpha=\Big(\frac{\hbar}{2eI_cR^2C}\Big)^{1/2}\tag{2}$$
gives, with primes meaning $d/d\tilde t$ (p. 269),
$$\phi''+\alpha\phi'+\sin\phi=I .\tag{3}$$
Here $\alpha>0$, and $I\ge0$ without loss of generality. With $y=\phi'$:
$$\phi'=y,\qquad y'=I-\sin\phi-\alpha y .\tag{4}$$
The phase space is a cylinder: $\phi$ is an angle and $y$ is real (p. 269).

**Fixed points.** They satisfy $y^*=0$ and $\sin\phi^*=I$. There are two on the cylinder if $I<1$ and none if $I>1$. The Jacobian is
$$A=\begin{pmatrix}0&1\\-\cos\phi^*&-\alpha\end{pmatrix},$$
with $\tau=-\alpha<0$ and $\Delta=\cos\phi^*=\pm\sqrt{1-I^2}$. One fixed point is a saddle and the other a sink (p. 269–270).
- For $\Delta>0$ the sink is a stable node if $\tau^2-4\Delta=\alpha^2-4\sqrt{1-I^2}>0$, otherwise a stable spiral.
- At $I=1$ node and saddle merge in a saddle-node of fixed points (p. 270).

**Existence of a closed orbit ($I>1$).** The author claims all trajectories are attracted to a unique stable limit cycle (p. 270).
1. The nullcline is $y=\alpha^{-1}(I-\sin\phi)$. Flow is downward above it and upward below it.
2. All trajectories eventually enter and stay in a strip $y_1\le y\le y_2$, for any $0<y_1<(I-1)/\alpha$ and $y_2>(I+1)/\alpha$. In the strip $y>0$, so $\phi'>0$ (p. 270).
3. Since $\phi=0$ and $2\pi$ are equivalent, restrict to the box $0\le\phi\le2\pi$, $y_1\le y\le y_2$.
4. The Poincaré (first-return) map $P(y)$ gives the height at which a trajectory starting at height $y$ on $\phi=0$ first returns to that line (pp. 270–271).
5. A fixed point $P(y^*)=y^*$ gives a closed orbit (p. 271).
6. $P(y_1)>y_1$ (flow is upward on $y=y_1$, so the trajectory never returns to that line) and $P(y_2)<y_2$ (same argument).
7. $P$ is continuous (continuous dependence on initial conditions for smooth fields).
8. $P$ is monotonic (otherwise trajectories would cross).
9. By the intermediate value theorem the graph of $P$ crosses the 45° diagonal at some $y^*$ (p. 271, Fig. 8.5.4).

**Uniqueness.** The argument so far leaves open that $P(y)\equiv y$ on an interval (a band of closed orbits) (p. 272).
- On a cylinder there are two topologically different kinds of periodic orbit: librations and rotations. For $I>1$ librations are impossible: by index theory a libration must encircle a fixed point, and there are none. So only rotations remain.
- Suppose two rotations $y_U(\phi)>y_L(\phi)$ (they cannot cross). Let
$$E=\tfrac12y^2-\cos\phi .\tag{5}$$
- Around any rotation $\Delta E=0$:
$$0=\Delta E=\int_0^{2\pi}\frac{dE}{d\phi}\,d\phi .\tag{6}$$
- From (5):
$$\frac{dE}{d\phi}=y\frac{dy}{d\phi}+\sin\phi ,\tag{7}$$
- and from (4):
$$\frac{dy}{d\phi}=\frac{y'}{\phi'}=\frac{I-\sin\phi-\alpha y}{y}.\tag{8}$$
- Substituting (8) into (7) gives $dE/d\phi=I-\alpha y$. So (6) becomes $0=\int_0^{2\pi}(I-\alpha y)\,d\phi$, i.e. every rotation satisfies
$$\int_0^{2\pi}y(\phi)\,d\phi=\frac{2\pi I}{\alpha}.\tag{9}$$
- But $y_U>y_L$ gives $\int y_U>\int y_L$, so (9) cannot hold for both. The rotation is unique (p. 273).

*Intuition note.* The return map $P$ starts above the diagonal and ends below it, so it must cross. A crossing is a closed orbit. Energy bookkeeping then shows that over one lap the energy pumped in by the current exactly balances the damping loss, which pins the average height of a rotation to one value.

**Homoclinic bifurcation (decreasing $I$).** Physically, as torque falls the pendulum can no longer whirl at some $I_c<1$, and all solutions damp to rest (p. 273). The author reports that Exercise 8.5.2 (numerical phase portraits) shows that for sufficiently small $\alpha$ the cycle is destroyed in a homoclinic bifurcation (pp. 273–274).
- For $I_c<I<1$ the system is bistable: sink plus stable cycle. $U$, a branch of the saddle's unstable manifold, tends to the cycle as $t\to\infty$ (Fig. 8.5.7).
- As $I$ decreases, the cycle moves down and squeezes $U$ toward the saddle's stable manifold. At $I=I_c$ they merge and $U$ is a homoclinic orbit (Fig. 8.5.8).
- For $I<I_c$ the connection breaks and $U$ spirals into the sink (Fig. 8.5.9) (p. 274–275).

This scenario holds only for sufficiently small $\alpha$. For $\alpha\to\infty$ (overdamped, Section 4.6) the cycle dies by an infinite-period bifurcation. By plausibility, confirmed by numerical integration (Exercise 8.5.2), the same occurs for large finite $\alpha$ (p. 275).

**Stability diagram (Fig. 8.5.10).** In the $(\alpha,I)$ plane there are three bifurcation curves (p. 275):
- homoclinic (thick curve, small $\alpha$),
- infinite-period (large $\alpha$),
- saddle-node of fixed points (the line $I=1$).

Regions: stable limit cycle above, stable fixed point below, bistable in between. The argument is heuristic; rigorous proofs are in Levi et al. (1978). Melnikov's method shows the homoclinic curve is tangent to $I=4\alpha/\pi$ as $\alpha\to0$, and the approximation works well even for moderate $\alpha$ because the curve is nearly straight (p. 275).

**Hysteretic I–V curve.** Take small $\alpha$ and start below the homoclinic curve, at the zero-voltage fixed point (pp. 275–276).
- Raise $I$. At $I>1$ the fixed point vanishes in a saddle-node and the junction jumps to the limit cycle (nonzero voltage).
- Lower $I$. The cycle persists below $I=1$, with frequency tending to zero like $[\ln(I-I_c)]^{-1}$ (Section 8.4 scaling).
- The dc voltage is proportional to frequency (Section 4.6), so it returns to zero continuously as $I\to I_c^+$ (Fig. 8.5.11).
- In practice the return looks like a jump, because $[\ln(I-I_c)]^{-1}$ has infinite derivatives of all orders at $I_c$ (Exercise 8.5.1). Sullivan and Zimmerman (1971) saw a jump to zero rotation rate in pendulum experiments (p. 276).

*Intuition note.* Hysteresis comes from bistability: up-sweep and down-sweep end at different states because the fixed point and cycle coexist between $I_c$ and 1. The return to zero is technically continuous but so steep (infinite derivatives of all orders at $I_c$) that it cannot be resolved.

### 8.6 Coupled oscillators and quasiperiodicity
The torus is the natural phase space for $\dot\theta_1=f_1(\theta_1,\theta_2)$, $\dot\theta_2=f_2(\theta_1,\theta_2)$ with $f_i$ periodic in both arguments (p. 276). Model of coupled oscillators:
$$\dot\theta_1=\omega_1+K_1\sin(\theta_2-\theta_1),\qquad \dot\theta_2=\omega_2+K_2\sin(\theta_1-\theta_2)\tag{1}$$
with phases $\theta_i$, natural frequencies $\omega_i>0$, coupling constants $K_i\ge0$. Used to model human circadian rhythms and the sleep-wake cycle (p. 277). Picture: two jogging friends who want to run together and compromise their speeds. If their preferred speeds are too different, phase-locking is impossible (p. 277). Phase portraits are drawn on a square with periodic boundary conditions (pp. 277–278).

**Uncoupled ($K_1=K_2=0$).** Trajectories are straight lines of slope $d\theta_2/d\theta_1=\omega_2/\omega_1$ (p. 278).
- *Rational* $\omega_1/\omega_2=p/q$ (no common factors): all trajectories are closed, since $\theta_1$ makes $p$ revolutions while $\theta_2$ makes $q$. Example $p=3,q=2$ is a trefoil knot on the torus. In general, for $p,q\ge2$ without common factors, the curves are $p{:}q$ torus knots (pp. 278–279).
- *Irrational* slope: the flow is **quasiperiodic**. Trajectories never close, because a closed one makes integer numbers of revolutions in both angles, forcing a rational slope. Each trajectory is dense on the torus: it comes arbitrarily close to every point without passing through every point (Exercise 8.6.3). Quasiperiodicity is a new long-term behaviour that occurs only on the torus (p. 279).

**Coupled ($K_1,K_2>0$).** The phase difference $\phi=\theta_1-\theta_2$ obeys the nonuniform oscillator of Section 4.3 (p. 280):
$$\dot\phi=\dot\theta_1-\dot\theta_2=\omega_1-\omega_2-(K_1+K_2)\sin\phi .\tag{2}$$
- Two fixed points exist if $|\omega_1-\omega_2|<K_1+K_2$, none if $>$. A saddle-node occurs at equality.
- With two fixed points, $\sin\phi^*=(\omega_1-\omega_2)/(K_1+K_2)$. All trajectories of (2) approach the stable one. So on the torus the flow approaches a periodic phase-locked solution with constant phase difference $\phi^*$.
- Its common frequency is $\omega^*=\dot\theta_1=\dot\theta_2=\omega_2+K_2\sin\phi^*$. Substituting for $\sin\phi^*$ gives
$$\omega^*=\frac{K_1\omega_2+K_2\omega_1}{K_1+K_2}.$$
- This compromise frequency lies between $\omega_2$ and $\omega_1$. It is not generally halfway; frequency shifts are proportional to coupling strengths:
$$\Big|\frac{\Delta\omega_1}{\Delta\omega_2}\Big|\equiv\Big|\frac{\omega_1-\omega^*}{\omega_2-\omega^*}\Big|=\Big|\frac{K_1}{K_2}\Big|\quad(\text{pp. 280–281}).$$
- On the torus the locked solutions are diagonal lines of slope 1 (Fig. 8.6.9). If the natural frequencies are pulled apart, stable and unstable locked solutions coalesce when $|\omega_1-\omega_2|=K_1+K_2$: a saddle-node of cycles. Afterwards the flow is quasiperiodic or rational as in the uncoupled case, but with curvy trajectories (p. 281).

### 8.7 Poincaré maps
Take an $n$-dimensional system $\dot{\mathbf x}=\mathbf f(\mathbf x)$ and a surface of section $S$ of dimension $n-1$, transverse to the flow (trajectories cross it, not parallel) (p. 281). The Poincaré map $P:S\to S$ follows trajectories from one intersection with $S$ to the next:
$$\mathbf x_{k+1}=P(\mathbf x_k).$$
A fixed point $\mathbf x^*=P(\mathbf x^*)$ is a closed orbit. Near it, the behaviour of $P$ gives the orbit's stability. Closed-orbit problems become fixed-point problems of a map, but a formula for $P$ is typically impossible (p. 282).

**Example 8.7.1.** For $\dot r=r(1-r^2)$, $\dot\theta=1$, with $S$ the positive $x$-axis, the time of flight is $2\pi$. So $r_1=P(r_0)$ satisfies
$$\int_{r_0}^{r_1}\frac{dr}{r(1-r^2)}=\int_0^{2\pi}dt=2\pi .$$
Evaluating the integral (Exercise 8.7.1):
$$P(r)=\big[1+e^{-4\pi}(r^{-2}-1)\big]^{-1/2}.$$
The cobweb construction (vertical line to the graph, horizontal line to the diagonal, repeat) shows that $r^*=1$ is the unique fixed point and is stable (pp. 282–283).

**Example 8.7.2.** The forced RC circuit $\dot x+x=A\sin\omega t$ becomes time-independent by setting $\theta=\omega t$: $\dot\theta=\omega$, $\dot x+x=A\sin\theta$, on a cylinder. Take $S=\{\theta=0 \bmod 2\pi\}$, with time of flight $2\pi/\omega$ (strobing once per drive cycle) (p. 283).
- The general solution is $x(t)=c_1e^{-t}+c_2\sin\omega t+c_3\cos\omega t$. Only $c_1$ depends on $x_0$, and $x_0=c_1+c_3$. So
$$P(x_0)=(x_0-c_3)e^{-2\pi/\omega}+c_3=x_0e^{-2\pi/\omega}+c_4,\qquad c_4=c_3(1-e^{-2\pi/\omega}).$$
- $P$ is a line of slope $e^{-2\pi/\omega}<1$. It meets the diagonal once, and the cobweb shrinks the deviation by a constant factor per step. The cycle is unique and globally stable (pp. 283–284).

**Linear stability of periodic orbits.** Let $\mathbf v_0$ be a small perturbation with $\mathbf x^*+\mathbf v_0\in S$. Then
$$\mathbf x^*+\mathbf v_1=P(\mathbf x^*+\mathbf v_0)=P(\mathbf x^*)+[DP(\mathbf x^*)]\mathbf v_0+O(\|\mathbf v_0\|^2),$$
where $DP(\mathbf x^*)$ is the $(n-1)\times(n-1)$ linearized Poincaré map. Since $\mathbf x^*=P(\mathbf x^*)$, dropping the $O$ terms gives $\mathbf v_1=[DP(\mathbf x^*)]\mathbf v_0$ (p. 284).
- **Criterion:** the closed orbit is linearly stable iff $|\lambda_j|<1$ for all $j=1,\dots,n-1$, where $\lambda_j$ are the eigenvalues of $DP(\mathbf x^*)$ (p. 284).
- Reason (generic case, no repeated eigenvalues): with eigenvectors $\mathbf e_j$ and $\mathbf v_0=\sum_{j=1}^{n-1}v_j\mathbf e_j$,
$$\mathbf v_1=DP(\mathbf x^*)\sum v_j\mathbf e_j=\sum v_j\lambda_j\mathbf e_j,\qquad \mathbf v_k=\sum v_j(\lambda_j)^k\mathbf e_j .$$
- If all $|\lambda_j|<1$, $\|\mathbf v_k\|\to0$ geometrically fast. If some $|\lambda_j|>1$, perturbations along $\mathbf e_j$ grow and $\mathbf x^*$ is unstable.
- If the largest has $|\lambda_m|=1$ (this occurs at bifurcations of periodic orbits) a nonlinear analysis is needed (p. 285).
- The $\lambda_j$ are the characteristic or Floquet multipliers. Strictly these are the nontrivial ones. There is always a trivial multiplier $\lambda\equiv1$ for perturbations along the orbit, which is just time translation. In general they require numerical integration (Exercise 8.7.10) (p. 285).

**Example 8.7.3.** For Example 8.7.1, put $r=1+\eta$. Then $\dot\eta=(1+\eta)(1-(1+\eta)^2)$, which gives $\dot\eta=-2\eta$ after dropping $O(\eta^2)$. So $\eta(t)=\eta_0e^{-2t}$, and after $t=2\pi$, $\eta_1=e^{-4\pi}\eta_0$. The multiplier is $e^{-4\pi}$, and $|e^{-4\pi}|<1$, so the cycle is linearly stable. The author says Exercise 8.7.1 asks you to show $P'(r^*)=e^{-4\pi}$ (p. 285).

**Example 8.7.4 (starts; unit ends mid-example).** The system
$$\dot\phi_i=\Omega+a\sin\phi_i+\tfrac1N\sum_{j=1}^N\sin\phi_j,\quad i=1,\dots,N\tag{1}$$
models a series array of overdamped Josephson junctions with a resistive load. The task is to find when the in-phase solution $\phi_1=\dots=\phi_N=\phi^*(t)$ is periodic and to find its multipliers (p. 286).
- In-phase: $d\phi^*/dt=\Omega+(a+1)\sin\phi^*$ (2). It is periodic iff $|\Omega|>|a+1|$.
- Perturb $\phi_i=\phi^*+\eta_i$ and drop quadratic terms:
$$\dot\eta_i=[a\cos\phi^*(t)]\eta_i+[\cos\phi^*(t)]\tfrac1N\sum_j\eta_j .\tag{3}$$
- Trick 1: set $\mu=\frac1N\sum\eta_j$ and $\xi_i=\eta_{i+1}-\eta_i$ ($i=1,\dots,N-1$). Then $\dot\xi_i=[a\cos\phi^*(t)]\xi_i$.
- Trick 2: use (2) to eliminate $dt$: $\dfrac{d\xi_i}{\xi_i}=\dfrac{[a\cos\phi^*]\,d\phi^*}{\Omega+(a+1)\sin\phi^*}$.
- The text breaks off at "Now we compute the change in the perturbations after one circuit around the closed orbit" (p. 286).

*Intuition note.* Stability of a cycle becomes the question "does one lap shrink perturbations?" The answer is the multiplier: below 1 in modulus means the orbit is stable. In Example 8.7.3 the multiplier $e^{-4\pi}$ is the radial decay rate $-2$ times the lap time $2\pi$, exponentiated.

## Toy example (ours, not from the text)
Take $\dot r=r(1-r)$, $\dot\theta=1$, with $S$ the positive $x$-axis, so the flight time is $2\pi$.
- The logistic solution is $r(t)=1/\big(1+(1/r_0-1)e^{-t}\big)$. With $c=e^{-2\pi}\approx0.001867$,
$$P(r_0)=\frac{1}{1+(1/r_0-1)c}.$$
- Fixed point: $r_0=1$ gives $P=1/(1+0)=1$. So the circle $r=1$ is a closed orbit.
- Cobweb from $r_0=0.5$: $1/r_0-1=1$, so $r_1=1/(1+0.001867)\approx0.99814$. It is already almost at 1.
- Multiplier: $P'(r_0)=\dfrac{c/r_0^2}{(1+(1/r_0-1)c)^2}$, which at $r_0=1$ is $c=e^{-2\pi}$. Check by linearizing: $r=1+\eta$, $\dot\eta\approx-\eta$, so after $2\pi$ the factor is $e^{-2\pi}$. ✓.
- Since $0.001867<1$, the cycle is stable, matching the method of Example 8.7.3.

## Concepts
- [[bifurcation]] — qualitative change of dynamics at a parameter value; here, the creation or destruction of cycles (p. 264)
- [[saddle-node-bifurcation]] — two fixed points (here also two cycles) merge and vanish; cycles are born with O(1) amplitude (pp. 264–265)
- [[global-bifurcation-of-cycles]] (new) — bifurcation of a limit cycle involving a large region of the phase plane, not one fixed point's neighbourhood (p. 264)
- [[infinite-period-bifurcation]] (new) — cycle develops a bottleneck; a fixed point appears on it, and the period diverges like (μ−μ_c)^(−1/2) (p. 265)
- [[homoclinic-bifurcation]] (new) — a cycle hits a saddle and becomes a homoclinic orbit; period scales as O(ln μ) (pp. 266–267)
- [[bifurcation-scaling-laws]] (new) — generic amplitude/period scaling of each cycle bifurcation, usable to identify mechanisms (p. 267)
- [[nongeneric-degenerate-bifurcation]] (new) — special case where an expected scaling law fails; here the van der Pol at ε=0 (p. 267)
- [[hysteresis]] — the path back differs from the path forward; here from coexisting stable fixed point and limit cycle (p. 268)
- [[limit-cycle]] — isolated closed orbit; here existence proved with a Poincaré map (p. 270)
- [[poincare-map]] (new) — first-return map on a transverse surface of section; its fixed points are closed orbits (pp. 270, 281–282)
- [[floquet-multiplier]] (new) — eigenvalue of the linearized Poincaré map; |λ|<1 for all gives stability (p. 285)
- [[quasiperiodicity]] (new) — flow on a torus with irrational frequency ratio; dense, never-closing orbits (p. 279)
- [[synchronization]] — coupled oscillators lock at a compromise frequency when |ω₁−ω₂|<K₁+K₂ (pp. 280–281)
- [[linear-stability-analysis]] — stability of the closed orbit from the linearized return map (p. 284)

## Canonical instances
- [[driven-pendulum-josephson-junction]] — bistability, homoclinic and infinite-period bifurcations, hysteretic I–V curve (pp. 269–276)
- [[van-der-pol-oscillator]] — degenerate Hopf; rescaling restores the ε^(1/2) amplitude law (pp. 267–268)
- [[coupled-oscillators-on-a-torus]] — two jogging friends; phase locking, torus knots, quasiperiodic flow (pp. 277–281)
- [[forced-rc-circuit]] — Poincaré map is a line of slope below 1, so a unique globally stable cycle (pp. 283–284)
- [[josephson-junction-array]] — in-phase solution of N junctions, multipliers by decoupling (p. 286, incomplete)

## Bridges (candidates)
- [structural-analogy] infinite-period bottleneck, period ~ (μ−μ_c)^(−1/2) ↔ complex-systems: critical slowing down near a tipping point — both show slowing as a threshold nears.
- [structural-analogy] saddle-node jump and slow return in the I–V curve ↔ complex-systems: tipping point with hysteresis — different forward and backward thresholds from bistability.
- [structural-analogy] two-oscillator phase locking with compromise frequency ω* ↔ complex-systems: Kuramoto synchronization — sine-coupled phases lock when coupling beats frequency spread.
- [metaphor] cobweb on the Poincaré map ↔ complex-systems: iterated discrete maps — repeated return behaves like a 1D map.

## Questions this raises
- Why does the homoclinic period scale as ln μ, and what is the exact meaning of "O(ln μ)" for μ ≪ 1 (Exercise 8.4.12)?
- In higher dimensions, how does a homoclinic bifurcation create chaos, as the author says it often does (p. 268)?
- What happens to the flow on the torus when the locked solution is lost and the frequency ratio varies?
- Can Floquet multipliers be computed for the N-junction in-phase solution, and when are they below 1 (Example 8.7.4)?

## Reading notes
- This part starts at Section 8.4 (printed p. 264) and ends at the start of the solution to Example 8.7.4 (printed p. 286, mid-example). Digest covers only what is on those pages.
- Page offset: printed = pdf − 15 for pdf 279–289. After pdf 289 (printed 274), four pages (pdf 290–293) have no extracted text and no printed number; pdf 294 is printed 275. So for pdf ≥ 294, printed = pdf − 19. No printed material appears to be missing, since 274 → 275 is continuous.
- The text refers to "Table 7.4.1" (twice, p. 267), while the table is captioned Table 8.4.1, so this is apparently a misprint. The van der Pol example cites Section 7.6 for the cycle amplitude $r\approx2$.
- The homoclinic period entry appears as O(ln μ) in the table; I kept it as printed. For μ ≪ 1, ln μ is negative.
- The unit refers to exercises (8.4.12, 8.5.1, 8.5.2, 8.6.3, 8.7.1, 8.7.10) but does not print them, so no exercise list is given.
- Several symbols (μ, θ, ω) were garbled in the text layer. I checked the equations against page images.
