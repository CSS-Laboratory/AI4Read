---
id: astrom-2021-feedbacksystems/ch15-architecture-p1
work: astrom-2021-feedbacksystems
unit: "15 Architecture and System Design (part 1/2): §15.1–§15.4, up to the start of complementary filtering"
pages: 15-1 to 15-23 (page numbers as printed in the page images; see Reading notes)
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Architecture and System Design (part 1/2)

## L0 — One line
Real control systems are built by arranging simple feedback loops inside a designed architecture, either top-down (layers, optimization, logic specifications, verification) or bottom-up (loop-by-loop structures such as cascade, selector and Smith predictor).

## L1 — The gist (≤ 120 words)
How do the simple feedback loops of earlier chapters fit into whole systems? The chapter first describes the design process (the design V, model-based design, agile development). It then presents two architecture styles. Top-down: layered decomposition (discrete decisions, trajectory optimization, feedback), receding horizon control (repeated finite-horizon optimization), hybrid systems (continuous plus discrete dynamics) with temporal-logic specifications, model checking and synthesis. Bottom-up: building controllers loop by loop with cascade, mid-range, selector, internal model control and Smith predictor structures. This matters because the chapter places simple feedback loops in the context of overall system design, including modularity, verification and safety guards. This part ends just after the start of complementary filtering.

**Prerequisites:** transfer functions and block diagrams; sensitivity functions S, T (Gang of Four/Six); PID control and integral windup; state feedback and LQR; basic logic (implication); time delay.

## L2 — Key ideas (5–10 bullets)
- Designing process and controller together (co-design) can make a system easier to control and can enable new capabilities, e.g. deliberately unstable aircraft (p. 15-1, p. 15-2).
- Faults cost far more to fix late; the design V, used with models as "virtual hardware", gives earlier validation, and requirements should be expressed mathematically and checked automatically (p. 15-2, p. 15-3).
- Many control specifications are properties of the Gang of Six transfer functions (introduced in Section 12.1), which are measured by injecting test signals at designated test points (p. 15-5).
- Top-down architectures split control into layers of abstraction: discrete decision logic, trajectory optimization (often receding horizon/MPC), and feedback. Bowtie (common interface within a layer) and hourglass (common interface between layers) patterns give modularity (p. 15-7 to p. 15-11).
- Hybrid (continuous + discrete) systems are specified with a cost function plus temporal logic. Model checking finds counterexamples, while synthesis builds a controller that satisfies the specification by construction (p. 15-12 to p. 15-17).
- Bottom-up design builds a system loop by loop. It can deal with many inputs, many outputs and constraints, but the consequences of adding loops and interactions between loops are hard to judge; for complicated systems a top-down approach may be better (p. 15-18).
- Cascade, mid-range and selector control each solve a specific multi-sensor/multi-actuator/constraint problem, with protection against integral windup (anti-windup) needing care in the cascade and selector structures (p. 15-18 to p. 15-21).
- IMC and the Smith predictor use a process model in parallel with the process. IMC cancels process poles and zeros, so it cannot be used for processes with unstable poles or zeros; the Smith predictor has two parallel paths with identical dynamics, which is particularly serious if the process has unstable poles (p. 15-21, p. 15-22).

## L3 — Walkthrough

### 15.1 Introduction (p. 15-1, p. 15-2)
- All control systems have sensors, actuators, communications, computers and operator interfaces, but come in very different sizes. The same engineering framework can analyze and design them (p. 15-1).
- The process is often designed before control is considered. **Co-design** (designing process and controller jointly) has significant advantages: the system can be made easy to control, e.g. by avoiding non-minimum-phase dynamics. Delays can be avoided by placing sensing and actuation well (p. 15-1).
- Feedback gives the designer an extra degree of freedom. In an extreme example, a system is made more maneuverable by making it unstable and then stabilizing it with a controller (p. 15-1).
- **Architecture** describes the elements (process, sensors, actuators, computers, communication devices, human-machine interfaces, algorithms, software) and how they are connected and interact. The text says architecture is increasingly seen as important in all engineering fields (p. 15-2).

*Intuition note.* The earlier chapters took the plant as given. Here the point is that choosing the plant, the sensor positions and the wiring between components is part of control design, and the text points to significant advantages of doing so (co-design).

### 15.2 System and Control Design (p. 15-2 to p. 15-6)
**Starting point and examples (p. 15-2).**
- System design starts by understanding the system and environment: static and dynamic properties, sensors and actuators, safe-operation bounds, and the nature of disturbances and users (p. 15-2).
- Sometimes the process is given, and sometimes process and controller are designed jointly. Co-design can optimize performance and is sometimes an enabler (p. 15-2).
- **Wright Flyer:** the Wright brothers (in Draper's account, quoted by the authors) chose negative stability and relied on the pilot to stabilize "pilot and machine". This increased maneuverability and controllability (p. 15-2).
- If an automatic controller stabilizes an unstable airframe, its reliability requirements are very strong. The X-29 (Example 14.2) is a similar case (p. 15-2).
- **Jet-engine stall (reference [EHBM08]):** feedback was attempted to reduce the risk of rotating stall, but actuators with the required bandwidth were not available. Analysis showed the problem could instead be alleviated by small asymmetries in the turbine (p. 15-2).

**Design process (p. 15-2, p. 15-3, p. 15-4).**
- Fig. 15.1 shows a design cycle and the cost of correcting faults at different stages. Late faults cost much more (p. 15-2, p. 15-3).
- The **V-model** (from NASA's Apollo program) is a design pattern for hardware and software. The left leg goes from requirements to system, module and component design. The right leg goes from components to the finished product and its validation (p. 15-2, p. 15-3).
- In the classical V, validation (building the right thing) and verification (building it right) are done late, when hardware is available. This gives a long feedback cycle (p. 15-3, Fig. 15.2a caption, p. 15-4).
- **Model-based systems engineering:** models act as virtual hardware, allowing partial validation at many stages. As hardware is built it replaces models in hardware-in-the-loop simulation. Feedback for validation becomes shorter (p. 15-3, p. 15-4).
- Efficient verification needs requirements expressed mathematically and checked automatically against models of the system and environment (p. 15-3).
  - *Regression analysis* checks that changes in one part do not create errors elsewhere. Efficient regression analysis requires robust system-level models and scripting that runs analyses over many operating conditions (p. 15-3).
  - System-level models also support *root cause analysis*, because errors can be reproduced (p. 15-3).
- Models must satisfy the needs of the analysis algorithms. Newton's method for nonlinear equations and optimization needs continuous first (sometimes second) derivatives. This property is **smoothness**. It can be lost through if-then-else statements, saturating actuators, or careless modeling of fluid flows that reverse (p. 15-3).
- **Agile development** is driven by software developers for products with short time to market and changing requirements. The Agile Manifesto values individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. Hardware is harder to change than software (p. 15-3, p. 15-4).

*Intuition note.* A fault found on the finished machine costs far more than one found in a model. Model-based design shortens the loop between a decision and its check, so errors are caught while they are cheap.

**Control design as a subpart (p. 15-4, p. 15-5).**
- Control design runs from requirements and modeling to implementation, testing, commissioning, operation and upgrading. The V-model used iteratively suits it, supported by a tool chain combining modeling, design and simulation. Testing is done iteratively at every step using models of different granularity as virtual systems (p. 15-4).
- Specifications are typically given by large-signal behavior (limits on actuation power and rate) and small-signal behavior (measurement noise, friction, A/D and D/A resolution). Requirements: handle disturbances, be robust to process variations and uncertainty, and follow references (p. 15-4).
- Many specifications can be captured by linear models and expressed through the **Gang of Four and Six** (Section 12.1). In Fig. 15.3 (p. 15-5):
  - Load disturbance attenuation: transfer function $G_{yv}$ from load disturbance $v$ to output $y$.
  - Noise-induced control action: $G_{uw}$ from measurement noise $w$ to control $u$.
  - Robustness to parameter variation and uncertainty: sensitivity functions $S$ and $T$.
  - With two degrees of freedom, reference response is shaped independently of disturbance response and robustness, and is characterized by $TF$ and $CSF$.
  - With error feedback only, reference response is characterized by $T$, so a compromise with the other requirements is needed (p. 15-5).
- To measure these transfer functions on models and hardware, the system needs test points (dashed arrows in Fig. 15.3). Example: $G_{yv}$ is found by injecting a signal at $\delta_1$ and measuring $s_{21}$. Chirp signals are convenient for frequency responses (p. 15-5).
- Models come from physics, experiments (step tests or signals designed for optimal information with limited perturbation), or both. System identification supplies tools. Early models are cruder, later ones more accurate (p. 15-5).
- A few standard design methods are in Chapters 7, 8, 11 and 12; many design methods are based on linear models. When conditions change significantly, gain scheduling, nonlinear control or adaptation is necessary. Receding horizon control (model predictive control) is common, especially with constraints on inputs or states (p. 15-5).

**Implementation (p. 15-5, p. 15-6).**
- Fig. 15.4: sensors, actuators, A/D and D/A converters, computer, clock, operator interface. The filter before the A/D converter is necessary so that high-frequency disturbances do not appear as low-frequency ones after sampling (aliasing) (p. 15-5, p. 15-6).
- Choices: real-time operating system, sampling period, anti-alias filter. Control laws must become difference equations, either by approximating differential equations (Section 8.5) or by direct design methods. Code can be generated automatically. Computational delays and synchronization must not create problems (p. 15-6).
- Commissioning may involve adjusting parameters; automatic tuning (Section 11.3) can help. In operation, the system should be monitored, and it may be upgraded or its specifications modified. A suite of test programs should be used through design and operation (p. 15-6).

### 15.3 Top-Down Architectures (p. 15-6 to p. 15-17)
When design is approached systematically with the design V, a top-down procedure is natural: start from desired system properties and decompose the control problem into interlinked problems at layers of abstraction. At each layer, assumptions are made about the layers above and below to simplify design (p. 15-6). The authors name other topics (cooperative control, diagnostics, fault recovery, game-theoretic control) and focus on multi-layer approaches (p. 15-7).

**Layered architectures (p. 15-7 to p. 15-9).**
- Fig. 15.5 shows a decomposition common in motion control (robotics, self-driving cars, flight control) (p. 15-7).
  - *Top layer:* discrete modes of behavior (takeoff/cruise/landing; highway/city/parking lot).
  - *Middle layer:* trajectories, often by optimization, with constraints on state and inputs and system-level performance.
  - *Lowest layer:* feedback control, where a linearized model at the current operating point along a trajectory may be used (p. 15-7, p. 15-8).
- Sensing is layered too. The lowest layers use individual, perhaps filtered, signals. Higher layers fuse multiple measurements. The top layer often needs sophisticated reasoning about the environment and other entities (p. 15-8).
- Fig. 15.5 suits moderate complexity, where users change modes and references. More layers are used with complicated user interaction. In *batch control* there are two extra layers on top: *procedural control* (executes the sequence of actions for a process task, e.g. charging a reactor) and *coordination control* (directs, initiates or modifies procedural control and equipment use) (p. 15-8).
- Production facilities typically have modes normal, maintenance and manual. Maintenance mode has its own algorithms and safety procedures. Different parts can be in different modes. Fig. 15.6 shows a distributed control system (DCS) architecture (p. 15-8, p. 15-9).

**Modularity patterns (Fig. 15.7, p. 15-8 to p. 15-10).**
- Modularity allows parallel development and upgrading components without redesigning everything (p. 15-8).
- **Bowtie:** a common interface within one layer lets many subsystems connect across it. Example: a common map representation lets many sensor types feed an autonomous vehicle's map and different controller layers read fused information from it. New sensors or functions can be added on either side without redesigning the rest (p. 15-8, p. 15-10).
- **Hourglass:** a common interface (protocol) between levels lets what is above and below it change independently. Example: the seven-layer OSI model for communication. Another: trajectories in a vehicle's planning. Any high-level function that eventually yields a trajectory is compatible with lower controllers that track it, and lower controllers can change as long as they track a given trajectory (p. 15-8, p. 15-9).
- Patterns can appear several times, giving "stacks" of sensing and control (p. 15-9).

**Example 15.1 Autonomous driving (p. 15-9, p. 15-10).** Fig. 15.8 shows Caltech's vehicle "Alice" for urban driving. Sensors (cameras, laser range finders, radar) are fused into a multi-layer map. The map is used to decide actions (drive, stop, change lanes) and plan a path. An optimization-based planner computes a trajectory for a tracking module. A supervisory module handles mission planning and contingency management (e.g. sensor or actuator failure) (p. 15-9). The mission and traffic planners are two levels of discrete logic, the path planner is trajectory optimization, and lower layers are control. Low-level sensing (speed, lane position) goes to the tracker, and higher-level information (other vehicles and their predicted motion) goes to the planners (p. 15-9, p. 15-10).

*Intuition note.* Layers let each design problem be simple, because each layer sees the others only through a narrow interface (a mode, a trajectory, a map). That narrow interface is also what lets you swap components.

**Online optimization / receding horizon control (p. 15-10, p. 15-11).**
- Fast trajectory computation allows *receding horizon control*: compute an (optimal) feasible trajectory from the current state over a finite horizon $T$, apply it for a shorter time $\delta < T$, then recompute from the new state over $[t+\delta,\, t+T+\delta]$ (Fig. 15.9). It is also called model predictive control (MPC). It originated in process control, where the processes are often slow enough to allow implementation (p. 15-10, p. 15-11).
- At each step the trajectory generation block solves
$$
\min_{(x,u)} \int_t^{t+T} L(x,u)\,d\tau + V(x(t+T)) \quad\text{subject to}\quad
\begin{cases} x(t)=\text{current state}\\ \dot x = f(x)+g(x)u,\\ lb \le c(x,u)\le ub.\end{cases}
\tag{15.1}
$$
- Instabilities can result if the problem is badly specified. Because optimization is over a finite horizon, optimal short-term behavior can lead *away* from the long-term solution. The terminal cost $V$ must have certain properties to ensure stability (see [MRRS00]) (p. 15-11).
- A main challenge is fast computation of feasible trajectories. Differentially flat systems (Section 8.5) make this easier (p. 15-11).
- Fig. 15.10 shows the two-degree-of-freedom structure. A trajectory generator computes a feedforward command $u_d$ and desired state $x_d$. A state feedback controller uses the measured or estimated state and $x_d$ to compute a correction $u_{fb}$. Uncertainty $\Delta$ stands for unmodeled dynamics, disturbances and noise (p. 15-12).

*Intuition note.* Plan a good path for a limited look-ahead, use only its first part, then replan with fresh measurements. Because the horizon is finite, the best short-term plan can lead away from the long-term solution, and instabilities can result if the problem is not specified correctly; the terminal cost $V$ must have certain properties to ensure stability.

**Discrete decision making and supervisory control (p. 15-11 to p. 15-14).**
- A major challenge in networked control systems (aerospace, computing, robotics, infrastructure) is ensuring that dynamics plus logical decision making meet safety and performance specifications. In many of these areas verification and validation are now dominant drivers of schedule and cost, and tools lag behind needs (p. 15-11, p. 15-12).
- *Hybrid model.* Subsystem $i$ has
$$\dot x^i = f^i(x^i,\alpha^i,u^i),\qquad y^i = h(x^i,\alpha^i),$$
with $x^i\in\mathbb R^{n_i}$ continuous state, $\alpha\in\mathcal A$ discrete state, $u^i\in\mathbb R^{m_i}$ input, $y^i\in\mathbb R^{p_i}$ measured output (p. 15-12).
- The discrete state changes by "guarded commands": $\alpha$ is updated only if a guard is true,
$$ g^p_j(x,\alpha) \implies \alpha' = r^p_j(x,\alpha).$$
This allows asynchronous evolution (e.g. failures) or dependence on the continuous state (nonlinearities, changes in connectivity). Such a model is a *discrete transition system*. Continuous plus discrete dynamics together form a *hybrid system* (p. 15-12).
- A controller is a continuous law plus a discrete protocol:
$$ u = k(x,\alpha),\qquad g^c_j(x,\alpha)\implies \alpha' = r^c_j(x,\alpha). \tag{15.2}$$
The protocol (a supervisory controller) is itself a discrete transition system that controls some subset of the discrete states. It is assumed to be updated by a periodically running process that checks the guards. This allows distributed computation on loosely regulated clocks (p. 15-12, p. 15-13).
- *Continuous specification:* a finite-horizon cost, with $V$ an appropriate positive function:
$$ J = \int_0^T L(x,\alpha,u)\,dt + V(x(T)). \tag{15.3}$$
- *Discrete specification:* temporal logic, which describes conditions on sequences of events. **Linear temporal logic (LTL)** has two operators: always ($\square$) and eventually ($\Diamond$). For a state formula $\varphi(\alpha)$, $\square\varphi$ means $\varphi$ is true at all future times, and $\Diamond\varphi$ means $\varphi$ is true at some future state (p. 15-13).
- Example: $\square(\varphi \implies \Diamond\psi)$ says that at all times, if $\varphi$ holds then eventually $\psi$ holds. It specifies responding to an event ($\varphi$) by an action ($\psi$). The outer $\square$ makes the system respond again every time the event recurs (p. 15-13).
- A typical supervisory specification:
$$ \varphi_{\rm init}\wedge\square\varphi_{\rm env} \implies \square\varphi_{\rm safe}\wedge\Diamond\varphi_{\rm goal}, \tag{15.4}$$
where $\varphi_{\rm init}$ is the initial state, $\varphi_{\rm env}$ the possible environment actions, $\varphi_{\rm safe}$ a safety requirement and $\varphi_{\rm goal}$ a progress requirement. These specifications are typically written in LTL or other temporal logics (including CTL and variants), which allow, e.g., "a condition holds until another is satisfied" (p. 15-13).
- The design problem: find a law of the form (15.2) satisfying (15.4) while minimizing (15.3). The traditional approach is optimization-based design of the continuous law and manual design of the discrete protocol, then checking by many repeated simulations (p. 15-13, p. 15-14).

*Intuition note.* Equation (15.4) reads: if the system starts right and the environment behaves as assumed, then it must always stay safe and must eventually reach its goal. "Safe" is a never-violate rule, and "goal" is a will-happen-eventually rule.

**Linking continuous and discrete controllers (p. 15-14, p. 15-15).**
- *Common framework:* mixed logical dynamical (MLD) systems (Bemporad and Morari) extend trajectory generation and receding horizon control to discrete variables. This needs mixed integer solvers (continuous plus integer variables) (p. 15-14).
- *Separate design:* solve supervisory and trajectory problems separately, each with a simplified representation of the layers above and below. For example, trajectory generation assumes the mode switches and then stays fixed long enough. The supervisor must then enforce this restriction on the time between mode switches (p. 15-14).
- This kind of link is a **vertical contract**, often written in *assume-guarantee* form (p. 15-14):
  - The supervisory layer *assumes* the trajectory layer meets the specification in a given mode given enough "settling" time, and *guarantees* not to switch modes faster than the settling time.
  - The trajectory layer *assumes* switching is sufficiently slow, and *guarantees* it meets the specification within the settling time.
- The supervisor needs a discrete transition model of the lower layers. One approach splits the continuous state space into regions, with transitions between adjacent regions (Fig. 15.11a). Trajectories in the discrete model must correspond to feasible continuous trajectories, and vice versa, so that commanded region changes can be executed and real motion corresponds to valid transitions (p. 15-14, p. 15-15).

**Model checking and program synthesis (p. 15-15 to p. 15-17).**
- Verification by simulation can be prohibitively time-consuming, since it is impractical to simulate every possible sequence of events. For purely discrete systems, **model checking** uses the structure of the logic formula and dynamics (p. 15-15).
- Method (Fig. 15.12): combine the system model and the (negated) temporal-logic specification into a *product transition system*. A path through it is a possible execution that *violates* the specification. If no such path exists, the specification is satisfied. If one is found, it is a counterexample for updating the design (p. 15-15, p. 15-16).
- Tools (nuSMV, PRISM, SPIN, TLC) handle relatively large systems and are widely used in industry and increasingly applied in mission- and safety-critical applications. A limitation is that model checking does not necessarily give insight into how to redesign; it provides a counterexample. The designer must find the cause, redesign and re-verify iteratively (p. 15-16).
- **Program synthesis / correct-by-construction synthesis** takes a discrete model and a temporal-logic specification and synthesizes a control protocol such that the closed loop satisfies the specification. The authors compare it conceptually to LQR (Section 7.5): from a cost and model ($A,B,C$), create $u=-Kx$ that by construction stabilizes the system and optimizes performance (p. 15-16).
- Model checking and synthesis use the same information (model and specification) but solve different problems (Fig. 15.13: verification returns "satisfied" or "violated + counterexample"; synthesis returns a controller or "no such controller exists") (p. 15-16, p. 15-17).
- Synthesis gives a protocol guaranteed to satisfy the specification whatever sequence of environmental events occurs. It is "not a panacea": it applies only to certain specifications and can be overwhelmed by complexity (p. 15-16, p. 15-17).
- *Practical layered safety scheme:* algorithms plus guards in layers. The innermost layer (for flight control, "flying home mode") is a simple robust controller, which can be designed to be correct-by-construction if the loop is simple enough. Higher layers give better performance and have guards that move the system to a lower, safer layer if performance fails. The guards' safety must also be guaranteed (Sha; guards for adaptive control in [THÅ00]) (p. 15-17).

*Intuition note.* Model checking asks "can anything go wrong?" and returns an example if yes. Synthesis asks "build me something that cannot go wrong" and returns a controller if one exists. The layered safety scheme keeps a simple robust controller as the innermost layer, which can be designed to be correct-by-construction if the loop is simple enough.

### 15.4 Bottom-Up Architectures (p. 15-17 to p. 15-23)
- Bottom-up design builds controllers by interconnecting low-level control systems, like standardized nuts and bolts or electronic components (p. 15-17).
- Building blocks: controllers (often PID), nonlinear functions, filters, logic, finite state machines, as hardware or software function blocks. Systems are built loop by loop using feedback, feedforward and gain scheduling, plus the structures introduced here: cascade, mid-range, selector, internal model control, Smith predictor, extremum seeking and complementary filtering (p. 15-18). (Extremum seeking is announced but not covered in these pages.)
- *Advantages:* handles many inputs, many outputs and constraints; can be designed, commissioned and tuned loop by loop. *Disadvantages:* consequences of adding loops are hard to judge, and interacting loops can cause difficulties. Easy for simple systems. For complicated systems a top-down approach may be better (p. 15-18).

**Cascade control – several sensors (p. 15-18, p. 15-19).**
- One actuator, two or more sensors (Fig. 15.14). Process: $u \to P_1 \to y_s \to P_2 \to y$. The primary controller $C_p$ keeps $y$ near $r$ by manipulating the reference $r_s$ of the secondary controller $C_s$. $C_s$ keeps $y_s$ near $r_s$ by manipulating $u$ (inner/secondary loop and outer/primary loop) (p. 15-18).
- Design loop by loop, inner loop first. With integral action, anti-windup is needed. For $C_s$ it is conventional, since it drives the actuator directly. For $C_p$, it must be told when $C_s$ is in anti-windup mode (p. 15-19).
- Cascade can use more than two sensors; the ultimate case is state feedback with all states measured. It is particularly useful when there is significant delay or dynamics between $u$ and $y$ but much less between $u$ and $y_s$. A tight inner loop reduces the effects of disturbances and uncertainty in $P_1$ and simplifies the outer-loop design (p. 15-19).

**Mid-range control – many actuators (p. 15-19).**
- Several control signals influence one output (Fig. 15.15). Example: a CD player with a fast actuator of small range and a slower actuator of wide range. $u_f$ (fine) and $u_c$ (coarse) act through $P_f$ and $P_c$ (p. 15-19).
- $C_f$ is the primary controller, keeping $y$ near $r$. $C_c$ measures $u_f$, with reference at the middle of $u_f$'s range, and drives $u_c$. So $u_f$ stays mid-range and can handle moderately large disturbances. Both controllers act for large disturbances. Tuning is loop by loop starting with $C_f$ (p. 15-19).

**Selector control – equipment protection (p. 15-20, p. 15-21).**
- A selector has many inputs and one output (maximum or minimum). The primary controller $C$ (output $u_n$) keeps $y$ near $r$. An auxiliary variable $z$ should stay in $z_{\min}<z<z_{\max}$, enforced by $C_{\max}$ and $C_{\min}$ (outputs $u_h$, $u_l$) with references $z_{\max}$, $z_{\min}$ (Fig. 15.16) (p. 15-20).
- Normally $z$ is inside the range and $u=u_n$. If $z$ exceeds $z_{\max}$, the error of $C_{\max}$ becomes negative and the minimum selector chooses $u_h$ instead of $u_n$. $C_{\max}$ then drives $z$ toward $z_{\max}$. A similar situation occurs below $z_{\min}$. Switching depends on the limits and on the gains of the secondary controllers, which are often proportional (p. 15-20).
- Uses: keep temperature while limiting pressure; avoid compressor stall. There are also median and two-out-of-three selectors for high-integrity systems. Selector control is related to manual control (Section 11.4) (p. 15-20, p. 15-21).
- Only one controller operates at a time, so design is loop by loop. But switching can be complicated. With integral action, the integral states of inactive controllers must be tracked, so windup protection requires care. With many constraints it is safer to use multivariable architectures such as MPC (p. 15-21).

**Internal model control (IMC) – disturbance observer (p. 15-21, p. 15-22).**
- Fig. 15.17: the controller contains a model $\hat P$ in parallel with the process, $G_f$, and an inverse $\hat P^{-1}$. The idea is to estimate the effect of disturbances $v$ and $w$ on the output (p. 15-21).
- If $\hat P=P$, the control signal $u$ has no effect on $\epsilon$, so $\epsilon = w + Pv$. This is the net disturbance effect at the process output, hence "disturbance observer". If $G_f=1$, $\hat P^{-1}$ generates a control that eliminates the disturbance. In reality the inverse is normally not realizable, but an approximate inverse and a proper $G_f$ give good attenuation (p. 15-21).
- Reference response, neglecting disturbances and with $\hat P=P$: $\epsilon=0$ and $G_{yr}=P\hat P^{-1}G_f=G_f$. In reality an approximate inverse $P^\dagger$ is used, and reference response is shaped by $P^\dagger G_f$ (p. 15-21).
- Equivalent standard loop with process $P$ and controller
$$C=\frac{P^{-1}G_f}{1-G_f}. \tag{15.5}$$
- If $\hat P=P$, $C$ cancels all process poles and zeros, so it cannot be used for processes with unstable poles or zeros. The same is seen from the two parallel paths with identical systems, a prototype of a system lacking observability and reachability (p. 15-21, p. 15-22).

**The Smith predictor – phase advance (p. 15-22, p. 15-23).**
- A controller architecture for time delays (Fig. 15.18). It holds a model $\hat P=\hat P_0e^{-s\tau}$ in parallel with the process $P=P_0e^{-s\tau}$. The model supplies $y_p$, a proxy for the undelayed output. It is similar to IMC (p. 15-22).
- If $\hat P_0=P_0$, then $\epsilon$ is zero for all $u$, and block-diagram algebra gives
$$G_{yr}(s)=\frac{P_0(s)C_0(s)}{1+P_0(s)C_0(s)}\,e^{-s\tau}. \tag{15.6}$$
So $C_0$ can be designed for the delay-free process $P_0$ (p. 15-22).
- The two parallel identical paths are especially serious if $P_0$ has unstable poles. Without modification it cannot be used for processes with integrators ([ÅHL94]) (p. 15-22).
- If $\hat P=P=P_0e^{-s\tau}$, it equals a conventional loop with controller
$$C=\frac{C_0}{1+C_0P_0(1-e^{-s\tau})}=C_0C_{\rm pred},\qquad C_{\rm pred}=\frac{1}{1+C_0P_0(1-e^{-s\tau})}. \tag{15.7}$$
  So it is $C_0$ in cascade with a predictor $C_{\rm pred}$ (p. 15-22).
- Near the gain crossover frequency of $P_0C_0$ the text states $P_0C_0\approx-1$ and $C_{\rm pred}\approx e^{sL}$ (the text uses $L$ here and $\tau$ elsewhere), i.e. significant phase advance (p. 15-22). *(Added step: with $P_0C_0=-1$ exactly, $C_{\rm pred}=1/(1-(1-e^{-s\tau}))=e^{s\tau}$.)*
- **Example (15.8):** $P_0=\dfrac1{s+1}$, $C_0=\left(1+\dfrac{1}{0.45s}\right)$, $L=8$. Fig. 15.19 compares the Bode plots of $C_{\rm pred}$ and the ideal predictor $e^{s\tau}$. The text says the phase lead is very close to ideal at $\omega=0.76$ and $\omega=1.3$, where it is $360^\circ$ and $720^\circ$. The gain has resonances at these frequencies, and phase rises about $180^\circ$ there, implying two complex pole pairs in the right half-plane (p. 15-23).
- The Smith predictor gives good reference response. Load-disturbance response is not much better than PI control, because the gain crossover (around 0.1 here) is limited by the delay and can also be reached with PI. But $C_{\rm pred}$ is a useful transfer function for large phase advance (p. 15-23).

*Intuition note.* The Smith predictor lets you tune the controller as if the delay were absent, using a model to "see" the undelayed output. The text warns that the two parallel paths with identical dynamics are particularly serious if $P_0$ has unstable poles, and that without modification it cannot be used for processes with integrators.

**Complementary filtering – sensor fusion (begins, p. 15-23).** The text introduces combining a slow-but-accurate sensor with a fast-but-drifting one (e.g. GPS with gyroscopes and accelerometers). With $y_1=x+w_1$, $y_2=x+w_2$, $w_1$ zero-mean and $w_2$ possibly drifting. The text breaks off here; the continuation is in the next part (p. 15-23).

## Toy example (ours, not from the text): selector control, static check
Setup: process gain from $u$ to $z$ is 0.8, so $z=0.8u$. Limits $z_{\min}=1$, $z_{\max}=4$. Primary output $u_n$ is given.
Secondary controllers (our choice, proportional with a bias):
- $u_h=4.5+2(4-z)$
- $u_l=1.5+2(1-z)$

Selector rule as in Fig. 15.16: $u=\min\bigl(u_h,\ \max(u_n,u_l)\bigr)$. We look for equilibria, i.e. values of $u$ consistent with $z=0.8u$ (a static check only, no dynamics).

1. **$u_n=3$.** Try $u=3$: $z=2.4$. $u_h=4.5+2(1.6)=7.7$. $u_l=1.5+2(-1.4)=-1.3$. $\max(3,-1.3)=3$; $\min(7.7,3)=3$. Consistent: the guards are inactive and $u=u_n$.
2. **$u_n=8$** (would give $z=6.4>4$). Suppose $u=u_h$: $u=4.5+2(4-0.8u)=12.5-1.6u$, so $2.6u=12.5$, $u=4.808$, $z=3.846$. Check: $u_l=1.5+2(1-3.846)=-4.19$, $\max(8,-4.19)=8$, $\min(4.808,8)=4.808$. Consistent: $C_{\max}$ takes over and holds $z$ just below $z_{\max}$.
3. **$u_n=0.5$** (would give $z=0.4<1$). Suppose $u=u_l$: $u=1.5+2(1-0.8u)=3.5-1.6u$, so $u=3.5/2.6=1.346$, $z=1.077$. Check: $u_h=4.5+2(2.923)=10.35$, $u_l=1.5+2(-0.0769)=1.346$. $\max(0.5,1.346)=1.346$; $\min(10.35,1.346)=1.346$. Consistent: $C_{\min}$ takes over.

Lesson: the primary loop runs unchanged while $z$ is within limits, and a protecting loop silently takes over at the limits. The proportional guards allow $z$ to settle slightly inside the limits (3.846 and 1.077).

## Concepts
- [[co-design]] (new) — designing process and controller jointly, e.g. to avoid non-minimum-phase dynamics or delays (p. 15-1)
- [[architecture-control-system]] (new) — how components (process, sensors, actuators, computers, interfaces, algorithms, software) are connected and interact (p. 15-2)
- [[design-v-model]] (new) — design pattern with requirements→components on the left leg and implementation→validation on the right (p. 15-2, p. 15-3)
- [[model-based-design-hil]] (new) — using models as virtual hardware, with hardware-in-the-loop as parts are built (p. 15-3)
- [[smoothness-of-models]] (new) — continuous first (and sometimes second) derivatives, needed by Newton-type algorithms (p. 15-3)
- [[layered-architecture]] (new) — hierarchy of control problems at different abstraction layers (modes, trajectories, feedback) (p. 15-7)
- [[bowtie-hourglass-patterns]] (new) — common interfaces within a layer (bowtie) or between layers (hourglass) giving modularity (p. 15-8, p. 15-10)
- [[model predictive control]] — receding horizon control: solve a finite-horizon problem, apply a short part, resolve; terminal cost matters for stability (p. 15-10, p. 15-11)
- [[feedforward]] — here, the trajectory generator's command $u_d$ in a two-degree-of-freedom design (p. 15-12)
- [[hybrid-system]] (new) — continuous dynamics plus a discrete state updated by guarded commands (p. 15-12)
- [[temporal-logic-ltl]] (new) — logic with "always" ($\square$) and "eventually" ($\Diamond$) for specifying event sequences (p. 15-13)
- [[vertical-contract]] (new) — assume-guarantee agreement between adjacent layers (p. 15-14)
- [[model-checking]] (new) — verifying a discrete system against a specification via the product transition system; yields a counterexample if the specification is violated (p. 15-15, p. 15-16)
- [[program-synthesis]] (new) — constructing a controller guaranteed to satisfy a specification (correct-by-construction) (p. 15-16)
- [[cascade-control]] (new) — one actuator, several sensors; the primary controller sets the reference of the inner loop (p. 15-18)
- [[mid-range-control]] (new) — a fine actuator is kept mid-range by a coarse actuator (p. 15-19)
- [[selector-control]] (new) — min/max selectors switch between controllers to respect constraints (p. 15-20)
- [[internal-model-control]] (new) — model in parallel with the process, estimating the disturbance effect; cancels process poles/zeros (p. 15-21)
- [[smith-predictor]] (new) — time-delay controller allowing design for the delay-free process (p. 15-22)
- [[integral action]] — anti-windup is needed in cascade and selector structures (p. 15-19, p. 15-21)
- [[delay (dead time)]] — handled by the Smith predictor; cascade control is particularly useful when significant delay lies between $u$ and the primary output but much less between $u$ and the secondary output (p. 15-19, p. 15-22)

## Canonical instances
- [[wright-flyer]] — deliberately unstable aircraft stabilized by the pilot; co-design as enabler (p. 15-2)
- [[x-29]] — unstable airframe needing a reliable automatic controller (p. 15-2)
- [[jet-engine-rotating-stall]] — feedback not feasible for lack of actuator bandwidth; alleviated instead by small turbine asymmetries (p. 15-2)
- [[autonomous-driving-alice]] — Example 15.1: layered architecture of Caltech's DARPA Grand Challenge vehicle (p. 15-9, p. 15-10)
- [[batch-control]] — extra procedural and coordination layers on top of Fig. 15.5 (p. 15-8)
- [[osi-model]] — seven-layer hourglass for communication interoperability (p. 15-8)
- [[cd-player-midranging]] — fast small-range plus slow wide-range actuator (p. 15-19)
- [[smith-predictor-example-15-8]] — $P_0=1/(s+1)$, PI controller, $L=8$, Bode plot of $C_{\rm pred}$ (p. 15-23)

## Bridges (candidates)
- [structural-analogy] Program synthesis ↔ LQR design: given a model and specification, produce a controller that by construction meets the specification — the authors draw this comparison (p. 15-16).
- [structural-analogy] Cascade control with all states measured ↔ state feedback: the text calls state feedback the "ultimate case" of cascade (p. 15-19).
- [structural-analogy] IMC/Smith predictor internal model ↔ observer (state estimator): a model runs in parallel with the process, and its mismatch with the output is used for correction.
- [structural-analogy] Hourglass pattern ↔ network protocol layering: a narrow common protocol lets layers above and below change independently (OSI model, p. 15-8).

## Questions this raises
- How can the effect of adding a new loop on an existing bottom-up design be judged without redesigning everything? The text says this is difficult (p. 15-18).
- What properties must the terminal cost $V$ have to guarantee MPC stability (the text refers to [MRRS00])?
- When the discretization of continuous dynamics gives only an approximation, how can a vertical contract guarantee that the supervisor's commands remain feasible (p. 15-15)?
- Why does IMC, which cancels process dynamics, still give good disturbance attenuation in practice with only an approximate inverse (p. 15-21)?

## Reading notes
- **Part boundaries:** this part starts at the chapter opening (Chapter 15, §15.1) and ends at the bottom of page 15-23, mid-section in "Complementary Filtering – Sensor Fusion" (it stops at "Using expo-"). The remainder of §15.4 and later sections (interaction, adaptation, industrial fields, as announced on p. 15-1) are not in these pages.
- **Page numbers:** the labels give no printed number, but the page images show running numbers "15-1" … "15-23". Printed = pdf − 498 (pdf 499 = 15-1). All references use these printed numbers as (p. 15-N).
- **Possible misprints (as seen in the images):**
  - p. 15-22 says "$C_{\rm pred}\approx e^{sL}$", while the predictor elsewhere is $e^{s\tau}$ ($L$ is only defined as 8 in eq. (15.8)).
  - In eq. (15.5) the image shows $P^{-1}$, while the block diagram uses $\hat P^{-1}$; the two coincide when $\hat P=P$.
  - Our arithmetic check (assuming $\tau=L=8$; the text only defines $L=8$): with delay 8, a $720^\circ$ ($4\pi$ rad) phase lead corresponds to $\omega=4\pi/8\approx1.57$, whereas the text says $1.3$; $360^\circ$ corresponds to $\omega\approx0.785$ (text: 0.76). The second resonance in Fig. 15.19 looks nearer 1.5 than 1.3.
  - Smaller typos: "Figure 15.19 … $e^{s\tau}$" uses τ, and the intro paragraph on p. 15-14 refers to "Section 15.3" for continuous controllers.
- Figures 15.1, 15.2, 15.6, 15.8 and 15.11 are small or low-resolution images; only their captions and visible labels were used.
- No exercises appear in these pages.
