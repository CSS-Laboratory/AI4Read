---
id: sutton-2018-rl/ch14-psychology
work: sutton-2018-rl
unit: "Chapter 14 — Psychology"
pages: 341–376
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
# Psychology (Sutton & Barto, Ch. 14)

## L0 — One line
Reinforcement-learning ideas (prediction with TD error, trial-and-error control, eligibility traces, environment models) correspond to several findings and theories of animal-learning psychology, and the TD model of classical conditioning is one instance where the algorithm accounts for some details of animal data.

## L1 — The gist (≤ 120 words)
Chapter 14 asks how the book's prediction and control algorithms relate to what psychologists found about animal learning. Prediction corresponds roughly to classical conditioning; control corresponds roughly to instrumental conditioning. The Rescorla–Wagner model is an error-correcting (LMS) rule that explains blocking. The TD model adds time, eligibility traces and bootstrapping, and so covers timing effects and higher-order conditioning. Eligibility traces and TD-learned values match older ideas about delayed reinforcement. Environment models correspond to cognitive maps. Model-free versus model-based learning corresponds to habitual versus goal-directed behavior. The authors stress that RL is an idealized engineering framework, not a detailed model of animals.

**Prerequisites:** TD error and TD(λ) with eligibility traces; linear function approximation (w·x); model-free vs model-based RL and planning; actor–critic; LMS (supervised error correction).

## L2 — Key ideas
- Prediction algorithms correspond to classical (Pavlovian) conditioning, and control algorithms to instrumental (operant) conditioning. The authors call this a convenient first approximation, since the two kinds of conditioning interact (pp. 342–343).
- Blocking (a new CS added to an already-trained CS gets little conditioning) challenged the idea that temporal contiguity of CS and US is enough for conditioning. The Rescorla–Wagner model explains it with a shared prediction error: only surprising events change associative strengths (pp. 345–348).
- Rescorla–Wagner is essentially the LMS (Widrow–Hoff) supervised rule. It is a trial-level model with no within-trial time and no higher-order conditioning (pp. 348–349).
- The TD model (14.4–14.6) works in real time, with eligibility traces and discounting. Through bootstrapping it yields second-order conditioning (a conditioned CS acts as a US for a new stimulus) and the new prediction that an earlier CS (conditioned stimulus) overrides blocking, which was later confirmed in rabbits. It also reproduces ISI dependence (conditioning depends on the CS–US onset gap) (pp. 349–355).
- The TD model's predictions depend strongly on the stimulus representation (CSC, microstimuli, presence: three ways of coding a stimulus as features over time). The model suggests a normative view: the nervous system tries to form accurate long-term predictions (pp. 350–357).
- Trial-and-error learning (Law of Effect) is selectional and associative, which is the "search plus memory" of RL. Shaping is a useful training idea for RL agents too (pp. 358–360).
- Delayed reinforcement is addressed by eligibility traces (like Hull's decaying stimulus traces) and TD-learned values (like conditioned reinforcement). In actor–critic, the TD error is the actor's conditioned reinforcement (pp. 361–363).
- Cognitive maps correspond to environment models, learnable without reward. Outcome-devaluation and overtraining experiments give evidence about whether behavior is goal-directed (model-based) or habitual (model-free). One proposal (Daw, Niv & Dayan) is that the more trustworthy process wins (pp. 363–368).
- RL vocabulary differs from psychology's: reinforcement, reward, action, and control all have different meanings (pp. 373–376).

## L3 — Walkthrough

### Chapter introduction (pp. 341–342)
- The goals are to show how RL ideas correspond to animal-learning findings, and how RL is influencing the study of animal learning (p. 341).
- RL here is an idealized framework for solving computational problems, not a detailed model of animals. Some correspondences connect ideas that arose independently, and the authors think these expose computational principles (p. 341).
- The chapter concentrates on laboratory theories about rats, pigeons and rabbits. The authors say these experiments found elemental learning principles that should not be neglected in artificial systems (p. 342).

### 14.1 Prediction and Control (pp. 342–343)
- The book's algorithms fall into prediction and control. These correspond to classical (Pavlovian) and instrumental (operant) conditioning (p. 342).
- **Prediction:** these algorithms estimate quantities that depend on how the environment is expected to unfold. They are policy-evaluation algorithms, but can predict any feature, not just reward. The link to classical conditioning is that both predict upcoming stimuli, rewarding or not (p. 342).
- **Instrumental conditioning:** the reinforcing stimulus is *contingent* on behavior; in classical conditioning it is not. This resembles Thorndike's Law of Effect, and control is at its core, matching policy-improvement algorithms (pp. 342–343).
- Caveat: classical conditioning also involves action ("Pavlovian control"), and both kinds of learning are probably engaged in most experiments (p. 343).
- Footnote: "control" means something different in animal learning theory (the environment controls the agent) (p. 342).
- *Reinforcement* in psychology covers learning in both kinds of conditioning. It originally meant strengthening, and is often extended to weakening. The cause of the change is the *reinforcer* (p. 343).

### 14.2 Classical Conditioning (pp. 343–344)
- Pavlov found that an inborn response can be triggered by an unrelated stimulus that is presented shortly before the trigger. His dogs salivated to a metronome sound that preceded food (p. 343).
- **Pavlov's view:** the normal animal must respond not only to stimuli that themselves bring benefit or harm, but also to stimuli that only *signal* the approach of such stimuli (p. 343).
- Terms: unconditioned stimulus (US) and response (UR) are the inborn trigger and reaction. A neutral stimulus that predicts the US becomes a conditioned stimulus (CS) and evokes a conditioned response (CR). The US is the reinforcer (p. 344).
- **Delay conditioning:** the CS lasts through the interstimulus interval (ISI, CS onset to US onset). **Trace conditioning:** the US starts after the CS ends; the gap is the trace interval (p. 344).
- Example: in rabbit nictitating-membrane conditioning, a tone predicts an air puff. The CR starts before the puff and is eventually timed to peak closure when the puff is likely, which protects better than reacting to the puff (p. 344).

#### 14.2.1 Blocking and Higher-order Conditioning (pp. 345–346)
- **Blocking:** an animal fails to learn a CR to a new CS that is presented together with an already-conditioned CS. Three stages: (1) tone → puff; (2) tone+light → puff; (3) light alone gives very few or no CRs (p. 345).
- A control group with no prior tone training learns to the light normally (footnote 2, p. 345).
- Blocking challenged the idea that temporal contiguity of CS and US is necessary and sufficient for conditioning (p. 345).
- **Higher-order conditioning:** a previously conditioned CS acts as a US for a new neutral stimulus. In Pavlov's second-order case, a black square was followed by the metronome, with no food. After ten trials the dog salivated to the square (p. 345).
- It is hard to show beyond second order, because the higher-order reinforcer loses value when not followed by the original US. Intermixing first-order trials or a general energizing stimulus can help (p. 345).
- **Higher-order instrumental conditioning:** a stimulus that predicts primary reinforcement (value built in by evolution) becomes a secondary or conditioned reinforcer. Money is the example (p. 346).
- In actor–critic methods, the critic's TD value estimates give conditioned reinforcement to the actor. This helps with credit assignment when the primary reward is delayed (p. 346).

#### 14.2.2 The Rescorla–Wagner Model (pp. 346–349)
- **Core idea:** an animal learns only when events violate its expectations, i.e. when it is surprised (no conscious expectation implied) (p. 346).
- **Original form.** For a compound CS AX followed by a US Y, with $V$ the associative strength (how strongly a stimulus predicts the US) (p. 347):
$$\Delta V_A=\alpha_{AY}\,(R_Y-V_{AX}),\qquad \Delta V_X=\alpha_{XY}\,(R_Y-V_{AX})$$
  Here $\alpha_{AY},\alpha_{XY}$ are step sizes depending on the CS components and the US. $R_Y$ is the asymptotic strength the US can support. The key assumption is $V_{AX}=V_A+V_X$. The changed strengths start the next trial (p. 347).
- Rescorla and Wagner left the response-generation mechanism open. They assumed only that larger $V$ gives stronger or more likely CRs, and negative $V$ gives no CR (p. 347).
- **Blocking explained.** While $V_{AX}<R_Y$ the error is positive, so strengths grow until $V_{AX}=R_Y$. If a new component is added to an already-conditioned compound, the error is already zero or small, so the new component gains little (p. 347).
- **RL notation.** A trial type (state) $s$ has a feature vector $\mathbf{x}(s)=(x_1(s),\dots,x_d(s))^\top$, with $x_i(s)=1$ if CS$_i$ is present and 0 otherwise. Both $\mathbf{x}(s)$ and the weight vector $\mathbf{w}$ have shape $d\times1$ (pp. 347–348).
$$\hat v(s,\mathbf w)=\mathbf w^\top\mathbf x(s)\tag{14.1}$$
$$\mathbf w_{t+1}=\mathbf w_t+\alpha\,\delta_t\,\mathbf x(S_t)\tag{14.2}$$
$$\delta_t=R_t-\hat v(S_t,\mathbf w_t)\tag{14.3}$$
- Here $t$ numbers whole trials. $\hat v$ is the US prediction, $R_t$ is the US magnitude, and $\delta_t$ is the prediction error, which one "can think of" as a measure of surprise. Only components present on a trial change, because of the factor $\mathbf x(S_t)$ (p. 348).
- **Relation to LMS.** The model is an error-correction supervised rule, essentially the LMS (Widrow–Hoff) rule. LMS differs in that inputs can be any real numbers and, in its simplest version, $\alpha$ does not depend on the input or stimulus identity (p. 348, footnote 3).
- It showed that a "mechanistic" theory could explain blocking, without cognitive theories such as scanning short-term memory backward. It adjusted contiguity theories simply. It is not a complete model of classical conditioning (pp. 348–349).

*Intuition note.* Think of the animal as holding a running guess of how big the US will be. Each stimulus present gets nudged by the shared mistake. If an earlier stimulus already makes the guess right, the mistake is zero and a newcomer gets nothing.

#### 14.2.3 The TD Model (pp. 349–350)
- It is a real-time model. $t$ now labels small time steps (say 0.01 s). The animal is seen as having an endless stream of states, and trials are just convenient fragments (p. 349).
- State features may describe history-dependent neural activity patterns triggered by stimuli. The model does not commit to any representation, and it includes discounting and eligibility traces (p. 349).
- Aggregate associative strength is still (14.1). The update replaces $\mathbf x(S_t)$ by an eligibility trace $\mathbf z_t$ and uses a TD error (p. 350):
$$\mathbf w_{t+1}=\mathbf w_t+\alpha\,\delta_t\,\mathbf z_t\tag{14.4}$$
$$\delta_t=R_{t+1}+\gamma\,\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)\tag{14.5}$$
$$\mathbf z_t=\gamma\lambda\,\mathbf z_{t-1}+\mathbf x(S_t)\tag{14.6}$$
  Here $\gamma\in[0,1]$ is the discount factor and $\lambda$ is the usual trace-decay parameter. $\mathbf x,\mathbf z,\mathbf w$ have shape $n\times1$ and $\hat v$ is a scalar (p. 350).
- If $\gamma=0$, the model reduces to Rescorla–Wagner, except that $t$ means a time step rather than a trial, and the target has a one-step lead. The model equals the backward view of semi-gradient TD($\lambda$) with linear function approximation (Chapter 12), except that $R_t$ need not be a reward (p. 350).

*Intuition note.* The key new ingredient inside the error is the next-step prediction (the update also uses an eligibility trace). The model can therefore learn from a later stimulus that predicts the US, not only from the US itself.

#### 14.2.4 TD Model Simulations (pp. 350–357)
- Real-time models make predictions about timing: ISI, CR shape, and serial compounds, where components occur in sequence (p. 350).
- **Three stimulus representations** (Fig. 14.1, Ludvig, Sutton & Kehoe 2012), differing in how much they generalize across nearby time points (p. 351):
  - *Presence:* one feature per component CS, equal to 1 while it is present. It is unrealistic, but still produces many timing phenomena (p. 351).
  - *Complete serial compound (CSC):* each stimulus onset starts a sequence of precisely timed, short, non-overlapping signals. This is a "tapped delay line" and is unrealistic, but a "useful fiction." It is used in most TD models of dopamine neurons (Ch. 15). Viewing it as essential to the TD model is "mistaken" (p. 352).
  - *Microstimuli (MS):* a cascade of overlapping internal stimuli, each wider in time and lower in peak. It is more realistic. Cascades may be started by USs as well as CSs (p. 352).
- **ISI dependence.** Even with the presence representation, the model produces the Rescorla–Wagner properties plus more. Conditioning typically is negligible for zero or negative ISI, rises to a maximum at a positive ISI, then falls to zero after an interval that varies widely with response system. These are core properties of the model (pp. 352–353).
- **Facilitation of remote associations.** Filling the empty trace interval between CS$_A$ and the US with a second CS (CS$_B$) facilitates conditioning to CS$_A$ (Kehoe 1982). The model shows facilitation of both rate and asymptote (p. 353).
- **Egger–Miller effect.** With two overlapping CSs in a delay configuration, CS$_B$ is in the better temporal relationship with the US. Yet CS$_A$'s presence substantially reduces conditioning to CS$_B$ compared with controls. The model reproduces this (p. 353).
- **Temporal primacy overrides blocking.** With the presence representation (and more complex ones), the model predicts that blocking is reversed if the added CS begins *earlier* than the pretrained CS. The new CS is not blocked, and as it gains strength, the pretrained CS loses strength (p. 354, Fig. 14.2). This had not been observed when the model was introduced. Kehoe, Schreurs and Graham (1987) confirmed it in rabbit nictitating-membrane conditioning, noting that non-TD models have difficulty with their data (p. 354).
- The explanation is bootstrapping: updates move strengths at a state toward strengths at later states, so an earlier predictor takes precedence (p. 354).
- **Second-order conditioning (Fig. 14.3).** In phase 1 CS$_B$ is trained until its strength is 1.65. In phase 2 CS$_A$ is followed by CS$_B$ (0.4 s each) with no US. CS$_A$ gains strength although never paired with the US. Then CS$_A$'s strength peaks and declines, because CS$_B$ is being extinguished: the US does not occur (pp. 354–355).
- Animal experiments show the same pattern. This is why higher-order conditioning is hard to demonstrate unless first-order trials are inserted occasionally (p. 355).
- The reason is $\gamma\hat v(S_{t+1},\mathbf w_t)-\hat v(S_t,\mathbf w_t)$ in (14.5). This temporal difference "has the same status" as $R_{t+1}$, so, as far as learning goes, a temporal difference is like a US occurring. The authors link this to the origin of TD in dynamic programming (p. 355).

*Intuition note.* A stimulus that reliably predicts a reinforcer starts to carry value itself. When it later fails to be followed by the US, its value fades, and so does the support it gives to anything that predicts it.

- **CR timing.** In many experiments CR magnitude or probability rises as the expected US time approaches, and the CR's timing and shape matter for its adaptive value (p. 355). The TD model has no built-in response-generation mechanism. The simplest choice is to equate the CR time course with the US-prediction time course, so CR features depend only on the representation and on $\alpha,\gamma,\lambda$ (p. 356).
- **Fig. 14.4** (US 25 steps after CS onset; $\alpha=.05$, $\lambda=.95$, $\gamma=.97$) (p. 356):
  - CSC: the prediction rises exponentially across the interval and peaks exactly at the US. The authors attribute the exponential rise to discounting (p. 356).
  - Presence: the prediction is almost constant while the stimulus is present, so many CR timing features cannot be reproduced (p. 356).
  - MS: after 200 trials the profile reasonably approximates the CSC curve, through a linear combination of microstimuli (pp. 356 and caption).
- The curves are "raw" US predictions. They were not meant to match any particular animal's CR profiles, but they show the strong influence of the representation (pp. 356–357).
- **Limits and view.** The model is far from perfect. It may need model-based elements or adaptive parameters. Bayesian models are an alternative approach (p. 357).
- Its notable feature is that it rests on a theory of what the nervous system is trying to do: form accurate long-term predictions, within representational limits. The authors call this a normative account in which long-term prediction is key (p. 357). TD also underlies an influential model of dopamine neurons (Ch. 15) (p. 357).

### 14.3 Instrumental Conditioning (pp. 357–361)
- Here the reinforcer depends on what the animal does. The authors use "instrumental" exclusively for behavior-contingent reinforcement. They note it is usually considered the same as Skinner's "operant" (pp. 357–358).
- **Thorndike's puzzle boxes.** Cats escaped by actions such as pressing a platform, pulling a string, or pushing a bar. Escape time almost invariably fell with experience, for example from 300 s to 6 or 7 s (p. 358).
- **Thorndike's view:** unsuccessful impulses are "stamped out," and the successful one is "stamped in" by the resulting pleasure (p. 358). This led to the Law of Effect, which the authors describe as learning by trial and error. They say it has been controversial and modified, but expresses an enduring principle (p. 358).
- RL algorithms are *selectional* (try alternatives and select by consequences) and *associative* (link alternatives to states, forming a policy). Natural selection is selectional but not associative (as commonly understood). Supervised learning is associative but not selectional, because it gives instructions (pp. 358–359).
- In computational terms, the Law of Effect combines search with memory. Memory may be a policy, value function, or model (p. 359).
- **Exploration.** Early researchers disagreed on whether exploration is blind "groping" or guided. RL needs only some exploration; ε-greedy and UCB are among the simplest forms (p. 359).
- **Admissible actions.** Thorndike's cats chose among "instinctual impulses," like the set $A(s)$ in RL. The authors note the cats might instead have used an instinctual context-specific ordering of actions, which would also make RL easier (p. 359).
- **Hull** stressed selection by consequences, with eligibility-like mechanisms, secondary reinforcement, and "behavioral oscillation" as a source of randomness (pp. 359–360).
- **Skinner** emphasized selection from spontaneously emitted behavior, not associative linkages. He built the operant chamber (Skinner box), with a lever delivering reward under a *reinforcement schedule*. Modeling such results with RL is "not well developed" (p. 360).
- **Shaping:** reinforcing successive approximations of the desired behavior. The authors recount Skinner's pigeon-bowling episode (a few minutes to learn). Shaping is also powerful in RL when non-zero reward is hard to obtain: start with an easier problem and increase difficulty (p. 360).
- **Motivation** (influences direction and vigor of behavior) is hard to link precisely to RL, but there are clear links with some of its dimensions (pp. 360–361):
  - The reward signal underlies motivation. Internal state components, such as hunger, can modulate what is rewarding (p. 361).
  - Value functions: a more proximal motive is to ascend the value-function gradient (p. 361).
  - After learning, motivational state also affects *vigor* (a hungry rat runs faster). This does not link cleanly to the framework here (p. 361).

### 14.4 Delayed Reinforcement (pp. 361–363)
- Early critics of the Law of Effect doubted that the present can affect the past. Learning can occur even with long delays, and in classical conditioning with a gap between CS offset and US onset. This is the problem of delayed reinforcement, related to Minsky's "credit-assignment problem" (pp. 361–362).
- RL has two mechanisms: eligibility traces, and TD-learned value functions that give near-immediate evaluations (instrumental) or prediction targets (classical). Both have counterparts in animal theories (p. 362).
- **Stimulus traces.** Pavlov said every stimulus leaves a trace in the nervous system for some time. Learning arises from the simultaneous presence of trace and US (p. 362).
- **Hull's goal gradient:** the maximum strength of a response falls with delay of reinforcement. He hypothesized exponentially decaying "molar stimulus traces" reaching zero after 30–40 s (p. 362).
- RL eligibility traces are like Hull's: decaying traces of past states or state–action pairs. Klopf (1972) introduced them as traces of synaptic activity, more complex than the exponential ones used here (p. 362).
- For longer gradients, Hull proposed conditioned reinforcement passing backward from the goal. Experiments showed that if stimuli regularly occur during the delay, learning drops less with delay (pp. 362–363).
- **Actor–critic correspondence.** The critic's TD error is a conditioned-reinforcement signal for the actor, giving immediate evaluation even if primary reward is delayed. Q-learning and Sarsa do similarly (p. 363).

### 14.5 Cognitive Maps (pp. 363–364)
- An environment model has a state-transition part and a reward-model part. Planning computes a policy from it. The simplest planning compares predicted outcomes of "imagined" decision sequences (p. 363).
- **Latent learning.** Rats in the experimental group got food in the goal box only from stage 2 of the experiment (controls had food throughout). They did not appear to learn much in stage 1, but once food appeared they quickly caught up with the controls. **Blodgett's conclusion:** they had developed a latent learning of the maze during the no-reward period (p. 363).
- **Tolman's interpretation:** animals learn a "cognitive map" without reward and use it when motivated, perhaps planning a different route. In modern terms, cognitive maps are environment models or models of a "task space." The authors compare this to using model-based algorithms, with models learned without explicit reward (p. 364).
- Tolman's account was that animals learn stimulus–stimulus (S–S) associations, which psychologists call expectancy theory. The authors say this is much like system identification in control engineering: learning a model from labeled examples S→S′, SA→S′, or S→R, SA→R. These are supervised learning, requiring no non-zero reward (p. 364).

### 14.6 Habitual and Goal-directed Behavior (pp. 364–368)
- Model-free versus model-based RL corresponds to habitual versus goal-directed control. Habits are triggered by stimuli and performed more or less automatically. Goal-directed behavior is controlled by knowledge of goal values and action–consequence relations (p. 364). Goal-directed control adapts rapidly to environmental change, while habits do not (pp. 364–365).
- **Maze of Fig. 14.5** (p. 365). From S1 the rat picks L or R, then L or R at S2 or S3. Goal-box rewards are 0 and 4 under S2, 2 and 3 under S3. Learned action values for the model-free strategy: $(S_1,L)=4$, $(S_1,R)=3$, $(S_2,L)=0$, $(S_2,R)=4$, $(S_3,L)=2$, $(S_3,R)=3$. The best choice is L at S1 and R at S2, giving return 4 (p. 366).
- A cached policy is another model-free option. Neither uses a transition model or links goal-box features to rewards (p. 366).
- The model-based strategy uses a transition model (a decision tree) and a reward model, and simulates paths to find the best return (p. 366).
- **Adapting to change.** A model-free agent must visit the affected states, act, and experience the new reward, possibly many times. A model-based agent changes its policy through planning (p. 366).
- *Example:* a rat that has learned the model is placed directly in the box right of S2 and finds reward 1 instead of 4. Planning then changes the policy to right turns at S1 and S3, with return 3, without more maze experience (p. 366).
- **Outcome-devaluation experiments** use this logic to test habit versus goal-directed control (pp. 366–367).
- **Adams & Dickinson (1981):** rats pressed a lever for sucrose pellets. They then got free pellets for 15 minutes with the lever retracted, and one group was injected with lithium chloride (nausea-inducing), over three sessions. By the last session, injected rats ate no pellets, so the pellets were devalued. A day later came an extinction session (lever present but disconnected from the dispenser). Injected rats pressed significantly less from the start (p. 367).
- **Adams & Dickinson's conclusion:** the rats used a cognitive map linking lever to pellets and pellets to nausea. They never experienced lever-pressing followed by sickness. The authors note that not every psychologist accepts the cognitive account, but the model-based planning explanation is widely accepted (p. 367).
- **Overtraining (Adams 1982).** Simplified: one group was trained to 100 rewarded presses and the overtrained group to 500, then both were devalued. Devaluation strongly reduced pressing in the non-overtrained group. In the overtrained group it had little effect, if anything making pressing more vigorous. This suggests overtraining produced a habit (pp. 367–368).
- **Daw, Niv & Dayan (2005):** animals use both model-free and model-based processes. Each proposes an action, and the process judged more trustworthy, by confidence measures kept during learning, wins. Early on, planning is more trustworthy, because it chains short-term predictions that become accurate with little experience. Later the model-free process is more trustworthy, because planning is prone to model errors and tree-pruning shortcuts. This predicts a shift from goal-directed to habitual behavior with experience. Other arbitration ideas exist (p. 368).

*Intuition note.* A cached value only changes when the animal actually revisits that state and acts. A model can be updated from news about one place and then used anywhere, which is why a changed outcome shows up in behavior at once only for model-based control.

### 14.7 Summary (pp. 368–370)
- RL is an abstract engineering framework. Many of its algorithms were inspired by psychology, and in some cases they helped build new animal-learning models (pp. 368–369).
- The authors restate the correspondences: prediction/classical, control/instrumental, TD model extending Rescorla–Wagner, eligibility traces/stimulus traces, values/secondary reinforcement, environment models/cognitive maps, model-free vs model-based/habit vs goal-directed (pp. 369–370).
- Omitted: psychology of decision making, ecological and evolutionary behavior, and multi-agent RL. The authors say RL does not imply a "tabula rasa" view (p. 370).

### Bibliographical and Historical Remarks (pp. 371–373)
- A references section by subsection. Items with content: Kamin (1968) first reported blocking; the surprise idea comes from Kamin (1969) (p. 371). The TD model first appeared in Sutton & Barto (1987) and more fully in 1990, and some papers read "TD" as Time Derivative (pp. 371–372). Ng et al. use "shaping" in a different sense: altering the reward without altering the optimal policies (p. 372). Donahoe & Burgos (2000) argue that model-free processes can account for devaluation results, and Dayan & Berridge (2014) argue that classical conditioning involves model-based processes (p. 373).

### Comments on Terminology (pp. 373–376)
- **Reinforcement:** traditionally the strengthening of behavior. The authors extend it to weakening. A reinforcer is not necessarily a reward or penalty, since a classical-conditioning US is delivered regardless of behavior (pp. 373–374).
- **Reward** in common usage is an object or event. The authors' $R_t$ is a number, like a neuroscience reward signal, not an object. They say a single master reward signal in the brain is unlikely (p. 374).
- **Reinforcement signal:** a number that multiplies a vector to determine parameter updates. For TD it is $\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$. $R_{t+1}$ is the primary contribution and the value difference is the conditioned contribution. $\delta_t$ is available only at $t+1$ (pp. 374–375).
- Skinner's positive/negative reinforcement and punishment are not needed here. The authors' negative reinforcement signal is not Skinner's negative reinforcement. They also note that appetitive and aversive systems differ in animals (p. 375).
- **Action** vs response, and **control** (the agent controls the environment, vs stimulus control in psychology). The authors cite Powers (1973) for an equivalent view: the agent controls the input it receives (pp. 375–376).
- RL is broader than S–R learning from rewards alone (p. 376).

## Toy example (ours, not from the text)
**Blocking with Rescorla–Wagner.** Let $R=1$, $\alpha=0.5$. Stimulus A and a new stimulus X; features $\mathbf x$ = (A, X).

*Stage 1 (A alone, 3 trials), $V_A$ starts at 0:*
- Trial 1: $\delta=1-0=1$, $V_A=0+0.5\cdot1=0.5$.
- Trial 2: $\delta=1-0.5=0.5$, $V_A=0.5+0.25=0.75$.
- Trial 3: $\delta=1-0.75=0.25$, $V_A=0.75+0.125=0.875$.

*Stage 2 (compound AX, 1 trial):* $\hat v=0.875+0=0.875$, so $\delta=0.125$. Then $V_A=0.875+0.0625=0.9375$ and $V_X=0+0.0625=0.0625$.

*Control (no stage 1):* $\hat v=0$, so $\delta=1$. Then $V_A=V_X=0.5$.

So X ends with 0.0625 when A was pretrained, against 0.5 in the control. The prior learning has almost blocked X.

**Second-order effect with the TD error.** Take $\lambda=0$ (so $\mathbf z_t=\mathbf x(S_t)$), $\gamma=0.9$, $\alpha=0.5$, presence features, $R=0$. The sequence is A → B → end (terminal value 0). Start with $w_B=1$, $w_A=0$.
- At A: $\delta=0+0.9\cdot1-0=0.9$, so $w_A=0+0.5\cdot0.9=0.45$. A gains strength although no US occurred.
- At B: $\delta=0+0-1=-1$, so $w_B=1-0.5=0.5$. B is being extinguished, as in Fig. 14.3.

## Concepts
- [[classical-conditioning]] (new) — learning that a CS predicts a US, with the US delivered regardless of behavior; corresponds roughly to prediction (pp. 342, 344)
- [[instrumental-conditioning]] (new) — learning where reinforcement is contingent on behavior; corresponds roughly to control; usually considered the same as Skinner's operant conditioning, though experiments and theories differ in some ways; the authors use "instrumental" exclusively (pp. 342, 357–358)
- [[blocking]] (new) — a CS added to an already-trained CS gets little conditioning, which challenged the idea that contiguity is sufficient (p. 345)
- [[rescorla-wagner-model]] (new) — trial-level error-correcting rule $\Delta\mathbf w=\alpha\delta\mathbf x$; essentially the LMS rule (pp. 346–348)
- [[td-model-of-conditioning]] (new) — real-time model with TD error (14.5) and eligibility traces; no fixed state representation (pp. 349–350)
- [[temporal-difference-learning / reward prediction error]] — here $\delta_t$ acts as a conditioned/primary reinforcement signal and as "surprise" (pp. 348, 350, 375)
- [[eligibility-trace]] (new) — decaying trace of past states; like Hull's stimulus traces; introduced by Klopf as synaptic traces, which are more complex than the exponential traces used here (pp. 350, 362)
- [[stimulus-representation]] (new) — how stimuli map to features: CSC, microstimuli, or presence; changes the TD model's predictions (pp. 350–352, 356)
- [[conditioned-reinforcement]] (new) — a reinforcing effect that a stimulus gets by predicting another reinforcer; in RL the TD value difference (pp. 346, 375)
- [[credit-assignment-problem]] (new) — distributing credit for success among earlier decisions (pp. 361–362)
- [[law-of-effect]] (new) — selecting and connecting actions by their consequences; corresponds to search plus memory (pp. 358–359)
- [[shaping]] (new) — reinforcing successive approximations of a desired behavior (p. 360)
- [[cognitive-map]] (new) — an animal's environment model or "task space"; learnable without reward (pp. 363–364)
- [[model-based vs model-free RL]] — corresponds to goal-directed vs habitual control (pp. 364–366)
- [[outcome-devaluation]] (new) — changing a reward's value between stages to test whether behavior is habitual or goal-directed (pp. 366–367)
- [[exploration vs exploitation]] — RL needs some exploration, which can be guided rather than blind (p. 359)
- [[policy]] — the learned association of states with actions (p. 358)
- [[perceptual control]] — the "agent controls its input" view, cited to Powers; only mentioned here (p. 376)

## Canonical instances
- [[pavlov-metronome-dog]] — salivation to a metronome that precedes food (p. 343)
- [[nictitating-membrane-conditioning]] — rabbit tone/air-puff CR timing; blocking and temporal-primacy experiments (pp. 344, 345, 354)
- [[kamin-blocking-three-stage]] — tone, tone+light, light-alone design (p. 345)
- [[egger-miller-overlapping-cs]] — an overlapping CS reduces conditioning to a CS with a better temporal relationship to the US (p. 353)
- [[temporal-primacy-overrides-blocking]] — TD-model prediction confirmed in rabbits (p. 354)
- [[second-order-conditioning-black-square]] — a dog salivates to a square followed by the metronome (p. 345)
- [[thorndike-puzzle-box]] — cat escape times fall with experience (p. 358)
- [[skinner-pigeon-bowling]] — shaping by reinforcing approximations (p. 360)
- [[latent-learning-maze]] — Blodgett/Tolman rats (pp. 363–364)
- [[niv-joel-dayan-maze]] — hypothetical maze contrasting model-free and model-based choice (pp. 365–366)
- [[adams-dickinson-devaluation]] — lever-pressing after lithium-chloride devaluation of pellets (p. 367)
- [[adams-overtraining]] — 100 vs 500 presses and sensitivity to devaluation (pp. 367–368)

## Bridges (candidates)
- [same-math] Rescorla–Wagner update (14.2–14.3) ↔ supervised learning: the LMS/Widrow–Hoff rule — the text calls them essentially the same, with the differences noted in footnote 3.
- [same-math] TD model (14.4–14.6) ↔ RL: backward-view semi-gradient TD($\lambda$) with linear approximation — stated as equivalent, except for what $R_t$ represents.
- [structural-analogy] Tolman's S–S and SA–S′ expectancies ↔ control engineering: system identification — the text says it is "much like" learning a model from labeled examples.
- [structural-analogy] CSC representation ↔ engineering: tapped delay line — each time since onset has its own feature.
- [structural-analogy] Skinner's shaping ↔ RL training: incrementally harder tasks when reward is sparse (p. 360).
- [metaphor] Agent "controlling its input" (Powers, cited) ↔ perceptual control: behavior as control of perception — only mentioned in one sentence (p. 376).

## Questions this raises
- How does an animal's brain actually generate representations like microstimuli, and which one best fits behavior? (the text leaves this open, pp. 352, 357)
- What measures of "confidence" would let an agent arbitrate between model-free and model-based control, and are there alternatives to Daw–Niv–Dayan? (p. 368)
- Can RL formalize behavior under reinforcement schedules and the vigor of responding? (the text says this is not well developed, pp. 360–361)
- What would be gained by separate appetitive and aversive systems, instead of one signed reward number? (p. 375)

## Reading notes
- Offset: printed = pdf − 22 (unit covers pdf 363–398 = printed 341–376). All citations use printed numbers.
- The text layer drops many Greek and special symbols (Δ, δ, α, γ, λ, ε). I restored them from context and from the image of p. 350. No images of pp. 347, 348 and 375 were supplied. Equations on those pages (the Rescorla–Wagner $\Delta V$ lines, (14.1)–(14.3), and the TD error in the terminology section) are therefore reconstructed from the text layer and the surrounding prose.
- p. 350: the text says "$R_t$ is the prediction target at time $t$," while (14.5) uses $R_{t+1}$.
- p. 349: "model model" is a duplicated word in the print. p. 368: "e↵ect" is used where "affect" seems intended.
- In the Rescorla–Wagner section the feature vector has dimension $d$; the TD section writes $n$. The text does not comment on this change of symbol; I treat them as the same dimension.
- Figures 14.1–14.5 and the unnumbered simulation plots on pp. 353–355 are described from captions and prose, plus the page images that were supplied (pp. 350, 351, 355, 356, 365, 366). Fig. 14.4 value ranges (e.g., 0–1) are read from the caption and image, not computed.
- The chapter has no exercises.
