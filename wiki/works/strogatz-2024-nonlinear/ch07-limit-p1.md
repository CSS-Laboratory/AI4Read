---
id: strogatz-2024-nonlinear/ch07-limit-p1
work: strogatz-2024-nonlinear
unit: "7 Limit Cycles (part 1/2): sections 7.0–7.4 and the start of 7.5"
pages: 198–216
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
# Limit Cycles (part 1/2)

## L0 — One line
A limit cycle is an isolated closed orbit that only nonlinear systems can have; in the plane we have tests that rule such orbits out, theorems that prove they exist, and a large-μ approximation for the van der Pol cycle.

## L1 — The gist (≤ 120 words)
Self-sustained oscillations (heartbeat, pacemaker neurons, chemical clocks) are modelled by stable limit cycles. How can we tell whether a two-dimensional system has one? The chapter gives three ways to rule closed orbits out (gradient systems, Liapunov functions, Dulac's criterion). It then gives a way to prove they exist (Poincaré–Bendixson with a trapping region) and a theorem for a whole family of damped oscillators (Liénard). The Poincaré–Bendixson theorem also shows why the plane cannot host chaos. Finally, for strong nonlinearity the van der Pol cycle becomes a relaxation oscillation: slow crawls and fast jumps, with period about μ(3 − 2 ln 2).

**Prerequisites:** phase-plane vector fields and fixed points; Jacobian, trace and determinant; polar coordinates; divergence and Green's theorem; basic integration.

## L2 — Key ideas (5–10 bullets)
- A limit cycle is an isolated closed trajectory. Linear systems cannot have one, because scaling a periodic solution gives a whole family of closed orbits (p. 198–199).
- Gradient systems $\dot{\mathbf x}=-\nabla V$ have no closed orbits, because $V$ strictly decreases along any non-fixed trajectory. An energy-like function that falls along flows gives the same conclusion (p. 201–203).
- A Liapunov function (positive definite, with $\dot V<0$ away from the fixed point) proves global stability of the fixed point and rules out closed orbits. No systematic recipe exists to find one (p. 203–204).
- Dulac's criterion: if $\nabla\cdot(g\dot{\mathbf x})$ has one sign on a simply connected region, Green's theorem forbids closed orbits there. Again, no algorithm finds $g$ (p. 204–205).
- Poincaré–Bendixson: for a continuously differentiable field, a confined trajectory in a closed bounded region with no fixed points implies a closed orbit in that region. A trapping region supplies the confinement (p. 205–206).
- Glycolysis model: the trapping region is not enough, because a fixed point sits inside. If that point is a repeller (trace > 0), a closed orbit is guaranteed (p. 207–211).
- The theorem works only in the plane. Chaos needs $n\ge3$ (p. 212).
- Liénard's theorem gives a unique stable limit cycle under conditions on $f$ and $g$. Van der Pol satisfies them (p. 212–213).
- For $\mu\gg1$ the van der Pol cycle has slow crawls ($\Delta t\sim O(\mu)$) and fast jumps ($\Delta t\sim O(\mu^{-1})$), giving $T\approx\mu(3-2\ln2)$ (p. 215–216).

## L3 — Walkthrough

### 7.0 Introduction
- A **limit cycle** is an isolated closed trajectory. "Isolated" means neighbouring trajectories are not closed; they spiral toward or away from it (p. 198).
- If all neighbours approach it, it is **stable** (attracting). Otherwise it is unstable, or in exceptional cases half-stable (p. 198).
- Stable limit cycles model **self-sustained oscillations**: the system oscillates without periodic forcing. Examples listed: heartbeat, pacemaker neuron, daily body rhythms, oscillating chemical reactions, self-excited bridge and wing vibrations. After a small perturbation the system returns to the standard cycle (p. 198).
- Limit cycles are inherently nonlinear. A linear system $\dot{\mathbf x}=A\mathbf x$ can have closed orbits, but not isolated ones: if $\mathbf x(t)$ is periodic, so is $c\mathbf x(t)$ for any $c\neq0$ (p. 199).
- So in a linear oscillation the initial conditions fix the amplitude. A limit cycle's amplitude is set by the system's structure (p. 199).

*Intuition note:* "Isolated" means no neighbouring closed orbits, unlike a linear oscillation. If the cycle is also stable, nearby starts are pulled onto it, so the oscillation size is set by the system and not by the starting point.

### 7.1 Examples
**Example 7.1.1 (simple limit cycle).** $\dot r=r(1-r^2),\ \dot\theta=1,\ r\ge0$ \tag{1}.
- Radial and angular parts are uncoupled. As a vector field on the line, $r^*=0$ is unstable and $r^*=1$ is stable (p. 199).
- All trajectories except $r^*=0$ approach $r=1$ monotonically, while rotating at constant angular velocity. So they spiral toward a limit cycle at $r=1$ (p. 200).
- $x(t)=r\cos\theta$ settles to a sinusoid of constant amplitude, matching $x(t)=\cos(t+\theta_0)$ (p. 200).

**Example 7.1.2 (van der Pol).** $\ddot x+\mu(x^2-1)\dot x+x=0$, $\mu\ge0$ \tag{2}.
- It came from the nonlinear circuits of the first radios (p. 200).
- The term $\mu(x^2-1)\dot x$ is nonlinear damping. It is positive damping for $|x|>1$ and negative damping for $|x|<1$. Large oscillations decay and small ones are pumped up (p. 200).
- The system settles where energy dissipated per cycle balances energy pumped in. With "quite a bit of work" one proves a unique, stable limit cycle for each $\mu>0$, following from a theorem in Section 7.4 (p. 201).
- Numerical example: $\mu=1.5$, start $(x,\dot x)=(0.5,0)$. The cycle is not a circle and the waveform is not a sine wave (p. 201).

### 7.2 Ruling Out Closed Orbits
Index theory (Chapter 6) is one method. Three more follow; the author calls them of limited applicability (p. 201).

**Gradient systems.** A system $\dot{\mathbf x}=-\nabla V$, with $V(\mathbf x)$ continuously differentiable and single-valued, is a gradient system with potential $V$ (p. 201).

**Theorem 7.2.1.** Closed orbits are impossible in gradient systems.
*Proof.* Suppose a closed orbit of period $T$ exists. $\Delta V=0$ after one circuit since $V$ is single-valued. But
$$\Delta V=\int_0^T\frac{dV}{dt}\,dt=\int_0^T(\nabla V\cdot\dot{\mathbf x})\,dt=-\int_0^T\|\dot{\mathbf x}\|^2dt<0,$$
unless $\dot{\mathbf x}\equiv\mathbf 0$, which would be a fixed point, not a closed orbit. Contradiction (p. 201–202).

- Most 2D systems are not gradient systems. All vector fields on the line are, which explains again why there are no oscillations there (p. 202).
- **Example 7.2.1.** $\dot x=\sin y,\ \dot y=x\cos y$ is gradient with $V=-x\sin y$, since $\dot x=-\partial V/\partial x$ and $\dot y=-\partial V/\partial y$. So no closed orbits (p. 202).
- **Example 7.2.2.** $\ddot x+(\dot x)^3+x=0$ has no periodic solutions. Take $E=\tfrac12(x^2+\dot x^2)$. Around a closed orbit $\Delta E=0$. But $\dot E=\dot x(x+\ddot x)=\dot x(-\dot x^3)=-\dot x^4\le0$, so $\Delta E=-\int_0^T(\dot x)^4dt<0$ unless $\dot x\equiv0$, which is a fixed point. Contradiction (p. 202–203).

**Liapunov functions.** Consider $\dot{\mathbf x}=\mathbf f(\mathbf x)$ with fixed point $\mathbf x^*$. A *Liapunov function* is a continuously differentiable real $V(\mathbf x)$ with (p. 203):
1. $V(\mathbf x)>0$ for all $\mathbf x\neq\mathbf x^*$, and $V(\mathbf x^*)=0$ (positive definite);
2. $\dot V<0$ for all $\mathbf x\neq\mathbf x^*$.

Then $\mathbf x^*$ is globally asymptotically stable ($\mathbf x(t)\to\mathbf x^*$ for all initial conditions). In particular there are no closed orbits. The proof is cited to Jordan and Smith (1987) (p. 203). Trajectories cannot stall elsewhere, since $V$ would then stop changing while $\dot V<0$ (p. 203). No systematic construction exists; "divine inspiration" is usually needed, and sums of squares occasionally work (p. 203).

*Intuition note:* Picture a bowl with its bottom at $\mathbf x^*$. If every trajectory must go strictly downhill, it cannot come back to where it started, so it cannot loop.

**Example 7.2.3.** $\dot x=-x+4y,\ \dot y=-x-y^3$. Try $V=x^2+ay^2$. Then
$$\dot V=2x\dot x+2ay\dot y=2x(-x+4y)+2ay(-x-y^3)=-2x^2+(8-2a)xy-2ay^4.$$
Choosing $a=4$ kills the $xy$ term: $\dot V=-2x^2-8y^4$. Then $V>0$ and $\dot V<0$ for $(x,y)\neq(0,0)$, so $V=x^2+4y^2$ is a Liapunov function. No closed orbits; all trajectories approach the origin (p. 203–204).

**Dulac's criterion.** Let $\dot{\mathbf x}=\mathbf f(\mathbf x)$ be continuously differentiable on a simply connected subset $R$ of the plane. If some continuously differentiable real $g(\mathbf x)$ makes $\nabla\cdot(g\dot{\mathbf x})$ have one sign throughout $R$, then no closed orbit lies entirely in $R$ (p. 204).
*Proof.* Suppose a closed orbit $C$ lies in $R$, enclosing region $A$, with outward normal $\mathbf n$. Green's theorem gives
$$\iint_A\nabla\cdot(g\dot{\mathbf x})\,dA=\oint_C g\dot{\mathbf x}\cdot\mathbf n\,d\ell.$$
The left side is nonzero because the integrand has one sign. The right side is zero because $\dot{\mathbf x}\cdot\mathbf n=0$ on a trajectory. Contradiction (p. 204).

- No algorithm finds $g$. Candidates that occasionally work: $g=1,\ 1/x^ay^b,\ e^{ax},\ e^{ay}$ (p. 204).
- **Example 7.2.4.** $\dot x=x(2-x-y),\ \dot y=y(4x-x^2-3)$ in $x,y>0$. With $g=1/(xy)$: $\nabla\cdot(g\dot{\mathbf x})=\partial_x\!\big(\tfrac{2-x-y}{y}\big)+\partial_y\!\big(\tfrac{4x-x^2-3}{x}\big)=-1/y<0$. The quadrant is simply connected, so no closed orbits (p. 205).
- **Example 7.2.5.** $\dot x=y,\ \dot y=-x-y+x^2+y^2$ with $g=e^{-2x}$: $\nabla\cdot(g\dot{\mathbf x})=-2e^{-2x}y+e^{-2x}(-1+2y)=-e^{-2x}<0$. No closed orbits (p. 205).

### 7.3 Poincaré–Bendixson Theorem
**Theorem.** Suppose (1) $R$ is a closed, bounded subset of the plane; (2) $\dot{\mathbf x}=\mathbf f(\mathbf x)$ is continuously differentiable on an open set containing $R$; (3) $R$ has no fixed points; (4) a trajectory $C$ is confined in $R$ (starts in $R$, stays for all future time). Then either $C$ is a closed orbit or it spirals toward one as $t\to\infty$. Either way, $R$ contains a closed orbit (p. 205). The proof is subtle and needs topology; references are given (p. 205–206).

- Because a closed orbit must encircle a fixed point, $R$ is drawn ring-shaped (p. 206).
- Conditions (1)–(3) are easy; (4) is hard. The standard trick is a **trapping region**: a closed connected set whose boundary has the vector field pointing inward everywhere. All trajectories inside are then confined. If it has no fixed points, it contains a closed orbit (p. 206).

**Example 7.3.1.** $\dot r=r(1-r^2)+\mu r\cos\theta,\ \dot\theta=1$ \tag{1}. Show a closed orbit survives for small $\mu>0$.
- Seek circles $r_{\min},r_{\max}$ with $\dot r>0$ on the inner and $\dot r<0$ on the outer. Then the annulus $0<r_{\min}\le r\le r_{\max}$ is trapping. It has no fixed points since $\dot\theta=1>0$ (p. 206).
- Since $\cos\theta\ge-1$, a sufficient condition for $\dot r>0$ on the inner circle is $1-r^2-\mu>0$. So any $r_{\min}<\sqrt{1-\mu}$ works when $\mu<1$; e.g. $r_{\min}=0.999\sqrt{1-\mu}$. Similarly $r_{\max}=1.001\sqrt{1+\mu}$ (p. 206).
- Conclusion: a closed orbit exists for all $\mu<1$, within $0.999\sqrt{1-\mu}<r<1.001\sqrt{1+\mu}$ (p. 207). These estimates are conservative; the orbit can exist for $\mu\ge1$ (Figure 7.3.3 shows $\mu=1$) (p. 207).

**Example 7.3.2 (glycolysis, Sel'kov model).** $\dot x=-x+ay+x^2y,\ \dot y=b-ay-x^2y$, with $x,y$ the concentrations of ADP and F6P and $a,b>0$ (p. 207–208). Construct a trapping region.
- Nullclines (curves where one velocity component is zero): $\dot x=0$ on $y=x/(a+x^2)$; $\dot y=0$ on $y=b/(a+x^2)$. The signs of $\dot x,\dot y$ in each region give the arrows. Above both nullclines, $\dot x>0$ and $\dot y<0$ (p. 208).
- The box has horizontal and vertical sides that are fine by Figure 7.3.4. The tricky side is a diagonal of slope $-1$ from $(b,b/a)$ to the nullcline $y=x/(a+x^2)$ (p. 208).
- Why: at large $x$, $\dot x\approx x^2y$ and $\dot y\approx-x^2y$, so $dy/dx\approx-1$. Compare $\dot x$ and $-\dot y$:
$$\dot x-(-\dot y)=-x+ay+x^2y+(b-ay-x^2y)=b-x.$$
So $-\dot y>\dot x$ if $x>b$. Then $dy/dx$ is more negative than $-1$, the vectors are steeper than the diagonal, and the field points inward there (p. 209).
- Poincaré–Bendixson does *not* apply directly, since a fixed point lies inside (nullcline intersection). If that point is a **repeller**, cut an infinitesimal hole around it. The repeller pushes trajectories into the punctured region, which has no fixed points, so the theorem applies (p. 209–210).

**Example 7.3.3.** Find the condition on $a,b$ for a closed orbit. It suffices that the fixed point is an unstable node or spiral (p. 210). Jacobian:
$$A=\begin{pmatrix}-1+2xy & a+x^2\\ -2xy & -(a+x^2)\end{pmatrix}.$$
At the fixed point $x^*=b,\ y^*=b/(a+b^2)$ (after "some algebra"): determinant $\Delta=a+b^2>0$ and trace
$$\tau=-\frac{b^4+(2a-1)b^2+(a+a^2)}{a+b^2}.$$
The fixed point is unstable for $\tau>0$ and stable for $\tau<0$. The dividing line $\tau=0$ is $b^2=\tfrac12\big(1-2a\pm\sqrt{1-8a}\big)$, a curve in $(a,b)$ space (Figure 7.3.7) (p. 210–211). For $\tau>0$ a closed orbit is guaranteed; numerical integration shows it is a stable limit cycle (typical case $a=0.08,\ b=0.6$) (p. 211).

*Intuition note:* Inward-pointing boundary traps the flow. If the fixed point inside is a repeller, trajectories cannot end there, so by Poincaré–Bendixson a trajectory in the punctured region approaches a closed orbit.

**No chaos in the phase plane.** The theorem says a trajectory confined to a closed bounded region without fixed points must approach a closed orbit; nothing more complicated is possible. This depends on two-dimensionality. For $n\ge3$ trajectories may wander forever in a bounded region, possibly on a strange attractor (a fractal set with aperiodic motion, sensitive to tiny initial changes). Hence chaos can never occur in the phase plane (p. 212).

### 7.4 Liénard Systems
- Many oscillating circuits (c. 1920–1950 research) are modelled by $\ddot x+f(x)\dot x+g(x)=0$ \tag{1}, Liénard's equation. It generalises van der Pol and describes a unit mass with nonlinear damping $f(x)\dot x$ and nonlinear restoring force $g(x)$ (p. 212).
- Equivalent system: $\dot x=y,\ \dot y=-g(x)-f(x)y$ \tag{2} (p. 212).

**Liénard's Theorem.** Suppose (1) $f,g$ are continuously differentiable for all $x$; (2) $g$ is odd; (3) $g(x)>0$ for $x>0$; (4) $f$ is even; (5) the odd function $F(x)=\int_0^xf(u)\,du$ has exactly one positive zero at $x=a$, is negative for $0<x<a$, is positive and nondecreasing for $x>a$, and $F(x)\to\infty$ as $x\to\infty$. Then system (2) has a unique, stable limit cycle surrounding the origin (p. 212–213). Proofs are cited to other books (p. 212).
- Plausibility: $g$ acts like a spring; $f$ means negative damping at small $|x|$ and positive at large $|x|$. Small oscillations grow and large ones shrink (p. 213).

**Example 7.4.1.** Van der Pol has $f=\mu(x^2-1)$, $g=x$. Conditions (1)–(4) are clear. $F(x)=\mu(\tfrac13x^3-x)=\tfrac13\mu x(x^2-3)$, so (5) holds with $a=\sqrt3$. Hence a unique, stable limit cycle (p. 213).

### 7.5 Relaxation Oscillations (start of section)
Now the question is quantitative: given a closed orbit, what are its shape and period? Approximations are possible when a parameter is large or small (p. 213). For $\mu\gg1$ the van der Pol limit cycle is a slow buildup then a sudden discharge, repeated. This is a **relaxation oscillation**. Other examples named: stick-slip bowed violin string, nerve cells firing under constant current (p. 214).

**Example 7.5.1 (phase plane for $\mu\gg1$).**
- Since $\ddot x+\mu\dot x(x^2-1)=\frac{d}{dt}\big(\dot x+\mu[\tfrac13x^3-x]\big)$, set
$$F(x)=\tfrac13x^3-x,\qquad w=\dot x+\mu F(x)\tag{1}$$
so that $\dot w=\ddot x+\mu\dot x(x^2-1)=-x$ \tag{2}. Equivalent system: $\dot x=w-\mu F(x),\ \dot w=-x$ \tag{3} (p. 214).
- With $y=w/\mu$: $\dot x=\mu[y-F(x)],\ \dot y=-\tfrac1\mu x$ \tag{4} (p. 214).
- Claimed picture (Figure 7.5.1): from any point except the origin, the trajectory moves horizontally onto the cubic nullcline $y=F(x)$, crawls along it to the knee B, jumps to the other branch at C, crawls to D, and repeats (p. 215).
- Justification. If $y-F(x)\sim O(1)$, then $|\dot x|\sim O(\mu)\gg1$ and $|\dot y|\sim O(\mu^{-1})\ll1$: motion is almost horizontal. Above the nullcline $\dot x>0$, so the trajectory moves toward it. Once $y-F(x)\sim O(\mu^{-2})$, both $\dot x,\dot y$ are $O(\mu^{-1})$. The trajectory crosses the nullcline vertically and creeps along the branch's backside at speed $O(\mu^{-1})$ until the knee (p. 215).
- Two widely separated time scales: crawls take $\Delta t\sim O(\mu)$, jumps $\Delta t\sim O(\mu^{-1})$. Figure 7.5.2 shows both for $\mu=10$, start $(2,0)$ (p. 215).

**Example 7.5.2 (period for $\mu\gg1$).**
- Jump time is negligible, so $T\approx2\int_{t_A}^{t_B}dt$ over one slow branch (the two branches take equal time by symmetry) (p. 216).
- On a slow branch $y\approx F(x)$, so $\dot y\approx F'(x)\dot x=(x^2-1)\dot x$. With $\dot y=-x/\mu$ from (4): $\dot x=-x/[\mu(x^2-1)]$, so
$$dt\approx-\frac{\mu(x^2-1)}{x}\,dx.\tag{5}$$
- The positive branch runs from $x_A=2$ to $x_B=1$ (Exercise 7.5.1 asks to check). Then
$$T\approx2\int_2^1\frac{-\mu}{x}(x^2-1)\,dx=2\mu\Big[\frac{x^2}{2}-\ln x\Big]_1^2=\mu[3-2\ln2],\tag{6}$$
which is $O(\mu)$ as expected (p. 216).
- Refinement ("with much more work"): $T\approx\mu[3-2\ln2]+2\alpha\mu^{-1/3}+\dots$, where $\alpha\approx2.338$ is the smallest root of $\mathrm{Ai}(-\alpha)=0$ (Airy function). The correction estimates the time to turn the corner between jumps (p. 216; the sentence continues past this unit).

*Intuition note:* Almost all of the period is spent creeping along the cubic nullcline; the jumps are nearly instantaneous. So, for $\mu\gg1$, the period grows in proportion to $\mu$.

## Toy example (ours, not from the text)
System: $\dot r=r(4-r^2),\ \dot\theta=1$. Does it have a closed orbit between $r=1$ and $r=3$?
- At $r=1$: $\dot r=1\cdot(4-1)=3>0$, so the flow points outward, i.e. into the annulus.
- At $r=3$: $\dot r=3\cdot(4-9)=-15<0$, so the flow points inward, i.e. into the annulus.
- So $1\le r\le3$ is a trapping region. It has no fixed points because $\dot\theta=1\ne0$. Poincaré–Bendixson gives a closed orbit in the annulus.
- Check (added step): $r=2$ gives $\dot r=2(4-4)=0$, so the orbit is the circle $r=2$. It is stable, since $\dot r>0$ for $0<r<2$ and $\dot r<0$ for $r>2$.

## Concepts
- [[limit cycle]] — isolated closed trajectory; stable if neighbours approach it (p. 198)
- [[nonlinearity]] — here: limit cycles cannot occur in linear systems, whose closed orbits form non-isolated families (p. 199)
- [[fixed point and stability]] — used for $r^*=0,1$ and for the repeller test via trace and determinant (p. 199, 210)
- [[linear stability analysis]] — Jacobian trace and determinant decide the fixed point's type in Example 7.3.3 (p. 210)
- [[state space / phase space]] — the plane, with trajectories, nullclines and trapping regions (p. 205–206)
- [[deterministic chaos]] — said to be impossible in the phase plane (p. 212)
- [[strange attractor / fractal]] — mentioned as what higher-dimensional systems can have (p. 212)
- [[gradient-system]] (new) — $\dot{\mathbf x}=-\nabla V$; no closed orbits (p. 201)
- [[liapunov-function]] (new) — positive definite $V$ with $\dot V<0$ away from $\mathbf x^*$ (p. 203)
- [[dulac-criterion]] (new) — one-signed $\nabla\cdot(g\dot{\mathbf x})$ on a simply connected region forbids closed orbits (p. 204)
- [[trapping-region]] (new) — closed connected set with inward-pointing field on its boundary (p. 206)
- [[poincare-bendixson-theorem]] (new) — confined trajectory without fixed points implies a closed orbit (p. 205)
- [[lienard-system]] (new) — $\ddot x+f(x)\dot x+g(x)=0$ (p. 212)
- [[relaxation-oscillation]] (new) — slow buildup and sudden discharge, with two separated time scales (p. 214–215)
- [[nullcline]] (new) — curve where $\dot x=0$ or $\dot y=0$ (p. 208)

## Canonical instances
- [[van-der-pol-oscillator]] — nonlinear damping gives a unique stable limit cycle; for $\mu=1.5$ it is not a circle, and for $\mu\gg1$ it is a relaxation oscillation with $T\approx\mu(3-2\ln2)$ (p. 200–201, 213–216)
- [[sel-kov-glycolysis-model]] — chemical oscillator with a trapping region and a fixed point that is a repeller when $\tau>0$ (p. 207–211)
- [[simple-polar-limit-cycle]] — $\dot r=r(1-r^2),\ \dot\theta=1$ (p. 199–200)

## Bridges (candidates)
- [structural-analogy] Liapunov function / gradient potential ↔ optimisation: a loss function that decreases along update steps rules out cycling — both use a strictly decreasing quantity to forbid loops.
- [structural-analogy] Relaxation oscillation (slow buildup, fast discharge) ↔ neuron firing and stick-slip: the text names both as other contexts where relaxation oscillations occur (p. 214).
- [metaphor] Trapping region ↔ absorbing sets in a model: the system cannot leave, so its long-run behaviour is limited to what lies inside.

## Questions this raises
- Beyond uniqueness in Liénard systems, how can one decide how *many* limit cycles a given planar system has?
- What happens at the parameter curve $\tau=0$ in the glycolysis model, where the fixed point changes from stable to unstable?
- In three dimensions, which extra ingredients turn a bounded, non-settling trajectory into a strange attractor?
- Why does the correction to the large-$\mu$ period scale like $\mu^{-1/3}$?

## Reading notes
- This part starts at the chapter opening (Section 7.0, printed p. 198) and ends at printed p. 216, in the middle of Section 7.5 (after Example 7.5.2, in the middle of the sentence about the $\mu^{-1/3}$ correction; later pages are not covered).
- Printed page numbers are visible and match the labels (printed = pdf − 15).
- The text layer has garbled symbols (e.g. $\mu$, $\theta$, $\tau$, inequality signs); all math was checked against the page images.
- Exercises (7.1.6, 7.2.5, 7.2.6, 7.3.8, 7.3.9, 7.5.1) are only referred to in these pages; none is printed, so no exercise list is given.
- Proofs of Liapunov stability, Poincaré–Bendixson and Liénard are not given; the author cites other books.
