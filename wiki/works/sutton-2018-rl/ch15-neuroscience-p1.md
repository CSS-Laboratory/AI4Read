---
id: sutton-2018-rl/ch15-neuroscience-p1
work: sutton-2018-rl
unit: "Chapter 15 — Neuroscience (part 1 of 2: intro and §§15.1–15.7)"
pages: 377–397
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Neuroscience (part 1/2): dopamine as a TD error, and a neural actor–critic

## L0 — One line
The phasic (burst-like) activity of dopamine neurons in mammals behaves like the TD error of reinforcement learning, and this suggests the brain may implement something like an actor–critic algorithm.

## L1 — The gist (≤ 120 words)
The chapter asks how reinforcement learning (RL) ideas relate to the brain. Its main answer is the reward prediction error hypothesis, which proposes that phasic dopamine activity delivers a TD (temporal-difference) error, not reward itself. The evidence comes from monkey recordings, where responses move from the reward to the earliest predictor and dip when a predicted reward is omitted. Optogenetic experiments (using light to control neurons) show that dopamine bursts act as reinforcement signals. The match is imperfect, for example when reward comes early. The unit also presents a hypothesised neural actor–critic in the striatum (a basal ganglia input area), with dopamine as the shared TD error. Notably, TD learning was developed without any knowledge of dopamine neurons.

**Prerequisites:** TD(0) and the TD error; value functions and policy evaluation; actor–critic idea (Ch. 13.5); the complete serial compound (CSC) stimulus representation (Ch. 14.2). No neuroscience is assumed.

## L2 — Key ideas
- **Two aims.** The chapter explains parallels between RL and reward learning in animal brains, and shows brain ideas (e.g. the eligibility trace, an RL mechanism that began as a conjectured property of synapses) behind RL. The authors say they are not neuroscientists and do not do justice to alternative hypotheses (pp. 377–378).
- **Signals must be separated.** A reward signal, a reinforcement signal (what directs learning), a value and a prediction error are different things. In TD methods the reinforcement signal is the TD error, not $R_t$ (pp. 380–381).
- **Reward prediction error hypothesis.** The hypothesis proposes that one function of phasic dopamine activity is to deliver an error between old and new estimates of expected future reward. If it is correct, phasic responses signal that error, not reward itself (pp. 381, 384).
- **Evidence from monkeys.** Responses of many neurons move from reward to earlier predictors and vanish at later ones. In many neurons they fall below baseline when an expected reward is omitted. The shift to earlier predictors is called a hallmark of TD learning, and the omission dip is another property shared with TD learning (pp. 388–390).
- **Idealised derivation.** In an idealised tabular (one value per state), undiscounted policy-evaluation task, $\delta$ shows the key features of the dopamine responses (pp. 391–393).
- **Imperfect fit.** Early reward is a known mismatch, which various researchers tackle with other representations and parameters. The authors say such findings refine the hypothesis without refuting its core claim, while other discrepancies are not so easily accommodated (pp. 393–394).
- **Wide broadcast.** Dopamine axons are huge and make about 500,000 contacts each. This suits a scalar reinforcement signal, though subpopulations may differ (p. 385).
- **Neural actor–critic.** Dorsal striatum is proposed as actor, ventral striatum as critic's value learner, dopamine as the TD error to both (pp. 395–397).

## L3 — Walkthrough

### Introduction (pp. 377–378)
The chapter's main objective is to explain parallels between RL algorithms and nervous systems (p. 377). Its most striking point of contact is dopamine, which appears to convey TD errors to structures where learning and decision making take place (p. 377). A second objective is to show brain ideas that shaped RL; the eligibility trace began as a conjectured property of synapses (p. 377). The authors say they are not neuroscientists, do not name most brain structures, and do not treat alternative hypotheses fairly (p. 378). They assume RL knowledge but no neuroscience (p. 378).

### 15.1 Neuroscience basics (pp. 378–379)
- **Neuron:** a cell with a cell body, dendrites (receive input) and one axon (carries output). Output is a sequence of action potentials ("spikes"). A neuron "fires" when it spikes. Models often use a real-valued firing rate, the average number of spikes per time unit (p. 378).
- **Axonal arbor:** the branching of an axon. A spike lights up all outgoing branches (propagation to a branch can sometimes fail), so a neuron with a big arbor can influence many targets (p. 378).
- **Synapse:** mediates communication from the presynaptic neuron's axon to the postsynaptic neuron. It usually releases a neurotransmitter that crosses the synaptic cleft and binds to receptors. One transmitter can act through several receptor types; dopamine has at least five (p. 379).
- **Activity types:** background activity (not driven by task-related input), phasic activity (bursts, usually caused by synaptic input), tonic activity (slow, often graded) (p. 379).
- **Synaptic efficacy:** the strength of a synapse's influence. Changes in efficacy are **synaptic plasticity**, a primary mechanism of learning. Learning-algorithm weights correspond to synaptic efficacies (p. 379).
- **Neuromodulator:** a transmitter with effects beyond direct fast excitation or inhibition. A neuromodulatory system can distribute something like a scalar reinforcement signal to many sites (p. 379).

### 15.2 Reward, reinforcement, values, prediction errors (pp. 380–381)
- A signal label (e.g. "reinforcement signal") names a term in RL theory. Applied to a neural signal, it means the signal behaves like, and is conjectured to function like, that term (p. 380).
- Interpretation is hard. Reward-related activity is in nearly every brain part, and different reward-related signals tend to be highly correlated (p. 380).
- **Reward signal $R_t$:** it defines the RL problem. A single master reward signal probably does not exist in the brain. $R_t$ is better seen as an abstraction summarising many neural signals (p. 380).
- **Reinforcement signal:** it directs changes to policy, value estimates or models. For TD methods it is the TD error (p. 380):
$$\delta_{t-1} = R_t + \gamma V(S_t) - V(S_{t-1}).$$
- Footnote: in the book's notation $\delta_t = R_{t+1}+\gamma V(S_{t+1})-V(S_t)$ is not available until $t+1$. The error available at $t$ is $\delta_{t-1}$. Time steps are thought of as tiny, so this shift is unimportant (pp. 380–381).
- **Values** $V$, $Q$ predict total future reward (p. 381).
- **Reward prediction errors (RPEs)** are discrepancies between expected and received reward. TD errors are special RPEs, comparing current and earlier long-term expectations. Neuroscientists generally (not always) mean TD RPEs. This chapter uses action-free TD errors, without ruling out action-dependent links (p. 381).
- Evidence suggests dopamine signals RPEs, and that phasic dopamine activity conveys TD errors (p. 381).

### 15.3 The reward prediction error hypothesis (pp. 381–383)
- **Statement:** one function of phasic activity of dopamine neurons in mammals is to deliver an error between an old and a new estimate of expected future reward to target areas. Montague, Dayan and Sejnowski (1996) first stated it explicitly. It came from Wolfram Schultz's experiments in the 1980s–early 1990s (pp. 381–382).
- **Setup by Montague et al.** (p. 382): they compared the TD model of classical conditioning (semi-gradient TD($\lambda$), linear function approximation) with recorded dopamine activity.
  1. Firing rates cannot be negative, so the quantity matched to dopamine activity is $\delta_{t-1}+b_t$, with $b_t$ the background firing rate. A negative TD error is a drop below background.
  2. A CSC representation: a sequence of short internal signals continues until US onset. Each time step after a stimulus is then a distinct state, so the state-dependent TD error can be sensitive to timing.
- **Four parallels** (p. 382): (1) phasic response only when a rewarding event is unpredicted; (2) early in learning, neutral cues cause no response, later they do; (3) if an earlier cue predicts an already-predictive cue, the response shifts to the earlier cue and stops for the later one; (4) if the predicted reward is omitted, the response falls below baseline shortly after the expected time.
- Not every neuron showed all of these, but most matched TD errors, which gives strong support. Some predictions do not match, and input representation is critical, especially for timing (p. 383).

*Intuition note:* If the hypothesis is right, dopamine bursts report "better or worse than expected", not "reward". A fully expected reward produces (almost) no surprise, so the TD error is silent and fewer neurons respond (p. 393).

### 15.4 Dopamine (pp. 383–387)
- **Basics:** dopamine neurons lie mainly in the SNpc and VTA (midbrain). Dopamine is involved in motivation, learning, action selection, addiction, schizophrenia and Parkinson's disease. Its role in aversive situations is controversial, and it can function differently in non-mammals (p. 383).
- **Traditional view:** dopamine neurons broadcast a reward signal. This came from Olds and Milner (1954), where electrical stimulation of rat brain regions acted as a very powerful reward. The effective sites excited dopamine pathways (p. 383).
- **If the hypothesis is right,** this view is not entirely correct. Phasic responses correspond to $\delta_{t-1}$, not $R_t$ (p. 384). The term $\gamma V(S_t)-V(S_{t-1})$ is the "higher-order reinforcement part", so $\delta$ can be silent when reward ($R_t\ne 0$) is fully predicted (p. 384).
- Olds and Milner's paper is mainly about reinforcement in instrumental conditioning: rats learned to press a lever for stimulation (p. 384).
- **Optogenetics** (light-sensitive proteins let laser flashes switch chosen neuron types on or off, at millisecond scale) (p. 384):
  - Tsai et al. (2009): phasic activation of dopamine neurons in mice conditioned a preference for the stimulated chamber side.
  - Steinberg et al. (2013): artificial bursts when rewards were expected but omitted sustained responding in extinction trials and enabled learning in blocking (Section 14.2.1).
  - Fruit flies (Claridge-Chang et al. 2009): bursts act like foot shock, reinforcing avoidance, at least for the neurons activated (pp. 384–385).
- These experiments did not show that activity is specifically TD-error-like. They show it acts like $\delta$ (or $-\delta$ in flies) as the reinforcement signal for prediction and control (p. 385).
- **Broadcast anatomy:** dopamine axons have 100–1,000 times more release sites than typical axons. Each makes roughly 500,000 synaptic contacts (p. 385).
- A scalar signal would suggest near-synchronous activity of all dopamine neurons. Modern evidence points to a more complicated picture, with subpopulations responding differently. Vector-valued RPEs make sense when decisions decompose into sub-decisions, or for structural credit assignment, i.e. sharing credit among many structures (p. 385).
- **Striatum:** most dopamine axons target frontal cortex and basal ganglia. The authors focus on the basal ganglia. Cortex gives input to the striatum, its main input structure, onto medium spiny neurons. Dorsal striatum is primarily implicated in action selection. Ventral striatum is thought critical for reward processing, including affective value (pp. 385–386).
- **Spine arrangement** (Fig. 15.1): cortical axons contact spine tips (releasing glutamate). Dopamine axons contact spine stems. This brings together presynaptic cortical activity, postsynaptic striatal activity and dopamine. Evidence is mounting that corticostriatal synaptic changes depend critically on appropriately timed dopamine (pp. 386–387).

### 15.5 Experimental support (pp. 387–390)
- Dopamine neurons respond to intense, novel or unexpected stimuli, but little of their activity relates to movement itself (p. 387).
- **Romo and Schultz (1990)** recorded dopamine neurons and muscle activity in two monkeys reaching for food (p. 387).
  - Self-initiated task: many neurons responded phasically when the monkey first touched food. They did not respond to touching the bare wire or to an empty bin.
  - Stimulus-triggered task: after training, neurons responded to the sight and sound of the opening cover, not to touching the food. Most did not respond to the opening outside the task.
  - Conclusion: they signal an expectation of reward, not movement or stimulus properties (pp. 387–388).
- **Ljungberg, Apicella and Schultz (1992):** lever press after a light "trigger cue" yields apple juice. Neurons first responded to the juice, then lost this response and responded to the light. Lever pressing became faster while fewer neurons responded to the trigger (Fig. 15.2, top and middle) (p. 388).
- **Schultz, Apicella and Ljungberg (1993):** an "instruction cue" 1 s before the trigger indicated the correct lever. Responses went almost exclusively to the instruction cue, and fewer neurons responded once learned (Fig. 15.2, bottom). Shifting to earlier predictors while losing later ones is a hallmark of TD learning (pp. 388–389).
- **Omission** (Fig. 15.3): when the monkey pressed the wrong lever and got no reward, many neurons fell below baseline shortly after the usual reward time, with no external cue marking it. So the monkeys kept track of reward timing internally (pp. 389–390).
- Schultz's group concluded that dopamine neurons respond to unpredicted rewards and to the earliest predictors. Activity falls below baseline if a reward or predictor is omitted at its expected time. RL researchers recognised the similarity to TD errors (p. 390).

### 15.6 TD error/dopamine correspondence (pp. 390–394)
**Idealised setting** (pp. 390–391):
- Policy evaluation: actions are already learned, and only $V$ for the fixed policy is learned.
- Each trial is an episode with the same sequence of distinct states. Returns are confined to a trial.
- CSC representation, so the case is tabular. TD(0) with a lookup table, $V=0$ initially, a deterministic task and $\gamma\approx 1$ (ignored).
- Reward is zero until the rewarding state, where it equals $R^\star>0$. In this undiscounted case, with predictions confined to a trial, the correct prediction for every reward-predicting state is $R^\star$ (p. 391).

**Terms** (p. 392): the *earliest* reward-predicting state is the first state in a trial that reliably predicts its reward. The *latest* is the state just before the rewarding state. The rewarding state itself does not predict this trial's return, which is zero for later trials.

**Derivation by cases** (Fig. 15.4; pp. 392–393):
1. *Early in learning*, all $V=0$:
$$\delta_{t-1}=R_t+V_t-V_{t-1}=R_t+0-0=R_t,$$
which is $0$ until it equals $R^\star$ at the rewarding state. This matches a dopamine response to unpredicted reward (p. 392).
2. TD(0) updates at each transition spread value backwards from the rewarding state until all reward-predicting states have $V=R^\star$. States before the earliest predictor stay low (p. 392).
3. *Learning complete*, transition between two predictors: $\delta_{t-1}=0+R^\star-R^\star=0$. Latest predictor to rewarding state: $\delta_{t-1}=R^\star+0-R^\star=0$ (p. 392).
4. Transition into the earliest predictor, from a state of value 0: $\delta_{t-1}=0+R^\star-0=R^\star>0$ (p. 392).
5. *Reward omitted after learning:* $\delta_{t-1}=0+0-R^\star=-R^\star$ at the usual reward time (p. 393).

These match: a persisting response to the earliest predictor, few responses to a fully predicted reward, and a dip below baseline on omission (p. 393).

*Intuition note:* The error is "what I now believe minus what I believed a step ago, plus reward". In the idealised task, once values are right, the only surprise left is the moment the first predictor appears.

**Earliest predictor, in general** (p. 393): it is an unpredicted predictor of reward, and there can be many. States before it are mostly followed by non-predictive states, so their values stay low. This might explain why dopamine responses shrink to even the earliest cue with overtraining. A new task would bring TD errors back, as observed.

**Discrepancy: early reward** (pp. 393–394):
- If reward comes later than expected, both TD errors and dopamine neurons give a positive response.
- If it comes earlier, dopamine neurons respond, as TD predicts. But at the originally expected time the TD error (with CSC) is negative, while dopamine activity does not drop below baseline (Hollerman and Schultz, 1998).
- Proposed fixes: reward cancels internal signals started by earlier stimuli (Suri and Schultz, 1999); representations from statistical modelling in sensory cortex (Daw et al., 2006); microstimulus representation (Ludvig, Sutton and Kehoe, 2008); prolonged eligibility traces (Pan et al., 2005). Fine details depend on interactions of eligibility traces, discounting and stimulus representation (p. 394).
- Such findings refine the hypothesis without refuting its core claim. Other discrepancies are not so easily accommodated, and more are likely to appear. The hypothesis has been an effective catalyst for experiments (p. 394).
- TD learning was developed with no knowledge of dopamine neurons. The authors say this unplanned, imperfect correspondence suggests the parallel captures something significant (p. 394).
- The evidence suggests that the brain might implement something like actor–critic, though other algorithms are plausible too (p. 395).

### 15.7 Neural actor–critic (pp. 395–397)
- **Algorithm:** the actor learns the policy. The critic learns the state-value function of the actor's current policy by TD, and sends $\delta$ to the actor. Positive $\delta$ means the action led to a better-than-expected state, negative means worse. The actor updates its policy from these critiques (p. 395).
- **Two reasons to suspect a brain implementation** (p. 395):
  1. Two components, and the striatum has two subdivisions, dorsal and ventral, both critical for reward learning. They may function roughly as actor and critic.
  2. $\delta$ is the reinforcement signal for both, with a different influence on each. This fits dopamine axons targeting both subdivisions, dopamine appearing to be critical for modulating plasticity in both, and the fact that a neuromodulator's action depends on the target.
- **ANN version** (Fig. 15.5a; pp. 396–397), following Barto, Sutton and Anderson (1983):
  - The critic is one unit $V$ plus a TD component that combines $V$ with reward and previous values.
  - The actor has $k$ units $A_i$. Their outputs form a $k$-dimensional action vector.
  - Both receive features $x_1,\dots,x_n$. Each connection has a weight (a synaptic efficacy). Critic weights parameterise $V$, actor weights parameterise the policy.
  - The actor has no direct access to reward, and the critic has none to the action (Fig. 15.5 caption, p. 396).
  - $\delta$ is the reinforcement signal for all weights in both networks. Together with the hypothesis and dopamine's wide arbors, this suggests the idea "may not be too farfetched" (p. 397).
- **Brain map** (Takahashi, Schoenbaum and Niv, 2008; Fig. 15.5b; p. 397):
  - The actor and the critic's value-learning part sit in the dorsal and ventral striatum respectively.
  - The ventral striatum sends value information to VTA and SNpc, where dopamine neurons combine it with reward information to produce TD-error-like activity. How they compute this is not yet understood.
  - The dopamine axons contact the spines of medium spiny neurons in both subdivisions. Corticostriatal synapse changes are governed by learning rules that depend critically on dopamine.
- **Implication (of the hypothesis in Fig. 15.5b):** the dopamine signal is not a master reward signal like $R_t$. One should not necessarily be able to record a signal like $R_t$ in any single neuron (p. 397).

*Intuition note:* Both actor and critic learn from the same "better or worse than expected" message. One broadcast chemical can serve both, since each target reacts according to its own circuitry.

## Toy example (ours, not from the text)
Chain of states: $p$ (a state before the earliest predictor), $s_0$ (earliest predictor), $s_1$ (latest predictor), then rewarding state $s_2$ with $R^\star=1$. Undiscounted TD(0), $\alpha=1$ for easy arithmetic, all $V=0$. Following the book's assumption, $V(p)$ stays 0 (not a reliable predictor). $V(s_2)=0$. Update: $V(S_{t-1})\leftarrow V(S_{t-1})+\delta_{t-1}$.

| Trial | Transition | $\delta=R+V(\text{next})-V(\text{prev})$ | New $V$ |
|---|---|---|---|
| 1 | $s_1\to s_2$ | $1+0-0=1$ | $V(s_1)=1$ |
| 2 | $s_0\to s_1$ | $0+1-0=1$ | $V(s_0)=1$ |
| 2 | $s_1\to s_2$ | $1+0-1=0$ | unchanged |
| 3 | $p\to s_0$ | $0+1-0=1$ | $V(p)$ held at 0 |
| 3 | $s_0\to s_1$ | $0+1-1=0$ | |
| 3 | $s_1\to s_2$ | $1+0-1=0$ | |
| Omission | $s_1\to s_2$, $R=0$ | $0+0-1=-1$ | |

(In trial 1, $s_0\to s_1$ also occurs, with $\delta=0+0-0=0$.) The error starts at the reward, moves to the earliest predictor ($\delta=1$ on $p\to s_0$), is 0 at the fully predicted reward, and is $-1$ when the reward is omitted. This is the pattern of Figure 15.4.

## Concepts
- [[temporal-difference-learning-reward-prediction-error]] — here, the TD error $\delta_{t-1}=R_t+\gamma V(S_t)-V(S_{t-1})$, a special RPE comparing old and new long-term reward expectations (pp. 380–381)
- [[reward-prediction-error-hypothesis]] (new) — phasic dopamine activity delivers an old-versus-new expected-reward error to target areas (p. 381)
- [[reinforcement-signal]] (new) — the signal that directs learning changes; for TD methods it is $\delta$, which differs from the reward signal $R_t$ (p. 380)
- [[policy]] — the rule being learned by the actor; its parameters correspond to actor synaptic weights (p. 397)
- [[synaptic-plasticity]] (new) — change in synaptic efficacy; it corresponds to weights adjusted by learning algorithms (p. 379)
- [[neuromodulator]] (new) — a transmitter such as dopamine acting beyond fast excitation/inhibition, able to broadcast a scalar-like signal (p. 379)
- [[complete-serial-compound-representation]] (new) — one distinct internal state per time step after a stimulus, which lets TD errors track timing (p. 382)
- [[actor-critic]] (new) — actor learns the policy, critic learns values by TD and sends $\delta$ to the actor (p. 395)
- [[credit-assignment]] (new) — here the structural version: sharing credit or blame among the structures that produced a decision (p. 385)
- [[optogenetics]] (new) — using light to activate or silence selected neuron types at millisecond scale (p. 384)

## Canonical instances
- [[schultz-monkey-instruction-trigger-task]] — dopamine responses shift from reward to trigger cue to earlier instruction cue; dip on omission (pp. 388–390)
- [[romo-schultz-food-bin-task]] — dopamine neurons respond to food touch, then to the predictive bin-opening cue (p. 387)
- [[olds-milner-self-stimulation]] — electrical brain stimulation reinforces lever pressing (pp. 383–384)
- [[steinberg-optogenetic-blocking]] — artificial dopamine bursts at omitted-reward times sustain responding and unblock learning (p. 384)
- [[td-error-idealised-trial]] — $\delta$ over trials: early learning, complete, omitted (Fig. 15.4; pp. 391–393)
- [[early-reward-mismatch]] — dopamine neurons do not dip at the original reward time, unlike CSC TD error (pp. 393–394)
- [[takahashi-neural-actor-critic]] — actor in dorsal, critic in ventral striatum, dopamine as $\delta$ (pp. 396–397)

## Bridges (candidates)
- [structural-analogy] TD error as dopamine burst ↔ control-theory: error signal driving a controller's adaptation — both use a deviation from expectation to correct future behaviour.
- [structural-analogy] Dopamine broadcasting one scalar to many synapses ↔ control-theory: a global feedback signal shared by many adjustable parameters.
- [structural-analogy] Actor–critic split ↔ control-theory: a controller plus a separate estimator of performance. Both act in one loop but have different learning roles.

## Questions this raises
- How do dopamine neurons compute a TD error from value and reward inputs? The text says this is not yet understood (p. 397).
- If different dopamine subpopulations send different RPEs, how are credit and blame divided among brain structures? (p. 385).
- Which stimulus representations and trace parameters best explain the early-reward result and the other discrepancies? (p. 394).
- What learning rules at corticostriatal synapses implement the actor and critic updates? (p. 395 postpones this to §15.8, in part 2).

## Reading notes
- This part begins at the start of Chapter 15 (printed p. 377) and ends at the foot of p. 397 with the sentence ending "…any single neuron." The source notes say the split is at a section boundary; these pages do not show how §15.7 ends. Pages 395 and 397 refer ahead to §15.8 for the actor and critic learning rules.
- Page offset: printed = pdf − 22.
- The text layer drops $\gamma$, minus signs, subscripts and $\delta$ in several equations (pp. 380–381 footnote, 382, 384, 391–393). I read them from the images of pp. 391–392 and from the logic of the derivation. No image was supplied for p. 393, so the omission case $0+0-R^\star=-R^\star$ is reconstructed from the surrounding derivation and Fig. 15.4.
- Fig. 15.1 caption shows the typo "D1 an D2" (image confirms).
- No exercises appear in this part.
