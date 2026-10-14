---
id: strogatz-2024-nonlinear/ch10-one-p2
work: strogatz-2024-nonlinear
unit: "10 One-Dimensional Maps (part 2/2): end of 10.5, 10.6 Universality and Experiments, 10.7 Renormalization, chapter exercises"
pages: 376-404
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Universality, experiments and renormalization for one-dimensional maps

## L0 — One line
Period-doubling in smooth one-humped maps follows universal rules (order of cycles; ratios 4.669… and −2.5029…), which Feigenbaum's renormalization theory explains and experiments support.

## L1 — The gist (≤ 120 words)
Why do very different one-humped maps, and real experiments, show the same period-doubling numbers? Metropolis et al. proved that the order in which stable cycles appear is the same for the unimodal (one-humped) maps they considered (precise conditions are in their paper). Feigenbaum found that the bifurcation spacings shrink by δ ≈ 4.669 and the distances from the maximum to the nearest cycle point by α ≈ −2.5029. Experiments (convection, circuits) give δ in reasonable agreement with this. The explanation is renormalization: iterate the map twice, rescale, shift the parameter, and repeat. A crude algebraic version gives δ ≈ 5.12 and α ≈ −2.24. The theory applies when the system's return map (Lorenz map) is nearly one-dimensional and one-humped; it does not apply to fully turbulent systems.

**Prerequisites:** fixed points, cycles and multipliers of 1-D maps; logistic map and orbit diagram; superstable cycles; Lorenz map (Section 9.4); basic Taylor expansion.

## L2 — Key ideas
- The Lyapunov exponent λ of the logistic map is negative before r∞ ≈ 3.57, approaches zero at period-doublings and becomes positive in chaos. Dips mark periodic windows (p. 376).
- The sine map and the logistic map have the same qualitative orbit diagram (same order and relative sizes of windows) but differ quantitatively. For the order of cycles, only the overall shape of the map matters, not its formula (p. 377).
- The U-sequence is the fixed order in which stable periodic attractors appear in unimodal maps. It was seen in the Belousov–Zhabotinsky reaction (pp. 377–379).
- δ = 4.669… (parameter direction) and α = −2.5029… (x direction) are universal constants of period-doubling (pp. 380–381).
- Experiments on convecting mercury and electronic circuits give δ values in reasonable agreement with 4.669, but they are hard beyond about five doublings (pp. 382–383).
- Feigenbaum's theory applies when a system's Lorenz map (the plot of each local maximum of a flow against the next) is nearly one-dimensional and unimodal; for that the attractor must be very flat, which requires strong dissipation. The Rössler system shows this. Turbulent fluids and fibrillating hearts are not covered (pp. 383–386).
- Renormalization: take f², rescale x by α, shift r to the next superstable value. (A superstable cycle has multiplier 0.) At the onset of chaos the limit g solves g(x) = α g²(x/α), and with g(0)=1 this gives α = 1/g(1) (pp. 387–391).
- An approximate "pedestrian" renormalization is done in closed form. It gives r∞ ≈ 3.56, δ ≈ 5.12, α ≈ −2.24 (pp. 391–394).

## L3 — Walkthrough

### 10.5 (end): Lyapunov exponent of the logistic map (p. 376)
This part finishes an example begun on the previous page. Figure 10.5.2 plots λ against r for the logistic map. Compared with the orbit diagram (Figure 10.2.7):
- λ stays negative for r < r∞ ≈ 3.57 and approaches zero at the period-doubling bifurcations. The negative spikes correspond to the 2ⁿ-cycles.
- Chaos begins near r ≈ 3.57, where λ first becomes positive.
- For r > 3.57, λ generally increases, except for dips caused by periodic windows. The period-3 window near r = 3.83 gives a large dip. (p. 376)

All dips should really reach λ = −∞. A superstable cycle occurs near the middle of each dip, and such cycles have λ = −∞ (Example 10.5.1). That part of the spike is too narrow to resolve in the figure. (p. 376)

*Intuition note.* In this figure, λ is negative where orbits settle onto a cycle and becomes positive where chaos begins (λ is defined earlier in the chapter, not on these pages). A superstable cycle has multiplier 0, so its λ = −∞.

### 10.6 Universality and Experiments

**Example 10.6.1 (sine map vs logistic map).** The sine map is $x_{n+1}=r\sin\pi x_n$ with $0\le r\le1$, $0\le x\le1$ (p. 376). Its graph has the same shape as the logistic map: smooth, concave down, with a single maximum. Such maps are called **unimodal** (one-humped) (p. 377).
- Orbit diagrams (Figure 10.6.2) look extremely alike. The sine map's r-axis is scaled by 4, because its maximum is $r$ while the logistic maximum is $\tfrac14 r$ (p. 377).
- The qualitative dynamics are identical. Both have a period-doubling route to chaos, then periodic windows between chaotic bands. The windows appear in the same order and with the same relative sizes. The period-3 window is largest in both, and the next largest before it are period 5 and period 6 (p. 377).
- Quantitative differences: period-doublings occur later in the logistic map and its windows are thinner (p. 377).

**Qualitative universality: the U-sequence.** Metropolis et al. (1973) considered unimodal maps $x_{n+1}=r f(x_n)$ with $f(0)=f(1)=0$ (precise conditions are in their paper). They proved that as $r$ varies, the order in which stable periodic solutions appear is independent of the map. This order is the **universal sequence (U-sequence)**. So the algebraic form of $f$ is irrelevant and only its overall shape matters (p. 377). Up to period 6 it is

$$1,\ 2,\ 2\times2,\ 6,\ 5,\ 3,\ 2\times3,\ 5,\ 6,\ 4,\ 6,\ 5,\ 6.$$

- Periods 1, 2, 2×2 are the first period-doublings. Periods 6, 5, 3 are the large windows of Figure 10.6.2. 2×3 is the first doubling of the 3-cycle. The last six cycles lie in tiny windows (Exercise 10.6.5 gives their locations in the logistic map) (pp. 378–379).
- Simoyi et al. (1982) studied the Belousov–Zhabotinsky reaction in a stirred flow reactor. As the flow rate increased, periodic and chaotic states alternated. Within experimental resolution the periodic states occurred in exactly the U-sequence order (p. 379).
- The U-sequence fixes the order but not the parameter values (p. 379).

*Intuition note.* Many different formulas give the same "script" of cycles. What counts is that the map has one smooth hump.

**Quantitative universality (Feigenbaum).** Capsule history (p. 379). Around 1975 Feigenbaum studied period-doubling in the logistic map. He used a calculator to compute $r_n$, the r where a 2ⁿ-cycle first appears. The $r_n$ converged geometrically, with the distances shrinking by a factor of about 4.669. By his own account, he later computed the sine map and found the same rate, although his earlier theory assumed a quadratic nonlinearity (p. 379).

The same rate appears for any unimodal map, so
$$\delta=\lim_{n\to\infty}\frac{r_n-r_{n-1}}{r_{n+1}-r_n}=4.669\ldots$$
is universal. It is a new mathematical constant, "as basic to period-doubling as π is to circles" (p. 380). In Figure 10.6.3, with $\Delta_n=r_n-r_{n+1}$ (as printed), $\Delta_n/\Delta_{n+1}\to\delta$ (p. 380).

Scaling in x: let $x_m$ be the maximum of $f$ and $d_n$ the distance from $x_m$ to the nearest point of the 2ⁿ-cycle. Then
$$\frac{d_n}{d_{n+1}}\to\alpha=-2.5029\ldots,$$
independent of the precise form of $f$. The sign is negative because the nearest point alternates above and below $x_m$ (pp. 380–381).

Feigenbaum explained why α and δ are universal using renormalization from statistical physics. He found an analogy between α, δ and the universal exponents of second-order phase transitions (p. 381).

*Intuition note.* Each new period-doubling happens about 4.669 times closer (in r) than the last. The distance from the maximum to the nearest cycle point also shrinks by about 2.5 each time, alternating in sign. These numbers do not depend on the details of the unimodal map (for a quadratic maximum).

**Experimental tests.** Libchaber et al. (1982) heated liquid mercury from below. The control parameter is the Rayleigh number $R$ (dimensionless temperature gradient) (p. 381).
- For $R<R_c$ the fluid is motionless. For $R>R_c$ convection begins in counterrotating rolls. A further instability makes a wave run along the rolls, so the temperature oscillates (p. 381).
- A dc magnetic field stabilizes the roll structure, so the heat can be raised without destroying the spatial organization (pp. 381–382).
- Temperature time series (Figure 10.6.5): at $R/R_c=3.47$ the motion is period-1. At 3.52 odd and even peaks differ, which is period-2. Further doublings follow (p. 382).
- Libchaber et al. measured δ = 4.4 ± 0.1, in "reasonable agreement" with the theory. The text prints 4.699 here, apparently a misprint for 4.669 (p. 382; see Reading notes).
- Table 10.6.1: water 4 doublings, 4.3(8); mercury 4, 4.4(1); diode 4, 4.5(6); diode 5, 4.3(1); transistor 4, 4.7(3); Josephson simulator 3, 4.5(3). "4.3(8)" means 4.3 ± 0.8 (pp. 382–383).
- The measurements are difficult. Since δ ≈ 5, each bifurcation needs about a fivefold better control of the parameter, and noise blurs high-period orbits. In practice one cannot measure more than about five doublings (p. 383).

**What do 1-D maps have to do with science?** The worry: the theory has no physics, real systems have many degrees of freedom, and they run in continuous time (p. 383). The answer is built on the **Rössler system** (p. 383):
$$\dot x=-y-z,\qquad \dot y=x+ay,\qquad \dot z=b+z(x-c).$$
It has one nonlinear term, $zx$.
- With $a=b=0.2$ (Figure 10.6.6): $c=2.5$ gives a limit cycle. $c=3.5$ gives a cycle looping twice, with about twice the period. $c=4$ gives a four-loop cycle. $c=5$ gives a strange attractor after an infinite cascade of doublings (p. 384).
- Period-doubling of a cycle needs three or more dimensions, so the cycle has room not to cross itself (p. 384).
- Using Lorenz's trick, plot $x_{n+1}$ against $x_n$, where $x_n$ is the nth local maximum of $x(t)$. At $c=5$ the points fall very nearly on a one-dimensional unimodal curve (Figure 10.6.7) (pp. 384–385).
- The orbit diagram (all local maxima for each $c$, Figure 10.6.8) shows the period-doubling route and a large period-3 window (pp. 385–386).

Conclusion (p. 386): the theory applies if the system's Lorenz map is nearly one-dimensional and unimodal. This holds for Rössler and probably for Libchaber's mercury. The attractor must then be very flat (only slightly more than two-dimensional). That requires strong dissipation, with only two or three active degrees of freedom while the rest "follow along slavishly". The magnetic field adds damping, which favours low-dimensional chaos. The theory does not apply to fully turbulent fluids or fibrillating hearts, which have many active degrees of freedom in space and time (p. 386).

### 10.7 Renormalization (intuitive treatment, p. 386)
**Notation.** $f(x,r)$ is a unimodal map with a period-doubling route to chaos, $x_m$ its maximum. $r_n$ is where a 2ⁿ-cycle is born, and $R_n$ is where the 2ⁿ-cycle is superstable (p. 387).

**Example 10.7.1.** For $f(x,r)=r-x^2$:
- At $R_0$ the fixed point is superstable. The conditions are $x^*=R_0-(x^*)^2$ and $\lambda=\partial f/\partial x|_{x^*}=-2x^*=0$. So $x^*=0$ and $R_0=0$.
- At $R_1$ the 2-cycle $\{p,q\}$ has multiplier $(-2p)(-2q)=0$, so 0 is in the cycle. The condition $f^2(0,R_1)=R_1-(R_1)^2=0$ gives $R_1=1$, since the other root is a fixed point (p. 387).

General rule: a superstable cycle of a unimodal map always contains $x_m$. So $R_n$ is found where the horizontal line at $x_m$ meets the "figtree" (the orbit diagram). $R_n$ lies between $r_n$ and $r_{n+1}$, and numerically the $R_n$ spacings also shrink by δ ≈ 4.669 (p. 387, Figure 10.7.1).

**Self-similarity and renormalization.** The figtree's twigs look like earlier branches, scaled down in both $x$ and $r$ (p. 387). To express this, compare $f(x,R_0)$ and $f^2(x,R_1)$. Both have a superstable fixed point at $x_m$. Note that $r$ was shifted from $R_0$ to $R_1$. The small central box of $f^2(x,R_1)$ looks like $f(x,R_0)$ after rescaling and reversing both axes (Figure 10.7.2) (p. 388).

Shift the origin to $x_m$ (redefine $x\to x-x_m$ and subtract $x_m$ from $f$). Blow up by $|\alpha|>1$ and invert via a negative $\alpha$. This equals replacing $f^2(x,R_1)$ by $\alpha f^2(x/\alpha,R_1)$ (Exercise 10.7.2). Hence (pp. 388–389)
$$f(x,R_0)\approx\alpha f^2\!\left(\frac{x}{\alpha},R_1\right).$$
So $f$ is *renormalized* by taking its second iterate, rescaling $x\to x/\alpha$ and shifting $r$ to the next superstable value. Repeating, with $f^2(x/\alpha,R_1)\approx\alpha f^4(x/\alpha^2,R_2)$:
$$f(x,R_0)\approx\alpha^2f^4\!\left(\frac{x}{\alpha^2},R_2\right),\qquad f(x,R_0)\approx\alpha^nf^{(2^n)}\!\left(\frac{x}{\alpha^n},R_n\right).$$

Feigenbaum found numerically that
$$\lim_{n\to\infty}\alpha^nf^{(2^n)}\!\left(\frac{x}{\alpha^n},R_n\right)=g_0(x),\tag{1}$$
where $g_0$ is a **universal function** with a superstable fixed point. The limit exists only if $\alpha=-2.5029\ldots$ (p. 390).
- Why universal: $g_0$ depends on $f$ only through its behaviour near $x=0$, since only that survives in $x/\alpha^n$ as $n\to\infty$. The global shape is lost, so $g_0$ is independent of $f$ (almost) (p. 390).
- Caveat: the *order* of the maximum is never forgotten. $g_0$ is universal for all $f$ with a quadratic maximum (the generic case). A fourth-degree maximum gives a different $g_0$ (p. 390).
- Starting from $R_i$ instead gives $g_i(x)=\lim\alpha^nf^{(2^n)}(x/\alpha^n,R_{n+i})$, with a superstable $2^i$-cycle (p. 390).
- At the onset of chaos, $R_i=R_\infty$, no $r$-shift is needed: $f(x,R_\infty)\approx\alpha f^2(x/\alpha,R_\infty)$. The limit $g=g_\infty$ satisfies the self-referential functional equation
$$g(x)=\alpha g^2\!\left(\frac{x}{\alpha}\right).\tag{2}$$
- Boundary conditions: $g'(0)=0$ (maximum at 0). Also $g(0)=1$ without loss of generality, because if $g(x)$ solves (2) so does $\mu g(x/\mu)$ with the same α (Exercise 10.7.3) (p. 390).

**Solving for α.** At $x=0$, (2) gives $g(0)=\alpha g(g(0))$. With $g(0)=1$ this is $1=\alpha g(1)$, so
$$\alpha=1/g(1).$$
No closed form for $g$ is known, so use a power series (quadratic maximum assumed) $g(x)=1+c_2x^2+c_4x^4+\ldots$, matching powers of $x$ in (2). Feigenbaum (1979) used seven terms and found $c_2\approx-1.5276$, $c_4\approx0.1048$, $\alpha\approx-2.5029$. So the theory explains the observed α. The explanation of δ needs more advanced tools (operators in function space, Fréchet derivatives) and is not given (p. 391).

*Intuition note.* Zooming into the hump of $f^{2^n}$ with the right magnification gives, as $n\to\infty$, the same picture. That is why details of $f$ away from the maximum do not matter (the order of the maximum does). The magnification factor α is forced by the self-consistency of this picture.

**Renormalization for pedestrians** (modified from May and Oster 1980 and Helleman 1980; approximate, p. 391). Suppose the period-2 cycle is born at $x=0$ when $\mu=0$. Near there, since the eigenvalue is −1 at the bifurcation, $x_{n+1}=-(1+\mu)x_n+ax_n^2+\ldots$. Higher-order terms are neglected, so results are approximate. Rescaling $x\to x/a$ sets $a=1$:
$$x_{n+1}=-(1+\mu)x_n+x_n^2+\ldots\tag{3}$$
Idea: the period-2 points $p,q$ will themselves period-double, and near that bifurcation $f^2$ has the same algebraic form (3). Compute the map for $f^2$ near $p$ and renormalize it into (3) (p. 391).

Steps (p. 392):
- Period-2 means $p=-(1+\mu)q+q^2$ and $q=-(1+\mu)p+p^2$. Subtracting and factoring out $p-q$ gives $p+q=\mu$. Multiplying gives $pq=-\mu$. So
$$p=\frac{\mu+\sqrt{\mu^2+4\mu}}{2},\qquad q=\frac{\mu-\sqrt{\mu^2+4\mu}}{2}.$$
- Shift the origin to $p$ (a fixed point of $f^2$). Expanding $p+\eta_{n+1}=f^2(p+\eta_n)$ (algebra left to Exercise 10.7.10) gives
$$\eta_{n+1}=(1-4\mu-\mu^2)\eta_n+C\eta_n^2+\ldots\tag{4}$$
$$C=4\mu+\mu^2-3\sqrt{\mu^2+4\mu}.\tag{5}$$
- Rescale $\tilde x_n=C\eta_n$:
$$\tilde x_{n+1}=(1-4\mu-\mu^2)\tilde x_n+\tilde x_n^2+\ldots\tag{6}$$
- Define $\tilde\mu$ by $-(1+\tilde\mu)=1-4\mu-\mu^2$. Then
$$\tilde x_{n+1}=-(1+\tilde\mu)\tilde x_n+\tilde x_n^2+\ldots\tag{7}$$
$$\tilde\mu=\mu^2+4\mu-2.\tag{8}$$
Both steps anticipated in the abstract theory appear: rescale the state and shift the parameter (p. 392).

When $\tilde\mu=0$ the renormalized map has a flip bifurcation, which means the 2-cycle gives birth to a 4-cycle (p. 393).

**Example 10.7.2.** Period 4 is born when $\mu^2+4\mu-2=0$, so $\mu=-2+\sqrt6$ (the other root is negative and irrelevant). The origin of $\mu$ is the birth of period 2, at $r=3$ for the logistic map. So $r_2=3+(-2+\sqrt6)=1+\sqrt6$, which agrees with the author's Example 10.3.3 (p. 393).

**Iterating.** Let $\mu_k$ be where the original map (3) gives birth to a 2ᵏ-cycle, with $\mu_1=0$ and $\mu_2=-2+\sqrt6\approx0.449$. Then
$$\mu_{k-1}=\mu_k^2+4\mu_k-2,\tag{9}$$
equivalently the forward iteration
$$\mu_k=-2+\sqrt{6+\mu_{k-1}}.\tag{10}$$
Starting from $\mu_1=0$, $\mu_k\to\mu^*>0$, a stable fixed point corresponding to the onset of chaos (Exercise 10.7.11) (p. 393).

**Example 10.7.3.** The fixed point of (9) satisfies $\mu^*=(\mu^*)^2+4\mu^*-2$, so
$$\mu^*=\tfrac12\left(-3+\sqrt{17}\right)\approx0.56.\tag{11}$$
On the logistic map $\mu=0$ is $r=3$, so $r_\infty\approx3.56$, against the numerical value $r_\infty\approx3.57$ (p. 394).

**Approximate δ and α** (p. 394).
- For large $k$, $\mu_k$ converges geometrically to $\mu^*$, so $\delta\approx(\mu_{k-1}-\mu^*)/(\mu_k-\mu^*)$. This is 0/0 as $k\to\infty$, so use L'Hôpital's rule with (9):
$$\delta\approx\frac{d\mu_{k-1}}{d\mu_k}\Big|_{\mu=\mu^*}=2\mu^*+4=1+\sqrt{17}\approx5.12.$$
This is about 10 percent above the true 4.67.
- $C$ plays the role of α, since $\tilde x_n=C\eta_n$ is the rescaling. Substituting $\mu^*$ into (5):
$$C=\frac{1+\sqrt{17}}{2}-3\left[\frac{1+\sqrt{17}}{2}\right]^{1/2}\approx-2.24,$$
which the author says is also within 10 percent of the true α ≈ −2.50.

*Intuition note.* Near each period-doubling, "double the map, zoom in, re-tune the knob" gives back the same form of map. The knob values then obey the simple recursion (9). Its fixed point is the onset of chaos and its slope there gives (in this approximation) the shrink factor δ ≈ 5.12.

### Exercises for Chapter 10 (pp. 394–404)
The exercises cover calculator experiments with maps, cobwebs, Newton's method and superstability (10.1), orbit diagrams of other maps (10.2), analysis of logistic, quadratic, cubic and shift maps (10.3), periodic windows and iteration patterns (10.4), Lyapunov exponents and the tent map (10.5), numerical estimation of δ and cycle patterns (10.6), and renormalization including the intermittency case (10.7).

## Toy example (ours, not from the text)
Iterate the pedestrian recursion (10) by hand: $\mu_k=-2+\sqrt{6+\mu_{k-1}}$, $\mu_1=0$.
- $\mu_2=-2+\sqrt6=-2+2.4495=0.4495$.
- $\mu_3=-2+\sqrt{6.4495}=-2+2.5396=0.5396$.
- $\mu_4=-2+\sqrt{6.5396}=-2+2.5573=0.5573$.
- $\mu_5=-2+\sqrt{6.5573}=-2+2.5607=0.5607$.

Differences: $\mu_2-\mu_1=0.4495$, $\mu_3-\mu_2=0.0901$, $\mu_4-\mu_3=0.0177$, $\mu_5-\mu_4=0.0034$. Successive ratios: $0.4495/0.0901\approx4.99$ and $0.0901/0.0177\approx5.09$. They approach the predicted $\delta\approx5.12$, and the values approach $\mu^*\approx0.5616$ (this uses $\mu^*=(-3+\sqrt{17})/2$ with $\sqrt{17}\approx4.1231$). (added step) The last ratio, $0.0177/0.0034\approx5.2$, is dominated by rounding. So the ratio of successive shrinkings is nearly constant, which is the geometric convergence behind δ.

## Concepts
- [[period-doubling-route-to-chaos]] — cascade of 2ⁿ-cycles ending in chaos, seen in maps, the Rössler flow and experiments (p. 377, p. 384)
- [[universality]] — in this unit: the order of cycles, δ and α are the same for all unimodal maps (with quadratic maximum for the constants); the author draws an analogy with phase-transition exponents (pp. 377, 380–381)
- [[unimodal-map]] (new) — smooth map, concave down, one maximum, with f(0)=f(1)=0 in the Metropolis et al. theorem (p. 377)
- [[u-sequence]] (new) — the universal order of stable periodic attractors in unimodal maps (p. 377)
- [[feigenbaum-constants]] (new) — δ = 4.669… (r-direction ratio) and α = −2.5029… (x-direction ratio, defined via d_n/d_{n+1}) (pp. 380–381)
- [[superstable-cycle]] (new) — cycle with multiplier 0; always contains x_m for a unimodal map (p. 387)
- [[renormalization]] (new) — iterate f twice, rescale x by α, shift r to the next superstable value, repeat (p. 389)
- [[functional-equation-g]] (new) — g(x) = αg²(x/α), g(0)=1, g′(0)=0, describing the limit at the onset of chaos (p. 390)
- [[lorenz-map]] (new) — plot of successive local maxima x_{n+1} against x_n for a flow; used to reduce the Rössler flow to a 1-D map (pp. 384–385)
- [[lyapunov-exponent]] — here read off for the logistic map: negative before r∞, positive in chaos, −∞ at superstable cycles (p. 376)
- [[strange-attractor]] — the Rössler attractor at c = 5; must be very flat for a nearly 1-D Lorenz map (pp. 384, 386)
- [[bifurcation]] — period-doubling (flip) bifurcations of cycles; for flows they need three or more dimensions (p. 384)

## Canonical instances
- [[sine-map-vs-logistic-map]] — two different formulas, same qualitative orbit diagram (pp. 376–378)
- [[belousov-zhabotinsky-u-sequence]] — periodic states in the U-sequence order in a stirred-flow reactor (p. 379)
- [[libchaber-convection-experiment]] — mercury convection with magnetic field gives period-doubling, δ = 4.4 ± 0.1 (pp. 381–382)
- [[rossler-system]] — three ODEs with one nonlinear term, period-doubling to a strange attractor with a 1-D-like Lorenz map (pp. 383–386)
- [[pedestrian-renormalization-logistic]] — algebraic renormalization giving r∞ ≈ 3.56, δ ≈ 5.12, α ≈ −2.24 (pp. 391–394)

## Bridges (candidates)
- [structural-analogy] Renormalization at period-doubling ↔ statistical physics: the author says α, δ are analogous to universal exponents at second-order phase transitions (p. 381). Both rely on repeated rescaling and loss of microscopic detail.
- [structural-analogy] Universality of δ ↔ universality (grad concept): different systems share macro behaviour near a transition. Here the systems are different unimodal maps.
- [metaphor] "Only two or three degrees of freedom are truly active; the rest follow slavishly" (p. 386) ↔ hierarchy and near-decomposability (fast variables slaved to slow ones).
- [structural-analogy] Slow convergence to a cycle on the verge of period-doubling (Exercise 10.6.1, p. 401) ↔ critical slowing down before a tipping point.

## Questions this raises
- What is the exact link between the conditions of the Metropolis et al. theorem and real systems whose return map is only nearly unimodal?
- Why does the order of the maximum (quadratic vs quartic) change the constants, and by how much (Exercise 10.7.7)?
- How could one measure α or δ more accurately when experiments reach only about five doublings?
- What replaces this theory for systems with many active degrees of freedom, such as turbulence (p. 386)?

## Exercises worth doing
- Ex. 10.1.13 (p. 395) — roots of g(x)=0 correspond to superstable fixed points of Newton's map; explains the fast convergence — difficulty: medium
- Ex. 10.3.5 (p. 397) — conjugacy: logistic and quadratic maps are the same dynamics in other variables — difficulty: easy
- Ex. 10.3.10 (p. 398) — exact solutions of the logistic map at r = 4 via the binary shift map — difficulty: medium
- Ex. 10.6.2 (p. 401) — estimating δ with superstable R_n avoids critical slowing down — difficulty: medium
- Ex. 10.7.5 (p. 403) — crudest estimate of α by matching O(x²) coefficients — difficulty: easy
- Ex. 10.7.8 (p. 403) — renormalization applied to intermittency near a tangent bifurcation — difficulty: hard

## Reading notes
- This part starts on printed p. 376, in the middle of an example about the Lyapunov exponent of the logistic map (Figure 10.5.2). The example heading is not on these pages. It ends on p. 404 with Exercise 10.7.11, so it includes Sections 10.6 and 10.7 and the chapter exercises printed on pp. 394–404. It does not start at a section boundary.
- Printed page = pdf page − 19.
- Misprint: on p. 382 the text gives the theoretical value "δ ≈ 4.699". Elsewhere in this part the value is 4.669 (or 4.67), so 4.699 is presumably a typo.
- On p. 380, Δₙ is printed as $r_n-r_{n+1}$, which is negative if the $r_n$ increase. The ratio Δₙ/Δₙ₊₁ is still positive.
- The text layer was garbled for many symbols (λ, δ, α, μ, exponents). All equations were checked against the page images. Figure 10.6.2 is credited "Courtesy of Andy Christian".
- Example 10.7.2 refers to Example 10.3.3 (a different part of the book), which is not in this unit. The claim that $r_2=1+\sqrt6$ there is reported only as the author states it.
