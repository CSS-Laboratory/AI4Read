---
id: strogatz-2024-nonlinear/ch01-overview
work: strogatz-2024-nonlinear
unit: 1 Overview
pages: 1-11
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Overview: Chaos, Fractals and the Place of Nonlinear Dynamics

## L0 — One line
Dynamics studies how systems change in time; it is organised by the number of variables and by linear versus nonlinear structure, and chaos and fractals appear in the nonlinear, three-or-more-variable part.

## L1 — The gist (≤ 120 words)
Strogatz introduces dynamics, the study of systems that evolve in time. He first gives a short history, from Newton through Poincaré's qualitative viewpoint to Lorenz's chaos. He then builds the logical structure: write ordinary differential equations in a very general first-order form, treat the variables as coordinates of a phase space, and distinguish linear systems (solvable by splitting into parts) from nonlinear ones (mostly impossible to solve analytically). Figure 1.3.1 sorts systems by number of variables and by linearity. The book starts in the nonlinear lower-left corner and moves right. Its method is geometric: draw trajectories rather than find formulas. The far corner, large nonlinear systems, is "the frontier".

**Prerequisites:** derivatives and basic differential equations (e.g. $\dot x = rx$); the idea of a coordinate plane.

## L2 — Key ideas (5–10 bullets)
- Chaos and fractals (fractals: the infinite patterns of Figure 1.0.1) belong to the wider subject of dynamics, which covers settling to equilibrium, cycling, and more complicated behaviour (p. 2).
- Poincaré changed the question from exact positions to qualitative ones, such as whether the solar system is stable. This geometric view underlies modern dynamics (p. 2).
- Lorenz (1963) used computer experiments to find chaos: aperiodic motion (never settling to a periodic state), sensitive dependence on initial conditions (two slightly different starts soon give totally different behaviour), and a butterfly-shaped set (p. 3).
- Ordinary differential equations fit the very general form $\dot x_i = f_i(x_1,\dots,x_n)$ (p. 6). Time dependence can always be removed by adding a variable (p. 8).
- A trajectory is a curve in phase space. Geometry can often reveal the trajectories without solving the equations (pp. 7–8).
- Linear systems equal the sum of their parts, so they can be split and solved. Nonlinear interactions break this (pp. 8–9).
- Figure 1.3.1 classifies systems by $n$ and by linearity. Oscillation first appears at $n=2$, chaos at $n\ge 3$ (pp. 10–11).

## L3 — Walkthrough

### 1.0 Chaos, Fractals, and Dynamics (pp. 1–2)
- The author notes popular fascination with chaos and fractals (Gleick's *Chaos*; Peitgen and Richter's picture book). He values them as hands-on mathematics alive and changing (p. 1).
- Style of the book: informal, concrete examples, geometric thinking rather than proofs, and "extremely applied". The science behind each application is explained from scratch (pp. 1–2).
- Chaos and fractals are part of **dynamics**: the subject of change, of systems evolving in time. Dynamics analyses systems that settle to equilibrium, repeat in cycles, or do something more complicated (p. 2).
- Differential equations, mechanics, chemical kinetics and population biology can all be placed in one framework, given at the chapter's end. Careful definitions come later (p. 2).

### 1.1 Capsule History of Dynamics (pp. 2–4)
- **Newton**, mid-1600s: invented differential equations and the laws of motion and gravitation, and explained Kepler's laws. He solved the two-body problem (Earth around Sun, inverse-square attraction) (p. 2).
- The three-body problem (sun, earth, moon) proved much harder. After decades it was realised to be essentially impossible to solve in the sense of explicit formulas (p. 2).
- **Poincaré**, late 1800s: asked qualitative questions (e.g. "Is the solar system stable forever, or will some planets eventually fly off to infinity?") and developed a geometric approach. He was also the first person to glimpse the possibility of **chaos**: deterministic behaviour that is aperiodic and depends sensitively on initial conditions, which makes long-term prediction impossible (p. 2).
- First half of the 20th century: chaos stayed in the background. Dynamics centred on nonlinear oscillators (radio, radar, phase-locked loops, lasers); the pioneers named are van der Pol, Andronov, Littlewood, Cartwright, Levinson and Smale. Separately, Birkhoff, then Kolmogorov, Arnol'd and Moser extended Poincaré's methods in classical mechanics (p. 3).
- 1950s: the high-speed computer let people experiment with equations and build intuition (p. 3).
- **Lorenz, 1963:** a simplified model of atmospheric convection rolls. Solutions never settled to equilibrium or a periodic state. Two slightly different initial conditions soon gave totally different behaviour, so the system is *inherently* unpredictable, because small measurement errors are amplified rapidly. Yet there was structure: in three dimensions the solutions fall on a butterfly-shaped set (Figure 1.1.1). Lorenz argued it must be "an infinite complex of surfaces", which today we would call a fractal (p. 3).
- 1970s (p. 4):
  - Ruelle and Takens proposed a theory of the onset of turbulence based on strange attractors.
  - May found chaos in iterated maps from population biology. His review stressed the teaching value of simple nonlinear systems, against misleading linear intuition.
  - Feigenbaum found universal laws for the transition from regular to chaotic behaviour: roughly, completely different systems can go chaotic in the same way. This linked chaos to phase transitions.
  - Experimentalists (Gollub, Libchaber, Swinney and others) tested the ideas in fluids, chemical reactions, circuits, mechanical oscillators and semiconductors.
  - Mandelbrot codified and popularised fractals. Winfree applied geometric methods to biological oscillations such as circadian and heart rhythms.
- Table 1.1.1 summarises this timeline (p. 5).

**Intuition note:** When exact formulas ran out (three bodies), progress came from asking different questions: what kind of long-term behaviour occurs. Computers then showed that simple deterministic equations can behave unpredictably.

### 1.2 The Importance of Being Nonlinear (pp. 4–9)
**Types of systems.** There are two main types of dynamical systems: differential equations (continuous time) and iterated maps or difference equations (discrete time). The book concentrates on differential equations, because they are used more widely. Maps return later as simple examples of chaos and as tools for analysing differential equations (p. 4).

**Ordinary vs partial.** The damped oscillator is an ordinary differential equation (one independent variable, $t$):
$$m\frac{d^2x}{dt^2}+b\frac{dx}{dt}+kx=0 \tag{1}$$
The heat equation is a partial differential equation (time $t$ and space $x$):
$$\frac{\partial u}{\partial t}=\frac{\partial^2 u}{\partial x^2}$$
The book deals almost exclusively with ordinary equations, since its concern is purely temporal behaviour (pp. 4–6).

**General form.** With $\dot x_i \equiv dx_i/dt$:
$$\dot x_1=f_1(x_1,\dots,x_n),\quad\dots,\quad \dot x_n=f_n(x_1,\dots,x_n). \tag{2}$$
The $x_i$ may be chemical concentrations, species populations, or planetary positions and velocities. The $f_i$ depend on the problem (p. 6).

**Rewriting the oscillator in form (2).** Put $x_1=x$, $x_2=\dot x$. Then $\dot x_1=x_2$ by definition, and from (1) (p. 6):
$$\dot x_2=\ddot x=-\frac{b}{m}\dot x-\frac{k}{m}x=-\frac{b}{m}x_2-\frac{k}{m}x_1 .$$
So the system is $\dot x_1=x_2$, $\dot x_2=-\frac{b}{m}x_2-\frac{k}{m}x_1$.

**Linear vs nonlinear.** A system is *linear* if all $x_i$ on the right appear to the first power only. Otherwise it is *nonlinear*. Typical nonlinear terms are products, powers and functions of the $x_i$: $x_1x_2$, $(x_1)^3$, $\cos x_2$ (p. 6).

**Pendulum.** $\ddot x+\frac{g}{L}\sin x=0$ ($x$ = angle from vertical, $g$ = gravity, $L$ = length). Equivalent system, nonlinear (pp. 6–7):
$$\dot x_1=x_2,\qquad \dot x_2=-\frac{g}{L}\sin x_1 .$$
- The usual fix is the small-angle approximation $\sin x\approx x$ for $x\ll1$. It makes the problem linear but throws away motions where the pendulum whirls over the top (p. 7).
- The pendulum can in fact be solved analytically with elliptic functions. But its behaviour is simple (swings at low energy, whirls at high energy), so there should be an easier route, which the book's geometric methods are meant to supply (p. 7).

**Phase space and trajectories.** A solution $(x_1(t),x_2(t))$ gives a point moving along a curve in the $(x_1,x_2)$ space. The curve is a **trajectory** and the space is the **phase space**. Every point can be an initial condition, so the phase space is completely filled with trajectories (p. 7). The goal is to run this in reverse: from the system, draw the trajectories. In many cases geometric reasoning does this without solving the system (pp. 7–8).

**Dimension.** For (2) the phase space has coordinates $x_1,\dots,x_n$. The system is called $n$-dimensional or $n$th-order (p. 8).

**Nonautonomous systems** (explicit time dependence). Take the forced oscillator $m\ddot x+b\dot x+kx=F\cos t$. Let $x_1=x$, $x_2=\dot x$, $x_3=t$, so $\dot x_3=1$ (p. 8):
$$\dot x_1=x_2,\qquad \dot x_2=\tfrac1m(-kx_1-bx_2+F\cos x_3),\qquad \dot x_3=1 \tag{3}$$
- An $n$th-order time-dependent equation is a special case of an $(n+1)$-dimensional system. Time dependence can always be removed by adding a dimension (p. 8).
- Benefit: trajectories stay "frozen" in phase space instead of wiggling. Physically, three numbers ($x$, $\dot x$, $t$) are needed to predict the future, so the state is three-dimensional (p. 8).
- Cost: nontraditional terminology. The forced oscillator is traditionally a second-order linear equation, but here it is a third-order nonlinear system because of the cosine. The author argues that forced oscillators share many properties of nonlinear systems, which justifies the choice (p. 8).

**Intuition note:** Adding variables, such as time itself, removes explicit time dependence, so trajectories stay frozen in phase space instead of wiggling and the geometric picture can be built.

**Why nonlinear problems are so hard** (pp. 8–9).
- Most nonlinear systems are impossible to solve analytically. The essential difference: *linear systems can be broken down into parts*. Each part is solved separately and the results recombined (p. 8).
- This underlies normal modes, Laplace transforms, superposition arguments and Fourier analysis. A linear system is "precisely equal to the sum of its parts" (p. 9).
- Nonlinear interactions occur whenever parts interfere, cooperate or compete. Example: two favourite songs played together do not give double the pleasure. Nonlinearity is vital to lasers, turbulence and Josephson-junction superconductivity (p. 9).

**Intuition note:** If a whole is the sum of its parts, you can study the parts alone. When the parts interact, you cannot split the problem this way, and the author names this as the essential difference that makes nonlinear systems harder to analyse.

### 1.3 A Dynamical View of the World (pp. 9–11)
- Figure 1.3.1 has two axes: the number of variables $n$ (the phase-space dimension) and linear vs nonlinear. Columns: $n=1$, $n=2$, $n\ge3$, $n\gg1$, continuum (p. 9, fig. p. 10).
- Example 1: exponential growth $\dot x=rx$. One variable suffices to predict the future, and the equation is linear, so it sits in the $n=1$ linear cell (p. 9).
- Example 2: the pendulum. Both angle $x$ and angular velocity $\dot x$ are needed to fix the solution. If only $x$ were known, we could not tell which way it swings. So it is in the $n=2$ column, nonlinear half (p. 9).
- The author calls parts of the picture debatable. The point is to classify systems by their dynamics (pp. 9–11).
- **Upper left:** small linear systems, with (roughly speaking) growth, decay or equilibrium at $n=1$ and oscillations at $n=2$. An RC circuit has $n=1$ and cannot oscillate; an RLC circuit has $n=2$ and can (p. 11).
- **Upper right:** linear partial differential equations (Maxwell, heat equation, Schrödinger). They involve a continuum of variables but are tractable through Fourier and transform methods (p. 11).
- **Lower half (nonlinear):** often deferred in courses. This book starts at the lower left and moves right. New phenomena appear at each step: fixed points and bifurcations at $n=1$, nonlinear oscillations at $n=2$, chaos and fractals at $n\ge3$. Geometry gives most of the information even though formulas are usually unavailable (p. 11).
- Figure 1.3.1 places examples in each nonlinear cell. At $n=1$: fixed points, bifurcations, logistic equation. At $n=2$: pendulum, limit cycles, predator–prey cycles. At $n\ge3$: Lorenz strange attractors, iterated maps, fractals. At $n\gg1$: coupled nonlinear oscillators, lasers, neural networks. In the continuum column: nonlinear waves, turbulent fluids, fibrillation, "Life" (p. 10).
- **"The frontier"** is the dashed region of large nonlinear systems (large $n$ and continuum), which in the figure also takes in a dashed block at the bottom of the $n\ge3$ column ("Practical uses of chaos", "Quantum chaos ?"). The author compares it to old maps marked "Here be dragons". Behaviour there is complicated in both space and time, e.g. turbulent fluid or fibrillating heart (pp. 10–11).

**Intuition note:** Two questions place any system: how many variables describe its state, and are the equations linear? Difficulty grows with both, and the hardest region, large and nonlinear, is the least understood.

## Toy example (ours, not from the text)
Test superposition (the "sum of parts" property) on one linear and one nonlinear equation.

*Linear:* $\dot x=-x$ has solution $x(t)=e^{-t}$ (derivative $-e^{-t}=-x$ ✓). Double it: $2e^{-t}$ has derivative $-2e^{-t}=-(2e^{-t})$ ✓. A multiple of a solution is again a solution.

*Nonlinear:* $\dot x=-x^2$ has solution $x(t)=1/(t+1)$, since $\dot x=-1/(t+1)^2=-x^2$ ✓. Now try $2x(t)=2/(t+1)$. Its derivative is $-2/(t+1)^2$, but $-(2x)^2=-4/(t+1)^2$. At $t=0$: left side $-2$, right side $-4$. ✗. Doubling a solution does not give a solution, so superposition fails.

*Phase-space trick:* $\ddot x=-x$ becomes $x_1=x$, $x_2=\dot x$, $\dot x_1=x_2$, $\dot x_2=-x_1$ ($n=2$). The forced equation $\dot x=\cos t$ becomes $\dot x_1=\cos x_2$, $\dot x_2=1$ ($n=2$, with $x_2=t$).

## Concepts
- [[nonlinearity]] — a system is nonlinear if some $x_i$ on the right-hand side is not simply to the first power (products, powers, functions); superposition then fails (pp. 6, 8–9)
- [[state space / phase space]] — space with coordinates $x_1,\dots,x_n$; each point is a state, each trajectory a solution; $n$ is its dimension (pp. 7–8)
- [[deterministic chaos]] — deterministic, aperiodic behaviour with sensitive dependence on initial conditions, making long-term prediction impossible (pp. 2–3)
- [[strange attractor / fractal]] — Lorenz's butterfly-shaped set, "an infinite complex of surfaces", now regarded as a fractal (p. 3)
- [[universality]] — Feigenbaum: roughly, completely different systems can go chaotic in the same way (p. 4)
- [[bifurcation]] — named as a new phenomenon appearing at $n=1$; not defined here (pp. 10–11)
- [[limit cycle]] — listed among $n=2$ nonlinear phenomena in Figure 1.3.1; not defined here (p. 10)
- [[fixed point and stability]] — fixed points listed as the $n=1$ nonlinear phenomenon; not defined here (pp. 10–11)
- [[autonomous vs nonautonomous system]] (new) — nonautonomous means explicit time dependence; adding $x_{n+1}=t$ turns it into form (2) (p. 8)
- [[iterated map]] (new) — a dynamical system in discrete time (difference equation), used later as a source of simple chaos examples (p. 4)

## Canonical instances
- [[lorenz-system]] — convection model with aperiodic motion, sensitivity and a butterfly-shaped attractor (p. 3)
- [[damped-harmonic-oscillator]] — linear, $n=2$; shows how to rewrite a second-order equation as a system (p. 6)
- [[pendulum]] — nonlinear, $n=2$; small-angle fudge vs geometric treatment (pp. 6–7)
- [[forced-harmonic-oscillator]] — time dependence removed by adding $x_3=t$; counted as a third-order nonlinear system (p. 8)
- [[exponential-growth]] — $\dot x=rx$, linear, $n=1$ (p. 9)
- [[rc-vs-rlc-circuit]] — $n=1$ cannot oscillate; $n=2$ can (p. 11)

## Bridges (candidates)
- [structural-analogy] Linear systems as the sum of their parts ↔ complex-systems: "more is different" — nonlinear interaction is where wholes stop being sums of parts.
- [structural-analogy] Feigenbaum universality ↔ complex-systems: universality near critical points — the text itself links chaos to phase transitions.
- [structural-analogy] Lorenz sensitive dependence ↔ complex-systems: Lyapunov exponent — both concern the rapid growth of small differences between trajectories (the text does not name the exponent).
- [structural-analogy] "The frontier" (large, nonlinear, spatio-temporal) ↔ complex-systems: agent-based and network models of many interacting parts.

## Questions this raises
- What exactly makes a trajectory picture enough to answer questions without a formula, for example for the pendulum?
- Why is chaos placed at $n\ge3$ for differential equations in Figure 1.3.1, when May found chaos in simple iterated maps (p. 4)?
- What does "sensitive dependence" mean quantitatively, and how fast do errors grow?
- Can a nonlinear system with many variables, the frontier, still be studied geometrically?

## Reading notes
- Printed page = pdf page − 15. PDF 27 (printed 12) is blank.
- The text layer drops Greek and special symbols in equations (e.g. overdots, $\equiv$, $\approx$, $\ll$, "$n+1$"). I checked these against the page images.
- Figure 1.3.1 is printed sideways across page 10. The text layer for it is scrambled, so I read it from the image.
- Eq. (1), (2), (3) are numbered as printed. The heat equation is unnumbered.
- Exercises: none in this chapter.
