---
id: strogatz-2024-nonlinear/ch06-phase-p2
work: strogatz-2024-nonlinear
unit: "6 Phase Plane (part 2/2): end of 6.7 Pendulum, 6.8 Index Theory, Exercises for Chapter 6"
pages: 174-197
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Index theory: global information about phase portraits

## L0 — One line
The index of a closed curve (the net number of counterclockwise turns of the vector field along it) equals the sum of the indices of the enclosed fixed points, so a closed orbit must enclose fixed points whose indices sum to +1.

## L1 — The gist (≤ 120 words)
Linearization describes a phase portrait only near a fixed point. Index theory gives global information. The index of a closed curve counts how many times the vector field turns counterclockwise as we go once around the curve. It is an integer. It does not change when the curve is deformed without crossing a fixed point. It equals the sum of the indices of the enclosed fixed points. A closed orbit has index +1, so it must enclose fixed points whose indices sum to +1. Saddles have index −1. Nodes, spirals, centers and stars have +1. This can rule out closed orbits in some systems.

**Prerequisites:** phase plane and vector field $\dot{\mathbf x}=\mathbf f(\mathbf x)$; classification of fixed points (node, saddle, spiral, center); angle of a vector; closed orbit.

## L2 — Key ideas
- Linearization is local. Index theory is a global tool that can say what must lie inside a closed curve (p. 174).
- The index $I_C$ of a simple closed curve $C$ is $\frac{1}{2\pi}[\phi]_C$. It needs the vector field only along $C$ (p. 175).
- The index is unchanged by deformations of $C$ that avoid fixed points. It is 0 if $C$ encloses no fixed points. Reversing time leaves it unchanged. A closed orbit has index +1 (pp. 177–178).
- The index of an isolated fixed point is $I_C$ for any small enclosing curve. It is +1 for stable and unstable nodes (so it is not tied to stability), spirals, centers and stars. It is −1 for a saddle (pp. 178–179).
- Theorem 6.8.1: $I_C=\sum_k I_k$ over the enclosed fixed points. The proof shrinks $C$ onto small circles joined by bridges whose contributions cancel (p. 179).
- Theorem 6.8.2: a closed orbit must enclose fixed points with indices summing to +1. So there is at least one fixed point inside, and a lone one cannot be a saddle (p. 180).
- Application: in the rabbit–sheep system, index counting plus the rule that trajectories cannot cross rules out closed orbits. If a system has no fixed points, it has no closed orbits (pp. 180–181).
- The chapter's exercises extend the chapter's topics: phase portraits, linearization, competition models, conservative, Hamiltonian and reversible systems, the pendulum, and index theory (pp. 181–197).

## L3 — Walkthrough

### End of 6.7 Pendulum (p. 174)
- In the damped pendulum, the energy $E$ decreases monotonically along trajectories, except at fixed points (p. 174). The text layer is garbled here and the page image was not available.
- Physical reading of the trajectory in Fig. 6.7.8: the pendulum starts whirling clockwise and loses energy. It spirals down the "arm" of the U-tube until $E$ reaches the value 1 (the symbol is garbled in the text). Then it cannot whirl any more, so it oscillates about the bottom. The motion then damps out and the pendulum rests at its stable equilibrium (p. 174).
- Conclusion of 6.7: in this pendulum example, pictures alone were enough to extract all the important features of the dynamics. Obtaining them analytically would be much more difficult, and the formulas much more confusing to interpret, even if we could find them (p. 174).

### 6.8 Index Theory
**Motivation (p. 174).** Linearization gives a detailed local view near a fixed point. It cannot say what happens after trajectories leave the neighborhood. If the vector field starts with quadratic or higher-order terms, linearization tells us nothing. Index theory gives global information. It lets us answer such questions as: must a closed trajectory encircle a fixed point, which types of fixed points are allowed inside, and which types can coalesce in bifurcations? It also gives information about higher-order fixed points and can sometimes rule out closed orbits (p. 174).

**Analogy (p. 174).** A "Gaussian surface" in electrostatics lets us find the total charge inside from the field on the surface. Here the vector field plays the role of the electric field, the curve $C$ plays the role of the surface, and the index plays the role of the charge.

**The index of a closed curve (p. 175).**
- Let $\dot{\mathbf x}=\mathbf f(\mathbf x)$ be a smooth vector field. $C$ is a simple closed curve (it does not intersect itself). It need not be a trajectory and it must not pass through a fixed point (p. 175).
- At each point of $C$ the vector $(\dot x,\dot y)$ makes the angle $\phi=\tan^{-1}(\dot y/\dot x)$ with the positive $x$-axis. As $\mathbf x$ moves once counterclockwise around $C$, $\phi$ changes continuously and returns to its direction. So its net change $[\phi]_C$ is an integer multiple of $2\pi$ (p. 175).
- Definition:
$$I_C=\frac{1}{2\pi}[\phi]_C .$$
$I_C$ is the net number of counterclockwise revolutions of the vector field as $\mathbf x$ goes once counterclockwise around $C$. Only the field along $C$ is needed (p. 175).
- Foolproof method: number the vectors counterclockwise along $C$. Move them, without rotating, so their tails meet at a common origin. Then count the net counterclockwise revolutions of the numbered vectors (p. 175).

*Intuition note.* Walk once around the loop and watch the arrow of the field. If the arrow turns once counterclockwise, the index is +1. If it turns once clockwise, the index is −1. If it swings back and forth with no net turn, the index is 0.

**Examples (pp. 175–177).**
- Ex. 6.8.1: in Fig. 6.8.2 the vectors rotate one full turn in the same (counterclockwise) sense, so $I_C=+1$ (pp. 175–176).
- Ex. 6.8.2: in Fig. 6.8.4 the vectors rotate one full turn clockwise as we go counterclockwise around $C$, so $I_C=-1$ (p. 176).
- Ex. 6.8.3: $\dot x=x^2y$, $\dot y=x^2-y^2$, $C$ the unit circle. Evaluate at convenient points. At $(1,0)$ the vector is $(0,1)$ (#1). At $\tfrac{1}{\sqrt2}(1,1)$ it is $\tfrac{1}{2\sqrt2}(1,0)$ (#2). Vectors #3 and #7 are both $(0,-1)$. Going from #1 to #9, the vectors rotate 180° clockwise (#1→#3), then 360° counterclockwise (#3→#7), then 180° clockwise (#7→#9). So $[\phi]_C=-\pi+2\pi-\pi=0$ and $I_C=0$ (p. 177). The author notes that one may plot more points for finer detail.

**Properties of the index (pp. 177–178).**
1. If $C$ can be continuously deformed into $C'$ without passing through a fixed point, then $I_C=I_{C'}$. Proof: $I_C$ varies continuously under the deformation and is an integer. A continuous integer-valued function must be constant. The author asks the reader to see where the assumption that the intermediate curves avoid fixed points was used (p. 177).
2. If $C$ encloses no fixed points, then $I_C=0$. Proof: by (1), shrink $C$ to a tiny circle. By smoothness all vectors there point in nearly the same direction, so $[\phi]_C=0$ (pp. 177–178).
3. Reversing all arrows ($t\to-t$) leaves the index unchanged. Proof: every angle changes from $\phi$ to $\phi+\pi$, so $[\phi]_C$ is unchanged (p. 178).
4. If $C$ is itself a closed orbit, then $I_C=+1$. The author does not prove this. The vector field is tangent to $C$, so as $\mathbf x$ winds once around $C$ the tangent vector also rotates once in the same sense (p. 178).

**Index of a point (pp. 178–179).**
- For an isolated fixed point $\mathbf x^*$, its index $I$ is $I_C$ for any closed curve $C$ that encloses $\mathbf x^*$ and no other fixed point. By property (1) this depends on $\mathbf x^*$ alone (p. 178).
- Ex. 6.8.4: near a stable node the field looks like that of Ex. 6.8.1, so $I=+1$. An unstable node also has $I=+1$, because reversing all arrows does not change the index (property 3). So the index is not related to stability, per se. A saddle looks like Ex. 6.8.2, so $I=-1$ (p. 179).
- Exercise 6.8.1 asks the reader to show that spirals, centers, degenerate nodes and stars all have $I=+1$. So a saddle differs from all the other familiar types of isolated fixed points (p. 179).

**Theorem 6.8.1 (p. 179).** If a closed curve $C$ surrounds $n$ isolated fixed points $\mathbf x_1^*,\dots,\mathbf x_n^*$, then
$$I_C=I_1+I_2+\dots+I_n ,$$
where $I_k$ is the index of $\mathbf x_k^*$.

*Ideas behind the proof (p. 179).* The author gives only the ideas of the proof.
- Deform $C$ like a balloon with the air sucked out, taking care not to hit any fixed point. The result is a curve $\Gamma$ made of $n$ small circles $\gamma_1,\dots,\gamma_n$ around the fixed points, joined by two-way bridges. By property (1), $I_\Gamma=I_C$.
- The bridge contributions to $[\phi]_\Gamma$ cancel, because each bridge is traversed once in each direction. On $\gamma_k$, $[\phi]_{\gamma_k}=2\pi I_k$ by definition. So
$$I_\Gamma=\frac{1}{2\pi}[\phi]_\Gamma=\frac{1}{2\pi}\sum_{k=1}^n[\phi]_{\gamma_k}=\sum_{k=1}^n I_k .$$

The author compares this with Gauss's law and refers to Exercise 6.8.12 for the index–charge analogy (p. 180).

**Theorem 6.8.2 (p. 180).** Any closed orbit in the phase plane must enclose fixed points whose indices sum to +1.
- Proof: for a closed orbit $C$, property (4) gives $I_C=+1$. Theorem 6.8.1 then gives $\sum_k I_k=+1$ (p. 180).
- Consequences: there is always at least one fixed point inside any closed orbit. If there is only one inside, it cannot be a saddle. The theorem can sometimes rule out closed trajectories (p. 180).

*Intuition note.* A closed orbit has index +1 because its own arrows turn once around it. That total turning must come from the fixed points inside, like total charge inside a surface. Saddles count −1, and nodes, spirals, centers and stars count +1, so if all the fixed points inside are of these usual types, a closed orbit encloses one more non-saddle than saddles (Exercise 6.8.6, p. 196).

**Ex. 6.8.5: rabbits vs. sheep has no closed orbits (p. 180).** The system is $\dot x=x(3-x-2y)$, $\dot y=y(2-x-y)$ with $x,y\ge0$. The fixed points are $(0,0)$, an unstable node; $(0,2)$ and $(3,0)$, stable nodes; and $(1,1)$, a saddle. The indices are $+1,+1,+1,-1$ (Fig. 6.8.9). There are three qualitatively different places for a closed orbit (p. 180):
- $C_1$ encloses no fixed point. This is impossible because the enclosed indices cannot sum to +1 (Theorem 6.8.2; by property (2) the index would be 0).
- $C_2$ encloses only the saddle, so the indices sum to $-1$, not $+1$. This is impossible.
- $C_3$ encloses a point of index $+1$ and so passes the index test. It would cross the $x$-axis or the $y$-axis, and these axes contain straight-line trajectories. Trajectories cannot cross, so $C_3$ is impossible too.

**Ex. 6.8.6 (p. 181).** The system $\dot x=xe^{-x}$, $\dot y=1+x+y^2$ has no fixed points. If $\dot x=0$ then $x=0$, so $\dot y=1+y^2\neq0$. By Theorem 6.8.2 there are no closed orbits.

### Exercises for Chapter 6 (pp. 181–197)
These cover the whole of Chapter 6. They are summarised by section, not solved here.
- **6.1–6.3 (pp. 181–184).** Sketching phase portraits (nullclines and vector fields); computer portraits (van der Pol oscillator, dipole fixed point, "two-eyed monster", "parrot"); saddle connections; a series approximation to a saddle's stable manifold (6.1.14); existence and uniqueness (6.2); and linearization, including cases where it is inconclusive or misleading. Examples are 6.3.10 ($\dot x=xy,\dot y=x^2-y$), 6.3.11 (a star that is a spiral in the nonlinear system), 6.3.13 (a linear center that is a nonlinear spiral) and 6.3.15 (attracting but not Liapunov stable). In 6.3.16 the author defines the phase portrait with a saddle connection to be not structurally stable, because a small change of the parameter $a$ changes its topology (p. 184).
- **6.4 (pp. 184–187).** Competition models of increasing complexity, with basins of attraction. Further models are a two-mode laser, an evolutionary model with exponent $c$, a Keynesian-cross economy, the hypercycle equation for $n=2$ (6.4.10) and the leftists–rightists–centrists opinion model (6.4.11).
- **6.5 (pp. 187–192).** Conserved quantities, homoclinic orbits, potentials, the Kermack–McKendrick epidemic, and general-relativity orbits. The text then defines a *Hamiltonian system*: for smooth $H(p,q)$,
$$\dot q=\frac{\partial H}{\partial p},\qquad \dot p=-\frac{\partial H}{\partial q},$$
with $H$ called the Hamiltonian (p. 189). Exercises 6.5.8–6.5.10 cover the harmonic oscillator, conservation of $H$, and the inverse-square law. Other exercises cover damped double wells, nonlinear centers, a glider and the bead on a rotating hoop. In 6.5.19 (Lotka–Volterra) the author notes that mathematical biologists dismiss the model because it is not structurally stable. Real predator–prey cycles typically have a characteristic amplitude, not a continuous family of neutrally stable cycles (p. 191). 6.5.20 is a rock–paper–scissors model with two conserved quantities (p. 192).
- **6.6 (pp. 192–194).** Reversible systems: phase portraits, the "manta ray" argument, a system on a cylinder, a Josephson junction array, and rotation on a sphere.
- **6.7 (pp. 194–195).** The damped pendulum, the pendulum driven by constant torque, and nonlinear damping. In 6.7.4 the reader is asked to derive the exact period $T=4K(\sin^2\tfrac12\alpha)$ and, for $\alpha\ll1$, $T(\alpha)=2\pi[1+\tfrac{1}{16}\alpha^2+O(\alpha^4)]$ (p. 195).
- **6.8 (pp. 196–197).** Unusual fixed points and their indices; $N+F+C=1+S$ for a closed orbit (6.8.6); ruling out closed orbits (6.8.7); arrangements of cycles (6.8.8–6.8.9); other surfaces (6.8.10); complex vector fields (6.8.11); "matter and antimatter" in bifurcations (6.8.12); and the integral formula $I_C=\frac{1}{2\pi}\oint_C\frac{f\,dg-g\,df}{f^2+g^2}$ (6.8.13, p. 197).

## Toy example (ours, not from the text)
Take the saddle field $\dot x=x$, $\dot y=-y$ and $C$ the unit circle. Sample the field at four points going counterclockwise. The angle of the vector is measured continuously (the vectors rotate steadily, so each quarter-step is a quarter-turn).

| Point | Vector | Angle |
|---|---|---|
| (1,0) | (1,0) | 0 |
| (0,1) | (0,−1) | −π/2 |
| (−1,0) | (−1,0) | −π |
| (0,−1) | (0,1) | −3π/2 |
| back to (1,0) | (1,0) | −2π |

So $[\phi]_C=-2\pi$ and $I_C=-1$. This matches the saddle index of −1 (p. 179).

Now take the node $\dot x=-x$, $\dot y=-y$. The angles run $\pi$, $3\pi/2$, $2\pi$, $5\pi/2$, $3\pi$, so $[\phi]_C=3\pi-\pi=2\pi$ and $I_C=+1$.

Now suppose a curve $C$ encloses exactly one node and one saddle. Theorem 6.8.1 gives $I_C=+1+(-1)=0\neq+1$. By Theorem 6.8.2, $C$ cannot be a closed orbit.

## Concepts
- [[index-of-closed-curve]] (new) — $I_C=\frac{1}{2\pi}[\phi]_C$, the net number of counterclockwise turns of the vector field along a simple closed curve (p. 175).
- [[index-of-fixed-point]] (new) — the index $I_C$ for any small closed curve enclosing only that isolated fixed point. It is +1 for nodes, spirals, centers and stars, and −1 for saddles (pp. 178–179).
- [[fixed point and stability]] — the author stresses that the index is not related to stability: stable and unstable nodes both have index +1 (p. 179).
- [[linear stability analysis]] — described as a local method, with its limits stated: it tells us nothing when the vector field starts with quadratic or higher-order terms (p. 174).
- [[state space / phase space]] — the phase plane, where index curves are drawn as probes, not necessarily trajectories (p. 175).
- [[bifurcation]] — index theory is said to constrain which fixed points can coalesce in bifurcations (p. 174). On these pages it is explored only in Exercise 6.8.12 (p. 196).
- [[hamiltonian-system]] (new) — a system $\dot q=\partial H/\partial p$, $\dot p=-\partial H/\partial q$ (p. 189).
- [[structural-stability]] (new) — a phase portrait is not structurally stable if an arbitrarily small perturbation changes its topology. Used in Exercise 6.3.16 and the Lotka–Volterra remark (pp. 184, 191).

## Canonical instances
- [[rabbits-vs-sheep]] — index counting plus the no-crossing rule rules out closed orbits (p. 180).
- [[damped-pendulum]] — energy decreases along trajectories. The trajectory spirals down the "arm", then settles (p. 174).
- [[lotka-volterra-predator-prey]] — exercise model whose neutrally stable cycles are criticised as not structurally stable (p. 191).
- [[rock-paper-scissors-model]] — three-species exercise model with two conserved quantities (p. 192).
- [[hypercycle-equation]] — exercise model of self-reproducing molecules (p. 186).
- [[opinion-model-leftists-rightists-centrists]] — exercise opinion-dynamics model (p. 187).
- [[kermack-mckendrick-epidemic]] — exercise epidemic model (p. 188).

## Bridges (candidates)
- [structural-analogy] Index of a curve = sum of indices inside ↔ electrostatics: Gauss's law (flux through a surface = enclosed charge). The author draws this analogy himself (pp. 174, 180).
- [structural-analogy] Index sum conserved as fixed points collide ↔ physics: particle–antiparticle collisions (the author's analogy, Exercise 6.8.12, p. 196; which fixed points play the role of "antimatter" is not stated on these pages).
- [same-math] Index as winding number of the vector field ↔ complex analysis: the winding number of a function around zeros (Exercise 6.8.11 uses complex vector fields, p. 196). The text only suggests the connection.

## Questions this raises
- The index uses only the vector field on $C$, yet it counts fixed points inside. Does an index argument tell us how many fixed points there are, or only the sum of their indices?
- Index theory rules out closed orbits in some regions. What other tools show that no closed orbit exists when index counting is inconclusive?
- Exercise 6.8.10 asks whether Theorem 6.8.2 holds on a torus, a cylinder or a sphere. Which step of the proof fails when the surface is not the plane?
- Many models in the exercises have conserved quantities and so give neutrally stable cycles. Why does the author call such cycles unrealistic for predator–prey?

## Exercises worth doing
- Ex. 6.8.1 (p. 196) — show that spirals, centers, stars and degenerate nodes have index +1; this completes the index table — difficulty: easy
- Ex. 6.8.6 (p. 196) — derive $N+F+C=1+S$ for a closed orbit from Theorem 6.8.2 — difficulty: easy
- Ex. 6.8.7 (p. 196) — use index theory to rule out closed orbits in $\dot x=x(4-y-x^2)$, $\dot y=y(x-1)$ — difficulty: medium
- Ex. 6.8.12 (p. 196) — the index sum is conserved through a two-dimensional saddle-node bifurcation, and its generalisation — difficulty: medium
- Ex. 6.8.13 (p. 197) — derive the integral formula for $I_C$ from $d\phi$ — difficulty: medium
- Ex. 6.5.9 (p. 189) — show that the Hamiltonian is conserved using the chain rule and Hamilton's equations — difficulty: easy

## Reading notes
- This is part 2 of Chapter 6. It starts at printed p. 174 with the closing lines of Section 6.7 (the page begins with "Hence E decreases monotonically...") and ends at p. 197 (end of the chapter exercises). All of 6.8 is included; according to the unit metadata, the earlier part of 6.7 is in part 1.
- Offset: printed = pdf − 15.
- The text layer is garbled for Greek letters and math signs: $\phi$ appears as "G", $\theta$ as "R", $\pi$ as "Q", and "+/−" signs are often lost. I checked these against the page images for pp. 175–197.
- No page image was supplied for printed p. 174. The pendulum paragraph ("R w 0", "E  1") is therefore read from the text only, and the two symbols are uncertain. I did not guess further.
- In Example 6.8.2 (p. 176) the text layer shows "I_C  1" as the result; the image shows $I_C=-1$.
- I did not solve exercises. The exercise section is summarised by topic, and only the formulas the author prints in the exercise text are quoted.
