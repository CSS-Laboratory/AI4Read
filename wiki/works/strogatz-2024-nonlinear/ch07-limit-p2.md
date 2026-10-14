---
id: strogatz-2024-nonlinear/ch07-limit-p2
work: strogatz-2024-nonlinear
unit: "7 Limit Cycles (part 2/2): end of 7.5, Section 7.6 Weakly Nonlinear Oscillators, and Exercises for Chapter 7"
pages: 217–243
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
# Weakly Nonlinear Oscillators: Two-Timing and Averaged Equations

## L0 — One line
For oscillators that are small perturbations of $\ddot x+x=0$, a plain power series in $\varepsilon$ breaks down, but two-timing (a fast time plus a slow time) gives averaged equations for a slowly varying amplitude and phase.

## L1 — The gist (≤ 120 words)
This unit asks how to predict the amplitude, frequency and shape of oscillations in equations that are small perturbations of $\ddot x+x=0$. A plain power series in $\varepsilon$ fails at long times: it produces terms that grow without bound (secular terms) and misrepresents slow amplitude change. Two-timing treats a fast time and a slow time $\varepsilon t$ as separate variables and removes the secular terms. This yields averaged equations for a slowly varying amplitude and phase. They show that the van der Pol equation has a stable limit cycle of radius $2+O(\varepsilon)$. For the Duffing equation, $\omega=1+\tfrac38\varepsilon a^2+O(\varepsilon^2)$, so for $\varepsilon>0$ (hardening spring) the frequency rises with amplitude.

**Prerequisites:** harmonic oscillator $\ddot x+x=0$; chain rule and partial derivatives; trig identities; power series; averages of periodic functions; polar coordinates in the phase plane; fixed points of a 1-D flow $\dot r=f(r)$.

## L2 — Key ideas
- **Weakly nonlinear oscillators** $\ddot x+x+\varepsilon h(x,\dot x)=0$ are small perturbations of the harmonic oscillator. For van der Pol with $\varepsilon=0.1$, trajectories spiral slowly out to an almost circular cycle of radius near 2 (pp. 217–218).
- **Regular perturbation theory fails over long times.** On a damped test oscillator it gives $\sin t-\varepsilon t\sin t$, with a secular term $t\sin t$. The approximation is expected to work only for $t\lesssim O(1/\varepsilon)$. It misses the slow decay and the frequency shift (pp. 219–220).
- **Two-timing** uses a fast time $\tau=t$ and a slow time $T=\varepsilon t$, regarded as independent. Functions of $T$ are regarded as constants on the fast scale; the author says this is hard to justify rigorously but works (p. 221).
- **Rule of the method:** choose the slow dependence of the amplitude and phase so that no resonant terms (forcing at the oscillator's own frequency, which would produce secular terms) appear at order $\varepsilon$ (p. 222). On the test problem this gives $e^{-\varepsilon t}\sin t$, nearly identical to the exact solution at $\varepsilon=0.1$ (p. 223).
- **van der Pol:** $r'=\tfrac18 r(4-r^2)$ and $\phi'=0$. So there is a stable, nearly circular limit cycle of radius $2+O(\varepsilon)$, with $\omega=1+O(\varepsilon^2)$ (pp. 224–225).
- **Averaged equations:** $r'=\langle h\sin\theta\rangle$ and $r\phi'=\langle h\cos\theta\rangle$, with averages over one cycle of $\theta$ (p. 226). They also give the whole van der Pol transient (p. 228).
- **Duffing oscillator:** the amplitude stays constant and $\omega=1+\tfrac38\varepsilon a^2+O(\varepsilon^2)$. Amplitude-dependent frequency is intrinsically nonlinear (pp. 228–229).
- **Rule of thumb for validity:** if $x$ and $x_0$ start from the same initial condition, $x_0$ stays within $O(\varepsilon)$ of $x$ for $t$ up to order $1/\varepsilon$. If $x$ is periodic, $x_0$ stays within $O(\varepsilon)$ of $x$ for all $t$ (p. 229).

## L3 — Walkthrough

### End of 7.5 (p. 217)
The unit opens in the middle of the last remarks of Section 7.5 (relaxation oscillations). The text points to a derivation of a formula credited to Mary Cartwright (1952) and to Stoker (1950). Its last remark: a relaxation oscillation has two time scales that operate *sequentially* (slow buildup, then fast discharge). In the next section the two time scales operate *concurrently*, which makes the problems "a bit more subtle" (p. 217).

### 7.6 Weakly Nonlinear Oscillators (pp. 217–229)

**Setting.** The equation is

$$\ddot x+x+\varepsilon h(x,\dot x)=0,\qquad 0\le\varepsilon\ll1,\tag{1}$$

with $h$ an arbitrary smooth function. This is a small perturbation of $\ddot x+x=0$, so it is called a *weakly nonlinear oscillator*. Two basic examples (p. 217):

$$\ddot x+x+\varepsilon(x^2-1)\dot x=0\quad\text{(van der Pol)}\tag{2}$$

$$\ddot x+x+\varepsilon x^3=0\quad\text{(Duffing)}\tag{3}$$

For van der Pol with $\varepsilon=0.1$ and an initial condition near the origin, the trajectory is a slowly winding spiral. It takes many cycles for the amplitude to grow, and it ends on an approximately circular limit cycle of radius close to 2 (Fig. 7.6.1, p. 217). The goal is to predict the shape, period and radius, using the closeness to the harmonic oscillator (p. 218).

**Regular perturbation theory and its failure (pp. 218–220).** Expand the solution as a power series in $\varepsilon$ (p. 218):

$$x(t,\varepsilon)=x_0(t)+\varepsilon x_1(t)+\varepsilon^2x_2(t)+\dots\tag{4}$$

The hope is that the first two terms carry the important information. The test problem is a weakly damped linear oscillator, solvable exactly (p. 218):

$$\ddot x+2\varepsilon\dot x+x=0\tag{5}$$

$$x(0)=0,\quad \dot x(0)=1\tag{6}$$

$$x(t,\varepsilon)=(1-\varepsilon^2)^{-1/2}e^{-\varepsilon t}\sin\!\big[(1-\varepsilon^2)^{1/2}t\big]\tag{7}$$

Substituting (4) into (5) and grouping powers of $\varepsilon$ gives

$$[\ddot x_0+x_0]+\varepsilon[\ddot x_1+2\dot x_0+x_1]+O(\varepsilon^2)=0.\tag{9}$$

Since (9) must hold for all small $\varepsilon$, each power's coefficient vanishes (p. 218):

$$O(1):\ \ddot x_0+x_0=0\tag{10}$$

$$O(\varepsilon):\ \ddot x_1+2\dot x_0+x_1=0\tag{11}$$

The initial conditions (6) give, for all $\varepsilon$ (p. 219):

$$x_0(0)=0,\quad x_1(0)=0\tag{12}$$

$$\dot x_0(0)=1,\quad \dot x_1(0)=0\tag{13}$$

Solving in order (p. 219):

$$x_0(t)=\sin t\tag{14}$$

$$\ddot x_1+x_1=-2\cos t\tag{15}$$

$$x_1(t)=-t\sin t\tag{16}$$

The right side of (15) is a *resonant forcing*. Its solution (16) is a *secular term*: it grows without bound as $t\to\infty$ (p. 219). The result is

$$x(t,\varepsilon)=\sin t-\varepsilon t\sin t+O(\varepsilon^2).\tag{17}$$

(17) is the first two terms of the series expansion of the exact solution (7) (Exercise 7.6.1). For fixed $t$ it is good if $\varepsilon t\ll1$, since the correction is really $O(\varepsilon^2t^2)$. For fixed $\varepsilon$, we can only expect it to work for $t\lesssim O(1/\varepsilon)$. With $\varepsilon=0.1$ it works reasonably for $t\ll10$ and breaks down afterwards (Fig. 7.6.2, p. 219).

Two failures (p. 220):
1. The true solution has a fast time $t\sim O(1)$ for the oscillation and a slow time $t\sim1/\varepsilon$ for the amplitude decay. Because of $t\sin t$, (17) falsely suggests growth. This is because $e^{-\varepsilon t}=1-\varepsilon t+O(\varepsilon^2t^2)$. Fixing it by this route would need infinitely many terms.
2. The true frequency is $\omega=(1-\varepsilon^2)^{1/2}\approx1-\tfrac12\varepsilon^2$, not 1. The error matters after $t\sim O(1/\varepsilon^2)$, a third, super-slow time scale.

*Intuition note.* Regular perturbation theory looks at the system on one time scale only. Here the amplitude changes on a second, slower scale, and the series shows that change as a growing term instead. Two-timing, next, builds the second scale in from the start.

**Two-timing (pp. 220–222).** The idea is that weakly nonlinear oscillators have at least two time scales. Let $\tau=t$ (fast) and $T=\varepsilon t$ (slow). Treat them as independent variables; functions of $T$ "will be regarded as constants" on the $\tau$ scale. The author calls this hard to justify rigorously, but it works. His analogy: your height is constant on the time scale of a day (p. 221). Expand

$$x(t,\varepsilon)=x_0(\tau,T)+\varepsilon x_1(\tau,T)+O(\varepsilon^2).\tag{18}$$

The chain rule gives

$$\dot x=\frac{dx}{dt}=\frac{\partial x}{\partial\tau}+\frac{\partial x}{\partial T}\frac{\partial T}{\partial t}=\frac{\partial x}{\partial\tau}+\varepsilon\frac{\partial x}{\partial T}\tag{19}$$

which in subscript notation reads

$$\dot x=\partial_\tau x+\varepsilon\partial_Tx.\tag{20}$$

Substituting (18):

$$\dot x=\partial_\tau x_0+\varepsilon(\partial_Tx_0+\partial_\tau x_1)+O(\varepsilon^2)\tag{21}$$

$$\ddot x=\partial_{\tau\tau}x_0+\varepsilon(\partial_{\tau\tau}x_1+2\partial_{T\tau}x_0)+O(\varepsilon^2)\tag{22}$$

**Example 7.6.1 (test problem again, pp. 221–223).** Substituting (21) and (22) into $\ddot x+2\varepsilon\dot x+x=0$ gives

$$\partial_{\tau\tau}x_0+\varepsilon(\partial_{\tau\tau}x_1+2\partial_{T\tau}x_0)+2\varepsilon\partial_\tau x_0+x_0+\varepsilon x_1+O(\varepsilon^2)=0.\tag{23}$$

Collecting powers (p. 221):

$$O(1):\ \partial_{\tau\tau}x_0+x_0=0\tag{24}$$

$$O(\varepsilon):\ \partial_{\tau\tau}x_1+2\partial_{T\tau}x_0+2\partial_\tau x_0+x_1=0\tag{25}$$

The general solution of (24) is

$$x_0=A\sin\tau+B\cos\tau\tag{26}$$

where now $A$ and $B$ are functions of the slow time $T$ (p. 222). Substituting (26) into (25), with a prime meaning $d/dT$:

$$\partial_{\tau\tau}x_1+x_1=-2(\partial_{T\tau}x_0+\partial_\tau x_0)=-2(A'+A)\cos\tau+2(B'+B)\sin\tau\tag{27}$$

The right side is resonant forcing and would give secular terms $\tau\sin\tau$, $\tau\cos\tau$ in $x_1$. The characteristic manoeuvre of two-timing is to set the coefficients of the resonant terms to zero (p. 222):

$$A'+A=0\tag{28}$$

$$B'+B=0\tag{29}$$

Hence $A(T)=A(0)e^{-T}$ and $B(T)=B(0)e^{-T}$. The initial conditions, required to hold for all small $\varepsilon$, give

$$x_0(0,0)=0\tag{30}$$

$$\partial_\tau x_0(0,0)=1\tag{31}$$

and also $x_1(0,0)=0$ and $\partial_Tx_0(0,0)+\partial_\tau x_1(0,0)=0$ (pp. 222–223). With (26): $B(0)=0$, so $B(T)\equiv0$, and $A(0)=1$. Therefore (p. 223)

$$x_0(\tau,T)=e^{-T}\sin\tau\tag{32}$$

$$x=e^{-T}\sin\tau+O(\varepsilon)=e^{-\varepsilon t}\sin t+O(\varepsilon)\tag{33}$$

For $\varepsilon=0.1$ the two-timing curve and the exact solution (7) are almost indistinguishable (Fig. 7.6.3). The author says the method "often works better than it has any right to" (p. 223). To capture the $O(\varepsilon^2)$ frequency error one could introduce a super-slow time $\mathcal T=\varepsilon^2t$ (p. 223).

*Intuition note.* Here the amplitude $A(T)$ is allowed to change slowly. Demanding no growing terms forces $A'=-A$, which is the decay that regular perturbation theory could not show with a few terms.

**Example 7.6.2 (van der Pol, pp. 223–225).** Claim: stable, nearly circular limit cycle with radius $2+O(\varepsilon)$ and frequency $\omega=1+O(\varepsilon^2)$. Using (21) and (22) on (2) (p. 224):

$$O(1):\ \partial_{\tau\tau}x_0+x_0=0\tag{34}$$

$$O(\varepsilon):\ \partial_{\tau\tau}x_1+x_1=-2\partial_{\tau T}x_0-(x_0^2-1)\partial_\tau x_0\tag{35}$$

Write the general solution of (34) with a slowly varying amplitude $r(T)$ and phase $\phi(T)$:

$$x_0=r(T)\cos(\tau+\phi(T))\tag{36}$$

Inserting (36) into (35) gives (as printed; see Reading notes on the overall sign):

$$\partial_{\tau\tau}x_1+x_1=-2\big(r'\sin(\tau+\phi)+r\phi'\cos(\tau+\phi)\big)-r\sin(\tau+\phi)\big[r^2\cos^2(\tau+\phi)-1\big]\tag{37}$$

Resonant terms are those proportional to $\cos(\tau+\phi)$ or $\sin(\tau+\phi)$. One hides in $\sin\cos^2$:

$$\sin(\tau+\phi)\cos^2(\tau+\phi)=\tfrac14[\sin(\tau+\phi)+\sin3(\tau+\phi)]\tag{38}$$

so that (p. 224)

$$\partial_{\tau\tau}x_1+x_1=\big[-2r'+r-\tfrac14r^3\big]\sin(\tau+\phi)+[-2r\phi']\cos(\tau+\phi)-\tfrac14r^3\sin3(\tau+\phi).\tag{39}$$

Avoiding secular terms requires

$$-2r'+r-\tfrac14r^3=0\tag{40}$$

$$-2r\phi'=0\tag{41}$$

(40) can be written as a vector field on the half-line $r\ge0$:

$$r'=\tfrac18r(4-r^2)\tag{42}$$

Then $r^*=0$ is unstable and $r^*=2$ is stable, so $r(T)\to2$ as $T\to\infty$. By (41), $\phi'=0$, so $\phi=\phi_0$ is constant. Hence (p. 225)

$$x(t)\to2\cos(t+\phi_0)+O(\varepsilon)\tag{43}$$

as $t\to\infty$: $x(t)$ approaches a stable limit cycle of radius $2+O(\varepsilon)$. With $\theta=t+\phi(T)$, the angular frequency is

$$\omega=\frac{d\theta}{dt}=1+\frac{d\phi}{dT}\frac{dT}{dt}=1+\varepsilon\phi'=1\tag{44}$$

through first order in $\varepsilon$. Hence $\omega=1+O(\varepsilon^2)$. An explicit $O(\varepsilon^2)$ term would need the super-slow time $\mathcal T=\varepsilon^2t$ or the Poincaré–Lindstedt method (exercises) (p. 225).

*Intuition note.* The 2-D oscillation is reduced to a 1-D flow for the amplitude $r$. Its stable fixed point at $r=2$ is the limit cycle, which fits the radius close to 2 seen in Fig. 7.6.1. The phase equation is $\phi'=0$, so the phase does not drift on the slow time scale.

**Averaged equations (pp. 225–227).** The same steps recur, so derive general formulas for (p. 225)

$$\ddot x+x+\varepsilon h(x,\dot x)=0.\tag{45}$$

The two-timing orders are

$$O(1):\ \partial_{\tau\tau}x_0+x_0=0\tag{46}$$

$$O(\varepsilon):\ \partial_{\tau\tau}x_1+x_1=-2\partial_{\tau T}x_0-h\tag{47}$$

where $h=h(x_0,\partial_\tau x_0)$. As before

$$x_0=r(T)\cos(\tau+\phi(T)).\tag{48}$$

The right side of (47) is

$$2[r'\sin(\tau+\phi)+r\phi'\cos(t+\phi)]-h\tag{49}$$

with $h=h(r\cos(\tau+\phi),-r\sin(\tau+\phi))$. Let $\theta=\tau+\phi$. Then $h$ is $2\pi$-periodic in $\theta$, so it has a Fourier series (p. 226):

$$h(\theta)=\sum_{k=0}^\infty a_k\cos k\theta+\sum_{k=1}^\infty b_k\sin k\theta\tag{50}$$

$$a_0=\tfrac1{2\pi}\!\int_0^{2\pi}\!h\,d\theta,\quad a_k=\tfrac1\pi\!\int_0^{2\pi}\!h\cos k\theta\,d\theta,\quad b_k=\tfrac1\pi\!\int_0^{2\pi}\!h\sin k\theta\,d\theta\quad(k\ge1)\tag{51}$$

Then (49) becomes

$$2[r'\sin\theta+r\phi'\cos\theta]-\sum_{k=0}^\infty a_k\cos k\theta-\sum_{k=1}^\infty b_k\sin k\theta.\tag{52}$$

The only resonant terms are $[2r'-b_1]\sin\theta$ and $[2r\phi'-a_1]\cos\theta$. So we need $r'=b_1/2$ and $r\phi'=a_1/2$:

$$r'=\tfrac1{2\pi}\int_0^{2\pi}h(\theta)\sin\theta\,d\theta\equiv\langle h\sin\theta\rangle$$

$$r\phi'=\tfrac1{2\pi}\int_0^{2\pi}h(\theta)\cos\theta\,d\theta\equiv\langle h\cos\theta\rangle\tag{53}$$

Here $\langle\cdot\rangle$ is an average over one cycle of $\theta$. (53) are the *averaged* or *slow-time equations*. To use them, write $h(r\cos\theta,-r\sin\theta)$, then average over $\theta$ treating $r$ as constant. Useful averages (p. 226):

$$\langle\cos\rangle=\langle\sin\rangle=0,\ \langle\sin\cos\rangle=0,\ \langle\cos^{2n+1}\rangle=\langle\sin^{2n+1}\rangle=0,$$

$$\langle\cos^2\rangle=\langle\sin^2\rangle=\tfrac12,\ \langle\cos^4\rangle=\langle\sin^4\rangle=\tfrac38,\ \langle\cos^2\sin^2\rangle=\tfrac18,$$

$$\langle\cos^{2n}\rangle=\langle\sin^{2n}\rangle=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)},\quad n\ge1.\tag{54}$$

Others follow from these: $\langle\cos^2\sin^4\rangle=\langle(1-\sin^2)\sin^4\rangle=\langle\sin^4\rangle-\langle\sin^6\rangle=\tfrac38-\tfrac{15}{48}=\tfrac1{16}$, and $\langle\cos^3\sin\rangle=0$ by direct integration (p. 227).

*Intuition note.* The slow equations come only from the resonant part of $h$, the part that oscillates at the oscillator's own frequency (its $\sin\theta$ and $\cos\theta$ components). The $\sin\theta$ component of $h$ changes the amplitude and the $\cos\theta$ component changes the phase. Averaging picks out exactly these two components.

**Example 7.6.3 (van der Pol transient, pp. 227–228).** Take $x(0)=1$, $\dot x(0)=0$. Here $h=(x^2-1)\dot x=(r^2\cos^2\theta-1)(-r\sin\theta)$. Then

$$r'=\langle h\sin\theta\rangle=r\langle\sin^2\theta\rangle-r^3\langle\cos^2\theta\sin^2\theta\rangle=\tfrac12r-\tfrac18r^3,$$

$$r\phi'=\langle h\cos\theta\rangle=r\langle\sin\theta\cos\theta\rangle-r^3\langle\cos^3\theta\sin\theta\rangle=0-0=0.$$

These match Example 7.6.2 (p. 227). The initial conditions give $r(0)\approx\sqrt{x(0)^2+\dot x(0)^2}=1$ and $\phi(0)=0$, so $\phi(T)\equiv0$. Solve $r'=\tfrac12r-\tfrac18r^3$ with $r(0)=1$ by separating variables, $\int\frac{8\,dr}{r(4-r^2)}=\int dT$, then partial fractions:

$$r(T)=2(1+3e^{-T})^{-1/2}\tag{55}$$

$$x(t,\varepsilon)\sim x_0(\tau,T)+O(\varepsilon)=\frac{2}{\sqrt{1+3e^{-\varepsilon t}}}\cos t+O(\varepsilon)\tag{56}$$

(55)–(56) describe the transient as the trajectory spirals out to the limit cycle, with $r\to2$. For $\varepsilon=0.1$, the agreement between the envelope (55) and numerical integration is described as striking (Fig. 7.6.4, p. 228).

**Example 7.6.4 (Duffing, pp. 228–229).** Goal: amplitude–frequency relation for $\ddot x+x+\varepsilon x^3=0$, with $\varepsilon$ of either sign. Here $h=x^3=r^3\cos^3\theta$. Then

$$r'=\langle h\sin\theta\rangle=r^3\langle\cos^3\theta\sin\theta\rangle=0,$$

$$r\phi'=\langle h\cos\theta\rangle=r^3\langle\cos^4\theta\rangle=\tfrac38r^3.$$

So $r(T)\equiv a$ (constant) and $\phi'=\tfrac38a^2$. As in Example 7.6.2,

$$\omega=1+\varepsilon\phi'=1+\tfrac38\varepsilon a^2+O(\varepsilon^2).\tag{57}$$

Frequency depending on amplitude is common and intrinsically nonlinear; it cannot occur for linear oscillators (p. 228). Physical reading (p. 229): the restoring force is $F(x)=-x-\varepsilon x^3=-kx$ with stiffness $k(x)=1+\varepsilon x^2$.
- For $\varepsilon>0$ the spring gets stiffer with displacement (hardening spring). One expects higher frequency, consistent with (57).
- For $\varepsilon<0$ it is a softening spring, exemplified by the pendulum (Exercise 7.6.15).
- $r'=0$ makes sense: Duffing is a conservative system and, for all sufficiently small $\varepsilon$, has a nonlinear center at the origin (Exercise 6.5.13). All orbits near the origin are periodic, so there is no long-term amplitude change.

*Intuition note.* For van der Pol the averaged amplitude equation has a nonzero stable fixed point, which gives a limit cycle. For Duffing the amplitude equation is $r'=0$, so every amplitude persists. The nonlinearity acts only on the phase, which changes the frequency.

**Validity of two-timing (p. 229).** Rule of thumb: the one-term approximation $x_0$ stays within $O(\varepsilon)$ of the true solution $x$ for all times up to and including $t\sim O(1/\varepsilon)$, assuming $x$ and $x_0$ start from the same initial condition. If $x$ is periodic, $x_0$ remains within $O(\varepsilon)$ of $x$ for all $t$. The author refers to Guckenheimer and Holmes (1983) and Grimshaw (1990) for rigorous results. Those authors use the *method of averaging*, which gives the same results as two-timing (Exercise 7.6.25). The relevant notion of approximation is *asymptotic* approximation; see Lin and Segel (1988) and Bender and Orszag (1978) (p. 229).

### Exercises for Chapter 7 (pp. 230–243)
The set covers Sections 7.1–7.6; it is only listed here, not solved. Exercises for 7.1–7.5 (pp. 230–238) include: phase portraits in polar coordinates, a circuit for the van der Pol oscillator and a circular pursuit problem (7.1, pp. 230–231); gradient systems, Liapunov functions and Dulac's criterion (7.2, pp. 231–233); Poincaré–Bendixson problems, cycle graphs and a heteroclinic cycle (7.3, pp. 234–236); Liénard systems (7.4, p. 236); relaxation oscillations and a cell-cycle model (7.5, pp. 237–238). The 7.6 exercises (pp. 238–243) include:
- Calibration of regular perturbation theory (7.6.2–7.6.3).
- Averaged equations for six given $h$ (7.6.4–7.6.9).
- Deriving trig identities and Fourier coefficients (7.6.10, 7.6.12).
- Higher harmonics (7.6.11).
- Exact Duffing period (7.6.13).
- A computer test of two-timing at $\varepsilon=2$ (7.6.14).
- The pendulum (7.6.15).
- Van der Pol amplitude via Green's theorem (7.6.16).
- The swing (7.6.17).
- The Mathieu equation with super-slow time (7.6.18).
- The Poincaré–Lindstedt method, in which the frequency is treated as unknown and fixed by demanding no secular terms. It is stated to be good for periodic solutions only (7.6.19–7.6.24; comment on p. 242).
- The method of averaging (7.6.25–7.6.26).

## Toy example (ours, not from the text)
Take the linearly damped oscillator $\ddot x+x+\varepsilon\dot x=0$, so $h=\dot x$. Then $h=-r\sin\theta$.
1. $r'=\langle h\sin\theta\rangle=-r\langle\sin^2\theta\rangle=-r\cdot\tfrac12=-\tfrac12r$.
2. $r\phi'=\langle h\cos\theta\rangle=-r\langle\sin\theta\cos\theta\rangle=0$.
3. So $r(T)=r_0e^{-T/2}$ and the phase is constant.

Numbers: $\varepsilon=0.1$, $r_0=1$, $T=\varepsilon t$.
- $t=0$: $r=1$.
- $t=10$: $T=1$, $r=e^{-0.5}\approx0.607$.
- $t=20$: $T=2$, $r=e^{-1}\approx0.368$.

Check against the exact solution: the characteristic roots are $\lambda=\tfrac{-\varepsilon\pm i\sqrt{4-\varepsilon^2}}2$, whose real part $-\varepsilon/2$ gives the decay $e^{-\varepsilon t/2}$. At $t=20$ this is $e^{-0.1\cdot20/2}=e^{-1}$, matching. A regular series would give $1-\varepsilon t/2=1-1=0$ at $t=20$ and negative values beyond, which shows the failure at times of order $1/\varepsilon$.

## Concepts
- [[weakly-nonlinear-oscillator]] (new) — equation $\ddot x+x+\varepsilon h(x,\dot x)=0$ with $0\le\varepsilon\ll1$, a small perturbation of the linear oscillator (p. 217)
- [[regular-perturbation-theory]] (new) — expanding the solution as a power series in $\varepsilon$ and solving order by order (p. 218)
- [[secular-term]] (new) — a term in a perturbation series that grows without bound in time, e.g. $t\sin t$ (p. 219)
- [[two-timing]] (new) — treating fast time $\tau=t$ and slow time $T=\varepsilon t$ as independent, removing resonant terms (p. 221)
- [[averaged-equations]] (new) — $r'=\langle h\sin\theta\rangle$, $r\phi'=\langle h\cos\theta\rangle$: slow equations for amplitude and phase (p. 226)
- [[limit cycle]] — here, a closed trajectory that nearby spiralling trajectories approach: van der Pol's stable cycle of radius $2+O(\varepsilon)$ (pp. 217, 225)
- [[fixed point and stability]] — used on the amplitude equation $r'=\tfrac18r(4-r^2)$: $r^*=0$ unstable, $r^*=2$ stable (p. 224)
- [[amplitude-dependent-frequency]] (new) — frequency that varies with amplitude, intrinsically nonlinear (Duffing: $\omega=1+\tfrac38\varepsilon a^2+O(\varepsilon^2)$) (pp. 228–229)
- [[hardening-softening-spring]] (new) — stiffness $k=1+\varepsilon x^2$ grows ($\varepsilon>0$) or shrinks ($\varepsilon<0$) with displacement (p. 229)

## Canonical instances
- [[van-der-pol-oscillator]] — weakly nonlinear case: near-circular stable limit cycle, radius $2+O(\varepsilon)$, transient (56) (pp. 217, 224–228)
- [[duffing-oscillator]] — constant amplitude, amplitude-dependent frequency (57) (pp. 217, 228–229)
- [[damped-linear-oscillator-test]] — $\ddot x+2\varepsilon\dot x+x=0$, shows regular perturbation failing and two-timing succeeding (pp. 218–223)
- [[pendulum]] — named as the example of a softening spring (p. 229)

## Bridges (candidates)
- [structural-analogy] Two-timing's fast cycle vs slowly varying amplitude ↔ complex-systems: hierarchy and near-decomposability — both separate fast and slow time scales and treat them semi-independently.
- [structural-analogy] Averaging over the fast phase to get slow equations ↔ complex-systems: mean-field approximation — both replace fast fluctuations by an average.
- [metaphor] Amplitude equation with a stable nonzero fixed point ↔ complex-systems: attractor — the limit cycle appears as a fixed point of $r$.

## Questions this raises
- When does the assumption "functions of $T$ act as constants on the fast scale" fail, given that the author says it is hard to justify rigorously?
- What happens to the averaged equations when $\varepsilon$ is not small, as in the $\varepsilon=2$ computer test (Ex. 7.6.14)?
- How do the $O(\varepsilon^2)$ frequency corrections follow from the Poincaré–Lindstedt method or a super-slow time?
- Can averaging handle forcing that depends explicitly on time, as in the swing and Mathieu exercises?

## Exercises worth doing
- Ex. 7.6.2 (p. 238) — calibrate regular perturbation theory on $\ddot x+x+\varepsilon x=0$ and ask whether secular terms should appear — difficulty: easy
- Ex. 7.6.12 (p. 239) — derive the Fourier-coefficient formulas behind (51) via orthogonality — difficulty: medium
- Ex. 7.6.14 (p. 240) — averaged equations for $\ddot x+\varepsilon\dot x^3+x=0$, compared with numerics at large $\varepsilon$ — difficulty: medium
- Ex. 7.6.17 (p. 240) — averaged equations for the swing; when does the rest state become unstable? — difficulty: hard
- Ex. 7.6.19 (p. 241) — Poincaré–Lindstedt method for Duffing; recovers $\omega_1=\tfrac38a^2$ — difficulty: medium
- Ex. 7.3.9 (p. 235) — regular perturbation theory used for a closed orbit shape — difficulty: medium

## Reading notes
- **Where the unit starts and ends.** It starts on p. 217 in the middle of a paragraph near the end of Section 7.5 ("and the crawls…"). It then covers all of Section 7.6 (pp. 217–229) and the "Exercises for Chapter 7" (pp. 230–243), which also contain exercises for Sections 7.1–7.5 whose text is not on these pages. The part begins mid-paragraph inside Section 7.5, so on these pages the split does not coincide with a section start.
- **Page offset:** printed = pdf − 15.
- **Text layer:** many symbols ($\varepsilon$, $\tau$, $\phi$, $\partial$) are garbled in the extracted text. Equations were checked against the page images.
- **Probable sign misprint in (37):** substituting (36) into (35) gives a right side with the opposite overall sign. For example, $-2\partial_{\tau T}x_0=+2(r'\sin(\tau+\phi)+r\phi'\cos(\tau+\phi))$. The printed (37) and (39) have the reverse sign, whereas (49) has the sign I get. Conditions (40)–(41), and hence (42)–(43), do not depend on the sign.
- **Other small misprints:**
  - In (49) the cosine is printed $\cos(t+\phi)$, presumably meaning $\tau+\phi$.
  - In the evaluation of $\langle\cos^3\sin\rangle$ on p. 227 the factor $\tfrac14$ is missing from the integral; the value 0 is unaffected.
  - Ex. 7.6.25(c) shows $\sin(t+\theta)$, presumably meaning $\sin(t+\phi)$.
- The Cartwright formula on p. 217 is not shown in these pages.
