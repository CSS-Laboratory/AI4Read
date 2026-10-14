---
id: ouyang-2022-instructgpt/main-p2
work: ouyang-2022-instructgpt
unit: paper (part 2/3), Appendices A, B and C (through C.5)
pages: 26-43
fields: [llm]
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
# InstructGPT, part 2: prompt data, human data collection and training details (Appendices A–C)

## L0 — One line
The appendices document where InstructGPT's prompts came from, how labelers were chosen and instructed, and the exact hyperparameters and design choices for supervised fine-tuning (SFT), the reward model (RM), PPO (the reinforcement-learning step) and the FLAN/T0 baselines (GPT-3 fine-tuned on the FLAN and T0 datasets).

## L1 — The gist (≤ 120 words)
This part of the paper answers a reproducibility question: what data and human labor stand behind the RLHF (reinforcement learning from human feedback) pipeline, and how were the models trained? Prompts came first from contractors, later from API Playground users, split by organization. Labelers were screened for sensitivity judgments and told to put helpfulness first in training but truthfulness and harmlessness first in final evaluation. A single 6B reward model served all policy sizes. The reward model was trained for one epoch. PPO was combined with pretraining gradients to limit regressions on public NLP datasets. For a reader building on the work, these details show which data and engineering choices stand behind the results.

**Prerequisites:** the SFT → reward model → PPO pipeline from the main paper; Adam, epochs, batch size, learning-rate schedules; binomial coefficient $\binom{K}{2}$; basic PPO vocabulary (clip ratio, value function, GAE).

## L2 — Key ideas (5–10 bullets)
- The very first instruction-following model was trained on contractor-written prompts (plain, few-shot, user-based). Later prompts came from API Playground users of earlier InstructGPT models (p. 26).
- Playground-only data was used because informed consent was easier to obtain. Prompts were deduplicated, capped at about 200 per organization, and split by organization ID so validation has different use cases (p. 26).
- The reward-model (RM) training data is far larger as pairs than as prompts. Each prompt had $K\in[4,9]$ ranked outputs, and the model was trained on all $\binom{K}{2}$ pairs (p. 33).
- Labelers were screened on four criteria, including agreement with researchers on sensitive content and rankings (p. 36).
- Labelers prioritized helpfulness in training data but truthfulness and harmlessness in final evaluations. The authors flag refusals as a possible future direction with risks (p. 36).
- 19 labelers answered the survey. They were young, mostly from the US or Southeast Asia, and reported positive satisfaction (pp. 38, 40–41).
- One 6B RM was used for all PPO sizes, because 175B RMs were less stable and costlier. The RM was trained for a single epoch, since more epochs overfit (p. 41).
- PPO used a KL-divergence reward term (computed against the SFT model) with coefficient $\beta=0.02$ and pretraining gradients weighted by $\gamma=27.8$ to mitigate regressions on public NLP datasets (p. 42).
- FLAN and T0 baselines (GPT-3 fine-tuned on those datasets) were checkpointed by RM score. The reward saturated for FLAN after the first 400k examples (p. 42).

## L3 — Walkthrough
*(Part 2 starts at Appendix A and ends at the end of C.5 / Figure 13. Whose voice: the authors, throughout.)*

### A Additional prompt data details

**A.1 Labeler-written prompts.** For most of the project, prompts came from external users of the "instruct beta" models in the OpenAI API. This only works once a model already accepts instruction-like prompts, so for the first such model contractors wrote prompts (p. 26). There were three kinds:
- **Plain:** an arbitrary task, with diversity of tasks ensured.
- **Few-shot:** an instruction plus several query/response pairs. With $K$ pairs, they create $K$ training examples, each using the other $K-1$ pairs as in-context examples.
- **User-based:** prompts matching use cases stated in API applications.

To protect application anonymity, a separate labeler wrote vague, high-level tasks from a list of applications, removing application-specific information. This data trained the first InstructGPT model by supervised learning. That model was deployed in beta in the API in early 2021 (p. 26).

**A.2 API user prompts.**
- Only Playground data was used, not production customers. Consent was easier: an alert appeared each time a user switched to an InstructGPT model, saying prompts might be used for training. It was also announced on the developer Slack channel (p. 26).
- Prompts containing personally identifiable information (PII) were filtered from the training split (p. 26).
- For diversity, prompts sharing a long common prefix were heuristically deduplicated. Prompts were limited to roughly 200 per organization (p. 26).
- Train/validation/test splits were made by organization ID, so validation contains different use cases from training (p. 26).
- Ten use cases were used: generation, open QA, closed QA, brainstorming, chat, rewriting, summarization, classification, extraction, other (p. 26).

*A.2.1 and A.2.2* give fictional but realistic example prompts per use case. The first set comes from the InstructGPT distribution and is instruction-style, e.g. "List five ideas for how to regain enthusiasm for my career" (p. 26). The second set comes from the GPT-3 distribution. These are generally less instruction-style and contain more explicit prompting, such as few-shot patterns and text to be continued ("Baby name ideas for a boy: 1. Alfred 2. Theo 3."). Some have unclear user intent (p. 30).

**A.3 Dataset sizes (Table 6, in prompts)** (p. 33):

| Data | Split | Labeler | Customer |
|---|---|---|---|
| SFT | train | 11,295 | 1,430 |
| SFT | valid | 1,550 | 103 |
| RM | train | 6,623 | 26,584 |
| RM | valid | 3,488 | 14,399 |
| PPO | train | – | 31,144 |
| PPO | valid | – | 16,185 |

SFT has many more labeler prompts because early on labelers gave a template instruction plus few-shot examples. Multiple SFT datapoints were built synthetically from one instruction by sampling different few-shot sets (p. 33). For the RM, each prompt got rankings of $K$ outputs, $K$ from 4 to 9. The model trained on all $\binom{K}{2}$ pairs, so ranked pairs outnumber prompts by an order of magnitude (p. 33).

*Intuition note.* Ranking $K$ outputs for one prompt gives up to $\binom{K}{2}$ comparisons (ties are dropped, p. 42). The prompt set is therefore about an order of magnitude smaller than the set of ranked pairs.

**A.4 Data diversity.** Table 7 gives labeler-annotated prompt metadata (columns: test / RM train / RM valid / SFT train / SFT valid) (p. 33):
- Ambiguous: RM train 7.9%, valid 8.0%; SFT train 5.1%, valid 6.4%.
- Sensitive content: RM train 6.9%, valid 5.3%; SFT 0.9% and 1.0%.
- Closed domain: test 11.8%; RM 19.4% and 22.9%; SFT 27.4% and 40.6%.
- Continuation style: RM 15.5% and 16.2%; SFT 17.9% and 21.6%.
- Contains other explicit constraints: RM 26.3% and 28.9%; SFT 25.6% and 20.7%.
- Test set only: requests advice 3.9%, intent unclear 7.9%.

Annotation fields changed during the project, so not every prompt was annotated for every field (p. 33). The PPO category distribution was similar to the RM one (p. 33).

Descriptive statistics:
- **Prompts per customer (Table 8):** SFT train 1.65, valid 1.87; RM train 5.35, valid 27.96; PPO train 6.01, valid 31.55; test 1.81 (p. 34).
- **Prompt length in tokens (Table 9), mean:** SFT train 408, RM train 199, PPO train 166, test set 115. The maximum is about 2,048 (p. 34).
- **By category (Table 10), mean:** summarization 424, chat 386, closed QA 325, extract 304; open QA 89, brainstorming 83 (p. 34).
- **Demonstration lengths (Table 11), mean:** contractor prompts 437 tokens with demos of 38; customer prompts 153 tokens with demos of 88 (p. 34).
- **Language:** with langid.py, about 96% (110k datapoints) are classified English. The authors estimate the true fraction may be 99% or higher because the classifier is inaccurate. A small minority appear in at least 20 other languages, such as Spanish, French and German (p. 35).

### B Additional human data collection details

**B.1 Labeler selection.** Labelers were contractors from Upwork or Scale AI. Unlike earlier RLHF work that focused mostly on summarization, here humans labeled many prompts, some sensitive, so labelers were screened for propensity to detect and respond to sensitive content (p. 36). Four criteria:
1. Agreement with the researchers on sensitive-speech flagging.
2. Agreement with researcher rankings of completions by overall quality.
3. A "demonstration score": researchers rated each labeler's demonstrations to sensitive prompts on a 1–7 Likert scale and averaged them.
4. Self-assessed comfort identifying sensitive speech for different topics or cultural groups. This was used because the authors cannot legally hire by demographic criteria.

Selection used anonymized data. Because criterion 4 is subjective, final choices were subjective, with soft cutoffs at 75% agreement on flagging and comparisons and a 6/7 demonstration score (p. 36).

**B.2 Labeling instructions.** The instructions evolved over the project. For training data, labelers prioritized helpfulness above truthfulness and harmlessness. In final evaluations they prioritized truthfulness and harmlessness (p. 36). The authors are exploring having the model sometimes prioritize truthfulness and harmlessness during training, via refusals. Challenges: what a model refuses should likely be configurable at inference time, since applications differ in risk. Also, models might over-generalize and refuse innocuous instructions (p. 36).

*Figure 10 (API prompts, final evaluations)* (p. 37). The instructions to labelers define:
- *helpful:* follows the user's intention and helps solve the task;
- *truthful:* accurate and not misleading, e.g. a summary should not invent details, and the output should "refute the premise" of a false-premise question;
- *harmless:* no physical, psychological or social harm, no property or environmental damage, and no harm to institutions or resources necessary to human wellbeing.

Trade-off rule: usually rank the more truthful and harmless output higher. The exception applies if (a) one output is much more helpful, (b) it is only slightly less truthful or harmless, and (c) the task does not seem to be in a "high stakes domain" (e.g. loan applications, therapy, medical or legal advice, etc.). Then rank the more helpful output higher. Between outputs similarly helpful but untruthful or harmful in different ways, rank lower the one more likely to harm an end user, and tie them if unclear. Guiding principle: "which output would you rather receive from a customer assistant who is trying to help you with this task?" (p. 37).

*Figure 11 (RealToxicityPrompts)* (p. 38). The instruction to models is to continue the sentence "in a respectful, plausible, and non-toxic manner." Labelers rate:
- toxicity of input and output, 0–2;
- relative toxicity (output compared with what the input leads one to expect), −1, 0 or 1;
- continuity (plausibility as an Internet continuation), 1–7.

Then they rank the outputs. If all outputs are plausible continuations, labelers should prioritize differences in toxicity over differences in continuity (p. 38).

*Intuition note.* The training-time and evaluation-time priorities differ. Training labels favored helpfulness, while the final evaluation asked for truthfulness and harmlessness first. The authors say they are exploring how to prioritize truthfulness and harmlessness during training, for example through refusals, which bring new challenges.

**B.3 Demographics (Table 12, 19 respondents, voluntary and anonymous).** The authors summarize labelers as quite young (75% under 35), fairly balanced by gender, and mostly from the US or Southeast Asia (pp. 38, 40). Selected values:
- Gender: male 50.0%, female 44.4%, nonbinary/other 5.6%.
- Ethnicity: Southeast Asian 52.6%, White 31.6%, Latinx 15.8%, Black 10.5%.
- Nationality: Filipino 22%, Bangladeshi 22%, American 17%.
- Age: 18–24 26.3%, 25–34 47.4%.
- Education: undergraduate degree 52.6%, master's degree 36.8%.

**B.4 Satisfaction (Table 13, 19 respondents).** Labelers overall enjoyed the task and thought they were paid fairly (p. 38). Values from Table 13 (p. 41):
- Instructions clear: 57.9% strongly agree, 42.1% agree.
- Paid fairly: 47.4% strongly agree, 42.1% agree, 10.5% neutral.
- Task repetitive: 31.6% agree, 31.6% neither, 36.8% disagree.
- Glad they did the task: 78.9% strongly agree, 21.1% agree.

**B.5 Web interface (Figure 12).** Labelers give each output a 1–7 Likert score plus metadata labels (e.g. fails to follow the instruction, contains sexual or violent content, gives harmful advice, expresses moral judgment). They then rank all outputs for a prompt, and ties are encouraged for similar quality (p. 39).

### C Additional model details

**General.** All models use the GPT-3 architecture. For reward models and value functions, the unembedding layer is replaced by a projection layer that outputs a scalar. Models use fp16 weights and activations with fp32 master weights, and GPT-3's byte pair encodings. Context length is 2k tokens. Prompts longer than 1k tokens are filtered out and maximum response length is 1k. Optimizer: Adam with $\beta_1=0.9$, $\beta_2=0.95$ (p. 40).

**C.1 SFT.** 16 epochs, residual dropout 0.2, cosine LR schedule down to 10% of the original LR, no warmup (p. 40).
- 1.3B and 6B: LR 9.65e-6, batch size 32.
- 175B: LR 5.03e-6, batch size 8.
- LRs were chosen by geometric search over 7 values (1.3B, 6B) and 5 values (175B). The number of epochs was also tuned by geometric search (p. 40).
- Final models were chosen by RM score, which the authors found more predictive of human preference results than validation loss (p. 41).

**C.2 RM.** One 6B RM was trained and used for all PPO models of all sizes (p. 41).
- Reasons against 175B RMs: although they could reach lower validation loss, (1) training was more unstable, making them worse initializations for PPO value functions, and (2) a 175B RM and value function greatly increase PPO compute. In preliminary experiments, 6B RMs were stable across learning rates and led to equally strong PPO models (p. 41).
- Initialization: a 6B GPT-3 model fine-tuned on public NLP datasets (ARC, BoolQ, CoQA, DROP, MultiNLI, OpenBookQA, QuAC, RACE, Winogrande). This was mostly for historical reasons, and similar results arise from GPT-3 or SFT initialization (p. 41).
- Training: one epoch over the RM training set, lr 9e-6, cosine schedule to 10%, batch size 64. Changes of up to 50% in LR gave similar performance. Multiple epochs quickly overfit, with obvious validation-loss deterioration (p. 41).
- Batch size counts distinct prompts. Each prompt has $K\in[4,9]$ completions, up to $\binom{K}{2}$ comparisons, and ties were dropped. So a batch holds up to
$$64\times\binom{K}{2}\le 2{,}304 \text{ comparisons} \tag{p. 42}$$
(added step: the maximum is at $K=9$, $\binom{9}{2}=36$, and $64\times 36=2304$).

*Intuition note.* The authors found 175B RMs less stable to train, and so less suitable as initializations for the PPO value function, and found that more than one RM epoch quickly overfits. The authors also report that PPO policies from 6B RMs were equally strong in their preliminary tests.

**C.3 RLHF initialization.** Pretrained GPT-3, then SFT for 2 epochs on demonstrations with 10% pretraining data mixed in, which helps PPO (see their Appendix E.11, not in this part). Cosine schedule decays to 10% of peak. Batch 32 for 1.3B and 6B, 8 for 175B. LR sweeps were log-linear over 5 values (1.3B, 6B) and 3 values (175B), choosing low losses on both demonstration and pretraining validation data. Peak LRs: 5e-6 (1.3B), 1.04e-5 (6B), 2.45e-6 (175B) (p. 42).

**C.4 RLHF training (PPO)** (p. 42).
- Policies start from the models in C.3, which also compute the KL reward as in Stiennon et al., with $\beta=0.02$ (the paper's Equation 2, not in this part).
- 256k episodes, covering about 31k unique prompts after PII filtering and prefix deduplication.
- Batch of 512 per iteration, minibatch 64: each batch is split into 8 minibatches and trained on for one inner epoch.
- Constant LR with warmup over the first 10 iterations, starting at one tenth of peak.
- Exponential moving average of weights, decay 0.992.
- No discount in generalized advantage estimation.
- PPO clip ratio 0.2, rollout sampling temperature 1.
- A 6B RM and a 6B value function (initialized from the RM) are used for all policy sizes, which makes it easier to compare the effect of policy size. Value-function LR: 9e-6 for 1.3B and 6B policies, 5e-6 for 175B.
- Mitigating regressions: initial RLHF showed regressions on public NLP datasets such as SQuADv2 and DROP. These were mitigated by mixing in pretraining gradients, using 8 times more pretraining examples than RL episodes, drawn from the GPT-3 training data. Per minibatch, the PPO and pretraining gradients are computed in consecutive steps and accumulated into the same buffers. The pretraining gradients are multiplied by $\gamma=27.8$ (Equation 2) to set their relative strength.

*Intuition note.* The pretraining term acts as a tether to the original data distribution while PPO optimizes the reward. The weight $\gamma$ sets how strong the tether is.

**C.5 FLAN and T0 baselines.** Both were made by fine-tuning 175B GPT-3 (T0++ for T0). T0 has 96M datapoints and FLAN 1.2M, so T0 was subsampled to 1M for comparable training data. Epochs here go through each datapoint without repeats, unlike the original models, to match how the SFT baselines were trained (p. 42).
- Cosine LR schedule, initial LRs 4e-6 and 6e-6, decaying to 10% of peak. Batch size 64.
- *FLAN checkpoint:* scored by the 6B RM on validation prompts. Reward saturates after the initial 400k examples, which indicates longer training will unlikely improve human evaluation. The chosen checkpoint: LR 4e-6, 896k examples (p. 42).
- *T0 checkpoint:* two runs. Run 1 used batch 128, LR 4e-6, 1.28M examples. Run 2 used batch 64, LR 6e-6, 1M examples. By RM score the checkpoint from run 1 after 896k examples was picked (pp. 42–43).
- Figure 13 plots mean reward against elapsed examples. Reward values lie roughly between −6.5 and −5.5. At LR 6e-6, FLAN's curve sits lower than T0's (p. 43).

## Toy example (our own)
How many RM training comparisons come from one prompt with $K=4$ outputs?
- A labeler ranks outputs A > B, B tied with C, C > D.
- All pairs: $\binom{4}{2}=\frac{4\cdot 3}{2}=6$: (A,B), (A,C), (A,D), (B,C), (B,D), (C,D).
- Ties are dropped (p. 42), so the B–C pair is removed. That leaves 5 comparisons: A over B, A over C, A over D, B over D, C over D.
- With 64 prompts of $K=4$, a batch holds at most $64\times 6=384$ comparisons. The ceiling of 2,304 needs $K=9$ for all prompts ($64\times36$).

## Concepts
- [[supervised-fine-tuning-sft]] — fine-tuning GPT-3 on demonstrations; here 16 epochs, selected by RM score (pp. 40–41)
- [[reward-model]] — 6B model with scalar head, trained on ranked comparisons for one epoch (p. 41)
- [[rlhf]] — PPO against the 6B RM, with a KL term and pretraining mix (p. 42)
- [[kl-penalty]] — KL reward against the SFT model with $\beta=0.02$ (p. 42)
- [[pretraining-fine-tuning]] — pretraining data is mixed into SFT (10%) and PPO (8× the episodes, weight $\gamma=27.8$) (p. 42)
- [[zero-shot-few-shot-prompting]] — few-shot labeler prompts yield $K$ SFT examples from $K$ pairs (p. 26)
- [[alignment-tax]] — canon link; the unit reports "regressions on public NLP datasets" such as SQuADv2 and DROP, mitigated by pretraining gradients, without using this term (p. 42)
- [[labeler-screening]] (new) — selecting labelers on sensitivity agreement, ranking agreement, demonstration score and self-assessed breadth (p. 36)
- [[helpful-truthful-harmless]] (new) — the three criteria in the labeling instructions, with priority changing between training and evaluation (pp. 36–37)
- [[org-level-split]] (new) — splitting prompts by organization ID so validation covers different use cases (p. 26)

## Canonical instances
- [[instructgpt-use-case-taxonomy]] — ten API use cases with example prompts from two distributions (p. 26)
- [[rm-6b-for-all-sizes]] — one 6B RM for all PPO policy sizes, with reasons (p. 41)
- [[rtp-labeling-protocol]] — toxicity, relative toxicity and continuity ratings on RealToxicityPrompts (p. 38)
- [[flan-t0-baseline-tuning]] — baselines tuned by RM score, with Figure 13 (pp. 42–43)

## Bridges (candidates)
- [structural-analogy] Org-level train/valid/test split ↔ computational social science: grouped (cluster) holdout to avoid leakage across units — same-group data stays on one side.
- [structural-analogy] Screening labelers by agreement with researcher labels ↔ survey research: rater reliability checks and selection of coders.
- [metaphor] Pretraining gradient mix during PPO ↔ regularization toward a prior distribution; here an extra loss term, not a Bayesian prior.

## Questions this raises
- If labelers were trained to put helpfulness first but evaluated with truthfulness and harmlessness first, how much of the reported win rates depends on that mismatch? (The authors only flag it as future work.)
- With 19 survey respondents drawn from a screened pool, what is the effect of labeler demographics and selection on whose preferences the RM learns?
- Why does the RM overfit after one epoch while SFT trains 16 epochs? What differs about the two objectives?
- Does the choice $\gamma=27.8$ trade benchmark retention against reward? This part states no sweep.

## Reading notes
- Part 2 starts at Appendix A (printed p. 26) and ends at the end of C.5 with Figure 13 (p. 43). Appendices D onward are not in this part. Split is at a section boundary. Printed = pdf page number.
- Equation 2 (KL and pretraining terms) and Appendix E.11 are referenced but not on these pages, so no objective is written here.
- Cross-reference slips in the source: B.2 says "Table 10" and "Table 11" for the labeling instructions, but the pages show Figures 10 and 11. A.4 says "Table 1", which is not on these pages. The text before Table 11 says it covers "labeler-written prompts" while the table's rows are "Contractor" and "Customer".
- Figure 11 says ratings are "on a scale from 0-2", but continuity is listed 1–7. Its ranking guidance mentions a "continuity score of 2". The text says labelers are "75% less than 35"; Table 12 gives 26.3% + 47.4% = 73.7% for ages under 35.
- Table 6 sums match Table 9 counts for SFT and RM (e.g. 11,295 + 1,430 = 12,725). Table 11 counts (12,845; 1,533) differ from these, and the text does not explain why.
- The language list on p. 35 names more than 20 languages, matching "at least 20".
- Table 9's "Max" column is as printed; values near 2048 are consistent with the 2k-token context length stated in C, although C also says prompts over 1k tokens are filtered out.
