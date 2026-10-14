---
id: astrom-2021-feedbacksystems/ch09-transfer-p2
work: astrom-2021-feedbacksystems
unit: "9 Transfer Functions (part 2/2): §9.5 Zero frequency gain, poles and zeros; §9.6 The Bode plot; §9.7 Further reading; Exercises (end of §9.4 algebraic-loop paragraph included)"
pages: 9-23 to 9-44
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Transfer Functions, part 2: Poles, Zeros and the Bode Plot

## L0 — One line
A transfer function's gain, poles and zeros, and its Bode plot (gain and phase against frequency), tell you at a glance how a linear system responds to signals, which cancellations are dangerous, and which model features limit control.

## L1 — The gist (≤ 120 words)
How can we read a linear system's behaviour directly from its transfer function G(s)? Poles (roots of the denominator) are the system's modes; zeros (roots of the numerator) block matching exponential signals. Setting s = iω gives gain and phase, drawn as a Bode plot that can be sketched by adding simple pieces. Right-half-plane zeros and time delays add phase lag without changing gain. Cancelling an unstable or slow process pole with a controller zero is a bad idea (cruise-control example). Frequency responses can also be measured and fitted with a transfer function (AFM, pupil examples).

**Prerequisites:** complex numbers (magnitude, argument); transfer function G(s) = C(sI−A)⁻¹B + D; eigenvalues; matrix rank; logarithms and decades.

## L2 — Key ideas (5–10 bullets)
- The zero-frequency gain is G(0) = D − CA⁻¹B, or b_m/a_n for the input/output differential equation. It is the steady-state output/input ratio (p. 9-23).
- Poles are modes e^{pt}. For a state-space system they are the eigenvalues of A. A transfer function is stable if all poles have negative real part (p. 9-24).
- Zeros block transmission of the exponential e^{st} at the zero. In state space, they are the s where the matrix (9.39), $\begin{pmatrix}A-sI&B\\C&D\end{pmatrix}$, loses rank. A fully actuated system, or one with the full state measured, has no zeros (p. 9-24).
- Pole/zero cancellation can hide fragility. An unstable cancellation leaves the reference-to-error map r→e looking fine while the disturbance-to-error map v→e is unstable. The lesson is not to cancel unstable or slow process poles (pp. 9-27, 9-28).
- A Bode plot uses log scales, so gains multiply and phases add term by term. Straight-line asymptotes for s^k, first-order and second-order factors let you sketch a general G(s) (pp. 9-29 to 9-33).
- A right-half-plane pole or zero, or a time delay e^{−sτ}, changes the phase strongly and leaves the gain curve unchanged. These limit achievable control performance (pp. 9-34, 9-35).
- Low- and high-frequency approximations of G(s) show how a system behaves for slow and fast signals (spring–mass, genetic circuit) (pp. 9-35 to 9-37).
- Frequency responses can be measured and fitted with transfer functions. Gain fits the poles/zeros, then a delay is added to fit the phase (pp. 9-38 to 9-40).

## L3 — Walkthrough

### End of §9.4: algebraic loops (p. 9-23)
When algebraic loops are present in a block diagram, algebraic equations must be solved to get the differential equations of the whole system. This is nontrivial because it needs symbolic solution. Most block-diagram modeling languages cannot do it and only report that a loop exists. In analog computing, loops were removed by inserting fast dynamics, which gives fast and slow modes that are hard to solve numerically. Modelica uses several sophisticated methods (p. 9-23).

### 9.5 Zero frequency gain, poles and zeros

**Zero frequency gain.** It is the magnitude of the transfer function at $s=0$. It is the ratio of steady-state output to a step input (a step is $u=e^{st}$ with $s=0$). For a state-space system, from (6.22) (p. 9-23):
$$G(0) = D - CA^{-1}B.$$
For
$$\frac{d^n y}{dt^n}+a_1\frac{d^{n-1} y}{dt^{n-1}}+\dots+a_n y = b_0\frac{d^m u}{dt^m}+b_1\frac{d^{m-1} u}{dt^{m-1}}+\dots+b_m u,$$
take $u$ and $y$ constant, $u_0$ and $y_0$. Then $a_n y_0 = b_m u_0$, so
$$G(0)=\frac{y_0}{u_0}=\frac{b_m}{a_n}.\tag{9.38}$$
(p. 9-23)

**Poles and zeros.** Let $G(s)=b(s)/a(s)$. Roots of $a(s)$ are the *poles*; roots of $b(s)$ are the *zeros*. If $p$ is a pole, $y(t)=e^{pt}$ solves (9.13) with $u=0$. So a pole is a *mode* with modal solution $e^{pt}$, and unforced motion after any excitation is a weighted sum of modes (p. 9-23).

The pure exponential output for input $e^{st}$, when $a(s)\ne 0$, is $G(s)e^{st}$. It is zero if $b(s)=0$, so zeros *block transmission* of the corresponding exponentials (p. 9-24).

- *Pole excess* (relative degree): $n_{pe}=n-m$. A rational transfer function is *proper* if $n_{pe}\ge0$ and *strictly proper* if $n_{pe}>0$ (p. 9-24).
- Uses of zeros: in integral control, the transfer function from disturbance to control error has a zero at the origin, so a constant disturbance gives no steady-state error. A vibration damper is designed so the transfer function from disturbance force to motion has a zero at the frequency to be damped (Example 9.4) (p. 9-24).

**State-space poles.** For $G(s)=C(sI-A)^{-1}B+D$, the poles are the eigenvalues of $A$. $G(s)$ is unbounded when $s$ is an eigenvalue, because there $\lambda(s)=\det(sI-A)=0$ and $sI-A$ is noninvertible. So poles depend only on $A$, the intrinsic dynamics. A transfer function is *stable* if all poles have negative real part (p. 9-24).

**State-space zeros.** Zeros are the complex $s$ for which $u=U_0e^{st}$ can give zero output. Insert $x=X_0e^{st}$ and $y=0$ in (9.2):
$$s e^{st}X_0=AX_0e^{st}+BU_0e^{st},\qquad 0=Ce^{st}X_0+De^{st}U_0,$$
$$\begin{pmatrix}A-sI & B\\ C & D\end{pmatrix}\begin{pmatrix}X_0\\U_0\end{pmatrix}e^{st}=0.$$
A solution with nonzero $X_0,U_0$ exists only if the matrix does not have full column rank. The zeros are the $s$ for which
$$\begin{pmatrix}A-sI & B\\ C & D\end{pmatrix}\tag{9.39}$$
loses rank (p. 9-24).

Zeros depend on $A,B,C,D$, i.e. on how inputs and outputs couple to states. If $B$ has full row rank, the matrix in (9.39) has $n$ independent rows for all $s$. If $C$ has full column rank, it has $n$ independent columns. So systems where $B$ or $C$ is square and full rank have no zeros. In particular, a system has no zeros if it is fully actuated or if the full state is measured (p. 9-24).

**Pole zero diagram** (Fig. 9.9): a cross marks each pole, a circle each zero. The figure has zeros at −5 and −1 and poles at −3 and −2 ± 2j. Left-half-plane poles are stable modes, right-half-plane poles unstable modes. Zeros use similar names but do not directly relate to stability. The gain must also be given for a complete description (p. 9-25).

> **Intuition note.** Poles say which natural motions $e^{pt}$ the system has. Zeros say which input exponentials get blocked. Poles come from $A$ alone; zeros also depend on how $B$ and $C$ connect inputs and outputs to the states.

**Example 9.11 (Balance system)** (pp. 9-25, 9-26). Start from the nonlinear equations of Example 3.2:
$$M_t\ddot q-ml\ddot\theta\cos\theta+c\dot q+ml\sin\theta(\dot\theta)^2=F,\qquad -ml\cos\theta\,\ddot q+J_t\ddot\theta+\gamma\dot\theta-mgl\sin\theta=0.$$
For small $\theta,\dot\theta$ the linear approximation is
$$M_t\ddot q-ml\ddot\theta+c\dot q=F,\qquad -ml\ddot q+J_t\ddot\theta+\gamma\dot\theta-mgl\theta=0.$$
With exponential signals:
$$M_ts^2q-mls^2\theta+csq=F,\qquad J_ts^2\theta-mls^2q+\gamma s\theta-mgl\theta=0.$$
Solving gives (all coefficients positive):
$$H_{\theta F}(s)=\frac{mls}{(M_tJ_t-m^2l^2)s^3+(\gamma M_t+cJ_t)s^2+(c\gamma-M_tmgl)s-mglc},$$
$$H_{qF}(s)=\frac{J_ts^2+\gamma s-mgl}{(M_tJ_t-m^2l^2)s^4+(\gamma M_t+cJ_t)s^3+(c\gamma-M_tmgl)s^2-mglcs}.$$
With small damping, set $c=\gamma=0$:
$$H_{\theta F}=\frac{ml}{(M_tJ_t-m^2l^2)s^2-M_tmgl},\qquad H_{qF}=\frac{J_ts^2-mgl}{s^2\big((M_tJ_t-m^2l^2)s^2-M_tmgl\big)}.$$
The nonzero poles and zeros are
$$p=\pm\sqrt{\frac{mglM_t}{M_tJ_t-m^2l^2}}\approx\pm2.68,\qquad z=\pm\sqrt{\frac{mgl}{J_t}}\approx\pm2.09,$$
close to those in Fig. 9.10, which uses the parameters of Example 7.7 (p. 9-26).

**Pole/zero cancellations** (pp. 9-26, 9-27). Common factors of numerator and denominator can be cancelled. Sometimes this is plain algebra, but it can mask fragility. If a cancellation happens only because terms in separate blocks coincide, it may not occur if one system is slightly perturbed. The actual behaviour can then differ severely from the expected one.

Take Fig. 9.6 with $F=1$, $C=n_c/d_c$, $P=n_p/d_p$. Then
$$G_{er}(s)=\frac{1}{1+PC}=\frac{d_c d_p}{d_cd_p+n_cn_p}.$$
Suppose the controller has a zero at $s=-a$ and the process a pole at $s=-a$. Write $n_c=(s+a)n_c'$ and $d_p=(s+a)d_p'$. Then
$$G_{er}=\frac{(s+a)d_cd_p'}{(s+a)d_cd_p'+(s+a)n_c'n_p}=\frac{d_cd_p'}{d_cd_p'+n_c'n_p},$$
so $s+a$ does not appear in $G_{er}$. For the effect of the disturbance $v$ on the error $e$:
$$G_{ev}(s)=-\frac{d_c n_p}{(s+a)d_cd_p'+(s+a)n_c'n_p}.$$
If $a<0$, this has a right-half-plane pole and is unstable. So even if $r\to e$ looks fine (perfect cancellation assumed), $v\to e$ can be unbounded. This is an *unstable pole/zero cancellation*. In state space, reachability or observability is lost when poles and zeros cancel (Example 9.7, Exercise 9.14), and the transfer function depends only on the reachable and observable subsystem $\Sigma_{ro}$ (p. 9-27).

**Example 9.12 (Cruise control)** (pp. 9-27, 9-28). The model is Fig. 9.6: $y$ velocity, $r$ desired velocity, $v$ road slope, $u$ throttle, $F=1$, and $P(s)=b/(s+a)$ for the linearized car. A "simple (but not necessarily good)" PI design takes $k_i=ak_p$. Then
$$C(s)=k_p+\frac{k_i}{s}=\frac{k_p(s+a)}{s},$$
with a zero at $s=-k_i/k_p=-a$ cancelling the process pole. So $PC=bk_p/s$ and
$$G_{yr}(s)=\frac{bk_p}{s+bk_p}.$$
The closed loop is first order with time constant $1/(bk_p)$. The cancelled mode at $s=-a$ is much slower than the closed-loop pole.

Numbers: $a=0.01$, $b=1.32$, $k_p=0.5$, $k_i=0.005$. The time constant is $1/(bk_p)=1.5$ s, so one expects settling in about 6 s (4 time constants). But in Fig. 9.11 the velocity error after a slope increase is larger and it takes a long time to settle, compared with the controller of Fig. 4.3b ($k_i=0.1$). The control signal stays practically constant after $t=15$ even though the error is large. The transfer functions from slope are
$$G_{yv}(s)=\frac{b_g s}{(s+a)(s+bk_p)},\qquad G_{uv}(s)=\frac{bk_p}{s+bk_p}.$$
The slow mode $s=-a=-0.01$ appears in $G_{yv}$ but not in $G_{uv}$. The controller zero at $-0.01$ cancels that slowly decaying process mode, so the control signal does not react to it. The error would diverge if the cancelled pole were unstable (p. 9-28).

Lesson: it is a bad idea to try to cancel unstable or slow process poles. Section 14.5 discusses this further (p. 9-28).

> **Intuition note.** A cancellation hides a mode from one input/output pair but does not remove it from the system. A disturbance entering elsewhere can excite the hidden mode. If it is slow, the error lingers; if it is unstable, the error grows.

### 9.6 The Bode plot

**Frequency response.** Set $s=i\omega$, i.e. the input $u=e^{i\omega t}=\cos\omega t+i\sin\omega t$. The output is
$$y(t)=G(i\omega)e^{i\omega t}=Me^{i(\omega t+\theta)}=M\cos(\omega t+\theta)+iM\sin(\omega t+\theta),$$
$$M=|G(i\omega)|,\qquad \theta=\arctan\frac{\operatorname{Im}G(i\omega)}{\operatorname{Re}G(i\omega)}.$$
Gain and phase are also called *magnitude* and *argument*. By linearity, a single sinusoid is amplified by $M$ and phase-shifted by $\theta$. Notation: $\angle G(i\omega)$ is phase in degrees, taken continuous (it may leave $[-180^\circ,180^\circ]$). $\arg G(i\omega)$ is phase in radians, always in $(-\pi,\pi]$. The *gain curve* is $|G(i\omega)|$ against $\omega$ on a log/log scale. The *phase curve* is $\angle G(i\omega)$ on a log/linear scale. Together they are a *Bode plot* (Fig. 9.12, the ideal PID $C(s)=20+10/s+10s=10(s+1)^2/s$) (p. 9-29).

**Sketching.** The logarithmic frequency axis covers a wide range. For $G=b_1b_2/(a_1a_2)$:
$$\log|G(s)|=\log|b_1|+\log|b_2|-\log|a_1|-\log|a_2|,\qquad \angle G=\angle b_1+\angle b_2-\angle a_1-\angle a_2.$$
So gains and phases of the factors add and subtract. A polynomial can be written as a product of terms of the type $k,\ s,\ s+a,\ s^2+2\zeta\omega_0s+\omega_0^2$, so sketching these terms suffices (pp. 9-29, 9-30).

*Powers of $s$.* For $G=s^k$ ($k=1$ differentiator, $k=-1$ integrator):
$$\log|G(i\omega)|=k\log\omega,\qquad \angle G(i\omega)=k\times90^\circ.$$
The gain curve is a straight line of slope $k$ and the phase is constant (Fig. 9.13) (p. 9-30).

*First order.* $G=a/(s+a)$, $a>0$:
$$\log|G(i\omega)|=\log a-\tfrac12\log(\omega^2+a^2),\qquad \angle G(i\omega)=-\frac{180}{\pi}\arctan\frac{\omega}{a}.$$
Approximations (Fig. 9.14a):
$$\log|G(i\omega)|\approx\begin{cases}0&\omega<a\\ \log a-\log\omega&\omega>a\end{cases}\qquad \angle G(i\omega)\approx\begin{cases}0&\omega<a/10\\ -45-45(\log\omega-\log a)&a/10<\omega<10a\\ -90&\omega>10a\end{cases}$$
The gain is flat to the *breakpoint* (corner frequency) $\omega=a$, then falls with slope −1. The phase falls by 45°/decade between $a/10$ and $10a$. So a first-order system acts like a constant at low frequency and like an integrator at high frequency (p. 9-32).

*Second order.* $G=\omega_0^2/(s^2+2\omega_0\zeta s+\omega_0^2)$, $0<\zeta<1$:
$$\log|G(i\omega)|=2\log\omega_0-\tfrac12\log\!\big(\omega^4+2\omega_0^2\omega^2(2\zeta^2-1)+\omega_0^4\big),\qquad \angle G(i\omega)=-\frac{180}{\pi}\arctan\frac{2\zeta\omega_0\omega}{\omega_0^2-\omega^2}.$$
The gain has zero slope for $\omega\ll\omega_0$ and slope −2 for large $\omega$. The largest gain $Q=\max_\omega|G(i\omega)|\approx1/(2\zeta)$ (the *Q-value*) occurs near $\omega\approx\omega_0$. Phase goes from 0 to −180°. Approximations: gain $0$ for $\omega\ll\omega_0$ and $2\log\omega_0-2\log\omega$ for $\omega\gg\omega_0$; phase $0$ and $-180$ likewise. The approximation is poor near $\omega_0$, where the plot depends strongly on $\zeta$ (Fig. 9.14b) (p. 9-32).

> **Intuition note.** On log axes a product of factors becomes a sum, so a complicated G(s) is built from a few simple straight-line pieces. Each pole bends the gain slope down by 1 at its corner frequency. Each zero bends it up by 1.

**Example 9.13 (Asymptotic approximation).** $G(s)=\dfrac{k(s+b)}{(s+a)(s^2+2\zeta\omega_0s+\omega_0^2)}$ with $a\ll b\ll\omega_0$ (Fig. 9.15) (pp. 9-32, 9-33).
- Gain: low-frequency gain $G(0)=kb/(a\omega_0^2)$. At $\omega=a$ the pole starts and the slope becomes −1. At $\omega=b$ the zero raises the slope by 1, net 0. At $\omega=\omega_0$ the second-order pole changes the slope to −2. The gain approximation is fairly accurate except near the peak due to the second-order pole (indicating that for this case $\zeta$ is reasonably small).
- Phase (effects stretch out further): at $a/10$ the pole starts a slope of −45°/decade. At $b/10$ the zero starts and gives a flat section. At $10a$ the pole's contribution ends, leaving +45°/decade from the zero. At $s\approx i\omega_0$ there is a jump of −180°. At $10b$ the zero's contribution ends and the phase is −180°. The phase approximation is less accurate than the gain one but captures the basic features.

**Poles and zeros in the right half-plane** (p. 9-34). Mirror-imaging a pole or zero in the imaginary axis leaves the gain curve unchanged but changes the phase significantly.

*Example 9.14.*
$$G=\frac{s+1}{(s+0.1)(s+10)},\quad G_{rhpp}=\frac{s+1}{(s-0.1)(s+10)},\quad G_{rhpz}=\frac{-s+1}{(s+0.1)(s+10)}.$$
All three have the same gain curve, but $G_{rhpp}$ and $G_{rhpz}$ have much larger phase lags than $G$ (Fig. 9.16) (p. 9-34).

*Time delay* $G(s)=e^{-s\tau}$: $|e^{-i\omega\tau}|=1$, so the gain is constant, but the phase is $-180\,\omega\tau/\pi$ degrees, very negative for large $\omega$. This is a more striking phase change than a right-half-plane zero, and delays are similar to RHP zeros in this respect. Intuitively, extra phase makes control harder because there is a delay between input and effect. RHP poles and zeros and delay limit achievable performance (Section 10.4, Chapter 14) (p. 9-35).

**System insights from the Bode plot** (pp. 9-35, 9-36). Many signals decompose into sinusoids, so the system can be viewed as a filter that changes amplitude and phase according to the frequency response. Where the gain slope is constant and phase near 0, the system acts as a pure gain. Where the slope is +1 and the phase near 90°, it acts as a differentiator. Fig. 9.17 shows three second-order filters:
- Low-pass, $\omega_0^2/(s^2+2\zeta\omega_0s+\omega_0^2)$: gain flat at low frequency, falling at high; phase 0 to −180°.
- Band-pass, $2\zeta\omega_0s/(s^2+2\zeta\omega_0s+\omega_0^2)$: unchanged gain near $\omega_0$, attenuation well below and above. Phase lead 90° below $\omega_0/100$ and lag 90° above $100\omega_0$, which corresponds to differentiation and integration in those ranges.
- High-pass, $s^2/(s^2+2\zeta\omega_0s+\omega_0^2)$.

Approximating $G(s)$ for small and large $s$ captures how slow and fast signals propagate (p. 9-36).

**Example 9.15 (Spring–mass).** $m\ddot q+c\dot q+kq=u$, $G(s)=1/(ms^2+cs+k)$. For small $s$, $G\approx1/k$: $q=(1/k)u$, a spring driven by a force. For large $s$, $G\approx1/(ms^2)$: $m\ddot q=u$, a mass driven by a force (double integrator) (Fig. 9.18) (p. 9-36).

**Example 9.16 (Transcriptional regulation)** (pp. 9-36, 9-37). A single gene; the question is how protein concentration responds to fluctuations $v$ in mRNA dynamics:
$$\frac{dm}{dt}=\alpha(p)-\delta m+v,\qquad \frac{dp}{dt}=\kappa m-\gamma p.$$
- Open loop (constitutive promoter): $\alpha(p)=\alpha_0$. For $v=0$ the equilibrium is $m_e=\alpha_0/\delta$, $p_e=\kappa\alpha_0/(\gamma\delta)$. The transfer function is $G^{ol}_{pv}(s)=\dfrac{\kappa}{(s+\delta)(s+\gamma)}$.
- Negative regulation (self-repression): $\alpha(p)=\dfrac{\alpha_1}{1+kp^n}+\alpha_0$. The equilibrium satisfies $m_e=\dfrac{\gamma}{\kappa}p_e$ and $\dfrac{\alpha_1}{1+kp_e^n}+\alpha_0=\delta m_e=\dfrac{\delta\gamma}{\kappa}p_e$. Linearizing around it gives
$$G^{cl}_{pv}(s)=\frac{\kappa}{(s+\delta)(s+\gamma)+\kappa\sigma},\qquad \sigma=\frac{n\alpha_1kp_e^{n-1}}{(1+kp_e^n)^2}.$$
Fig. 9.19c: the feedback circuit attenuates the response to low-frequency disturbances but slightly amplifies high-frequency disturbances compared with open loop (p. 9-37).

**Determining transfer functions experimentally** (p. 9-38). Perturb the input with a sinusoid at a fixed frequency. At steady state, the amplitude ratio and phase lag give the response at that frequency. Sweeping frequency gives the full response. With correlation techniques the response can be found very accurately, and a transfer function obtained by curve fitting. Instruments automating this are *spectrum analyzers*.

**Example 9.17 (Atomic force microscope).** The fast dynamics allow a frequency response in less than a second (Fig. 9.20). The fitted model is
$$G(s)=\frac{k\omega_2^2\omega_3^2\omega_5^2(s^2+2\zeta_1\omega_1s+\omega_1^2)(s^2+2\zeta_4\omega_4s+\omega_4^2)e^{-s\tau}}{\omega_1^2\omega_4^2(s^2+2\zeta_2\omega_2s+\omega_2^2)(s^2+2\zeta_3\omega_3s+\omega_3^2)(s^2+2\zeta_5\omega_5s+\omega_5^2)},$$
with $\omega_i=2\pi f_i$, $k=5$, $f_1=2.4$, $f_2=2.6$, $f_3=6.5$, $f_4=8.3$, $f_5=9.3$ kHz, $\zeta_1=0.03$, $\zeta_2=0.03$, $\zeta_3=0.042$, $\zeta_4=0.025$, $\zeta_5=0.032$, $\tau=10^{-4}$ s. Zero frequencies $\omega_1,\omega_4$ sit at gain minima; pole frequencies $\omega_2,\omega_3,\omega_5$ at local maxima. Damping ratios are tuned to fit peaks and dips. After the gain fits, the delay is adjusted to fit the phase. The pole at 2.55 kHz is a "trampoline" mode; the other resonances are higher modes (pp. 9-38, 9-39).

**Example 9.18 (Pupillary light reflex).** The eye regulates pupil opening to control retinal light. Stark (1960s) varied light sinusoidally and measured pupil area. A closed loop is insensitive to internal parameters, so it reveals little about the internals. A wide beam covering the whole pupil gives closed-loop dynamics. A narrow beam not influenced by the pupil opening gives open-loop dynamics (Fig. 9.21). Fitting the open-loop gain gives $G(s)=0.17/(1+0.08s)^3$, which fits the phase poorly. Adding a 0.2 s delay leaves the gain unchanged, improves the phase fit, and gives
$$G(s)=\frac{0.17}{(1+0.08s)^3}e^{-0.2s}$$
(Fig. 9.22) (p. 9-39).
For both examples, models are hard to derive from first principles; combining analytical modeling and experimental parameter identification is often fruitful. Experiments on frequency response are less attractive for slow systems because they take long (p. 9-40).

### 9.7 Further reading (pp. 9-40, 9-41)
The text credits Fourier with characterizing a linear system by its steady-state response to sinusoids, Steinmetz with the $i\omega$ method for circuits, and Gardner and Barnes with transfer functions via the Laplace transform. Laplace-based response calculation is less important today because computers generate responses easily. Pole/zero cancellation was "one of the mysteries of early control theory". Its system-theoretic consequences were clear only after Kalman's decomposition. Later chapters use transfer functions to analyze stability and describe model uncertainty (pp. 9-40, 9-41).

## Toy example (ours, not from the text)
Show an unstable cancellation and its fragility. Take $P(s)=1/(s-1)$ (unstable pole at $s=1$) and $C(s)=(s-1)/s$ (zero at $s=1$). So $n_c=s-1$, $d_c=s$, $n_p=1$, $d_p=s-1$, i.e. $a=-1$ in the text's notation.
1. $PC=\dfrac{1}{s-1}\cdot\dfrac{s-1}{s}=\dfrac1s$ after cancelling.
2. $G_{er}=\dfrac{d_cd_p}{d_cd_p+n_cn_p}=\dfrac{s(s-1)}{s(s-1)+(s-1)}=\dfrac{s(s-1)}{(s-1)(s+1)}=\dfrac{s}{s+1}$. Stable, with pole $-1$.
3. $G_{ev}=-\dfrac{d_cn_p}{d_cd_p+n_cn_p}=-\dfrac{s}{(s-1)(s+1)}$. It has a pole at $s=+1$, so it is unstable.
4. Perturb the controller to $C=(s-0.9)/s$. Then $G_{er}=\dfrac{s(s-1)}{s(s-1)+(s-0.9)}=\dfrac{s(s-1)}{s^2-0.9}$. The denominator's roots are $\pm\sqrt{0.9}\approx\pm0.949$, so one pole is in the right half-plane even for $r\to e$.

Result: the perfect cancellation hid the unstable mode from $r\to e$ but not from $v\to e$, and a 10% change in the zero exposes it everywhere.

## Concepts
- [[transfer-function]] — input-to-output relation $G(s)=b(s)/a(s)$, equal to $C(sI-A)^{-1}B+D$ for state-space systems (p. 9-24)
- [[zero-frequency-gain]] (new) — $G(0)=D-CA^{-1}B=b_m/a_n$, steady-state output/input ratio (p. 9-23)
- [[poles-and-zeros]] (new) — roots of $a(s)$ (modes $e^{pt}$) and of $b(s)$ (blocked exponentials) (p. 9-23, 9-24)
- [[eigenvalues and modes]] — poles of a state-space system are the eigenvalues of $A$; unforced motion is a sum of modes (p. 9-24)
- [[stability]] — here: a transfer function is stable if all poles have negative real part (p. 9-24)
- [[pole-zero-cancellation]] (new) — common factor cancelled in $G$; unstable or slow cancellations hide fragility and lose reachability/observability (p. 9-27)
- [[Bode plot]] — gain on log/log and phase on log/linear scales against frequency; factor contributions add (p. 9-29)
- [[delay (dead time)]] — $e^{-s\tau}$: gain 1, phase $-180\omega\tau/\pi$ degrees; like a RHP zero in phase effect (p. 9-35)
- [[controllability (reachability)]] / [[observability]] — lost under pole/zero cancellation (p. 9-27)
- [[integral action]] — integral control gives a zero at the origin from disturbance to error (p. 9-24)
- [[PID control]] — Fig. 9.12 shows the Bode plot of an ideal PID (p. 9-30)
- [[frequency-response-identification]] (new) — measure sinusoidal response, fit a transfer function (p. 9-38)

## Canonical instances
- [[balance-system-cart-pendulum]] — poles and zeros of $H_{\theta F}$, $H_{qF}$; ±2.68, ±2.09 (p. 9-26)
- [[cruise-control]] — PI design cancelling the process pole; slow mode remains (p. 9-28)
- [[spring-mass-system]] — spring at low frequency, mass at high frequency (p. 9-36)
- [[gene-self-repression]] — negative feedback attenuates low-frequency noise (p. 9-37)
- [[atomic-force-microscope]] — fitted high-order transfer function with delay (p. 9-38)
- [[pupillary-light-reflex]] — third-order lag plus 0.2 s delay (p. 9-39)

## Bridges (candidates)
- [same-math] Poles as eigenvalues of $A$ ↔ linear algebra: roots of $\det(sI-A)$ — the same characteristic polynomial.
- [structural-analogy] Bode plot as filter view of a system ↔ signal processing: low-/band-/high-pass filters — the same frequency-selective picture.
- [structural-analogy] Hidden cancelled mode ↔ observability/reachability: an unobservable or unreachable mode does not show in the transfer function.
- [structural-analogy] Self-repressing gene attenuating disturbance ↔ negative feedback in engineered loops: lower low-frequency sensitivity.
- [metaphor] A zero as a "notch" that blocks a frequency ↔ vibration damper design.

## Questions this raises
- Why does extra phase lag (RHP zero, delay) limit performance, and by how much (Section 10.4, Chapter 14)?
- Why does the genetic feedback circuit amplify slightly at high frequency, while lowering gain at low frequency?
- Can a controller zero ever be placed safely near a slow stable process pole?
- How can poles and zeros be recovered if the Bode data are noisy or the system is slow?

## Exercises worth doing
- Ex. 9.1 (p. 9-41) — exponential response and the resonance $te^{at}$ at a pole — easy
- Ex. 9.2 (p. 9-41) — sinusoidal steady-state output is $|G(i\omega)|A\sin(\omega t+\arg G)$ — medium
- Ex. 9.3 (p. 9-41) — transfer function of the linearized inverted pendulum (used again in Ex. 9.15) — easy
- Ex. 9.8 (pp. 9-42, 9-43) — three different state-space models give the same $G(s)$ — easy
- Ex. 9.13 (p. 9-44) — solutions $e^{\lambda t}$ for poles and identically-zero output for zeros — medium
- Ex. 9.14 (p. 9-44) — a pole/zero cancellation makes the closed loop unreachable and unobservable — hard

## Reading notes
- This part starts at the end of §9.4 (algebraic loops, pdf 321) and runs to the end of the chapter's exercises (pdf 342).
- Printed page numbers are not in the labels but appear in page headers as "9-N". Offset: header 9-N = pdf (N + 298). Citations use these headers, e.g. (p. 9-23) = pdf 321.
- Fig. 9.16 caption (p. 9-34): it says $G$ "has all poles and zeros in the right half-plane", but Example 9.14 gives $G$ with left-half-plane poles and zeros. It also contains the misprint "s− = 0.1".
- p. 9-35: the time-delay gain/phase is written with $G(i\omega\tau)$ where $G(i\omega)$ is meant.
- The pole excess/proper definitions use $n_{pe}=n-m$ as printed.
- Exercises 9.1 to 9.15 are printed with no solutions in this unit. Exercise 9.6 and several figures reference earlier sections not included here.
