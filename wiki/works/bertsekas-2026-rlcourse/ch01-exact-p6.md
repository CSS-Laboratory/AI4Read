---
id: bertsekas-2026-rlcourse/ch01-exact-p6
work: bertsekas-2026-rlcourse
unit: "1 Exact and Approximate Dynamic Programming (part 6/6): end of 1.7, 1.8 Notes, Sources, and Exercises"
pages: 140-162
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Chapter 1, part 6: closing remarks, chapter summary, literature notes, exercises

## L0 — One line
The book's principal subjects are approximation in value space, rollout and policy iteration, which the author relates to Newton's method on the Bellman equation. The notes give sources for these strands, and the exercises let the reader test them.

## L1 — The gist (≤ 120 words)
This part finishes the comparison of optimization and machine learning (ML). It then summarizes Chapter 1 on dynamic programming (DP), lists courses it could support, reviews the literature, and gives nine exercises. The question is what the book's core is and where it comes from. The answer: approximation in value space (choosing actions by looking ahead with an approximate cost function), rollout and policy iteration, which the author links to Newton's method applied to the Bellman equation, not to gradient descent. The notes cover exact DP, rollout, multiagent problems, adaptive control and model predictive control (MPC). The exercises cover a travelling-salesman problem (TSP), a stock-selling problem, the Newton-step identity for linear quadratic problems, and regions of stability.

**Prerequisites:** dynamic programming (Bellman equation, value iteration); one-dimensional linear quadratic problem and its Riccati equation; Newton's method for $H(K)=0$; basic probability.

## L2 — Key ideas (5–10 bullets)
- Optimization and machine learning often overlap in tools, and may differ in emphasis and priority depending on the problem. In ML, specialized methods without general performance guarantees may be perfectly acceptable. (p. 140)
- The chapter covers six themes: exact DP, approximation in value space, off-line training with on-line play, policy iteration and rollout, major models, function approximation. (pp. 140–141)
- Rollout (using the cost of a fixed base policy as the approximation in one-step lookahead) is the first iteration of policy iteration from the base policy. It needs no off-line training once the base policy exists. Policy iteration is repeated rollout and does need training. (p. 144)
- The author says approximation in value space applies Newton's method to the Bellman equation, with no connection to gradient descent. First-order methods such as Gauss-Seidel and Jacobi (iterative methods for systems of equations) can be applied to such equations, but he says they are much slower than Newton's method. (p. 145)
- The author says measurability difficulties are usually neglected in the reinforcement learning (RL) literature (and in this book), and that this is fine because they do not play an important role in practical applications. They do not arise for finite or countably infinite state and control spaces. (p. 143)
- The author says RL's learning from interaction is more or less the same as classical dual and adaptive control. Feldbaum's dual control papers, starting in 1960, stressed the division of effort between estimation and control, now called the exploration–exploitation tradeoff. (p. 147)
- Exercises 1.1 and 1.4 show rollout improving on a base heuristic (TSP: 37 vs 48; stock sale: 2.269 vs 2.268). The printed TSP complexity estimate for rollout is $O(N^4)$. Finite-sample Monte Carlo can degrade rollout (20 samples did worse than the heuristic). (pp. 151–152, 157)
- Exercise 1.7 asks the reader to show algebraically that one-step lookahead is a Newton step. Exercises 1.8–1.9 study the region of stability (the set of cost approximations whose lookahead policy is stable), which generally expands as the lookahead length grows. (pp. 159–162)

## L3 — Walkthrough

### End of Section 1.7: optimization versus machine learning (p. 140)
- The part given starts mid-discussion. The author says the starting point in ML is often a specific dataset or training problem, for example translation or image recognition. (p. 140)
- There the priority is a method that works well for that dataset, even if it does not generalize. Specialized architectures, implementation techniques and heuristics "may be perfectly acceptable" without rigorous, generally applicable guarantees. (p. 140)
- Conclusion (author): both fields use models and rigorous analysis and overlap in tools and applications. They may differ in emphasis on analysis, insight and generality versus practical effectiveness. This can create tension between fields. (p. 140)

*Intuition note.* In this passage the author says that in ML a method tuned to one dataset or problem may be perfectly acceptable even without general guarantees. Depending on the problem, fields may differ in how much they stress analysis and generality versus practical effectiveness, and he notes this can cause tension.

### 1.8 Notes, Sources, and Exercises

**Chapter summary (p. 140–141).** The author lists what the chapter covers:
- (a) Exact DP in all major forms: deterministic and stochastic, discrete and continuous, finite and infinite horizon.
- (b) Approximation in value space with one-step and multistep lookahead, "the workhorse of RL", behind its major success stories including AlphaZero. It is contrasted with approximation in policy space, and the two may be combined.
- (c) The split between off-line training and on-line play. Their synergy can be intuitively explained through Newton's method.
- (d) Policy iteration (primarily off-line) and rollout (primarily a less ambitious on-line method). Both are related to Newton's method and draw effectiveness from it.
- (e) Major models: discrete optimization, POMDP, multiagent problems, adaptive control, model predictive control (MPC).
- (f) Function approximation, e.g. neural networks and feature-based architectures.

**Courses the chapter can support (p. 141).** The author lists ten topics:
1. rollout and policy iteration;
2. neural networks and other architectures for off-line training;
3. aggregation;
4. sequential decision making with changing parameters, estimation, and simultaneous identification and control;
5. temporal difference methods and Q-learning;
6. sampling methods for off-line training;
7. statistical estimates and efficiency of sampling;
8. on-line methods such as multi-armed bandits;
9. simulation-based approximation in policy space (policy gradient, random search);
10. deeper control design (MPC, adaptive control; robotics, transportation).

This book focuses on (1)–(4), with limited coverage of (9) in Section 3.5. (p. 141)

**Notes and Sources, Sections 1.1–1.4 (pp. 142–144).**
- The author's coverage of exact DP is brief. For fuller treatments he points to his own textbooks [Ber17a], [Ber12], to Puterman [Put94], and to Bertsekas–Shreve [BeS78]. [BeS78] treats the measure-theoretic issues of stochastic optimal control. (p. 142)
- The footnote on measurability (p. 142–143) gives these facts:
  - The Borel-space framework stems from Blackwell's work in the 1960s.
  - It uses the theory of analytic sets, introduced by Suslin in 1917.
  - If $F(x,u)$ is Borel measurable, $G(x)=\min_u F(x,u)$ need not be. It belongs to the broader class of lower semianalytic functions.
  - Even when minimizing policies exist, none may be Borel measurable. A minimizing universally measurable policy does exist.
  - So DP algorithms such as value and policy iteration leave the Borel framework. The broader universal-measurability framework of [BeS78] is needed "in the absence of additional (fairly strong) assumptions".
- Author's position: RL literature usually neglects measurability, "and this is fine" because, he says, measurability issues do not play an important role in practical applications; it does not arise for finite or countably infinite spaces. He adds that quite a few published works claim to address it with narratives that are "confusing or plain incorrect". (p. 143)
- The abstract DP monograph [Ber22b] encodes a model's structure in its abstract (Bellman) operator, its "mathematical signature". Properties such as monotonicity and contraction largely determine which results and algorithms apply. This framework also supports Newton-method visualizations. (p. 143)
- Rollout (p. 143–144):
  - Rollout is the first iteration of policy iteration from the base policy.
  - Truncated rollout is an "optimistic" single policy iteration, with the policy evaluated inexactly by a limited number of value iterations.
  - Policy iteration is repeated rollout. It is more ambitious and needs off-line training, possibly with neural networks.
  - Rollout needs no off-line training once the base policy exists. This is its principal advantage over policy iteration. The author calls it reliable, easy to implement and usable with on-line replanning. He also calls it compatible with transformer networks and large language models (Section 2.3.7).
  - The name was introduced by Tesauro and Galperin [TeG96] for backgammon: evaluating a position by playing it out many times with random dice and a fixed policy for both sides. (footnote, p. 143–144)
  - **Tesauro–Galperin (quoted by the author):** truncated rollouts gave "at least an order of magnitude speed-up compared to full rollouts", with fewer steps and lower variance per trial. The author says experience since 1996 is consistent with this. (p. 144)

**Notes, Section 1.5 (p. 144–145).**
- Kleinman [Kle68] first derived the link between policy iteration and Newton's method for linear quadratic problems, in continuous time. Hewer [Hew71] treated discrete time. (p. 144)
- The general relation of approximation in value space to Newton's method, and its links to MPC and adaptive control, was first presented in the author's [Ber20a], [Ber21b], [Ber22c], [Ber22a]. It explains the synergy of off-line training and on-line play, including how multistep lookahead improves the starting point of the Newton step. [Ber22a] also analyzes Newton variants for nondifferentiable fixed-point problems like the Bellman equation. (p. 145)
- **Author's point:** Newton's method is applied here to a system of equations (the Bellman equation). This has "no connection" with gradient descent used in e.g. neural network training. He says no gradient descent method can solve systems like the Bellman equation. (p. 145)
- First-order deterministic methods (Gauss-Seidel, Jacobi, and stochastic asynchronous extensions) can be applied to Bellman equations. They include various Q-learning algorithms. The author says they are much slower than Newton's method and have limited utility in on-line play. (p. 145)

*Intuition note.* The author applies Newton's method to the Bellman equation, a system of equations, and says this has no connection with gradient descent, which is used for optimization problems such as neural network training. He also says multistep lookahead enhances the starting point of the Newton step.

**Notes, Section 1.6 (pp. 145–148).**
- Multiagent problems (pp. 145–146):
  - Early names were *team theory* and *decentralized control*.
  - "Multiagent" is used in different senses. In one sense, agents lack common information ("nonclassical information patterns"), which cannot be solved by exact DP. In another, agents are weakly coupled and decoupled suboptimal computations exploit this.
  - Agent-by-agent minimization in multiagent rollout was proposed in [Ber19c], with links to person-by-person optimality from team theory.
  - Later computational studies report large-scale multi-robot and vehicle routing problems with partial state information, using policy neural networks and precomputed signaling policies. They compare against policy gradient approaches.
- Adaptive control (pp. 146–147):
  - The literature is very extensive, with methods spanning 60 years.
  - PID ideas are used in adaptive and robust control. The author cites Wikipedia saying Minorsky developed a formal PID control law in 1922.
  - Feldbaum introduced the DP framework for adaptive control from 1960 under the name *dual control theory*. It stressed the division of effort between estimation and control, now called the exploration–exploitation tradeoff. In 1963 he concluded that approximate solution methods and sub-optimal strategies were the most important near-term problem. (p. 147)
  - The author says RL's "learning from interaction with the environment" is more or less the same as classical dual and adaptive control. Adaptive and dual control can be formulated as POMDP (Section 2.11). Rollout in this setting was first suggested in [Ber22a], Section 6.7. (p. 147)
- Model predictive control (pp. 147–148):
  - The idea is on-line optimization with a truncated rolling horizon and a terminal cost approximation.
  - It arose in several contexts: control and OR folklore of the 1960s–70s, chemical process control (where the names MPC and "dynamic matrix control" arose), and independently heuristic search, planning and games in computer science.
  - "Predictive" refers to taking the system's future into account while applying control now. The author lists early papers, surveys and textbooks, his [Ber05a] on MPC–rollout connections and [Ber24] on the DP/Newton framework applied to MPC.

**Reinforcement learning sources (pp. 148–150).**
- The first DP/RL books of the 1990s were Bertsekas–Tsitsiklis 1996 (decision, control and optimization viewpoint) and Sutton–Barto 1998 (AI viewpoint; 2nd edition 2018). Both treat finite-state Markovian models with transition-probability notation and do not address continuous spaces, a major focus of this book. (p. 148)
- The author then lists more recent books, each with a one-clause focus: simulation-based optimization, sensitivity approach, adaptive sampling, function approximation, bandits, OR applications, adaptive control, MPC, convergence by the ODE approach, partial state information, and others. (pp. 148–149)
- This book is similar in style to his [Ber19a], [Ber20a], [Ber22a] and [Ber22b]. [Ber19a] gives broader coverage of value-space methods (certainty equivalent control, aggregation) and more on policy-space approximation. [Ber20a] introduced the Newton connection. [Ber22b] supplies the Bellman-operator framework behind the Newton visualizations. (pp. 149–150)
- Surveys are listed by focus: real-time DP, general RL principles, linear programming and resource allocation approaches, policy gradient, Monte Carlo tree search, planning, deep RL, and the author's own surveys on rollout/MPC, aggregation, multiagent problems and RL–MPC relations. (p. 150)

### Exercises (pp. 151–162)

**Ex. 1.1 TSP rollout (pp. 151–152).** A five-city TSP (cities A–E), a modification of Example 1.2.3. Results printed in Fig. 1.8.1 and the text:
- (a) The exact DP optimal tour from A is ABDECA, cost 20.
- (b) The nearest-neighbor heuristic gives ACDBEA, cost 48.
- (c) Rollout with one-step lookahead and the nearest-neighbor base heuristic gives AECDBA, cost 37. At A it compares the heuristic tours from AB, AC, AD, AE (costs 49, 48, 63, 37). At AE it compares AEB, AEC, AED (costs 42, 37, 63). At AEC it compares 52 and 37. (p. 152)
- (d) The exercise asks the reader to show that rollout with two-step lookahead generates the optimal tour. (p. 152)
- (e) Printed answer: the heuristic needs $O(N)$ comparisons at each of $N$ stages, so $O(N^2)$. Rollout at stage $k$ runs it $N-k$ times, so $O(N^2)$ runs and $O(N^4)$ in total. This is a low-order polynomial increase over the base heuristic and potentially a huge improvement over exact DP. (p. 152)

*Intuition note.* Rollout asks, at each step, which next city makes the heuristic's completed tour cheapest, and commits to that one city. It beat the heuristic here (37 vs 48) but not the optimum (20). Part (d) of the exercise asks the reader to show that two-step lookahead generates the optimal tour.

**Ex. 1.2 LQ and Newton step (pp. 152–153).** Undiscounted problem with $a=2$, $b=1$, $q=1$, $r=5$. The parts ask for graphical work:
- solve the Riccati equation graphically (Fig. 1.5.1 style);
- solve it for the linear policy $\mu(x)=-(3/2)x$;
- run value iteration from $K_0<K^*$ and $K_0>K^*$;
- show one-, two- and three-step lookahead as Newton steps, with $\tilde K<K^*$ and $\tilde K>K^*$, and find the stability region;
- plot the error $|K_{\tilde\mu}-K^*|$ against $|\tilde K-K^*|$;
- show rollout and truncated rollout graphically.

**Ex. 1.3 Spiders and flies (p. 153).** Two spiders, five stationary flies. The base policy moves each spider one square towards its nearest fly (Manhattan distance, horizontal preferred on ties). The exercise compares multiagent rollout (Section 1.6.7), ordinary rollout and the base policy.

**Ex. 1.4 Exercising an option (pp. 153–158).**
- Setup:
  - Price $x_k\in\{0,\dots,\bar x\}$ moves $+1$ w.p. $p^+$, stays w.p. $1-p^+-p^-$, and moves $-1$ w.p. $p^-$. Here $0<p^-\le p^+$ and $p^++p^-<1$.
  - At $0$ it moves to $1$ w.p. $p^+$ and otherwise stays. At $\bar x$ it moves to $\bar x-1$ w.p. $p^-$ and otherwise stays.
  - The investor may sell at any of periods $0,\dots,N-1$. If unsold, the stock is sold at period $N$ at price $x_N$. The goal is to maximize expected sale value. (pp. 153–154)
- (a) Exact DP, printed solution:
$$J_N^*(x_N)=x_N \tag{1.96}$$
$$J_k^*(0)=p^+J_{k+1}^*(1)+(1-p^+)J_{k+1}^*(0) \tag{1.97}$$
$$J_k^*(\bar x)=\bar x \tag{1.98}$$
  and for $0<x_k<\bar x$:
$$J_k^*(x_k)=\max\Big\{x_k,\ p^+J_{k+1}^*(x_k+1)+(1-p^+-p^-)J_{k+1}^*(x_k)+p^-J_{k+1}^*(x_k-1)\Big\} \tag{1.99}$$
  Sell if $x_k$ attains the maximum. Do not sell at $0$; sell at $\bar x$. (p. 154)
- Data for Figs. 1.8.2–1.8.4: $N=10$, $x_0=2$, $\bar x=10$, $p^+=p^-=0.25$. Fig. 1.8.2 shows $J_0^*(2)=2.303$. Note: when the bounds never become active, e.g. $N=10$, $x_0=20$, $\bar x=40$, the author says it can be verified that the optimal expected reward is $J^*(x_0)=x_0$ and all policies are optimal. (p. 154–155)
- (b) Base heuristic: sell if price $\ge\beta x_0$ ($\beta>1$). Its reward-to-go from $x_k$, with threshold $\beta x_k$, is $J_n^{x_k}(x_n)$, $n=k,\dots,N$:
$$J_N^{x_k}(x_N)=x_N \tag{1.100}$$
  for $0<x_n<\beta x_k$:
$$J_n^{x_k}(x_n)=p^+J_{n+1}^{x_k}(x_n+1)+(1-p^+-p^-)J_{n+1}^{x_k}(x_n)+p^-J_{n+1}^{x_k}(x_n-1) \tag{1.101}$$
$$J_n^{x_k}(0)=p^+J_{n+1}^{x_k}(1)+(1-p^+)J_{n+1}^{x_k}(0) \tag{1.102}$$
  and for $x_n\ge\beta x_k$:
$$J_n^{x_k}(x_n)=x_n \tag{1.103}$$
  The values depend on the starting state $x_k$, so the heuristic is not sequentially consistent. For rollout only $J_{k+1}^{x_k+1}(x_k+1)$, $J_{k+1}^{x_k}(x_k)$, $J_{k+1}^{x_k-1}(x_k-1)$ are needed per encountered state. They can also be estimated on-line by Monte Carlo. (p. 155–156)
- (c) One-step lookahead with $\tilde J$ from the heuristic. Rollout policy: sell at $x_k$ if
$$p^+J_{k+1}^{x_k+1}(x_k+1)+(1-p^+-p^-)J_{k+1}^{x_k}(x_k)+p^-J_{k+1}^{x_k-1}(x_k-1)\le x_k,$$
  otherwise don't sell. (p. 156–157)
- Printed numbers from $x_0=2$, $\beta=1.4$: base heuristic 2.268, rollout 2.269 (exact heuristic values). The text also says the optimal reward is "2.4" (see Reading notes). Rollout rewards-to-go are $\ge$ those of the heuristic. (p. 157)
- With 20-sample Monte Carlo per needed value, rollout gets 2.264, worse than the heuristic. With 200 samples it gets 2.273. Each was evaluated by 400-sample simulation of the rollout policy. (p. 157)
- The heuristic is not a legitimate policy (its decision at $x_n$ depends on the starting state $x_k$). Rollout is always an approximation-in-value-space scheme and yields a legitimate policy. (p. 157)
- (d) Two-step lookahead needs five heuristic values per state ($x_k+2,\dots,x_k-2$). With $\ell$-stage lookahead, simulation work per stage is proportional to $2\ell+1$, the number of leaves of the lookahead tree. (p. 158)

**Ex. 1.5 Cruise control (pp. 158–159).** System $x_{k+1}=ax_k+bu_k+w_k$, $0<a\le1$, $w_k$ zero mean with variance $\sigma^2$. Cost:
$$(x_N-\bar x_N)^2+\sum_{k=0}^{N-1}\big((x_k-\bar x_k)^2+ru_k^2\big)$$
with given nonpositive targets $\bar x_k$ (a velocity profile). Design an experiment comparing a fixed linear policy $\pi$ (nominal profile), re-optimization $\pi^*$ at each profile change, and rollout $\tilde\pi$ with base $\pi$ and on-line replanning. (p. 158–159)

**Ex. 1.6 Parking (p. 159).** From Example 1.6.4. Spaces $1..L$ plus a garage at index $N$ where parking costs $C$. Moving to $i-1$ costs $t-i$, to $i+1$ costs $t+i$, and parking costs $c(i)$. The driver remembers visited spaces and may return, and must park within $N$ stages. Task: write an exact DP program over a state space as small as possible; comment on run-time as spaces increase.

**Ex. 1.7 Newton's method for the Riccati equation (pp. 159–161).**
- Newton for $H(K)=0$:
$$K_{k+1}=K_k-\left(\frac{\partial H(K_k)}{\partial K}\right)^{-1}H(K_k) \tag{1.104}$$
  with
$$H(K)=K-\frac{a^2rK}{r+b^2K}-q \tag{1.105}$$
- (a) Show, for all $K$ leading to a stable one-step lookahead policy,
$$K_L=K-\left(\frac{\partial H(K)}{\partial K}\right)^{-1}H(K) \tag{1.106}$$
  where
$$K_L=\frac{q+rL^2}{1-(a+bL)^2} \tag{1.107}$$
  is the quadratic cost coefficient of $\mu(x)=Lx$ with
$$L=-\frac{abK}{r+b^2K} \tag{1.108}$$
- Printed proof: express every term through $L$, then check an identity in $L$.
$$K=-\frac{rL}{b(a+bL)} \tag{1.109}$$
$$H(K)=-\frac{rL}{b(a+bL)}+\frac{arL}{b}-q \tag{1.110}$$
$$\frac{\partial H(K)}{\partial K}=1-\frac{a^2r^2}{(r+b^2K)^2}=1-(a+bL)^2 \tag{1.111}$$
  Substituting into (1.106) gives
$$\frac{q+rL^2}{1-(a+bL)^2}=-\frac{rL}{b(a+bL)}-\frac{1}{1-(a+bL)^2}\left(-\frac{rL}{b(a+bL)}+\frac{arL}{b}-q\right),$$
  or, multiplying by $1-(a+bL)^2$,
$$q+rL^2=-\frac{rL\big(1-(a+bL)^2\big)}{b(a+bL)}+\frac{rL}{b(a+bL)}-\frac{arL}{b}+q.$$
  The author says a straightforward calculation shows this is an identity in $L$. (added step) Right side: $\frac{rL(a+bL)^2}{b(a+bL)}-\frac{arL}{b}+q=\frac{rL(a+bL)-arL}{b}+q=rL^2+q$. (p. 160–161)
- (b) asks what happens when $K$ lies outside the region of stability. (c) asks to show for $\ell$-step lookahead
$$|K_{\tilde L}-K^*|\le c\,\big|F^{\ell-1}(\tilde K)-K^*\big|^2,$$
  where $F^{\ell-1}$ is the $(\ell-1)$-fold application of $F$ to $\tilde K$. This is a stronger bound. (p. 161)

*Intuition note.* The identity says the cost coefficient of the lookahead policy equals the Newton update of the Riccati equation. So one-step lookahead from $K$ is one Newton step, which is the exercise's way of making the Newton interpretation algebraic.

**Ex. 1.8 Error bounds and stability region (p. 161).** Data $a=2$, $b=1$, $q=1$, $r=1$. Tasks:
- plot regions of stability for one-, two- and four-step lookahead;
- verify Fig. 1.8.5, which shows the performance errors of one- and two-step lookahead against $\tilde K$. Verify that longer lookahead expands the stability region and that the error rises sharply near the boundary;
- experiment with other data and verify that for an already stable system ($|a|<1$) the stability region includes the whole nonnegative axis.

**Ex. 1.9 Region of stability, multistep lookahead (p. 162).**
- Definitions: a stationary policy $\mu$ is unstable if $J_\mu(x)=\infty$ for some $x$, and stable otherwise. The $\ell$-step region of stability is the set of $\tilde J$ whose $\ell$-step lookahead policy is stable. Generally it expands as $\ell$ increases. (p. 162)
- In finite-state discounted problems all policies are stable. In stochastic shortest path (SSP) problems there are improper policies, which do not terminate with positive probability from some states and can be unstable. (p. 162)
- Example: one state 1 plus termination state $t$. Staying costs $\epsilon>0$, moving to $t$ costs 1. $J^*(1)=1$ solves $J^*(1)=\min\{1,\epsilon+J^*(1)\}$.
  - (a) Show that the one-step region is $\tilde J(1)>1-\epsilon$, and the $\ell$-step region is $\tilde J(1)>1-\ell\epsilon$. Also asks what happens at $\tilde J(1)=1-\epsilon$. Note: the $\ell$-step region becomes arbitrarily large for large $\ell$, but its boundary is arbitrarily close to $J^*(1)$ for small $\epsilon$.
  - (b) Additional states $i=2,\dots,n$, each with stay cost $\epsilon$ or move to $i-1$ at cost 0. Partial answer given: the one-step region is all $\tilde J$ with $\epsilon+\tilde J(i)>\tilde J(i-1)$ for $i\ge2$ and $\epsilon+\tilde J(1)>1$. (p. 162)

## Toy example (ours, not from the text)
Check the Newton-step identity (1.106) numerically with $a=b=q=r=1$ and $K=1$.
- Lookahead gain (1.108): $L=-\frac{abK}{r+b^2K}=-\frac{1}{1+1}=-\tfrac12$.
- Cost coefficient (1.107): $a+bL=\tfrac12$, so $1-(a+bL)^2=\tfrac34$, and $K_L=\frac{1+\frac14}{3/4}=\frac{5/4}{3/4}=\tfrac53$.
- Newton side: $H(1)=1-\frac{1\cdot1\cdot1}{1+1}-1=-\tfrac12$. $H'(1)=1-\frac{1}{(1+1)^2}=\tfrac34$. Newton: $1-\frac{-1/2}{3/4}=1+\tfrac23=\tfrac53$. Both sides give $5/3$.
- For comparison, $K^*$ solves $K^2-K-1=0$, so $K^*\approx1.618$. One step moved from $K=1$ to $1.667$.

## Concepts
- [[rollout]] (new) — apply a base policy's value as the cost approximation in one-step lookahead; equals one policy-iteration step (pp. 143–144)
- [[truncated-rollout]] (new) — simulate the base policy a few steps, then use a terminal cost estimate; "optimistic" single policy iteration (p. 144)
- [[approximation-in-value-space]] (new) — choose actions by lookahead with an approximate cost function; the workhorse of RL (p. 140)
- [[policy-iteration]] (new) — repeated rollout; evaluation plus improvement, needs off-line training (p. 144)
- [[newton-view-of-dp]] (new) — lookahead is a Newton step on the Bellman equation, not gradient descent (p. 145)
- [[region-of-stability]] (new) — set of cost approximations whose $\ell$-step lookahead policy is stable; usually grows with $\ell$ (p. 162)
- [[base-heuristic]] (new) — a fixed heuristic whose value defines the rollout cost approximation (pp. 152, 155, 157)
- [[bellman-operator]] (new) — abstract DP operator encoding a model; its monotonicity and contraction determine results (p. 143)
- [[dual-control]] (new) — Feldbaum's DP framework for adaptive control; estimation versus control (p. 147)
- [[exploration vs exploitation]] — author identifies it with Feldbaum's division of effort between estimation and control (p. 147)
- [[model predictive control]] — on-line optimization over a truncated rolling horizon with terminal cost approximation (p. 147)
- [[PID control]] — mentioned as applied in adaptive and robust control; Minorsky 1922 (p. 147)
- [[stability]] — in Ex. 1.9, a policy is stable if $J_\mu(x)<\infty$ for all $x$ (p. 162)
- [[Bellman equation / value function]] — for Ex. 1.9, $J^*(1)=\min\{1,\epsilon+J^*(1)\}$ (p. 162)

## Canonical instances
- [[tsp-rollout]] — 5-city TSP: heuristic 48, one-step rollout 37, optimal 20 (pp. 151–152)
- [[option-exercise-rollout]] — stock-selling DP; base heuristic 2.268, rollout 2.269; Monte Carlo accuracy matters (pp. 154–157)
- [[scalar-lq-riccati]] — Newton-step identity for $K_L$ (pp. 159–161)
- [[backgammon-rollout]] — origin of the name; truncated rollout with a neural-net estimate (pp. 143–144)
- [[single-state-ssp-instability]] — $\ell$-step region $\tilde J(1)>1-\ell\epsilon$ (p. 162)
- [[spiders-and-flies]], [[parking-problem]], [[cruise-control]] — exercise settings (pp. 153, 158–159)

## Bridges (candidates)
- [same-math] Lookahead from $\tilde K$ ↔ numerical analysis: one Newton iteration on the scalar Riccati equation — shown algebraically in Ex. 1.7.
- [structural-analogy] Dual control (estimation vs control) ↔ RL: exploration–exploitation tradeoff — the author identifies them (p. 147).
- [structural-analogy] MPC (rolling horizon plus terminal cost) ↔ rollout and approximation in value space — author links them (pp. 147–148).
- [metaphor] Region of stability ↔ control-theory stability margin: longer lookahead generally enlarges the set of cost estimates that give a stable policy (Ex. 1.9).

## Questions this raises
- Why can a poor $\tilde J$ inside the region of stability still give a bad policy, as the sharp error near the boundary suggests (Ex. 1.8)?
- How many Monte Carlo samples are needed before rollout reliably beats its base heuristic (Ex. 1.4: 20 samples not enough, 200 enough)?
- Is there a general condition under which multiagent (agent-by-agent) rollout keeps the cost improvement property?
- For which problems do truncated rollout and a learned terminal cost beat full rollout in practice?

## Exercises worth doing
- Ex. 1.2 (p. 152) — graphical Riccati, value iteration and Newton interpretation of lookahead, stability regions — difficulty: medium
- Ex. 1.3 (p. 153) — compare multiagent rollout, ordinary rollout and the base policy on spiders and flies — difficulty: medium
- Ex. 1.7 (b)–(c) (p. 161) — behavior outside the stability region; $\ell$-step quadratic convergence bound — difficulty: hard
- Ex. 1.8 (p. 161) — regions of stability and error versus $\tilde K$ for different lookahead lengths — difficulty: medium
- Ex. 1.9 (p. 162) — improper policies, instability, $\ell$-step region $1-\ell\epsilon$ — difficulty: hard

## Reading notes
- This part starts mid-Section 1.7 (the last paragraphs on optimization versus ML, p. 140). It runs through all of 1.8 and ends at Exercise 1.9(b), p. 162. Printed = pdf − 20.
- The text layer of the Fig. 1.8.1 page (p. 151) is garbled. I used the page image, where the cost matrix and tour costs are legible.
- In Ex. 1.4(c) (p. 157) the text says the optimal policy attains reward "2.4", but Fig. 1.8.2 (p. 155) shows 2.303 at $x_0=2$. The two figures disagree.
- On p. 157 the text says rollout with 200 samples (2.273) "performs nearly as well as the optimal" but "somewhat worse than" exact-value rollout. The exact-value rollout is printed as 2.269, so 2.273 is higher. The text is internally inconsistent here.
- In Ex. 1.6 the source uses $N$ both for the garage index and the number of stages.
- Ex. 1.4 (b) says the heuristic sells at price $\ge\beta x_0$; (c) says "exceeds". I kept the source's wording.
- Not given: solutions to Ex. 1.2, 1.3, 1.5, 1.6, 1.8, and 1.9 (only a partial answer to 1.9(b)); also none for Ex. 1.1(d) or 1.7(b)–(c). The bibliography is condensed here; reference keys such as [Ber22a] are the author's.
