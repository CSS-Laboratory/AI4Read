---
id: strogatz-2024-nonlinear/ch12-strange
work: strogatz-2024-nonlinear
unit: "12 Strange Attractors"
pages: 429–459
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
# Strange Attractors (Strogatz, ch. 12)

## L0 — One line
The basic mechanism behind strange attractors is repeated stretching and folding of phase space, which the chapter shows in simple maps (baker's, Hénon), in the Rössler flow, and in real experiments (a chemical reaction, a driven beam).

## L1 — The gist (≤ 120 words)
Earlier chapters showed that chaos exists but not why. How can trajectories separate exponentially fast and yet stay bounded? The chapter's answer is stretching (sensitive dependence), folding (boundedness) and, in dissipative (volume-shrinking) systems, contraction. This gives a layered, Cantor-like (separated layers) fractal cross section. The pastry, baker's and Hénon maps and the Rössler flow make this concrete. Two experiments then show real strange attractors. Attractor reconstruction (rebuilding the attractor from delayed copies) recovers the Belousov–Zhabotinsky (BZ) chemical attractor from one time series. The driven double-well beam shows Poincaré sections (slices of the flow), transient chaos and fractal basin boundaries. This matters because it explains chaos geometrically and gives standard tools for experimental data.

**Prerequisites:** 2D maps and Jacobian determinants; fixed points and limit cycles; box dimension and Cantor sets; the Lorenz system; the logistic map and period doubling.

## L2 — Key ideas (5–10 bullets)
- Strange attractors combine boundedness with exponential divergence (at least initially) through repeated stretching and folding. Contraction in other directions reflects dissipation (p. 430).
- The pastry map and the baker's map show the fractal structure: the attractor is locally a smooth curve (or ribbon) times a Cantor set (pp. 431–434; the ribbon version for the Rössler flow is on p. 442).
- For $a<\tfrac12$ the baker's map contracts area, has a fractal attractor of box dimension $1+\ln\tfrac12/\ln a$ and attracts all orbits. At $a=\tfrac12$ it preserves area and has no attractor (pp. 433–435).
- The Hénon map is an invertible, constant-dissipation 2D map ($\det\mathbf J=-b$) built from stretch–fold–reflect steps. At $a=1.4$, $b=0.3$ it shows self-similar fine structure (pp. 435–440).
- The Rössler flow stretches by spiralling out, folds through the third dimension and re-injects. This explains why a chaotic flow needs three dimensions (p. 441).
- The claim behind attractor reconstruction is that, for systems governed by an attractor, time delays let a single time series reveal it (p. 444). Roux et al. used it to establish chemical chaos in the BZ reaction (pp. 443–445).
- Reconstruction needs a choice of embedding dimension and delay, and, the author warns, much research claiming chaos in stock prices, brain waves, heart rhythms or sunspots is dubious (pp. 446–447).
- In the forced double-well oscillator, a Poincaré section resolves the tangled motion into a fractal cross section of a strange attractor, and the model also shows transient chaos and fractal basin boundaries (pp. 448–453).

## L3 — Walkthrough

### 12.0 Introduction (p. 429)
Earlier chapters show *what* happens in chaos, not *why*. Questions: what causes sensitive dependence, and how does a differential equation produce a fractal attractor? Around 1976 only the Lorenz attractor and Smale's constructions were known. Hénon and Rössler (1976) supplied transparent examples using stretching and folding. The chapter ends with experimental examples that illustrate attractor reconstruction and Poincaré sections (p. 429).

### 12.1 The Simplest Examples (pp. 429–435)
**Puzzle.** On a strange attractor, trajectories stay in a bounded region but separate exponentially fast, at least initially (p. 429). **Mechanism:** the flow contracts a blob in some directions (dissipation) and stretches it in others (sensitive dependence). Stretching cannot continue forever, so the blob is folded back on itself (p. 430).

**Pastry map (Figs. 12.1.2–12.1.3).** A rectangle is flattened, stretched and folded into a horseshoe $S_1$. Then $S_1$ goes to $S_2$, and so on. At each stage the layers are thinner and there are twice as many (p. 431). The limit set $S_\infty$ has infinitely many smooth layers with gaps of various sizes. A vertical cross section resembles a Cantor set. So $S_\infty$ is locally the product of a smooth curve and a Cantor set (p. 431). A drop of food colouring spreads through the dough, which gives sensitive dependence (p. 430).

*Terminology.* Strogatz calls this the *pastry map*. He reserves "horseshoe" for Smale's horseshoe, which has no strange attractor; its invariant set is "more like a strange saddle" (p. 431).

**Example 12.1.1 — baker's map** on the unit square, with $0<a\le\tfrac12$:
$$(x_{n+1},y_{n+1})=\begin{cases}(2x_n,\ a y_n) & 0\le x_n\le \tfrac12\\[2pt] (2x_n-1,\ a y_n+\tfrac12) & \tfrac12\le x_n\le 1\end{cases}$$
Geometry: stretch to a $2\times a$ rectangle, cut it in half, and stack the right half on the left at height $y=\tfrac12$ (p. 432). Justification: on the left half $x$ is doubled and $y$ is multiplied by $a$. On the right half the image is the same plus the shift $(-1,\tfrac12)$, which is the stacking (p. 432). The map has sensitive dependence from the $x$-stretching and uncountably many chaotic orbits (p. 432).

**Example 12.1.2 — attractor for $a<\tfrac12$.** Let $S$ be the square. $B^n(S)$ consists of $2^n$ horizontal strips of height $a^n$; $B(S)$ has two strips of height $a$ (p. 433). The limit $A=B^\infty(S)$ is a Cantor set of line segments. To show it exists: $B^{n+1}(S)\subset B^n(S)$ (nested, "Chinese boxes") and each $B^n(S)$ is compact. A nested family of compact sets has a non-empty compact intersection (Munkres 1975). This is $A$, and $A\subset B^n(S)$ for all $n$ (p. 433). Attraction: $B^n(x_0,y_0)$ lies in a strip of $B^n(S)$, and every point of those strips is within $a^n$ of $A$. Since $a^n\to0$, the distance to $A$ tends to $0$ (p. 433).

**Example 12.1.3 — box dimension.** Cover $A$ with boxes of side $\varepsilon=a^n$. Each strip (length 1) needs about $a^{-n}$ boxes and there are $2^n$ strips, so $N\approx a^{-n}\,2^n=(a/2)^{-n}$. Then
$$d=\lim_{\varepsilon\to0}\frac{\ln N}{\ln(1/\varepsilon)}=\lim\frac{\ln[(a/2)^{-n}]}{\ln(a^{-n})}=1+\frac{\ln\frac12}{\ln a}.$$
Check: $d\to2$ as $a\to\tfrac12$, since the attractor fills more of $S$ (p. 434).

*Intuition note.* The attractor is made of long strips, so it has dimension 1 along the strips. The Cantor-like stack of strips adds a fractional part. When the strips are thick enough to leave no gaps ($a=\tfrac12$), the fractional part reaches 1 and the set fills the whole square.

**Importance of dissipation.** For any region $R$, $\text{area}(B(R))=2a\times\text{area}(R)$; cutting does not change area. So for $a<\tfrac12$ the map contracts area, which is the analog of volume contraction in the Lorenz equations (Section 9.2). It follows that the attractor has zero area and the map has no repelling fixed points (p. 434). For $a=\tfrac12$ the map is area-preserving and $S$ maps onto itself with no gaps. Transients never decay, and orbits shuffle around the square without settling onto a lower-dimensional attractor (pp. 434–435). In general a map or flow that contracts volumes is *dissipative* (friction, viscosity). Area-preserving maps go with conservative, Hamiltonian systems. Area-preserving maps cannot have attractors, because an attractor must attract all orbits from a small open set around it (Section 9.3) and that is incompatible with area preservation (p. 435).

### 12.2 Hénon Map (pp. 435–440)
Hénon (1976) wanted to resolve the thin sheets of the Lorenz attractor. After one circuit, volumes shrink by a factor of about 14,000 (Lorenz 1963), which makes numerics hard. He sought a map with the essential features and adjustable dissipation. Maps are faster to simulate and can be followed more accurately and for longer (p. 435).
$$x_{n+1}=y_n+1-ax_n^2,\qquad y_{n+1}=bx_n\tag{1}$$
**Construction (Fig. 12.2.1).** Start with a rectangle elongated along $x$. Then apply:
- $T'$: $x'=x,\ y'=1+y-ax^2$ (primes denote iteration, not derivatives). It stretches and folds; the top and bottom become parabolas, and $a$ controls folding.
- $T''$: $x''=bx',\ y''=y'$ with $-1<b<1$ (contract along $x$).
- $T'''$: $x'''=y'',\ y'''=x''$ (reflect across $y=x$).

The composite $T=T'''T''T'$ is map (1) (p. 436).

**Properties.** (1) *Invertible*, unlike the logistic map, whose points (except the maximum) have two pre-images. This mirrors the unique trajectory through each point in Lorenz. (2) *Dissipative*, with the same contraction everywhere (analog of the constant negative divergence in Lorenz). (3) For certain parameters there is a *trapping region* containing the attractor (Fig. 12.2.2; Ex. 12.2.9). (4) Some trajectories *escape to infinity*, unlike Lorenz, because far from the origin the quadratic term dominates and repels orbits (pp. 436–437).

**Example 12.2.1 — inverse.** Solving (1) for $x_n,y_n$ gives
$$x_n=b^{-1}y_{n+1},\qquad y_n=x_{n+1}-1+ab^{-2}(y_{n+1})^2,$$
so $T^{-1}$ exists for all $b\ne0$ (p. 437).

**Example 12.2.2 — area contraction.** For a map $x_{n+1}=f(x_n,y_n)$, $y_{n+1}=g(x_n,y_n)$ the Jacobian is
$$\mathbf J=\begin{pmatrix}\partial f/\partial x&\partial f/\partial y\\ \partial g/\partial x&\partial g/\partial y\end{pmatrix}.$$
If $|\det\mathbf J|<1$ everywhere, the map contracts area. Reason: an infinitesimal rectangle of area $dx\,dy$ goes to a parallelogram of area $|\det\mathbf J|\,dx\,dy$. For Hénon, $f=1-ax^2+y$ and $g=bx$, so
$$\mathbf J=\begin{pmatrix}-2ax&1\\ b&0\end{pmatrix},\qquad \det\mathbf J=-b.$$
So for $-1<b<1$ every region's area shrinks by the constant factor $|b|$ per iteration (p. 438).

**Choosing parameters.** $b$ should not be too close to 0 (excess contraction hides the fine structure). If $b$ is too large the folding is too weak, because $b$ also produces extra folding. A good choice is $b=0.3$ (p. 438). For $a$ too small or too large all trajectories escape. For intermediate $a$, trajectories escape or approach an attractor depending on initial conditions. As $a$ grows the attractor goes from a stable fixed point to a stable 2-cycle, then period doubling to chaos, then chaos with periodic windows. Hénon chose $a=1.4$ (p. 438).

**Zooming in.** With $a=1.4$, $b=0.3$, Hénon computed ten thousand iterates starting from the origin. The attractor is boomerang-shaped, made of parallel curves (Fig. 12.2.3a). Enlargement shows what seem to be six curves grouped 1, 2, 3. Enlarging the three curves shows six curves grouped again 1, 2, 3, and so on. The self-similarity continues to arbitrarily small scales (p. 439).

**Unstable manifold.** The attractor seems Cantor-like transversally and smooth longitudinally. It is closely related to the unstable manifold of a saddle point on its edge. Benedicks and Carleson (1991) proved that the attractor is the closure of a branch of this manifold. Hobson (1993) computed the manifold very accurately, and it is indistinguishable from the attractor (p. 440).

*Intuition note.* The Hénon map was built to copy the main features of the Lorenz system (stretch-and-fold, contraction) in a simple map whose dissipation $|b|$ you can tune. Because $|\det\mathbf J|=|b|$ everywhere, area shrinks by the same factor at every point.

### 12.3 Rössler System (pp. 440–442)
Rössler found inspiration in a taffy-pulling machine. His system has only one quadratic nonlinearity, $xz$:
$$\dot x=-y-z,\qquad \dot y=x+ay,\qquad \dot z=b+z(x-c)\tag{1}$$
It has a period-doubling route to chaos as $c$ increases (Section 10.6). With $a=b=0.2$, $c=5.7$ numerical integration shows a strange attractor (p. 441). Trajectories separate by spiralling out (*stretching*). They then cross without intersecting by going into the third dimension (*folding*), and circulate back near their start (*re-injection*). This is why a chaotic flow needs three dimensions (p. 441).

Following Abraham and Shaw: near a trajectory there is compression toward the attractor and divergence along it. The expanding sheet is folded in two and bent around to nearly join the narrow part. One sheet becomes two after a circuit, then four, then eight, and so on (Figs. 12.3.3–12.3.4). So the flow acts like the pastry transformation with phase space as the dough (pp. 441–442).

**Poincaré section** (a plane slice, Fig. 12.3.5). A further one-dimensional slice shows an infinite set of dots separated by gaps of various sizes, a topological Cantor set. Each dot is one layer. The model is a Cantor set of surfaces: locally topologically equivalent to the Cartesian product of a ribbon and a Cantor set, as the pastry map suggested (p. 442).

### 12.4 Chemical Chaos and Attractor Reconstruction (pp. 443–447)
**BZ reaction.** Malonic acid is oxidized in acid by bromate ions, with or without a catalyst. It is known to show limit-cycle oscillations. Schmitz et al. (1977) first reported chemical chaos, but some chemists suspected uncontrolled fluctuations in control parameters (p. 443). Roux, Simoyi, Wolf and Swinney used a continuous-flow stirred tank reactor. Fresh chemicals are pumped in at a constant flow rate (the control parameter) to stay far from equilibrium. Stirring enforces spatial homogeneity, which reduces the effective number of degrees of freedom. They measured the bromide concentration $B(t)$ (Fig. 12.4.1). It looks periodic but its amplitude is erratic (p. 443).

**Reconstruction.** Only one variable is measured, but the reaction has at least twenty other species (p. 444). Packard et al. (1980) and Takens (1981) gave the method. The claim is that, for systems governed by an attractor, the full phase-space dynamics can be reconstructed from a single time series, using time delays. Define $\mathbf x(t)=(B(t),B(t+\tau))$ with $\tau>0$. With $\tau=8.8$ s the data trace a strange attractor resembling Rössler's (Fig. 12.4.2). In three dimensions, $\mathbf x(t)=(B(t),B(t+\tau),B(t+2\tau))$ (p. 444).

**Evidence chain (Roux et al.).**
1. A Poincaré section, taken with a plane roughly normal to the orbits, falls within resolution on a one-dimensional curve. So the attractor is approximately a two-dimensional sheet (p. 444).
2. Successive values $X_n$ of $B(t+\tau)$ at the crossings give a smooth one-dimensional map $X_{n+1}$ vs $X_n$ (Fig. 12.4.3). Within experimental resolution the data fall on a smooth curve, which confirms that the aperiodic behaviour is governed by deterministic laws: given $X_n$, the map determines $X_{n+1}$ (p. 444).
3. The map is unimodal, like the logistic map. This suggests period doubling, which was found experimentally (Coffman et al. 1987; Fig. 12.4.4) (p. 444).
4. Past the onset of chaos, periodic windows occurred as flow rate varied in the order predicted by the U-sequence (Section 10.6) (p. 445).

Together these demonstrate deterministic chaos in a nonequilibrium chemical system. It is understood largely via 1D maps although the kinetics are at least twenty-dimensional. But universality theory works only because the attractor is nearly a 2D surface. That low dimension comes from continuous stirring and strong dissipation. Higher-dimensional phenomena such as chemical turbulence remain beyond the theory (p. 445).

**Practical issues** (p. 446):
- *Embedding dimension* (number of delays): enough are needed for the attractor to disentangle itself. The usual approach is to increase the dimension and compute the correlation dimension, which levels off at the "true" value once the dimension is large enough. The method fails if the dimension is too large, because sparse data cause sampling problems, which limits dimension estimates for high-dimensional attractors.
- *Delay $\tau$*: for noisy real data the optimum is typically about one-tenth to one-half of the mean orbital period.

**Example 12.4.1.** Take a limit cycle with $x(t)=\sin t$ and $\mathbf x(t)=(x(t),x(t+\tau))$. For $0<\tau<\pi/2$ the trajectory is an ellipse with long axis on the diagonal. At $\tau=\pi/2$ it is a circle, since $x=\sin t$ and $y=\sin(t+\pi/2)=\cos t$. For larger $\tau$ it is an ellipse with long axis along $y=-x$ (Fig. 12.4.5; the book shows $\tau=\pi/6,\ \pi/2,\ 5\pi/6$). Each is a closed curve, a topologically faithful limit cycle. The best delay is $\tau=\pi/2$, one quarter of the period, because the reconstruction is then most "open". Narrow cigar shapes blur more easily with noise (pp. 446–447).

*Intuition note.* A delayed copy of one variable acts as a second coordinate. Roux et al. found that such a pair can show the attractor's shape, and the author notes that the method works there because the attractor is nearly a 2D surface (p. 445). In the sine example a small delay gives a narrow cigar-shaped curve along the diagonal, which noise blurs more easily.

**Chaos versus noise.** In principle, as embedding dimension increases the correlation dimension levels off for chaos but keeps increasing for noise. Lorenz called reconstruction the most surprising development. Strogatz warns that much research on chaos in stock prices, brain waves, heart rhythms or sunspots is dubious (cites Kaplan and Glass 1993) (p. 447).

### 12.5 Forced Double-Well Oscillator (pp. 447–453)
Forced (nonautonomous) systems turn up many strange attractors (p. 447).

**Magneto-elastic system** (Moon and Holmes 1979; Fig. 12.5.1). A steel beam is clamped in a rigid frame. Two magnets pull it in opposite directions, so it buckles to one side or the other (two locally stable states, separated by the unstable straight position). The frame is shaken sideways, and $x(t)$ is the tip's displacement. With weak forcing the beam vibrates near one magnet. As forcing slowly increases, it suddenly starts whipping back and forth erratically. The motion lasts for hours, tens of thousands of drive cycles (p. 448).

**Double-well analog.** A damped particle in a double-well potential, shaken periodically (Fig. 12.5.2). Physical expectation: weak shaking gives small oscillations in one well. We can imagine at least two stable oscillations, small-amplitude in one well and large-amplitude across the hump; the choice between them probably depends on initial conditions. Very strong shaking always flings the particle across the hump. An intermediate regime, with barely enough energy to reach the hump top, "seems potentially chaotic" (p. 449).

**Model** (Moon–Holmes), dimensionless:
$$\ddot x+\delta\dot x-x+x^3=F\cos\omega t\tag{1}$$
with $\delta>0$ the damping, $F$ the forcing strength and $\omega$ the frequency. It is Newton's law in the potential $V(x)=\tfrac14x^4-\tfrac12x^2$. The force $F\cos\omega t$ is an inertial force from the moving frame, with $x$ measured relative to that frame (p. 449). Throughout, $\delta=0.25$, $\omega=1$, and $F$ is varied (p. 450).

**Example 12.5.1** ($F=0.18$). Numerical integration converges to periodic solutions (Fig. 12.5.3). There are two limit cycles besides the two shown, and possibly others, all confined to a single well (p. 450).

**Example 12.5.2** ($F=0.40$, $(x_0,y_0)=(0,0)$, $y=\dot x$). $x(t)$ and $y(t)$ look aperiodic (Fig. 12.5.4), suggesting chaos at least for these initial conditions, and $x$ changes sign repeatedly. The plot of $x$ vs $y$ is messy (Fig. 12.5.5). It is not a true phase portrait: the state is $(x,y,t)$, so the plot is a 2D projection of a 3D trajectory (pp. 450–451).

**Poincaré section.** Plot $(x(t),y(t))$ whenever $t$ is an integer multiple of $2\pi$ ("strobing" at the same phase in each drive cycle). The tangle resolves into a fractal set, a cross section of a strange attractor (Fig. 12.5.6). Points hop erratically over it, with sensitive dependence. Simulation and experiment agree qualitatively (Fig. 12.5.7) (pp. 451–452). (The text says "the system of Example 12.5.1", but that example has only limit cycles; the chaotic case is Example 12.5.2, so the figure presumably belongs to it, though the pages do not say; see Reading notes.)

**Transient chaos.** Even with no strange attractor, if two or more stable limit cycles coexist there can be chaotic transients, and the final state depends sensitively on initial conditions (Moon–Li 1985; Grebogi et al. 1983b) (p. 452).

**Example 12.5.3** ($F=0.25$). The start $(x_0,y_0)=(0.2,0.1)$ gives a chaotic transient, then a periodic state with $x>0$: small oscillations in the right well. Changing $x_0$ to $0.195$ gives a final state in the left well (Fig. 12.5.8). The author suggests starting points near the "ghost" of the strange attractor (p. 453).

**Fractal basin boundaries.** Colour each initial condition in a $900\times900$ grid by its fate (blue = left well, red = right well). Color plate 3 shows large single-colour patches. Between them the slightest change in initial conditions alternates the final state. Magnification shows intermingling down to arbitrarily small scales, so the basin boundary is a fractal. Near it long-term prediction is essentially impossible (p. 453). (The colour plates are not in these pages.)

*Intuition note.* Sensitivity to initial conditions can occur even when every long-term outcome is simple. If two simple outcomes have intertwined, infinitely fine basin boundaries, you cannot predict which one a nearby start will reach.

## Toy example (ours, not from the text)
Baker's map with $a=\tfrac14$.

*Dimension.* $N\approx(a/2)^{-n}=8^n$ boxes of side $\varepsilon=4^{-n}$. So $d=\ln 8^n/\ln 4^n=3\ln2/(2\ln2)=1.5$. The formula gives $1+\ln\frac12/\ln\frac14=1+\tfrac12=1.5$. Area factor: $2a=0.5$. After $n=2$ there are 4 strips of height $1/16$, with total height $1/4=(2a)^2$.

*Sensitive dependence.* Take $P=(0.1,0.5)$ and $Q=(0.11,0.5)$.
- Step 1: $P\to(0.2,\,0.125)$, $Q\to(0.22,\,0.125)$.
- Step 2: $P\to(0.4,\,0.03125)$, $Q\to(0.44,\,0.03125)$.
- Step 3: $P\to(0.8,\,0.0078125)$, $Q\to(0.88,\,0.0078125)$.
- Step 4: both have $x>\tfrac12$. $P\to(0.6,\ 0.25\cdot0.0078125+0.5=0.501953125)$ and $Q\to(0.76,\,0.501953125)$.
- Step 5: $P\to(0.2,\,0.625488\ldots)$, $Q\to(0.52,\,0.625488\ldots)$.
- Step 6: $P$ has $x=0.2<\tfrac12$, so $P\to(0.4,\,0.156372\ldots)$. $Q$ has $x=0.52>\tfrac12$, so $Q\to(0.04,\,0.656372\ldots)$.

The $x$-gap grows $0.01,0.02,0.04,0.08,0.16,0.32,0.36$ (doubling each step, then wrapped), while the $y$-gap is $0$ until the points fall on different halves at step 6, when it becomes $0.5$. The $x$-doubling is the stretch and the cut-and-stack is the fold. The $y$ shrinking by $a$ is the contraction.

## Concepts
- [[strange attractor / fractal]] — bounded attractor, locally a smooth sheet/curve times a Cantor set, with sensitive dependence (pp. 429–431)
- [[stretching-and-folding]] (new) — the mechanism: stretch gives divergence, fold keeps the dynamics bounded (p. 429)
- [[deterministic chaos]] — bounded aperiodic behaviour; here shown to come from deterministic maps or flows (p. 432)
- [[dissipative vs area-preserving]] (new) — dissipative systems contract phase-space volume and can have attractors; area-preserving ones cannot (pp. 434–435)
- [[attractor / basin of attraction]] — set approached by orbits, and its set of initial conditions; basin boundaries can be fractal (pp. 433, 453)
- [[Poincaré section]] (new) — slice of a flow, or stroboscopic sampling of a forced system, that exposes an attractor's cross section (pp. 442, 451)
- [[attractor reconstruction]] (new) — building a phase-space trajectory from delayed copies of one time series (p. 444)
- [[transient chaos]] (new) — complicated motion before settling onto a non-chaotic attractor (p. 452)
- [[fractal basin boundary]] (new) — basin boundary with structure at all scales, so the final state is unpredictable near it (p. 453)
- [[period-doubling route to chaos]] — appears in Hénon, Rössler and BZ data (pp. 438, 441, 444)
- [[limit cycle]] — periodic attractors in the double-well simulations; reconstructed in the sin example (pp. 446, 450)
- [[universality]] — the 1D unimodal-map predictions (U-sequence) hold for the BZ data (p. 445)

## Canonical instances
- [[pastry-map]] — stretching and folding gives layered Cantor structure (p. 430)
- [[baker's-map]] — dissipative ($a<\tfrac12$) fractal attractor vs area-preserving ($a=\tfrac12$) (pp. 432–435)
- [[henon-map]] — 2D invertible map with a fractal attractor (pp. 435–440)
- [[rossler-system]] — chaotic flow with one nonlinear term (pp. 440–442)
- [[BZ-reaction]] — experimental chemical chaos shown by attractor reconstruction (pp. 443–445)
- [[forced-double-well-oscillator]] — driven beam; Poincaré section, transient chaos, fractal basins (pp. 448–453)

## Bridges (candidates)
- [structural-analogy] Fractal basin boundaries ↔ path dependence: near a basin boundary a tiny difference in start decides the long-run outcome.
- [same-math] Jacobian determinant as area/volume scaling ↔ change-of-variables for densities under a map: both use $|\det\mathbf J|$.
- [structural-analogy] Attractor reconstruction from one series ↔ inferring hidden state from one observed indicator in time-series social data.
- [metaphor] Pastry stretch–fold mixing ↔ mixing and thorough spreading of a small perturbation through a population.

## Questions this raises
- Why can delayed copies of one variable reproduce an attractor's topology (the text says "somehow"), and what limits this?
- How do we distinguish low-dimensional chaos from noise in data, and why is so much applied work dubious?
- What does area-preserving (Hamiltonian) chaos look like when there is no attractor?
- How can one prove that the Hénon attractor is strange for the standard parameters (the text cites Benedicks–Carleson)?

## Exercises worth doing
- Ex. 12.1.5 (p. 454) — binary-shift view of the area-preserving baker's map: periodic, aperiodic and dense orbits — difficulty: medium
- Ex. 12.1.7 (p. 454) — Smale horseshoe and the points that survive forever; link to transient chaos — difficulty: medium
- Ex. 12.2.6 (p. 457) — stability of the Hénon fixed points via Jacobian eigenvalues and the flip bifurcation — difficulty: medium
- Ex. 12.4.1 (p. 458) — prove the delayed sine trajectory is an ellipse — difficulty: easy
- Ex. 12.4.3 (p. 458) — reconstruct the Rössler attractor from $x(t)$ and compare $\tau$ to orbital period — difficulty: medium
- Ex. 12.5.5 (p. 459) — compute fractal basin boundaries for the driven pendulum — difficulty: hard

## Reading notes
- Printed = pdf − 19.
- The text layer is garbled for many math symbols (inequalities, Greek letters). I checked the images.
- Example 12.1.3 prints the second limit as "$n\to0$"; it should be $n\to\infty$, since $\varepsilon=a^n\to0$.
- The text says Fig. 12.5.6 is the Poincaré section "for the system of Example 12.5.1". Example 12.5.1 ($F=0.18$) has only limit cycles, so the fractal section presumably belongs to the chaotic case of Example 12.5.2 ($F=0.40$); the pages do not say which $F$ Fig. 12.5.6 uses. I report this as printed.
- Color plates 3–4 (fractal basins) are not in these pages. The exercises (pp. 454–459) are listed only, not solved.
