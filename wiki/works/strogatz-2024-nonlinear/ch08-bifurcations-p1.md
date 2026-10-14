---
id: strogatz-2024-nonlinear/ch08-bifurcations-p1
work: strogatz-2024-nonlinear
unit: "8 Bifurcations Revisited (part 1/3): 8.0–8.3"
pages: 244–263
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Bifurcations Revisited, part 1: fixed-point bifurcations, Hopf bifurcations, a chemical oscillator

## L0 — One line
In two dimensions, fixed points still collide and vanish along one line (a zero eigenvalue), but a new route exists: a pair of complex eigenvalues crosses the imaginary axis (Hopf bifurcation), switching oscillations on or off.

## L1 — The gist (≤ 120 words)
Which new things can happen when a parameter changes in a two-dimensional flow? Saddle-node, transcritical and pitchfork bifurcations are the one-dimensional ones, now with an extra direction of simple attraction or repulsion. Hopf bifurcations are new: a stable spiral turns unstable and a limit cycle (an isolated closed orbit) appears or disappears. The supercritical case gives a small cycle growing like √(μ−μc); the subcritical case gives a sudden jump and hysteresis (large oscillations persist when the parameter is reversed). A genetic switch (saddle-node) and a chlorine dioxide–iodine–malonic acid oscillator (supercritical Hopf) show the theory at work. Hopf bifurcations describe how oscillations can start and stop, e.g. in chemistry and nerve cells.

**Prerequisites:** 1D bifurcations (Ch. 3); Jacobian, trace τ, determinant Δ, eigenvalues; nullclines; polar coordinates; trapping region and Poincaré–Bendixson (Ch. 7).

## L2 — Key ideas
- A bifurcation is a change in the topological structure of the phase portrait: the number or stability of fixed points, closed orbits or saddle connections (p. 244).
- Saddle-node, transcritical and pitchfork bifurcations in 2D are essentially 1D events: the action is on one line, and the other direction is simple attraction or repulsion (pp. 244, 248–249).
- All three are zero-eigenvalue bifurcations (Δ = 0, where Δ is the determinant of the Jacobian) and always involve a collision of fixed points (p. 251).
- Hopf bifurcation: a complex-conjugate eigenvalue pair crosses the imaginary axis. The supercritical type gives a limit cycle of size ∝ √(μ−μc) and frequency ≈ Im λ (pp. 251–254).
- The subcritical type is more dramatic. An unstable cycle shrinks onto the fixed point, trajectories jump to a distant attractor, and hysteresis results (p. 255).
- Linearization cannot tell sub- from supercritical. In one example, reasoning plus numerics could decide; computer experiments are not proofs, and a degenerate case (a nonlinear center, i.e. a fixed point surrounded by closed orbits) must be excluded (pp. 256–257).
- Chemical oscillators can be modelled in 2D. The ClO₂–I₂–MA model has a trapping region (a region trajectories cannot leave), a repelling fixed point for b < bc, and a supercritical Hopf locus b = 3a/5 − 25/a (pp. 259–263).

## L3 — Walkthrough

### 8.0 Introduction (p. 244)
In 2D, closed orbits as well as fixed points can be created, destroyed or destabilized. A bifurcation occurs when the phase portrait changes topological structure (topological equivalence, Sec. 6.3). Each bifurcation is introduced by a prototype, then harder examples.

### 8.1 Saddle-node, transcritical, pitchfork (pp. 244–251)

**Saddle-node prototype (p. 245).**
$$\dot x=\mu-x^2,\qquad \dot y=-y \tag{1}$$
For μ > 0 there is a stable node at $(\sqrt\mu,0)$ and a saddle at $(-\sqrt\mu,0)$. They collide at μ = 0 and vanish for μ < 0. After they vanish they leave a *ghost*, a bottleneck that delays trajectories. The delay time generically scales as $(\mu-\mu_c)^{-1/2}$ (p. 245).

**Nullcline picture (pp. 245–246).** In $\dot x=f,\ \dot y=g$, fixed points are nullcline intersections. If the nullclines become tangent at μc and then pull apart, the fixed points collide and disappear. The author says all saddle-node bifurcations have this character locally.

**Example 8.1.1 (Griffith's genetic switch, pp. 246–248).**
$$\dot x=-ax+y,\qquad \dot y=\frac{x^2}{1+x^2}-by,\quad a,b>0.$$
Here x is protein concentration and y is mRNA concentration; the gene is induced by two copies of its own protein.
- Nullclines: $y=ax$ and $y=x^2/[b(1+x^2)]$. The origin is a fixed point. The others satisfy
$$ab(1+x^2)=x \tag{2}$$
$$x^*=\frac{1\pm\sqrt{1-4a^2b^2}}{2ab}\quad\text{if }2ab<1.$$
- They coalesce at 2ab = 1, so $a_c=1/2b$, with $x^*=1$ there. Three fixed points exist for $a<a_c$ (p. 247).
- Jacobian: $A=\begin{pmatrix}-a&1\\ 2x/(1+x^2)^2&-b\end{pmatrix}$. Trace $\tau=-(a+b)<0$, so fixed points are sinks or saddles (p. 248).
- Origin: Δ = ab > 0 and τ² − 4Δ = (a−b)² > 0, so a stable node (the degenerate case a = b is ignored).
- Other points: use (2), i.e. $ab=x/(1+x^2)$. Then
$$\Delta=ab-\frac{2x^*}{(1+x^{*2})^2}=ab\Big[1-\frac{2}{1+x^{*2}}\Big]=ab\,\frac{x^{*2}-1}{1+x^{*2}}.$$
- So Δ < 0 for the middle point (0 < x* < 1): a saddle. For x* > 1, Δ < ab, hence τ² − 4Δ > (a−b)² > 0: a stable node.
- The saddle's stable manifold separates the two basins. The unstable manifold is trapped between the nullclines (p. 248).
- Biology: the system can act as a biochemical switch only if the decay rates satisfy ab < 1/2. The two stable states are gene silent (origin) and gene active (x, y large). The stable manifold acts as a threshold (p. 248).

Trajectories relax quickly onto the saddle's unstable manifold, which plays the role of the x-axis in Fig. 8.1.1. The fixed points slide together "like beads on a string" (p. 249). This is why 1D bifurcations are building blocks; center manifold theory justifies it rigorously (p. 249).

*Intuition note:* In 2D the fixed points still approach and annihilate along one curve. The rest of the plane just funnels trajectories toward that curve. So, in many respects, the 1D theory describes what happens.

**Transcritical and pitchfork prototypes (p. 249).** Each uses ẏ = −y:
- $\dot x=\mu x-x^2$ (transcritical)
- $\dot x=\mu x-x^3$ (supercritical pitchfork)
- $\dot x=\mu x+x^3$ (subcritical pitchfork)

**Example 8.1.2 (p. 249).** Supercritical pitchfork. For μ < 0 the origin is the only fixed point, a stable node. At μ = 0 it is still stable but decays only algebraically along x (critical slowing down). For μ > 0 the origin is a saddle and there are stable nodes at $(\pm\sqrt\mu,0)$.

**Example 8.1.3 (symmetry, pp. 250–251).**
$$\dot x=\mu x+y+\sin x,\qquad \dot y=x-y.$$
- The system is invariant under (x, y) → (−x, −y). The origin is a fixed point for all μ.
- Jacobian: $A=\begin{pmatrix}\mu+1&1\\1&-1\end{pmatrix}$, with τ = μ and Δ = −(μ+2). The origin is stable for μ < −2 and a saddle for μ > −2, suggesting μc = −2.
- Other fixed points have y = x, so $(\mu+1)x+\sin x=0$. Expanding, $(\mu+1)x+x-\frac{x^3}{3!}+O(x^5)=0$. Dividing by x: $\mu+2-x^2/6\approx0$, so $x^*\approx\pm\sqrt{6(\mu+2)}$ for μ slightly above −2.
- The pair exists after the origin becomes a saddle, so the bifurcation is supercritical (a subcritical one would have the pair while the origin is stable). The new points are therefore stable.
- At μc, $A\approx\begin{pmatrix}-1&1\\1&-1\end{pmatrix}$ with eigenvectors (1,1) for λ = 0 and (1,−1) for λ = −2. For μ slightly above −2 the zero eigenvalue becomes slightly positive. This gives Fig. 8.1.7, valid only locally in μ and in phase space.

**Zero-eigenvalue bifurcations (p. 251).** In all these examples Δ = 0, i.e. an eigenvalue is zero. Saddle-node, transcritical and pitchfork are zero-eigenvalue bifurcations (not the only ones, but the most common). They always involve a collision of two or more fixed points.

### 8.2 Hopf bifurcations (pp. 251–257)
**Setting (pp. 251–252).** A stable fixed point has both eigenvalues in Re λ < 0. They are either real negative or complex conjugate (Fig. 8.2.1). To destabilize it, an eigenvalue must cross into the right half-plane. A real one crossing zero gives Sec. 8.1. A complex pair crossing the imaginary axis together is the new case.

**Supercritical Hopf (pp. 252–254).** Damped oscillations ("ringing") decay more slowly as μ → μc and turn to growth. In many cases the result is a small sinusoidal limit cycle (an isolated closed orbit) around the old steady state. In phase space: a stable spiral becomes an unstable spiral surrounded by a small, nearly elliptical limit cycle. This works in any dimension n ≥ 2; the text treats 2D.

Prototype:
$$\dot r=\mu r-r^3,\qquad \dot\theta=\omega+br^2.$$
- μ controls stability, ω is the frequency of infinitesimal oscillations, and b sets how frequency depends on amplitude (p. 253).
- μ < 0: stable spiral. μ = 0: still a stable spiral, only algebraically weak; linearization wrongly predicts a center. μ > 0: unstable spiral plus a stable circular cycle at $r=\sqrt\mu$.
- Cartesian form (x = r cos θ, y = r sin θ):
$$\dot x=\dot r\cos\theta-r\dot\theta\sin\theta=(\mu r-r^3)\cos\theta-r(\omega+br^2)\sin\theta$$
$$=\big(\mu-[x^2+y^2]\big)x-\big(\omega+b[x^2+y^2]\big)y=\mu x-\omega y+\text{cubic terms},$$
and similarly $\dot y=\omega x+\mu y+\text{cubic terms}$.
- So $A=\begin{pmatrix}\mu&-\omega\\ \omega&\mu\end{pmatrix}$ and $\lambda=\mu\pm i\omega$ (p. 254). The eigenvalues cross the imaginary axis left to right as μ increases through 0.

**Rules of thumb (generic for supercritical Hopf, p. 254).**
1. The limit cycle grows continuously from zero, with size ∝ $\sqrt{\mu-\mu_c}$ for μ near μc.
2. Frequency ω ≈ Im λ at μ = μc: exact at birth, correct within O(μ−μc) nearby. So $T=2\pi/\mathrm{Im}\,\lambda+O(\mu-\mu_c)$.

Artifacts of the prototype (p. 254): real cycles are elliptical and distort as μ moves away. Also Im λ is exactly constant in the example, whereas normally the eigenvalues follow curved paths and cross with nonzero slope (Fig. 8.2.4).

*Intuition note:* A Hopf bifurcation starts oscillations from nothing: amplitude grows slowly (as a square root) while the rhythm is already set by the imaginary part of the eigenvalue. Measuring Im λ at the threshold predicts the period approximately.

**Subcritical Hopf (p. 255).** The subcritical case is always much more dramatic and potentially dangerous in engineering. Trajectories must jump to a distant attractor, which may be a fixed point, another limit cycle, infinity, or (in 3D and higher) a chaotic attractor (Lorenz, Ch. 9). Prototype:
$$\dot r=\mu r+r^3-r^5,\qquad \dot\theta=\omega+br^2.$$
- The cubic term is now destabilizing.
- For μ < 0 there are two attractors: a stable fixed point at the origin and a stable large limit cycle. An unstable cycle lies between them.
- As μ increases, the unstable cycle tightens like a noose around the origin. At μ = 0 it shrinks to zero amplitude and engulfs the origin, which becomes unstable. For μ > 0 the large cycle is the only attractor.
- Hysteresis: large oscillations cannot be switched off by returning μ to 0. They persist until μ = −1/4, where the stable and unstable cycles collide and annihilate (a bifurcation of Sec. 8.4, not covered here).
- Occurrence: nerve cells, aeroelastic flutter, instabilities of fluid flows (p. 256).

**Which type? (p. 256).** Linearization cannot tell: in both cases a pair of eigenvalues moves from the left to the right half-plane. An analytical criterion exists but can be hard to use. A "quick and dirty" test is computer experiment:
- If a small attracting cycle appears right after the fixed point goes unstable, and its amplitude shrinks to zero when μ is reversed, it is supercritical.
- Otherwise it is probably subcritical, and hysteresis is possible.
- Computer experiments are not proofs.

**Degenerate Hopf (p. 256).** The damped pendulum $\ddot x+\mu\dot x+\sin x=0$ (equation reconstructed, see Reading notes) changes the origin from stable to unstable spiral as μ passes through 0. At μ = 0 there is a band of closed orbits, which are not limit cycles (a limit cycle is isolated). This typically arises when a nonconservative system suddenly becomes conservative: the fixed point becomes a nonlinear center, not a weak spiral.

**Example 8.2.1 (pp. 256–257).** The system is $\dot x=\mu x-y+xy^2,\ \dot y=x+\mu y+y^3$ (sign of $y^3$ reconstructed, see Reading notes).
- $A=\begin{pmatrix}\mu&-1\\1&\mu\end{pmatrix}$, τ = 2μ, Δ = μ² + 1 > 0, λ = μ ± i. The origin goes from stable to unstable spiral as μ increases through 0, suggesting a Hopf bifurcation.
- In polar coordinates $\dot r=\mu r+ry^2$ (to be checked by the reader). So $\dot r\ge\mu r$. For μ > 0, r(t) grows at least as fast as $r_0e^{\mu t}$ and all trajectories are repelled to infinity. No closed orbits exist for μ > 0, so it cannot be supercritical.
- Degenerate would need a nonlinear center at μ = 0, but $\dot r$ is strictly positive away from the x-axis, so closed orbits are impossible.
- By elimination, it is subcritical. Fig. 8.2.6 (μ = −0.2) shows an unstable limit cycle around the stable fixed point.

### 8.3 Oscillating chemical reactions (pp. 257–263)

**Belousov's story (p. 258–259).** In the early 1950s Belousov mixed citric acid, bromate ions, sulfuric acid and a cerium catalyst. The mixture oscillated between yellow and colorless dozens of times over about an hour. He could not publish, because it was thought thermodynamics forces monotonic approach to equilibrium. A brief abstract appeared in 1959. Zhabotinsky confirmed the effect and presented it in Prague in 1968; it became the BZ reaction. Later work found propagating waves (rings and spirals) in unstirred layers, similar to waves in neural or cardiac tissue; spiral and scroll waves are implicated in some cardiac arrhythmias. Belousov and Zhabotinsky received the Lenin Prize in 1980, ten years after Belousov's death.

**Model of the ClO₂–I₂–MA reaction (p. 259–260).** Lengyel et al. (1990) give three reactions with empirical rate laws (p. 259):
$$\mathrm{MA}+\mathrm{I_2}\to\mathrm{IMA}+\mathrm{I^-}+\mathrm{H^+};\quad \frac{d[\mathrm{I_2}]}{dt}=-\frac{k_{1a}[\mathrm{MA}][\mathrm{I_2}]}{k_{1b}+[\mathrm{I_2}]}\tag{1}$$
$$\mathrm{ClO_2}+\mathrm{I^-}\to\mathrm{ClO_2^-}+\tfrac12\mathrm{I_2};\quad \frac{d[\mathrm{ClO_2}]}{dt}=-k_2[\mathrm{ClO_2}][\mathrm{I^-}]\tag{2}$$
$$\mathrm{ClO_2^-}+4\mathrm{I^-}+4\mathrm{H^+}\to\mathrm{Cl^-}+2\mathrm{I_2}+2\mathrm{H_2O};\quad \frac{d[\mathrm{ClO_2^-}]}{dt}=-k_{3a}[\mathrm{ClO_2^-}][\mathrm{I^-}][\mathrm{H^+}]-k_{3b}[\mathrm{ClO_2^-}][\mathrm{I_2}]\frac{[\mathrm{I^-}]}{u+[\mathrm{I^-}]^2}\tag{3}$$ Simulations show MA, I₂ and ClO₂ vary much more slowly than the intermediates I⁻ and ClO₂⁻. Treating the slow ones as constants and making other reasonable simplifications (the constant approximation cannot capture the final approach to equilibrium) gives, after nondimensionalization, with x, y the dimensionless concentrations of I⁻ and ClO₂⁻ and a, b > 0:
$$\dot x=a-x-\frac{4xy}{1+x^2}\tag{4}$$
$$\dot y=bx\Big(1-\frac{y}{1+x^2}\Big)\tag{5}$$

**Example 8.3.1: a closed orbit exists (pp. 260–261).**
- Nullclines: ẋ = 0 on $y=\dfrac{(a-x)(1+x^2)}{4x}$ (6); ẏ = 0 on the y-axis and on the parabola y = 1 + x².
- A box whose boundary vectors all point inward is a trapping region (Fig. 8.3.2). It contains the fixed point $x^*=a/5,\ y^*=1+(a/5)^2$, so Poincaré–Bendixson cannot be applied directly. If the fixed point is a repeller, apply it to the punctured box.
- Jacobian: $\dfrac{1}{1+x^{*2}}\begin{pmatrix}3x^{*2}-5&-4x^*\\2bx^{*2}&-bx^*\end{pmatrix}$, using y* = 1 + x*².
- $\Delta=\dfrac{5bx^*}{1+x^{*2}}>0$ and $\tau=\dfrac{3x^{*2}-5-bx^*}{1+x^{*2}}$. Since Δ > 0, the point is never a saddle, so it is a repeller if τ > 0.
- τ > 0 iff $b<3x^*-5/x^*$ (added step), i.e.
$$b<b_c\equiv\frac{3a}{5}-\frac{25}{a}\tag{7}$$
When (7) holds, a closed orbit exists somewhere in the punctured box.

**Example 8.3.2: type of bifurcation (p. 262).** As b decreases through bc, the fixed point goes from stable to unstable spiral. For a = 10, bc = 3.5. Numerically, b = 4 gives all trajectories spiralling into the fixed point; b = 2 gives a stable limit cycle (Fig. 8.3.3). So the bifurcation is supercritical. Plotting portraits as b → bc from below would confirm the cycle shrinks continuously to a point. The Hopf locus is b = 3a/5 − 25/a, separating "stable fixed point" from "stable limit cycle" (Fig. 8.3.4).

**Example 8.3.3: period (p. 263).** At bc, τ = 0 and Δ > 0, so $\lambda=\pm i\sqrt\Delta$. Substituting bc and x* = a/5:
$$\Delta=\frac{5b_cx^*}{1+x^{*2}}=\frac{5\left(\frac{3a}{5}-\frac{25}{a}\right)\frac a5}{1+(a/5)^2}=\frac{15a^2-625}{a^2+25}.$$
So $\omega\approx\Delta^{1/2}$ and $T=2\pi/\omega=2\pi\big[(a^2+25)/(15a^2-625)\big]^{1/2}$. As a → ∞, $T\to2\pi/\sqrt{15}$, printed as ≈ 1.63 (Fig. 8.3.5).

## Toy example (ours)
Take the supercritical prototype with ω = 2, b = 0: ṙ = μr − r³, θ̇ = 2.
- Cycle radius: ṙ = 0 gives r* = √μ. Then μ = 0.09 gives r* = 0.3, and μ = 0.36 gives r* = 0.6. Multiplying μ by 4 doubles the amplitude (rule 1).
- Stability: d(ṙ)/dr = μ − 3r² = μ − 3μ = −2μ < 0 at r*, so the cycle is stable (e.g. −0.18 for μ = 0.09).
- Eigenvalues at the origin: λ = μ ± 2i, i.e. 0.09 ± 2i and 0.36 ± 2i. Real parts are positive, so the origin is an unstable spiral.
- Period: T = 2π/2 = π ≈ 3.14 for both μ, as rule 2 says (exact here since b = 0).

## Concepts
- [[bifurcation]] — change of topological structure of the phase portrait as a parameter varies (p. 244)
- [[saddle-node-bifurcation]] — two fixed points collide and vanish; in 2D the action lies on the unstable manifold of the saddle (pp. 245, 248)
- [[zero-eigenvalue-bifurcation]] (new) — bifurcation with Δ = 0 / a zero eigenvalue; includes saddle-node, transcritical, pitchfork (p. 251)
- [[hopf-bifurcation]] (new) — complex-conjugate eigenvalue pair crosses the imaginary axis; a cycle is born or dies (p. 251)
- [[limit-cycle]] — isolated closed orbit; the cycle is born at a Hopf bifurcation (pp. 252, 256)
- [[hysteresis]] — in the subcritical Hopf, large oscillations persist after μ returns to 0 (p. 255)
- [[critical-slowing-down]] — algebraic instead of exponential decay at μ = 0 (p. 249)
- [[linear-stability-analysis]] — classify fixed points by trace and determinant of the Jacobian (pp. 247–248)
- [[attractor-basin]] — the saddle's stable manifold separates the basins of two sinks (p. 248)
- [[nullcline]] (new) — curve where ẋ = 0 or ẏ = 0; intersections are fixed points (p. 245)
- [[trapping-region]] (new) — region whose boundary vectors point inward; with a repelling fixed point it gives a closed orbit (p. 261)
- [[ghost-bottleneck]] (new) — slow passage after a saddle-node; delay ∝ (μ−μc)^(−1/2) (p. 245)

## Canonical instances
- [[griffith-genetic-switch]] — gene activated by its own protein; bistability if ab < 1/2 (pp. 246, 248)
- [[bz-reaction]] — Belousov–Zhabotinsky chemical oscillation and its history (p. 258)
- [[clo2-i2-ma-oscillator]] — two-variable model with supercritical Hopf locus b = 3a/5 − 25/a (pp. 259–262)
- [[damped-pendulum-degenerate-hopf]] — μ = 0 gives a band of closed orbits, not limit cycles (p. 256)

## Bridges (candidates)
- [structural-analogy] Hopf bifurcation ↔ complex-systems: onset of self-sustained oscillation as a control parameter passes a threshold
- [same-math] Saddle-node ghost bottleneck (time ∝ (μ−μc)^(−1/2)) ↔ complex-systems: tipping points and critical slowing down (same 1D normal form)
- [structural-analogy] Subcritical Hopf jump and hysteresis ↔ complex-systems: tipping points with irreversible switching
- [metaphor] Genetic switch with a saddle's stable manifold as threshold ↔ complex-systems: threshold models of cascades

## Questions this raises
- Which analytical criterion decides sub- versus supercritical Hopf, and why is it hard to use (p. 256)?
- What bifurcation destroys the large cycle at μ = −1/4 (Sec. 8.4, p. 255)?
- How can the subcritical Hopf in 3D lead to chaos (Lorenz, Ch. 9, p. 255)?
- Why does a nonconservative system turn conservative at a degenerate Hopf point, and how robust is this?

## Reading notes
- This part starts at 8.0 (printed p. 244) and ends after Example 8.3.3 and Fig. 8.3.5 (p. 263). It splits at a section boundary; 8.4 onward is not covered. Printed = pdf − 15.
- No page image was provided for printed p. 256 (pdf 271), so I used the text layer there. The pendulum equation on p. 256 is garbled; $\ddot x+\mu\dot x+\sin x=0$ is my reconstruction.
- Example 8.2.1: signs of $xy^2$ and $y^3$ are garbled in the text layer. I chose $+xy^2$ and $+y^3$ because they give the printed $\dot r=\mu r+ry^2$ (added step: $r\dot r=x\dot x+y\dot y=\mu r^2+x^2y^2+y^4=\mu r^2+r^2y^2$).
- Misprint-like: p. 263 gives $2\pi/\sqrt{15}\approx1.63$; direct computation gives about 1.62.
- Equations (1)–(3) of the chemical model (p. 259) are transcribed in L3 as printed; the source gives them as empirical rate laws without derivation. The section on exercises is omitted: no exercise text is in these pages (only references to Exercises 8.2.11–15 and 2.4.9).
