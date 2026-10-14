---
id: spielman-2025-sagt/ch18-dynamic
work: spielman-2025-sagt
unit: "Chapter 18 — Dynamic and Nonlinear Networks"
pages: 155-162
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Dynamic and Nonlinear Networks

## L0 — One line
Resistor networks with nonlinear resistors keep a unique, energy-minimizing equilibrium, and the author argues that a thermistor network (resistors that heat up) has an equilibrium law of this type; in the low-ambient-temperature limit its energy minimization becomes a minimum s-t cut.

## L1 — The gist (≤ 120 words)
How much of the classical resistor-network theory survives when resistors are nonlinear, or when resistance changes over time? For nonlinear resistors with a continuous, increasing, odd flow law φ (flow versus voltage drop on an edge), fixed boundary voltages give a unique valid flow. It is the minimizer of a convex energy, and a dual flow-energy gives the same flow. The chapter links this to semi-supervised learning with |x(a)−x(b)|^p penalties. A thermistor model (resistance proportional to temperature) has an equilibrium flow law of this nonlinear type. When the ambient temperature goes to zero (all α_e=1), its energy minimization becomes a minimum s-t cut. Convergence of the dynamics is stated, not proved.

**Prerequisites:** potentials, flows and flow conservation in resistor networks (Ohm's law); convex functions; partial derivatives; a first-order ODE; s-t cuts.

## L2 — Key ideas (5–10 bullets)
- A nonlinear resistor has a flow law φ_e(v), assumed continuous, monotone increasing and odd; the linear resistor φ=v/r is a special case (pp. 155–156).
- Integrating φ gives a strictly convex edge energy Φ_e; minimizing total energy gives the unique valid flow for fixed boundary voltages (Thm 18.3.1, p. 157).
- Penalties |x(a)−x(b)|^p, 1<p<2, can improve semi-supervised learning but are slower to minimize than p=2 (pp. 157–158).
- The inverse ψ=φ⁻¹ gives a dual flow-energy Ψ. Minimizing Ψ over compatible flows gives the same flow (Thm 18.5.1, p. 158).
- Φ(v)+Ψ(f)=vf when f=φ(v) (Thm 18.5.2, p. 159); the author also states Φ+Ψ ≥ vf in general, without proof (p. 158).
- Thermistor model: ∂T_e/∂t = r_e f_e² − (T_e−T_A) with r_e=α_eT_e. With fixed voltages, convergence is claimed, not proved (pp. 160–161).
- At equilibrium the thermistor flow law is (18.3), which satisfies a–c, so a stable solution exists (p. 161).
- With all α_e=1 and T_A→0, the energy becomes Σ|v(a)−v(b)|; the author says its minimum is achieved by a minimum s-t cut (pp. 161–162).

## L3 — Walkthrough

**18.1–18.2 Non-linear networks (pp. 155–156).** Overview: two generalizations are studied, nonlinear resistors and resistances that change over time. Non-linear networks were introduced over 50 years ago; the time-varying material is from Cameron Musco's 2012 senior thesis (p. 155). Duffin's model: flow over edge e is φ_e(v) for potential difference v. Assumptions: (a) continuous, (b) monotone increasing, (c) symmetric, φ_e(−v)=−φ_e(v), so φ_e(0)=0. Ordinary resistor: φ_e(v)=v/r. Claim, proved next: if the graph is connected and voltages are fixed at some vertices, voltages elsewhere exist that give flow-in = flow-out at non-boundary vertices, and the flow is unique (p. 156).

**18.3 Energy (pp. 156–157).** Define $\Phi_e(v)\overset{\text{def}}{=}\int_0^v\phi_e(t)\,dt$. For $\phi_e(v)=v/r$ this is $\tfrac12 v^2/r$, the Lecture 13 energy. Conditions a–c imply: (d) Φ_e strictly convex (a convex function that lies strictly below its chords), (e) Φ_e(0)=0, (f) Φ_e(−x)=Φ_e(x). A strictly convex function has a unique minimum; sums of strictly convex functions are strictly convex (p. 156).

**Theorem 18.3.1.** (The source prints $f_e$ for $\phi_e$; see Reading notes.) For any $S\subseteq V$ and fixed voltages $w_a$, $a\in S$, voltages $v_a$ for $a\notin S$ exist that give flow-in = flow-out at every $a\notin S$, and they are unique (p. 157).

*Proof.* Let $\Phi(v)=\sum_{(a,b)\in E}\Phi_{(a,b)}(v_a-v_b)$, strictly convex, so it has a minimum subject to the fixed voltages. At the minimum, for every $a\notin S$:
$$0=\frac{\partial\Phi(v)}{\partial v_a}=\sum_{b:(a,b)\in E}\frac{\partial\Phi_{(a,b)}(v_a-v_b)}{\partial v_a}=\sum_{b:(a,b)\in E}\phi_{(a,b)}(v_a-v_b).$$
Set $f_{(a,b)}=\phi_{(a,b)}(v_a-v_b)$. This is a valid flow, since the signed flows out of each $a\notin S$ sum to zero. Conversely, any voltages with no loss or gain at $a\notin S$ make all partial derivatives zero. By strict convexity that happens only at the unique minimum (p. 157).

*Intuition note:* Equilibrium voltages are exactly where total energy is lowest among settings that respect the fixed boundary voltages. Because the energy is strictly convex, there is only one such point.

**18.4 Semi-supervised learning (pp. 157–158).** Lecture 13 estimates $f$ on $V$ from its values on $S$ by $\min_{x:\,x(a)=f(a),\,a\in S}\sum_{(a,b)\in E}(x(a)-x(b))^2$, solved by linear equations. The author says this sometimes works poorly. Bridle and Zhu (and, essentially, Herbster and Guy) suggest $\sum|x(a)-x(b)|^p$ with $1<p<2$. A well-chosen $p$ often improves accuracy, but minimization is much slower than for $p=2$ (p. 158).

**18.5 Dual energy (pp. 158–159).** Let $\psi=\phi^{-1}$ and $\Psi(f)\overset{\text{def}}{=}\int_0^f\psi(t)\,dt$. Minimizing the summed flow-energies over flows again gives the unique valid flow (Φ is implicit in Duffin, Ψ is from Millar). Classically Φ=Ψ; here they differ, but when $v=\psi(f)$ their sum is $vf$ (to be proved later, p. 158). Stated: for all $f,v$, $\Psi(f)+\Phi(v)\ge fv$, with equality only when $v=\psi(f)$ (p. 158).

**Theorem 18.5.1.** Under 18.3.1's conditions, let $f_{ext}$ be the external flows from the induced voltages. The flow $f$ compatible with $f_{ext}$ that minimizes $\Psi(f)=\sum\Psi_{(a,b)}(f_{(a,b)})$ is the flow induced by the voltages of Theorem 18.3.1 (p. 158).

*Sketch.* It suffices to show $f$ is a potential flow ($f_{(a,b)}=\phi_{(a,b)}(v_a-v_b)$ for some $v$), then use uniqueness. Desired differences $\psi(f_{(a,b)})$ are realizable as potentials iff they sum to zero around every cycle (fix one vertex's potential, sum along paths). Minimality: pushing $\epsilon$ of flow around a cycle leaves $\Psi$ unchanged to first order. Since $\partial\Psi_e/\partial f=\psi_e(f)$, the sum of desired differences around each cycle is zero (pp. 158–159).

**Theorem 18.5.2.** If $f=\phi(v)$ then $\Phi(v)+\Psi(f)=vf$. Proof by picture: Φ(v) is the area under the φ curve from 0 to $v$. Ψ(f) is the area between the curve and the $f$-axis, up to height $\phi(v)$. These are complementary parts of the rectangle with corner $(v,\phi(v))$ (p. 159). Author's conclusion: almost all classical theory carries over (p. 159).

*Intuition note:* The area under a curve plus the area to its left fills the rectangle $v\times f$. So voltage-based and flow-based energies are two views of one rectangle.

**18.6 Thermistor networks (pp. 160–161).** A thermistor's resistance rises with temperature. Heat produced is resistance × flow². Temperatures relax toward an ambient $T_A$. With $r_e=\alpha_eT_e$ (18.1), $T_e\ge0$:
$$\frac{\partial T_e}{\partial t}=r_ef_e^2-(T_e-T_A)\tag{18.2}$$
(constant on the second term set to 1), so $\partial T_e/\partial t=\alpha_eT_ef_e^2-(T_e-T_A)$ (p. 160).

*Imposed current need not converge.* One resistor with $\alpha_e=2$ gives $\partial T_e/\partial t=2T_e-(T_e-T_A)=T_e+T_A$ (added step: this takes $f_e=1$, which the text leaves implicit), so $T_e\to\infty$. The author therefore prefers to fix voltages instead, and says convergence can then be proved; he does not prove it (p. 160).

*Equilibrium.* If everything converges, $0=\alpha_eT_ef_e^2-(T_e-T_A)$. Using $f_er_e=v_e$, i.e. $f_e\alpha_eT_e=v_e$: $0=v_ef_e-T_e+T_A$. Multiplying by $f_e$: $0=v_ef_e^2-v_e/\alpha_e+f_eT_A$. The roots are $f_e=\pm\sqrt{1/\alpha_e+(T_A/2v_e)^2}-T_A/(2v_e)$. Choosing the sign that gives $f_e$ the same sign as $v_e$ (p. 161):
$$f_e=\frac1{2v_e}\left(\sqrt{\frac{(2v_e)^2}{\alpha_e}+T_A^2}-T_A\right)\tag{18.3}$$
This tends to 0 for small $v_e$ (set to 0 at $v_e=0$) and to $\pm\alpha_e^{-1/2}$ for large $|v_e|$. Defining $\phi_e(v_e)$ as (18.3), the author says it satisfies a, b, c. Theorem 18.3.1 then gives a stable solution (p. 161).

*Intuition note:* A heated resistor resists more, so flow saturates at $\alpha_e^{-1/2}$ however large the voltage. That saturating law is nonlinear but monotone, so the earlier theory applies.

**18.7 Low temperatures (pp. 161–162).** Take all $\alpha_e=1$ and $T_A\to0$: $\phi_e=0$ if $v_e=0$, $1$ if $v_e>0$, $-1$ if $v_e<0$. For small $T_A$ the behaviour is similar. Each edge has flow near 1 or a negligible drop, with energy near 1 or near 0 respectively (pp. 161–162). The minimization becomes
$$\min_{v:\,v(s)=0,\,v(t)=1}\sum_{(a,b)\in E}|v(a)-v(b)|$$
(Integrating the limiting φ gives |v|: added step.) The author says one can show the minimum occurs at all-0/1 voltages. The energy is then the number of edges between voltage 0 and 1, so the minimizer is a minimum s-t cut (p. 162).

## Toy example (ours)
Path s–m–t. Edge 1 (s,m) is linear, φ₁(v)=v. Edge 2 (m,t) has φ₂(v)=v³ (continuous, increasing, odd). Fix $v_s=1$, $v_t=0$; unknown $x=v_m$.
- Flow conservation at m: $1-x=x^3$, i.e. $x^3+x-1=0$.
- Energy: $\Phi(x)=\tfrac12(1-x)^2+\tfrac14x^4$, with $\Phi'(x)=-(1-x)+x^3$, the same equation.
- Check: $\Phi'(0.68)=-0.32+0.3144\approx-0.006<0$ and $\Phi'(0.69)=-0.31+0.3285\approx0.019>0$, so the unique root is in (0.68, 0.69). Flow ≈ 0.32 on each edge.
- Duality check on edge 2 at $v=0.5$: $f=0.125$, $\psi(f)=f^{1/3}$, $\Phi=0.5^4/4=0.015625$, $\Psi=\tfrac34 f^{4/3}=0.75\cdot0.0625=0.046875$. Sum $=0.0625=fv=0.125\cdot0.5$ ✓.

## Concepts
- [[nonlinear-resistor-network]] (new) — resistor network where edge flow is $\phi_e(v)$, continuous, increasing, odd (p. 155–156)
- [[edge-energy-potential]] (new) — $\Phi_e(v)=\int_0^v\phi_e$; strictly convex; minimizing its sum gives the equilibrium (p. 156)
- [[dual-flow-energy]] (new) — $\Psi(f)=\int_0^f\psi$, $\psi=\phi^{-1}$; minimizing over flows gives the same equilibrium (p. 158)
- [[potential-flow]] (new) — a flow with $f_{(a,b)}=\phi_{(a,b)}(v_a-v_b)$ for some vertex potentials (p. 158)
- [[thermistor-network]] (new) — resistance $r_e=\alpha_eT_e$ evolving by (18.2) (pp. 160–161)
- [[minimum-s-t-cut]] (new) — a cut separating $s$ from $t$ with fewest edges (with 0/1 voltages, $v(s)=0$, $v(t)=1$, the number of edges between 0 and 1); the author says it achieves the minimum of $\sum|v(a)-v(b)|$ in the low-temperature limit (p. 162)

## Canonical instances
- [[thermistor-divergence-example]] — one resistor, $\alpha_e=2$, imposed current: temperature diverges (p. 160)
- [[p-penalty-semi-supervised]] — $|x(a)-x(b)|^p$, $1<p<2$, in place of squares (pp. 157–158)

## Bridges (candidates)
- [structural-analogy] Dual energies Φ, Ψ with $\Phi+\Psi\ge fv$ ↔ convex analysis: conjugate functions and the Fenchel–Young inequality — same rectangle-area picture.
- [same-math] Linear case $\Phi=\tfrac12v^2/r$ ↔ graph Laplacian: quadratic form $\sum(x(a)-x(b))^2$ (the source calls it the Lecture 13 energy).
- [structural-analogy] Low-temperature limit $\sum|v(a)-v(b)|$ ↔ total variation / min-cut relaxations.

## Questions this raises
- Why is minimization for $1<p<2$ slower than for $p=2$?
- How is convergence of the thermistor dynamics proved with fixed voltages?
- How does the small-$T_A$ solution relate to the exact min cut, and how small must $T_A$ be?
- How do the weights $\alpha_e$ enter the edge weights of the cut when they are not all 1?

## Reading notes
- Printed page = pdf − 24.
- The chapter opens with a note that it is unedited.
- Theorem 18.3.1 prints "functions $f_e$" where context requires $\phi_e$.
- Theorem 18.5.1 is only sketched. Theorem 18.5.2's proof is a picture. Convergence (18.6), the claim that (18.3) satisfies a–c, and the 0/1 optimality (18.7) are asserted, not proved.
- Inequality Ψ+Φ ≥ fv is stated without proof. Typos: "situtations", "Equivalenty".
