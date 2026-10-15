---
id: state
type: concept
fields: [control-theory, bayesian, information-theory, political-science]
fields_strong: [control-theory, bayesian, information-theory, political-science]
n_sources: 29
n_works: 10
tiers: [core, deep, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch02-change, ashby-1956-cybernetics/ch03-determinate, ashby-1956-cybernetics/ch04-machine, ashby-1956-cybernetics/ch06-black, ashby-1956-cybernetics/ch07-quantity, ashby-1956-cybernetics/ch09-incessant, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch07-state, bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch05-v, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch07-vii, bellman-1957-dp/ch09-ix, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch03-learning-p1, clark-2017-principles/ch04-origins-p1, kalman-1960-filtering/main, liberzon-2012-calculus/ch01-introduction, sarkka-2023-bayesianfiltering/ch01-are, sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch03-batch, sarkka-2023-bayesianfiltering/ch06-bayesian, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch17-frontiers, welch-2004-kalmanintro/main]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# state

## Canon spine entry

- **state** (control-theory): the minimal set of numbers that, with future inputs, determines future behavior (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch02-change]] (p. 10): used informally here as one of the two ends of a transition; no formal state concept yet
- [[ashby-1956-cybernetics/ch03-determinate]] (p. 25): any well-defined condition that can be recognised if it recurs; here an operand
- [[ashby-1956-cybernetics/ch04-machine]] (p. 50): here a vector of component values; whole-machine state of coupled parts is a vector of the parts' states
- [[ashby-1956-cybernetics/ch06-black]] (p. 88): Ashby's input/output state as a snapshot of levers/dials; machines specified by transitions of states
- [[ashby-1956-cybernetics/ch07-quantity]] (p. 136): used for the machine's condition; a set of states is the operand set for a transformation [work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch09-incessant]] (p. 172): as used here, the choice of what counts as state decides whether the system is state-determined; "memory" is a hypothesis made when observation is limited [work fields: control-theory, information-theory]
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (pp. 3-2, 3-10): variables that capture the past for predicting the future; in physical systems they account for storage of mass, momentum, energy
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-3, p. 4-13, p. 4-23): the quantities whose values determine future behaviour; here $v$ (car), $(\varphi,\dot\varphi)$ (bicycle), $(x_{cpu},x_{mem})$, concentrations, populations
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-9): variables that permit prediction of future evolution given future inputs
- [[bellman-1957-dp/ch01-i-p1]] (p. 7): here the remaining quantity $x$ together with the number of stages left $N$
- [[bellman-1957-dp/ch03-iii]] (p. 82): the small set of parameters describing the system at a stage; the number of stages left is kept as a separate parameter
- [[bellman-1957-dp/ch05-v]] (pp. 155, 157): stock $x$ and number of remaining stages $n$; with lags, extra variables for goods on order
- [[bellman-1957-dp/ch06-vi]] (p. 184): each industry's state is assumed to be completely specified by its stockpile and capacity
- [[bellman-1957-dp/ch07-vii]] (p. 207): here four numbers $x_1..x_4$: stockpiles and capacities of autos and steel
- [[bellman-1957-dp/ch09-ix]] (pp. 249, 252, 263, 265, 268): variables on which the optimal value depends: $c$; $(c,T)$; $(a,c)$; $(c,T,m)$; $(a,k)$
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 10, 13): the quantity $x_k$ that, with controls, determines future states via $f_k$; in the scheduling example, the set of operations already done
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 81): here: information known to the controller at $k$ that can help choose $u_k$; it separates past from future ("Markov property")
- [[bertsekas-2026-rlcourse/ch03-learning-p1]] (pp. 356–361): in this unit, board position (tetris, chess), queue lengths, or information-vector summaries; features give a compact description
- [[kalman-1960-filtering/main]] (p. 39): least data about the past needed to predict the future
- [[liberzon-2012-calculus/ch01-introduction]] (p. 1): the vector $x\in\mathbb R^n$ in $\dot x=f(t,x,u)$
- [[sarkka-2023-bayesianfiltering/ch01-are]] (p. 1, p. 9): the dynamic variables that fully describe the system, e.g. $(x_k,\dot x_k)$ [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (p. xxvi): $\mathbf x_k$ at step $k$, $\mathbf x(t)$ at continuous time [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch03-batch]] (p. 35): here the vector of unknown parameters of the system, not the regressor [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (p. 91): the hidden variable $\mathbf x_k$ whose distribution is estimated [work fields: control-theory, bayesian]
- [[sutton-2018-rl/ch01-introduction]] (p. 7): informally, whatever information the agent has about its environment
- [[sutton-2018-rl/ch03-finite]] (pp. 49–50): in this unit, what the agent can know that is useful for choosing; it should carry all past information relevant to the future
- [[sutton-2018-rl/ch17-frontiers]] (p. 465): here a function of history, not given by the environment
- [[welch-2004-kalmanintro/main]] (p. 2): $x\in\Re^n$, the quantity being estimated

### political-science

- [[clark-2017-principles/ch04-origins-p1]] (pp. 87, 90–91): an entity relying on coercion and the threat of force to rule in a given territory; the authors drop Weber's "legitimate" and "monopoly" [new]

## Instances that use it

- [[wolfers-oil-governors]] — governors in oil states were rewarded or punished for world oil prices — from [[achen-2016-realists/ch04-rational]]
- [[drought-flood-elections-1900-2000]] — incumbent-party state vote falls with absolute PHDI across 26 elections — from [[achen-2016-realists/ch05-blind]]
- [[drought-2000-election]] — climate distress cost Gore an estimated 2.7 points nationally, about 2.8 million votes and seven states — from [[achen-2016-realists/ch05-blind]]
- [[new-deal-1936-election]] — state-level evidence of myopic economic voting in FDR's landslide — from [[achen-2016-realists/ch07-chicken]]
- [[ammonia-inversion]] — a tunnelling molecule whose stationary state has no dipole moment — from [[anderson-1972-moreisdifferent/main]]
- [[povinelli-sceptical-argument]] — Figure 3.2: a mental-state step may be skipped between observed and predicted behaviour — from [[apperly-2011-mindreaders/ch03-evidence]]
- [[buridans-ass-welfare]] — even from a known nonmaximal state, no way to know which of the better states to move to — from [[arrow-1951-socialchoice/ch04-iv]]
- [[scitovsky-three-state-example]] — two goods, two people, x I y, y I z, but not x I z — from [[arrow-1951-socialchoice/ch04-iv]]
- [[kinematic-graph-u-and-t]] — worked graphs with a stopping state, cycles and several basins — from [[ashby-1956-cybernetics/ch02-change]]
- [[stickleback-courtship]] — non-numerical states in a determinate system — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[pneumonia-course]] — series of non-numerical states — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[two-coin-vector]] — the transformations $N$ and $M$ on four vector states — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[causalgia]] — a two-state regenerative circuit, one state painful — from [[ashby-1956-cybernetics/ch05-stability]]
- [[five-state-two-views]] — two basins and cycle vs one basin and no cycle, from different sub-machines — from [[ashby-1956-cybernetics/ch06-black]]
- [[coffee-cooling-information-loss]] — stored information decays as the state runs to "cold" — from [[ashby-1956-cybernetics/ch07-quantity]]
- [[lossy-four-state-coder-table]] — the 4-state, 3-parameter transducer whose output loses a distinction (BC duplicated), so it cannot be a perfect coder — from [[ashby-1956-cybernetics/ch08-transmission]]
- [[insect-in-pool]] — three-state Markov chain (B, W, P); equilibrium (44.9, 42.9, 12.2); entropy 0.842 bits per step — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[merging-a-and-d-to-x]] — merging states without loss of entropy — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[mouse-and-cat]] — survival as a set of living states stable under C — from [[ashby-1956-cybernetics/ch10-regulation]]
- [[signalman-in-fog]] — restricted information about T's state — from [[ashby-1956-cybernetics/ch12-error]]
- [[telephone-selector]] — determinate two-state error-controlled hunt — from [[ashby-1956-cybernetics/ch12-error]]
- [[cruise-control]] — PI speed control robust to road slope and mass; mode logic via state machine — from [[astrom-2021-feedbacksystems/ch01-introduction]]
- [[traffic-light-controller]] — four-state finite state machine — from [[astrom-2021-feedbacksystems/ch03-system-p1]]
- [[virtual-memory-paging]] — discrete feedback with three states — from [[astrom-2021-feedbacksystems/ch03-system-p2]]
- [[predator-prey]] — linearised state feedback regulates lynx population — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[drug-administration-two-compartment]] — state-feedback dosing vs pulsed doses — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[noisy-sinusoidal-disturbance]] — disturbance modeled by a noise-driven oscillator and state augmentation — from [[astrom-2021-feedbacksystems/ch08-output]]
- [[integral-action-by-augmentation]] — constant disturbance estimated as a state — from [[astrom-2021-feedbacksystems/ch08-output]]
- [[electric-car-two-motors-cruise-control]] — two PI controllers give steady-state wheel forces of different signs, so one wheel drives and the other brakes — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]]
- [[revised-state-transition]] — Markov-model rule that stopped cooperating after enough defections — from [[axelrod-1984-cooperation/appa-tournament]]
- [[leyland-rule]] — rank 49 actually, but first in the hypothetical tournament with REVISED STATE TRANSITION times five — from [[axelrod-1984-cooperation/appa-tournament]]
- [[unbounded-allocation-process]] — state $(x,z)$, decision $y$, transformation $ay+b(x-y)$ — from [[bellman-1957-dp/ch03-iii]]
- [[stochastic-gold-mining]] — state $(x,y,z)$, choice Anaconda or Bonanza — from [[bellman-1957-dp/ch03-iii]]
- [[expected-time-to-known-state]] — Type Three problem of reaching state 0 with certainty, by observing (L) or transforming ($T_l$) — from [[bellman-1957-dp/ch04-iv]]
- [[auto-steel-tool-model]] — six-state discrete and continuous bottleneck process — from [[bellman-1957-dp/ch06-vi]]
- [[auto-steel-bottleneck]] — two-industry model with four states and four allocation rates — from [[bellman-1957-dp/ch07-vii]]
- [[isoperimetric-problem]] — max area with length budget $L-L'$ as state — from [[bellman-1957-dp/ch09-ix]]
- [[maximize-state-one-probability]] — decision process maximizing the probability of $S_1$ — from [[bellman-1957-dp/ch11-xi]]
- [[nonunique-maxima-counterexample]] — two-state example with infinitely many solutions — from [[bellman-1957-dp/ch11-xi]]
- [[traveling-salesman-dp]] — exponential state growth makes exact DP intractable; rollout with nearest neighbor is polynomial — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[two-state-discount-threshold]] — shortest path with states 1, 2, $t$; discounting changes the solution discontinuously at a threshold $\alpha$ — from [[bertsekas-2026-rlcourse/ch01-exact-p2]]
- [[bidirectional-parking]] — belief-state DP with time-varying free probabilities — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[llm-ngram-dp]] — text strings as states, words as controls, a GPT as a policy — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[discrete-optimization-as-dp]] — $k$-solutions as states — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[unstable-scalar-system-with-state-constraint]] — $x_{k+1}=2x_k+u_k$, $|u|\le1$, largest invariant set $|x|\le1$ — from [[bertsekas-2026-rlcourse/ch01-exact-p5]]
- [[single-state-ssp-instability]] — $\ell$-step region $\tilde J(1)>1-\ell\epsilon$ — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[markov-jump-parameter-problem]] — augmented state, CE with most likely parameter path — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[radial-basis-functions]] — Gaussian features around anchor states, as in (3.4) — from [[bertsekas-2026-rlcourse/ch03-learning-p1]]
- [[example-3-3-1-small-delta]] — scalar linear-quadratic system where $Q_\pi$ is dominated by a state-only term — from [[bertsekas-2026-rlcourse/ch03-learning-p2]]
- [[coarse-grid-approximation]] — representative states on a coarse grid with proximity-based $\phi_{jy}$ — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]
- … 136 more instance lines mention this id

## Candidate bridges

- [structural-analogy] Povinelli's behaviour-only reading ↔ Clever Hans effect: apparent mental-state competence that may come from simple cues in the test. — from [[apperly-2011-mindreaders/ch03-evidence]] (theory-of-mind → theory-of-mind)
- [metaphor] Similarity-to-self narrowing the plausible thoughts of others under uncertainty (p. 70) ↔ Bayesian theory of mind: priors that constrain inference over mental states. — from [[apperly-2011-mindreaders/ch04-evidence]] (theory-of-mind → theory-of-mind)
- [structural-analogy] relevance problem (what to feed into mindreading) ↔ inverse planning / POMDP: the modeller must specify the state space, priors and goals before inference — the chapter says theories treat this as given. — from [[apperly-2011-mindreaders/ch07-elaborating]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Repeated transformation and trajectory on the kinematic graph ↔ control-theory: state evolution of a discrete-time system, with the initial state set and then left to run without input (the text calls the correspondence "analogous"). — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → control-theory)
- [same-math] Canonical representation $x'=f(x)$ ↔ control-theory: autonomous discrete-time state-space model $x_{k+1}=f(x_k)$ — same one-step rule, repeated powers. — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [structural-analogy] Adding angular velocity to make the pendulum single-valued ↔ control-theory: state must include all variables needed to predict the future (state concept). — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [same-math] machine $x'=f(x,a)$ with parameter $a$ ↔ control-theory: discrete-time state model with an input — $a$ plays the role of the input. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → control-theory)
- [structural-analogy] coupling by setting the parameter as a function of the other machine's state ↔ control-theory: feedback law (state or output feedback) — the loop is closed by making input depend on state. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → control-theory)
- [structural-analogy] diagram of immediate effects ↔ dependency graph of a dynamical system (which state variables enter each equation) — arrows record who affects whom in one step. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → unspecified)
- [structural-analogy] $\lim T^nD(a)=a$ ↔ control-theory: asymptotic stability of an equilibrium to a perturbation — Ashby's limit test on arbitrary state sets. — from [[ashby-1956-cybernetics/ch05-stability]] (control-theory → control-theory)
- [structural-analogy] Observer Two inferring hidden Z from past inputs (p. 115) ↔ control-theory: an observer / state estimator rebuilding hidden state from past inputs and outputs — both replace a hidden variable by a function of observed history. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [metaphor] Ashby's models as homomorphisms (p. 109) ↔ control-theory: good regulator theorem (a regulator must contain a model of its system) — links "model" to regulation, but this unit does not state that theorem. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [structural-analogy] law of Experience ↔ state estimation: a system forgets its initial state and the state tracks the input history — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → other:state-estimation)
- [structural-analogy] $\log_2 r$ bits per step through an $r$-state channel ↔ information theory: channel capacity — Ashby derives only an upper bound from state count, in a determinate setting — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → information-theory)
- [same-math] Population update $D'=MD$ with a column-stochastic $M$ ↔ control-theory: discrete-time linear state-space model $x_{k+1}=Ax_k$. The equilibrium is a fixed vector of $M$, and the "dying oscillations" are mode behaviour. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] Re-coding to Markov form ↔ control-theory: state augmentation, adding past values to the state so the dynamics become first-order. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] "Memory is a hypothesis forced by limited observation" (p. 172) ↔ control-theory: observability, where hidden state is inferred from a sequence of outputs. Ashby himself links this to S.6/21. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [same-math] Markovian machine with absorbing state; mean time to absorption ↔ Markov chains: absorbing-state expected hitting time (p. 230 average equals a geometric-series mean). — from [[ashby-1956-cybernetics/ch12-error]] (control-theory → other:probability)
- [structural-analogy] Matching closed-loop characteristic polynomial coefficients (2.26)–(2.28) ↔ control theory: pole placement by state feedback — both choose gains to put closed-loop roots where wanted (the chapter only points to later chapters, p. 2-28). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → control-theory)
- [structural-analogy] Hysteresis from positive feedback with saturation ↔ bistable switches with two stable states — the same equilibrium-and-slope picture (stable where $G'>0$). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → unspecified)
- [structural-analogy] Energy function $V$ with $\dot V\le0$ ↔ control theory (stability): a scalar function of the state that cannot increase proves boundedness without solving the ODE. — from [[astrom-2021-feedbacksystems/ch03-system-p1]] (control-theory → control-theory)
- [same-math] PI controller as a controller state $z$ with $\dot z=v_r-v$ (4.4) ↔ op-amp PI circuit (p. 4-11) — both realize a PI law (the op-amp circuit with an inversion sign). — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [same-math] Two-compartment drug model (4.28) ↔ any linear state-space model $\dot x=Ax+Bu$, $y=Cx$ — literally the same matrix form. — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [metaphor] Bistable genetic switch (two stable states, an unstable middle) ↔ social/economic models with two stable regimes and tipping. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → unspecified)
- [structural-analogy] Modes and eigenvectors ↔ principal components / spectral decomposition in data analysis: a state vector decomposed along eigen-directions that evolve independently. — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → linear-algebra)
- [same-math] Observer design by eigenvalue assignment ↔ state feedback pole placement (ch. 7): the same problem with $A,B,K$ replaced by $A^T,C^T,L^T$ (p. 8-7). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
- [structural-analogy] PID's linear extrapolation vs observer prediction ↔ state-space control: both predict, one from a model and one from the signal's slope (p. 11-1). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → control-theory)
- [structural-analogy] Cascade control with all states measured ↔ state feedback: the text calls state feedback the "ultimate case" of cascade (p. 15-19). — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → control-theory)
- [structural-analogy] IMC/Smith predictor internal model ↔ observer (state estimator): a model runs in parallel with the process, and its mismatch with the output is used for correction. — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → control-theory)
- [same-math] Recursive least squares (15.19) ↔ Kalman filter: the author states RLS is a special case of the Kalman filter (§8.2). — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [structural-analogy] polynomial division p = sq + r ↔ number theory: integer division with remainder — the author states the analogy himself (p. 123) — from [[axler-2024-ladr/ch04-polynomials]] (linear-algebra → other:mathematics)
- [structural-analogy] $T^kv=\lambda^kv$ for eigenvectors (5.59) ↔ Markov matrices / power iteration: steady-state and long-run behaviour from eigen-decomposition — same mechanism, not developed here. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [same-math] Gram–Schmidt (6.32) ↔ linear-algebra: QR factorization — orthonormalising the columns of an independent list gives the $Q$ factor (the text itself does not state QR). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] positive operators ↔ nonnegative real numbers; self-adjoint ↔ real; unitary ↔ unit circle — Axler states this analogy (p. 262). — from [[axler-2024-ladr/ch07-operators-p2]] (linear-algebra → unspecified)
- [structural-analogy] Quadratic closed forms of §17 ↔ LQR: value function quadratic in the state — here only on a restricted interval with constraint $0\le y\le x$. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [structural-analogy] Vector-state multi-activity recursion ↔ state-space models: resources as state vector, allocations as inputs. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [structural-analogy] gain/loss ratio rule ↔ control-theory: an index policy that ranks actions by a single number computed per option — the text proves it for this two-mine process and only states it for the extensions (Theorems 3–4). — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] Type Three problem with $p$ a probability vector over states ↔ belief-state formulation of decisions under partial observation: "observe the true state" resets the belief to a vertex. — from [[bellman-1957-dp/ch04-iv]] (control-theory → other:belief-state-formulation-of)
- [same-math] $f_{n+1}(x)=\min_z T(z,x,f_n)$ iterated from $f_0$ ↔ control-theory: value iteration for a discounted MDP with a continuous state — the same successive-approximation scheme. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [structural-analogy] $f'(x)=-k$ as "price" of stock, with derivatives as Lagrange multipliers (p. 162) ↔ control-theory: costates / shadow prices in the Pontryagin principle — both give the marginal value of the state. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [metaphor] Supply lag (§14) ↔ control-theory: a longer lag (two periods) forces extra state variables, and the optimal policy is no longer a simple order-up-to rule. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [structural-analogy] Dual variables $y(t)$, which run backward from terminal conditions ↔ Pontryagin costates (shadow prices along a trajectory) — also evolve backward, price the state. — from [[bellman-1957-dp/ch06-vi]] (control-theory → unspecified)
- [structural-analogy] impulse at $t=0$ bringing $x_3$ to 0 ↔ impulse control: instantaneous jumps in state when controls are unbounded. — from [[bellman-1957-dp/ch07-vii]] (control-theory → other:psychology-cognitive-science)
- [structural-analogy] Policy $v(c,T)$ as feedback on state ↔ control-theory: state feedback $u=-Kx$ — action as function of the current state (the toy example gives $y=-x$) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] Max-Min functional equation ↔ control-theory: Bellman equation of a one-person problem — replacing $\max$ by $\max\min$ keeps the "payoff plus value of next state" form. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)
- [same-math] DP backward recursion (1.5) ↔ shortest-path algorithms on staged acyclic graphs: the book states the equivalence of finite-state deterministic problems and shortest paths (p. 12) — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → other:computer-science)
- [structural-analogy] Belief state $b_k$ with update $F_k$ ↔ control-theory state estimation: Kalman filter output used as the state of a perfect-information problem (the text names Kalman filtering as one choice of $F_k$). — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → control-theory)
- [structural-analogy] State augmentation with $x_{k-1},u_{k-1}$ ↔ state-space modeling: higher-order recursions rewritten as first-order systems. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → control-theory)
- [structural-analogy] Finite-history state for POMDP ↔ sequence models: the author states that this is how LLMs such as ChatGPT work. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → other:sequence-models)
- [structural-analogy] Integral term of PID ↔ control-theory: disturbance observer on an augmented state $(x,w)$ with $w_{k+1}=w_k$ — the author calls the integral term the simplest instance of the idea of inferring a constant disturbance, and calls the MPC version "a similar strategy" (pp. 130–131). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → control-theory)
- … 222 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
