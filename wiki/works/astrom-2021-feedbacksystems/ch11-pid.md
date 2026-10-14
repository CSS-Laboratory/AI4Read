---
id: astrom-2021-feedbacksystems/ch11-pid
work: astrom-2021-feedbacksystems
unit: "11 PID Control"
pages: 11-1 to 11-26
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
# PID Control

## L0 — One line
PID control adds three terms (present error, accumulated error, predicted error), and the integral term guarantees zero steady-state error if a steady state exists. Practical use also needs tuning rules, anti-windup, derivative filtering and careful implementation.

## L1 — The gist (≤ 120 words)
Most regulatory controllers in industry use PID control (one survey found 97%). The chapter asks how to pick the three gains, and how to build a controller that works with real actuators and computers. The answers: choose gains by pole placement on simple low-order models, or tune empirically (Ziegler–Nichols, FOTD rules, relay experiments). Integral action removes steady-state error but causes "windup" when the actuator saturates. An extra feedback path (anti-windup) fixes this. Filtering the derivative, weighting the setpoint, and careful discrete-time code make the idealized law usable. This matters because, in hierarchical advanced control systems, high-level controllers give setpoints to PID loops in a lower layer.

**Prerequisites:** Laplace transfer functions and loop transfer function; closed-loop poles, damping ratio, natural frequency; Nyquist and Bode plots; first-order and second-order systems; basic sampling.

## L2 — Key ideas (5–10 bullets)
- The ideal PID law is the sum of a proportional, an integral and a derivative term, $u=k_pe+k_i\int e+k_d\,\dot e$; it is parameterized by gains or by time constants $T_i,T_d$ (p. 11-2, 11-3).
- Integral action forces $e\to0$ whenever a steady state exists. The proof (with $k_i\neq0$) does not assume a linear or time-invariant process, but it does assume an equilibrium (p. 11-4).
- For a first-order process, PI gains place the two closed-loop poles exactly. Integral gain $k_i$ measures load-disturbance rejection through the integrated error (p. 11-5, 11-8).
- Empirical tuning (Ziegler–Nichols) needs only two numbers from a step or oscillation experiment. It is simple but gives low robustness. Rules based on a first-order-plus-time-delay (FOTD) model improve on it, and relay autotuning automates the oscillation experiment (p. 11-11 to 11-15).
- Actuator saturation breaks the loop, and the integrator keeps accumulating ("windup"). Feeding back the difference between the commanded and saturated signal avoids this (p. 11-15, 11-16).
- Windup protection can be analysed with the circle criterion, a stability test for a linear block with a sector-bounded nonlinearity (p. 11-17). The same extra feedback path also gives switching between manual and automatic mode without transients (p. 11-18).
- Practical PID needs a filtered derivative, setpoint weighting ($\beta,\gamma$) and a discretization that stays stable (p. 11-19, 11-20, 11-23).

## L3 — Walkthrough

### Opening and 11.1 Basic control functions (p. 11-1 to 11-7)

**Why PID matters.** A survey of over 11,000 controllers in refining, chemicals, and pulp and paper found that 97% of regulatory controllers use PID (p. 11-1). In 100+ boiler-turbine units in Guangdong, 94.4% were PI, 3.7% PID and 1.9% advanced (p. 11-1). Derivative action is used in only about 4% of controllers. For many systems, prediction by linear extrapolation amplifies measurement noise. Its benefit is significant mainly for processes that allow large gains, for example temperature control with low-noise sensors (p. 11-1, 11-2). Advanced controllers sit above PID loops in a hierarchy and give them setpoints. This is why PID has not lost importance (p. 11-2). The authors also say there is growing evidence of PID in biological systems (p. 11-2).

**Observer vs PID.** An observer-based controller predicts the future state with a model. A PID controller uses linear extrapolation of the measured output. A PI controller uses no prediction (p. 11-1).

**Ideal PID with error feedback** (Figure 11.1a) (p. 11-2):
$$u=k_pe+k_i\int_0^te(\tau)\,d\tau+k_d\frac{de}{dt}=k_p\Big(e+\frac1{T_i}\int_0^te(\tau)\,d\tau+T_d\frac{de}{dt}\Big)\tag{11.1}$$
Here $e=r-y$. In Figure 11.1a all three terms act on $e$. In Figure 11.1b (two degrees of freedom) integral action acts on the error, but P and D act only on $y$ (p. 11-2). The reference $r$ is called the setpoint in PID literature. Figure 11.1a has no feedforward term (p. 11-2).

**Parameters.** $T_i=k_p/k_i$ (integral time) and $T_d=k_d/k_p$ (derivative time). The proportional band is $PB=100/k_p$ (p. 11-3).

**Pure proportional control.** For a unit reference step, the transfer function from reference to error is
$$G_{er}(s)=\frac1{1+C(s)P(s)}=\frac1{1+k_pP(s)}\tag{11.2}$$
If the closed loop is stable, the steady-state error is $G_{er}(0)=1/(1+k_pP(0))$ (p. 11-3). For $P=1/(s+1)^3$ (Figure 11.2a), gains $k_p=1,2,5$ give errors 0.5, 0.33, 0.17. The system becomes more oscillatory as gain rises and is unstable at $k_p=8$. The initial control value equals $k_p$ (p. 11-3, 11-4).

**Feedforward fix.** The law $u=k_pe+u_{ff}$ (11.3) with $u_{ff}=r/P(0)=k_fr$ gives exact steady state if there are no disturbances. It needs exact $P(0)$ (p. 11-4). The term $u_{ff}$ is called the reset value and was adjusted manually in early controllers. Multiplying the reference by $1+k_pP(0)$ also needs exact $P(0)$ (p. 11-4).

**Integral action: general proof** (p. 11-4). Take (11.1) with $k_i\neq0$. Assume $u\to u_0$ and $e\to e_0$. Then
$$u_0=k_pe_0+k_i\lim_{t\to\infty}\int_0^te(t)\,dt .$$
The right side is not finite unless $e\to0$. So $e_0=0$. Hence, if a steady state exists, the error is zero. This is sometimes called "the magic of integral action". The proof does not assume a linear or time-invariant process, but it does assume an equilibrium (p. 11-4). Integral action is better than feedforward here because feedforward needs precise process knowledge (p. 11-4).

**Frequency view.** $C(s)=k_p+k_i/s+k_ds$ (11.4). Since $C(0)=\infty$, (11.2) gives $G_{er}(0)=0$ (p. 11-4).

> **Intuition note.** The integral keeps changing as long as any error remains (with $k_i\neq0$). So the controller output can only stop changing when the error is exactly zero. No linearity is needed, but the loop must settle to a steady state.

**Automatic reset** (Figure 11.3a). The controller output is low-pass filtered and fed back with positive gain. Block-diagram algebra gives
$$G_{ue}=k_p\frac{1+sT_i}{sT_i}=k_p+\frac{k_p}{sT_i},$$
which is a PI controller (p. 11-4, 11-5). (Added step: $u=k_pe+u/(1+sT_i)\Rightarrow u\,\frac{sT_i}{1+sT_i}=k_pe$.) It was an early implementation because a low-pass filter was easier to build than an integrator (p. 11-4).

**Effect of $k_i$** (Figure 11.2b, $k_p=1$, $k_i=0,0.2,0.5,1$). $k_i=0$ gives a 50% steady-state error. Larger $k_i$ converges faster but is more oscillatory (p. 11-5).

**Load disturbance and integrated error.** Take a stable loop at rest and apply a unit step load disturbance at the process input. The output returns to zero and the controller output settles at a value that compensates for the disturbance. Because $e\to0$, (11.1) gives $u(\infty)=k_i\int_0^\infty e\,dt$. So $IE=\int_0^\infty e\,dt$ is inversely proportional to $k_i$ and measures disturbance attenuation. Too large a $k_i$ gives oscillation, poor robustness and possibly instability (p. 11-5).

**Derivative action.** $u=k_pe+k_d\dot e=k_p(e+T_d\dot e)=:k_pe_p$. Here $e_p$ is a prediction of the error at $t+T_d$ by linear extrapolation (p. 11-5). Derivative action can be built as the signal minus its low-pass-filtered version (Figure 11.3b):
$$G_{ue}(s)=k_p\Big(1-\frac1{1+sT_d}\Big)=k_p\frac{sT_d}{1+sT_d}=\frac{k_ds}{1+sT_d}\tag{11.5}$$
For $|s|\ll1/T_d$, $G_{ue}\approx k_pT_ds=k_ds$. At high frequency it acts as constant gain $k_p$. So it is a filtered derivative (p. 11-6). In Figure 11.2c ($k_p=2.5,k_i=1.5,k_d=0,1,2,4$), more $k_d$ gives more damping. A reference step makes the derivative term an impulse, which Figure 11.1b avoids (p. 11-6).

**Biology.** Disturbance attenuation by feedback in biology is often called adaptation. Feedback with integral action is called perfect adaptation. P, I and D action arise from interacting dynamic subsystems. PI action can arise from the interaction of several hormones (p. 11-6).

**Example 11.1 (PD action in the retina)** (p. 11-6, 11-7). Cones receive light $u$ and excite horizontal cells. Horizontal cells give inhibitory feedback to the cones. With average pulse rates $x_1$ (cones), $x_2$ (horizontal cells):
$$\frac{dx_1}{dt}=\frac1{T_c}(-x_1-kx_2+u),\qquad\frac{dx_2}{dt}=\frac1{T_h}(x_1-x_2).$$
With $k=4$, $T_c=0.025$, $T_h=0.08$, the step response has a large initial peak followed by a lower constant value, typical of proportional plus derivative action (p. 11-7).

### 11.2 Simple controllers for complex systems (p. 11-7 to 11-11)

State-space design makes the controller order follow the model order (p. 11-7). Low-order models can come from first principles. First-order: one storage variable, e.g. car velocity, tank level. Second-order: two storage variables, e.g. car position and velocity, two connected tanks (p. 11-7).

**Integral control.** Any stable system can be controlled by an integral controller if the closed-loop requirements are modest. Approximate $P\approx K=P(0)$ at low frequency. Then $L=Kk_i/s$ and the closed-loop characteristic polynomial is $s+Kk_i$. For desired closed-loop time constant $T_{cl}$: $k_i=1/(T_{cl}P(0))$. A reasonable criterion is $T_{cl}>T_{ar}$, where the average residence time is $T_{ar}=-P'(0)/P(0)$ (p. 11-7).

**Higher performance.** Use $P(s)\approx P(0)/(1+sT_{ar})$ with
$$k_i=\frac1{2P(0)T_{ar}}\tag{11.6}$$
Then $L(s)\approx\dfrac1{2sT_{ar}(1+sT_{ar})}$ and the closed-loop poles are $s=(-0.5\pm0.5i)/T_{ar}$. With the approximations of Table 7.1, $\omega_0=1/(T_{ar}\sqrt2)$. Rise time is $3.1T_{ar}$, settling time $7.9T_{ar}$, overshoot 4% (p. 11-8). (Added step: $1+L^{-1}$ gives $2T_{ar}^2s^2+2T_{ar}s+1=0$.)

**Example 11.2 (AFM, integral control)** (p. 11-8). The model is $P(s)=\dfrac{a(1-e^{-s\tau})}{s\tau(s+a)}$, with $a=\zeta\omega_0$, $\tau=2\pi n/\omega_0$ and gain normalized to 1. It has a delay term in the numerator. $P(0)=1$ and $P'(0)=-\tau/2-1/a=-(2+a\tau)/(2a)$. At low frequency $L(s)\approx k_i(P(0)+sP'(0))/s=k_iP'(0)+k_iP(0)/s$. Setting $k_i=-1/(2P'(0))$ by rule (11.6) gives good low-frequency performance and good margins (Figure 11.5). So a simple integral controller works despite the delay term (p. 11-8, 11-9).

**PI pole placement for a first-order process.** For $P=b/(s+a)$, the closed-loop polynomial is $s(s+a)+bk_ps+bk_i=s^2+(a+bk_p)s+bk_i$. Matching $p(s)=s^2+a_1s+a_2$ gives
$$k_p=\frac{a_1-a}{b},\qquad k_i=\frac{a_2}{b}\tag{11.7}$$
For a slower closed loop than open loop: $a_1=a+\alpha$, $a_2=\alpha a$, with $\alpha<a$ (p. 11-8, 11-9). For a faster one: $a_1=2\zeta_c\omega_c$, $a_2=\omega_c^2$. The choice of $\omega_c$ is limited by the highest frequency where the model is valid. It is also limited by actuator saturation, since large $\omega_c$ needs fast actions (p. 11-9).

**Example 11.3 (cruise control, PI)** (p. 11-9, 11-10). The model is
$$\frac{d(v-v_e)}{dt}=-a(v-v_e)-b_g(\theta-\theta_e)+b(u-u_e)\tag{11.8}$$
with $a=0.01$, $b=1.32$, $b_g=9.8$, $v_e=20$, $\theta_e=0$, $u_e=0.1687$. The open-loop time scale is $1/a\approx100$ s. Choose a second-order closed loop with $\zeta_c,\omega_c$ and gains from (11.7). A hill of $4^\circ$ starts at $t=5$ s (Figure 11.6). $\zeta_c\ge1$ gives no overshoot in $v$. A larger $\omega_c$ gives a smaller largest velocity error but faster control action. A reasonable $\omega_c$ is 0.5–1.0. Even $\omega_c=0.2$ gives a largest error of only about 1.3 m/s (p. 11-10).

**Higher-order cases.** A PI controller can control a second-order process, but the closed-loop pole locations are restricted. A PID controller can place the poles of a second-order process arbitrarily (Exercise 11.2) (p. 11-10). With a high-order model, one can attempt to place only a few dominant poles; an integral controller has one parameter and can position one pole. For the integral controller $L=k_iP(s)/s$, the roots solve $s+k_iP(s)=0$. Requiring $s=-a$ gives $k_i=a/P(-a)$. This pole is dominant if $a$ is smaller than the magnitude of the other closed-loop process poles (p. 11-11).

### 11.3 PID tuning (p. 11-11 to 11-15)

PID has few parameters, so empirical tuning methods exist (p. 11-11).

**Ziegler–Nichols (1940s)** (p. 11-11, 11-12).
- *Step response method.* Do a bump test: bring the process to steady state, change the input, then scale the output to a unit step. Draw the steepest tangent. Its intercepts with the axes give $a$ and $\tau$ (Figure 11.7a). $\tau$ approximates the time delay and $a/\tau$ is the steepest slope. One only needs to wait until the inflection point.
- *Frequency method.* Set $k_i=k_d=0$ and raise $k_p$ until oscillation. This gives the critical gain $k_c$ and period $T_c$. By the Nyquist criterion, $k_cP(i\omega_c)=-1$ with $\omega_c=2\pi/T_c$, which is the point of the Nyquist curve with 180° phase lag (Figure 11.7b).
- The rules came from extensive simulation: controllers were tuned manually for representative processes and then correlated with $a,\tau$.

| Type | $k_p$ | $T_i$ | $T_d$ | | $k_p$ | $T_i$ | $T_d$ |
|---|---|---|---|---|---|---|---|
| P | $1/a$ | | | | $0.5k_c$ | | |
| PI | $0.9/a$ | $\tau/0.3$ | | | $0.45k_c$ | $T_c/1.2$ | |
| PID | $1.2/a$ | $\tau/0.5$ | $0.5\tau$ | | $0.6k_c$ | $T_c/2$ | $T_c/8$ |

(Table 11.1: step response method on the left, frequency response method on the right (p. 11-12).) The methods were simple and widely adopted. Their two drawbacks: they use too little process information, and the closed loops lack robustness (p. 11-12).

**FOTD model** (p. 11-12, 11-13):
$$P(s)=\frac K{1+sT}e^{-\tau s},\qquad\tau_n=\frac\tau{T+\tau}\tag{11.9}$$
$\tau_n\in(0,1)$ is the relative (normalized) delay. Near 0: lag dominated. Near 1: delay dominated. In between: balanced. From a bump test: $K$ is the steady-state step value, $\tau$ is as before, $T_{63}$ is the time to 63% of the steady state, and $T=T_{63}-\tau$. This takes longer than ZN because one must wait for steady state (p. 11-13).

Improved PI rules, based on [ÅH06] (ZN values in parentheses) (p. 11-13):
$$k_p=\frac{0.15\tau+0.35T}{K\tau}\ \Big(\frac{0.9T}{K\tau}\Big),\qquad k_i=\frac{0.46\tau+0.02T}{K\tau^2}\ \Big(\frac{0.27T}{K\tau^2}\Big)\tag{11.10a}$$
$$k_p=0.16k_c\ (0.45k_c),\qquad k_i=\frac{0.16k_c+0.72/K}{T_c}\ \Big(\frac{0.54k_c}{T_c}\Big)\tag{11.10b}$$
The improved formulas typically give lower gains than original ZN (p. 11-13).

**Example 11.4 (AFM, PI tuning)** (p. 11-13, 11-14). The normalized model is $P(s)=\dfrac{1-e^{-sT_n}}{sT_n(s+1)}$ with $T_n=2n\pi\zeta$. For $\zeta=0.002$, $n=20$: the first real-axis crossing is $\mathrm{Re}\,s=-0.0461$ at $\omega_c=13.1$. So $k_c=21.7$ and $T_c=0.48$.

| Rule | $k_p$ | $k_i$ ($T_i$) | Stability margin $s_m$ |
|---|---|---|---|
| ZN | 8.67 | 22.6 (0.384) | 0.31 (small) |
| Modified ZN (11.10b) | 3.47 | 8.73 (0.397) | 0.61 |

The ZN controller gives a large overshoot in the control signal. The modified rule reduces overshoot, and the control signal reaches steady state almost at once (Figure 11.8). A pure integral controller has normalized gain $k_i=1/(2+T_n)=0.44$, more than an order of magnitude smaller than the PI integral gain (p. 11-14).

> **Intuition note.** The FOTD rules use one more fact about the process than ZN does (e.g. the gain $K$). The improved formulas typically give lower gains. In the AFM example the stability margin rises from 0.31 to 0.61, about double.

**Scope of FOTD tuning.** The FOTD-based rules work well for PI. Derivative action has little effect for delay-dominated processes but can give substantial performance for lag-dominated ones. PID tuning for lag-dominated processes cannot be based on the FOTD model (p. 11-14).

**Relay feedback** (p. 11-14, 11-15). Connect the process in a loop with a relay (Figure 11.9a). For many systems the loop oscillates: $u$ is a square wave and $y$ is nearly sinusoidal, 180° out of phase, with period $T_c$. Expand the square wave in a Fourier series. The first harmonic has amplitude $4d/\pi$ ($d$ = relay amplitude). If $a$ is the amplitude of $y$:
$$|P(i\omega_c)|=\frac{\pi a}{4d},\qquad k_c=\frac{4d}{\pi a},\qquad\omega_c=\frac{2\pi}{T_c}.$$
Then apply ZN rules. The experiment can be automated: the relay amplitude is adjusted to keep oscillations small, and the relay is replaced by the PID controller afterwards. It is used in many commercial controllers. An asymmetric relay gives more parameters (p. 11-15).

### 11.4 Integral windup (p. 11-15 to 11-19)

**Mechanism.** Actuators have limits. When the actuator saturates, the loop is effectively open. The error stays nonzero, so the integral term and controller output grow very large. The control signal stays saturated even after the error changes sign, and large transients follow. This is integrator windup (p. 11-15).

**Example 11.5 (cruise control, windup)** (p. 11-15, 11-16). A $6^\circ$ hill at $t=5$ saturates the throttle. The error falls slowly because engine torque is only slightly above that needed. The integral keeps building until $e=0$ at $t\approx25$, yet the controller output is still above the limit. Velocity settles at $t\approx40$, after a large overshoot (Figure 11.10a).

**Avoiding windup** (Figure 11.11) (p. 11-16). Add a feedback path from a model of the saturating actuator. Let $u_a$ be the controller output and $u$ the actuator-model output. The signal $e_s$ ($=u-u_a$, as the figure's sum and the equation below show) is fed to the integrator input through $k_{aw}$. It is zero if there is no saturation. During saturation it drives $e_s\to0$, so the controller output stays close to the limit and responds as soon as the error changes sign. A large $k_{aw}$ gives fast reset, but measurement noise can cause undesirable reset if $k_{aw}$ is too large. A reasonable choice is a multiple of $k_i$. The feedforward input $u_{ff}$ enters before the saturation model, so the scheme also handles saturation due to feedforward (p. 11-16, 11-17).

**Example 11.6.** With anti-windup ($k_{aw}=2$, compared with the integral gain $k_i=0.2$ as printed), the integrator is quickly reset and the overshoot is avoided (Figure 11.10b) (p. 11-17).

**Stability with anti-windup.** Redraw the loop as a linear block plus a static saturation. The saturation is sector-bounded with $k_{low}=0$, $k_{high}=1$ in (10.17). The linear part is
$$H(s)=\frac{sP(s)C(s)-k_{aw}}{s+k_{aw}}\tag{11.11}$$
(Exercise 11.12). The circle reduces to the line $\mathrm{Re}\,s=-1$. By the circle criterion the loop is stable if the Nyquist curve of $H$ lies to the right of $\mathrm{Re}\,s=-1$. With describing functions, oscillations may occur if $H(i\omega)$ crosses the negative real axis to the left of $-1$ (p. 11-17).

**Manual control and tracking** (p. 11-18). A switch selects automatic (A) or manual (M) mode (Figure 11.11). In manual mode the feedback through $k_{aw}$ makes $u_a$ track the manual input $u_m$, so there is no transient on switching to automatic. With integrator state $x$ (the text also calls the integrator output $z$):
$$\frac{dx}{dt}=k_i(r-y_f)+k_{aw}(u-u_a),\quad u_a=z-k_py_f-k_d\dot y_f,\quad u=\begin{cases}F(u_a)&\text{automatic}\\F(u_m)&\text{manual}\end{cases}$$
$F$ is the actuator model. Since $k_{aw}$ is typically larger than $k_i$, $u$ tracks $u_m$ (ideally if $k_i(r-y_f)=0$) (p. 11-18).

**General controllers** (Figure 11.12) (p. 11-18, 11-19). For output feedback with state feedback and observer, a saturation sends the observer the commanded instead of the saturated input. The fix is to put an actuator model in front of the observer and feed it the model output. If the observer model is designed so that the process actuator never saturates, the loop is a static actuator-model block plus a linear block
$$H(s)=K\big(sI-A+LC\big)^{-1}\big(B+LC[sI-A]^{-1}B\big)\tag{11.12}$$
Here $K$ is the feedback gain matrix and $L$ is the Kalman-filter gain matrix. (The bracket grouping is reconstructed from a garbled layout; see Reading notes.) With a simple saturation, $k_{low}=0$, $k_{high}=1$. The circle criterion then says the loop is stable if the Nyquist plot of $L(i\omega)$ is right of $\mathrm{Re}\,z=-1/k_{high}=-1$ and the winding number condition holds (p. 11-19). Manual control and tracking can be built the same way (p. 11-19).

> **Intuition note.** Windup is the integrator "winding up" while the actuator cannot respond. Anti-windup gives the integrator a second input that is nonzero only during saturation. It quickly resets the integrator so that the controller output is kept close to the actuator limit.

### 11.5 Implementation (p. 11-19 to 11-23)

**Filtering the derivative.** An ideal derivative has high gain at high frequency, so noise causes large control variations. Replace $k_ds$ by $k_ds/(1+sT_f)$, with $T_f=T_d/N$ and typically $N$ in the range 5–20. The implementation of Figure 11.3b automatically filters, with $N=1$ (p. 11-19). Alternatively, filter the measurement with a second-order filter:
$$C(s)=k_p\Big(1+\frac1{sT_i}+sT_d\Big)\frac1{1+sT_f+(sT_f)^2/2}\tag{11.13}$$
The filter box $G_f(s)$ in Figure 11.11 has the dynamics
$$\frac d{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}0&1\\-2T_f^{-2}&-2T_f^{-1}\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}+\begin{pmatrix}0\\2T_f^{-2}\end{pmatrix}y\tag{11.14}$$
The states are $x_1=y_f$ and $x_2=dy_f/dt$. The second-order filter also gives good high-frequency roll-off, which improves robustness (p. 11-19, 11-20).

**Setpoint weighting.** In Figure 11.2c the initial peak in $u$ comes from the derivative of the reference. An intermediate form between the two configurations of Figure 11.1 is
$$u=k_p(\beta r-y)+k_i\int_0^t\big(r(\tau)-y(\tau)\big)d\tau+k_d\Big(\gamma\frac{dr}{dt}-\frac{dy}{dt}\Big)\tag{11.15}$$
Integral action must act on the error so that the error goes to zero in steady state. Different $\beta,\gamma$ give the same response to load disturbances and measurement noise, but different responses to the reference. This is two-degree-of-freedom action. $\beta=\gamma=0$ is an I-PD controller (p. 11-20).

**Example 11.7 (cruise control with setpoint weighting)** (Figure 11.13: $k_p=0.74$, $k_i=0.19$, $\beta=0,0.5,1$, $\gamma=0$). With $\beta=1$ there is a velocity overshoot, and the throttle starts near saturation. With $\beta=0$ there is no overshoot and the control signal is much smaller, giving better drive comfort. Typically $\beta\in[0,1]$, and $\gamma$ is normally zero to avoid large transients (p. 11-20).

**Operational amplifiers.** For an op-amp circuit the transfer function is $-Z_2/Z_1$ (approximation (4.14) with impedances). PI circuit (Figure 11.14a): $Z_1=R_1$, $Z_2=R_2+1/(sC_2)$. Then $Z_2/Z_1=R_2/R_1+1/(R_1C_2s)$, so $k_p=R_2/R_1$ and $k_i=1/(R_1C_2)$ (p. 11-21). PID circuit (Figure 11.14b): $Z_1=\dfrac{R_1}{1+R_1C_1s}$, $Z_2=R_2+\dfrac1{C_2s}$, and
$$\frac{Z_2}{Z_1}=\frac{(1+R_1C_1s)(1+R_2C_2s)}{R_1C_2s},$$
which gives (p. 11-22)
$$k_p=\frac{R_1C_1+R_2C_2}{R_1C_2},\quad T_i=R_1C_1+R_2C_2,\quad T_d=\frac{R_1R_2C_1C_2}{R_1C_1+R_2C_2}.$$

**Computer implementation.** Loop: wait for clock; read sensor; compute output; send output; update state; repeat. Sending the output as soon as it is computed and doing updates afterward minimizes delay. The authors say this is seldom done in commercial systems (p. 11-22). For the controller of Figure 11.11, with $u=\mathrm{sat}(u_a)$ and sampling instants $t_{k+1}=t_k+h$:
$$P(t_k)=k_p\big(\beta r(t_k)-y(t_k)\big)\tag{11.16}$$
$$I(t_{k+1})=I(t_k)+k_ih\,e(t_k)+\frac h{T_{aw}}\big(\mathrm{sat}(u_a)-u_a\big),\qquad T_{aw}=\frac h{k_{aw}}\tag{11.17}$$
The derivative term obeys $T_f\dot D+D=-k_d\dot y$. A backward difference gives
$$T_f\frac{D(t_k)-D(t_{k-1})}h+D(t_k)=-k_d\frac{y(t_k)-y(t_{k-1})}h$$
$$D(t_k)=\frac{T_f}{T_f+h}D(t_{k-1})-\frac{k_d}{T_f+h}\big(y(t_k)-y(t_{k-1})\big)\tag{11.18}$$
The factor $T_f/(T_f+h)$ is nonnegative and less than 1 for all $h>0$, which guarantees a stable difference equation (p. 11-22, 11-23). The pseudocode precomputes `bi=ki*h`, `ad=Tf/(Tf+h)`, `bd=kd/(Tf+h)`, `br=h/Taw`. In each cycle it computes `P`, `D=ad*D-bd*(y-yold)`, `ua=P+I+D` and `u=sat(ua,ulow,uhigh)`. It then writes `u` to the output and updates `I=I+bi*(r-y)+br*(u-ua)` and `yold=y`. It has three states: `yold`, `I`, `D`. The latency is four multiplications, four additions and one `sat` evaluation. Fixed-point arithmetic on a PLC is possible. Here saturation is applied inside the controller instead of measuring the actuator output as in Figure 11.11 (p. 11-23).

### 11.6 Further reading (p. 11-24)
Sources cited include history (Bennett, Mindel), industrial perspectives, windup ([ZT11]), and Åström–Hägglund. The industrial perspectives all mention that a significant fraction of PID controllers are poorly tuned. The book [O'D06] lists more than 1730 tuning rules. The ZN rules (1942) came from experiments with pneumatic simulators and Bush's differential analyzer. One application is explaining popular monetary policy rules (p. 11-24).

## Toy example (ours, not from the text)
Plant $\dot y=-y+u$ (so $P(s)=1/(s+1)$). Unit reference step $r=1$. Euler step $h=0.5$: $e=r-y$, $u=k_pe+I$, $y_{new}=y+h(-y+u)$, $I_{new}=I+hk_ie$.

*P only, $k_p=1$* (steady state needs $\dot y=0$, i.e. $y=u=e$, so $y=0.5$):
- Step 0: $e=1$, $u=1$, $y=0+0.5(0+1)=0.5$.
- Step 1: $e=0.5$, $u=0.5$, $y=0.5+0.5(-0.5+0.5)=0.5$. It stays at 0.5, with a steady-state error of 0.5, which equals $1/(1+k_pP(0))$ (p. 11-3 formula).

*PI, $k_p=1$, $k_i=1$:*

| k | $y$ | $I$ | $e$ | $u$ | $y_{new}$ | $I_{new}$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | $1+0=1$ | $0+0.5(0+1)=0.5$ | $0+0.5\cdot1=0.5$ |
| 1 | 0.5 | 0.5 | 0.5 | $0.5+0.5=1$ | $0.5+0.5(-0.5+1)=0.75$ | $0.5+0.25=0.75$ |
| 2 | 0.75 | 0.75 | 0.25 | $0.25+0.75=1$ | $0.75+0.5(0.25)=0.875$ | $0.75+0.125=0.875$ |
| 3 | 0.875 | 0.875 | 0.125 | $0.125+0.875=1$ | $0.875+0.5(0.125)=0.9375$ | $0.875+0.0625=0.9375$ |

$y$ and $I$ move toward 1. The error halves each step. The integrator ends up supplying the whole control value $u=1$ that the plant needs, so $e\to0$. This is the "magic of integral action": no knowledge of $P(0)$ was used.

## Concepts
- [[PID control]] — control signal as sum of P (present error), I (past errors), D (predicted error) terms, eq. (11.1) (p. 11-2)
- [[integral action]] — forces zero steady-state error if a steady state exists; no linearity assumed (p. 11-4)
- [[reference (set point)]] — command signal $r$, called setpoint in PID literature (p. 11-2)
- [[error signal]] — $e=r-y$ (p. 11-2)
- [[feedforward]] — term $u_{ff}=k_fr$ that gives the desired steady state but needs exact $P(0)$ (p. 11-4)
- [[gain]] — $k_p,k_i,k_d$; time-constant form $T_i,T_d$ (p. 11-2, 11-3)
- [[delay (dead time)]] — in the FOTD model, $\tau$; relative delay $\tau_n$ classifies lag, balanced or delay dominated (p. 11-13)
- [[robustness]] — ZN tuning lacks it; in the AFM example the modified rule raises the stability margin (p. 11-12, 11-13)
- [[stability]] — loop stability tested via the circle criterion for anti-windup (p. 11-17)
- [[Nyquist criterion]] — gives the critical point used by the ZN frequency method (p. 11-12)
- [[observer (state estimator)]] — observer-based control predicts the state with a model, unlike PID's linear extrapolation (p. 11-1)
- [[integrator-windup]] (new) — integral term grows during actuator saturation, causing long transients (p. 11-15)
- [[anti-windup]] (new) — feedback of $u-u_a$ through $k_{aw}$ to the integrator (p. 11-16)
- [[ziegler-nichols-tuning]] (new) — empirical rules from $(a,\tau)$ or $(k_c,T_c)$ (p. 11-12)
- [[fotd-model]] (new) — first-order-plus-time-delay model $Ke^{-\tau s}/(1+sT)$ (p. 11-12)
- [[relay-autotuning]] (new) — relay-induced oscillation gives $k_c,T_c$ automatically (p. 11-14)
- [[setpoint-weighting]] (new) — $\beta,\gamma$ in (11.15); gives two-degree-of-freedom PID (p. 11-20)
- [[derivative-filtering]] (new) — $k_ds/(1+sT_f)$ or measurement filter to limit noise gain (p. 11-19)
- [[average-residence-time]] (new) — $T_{ar}=-P'(0)/P(0)$, a response-time measure (p. 11-7)

## Canonical instances
- [[cruise-control]] — PI design by pole placement; windup on a steep hill; setpoint weighting (p. 11-9, 11-15, 11-20)
- [[afm-tapping-mode]] — integral control, ZN versus modified ZN PI tuning (p. 11-8, 11-13)
- [[retina-cone-horizontal-cells]] — biological PD action (p. 11-6)
- [[op-amp-pid-circuit]] — PI and PID built from op amps (p. 11-21, 11-22)
- [[boiler-turbine-survey]] — 94.4% PI, 3.7% PID, 1.9% advanced (p. 11-1)

## Bridges (candidates)
- [structural-analogy] Integral action / perfect adaptation ↔ biology: adaptation in sensory systems such as the pupillary reflex — the text links both to feedback with integral action (p. 11-6).
- [same-math] Anti-windup circle-criterion test ↔ nonlinear stability: the sector-bounded nonlinearity test (10.17) applied to a saturation (p. 11-17).
- [structural-analogy] PID's linear extrapolation vs observer prediction ↔ state-space control: both predict, one from a model and one from the signal's slope (p. 11-1).
- [metaphor] PID rules explaining monetary policy ↔ economics: noted as an "unconventional application" (p. 11-24).

## Questions this raises
- How can ZN-style rules be modified (beyond the PI rules given) to deliver a target stability margin, and what do PID rules look like for lag-dominated processes?
- When does the first-order or second-order reduction in 11.2 fail, and how does a high $\omega_c$ interact with robustness (the text defers this to Section 14.5)?
- How does conditional integration (Exercise 11.11) compare with the $k_{aw}$ scheme, and when can it fail?
- How should $N$ (derivative filter) and $k_{aw}$ be chosen jointly, given that noise limits both?

## Exercises worth doing
- Ex. 11.1 (p. 11-24) — derive $G_{yr}$ for both PID structures; shows how structure changes the zeros but not the poles — difficulty: easy
- Ex. 11.2 (p. 11-24) — PI pole placement for a second-order process; shows the constraint that the poles sum to $-a_1$ — difficulty: medium
- Ex. 11.7 (p. 11-25) — closed-loop average residence time $T_{ar}=T_i/(P(0)k_p)$ — difficulty: medium
- Ex. 11.10 (p. 11-26) — simulate windup and anti-windup for $P=1/s$ with $|u|\le1$ — difficulty: easy
- Ex. 11.11 (p. 11-26) — conditional integration phase portrait; warns against ad hoc nonlinearities — difficulty: medium
- Ex. 11.12 (p. 11-26) — stability of anti-windup via circle criterion, $k_{aw}>k_i/k_p$ — difficulty: hard

## Reading notes
- **Page numbers.** The page labels give no printed number, but the page images show running numbers such as "11-3". I cite these as (p. 11-N). Offset: pdf = 374 + N (pdf 375 = p. 11-1; pdf 400 = p. 11-26).
- **Example 11.4 numbers.** With $k_c=21.7$, $T_c=0.48$, Table 11.1b gives $k_p=0.45\cdot21.7\approx9.8$, not the printed 8.67. $k_i=0.54k_c/T_c\approx24.4$ versus the printed 22.6. The printed pair is consistent with $T_i=0.384$, since $8.67/22.6\approx0.384$. I report the printed values. The modified-rule values (3.47, 8.73) do match (11.10b) with $K=1$ (gain normalized to 1).
- **Example 11.6 vs Figure 11.10.** The text gives $k_i=0.2$; the Figure 11.10 caption gives $k_i=0.1$.
- **Notation in the manual-mode equations (p. 11-18).** The state is written $x$ in $dx/dt$, but the integrator output is called $z$ in $u_a=z-\dots$.
- **Eq. (11.12).** The text layer's bracket grouping is garbled. I reconstructed the grouping $K(sI-A+LC)^{-1}(B+LC[sI-A]^{-1}B)$ from the layout. Check it against the book before reuse.
- **Pseudocode (p. 11-23).** The line `daout(ch1)` shows no argument (presumably `u`). The code uses `b` for $\beta$ and has the typo "Initalize". Note also that $br=h/T_{aw}=k_{aw}$ by $T_{aw}=h/k_{aw}$.
- **Wording.** In 11.2 the text says the pole $s=-a$ will be dominant if $a$ is smaller than the magnitude of "the other closed loop process poles". This is a sufficient condition as written, not a "must". L3 keeps that wording.
- **Omitted.** Figure data (Figures 11.6, 11.8, 11.13) are summarized only from captions and text.
