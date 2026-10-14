---
id: rafailov-2023-dpo/main
work: rafailov-2023-dpo
unit: paper
pages: 1-27
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

## L0 — One line
Under the Bradley–Terry preference model, the KL-constrained RLHF problem can be solved exactly by training the language model with a simple binary classification loss on preference pairs, with no separate reward model and no reinforcement learning.

## L1 — The gist (≤ 120 words)
RLHF (reinforcement learning from human feedback) aligns a language model with human preferences by fitting a reward model and then running reinforcement learning (RL). This is complex and often unstable. The paper asks whether the same KL-constrained reward-maximization problem can be solved without either step. Answer: the reward can be rewritten as β times a log-ratio between the policy and a reference policy. The preference loss then becomes a classification loss on the policy itself. This is Direct Preference Optimization (DPO). In the authors' experiments on sentiment, summarization and dialogue (models up to 6B parameters), DPO performs as well as or better than PPO-based RLHF. It is also much simpler to implement and train.

**Prerequisites:** logistic/sigmoid function; maximum likelihood; KL divergence; the idea that a language model defines a policy π(y|x); basic RLHF vocabulary (reward model, PPO); sums over discrete outcomes; gradients of log-probabilities.

## L2 — Key ideas (5–10 bullets)
- **Goal.** Optimize a language model to follow human preferences without fitting a reward model and without RL sampling in the training loop (p. 2).
- **Closed-form optimum.** The KL-constrained reward-maximization objective has the optimal policy $\pi_r \propto \pi_{\text{ref}}\exp(r/\beta)$. Inverting it gives $r = \beta\log(\pi_r/\pi_{\text{ref}}) + \beta\log Z(x)$ (p. 4).
- **Change of variables.** The Bradley–Terry model uses only reward differences, so the normalizer $Z(x)$ (the partition function) cancels. The preference loss can then be written in terms of the policy alone (Eq. 7, p. 4).
- **Gradient.** The DPO gradient raises the likelihood of the preferred answer and lowers that of the dispreferred one. Each example is weighted more when the implicit reward orders the pair wrongly (p. 5).
- **No loss of generality.** Under mild assumptions (for uniqueness: $\pi_{\text{ref}}>0$ and $\beta>0$), every reward class consistent with Plackett–Luce/Bradley–Terry has exactly one member of the form $\beta\log(\pi/\pi_{\text{ref}})$ (Theorem 1, Prop. 1; pp. 6, 18–19).
- **Diagnosis of actor-critic.** The PPO-style objective contains a normalizer that acts like a soft value function. Without it the gradient may have high variance. The DPO reward needs no baseline (p. 6).
- **Empirical results.** Experiments on three tasks (sentiment, summarization, dialogue) report DPO as at least as good as PPO (pp. 7–9). One GPT-4-judged summarization comparison: DPO about 61%, PPO 57% (p. 9).
- **Judge validity.** In a human study, GPT-4 tended to agree with humans about as often as humans agree with each other, which the authors take to suggest it is a reasonable proxy (p. 10).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–2)
- Large unsupervised LMs learn broad knowledge, but precise control is hard because training is unsupervised (p. 1).
- The authors want to bias a model toward the high-quality behavior in its training data. Their example: the model should know a misconception held by 50% of people without asserting it in 50% of answers (p. 1).
- RLHF (reinforcement learning from human feedback) is the "most successful class" of methods. It fits a reward model to human preferences, then uses RL to maximize reward without drifting far from the original model. Its pipeline trains multiple LMs and samples from the policy during training, which is costly (p. 2).
- DPO "implicitly optimizes the same objective" as RLHF algorithms (reward maximization with a KL constraint). It uses a change of variables to define the preference loss as a function of the policy directly (p. 2).
- The DPO update raises the relative log probability of preferred over dispreferred responses. It adds a dynamic per-example importance weight. The authors say this weight prevents the degeneration they find with a naive probability-ratio objective (p. 2).
- Claim: DPO is at least as effective as existing methods, including PPO-based RLHF, on sentiment modulation, summarization and dialogue, with models up to 6B parameters (p. 2).

### 2 Related Work (pp. 2–3)
- Instruction tuning on human-written completions improves LMs. Relative human judgments are often easier to collect than expert demonstrations, so later work fine-tunes with preference data (p. 2).
- Existing methods first fit a reward function under a preference model such as Bradley–Terry. Then they run RL (REINFORCE, PPO or variants). Related work generates synthetic preference data from LLMs guided by a text rubric (p. 3).
- In contextual dueling bandits, the optimal policy is replaced by a *von Neumann winner*: a policy whose expected win rate against any other policy is at least 50%. Their preference labels arrive online, whereas LLM preference learning uses a fixed offline batch (p. 3).
- Preference-based RL (PbRL) generally first estimates the latent scoring function and then optimizes it. DPO instead is a single-stage policy-learning approach (p. 3).

### 3 Preliminaries: the RLHF pipeline (pp. 3–4)
The pipeline has three phases (p. 3).

**SFT.** Fine-tune a pre-trained LM with supervised learning on high-quality task data to get $\pi^{\text{SFT}}$ (p. 3).

**Reward modelling.** Prompt $\pi^{\text{SFT}}$ with $x$ to get pairs $(y_1,y_2)\sim\pi^{\text{SFT}}(y\mid x)$. Humans mark a preferred $y_w$ and a dispreferred $y_l$, written $y_w\succ y_l\mid x$. Preferences are assumed to come from a latent reward $r^*(y,x)$ that we cannot access (p. 3). The Bradley–Terry (BT) model stipulates:
$$p^*(y_1\succ y_2\mid x)=\frac{\exp(r^*(x,y_1))}{\exp(r^*(x,y_1))+\exp(r^*(x,y_2))}\tag{1}$$
The more general Plackett–Luce ranking models are also compatible if several ranked answers are available (p. 3). With a static dataset $\mathcal D=\{x^{(i)},y_w^{(i)},y_l^{(i)}\}_{i=1}^N$, a reward model $r_\phi$ is fit by maximum likelihood, framed as binary classification (σ is the logistic function):
$$\mathcal L_R(r_\phi,\mathcal D)=-\mathbb E_{(x,y_w,y_l)\sim\mathcal D}\big[\log\sigma(r_\phi(x,y_w)-r_\phi(x,y_l))\big]\tag{2}$$
In LMs, $r_\phi$ is often initialized from $\pi^{\text{SFT}}$ plus a linear layer giving one scalar. Prior work normalizes rewards so that $\mathbb E_{x,y\sim\mathcal D}[r_\phi(x,y)]=0$ for all $x$ (p. 3).

**RL fine-tuning.** The learned reward is used in:
$$\max_{\pi_\theta}\ \mathbb E_{x\sim\mathcal D,\,y\sim\pi_\theta(y|x)}\big[r_\phi(x,y)\big]-\beta\,\mathbb D_{\text{KL}}\big[\pi_\theta(y\mid x)\,\|\,\pi_{\text{ref}}(y\mid x)\big]\tag{3}$$
Here $\pi_{\text{ref}}$ is the initial SFT model and $\pi_\theta$ is also initialized to it. The constraint keeps the policy where the reward model is accurate. It also keeps generation diverse and prevents mode collapse to single high-reward answers (p. 4). Language generation is discrete, so the objective is not differentiable. The standard approach builds $r(x,y)=r_\phi(x,y)-\beta(\log\pi_\theta(y|x)-\log\pi_{\text{ref}}(y|x))$ and maximizes it with PPO (p. 4).

### 4 Direct Preference Optimization (pp. 4–5)
**Key insight:** use an analytical mapping from reward functions to optimal policies, which turns a loss over rewards into a loss over policies. The policy network then represents both the LM and the implicit reward (p. 4).

**Optimal policy.** For a general reward $r$, the optimum of Eq. 3 is (derivation in A.1):
$$\pi_r(y\mid x)=\frac{1}{Z(x)}\pi_{\text{ref}}(y\mid x)\exp\!\Big(\frac1\beta r(x,y)\Big)\tag{4}$$
with partition function $Z(x)=\sum_y\pi_{\text{ref}}(y|x)\exp(\tfrac1\beta r(x,y))$. Even with the MLE reward $r_\phi$, $Z(x)$ is expensive to estimate, so Eq. 4 is hard to use directly (p. 4). Taking logs and rearranging:
$$r(x,y)=\beta\log\frac{\pi_r(y\mid x)}{\pi_{\text{ref}}(y\mid x)}+\beta\log Z(x)\tag{5}$$
**Cancelling $Z$.** The BT model depends only on reward differences: $p^*(y_1\succ y_2|x)=\sigma(r^*(x,y_1)-r^*(x,y_2))$. Substituting Eq. 5 for $r^*$, $Z(x)$ cancels. The optimal RLHF policy $\pi^*$ under BT then satisfies (derivation in A.2):
$$p^*(y_1\succ y_2\mid x)=\frac{1}{1+\exp\!\Big(\beta\log\frac{\pi^*(y_2|x)}{\pi_{\text{ref}}(y_2|x)}-\beta\log\frac{\pi^*(y_1|x)}{\pi_{\text{ref}}(y_1|x)}\Big)}\tag{6}$$
A Plackett–Luce version is in A.3 (p. 4).

**DPO loss.** Maximum likelihood for a parametrized policy gives (p. 4):
$$\mathcal L_{\text{DPO}}(\pi_\theta;\pi_{\text{ref}})=-\mathbb E_{(x,y_w,y_l)\sim\mathcal D}\Big[\log\sigma\Big(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)}-\beta\log\frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\Big)\Big]\tag{7}$$
This fits an implicit reward whose optimal policy is $\pi_\theta$. Since it equals fitting a reparametrized BT model, it has properties such as consistency under suitable assumptions on the preference data distribution (pp. 4–5).

*Intuition note.* Compare the policy with the reference. Ask how much more the policy has raised the preferred answer than the dispreferred one. DPO trains that gap to be positive using ordinary logistic regression. The KL constraint is built in through the reference model, so no RL loop is needed.

**What the update does.** The gradient is (derivation in A.4; p. 5):
$$\nabla_\theta\mathcal L_{\text{DPO}}=-\beta\,\mathbb E_{(x,y_w,y_l)\sim\mathcal D}\Big[\underbrace{\sigma(\hat r_\theta(x,y_l)-\hat r_\theta(x,y_w))}_{\text{higher weight when reward estimate is wrong}}\Big[\underbrace{\nabla_\theta\log\pi(y_w|x)}_{\text{increase likelihood of }y_w}-\underbrace{\nabla_\theta\log\pi(y_l|x)}_{\text{decrease likelihood of }y_l}\Big]\Big]$$
Here $\hat r_\theta(x,y)=\beta\log\frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$ is the implicit reward. Examples are weighted by how much higher $\hat r_\theta$ rates the dispreferred completion, scaled by β. In the authors' experiments, a naive version without the weight can make the LM degenerate (Appendix Table 3) (p. 5).

*Intuition note.* Pairs the model already orders correctly get a small weight. Pairs it orders wrongly get a large weight. The authors say this weight prevents the model degeneration they found with a naive probability-ratio objective (pp. 2, 5).

**Pipeline** (p. 5):
1. Sample $y_1,y_2\sim\pi_{\text{ref}}(\cdot|x)$ for each prompt and label with human preferences, giving an offline dataset $\mathcal D$.
2. Minimize $\mathcal L_{\text{DPO}}$ for the given $\pi_{\text{ref}}$, $\mathcal D$ and β.

Public preference datasets are reused. Their samples come from $\pi^{\text{SFT}}$, so set $\pi_{\text{ref}}=\pi^{\text{SFT}}$ when available. Otherwise set $\pi_{\text{ref}}=\arg\max_\pi\mathbb E_{x,y_w\sim\mathcal D}[\log\pi(y_w|x)]$. This helps reduce the shift between the unavailable true reference distribution and the $\pi_{\text{ref}}$ used (p. 5).

### 5 Theoretical Analysis (pp. 5–6)

#### 5.1 Your language model is secretly a reward model
**Definition 1.** Two reward functions $r,r'$ are *equivalent* iff $r(x,y)-r'(x,y)=f(x)$ for some function $f$. This partitions reward functions into classes (p. 5).

**Lemma 1.** Under Plackett–Luce (in particular Bradley–Terry), two rewards from the same class induce the same preference distribution (p. 5). This is a known under-specification of Plackett–Luce, which usually forces extra identifiability constraints (pp. 5–6).

**Lemma 2.** Two rewards from the same class induce the same optimal policy under the constrained RL problem (p. 5). So for the final objective we only need *some* reward from the optimal class (p. 6). Proofs are in A.5.

**Theorem 1.** Under mild assumptions, all reward classes consistent with Plackett–Luce (and BT in particular) can be represented as $r(x,y)=\beta\log\frac{\pi(y|x)}{\pi_{\text{ref}}(y|x)}$ for some model $\pi(y|x)$ and a given $\pi_{\text{ref}}$ (p. 6).

*Proof sketch (p. 6).* Take any $r$, with optimal model $\pi_r$ from Eq. 4. Define the projection
$$f(r;\pi_{\text{ref}},\beta)(x,y)=r(x,y)-\beta\log\sum_y\pi_{\text{ref}}(y|x)\exp\!\Big(\frac1\beta r(x,y)\Big)\tag{8}$$
It subtracts the log partition function, which depends only on $x$, so $f(r)$ is in the class of $r$. Replacing $r$ by the right side of Eq. 5 gives $f(r;\pi_{\text{ref}},\beta)(x,y)=\beta\log\frac{\pi_r(y|x)}{\pi_{\text{ref}}(y|x)}$. So the class is represented, with no loss of generality (p. 6).

Equivalently, the reparameterization picks the reward in each class that satisfies (p. 6):
$$\sum_y\pi_{\text{ref}}(y|x)\exp\!\Big(\frac1\beta r(x,y)\Big)=1\tag{9}$$
Then $\pi(y|x)$ is a valid distribution. By Eq. 4, the left side is the partition function of the optimal policy for $r$. So the constraint preserves the representable reward class but makes the optimal policy analytically tractable for all $x$ (p. 6).

*Intuition note.* Rewards that differ only by a prompt-dependent constant are indistinguishable from preference data. DPO fixes the constant so that the "policy" implied by the reward sums to 1. Nothing expressible is lost.

#### 5.2 Instability of actor-critic algorithms
- Following the control-as-inference view, assume $\pi_\theta$ and minimize $\mathbb D_{\text{KL}}[\pi_\theta\|\pi^*]$. The text calls $\pi^*$ the optimal policy "from Eq. 7"; the optimal-policy form is Eq. 4 (see Reading notes). With some algebra this gives (p. 6):
$$\max_{\pi_\theta}\mathbb E_{\pi_\theta(y|x)}\Big[\underbrace{r_\phi(x,y)-\beta\log\sum_y\pi_{\text{ref}}(y|x)\exp\!\big(\tfrac1\beta r_\phi(x,y)\big)}_{f(r_\phi,\pi_{\text{ref}},\beta)}-\underbrace{\beta\log\frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}}_{\text{KL}}\Big]\tag{10}$$
- This is the objective optimized in prior work, using the DPO-equivalent reward for the class of $r_\phi$. The normalization term can be read as the soft value function of $\pi_{\text{ref}}$. It does not change the optimal solution. Without it, the policy gradient could have high variance and make learning unstable (p. 6).
- A learned value function can be difficult to optimize. Prior work used a human-completion baseline, which is essentially a single-sample Monte-Carlo estimate of the normalizer. The DPO reward "does not require any baselines" (p. 6).

### 6 Experiments (pp. 7–10)
**Tasks** (p. 7):
- *Controlled sentiment.* $x$ is an IMDb movie-review prefix. The policy must generate positive text. Preference pairs are generated with a pre-trained sentiment classifier, with $p(\text{positive}|x,y_w)>p(\text{positive}|x,y_l)$. SFT is GPT-2-large fine-tuned on IMDb train reviews.
- *Summarization.* $x$ is a Reddit forum post. The data is Reddit TL;DR with human preferences from Stiennon et al. The preferences were gathered on samples from a different, similarly trained SFT model.
- *Single-turn dialogue.* $x$ is a human query. The data is the Anthropic Helpful and Harmless set (170k dialogues). No SFT model is available, so an off-the-shelf LM is fine-tuned on the preferred completions only.

**Evaluation** (pp. 7–8). For sentiment, the ground-truth reward is a classifier. Each algorithm is evaluated by its reward–KL frontier. For summarization and dialogue the true reward is unknown, so the metric is the win rate against a baseline, with GPT-4 as a proxy for humans. The baseline is the test-set reference summary (summarization) or the preferred response (dialogue).

**Methods** (p. 8):
- Zero-shot GPT-J (summarization) and 2-shot Pythia-2.8B (dialogue).
- The SFT model, and Preferred-FT (supervised fine-tuning on $y_w$).
- Unlikelihood, which maximizes the probability of $y_w$ and minimizes that of $y_l$, with coefficient $\alpha\in[0,1]$.
- PPO with a learned reward, and PPO-GT, an oracle using the true reward in sentiment (two implementations; the modified one normalizes rewards and tunes hyperparameters).
- Best of $N$: sample $N$ responses and return the one the learned reward ranks highest. It is strong but impractical because it needs $N$ samples per query at test time.

**6.1 How well can DPO optimize the RLHF objective?** (pp. 8–9)
- Runs sweep target KL ∈ {3, 6, 9, 12} for PPO, β ∈ {0.05, 0.1, 1, 5} for DPO, α ∈ {0.05, 0.1, 0.5, 1} for unlikelihood, and random seeds for Preferred-FT. This is 22 runs in total.
- Every 100 steps until convergence, each policy is evaluated for mean true reward and mean sequence-level KL (the sum of per-timestep KLs) (p. 8).
- Result (Fig. 2 left): DPO has "by far the most efficient frontier". It has the highest reward at low KL. Its trade-off "strictly dominates" PPO, even when PPO has ground-truth rewards (PPO-GT). The two optimize the same objective (pp. 8–9).

**6.2 Real preference datasets** (p. 9)
- *Summarization* (Fig. 2 right, GPT-4 win rate vs reference summaries): DPO reaches about 61% at temperature 0.0. PPO reaches 57% at its best temperature (0.0). DPO also exceeds the Best-of-$N$ maximum. β was not meaningfully tuned, so the authors say this may underestimate DPO.
- PPO can degrade to the base GPT-J level at high temperatures. Preferred-FT does not improve significantly over SFT.
- In a human head-to-head, DPO at temperature 0.25 was preferred 58% of the time over PPO at temperature 0.
- *Dialogue:* the reference model is Pythia-2.8B fine-tuned (Preferred-FT) on chosen completions. DPO performs as well as or better than Best of 128 and the 2-shot baseline at each method's best temperature. Best of $N$ plateaus at 128 here (Appendix Fig. 4).
- A public PPO-trained Anthropic-HH model (from a "well-known source") could not be made to beat base Pythia-2.8B at any prompt or temperature. The authors therefore treat Best of 128 as a rough proxy for PPO-level performance. DPO is "the only computationally efficient method" that improves over the preferred completions, and it converges relatively quickly (Fig. 3).

**6.3 Generalization to a new input distribution** (p. 9). Summarization policies trained on Reddit TL;DR were applied to CNN/DailyMail news articles. The prompt was the GPT-4 (C) prompt with "forum post" replaced by "news article". Win rates vs ground-truth summaries (Table 1):

| Alg. | Temp 0 | Temp 0.25 |
|---|---|---|
| DPO | 0.36 | 0.31 |
| PPO | 0.26 | 0.23 |

The authors call this "initial evidence" that DPO policies generalize similarly well to PPO policies. DPO did not use the unlabeled Reddit TL;DR prompts that PPO uses (p. 9).

**6.4 Validating GPT-4 judgments** (p. 10). Two GPT-4 prompts were used. (S) asks which summary better summarizes the important information. (C) also asks for conciseness, because under (S) GPT-4 prefers longer, more repetitive summaries than humans do. Three methods were each compared with greedy PPO (temperature 0): DPO (temp 0.25), SFT (temp 0.25) and PPO (temp 1.0, "PPO-1"). Only DPO and PPO-1 have multiple human judgments.

| | DPO | SFT | PPO-1 |
|---|---|---|---|
| N respondents | 272 | 122 | 199 |
| GPT-4 (S) win % | 47 | 27 | 13 |
| GPT-4 (C) win % | 54 | 32 | 12 |
| Human win % | 58 | 43 | 17 |
| GPT-4 (S)–H agree | 70 | 77 | 86 |
| GPT-4 (C)–H agree | 67 | 79 | 85 |
| H–H agree | 65 | – | 87 |

GPT-4 tends to agree with humans about as often as humans agree with each other, which the authors say suggests it is a reasonable proxy for human evaluation. The (C) prompt gives win rates more representative of humans, so it is used in Section 6.2 (p. 10).

*Intuition note.* The key claim of the experiments is not just "DPO wins". DPO reaches a better reward at the same distance from the reference model than PPO, even when PPO sees the true reward. The authors read this as DPO being a more efficient optimizer of the same objective.

### 7 Discussion (p. 10)
DPO identifies a mapping between LM policies and reward functions, so the LM can be trained with a cross-entropy loss "without reinforcement learning or loss of generality". It performs similarly or better than existing RLHF with virtually no hyperparameter tuning (p. 10). Open questions listed by the authors:
- How does DPO generalize out of distribution, compared with an explicit reward function?
- Can self-labeling use unlabeled prompts?
- How does reward over-optimization appear, and is the slight performance decrease in Fig. 3 right an instance?
- Does DPO scale to models orders of magnitude larger? Only models up to 6B were tested.
- GPT-4 win rates depend on the prompt.
- Other applications, such as generative models in other modalities (p. 10).

### Appendix A: Mathematical derivations (pp. 15–19)
**A.1 Optimum of the KL-constrained objective (pp. 15–16).** Start from
$$\max_\pi\mathbb E_{x\sim\mathcal D,y\sim\pi}\big[r(x,y)\big]-\beta\mathbb D_{\text{KL}}\big[\pi(y|x)\|\pi_{\text{ref}}(y|x)\big]\tag{11}$$
for any reward $r$, any $\pi_{\text{ref}}$, and a general non-parametric policy class. Then:
$$\begin{aligned}&=\max_\pi\mathbb E_{x}\mathbb E_{y\sim\pi}\Big[r(x,y)-\beta\log\frac{\pi(y|x)}{\pi_{\text{ref}}(y|x)}\Big]\\&=\min_\pi\mathbb E_{x}\mathbb E_{y\sim\pi}\Big[\log\frac{\pi(y|x)}{\pi_{\text{ref}}(y|x)}-\frac1\beta r(x,y)\Big]\\&=\min_\pi\mathbb E_{x}\mathbb E_{y\sim\pi}\Big[\log\frac{\pi(y|x)}{\frac1{Z(x)}\pi_{\text{ref}}(y|x)\exp(\frac1\beta r(x,y))}-\log Z(x)\Big]\end{aligned}\tag{12}$$
$Z(x)$ depends only on $x$ and $\pi_{\text{ref}}$, not on $\pi$. Define $\pi^*(y|x)=\frac1{Z(x)}\pi_{\text{ref}}(y|x)\exp(\frac1\beta r(x,y))$. It is a valid distribution because $\pi^*\ge0$ and $\sum_y\pi^*=1$. Then:
$$\min_\pi\mathbb E_x\Big[\mathbb E_{y\sim\pi}\log\frac{\pi(y|x)}{\pi^*(y|x)}-\log Z(x)\Big]=\min_\pi\mathbb E_x\big[\mathbb D_{\text{KL}}(\pi\|\pi^*)-\log Z(x)\big]\tag{13–14}$$
Gibbs' inequality says KL is minimized at 0 if and only if the two distributions are identical. Since $Z(x)$ does not depend on $\pi$:
$$\pi(y|x)=\pi^*(y|x)=\frac1{Z(x)}\pi_{\text{ref}}(y|x)\exp\!\Big(\frac1\beta r(x,y)\Big)\ \text{ for all }x\in\mathcal D\tag{15}$$

**A.2 DPO objective under Bradley–Terry (p. 16).** Start from Eq. 16 (identical to Eq. 1) and from Eq. 17, which is Eq. 5 applied to $r^*$ and $\pi^*$: $r^*(x,y)=\beta\log\frac{\pi^*(y|x)}{\pi_{\text{ref}}(y|x)}+\beta\log Z(x)$. Substituting, each exponential contains an extra $\beta\log Z(x)$, which factors out and cancels between numerator and denominator. Dividing top and bottom by the numerator (added step) gives
$$p^*(y_1\succ y_2|x)=\frac{1}{1+\exp\big(\beta\log\frac{\pi^*(y_2|x)}{\pi_{\text{ref}}(y_2|x)}-\beta\log\frac{\pi^*(y_1|x)}{\pi_{\text{ref}}(y_1|x)}\big)}=\sigma\Big(\beta\log\frac{\pi^*(y_1|x)}{\pi_{\text{ref}}(y_1|x)}-\beta\log\frac{\pi^*(y_2|x)}{\pi_{\text{ref}}(y_2|x)}\Big)$$
The authors say the last line is the per-instance loss in Eq. 7 (p. 16).

**A.3 Plackett–Luce (pp. 16–17).** Given a prompt $x$ and $K$ answers, a user outputs a ranking $\tau:[K]\to[K]$:
$$p^*(\tau|y_1,\dots,y_K,x)=\prod_{k=1}^K\frac{\exp(r^*(x,y_{\tau(k)}))}{\sum_{j=k}^K\exp(r^*(x,y_{\tau(j)}))}\tag{18}$$
For $K=2$ this reduces to BT. Substituting Eq. 5, $Z(x)$ cancels again:
$$p^*(\tau|y_1,\dots,y_K,x)=\prod_{k=1}^K\frac{\exp\big(\beta\log\frac{\pi^*(y_{\tau(k)}|x)}{\pi_{\text{ref}}(y_{\tau(k)}|x)}\big)}{\sum_{j=k}^K\exp\big(\beta\log\frac{\pi^*(y_{\tau(j)}|x)}{\pi_{\text{ref}}(y_{\tau(j)}|x)}\big)}\tag{19}$$
With a ranking dataset, the maximum-likelihood objective is
$$\mathcal L_{\text{DPO}}(\pi_\theta,\pi_{\text{ref}})=-\mathbb E_{\tau,y_1,\dots,y_K,x\sim\mathcal D}\Big[\log\prod_{k=1}^K\frac{\exp\big(\beta\log\frac{\pi_\theta(y_{\tau(k)}|x)}{\pi_{\text{ref}}(y_{\tau(k)}|x)}\big)}{\sum_{j=k}^K\exp\big(\beta\log\frac{\pi_\theta(y_{\tau(j)}|x)}{\pi_{\text{ref}}(y_{\tau(j)}|x)}\big)}\Big]\tag{20}$$

**A.4 Gradient (p. 17).** The appendix writes
$$\nabla_\theta\mathcal L_{\text{DPO}}=-\nabla_\theta\mathbb E\Big[\log\sigma\Big(\beta\log\frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}-\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)}\Big)\Big]\tag{21}$$
$$=-\mathbb E\Big[\frac{\sigma'(u)}{\sigma(u)}\nabla_\theta(u)\Big],\quad u=\beta\log\tfrac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}-\beta\log\tfrac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)}\tag{22}$$
It then uses $\sigma'(x)=\sigma(x)(1-\sigma(x))$ and $\sigma(-x)=1-\sigma(x)$. It reaches the displayed final gradient, and says that substituting $\hat r_\theta$ gives the Section 4 form (p. 17). The signs in Eqs. 21–22 and in the final display differ from Eq. 7 and from the Section 4 gradient (see Reading notes). The main-text form is the one consistent with Eq. 7. (Added step, checked: with $\Delta=\hat r_\theta(x,y_w)-\hat r_\theta(x,y_l)$ and loss $-\log\sigma(\Delta)$, $\nabla_\theta\mathcal L=-\sigma(-\Delta)\nabla_\theta\Delta$ and $\nabla_\theta\Delta=\beta(\nabla\log\pi_\theta(y_w|x)-\nabla\log\pi_\theta(y_l|x))$.)

**A.5 Proofs of Lemmas 1 and 2 (pp. 17–18).**
- *Lemma 1.* If $r'=r+f(x)$, the Plackett–Luce probability becomes $\prod_k\frac{\exp(f(x))\exp(r(x,y_{\tau(k)}))}{\exp(f(x))\sum_{j\ge k}\exp(r(x,y_{\tau(j)}))}$. The factors $\exp(f(x))$ cancel, giving $p_r$.
- *Lemma 2.* With $r'=r+f(x)$, Eq. 4 gives $\pi_{r'}(y|x)=\frac{1}{\sum_y\pi_{\text{ref}}\exp(\frac1\beta(r+f))}\pi_{\text{ref}}\exp(\frac1\beta(r+f))$. Pull $\exp(\frac1\beta f(x))$ out of both the sum and the numerator. It cancels, giving $\pi_r(y|x)$.

**A.6 Proof of Theorem 1 and Proposition 1 (pp. 18–19).**
- *Theorem 1 restated.* Assume $\pi_{\text{ref}}(y|x)>0$ for all $x,y$ and $\beta>0$. All equivalence classes can be represented as $r=\beta\log\frac{\pi(y|x)}{\pi_{\text{ref}}(y|x)}$ for some $\pi$. Proof: from Eq. 5, $r'=f(r,\pi_{\text{ref}},\beta)=r-\beta\log Z(x)$ lies in the class of $r$ and equals $\beta\log\frac{\pi_r}{\pi_{\text{ref}}}$ (p. 18).
- By Lemma 2, $f$ maps all rewards in a class to the same function: $f(r)=\beta\log\frac{\pi_r}{\pi_{\text{ref}}}=\beta\log\frac{\pi'_r}{\pi_{\text{ref}}}=f(r')$ (p. 18).
- *Proposition 1.* Under the same assumptions, every class has a *unique* reward of the form $\beta\log\frac{\pi}{\pi_{\text{ref}}}$. Proof by contradiction: suppose $r'=r+f(x)$ with $r=\beta\log\frac{\pi}{\pi_{\text{ref}}}$ and $r'=\beta\log\frac{\pi'}{\pi_{\text{ref}}}$. Then $\pi(y|x)\exp(\frac1\beta f(x))=\pi'(y|x)$. Summing over $y$ gives $\exp(\frac1\beta f(x))=1$, so $f(x)=0$ since $\beta>0$, hence $r=r'$ (p. 19).

### Appendix B: Implementation (pp. 19–20)
The loss is a few lines of PyTorch. Inputs: `pi_logps`, `ref_logps` of shape (B,) (sequence log-probabilities); `yw_idxs`, `yl_idxs` of shape (T,) index the preferred and dispreferred completions. The code computes `pi_logratios = pi_yw − pi_yl`, `ref_logratios = ref_yw − ref_yl`, then `losses = −logsigmoid(beta·(pi_logratios − ref_logratios))`, which is Eq. 7 per pair. It also returns `rewards = beta·(pi_logps − ref_logps).detach()` (p. 20). Defaults: β = 0.1, batch size 64, RMSprop, learning rate 1e-6 with linear warmup from 0 over 150 steps. For TL;DR summarization β = 0.5 (p. 20).

### Appendix C: Experimental set-up (pp. 20–22)
- *C.1 IMDb.* Prompts are 2–8-token prefixes. The ground-truth reward is `siebert/sentiment-roberta-large-english`, and the base model is `gpt2-large`. SFT runs 1 epoch on a subset of IMDb. They sample 4 completions for each of 25,000 prefixes and build 6 preference pairs per prefix with the ground-truth reward. The RLHF reward model starts from gpt2-large and trains 3 epochs, keeping the best validation-accuracy checkpoint. The authors' PPO uses batches of 1024 per PPO step. The "TRL" run uses the TRL library's hyperparameters (p. 20).
- *C.2 GPT-4 prompts.* `gpt-4-0314` is used, with the order of the two candidates randomized each time. The (S), (C) and dialogue prompts are printed. Each asks for a one-sentence comparison and then "A" or "B" (pp. 20–21).
- *C.3 Unlikelihood.* Unlikelihood is included as a baseline only in the sentiment experiments (Table 3 shows its samples on TL;DR prompts). In summarization and dialogue it produces "generally meaningless responses", which the authors believe results from unconstrained likelihood *minimization*. Table 3 shows outputs that are almost entirely repetitions of "when" (pp. 21–22).

### Appendix D: Additional results (pp. 22–27)
- *D.1* (Fig. 4): Best of $N$ for $N\in\{1,4,16,64,128\}$ (dialogue; the TL;DR panel shows 64, 128, 256). Performance plateaus after roughly 64–128 samples (pp. 22–23).
- *D.2* (Tables 4–10): sample comparisons.
  - In three TL;DR examples, GPT-4 prefers the DPO summary (temperature 0.25) over the PPO summary (temperature 0). In Tables 4 and 5 the PPO samples are repetitive or trail off; in Table 6 the GPT-4 judgment says the DPO summary does not assume a need for weight loss (pp. 23–24).
  - In two dialogue cases GPT-4 prefers DPO over the dataset's chosen response (GT). In one, DPO gives a long answer about the Civil Rights Movement that offers essay topics and hits the maximum generation length. In the other, it declines to find a private address (p. 25).
  - In two other cases GPT-4 prefers GT. In the WWII example, DPO's answer is fluent but factually wrong. In the "7 plus 2" example, GT says "11", which is wrong, and GPT-4 wrongly judges it correct (p. 26).
- *D.3 Human study* (p. 27): three matchups against PPO at temperature 0: DPO (0.25), SFT (0.25) and PPO (1.0). The authors sampled 150 DPO-vs-PPO-0 and 100 PPO-1-vs-PPO-0 comparisons, with two raters each, giving 275 and 200 judgments. They sampled 125 SFT comparisons with one rater each. Ties (about 1%) were ignored. There were 25 volunteer raters (Stanford-affiliated, mainly STEM/CS), each comparing 25 summaries. One volunteer finished late and was excluded from the analysis (p. 27).

## Toy example (ours, not from the paper)
One prompt $x$, one pair $(y_w,y_l)$, β = 0.5. Reference sequence probabilities: $\pi_{\text{ref}}(y_w)=0.2$, $\pi_{\text{ref}}(y_l)=0.3$. The margin is $m=\beta[\log(\pi_\theta(y_w)/\pi_{\text{ref}}(y_w))-\log(\pi_\theta(y_l)/\pi_{\text{ref}}(y_l))]$. The loss is $-\ln\sigma(m)$ and the gradient weight is $\sigma(-m)$.

| State | $\pi_\theta(y_w),\pi_\theta(y_l)$ | log-ratios $(y_w,y_l)$ | $m$ | $\sigma(m)$ | Loss | Weight $\sigma(-m)$ |
|---|---|---|---|---|---|---|
| (a) policy = reference | 0.2, 0.3 | 0, 0 | 0 | 0.5 | $\ln 2=0.693$ | 0.5 |
| (b) correct order | 0.3, 0.2 | $\ln1.5=0.4055$, $\ln(2/3)=-0.4055$ | $0.5\times0.811=0.4055$ | $1/(1+2/3)=0.6$ | $-\ln0.6=0.511$ | 0.4 |
| (c) wrong order | 0.1, 0.45 | $\ln0.5=-0.693$, $\ln1.5=0.4055$ | $0.5\times(-1.0986)=-0.549$ | $1/(1+\sqrt3)=0.366$ | $-\ln0.366=1.005$ | $0.634$ |

Here $e^{-0.4055}=2/3$ and $e^{0.549}=\sqrt3\approx1.732$. The wrongly ordered state (c) has the highest loss and the largest weight, so it gets the largest push. The correctly ordered state (b) has a lower loss and a smaller weight.

Shift check: adding the same constant $f(x)$ to both rewards leaves $m$ unchanged, as Lemma 1 says. For example, with $r$-values $0.2$ and $-0.2$, adding $+3$ gives $3.2$ and $2.8$. The difference is $0.4$ either way.

## Concepts
- [[dpo]] — (new) Direct Preference Optimization: a classification loss on preference pairs that trains the policy, whose log-ratio to a reference is the implicit reward (p. 2, Eq. 7 p. 4).
- [[rlhf]] — three phases: SFT, reward learning, RL fine-tuning with a KL-penalized reward (p. 3).
- [[reward-model]] — a network $r_\phi(x,y)$ fit by maximum likelihood on pairwise preferences (Eq. 2); DPO replaces it with an implicit one (p. 3).
- [[bradley-terry-model]] — preference probability is the logistic function of the reward difference (Eq. 1) (p. 3).
- [[kl-penalty]] — the β-weighted KL term in Eq. 3 that keeps $\pi_\theta$ near $\pi_{\text{ref}}$ and preserves diversity (p. 4).
- [[supervised-fine-tuning]] — the first RLHF phase, giving $\pi^{\text{SFT}}$ (and Preferred-FT as a baseline) (pp. 3, 8).
- [[plackett-luce-model]] — (new) a ranking model that generalizes BT to $K$ answers (Eq. 18) (pp. 3, 16).
- [[partition-function]] — (new) $Z(x)=\sum_y\pi_{\text{ref}}\exp(r/\beta)$; hard to compute but cancels in pairwise preferences (p. 4).
- [[implicit-reward]] — (new) $\hat r_\theta(x,y)=\beta\log\frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$, the reward defined by the policy (p. 5).
- [[reward-equivalence-class]] — (new) rewards differing by a function of $x$ alone; same preferences and same optimal policy (p. 5).
- [[best-of-n]] — (new) sample $N$ responses, return the one the learned reward ranks highest; a strong but costly baseline (p. 8).
- [[win-rate-gpt4-judge]] — (new) fraction of comparisons a model wins as judged by GPT-4, used as a proxy for human judgment (pp. 7, 10).
- [[ppo]] — (new) the actor-critic RL algorithm used in standard RLHF; the paper's main baseline (p. 4).

## Canonical instances
- [[imdb-controlled-sentiment]] — a controlled setting with a known reward classifier, used to trace the reward–KL frontier (p. 7–8).
- [[tldr-summarization]] — Reddit TL;DR summarization with human preferences; DPO about 61% vs PPO 57% GPT-4 win rate (p. 9).
- [[anthropic-hh-dialogue]] — single-turn helpful/harmless dialogue; DPO as the only efficient method improving over preferred completions (p. 9).
- [[cnn-dailymail-shift]] — out-of-distribution summarization test (Table 1) (p. 9).
- [[unlikelihood-degeneration]] — unlikelihood training produced generally meaningless outputs, which the authors believe results from unconstrained likelihood minimization of $\log p(y_l|x)$, with outputs ("when when…", Table 3) (p. 22).
- [[gpt4-human-agreement-study]] — Table 2 human study validating GPT-4 judgments (p. 10).

## Bridges (candidates)
- [same-math] Optimal policy $\pi\propto\pi_{\text{ref}}\exp(r/\beta)$ (Eq. 4) ↔ statistical mechanics: a Gibbs/Boltzmann distribution (exponential tilting of a base measure), with $Z(x)$ the partition function and β a temperature. The paper uses the term partition function but does not mention physics.
- [same-math] Bradley–Terry loss (Eq. 2/7) ↔ statistics: logistic regression on score differences for paired-comparison data.
- [same-math] Plackett–Luce (Eq. 18) ↔ discrete-choice modelling: sequential multinomial-logit choice from a shrinking set of options.
- [structural-analogy] Reward classes equal up to $f(x)$ (Def. 1) ↔ social science: utility is identified only up to a person- or context-specific constant in choice models. Only differences matter.
- [metaphor] LLM-as-judge validated against humans (Sec. 6.4) ↔ computational social science: validating an automated coder against human coders by agreement rates.

## Questions this raises
- The paper tests DPO only on models up to 6B parameters and mainly on preferences gathered from a different (SFT) policy. How sensitive is DPO to a mismatch between $\pi_{\text{ref}}$ and the policy that generated the pairs? (pp. 5, 10)
- Does an offline-only method over-optimize in a different way from online RL, and is the late dip in Fig. 3 right an example? (p. 10)
- How far can GPT-4 win rates be trusted, given prompt sensitivity and agreement on only about 65–86% of judgments? (pp. 10, 22–26)
- Where else might a closed-form policy–reward map replace an RL step, for example other modalities, as the authors suggest? (p. 10)

## Reading notes
- Printed page = pdf page (offset 0). Source pages 1–27; author contributions and acknowledgments are skipped. The reference list (pp. 11–14) was not digested.
- **Eq. 21–22 and the final A.4 display.** The images show Eq. 21 with $\beta\log\pi_\theta(y_l)/\pi_{\text{ref}}(y_l)-\beta\log\pi_\theta(y_w)/\pi_{\text{ref}}(y_w)$ inside σ, the opposite order from Eq. 7. The final gradient display in A.4 has weight $\sigma(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)}-\beta\log\frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)})$. The main-text gradient (p. 5) instead has $\sigma(\hat r_\theta(x,y_l)-\hat r_\theta(x,y_w))$, which is the form consistent with Eq. 7. These look like sign slips in the appendix.
- **Section 5.2 reference.** The text calls $\pi^*$ "the optimal policy from Eq. 7"; Eq. 7 is the DPO loss, and the optimal-policy form is Eq. 4. This looks like a wrong cross-reference.
- **Figure 3 caption.** It says DPO improves over "chosen summaries" in the Anthropic-HH test set. The text says preferred completions (dialogue responses).
- **Section 4 and Table 3.** The "naive version" without the weighting is said to degenerate (Appendix Table 3). Table 3 itself is labelled "Unlikelihood samples" (p. 22).
- **Table 2 versus D.3.** Table 2 gives 272, 122, 199 respondents. Appendix D.3 says 275, 125 and 200 judgments, and says ties (about 1%) were ignored.
- Figure 4 right panel legend shows Best of 64, 128, 256; the caption says $N=\{1,4,16,64,128\}$.
- The Section 6.2 text says "prior work has found that fine-tuning LMs using PPO on human preferences to provide more effective summaries" (a grammar slip in the source).
- Figure/table text layer was readable. All equations were checked against the page images.
