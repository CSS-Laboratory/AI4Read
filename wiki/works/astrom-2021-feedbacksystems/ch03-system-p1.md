---
id: astrom-2021-feedbacksystems/ch03-system-p1
work: astrom-2021-feedbacksystems
unit: "3 System Modeling (part 1/2): 3.1 Modeling Concepts and 3.2 State Space Models (to the start of the stability argument)"
pages: 3-1 to 3-21
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
# System Modeling (part 1/2)

## L0 — One line
A model is a precise representation of a system's dynamics (yet only an approximation of the real system), and in control it is often written as a state space model: first-order differential equations (continuous time) or difference equations (discrete time) in state, input and output.

## L1 — The gist (≤ 120 words)
The chapter asks how to build precise mathematical models of dynamical systems for analysis, simulation and control design. This part reviews the traditions behind modeling: mechanics (state), electrical engineering (input/output) and control (a merger of both). It then covers multidomain, hybrid and uncertain models. After that it introduces state space models as differential and difference equations. Examples include the spring–mass system, balance systems, predator–prey, an e-mail server, a discretized PI controller and a traffic-light state machine. It also shows Euler simulation and starts an energy argument for stability. It matters because every model is an approximation, so its limits must be respected.

**Prerequisites:** derivatives and ODEs; vectors and matrix–vector products; small-angle approximations; basic Boolean logic.

## L2 — Key ideas (5–10 bullets)
- A model is a precise representation of dynamics used to answer questions. The right model depends on the question, so one system can have several models of different fidelity (p. 3-1).
- The *state* summarizes the past for the purpose of predicting the future. In Newton's mechanics, current positions and velocities suffice (p. 3-2).
- Two traditions fed control. Mechanics gave state and phase portraits (traces of the states from different initial conditions). Electrical engineering gave input/output behavior (how the output responds to the input), with step and frequency responses for linear time-invariant systems (systems where superposition holds and the response does not depend on when the input is applied). Control merged them into state space models of input/output systems (pp. 3-2 to 3-6).
- Feedback design can often use comparatively simple models because of the inherent robustness of feedback. Feedforward (using a model to precompute inputs) and validation (checking the detailed response) may need more accurate models, so a hierarchy of models is common (p. 3-6).
- Differential algebraic equations (equations $F(z,\dot z)=0$ that also allow pure algebraic relations) suit component-based (multidomain) modeling. Finite state machines (a finite list of modes with transitions) and hybrid systems (continuous dynamics plus discrete logic) add discrete logic. Model uncertainty is often hard to quantify, and a model is valid only in limited amplitude and frequency ranges (pp. 3-7 to 3-9).
- The standard forms are $\dot x=f(x,u),\ y=h(x,u)$, the linear form $\dot x=Ax+Bu,\ y=Cx+Du$, and the discrete form $x[k+1]=f(x[k],u[k])$. The discrete linear case has the closed-form solution (3.12) (pp. 3-10, 3-14, 3-15).
- Higher-order ODEs convert to first-order state form. Nonlinear balance systems linearize near upright using $\sin\theta\approx\theta$, $\cos\theta\approx1$ and dropping $\dot\theta^2$ terms (pp. 3-11, 3-13, 3-14).
- Difference equations model discrete-time phenomena and also approximate differential equations. Euler integration (3.17), which advances the state by $h$ times its rate of change, and the discretized PI controller both replace a derivative by a finite difference; the text notes that Euler integration is a difference equation, as in Example 3.6 (pp. 3-17, 3-20).
- To show that the mass returns to rest from any initial condition (later called asymptotic stability), the text starts an energy-function argument: the energy $V$ has derivative $-cx_2^2$, described as always negative or zero, so $V$ never increases and the states stay bounded. A more detailed analysis is still needed for the return to rest (p. 3-21).

## L3 — Walkthrough

### Chapter opening (p. 3-1)
- **Epigraph (Dyson, reporting Fermi, reporting von Neumann):** Fermi asked how many arbitrary parameters Dyson's model used. Dyson said four. Fermi recalled von Neumann's remark that with four parameters one can fit an elephant, and with five make him wiggle his trunk (p. 3-1).
- A *model* is a precise representation of a system's dynamics, used to answer questions via analysis and simulation. The model chosen depends on the questions, so there may be several models of one system, with different fidelity (p. 3-1).
- The chapter covers two methods common in feedback and control: differential equations and difference equations (p. 3-1).

### 3.1 Modeling Concepts
- Models allow reasoning and predictions, but they are approximations of the underlying system. Analysis and design must respect the limits of the model (p. 3-1).
- *Dynamical system* (roughly): one where effects of actions do not occur immediately. Examples are car velocity after pressing the gas pedal, room temperature after switching on a heater, a headache after an aspirin, and revenues after funding a development project. Revenues may rise in the long term if it was a good investment (pp. 3-1, 3-2).

**The Heritage of Mechanics (p. 3-2)**
- Dynamics began with planetary motion (Brahe's observations, Kepler's ellipses, Newton's law of gravitation and force = mass × acceleration). Newton also invented calculus and differential equations (p. 3-2).
- Planetary motion could be predicted from the current positions and velocities of all planets; the past motion need not be known (p. 3-2).
- **State** of a dynamical system: a collection of variables that completely captures the past motion for the purpose of predicting future motion. The set of all possible states is the **state space** (p. 3-2).
- A common model class is the ordinary differential equation (ODE). The spring–mass system with damping (Fig. 3.1):
$$m\ddot q + c(\dot q) + kq = 0 \tag{3.1}$$
 Here $q\in\mathbb R$ is the mass position relative to rest, $\dot q$ the velocity, $\ddot q$ the acceleration. The spring obeys Hooke's law (force proportional to displacement). The damper $c(\dot q)$ is a nonlinear function that can model Coulomb friction and viscous drag (pp. 3-2, 3-3).
- Position and velocity form the state vector $x=(q,\dot q)$. With two states, the system is **second-order** (p. 3-3).
- Fig. 3.2 shows two views. The *time plot* shows each state against time. The *phase portrait* shows traces from different initial conditions in the state space, with arrows for the velocity $\dot x$. It gives an intuitive picture of the equation as a vector field or flow. It works for two states and is hard to visualize for higher order (p. 3-3).
- (3.1) is **autonomous**: no external influences. This is natural for celestial mechanics, where planets are hard to influence. The authors note this usage differs slightly from "autonomous vehicle" (p. 3-3).
- Adding an input gives the forced (controlled) equation
$$m\ddot q + c(\dot q) + kq = u \tag{3.2}$$
 The input $u(t)$ can influence the rate of change of the state. New questions become possible: the influence of external disturbances on trajectories, and whether the system can be "steered" from one state to another by choosing the input (pp. 3-3, 3-4).

**The Heritage of Electrical Engineering (pp. 3-4, 3-5)**
- Amplifier design led to a focus on input/output behavior. A system is a device that transforms inputs into outputs (Fig. 3.3: a detailed circuit diagram versus a block diagram). Conceptually an input/output model is a giant table: given $u(t)$ over an interval, produce $y(t)$ (p. 3-4).
- The framework lets one decompose a system (e.g., radio: receiver, demodulator, amplifier, speakers) into components connected through inputs and outputs (p. 3-4).
- **Linear** (roughly): superposing two inputs gives the sum of the outputs for each input applied separately. **Time-invariant**: the response to an input does not depend on when it is applied. Many electrical systems can be modeled as linear time-invariant systems, so many tools exist (p. 3-4).
- **Step response:** output for an input that jumps abruptly from zero to a constant. It characterizes performance and is often used to specify desired dynamics (Fig. 3.4a: input steps 0→1 at $t=5$ s) (p. 3-5).
- **Frequency response:** response to sinusoidal inputs, built on complex variables and Laplace transforms. The idea is to characterize a system by its steady-state response to sinusoids. An arbitrary signal is decomposed into sinusoids (e.g., by the Fourier transform), and linearity is used to combine the outputs (Fig. 3.4b: gain and phase) (p. 3-5).
- The input/output view suits experimental determination of dynamics, by recording responses to a step or to sinusoids over a range of frequencies (p. 3-5).

**The Control View (pp. 3-5, 3-6)**
- Control theory emerged in the 1940s, strongly influenced by the input/output view. A second wave from the late 1950s was inspired by mechanics and the state space view (spacecraft orbit control is an example). The two views gradually merged into today's state space representation of input/output systems. In the 1970s, automation added the need to include logic and sequencing (pp. 3-5, 3-6).
- The mechanical model (3.2) was replaced by
$$\frac{dx}{dt}=f(x,u),\qquad y=h(x,u) \tag{3.3}$$
 with $x$ the state vector, $u$ the control signals, $y$ the measurements, and $f,h$ possibly nonlinear maps. Dynamics are modeled as first-order equations. Higher-order equations are captured by suitable choice of state and of $f,h$ (p. 3-6).
- New questions: can states be reached by choice of $u$ (**reachability**)? Does $y$ contain enough information to reconstruct the state (**observability**)? These are treated in Chapters 7 and 8 (p. 3-6).
- Disturbances and model uncertainty became critical. Modeling disturbances as deterministic signals (steps, sinusoids) has the drawback that such signals cannot be predicted precisely. A more realistic approach models disturbances as random signals, which links prediction and control. State models are convenient for a nominal model, while uncertainties are easier to describe with input/output models (often via frequency response). Uncertainty returns in Chapter 13 (p. 3-6).
- Feedback systems can often be analyzed and designed using comparatively simple models, because of their inherent robustness. Other uses need more complexity and accuracy: *feedforward* (precompute inputs that make the system respond in a certain way) and *validation* (verify the detailed response). Hence a hierarchy of models of different complexity and fidelity is common (p. 3-6).

*Intuition note.* The state is what you must know now to predict the future without needing the past (the text's wording: variables that capture the past for the purpose of predicting the future). Control took mechanics' state and electrical engineering's input/output view and put them in one form, equation (3.3). Because of the inherent robustness of feedback, comparatively simple models can often be used for design, though other uses (feedforward, validation) may need more accuracy.

**Multidomain Modeling (pp. 3-6, 3-7)**
- Systems engineering often meets heterogeneous systems (chemical, electrical, mechanical, information). The method: partition into subsystems. Each is described by balance equations for mass, energy and momentum, or by descriptions of information processing. Interfaces constrain variables of the subsystems to be equal (e.g., mass, energy or momentum fluxes). The complete model combines subsystems and interfaces (p. 3-7).
- This allows libraries of reusable components. It takes several iterations to get a good library (p. 3-7).
- State models or ODEs are not suitable for this component-based modeling, because states may disappear when components are connected. Two capacitors each have a voltage state, but one state disappears when they are connected in parallel. Two rotating inertias, each with angle and angular velocity, lose two states when joined by a rigid shaft (p. 3-7).
- Remedy: **differential algebraic equations** $F(z,\dot z)=0$, $z\in\mathbb R^n$. A special case:
$$\dot x=f(x,y),\qquad g(x,y)=0 \tag{3.4}$$
 with $z=(x,y)$ and $F=(\dot x-f(x,y),\ g(x,y))$. The derivative $\dot z$ is not given explicitly, and pure algebraic relations may link components of $z$. This is also called equation-based, acausal or behavioral modeling. For parallel capacitors one adds the algebraic equation that the voltages are equal (p. 3-7).
- **Modelica** is a language for component-based modeling. It uses differential algebraic equations as the basic description and object-oriented programming to structure models. It is intended as a standard exchange format, with free and commercial libraries (pp. 3-7, 3-8).

**Finite State Machines and Hybrid Systems (p. 3-8)**
- A **hybrid system** (cyberphysical system) combines continuous dynamics with discrete logic, e.g., modes such as on, off, degraded (p. 3-8).
- A **finite state machine** has a finite set of discrete states $\alpha\in Q$ ("modes") and transitions between them. A *guarded transition system*:
$$g_i(\alpha,\beta)\Longrightarrow \alpha'=r_i(\alpha),\qquad i=1,\dots,N.$$
 $g_i$ is a Boolean function of the mode $\alpha$ and an input $\beta$ (an environmental event such as a button press or component failure). If $g_i$ is true, the system moves to $\alpha'$ given by the transition map $r_i$ (p. 3-8).
- A hybrid system with continuous state $x$ and discrete state $\alpha$:
$$\frac{dx}{dt}=f_\alpha(x,u),\qquad g_i(x,\alpha,\beta)\Longrightarrow \alpha'=r_i(x,\alpha),\quad i=1,\dots,N.$$
 The ODE depends on the mode (subscript $\alpha$). Guards and rules depend on the continuous state (p. 3-8).
- Other representations exist, including "reset logic" (non-continuous jumps in continuous variables at mode changes). Tools named: StateFlow, Modelica, Ptolemy (p. 3-8).

**Model Uncertainty (pp. 3-8, 3-9)**
- Reducing uncertainty is one of the main reasons for feedback, so uncertainty must be characterized. Measurements carry a nominal value plus an uncertainty measure; the same would be useful for models, but model uncertainty is often hard to express quantitatively (p. 3-8).
- *Static system:* an uncertainty band (Fig. 3.5a). At low signal levels, uncertainty comes from sensor resolution, friction and quantization. At large levels there are saturations or failures. It is rare to find models accurate over signal ranges larger than $10^4$ (p. 3-9).
- *Dynamical models:* it is much more difficult. Assigning uncertainty to parameters is often not sufficient. Neglected phenomena (e.g., small time delays) matter, and "in control the ultimate test is how well a control system based on the model performs" (p. 3-9). There are slow effects (aging, drift) and high-frequency effects (a resistor is not purely resistive at very high frequency; a beam shows extra dynamics under high-frequency excitation) (p. 3-9).
- The **uncertainty lemon** (Fig. 3.5b) shows that a model is valid only in certain amplitude and frequency ranges. Fig. 3.5c represents a model as a nominal model $M$ plus an uncertainty model $\Delta$, to be used with transfer functions in Chapter 13 (p. 3-9).
- Practical advice: recognize the limits of a model and do not use it outside its range of applicability. One can describe the lemon and check that signals stay inside it. Analog computers gave alarms when signal levels were exceeded, and digital simulation can do likewise (p. 3-9).

### 3.2 State Space Models (p. 3-10)
This section covers differential equations, difference equations and finite state systems.

**Ordinary Differential Equations (pp. 3-10, 3-11)**
- For a physical system, the state consists of the variables needed to account for storage of mass, momentum and energy. How accurately to represent this is a key modeling decision (p. 3-10).
- State $x\in\mathbb R^n$ (state vector), control $u\in\mathbb R^p$, measured signal $y\in\mathbb R^q$:
$$\frac{dx}{dt}=f(x,u),\qquad y=h(x,u) \tag{3.5}$$
 with $f:\mathbb R^n\times\mathbb R^p\to\mathbb R^n$ and $h:\mathbb R^n\times\mathbb R^p\to\mathbb R^q$ smooth. This is a **state space model**. Its **order** is the dimension $n$ of the state (p. 3-10).
- (3.5) is **time invariant** because $f,h$ do not depend explicitly on $t$. $f$ gives the rate of change of the state, and $h$ gives the measured values (p. 3-10).
- **Linear** state space model: $f,h$ linear in $x,u$:
$$\frac{dx}{dt}=Ax+Bu,\qquad y=Cx+Du \tag{3.6}$$
 with constant matrices. This is *linear time-invariant* (LTI); the text usually just says "linear". Names: $A$ dynamics matrix, $B$ control matrix, $C$ sensor matrix, $D$ direct term. Often $D=0$, meaning $u$ does not influence $y$ directly (p. 3-10). (added step: shapes are $A\in\mathbb R^{n\times n}$, $B\in\mathbb R^{n\times p}$, $C\in\mathbb R^{q\times n}$, $D\in\mathbb R^{q\times p}$, which follow from the dimensions of $x,u,y$.)
- An $n$th-order linear ODE generalizing the mechanical second-order case (p. 3-10):
$$\frac{d^ny}{dt^n}+a_1\frac{d^{n-1}y}{dt^{n-1}}+\cdots+a_ny=u \tag{3.7}$$
- **Conversion to state form:** define $x_1=d^{n-1}y/dt^{n-1},\ x_2=d^{n-2}y/dt^{n-2},\ \dots,\ x_{n-1}=dy/dt,\ x_n=y$. Then
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\\vdots\\x_{n-1}\\x_n\end{pmatrix}=\begin{pmatrix}-a_1x_1-\cdots-a_nx_n\\x_1\\\vdots\\x_{n-2}\\x_{n-1}\end{pmatrix}+\begin{pmatrix}u\\0\\\vdots\\0\\0\end{pmatrix},\qquad y=x_n.$$
 With suitable $A,B,C,D$ this is linear state space form (p. 3-11). (added step: the first row is (3.7) solved for the highest derivative; the other rows say that the derivative of each state is the next-higher one.)
- A more general output $y=b_1x_1+\cdots+b_nx_n+du$ gives
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{pmatrix}=\begin{pmatrix}-a_1&-a_2&\cdots&-a_{n-1}&-a_n\\1&0&\cdots&0&0\\0&1&&0&0\\\vdots&&\ddots&&\vdots\\0&0&&1&0\end{pmatrix}x+\begin{pmatrix}1\\0\\0\\\vdots\\0\end{pmatrix}u,\qquad y=\begin{pmatrix}b_1&b_2&\cdots&b_n\end{pmatrix}x+du \tag{3.8}$$
 This is called **reachable canonical form**, studied in later chapters. Many other representations exist (Chapters 6–8). Input derivatives can also be allowed in (3.7) (p. 3-11).

**Example 3.1 Spring–mass system (pp. 3-11, 3-12).**
- Take (3.2) with output $y=q$ and viscous friction $c(\dot q)=c\dot q$. State $x=(x_1,x_2)=(\dot q,q)$ (note the order: velocity first). Then
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}-c/m&-k/m\\1&0\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}+\begin{pmatrix}1/m\\0\end{pmatrix}u.$$

**Example 3.2 Balance systems (pp. 3-12 to 3-14).**
- A *balance system* is a mechanical system whose center of mass is balanced above a pivot point. Examples (Fig. 3.6): Segway, a rocket with a gimballed nozzle, standing humans or animals, balancing a stick on a hand. All use forces at the bottom to keep the system upright (p. 3-12).
- General mechanical form: $M(q)\ddot q+C(q,\dot q)+K(q)=B(q)u$. $M$ is the inertia matrix, $C$ the Coriolis forces plus damping, $K$ the potential-energy forces, $B$ the coupling of external forces. $q$ may be a vector of configuration variables. The terms are often nonlinear in $q$ (pp. 3-12, 3-13).
- Cart–pendulum (Fig. 3.6c): state $x=(q,\theta,\dot q,\dot\theta)$, input $u=F$ (horizontal force at the base), outputs $y=(q,\theta)$. Newtonian mechanics gives
$$\begin{pmatrix}M+m&-ml\cos\theta\\-ml\cos\theta&J+ml^2\end{pmatrix}\begin{pmatrix}\ddot q\\\ddot\theta\end{pmatrix}+\begin{pmatrix}c\dot q+ml\sin\theta\,\dot\theta^2\\\gamma\dot\theta-mgl\sin\theta\end{pmatrix}=\begin{pmatrix}F\\0\end{pmatrix} \tag{3.9}$$
 $M$ is the base mass; $m,J$ are mass and moment of inertia of the balanced body; $l$ is the distance from the base to its center of mass; $c,\gamma$ are viscous friction coefficients; $g$ is gravity (p. 3-13).
- With $M_t=M+m$, $J_t=J+ml^2$, $c_\theta=\cos\theta$, $s_\theta=\sin\theta$:
$$\frac{d}{dt}\begin{pmatrix}q\\\theta\\\dot q\\\dot\theta\end{pmatrix}=\begin{pmatrix}\dot q\\\dot\theta\\ \dfrac{-mls_\theta\dot\theta^2+mg(ml^2/J_t)s_\theta c_\theta-c\dot q-(\gamma/J_t)mlc_\theta\dot\theta+u}{M_t-m(ml^2/J_t)c_\theta^2}\\[3mm] \dfrac{-ml^2s_\theta c_\theta\dot\theta^2+M_tgls_\theta-clc_\theta\dot q-\gamma(M_t/m)\dot\theta+lc_\theta u}{J_t(M_t/m)-m(lc_\theta)^2}\end{pmatrix},\qquad y=\begin{pmatrix}q\\\theta\end{pmatrix}$$
 (p. 3-13).
- If $\theta$ is near 0 and $\dot\theta$ is small, use $\sin\theta\approx\theta$, $\cos\theta\approx1$ and ignore quadratic and higher terms in $\dot\theta$. The result is linear, with $\mu=M_tJ_t-m^2l^2$ (pp. 3-13, 3-14):
$$\frac{d}{dt}\begin{pmatrix}q\\\theta\\\dot q\\\dot\theta\end{pmatrix}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&m^2l^2g/\mu&-cJ_t/\mu&-\gamma lm/\mu\\0&M_tmgl/\mu&-clm/\mu&-\gamma M_t/\mu\end{pmatrix}\begin{pmatrix}q\\\theta\\\dot q\\\dot\theta\end{pmatrix}+\begin{pmatrix}0\\0\\J_t/\mu\\lm/\mu\end{pmatrix}u,\qquad y=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix}x.$$
 (added step: shapes are $A$ $4\times4$, $B$ $4\times1$, $C$ $2\times4$.)

**Example 3.3 Inverted pendulum (p. 3-14).** If the base position $q$ need not be controlled (e.g., only the rocket's upright orientation matters), the model reduces to
$$\frac{d}{dt}\begin{pmatrix}\theta\\\dot\theta\end{pmatrix}=\begin{pmatrix}\dot\theta\\ \dfrac{mgl}{J_t}\sin\theta-\dfrac{\gamma}{J_t}\dot\theta+\dfrac{l}{J_t}u\cos\theta\end{pmatrix},\qquad y=\theta \tag{3.10}$$
with $\gamma$ the rotational friction coefficient and $u$ the force applied at the base.

*Intuition note.* Converting an $n$th-order ODE to $n$ first-order equations is done by a change of variables: the state is the output and its first $n-1$ derivatives (for the form (3.7)). The balance-system example shows one workflow: derive a nonlinear model, then approximate it near $\theta\approx0$ to get a linear model with matrices $A,B,C$.

**Difference Equations (pp. 3-14, 3-15)**
- When the system is more naturally described at discrete times $k=0,1,2,\dots$, it is a *discrete-time system*. State again means the variables that summarize the past for predicting the future (p. 3-14).
$$x[k+1]=f(x[k],u[k]),\qquad y[k]=h(x[k],u[k]) \tag{3.11}$$
 with $x[k]\in\mathbb R^n$, $u[k]\in\mathbb R^p$, $y[k]\in\mathbb R^q$, and $f,h$ smooth. It is a *difference equation* because it tells how $x[k+1]$ differs from $x[k]$. The $j$th state at time $k$ is $x_j[k]$ (p. 3-14).
- Linear case: $x[k+1]=Ax[k]+Bu[k]$, $y[k]=Cx[k]+Du[k]$, with the same matrix names (p. 3-14).
- By repeated substitution, with initial condition $x[0]$ and inputs $u[0],\dots,u[T]$, for $k>0$:
$$x[k]=A^kx[0]+\sum_{j=0}^{k-1}A^{k-j-1}Bu[j],\qquad y[k]=CA^kx[0]+\sum_{j=0}^{k-1}CA^{k-j-1}Bu[j]+Du[k] \tag{3.12}$$
 (p. 3-15). (added check: for $k=1$ the sum has the single term $j=0$, giving $x[1]=Ax[0]+Bu[0]$, as the recursion says.)
- Difference equations are also useful as approximations of differential equations (p. 3-15).

*Intuition note.* Formula (3.12) says the state at time $k$ is the initial state pushed forward $k$ times by $A$, plus each past input $u[j]$, entering through $B$, pushed forward $k-j-1$ times by $A$. The state carries the effect of all earlier inputs.

**Example 3.4 Predator–prey (pp. 3-15, 3-16).**
- Two species, one feeding on the other. Fig. 3.7 shows 90 years of annual data for lynx and hare populations in the Canadian Rockies. They are oscillatory (p. 3-15).
- With $H$ hares and $L$ lynxes:
$$H[k+1]=H[k]+b_h(u)H[k]-aL[k]H[k],\qquad L[k+1]=L[k]+cL[k]H[k]-d_lL[k] \tag{3.13}$$
 $b_h(u)$ is the hare birth rate per period, a function of food supply $u$. $d_l$ is the lynx mortality rate. $a,c$ are interaction coefficients (p. 3-15).
- The term $aLH$ models predation, assumed proportional to the rate at which predators and prey meet, hence to the product of populations. $cLH$ is the lynx growth term of similar form. The model assumes, for example, that hares decrease only through predation. Still, it "often is sufficient to answer basic questions" (pp. 3-15, 3-16).
- Simulation starts from $x[0]=(H_0,L_0)$ and iterates (3.13). With $a=c=0.014$, $b_h(u)=0.6$, $d_l=0.7$, period and magnitude of the cycles approximately match the data (Fig. 3.8). Details differ from the data, which is expected given the simple assumptions. The trends are qualitatively similar (p. 3-16).

**Example 3.5 E-mail server (pp. 3-16, 3-17).**
- The IBM Lotus (Domino) server handles e-mail, documents and notes. Performance was poor when the CPU was overloaded by too many requests, so load control was introduced (p. 3-16).
- Input: MaxUsers, the number of client connections, set by the administrator. Output: RIS (RPCs in server), the number of requests being served. The steady-state input–output relation was first found to be linear (p. 3-16).
- Reference [HDPT04] uses system identification to fit a first-order difference equation (p. 3-17):
$$y[k+1]=ay[k]+bu[k],\qquad u=\text{MaxUsers}-\overline{\text{MaxUsers}},\quad y=\text{RIS}-\overline{\text{RIS}}$$
 with $a=0.43$, $b=0.47$, nominal point $\overline{\text{MaxUsers}}=165$, $\overline{\text{RIS}}=135$, and requests averaged over a 60 s sampling period (p. 3-17).

**Example 3.6 Difference approximation of a PI controller (p. 3-17).**
- Early controllers were analog (differential equations). Implementing one on a computer requires approximation, e.g., replacing derivatives by finite differences (p. 3-17).
- PI controller: $u(t)=k_pe(t)+k_i\int_0^te(\tau)d\tau=k_pe(t)+x(t)$, with $x(t)=k_i\int_0^te(\tau)d\tau$. The controller state obeys
$$\frac{dx}{dt}=k_ie(t) \tag{3.14}$$
- With error measured at $t=h,2h,3h,\dots$, replace the derivative by $\dfrac{x(jh+h)-x(jh)}{h}=k_ie(jh)$. This gives the difference equation
$$x[j+1]=x[j]+hk_ie[j],\qquad u[j]=k_pe[j]+x[j],$$
 with $x[j]=x(jh)$, $e[j]=e(jh)$, $u[j]=u(jh)$. The index $j$ avoids confusion with the gains $k_p,k_i$. It needs only addition and multiplication (p. 3-17).
- The approximation works well provided the sampling interval is so short that $e(t)$ changes very little over it (p. 3-17).

**Finite State Machines (pp. 3-17 to 3-19)**
- Some systems have discrete states (on, off, standby, fault). In a finite state machine the states come from a finite list of modes, and dynamics are transitions between modes, possibly in response to external signals (pp. 3-17, 3-18).

**Example 3.7 Traffic light controller (p. 3-18).**
- State = which lights are on (east–west or north–south). A light stays on for a minimum time and then changes only when a car arrives in the opposite direction. Each direction therefore has two states, waiting for a car and waiting for the timer. This gives four states (Fig. 3.9): N–S waiting, N–S countdown, E–W waiting, E–W countdown (p. 3-18).
- Cycle: from N–S waiting, a car arriving on the E–W street starts a timer. When the timer expires, the E–W lights turn on. Then wait for a car on the N–S street, and so on. Inputs: signals indicating cars at the roads. Outputs: signals changing the light colors. The dynamics are the transition diagram (p. 3-18).

- Formally, $\alpha\in Q_{sys}$ (a discrete set), input events $\beta\in Q_{in}$, output actions $\gamma\in Q_{out}$. A **guarded command system**:
$$g_i(\alpha,\beta)\Longrightarrow\begin{cases}\alpha'=r_i(\alpha,\beta),\\ \gamma=a_i(\alpha,\beta),\end{cases}\qquad i=1,\dots,N \tag{3.15}$$
 If the Boolean guard $g_i$ is true, the state moves to $\alpha'$ by the transition map $r_i$, and the output action $a_i$ is produced. There can be many rules (pp. 3-18, 3-19).
- Compared with (3.11), transitions need not occur at regularly spaced times. There is no strict notion of time; only the sequence of events is tracked (p. 3-19).
- Specifications are often logical formulas. Example: if sensor $k$ is not functioning, the system cannot move to a mode requiring sensor $k$:
 $\alpha\in\{\text{sensor }k\text{ not functioning}\}\Longrightarrow\alpha'\notin\{\text{states requiring sensor }k\}$.
 A formula $p\Longrightarrow q$ can be written as the logical function $(!p)\,||\,(p\,\&\&\,q)$, which asserts that if $p$ is true then $q$ must be true (p. 3-19).
- Finite state machines are often combined with continuous models to make hybrid systems. Hybrid systems are beyond this text's scope (references Lee–Seshia, Alur) (p. 3-19).

**Simulation and Analysis (pp. 3-19 to 3-21)**
- A common question is predicting the state evolution from an initial condition. For simple models this can be done in closed form; more often by computer simulation (p. 3-19).
- Driven spring–mass system (Fig. 3.10), force $u=A\sin\omega t$, with Hooke's law and viscous damping:
$$m\ddot q+c\dot q+kq=u \tag{3.16}$$
 With $x=(q,\dot q)$ and $y=q$:
$$\frac{dx}{dt}=\begin{pmatrix}x_2\\-\frac{c}{m}x_2-\frac{k}{m}x_1+\frac{u}{m}\end{pmatrix},\qquad y=x_1.$$
 It is linear, second-order, with one input and one output (pp. 3-19, 3-20).
- **Euler integration:** for $\dot x=f(x,u)$, assume the rate $f(x,u)$ is constant over $[t,t+h]$, $h>0$ small:
$$x(t+h)=x(t)+hf(x(t),u(t)) \tag{3.17}$$
 Iterating gives $x(t)$. With $x[k]=x(kh)$, this is a difference equation, as in Example 3.6. MATLAB and Mathematica use more accurate methods but "still have some of the same basic trade-offs" (p. 3-20).
- Fig. 3.11 compares Euler solutions for $h=1,\,0.5,\,0.1$ with the analytical solution. As $h$ decreases, the computed solution converges to the exact one. After an initial transient the system settles into periodic motion, the **steady-state response** to the input (pp. 3-20, 3-21).
- Models can answer other questions. Two are central to this text: stability of an equilibrium point and the input/output frequency response. The text illustrates both and returns in later chapters (p. 3-21).
- **Stability argument (begins; the part ends mid-argument).** Unforced system:
$$\frac{dx}{dt}=\begin{pmatrix}x_2\\-\frac{c}{m}x_2-\frac{k}{m}x_1\end{pmatrix} \tag{3.18}$$
 with $x_1$ the position and $x_2$ the velocity. Goal: show that from any initial state away from rest, the system eventually returns to rest. The text will later call this *asymptotically stable*. Simulating many initial conditions would only be heuristic, so the author seeks a proof for any initial condition (p. 3-21).
- Construct $V:\mathbb R^n\to\mathbb R$ mapping the state to a positive real number. For mechanical systems a convenient choice is the energy:
$$V(x)=\tfrac12kx_1^2+\tfrac12mx_2^2 \tag{3.19}$$
 Then
$$\frac{dV}{dt}=kx_1\dot x_1+mx_2\dot x_2=kx_1x_2+mx_2\left(-\frac{c}{m}x_2-\frac{k}{m}x_1\right)=-cx_2^2,$$
 (added step: the terms $kx_1x_2$ and $-kx_1x_2$ cancel). The source says this is "always either negative or zero". Hence $V(x(t))$ is never increasing and, "using a bit of analysis that we will see formally later", the individual states must remain bounded (p. 3-21).
- To show the states return to the origin, "a slightly more detailed analysis" is needed. The text begins an intuitive argument ("suppose …") and the pages given end there (p. 3-21).

*Intuition note.* Energy is a quantity that depends only on the state. Here $\dot V=-cx_2^2$, which the text calls always negative or zero (this presupposes $c\ge0$), so the energy never increases and, by "a bit of analysis that we will see formally later", the states stay bounded. This does not yet prove the mass returns to rest; the text says a finer argument is needed.

## Toy example (ours, not from the text)
Euler integration (3.17) of the unforced spring–mass system, choosing $m=1$, $c=1$, $k=1$, $h=0.5$, $x=(q,\dot q)$, $x(0)=(1,0)$.

- Here $f(x)=(x_2,\,-x_2-x_1)$, so $\dot x=Ax$ with $A=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}$. Euler gives $x[k+1]=(I+hA)x[k]$ with $I+hA=\begin{pmatrix}1&0.5\\-0.5&0.5\end{pmatrix}$ (shape $2\times2$ times $2\times1$).
- Step 1: $f(1,0)=(0,\,-0-1)=(0,-1)$. So $x[1]=(1+0.5\cdot0,\ 0+0.5\cdot(-1))=(1,-0.5)$. Matrix check: $(1\cdot1+0.5\cdot0,\ -0.5\cdot1+0.5\cdot0)=(1,-0.5)$. ✓.
- Step 2: $f(1,-0.5)=(-0.5,\ 0.5-1)=(-0.5,-0.5)$. So $x[2]=(1-0.25,\ -0.5-0.25)=(0.75,-0.75)$. Matrix check: $(1-0.25,\ -0.5-0.25)$ ✓.
- Energy (3.19): $V(x[0])=\tfrac12\cdot1+0=0.5$. $V(x[1])=\tfrac12\cdot1+\tfrac12\cdot0.25=0.625$. $V(x[2])=\tfrac12(0.5625)+\tfrac12(0.5625)=0.5625$.
- The exact system has $dV/dt=-cx_2^2\le0$ (e.g., $-0.25$ at $x[1]$), yet the coarse Euler step raised $V$ from 0.5 to 0.625. This shows the step size trade-off: the Euler difference equation only approximates the ODE, and it is accurate only for small $h$.

## Concepts
- [[state]] — variables that capture the past for predicting the future; in physical systems they account for storage of mass, momentum, energy (pp. 3-2, 3-10)
- [[state-space-model]] — $\dot x=f(x,u)$, $y=h(x,u)$; linear case $\dot x=Ax+Bu$, $y=Cx+Du$ (pp. 3-6, 3-10)
- [[linearization]] — here used as approximating a nonlinear model near $\theta\approx0$ with $\sin\theta\approx\theta$, $\cos\theta\approx1$ and dropping $\dot\theta^2$ terms (p. 3-13)
- [[controllability]] — here called *reachability*: can possible states be reached by choosing $u$; only named, treated in Chs. 7 and 8 (p. 3-6)
- [[observability]] — whether $y$ contains enough information to reconstruct the state; only named (p. 3-6)
- [[stability]] — here: rest position is *asymptotically stable* if states return to rest from any initial condition; defined later (p. 3-21)
- [[feedforward]] — using a model to precompute inputs that make the system respond in a certain way (p. 3-6)
- [[robustness]] — the inherent property of feedback systems that the text gives as the reason they can often be analyzed and designed using comparatively simple models (p. 3-6)
- [[disturbance-and-noise]] — disturbances modeled as deterministic signals (steps, sinusoids) or, more realistically, as random signals (p. 3-6)
- [[delay]] — neglected small time delays are an example of uncertainty that can matter in control (p. 3-9)
- [[transfer-function]] — describes the frequency response of an input/output system; only mentioned (p. 3-9)
- [[pid-control]] — the PI case: $u=k_pe+k_i\int e$, discretized in Example 3.6 (p. 3-17)
- [[difference-equation]] (new) — $x[k+1]=f(x[k],u[k])$; discrete-time model, also an approximation to ODEs (p. 3-14)
- [[euler-integration]] (new) — $x(t+h)=x(t)+hf(x(t),u(t))$, assuming constant rate over $h$ (p. 3-20)
- [[phase-portrait]] (new) — traces of states from different initial conditions with velocity arrows (p. 3-3)
- [[linear-time-invariant-system]] (new) — superposition holds; response does not depend on when the input is applied (p. 3-4)
- [[step-response]] / [[frequency-response]] (new) — outputs for a step input / for sinusoidal inputs of different frequencies (p. 3-5)
- [[differential-algebraic-equation]] (new) — $F(z,\dot z)=0$; allows algebraic relations, suited to component-based modeling (p. 3-7)
- [[finite-state-machine]] and [[hybrid-system]] (new) — discrete modes with guarded transitions; with continuous dynamics too (pp. 3-8, 3-18)
- [[model-uncertainty]] (new) — uncertainty band, uncertainty lemon, nominal model $M$ plus uncertainty $\Delta$ (p. 3-9)
- [[energy-function-stability-argument]] (new) — $V=\tfrac12kx_1^2+\tfrac12mx_2^2$ with $\dot V=-cx_2^2$ (p. 3-21)

## Canonical instances
- [[spring-mass-system]] — second-order mechanical model, autonomous (3.1), forced (3.2), driven (3.16) (pp. 3-2, 3-11, 3-19)
- [[balance-system]] — cart–pendulum with nonlinear (3.9) and linearized models; inverted pendulum (3.10) (pp. 3-12 to 3-14)
- [[predator-prey]] — lynx–hare discrete-time model (3.13) (pp. 3-15, 3-16)
- [[email-server-model]] — first-order difference model with $a=0.43$, $b=0.47$ (p. 3-17)
- [[pi-controller-discretization]] — Euler discretization of a PI controller (p. 3-17)
- [[traffic-light-controller]] — four-state finite state machine (p. 3-18)

## Bridges (candidates)
- [same-math] Euler integration (3.17) ↔ discretized PI controller (Ex. 3.6): both replace $\dot x=\ldots$ by $x[k+1]=x[k]+h\cdot(\text{rate})$, as the text itself notes (p. 3-20).
- [structural-analogy] Energy function $V$ with $\dot V\le0$ ↔ control theory (stability): a scalar function of the state that cannot increase proves boundedness without solving the ODE.
- [structural-analogy] Predator–prey difference model (3.13) ↔ social-science dynamics: products of population sizes model pairwise encounters (the $aLH$ and $cLH$ terms).
- [metaphor] Uncertainty lemon ↔ any social-science model: a model is valid only over a limited range of conditions.

## Questions this raises
- How can $\dot V=-cx_2^2$, which is zero whenever $x_2=0$, still lead to the conclusion that the state returns to the origin? (The text promises a more detailed argument, cut off here.)
- How small must the step $h$ be in Euler integration for a given accuracy, and what do better methods do differently?
- Which state-space matrices correspond to a given frequency response (Fig. 3.4b), and vice versa?
- How does one quantify the uncertainty $\Delta$ of a dynamical model (Chapter 13)?

## Reading notes
- **Where the part starts and ends:** it starts at the chapter opening (Chapter 3 epigraph and intro) and runs through all of 3.1 and 3.2 up to the middle of "Simulation and Analysis". It stops in mid-argument ("suppose …", p. 3-21). The split was at a section boundary per the source notes, but the text layer ends mid-sentence.
- **Page numbers:** the text-layer labels give no printed number, but the page images show printed numbers "3-1" to "3-21". Printed = "3-" followed by (pdf − 72), i.e., pdf 73 = p. 3-1. The citations (p. 3-N) use these.
- **OCR:** the text layer garbles the matrices in (3.8) and Examples 3.1–3.2. I checked them against the page images.
- **Source oddities:**
 - In Example 3.1 the state is $x=(\dot q,q)$, while earlier (Section 3.1, p. 3-3) and later (p. 3-20) it is $(q,\dot q)$.
 - The text before (3.8) defines $x_i$ as derivatives of $y$ for the case $y=x_n$. It does not say how the states are redefined in (3.8), where $y=b_1x_1+\dots+b_nx_n+du$.
 - In Example 3.4 the text says the time index $k$ corresponds "to each day", while Fig. 3.7 and Fig. 3.8 are in years.
 - The text says $\dot V$ is "always either negative or zero". This presupposes $c\ge0$, which is not stated on these pages.
 - Pages 3-8 and 3-17 show a small road-sign symbol beside the "Finite State Machines" headings; the pages do not explain it.
 - The source prints no exercises in this part.
