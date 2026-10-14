---
id: bertsekas-2026-rlcourse/ch02-approximation-p5
work: bertsekas-2026-rlcourse
unit: "2 Approximation in Value Space - Rollout Algorithms (part 5/7): end of 2.7.4, 2.7.5–2.7.6, 2.8, 2.9 (to the start of autonomous multiagent rollout)"
pages: 269–295
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Rollout: Monte Carlo tree search, infinite control spaces, and multiagent rollout

## L0 — One line
Rollout can be made cheaper: by selective sampling (MCTS, with a hopefully small risk of worse performance), by optimization solvers for continuous controls (the certainty-equivalent variant loses cost improvement), and by choosing the components of a multi-component control one agent at a time, which keeps the cost-improvement guarantee at cost of order $nm$ instead of $n^m$.

## L1 — The gist (≤ 120 words)
Rollout improves a base policy by one-step lookahead plus simulation. This part asks how to keep it affordable. For stochastic problems: average cost-difference samples (no extra noise under a condition) and focus sampling with Monte Carlo tree search (MCTS), e.g. with the UCB rule (a bonus for rarely tried controls). For continuous controls: use a base heuristic that is itself an optimization, and certainty equivalence (fixing future disturbances at nominal values) to keep the problem small. For controls with $m$ components: choose components one at a time, needing order $nm$ base-policy evaluations per stage, not $n^m$. Proposition 2.9.1 shows this still guarantees no worse cost than the base policy. Without coordination between agents, cost can get worse (Example 2.9.3).

**Prerequisites:** finite-horizon dynamic programming and Q-factors; base policy and rollout (one-step lookahead with simulation); expectation and variance; basic nonlinear programming.

## L2 — Key ideas
- Averaging cost-difference samples (same $w_k$ for both controls) has no larger variance than differencing independent averages iff the two sample errors are nonnegatively correlated, Eq. (2.79). Condition (2.80) is sufficient for this. (pp. 269–270)
- MCTS spends simulation effort selectively: shorter trajectories with a terminal cost, early discarding of controls, and selective deeper lookahead. The next control to sample minimizes an exploitation index (usually the empirical mean cost) plus an exploration index (a bonus for rarely sampled controls), e.g. the UCB rule. (pp. 270–273)
- A randomized policy can be improved by shifting probability toward the rollout-best control, or toward the MCTS frequency counts. (p. 274)
- For infinite control sets, use a base heuristic that is an $(\ell-1)$-stage optimization, so rollout becomes one $\ell$-stage nonlinear or mixed-integer program. This needs a mathematical model, not just a simulator. (pp. 275–279)
- Stochastic problems can be handled by a stochastic first stage and certainty equivalence afterwards. The program then has $d(1+(N-k-1)m)$ variables, but the cost improvement property is lost. (pp. 279–283)
- Multiagent (agent-by-agent) rollout optimizes one control component at a time, using the already-chosen components for earlier agents and the base policy for later ones. It costs $O(nm)$ instead of $O(n^m)$ and keeps cost improvement (Prop. 2.9.1). (pp. 283–291)
- Choosing the agent order greedily costs $m(m+1)/2$ minimizations and can be parallelized in $m$ batches. (pp. 291–292)
- A poor base policy can give an excellent rollout policy: spiders-and-flies, vehicle routing. (pp. 286–288)
- If agents compute in parallel using base-policy guesses for their predecessors, cost can get worse than the base policy. A precomputed signaling policy (a guess of what each agent will do) is designed to play a coordination role. (pp. 294–295)

## L3 — Walkthrough

### 2.7.4 (end): Q-factor differences — why they reduce variance
The unit starts mid-argument. $D_k(x_k,u_k,w_k)$ is the simulation error of a cost sample, with $E\{D_k\}=0$; its definition comes before this unit. The comparison is between two ways of estimating $\tilde Q_{k,\pi}(x_k,u_k)-\tilde Q_{k,\pi}(x_k,\hat u_k)$:
- averaging samples of the cost *difference*, using the same $w_k$ for both controls (the "former" method), or
- differencing two independently obtained averages (the "latter" method).

The former has error variance no larger than the latter iff (p. 269)
$$E_{w_k,\hat w_k}\big\{|D_k(x_k,u_k,w_k)-D_k(x_k,\hat u_k,\hat w_k)|^2\big\}\ \ge\ E_{w_k}\big\{|D_k(x_k,u_k,w_k)-D_k(x_k,\hat u_k,w_k)|^2\big\}.$$
Expanding the squares and using $E\{D_k\}=0$ turns this into
$$E\{D_k(x_k,u_k,w_k)\,D_k(x_k,\hat u_k,w_k)\}\ \ge 0, \tag{2.79}$$
i.e. the two errors are nonnegatively correlated. (Added step: with independent errors the left side is $E|D|^2+E|\hat D|^2$; with the same $w_k$ the right side is $E|D|^2+E|\hat D|^2-2E[D\hat D]$. So the condition is $2E[D\hat D]\ge 0$.) The author says this is likely to hold in many problems (p. 269).

**Sufficient condition.** Suppose there is $\gamma<1$ such that for all $x_k,u_k,\hat u_k$
$$E\{|D_k(x_k,u_k,w_k)-D_k(x_k,\hat u_k,w_k)|^2\}\le \gamma\, E\{|D_k(x_k,u_k,w_k)|^2\}. \tag{2.80}$$
Roughly, this says that changing $u_k$ changes the error little relative to the randomness of $w_k$ (p. 269). Using $ab\ge a^2-|a|\,|b-a|$ (writing $D$ for $D_k(x_k,u_k,w_k)$ and $\hat D$ for $D_k(x_k,\hat u_k,w_k)$):
$$E\{D\hat D\}\ \ge\ E\{|D|^2\}-E\{|D|\,|\hat D-D|\}\ \ge\ E\{|D|^2\}-\tfrac12E\{|D|^2\}-\tfrac12E\{|\hat D-D|^2\}\ \ge\ \tfrac{1-\gamma}{2}E\{|D|^2\}.$$
The second step uses $-|a||b|\ge-\frac12(a^2+b^2)$. The third step uses (2.80) (p. 270). So under (2.80), (2.79) holds, and averaging cost-difference samples does not increase the simulation error variance (p. 270).

*Intuition note.* If both controls are simulated with the same random numbers, part of the noise is shared and cancels in the difference. By the author's rough argument, this helps (the variance does not increase) when the randomness of $w_k$ affects the error more than the change in $u_k$ does.

**Advantages.** When Q-factors are approximated by parametric architectures, it may be important to approximate and compare the differences $A_{k,\pi}(x_k,u_k)=Q_{k,\pi}(x_k,u_k)-\min_{u_k\in U_k(x_k)}Q_{k,\pi}(x_k,u_k)$. This is the *advantage* of the pair. It serves as well as $Q$ for comparing controls and may work better under approximation errors (p. 270). Details are deferred to Chapter 3.

### 2.7.5 Monte Carlo tree search
Plain simulation-based rollout draws the same large number of full-length trajectories from every pair $(x_k,u_k)$. Three drawbacks (p. 270):
- (a) trajectories may be too long;
- (b) clearly inferior controls waste sampling effort;
- (c) promising controls may deserve deeper multistep lookahead.

MCTS variants trade computation against a hopefully small risk of worse performance. They discard controls early and limit simulation (fewer samples, shorter horizon, or both) (p. 270).

Remedies (p. 271):
- For (a): use truncated trajectories with a terminal cost approximation. The cost can be zero, can come from an auxiliary calculation, or can come from a trained approximation (e.g. a neural network) of the base policy's cost. In an extreme case rollout is skipped (zero-length trajectories).
- For (b): a heuristic or statistical test discards controls early, even before any simulation (e.g. on the advice of a trained neural network).
- For (c): a heuristic lengthens the lookahead selectively, similar to the incremental multistep scheme of Section 2.4.2.

MCTS with multistep lookahead keeps a *lookahead tree*, expanded as Q-factors are evaluated by simulation. It balances exploitation (controls that look best) and exploration (inadequately sampled controls). Ideas from multiarmed bandit problems played an important role (p. 271). For one-step lookahead, MCTS aims to find efficiently the minimum of the expected values of finitely many random variables (p. 271).

**Example 2.7.5 (adaptive sampling, one-step lookahead).** At $x_k$ we want $\tilde u_k$ minimizing
$$\tilde Q_k(x_k,u_k)=E\{g_k(x_k,u_k,w_k)+\tilde J_{k+1}(f_k(x_k,u_k,w_k))\},$$
estimated by averaging samples. There are $m$ controls, labelled $1,\dots,m$. At sampling period $\ell$, control $i_\ell$ is chosen and a sample $S_{i_\ell}$ is drawn. After $n$ periods the empirical mean (for each control sampled at least once) is (p. 272)
$$Q_{i,n}=\frac{\sum_{\ell=1}^n\delta(i_\ell=i)S_{i_\ell}}{\sum_{\ell=1}^n\delta(i_\ell=i)},\qquad \delta(i_\ell=i)=\begin{cases}1&i_\ell=i\\0&i_\ell\ne i.\end{cases}$$
Declaring the control with minimal $Q_{i,n}$ "best" has a positive probability of error. Roughly speaking, adaptive sampling aims to design the selection and stopping rules to keep the error probability small (some effort on every control) and the number of samples limited (little effort on apparent losers) (p. 272).

The next control sampled minimizes $T_{i,n}+R_{i,n}$, an exploitation index plus an exploration index (p. 273). Usually $T_{i,n}=Q_{i,n}$. The exploration index depends on the count $s_i=\sum_{\ell=1}^n\delta(i_\ell=i)$. The frequently suggested **UCB rule** (upper confidence bound) is
$$R_{i,n}=-c\sqrt{\frac{\log n}{s_i}},$$
with $c>0$ chosen empirically. Some analysis suggests values near $c=\sqrt2$ if $Q_{i,n}$ is normalized to $[-1,0]$ (p. 273). The rule is from Auer, Cesa-Bianchi and Fischer; for trees it is called UCT. Its justification comes from multiarmed-bandit analysis and is beyond the book's scope. AlphaZero uses a different exploitation term that depends on lookahead depth (p. 273).

*Intuition note.* Costs are minimized, so $R_{i,n}$ is a bonus (negative number) that is larger in size for controls with few samples $s_i$. Rarely sampled controls get a better index and are tried again. This is the exploitation–exploration balance.

Multistep MCTS: a simulated trajectory is run from the tree node that minimizes the sum $T_{i,n}+R_{i,n}$. Schemes are problem-dependent (p. 273).

Applications (p. 273): AlphaGo combines MCTS with rollout using a base policy trained off-line by a deep neural network. AlphaZero critically relies on MCTS but does not use rollout in on-line play (it relies primarily on very long lookahead). Based on early tests, MCTS is not effective in computer backgammon. Its success appears problem-dependent and implementation-dependent.

### 2.7.6 Randomized policy improvement by MCTS
So far base and rollout policies are deterministic. AlphaGo and AlphaZero use MCTS to generate and train randomized policies (a distribution over moves at each position) (p. 274).
- A randomized policy can serve as a base policy in the same way as a deterministic one: sample trajectories with randomly selected controls and average the Q-factor samples. The resulting rollout policy is deterministic (p. 274).
- To get a randomized improved policy, increase the probability of the "best" control $\tilde\mu_k(x_k)$ by some amount, and decrease the others proportionally (p. 274).
- With MCTS, the frequency counts of controls (proportion of rollout trajectories per control) are available. Move the base probabilities in the direction of the counts: more probability for high-count controls, less for the others. The author calls this reminiscent of gradient-type methods and successful in some contexts (p. 274).

### 2.8 Rollout for infinite control spaces — optimization heuristics
With an infinite control set, one must otherwise discretize or sample, which can be inconvenient and ineffective. The alternative is a base heuristic that involves a continuous optimization, with a linear or nonlinear programming method solving the lookahead problem (p. 275).

#### 2.8.1 Deterministic problems
For $x_{k+1}=f_k(x_k,u_k)$ with stage cost $g_k$ (p. 275):
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k),\tag{2.81}$$
$$\tilde Q_k(x_k,u_k)=g_k(x_k,u_k)+H_{k+1}\big(f_k(x_k,u_k)\big),\tag{2.82}$$
where $H_{k+1}$ is the base heuristic's cost. If $H_{k+1}$ has a differentiable closed form and $g_k,f_k$ are differentiable in $u_k$, then $\tilde Q_k$ is differentiable and gradient methods apply. But closed-form $H_{k+1}$ is quite restrictive, and numerical differentiation may be inconvenient or unreliable (p. 275).

**Circumvention.** Let $H_{k+1}(x_{k+1})$ be the optimal cost of a related $(\ell-1)$-stage deterministic optimal control problem. Then (2.81)–(2.82) is implemented by solving one $\ell$-stage deterministic problem. It concatenates the minimization over $u_k$ with the $(\ell-1)$-stage minimization of the heuristic (Fig. 2.8.1). It may be solvable on-line by nonlinear programming or optimal control methods (pp. 275–276). Footnote (p. 276): this requires a mathematical model, not only a simulator. If the control space mixes discrete and continuous parts, mixed integer programming may be needed, or brute-force enumeration of the discrete part followed by continuous optimization. Model predictive control (Section 1.6.9) is a major paradigm of this type (p. 276).

**Example 2.8.1 (supply chain).** The system has a production center (stock $x^1_k$, production $u^1_k$) and a retail center (stock $x^2_k$; negative means backordered). Shipments $u^2_k$ arrive $\tau\ge1$ time units later. Demands $d_k$ are known over $N$ stages (p. 276–277). The system equations are
$$x^1_{k+1}=x^1_k+u^1_k-u^2_k,\qquad x^2_{k+1}=x^2_k+u^2_{k-\tau}-d_k.$$
The state includes the stock in transit $u^2_{k-\tau-1},\dots,u^2_{k-1}$, so exact DP needs state augmentation (p. 277). Cost per stage has three parts: production (depends on $x^1_k,u^1_k$), transportation (on $u^2_k$), and fulfillment (on $x^2_k$, penalizing both excess and backorders); their precise forms are immaterial (p. 277). The control is often continuous or mixed. At stage $k$, a heuristic optimization finds the stream of future production and shipment levels over $\ell$ steps, and the first component is applied. A sample base policy brings retail inventory to a target value $\ell$ stages ahead, possibly holding it there for part of the remaining periods. The resulting nonlinear or mixed integer program may be solvable far more efficiently than by discretized DP (p. 277). Footnote (p. 277): with large delays the augmented state space is very large, but rollout is not affected much, so it suits problems with delayed effects. Rollout also readily incorporates on-line replanning after demand changes, equipment failures or new forecasts (p. 278).

**Example 2.8.2 (multistage linear and mixed integer programming).** The dynamics are $x_{k+1}=A_kx_k+B_ku_k+d_k$ and the cost is $c_N'x_N+\sum_{k=0}^{N-1}(c_k'x_k+d_k'u_k)$. The constraints are $x_N\in T$ and $(x_k,u_k)\in P_k$, with linear and possibly integer constraints (p. 278). Multi-item production example: $x^i_{k+1}=\sum_{j=1}^na^{ij}_ku^{ij}_k-d^i_k$, with $u^{ij}_k$ the amount of product $i$ used to make product $j$, and $\sum_{j}u^{ij}_k\le x^i_k$ (p. 278). Exact solution by linear or mixed integer programming may be very time-consuming for large $N$ and may need to be redone on-line if data change and replanning is necessary. A suboptimal alternative is truncated rollout: an $\ell$-stage mixed integer optimization with a polyhedral terminal cost $\tilde J_{k+\ell}$. Options for the terminal cost: zero; a polyhedral lower bound from relaxing the integer constraints after stage $k+\ell$; or a data-trained function (p. 279).

#### 2.8.2 Rollout based on stochastic programming
**Example 2.8.3 (two-stage stochastic programming).** Choose $u_0\in U_0$ at cost $g_0(u_0)$. Then $w_0$ takes value $w^i$ with probability $p^i$ ($i=1,\dots,m$). Then choose $u^i_1\in U_1(u_0,w^i)$ at cost $g_1(u^i_1,w^i)$. Minimize $g_0(u_0)+\sum_{i=1}^mp^ig_1(u^i_1,w^i)$ (p. 279). As a DP: $x_1=w_0$, and a separate second-stage decision $u^i_1$ is computed for each $i$ (Fig. 2.8.3, p. 280). If $u_0\in\Re^{d_0}$ and $u_1\in\Re^{d_1}$, it is equivalently a nonlinear program of dimension $d_0+md_1$ (p. 280).

Generalization (p. 281): a two-stage stochastic DP with $w_0,w_1$ each taking $m$ values, with probabilities $p^i_0$ and $p^j_1$. Bringing the inner minimization outside the inner brackets shows that the DP algorithm is equivalent to the nonlinear program
$$\min\ \sum_{i=1}^mp^i_0\Big\{g_0(x_0,u_0,w^i)+\sum_{j=1}^mp^j_1\Big\{g_1\big(f_0(x_0,u_0,w^i),u^i_1,w^j\big)+g_2\Big(f_1\big(f_0(x_0,u_0,w^i),u^i_1,w^j\big)\Big)\Big\}\Big\}$$
$$\text{s.t. }u_0\in U_0(x_0),\quad u^i_1\in U_1\big(f_0(x_0,u_0,w^i)\big),\ i=1,\dots,m, \tag{2.83}$$
with $d(1+m)$ scalar variables if controls lie in $\Re^d$ (p. 281). For $N$ stages the number of variables grows exponentially in $N$. With $m$ the maximum number of disturbance values per stage and $d$ the control dimension, the number is bounded by $d(1+m+m^2+\dots+m^{N-1})$ (p. 281).

#### 2.8.3 Stochastic rollout with certainty equivalence
To shrink this program, use stochastic optimization at the current stage and deterministic optimization with assumed certainty equivalence afterwards, with the base policy. Given $x_k,u_k$, the next states are $x^i_{k+1}=f_k(x_k,u_k,w^i_k)$ with probabilities $p^i_k$. The approximate Q-factor and rollout control are (p. 282)
$$\tilde Q_k(x_k,u_k)=\sum_{i=1}^mp^i_k\Big(g_k(x_k,u_k,w^i_k)+\tilde H_{k+1}(x^i_{k+1})\Big),\tag{2.84}$$
$$\tilde\mu_k(x_k)\in\arg\min_{u_k\in U_k(x_k)}\tilde Q_k(x_k,u_k).\tag{2.85}$$
Here $\tilde H_{k+1}(x^i_{k+1})$ is the cost of a base policy that, from $x^i_{k+1}$, optimizes the cost-to-go assuming future disturbances $w_{k+1},\dots,w_{N-1}$ take nominal values $\overline w_{k+1},\dots,\overline w_{N-1}$. This algorithm does *not* have the cost improvement property, because $\tilde H_{k+1}$ is the cost of a policy applied to the certainty-equivalent version of the problem, which only approximates the policy's true cost (p. 282).

Problem (2.85) is a seamless $(N-k)$-stage deterministic optimization involving $u_k$ and, for each disturbance value $w^i_k$, a control sequence $(u^i_{k+1},\dots,u^i_{N-1})$. If controls lie in $\Re^d$, it has
$$d\big(1+(N-k-1)m\big)\tag{2.86}$$
scalar variables. Deterministic software, especially for linear programming, handles very large numbers of variables, so very large continuous problems can be addressed. The author cites Hu et al. for maintenance scheduling (p. 282).

*Intuition note.* The exponential tree of stochastic programming is kept only for one stage. After that, every branch follows one deterministic path, so the size grows only linearly in the horizon.

**Multistep variant.** Treat uncertainty fully in the first $\ell$ stages and by certainty equivalence in the remaining $N-k-\ell$ (assume $\ell<N-k$). The number of variables is $d\big(1+m+\dots+m^{\ell-1}+(N-k-\ell)m^\ell\big)$. Apply the first control $\tilde u_k$ and discard $\{\tilde\mu_{k+1},\tilde\mu_{k+2},\dots\}$. This can be combined with multiagent rollout (p. 283).

### 2.9 Multiagent rollout
**Setup.** The control has $m$ components, $u_k=(u^1_k,\dots,u^m_k)$, and the constraint set is a Cartesian product (each component chosen by a separate "agent"; each set finite):
$$U_k(x_k)=U^1_k(x_k)\times\dots\times U^m_k(x_k).\tag{2.87}$$
The one-step lookahead
$$\tilde u_k\in\arg\min_{u_k\in U_k(x_k)}E\{g_k(x_k,u_k,w_k)+J_{k+1,\pi}(f_k(x_k,u_k,w_k))\}\tag{2.88}$$
involves up to $n^m$ Q-factors, where $n$ is the maximum size of the sets $U^\ell_k(x_k)$. Standard rollout therefore needs $O(n^m)$ base-policy cost computations per stage (p. 283). Multiagent (agent-by-agent) rollout achieves
$$J_{k,\tilde\pi}(x_k)\le J_{k,\pi}(x_k),\quad\forall x_k,k,\tag{2.89}$$
with only $O(nm)$ computations per stage (pp. 283–284).

**Mechanism.** Rollout computation grows with the size of the control space and not with the size of the state space. So "unfold" $u_k$ into its $m$ components and insert artificial intermediate states $(x_k,u^1_k),\dots,(x_k,u^1_k,\dots,u^{m-1}_k)$. The transitions through these states cost zero. The last component $u^m_k$ triggers $x_{k+1}=f_k(x_k,u_k,w_k)$ and the stage cost $g_k$ (Fig. 2.9.1, p. 284). The reformulated problem is equivalent to the original: each policy corresponds to a policy of the other with the same cost function. Footnote (p. 284): by substituting the earlier agents' control functions, each agent's control can be viewed as a function of $x_k$ alone, so the multi-transition structure cannot reduce cost beyond what a single transition achieves.

**Algorithm.** Apply standard rollout to the reformulated problem with a base policy $\pi=\{\mu_0,\dots,\mu_{N-1}\}$, $\mu_k=(\mu^1_k,\dots,\mu^m_k)$. At each stage there are $m$ minimizations, one per agent. The past components are the already-chosen rollout controls, and the future components come from the base policy (p. 285). At $(x_k,u^1_k,\dots,u^{\ell-1}_k)$ and for each $u^\ell_k\in U^\ell_k(x_k)$, simulate trajectories to stage $N$ with all future controls from the base policy. Average their costs to get Q-factors, and pick the $u^\ell_k$ with the minimal one. Cost is $O(n)$ per intermediate state, $O(nm)$ per stage (p. 285).

On-line multiagent operation assumes (p. 285): (a) all agents know the current $x_k$ and the base policy (all agents' control functions); (b) there is an order in which agents compute and apply their controls; (c) agents share information, so agent $\ell$ knows $u^1_k,\dots,u^{\ell-1}_k$. The resulting rollout policy may differ from that of standard rollout, but needs far less computation and keeps (2.89) (p. 286).

**Example 2.9.1 (spiders and flies).** Two spiders and two flies lie on integer points of a line. The flies are fixed (the problem is similar if they move randomly). Each spider moves one unit left or right. The goal is to minimize the time to capture both flies (p. 286). The optimal policy sends the spiders toward different flies; the minimal capture time is the maximum of the initial distances of the two spider-fly pairs of the optimal policy (p. 286). The base policy moves each spider one unit toward the closest fly (ties go to the right-side fly). It is poor: both spiders may move the same way unnecessarily, because each acts selfishly (pp. 286–287).

Multiagent rollout, at a stage where both spiders are closest to fly 2 (Fig. 2.9.2): spider 1 compares the Q-factors of left and right, with spider 2 and later moves following the base policy. It moves away from spider 2, even if this increases its distance to its closest fly, because it recognizes that spider 2 will capture fly 2 earlier. Then spider 2 acts similarly (p. 287). The algorithm induces implicit coordination and can be verified to produce an optimal move sequence from any initial positions; ordinary rollout also does (p. 287). The author concludes that a poor base heuristic can give an excellent rollout solution, because rollout is "farsighted" (p. 287). In a two-dimensional version (flies at two corners of a square, spiders starting from the same position), the spiders separate under the rollout policy, but move in unison under the base policy (p. 287).

**Example 2.9.2 (multi-vehicle routing).** $m$ vehicles move on a graph to perform tasks at nodes in a minimum number of vehicle moves. The state (positions plus pending tasks) and the number of joint moves both grow exponentially (p. 289). Base heuristic: each vehicle moves one step toward its closest pending task (in number of moves). Multiagent rollout takes the vehicles one at a time, comparing the Q-factors of that vehicle's moves, assuming the other moves follow the base heuristic and accounting for moves and tasks already done. This considers a number of moves polynomial in $m$ per stage (p. 289). In the instance of Fig. 2.9.3, vehicles start at nodes 1 and 2, with pending tasks at nodes 7 and 9. The base heuristic sends both vehicles to node 4; its trajectory is $1\to4\to7$ for vehicle 1 and $2\to4\to7\to10\to12\to9$ for vehicle 2, at total cost 7. One-vehicle-at-a-time rollout first moves vehicle 1 to node 3, then vehicle 2 to node 4. It ends with the optimal solution (vehicle 1 to node 9 in three moves, vehicle 2 to node 7 in two), at total cost 5 (p. 288). Footnote (p. 289): an alternative base heuristic also chooses vehicle by vehicle, and may differ when one vehicle's move changes a task's status.

**Cost improvement.** It is unclear which of standard and agent-by-agent rollout attains lower cost (p. 289). Footnote (pp. 289–290): in a single-stage problem, if the base control $u_0$ is not optimal but cannot be improved by changing any single component, multiagent rollout stays at $u_0$, while standard rollout finds an optimal control. This resembles coordinate descent, which can get stuck. In multistage rollout with possibly stochastic disturbances the consequences appear not serious, and multi-stage examples exist where multiagent rollout does better. Both rollout policies are no worse than the base policy (p. 290).

**Proposition 2.9.1 (cost improvement for multiagent rollout).** The multiagent rollout policy $\tilde\pi$ satisfies $J_{k,\tilde\pi}(x_k)\le J_{k,\pi}(x_k)$ for all $x_k$ and $k$ (2.90), where $\pi$ is the base policy (p. 290).

*Proof sketch (case $m=2$; general $m$ "entirely similar").* Induction. At $k=N$: $J_{N,\tilde\pi}=J_{N,\pi}=g_N$. Assume the claim at $k+1$. Then
$$\begin{aligned}J_{k,\tilde\pi}(x_k)&=E\{g_k(x_k,\tilde\mu^1_k,\tilde\mu^2_k,w_k)+J_{k+1,\tilde\pi}(f_k(x_k,\tilde\mu^1_k,\tilde\mu^2_k,w_k))\}\\&\le E\{g_k(x_k,\tilde\mu^1_k,\tilde\mu^2_k,w_k)+J_{k+1,\pi}(f_k(x_k,\tilde\mu^1_k,\tilde\mu^2_k,w_k))\}\\&=\min_{u^2_k\in U^2_k(x_k)}E\{g_k(x_k,\tilde\mu^1_k,u^2_k,w_k)+J_{k+1,\pi}(f_k(x_k,\tilde\mu^1_k,u^2_k,w_k))\}\\&\le E\{g_k(x_k,\tilde\mu^1_k,\mu^2_k,w_k)+J_{k+1,\pi}(f_k(x_k,\tilde\mu^1_k,\mu^2_k,w_k))\}\\&=\min_{u^1_k\in U^1_k(x_k)}E\{g_k(x_k,u^1_k,\mu^2_k,w_k)+J_{k+1,\pi}(f_k(x_k,u^1_k,\mu^2_k,w_k))\}\\&\le E\{g_k(x_k,\mu^1_k,\mu^2_k,w_k)+J_{k+1,\pi}(f_k(x_k,\mu^1_k,\mu^2_k,w_k))\}=J_{k,\pi}(x_k).\end{aligned}$$
Here the arguments of $\tilde\mu^1_k,\tilde\mu^2_k,\mu^1_k,\mu^2_k$ are $x_k$. Justifications given (p. 291): the first equality is the DP equation of $\tilde\pi$; the first inequality is the induction hypothesis; the second equality is the rollout definition for agent 2; the third is the rollout definition for agent 1; the fourth is the DP equation of $\pi$. (Added step: the other two "$\le$" hold because a minimum over a set is at most its value at the base control $\mu^2_k$, respectively $\mu^1_k$.)

*Intuition note.* Each agent's minimization can only do better than keeping the base control. So each agent's step, taken in turn, can only lower the expected cost, and the chain of inequalities ends at the base policy's cost.

**Optimizing the agent order (multiagent parallelization).** At each stage, solve the $m$ single-agent minimizations in which each agent in turn is first. Fix as first the agent $\ell_1$ with the minimal Q-factor. Then solve $m-1$ problems for the second slot, and so on. The total number of minimizations is
$$m+(m-1)+\dots+1=\frac{m(m+1)}2.\tag{2.91}$$
This likely gives substantially better performance and removes the need to guess an order. It increases the Q-factor calculations by roughly a factor $(m+1)/2$, which is still far below the exponential all-at-once approach. With $m$ parallel processors the minimizations take $m$ batches, about the same time as a fixed order. The cost improvement proof still holds by induction when the order varies by stage (p. 292).

**Variants (pp. 292–293).**
- (a) Truncated rollout and terminal cost approximation (cost improvement need not hold).
- (b) Infinite sets $U^\ell_k(x_k)$ (intervals): use one-dimensional search for each agent.
- (c) Deterministic problems may use a general heuristic instead of a base policy. If the sequential improvement assumption fails for the modified problem, cost improvement may fail, but fortification (Section 2.3.2) can restore it.
- (d) Infinite horizon: policy iteration, viewed as repeated rollout, with agent-by-agent improvement. [Ber21a] analyses exact policy evaluation with agent-by-agent improvement and shows convergence to an agent-by-agent optimal policy, a form of locally optimal policy.
- (e) Deterministic continuous-time problems (Section 2.6) with $u(t)=(u^1(t),\dots,u^m(t))$.
- (f) Q-factor differences, to handle base-policy cost approximation errors that may overwhelm $g_k$ (see advantage updating in Chapter 3).

**Constrained multiagent rollout.** With the same Cartesian structure and the same unfolding into intermediate states, rollout requires $m$ minimizations of $O(n)$ each, $O(nm)$ per stage. The standard rollout minimization (2.47) involves up to $n^m$ terms $G(T_k(\tilde y_k,u_k))$ (p. 293). (Eq. (2.47) is defined earlier in the chapter, outside this unit.)

### 2.9.1 Asynchronous and autonomous multiagent rollout
In an asynchronous scheme, agent $\ell$ computes its rollout control before knowing the rollout controls of some agents $1,\dots,\ell-1$, and uses their base policy controls $\mu^1_k(x_k),\dots,\mu^{\ell-1}_k(x_k)$ instead. This often works well, but it lacks the cost improvement property (p. 294).

**Example 2.9.3 (cost deterioration without coordination).** Two agents, a single state, controls $u^1_k,u^2_k\in\{0,1\}$. The stage cost is 0 if $u^1_k\ne u^2_k$, 1 if both are 0, and 2 if both are 1. The base policy applies $u^1_k=u^2_k=0$ (cost 1 per stage). When both agents do rollout assuming the other uses the base control, the first agent applies $u^1_k=1$. The second, not knowing this, also applies $u^2_k=1$, so the cost is 2 per stage. If agent 2 knows agent 1's choice, it applies $u^2_k=0$, giving the optimal cost 0 per stage (p. 294).

The author speculates that if agents are "weakly coupled" (one agent's choice has little impact on the desirability of other agents' controls), a more flexible communication pattern may suffice. Footnote (p. 295): agents could be split into coupled groups (e.g. by geographic proximity), coordinating only within each group; groups may compute in parallel.

**Autonomous multiagent rollout with signaling policies.** Agents do not communicate their computed controls. Instead, once they know the state, they use precomputed (or easily computed) approximations of the preceding agents' controls and compute in parallel and asynchronously. This has some redundant computation but allows more speedup (p. 295). Besides the base policy $\mu_k$, a *signaling policy* $\hat\mu_k=\{\hat\mu^1_k,\dots\}$ is computed off-line and known to all agents. Intuitively, $\hat\mu^\ell_k(x_k)$ is an intelligent "guess" of what agent $\ell$ will do at $x_k$, used by all other agents (p. 295). The part ends mid-sentence, as the text begins to define the rollout policy $\tilde\pi$ generated by base and signaling policies.

## Toy example (ours, not from the text)
One stage, state $x$, two agents with controls in $\{0,1\}$ ($n=2$, $m=2$). Suppose the total cost (stage cost plus the base policy's cost-to-go, found by simulation) is given by this table. The base policy chooses $(0,0)$.

| $(u^1,u^2)$ | (0,0) | (0,1) | (1,0) | (1,1) |
|---|---|---|---|---|
| $Q$ | 5 | 4 | 3 | 1 |

- Standard rollout evaluates all $n^m=2^2=4$ pairs and picks $(1,1)$, with cost 1.
- Agent-by-agent rollout, agent 1 first: with agent 2 at its base control 0, compare $Q(0,0)=5$ and $Q(1,0)=3$, so $u^1=1$. Agent 2 then, with $u^1=1$ fixed, compares $Q(1,0)=3$ and $Q(1,1)=1$, so $u^2=1$. The result is $(1,1)$, cost 1.
- Cost chain: $5\ (\text{base})\ \ge 3\ \ge 1$. Each agent step cannot raise the cost, which is the mechanism of Proposition 2.9.1.
- Counting: here $nm=4$ equals $n^m=4$, so there is no saving. For $n=2,m=10$: $2^{10}=1024$ versus $2\cdot10=20$. For $n=3,m=4$: $81$ versus $12$.
- Coordination matters: if agent 2 had ignored agent 1's choice and assumed agent 1 uses base control 0, it would compare $Q(0,0)=5$ and $Q(0,1)=4$ and choose 1. Here that gives $(1,1)$ by luck. With the costs of Example 2.9.3 the same reasoning gives deterioration.

## Concepts
- [[rollout-algorithm]] (new) — one-step (or multistep) lookahead with a base policy's cost estimated by simulation or optimization; the resulting policy is no worse than the base for standard and multiagent rollout (p. 290), but not necessarily for truncated or certainty-equivalent variants (pp. 282, 292); see also pp. 275, 283
- [[base-policy]] (new) — the given policy or heuristic whose cost rollout improves (pp. 274, 275, 285)
- [[q-factor]] (new) — cost of applying a control now and then following a given policy; here estimated by sampling (pp. 269, 272)
- [[advantage]] (new) — $A(x,u)=Q(x,u)-\min_uQ(x,u)$; used to compare controls under approximation errors (p. 270)
- [[monte-carlo-tree-search]] (new) — adaptive, selective sampling plus lookahead tree to save simulation effort (pp. 270–273)
- [[ucb-rule]] (new) — exploration index $R_{i,n}=-c\sqrt{\log n/s_i}$ added to the empirical mean (p. 273)
- exploration vs exploitation — in MCTS: sample the best-looking control vs the poorly sampled ones (pp. 271–273)
- [[certainty-equivalence]] (new) — fix future disturbances at nominal values and optimize deterministically (p. 282)
- [[stochastic-programming]] (new) — stochastic optimal control written as one large deterministic program with a decision per scenario (pp. 279–281)
- model predictive control — cited as a major paradigm of $\ell$-stage lookahead optimization (p. 276)
- [[multiagent-rollout]] (new) — agent-by-agent minimization of control components, cost $O(nm)$ per stage, keeps cost improvement (pp. 283–285)
- [[cost-improvement-property]] (new) — $J_{k,\tilde\pi}\le J_{k,\pi}$; holds for multiagent rollout (Prop. 2.9.1), not for the certainty-equivalent or asynchronous variants (pp. 282, 290, 294)
- [[signaling-policy]] (new) — a precomputed policy giving each agent a guess of the predecessors' controls (p. 295)
- policy — here also randomized policies, mapping a state to a probability distribution over controls (p. 274)

## Canonical instances
- [[spiders-and-flies]] — poor base policy, excellent (here optimal) rollout via implicit coordination (pp. 286–287)
- [[multi-vehicle-routing]] — base cost 7 vs rollout cost 5; polynomial rather than exponential in $m$ (pp. 288–289)
- [[supply-chain-delay]] — rollout with continuous controls, delays and on-line replanning (pp. 276–278)
- [[two-stage-stochastic-programming]] — DP over scenarios equals a nonlinear program of dimension $d(1+m)$ (pp. 279–281)
- [[agent-coordination-failure]] — Example 2.9.3: rollout cost 2 vs base cost 1 (p. 294)
- [[alphago-alphazero]] — MCTS, with or without rollout, in games; MCTS tested as ineffective in backgammon (pp. 273–274)

## Bridges (candidates)
- [structural-analogy] UCB exploration bonus ↔ multiarmed bandits: confidence-bound action selection — the author says the UCB justification comes from bandit analysis (p. 273).
- [structural-analogy] Agent-by-agent rollout ↔ optimization: coordinate descent on a function of $m$ components — the author's own footnote (p. 290).
- [structural-analogy] Certainty-equivalent rollout ↔ control theory: optimizing with future disturbances fixed at nominal values, as in model predictive control (p. 276).
- [structural-analogy] Trading control-space size for state-space size (Fig. 2.9.1) ↔ DP: state augmentation (also used for delays, p. 277).
- [metaphor] Frequency-count policy update in MCTS ↔ gradient-style policy improvement (p. 274, "reminiscent of gradient-type methods").

## Questions this raises
- When does the sample-error correlation (2.79) fail, so that cost-difference averaging would increase variance?
- How much does agent order matter in practice, and when does greedy ordering (2.91) fail to find a good order?
- How do signaling policies keep (or approximately keep) cost improvement without sharing rollout controls?
- When is the certainty-equivalence approximation badly wrong, given that its cost improvement is lost?

## Reading notes
- This part starts at printed p. 269, in the middle of the discussion of Q-factor differences in Sec. 2.7.4. It ends at p. 295, in the middle of the sentence defining the autonomous multiagent rollout policy $\tilde\pi$. Printed page = pdf − 20.
- The text layer of p. 269 is garbled (arrows for minus signs); I checked the equations against the page image.
- The definition of $D_k$ and the earlier sections (2.7.4 beginning, 2.4.2, 2.3.2, Eq. (2.47), (2.77)) are outside this unit.
- Page 289 text says vehicles are taken "in the order $1,\dots,n$", although $m$ is the number of vehicles elsewhere; page 295 writes the base and signaling policies with indices up to $m-1$. I report both as printed.
- The source labels Example 2.8.1's inventory "ℓ stages ahead" target with the same letter $\ell$ as agent indices elsewhere; I kept the author's usage.
- No exercises appear in this part.
