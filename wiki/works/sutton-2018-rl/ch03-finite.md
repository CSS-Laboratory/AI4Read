---
id: sutton-2018-rl/ch03-finite
work: sutton-2018-rl
unit: "Chapter 3 — Finite Markov Decision Processes"
pages: 47-71
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Finite Markov Decision Processes

## L0 — One line
A finite MDP formalizes goal-directed interaction as states, actions and rewards with probabilistic dynamics; the goal is a policy that maximizes expected discounted return, characterized by value functions that satisfy Bellman equations.

## L1 — The gist (≤ 120 words)
How can learning from interaction to achieve a goal be stated precisely? The chapter defines the finite Markov decision process (MDP). An agent chooses actions. The environment returns a next state and a numerical reward, with probabilities given by one dynamics function $p$. The agent's goal is to maximize expected (discounted) return (the sum of future rewards, weighted less for later steps). Value functions $v_\pi$ and $q_\pi$ score states and actions under a policy (a rule for choosing actions) and satisfy recursive Bellman equations. The optimal value functions satisfy the Bellman optimality equations, and acting greedily with respect to them gives an optimal policy. Exact solution is rarely feasible (too much computation or memory, unknown dynamics), so reinforcement learning usually has to approximate.

**Prerequisites:** discrete probability and conditional expectation; summation notation; geometric series; the idea of a function of several arguments.

## L2 — Key ideas
- **One function defines the environment.** The four-argument $p(s',r\mid s,a)$ gives the joint probability of next state and reward, and every other quantity (transition probabilities, expected rewards) follows from it (pp. 48–49).
- **The Markov property is a demand on the state.** The state must carry everything from the past that matters for the future (p. 49).
- **The agent–environment boundary is the limit of the agent's control, not of its knowledge.** Anything the agent cannot change arbitrarily, including the reward computation, is environment (p. 50).
- **The goal is encoded as a scalar reward.** The reward says what to achieve, not how; subgoals should not be rewarded (pp. 53–54).
- **Return and discounting.** $G_t=\sum_k\gamma^kR_{t+k+1}$ handles continuing tasks. It obeys $G_t=R_{t+1}+\gamma G_{t+1}$ (pp. 55–57).
- **Value functions satisfy the Bellman equation.** $v_\pi$ is the unique solution of a recursive consistency condition, which is the basis of many computation and learning methods (pp. 58–60).
- **Optimal value functions obey Bellman optimality equations.** A policy greedy with respect to $v_*$ is optimal, so a one-step search suffices (pp. 62–65).
- **Exact solution is usually impractical, so approximation is the norm.** Memory, computation and unknown dynamics force it; focusing effort on frequently met states is a key opportunity (pp. 66–68).

## L3 — Walkthrough

### Chapter introduction (p. 47)
- A finite MDP has evaluative feedback, as in bandits. It also has an associative aspect: different actions are chosen in different situations (p. 47).
- Actions affect not only immediate reward but also later states and so later rewards. So there is delayed reward and a need to trade off immediate against delayed reward (p. 47).
- Bandits estimate $q_*(a)$. MDPs estimate $q_*(s,a)$ for each action in each state, or $v_*(s)$ for each state under optimal actions (p. 47).
- The authors name a tension between breadth of applicability and mathematical tractability (p. 47).

### 3.1 The Agent–Environment Interface
- **Agent** = learner and decision maker. **Environment** = everything outside it. Footnote 1: these terms replace the engineers' *controller*, *controlled system (plant)* and *control signal* because they are meaningful to a wider audience (pp. 47–48).
- Time is discrete: $t=0,1,2,\dots$. At step $t$ the agent sees $S_t\in\mathcal S$ and chooses $A_t\in\mathcal A(s)$. One step later it receives a reward $R_{t+1}\in\mathcal R\subset\mathbb R$ and finds itself in $S_{t+1}$ (p. 48).
- Footnote 4: $R_{t+1}$ rather than $R_t$ stresses that $R_{t+1}$ and $S_{t+1}$ are jointly determined (p. 48). The resulting trajectory is
$$S_0,A_0,R_1,S_1,A_1,R_2,S_2,A_2,R_3,\dots \tag{3.1}$$
- In a *finite* MDP, $\mathcal S$, $\mathcal A$, $\mathcal R$ have finitely many elements. Then $S_t,R_t$ have discrete distributions that depend only on the preceding state and action (p. 48). The **dynamics** are
$$p(s',r\mid s,a)\doteq\Pr\{S_t=s',R_t=r\mid S_{t-1}=s,A_{t-1}=a\} \tag{3.2}$$
  with $p:\mathcal S\times\mathcal R\times\mathcal S\times\mathcal A\to[0,1]$ (p. 48). It is an ordinary function. The "|" only signals that $p$ is a probability distribution for each $(s,a)$:
$$\sum_{s'\in\mathcal S}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1\quad\text{for all }s\in\mathcal S,\ a\in\mathcal A(s). \tag{3.3}$$
- **Markov property.** The probabilities of $S_t,R_t$ depend on $S_{t-1},A_{t-1}$ and, given those, not at all on earlier states and actions. The authors view this as a restriction on the *state*. The state must include all aspects of past interaction that make a difference for the future. If it does, it has the Markov property. The book assumes it throughout (p. 49). Later parts treat approximation methods that do not rely on it, and Chapter 17 treats constructing a Markov state from non-Markov observations (p. 49).
- Everything else can be computed from $p$ (p. 49):
$$p(s'\mid s,a)\doteq\Pr\{S_t=s'\mid S_{t-1}=s,A_{t-1}=a\}=\sum_{r\in\mathcal R}p(s',r\mid s,a) \tag{3.4}$$
$$r(s,a)\doteq\mathbb E[R_t\mid S_{t-1}=s,A_{t-1}=a]=\sum_{r\in\mathcal R}r\sum_{s'\in\mathcal S}p(s',r\mid s,a) \tag{3.5}$$
$$r(s,a,s')\doteq\mathbb E[R_t\mid S_{t-1}=s,A_{t-1}=a,S_t=s']=\sum_{r\in\mathcal R}r\,\frac{p(s',r\mid s,a)}{p(s'\mid s,a)} \tag{3.6}$$
  The book mostly uses the four-argument $p$ (p. 49).
- **Flexibility** (pp. 49–50): time steps need not be fixed real-time intervals. Actions may be low-level (motor voltages) or high-level (go to graduate school), or even mental (what to think about). States may be raw sensor readings, symbolic descriptions, memory-based, or subjective (e.g. being unsure where an object is). In general, actions can be any decisions we want to learn to make, and states anything we can know that might help in making them (p. 50).
- **Boundary.** The boundary is usually drawn closer to the agent than the physical body. Motors, linkages, sensing hardware, muscles and sensory organs should usually be considered part of the environment. Rewards, too, are presumably computed inside the body but are considered external (p. 50).
  - Rule: anything the agent cannot change arbitrarily is outside it. The reward computation is always external because it defines the task. The agent may know all of how the environment works and still face a hard task, like a Rubik's cube (p. 50). In the authors' words: "The agent–environment boundary represents the limit of the agent's absolute control, not of its knowledge." (p. 50)
  - Many agents with different boundaries may operate in one robot. In practice, the boundary is determined once states, actions and rewards are chosen (p. 50).
- The framework reduces goal-directed learning to three signals: actions (choices), states (basis of choice), rewards (the goal). It may not be sufficient to represent all decision-learning problems usefully, but it has proved widely useful. Choosing representations is "more art than science" at present (p. 50).

**Examples**
- **Ex. 3.1 Bioreactor.** Actions: target temperatures and stirring rates passed to lower-level controllers. States: sensor readings (perhaps filtered and delayed) plus symbolic inputs about the ingredients. Rewards: moment-by-moment rate of useful chemical production. Here states and actions are vectors, which is typical of RL tasks; rewards, on the other hand, are always single numbers (p. 51).
- **Ex. 3.2 Pick-and-place robot.** Actions: motor voltages. States: joint angles and velocities. Reward: +1 per object placed; to encourage smooth movement, a small negative reward per step, as a function of jerkiness, could be added (p. 51).
- **Ex. 3.3 Recycling robot** (pp. 52–53). States $\mathcal S=\{\text{high},\text{low}\}$ (battery charge). $\mathcal A(\text{high})=\{\text{search},\text{wait}\}$, $\mathcal A(\text{low})=\{\text{search},\text{wait},\text{recharge}\}$.
  - Search from high stays high with probability $\alpha$, drops to low with $1-\alpha$. Search from low stays low with probability $\beta$. With probability $1-\beta$ the battery is depleted, the robot is rescued (reward $-3$) and the battery returns to high. Each can is a unit reward. $r_{\text{search}}>r_{\text{wait}}$ are the expected rewards of searching and waiting (p. 52).

| $s$ | $a$ | $s'$ | $p(s'\mid s,a)$ | $r(s,a,s')$ |
|---|---|---|---|---|
| high | search | high | $\alpha$ | $r_{\text{search}}$ |
| high | search | low | $1-\alpha$ | $r_{\text{search}}$ |
| low | search | high | $1-\beta$ | $-3$ |
| low | search | low | $\beta$ | $r_{\text{search}}$ |
| high | wait | high | 1 | $r_{\text{wait}}$ |
| high | wait | low | 0 | – |
| low | wait | high | 0 | – |
| low | wait | low | 1 | $r_{\text{wait}}$ |
| low | recharge | high | 1 | 0 |
| low | recharge | low | 0 | – |

  - A **transition graph** shows the same dynamics. It has state nodes (large open circles) and action nodes (small solid circles, one per state–action pair). Each arrow leaving an action node is labelled with $p(s'\mid s,a)$ and $r(s,a,s')$. Arrow probabilities leaving an action node sum to 1 (p. 53).

> **Intuition note.** An MDP is just a table of "from this situation, with this choice, what happens next and how much do I get?", stated as probabilities. The Markov property says the "situation" already contains all the history that matters.

### 3.2 Goals and Rewards
- The goal is formalized by a reward signal $R_t\in\mathbb R$ passing from environment to agent. The agent maximizes cumulative reward in the long run, not immediate reward (p. 53).
- **Reward hypothesis:** all of what we mean by goals and purposes can be well thought of as maximizing the expected value of the cumulative sum of a scalar reward signal (p. 53). This is one of the most distinctive features of RL (p. 53).
- Examples (p. 53): a walking robot gets reward proportional to forward motion. A maze robot gets a negative reward per time step before escape (the text layer shows "1"; the sign is lost, but "escape as quickly as possible" implies negative). A can-collecting robot gets 0 mostly and +1 per can, possibly negative rewards for bumping. Chess/checkers: +1 win, −1 loss, 0 draw and all nonterminal positions (text layer lost the minus on the loss reward).
- The agent maximizes its reward, so rewards must truly indicate what we want achieved. The reward is *not* the place for prior knowledge about how to achieve it. A chess agent should be rewarded only for winning, not for subgoals like taking pieces, because it might achieve those and lose. The reward says what, not how (p. 54). Footnote 5 says better places for prior knowledge are the initial policy or initial value function (p. 54).

### 3.3 Returns and Episodes
- The agent maximizes the expected **return** $G_t$, a function of the reward sequence $R_{t+1},R_{t+2},\dots$ (p. 54). The simplest case is the plain sum
$$G_t\doteq R_{t+1}+R_{t+2}+\dots+R_T \tag{3.7}$$
  with final step $T$. This suits **episodic tasks**, where interaction breaks into *episodes* (plays of a game, trips through a maze). Each ends in a **terminal state**, followed by a reset to a standard start or a sample from a start distribution (p. 54).
- The next episode begins independently of how the last one ended, so all episodes can be treated as ending in one terminal state with different rewards. $\mathcal S$ denotes nonterminal states and $\mathcal S^+$ all states plus the terminal state. $T$ is a random variable (p. 54).
- **Continuing tasks** do not break into episodes (process control, long-lived robot). Then $T=\infty$ and (3.7) can easily be infinite (e.g. +1 every step) (pp. 54–55).
- **Discounted return** (p. 55):
$$G_t\doteq R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\dots=\sum_{k=0}^\infty\gamma^kR_{t+k+1},\qquad 0\le\gamma\le1 \tag{3.8}$$
  - A reward $k$ steps ahead is worth $\gamma^{k-1}$ times an immediate one (p. 55).
  - If $\gamma<1$, the infinite sum is finite as long as the reward sequence is bounded (p. 55).
  - If $\gamma=0$ the agent is "myopic": it maximizes only $R_{t+1}$. If each action influenced only the immediate reward, a myopic agent could maximize (3.8) by maximizing each immediate reward separately. In general, maximizing immediate reward can reduce the return. As $\gamma\to1$ future rewards count more strongly (p. 55).
- **Recursion** (p. 55):
$$\begin{aligned}G_t&\doteq R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\gamma^3R_{t+4}+\cdots\\&=R_{t+1}+\gamma\big(R_{t+2}+\gamma R_{t+3}+\gamma^2R_{t+4}+\cdots\big)\\&=R_{t+1}+\gamma G_{t+1}\end{aligned}\tag{3.9}$$
  It holds for all $t<T$, even if termination occurs at $t+1$, provided $G_T=0$ (p. 55).
- For a constant reward $+1$ and $\gamma<1$ (p. 55):
$$G_t=\sum_{k=0}^\infty\gamma^k=\frac1{1-\gamma}. \tag{3.10}$$

> **Intuition note.** Discounting makes distant rewards count less, which (for $\gamma<1$ and bounded rewards) keeps infinite sums finite. Equation (3.9) says "return now = reward now + discounted return from the next step", a relation the book calls important for the theory and algorithms of RL (p. 55).

- **Ex. 3.4 Pole-balancing** (p. 56). Keep a pole on a moving cart from falling. Episodic version: +1 for every non-failure step, so the return is the number of steps until failure. Balancing forever would give infinite return. Continuing, discounted version: reward −1 on each failure and 0 otherwise, so the return relates to $-\gamma^{K-1}$, where $K$ is the number of steps before failure (the minus signs are lost in the text layer; no image of this page was supplied). Either way, the return is maximized by balancing as long as possible (p. 56).

### 3.4 Unified Notation for Episodic and Continuing Tasks
- Episodic tasks are mathematically easier: each action affects only finitely many rewards (p. 57).
- Strictly one would write $S_{t,i}$ for step $t$ of episode $i$. In practice episode numbers are dropped, since statements usually concern one episode or all episodes (p. 57).
- **Absorbing state:** treat termination as entering a special state that transitions only to itself and gives reward 0. In the book's diagram, $S_0\to S_1\to S_2\to$ absorbing state, with $R_1=R_2=R_3=+1$ and then $R_4=R_5=\dots=0$. The return is the same whether one sums the first $T=3$ rewards or the infinite sequence, also with discounting (p. 57).
- General return (p. 57), including $T=\infty$ or $\gamma=1$ but not both:
$$G_t\doteq\sum_{k=t+1}^{T}\gamma^{k-t-1}R_k \tag{3.11}$$
  Chapter 10 will introduce a formulation that is both continuing and undiscounted (p. 58).

### 3.5 Policies and Value Functions
- **Value functions** estimate how good it is to be in a state (or to take an action in a state), defined as expected return. They depend on how the agent acts, so they are defined for a **policy** (p. 58).
- A policy is a mapping from states to probabilities of selecting each action. $\pi(a\mid s)$ is the probability that $A_t=a$ if $S_t=s$. RL methods specify how $\pi$ changes with experience (p. 58).
- **State-value function** (p. 58), with $t$ any time step and the terminal state's value always zero:
$$v_\pi(s)\doteq\mathbb E_\pi[G_t\mid S_t=s]=\mathbb E_\pi\Big[\sum_{k=0}^\infty\gamma^kR_{t+k+1}\ \Big|\ S_t=s\Big],\ \text{for all }s\in\mathcal S \tag{3.12}$$
- **Action-value function** (p. 58):
$$q_\pi(s,a)\doteq\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=\mathbb E_\pi\Big[\sum_{k=0}^\infty\gamma^kR_{t+k+1}\ \Big|\ S_t=s,A_t=a\Big] \tag{3.13}$$
- **Estimation from experience** (pp. 58–59). If the agent keeps, for each state, an average of the returns that followed it, the average converges to $v_\pi(s)$ as the number of visits goes to infinity. The same holds for $q_\pi$ with per-action averages. These are **Monte Carlo methods** (Chapter 5). With very many states, separate averages may not be practical, so $v_\pi,q_\pi$ would have to be kept as parameterized functions with fewer parameters than states; accuracy then depends on the approximator (Part II) (p. 59).
- **Bellman equation for $v_\pi$.** For any policy $\pi$ and any state $s$ (p. 59):
$$\begin{aligned}v_\pi(s)&\doteq\mathbb E_\pi[G_t\mid S_t=s]\\&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]&&\text{(by (3.9))}\\&=\sum_a\pi(a\mid s)\sum_{s'}\sum_r p(s',r\mid s,a)\Big[r+\gamma\,\mathbb E_\pi[G_{t+1}\mid S_{t+1}=s']\Big]\\&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\Big[r+\gamma v_\pi(s')\Big],\ \text{for all }s\in\mathcal S\end{aligned}\tag{3.14}$$
  - Actions come from $\mathcal A(s)$, next states from $\mathcal S$ (or $\mathcal S^+$ if episodic), rewards from $\mathcal R$. The last step merges the two sums into one over $(s',r)$ (p. 59).
  - Read it as an expected value over triples $(a,s',r)$ with probability $\pi(a\mid s)p(s',r\mid s,a)$ (p. 59).
  - It says the value of the start state equals the discounted value of the expected next state plus the expected reward along the way (p. 59).
- **Backup diagram:** root state $s$ at top, branching over actions (by $\pi$), then over $(r,s')$ (by $p$). "Backup" operations transfer value information back from successors to a state (pp. 59–60). In backup diagrams, state nodes need not be distinct states (a state may be its own successor) (p. 60).
- $v_\pi$ is the unique solution to its Bellman equation (p. 60).

> **Intuition note.** (3.14) is a consistency check: a state's value must agree with the average of "reward plus discounted value of where I land", weighted by how I act and how the world responds. Because it links each state to its successors, it can be used to compute, approximate or learn values.

- **Ex. 3.5 Gridworld** (p. 60). A 5×5 grid. Actions north/south/east/west move one cell deterministically. Moves off the grid leave the position unchanged and give reward $-1$. Other moves give 0, except out of special states A and B. From A, all actions give +10 and go to A′. From B, all give +5 and go to B′.
  - Equiprobable random policy, $\gamma=0.9$: values come from solving the linear system (3.14). The top row of $v_\pi$ is 3.3, 8.8, 4.4, 5.3, 1.5, so A is 8.8 and B is 5.3. Values are negative near the lower edge (down to −2.0), because the random policy often hits the edge there (p. 60).
  - A is the best state, but its value is *less* than 10 because A′ is likely to run into the edge. B is worth *more* than 5 because B′ has positive value. The expected penalty at B′ is more than compensated by chances of stumbling onto A or B (p. 60).
- **Ex. 3.6 Golf** (p. 61). Reward −1 per stroke until the ball is in the hole; the state is the ball location; the value is minus the number of strokes needed. $v_{\text{putt}}$ is for the policy that always putts: $-1$ on the green, $-2$ for the next contour, and so on; sand traps are $-\infty$ because putting does not get out of them. From the tee it takes six strokes by putting (p. 61).

### 3.6 Optimal Policies and Optimal Value Functions
- Value functions give a **partial ordering** over policies: $\pi\ge\pi'$ iff $v_\pi(s)\ge v_{\pi'}(s)$ for all $s\in\mathcal S$ (p. 62). There is always at least one policy better than or equal to all others. This is an optimal policy. There may be several, denoted $\pi_*$. They share (pp. 62–63)
$$v_*(s)\doteq\max_\pi v_\pi(s) \tag{3.15}$$
$$q_*(s,a)\doteq\max_\pi q_\pi(s,a) \tag{3.16}$$
$$q_*(s,a)=\mathbb E[R_{t+1}+\gamma v_*(S_{t+1})\mid S_t=s,A_t=a] \tag{3.17}$$
- **Ex. 3.7 Golf, optimal values** (p. 63). $q_*(s,\text{driver})$ is the value of driving first and then choosing the better club. The $-1$ contour covers only a small part of the green (a one-shot drive works only when very close). The $-2$ contour reaches much farther, since a drive onto the green is followed by a putt. The $-3$ contour includes the tee: two drives and a putt.
- **Bellman optimality equation for $v_*$.** $v_*$ is a value function, so it satisfies (3.14). But its consistency condition can be written without reference to any policy. The value of a state under an optimal policy equals the expected return of the best action from it (p. 63):
$$\begin{aligned}v_*(s)&=\max_{a\in\mathcal A(s)}q_{\pi_*}(s,a)\\&=\max_a\mathbb E_{\pi_*}[G_t\mid S_t=s,A_t=a]\\&=\max_a\mathbb E_{\pi_*}[R_{t+1}+\gamma G_{t+1}\mid S_t=s,A_t=a]&&\text{(by (3.9))}\\&=\max_a\mathbb E[R_{t+1}+\gamma v_*(S_{t+1})\mid S_t=s,A_t=a]\end{aligned}\tag{3.18}$$
$$=\max_a\sum_{s',r}p(s',r\mid s,a)\big[r+\gamma v_*(s')\big]. \tag{3.19}$$
- For $q_*$ (p. 64):
$$q_*(s,a)=\mathbb E\Big[R_{t+1}+\gamma\max_{a'}q_*(S_{t+1},a')\ \Big|\ S_t=s,A_t=a\Big]=\sum_{s',r}p(s',r\mid s,a)\Big[r+\gamma\max_{a'}q_*(s',a')\Big]. \tag{3.20}$$
- Fig. 3.4 backup diagrams are like those for $v_\pi,q_\pi$, but arcs at the agent's choice points mean "take the maximum" instead of averaging by a policy (p. 64).
- **Solving.** For finite MDPs, (3.19) has a unique solution. It is a system of $n$ nonlinear equations in $n$ unknowns for $n$ states. If $p$ is known, one can in principle solve it for $v_*$ by methods for nonlinear systems; a related system gives $q_*$ (p. 64).
- **From $v_*$ to a policy** (pp. 64–65). In each state, one or more actions attain the max in (3.19). Any policy giving nonzero probability only to those actions is optimal. Equivalently, any policy *greedy* with respect to $v_*$ is optimal. *Greedy* means choosing using only short-term consequences. It is enough here because $v_*$ already accounts for the reward consequences of all future behavior. So a one-step-ahead search yields long-term optimal actions.
- **With $q_*$** the agent needs no one-step search: it picks an action maximizing $q_*(s,a)$. $q_*$ "caches" the one-step searches. Optimal actions can be chosen without knowing successor states or the environment's dynamics, at the cost of representing a function of state–action pairs (p. 65).

> **Intuition note.** The Bellman optimality equation replaces "average over my policy's choices" by "take the best choice". Once you know $v_*$, the long-horizon problem collapses into a one-step comparison.

- **Ex. 3.8 Gridworld solved** (p. 65). The optimal $v_*$ has top row 22.0, 24.4, 22.0, 19.4, 17.5, so $v_*(A)=24.4$ and $v_*(B)=19.4$ (read from the figure). The optimal policy is shown by arrows; cells with several arrows have several optimal actions.
- **Ex. 3.9 Recycling robot** (pp. 65–66). With $h,l$ for high and low and $s,w,re$ for the actions, and $r_s,r_w$ for $r_{\text{search}},r_{\text{wait}}$, (3.19) gives
$$v_*(h)=\max\Big\{\,r_s+\gamma[\alpha v_*(h)+(1-\alpha)v_*(l)],\ \ r_w+\gamma v_*(h)\Big\}$$
$$v_*(l)=\max\Big\{\,\beta r_s-3(1-\beta)+\gamma[(1-\beta)v_*(h)+\beta v_*(l)],\ \ r_w+\gamma v_*(l),\ \ \gamma v_*(h)\Big\}.$$
  For any $r_s,r_w,\alpha,\beta,\gamma$ with $0\le\gamma<1$ and $0\le\alpha,\beta\le1$, exactly one pair $v_*(h),v_*(l)$ satisfies both equations (p. 66). (The first equation is derived in the book from the table: $p(h\mid h,s)=\alpha$, $p(l\mid h,s)=1-\alpha$, $p(h\mid h,w)=1$, $p(l\mid h,w)=0$ (p. 65).)
- **Why explicit solution is rarely useful** (p. 66). It is like exhaustive lookahead and relies on three assumptions rarely true in practice: (1) the dynamics are accurately known, (2) there is enough computation, (3) the states are Markov. In backgammon, (1) and (3) are fine but (2) fails: about $10^{20}$ states would take thousands of years on today's fastest computers. So RL typically settles for approximate solutions.
- Many methods can be seen as approximately solving the Bellman optimality equation (p. 66):
  - heuristic search expands the right side of (3.19) to some depth and uses a heuristic evaluation at the leaves;
  - dynamic programming is related even more closely;
  - many RL methods use actual experienced transitions in place of expected transitions.

### 3.7 Optimality and Approximation
- An agent that learns an optimal policy has done very well, but this rarely happens. Optimality is an ideal that agents can only approximate. Even with a complete model, solving the Bellman optimality equation is usually impossible; large custom computers cannot compute optimal chess moves (p. 67).
- Constraints: computation per time step and memory (p. 67). **Tabular** methods keep one table entry per state (or pair). When there are far more states than entries, functions must be approximated by compact parameterized representations (p. 67).
- Opportunity: many states may be met so rarely that suboptimal actions there barely affect reward. Tesauro's backgammon player plays very well though it may decide badly on boards never met against experts, perhaps on a large fraction of the state set. RL's online nature lets it put more effort on frequently met states. This is one key property that distinguishes RL from other approaches to approximately solving MDPs (pp. 67–68).

### 3.8 Summary (pp. 68–69)
- The task is defined by its interface: actions are the agent's choices, states the basis for choices, rewards the basis for evaluating them. Everything inside the agent is known and controllable; the environment is incompletely controllable and may or may not be known. A policy is a stochastic rule from states to actions (p. 68).
- With well-defined transition probabilities this is an MDP. Much of the theory is restricted to finite MDPs, but the methods and ideas apply more generally (p. 68).
- The undiscounted return suits episodic tasks. The discounted return suits tabular continuing tasks (but see Sections 10.3–4) (p. 68).
- Optimal value functions are unique for a given MDP; there can be many optimal policies. Any policy greedy with respect to the optimal value functions must be optimal (p. 68).
- *Complete knowledge* means the agent has the full four-argument $p$. *Incomplete knowledge* means it does not (p. 69). Even with a perfect model, memory and per-step computation limit use of it, so approximations are needed (p. 69).

### Bibliographical and Historical Remarks (pp. 69–71)
- MDPs come from optimal control. RL adds a focus on approximation and incomplete information for realistically large problems (p. 69).
- The book's $p(s',r\mid s,a)$ is "slightly unusual". The MDP literature more often uses $p(s'\mid s,a)$ and $r(s,a)$. The authors prefer theirs because RL often needs individual sample rewards and because it shows $S_t,R_t$ are jointly determined (p. 70).
- The episodic/continuing terminology differs from the literature's finite-, indefinite- and infinite-horizon tasks. Episodic and continuing are "similar to" indefinite- and infinite-horizon. The authors emphasize the nature of the interaction over the form of the objective (p. 70).
- Mapping states to long-term values is a key part of optimal control theory (developed in the 1950s). Q-learning (Watkins, 1989) made action-value functions ("Q-functions") prominent, though the idea is older. Bellman called (3.19) the "basic functional equation". Its continuous-time, continuous-state counterpart is the Hamilton–Jacobi–Bellman equation, with roots in classical physics (p. 71).

## Toy example (ours, not from the text)
A two-state continuing MDP, $\gamma=0.5$, all transitions deterministic.
- State A: action *stay* → reward 1, next state A. Action *move* → reward 0, next state B.
- State B: only action *back* → reward 2, next state A.

**Policy "always stay".** From A the rewards are 1, 1, 1, …, so by (3.10) $v(A)=1/(1-0.5)=2$.

**Policy "always move".** Bellman (3.14) gives $v(A)=0+0.5\,v(B)$ and $v(B)=2+0.5\,v(A)$. Substituting, $v(A)=0.5(2+0.5v(A))=1+0.25v(A)$, so $v(A)=1/0.75=4/3\approx1.333$. Then $v(B)=2+0.5\cdot1.333=2.667$.

**Random policy** ($\pi(\text{stay}\mid A)=\pi(\text{move}\mid A)=0.5$). $v(A)=0.5[1+0.5v(A)]+0.5[0+0.5v(B)]$ and $v(B)=2+0.5v(A)$. So $v(A)=0.5+0.25v(A)+0.25(2+0.5v(A))=1+0.375v(A)$, giving $v(A)=1/0.625=1.6$ and $v(B)=2.8$. Check: $0.5(1+0.8)+0.5(0+1.4)=0.9+0.7=1.6$ ✓.

**Optimal values.** Guess $v_*(A)=2$ (stay). Then $v_*(B)=2+0.5\cdot2=3$. Check (3.19) at A: $\max\{1+0.5\cdot2,\ 0+0.5\cdot3\}=\max\{2,1.5\}=2$ ✓. The greedy action in A is *stay*, so "always stay" is optimal. The policies are ordered 2 > 1.6 > 1.333 at state A, as the partial ordering of §3.6 requires.

## Concepts
- [[markov-decision-process]] — formal problem: states, actions, rewards, with dynamics $p$ depending only on the previous state and action (p. 48)
- [[state]] — in this unit, what the agent can know that is useful for choosing; it should carry all past information relevant to the future (pp. 49–50)
- [[markov-property]] (new) — a state that includes all aspects of past interaction that make a difference for the future (p. 49)
- [[dynamics-function]] (new) — $p(s',r\mid s,a)$, from which transition probabilities and expected rewards follow (p. 48)
- [[plant]] — engineers' term for what the book calls the environment (p. 48, fn. 1)
- [[agent-environment-boundary]] (new) — limit of the agent's absolute control, not of its knowledge (p. 50)
- [[reward-hypothesis]] (new) — goals as maximizing expected cumulative scalar reward (p. 53)
- [[return]] (new) — $G_t$, a function of future rewards; discounted sum (3.8) (pp. 54–55)
- [[discount-rate]] (new) — $\gamma\in[0,1]$ weighting future rewards by $\gamma^{k-1}$ (p. 55)
- [[episodic-vs-continuing-tasks]] (new) — interaction that breaks into episodes ending in a terminal state, versus one that goes on without limit (p. 54)
- [[policy]] — mapping from states to action probabilities, $\pi(a\mid s)$ (p. 58)
- [[bellman-equation-value-function]] — value functions $v_\pi$, $q_\pi$ are expected returns and satisfy recursive relationships, written out in (3.14) for $v_\pi$ (pp. 58–59)
- [[action-value-function]] (new) — $q_\pi(s,a)$, expected return from taking $a$ in $s$, then following $\pi$ (p. 58)
- [[bellman-optimality-equation]] (new) — (3.19) for $v_*$ and (3.20) for $q_*$; for $v_*$, the value of a state under an optimal policy equals the expected return of its best action (pp. 63–64)
- [[backup-diagram]] (new) — tree diagram of the successor relations behind value updates (pp. 59–60)
- [[greedy-policy]] (new) — chooses by one-step consequences; greedy with respect to $v_*$ is optimal (p. 64)
- [[tabular-methods]] (new) — one table entry per state or pair; otherwise parameterized approximation (p. 67)
- [[model-based-vs-model-free-rl]] — the unit contrasts complete knowledge (full $p$) with incomplete knowledge (p. 69)

## Canonical instances
- [[recycling-robot]] — two-state MDP with explicit table, transition graph and Bellman optimality equations (pp. 52, 65–66)
- [[gridworld]] — 5×5 grid with special states A and B; $v_\pi$ for random policy and $v_*$ (pp. 60, 65)
- [[golf-example]] — negative reward per stroke; $v_{\text{putt}}$ and $q_*(s,\text{driver})$ contours (pp. 61, 63)
- [[pole-balancing]] — episodic (+1 per step) versus discounted continuing (failure penalty) formulation (p. 56)
- [[bioreactor]] and [[pick-and-place-robot]] — vector-valued states and actions (p. 51)
- [[backgammon]] — about $10^{20}$ states; exact solution infeasible; Tesauro's player (pp. 66–68)

## Bridges (candidates)
- [structural-analogy] agent / environment / action ↔ control theory: controller / controlled system (plant) / control signal — the book says it uses the first names in place of the second (p. 48).
- [structural-analogy] Bellman optimality equation (3.19) ↔ control theory: Hamilton–Jacobi–Bellman equation — the text calls the HJB equation the continuous-time, continuous-state counterpart (p. 71).
- [same-math] Bellman equation (3.14) for $v_\pi$ ↔ linear algebra: a linear system of equations in $n$ unknowns — Example 3.5 says $v_\pi$ was computed by solving such a system (p. 60).
- [structural-analogy] greedy action choice from $q_*$ ↔ optimal control: one-step lookahead on a value function — the text frames $q_*$ as caching one-step searches (p. 65).
- [metaphor] discount rate $\gamma$ (myopic to farsighted) ↔ everyday patience about delayed reward (p. 55).

## Questions this raises
- How can the Bellman equations be turned into algorithms that compute or learn $v_\pi$ or $v_*$ (dynamic programming, Monte Carlo, and so on)?
- When the state is not Markov, how can a good state be constructed from observations (Chapter 17)?
- How should the reward be designed so that maximizing it achieves what we really want (Section 17.4)?
- How much does an approximate value function lose compared with $v_*$ when it concentrates on frequently visited states?

## Exercises worth doing
- Ex. 3.5 (p. 55) — how the episodic case changes the sums over next states in (3.3) — difficulty: easy
- Ex. 3.8 (p. 56) — computing returns by working backwards with (3.9) — difficulty: easy
- Ex. 3.14 (p. 60) — numerically checking the Bellman equation on the gridworld centre state — difficulty: easy
- Ex. 3.15 (p. 61) — shifting all rewards by a constant $c$ changes values by a constant; find it from (3.8) — difficulty: medium
- Ex. 3.17 (p. 61) — deriving the Bellman equation for $q_\pi$ — difficulty: medium
- Ex. 3.22 (p. 66) — which policy is optimal for different $\gamma$ — difficulty: easy

## Reading notes
- Printed page = pdf page − 22 (pdf 69 = printed 47). The unit's last pdf page (94, printed 72) is blank.
- The text layer drops minus signs and some symbols, e.g. "reward of 3" for $-3$ and "$\gamma^{K\ 1}$". Where an image was supplied (pp. 48–49, 52, 55, 57–61, 63–66), I checked equations and numbers against it. The pole-balancing, maze and chess reward signs (pp. 53, 56) had no page image; I state them as negative where the surrounding text implies it.
- The Fig. 3.2 and 3.5 values were read from the page images. The text layer for p. 60 is garbled (duplicated figure text).
- The page-82 image shows the figure as "Figure 3.2". The garbled text layer also contains an older "Figure 3.5" caption; I used the image.
- Exercises are listed but not solved. Example 3.9 gives only the $v_*(h)$ derivation from the table; the $v_*(l)$ equation is stated without steps (p. 66).
