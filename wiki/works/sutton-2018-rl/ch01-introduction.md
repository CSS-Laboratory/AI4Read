---
id: sutton-2018-rl/ch01-introduction
work: sutton-2018-rl
unit: "Chapter 1 — Introduction"
pages: 1-22
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
# Introduction (Sutton & Barto, Chapter 1)

## L0 — One line
Reinforcement learning is learning what to do so as to maximize a numerical reward signal; its two most important distinguishing features are trial-and-error search and delayed reward, and the chapter explains it with the tic-tac-toe example and a history of three threads.

## L1 — The gist (≤ 120 words)
The chapter asks what is distinctive about learning from interaction with an environment to reach a goal. Its answer: the learner is not told which action is correct; it gets a reward number and must discover good actions by trial-and-error search, and rewards may come late. Four elements make up a reinforcement learning system: policy, reward signal, value function and, optionally, a model. A tic-tac-toe player shows how learned values (updated by temporal differences) use information that evolutionary methods ignore. The history joins trial-and-error learning from psychology, optimal control with dynamic programming, and temporal-difference learning. The chapter formalizes the problem as optimal control of systems that are only partly known.

**Prerequisites:** basic probability (expected value); the idea of a state of a system; the notion of a controller acting on a system.

## L2 — Key ideas
- Reinforcement learning (RL) maps situations to actions to maximize a numerical reward. Its two most important distinguishing features are trial-and-error search and delayed reward (p. 1).
- RL is formalized as optimal control of incompletely known Markov decision processes (MDPs: models in which an agent senses states, takes actions and has goals). The authors consider it a third paradigm beside supervised learning (learning from labeled examples) and unsupervised learning (finding structure in unlabeled data) (p. 2).
- Exploration versus exploitation is a challenge that arises in RL and not in other kinds of learning (it does not arise, at least in the purest forms of supervised and unsupervised learning). It has been intensively studied for many decades and remains unresolved (p. 3).
- Four elements: a policy (a mapping from perceived states to actions), a reward signal, a value function (the reward an agent can expect to accumulate from a state onward), and optionally a model of the environment. Rewards are in a sense primary; values are predictions of reward, and a method for efficiently estimating them is the most important component of almost all RL algorithms the book considers (pp. 6–7).
- Methods that never estimate value functions (evolutionary methods, which keep the policies that earn most reward and vary them) can be effective under some conditions, but they ignore much of the useful structure available during play. The authors do not treat them as especially well suited to RL (pp. 7–8, 11).
- Tic-tac-toe illustrates a value table updated by a temporal-difference rule (an update based on the difference between estimates at two successive times). Under stated conditions it converges to an optimal policy against a fixed opponent, with no opponent model and no explicit search (pp. 9–11).
- Dynamic programming (the optimal-control methods built on the Bellman equation) is counted as RL by the authors, because complete- and incomplete-knowledge cases are closely related (p. 15).
- History: trial-and-error learning (psychology), optimal control (Bellman), and temporal-difference learning merged in the late 1980s (pp. 13–14, 21).

## L3 — Walkthrough

**Opening (p. 1).** Learning from interaction is presented as foundational. The book takes an engineer's view: it studies idealized learning situations and designs machines, evaluating them by analysis or experiment (p. 1). RL is "much more focused on goal-directed learning from interaction" than other machine-learning approaches (p. 1).

### 1.1 Reinforcement Learning
- **Definition.** RL is learning what to do (how to map situations to actions) to maximize a numerical reward signal. The learner is not told which actions to take and must discover them by trying (p. 1).
- **Two features.** In the most interesting and challenging cases, actions may affect not only immediate reward but also the next situation and so all later rewards. Trial-and-error search and delayed reward are the two most important distinguishing features (p. 1).
- **Three meanings of one name.** "Reinforcement learning" names a problem, a class of solution methods, and a field. The authors insist these be kept separate; mixing problem and method causes confusion (p. 2).
- **Formalization.** The problem is formalized from dynamical systems theory as optimal control of incompletely known MDPs (details in Chapter 3). An agent must sense the state of its environment to some extent, act to affect it, and have goals relating to it. MDPs include sensation, action and goal in simplest form. Any method well suited to such problems counts as an RL method (p. 2).
- **Versus supervised learning.** Supervised learning uses labeled examples from a knowledgeable supervisor and aims to generalize to new situations. It is not adequate alone for interaction, because examples that are correct and representative of all situations are often impractical to obtain (p. 2).
- **Versus unsupervised learning.** This finds hidden structure in unlabeled data. RL instead maximizes reward. Finding structure may help, but does not by itself address the RL problem. So RL is a third paradigm (p. 2).
- **Exploration–exploitation.** To get reward the agent must prefer actions that worked before. To find such actions it must try new ones. Neither can be pursued exclusively without failing. On a stochastic task each action must be tried many times to estimate its expected reward. The dilemma has been studied for decades and "remains unresolved". It does not arise at all in the purest forms of supervised and unsupervised learning (p. 3).
- **Whole problem.** RL starts from a complete, interactive, goal-seeking agent that acts under uncertainty. Other work isolates subproblems (supervised learning, planning) without their role in a larger picture. Subproblems should play clear roles in complete agents (p. 3).
- **Agent can be a component.** Example: an agent that monitors a robot's battery charge and sends commands to the robot's control architecture. Its environment is the rest of the robot plus the robot's environment (pp. 3–4).
- **Links to other fields.** RL belongs to a trend toward integration with statistics and optimization. Parameterized approximators in some RL methods address the "curse of dimensionality". RL is the form of machine learning closest to human and animal learning. It has given back a psychological model of animal learning and a model of parts of the brain's reward system (p. 4).
- **General principles.** Since the late 1960s many AI researchers presumed there were no general principles and only many special-purpose tricks ("strong methods" versus "weak methods"). The authors call this view premature and now uncommon. RL is part of the swing back toward simple general principles (p. 4).

*Intuition note.* The learner is not told which action is right; it gets a reward signal instead. It must try things, and a move's effect may show only later. That is why RL needs both search and credit for delayed outcomes.

### 1.2 Examples (pp. 4–6)
Examples: a chess move; a refinery adaptive controller that need not stick to engineers' set points; a gazelle calf learning to run; a robot choosing between collecting trash and recharging; Phil preparing breakfast (goal–subgoal hierarchies) (pp. 4–5).

Shared features:
- an active agent interacting with its environment and seeking a goal despite uncertainty;
- actions affect future states, so correct choice needs foresight (p. 5);
- action effects cannot be fully predicted, so the agent must monitor and react (Phil watches the milk) (p. 5);
- goals are explicit in that progress can be judged from what the agent senses (p. 5);
- experience improves performance. Prior knowledge influences what is easy to learn, but interaction is essential for adapting to the task's specifics (pp. 5–6).

### 1.3 Elements of Reinforcement Learning
Beyond agent and environment there are four subelements (p. 6).
- **Policy.** A mapping from perceived states to actions (like stimulus–response rules). It may be a table or involve search, and may be stochastic. It alone suffices to determine behavior (p. 6).
- **Reward signal.** On each step the environment sends one number. The agent's sole objective is to maximize total reward over the long run. Reward defines good and bad events and is the primary basis for changing the policy (p. 6).
- **Value function.** The value of a state is the total reward an agent can expect to accumulate from that state onward. A state can have low immediate reward but high value if high-reward states follow, or the reverse (p. 6).
- **Primary versus secondary.** Rewards are primary; values are predictions of reward and secondary. Yet action choice rests on values, because maximizing long-run reward means seeking states of highest value. Values must be estimated from experience over the agent's lifetime, whereas rewards come directly from the environment. A method for efficient value estimation is the most important component of almost all RL algorithms in the book (pp. 6–7).
- **Model.** Something that mimics the environment, e.g. predicts next state and reward from a state and action. Models support planning, meaning deciding by considering possible futures before experiencing them. Methods using models are model-based; those that are explicitly trial-and-error learners are model-free (p. 7).

*Intuition note.* Reward is what the world pays now; value is what you expect to collect from here on. Choosing by value lets a low-reward step lead to a better place.

### 1.4 Limitations and Scope
- **State.** The book takes the state as given by some preprocessing system, informally "whatever information is available to the agent". It does not address constructing or learning the state signal (briefly in Section 17.3). This is because the focus is on decision making (p. 7).
- **Evolutionary methods.** Genetic algorithms, simulated annealing and similar methods never estimate value functions. They run many static policies, each over an extended time, keep the best and vary them. They can be effective if the policy space is small or structured so that good policies are common, or if much time is available. They also have advantages when the agent cannot sense the complete state (pp. 7–8).
- **Why not covered.** They ignore the structure that a policy maps states to actions, and the states visited and actions chosen. Methods that use this "can be much more efficient … in many cases". The authors do not consider evolutionary methods by themselves especially well suited to RL and do not cover them (p. 8).

### 1.5 An Extended Example: Tic-Tac-Toe
**Setup.** We play X against an imperfect opponent. For now draws and losses count as equally bad (p. 8).

**Classical approaches.**
- Minimax is not correct here because it assumes a particular way of playing by the opponent. A minimax player would never enter a state from which it could lose, even if it always won from that state against this opponent (p. 8).
- Dynamic programming gives an optimal solution for any opponent, but needs a complete specification of the opponent's move probabilities. Assuming this is unavailable, about the best one can do is to learn an opponent model first and then apply dynamic programming to it. This is not that different from some RL methods later in the book (pp. 8–9).
- An evolutionary method would search policy space (a policy being a rule giving a move for every board state). It would estimate each policy's winning probability by playing games, for example by hill-climbing or with a population of policies (p. 9).

**Value-function method.**
- Keep a table with one number per game state: the latest estimate of the probability that we win from that state. This is the state's value, and the table is the learned value function (p. 9).
- Initial values: 1 for states with three Xs in a row, 0 for states with three Os in a row or filled boards, 0.5 for all others (p. 9).
- Move selection: look up the values of the states each possible move leads to. Most of the time move greedily (highest value). Occasionally pick randomly among other moves; these are exploratory moves (p. 9).
- Learning: after each greedy move, "back up" the value of the later state to the earlier state. Let $S_t$ be the state before the greedy move and $S_{t+1}$ the state after. The update is a move a fraction of the way toward the later value (p. 9, image p. 10):
$$V(S_t) \leftarrow V(S_t) + \alpha\big[V(S_{t+1}) - V(S_t)\big]$$
Here $\alpha$ is a small positive fraction, the step-size parameter, which sets the learning rate. This is a temporal-difference (TD) update, named because it uses the difference $V(S_{t+1})-V(S_t)$ between estimates at two successive times (p. 10).
- Figure 1.1: exploratory moves do not cause learning; each other move does, with values moved up the tree from later to earlier nodes (p. 10).

**Performance claims (authors' statements, p. 10).**
- If $\alpha$ is reduced properly over time, the method converges, for any fixed opponent, to the true winning probabilities given optimal play by our player.
- The non-exploratory moves then taken are optimal against this opponent.
- If $\alpha$ is not reduced all the way to zero, the player also plays well against opponents that slowly change their play.

**Evolutionary versus value methods.** An evolutionary method holds a policy fixed over many games. The win frequency gives an unbiased estimate of that policy's win probability. But policy changes occur only after many games, and only each game's final outcome is used. All behavior in a won game gets credit, "even … moves that never occurred" (p. 11). Value-function methods evaluate individual states and use information available during play. Both search policy space (p. 11).

**Key features shown (p. 11).**
- Learning while interacting.
- A clear goal, with correct play needing foresight about delayed effects. The simple player would learn multi-move traps for a shortsighted opponent.
- The effect of planning and lookahead is obtained without an opponent model and without explicit search.

*Intuition note.* Each state's value is nudged toward the value of the state that follows it. A final win or loss therefore leaks backwards, game after game, to the earlier positions that led there.

**Beyond tic-tac-toe (pp. 11–12).**
- RL applies without an adversary ("game against nature"), without episodes, with continuing tasks and rewards at any time, and with continuous time (theory omitted here).
- It applies with huge or infinite state sets. Tesauro combined the algorithm with a neural network for backgammon (about $10^{20}$ states). The program eventually played better than the world's best humans. Generalization from past states is what the network supplies. This is where supervised learning is most needed inside RL (pp. 11–12).
- It does not require a tabula rasa: prior information can be incorporated. The state can be partly hidden (p. 12).
- Models are optional. The tic-tac-toe player must foresee the results of its own moves, yet it is model-free with respect to the opponent. Model-free methods can have advantages when constructing an accurate model is the real bottleneck, and are building blocks for model-based methods. RL can also work at several levels of a hierarchy (p. 12).

### 1.6 Summary (p. 13)
RL is a computational approach to goal-directed learning and decision making by an agent interacting directly with its environment. It requires no exemplary supervision or complete model. The authors' opinion is that RL is the first field to seriously address the computational issues of learning from interaction for long-term goals. MDPs define the interaction in terms of states, actions and rewards, capturing cause and effect, uncertainty and explicit goals. The authors take the position that value functions are important for efficient search in policy space. This separates RL from evolutionary methods (p. 13).

### 1.7 Early History
Three threads (trial and error, optimal control, temporal difference) merged in the late 1980s (pp. 13–14).

**Optimal control thread (pp. 14–15).**
- "Optimal control" came into use in the late 1950s. In the mid-1950s Bellman and others extended Hamilton–Jacobi theory, using state and a value ("optimal return") function to define a functional equation, now called the Bellman equation. Solving it is dynamic programming (Bellman 1957a). Bellman (1957b) introduced MDPs, and Howard (1960) devised policy iteration (p. 14).
- Dynamic programming is widely considered the only feasible way to solve general stochastic optimal control problems. Its computation grows exponentially with the number of state variables (Bellman's "curse of dimensionality"), yet it is more efficient and widely applicable than other general methods (p. 14).
- Possible reasons for the late link to learning (the authors say they cannot be sure): the likely main cause was the separation of the disciplines and their goals; also perhaps the prevalent view of dynamic programming as off-line and dependent on accurate models; and the fact that its simplest form runs backwards in time. Full integration with online learning came, in the authors' view, with Watkins (1989) (pp. 14–15).
- The authors consider all optimal control work to be, in a sense, work in RL. Most conventional methods need complete system knowledge, but many dynamic programming algorithms are incremental and iterative, like learning methods. Theories for complete and incomplete knowledge are so closely related that they belong together (p. 15).

**Trial-and-error thread (pp. 15–19).**
- Thorndike's Law of Effect (1911) in brief: other things being equal, responses followed by satisfaction become more likely to recur in that situation, and those followed by discomfort less likely, with strength depending on the degree (p. 15). The law has been controversial but is widely regarded as a basic principle (p. 16).
- "Reinforcement" first appeared in this context, to the authors' knowledge, in the 1927 translation of Pavlov. Some psychologists later extended the idea to include weakening of behavior and omission of stimuli; for something to count as a reinforcer, the change must persist after the reinforcer is withdrawn (p. 16).
- Turing (1948) described a "pleasure-pain system" along these lines. Electro-mechanical learners followed: Ross (1933) maze machine, Walter's tortoise, Shannon's maze mouse Theseus (1952), Minsky's SNARCs (1954) (p. 16).
- Confusion with supervised learning (Farley and Clark; Rosenblatt; Widrow and Hoff) partly led to genuine trial-and-error research becoming rare in the 1960s–70s. Trial and error means selecting actions from evaluative feedback that does not rely on knowing the correct action (p. 17).
- Minsky (1961) named the credit-assignment problem: how to distribute credit for success among the many decisions involved. All methods in the book are in a sense directed at it (p. 17).
- Other work:
  - Andreae's STeLLA, with an internal model and a "leakback" credit mechanism (p. 17).
  - Michie's MENACE (matchboxes with colored beads for tic-tac-toe), GLEE, and BOXES. BOXES balanced a cart-pole from a failure signal alone, an early RL task with incomplete knowledge (pp. 17–18).
  - Widrow, Gupta and Maitra's "learning with a critic" instead of "learning with a teacher". The authors' term "critic" derives from it (p. 18).
  - Learning automata and the k-armed bandit (a nonassociative selectional problem; Chapter 2) (p. 18).
  - Economics (Cross 1973), Holland's classifier systems with the bucket-brigade credit-assignment algorithm, and Klopf's hedonic view that revived the thread (p. 19).

**Temporal-difference thread (pp. 20–21).**
- TD methods are driven by differences between successive estimates of the same quantity. Origins lie partly in secondary reinforcers, stimuli paired with a primary reinforcer. Samuel (1959) first implemented TD ideas in his checkers program. Minsky (1961) linked this to secondary reinforcement (p. 20).
- Klopf (1972) and Sutton (1978) brought together trial and error and TD ideas and links to animal learning, including a TD model of classical conditioning. The actor–critic architecture was applied to Michie and Chambers's pole balancing. Sutton (1988) separated TD learning from control as a general prediction method and introduced TD($\lambda$). Witten (1977) published what appears to be the earliest TD rule, tabular TD(0) (pp. 20–21).
- Watkins's Q-learning (1989) fully joined the TD and optimal control threads. TD-Gammon (1992) brought attention. Later, TD behavior was noted to resemble dopamine-neuron activity (Chapter 15) (p. 21).

**Bibliographical remarks (p. 22).** The chapter lists general RL books and surveys. It notes that Phil's breakfast was inspired by Agre (1988), and that the TD method of the tic-tac-toe example is developed in Chapter 6 (p. 22).

## Toy example (ours, not from the text)
A three-state "game": $s_1 \to s_2 \to$ win. A win has value 1. Start with $V(s_1)=V(s_2)=0.5$. Take $\alpha = 0.5$, chosen for easy arithmetic (the text says "small"). Apply $V(S_t)\leftarrow V(S_t)+\alpha[V(S_{t+1})-V(S_t)]$ after each move.

Game 1:
- Move $s_1\to s_2$: $V(s_1)=0.5+0.5(0.5-0.5)=0.5$.
- Move $s_2\to$ win: $V(s_2)=0.5+0.5(1-0.5)=0.75$.

Game 2:
- Move $s_1\to s_2$: $V(s_1)=0.5+0.5(0.75-0.5)=0.625$.
- Move $s_2\to$ win: $V(s_2)=0.75+0.5(1-0.75)=0.875$.

The win information has moved backwards from $s_2$ to $s_1$. Both values keep rising toward 1 only because this fictional game is always won.

## Concepts
- [[policy]] — roughly, a mapping from perceived states to actions; alone sufficient to determine behavior; may be stochastic (p. 6)
- [[bellman-equation-value-function]] — value of a state = expected total future reward from it; estimated, not given (p. 6); Bellman equation as the dynamic-programming functional equation (p. 14)
- [[markov-decision-process]] — formal framework of states, actions and rewards for agent–environment interaction; formal definition in Chapter 3 (pp. 2, 13)
- [[exploration-vs-exploitation]] — must try new actions to learn, yet use known good ones; unresolved (p. 3)
- [[temporal-difference-learning]] — updates driven by the difference between estimates at successive times (p. 10)
- [[model-based-vs-model-free-rl]] — planning with a model of the environment versus explicit trial-and-error learning (p. 7)
- [[state]] — informally, whatever information the agent has about its environment (p. 7)
- [[reward-signal]] (new) — single number per step defining the goal; agent maximizes its long-run total (p. 6)
- [[trial-and-error-learning]] (new) — choosing actions from evaluative feedback without knowing the correct action (p. 17)
- [[credit-assignment]] (new) — spreading credit for an outcome over the decisions that produced it (p. 17)
- [[evolutionary-methods]] (new) — search over policies using whole-lifetime outcomes, with no value estimates (p. 7)
- [[dynamic-programming]] (new) — optimal-control solution methods based on the Bellman equation; almost all conventional methods require complete knowledge of the system (pp. 14–15)
- [[supervised-vs-reinforcement-learning]] (new) — labeled correct answers versus an evaluative reward only (pp. 2, 17)
- [[step-size-parameter]] (new) — fraction $\alpha$ setting how far an update moves toward its target (p. 10)

## Canonical instances
- [[tic-tac-toe-td-player]] — value table plus TD updates; learns without an opponent model (pp. 9–11)
- [[td-gammon]] — TD plus a neural network for a game of about $10^{20}$ states (p. 11)
- [[menace-boxes]] — Michie's matchbox tic-tac-toe learner and cart-pole BOXES (pp. 17–18)
- [[refinery-adaptive-controller]] — real-time optimization not tied to the original set points (pp. 4–5)
- [[phil-breakfast]] — nested goals and subgoals in everyday behavior (p. 5)

## Bridges (candidates)
- [structural-analogy] TD error between successive value estimates ↔ neuroscience: dopamine-neuron activity (the text reports an "uncanny similarity", p. 21)
- [structural-analogy] Value function ↔ control theory: the optimal return function of the Bellman equation (p. 14); the chapter treats optimal control as work in RL (p. 15)
- [metaphor] Evolutionary policy search ↔ biological evolution (the text calls the operation "analogous", p. 7)
- [structural-analogy] Policy as stimulus–response rules ↔ psychology: Law of Effect (pp. 6, 15)

## Questions this raises
- If exploration and exploitation cannot both be pursued exclusively, how can one choose how much to explore (Chapter 2)?
- What precisely does "converges to the optimal policy" need (decay of $\alpha$, exploration, fixed opponent), and how is this proved?
- How does the Markov decision process make "state" precise (Chapter 3)?
- How can reward be assigned to early decisions when only the final outcome is known?

## Exercises worth doing
- Ex. 1.1 (p. 12) — self-play: what happens when both sides learn — difficulty: medium
- Ex. 1.2 (p. 12) — exploit symmetries; should symmetric positions always share a value? — difficulty: medium
- Ex. 1.3 (p. 12) — greedy play without exploration: what goes wrong — difficulty: easy
- Ex. 1.4 (p. 13) — learning from exploratory moves: which two probability sets result — difficulty: hard
- Ex. 1.5 (p. 13) — other improvements to the player — difficulty: medium

## Reading notes
- Printed page = pdf − 22 (pdf 23 = printed 1).
- The text layer garbles Greek letters and symbols: $\alpha$ appears as "↵", the arrow and brackets in the update rule are lost, and the $\lambda$ is missing (read from the gap; no p. 21 image checked) in "TD($\lambda$)" (shown as "TD( )"). The page image of p. 10 confirms the update rule as written above. The exponent in $10^{20}$ appears as "1020" in the text layer.
- Figure 1.1 labels are garbled in the text; I used the image of p. 10 (nodes a–g, starred best moves, red backup arrows).
- Exercise statements end with a star symbol in the text.
- Section 1.7 is condensed; many names and dates were selected, not all reproduced.
