---
id: strogatz-2024-nonlinear/ch05-linear
work: strogatz-2024-nonlinear
unit: "5 Linear Systems"
pages: 125-145
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
# Linear Systems (two-dimensional)

## L0 — One line
The phase portrait of a 2D linear system $\dot{\mathbf x}=A\mathbf x$ is fixed by the eigenvalues and eigenvectors of $A$; since the eigenvalues depend only on the trace $\tau$ and determinant $\Delta$, one $(\Delta,\tau)$ diagram shows the type and stability of the fixed points (stars and degenerate nodes share a borderline).

## L1 — The gist (≤ 120 words)
How can we understand motion in the phase plane without solving equations by hand? For $\dot{\mathbf x}=A\mathbf x$, look for straight-line solutions $e^{\lambda t}\mathbf v$. These exist when $\mathbf v$ is an eigenvector of $A$ with eigenvalue $\lambda$. For distinct eigenvalues, combining the two eigensolutions gives the general solution. The eigenvalues depend only on $\tau$ and $\Delta$, so one $(\Delta,\tau)$ diagram sorts all fixed points: saddles, nodes, spirals, and borderline cases such as centers. The chapter also defines stability terms. It ends with a love-affair model. This matters because linear systems also play an important role in classifying fixed points of nonlinear systems.

**Prerequisites:** matrix–vector multiplication; eigenvalues and eigenvectors; determinant and trace of a 2×2 matrix; complex numbers and Euler's formula; solving $\dot x=ax$; the ideas of fixed point and vector field.

## L2 — Key ideas
- A linear system obeys superposition, and $\mathbf x^*=\mathbf 0$ is always a fixed point (p. 126).
- Phase-plane pictures show the behaviour of a system without solving it; the oscillator's closed orbits are periodic motions (pp. 126–128).
- When the matrix is diagonal, $\dot x=ax,\ \dot y=-y$, varying $a$ gives node, star, line of fixed points, and saddle (pp. 129–130).
- Stability has two independent notions: attracting (nearby trajectories approach the point as $t\to\infty$) and Liapunov stable (nearby trajectories stay nearby for all time). "Stable" means both (pp. 130–131).
- Straight-line solutions $e^{\lambda t}\mathbf v$ (eigensolutions) exist when $A\mathbf v=\lambda\mathbf v$. Distinct eigenvalues give the general solution (6) (pp. 131–133).
- Eigenvalues are roots of $\lambda^2-\tau\lambda+\Delta=0$. They are real or complex, giving nodes, saddles, spirals (trajectories winding around the point) and centers (closed orbits) (pp. 132, 135–136).
- Equal eigenvalues give a star node (straight-line trajectories through the origin; two independent eigenvectors, $A=\lambda I$ with $\lambda\ne0$) or a degenerate node (one eigendirection) (pp. 136–138).
- The $(\Delta,\tau)$ diagram classifies all fixed points. Saddles, nodes and spirals fill open regions; centers, stars, degenerate nodes and non-isolated points are borderline (pp. 138–139).
- In the love-affair model, equal cautious lovers end in indifference or in an explosive relationship, depending on $a^2$ versus $b^2$ (pp. 140–141).

## L3 — Walkthrough

### 5.0–5.1 Definitions and examples
Higher-dimensional phase spaces allow richer behaviour than 1D flows, so the author starts with linear systems in two dimensions (p. 125). They matter in their own right and for classifying fixed points of nonlinear systems (p. 125).

A **two-dimensional linear system** is
$$\dot x=ax+by,\qquad \dot y=cx+dy,$$
or $\dot{\mathbf x}=A\mathbf x$ with $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $\mathbf x=\begin{pmatrix}x\\y\end{pmatrix}$ (p. 125). It is linear because if $\mathbf x_1,\mathbf x_2$ are solutions, so is $c_1\mathbf x_1+c_2\mathbf x_2$. Also $\dot{\mathbf x}=\mathbf 0$ when $\mathbf x=\mathbf 0$, so $\mathbf x^*=\mathbf 0$ is a fixed point for every $A$ (p. 126). Solutions are trajectories in the $(x,y)$ plane, called the **phase plane** (p. 126).

**Example 5.1.1 (simple harmonic oscillator).** The equation is $m\ddot x+kx=0$, with $x$ the displacement from equilibrium (p. 126). The aim is to deduce behaviour without solving it (p. 126). The state is position $x$ and velocity $v$, so with $\omega^2=k/m$:
$$\dot x=v,\qquad \dot v=-\omega^2x \tag{3}$$
This assigns the vector $(v,-\omega^2x)$ at each point, a **vector field** on the phase plane (p. 126).
- On the $x$-axis the vectors point down for $x>0$ and up for $x<0$, and get longer as $|x|$ grows.
- On the $v$-axis the field is $(v,0)$: right for $v>0$, left for $v<0$ (p. 127).

Picture an imaginary fluid flowing with this velocity. A **phase point** placed at $(x_0,v_0)$ is carried by the flow (p. 127). The origin is a fixed point. Every other phase point circulates and returns to its start, so the trajectories are **closed orbits**. The picture of all trajectories is the **phase portrait** (p. 127).

Interpretation: the fixed point is static equilibrium. Closed orbits are periodic oscillations (p. 127). At most negative $x$ the velocity is zero (spring most compressed). The mass then speeds back through $x=0$, overshoots, stops at the other extreme, and returns (p. 128). The orbits are ellipses $\omega^2x^2+v^2=C$ with $C\ge0$. The author leaves the derivation and the link to energy conservation to Exercise 5.1.1 (p. 128).

**Example 5.1.2 (diagonal case).** Take $A=\begin{pmatrix}a&0\\0&-1\end{pmatrix}$. The equations $\dot x=ax,\ \dot y=-y$ are **uncoupled** (no $x$ in the $y$-equation and vice versa), so each is solved separately (p. 129):
$$x(t)=x_0e^{at},\qquad y(t)=y_0e^{-t}.\tag{1}$$
In every case $y$ decays. For $a<0$, $x$ decays too, so all trajectories approach the origin; the direction of approach depends on how $a$ compares with $-1$ (p. 129). The cases (Fig. 5.1.5):
- **$a<-1$:** $x$ decays faster than $y$. Trajectories approach the origin tangent to the slower direction (the $y$-axis). Looking backward in time, they become parallel to the faster direction (the $x$-axis). The author says this follows from the slope $dy/dx=\dot y/\dot x$ (Exercise 5.1.2). The origin is a **stable node** (pp. 129–130).
- **$a=-1$:** $y/x=y_0/x_0$ is constant, so all trajectories are straight lines through the origin. This happens because the two decay rates are precisely equal. The point is a **symmetrical node or star** (p. 130).
- **$-1<a<0$:** again a node, but trajectories now approach along the $x$-direction, which decays more slowly for this range of $a$ (p. 130).
- **$a=0$:** $x(t)\equiv x_0$. There is an entire **line of fixed points** on the $x$-axis, and trajectories approach it along vertical lines (p. 130).
- **$a>0$:** the origin is unstable because of exponential growth in $x$. Most trajectories head to infinity. Trajectories starting on the $y$-axis go to the origin, "walking a tightrope". The origin is a **saddle point** (p. 130).

For a saddle, the **stable manifold** is the set of initial conditions $\mathbf x_0$ with $\mathbf x(t)\to\mathbf x^*$ as $t\to\infty$; here it is the $y$-axis. The **unstable manifold** is the set with $\mathbf x(t)\to\mathbf x^*$ as $t\to-\infty$; here it is the $x$-axis. A typical trajectory approaches the unstable manifold as $t\to\infty$ and the stable manifold as $t\to-\infty$ (p. 130).

*Intuition note:* In a diagonal system each axis is a line along which motion is simple exponential growth or decay. The relative decay rates decide which axis the trajectories hug.

**Stability language** (informal here; precise definitions in Exercise 5.1.10) (pp. 130–131):
- **Attracting:** all trajectories starting near $\mathbf x^*$ approach it as $t\to\infty$. If it attracts all trajectories, it is **globally attracting** (p. 130).
- **Liapunov stable:** trajectories that start sufficiently close to $\mathbf x^*$ stay close for all time (p. 130).
- **Neutrally stable:** Liapunov stable but not attracting, as in Fig. 5.1.5d. The oscillator's equilibrium is another example. This is common in mechanical systems without friction (pp. 130–131).
- Neither notion implies the other. Counterexample: $\dot\theta=1-\cos\theta$ on the circle. The point $\theta^*=0$ attracts all trajectories but is not Liapunov stable, since some trajectories starting infinitesimally close make a large excursion (p. 131).
- **Stable** (or **asymptotically stable**) means both Liapunov stable and attracting. The origin in Fig. 5.1.5e is **unstable** because it is neither attracting nor Liapunov stable (p. 131).
- Graphics: open dots mark unstable fixed points, solid dots mark Liapunov stable ones (p. 131).

*Intuition note:* "Attracting" asks where trajectories end. "Liapunov stable" asks whether they stray far on the way. They are different questions.

### 5.2 Classification of linear systems
Idea: find analogues of the coordinate-axis straight-line solutions. Try
$$\mathbf x(t)=e^{\lambda t}\mathbf v,\quad \mathbf v\ne\mathbf 0\tag{2}$$
(p. 131). Substituting into $\dot{\mathbf x}=A\mathbf x$ gives $\lambda e^{\lambda t}\mathbf v=e^{\lambda t}A\mathbf v$. Cancelling $e^{\lambda t}$:
$$A\mathbf v=\lambda\mathbf v\tag{3}$$
So the solution (2) exists if $\mathbf v$ is an eigenvector of $A$ with eigenvalue $\lambda$; it is then called an **eigensolution** (p. 132).

The eigenvalues satisfy $\det(A-\lambda I)=0$. For a 2×2 matrix this expands to
$$\lambda^2-\tau\lambda+\Delta=0\tag{4}$$
with $\tau=\operatorname{trace}(A)=a+d$ and $\Delta=\det(A)=ad-bc$. Then
$$\lambda_1=\frac{\tau+\sqrt{\tau^2-4\Delta}}{2},\qquad \lambda_2=\frac{\tau-\sqrt{\tau^2-4\Delta}}{2}\tag{5}$$
so the eigenvalues depend only on $\tau$ and $\Delta$ (p. 132).

If $\lambda_1\ne\lambda_2$, a linear-algebra theorem says the eigenvectors $\mathbf v_1,\mathbf v_2$ are linearly independent and span the plane. So any $\mathbf x_0=c_1\mathbf v_1+c_2\mathbf v_2$, and
$$\mathbf x(t)=c_1e^{\lambda_1t}\mathbf v_1+c_2e^{\lambda_2t}\mathbf v_2\tag{6}$$
is the general solution. It is a linear combination of solutions, so it is a solution. It satisfies $\mathbf x(0)=\mathbf x_0$, so by the existence and uniqueness theorem (Section 6.2) it is the only one (pp. 132–133).

**Example 5.2.1.** Solve $\dot x=x+y,\ \dot y=4x-2y$ with $(x_0,y_0)=(2,-3)$.
- $\tau=-1$, $\Delta=-6$, so $\lambda^2+\lambda-6=0$ and $\lambda_1=2,\ \lambda_2=-3$ (p. 133).
- For $\lambda_1=2$: $\begin{pmatrix}-1&1\\4&-4\end{pmatrix}\mathbf v=\mathbf 0$ gives $\mathbf v_1=(1,1)$. For $\lambda_2=-3$: $\begin{pmatrix}4&1\\4&1\end{pmatrix}\mathbf v=\mathbf 0$ gives $\mathbf v_2=(1,-4)$ (p. 133).
- General solution: $\mathbf x(t)=c_1\binom11e^{2t}+c_2\binom{1}{-4}e^{-3t}$ (7).
- At $t=0$: $2=c_1+c_2$, $-3=c_1-4c_2$, so $c_1=1,\ c_2=1$ (p. 134).
- Result: $x(t)=e^{2t}+e^{-3t}$, $y(t)=e^{2t}-4e^{-3t}$ (p. 134).

**Example 5.2.2.** For this system one eigensolution grows ($\lambda_1=2$) and one decays ($\lambda_2=-3$), so the origin is a saddle. The stable manifold is the line spanned by $\mathbf v_2=(1,-4)$ and the unstable manifold is the line spanned by $\mathbf v_1=(1,1)$ (p. 134). All one needs for the phase portrait is the eigenvalues and eigenvectors (p. 134).

**Example 5.2.3 (both eigenvalues negative, $\lambda_2<\lambda_1<0$).** Both eigensolutions decay: a stable node, but the eigenvectors are in general not perpendicular. Trajectories typically approach tangent to the **slow eigendirection** (eigenvector with smaller $|\lambda|$). In backward time they become parallel to the fast eigendirection. Reversing all arrows in Fig. 5.2.3 gives a typical phase portrait for an unstable node (p. 135).

**Example 5.2.4 (complex eigenvalues).** Complex eigenvalues give a **center** or a **spiral** (p. 135). Complex eigenvalues occur when $\tau^2-4\Delta<0$. Write $\lambda_{1,2}=\alpha\pm i\omega$ with $\alpha=\tau/2$, $\omega=\tfrac12\sqrt{4\Delta-\tau^2}\ne0$. The eigenvalues are distinct, so (6) still holds, but the $c$'s and $\mathbf v$'s are complex. By Euler's formula $e^{i\omega t}=\cos\omega t+i\sin\omega t$, so $\mathbf x(t)$ combines $e^{\alpha t}\cos\omega t$ and $e^{\alpha t}\sin\omega t$ (p. 136).
- $\alpha<0$: decaying oscillations, a **stable spiral**.
- $\alpha>0$: growing oscillations, an **unstable spiral**.
- $\alpha=0$ (pure imaginary): all solutions are periodic with period $T=2\pi/\omega$, fixed amplitude, and the point is a center. Centers are neutrally stable (pp. 135–136).

A lightly damped oscillator would give a spiral, since it loses a little energy each cycle (p. 135). The sense of rotation is found by computing a few vectors of the field (p. 136).

*Intuition note:* Complex eigenvalues mean rotation. The real part $\alpha$ sets whether the rotation shrinks, grows or keeps its size.

**Example 5.2.5 (equal eigenvalues $\lambda_1=\lambda_2=\lambda$).** Two cases (p. 136):
- *Two independent eigenvectors:* every vector is an eigenvector, because $A\mathbf x_0=c_1\lambda\mathbf v_1+c_2\lambda\mathbf v_2=\lambda\mathbf x_0$. So $A=\lambda I$. For $\lambda\ne0$ trajectories $\mathbf x(t)=e^{\lambda t}\mathbf x_0$ are straight lines and the point is a **star node**. For $\lambda=0$ the whole plane consists of fixed points (p. 137).
- *Only one eigenvector* (one-dimensional eigenspace): for example $A=\begin{pmatrix}\lambda&b\\0&\lambda\end{pmatrix}$ with $b\ne0$ (Exercise 5.2.11). The point is a **degenerate node**. As $t\to\pm\infty$ all trajectories become parallel to the single eigendirection (p. 137).

The degenerate node can be seen as an ordinary node whose two eigendirections are "scissored together". It is also on the borderline between a spiral and a node (pp. 137–138).

**Classification of fixed points (Fig. 5.2.8).** The axes are $\tau$ and $\Delta$. From $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-\tau\lambda+\Delta$:
$$\Delta=\lambda_1\lambda_2,\qquad \tau=\lambda_1+\lambda_2 .$$
Together with (5) these give (p. 138):
- $\Delta<0$: real eigenvalues of opposite sign, a saddle.
- $\Delta>0$: either real with the same sign (nodes, $\tau^2-4\Delta>0$) or complex conjugate (spirals and centers, $\tau^2-4\Delta<0$).
- The parabola $\tau^2-4\Delta=0$ separates nodes from spirals; star and degenerate nodes lie on it.
- $\tau<0$: both eigenvalues have negative real parts, so stable. $\tau>0$: unstable spirals and nodes. Centers lie on $\tau=0$.
- $\Delta=0$: at least one eigenvalue is zero. The origin is not isolated: a line of fixed points, or a plane if $A=0$ (p. 139).

Saddles, nodes and spirals occupy large open regions. Centers, stars, degenerate nodes and non-isolated fixed points are borderline cases lying on curves. Of these, centers are by far the most important; they are common in frictionless, energy-conserving mechanical systems (p. 139).

**Examples 5.2.6–5.2.7.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $\Delta=-2<0$, so a saddle. For $A=\begin{pmatrix}2&1\\3&4\end{pmatrix}$, $\Delta=5$, $\tau=6$, $\tau^2-4\Delta=16>0$: a node, unstable since $\tau>0$ (p. 139).

*Intuition note:* $\Delta<0$ means real eigenvalues of opposite sign (a saddle). For $\Delta>0$, the sign of $\tau$ decides stable versus unstable. The sign of $\tau^2-4\Delta$ says whether the eigenvalues are real or complex.

### 5.3 Love affairs
Romeo loves Juliet. Juliet is fickle: the more he loves her, the more she wants to run away. Romeo echoes her feelings (p. 139). Let $R(t)$, $J(t)$ be Romeo's and Juliet's love (positive) or hate (negative) at time $t$. The model is
$$\dot R=aJ,\qquad \dot J=-bR,\quad a,b>0$$
The origin is a center: a never-ending cycle of love and hate. They achieve simultaneous love one-quarter of the time (p. 140).

The general model is $\dot R=aR+bJ,\ \dot J=cR+dJ$ with parameters of either sign. The signs specify "romantic styles"; $a>0,b>0$ is an "eager beaver" (p. 140). The author leaves naming the other styles to the exercises (p. 140).

**Example 5.3.1 (two identically cautious lovers).** $\dot R=aR+bJ,\ \dot J=bR+aJ$ with $a<0,\ b>0$. Here $a$ measures cautiousness and $b$ responsiveness. Then $A=\begin{pmatrix}a&b\\b&a\end{pmatrix}$ and (p. 141):
$$\tau=2a<0,\qquad \Delta=a^2-b^2,\qquad \tau^2-4\Delta=4b^2>0 .$$
The origin is a saddle if $a^2<b^2$ and a stable node if $a^2>b^2$. The eigenpairs are $\lambda_1=a+b,\ \mathbf v_1=(1,1)$ and $\lambda_2=a-b,\ \mathbf v_2=(1,-1)$. Since $a+b>a-b$, $(1,1)$ spans the unstable manifold in the saddle case and the slow eigendirection in the node case (p. 141).
- $a^2>b^2$: the relationship fizzles out to mutual indifference (the author: the lesson "seems to be that excessive caution can lead to apathy").
- $a^2<b^2$: explosive. Depending on initial feelings it becomes a love fest or a war, and all trajectories approach the line $R=J$, so feelings become mutual (p. 141).

## Toy example (ours)
System: $\dot x=3x-2y,\ \dot y=2x-2y$, with $\mathbf x(0)=(3,3)$.
1. $\tau=3+(-2)=1$, $\Delta=3(-2)-(-2)(2)=-6+4=-2<0$, so the origin is a saddle.
2. $\lambda^2-\lambda-2=0$ gives $\lambda=2$ and $\lambda=-1$.
3. For $\lambda=2$: $\begin{pmatrix}1&-2\\2&-4\end{pmatrix}\mathbf v=\mathbf 0$ gives $\mathbf v_1=(2,1)$. Check: $A(2,1)=(6-2,\,4-2)=(4,2)=2(2,1)$.
4. For $\lambda=-1$: $\begin{pmatrix}4&-2\\2&-1\end{pmatrix}\mathbf v=\mathbf 0$ gives $\mathbf v_2=(1,2)$. Check: $A(1,2)=(3-4,\,2-4)=(-1,-2)$.
5. $(3,3)=c_1(2,1)+c_2(1,2)$ gives $3=2c_1+c_2$ and $3=c_1+2c_2$, so $c_1=c_2=1$.
6. $\mathbf x(t)=(2e^{2t}+e^{-t},\ e^{2t}+2e^{-t})$. At $t=0$ this is $(3,3)$.
7. Stable manifold: the line through $(1,2)$. A start at $(1,2)$ gives $\mathbf x=e^{-t}(1,2)\to\mathbf 0$. Unstable manifold: the line through $(2,1)$. Other starts, such as $(3,3)$, drift toward the unstable line as $t\to\infty$.

## Concepts
- [[linear-system-2d]] (new) — $\dot{\mathbf x}=A\mathbf x$ with a 2×2 matrix; superposition holds; the origin is always a fixed point (pp. 125–126)
- [[state-space-phase-space]] — here the phase plane, with state $(x,v)$ or $(x,y)$ and solutions drawn as trajectories (pp. 126–127)
- [[fixed-point-stability]] — attracting, Liapunov stable, neutrally stable, asymptotically stable, unstable (pp. 130–131)
- [[linear-stability-analysis]] — here only the linear case: type read from eigenvalues, equivalently from $\tau$ and $\Delta$ (pp. 132, 138)
- [[eigensolution]] (new) — a solution $e^{\lambda t}\mathbf v$ with $A\mathbf v=\lambda\mathbf v$ (pp. 131–132)
- [[stable-unstable-manifold]] (new) — sets of initial conditions that approach the saddle as $t\to+\infty$ or $t\to-\infty$ (p. 130)
- [[fixed-point-types-2d]] (new) — node, star, degenerate node, saddle, spiral, center, line or plane of fixed points (pp. 129–139)
- [[trace-determinant-classification]] (new) — the $(\Delta,\tau)$ diagram of Fig. 5.2.8 (p. 138)
- [[attractor-basin]] — only touched on (global attraction of the origin in Fig. 5.1.5a–c) (p. 130)

## Canonical instances
- [[simple-harmonic-oscillator]] — center, closed elliptical orbits (pp. 126–128)
- [[damped-oscillator-spiral]] — a lightly damped oscillator would give a spiral (p. 135)
- [[romeo-juliet-love-model]] — $\dot R=aJ,\ \dot J=-bR$ gives a center; the cautious-lovers case gives saddle or node (pp. 139–141)
- [[theta-dot-1-minus-cos-theta]] — attracting but not Liapunov-stable point on the circle (p. 131)

## Bridges (candidates)
- [structural-analogy] $\tau,\Delta$ classification ↔ complex systems: in the linearised neighbourhood of a fixed point, stability is read from the eigenvalues. The chapter says the classification will matter for nonlinear systems (p. 125).
- [structural-analogy] Saddle with stable and unstable manifolds ↔ tipping points and path dependence: only start points on the stable line reach the fixed point, others are pushed away.
- [metaphor] Romeo–Juliet feedback ↔ micromotives vs. macrobehavior: simple personal rules give outcomes (cycle, apathy, war) that neither partner chose.

## Questions this raises
- What changes when the system is nonlinear: which parts of this classification survive near a fixed point?
- Centers are borderline cases. What happens to a center under a small nonlinear perturbation, or small damping?
- How would the love model change with more than two people, or with non-constant coefficients?
- In which settings is "attracting but not Liapunov stable" important, as with $\dot\theta=1-\cos\theta$?

## Exercises worth doing
- Ex. 5.1.1 (p. 142) — derive the elliptical orbits and link them to energy conservation — difficulty: easy
- Ex. 5.1.10 (p. 142) — classify examples as attracting, Liapunov stable, asymptotically stable or none — difficulty: medium
- Ex. 5.1.9 (p. 142) — a saddle solved by decoupling with new variables $u,v$ — difficulty: medium
- Ex. 5.2.2 (p. 144) — turn a complex-eigenvalue solution into real sines and cosines — difficulty: medium
- Ex. 5.2.11 (p. 144) — show a degenerate-node matrix has a one-dimensional eigenspace — difficulty: medium
- Ex. 5.2.14 (p. 145) — probability of each fixed-point type for random matrices (Monte Carlo) — difficulty: hard

## Reading notes
- Printed page = pdf − 15 (pdf 140 = printed 125).
- The text layer has garbled symbols: $\lambda$ appears as "M", $\tau$ as "U", $\Delta$ as "%", $\omega$ as "X", $\pi$ as "Q", $\alpha$ as "B", and minus signs and arrows are often lost. I checked the equations against the page images.
- In the image of Fig. 5.1.5(c), the caption reads "=1 <a<0", which appears to be a misprint for "−1 < a < 0". The text on p. 130 says $-1<a<0$.
- The unit contains the exercises printed on pp. 142–145. They are listed above, not solved.
- Figure 5.2.8 puts $\tau$ on the vertical axis and $\Delta$ on the horizontal axis. The text calls it the "(Δ,τ) plane" on p. 139.
- The oscillator Example 5.1.1 uses $x$ for displacement and also uses $v$ for velocity.
