---
id: astrom-2021-feedbacksystems/ch13-robust
work: astrom-2021-feedbacksystems
unit: "13 Robust Performance"
pages: 13-1 to 13-30
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Robust Performance (Åström & Murray, Ch. 13)

## L0 — One line
Feedback tolerates model errors: stability is guaranteed (by a conservative test) when the relative error stays below 1/|T| at each frequency, relative errors in closed-loop responses are scaled by the sensitivity functions S or T, and the ν-gap metric is the proper way to compare a process with its model for feedback.

## L1 — The gist (≤ 120 words)
Models are simplified and only approximately correct. The chapter asks how large an error in the process model a feedback loop can tolerate, and how to design controllers that stay stable and perform well anyway. Answers: (1) closeness of systems should be measured in the loop (Vinnicombe's ν-gap metric), not by open-loop responses; (2) stability is guaranteed for stable perturbations of relative size $|\delta|<1/|T|$ at every frequency (a conservative test); (3) relative errors in closed-loop responses are scaled by S or T; (4) design tools are the Youla parameterization, QFT, LQG, and H∞ control with weights; (5) some problems exceed linear robust design. This matters because it helps explain why simplified models are often enough for design.

**Prerequisites:** Nyquist criterion and winding numbers; sensitivity S = 1/(1+PC), complementary sensitivity T = PC/(1+PC), and loop transfer function L = PC; Gang of Four = S, PS, CS, T; small gain theorem; Bode plots; state feedback, observers and Kalman filter (as background); derivatives of rational functions. Terms used above and defined in L3: chordal distance (distance between points projected onto a sphere, p. 13-6); winding-number condition (the encirclement-count condition in (13.7)); Youla parameterization (all stabilizing controllers via a free stable Q); QFT (quantitative feedback theory, graphical loop shaping); LQR (state feedback minimizing a quadratic cost) and LQG (LQR plus Kalman filter); H∞ control (minimizing the H∞ norm, the peak over frequency of the largest singular value of a transfer matrix); gain scheduling (switching controllers by a measured variable).

## L2 — Key ideas (5–10 bullets)
- Parametric uncertainty is checked by evaluating performance criteria over a range of parameters (by simulation in Example 13.1). Unmodeled dynamics are handled by adding a bounded transfer function (additive, multiplicative or feedback form) to the nominal model (p. 13-2, 13-3, 13-4).
- Open-loop similarity can mislead. Two systems can look alike open loop and behave very differently closed loop, and the reverse. Matching frequency responses also needs a winding-number condition (p. 13-4, 13-5).
- The ν-gap metric $\delta_\nu$ (largest chordal distance between Nyquist curves, set to 1 if the winding condition fails) is the proper measure of closeness for feedback (p. 13-6, 13-7).
- Robust stability under multiplicative uncertainty is guaranteed if $|\delta(i\omega)|<1/|T(i\omega)|$ at all ω (a conservative, sufficient condition). It allows large errors where T is small, so a model accurate near crossover is often sufficient (resonant-peak systems are an exception) (p. 13-10, 13-12).
- For small process changes, the relative error of $G_{yv}$ and $G_{yr}$ is S times the relative process error, and for $G_{uw}$ it is −T times it (p. 13-16, 13-17).
- The Youla parameterization lists all stabilizing controllers; the free stable function Q enters the Gang of Four affinely (p. 13-13 to 13-15).
- Design requirements conflict. Nanopositioner designs show trade-offs between bandwidth, noise injection, disturbance attenuation and control effort (p. 13-19 to 13-21).
- LQR has strong robustness, but adding an observer can lose it. H∞ minimizes a norm of the Gang of Four; its inverse is a generalized stability margin. Vinnicombe's theorem links it to the ν-gap (p. 13-23 to 13-26).
- Robust linear design has limits. Gain scheduling, automatic tuning and adaptation are the alternatives the text names when variations are too large for a linear controller (p. 13-27, 13-28).

## L3 — Walkthrough

### Chapter opening (p. 13-1)
Black's 1934 quote: build an amplifier with deliberately excess gain, then feed back and throw the excess away. This gives far more constant amplification and less nonlinearity (p. 13-1). The chapter studies robustness of stability and performance when process dynamics are uncertain, using generalized Nyquist arguments (p. 13-1).

### 13.1 Modeling Uncertainty (p. 13-1 to 13-8)

**Parametric uncertainty** means the parameters of the model are not precisely known (e.g. car mass). It is investigated by evaluating the performance criteria over a range of parameters (p. 13-1, 13-2).

*Example 13.1 (cruise control, p. 13-2).* A PI controller with $k_p=0.5$, $k_i=0.1$ is designed for m = 1600 kg, fourth gear (α = 12), $v_e$ = 20 m/s. It is tested on linearized models with 1600 < m < 2000 kg, α = 10, 12, 16, and 10 ≤ v ≤ 40 m/s, for a 4° slope. The largest velocity error is 0.5–1.2 m/s and the settling time is about 15 s. The control signal exceeds 1 in some cases, meaning the throttle is fully open. The two closed-loop eigenvalues show good damping in all cases (Fig. 13.1). Conclusion: the example indicates that, at least as far as parametric variations go, a design based on a simple nominal model with fixed controller parameters gives satisfactory control. Low gear and low speed were not considered, since cruise controllers are not typically used there (p. 13-2).

**Unmodeled dynamics** are neglected mechanisms, e.g. engine combustion or small computer delays (p. 13-3). A more detailed model costs effort and is itself uncertain (p. 13-3). The alternative is to augment the nominal model P with a bounded transfer function representing the gross features of what is neglected. This also covers infinite-dimensional pieces such as delays (p. 13-3). Three forms (Fig. 13.2):
- additive: $\tilde P=P+\Delta$;
- multiplicative: $P(1+\delta)$;
- feedback: $\Delta_{fb}$ (the figure shows $\Delta_{fb}$ in a feedback path around P; Table 13.1 writes the process as $P/(1+\Delta_{fb}P)$).

They are related by

$$\delta=\frac{\Delta}{P},\qquad \Delta_{fb}=\frac{\Delta}{P(P+\Delta)}=\frac{\delta}{P(1+\delta)}.$$

If the closed loop is stable for all Δ satisfying a bound (e.g. $|\Delta|<\epsilon$), the system is **robustly stable** (p. 13-3, 13-4).

**When are two systems similar? (p. 13-4, 13-5).** A naive idea is that two systems are close if their open-loop responses are close. The examples show this fails.

*Example 13.2 (similar open loop, different closed loop).*

$$P_1=\frac{k}{s+1},\qquad P_2=\frac{k}{(s+1)(sT+1)^2}\tag{13.1}$$

With T = 0.025, k = 100 the open-loop step responses are barely distinguishable. With unit feedback (C = 1):

$$T_1=\frac{k}{s+1+k},\qquad T_2=\frac{k}{s^3T^2+(T^2+2T)s^2T+(1+2T)s+1+k}\tag{13.2}$$

$T_1$ is stable for k > −1; $T_2$ is stable for $-1<k<2T+4+2/T$. For k = 100, T = 0.025, $T_1$ is stable and $T_2$ is unstable (p. 13-4). (See Reading notes on the printed denominator.)

*Example 13.3 (different open loop, similar closed loop).* $P_1=k/(s+1)$, $P_2=k/(s-1)$ (13.3). $P_1$ is stable and $P_2$ unstable. With C = 1:

$$T_1=\frac{k}{s+k+1},\qquad T_2=\frac{k}{s+k-1}\tag{13.4}$$

These are very close for large k (p. 13-4).

*Example 13.4 (frequency responses, p. 13-5).* $P_1=\dfrac{2}{(1+5s)^3(1-0.05s)}$ and $P_2=\dfrac{2}{(1+5s)^3(1+0.05s)}$ (13.5) have nearly identical Bode and Nyquist plots. $P_1$ has one right half-plane pole, $P_2$ none; neither has zeros. Both $1+P_1$ and $1+P_2$ have winding number $n_w=0$. By the Nyquist criterion ($n_{z,D}=n_{w,\Gamma}+n_{p,D}$), the closed loop with $P_1$ has one right half-plane zero and is unstable, while the one with $P_2$ is stable. Lesson: similar open-loop frequency responses are not enough; the winding number condition must also hold (p. 13-5).

> *Intuition note.* Closeness has to be judged inside the loop. A small open-loop difference (a fast extra lag, a sign of one pole) can change the closed-loop outcome completely. Large open-loop differences can disappear when high gain feeds back.

**The Vinnicombe metric (p. 13-6, 13-7).** Chordal metric between the frequency responses (13.6):

$$d_{P_1P_2}(\omega):=\frac{|P_1(i\omega)-P_2(i\omega)|}{\sqrt{1+|P_1(i\omega)|^2}\sqrt{1+|P_2(i\omega)|^2}}$$

It maps two complex numbers to [0, 1]. Geometrically, the points are projected onto a sphere of diameter 1 at the origin (the Riemann sphere), by a line through the north pole (inverse stereographic projection). The chordal distance is the Euclidean distance between the projected points (Fig. 13.5) (p. 13-6).

Vinnicombe's set $\mathcal C$ of pairs of rational transfer functions (13.7):

$$\mathcal C=\Big\{P_1,P_2:\ 1+P_1(i\omega)P_2(-i\omega)\neq0\ \forall\omega,\ \ n_{w,\Gamma}(1+P_1(s)P_2(-s))+n_{p,rhp}(P_1(s))-n_{p,rhp}(P_2(-s))=0\Big\}$$

Here $n_{w,\Gamma}$ is the winding number around the Nyquist contour Γ and $n_{p,rhp}$ counts open right half-plane poles (p. 13-6).

**Definition 13.1 (ν-gap metric).**

$$\delta_\nu(P_1,P_2)=\begin{cases}\sup_\omega d_{P_1P_2}(\omega),&(P_1,P_2)\in\mathcal C\\ 1,&\text{otherwise}\end{cases}\tag{13.8}$$

Vinnicombe showed $\delta_\nu$ is a metric, extended it to multivariable and infinite-dimensional systems, and gave strong robustness results (p. 13-7). MATLAB: `gapmetric`. The winding condition implies that connecting $P_1(s)$ in feedback with $P_1(-s)$ and with $P_2(-s)$ gives the same number of right half-plane poles. A necessary condition is that $1+P_1(s)P_1(-s)$ and $1+P_1(s)P_2(-s)$ have the same number of right half-plane zeros. It can be read as a continuity condition: P can be perturbed continuously from $P_1$ to $P_2$ without passing through any P with $d_{P_1P}(\omega)=1$ (p. 13-7).

*Example 13.5 (for Ex. 13.2, p. 13-7, 13-8).* $f(s)=1+P_1(s)P_2(-s)=1+\dfrac{k^2}{(1-s^2)(1-sT)^2}$, k = 100. The curve $f(i\omega)$ is a closed contour in the right half-plane that does not encircle the origin, so $n_{w,\Gamma}=0$. Neither process has right half-plane poles, so $(P_1,P_2)\in\mathcal C$. Both $1+P_1(s)P_1(-s)$ and $1+P_1(s)P_2(-s)$ have one right half-plane zero. Then $\delta_\nu=0.89$, large because 1.0 is the maximum (p. 13-8).

*Example 13.6 (for Ex. 13.3, p. 13-8, 13-9).* $1+P_1(i\omega)P_2(-i\omega)=1-\dfrac{k^2}{(1+i\omega)^2}=1-\dfrac{k^2(1-\omega^2)}{(1+\omega^2)^2}+\dfrac{2k^2i\omega}{(1+\omega^2)^2}$. The imaginary part is zero at ω = 0 and ω = ∞, with real parts $1-k^2$ and 1. So the function is zero only at ω = 0 with k = 1. Also $f(s)=1-\dfrac{k^2}{(s+1)^2}=\dfrac{s^2+2s+1-k^2}{(s+1)^2}$ has a right half-plane zero if k > 1. The winding number is 0 if k ≤ 1 and 1 if k > 1 (Fig. 13.6c). The text concludes $\delta_\nu=1$ for k ≤ 1 and $(P_1,P_2)\in\mathcal C$ for k > 1. Then

$$d_{P_1P_2}(\omega)=\frac{2k}{1+k^2+\omega^2},\qquad \delta_\nu(P_1,P_2)=\begin{cases}1&k\le1\\ \dfrac{2k}{1+k^2}&k>1\end{cases}$$

The maximum is at ω = 0. For k = 100, $\delta_\nu=0.02$ (closed loops very close) (p. 13-9).

> *Intuition note.* $\delta_\nu$ is the largest gap between Nyquist curves on the sphere, with the value set to 1 if the winding-number condition (13.7) fails. A small value indicates similar closed-loop behavior under feedback (Example 13.6: 0.02 means very close closed loops).

### 13.2 Stability in the Presence of Uncertainty (p. 13-9 to 13-15)

**Robust stability using Nyquist (p. 13-9, 13-10).** The stability margin is $s_m=1/M_s$, the shortest distance from the Nyquist curve to −1, where $M_s$ is the maximum of the sensitivity function (p. 13-9). Consider a stable feedback loop and change P to P + Δ, with Δ a stable transfer function (needed for the winding condition). The loop transfer function changes from PC to PC + CΔ. The number of encirclements of −1 stays unchanged as long as $1+(P+\Delta)C$ never reaches 0. The distance from −1 to L = PC is $|1+L|$, so it is enough that $|C\Delta|<|1+L|$, which is guaranteed if

$$|\Delta|<\Big|\frac{1+PC}{C}\Big|=\Big|\frac{1+L}{C}\Big|\quad\text{or}\quad|\delta|<\frac1{|T|},\quad \delta:=\frac{\Delta}{P}\tag{13.9}$$

Required at all frequencies:

$$|\delta(i\omega)|=\Big|\frac{\Delta(i\omega)}{P(i\omega)}\Big|<\Big|\frac{1+L(i\omega)}{L(i\omega)}\Big|=\frac1{|T(i\omega)|}\quad\forall\omega\ge0\tag{13.10}$$

The condition is conservative, since larger perturbations are allowed in directions other than toward −1 (p. 13-10). It lets us check stability for any Δ within the bound without knowing it exactly. Large variations are allowed where T is small and smaller ones where T is large. Conversely, to demand a given robustness, one can try to choose C so that T is small in the right frequency bands (p. 13-10). A conservative estimate is

$$|\delta(i\omega)|<\frac1{|T(i\omega)|}\le\frac1{M_t},\qquad M_t=\sup_\omega|T(i\omega)|=\Big\|\frac{PC}{1+PC}\Big\|_\infty\tag{13.11, 13.12}$$

Reasonable $M_t$ is 1.2 to 2. The text says Exercise 13.7 shows that if $M_t=2$ then pure gain variations of 50% or pure phase variations of 30° are permitted (p. 13-11).

> *Intuition note.* Think of the Nyquist curve with a circle of radius $|C\Delta|$ around each point. As long as no circle reaches −1, nothing changes in the encirclement count, so stability is kept. The bound says how big the circle may be.

*Example 13.7 (cruise control, p. 13-11, 13-12).* $P(s)=\dfrac{1.32}{s+0.01}$, PI with $k_p=0.5$, $k_i=0.1$.
- At low frequency T → 1, so $|\delta|<1$ (perturbations as large as P itself).
- $M_t=1.17$ at $\omega_{mt}=0.26$ gives the tightest bound, $|\delta|<0.86$ or $|\Delta|<4.36$.
- At ω = 5 rad/s, $|T|=0.264$, so $|\delta|<3.8$.

Conclusion: good robustness, and the high-frequency properties of the transmission are not important for the cruise controller design. Fig. 13.8b shows the allowed perturbation circles $|C\Delta|=|CP|/|T|$ around the Nyquist curve (p. 13-11, 13-12). The text calls this typical of many processes: moderately small uncertainties are required only around the gain crossover frequencies, while large uncertainties can be permitted at higher and lower frequencies. A simple model good around crossover is thus often enough. Systems with many resonant peaks are an exception (p. 13-12).

**Small gain interpretation (p. 13-12, 13-13).** Block-diagram manipulation (Fig. 13.9) isolates the uncertainty. The two-block loop has loop transfer function $L=\dfrac{PC}{1+PC}\dfrac{\Delta}{P}=T\delta$. Equation (13.10) says its gain is below 1, so the system is stable by the small gain theorem (Theorem 10.4). Table 13.1 (proofs left as exercises):

| Process | Uncertainty | Robust stability |
|---|---|---|
| $P+\Delta$ | additive | $\|CS\Delta\|_\infty<1$ |
| $P(1+\delta)$ | multiplicative | $\|T\delta\|_\infty<1$ |
| $P/(1+\Delta_{fb}P)$ | feedback | $\|PS\Delta_{fb}\|_\infty<1$ |

*Example 13.8 (sector-bounded nonlinearity, p. 13-12, 13-13).* A nonlinear gain F(x) with $k_{low}x<F(x)<k_{high}x$ is in feedback with a linear part H(s). If the nominal design has maximum sensitivities $M_s$ and $M_t$, the circle criterion shows stability for

$$k_{low}=\frac{M_s}{M_s+1}\ \text{or}\ \frac{M_t-1}{M_t},\qquad k_{high}=\frac{M_s}{M_s-1}\ \text{or}\ \frac{M_t+1}{M_t}$$

With $M_s=M_t=1.4$: gain variations from 0.3 to 3.5. With $M_s=M_t=2$: 0.5 to 2 (p. 13-13). (Added step: these ranges equal the smaller $k_{low}$ and larger $k_{high}$ of the two alternatives, e.g. for 1.4: 0.4/1.4 ≈ 0.29 and 1.4/0.4 = 3.5.)

*Example 13.9 (Bode's ideal loop transfer function, p. 13-13).* $L(s)=ks^{-n}$, $1\le n\le5/3$ (13.13). The gain curve is a line of slope −n and $\arg L(i\omega)=-n\pi/2$. Phase margin $\varphi_m=90(2-n)^\circ$ for all k; stability margin $s_m=\sin\pi(1-n/2)$. It cannot be realized with lumped components unless n is an integer, but it can be approximated by a proper rational function over a frequency range (Exercise 13.8). An op-amp circuit with $G(s)\approx k/(s+a)$ realizes it with n = 1 (p. 13-13).

**Youla parameterization (p. 13-13 to 13-15).** Purpose: describe all stabilizing controllers, so a search over controllers needs no explicit stability test (p. 13-13, 13-14).

*Stable process.* Choose a stable Q and set $T=PQ$ (feedforward). Implemented by feedback with C:

$$C=\frac{Q}{1-PQ},\qquad u=Q(r-y+Py)\tag{13.14}$$

Gang of Four: $S=1-PQ$, $PS=P(1-PQ)$, $CS=Q$, $T=PQ$. All are stable if P and Q are stable, so C is stabilizing. All stabilizing controllers for a stable process have this form for some Q (p. 13-14). In the block diagram (Fig. 13.10a) the signal z is a subtraction of identical signals and is zero in steady state. The two parallel copies of P create modes that are not reachable and observable, and these are stable because P is stable. Similar architectures appear in the Smith predictor and internal model controller (Section 15.4) (p. 13-14).

*Unstable process.* Write $P=n_p/d_p$ and $C=n_c/d_c$ without common factors. With stable polynomials $f_p$, $f_c$:

$$P=\frac{n_p}{d_p}=\frac{N_p}{D_p},\qquad C=\frac{n_c}{d_c}=\frac{N_c}{D_c}\tag{13.15}$$

where $N_p$, $D_p$, $N_c$, $D_c$ are stable rational functions. The sensitivity functions are

$$S=\frac{D_pD_c}{D_pD_c+N_pN_c},\quad PS=\frac{N_pD_c}{D_pD_c+N_pN_c},\quad CS=\frac{D_pN_c}{D_pD_c+N_pN_c},\quad T=\frac{N_pN_c}{D_pD_c+N_pN_c}$$

C is stabilizing if and only if $D_pD_c+N_pN_c$ has no right half-plane zeros. For stable Q, adding $N_pQ$ to $D_c$ and subtracting $D_pQ$ from $N_c$ leaves the closed-loop poles unchanged:

$$\overline C=\frac{N_c-D_pQ}{D_c+N_pQ},\qquad D_cu=N_c(r-y)+Q(D_py-N_pu)\tag{13.16}$$

The new Gang of Four (13.17):

$$S=\frac{D_p(D_c+N_pQ)}{D_pD_c+N_pN_c},\ \ PS=\frac{N_p(D_c+N_pQ)}{D_pD_c+N_pN_c},\ \ \overline CS=\frac{D_p(N_c-D_pQ)}{D_pD_c+N_pN_c},\ \ T=\frac{N_p(N_c-D_pQ)}{D_pD_c+N_pN_c}$$

All are stable, so (13.16) parameterizes stabilizing controllers. Conversely, all stabilizing controllers can be written this way ([Vid85, Sec. 3.1], cited by the text). Q appears affinely in the Gang of Four, which suits optimization over Q (p. 13-15).

> *Intuition note.* Q is a free "dial" that cannot destroy stability as long as it is stable. Because closed-loop transfer functions are affine in Q, finding a good controller becomes a search over stable Q.

### 13.3 Performance in the Presence of Uncertainty (p. 13-15 to 13-19)

Setup: the basic loop of Fig. 13.11 with reference r, load disturbance v, measurement noise w (p. 13-16).

**Disturbance attenuation.** From load disturbance to output:

$$G_{yv}=\frac{P}{1+PC}=PS\tag{13.18}$$

With constant low-frequency process gain and integral action, $G_{yv}\approx s/k_i$, so $k_i$ measures low-frequency attenuation (p. 13-16). Differentiating with respect to P gives $\dfrac{dG_{yv}}{dP}=\dfrac{1}{(1+PC)^2}=\dfrac{SP}{P(1+PC)}=S\dfrac{G_{yv}}{P}$, hence

$$\frac{dG_{yv}}{G_{yv}}=S\frac{dP}{P}\tag{13.19}$$

This holds for small variations. The response to load disturbances is insensitive to process variations where |S| is small (p. 13-16).

**Noise injection.** From measurement noise to control signal:

$$G_{uw}=-\frac{C}{1+PC}=-\frac TP\tag{13.20}$$

Noise is typically high-frequency, and PC is small there, so $G_{uw}\approx C$. Hence the controller needs small high-frequency gain (**high-frequency roll-off**), e.g. low-pass filtering in PID control (p. 13-17). Differentiating: $\dfrac{dG_{uw}}{dP}=\dfrac{C}{(1+PC)^2}C=-T\dfrac{G_{uw}}{P}$, so

$$\frac{dG_{uw}}{G_{uw}}=-T\frac{dP}{P}\tag{13.21}$$

Where PC is small, T is small and process uncertainty has little influence on $G_{uw}$ (p. 13-17).

**Reference response.**

$$G_{yr}=\frac{PCF}{1+PC}=TF\tag{13.22}$$

$\dfrac{dG_{yr}}{dP}=\dfrac{CF}{1+PC}-\dfrac{PCFC}{(1+PC)^2}=\dfrac{CF}{(1+PC)^2}=S\dfrac{G_{yr}}{P}$, so

$$\frac{dG_{yr}}{G_{yr}}=S\frac{dP}{P}\tag{13.23}$$

The relative error in the closed loop is small when the sensitivity is small. Assumptions: perturbations are small, and stable (no new right half-plane poles). The analysis is conservative (p. 13-17, 13-18).

> *Intuition note.* S acts as a "magnifying glass" for process errors in reference and disturbance responses, and T does so for the noise-to-control path. Small S at low frequencies protects tracking and disturbance rejection; small T at high frequencies protects the noise path.

*Example 13.10 (op-amp circuit, p. 13-18, 13-19).* The block diagram of Fig. 13.12b (from Exercise 10.1) models the op amp as $v_2=-G(s)v$, and the load as a disturbance d at the output of G:

$$G_{v_2v_1}=-\frac{R_2}{R_1}\frac{G(s)}{G(s)+R_2/R_1+1}$$

If G is large over the desired band, the response is close to the ideal $\alpha:=R_2/R_1$. With $G=b/(s+a)$, $b=ak$ (gain-bandwidth product), the text gives $S=\dfrac{s+a}{s+a+\alpha b}$, $T=\dfrac{\alpha b}{s+a+\alpha b}$. Then $\dfrac{dG_{v_2v_1}}{G_{v_2v_1}}=S\dfrac{dP}{P}$, so at low frequencies (S small) changes in a or b matter little, if b is large enough. For the load, $G_{v_2d}=S$, and

$$\frac{dG_{v_2d}}{dP}=\frac{-C}{(1+PC)^2}=-\frac TP G_{v_2d}\ \Rightarrow\ \frac{dG_{v_2d}}{G_{v_2d}}=-T\frac{dP}{P}$$

At low frequencies (T ≈ 1) relative changes in disturbance rejection are about the same as the process perturbations, and they drop off at higher frequencies. But $G_{v_2d}$ itself is small at low frequency, so this may not matter in many applications (p. 13-19). Exercise 13.11 treats feedforward configurations (p. 13-19).

### 13.4 Design for Robust Performance (p. 13-19 to 13-28)

Typical requirements (attenuate load disturbances; moderate noise injection; follow commands; low sensitivity to process variations) are captured by S, T, $G_{yv}$, $G_{uw}$, $G_{yr}$, $G_{ur}$; at least six transfer functions must be considered (Section 12.1). The requirements conflict. A higher bandwidth improves load disturbance attenuation but worsens noise injection (p. 13-19).

*Example 13.11 (nanopositioner for an atomic force microscope, p. 13-19 to 13-21).* $P(s)=\dfrac{\omega_0^2}{s^2+2\zeta\omega_0s+\omega_0^2}$ (Example 10.9). With an integral controller, $\omega_{gc}<2\zeta\omega_0(1-s_m)$ is needed for robustness; a PI controller gives little improvement (p. 13-19).

*Design 1: cancel the fast stable pole.* Choose the PID controller

$$C(s)=\frac{k_ds^2+k_ps+k_i}{s}=\frac{k_i}{s}\frac{s^2+2\zeta\omega_0s+\omega_0^2}{\omega_0^2}\tag{13.24}$$

with $k_p=2\zeta k_i/\omega_0$, $k_d=k_i/\omega_0^2$, giving $L(s)=k_i/s$. With $k_i=0.5$ the bandwidth rises from $\omega_{gc}=0.01$ to $\omega_{gc}=k_i=0.5$. But PS has a peak at $\omega/\omega_0=1$ (high sensitivity to load disturbances near resonance), CS has a notch at $\omega_0$ and CS grows without bound at high frequency (noise-sensitive; likely unusable) (p. 13-20). Adding a second-order filter:

$$C(s)=\frac{k_i}{s}\frac{s^2+2\zeta\omega_0s+\omega_0^2}{\omega_0^2(1+sT_f+(sT_f)^2/2)}\tag{13.25}$$

$T_f$ is a compromise: a larger value reduces noise effects but lowers the stability margin. $T_f=0.2/k_i$ is a reasonable choice. Noise sensitivity drops dramatically at a marginal cost in S. The poor resonance-frequency disturbance attenuation is invisible in S (pole cancellation) but visible in PS (p. 13-20, 13-21).

*Design 2: active damping.* With ideal PID,

$$L(s)=\frac{\omega_0^2(k_ds^2+k_ps+k_i)}{s(s^2+2\zeta\omega_0s+\omega_0^2)}\tag{13.26}$$

the characteristic polynomial is

$$s^3+(k_d\omega_0^2+2\zeta\omega_0)s^2+(k_p+1)\omega_0^2s+k_i\omega_0^2\tag{13.27}$$

A general third-order polynomial is parameterized as

$$s^3+(\alpha_c+2\zeta_c)\omega_cs^2+(1+2\alpha_c\zeta_c)\omega_c^2s+\alpha_c\omega_c^3\tag{13.28}$$

($\alpha_c,\zeta_c$ fix relative pole positions; $\omega_c$ fixes their magnitude and the bandwidth). Matching coefficients gives a linear equation with solution

$$k_p=\frac{(1+2\alpha_c\zeta_c)\omega_c^2}{\omega_0^2}-1,\quad k_i=\frac{\alpha_c\omega_c^3}{\omega_0^2},\quad k_d=\frac{(\alpha_c+2\zeta_c)\omega_c}{\omega_0^2}-\frac{2\zeta_c}{\omega_0}\tag{13.29}$$

(printed as such; see Reading notes). With roll-off:

$$C(s)=\frac{k_ds^2+k_ps+k}{s(1+sT_f+(sT_f)^2/2)}\tag{13.30}$$

If the PID is designed without the filter, $T_f$ must be well below $T_d$; $T_f=T_d/10=0.1k_d/k$ is reasonable (p. 13-21). For $\zeta_c=0.707$, $\alpha_c=1$, $\omega_c=\omega_0,2\omega_0,4\omega_0$ (Fig. 13.14): the maxima of S and T are small and disturbances are well attenuated over the whole range. Large control signals are needed: the maximum CS gains are 19, 103, 434. So there is a trade-off between disturbance attenuation and controller gain, and low-noise sensors and wide-range actuators are required (p. 13-21).

*Other design methods.* Methods that guarantee robust performance appeared only in the late 1980s. Many give controllers with the structure of state feedback plus an observer (p. 13-22).

**Quantitative feedback theory (QFT) (p. 13-22, 13-23).** A graphical loop-shaping method by Horowitz. First find a controller that gives a T robust to process variations, then shape the reference response by feedforward. On a Nyquist plot, level curves of |T| form a Hall chart. |T| = 1 on the line Re L = −0.5, and near that line large process variations change T only moderately. The shaded region 0.9 < |T| < 1.1 is shown in Fig. 13.15. One represents uncertainty at each frequency by a region and shapes L so the variation of T is as small as possible, often on a Nichols chart (the conformal map of the Hall chart under N = log L, scale flipped).

**Linear quadratic control (p. 13-23, 13-24).** The trade-off between disturbance attenuation and noise injection can be made by minimizing

$$J=\int_0^\infty\big(y^2(t)+\rho u^2(t)\big)\,dt.$$

With all states measured, the controller is $u=-Kx$ (LQR). It has phase margin of at least 60° and infinite gain margin (p. 13-23). With unmeasured states, use an observer or a Kalman filter. The Kalman filter has the same structure as the eigenvalue-assigned observer, but its gains L come from an optimization problem. LQ control plus a Kalman filter is LQG. The Kalman filter is optimal when load disturbance and measurement noise are Gaussian. The computation solves algebraic Riccati equations (MATLAB `care`, `dare`; also `lqg`, `lqi`, `kalman`) (p. 13-23, 13-24). The state feedback gains depend on ρ, the filter gains on the noise models. The robustness of state feedback is unfortunately lost when the observer is added [Doy78]. Some parameters give poor robustness, so measuring states and reconstructing them with an observer are fundamentally different (p. 13-24).

**H∞ control (p. 13-24, 13-25).** It minimizes the H∞ norm of a matrix of transfer functions (defined in (10.15)). In Fig. 13.16a, the process $\mathcal P$ has inputs u (control) and χ (generalized disturbance) and outputs ξ (generalized error) and y (measurement). The closed loop is linear:

$$\xi=\mathcal G(P(s),C(s))\chi\tag{13.31}$$

The aim is a C that keeps the gain of $\mathcal G$ small even with process uncertainty. Many choices of uncertainty and norm give different designs (p. 13-24).

Regulation case (r = 0, Fig. 13.16b): $\xi=(\mu,\eta)$, $\mu=v-u$, $\chi=(v,-w)$:

$$\xi=\begin{pmatrix}\mu\\ \eta\end{pmatrix}=\begin{pmatrix}\dfrac1{1+PC}&\dfrac C{1+PC}\\[2mm]\dfrac P{1+PC}&\dfrac{PC}{1+PC}\end{pmatrix}\begin{pmatrix}v\\-w\end{pmatrix}=:\mathcal G(P,C)\chi\tag{13.32}$$

If C is stabilizing,

$$\|\mathcal G(P,C)\|_\infty=\sup_\omega\bar\sigma(\mathcal G)=\sup_\omega\frac{\sqrt{(1+|P(i\omega)|^2)(1+|C(i\omega)|^2)}}{|1+P(i\omega)C(i\omega)|}\tag{13.33}$$

with $\bar\sigma$ the largest singular value. The entries are the Gang of Four. The diagonal entries S and T capture robustness. The off-diagonal entries $G_{yv}$ and $-G_{uw}$ capture performance. Minimizing the norm balances both. Numerical methods find a stabilizing minimizer if one exists. It has the structure of state feedback plus observer (Fig. 8.7, Theorem 8.3), with gains from algebraic Riccati equations (`hinfsyn`) (p. 13-25).

**Generalized stability margin (p. 13-25, 13-26).** Recall $s_m=\inf_\omega|1+P(i\omega)C(i\omega)|=1/M_s$ for stabilizing C. Define

$$\sigma_m=\begin{cases}\inf_\omega\dfrac{|1+P(i\omega)C(i\omega)|}{\sqrt{(1+|P(i\omega)|^2)(1+|C(i\omega)|^2)}}&C\text{ stabilizes }P\\0&\text{otherwise}\end{cases}\tag{13.34}$$

The text states it can be shown that the infimum equals $\inf_\omega\dfrac{|P+1/C|}{\sqrt{(1+|P|^2)(1+|1/C|^2)}}$. So $\sigma_m$ is the shortest chordal distance between $P(i\omega)$ and $-1/C(i\omega)$. Using (13.6) and (13.33):

$$\sigma_m(P,C)=\begin{cases}1/\|\mathcal G(P,C)\|_\infty&C\text{ stabilizes }P\\0&\text{otherwise}\end{cases}\tag{13.35}$$

**Theorem 13.1 (Vinnicombe's robustness theorem).** Consider a process P. Assume the controller C gives generalized stability margin $\sigma_m$. Then C stabilizes all processes $P_1$ such that $\delta_\nu(P,P_1)<\sigma_m(P,C)$. The text says it is proved in [Vin01] and generalizes (13.11) (p. 13-26).

Relation to classical margins. From (13.34):

$$|1+P(i\omega)C(i\omega)|^2\ge\sigma_m^2(1+|P(i\omega)|^2)(1+|C(i\omega)|^2)\tag{13.36}$$

- *Gain margin.* If the Nyquist curve crosses the negative real axis, $PC=-k$ with 0 < k < 1. Then $|1-k|^2\ge\sigma_m^2(1+|P|^2+|C|^2+k^2)\ge\sigma_m^2(1+k)^2$ (the second step uses $|P|^2+|C|^2\ge2|P||C|=2k$; added step). Hence
$$k\le\frac{1-\sigma_m}{1+\sigma_m},\qquad g_m=\frac1k\ge\frac{1+\sigma_m}{1-\sigma_m}\tag{13.37}$$
- *Phase margin.* If L crosses the unit circle with phase margin $\varphi_m$, $PC=-e^{i\varphi_m}$. Then $|1-e^{i\varphi_m}|^2\ge\sigma_m^2(1+|P|^2+1/|P|^2+1)\ge4\sigma_m^2$ since $|x|+1/|x|\ge2$. With $|1-e^{i\varphi_m}|=2\sin(\varphi_m/2)$, this gives
$$\varphi_m\ge2\arcsin\sigma_m\tag{13.38}$$
(the printed intermediate line omits a square on the sine; see Reading notes). For $\sigma_m=1/3,1/2,2/3$: $g_m\ge2,3,5$ and $\varphi_m\ge39^\circ,60^\circ,84^\circ$ (p. 13-26).

> *Intuition note.* $\sigma_m$ combines the classical distance to −1 with the chordal geometry of the ν-gap. The theorem then says any process closer than $\sigma_m$ to the model (in ν-gap) is stabilized. The gain and phase margin formulas turn this into familiar numbers.

**Disturbance weighting (p. 13-26, 13-27).** Weights W change the H∞ solution (Fig. 13.17a). A weight on the load disturbance can be moved into the process and controller, giving an equivalent standard problem with $\overline P=PW$, $\overline C=W^{-1}C$:

$$\bar\xi=\begin{pmatrix}\bar\mu\\ \bar\eta\end{pmatrix}=\begin{pmatrix}\dfrac1{1+\overline P\,\overline C}&\dfrac{\overline P}{1+\overline P\,\overline C}\\[2mm]\dfrac{\overline C}{1+\overline P\,\overline C}&\dfrac{\overline P\,\overline C}{1+\overline P\,\overline C}\end{pmatrix}\begin{pmatrix}\bar v\\-w\end{pmatrix}=\mathcal G(\overline P,\overline C)\bar\chi$$

Since $\overline P\,\overline C=PC$, only the off-diagonal entries change; S and T do not. The load entry becomes $PW/(1+PC)$ and the noise entry $CW^{-1}/(1+PC)$. Solve for $\overline C$, then the real controller is $C=W\overline C$. A scalar W > 1 increases the effect of load disturbances and reduces that of noise. Choosing W = k/s automatically gives integral action; emphasizing high frequencies gives roll-off (p. 13-27).

**Limits of robust design (p. 13-27, 13-28).** Sometimes process variations are so large that no linear controller gives a robust system with good performance. If a measured variable correlates with the variations, use **gain scheduling** (controllers designed for different parameter values, selected by the measured signal; Section 8.5). The cruise controller could schedule on gear position and velocity, and aircraft on Mach number and dynamic pressure. Switching must avoid bad transients (bumpless transfer) (p. 13-27). If such variables cannot be measured, use automatic tuning (measure the process by perturbing it, then design; needs constant parameters; widely applied to PID) or adaptive methods when parameters change (p. 13-28).

### 13.5 Further Reading (p. 13-28)
The text lists history and references. Robustness was central in classical control (Bode, James–Nichols–Phillips, Horowitz). The text says QFT can be regarded as an extension of Bode's work. The gap metric came from Zames and El-Sakkary and the graph metric from Vidyasagar. The ν-gap, "the proper notion," is due to Vinnicombe. Robustness was de-emphasized by optimization-based design; the strong robustness of state feedback (Anderson and Moore) added to optimism. The poor robustness of output feedback (Rosenbrock, Horowitz, Doyle) renewed interest. Doyle–Glover–Khargonekar–Francis showed that Riccati equations give a low-order controller. Nonlinear extensions treat the problem as a game against an adversarial disturbance (p. 13-28).

## Toy example (ours, not from the text)
Process $P=1/(s+1)$, proportional controller C = 4. Then $L=4/(s+1)$, $T=\dfrac{4}{s+5}$, $S=\dfrac{s+1}{s+5}$.

1. $|T(i\omega)|=4/\sqrt{25+\omega^2}$. At ω = 0: 0.8. At ω = 3: $4/\sqrt{34}=0.686$. So $M_t=0.8$.
2. Bound (13.10): $|\delta|<1/|T|$ is 1.25 at ω = 0 and $\sqrt{34}/4=1.458$ at ω = 3. The bound is smallest at ω = 0 (the maximum of |T|).
3. Test a constant relative error, $\tilde P=P(1+\delta)$. The closed-loop pole is the zero of $s+1+4(1+\delta)=s+5+4\delta$.
   - δ = 1.2: pole at −9.8 (stable).
   - δ = −1.2: pole at −0.2 (stable).
   - δ = −1.25: pole at 0 (marginal), exactly where $|\delta|=1/|T(0)|$.
   Here the bound is reached at a real negative δ at ω = 0; as the text says, the bound is conservative for other perturbation directions.
4. Sensitivity (13.23) with F = 1: at ω = 0, $S=1/5=0.2$. A 10% error in P should give about 2% error in $G_{yr}=T$. Check: with $\tilde P=1.1/(s+1)$, $\tilde T(0)=4.4/5.4=0.8148$ versus 0.8, an increase of 1.85%. This agrees with 2% for a small dP.

## Concepts
- [[robustness]] — closed loop stays stable and performs well despite model error (p. 13-1)
- [[parametric-uncertainty]] (new) — plant parameters not precisely known; checked by sweeping them (p. 13-1)
- [[unmodeled-dynamics]] (new) — neglected mechanisms, represented by a bounded transfer function Δ, δ or $\Delta_{fb}$ (p. 13-3)
- [[robust-stability]] (new) — stability for all uncertainties inside a given bound (p. 13-3)
- [[vinnicombe-metric]] (new) — ν-gap: sup of chordal distance if winding condition holds, else 1 (p. 13-7)
- [[chordal-metric]] (new) — distance between points projected on a sphere (p. 13-6)
- [[sensitivity-function]] (new) — S = 1/(1+PC); scales relative process error in $G_{yv}$, $G_{yr}$ (p. 13-16)
- [[complementary-sensitivity]] (new) — T = PC/(1+PC); sets the robust-stability bound 1/|T| (p. 13-10)
- [[small-gain-theorem]] (new; Theorem 10.4 referenced) — loop gain below 1 gives stability; used for Table 13.1 (p. 13-12)
- [[nyquist-criterion]] — encirclement test used to bound allowed perturbations (p. 13-10)
- [[youla-parameterization]] (new) — all stabilizing controllers via a free stable Q (p. 13-13)
- [[gang-of-four]] (new) — S, PS, CS, T (p. 13-14)
- [[high-frequency-rolloff]] (new) — small controller gain at high frequency to limit noise injection (p. 13-17)
- [[lqr]] — state feedback minimizing $\int(y^2+\rho u^2)dt$; phase margin ≥ 60°, infinite gain margin (p. 13-23)
- [[kalman-filter]] — observer with gains from an optimization, optimal for Gaussian noise (p. 13-23)
- [[h-infinity-control]] (new) — minimize $\|\mathcal G(P,C)\|_\infty$ (p. 13-24)
- [[generalized-stability-margin]] (new) — $\sigma_m=1/\|\mathcal G\|_\infty$ for stabilizing C (p. 13-25)
- [[quantitative-feedback-theory]] (new) — loop shaping so T varies little over the uncertainty region (p. 13-22)
- [[gain-scheduling]] (new) — switching controllers by a measured variable correlated with parameters (p. 13-27)
- [[stability]] — closed loop is stable when its characteristic polynomial has no right half-plane zeros, as used in Example 13.4 (p. 13-5)

## Canonical instances
- [[cruise-control]] — PI controller robust to mass, gear, speed variations; bound with $M_t=1.17$ (p. 13-2, 13-11)
- [[open-vs-closed-loop-similarity]] — Examples 13.2–13.4: open-loop closeness does not match closed-loop closeness (p. 13-4, 13-5)
- [[bode-ideal-loop-transfer-function]] — $L=ks^{-n}$ gives phase margin independent of gain (p. 13-13)
- [[op-amp-feedback-amplifier]] — closed loop near ideal ratio $R_2/R_1$ when G is large (p. 13-18)
- [[afm-nanopositioner]] — pole-cancelling PID versus active-damping PID (p. 13-19 to 13-21)

## Bridges (candidates)
- [structural-analogy] $\delta_\nu$ via the Riemann sphere ↔ geometry: chordal distance on the sphere — a metric on transfer functions.
- [same-math] $dG/G=S\,dP/P$ ↔ sensitivity analysis: the relative-change (logarithmic) derivative of a closed-loop function with respect to a parameter.
- [structural-analogy] Youla Q (all stabilizers; affine in Q) ↔ convex optimization: searching over Q gives a convex-looking search space (the text says only "useful for optimization").
- [metaphor] Black's "excess gain thrown away by feedback" ↔ error-correcting redundancy: spend gain to buy insensitivity.
- [metaphor] H∞ design as a game against an adversarial disturbance (mentioned in 13.5) ↔ game theory: worst-case player.

## Questions this raises
- The robust-stability bound is sufficient but conservative. How much larger can real perturbations be when their direction in the complex plane is known?
- How does the ν-gap handle delays and resonant systems with many peaks, which the text marks as an exception to the "model only near crossover" rule?
- Why does adding an observer to LQR destroy its guaranteed margins, and how does LQG/LTR-style design address this (not covered here)?
- How should a designer choose the weight W in practice to meet integral-action and roll-off specs together?

## Exercises worth doing
- Ex. 13.1 (p. 13-29) — which uncertainty forms allow continuous change between $P_1$ and $P_2$; builds feel for additive vs multiplicative vs feedback forms — difficulty: medium
- Ex. 13.3 (p. 13-29) — difference of T for two processes; compare with chordal metric (13.6) — difficulty: easy
- Ex. 13.4 (p. 13-29) — compute ν-gap among three simple processes for k = 1, 2 — difficulty: medium
- Ex. 13.6 (p. 13-29) — modify (13.10) to guarantee a specified stability margin — difficulty: medium
- Ex. 13.7 (p. 13-29) — from $M_s=2$ get phase margin ≥ 30° and 50% gain tolerance — difficulty: easy
- Ex. 13.10 (p. 13-30) — ideal delay compensator is unstable for arbitrarily small delay changes; shows nominal performance without robustness — difficulty: medium
- Ex. 13.12 (p. 13-30) — singular values of $\mathcal G(P,C)$ and $\bar\sigma=1/\delta_\nu(P,-1/C)$ — difficulty: hard

## Reading notes
- Printed page numbers "13-k" are visible in the page headers/footers (text layer and images), although the unit metadata listed printed pages as unknown. Offset: pdf = 434 + k (the chapter starts at pdf 435 = 13-1). Citations use (p. 13-k).
- Example 13.2, eq. (13.2): the image shows the $T_2$ denominator as $s^3T^2+(T^2+2T)s^2T+(1+2T)s+1+k$. Expanding $(s+1)(sT+1)^2+k$ gives $(T^2+2T)s^2$ with no extra T. The stated stability range $k<2T+4+2/T$ matches the expanded form (my Routh check).
- Eq. (13.15) text: "Np = dp/fp, Dp = np/fp" looks swapped relative to $P=N_p/D_p$ and the pattern for $N_c$, $D_c$ (I would expect $N_p=n_p/f_p$, $D_p=d_p/f_p$).
- Eq. (13.29): $k_d$ is printed with $2\zeta_c/\omega_0$. Matching coefficients in (13.27) and (13.28) gives $2\zeta/\omega_0$, with ζ the process damping. Eq. (13.30) writes $k$ in the numerator where $k_i$ is expected.
- Eq. (13.38) intermediate line "4 sin(φm/2) ≥ 4σm²" lacks a square on the sine; the line before it has $|1-e^{i\varphi_m}|^2=4\sin^2(\varphi_m/2)$.
- p. 13-11: the text states the 50% / 30° result for $M_t=2$ and cites Exercise 13.7, but Exercise 13.7 is posed with $M_s=2$.
- Example 13.6: the text mentions the right half-plane pole of $P_2$ while condition (13.7) involves $P_2(-s)$; I could not reconcile the stated case split (δν = 1 for k ≤ 1) with the formula and report it as printed. Fig. 13.6 caption writes $P_2=k/(-s+1)$.
- Example 13.10: S and T are printed with $\alpha b$ (e.g. $T=\alpha b/(s+a+\alpha b)$). From the printed $G_{v_2v_1}$ formula I would expect the loop gain to be $G R_1/(R_1+R_2)$. I report the printed forms as given.
- The relation $\Delta_{fb}=\Delta/(P(P+\Delta))$ (p. 13-4) has no minus sign. With the form $P/(1+\Delta_{fb}P)$ of Table 13.1, my algebra gives a minus sign; the sign convention of Fig. 13.2c may explain it.
- p. 13-16: after (13.19) the text writes "$G_{yu}$" where $G_{yv}$ is meant.
- Fig. 13.14 caption/legend line styles for $\omega_c=2\omega_0$ and $4\omega_0$ appear to differ between caption and plot legend.
- A margin symbol appears beside the headings "The Vinnicombe Metric", "Youla Parameterization", "13.4 Design for Robust Performance" and "H∞ Control"; these pages do not explain what it means.
