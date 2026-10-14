---
id: todorov-2002-ofc/main
work: todorov-2002-ofc
unit: paper
pages: 1-10
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Optimal feedback control as a theory of motor coordination

## L0 — One line
An optimal feedback controller corrects only those deviations that hurt the task, so it lets variability pile up in redundant (task-irrelevant) directions, which, the authors argue, explains many coordination phenomena.

## L1 — The gist (≤ 120 words)
Motor behaviour reaches goals reliably, yet movement details vary from trial to trial, mostly in directions that do not matter for the task. Serial "plan a trajectory, then track it" models struggle with this. Todorov and Jordan propose stochastic optimal feedback control, with signal-dependent noise (noise that grows with the command size) and delayed, noisy sensing. They argue that the optimal law follows a "minimal intervention" principle. They show this with a local analysis for a general class of systems. Simulations and five experiments (two are reanalyses) support it. Synergies (coupled control directions), controlled parameters, simplifying rules and discrete coordination modes then emerge without being built in. Redundancy becomes part of the solution, not a problem.

**Prerequisites:** expectation and variance; gradient and Hessian; dynamic programming (cost-to-go); linear systems with a quadratic cost and Kalman filtering; PCA.

## L2 — Key ideas (5–10 bullets)
- Serial planning/execution models replace the goal by one desired trajectory. The authors call this incompatible with task-constrained variability and goal-directed corrections (p. 1).
- Their theory assumes signal-dependent noise, delayed and noisy sensors, an internal forward model, an outcome-based cost and a quadratic effort penalty. The control law is left unconstrained (pp. 2–3).
- Minimal intervention principle: deviations from the average trajectory are corrected only when they interfere with task performance (p. 3). A one-step example illustrates it (p. 3).
- General local analysis: with $v^*$ the optimal cost-to-go, a deviation is redundant if $\Delta v^*=0$. Correction and $\Delta v^*$ are dot-products of the same vectors, so redundant deviations get no correction (p. 4).
- Experiments on trajectory redundancy (targets added or resized, hitting) show variance lowered where accuracy matters and raised elsewhere. Paper-ball making shows very large joint variability with always-successful outcomes (pp. 5–6).
- A telescopic-arm model yields synergies, apparent "frozen" joints, a hierarchy of controlled parameters, low resistance to task-irrelevant perturbations and two preferred relative-phase modes (pp. 7–8).
- Redundancy exploitation grows with mechanical complexity, and a generic reinforcement learner finds it early (p. 8).
- Limits: linear LQG simulations and no explicit treatment of learning. The authors say their general analysis assures them the basic phenomena will stay qualitatively the same in nonlinear models (p. 9).

## L3 — Walkthrough

### Introduction (pp. 1–2)
**Problem.** The body has more degrees of freedom than a task needs. Two facts seem to conflict (p. 1):
- High-level goals are reached reliably.
- Trial-to-trial fluctuations in single degrees of freedom are on average larger than fluctuations in task-relevant parameters. Variability lies in a redundant subspace (the "uncontrolled manifold") and is not suppressed (p. 1).

Perturbations are also compensated so as to keep task performance, not a stereotyped pattern (p. 1).

**Serial models (the view criticised).** Planning picks one desired trajectory and execution tracks it. The authors say the evidence is incompatible with this: it indicates that execution mechanisms can tell crucial details from irrelevant ones, which would be impossible if the goal were replaced by a specific trajectory (p. 1).

**Functional synergies (another view).** Synergies are high-level "control knobs". The authors say how they are constructed, what control scheme uses them and why the motor system should prefer them remain unclear (p. 1).

**Their proposal.** Treat coordination as stochastic optimal feedback control. They argue that stereotypy comes from separating planning and execution, a choice made for simplicity and not for optimality (pp. 1–2).

**Key claim.** Optimal performance is achieved by a feedback law that resolves redundancy moment by moment, whenever all three conditions hold (p. 2):
- the task allows redundant solutions;
- movement duration exceeds the shortest sensorimotor delay;
- the initial state or the consequences of controls are uncertain.

**Relation to dynamical-systems views.** Optimal control and plant together give a specific dynamical system, with no trajectory/execution split. The difference: here the control law is predicted by optimizing a simple criterion, not inferred from data (p. 2).

### Optimality principles in motor control (pp. 2–3)
- Optimality gives computational-level theories. They say why behaviour is as it is, not how the nervous system implements or learns it (p. 2).
- Assumptions (p. 2):
  - **Noise:** signal-dependent (multiplicative). Isometric data show muscle-force s.d. grows linearly with the mean.
  - **Sensing:** the plant is seen only through delayed, noisy sensors, so an internal forward model integrates feedback, plant dynamics and an efference copy of past controls to estimate the state.
  - **Cost:** based on task outcome (instructions) plus a quadratic effort penalty. Reasons given: spending energy hurts future tasks, and people are often "lazy". The true extra term should grow faster than linearly, since larger forces recruit more rapidly fatiguing motor units.
- Under multiplicative noise, endpoint variance is minimal when the open-loop desired trajectory is smooth (cited result). This motivates outcome-based indices, though optimal feedback control is not guaranteed to reproduce it (p. 2).
- The key difference from trajectory planning is the constraint on the control law. LQG controllers here face no control constraints. Unknown biological information-processing limits are lumped into two scalars, sensory and motor noise magnitude, tuned to match overall variability. These give little control over the structure of predicted variability (p. 3).

### Results: the minimal intervention principle (pp. 3–4)
**Statement.** Deviations from the average trajectory are corrected only when they interfere with task performance. If this principle holds and noise perturbs the system in all directions, the interplay of noise and control will cause larger variability in task-irrelevant directions. Uncorrected deviations mean unused control dimensions, which is what is read as evidence for synergies (p. 3).

**Why it should hold.** A controller concerned only with task performance gains nothing from correcting irrelevant deviations. A corrective control can even be harmful, because noise and effort are control-dependent (p. 3).

**One-step example (p. 3).** Choose $u_1,u_2$ to minimize
$$E_\varepsilon\,(x_1^{final}+x_2^{final}-X^*)^2 + r(u_1^2+u_2^2),$$
with
$$x_i^{final}=a x_i+u_i(1+\sigma\varepsilon_i),\quad i\in\{1,2\},$$
where $\varepsilon_i$ are independent, mean 0, variance 1. The task is $x_1+x_2=X^*$ at minimal effort.
- Define $Err = a(x_1+x_2)-X^*$, the expected task error when $u_1=u_2=0$.
- (added step) The expected cost equals $(Err+u_1+u_2)^2+(r+\sigma^2)(u_1^2+u_2^2)$.
- For unbiased control the optimal controls minimize $(r+\sigma^2)(u_1^2+u_2^2)$ subject to $u_1+u_2=-Err$. The unique optimal law is $u_1=u_2=-Err/2$.
- $Err$ depends on $x_1+x_2$ only. A task-irrelevant deviation (add a constant to $x_1$, subtract it from $x_2$) triggers no response. The resulting variability is elongated in the redundant dimension (Fig. 1, left).

**Contrast: eliminating redundancy.** Take the optimal controller's average behaviour as the desired state, $x_1^{final}=x_2^{final}=X^*/2$. The control law is $u_i=X^*/2-a x_i$, which is suboptimal. It gives symmetric variability (Fig. 1, right). Fig. 1 setup: $X^*=2$, $a=\sigma=0.8$, 20,000 starts from a circular Gaussian (mean (1,1), variance 1). The optimal law gets low task error by letting the redundant dimension vary, a "noise buffer". Suppressing it costs more variability in the dimension that matters (p. 3; setup in the Fig. 1 caption, p. 2).

**Two by-products (p. 4).** The optimal controls are synergetically coupled, because the synergy is the optimal solution, not a simplification. They are also smaller than the controls needed to hit the best desired state.

*Intuition note.* The controller ignores deviations that do not change the outcome, since acting on them costs effort and adds noise. Those deviations then pile up as variability along the redundant direction.

**General formalization (p. 4).**
- Let $v^*(t,x)$ be the optimal cost-to-go: the expected cumulative cost if the plant is in $x$ at time $t$ and $\pi^*$ is used until the end. Instantaneous cost: $q(t,x)+u^TR(t,x)u\ge 0$ ($q$ encodes task error, the second term effort), $x\in\mathbb{R}^m$, $u\in\mathbb{R}^n$.
- The authors define all states with equal $v^*$ as task-equivalent. With average trajectory $\bar x(t)$, the deviation $\Delta x$ is redundant if $\Delta v^*(\Delta x)=0$, where $\Delta v^*(\Delta x)=v^*(t,\bar x+\Delta x)-v^*(t,\bar x)$.
- At the end of a reaching movement this reduces to the kinematic notion of redundancy. During movement $v^*$ also depends on dynamics: completing a movement from states far from the target needs larger, costlier and noisier controls.
- Plant family:
$$dx = a(t,x)\,dt + B(t,x)\,u\,dt + \sum_{i=1}^k C_i(t,x)\,u\,d\varepsilon_i,$$
  with passive dynamics $a$, control dynamics $B$, multiplicative-noise magnitudes $C_i$ and independent standard Brownian motions $\varepsilon_i$.
- Expected state change from the optimal control: $\dot x_{\mathbf u}=B(t,\bar x+\Delta x)\,\pi^*(t,\bar x+\Delta x)$. Corrective action is the projection of $-\dot x_{\mathbf u}$ on $\Delta x$: $corr(\Delta x)\triangleq\langle\Delta x,-\dot x_{\mathbf u}\rangle$.
- The control law follows from $v^*$:
$$\pi^*(t,x)=-Z(t,x)^{-1}B(t,x)^T v_x^*(t,x),\qquad Z=2R+\sum_{i=1}^k C_i^T v_{xx}^* C_i,$$
  where $v_x^*$, $v_{xx}^*$ are the gradient and Hessian of $v^*$.
- Expanding $v^*$ to second order and its gradient to first order, with other quantities constant near $\bar x$, gives:
$$\Delta v^*(\Delta x)\approx\langle\Delta x,\;v_x^*+v_{xx}^*\Delta x\rangle,$$
$$corr(\Delta x)\approx\langle\Delta x,\;v_x^*+v_{xx}^*\Delta x\rangle_{BZ^{-1}B^T},\quad \langle a,b\rangle_M=a^TMb.$$
- Conclusions (p. 4):
  - When $v_x^*+v_{xx}^*\Delta x=0$, which can hold for infinitely many $\Delta x$ if the Hessian is singular, $\Delta x$ is redundant and the law takes no corrective action.
  - $corr$ and $\Delta v^*$ are positively correlated: the law resists deviations to more costly states and magnifies deviations to less costly ones.
  - So minimal intervention is a very general property of optimal feedback control.

*Intuition note.* The cost-to-go says how bad a state is. A deviation that leaves the cost-to-go unchanged gets no push-back. A deviation that raises it gets pushed back, in proportion.

### Mechanical redundancy (p. 5)
Static redundancy (Fig. 1) matches postural tasks. Prolonged behaviour was simulated for 0.5 s from the same start.
- **Sim 1, aiming:** a 2-D point mass moves about 20 cm and may end anywhere on a line of sight $X_2=X_1\tan(-20^\circ)$. Final positions cluster along that line, orthogonal to the task-error dimension (Fig. 2a).
- **Sim 2, intercept:** two 1-D point masses start 20 cm apart and must end at the same unspecified position. The covariance ellipsoid is again orthogonal to the task-error dimension. The authors cite similar findings in two-finger and two-arm interception.
- **Sensitivity of Intercept (Fig. 2b),** one parameter at a time:
  - The effect, aspect ratio greater than one, is very robust.
  - More motor noise raises overall variability and aspect ratio. More sensory noise raises variability but lowers aspect ratio (open loop makes exploitation impossible).
  - Sensory delay is roughly equivalent to extra sensory noise, since the forward model extrapolates delayed data (except when large abrupt perturbations are present).
  - Longer movement time lowers bias and variability and raises exploitation.
  - A larger effort penalty $R$ lowers exploitation. The authors call this counterintuitive, since the derivation needs $2R+\sum C_i^Tv_{xx}^*C_i$ positive-definite.

### Trajectory redundancy (pp. 5–6)
Experiments compare conditions with similar average trajectories but different task goals. The desired-trajectory hypothesis predicts no difference.
- **Experiment 1** (8 subjects, planar arm movements, Fig. 3a): condition A has 5 widely spaced targets. Condition B adds 16 targets along A's average path. Model (Sim 3): in A, variability is allowed between targets. In B it becomes more nearly constant, rising at the original targets and falling between them. Results:
  - In A, variance at targets was 0.14 ± 0.01 cm², smaller than 0.26 ± 0.03 cm² at midpoints (P < 0.01).
  - In B, the values were 0.18 ± 0.02 and 0.18 ± 0.03 cm², no difference.
  - Compared with A, variance rose at the original targets (P < 0.05) and fell between them (P < 0.01).
  - Average behaviour in A and B was not identical, but the differences cannot account for the change in variability under the desired-trajectory hypothesis (Supplementary Notes). Reanalysis of published experiment 2 confirmed it.
- **Experiment 3** (7 subjects, Sim 4, Fig. 3b): a smaller target should have lower variability and the other target higher. Observed: 0.34 ± 0.02 cm² at the smaller target versus 0.42 ± 0.02 cm² at the larger (P < 0.05).
- The authors conclude the motor system exploits redundancy of end-effector trajectories, and that this is necessarily due to online feedback. In open loop, variability would grow throughout the movement. In related experiments with vision of the hand blocked, positional variance was about twice as high (p. 6).
- **Hitting/throwing** (p. 6, Fig. 4). Experiment 4 is a reanalysis of published data: 9 subjects hitting ping-pong balls. The throwing model (Sim 5) lets the ball be released anywhere in a region. Its average trajectory then served as the desired trajectory for a tracking controller (Sim 6).
  - The tracker cancels start-position variability and is more repeatable, but has larger target error. The optimal controller is more accurate.
  - After release the optimal controller lets variance accumulate. In the data, end-point variance divided by impact-point variance was 7.6 ± 2.2, different from 1 (P < 0.05). The tracker brings it to almost zero.
  - In data and optimal control, positional variance peaks well before the reversal point. In the tracker it peaks near peak forward velocity.
  - Correlation of hand coordinates at impact/release with end-point coordinates is r ≈ 0.5 in data and optimal control, and near 0 for the tracker. The optimal controller does not correct deviations that do not matter, so temporal correlations stay high.

### Redundancy in object manipulation (pp. 6–7)
Experiment 5: five subjects turned paper sheets into balls (20 hand joint angles; Fig. 5).
- Joint variability at a single time point was comparable to the range of joint excursions along the average trajectory, yet every trial succeeded. The authors say a desired-trajectory executor this inaccurate would leave the hand dysfunctional (p. 6).
- PCA on postures at one time point shows elongated variability (Fig. 5c; 10 PCs for 95% variance).
- Bootstrap test (p. 7): build synthetic postures by taking each joint angle from a randomly chosen trial. This raises variability in below-average-variance subspaces and lowers it in above-average ones. If synthetic postures look inappropriate for the task (Fig. 5d), the real variability was smaller in task-relevant dimensions, so redundancy is exploited.
- Grasping a cylinder gives much more repeatable trajectories (Fig. 5a, b). The same joints, muscles and largely overlapping circuits thus yield very different variability, which the authors say calls for unified models. They say they will show elsewhere that optimal feedback control models have this property (p. 7).

### Emergent properties (pp. 7–8)
**Telescopic model.** $M$ point masses slide on a vertical pole under gravity. Single-joint actuators link points $0{:}1,\dots,M{-}1{:}M$ and double-joint ones link $0{:}2,\dots,M{-}2{:}M$ (point 0 is the fixed base). Lengths $X_1..X_M$ play the role of joint angles. The last point, at $X_1+\dots+X_M$, is the end-effector (p. 7).

- **Simplifying rule (Sim 7, $M=3$, 4 targets, Fig. 6a).** $X_2$ looks constant, a likely "simplifying rule" if seen in data. No rule is built in. The effect emerges from system symmetries (weaker for $X_2, X_4$ at $M=5$, absent for $M=2,4$). $X_2$ is not frozen: it fluctuates as much as $X_1$ and $X_3$ and more than the end-effector. All three joints are used to compensate for each other's fluctuations, but that information is lost when only the average is analysed (p. 7).
- **Synergies.** The number of synergies at time $t$ is the rank of $L_t$, which maps the state estimate to the control signal. This rank is the dimension of the control subspace the controller can span for any state distribution. At $M=10$ (19-D control, 40-D state), at most 4 dimensions are used (Fig. 6b). The structure of each synergy is preserved over time. One synergy disappears after each target. Synergy 1 can be read as moving to the current target, synergy 2 as preparing for the next, and so on (pp. 7–8).
- **Controlled parameters** ($M=2$, 4-target task). The index of performance was set on five levels: control signals, forces, joint angles, end-effector trajectory, end-effector at passage times. All five controllers have the same average behaviour. Variability is minimal on the level where the index is specified (Fig. 6c). For the task-optimal controller, variability increases with distance from the task. The same ordering holds for the joint-angle index and almost holds for the trajectory index. It fails for kinetic variables: forces and control signals vary more than kinematics even when specified. So the kinetic/kinematic difference is a property of the controlled mechanics, not the controller (p. 8).
- **Perturbations** ($M=2$, sinusoidal tracking, Sim 9; Fig. 6d). Random numbers added to all three control signals at one time (s.d. 30 N, per caption) changed the intermediate point a lot, while the end-effector returned quickly to the sinusoid. This agrees with cited experiments (p. 8).
- **Discrete coordination modes** (Fig. 6e). Across oscillation frequencies, the relative phase of end-effector ($X_1+X_2$) and intermediate point ($X_1$) shows two preferred modes, in phase and 180° out of phase, with a fairly sharp transition and larger phase fluctuations there. The same holds with additive noise (data not shown). The model is not directly applicable to two-finger tapping, but the effect is qualitatively similar to the sharp transition and phase fluctuations observed there (p. 8).
- **Mechanical complexity** ($M=1$ to 20, Sim 8). The observed-minus-reshuffled end-effector variability grows with $M$ (Fig. 6f, right). The cost ratio, optimal over a tracker with the same average joint trajectory, falls from 0.9 at $M=1$ to 0.22 at $M=20$ (p. 8).
- **Learning** (Sim 10, $M=2$ posture task). Starting from the optimal open-loop controller, a generic reinforcement learning algorithm modifies the feedback law's parameters. It found redundancy useful long before reaching the optimal feedback law (Fig. 6f, left) (p. 8).

*Intuition note.* Synergies, "frozen" joints and a hierarchy of low-variability parameters are not needed as design rules. They appear as side effects of optimizing the task cost with noisy actuators.

### Discussion (pp. 8–9)
- **Claims.** This is a computational-level theory (Marr). Optimal performance is achieved by exploiting redundancy. Goal-directed corrections, synergies, coordination modes, simplifying rules and controlled parameters "may reflect" task-optimal laws, not built-in shortcuts. Redundancy is part of the solution (p. 8).
- **Noise as information.** Internal noise lets the experimenter characterize the output distribution ("system identification"). Variability gives perhaps the strongest support. Preliminary results on reaching (cited abstract) cover smoothness and accuracy, gradual correction of target perturbations, smaller-target speed profiles and reaching asymmetries. Cosine tuning was explained in separate work (pp. 8–9).
- **Limits (p. 9).**
  - Linear dynamics cannot give the lack of mirror symmetry in via-point tasks, and need specified passage times.
  - The theory is independent of LQG, and the authors say the general analysis assures the basic phenomena stay qualitatively the same in nonlinear models.
  - Learning and adaptation are not treated explicitly. The authors report preliminary models and say visuomotor adaptation results "may seem problematic" but they believe they can account for them. Reinforcement learning is suggested for skill acquisition.
- **Psychophysics.** Understanding a new task will need more than measuring a new average trajectory. The optimal controller for each task likely has unique properties (p. 9).

### Methods (p. 9)
- $v^*$ is very hard to compute: the Hamilton–Jacobi–Bellman equation has no analytical solution, and convergent numerical schemes work only in low dimensions. Delayed noisy observation adds complications.
- Simulations use LQG in discrete time with multiplicative noise:
$$x_{t+\Delta t}=Ax_t+Bu_t+\sum_{i=1}^k C_i u_t\varepsilon_{i,t},$$
  with low-pass filtered controls, quadratic task error $x_t^TQ_tx_t$ and a state holding positions, velocities, forces and task constants.
- The optimal law is $u_t=-L_t\hat x_t$, with $\hat x_t$ from a Kalman-filter forward model, fed delayed noisy measurements of position, velocity and force. (Matrix shapes are not given in the main text; see Supplementary Notes.)
- Experiments 1 and 3: LED pointer tracked at 120 Hz. Exp. 1: 40 movements per condition, 1.2–1.5 s window, 1 cm targets. Exp. 3: 15 trials per condition, 1.2–1.4 s, 1.6 cm targets (0.8 cm for the small one). Positional variance: resample to 100 points along the path, find nearest points to the average, sum $x$ and $y$ variances.
- Experiment 5: 40 trials per subject, Cyberglove 100 Hz, aligned and time-scaled to the average, detrended, joints normalized to variance 1.

## Toy example (ours, not from the text)
Use the one-step problem with $a=1$, $\sigma^2=0.25$, $r=0.75$ (so $r+\sigma^2=1$) and $X^*=2$. (added step) The expected cost is $(Err+u_1+u_2)^2+(r+\sigma^2)(u_1^2+u_2^2)$.

Start A: $(x_1,x_2)=(1.5,1.5)$. $Err=1\cdot3-2=1$.
- Optimal law: $u_1=u_2=-0.5$. Sum $=-1$, so $(Err+\sum u)^2=0$. Effort term: $1\times(0.25+0.25)=0.5$. Cost $=0.5$.
- Desired-state law $u_i=1-x_i$: $u=(-0.5,-0.5)$, the same, so cost 0.5.

Start B: $(2.0,1.0)$, the same sum, so a purely task-irrelevant deviation ($\delta=0.5$). $Err=1$.
- Optimal law: $u=(-0.5,-0.5)$ again, with no reaction to $\delta$. Mean final state $(1.5,0.5)$, sum 2. Cost $0.5$.
- Desired-state law: $u=(1-2,1-1)=(-1,0)$. Sum $=-1$, so the error term is 0. Effort term: $1\times(1+0)=1$. Cost $1$, twice the optimal. It also moves the mean state to $(1,1)$, a correction of something irrelevant.

Lesson: the optimal law treats B exactly like A, and the deviation $\delta$ stays in the final state as redundant variability.

## Concepts
- [[minimal-intervention-principle]] — deviations from the average trajectory are corrected only if they interfere with task performance (p. 3)
- [[redundancy]] (new) — states with equal cost-to-go $v^*$ are task-equivalent, so $\Delta v^*=0$ means a redundant deviation (p. 4)
- [[value-function]] — $v^*(t,x)$, the optimal cost-to-go; it determines $\pi^*$ (p. 4)
- [[policy]] — the optimal feedback law $u=\pi^*(t,x)$, a time-varying map from states to controls (p. 4)
- [[hamilton-jacobi-bellman-equation]] — the equation $v^*$ satisfies; no analytical solution in general (p. 9)
- [[signal-dependent-noise]] (new) — multiplicative motor noise; force s.d. grows linearly with the mean (p. 2)
- [[observer-state-estimator]] — forward model combining delayed noisy feedback, plant dynamics and efference copy (p. 2)
- [[kalman-filter]] — gives the internal state estimate $\hat x_t$ in the simulations (p. 9)
- [[open-loop-vs-closed-loop]] — the desired-trajectory view executes a plan open loop. Optimal feedback uses online information (pp. 2, 6)
- [[delay-dead-time]] — sensory delay is roughly equivalent to extra sensory noise because the forward model extrapolates delayed data (p. 5)
- [[desired-trajectory-hypothesis]] (new) — planning replaces the goal by one trajectory that execution tracks (p. 1)
- [[motor-synergy]] (new) — here, a coupled control direction; their number is the rank of $L_t$ (pp. 4, 7)

## Canonical instances
- [[two-variable-one-step-problem]] — the sum $x_1+x_2$ must equal $X^*$; the optimal law cancels only $Err$ (p. 3)
- [[pistol-aiming-and-intercept-sims]] — final-state variance is orthogonal to the task-error line (p. 5)
- [[via-point-target-experiments]] — adding or shrinking targets reshapes variance along the path (pp. 5–6)
- [[hitting-and-throwing]] — the optimal controller beats a tracker on target accuracy and lets variance grow after release (p. 6)
- [[paper-ball-manipulation]] — very large joint variability with always-successful outcomes (p. 6)
- [[telescopic-arm-model]] — emergent synergies, "frozen" joint, two phase modes (p. 7)

## Bridges (candidates)
- [same-math] $v^*$ and $\pi^*=-Z^{-1}B^Tv_x^*$ ↔ control-theory: dynamic programming and the HJB equation — the same optimal-control machinery (pp. 4, 9)
- [same-math] forward model with efference copy ↔ control-theory: Kalman filter/observer (pp. 2, 9)
- [structural-analogy] minimal intervention (correct only task-relevant error) ↔ perceptual control: only controlled variables are held at their reference — both treat the task as defining what gets regulated
- [structural-analogy] redundant dimension as a "noise buffer" ↔ requisite variety: spare dimensions give the regulator room to absorb disturbance — only a loose parallel
- [metaphor] "postponing decisions until the last possible moment" ↔ model predictive control: acting from the current state estimate and re-deciding as information arrives (p. 2)

## Questions this raises
- How well does the theory work for nonlinear plants and for tasks where passage times are not fixed (p. 9)?
- Which cost terms for the true task are right, when "the task" cannot be measured independently of the instructions (p. 2)?
- How would learning, including adaptation experiments, shape the controller toward the optimal law (p. 9)?
- What is the exact link between the ratio $0.9\to0.22$ (cost ratio vs. trajectory tracker) and mechanical complexity, beyond the simulation (p. 8)?

## Reading notes
- Printed page labels 1–10 match the PDF pages; the running footer shows journal pages 1226–1235 (printed = journal − 1225). Citations use labels 1–10.
- Supplementary Notes (simulation details, Sims 1–10 parameters) are not in the source. Matrix shapes of the LQG model are not given in the main text.
- Page 4 (typeset text): the printed expansion $\Delta v^*(\Delta x)\approx\langle\Delta x,v_x^*+v_{xx}^*\Delta x\rangle$ has no ½ before the Hessian term. A strict second-order Taylor expansion would normally give ½ $v_{xx}^*$. This does not change the qualitative conclusions (in the form printed, $\Delta v^*$ is zero when the vector $v_x^*+v_{xx}^*\Delta x$ is zero).
- The text layer on pages 3–4 is garbled in the symbols (Δ, Greek letters). The page images were used.
- Visible typos in the source: "This questions was addressed" (p. 8). In the main text on p. 8 ("variability reached its minimum ( )"), the marker (○) is missing from the text layer but visible in the page image.
- Figure values read from plots (e.g. curve shapes in Figs. 2b, 4b) are not reported as numbers here.
