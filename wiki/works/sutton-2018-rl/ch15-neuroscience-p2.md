---
id: sutton-2018-rl/ch15-neuroscience-p2
work: sutton-2018-rl
unit: "Chapter 15 (part 2/2): end of 15.7, then 15.8–15.13 and Bibliographical and Historical Remarks"
pages: 398–420
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Neuroscience (part 2/2): actor and critic learning rules, hedonistic neurons, teams, model-based methods, addiction

## L0 — One line
The learning rules of the actor and the critic in an actor–critic algorithm differ only in the kind of eligibility trace they use, and this difference may match how dopamine-modulated corticostriatal synapses change.

## L1 — The gist (≤ 120 words)
The question: if the brain runs something like actor–critic, what synaptic learning rules would that imply? Both rules use the same dopamine-like TD-error signal. The critic's eligibility traces (decaying records of past synaptic activity) depend only on presynaptic activity (a two-factor rule). The actor's traces also depend on the unit's own output (a three-factor rule), like reward-modulated spike-timing-dependent plasticity (STDP) and Klopf's hedonistic neuron. If each unit learns well enough, many units sharing one broadcast signal form a team that can learn without communicating. The chapter also covers model-based brain systems (dorsolateral and dorsomedial striatum, orbitofrontal cortex, hippocampus) and Redish's TD model of addiction. It matters because many computationally motivated reinforcement-learning features turn out to fit neuroscience data.

**Prerequisites:** TD error and eligibility traces; policy-gradient/REINFORCE and the actor–critic algorithm (Ch. 13); logistic function; gradient of a log-probability; model-free vs model-based RL.

## L2 — Key ideas (5–10 bullets)
- The actor and critic use the same TD error δ. The critic reduces |δ| (prediction, like the TD model of classical conditioning); the actor keeps δ as positive as possible (control, like the Law of Effect) (p. 398).
- Critic traces are non-contingent (presynaptic only). Actor traces are contingent (they also include the unit's own action), and this is the only difference between the rules (p. 400).
- A contingent trace combined with a dopamine-like reinforcement signal gives a three-factor rule (p. 401). It resembles reward-modulated spike-timing-dependent plasticity (STDP); indirect evidence, from neuromodulator windows of up to 10 s, points to prolonged contingent traces at corticostriatal synapses (p. 402).
- Klopf's hedonistic neuron says single neurons act like reinforcement learners. Bacterial chemotaxis ("run and twiddle") shows a single cell can seek some stimuli and avoid others (pp. 402–404).
- Many actor units sharing one reward signal form a team. Teams need contingent traces and variable output; non-contingent traces fail. Williams showed that teams of Bernoulli-logistic REINFORCE units ascend the average-reward gradient (pp. 405–407).
- Model-free and model-based processes map onto brain regions only partly: dorsolateral (DLS) vs dorsomedial (DMS) striatum, orbitofrontal cortex (OFC), hippocampus. The separation is not clean (pp. 407–409).
- Redish's model of addiction: a drug-induced δ cannot be "predicted away", so values grow without bound. It is a partial model only (pp. 409–410).

## L3 — Walkthrough

### End of 15.7 (p. 398)
- The reward input to dopamine neurons (SNpc, VTA) in Figure 15.5b is really a vector of reward-related information arriving over many channels. The theoretical scalar $R_t$ might correspond to the net contribution of all reward-related information to dopamine neuron activity; it results from a pattern of activity across many neurons in different brain areas (p. 398).
- The actor–critic implementation of Figure 15.5b may be correct in some respects but, the authors say, clearly needs refinement to be a full model of phasic dopamine activity (p. 398).

### 15.8 Actor and Critic Learning Rules (pp. 398–402)
**Setting.** Assume dopamine neurons broadcast one reinforcement signal, the TD error δ, to corticostriatal synapses of both dorsal and ventral striatum (the authors say this is likely an oversimplification) (p. 398). The effect differs by component:
- Actor: δ plus eligibility traces says how to change action probabilities toward higher-valued states. This is Law-of-Effect-type learning: the actor works to keep δ as positive as possible (p. 398).
- Critic: δ with traces says how to change value parameters to improve prediction. The critic works to bring |δ| close to zero, like the TD model of classical conditioning (Section 14.2) (p. 398).
- The difference between the two rules lies solely in the eligibility traces each uses (p. 398).

**Algorithm used** (actor–critic for continuing problems with traces, Section 13.6) (pp. 398–399):

$$\delta_t = R_{t+1} + \gamma \hat v(S_{t+1},\mathbf w) - \hat v(S_t,\mathbf w)$$
$$\mathbf z^{\mathbf w}_t = \gamma\lambda^{\mathbf w}\mathbf z^{\mathbf w}_{t-1} + \nabla\hat v(S_t,\mathbf w)$$
$$\mathbf z^{\boldsymbol\theta}_t = \gamma\lambda^{\boldsymbol\theta}\mathbf z^{\boldsymbol\theta}_{t-1} + \nabla\ln\pi(A_t|S_t,\boldsymbol\theta)$$
$$\mathbf w \leftarrow \mathbf w + \alpha^{\mathbf w}\delta_t\mathbf z^{\mathbf w}_t,\qquad \boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha^{\boldsymbol\theta}\delta\,\mathbf z^{\boldsymbol\theta}_t$$

Here $\gamma\in[0,1)$ is the discount rate, $\lambda^{\mathbf w},\lambda^{\boldsymbol\theta}\in[0,1]$ are bootstrapping parameters, and $\alpha^{\mathbf w},\alpha^{\boldsymbol\theta}>0$ are step sizes (p. 399).

**Critic unit.** A single linear neuron-like unit (labelled V in Figure 15.5a) (p. 399):
$$\hat v(s,\mathbf w)=\mathbf w^\top\mathbf x(s)\tag{15.1}$$
- $\mathbf x(s)=(x_1(s),\dots,x_n(s))^\top$ is the feature vector, and $\mathbf w=(w_1,\dots,w_n)^\top$ is the weight vector. Each $x_i(s)$ is like the presynaptic signal at a synapse of efficacy $w_i$ (p. 399).
- Because $\hat v$ is linear in $\mathbf w$, $\nabla\hat v(S_t,\mathbf w)=\mathbf x(S_t)$ (p. 399).
- Each synapse has its own trace, one component of $\mathbf z^{\mathbf w}_t$. It accumulates with presynaptic activity and otherwise decays toward zero at a rate set by $\lambda^{\mathbf w}$. A synapse is eligible while its trace is non-zero (p. 399).
- The actual change depends on the reinforcement signals that arrive while it is eligible (p. 399).
- These are **non-contingent** traces: they depend only on presynaptic activity, not on postsynaptic activity. The critic's rule is then essentially the TD model of Section 14.2, and it equals the critic of Barto et al. (1983) (p. 399).
- A one-unit critic is the simplest start; it stands in for a more complex network that learns richer value functions (p. 399).

**Actor units.** A one-layer network of $k$ identical units, each with weight vector $\boldsymbol\theta_j$, all receiving the same $\mathbf x(S_t)$ (pp. 399–400). One option is a **Bernoulli-logistic unit**: output $A_t\in\{0,1\}$ (1 = the neuron fires), with probability from the exponential soft-max (13.2), which for two actions is (p. 400)
$$\pi(1|s,\boldsymbol\theta)=1-\pi(0|s,\boldsymbol\theta)=\frac{1}{1+\exp(-\boldsymbol\theta^\top\mathbf x(s))}\tag{15.2}$$
Exercise 13.5 asks for this gradient; for the state and action that actually occurred, the result is (p. 400):
$$\nabla\ln\pi(A_t|S_t,\boldsymbol\theta)=\big(A_t-\pi(1|S_t,\boldsymbol\theta)\big)\mathbf x(S_t)\tag{15.3}$$
- In Figure 15.5a, $\delta_t$ is broadcast to all synapses of all actor units, which makes the actor a team of RL agents (Section 15.10) (p. 400).
- The trace is **contingent**: it depends on presynaptic activity $\mathbf x(S_t)$ and on the unit's own output through $A_t-\pi(1|S_t,\boldsymbol\theta)$. This factor is positive when $A_t=1$ and negative otherwise (p. 400).
- The authors state that this postsynaptic contingency is the only difference between the critic and actor learning rules (p. 400).
- Contingent traces keep a record of what action was taken in what state. Credit (δ>0) or blame (δ<0) can then be shared among policy parameters according to their contribution to outputs that could have influenced later δ (p. 400).

*Intuition note.* A trace is a short-lived tag on a synapse that says "I was involved". For the critic, involvement means only that input arrived. For the actor, it also records which way the unit's output went, so a later δ can push the unit toward or away from that output.

**Two-factor vs three-factor rules.** Both rules are related to Hebb's proposal and share with it the idea that a synapse's change depends on the interaction of several factors (pp. 400–401).
- Critic: δ × presynaptic-only traces = a two-factor rule (pp. 400–401).
- Actor: traces depend on pre- and postsynaptic activity, so with δ it is a three-factor rule. Unlike Hebb's proposal, relative timing is critical, and traces let δ act on synapses active in the recent past (p. 401).

**Timing subtleties** (p. 401).
- The model ignores the several tens of milliseconds a real synapse needs to affect firing; (15.1) and (15.2) act instantaneously. This is common in abstract Hebbian models; more realistic models must include activation time (p. 401).
- Activation time matters for contingent traces. The presynaptic factor must be a cause of the postsynaptic factor in the trace. Ignoring activation time makes this true automatically here (p. 401).
- Activation time should not be confused with the (generally much longer) delay before a neuron receives a reinforcement signal influenced by its activity. Traces span the longer interval (p. 401).

**STDP.** In spike-timing-dependent plasticity, the dependence can take different forms; in the most-studied one a synapse strengthens if presynaptic spikes arrive shortly before the postsynaptic neuron fires. It weakens if the order is reversed. This is one ingredient of actor-like learning, since it takes activation time into account (p. 401).

**Reward-modulated STDP** is a three-factor form in which neuromodulatory input must follow appropriately timed pre- and postsynaptic spikes (p. 402).
- Evidence is accumulating that it occurs at spines of medium spiny neurons of the dorsal striatum, with dopamine as the modulator (p. 402).
- Yagishita et al. (2014) found lasting corticostriatal changes only if a neuromodulatory pulse arrives within a window of up to 10 seconds after a pre-then-post spike pair. The evidence is indirect, but it points to contingent traces with prolonged time courses; their molecular mechanisms are not understood (p. 402).
- The actor unit appeared in simpler form in Barto et al. (1983), inspired by Klopf's hypothesis. Not all of Klopf's details fit current knowledge, but STDP findings suggest his ideas "may not have been far off the mark" (p. 402).

### 15.9 Hedonistic Neurons (pp. 402–404)
**Klopf's conjecture** (Klopf's view, not established fact) (pp. 402–403):
- Individual neurons seek to maximise the difference between synaptic input treated as rewarding and input treated as punishing. They adjust synaptic efficacies according to the consequences of their own action potentials (p. 402).
- Rewards and punishments arrive through the same synapses that excite or inhibit the neuron. Klopf wanted to avoid any centralised source of training information (p. 402).
- Synapses are made "eligible" (his term) by synaptically local traces, which he thought were molecular, not electrical (p. 402).
- Mechanism: when a neuron fires, all synapses that contributed become eligible. If an increase of reward follows within an appropriate time, eligible synapses strengthen. If an increase of punishment follows, they weaken. A trace starts upon pairing of presynaptic activity with the postsynaptic activity it helps cause. This is a contingent trace, essentially the actor's three-factor rule (p. 403).
- In Klopf's theory the trace's shape reflects the durations of the feedback loops the neuron sits in, some inside the animal and some through the external environment. It is like a histogram of loop durations, peaking at the most prevalent loop duration (p. 403).
- The book's traces are simplified, geometrically decaying (parameters γ and λ). The authors treat them as placeholders for traces closer to Klopf's, which might refine credit assignment (p. 403).

**Chemotaxis analogy.** Binding events at receptors of *E. coli* modulate how often it reverses flagellar rotation, and each reversal makes it tumble and set off in a random new direction. Reversal frequency falls when it swims up attractant gradients and rises up repellent gradients (p. 403). This is klinokinesis, a kind of trial and error; the bacterium needs short-term memory but probably not long-term memory (p. 403). Selfridge's "run and twiddle": "keep going in the same way if things are getting better, and otherwise move around" (p. 404).
- A neuron might similarly "swim" among its feedback loops, but its synaptic strengths keep information about past trial and error. If this view is plausible, the closed-loop nature of the neuron's interaction with its environment (the rest of the animal plus the world) matters for understanding it (p. 404).
- Klopf also argued that intelligent behaviour may result from a society or economy of self-interested neurons (p. 404).

### 15.10 Collective Reinforcement Learning (pp. 404–407)
- Each actor unit tries to increase δ, so δ acts as its reward. Each unit is an RL agent, a "hedonistic neuron". Assume (as a simplification) that all receive the same signal at the same time (p. 404).
- All agents maximising a common reward is a **cooperative game / team problem**. The common reward evaluates the collective action, so each agent has only limited influence on it. This creates a **structural credit assignment problem**: which members deserve credit or blame? (p. 405)
- In a competitive game, agents get different reward signals and may have conflicts of interest. This might be relevant to heterogeneity of dopamine activity, but the book focuses on teams (p. 405).
- **Result:** if each agent can learn effectively despite a very noisy reward signal and incomplete state information, then the population learns collective actions that improve under the common signal, even without communication. For each agent, the others are part of its environment, and each can only partially observe that environment (p. 405).

**Two required features for neuron-like team members** (pp. 405–406):
1. *Contingent eligibility traces.* They keep an action memory, so the unit can raise or lower the probability of its recent action. This is only a preliminary step: the link between one member's action and the team reward is a statistical correlation estimated over many trials (p. 406). Learning with non-contingent traces does not work at all in the team setting, since they cannot correlate actions with reward changes. They suffice for learning to predict (the critic) but not for learning to control (the actor). A population of critic-like units would all learn to predict the same quantity, which is not a team problem (p. 406).
2. *Variability in actions*, so the team explores collective actions. The simplest way is for each member to vary its own output independently. Bernoulli-logistic units always show variability, since the weighted sum only biases firing probability (p. 406).

**Williams (1992):** a team of Bernoulli-logistic REINFORCE units implements a policy-gradient algorithm for the team's average common reward rate. Each unit maximises its own average reward rate. This also holds when the units form a multilayer ANN with the reward broadcast to all of them (pp. 406–407). Such a team learns like a backpropagation-trained network, with the broadcast reward replacing backpropagation. Backpropagation is considerably faster in practice, but the team method is more plausible as a neural mechanism, given reward-modulated STDP (p. 407).

More sophisticated options exist: coordinated exploration, or restricting collective actions. An example of restriction is winner-take-all (for example by lateral inhibition), where only the winners get credit or blame (p. 407).

*Intuition note.* In a team, no unit sees what the others do, and each sees only a noisy team score. Each unit therefore tries random variations and correlates its own variation with the score over many trials. This works only if the unit remembers its own action (contingent trace) and actually varies it.

### 15.11 Model-based Methods in the Brain (pp. 407–409)
- The basic actor–critic is model-free, so the hypothesis covers only habitual behaviour. What produces goal-directed behaviour? (p. 407)
- Inactivation experiments with outcome devaluation in rats: inactivating the dorsolateral striatum (DLS) impairs habit learning, so the animal relies more on goal-directed processes. Inactivating the dorsomedial striatum (DMS) impairs goal-directed processes. This suggests rodent DLS is more involved in model-free and DMS more in model-based processes. It also means the actor-in-dorsal-striatum placement is too simple (p. 407). Human imaging and primate studies support that the analogous primate structures are differentially involved (p. 408).
- The orbitofrontal cortex (OFC) shows strong activity (in human imaging and monkey single-neuron recordings) related to the subjective reward value of significant stimuli and to the reward expected from actions. This suggests (not free of controversy) involvement in goal-directed choice, and perhaps the reward part of an environment model (p. 408).
- The hippocampus: critical for navigation in the goal-directed way that led Tolman to cognitive maps, and perhaps for imagining new experiences (p. 408). When a rat pauses at a maze choice point, the decoded hippocampal spatial representation sweeps forward (not backward) along possible paths (Johnson and Redish, 2007). These sweeps closely match the rat's later navigation (Pfeiffer and Foster, 2013). This suggests the hippocampus supports the state-transition part of the model and a system that simulates future state sequences, a form of planning (p. 408).
- **Open questions** (p. 408): how can structurally similar DLS and DMS support such different modes? Are transition and reward components in separate structures? Is all planning decision-time simulation like a rollout algorithm (Section 8.10), or are models also used in the background as in Dyna (Section 8.2)? How does the brain arbitrate between systems? Is there a clear separation?
- The evidence does not point to a clear separation. Doll, Simon, and Daw (2012) wrote that model-based influences "appear ubiquitous more or less wherever the brain processes reward information", including dopamine signals (p. 409).

### 15.12 Addiction (pp. 409–410)
- Background view: drugs, being intensely reinforcing, may co-opt natural learning and decision mechanisms. Many (not all) drugs of abuse raise dopamine near striatal dopamine terminals. The open question is whether addiction is normal learning with evolutionarily novel substances or interference with normal learning (p. 409).
- **Redish's (2004) model** of some, certainly not all, features of addiction (p. 409):
  - Cocaine and some other drugs produce a transient dopamine increase. The model assumes this raises δ in a way changes in the value function cannot cancel.
  - Normally δ shrinks as a reward becomes predicted (Section 15.6). The drug's contribution does not: drug rewards cannot be "predicted away".
  - The model implements this by preventing δ from ever becoming negative when the reward is due to the drug. This removes TD's error correction for states tied to drug intake, so their values rise without bound and actions leading to them are preferred above all others.
- **Limits** (p. 410): addiction is far more complicated. Dopamine seems not critical in all forms, susceptibility varies, the model omits circuit changes of chronic use (such as diminishing drug effect), and addiction likely involves model-based processes. Still, the model shows RL theory being applied to a health problem. RL theory also influenced computational psychiatry (p. 410).

### 15.13 Summary (pp. 410–412)
The summary restates the chapter: dopamine neurons' phasic responses signal reward prediction errors and act as a reinforcement signal, not a reward signal. A prominent hypothesis is that the dorsal and ventral striatum may function respectively like an actor and a critic. The only difference between the actor and critic rules is the kind of eligibility trace, and the actor rule corresponds closely to reward-modulated STDP (window up to 10 s) (pp. 410–411). Klopf's hypothesis is the root of synaptic eligibility. Team learning with a globally broadcast signal is a neurally plausible alternative to backpropagation. Model-free and model-based processes do not appear to be neatly separated; Redish's model illustrates how a computational view generates testable theories (pp. 411–412). The authors add that many purely computational features of RL algorithms turn out to match neuroscience data, and eligibility traces and team learning may follow (p. 412).

### Bibliographical and Historical Remarks (pp. 413–419)
Compressed; each entry names the claim the source attaches to it.
- **General** (p. 413): starting reviews are Niv (2009), Dayan and Niv (2008), Glimcher (2011) and others. Glimcher (2003) introduced "neuroeconomics".
- **15.2** (p. 413): Berridge and Kringelbach review reward and pleasure. Berridge and Robinson separate "liking" from "wanting". Hare et al. distinguish goal values, decision values and prediction errors; decision value = goal value minus action cost.
- **15.3** (pp. 413–414): the hypothesis was first explicitly stated by Montague, Dayan, and Sejnowski (1996), as RPEs, though their development made clear they meant TD errors. Earlier links come from Montague et al. (1993) and Quartz et al. (1992). Other models cover honeybee foraging with octopamine, basal-ganglia mappings (Barto 1995a; Houk, Adams, Barto 1995) and birdsong. O'Reilly and Frank argued dopamine signals are RPEs but not TD errors, citing variable interstimulus intervals and the rarity of conditioning beyond second order.
- **15.4** (p. 414): optogenetic experiments are cited. Dopamine neurons may form populations with different targets and functions. Eshel et al. found homogeneous RPE responses in lateral VTA in mice, which does not rule out diversity over wider areas.
- **15.5–15.7** (p. 415): Schultz (1998) is a survey; imaging studies support TD-like signals in humans. Section 15.6 follows Barto (1995a). Section 15.7 is largely based on Takahashi, Schoenbaum, and Niv (2008) and Niv (2009). O'Doherty et al. (2004) suggested the actor and critic are most likely in the dorsal and ventral striatum respectively. Many more anatomically detailed hypotheses exist.
- **15.8** (pp. 415–416): the early network's actor trace used only $A_t\times\mathbf x(S_t)$, not $(A_t-\pi(1|S_t,\boldsymbol\theta))\mathbf x(S_t)$. Reynolds and Wickens proposed a three-factor corticostriatal rule. Markram et al. (1997) gave the definitive STDP demonstration. Rao and Sejnowski suggested STDP as a TD-like mechanism with non-contingent traces of about 10 ms; Dayan commented that this needs an error as in Sutton and Barto's 1981 model, not a true TD error. Pawlak and Kerr showed dopamine is necessary for STDP at corticostriatal synapses. Yagishita et al. found spine enlargement only during a window of 0.3 to 2 seconds after STDP stimulation (p. 416). The main text gives a window of up to 10 s for neuromodulator arrival (see Reading notes).
- **15.9** (pp. 416–418): similar earlier ideas. Crow (1968) proposed a contingent eligibility for whole neurons, with reward signals sent over a separate fiber system. Miller (1981) proposed synaptically local contingent traces plus a critic-like "sensory analyzer unit" and anticipated reward-modulated STDP. Seung's "hedonistic synapse" is essentially Minsky's SNARC. Other related proposals: Frey and Morris's "synaptic tag"; O'Reilly and Frank's working memory instead of traces; He et al. (2015) found evidence of contingent traces in cortical synapses. Chemotaxis metaphors: Barto (1989), Koshland, Shimansky.
- **15.10** (pp. 418–419): three phases of research. (1) Tsetlin's learning automata. (2) Associative extensions, including associative search elements, Barto and Anandan's associative reward-penalty ($A_{R-P}$) algorithm, teams of $A_{R-P}$ units learning XOR with a global signal, and Williams (1992), who analysed these rules and related them to backpropagation. He showed a special case of $A_{R-P}$ is REINFORCE, though the general $A_{R-P}$ gave better results. (3) Work influenced by dopamine as a broadcast neuromodulator and reward-modulated STDP.
- **15.11–15.12** (p. 419): the DLS/DMS result is reviewed by Yin and Knowlton (2006). OFC findings come from Valentin et al. and Padoa-Schioppa and Assad. Bromberg-Martin et al. (2010) found dopamine signals carry information relevant to both habitual and goal-directed behaviour. Doll, Simon, and Daw (2012) argued there may not be a clear separation. Keiflin and Janak (2015) review TD errors and addiction; Nutt et al. critically evaluate the dopamine-disorder hypothesis of addiction.

## Toy example (ours, not from the text)
One Bernoulli-logistic actor unit and one critic unit, with one input feature $x=1$ always, $\theta=0$, so $\pi(1)=1/(1+e^0)=0.5$. Take $\gamma=0.5$, $\lambda=1$ (so $\gamma\lambda=0.5$), $\alpha=0.1$. Assume $\delta_1=0$, so nothing changes at step 1.
- Step 1, suppose $A_1=1$. Actor gradient $=(1-0.5)\cdot1=0.5$, so $z^\theta_1=0.5$. Critic gradient is $x=1$, so $z^w_1=1$.
- Step 2, suppose $A_2=0$ (θ still 0). Actor gradient $=(0-0.5)\cdot 1=-0.5$, so $z^\theta_2=0.5\cdot0.5-0.5=-0.25$. Critic: $z^w_2=0.5\cdot1+1=1.5$.
- Now $\delta_2=+1$ arrives. Actor: $\Delta\theta=0.1\cdot1\cdot(-0.25)=-0.025$. Firing becomes slightly less likely: $\pi(1)=1/(1+e^{0.025})\approx0.4938$. Critic: $\Delta w=0.1\cdot1\cdot1.5=0.15$.
- Lesson: the critic's trace is $\ge 0$ whatever the unit did, so δ>0 raises the value estimate. The actor's trace carries the sign of the unit's recent action choices, so the same δ raises or lowers the firing probability depending on what the unit did. This is the single difference between the rules.

## Concepts
- [[temporal-difference-learning-reward-prediction-error]] — δ is the TD error, here the dopamine-like reinforcement signal sent to both actor and critic (p. 398)
- [[policy]] — here, the firing probability of an actor unit, π(1|s,θ) (p. 400)
- [[model-based-vs-model-free-rl]] — mapped onto habitual vs goal-directed behaviour and onto DLS/DMS (p. 407)
- [[exploration-vs-exploitation]] — in a team, needed as variability in each member's output (p. 406)
- [[feedback]] — in Klopf's view, feedback loops inside and outside the animal shape a neuron's trace (p. 403)
- [[eligibility-trace]] (new) — synapse-local decaying record of past activity that lets a later reinforcement signal change it (p. 399)
- [[contingent-eligibility-trace]] (new) — trace that depends on presynaptic input and on the unit's own output (p. 400)
- [[non-contingent-eligibility-trace]] (new) — trace depending only on presynaptic activity (p. 399)
- [[actor-critic]] (new) — actor adjusts the policy; critic learns values; both driven by the same δ (p. 398)
- [[three-factor-learning-rule]] (new) — synaptic change depends on pre- and postsynaptic activity plus a reinforcement signal (p. 401)
- [[reward-modulated-stdp]] (new) — STDP changes occur only if neuromodulator arrives in a window after the spike pair (p. 402)
- [[hedonistic-neuron]] (new) — Klopf's conjecture that single neurons are reinforcement learners (p. 402)
- [[team-problem]] (new) — agents all maximising one common reward that evaluates the collective action (p. 405)
- [[structural-credit-assignment]] (new) — deciding which team members deserve credit or blame for the common reward (p. 405)

## Canonical instances
- [[ecoli-chemotaxis-klinokinesis]] — single-cell run-and-twiddle seeking of attractants (p. 403)
- [[yagishita-2014-reward-modulated-stdp]] — dopamine window of up to 10 s after spike pair at corticostriatal synapses (p. 402)
- [[hippocampal-forward-sweeps]] — spatial representation sweeps forward at a maze choice point, suggesting planning (p. 408)
- [[outcome-devaluation-dls-dms]] — DLS inactivation impairs habits; DMS inactivation impairs goal-directed behaviour (p. 407)
- [[redish-2004-addiction-model]] — δ cannot go negative for drug reward, so values grow unboundedly (p. 409)
- [[williams-1992-reinforce-teams]] — Bernoulli-logistic REINFORCE teams ascend the average reward gradient (p. 406)

## Bridges (candidates)
- [same-math] ∇ ln π(A|S,θ) = (A − π(1))x for a logistic unit ↔ statistics: the gradient of the Bernoulli log-likelihood under a logistic link — same expression form.
- [same-math] eligibility trace $z_t=\gamma\lambda z_{t-1}+g_t$ ↔ signal processing: a first-order exponentially decaying (low-pass) sum of past inputs.
- [structural-analogy] "run and twiddle" in chemotaxis ↔ control-theory: perturb-and-keep-if-improving search with a short memory of the last change.
- [structural-analogy] team of units with one broadcast reward ↔ game theory: cooperative game with common payoff, where credit assignment replaces communication.
- [metaphor] hedonistic neuron / society of neurons ↔ economics: an economy of self-interested agents.

## Questions this raises
- If critic traces are non-contingent but actor traces are contingent, what changes in the biology make the two striatal regions differ (the text says only that the molecular mechanisms producing the traces are not yet understood, p. 402)?
- When many units share one δ, how much slower than backpropagation is the team method, as the number of units grows? (The text says only "considerably faster", p. 407.)
- If dopamine also carries model-based information, which part of δ is reward prediction error and which comes from a model?
- Does the prevented-negative-δ account of addiction predict testable differences from normal learning?

## Reading notes
- **Part boundaries.** This unit starts mid-Section 15.7 (the paragraph on reward input to dopamine neurons, printed p. 398) and ends with the Bibliographical and Historical Remarks on printed p. 419. Printed p. 420 has no text in the text layer. It is the second half of Chapter 15 (the source note says it was split at a section boundary). Printed = pdf − 22.
- **OCR.** The text layer garbles Greek symbols (δ, θ, λ, γ, α) and bold vectors. Equations here were read from the page image of printed pp. 399–400. In the actor update the printed equation is $\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha^{\boldsymbol\theta}\delta\,\mathbf z^{\boldsymbol\theta}_t$ with δ lacking the subscript t, unlike the critic update.
- **Inconsistencies in the printed text.**
  - Section 15.8 cites the algorithm in Section 13.6; the summary (p. 411) says Section 13.5.
  - Klopf's hypothesis is cited as Klopf (1972, 1982) on pp. 402 and 416, but as (1972, 1981) in the summary (p. 411).
  - The Yagishita et al. window is given as up to 10 s in the text (pp. 402, 411) but as 0.3 to 2 s in the remarks (p. 416). The pages do not say whether these describe the same measurement; I report both.
  - Spelling misprints: "Gimcher (2011)" on p. 413, a missing word after "may not" on p. 419, "Wightmman" on p. 414.
- Quotes from Crow (1968) and Miller (1981) in the remarks are summarised, not quoted.
