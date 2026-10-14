---
id: astrom-2021-feedbacksystems/ch02-feedback
work: astrom-2021-feedbacksystems
unit: "2 Feedback Principles"
pages: 2-1 to 2-30
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
# Feedback Principles (Åström & Murray, Chapter 2)

## L0 — One line
Negative feedback (a correction that opposes the error between target and output) makes a system less sensitive to disturbances and parameter changes and helps its output follow a target, while positive feedback (a correction that adds to the signal) has complementary properties, and transfer functions give the algebra to analyse both.

## L1 — The gist (≤ 120 words)
The chapter asks what feedback does: the output y is subtracted from a reference r (the target) and the difference drives the controller. Simple models show that negative feedback reduces the effect of disturbances and of parameter changes, and improves how well the output follows the reference. Transfer functions (ratios of polynomials in s describing the input–output response) make the algebra easy. Dynamics left out of the model limit how fast the response can be made. Positive feedback raises gain but can bring high sensitivity, oscillation, or switching memory.

**Prerequisites:** complex numbers (modulus, argument); linear ODEs with constant coefficients; roots of polynomials; derivative of a ratio; basic idea of a block diagram.

## L2 — Key ideas (5–10 bullets)
- **Static model of feedback.** The process is a "saturation" (output equals input up to ±1, then is clipped), and the controller is a gain $k$. Negative feedback widens the *linear range* (the input interval where output is proportional to input) by $k+1$. In the linear range it also divides by $k+1$ both the *sensitivity* (relative output change per relative change in $k$) and the effect of a load disturbance (an external signal added at the process input). The price is a lower closed-loop gain (pp. 2-2 to 2-5).
- **Positive feedback in the static model.** With gain $k<1$ it raises the gain to $k/(1-k)$, but shrinks the linear range by $1-k$ and increases sensitivity. With $k>1$ one input can give several outputs (hysteresis: the output depends on history) (pp. 2-4, 2-5).
- **Transfer functions.** For $u=e^{st}$ the particular solution is $G(s)e^{st}$ with $G=b(s)/a(s)$. Series, parallel and feedback connections then follow by algebra, e.g. $G_1/(1+G_1G_2)$. Stability needs all roots of $a(s)$ to have negative real parts, and Routh–Hurwitz tests this through the coefficients (pp. 2-7 to 2-11).
- **Disturbance attenuation.** For a first-order process, proportional control leaves a steady-state error after a constant disturbance. A PI controller (proportional plus integral of the error; the integral part is called integral action) gives none. Its gains follow from matching the closed-loop polynomial to $s^2+2\zeta_c\omega_c s+\omega_c^2$, where $\omega_c$ sets response speed and the damping ratio $\zeta_c$ sets its shape (pp. 2-12 to 2-16).
- **Unmodeled dynamics.** A larger $\omega_c$ gives better attenuation, but an extra lag $1+sT$ left out of the model gives a stability limit $\omega_c T<2\zeta_c(1+aT)$ (p. 2-16).
- **Reference tracking.** With integral action, $G_{yr}(0)=1$ if the loop is stable. The "two degrees of freedom" controller, where a parameter $\beta$ scales the reference in the proportional term, keeps the disturbance response and gives less overshoot (pp. 2-17 to 2-20).
- **Robustness.** Closing a high-gain integral loop around a nonlinear, variable amplifier gives an almost linear input–output relation. The error is about $\pi^2/(bk_i)$. The usable $k_i$ is limited by unmodeled dynamics (pp. 2-20 to 2-23).
- **Positive feedback in use.** Growth must be limited by nonlinearity. Examples: Hewlett's oscillator, integral action by positive feedback, and a saturation circuit with two stable equilibria (memory, Schmitt trigger) (pp. 2-23 to 2-27).

## L3 — Walkthrough

### Introduction (p. 2-1)
The chapter uses simple static and dynamical models to show four properties of feedback: disturbance attenuation, reference tracking, robustness to uncertainty, and shaping of behaviour (p. 2-1). It can be skipped by readers who want the detailed treatment first (p. 2-1).

### 2.1 Nonlinear Static Models (pp. 2-1 to 2-5)

**Summary claimed by the author (p. 2-1).** Negative feedback increases the range of linearity, improves reference tracking, and reduces the gain and the effects of disturbances and parameter variations. Moderate positive feedback does the opposite: it shrinks the linear range and increases gain. At a critical value the gain is infinite and the system acts like a relay; larger values give hysteretic behaviour. Static models cannot show stability; positive feedback combined with dynamics often gives instability and oscillation (p. 2-1).

**Setup (Fig. 2.1, p. 2-2).** The reference is $r$. The controller input is $e=r-y$, and the controller is a constant gain $k>0$. The load disturbance $v$ enters at the process input. The lower block (±1) selects positive or negative feedback. The process and controller are

$$y=F(x)=\operatorname{sat}(x)=\begin{cases}-1 & x\le -1\\ x & |x|<1\\ 1 & x\ge 1\end{cases},\qquad u=ke. \tag{2.1}$$

The process is linear for $|x|<1$ (the linear range), where its gain is 1 (p. 2-2). With no feedback and $v$ neglected,

$$y=F(kr)=\operatorname{sat}(kr), \tag{2.2}$$

which has gain $k$ and linear range $|r|<1/k$ (p. 2-2).

**Reference response, negative feedback (pp. 2-2, 2-3).** With $v=0$ and the lower block $-1$:
$$y=\operatorname{sat}(u),\quad u=k(r-y) \tag{2.3}$$
$$y=\operatorname{sat}(k(r-y)). \tag{2.4}$$
In the linear range $|k(r-y)|<1$ one gets $y=\frac{k}{k+1}r$ (added step: $y=k(r-y)\Rightarrow y(1+k)=kr$). Otherwise the output saturates at $\pm1$. The author states that the overall relation is (p. 2-3)

$$y=\operatorname{sat}\!\Big(\frac{k}{k+1}r\Big)=\begin{cases}-1 & r\le-\frac{k+1}{k}\\ \frac{k}{k+1}r & |r|<\frac{k+1}{k}\\ 1 & r\ge\frac{k+1}{k}\end{cases}\tag{2.5}$$

The closed-loop linear range is $|r|<(k+1)/k$. Compared with (2.2), negative feedback widens the linear range by a factor $k+1$ (p. 2-3; Fig. 2.2a).

*Intuition note.* The loop feeds back the output, so the controller only has to produce the *difference* $r-y$. The input can therefore be larger before the output hits its limit. The cost is that the gain falls from $k$ to $k/(k+1)$ (the author names this trade-off on p. 2-5).

**Sensitivity (pp. 2-3, 2-4).** Sensitivity describes how parameter changes affect performance (p. 2-3). Open loop, $y=kr$:
$$\frac{dy}{dk}=r=\frac{y}{k}\;\Longrightarrow\;\frac{dy}{y}=\frac{dk}{k}\tag{2.6}$$
The sensitivity is 1, so a 10% change in $k$ gives a 10% change in $y$ (p. 2-3). Closed loop, using (2.5):
$$\frac{dy}{dk}=\frac{r}{k+1}-\frac{kr}{(k+1)^2}=\frac{r}{(k+1)^2}=\frac{y}{k(k+1)},\qquad \frac{dy}{y}=\frac{1}{k+1}\frac{dk}{k}\tag{2.7}$$
Negative feedback reduces the sensitivity to gain variations by a factor $k+1$. For $k=100$, a 10% change in $k$ gives less than a 0.1% change in $y$ (p. 2-4).

**Positive feedback (p. 2-4).** Replacing $-1$ by $+1$ turns (2.5) into
$$y=\operatorname{sat}\!\Big(\frac{k}{-k+1}r\Big).\tag{2.8}$$
- For $k<1$ the closed-loop gain is positive and larger than the open-loop gain (Fig. 2.2b). The linear range is $|r|<(1-k)/k$, so it shrinks by a factor $1-k$. As $k\to1$ the gain tends to infinity, the range to zero, and the system acts like a relay (p. 2-4).
- For $k>1$ the closed-loop gain is negative and approaches $-1$ as $k\to\infty$ (Fig. 2.2c). Several outputs are possible for $|r|<k/(k+1)$, and the system acts like a switch with hysteresis. The author says that Section 2.6 shows that, if the process has dynamics, all points where the input/output curve has negative slope are unstable (p. 2-4).

**Example 2.1, superregenerative amplifier (p. 2-4).** Armstrong built a one-tube receiver of this kind in 1914 as an undergraduate. It is modelled as an amplifier with gain $k$ and saturated output, with positive feedback. Using (2.8), the closed-loop gain is $k_{cl}=k/(1-k)$.
- $k=0.999$ gives $k_{cl}=999$.
- $k=0.99$ (a change of less than 1%) gives $k_{cl}=99$, a tenfold difference.

The drawback: the system is highly sensitive, the gain must be adjusted carefully to avoid oscillation, and the oscillatory nature needs a dynamic model. It is still used in simple walkie-talkies, garage door openers and toys (p. 2-4).

**Load disturbance (pp. 2-4, 2-5).** Open loop, $y=\operatorname{sat}(kr+v)$: in the linear region the gain from $v$ to $y$ is 1, so disturbances pass unattenuated. Closed loop with negative feedback and $r=0$: $y=\operatorname{sat}(v-ky)$, which in the linear range gives $y=v/(k+1)$. More generally (stated, not derived)
$$y=\operatorname{sat}\!\Big(\frac{v}{k+1}\Big).\tag{2.9}$$
Negative feedback reduces the effect of load disturbances by $k+1$ in the linear region (p. 2-5).

**Combined conclusion (p. 2-5).** Negative feedback increases the range of linearity, decreases sensitivity to parameter uncertainty and attenuates load disturbances; the trade-off is lower closed-loop gain. Positive feedback has the opposite effect: it can increase the closed-loop gain, but at the cost of increased sensitivity and amplification of disturbances (p. 2-5).

### 2.2 Linear Dynamical Models (pp. 2-5 to 2-12)

The tools introduced are block diagrams, linear differential equations and transfer functions. The values of the transfer function on the imaginary axis give the steady-state response to sinusoids, so a transfer function can be found experimentally (p. 2-5).

**Linear ODE and polynomials (p. 2-5).**
$$\frac{d^ny}{dt^n}+a_1\frac{d^{n-1}y}{dt^{n-1}}+\dots+a_ny=b_0\frac{d^mu}{dt^m}+b_1\frac{d^{m-1}u}{dt^{m-1}}+\dots+b_mu\tag{2.10}$$
$$a(s)=s^n+a_1s^{n-1}+\dots+a_n,\qquad b(s)=b_0s^m+b_1s^{m-1}+\dots+b_m\tag{2.11}$$
Here $u$ is the input, $y$ the output, and the coefficients are real. $a(s)$ is the characteristic polynomial. The author assumes $a$ and $b$ have no common roots (p. 2-6).

**LTI (p. 2-6).** Equation (2.10) is time-invariant (if $u(t),y(t)$ is a solution, so is $u(t+\tau),y(t+\tau)$). It is linear (if $u_1,y_1$ and $u_2,y_2$ are solutions, so is $\alpha u_1+\beta u_2,\ \alpha y_1+\beta y_2$). Such systems are called LTI. An LTI system can be characterised by a single well-chosen input/output pair, for example its step response (p. 2-6).

**Homogeneous solution (p. 2-6).** The solution is a homogeneous part (independent of input) plus a particular part (depends on input). The homogeneous equation is
$$\frac{d^ny}{dt^n}+a_1\frac{d^{n-1}y}{dt^{n-1}}+\dots+a_ny=0\tag{2.12}$$
With roots $s_k$ of $a(s)=0$ and no repeated roots,
$$y(t)=\sum_{k=1}^nC_ke^{s_kt}\tag{2.13}$$
and the $C_k$ come from the initial conditions (p. 2-6).
- Roots are real or in complex conjugate pairs. A real root gives $e^{s_kt}$, which decays if $s_k<0$, is constant if $s_k=0$ and grows if $s_k>0$ (Fig. 2.3, p. 2-7). The *time constant* $T=1/s_k$ describes how quickly the signal decays.
- A complex root $s_k=\sigma\pm i\omega$ gives $e^{\sigma t}\sin\omega t$ and $e^{\sigma t}\cos\omega t$. Zero crossings are spaced $\pi/\omega$ apart, and the envelope is $\pm e^{\sigma t}$ (p. 2-6).
- With repeated roots,
$$y(t)=\sum_{k=1}^mC_k(t)e^{s_kt}\tag{2.14}$$
where $C_k(t)$ is a polynomial of degree less than the multiplicity of $s_k$, and $\sum_k(\deg C_k+1)=n$ free parameters (details in Section 6.2, p. 2-6).

Fig. 2.3 shows $s=0,-1,1,i,-0.2+i,0.2+i$. The real part negative gives decay, positive gives growth (p. 2-7).

**Transfer function (p. 2-7).** Take $u=e^{st}$ with $s\neq s_k$ and look for a particular solution $y=G(s)e^{st}$. Then
$$\frac{d^ku}{dt^k}=s^ke^{st},\qquad \frac{d^ky}{dt^k}=s^kG(s)e^{st}\tag{2.15}$$
Inserting into (2.10):
$$(s^n+a_1s^{n-1}+\dots+a_n)G(s)e^{st}=(b_0s^m+\dots+b_m)e^{st}$$
$$G(s)=\frac{b_0s^m+b_1s^{m-1}+\dots+b_m}{s^n+a_1s^{n-1}+\dots+a_n}=\frac{b(s)}{a(s)}\tag{2.16}$$
$G$ is the transfer function. The full solution for $u=e^{st}$ is
$$y(t)=\sum_{k=1}^mC_k(t)e^{s_kt}+G(s)e^{st}\tag{2.17}$$

*Intuition note.* Exponentials are "eigen-inputs" of LTI systems: the output is the same exponential times a number $G(s)$. So $G$ can be read directly off the differential equation, and differentiation becomes multiplication by $s$.

**Reading $G$ (pp. 2-8, 2-9).**
- $G$ is read off (2.10) by inspection. The ODE can be recovered from $G$ if $a,b$ have no common factors. Input and initial conditions must both be given for the full response (p. 2-8).
- For complex $s$, $G$ maps complex numbers to complex numbers. The input $e^{i\omega t}=\cos\omega t+i\sin\omega t$ gives $G(i\omega)e^{i\omega t}$. Taking imaginary parts for $u=\sin\omega t$ (p. 2-8):
$$y(t)=\operatorname{Im}\big(G(i\omega)e^{i\omega t}\big)=\operatorname{Im}\big(|G(i\omega)|e^{i\arg G(i\omega)}e^{i\omega t}\big)=|G(i\omega)|\sin(\omega t+\arg G(i\omega)).$$
$G(i\omega)$, $|G(i\omega)|$ and $\arg G(i\omega)$ are the frequency response, gain and phase (p. 2-8).
- For constant $u=u_0$, $y=(b_m/a_n)u_0=G(0)u_0$ (set $s=0$). $G(0)$ is the zero-frequency (static) gain. If the equation is stable, the solution converges to $G(0)u_0$ (p. 2-8).
- Fig. 2.4, $G=1/(s+1)^2$: the dashed line is the pure sine (all $C_k=0$). The solid line has $y(0)$ and its derivatives zero. Since all roots have negative real parts, the homogeneous part vanishes and the response converges to the particular solution (p. 2-8).
- *Poles* are the roots of $a(s)=0$, where $G$ is infinite. Lightly damped poles (real part negative but near zero) can give resonance when a sinusoid's frequency is near the imaginary part of the pole (p. 2-8).
- *Zeros* are the roots of $b(s)$: $G(s_j)=0$, so $e^{s_jt}$ is blocked (a "transmission zero") (pp. 2-8, 2-9).
- The frequency response of a stable system can be measured with sinusoidal inputs, as an alternative or complement to physical modelling (p. 2-9).

**Stability and Routh–Hurwitz (pp. 2-9, 2-10).** Equation (2.10) is *stable* if all solutions of (2.12) go to zero for any initial condition. By (2.14) this requires all roots of $a(s)=0$ to have negative real parts (p. 2-9). Routh–Hurwitz gives conditions on the coefficients without computing roots (p. 2-9):
- First order: stable when $a_1>0$ (root $-a_1$).
- Second order: roots $s=\frac12(-a_1\pm\sqrt{a_1^2-4a_2})$; both real parts negative iff $a_1>0$ and $a_2>0$ (p. 2-10).
- Third order: negative real parts iff
$$a_1,a_2,a_3>0\ \text{ and }\ a_1a_2>a_3.\tag{2.18}$$
- Fourth order:
$$a_1,a_2,a_3,a_4>0,\quad a_1a_2>a_3,\quad a_1a_2a_3>a_1^2a_4+a_3^2.\tag{2.19}$$
Similar conditions exist for any order (p. 2-10).

*Intuition note.* Stability can be decided from signs of combinations of coefficients, which matters when the roots of a high-order polynomial are hard to compute.

**Block diagrams (pp. 2-10, 2-11).** Assume $u=e^{st}$ and a stable system, so that only the exponential response matters (p. 2-10). The convention is $y=G_{yu}u$ (left subscript output, right subscript input).
- Series (Fig. 2.5a): $y_1=G_1e^{st}$, $y=G_2G_1e^{st}$, so $G_{yu}=G_2G_1$.
- Parallel (Fig. 2.5b): $G_{yu}=G_1+G_2$.
- Feedback (Fig. 2.5c): $y=G_1e=G_1(u-G_2y)$, i.e. $y=\frac{G_1}{1+G_1G_2}e^{st}$ (added step: $y(1+G_1G_2)=G_1e^{st}$), so
$$G_{yu}(s)=\frac{G_1(s)}{1+G_1(s)G_2(s)}.\tag{2.20}$$

**Software and step response (pp. 2-11, 2-12).** MATLAB handles transfer functions: `tf('s')`, `series`, `parallel`, `feedback` (negative feedback by default). A step input is 0 for $t\le0$ and 1 for $t>0$. Standard step-response features (Fig. 2.6) are rise time $T_r$, settling time $T_s$, overshoot $M_p$ and steady-state value $y_{ss}$. Commands: `step(G)`, `step(G,T)`, `lsim(G,u,t)`. Chapter 9 extends transfer functions to time delays and PDEs (p. 2-12).

### 2.3 Using Feedback to Attenuate Disturbances (pp. 2-12 to 2-17)

Keeping a variable near a constant reference despite disturbances is the *regulation problem*. Examples named: Watt's steam engines, generators driven by water turbines, process industry, machine tools, car engine and cruise control, body temperature, blood pressure and the pupillary reflex (p. 2-12).

**Disturbance transfer function (pp. 2-12, 2-13).** In Fig. 2.7 take $r=0$ and $v=e^{st}$. Then $y=Pe^{st}-PCy$, so
$$G_{yv}(s)=\frac{P(s)}{1+P(s)C(s)}\tag{2.21}$$
The process is first order (a reasonable model if storage of mass, momentum or energy is captured by one state, e.g. car velocity, angular velocity, tank level):
$$\frac{dy}{dt}+ay=bu,\ a>0,\ b>0,\qquad P(s)=\frac{b}{s+a}\tag{2.22}$$

**Proportional control (pp. 2-13, 2-14).** With $u=k_pe$, $C=k_p$:
$$G_{yv}=\frac{b/(s+a)}{1+bk_p/(s+a)}=\frac{b}{s+(a+bk_p)},\quad \frac{dy}{dt}+(a+bk_p)y=bv.$$
The loop is stable if $a+bk_p>0$. A constant $v=v_0$ gives an output approaching $y_0=G_{yv}(0)v_0=\frac{b}{a+bk_p}v_0$ with time constant $T=1/(a+bk_p)$. Without feedback it approaches $bv_0/a$, so the effect is reduced if $k_p>0$. The error decreases with increasing $k_p$ (Fig. 2.8a) (p. 2-14).

**PI control (pp. 2-14, 2-15).**
$$u(t)=k_pe(t)+k_i\int_0^te(\tau)d\tau\tag{2.23}$$
Differentiating, $\dot u=k_p\dot e+k_ie$, so $C(s)=k_p+k_i/s$. Then
$$G_{yv}(s)=\frac{P}{1+PC}=\frac{bs}{s^2+(a+bk_p)s+bk_i}\tag{2.24}$$
(added step: $\frac{b/(s+a)}{1+b(k_ps+k_i)/(s(s+a))}=\frac{bs}{s(s+a)+b(k_ps+k_i)}$). In ODE form
$$\frac{d^2y}{dt^2}+(a+bk_p)\frac{dy}{dt}+bk_iy=b\frac{dv}{dt}\tag{2.25}$$
The disturbance enters as a derivative, so a constant disturbance gives no steady-state error; equivalently $G_{yv}(0)=0$ (p. 2-15).

*Intuition note.* If the loop is stable, the integrator keeps changing $u$ as long as the error is non-zero. So the error can only settle at zero for a constant disturbance, which matches $G_{yv}(0)=0$.

**Choosing gains (p. 2-15).** The closed-loop characteristic polynomial is
$$a_{cl}(s)=s^2+(a+bk_p)s+bk_i\tag{2.26}$$
Its roots can be assigned arbitrarily through $k_p,k_i$. Choosing roots $-\sigma_d\pm i\omega_d$:
$$(s+\sigma_d+i\omega_d)(s+\sigma_d-i\omega_d)=s^2+2\sigma_ds+\sigma_d^2+\omega_d^2\tag{2.27}$$
The homogeneous solution consists of $e^{-\sigma_dt}\sin\omega_dt$ and $e^{-\sigma_dt}\cos\omega_dt$. $\sigma_d$ sets the decay rate and $\omega_d$ (damped frequency) the oscillation frequency. Matching coefficients of (2.26) and (2.27):
$$k_p=\frac{2\sigma_d-a}{b},\qquad k_i=\frac{\sigma_d^2+\omega_d^2}{b}\tag{2.28}$$
Common parametrisation: natural frequency $\omega_c=\sqrt{\sigma_d^2+\omega_d^2}$ and damping ratio $\zeta_c=\sigma_d/\omega_c$, so $a_{cl}=s^2+2\zeta_c\omega_cs+\omega_c^2$. The author states that $\zeta_c$ determines the shape of the response and $\omega_c$ its speed (p. 2-15).

*(added step) Check against Fig. 2.8 caption ($a=1,b=2$, $\zeta_c=0.707$).* $\omega_c=1$ gives $k_p=(2\cdot0.707-1)/2\approx0.207$ and $k_i=1/2=0.5$. $\omega_c=2$ gives $k_p=(2.828-1)/2\approx0.914$ and $k_i=4/2=2$. These match the caption (p. 2-14).

Fig. 2.8b ($\zeta_c=1/\sqrt2$): proportional control leaves a steady-state error that falls with $k_p$; with PI it is zero. The text says that with larger $\omega_c$ both "the decay rate and the peak error decrease" (wording as printed; see Reading notes). Larger gains give smaller errors and control signals that react faster (p. 2-15).

**Frequency view (p. 2-16).** With (2.28), $G_{yv}=bs/(s^2+2\zeta_c\omega_cs+\omega_c^2)$. For small $\omega$, $|G_{yv}(i\omega)|\approx b\omega/\omega_c^2$; for large $\omega$, $\approx b/\omega$. The maximum is $b/(2\zeta_c\omega_c)$ at $\omega=\omega_c$. A large $\omega_c$ therefore gives good load-disturbance attenuation (p. 2-16). The method gives PI parameters for processes approximated by first-order systems and can be generalised with more complex controllers. To get the benefit of large gains the model must be accurate over wide frequency ranges (p. 2-16).

**Unmodeled dynamics (p. 2-16).** Arbitrarily fast response seems possible by raising $\omega_c$, but limits exist. Gains grow with $\omega_c$: $k_p=(2\zeta_c\omega_c-a)/b$, $k_i=\omega_c^2/b$, so the control signal may saturate. Also (2.22) is only valid in a frequency range. With an extra lag $1+sT$ (sensors, actuators, other neglected dynamics, "unmodeled dynamics"):
$$P(s)=\frac{b}{(s+a)(1+sT)}\tag{2.29}$$
$$a_{cl}=s(s+a)(1+sT)+b(k_ps+k_i)=s^3T+s^2(1+aT)+2\zeta_c\omega_cs+\omega_c^2.$$
(added step: $s(s+a)(1+sT)=s^3T+s^2(1+aT)+as$, and $a+bk_p=2\zeta_c\omega_c$, $bk_i=\omega_c^2$.) By (2.18) the loop is stable if $\omega_c^2T<2\zeta_c\omega_c(1+aT)$, i.e.
$$\omega_cT<2\zeta_c(1+aT).$$
(added step: dividing by $T$, $a_1=(1+aT)/T$, $a_2=2\zeta_c\omega_c/T$, $a_3=\omega_c^2/T$; $a_1a_2>a_3$ gives the bound.) So $\omega_c$ and the achievable response time are limited by $T$, which is typically smaller than the process time constant $1/a$ (p. 2-16). If unmodeled dynamics of components or of interacting subsystems are ignored, the implemented system can behave poorly (instability is one extreme). The author says the ability to reason about uncertainty is what makes control theory a powerful tool for design (p. 2-17).

*Intuition note.* In the first-order model nothing stops you from asking for infinite speed. A real, neglected lag $T$ turns a too-high $\omega_c$ into instability.

### 2.4 Using Feedback to Track Reference Signals (pp. 2-17 to 2-20)

Making the output follow a reference is the *servo problem* (cruise control, steering, antenna or telescope tracking, audio amplifiers, machine tools, robots) (p. 2-17).

**PI tracking (p. 2-17).** Process and controller:
$$P=\frac{b}{s+a},\qquad C=\frac{k_ps+k_i}{s}\tag{2.30}$$
With $v=0$,
$$G_{yr}=\frac{PC}{1+PC}=\frac{bk_ps+bk_i}{s^2+(a+bk_p)s+bk_i}\tag{2.31}$$
$G_{yr}(0)=1$, so $y=r$ for constant $r,y$ whatever $a,b$ are, as long as the loop is stable. The author attributes this to integral action (p. 2-17). Matching $a_{cl}(s)=s^2+(a+bk_p)s+bk_i$ (2.32) to $s^2+2\zeta_c\omega_cs+\omega_c^2$ with $\zeta_c,\omega_c>0$:
$$k_p=\frac{2\zeta_c\omega_c-a}{b},\qquad k_i=\frac{\omega_c^2}{b}\tag{2.33}$$
equivalent to (2.28). Fig. 2.9 ($a=b=1$): response time falls with larger $\omega_c$, and the initial control value rises (it is $k_p$). Overshoot falls with larger $\zeta_c$. For $\omega_c=2$, $\zeta_c=1$ gives short settling and no overshoot (p. 2-17, p. 2-18).

**Time-varying references (p. 2-18).** With (2.33),
$$G_{yr}=\frac{(2\zeta_c\omega_c-a)s+\omega_c^2}{s^2+2\zeta_c\omega_cs+\omega_c^2}$$
Constant inputs are tracked perfectly. If $|s|=|i\omega|<\omega_c$, then "using some approximations" $G_{yr}$ is close to one (the author does not give the approximation). So $\omega_c$ bounds the frequency of references tracked with small error; this is the *bandwidth* of the closed loop (p. 2-18).

**Two degrees of freedom (pp. 2-18 to 2-20).** With error feedback a reference step gives an immediate step in $u$, which is quick but may give large overshoot. Replace the PI law by
$$u(t)=k_p\big(\beta r(t)-y(t)\big)+k_i\int_0^t(r(\tau)-y(\tau))d\tau\tag{2.34}$$
so proportional action acts only on the fraction $\beta$ of $r$ (Fig. 2.10). The transfer functions are
$$C_{ur}(s)=\beta k_p+\frac{k_i}{s},\qquad -C_{uy}(s)=k_p+\frac{k_i}{s}=C(s)\tag{2.35}$$
They differ, hence "two degrees of freedom". With $P=b/(s+a)$:
$$G_{yr}=\frac{b\beta k_ps+bk_i}{s^2+(a+bk_p)s+bk_i},\qquad G_{yv}=\frac{bs}{s^2+(a+bk_p)s+bk_i}\tag{2.36}$$
The load-disturbance response equals that with error feedback; the reference response differs (p. 2-19). In Fig. 2.11 ($P=1/s$, $k_p=1.414$, $k_i=1$, $\beta=0,0.5,1$), smaller $\beta$ gives less overshoot and gentler control than error feedback ($\beta=1$) (p. 2-19). Section 12.4 will show that reference and disturbance responses can be completely separated with a more general architecture. Two degrees of freedom need both $r$ and $y$ measured. Where only $e=r-y$ is available (DVD players, optical memories, atomic force microscopes), only error-feedback controllers can be used (p. 2-20).

### 2.5 Using Feedback to Provide Robustness (pp. 2-20 to 2-23)

Black used negative feedback to build good telephone-network amplifiers from nonlinear, time-varying vacuum tubes. The general recipe is to localise the nonlinearities and sources of variation and close feedback loops around them (p. 2-20). The author quotes Bode on hearing a signal pass through many amplifiers in series, and refers to Exercise 2.9 (p. 2-20).

**Open-loop amplifier (pp. 2-20, 2-21).**
$$y=F(u)=\alpha(u+\beta u^3),\ -3\le u\le3\tag{2.37}$$
Nominal values are $\alpha=0.2$, $\beta=1$; the ranges are $0.1\le\alpha\le0.5$, $0\le\beta\le2$. For the input
$$u(t)=\sin t+\sin\pi t+\sin\pi^2t\tag{2.38}$$
Fig. 2.12b shows large variability and heavy distortion at both small and large amplitudes (p. 2-21).

**Closed loop (pp. 2-21, 2-22).** An integral controller $C=k_i/s$ around $F$ (Fig. 2.13), with $k_i=1000$, gives an almost linear input–output relation close to the desired response, with some variability due to the loop dynamics (Fig. 2.14) (p. 2-21).

**Nonlinear analysis by approximation (pp. 2-22, 2-23).** If $\beta=0$ the system is linear. Otherwise linearise around $u=u_0$ with slope $F'(u_0)$:
$$P(s)=F'(u_0)=\alpha(1+3\beta u_0^2)=:b,\qquad C(s)=\frac{k_i}{s}\tag{2.39}$$
$$G_{yr}=\frac{bk_i}{s+bk_i},\qquad G_{er}=1-G_{yr}=\frac{s}{s+bk_i}\tag{2.40}$$
This is first order with pole $-bk_i$. The smallest $b$ is 0.1, so with $k_i=1000$ the slowest pole is at 100 rad/s, fast compared with the highest input frequency $\pi^2$ rad/s (p. 2-22). From $G_{er}$ (added step: $(s+bk_i)E=sR$),
$$\frac{de}{dt}=-bk_ie+\frac{dr}{dt},\qquad \frac{dr}{dt}=\cos t+\pi\cos\pi t+\pi^2\cos\pi^2t\tag{2.41}$$
Neglecting $de/dt$:
$$e(t)\approx\frac{1}{bk_i}\frac{dr}{dt}\approx\frac{\pi^2}{bk_i}\cos(\pi^2t)\tag{2.42}$$
(the last step keeps the largest-amplitude term; added step). For $b=0.1$ this is $e\approx0.1\cos\pi^2t$, a good estimate of the maximum error over the uncertain parameters (Fig. 2.14c) (p. 2-23). This assumes a constant-gain amplifier. The loop has time constant $T_{cl}=1/(bk_i)$; amplifier dynamics must be fast compared with it for good tracking. So the largest admissible $k_i$ is set by the unmodeled dynamics (p. 2-23).

*Intuition note.* High loop gain forces $y$ to follow $r$ whatever $F$ is, so the error is roughly (rate of change of $r$) divided by loop gain. The same limit as in 2.3 caps how large that gain can be.

### 2.6 Positive Feedback (pp. 2-23 to 2-27)

Negative feedback can be understood by linear analysis. Positive feedback needs nonlinear effects, because without nonlinearity the instability grows without bound; the nonlinear elements limit the signals (p. 2-23). Examples named: encouragement, neurons (positive and negative feedback to generate spikes, Fig. 2.15 for the mollusc *Tritonia*), exponential growth $\dot x=\alpha x$ with $x=e^{\alpha t}$ (limited by food), microphone howl, stampedes, bank runs, boom-bust behaviour; all end in growth limited by finite resources (pp. 2-23, 2-24). Positive and negative are clear for static feedback; with dynamic feedback the action can change from positive to negative depending on signal frequency (p. 2-24).

**Hewlett's oscillator (pp. 2-24, 2-25).** From Hewlett's 1939 Stanford master's thesis, and the first product of Hewlett-Packard (p. 2-24). In a vacuum tube the current is controlled by the grid–cathode voltage $V_g-V_c$ (higher difference, more current) (p. 2-24). Fig. 2.16a has two tubes and two loops:
- Positive feedback from the anode of tube 2 to the grid of tube 1 through the network $R_1,C_1,R_2,C_2$. With proper gain it gives oscillation at $\omega=1/\sqrt{R_1R_2C_1C_2}$.
- Negative feedback through $R_f$ and a lamp with resistance $R_b$. Lamp resistance increases with temperature, so a larger $V_{out}$ amplitude means more current, higher resistance and lower gain. The result is a stable amplitude and frequency (p. 2-25).

**Integral action by positive feedback (p. 2-25).** In Fig. 2.17 the control signal is low-pass filtered ($1/(1+sT_i)$) and added back to $k_pe$. Proportional feedback typically leaves a steady-state error; the added bias compensates it. Then
$$G_{ue}=\frac{k_p}{1-1/(1+sT_i)}=k_p+\frac{k_p}{sT_i}$$
(added step: $1-\frac1{1+sT_i}=\frac{sT_i}{1+sT_i}$), a PI controller. The method is still used in many industrial regulators (p. 2-25).

**Positive feedback with saturation (pp. 2-25 to 2-27).** Fig. 2.18: first-order block $b/(s+a)$ with $a=1,b=4$, then $y=F(x)=\frac{x}{1+|x|}$, so $x=F^{-1}(y)=\frac{y}{1-|y|}$, with $+1$ feedback (p. 2-26).
$$\frac{dx}{dt}=-ax+b(r+y)=b(r-G(y)),\qquad G(y):=\frac{aF^{-1}(y)}{b}-y=\frac{ay}{b(1-|y|)}-y$$
$$\frac{dy}{dt}=\frac{dF}{dx}\Big|_{F^{-1}(y)}\frac{dx}{dt}=F'\big(F^{-1}(y)\big)\,b\,(r-G(y))\tag{2.43}$$
$F$ is monotone with $F'>0$, so equilibria for constant $r$ solve $r=G(y)$ (p. 2-26). For $a=1$, $b=4$ (Fig. 2.19a), $G$ has a local maximum $r_{max}=(1-\sqrt{a/b})^2=0.25$ at $y=-1+\sqrt{a/b}=-0.5$ and a local minimum $r_{min}=-0.25$ at $y=0.5$. There is one equilibrium if $|r|>0.25$, two if $|r|=0.25$, and three if $|r|<0.25$ (p. 2-26).

Equation (2.43) is first order. An equilibrium $y_e$ is stable if $G'(y_e)>0$ and unstable if $G'(y_e)<0$ (added step: the right side of (2.43) is a positive factor times $r-G(y)$). So there are two stable equilibria for $r_{min}<r<r_{max}$ and one for $|r|\ge r_{max}$ (p. 2-26).

*Behaviour as $r$ changes (p. 2-26).* Start at $r=0$ in the left stable equilibrium ($y<0$). Increasing $r$ moves the equilibrium slightly right. At $r=0.25$ the solution moves to the right stable equilibrium ($y>0$) (line B), and then $y$ increases with $r$. The static relation $y=G^\dagger(r)$ is hysteretic (Fig. 2.19b), with switches at $r=\pm r_{max}=\pm0.25$ (pp. 2-26, 2-27). Fig. 2.19c uses $a=5$, $b=50$ for clearer switches. The hysteresis width is $2r_{max}$, and $a$ sets the sharpness of the corners. The circuit is used as a trigger (Schmitt trigger) and as a memory element in solid-state memories, showing that feedback can give discrete behaviour (p. 2-27).

*Intuition note.* Positive feedback makes the middle equilibrium unstable; saturation limits the outer ones, which stay stable. The state stays on whichever side it was last pushed to, which is a one-bit memory.

### 2.7 Further Reading (p. 2-28)
Texts on the history of control (Bennett, Mindel) and on "classical control" are named. *Feedback Control for Everyone* [AM10] is the gentler introduction. Two-degree-of-freedom controllers were introduced by Horowitz [Hor63] (p. 2-28). Pointers: transfer functions in Chapters 3 and 9; stability in Chapters 5 and 10; coefficient matching in Chapters 7, 8 and 13; feedforward in Sections 8.5 and 12.4 (p. 2-28).

## Toy example (ours, not from the text)
Static loop of §2.1 with $k=9$, negative feedback.
- **Linear range.** Open loop: $|r|<1/9\approx0.111$. Closed loop: $|r|<(9+1)/9\approx1.111$, a factor of $10=k+1$.
- **Gain.** At $r=0.05$, closed loop $y=\frac{9}{10}(0.05)=0.045$. Check: $9(0.05-0.045)=0.045$. ✓ Open loop gives $y=0.45$, ten times higher gain.
- **Sensitivity.** Raise $k$ by 10% to 9.9. Open loop: $y$ rises 10%. Closed loop: $y=\frac{9.9}{10.9}(0.05)=0.04541$, a rise of $(0.04541-0.045)/0.045\approx0.9\%$. This is about 10% × $1/(k+1)=1\%$, consistent with (2.7) for small changes.
- **Disturbance.** $r=0$, $v=0.2$. Open loop: $y=0.2$. Closed loop: $y=0.2/10=0.02$. Check: $0.2-9(0.02)=0.02$. ✓

## Concepts
- [[feedback]] — here: a loop in which the controller input is $e=r-y$, the difference between reference and process output (p. 2-1)
- [[negative-feedback]] — lower block $-1$; widens linear range, cuts sensitivity and disturbance effect by $k+1$ in the static model (pp. 2-3, 2-4, 2-5)
- [[positive-feedback]] — lower block $+1$; gain $k/(1-k)$, shrunken linear range, higher sensitivity, hysteresis for $k>1$ (pp. 2-4, 2-5)
- [[open-loop-vs-closed-loop]] — open loop is controller plus process without feedback, $y=\operatorname{sat}(kr)$ (p. 2-2)
- [[reference]] — the signal $r$ giving the desired output (p. 2-1)
- [[error-signal]] — $e=r-y$, the controller input (p. 2-1)
- [[plant]] — the "process" $P$ being controlled (p. 2-2)
- [[disturbance-and-noise]] — load disturbance $v$ entering at the process input (p. 2-2)
- [[gain]] — controller gain $k$ (static); also $|G(i\omega)|$ for sinusoidal input (pp. 2-2, 2-8)
- [[stability]] — here: all homogeneous solutions go to zero; all roots of $a(s)$ have negative real parts (p. 2-9)
- [[pid-control]] — the chapter treats PI control $u=k_pe+k_i\int e$ (p. 2-14); Exercise 2.7 (p. 2-29) asks for a PID design for a second-order process
- [[integral-action]] — gives zero steady-state error to a constant disturbance, and $G_{yr}(0)=1$ if stable (pp. 2-15, 2-17)
- [[robustness]] — here: feedback around a nonlinear, variable amplifier gives a practically linear input–output relation (p. 2-23)
- [[transfer-function]] — $G(s)=b(s)/a(s)$, the factor multiplying $e^{st}$ in the particular solution (p. 2-7)
- [[linearization]] — approximating $F$ by its slope $F'(u_0)$ at an operating point (p. 2-22)
- [[linear-range]] (new) — input interval where the saturating process or loop acts as a linear map (p. 2-2)
- [[sensitivity]] (new) — how changes in parameters affect performance; here $(dy/y)/(dk/k)$ (p. 2-3)
- [[saturation]] (new) — $\operatorname{sat}(x)$, clipping of the output at $\pm1$ (p. 2-2)
- [[hysteresis]] (new) — several stable outputs for the same input, with switching at $\pm r_{max}$ (pp. 2-4, 2-26)
- [[poles-and-zeros]] (new) — roots of $a(s)$ and of $b(s)$; zeros block the exponential $e^{s_jt}$ (pp. 2-8, 2-9)
- [[routh-hurwitz-criterion]] (new) — stability conditions in terms of coefficients of $a(s)$ (pp. 2-9, 2-10)
- [[natural-frequency-damping-ratio]] (new) — $\omega_c$, $\zeta_c$ with $a_{cl}=s^2+2\zeta_c\omega_cs+\omega_c^2$ (p. 2-15)
- [[unmodeled-dynamics]] (new) — neglected dynamics such as $1+sT$; they limit $\omega_c$ and the achievable response time (p. 2-16)
- [[bandwidth]] (new) — $\omega_c$ bounds the reference frequencies tracked with small error (p. 2-18)
- [[two-degrees-of-freedom]] (new) — controller with different transfer functions $C_{ur}$ and $C_{uy}$ (p. 2-19)
- [[regulation-and-servo-problem]] (new) — hold a constant reference despite disturbances vs. follow a reference (pp. 2-12, 2-17)

## Canonical instances
- [[saturating-static-loop]] — the $\operatorname{sat}$ process with gain $k$, positive or negative feedback (p. 2-2)
- [[superregenerative-amplifier]] — positive feedback gives gain 999 but is highly sensitive (p. 2-4)
- [[watt-governor-and-pupillary-reflex]] — regulation examples (p. 2-12)
- [[black-feedback-amplifier]] — negative feedback around a nonlinear amplifier (pp. 2-20 to 2-23)
- [[hewlett-oscillator]] — positive loop sets frequency, lamp-based negative loop sets amplitude (pp. 2-24, 2-25)
- [[schmitt-trigger-memory]] — positive feedback with saturation gives hysteresis (p. 2-27)
- [[tritonia-swimming-network]] — excitatory and inhibitory neural feedback (p. 2-23)

## Bridges (candidates)
- [structural-analogy] Matching closed-loop characteristic polynomial coefficients (2.26)–(2.28) ↔ control theory: pole placement by state feedback — both choose gains to put closed-loop roots where wanted (the chapter only points to later chapters, p. 2-28).
- [same-math] Sensitivity $\frac{dy/y}{dk/k}=\frac1{k+1}$ (2.7) ↔ economics: elasticity of $y=\frac{k}{k+1}r$ with respect to $k$ — both are the log-derivative $d\ln y/d\ln k$.
- [structural-analogy] Hysteresis from positive feedback with saturation ↔ bistable switches with two stable states — the same equilibrium-and-slope picture (stable where $G'>0$).
- [metaphor] Positive feedback in bank runs, stampedes, boom-bust (p. 2-24) ↔ social dynamics: herding and self-reinforcing behaviour; the chapter gives no model for these.

## Questions this raises
- Why is $a_1a_2>a_3$ the right third-order condition, and how are the Routh–Hurwitz conditions derived for general order?
- How can loop gain be pushed as high as possible when unmodeled dynamics impose limits like $\omega_cT<2\zeta_c(1+aT)$?
- How do two-degrees-of-freedom designs achieve a complete separation of reference and disturbance responses (Section 12.4)?
- With dynamic positive feedback, at which frequencies does the feedback act as positive or negative, and what does this mean for stability?

## Exercises worth doing
- Ex. 2.2 (p. 2-28) — show $y=y_0+T\,dy_0/dt$ for an added zero, and see how a zero changes the step response — difficulty: medium
- Ex. 2.3 (p. 2-28) — derive the PI closed-loop ODE and $H_{yr}$ both by differential equations and by block-diagram algebra — difficulty: easy
- Ex. 2.5 (p. 2-29) — use Routh–Hurwitz to find the largest proportional gain keeping the pupil-reflex loop stable — difficulty: medium
- Ex. 2.6 (p. 2-29) — sensitivity of $G_{yr}$ to a 10% process-gain change for $P=1$, $C=k_i/s$ — difficulty: easy
- Ex. 2.7 (p. 2-29) — PID design by coefficient matching for a second-order process — difficulty: medium
- Ex. 2.8 (p. 2-30) — show $y+\frac1kF^{-1}(y)=r$ and bound the deviation from $y=r$ for large $k$ — difficulty: medium

## Reading notes
- Page labels give no printed number, but each page image shows a running number "2-N" (2-1 to 2-30). All citations use these as (p. 2-N). Offset: pdf = N + 42 (pdf 43 = p. 2-1).
- Margin symbols appear in the images: a circled "A" (p. 2-9), "H" (pp. 2-10, 2-20), a road-sign-like symbol at "Nonlinear Analysis and Approximations" (p. 2-22), and "F" (p. 2-26). Their meaning is not explained in these pages.
- Misprints seen: p. 2-10 writes "$y(t)=G_2(s)y_1(s)$" (presumably $y_1(t)$), "$G_s(s)$" and "$G(\,s)$" for $G_2(s)$; p. 2-20 "was in invented"; Exercise 2.10 "Queing".
- p. 2-6 defines $T=1/s_k$ as the time constant of a real root; as printed it would be negative for a decaying exponent.
- p. 2-15 says $\zeta_c$ is "in the range $[-1,1]$", while design uses $\zeta_c>0$ (p. 2-17).
- p. 2-15: "both the decay rate and the peak error decrease" with larger $\omega_c$. Fig. 2.8b shows faster decay, so "decay rate" seems to mean decay time. I kept the printed wording.
- The intuition notes, the Toy example and the (added step) lines are mine. Exercise solutions are not printed in this unit.
