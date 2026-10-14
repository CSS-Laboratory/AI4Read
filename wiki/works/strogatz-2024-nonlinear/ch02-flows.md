---
id: strogatz-2024-nonlinear/ch02-flows
work: strogatz-2024-nonlinear
unit: "2 Flows on the Line"
pages: 15–44
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
# Flows on the Line (first-order systems $\dot x = f(x)$)

## L0 — One line
A one-dimensional system $\dot x=f(x)$ can be understood qualitatively from the graph of $f$: trajectories run monotonically to fixed points or to $\pm\infty$, so stability can be read off geometrically, and oscillation is impossible.

## L1 — The gist (≤ 120 words)
How can we analyse a nonlinear equation $\dot x=f(x)$ without solving it? Strogatz treats $f(x)$ as a velocity field on the line. Fixed points ($f=0$) organise the flow. The slope $f'(x^*)$ gives stability and a time scale, but fails when it is zero. A smooth $f$ gives unique local solutions, though they may blow up in finite time. Trajectories on a line never reverse, so no oscillations occur. The same flow can be pictured as downhill motion in a potential. Numerical integration (Euler, improved Euler, Runge–Kutta) handles equations that resist formulas. Strogatz says the degenerate cases ($f'(x^*)=0$) arise in bifurcations, discussed later.

**Prerequisites:** derivatives, Taylor expansion, separation of variables, chain rule, basic sketching of functions.

## L2 — Key ideas
- A differential equation $\dot x=f(x)$ is a vector field on the line; plotting $\dot x$ against $x$ answers qualitative questions faster than the exact solution (pp. 16–18).
- Fixed points $x^*$ ($f(x^*)=0$) are equilibria. Stability means small disturbances decay; "locally stable" need not mean "globally stable" (pp. 19–20).
- The logistic equation has an unstable fixed point at $0$ and a stable one at $K$. The graph of $f$ also gives the shape of the solutions, which are S-shaped (sigmoid) for $N_0<K/2$. Strogatz says the model should be seen as a metaphor and not taken literally (pp. 21–24).
- Linear stability: $\dot\eta\approx\eta f'(x^*)$, so $f'(x^*)$'s sign gives stability and $1/|f'(x^*)|$ is a time scale. If $f'(x^*)=0$ the test is silent (pp. 24–26).
- If $f$ and $f'$ are continuous, solutions exist locally and are unique. The theorem does not promise solutions for all time; blow-up happens (pp. 27–28).
- Fixed points dominate first-order dynamics: no overshoot, no periodic solutions. Strogatz calls this topological in origin (a monotonic flow on a line never returns to its start), and it matches the overdamped limit (very strong friction) of Newton's law (pp. 28–30).
- A first-order flow can be pictured as motion in a potential $V$ defined by $f=-dV/dx$: $V$ decreases along trajectories, local minima are stable and local maxima are unstable (pp. 30–31).
- Euler's method is simple, but its approximation gets bad quickly unless $\Delta t$ is very small. Improved Euler and Runge–Kutta reduce the error faster as $\Delta t\to0$, though higher order is not necessarily better because of extra cost. Round-off error (the finite precision of computers) also stops us from shrinking $\Delta t$ without limit (pp. 32–35).

## L3 — Walkthrough

### 2.0 Introduction (p. 15)
Strogatz starts with $n=1$: $\dot x=f(x)$, with $f$ smooth and real-valued; he calls these one-dimensional or first-order systems (p. 15). "System" means a dynamical system, so a single equation counts. $f$ may not depend explicitly on time. $\dot x=f(x,t)$ is really two-dimensional, since $x$ and $t$ are both needed to predict the future (p. 15).

### 2.1 A Geometric Way of Thinking (pp. 16–18)
Example: $\dot x=\sin x$ \tag{1}. Separating variables:
$$dt=\frac{dx}{\sin x},\qquad t=\int\csc x\,dx=-\ln|\csc x+\cot x|+C .$$
With $x=x_0$ at $t=0$, $C=\ln|\csc x_0+\cot x_0|$, so
$$t=\ln\left|\frac{\csc x_0+\cot x_0}{\csc x+\cot x}\right| .\tag{2}$$
This is exact but hard to interpret. Questions: what happens for $x_0=\pi/4$ as $t\to\infty$, and for arbitrary $x_0$? (p. 16)

Graphical approach: let $x$ be the position of a particle on the line and $\dot x$ its velocity. Then $\dot x=\sin x$ is a **vector field on the line**. Plot $\dot x$ against $x$ and draw arrows on the axis: right where $\dot x>0$, left where $\dot x<0$ (p. 16). Think of a steady fluid flow. Where $\dot x=0$ there is no flow: **fixed points**. A stable fixed point (attractor, sink; solid dot) has flow toward it. An unstable one (repeller, source; open circle) has flow away (p. 17).

Answers from Fig. 2.1.1:
1. From $x_0=\pi/4$ the particle speeds up until $x=\pi/2$ (maximum of $\sin x$). Then it slows and approaches the stable point $x=\pi$ from the left. So $x(t)$ is concave up, then concave down (p. 17).
2. For any $x_0$ the particle goes to the nearest stable fixed point in the direction of the flow. If $\dot x=0$ initially, $x$ stays constant (p. 17, Fig. 2.1.3 on p. 18).

A picture cannot tell us certain quantitative things, e.g. the time at which the speed is greatest. Often only qualitative information is needed (p. 18).

*Intuition note:* The exact formula (2) hides what the graph shows at once: where the particle stops and which way it moves. Here, reading the sign of $f$ gives the long-term fate of each start.

### 2.2 Fixed Points and Stability (pp. 18–21)
For general $\dot x=f(x)$, draw $f$ and sketch the flow on the real line. The line is the **phase space**; the imaginary fluid is the **phase fluid**; a particle at $x_0$ is a **phase point**. Its path $x(t)$ is the **trajectory** based at $x_0$. A picture of all qualitatively different trajectories is a **phase portrait** (p. 19). Fixed points $x^*$ satisfy $f(x^*)=0$ and are stagnation points. They are equilibrium solutions: if $x=x^*$ initially then $x(t)=x^*$ for all time. An equilibrium is **stable** if all sufficiently small disturbances damp out in time (p. 19). Stability is defined through *small* disturbances (p. 20).

**Example 2.2.1** ($\dot x=x^2-1$): $f(x^*)=0$ gives $x^*=\pm1$. The flow is right where $x^2-1>0$ and left where it is $<0$, so $x^*=-1$ is stable and $x^*=1$ is unstable (p. 19). A large disturbance past $x=1$ is repelled to $+\infty$. So $x^*=-1$ is *locally* stable but not *globally* stable (p. 20).

**Example 2.2.2** (RC circuit: resistor $R$, capacitor $C$, battery $V_0$; switch closed at $t=0$, $Q(0)=0$). Voltage drops sum to zero, $-V_0+RI+Q/C=0$, and $\dot Q=I$:
$$\dot Q=f(Q)=\frac{V_0}{R}-\frac{Q}{RC}.$$
$f$ is a line of negative slope with fixed point $Q^*=CV_0$. The flow is always toward $Q^*$: it is globally stable, approached from all initial conditions. A phase point from the origin moves monotonically to $Q^*$ with speed $\dot Q$ decreasing linearly, so $Q(t)$ is increasing and concave down (pp. 20–21).

**Example 2.2.3** ($\dot x=x-\cos x$): instead of plotting $x-\cos x$, plot $y=x$ and $y=\cos x$ together. They cross exactly once, at $x^*=\cos x^*$. The line is above the cosine for $x>x^*$ ($\dot x>0$) and below for $x<x^*$. So $x^*$ is the only fixed point and it is unstable. Stability is classified without a formula for $x^*$ (p. 21).

*Intuition note:* In the graphical method, stability depends on the sign of $f$ on each side of a zero. So you can classify fixed points of an equation you cannot solve.

### 2.3 Population Growth (pp. 21–24)
Simplest model: $\dot N=rN$, $r>0$, giving $N(t)=N_0e^{rt}$ (p. 22). To model overcrowding, assume the per capita growth rate $\dot N/N$ decreases linearly with $N$: rate $r$ for small $N$, negative above the **carrying capacity** $K$. This gives the **logistic equation**
$$\dot N=rN\left(1-\frac NK\right),$$
first suggested for human populations by Verhulst in 1838 (p. 22). Only $N\ge0$ is plotted (Fig. 2.3.3). Fixed points: $N^*=0$ (unstable: a small population grows exponentially fast) and $N^*=K$ (stable: disturbances decay monotonically). From any $N_0>0$ the population approaches $K$; if $N_0=0$ it stays $0$ (p. 22).

Shapes of solutions (the parabola in Fig. 2.3.3 peaks at $N=K/2$) (p. 23):
- $N_0<K/2$: accelerating at first (concave up), then concave down: S-shaped (sigmoid).
- $K/2<N_0<K$: decelerating from the start, concave down for all $t$.
- $N_0>K$: $N(t)$ decreases toward $K$ and is concave up.
- $N_0=0$ or $N_0=K$: constant.

*Critique of the logistic model* (pp. 23–24). The algebraic form should not be taken literally. It is a metaphor for populations that tend to grow from zero toward a carrying capacity (p. 23). Pearl (1927) proposed a stricter reading: a universal law of growth. Lab colonies of bacteria, yeast and similar organisms in constant conditions often gave sigmoid curves, sometimes matching the logistic closely. Fruit flies, flour beetles and others with complex life cycles matched much worse: after initial logistic growth they showed large, persistent fluctuations, not a steady approach to $K$ (p. 24). Possible causes mentioned: age structure and time-delayed effects of overcrowding (p. 24).

*Intuition note:* One picture (a parabola of $\dot N$ against $N$) gives both the fixed points and the whole family of curve shapes. The logistic equation captures "grow, then saturate", not the details of real species.

### 2.4 Linear Stability Analysis (pp. 24–26)
Goal: a quantitative measure, such as the decay rate to a stable fixed point. Let $x^*$ be a fixed point and $\eta(t)=x(t)-x^*$ a small perturbation. Then $\dot\eta=\dot x=f(x^*+\eta)$ since $x^*$ is constant. Taylor expansion:
$$f(x^*+\eta)=f(x^*)+\eta f'(x^*)+O(\eta^2),$$
where $O(\eta^2)$ means quadratically small terms. Since $f(x^*)=0$,
$$\dot\eta=\eta f'(x^*)+O(\eta^2).$$
If $f'(x^*)\neq0$ the $O(\eta^2)$ terms are negligible, giving the **linearization about $x^*$**: $\dot\eta\approx\eta f'(x^*)$. The perturbation grows exponentially if $f'(x^*)>0$ and decays if $f'(x^*)<0$. If $f'(x^*)=0$, the quadratic terms are not negligible and a nonlinear analysis is needed (pp. 24–25).

The sign of $f'(x^*)$ gives stability; its magnitude is an exponential growth or decay rate. The reciprocal $1/|f'(x^*)|$ is a **characteristic time scale**: the time for $x(t)$ to vary significantly near $x^*$ (p. 25).

**Example 2.4.1** ($\dot x=\sin x$): $x^*=k\pi$, $f'(x^*)=\cos k\pi=1$ ($k$ even), $-1$ ($k$ odd). So even $k$ is unstable and odd $k$ is stable, as in Fig. 2.1.1 (p. 25).

**Example 2.4.2** (logistic): $f'(N)=r-2rN/K$, so $f'(0)=r$ and $f'(K)=-r$. $N^*=0$ is unstable, $N^*=K$ is stable. In both cases the time scale is $1/r$ (p. 25).

**Example 2.4.3** ($f'(x^*)=0$): nothing can be said in general. For $x^*=0$ in (a) $\dot x=-x^3$: stable. (b) $\dot x=x^3$: unstable. (c) $\dot x=x^2$: **half-stable** (attracting from the left, repelling from the right; half-filled circle). (d) $\dot x=0$: a whole line of fixed points; perturbations neither grow nor decay (p. 26). These cases arise naturally in bifurcations, discussed later (p. 26).

*Intuition note:* Close to a fixed point the curve $f$ looks like a straight line of slope $f'(x^*)$. A steeper slope means faster return (or escape). A flat slope means the linear picture is no longer enough.

### 2.5 Existence and Uniqueness (pp. 26–28)
The treatment so far has been informal about whether solutions exist and are unique (p. 26).

**Example 2.5.1** ($\dot x=x^{1/3}$, $x_0=0$): $x(t)=0$ is a solution. Separating variables, $\int x^{-1/3}dx=\int dt$ gives $\tfrac32x^{2/3}=t+C$; with $x(0)=0$, $C=0$, so $x(t)=\left(\tfrac23t\right)^{3/2}$ is also a solution (p. 27). Uniqueness fails and the geometric picture breaks down, since the phase point "doesn't know how to move". There are in fact infinitely many solutions (Ex. 2.5.4). A hint to the cause: $f'(0)$ is infinite (Fig. 2.5.1) (p. 27).

**Existence and Uniqueness Theorem.** Consider $\dot x=f(x)$, $x(0)=x_0$. Suppose $f(x)$ and $f'(x)$ are continuous on an open interval $R$ of the $x$-axis and $x_0\in R$. Then the initial value problem has a solution $x(t)$ on some time interval $(-\tau,\tau)$ about $t=0$, and the solution is unique (p. 27). This gives *sufficient* conditions only. Proofs are cited to other texts (p. 27).

**Example 2.5.2** ($\dot x=1+x^2$, $x(0)=x_0$): $f$ and $f'$ are continuous for all $x$, so solutions exist and are unique for any $x_0$. But the theorem does not say they exist for all time, only on a possibly very short interval around $t=0$. For $x_0=0$: $\int\frac{dx}{1+x^2}=\int dt$ gives $\tan^{-1}x=t+C$, $C=0$, so $x(t)=\tan t$. This exists only for $-\pi/2<t<\pi/2$, since $x\to\pm\infty$ as $t\to\pm\pi/2$ (p. 28). Reaching infinity in finite time is called **blow-up**; it is relevant to models of combustion and other runaway processes (p. 28). From now on Strogatz will not worry about this issue (p. 28).

*Intuition note:* Smoothness of $f$ guarantees a unique solution from each start, but only on a possibly short time interval. For example, $\dot x=1+x^2$ sends the particle to infinity in finite time.

### 2.6 Impossibility of Oscillations (pp. 28–30)
In all examples, trajectories approached a fixed point or diverged to $\pm\infty$, and these are the only possibilities on the real line. Trajectories must increase or decrease monotonically or stay constant; the phase point never reverses direction (p. 28). So approach to equilibrium is always monotonic: no overshoot, no damped oscillations. Undamped oscillations are impossible too: there are no periodic solutions of $\dot x=f(x)$ (p. 29). This is topological in origin: flowing monotonically on a line never returns you to the start. On a circle it could, and vector fields on the circle can have periodic solutions (Chapter 4) (p. 29).

*Mechanical analog: overdamped systems* (pp. 29–30). Take Newton's law for a mass $m$ on a nonlinear spring with restoring force $F(x)$, in very viscous fluid with damping force $b\dot x$:
$$m\ddot x+b\dot x=F(x).$$
If $b\dot x\gg m\ddot x$ the system behaves like $b\dot x=F(x)$, i.e. $\dot x=f(x)$ with $f(x)=b^{-1}F(x)$. The mass sits at a stable equilibrium ($f=0$, $f'<0$); if displaced, it is dragged back slowly, with no overshoot (pp. 29–30). Strogatz admits a "slight swindle": neglecting $m\ddot x$ is valid only after a rapid initial transient in which inertia and damping are comparable; this is deferred to Section 3.5 (p. 30).

*Intuition note:* On a line, the only way to go back is to turn around, and that would require a point where the velocity is zero. A zero-velocity point is a fixed point, where the flow stops. (Added reading of "never reverses direction", p. 28.)

### 2.7 Potentials (pp. 30–31)
Define the **potential** $V(x)$ by
$$f(x)=-\frac{dV}{dx}.$$
The particle is heavily damped, sliding down a potential well through "goo" (p. 30). By the chain rule, $\frac{dV}{dt}=\frac{dV}{dx}\frac{dx}{dt}$. Since $\dot x=f(x)=-dV/dx$,
$$\frac{dV}{dt}=-\left(\frac{dV}{dx}\right)^2\le0 .$$
So $V$ decreases along trajectories, and the particle moves toward lower potential. If the particle is at a point where $dV/dx=0$, then $V$ remains constant; this implies $\dot x=0$: equilibria occur at the fixed points of the vector field. Local minima of $V$ are stable fixed points; local maxima are unstable (p. 31).

**Example 2.7.1** ($\dot x=-x$): $V(x)=\tfrac12x^2+C$. The potential is defined only up to an additive constant (take $C=0$). The only equilibrium, $x=0$, is stable (p. 31).

**Example 2.7.2** ($\dot x=x-x^3$): $V=-\tfrac12x^2+\tfrac14x^4+C$. Minima at $x=\pm1$ are stable, the maximum at $x=0$ is unstable. This is a **double-well potential**, and the system is **bistable** (two stable equilibria) (p. 31).

*Intuition note:* In one dimension every flow is "rolling downhill". Valleys are stable states and hilltops are unstable ones.

### 2.8 Solving Equations on the Computer (pp. 32–35)
**Euler's method.** Given $\dot x=f(x)$, $x=x_0$ at $t=t_0$, approximate $x(t)$. Flowing for a short time $\Delta t$ moves the phase point about $f(x_0)\Delta t$ (distance = rate × time), so $x(t_0+\Delta t)\approx x_1=x_0+f(x_0)\Delta t$. Iterating gives the update rule
$$x_{n+1}=x_n+f(x_n)\Delta t .$$
The approximation "gets bad in a hurry" unless $\Delta t$ is very small. It is not recommended in practice but contains the conceptual essence of the better methods (pp. 32–33).

**Improved Euler method.** Euler uses the derivative only at the left end of the interval. Instead, take a trial step, then average the derivative at both ends:
$$\tilde x_{n+1}=x_n+f(x_n)\Delta t\quad\text{(trial step)},$$
$$x_{n+1}=x_n+\tfrac12\left[f(x_n)+f(\tilde x_{n+1})\right]\Delta t\quad\text{(real step)}.$$
The error $E=|x(t_n)-x_n|$ goes to $0$ as $\Delta t\to0$ in both methods, but $E\propto\Delta t$ for Euler (first order) and $E\propto(\Delta t)^2$ for improved Euler (second order) (Exercises 2.8.7–2.8.8) (p. 33).

**Fourth-order Runge–Kutta.** Higher order is not necessarily better, since it costs more function evaluations. A good balance is RK4:
$$k_1=f(x_n)\Delta t,\quad k_2=f(x_n+\tfrac12k_1)\Delta t,\quad k_3=f(x_n+\tfrac12k_2)\Delta t,\quad k_4=f(x_n+k_3)\Delta t,$$
$$x_{n+1}=x_n+\tfrac16(k_1+2k_2+2k_3+k_4).$$
Some problems need small steps in some intervals and allow large ones elsewhere; then automatic stepsize control is useful (p. 34).

**Round-off error.** Computers cannot tell apart numbers differing by a small $\delta$: for numbers of order 1, typically $\delta\approx10^{-7}$ (single precision) and $\approx10^{-16}$ (double). Round-off enters every calculation and accumulates seriously if $\Delta t$ is too small, so one cannot just pick a tiny $\Delta t$ (p. 34).

**Practical matters.** Options: write your own routines; use Matlab, Mathematica or Maple; or use dynamical-systems programs such as PPlane (good for beginners) and XPP (more powerful) (p. 34).

**Example 2.8.1** ($\dot x=x(1-x)$, i.e. logistic with $r=1$, $K=1$). The equation is also read as a **slope field** in the $(t,x)$ plane: at each point it gives the slope $dx/dt$ of the solution through that point. A solution is a curve tangent to the local slope. Four solutions were computed with Runge–Kutta, $\Delta t=0.1$; they have the shapes predicted in Section 2.3 (p. 35).

*Intuition note:* Numerical integration is the vector-field idea in discrete form: look at the current velocity, move a little, repeat. Better methods sample the velocity more than once per step.

## Toy example (ours, not from the text)
System $\dot x=f(x)=x^2-4$.
- Fixed points: $x^2-4=0$, so $x^*=\pm2$.
- Linear stability: $f'(x)=2x$. At $x^*=-2$, $f'=-4<0$: stable, time scale $1/4=0.25$. At $x^*=2$, $f'=4>0$: unstable.
- Check of the linearization at $x=-1.9$ ($\eta=0.1$): exact $f(-1.9)=3.61-4=-0.39$. Linear prediction $\eta f'(x^*)=0.1\times(-4)=-0.4$. The difference is $0.01=\eta^2$, as the $O(\eta^2)$ term says.
- Euler with $\Delta t=0.1$ from $x_0=-1$: $f(-1)=1-4=-3$, so $x_1=-1+(-3)(0.1)=-1.3$. $f(-1.3)=1.69-4=-2.31$, so $x_2=-1.3-0.231=-1.531$. The point moves left toward $-2$, as the flow arrows say (flow is left where $x^2-4<0$).
- From $x_0=3$: $f(3)=5$, $x_1=3+0.5=3.5$, moving away from $2$ toward $+\infty$. This is a large disturbance past the unstable point, as in Example 2.2.1.
- Potential: $-dV/dx=x^2-4$ gives $V=-x^3/3+4x$ (with $C=0$). $V'(x)=-(x^2-4)$ vanishes at $\pm2$. $V''=-2x$ is $+4$ at $x=-2$ (minimum, stable) and $-4$ at $x=2$ (maximum, unstable).

## Concepts
- [[fixed point and stability]] — a point where $f(x^*)=0$; stable if small disturbances die out (pp. 17, 19)
- [[linear stability analysis]] — here in 1D: the sign of $f'(x^*)$ decides stability; fails if $f'(x^*)=0$ (pp. 24–25)
- [[state space / phase space]] — here the real line, with the "phase fluid" flowing on it (p. 19)
- [[vector-field-on-the-line]] (new) — $f(x)$ read as the velocity at each $x$ (p. 16)
- [[phase-portrait]] (new) — picture of all qualitatively different trajectories (p. 19)
- [[local-vs-global-stability]] (new) — stability to small disturbances versus approach from all initial conditions (p. 20)
- [[characteristic-time-scale]] (new) — $1/|f'(x^*)|$, the time for $x$ to change significantly near $x^*$ (p. 25)
- [[logistic-equation]] (new) — $\dot N=rN(1-N/K)$; growth with a carrying capacity (p. 22)
- [[existence-and-uniqueness]] (new) — if $f,f'$ are continuous, a unique local solution exists (p. 27)
- [[blow-up]] (new) — reaching infinity in finite time (p. 28)
- [[overdamped-limit]] (new) — $b\dot x\gg m\ddot x$, so $m\ddot x+b\dot x=F$ reduces to a first-order system (p. 29)
- [[potential-function]] (new) — $V$ with $f=-dV/dx$; decreases along trajectories (p. 30)
- [[numerical-integration]] (new) — Euler, improved Euler and Runge–Kutta methods and their error orders (pp. 32–34)
- [[bifurcation]] — only mentioned: the degenerate cases $f'(x^*)=0$ "arise naturally" there (p. 26)

## Canonical instances
- [[sin-x-flow]] — $\dot x=\sin x$: alternating stable and unstable fixed points (p. 17)
- [[logistic-growth]] — sigmoid approach to carrying capacity; limits of the model (pp. 22–24)
- [[rc-circuit-charging]] — globally stable linear first-order system (p. 20)
- [[degenerate-fixed-points]] — $\pm x^3$, $x^2$, $0$ with $f'(0)=0$ (p. 26)
- [[non-unique-solution-x13]] — $\dot x=x^{1/3}$ (p. 27)
- [[finite-time-blow-up]] — $\dot x=1+x^2$, $x=\tan t$ (p. 28)
- [[double-well-bistability]] — $V=-\tfrac12x^2+\tfrac14x^4$ (p. 31)

## Bridges (candidates)
- [same-math] $f'(x^*)$ stability test ↔ complex-systems: Jacobian eigenvalue test in higher dimensions — for $n=1$ the Jacobian is the single number $f'(x^*)$.
- [structural-analogy] double-well potential, two stable equilibria ↔ tipping points/hysteresis: two coexisting stable states (the text does not make this link).
- [structural-analogy] Euler time-stepping of a vector field ↔ agent-based models: advancing a state by small updates from local rules.
- [metaphor] logistic equation as "a metaphor" for saturating growth ↔ many-model thinking: a simple model used for qualitative insight, not as a literal law (the author calls it a metaphor, p. 23).

## Questions this raises
- What happens to the fixed points and their stability when a parameter in $f$ changes (the bifurcation question the author postpones, p. 26)?
- Which kinds of behaviour appear when the phase space is two-dimensional or a circle, where oscillations become possible (p. 29)?
- When is dropping the inertia term justified, given the "swindle" about the initial transient (p. 30)?
- How should one choose $\Delta t$, balancing truncation error against round-off error (p. 34)?

## Exercises worth doing
- Ex. 2.2.10 (p. 37) — which fixed-point patterns (all reals, integers only, three stable, none, exactly 100) are possible for smooth $f$ — medium
- Ex. 2.3.5 (p. 40) — fitter species' share $x$ obeys a logistic equation, solved analytically and geometrically — medium
- Ex. 2.4.9 (p. 41) — critical slowing down: $\dot x=-x^3$ decays algebraically, not exponentially, where $f'(0)=0$ — medium
- Ex. 2.5.5 (p. 42) — general non-uniqueness for $\dot x=|x|^{p/q}$, $x(0)=0$, depending on $p<q$ or $p>q$ — hard
- Ex. 2.6.1 (p. 42) — resolve the paradox that $m\ddot x=-kx$ oscillates in one dimension — easy
- Ex. 2.8.3 (p. 43) — test Euler's method on $\dot x=-x$ and see how the error scales with $\Delta t$ — easy

## Reading notes
- Printed page = pdf page − 15. The unit covers printed pp. 15–44; exercises are on pp. 36–44.
- The text layer is garbled in places: dots over $x$, "≥", "π", "τ", "Δ" and "∞" are corrupted. All formulas above were checked against the page images.
- Possible misprints in the exercises as shown in the images: Ex. 2.5.6(c) says "Combining (b) and (c)" where (a) and (b) seem meant. Ex. 2.8.3(c) writes "ln E vs. ln t" where $\ln\Delta t$ seems intended. Ex. 2.8.6(d) says "Repeat part (b)", where part (c) seems meant.
- Source name for the citation: the metadata says 3rd ed. (2024); no edition line is visible on these pages.
