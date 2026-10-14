---
id: ouyang-2022-instructgpt/main-p1
work: ouyang-2022-instructgpt
unit: paper (part 1/3) — Abstract, Sections 1–5, Acknowledgements, References
pages: 1–25
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Training language models to follow instructions with human feedback (InstructGPT) — main text

## L0 — One line
Fine-tuning GPT-3 with human demonstrations, a reward model learned from human rankings, and PPO makes labelers prefer its outputs over those of a model 100x larger, while truthfulness improves and some harms and mistakes remain.

## L1 — The gist (≤ 120 words)
Large language models trained to predict the next token often do not do what users want: they invent facts, produce toxic text, or ignore instructions. The paper asks whether fine-tuning with human feedback can fix this. The authors fine-tune GPT-3 in three steps: supervised learning on labeler demonstrations, a reward model trained on labeler rankings, and reinforcement learning (using PPO, a standard RL algorithm) against that reward. The resulting models are called InstructGPT. Labelers prefer outputs of a 1.3B InstructGPT model to those of 175B GPT-3. Truthfulness improves, toxicity improves a little when the model is prompted to be respectful, bias does not. The alignment is to the preferences of a specific group, and simple mistakes remain.

**Prerequisites:** next-token language modelling; supervised fine-tuning; the sigmoid function and log-likelihood; the basic idea of a reward and a policy in reinforcement learning.

## L2 — Key ideas (5–10 bullets)
- **Misalignment of the pretraining objective.** Next-token prediction on web text is a different objective from following the user's instructions helpfully and safely, so the paper calls it misaligned, and big LMs often show unintended behaviour such as invented facts or toxic text (pp. 1–2).
- **Three-step recipe.** (1) supervised fine-tuning (SFT) on demonstrations, (2) reward model (RM) trained on ranked outputs, (3) PPO (a reinforcement-learning algorithm) against the RM with a KL penalty, a term that punishes drifting away from the SFT model (pp. 2–3, 6, 8–9).
- **Pairwise ranking loss.** The RM is trained on all $\binom{K}{2}$ pairs from each ranked prompt as one batch element. This avoids overfitting and saves compute (p. 8, eq. 1).
- **PPO-ptx.** Mixing pretraining-likelihood gradients into PPO (eq. 2) reduces the alignment tax (the performance lost on some public NLP datasets because of alignment training). It works better than raising the KL coefficient, but does not remove all regressions (pp. 9, 14–15, 20).
- **Main result.** On the API prompt distribution, labelers prefer InstructGPT to GPT-3 at every size. 175B InstructGPT beats 175B GPT-3 in 85 ± 3% of comparisons (pp. 2–3, 11).
- **Mixed safety results.** Truthfulness improves, and so does closed-domain hallucination (making up information not in the input; 21% vs 41%). Toxicity improves only when prompted to be respectful. Bias metrics show no improvement (pp. 3, 13–14).
- **Public NLP instruction datasets (FLAN, T0: collections of public NLP tasks written with instructions) do less well** than human-preference data on the API distribution. The authors believe there are two reasons: the API distribution is mostly open-ended generation, and public datasets lack input diversity (pp. 4, 12–13).
- **Whose preferences?** The model is aligned to about 40 contractors, the researchers' instructions and OpenAI API customers, not to a broader notion of human values (pp. 2, 18–19).
- **Remaining failures.** The model mostly follows the user's instruction even when it could be harmful, can over-hedge, sometimes assumes a false premise is true, and still makes up facts (pp. 16–19).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–4)
**Problem.** Larger LMs do not automatically follow user intent. They can be untruthful, toxic or unhelpful, which the authors describe as the models not being aligned with their users (p. 1). The reason given: the usual objective, predicting the next token on web pages, differs from the objective of following the user's instructions helpfully and safely. The authors therefore call the language modeling objective *misaligned* (p. 2).

**Target behaviour.** Following Askell et al. (2021), models should be *helpful* (help solve the task), *honest* (not fabricate or mislead) and *harmless* (not cause physical, psychological or social harm). Evaluation of these is in Section 3.6 (p. 2).

**Method in outline (Fig. 2, pp. 2–3).**
- Hire a team of 40 contractors, chosen by a screening test.
- Collect human demonstrations on mostly English API prompts plus some labeler-written prompts, and train SFT baselines.
- Collect human comparisons between model outputs on a larger set of API prompts, and train an RM to predict the preferred output.
- Fine-tune the SFT model with PPO to maximise the RM reward.
- The API prompts used for training were submitted to earlier versions of the InstructGPT models on the API Playground, which had been trained only on demonstration data. Prompts containing PII are filtered out (fn. 3, p. 2).
- The authors state that this aligns GPT-3 to the stated preferences of a specific group (mostly labelers and researchers), not a broader notion of "human values" (p. 2).
- Models are 1.3B, 6B and 175B, all with the GPT-3 architecture. Evaluation is mainly by labelers on held-out customers' prompts, plus public NLP datasets (pp. 2–3).

**Main findings as claimed in the introduction (pp. 3–4).**
- *Preference.* 1.3B InstructGPT outputs are preferred to 175B GPT-3 outputs, even though they differ only in the human-data fine-tuning. This holds even when GPT-3 gets a few-shot prompt. 175B InstructGPT is preferred to 175B GPT-3 85 ± 3% of the time, and to few-shot 175B GPT-3 71 ± 4% (p. 3).
- *Truthfulness.* On TruthfulQA, InstructGPT gives truthful and informative answers about twice as often as GPT-3. The result is equally strong on questions not adversarially selected against GPT-3. On closed-domain tasks (output should not contain information absent from the input), InstructGPT hallucinates 21% vs 41% for GPT-3 (p. 3).
- *Toxicity and bias.* About 25% fewer toxic outputs than GPT-3 on RealToxicityPrompts when prompted to be respectful. No significant improvement on Winogender or CrowS-Pairs (p. 3).
- *Alignment tax.* RLHF causes regressions on SQuAD, DROP, HellaSwag and WMT 2015 French→English. Mixing pretraining-log-likelihood updates into PPO (PPO-ptx) greatly reduces them without compromising labeler preference scores (pp. 3–4).
- *Held-out labelers* (who produced no training data) prefer InstructGPT at about the same rate as training labelers. This is a preliminary experiment, and more work is needed on broader groups and on inputs where humans disagree (p. 4).
- *FLAN and T0.* Against the SFT baseline, InstructGPT has a 73.4 ± 2% win rate, versus 26.8 ± 2% for the authors' T0 and 29.8 ± 2% for their FLAN model (p. 4).
- *Generalisation.* InstructGPT can follow instructions to summarise code, answer questions about code, and sometimes follow instructions in other languages, although these are very rare in the fine-tuning data (p. 4).
- *Mistakes remain:* failing to follow instructions, making up facts, long hedging answers, missing false premises (p. 4).

**Intuition note.** The abstract says that making models bigger does not by itself make them better at following user intent (p. 1). Consistent with that, on this prompt distribution a 1.3B model fine-tuned on human data is preferred to a 175B GPT-3 with the same architecture and over 100x more parameters (p. 3).

### 2 Related work (pp. 4–5)
- **RLHF lineage.** RLHF began with simple simulated robots and Atari games (Christiano et al., 2017; Ibarz et al., 2018). It was then applied to summarisation (Ziegler et al., 2019; Stiennon et al., 2020; Wu et al., 2021, and others) and to other text domains such as dialogue, translation and story generation. The authors say their work can be seen as a direct application of RLHF to aligning language models on a broad range of language tasks (pp. 4–5).
- **What alignment means.** Kenton et al. (2021) catalogue misalignment issues. In concurrent work, Askell et al. (2021) propose language assistants as an alignment testbed (p. 5).
- **Instruction training.** Cross-task-generalisation work fine-tunes LMs on many public NLP datasets with instructions. A consistent finding is that this improves performance on held-out tasks, zero-shot and few-shot (p. 5).
- **Harms.** Documented harms include bias, private-data leakage and misinformation. Interventions can have side effects: reducing toxicity can reduce the ability to model text from under-represented groups (Xu et al., 2021) (p. 5).
- **Mitigation methods** cited include value-targeted fine-tuning, filtering the pretraining data, blocking words or n-grams, control tokens, embedding regularisation, data augmentation, and steering with a second smaller LM (p. 5).

### 3 Methods and experimental details

#### 3.1 High-level methodology (p. 6)
The method follows Ziegler et al. (2019) and Stiennon et al. (2020). Starting inputs: a pretrained LM, a prompt distribution, and trained human labelers.
- **Step 1.** Labelers demonstrate desired behaviour on prompts. Fine-tune pretrained GPT-3 on this with supervised learning.
- **Step 2.** Collect comparisons between model outputs (labeler indicates the preferred one). Train an RM to predict the preferred output.
- **Step 3.** Use the RM output as a scalar reward. Fine-tune the supervised policy with PPO.
- Steps 2 and 3 can be iterated. In practice, most comparison data comes from the SFT policies, some from PPO policies (p. 6).

#### 3.2 Dataset (pp. 6–7)
- **Source.** Prompts are mostly text submitted to the OpenAI API through the Playground, using an early InstructGPT model. Customers were notified that data could be used for training. Production-API data is not used (p. 6).
- **Hygiene.** Prompts with a long common prefix are heuristically deduplicated, with at most 200 prompts per user ID. Train/validation/test splits are by user ID, so validation and test contain no users from training. Training prompts are filtered for PII (p. 6).
- **Bootstrap prompts.** To train the very first models, labelers wrote prompts, because instruction-like prompts were rare on the API. Three kinds: *plain* (arbitrary diverse task), *few-shot* (an instruction plus several query/response pairs), *user-based* (prompts for use-cases stated in API waitlist applications) (p. 7).
- **Three datasets.** SFT dataset: labeler demonstrations, about 13k training prompts (API and labeler-written). RM dataset: labeler rankings of outputs, 33k training prompts (API and labeler-written). PPO dataset: no human labels, 31k prompts (API only). Details in Table 6, which is not in this part (p. 7).
- **Composition (Table 1, RM dataset, API prompts).** Generation 45.6%, Open QA 12.4%, Brainstorming 11.2%, Chat 8.4%, Rewrite 6.6%, Summarization 4.2%, Classification 3.5%, Other 3.5%, Closed QA 2.6%, Extract 1.9% (p. 6). Most use-cases are generative rather than classification or QA (p. 7).
- Table 2 gives researcher-written illustrative prompts (e.g. a brainstorming prompt asking for five ideas to regain enthusiasm for one's career) (p. 6).

#### 3.3 Tasks (p. 7)
- Training tasks come from labeler-written prompts and early-InstructGPT API prompts. The dataset is over 96% English (p. 7).
- A task can be specified by a direct instruction (e.g. write a story about a wise frog), by few-shot examples, or by implicit continuation (the start of a story). Labelers infer the user's intent and skip prompts where the task is very unclear. They also weigh implicit intentions such as truthfulness and avoidance of biased or toxic language, following the provided instructions and their best judgment (p. 7).

#### 3.4 Human data collection (pp. 7–8)
- About 40 contractors were hired via Upwork and ScaleAI. They were chosen for sensitivity to different demographic groups' preferences and skill at spotting potentially harmful outputs, measured by a screening test (Appendix B.1, not in this part) (p. 7).
- **Conflicting criteria.** During training, helpfulness to the user is prioritised (the authors say prioritising otherwise requires design decisions left to future work, Section 5.4). In final evaluations, labelers were asked to prioritise truthfulness and harmlessness, because the authors say this is what they really care about (pp. 7–8).
- Labelers got onboarding, detailed instructions and a shared chat room for questions (p. 8).
- A separate set of *held-out* labelers, from the same vendors but with no screening test, produce no training data. They test generalisation to other labelers' preferences (p. 8).
- **Agreement.** Training labelers agree with each other 72.6 ± 1.5% of the time, held-out labelers 77.3 ± 1.3%. For comparison, researcher–researcher agreement in Stiennon et al. (2020) was 73 ± 4% (p. 8).

#### 3.5 Models (pp. 8–9)
Start from the pretrained GPT-3 models of Brown et al. (2020), trained on broad Internet data but with "poorly characterized behavior" (p. 8).

**SFT.** Fine-tune GPT-3 on labeler demonstrations. 16 epochs, cosine learning-rate decay, residual dropout 0.2. Final SFT model selection uses the RM score on the validation set. SFT models overfit validation loss after 1 epoch, but more epochs help both RM score and human preference ratings despite this (p. 8).

**Reward model (RM).**
- Start from the SFT model with the final unembedding layer removed. The model takes a prompt and response and outputs a scalar reward (p. 8).
- Only 6B RMs are used. 175B RM training "could be unstable" and thus less suitable as the value function in RL (Appendix C) (p. 8).
- Stiennon et al. (2020) train on pairs with a cross-entropy loss where comparisons are labels. The reward difference represents the log odds that one response is preferred by a human labeler (p. 8).
- To speed up collection, labelers rank $K$ responses, with $K$ between 4 and 9. This gives $\binom{K}{2}$ comparisons per prompt. Shuffling all comparisons into one dataset made the RM overfit within a single pass, because comparisons from one task are very correlated (fn. 5: each completion would potentially be used for $K-1$ separate gradient updates). So all $\binom{K}{2}$ comparisons from a prompt form *one batch element*. This needs one forward pass per completion rather than $\binom{K}{2}$ passes, no longer overfits, and gives much better validation accuracy and log loss (p. 8).

The loss:

$$\text{loss}(\theta) = -\frac{1}{\binom{K}{2}}\, E_{(x,y_w,y_l)\sim D}\left[\log\left(\sigma\left(r_\theta(x,y_w) - r_\theta(x,y_l)\right)\right)\right] \tag{1}$$

Here $r_\theta(x,y)$ is the scalar RM output for prompt $x$ and completion $y$ with parameters $\theta$. $y_w$ is the preferred completion in the pair $(y_w, y_l)$, and $D$ is the dataset of human comparisons (p. 8). Shapes: input is a (prompt, completion) text pair; output is one scalar; per prompt there are $K$ scalars and $\binom{K}{2}$ pair terms.

**Normalisation.** The RM loss is invariant to shifts in reward, so a bias is added such that labeler demonstrations get mean score 0 before RL (p. 9).

**Intuition note.** Equation (1) says: push up the reward of the winner relative to the loser. Only reward *differences* matter, which is why the authors add a bias to fix the absolute level before RL (p. 9). Batching all pairs of one prompt together stops the model from seeing the same completion many times as if the data were independent.

**RL (PPO).**
- Following Stiennon et al., the SFT model is fine-tuned with PPO. The environment is a *bandit*: it shows a random customer prompt, expects a response, returns a reward from the RM, and ends the episode (p. 9).
- A per-token KL penalty from the SFT model is added to mitigate over-optimisation of the RM. The value function is initialised from the RM. These models are "PPO" (p. 9).
- To fix regressions on public NLP datasets, pretraining gradients are mixed into the PPO gradients: "PPO-ptx". The combined objective:

$$\text{objective}(\phi) = E_{(x,y)\sim D_{\pi_\phi^{\mathrm{RL}}}}\left[r_\theta(x,y) - \beta \log\left(\pi_\phi^{\mathrm{RL}}(y\mid x)/\pi^{\mathrm{SFT}}(y\mid x)\right)\right] + \gamma\, E_{x\sim D_{\text{pretrain}}}\left[\log\left(\pi_\phi^{\mathrm{RL}}(x)\right)\right] \tag{2}$$

- $\pi_\phi^{\mathrm{RL}}$ is the learned RL policy, $\pi^{\mathrm{SFT}}$ the supervised model, $D_{\text{pretrain}}$ the pretraining distribution. $\beta$ (KL reward coefficient) and $\gamma$ (pretraining loss coefficient) control the strength of the KL penalty and the pretraining gradients. For "PPO" models, $\gamma=0$. Unless otherwise specified, "InstructGPT" means the PPO-ptx models (p. 9).
- (added step) The sequence log-ratio $\log(\pi^{\mathrm{RL}}(y\mid x)/\pi^{\mathrm{SFT}}(y\mid x))$ equals the sum over tokens of the per-token log-ratios, so eq. (2)'s sequence-level penalty matches the "per-token KL penalty" described in the text.

**Intuition note.** The reward is the RM score minus a leash (the KL term) that the authors add to mitigate over-optimisation of the RM (p. 9). The $\gamma$ term mixes in pretraining gradients, which the authors introduce to fix regressions on public NLP datasets (p. 9).

**Baselines (p. 9).** SFT models and GPT-3. Also GPT-3 with a few-shot prefix prepended to the instruction ("GPT-3-prompted"). The prefix was chosen in a competition between two authors (RL and DA): each spent an hour interacting with GPT-3 and proposed two prefixes. The winner was the one with the highest RM score on the prompt validation set (fn. 6). Also 175B GPT-3 fine-tuned on FLAN and T0, each on about 1 million examples. The checkpoint with the highest RM score on validation is chosen (p. 9).

#### 3.6 Evaluation (pp. 9–10)
**Definition of alignment.** The authors say the definition of alignment has been vague. They follow Leike et al. (2018): models act in accordance with user intentions. Practically, they use the Askell et al. framework: helpful, honest, harmless (pp. 9–10).
- **Helpful.** Follow instructions and also infer intention from a few-shot prompt or a pattern like "Q: {question}\nA:". Because intention can be ambiguous, the main metric is labeler preference. A caveat: labelers are not the users who wrote the prompts, so labeler-inferred and actual intention could diverge (p. 10).
- **Honest.** Hard to measure in purely generative models, since it needs the model's "belief", which cannot be inferred from a black box. Instead they measure *truthfulness* via (1) tendency to make up information on closed-domain tasks ("hallucinations") and (2) TruthfulQA. The authors say this captures only a small part of what is meant by truthfulness (p. 10).
- **Harmless.** Harm depends on how outputs are used (toxic output can be harmful in a chatbot but useful for data augmentation). An earlier "potentially harmful" labeling was discontinued as it required too much speculation. Instead, proxy criteria: inappropriate for a customer assistant, denigrates a protected class, sexual or violent content, plus benchmarks RealToxicityPrompts and CrowS-Pairs (p. 10).

**Two quantitative evaluation families (p. 10).**
1. *API distribution.* Main metric: human preference on held-out prompts from customers not in training. Since training prompts were written for InstructGPT models, they may disadvantage GPT-3 baselines. So the authors also evaluate on prompts submitted to GPT-3 models. For each model they compute how often its output is preferred to a baseline policy, the 175B SFT model, chosen because the authors say its performance is about in the middle of the compared models. Labelers also give a 1–7 Likert overall-quality score and metadata (Table 3: binary flags such as fails to follow the correct instruction, hallucination, satisfies instruction constraint, sexual or violent content, denigrates a protected class, gives harmful advice, expresses opinion or moral judgment, etc.) (pp. 9–10).
2. *Public NLP datasets.* Safety-related ones (truthfulness, toxicity, bias) and zero-shot performance on traditional tasks (QA, reading comprehension, summarisation). Human toxicity evaluation on RealToxicityPrompts. Samples are released (p. 10).

### 4 Results

#### 4.1 Results on the API distribution (pp. 11–13)
- **Preference.** Labelers significantly prefer InstructGPT across model sizes (Fig. 1, p. 2). GPT-3 is worst. One gets step-size improvements by a well-crafted few-shot prompt, then SFT, then PPO on comparison data. Adding pretraining-mix updates in PPO does not change labeler preference much. 175B InstructGPT is preferred to GPT-3 85 ± 3% and to few-shot GPT-3 71 ± 4% of the time (p. 11).
- **Prompts for GPT-3.** Results do not change significantly on prompts submitted to GPT-3 models (Fig. 3), though PPO-ptx models do slightly worse at larger sizes (p. 11).
- **Concrete axes (Fig. 4, collapsed across model sizes).** Compared with GPT-3, InstructGPT is more appropriate as a customer assistant, follows explicit constraints more often (e.g. a limit on answer length in paragraphs), more often attempts the correct instruction, and hallucinates less on closed-domain tasks. The authors say these results suggest that InstructGPT is more reliable and easier to control than GPT-3. Other metadata categories occur too rarely for significant differences (pp. 11–12).
- **Held-out labelers.** They show similar ranking preferences (Fig. 3), and all InstructGPT models still greatly outperform GPT-3 baselines, so, the authors say, the models are not simply overfitting to the preferences of training labelers (p. 12).
- **RM cross-validation.** Labelers are split into 5 groups. 5 RMs (3 seeds) are trained with 5-fold cross validation, using 4 groups for training and 1 for evaluation. Accuracy on predicting held-out-group preferences: 69.6 ± 0.9%, versus 72.4 ± 0.4% on training-group labelers (p. 12).
- **FLAN and T0 (Fig. 5).** They beat default GPT-3 and are on par with well-prompted GPT-3, but are worse than the SFT baseline. Head to head, 175B InstructGPT is preferred over FLAN 78 ± 4% and over T0 79 ± 4% (pp. 12–13).
- **Authors' two proposed reasons** (p. 13). (i) Public NLP datasets capture tasks easy to score automatically, such as classification and QA. Classification and QA are only about 18% of API use, whereas open-ended generation and brainstorming are about 57% of the prompt dataset. (ii) It is hard for public datasets to reach high input diversity. The authors add that NLP tasks are still a kind of instruction we want models to solve, so the broadest model would combine both kinds of data (p. 13).

**Intuition note.** Fig. 1 shows an ordering of steps: GPT-3 < prompted GPT-3 < SFT < PPO, each step giving a step-size improvement in labeler preference (p. 11). Adding the pretraining mix does not change labeler preference much (p. 11).

#### 4.2 Results on public NLP datasets (pp. 13–15)
**Truthfulness (TruthfulQA, human evaluation; Fig. 6).**
- PPO models show small but significant improvements in truthful and informative outputs vs GPT-3, by default with no instruction to tell the truth. The exception is the 1.3B PPO-ptx model, slightly worse than same-size GPT-3 (p. 13).
- On prompts not adversarially selected against GPT-3, PPO models are still significantly more truthful and informative, although the absolute improvement shrinks by a couple of percentage points (p. 13).
- With the "Instruction+QA" prompt (answer "I have no comment" when unsure), PPO models err on the side of being truthful and uninformative rather than confidently saying a falsehood. GPT-3 is not as good at this (p. 13).
- Fewer closed-domain hallucinations (Fig. 4) are additional evidence (p. 13).
- (Reading note on strength: the introduction says "about twice as often" (p. 3). Section 4.2 says "small but significant" (p. 13). The Acknowledgements say the automatic TruthfulQA metrics were overstating the gains of the PPO models (p. 21).)

**Toxicity (RealToxicityPrompts; Fig. 7).**
- Samples are scored by Perspective API (the standard procedure) and rated by labelers on absolute toxicity, toxicity relative to the prompt, continuity and overall preference. Prompts are sampled uniformly by prompt toxicity (not the standard sampling), so absolute toxicity numbers are inflated (p. 14).
- With a "respectful prompt", InstructGPT is less toxic than GPT-3 by Perspective API. The advantage disappears with no prompt. When explicitly prompted to be toxic, InstructGPT is much more toxic than GPT-3 (Fig. 39, Appendix E) (p. 14).
- Human evaluations agree: less toxic in the respectful setting, similar with no prompt (p. 14).
- All models score as less toxic than expected given the prompt (a negative score on a −1 to 1 scale, 0 = about as toxic as expected). SFT is least toxic but has the lowest continuity and is least preferred, which "could indicate" very short or degenerate responses (p. 14).

**Bias (modified Winogender and CrowS-Pairs).**
- The authors compute relative probabilities of each sentence in a pair and the entropy (in bits) of the binary distribution. A perfectly unbiased model has no preference and maximum entropy. By this metric, the models are not less biased than GPT-3. PPO-ptx shows similar bias to GPT-3. When instructed to be respectful it has lower entropy, so higher bias. The pattern is unclear; instructed models seem more certain regardless of stereotypical content (p. 14).

**Alignment tax.**
- By default PPO on the API distribution lowers performance on several public NLP datasets. The authors want an alignment method without such a tax, because a tax gives people a reason to use models that are unaligned but more capable on these tasks (p. 14).
- Fig. 29 (Appendix, not in this part): PPO-ptx mitigates the regressions on all datasets and even surpasses GPT-3 on HellaSwag. It still lags GPT-3 on DROP, SQuADv2 and translation (p. 15).
- Mixing pretraining updates beats the simpler fix of raising the KL coefficient. Fig. 33: some pretraining-mix coefficient reverses the regressions on SQuADv2 and DROP with minimal loss in validation reward. Fig. 34: raising the KL coefficient significantly lowers validation reward and never fully recovers DROP and SQuAD. Changing the KL reference model from the PPO init to GPT-3 gives similar results (p. 15).

**Intuition note.** Alignment training can make a model worse at ordinary benchmarks. Keeping a pretraining-likelihood term in the objective greatly reduces these regressions, though it does not remove all of them (pp. 4, 15, 20).

#### 4.3 Qualitative results (pp. 15–17)
- **Generalisation.** InstructGPT follows instructions in non-English languages and does code summarisation and QA, although these are a "tiny minority" of fine-tuning data (fn. 9: labelers skip evaluations needing expertise they lack, though some use translation services for simple instructions). The authors suggest that "in some cases" alignment methods could generalise to inputs humans did not supervise (pp. 15–16).
- Not tracked quantitatively. Fig. 8 (French frog-story prompt; code question on `binomial_coefficient`): prompts are cherry-picked, outputs are not. The 175B PPO-ptx model often answers in English when the instruction is in another language. GPT-3 can do these tasks with more careful prompting and rarely follows instructions in these domains. In the code example, the caption says InstructGPT's answer is not quite correct, and GPT-3 answers the question about 50% of the time (pp. 15–16).
- **Simple mistakes (Fig. 9).** (1) With a false-premise instruction (e.g. why eat socks after meditating), the model sometimes assumes the premise is true. (2) It can over-hedge on simple questions (the cannonball–pumpkin example). (3) Performance degrades with multiple explicit constraints (e.g. listing 10 movies made in the 1930s and set in France) or constraints that are hard for LMs (e.g. a summary in a set number of sentences) (p. 16).
- **Suspected causes (the authors' suspicions).** They suspect behaviour (2) emerges partly because labelers are told to reward epistemic humility, so they may tend to reward hedging, and the RM picks this up. They suspect behaviour (1) occurs because few training prompts assume false premises and the models do not generalise well to such examples. They believe both could be dramatically reduced by adversarial data collection (Dinan et al., 2019b) (p. 17).

### 5 Discussion

#### 5.1 Implications for alignment research (p. 17–18)
- The approach is iterative: improve alignment of current systems rather than abstractly aligning systems that do not yet exist. Disadvantage: it does not face problems specific to aligning superhuman systems. Advantage: a clear empirical feedback loop. RLHF is also a building block in several proposals for aligning superhuman systems, e.g. book summarisation (p. 17).
- **Lesson 1 – alignment cost is modest relative to pretraining.** Training 175B SFT takes 4.9 petaflops/s-days and 175B PPO-ptx takes 60, versus 3,640 for GPT-3. The authors say RLHF makes models more helpful to users than a 100x model size increase does. They suggest that right now investing more in aligning existing models is more cost-effective than training larger ones, at least for their customers' natural-language task distribution (p. 17).
- **Lesson 2 – generalisation of "following instructions"** to unsupervised settings (non-English, code). Important because supervising every task is too expensive. More research is needed on how it scales with capability (p. 17).
- **Lesson 3 – most degradations mitigated.** A high alignment tax might prevent adoption, so low-tax techniques are needed. The authors say their results are good news for RLHF as a low-tax alignment technique (p. 17).
- **Lesson 4 – validated in the real world,** on systems used in production with customers, unlike earlier theoretical, synthetic-domain or public-dataset work (pp. 17–18, fn. 10).

#### 5.2 Who are we aligning to? (p. 18)
End behaviour depends on the base model and its data, the fine-tuning data and the alignment method. The authors align to labelers' preferences, which were shaped by the instructions given, the paid-job context, and who gave the instructions. Four caveats:
1. *Training labelers.* Mostly English-speaking people in the United States or Southeast Asia, hired via Upwork or Scale AI. They disagree on many examples (about 73% agreement).
2. *Researchers' preferences.* The authors write the instructions and answer edge-case questions. The effect of instruction sets and interface design needs study.
3. *Customers.* Training prompts come from OpenAI customers on the Playground, so they implicitly align to what customers (and in some cases their end-users) value. Customers may not optimise for end-user well-being (example: maximising time on a platform). Labelers cannot see the contexts where outputs will be seen.
4. *Not representative.* Customers are not representative of all users or affected groups. API users were selected from a waitlist seeded with OpenAI employees' networks.

The authors say they are not claiming that researchers, labelers or customers are the right source of preferences. They say it is impossible to train a system aligned to everyone's preferences at once. One suggested path: models conditioned on, or easily fine-tuned or prompted for, different groups' preferences. That raises hard questions about whose preferences to condition on and how groups can opt out (p. 18).

#### 5.3 Limitations (p. 19)
- *Methodology.* Value judgments are shaped by about 40 contractors' identity and background. The group is small to allow high-bandwidth communication, but it is "clearly not representative". Most comparisons are labeled by only 1 contractor for cost reasons. Multiple labels could show where labelers disagree. Aligning to the average labeler may not be desirable, e.g. text that disproportionately affects a minority group might weight that group's labelers more (p. 19).
- *Models.* The models are neither fully aligned nor fully safe: they still produce toxic or biased output, make up facts and generate sexual or violent content without explicit prompting. Perhaps the greatest limitation: they mostly follow the user's instruction even if harmful. With a prompt to be maximally biased, InstructGPT is more toxic than equal-size GPT-3 (p. 19).

#### 5.4 Open questions (pp. 19–20)
Ideas the authors list: adversarial data collection; filtering pretraining data; combining with truthfulness methods such as WebGPT; training refusal of harmful instructions (the present model complies, and refusal is harder because harm depends on deployment context; the authors plan to explore it); combining with steerability methods (control codes, small-model guidance); other algorithms (expert iteration, behaviour cloning on a subset of comparison data, constrained optimisation); other feedback forms (edits, natural-language critiques) (p. 19–20). The pretraining-mix fix does not completely mitigate performance regressions and may make undesirable behaviours more likely if they are in the pretraining data. Filtering the mix for toxic content or adding synthetic instructions would likely help (p. 20). Following Gabriel (2020), alignment targets differ (instructions, intentions, revealed preferences, ideal preferences, interests, values). This paper aligns to inferred user intention "for simplicity". A biggest open question is designing a transparent, representative process that reaches broad consensus (p. 20).

#### 5.5 Broader impacts (p. 20)
- Next-word prediction is "only a proxy" for what we want. The techniques hold promise for more helpful, truthful and harmless models. As scaling continues, more care is needed (p. 20).
- Better instruction following also makes misuse easier (misinformation, hateful or abusive content). Alignment is "not a panacea" but one tool in a broader safety ecosystem. Some high-stakes domains (medical diagnosis, credit, employment, housing, political advertising, law enforcement and others) call for great care or no deployment (p. 20).
- Release trade-offs: open-sourcing makes harmful use hard to limit without regulation. Restricting access to a few organisations excludes most people. API deployment allows use-case restriction, monitoring, revoking access and rate limiting, but costs transparency and centralises power. Who the models are aligned to "will significantly affect" whether the net impact is positive or negative (p. 20).

### Acknowledgements and References (pp. 21–25)
Thanks, a list of labelers and references. One acknowledgement of substance: Evans and Lin pointed out that the automatic TruthfulQA metrics were overstating the gains of the PPO models (p. 21).

## Toy example (ours, not from the paper)
**Reward-model loss, eq. (1), with $K=3$.** A labeler ranks completions A > B > C for one prompt. Suppose the RM currently gives $r(A)=2,\ r(B)=1,\ r(C)=0$. There are $\binom{3}{2}=3$ pairs.
- (A,B): $\sigma(2-1)=\sigma(1)=1/(1+e^{-1})=0.7311$; $\log = -0.3133$.
- (A,C): $\sigma(2)=0.8808$; $\log=-0.1269$.
- (B,C): $\sigma(1-0)=0.7311$; $\log=-0.3133$.
- Sum of logs $=-0.7535$. Mean $=-0.7535/3=-0.2512$. Loss $=0.2512$ (one batch element for this prompt).
- If the RM ordered them wrongly ($r(A)=0, r(B)=1, r(C)=2$): $\sigma(-1)=0.2689$, $\log=-1.3133$ (twice); $\sigma(-2)=0.1192$, $\log=-2.1269$. Mean $=(1.3133+1.3133+2.1269)/3=4.7535/3=1.5845$. Loss rises from 0.25 to 1.58, so training pushes toward the labeler's ranking.

**Shift invariance.** Adding 10 to all rewards leaves every difference unchanged, so the loss is identical. This is why the paper adds a bias so demonstrations score 0 on average.

**KL-penalised reward (eq. 2, sequence level, one sample).** Take $r_\theta=1.0$, $\beta=0.1$, $\pi^{\mathrm{RL}}(y|x)=0.2$, $\pi^{\mathrm{SFT}}(y|x)=0.1$. Then $\log(0.2/0.1)=\ln 2=0.6931$. Penalised reward $=1.0-0.1\times0.6931=0.9307$. If the policy has drifted so that the ratio is 4, $\ln 4=1.3863$ and the reward is $1.0-0.1386=0.8614$. The more the policy departs from SFT, the more reward is subtracted.

## Concepts
- [[supervised fine-tuning (SFT)]] — fine-tuning GPT-3 on labeler demonstrations; here run 16 epochs despite validation-loss overfitting after 1 (p. 8)
- [[reward model]] — SFT model minus unembedding layer, outputting a scalar for (prompt, response); only 6B used (p. 8)
- [[Bradley–Terry model]] — eq. (1) uses $\sigma(r_w-r_l)$ as P(winner preferred); the paper describes it as "log odds" via Stiennon et al., without naming Bradley–Terry (canon link; not stated in this unit) (p. 8)
- [[RLHF]] — use human preferences as a reward signal to fine-tune; here PPO against the RM (p. 2)
- [[KL penalty]] — per-token penalty from the SFT model to curb RM over-optimisation, coefficient $\beta$ (p. 9)
- [[alignment tax]] — lower performance on some tasks caused by alignment training (here SQuAD, DROP, HellaSwag, translation) (pp. 3–4)
- [[pretraining / fine-tuning]] — GPT-3 pretrained on web text, then fine-tuned in three steps (p. 8)
- [[zero-shot / few-shot prompting]] — the GPT-3-prompted baseline prepends a few-shot prefix to emulate instruction following (p. 9)
- [[ppo-ptx]] (new) — PPO plus a $\gamma$-weighted pretraining log-likelihood term; "InstructGPT" by default means this (p. 9)
- [[helpful-honest-harmless]] (new) — the Askell et al. criteria used to define alignment; honesty measured only as truthfulness (p. 10)
- [[preference win rate]] (new) — fraction of comparisons where a model's output is preferred to the 175B SFT baseline's (p. 10)
- [[misaligned objective]] (new) — next-token prediction is a different objective from following instructions helpfully and safely (p. 2)
- [[bandit environment]] (new) — each episode is one prompt, one response, one reward (p. 9)
- [[cross-entropy / log-loss]] — the RM is trained with a cross-entropy loss over pairwise comparisons (p. 8)

## Canonical instances
- [[instructgpt-pipeline]] — three-step SFT → RM → PPO pipeline (Fig. 2) (p. 3)
- [[instructgpt-1.3b-beats-gpt3-175b]] — 1.3B PPO-ptx preferred to 175B GPT-3 by labelers (Fig. 1) (p. 2)
- [[truthfulqa-eval]] — TruthfulQA human evaluation, with and without an Instruction+QA prompt that tells the model to say it has no comment when unsure (p. 13)
- [[realtoxicityprompts-eval]] — toxicity improves only with "respectful" prompt; much worse when prompted to be toxic (p. 14)
- [[flan-t0-comparison]] — fine-tuning on public NLP instruction datasets is preferred less than InstructGPT on API prompts (pp. 12–13)
- [[false-premise-failure]] — a question about why one should eat socks after meditating; the model can go along with the false premise (Fig. 9) (p. 16)

## Bridges (candidates)
- [same-math] Pairwise ranking loss $-\log\sigma(r_w-r_l)$ ↔ preference-learning / logistic regression on score differences: same formula as logistic regression on a difference of scores.
- [structural-analogy] KL-penalised reward ↔ regularised optimisation: the KL term acts as a regulariser toward a reference policy.
- [structural-analogy] Aligning to ~40 contractors' preferences ↔ survey sampling and measurement (computational social science): who is sampled defines the "population preference" that is measured.
- [metaphor] Alignment tax ↔ economic "tax" on adoption: a cost that discourages use of aligned models (the paper uses this reasoning, p. 14).

## Questions this raises
- If inter-labeler agreement is only about 73%, what exactly does the RM learn about the "average" labeler, and which disagreements are lost?
- How does the 85 ± 3% preference result change if the judges are the actual users who wrote the prompts, not labelers?
- Why does being prompted to be toxic make InstructGPT more toxic than GPT-3? What does that say about the trade-off between instruction following and harm?
- Why are the PPO-ptx gains on public datasets only partial? Would adding more pretraining mix, or filtering the mix, close the gap?

## Reading notes
- **Part boundaries.** This part starts at the title page and abstract (p. 1) and ends at the last reference on p. 25. It covers Sections 1–5, Acknowledgements and References. The appendices (A–E; datasets, labeler details, training details, extended results) are not in this part. Figures 29, 33, 34, 39 and Tables 6 and 14 are cited by the text but not shown here, so their content is not reported. The unit was split at a section boundary.
- **Page numbers.** Printed = pdf for all pages.
- **Misprints seen in the images.** "Most of the use-cases have are generative" (p. 7); "evaluatoins" (p. 13); "Satisifies" in Table 3 (p. 9); "aren't as good" with singular subject "the baseline GPT-3 model" (p. 13). The roadmap on p. 4 lists the task and dataset details as 3.3 and 3.2, reversing the order of the sections.
- **Eq. (2).** The image shows the last term as $\gamma E_{x\sim D_{\text{pretrain}}}[\log(\pi^{\mathrm{RL}}_\phi(x))]$, with $x$ (not $y\mid x$) as the argument. I copied it as printed.
- **Figures.** Values in Figs. 1, 3–7 are bar and line plots with 95% confidence intervals. I report only numbers stated in the text.
- The text layer for eq. (1) and fn. 5 was garbled (fractions, binomial coefficients); I checked them against the page images.
- The paper's own cross-references (e.g. "Section 5.4" for conflicting criteria) were followed as written.
