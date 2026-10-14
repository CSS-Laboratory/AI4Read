---
id: astrom-2021-feedbacksystems/ch03-system-p2
work: astrom-2021-feedbacksystems
unit: "3 System Modeling (part 2/2): end of 3.2, 3.3 Modeling Methodology, 3.4 Modeling Examples, 3.5 Further Reading, Exercises"
pages: 3-22 to 3-48
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
# System Modeling, part 2: methodology and a gallery of examples

## L0 — One line
A few tools (block diagrams, experiments, scaling, differential-equation models) let you build and simplify models of very different systems, and the right level of detail often depends on experience and on the question asked.

## L1 — The gist (≤ 120 words)
How do we build, simplify and use models of dynamical systems? This part finishes the Lyapunov (energy-function stability) and frequency-response (steady sinusoidal output) examples, then presents block diagrams, algebraic loops, fitting models to step-response experiments, and scaling to dimension-free variables. A gallery of examples follows: vehicle steering, a vectored thrust aircraft, a water heater, a drum boiler with inverse response, queues, memory paging, sensor-network consensus (agents agreeing on an average), gene regulation and neurons. The examples span many fields. The author notes that the level of detail of the blocks in a block diagram often depends on experience and on the questions to be answered.

**Prerequisites:** ordinary differential equations; first-order and second-order (spring–mass) systems; matrices and vectors; basic logarithms and sinusoids; the state-space form $\dot x = f(x,u)$ from earlier in the chapter.

## L2 — Key ideas (5–10 bullets)
- **Stability by an energy-like function.** If $V$ never increases and can stop decreasing only at the origin, the spring–mass origin is stable for any initial condition (p. 3-22).
- **Frequency response.** For the spring–mass system, the author says (to be proved in Chapter 6) that the long-term response to a sinusoidal input is a sinusoid at the same frequency, with gain $g(\omega)$ (amplitude ratio) and phase $\varphi(\omega)$ (shift). For linear systems these do not depend on the input amplitude (p. 3-22).
- **Block diagrams show information flow and hide detail.** The fly flight example uses five blocks. How much to hide often depends on experience and on the question asked (pp. 3-23, 3-25, 3-26).
- **Algebraic loops.** A loop in which every block has a direct input-to-output connection forces you to solve algebraic equations before you get a differential equation. Most block-diagram modeling languages cannot handle such loops and only report that they are present (p. 3-26).
- **Models from experiments.** A step response gives parameters. For the spring–mass system the steady state, oscillation period and decay of peaks give $k$, $m$ and $c$ (pp. 3-27, 3-28).
- **Scaling.** Dimension-free variables cut the number of parameters: 2 → 0 for the spring–mass system, 5 → 2 for the balance system (pp. 3-28, 3-29).
- **Differential and difference equation models fit many fields.** Examples: steering kinematics, thrust-vectored aircraft, thermofluid balances, flow models of queues, discrete feedback in paging, consensus (agents agreeing on a common value) on graphs, gene circuits, neurons (pp. 3-30 to 3-43).
- **Some behavior is counter-intuitive.** The drum level first rises when steam flow rises (inverse response). Queue length grows sharply as $\lambda\to\mu_{\max}$ (pp. 3-34, 3-36).

## L3 — Walkthrough

### 3.2 (end of section): Lyapunov argument and frequency response

**Lyapunov argument, concluded (p. 3-22).** This continues the spring–mass analysis begun in part 1; the function $V$ and equation (3.18) are not in these pages. The author states that $\dot V \le 0$.
1. Suppose $V(x(t))$ stops decreasing for some period. Then $\dot V = 0$, which implies $x_2(t)=0$ in that period.
2. Then $\dot x_2 = 0$. Substituting into the second line of (3.18):
$$0=\dot x_2 = -\frac{c}{m}x_2-\frac{k}{m}x_1=-\frac{k}{m}x_1 .$$
3. So $x_1=0$ as well. The only time $V$ can stop decreasing is at the origin (the rest position).
4. Since $V$ never increases, the author concludes the origin is stable for any initial condition. He calls this *Lyapunov stability analysis* and says Chapter 5 treats it in detail.

> *Intuition note.* If an energy-like quantity can only go down, and it can stay still only at rest, the origin is stable (the page's conclusion; convergence is not claimed here). The argument never solves the differential equation.

**Frequency response (p. 3-22).** The system is $m\ddot q+c\dot q+kq=u$ (3.20), with input $u(t)=A\sin\omega t$.
- If $q(t)$ solves (3.20) for $u(t)$, then $2q(t)$ solves it for $2u(t)$ ("easily verified by substitution"). So it suffices to take $A=1$.
- The author says he will prove in Chapter 6 that the long-term response is a sinusoid at the same frequency:
$$q(t)=g(\omega)\sin(\omega t+\varphi(\omega)).$$
Here $g(\omega)$ is the *gain* and $\varphi(\omega)$ the *phase* (phase offset).
- Numerically, simulate at frequencies $\omega_1,\dots,\omega_N$ and plot gain and phase. Fig. 3.12 shows gain only: time responses on the left, the same data as gain versus frequency (log scales) on the right (p. 3-23).
- For linear systems the frequency response does not depend on $A$. For nonlinear systems gain and phase then depend on $A$ (p. 3-22).

> *Intuition note.* "Gain" here means the amplitude ratio output/input at one frequency. Do not confuse it with a controller gain. Linearity is what lets one unit-size test stand for all sizes.

### 3.3 Modeling Methodology

**Schematic diagrams (p. 3-23).** These range from stylistic pictures to simplified standard symbols. They show subprocesses, their interconnection, the variables that can be manipulated and the signals that can be measured. Fig. 3.13 gives four disciplines: power systems, a cell-biology circuit, a distillation column, and a Petri net of a communication protocol (p. 3-24).

**Block diagrams (pp. 3-23, 3-24).**
- A block diagram emphasizes information flow and hides details. Boxes are process elements. Arrows into a box are inputs (variables that influence the process); arrows out are outputs (signals of interest or signals that drive other subsystems). Blocks can be nested in hierarchies.
- Fig. 3.14 gives the standard elements: summing junction, gain block ($u\mapsto ku$), saturation, nonlinear map $f(u)$, integrator ($\int_0^t u\,dt$), and a general input/output system block.

**Example: fly flight control (Fig. 3.15, pp. 3-25, 3-26).**
- Flies can fly upwind by using optical flow in their compound eyes as feedback. Roughly, the fly controls its orientation so that the point of contraction of the visual field is centered (p. 3-25).
- Five blocks: (a) sensory motor system, (b) wing aerodynamics, (c) body dynamics, (d) drag aerodynamics (the wind enters here), (e) vision system.
- The sensory motor system takes vision output and produces muscle commands. The wings turn commands into forces. These combine with drag into a net force on the body. Body position, speed and orientation feed back to drag and vision, which closes the loop (p. 3-25).
- Each block can itself be complicated: about 700 elements per eye, about 200,000 neurons in the sensory motor system. The level of detail "often depends on experience and on the questions that one wants to answer" (pp. 3-25, 3-26).

> *Intuition note.* A block diagram is a map, not the territory. You choose which details to fold into a box, and a good choice depends on what you want to learn.

**Algebraic loops (p. 3-26).**
- To simulate a block diagram we need differential equations for the whole system. Simple substitution fails when a closed loop of subsystems all have a *direct connection* (a change in input $u$ gives an instantaneous change in output $y$). Such a loop is an *algebraic loop*.
- No direct connection: $\dot x=f(x,u),\; y=h(x)$ (3.21), with $u=-ky$. Substituting gives the ordinary differential equation $\dot x=f(x,-kh(x))$, $y=h(x)$.
- Direct connection: $y=h(x,u)$ with $u=-ky$ gives $\dot x=f(x,-ky)$, $y=h(x,-ky)$. The algebraic equation $y=h(x,-ky)$ must first be solved for $y=\alpha(x)$, which "in general is a complicated task".
- The result is a set of differential algebraic equations (like (3.4)). Resolving them needs symbolic solution of algebraic equations.
- Most block-diagram modeling languages cannot do this and only report that loops exist. In analog computing, loops were removed by inserting fast dynamics, which created fast and slow modes that are hard to solve numerically. Modelica uses several sophisticated methods.

**Modeling from experiments (p. 3-27).**
- With sensors and actuators one can get input/output models from experiments. This can be combined with physics-based modeling through feedback and interconnection.
- *Step response* experiment: hold the input constant until a stable system's output settles, change the input quickly to a new level, and observe. The shape indicates the response time and whether the response is oscillatory or monotone.

**Example 3.8, spring–mass system (pp. 3-27, 3-28).** The system is $m\ddot q+c\dot q+kq=u$ (3.22). The goal is to find $m,c,k$ from a step of size $F_0$.
- Author's formula (to be shown in Chapter 7), for $c^2<4km$, from rest:
$$q(t)=\frac{F_0}{k}\left(1-\frac{1}{\omega_d}\sqrt{\frac km}\,e^{-ct/2m}\sin(\omega_d t+\varphi)\right),$$
$$\omega_d=\frac{\sqrt{4km-c^2}}{2m},\qquad \varphi=\tan^{-1}\!\left(\frac{\sqrt{4km-c^2}}{c}\right).$$
- Three measurements on Fig. 3.16 (step $F_0=20$ N):
  - Steady state: $q(\infty)=F_0/k$ (3.23). The parameter $1/k$ is called the gain of the system (for a unit step).
  - Period $T$ between two peaks: $\dfrac{2\pi}{T}=\dfrac{\sqrt{4km-c^2}}{2m}$.
  - Decay between two peaks:
$$\log\!\Big(q(t_1)-\frac{F_0}{k}\Big)-\log\!\Big(q(t_2)-\frac{F_0}{k}\Big)=\frac{c}{2m}(t_2-t_1)\tag{3.24}$$
- Solving the three equations gives $m\approx250$ kg, $c\approx60$ N s/m, $k\approx40$ N/m (p. 3-28).

> *Intuition note.* Each measurable feature of the curve (final level, ringing speed, ringing decay) pins down one combination of parameters. Three features, three unknowns.

**Other experiments (p. 3-28).**
- Sinusoidal signals are common, especially for fast dynamics; correlation techniques give precise measurements.
- Repeating experiments with different amplitudes gives an indication of nonlinearities.
- Sinusoidal experiments are very time consuming for slow dynamics. There, signals that switch between two levels are advantageous.
- *System identification* is the control subfield on experimental determination of models. It treats optimal inputs, open- versus closed-loop experiments, model accuracy and fundamental limits.

**Normalization and scaling (pp. 3-28, 3-29).**
- Dimension-free variables can reduce the number of parameters and reveal properties of the model. Scaling also improves numerics. Procedure: choose a unit for each variable and divide by it.

**Example 3.9, undamped spring–mass (pp. 3-28, 3-29).** The system is $m\ddot q+kq=u$ with parameters $m,k$.
1. Let $x=q/l$, $\tau=\omega_0 t$, $\omega_0=\sqrt{k/m}$, with $l$ a chosen length. Scale force by $ml\omega_0^2$: $v=u/(ml\omega_0^2)$.
2. Then
$$\frac{d^2x}{d\tau^2}=\frac{d^2q/l}{d(\omega_0t)^2}=\frac{1}{ml\omega_0^2}(-kq+u)=-x+v .$$
The normalized model has no parameters (the original had two).
3. With $z_1=x=q/l$, $z_2=dx/d\tau=\dot q/(l\omega_0)$:
$$\frac{d}{d\tau}\begin{pmatrix}z_1\\z_2\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}z_1\\z_2\end{pmatrix}+\begin{pmatrix}0\\v\end{pmatrix}.$$
This describes any spring–mass system. To recover physical frequency or magnitude, one must invert the scaling.

**Example 3.10, balance system (p. 3-29).** Set $c=0$, $\gamma=0$ in (3.9) (Example 3.2 is in part 1):
$$(M+m)\ddot q-ml\cos\theta\,\ddot\theta+ml\sin\theta\,\dot\theta^2=F,\qquad -ml\cos\theta\,\ddot q+(J+ml^2)\ddot\theta-mgl\sin\theta=0 .$$
- Let $\omega_0=\sqrt{mgl/(J+ml^2)}$, length scale $l$, time scale $1/\omega_0$, force scale $(M+m)l\omega_0^2$. Then $\tau=\omega_0t$, $x=q/l$, $u=F/((M+m)l\omega_0^2)$.
- The scaled equations:
$$\frac{d^2x}{d\tau^2}-\alpha\cos\theta\frac{d^2\theta}{d\tau^2}+\alpha\sin\theta\Big(\frac{d\theta}{d\tau}\Big)^2=u,\qquad -\beta\cos\theta\frac{d^2x}{d\tau^2}+\frac{d^2\theta}{d\tau^2}-\sin\theta=0,$$
with $\alpha=m/(M+m)$ and $\beta=ml^2/(J+ml^2)$.
- Five parameters ($m,M,J,l,g$) become two ($\alpha,\beta$).
- If $M\gg m$ and $ml^2\gg J$, then $\alpha\approx0$, $\beta\approx1$, and
$$\frac{d^2x}{d\tau^2}=u,\qquad \frac{d^2\theta}{d\tau^2}-\sin\theta=u\cos\theta,$$
a mass combined with an inverted pendulum driven by the same input.
- For large systems scaling is not easy; it needs understanding of the physics and of the numerical methods. It "is therefore still an art" (p. 3-29).

> *Intuition note.* Scaling asks: in what natural units does this system look the same no matter its size? What is left (here $\alpha,\beta$) are the dimension-free parameters of the scaled model.

### 3.4 Modeling Examples (p. 3-30)
The section gives examples from many fields. Chapter 4 gives a more detailed set of running applications.

**Motion control: Example 3.11, vehicle steering (pp. 3-30, 3-31).**
- Setup: a vehicle with fixed rear axle and steerable front wheels. $b$ is the wheelbase, $a$ the distance from the rear wheel to the center of mass, $\delta$ the steering angle, $\theta$ the heading, $(x,y)$ the center of mass, and $\alpha$ the angle between the velocity $v$ and the vehicle centerline. $O$ is where the normals to the front and rear wheels meet.
- With no wheel slip, motion is rotation about $O$. With $r_r$ the distance from $O$ to the rear contact point, $b=r_r\tan\delta$ and $a=r_r\tan\alpha$, so $\tan\alpha=(a/b)\tan\delta$:
$$\alpha=\arctan\!\Big(\frac{a\tan\delta}{b}\Big)\tag{3.25}$$
$$\frac{dx}{dt}=v\cos(\alpha+\theta),\qquad \frac{dy}{dt}=v\sin(\alpha+\theta)\tag{3.26}$$
- The distance from the center of mass to $O$ is $r_c=a/\sin\alpha$, so the angular velocity is $v/r_c=(v/a)\sin\alpha$:
$$\frac{d\theta}{dt}=\frac{v}{r_c}=\frac{v\sin\alpha}{a}=\frac va\sin\!\Big(\arctan\frac{a\tan\delta}{b}\Big)\approx\frac vb\,\delta\tag{3.27}$$
The approximation holds for small $\delta$ and $\alpha$.
- Equations (3.25)–(3.27) form the *bicycle model*: no slip, and the two front wheels approximated by one. Slip can be added with an extra state. The author says such a model (with the extra state) also describes ship steering and aircraft and missile pitch dynamics. Choosing the reference point at the rear wheels ($a=0$) gives the *Dubins car*. Reversing the sign of $v$ covers rear-wheel steering (p. 3-31).

**Example 3.12, vectored thrust aircraft (pp. 3-31, 3-32).**
- The Harrier's thrust is modeled as forces $F_1$ (horizontal) and $F_2$ (vertical) acting at distance $r$ below the aircraft's center of mass, in a vertical plane. $(x,y,\theta)$ is the pose; $m$ mass, $J$ moment of inertia, $g$ gravity, $c$ damping.
$$m\ddot x=F_1\cos\theta-F_2\sin\theta-c\dot x,\quad m\ddot y=F_1\sin\theta+F_2\cos\theta-mg-c\dot y,\quad J\ddot\theta=rF_1\tag{3.28}$$
- With $u_1=F_1$, $u_2=F_2-mg$ the origin is an equilibrium at zero input:
$$m\ddot x=-mg\sin\theta-c\dot x+u_1\cos\theta-u_2\sin\theta,\quad m\ddot y=mg(\cos\theta-1)-c\dot y+u_1\sin\theta+u_2\cos\theta,\quad J\ddot\theta=ru_1\tag{3.29}$$
Three coupled second-order equations.

**Thermofluid systems (pp. 3-32, 3-33).** They are used in process control, power generation and heating, ventilation and air conditioning. Dynamics are often complicated by two-phase flow; accurate modeling often needs partial differential equations and computational fluid dynamics.

**Example 3.13, water heater (p. 3-33).**
- Tank with mass of water $m=\rho Ah$, temperature $T$, inflow/outflow rates $q_{in},q_{out}$, inflow temperature $T_{in}$, outflow temperature $T$, specific heat $C$, heater power $P$. Energy is $mCT$. Losses are neglected and all water in the tank is assumed to have the same temperature.
$$\frac{dm}{dt}=q_{in}-q_{out},\qquad \frac{d(mCT)}{dt}=P+q_{in}CT_{in}-q_{out}CT\tag{3.30}$$
- With $C$ constant: $\frac{d(mCT)}{dt}=\frac{dm}{dt}CT+mC\frac{dT}{dt}$. Solving for $dT/dt$ and eliminating $dm/dt$ gives
$$\frac{dm}{dt}=q_{in}-q_{out},\qquad \frac{dT}{dt}=\frac{q_{in}}{m}(T_{in}-T)+\frac{1}{mC}P\tag{3.31}$$
- (added step) Substituting $dm/dt=q_{in}-q_{out}$: $mC\,dT/dt=P+q_{in}CT_{in}-q_{out}CT-(q_{in}-q_{out})CT=P+q_{in}C(T_{in}-T)$; then divide by $mC$.
- States: $m$ and $T$. Inputs: $P$ and $q_{in}$. Disturbances: $T_{in}$ and $q_{out}$.

**Example 3.14, drum boiler (pp. 3-34, 3-35).**
- Like the water heater, but $\rho$ and $C$ depend on the state, and water and steam are mixed in the riser and the drum. Modeling is still by mass and energy balances; the two-phase flow adds complications.
- Drum-level control matters: too low and the tubes burn through; too high and water may enter the turbine. Self-circulation through drum–downcomer–riser is driven by density differences. The boiler discussed has 22 downcomer tubes, 788 riser tubes and a drum volume of 40 m³.
- **Shrink and swell (inverse response).**
  - If the steam valve is opened suddenly, one may expect the level to fall. Instead drum pressure falls, bubbles in riser and drum grow, and the level first rises. If the valve is kept open, the level finally starts to decrease.
  - Likewise, more feedwater lowers the drum temperature, bubbles collapse, and the level first decreases.
- Fig. 3.20 compares a fifth-order simulation model (mass, energy and momentum balances, details in [ÅB00]) with plant data for open-loop steam-flow perturbations at medium load. The experiment removed all controllers.
- The inverse response makes control hard. So the system has steam-flow and feedwater-flow sensors, which help predict whether the mass of water and steam is rising or falling. The consequences are discussed in Section 14.4 (p. 3-34).

> *Intuition note.* The level is not a pure measure of how much water is in the drum, because bubbles take up volume. Bubble growth can move the level the "wrong" way at first; if the valve is kept open the level finally decreases (p. 3-34). (The fast-versus-slow comparison is the digest's gloss, not stated in the text.)

**Example 3.15, queuing systems (pp. 3-35 to 3-37).**
- Requests arrive, queue and are served. The queue grows when arrivals exceed service. When the queue is too large, an admission control policy denies service.
- A discrete model tracks each request (integer state, random arrivals and services). The simpler *flow model* treats arrivals and services as continuous flows (rates $\lambda$ and $\mu$), as proposed by Agnew:
$$\frac{dx}{dt}=\lambda-\mu=\lambda-\mu_{\max}f(x),\quad x\ge0\tag{3.32}$$
- Without capacity limits $\mu=x/T$ ($T$ = time to serve one customer). In reality growth is slower and $\mu\le\mu_{\max}$. So $f$ is monotone, approximately linear for small $x$, and $f(\infty)=1$. $f$ can be found empirically. A simple choice $f(x)=x/(1+x)$ gives
$$\frac{dx}{dt}=\lambda-\mu_{\max}\frac{x}{x+1}\tag{3.33}$$
- Tipper showed that, if arrivals and services are Poisson processes, the average queue length is given by (3.33) (p. 3-36).
- Equilibrium: set $dx/dt=0$ in (3.33) for constant $\lambda$:
$$x_e=\frac{\lambda}{\mu_{\max}-\lambda}\tag{3.34}$$
- Queue length grows rapidly as $\lambda\to\mu_{\max}$; queue length below 20 requires $\lambda/\mu_{\max}<0.95$. The average service time can be shown to be $T_s=(x+1)/\mu_{\max}$, which increases dramatically as $\lambda\to\mu_{\max}$ (Fig. 3.22a).
- Overload (Fig. 3.22b): $\mu_{\max}=1$, $\lambda=0.5$, raised to 4 at $t=20$ and back to 0.5 at $t=25$. The queue builds up quickly and clears slowly. Since response time is proportional to queue length, service stays poor for a long time. This is the *rush-hour effect*.
- The flow model (dashed line in the figure) captures the average behavior qualitatively; individual samples vary when the queue is short.

> *Intuition note.* The text reports that after a temporary overload the queue builds up quickly and clears very slowly, so service stays poor for a long time (p. 3-36); it gives no mechanism on these pages.

**Example 3.16, virtual memory paging control (pp. 3-37, 3-38).**
- IBM 370 (OS/VS): virtual memory lets programs address more memory than the fast memory (RAM). Under overload, execution times became very long (open circles in Fig. 3.23a).
- Fix: a discrete feedback system. CPU load and the number of page swaps were measured, and the state was classified as normal (high CPU activity), underload (low CPU activity, few page replacements) or overload (moderate-to-low CPU load, many page replacements). Boundaries and measuring times were chosen from simulations.
- Control strategy: do nothing in normal; exclude a process from memory in overload; allow a new or previously excluded process in underload. Simulations (crosses in Fig. 3.23a) show the effectiveness. The author says similar crude-quantization, heuristic schemes are used in communication systems and web-server control.

**Example 3.17, consensus protocols in sensor networks (pp. 3-38, 3-39).**
- Problem: agents each hold a local number, communicate only with some neighbors (the network is *connected*: no two groups are completely isolated), and should all agree on the average.
- The network is a graph (nodes = sensors, edges = direct links). The adjacency matrix has a 1 where two nodes are connected. For Fig. 3.24a:
$$A=\begin{pmatrix}0&1&0&0&0\\1&0&1&1&1\\0&1&0&1&0\\0&1&1&0&0\\0&1&0&0&0\end{pmatrix},\quad \mathcal N_2=\{1,3,4,5\},\ \mathcal N_3=\{2,4\}.$$
- $x_i$ is the state of sensor $i$ (its estimate of the average), initialized to its measurement. The protocol is
$$x_i[k+1]=x_i[k]+\gamma\sum_{j\in\mathcal N_i}\big(x_j[k]-x_i[k]\big)\tag{3.35}$$
- Combined: $x[k+1]=x[k]-\gamma(D-A)x[k]$ (3.36). Here $A$ is the adjacency matrix and $D$ is diagonal with the number of neighbors of each node. $\gamma$ is the rate at which estimates are updated from neighbors. $L:=D-A$ is the *Laplacian* of the graph. (added step) For $N$ agents, $x[k]\in\mathbb R^N$ and $A,D,L\in\mathbb R^{N\times N}$; for Fig. 3.24a, $N=5$ and $D=\mathrm{diag}(1,4,2,2,1)$.
- Author's claims, stated without proof: if the network is connected, $x_e=(\alpha,\dots,\alpha)$ is an equilibrium; $\alpha$ is the average of the initial states; for any connected graph one can always find a $\gamma$ for which the states converge to the average. The author warns that cycles in the graph make an infinite loop conceivable. A formal analysis needs tools from later chapters. Fig. 3.24b shows a simulation.
- Other consensus states (maximum, minimum, node count, higher-order moments) can be obtained with other feedback laws (p. 3-39).

> *Intuition note.* Each agent moves a bit toward its neighbors' values. Because the update is symmetric across each link, the total is preserved, so the common value they settle on is the average. (This reasoning is the digest's gloss; the text states the result without proof.)

**Biological systems (p. 3-40).** Biology is called "perhaps the richest source" of feedback examples. Homeostasis (regulating a quantity such as temperature or blood sugar to a fixed value) is one of many types of feedback interaction.

**Example 3.18, transcriptional regulation (pp. 3-40, 3-41).**
- Transcription makes mRNA from DNA; transcription factors bind to the gene's promoter region and repress or activate RNA polymerase. The mRNA is translated into protein (Fig. 3.25).
- Repression of protein A (concentration $p_a$, mRNA $m_a$) by protein B ($p_b$), using a Hill function:
$$\frac{dm_a}{dt}=\frac{\alpha_{ab}}{1+k_{ab}p_b^{n_{ab}}}+\alpha_{a0}-\delta_am_a,\qquad \frac{dp_a}{dt}=\kappa_am_a-\gamma_ap_a\tag{3.37}$$
  - $\alpha_{ab}+\alpha_{a0}$ is the unregulated transcription rate.
  - $\delta_a$ is the mRNA degradation rate.
  - $\alpha_{ab},k_{ab},n_{ab}$ describe how B represses A.
  - $\kappa_a$ is the protein production rate from mRNA.
  - $\gamma_a$ is the protein degradation rate.
  - $\alpha_{a0}$ is the promoter's "leakiness".
  - $n_{ab}$ is the Hill coefficient, related to cooperativity.
- Activation:
$$\frac{dm_a}{dt}=\frac{\alpha_{ab}k_{ab}p_b^{n_{ab}}}{1+k_{ab}p_b^{n_{ab}}}+\alpha_{a0}-\delta_am_a,\qquad \frac{dp_a}{dt}=\kappa_am_a-\gamma_ap_a\tag{3.38}$$
For an activator with $p_b=0$ the production rate is $\alpha_{a0}\ll\alpha_{ab}$ (repressor: $\alpha_{ab}+\alpha_{a0}$). For large $p_b$ it becomes $\alpha_{ab}+\alpha_{a0}$ (repressor: $\alpha_{a0}$). So they act in opposite fashion.
- **Repressilator** (Elowitz and Leibler): three proteins, TetR, λ cI and LacI, each repress another in a cycle (Fig. 3.26a). Three copies of (3.37) give state $x=(m_{TetR},p_{TetR},m_{cI},p_{cI},m_{LacI},p_{LacI})$. Parameters in Fig. 3.26b: $n=2$, $\alpha=0.5$, $k=6.25\times10^{-4}$, $\alpha_0=5\times10^{-4}$, $\delta=5.8\times10^{-3}$, $\kappa=0.12$, $\gamma=1.2\times10^{-3}$; $x(0)=(1,200,0,0,0,0)$. "If the dynamics of the circuit are designed properly", the concentrations oscillate.

**Example 3.19, nerve cells (pp. 3-41 to 3-43).**
- Anatomy and facts given: neuron types (sensory, motor, interneurons); about 100 billion neurons in a human brain; three parts (soma 4–100 µm, axon 1 mm–1 m, dendrites). A spike is generated when the membrane voltage difference reaches a critical level; rates are 1 Hz–1 kHz. Neurotransmitters released at the synapse open ion channels. Sodium and potassium channels are two common kinds: potassium has a slow excitatory action; sodium has a fast excitatory and a slow inhibitory action (p. 3-42).
- **Hodgkin–Huxley model**: the membrane is a capacitor,
$$C\frac{dV}{dt}=I_{Na^+}+I_{K^+}+I_{leak}+I_{input},$$
with Ohm's law currents $I_{Na^+}=g_{Na}(E_{Na^+}-V)$, $I_{K^+}=g_K(E_{K^+}-V)$, $I_{leak}=g_{leak}(E_{leak}-V)$.
- Conductances: $g_{Na}\propto m^3h$, $g_K\propto n^4$, $g_{leak}$ constant. The gating variables obey
$$\frac{dm}{dt}=\frac{m_a(V)-m}{\tau_m(V)},\quad \frac{dh}{dt}=\frac{h_a(V)-h}{\tau_h(V)},\quad \frac{dn}{dt}=\frac{n_a(V)-n}{\tau_n(V)}$$
The functions come from experimental data. $m_a,n_a$ are monotone increasing in $V$ (excitatory); $h_a$ is monotone decreasing (inhibitory); $\tau_m$ is almost an order of magnitude smaller than $\tau_h,\tau_n$ (p. 3-43).
- Nernst's law: $E=\frac{RT}{nF}\log\frac{c_e}{c_i}$. At 20 °C: $RT/F=20$ mV, $E_{Na^+}=55$ mV, $E_{K^+}=-92$ mV.
- HH has many widely different time scales, so approximations exist, e.g. FitzHugh–Nagumo (Exercise 3.11). Fig. 3.28: at rest ($I=0$, $V=0$); a short pulse at $t=5$ ms gives one spike; excitation at $t=30$ ms leads to repeated spiking.
- Background given in the text: HH was developed for the squid giant axon; Hodgkin and Huxley shared the 1963 Nobel Prize in Physiology (with J. C. Eccles). The voltage clamp of Section 1.4 was used to determine $m_a(V),n_a(V),h_a(V)$. Integrate-and-fire models combine ODEs with discrete transitions (hybrid systems).

### 3.5 Further Reading (p. 3-44)
The author lists, among others: Cannon (classic on physical-system modeling), Aris (dimension-free variables), Keener & Sneyd, J. D. Murray and Wilson (biology), Ljung (system identification), and notes that Fourier introduced the Fourier series while modeling heat conduction.

### Exercises (pp. 3-44 to 3-48)
Exercises 3.1–3.11 cover: chain-of-integrators form; a discrete-time system; Keynesian economics; least-squares identification; normalized oscillator; Dubins car; motor drive with flexible shaft; electric generator (pendulum-like); admission control for a queue; a two-repressor genetic switch; FitzHugh–Nagumo simulation. Selected ones are listed below.

## Toy example (ours, not from the text)
**Identify a spring–mass system from a step response**, using the three relations of Example 3.8.

Suppose a step of $F_0=10$ N gives these readings: final position $q(\infty)=2$ m; time between two peaks $T=\pi$ s; the peak excess $q(t)-q(\infty)$ falls so that $\log(q(t_1)-F_0/k)-\log(q(t_2)-F_0/k)=\pi$ over $t_2-t_1=\pi$.
1. From (3.23): $k=F_0/q(\infty)=10/2=5$ N/m.
2. From (3.24): $\dfrac{c}{2m}=\dfrac{\pi}{\pi}=1\ \text{s}^{-1}$, so $c=2m$.
3. From the period relation: $\dfrac{2\pi}{T}=2$, and $\Big(\dfrac{2\pi}{T}\Big)^2=\dfrac{4km-c^2}{4m^2}=\dfrac km-\Big(\dfrac c{2m}\Big)^2$ (added step: algebra). So $4=\dfrac5m-1$, i.e. $m=1$ kg.
4. Then $c=2m=2$ N s/m.

Check: $c^2=4<4km=20$, so the oscillatory formula applies; $\omega_d=\sqrt{20-4}/2=2$ and $T=2\pi/2=\pi$ ✓.

## Concepts
- [[stability]] — Lyapunov argument: a quantity that never increases and stops only at the origin shows the origin is stable (p. 3-22)
- [[frequency-response]] (new) — steady-state gain $g(\omega)$ and phase $\varphi(\omega)$ of the output to a sinusoidal input; amplitude-independent for linear systems (p. 3-22)
- [[gain]] — here the frequency-response amplitude ratio $g(\omega)$, and (for a step test) $1/k$. This is not the controller-gain sense of the canon list (pp. 3-22, 3-27)
- [[block-diagram]] (new) — boxes and arrows showing information flow; hides detail; can be hierarchical (p. 3-23)
- [[feedback]] — the fly's visual motion measurement steers the wings, closing the loop (p. 3-25)
- [[algebraic-loop]] (new) — closed loop of blocks with direct input-to-output connections; needs algebraic solving, giving differential algebraic equations (p. 3-26)
- [[step-response]] (new) — output after a quick change of a constant input; its shape gives parameters (p. 3-27)
- [[system-identification]] (new) — subfield on experimental determination of models (p. 3-28)
- [[normalization-scaling]] (new) — dimension-free variables that reduce the number of parameters (p. 3-28)
- [[state-space-model]] — differential equations in state variables, used throughout the examples (e.g. p. 3-29)
- [[inverse-response]] (new) — "shrink and swell": output first moves opposite to its final direction (p. 3-34)
- [[flow-model]] (new) — continuous-flow approximation of a discrete queue (p. 3-36)
- [[homeostasis]] — regulating a quantity such as temperature or blood sugar to a fixed value (p. 3-40)
- [[hill-function]] (new) — model of repression/activation of transcription, with Hill coefficient $n$ (p. 3-40)
- [[graph-laplacian]] (new) — $L=D-A$; drives the consensus update (p. 3-39)

## Canonical instances
- [[spring-mass-system]] — Lyapunov analysis, frequency response, step-response identification, scaling (pp. 3-22, 3-27, 3-28)
- [[balance-system]] — scaling from 5 to 2 parameters (p. 3-29)
- [[fly-flight-control]] — block-diagram example of feedback (p. 3-25)
- [[vehicle-steering]] — bicycle model, Dubins car (p. 3-30)
- [[vectored-thrust-aircraft]] — Harrier model (p. 3-31)
- [[water-heater]] — mass and energy balance (p. 3-33)
- [[drum-boiler]] — inverse response (p. 3-34)
- [[queuing-system]] — flow model and rush-hour effect (p. 3-35)
- [[virtual-memory-paging]] — discrete feedback with three states (p. 3-37)
- [[consensus-protocol]] — average consensus on a graph (p. 3-38)
- [[repressilator]] — three-gene repression cycle that oscillates (p. 3-41)
- [[hodgkin-huxley-neuron]] — conductance-based neuron model (p. 3-42)

## Bridges (candidates)
- [structural-analogy] Fly steering so the contraction point stays centered ↔ perceptual control: an organism acts to keep a perceived quantity at a reference value.
- [structural-analogy] Consensus update $x[k+1]=x[k]-\gamma Lx[k]$ ↔ diffusion on a graph: each node moves toward its neighbors, as heat flows between neighbors.
- [structural-analogy] Hill-function repression in genes ↔ saturating nonlinear map block (Fig. 3.14d): both are input–output curves that flatten at high input.
- [metaphor] Rush-hour effect in queues ↔ delay (dead time): slow recovery after a short overload resembles slow response, though the mechanism here is saturated service rate.

## Questions this raises
- How does one decide how much detail a block should hide, and how can one test that a simplified model still answers the question?
- Why do capacity limits ($\mu_{\max}$) make a queue's recovery so much slower than its build-up, and what does admission control change?
- What does it mean for a system's step response to start in the "wrong" direction, and what does that imply for feedback design (promised for Section 14.4)?
- For which connected graphs and which values of $\gamma$ does consensus converge (the text says one can always find such a $\gamma$)?

## Exercises worth doing
- Ex. 3.3 (p. 3-45) — Keynes multiplier from equilibrium of a difference-equation model, and writing it as a discrete-time state model — difficulty: easy
- Ex. 3.4 (p. 3-45) — least-squares identification of unknown parameters from state measurements (builds $H\alpha=b$) — difficulty: medium
- Ex. 3.5 (p. 3-45) — normalizing the damped oscillator to the single parameter $\zeta$ — difficulty: easy
- Ex. 3.6 (p. 3-46) — derive the Dubins car from the bicycle model with $a=0$ — difficulty: easy
- Ex. 3.9 (p. 3-47) — admission control for the queue with saturated proportional control; simulate and study the effect of $r$ — difficulty: medium
- Ex. 3.10 (p. 3-47) — two-repressor genetic switch in normalized coordinates; show $\mu\approx200$ and simulate — difficulty: hard

## Reading notes
- **Where this part starts and ends.** It starts in the middle of Section 3.2 (the end of the Lyapunov argument for the spring–mass system, pdf 94) and runs to the last page supplied (Exercise 3.11, pdf 120). Section 3.1, the start of 3.2, equation (3.18) and the definition of $V$ are in part 1 and not available here. The task note says the split is at a section boundary, but this part actually begins in the middle of Section 3.2.
- **Page numbers.** The page labels show no printed number, but the running heads show chapter-style numbers (e.g. "3-22" on pdf 94). I cite these. Offset: printed 3-N = pdf − 72 (pdf 94 = 3-22, pdf 120 = 3-48). The task metadata suggested pdf references, but the printed numbers are visible, so I used them.
- **Misprints seen in the source.** Fig. 3.14 caption: "the the". Example 3.11: "it the follows". Example 3.18: the text says that for large $p_b$ "the first term … approaches 1". As written, the first term $\alpha_{ab}k_{ab}p_b^{n}/(1+k_{ab}p_b^{n})$ approaches $\alpha_{ab}$; it is the fraction that approaches 1. The stated transcription rate $\alpha_{ab}+\alpha_{a0}$ is consistent with that. Fig. 3.27a is captioned "Small network of neurons", but the image shows a single neuron.
- **Checks.** In Example 3.8, $q(\infty)=F_0/k=20/40=0.5$ m, consistent with the final level in Fig. 3.16. Fig. 3.22b shows a simulation, not a derived result.
- **References.** Exercise 3.9 refers to $\mathrm{sat}_{(a,b)}$ "defined by equation (4.10)", which is outside this unit. Claims about Chapters 5, 6, 7 and Section 14.4 are forward references only.
