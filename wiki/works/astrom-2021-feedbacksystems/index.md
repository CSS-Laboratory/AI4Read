---
id: astrom-2021-feedbacksystems/index
work: astrom-2021-feedbacksystems
type: work-map
units: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch13-robust, astrom-2021-feedbacksystems/ch14-fundamental, astrom-2021-feedbacksystems/ch15-architecture-p1, astrom-2021-feedbacksystems/ch15-architecture-p2]
---

# Åström, K. J., & Murray, R. M. (2021). *Feedback Systems: An Introduction for Scientists and Engineers* (2nd ed.). Princeton University Press. ISBN 9780691193984.

## In one paragraph
The book teaches feedback as a general idea for science and engineering. Corrective action based on the error between desired and actual behaviour makes systems robust to disturbances and uncertainty. It also reshapes their dynamics, but it can cause instability and inject noise. The authors build the tools to analyse this. They start with state-space models and stability. They then design state feedback, observers, LQR and the Kalman filter. Next come transfer functions, Bode and Nyquist analysis, PID control and frequency-domain design. Robustness and fundamental limits follow: some things no controller can do. The book ends with system architecture, interaction between loops, adaptation and learning. Examples range from cruise control and bicycles to drugs, populations and gene circuits. It matters because feedback appears everywhere, and intuition about loops often fails.

## The path through the work
- [[astrom-2021-feedbacksystems/ch01-introduction]] — Feedback means basing corrective action on the difference between desired and actual performance; this simple idea gives robustness, reshapes dynamics and enables modular design, but it can also cause instability and inject noise.
- [[astrom-2021-feedbacksystems/ch02-feedback]] — Negative feedback (a correction that opposes the error between target and output) makes a system less sensitive to disturbances and parameter changes and helps its output follow a target, while positive feedback (a correction that adds to the signal) has complementary properties, and transfer functions give the algebra to analyse both.
- [[astrom-2021-feedbacksystems/ch03-system-p1]] — A model is a precise representation of a system's dynamics (yet only an approximation of the real system), and in control it is often written as a state space model: first-order differential equations (continuous time) or difference equations (discrete time) in state, input and output.
- [[astrom-2021-feedbacksystems/ch03-system-p2]] — A few tools (block diagrams, experiments, scaling, differential-equation models) let you build and simplify models of very different systems, and the right level of detail often depends on experience and on the question asked.
- [[astrom-2021-feedbacksystems/ch04-examples]] — Seven everyday and scientific systems (car, bicycle, op amp, web server and Internet, atomic force microscope, drug and glucose dynamics, populations) are each reduced to a small model with a state, inputs and outputs; for several of them the author also says where the model stops being valid.
- [[astrom-2021-feedbacksystems/ch05-dynamic]] — Stability of equilibria and other solutions of nonlinear systems can be judged by phase portraits, by linearization (eigenvalues of the Jacobian), or by an energy-like Lyapunov function, and linearization and Lyapunov functions can also be used to design feedback.
- [[astrom-2021-feedbacksystems/ch06-linear]] — A linear time-invariant system is completely described by the matrix exponential $e^{At}$ and the convolution equation, and a nonlinear system near an equilibrium can be approximated by a linear one (Jacobian linearization).
- [[astrom-2021-feedbacksystems/ch07-state]] — If a single-input linear system is reachable, feeding back its full state can place the closed-loop eigenvalues anywhere, so the designer can shape the dynamics directly; practical limits are actuator size, the choice of eigenvalues, and the need for exact calibration (integral action removes the calibration need; an optimal cost is another way to choose the gains).
- [[astrom-2021-feedbacksystems/ch08-output]] — If a linear system is reachable and observable, an observer (a model corrected by the measured output) can rebuild the hidden state, and feeding back that estimate gives a closed loop whose eigenvalues are those of the state-feedback design together with those of the observer, so the two designs can be done separately.
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] — A linear time-invariant system's response to the exponential input $e^{st}$ contains the pure exponential part $G(s)e^{st}$, and this single function $G(s)$ lets you compute with systems and block diagrams by algebra.
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] — A transfer function's gain, poles and zeros, and its Bode plot (gain and phase against frequency), tell you at a glance how a linear system responds to signals, which cancellations are dangerous, and which model features limit control.
- [[astrom-2021-feedbacksystems/ch10-frequency]] — Stability and robustness of a feedback loop can be read from how sinusoids travel around the loop, i.e. from the shape of the open-loop frequency response $L(i\omega)$ relative to the critical point $-1$ (the Nyquist criterion and the margins built on it).
- [[astrom-2021-feedbacksystems/ch11-pid]] — PID control adds three terms (present error, accumulated error, predicted error), and the integral term guarantees zero steady-state error if a steady state exists. Practical use also needs tuning rules, anti-windup, derivative filtering and careful implementation.
- [[astrom-2021-feedbacksystems/ch12-frequency]] — Closed-loop behaviour (tracking, disturbance rejection, noise, robustness) is described by a few transfer functions formed from $P$, $C$ and $F$ that all have $1+L$ in the denominator, where $L=PC$ is the loop transfer function, so a controller can be designed by shaping $L$ in frequency, with feedforward added for reference response.
- [[astrom-2021-feedbacksystems/ch13-robust]] — Feedback tolerates model errors: stability is guaranteed (by a conservative test) when the relative error stays below 1/|T| at each frequency, relative errors in closed-loop responses are scaled by the sensitivity functions S or T, and the ν-gap metric is the proper way to compare a process with its model for feedback.
- [[astrom-2021-feedbacksystems/ch14-fundamental]] — Right half-plane (RHP) poles and zeros, time delays, and actuator and noise limits put fundamental limits on achievable feedback performance and robustness, and many of these limits can be written as simple inequalities.
- [[astrom-2021-feedbacksystems/ch15-architecture-p1]] — Real control systems are built by arranging simple feedback loops inside a designed architecture, either top-down (layers, optimization, logic specifications, verification) or bottom-up (loop-by-loop structures such as cascade, selector and Smith predictor).
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] — Building a control system loop by loop can create hidden interactions (measured by the relative gain array, and shown by parallel integrators), and when the process is uncertain the controller itself can adapt or learn (adaptive control, neural networks).

## Big ideas across units
- **Feedback's benefits and costs.** Feedback gives robustness, redesigned dynamics and modularity. It risks instability, noise injection and complexity. Positive feedback is the complementary case, needing saturation to limit growth. Units: ch01-introduction, ch02-feedback, ch04-examples, ch13-robust, ch14-fundamental.
- **Models as state-space approximations.** Every model is an approximation, valid only in limited ranges. State-space models, linearization and linear-system tools let linear design stand in for nonlinear systems. Units: ch03-system-p1, ch03-system-p2, ch04-examples, ch05-dynamic, ch06-linear.
- **Stability in several guises.** Stability is treated through transfer-function roots (Routh–Hurwitz), Lyapunov and energy arguments, eigenvalues and linearization, and finally the Nyquist criterion and margins. Units: ch02-feedback, ch03-system-p1, ch03-system-p2, ch05-dynamic, ch06-linear, ch09-transfer-p2, ch10-frequency.
- **Integral action and PID.** Integral action removes steady-state error under constant disturbances. It reappears as a PI design, an augmented state, an estimated disturbance, a practical PID with anti-windup, and a central integrator across parallel actuators. Units: ch01-introduction, ch02-feedback, ch07-state, ch08-output, ch11-pid, ch15-architecture-p2.
- **Reachability, observability and separated design.** Reachability enables eigenvalue assignment and LQR. Observability enables observers and the Kalman filter. The two designs separate. The same properties explain pole/zero cancellation and hidden modes. Units: ch07-state, ch08-output, ch09-transfer-p1, ch09-transfer-p2, ch15-architecture-p2.
- **Transfer functions and frequency-domain thinking.** From the first transfer-function algebra to Bode plots, Nyquist, loop shaping and the Gang of Four. Units: ch02-feedback, ch06-linear, ch09-transfer-p1, ch09-transfer-p2, ch10-frequency, ch12-frequency.
- **Robustness and fundamental limits.** Feedback tolerates model error (the 1/|T| condition, ν-gap). RHP poles and zeros, delays and the waterbed effect set limits no controller can beat. Units: ch02-feedback, ch10-frequency, ch12-frequency, ch13-robust, ch14-fundamental.
- **Logic, layers and architecture.** Real systems combine loops with logic, selectors and layered decisions, and may add adaptation or learning. Units: ch01-introduction, ch03-system-p1, ch15-architecture-p1, ch15-architecture-p2.

## How to read it
- **Essential first pass.** The catalog's focus covers Ch. 1, 2, 4, 5 (stability), 7 (reachability, LQR), 8 (observability, Kalman filtering) and 11 (PID). Read ch01 and ch02 first, since all later units build on their ideas.
- **Dependencies from the stated prerequisites.**
  - ch03 (modelling) feeds ch04 (examples), which also needs PI control from ch01.
  - ch05 and ch06 build on the state-space models of ch03.
  - ch07 needs the linear-system tools of ch06. ch08 needs ch07 (reachability, LQR, Riccati equation).
  - ch09 needs reachability and observability, and the Kalman decomposition from ch08.
  - ch10 needs transfer functions and Bode plots (ch09).
  - ch11 assumes transfer functions, Nyquist and Bode plots.
  - ch12 needs Nyquist, margins and PID. ch13 needs ch10 and ch12 (S, T, Gang of Four).
  - ch14 needs sensitivity functions, Bode and Nyquist, and state feedback with observers.
  - ch15 part 1 needs ch12, ch11 (windup) and ch07. Part 2 needs reachability, observability and pole–zero cancellation.
- **Reasonable to skim or defer on a first pass.** These are illustrative or advanced, going by their L1 descriptions.
  - The gallery of examples in ch03-system-p2.
  - The application fields and the neural-network material at the end of ch15-architecture-p2.
  - The late robust-design and limits chapters (ch13, ch14), which are not in the catalog focus.

## Concepts introduced
Spelling variants of the same concept in different units are merged under one id.

**Ch. 1 Introduction** ([[astrom-2021-feedbacksystems/ch01-introduction]])
- [[feedback]]
- [[open-loop-vs-closed-loop]]
- [[negative-feedback]]
- [[positive-feedback]]
- [[feedforward]]
- [[reference-set-point]]
- [[error-signal]]
- [[plant]]
- [[disturbance-and-noise]]
- [[delay-dead-time]]
- [[gain]]
- [[stability]]
- [[pid-control]]
- [[integral-action]]
- [[robustness]]
- [[homeostasis]]
- [[on-off-control]]
- [[control-law]]
- [[integrator-windup]]
- [[cascaded-loops-modularity]]
- [[finite-state-machine]]
- [[selector]]
- [[layered-control-architecture]]
- [[hybrid-system]]

**Ch. 2 Feedback Principles** ([[astrom-2021-feedbacksystems/ch02-feedback]])
- [[transfer-function]]
- [[linearization]]
- [[linear-range]]
- [[sensitivity]]
- [[saturation]]
- [[hysteresis]]
- [[poles-and-zeros]]
- [[routh-hurwitz-criterion]]
- [[natural-frequency-damping-ratio]]
- [[unmodeled-dynamics]]
- [[bandwidth]]
- [[two-degrees-of-freedom]]
- [[regulation-and-servo-problem]]

**Ch. 3 System Modeling, part 1** ([[astrom-2021-feedbacksystems/ch03-system-p1]])
- [[state]]
- [[state-space-model]]
- [[controllability-reachability]]
- [[observability]]
- [[difference-equation]]
- [[euler-integration]]
- [[phase-portrait]]
- [[linear-time-invariant-system]]
- [[step-response]]
- [[frequency-response]]
- [[differential-algebraic-equation]]
- [[model-uncertainty]]
- [[energy-function-stability-argument]]

**Ch. 3 System Modeling, part 2** ([[astrom-2021-feedbacksystems/ch03-system-p2]])
- [[block-diagram]]
- [[algebraic-loop]]
- [[system-identification]]
- [[normalization-scaling]]
- [[inverse-response]]
- [[flow-model]]
- [[hill-function]]
- [[graph-laplacian]]

**Ch. 4 Examples** ([[astrom-2021-feedbacksystems/ch04-examples]])
- [[compartment-model]]
- [[uncertainty-lemon]]
- [[equilibrium-point]]
- [[logistic-growth]]
- [[limit-cycle]]

**Ch. 5 Dynamic Behavior** ([[astrom-2021-feedbacksystems/ch05-dynamic]])
- [[asymptotic-stability]]
- [[lipschitz-continuity]]
- [[finite-escape-time]]
- [[eigenvalues-and-modes]]
- [[lyapunov-function]]
- [[lyapunov-equation]]
- [[invariance-principle]]
- [[region-of-attraction]]
- [[bifurcation]]
- [[root-locus]]
- [[control-lyapunov-function]]

**Ch. 6 Linear Systems** ([[astrom-2021-feedbacksystems/ch06-linear]])
- [[linear-system-superposition]]
- [[time-invariance]]
- [[matrix-exponential]]
- [[jordan-form]]
- [[convolution-equation]]
- [[impulse-response]]
- [[transient-vs-steady-state]]
- [[bode-plot]]
- [[bandwidth-and-dc-gain]]
- [[coordinate-transformation]]
- [[sampling]]
- [[feedback-linearization]]

**Ch. 7 State Feedback** ([[astrom-2021-feedbacksystems/ch07-state]])
- [[state-feedback-pole-placement]]
- [[reachability-matrix]]
- [[reachable-canonical-form]]
- [[dynamic-compensator]]
- [[dominant-eigenvalues]]
- [[lqr]]
- [[riccati-equation]]
- [[ackermann-formula]]

**Ch. 8 Output Feedback** ([[astrom-2021-feedbacksystems/ch08-output]])
- [[observability-matrix]]
- [[observer]]
- [[duality]]
- [[separation-principle]]
- [[internal-model-principle]]
- [[kalman-filter]]
- [[kalman-gain]]
- [[kalman-decomposition]]
- [[differential-flatness]]
- [[gain-scheduling]]
- [[extended-kalman-filter]]

**Ch. 9 Transfer Functions, part 1** ([[astrom-2021-feedbacksystems/ch09-transfer-p1]])
- [[exponential-signal]]
- [[frequency-domain-modeling]]
- [[realization]]
- [[pole-zero-cancellation]]
- [[laplace-transform]]
- [[block-diagram-algebra]]
- [[generalized-impedance]]

**Ch. 9 Transfer Functions, part 2** ([[astrom-2021-feedbacksystems/ch09-transfer-p2]])
- [[zero-frequency-gain]]
- [[frequency-response-identification]]

**Ch. 10 Frequency Domain Analysis** ([[astrom-2021-feedbacksystems/ch10-frequency]])
- [[loop-transfer-function]]
- [[nyquist-criterion]]
- [[critical-point]]
- [[winding-number]]
- [[principle-of-variation-of-the-argument]]
- [[conditional-stability]]
- [[gain-margin]]
- [[phase-margin]]
- [[stability-margin]]
- [[delay-margin]]
- [[minimum-phase-system]]
- [[hinf-norm-system-gain]]
- [[small-gain-theorem]]
- [[passivity]]
- [[circle-criterion]]
- [[describing-function]]

**Ch. 11 PID Control** ([[astrom-2021-feedbacksystems/ch11-pid]])
- [[anti-windup]]
- [[ziegler-nichols-tuning]]
- [[fotd-model]]
- [[relay-autotuning]]
- [[setpoint-weighting]]
- [[derivative-filtering]]
- [[average-residence-time]]

**Ch. 12 Frequency Domain Design** ([[astrom-2021-feedbacksystems/ch12-frequency]])
- [[sensitivity-function]]
- [[complementary-sensitivity]]
- [[gang-of-four-six]]
- [[loop-shaping]]
- [[lead-lag-compensation]]
- [[bode-phase-area-formula]]
- [[approximate-inverse]]
- [[rise-time-bandwidth-product]]
- [[inner-outer-loop-design]]

**Ch. 13 Robust Performance** ([[astrom-2021-feedbacksystems/ch13-robust]])
- [[parametric-uncertainty]]
- [[robust-stability]]
- [[vinnicombe-metric]]
- [[chordal-metric]]
- [[youla-parameterization]]
- [[high-frequency-rolloff]]
- [[h-infinity-control]]
- [[generalized-stability-margin]]
- [[quantitative-feedback-theory]]

**Ch. 14 Fundamental Limits** ([[astrom-2021-feedbacksystems/ch14-fundamental]])
- [[stabilizability]]
- [[strong-stabilizability]]
- [[pbh-test]]
- [[non-minimum-phase]]
- [[all-pass-factor]]
- [[bode-integral-formula]]
- [[gain-crossover-frequency-inequality]]
- [[maximum-modulus-principle]]
- [[actuator-saturation]]

**Ch. 15 Architecture and System Design, part 1** ([[astrom-2021-feedbacksystems/ch15-architecture-p1]])
- [[co-design]]
- [[architecture-control-system]]
- [[design-v-model]]
- [[model-based-design-hil]]
- [[smoothness-of-models]]
- [[bowtie-hourglass-patterns]]
- [[model-predictive-control]]
- [[temporal-logic-ltl]]
- [[vertical-contract]]
- [[model-checking]]
- [[program-synthesis]]
- [[cascade-control]]
- [[mid-range-control]]
- [[internal-model-control]]
- [[smith-predictor]]

**Ch. 15 Architecture and System Design, part 2** ([[astrom-2021-feedbacksystems/ch15-architecture-p2]])
- [[relative-gain-array]]
- [[complementary-filter]]
- [[extremum-seeking]]
- [[parallel-subsystems-central-integrator]]
- [[model-reference-adaptive-control]]
- [[self-tuning-regulator]]
- [[certainty-equivalence]]
- [[recursive-least-squares]]
- [[persistent-excitation]]
- [[dual-control]]
- [[artificial-neural-network]]
- [[convolutional-neural-network]]
