---
id: astrom-2021-feedbacksystems/ch12-frequency
work: astrom-2021-feedbacksystems
unit: "12 Frequency Domain Design"
pages: 12-1 to 12-34
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Frequency Domain Design

## L0 — One line
Closed-loop behaviour (tracking, disturbance rejection, noise, robustness) is described by a few transfer functions formed from $P$, $C$ and $F$ that all have $1+L$ in the denominator, where $L=PC$ is the loop transfer function, so a controller can be designed by shaping $L$ in frequency, with feedforward added for reference response.

## L1 — The gist (≤ 120 words)
How can a controller meet several conflicting requirements at once? The chapter defines the Gang of Four and Gang of Six, the closed-loop transfer functions that carry these requirements. It shows how specifications translate into the shape of $L=PC$: high gain at low frequency, low gain at high frequency, and a moderate slope near crossover for good margins. Lead and lag compensators build this shape. Feedforward then sets the reference response, but it needs (approximate) inverse models. The root locus shows how one gain moves the closed-loop poles. Design examples include a microscope and a vectored thrust aircraft. Stein's epigraph: sensitivity improvements in one frequency range must be paid for by deteriorations in another.

**Prerequisites:** Transfer functions and Bode plots; Nyquist criterion, gain and phase margin; PID control; poles and zeros; step response (rise time, overshoot); initial/final value theorems.

## L2 — Key ideas (5–10 bullets)
- Table 12.1 lists 15 transfer functions from the inputs $r,v,w$ to the signals, many of them repeated. A subset of six (the Gang of Six) is the focus of most control designs, and four of these (the Gang of Four: $S$, $PS$, $CS$, $T$) capture the response to disturbances. (pp. 12-3, 12-4)
- $S+T=1$. Since $PC$ typically goes to zero at high frequency, $S\to1$ and $T\to0$ there, so very high-frequency references cannot be tracked and high-frequency noise reaches the error unfiltered. (p. 12-4)
- A loop transfer function can hide pole/zero cancellations. A system is called internally stable when all four of $S,PS,CS,T$ are stable (and $F$, if present, is stable). (p. 12-5)
- Specifications are expressed with a few numbers: $M_s=1/s_m$ (peak of $|S|$, a robustness measure), $M_t$ (peak of $|T|$), bandwidth, crossover frequencies (where a gain curve crosses 1), and error coefficients (small-$s$ expansion of the transfer function from reference to error). In the author's examples the product of rise time and bandwidth appears roughly constant, about 3. (pp. 12-6 to 12-9)
- Loop shaping: large $|L|$ at low frequency, small $|L|$ at high frequency. The slope $n_{gc}$ of $|L|$ near the gain crossover $\omega_{gc}$ is tied to phase margin by $n_{gc}\approx-2+\varphi_m/90$ (approximately, for a minimum-phase system with a roughly constant slope). (pp. 12-13, 12-14)
- Lead compensation adds phase near crossover but raises high-frequency gain (Bode's phase area formula). Lag compensation raises low-frequency gain. (pp. 12-15, 12-16)
- Feedforward gives $G_{yr}=F_m$ if $F_r=F_m/P$, and cancels the effect of a measured load disturbance if $F_v=1/P_1$. Both need inverse process models, which can be problematic for time delays, right half-plane zeros and high pole excess, where approximate inverses may be needed. (pp. 12-18 to 12-23)
- The root locus shows closed-loop poles as a gain varies from 0 to $\infty$. It has $n$ branches ($n$ = number of open-loop poles) and $n_{pe}$ asymptotes from $s_0$ ($n_{pe}$ = pole excess, poles minus zeros). Open-loop systems with a right half-plane zero or pole excess above 2 are unstable at high enough gain. (pp. 12-24, 12-25)
- Inner/outer loop design splits a complex plant into simpler loops. (pp. 12-27 to 12-29)

## L3 — Walkthrough

The chapter epigraph (Stein, 1989) says that "Sensitivity improvements in one frequency range must be paid for with sensitivity deteriorations in another" (p. 12-1). It adds that the price is higher for open-loop unstable plants, and that this holds for every controller. This unit does not derive it; properties of the sensitivity functions are discussed further in Chapters 13 and 14 (p. 12-5).

### 12.1 Sensitivity Functions (pp. 12-1 to 12-6)

**Why work with the loop.** We can design closed-loop behaviour by looking at the open-loop transfer function $L=PC$. Nyquist stability already used $L$. If a specification is stated in terms of $L$, we see directly how $C$ changes it. This is easier than reasoning about $G_{yr}=PC/(1+PC)$ (p. 12-1).

**Setup (Figure 12.1, p. 12-2).** The controller has a feedback block $C$ and a feedforward block $F$. The external inputs are the reference $r$, the load disturbance $v$ and the measurement noise $w$.
- $F$ generates a model reference $y_m$. The error is $e=y_m-y$.
- The process has three inputs ($u,v,w$) and one output ($y$). The controller has two inputs ($y,r$) and one output ($u$).
- Load disturbance $v$ drives the process away from its desired behaviour. Noise $w$ corrupts sensor information.
- Cruise control gives an example: slope changes are the load disturbance, and the electronics converting shaft pulses to speed give the noise.
- Load disturbances typically have low frequencies, below the controller bandwidth. Noise typically has higher frequencies.
- Assumptions: $v$ enters at the process input and $w$ acts at the process output. This is a simplification, said to cost no significant generality (p. 12-2).

**Table 12.1 (p. 12-3).** Rows are the inputs, columns the signals $y,u,e,\mu,\eta$ ($\mu$ = process input, $\eta$ = process output):

$$
\begin{array}{c|ccccc}
 & y & u & e & \mu & \eta\\\hline
r & \frac{PCF}{1+PC} & \frac{CF}{1+PC} & \frac{F}{1+PC} & \frac{CF}{1+PC} & \frac{PCF}{1+PC}\\[2pt]
v & \frac{P}{1+PC} & \frac{-PC}{1+PC} & \frac{-P}{1+PC} & \frac{1}{1+PC} & \frac{P}{1+PC}\\[2pt]
w & \frac{1}{1+PC} & \frac{-C}{1+PC} & \frac{-1}{1+PC} & \frac{-C}{1+PC} & \frac{-PC}{1+PC}
\end{array}
$$

**Gang of Six.** Many of the 15 entries repeat. The subset used most is

$$
G_{yr}=\frac{PCF}{1+PC},\quad -G_{uv}=\frac{PC}{1+PC},\quad G_{yv}=\frac{P}{1+PC},\quad
G_{ur}=\frac{CF}{1+PC},\quad -G_{uw}=\frac{C}{1+PC},\quad G_{yw}=\frac{1}{1+PC}.\tag{12.1}
$$

The signs are chosen for later convenience and do not affect magnitudes (p. 12-3).

**Gang of Four.** The responses to load disturbance and noise are called *sensitivity functions*:

$$
S=\frac1{1+PC},\quad PS=\frac{P}{1+PC},\quad T=\frac{PC}{1+PC},\quad CS=\frac{C}{1+PC}.\tag{12.2}
$$

These are the sensitivity, load (input) sensitivity, complementary sensitivity and noise (output) sensitivity functions (p. 12-3).

**Role of $F$.** Within the Gang of Six, $F$ appears only in $G_{yr}$ and $G_{ur}$ (it also enters the true error $\epsilon$ below). It is a second degree of freedom besides $C$. In practice it is common to first design $C$ with the Gang of Four for disturbances and noise, then uses $F$ for reference tracking (p. 12-4).

**True tracking error.** The true error is $\epsilon=r-\eta$ (before noise is added). It is not a signal in the diagram (p. 12-4):

$$
\epsilon=\Bigl(1-\frac{PCF}{1+PC}\Bigr)r-\frac{P}{1+PC}v-\frac{PC}{1+PC}w=(1-TF)r-PSv-Tw .
$$

**Pure error feedback** is $F=1$. Then (12.1) and (12.2) coincide, the Gang of Four characterises the system, and $\epsilon=Sr-PSv-Tw$. Design freedom is smaller, because $C$ must handle disturbance attenuation, robustness and tracking at once (p. 12-4).

**Basic properties (p. 12-4).**
- From (12.2), $S+T=1$, which is why $T$ is called complementary.
- $PC$ typically goes to zero for large $s$. Then $T\to0$ and $S\to1$. Very high-frequency references cannot be tracked ($|G_{yr}|=|FT|\to0$), and high-frequency noise reaches the error unfiltered ($|G_{ew}|=|S|\to1$).
- For a controller with integral action and a process with non-vanishing zero-frequency gain, $PC\to\infty$ as $s\to0$. Then $S\to0$ and $T\to1$, and low-frequency disturbances can be completely attenuated ($|G_{ev}|=|PS|\to0$).

*Intuition note.* At high frequency the loop does almost nothing, so the output looks like the open-loop output. At low frequency a large loop gain makes the output follow the reference. Because $S$ and $T$ always add to 1, where one is small the other is close to 1.

**Example 12.1 (p. 12-5): loop transfer function gives limited insight.** Take $P=1/(s-a)$ and a PI controller with error feedback $C=k(s-a)/s$. Then $L=k/s$ and

$$
S=\frac{s}{s+k},\quad PS=\frac{s}{(s-a)(s+k)},\quad CS=\frac{k(s-a)}{s+k},\quad T=\frac{k}{s+k}.
$$

The factor $s-a$ cancels in $L$, $S$ and $T$. If $a>0$, however, the cancellation is serious: $PS$ (load disturbance to output) is then unstable, and a small $v$ gives an unbounded output.

**Internal stability (p. 12-5).** If all four functions in (12.2) are stable, the system is *internally stable*. A feedforward $F$, if present, must also be stable. For general systems, internal stability means every input/output transfer function is stable. Usually "stable" is used for "internally stable."

**General formulation (Figure 12.2, pp. 12-5, 12-6).** The process $\mathcal P$ has inputs $u$ and a disturbance vector $\chi$. Its outputs are $y$, $r$ and a performance vector $\xi$.
- Figure 12.1 is captured with $\chi=(r,v,w)$ and $\xi=(e,\mu,\eta,\epsilon)$ (Exercise 12.2).
- With $\xi$ restricted to the errors $e,\epsilon$, the problem is to find $\mathcal C$ so that the gain from $\chi$ to $\xi$ is as small as possible (see Section 13.4).
- MIMO systems are handled by taking $u,y$ as vectors. The author warns that matrix multiplication is not commutative (p. 12-6).

### 12.2 Performance Specifications (pp. 12-6 to 12-12)

Specifications cover robustness, reference following, load attenuation and limited noise injection. They are written with the Gang of Six, with $L$, and with features of their time and frequency responses (p. 12-6).

**Robustness and features (p. 12-6).**
- Gain margin $g_m$, phase margin $\varphi_m$ and stability margin $s_m$ come from Section 10.3.
- $M_s=1/s_m$ (largest value of $|S|$) is also a robustness measure (Figure 12.3a).
- Step-response features: overshoot, rise time, settling time.
- Frequency-response features: peak values and frequencies, gain crossover frequency, bandwidth.
- $M_s$ occurs at $\omega_{ms}$. $M_t$ is the maximum of $|T|$, at $\omega_{mt}$.
- The *sensitivity crossover frequency* $\omega_{sc}$ is where $|S(j\omega)|=1$.
- Crossover frequencies and bandwidth are well defined only for monotone curves. Otherwise the lowest such frequency is typically used.

Roughly, short-time behaviour relates to high-frequency behaviour and vice versa. The precise relation is the Laplace transform. Typical feature relations are in Tables 7.1 and 7.2 (p. 12-7).

**Response to reference signals (pp. 12-7 to 12-9).**
- $G_{yr}=PCF/(1+PC)$ and $G_{ur}=CF/(1+PC)$. For $F=1$, $G_{yr}=T$. Keeping $F\neq1$ allows shaping the response (p. 12-7).
- $G_{yr}$ typically has unit zero-frequency gain, so a step gives zero steady-state error (p. 12-7).
- *Error coefficients* $e_k$ come from the small-$s$ expansion of the transfer function from $r$ to $e$:

$$G_{er}(s)\approx e_1 s+e_2s^2+\cdots,\qquad e(t)=r(t)-y(t)=G_{er}r=e_1\frac{dr}{dt}+e_2\frac{d^2r}{dt^2}+\cdots .$$

- A ramp $r=v_0t$ gives steady-state error $v_0e_1$, so the error is zero if $e_1=0$.
- A system with $e_1=0$ has $e(t)=2ae_2$ for $r=a_0t^2$ (as printed; see Reading notes).
- This supports "small $s$ = large times", a consequence of the final value theorem (p. 12-8).
- The control-signal response $G_{ur}$ should also be examined, because it shows the size and rate of control needed (p. 12-8).

**Example 12.2 (pp. 12-8, 12-9).** $P=(s+1)^{-3}$, with PI error feedback $k_p=0.6$, $k_i=0.5$ (solid curves). The dashed curves use a feedforward that gives $G_{yr}=(0.5s+1)^{-3}$:

$$F=\frac{G_{yr}(1+PC)}{PC}=\frac{2s^4+6s^3+6s^2+3.2s+1}{0.15s^4+1.025s^3+2.55s^2+2.7s+1}.$$

- Feedforward gives a faster response without overshoot, but needs much larger control signals.
- It has a larger bandwidth and no resonant peak, and $G_{ur}$ has higher gain at high frequency (pp. 12-8, 12-9).

**Time–frequency relations from Figure 12.4 (p. 12-9).**
- A large overshoot corresponds to a large resonant peak.
- For a unit reference, $u(t)\to G_{ur}(0)$ as $t\to\infty$. If $x(0)=0$, then $u(0)=G_{ur}(\infty)$.
- *Rise time–bandwidth product* $T_r\omega_b$ is dimension-free. Here $T_r=1.7$ (dashed), $3.0$ (solid) and $\omega_b=1.9$, $0.8$, giving $T_r\omega_b=3.2$ and $2.4$. Tables 7.1/7.2 give $\approx2.7$–$2.8$.
- It thus "appears" that $T_r\omega_b\approx3$. The product increases if the roll-off is faster (Exercise 12.5, which uses a slightly different bandwidth definition).

*Intuition note.* A faster step response needs a wider frequency band. In the author's examples their product stays roughly constant, so a faster step response goes with a larger bandwidth.

**Response to load disturbances and noise (pp. 12-9 to 12-11).**
- Compare closed loop with open loop ($C=0$) under identical disturbances. Then $y_{cl}=S\,y_{ol}$ (Exercise 12.6).
- Frequencies with $|S(i\omega)|<1$ are attenuated. Those with $|S(i\omega)|>1$ are amplified. $\omega_{sc}$ is the lowest frequency with $|S|=1$ (p. 12-9).
- Nyquist view: $1+L(i\omega)=1/S$ is the vector from $-1$ to $L(i\omega)$. Sensitivity is below 1 outside the circle of radius 1 centred at $-1$, and above 1 inside it (pp. 12-9, 12-10; Figure 12.5).
- $M_s$ at $\omega_{ms}$ is the largest amplification. It corresponds to the point of the Nyquist curve closest to $-1$, so $M_s=1/s_m$ and is also a robustness measure.
- For $\varphi_m=60^\circ$, "it can be shown" that $\omega_{sc}=\omega_{gc}=\omega_{tc}$ (the gain and complementary-sensitivity crossover frequencies) (p. 12-10).

Load response:

$$G_{yv}=\frac{P}{1+PC}=PS=\frac TC .\tag{12.3}$$

- For small $s$, $T\approx1$ so $G_{yv}\approx1/C$.
- With $P(0)\neq0$ and integral action, $C\approx k_i/s$, so $G_{yv}\approx s/k_i$. The integral gain $k_i$ thus measures low-frequency disturbance attenuation.
- At high frequency $S\approx1$ and $G_{yv}\approx P$ (p. 12-10).

Noise response (noise causes actuator wear and may saturate it; a typical requirement is that control variations stay a fraction of the allowed range):

$$-G_{uw}=\frac{C}{1+PC}=\frac TP=CS .\tag{12.4}$$

At high frequency $S\approx1$, so $-G_{uw}\approx C$. It is therefore useful to filter the derivative so that $C(s)\to0$ at large $s$ (high-frequency roll-off) (p. 12-11).

**Example 12.3 (pp. 12-11, 12-12).** $P=(s+1)^{-3}$ with PID $k_p=2$, $k_i=1.5$, $k_d=2.0$ and a second-order noise filter (damping $1/\sqrt2$, $T_f=0.1$):

$$C(s)=\frac{k_ds^2+k_ps+k_i}{s(s^2T_f^2/2+sT_f+1)}.\tag{12.5}$$

- Load step: $y$ peaks at 0.28 at $t=2.73$ s. $|G_{yv}|$ peaks at 0.58 at $\omega=0.7$ rad/s.
- Noise: $u$ has a valley of $-14$ at $t=0.08$ s. $|G_{uw}|$ peaks at 20 at $\omega=14$ rad/s. This is far above the load peak and far above $\omega_{gc}=0.78$ rad/s. Without the filter the gain would keep rising after 20 rad/s.
- Exercise 12.7 gives $\max|CS|\approx k_d/T_f=20$ at $\omega=\sqrt2/T_f=14.1$ rad/s (the text prints $T_d$; see Reading notes).

**Band-pass rule (p. 12-12).** $G_{yv}$ and $G_{uw}$ have band-pass shape, so their step responses are zero at small and large times. For $G_{yv}$, $\omega_p t_p=0.7\cdot2.7\approx1.9$. For $G_{uw}$, $\omega_p t_p=14\cdot0.08\approx1.1$. This supports the rule that for band-pass transfer functions the peak time times the peak frequency lies in 1–2 (Exercise 12.8). The text words it as "resonant peak"; the numbers computed are peak frequencies.

**Measuring specifications (Figure 12.7, p. 12-12).** Specifications can be checked numerically from the Gang of Six. For a real system one needs test points for injecting signals $\delta_k$ and measuring $s_{ij}$. For example, $G_{yv}$ is found by injecting at $\delta_1$ and measuring $s_{21}$. A frequency analyzer measures transfer functions directly.

### 12.3 Feedback Design via Loop Shaping (pp. 12-13 to 12-17)

**Idea (p. 12-13).** The Nyquist theorem works with $L=PC$, so the effect of $C$ on $L$ is easy to see. To stabilize an unstable system, bend the Nyquist curve away from $-1$. *Loop shaping* means choosing a compensator that gives $L$ a desired shape. Two routes are named:
- Choose a good $L$ and compute $C=L/P$. This may give high-order controllers and has limits for right half-plane poles and zeros (Sections 12.4, 14.3).
- Start from $P$, set the gain for the desired bandwidth, then add poles and zeros.

**Design considerations (Figure 12.8, pp. 12-13, 12-14).**
- Performance needs large $|L|$ where tracking and low-frequency load attenuation are wanted. For $|L|>100$, disturbances are attenuated by about a factor of 100 or more and tracking error is below 1%.
- $CS=C/(1+L)$, so $C$ should have low high-frequency gain (high-frequency roll-off).
- The shape is thus: $|L(i\omega_{gc})|=1$, large gain below, small gain above.
- Robustness is determined near $\omega_{gc}$. Bode's relations (Section 10.4) limit how fast the gain can fall. For a roughly constant slope $n_{gc}$ at $\omega_{gc}$ and a minimum-phase system:

$$n_{gc}\approx-2+\frac{\varphi_m}{90}\quad(\varphi_m\text{ in degrees}).\tag{12.6}$$

- A steeper slope gives a smaller phase margin. The approximation holds if the gain curve is not far from a straight line. The margins $30^\circ,45^\circ,60^\circ$ correspond to slopes $-5/3,-3/2,-4/3$.
- Time delays and right half-plane poles/zeros impose further limits (Chapter 14).

*Intuition note.* The loop gain must fall from large to small across the crossover. Falling too steeply there costs phase margin, so the controller has to bring $L$ down gently enough.

**Procedure (p. 12-14).**
- Loop shaping is trial and error, starting from the Bode plot of $P$.
- Choosing $\omega_{gc}$ is a major decision. It is a compromise between load attenuation and noise injection.
- If $\varphi_m=60^\circ$, $\omega_{gc}=\omega_{sc}$. For smaller margins, $\omega_{gc}<\omega_{sc}$.
- Next, shape $L$ with controller gain, poles and zeros. Lag compensation raises low-frequency gain. Lead compensation changes behaviour near crossover.
- The method is simple for SISO systems. It can also be used with one input and many outputs by closing loops one at a time.
- For minimum-phase systems the only limitation is that large phase leads and high gains may be needed for fast response. Non-minimum-phase limits are in Section 14.3.

**Lead and lag compensation (pp. 12-15, 12-16).**

$$C(s)=k\frac{s+a}{s+b},\qquad a>0,\ b>0.\tag{12.7}$$

- Lead compensator: $a<b$. Lag compensator: $a>b$.
- PI control is a lag compensator with $b=0$.
- A lead compensator is essentially a PD controller with filtering, the filter being the pole at $s=b$.
- A first-order compensator gives up to $90^\circ$ of phase lead. Higher-order versions $C(s)=k\,(s+a)^n/(s+b)^n$, $a<b$, give more (Exercise 12.17).
- Figure 12.9 uses $a=0.25$, $b=4$, $k=16$ (lead) and $a=4$, $b=0.25$, $k=1$ (lag).
- Lag raises low-frequency gain, so it improves low-frequency tracking and attenuation. Lead improves phase margin: for $a<b$ it adds phase between the pole/zero pair, extending about $10\times$ in frequency in each direction.

**Bode's phase area formula (p. 12-16).** Let $G(s)$ have $G(0)>0$, no right half-plane poles or zeros, and $\lim_{s\to\infty}G(s)=G(\infty)>0$. Then

$$\log\frac{G(\infty)}{G(0)}=\frac2\pi\int_0^\infty\arg G(i\omega)\,d\log\omega=\frac2\pi\int_{-\infty}^{\infty}\arg G(ie^u)\,du .\tag{12.8}$$

The log of the gain ratio is proportional to the area under the phase curve. Lead compensation thus requires high gain at high frequency and increases sensitivity to measurement noise. The formula is attributed to Bode [Bod45, p. 286].

*Intuition note.* Phase lead is not free. The more phase you add, over a wider range, the more the high-frequency gain must exceed the low-frequency gain.

**Example 12.4: atomic force microscope in tapping mode (p. 12-16).**
- Model: $P(s)=\dfrac{a(1-e^{-s\tau})}{s\tau(s+a)}$, with $a=\zeta\omega_0$, $\tau=2\pi n/\omega_0$ and gain normalised to 1. Parameters: $a=1$, $\tau=0.25$.
- Step 1, integral control only: $L=k_iP/s$. Adjusting $k_i$ so that the loop is marginally stable gives $k_i=8.3$.
- Step 2, add proportional action and increase $k_p$ gradually. $k_p=3.5$ gives $M_s=1.6$ and $M_t=1.3$, with a much larger phase margin than integral-only.
- Gang of Four check (Figure 12.10b): the largest $PS$ is 0.3, so loads are well attenuated. The largest $|CS|$ is 6. The controller has gain $k_p=3.5$ at high frequency, so adding high-frequency roll-off may be considered.

**Example 12.5: roll control of a vectored thrust aircraft (pp. 12-17 to 12-19).**
- Model: $P(s)=r/(Js^2)$, with parameters in Figure 12.11b: $m=4.0$ kg, $J=0.0475$ kg m², $r=25.0$ cm, $c=0.05$ kg m/s, $g=9.8$ m/s².
- Specification: error below 1% in steady state, and tracking error below 10% up to 10 rad/s.
- The author would like a gain of at least 10 at 10 rad/s, which requires $\omega_{gc}$ to be higher. Raising the gain alone would give a very low phase margin, so phase must be added at the crossover.
- Lead compensator (12.7) with $a=2$, $b=50$, $k=200$. Result: $|L|>10$ up to 10 rad/s and more than $60^\circ$ phase margin (Figure 12.12).

### 12.4 Feedforward Design (pp. 12-18 to 12-24)

**Combining feedforward and feedback (Figure 12.13, p. 12-18).** The process is split as $P=P_1P_2$, with the measured disturbance $v$ entering at the input of $P_2$. $F_m$ is the desired (model) response to $r$. $F_r$ and $F_v$ are the feedforward blocks for $r$ and $v$. The design splits in two:
- $C$ gives robustness and disturbance attenuation.
- $F_r$, $F_v$ are designed independently for reference response and measured disturbances.

**Reference response.**

$$G_{yr}=\frac{P(CF_m+F_r)}{1+PC}=TF_m+SPF_r=F_m+S(PF_r-F_m)\tag{12.9}$$

using $T=1-S$ (added step: $TF_m+SPF_r=F_m(1-S)+SPF_r=F_m+S(PF_r-F_m)$). $G_{yr}$ is close to $F_m$ if $PF_r-F_m$ is small or if $S$ is small. Perfect feedforward is

$$F_r=\frac{F_m}{P_1P_2}=\frac{F_m}{P},\tag{12.10}$$

which gives $G_{yr}=F_m$. $F_r$ contains an inverse process model (p. 12-19).

**Measured disturbance.**

$$G_{yv}=\frac{P_2(1-P_1F_v)}{1+PC}=P_2S(1-P_1F_v)\tag{12.11}$$

is small if $1-P_1F_v$ is small or if $S$ is small. Perfect compensation:

$$F_v=\frac1{P_1}.\tag{12.12}$$

*Intuition note.* Feedforward cancels a known effect before it shows in the output, by applying the inverse of the process. It works only as far as the inverse is accurate. Feedback with small $S$ is the other way to make the error small.

**Example 12.6: vehicle steering (pp. 12-19, 12-20).** $P(s)=(\gamma s+1)/s^2$ maps steering angle to lateral deviation. The desired response without overshoot is $F_m=\omega_c^2/(s+\omega_c)^2$. Then (12.10) gives

$$F_r=\frac{F_m}{P}=\frac{\omega_c^2s^2}{(\gamma s+1)(s+\omega_c)^2},$$

which is stable if $\gamma>0$. For $\omega_c=0.2$, a lane change takes about 20 vehicle lengths with smooth steering (Figure 12.14). The text states the largest steering angle as "slightly larger than 0.2 rad (12°)" (see Reading notes).

**Difficulties (p. 12-20).** The ideal compensators are

$$F_r=\frac{F_m}{P_1P_2},\qquad F_v=\frac1{P_1}.\tag{12.13}$$

Inversion is problematic for time delays, right half-plane zeros or high pole excess:
- Inverting a delay needs prediction, which cannot be done perfectly except when the command is known in advance.
- Right half-plane zeros give an unstable inverse, so approximate inverses may be needed.
- Positive pole excess requires differentiation, so the reference must be smooth and noise can be a problem.

There is freedom in $F_m$. A stable $F_r$ can be obtained if $F_m$ has the same delays and right half-plane zeros as the process (p. 12-21).

**Example 12.7: right half-plane zero (pp. 12-21, 12-22).**
- Take $P=\dfrac{1-s}{(s+1)^2}$ and $F_m=\dfrac{\omega_m^2(1-s)}{s^2+2\zeta_c\omega_ms+\omega_m^2}$. $F_m$ keeps the zero at $s=1$. Then

$$F_r(s)=\frac{\omega_m^2(s+1)^2}{s^2+2\zeta_c\omega_ms+\omega_m^2}.\tag{12.14}$$

- The same $F_r$ results for $P=1/(s+1)^2$ and $F_m=\omega_m^2/(s^2+2\zeta_c\omega_ms+\omega_m^2)$. Without the right half-plane zero, fast well-behaved responses are possible (dashed curves in Figure 12.15).
- The response goes the wrong way first, called *inverse response*. It is barely visible at $\omega_m=1$ but grows with speed: at $\omega_m=5$ the undershoot is more than 200%. A right half-plane zero thus limits achievable bandwidth (Chapter 14). A reasonable $\omega_m$ is 0.2–0.5.
- $F_r(0)=1$ and $F_r(\infty)=\omega_m^2$, so by the initial value theorem $u_{ff}(0)=\omega_m^2$.
- Control signal: for $\omega_m=0.2$ it grows from 0.04 to 1 with small overshoot. For $\omega_m=1$ it starts at 1, overshoots, then settles at 1. For $\omega_m=5$ it starts at 25 and decays to 1 with an undershoot.

**Approximate inverses.** Processes with right half-plane zeros have no stable inverse.

**Theorem 12.1 (approximate inverse; stated without proof, pp. 12-22, 12-23).** Let the rational $G(s)$ have all poles in the left half-plane and no zeros on the imaginary axis. Factor $G=G^+G^-$, where $G^+$ has all zeros in the left half-plane and $G^-$ all zeros in the right half-plane. An approximate stable inverse that minimises the mean square error for a step input is

$$G^\dagger(s)=\frac1{G^+(s)\,G^-(-s)}.\tag{12.15}$$

**Example 12.8 (p. 12-23).** Take $P=(1-s)/(s+1)^2$ and $F_m=\omega_m^2/(s^2+2\zeta_c\omega_ms+\omega_m^2)$, without the zero in $F_m$.
- $P^-=1-s$ and $P^+=1/(s+1)^2$, so $P^\dagger=\dfrac1{P^+(s)P^-(-s)}=\dfrac{(s+1)^2}{1+s}=s+1$.
- $F_r=F_mP^\dagger=\dfrac{\omega_m^2(s+1)}{s^2+2\zeta_c\omega_ms+\omega_m^2}$. This no longer relies on cancelling the right half-plane zero.
- Then $G_{yr}=PF_r$, which the text prints as $\dfrac{1-s}{(s^2+2\zeta_c\omega_ms+\omega_m^2)(s+1)}$ (see Reading notes).
- Compared with Example 12.7: small differences at $\omega_m=0.2$, large at $\omega_m=5$. The approximate inverse gives smaller undershoot but somewhat longer settling.

**Summary (p. 12-23).** Feedforward improves reference response and reduces measurable disturbances. It is limited by delays, right half-plane zeros and high pole excess. Zeros depend on the sensors and can be changed by moving or adding sensors. Feedforward can be sensitive to model uncertainty (Chapter 13), so it is usually combined with feedback for robust performance.

### 12.5 The Root Locus Method (pp. 12-24 to 12-27)

**Motivation (p. 12-24).** With a controller of restricted complexity, not all closed-loop poles can be placed. The simplest case, one adjustable parameter, is handled by the *root locus*: the roots of the characteristic polynomial as a function of a parameter. Its general shape is easy to get and often very informative.

**Setup.** $P(s)=\dfrac{b(s)}{a(s)}=b_0\dfrac{(s-z_1)\cdots(s-z_m)}{(s-p_1)\cdots(s-p_n)}$, with $a$ of degree $n$, $b$ of degree $m$, and pole excess $n_{pe}=n-m\ge0$. The controller is $C=k$, with $k$ from 0 to $\infty$ (pp. 12-24, 12-25).

$$a_{cl}(s)=a(s)+kb(s).\tag{12.16}$$

There are $n$ branches. At $k=0$ the closed-loop poles equal the open-loop poles.

**Small gain (p. 12-25).** Near an open-loop pole $p_l$ of multiplicity $m$, write $a(s)=(s-p_l)^m\tilde a(s)$. Then

$$(s-p_l)^m\tilde a(s)+kb(s)\approx(s-p_l)^m\tilde a(p_l)+kb(p_l)=0,$$

so $s=p_l+\sqrt[m]{-kb(p_l)/\tilde a(p_l)}$. This gives a star of $m$ branches from $p_l$, with angle $2\pi/m$ between neighbours.

**Large gain (p. 12-25).** For large $s$ and $k$,

$$a_{cl}(s)=b(s)\Bigl(\frac{a(s)}{b(s)}+k\Bigr)\approx b(s)\Bigl(\frac{s^{n_{pe}}}{b_0}+k\Bigr).\tag{12.17}$$

For large $k$ the closed-loop poles approach the roots of $b(s)$ and $\sqrt[n_{pe}]{-b_0k}$. A better approximation (Exercise 12.15) is

$$s=s_0+\sqrt[n_{pe}]{-kb_0},\qquad s_0=\frac1{n_{pe}}\Bigl(\sum_{k=1}^np_k-\sum_{k=1}^mz_k\Bigr).\tag{12.18}$$

The asymptotes are $n_{pe}$ lines radiating from $s_0$, the "center of mass" of poles and zeros. For $b_0k>0$ their angles to the real axis are $(\pi+2l\pi)/n_{pe}$, $l=1,\dots,n_{pe}$. The angles between asymptotes are $360^\circ/n_{pe}$ (Figure 12.17).

**Summary (p. 12-25).** $n$ branches start at the open-loop poles and end at open-loop zeros or at infinity. The branches that go to infinity follow the asymptotes (12.18). Consequence: open-loop systems with right half-plane zeros or pole excess larger than 2 will always be unstable for sufficiently large gains.

*Intuition note.* Every zero attracts one branch. The branches left over run off to infinity along fixed directions. If a zero is in the right half-plane, or if more than two branches run off (so some asymptotes lean into the right half-plane), high gain eventually destabilises.

**Sketching rules (p. 12-25).** Multiple roots give a locally symmetric star. For $kb_0>0$, the real axis carries locus segments where the number of real poles and zeros to the right is odd (Exercise 12.16). Departure directions from poles are in Exercise 12.19.

**Examples (12.19, Figure 12.18, pp. 12-26, 12-27).** $P_a=k\frac{s+1}{s^2}$, $P_b=k\frac{s+1}{s(s+2)(s^2+2s+4)}$, $P_c=k\frac{s+1}{s(s^2+1)}$, $P_d=k\frac{s^2+2s+2}{s(s^2+1)}$.
- $P_a$: two roots start at the origin ($m=2$ star). The locus bends toward the zero and is a circle around $s=-1$. Two roots meet on the real axis and depart, one toward the zero and one to $-\infty$. The real-axis segment is $(-\infty,-1]$.
- $P_b$: starts at $s=-2,0,-1\pm i\sqrt3$. With $n_{pe}=3$, the asymptotes originate at $s_0=-1$.
- $P_c$: $n_{pe}=2$, so vertical asymptotes from $s_0=0.5$. The real-axis segment is $[-1,0]$.
- $P_d$: three branches. One is the real segment $(-\infty,0]$. The other two start at the complex poles and end at the zeros.

**Design use (p. 12-27).** Take PI control of $1/(s^2+1)$ with $C=k(s+2)/s$, described as the case of Figure 12.18c. The locus shows instability for all $k$, so the process cannot be stabilised by a PI controller. A PID controller $C=k(s^2+2s+2)/s$ has zeros left of the undamped poles. Figure 12.18d shows stability for $k>0$, so $k$ can be chosen to place the poles well. The root locus can also show the effect of parameters other than gain (Example 5.17).

### 12.6 Design Example (pp. 12-27 to 12-30)

**Example 12.9: lateral control of a vectored thrust aircraft.** The aircraft uses an inner/outer loop design (Figure 12.19).
- The inner loop $H_i$ (roll dynamics $P_i$ with controller $C_i$) makes $\theta$ follow $\theta_r$ quickly and accurately.
- The outer loop (lateral dynamics $P_o$, controller $C_o$) treats the roll angle as a direct input. This is valid if the roll loop is fast relative to the desired position bandwidth.
- Specification for the whole system: zero steady-state error in lateral position, bandwidth about 1 rad/s, phase margin $45^\circ$ (p. 12-27).

**Inner loop (p. 12-28).** $P_i=H_{\theta u_1}=r/(Js^2)$. Aim: bandwidth 10 rad/s (10 times the outer loop) and low-frequency error at most 5%. The lead compensator of Example 12.5 is used: $C_i=k\frac{s+a}{s+b}$ with $a=2$, $b=50$, $k=200$. The closed loop satisfies

$$H_i=\frac{C_i}{1+C_iP_i}-mg\frac{C_iP_i}{1+C_iP_i}=\frac{C_i(1-mgP_i)}{1+C_iP_i}.$$

Figure 12.20b shows $H_i\approx-mg=-39.2$ is a good approximation up to 10 rad/s.

**Outer loop (pp. 12-28, 12-29).** Assume perfect roll control:

$$P(s)=H_i(0)P_o(s)=\frac{H_i(0)}{ms^2+cs}.$$

The author notes this approximation may not be valid and must be verified at the end. The outer process is a double integrator. A lead controller is chosen with $|L_o|<0.1$ for $\omega>10$ rad/s, so that high-frequency $H_i$ dynamics can be neglected:

$$C_o(s)=-k_o\frac{s+a_o}{s+b_o}.$$

The minus sign cancels the negative sign in the process. Parameter choices:
- Phase lead flattens out at about $b_o/10$. Crossover is desired at $\omega_{gc}=1$ rad/s, so $b_o=10$.
- For adequate phase lead at crossover, $b_o/10<10a_o<b_o$, so $a_o\in(0.1,1)$. Choose $a_o=0.3$.
- A simple calculation shows $k_o=2$ gives loop gain of magnitude 1 or more at crossover.
- Result: $C_o(s)=-2\dfrac{s+0.3}{s+10}$.

**Verification (pp. 12-29, 12-30).** The combined system has phase margin $68^\circ$ and gain margin 6.2 (Figure 12.21). The specifications are satisfied. The Gang of Four (Figure 12.22) is reasonable. $PS$ is large at low frequency because the controller has no integral action. Splitting into inner and outer loops is common and simplifies complex designs. Designing directly from $y$ to $u_1$ is described as very challenging; the extra measurement of $\theta$ greatly simplifies the design because it can be broken into simpler pieces.

### 12.7 Further Reading (p. 12-30)
The author's notes (history, in brief):
- Loop shaping emerged at Bell Labs with Black's negative-feedback amplifier. Nyquist derived his criterion to understand "singing" (instability).
- Bode established the amplitude–phase relation for minimum-phase systems, the ideal loop transfer functions and the phase area formula.
- Horowitz developed two degrees of freedom.
- The importance of the sensitivity functions came with $H_\infty$ methods in the 1980s.
- Fundamental limits from nonlinearities, poles and zeros are discussed in Chapter 14.

## Toy example (ours)
Take $P(s)=1/s$ and $C=k=10$. Then $L=10/s$.
- $S=\dfrac1{1+L}=\dfrac{s}{s+10}$ and $T=\dfrac{10}{s+10}$. So $S+T=\dfrac{s+10}{s+10}=1$.
- At $s=i\omega$, $|S|=\omega/\sqrt{\omega^2+100}$.
 - $\omega=0.1$: $|L|=100$ and $|S|=0.1/\sqrt{100.01}\approx0.0100$. This agrees with the rule that $|L|>100$ gives attenuation by about 100 (p. 12-14).
 - $\omega=1$: $|S|=1/\sqrt{101}\approx0.0995$ and $|T|=10/\sqrt{101}\approx0.995$.
 - $\omega=10$ (where $|L|=1$): $|S|=10/\sqrt{200}\approx0.707$.
 - $\omega=100$: $|S|=100/\sqrt{10100}\approx0.995$. At high frequency, noise passes almost unchanged.
- The gain slope of $L$ at crossover is $-1$. Equation (12.6) gives $\varphi_m\approx90(n_{gc}+2)=90^\circ$, which matches $\arg L=-90^\circ$ at all frequencies (phase margin $180^\circ-90^\circ$).
- Here $|S|<1$ at every frequency. A first-order loop has no peak, which is why $M_s$ is not an issue. A real loop with more phase lag would have $|S|>1$ near crossover.

## Concepts
- [[feedback]] — $C$ acts on the measured output $y$, with $-1$ in the loop (p. 12-2)
- [[feedforward]] — blocks $F_r$, $F_v$ act on reference and measured disturbance, ideally by inverse models (p. 12-18)
- [[transfer-function]] — used to relate every signal pair in Table 12.1 (p. 12-3)
- [[bode-plot]] — gain and phase vs frequency, used to read $S$, $T$, $L$ and compensators (p. 12-13)
- [[nyquist-criterion]] — here used as a design picture: bend the curve away from $-1$ (p. 12-13)
- [[stability]] — internal stability means all four of $S,PS,CS,T$ are stable (p. 12-5)
- [[pid-control]] — PI is a lag compensator, PD with filter a lead compensator (p. 12-15)
- [[integral-action]] — makes $S\to0$ at low frequency; $G_{yv}\approx s/k_i$ (p. 12-10)
- [[robustness]] — measured by margins and by $M_s=1/s_m$ (p. 12-6)
- [[disturbance-and-noise]] — load disturbance $v$ at the process input, measurement noise $w$ at the output (p. 12-2)
- [[delay]] — time delays limit feedforward inversion and loop shaping (p. 12-20)
- [[sensitivity-function]] (new) — $S=1/(1+PC)$; $|S|<1$ means a disturbance is attenuated, $|S|>1$ amplified (pp. 12-3, 12-9)
- [[complementary-sensitivity]] (new) — $T=PC/(1+PC)=1-S$ (p. 12-3)
- [[gang-of-four-six]] (new) — the six (or four) transfer functions that capture closed-loop performance (p. 12-3)
- [[two-degree-of-freedom]] (new) — controller with feedback $C$ and feedforward $F$ designed separately (pp. 12-2, 12-18)
- [[loop-shaping]] (new) — design by giving $L=PC$ a desired shape with compensators (p. 12-13)
- [[lead-lag-compensation]] (new) — $C=k(s+a)/(s+b)$; lead if $a<b$, lag if $a>b$ (p. 12-15)
- [[bode-phase-area-formula]] (new) — $\log G(\infty)/G(0)=\frac2\pi\int\arg G\,d\log\omega$ for minimum-phase $G$ (p. 12-16)
- [[approximate-inverse]] (new) — $G^\dagger=1/(G^+(s)G^-(-s))$ for processes with right half-plane zeros (p. 12-23)
- [[root-locus]] (new) — closed-loop poles as one parameter varies (p. 12-24)
- [[rise-time-bandwidth-product]] (new) — $T_r\omega_b\approx3$ in the author's examples (p. 12-9)
- [[inner-outer-loop-design]] (new) — a fast inner loop treated as ideal when designing the outer loop (p. 12-27)

## Canonical instances
- [[cruise-control]] — slope changes as load disturbance, shaft-pulse electronics as noise (p. 12-2)
- [[atomic-force-microscope]] — PI loop shaping with $k_i=8.3$ (critical) and $k_p=3.5$ (p. 12-16)
- [[vectored-thrust-aircraft]] — lead compensation for roll; inner/outer design for lateral position (pp. 12-17, 12-27)
- [[vehicle-steering]] — feedforward lane change with $F_r=F_m/P$ (p. 12-19)
- [[rhp-zero-inverse-response]] — right half-plane zero causes initial undershoot in feedforward response (p. 12-21)
- [[pi-cancellation-instability]] — hidden unstable cancellation in $P=1/(s-a)$, $C=k(s-a)/s$ (p. 12-5)

## Bridges (candidates)
- [structural-analogy] $S+T=1$ and the cost of high bandwidth ↔ signal processing: a trade-off between passing signal and passing noise. Both are "pass band versus noise" constraints.
- [structural-analogy] Root locus asymptotes and the closed-loop polynomial $a+kb$ ↔ eigenvalue assignment: both study roots of the closed-loop characteristic polynomial.
- [structural-analogy] Feedforward $F_r=F_m/P$ as model inversion ↔ model-based control in neuroscience: an internal inverse model produces the command.
- [metaphor] Inner/outer loops ↔ hierarchical control in organisations: fast local loops are treated as ideal by the slower layer above.

## Questions this raises
- Why exactly must sensitivity be paid for elsewhere (Stein's epigraph), and how does the price grow for unstable plants (Chapters 13–14)?
- How much model error can a feedforward design tolerate before the feedback loop has to repair it (Chapter 13)?
- When is the "perfect inner loop" assumption in Example 12.9 safe, and how can one test it?
- How can the right half-plane zero limit be quantified, and can sensor placement remove it?

## Exercises worth doing
- Ex. 12.1 (p. 12-31) — compute Gang of Four responses for $a=-1$, $k=0.2$ and $5$; builds feel for $S,PS,CS,T$ — difficulty: easy
- Ex. 12.6 (p. 12-32) — show $y_{cl}=S\,y_{ol}$; the basic meaning of sensitivity — difficulty: easy
- Ex. 12.5 (p. 12-32) — rise time–bandwidth product $T_r\tilde\omega_b\ge\pi$ for an ideal low-pass filter — difficulty: medium
- Ex. 12.8 (p. 12-32) — peak frequency–peak time product for a band-pass second-order system — difficulty: medium
- Ex. 12.10 (p. 12-33) — verify Bode's phase area formula numerically for a lead compensator — difficulty: medium
- Ex. 12.18 (p. 12-34) — relate $|S(i\omega_{gc})|=|T(i\omega_{gc})|$ to $\varphi_m$ — difficulty: medium

## Reading notes
- Page labels give "printed=?", but the page images print "12-N" at the page foot or head. Here pdf $=400+N$, so pdf 401 is printed 12-1. I cite printed pages as (p. 12-N).
- Misprints and inconsistencies seen in the images:
 - p. 12-4: the text gives low-frequency tracking as "$|G_{yr}|=|FT|\to0$". Since $T\to1$ there, the intended limit is presumably $|F|$, not 0. The high-frequency statement ($\to0$) is correct.
 - p. 12-8: "$e(t)=2ae_2$ for $r=a_0t^2$" uses $a$ where $a_0$ appears to be meant.
 - Example 12.2: p. 12-8 gives the initial control as 13.3 (feedforward) and 0.6 (PI). p. 12-9 gives initial values 8 and 6. From the printed $F$, $F(\infty)=2/0.15\approx13.3$ and $G_{ur}(\infty)=C(\infty)F(\infty)=0.6\cdot13.3\approx8$ (my arithmetic). So 13.3 is $F(\infty)$, not $u(0)$, and "6" looks like a misprint for 0.6.
 - p. 12-12: "$\omega=\sqrt2/T_d$" should be $T_f$ (Exercise 12.7 uses $T_f$; $\sqrt2/0.1=14.1$). The rule "peak time × resonant peak" is computed with peak frequency.
 - Example 12.6: the text says the largest steering angle is slightly above 0.2 rad, but the Figure 12.14b axis stops at 0.04 and the curve peaks near 0.03.
 - Figures 12.15 and 12.16 captions list $\omega_m=0.2,1$ and "0.5", but the panels show 5.
 - Example 12.8: the printed $G_{yr}$ has no $\omega_m^2$ in the numerator. $PF_r$ as computed from $F_r$ would contain it.
 - p. 12-27: the PI design example uses $C=k(s+2)/s$ with $P=1/(s^2+1)$ and refers to Figure 12.18c, but $P_c$ has its zero at $-1$, not $-2$.
 - Exercise 12.3 uses $F_u$, which is not defined in the text (probably $F_r$). Exercise 12.19 uses $s_k$ where the zeros $z_k$ appear to be meant.
- Theorem 12.1 and the claim that $\omega_{sc}=\omega_{gc}=\omega_{tc}$ at $\varphi_m=60^\circ$ are stated without proof in the source.
- Page 12-9 states the initial values of the bottom-row time responses in Figure 12.4 as 8 (dashed) and 6 (solid); in the figure image the solid curve starts well below 1 (near 0.6).
- Exercises are listed, not solved. Solutions are not printed in this unit.
