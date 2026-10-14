---
id: rabinowitz-2018-machine-tom/main
work: rabinowitz-2018-machine-tom
unit: paper
pages: pdf 1–10 (printed page numbers not visible)
fields: [theory-of-mind]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Machine Theory of Mind (Rabinowitz et al., 2018)

## L0 — One line
A neural "observer" (the ToMnet) can meta-learn, from behaviour alone and with weak assumptions, a prior over agents plus a fast agent-specific posterior, and in gridworlds this is enough to pass a Sally-Anne-style false-belief test.

## L1 — The gist (≤ 120 words)
How can an observer learn by itself to model other agents from few observations, without a hand-built model of rational planning? The authors build the ToMnet (a "Theory of Mind network", a neural observer), which meta-learns (learns to learn) across many agents. Its weights act as a general prior, and an embedding computed from one agent's past behaviour acts as an agent-specific posterior. In gridworlds it approximates Bayes-optimal inference for random agents, infers goals, models deep-RL agents, and predicts that agents act on false beliefs when changes happen out of their sight. A further variant reports beliefs explicitly. The authors stress that the experiments are simple, and scaling is open.

**Prerequisites:** POMDPs (tasks where the agent sees only part of the state) and policies; gridworlds (grid-shaped toy environments); embeddings (learned vector summaries); Bayesian posterior/prior; Dirichlet distribution; value iteration; KL and Jensen-Shannon divergence; basic deep learning (embeddings, LSTM).

## L2 — Key ideas (5–10 bullets)
- Machine ToM is framed as meta-learning. Weights give a "general theory of mind" (prior); an embedding from one agent's observations gives an "agent-specific theory of mind" (posterior) (pdf 2).
- The architecture has a character net, a mental state net and a prediction net, trained end to end. The core design is not changed across agent species, only its capacity (pdf 3).
- On random agents, the ToMnet approximates Bayes-optimal online inference of policies and learns species-level priors, including bimodal ones (pdf 3).
- On goal-directed agents it infers preferences from partial traces, with accuracy comparable to Bayesian IRL (inverse reinforcement learning, which recovers rewards from behaviour) in one test. It also infers cost-sensitive "subspecies" (pdf 4).
- For deep-RL agents it infers species implicitly. With a variational information bottleneck (a penalty that forces the embedding into a compact, noisy code), embeddings disentangle, and it finds an unexpected substructure: right-hand vs left-hand wall-followers (pdf 5).
- In the false-belief tests, it predicts that agents largely ignore changes outside their view (with a soft rather than hard boundary). The authors read this as an implicit separation of what the observer knows from what the agent can know (pdf 7).
- The authors conclude that representational ToM can arise simply from observing competent agents in POMDPs, and judge it unlikely to be due to the architecture itself (pdf 8).
- An explicit belief-reporting variant needs supervised belief labels, so the authors expect it will likely not scale as is (pdf 8).

## L3 — Walkthrough

### 1. Introduction (pdf 1–2)
- Humans predict strangers' behaviour with high-level models that say little about true underlying structure. They represent mental states such as desires and beliefs. Human understanding is judged by how well it enables prediction and planning, not by matching mechanistic ground truth (pdf 1).
- Goal: a system that *learns* to model other agents from limited data. It does not assert a generative model of behaviour plus an inversion algorithm (pdf 1).
- Contrast with earlier work: hand-crafted noisy-rational planner models (inverse RL, Bayesian ToM, game theory); work expecting known strong parametric models (Foerster et al., Everett); and concurrent work assuming others are functionally identical to oneself (Raileanu et al.). Here: very weak assumptions, learned via meta-learning (pdf 1).
- The authors say a main message is that many initial challenges can be cast as simple learning problems when formulated in the right way (pdf 1).
- Setup: at test time the observer meets a novel agent with a rich prior, then forms a posterior from observed behaviour. Over training it should get better at forming predictions from limited data ("learning to learn") (pdf 2).
- Two concepts: the *general theory of mind* is the learned network weights. The *agent-specific theory of mind* is the "agent embedding" formed from one agent's observations. They correspond to a prior and a posterior over behaviour (pdf 2).
- The experiments are inspired by Bayesian ToM work but do not replicate it. Alignment with human judgements is left as future work (pdf 2).

*Intuition note:* The network's weights hold what is common to all agents it has seen. The embedding holds what is special about the agent in front of it.

### 2. Model (pdf 2–3)
**2.1 Tasks.**
- A family of POMDPs $\mathcal{M}=\bigcup_j \mathcal{M}_j$. Rewards, discount factors and observation functions belong to the *agents*, not the POMDPs. Only single-agent POMDPs are used (pdf 2).
- A family of agents $\mathcal{A}=\bigcup_i \mathcal{A}_i$. Policies may be stochastic, algorithmic or learned. They are not assumed optimal. Hidden states do not carry over between episodes (pdf 2).
- POMDPs are 11×11 gridworlds with actions up/down/left/right/stay, deterministic dynamics and consumable objects. Walls, objects and start positions are randomly sampled (pdf 2).
- Agent $\mathcal{A}_i$ on $\mathcal{M}_j$ produces $\tau_{ij}=\{(s_t,a_t)\}_{t=0}^T$. The observer sees $\tau^{(obs)}_{ij}=\{(x^{(obs)}_t,a^{(obs)}_t)\}_{t=0}^T$. In all experiments it has unrestricted access to the MDP state and the agents' actions, but not to parameters, rewards, policies or identifiers (pdf 2).
- Training: the observer sees $\{\tau_{ij}\}_{j=1}^{N_{\text{past}}}$ from one unlabelled agent ($N_{\text{past}}$ varies, may be zero). It then predicts behaviour, and possibly latent states such as beliefs, in a "current episode" in $\mathcal{M}_k$. It may be seeded with a partial trajectory up to time $t$ (pdf 2).
- This resembles one-shot imitation, but the observer need not execute the behaviour. The "teacher" may know less about the environment than the "student" and may carry systematic biases (pdf 3).

**2.2 Architecture (Fig. 1).**
- *Character net*: past trajectories $\{\tau^{(obs)}_{ij}\}_{j=1}^{N_{\text{past}}}\to e_{\text{char}}$ (pdf 3).
- *Mental state net*: current trajectory up to $t-1\to e_{\text{mental}}$ (pdf 3).
- *Prediction net*: embeddings plus current state $\to$ next-step action policy $\hat\pi$, object-consumption probabilities $\hat c$, and successor representations $\widehat{SR}$ (pdf 3).
- Trained end to end. The core architecture and algorithm are unchanged across species, only its capacity (pdf 3). Layer shapes are in appendices not provided here.

### 3. Experiments (pdf 3–8)
**3.1 Random agents (pdf 3).**
- Each agent has a fixed action-probability vector $\boldsymbol\pi_i$. In species $\mathcal{S}(\alpha)$, $\boldsymbol\pi_i\sim\text{Dirichlet}(\alpha)$. Small $\alpha$ gives deterministic policies, large $\alpha$ stochastic ones. The mental net is omitted (pdf 3).
- Trained on one species, the ToMnet learns to approximate Bayes-optimal online inference about policies. Predictions for the observed action rise with more past episodes, and lower $\alpha$ gives sparser priors (Fig. 2a) (pdf 3).
- It predicts best on the species it was trained on (Fig. 2b). Trained on a mixture ($\alpha=0.01$ and $\alpha=3$), it learns the bimodal expectation. It learns about two species, not two agents (pdf 3).
- The 2-D embedding $e_{\text{char}}$ segregates agents along canonical directions by their 5-dim empirical action counts (Fig. 2c) (pdf 3).

*Intuition note:* Without being told Bayes' rule, the network behaves like a Bayesian observer whose prior matches the agents it has met. The general theory is the prior. The embedding is the sufficient summary of one agent (pdf 3–4).

**3.2 Goal-directed behaviour (pdf 4).**
- Agents have a fixed reward over four objects and plan with value iteration, with full observability. Three experiments follow (pdf 4).
- (1) One full past trajectory, then a query on a new MDP. The ToMnet predicts the next action, object consumption and successor representations (expected discounted state occupancy). Predictions qualitatively matched true behaviour (Fig. 3) (pdf 4).
- (2) Only single observation-action pairs, $N_{\text{past}}\sim\mathcal{U}\{0,10\}$. With $N_{\text{past}}=0$ there is a strong species prior. More observations improve prediction, with results comparable to Bayesian IRL (BIRL) (Fig. 4) (pdf 4).
- Open question: scaling. Since the ToMnet does not specify the generative model, a bias/variance argument applies. It will have higher sample complexity than BIRL when agents truly are noisy-rational utility maximisers, but it can handle richer populations (pdf 4).
- The ToMnet is not constrained to infer reward functions explicitly, yet 2-D embeddings show the preferred object clearly (Fig. 4d) (pdf 4).
- (3) 20% of agents get a very high move cost (0.5), so they tend to seek the closest object. With $N_{\text{past}}\sim\mathcal{U}\{0,5\}$ full trajectories, the ToMnet infers the subspecies from even one trajectory (Fig. 5). The authors liken this to children jointly reasoning about costs and rewards (pdf 4).

**3.3 Deep RL agents (pdf 5–6).**
- Three species in subgoal gridworlds: max reward for the subgoal first, then an agent-specific preferred object. Consuming a non-subgoal object ends the episode. All use UNREAL: *blind* (sees only $a_{t-1}$, $r_{t-1}$, LSTM), *sighted but stateless* (5×5 window, feed-forward), *sighted and stateful* (5×5, LSTM) (pdf 5).
- Training: 120 trained agents (3 species × 4 objects × 10 seeds), tested on 120 more. Both character and mental nets are needed (pdf 5).
- Without species labels, the ToMnet infers species and predicts SRs. Blind agents continue until a wall, stateless agents consume objects opportunistically, stateful agents explore and seek the subgoal (Fig. 6) (pdf 5).
- With $e_{\text{char}}\in\mathbb{R}^8$ the embedding had no discernible structure. The authors suspect this is due to the deep prediction net and no pressure to compress. Replacing $e_{\text{char}}$ with Gaussian posteriors $q(e_{\text{char}}|\cdot)$ under a variational information bottleneck disentangled factors (Fig. 7). Dimensions 1–2 encode species, 3–4 the preferred object, and the remaining four collapse to the prior (pdf 5–6).
- It split sighted/stateless agents into two clusters, which the authors explain as the right-hand and left-hand wall-following rules (Fig. 8) (pdf 5).

**3.4 Acting on false beliefs (pdf 6–8).**
- A false-belief understanding is called the most celebrated indicator of rich ToM (pdf 5–6).
- *Swap events*: on stepping on the subgoal, with probability $p=0.1$, the four other objects permute locations. They affect an agent's policy only if within its field of view. Out of view, the policy at the next step is unaffected, which the authors call a signature of a false belief. Over time agents show corrective behaviour (Fig. 9). The agents were competent but not optimal (pdf 6).
- ToMnet trained on 40 sighted/stateful agents (4 objects × 10 seeds), tested on 40 held out. It predicts only behaviour, so a Sally-Anne variant is used (pdf 6).
- *Sally-Anne gridworld*: the agent sees its blue object, must leave for the subgoal, then return. A swap may move the object, and the agent sees it only if the subgoal is close. Agents are forced off-policy along the path. The effect is
$$\Delta\pi_L=\frac{\pi(a_L\mid\text{no swap})-\pi(a_L\mid\text{swap})}{\pi(a_L\mid\text{no swap})}\times100\%.$$
True agents: if swap distance ≤ 2, they do not return left; otherwise the policy is unchanged (Fig. 10b) (pdf 7).
- The ToMnet observes the full state, so it knows of swaps the agent does not. It predicted the right behaviours: far-away changes do not affect the agent. The authors say it must have implicitly learned to separate what it knows from what the agent can plausibly know (pdf 7).
- *Natural test*: swaps over many mazes, using only episodes where the agent had seen its preferred object. Ground truth is the Jensen-Shannon divergence $D_{JS}$ between action probabilities with and without a swap. True 5×5 agents change within about 2 blocks. The ToMnet learned local sensitivity and out-of-sight invariance, but with a soft boundary, more liberal about far-off changes (Fig. 11a). It predicted corrective behaviour too (Fig. A3a) (pdf 7).
- On mixed populations with different fields of view, the ToMnet infers each agent's view from past behaviour (Fig. 11b). It learned these statistics even if it never saw swap events in training (Fig. A4) (pdf 7–8).
- Authors' conclusion: the ToMnet learns an implicit understanding that agents act on their own representations, even when wrong. This is unlikely due to the straightforward architecture. Representational ToM can arise simply by observing competent agents in POMDPs (pdf 8).

*Intuition note:* The network never sees a "belief" label here. It appears to learn, at least approximately, that behaviour follows what an agent could have seen rather than what is true (with a soft, not hard, visibility boundary).

**3.5 Explicit belief inference (pdf 8).**
- UNREAL agents were trained to also report object and subgoal locations each step. These readouts are from the LSTM state and not causal to the policy. A single ToMnet, trained on agents with several fields of view and seeing only overt behaviour, predicts policy, consumption, SRs and reported beliefs (pdf 8).
- The ToMnet captures that agents with less visibility of changes in their world are more likely to report false beliefs and behave according to them too (Fig. 12). With an information bottleneck, embeddings separate field of view and preferred object. Blind and 3×3 agents are easily distinguished, while there is little in past behaviour to separate 7×7 from 9×9 agents (or little benefit in making this distinction) (pdf 8).
- Limits: this construction will likely not scale as is. It needs access to others' latent belief states for supervision; here these are given via a rich communication channel, which in the real world is likely much sparser. Predicting beliefs about every aspect of the world is intractable, and may need abstract queryable embeddings (pdf 8).

### 4. Discussion (pdf 8)
- Claimed: meta-learning yields a general model plus online agent-specific models, with few assumptions, and can discover abstractions in behaviour space (pdf 8).
- The authors call their experiments simple and designed to illustrate the core ideas, and say there is much work to do to scale the ToMnet (pdf 8).
- Future work listed: richer domains (e.g. 3D); limiting the observer's own observability; other dimensions (prosocial/adversarial, reactive/planning); discovering structure in natural or artificial populations; embedding ToMnets in multi-agent decision-makers; more data efficiency; inductive biases; drawing on one's own cognition (pdf 8).

## Toy example (ours, not from the paper)
Illustrates the Bayes-optimal inference the ToMnet is said to approximate on random agents (pdf 3).
- Species has two agent types, equally likely: Type U picks "up" with probability 0.9; Type D picks "up" with probability 0.1.
- Prior predictive ($N_{\text{past}}=0$): $0.5\cdot0.9+0.5\cdot0.1=0.5$.
- Observe one "up". Posterior for U: $\frac{0.5\cdot0.9}{0.5\cdot0.9+0.5\cdot0.1}=\frac{0.45}{0.50}=0.9$.
- New prediction of "up" next time: $0.9\cdot0.9+0.1\cdot0.1=0.81+0.01=0.82$, up from 0.5. The "embedding" here is just the posterior 0.9.
- $\Delta\pi_L$ check: if $\pi(a_L\mid\text{no swap})=0.8$ and $\pi(a_L\mid\text{swap})=0.2$, then $\Delta\pi_L=(0.8-0.2)/0.8\times100\%=75\%$. If the policy is unchanged (0.8 vs 0.8), $\Delta\pi_L=0\%$, the false-belief signature.

## Concepts
- [[machine theory of mind]] (new) — a system that learns to model other agents from limited data, with weak generative assumptions (pdf 1)
- [[meta-learning]] (new) — learning across many agents so inference on a new agent is fast and sample-efficient (pdf 2)
- [[character embedding]] (new) — vector $e_{\text{char}}$ from past episodes; the "agent-specific theory of mind" (pdf 2–3)
- [[general vs agent-specific theory of mind]] (new) — prior (weights) vs posterior (embedding) over agent behaviour (pdf 2)
- [[POMDP]] — environment family with rewards and observation functions attached to agents (pdf 2)
- [[Bayesian theory of mind (BToM)]] — hand-crafted noisy-rational planner model that this work contrasts with (pdf 1)
- [[inverse reinforcement learning]] — recovering rewards from behaviour; BIRL used as a baseline (pdf 4)
- [[successor representation]] (new) — expected discounted state occupancy, used as a prediction target (pdf 4)
- [[variational information bottleneck]] (new) — replaces embedding vectors with Gaussian posteriors; in these experiments it drove the ToMnet to disentangle factors of variation (pdf 5)
- [[unexpected transfer task]] (new) — the Sally-Anne test, here as a gridworld variant (pdf 6–7)
- [[first-order false belief]] (new) — agent acts on a belief that differs from the true state (pdf 6)
- [[goal-directed behaviour assumption]] (new) — humans' elementary assumption that others' behaviour is goal-directed; the ToMnet does not prespecify a generative model of behaviour (pdf 4)

## Canonical instances
- [[sally-anne-gridworld]] — swap events outside the field of view leave the agent's policy unchanged, and the ToMnet predicts this (pdf 7)
- [[dirichlet-random-agents]] — species $\mathcal{S}(\alpha)$ with Bayes-optimal comparison (pdf 3)
- [[wall-following-subspecies]] — left/right-hand rule agents found by the ToMnet (pdf 5)
- [[high-move-cost-subspecies]] — 20% of agents with cost 0.5 inferred from one trajectory (pdf 4)

## Bridges (candidates)
- [structural-analogy] ToMnet embedding as posterior ↔ Bayesian inference: Bayes-optimal posterior over agent type — compared with Bayes-optimal curves only in the Dirichlet case (pdf 3)
- [structural-analogy] ToMnet vs BIRL ↔ statistics: bias/variance trade-off between a fixed generative model and a flexible learner (pdf 4)
- [structural-analogy] Sally-Anne gridworld ↔ developmental psychology: predicting where an agent will go, not asking what it believes (pdf 7)
- [metaphor] Information bottleneck on $e_{\text{char}}$ ↔ discovering latent "personality" factors (pdf 5–6)

## Questions this raises
- Does passing the swap tests show a belief representation, or only the learned statistics of visibility? The authors say "implicit" (pdf 7–8).
- What would a ToMnet need when the observer's own observability is limited (pdf 8)?
- How could belief supervision be made sparse or unnecessary (pdf 8)?
- Do the results hold in richer environments than 11×11 gridworlds (pdf 8)?

## Reading notes
- Page labels give no printed page numbers and none are visible in the images, so all citations use pdf pages (pdf 1–10). The unit metadata (not the pages themselves) gives the citation pages as pp. 4218–4227.
- The text refers to "Fig 2d" (pdf 3), but the caption lists only panels (a)–(c) (pdf 3).
- Appendices (the pages cite Appendices A, C, D and F, and Figs A1–A6) are not included. Network layer sizes, losses and hyperparameters are therefore not digested. The footnote points to an extended arXiv version (pdf 1).
- Whether the "BIRL" comparison in Fig. 4c has the ToMnet matching or exceeding BIRL is only stated as "comparable" (pdf 4).
