---
id: boyd-2018-vmls/ch09-linear
work: boyd-2018-vmls
unit: "Chapter 9 — Linear dynamical systems"
pages: 163-175
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Linear dynamical systems

## L0 — One line
A system whose next state is a matrix times its current state (plus optional input and offset) can be simulated by repeated matrix–vector multiplication, and many real processes can be described this way, at least approximately.

## L1 — The gist (≤ 120 words)
A linear dynamical system describes a quantity that changes over time by one rule. The next state is a matrix times the current state, optionally plus an input term and an offset (extra terms for outside factors). The chapter asks how real processes fit this form. It builds four models: an age-structured population, an epidemic, a mass moving under force (using Euler's method to turn differential equations into a recursion), and a supply chain on a network. Once the matrices and the current state are known, iterating the update predicts the future and supports "what if" experiments. The chapter notes that such models may be only approximations, so results must be interpreted with care.

**Prerequisites:** matrix–vector multiplication; block matrices; the incidence matrix of a directed graph (book §7.3); the idea of a derivative as a rate of change.

## L2 — Key ideas (5–10 bullets)
- The state $x_t$ holds all information needed to determine the future, so, given the dynamics matrices, past states are not needed; the update is $x_{t+1}=A_tx_t$ (p. 163).
- Inputs and offsets extend the model to $x_{t+1}=A_tx_t+B_tu_t+c_t$, modelling outside influences (p. 164).
- A K-Markov (auto-regressive) model, where the next state depends on K−1 previous states as well as the current one, can be reduced to a standard linear dynamical system by choosing a bigger state (p. 164; exercise 9.4, p. 175).
- Simulation means iterating the update; it gives predictions and what-if analyses, but to the extent that the model only approximates the real system, results must be interpreted with care (p. 164).
- Population dynamics: births form the first row of $A$, survival rates $1-d_i$ the diagonal just below the main one (the subdiagonal); immigration enters as an added input vector, i.e. $B=I$ (pp. 165–167).
- Epidemic dynamics: the fractions in four infection states evolve through a $4\times4$ matrix whose entries are daily transition fractions (p. 168).
- The Euler method replaces derivatives by finite differences (change over one small time step divided by the step size), turning Newton's law for a mass into $x_{k+1}=Ax_k+Bf_k$ (pp. 169–170).
- Supply chain: $x_{t+1}=x_t+A^{\rm sc}f_t+p_t-s_t$ is a linear system with input $(f_t,p_t)$ and offset $-s_t$ (pp. 171–173).

## L3 — Walkthrough

### 9.1 Linear dynamical systems (pp. 163–164)
- **State and trajectory.** $x_1,x_2,\dots$ is a sequence of $n$-vectors; the subscript $t$ is time. $x_t$ is the *state* at time $t$; the sequence is a *trajectory* (p. 163). Examples: a daily portfolio, positions and velocities of a mechanical system, quarterly economic activity. If $x_t$ is a portfolio, $(x_5)_3$ is the amount of asset 3 held on day 5 (p. 163).
- **Definition.** A linear dynamical system makes each $x_{t+1}$ a linear function of $x_t$ (p. 163):
$$x_{t+1}=A_tx_t,\quad t=1,2,\dots \tag{9.1}$$
  The $n\times n$ matrices $A_t$ are the *dynamics matrices*; (9.1) is the *dynamics* or *update equation*. If $A_t$ does not depend on $t$, the system is *time-invariant* (p. 163).
- Knowing $x_t$ (and $A_t,A_{t+1},\dots$) gives all future states by iterating (9.1). Past states are not needed, which is why $x_t$ is called the state (p. 163).

*Intuition note.* The state is a complete summary of the past, as far as the future is concerned. One matrix multiplication moves the system one step forward.

- **With input** (p. 164):
$$x_{t+1}=A_tx_t+B_tu_t+c_t \tag{9.2}$$
  $u_t$ is the $m$-vector *input* (also called *exogenous variable*, since, roughly speaking, it comes from outside the system), $B_t$ is the $n\times m$ *input matrix*, $c_t$ is the $n$-vector *offset* (p. 164).
- **Markov model.** (9.1) is sometimes called a Markov model: the next state depends on the current one and not on earlier states. A (linear) *K-Markov model* lets $x_{t+1}$ depend on the current state and $K-1$ previous states (p. 164):
$$x_{t+1}=A_1x_t+\cdots+A_Kx_{t-K+1},\quad t=K,K+1,\dots \tag{9.3}$$
  with $n\times n$ matrices $A_1,\dots,A_K$. In time series analysis and econometrics these are called (vector) *auto-regressive models*. For $K=1$ it equals a time-invariant system (9.1). For $K>1$ it can be reduced to (9.1) with an appropriately chosen state (exercise 9.4) (p. 164).
- **Simulation.** Given the matrices and the state at time $t$, iterate (9.1) (or (9.2) if the inputs are also known) to get $x_{t+1},x_{t+2},\dots$. This makes predictions. Since (9.1) may only approximate a real system, results must be interpreted carefully. *What-if simulations* test changes in the system or particular inputs (p. 164).

### 9.2 Population dynamics (pp. 164–167)
- **Setup.** $x_t$ is a 100-vector; $(x_t)_i$ is the number of people of age $i-1$ in year $t$. Treating counts as real numbers is acceptable at this scale. People aged 100 or older are not tracked (p. 165).
- **Rates.** The birth-rate vector $b$: $b_i$ is the average number of births per person of age $i-1$. This is half the births per woman, assuming equal numbers of men and women. $b_i\approx0$ for $i<13$ and $i>50$. The death-rate vector $d$: $d_i$ is the portion of those aged $i-1$ who die this year (p. 165).
- **Derivation** (births and deaths only, no immigration) (p. 165):
$$(x_{t+1})_1=b^Tx_t,\qquad (x_{t+1})_{i+1}=(1-d_i)(x_t)_i,\ i=1,\dots,99.$$
  Assembled into
$$x_{t+1}=Ax_t \tag{9.4}$$
$$A=\begin{bmatrix} b_1&b_2&b_3&\cdots&b_{98}&b_{99}&b_{100}\\ 1-d_1&0&0&\cdots&0&0&0\\ 0&1-d_2&0&\cdots&0&0&0\\ \vdots&\vdots&\vdots&&\vdots&\vdots&\vdots\\ 0&0&0&\cdots&1-d_{98}&0&0\\ 0&0&0&\cdots&0&1-d_{99}&0\end{bmatrix}$$
  ($100\times100$; first row $b^T$, subdiagonal $1-d_i$) (p. 167).
- **Use.** Predicting total population in 10 years, school-age children, retirement-age adults. Figure 9.4 shows the predicted 2020 US age distribution, from iterating $x_{t+1}=Ax_t$ for $t=1,\dots,10$, starting at the 2010 distribution (Figure 9.1). It assumes no immigration and constant birth and death rates (Figures 9.2, 9.3) (p. 167). Such models project the number of retirees and run what-if analyses of changed birth or death rates (p. 167).
- **Immigration.** Add a 100-vector $u_t$: $x_{t+1}=Ax_t+u_t$, which is (9.2) with $B=I$. $(u_t)_i$ is the number of immigrants of age $i-1$ in year $t$; negative entries mean net emigration (p. 167).

*Intuition note.* Each column of $A$ says where people of one age go next year: older by one year (if they survive) and, for the first row, how many babies they produce.

### 9.3 Epidemic dynamics (pp. 168–169)
- Nonlinear epidemic models also exist; this is a simple linear one (p. 168). $x_t$ is a 4-vector of population fractions: *susceptible*, *infected*, *recovered (and immune)*, *deceased*. Example: $x_t=(0.75,0.10,0.10,0.05)$ means 75% susceptible, 10% infected, 10% recovered, 5% deceased (p. 168).
- **Assumptions per day** (p. 168): 5% of susceptibles become infected (95% stay susceptible). Of the infected, 1% die, 10% recover with immunity, 4% recover without immunity (become susceptible), and 85% remain infected. Recovered and deceased stay in their states.
- **Derivation** (p. 168):
  - $(x_{t+1})_1=0.95(x_t)_1+0.04(x_t)_2$ (susceptibles who stay susceptible, plus infected who recover without immunity).
  - $(x_{t+1})_2=0.85(x_t)_2+0.05(x_t)_1$.
  - $(x_{t+1})_3=(x_t)_3+0.10(x_t)_2$.
  - $(x_{t+1})_4=(x_t)_4+0.01(x_t)_2$.
$$x_{t+1}=\begin{bmatrix}0.95&0.04&0&0\\0.05&0.85&0&0\\0&0.10&1&0\\0&0.01&0&1\end{bmatrix}x_t$$
- **Simulation** (Figure 9.5, initial condition $x_0=(1,0,0,0)$): after around 100 days the state converges to one with a little under 10% of the population deceased and the remaining population immune (p. 168).

### 9.4 Motion of a mass (pp. 169–171)
- **Physics.** A mass $m>0$ moves on a line with position $p(\tau)$ ($\tau$ continuous), external force $f(\tau)$, and drag coefficient $\eta>0$. Newton's law (p. 169):
$$m\frac{d^2p}{d\tau^2}(\tau)=-\eta\frac{dp}{d\tau}(\tau)+f(\tau).$$
  The drag force is proportional to velocity and opposite in direction. With velocity $v=dp/d\tau$ this becomes two coupled equations (p. 170):
$$\frac{dp}{d\tau}=v,\qquad m\frac{dv}{d\tau}=-\eta v+f.$$
- **Discretization.** Choose a sampling interval $h>0$ small enough that velocity and forces change little over $h$ seconds. Define $p_k=p(kh)$, $v_k=v(kh)$, $f_k=f(kh)$ and use (p. 170)
$$\frac{dp}{d\tau}(kh)\approx\frac{p_{k+1}-p_k}{h},\qquad \frac{dv}{d\tau}(kh)\approx\frac{v_{k+1}-v_k}{h}. \tag{9.5}$$
  Replacing $\approx$ by $=$: $\frac{p_{k+1}-p_k}{h}=v_k$ and $m\frac{v_{k+1}-v_k}{h}=f_k-\eta v_k$.
  (added step) Solving: $p_{k+1}=p_k+hv_k$ and $v_{k+1}=(1-h\eta/m)v_k+(h/m)f_k$.
- **Result.** With state $x_k=(p_k,v_k)$ (p. 170):
$$x_{k+1}=\begin{bmatrix}1&h\\0&1-h\eta/m\end{bmatrix}x_k+\begin{bmatrix}0\\h/m\end{bmatrix}f_k,\quad A=\begin{bmatrix}1&h\\0&1-h\eta/m\end{bmatrix},\ B=\begin{bmatrix}0\\h/m\end{bmatrix}.$$
  This is of the form (9.2) with input $f_k$. It is approximate because of (9.5), but accurate for small enough $h$. The approximation (9.5) is the *Euler method*; more sophisticated methods exist (p. 170).
- **Example** (p. 171): $m=1$ kg, $\eta=1$, $h=0.01$ s. Force: $0$ on $[0,0.5)$, $1.0$ on $[0.5,1.0)$, $-1.3$ on $[1.0,1.4)$, $0$ from $1.4$ on. Simulate 6 seconds from $x_1=(0,0)$ (at rest at position 0), iterating from $k=1$ to $k=600$. Figure 9.7 shows force, position, velocity.

*Intuition note.* Euler's method treats the rate of change as roughly constant over one small step (the text asks that $h$ be small enough that velocity and forces do not change very much). Then "new = old + $h\times$ rate" is a matrix–vector update.

### 9.5 Supply chain dynamics (pp. 171–173)
- **Setup.** One divisible commodity is stored at $n$ locations. $x_t$ ($n$-vector) holds *deviations* of levels from target levels; positive means more than target (p. 171). Purchases $p_t$ and sales $s_t$ are $n$-vectors (negative if returns are included); $(p_t-s_t)_i$ is the amount added at location $i$ (p. 171).
- **Links.** $m$ transportation links are described by the $n\times m$ incidence matrix $A^{\rm sc}$ (§7.3). Link direction is only a reference direction: flow along it is positive, opposite is negative. $f_t$ is the $m$-vector of flows, e.g. $(f_6)_2=-1.4$ means 1.4 units moved on link 2 against its direction. $A^{\rm sc}f_t$ is the net inflow to each location (p. 171).
- **Dynamics** (p. 173):
$$x_{t+1}=x_t+A^{\rm sc}f_t+p_t-s_t,\quad t=1,2,\dots$$
  In a controlled chain, $s_t$ is beyond our control, while $f_t$ and $p_t$ can be chosen. So treat $s_t$ as the offset and $u_t=(f_t,p_t)$ as the input in (9.2), with $A=I$, $B=[A^{\rm sc}\ \ I]$. ($A^{\rm sc}$ is the incidence matrix; $A$ is the dynamics matrix.) Then $x_{t+1}=Ax_t+B(f_t,p_t)-s_t$ (p. 173).
- **Example** (Figure 9.8: $n=3$, $m=3$) (p. 173):
$$x_{t+1}=x_t+\begin{bmatrix}-1&-1&0&1&0&0\\1&0&-1&0&1&0\\0&1&1&0&0&1\end{bmatrix}\begin{bmatrix}f_t\\p_t\end{bmatrix}-s_t.$$
  The author suggests checking that the product gives the commodity added at each location by shipping and purchasing (p. 173).

*Intuition note.* In the Figure 9.8 example, each column of $A^{\rm sc}$ has $-1$ at the node a link leaves and $+1$ at the node it enters (see the matrix above). So a positive flow on that link takes from one location and gives to another.

## Toy example (ours, not from the text)
Three age groups (young, adult, old) with $x_t=(\text{young},\text{adult},\text{old})$:
$$A=\begin{bmatrix}0&1&0.5\\0.8&0&0\\0&0.5&0\end{bmatrix},\quad x_1=(10,20,30).$$
Row 1: births (each adult yields 1 baby, each old person 0.5). Row 2: 80% of young survive into the adult group. Row 3: 50% of adults survive into the old group.
- $x_2=Ax_1$: row 1 $=0\cdot10+1\cdot20+0.5\cdot30=35$; row 2 $=0.8\cdot10=8$; row 3 $=0.5\cdot20=10$. So $x_2=(35,8,10)$.
- $x_3=Ax_2$: row 1 $=0\cdot35+1\cdot8+0.5\cdot10=13$; row 2 $=0.8\cdot35=28$; row 3 $=0.5\cdot8=4$. So $x_3=(13,28,4)$. Computing $x_3$ used only $x_2$, not $x_1$: the state suffices.
- With input $u=(1,0,0)$ (one newcomer per period), $B=I$: $x_2=Ax_1+u=(36,8,10)$.

## Concepts
- [[linear dynamical system]] (new) — $x_{t+1}=A_tx_t$: next state is a linear function of the current state (p. 163)
- [[state / trajectory]] (new) — $x_t$ holds all information needed for the future; the sequence $x_1,x_2,\dots$ is the trajectory (p. 163)
- [[time-invariant system]] (new) — a linear dynamical system whose dynamics matrix does not depend on $t$ (p. 163)
- [[input, offset]] (new) — extra terms $B_tu_t+c_t$; $u_t$ is an outside (exogenous) $m$-vector input (p. 164)
- [[Markov model / K-Markov (auto-regressive) model]] (new) — next state depends on the current state only, or on it and $K-1$ previous states (p. 164)
- [[simulation]] (new) — iterating the update equation to predict future states; used for what-if analysis (p. 164)
- [[Euler method / discretization]] (new) — replacing derivatives by finite differences over step $h$, giving a recursion (p. 170)
- [[matrix as transformation]] — here, $A$ maps today's state to tomorrow's (p. 163)
- [[matrix multiplication as composition]] — implicitly: iterating the update applies $A$ repeatedly (p. 163)
- [[incidence matrix]] — $A^{\rm sc}$, $n\times m$; converts link flows into net inflow at nodes (p. 171)

## Canonical instances
- [[population-dynamics-model]] — age-structured population with birth-rate row and survival subdiagonal (p. 165)
- [[epidemic-dynamics-model]] — susceptible/infected/recovered/deceased fractions evolving by a $4\times4$ matrix (p. 168)
- [[mass-on-a-line]] — Newton's law with drag, discretized by Euler's method (p. 170)
- [[supply-chain-dynamics]] — warehouse level deviations driven by flows (via incidence matrix), purchases and sales (p. 173)

## Bridges (candidates)
- [same-math] Epidemic matrix ↔ Markov (stochastic) matrix: each column of the $4\times4$ matrix is non-negative and sums to 1 (0.95+0.05; 0.04+0.85+0.10+0.01; 1; 1). This is our observation, not stated in the unit.
- [structural-analogy] Dynamics matrix $A$ ↔ eigen-decomposition and powers $A^k$: iterating (9.1) gives $x_t=A^{t-1}x_1$ for constant $A$ (added step), which later tools can analyse.
- [structural-analogy] K-Markov model ↔ vector auto-regression in econometrics (named on p. 164).
- [structural-analogy] Supply chain incidence matrix ↔ graph models: $A^{\rm sc}f$ converts edge flows into node changes.

## Questions this raises
- What happens to $x_t$ in the long run (e.g. the epidemic's convergence, population growth)? Which properties of $A$ decide this?
- How small must $h$ be in Euler's method, and how does error grow with simulation length?
- Can inputs $u_t$ be chosen to steer the state to a target (e.g. the supply chain back to target levels)?
- If $A$ is unknown, how can it be estimated from observed trajectories?

## Exercises worth doing
- Ex. 9.1 (p. 174) — write a compartmental system as $x_{t+1}=Ax_t$; practice tracking inflows and outflows per column — difficulty: easy
- Ex. 9.3 (p. 174) — find $F,g$ such that $Fz=g$ characterizes equilibrium points of $x_{t+1}=Ax_t+c$ — difficulty: medium
- Ex. 9.4 (p. 175) — reduce a 2-Markov model to $z_{t+1}=Bz_t$ with $z_t=(x_t,x_{t-1})$ — difficulty: medium
- Ex. 9.5 (p. 175) — Fibonacci sequence as a linear dynamical system, with a modified version — difficulty: easy
- Ex. 9.6 (p. 175) — recursive averaging as a system with time-varying matrices $A_t,B_t$ — difficulty: hard
- Ex. 9.7 (p. 175) — cost of simulating $x_{t+1}=Ax_t+Bu_t$ in flops — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (labels give printed numbers directly). Source pdf 173–185 contain content; pdf 186 is blank.
- In §9.3 the epidemic simulation starts at $x_0$, although the chapter indexes time from $t=1$ (p. 168). The text has the typo "have have" on p. 168.
- The population matrix $A$ in the text layer is garbled; I took it from the page image (p. 167). Figure curves (e.g. Figures 9.5, 9.7) are described only as the text states them, plus values visible in the images.
- The units of $\eta$ are given in the source as "Newtons per meter per second" (p. 171).
- Exercise solutions are not printed in this unit.
