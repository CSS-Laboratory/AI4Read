---
id: astrom-2021-feedbacksystems/ch04-examples
work: astrom-2021-feedbacksystems
unit: "4 Examples"
pages: 4-1 to 4-32
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
# Chapter 4 — Examples

## L0 — One line
Seven everyday and scientific systems (car, bicycle, op amp, web server and Internet, atomic force microscope, drug and glucose dynamics, populations) are each reduced to a small model with a state, inputs and outputs; for several of them the author also says where the model stops being valid.

## L1 — The gist (≤ 120 words)
The chapter gives worked examples that later chapters reuse. The examples describe states, inputs and outputs (a disturbance is named for cruise control), write simple equations (mostly ODEs, one discrete-time), and for several of them say where the model stops being valid. Some are physical (car, bicycle, op amp, microscope), some are computing systems (web server, Internet congestion), and some are biological or ecological (drugs, glucose, predator–prey). Messages that appear: a simple model can be good enough for control design (cruise control), feedback can make precise systems from uncertain parts, and feedback can be hidden in a design, as in the bicycle fork.

**Prerequisites:** first-order ODEs and equilibria; matrix–vector notation; the idea of state, input and output from Chapter 3; PI control (Chapter 1).

## L2 — Key ideas
- A model for control design can be very simple even when the system has many components. The author asks us to respect its validity range ("uncertainty lemon", Fig. 3.5b) (p. 4-2, p. 4-4).
- Cruise control is a first-order nonlinear system with state $v$, input $u$ and disturbance $F_d=mg\sin\theta$. A PI controller removes the steady-state speed error on a hill (p. 4-3, p. 4-4).
- A bicycle's front fork creates a feedback from roll angle to steering angle. In the author's crude model this feedback can stabilize the bicycle above a threshold speed (p. 4-7).
- Op-amp feedback makes the closed-loop gain depend almost only on the resistor ratio, so variations in the very large open-loop gain $k$ have little effect (p. 4-10).
- Computing systems also have states, actuators and models: a linear discrete-time model of a web server identified from data, and a delay-differential model of TCP congestion control (p. 4-13, p. 4-15).
- Microscope, drug and glucose examples show modelling choices: static versus dynamic blocks, and compartments with proportional flows. Compartment models can be written "by inspection" from the diagram (p. 4-19, p. 4-23).
- Population models give equilibria that can be computed by hand, such as the three predator–prey equilibria. For the chosen parameters, the simulated populations oscillate (p. 4-27, p. 4-28).

## L3 — Walkthrough

**Chapter opening.** The epigraph (Golomb, 1970) warns against applying a model before one understands its simplifying assumptions and can test them. It ends: "You will never strike oil by drilling through the map." (p. 4-1). First-time readers may focus on a few familiar examples to grasp state, input, output and dynamics (p. 4-1).

### 4.1 Cruise control
**Setup.** The controller (typically PI) takes speed $v$ and reference $v_r$ and produces a normalized control signal $u$ for the throttle actuator. The throttle sets engine torque $T$, which acts through gears and wheels as force $F$. Disturbance forces $F_d$ come from road slope, rolling resistance and aerodynamics (p. 4-1, Fig. 4.1 on p. 4-2). A driver interface sets the reference speed. The system disconnects when the brake is touched (p. 4-1).

**Model.** With $m$ the total mass:
$$m\frac{dv}{dt}=F-F_d \tag{4.1}$$
Typical mass is 1000–2000 kg; 1600 kg is used (p. 4-2).

The engine torque is proportional to the fuel injection rate, which is proportional to the control signal $0\le u\le 1$. Torque at full throttle depends on engine speed $\omega$:
$$T(\omega)=T_m\Big(1-\beta\Big(\frac{\omega}{\omega_m}-1\Big)^2\Big)\tag{4.2}$$
Typical values are $T_m=190$ Nm, $\omega_m=420$ rad/s (about 4000 RPM) and $\beta=0.4$ (p. 4-2).

With gear ratio $n$ and wheel radius $r$: $\omega=\frac{n}{r}v=:\alpha_n v$ and $F=\frac{nu}{r}T(\omega)=\alpha_n u\,T(\alpha_n v)$ (p. 4-2). For gears 1–5, $\alpha_n=40,25,16,12,10$. $1/\alpha_n$ is the effective wheel radius. The gear "flattens" the torque curve, so nearly full torque is available over almost the whole speed range (Fig. 4.2, p. 4-3).

The disturbance has three parts (p. 4-3):
- gravity, $F_g=mg\sin\theta$, with slope $\theta$ and $g=9.8$ m/s²;
- rolling friction, $F_r=mgC_r\,\mathrm{sgn}(v)$, with $C_r=0.01$;
- aerodynamic drag, $F_a=\tfrac12\rho C_d A|v|v$, with $\rho=1.3$ kg/m³, $C_d=0.32$, $A=2.4$ m².

The summary model is
$$m\frac{dv}{dt}=\alpha_n u\,T(\alpha_n v)-mgC_r\,\mathrm{sgn}(v)-\tfrac12\rho C_dA|v|v-mg\sin\theta .\tag{4.3}$$
It is first order. The state is $v$, which is also the output. The input is $u$ and the disturbance is $F_d=mg\sin\theta$. It is nonlinear (torque curve, gravity term, rolling friction, drag). Parameters can vary, for example with passengers and load (p. 4-3, p. 4-4).

**PI controller.** $u(t)=k_pe(t)+k_i\int_0^te(\tau)d\tau$. As a dynamical system with controller state $z$:
$$\frac{dz}{dt}=v_r-v,\qquad u=k_p(v_r-v)+k_iz.\tag{4.4}$$
The integrator ensures that the steady-state error goes to zero even with disturbances or modelling errors (p. 4-4).

**Hill response (Fig. 4.3b).** The hill is a net 4° change in $\theta$, ramped linearly between $t=5$ and $t=6$, with $k_p=0.5$ and $k_i=0.1$. The author says that even if the hill is so steep that the throttle changes from 0.17 to almost full throttle, the largest speed error is below 1 m/s and the speed is recovered after 20 s (p. 4-4).

**Validity.** The model is not valid for very rapid throttle changes (engine dynamics ignored) or very slow ones (engine properties change over years) (p. 4-4). It is still useful because of the robustness of feedback: a controller designed on an imperfect model can use feedback to manage the uncertainty (p. 4-5).

**Interface.** A finite state machine (Fig. 4.4) governs the modes of the PI controller and reference generator. The caption says there are four modes (the diagram labels them Off, Standby, Cruise, Hold) and five buttons: on, off, set, resume, cancel (p. 4-5). Other automotive applications mentioned: emissions control, traction control, power control, adaptive cruise control (p. 4-5).

*Intuition note.* A car with many parts reduces to one first-order equation: force balance, with the engine as the input and the road as the disturbance. In steady state the integral term drives the speed error to zero, even with a slope disturbance (p. 4-4).

### 4.2 Bicycle dynamics
**Frame model.** Use coordinates fixed to the bicycle: $\xi$ through the wheel contact points, $\eta$ horizontal, $\zeta$ vertical. Let $v_0$ be the rear-wheel velocity, $b$ the wheelbase, $\varphi$ the tilt (roll) angle and $\delta$ the steering angle. The frame rotates about a point $O$ with angular velocity $\omega=v_0\delta/b$ (p. 4-5, p. 4-6). Tilting is like an inverted pendulum (p. 4-6). Let $m$ be the total mass, $J$ the moment of inertia about $\xi$ and $D$ the product of inertia for the $\xi\zeta$ axes. The centre of mass has coordinates $a,h$ relative to the rear contact point $P_1$, with $J\approx mh^2$ and $D=mah$. For small $\delta$:
$$J\frac{d^2\varphi}{dt^2}-\frac{Dv_0}{b}\frac{d\delta}{dt}=mgh\sin\varphi+\frac{mv_0^2h}{b}\delta .\tag{4.5}$$
$mgh\sin\varphi$ is the gravity torque. The terms with $\delta$ are steering torques: $(Dv_0/b)\,d\delta/dt$ from inertial forces and $(mv_0^2h/b)\,\delta$ from centripetal forces (p. 4-6).

**Fork as feedback.** The front-wheel contact point $P_2$ lies behind the steering axis; the distance $c$ is the trail. A large trail increases stability but makes steering less agile (p. 4-6). Hence $\delta$ is influenced both by the steering torque $T$ and by the tilt $\varphi$. A bicycle with a fork is a feedback system (Fig. 4.6), with "circular causality" between $\delta$ and $\varphi$. With positive trail the bicycle steers into the lean, creating a centrifugal force that attempts to diminish the lean (p. 4-6, p. 4-7).

**Crude model.** Model the fork as the static system
$$\delta=k_1T-k_2\varphi .\tag{4.6}$$
Substituting (4.6) into (4.5) and approximating $\sin\varphi\approx\varphi$ gives (added step: move the $\varphi$ and $\dot\varphi$ terms to the left)
$$J\frac{d^2\varphi}{dt^2}+\frac{Dv_0k_2}{b}\frac{d\varphi}{dt}+\Big(\frac{mv_0^2hk_2}{b}-mgh\Big)\varphi=\frac{Dv_0k_1}{b}\frac{dT}{dt}+\frac{mv_0^2hk_1}{b}T .\tag{4.7}$$
The left side looks like a spring–mass system with damping $Dv_0k_2/b$ and spring term $mv_0^2hk_2/b-mgh$. The spring term is negative at $v_0=0$ and positive for $v_0>\sqrt{gb/k_2}$ (added step: this is $mv_0^2hk_2/b>mgh$). The author concludes that, in this model, the bicycle is unstable at small velocities and the fork feedback makes it stable at sufficiently large velocity (p. 4-7).

**Whipple model.** The simple model neglects fork dynamics, tire–road interaction and velocity-dependent parameters. The more accurate Whipple model (presented in 1899, p. 4-8), for small angles, is
$$M\begin{pmatrix}\ddot\varphi\\ \ddot\delta\end{pmatrix}+Cv_0\begin{pmatrix}\dot\varphi\\ \dot\delta\end{pmatrix}+(K_0+K_2v_0^2)\begin{pmatrix}\varphi\\ \delta\end{pmatrix}=\begin{pmatrix}0\\ T\end{pmatrix}\tag{4.8}$$
Here $M,C,K_0,K_2$ are $2\times2$ matrices depending on geometry and mass distribution. It has a form somewhat similar to the spring–mass system of Chapter 3. Even this model neglects tire–road interaction, which would need two more states (p. 4-7).

*Intuition note.* The fork turns the wheel into the lean. That is a correction proportional to the tilt, a feedback built into the geometry. In the crude model the stabilizing effect beats gravity when the bicycle is fast enough (above $\sqrt{gb/k_2}$); the author concludes the bicycle is unstable at small velocities.

### 4.3 Operational amplifier circuits
**Op-amp model.** The op amp is "a modern implementation of Black's feedback amplifier" (p. 4-8). It has inverting input $v_-$, non-inverting input $v_+$ and output $v_{out}$. Assume zero input currents and a static output
$$v_{out}=\mathrm{sat}_{(v_{min},v_{max})}\big(k(v_+-v_-)\big),\tag{4.9}$$
$$\mathrm{sat}_{(a,b)}(x)=\begin{cases}a&x<a\\x&a\le x\le b\\ b&x>b\end{cases}\tag{4.10}$$
Here $k$ is in the range $10^6$–$10^8$ and $e_-\le v_{min}<v_{max}\le e_+$ (supply voltages). In the linear range
$$v_{out}=k(v_+-v_-)=:-kv .\tag{4.11}$$
The linear range of input is very small because $k$ is very large (p. 4-8). A smooth saturation (Fig. 4.8) gives a more accurate model (p. 4-8).

**Feedback amplifier (Fig. 4.9a).** Assume $i_0=0$ and $v=v_--v_+=0$. Ohm's law gives $v_1/R_1=-v_2/R_2$, so
$$\frac{v_2}{v_1}=-k_{cl},\quad k_{cl}=\frac{R_2}{R_1}.\tag{4.12}$$
A more accurate model keeps $v$ small but non-zero. The current balance is
$$\frac{v_1-v}{R_1}=\frac{v-v_2}{R_2}.\tag{4.13}$$
With (4.11) and $v_{out}=v_2$:
$$k_{cl}=-\frac{v_2}{v_1}=\frac{R_2}{R_1}\,\frac{kR_1}{R_1+R_2+kR_1}\approx\frac{R_2}{R_1}.\tag{4.14}$$
If $k$ is large, the closed-loop gain is close to $R_2/R_1$, so it depends only on the passive components, and variations in $k$ have only a marginal effect. Example: $k=10^6$ and $R_2/R_1=100$; a 100% variation in $k$ gives only 0.01% variation in closed-loop gain. Feedback "trades high gain and low robustness for low gain and high robustness". Equation (4.14) inspired Black (p. 4-10).

**Block diagram (Fig. 4.9b).** Solving (4.13) for $v$:
$$v=\frac{R_2}{R_1+R_2}v_1+\frac{R_1}{R_1+R_2}v_2=\frac{R_1}{R_1+R_2}\Big(\frac{R_2}{R_1}v_1+v_2\Big).$$
The diagram shows the feedback; the gain from $v_2$ to $v$ is $R_1/(R_1+R_2)$. If the loop is stable and the amplifier gain is large, the error $e$ is small and $v_2=-(R_2/R_1)v_1$. $R_1$ appears in two blocks, which the author says is one reason block diagrams are not always well suited for some types of physical modelling (p. 4-10).

**Dynamic model.** The more realistic model is
$$\frac{dv_{out}}{dt}=-av_{out}-bv.\tag{4.15}$$
The parameter $b$ is the gain-bandwidth product. The model fails at very high or low frequencies, for large signals (supply limit typically 5–10 V) and for very small signals (noise) (p. 4-10).

**PI controller circuit (Fig. 4.10).** Assume $i_0=0$ and $v$ negligible. The current through $R_1$ and the capacitor is $i=v_1/R_1=C\,dv_c/dt$. Then
$$v_c(t)=\frac1C\int i\,dt=\frac1{R_1C}\int_0^tv_1(\tau)d\tau,$$
$$v_2(t)=-R_2i-v_c=-\frac{R_2}{R_1}v_1(t)-\frac1{R_1C}\int_0^tv_1(\tau)d\tau,$$
which is the input/output relation of a PI controller (p. 4-11). The author states that any linear system can be implemented with op amps, resistors and capacitors (p. 4-10).

*Intuition note.* With a stable loop and a large gain, feeding a fraction of the output back to the input keeps the input voltage $v$ very small. The output is then set by the resistor ratio, not by the unreliable internal gain.

### 4.4 Computing systems and networks
Sensors measure resource use (processor load, memory, bandwidth). Actuators set limits on resources, turn processes on or off, delay a resource or reject requests. Empirical models are often used when no first-principles model exists (p. 4-11).

**Web server control.** An Apache server queues connection requests and starts a subprocess per accepted connection. Each subprocess alternates Busy and Wait. After a time set by `KeepAlive` it becomes Idle. At most `MaxClients` requests are served at once (p. 4-12, Fig. 4.11). The parameters trade performance against resource use. More `MaxClients` pulls requests off the queue faster but needs more processing and memory. A longer `KeepAlive` lowers processing load but lengthens the queue (p. 4-12, p. 4-13). Feedback can keep performance good although the available processing power and memory are uncertain (p. 4-12).

The discrete-time linear model has states $x_{cpu}$ (average processor load) and $x_{mem}$ (percentage memory usage), and inputs $u_{ka}$ and $u_{mc}$:
$$\begin{pmatrix}x_{cpu}[k+1]\\x_{mem}[k+1]\end{pmatrix}=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix}\begin{pmatrix}x_{cpu}[k]\\x_{mem}[k]\end{pmatrix}+\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix}\begin{pmatrix}u_{ka}[k]\\u_{mc}[k]\end{pmatrix}\tag{4.16}$$
Shapes: state $\in\mathbb R^2$, $A$ is $2\times2$, $B$ is $2\times2$, input $\in\mathbb R^2$. System identification by Diao et al. gave
$$A=\begin{pmatrix}0.54&-0.11\\-0.026&0.63\end{pmatrix},\quad B=\begin{pmatrix}-85&4.4\\-2.5&2.8\end{pmatrix}\times10^{-4},$$
linearized about $x_{cpu}=0.58$, $u_{ka}=11$ s, $x_{mem}=0.55$, $u_{mc}=600$ (p. 4-13).

Reading the matrices (author): a longer `KeepAlive` (first column of $B$) lowers both processor and memory usage. `MaxClients` raises both. The largest effect on processor load is `KeepAlive`. The diagonal of $A$ describes how each resource returns to equilibrium. The off-diagonal terms show coupling between the resources (p. 4-13). The model uses averages over a sample time, so it is not accurate for high-frequency phenomena (p. 4-13).

**Congestion control.** TCP/IP evolved after congestion collapses in the mid 1980s, when throughput "could drop by a factor of 1000". TCP conserves the number of packets in the loop from sender to receiver and back. The sending rate increases when there is no congestion and drops to a low level when there is (p. 4-14). Model three elements: sources, router queues and admission control (Fig. 4.12a).

*Source (TCP/Reno).* The window size (packets sent without waiting for acknowledgments) is, roughly speaking, increased at a fixed rate while packets are acknowledged and cut in half when packets are lost (p. 4-15). With $N$ sources, window $w_i$, end-to-end drop probability $q_i$ and round-trip time $\tau_i$:
$$\frac{dw_i}{dt}=(1-q_i)\frac{r_i(t-\tau_i)}{w_i}-q_i\Big(\frac{w_i}{2}r_i(t-\tau_i)\Big),\qquad r_i=\frac{w_i}{\tau_i}.\tag{4.17}$$
The first term is the increase when a packet is received. The second is the decrease when one is lost. The delay $\tau_i$ is the time to receive acknowledgments (p. 4-15).

*Link (router queue).* With $L$ links, buffer contents $b_l$ and link capacity $c_l$:
$$\frac{db_l}{dt}=\begin{cases}s_l-c_l&b_l>0\\0&b_l=0\end{cases},\qquad s_l=\sum_{i=1}^LR_{li}\,r_i(t-\tau^f_{li}).\tag{4.18}$$
$R_{li}=1$ if link $l$ is used by source $i$ (else 0), and $R\in\mathbb R^{L\times N}$ is the routing matrix (p. 4-15).

*Admission control.* The drop probability is $p_l=\beta_l(b_l,b_{l,max})$ with $\beta_l(0,\cdot)=0$ and $\beta_l(b_{l,max},b_{l,max})=1$. For now $p_l=\rho_lb_l$ (Exercise 4.5 gives a more detailed model) (p. 4-15). The end-to-end loss probability is, as printed,
$$q_i=1-\prod_{l=1}^LR_{li}(1-p_l)\approx\sum_{l=0}^LR_{li}\,p_l(t-\tau^b_{il}),\tag{4.19}$$
valid for small individual drop probabilities, with $\tau^b_{il}$ the backward delay (p. 4-16).

*Special case.* Take $N$ identical sources and one link, ignore forward and backward delays, and assume the router is never saturated or empty. Then, with $\tau^p:=b/c$,
$$\frac{dw_i}{dt}=\frac1{\tau^p}-\frac{\rho c(2+w_i^2)}2,\qquad\frac{db}{dt}=\sum_{i=1}^N\frac{w_i}{\tau^p}-c.\tag{4.20}$$
Here $w_i\in\mathbb R$ ($i=1..N$) are window sizes, $b\in\mathbb R$ is the buffer size, $\rho$ sets the drop rate and $c$ is the link capacity. Substituting $\tau^p$:
$$\frac{dw_i}{dt}=\frac cb-\rho c\Big(1+\frac{w_i^2}2\Big),\qquad\frac{db}{dt}=\sum_{i=1}^N\frac{cw_i}b-c.\tag{4.21}$$
(p. 4-16).

*Equilibrium.* Set $\dot w_i=\dot b=0$. By symmetry all $w_i$ are equal, and the author says there is a unique equilibrium:
$$w_{i,e}=\frac{b_e}N=\frac{c\tau^p_e}N,\qquad\frac1{2\rho^2N^2}(\rho b_e)^3+(\rho b_e)-1=0.\tag{4.22}$$
(Added step: from $\dot w=0$, $1/b=\rho(1+w^2/2)$; with $w=b/N$ this gives $1=\rho b+\rho b^3/(2N^2)$, which is the cubic.) It is solved numerically; $\rho b_e$ as a function of $1/(2\rho^2N^2)$ is plotted in Fig. 4.12b. Further equalities:
$$\tau^p_e=\frac{b_e}c=\frac{Nw_e}c,\quad q_e=Np_e=N\rho b_e,\quad r_e=\frac{w_e}{\tau^p_e}.\tag{4.23}$$
(p. 4-16).

*Simulation (Fig. 4.13).* 60 sources start at random window sizes; 20 drop out at $t=500$ ms and the others raise their rates. Buffer and window sizes adjust automatically to match the link capacity (p. 4-17).

*Intuition note.* Each computer grows its window while packets get through and halves it after a loss. Because the loss probability grows with the shared buffer, the model has a unique equilibrium, and in the simulation buffer and window sizes adjust to match the link capacity.

### 4.5 Atomic force microscopy
**Principle.** The scanning tunneling microscope (1986 Nobel Prize to Binnig and Rohrer) stimulated a family of instruments including the atomic force microscope (AFM), where a sample is probed by a tip on a cantilever (p. 4-17). In tapping mode the cantilever vibrates and the amplitude is controlled by feedback. In contact mode its bending is controlled. In both cases a piezo element actuates the vertical position of the cantilever base or the sample. Control design directly affects picture quality and scanning rate (p. 4-17, p. 4-18). The tip radius is of order 10 nm. The tilt of the cantilever is measured by a laser beam and photodiode. A controller drives the vertical position $z$ so that the deflection stays constant, so the signal driving the piezo measures the atomic forces (Fig. 4.14a, p. 4-18).

**Block diagram (Fig. 4.15).** Accessible signals: amplifier input $u$, piezo voltage $v$, photodiode-amplifier output $y$. The controller is a PI controller implemented on a computer with A/D and D/A converters. The deflection is $\varphi$ (p. 4-18). Horizontal motion is typically modelled as a low-damping spring–mass system. Vertical motion is more complicated (p. 4-18).

**Experiment and model (p. 4-19, p. 4-20).** The system is a high-performance design from [SÅD+07] in which the cantilever base is positioned by a piezo stack. The measured step response from $u$ to $y$ (Fig. 4.16a) shows a fast response with a poorly damped oscillation of period about 35 µs. The cantilever's natural frequency (several hundred kHz) is much higher than the observed oscillation of about 30 kHz, so the cantilever, amplifier and photodiode are modelled as static. The piezo with suspension is two masses $m_1,m_2$ separated by an ideal piezo element generating force $F$, with spring $k_2$ and damping $c_2$ on $m_2$ (Fig. 4.16b):
$$m_1\ddot z_1=F,\qquad m_2\ddot z_2=-c_2\dot z_2-k_2z_2-F .$$
Take $l=z_1-z_2$ as control variable and $z_1$ as output. Eliminating $F$ (add the equations) and substituting $z_2=z_1-l$ gives
$$(m_1+m_2)\frac{d^2z_1}{dt^2}+c_2\frac{dz_1}{dt}+k_2z_1=m_2\frac{d^2l}{dt^2}+c_2\frac{dl}{dt}+k_2l.\tag{4.24}$$
With the static relations $l=k_3u$ and $y=k_4z_1$, this is a complete model from $u$ to $y$ (p. 4-20). Its validity: up to the frequencies of the fastest modelled modes, and over a range of motion where linearized stiffness is adequate (p. 4-20).

**Interpretation.** When voltage is applied the piezo expands by $l_0$, $m_1$ moves up and $m_2$ moves down instantaneously. The system then settles after a poorly damped oscillation (p. 4-20). The designer may accept the oscillation with a slow response, design a controller that damps it, or redesign the mechanics for higher-frequency resonances. The last two give faster response and imaging. Tuning of the loop is currently manual in simple systems (p. 4-20).

*Intuition note.* Two masses joined by an expanding crystal behave like a poorly damped spring–mass system. That qualitatively explains the ringing in the step response, without modelling the electronics in detail.

### 4.6 Drug administration
**Open-loop dosing.** "Take two pills three times a day" is a solution of an open-loop control problem: quantized (two pills) and sampled (every 8 hours). Prescriptions rest on simple models in empirical tables, with dose based on age and weight (p. 4-21). Understanding how a drug spreads is called pharmacokinetics. Compartment models go back to Widmark's alcohol model in the 1920s (Fig. 4.17: perfect mixing in each compartment; flows proportional to concentration differences) (p. 4-21).

**Effect.** The effect $e$ of concentration $c$ is typically nonlinear:
$$e=\frac{c}{EC_{50}+c}\,e_{max}.\tag{4.25}$$
It is linear at low concentrations and saturates at high ones. $EC_{50}$ is the concentration giving half the maximal response. A dynamic relation is called pharmacodynamics (p. 4-22).

**One compartment.** With concentration $c$, volume $V$ and outflow rate $q$:
$$V\frac{dc}{dt}=-qc,\quad c\ge0.\tag{4.26}$$
The solution is $c(t)=c_0e^{-qt/V}=c_0e^{-kt}$, an exponential decay with time constant $T=V/q$. The input enters as the initial condition; more generally it can be a mass flow into the compartment (injection, or a dissolving pill). $k=q/V$ is the elimination rate constant. Extrapolating measurements back to $c_0$ gives the volume $V=m/c_0$ if the injected amount $m$ is known (p. 4-22).

**Two compartments (Fig. 4.18a).** A drug of concentration $c_0$ is injected into compartment 1 at volume flow rate $u$. The output is $c_2$. The flow between compartments is $q$, and $q_0$ is the outflow from compartment 1 not going to compartment 2:
$$V_1\frac{dc_1}{dt}=q(c_2-c_1)-q_0c_1+c_0u,\quad V_2\frac{dc_2}{dt}=q(c_1-c_2),\quad y=c_2,\quad c_1,c_2\ge0.\tag{4.27}$$
With $k_0=q_0/V_1$, $k_1=q/V_1$, $k_2=q/V_2$, $b_0=c_0/V_1$ (shapes: $c\in\mathbb R^2$, $A$ is $2\times2$, $B$ is $2\times1$, $C$ is $1\times2$):
$$\frac{dc}{dt}=\begin{pmatrix}-k_0-k_1&k_1\\k_2&-k_2\end{pmatrix}c+\begin{pmatrix}b_0\\0\end{pmatrix}u,\qquad y=\begin{pmatrix}0&1\end{pmatrix}c.\tag{4.28}$$
The matrix form can be written by inspection of the diagram (p. 4-23). Fig. 4.18b shows a six-compartment thyroid-hormone model, with $k_{ij}$ the transport from compartment $j$ to $i$ (p. 4-23). Such models have limited validity: the body changes slowly with time, averages hide rapid changes, and there are nonlinear transport effects. Variables like concentration and mass are always positive, and choosing the compartments is an essential difficulty (p. 4-23).

**Insulin–glucose dynamics.** The pancreas secretes insulin and glucagon. Glucagon is released when glucose is low and acts on the liver to release glucose. Insulin is secreted when glucose is high and lowers glucose by making liver and other cells take up more (p. 4-24). Diabetes is impaired production of insulin (type 1) or reduced ability to absorb it (type 2). Long exposure to high blood sugar is serious, and so are low levels (p. 4-24, p. 4-25). Models are tested on intravenous glucose-injection experiments (Fig. 4.19c) (p. 4-25).

The Bergman minimal model has two states: plasma glucose $G$ and $X$, the effect of insulin on glucose removal (proportional to interstitial insulin $I$, as the author states):
$$\frac{dG}{dt}=-p_1(G-G_e)-XG+u_G,\qquad\frac{dX}{dt}=-p_2X+p_3(I-I_e).\tag{4.29}$$
The first equation has a linear clearance term, the nonlinear term $XG$ (insulin enhances glucose removal) and the injection $u_G$. With $u_G=0$ and $I=I_e$, there is an equilibrium $G=G_e$, $X=0$ (p. 4-25). A fit of a slightly richer model to an injection test on a normal person shows a rapid glucose rise, a spike-like insulin response, then a gradual approach to equilibrium (p. 4-25). Exercise 4.8 gives a three-state model that includes insulin dynamics (p. 4-25).

**Devices.** A University of Virginia type-1 diabetes model was approved by the FDA as a replacement for animal testing of closed-loop strategies ("in silico testing"). A continuous glucose monitor senses interstitial glucose and needs calibration. An artificial pancreas combines a glucose monitor, insulin pump and control algorithm. The Medtronic MiniMed 670G (FDA-approved 2016 for adults, 2018 for children over seven) samples every 5 minutes and uses a PID algorithm. Similar devices with model predictive control have been tested. Safety demands are extreme, and it is essential to avoid hypoglycemia (p. 4-25, p. 4-26).

*Intuition note.* A compartment model is a set of stirred tanks with flows proportional to concentration differences. Each arrow in the diagram becomes one rate constant in the matrix, which is why the matrix can be written by inspection.

### 4.7 Population dynamics
**Logistic growth.** With birth rate $b$ and mortality $d$:
$$\frac{dx}{dt}=bx-dx=(b-d)x=rx,\ x\ge0.\tag{4.30}$$
It gives exponential increase if $b>d$ and decrease if $b<d$. A more realistic model lets the birth rate fall when the population is large; with carrying capacity $k$:
$$\frac{dx}{dt}=rx\Big(1-\frac xk\Big),\ x\ge0.\tag{4.31}$$
(p. 4-26).

**Predator–prey.** With $H$ hares (prey) and $L$ lynxes (predator), replacing the difference-equation model of Example 3.4:
$$\frac{dH}{dt}=rH\Big(1-\frac Hk\Big)-\frac{aHL}{c+H},\qquad\frac{dL}{dt}=b\frac{aHL}{c+H}-dL.\tag{4.32}$$
Here $r$ is the hare growth rate, $k$ their maximum population without lynxes, $a$ the interaction term and $c$ controls prey consumption at low hare population. $b$ is the lynx growth coefficient and $d$ the lynx mortality (p. 4-27).

**Equilibria** (setting the right-hand sides to zero). From the second equation:
$$L_e=0\ \text{ or }\ H_e^*=\frac{cd}{ab-d}.\tag{4.33}$$
For $L_e=0$ the first equation gives $H_e=0$ or $H_e=k$. For $L_e\ne0$:
$$L_e^*=\frac{rH_e(c+H_e)}{aH_e}\Big(1-\frac{H_e}k\Big)=\frac{bcr(abk-cd-dk)}{(ab-d)^2k}.\tag{4.34}$$
(Added step: $c+H_e^*=abc/(ab-d)$ and $1-H_e^*/k=(abk-cd-dk)/(k(ab-d))$.) There are three possible equilibrium points: $(0,0)$, $(k,0)$ and $(H_e^*,L_e^*)$. They may be negative for some parameters, which makes them unachievable (p. 4-27).

**Simulation (Fig. 4.20).** Parameters $a=3.2$, $b=0.6$, $c=50$, $d=0.56$, $k=125$, $r=1.6$. Starting near the nonzero equilibrium, both populations oscillate, reminiscent of Fig. 3.7. The caption calls the oscillation a limit cycle (p. 4-27, p. 4-28).

*Intuition note.* Setting the rates to zero turns a dynamics problem into algebra. Here it yields the empty system, hares at carrying capacity with no lynxes, and a coexistence state whose values $H_e^*,L_e^*$ may be negative (unachievable) for some parameters.

### Exercises (listed on pp. 4-28 to 4-31; no solutions printed in the unit)
See the "Exercises worth doing" section below.

## Toy example (our own, not from the text)
Apply the §4.6 recipe to a two-compartment model. Take $V_1=2$ L, $V_2=4$ L, $q=1$ L/min, $q_0=0.5$ L/min and injected concentration $c_0=10$ mg/L.

- Rates: $k_0=q_0/V_1=0.25$, $k_1=q/V_1=0.5$, $k_2=q/V_2=0.25$, $b_0=c_0/V_1=5$.
- Matrix (4.28): $A=\begin{pmatrix}-0.75&0.5\\0.25&-0.25\end{pmatrix}$, $B=\begin{pmatrix}5\\0\end{pmatrix}$, $C=(0\ 1)$.
- Check at $c=(4,2)^T$ mg/L with $u=0$: $\dot c_1=-0.75(4)+0.5(2)=-3+1=-2$ and $\dot c_2=0.25(4)-0.25(2)=1-0.5=0.5$ mg/L per min.
- Check against the mass balances (4.27): $V_1\dot c_1=1(2-4)-0.5(4)=-4$, so $\dot c_1=-2$ ✓. $V_2\dot c_2=1(4-2)=2$, so $\dot c_2=0.5$ ✓.
- Total drug mass changes at $V_1\dot c_1+V_2\dot c_2=2(-2)+4(0.5)=-2$ mg/min. This equals $-q_0c_1=-0.5\cdot4$ ✓. Mass leaves only through $q_0$.

The state is $(c_1,c_2)$, the input is $u$ and the output is $c_2$. Each arrow in the diagram became one coefficient, as the chapter says.

## Concepts
- [[state]] — the quantities whose values determine future behaviour; here $v$ (car), $(\varphi,\dot\varphi)$ (bicycle), $(x_{cpu},x_{mem})$, concentrations, populations (p. 4-3, p. 4-13, p. 4-23)
- [[state-space-model]] — dynamics written as vector equations with matrices, e.g. (4.16) and (4.28) (p. 4-13, p. 4-23)
- [[feedback]] — measured output used to adjust input; here also built into mechanics (bicycle fork) and circuits (p. 4-7, p. 4-10)
- [[negative-feedback]] — the op-amp circuit feeds a fraction of the output back against the input, giving a stable amplifier (Fig. 4.9 caption, p. 4-9)
- [[pid-control]] — mostly the PI form: cruise control (4.4), the op-amp circuit, the AFM controller; the MiniMed 670G uses a PID algorithm (p. 4-4, p. 4-11, p. 4-18, p. 4-26)
- [[integral-action]] — the integrator drives steady-state error to zero despite disturbances and model errors (p. 4-4)
- [[robustness]] — closed-loop op-amp gain is insensitive to the open-loop gain $k$; an imperfect model can still be used for design (p. 4-5, p. 4-10)
- [[linearization]] — the web-server model is linear around an equilibrium; $\sin\varphi\approx\varphi$ for the bicycle (p. 4-7, p. 4-13)
- [[delay-dead-time]] — round-trip and forward/backward delays in the congestion model (4.17)–(4.19) (p. 4-15, p. 4-16)
- [[open-loop-vs-closed-loop]] — "two pills three times a day" is open loop (p. 4-21)
- [[homeostasis]] — healthy regulation of blood glucose in the range the author gives, 70–110 mg/L (as printed) (p. 4-24)
- [[disturbance-and-noise]] — road slope as $F_d$ (p. 4-3)
- [[reference-set-point]] — $v_r$ for speed, a deflection reference for the AFM (p. 4-1, p. 4-18)
- [[compartment-model]] (new) — body or system split into perfectly mixed compartments with flows proportional to concentration differences (p. 4-21)
- [[uncertainty-lemon]] (new) — the author's picture (Fig. 3.5b) of the range of inputs and frequencies where a model is valid (p. 4-4)
- [[equilibrium-point]] (new) — constant state found by setting the derivatives to zero (p. 4-16, p. 4-27)
- [[finite-state-machine]] (new) — discrete-mode logic, e.g. Off/Standby/Cruise/Hold (p. 4-5)
- [[saturation]] (new) — output clipped to $[v_{min},v_{max}]$ in (4.9)–(4.10) (p. 4-8)
- [[logistic-growth]] (new) — growth that slows toward carrying capacity $k$ (4.31) (p. 4-26)
- [[limit-cycle]] (new) — the oscillation in the predator–prey simulation (caption of Fig. 4.20) (p. 4-28)

## Canonical instances
- [[cruise-control]] — first-order nonlinear plant with PI feedback; hill response (p. 4-3, p. 4-4)
- [[bicycle-dynamics]] — inverted-pendulum-like frame plus fork feedback; Whipple model (p. 4-6, p. 4-7)
- [[op-amp-feedback-amplifier]] — gain set by resistors, low sensitivity to $k$ (p. 4-10)
- [[web-server-control]] — identified linear discrete-time model with `KeepAlive` and `MaxClients` (p. 4-13)
- [[internet-congestion-control]] — TCP/Reno window, router queue and drop-probability model (p. 4-15, p. 4-16)
- [[atomic-force-microscope]] — two-mass piezo model of the oscillatory vertical positioner (p. 4-19, p. 4-20)
- [[drug-compartment-models]] — one- and two-compartment drug distribution (p. 4-22, p. 4-23)
- [[insulin-glucose-minimal-model]] — Bergman model (4.29) (p. 4-25)
- [[artificial-pancreas]] — closed-loop insulin delivery with monitor, pump and PID (p. 4-26)
- [[predator-prey-lynx-hare]] — equilibria (4.33)–(4.34) and oscillating simulation (p. 4-27, p. 4-28)

## Bridges (candidates)
- [structural-analogy] Op-amp closed-loop gain (4.14) ↔ control theory: sensitivity reduction by high loop gain — high open-loop gain bought low sensitivity; the chapter shows the effect, with the formal tool left to later chapters.
- [same-math] PI controller as a controller state $z$ with $\dot z=v_r-v$ (4.4) ↔ op-amp PI circuit (p. 4-11) — both realize a PI law (the op-amp circuit with an inversion sign).
- [structural-analogy] TCP window halving on loss and growth otherwise ↔ negative feedback with quantized actions — the window shrinks when the congestion signal appears.
- [same-math] Two-compartment drug model (4.28) ↔ any linear state-space model $\dot x=Ax+Bu$, $y=Cx$ — literally the same matrix form.
- [structural-analogy] Predator–prey oscillation ↔ the damped-oscillation modes of spring–mass systems — both give oscillating time responses, but the predator–prey system is nonlinear and the chapter calls its oscillation a limit cycle.
- [metaphor] Glucose regulation by insulin/glucagon ↔ thermostat-type regulation — both hold a variable in a range by opposing deviations.

## Questions this raises
- How can the bicycle's threshold speed $\sqrt{gb/k_2}$ be checked against the more detailed Whipple model (4.8)?
- When is the one-line Ohm's-law model (4.12) enough, and when must the dynamic model (4.15) be used?
- How does the congestion equilibrium (4.22) change with $N$, and are the dynamics (4.21) stable near it?
- How can the PI parameters $k_p,k_i$ in (4.4) be chosen so that the hill response meets a specification (Chapter 11, as the author says)?

## Exercises worth doing
- Ex. 4.1 (p. 4-28) — simulate the cruise-control hill response with mass changed by ±25% and redesign the PI controller to return within 1% in 3 s — difficulty: medium
- Ex. 4.2 (p. 4-28) — put the frame model (4.5) in state-space form and interpret the states — difficulty: easy
- Ex. 4.3 and 4.4 (pp. 4-28 to 4-29) — derive state-space models of op-amp circuits (a circuit with two capacitors, and an oscillator) — difficulty: medium
- Ex. 4.5 (p. 4-29) — extend the congestion model with RED and find parameters giving a stable equilibrium versus oscillation — difficulty: hard
- Ex. 4.7 (p. 4-30) — simulate the nonlinear compartment model of alcohol for oral and intravenous doses — difficulty: medium
- Ex. 4.9 (p. 4-31) — find the sustainable fishery equilibrium and simulate over-fishing to discuss quotas — difficulty: medium

## Reading notes
- Page labels show no printed number, but the page images show running numbers "4-N". Printed page 4-N equals pdf page 120+N (pdf 121 = 4-1, pdf 152 = 4-32). Citations use "p. 4-N". The unit metadata asked for pdf references; add 120 to convert.
- Cruise control: the text says the interface has four buttons (on-off, set/decelerate, resume/accelerate, cancel); the Fig. 4.4 caption lists five buttons (on, off, set, resume, cancel) (p. 4-5).
- Cruise control: the text says the throttle goes "from 0.17 to almost full throttle". Fig. 4.3b shows $u$ rising to about 0.7–0.8 (p. 4-4).
- Congestion model: (4.19) is printed as $1-\prod R_{li}(1-p_l)$ with the sum starting at $l=0$. With $R_{li}\in\{0,1\}$, an index starting at 1 and a power $(1-p_l)^{R_{li}}$ would be expected. I report it as printed. In (4.23), $q_e=N\rho b_e$: reducing (4.17) to (4.20) with $q_i=\rho b$ reproduces (4.20), so the factor $N$ looks inconsistent with (4.20). This is my observation, not the author's.
- Predator–prey: the text defines $x_e=(L_e,H_e)$, but the listed vectors $(k,0)$ and $(H_e^*,L_e^*)$ have $H$ first, so the order is $(H,L)$ (p. 4-27).
- Glucose range is printed as "70–110 mg/L", while Fig. 4.19c uses mg/dl. "GCM" is printed for a continuous glucose monitor (p. 4-24, p. 4-25).
- Ex. 4.8 lists a parameter $p_7=199$ that does not appear in the model equations (p. 4-31). pdf 152 contains only a running header.
- The page-4-13 text says the "first column of $B$" is `KeepAlive`, consistent with the input order $(u_{ka},u_{mc})$ in (4.16).
- Matrices in (4.8), (4.16) and (4.28) were checked against the page images. No equation was unreadable.
