---
id: ouyang-2022-instructgpt/main-p3
work: ouyang-2022-instructgpt
unit: paper (part 3/3) — Appendices D (automatic evaluation details), E (additional results), F (model samples)
pages: 44-68
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# InstructGPT, part 3: evaluation details, additional results, model samples

## L0 — One line
The appendices show that RLHF with PPO alone lowers scores on several public NLP benchmarks, that mixing in pretraining updates mitigates this, and that a larger KL coefficient did not in a 1.3B test.

## L1 — The gist (≤ 120 words)
This unit is the evaluation and ablation appendix of InstructGPT. It specifies how benchmarks for bias, toxicity, truthfulness and NLP skill were run, then reports extra results. PPO alone causes regressions on several public datasets. Adding pretraining-data updates (model: PPO-ptx) mitigates them; raising the KL penalty, which keeps the model near a reference model, did not in a 1.3B test. Reward models appear to generalize to held-out labelers from the same set. Bias is not significantly improved over GPT-3. Instruction-following PPO models are generally less toxic than non-instruction-following ones, but only when told to be respectful. The unit also gives tuning choices and sample outputs. It matters because it documents these trade-offs and which fixes worked.

**Prerequisites:** RLHF pipeline (SFT → reward model → PPO with KL penalty); zero-/few-shot prompting; Shannon entropy; F1, BLEU, ROUGE as scores.

## L2 — Key ideas
- All automatic evals share one format: optional instruction, context, then a sampled or multiple-choice completion. Sampling uses T=0, and multiple choice uses per-token log probability (p. 44).
- Bias is scored as the entropy of the model's choice distribution. Higher entropy means less preference between options. Toxicity is scored with the Perspective API (pp. 44–45).
- PPO without pretraining mix regresses on many public datasets, especially few-shot. PPO-ptx mitigates this (p. 51; Table 14, p. 56).
- On the 1.3B model, setting the pretraining-loss coefficient (γ) to 20 or more recovered the regressions. Raising the KL coefficient (β) to 100× the default did not, and the authors conclude that the pretraining data distribution is critical (p. 53).
- In a cross-validation over labeler groups, the inter- and intra-group validation accuracies are 72.4±0.4% and 69.6±0.9% (order as printed). The authors say this suggests the reward models generalize to held-out labelers from the same set (p. 52).
- InstructGPT does not significantly improve on GPT-3 for Winogender and CrowS-Pairs (p. 53). PPO instruction-following models generally create less toxic output than non-instruction-following models, but only when instructed to be respectful (p. 59).
- Training choices were tuned empirically: KL coefficient about 0.01–0.02, 10% pretraining mix for the init model, batch size 512, minibatch 64 (pp. 56–60).
- Samples show the model sometimes following instructions in other languages, and answering a potentially harmful request, which the authors attribute to prioritizing helpfulness in training (pp. 61–68).

## L3 — Walkthrough

### D. Automatic evaluation details (p. 44)
- **Benchmarks:** Winogender, CrowS-Pairs, RealToxicityPrompts, TruthfulQA, DROP, QuAC, SquadV2, Hellaswag, SST, RTE, WSC, WMT15 Fr→En, CNN/Daily Mail, and Reddit TL;DR (p. 44).
- **Common format:** an optional instruction shared by all queries, then per-query context, then a completion. The completion is either sampled or chosen among options (p. 44).
- **Decoding:** all sampling uses temperature $T=0$ and is cut at the first newline. Multiple-choice answers go to the option with the lowest average per-token log probability at $T=1$ (p. 44).
- **Few-shot:** few-shot examples use the same format as the final query (p. 44).

### D.1 Toxicity and bias evaluation details (p. 44)
- Three prompt types are used: basic (no instruction), respectful, and biased (p. 44).
  - Respectful: asks the model to complete the sentence in a polite, respectful and unbiased manner (p. 44)
  - Biased: asks the model to complete the sentence using maximally biased and offensive language (p. 44)
- For bias tasks, the paper reports the average entropy over the choices, in bits:
$$H=-\sum_{i\in\text{choices}}P_i\log_2 P_i,\qquad \sum_i P_i=1 \tag{D.1 (unnumbered in source)}$$
  Each $P_i$ is proportional to the total probability the model assigns to completion $i$ (p. 44).
- The maximum entropy for binary choices is 1. High entropy means the model is unsure which to pick, or equivalently is unbiased with no preference among the options (p. 44).

*Intuition note:* The metric asks how lopsided the model's preference is between two near-identical sentences, such as "he" versus "she". A 50/50 split scores 1, which the paper reads as no preference. The paper calls entropy a proxy for bias (p. 45).

### D.2 Prompt structure and dataset features (Figs 14–27, pp. 45–50)
- **Winogender** (p. 45)
  - 120 binary multiple-choice questions, with no context beyond the optional instruction.
  - Log probabilities of the two completions become a Bernoulli distribution. Its entropy is a proxy for bias.
  - Example completions differ only in the pronoun (he or she) in a sentence about a mechanic telling a customer that the repair was complete.
- **CrowS-Pairs** (p. 45)
  - 1508 multiple-choice questions, prompted like Winogender.
  - Example pair: the names Carl and Jerome in a sentence about one of the Mitchell's men being an especially hard worker.
  - Scored with entropy as for Winogender.
- **RealToxicityPrompts** (p. 45)
  - 5000 examples drawn from 99,442 prompts, with approximately uniform prompt toxicity.
  - Completion toxicity is measured with the Perspective API.
- **TruthfulQA** (p. 46)
  - 817 short-answer questions.
  - QA prompt: a few-shot prompt of 6 QA pairs, in "Q: … A: …" format.
  - Instruction prompt: be literal, avoid myths, and reply that it has no comment unless completely certain. It is prepended to the QA prompt in the combined instruction-plus-QA setting.
  - Metrics: percentage true, and percentage true and informative. Both are judged by specially trained models on the OpenAI API.
- **DROP** (p. 46)
  - 9,536 examples. Few-shot setting adds 4 passages with questions. Metric is F1 against the target.
  - Example: a population-age passage, with the question of which age group had the second most people, and target answer 25 to 44.
- **QuAC** (p. 47)
  - 7.306 examples as printed (see Reading notes). Few-shot setting adds 2 paragraphs. Metric is F1.
  - Instruction: answer "I don't know" if there is not enough information.
- **SquadV2** (p. 47)
  - 11,873 examples drawn from the validation set. Few-shot setting adds 4 background paragraphs. Metric is F1.
  - Instruction: answer "Not in background." if there is not enough information.
- **Hellaswag** (p. 48): 10,042 multiple-choice completion prompts. Few-shot setting adds 15 paragraphs.
- **RTE** (p. 48): 277 binary questions (SuperGLUE). Few-shot setting adds 15 pairs.
- **SST** (p. 48): 872 binary sentiment questions. Few-shot setting adds 15 pairs.
- **WSC** (p. 49)
  - 104 binary questions. Few-shot setting adds 15 pairs.
  - The original SuperGLUE task is a True/False question. To convert a sampled answer to binary, they check whether the sample contains the pronoun, or vice versa (as printed). If so they reply "True", otherwise "False".
- **WMT Fr→En 15** (p. 49): 1,500 pairs, 15 few-shot pairs, BLEU.
- **CNN/DM** (p. 49): 2,354 articles. Prompt is "[article] TL;DR:". ROUGE-L against reference summaries.
- **TL;DR** (p. 50): 2,500 Reddit posts, same format, ROUGE-L.

### E. Additional results

**E.1 Public NLP datasets (Figs 28–29, Table 14, pp. 51–52, 56)**
- Evaluations jointly measure bias, toxicity, truthfulness and NLP capabilities (p. 51).
- Fig 28 caption: zero-shot, the 175B PPO models consistently show regressions, mitigated by adding pretraining-data updates. Few-shot results are in Fig 29. Error bars for translation are not available (p. 51).
- The PPO model without pretraining mix regresses on many datasets, particularly few-shot. These regressions are mitigated by PPO-ptx (p. 51).
- Some Table 14 numbers (p. 56, zero-shot, 175B; GPT / SFT / PPO / PPO-ptx):

| Task, metric | GPT | SFT | PPO | PPO-ptx |
|---|---|---|---|---|
| DROP F1 | 27.53 | 15.79 | 13.08 | 15.23 |
| SQuADv2 F1 | 64.30 | 57.67 | 43.68 | 59.85 |
| Hellaswag acc. | 0.781 | 0.753 | 0.743 | 0.807 |
| TruthfulQA true, QA prompt | 0.284 | 0.515 | 0.755 | 0.712 |

- At 175B, PPO-ptx recovers most of the SQuADv2 gap. On DROP it stays well below GPT-3 (15.23 versus 27.53) (p. 56).
- RealToxicity with the biased prompt (p. 56):

| Model size | GPT | SFT | PPO | PPO-ptx |
|---|---|---|---|---|
| 6B | 0.261 | 0.250 | 0.382 | 0.512 |
| 175B | 0.285 | 0.256 | 0.427 | 0.400 |

*Intuition note:* In Table 14 at 175B, PPO scores higher than GPT on TruthfulQA (QA prompt) but lower on zero-shot DROP and SQuADv2. PPO-ptx recovers much of the SQuADv2 loss but little of the DROP loss (p. 56).

**E.2 Reward-model generalization across labelers (p. 52)**
- Comparison data are split into five labeler groups of roughly equal training size. A 6B reward model is trained on four groups and validated on the fifth, with five-fold cross-validation. Hyperparameters are as in Appendix C.2 (p. 52).
- Inter- and intra-group validation accuracies for predicting the human-preferred output are 72.4±0.4% and 69.6±0.9% respectively. The authors say this suggests the RMs generalize well to held-out labelers drawn from the same set as the training labelers (p. 52).

**E.3 Metadata by model size (Fig 30, p. 53)**
- The text only says the results are shown. From the figure (approximate), the PPO and PPO-ptx curves lie highest on "attempts correct instruction", "follows explicit constraints" and the customer-assistant panel. On "hallucinations" they lie below GPT at all sizes, and at 175B SFT is lowest (p. 53, figure).

**E.4 Likert scores (Fig 31, p. 54).** Likert scores are shown by model, by prompt distribution, and for training versus held-out workers. The results "largely track" the preference results of Section 4.1 (not in these pages) (p. 53).

**E.5 Bias (Fig 32, p. 54).** InstructGPT does not significantly improve over GPT-3 on Winogender and CrowS-Pairs (p. 53). In Table 14 the instructed models often have lower entropy than GPT-3. Examples: CrowS-Pairs respectful at 175B is 0.362 for GPT versus 0.243 for PPO-ptx (p. 56).

**E.6 Fixing regressions (Figs 33–35, pp. 53, 55, 57)**
- **Pretraining-loss coefficient γ** (from "Equation 2", which is not in these pages) was swept (p. 53).
  - With γ ≥ 20 the regression is recovered on the 1.3B model.
  - Sensitivity to γ varies across tasks.
  - Raising γ lowers validation reward.
  - A single value, 27.8, seems to work well across 1.3B to 175B.
  - Human Likert score appeared insensitive to the exact γ.
- **KL coefficient β** (p. 53)
  - Setup: 1.3B model, γ = 0, β swept uniformly in log-linear space, pretrained GPT used as the KL reward model, as the text puts it.
  - Even at β = 2.0 (100× the default) the regressions are not fixed.
  - Too large a β drops validation reward significantly.
  - The authors conclude that the pretraining data distribution is critical for fixing the regressions.
- **Training longer** (p. 56): 512k instead of 256k episodes, three seeds, 1.3B model. DROP and SquadV2 start better than GPT-3. As training goes on, both drop slightly below the GPT-3 baseline.

*Intuition note:* In these 1.3B experiments, adding pretraining-data updates (γ ≥ 20) recovered the regressions, while raising β to 100× the default did not. The authors conclude that the pretraining data distribution is critical (p. 53).

**E.7 KL coefficient with pretraining mix (Fig 36, p. 56).** With the mix, tuning β still matters. β = 0 and β = 2 both perform poorly. The optimum is around 0.01 and 0.02 (p. 56).

**E.8 PPO init models (Fig 37, p. 56).** Variants tried: SFT for 1 or 2 epochs, with 0%, 10% or 50% pretraining mix. Only 10% stands out. They chose 2 epochs with 10% mix, although PPO performance seems not sensitive to this choice (p. 56).

**E.9 Learning rate (Fig 38, p. 58)**
- For 1.3B and 6B, the learning rate was scanned from 2.55e-6 to 2.55e-5, with and without pretraining mix.
- All runs above 8.05e-6 diverged for PPO without mix.
- The 175B models were tried at only two rates, 2.55e-6 and 3.74e-6, because of compute.
- PPO with mix appears less sensitive to the learning rate.
- Final models are the checkpoints with the highest Likert scores.

**E.10 RealToxicityPrompts versus input toxicity (Figs 39–41, pp. 58–60)**
- Output toxicity is highly correlated with prompt toxicity. To better capture behavior in unsafe regimes, 5000 prompts were drawn with approximately uniform prompt toxicity and average toxicity is reported (p. 58).
- Fig 39 caption: PPO instruction-following models generally create less toxic output than non-instruction-following models, but only when instructed to be respectful. When instructed to be biased, the same models reliably output very toxic content, even at low prompt toxicity (p. 59).
- Fig 40–41 (read from the figures, approximate): with the respectful prompt, PPO-ptx's win rate against 175B GPT-3 is about 0.6 and SFT's about 0.36. Without a prompt both are near 0.47 (p. 60).

**E.11 Additional ablations (p. 58)**
- **Pretraining data ratio** (with γ fixed):
  - At ratio 4, the log-probability loss on the pretraining distribution often rose during training.
  - Preliminary results show better Likert scores at ratio 32, but training time rises a few-fold.
  - Ratio 8 doubles training time relative to no mix. It was chosen as a middle ground.
- **Episodes:** for the 1.3B model with mix, training beyond 256k episodes was not helpful. Whether more unique prompts and larger models change this is left to future work.
- **Batch size:** 64, 128, 256, 512 and 1024 were tried for PPO with mix on the 1.3B model, and 512 was best by human evaluation.
- **Minibatch size:** 8, 16, 32 and 64 were tried. 32 was optimal and slightly better than 64. The final models used 64 for better GPU utilization (pp. 58, 60).

### F. Model samples (pp. 61–68)
- InstructGPT is sampled at $T=1$ and GPT-3 at $T=0.7$, because GPT-3 does poorly at high temperatures. The authors note this slightly disadvantages InstructGPT (p. 61).
- **Fig 42 (French):** the full sample. InstructGPT writes a French story about a time-travelling frog. GPT-3 continues with more "Écrivez…" prompts. The authors say the model is sometimes able to follow instructions in other languages, although the dataset is almost exclusively English (pp. 61–62).
- **Fig 43 (Swedish):** InstructGPT follows the instruction but writes mostly in English (p. 63).
- **Fig 44 (harmful prompt):** The prompt asks how to steal from a grocery store without getting caught. InstructGPT gives tips. The authors attribute this propensity to prioritizing helpfulness to the user in training data (pp. 61, 63).
- **Fig 45 (code description):** InstructGPT describes a prime sieve. The authors say the model is still far from perfect at this (pp. 61, 64).
- **Figs 46–50 (labeler prompts):** each shows a prompt, the human demonstration, and both models' completions (pp. 65–68).
  - These 5 prompts were selected from 15, so the prompts are lightly cherry-picked and the completions are not (pp. 61, 65).
  - Tasks: bullet-point trends from a passage (46), "serendipity" in a sentence (47), three reading questions (48), shopping list from a recipe (49), ELI5 anxiety lump (50).
  - In Fig 47 GPT-3 repeats instructions, while InstructGPT writes an example sentence.
  - In Fig 48 GPT-3 answers Q1 with Chief Justice John Roberts, whereas the labeler and InstructGPT say the Supreme Court.

## Toy example (ours, not from the text)
Bias entropy for one Winogender-style pair. Suppose the model assigns total probability 0.6 to the "he" completion and 0.2 to the "she" completion.
1. Normalize: $P_{he}=0.6/0.8=0.75$, $P_{she}=0.2/0.8=0.25$.
2. $H=-(0.75\log_2 0.75+0.25\log_2 0.25)$. Here $\log_2 0.75=-0.41504$ and $\log_2 0.25=-2$.
3. $H=0.75\times0.41504+0.25\times2=0.31128+0.5=0.811$ bits.

Other cases:
- Probabilities 0.5 / 0.5 give $H=1$ (the maximum, "no preference").
- Probabilities 0.9 / 0.1 give $H=0.9\times0.152003+0.1\times3.321928=0.1368+0.3322=0.469$ bits (stronger preference).

Averaging $H$ over all 120 pairs gives the reported score. Higher is read as less biased.

## Concepts
- [[alignment-tax]] — here, regressions of PPO models on public NLP datasets, mitigated by pretraining mix (p. 51)
- [[pretraining-mix-ptx]] (new) — adding pretraining-data gradient updates (coefficient γ) during PPO. PPO-ptx is the resulting model (pp. 51, 53)
- [[kl-penalty]] — reward-side KL term with coefficient β against a reference model. Here, raising it to 100× the default did not fix regressions on the 1.3B model (p. 53)
- [[rlhf]] — PPO fine-tuning against a reward model. Here, its ablations: learning rate, batch size, init model (pp. 56–58)
- [[supervised-fine-tuning-sft]] — baseline fine-tuning on demonstrations. Also used as PPO's init model (p. 56)
- [[reward-model]] — preference predictor. Here, its cross-labeler generalization is tested (p. 52)
- [[zero-shot-few-shot-prompting]] — the benchmark settings, with 0 or 2–15 in-prompt examples (pp. 44–50)
- [[entropy-bias-metric]] (new) — entropy of the normalized choice probabilities over minimally different completions. Higher means less preference (p. 44)

## Canonical instances
- [[winogender]] — 120 binary pairs; bias via entropy (p. 45)
- [[crows-pairs]] — 1508 pairs; bias via entropy (p. 45)
- [[realtoxicityprompts]] — toxicity via Perspective API; 5000 prompts with roughly uniform toxicity (p. 45)
- [[truthfulqa]] — 817 questions; true and true+informative metrics (p. 46)
- [[drop-squadv2-regression]] — the two datasets used to track PPO regressions and their recovery (pp. 55, 57)
- [[instruction-following-samples]] — Figs 42–50: other-language, harmful-request, code and labeler-prompt examples (pp. 62–68)

## Bridges (candidates)
- [same-math] Entropy bias metric ↔ information theory: Shannon entropy of a normalized binary distribution — literally $-\sum P\log_2P$.
- [structural-analogy] KL coefficient β ↔ regularization: a strength knob trading validation reward against staying near a reference.
- [structural-analogy] Pretraining mix (ptx) ↔ continual learning: mixing in old-distribution data while training on new objectives to limit forgetting.
- [structural-analogy] Cross-labeler validation ↔ survey methodology: testing whether a model fitted on some annotators predicts held-out annotators.

## Questions this raises
- Why does the pretraining term fix regressions when a 100× larger KL term does not? Is it about the sampled prompts or about the objective?
- Is "higher entropy = less biased" a valid reading, given that a model with no preference could also simply be uncertain?
- Do the labeler-generalization results hold for people outside the training labelers' demographic and cultural group? The test only covers held-out labelers from the same set.
- How can an instructed model be less toxic under a respectful prompt but more toxic under a biased one? What does that say about "alignment"?

## Reading notes
- This part starts at Appendix D (printed p. 44) and ends with Fig 50 (p. 68). Equation 2, Section 4.1, Appendix C.2 and Figure 8 are referred to but not included in these pages. Printed page = pdf page.
- Misprints and oddities visible in the images:
  - QuAC "7.306 examples" (probably 7,306).
  - The CNN/DM and TL;DR few-shot lines say there are 15 additional French / English pairs, apparently copied from the translation table.
  - TruthfulQA calls the same prompt "Instruction prompt" and "helpful instruction".
  - Table 14 has identical CNN/DM and TLDR ROUGE-L rows.
  - Table 14 uses the column label "XL", presumably the 1.3B model, since the figures use 1.3B.
  - The text says the multiple-choice answer is the one with the lowest average per-token log probability. This is probably meant as the best-scoring option, but I report it as printed.
  - E.2 lists inter-group before intra-group accuracy. I report the order as printed.
  - Fig 33 caption has the typo "validatoin".
  - Fig 36's caption calls the blue line "reward value", while its axis is Likert score.
  - Fig 37's fourth bar is labelled as pretraining fraction 0 with 2 epochs, while the text says the chosen setting is 2 epochs with 10% mix.
  - Fig 49's labeler demonstration begins "ucchini" (no initial z) as printed.
  - In Fig 50 the labeler demonstration has garbled quote characters (visible in the image as well as in the text layer).
- Fig 30, 40 and 41 values are read from the images and are approximate. The text of this part does not define "relative toxicity" or "continuity".
