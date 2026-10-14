---
id: strogatz-2024-nonlinear/ch10-one-p1
work: strogatz-2024-nonlinear
unit: "10 One-Dimensional Maps (part 1/2): 10.0–10.5 (to Example 10.5.3)"
pages: 355-375
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# One-Dimensional Maps, part 1: fixed points, the logistic map, windows, Liapunov exponent

## L0 — One line
A simple one-dimensional map such as the logistic map $x_{n+1}=rx_n(1-x_n)$ goes from a steady state to period-doubling to chaos as $r$ grows, and fixed-point stability, cobwebs and the Liapunov exponent let us analyse this.

## L1 — The gist (≤ 120 words)
Strogatz studies systems where time is discrete: $x_{n+1}=f(x_n)$. Stability of a fixed point depends on the multiplier $f'(x^*)$. Cobweb diagrams (graphical iteration) show global behaviour. For the logistic map, increasing $r$ gives a fixed point, then cycles of period 2, 4, 8, …, then chaos. Inside the chaos, periodic windows (ranges of $r$ with a stable cycle) appear. The period-3 window is born in a tangent (saddle-node) bifurcation; just below it, orbits show intermittency (near-periodic phases broken by chaotic bursts). The Liapunov exponent measures exponential separation of nearby orbits; a positive value signals chaos. Maps matter because they are easy to simulate and produce very complicated behaviour from simple rules. They have also successfully predicted routes to chaos in real experiments.

**Prerequisites:** derivatives, chain rule, Taylor expansion, 1D flows and bifurcations (saddle-node, transcritical, pitchfork), solving a quadratic.

## L2 — Key ideas
- A map $x_{n+1}=f(x_n)$ is a discrete-time system. It can show much wilder behaviour than a differential equation, because points hop instead of flowing (pp. 355–356).
- A fixed point $x^*$ is stable if $|f'(x^*)|<1$ and unstable if $|f'(x^*)|>1$. The marginal case $|f'|=1$ needs other tools, such as cobwebs (p. 357).
- Cobwebs show global behaviour: spiralling for negative multiplier, monotone approach at stable fixed points with positive multiplier (pp. 358–359).
- Logistic map: extinction for $r<1$, steady state for $1<r<3$, then a period-doubling cascade with ratio $\delta=4.669\ldots$ to chaos at $r_\infty\approx3.57$ (pp. 360–362).
- The orbit diagram mixes order and chaos: periodic windows sit among chaotic clouds, and the diagram reappears in miniature inside the period-3 window (p. 363).
- Fixed points and 2-cycles can be found exactly. The 2-cycle exists for $r>3$ and has multiplier $4+2r-r^2$, stable for $3<r<1+\sqrt6$ (pp. 364–368).
- The period-3 window opens by a tangent (saddle-node) bifurcation. Just before it, the "ghost" of the cycle gives intermittency (pp. 369–371).
- Liapunov exponent for maps: $\lambda=\lim\frac1n\sum\ln|f'(x_i)|$. It is negative on stable cycles, and $\ln r$ for the tent map (pp. 373–375).

## L3 — Walkthrough

### 10.0 Introduction (pp. 355–356)
- Maps are also called difference equations, recursion relations or iterated maps. The sequence $x_0,x_1,x_2,\dots$ is the *orbit* of $x_0$. Opening riddle: repeatedly press cos on a calculator in radian mode (answered in Example 10.1.3) (p. 355).
- Maps arise (1) as tools for differential equations (Poincaré maps, the Lorenz map), (2) as models where time is naturally discrete (digital electronics, parts of economics, non-overlapping animal generations), (3) as "mathematical laboratories for chaos" (p. 355).
- They can behave more wildly than differential equations, because points hop (Fig. 10.0.1). They are easy to simulate, and have yielded successful predictions about routes to chaos in semiconductors, convecting fluids, heart cells, lasers and chemical oscillators (p. 356).

### 10.1 Fixed points and cobwebs (pp. 356–359)
**Fixed point and linearization.** $x^*$ is a *fixed point* if $f(x^*)=x^*$; then an orbit starting there stays there (p. 356). Put $x_n=x^*+\eta_n$ and expand:
$$x^*+\eta_{n+1}=f(x^*+\eta_n)=f(x^*)+f'(x^*)\eta_n+O(\eta_n^2).$$
Since $f(x^*)=x^*$, this gives $\eta_{n+1}=f'(x^*)\eta_n+O(\eta_n^2)$ (p. 357). Neglecting $O(\eta_n^2)$ gives the *linearized map* $\eta_{n+1}=\lambda\eta_n$ with *multiplier* $\lambda=f'(x^*)$. Then $\eta_1=\lambda\eta_0$, $\eta_2=\lambda^2\eta_0$, and in general $\eta_n=\lambda^n\eta_0$ (p. 357).
- If $|\lambda|<1$, $\eta_n\to0$ and $x^*$ is linearly stable. If $|\lambda|>1$ it is unstable. These conclusions can be proven for the original nonlinear map. In the marginal case $|f'(x^*)|=1$, the neglected $O(\eta_n^2)$ terms decide stability (p. 357).

*Intuition note:* Near a fixed point, a small error is multiplied by about $f'(x^*)$ at every step. It shrinks if that factor has size below 1 and grows if above 1. At exactly 1 the first-order picture is silent.

**Example 10.1.1.** $x_{n+1}=x_n^2$. Fixed points: $x^*=(x^*)^2$, so $x^*=0$ or $1$. Multiplier $\lambda=2x^*$: $x^*=0$ is stable ($|\lambda|=0<1$), $x^*=1$ is unstable ($|\lambda|=2>1$) (p. 357). A fixed point with $\lambda=0$ is *superstable*: perturbations decay like $\eta_n\sim\eta_0^{(2^n)}$, much faster than the usual $\lambda^n\eta_0$ (p. 357).

**Cobwebs.** From $x_0$, go vertically to the graph of $f$ (height $x_1$), then horizontally to the diagonal $x_{n+1}=x_n$, then vertically to the curve again; repeat (Fig. 10.1.1) (p. 358). Cobwebs show global behaviour at a glance and are most valuable when linear analysis fails (p. 358).

**Example 10.1.2.** $x_{n+1}=\sin x_n$. At $x^*=0$, $\lambda=\cos0=1$, a marginal case. The cobweb (Fig. 10.1.2) shows the orbit slowly rattling down a narrow channel to 0, so 0 is locally stable. It is globally stable, since for any $x_0$ the first iterate lies in $-1\le x_1\le1$ (because $|\sin x|\le1$), where the same picture holds (p. 358).

**Example 10.1.3 (the riddle).** For $x_{n+1}=\cos x_n$, $x_n\to0.739\ldots$ from any start. This number is the unique solution of $x=\cos x$, a fixed point of the map. The cobweb spirals in (Fig. 10.1.3), giving damped oscillations. This is characteristic of $\lambda<0$; for stable fixed points with $\lambda>0$ convergence is monotonic (p. 359).

### 10.2 Logistic map: numerics (pp. 360–363)
May (1976) stressed that simple nonlinear maps can have very complicated dynamics (p. 360). The *logistic map* is
$$x_{n+1}=rx_n(1-x_n).\tag{1}$$
Here $x_n\ge0$ is a dimensionless population in generation $n$ and $r\ge0$ is the growth rate. The parabola has maximum $r/4$ at $x=\tfrac12$. Restricting to $0\le r\le4$ maps $[0,1]$ into itself (p. 360).

**Period-doubling.** Observed by computer (pp. 360–362):
- $r<1$: extinction, $x_n\to0$ (provable by cobwebbing, Ex. 10.2.2).
- $1<r<3$: approach to a nonzero steady state (Fig. 10.2.2, $r=2.8$).
- $r=3.3$: a *period-2 cycle* (alternating large/small values, Fig. 10.2.3).
- $r=3.5$: period 4 (Fig. 10.2.4).

Let $r_n$ be where a $2^n$-cycle first appears. Computer experiments give (p. 362):

| $n$ | $r_n$ | period born |
|---|---|---|
| 1 | 3 | 2 |
| 2 | 3.449… | 4 |
| 3 | 3.54409… | 8 |
| 4 | 3.5644… | 16 |
| 5 | 3.568759… | 32 |
| ∞ | 3.569946… | ∞ |

The convergence is essentially geometric:
$$\delta=\lim_{n\to\infty}\frac{r_n-r_{n-1}}{r_{n+1}-r_n}=4.669\ldots$$
Section 10.6 returns to this number (p. 362).

**Chaos and windows.** May asked what happens for $r>r_\infty$ (via Gleick). For many $r$ the sequence never settles to a fixed point or periodic orbit; it is aperiodic (Figs. 10.2.5, 10.2.6 for $r=3.9$) (p. 362).

The *orbit diagram* plots the attractor against $r$. Recipe: pick $r$; start from a random $x_0$; iterate about 300 times to remove transients; plot $x_{301},\dots,x_{600}$ above $r$; move to the adjacent $r$ (p. 363). Reading Fig. 10.2.7 (for $3.4\le r\le4$) (p. 363):
- At $r=3.4$ there are two branches (period 2). Both split at once into period 4, and so on, until at $r=r_\infty\approx3.57$ the attractor changes from a finite to an infinite set.
- For $r>r_\infty$ there are *periodic windows* between chaotic clouds. The large window near $r\approx3.83$ holds a stable 3-cycle. A blow-up of part of it shows a copy of the orbit diagram in miniature.

*Intuition note:* More $r$ does not mean steadily more chaos. Order returns in windows, and the same pattern repeats at smaller scales.

### 10.3 Logistic map: analysis (pp. 364–368)
**Example 10.3.1 (fixed points).** $x^*=rx^*(1-x^*)$ gives $x^*=0$ or $x^*=1-\tfrac1r$; the latter is allowable only if $r\ge1$. Multiplier: $f'(x^*)=r-2rx^*$. At 0, $\lambda=r$: stable for $r<1$, unstable for $r>1$. At $x^*=1-\frac1r$: $\lambda=r-2r(1-\frac1r)=2-r$. This is stable for $-1<2-r<1$, i.e. $1<r<3$, and unstable for $r>3$ (pp. 364–365).

Graphically (Fig. 10.3.1), the parabola is tangent to the diagonal at $r=1$. $x^*$ branches off the origin in a *transcritical bifurcation* at $r=1$. At $r=3$, $f'(x^*)=-1$ and a *flip bifurcation* occurs (p. 365).

**Example 10.3.2 (2-cycle exists for $r>3$).** A 2-cycle is $p,q$ with $f(p)=q$, $f(q)=p$. So $p$ is a fixed point of the *second-iterate map* $f^2(x)\equiv f(f(x))$, a quartic (Fig. 10.3.2). The equation $f^2(x)=x$ has the fixed points $0$ and $1-\frac1r$ as trivial roots. Factoring them out leaves a quadratic. Expansion gives $r^2x(1-x)[1-rx(1-x)]-x=0$. After long division the roots are (pp. 365–366)
$$p,q=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r},$$
real for $r>3$. At $r=3$ they coincide at $x^*=\frac23$, so the 2-cycle is born continuously from $x^*$. For $r<3$ the roots are complex: no 2-cycle (p. 366).

Cobwebs near a fixed point with $f'(x^*)\approx-1$ (Fig. 10.3.3) show how a flip can create a 2-cycle. If $f$ is concave down there, the cobweb tends to produce a small stable 2-cycle. Flip bifurcations can also be subcritical, with an unstable 2-cycle below the bifurcation (Ex. 10.3.11) (p. 367).

**Example 10.3.3 (stability of the 2-cycle).** Strategy: reduce cycle stability to fixed-point stability. $p$ and $q$ are fixed points of $f^2$; the 2-cycle is stable precisely if they are stable fixed points of $f^2$ (p. 367). Multiplier:
$$\lambda=\tfrac{d}{dx}f(f(x))\big|_{x=p}=f'(f(p))f'(p)=f'(q)f'(p).$$
The same $\lambda$ results at $x=q$, so the two branches bifurcate simultaneously (p. 367). Then (p. 368)
$$\lambda=r(1-2q)\,r(1-2p)=r^2[1-2(p+q)+4pq]=r^2\Big[1-\tfrac{2(r+1)}{r}+\tfrac{4(r+1)}{r^2}\Big]=4+2r-r^2.$$
(Added step: from the roots above, $p+q=\frac{r+1}{r}$ and $pq=\frac{r+1}{r^2}$.) Stability requires $|4+2r-r^2|<1$, i.e. $3<r<1+\sqrt6=3.449\ldots$ (added step: $4+2r-r^2<1\iff r>3$ for $r>0$; $4+2r-r^2>-1\iff r<1+\sqrt6$). This explains the numerical $r_1,r_2$ (p. 368).

*Intuition note:* A cycle of length 2 is a fixed point seen every two steps. Its stability factor is the product of the slopes at its two points.

Fig. 10.3.4 is a *bifurcation diagram*: unlike an orbit diagram, it also shows unstable objects. Exact results are hard to get beyond here; the rest relies on graphs and numerics (p. 368).

### 10.4 Periodic windows (pp. 368–373)
The period-3 window runs near $3.8284\ldots\le r\le3.8415\ldots$. The same mechanism creates all windows (p. 368).

**Birth of the 3-cycle.** Points of a 3-cycle satisfy $p=f^3(p)$, fixed points of the eighth-degree map $f^3$, which cannot be solved explicitly. Fig. 10.4.1 ($r=3.835$) shows eight intersections of $f^3$ with the diagonal: six are genuine period-3 points, two are fixed points. Black dots mark the stable 3-cycle (shallow slope); open dots mark an unstable one (slope exceeds 1) (p. 369). As $r$ decreases, hills move down and valleys rise. At $r=3.8$ the six intersections have vanished (Fig. 10.4.2). So at some intermediate $r$ the graph is tangent to the diagonal. The stable and unstable cycles coalesce and annihilate in a *tangent bifurcation*, which starts the window (p. 369).

The tangent bifurcation occurs at $r=1+\sqrt8=3.8284\ldots$ (Myrberg 1958). Strogatz says this is hard to derive, though often quoted without proof; see Ex. 10.4.10 and Saha and Strogatz (1994) (p. 370).

**Intermittency.** For $r$ just below the window (e.g. $r=3.8282$, Fig. 10.4.3), the orbit looks like a 3-cycle for a while, then bursts chaotically, then returns. This is the "ghost" of the vanished cycle. Ghosts always occur near saddle-node bifurcations, and a tangent bifurcation is a saddle-node bifurcation by another name (p. 371). The orbit returns to the ghost repeatedly, with chaotic bouts between visits; this is *intermittency* (Pomeau and Manneville 1980). Geometry (Fig. 10.4.4): after the bifurcation, narrow channels remain between the diagonal and $f^3$. The orbit needs many iterations to squeeze through, so $f^3(x_n)\approx x_n$ and it looks like a 3-cycle. It then escapes, wanders chaotically, and re-enters a channel at an unpredictable time and place (p. 371).

Intermittency arises commonly where the periodic-to-chaotic transition is a saddle-node bifurcation of cycles; Ex. 10.4.8 shows it in the Lorenz equations. Experimentally it looks like near-periodic motion with irregular bursts. Their timing is statistically distributed although the system is deterministic. Farther from the window the bursts are more frequent, until fully chaotic: the *intermittency route to chaos* (p. 371). Fig. 10.4.5 shows it in a laser (control parameter: mirror tilt). Bursts become more frequent from bottom to top of the figure. The kind discussed here is Type I (p. 372).

**Period-doubling inside the window.** Just after the stable 3-cycle is born, the slope of $f^3$ at the black dots is close to $+1$. As $r$ increases it decreases steadily and reaches $-1$. A flip bifurcation then splits each dot, giving a 6-cycle. The same mechanism as before produces orbits of period $3\cdot2^n$, and a similar cascade is found in all periodic windows (pp. 372–373).

### 10.5 Liapunov exponent (pp. 373–375)
To call aperiodic orbits chaotic we want sensitive dependence: neighbouring orbits separate exponentially fast, on average (p. 373). Take $x_0$ and a nearby $x_0+\delta_0$. If $|\delta_n|\approx|\delta_0|e^{n\lambda}$, then $\lambda$ is the *Liapunov exponent*; positive $\lambda$ is a signature of chaos. With $\delta_n=f^n(x_0+\delta_0)-f^n(x_0)$ and $\delta_0\to0$ (p. 373):
$$\lambda\approx\frac1n\ln\left|\frac{\delta_n}{\delta_0}\right|=\frac1n\ln\left|\frac{f^n(x_0+\delta_0)-f^n(x_0)}{\delta_0}\right|=\frac1n\ln|(f^n)'(x_0)|.$$
By the chain rule $(f^n)'(x_0)=\prod_{i=0}^{n-1}f'(x_i)$, so
$$\lambda\approx\frac1n\ln\Big|\prod_{i=0}^{n-1}f'(x_i)\Big|=\frac1n\sum_{i=0}^{n-1}\ln|f'(x_i)|.$$
If a limit exists, it defines the exponent of the orbit from $x_0$ (p. 374):
$$\lambda=\lim_{n\to\infty}\Big\{\frac1n\sum_{i=0}^{n-1}\ln|f'(x_i)|\Big\}.$$
$\lambda$ depends on $x_0$ but is the same for all $x_0$ in the basin of attraction of one attractor. It is negative for stable fixed points and cycles, and positive for chaotic attractors (p. 374).

*Intuition note:* Each step stretches a tiny gap by about $|f'(x_i)|$. The exponent is the average log of this stretch per step. Positive means gaps grow exponentially; negative means they shrink.

**Example 10.5.1.** A stable $p$-cycle through $x_0$ has $\lambda<0$; if superstable, $\lambda=-\infty$. Proof: $x_0$ is a fixed point of $f^p$ with $|(f^p)'(x_0)|<1$. The same $p$ terms repeat, so $\lambda=\frac1p\sum_{i=0}^{p-1}\ln|f'(x_i)|=\frac1p\ln|(f^p)'(x_0)|<0$. If superstable, $(f^p)'(x_0)=0$ and $\lambda=\frac1p\ln0=-\infty$ (p. 374).

**Example 10.5.2 (tent map).** $f(x)=rx$ for $0\le x\le\frac12$, $f(x)=r-rx$ for $\frac12\le x\le1$, with $0\le r\le2$ (Fig. 10.5.1). Since $f'(x)=\pm r$ everywhere, $\lambda=\ln r$ for any $x_0$. This suggests chaos for all $r>1$ (p. 375). Its dynamics can be understood in detail (see Devaney 1989) (p. 375).

**Example 10.5.3 (numerical scheme for the logistic map).** Fix $r$; start from a random $x_0$; iterate about 300 times for transients to decay; then iterate about 10,000 more, storing only the current $x_n$. Add $\ln|f'(x_n)|=\ln|r-2rx_n|$ to a running sum, and divide the total by 10,000. Repeat for the next $r$ (p. 375). (The resulting graph, Fig. 10.5.2, is on the next page, outside this unit.)

## Toy example (our own, not from the text)
**Part A, fixed point.** Take $r=2.5$. Then $x^*=1-\frac1{2.5}=0.6$ and $\lambda=2-r=-0.5$. Start at $x_0=0.62$ (deviation $\eta_0=+0.02$).
- $x_1=2.5(0.62)(0.38)=2.5(0.2356)=0.589$, so $\eta_1=-0.011$.
- $x_2=2.5(0.589)(0.411)=2.5(0.242079)=0.6051975$, so $\eta_2\approx+0.0052$.

The deviations alternate in sign and shrink by a factor near $|\lambda|=0.5$ (ratios $-0.55$, $-0.47$). This is a damped oscillation, as predicted for $\lambda<0$.

**Part B, 2-cycle.** Take $r=3.3$, in $(3,1+\sqrt6)$. Then $\sqrt{(r-3)(r+1)}=\sqrt{0.3\cdot4.3}=\sqrt{1.29}\approx1.1358$. So $p=(4.3-1.1358)/6.6\approx0.4794$ and $q=(4.3+1.1358)/6.6\approx0.8236$. Check: $f(p)=3.3(0.4794)(0.5206)\approx0.8236=q$. Multiplier: $4+2(3.3)-3.3^2=4+6.6-10.89=-0.29$, and $|-0.29|<1$, so the cycle is stable, as in Fig. 10.2.3.

## Concepts
- [[iterated-map]] (new) — a rule $x_{n+1}=f(x_n)$ in discrete time; its orbit is $x_0,x_1,\dots$ (p. 355)
- [[fixed-point-and-stability]] — $f(x^*)=x^*$; stable if $|f'(x^*)|<1$, unstable if $>1$, marginal at $=1$ (p. 357)
- [[linear-stability-analysis]] — linearize $\eta_{n+1}=f'(x^*)\eta_n$; multiplier $\lambda$ decides (p. 357)
- [[superstable-fixed-point]] (new) — multiplier 0; perturbations decay like $\eta_0^{(2^n)}$ (p. 357)
- [[cobweb-diagram]] (new) — graphical iteration between the curve of $f$ and the diagonal (p. 358)
- [[logistic-map]] (new) — $x_{n+1}=rx_n(1-x_n)$, $0\le r\le4$ (p. 360)
- [[period-doubling-route-to-chaos]] — cycles of period $2^n$ appear at $r_n$ and accumulate at $r_\infty\approx3.57$ (p. 362)
- [[feigenbaum-delta]] (new) — ratio $\delta=4.669\ldots$ of successive bifurcation spacings (p. 362)
- [[orbit-diagram]] (new) — attractor plotted against $r$; the bifurcation diagram also shows unstable states (pp. 363, 368)
- [[periodic-window]] (new) — an $r$-interval with a stable cycle inside the chaotic regime (p. 363)
- [[bifurcation]] — transcritical (r=1), flip (r=3), tangent (window birth) for maps (pp. 365, 369)
- [[saddle-node-bifurcation]] — author states a tangent bifurcation is this under another name (p. 371)
- [[intermittency]] (new) — near-periodic "ghost" phases interrupted by chaotic bursts, just below a window (p. 371)
- [[deterministic-chaos]] — aperiodic, sensitive dependence; here tested by $\lambda>0$ (p. 373)
- [[lyapunov-exponent]] — $\lambda=\lim\frac1n\sum\ln|f'(x_i)|$ (p. 374)
- [[attractor-basin]] — $\lambda$ is the same across one basin of attraction (p. 374)
- [[tent-map]] (new) — piecewise linear map with $\lambda=\ln r$ (p. 374)

## Canonical instances
- [[cosine-iteration]] — $x_{n+1}=\cos x_n\to0.739\ldots$, spiral cobweb (p. 359)
- [[sine-map-marginal]] — $x_{n+1}=\sin x_n$, marginal fixed point, globally stable (p. 358)
- [[logistic-map-period-doubling]] — $r_1,\dots,r_\infty$ table and $\delta$ (p. 362)
- [[period-3-window]] — tangent bifurcation at $1+\sqrt8$, intermittency, 6-cycle (pp. 368–373)
- [[laser-intermittency]] — experimental intermittency route to chaos (p. 372)
- [[tent-map-lyapunov]] — $\lambda=\ln r$ (p. 375)

## Bridges (candidates)
- [same-math] tangent bifurcation of $f^3$ ↔ saddle-node bifurcation of flows: author states they are the same bifurcation under another name (p. 371).
- [structural-analogy] ghost of a vanished cycle (intermittency) ↔ tipping points: dwelling near a ghost before leaving, a slow passage after a fold.
- [structural-analogy] multiplier $|\lambda|\to1$ at flip/transcritical points ↔ critical slowing down: recovery from perturbations becomes slow as stability is lost.
- [structural-analogy] logistic map for non-overlapping generations ↔ population dynamics: discrete growth with density limit.

## Questions this raises
- Why is the ratio $\delta=4.669\ldots$ the same for other maps? (Section 10.6 on universality, announced p. 356.)
- Is positive $\lambda$ enough to call an orbit chaotic, given that for the tent map the author says $\lambda=\ln r>0$ only "suggests" chaos for $r>1$ (p. 375)?
- Why does the period-3 tangent bifurcation occur exactly at $1+\sqrt8$, and how does Saha and Strogatz derive it (p. 370)?
- How does the Liapunov exponent of the logistic map vary with $r$ in $3\le r\le4$ (Example 10.5.3)?

## Reading notes
- This is part 1 of Chapter 10. It starts at the chapter start (10.0, p. 355) and ends on p. 375 after Example 10.5.3, just before Fig. 10.5.2. It was split at a section boundary. Sections 10.6 (universality) and 10.7 (renormalization) and the chapter exercises are not in these pages, so no exercises are listed.
- Page offset: printed = pdf − 19.
- The text layer is garbled in places (multiplier symbol shown as "M", missing minus signs). All math was checked against the page images.
- Possible misprint, p. 368: the last line of Example 10.3.3 prints the condition as $|4+2r+r^2|<1$. The derived multiplier just above is $4+2r-r^2$, and the stated range $3<r<1+\sqrt6$ fits that expression, so the "+" appears to be an error for "−". I wrote the corrected form.
- On p. 371 the book says "(Sections 4.3 and 8.1)" for saddle-node bifurcations; these sections are outside this unit.
