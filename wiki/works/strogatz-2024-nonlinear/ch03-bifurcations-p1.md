---
id: strogatz-2024-nonlinear/ch03-bifurcations-p1
work: strogatz-2024-nonlinear
unit: "3 Bifurcations (part 1/2): §§3.0–3.5"
pages: 45–69
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
# Bifurcations of fixed points on the line (§§3.0–3.5)

## L0 — One line
In a one-dimensional flow, changing a parameter can create, destroy or swap the stability of fixed points, and three normal forms (saddle-node, transcritical, pitchfork) capture these changes.

## L1 — The gist (≤ 120 words)
One-dimensional flows have trivial dynamics at fixed parameters: solutions settle at a fixed point or go to infinity. What is interesting is how the flow changes qualitatively as a parameter varies. These changes are bifurcations. The chapter builds three normal forms: saddle-node ($\dot x=r\pm x^2$), transcritical ($\dot x=rx-x^2$) and pitchfork ($\dot x=rx\mp x^3$). It applies them to a laser threshold and to a bead on a rotating hoop. The subcritical pitchfork brings jumps and hysteresis. The hoop shows that dropping a second-order term is valid only after a fast transient. This gives a toolkit for modelling thresholds and transitions.

**Prerequisites:** first-order flows $\dot x=f(x)$, fixed points and linear stability ($f'(x^*)$ sign), Taylor series, chain rule, potentials $V$ with $f=-dV/dx$.

## L2 — Key ideas (5–10 bullets)
- A bifurcation is a qualitative change in the flow as a parameter varies. Such changes model transitions and instabilities, such as beam buckling (p. 45).
- Saddle-node: two fixed points approach, collide and annihilate. $\dot x=r\pm x^2$ is the prototype (called a "normal form": a standard equation that typical cases resemble), and close to such a bifurcation the dynamics typically look like it (pp. 46, 49–51).
- Transcritical: a fixed point exists for all $r$ and the two fixed points exchange stability without disappearing. This is the laser threshold mechanism (pp. 51–56).
- Supercritical pitchfork: in a symmetric system, a stable fixed point gives way to a symmetric pair. At $r=0$ the decay is slow (critical slowing down) (pp. 56–57).
- Subcritical pitchfork: the cubic term destabilises, so blow-up (escape to infinity in finite time) occurs in the pure cubic equation; a stabilising $x^5$ gives coexisting stable states, jumps and hysteresis (lack of reversibility when the parameter is varied back) (pp. 59–61).
- Graphical tricks: intersect two simple curves, or solve for the parameter as a function of $x^*$ (pp. 48–49, 58).
- Nondimensionalising (rewriting the equation with dimensionless variables) gives a small parameter $\varepsilon$ that suggests the first-order approximation for very strong damping (the overdamped limit) (pp. 65–67).
- The paradox of two versus one initial conditions is resolved by a phase-plane picture: a fast transient onto a curve, then slow drift (pp. 67–69).

## L3 — Walkthrough

### 3.0 Introduction (p. 45)
- On the line, solutions either settle at equilibrium or go to $\pm\infty$ (p. 45). The interest lies in **dependence on parameters**: fixed points can be created or destroyed, or change stability (p. 45).
- These qualitative changes are **bifurcations**. The parameter values where they occur are **bifurcation points** (p. 45).
- Example: the beam of Fig. 3.0.1. The weight is the control parameter, the deflection is $x$. Under a light load the vertical position is stable. Under a too-heavy load it becomes unstable and the beam may buckle (p. 45).

### 3.1 Saddle-node bifurcation (pp. 46–51)
- Mechanism: as a parameter varies, two fixed points move together, collide and annihilate (p. 46).
- Prototype:
$$\dot x = r + x^2 \tag{1}$$
  For $r<0$ there are two fixed points, one stable and one unstable. At $r=0$ they merge into a half-stable point $x^*=0$. For $r>0$ there are none. A bifurcation occurs at $r=0$ because the flows on either side differ qualitatively (p. 46).
- **Ways to draw it.** A stack of vector fields (Fig. 3.1.2). A continuous stack gives the curve $r=-x^2$, with solid line for stable and broken line for unstable points (Fig. 3.1.3). Most commonly the axes are swapped so that $r$ is horizontal. This is the **bifurcation diagram** (Fig. 3.1.4) (pp. 46–47).
- **Terminology.** Also called fold or turning-point bifurcation. "Saddle-node" comes from the analogous planar case (Section 8.1). Viewed in the opposite direction it is a **blue sky bifurcation**: a pair appears "out of the clear blue sky" (pp. 47–48). The word "bifurcation" means "splitting into two branches" (p. 48).
- Version with $r$ reversed:
$$\dot x = r - x^2 \tag{2}$$
  It has no fixed points for $r<0$, one at $r=0$, and two for $r>0$ (p. 48).
- **Example 3.1.1.** For $\dot x=r-x^2$: $x^*=\pm\sqrt r$ exist for $r>0$. With $f'(x^*)=-2x^*$, $x^*=+\sqrt r$ is stable and $x^*=-\sqrt r$ is unstable. At $r=0$, $f'(x^*)=0$: the linearisation vanishes when the points coalesce (p. 48).
- **Example 3.1.2.** $\dot x=r-x-e^{-x}$. The fixed points cannot be found explicitly as a function of $r$. Plot the line $r-x$ and the curve $e^{-x}$. Intersections are fixed points. Flow is to the right where the line lies above the curve (p. 49). The right intersection is stable and the left one unstable. Lowering $r$ slides the line down until it is tangent to the curve. Below that value there are no fixed points (p. 49). Tangency requires equal functions and equal derivatives: $e^{-x}=r-x$ and $-e^{-x}=-1$. So $x=0$, $r=1$. The bifurcation point is $r_c=1$ at $x=0$ (p. 49).
- **Normal forms.** Near the bifurcation of Example 3.1.2, expand $e^{-x}$ about $x=0$:
$$\dot x=r-x-\Big[1-x+\tfrac{x^2}{2!}+\dots\Big]=(r-1)-\tfrac{x^2}{2}+\dots$$
  To leading order in $x$ this has the algebraic form of $\dot x=r-x^2$, and can be made to agree exactly by rescaling $x$ and $r$ (p. 50).
- **Why this form is typical.** Two fixed points can collide only if $f(x)$ has two nearby roots, so $f$ must look locally bowl-shaped (parabolic) (Fig. 3.1.7). Zooming in shows a parabola crossing, touching, then missing the axis (p. 50).
- **Algebraic version.** Write $\dot x=f(x,r)$ near $x=x^*$, $r=r_c$. Neglecting quadratic terms in $(r-r_c)$ and cubic terms in $(x-x^*)$ (pp. 50–51):
$$\dot x = f(x^*,r_c)+(x-x^*)\frac{\partial f}{\partial x}\Big|_{(x^*,r_c)}+(r-r_c)\frac{\partial f}{\partial r}\Big|_{(x^*,r_c)}+\tfrac12 (x-x^*)^2\frac{\partial^2 f}{\partial x^2}\Big|_{(x^*,r_c)}+\cdots$$
  The first term vanishes because $x^*$ is a fixed point. The second vanishes by the tangency condition of a saddle-node bifurcation. Hence (p. 51)
$$\dot x = a(r-r_c)+b(x-x^*)^2+\cdots \tag{3}$$
  with $a=\partial f/\partial r|_{(x^*,r_c)}$ and $b=\tfrac12\partial^2 f/\partial x^2|_{(x^*,r_c)}$. This assumes $a,b\neq 0$, the typical case (p. 51).
- The prototypes are the **normal forms** of the saddle-node bifurcation. Normal-form theory is said to hold much more than is shown here (p. 51).

*Intuition note:* A typical smooth system that loses two fixed points at once looks, close up, like a parabola sliding off the axis. So one simple equation describes such a bifurcation locally, in the typical case where $a$ and $b$ are not zero.

### 3.2 Transcritical bifurcation (pp. 51–54)
- Used when a fixed point must exist for every parameter value, for example the zero-population state in the logistic equation. Its stability may still change (p. 51).
- Normal form:
$$\dot x = rx - x^2 \tag{1}$$
  This resembles the logistic equation, but $x$ and $r$ may now take either sign. $x^*=0$ exists for all $r$ (p. 51).
- For $r<0$: $x^*=r$ is unstable and $x^*=0$ is stable. As $r$ increases they merge at $r=0$. For $r>0$ the origin is unstable and $x^*=r$ is stable. This is an **exchange of stabilities** (p. 52).
- Contrast with the saddle-node: here the two fixed points do not disappear. They only switch stability (p. 52). The bifurcation diagram is Fig. 3.2.2 (p. 52).
- **Example 3.2.1.** $\dot x=x(1-x^2)-a(1-e^{-bx})$. Since $x=0$ is always a fixed point, it is plausible that this fixed point will bifurcate transcritically, if it bifurcates at all (p. 52). For small $x$: $1-e^{-bx}=bx-\tfrac12b^2x^2+O(x^3)$. Therefore
$$\dot x=(1-ab)x+(\tfrac12ab^2)x^2+O(x^3).$$
  The bifurcation curve is $ab=1$. The other fixed point solves $1-ab+(\tfrac12ab^2)x\approx0$, so
$$x^*\approx\frac{2(ab-1)}{ab^2}.$$
  This is approximately correct only when $x^*$ is small, i.e. when $ab$ is close to 1 (p. 53).
- **Example 3.2.2.** $\dot x=r\ln x+x-1$ near $x=1$, which is a fixed point for all $r$. Put $u=x-1$ (p. 53):
$$\dot u=r\ln(1+u)+u=r[u-\tfrac12u^2+O(u^3)]+u\approx(r+1)u-\tfrac12ru^2+O(u^3).$$
  So $r_c=-1$. To remove the $u^2$ coefficient, let $u=av$. Then $\dot v=(r+1)v-(\tfrac12ra)v^2+O(v^3)$. Choosing $a=2/r$ gives $\dot v=(r+1)v-v^2+O(v^3)$. With $R=r+1$ and $X=v$ this is $\dot X\approx RX-X^2$, where $X=u/a=\tfrac12r(x-1)$ (p. 53).
- Normal-form theory assures that a change of variables exists giving strict equality. The solution above approximates it (pp. 53–54).

### 3.3 Laser threshold (pp. 54–56)
- Physical picture (solid-state laser; the model follows Haken 1983). Excited atoms act as little antennas. With weak pumping they radiate independently, with random phases, like a lamp. Above a pump threshold they oscillate in phase and a coherent, intense beam appears (p. 54). The text calls this self-organizing: coherence arises from cooperation among atoms although the pump excites them randomly (p. 54).
- Model: the variable is the photon number $n(t)$ (p. 55).
$$\dot n=\text{gain}-\text{loss}=GnN-kn$$
  Gain comes from stimulated emission, at a rate proportional to $n$ and to the number of excited atoms $N(t)$, with $G>0$. Loss is photon escape, with $k>0$. $\tau=1/k$ is the typical photon lifetime (p. 55).
- Key idea: each emission de-excites an atom. Assume the pump alone would hold $N_0$ excited atoms, so (p. 55)
$$N(t)=N_0-\alpha n,\quad \alpha>0.$$
  Then
$$\dot n=Gn(N_0-\alpha n)-kn=(GN_0-k)n-(\alpha G)n^2.$$
  Only $n>0$ is physical (p. 55).
- Results: for $N_0<k/G$, $n^*=0$ is stable (lamp). At $N_0=k/G$ there is a transcritical bifurcation. For $N_0>k/G$ the origin is unstable and a stable point
$$n^*=\frac{GN_0-k}{\alpha G}>0$$
  appears (laser action). So $N_0=k/G$ is the laser threshold in this model (p. 56, Fig. 3.3.3).
- The model ignores the dynamics of the excited atoms, spontaneous emission and other effects. Improved models are in Exercises 3.3.1–3.3.2 (p. 56).

*Intuition note:* More pumping means more gain per photon. Below threshold, gain is smaller than loss and any light dies out. Above it, gain exceeds loss until atoms are depleted enough to balance, so a steady beam appears.

### 3.4 Pitchfork bifurcation (pp. 56–62)
- Common in problems with symmetry. Fixed points tend to appear and disappear in symmetric pairs. In the beam example, a vertical beam can buckle left or right, giving two symmetric new fixed points (p. 56).

**Supercritical pitchfork (pp. 56–59)**
$$\dot x=rx-x^3 \tag{1}$$
- Invariant under $x\to-x$, the left–right symmetry (p. 57).
- For $r<0$ the origin is the only fixed point and it is stable. At $r=0$ it is still stable but weakly, since the linearisation vanishes. Decay is algebraic rather than exponential (Exercise 2.4.9), called **critical slowing down** in physics. For $r>0$ the origin is unstable and two stable fixed points sit at $x^*=\pm\sqrt r$ (p. 57). The bifurcation diagram (Fig. 3.4.2) gives the "pitchfork" shape (p. 57).
- **Example 3.4.1.** $\dot x=-x+\beta\tanh x$ (magnet and neural-network models; the page image uses $\beta$). Fixed points are intersections of $y=x$ and $y=\beta\tanh x$. The slope of the tanh curve at the origin is $\beta$. For $\beta<1$ the origin is the only fixed point. At $\beta=1$ a pitchfork bifurcation occurs at $x^*=0$. For $\beta>1$ two new stable fixed points appear and the origin is unstable (p. 58). For accurate plotting, treat $x^*$ as the independent variable and compute $\beta=x^*/\tanh x^*$. Plot these pairs with $\beta$ horizontal. This works because $f(x,\beta)=-x+\beta\tanh x$ depends more simply on $\beta$ than on $x$ (pp. 58–59).
- **Example 3.4.2.** Potential for $\dot x=rx-x^3$: from $-dV/dx=rx-x^3$,
$$V(x)=-\tfrac12rx^2+\tfrac14x^4$$
  (constant dropped). For $r<0$ there is a quadratic minimum at the origin. At $r=0$ it is a flatter quartic minimum. For $r>0$ the origin is a local maximum with a symmetric pair of minima beside it (p. 59).

**Subcritical pitchfork (pp. 59–61)**
$$\dot x=rx+x^3 \tag{2}$$
- The cubic term is now destabilising. The pitchfork is inverted. $x^*=\pm\sqrt{-r}$ are unstable and exist only for $r<0$. The origin is stable for $r<0$ and unstable for $r>0$, but now the cubic term helps drive trajectories outward. This leads to **blow-up**: the text says $x(t)\to\pm\infty$ in finite time from any $x_0\neq0$ (Exercise 2.5.3) (p. 60).
- In real systems higher-order terms usually oppose this. With $x\to-x$ symmetry kept, the first stabilising term is $x^5$. The canonical example is
$$\dot x=rx+x^3-x^5 \tag{3}$$
  The coefficients of $x^3$ and $x^5$ may be taken as 1 without loss of generality (Exercise 3.5.8) (p. 60). The detailed analysis is left to Exercises 3.4.14–3.4.15; the text summarises it (pp. 60–61).
- Fig. 3.4.7: near the origin the picture is as in Fig. 3.4.6. The unstable branches turn around and become stable at $r=r_s<0$. Stable large-amplitude branches exist for all $r>r_s$ (pp. 60–61).
- Three points (p. 61):
  1. For $r_s<r<0$ two kinds of stable state coexist (origin and large-amplitude points). The initial condition decides which is approached. The origin is locally stable but not globally stable.
  2. **Jumps and hysteresis.** Start at $x^*=0$ and increase $r$. The state stays at the origin until $r=0$, then jumps to a large-amplitude branch. If $r$ is then decreased, the state stays on that branch even below $0$. It returns to the origin only after $r$ falls below $r_s$. This lack of reversibility is **hysteresis** (Fig. 3.4.8).
  3. The bifurcation at $r_s$ is a saddle-node bifurcation.
- **Terminology.** Supercritical: forward bifurcation, related to continuous (second-order) phase transitions; "soft" or "safe" in engineering because nonzero points are born at small amplitude. Subcritical: inverted or backward bifurcation, related to discontinuous (first-order) phase transitions; "hard" or "dangerous" because of the jump to large amplitude (pp. 61–62).

*Intuition note:* The sign of the cubic term decides what the bifurcation does. With a restoring cubic, new states grow gently from zero. With a destabilising cubic, nothing nearby holds the system, so it jumps far away and may not return when the cause is reversed.

### 3.5 Overdamped bead on a rotating hoop (pp. 62–69)
- **Setup.** A bead of mass $m$ slides on a hoop of radius $r$ that rotates at constant angular velocity $\omega$ about its vertical axis. The system sits in a very viscous fluid. Let $\phi\in(-\pi,\pi]$ be the angle from the downward vertical, and $\rho=r\sin\phi$ the distance from the axis (p. 62). Forces: gravity $mg$, centrifugal $m\rho\omega^2$, and damping $b\dot\phi$, all with $g,b>0$. Resolving along the tangent gives (pp. 62–63)
$$mr\ddot\phi=-b\dot\phi-mg\sin\phi+mr\omega^2\sin\phi\cos\phi \tag{1}$$
  This is second order. The plan is to neglect $mr\ddot\phi$ now and justify it later (p. 63).
- **First-order system.**
$$b\dot\phi=-mg\sin\phi+mr\omega^2\sin\phi\cos\phi=mg\sin\phi\Big(\frac{r\omega^2}{g}\cos\phi-1\Big) \tag{2}$$
  Fixed points: $\phi^*=0$ (bottom) and $\phi^*=\pi$ (top) always exist. There are two additional ones if $r\omega^2/g>1$, at $\phi^*=\pm\cos^{-1}(g/r\omega^2)$ (p. 63).
- Let $\gamma=r\omega^2/g$ and solve $\cos\phi^*=1/\gamma$ graphically (Fig. 3.5.4). For $\gamma<1$ there is no intersection. For $\gamma>1$ there is a symmetric pair. As $\gamma\to\infty$ they approach $\pm\pi/2$ (pp. 63–64). A supercritical pitchfork bifurcation occurs at $\gamma=1$. Checking stability is left to Exercise 3.5.2 (p. 65).
- **Physical reading.** For $\gamma<1$ the centrifugal force is too weak and the bead stays at the bottom. For $\gamma>1$ the bottom is unstable because any displacement is amplified. The bead rises until gravity balances the centrifugal force. Which of the two symmetric points is chosen depends on the initial disturbance. These are **symmetry-broken** solutions, with less symmetry than the equation. The equation is symmetric under $\phi\to-\phi$ (p. 65).
- **Dimensional analysis.** When may the inertia term $mr\ddot\phi$ be dropped? Taking $m\to0$ alone also kills gravity and centrifugal terms, so more care is needed (p. 65). Define dimensionless time $\tau=t/T$. By the chain rule $\dot\phi=\frac1T\frac{d\phi}{d\tau}$ and $\ddot\phi=\frac1{T^2}\frac{d^2\phi}{d\tau^2}$ (p. 66). Dividing (1) by $mg$:
$$\Big(\frac{r}{gT^2}\Big)\frac{d^2\phi}{d\tau^2}=-\Big(\frac{b}{mgT}\Big)\frac{d\phi}{d\tau}-\sin\phi+\Big(\frac{r\omega^2}{g}\Big)\sin\phi\cos\phi \tag{3}$$
- Want the left side negligible and the right-side terms comparable, so $b/(mgT)\approx O(1)$ and $r/(gT^2)\ll1$. The first sets $T=b/(mg)$. The second then becomes
$$\frac rg\Big(\frac{mg}{b}\Big)^2\ll1 \tag{4}$$
  i.e. $b^2\gg m^2gr$: strong damping or small mass, in a precise sense (pp. 66–67).
- Define
$$\varepsilon=\frac{m^2gr}{b^2} \tag{5}$$
  Then
$$\varepsilon\frac{d^2\phi}{d\tau^2}=-\frac{d\phi}{d\tau}-\sin\phi+\gamma\sin\phi\cos\phi \tag{6}$$
  The five parameters $m,g,r,\omega,b$ reduce to two groups, $\gamma$ and $\varepsilon$. For $\varepsilon\to0$ (overdamped limit), (6) should be well approximated by (p. 67)
$$\frac{d\phi}{d\tau}=f(\phi),\quad f(\phi)=-\sin\phi+\gamma\sin\phi\cos\phi=\sin\phi(\gamma\cos\phi-1) \tag{7}$$
- **A paradox.** The second-order equation needs two independent initial conditions (position and velocity). The first-order equation fixes the velocity once the position is given. So (7) cannot in general satisfy both (p. 67).
- **Phase plane.** Let $\Omega=\phi'=d\phi/d\tau$. An initial condition is a point $(\phi_0,\Omega_0)$ and the solution is a trajectory (p. 68). Rewrite (6) as $\varepsilon\Omega'=f(\phi)-\Omega$, giving the vector field (p. 68)
$$\phi'=\Omega \tag{8a}$$
$$\Omega'=\frac1\varepsilon\big(f(\phi)-\Omega\big) \tag{8b}$$
  The vector $(\phi',\Omega')$ is the local velocity of a "phase fluid" on the plane (p. 68).
- **Resolution.** For $\varepsilon\to0$, trajectories slam straight up or down onto the curve $C$: $f(\phi)=\Omega$. They then ooze slowly along it to a fixed point (Fig. 3.5.8) (p. 69). Order-of-magnitude argument: suppose the point lies an $O(1)$ distance below $C$, so $\Omega<f(\phi)$ and $f(\phi)-\Omega\approx O(1)$. Then (8b) gives $\Omega'\approx O(1/\varepsilon)\gg1$. The point zaps up to where $f(\phi)-\Omega\approx O(\varepsilon)$, which becomes indistinguishable from $C$ as $\varepsilon\to0$. On $C$, $\Omega\approx f(\phi)$, so $\phi'=f(\phi)$ approximately (p. 69).
- Conclusion: (6) behaves like (7) only after a rapid initial transient, during which $\varepsilon\,d^2\phi/d\tau^2$ cannot be neglected. The single time scale $T=b/mg$ fits the slow drift but not the fast transient (Exercise 3.5.5) (p. 69).

*Intuition note:* With very strong damping, the velocity is forced to follow the value $f(\phi)$ set by the position almost at once. The fast initial "zap" gets rid of the extra initial condition. After that the bead's motion is governed by the simple one-dimensional flow.

## Toy example (ours, not from the text)
Take $\dot x=r+2x-x^2$.
- Complete the square: $r+2x-x^2=(r+1)-(x-1)^2$. With $X=x-1$ and $R=r+1$ this is $\dot X=R-X^2$, the normal form (2) of §3.1 (added step).
- Fixed points: $x^*=1\pm\sqrt{r+1}$. Stability from $f'(x)=2-2x$.
- $r=0$: $x^*=1\pm1=0$ and $2$. $f'(0)=2>0$ so $0$ is unstable. $f'(2)=-2<0$ so $2$ is stable.
- $r=-1$: $x^*=1$ only, and $f'(1)=0$ (half-stable).
- $r=-2$: $r+1=-1<0$, so there are no real fixed points.
- The bifurcation is at $r_c=-1$, $x=1$. Moving $r$ from $0$ down to $-2$ destroys the pair.

## Concepts
- [[bifurcation]] — qualitative change of the flow as a parameter varies; bifurcation point = parameter value where it occurs (p. 45)
- [[saddle-node-fold-bifurcation]] — two fixed points collide and vanish. Normal form $\dot x=r\pm x^2$. Also called fold, turning-point or blue-sky bifurcation (pp. 46–48)
- [[fixed-point-and-stability]] — a state with $f(x^*)=0$, stable or unstable by sign of $f'(x^*)$ (p. 48)
- [[linear-stability-analysis]] — stability from the sign of $f'(x^*)$. At the saddle-node bifurcation point $f'(x^*)=0$: the linearisation vanishes (p. 48; also p. 57 for the pitchfork at $r=0$)
- [[hysteresis]] — lack of reversibility when a parameter is varied, from coexisting stable states (p. 61)
- [[critical-slowing-down]] — algebraic instead of exponential decay when the linearisation vanishes at $r=0$ of the pitchfork (p. 57)
- [[normal-form]] (new) — prototypical equation that the dynamics near a bifurcation typically look like, e.g. $\dot x=r-x^2$ (p. 51)
- [[transcritical-bifurcation]] (new) — fixed point exists for all $r$; two points exchange stability. $\dot x=rx-x^2$ (pp. 51–52)
- [[pitchfork-bifurcation]] (new) — symmetric pair appears or disappears. Supercritical: $\dot x=rx-x^3$. Subcritical: $\dot x=rx+x^3$ (pp. 56, 59)
- [[symmetry-breaking]] (new) — a solution with less symmetry than its governing equation (p. 65)
- [[nondimensionalization]] (new) — rescaling to dimensionless groups so "small" means $\ll 1$ (p. 65)
- [[overdamped-limit]] (new) — $\varepsilon\to0$ limit where the second-order equation reduces to first-order after a fast transient (pp. 67–69)
- [[state-space-phase-space]] — here the phase plane $(\phi,\Omega)$ for second-order systems (p. 68)

## Canonical instances
- [[beam-buckling]] — load as control parameter; vertical state becomes unstable and two buckled states are born (pp. 45, 56)
- [[laser-threshold]] — transcritical bifurcation in photon number at $N_0=k/G$ (pp. 54–56)
- [[bead-on-rotating-hoop]] — supercritical pitchfork at $\gamma=r\omega^2/g=1$ (pp. 62–65)
- [[tanh-magnet-neural-network-model]] — $\dot x=-x+\beta\tanh x$, pitchfork at $\beta=1$ (p. 58)

## Bridges (candidates)
- [structural-analogy] Subcritical pitchfork jumps and hysteresis ↔ complex systems: tipping points with hysteresis — coexisting stable states mean reversing the cause does not reverse the effect.
- [structural-analogy] Supercritical pitchfork and critical slowing down ↔ complex systems: early-warning signals near a tipping point — the text names slow decay at $r=0$ but not warning signals.
- [structural-analogy] Pitchfork as continuous (second-order) and subcritical as discontinuous (first-order) phase transition ↔ criticality / phase transition — the text states this relation (pp. 61–62).
- [metaphor] Laser onset of coherence from random pumping ↔ emergence / self-organization — the text calls it "self-organizing" (p. 54).

## Questions this raises
- What happens to these bifurcations when a small asymmetry breaks the $x\to-x$ symmetry of the pitchfork?
- How can one tell from data which bifurcation type a real system undergoes, such as soft versus hard onset?
- Which other fast–slow situations allow a high-order equation to be reduced, and how general is the "fast transient onto a curve" picture?
- What new bifurcations appear in two and three dimensions (the text promises more in later chapters, p. 46)?

## Reading notes
- This is part 1 of Chapter 3. It starts at §3.0 (printed p. 45) and ends at the end of §3.5 (printed p. 69). The remainder of the chapter, including exercises that this part refers to, is not covered. No exercise list appears in these pages, so no "Exercises" section is given.
- Printed page = pdf − 15.
- The text layer garbles symbols (Greek letters, minus signs, inequality signs). All math was checked against the page images. Example 3.4.1 uses $\beta$ in the image (the text layer showed "C"). The laser model uses $\alpha$.
- In Example 3.4.2 the page says "Recall from Section 2.7" for potentials; Section 2.7 is not in this unit.
- The claim on blow-up (p. 60) cites Exercise 2.5.3, not given here. The remark about subcritical systems uses "initial condition $x_0\neq0$" as printed.
