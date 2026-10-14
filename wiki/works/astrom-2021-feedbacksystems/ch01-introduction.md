---
id: astrom-2021-feedbacksystems/ch01-introduction
work: astrom-2021-feedbacksystems
unit: "1 Introduction"
pages: 1-1 to 1-30
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Chapter 1 — Introduction (feedback, feedforward, control, and simple feedback laws)

## L0 — One line
Feedback means basing corrective action on the difference between desired and actual performance; this simple idea gives robustness, reshapes dynamics and enables modular design, but it can also cause instability and inject noise.

## L1 — The gist (≤ 120 words)
The chapter asks what feedback and control are and why they matter. Feedback is a circular coupling of two dynamical systems, so intuition about it often fails and formal methods are needed. Feedforward acts on measured disturbances or plans instead of on errors. Control is the use of algorithms and feedback in engineered systems. The authors survey applications in power, communications, aerospace, biology, networks and economics. They list what feedback offers (robustness, redesigned dynamics, modularity) and what it costs (instability, noise, complexity). They preview on-off, proportional, integral and PID control, then logic and layered architectures. It matters because the rest of the book formalizes these ideas.

**Prerequisites:** basic idea of a differential equation or rate of change; integrals as accumulated area; block diagrams (boxes with signals as arrows).

## L2 — Key ideas
- Feedback couples two systems in a loop, so simple causal reasoning becomes circular. Behavior is often counter-intuitive and needs formal analysis (p. 1-1).
- Negative feedback tries to react to disturbances so that their effects decrease; positive feedback makes an increase grow further, has a destabilizing effect, and is usually accompanied by saturation (a limit on how far the quantity can grow) (p. 1-2).
- Feedback is reactive and needs an error. Feedforward acts on a measured disturbance or plan, needs a good model, and has no stability risk (pp. 1-4, 1-5).
- The central concept in control is the feedback loop of sensing, computation and actuation. Key design issues are stability plus additional desired behavior, such as good disturbance attenuation (reducing the effect of disturbances) (p. 1-5).
- Feedback gives robustness to disturbances and to uncertain process dynamics. It can redesign dynamics (stabilize, speed up) and create modularity through nested loops (pp. 1-14 to 1-17).
- The costs of feedback are possible instability, injected measurement noise, and system complexity (pp. 1-17, 1-18).
- Simple laws are on-off, proportional, integral and PID. Integral action removes steady-state error under a constant disturbance, at the cost of risks such as windup (a possible problem when the control action has magnitude limits) (pp. 1-18 to 1-20).
- Real systems combine feedback with logic (state machines, which switch the controller between modes; selectors, which pick the largest or smallest of several inputs) and layers of optimization, decision-making and low-level loops (pp. 1-20 to 1-27).

## L3 — Walkthrough
Page references use the printed numbers "1-N" visible in the page images.

### 1.1 What Is Feedback? (pp. 1-1 to 1-3)
- **Definitions.** A *dynamical system* is a system whose behavior changes over time, often in response to external stimulation or forcing. *Feedback* is the situation in which two or more dynamical systems are connected so that each influences the other, so their dynamics are strongly coupled (p. 1-1).
- Simple causal reasoning is hard because system 1 influences system 2 and system 2 influences system 1, which gives a circular argument. The authors conclude that feedback behavior is often counter-intuitive and formal methods are necessary (p. 1-1).
- **Closed vs open loop (Fig. 1.1).** The systems are connected in a cycle: the output $y$ of system 2 is the input of system 1, and the output $u$ of system 1 is the input of system 2. This is *closed loop*. If the interconnection is broken, so system 1 receives an external input $r$ instead, it is *open loop*. The choice of "system 1" and "system 2" is somewhat arbitrary, because it only depends on where you start describing the loop (pp. 1-1, 1-2).
- **Biological example: blood glucose.** The body tries to keep glucose concentration constant, at about 90 mg per 100 mL of blood. When glucose rises, the pancreas releases insulin, which makes the body store excess glucose in the liver. When glucose is low, the pancreas secretes glucagon, which has the opposite effect. Liver = system 1 (output: glucose concentration). Pancreas = system 2 (output: amount of insulin or glucagon) (p. 1-2).
- **Engineering example: centrifugal governor (Fig. 1.2).** A flyball mechanism on the steam-engine shaft is linked to the throttle. If engine speed rises, the flyballs spread apart and a linkage closes the throttle. The engine slows and the flyballs come back together. Steam engine = system 1, governor = system 2. When properly designed it keeps speed constant, roughly independent of load. It was an enabler of the Watt steam engine (p. 1-2).
- **Negative vs positive feedback.** The examples so far are *negative feedback*, in which we attempt to react to disturbances in such a way that their effects decrease. *Positive feedback* is the opposite: an increase in a quantity leads, through feedback, to a further increase. It is destabilizing and usually accompanied by a saturation that limits growth. It is often considered undesirable but is used to get very fast responses and in systems with oscillatory dynamics. The authors give encouragement as an example (p. 1-2).
- **Benefits (p. 1-3).** Feedback can make a system resilient to external influences. It can create linear behavior from nonlinear components (common in electronics). It can make a system insensitive both to disturbances and to variations in its own elements.
- **Drawbacks (p. 1-3).** Feedback can create instabilities (oscillations, runaway behavior). It can introduce unwanted sensor noise, requiring careful filtering. Hence much of the study of feedback is about dynamics.
- **Ubiquity.** Examples named: building environment and power, cars, electronics, manufacturing, communications, military and space systems, AFMs and telescopes. In nature: homeostasis, global climate, ecosystems, economies through markets (p. 1-3).

*Intuition note.* Feedback is a circle, not a line: A affects B and B affects A. Because of this, it is hard to work out what happens by following causes one step at a time, so formal methods are needed.

### 1.2 What Is Feedforward? (p. 1-4)
- Feedback is reactive: an error must exist before correction. If a disturbance can be measured before it enters the system, the controller can generate a signal that counteracts it. This is *feedforward* (p. 1-4).
- Feedforward is particularly useful for shaping the response to command signals, because command signals are always available. It tries to match two signals, so it requires good process models; otherwise the corrections may have the wrong size or timing (p. 1-4).
- **Fig. 1.3.** Both configurations have a process $P$, a controller $C$, a reference $r$ (desired output) and a disturbance $v$. In the feedback system, $C$ measures the output $y$ and does not directly measure $v$. In the feedforward system, $C$ measures $r$ and $v$ and computes the process input that should create the desired output. It does not measure the actual output $y$ (p. 1-4).
- **Analogies the authors offer.** Feedback vs feedforward resembles a market economy vs a planned economy. In business, a reactive approach vs extensive strategic planning. In biology, feedforward has been suggested as essential for human motion control, tuned during training. Experience indicates it is often advantageous to combine them, and the right balance needs insight into their properties (p. 1-4).
- **Table 1.1 (p. 1-5).**

| Feedback | Feedforward |
|---|---|
| Closed loop | Open loop |
| Acts on deviations | Acts on plans |
| Robust to model uncertainty | Sensitive to model uncertainty |
| Risk for instability | No risk for instability |

*Intuition note.* Feedback fixes mistakes after they show up; feedforward tries to prevent mistakes using a model. A poor model hurts feedforward more than feedback (Table 1.1).

### 1.3 What Is Control? (pp. 1-5, 1-6)
- In this book *control* is defined as the use of algorithms and feedback in engineered systems. Examples: electronic amplifiers, setpoint controllers in chemical processing, fly-by-wire, Internet router protocols. At its core control is an *information* science (p. 1-5).
- A modern controller senses the system, compares with desired behavior, computes corrective actions based on a model of the system's response, and actuates. This loop of sensing, computation and actuation is the central concept (p. 1-5).
- **Key design issues.** The closed loop must be *stable* (bounded disturbances give bounded errors). It should also have further desired behavior, such as good disturbance attenuation and fast response to changes in operating point (p. 1-5).
- **Fig. 1.4, computer-controlled system.** The process (actuators, system, sensors) is perturbed by noise at actuation and sensing, and by external disturbances. The controller has a filter, an A/D converter, a computer, and a D/A converter, synchronized by a clock. An operator supplies command signals (reference values or more general task descriptions). The algorithm that computes the action from sensor values is the *control law*. Uncertainty comes from noise, disturbances and uncertain dynamics (parameter errors, unmodeled effects) (pp. 1-5, 1-6).
- **Relation to other fields.** Control shares tools with physics, computer science and operations research but differs in insights and approach. Control-oriented modeling represents interactions between subsystems with input/output models. This gives insights such as disturbance attenuation and stable interconnection, and allows robust interconnections. Control software differs from traditional software because of system dynamics and real-time implementation (p. 1-6).

### 1.4 Uses of Feedback and Control (pp. 1-6 to 1-12)
Feedback makes it possible to design precise systems from imprecise components, to stabilize an unstable system, and to reduce disturbance effects. It also offers new degrees of freedom through sensing, actuation and computation (pp. 1-6, 1-7). Application survey:
- **Power (p. 1-7).** Early control development was driven by electrical power. Energy is hard to store, so production must match consumption. Regulation is easy with one generator and one consumer, harder in a distributed network. Large networks share loads and average consumption. Fig. 1.5: European network in 2016, more than 800 GW, more than 500 million citizens.
- **Telecommunications (p. 1-8).** Vacuum-tube amplifiers were nonlinear and time varying, so they distorted. Black's negative feedback amplifier gave stable, linear amplifiers. Research on it led to Nyquist's stability criterion and Bode's design methods and theorems on fundamental limits. Future 5G networks will permit real-time control over networks.
- **Aerospace (p. 1-8).** The Wright brothers are famous for *controlled* powered flight. Their Flyer had moving control surfaces and warpable wings. The aircraft was not stable, so continuous pilot corrections were mandatory.
- **Materials and processing (p. 1-8).** Drivers: stricter pollution limits, smaller storage (so tighter upstream control), and energy costs encouraging highly integrated plants. These trends raise complexity and performance requirements.
- **Instrumentation (pp. 1-8, 1-9).**
  - *Accelerometer.* A mass on a spring with a deflection sensor depends on accurate calibration of the spring and sensor. A weak spring gives high sensitivity but low bandwidth. With force feedback, a voice coil holds the mass at a constant position, and acceleration is proportional to the coil current. Precision then depends on the voice-coil calibration, not on the sensor, and the sensitivity/bandwidth compromise is avoided.
  - *Voltage clamp (Fig. 1.6).* Feedback controls the current $I$ so that the membrane voltage drop $\Delta v = v_\mathrm{i}-v_\mathrm{e}$ equals its reference $\Delta v_\mathrm{r}$. The current $I$ then equals the ion current. Hodgkin and Huxley used it on the squid giant axon. The patch clamp, developed by Neher and Sakmann, can show exactly when a single ion channel opens or closes.
- **Robotics and intelligent machines (p. 1-9).** Cybernetic engineering aimed at flexible, "intelligent" responses. Wiener (1948) and Tsien (1954), together with other works of the time, form much of the intellectual basis of modern robotics and control. Drones use GPS, accelerometers, magnetometers and gyros. Autonomous cars use laser rangefinders, cameras and radar plus decision-making and control algorithms (Fig. 1.7).
- **Networks and computing (pp. 1-10, 1-11).** The Internet is probably the largest feedback control system humans have built. The control problem is decentralized in nature: decisions must be made quickly and based only on local information. Stability is complicated by varying time lags, because information arrives late and the effect of a local action is felt network-wide only after substantial delay. For a server in a multi-tier system (Fig. 1.8), a quality-of-service variable (response time, throughput, memory use) is measured. Control variables might be messages accepted, OS priorities or memory allocation. Feedback keeps the variables in a target range.
- **Economics (p. 1-11).** The economy is a large dynamical system with many actors. It is hard to model because it is strongly influenced by actors' behavior and because conservation laws for important variables are missing (stock value changes rapidly and erratically). **Krugman (quoting Keynes):** the financial system was a crucial failing component; Keynes spoke of a "colossal muddle" in controlling a machine "we do not understand", and Krugman says both statements are as true now as then (p. 1-11). Supply chains (Fig. 1.9) do obey a conservation law, since products are physical, so they can be modeled by counting inventories. Multiple feedback loops exist because each agent tries to keep a proper inventory level (pp. 1-11, 1-12).
- **Feedback in nature (pp. 1-12, 1-13).**
  - Reverse engineering of biological control networks (Fig. 1.10, the growth-signaling circuitry of the mammalian cell).
  - Ecosystems: recent experience with bacterial networks suggests much of their complexity is due to multiple layers of feedback loops that give robust functionality to the cell. Sometimes cell-level events benefit the colony at the expense of the individual.
  - **Maynard Smith (1952):** the earliest birds, pterosaurs and flying insects were stable, presumably because without a highly evolved sensory and nervous system they could not fly otherwise. He says it appears that in birds and at least in some insects the evolution of these systems rendered the earlier stability "no longer necessary" (pp. 1-12, 1-13).

*Intuition note.* In many of these examples the pattern is similar: something must be kept near a target, so you measure it and adjust. The examples differ in scale, in delays (networks) and in how easy the system is to model (economics, supply chains).

### 1.5 Feedback Properties (pp. 1-13 to 1-18)
The principle: base correcting actions on the difference between desired and actual performance (p. 1-13).

**Robustness to uncertainty (pp. 1-14, 1-15).**
- Measuring the difference between the sensed and desired value lets us supply a corrective action that partially compensates for disturbances. This is what Watt exploited. Feedback also gives robustness to variations in process dynamics: the change is sensed and the system is pushed back, even if the process parameters are not directly measured (p. 1-14).
- **Cruise-control example (Fig. 1.11).** Velocity is measured and compared to the desired value. A proportional-integral (PI) controller makes the gas depend on the error and on the integral of the error. When the road changes from flat to constant uphill, the car decelerates, the controller sees the error and raises the throttle. In the plotted simulation, the velocity returns to the desired value within about 15 s, for masses between 1200 and 2000 kg (the text says "a factor of ± 25%"). The authors conclude that feedback improves both performance and robustness (p. 1-14).
- **Black's feedback amplifier (1927).** Distortion from the nonlinear tube and amplifier drift had been obstacles. Negative feedback reduces the gain but makes the amplifier insensitive to variations in tube characteristics, giving stable, linear amplifiers (p. 1-15).

**Design of dynamics (pp. 1-15, 1-16).**
- Feedback can alter behavior: unstable systems can be stabilized, sluggish systems made responsive, drifting operating points held constant (p. 1-15).
- **Wilbur Wright (1901).** Wings and engines were known; "inability to balance and steer" remained the open problem, and he said other difficulties were of minor importance (p. 1-15).
- The Wright Flyer resolved the compromise between stability and maneuverability by being unstable but maneuverable. The pilot had to keep adjusting the rudder: if the pilot let go, the plane would crash. Other early aviators built stable airplanes with poor maneuverability that could not be brought into the air. Modern fighters are also unstable in certain flight regimes (p. 1-15).
- Sperry's autopilot used a gyro-stabilized pendulum to indicate the vertical and a feedback mechanism that pulled the stick up if the plane pointed down, and vice versa. It was the first use of feedback in aeronautical engineering (Fig. 1.12). The authors call it an example of using feedback to stabilize an unstable system, hence "design the dynamics" (p. 1-16).

**Creating modularity (pp. 1-16, 1-17).**
- A *modular* system is one in which individual components can be replaced without modifying the entire system. Feedback can let components keep their input/output properties robustly despite changes in interconnections (p. 1-16).
- **Fig. 1.13: electrical drive with three cascaded loops.** The innermost loop is the current loop (current controller CC drives the amplifier so motor current tracks its setpoint). The middle loop is the velocity loop (VC sets the CC setpoint). The outer loop is the position loop (PC sets the VC setpoint). Each loop's setpoint is the externally supplied reference plus the output of the next outer controller (pp. 1-16, 1-17).
- **Design argument.** With a well-designed current controller, current follows its setpoint. Motor torque is proportional to current, so the dynamics from the CC input to motor velocity are approximately an integrator, written $1/s$ in Fig. 1.13. This simplified model is used to design the velocity loop, and then the position loop is also simple. Loops can be tuned sequentially from the inner loop (p. 1-17).
- **Modularity.** Each design stage depends only on the closed-loop behavior of the system (in the nested architecture, the inner loops). If the motor is replaced, redesign CC to give the same closed-loop performance and leave the outer loops unchanged. An existing inner-loop design can be reused if it gives enough performance for the outer loop (p. 1-17).

**Challenges of feedback (pp. 1-17, 1-18).**
- Chief drawback: possible instability if the system is not designed properly. Example: a microphone with the amplification turned up too high, a feedback instability. The system must be stable under nominal conditions and under all possible perturbations of the dynamics (p. 1-17).
- Feedback couples parts of a system and often injects measurement noise. Measurements must be filtered so actuation and process do not respond to noise, while the sensor signal is still coupled in properly for performance (p. 1-17).
- Complexity: control systems are often complicated, so costs and benefits must be balanced. Example: microprocessor-based feedback in cars began in the early 1970s, driven by stricter emissions standards that could be met only through electronic controls. Early systems were expensive and failed often (p. 1-18).

*Intuition note.* Feedback gets accuracy from measuring, not from precise parts. The costs are a risk of instability and measurement noise entering the system.

### 1.6 Simple Forms of Feedback (pp. 1-18 to 1-20)
**On-off control.** With control error $e = r - y$ and actuation command $u$:
$$u=\begin{cases}u_{\max} & \text{if } e>0,\\ u_{\min} & \text{if } e<0,\end{cases}\tag{1.1}$$
Maximum corrective action is always used. Advantages: simple, no parameters to choose. It often keeps the variable close to the reference (a thermostat), typically with oscillation, which is often acceptable if small. Equation (1.1) is undefined at $e=0$; common fixes are a *dead zone* or *hysteresis* (Fig. 1.14). With hysteresis the output depends on past inputs (pp. 1-18, 1-19).

**Proportional control.** On-off control often oscillates because the system overreacts: a small change in error moves the actuator over its full range. Proportional control avoids this for small errors:
$$u=\begin{cases}u_{\max} & \text{if } e\ge e_{\max},\\ k_\mathrm{p}\,e & \text{if } e_{\min}<e<e_{\max},\\ u_{\min} & \text{if } e\le e_{\min},\end{cases}\tag{1.2}$$
where $k_\mathrm{p}$ is the controller gain, $e_{\min}=u_{\min}/k_\mathrm{p}$ and $e_{\max}=u_{\max}/k_\mathrm{p}$. The interval $(e_{\min},e_{\max})$ is the *linear range*, where
$$u=k_\mathrm{p}(r-y)=k_\mathrm{p}\,e\quad\text{if } e_{\min}\le e\le e_{\max}.\tag{1.3}$$
Drawback: the process variable often deviates from its reference. If some control signal level is needed to hold the desired value, then $e\neq 0$ is needed to generate it (p. 1-19).

**Integral control.**
$$u(t)=k_\mathrm{i}\int_0^t e(\tau)\,d\tau,\tag{1.4}$$
with integral gain $k_\mathrm{i}$. The authors state it can be shown by simple arguments that a controller with integral action has zero steady-state error (this is Exercise 1.5). Caveats: there may be no steady state (the system may oscillate). With magnitude limits as in (1.2), "integrator windup" can occur and may give poor performance unless "anti-windup" compensation is used. Because integral feedback gives zero error under constant disturbances, it is one of the most used forms of feedback (p. 1-19).

**Derivative action and PID.** To give anticipation, use linear extrapolation to predict the error $T_\mathrm{d}$ time units ahead:
$$e(t+T_\mathrm{d})\approx e(t)+T_\mathrm{d}\,\frac{de(t)}{dt}.$$
Combining the three terms gives the PID controller:
$$u(t)=k_\mathrm{p}\,e(t)+k_\mathrm{i}\int_0^t e(\tau)\,d\tau+k_\mathrm{d}\,\frac{de(t)}{dt}.\tag{1.5}$$
The action is a sum of the present (proportional term), the past (integral of error), and the future (linear extrapolation of the error, i.e. the derivative term) (Fig. 1.15). The authors say more than 95% of industrial control problems are solved by PID control, though many of these controllers are PI because derivative action is often not included (p. 1-20).

*Intuition note.* P reacts to the error now, I to the error accumulated so far, D to where the error is heading. P alone can leave a lasting offset. I can remove it under a constant disturbance if a steady state is reached, but windup can occur when the control action has magnitude limits, and there may be no steady state (the system may oscillate).

### 1.7 Combining Feedback with Logic (pp. 1-20 to 1-23)
Continuous control is often combined with logic for changes in operating mode, equipment protection, manual interaction and saturating actuators. Example: a compressor's outflow is the primary variable, but the controller may switch mode to avoid compressor stall (p. 1-20).

**Cruise control (Fig. 1.16, p. 1-21).** The basic function, keeping velocity constant, is typically done by a PI controller. It must be switched off when braking, accelerating or changing gears. A finite state machine governs the modes of the PI controller and the reference generator. It has four modes and four buttons (on/off, coast/set, resume/accelerate, cancel):
- *Off ↔ Standby* via the on/off switch.
- *Standby → Cruise* by pushing set/coast. The velocity reference is the car's velocity when the button is released.
- *In Cruise*, the reference is raised with resume/accelerate and lowered with set/coast. If the driver accelerates with the pedal, speed returns to the set value on release.
- *Braking* sends Cruise → Hold, and the setpoint is remembered. Resume/accelerate returns to Cruise.
- *Cancel* moves Cruise → Standby, and the reference is remembered. On/off turns the system off when it is engaged.
The PI controller is designed for good regulation and good transients when switching between resume and control modes (p. 1-21).

**Server farms (Fig. 1.17, p. 1-22).** Energy can be more than 40% of data-center operating cost. Demand varies strongly, with constraints on electricity and cooling. Raising an individual server's voltage raises its clock rate and throughput, but also energy and cooling needs. Switching servers off saves energy, but switching one on takes time. The cooling measurement is the server with the highest temperature. Temperature control combines feedforward logic (when servers are switched on and off) with PID feedback.

**Air–fuel control for ship boilers (Fig. 1.18, p. 1-23).** Two loops control air and oil flow. A supervisory controller adjusts the ratio: efficient on open sea, but air excess is needed in harbor, because black smoke is penalized. Solution: PI controllers plus *selectors*. A selector is a static system with several inputs and one output. A maximum selector outputs the largest input, a minimum selector the smallest.
- *Power demand increases:* the air controller's reference is the commanded power (via the max selector), and the oil controller's reference is the measured airflow. Oil lags air, so there is air excess.
- *Power demand decreases:* the oil controller's reference is the power demand (min selector), and the air controller's reference is the oil flow (max selector). Again air excess results.
Simulation (Fig. 1.18b) shows air flow above fuel flow for both step directions. Selectors are also used for reliability: with three sensors, accepting only values where two agree guards against failure of a single sensor.

### 1.8 Control System Architectures (pp. 1-24 to 1-27)
Real systems combine simple loops into hierarchies of controllers, logic and optimization (Fig. 1.19 shows layers; Chapter 15 treats this in more detail) (p. 1-24).
- **Freight train trip optimizer (GE, Fig. 1.20).** Requirements: arrive on time with little fuel; avoid unnecessary braking. Low layer: a speed regulator (with a track model, GPS and an estimator; the key disturbance is ground slope) and logic to avoid zones occupied by another train. The speed setpoint comes from a trip optimizer that computes a fuel-minimizing plan for the desired arrival time, set by a dispatch center. The top layer is the human operator. A typical locomotive burns about 35,000 gallons per year and can save an average 10% with Trip Optimizer (pp. 1-24, 1-25).
- **Process control (paper factory, Figs. 1.21, 1.22).** Each production unit has PI(D) loops for flow, temperature and tank levels (time scales from fractions of seconds to minutes), plus safety logic and sequencing. A supervisory system measures tank levels and sets production rates by optimization on minutes-to-hours scales. These systems span many time and spatial scales and integrate with supply chains. Fig. 1.22 shows a distributed control system (DCS) architecture (p. 1-25).
- **Autonomous driving (Fig. 1.23, Caltech's "Alice").** Sensors are fused into a multi-layer map. The traffic planner and mission planner are two levels of discrete decision logic. An optimization-based path planner computes a trajectory, which a path-following module tracks. A supervisory module handles mission planning and contingencies. Low-level information (speed, lane position) goes to the tracking controller; higher-level information goes to the planners (p. 1-27).

### 1.9 Further Reading (pp. 1-27, 1-28)
Pointers to history (Mayr, Bennett, Mindell, Kelly), engineering and mathematical textbooks, biology and physics texts, and computing-systems books. Systems combining continuous feedback with logic and sequencing are called *hybrid systems*; their theory is outside this text (p. 1-28).

## Toy example (ours, not from the text)
**Idea:** feedback acts on the measured error, so it copes with a disturbance the plan did not include. It also shows why proportional control alone can leave an offset (p. 1-19).

Plant (a leaking tank): $y_{k+1}=y_k+u_k-d$, with $y_0=0$, reference $r=10$. The plan assumed $d=0$, but the true leak is $d=1$.

*Open loop (the plan):* $u_0=10$, then $u_k=0$. Then $y_1=0+10-1=9$, $y_2=9+0-1=8$, $y_3=7$, … The output drifts down by 1 each step, because nothing measures it.

*Feedback with $u_k=k_\mathrm{p}e_k$, $e_k=r-y_k$, $k_\mathrm{p}=0.5$:*

| k | $y_k$ | $e_k$ | $u_k=0.5e_k$ | $y_{k+1}=y_k+u_k-1$ |
|---|---|---|---|---|
| 0 | 0 | 10 | 5 | 4 |
| 1 | 4 | 6 | 3 | 6 |
| 2 | 6 | 4 | 2 | 7 |
| 3 | 7 | 3 | 1.5 | 7.5 |
| 4 | 7.5 | 2.5 | 1.25 | 7.75 |

The error follows $e_{k+1}=r-y_{k+1}=e_k-0.5e_k+1=0.5e_k+1$ (added step), whose steady value solves $e=0.5e+1$, so $e=2$ and $y\to 8$. The output holds near the reference despite the unmodeled leak, but with an offset of 2. At that steady state $u=0.5\cdot 2=1=d$: the controller needs $e\ne 0$ to produce the input that cancels the leak. This is the proportional-control drawback described on p. 1-19, and what integral action (1.4) is introduced to remove.

## Concepts
- [[feedback]] — two or more dynamical systems coupled so each influences the other; correction based on desired vs actual performance (pp. 1-1, 1-13)
- [[open loop vs closed loop]] — closed: systems interconnected in a cycle; open: the interconnection is broken (p. 1-1)
- [[negative (balancing) feedback]] — reacting to disturbances so their effects decrease (p. 1-2)
- [[positive (reinforcing) feedback]] — an increase leads to further increase; destabilizing, usually limited by saturation (p. 1-2)
- [[feedforward]] — measure a disturbance (or the reference) and act before it affects the output; needs a good model (p. 1-4)
- [[reference (set point)]] — desired output $r$ (also "setpoint" for inner loops) (pp. 1-4, 1-16)
- [[error signal]] — control error $e=r-y$ (p. 1-18)
- [[plant]] — here the "process" $P$ or "system" being controlled; in Fig. 1.4 it includes sensors and actuators (pp. 1-4, 1-6)
- [[disturbance and noise]] — external perturbations $v$ on the process and noise in sensing and actuation (pp. 1-4, 1-6)
- [[delay (dead time)]] — varying time lags complicate stability in networks (p. 1-10)
- [[gain]] — controller gain $k_\mathrm{p}$ in (1.2); also the amplifier gain reduced by negative feedback (pp. 1-15, 1-19)
- [[stability]] — in this chapter: bounded disturbances give bounded errors (p. 1-5)
- [[PID control]] — sum of proportional, integral and derivative terms, Eq. (1.5) (p. 1-20)
- [[integral action]] — control proportional to the integral of the error; zero steady-state error if a steady state is reached (p. 1-19)
- [[robustness]] — feedback gives good performance despite disturbances and uncertain process dynamics (p. 1-14)
- [[homeostasis]] — biological feedback maintaining thermal, chemical and biological conditions (p. 1-3)
- [[on-off control]] (new) — $u_{\max}$ or $u_{\min}$ according to the sign of $e$, Eq. (1.1) (p. 1-18)
- [[control law]] (new) — the algorithm computing the control action from sensor values (p. 1-5)
- [[integrator windup]] (new) — a problem when integral control meets actuator limits; needs anti-windup compensation (p. 1-19)
- [[cascaded loops / modularity]] (new) — nested loops where each design stage depends only on the closed-loop behavior of the system (p. 1-17)
- [[finite state machine]] (new) — logic that switches the controller between modes (p. 1-21)
- [[selector]] (new) — static max/min of inputs, used for logic and sensor-failure protection (p. 1-23)
- [[layered control architecture]] (new) — hierarchy of feedback, logic and optimization layers (p. 1-24)
- [[hybrid system]] (new) — feedback combined with logic and sequencing; theory outside this book (p. 1-28)

## Canonical instances
- [[blood-glucose-regulation]] — insulin/glucagon feedback keeping glucose near 90 mg/100 mL (p. 1-2)
- [[centrifugal-governor]] — flyball negative feedback on steam-engine speed (p. 1-2)
- [[black-feedback-amplifier]] — negative feedback linearizes a nonlinear tube amplifier at the cost of gain (p. 1-15)
- [[wright-flyer-and-sperry-autopilot]] — unstable but maneuverable aircraft; feedback stabilization (pp. 1-15, 1-16)
- [[cruise-control]] — PI speed control robust to road slope and mass; mode logic via state machine (pp. 1-14, 1-21)
- [[voltage-clamp]] — feedback used as a measuring instrument for ion currents (p. 1-9)
- [[electrical-drive-cascade]] — current, velocity and position loops (p. 1-17)
- [[supply-chain-dynamics]] — inventory feedback with a conservation law (p. 1-12)
- [[air-fuel-selector-control]] — max/min selectors keep air excess in ship boilers (p. 1-23)
- [[trip-optimizer]] — layered train control: speed regulator plus fuel-optimal plan (p. 1-24)
- [[server-farm-control]] — feedforward logic plus PID for temperature (p. 1-22)
- [[economy-as-controlled-system]] — financial system as a controller that may fail (p. 1-11)

## Bridges (candidates)
- [structural-analogy] Feedback vs feedforward ↔ economics: market-based vs planned economy — the text itself draws the analogy (p. 1-4).
- [structural-analogy] Feedback instability (microphone howl) ↔ positive feedback / runaway in markets or ecosystems — same loop-gain logic, but the chapter does not develop it.
- [structural-analogy] Integral action u = k_i∫e ↔ accumulator or error-correction terms in learning rules — only if both are the same running sum of errors (not stated in this unit).
- [structural-analogy] Cascaded loops with setpoints ↔ hierarchical organization (inner loops follow commands from outer loops) in management or in motor control.
- [metaphor] Maynard Smith's birds (stability traded for maneuverability once sensing evolved) ↔ organisms that rely on sensing and neural control instead of passive stability.

## Questions this raises
- When, formally, does a closed loop become unstable, and how does delay change that?
- How should an engineer choose the balance between feedforward and feedback when the model is imperfect?
- Why can integral action lead to windup when the control action has magnitude limits, and how is this avoided?
- How do the layers of Fig. 1.19 (optimization, estimation, PID) interact and stay stable together (Chapter 15)?

## Exercises worth doing
- Ex. 1.1 (p. 1-28) — identify sensing, actuation, control law and uncertainty in five everyday feedback systems — difficulty: easy
- Ex. 1.2 (p. 1-28) — map the balance-on-one-foot control system onto Fig. 1.4 — difficulty: easy
- Ex. 1.3 (p. 1-28) — compare control systems for tracking a moving hand versus shaking the head — difficulty: medium
- Ex. 1.4 (p. 1-28) — tune the cruise-control law by trial and error for m = 1200 kg and test robustness at m = 2000 kg — difficulty: medium
- Ex. 1.5 (p. 1-29) — show integral action gives zero error if a steady state is reached (no saturation) — difficulty: medium
- Ex. 1.6 (p. 1-29) — specify actions in each state of the cruise-control state machine and any extra stored variables — difficulty: medium

## Reading notes
- The page labels give no printed number ("?"), but the page images show running numbers of the form "1-N" (e.g. "1-1" on the first page). All citations use these. Offset: pdf page = N + 12 (pdf 13 = p. 1-1, pdf 41 = p. 1-29).
- pdf 42 (p. 1-30) contains only the running header and no text.
- The text layer shows stray circled "L" marks on pp. 1-8 and 1-12; they carry no content.
- Small misprints in the source: "desired the reference value" (p. 1-4); "can be see in the control" (p. 1-24).
- Equations (1.1)–(1.5) and the extrapolation formula were checked against the page images. Equation (1.2) uses $\ge$ and $\le$ at the ends, while (1.3) states the linear range with closed bounds. This follows the source.
- The 1.5 text says the mass "varies by a factor of ± 25%", while the Fig. 1.11 caption says masses between 1200 and 2000 kg. I report both as printed.
- Black's amplifier is cited as [Bla34] in 1.4 and described as invented in 1927 in 1.5. [Bla34] is a citation key and the pages do not state a conflict; I only note that the 1927 invention date appears in 1.5.
- Exercises 1.5 and 1.4 refer to equations and a companion web site; the solutions are not given in this unit.
