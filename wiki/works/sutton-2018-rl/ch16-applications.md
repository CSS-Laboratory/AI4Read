---
id: sutton-2018-rl/ch16-applications
work: sutton-2018-rl
unit: "Chapter 16 — Applications and Case Studies"
pages: 421–458
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Applications and Case Studies (Sutton & Barto, ch. 16)

## L0 — One line
The chapter's case studies (TD-Gammon, Watson, DQN, AlphaGo and others) illustrate the trade-offs of real applications, in particular how domain knowledge is incorporated and how often representation is critical; such applications typically require as much art as science.

## L1 — The gist (≤ 120 words)
The chapter looks at reinforcement learning in real applications, to illustrate the trade-offs and issues that arise. It presents eight case studies: backgammon, Samuel's checkers, Jeopardy! wagering, DRAM memory scheduling, Atari games, Go, web-ad personalization and thermal soaring. The cases illustrate choices about the state representation, the reward, how to generate experience, and how to combine learned value functions with search or other safeguards. Some systems start from handcrafted features (TD-Gammon 1.0). Others use no handcrafted features (DQN, AlphaGo Zero). The authors stress that applications "typically require as much art as science". The cases illustrate some of the trade-offs and issues that arise.

**Prerequisites:** TD(λ) and eligibility traces; Sarsa and Q-learning; off-policy learning (learning about one policy from data produced by another); afterstates (the position just after the agent's own move); minimax search (look-ahead where one side maximizes and the other minimizes); function approximation (linear, tile coding, neural networks); Monte Carlo tree search; policy iteration; MDPs; bandits.

## L2 — Key ideas
- The chapter's purpose is to show trade-offs: how domain knowledge enters the formulation, and how often representation is the critical issue. Applications are "still far from routine" (p. 421).
- **TD-Gammon:** nonlinear TD(λ) with a neural network, trained by self-play, reached near-grandmaster level. The version with almost no backgammon knowledge matched the best earlier programs, and added features and shallow search made it better still (pp. 421–426).
- **Samuel's checkers player** was a precursor. It updated toward minimax (look-ahead) search values but had no rewards and no terminal anchoring, so the authors say it may have lacked an essential part of sound TD learning (pp. 426–429).
- **Watson's Daily-Double wagering:** action values were computed from learned afterstate values and a confidence estimate. Learning used simulated games against opponent models instead of self-play, risk-reduction adjustments were added, and Monte-Carlo trials were used in endgames (pp. 429–432).
- **DRAM controller:** scheduling was posed as an MDP whose pre-defined legal-action sets ensured that exploration could not endanger the hardware. Sarsa with tile coding learned online and beat a fixed learned policy by 8% (pp. 432–436).
- **DQN:** one architecture, one set of hyperparameters and raw pixel input learned many Atari games. Experience replay (updating from randomly sampled stored transitions), a periodically frozen target network (a copy of the weights that supplies the targets) and error clipping were its stabilizing changes (pp. 436–441).
- **AlphaGo and AlphaGo Zero:** MCTS guided by deep networks beat top players. AlphaGo Zero, using self-play only, no human data and a simpler MCTS, then beat AlphaGo. The authors describe it as a form of policy iteration, and Silver et al. say MCTS "may therefore be viewed as" a policy improvement operator (pp. 441–450).
- **Personalized web services:** a contextual-bandit (greedy) policy was compared with an MDP-based life-time-value policy. High-confidence off-policy evaluation (estimating a policy's performance, with probabilistic guarantees, from data collected by other policies) gave the guarantees behind Adobe's 2016 announcement that the new algorithm would be a standard component of its Marketing Cloud (pp. 450–453).
- **Thermal soaring:** reward design and minimal-cue discovery were central. Of the cue sets tried, vertical wind acceleration plus torque worked best for staying in a thermal, and altitude gain peaked at discount rate γ = 0.99 (pp. 453–457).

## L3 — Walkthrough

### Introduction (p. 421)
The chapter gives case studies, some of potential economic significance. Samuel's checkers player is mainly of historical interest. The authors emphasize how domain knowledge is built into the problem formulation and solution, and the representation issues that are often critical. Some algorithms here are more complex than those in the rest of the book. Applications "typically require as much art as science" (p. 421).

### 16.1 TD-Gammon (pp. 421–426)

**The game.** Backgammon is played with 15 white and 15 black pieces on 24 points. Dice give the allowed step sizes. Pieces can hit lone opposing pieces, and two or more pieces on a point protect it. White wins by getting all pieces home and off the board first (pp. 421–422).

**Why TD learning suits it, and why classical search does not.**
- The number of positions is far more than any memory could hold. The game tree has an effective branching factor of about 400, too large for the heuristic search that works in chess and checkers (p. 422).
- The state is fully known at all times. The game ends in a win or loss that can be treated as a final reward to be predicted (p. 422).
- The earlier theory could not be applied usefully. Lookup tables are impossible, and the opponent adds uncertainty and time variation (p. 422).

**Value function.** $\hat v(s,\mathbf w)$ estimates the probability of winning from position $s$. Rewards are zero except on winning (p. 422). The network was a layer of input units, a layer of hidden units (40–80 in Figure 16.1) and an output unit. The real network had two extra output units for "gammon" wins (p. 423).

**Input representation (198 units, p. 423).**
- For each of 24 points and each colour, 4 units code the piece count $n$:
  - $n=0$: all four units are 0.
  - $n=1$: unit 1 is 1 (a "blot", a piece that can be hit).
  - $n\ge 2$: unit 2 is 1 (a "made point", where the opponent cannot land).
  - $n=3$: unit 3 is 1 (a "single spare").
  - $n>3$: unit 4 is $(n-3)/2$ ("multiple spares").
- This gives $4\times 2\times 24 = 192$ units.
- Two more units code pieces on the bar ($n/2$ each). Two code pieces borne off ($n/15$ each). Two binary units say whose turn it is. Total: $192+2+2+2=198$.
- Tesauro's logic: represent the position directly, keep the unit count small, give one unit to each conceptually distinct possibility, and scale all to roughly 0–1 (p. 423).

**Network computation.** Hidden unit $j$ outputs
$$h(j)=\sigma\Big(\sum_i w_{ij}x_i\Big)=\frac{1}{1+e^{-\sum_i w_{ij}x_i}},$$
with $x_i$ the input values. The output lies in $(0,1)$ and can be read as a probability from summed evidence. The output unit applies the same sigmoid to a weighted sum of hidden outputs (p. 424).

**Learning rule.** Semi-gradient TD($\lambda$), with gradients by backpropagation (p. 424):
$$\mathbf w_{t+1}\doteq \mathbf w_t+\alpha\Big[R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)\Big]\mathbf z_t \tag{16.1}$$
$$\mathbf z_t\doteq\gamma\lambda\mathbf z_{t-1}+\nabla\hat v(S_t,\mathbf w_t),\quad \mathbf z_0\doteq\mathbf 0.$$
Here $\gamma=1$ and reward is zero except at a win, so the TD error is usually just $\hat v(S_{t+1},\mathbf w)-\hat v(S_t,\mathbf w)$ (p. 424).

**Experience and move choice.**
- Games came from self-play. For each of the roughly 20 ways to play a dice roll, the network scored the resulting afterstate (the position just after the player's move). The move with the highest estimate was played (p. 424).
- Each game was an episode. The rule (16.1) was applied after every move. Weights started small and random, so early games were poor and often lasted hundreds or thousands of moves. Performance improved rapidly after a few dozen games (p. 424).

**Results.**
- After about 300,000 self-play games, TD-Gammon 0.0 played about as well as the best earlier programs (p. 424).
- The reigning champion, Neurogammon, used an ANN trained on expert moves plus specially crafted features. It won the World Backgammon Olympiad in 1989. TD-Gammon 0.0 was built with essentially zero backgammon knowledge (p. 425).
- TD-Gammon 1.0 added specialized features to self-play TD learning. It was clearly better than all earlier programs and found serious competition only among human experts (p. 425).
- Versions 2.0 and 2.1 (40 and 80 hidden units) added a selective two-ply search. This search considered the opponent's dice rolls and moves and ran the second ply only for highly ranked candidate moves, about four or five on average. Search affected only move choice, not learning (p. 425).
- Versions 3.0 and 3.1 used 160 hidden units and a selective three-ply search. The authors note this combines learned value functions with decision-time search, as in heuristic search and MCTS (p. 425).
- Tesauro and Galperin (1997) used trajectory sampling instead of full-width search. This cut live-play error rate 4x–6x at about 5–10 s per move (p. 425).
- Table 16.1 (p. 425):

| Program | Hidden units | Training games | Opponents | Result |
|---|---|---|---|---|
| 0.0 | 40 | 300,000 | other programs | tied for best |
| 1.0 | 80 | 300,000 | Robertie, Magriel, … | −13 pts / 51 games |
| 2.0 | 40 | 800,000 | various Grandmasters | −7 pts / 38 games |
| 2.1 | 80 | 1,500,000 | Robertie | −1 pt / 40 games |
| 3.0 | 80 | 1,500,000 | Kazaros | +6 pts / 20 games |

- TD-Gammon 3.0 appeared to play close to, or possibly better than, the best humans. A later rollout analysis found a "lopsided advantage" in piece-movement decisions and a "slight edge" in doubling decisions for 3.1 (p. 426).
- Top human players changed how they play some openings after TD-Gammon. Later self-teaching programs (Jellyfish, Snowie, GNUBackgammon) spread its knowledge (p. 426).

*Intuition note.* A network that only has to predict "who wins from here" can be trained by comparing each position's prediction with the next one, with no expert labels. Self-play supplies unlimited data. Handcrafted features and a little lookahead then add strength on top of the same learner.

### 16.2 Samuel's Checkers Player (pp. 426–429)

**Background.** Samuel wrote a checkers program for the IBM 701 in 1952. His first learning program was done in 1955 and shown on television in 1956. He chose games because they are simpler than problems "taken from life", and checkers over chess so he could focus more on learning (p. 426).

**Search.** The program searched ahead from the current position. Terminal positions were scored by a linear "scoring polynomial". Following Shannon's minimax procedure, each position got the "backed-up score" of the best move, with the machine maximizing and the opponent minimizing. Some versions used alpha-beta-like cutoffs (pp. 426–427).

**Rote learning.**
- The program saved each position with its backed-up value. When a stored position later appeared as a search leaf, it effectively deepened the search (p. 427).
- To encourage the shortest path to a win, a position's value was reduced slightly each time it was backed up one ply. The authors call this discounting-like and say Samuel found it essential (p. 427).
- Rote learning gave slow, steady improvement, most effective in openings and endgames. The program became a "better-than-average novice" (p. 427).

**Learning by generalization.**
- This is the same in concept as TD-Gammon's learning. The program played another version of itself and updated after each move (p. 427).
- Each on-move position's value was updated toward the minimax value of a search from the next on-move position (Figure 16.2). The actual algorithm was more complex (p. 427).
- There were no explicit rewards. The weight of the piece-advantage feature was fixed. This feature counts the program's pieces relative to the opponent's, with kings weighted higher. Piece advantage is highly correlated with winning in checkers (p. 427).

**Authors' critique (p. 428).**
- TD learning makes a value function consistent with itself, but it also needs a tie to true values, via rewards, discounting or a fixed terminal value. Samuel's method had none of these.
- As Samuel himself pointed out, his value function could have become consistent merely by giving a constant value to all positions. The large fixed weight lowers the chance of such solutions but does not prohibit them. A constant function could still arise if the modifiable weights cancel the fixed one.
- Samuel saw the program get worse during long self-play. He reset the largest-magnitude weight to zero. He thought this jarred the program out of local optima. The authors suggest it may instead have removed evaluation functions that were consistent but unrelated to winning.

**Outcome.** The generalization version approached "better-than-average" play. Amateurs called it "tricky but beatable". It had a good middle game and weak opening and endgame play. It could also search for useful features. The 1967 version added alpha-beta pruning, "book learning" from expert games, and signature tables in place of linear approximation. It played much better but not at master level (pp. 428–429).

*Intuition note.* Samuel's idea of pulling a position's value toward the values of positions that follow is the heart of TD learning. But consistency alone is not enough: without a reward or terminal anchor, a value function can be perfectly consistent and useless.

### 16.3 Watson's Daily-Double Wagering (pp. 429–432)

**Setting.** Jeopardy! has three contestants and 30 clue squares in six categories. A correct response adds the square's value, and a wrong or missing response subtracts it. On a Daily-Double (DD) square the contestant bets before seeing the clue. The bet must exceed $5 and not exceed the current score. Winning often depends on DD strategy. Tesauro et al. adapted TD-Gammon for Watson's DD wagering, the component that owes most to RL (pp. 429–430).

**Method (p. 430).**
- Watson compared action values $\hat q(s,\text{bet})$, estimating win probability, over each round-dollar legal bet. It took the maximum, except for risk adjustments.
- Two learned ingredients:
  - A state-value function $\hat v(\cdot,\mathbf w)$ gave afterstate win probabilities. It was learned like TD-Gammon: nonlinear TD($\lambda$), a multilayer ANN and backpropagated TD errors. The input features were designed for Jeopardy!: the three scores, DDs remaining, total value of remaining clues, and so on.
  - "In-category DD confidence" $p_{DD}$ estimated the chance of answering the unseen clue correctly. It was conditioned on the numbers of right and wrong responses so far in the category, estimated from many thousands of historical categories.
- The action value, with $S_W$ Watson's score:
$$\hat q(s,\text{bet})=p_{DD}\times\hat v(S_W+\text{bet},\ldots)+(1-p_{DD})\times\hat v(S_W-\text{bet},\ldots) \tag{16.2}$$
- The authors link this to Exercise 3.19: an action value is the expected next-state value given the action. Here it is the expected afterstate value (p. 430).

**Risk.** Maximizing $\hat q$ incurred "a frightening amount of risk" (p. 430). So Tesauro et al. subtracted a small fraction of the standard deviation of the correct/incorrect afterstate evaluations. They also banned bets that would push the wrong-answer afterstate value below a limit. These measures slightly reduced expected win probability but cut downside risk, especially in extreme cases where a risk-neutral Watson would bet most or all of its bankroll (p. 430).

**Why not self-play (p. 431).**
- Watson differs greatly from human contestants, so self-play would visit atypical states.
- Jeopardy! has imperfect information: contestants do not know opponents' confidence. The authors compare self-play to playing poker against someone holding your own cards.
- Instead, much effort went into opponent models. These were stochastic process models of play events, not of language. They were built from a fan-made archive covering nearly 300,000 clues.
- Three models were built: Average Contestant (all data), Champion (games with the 100 best players) and Grand Champion (the 10 best). $\hat v$ was learned over millions of simulated games against these models (pp. 430–431).

**Results (p. 431).** In simulation, Watson's win rate was 61% with a baseline heuristic wagering strategy. It was 64% with learned values and a default confidence, and 67% with live in-category confidence. Tesauro et al. regarded this as a significant improvement, given that DD wagering was needed only about 1.5–2 times per game.

**Time and Monte Carlo.** The ANN allowed bets within live time limits. Later, faster simulation made it possible near game end to estimate bets by averaging Monte-Carlo trials simulated to the game's end. This significantly improved endgame bets. Using such trials for all decisions was impossible given game complexity and time limits (p. 431).

*Intuition note.* Watson's bet is a one-step lookahead. It weights the learned value of "I was right" and "I was wrong" by how likely each is. The extra safeguards show that maximizing expected win probability alone can still expose a system to large losses.

### 16.4 Optimizing Memory Control (pp. 432–436)

**Problem.** A DRAM memory controller must schedule read/write requests under many timing and resource constraints, with multiple cores sharing DRAM. Conventional controllers did not use past scheduling experience or account for long-term consequences. İpek et al. designed an RL controller at the level of on-chip hardware, evaluated in simulation (p. 432).

**DRAM facts needed (pp. 432–433).**
- Cells are arranged in rows and columns and must be refreshed.
- Access involves four commands: activate (open a row into the row buffer), read/write (column commands) and precharge (write back the buffer so another row can be opened).
- Read/write commands to an open row are faster than switching rows ("row locality").
- A transaction queue holds pending requests.
- FR-FCFS gives column commands priority over row commands and breaks ties by oldest. It had the best average latency among earlier policies under common conditions (Rixner, 2004).

**MDP formulation (p. 433).**
- States are the contents of the transaction queue.
- Actions are precharge, activate, read, write and NoOp.
- Reward is 1 for read or write and 0 otherwise.
- Transitions are stochastic because workloads of the cores are outside the scheduler's control.

**Constrained action sets (p. 434).**
- The available actions depend on the state, $A_t\in A(S_t)$. The sets $A(S_t)$ were effectively pre-defined to forbid commands that would violate timing or resource constraints.
- This explains NoOp, which is chosen when it is the only legal action. It also explains the sparse reward. Only read and write send data on the bus, so only they add throughput. Precharge and activate earn nothing now but make later rewarded actions possible.

**Algorithm and features (p. 434).**
- The agent used Sarsa with linear function approximation by tile coding with hashing: 32 tilings, each storing 256 action values as 16-bit fixed-point numbers. Exploration was ε-greedy with ε = 0.05.
- Six integer features described the queue, for example counts of read requests and of write requests, and counts of requests waiting for their row to be opened. Others related to cache interaction and were omitted in the text. The authors chose them from a longer list by simulation with stepwise feature selection.
- The tile-coding inputs (queue contents) differ from the features that define $A(S_t)$ (timing and resource constraints). So action constraints stop exploration from endangering the physical system, and learning stays within a "safe" region of the larger hardware state space.

**Hardware (pp. 434–435).** Two five-stage pipelines compute and compare two action values per processor cycle and update one. The simulated chip was 4 GHz with 4 cores, giving 10 processor cycles per DRAM cycle, so up to 12 actions could be evaluated per DRAM cycle. Legal commands rarely exceeded this, and performance loss was negligible if time did not allow evaluating all.

**Results.**
- Compared with FR-FCFS, an in-order controller and an unrealizable "Optimistic" controller that ignores all timing and resource constraints (p. 435).
- On nine memory-intensive workloads, the RL controller improved on FR-FCFS by 7% to 33% (average 19%). It closed 27% of the gap to Optimistic (p. 435, Figure 16.4).
- A fixed policy trained on all nine benchmarks was 8% worse on average than online learning (p. 436).
- The controller was never built in hardware because of fabrication cost. The authors report that the simulations argue it could reach performance that otherwise needs more complex memory systems, and relieve designers of hand-designing scheduling policies. Mukundan and Martínez (2012) extended it with more actions, other criteria (including energy) and rewards derived by genetic algorithms, and surpassed the earlier results (p. 436).

*Intuition note.* Here safety lives in the action sets, not in the reward. Learning can try anything legal, and "legal" is defined by the hardware rules.

### 16.5 Human-level Video Game Play (pp. 436–441)

**Motivation.** Representing value functions is a central difficulty. Most successful applications used features handcrafted from human knowledge. TD-Gammon 0.0 (raw-like input) matched earlier programs, while added features gave 1.0 (pp. 436–437). Mnih et al. (DeepMind) built the **deep Q-network (DQN)**: Q-learning with a deep convolutional ANN, to show an agent can do well on many problems without problem-specific features (p. 437).

**Setup.**
- 49 Atari 2600 games were played through an emulator (the Arcade Learning Environment). Weights were reset to random before each game, so DQN learned a different policy per game. Raw input, architecture and all parameter values were the same for every game (p. 437).
- Like TD-Gammon, DQN uses a multilayer ANN with semi-gradient TD and backpropagation. It uses Q-learning, not TD($\lambda$), and action values, not afterstate values. Afterstates were not readily available. Single-step emulator simulations or a learned model could have supplied next states but would be more complex and slower (pp. 437–438). Q-learning is model-free and off-policy, which experience replay requires (p. 438).

**Evaluation protocol (p. 438).**
- DQN trained for 50 million frames (about 38 days of experience) per game.
- Its score was averaged over 30 sessions of up to 5 minutes from random initial states.
- A professional human tester (sound off) got 2 hours of practice, then played about 20 episodes of up to 5 minutes.
- DQN beat the best earlier learning system on all but 6 games and the human on 22 games. Counting at least 75% of the human score as comparable, DQN reached or exceeded human level on 29 of 46 games.

**Input and architecture (pp. 438–439).**
- Each frame is 210×160 pixels, 128 colours, 60 Hz. It was preprocessed to an 84×84 array of luminance values. The four most recent frames were stacked, giving input shape 84×84×4, which helps with partial observability and makes many games more Markovian. This preprocessing was identical across games.
- Layer shapes: conv → 32 maps of 20×20; conv → 64 maps of 9×9; conv → 64 maps of 7×7 (3,136 units, rectifier $\max(0,x)$); fully connected 512 units; output 18 units, one per possible action. Games had 4 to 18 valid actions, so not all outputs were used in every game (p. 439).

**Reward and exploration (p. 439).** Reward was +1 if the score rose, −1 if it fell and 0 otherwise. This let one step size work for all games. Exploration was ε-greedy, with ε decreasing linearly over the first million frames and then staying low. Other parameters were set by informal search on a few games and then held fixed.

**Update (semi-gradient Q-learning, before Mnih et al.'s changes) (p. 439):**
$$\mathbf w_{t+1}=\mathbf w_t+\alpha\Big[R_{t+1}+\gamma\max_a\hat q(S_{t+1},a,\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t)\Big]\nabla\hat q(S_t,A_t,\mathbf w_t) \tag{16.3}$$
Think of 18 separate networks sharing early layers. Backpropagation is applied only to the one for $A_t$ (p. 439).

**Stabilizing changes (p. 440).**
- Mini-batch updates (32 images), and RMSProp, which adapts each weight's step size using a running average of recent gradient magnitudes.
- Three modifications of Q-learning:
  1. **Experience replay:** store $(S_t,A_t,R_{t+1},S_{t+1})$ in a replay memory. Perform each update on a mini-batch sampled uniformly at random, rather than moving along the trajectory. This is possible because Q-learning is off-policy. The authors list its advantages: each experience is reused for many updates, successive updates are decorrelated (lower variance), and dependence of experiences on the current weights is removed (one instability source).
  2. **Duplicate target network:** every $C$ updates, copy the current weights into a second network held fixed for the next $C$ updates. Its output $\tilde q$ supplies the targets. This addresses the dependence of the target on the weights being updated, which can cause oscillation or divergence (Chapter 11):
$$\mathbf w_{t+1}=\mathbf w_t+\alpha\Big[R_{t+1}+\gamma\max_a\tilde q(S_{t+1},a,\mathbf w_t)-\hat q(S_t,A_t,\mathbf w_t)\Big]\nabla\hat q(S_t,A_t,\mathbf w_t)$$
  3. **Error clipping:** the bracketed error was clipped to $[-1,1]$.

**Ablations and limits (p. 441).** On 5 games, replay and the duplicate target network each alone significantly improved performance, and together very dramatically. The deep convolutional version beat a single-linear-layer version strikingly on all 5 test games. The authors (citing Mnih et al.) state the limits:
- Learning was separate for each game, so no single agent excelled at all.
- All the games use video, which suits a convolutional network.
- Some games (e.g., Montezuma's Revenge, where DQN did about as well as a random player) need deeper planning than DQN does.

*Intuition note.* DQN keeps the learning rule simple and spends its effort on making it stable: reuse shuffled past data, and chase a target that stays still for a while. Features are learned by the network, not designed by hand.

### 16.6 Mastering the Game of Go (pp. 441–450)

**Background (pp. 441–443).**
- AlphaGo (Silver et al., 2016) combined deep ANNs, supervised learning, MCTS and RL. It beat European champion Fan Hui 5–0 (the first win over a professional without handicap in full games). A similar version beat 18-time world champion Lee Sedol 4 of 5 games.
- Go rules: stones are placed on a 19×19 grid. A group is captured when it has no adjacent empty point (Figure 16.5).
- Go has about 250 legal moves per position versus about 35 for chess, and games of about 150 moves versus about 80. But the authors say size is not the main difficulty. Experts agree the major stumbling block is defining an adequate position evaluation function. Müller (2002): "No simple yet reasonable evaluation function will ever be found for Go." MCTS was a major step, but master level stayed elusive (p. 443).
- **MCTS recap (Section 8.11).** It is decision-time planning with no global evaluation function. Each iteration traverses the tree using edge statistics and expands a leaf. It then runs a rollout (a simulation to a terminal state using a rollout policy) and backs up the return into the traversed edges. After many iterations, the action is chosen from root statistics. The next move restarts with the new current state as root (p. 443).

#### 16.6.1 AlphaGo (pp. 444–447)

**APV-MCTS ("asynchronous policy and value MCTS").**
- Tree expansion chooses edges by probabilities from a 13-layer convolutional **SL policy network**, trained by supervised learning on nearly 30 million human expert moves.
- A newly added node $s$ is evaluated by mixing a learned value $v_\theta$ (from the **value network**) with the rollout return $G$:
$$v(s)=(1-\eta)\,v_\theta(s)+\eta\,G \tag{16.4}$$
- Rollouts used a fast linear **rollout policy**, also supervised-trained. The most-visited root edge is the move played (p. 444).

**Training pipeline (Figure 16.6; all networks trained before live play, weights fixed during play, p. 445).**
- The **RL policy network** has the SL network's structure and was initialized from its weights. It was improved by policy-gradient RL in games against randomly selected earlier versions of itself, to avoid overfitting to the current policy. Reward was +1 for a win, −1 for a loss and 0 otherwise, without MCTS. It trained on a million games in a day on 50 processors. It won more than 80% against the SL policy and 85% against a Go program using MCTS with 100,000 simulations per move (pp. 445–446).
- The **value network** has the same structure but a single output unit and an extra input feature for the colour to play. It was trained by Monte Carlo policy evaluation on self-play games played by the RL policy. The data set had 30 million positions, each from a unique game, to avoid overfitting from correlated positions. Training used 50 million mini-batches of 32 and took a week on 50 GPUs (p. 446).
- The authors note that TD-Gammon-style self-play TD($\lambda$) might have approximated the value function, but the team took an approach that held more promise for such a complex game (p. 444).

**Networks' details (p. 445).** The SL and RL policy networks have 13 convolutional layers and a final soft-max over the 19×19 points. Their input is a 19×19×48 image stack of binary or integer features, including stone occupancy and rule-based features. Training the SL network took about 3 weeks on 50 processors. It reached 57% accuracy; the best accuracy of other groups at the time of publication was 44.4%.

**Rollout policy (p. 446).** It was trained from 8 million human moves. Deep networks were too slow for the very many rollouts needed. The rollout policy managed about 1,000 simulated games per second per thread.

**SL versus RL policy (p. 446).** AlphaGo played better against humans when expansion used the SL policy rather than the RL policy. The team conjectured that the RL policy is tuned to respond to optimal moves instead of the broader set of human moves. For the value function the situation was reversed. The value function derived from the RL policy worked better.

**Ablation on η (pp. 446–447).** With $\eta=0$ (value network only) AlphaGo played better than rollout-only ($\eta=1$) AlphaGo and better than the strongest of the other Go programs existing at the time. Best play came at $\eta=0.5$. The two evaluations complement each other: the value network evaluates the strong but too-slow RL policy, and the fast, weaker rollouts add precision for the actual positions.

*Intuition note.* AlphaGo cannot afford a perfect evaluation, so it averages two imperfect ones. One is slow to build but cheap to query (the value network), and the other is cheap and noisy (rollouts). Mixing them beat either alone.

#### 16.6.2 AlphaGo Zero (pp. 447–450)

**Differences from AlphaGo (p. 447).**
- No human data or guidance beyond the rules, and raw board input.
- Learning only by self-play RL, implementing a form of policy iteration (policy evaluation interleaved with improvement).
- MCTS is used during learning, not only in live play.
- One network instead of several, and no rollouts (hence no rollout policy). Each MCTS iteration ends at a leaf of the current tree.

**Network output and the use of MCTS (p. 447).**
- The network $f_\theta$ outputs a scalar $v$ (estimated win probability for the current player) and a vector $\mathbf p$ of move probabilities (one per stone placement, plus pass/resign).
- Moves are not sampled from $\mathbf p$. Instead $\mathbf p$ and $v$ guide an MCTS run that returns improved move probabilities $\pi_i$, from which self-play moves are drawn. Silver et al.: "MCTS may therefore be viewed as a powerful *policy improvement* operator."

**Network and training details (pp. 448–449).**
- Input is 19×19×17 binary planes: 8 for the current player's stones (current plus seven past positions), 8 for the opponent's, and 1 for colour. The history and colour are needed because the board position alone is not a Markov state of Go (repetition is not allowed, and compensation points exist).
- The network is "two-headed". The shared trunk has 41 convolutional layers with batch normalization and residual skip connections. One head gives 362 outputs ($19^2+1$ moves) and the other gives the single value $v$. Totals are 43 and 44 layers respectively.
- Training started from random weights, with SGD on batches sampled uniformly from the most recent 500,000 self-play games. Noise was added to $\mathbf p$ to encourage exploration. Every 1,000 training steps the latest policy played 400 games (MCTS with 1,600 iterations per move) against the current best. If it won (by a margin chosen to reduce noise), it became the best policy for self-play.
- Weights are updated so that $\mathbf p$ moves toward the MCTS policy and $v$ toward the probability that the current best policy wins from that position (Figure 16.7).

**Results (pp. 449–450).**
- 4.9 million self-play games took about 3 days. Each move used 1,600 MCTS iterations (about 0.4 s). There were 700,000 batches of 2,048 positions.
- Elo ratings (a rating system whose differences predict game outcomes): AlphaGo Zero 4,308; the Fan Hui version of AlphaGo 3,144; the Lee Sedol version 3,739. In 100 games against the exact Lee Sedol version under match conditions, AlphaGo Zero won all 100 (p. 449).
- A supervised-learning player with the same architecture, trained on nearly 30 million positions from 160,000 games, initially played better than AlphaGo Zero and predicted human moves better. It was weaker after AlphaGo Zero had trained for a day. This suggested AlphaGo Zero found a strategy different from human play, including novel variations of classical move sequences (p. 449).
- A larger network trained over 29 million games (about 40 days) reached Elo 5,185. AlphaGo Master (Elo 4,858, which used human data and features and had beaten top professionals 60–0 online) lost 89–11 over 100 games (p. 450).
- The authors conclude that superhuman play can be reached by pure RL with a simple MCTS and deep ANNs, with minimal domain knowledge. AlphaZero (Silver et al., 2017b) is a general RL algorithm that improves on the best programs in Go, chess and shogi (p. 450).

### 16.7 Personalized Web Services (pp. 450–453)

**Formulations (pp. 450–451).**
- A/B testing is non-associative (like a two-armed bandit) and does not personalize. Adding user and content features gives a **contextual bandit** (associative RL). Li et al. (2010) used one to choose the featured news story on Yahoo! Front Page Today, maximizing click-through rate (CTR). It improved on a standard bandit algorithm by 12.5%.
- Theocharous et al. (2015) argued that an MDP with the goal of total clicks over repeated visits can do better. Contextual-bandit policies are greedy. They treat each visit as if made by a new visitor drawn from the population, ignoring that users return.
- Example: a greedy car ad offers a discount immediately. A longer-term policy might first mention financing, then the service department, then the discount on a later visit, moving the user "down a sales funnel" (p. 451).

**Off-policy evaluation (p. 451).** Deploying a new policy is risky, so the team had to estimate a policy's performance from data collected by other policies, with high confidence. The text focuses on the algorithms and results.

**Data (pp. 451–452).** Bank-website data had reward 1 for a click and 0 otherwise. One data set had about 200,000 interactions with 7 offers (random offering). Another had 4,000,000 interactions with 12 offers. Customer features included time since last visit, number of visits, last click time, location, interests and demographics. Rewards are sparse and returns have high variance.

**The two algorithms (p. 452).**
- *Greedy optimization:* a random forest (RF) estimates click probability from user features by supervised learning. The policy is ε-greedy: with probability $1-\varepsilon$ it picks the offer with the highest predicted click probability, otherwise a uniformly random other offer.
- *LTV optimization:* fitted Q iteration (FQI), a batch-mode RL algorithm (the whole data set is available from the start) using the same RF as regressor. FQI convergence is not monotonic, so the best FQI policy was tracked by off-policy evaluation on a validation set. FQI started from the RF mapping of the greedy approach, and the final policy was ε-greedy on the best FQI policy.

**Metrics (p. 452):**
$$\text{CTR}=\frac{\text{Total \# of Clicks}}{\text{Total \# of Visits}},\qquad \text{LTV}=\frac{\text{Total \# of Clicks}}{\text{Total \# of Visitors}}.$$
In Figure 16.8, with 4 users making 5, 3, 5 and 4 visits (17 visits) and 6 clicks in total, CTR $=6/17\approx0.35$ and LTV $=6/4=1.5$ (p. 453). LTV exceeds CTR to the extent that individual users revisit, so it indicates success at encouraging extended interactions.

**Results (p. 453).** Greedy optimization did best on CTR and LTV optimization did best on the LTV metric. The high-confidence off-policy method gave probabilistic guarantees that LTV optimization would, with high probability, produce policies better than currently deployed ones. Adobe announced in 2016 that the LTV algorithm would be a standard component of the Adobe Marketing Cloud.

### 16.8 Thermal Soaring (pp. 453–457)

**Goal and model (pp. 453–454).** Reddy et al. (2016) used RL to study soaring in the strong turbulence that accompanies updrafts. The goal was mainly insight into the cues birds use, and also technology for autonomous gliders. The problem was a continuing, discounted MDP. Air flow in a 1 km box came from physics-based partial differential equations, and small random perturbations produced thermals and turbulence. Glider flight used aerodynamic equations (Figure 16.9).

**Actions (p. 454).** Three choices (increase, decrease, keep) each for bank angle (changes of 5°) and angle of attack (changes of 2.5°) give $3^2$ actions. Bank angle was bounded to $[-15^\circ,+15^\circ]$.

**State (pp. 454–455).** To find the minimal useful cues, they used state aggregation over four dimensions: local vertical wind speed, vertical wind acceleration, torque (the difference between vertical wind speeds at the wing tips) and local temperature. Each was split into three bins (positive high, negative high, small). Only two dimensions proved critical.

**Reward (p. 455).** A final-altitude-gain reward, with a large penalty for touching the ground, did not work for episodes of realistic length, and eligibility traces did not help. Learning was best with a per-step reward that linearly combined the vertical wind velocity and vertical wind acceleration seen on the previous step.

**Learning (p. 455).**
- One-step Sarsa with soft-max action selection (13.2) over preferences
$$h(s,a,\theta)=\frac{\hat q(s,a,\theta)-\min_b\hat q(s,b,\theta)}{\tau\big(\max_b\hat q(s,b,\theta)-\min_b\hat q(s,b,\theta)\big)}$$
- Action values are normalized to $[0,1]$ and divided by temperature $\tau$. The maximum-valued action gets preference $1/\tau$ and the minimum gets 0. As $\tau\to0$ the policy approaches greedy.
- $\tau$ went from 2.0 to 0.2 during learning, step size was 0.1 and discount 0.98.
- Episodes were 2.5 simulated minutes with a 1-second time step. Learning effectively converged after a few hundred episodes. Before learning, the glider descended. After learning, it gained altitude by spiralling in the rising air (Figure 16.10). Performance varied widely across air-flow periods, but ground contacts fell to nearly zero.

**Findings (pp. 455–457).**
- Vertical wind acceleration plus torque worked best. The authors conjectured these give gradient information in two directions, allowing a choice between turning (bank) and holding course. Vertical wind velocity indicates thermal strength but does not help staying in the flow. Temperature was of little help.
- Angle of attack control did not help in staying within one thermal. It is useful for travelling between thermals.
- Policies shared features across turbulence levels: bank sharply toward the wing with higher lift when sensing negative wind acceleration, and do nothing for large positive acceleration with no torque. In strong turbulence the policies preferred small bank angles, and in weak turbulence they banked sharply. The authors suggest a controller could adapt by detecting when vertical wind acceleration crosses a threshold.
- Altitude gain rose with $\gamma$ and peaked at $\gamma=0.99$, which suggests soaring needs long-term consequences to be taken into account (p. 457).
- Hypotheses can be tested on real gliders and compared with bird behaviour (p. 457). A footnote reports the work was later applied to real gliders (Reddy et al., Nature, 2018).

*Intuition note.* Restricting the agent's senses and actions and seeing which cues survive is itself a scientific tool. In the learning experiments, vertical wind acceleration and torque worked best, and the authors conjectured that they do so because they carry information about the gradient of vertical wind velocity.

## Toy example (ours, not from the text)
Aim: show how a learned value function plus an uncertain outcome turns into an action choice (the logic of Watson's (16.2)), and why a safeguard may change it. All numbers are invented.

Suppose Watson has $S_W=1000$ and $p_{DD}=0.6$. A hypothetical $\hat v$ gives afterstate win probabilities:
- Bet 200: $\hat v(1200)=0.70$, $\hat v(800)=0.50$.
- Bet 1000: $\hat v(2000)=0.95$, $\hat v(0)=0.20$.

Using (16.2):
- $\hat q(200)=0.6\times0.70+0.4\times0.50=0.42+0.20=0.62$.
- $\hat q(1000)=0.6\times0.95+0.4\times0.20=0.57+0.08=0.65$.

A risk-neutral choice is the 1000 bet (0.65 > 0.62). Now add a safeguard like the one described in the text: forbid bets whose wrong-answer afterstate value is below a limit. Take 0.30 as our invented limit. The bet 1000 has wrong-answer value 0.20 < 0.30, so it is banned. The bet 200 has 0.50 ≥ 0.30, so it is allowed. The chosen bet becomes 200, at a cost of $0.65-0.62=0.03$ in expected win probability. This matches the text's description: a slightly lower expectation and much lower extreme risk (p. 430).

The mixing in (16.4) is equally simple. With $\eta=0.5$, $v_\theta(s)=0.62$ and rollout return $G=1$: $v(s)=0.5\times0.62+0.5\times1=0.81$.

## Concepts
- [[temporal-difference-learning]] — update value estimates toward the next prediction plus reward; used by TD-Gammon, Samuel, Watson, DQN (p. 424)
- [[afterstate]] (new) — the position right after the agent's move, before the opponent or chance acts; valued instead of states in TD-Gammon and Watson (p. 424)
- [[self-play]] (new) — an agent learns by playing against itself or a copy; the source of unlimited games in TD-Gammon, Samuel, AlphaGo Zero (p. 424)
- [[exploration-vs-exploitation]] — here: ε-greedy (DRAM, DQN), soft-max with falling temperature (soaring), added output noise (AlphaGo Zero) (pp. 434, 439, 449, 455)
- [[policy]] — rule for choosing actions; here also the move probabilities produced by MCTS in AlphaGo Zero (p. 447)
- [[markov-decision-process]] — formulation used for DRAM scheduling, ad recommendation and soaring (pp. 433, 451, 453)
- [[model-based-vs-model-free-rl]] — DQN chose model-free Q-learning over learned models or emulator look-ahead for simplicity and speed (pp. 437–438)
- [[experience-replay]] (new) — store transitions and update from random samples; allowed by off-policy learning (p. 440)
- [[target-network]] (new) — frozen weight copy giving Q-learning targets for $C$ updates to improve stability (p. 440)
- [[monte-carlo-tree-search]] (new) — decision-time planning that grows a search tree with rollouts and backed-up returns (p. 443)
- [[policy-improvement-operator]] (new) — in AlphaGo Zero, MCTS returns a better policy than the network's raw output (p. 447)
- [[contextual-bandit]] (new) — bandit with context features; greedy because it ignores long-term effects (p. 450)
- [[off-policy-evaluation]] (new) — estimate a policy's performance from data generated by other policies (p. 451)
- [[state-aggregation]] (new) — group states and share one value per group; used in soaring (p. 454)

## Canonical instances
- [[td-gammon]] — nonlinear TD(λ) + ANN + self-play reaches near-grandmaster play; shows the role of representation and search (p. 421)
- [[samuel-checkers]] — early TD-like learning with minimax backups; no rewards or terminal anchoring (p. 426)
- [[watson-daily-double]] — action values from learned afterstate values and confidence, with risk control (p. 430)
- [[dram-memory-controller]] — RL scheduler with hardware-safe constrained action sets (p. 432)
- [[dqn-atari]] — one architecture and parameter set across Atari games using raw frames (p. 437)
- [[alphago]] — MCTS guided by SL policy, RL-trained value network and rollouts (p. 444)
- [[alphago-zero]] — pure self-play policy iteration with MCTS as policy improvement (p. 447)
- [[adobe-ltv-ad-recommendation]] — greedy vs long-term policies with high-confidence off-policy evaluation (p. 450)
- [[thermal-soaring-glider]] — RL to find minimal sensory cues for soaring in turbulence (p. 453)

## Bridges (candidates)
- [structural-analogy] MCTS re-run from the new current state at every step, applying only the first action ↔ control-theory: receding-horizon / model predictive control — plan ahead, act once, re-plan (p. 443).
- [structural-analogy] Stacking the four latest frames to handle states not fully observable from one image ↔ control-theory: observability and state estimation — use history to recover hidden state (p. 438).
- [structural-analogy] Pre-defined legal-action sets $A(S_t)$ that keep exploration within hardware limits ↔ control-theory: constrained control / safe exploration (p. 434).
- [metaphor] Frozen target network updated every $C$ steps ↔ control-theory: time-scale separation between a slow reference and a fast loop (p. 440).

## Questions this raises
- Samuel's value function could become consistent but useless. Which anchors (rewards, terminal values, discounting) are enough in general, and how can one detect drift away from winning during training?
- DQN is described as learning separately for each game. What would be needed for one agent to learn many tasks together?
- Why does mixing two imperfect evaluations ($\eta=0.5$ in AlphaGo) work better than relying on either one? Does the best mix depend on game or time budget?
- LTV policies are claimed to beat greedy ones on the LTV metric only. How should one choose a metric when the true goal is eventual sales, which the text does not measure?

## Reading notes
- Page offset: printed = pdf − 22 (e.g., pdf 443 = printed 421). The last pdf page (480, printed 458) is blank.
- The text layer for p. 423 overlaps text from an earlier draft (an equation numbered 15.1, a reference to Figure 15.2). The image shows the final text; the equation is numbered (16.1) on p. 424. The text layers of pp. 445 and 454 also contain figure or paper-excerpt text mixed in. I used the page images.
- Source inconsistencies: Table 16.1 lists 80 hidden units for TD-Gammon 3.0, while the text on p. 425 says versions 3.0 and 3.1 used 160. The DQN section says 49 Atari games (pp. 437–438) but then reports results on "46 games" (p. 438). I kept the numbers as printed and did not resolve them.
- The Q-learning target-network update on p. 440 is printed with $\tilde q(S_{t+1},a,\mathbf w_t)$. I copied it as printed.
- Chapter 16 prints no exercises. The AlphaGo Zero loss is not written out as an equation in this chapter, so none is given here.
- Several details are only referred to other sources (e.g., high-confidence off-policy evaluation; Watson's full strategy). I did not add them.
