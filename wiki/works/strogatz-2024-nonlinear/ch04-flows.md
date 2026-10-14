---
id: strogatz-2024-nonlinear/ch04-flows
work: strogatz-2024-nonlinear
unit: "4 Flows on the Circle"
pages: 95-122
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Flows on the Circle

## L0 — One line
A first-order flow on a circle can oscillate, and the nonuniform oscillator $\dot\theta=\omega-a\sin\theta$ appears in pendulums, fireflies and Josephson junctions, with a saddle-node bifurcation ending the oscillation.

## L1 — The gist (≤ 120 words)
What can a one-dimensional flow do if its phase space is a circle instead of a line? Because the circle closes on itself, a particle can return to its starting point, so periodic solutions appear for the first time. The chapter studies the uniform oscillator $\dot\theta=\omega$ and the nonuniform oscillator $\dot\theta=\omega-a\sin\theta$. The nonuniform oscillator has period $2\pi/\sqrt{\omega^2-a^2}$ and stops oscillating in a saddle-node bifurcation at $a=\omega$, with a slow "bottleneck" just before. The same equation describes an overdamped pendulum, entrainment of fireflies, and an overdamped Josephson junction. Adding inertia to the junction gives hysteresis, which the line and the circle cannot show.

**Prerequisites:** 1D flows $\dot x=f(x)$, fixed points and linear stability, saddle-node bifurcation, basic integration, nondimensionalization (Ch. 2–3).

## L2 — Key ideas
- A vector field on the circle needs a unique velocity at each point, so $f(\theta)$ must be $2\pi$-periodic. This is why $\dot\theta=\theta$ fails (p. 96–97).
- Uniform oscillator: $\theta=\omega t+\theta_0$, period $2\pi/\omega$. There is no amplitude variable. Two uncoupled oscillators show beats, with phase difference growing at rate $\omega_1-\omega_2$ (p. 97–98).
- Nonuniform oscillator $\dot\theta=\omega-a\sin\theta$: for $a<\omega$ it oscillates with $T=2\pi/\sqrt{\omega^2-a^2}$. At $a=\omega$ a half-stable fixed point is born in a saddle-node bifurcation, and for $a>\omega$ there is a stable and an unstable fixed point (p. 98–100).
- Near a saddle-node bifurcation, a ghost (a remnant of the vanished fixed points) causes a bottleneck (a very slow passage), and passage time scales like $r^{-1/2}$ ($T\approx\pi/\sqrt r$). The text presents this as very general, for a generic parabolic minimum, and not special to the sine (p. 101–103).
- The overdamped pendulum with constant torque reduces to $\theta'=\gamma-\sin\theta$. It overturns for $\gamma>1$ and has equilibria for $\gamma<1$ (p. 103–105).
- Firefly entrainment model: the phase difference obeys $\phi'=\mu-\sin\phi$. Locking (constant phase difference) occurs for $|\Omega-\omega|\le A$, and drift occurs outside that range (p. 106–108).
- The overdamped Josephson junction is the same equation, with $\langle V\rangle=I_cR\sqrt{(I/I_c)^2-1}$ for $I>I_c$. With non-negligible capacitance the I–V curve is hysteretic (the voltage follows different paths when the current is raised and lowered) (p. 112–115).
- On the line only fixed points exist; on the circle fixed points and periodic solutions exist, but not simultaneously. The text says hysteresis occurs because a stable fixed point coexists with a stable periodic solution, and calls it one example of the new phenomena of two-dimensional systems (p. 115).

## L3 — Walkthrough

### 4.0 Introduction
The equation $\dot\theta=f(\theta)$ defines a *vector field on the circle*: $\theta$ is a point on the circle and $\dot\theta$ the velocity there. The circle is one-dimensional like the line, but a particle flowing one way can eventually return to its start. So periodic solutions are possible, and the circle is the most basic model of a system that can oscillate (p. 95). In other respects flows on the circle resemble flows on the line (p. 95). Fireflies and Josephson junctions are modeled by the same equation, though their frequencies differ by about ten orders of magnitude (p. 95).

### 4.1 Examples and definitions
- **Example 4.1.1** ($\dot\theta=\sin\theta$). Put $\theta=0$ at "east", with $\theta$ increasing counterclockwise. Fixed points are $\theta^*=0$ and $\theta^*=\pi$. On the upper semicircle $\sin\theta>0$, so the flow is counterclockwise. On the lower semicircle it is clockwise. Hence $\theta^*=\pi$ is stable and $\theta^*=0$ is unstable. This is the same system as $\dot x=\sin x$ in Section 2.1, but it is clearer on the circle (p. 96).
- **Example 4.1.2** ($\dot\theta=\theta$, $-\infty<\theta<\infty$). This is not a vector field on the circle. $\theta=0$ and $\theta=2\pi$ label the same point but imply velocities $0$ and $2\pi$ (p. 96). Restricting to $-\pi<\theta\le\pi$ makes the velocity jump at $\theta=\pi$ (p. 96). On the line there is no problem, since $0$ and $2\pi$ are different points (p. 96).
- **Definition.** A vector field on the circle is a rule that assigns a unique velocity vector to each point (p. 96). Such vector fields arise in practice when we have $\dot\theta=f(\theta)$ with $f$ real-valued, smooth enough for existence and uniqueness, and $2\pi$-periodic: $f(\theta+2\pi)=f(\theta)$ for all $\theta$ (p. 96). Periodicity makes $\dot\theta$ the same whether the point is called $\theta$, $\theta+2\pi$, or $\theta+2\pi k$ (p. 97).

*Intuition note.* A point on a circle has many names ($\theta$, $\theta+2\pi$, …). A rule for motion must give the same answer under every name. Periodicity of $f$ guarantees this.

### 4.2 Uniform oscillator
A point on a circle is often called an angle or *phase*. The simplest oscillator is $\dot\theta=\omega$ with constant $\omega$, solved by $\theta(t)=\omega t+\theta_0$. This is uniform motion at angular frequency $\omega$, returning to the same point after the *period* $T=2\pi/\omega$ (p. 97). There is no amplitude variable. An amplitude as well as a phase would make the phase space two-dimensional, which comes later in the book (p. 97).

**Example 4.2.1 (joggers).** Speedy needs $T_1$ seconds per lap and Pokey needs $T_2>T_1$. Then $\dot\theta_1=\omega_1=2\pi/T_1$ and $\dot\theta_2=\omega_2=2\pi/T_2$. Speedy laps Pokey when the phase difference $\phi=\theta_1-\theta_2$ has grown by $2\pi$. By subtraction $\dot\phi=\omega_1-\omega_2$, so (p. 97–98)
$$T_{\text{lap}}=\frac{2\pi}{\omega_1-\omega_2}=\left(\frac1{T_1}-\frac1{T_2}\right)^{-1}.$$
This is the *beat phenomenon*: noninteracting oscillators with different frequencies go in and out of phase periodically, like two churches' bells. If the oscillators interact, we can get more interesting effects (p. 98).

*Intuition note.* Only the phase difference matters for lapping, and it grows at the constant rate $\omega_1-\omega_2$. A lap happens each time it gains $2\pi$.

### 4.3 Nonuniform oscillator
$$\dot\theta=\omega-a\sin\theta \tag{1}$$
It arises in phase-locked loops, neurons, firefly rhythms, sleep–wake cycles, Josephson junctions, charge-density waves, and the overdamped pendulum with constant torque (p. 98). Assume $\omega>0$, $a\ge0$; the other signs are similar. $\omega$ is the mean and $a$ the amplitude of $f(\theta)$ (p. 98).

**Vector fields.** For $a=0$ we get the uniform oscillator. For $a>0$ the flow is fastest at $\theta=-\pi/2$ and slowest at $\theta=\pi/2$, more strongly as $a$ grows (p. 98). The three regimes are (p. 98–99):
- $a<\omega$: for $a$ slightly below $\omega$ the oscillation is jerky. $\theta(t)$ spends a long time in a *bottleneck* near $\pi/2$ and then moves quickly around the rest of the circle.
- $a=\omega$: oscillation stops. A half-stable fixed point is born in a saddle-node bifurcation at $\theta=\pi/2$.
- $a>\omega$: the half-stable point splits into a stable and an unstable fixed point. All trajectories approach the stable one as $t\to\infty$.

**Example 4.3.1 (linear stability, $a>\omega$).** The fixed points satisfy $\sin\theta^*=\omega/a$, $\cos\theta^*=\pm\sqrt{1-(\omega/a)^2}$. Then $f'(\theta^*)=-a\cos\theta^*=\mp a\sqrt{1-(\omega/a)^2}$. The point with $\cos\theta^*>0$ has $f'<0$ and is stable (p. 99–100).

**Oscillation period ($a<\omega$).**
$$T=\int dt=\int_0^{2\pi}\frac{dt}{d\theta}\,d\theta=\int_0^{2\pi}\frac{d\theta}{\omega-a\sin\theta}=\frac{2\pi}{\sqrt{\omega^2-a^2}}\tag{2}$$
using (1) for $dt/d\theta$. The integral can be evaluated by complex variable methods or by the substitution $u=\tan\frac\theta2$ (Exercise 4.3.2) (p. 100). For $a=0$, $T=2\pi/\omega$. $T$ increases with $a$ and diverges as $a\to\omega^-$ (Figure 4.3.4, p. 100). Using $\sqrt{\omega^2-a^2}=\sqrt{\omega+a}\sqrt{\omega-a}\approx\sqrt{2\omega}\sqrt{\omega-a}$ as $a\to\omega^-$,
$$T\approx\left(\frac{\pi\sqrt2}{\sqrt\omega}\right)\frac1{\sqrt{\omega-a}},\tag{3}$$
so $T$ blows up like $(a_c-a)^{-1/2}$ with $a_c=\omega$ (p. 100–101).

**Ghosts and bottlenecks.** The square-root law is a very general feature of systems near a saddle-node bifurcation (p. 101). Decrease $a$ from $a>\omega$: the two fixed points approach, collide and vanish. For $a$ slightly below $\omega$ they no longer exist but leave a *saddle-node remnant or ghost* that causes slow passage through a bottleneck. In $\theta(t)$ the trajectory spends practically all its time getting through the bottleneck (p. 101).

*General scaling law.* Only the behavior of $\dot\theta$ near its minimum matters, since the time spent there dominates. Generically $\dot\theta$ is parabolic there, so after a local rescaling of space the dynamics reduce to the saddle-node normal form $\dot x=r+x^2$, with $r$ proportional to the distance from the bifurcation and $0<r\ll1$ (p. 101–102). Taking $x$ from $-\infty$ to $+\infty$ (p. 102):
$$T_{\text{bottleneck}}\approx\int_{-\infty}^{\infty}\frac{dx}{r+x^2}=\frac{\pi}{\sqrt r}.\tag{4}$$
Exercise 4.3.1 reminds how to evaluate the integral (p. 102).

**Example 4.3.2 (period via normal form).** Let $\phi=\theta-\pi/2$, small. Then (p. 102)
$$\dot\phi=\omega-a\sin(\phi+\tfrac\pi2)=\omega-a\cos\phi=\omega-a+\tfrac12a\phi^2+\cdots$$
Let $x=(a/2)^{1/2}\phi$ and $r=\omega-a$. Then $(2/a)^{1/2}\dot x\approx r+x^2$ to leading order in $x$. Separating variables gives $T\approx(2/a)^{1/2}\int_{-\infty}^\infty\frac{dx}{r+x^2}=(2/a)^{1/2}\frac{\pi}{\sqrt r}$. With $r=\omega-a$ and $2/a\to2/\omega$ as $a\to\omega^-$, this is $T\approx\frac{\pi\sqrt2}{\sqrt\omega}\frac1{\sqrt{\omega-a}}$, which agrees with (3) (p. 102–103).

*Intuition note.* Just after a pair of fixed points disappears, the flow is almost, but not quite, stopped at that spot. A trajectory crawls through it. The crawl time is $\pi/\sqrt r$, whatever the rest of the model looks like, as long as the minimum is parabolic.

### 4.4 Overdamped pendulum
$\theta$ is the angle from the downward vertical, increasing counterclockwise. With mass $m$, length $L$, damping $b$, gravity $g$ and constant torque $\Gamma$, all positive (p. 103):
$$mL^2\ddot\theta+b\dot\theta+mgL\sin\theta=\Gamma.\tag{1}$$
In the overdamped limit of extremely large $b$ the inertia term is negligible (Section 3.5, Exercise 4.4.1):
$$b\dot\theta+mgL\sin\theta=\Gamma.\tag{2}$$
To think about this physically, the text asks us to imagine the pendulum immersed in molasses. This is the opposite limit from the frictionless, energy-conserving pendulum. Energy is lost to damping and pumped in by the torque (p. 104). Dividing by $mgL$ and setting
$$\tau=\frac{mgL}{b}t,\qquad\gamma=\frac{\Gamma}{mgL}\tag{3}$$
gives
$$\theta'=\gamma-\sin\theta,\qquad\theta'=d\theta/d\tau.\tag{4}$$
$\gamma$ is the ratio of applied torque to maximum gravitational torque. If $\gamma>1$ gravity can never balance the torque and the pendulum overturns continually, nonuniformly (gravity helps on one side, opposes on the other) (p. 104). As $\gamma\to1^+$ the climb past $\theta=\pi/2$ on the slow side takes longer and longer. At $\gamma=1$ a fixed point appears at $\theta^*=\pi/2$ and splits in two for $\gamma<1$. On physical grounds the lower equilibrium is the stable one (p. 104). As $\gamma$ decreases the fixed points move apart. At $\gamma=0$ there is an unstable equilibrium at the top and a stable one at the bottom (p. 105).

### 4.5 Fireflies
In parts of southeast Asia, thousands of male fireflies flash in unison. They start unsynchronized at dusk and the synchrony builds up gradually. The text says the key is that the fireflies influence each other: on seeing another's flash, a firefly speeds up or slows down to flash more nearly in phase next cycle (p. 105).

Hanson (1978) flashed a light periodically at a firefly (natural period about 0.9 s). For stimulus periods close to its natural one, the firefly matched the stimulus frequency: it was *entrained*. If the stimulus was too fast or too slow, entrainment was lost and a beat-like effect occurred. But the phase difference did not grow uniformly. It grew slowly during part of the cycle, then rapidly through $2\pi$. This is *phase walkthrough* or *phase drift* (p. 105).

**Model** (Ermentrout and Rinzel 1984). $\theta$ is the firefly's phase ($\theta=0$ at a flash). Without stimulus $\dot\theta=\omega$. The stimulus phase $\Theta$ obeys
$$\dot\Theta=\Omega,\tag{1}$$
with $\Theta=0$ at the stimulus flash. If the stimulus is ahead the firefly speeds up, and if it flashes too early it slows down:
$$\dot\theta=\omega+A\sin(\Theta-\theta),\quad A>0.\tag{2}$$
If $0<\Theta-\theta<\pi$ then $\dot\theta>\omega$. $A$ is the *resetting strength*, the firefly's ability to change its instantaneous frequency (p. 106).

**Analysis.** For the phase difference $\phi=\Theta-\theta$, subtracting (2) from (1) gives a nonuniform oscillator:
$$\dot\phi=\dot\Theta-\dot\theta=\Omega-\omega-A\sin\phi.\tag{3}$$
With
$$\tau=At,\qquad\mu=\frac{\Omega-\omega}{A}\tag{4}$$
we get
$$\phi'=\mu-\sin\phi.\tag{5}$$
$\mu$ measures the frequency difference relative to the resetting strength. Cases for $\mu\ge0$ (the case $\mu<0$ is similar) (p. 106–107):
- $\mu=0$: all trajectories flow to a stable fixed point $\phi^*=0$. The firefly entrains with zero phase difference.
- $0<\mu<1$: the curve lifts and the stable and unstable points approach. All trajectories go to a stable fixed point with $\phi^*>0$. The phase difference is constant, so the firefly is *phase-locked*: same instantaneous frequency, no longer in unison. Since $\mu>0$ means $\Omega>\omega$, the stimulus flashes ahead and the firefly lags by constant $\phi^*$ without being lapped.
- $\mu=1$: the fixed points coalesce in a saddle-node bifurcation.
- $\mu>1$: no fixed points, so locking is lost and $\phi$ increases indefinitely (phase drift). The rate is not uniform, in qualitative agreement with Hanson. From $\phi'=\mu-\sin\phi$ (added step), $\phi$ moves slowest where $\sin\phi=1$, at $\phi=\pi/2$, and fastest at $\phi=-\pi/2$.

**Predictions.** Entrainment is predicted only for $\omega-A\le\Omega\le\omega+A$, the *range of entrainment* (Figure 4.5.2, p. 107–108). Measuring this range fixes $A$. Then the phase difference during entrainment is predicted (p. 108) as
$$\sin\phi^*=\frac{\Omega-\omega}{A},\quad-\pi/2\le\phi^*\le\pi/2\ \text{(stable fixed point of (3))}\tag{6}$$
and, for $\mu>1$, the drift period (using (2) of Section 4.3) is
$$T_{\text{drift}}=\int_0^{2\pi}\frac{d\phi}{\Omega-\omega-A\sin\phi}=\frac{2\pi}{\sqrt{(\Omega-\omega)^2-A^2}}.\tag{7}$$
Since $A$ and $\omega$ are presumably fixed properties of the firefly, (6) and (7) could be tested by varying $\Omega$. The text says such experiments have yet to be done (p. 108).

**Biological caveat.** The model is reasonable for species such as *Pteroptyx cribellata*, which behave as if $A$ and $\omega$ are fixed. *Pteroptyx malaccae*, the best synchronizer, shifts its own $\omega$ toward $\Omega$ and achieves nearly zero phase difference even at periods differing by ±15% (Hanson 1978). Ermentrout (1991) models this (p. 108).

*Intuition note.* A firefly that adjusts to a periodic stimulus obeys a nonuniform-oscillator equation in its phase difference from the stimulus. When the frequency mismatch is small, the phase difference settles to a constant (locking). When the mismatch is large, the phase difference keeps growing, slowly where the sine curve is lowest and quickly elsewhere.

### 4.6 Superconducting Josephson junctions
Josephson junctions generate voltage oscillations of typically $10^{10}$–$10^{11}$ cycles per second and can detect extremely small potentials (p. 109). Quantum mechanics is required to explain the *origin* of the effect, but the *dynamics* can be described classically. The equation for one junction is the same as for a pendulum (p. 109).

**Physical background.** A junction is two superconductors with a weak connection (insulator, normal metal, semiconductor, etc.). The two regions may be characterized by wave functions $\psi_je^{i\phi_j}$. In the superconducting ground state the electrons form Cooper pairs described by a single macroscopic wave function, and the pairs all adopt the same phase because this minimizes the energy (p. 109). The text compares the pairs to "a miniature version of synchronous fireflies" (p. 109). Josephson (1962) suggested that a current could pass with no voltage difference, by quantum tunneling of Cooper pairs. Anderson and Rowell observed it in 1963 (p. 109).

**Josephson relations.** A dc current $I>0$ is driven through the junction. Using quantum mechanics, if $I<I_c$ (the critical current) no voltage develops. The phases differ by a constant $\phi=\phi_2-\phi_1$ satisfying (p. 110)
$$I=I_c\sin\phi.\tag{1}$$
When $I>I_c$ the phases slip and a voltage appears, with $\hbar$ = Planck's constant over $2\pi$ and $e$ the electron charge:
$$V=\frac{\hbar}{2e}\dot\phi.\tag{2}$$

**Equivalent circuit and pendulum analog.** The supercurrent $I_c\sin\phi$ flows in parallel with a capacitor (displacement current) and a resistor (ordinary current), a circuit first analyzed by Stewart (1968) and McCumber (1968). By Kirchhoff's laws all branches share the voltage $V$, so (p. 111)
$$C\dot V+\frac VR+I_c\sin\phi=I,\tag{3}$$
and with (2)
$$\frac{\hbar C}{2e}\ddot\phi+\frac{\hbar}{2eR}\dot\phi+I_c\sin\phi=I.\tag{4}$$
This is precisely analogous to the pendulum (1) of Section 4.4. The text's dictionary (p. 111):

| Pendulum | Josephson junction |
|---|---|
| angle $\theta$ | phase difference $\phi$ |
| angular velocity $\dot\theta$ | voltage $\frac{\hbar}{2e}\dot\phi$ |
| mass $m$ | capacitance $C$ |
| applied torque $\Gamma$ | bias current $I$ |
| damping constant $b$ | conductance $1/R$ |
| max. gravitational torque $mgL$ | critical current $I_c$ |

Sullivan and Zimmerman (1971) built a mechanical analog. Pendulum rotation rate versus torque corresponds to the junction's I–V curve (p. 111–112).

**Typical values.** $I_c\approx1\,\mu$A–1 mA, $I_cR\approx1$ mV, $2e/h\approx4.83\times10^{14}$ Hz/V (so frequencies on the order of $10^{11}$ Hz), length scale about 1 μm (p. 112).

**Dimensionless form.** Divide (4) by $I_c$ and let
$$\tau=\frac{2eI_cR}{\hbar}t.\tag{5}$$
Then
$$\beta\phi''+\phi'+\sin\phi=\frac I{I_c},\qquad\beta=\frac{2eI_cR^2C}{\hbar}\tag{6}$$
(added step: $\dot\phi=\frac{2eI_cR}{\hbar}\phi'$, so the $\phi'$ coefficient becomes $1$ and the $\phi''$ coefficient becomes $\beta$.) $\beta$ is the *McCumber parameter*, a dimensionless capacitance, ranging from about $10^{-6}$ to much larger values (about $10^{6}$) (p. 112). In the overdamped limit $\beta\ll1$, $\beta\phi''$ is dropped after a rapid transient (Section 3.5):
$$\phi'=\frac I{I_c}-\sin\phi.\tag{7}$$
By Section 4.3, solutions tend to a stable fixed point for $I<I_c$ and are periodic for $I>I_c$ (p. 112).

**Example 4.6.1 (I–V curve, overdamped).** Find the average voltage $\langle V\rangle$ in steady state (p. 113). It suffices to find $\langle\phi'\rangle$, since $\langle V\rangle=\frac\hbar{2e}\langle\dot\phi\rangle$ and $\langle\dot\phi\rangle=\frac{2eI_cR}\hbar\langle\phi'\rangle$ by (5). Thus
$$\langle V\rangle=I_cR\langle\phi'\rangle.\tag{8}$$
- If $I\le I_c$, solutions approach $\phi^*=\sin^{-1}(I/I_c)$, with $-\pi/2\le\phi^*\le\pi/2$. So $\phi'=0$ and $\langle V\rangle=0$.
- If $I>I_c$, solutions are periodic with (time in units of $\tau$)
$$T=\frac{2\pi}{\sqrt{(I/I_c)^2-1}}.\tag{9}$$
The cycle average is
$$\langle\phi'\rangle=\frac1T\int_0^T\frac{d\phi}{d\tau}d\tau=\frac1T\int_0^{2\pi}d\phi=\frac{2\pi}T.\tag{10}$$
Combining (8)–(10):
$$\langle V\rangle=\begin{cases}0,&I\le I_c\\ I_cR\sqrt{(I/I_c)^2-1},&I>I_c\end{cases}\tag{11}$$
Voltage stays zero until $I>I_c$, then rises sharply and tends to Ohmic $\langle V\rangle\approx IR$ for $I\gg I_c$ (Figure 4.6.4, p. 113–114).

**Hysteresis for $\beta\ne0$.** This analysis applies only to $\beta\ll1$. If $\beta$ is not negligible the I–V curve can be hysteretic (Figure 4.6.5): raising $I$ slowly, $V=0$ until $I>I_c$, then $V$ jumps to a nonzero value. Lowering $I$, $V$ does not return to zero at $I_c$; $I$ must go below $I_c$ first (p. 114). By the pendulum analogy, inertia keeps a whirling pendulum going when the torque drops below the critical torque $\Gamma_c$ (p. 114–115). The text says it will show in Section 8.5 that hysteresis occurs because a stable fixed point coexists with a stable periodic solution. On the line only fixed points exist; on the circle both can exist, but not simultaneously. The text calls this one example of the new kinds of phenomena that can occur in two-dimensional systems (p. 115).

*Intuition note.* Without inertia the junction either sits still (below $I_c$) or oscillates (above), so the path up equals the path down. With inertia, both behaviors can be possible at the same current (for some currents), so history decides.

### Exercises (p. 115–121)
Exercises cover well-defined fields on the circle, potentials, beats and the clock problem, bifurcations of various $\dot\theta=f(\theta;\mu)$, general scaling laws near bottlenecks, the validity of the overdamped limit, a torsional spring, firefly variants with a triangle-wave response, excitable systems, Josephson junction waveforms and washboard potential, and arrays of junctions (p. 115–121).

## Toy example (ours, not from the text)
Take $\omega=5$, $a=4.9$ in $\dot\theta=\omega-a\sin\theta$.
- Fixed points: $\sin\theta^*=5/4.9>1$, so none exist. Since $a<\omega$ the flow always has $\dot\theta\ge0.1>0$, so it circulates.
- Exact period (2): $T=2\pi/\sqrt{25-24.01}=2\pi/\sqrt{0.99}=6.2832/0.99499\approx6.315$.
- Bottleneck estimate (3): $\frac{\pi\sqrt2}{\sqrt5}\cdot\frac1{\sqrt{0.1}}=\frac{\pi\sqrt2}{\sqrt{0.5}}=2\pi\approx6.283$. This is within about 0.5% of the exact value.
- Slowest speed is $\omega-a=0.1$ at $\theta=\pi/2$. Fastest is $\omega+a=9.9$ at $\theta=-\pi/2$. For uniform rotation ($a=0$) the period would be $2\pi/5\approx1.26$, about 5 times shorter.

Firefly check ($\omega=1$, $A=0.2$): entrainment range is $0.8\le\Omega\le1.2$. For $\Omega=1.1$, $\sin\phi^*=0.1/0.2=0.5$, so $\phi^*=\pi/6$. For $\Omega=1.3$, $\mu=1.5>1$ and $T_{\text{drift}}=2\pi/\sqrt{0.09-0.04}=6.2832/0.2236\approx28.1$.

## Concepts
- [[vector-field-on-circle]] (new) — rule giving a unique velocity at each point of a circle; needs $2\pi$-periodic $f$ (p. 96).
- [[phase-oscillator]] (new) — oscillator described by phase $\theta$ alone, no amplitude variable (p. 97).
- [[beat-phenomenon]] (new) — noninteracting oscillators with different frequencies drift in and out of phase (p. 98).
- [[fixed point and stability]] — here $\theta^*$ with $f(\theta^*)=0$, classified by sign of $f'$ (p. 99).
- [[saddle-node (fold) bifurcation]] — two fixed points collide at $a=\omega$ (or $\gamma=1$, $\mu=1$, $I=I_c$) and vanish (p. 99).
- [[bottleneck-ghost]] (new) — after the collision, a remnant of the fixed points makes passage slow (p. 101).
- [[square-root-scaling-law]] (new) — time through a bottleneck scales as $r^{-1/2}$ ($\pi/\sqrt r$ for $\dot x=r+x^2$) (p. 100–102).
- [[synchronization]] — firefly entrainment and phase-locking to a periodic stimulus (p. 105–107).
- [[entrainment-phase-locking]] (new) — constant phase difference, same instantaneous frequency; range $\omega-A\le\Omega\le\omega+A$ (p. 107–108).
- [[hysteresis]] — Josephson I–V curve when $\beta$ is not negligible: different paths up and down (p. 114).
- [[overdamped-limit]] (new) — inertia term dropped, reducing a second-order system to first order (p. 103).

## Canonical instances
- [[overdamped-pendulum]] — $\theta'=\gamma-\sin\theta$; overturning for $\gamma>1$ (p. 103–105).
- [[firefly-synchrony]] — phase-difference model $\phi'=\mu-\sin\phi$ (p. 105–108).
- [[josephson-junction]] — overdamped I–V curve and hysteresis with inertia (p. 109–115).
- [[pendulum-josephson-analogy]] — same equation, dictionary of variables (p. 111).
- [[joggers-and-church-bells]] — beats from different constant frequencies (p. 97–98).

## Bridges (candidates)
- [same-math] Firefly phase difference $\phi'=\mu-\sin\phi$ ↔ Josephson junction (overdamped) $\phi'=I/I_c-\sin\phi$ — identical equation with $\mu\leftrightarrow I/I_c$.
- [same-math] Nonuniform oscillator ↔ overdamped pendulum with constant torque — the same equation after nondimensionalizing.
- [structural-analogy] Ghost/bottleneck and the $r^{-1/2}$ law ↔ tipping points and critical slowing down: slow motion near a vanished fixed point (canon link; not stated in this unit).
- [structural-analogy] Entrainment and drift ↔ Kuramoto-type synchronization of coupled oscillators (canon link; not stated in this unit).
- [metaphor] Cooper pairs sharing one phase ↔ synchronous fireflies (the text's own comparison, p. 109).

## Questions this raises
- How does the hysteresis of the Josephson junction arise from a stable fixed point coexisting with a stable periodic orbit (promised for Section 8.5)?
- What happens to entrainment when many oscillators interact, as in arrays of junctions?
- If a firefly shifts its own frequency $\omega$ toward the drive (as *P. malaccae* does), how does the phase-difference equation change?
- How does the bottleneck exponent change if the minimum of $\dot x$ is higher order than quadratic (Exercise 4.3.10)?

## Exercises worth doing
- Ex. 4.1.8 (p. 115) — single-valued potentials on the circle; why $\dot\theta=1$ has none — difficulty: medium
- Ex. 4.1.9 (p. 115) — why the line's no-periodic-orbit proofs fail on the circle — difficulty: medium
- Ex. 4.3.2 (p. 116) — derive the period formula (2) by $u=\tan\frac\theta2$ — difficulty: medium
- Ex. 4.3.9 (p. 117) — rederive the $r^{-1/2}$ law by scaling arguments — difficulty: medium
- Ex. 4.3.10 (p. 117) — bottleneck scaling for $\dot x=r+x^{2n}$ — difficulty: hard
- Ex. 4.5.1 (p. 118) — firefly model with a triangle-wave response — difficulty: medium
- Ex. 4.6.3 (p. 119) — washboard potential for the overdamped junction — difficulty: medium

## Reading notes
- Printed page = pdf page − 15 (pdf 110 = printed 95). The final pdf page (137, printed 122) is blank.
- The text layer is garbled: Greek letters appear as other letters (θ as "R", ω as "X", φ as "G", γ and μ as "H" and "N"), and minus signs are sometimes lost. Equations were checked against the page images.
- p. 112 prints "$2e/h\approx4.83\times10^{14}$ Hz/V" with $h$, while the nearby formulas use $\hbar$. I kept the printed form.
- p. 107: the sentence on where $\phi$ moves slowest and fastest reads "$\phi=\pi/2$" at both places in the image. From $\phi'=\mu-\sin\phi$ the fastest point is $\phi=-\pi/2$; I used that and marked it as an added step.
- I did not solve any exercise.
