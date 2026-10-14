---
id: astrom-2021-feedbacksystems/ch14-fundamental
work: astrom-2021-feedbacksystems
unit: "14 Fundamental Limits"
pages: 14-1 to 14-33 (chapter-page numbers as printed in the page headers)
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Fundamental Limits

## L0 — One line
Right half-plane (RHP) poles and zeros, time delays, and actuator and noise limits put fundamental limits on achievable feedback performance and robustness, and many of these limits can be written as simple inequalities.

## L1 — The gist (≤ 120 words)
The chapter asks what no controller can do, whatever its design. Bode's integral formula shows that lowering sensitivity at some frequencies raises it at others (the "waterbed" effect). Phase-lag and maximum-modulus arguments show that RHP zeros and delays cap the usable bandwidth, while RHP poles force a minimum bandwidth. A pole close to a zero in the RHP makes robust control impossible. The chapter then gives pole-placement rules: match slow stable zeros and fast stable poles with closed-loop poles. It ends with large-signal limits (saturation, minimum-time moves) and small-signal limits (noise, friction). Knowing the limits early guides sensor, actuator and system design.

**Prerequisites:** transfer functions, poles and zeros; Bode and Nyquist plots, phase margin; sensitivity functions S and T; state feedback and observers; complex analytic functions (contour integrals); the describing function.

## L2 — Key ideas (5–10 bullets)
- Poles come from the process dynamics, but zeros depend on where sensors and actuators are placed. Moving the output can therefore remove a RHP zero, whereas time delays generally cannot be removed this way (p. 14-4, 14-5).
- Strong stabilizability (stabilizing with a *stable* controller) depends on the pattern of real poles and zeros in the RHP. A process with a RHP pole to the right of a RHP zero (p > z) needs an unstable controller (p. 14-3).
- Bode's integral formula is a conservation law for log|S|. Under its assumptions, if the loop has no RHP poles the area of log|S| above zero equals the area below it; with RHP poles the integral is $\pi\sum p_k$, which is positive, so overall sensitivity is larger (p. 14-6).
- The process is split into a minimum-phase part and an *all-pass* part (unit gain, extra phase lag). The gain crossover frequency inequality limits the all-pass phase lag at the gain crossover frequency $\omega_{gc}$ of the loop. A RHP zero or a delay sets an upper bound on crossover frequency; a RHP pole sets a lower bound (p. 14-11 to 14-14).
- The maximum modulus principle (a bounded analytic function on the RHP is largest on the imaginary axis) gives explicit bounds on the peak values $M_s=\max|S|$ and $M_t=\max|T|$ and on crossover frequencies (Table 14.1). For a single RHP pole/zero pair, M_s ≥ (z+p)/|z−p|, so pole and zero must be well separated (p. 14-18, 14-20).
- For the rear-steered bicycle the zero/pole ratio z/p = (v₀/a)√(h/g) grows with speed, so to ride it comfortably the speed must be sufficiently large (with $M_s=2$ the bound is 9.4 m/s for one bicycle and 1.2 m/s for the other) (p. 14-19, 14-20).
- In pole placement, place closed-loop poles near slow stable process zeros and near fast stable process poles. Otherwise S or T gets large peaks, even though the poles look well damped (p. 14-24, 14-25).
- Large-signal limits (saturation, minimum-time moves) and small-signal limits (noise, quantization, friction) also bound performance. Friction oscillation can be predicted approximately with the describing function (p. 14-26 to 14-30).

## L3 — Walkthrough

### Intro and 14.1 System design considerations (p. 14-1 to 14-5)
The chapter covers limits from non-minimum phase dynamics (time delays, RHP poles and zeros), large-signal limits (actuator rate and power, process-protection constraints) and small-signal limits (noise, friction, quantization). It also covers consequences for loop shaping and rules for pole placement (p. 14-1). The author's advice: recognise the limits early and co-design process and controller where possible (p. 14-2). A time delay limits the achievable response speed (the text calls this intuitively clear). A RHP pole/zero pair with the pole close to the zero cannot be controlled robustly (p. 14-2).

**Stabilizability and strong stabilizability (p. 14-2, 14-3).**
- Pole placement by state feedback needs reachability; by output feedback it needs reachability and observability (p. 14-2).
- *Stabilizable*: all unstable eigenvalues can be moved by feedback. *Strongly stabilizable*: the system can be stabilized by a stable controller. An unstable controller does not by itself make the closed loop unstable (p. 14-2).
- A reachable linear system with state feedback is always stabilizable. If it is not reachable, Kalman's decomposition gives
$$\frac{d}{dt}\begin{pmatrix}x_r\\ x_{\bar r}\end{pmatrix}=\begin{pmatrix}A_r & 0\\ * & A_{\bar r}\end{pmatrix}\begin{pmatrix}x_r\\ x_{\bar r}\end{pmatrix}+\begin{pmatrix}B_r\\ 0\end{pmatrix}u \tag{14.1}$$
- The reachable part can get arbitrary eigenvalues from some $K_r$, so (14.1) is stabilizable if and only if the eigenvalues of $A_{\bar r}$ are in the left half-plane (p. 14-2, 14-3).
- PBH test: a system with $n$ states is reachable if and only if
$$\operatorname{rank}\begin{pmatrix}A-sI & B\end{pmatrix}=n \tag{14.2}$$
  holds for all complex $\lambda$ (the page writes both $s$ and $\lambda$). The system is stabilizable if the condition holds for all $\lambda$ in the RHP $\operatorname{Re}s\ge 0$. So stabilizability is weaker than reachability (p. 14-3).
- Output-feedback controller (estimator plus feedback on the estimate):
$$\frac{d\hat x}{dt}=A\hat x+Bu+L(y-C\hat x),\qquad u=-K\hat x \tag{14.3}$$
  Controller poles are the eigenvalues of $A-BK-LC$. Controller zeros are the values of $s$ where
$$\begin{pmatrix}A-BK-LC-sI & L\\ K & 0\end{pmatrix} \tag{14.4}$$
  loses rank. A stabilizable and observable system always has a stabilizing controller; whether that controller is stable is "more subtle" (p. 14-3).
- **Theorem 14.1 (strong stabilizability).** For $P(s)=n(s)/d(s)$ with no common factor, the system can be strongly stabilized if and only if all $d(z_k)$ have the same sign for all $z_k$ with $n(z_k)=0$. It is proven in Vidyasagar (p. 14-3). For one pole $p$ and one zero $z$, a process with $p>z$ requires a controller with a RHP pole, i.e. an unstable controller (Fig. 14.1 and p. 14-3, 14-4).
- **Theorem 14.2.** A linear system is strongly stabilizable if and only if it has an even number of real poles between every pair of real zeros in $\operatorname{Re}s\ge0$ (p. 14-3).
- So strong stabilizability depends on pole/zero patterns fixed early in design. This does not mean unstable systems should always be avoided, e.g. for high-maneuverability aircraft (p. 14-3).

*Intuition note:* Whether a stable controller can do the job is decided by where the process's poles and zeros sit relative to each other. Poles are fixed by the dynamics, so this has to be considered early.

**RHP zeros and delays (p. 14-4, 14-5).**
- Poles are eigenvalues of $A$ and are unaffected by sensors and actuators. Zeros depend on how sensors and actuators connect to the process, so they can be changed by moving or adding sensors or actuators (p. 14-4).
- **Example 14.1 (vehicle steering).** The model is $P(s)=(av_0 s+v_0^2)/(bs)$, with $v_0$ the velocity, $a$ the offset of the reference point and $b$ the wheelbase. It has a RHP zero when the velocity is negative. Measuring the position of the rear-wheel centre gives $a=0$ and $G(s)=v_0^2/(bs)$, with no RHP zero (p. 14-4, 14-5). A calibration error $\epsilon$ puts a zero at $v_0/\epsilon$. This is a "fast" zero whose effect is "relatively minor" (p. 14-5).
- Delays add phase lag and have effects similar to RHP zeros. The first- and second-order Padé approximations (unit-gain rational functions approximating a delay) are
$$G_1(s)=\frac{1-s\tau/2}{1+s\tau/2},\qquad G_2(s)=\frac{1-\tau s/2+(\tau s)^2/12}{1+\tau s/2+(\tau s)^2/12}.$$
  $G_1$ has a RHP zero at $2/\tau$. $G_2$ has RHP zeros at $s=(3\pm i\sqrt3)/\tau$ (p. 14-5).
- Unlike zeros, delays generally cannot be removed by sensor or actuator placement, so computing and communication architecture should minimise them (p. 14-5).

### 14.2 Bode's integral formula (p. 14-5 to 14-10)
Sensitivity $S=1/(1+L)$ ($L=PC$ is the loop transfer function). Disturbances at frequency $\omega$ are attenuated if $|S(i\omega)|<1$ and amplified if $|S(i\omega)|>1$. $M_s=\max_\omega|S(i\omega)|$, and $1/M_s$ equals the stability margin $s_m$ (p. 14-5).

**Theorem 14.3 (Bode's integral formula).** Let $S$ be the sensitivity function of an internally stable closed loop with loop transfer function $L$. Assume $sL(s)\to0$ as $s\to\infty$. Then
$$\int_0^\infty \log|S(i\omega)|\,d\omega=\int_0^\infty\log\frac{1}{|1+L(i\omega)|}\,d\omega=\pi\sum p_k \tag{14.5}$$
where the sum is over the RHP poles $p_k$ of $L$ (p. 14-6).
- Consequences: lowering sensitivity at some frequencies raises it at others (the *waterbed effect*). Systems with RHP open-loop poles have larger overall sensitivity than stable ones. With no RHP poles the integral is 0, so on a linear frequency axis the area of $\log|S|$ above zero equals the area below (Fig. 14.2). Making $S$ small up to $\omega_{sc}$ is balanced by larger $S$ above $\omega_{sc}$ (p. 14-6).
- The assumption $sL(s)\to0$ is essential. Exercise 14.2 shows that without it the sensitivity can be made arbitrarily small. Exercise 14.3 covers $sL(s)\to k$ (p. 14-6).
- Complementary sensitivity $T=L/(1+L)$ obeys
$$\int_0^\infty\frac{\log|T(i\omega)|}{\omega^2}\,d\omega=\pi\sum\frac1{z_i} \tag{14.6}$$
  summed over the RHP zeros of $L=PC$ (Exercise 14.4). So slow RHP zeros are worse than fast ones, just as fast RHP poles are worse than slow ones (p. 14-7).

*Intuition note:* Sensitivity behaves like a fixed amount of water in a bed. If you press it down in one frequency range, it bulges elsewhere. Unstable open-loop poles add extra water.

**Example 14.2 (X-29 aircraft, after G. Stein) (p. 14-7, 14-8).**
- Data: phase margin required ≥ 45°. The longitudinal dynamics are like an inverted pendulum, with a RHP pole $p\approx6$ rad/s and a RHP zero $z=26$ rad/s. Actuator bandwidth is $\omega_a=40$ rad/s and desired pitch bandwidth is $\omega_1=3$ rad/s.
- Assumed sensitivity shape (Fig. 14.3b):
$$|S(i\omega)|=\begin{cases}\dfrac{\omega}{\omega_1}M_s & \omega<\omega_1\\ M_s & \omega_1\le\omega<\omega_a\\ 1 & \omega_a\le\omega<\infty\end{cases}$$
- Bode's integral becomes
$$\int_0^{\omega_1}\log\frac{\omega M_s}{\omega_1}\,d\omega+(\omega_a-\omega_1)\log M_s=\pi p.$$
  Integration by parts gives, "after some calculation", $-\omega_1+\omega_a\log M_s=\pi p$, hence
$$M_s=e^{(\pi p+\omega_1)/\omega_a}.$$
- With $p=6$, $\omega_1=3$, $\omega_a=40$ the text gets $M_s=1.75$: disturbances between $\omega_1$ and $\omega_a$ are amplified by that factor. Using (10.7), $\varphi_m\ge2\arcsin\frac1{2M_s}=33^\circ$, so the 45° requirement "may not be achievable" (p. 14-8).

**Derivation of (14.5) by contour integration (p. 14-8 to 14-10).**
- Assume distinct RHP poles $p_k$ and $L$ decaying faster than $1/s$. Integrate $\log S(s)$, $S=1/(1+L)$, counter-clockwise along the Nyquist contour $\Gamma$ (Fig. 14.4). $\Gamma$ encloses the RHP except small paths around each $p_k$, where $S$ has a zero and $\log S$ is singular.
$$I=\oint_\Gamma\log S(s)\,ds=I_1+I_2+I_3=0,$$
  because $\log S$ is analytic inside the contour. $I_1$ is the imaginary axis, $I_2$ a large semicircle of radius $R$, $I_3$ the paths around the poles (p. 14-8).
- $I_1=-i\int_{-R}^{R}\log S(i\omega)\,d\omega=-2i\int_0^R\log|S(i\omega)|\,d\omega$, since the real part of $\log S(i\omega)$ is even and the imaginary part is odd (p. 14-8, 14-9).
- $I_2=\int_\supset\log S\,ds=-\int_\supset\log(1+L)\,ds\approx-\int_\supset L\,ds\to0$ as $R\to\infty$, because $L$ decays faster than $1/s$ (p. 14-9).
- $I_3$ splits into $X_+$, a small circle $\gamma$ of radius $r$, and $X_-$. On $\gamma$ the integrand is of order $\log r$ over length $2\pi r$, so that integral tends to 0 as $r\to0$. Near $p_k$, $S\approx k(s-p_k)$, so the argument of $S$ decreases by $2\pi$ on going around $p_k$ clockwise. Hence $|S_{X_+}|=|S_{X_-}|$ and $\arg S_{X_-}=\arg S_{X_+}-2\pi$, so $\log S_{X_+}-\log S_{X_-}=2\pi i$ (p. 14-9).
- $X_+$ and $X_-$ are traversed in opposite directions and have length $\operatorname{Re}p_k$, so their sum is $2\pi i\,\operatorname{Re}p_k$ (p. 14-10).
- Summing over all poles: $I_1+I_2+I_3=-2i\int_0^\infty\log|S(i\omega)|\,d\omega+i\sum_k2\pi\operatorname{Re}p_k=0$. Poles come in complex-conjugate pairs, so $\sum\operatorname{Re}p_k=\sum p_k$, giving (14.5) (p. 14-10).

### 14.3 Gain crossover frequency inequality (p. 14-10 to 14-15)
Loop shaping makes $|L|$ large where disturbance attenuation is wanted and small at high frequency where noise dominates, with good robustness around the gain crossover frequency $\omega_{gc}$ (p. 14-10).

**Factorisation.** $P=P_{mp}P_{ap}$ \tag{14.7}, where $P_{mp}$ (minimum phase) has all poles and zeros in the open left half-plane. $P_{ap}$ is normalised to $|P_{ap}(i\omega)|=1$ (an *all-pass* factor) with negative phase. $P$ and $P_{mp}$ have the same gain curve, but $P$ has more phase lag. Example (14.8):
$$P(s)=\frac{s-2}{(s+1)(s-1)}=\frac{s+2}{(s+1)^2}\cdot\frac{(s-2)(s+1)}{(s+2)(s-1)}=P_{mp}P_{ap}.$$

**Derivation of the inequality.** The phase-margin condition is
$$\arg L(i\omega_{gc})=\arg P_{ap}+\arg P_{mp}+\arg C\ \ge\ -\pi+\varphi_m \tag{14.9}$$
Let $n_{gc}$ be the slope of the gain curve of $L$ at crossover, $n_{gc}=\frac{d\log|L|}{d\log\omega}\big|_{\omega_{gc}}$ (same as for $P_{mp}C$, since $|P_{ap}|=1$). If $C$ has no RHP poles or zeros, Bode's relations (10.9) give $\arg P_{mp}(i\omega)+\arg C(i\omega)\approx n_{gc}\frac\pi2$ (p. 14-11).

**Theorem 14.4 (gain crossover frequency inequality).** Let $C$ be a stabilizing compensator with no RHP poles or zeros, phase margin $\varphi_m$, crossover frequency $\omega_{gc}$ and slope $n_{gc}$. Then
$$\varphi_{ap}:=-\arg P_{ap}(i\omega_{gc})\ \le\ \pi-\varphi_m+n_{gc}\frac\pi2=:\bar\varphi_{ap} \tag{14.10}$$
(p. 14-11). Examples of $\bar\varphi_{ap}$:
- $\varphi_m=\pi/3$, $n_{gc}=-1$ gives $\pi/6\approx0.52$ rad (30°).
- $\varphi_m=\pi/4$, $n_{gc}=-1/2$ gives $\pi/2$ (90°) (p. 14-11, 14-12).

Non-minimum phase parts therefore restrict crossover frequencies, and some systems cannot be controlled with sufficient margins (p. 14-12).

*Intuition note:* The all-pass part adds phase lag without changing gain. The loop only has a limited phase budget at crossover, so the lag of the non-minimum phase part must fit inside it.

**Example 14.3 (RHP zero).** $P_{ap}=(z-s)/(z+s)$, $z>0$, with lag $\varphi_{ap}=2\arctan(\omega/z)$. Then
$$\omega_{gc}\le z\tan(\bar\varphi_{ap}/2) \tag{14.11}$$
For $\bar\varphi_{ap}=\pi/3$, $\omega_{gc}<0.6z$. Slow RHP zeros give lower crossover than fast ones (p. 14-12). The text links RHP zeros to physics, e.g. hydroelectric power (Ex. 14.5), drum-level inverse response (Ex. 3.14) and product-development cost (p. 14-12).

**Example 14.4 (RHP pole).** $P_{ap}=(s+p)/(s-p)$, lag $2\arctan(p/\omega)$. Then
$$\omega_{gc}\ge\frac{p}{\tan(\bar\varphi_{ap}/2)} \tag{14.12}$$
For $\bar\varphi_{ap}=\pi/3$, $\omega_{gc}>1.7p$. Fast RHP poles need larger crossover frequency, so process, actuators and sensors need sufficiently high bandwidth (p. 14-12, 14-13).

**Example 14.5 (RHP pole/zero pair).** The process is written "$P(s)=\frac{a-z}{s-p}$" (the numerator should read $s-z$, see Reading notes). The all-pass factor is $P_{ap}=\frac{(z-s)(s+p)}{(z+s)(s-p)}$ \tag{14.13} with lag
$$\varphi_{ap}=2\arctan(\omega/z)+2\arctan(p/\omega) \tag{14.14}$$
(Fig. 14.6a). To keep the lag below 90° the ratio $z/p$ must be larger than 6 (read from Fig. 14.6). The crossover values are also quite restricted. Theorem 14.4 cannot be applied if $p>z$, because a stabilizing controller then needs a RHP pole (p. 14-13, 14-14).

**Time delays (p. 14-14).** For a delay the text writes $P_{ap}(s)=e^{\tau s}$ (sign as printed, see Reading notes). Inequality (14.10) gives $\omega_{gc}\tau\le\bar\varphi_{ap}$. Delays act like RHP zeros: they force low bandwidth and crossover.

**Example 14.6 (RHP pole and delay).**
$$P_{ap}=\frac{s+p}{s-p}e^{-\tau s},\qquad\varphi_{ap}=\omega\tau+2\arctan(p/\omega)\tag{14.15}$$
The behaviour is similar to a pole/zero pair (Fig. 14.6b). The minimum lag is $\sqrt{p\tau(2-p\tau)}+2\arctan\sqrt{p\tau/(2-p\tau)}$, at $\omega\tau=\sqrt{p\tau(2-p\tau)}$ (Exercise 14.7). By (14.9), a system with a RHP pole $p$ and delay $\tau$ cannot be stabilized by a controller without RHP poles and zeros if $p\tau\ge2$ (p. 14-14).

**Example 14.7 (balance system).**
- Transfer functions from force $F$ to angle $\theta$ and cart position $q$:
$$H_{\theta F}=\frac{ml}{(M_tJ_t-m^2l^2)s^2-mglM_t},\qquad H_{qF}=\frac{J_ts^2-mgl}{s^2\big((M_tJ_t-m^2l^2)s^2-mglM_t\big)}$$
- Using the cart position as measurement, $H_{qF}$ has poles $\{0,0,\pm\sqrt{mglM_t/(M_tJ_t-m^2l^2)}\}$ and zeros $\{\pm\sqrt{mgl/J_t}\}$. With the Example 7.7 parameters: $p=2.68$, $z=2.09$. The text states that, with the best crossover choice, the all-pass lag is 166° (from (14.14)), so no reasonable phase margin is possible. $p/z=1.28$, far from the value 6 needed. Achievable margin is very small for a 2–4 rad/s bandwidth (p. 14-14).
- Changing the output to a point at distance $r$ along the pendulum, $y=q-r\sin\theta$:
$$H_{yF}=H_{qF}-rH_{\theta F}=\frac{(J_t-mlr)s^2-mgl^2}{s^2\big((M_tJ_t-m^2l^2)s^2-mglM_t\big)}$$
  (numerator as printed; see Reading notes). If $mlr-J_t>0$ the RHP zero is replaced by two imaginary zeros. The gain crossover frequency is then determined by the RHP pole $p=\sqrt{mglM_t/(M_tJ_t-m^2l^2)}$ (Example 14.4). With admissible lag $\varphi_l=45^\circ$, $\omega_{gc}\ge p/\tan(\varphi_l/2)=6.48$ rad/s. If actuator bandwidth is about 10 times higher (roughly 10 Hz), robust tracking up to this frequency is possible (p. 14-15).

### 14.4 The maximum modulus principle (p. 14-15 to 14-20)
**Theorem 14.5.** Let $\Omega\subset\mathbb C$ be nonempty, bounded, open and connected, and $G$ continuous on the closure $\bar\Omega$ and analytic on $\Omega$. Then $\sup_{s\in\bar\Omega}|G|=\sup_{s\in\partial\Omega}|G|$.

**Corollary.** For $G$ bounded and analytic on the closed RHP, $\max_\omega|G(i\omega)|=\max_{\operatorname{Re}s\ge0}|G(s)|$ (p. 14-15).

Facts used: $S=\frac1{1+PC}$, $T=\frac{PC}{1+PC}$, $S+T=1$. Zeros of $S$ are the poles of process and controller. Zeros of $T$ are the zeros of process and controller. Hence $S(z)=1$ at zeros $z$ and $T(p)=1$ at poles $p$ of process or controller (p. 14-15).

**Requirements.** Nominal bounds
$$S_r(s)=\frac{M_ss}{s+a},\qquad T_r(s)=\frac{M_tb}{s+b}\tag{14.16}$$
with requirements $|S|\le|S_r|$, $|T|\le|T_r|$ \tag{14.17}. Crossover frequencies and bandwidth:
$$\omega_{sc}=\frac{a}{\sqrt{M_s^2-1}},\quad\omega_{tc}=b\sqrt{M_t^2-1},\quad\omega_b=b\sqrt{2M_t^2-1}\tag{14.18}$$
(p. 14-16).

**Example 14.8 (RHP zero).** Assume the process has a RHP zero $z$ and no other RHP poles or zeros. The requirement (14.17) implies $\max_\omega|S/S_r|\le1$ \tag{14.19}. $S/S_r$ is analytic in the RHP, so the maximum modulus principle gives
$$\max_\omega\left|\frac{S(i\omega)}{S_r(i\omega)}\right|\ge\left|\frac{S(z)}{S_r(z)}\right|=S(z)\frac{z+a}{M_sz}=\frac{z+a}{M_sz}.$$
This is compatible with (14.19) only if $z+a\le M_sz$, hence
$$a\le z(M_s-1),\qquad\omega_{sc}\le z\sqrt{\frac{M_s-1}{M_s+1}}\tag{14.20}$$
(p. 14-16, 14-17). For complex zeros $z_{re}\pm iz_{im}$ (Exercise 14.9):
$$a\le\sqrt{M_s^2z_{re}^2+(M_s^2-1)z_{im}^2}-z_{re},\quad\omega_{sc}\le\frac{\sqrt{M_s^2z_{re}^2+(M_s^2-1)z_{im}^2}-z_{re}}{\sqrt{M_s^2-1}}\tag{14.21}$$
which reduces to (14.20) for $z_{im}=0$. With several RHP zeros the smallest bound applies (p. 14-17). A similar analysis for $T$ (Exercise 14.10) shows that RHP poles require sufficiently large $\omega_{tc}$ and $\omega_b$ (p. 14-17).

**Example 14.9 (poles and zeros in the RHP).** Write $P=\frac{n(s)}{d(s)}\tilde P(s)$ \tag{14.22}, where $n$ has the RHP zeros $z_k$, $d$ has the RHP poles $p_k$, and $\tilde P$ has none. For stabilizing controllers
$$S=\frac1{1+PC}=\frac{d}{d+n\tilde PC},\qquad S(z_k)=1.$$
Take $W_p(s)=d(-s)/d(s)$. It has $|W_p(i\omega)|=1$, and $W_pS$ is analytic in the RHP ($d$ cancels and the roots of $d(-s)$ are in the left half-plane). Then
$$M_s=\max_\omega|W_pS|\ge|W_p(z_k)S(z_k)|=\left|\frac{d(-z_k)}{d(z_k)}\right|\tag{14.23}$$
$$M_s\ge\max_k\left|\frac{d(-z_k)}{d(z_k)}\right|\tag{14.24}$$
For a single pair, $n=s-z$, $d=s-p$:
$$M_s\ge\left|\frac{z+p}{z-p}\right|\tag{14.25}$$
$$\frac zp\ge\frac{M_s+1}{M_s-1}\ \text{ if }z>p,\qquad\frac zp\le\frac{M_s-1}{M_s+1}\ \text{ if }z<p\tag{14.26}$$
(p. 14-18). Pole and zero must be well separated. For $M_s=3$ the critical ratios are 0.5 and 2; for $M_s=1.4$ they are 1/6 and 6. For $T$ (Exercise 14.11):
$$M_t\ge\max_k\left|\frac{n(-p_k)}{n(p_k)}\right|\tag{14.27}$$
$$M_t\ge\left|\frac{z+p}{z-p}\right|\ \Rightarrow\ \frac zp\ge\frac{M_t+1}{M_t-1}\ \text{ or }\ \frac zp\le\frac{M_t-1}{M_t+1}\tag{14.28}$$
(p. 14-18).

*Intuition note:* A RHP zero wants low bandwidth and a RHP pole wants high bandwidth. When they are close the two demands collide, and a large sensitivity peak is unavoidable.

**Example 14.10 (rear-wheel-steered bicycle).**
- Model (Section 4.2): $J\ddot\varphi-\frac{Dv_0}{b}\dot\delta=mgh\sin\varphi+\frac{mv_0^2h}{b}\delta$, with $J\approx mh^2$, $D\approx mah$. Reversing the sign of velocity gives
$$mh^2\ddot\varphi+\frac{mhav_0}{b}\dot\delta=mgh\sin\varphi+\frac{mv_0^2h}{b}\delta.$$
- Transfer function: $P_{\varphi\delta}=\frac{-av_0s+v_0^2}{b(hs^2-g)}=\frac{av_0}{bh}\frac{-s+v_0/a}{s^2-g/h}$. RHP pole $p=\sqrt{g/h}$, RHP zero $z=v_0/a$.
- By (14.26): $\frac zp=\frac{v_0}a\sqrt{\frac hg}\ge\frac{M_s+1}{M_s-1}$, so $v_0\ge a\sqrt{\frac gh}\frac{M_s+1}{M_s-1}$. The pole does not depend on speed, but the zero grows with speed, so the speed must be sufficiently large.
- With $M_s=2$: $v_0\ge9.4$ m/s (34 km/h) for the bicycle in Fig. 14.8a and $v_0\ge1.2$ m/s (3.8 km/h) for 14.8b. The first "has indeed proven to be unrideable", the second is rideable (p. 14-19, 14-20). The parameter values are not given in this unit.

**Remaining comments (p. 14-20).** It is "perhaps surprising" that processes with $p>z$ can be controlled robustly, but this needs "more clever design techniques". Stabilization by a stable controller holds if and only if the number of poles between every pair of RHP zeros is even (Theorem 14.2, credited to Youla). Table 14.1 summarises the limits:

| Process feature | Limit |
|---|---|
| Real RHP zero $z$ | $\omega_{sc}\le z\sqrt{\frac{M_s-1}{M_s+1}}$ |
| Complex RHP zeros | $\omega_{sc}\le\frac{\sqrt{M_s^2z_{re}^2+(M_s^2-1)z_{im}^2}-z_{re}}{\sqrt{M_s^2-1}}$ |
| Real RHP pole $p$ | $\omega_{tc}\ge p\sqrt{\frac{M_t+1}{M_t-1}}$ |
| Complex RHP poles | $\omega_{tc}\ge\frac{\sqrt{M_t^2p_{re}^2+(M_t^2-1)p_{im}^2}+p_{re}}{\sqrt{M_t^2-1}}$ |
| Pole/zero pair | $M_s\ge\left\lvert\frac{p+z}{p-z}\right\rvert,\ M_t\ge\left\lvert\frac{p+z}{p-z}\right\rvert$ |
| RHP poles and zeros | $M_s\ge\max_k\left\lvert\frac{d(-z_k)}{d(z_k)}\right\rvert,\ M_t\ge\max_k\left\lvert\frac{n(-p_k)}{n(p_k)}\right\rvert$ |
| RHP pole $p$ and delay $\tau$ | $M_t\ge e^{p\tau},\ M_s\ge e^{p\tau}-1$ |

The delay row is listed in Table 14.1 without derivation in this unit.

### 14.5 Robust pole placement (p. 14-20 to 14-25)
A design method that does not include robustness requirements (pole placement is the case treated here) must be checked for robustness. The section shows that process zeros must be taken into account when choosing closed-loop poles (p. 14-20, 14-21).

**Fast stable process poles.** A pole is "fast" if its magnitude exceeds the intended closed-loop bandwidth (p. 14-21).

**Example 14.11.** $P=b/(s+a)$, $a>0$, with PI controller $C=k_p+k_i/s$.
- Characteristic polynomial: $s(s+a)+b(k_ps+k_i)=s^2+(a+bk_p)s+k_ib$.
- Desired poles $-p_1,-p_2$ give $k_p=\frac{p_1+p_2-a}{b}$, $k_i=\frac{p_1p_2}{b}$, and
$$S=\frac{s(s+a)}{(s+p_1)(s+p_2)},\qquad T=\frac{(p_1+p_2-a)s+p_1p_2}{(s+p_1)(s+p_2)}.$$
- If $p_1<p_2<a$ (process pole faster than the closed-loop poles), $k_p<0$ and the controller has a RHP zero. This is "an indication that the system may have bad properties". For $a=b=1$, $p_1=0.05$, $p_2=0.2$ (Fig. 14.9a), $S\approx1$ at high frequency, and $|S|$ rises from $\omega=a$ downward until the frequency is below $p_2$. The text calls the resulting peak "approximately $\omega=a/\sqrt{p_1p_2}\approx10$" (see Reading notes).
- Choosing $p_2=a$ gives $k_p=p_1/b$, $k_i=ap_1/b$. The controller zero at $s=-a$ cancels the fast process pole. Then $L=bk_p/s$, $S=s/(s+bk_p)$, $T=bk_p/(s+bk_p)$. Fig. 14.9b (closed-loop poles $p_1=5$, $p_2=20$, process pole $a=1$) shows no sensitivity peak (p. 14-21, 14-22).

**Slow stable process zeros.** A zero is "slow" if its magnitude is below the intended bandwidth (p. 14-22).

**Example 14.12 (vehicle steering).**
- $P(s)=\frac{\gamma s+1}{s^2}$. A faster design uses $\omega_c=10$, $\zeta_c=0.707$, $\omega_o=20$, $\zeta_o=0.707$, with gains $k_1=100$, $k_2=-35.86$, $l_1=28.28$, $l_2=400$ and
$$C(s)=\frac{-11516s+40000}{s^2+42.4s+6657.9}\tag{14.29}$$
- The loop is stable but not robust: phase margin 7°, gain margin 1.08 (instability if gain rises 8%), $M_s=13$, $M_t=12$ (Fig. 14.10, 14.11). The controller has a RHP zero at $s=3.5$, and by Example 14.3 a process zero at 3.5 would allow $\omega_{gc}\le2$ (p. 14-22, 14-23).
- Cause: $T=\frac{n_pn_c}{d_pd_c+n_pn_c}$ has as zeros the process and controller zeros. $T(0)=1$ because of the double integrator. $|T|$ rises at the process zero ($\omega=2$) and the controller zero (3.5), and falls only at the closed-loop poles ($\omega=10$, 20), giving a high peak (p. 14-23, 14-24).
- Fix: $\omega_c=10$, $\zeta_c=2.6$ puts closed-loop poles at $s=-2$ and $s=-50$:
$$C(s)=\frac{3628s+40000}{s^2+80.28s+156.56}=3628\frac{s+11.02}{(s+2)(s+78.28)}\tag{14.31}$$
  The controller pole at $-2$ cancels the process zero. $C(0)=6.0$ for (14.29) but $C(0)=255$ for (14.31). Now $M_s=1.34$ and $M_t=1.41$. $|PS|$ shows better disturbance attenuation, and $|CS|$ shows less sensitivity to measurement noise (p. 14-24).
- Recipe: cancel the slow stable process zero, design for the system without it, then add the pole to the controller (p. 14-24).

**Lessons (p. 14-24, 14-25).** Evaluate the whole Gang of Four. Seemingly reasonable pole-placement designs need not be robust. Robustness requires closed-loop poles equal or close to slow stable process zeros. Slow unstable zeros limit bandwidth. The text warns that exact cancellation may cause undesirable dynamics or lack of robustness under model uncertainty, and says this is addressed "below" (see Reading notes).

**Design rules (p. 14-25).**
- With $M_t=\sup_\omega|T(i\omega)|=\|PC/(1+PC)\|_\infty$ (13.12): $T=1$ at low frequency and rises near slow process zeros unless a closed-loop pole is near. So slow stable zeros should be canceled by controller poles. Slow unstable zeros cannot be canceled, so $\omega_{gc}$ must be below the slowest unstable zero.
- With $M_s=\|1/(1+PC)\|_\infty$: $S=1$ at high frequency and rises moving down past fast process poles, unless closed-loop poles are near them. Controller zeros near the fast pole can do this. A fast unstable pole cannot be canceled, so $\omega_{gc}$ must be sufficiently large.
- Summary: slow stable process zeros should be matched by slow closed-loop poles, and fast stable process poles by fast closed-loop poles. Slow unstable zeros and fast unstable poles impose severe limits.

### 14.6 Nonlinear effects (p. 14-26 to 14-30)
**Actuation limits.** Motors, amplifiers and pumps have limits, as do protection constraints; limits can apply to amplitude and rate of the control signal and to internal variables (p. 14-26). Example: the 2004 grounding of a Swedish ferry entering Umeå in 20 m/s wind. Wind forces of 600 kN and more exceeded the propeller and rudder forces, and even a 260 kN tugboat could not have helped (p. 14-26).

**Example 14.13 (current limit in a servo).**
- Voice-coil model: $m\ddot x=F=k_II$ \tag{14.32}. Maximum acceleration $a_{max}=k_II_{max}/m$; maximum velocity $v_{max}=V_{max}/k_I$ (p. 14-26).
- Minimum-time transition: apply maximum acceleration until the midpoint, then maximum braking ("bang-bang"). With a velocity limit, accelerate only until $v_{max}$, coast, then brake. Using $v=at$ and $x=at^2/2=v^2/(2a)$, the minimum time over distance $\ell$ (zero velocity at both ends) is
$$t=\begin{cases}2\sqrt{\ell/a_{max}}&\ell\le v_{max}^2/a_{max}\\ \ell/v_{max}+v_{max}/a_{max}&\ell>v_{max}^2/a_{max}\end{cases}\tag{14.33}$$
- (added step) First case: each half takes $\sqrt{\ell/a_{max}}$ and the peak speed is $\sqrt{a_{max}\ell}\le v_{max}$. Second case: two ramps of duration $v_{max}/a_{max}$ cover $v_{max}^2/a_{max}$ in total, and the rest is covered at $v_{max}$.
- Fig. 14.12 parameters: $m=2.5\times10^{-3}$ kg, $k_I=2.5$ N/A, $I_{max}=0.5$ A, $V_{max}=5$ V, giving $a_{max}=500$ m/s² and $v_{max}=2$ m/s (p. 14-27). Software for minimum-time control of more complex systems is readily available.

**Stability with saturation.** The circle criterion models saturation as a sector nonlinearity with $k_{low}=0$, $k_{high}=1$: the system is stable if the Nyquist curve of the linear part has $\operatorname{Re}H(s)>-1$. The describing function method (an approximation) is slightly less constraining: its image for saturation is the negative real axis from $-\infty$ to $-1$, so the Nyquist curve of $H$ should not cross the negative real axis at a gain greater than one (p. 14-27, 14-28).

**Noise, quantization, friction (p. 14-28).** The controller feeds measurement noise into the system. Output fluctuations limit regulation; control-signal fluctuations cause wear or saturation. Noise is mainly high-frequency, so it limits the controller's high-frequency gain, the bandwidth and the response time. Linear methods (transfer functions from noise sources) estimate the effects, and filtering and high-frequency roll-off help. Quantization can be approximated as noise with variance $\delta^2/12$ ($\delta$ = quantization level). Friction typically generates oscillations limiting performance (quantization can too), and nonlinear friction compensation can reduce them.

**Example 14.14 (friction in the cart–pendulum).**
- Coulomb friction: $F=-\mu_fM_tg\,\mathrm{sgn}(v)$ \tag{14.34}, $\mu_f=0.001$. With the slower-pole state feedback from Example 7.7, simulation shows oscillations with period $T_p=37$ s and cart-velocity amplitude $A\approx0.52$ m/s, far from sinusoidal (Fig. 14.14a) (p. 14-28).
- Physical argument: the pendulum falls; the cart stays still until the control force exceeds friction; then the cart moves and the cycle repeats (p. 14-29).
- Describing-function analysis (after reducing Fig. 14.13a to Fig. 14.13b): the friction block has
$$N(a)=\frac{4\mu_fM_tg}{a\pi}\tag{14.35}$$
  ($a$ = velocity amplitude). The linear block from friction force $F$ to velocity $v$ is
$$G(s)=\frac{0.01837s^3-0.08s}{s^4+1.046s^3+0.9109s^2+0.2552s+0.03781}\tag{14.36}$$
  from $\dot x=(A-BK)x+BF$, $v=(0\ 0\ 1\ 0)x$.
- Oscillation condition $G(i\omega)N(a)=-1$: the Nyquist curve of $G$ meets $-1/N(a)$ at $\omega=0.21$ with $1/N(a)=0.39$. This gives $T_p=2\pi/0.21=30$ s and $a=4\times0.39\,\mu_fM_tg/\pi=0.43$ m/s. The gap to the simulated 37 s and 0.52 m/s is attributed to the sinusoid assumption (p. 14-29, 14-30).

### 14.7 Further reading (p. 14-30)
The text credits Bode with coining "non-minimum phase" and recommends Stein's Bode Lecture paper on unstable poles. The maximum-modulus section is based on [RÅ15], the loop-shaping section on [Åst00]. The pole-placement rules are "not widely known". Actuator limits can be explored with optimal control theory (p. 14-30). Exercises 14.1–14.15 follow (p. 14-30 to 14-33).

## Toy example
(Ours, not from the text.) A process has a RHP zero at $z=3$ and a RHP pole at $p=1$, with a controller having no RHP poles or zeros.

1. Crossover bound from a RHP zero, using (14.10) and (14.11). Take $\varphi_m=\pi/3$, $n_{gc}=-1$. Then $\bar\varphi_{ap}=\pi-\pi/3-\pi/2=\pi/6$. So $\omega_{gc}\le3\tan(\pi/12)=3\times0.268=0.80$ rad/s.
2. Crossover bound from the pole (14.12), using the same $\bar\varphi_{ap}=\pi/6$: $\omega_{gc}\ge1/\tan(\pi/12)=1/0.268=3.73$ rad/s. This conflicts with step 1, which already suggests robust control is hard here. (These two bounds are for the all-pass factor of the pole and zero treated separately, as in Examples 14.3 and 14.4.)
3. Maximum sensitivity from (14.25): $M_s\ge(3+1)/|3-1|=2$. If the zero were at 1.5: $M_s\ge2.5/0.5=5$, and closer pairs are worse.
4. Waterbed (a separate idealised case with no RHP poles). Suppose (idealised) $|S|=0.5$ on $[0,2]$ and $|S|=M$ on $[2,4]$, $|S|=1$ elsewhere. Natural log: $2\ln0.5=-1.386$. For $\int\log|S|\,d\omega=0$ we need $2\ln M=1.386$, so $M=e^{0.693}=2$. Halving the disturbance effect over a band forces a doubling elsewhere.

## Concepts
- [[stabilizability]] (new) — all unstable eigenvalues can be moved by feedback; weaker than reachability (p. 14-2, 14-3)
- [[strong-stabilizability]] (new) — stabilizable by a stable controller; fixed by the pattern of RHP real poles and zeros (Thm 14.1, 14.2) (p. 14-2, 14-3)
- [[pbh-test]] (new) — rank test of $(A-sI\ \ B)$ for reachability or stabilizability (p. 14-3)
- [[controllability (reachability)]] — needed for arbitrary state-feedback eigenvalues (p. 14-2)
- [[state feedback / pole placement]] — choosing closed-loop poles; this unit adds rules for choosing them robustly (p. 14-20, 14-25)
- [[non-minimum-phase]] (new) — poles or zeros in the RHP, or delays; extra phase lag at the same gain (p. 14-10)
- [[all-pass-factor]] (new) — the unit-gain factor $P_{ap}$ carrying the non-minimum phase lag (p. 14-10)
- [[delay (dead time)]] — adds phase lag, with effects similar to a RHP zero; approximated by Padé (p. 14-5, 14-14)
- [[sensitivity-function]] (new) — $S=1/(1+PC)$; amplification of disturbances; $M_s=\max|S|$ (p. 14-5)
- [[complementary-sensitivity-function]] (new) — $T=PC/(1+PC)$, with $S+T=1$ (p. 14-15)
- [[bode-integral-formula]] (new) — $\int_0^\infty\log|S|\,d\omega=\pi\sum p_k$; the waterbed effect (p. 14-6)
- [[gain-crossover-frequency-inequality]] (new) — (14.10): all-pass lag at crossover is bounded by the phase budget (p. 14-11)
- [[maximum-modulus-principle]] (new) — a bounded analytic function's maximum on the closed RHP occurs on the imaginary axis; basis of the $M_s$, $M_t$ bounds (p. 14-15)
- [[robustness]] — here measured by $M_s$, $M_t$, phase and gain margin (p. 14-5, 14-23)
- [[stability]] — robust control of a system with RHP poles needs a sufficiently high gain crossover frequency (p. 14-13)
- [[describing-function]] (new) — approximate nonlinear analysis assuming sinusoidal signals; indicates a possible friction oscillation (p. 14-29)
- [[actuator-saturation]] (new) — limits on amplitude or rate of the control signal; handled with sector bounds or minimum-time analysis (p. 14-26 to 14-28)

## Canonical instances
- [[vehicle-steering]] — output placement removes a RHP zero (Ex. 14.1); slow-zero cancellation fixes a fragile design (Ex. 14.12) (p. 14-4, 14-22)
- [[x29-aircraft]] — Bode integral gives $M_s\approx1.75$ for $p=6$, $\omega_1=3$, $\omega_a=40$ (p. 14-7, 14-8)
- [[balance-system]] — cart-position output has $p=2.68$, $z=2.09$, hard to control; friction-induced oscillations (Ex. 14.7, 14.14) (p. 14-14, 14-28)
- [[bicycle-rear-steering]] — minimum rideable speed from $z/p$ (p. 14-19)
- [[voice-coil-servo]] — minimum-time move with current and velocity limits (p. 14-26)
- [[umea-ferry-grounding]] — actuator power too low against wind load (p. 14-26)

## Bridges (candidates)
- [structural-analogy] Waterbed effect (conservation of ∫log|S|) ↔ conservation laws in physics: a fixed total that can only be redistributed — one line why: the constraint is an invariant, but this one is an analytic-function identity.
- [same-math] Bode relations between gain slope and phase (used in (14.10)) ↔ signal processing: Hilbert-transform relation between log-magnitude and phase of minimum-phase systems — shared mathematics is the relation of real and imaginary parts of an analytic log function (not stated in this unit).
- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7).
- [metaphor] Pole/zero cancellation as "designing the controller around the process" ↔ engineering co-design of plant and controller (p. 14-2).

## Questions this raises
- How can a process with $p>z$ be controlled robustly, as the text says is possible with "more clever design techniques" (p. 14-20)?
- The text warns that exact cancellation of poles and zeros may lose robustness under model uncertainty. How should one quantify this?
- How tight are the bounds in Table 14.1? Are they attained by some controller, or only lower bounds?
- How would measurement noise and the sensitivity limits combine into a single bandwidth bound (compare Exercise 14.15)?

## Exercises worth doing
- Ex. 14.1 (p. 14-30) — PI control of a pole/zero pair, compare $M_s$ with the bound, both cases $z>p$ and $z<p$, plus root loci — difficulty: hard
- Ex. 14.2 (p. 14-31) — shows why $sL(s)\to0$ matters in Bode's formula (here $sL\to k$) — difficulty: easy
- Ex. 14.3 (p. 14-31) — generalise Bode's formula to $\lim sL(s)=a$, result $\pi\sum p_k-a\pi/2$ — difficulty: medium
- Ex. 14.6 (p. 14-31) — stability range and best margin $s_m=|p-z|/(p+z)$ for a pole/zero pair — difficulty: medium
- Ex. 14.8 (p. 14-32) — X-29 margins from $p=6$, $z=26$ — difficulty: medium
- Ex. 14.14 (p. 14-32) — verify the minimum-time curves of Fig. 14.12 by hand — difficulty: easy

## Reading notes
- Page labels give no printed number, but the page images show headers "14-N" (chapter-page numbers). Citations use these as "p. 14-N". Offset: printed 14-N = pdf (N + 464); pdf 498 is a nearly empty page with only the running header.
- Eq. (14.2): printed with $s$ in the matrix but "$\lambda\in\mathbb C$" in the text. "Re s > 0 for strict stabilizability" is printed as written; the wording is unusual.
- Theorem 14.1 as printed does not restrict the zeros $z_k$ to the RHP or to real zeros. Compare with Theorem 14.2, which speaks of real zeros in $\operatorname{Re}s\ge0$. On p. 14-3 Theorem 14.2 is credited to Doyle, Frances and Tannenbaum; on p. 14-20 the same criterion is credited to Youla and stated without the word "real".
- p. 14-5: the subscript of the second Padé formula is garbled in print (a stray parenthesis instead of $2$); it should read $G_2(s)$.
- Example 14.2: the formula $M_s=e^{(\pi p+\omega_1)/\omega_a}$ with $p=6$, $\omega_1=3$, $\omega_a=40$ evaluates to $e^{0.546}\approx1.73$; the text prints 1.75. The 33° phase-margin estimate is unaffected at this precision.
- Example 14.5: the process is printed $P(s)=\frac{a-z}{s-p}$; the numerator should be $s-z$ (the all-pass factor following it uses $z-s$).
- p. 14-14: the delay all-pass factor is printed $e^{\tau s}$; Example 14.6 uses $e^{-\tau s}$.
- Example 14.7: the all-pass lag is given as 166°. With (14.14), $p=2.68>z=2.09$, I get $4\arctan\sqrt{p/z}\approx194^\circ$ at $\omega=\sqrt{pz}$. 166° equals the Exercise 14.7 formula $2\arctan(2\sqrt{pz}/|z-p|)$ with $|z-p|$. The conclusion (no reasonable margin) holds either way. The numerator of $H_{yF}$ is printed with $mgl^2$; from $H_{qF}-rH_{\theta F}$ it should be $mgl$.
- Exercise 14.7: the formula for $\varphi_{ap2}$ is printed with $2p-p\tau$ inside the arctan, where Example 14.6 has $2-p\tau$.
- Example 14.11: the text says the peak is "approximately $\omega=a/\sqrt{p_1p_2}\approx10$". Fig. 14.9a shows a peak of roughly 4 in magnitude, so this probably refers to a magnitude estimate. Also, the "$p_2=a$" fix is followed by a figure with $a<p_1<p_2$.
- The text promises (p. 14-25) a more detailed treatment of exact pole/zero cancellation "below"; no such discussion appears in these pages.
- Fig. 14.12 caption says full acceleration lasts until $t=5$ ms and braking starts at 10 ms. The plots and (14.33) with the stated numbers give about 4 ms and 11 ms (total 15 ms).
- Ex. 14.10's text of the inequality for $\omega_{tc}$ is printed as an upper bound ($\omega_{tc}\le\ldots$) in (14.37), while Table 14.1 and Section 14.4 give a lower bound ($\omega_{tc}\ge\ldots$). Not resolved here.
- Table 14.1's delay row ($M_t\ge e^{p\tau}$, $M_s\ge e^{p\tau}-1$) is not derived in these pages.
- The chapter opens with a quotation about a front-drive rear-steering recumbent bicycle (Whitt and Wilson, *Bicycling Science*, 1997).
