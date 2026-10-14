---
id: sutton-2018-rl/ch17-frontiers
work: sutton-2018-rl
unit: "Chapter 17 — Frontiers"
pages: 459-480
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Frontiers (Sutton & Barto, ch. 17)

## L0 — One line
The chapter points to topics it sees as important for RL's future: predicting many signals, planning with multi-step options, building states from observation histories, designing rewards with care, and making embedded agents safe.

## L1 — The gist (≤ 120 words)
The chapter asks what lies beyond the book's framework. It sketches four extensions: predicting any signal (general value functions), planning with multi-step courses of action (options), building agent state from the history of observations and actions, and designing reward signals. It then lists six open issues and discusses the promise and danger of putting RL agents into the real world. The authors say many of these topics go beyond what is reliably known. One recurring idea is that learning many predictions may help an agent build its state features. On safety, they say careful reward design is essential for agents in the real world, and that adapting control-engineering methods is one of the most pressing areas.

**Prerequisites:** MDPs, value functions, Bellman equations, value iteration, off-policy learning, function approximation, TD learning, and the idea of a model (chs. 3, 4, 8, 10–12).

## L2 — Key ideas
- A general value function (GVF) predicts the discounted sum of any signal (the "cumulant"), under any policy and any state-dependent termination (discount) function. It can be learned with the book's usual methods (p. 459–460).
- Auxiliary prediction tasks can help the main task by shaping shared representations. Learned predictions can also trigger built-in reflexes, as in classical conditioning (p. 460–461).
- An option (policy plus termination function) generalizes action. Its model has a discounted reward part and a discounted transition part that does not sum to one. This gives Bellman equations and value iteration over options (p. 461–463).
- Without explicit states, state is a function of history. It is Markov if and only if equal states imply equal test probabilities (a test is a specific future sequence of actions and observations). It should be compact and recursively updatable (p. 465–466).
- Belief states (from partially observable MDPs, or POMDPs) and predictive state representations are two examples of a Markov state. In practice the agent's state will only approximate Markov, and the authors say there are no useful theoretical guarantees at present for that case (p. 467–468).
- Reward design is critical. Ways to get or improve a reward signal include value initialization, shaping, imitation or inverse RL, and automated reward search. The agent's best reward may differ from the designer's goal (p. 469–472).
- Six open issues remain, including online deep learning, representation learning, planning with learned models, automatic task choice, curiosity, and safety (p. 472–474).
- Because RL is based on optimization, it inherits the risks as well as the benefits of optimization. The authors point to control engineering's modelling, testing and stability theory as a source of methods to adapt for safety (p. 476–478).

## L3 — Walkthrough

### 17.1 General value functions and auxiliary tasks (p. 459–461)

**Definitions.** Earlier chapters let value depend on an arbitrary target policy and, via a termination function $\gamma: \mathcal S \to [0,1]$, on a state-dependent discount (12.17) (p. 459). The next step is to predict arbitrary signals instead of reward. The summed signal is called the **cumulant**, $C_t \in \mathbb R$. A **general value function** is

$$v_{\pi,\gamma,C}(s) \doteq \mathbb E\!\left[\sum_{k=t}^{\infty}\Big(\prod_{i=t+1}^{k}\gamma(S_i)\Big)C_{k+1}\;\Big|\; S_t=s,\ A_{t:\infty}\sim\pi\right]. \tag{17.1}$$

It is approximated by a parameterized form such as $\hat v(s,\mathbf w)$, with a different $\mathbf w$ for each choice of $\pi,\gamma,C$ (p. 459). The authors say "value function" is perhaps a misnomer, since there is no necessary link to reward. "Prediction" or "forecast" (Ring, in preparation) are alternative names. A GVF has the form of a value function, so the book's methods can learn it. Policies maximizing it can be learned by generalized policy iteration or actor–critic (p. 459–460).

**Why predict signals other than reward?** These are *auxiliary tasks*, extra to the main task. The authors first say diverse predictions can form a powerful kind of environmental model (explained later), then give two simpler ways, and a last, perhaps most important, role.
1. *Shared representations.* Auxiliary tasks may need the same features as the main task and may be easier (less delay, clearer action–outcome link). Good features found early on easy tasks may speed the main task. There is "no necessary reason" this holds, but it often seems plausible (p. 460).
   - Architecture: a neural network with several "heads" (output parts), one for the main value function and others for auxiliary tasks. In the authors' picture, all heads could send errors by stochastic gradient descent into a shared body, which would then try to build representations supporting all heads.
   - Examples tried: predicting pixel change, the next reward, and the distribution of the return. In many cases this greatly accelerated learning on the main task (Jaderberg et al., 2017) (p. 460).
2. *Pavlovian-style reflexes.* One way to understand classical conditioning is as a learned prediction linked to a built-in (not learned) reaction. Example: humans and many animals appear to blink whenever their prediction of being poked in the eye exceeds a threshold. Designers can do the same. A self-driving car could stop when its learned collision prediction exceeds a threshold. A vacuum robot could head for the charger whenever its learned prediction of running out of battery before returning is non-zero. The correct prediction depends on house size, room and battery age, which are hard for a designer to know. A reliable rule in sensor terms would be hard to build in, but a rule in terms of the learned prediction might be easy (p. 460–461).
3. *Learning the state representation.* The authors call this perhaps the most important role: moving beyond the assumption that the state representation is fixed and given. It is deferred to 17.3 (p. 461).

*Intuition note.* A GVF is the usual value function with the reward replaced by any signal you care about. Learning many such predictions at once may push the learner toward useful features (the authors' example: part of the idea of physical objects), and those features may also help with reward.

### 17.2 Temporal abstraction via options (p. 461–464)

**Motivation.** MDPs can formalize tasks at very different time scales: muscle twitches, flights, jobs. One might think a single MDP cannot cover all levels, since planning a flight in muscle twitches is useless; the authors answer "Perhaps it can." One popular idea: define the MDP at a fine time step and plan at higher levels with extended courses of action (p. 461).

**Options.** An option is $\omega=\langle\pi_\omega,\gamma_\omega\rangle$: a policy and a state-dependent termination function. To execute it at time $t$, take $A_t\sim\pi_\omega(\cdot|S_t)$, then terminate at $t+1$ with probability $1-\gamma_\omega(S_{t+1})$. If it does not terminate, continue with $A_{t+1}$, and so on (p. 461–462). A low-level action $a$ is an option with $\pi_\omega(s)=a$ for all $s\in\mathcal S$ and $\gamma_\omega(s)=0$ for all $s\in\mathcal S^+$, so options effectively extend the action space (p. 462).

**Generalizations.**
- The action-value function becomes an *option-value function*. The policy becomes a *hierarchical policy* that selects options, which run until termination (p. 462).
- In the simplest case, update only when an option terminates. More subtly, updates can be made on each time step by "intra-option" algorithms, which in general require off-policy learning (p. 462).

**Option models.** The model has two parts. The reward part is

$$r(s,\omega)\doteq\mathbb E\big[R_1+\gamma R_2+\gamma^2R_3+\cdots+\gamma^{\tau-1}R_\tau\;\big|\;S_0=s,\ A_{0:\tau-1}\sim\pi_\omega,\ \tau\sim\gamma_\omega\big], \tag{17.2}$$

where $\tau$ is the random termination time. Discounting is by $\gamma$, while termination is by $\gamma_\omega$ (p. 462). The transition part, for each start state $s$ and each possible termination state $s'$, is

$$p(s'|s,\omega)\doteq\sum_{k=1}^{\infty}\gamma^{k}\Pr\{S_k=s',\ \tau=k\mid S_0=s,\ A_{0:k-1}\sim\pi_\omega,\ \tau\sim\gamma_\omega\}. \tag{17.3}$$

Because of the factor $\gamma^k$, this $p$ is no longer a transition probability, and does not sum to one over $s'$ (p. 462).

**Planning with options.** The Bellman equation for a hierarchical policy $\pi$ is

$$v_\pi(s)=\sum_{\omega\in\Omega(s)}\pi(\omega|s)\Big[r(s,\omega)+\sum_{s'}p(s'|s,\omega)\,v_\pi(s')\Big], \tag{17.4}$$

with $\Omega(s)$ the options available in $s$. If $\Omega(s)$ holds only low-level actions, this reduces to a version of (3.14), with no explicit $\gamma$ because $\gamma$ is inside $p$ (p. 463). Value iteration with options is

$$v_{k+1}(s)\doteq\max_{\omega\in\Omega(s)}\Big[r(s,\omega)+\sum_{s'}p(s'|s,\omega)\,v_k(s')\Big],\quad\text{for all }s\in\mathcal S.$$

If $\Omega(s)$ includes all low-level actions, it converges to the conventional $v_*$. If only a subset of options is considered, it converges to the best hierarchical policy limited to that subset. That policy may be sub-optimal, but convergence can be much faster (fewer options, and each option jumps over many steps) (p. 463).

**Learning option models as GVFs.** One natural way to learn the option model is as a collection of GVFs (p. 463).
- *Reward part:* use cumulant $C_t=R_t$, policy $\pi=\pi_\omega$, termination $\gamma(s)=\gamma\cdot\gamma_\omega(s)$. The true GVF then equals $r(s,\omega)$.
- *Transition part:* use one GVF per possible termination state $s'$, with cumulant $C_t=(1-\gamma_\omega(S_t))\,\mathbb 1_{S_t=s'}$ and the same policy and termination functions. The true GVF then equals $p(s'|s,\omega)$.
- Putting these together with function approximation and other components is "beyond the current state of the art" (p. 463).

*Intuition note.* An option is a macro-action that runs for a random number of steps. Its model tells you the discounted reward collected and the discounted chance of ending in each state. Planning over a restricted set of options can converge much faster, since fewer options are considered and each option jumps over many time steps.

**Exercise 17.1** (p. 464) asks for the average-reward analogues of (17.4), (17.2) and (17.3).

### 17.3 Observations and state (p. 464–468)

**Background.** Tabular methods (Part I) amount to assuming the state is fully observed. Parametric function approximation (Part II) is far less restrictive. If a state variable is unobservable, the parameterization can make the value independent of it, so the authors say all results for the parameterized case carry over to partial observability unchanged (p. 464). Still, many issues need an explicit treatment. There are four steps.

**Step 1: change the problem (p. 464).** The environment emits observations $O_t\in\mathcal O$, not states. Without loss of generality, reward is a known function of the observation. The interaction is the sequence $A_0,O_1,A_1,O_2,\dots$, either endless or in episodes.

**Step 2: recover state from the data stream (p. 465).**
- *History:* $H_t\doteq A_0,O_1,\dots,A_{t-1},O_t$. It is the most we can know about the past from the data stream, but it grows without bound.
- A *state* is a compact summary $S_t=f(H_t)$. It is *Markov* if it keeps all information in the history needed to predict futures as well as the full history does. Real agents' states will not be Markov but may approach it as an ideal.
- A *test* is a specific future sequence of alternating actions and observations. For a three-step test $\tau=a_1o_1a_2o_2a_3o_3$:

$$p(\tau|h)\doteq\Pr\{O_{t+1}=o_1,O_{t+2}=o_2,O_{t+3}=o_3\mid H_t=h,A_t=a_1,A_{t+1}=a_2,A_{t+2}=a_3\}. \tag{17.5}$$

- Formally, $f$ is Markov if and only if

$$f(h)=f(h')\ \Rightarrow\ p(\tau|h)=p(\tau|h'),\quad\text{for all }h,h',\tau\in\{\mathcal A\times\mathcal O\}^*. \tag{17.6}$$

- A Markov state is enough for any prediction, including any GVF. It is also enough for optimal behavior: if $f$ is Markov, there is always a deterministic $\pi$ such that $A_t\doteq\pi(f(H_t))$ is an optimal policy (p. 465).

**Step 3: computational considerations (p. 465–467).**
- The state should be *compact* (the identity $S_t=H_t$ is Markov but grows unboundedly) and recursively updatable by a **state-update function** $u$:

$$S_{t+1}\doteq u(S_t,A_t,O_{t+1}),\ \text{for all }t\ge0,\ \text{with }S_0\text{ given}. \tag{17.7}$$

  Given $f$ one can always construct a $u$, but it may be inconvenient or non-compact. $u$ must be cheap to compute, since no action or prediction is possible until the state is available. Fig. 17.1 shows an agent architecture with $u$, policy/value function, model and planner. The model and planner see only the states produced by $u$, not observations (p. 465–466).
- *One-step criterion:* if $f$ is incrementally updatable, then it is Markov if and only if

$$f(h)=f(h')\ \Rightarrow\ \Pr\{O_{t+1}=o|H_t=h,A_t=a\}=\Pr\{O_{t+1}=o|H_t=h',A_t=a\}, \tag{17.8}$$

  for all $h,h'\in\{\mathcal A\times\mathcal O\}^*$, $o\in\mathcal O$, $a\in\mathcal A$ (p. 466).
- Accurate one-step predictions plus $u$ determine the probability of any test, by alternating one-step prediction and state update. Caveats: getting long-term predictions this way is exponentially complex in their length. It works only if one-step predictions are exact, because errors compound and can make long-term predictions "wildly inaccurate", which often happens in practice (p. 466–467).

**POMDP example (p. 467).** The environment has a latent state $X_t$ that the agent never sees (not to be confused with the agent state $S_t$). The natural Markov state is the *belief state*, the distribution over latent states given the history. With $d$ latent states, $\mathbf S_t\doteq\mathbf s_t\in[0,1]^d$ with

$$\mathbf s_t[i]\doteq\Pr\{X_t=i\mid H_t\},\quad i\in\{1,\dots,d\}. \tag{17.9}$$

Its size stays fixed as $t$ grows. It is updated by Bayes' rule, assuming complete knowledge of the environment's workings:

$$u(\mathbf s,a,o)[i]\doteq\frac{\sum_{x=1}^{d}\mathbf s[x]\,p(i,o|x,a)}{\sum_{x=1}^{d}\sum_{x'=1}^{d}\mathbf s[x]\,p(x',o|x,a)},\quad\text{for all }a\in\mathcal A,\,o\in\mathcal O, \tag{17.10}$$

where $p(x',o|x,a)\doteq\Pr\{X_t=x',O_t=o\mid X_{t-1}=x,A_{t-1}=a\}$ is the POMDP (latent-state) analogue of the MDP four-argument $p$. The authors say it is popular in theory with many applications, but its assumptions and computation "scale poorly", and they do not recommend it as an approach to AI (p. 467).

**Predictive State Representations (PSRs) (p. 467).** In a PSR, the state is a $d$-vector of probabilities of $d$ chosen "core" tests (17.5), updated by a Bayes-like $u$. Its meaning is grounded in observable predictions instead of the never-observed $X_t$, which arguably makes learning easier. Extensions are listed (end-tests, compositional tests, spectral methods, TD-learned abstract tests). Some of the best theory is for Observable Operator Models and Sequential Systems (Thon, 2017).

**Step 4: re-introduce approximation (p. 468).**
- Simplest approximate state: the latest observation, $S_t=O_t$. It cannot handle hidden information. Better is the $k$th-order history, the last $k$ observations and actions ($k\ge1$), kept by a shift-in/shift-out $u$. It is still simple but can greatly increase capabilities.
- If (17.8) holds only approximately, long-term prediction can degrade dramatically from slightly inaccurate one-step predictions. Longer-term tests, GVFs and state-update functions may or may not approximate better. The objectives differ and there are "no useful theoretical guarantees at present" (p. 468).
- The authors propose a heuristic to replace the Markov guarantee: what is good for some predictions may be good for others. This links to multi-headed learning (17.1). The suggested approach is to pursue many predictions and use them to direct the construction of state features. The agent, not a person, should choose the predictions, which would need a general language for predictions.
- POMDP and PSR approaches can be used with approximate states. State need not be accurate to its semantics to be useful. For example, echo state networks (Jaeger, 2002) keep almost arbitrary information about history and can perform well. Learning the state-update function is a major part of the representation-learning problem in RL (p. 468).

*Intuition note.* If you cannot see the world's state, you keep a running summary of what you have seen and done. It is a perfect summary if it lets you predict every possible future as well as the full history would (for a state that can be updated incrementally, exact next-step predictions are enough). A belief state is one exact summary. Practical agents use cruder ones, with no guarantee, but many predictions may guide them.

### 17.4 Designing reward signals (p. 469–472)

- RL needs no instruction about correct actions, but success depends strongly on how well the reward frames the designer's goal. The reward signal is the part of the environment that computes $R_t$. By ch. 14's discussion it is more like a signal inside an animal's brain, and the brain parts that generate such signals evolved over millions of years, so good design is not always easy (p. 469).
- *Challenges.* Goals that are easy to define (a game score) are easy to reward. Complex tasks such as a household robot are hard to translate. Agents may find unexpected, possibly undesirable or dangerous ways to get reward (revisited in 17.6). *Sparse reward* means reward is too rare, so the agent may wander aimlessly (Minsky's "plateau problem"). In practice designers use informal trial and error (p. 469).
- *Subgoal rewards* can mislead the agent away from the true goal. A better way to give guidance is to leave the reward alone and initialize the value function with a guess $v_0$. With linear features $\mathbf x:\mathcal S\to\mathbb R^d$:

$$\hat v(s,\mathbf w)\doteq\mathbf w^\top\mathbf x(s)+v_0(s). \tag{17.11}$$

  With $\mathbf w=\mathbf 0$ the initial value is $v_0$, and the asymptotic quality is set by the features as usual. This works for nonlinear approximators too, but speed-up is not guaranteed (p. 470).
- *Shaping* (Skinner; Section 14.3). Sparse reward is also a problem of the agent's policy, which rarely meets rewarding states. Shaping changes the reward (and possibly the task dynamics) as learning proceeds. It starts from a non-sparse reward for the current behavior and moves gradually to the real problem. The agent faces increasingly hard problems, each easier because of the earlier ones (p. 470).
- *Imitation / inverse RL.* If an expert is observable, one can imitate by supervised learning or recover a reward by inverse RL and then run RL on it. Recovery cannot be exact, since a policy is optimal for many rewards (all policies are optimal for a constant reward), but plausible candidates exist. The method needs strong assumptions: known dynamics, features in which reward is linear, and repeatedly solving the full problem. Abbeel and Ng (2004) argue it can sometimes beat supervised learning (p. 470–471).
- *Automated reward search (bilevel optimization).* Treat the reward as an algorithm parameter. An outer optimizer scores each candidate reward by running RL with it and applying a "high-level" objective that encodes the designer's true goal. Online gradient ascent on that objective is possible (Sorg et al., 2010). This is analogous to evolution: the high-level objective is evolutionary fitness (p. 471).
  - Experiments (Singh, Lewis, and Barto, 2009) show intuition alone is not always adequate. Performance can be very sensitive to reward details. An agent's goal should not always equal the designer's goal. A possible explanation: the agent may be unable to reach the designer's goal whatever its reward, and under limits on computation, information or time, pursuing a different goal can sometimes end up closer to the designer's goal than pursuing it directly (p. 471).
  - Natural examples: because we cannot directly assess the nutritional value of most foods, evolution gave us a reward that makes us seek certain tastes (not infallible). An animal cannot always observe its own fitness, so evolution supplies rewards tied to observable predictors of it (p. 471).
- An RL agent can be a component of a larger system. Reward may then depend on internal factors (motivation, memories) or on learning progress itself. This leads to "intrinsically-motivated reinforcement learning" (p. 472).

### 17.5 Remaining issues (p. 472–474)

The foundation described is model-free and model-based methods working together (Dyna, ch. 8), with function approximation and online incremental algorithms, including off-policy training. GVFs and option models both involve off-policy learning, and the authors say the full rationale for off-policy training is given only in this chapter (p. 472). Six issues remain:
1. **Online deep function approximation.** Deep learning works well only with batch training on large data sets, off-line self-play, or interleaved experience of multiple agents. It struggles in incremental online settings because of "catastrophic interference" or "correlated data": new learning tends to replace old. Replay buffers are a workaround. The authors see no reason the limitation is insurmountable, but no fix has yet been devised (p. 472–473).
2. **Representation learning** (also called constructive induction or meta-learning): learning features so that future learning generalizes better. It is an old problem. The authors say perhaps there is no solution, but it is equally likely that the time for one has not yet arrived, and in RL it can be identified with learning the state-update function. A footnote states they are unconvinced that DQN (Section 16.5) already solves it (p. 473).
3. **Scalable planning with learned models.** Planning works well when the model is known (AlphaGo Zero, computer chess). Full model-based RL with learned models is rare. Dyna is usually tabular, few studies used learned linear models, and even fewer used option models. Model learning must be selective, focusing on key consequences of the important options, because irrelevant detail can make planning "almost useless" (p. 473).
4. **Automating the choice of tasks.** Cumulants, policies and termination functions of GVFs are now chosen by hand. They should be represented in the machine so they can be set, monitored and searched, with tasks built on tasks like features in a network. "The tasks are the questions, and the contents of the ANN are the answers" (p. 474).
5. **Curiosity.** When reward is absent or weakly dependent on behavior, learning progress can serve as intrinsic reward. Other intrinsic signals mark novelty or the agent's ability to cause change. The agent can use them to pose tasks for itself, a computational analog of play (p. 474).
6. **Safety** of embedding agents in physical environments, discussed in 17.6 (p. 474).

### 17.6 RL and the future of AI (p. 475–478)

- *Status.* Since the first edition, AI promise has become applications, and "deep reinforcement learning" is among the most remarkable developments. A large gap remains between AI and humans and other animals. Superhuman performance exists in some domains (even Go), but not complete, interactive, quickly learning agents. RL is expected to be a critical component of such agents (p. 475).
- *Other contributions.* RL links to psychology and neuroscience (chs. 14–15) and, through computational psychiatry, may help treat mental disorders such as addiction (the authors' stated belief). Policies from simulation can advise human decisions in education, healthcare, transportation, energy and public resources, and RL's use of long-term consequences is relevant. RL may overcome some scaling difficulties of traditional decision support (p. 475–476).
- *Warnings.* Warnings have been voiced that AI poses serious threats. The authors recall Herbert Simon's 2000 talk: Prometheus (the gift of fire) and Pandora (the opened box). Simon urged that we are designers of our future, not mere spectators, and that our decisions can tilt the scale in Prometheus' favor; the authors say this is certainly true for RL (p. 476).
- *Simulation vs. real world.* Simulators are safe, generally cheaper than real experience, typically faster than real time, and can make virtually unlimited data available; most current applications learn from simulation. But the full potential of RL requires agents in real-world experience, because it is often hard or impossible to simulate real-world dynamics faithfully, especially when human behavior is involved. It is for such real-world embedded agents that the warnings need to be heeded (p. 476).
- *Optimization risk.* RL inherits the plusses and minuses of optimization. The minus is devising a reward that yields the desired results and avoids undesired ones. When we specify what we want only indirectly, as in a reward signal, we will not know how closely the agent fulfills our wish until learning is complete. Literary versions: Goethe's "The Sorcerer's Apprentice", and Wiener on "The Monkey's Paw": it "grants what you ask for, not what you should have asked for or what you intend" (p. 477). Careful design of reward signals is essential if an agent is to act in the real world without human vetting of its actions or an easy way to interrupt it. Mitigations exist (hard and soft constraints, robust or risk-sensitive policies, several objective functions). Some have been adapted to RL, and more research is needed (p. 477).
- *Safe behavior while learning.* This resembles problems control engineers have long faced (aircraft, chemical processes). Control relies on careful modelling, validation and testing, and has theory on convergence and stability of adaptive controllers when dynamics are not fully known. Guarantees are "never iron-clad" because they depend on assumptions. The authors call adapting and extending control-engineering methods one of the most pressing areas for RL research (p. 477–478).
- *Closing.* The authors note that job displacement is a threat already here, yet there are reasons to believe benefits can outweigh disruption. Developers should follow best practices from similar technologies while extending them (p. 478).

### Bibliographical and historical remarks (p. 478–480)
These mostly give sources, plus a few statements about what has not yet been done. GVFs were first explicitly identified by Sutton and colleagues, and multi-headed RL was first shown by Jaderberg et al. (2017). Options come from Sutton, Precup and Singh (1999) and earlier work, but early works did not treat off-policy learning with function approximation. The authors say that using GVFs to implement option models has not previously been described, and that options for the average-reward setting have not yet been developed in the literature. PSRs, OOMs and Sequential Systems are credited to Littman et al., Jaeger and Thon. Skinner's shaping differs from "potential-based shaping" (Ng et al., 1999), which Wiewiora (2003) showed equivalent to initial value approximation as in (17.11). Further references cover curiosity, empowerment and intrinsic motivation (p. 478–480).

## Toy example (ours, not from the text)
A chain of states $s_0\to s_1\to s_2\to s_3$. Option $\omega$ always moves right and terminates exactly on reaching $s_3$ ($\gamma_\omega=1$ at $s_0,s_1,s_2$, and $0$ at $s_3$). Each step gives reward 1, and $\gamma=0.9$. Here $\tau=3$ with probability 1.

- Reward part (17.2): $r(s_0,\omega)=R_1+\gamma R_2+\gamma^2R_3=1+0.9+0.81=2.71$.
- Transition part (17.3): only $k=3$, $s'=s_3$ contributes, so $p(s_3|s_0,\omega)=\gamma^3\cdot 1=0.729$. All other $s'$ get 0. The total is $0.729\ne1$, as the text warns.
- Bellman (17.4) with only this option, $\pi(\omega|s_0)=1$, and assumed $v(s_3)=10$: $v(s_0)=2.71+0.729\times10=2.71+7.29=10.00$.
- Check: with reward 1 forever and $\gamma=0.9$ the true value is $1/(1-0.9)=10$, which matches. One option backup jumped three steps.

## Concepts
- [[general-value-function]] (new) — prediction of the discounted sum of any cumulant under a policy and termination function, as in (17.1) (p. 459)
- [[cumulant]] (new) — the signal $C_t$ accumulated in a GVF in place of reward (p. 459)
- [[auxiliary-task]] (new) — extra prediction or control task that may speed the main task via shared representations (p. 460)
- [[option]] (new) — pair of policy and termination function acting as a temporally extended action (p. 461)
- [[option-model]] (new) — discounted expected reward (17.2) plus discounted termination-state weights (17.3) (p. 462)
- [[hierarchical-policy]] (new) — policy that chooses options, which run until termination (p. 462)
- [[history-and-markov-state]] (new) — state as a function of the action–observation history. Markov if equal states imply equal test probabilities (17.6) (p. 465)
- [[state-update-function]] (new) — recursive map $S_{t+1}=u(S_t,A_t,O_{t+1})$ (17.7) (p. 465)
- [[belief-state]] (new) — POMDP distribution over latent states given history, updated by Bayes' rule (17.9–17.10) (p. 467)
- [[predictive-state-representation]] (new) — state as probabilities of core future tests (p. 467)
- [[reward-shaping]] (new) — Skinner-style gradual change of reward or task as learning proceeds (p. 470)
- [[intrinsic-reward]] (new) — reward from internal factors such as learning progress, implementing curiosity (p. 474)
- [[inverse reinforcement learning (inverse optimal control)]] — recover a reward that makes an expert's behavior optimal. This is not exactly possible, since many rewards fit one policy (p. 470)
- [[state]] — here a function of history, not given by the environment (p. 465)
- [[policy]], [[model-based vs model-free RL]], [[Bellman equation / value function]], [[exploration vs exploitation]] — used throughout, extended to options and GVFs (p. 461–463)
- [[stability]] — adaptive-control theory on stability and convergence is cited as the model for RL safety (p. 477)

## Canonical instances
- [[blink-reflex-pavlovian-control]] — prediction of an eye poke triggers a built-in blink (p. 460)
- [[vacuum-robot-battery-prediction]] — a learned battery prediction triggers return to the charger (p. 461)
- [[multi-head-network-auxiliary-tasks]] — shared body, separate heads for main and auxiliary tasks (p. 460)
- [[pomdp-belief-state]] — the belief vector as a Markov state (p. 467)
- [[echo-state-network-state]] — near-arbitrary history information used as state (p. 468)
- [[constant-reward-ambiguity]] — all policies are optimal for a constant reward, so inverse RL is ambiguous (p. 470)
- [[taste-reward-evolution]] — evolution designs the reward signal (taste seeking) to compensate for the animal's limits (p. 471)
- [[sorcerers-apprentice-monkeys-paw]] — literary cases of getting what you asked for, not what you wanted (p. 477)

## Bridges (candidates)
- [structural-analogy] state-update function $u$ and belief update (17.10) ↔ control theory: observer / Bayesian state estimator — both recursively fold new measurements into a compact state summary.
- [structural-analogy] inverse RL ↔ control theory: inverse optimal control — both infer the objective that makes observed behavior optimal.
- [structural-analogy] options with termination functions ↔ control theory: hierarchical or supervisory control — higher-level choices select lower-level policies that run until a condition ends them.
- [metaphor] bilevel reward optimization (RL inside an evolution-like outer loop) ↔ biology: evolution of reward systems — the text itself draws this analogy.
- [structural-analogy] RL safety via modelling, testing and stability theory ↔ control theory: robustness and adaptive-control guarantees (p. 477).

## Questions this raises
- How should an agent choose which cumulants, policies and terminations to learn, and how would it judge which predictions are useful?
- If one-step prediction errors compound, what objective should be used to learn an approximate state-update function?
- When is it right for an agent's reward to differ from the designer's goal, and how can this be tested?
- Which control-engineering stability results carry over to RL agents that learn online with function approximation?

## Exercises worth doing
- Ex. 17.1 (p. 464) — derive the average-reward versions of the hierarchical Bellman equation (17.4) and of the two option-model parts (17.2)–(17.3). This forces you to see what discounting did in those equations — difficulty: hard

## Reading notes
- Printed page = pdf page − 22 (pdf 481–502 = printed 459–480). Cited pages use printed numbers.
- Page images were provided only for printed pp. 462, 463, 465, 466, 467. Other pages were read from the text layer. Equations on those pages (17.1, 17.11) were not checked against an image.
- On p. 468 the text layer prints the $k$th-order history as ending in $A_{t-k}$. I did not check this against an image, so I describe it in words ("last $k$ observations and actions").
- The text layer has the typo "suppose we wants" (p. 470); I did not alter any content because of it.
- Ring's work on GVFs is cited as "in preparation" (p. 459, 478).
- Footnote 1 (p. 473) is the authors' own opinion on DQN and representation learning; it is reported as such above.
- The title page and edition details are not part of these pages. The citation comes from the unit metadata.
