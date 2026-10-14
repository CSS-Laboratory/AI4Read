---
id: astrom-2021-feedbacksystems/ch09-transfer-p1
work: astrom-2021-feedbacksystems
unit: "9 Transfer Functions (part 1/2): sections 9.1–9.4 (to the end of 'Algebraic Loops')"
pages: 9-1 to 9-22 (pdf 299–320)
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Transfer Functions (part 1): from exponential signals to block-diagram algebra

## L0 — One line
A linear time-invariant system's response to the exponential input $e^{st}$ contains the pure exponential part $G(s)e^{st}$, and this single function $G(s)$ lets you compute with systems and block diagrams by algebra.

## L1 — The gist (≤ 120 words)
The unit asks how to describe the input/output behaviour of a linear time-invariant system without tracking its internal state. The answer is the transfer function $G(s)$, the coefficient of $e^{st}$ in the pure exponential part of the response. It is $C(sI-A)^{-1}B+D$ for a state-space model, a ratio of polynomials for a differential equation, and a non-rational function for delays and heat flow. Laplace transforms give the same $G(s)$. Series, parallel and feedback connections then become products, sums and $G_1/(1+G_1G_2)$. This matters because complex feedback loops reduce to algebra. A hidden-state caveat appears: pole/zero cancellation is related to lack of reachability and observability, so $G$ shows only part of the dynamics.

**Prerequisites:** complex numbers and Euler's formula; state-space models $\dot x=Ax+Bu$; matrix inverse and exponential; reachability and observability; poles and zeros (roots of the denominator and numerator of a rational function); the Kalman decomposition (splitting a system into reachable/observable parts); basic integration by parts.

## L2 — Key ideas (5–10 bullets)
- **Exponential signals are the test input.** For $u=e^{st}$ the output contains a pure exponential $G(s)e^{st}$; $G$ generalises the frequency response $G(i\omega)$ to complex $s$ (p. 9-2, 9-4, 9-5).
- **Formulas for $G$.** $G(s)=C(sI-A)^{-1}B+D$; for the ODE (9.13) $G=b(s)/a(s)$, readable by inspection from the coefficients (p. 9-4, 9-8).
- **Transfer functions need not be rational.** A delay gives $e^{-s\tau}$; heat flow in a rod gives $e^{-\sqrt s}$ (p. 9-11, 9-12).
- **$G$ is invariant to state coordinates but not unique as a realization.** A coordinate change $T$ gives another realization; a minimal one has at most $n$ states, possibly fewer if poles and zeros cancel (p. 9-12, 9-13).
- **Cancellation is related to lack of reachability and observability.** $G$ only represents the reachable and observable part $\Sigma_{ro}$ of the Kalman decomposition (p. 9-13).
- **Laplace transforms give the same $G$.** Integration becomes division by $s$, convolution becomes a product, and $Y=HU$ (p. 9-15, 9-16).
- **Block-diagram algebra.** Series gives $G_2G_1$, parallel gives $G_1+G_2$, feedback gives $G_1/(1+G_1G_2)$; error transfer functions follow (p. 9-17, 9-19).
- **Observer-based controllers can be written as transfer functions,** but should be implemented as one order-$n$ system (p. 9-20, 9-22).
- **Algebraic loops** (closed loops of blocks that all have a direct connection from input to output) mean the closed-loop equations cannot be formed by simple substitution; an algebraic equation must be solved (p. 9-22).

## L3 — Walkthrough

### Opening and 9.1 Frequency Domain Modeling (p. 9-1 – 9-3)
- Bode's epigraph: regulators are often second- to fourth-order, while a feedback amplifier he designed would have had a differential-equation set of order 55 — "It turned out to be 55." (p. 9-1).
- Figure 9.1 (repeated as 9.6): process $P$, feedback controller $C$, reference shaping $F$; signals $r, e, u, v, \mu, \eta, w, y$. $v$ is the load disturbance and $w$ the measurement noise (p. 9-2).
- A periodic input is a sum of sines and cosines at multiples $k\omega_f$ of the fundamental frequency $\omega_f$. In steady state each component gets a gain and phase shift from the frequency response
$$G(i\omega)=C(i\omega I-A)^{-1}B+D,\qquad \omega=k\omega_f. \tag{9.1}$$
 Superposition then gives the steady-state response to any periodic signal (p. 9-2).
- The transfer function generalises this to inputs $u=e^{st}$. It has precisely the form of (9.1), since (9.1) came from writing sinusoids as complex exponentials. It can also be introduced as the ratio of Laplace transforms of output and input with zero initial state, but one need not understand Laplace transforms to use it (p. 9-2).
- *Frequency domain modeling* = modeling by response to sinusoids and exponentials, with generalised frequency $s$ in place of time $t$. The transfer function is a complete representation of a linear system in the frequency domain (p. 9-2).
- Uses mentioned: convenient manipulation of complex feedback systems; Bode and Nyquist plots; expressing modeling errors (sensitivity to process variations, Chapter 13); analysing static approximations of dynamics or low-order approximations of high-order models; concepts of degree of stability (p. 9-2, 9-3).
- Frequency-domain analysis applies primarily to linear systems. Gain and phase can be generalised to nonlinear systems; the propagation of sinusoids can approximately be captured by an analogue of the frequency response, the *describing function* (Section 10.5, not in this part) (p. 9-3).

### 9.2 Determining the Transfer Function (p. 9-3 – 9-13)
The response of a linear system has two parts: initial-condition response and forced response; the transfer function characterises the forced response (p. 9-3).

**Transmission of exponential signals.**
- Exponential signal: $e^{st}$ with $s=\sigma+i\omega$ complex. A constant is $e^{\alpha t}$ with $\alpha=0$. By Euler's formula
$$e^{(\sigma+i\omega)t}=e^{\sigma t}e^{i\omega t}=e^{\sigma t}(\cos\omega t+i\sin\omega t),$$
 with $\sigma<0$ giving the decay rate (p. 9-3). Figure 9.2 shows $s=0,-1,1,i,-0.2+i,0.2+i$: negative real part decays, positive real part grows (p. 9-4). Complex-valued signals are allowed in derivations; in practice real combinations are used (p. 9-3).
- For $\dot x=Ax+Bu,\ y=Cx+Du$ (9.2), take $u=e^{st}$ with $s\notin\lambda(A)$ ($\lambda(A)$ = set of eigenvalues). Then
$$x(t)=e^{At}x(0)+\int_0^t e^{A(t-\tau)}Be^{s\tau}d\tau=e^{At}x(0)+e^{At}(sI-A)^{-1}\bigl(e^{(sI-A)t}-I\bigr)B.$$
- The output is
$$\begin{aligned}y(t)&=Cx(t)+Du(t)\\&=Ce^{At}x(0)+\bigl(C(sI-A)^{-1}B+D\bigr)e^{st}-Ce^{At}(sI-A)^{-1}B\\&=Ce^{At}\bigl(x(0)-(sI-A)^{-1}B\bigr)+\bigl(C(sI-A)^{-1}B+D\bigr)e^{st}.\end{aligned}\tag{9.3}$$
 The first line splits into initial-condition response ($Ce^{At}x(0)$) and input response; the last line splits into the transient response and the pure exponential response $y_p$ (p. 9-4).
- The transfer function is the coefficient of $e^{st}$:
$$G(s)=C(sI-A)^{-1}B+D. \tag{9.4}$$
 The response (9.3) is singular at eigenvalues of $A$ (where $sI-A$ is not invertible), which is why $s\notin\lambda(A)$ was assumed; $G$ can be extended to all $s$ by analytic continuation (p. 9-4, 9-5).
- Structure: $e^{At}$ is expressed via eigenvalues (Jordan form for repeated ones), so the transient is a combination of terms $p_j(t)e^{\lambda_jt}$ with $p_j$ a polynomial of degree less than the multiplicity of $\lambda_j$ (Exercise 9.1). The pure exponential solution is
$$y_p(t)=\bigl(C(sI-A)^{-1}B+D\bigr)e^{st}=G(s)e^{st}, \tag{9.5}$$
 a particular solution of (9.2). The output equals $y_p$ if the initial condition is chosen as
$$x(0)=(sI-A)^{-1}B. \tag{9.6}$$
 If the system is asymptotically stable ($e^{At}\to0$) and the input is a constant or $e^{i\omega t}$, the response converges to a constant or sinusoidal steady state (p. 9-5).
- Let $\mathcal E$ be the class of time functions built from combinations of $X(s)e^{st}$. For $u\in\mathcal E$ there is a particular solution $y\in\mathcal E$; it is the actual response if the initial condition is (9.6). Notation:
$$y=G_{yu}u, \tag{9.7}$$
 which assumes combinations of exponential signals. The subscripts are often dropped (p. 9-5).

*Intuition note.* The part of the response that has the shape of the input exponential is just the input multiplied by the number $G(s)$. So $G(s)$ is a "multiplication factor per exponential", and the rest of the response (the transient) dies out if the system is asymptotically stable.

**Example 9.1 Damped oscillator.** $\dot x=\begin{pmatrix}0&\omega_0\\-\omega_0&-2\zeta\omega_0\end{pmatrix}x+\begin{pmatrix}0\\k\omega_0\end{pmatrix}u,\ y=\begin{pmatrix}1&0\end{pmatrix}x$ (9.8); asymptotically stable if $\zeta>0$ (p. 9-5, 9-6). (added step) With $\det(sI-A)=s^2+2\zeta\omega_0s+\omega_0^2$:
$$G_{yu}(s)=C(sI-A)^{-1}B=\frac{k\omega_0^2}{s^2+2\zeta\omega_0s+\omega_0^2}. \tag{9.9}$$
- Step input: $s=0$ gives $y=G_{yu}(0)u=k$ for $u=1$ (p. 9-6).
- Sinusoid: $\sin\omega t=\tfrac12(ie^{-i\omega t}-ie^{i\omega t})$, so $y=\tfrac12\bigl(iG(-i\omega)e^{-i\omega t}-iG(i\omega)e^{i\omega t}\bigr)$. Write $G(i\omega)=\dfrac{k\omega_0^2}{-\omega^2+(2\zeta\omega_0\omega)i+\omega_0^2}=Me^{i\theta}$ with
$$M=\frac{k\omega_0^2}{\sqrt{(\omega_0^2-\omega^2)^2+(2\zeta\omega_0\omega)^2}},\qquad \frac{\sin\theta}{\cos\theta}=\frac{-2\zeta\omega_0\omega}{\omega_0^2-\omega^2}.$$
 Since $G(-i\omega)=G^*(i\omega)=Me^{-i\theta}$, we get $y=M\cdot\tfrac12\bigl(ie^{-i(\omega t+\theta)}-ie^{i(\omega t+\theta)}\bigr)=M\sin(\omega t+\theta)$ (p. 9-6). Other inputs: write them as combinations of exponentials and use linearity.

**Example 9.2 Operational amplifier circuit.** Section 4.3's static model $v_{out}=-kv$ is replaced by $v_{out}=-Gv$ with
$$G(s)=\frac{ak}{s+a}, \tag{9.10}$$
a first-order system with time constant $1/a$. $k$ = open loop gain; $ak$ = gain-bandwidth product; typical $k=10^7$, $ak=10^7$–$10^9$ rad/s (p. 9-6, 9-7).
- Circuit (Figure 9.3a, resistors $R_1,R_2$): if $v_1=e^{st}$, there are solutions in which all signals are in $\mathcal E$ (all circuit elements are linear). With zero current into the amplifier, $\frac{v_1-v}{R_1}=\frac{v-v_2}{R_2}$, i.e.
$$(R_1+R_2)v=R_2v_1+R_1v_2,\qquad v_2=-Gv,\qquad v,v_1,v_2\in\mathcal E. \tag{9.11}$$
- Eliminating $v$:
$$v_2=\frac{-R_2G}{R_1+R_2+R_1G}v_1=\frac{-R_2ak}{R_1ak+(R_1+R_2)(s+a)}v_1,$$
$$G_{v_2v_1}=\frac{-R_2ak}{R_1ak+(R_1+R_2)(s+a)}. \tag{9.12}$$
- Low-frequency gain ($s=0$): $G_{v_2v_1}(0)=\dfrac{-kR_2}{(k+1)R_1+R_2}\approx-\dfrac{R_2}{R_1}$, the result of (4.12). Bandwidth: $\omega_b=a\dfrac{R_1(k+1)+R_2}{R_1+R_2}\approx a\dfrac{R_1k}{R_2}$ for $k\gg1$, where the approximation holds for $R_2/R_1\gg1$. At high frequency the gain drops as $R_2ak/(\omega(R_1+R_2))$. Figure 9.3b uses $k=10^7$, $a=10$ rad/s, $R_2=10^6\,\Omega$, $R_1=1,10^2,10^4,10^6\,\Omega$ (p. 9-7, 9-8).
- The shortcut: work directly with $v$ assumed exponential instead of writing $V(s)e^{st}$. With transfer functions the analysis is as easy as with static systems; resistances become impedances (p. 9-8).

**Transfer functions for linear differential equations.** For
$$\frac{d^ny}{dt^n}+a_1\frac{d^{n-1}y}{dt^{n-1}}+\dots+a_ny=b_0\frac{d^mu}{dt^m}+b_1\frac{d^{m-1}u}{dt^{m-1}}+\dots+b_mu \tag{9.13}$$
(input derivatives allowed), let $u=e^{st}$ and $y=y_0e^{st}$. Then $(s^n+a_1s^{n-1}+\dots+a_n)y_0e^{st}=(b_0s^m+\dots+b_m)e^{st}$. Define
$$a(s)=s^n+a_1s^{n-1}+\dots+a_n,\qquad b(s)=b_0s^m+b_1s^{m-1}+\dots+b_m. \tag{9.14}$$
$a(s)$ is the characteristic polynomial. If $a(s)\ne0$,
$$y(t)=y_0e^{st}=\frac{b(s)}{a(s)}e^{st},\tag{9.15}$$
$$G(s)=\frac{b(s)}{a(s)}=\frac{b_0s^m+b_1s^{m-1}+\dots+b_m}{s^n+a_1s^{n-1}+\dots+a_n}. \tag{9.16}$$
$G$ can be written by inspection from the coefficients. Poles and zeros are the roots of $a(s)$ and $b(s)$; system properties are determined by them (explored in Section 9.5, in part 2) (p. 9-8, 9-9).

**Example 9.3 Electrical circuit elements** (current in, voltage out; generalised impedance $Z(s)$). Resistor $V=IR$: $Z=R$. Inductor $L\,dI/dt=V$: with $I=e^{st}$, $V=Lse^{st}$, so $Z=Ls$. Capacitor $C\,dV/dt=I$: $Z=1/(Cs)$. Circuits can then be analysed algebraically like resistor networks (p. 9-9).

**Example 9.4 Vibration damper** (Figure 9.4: mass $m_1$ with damper $c_1$, spring $k_1$, auxiliary mass $m_2$ on spring $k_2$; force $F$ on $m_1$). Newton: $m_1\ddot q_1+c_1\dot q_1+k_1q_1+k_2(q_1-q_2)=F$, $m_2\ddot q_2+k_2(q_2-q_1)=0$. Exponential solutions:
$$(m_1s^2+c_1s+k_1)q_1+k_2(q_1-q_2)=F,\qquad m_2s^2q_2+k_2(q_2-q_1)=0.\tag{9.17}$$
From the second, $q_2=\frac{k_2}{m_2s^2+k_2}q_1$. Inserting: $(m_1s^2+c_1s+k_1)q_1+k_2\bigl(1-\frac{k_2}{m_2s^2+k_2}\bigr)q_1=F$, hence $\bigl((m_1s^2+c_1s+k_1+k_2)(m_2s^2+k_2)-k_2^2\bigr)q_1=(m_2s^2+k_2)F$, and
$$G_{q_1F}(s)=\frac{m_2s^2+k_2}{m_1m_2s^4+m_2c_1s^3+(m_1k_2+m_2(k_1+k_2))s^2+k_2c_1s+k_1k_2}.$$
It has zeros at $s=\pm i\sqrt{k_2/m_2}$, so sinusoids at that frequency are blocked (discussed in Section 9.5). Table 9.1 lists common transfer functions (p. 9-9, 9-10, 9-11): integrator $1/s$; differentiator $s$; first-order $1/(s+a)$; double integrator $1/s^2$; damped oscillator $1/(s^2+2\zeta\omega_0s+\omega_0^2)$; state space $C(sI-A)^{-1}B+D$; PID $k_p+k_ds+k_i/s$; delay $e^{-\tau s}$ (p. 9-11). Multi-input multi-output systems have similar forms (p. 9-10).

**Example 9.5 Time delay.** $y(t)=u(t-\tau)$ (9.18). With $u=e^{st}$: $y=e^{s(t-\tau)}=e^{-s\tau}e^{st}$, so $G(s)=e^{-s\tau}$, not a rational function (p. 9-10, 9-11).

**Example 9.6 Heat propagation** in a semi-infinite rod, input = end temperature, output = temperature at $x=1$:
$$\frac{\partial\theta}{\partial t}=\frac{\partial^2\theta}{\partial x^2},\quad y(t)=\theta(1,t),\quad\theta(0,t)=u(t). \tag{9.19}$$
Try $\theta(x,t)=\psi(x)e^{st}$: $s\psi=\psi''$, $\psi(0)=1$, so $\psi(x)=Ae^{x\sqrt s}+Be^{-x\sqrt s}$. Boundedness gives $A=0$; the boundary condition gives $B=1$. Then $y=\psi(1)e^{st}=e^{-\sqrt s}u$, so $G(s)=e^{-\sqrt s}$, again not rational (p. 9-11, 9-12).

**State space realizations.**
- Realization problem: given $G(s)$, find $(A,B,C,D)$ with $G(s)=C(sI-A)^{-1}B+D$; such a system is a (state space) realization (p. 9-12).
- Coordinate change $z=Tx$, $T$ nonsingular: $\dot z=TAT^{-1}z+TBu$, $y=CT^{-1}z+Du$, i.e.
$$\tilde A=TAT^{-1},\quad\tilde B=TB,\quad\tilde C=CT^{-1}. \tag{9.20}$$
$$\tilde G(s)=CT^{-1}(sI-TAT^{-1})^{-1}TB+D=C\bigl(T^{-1}(sI-TAT^{-1})T\bigr)^{-1}B+D=C(sI-A)^{-1}B+D=G(s).$$
 So $G$ is invariant to state coordinates (p. 9-12).
- Hence a realization is never unique, but its dimension is unchanged by $T$. A *minimal realization* has as few states as possible. For $G=b/a$ with $\deg a=n$ there is always a realization with $n$ states (reachable canonical form (7.6)); a minimal realization has at most $n$ states, but the number may be lower if there are pole/zero cancellations (p. 9-13).

**Example 9.7 Cancellation.** $A=\begin{pmatrix}-3&1\\-2&0\end{pmatrix}$, $B=\begin{pmatrix}1\\1\end{pmatrix}$, $C=\begin{pmatrix}1&0\end{pmatrix}$:
$$G(s)=\frac{1}{s^2+3s+2}\begin{pmatrix}1&0\end{pmatrix}\begin{pmatrix}s&1\\-2&s+3\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\frac{s+1}{s^2+3s+2}=\frac{s+1}{(s+1)(s+2)}=\frac1{s+2}.$$
A second-order system gives a first-order $G$. The reachability matrix $W_r=\begin{pmatrix}B&AB\end{pmatrix}=\begin{pmatrix}1&-2\\1&-2\end{pmatrix}$ has rank 1, so the system is not reachable. Per Section 8.3, $G$ is given by the reachable and observable subsystem $\Sigma_{ro}$ of the Kalman decomposition, here first order (p. 9-13).
- General statement: by (8.20) the input/output response is determined solely by $\Sigma_{ro}$; when a system lacks reachability and observability, this shows up as cancellation of poles and zeros in the transfer function computed from the full system matrices. Cancellation was long controversial (rule: do not cancel factors with roots in the right half-plane); Kalman's decomposition clarifies that $G$ represents only part of the dynamics. More in Section 9.5 (p. 9-13).
- MIMO: with $p$ inputs and $q$ outputs, $G:\mathbb C\to\mathbb C^{q\times p}$; the techniques generalise but minimal realization becomes substantially more complicated (p. 9-13, 9-14).

*Intuition note.* The transfer function sees only what the input can reach and the output can see. A hidden mode that fails either test leaves no trace in $G$, which is why $(s+1)$ cancelled.

### 9.3 Laplace Transforms (p. 9-14 – 9-16)
Optional section; the author says students unfamiliar with Laplace transforms can safely skip it. Today responses are computed by simulation, but Laplace transforms still give insight (p. 9-14).
- Definition, for integrable $f:\mathbb R_+\to\mathbb R$ growing no faster than $e^{s_0t}$:
$$F(s)=\int_0^\infty e^{-st}f(t)\,dt,\qquad \mathrm{Re}\,s>s_0. \tag{9.21}$$
 Table 9.2: step $1/s$; impulse $1$; $\sin at\to a/(s^2+a^2)$; $\cos at\to s/(s^2+a^2)$; $e^{-\alpha t}\sin at\to a/((s+\alpha)^2+a^2)$; $e^{-\alpha t}\cos at\to(s+\alpha)/((s+\alpha)^2+a^2)$ (p. 9-14).
- Linearity: $\mathcal L(af+bg)=a\mathcal Lf+b\mathcal Lg$ (9.22) (p. 9-14).
- Integral: by integration by parts,
$$\mathcal L\!\int_0^tf(\tau)d\tau=\int_0^\infty e^{-st}\Bigl(\int_0^tf\Bigr)dt=-\frac{e^{-st}}{s}\int_0^tf\Big|_0^\infty+\int_0^\infty\frac{e^{-s\tau}}{s}f(\tau)d\tau=\frac1s\int_0^\infty e^{-s\tau}f(\tau)d\tau,$$
$$\mathcal L\!\int_0^tf(\tau)d\tau=\frac1s\mathcal Lf=\frac1sF(s). \tag{9.23}$$
 (added step: the boundary term vanishes because the inner integral is 0 at $t=0$ and $e^{-st}$ decays for $\mathrm{Re}\,s$ large enough.) Integration = division by $s$ (p. 9-15).
- Derivative:
$$\mathcal L\frac{df}{dt}=\int_0^\infty e^{-st}f'(t)dt=e^{-st}f(t)\Big|_0^\infty+s\int_0^\infty e^{-st}f(t)dt=-f(0)+s\mathcal Lf,$$
$$\mathcal L\frac{df}{dt}=s\mathcal Lf-f(0)=sF(s)-f(0). \tag{9.24}$$
 Differentiation corresponds to multiplication by $s$ when $f(0)=0$; in general the term $-f(0)$ appears (p. 9-15).
- Using Laplace transforms, $G$ is defined as the ratio of transforms of output to input with zero initial conditions. (The page text says "input and the output", reversed; see Reading notes.) (p. 9-15)

**Example 9.8.** Transform (9.2): $sX(s)-x(0)=AX(s)+BU(s)$, $Y(s)=CX(s)+DU(s)$. Eliminating $X$:
$$X(s)=(sI-A)^{-1}x(0)+(sI-A)^{-1}BU(s). \tag{9.25}$$
With $x(0)=0$: $Y=\bigl(C(sI-A)^{-1}B+D\bigr)U$, so $G=C(sI-A)^{-1}B+D$, matching (9.4) (p. 9-15).

**Example 9.9 Impulse response.** With zero initial state, $y(t)=\int_0^\infty h(t-\tau)u(\tau)d\tau$, $h$ causal ($h(t')=0$ for $t'<0$). Then
$$Y(s)=\int_0^\infty e^{-st}\!\int_0^\infty h(t-\tau)u(\tau)d\tau dt=\int_0^\infty\!\!\int_0^t e^{-s(t-\tau)}e^{-s\tau}h(t-\tau)u(\tau)d\tau dt=\int_0^\infty\!\!\int_0^\infty e^{-st'}h(t')e^{-s\tau}u(\tau)d\tau dt'=H(s)U(s).$$
The transform of a convolution is the product of the transforms; this simplicity is one reason Laplace transforms were popular in engineering (p. 9-16).
- Initial value theorem: $\lim_{t\to0}f(t)=\lim_{s\to\infty}sF(s)$. With a step input ($U=1/s$): $u(0)=\lim_{s\to\infty}s\,G_{ur}(s)\frac1s=G_{ur}(\infty)$. Final value theorem: $\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$, giving $\lim_{t\to\infty}y(t)=G_{yr}(0)$ for a step $r$. The book states these without conditions on these pages (p. 9-16).

### 9.4 Block Diagrams and Transfer Functions (p. 9-17 – 9-22)
All signals are assumed in $\mathcal E$, $y=Gu$; outputs from several inputs follow by superposition (p. 9-17).
- **Series** (Figure 9.5a): $y=G_2(G_1u)=(G_2G_1)u$ (9.26), so $G=G_2G_1$. The order is the reverse of the left-to-right diagram, which matters if $G_1$ or $G_2$ is vector-valued (p. 9-17).
- **Parallel** (9.5b): $y=G_1u+G_2u$, so $G=G_1+G_2$ (p. 9-17).
- **Feedback** (9.5c): $y=G_1e,\ e=u-G_2y$ (9.27). Then $(1+G_1G_2)y=G_1u$ and
$$G=\frac{G_1}{1+G_1G_2}. \tag{9.28}$$
 These three rules are the basis for more complicated systems (p. 9-18).

*Intuition note.* In the feedback rule, $G_1G_2$ is the gain once around the loop. The closed loop is the forward gain divided by one plus the loop gain.

**Control system transfer functions** (Figure 9.6: $F$, $C$, $P$; inputs $r$, $v$, $w$). Relations: $e=Fr-y$, $y=w+\eta$, $\eta=P(v+u)$, $u=Ce$. Then $e=Fr-(w+P(v+Ce))=Fr-w-Pv-PCe$, and solving for $e$:
$$e=\frac{F}{1+PC}r-\frac1{1+PC}w-\frac P{1+PC}v=G_{er}r+G_{ew}w+G_{ev}v, \tag{9.29}$$
$$G_{er}=\frac F{1+PC},\quad G_{ew}=\frac{-1}{1+PC},\quad G_{ev}=\frac{-P}{1+PC}. \tag{9.30}$$
The error is a sum of three terms; superposition gives the same result. By block manipulation (Figure 9.7: merge $P,C$; replace the loop; multiply in series),
$$G_{yr}=\frac{PCF}{1+PC}. \tag{9.31}$$
Other transfer functions: Exercise 9.10. General idea: start from the variable of interest and trace backwards around the loop. All terms in (9.30) share the denominator; numerators are the products of blocks on the direct path from input to output. For multiple loops this inspection rule can be tricky (p. 9-19, 9-20).

**State space controller with observer.** Process $\dot x=Ax+Bu,\ y=Cx$; controller $u=-K\hat x+k_fr$ (9.32); observer $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)$ (9.33). The controller has output $u$ and inputs $r$, $y$:
$$u=G_{ur}r+G_{uy}y. \tag{9.34}$$
$G_{uy}$ is the feedback action and $G_{ur}$ the feedforward action. They are called *open loop* transfer functions because they ignore the process dynamics (cutting the loop). Rewrite (9.33) as
$$\dot{\hat x}=(A-BK-LC)\hat x+Bk_fr+Ly. \tag{9.35}$$
With exponential signals: $(sI-(A-BK-LC))\hat x=Bk_fr+Ly$, so
$$G_{ur}=k_f-K(sI-A+BK+LC)^{-1}Bk_f,\qquad G_{uy}=-K(sI-A+BK+LC)^{-1}L. \tag{9.36}$$
(p. 9-20)

**Example 9.10 Vehicle steering** (Figure 9.8; model from Example 6.13, controller and estimator from Examples 7.4 and 8.3). The estimator is split into $G_{\hat xu}$ and $G_{\hat xy}$:
$$G_{\hat xu}=\begin{pmatrix}\frac{\gamma s+1}{s^2+l_1s+l_2}\\[2pt]\frac{s+l_1-\gamma l_2}{s^2+l_1s+l_2}\end{pmatrix},\qquad G_{\hat xy}=\begin{pmatrix}\frac{l_1s+l_2}{s^2+l_1s+l_2}\\[2pt]\frac{l_2s}{s^2+l_1s+l_2}\end{pmatrix},$$
with observer gains $l_1,l_2$ and $\gamma$ the scaled position of the centre of mass from the rear wheels. With state feedback gains $k_1,k_2$ and feedforward gain $k_f$:
$$G_{ur}=\frac{k_f}{1+KG_{\hat xu}}=\frac{k_f(s^2+l_1s+l_2)}{s^2+s(\gamma k_1+k_2+l_1)+k_1+l_2+k_2l_1-\gamma k_2l_2},$$
$$G_{uy}=\frac{-KG_{\hat xy}}{1+KG_{\hat xu}}=\frac{s(k_1l_1+k_2l_2)+k_1l_2}{s^2+s(\gamma k_1+k_2+l_1)+k_1+l_2+k_2l_1-\gamma k_2l_2}.$$
Process: $P(s)=\begin{pmatrix}1&0\end{pmatrix}\begin{pmatrix}s&-1\\0&s\end{pmatrix}^{-1}\begin{pmatrix}\gamma\\1\end{pmatrix}=\dfrac{\gamma s+1}{s^2}$. Closed loop:
$$G_{yr}=\frac{P\,G_{ur}}{1-P\,G_{uy}}=\frac{k_f(\gamma s+1)}{s^2+(k_1\gamma+k_2)s+k_1}.$$
The source explains the unusual minus sign by saying that $G_{ur}$ is in the feedback path and incorporates the $-1$ gain element (p. 9-22); the term in that denominator is $G_{uy}$ (see Reading notes).
- The observer gains $l_1,l_2$ do not appear in $G_{yr}$; this is true in general (Figure 8.9b, Section 8.3). An observer-based controller should be implemented as the order-$n$ multivariable system (9.35), not as two separate transfer functions (9.34): that would give order $2n$ and unobservable modes (p. 9-22).

**Algebraic loops.** The simple procedure of forming the closed-loop differential equations by substitution cannot be used when a closed loop contains only subsystems with direct input-to-output connection (an *algebraic loop*). For $\dot x=f(x,u)$, $y=h(x)$ (9.37) with $u=-ky$ there is no direct term, so $\dot x=f(x,-ky),\ y=h(x)$ is obtained by substitution (easy to automate). If $y=h(x,u)$, then $y=h(x,-ky)$ must be solved for $y=\alpha(x)$ to get a differential equation for $x$, "which in general is a complicated task" (p. 9-22).

## Toy example (ours, not from the text)
System $\dot y+2y=u$. By inspection from (9.16): $a(s)=s+2$, $b(s)=1$, so $G(s)=1/(s+2)$.
- Check with $u=e^{-t}$ ($s=-1$): $G(-1)=1/(-1+2)=1$, so $y_p=e^{-t}$. Then $\dot y_p+2y_p=-e^{-t}+2e^{-t}=e^{-t}=u$ ✓.
- Step input ($s=0$): $G(0)=1/2$, so $y\to0.5$.
- Sinusoid $u=\sin t$ ($\omega=1$): $G(i)=1/(2+i)$. $M=1/\sqrt{4+1}=1/\sqrt5\approx0.447$; $\theta=-\arctan(1/2)\approx-26.6^\circ$.
- Feedback rule (9.28) with $G_1=1/(s+2)$, $G_2=3$: $G=\dfrac{1/(s+2)}{1+3/(s+2)}=\dfrac1{s+2+3}=\dfrac1{s+5}$. Direct check: $\dot y+2y=u-3y\Rightarrow\dot y+5y=u$, $G=1/(s+5)$ ✓. The steady step gain falls from $1/2$ to $1/5$.

## Concepts
- [[transfer-function]] — coefficient of $e^{st}$ in the pure exponential response; $C(sI-A)^{-1}B+D$ for state space, $b(s)/a(s)$ for ODEs (p. 9-4, 9-8)
- [[exponential-signal]] (new) — $e^{st}$ with complex $s$; includes constants, damped and growing oscillations (p. 9-3)
- [[frequency-domain-modeling]] (new) — describing a system by response to sinusoids/exponentials, using $s$ instead of $t$ (p. 9-2)
- [[state-space-model]] — $\dot x=Ax+Bu,\ y=Cx+Du$ (9.2), the starting point for deriving $G$ (p. 9-3)
- [[poles-and-zeros]] (new) — roots of $a(s)$ and $b(s)$ in $G=b/a$ (p. 9-9)
- [[realization]] (new) — a state-space system $(A,B,C,D)$ with $G(s)=C(sI-A)^{-1}B+D$; not unique; minimal has fewest states (p. 9-12, 9-13)
- [[pole-zero-cancellation]] (new) — common factors in $b/a$, related to lack of reachability and observability (p. 9-13)
- [[controllability]] — here called reachability; its rank test appears in Example 9.7 (p. 9-13)
- [[observability]] — with reachability determines the part $\Sigma_{ro}$ that $G$ represents (p. 9-13)
- [[laplace-transform]] (new) — $F(s)=\int_0^\infty e^{-st}f(t)dt$; integration $\to$ division by $s$; convolution $\to$ product (p. 9-14 – 9-16)
- [[block-diagram-algebra]] (new) — series $G_2G_1$, parallel $G_1+G_2$, feedback $G_1/(1+G_1G_2)$ (p. 9-17, 9-18)
- [[generalized-impedance]] (new) — transfer function from current to voltage: $R$, $Ls$, $1/(Cs)$ (p. 9-9)
- [[observer]] — state estimator (9.33), combined into a controller transfer function (p. 9-20)
- [[feedforward]] — $F$ in Figure 9.6 and $G_{ur}$ (p. 9-18, 9-20)
- [[disturbance-and-noise]] — load disturbance $v$ and measurement noise $w$ as inputs to $e$ (p. 9-18, 9-19)
- [[delay]] — $y(t)=u(t-\tau)$, $G=e^{-s\tau}$ (p. 9-11)
- [[algebraic-loop]] (new) — closed loop of blocks all with direct input-output connection (p. 9-22)

## Canonical instances
- [[damped-oscillator]] — $G=k\omega_0^2/(s^2+2\zeta\omega_0s+\omega_0^2)$; gain $M$ and phase $\theta$ from $G(i\omega)$ (p. 9-5, 9-6)
- [[op-amp-feedback-circuit]] — dynamic op amp gives closed-loop $G$, gain $\approx-R_2/R_1$, bandwidth $\approx aR_1k/R_2$ (p. 9-6 – 9-8)
- [[electrical-impedances]] — $R$, $Ls$, $1/(Cs)$ (p. 9-9)
- [[vibration-damper]] — zero at $\pm i\sqrt{k_2/m_2}$ blocks that frequency (p. 9-9, 9-10)
- [[time-delay-system]] — non-rational $e^{-s\tau}$ (p. 9-11)
- [[heat-propagation-rod]] — $G=e^{-\sqrt s}$ (p. 9-11, 9-12)
- [[vehicle-steering]] — observer-based controller as transfer functions; $G_{yr}$ independent of $l_1,l_2$ (p. 9-21, 9-22)

## Bridges (candidates)
- [same-math] Laplace transform of a convolution is a product ($Y=HU$) ↔ probability: the transform of a density of a sum of independent variables is the product of transforms — same convolution theorem.
- [structural-analogy] $e^{st}$ passes through an LTI system multiplied by $G(s)$ ↔ linear algebra: an eigenvector is scaled by its eigenvalue — exponentials act like eigenfunctions.
- [structural-analogy] Generalised impedance $Z(s)$ with algebraic circuit analysis ↔ resistor networks: same series/parallel rules with $Z$ replacing $R$.
- [structural-analogy] Feedback rule $G_1/(1+G_1G_2)$ ↔ economics/biology models of reinforcing and balancing loops: forward gain divided by one plus loop gain (a loop sign of $-1$ is built into the rule).

## Questions this raises
- What exactly do poles and zeros tell us about stability and about blocked frequencies (promised in Section 9.5)?
- How does the Bode plot display $|G(i\omega)|$ and phase, and what does it reveal about feedback design?
- If a cancelled factor lies in the right half-plane, what goes wrong in closed loop, and how does that relate to the old rule "do not cancel right half-plane roots"?
- Which condition on $F(s)$ makes the final value theorem valid?

## Exercises worth doing
The exercises themselves are not printed in these pages; only references appear.
- Ex. 9.1 (p. 9-5) — show that the transient response is a combination of $p_j(t)e^{\lambda_jt}$ with $\deg p_j<$ multiplicity — difficulty: medium
- Ex. 9.10 (p. 9-19) — derive the remaining transfer functions of the feedback system by block algebra, as done for $G_{yr}$ — difficulty: easy

## Reading notes
- **Part boundaries.** This part starts at the opening of Chapter 9 (epigraph, Section 9.1) and ends at the end of the "Algebraic Loops" subsection of 9.4 (p. 9-22, last words "complicated task"). The split is at a section boundary as noted. The text refers ahead to Section 9.5 (poles and zeros), Section 10.5 and Chapter 13; these are not on these pages.
- **Page numbers.** The page labels give no printed number, but the page images show chapter-style numbers "9-1" … "9-22". Citations use these, e.g. "p. 9-5". Offset: pdf = 298 + n for page 9-n (pdf 299 = 9-1; pdf 320 = 9-22).
- **Misprint (Example 9.1, eq. 9.9).** The image shows the adjugate matrix as $\begin{pmatrix}s+2\zeta\omega_0&-\omega_0\\\omega_0&s\end{pmatrix}$. For $sI-A=\begin{pmatrix}s&-\omega_0\\\omega_0&s+2\zeta\omega_0\end{pmatrix}$ the off-diagonal entries should be $+\omega_0$ (upper right) and $-\omega_0$ (lower left). The final result $k\omega_0^2/(s^2+2\zeta\omega_0s+\omega_0^2)$ is correct with the corrected signs.
- **Wording slip (Section 9.3, p. 9-15).** The text says $G$ is "the ratio of the transform of the input and the output". Section 9.1 (p. 9-2) and Example 9.8 give output over input; this digest uses output/input.
- The final value theorem is stated without conditions in the source; the digest reports it as stated.
- **Wording slip (Example 9.10, p. 9-22).** The source says the minus sign in the denominator of $G_{yr}$ occurs because $G_{ur}$ is in the feedback path. The term in that denominator is $G_{uy}$, so $G_{ur}$ looks like a slip for $G_{uy}$; the digest reports the source wording and flags it here.
- Marginal icons (e.g. circled letters) appear in the margins; their meaning is not explained on these pages. The text layer garbled the matrices; the page images were used for them.
- Cross-references to equations (6.23), (6.24), (7.6), (8.15), (8.16), (8.20), Figures 8.7 and 8.9b, and Examples 6.13, 7.4, 8.3 point to earlier chapters not provided here.
