---
id: astrom-2021-feedbacksystems/ch10-frequency
work: astrom-2021-feedbacksystems
unit: "10 Frequency Domain Analysis"
pages: 10-1 to 10-32 (chapter-style printed numbers)
fields: [control-theory]
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
# Frequency Domain Analysis (Åström & Murray, ch. 10)

## L0 — One line
Stability and robustness of a feedback loop can be read from how sinusoids travel around the loop, i.e. from the shape of the open-loop frequency response $L(i\omega)$ relative to the critical point $-1$ (the Nyquist criterion and the margins built on it).

## L1 — The gist (≤ 120 words)
How can we tell whether a closed loop is stable, and how far from instability it is, by looking only at the open-loop transfer function $L=PC$? Nyquist's answer: trace $L(s)$ along the Nyquist contour and count encirclements of $-1$. With a winding-number correction for unstable open-loop poles, it still gives a stability test. How closely the curve passes $-1$ gives gain, phase and stability margins. The chapter also covers Bode's gain–phase relation, non-minimum-phase systems, and extensions to nonlinear loops (small-gain theorem, passivity, circle criterion, describing functions). It matters because it shows how a controller should be changed, not just whether the loop is stable.

**Prerequisites:** transfer functions and frequency response (Bode plots); complex numbers (magnitude, argument); poles/zeros and stability; basic Fourier series and eigenvalues of matrices (for §10.5).

## L2 — Key ideas (5–10 bullets)
- Oscillation can persist in a loop if $L(i\omega_0)=-1$. The point $-1$ is the "critical point", and stability is judged by how the frequency response sits relative to it (p. 10-2, 10-3).
- Time delay does not change $|L|$ but adds phase lag, so a small delay can destabilise a loop that is stable without it (Example 10.1, p. 10-4).
- Simplified Nyquist criterion: if $L$ has no poles in the closed right half-plane (except possibly at the origin), the loop is stable iff the Nyquist curve has no net encirclement of $-1$ (Thm 10.1, p. 10-6).
- General criterion: $Z=N+P$, with $N$ the clockwise encirclements of $-1$ and $P$ the open-loop unstable poles. It follows from the principle of variation of the argument and explains conditional stability, where raising gain can stabilise (p. 10-10 to 10-14).
- Gain, phase and stability margins measure distance from $-1$. They are related by (10.7), and good gain and phase margins can still hide a small stability margin (p. 10-15 to 10-18).
- For minimum-phase systems phase is fixed by the gain curve (Bode's relation). Delays and right-half-plane poles or zeros add extra phase lag and limit performance (p. 10-19, 10-20).
- Gain generalises to the $\infty$-norm $\|G\|_\infty$ and phase to an angle between signals. This gives the small-gain theorem, the passivity theorem and the circle criterion for nonlinear loops (p. 10-22 to 10-24).
- Describing functions predict possible limit cycles from the intersection of $H(i\omega)$ with $-1/N(a)$. The method is approximate because it neglects higher harmonics (p. 10-25, 10-26).

## L3 — Walkthrough

### Opening epigraph and framing (p. 10-1)
The epigraph from Nyquist (1956) says that a feedback factor much larger than one gave good performance, and that "stability with a feedback factor larger than unity was puzzling." The chapter studies stability and robustness by following sinusoids of different frequencies around the loop, and reasons about the closed loop via the open-loop transfer function (p. 10-1). The authors contrast this with proving stability by Lyapunov functions (Chapter 5): the Nyquist criterion allows us to determine more than just whether a system is stable or unstable. The Nyquist criterion also gives *degrees* of stability (margins) and indicates how to change an unstable system (p. 10-1, 10-2).

### 10.1 The Loop Transfer Function (p. 10-1 to 10-4)
**Traditional test.** With $P=n_p/d_p$ and $C=n_c/d_c$ (Fig. 10.1a):
$$G_{yr}(s)=\frac{PC}{1+PC}=\frac{n_p(s)n_c(s)}{d_p(s)d_c(s)+n_p(s)n_c(s)},\qquad \lambda(s)=d_p(s)d_c(s)+n_p(s)n_c(s).$$
The loop is stable iff all roots of $\lambda$ have negative real part. This is straightforward but gives little design guidance (p. 10-2).

**Nyquist's idea.** Break the loop (Fig. 10.1b) and define the *loop transfer function* $L(s)=P(s)C(s)$. It is the transfer function from point A to point B, multiplied by $-1$ for negative feedback (p. 10-2).
- Inject a sinusoid of frequency $\omega_0$ at A. In steady state B carries a sinusoid of the same frequency.
- If B has the same amplitude and phase as A, we could disconnect the injected signal and connect A to B, so, the authors say, it seems reasonable that an oscillation can be maintained. Tracing signals gives the condition
$$L(i\omega_0)=-1 \tag{10.1}$$
- The point $-1$ is called the *critical point*. Let $\omega_c$ be a frequency with $\angle L(i\omega_c)=180^\circ$. Then the system is stable if $|L(i\omega_c)|<1$. The authors call this "essentially true", but it has subtleties that require the proper Nyquist theory (p. 10-3).

**Example 10.1 (motor with proportional controller and delay)** (p. 10-3, 10-4). A DC motor has inertia $J$ and damping $c$; position is sensed with delay $\tau$ (Fig. 10.2).
$$P(s)=\frac{k_I}{Js^2+cs},\quad C(s)=k_p,\quad L(s)=P(s)C(s)e^{-\tau s}=\frac{k_Ik_p}{Js^2+cs}e^{-\tau s}.$$
- Without delay ($\tau=0$), the text says the phase of $L$ goes from 90° near $s=0$ to 180° for large $s$. (Fig. 10.3a shows the phase falling from $-90^\circ$ towards $-180^\circ$, i.e. a lag.) The gain falls with frequency, so the oscillation condition cannot be met: the gain is below 1 at high frequency (p. 10-3).
- With a delay, the magnitude of $L$ is unchanged, but the phase lag grows with $\tau$ (p. 10-4).
- Let $\omega_0$ be the frequency where $|L(i\omega_0)|=1$ and $\theta_0$ the phase of the undelayed system there. A delay $\tau_c=(\pi+\theta_0)/\omega_0$ gives $L(i\omega_0)=-1$, so an oscillation may result (p. 10-4).
- Fig. 10.3 (parameters $k_I=1$, $J=2$, $c=1$, $k_p=1$; caption $\tau=0,1,3$, legend $\tau=0,\tau_c,3\tau_c$) shows stable, oscillatory and unstable step responses as the delay grows. Delayed disturbances return in phase with the originals. If the loop gain is $\ge 1$ this can lead to instability (p. 10-4).

**Intuition note.** Delay costs only phase, never gain. Instability can arise when the signal returns *in phase* (angle $-180^\circ$ in $L$) with loop gain of at least 1. The full test, however, is the encirclement count of the next section, not the gain at one crossing.

Working with $L=PC$ shows directly how to change the controller: scaling the gain scales the curve, so the critical point can be avoided. Reducing gain or otherwise avoiding $-1$ is the simplest way to stabilise. Systematic ways ("loop shaping") come in Chapter 12 (p. 10-4).

### 10.2 The Nyquist Criterion (p. 10-4 to 10-14)

**The Nyquist plot** (p. 10-5). The *Nyquist contour* $\Gamma\subset\mathbb C$ (the "D contour") is the imaginary axis together with an arc at infinity. The *Nyquist plot* is the image of $L(s)$ as $s$ traverses $\Gamma$ clockwise (Fig. 10.4).
- If $L\to0$ for large $s$ (the usual case), the arc at infinity maps to the origin.
- The part for $\omega<0$ is the mirror image of the part for $\omega>0$.
- If $L$ has poles on the imaginary axis, $\Gamma$ gets small semicircles to the right of them. For a pole at the origin:
$$\Gamma=\lim_{\substack{r\to0\\R\to\infty}}\Big(\big(-iR,-ir\big)\cup\{re^{i\theta}:\theta\in[-\tfrac\pi2,\tfrac\pi2]\}\cup\big(ir,iR\big)\cup\{Re^{-i\theta}:\theta\in[-\tfrac\pi2,\tfrac\pi2]\}\Big)\tag{10.2}$$

**Theorem 10.1 (Simplified Nyquist criterion)** (p. 10-6). Let $L(s)$ be the loop transfer function of a negative feedback system (Fig. 10.1a) with no poles in the closed right half-plane ($\operatorname{Re}s\ge0$) except possibly at the origin. Then $G_{cl}=L/(1+L)$ is stable **if and only if** the image of $L$ along $\Gamma$ (10.2) has no net encirclements of $-1$.
- Procedure: put a pin at $-1$, attach a string to the curve and move it along the curve. There is no encirclement if the string does not wind up on the pin. The number of encirclements is the *winding number* (p. 10-6).

**Intuition note.** The curve $L(i\omega)$ is a record of how every frequency is amplified and delayed around the loop. Stability fails exactly when this record wraps around the "perfectly reinforcing" point $-1$. (Applies when $L$ has no right-half-plane poles.)

**Example 10.2 (third-order system)** (p. 10-6, 10-7). For $L(s)=1/(s+a)^3$, on $s=i\omega$:
$$L(i\omega)=\frac{1}{(i\omega+a)^3}=\frac{(a-i\omega)^3}{(a^2+\omega^2)^3}=\frac{a^3-3a\omega^2}{(a^2+\omega^2)^3}+i\,\frac{\omega^3-3a^2\omega}{(a^2+\omega^2)^3}.$$
Fig. 10.5 uses $a=0.6$. On the outer arc $s=Re^{-i\theta}$, $L=1/(Re^{-i\theta}+a)^3\to0$ as $R\to\infty$, so the arc maps to the origin (p. 10-7).

**Sketching from the Bode plot** (p. 10-7). Plot $L(i\omega)$ for $\omega$ from 0 to $\infty$ from magnitude and phase. Add the arc $L(Re^{i\theta})$, which goes to zero if the high-frequency gain goes to zero (iff $L$ strictly proper). Mirror the curve for the dashed part, and label with arrows for clockwise traversal.

**Example 10.3 (pole at origin)** (p. 10-7, 10-8). $L(s)=k/(s(s+1)^2)$, nominal $k=1$ (Fig. 10.6).
- Gain slope is $-1$ at low frequency and $-3$ after the double pole at $\omega=1$. For small $s$, $L\approx k/s$, so the low-frequency asymptote meets unit gain at $\omega=k$.
- Phase goes $-90^\circ\to-180^\circ$ at $\omega=1$ $\to-270^\circ$.
- The Nyquist curve starts at phase $-90^\circ$, crosses the negative real axis at $\omega=1$ where $L(i)=-0.5$, and goes to zero along the imaginary axis. The small semicircle at the origin maps to a large circle in the right half-plane.
- No encirclement of $-1$ means the loop is stable. Since $L(i)=-k/2$, it becomes unstable if the gain increases to $k=2$ or beyond (p. 10-8).

The criterion does *not* require $|L(i\omega_c)|<1$ at every negative-real-axis crossing. It requires zero net encirclements, so the curve may cross at magnitude above 1 and cross back. This surprised early amplifier designers (the epigraph). Changing gain just scales the curve (p. 10-8).

**Example 10.4 (Internet congestion control)** (p. 10-8, 10-9). $N$ identical TCP sources share one router with admission control; a disturbance $d$ models external traffic (Fig. 10.7a). Variables: $w$ window size per source, $q$ end-to-end drop probability, $b$ buffer occupancy, $p$ router drop probability, $\bar w$ total packets from the $N$ sources. Transfer functions (from Exercise 9.6), with forward/backward delays pulled out as separate blocks:
$$\tilde G_{b\bar w}(s)=\frac{1}{\tau_e^ps+e^{-\tau^fs}},\quad G_{wq}(s)=-\frac{1}{q_e(\tau_e^ps+q_ew_e)},\quad \tilde G_{pb}(s)=\rho.$$
Here $(w_e,b_e)$ is the equilibrium, $\tau_e^p$ the steady-state round-trip time, and $\tau^f,\tau^b$ forward and backward propagation times. The loop transfer function is
$$L(s)=\rho\cdot\frac{N}{\tau_e^ps+e^{-\tau^fs}}\cdot\frac{1}{q_e(\tau_e^ps+q_ew_e)}\,e^{-\tau_e^ts},\qquad \tau^t=\tau^p+\tau^f+\tau^b .$$
Using $w_e=b_e/N=\tau_e^pc/N$ and $q_e=2/(2+w_e^2)\approx2/w_e^2=2N^3/(\tau_e^pc)^2$ (eq. (4.17)), the authors state
$$L(s)=\rho\cdot\frac{N}{\tau_e^ps+e^{-\tau^fs}}\cdot\frac{c^3(\tau_e^p)^3}{2N^2\big(c(\tau_e^p)^2s+2N\big)}\,e^{-\tau_e^ts}.$$
- Approximation near the phase-crossover frequency $\omega_{pc}$. The second factor is stable if $\tau_e^p>\tau^f$ and fast, so use its zero-frequency gain $N$. The third factor is slow (the text says it can be shown that $2N\ll c(\tau_e^p)^2\omega_{pc}$), so approximate it by an integrator:
$$L(s)\approx\rho\cdot N\cdot\frac{c^3(\tau_e^p)^3}{2N^2\,c(\tau_e^p)^2s}\,e^{-\tau_e^ts}=\frac{\rho c^2\tau_e^p}{2Ns}\,e^{-\tau_e^ts}.$$
- The integrator gives phase lag $\pi/2$, and the text states $\omega_{pc}=\pi/(2\tau_e^p)$. A necessary condition for stability is $|L(i\omega_{pc})|<1$, i.e.
$$\frac{\rho c^2(\tau_e^p)^2}{\pi N}<1 .$$
- If the quantity exceeds 1, the loop is unstable by the Nyquist criterion. For fixed $\tau_e^p$ the system becomes unstable as link capacity $c$ grows, so TCP may not scale to high-capacity networks (Low et al.). Exercise 10.3 suggests ways around this (p. 10-9).

### The General Nyquist Criterion (advanced section, p. 10-10 to 10-13)
Theorem 10.1 excludes right-half-plane poles of $L$; the general case needs complex-variable theory. Here encirclements are counted *counterclockwise* (mathematical convention) (p. 10-10).

**Theorem 10.2 (Principle of variation of the argument)** (p. 10-10). Let $\Gamma$ be a closed contour with interior $D$. Assume $f:\mathbb C\to\mathbb C$ is analytic on $\Gamma$ and in $D$ except for a finite number of poles and zeros in $D$. Then the winding number of $f(s)$ as $s$ traverses $\Gamma$ counterclockwise is
$$n_{w,\Gamma}(f(s))=\frac1{2\pi}\Delta\arg_\Gamma f(s)=\frac1{2\pi i}\int_\Gamma\frac{f'(s)}{f(s)}ds=n_{z,D}-n_{p,D},$$
where $\Delta\arg_\Gamma$ is the net change of angle, $n_{z,D}$ and $n_{p,D}$ count zeros and poles in $D$, and a zero or pole of multiplicity $m$ counts $m$ times.

*Why (graphical idea, Fig. 10.8; p. 10-10, 10-11).* Write
$$f(s)=\frac{(s-z_1)\cdots(s-z_m)}{(s-p_1)\cdots(s-p_n)}\tag{10.3}$$
as $r_1e^{i\psi_1}\cdots r_me^{i\psi_m}/(\rho_1e^{i\theta_1}\cdots\rho_ne^{i\theta_n})$ (the text's denominator index "$\rho_m$" appears to be $\rho_n$). Then $\arg f=\sum_i\psi_i-\sum_i\theta_i$. A zero or pole outside $\Gamma$ contributes no net angle change. One inside contributes $+2\pi$ (zero) or $-2\pi$ (pole). So the total is $2\pi(n_{z,D}-n_{p,D})$.

*Formal proof* (p. 10-11).
1. Near a zero $s=a$ of multiplicity $m$: $f(s)=(s-a)^mg(s)$ with $g$ analytic and nonzero.
2. Then $f'/f=m/(s-a)+g'/g$, and the second term is analytic at $a$. So $f'/f$ has a single pole at $a$ with residue $m$.
3. The residues at zeros sum to $n_{z,D}$; at poles they sum to $-n_{p,D}$. Hence
$$n_{z,D}-n_{p,D}=\frac1{2\pi i}\int_\Gamma\frac{f'}{f}ds=\frac1{2\pi i}\int_\Gamma\frac d{ds}\log f\,ds=\frac1{2\pi i}\Delta\arg_\Gamma\log f(s).$$
4. $\log f=\log|f|+i\arg f$. $|f|$ returns to its value around a closed contour, so $\Delta\arg_\Gamma\log f=i\Delta\arg_\Gamma\arg f$. (added step: substituting gives $\frac{1}{2\pi i}\cdot i\,\Delta\arg f=\frac1{2\pi}\Delta\arg f$, the first form of the theorem.)

**Intuition note.** A closed curve of $f$ winds around the origin once for each zero inside the contour and backwards once for each pole inside. So counting windings counts "zeros minus poles" without finding them.

**Contour and orientation** (p. 10-12). Take $-iR\le s\le iR$ plus a right semicircle of radius $R$, with small right semicircles of radius $r$ around imaginary-axis poles. Choose $R$ large and $r$ small enough that all open-loop right-half-plane poles are enclosed. This $\Gamma$ has orientation *opposite* to Fig. 10.4a. Engineers traverse it clockwise (increasing frequency goes up the imaginary axis, easy to sketch from a Bode plot). Mathematicians count winding counterclockwise. The difference does not matter if the same convention is used for both the traversal and the winding number.

**Theorem 10.3 (General Nyquist criterion)** (p. 10-12). Let $L(s)$ have $n_{p,rhp}$ poles in the region enclosed by $\Gamma$, and let $n_{w,\Gamma}(1+L(s))$ be the counterclockwise winding number of $1+L(s)$ along $\Gamma$. Assume $1+L(i\omega)\neq0$ for all $\omega$ on $\Gamma$ and
$$n_{w,\Gamma}(1+L(s))+n_{p,rhp}=0 .$$
Then the closed loop has no poles in the closed right half-plane and is stable.

*Proof* (p. 10-12). Apply Theorem 10.2 to $f=1+L$. The closed-loop poles are the zeros of $f$, which has none on $\Gamma$. The winding-number condition then says $f$ has no zeros in the right half-plane. Since $1+L$ is a shifted copy of $L$, we state it as net encirclements of $-1$ by the image of $L$.
- Condition $1+L(i\omega)\ne0$: the curve does not pass through $-1$.
- The *winding number condition*: the curve encircles $-1$ as many times as $L$ has right-half-plane poles (p. 10-12).

**Clockwise form** (p. 10-12, 10-13). Let $P$ = number of unstable poles of $L$, $N$ = clockwise encirclements of $-1$, $Z$ = number of unstable zeros of $1+L$ (= unstable closed-loop poles). Then
$$Z=N+P .$$
(added step: Thm 10.2 gives counterclockwise winding number $Z-P$ for counterclockwise traversal of $\Gamma$. Traversing $\Gamma$ clockwise flips the sign, and counting encirclements clockwise flips it again, so $N=Z-P$, i.e. $Z=N+P$. Check with Example 10.5: $N=-1$, $P=1$ gives $Z=0$.) Poles on the imaginary axis produce parts of the curve with large magnitude, so the winding number needs care (p. 10-13).

**Example 10.5 (stabilised inverted pendulum)** (p. 10-13). $P(s)=1/(s^2-1)$ (input: pivot acceleration; output: angle). PD controller $C(s)=k(s+2)$, so $L(s)=k(s+2)/(s^2-1)$, with $L(0)=-2k$, $L(\infty)=0$.
- For $k>0.5$ the curve encircles $-1$ counterclockwise (contour clockwise), so $N=-1$. With $P=1$: $Z=N+P=0$, stable.
- For $k<0.5$ there is no encirclement and the closed loop has one right-half-plane pole.
- So the system is unstable for small gains and stable for high gains.

**Conditional stability** (p. 10-13, 10-14). An unstable system can often be stabilised by *reducing* gain, but as Example 10.5 shows, sometimes *increasing* it stabilises. Electrical engineers designing feedback amplifiers first met this and coined *conditional stability*. It was a strong motivation for Nyquist's theory.

**Example 10.6** (p. 10-14). $L(s)=\dfrac{3k(s+6)^2}{s(s+1)^2}$ (10.4); Fig. 10.10 uses $k=1$. The curve crosses the negative real axis twice: at $L=-12$ for $\omega=2$ and at $L=-4.5$ for $\omega=3$.
- The tracing argument of Fig. 10.1b is misleading here: a unit sinusoid at 2 rad/s injected at A returns in phase with amplitude 12, which suggests instability.
- Yet the winding number is zero, so Theorem 10.3 shows stability.
- More precisely: stable for $k>2/9$, unstable for $1/12<k<2/9$, stable again for $k<1/12$.

**Intuition note.** What matters is the *net winding*, not the gain at a single crossing. A large loop gain at one crossing does not by itself mean instability: in Example 10.6 the curve crosses at $-12$ and the winding number is still zero.

### 10.3 Stability Margins (p. 10-14 to 10-18)
Practical designs need margins describing how far from instability they are (p. 10-14).
- **Stability margin** $s_m$: shortest distance from the Nyquist curve to $-1$. The curve then lies outside a circle of radius $s_m$ around $-1$ (p. 10-15).
- Increasing controller gain expands the Nyquist curve radially; increasing controller phase turns it clockwise. Hence the amount of gain or phase that can be added before instability can be read off the plot (p. 10-15).
- **Gain margin** $g_m$: smallest multiplier of loop gain that makes the system unstable. With several crossings, take the one closest to $-1$. Let $\omega_{pc}$ be the *phase crossover frequency*, where the curve crosses the negative real axis ($\angle L=-180^\circ$):
$$g_m=\frac1{|L(i\omega_{pc})|}\tag{10.5}$$
- **Phase margin**: phase lag needed to reach the stability limit. With *gain crossover frequency* $\omega_{gc}$ (where $|L|=1$; the text writes $L(i\omega_{pc})$ here, which looks like a misprint):
$$\varphi_m=180^\circ+\angle L(i\omega_{gc})\tag{10.6}$$
With several intersections, use the one closest to $-1$ (p. 10-15, 10-16).
- On a Bode plot, find $\omega_{pc}$ where phase is $-180^\circ$ and invert the gain there; find $\omega_{gc}$ where gain is 1 and add $180^\circ$ to the phase. If the curves cross the reference lines many times, use the Nyquist plot instead (p. 10-16).

**Relations among margins** (p. 10-16):
$$g_m\ge\frac1{1-s_m},\qquad \varphi_m\ge2\arcsin(s_m/2)\tag{10.7}$$
They follow from Fig. 10.12 (the text's reference; Fig. 10.11a shows the margins) and the fact that $s_m$ is less than the distance $d=2\sin(\varphi_m/2)$ from $-1$ to the gain-crossover point. (added step for the first: the distance from $-1$ to $-1/g_m$ is $1-1/g_m$, and $s_m$ is at most this, so $1/g_m\le1-s_m$ for $s_m<1$.)

**Drawbacks** (p. 10-16). $s_m$ has no natural place on a Bode plot; it equals $1/M_s$, where $M_s$ is the peak magnitude of $1/(1+PC)$ (Chapter 13). Gain and phase margins must *both* be given to ensure the curve is not near $-1$. The winding number is hard to show on a Bode plot. In general, use the Nyquist plot.

**Example 10.7** (p. 10-16). $L(s)=3/(s+1)^3$ gives $g_m=2.67$, $\varphi_m=41.7^\circ$, $s_m=0.464$ (Fig. 10.12).

**Example 10.8 (good gain/phase margins, poor stability margin)** (p. 10-16, 10-17). $L(s)=\dfrac{0.38(s^2+0.1s+0.55)}{s(s+1)(s^2+0.06s+0.5)}$. Numerically $g_m=266$ and $\varphi_m=70^\circ$ look robust, but the Nyquist curve passes close to $-1$: $s_m=0.27$ (very low). The closed loop has two resonant modes, with damping ratios $\zeta=0.81$ and $\zeta=0.014$, and a highly oscillatory step response (Fig. 10.13).

**Typical values** (p. 10-17): $\varphi_m=30^\circ$–$60^\circ$, $g_m=2$–$5$, $s_m=0.5$–$0.8$. The *delay margin* is the smallest added time delay that makes the system unstable. For quickly decaying loop gains it is closely related to the phase margin. If the gain curve has several high-frequency peaks, it is the more relevant measure.

**Example 10.9 (AFM nanopositioner)** (p. 10-17, 10-18). A spring–mass model with low damping:
$$P(s)=\frac{\omega_0^2}{s^2+2\zeta\omega_0s+\omega_0^2}\tag{10.8}$$
with e.g. $\zeta=0.1$. With integral action, $L(s)=k_i\omega_0^2/(s(s^2+2\zeta\omega_0s+\omega_0^2))$.
- The phase crossover is $\omega_{pc}=\omega_0$, independent of $k_i$. There $L(i\omega_0)=-k_i/(2\zeta\omega_0)$, so $s_m=1-k_i/(2\zeta\omega_0)$.
- Choosing $s_m$ requires $k_i=2\zeta\omega_0(1-s_m)$.
- Fig. 10.14 (parameters $\zeta=0.01$, $k_i=0.008$) shows $g_m=2.5$ and $s_m=0.6$. The gain curve is nearly a straight line at low frequency with a resonant peak at $\omega_0$. The gain crossover is approximately $k_i$. Phase falls monotonically from $-90^\circ$ to $-270^\circ$, equal to $-180^\circ$ at $\omega_0$. Raising $k_i$ shifts the gain curve up and raises the gain crossover.

### 10.4 Bode's Relations and Minimum Phase Systems (p. 10-18 to 10-22)
Bode plots suggest a link between gain and phase: integrator slope $-1$ with phase $-\pi/2$; differentiator slope $+1$ with phase $\pi/2$; $G=s+a$ has slope $0\to+1$ and phase $0\to\pi/2$ (p. 10-18, 10-19). Bode found an exact relation for a special class: systems with no time delays and no right-half-plane poles or zeros, and with $\log|G(s)|/s\to0$ as $s\to\infty$ for $\operatorname{Re}s\ge0$. He called them *minimum phase* because they have the smallest phase lag of all systems with the same gain curve (p. 10-19). For them the phase is determined by the gain curve and vice versa:
$$\arg G(i\omega_0)=\frac\pi2\int_0^\infty f(\omega)\frac{d\log|G(i\omega)|}{d\log\omega}\frac{d\omega}{\omega}\approx\frac\pi2\frac{d\log|G(i\omega)|}{d\log\omega}\Big|_{\omega=\omega_0}\tag{10.9}$$
$$f(\omega)=\frac2{\pi^2}\log\Big|\frac{\omega+\omega_0}{\omega-\omega_0}\Big|,\qquad\int_0^\infty f(\omega)\frac{d\omega}{\omega}=1\tag{10.10}$$
So the phase is a weighted average of the slope of the gain curve. The sign of a minimum-phase $G$ must be chosen so that $\angle G>\angle(-G)$ (since $|G|=|-G|$ and $\angle(-G)=\angle G-180^\circ$) (p. 10-19).

**Intuition note.** For a minimum-phase system, if the gain curve falls with slope $-n$ around a frequency, the phase there is roughly $-n\cdot90^\circ$ (exactly so for constant slope, Example 10.10; otherwise (10.9) is an approximation). So the phase can be estimated from the slope of the gain curve.

**Example 10.10** (p. 10-19). $G=s^n$: $\log G=n\log s$, so $d\log G/d\log s=n$ and $\arg G(i\omega_0)=\frac\pi2\int_0^\infty nf(\omega)\frac{d\omega}\omega=n\frac\pi2$ by (10.10). Constant gain slope $n$ gives the horizontal phase line $n\pi/2$.

**Non-minimum-phase examples** (Fig. 10.15; p. 10-20). In each case the minimum-phase system with the same unit gain is $G=1$.
- Time delay $G=e^{-s\tau}$: $|G|=1$, $\arg G=-\omega\tau$, an extra lag growing linearly with $\omega$.
- RHP zero $G=(a-s)/(a+s)$, $a>0$: $|G|=1$, $\arg G=-2\arctan(\omega/a)$.
- RHP pole $G=(s+a)/(s-a)$, $a>0$: $\arg G=-2\arctan(a/\omega)$.
- RHP poles and zeros severely limit achievable performance (Chapter 14) and should be avoided by redesign. Poles are intrinsic to the system. Zeros depend on how inputs and outputs couple to the states, so moving or adding sensors and actuators can change them. Non-minimum-phase systems are quite common.

**Example 10.11 (vehicle steering)** (p. 10-20 to 10-22). From steering angle to lateral position (Ex. 6.13):
$$P(s)=\frac{av_0s+v_0^2}{bs^2},$$
with $v_0$ the velocity and $a,b>0$. The text places the zero at $s=v_0/a$. Setting the numerator to zero gives $-v_0/a$ (see Reading notes). Driving forward puts the zero in the left half-plane; reversing ($v_0<0$) puts it in the right half-plane. The unit step response is
$$y(t)=\frac{av_0t}b+\frac{v_0^2t^2}{2b}.$$
- It starts like an integrator. For $v_0<0$ the initial motion is in the wrong direction (an *inverse response*, typical of non-minimum-phase systems).
- Fig. 10.16 uses $a=1.5$ m, $b=3$ m, $v_0=\pm2$ m/s. The reverse case shows an initial motion in the opposite direction and a delay before the car moves as desired. The gain curves are identical for both directions; only the phase differs.
- The zero's position depends on the sensor location. The calculation puts the sensor at the center of mass; with the sensor at the rear wheel the zero disappears and there is no inverse response.
- Small-$t$ behaviour $y\approx av_0t/b$ relates to the high-frequency behaviour $P\approx av_0/(bs)$; large-$t$ behaviour relates to low-frequency properties. The initial value theorem (Sec. 9.3) makes this formal (p. 10-22).

### 10.5 Generalized Notions of Gain and Phase (advanced section, p. 10-22 to 10-26)
The aim is to extend gain and phase to more general systems, including some nonlinear ones, and to find Nyquist analogues when signals are approximately sinusoidal (p. 10-22).

**System gain and passivity.**
- *Static linear case* $y=Au$, $A$ complex and not necessarily square. With the Euclidean norm $\|u\|=\sqrt{\sum|u_i|^2}$ (10.11), $\|y\|^2=u^*A^*Au$ ($^*$ = conjugate transpose). $A^*A$ is positive semidefinite (the text calls it symmetric) and $\|y\|^2\le\bar\lambda(A^*A)\|u\|^2$, with $\bar\lambda$ the largest eigenvalue. The gain is
$$\gamma=\max_u\frac{\|y\|}{\|u\|}=\sqrt{\bar\lambda(A^*A)}\tag{10.12}$$
The square roots of the eigenvalues of $A^*A$ are the *singular values* of $A$; the largest is $\bar\sigma(A)$ (p. 10-22).
- *Dynamical systems.* Treat inputs and outputs as signals in $L_2$ (square-integrable functions), $\|u\|_2=\sqrt{\int_0^\infty|u|^2(\tau)d\tau}$. For vector signals, replace $|\cdot|$ by (10.11). The gain is
$$\gamma=\sup_{u\in L_2}\frac{\|y\|_2}{\|u\|_2}\tag{10.13}$$
where the supremum (smallest number $\ge$ the argument) is used because a maximum may not exist. This can even be used for some nonlinear systems, with care about initial conditions and global nonlinearities (p. 10-23).
- Roughly: a system is *BIBO stable* if bounded inputs give bounded outputs for all initial states. It is *input-to-state stable* (ISS) if $\|x(t)\|\le\beta(\|x(0)\|)+\gamma(\|u\|)$ with $\beta,\gamma$ monotonically increasing and vanishing at the origin (p. 10-23).
- For a stable SISO linear system, it can be shown that
$$\gamma=\sup_\omega|G(i\omega)|=:\|G\|_\infty\tag{10.14}$$
the peak of the frequency response (the "infinity norm"). For a multivariable system with transfer matrix $G(s)$:
$$\gamma=\|G\|_\infty=\sup_\omega\bar\sigma(G(i\omega))\tag{10.15}$$
- *Phase.* Define the angle between signals by $\langle u,y\rangle=\|u\|\|y\|\cos\varphi$ (10.16), with $\langle u,y\rangle=\int_0^\infty u(\tau)y(\tau)d\tau$ for $L_2$ signals. Systems whose input–output phase is $90^\circ$ or less for all inputs are *passive*; strictly less than $90^\circ$ means *strictly passive* (p. 10-23, 10-24).

**Intuition note.** The largest amplification of any input is the tallest peak of $|G(i\omega)|$, which is the resonance. For matrices the same role is played by the largest singular value.

**Extensions of the Nyquist criterion** (p. 10-24, 10-25). For linear loops, Nyquist implies stability if $|L(i\omega)|<1$ at all frequencies.
- **Theorem 10.4 (Small gain).** Consider the loop of Fig. 10.17 ($H_1$ and $H_2$ input/output stable, signal spaces and initial conditions properly defined) with gains $\gamma_1,\gamma_2$. Then the closed loop is input/output stable if $\gamma_1\gamma_2<1$, and its gain is
$$\gamma=\frac{\gamma_1}{1-\gamma_1\gamma_2}.$$
- **Passivity theorem** (stated in prose): for the loop of Fig. 10.17, the closed loop is stable if both $H_1$ and $H_2$ are passive and one of them is strictly passive. It generalises the linear fact that the loop is stable if the phase of $H_1H_2$ is always below $180^\circ$.
- **Theorem 10.5 (Circle criterion).** Let $H_1$ be linear with transfer function $H(s)$ and $H_2$ a static nonlinearity $F(x)$ sector-bounded as
$$k_{low}x\le F(x)\le k_{high}x\tag{10.17}$$
(Fig. 10.18). The negative-feedback closed loop is stable if the Nyquist curve of $H(i\omega)$ is outside the circle with diameter $-1/k_{low}\le x\le-1/k_{high}$ and the encirclement condition is satisfied.

The authors call these extensions powerful and easy to apply, and refer to [Kha01] for proofs; they will be used in Chapter 13 (p. 10-25).

**Describing functions** (p. 10-25, 10-26). For a loop of a linear system $H$ and a static nonlinearity $F$ (Fig. 10.19a), look for conditions that maintain an oscillation. If $H$ is low-pass, its output is approximately sinusoidal even for irregular input, so we follow only the first harmonic. Expand
$$F(ae^{i\omega t})=\sum_{n=0}^\infty M_n(a)e^{i(n\omega t+\varphi_n(a))}.$$
The *describing function* is the complex gain of the first harmonic:
$$N(a)=M_1(a)e^{i\varphi_1(a)}\tag{10.18}$$
It can also be computed from the first Fourier term of the output for sinusoidal input. Neglecting higher harmonics, an oscillation can be maintained if
$$H(i\omega)N(a)=-1\tag{10.19}$$
i.e. the phase of $H(i\omega)N(a)$ is $180^\circ$ and its magnitude is one. Plot $H(i\omega)$ and $-1/N(a)$ ($a$ from 0 to $\infty$) together (Fig. 10.19b). Their intersection gives the predicted amplitude and frequency of the oscillation (a possible limit cycle). The method is approximate because higher harmonics are neglected (p. 10-26).

**Intuition note.** The describing function is "gain of a nonlinearity for a sine of size $a$". Nyquist's fixed point $-1$ becomes a *curve* $-1/N(a)$, because the nonlinear gain depends on amplitude.

**Example 10.12 (relay with hysteresis)** (p. 10-26, 10-27). The relay output has amplitude $b$ and switches at input $\pm c$. For input $u=a\sin\omega t$: the output is zero if $a\le c$; for $a>c$ it is a square wave of amplitude $b$ switching at $\omega t=\arcsin(c/a)+n\pi$. The first harmonic is $y(t)=\frac{4b}\pi\sin(\omega t-\alpha)$ with $\sin\alpha=c/a$. For $a>c$:
$$N(a)=\frac{4b}{a\pi}\Big(\sqrt{1-\frac{c^2}{a^2}}-i\frac ca\Big),\qquad\frac1{N(a)}=\frac{\pi\sqrt{a^2-c^2}}{4b}+i\frac{\pi c}{4b}.$$
In the text, $H(s)=2/(s+1)^4$ with $b=1$, $c=0.5$ gives an intersection at $a=1$, $\omega=0.77$ rad/s: a possible oscillation if process and relay are connected in feedback (Fig. 10.20). A relay without hysteresis has $N(a)=4b/(a\pi)$, so $-1/N(a)$ is the negative real axis. For a saturation, $-1/N(a)$ is the part of the negative real axis from $-\infty$ to $-1$ (p. 10-27).

### 10.6 Further Reading (p. 10-27, 10-28)
- Nyquist's criterion appeared in the Bell System Technical Journal in 1932 [Nyq32]. Nyquist used $+1$ as the critical point; Bode changed it to $-1$, now standard.
- Nyquist used a direct calculation based on sinusoid propagation, not complex function theory. MacColl [Mac45] gives the short proof via the principle of variation of the argument. Bode [Bod45] used complex function theory extensively and treated minimum phase in detail.
- Khalil [Kha01] is the reference for passivity, small gain and describing functions. Frequency methods saw a resurgence with robust control in the 1980s (Chapter 13).

## Toy example (ours, not from the text)
**Loop** $L(s)=k/(s+1)^3$. No right-half-plane poles, so Theorem 10.1 applies.
1. Phase of $L(i\omega)$ is $-3\arctan\omega$. It equals $-180^\circ$ when $\arctan\omega=60^\circ$, i.e. $\omega_{pc}=\tan60^\circ=\sqrt3$.
2. Magnitude there: $|L|=k/(1+\omega^2)^{3/2}=k/4^{3/2}=k/8$. So the curve crosses the negative real axis at $-k/8$.
3. If $k/8<1$ the crossing lies between $-1$ and 0: no encirclement, stable. If $k/8>1$ the crossing is beyond $-1$: encirclement, unstable. Gain margin: $g_m=1/|L(i\omega_{pc})|=8/k$. For $k=3$: $g_m=8/3\approx2.67$.
4. Check with the characteristic polynomial $(s+1)^3+k=s^3+3s^2+3s+1+k$. For $k=8$ this is $s^3+3s^2+3s+9=(s+3)(s^2+3)$, with roots $\pm i\sqrt3$, so the loop oscillates at $\omega=\sqrt3$ exactly as predicted.
5. Phase margin for $k=3$: $|L|=1$ requires $(1+\omega^2)^{3/2}=3$, so $1+\omega^2=3^{2/3}\approx2.080$ and $\omega_{gc}\approx1.039$. Phase $=-3\arctan(1.039)\approx-3(46.1^\circ)=-138.3^\circ$. So $\varphi_m=180^\circ-138.3^\circ\approx41.7^\circ$.

For $k=3$, step 3 gives $g_m\approx2.67$ and step 5 gives $\varphi_m\approx41.7^\circ$, matching Example 10.7.

## Concepts
- [[loop-transfer-function]] (new) — $L=PC$, the transfer function around the broken loop (with sign for negative feedback); the object Nyquist analyses (p. 10-2)
- [[nyquist-criterion]] — stability from encirclements of $-1$ by the image of $L$ along the Nyquist contour; simplified (Thm 10.1) and general (Thm 10.3, $Z=N+P$) forms (p. 10-6, 10-12)
- [[critical-point]] (new) — the point $-1$ in the complex plane; oscillation condition $L(i\omega_0)=-1$ (p. 10-2, 10-3)
- [[winding-number]] (new) — net number of times a closed curve goes around a point; here counts encirclements of $-1$ (p. 10-6, 10-10)
- [[principle-of-variation-of-the-argument]] (new) — winding number of $f$ along $\Gamma$ equals zeros minus poles inside (Thm 10.2) (p. 10-10)
- [[conditional-stability]] (new) — a system stable only for gain in some range, so that raising gain can stabilise (p. 10-13, 10-14)
- [[stability]] — closed-loop poles in the open left half-plane; here tested through $L(i\omega)$ (p. 10-2)
- [[gain-margin]] (new) — $g_m=1/|L(i\omega_{pc})|$, the smallest gain multiplier causing instability (p. 10-15)
- [[phase-margin]] (new) — $\varphi_m=180^\circ+\angle L(i\omega_{gc})$ (p. 10-15)
- [[stability-margin]] (new) — shortest distance $s_m$ from the Nyquist curve to $-1$; equals $1/M_s$ (p. 10-14, 10-16)
- [[delay-margin]] (new) — smallest additional time delay that destabilises the loop (p. 10-17)
- [[delay-dead-time]] — a pure delay $e^{-s\tau}$ leaves gain unchanged and adds phase lag $\omega\tau$ (p. 10-4, 10-20)
- [[bode-plot]] — gain and phase against frequency; used to sketch Nyquist curves and read margins (p. 10-7, 10-16)
- [[minimum-phase-system]] (new) — no delay and no RHP poles/zeros (plus a growth condition); phase fixed by gain curve (Bode's relation (10.9)) (p. 10-19)
- [[inverse-response]] (new) — initial response in the wrong direction, typical of RHP zeros (p. 10-21)
- [[hinf-norm-system-gain]] (new) — $\|G\|_\infty=\sup_\omega|G(i\omega)|$ (SISO) or $\sup_\omega\bar\sigma(G(i\omega))$ (MIMO) as $L_2$ gain (p. 10-23)
- [[small-gain-theorem]] (new) — loop of two stable systems is stable if $\gamma_1\gamma_2<1$ (p. 10-24)
- [[passivity]] (new) — phase between input and output at most $90^\circ$ for all inputs (p. 10-24)
- [[circle-criterion]] (new) — Nyquist curve outside the circle with diameter $-1/k_{low}\le x\le-1/k_{high}$ (and the encirclement condition satisfied) for a sector-bounded nonlinearity (p. 10-24)
- [[describing-function]] (new) — complex first-harmonic gain $N(a)$ of a static nonlinearity; oscillation if $H(i\omega)N(a)=-1$ (p. 10-25)
- [[robustness]] — here expressed by margins: how much the system may deviate from the nominal model and remain stable (p. 10-17)

## Canonical instances
- [[dc-motor-with-sensing-delay]] (new) — delay turns a stable proportional loop into an oscillating, then unstable one (p. 10-3, 10-4)
- [[tcp-congestion-control]] — loop gain $\rho c^2(\tau_e^p)^2/(\pi N)<1$ condition; instability as link capacity grows (p. 10-8, 10-9)
- [[inverted-pendulum]] — PD control stable only for $k>0.5$ ($Z=N+P=0$) (p. 10-13)
- [[atomic-force-microscope-nanopositioner]] — integral control of a lightly damped resonance; $k_i=2\zeta\omega_0(1-s_m)$ (p. 10-17, 10-18)
- [[vehicle-steering]] — reverse driving gives a non-minimum-phase zero and inverse response (p. 10-20 to 10-22)
- [[relay-with-hysteresis]] — describing-function prediction of limit cycle amplitude and frequency (p. 10-26, 10-27)

## Bridges (candidates)
- [structural-analogy] Nyquist encirclement count $Z=N+P$ ↔ complex analysis: zeros-minus-poles via the argument principle — the criterion is an application of that theorem.
- [same-math] $\|G\|_\infty$ as system gain ↔ linear algebra: largest singular value $\bar\sigma(A)$ of a matrix — (10.15) applies the matrix definition (10.12) at each frequency and takes the supremum.
- [structural-analogy] Small-gain condition $\gamma_1\gamma_2<1$ ↔ geometric series: closed-loop gain $\gamma_1/(1-\gamma_1\gamma_2)$ has the form of a sum $\gamma_1\sum(\gamma_1\gamma_2)^n$ (the book does not say this).
- [structural-analogy] Minimum-phase gain–phase tie (Bode, (10.9)) ↔ causality: kernel-weighted relation between magnitude and phase (the book does not discuss the link).
- [metaphor] Delay-induced oscillation in a loop ↔ time-lagged feedback in other fields (e.g. congestion in networks): the same "returns in phase with gain ≥1" mechanism.

## Questions this raises
- How is the Nyquist curve of $L$ related to the closed-loop sensitivity peak $M_s$ (with $s_m=1/M_s$) and to robust control design (Chapter 13)?
- When does the approximation (10.9), $\arg G\approx\frac\pi2\,d\log|G|/d\log\omega$, hold well enough to design from the gain curve alone? (Exercise 10.10.)
- How reliable is describing-function analysis when higher harmonics are not small, and how can its predicted limit cycles be checked against simulation? (Exercise 10.14.)
- Which sensor or actuator changes remove right-half-plane zeros, and how much performance does a remaining RHP zero or pole cost (Chapter 14)?

## Exercises worth doing
- Ex. 10.3 (p. 10-28) — TCP loop $L=(k/s)e^{-s\tau}$: choose the gain from the measured delay to keep $s_m\ge0.6$ for all $\tau$ — difficulty: medium
- Ex. 10.4 (p. 10-29) — Nyquist plot of $ke^{-\sqrt s}$, find the $-180^\circ$ frequency and the critical gain (the exercise states $k=e^\pi$) — difficulty: medium
- Ex. 10.5 (p. 10-29) — gain, phase and stability margins as functions of $\zeta$ for a double integrator with PD control — difficulty: medium
- Ex. 10.9 (p. 10-29, 10-30) — Kalman's inequality for LQR and its consequence on the Nyquist curve (phase margin $>60^\circ$) — difficulty: hard
- Ex. 10.11 (p. 10-30) — Padé approximation: a long delay behaves like a small RHP zero — difficulty: medium
- Ex. 10.12 (p. 10-30) — inverse response of $G=6(-s+1)/(s^2+5s+6)$ versus the minimum-phase version — difficulty: easy

## Reading notes
- **Page numbers.** The text layer gives no printed page labels ("?"), but the page images show running headers "10-1" … "10-32". Citations use these: (p. 10-N). Offset: printed 10-N = pdf (N + 342), e.g. pdf 343 = 10-1. The last page (pdf 374 / 10-32) contains only a header.
- **Advanced-section markers.** A road-sign icon appears beside "The General Nyquist Criterion", "Formal proof", §10.5 and Exercise 10.8; the page text does not explain the icon.
- **Misprints and inconsistencies seen in the images.**
  - Example 10.1: the text gives the undelayed phase as 90° to 180°; the Bode plot (Fig. 10.3a) shows $-90^\circ$ to $-180^\circ$ (lag). It also says phase "increases" with $\tau$, where the lag increases.
  - Example 10.4: the text writes $\tilde G_{qp}$ where the figure and equations use $\tilde G_{pb}$. It gives $\omega_{pc}=\pi/(2\tau_e^p)$ although the delay in $L$ is $\tau_e^t$; the step seems to take $\tau_e^t\approx\tau_e^p$, which is not stated.
  - Eq. (10.3) discussion: denominator index "$\rho_m$" should be $\rho_n$.
  - Theorem 10.3 discussion: "unstable stable zeros" (should be "unstable zeros").
  - §10.3: the gain crossover frequency is defined as where "$L(i\omega_{pc})$" meets the unit half-circle (should be $L(i\omega_{gc})$); inequalities (10.7) cite Fig. 10.12, but the margins are drawn in Fig. 10.11.
  - Example 10.9: Fig. 10.14 uses $\zeta=0.01$, $k_i=0.008$ while the text suggests $\zeta=0.1$ as typical.
  - Example 10.11: the zero of $P(s)=(av_0s+v_0^2)/(bs^2)$ is at $s=-v_0/a$, but the text says $v_0/a$; the left/right half-plane statements are consistent with $-v_0/a$.
  - §10.5: $A^*A$ is called "symmetric" (it is Hermitian, since $A$ is complex).
  - Example 10.12: the text uses $b=1$, $c=0.5$ and $H=2/(s+1)^4$, while the Fig. 10.20 caption says $H=(s+1)^{-4}$, $b=3$, $c=1$.
  - Exercise 10.15: the saturation definition prints "$-1$ if $x\le1$" (probably $x\le-1$), and $N(a)$ is written in terms of $x$ rather than $a$.
- Page pdf 359 (10-17) text layer shows Example 10.9's $s(s+2\zeta\omega_0s+\omega_0^2)$ with the square on the first $s$ displaced; read as $s^2$.
- Chapter 10 exercises 10.1–10.15 are printed; only a selection is listed above.
