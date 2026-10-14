---
id: strogatz-2024-nonlinear/ch03-bifurcations-p2
work: strogatz-2024-nonlinear
unit: "3 Bifurcations (part 2/2): end of 3.5, 3.6 Imperfect Bifurcations and Catastrophes, 3.7 Insect Outbreak, chapter exercises"
pages: 70–94
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Imperfect Bifurcations, Catastrophes, and the Spruce Budworm Outbreak

## L0 — One line
A small symmetry-breaking term turns a pitchfork bifurcation into a "cusp catastrophe" with possible sudden jumps, and a simple budworm model of insect outbreaks shows the same cusp structure, with a threshold and hysteresis.

## L1 — The gist (≤ 120 words)
The unit asks what happens to a pitchfork bifurcation when the left–right symmetry is only approximate, and whether the resulting sudden jumps appear in real systems. For $\dot x = h + rx - x^3$ with $h\neq 0$, the pitchfork breaks into two pieces. Saddle-node curves meet at a cusp point, and the fixed-point surface is a cusp catastrophe. The spruce budworm model of Ludwig et al. has the same structure. It has a low "refuge" state, a high "outbreak" state, a bistable region (two stable states), a threshold, and hysteresis (restoring the old parameters does not undo an outbreak). A slowly growing forest drifts the parameters toward outbreak. The unit also closes the singular-limit discussion and gives chapter exercises.

**Prerequisites:** one-dimensional flows $\dot x=f(x)$; fixed points and stability; saddle-node and pitchfork bifurcations; graphical analysis; nondimensionalization (Section 3.5).

## L2 — Key ideas
- In a singular limit the highest-derivative term drops out, and then the initial or boundary conditions can't be satisfied. The "thin layer of time" near $t=0$ is a boundary layer (p. 70).
- A real symmetry is often only approximate. An imperfection parameter $h$ breaks it, and the system $\dot x=h+rx-x^3$ then has two parameters (p. 70).
- Its saddle-node curves $h=\pm h_c(r)$ meet tangentially at a cusp point, a codimension-2 bifurcation. Inside the cusp there are three fixed points, outside one (p. 71).
- The same results can be drawn as a stability diagram, as $x^*$ vs. $r$ or vs. $h$, or as one folded cusp-catastrophe surface. A jump over the fold is the "catastrophe" (pp. 72–73).
- The budworm model reduces to $\dot x = rx(1-x/k) - x^2/(1+x^2)$. The nondimensionalization is chosen so the predation curve contains no parameters (pp. 75–77).
- The model has refuge ($a$) and outbreak ($c$) levels. The unstable middle point $b$ is a threshold, and hysteresis makes an outbreak hard to reverse (pp. 77–78).
- The bifurcation curves have exact parametric form $r=2x^3/(1+x^2)^2$, $k=2x^3/(x^2-1)$ for $x>1$. The diagram can again be regarded as a cusp-catastrophe projection (pp. 78–79).
- As the forest grows, $r$ rises with $k$ fixed, so $(k,r)$ drifts from the bistable region toward the outbreak region (p. 80).

## L3 — Walkthrough

### End of 3.5: A singular limit (p. 70)
- Difficulty in the bead-on-hoop problem: in the limit of strong damping, the term with the highest-order derivative drops out of the equation. Then the initial or boundary conditions cannot be satisfied. Such a limit is called **singular** (p. 70).
- Example: high Reynolds number in fluid mechanics, which explains the thin "boundary layers" over airplane wings. Here the rapid transient is a boundary layer in time near $t=0$ (p. 70).
- The mathematics of such limits is **singular perturbation theory** (p. 70).

### 3.6 Imperfect bifurcations and catastrophes (pp. 70–74)
**Setup.** Pitchfork bifurcations are common when a problem has a symmetry. Real symmetries are often only approximate, so consider
$$\dot x = h + rx - x^3 \tag{1}$$
For $h=0$ this is the normal form of the supercritical pitchfork, symmetric under $x\to -x$. For $h\neq 0$ the symmetry is broken, so $h$ is called an **imperfection parameter** (p. 70).

**Fixed points, graphically.** Fix $r$ and vary $h$. Plot $y=rx-x^3$ and $y=-h$; intersections are fixed points (p. 70).
- For $r\le 0$ the cubic is monotonically decreasing, so there is exactly one intersection (p. 70).
- For $r>0$ there can be one, two or three intersections, depending on $h$ (p. 70).
- The critical case is when the horizontal line is tangent to the cubic's local maximum or minimum. That is a saddle-node bifurcation (p. 71).

**Computing $h_c$.** The local maximum satisfies $\frac{d}{dx}(rx-x^3)=r-3x^2=0$, so $x_{\max}=\sqrt{r/3}$ (p. 71). The cubic's value there is
$$r x_{\max}-(x_{\max})^3=\frac{2r}{3}\sqrt{\frac r3}.$$
The value at the minimum is the negative of this. So saddle-nodes occur at $h=\pm h_c(r)$ with $h_c(r)=\frac{2r}{3}\sqrt{r/3}$. (The printed formula shows denominator 2, which disagrees with the line above; see Reading notes.) Equation (1) has three fixed points for $|h|<h_c(r)$ and one for $|h|>h_c(r)$ (p. 71).

**Stability diagram.** Plot the curves $h=\pm h_c(r)$ in the $(r,h)$ plane (Fig. 3.6.2). They meet tangentially at $(r,h)=(0,0)$, a **cusp point**. Saddle-node bifurcations occur along the boundaries, except at the cusp. There we have a **codimension-2 bifurcation**: this essentially means two parameters must be tuned, whereas earlier bifurcations needed one (codimension-1) (p. 71). Pictures like this show the behaviors found as we move around **parameter space**, and are called **stability diagrams** (p. 72).

**Bifurcation diagrams (p. 72–73).**
- $x^*$ vs. $r$, fixed $h=0$: the usual pitchfork. For $h\neq0$ the pitchfork disconnects into two pieces (Fig. 3.6.3).
- The upper piece is entirely stable fixed points. The lower piece has both stable and unstable branches (p. 72).
- As $r$ increases from negative values there is no longer a sharp transition at $r=0$. The fixed point glides smoothly along the upper branch. The lower stable branch is not reachable without a fairly large disturbance (p. 72).
- $x^*$ vs. $h$, fixed $r$ (Fig. 3.6.4): for $r\le 0$ there is one stable fixed point for each $h$. For $r>0$ there are three fixed points when $|h|<h_c(r)$, and one otherwise. In the triple-valued region the middle branch is unstable and the upper and lower branches are stable. These graphs look like Fig. 3.6.1 rotated by 90° (p. 73).

**Cusp catastrophe.** Plot $x^*$ above the $(r,h)$ plane to get the **cusp catastrophe** surface (Fig. 3.6.5). It folds over on itself. Projecting the folds onto the $(r,h)$ plane gives the bifurcation curves. A cross-section at fixed $h$ gives Fig. 3.6.3, and at fixed $r$ gives Fig. 3.6.4 (p. 73). As parameters change, the state can be carried over the edge of the upper surface and drop discontinuously to the lower surface (Fig. 3.6.6). That is the "catastrophe" (p. 73). The author mentions a violent controversy about catastrophe theory in the late 1970s (p. 73).

*Intuition note.* A tiny asymmetry removes the sharp pitchfork transition. Instead there is a smooth path and a separate "other" state. Reaching that other state, or leaving the present one, can involve a sudden jump.

**Bead on a tilted wire (p. 74).** A bead of mass $m$ slides on a wire at angle $\theta$ to the horizontal. It is attached to a spring (stiffness $k$, relaxed length $L_0$) and acted on by gravity. $x=0$ is the wire point closest to the spring's support point, at distance $a$ from the wire.
- For $\theta=0$ there is left–right symmetry and $x=0$ is always an equilibrium. If $L_0<a$ the spring is in tension and it should be stable. If $L_0>a$ the spring is compressed. The author then expects an unstable equilibrium at $x=0$ and a stable pair on either side (p. 74).
- For $\theta\neq 0$ and small tilt, the author expects three equilibria if $L_0>a$. If the tilt is too steep, "perhaps" the uphill equilibrium might suddenly disappear, causing the bead to jump catastrophically to the downhill one (p. 74). Exercise 3.6.5 gives the mathematics.

### 3.7 Insect outbreak (pp. 74–80)
**Background (pp. 74–75).** The spruce budworm attacks balsam fir in eastern Canada. An outbreak can defoliate and kill most firs in about four years (p. 74). Ludwig et al. (1978) exploit a separation of time scales (p. 75):
- Budworms can increase density fivefold in a year, so their time scale is months.
- Trees replace their foliage in about 7–10 years and live 100–150 years without budworms.
- So the forest variables are treated as constants during the budworm analysis. At the end they are allowed to drift slowly, and this drift triggers an outbreak (p. 75).

**Model (p. 75).** Without predators, budworm population $N(t)$ grows logistically (growth rate $R$, carrying capacity $K$). $K$ depends on foliage, so it is a slowly drifting parameter, held fixed for now. Predation $p(N)$, chiefly by birds, is nearly zero when budworms are scarce. It turns on sharply above a level $N=A$ and then saturates. Ludwig et al. assume $p(N)=\dfrac{BN^2}{A^2+N^2}$ with $A,B>0$, giving
$$\dot N = RN\Big(1-\frac NK\Big) - \frac{BN^2}{A^2+N^2}. \tag{1}$$
"Outbreak" must mean that, as parameters drift, the population jumps suddenly from a low to a high level (p. 75).

**Dimensionless form (p. 76).** The model has four parameters $R,K,A,B$. Heuristic: put all dimensionless groups in the logistic part, none in the predation part. This eases the graphical analysis. Divide (1) by $B$ and set $x=N/A$:
$$\frac AB\frac{dx}{dt}=\frac RB\,Ax\Big(1-\frac{Ax}{K}\Big)-\frac{x^2}{1+x^2}\tag{2}$$
Define $\tau=\dfrac{Bt}{A},\; r=\dfrac{RA}{B},\; k=\dfrac KA$. Then
$$\frac{dx}{d\tau}=rx\Big(1-\frac xk\Big)-\frac{x^2}{1+x^2}\tag{3}$$
$r$ and $k$ are the dimensionless growth rate and carrying capacity (p. 76).

**Fixed points (pp. 76–78).**
- $x^*=0$ is always unstable (Exercise 3.7.1). Predation is extremely weak for small $x$, so the population grows exponentially near zero (p. 76).
- Other fixed points solve
$$r\Big(1-\frac xk\Big)=\frac{x}{1+x^2}\tag{4}$$
- The left side is a straight line with $x$-intercept $k$ and $y$-intercept $r$. The right side is a curve independent of the parameters, so varying $r,k$ moves only the line (p. 77).
- For sufficiently small $k$ there is exactly one intersection for any $r>0$. For large $k$ there can be one, two or three, depending on $r$ (p. 77).
- Suppose there are three intersections $a<b<c$. Decreasing $r$ at fixed $k$ rotates the line counterclockwise about $k$. Then $b$ and $c$ coalesce in a saddle-node bifurcation when the line is tangent to the curve. Only $a$ remains besides $x^*=0$. Similarly $a$ and $b$ collide and annihilate as $r$ increases (p. 77).
- Stability alternates along the $x$-axis and $x^*=0$ is unstable. So $a$ is stable, $b$ unstable, $c$ stable (Fig. 3.7.4). $a$ is the **refuge** level and $c$ the **outbreak** level (p. 77).
- The fate is decided by the initial condition $x_0$. An outbreak occurs if and only if $x_0>b$, so $b$ acts as a threshold (p. 78).
- An outbreak can also be triggered by drift of $r,k$ that makes $a$ disappear. The population then jumps to $c$. By hysteresis, restoring the old parameter values will not bring the population back to the refuge level (p. 78).

**Bifurcation curves (pp. 78–79).** We cannot write $r$ explicitly as a function of $k$. Instead the curves are parametric, $(k(x),r(x))$, with $x$ as the curve parameter (p. 78). Tangency of line and curve requires both
$$r\Big(1-\frac xk\Big)=\frac{x}{1+x^2}\tag{5}$$
$$\frac{d}{dx}\Big[r\Big(1-\frac xk\Big)\Big]=\frac{d}{dx}\Big[\frac{x}{1+x^2}\Big]\tag{6}$$
Differentiating, (6) reduces to
$$-\frac rk=\frac{1-x^2}{(1+x^2)^2}\tag{7}$$
Substituting $r/k$ from (7) into (5) gives
$$r=\frac{2x^3}{(1+x^2)^2}\tag{8}$$
Inserting (8) into (7) gives
$$k=\frac{2x^3}{x^2-1}\tag{9}$$
$k>0$ restricts $x$ to $x>1$ (p. 78).
(Added step: from (7), $r/k=(x^2-1)/(1+x^2)^2$; (5) gives $r=\frac{x}{1+x^2}+x\frac rk$, which equals $\frac{2x^3}{(1+x^2)^2}$; then $k=r/(r/k)$.)

Plotting $(k(x),r(x))$ for $x>1$ gives Fig. 3.7.5. Its regions are **refuge** (only $a$ stable, low $r$), **outbreak** (only $c$ stable, large $r$), and **bistable** (both stable states) (p. 79). The diagram is very similar to Fig. 3.6.2 and is the projection of a cusp catastrophe surface (Fig. 3.7.6) (p. 79). Exercise 3.7.2 deals with analytical properties of the curves (p. 79).

*Intuition note.* The line-versus-fixed-curve picture shows how two stable levels can coexist. Raising $r$ slides the system toward one fold and lowering it toward the other. The bistable wedge is where history decides which state the population occupies.

**Comparison with observations (p. 80).** According to Ludwig et al., $r$ increases as the forest grows while $k$ stays fixed. Reasoning: let $S$ be average tree size (total branch surface area per stand). Then $K=K'S$. Also $A=A'S$, because birds search units of foliage, not acres, so $A'$ has dimensions of budworms per unit branch area. Hence
$$r=\frac{RA'}{B}S,\qquad k=\frac{K'}{A'}\tag{10}$$
- For a young forest, typically $k\approx 300$ and $r<1/2$, so the parameters lie in the bistable region. Birds keep the population down.
- As $S$ grows, $(k,r)$ drifts upward toward the outbreak region. Ludwig et al. estimate $r\approx 1$ for a fully mature forest, "dangerously" in the outbreak region.
- After an outbreak the firs die and birch takes over. Birch uses nutrients less efficiently, and firs return after about 50–100 years (Murray 2002).
- Neglected in the model: tree dynamics and the spatial distribution and dispersal of budworms (p. 80).

### Exercises for Chapter 3 (pp. 80–94)
The exercises cover sections 3.1–3.7 and are not digested in detail. Topics include:
- classification of bifurcations;
- laser threshold and adiabatic elimination (pp. 81–82);
- potentials and a first-order phase transition (p. 84);
- nondimensionalization;
- imperfect transcritical and perturbed pitchfork systems;
- the tilted-wire bead;
- Landau equation, tricritical bifurcation and the Ising magnet (pp. 87–89);
- fishery, biochemical-switch and epidemic models;
- hysteretic activation and irreversible response in systems biology (pp. 90–94).

## Toy example (ours, not from the text)
Take $\dot x = h + 3x - x^3$, so $r=3$ in equation (1).
1. $x_{\max}=\sqrt{r/3}=1$.
2. Cubic value at the maximum: $3(1)-1^3=2$. This equals $\frac{2r}{3}\sqrt{r/3}=2\cdot1=2$, so $h_c=2$.
3. Take $h=1$ ($<2$) and $f(x)=1+3x-x^3$. Then $f(-2)=1-6+8=3$, $f(-1)=1-3+1=-1$, $f(0)=1$, $f(1)=3$, $f(2)=1+6-8=-1$. There are sign changes in $(-2,-1)$, $(-1,0)$ and $(1,2)$, so three fixed points.
4. Take $h=3$ ($>2$) and $f(x)=3+3x-x^3$. Then $f(2)=1$ and $f(3)=3+9-27=-15$. There is a root in $(2,3)$. For $x\le 2$: $f(-2)=5$, $f(-1)=1$, $f(0)=3$, so $f>0$ at these points. One fixed point.
5. Slow sweep: start at $h=3$ with the single fixed point near $x\approx2.1$ (since $f(2.1)=0.039$). Lower $h$ slowly. At $h=-2$, $\dot x=-(x-1)^2(x+2)$ (check: $-(x^2-2x+1)(x+2)=-x^3+3x-2$). The upper fixed point has been gliding down and now sits at the double root $x=1$. For $h$ slightly below $-2$, e.g. $h=-3$, the only fixed point is near $x\approx-2.1$ ($f(-2)=-1$, $f(-2.2)=1.05$). The state drops discontinuously from about 1 to about $-2$: the catastrophe. Raising $h$ again, the state stays on the lower branch until $h=+2$. That is hysteresis.

## Concepts
- [[saddle-node-fold-bifurcation]] — two fixed points collide and vanish where a line is tangent to a curve; here along $h=\pm h_c(r)$ and the budworm curves (p. 71, p. 77)
- [[bifurcation]] — qualitative change in the fixed points as a parameter varies; here the saddle-node bifurcations along $h=\pm h_c(r)$ (p. 71)
- [[hysteresis]] — after an outbreak, restoring old parameter values does not restore the refuge state (p. 78)
- [[fixed-point-and-stability]] — stability alternates along the $x$-axis; $a$ stable, $b$ unstable, $c$ stable (p. 77)
- [[tipping-point]] — here the sudden jump from low to high population (an "outbreak") when a fixed point disappears (p. 78)
- [[imperfect-bifurcation]] (new) — a bifurcation with an extra imperfection parameter $h$ that breaks a symmetry; here $\dot x=h+rx-x^3$ (p. 70)
- [[cusp-catastrophe]] (new) — surface of fixed points over a two-parameter plane that folds over, with jumps at the fold edges (p. 73)
- [[codimension]] (new) — number of parameters to tune to reach a bifurcation; the cusp point is codimension-2 (p. 71)
- [[stability-diagram]] (new) — plot of regions in parameter space with different behavior types (p. 72)
- [[singular-limit]] (new) — limit in which the highest-derivative term drops out, leaving unmet initial conditions (p. 70)
- [[time-scale-separation]] (new) — fast variable (budworms) treated with the slow one (forest) held constant (p. 75)
- [[nondimensionalization]] (new) — rescaling to dimensionless groups; here chosen so predation has no parameters (p. 76)

## Canonical instances
- [[imperfect-pitchfork-h-rx-x3]] — $\dot x=h+rx-x^3$; cusp at $(0,0)$ (p. 70)
- [[bead-on-tilted-wire]] — mechanical example of imperfect bifurcation and catastrophe (p. 74)
- [[spruce-budworm-model]] — Ludwig et al. outbreak model with refuge, outbreak and bistable regions (p. 75)

## Bridges (candidates)
- [structural-analogy] cusp catastrophe and bistable region ↔ complex-systems: tipping points with hysteresis — a sudden jump plus a different path back
- [structural-analogy] imperfection $h$ breaking up/down symmetry ↔ physics: external field $h$ on the Ising magnet (Exercise 3.6.7, p. 89), where the phase transition is softened
- [structural-analogy] unstable middle fixed point $b$ as threshold ↔ social science: threshold models of adoption, where the outcome depends on the initial state
- [structural-analogy] slow drift of $r$ pushing a system to a fold ↔ early-warning signals: a slowly changing parameter carries a system toward a critical transition
- [metaphor] boundary layer in time near $t=0$ ↔ social systems with fast initial adjustments before slow dynamics

## Questions this raises
- Does the budworm model give any warning before the refuge level $a$ disappears, e.g., slower recovery from perturbations?
- How would the budworm picture change if the tree variables fed back on $K$ and $r$ dynamically, instead of drifting as an externally given slow variable?
- What does adding a small imperfection do to a saddle-node bifurcation (Exercise 3.6.4)?
- Are there general conditions under which a cusp with a bistable wedge appears, beyond these two examples?

## Exercises worth doing
- Ex. 3.6.2 (p. 86) — imperfect transcritical bifurcation: bifurcation diagrams, regions in $(r,h)$, potentials — difficulty: medium
- Ex. 3.6.5 (p. 87) — bead on tilted wire: derive the equilibrium equation and exact parametric bifurcation curves — difficulty: hard
- Ex. 3.5.6 (p. 85) — model singular-limit problem $\varepsilon\ddot x+\dot x+x=0$ and its two time scales — difficulty: medium
- Ex. 3.7.2 (p. 89) — limits of $r(x),k(x)$ and exact cusp point of the budworm diagram — difficulty: medium
- Ex. 3.7.4 (p. 90) — improved fishery model with one, two or three fixed points and a stability diagram — difficulty: hard
- Ex. 3.7.7 (p. 93) — hysteretic activation in a protein positive-feedback loop — difficulty: medium

## Reading notes
- This part begins at printed p. 70 inside Section 3.5 (the "A Singular Limit" paragraph) and ends at p. 94, the end of the chapter's exercises. The part starts at the subsection heading "A Singular Limit" inside Section 3.5, not at the start of a section. Printed page = pdf page − 15.
- The text layer garbles symbols (e.g., ≠, ≤, Greek letters); I checked equations against the page images.
- Misprint on p. 71: the displayed formula for $h_c(r)$ appears with $2r/2$. The preceding line gives $\frac{2r}{3}\sqrt{r/3}$ and derivation confirms 2r/3. I used 2r/3.
- Exercise 3.7.2 refers to Eqs. (3.7.8) and (3.7.9) for the curves, which appear in this unit as (8) and (9).
- Fig. 3.7.5 plots $k$ only up to 40, while the text quotes $k\approx300$ for a young forest.
- Several section statements about bifurcation types in exercises were not worked out here.
