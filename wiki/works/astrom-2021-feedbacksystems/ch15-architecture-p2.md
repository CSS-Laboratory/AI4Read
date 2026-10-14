---
id: astrom-2021-feedbacksystems/ch15-architecture-p2
work: astrom-2021-feedbacksystems
unit: "15 Architecture and System Design (part 2/2): end of §15.4 to §15.8"
pages: 15-24 to 15-42
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Architecture and System Design, part 2: interaction, adaptation, learning, application fields

## L0 — One line
Building a control system loop by loop can create hidden interactions (measured by the relative gain array, and shown by parallel integrators), and when the process is uncertain the controller itself can adapt or learn (adaptive control, neural networks).

## L1 — The gist (≤ 120 words)
This part asks what goes wrong when many loops or actuators act on the same plant, and what to do when the plant model is poorly known. For interaction it gives the relative gain array, and an electric-car example showing that two parallel PI controllers create an unreachable, unobservable integrator mode. The remedy is one central integrator. For uncertainty it presents adaptive control (MRAC, self-tuning regulator, persistent excitation, dual control), a table-based learner (BOXES), neural networks and a convolutional network for object detection. It closes with four application fields (aerospace, automotive, process, telecom) and further reading.

**Prerequisites:** transfer functions and matrices; reachability/observability and pole–zero cancellation; PI control; least squares; gradient descent; basic probability.

## L2 — Key ideas (5–10 bullets)
- **Extremum seeking** perturbs the reference sinusoidally and uses the phase between the perturbation and the performance measure to move the reference toward the optimum (p. 15-24).
- **Relative gain array** $\Lambda = P\circ P^{-T}$ compares each open-loop gain with the gain when all other loops are perfectly controlled. Rows and columns sum to one, and it can be used for pairing inputs with outputs (pp. 15-25, 15-26).
- **Parallel actuators:** with proportional control, the gains set how the disturbance load is shared. Separate integrators on each actuator create an unreachable and unobservable mode, so use one central integrator (pp. 15-27 to 15-29).
- **Adaptive control** uses a second, slower loop that adjusts controller parameters (model reference adaptive control, MRAC, with the MIT rule; the self-tuning regulator with recursive estimation and certainty equivalence, i.e. treating the estimates as the true parameters) (pp. 15-29, 15-30).
- **Closed-loop estimation needs excitation.** If the only perturbation is the injected signal $\delta_1$ (with $r=v=w=0$), any model relating $u$ and $y$ gives $-1/C$; disturbances entering through the reference allow the process model to be estimated. Persistent excitation (a condition on how richly the control signal varies) determines how many parameters can be estimated reliably, and dual control (control that investigates as well as directs) introduces perturbations when natural disturbances do not excite the process enough (pp. 15-31 to 15-33).
- **Learning:** BOXES (a learning program that quantizes the state into boxes) stores a control law as a 225-entry table. Neural networks represent nonlinear functions more efficiently and are trained by gradient methods (pp. 15-33, 15-34, 15-35).
- A **convolutional network** composes convolution (feature-detecting filters), ReLU ($\max(x,0)$), max-pooling (down-sampling) and softmax (turning scores into probabilities) into a trainable sensor for object detection (pp. 15-36, 15-37).
- **Application fields** give a flavour of the systems, controllers and users in each area: aerospace, automotive, process industry, telecommunication (pp. 15-38 to 15-41).

## L3 — Walkthrough

*This part starts in the middle of §15.4 (end of the complementary-filter discussion) and runs to the end of §15.8.*

### 15.4 (end): complementary filtering, extremum seeking
**Complementary filter.** For exponential signals the filter recovering signal $x$ from two measurements $y_1, y_2$ is (p. 15-24)
$$y_f = \frac{1}{s+1}\,y_1 + \frac{s}{s+1}\,y_2 = G_1(s)y_1 + G_2(s)y_2. \tag{15.9}$$
Since $G_1(s)+G_2(s)=1$, the filter is called complementary (p. 15-24). Both complementary and Kalman filtering fuse several sensors and can be optimized if noise characteristics are known. Complementary filtering needs only a model of the sensor system. The Kalman filter needs a model of the whole system dynamics, but it can also use the control actions (p. 15-24).

**Extremum seeking (self-optimization).** Instead of holding the output at a constant reference, the controller changes the reference so that a performance criterion is optimized (p. 15-24).
- The reference $r$ is varied sinusoidally and the performance $j$ is observed (Fig. 15.20a).
- Near the optimum (B) the performance changes very little. It is in phase with the reference variation if $r$ is left of the maximum (A), and out of phase if $r$ is right of it (C). The phase difference tells how to move the reference (p. 15-24).
- Block diagram (Fig. 15.20b): a block PC computes $J$ from $u$ and $y$. A signal generator SG sends a sinusoid to the reference of the closed-loop system. The sinusoid is correlated with $J$, and a low-pass-filtered version goes to the reference. The perturbation should be slow enough that process dynamics can be neglected (p. 15-24).
- Other schemes exist that differ in how probing, analysis and action are done (p. 15-24).

*Intuition note.* Wiggle the setting a little and see whether the score moves with the wiggle or against it. Move the setting in the direction where the score rises with it.

### 15.5 Interaction
Building loop by loop can cause unintended interactions (p. 15-24). The section introduces the relative gain array (RGA) and then parallel systems (p. 15-24).

**The Relative Gain Array.** The pairing problem is to decide whether $y_i$ should be controlled by $u_j$ or by another input. The second problem is whether loops interact. Understanding the second also solves the first (p. 15-25).

Setup: $p$ inputs and $p$ outputs, transfer function matrix $P$, open-loop transfer function from input $j$ to output $i$ is $P_{ij}$ (p. 15-25).
- Simple situation: all other loops perfectly controlled, i.e. $y_k=0$ for $k\ne i$. Then $u_j=(P^{-1})_{ji}y_i$. The closed-loop transfer function from $u_j$ to $y_i$ is thus $1/(P^{-1})_{ji}$. (The page prints $y_j$ and $u_i$ at two places; see Reading notes.) (p. 15-25)
- Relative gain: the ratio of the transfer functions from $u_j$ to $y_i$ under open loop and under ideal closed-loop control (p. 15-25):
$$\lambda_{ij}=P_{ij}(P^{-1})_{ji}=P_{ij}(P^{-T})_{ij},\qquad \Lambda = P\circ P^{-T}. \tag{15.10}$$
Here $\circ$ is element-by-element (Hadamard) multiplication. $\Lambda$ is the RGA, or Bristol's RGA. It was derived for the steady state ($s=0$) and later extended to dynamics (p. 15-25).

**Example 15.2 (2×2 static system).** With $P=\begin{pmatrix}p_{11}&p_{12}\\p_{21}&p_{22}\end{pmatrix}$ and $P^{-1}=\frac{1}{p_{11}p_{22}-p_{12}p_{21}}\begin{pmatrix}p_{22}&-p_{12}\\-p_{21}&p_{11}\end{pmatrix}$, the text prints (p. 15-26)
$$\Lambda=\begin{pmatrix}1-\lambda&\lambda\\ \lambda&1-\lambda\end{pmatrix},\qquad \lambda=\frac{p_{11}p_{22}}{p_{11}p_{22}-p_{12}p_{21}}.$$
The interaction is characterized by one number $\lambda$, and all row and column sums are one (p. 15-26). (Added step: by (15.10), $\Lambda_{11}=p_{11}\cdot p_{22}/(p_{11}p_{22}-p_{12}p_{21})=\lambda$ and $\Lambda_{12}=p_{12}\cdot(-p_{21})/(p_{11}p_{22}-p_{12}p_{21})=1-\lambda$. So by the definition the diagonal entries are $\lambda$ and the off-diagonal entries $1-\lambda$, the reverse of the print; see Reading notes.)

**Properties.** Because $P^{-1}$ is the inverse, $\sum_{k=1}^n P_{ik}(P^{-1})_{kj}=\delta_{ij}$, and hence $\sum_{i=1}^n P_{ij}(P^{-1})_{ji}=1$ (the page writes $\delta_{ii}$). Row and column sums of $\Lambda$ are all one, so the interactions are characterized by $(n-1)^2$ elements: one for $2\times2$, four for $3\times3$ (p. 15-26).

**Static interpretation.** $\lambda_{ij}=1$ means no interaction, since open- and closed-loop gains are equal. The interaction increases the gain if $\lambda_{ij}<1$ and decreases it if $\lambda_{ij}>0$ (as printed; $>1$ is presumably meant). A negative $\lambda_{ij}$ means the interaction changes the sign of the gain (p. 15-26).

**Example 15.3 (pairing).** The static gain matrix and its RGA are (p. 15-26)
$$P=\begin{pmatrix}2.662&8.351&8.351\\0.382&-0.559&-0.559\\0&11.896&-0.351\end{pmatrix},\quad \Lambda=\begin{pmatrix}0.32&0.02&\mathbf{0.66}\\ \mathbf{0.68}&0.01&0.31\\0&\mathbf{0.97}&0.03\end{pmatrix}.$$
There is one largest entry in each row and column, giving the pairing $y_1{:}u_3$, $y_2{:}u_1$, $y_3{:}u_2$. These relative gains are reasonably large (p. 15-26).

Summary of the RGA (p. 15-26): it is dimension free, easy to compute, and gives insight into interaction and pairing. Analysis of $\Lambda(i\omega)$ gives insight into the frequency dependence of the interactions. It also tells which variables to group for multivariable control. Because it assumes perfect control of the other loops, it does not capture all aspects of interaction.

*Intuition note.* $\lambda_{ij}$ asks: how different is the gain from $u_j$ to $y_i$ once all the other loops are working perfectly? A value of exactly 1 means no interaction: open- and closed-loop gains are the same. The author also uses the largest entries of $\Lambda$ to choose pairings (Example 15.3).

**Parallel systems.** Several subsystems may control one variable: several heaters, motors on each wheel, a power grid with hundreds of sources (p. 15-27).

**Example 15.4 (electric car cruise control).** Two motors, linear motion, only gravity disturbance $F_d=mg\theta$. Model (p. 15-27):
$$m\frac{dv}{dt}=F_1+F_2-mg\theta. \tag{15.11}$$
- *Proportional controllers:* $F_1=k_{p1}(r-v)$, $F_2=k_{p2}(r-v)$ (15.12). Then $m\,dv/dt=k_p(r-v)-mg\theta$ with $k_p=k_{p1}+k_{p2}$. For constant $\theta$: $e_{ss}=r-v_{ss}=mg\theta/k_p$, and $F_{1,ss}=\frac{k_{p1}}{k_{p1}+k_{p2}}mg\theta$, $F_{2,ss}=\frac{k_{p2}}{k_{p1}+k_{p2}}mg\theta$. The gains thus decide how the compensation is distributed among the motors (p. 15-27).
- *A PI controller on each motor:*
$$m\frac{dv}{dt}=(k_{p1}+k_{p2})(r-v)+k_{i1}I_1+k_{i2}I_2-mg\theta,\quad \frac{dI_1}{dt}=r-v,\ \frac{dI_2}{dt}=r-v. \tag{15.13}$$
For constant $r,\theta$ the equilibrium has $v=r$ and constant $I_1,I_2$, which are not unique. They can have any values satisfying $k_{i1}I_1+k_{i2}I_2=mg\theta$ (printed with $k_pI_1$; see Reading notes). Infinitely many equilibria signal difficulty (pp. 15-27, 15-28).
- *Transfer functions* with $k_i=k_{i1}+k_{i2}$ (p. 15-28):
$$G_{vr}=\frac{k_ps+k_i}{ms^2+k_ps+k_i},\qquad G_{v\theta}=\frac{mgs}{ms^2+k_ps+k_i}. \tag{15.14}$$
$G_{vr}(0)=1$ and $G_{v\theta}(0)=0$, so there is no steady-state error to reference or slope.
- *Hidden mode.* (15.13) is third order and (15.14) second order, so a pole/zero cancellation occurred. The cancelled mode obeys $d(I_1-I_2)/dt=0$, an eigenvalue at the origin. The Kalman decomposition (Fig. 8.9a) has a first-order integrator subsystem that is neither reachable from $F_1,F_2$ nor observable from $v$. Two parallel systems with the same mode are a prototype of such a system (p. 15-28).
- *Simulation (Fig. 15.21a).* A pulse is applied at the input of wheel 1's PI controller. The error $e=r-v$ is well behaved and settles in about 10 time units. $F_1$ reacts quickly to reduce the disturbance but $F_2$ goes the opposite way. In steady state both forces are constant but have opposite signs: one wheel drives and the other brakes (pp. 15-28, 15-29).
- *Remedy:* one PI controller whose output is distributed, with $0<\alpha<1$ (p. 15-29):
$$F_1=\alpha\big(k_p(r-v)+k_iI\big),\quad F_2=(1-\alpha)\big(k_p(r-v)+k_iI\big),\quad \frac{dI}{dt}=r-v. \tag{15.15}$$
The closed loop is second order, $\ \dot v = k_p(r-v)+k_iI-mg\theta,\ \dot I=r-v$ (15.16; the printed left side lacks $m$). It has the same $G_{vr}$, $G_{v\theta}$ (15.14). In Fig. 15.21b both forces now collaborate against the disturbance. $e$ and $F_1+F_2$ are the same as with two PI controllers (p. 15-29).

**Generalization (author).** With proportional controllers on parallel systems, the gains determine how disturbance attenuation is divided. Integral control cannot be used in the individual subsystems. Use a central integrator and distribute its output to the subsystems' controllers (p. 15-29).

*Intuition note.* Two integrators fed by the same error give a mode ($I_1-I_2$, eigenvalue at the origin) that the speed error cannot see, because the speed depends only on the weighted sum $k_{i1}I_1+k_{i2}I_2$. A disturbance at one controller can leave the integrators at different values for good, and the forces then have opposite signs (one wheel drives, the other brakes). The author's remedy is one central integrator.

### 15.6 Adaptation and Learning
Definitions as given (p. 15-29): adaptation is adjusting to a specified use or situation. Learning is acquiring knowledge or skill by study, instruction or experience. Reasoning is seeking truth or knowledge by inferring from fact or logic. The author notes that human abilities are still far ahead of engineered systems (p. 15-29).

**Adaptive control.** It can be used when the process and environment vary significantly and neither robust control nor gain scheduling is applicable. Model reference control and the self-tuning regulator both have two loops: a conventional loop (process $P$, controller $C$) and a slower loop adjusting the controller parameters $\theta$ (Fig. 15.22) (p. 15-29).

*MRAC.* It is mainly for reference tracking. Blocks: the model $F_m$ (ideal response, shaped by requirements $R$), the controller $C$ with adjustable $\theta$, and the parameter adjustment mechanism PA. PA receives $u$, $y$ and the desired response $y_m$ and produces $\theta$. A simple rule is the "MIT rule" (p. 15-30):
$$\frac{d\theta}{dt}=-\gamma\, e\,\frac{\partial e}{\partial\theta},\qquad e=y_m-y, \tag{15.17}$$
where $\gamma$ is a parameter and $\partial e/\partial\theta$ a sensitivity derivative. Other rules exist, some from Lyapunov theory (p. 15-30).

*Self-tuning regulator (STR).* It is used for tracking and regulation. Blocks: $C$ with adjustable $\theta$, a recursive parameter estimator RPE (estimates process parameters from $u$ and $y$), and a controller design calculation CDC (finds controller parameters from them). It is common to treat estimates as the true parameters, the *certainty equivalence principle*. Uncertainty can be taken into account because many estimators also give parameter uncertainty (p. 15-30).

*Recursive least squares.* For the model (p. 15-31)
$$y_{t+1}=-a_1y_t-a_2y_{t-1}+\dots+b_1u_t+\dots+e_{t+1}=\varphi_t\theta+e_{t+1},\tag{15.18}$$
$\varphi_t=[-y_t\ -y_{t-1}\ \cdots\ u_t\ u_{t-1}\ \cdots]$, $\theta=[a_1\ a_2\ \cdots\ b_1\ b_2\ \cdots]^T$. The estimate minimizes the mean square error $\sum e_k^2$ and is given as printed by
$$\hat\theta_t=\hat\theta_{t-1}+K_t\big(y_t-\varphi_t\hat\theta_{t-1}^T\big),\quad K_t=P_t\varphi_t^T,\quad P_t=P_{t-1}\varphi_t^T(\lambda+\varphi_tP_{t-1}\varphi_t^T)^{-1}. \tag{15.19}$$
Shapes (added): $\varphi_t$ is $1\times n$, $\theta$ is $n\times1$, $K_t$ is $n\times1$, $P_t$ should be $n\times n$ (see Reading notes on the printed form). It is a special case of the Kalman filter, eq. (8.8) in §8.2. The parameter $\lambda$ controls how fast old data are forgotten. Variants: directional forgetting, and square-root algorithms that update the square root of $P$ (p. 15-31).

Applications: flight control, process control, wheel-slip control and other automotive uses (p. 15-31).

**Example 15.5 (adaptive ship steering).** A conventional autopilot is typically PID. The main disturbances are wind and waves, which can change a lot. An adaptive controller can model wave-generated forces and counteract them. The model is of form (15.18) with 4 $a$-parameters (constrained to contain an integrator) and 2 $b$-parameters. Sea trials: better than conventional in normal weather, substantially better in bad weather. Fig. 15.23 shows the Steermaster autopilot (developed by Kockums, now marketed by Northrop Grumman), each autopilot run about an hour on a 225000 ton tanker, wind about 10 knots. The adaptive autopilot has significantly smaller heading variations, corresponding to about 3% less fuel consumption (p. 15-31, 15-32).

**Estimation in closed loop.** Where excitation enters matters. In the loop of Fig. 15.3 with only the injected signal $\delta_1$ ($r=v=w=0$) (pp. 15-31, 15-32):
$$y=\frac{P}{1+PC}\delta_1,\qquad u=-\frac{CP}{1+PC}\delta_1\ \Rightarrow\ y=-\frac1{C(s)}u,$$
so any model relating $u$ and $y$ gives the negative inverse of the controller. If instead disturbances enter through $r$ (other inputs zero):
$$y=\frac{PC}{1+PC}F(s)r,\qquad u=\frac{C}{1+PC}F(s)r\ \Rightarrow\ y=P(s)u,$$
and the process model can be estimated (p. 15-32).

**Persistent excitation.** A signal $u$ is persistently exciting of order $n$ if (p. 15-32)
$$U=\lim_{t\to\infty}\frac1T\int_0^T\big(A(p)u(k)\big)^2>0$$
for all nonzero polynomials $A$ in $p=d/dt$ of degree $\le n-1$. It determines how many parameters can be reliably estimated. A constant is persistently exciting of order 1, a sinusoid of order two. Load disturbances are particularly harmful; a scheme to detect them is cited. To obtain reliable estimates it is necessary to monitor the excitation and only update parameters when excitation is sufficient (p. 15-32).

**Dual control.** Feldbaum stressed that control should be investigating as well as directing and coined the term dual control. Using optimal stochastic control, the controller actively introduces perturbations when natural disturbances do not excite the process enough. The *hyper state* is the conditional probability distribution of the regular states and the parameters. Exact computation is possible only in simple cases, so many heuristic schemes exist. In machine learning this approach is called reinforcement learning (pp. 15-32, 15-33).

*Intuition note.* A controller that never disturbs the plant may learn nothing about it. Dual control, as described by the author, introduces perturbations on purpose when natural disturbances do not excite the process enough.

**Learning.** A nonlinear function with a learning mechanism is a simple learning system. In *supervised learning* the function is built from many arguments with their function values. In *reinforcement learning* a criterion of good fit is given, and learning selects random arguments and changes the function until the fit is good. Representation is a central issue. A simple representation quantizes the variables (p. 15-33).

**Example 15.6 (Michie's BOXES).** Michie and Chambers' game-playing program, applied to stabilizing an inverted pendulum on a cart (Fig. 7.2b); cart position, velocity, pendulum angle and angular velocity are measured; the control law is $f:\mathbb R^4\to\mathbb R$ (p. 15-33).
- Quantization: 5 levels for position and angle, 3 for each velocity, and 2 control levels (left L / right R). The table has $5\times5\times3\times3=225$ entries.
- Each entry holds five numbers: LL, RL (left/right life), LU, RU (left/right usage) and T (target, related to the current mean stabilization time). Life is a weighted average of how many times the entry was used before failure; usage is a weighted number of uses before failure.
- The action on entering a box is a heuristic function of LL, RL, LU, RU, T. The table starts with random numbers and is updated over experiments.
- Typical experiment: pendulum stabilized in 25 minutes after a 60-hour training period (p. 15-33).

The author remarks that this is not the best case for learning: a student could design a stabilizing controller in under an hour, and a conventional design avoids the crude quantization. Machine learning has developed much since the late 1960s (p. 15-33).

**Neural networks.** A drawback of BOXES is that gridding needs very large tables. An artificial neural network is a more efficient representation (p. 15-34). Neuron model, with weights $w_i$ (p. 15-34):
$$y=g\Big(\sum_{k=1}^n w_iu_i\Big). \tag{15.20}$$
$g$ was originally sigmoid, e.g. $\tanh x$ or $(1+e^{-x})^{-1}$. Others now used: $\max(0,x)$, $e^{-x^TQx}$, $(1+x^TQx)^{-1}$. A layered network such as Fig. 15.24 represents $f:\mathbb R^3\to\mathbb R^2$ as
$$f(u)=g\Big(W^{(3)}g\big(W^{(2)}g(W^{(1)}u)\big)\Big), \tag{15.21}$$
$W^{(k)}$ is the weight matrix to layer $k$, and $g$ is applied element-wise to vectors. In Fig. 15.24 the layers have 3, 4, 4 and 1 nodes, so the shapes would be $W^{(1)}$ $4\times3$, $W^{(2)}$ $4\times4$, $W^{(3)}$ $1\times4$ (read off the figure; the text says output in $\mathbb R^2$). Kolmogorov proved that any continuous function on a finite cube can be represented by a network with one hidden layer. Håstad clarified the strong advantage of many layers (p. 15-34).

Weights $w^{(k)}_{ij}$ are found by matching many arguments to function values. A useful feature is that both the function and its inverse can be generated from data (pp. 15-34, 15-35). For a single neuron the gradient algorithm is
$$w_i(k+1)=w_i(k)+\gamma u_i^0(k)\big(y^0(k)-y(k)\big), \tag{15.22}$$
with training data $u^0,y^0$ and $y$ from (15.20) with $u=u^0$. It approximates a gradient scheme for minimizing the mean square error and is similar to the MIT rule (15.17). In neurophysiology it is known as Hebb's rule. Multi-layer networks are updated by gradient descent, with the gradient computed by back propagation (p. 15-35).

**Deep learning.** Networks with many layers are useful for preprocessing data from information-rich sensors (cameras, spectrometers), e.g. recognizing and tracking objects in autonomous driving (p. 15-35). Object recognition in Fig. 15.25 uses a convolutional neural network (CNN). An image is an $m\times n$ array with an extra index $k$ for colour or feature planes. ANNs have two operations (weighted sum and monotone scalar function); CNNs have more (p. 15-35). The operations (p. 15-36):
- Convolution $C$: $y(i,j,k)=w_o(k)+\sum_u\sum_v\sum_l x(i-u,j-v,l)\,w(u,v,l,k)$, with bias $w_o$ and weights $w$. It detects features (edges, corners, wheels, cars, ...).
- ReLU $R$: $y(i,j,k)=\max\big(x(i,j,k),0\big)$, element-wise, same size.
- Max-pooling $P$: from size $m\times n\times k$ to $m/2\times n/2\times k$,
$y(i,j,k)=\max\big(x(2i,2j,k),x(2i-1,2j,k),x(2i,2j-1,k),x(2i-1,2j-1,k)\big)$. It reduces dimension but keeps the most important features. Minimum and average pooling also exist.
- Softmax $S$: $y(i,j,k)=\dfrac{e^{x(i,j,k)}}{\sum_l e^{x(i,j,l)}}$, $\sum_k y(i,j,k)=1$. Outputs lie in $[0,1]$ and indicate the subjective probability of object $k$ at position $ij$. It is typically used in the final layer.

Parameters appear only in the convolution layers and are found by optimization on large training sets. Choosing array sizes, number of layers and operator order is an art needing experience (p. 15-36).

*The network of Fig. 15.25/15.26.* The input is a $300\times300$ RGB box; the output is three $20\times20$ images (car, bicycle, person). It has 25 million parameters (p. 15-36). With $f\circ g(x)=f(g(x))$ it is
$$Q=S\circ C\circ R\circ C\circ(P\circ R\circ C)^3,$$
a composition of 13 functions. The first part creates many patterns with $C,R,P$; recognition is done by $S\circ C\circ R\circ C$ (pp. 15-36, 15-37). Different kernels detect different features, each stored in its own layer. The $C,R,P$ block is repeated to create more features (p. 15-37). A camera with a CNN can be seen as a trainable sensor that detects, classifies and positions objects in real time. Computations are fast and parallelizable, and the trained network runs at 60 Hz on a standard PC with an NVIDIA Titan X card (p. 15-37). The text there says the network behind Fig. 15.25 has more than 12 million parameters and estimates 11 objects (p. 15-37).

*Intuition note.* A CNN is a long chain of simple steps: slide small filters over the image, keep positive responses, shrink the image, and finally turn scores into probabilities. Parameters appear only in the convolution layers and are found by optimization on large training sets (p. 15-36).

### 15.7 Control design in common application fields
Control is called a "hidden technology" because it is used practically everywhere without being noticed (p. 15-37). Four fields follow.

**Aerospace.** Early user of control; Sperry's autopilot 1914, autonomous flight 1947. About 2500 aircraft produced in 2015, revenue over 20 billion dollars. Users are highly skilled pilots and astronauts who influence the system directly in many ways (Apollo 13 is mentioned). The industry drove redundancy, simulation and model-based engineering, accelerometers and gyroscopes, anti-lock braking (aircraft 1929), extremum control (aircraft engines 1951), gain scheduling and adaptive control, optimal control and Kalman filtering in space efforts, nonlinear control of satellites, and unmanned air vehicles (operational 1970) (p. 15-38).

**Automotive.** A multi-trillion dollar business dominated by six large companies. Used by ordinary people who change modes and setpoints. Control runs on electronic control units (ECUs); modern cars have more than 100. Computer control began in the late 1970s for emission requirements, then suspension control, ABS, EBS, ESC (p. 15-38). Adaptive cruise control uses radar; collision avoidance, parking assist and autonomous driving follow (p. 15-39). Model-based engineering (the Toyota Prius is an example) and supplier-supplied validated models are used. The AUTOSAR partnership, formed 2003, standardizes software architecture for modularity, scalability and reuse. The mass market stimulated cheap sensors, microcontrollers and the PLC (p. 15-39). General Motors asked for a standard machine controller to replace relays, which gave the PLC. Its architecture uses round-robin schedulers with different cycle rates; languages are ladder diagrams, function block diagrams, sequential function charts and structured text (p. 15-39).

**Process industry.** Automation is delivered by specialized companies (Taylor Instruments 1851, Foxboro 1908). It is a 100 billion dollar industry; distributed control systems (DCS) are about 20% of the market and five suppliers hold over 50%. Analog controllers were replaced by DCS and relay logic by PLCs. A DCS is a toolbox for connecting sensors, actuators and algorithms; ExxonMobil has contracted Lockheed Martin to specify an open, secure, standards-based next generation (pp. 15-39, 15-40). Plants have thousands of sensors and actuators on standardized networks (IEC 61784). Valves are common actuators, with cascade control: inner valve-positioner loops reduce friction and nonlinearity, and outer loops control pressure, temperature and quality. Users: plant managers, process engineers, instrument engineers, operators. Standards come from ISA and IEC (p. 15-40). About 97% of controllers are PID, only a small fraction with derivative action; a study of 100 boiler-turbine units in Guangdong found 94.4% PI, 3.7% PID, 1.9% advanced. Cascade, selector, midrange control, gain scheduling, automatic tuning and MPC are common. MPC emerged at Shell as dynamic matrix control (p. 15-40).

**Telecommunication.** Black's negative feedback amplifier was inspired by long-distance telephony. About 7.4 billion mobile subscriptions at the start of 2016; IoT devices were expected to pass that by 2018. Mobile phones reduced sensor costs (camera, GPS, accelerometer, gyro) by orders of magnitude, with reuse in other fields (e.g. virtual reality). Standardization is extensive (3GPP: GSM, WCDMA, LTE, future 5G; IEEE 802.11). Control acts from analog amplifier linearity and efficiency to choice of transmission power and coding. PID is often used with gain scheduling and simple adaptive schemes (p. 15-41).

### 15.8 Further reading
Pointers only (p. 15-42): [CCS15] on architecture; [ÅH06] on PID and bottom-up architectures; internal model control [BT78] and internal model principle [FW76]; Smith predictor and posicast control by O. J. M. Smith; decoupling [Wad97], [HK83]; RGA [Bri66], [McA83]; gain scheduling, which still dominates flight control; adaptive control and system identification [Lju99a]. Neural-network history: Rosenblatt's perceptron, Widrow's Adaline, Minsky–Papert's criticism (called "severe and partially unfair"), backpropagation [RHW86] (said to be closely related to dynamic programming), and the ImageNet benchmark. Classification error fell from about 30% in 2010 to 3% in 2016. AlphaGo uses Monte Carlo tree search with knowledge from machine learning.

## Toy example (ours, not from the text)
Take the static plant $P=\begin{pmatrix}2&1\\1&1\end{pmatrix}$.
1. Determinant: $2\cdot1-1\cdot1=1$. So $P^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$, which is symmetric, so $P^{-T}=P^{-1}$.
2. $\Lambda=P\circ P^{-T}$: $\Lambda_{11}=2\cdot1=2$, $\Lambda_{12}=1\cdot(-1)=-1$, $\Lambda_{21}=1\cdot(-1)=-1$, $\Lambda_{22}=1\cdot2=2$. So $\Lambda=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$. Row and column sums are 1.
3. Check with Example 15.2: $\lambda=p_{11}p_{22}/\det=2/1=2$, and the diagonal is $\lambda=2$, the off-diagonal $1-\lambda=-1$.
4. Meaning for the pairing $y_1{:}u_1$: open-loop gain 2; with $y_2=0$ held perfectly, $u_1=(P^{-1})_{11}y_1=1\cdot y_1$, so the gain is $1/1=1$. Ratio $=2$, so closing the other loop halves the gain. For the pairing $y_1{:}u_2$: open-loop gain $P_{12}=1$, ideal closed-loop gain $1/(P^{-1})_{21}=-1$, ratio $-1$, so interaction flips the sign. Pair the diagonal.

## Concepts
- [[relative-gain-array]] (new) — $\Lambda=P\circ P^{-T}$; ratio of open-loop gain to gain with other loops perfectly controlled (p. 15-25)
- [[complementary-filter]] (new) — fuse two sensors with filters $G_1+G_2=1$ (p. 15-24)
- [[extremum-seeking]] (new) — perturb the reference sinusoidally and use phase to climb to the optimum (p. 15-24)
- [[parallel-subsystems-central-integrator]] (new) — parallel actuators with separate integrators leave an unreachable, unobservable mode; use one integrator (p. 15-29)
- [[controllability]] / [[observability]] — here: the cancelled mode $I_1-I_2$ is neither reachable from the forces nor observable from $v$ (p. 15-28)
- [[eigenvalues-and-modes]] — the cancelled mode has an eigenvalue at the origin (p. 15-28)
- [[integral-action]] — drives steady-state error to zero ($G_{v\theta}(0)=0$) (p. 15-28)
- [[pid-control]] — the dominant controller in process industry (p. 15-40)
- [[model-reference-adaptive-control]] (new) — adjust $\theta$ so the output follows the model $F_m$; MIT rule (p. 15-30)
- [[self-tuning-regulator]] (new) — recursive estimator plus controller design block (p. 15-30)
- [[certainty-equivalence]] (new) — treat estimated parameters as true in design (p. 15-30)
- [[recursive-least-squares]] (new) — recursive estimate, special case of the Kalman filter (p. 15-31)
- [[persistent-excitation]] (new) — signal condition limiting the number of reliably estimable parameters (p. 15-32)
- [[dual-control]] (new) — control that both investigates and directs; hyper state is a conditional distribution (p. 15-32)
- [[artificial-neural-network]] (new) — layered composition of weighted sums and monotone functions (p. 15-34)
- [[convolutional-neural-network]] (new) — composition of $C$, $R$, $P$, $S$ operators (p. 15-36)
- [[model-predictive-control]] — originated at Shell as dynamic matrix control (p. 15-40)

## Canonical instances
- [[rga-3x3-pairing-example]] — largest RGA entries give pairing $y_1{:}u_3$, $y_2{:}u_1$, $y_3{:}u_2$ (p. 15-26)
- [[electric-car-two-motors-cruise-control]] — two PI controllers give steady-state wheel forces of different signs, so one wheel drives and the other brakes (pp. 15-28, 15-29)
- [[adaptive-ship-steering]] — adaptive autopilot, smaller heading variation, about 3% less fuel (p. 15-31)
- [[boxes-pendulum-learning]] — 225-entry table learns to balance a pendulum (p. 15-33)
- [[cnn-object-detection]] — 13-function composition detecting car, bicycle, person (p. 15-36)

## Bridges (candidates)
- [same-math] Recursive least squares (15.19) ↔ Kalman filter: the author states RLS is a special case of the Kalman filter (§8.2).
- [structural-analogy] MIT rule (15.17) ↔ neuron gradient rule (15.22): both adjust parameters along the error times a sensitivity or input, as the author notes.
- [structural-analogy] Dual control ↔ exploration vs exploitation: both trade immediate performance against information gain; the author links dual control to reinforcement learning.
- [structural-analogy] Backpropagation ↔ principle of optimality / dynamic programming: the author says they are closely related.
- [structural-analogy] Complementary filter ↔ Kalman filter: both fuse sensors; the former needs only a sensor model.

## Questions this raises
- How does the dynamic RGA $\Lambda(i\omega)$ change the pairing choice when low- and high-frequency gains differ?
- When several actuators share a load with one central integrator, how should $\alpha$ be chosen?
- How can one tell in practice that excitation is "sufficient" before updating parameters in a self-tuning regulator?
- When does a learned table or network beat a conventional design, given the BOXES comparison?

## Reading notes
- **Pages and numbering.** The labels give no printed number, but the page images show chapter-based page numbers "15-24" to "15-42". Citations use these, e.g. (p. 15-24). Offset: printed 15-N = pdf (498 + N), so pdf 522–540 = 15-24 to 15-42.
- **Where the part starts and ends.** It starts mid-§15.4 (end of complementary filtering, eq. 15.9; the earlier definitions of $y_1$, $y_2$ are not in these pages) and ends at the end of §15.8 Further Reading. Source notes: split at a section boundary.
- **Misprints and inconsistencies seen in the images:**
  - RGA derivation (p. 15-25): the text says "from $u_j$ to $u_i$" and "$u_j$ to $y_j$"; by context $y_i$ is meant.
  - Example 15.2 (p. 15-26): the matrix is printed with $1-\lambda$ on the diagonal and $\lambda$ off the diagonal, with $\lambda=p_{11}p_{22}/\det$. By (15.10) the diagonal is $\lambda$. The accompanying sentence repeats "diagonal elements equal $1-\lambda$".
  - Sum on p. 15-26: $\delta_{ii}$ appears where the summed index is $i$ and the fixed index is $j$.
  - Static interpretation (p. 15-26): "decreases the gain if $\lambda_{ij}>0$" is printed. $>1$ is presumably meant.
  - Equilibrium condition (p. 15-27): printed "$k_pI_1+k_{i2}I_2=mg\theta$". It should be $k_{i1}I_1+k_{i2}I_2$.
  - (15.16): the left side $dv/dt$ lacks the factor $m$.
  - (15.19) on p. 15-31: $\varphi_t\hat\theta_{t-1}^T$ is dimensionally inconsistent with $\theta$ a column vector. The printed $P_t$ formula would give an $n\times1$ object, not an $n\times n$ matrix. I copied the print.
  - Persistent excitation (p. 15-32): the limit is over $t$ but the integral is to $T$, and the argument is written $u(k)$.
  - (15.20): the sum index is $k$ but the summand uses $i$.
  - Fig. 15.24 caption says "a hidden layer", but the figure shows two hidden layers and one output node, while the text says $\mathbb R^3\to\mathbb R^2$.
  - Parameter counts: the Fig. 15.25 caption and p. 15-36 say 25 million parameters; p. 15-37 says more than 12 million.
  - "Unsupervised learning" (p. 15-33) is used for BOXES, though only supervised and reinforcement learning are defined there.
  - A citation is empty on p. 15-42 ("well described in []"). The MRAC figure shows a garbled label "$y_t extm$" for $y_m$.
- Figure/equation page images were checked for all equations above. No exercises appear in this part.
