---
id: wei-2022-emergent/main
work: wei-2022-emergent
unit: paper
pages: 1-30
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Emergent Abilities of Large Language Models

## L0 — One line
The paper surveys abilities that are near-random in smaller language models and well above random in larger ones, so they could not have been predicted by extrapolating smaller models, and it asks whether more scaling will bring more.

## L1 — The gist (≤ 120 words)
Scaling language models often improves loss and many tasks in a smooth, predictable way. The authors ask which abilities do not follow this pattern. They call an ability emergent if it is absent in smaller models and present in larger ones. They collect examples from prior work: few-shot tasks, and prompting or finetuning methods that only help at large scale. They discuss possible explanations (task depth, memorization, evaluation metrics), ways to get abilities at smaller scale, emergent risks, and future work. Their analyses give no complete explanation and no way to predict the scale at which emergence occurs. This matters because capabilities of larger future models may be hard to forecast.

**Prerequisites:** what a language model, a benchmark and a scaling curve are; a scaling law (a predictable trend of performance with scale); training compute in FLOPs; cross-entropy loss; exact match (the answer must equal the target exactly); few-shot prompting (Section 3 explains it); BIG-Bench and MMLU (benchmark suites of many tasks or exam topics); GPT-3, LaMDA, Gopher, Chinchilla and PaLM (names of language-model families).

## L2 — Key ideas (5–10 bullets)
- **Definition.** An ability is emergent if it is not present in smaller models but present in larger ones. Hence it cannot be predicted by extrapolating a scaling law from small models (p. 2).
- **Typical curve.** Performance stays near random until a critical scale, then rises well above random. This change is also known as a phase transition (p. 2).
- **Scale has no single proxy, and the threshold is not fixed.** The scale at which an ability is first seen depends on several factors, for example data quality, and not being limited by data amount or parameter count. The paper does not claim any specific scale is required (pp. 2–3).
- **Evidence.** Eight few-shot tasks across five model families (Fig. 2) and several prompting or finetuning techniques (Fig. 3) show this pattern. Table 1 lists the scales (pp. 3–6).
- **Not (only) a metric artifact.** Cross-entropy loss improves at scales where accuracy or exact match stays near random. Partial-credit metrics do not remove emergence, and classification tasks also show it (pp. 7, 19–22).
- **Beyond scaling.** PaLM 62B is above random on 14 BIG-Bench tasks where the larger LaMDA 137B and GPT-3 175B are near random, and better data, training objectives or instruction finetuning may unlock abilities in smaller models. Scale is not the only factor (pp. 7–8).
- **Risks and sociology.** Risks may also emerge unpredictably. Scale has also pushed the field toward general-purpose models (pp. 8–10).
- **Task type.** In BIG-Bench the authors find no clear trend in which kinds of task emerge, and many tasks are still flat (pp. 22–23). In MMLU, Social Science and Humanities jump most from the second-largest to the largest model and STEM least, with similar curve shapes (p. 24).

## L3 — Walkthrough

### Abstract and §1 Introduction (pp. 1–2)
- Scaling up LMs has been shown to improve performance and sample efficiency on many downstream tasks. The effect of scale can often be predicted by scaling laws. For example, cross-entropy-loss scaling curves span more than seven orders of magnitude (p. 1).
- Some downstream tasks counterintuitively do not appear to improve continuously with scale, and such tasks cannot be predicted ahead of time (p. 1).
- Definition of emergence, adapted from Steinhardt (2022) and rooted in Anderson's 1972 essay "More Is Different": "Emergence is when quantitative changes in a system result in qualitative changes in behavior." (p. 2)
- Plan: define emergent abilities (§2). Survey them in few-shot prompting (§3) and augmented prompting strategies (§4). Highlight open questions: why they arise and whether more scaling brings more (§5) (p. 2).
- The survey covers pre-trained Transformer LMs (fn. 1, p. 2).

### §2 Emergent abilities definition (pp. 2–3)
- **Definition.** An ability is emergent if it is not present in smaller models but is present in larger models (p. 2).
- **Pattern.** On a scaling curve (x: model scale, y: performance), performance is near-random until a critical threshold, then rises substantially above random. This is called a *phase transition*: a dramatic change in overall behavior that would not have been foreseen from smaller systems (p. 2).
- **Axes.** Scale is measured mainly by training compute in FLOPs. Parameter-count plots are in Appendix D. The two give similar curve shapes because most dense Transformer families scaled compute roughly in proportion to parameters (p. 2).
- **Dataset size** is not plotted, because many families use a fixed number of training examples for all model sizes (p. 2).
- **No single proxy for scale.**
  - Chinchilla has one-fourth as many parameters as Gopher but similar training compute.
  - Sparse mixture-of-experts models have more parameters per unit of compute than dense models.
  - So emergence may be best seen as a function of many correlated variables. Fig. 4 later uses WikiText103 perplexity, which closely correlates with compute for Gopher/Chinchilla, though maybe not in the long run (p. 2).
- **The emergence scale is not an immutable property of the ability** (p. 3).
  - It may occur at lower compute or fewer parameters with higher-quality data.
  - It also depends on not being limited by data amount, data quality or parameter count.
  - Current LMs are likely not trained optimally.
  - The goal is not to claim a specific scale is required, but to discuss examples from prior work (p. 3).

*Intuition note.* "Emergent" here is defined by what a scaling curve looks like, not by an explanation. The point is that small-model trends would not have forecast the jump. The scale at which a jump appears can shift with data and training.

### §3 Few-shot prompted tasks (pp. 3–4)
- **Setting.** In prompting, a pre-trained LM gets a prompt (e.g. a natural-language instruction) and completes the response, with no gradient updates. Few-shot prompting adds a few input–output examples to the context (Fig. 1: sentiment labels for movie reviews) (p. 3).
- An ability is emergent here when the model is random until some scale and well above random after it. Fig. 2 shows eight cases across five model families (p. 3). Each point in Fig. 2 is a separate model (p. 4).
- **BIG-Bench** (crowd-sourced suite of over 200 benchmarks) (p. 3).
  - Fig. 2A, arithmetic (3-digit add/subtract, 2-digit multiply): GPT-3 and LaMDA have close-to-zero performance for several orders of magnitude of compute. The jump comes at $2\cdot10^{22}$ FLOPs (13B parameters) for GPT-3 and $10^{23}$ FLOPs (68B) for LaMDA (p. 3).
  - Similar behavior at around the same scale appears for IPA transliteration (B), word unscrambling (C) and Persian question answering (D). More in Appendix E (p. 3).
- **TruthfulQA** (E). It is adversarially curated against GPT-3 models, which stay at random even at the largest size. Gopher is random until its largest model ($5\cdot10^{23}$ FLOPs, 280B), which is then more than 20% above random (p. 3).
- **Grounded conceptual mappings** (F). Performance only jumps above random with the largest GPT-3 model (p. 3).
- **MMLU** (G; 57 tests). For GPT-3, Gopher and Chinchilla, models of ~$10^{22}$ FLOPs (~10B) or smaller are no better than guessing on average. At $3$–$5\cdot10^{23}$ FLOPs (70B–280B) they substantially surpass random. The authors call this striking because it *could imply* that solving knowledge questions across many topics *might* require scaling past this threshold, for dense models without retrieval or external memory (p. 3).
- **Word in Context, WiC** (H). GPT-3 and Chinchilla fail to beat random one-shot even at ~$5\cdot10^{23}$ FLOPs. Above-random performance emerged when PaLM reached $2.5\cdot10^{24}$ FLOPs (540B) (p. 4).

*Intuition note.* In all eight cases, a family of models of growing size sits at chance level and then, at one larger size, clearly leaves it. The sizes differ by task and family. Some curves have only a few points, so the exact threshold is imprecise.

### §4 Augmented prompting strategies (pp. 4–5)
- A technique also counts as an emergent ability if it gives no improvement, or hurts, compared with not using it, until applied to a large-enough model (p. 4).
- **Multi-step reasoning.** Chain-of-thought prompting makes the model write intermediate steps before the answer. It surpasses standard prompting only at about $10^{23}$ FLOPs (~100B) (Fig. 3A). A similar emergence was seen when few-shot prompts were augmented with explanations given after the final answer (p. 5).
- **Instruction following.** Finetuning on tasks phrased as instructions lets models follow instructions for unseen tasks. Wei et al. (2022a) found it *hurts* models of $7\cdot10^{21}$ FLOPs (8B) or smaller and improves performance only at $10^{23}$ FLOPs (~100B) (Fig. 3B). Sanh et al. later induced such behavior in smaller encoder-decoder T5 models (p. 5).
- **Program execution.** Finetuning to predict intermediate outputs ("scratchpad") helps on 8-digit addition only for models of ~$9\cdot10^{19}$ FLOPs (40M parameters) or larger (Fig. 3C) (p. 5).
- **Calibration** (does the model know which questions it will get right?). Kadavath et al. compared the True/False technique ("P(True)" that its own proposed answer is correct) with standard methods that compare the probability of the correct answer against other options. The True/False technique's superiority emerges only at the largest scale, ~$3\cdot10^{23}$ FLOPs (52B) (Fig. 3D) (p. 5).

**Table 1 (p. 6)** lists emergent scale as FLOPs / parameters / model.
- *Few-shot:* 3-digit add/subtract $2.3\cdot10^{22}$ / 13B (GPT-3); 4–5 digit $3.1\cdot10^{23}$ / 175B; MMLU 57-topic average $3.1\cdot10^{23}$ / 175B (GPT-3); CivilComments toxicity classification $1.3\cdot10^{22}$ / 7.1B (Gopher); TruthfulQA $5.0\cdot10^{23}$ / 280B and MMLU (26 topics) $5.0\cdot10^{23}$ / 280B (Gopher); grounded mappings $3.1\cdot10^{23}$ / 175B (GPT-3); MMLU (30 topics) $5.0\cdot10^{23}$ / 70B (Chinchilla); WiC $2.5\cdot10^{24}$ / 540B (PaLM); many BIG-Bench tasks.
- *Augmented:* instruction following $1.3\cdot10^{23}$ / 68B (FLAN); scratchpad 8-digit addition $8.9\cdot10^{19}$ / 40M (LaMDA); open-book fact checking $1.3\cdot10^{22}$ / 7.1B (Gopher); chain-of-thought math word problems $1.3\cdot10^{23}$ / 68B (LaMDA); chain-of-thought StrategyQA $2.9\cdot10^{23}$ / 62B (PaLM); differentiable search index $3.3\cdot10^{22}$ / 11B (T5); self-consistency decoding $1.3\cdot10^{23}$ / 68B (LaMDA); leveraging explanations $5.0\cdot10^{23}$ / 280B (Gopher); least-to-most prompting $3.1\cdot10^{23}$ / 175B (GPT-3); zero-shot chain-of-thought $3.1\cdot10^{23}$ / 175B (GPT-3); P(True) calibration $2.6\cdot10^{23}$ / 52B (Anthropic); multilingual chain-of-thought $2.9\cdot10^{23}$ / 62B (PaLM); ask-me-anything prompting $1.4\cdot10^{22}$ / 6B (EleutherAI).

### §5 Discussion (pp. 6–11)
**Main points (pp. 6–7).**
- A range of abilities has so far been observed only in sufficiently large models, so emergence cannot be predicted by extrapolating smaller ones (p. 6).
- Emergent few-shot tasks are also unpredictable because they are not explicitly in pre-training, and we likely do not know the full scope of such tasks (p. 6).
- Tasks LMs cannot do now are prime candidates for future emergence. For example, dozens of BIG-Bench tasks have no above-random result even for the largest GPT-3 and PaLM (Appendix E.4) (p. 6).
- **Historical example: WiC.**
  - GPT-3 at ~$3\cdot10^{23}$ FLOPs (175B) did not get above-random one-shot performance. Brown et al. blamed possibly the architecture or the autoregressive objective, and suggested a bidirectional model of similar size.
  - Later, scaling decoder-only PaLM from $3\cdot10^{23}$ (62B) to $3\cdot10^{24}$ FLOPs (540B) gave a significant jump, without those architectural changes (pp. 6–7).
  - Footnote 3: GPT-3 gets ~55% on the dev set with few-shot (not one-shot) prompting. This did not appear to result from scale and did not hold on the test server (p. 6).

#### 5.1 Potential explanations of emergence (p. 7)
- There are currently few compelling explanations (p. 7).
- Natural intuitions for some tasks: if a reasoning task needs $l$ sequential steps, this *might* need a model with depth of at least $O(l)$ layers. More parameters and training enable better memorization, *which could help* tasks needing world knowledge. Closed-book QA may need enough parameters to hold the compressed knowledge itself (p. 7).
- **Metrics.**
  - Exact string match on long targets *may disguise* compounding small improvements as emergence. The same logic may apply to multi-step problems scored only on the final answer.
  - But a jump in final-answer accuracy does not explain why intermediate-step quality suddenly becomes above random. Metrics without partial credit are at best an incomplete explanation, because emergence is also seen on classification tasks (Fig. 2D–H) (p. 7).
- **Cross-entropy check** (Appendix A; six BIG-Bench tasks, same setup as BIG-Bench 2022). Cross-entropy loss improves even at small scales where exact match, BLEU and accuracy are near random. So downstream metrics *can mask* gains in the log-likelihood of the target. But this does not explain why downstream metrics are emergent, nor predict the scale at which emergence occurs. More work is needed (p. 7).

*Intuition note.* Part of what looks like a sudden jump may be a smooth improvement hidden below a threshold metric. The authors still say this is incomplete: it does not predict when the jump comes, and emergence appears on classification tasks too.

#### 5.2 Beyond scaling (pp. 7–8)
- An ability seen to emerge at one scale may later be achieved at a smaller scale. Scale is not the singular factor (p. 7).
- **14 BIG-Bench tasks** (listed in Appendix F) are near-random for LaMDA 137B and GPT-3 175B, but PaLM 62B is above random despite fewer parameters and FLOPs. Possible reasons, not tested by ablation (too costly): higher-quality data (more multilingual and code data than LaMDA) and architecture differences such as split digit-encodings (p. 7).
- A different pre-training objective may help. Tay et al. (2022c) found that a cheap continued pre-training stage with a mixture-of-denoisers objective enabled emergent performance on several BIG-Bench tasks (p. 7).
- **Once an ability is found, it can get cheaper.**
  - Instruction finetuning first worked only at 68B+ decoder-only models (Wei et al.). Sanh et al. got similar behavior from an 11B encoder-decoder model (pp. 7–8).
  - Ouyang et al.'s InstructGPT (finetuning plus reinforcement learning from human feedback) let a 1.3B model outperform much larger models in human-rater evaluations on a broad set of use cases (p. 8).
- Other routes:
  - Pre-training data features (long-range coherence, many rare classes) correlate with emergent few-shot prompting. Few-shot learning can require certain architectures in some scenarios (Xie et al.; Chan et al.).
  - Threshold frequencies of training data can activate emergent syntactic rule-learning with parameters and FLOPs held constant, with "aha" moments (Wei et al. 2021b) (p. 8).
- **Limits of scaling alone** (p. 8):
  - Scaling may be bottlenecked by hardware.
  - Some abilities may not have emerged yet.
  - Others may never emerge, for example tasks far out of the distribution of even a very large training set.
  - An ability could emerge and then plateau, with no guarantee it reaches the desired level.

#### 5.3 Another view of emergence (p. 8)
- Emergence can also be plotted against WikiText103 perplexity. Fig. 4 puts MMLU accuracy on the y-axis against training FLOPs, parameters and WikiText103 perplexity (p. 8).
- For Gopher and Chinchilla the three plots look similar, because perplexity and FLOPs are highly correlated for these models (p. 8).
- This correlation may fail for new techniques (e.g. retrieval-augmented models may reach low perplexity with less compute). Comparing perplexity across families is complicated by training-data differences. Emergence should probably be seen as a function of many correlated variables (p. 8).

#### 5.4 Emergent risks (pp. 8–9)
- Like abilities, risks could emerge without being in pre-training. Risks of truthfulness, bias and toxicity matter whether or not they are strictly "emergent" by §2, and some increase with scale (Inverse Scaling Prize). Because work on emergence incentivizes scaling, one should watch risks that grow with scale even if not emergent (pp. 8–9).
- Findings summarized from prior work (p. 9):
  - WinoGender (gender bias in occupations) has improved with scale. BBQ found bias can increase with scale in ambiguous contexts.
  - Askell et al.: larger models could give more toxic responses on RealToxicityPrompts, but prompts with examples of being "helpful, harmless, and honest" mitigated this.
  - Larger models were more likely to memorize training data. Deduplication can reduce memorization while improving performance.
  - TruthfulQA: GPT-3 models more often mimicked human falsehoods as they got larger. Rae et al. later showed that on a multiple-choice version, Gopher 280B was substantially better than random (emergent).
- Further emergent risks *might* exist only in future models or be uncharacterized now (e.g. backdoor vulnerabilities, inadvertent deception, harmful content synthesis, from Hendrycks et al.). Proposed approaches: data filtering, forecasting, governance, automatic discovery of harmful behaviors (p. 9).

#### 5.5 Sociological changes (p. 10)
- Another qualitative change is sociological: scale has shifted how the community uses LMs, from task-specific toward "general-purpose" models that aim to do tasks not explicitly in training (p. 10).
- Cases where few-shot prompting of a general-purpose model beat prior state of the art held by finetuned task-specific models (p. 10):
  - GPT-3 175B on TriviaQA and PiQA.
  - PaLM 540B on three arithmetic reasoning benchmarks.
  - Flamingo 80B on six visual question answering benchmarks.
- These are *not necessarily emergent*, since their scaling curves are smooth and predictable (Fig. 13, p. 28). They underscore the sociological shift (p. 10).
- Prompted LMs are used outside NLP research: translating instructions into robot actions, interacting with users, multimodal reasoning. Real-world deployments include GitHub Copilot and OpenAI's GPT-3 API (p. 10).

#### 5.6 Directions for future work (pp. 10–11)
- **Further model scaling.** It has so far increased capabilities but is expensive and needs hardware solutions, so other approaches will likely matter (p. 10).
- **Better architectures and training.** Sparse mixture-of-experts (more parameters at constant compute per input), variable compute per input, more local learning than full backpropagation, external memory. These are promising but not widely adopted (p. 10).
- **Data scaling.** Hoffmann et al. argued prior work underestimated the data needed for a compute-optimal model. More data could allow more emergent abilities at fixed model size (pp. 10–11).
- **Better prompting and its understanding.** Calibrating output probabilities, noisy-channel prompting, intermediate steps in exemplars. Understanding what makes prompting work could show how to elicit emergent abilities at smaller scale (p. 11).
- **Frontier tasks.** Dozens of BIG-Bench tasks (often abstract reasoning, e.g. chess, hard math) are still at or below random. Multilingual emergence: Fig. 2D suggests both PaLM's training data and 62B parameters are needed for Persian QA (p. 11).
- **Understanding emergence.** The paper's analyses (Appendix A.1, A.2, A.3, B) did not fully explain or predict emergence. Suggested: relate emergent tasks to similar training data; build synthetic compositional tasks and track each sub-task with scale (p. 11).

### §6 Conclusions and Broader Impact (p. 11)
- Emergent abilities span many models, tasks and settings. They are a recently discovered outcome of scaling. How they emerge and whether more scaling brings more are important research questions (p. 11).
- The paper says it surveyed results in the existing literature without proposing new methods or models (it also reports its own appendix analyses). It says emergent abilities are unpredictable in several ways and include emergent risks (p. 11).

### Appendix A.1 Cross-entropy analysis (pp. 19–21)
- **Setup.** Six few-shot BIG-Bench tasks emergent for LaMDA. Three are generative (exact match or BLEU): modified arithmetic, IPA transliterate, word unscramble. Three are classification (accuracy): logical arguments, sports understanding, figure of speech (pp. 19–21).
- For small models (≤$10^{22}$ FLOPs / ≤27B params), EM/BLEU/accuracy is near random (p. 19).
- Cross-entropy loss can show progress even when two answers are both wrong, by capturing which is closer in probability (p. 19).
- **Two possible outcomes** (p. 19):
  - Outcome 1: loss also does not improve where the metric is random. Then the model truly does not improve.
  - Outcome 2: loss improves where the metric is random. Then models do improve, but the metric hides it, until a critical scale lifts the metric.
- **Result.** All six tasks fall under Outcome 2. The authors conclude that small models improve in ways the metrics miss, but the tasks are still considered emergent, and there is no straightforward indicator for predicting emergence (p. 19).
- **Generative tasks (Fig. 5).** The error rate is nearly 100% for small models, but loss improves for them. At the point of emergence the authors see an "elbow" in the loss (p. 19).
- **Classification (Fig. 6).** Loss keeps improving while accuracy is near random (p. 19). The log-probabilities of the correct *and* incorrect answers can both decrease, even when probabilities are normalized across options. The reason given: larger models give less extreme probabilities (fewer values near 0 or 1), so average log-probabilities have fewer very small values. For each of the three tasks the two log-probabilities eventually diverge at some scale, when task performance rises substantially (pp. 19–20). Logical arguments has only 32 samples, which may add noise (p. 21).

### Appendix A.2 Different metrics for generative tasks (p. 22)
- Fig. 7 shows three generative tasks (modified arithmetic, IPA transliterate, periodic elements) under all BIG-Bench metrics (exact match, ROUGE variants, BLEURT, BLEU, sequence F1, multiple-choice grade). Emergence is apparent for all metrics. So exact match alone is not a complete explanation for emergence on generative tasks (p. 22).
- Word unscramble and repeat copy logic are excluded because exact match is the only sensible metric for them (word-level partial credit is not valid) (p. 22).

### Appendix A.3 BIG-Bench task analysis (pp. 22–23)
- Two co-authors manually classified all 210 BIG-Bench tasks as emergent or not, using the §3 definition (near-random until a scale, then substantially above). Because "near-random" is subjective, they agreed with confidence on all tasks labeled emergent. Annotations are in Appendix E (p. 22).
- Fig. 8 splits tasks per keyword into emergent with LaMDA/GPT-3, emergent only with PaLM, smoothly increasing, and flat (no model above random). 40 tasks fit none of these (too noisy, not correlated with scale, etc.) (p. 22).
- Counting emergent tasks per keyword mostly reflects common keywords, so percentages are used. Highest percent emergent: analogical reasoning, word sense disambiguation, truthfulness, social reasoning, emotional understanding (p. 22).
- Only two of the top five are reasoning-related. Logical and causal reasoning are not especially emergent. Arithmetic and mathematics had a relatively low percentage emergent, which was unexpected. Overall, no clear trends for which task types are most emergent (pp. 22–23).
- Flat scaling is more intuitive: visual reasoning has the largest flat fraction (8/13). Other high-flat keywords are non-language, repeated interaction, context length, computer code and multi-step. These are weaknesses of LLMs and possible directions for future emergence (p. 23).

### Appendix B Further MMLU analysis (pp. 24–25)
- MMLU has 57 topics in four mutually exclusive categories: Humanities, STEM, Social Science, other (p. 24).
- Social Science and Humanities show the largest jump from the second-largest model (7B) to the largest (70B Chinchilla, 280B Gopher). STEM shows the smallest. At 7B, all four categories are around random (25%). For a given x-axis all four categories have similar curve shapes (Figs. 9, 10) (p. 24).

### Appendix C Model details (p. 26)
- Table 2 gives parameters, training tokens and training FLOPs for GPT-3, LaMDA, Gopher, Chinchilla, PaLM and the Anthropic LM. Models span from LaMDA 2.1M parameters to PaLM 540B with $2.5\cdot10^{24}$ FLOPs, roughly 8× GPT-3's budget (p. 26).
- Examples: GPT-3 175B, 300B tokens, $3.14\cdot10^{23}$ FLOPs; Chinchilla 70B, 1.34T tokens, $5.63\cdot10^{23}$; PaLM 540B, 780B tokens, $2.53\cdot10^{24}$ (p. 26).

### Appendix D Scaling with parameter count (pp. 27–28)
- Figs. 11–13 repeat Figs. 2, 3 and the state-of-the-art comparisons with parameter count on the x-axis (p. 27). Fig. 13 shows few-shot task-general models surpassing prior task-specific state of the art on TriviaQA, Physical QA (GPT-3), GSM8K (PaLM) and OKVQA (Flamingo) (p. 28).

### Appendix E BIG-Bench task classification (pp. 29–30)
- Each task appears in one category (p. 29).
- Lists: smoothly increasing; emergent with GPT-3 or LaMDA (e.g. IPA transliterate, modified arithmetic, strategyqa, word unscrambling); emergent with PaLM; flat (E.4, e.g. checkmate in one, sudoku, python programming challenge; "potential candidates for future emergence"); other (better than random but not correlated with scale; gets worse with scale, e.g. bbq lite; too few examples; incomplete evals) (pp. 29–30).

### Appendix F (p. 30)
- Lists the 14 tasks where PaLM 62B is emergent but GPT-3 175B and LaMDA 137B are not (e.g. anachronisms, emoji movie, logic grid puzzle, metaphor understanding, parsinlu qa) (p. 30).

## Toy example
*(Our own illustration, not from the paper. It shows only one idea from §5.1 and Appendix A.1: smooth gains can hide below a threshold metric. The paper calls this an incomplete explanation of emergence.)*

A model must output a 4-token target exactly. Assume (our simplification) the 4 tokens are independent, and the model's per-token probability of the right token grows smoothly with size.

| Model | $p$ per token | Exact match $=p^4$ | Per-token loss $-\ln p$ | Sequence loss $=4\times$ |
|---|---|---|---|---|
| A | 0.2 | $0.2^4=0.0016$ | 1.609 | 6.44 |
| B | 0.4 | $0.4^4=0.0256$ | 0.916 | 3.67 |
| C | 0.6 | $0.6^4=0.1296$ | 0.511 | 2.04 |
| D | 0.8 | $0.8^4=0.4096$ | 0.223 | 0.89 |
| E | 0.9 | $0.9^4=0.6561$ | 0.105 | 0.42 |

Models A and B look "near-zero" on exact match (0.16% and 2.6%), yet their loss falls from 6.44 to 3.67. Exact match then climbs steeply (0.13 → 0.41 → 0.66). This is the "Outcome 2" pattern of Appendix A.1: loss improves where the downstream metric looks flat. In the paper, however, partial-credit metrics and classification tasks still show emergence, so the paper does not treat this as the whole story.

## Concepts
- [[emergent-ability]] (new) — an ability not present in smaller models but present in larger ones, so not predictable by extrapolating small-model scaling (p. 2).
- [[phase-transition]] (new) — a dramatic change in overall behavior not foreseen from smaller-scale systems; here, near-random → well-above-random as scale grows (p. 2).
- [[scaling-law]] — consistent, predictable performance improvement with scale, e.g. cross-entropy curves over 7+ orders of magnitude (p. 1).
- [[zero-shot-few-shot-prompting]] — giving a pre-trained model a prompt, with or without a few examples, with no gradient updates (p. 3).
- [[chain-of-thought]] — prompting the model to produce intermediate steps before the final answer (p. 5).
- [[instruction-finetuning]] (new) — finetuning on tasks phrased as instructions so the model follows instructions for unseen tasks (p. 5).
- [[scratchpad]] (new) — finetuning a model to output intermediate computation steps (p. 5).
- [[calibration]] (new) — whether a model can predict which questions it will answer correctly; compared via P(True) versus option probabilities (p. 5).
- [[cross-entropy-log-loss]] — loss used in scaling laws. It can improve at scales where accuracy, exact match or BLEU stay near random (pp. 7, 19).
- [[perplexity]] — here, language-model perplexity on WikiText103, used as an alternative x-axis for emergence (p. 8).
- [[compute-optimal-training]] — Hoffmann et al.'s argument that more training data is needed than earlier work implied; the paper cites it for data scaling (pp. 10–11).
- [[mixture-of-experts]] (new) — sparse models with more parameters per unit of compute than dense models (pp. 2, 10).

## Canonical instances
- [[big-bench]] — crowd-sourced suite of over 200 tasks; source of many emergent-task examples and of the classification in Appendix A.3 (pp. 3, 22).
- [[mmlu-benchmark]] — 57-topic test; near-random at ≤~10B and well above random at 70B–280B (p. 3).
- [[truthfulqa]] — adversarially curated against GPT-3; Gopher 280B emerges (p. 3).
- [[wic-benchmark]] — GPT-3 fails; PaLM 540B succeeds without architecture change (pp. 4, 6–7).
- [[wikitext103-perplexity]] — alternative x-axis to scale for MMLU emergence (p. 8).
- [[palm-62b-vs-gpt3]] — smaller model above random on 14 tasks where larger GPT-3/LaMDA are not (p. 7).

## Bridges (candidates)
- [metaphor] Emergence in the paper's sense ↔ physics: Anderson's "more is different" and phase transitions — the paper takes the framing, but its definition is only about scaling-curve shape (p. 2).
- [structural-analogy] Smooth latent improvement hidden by a threshold metric (exact match) ↔ measurement in statistics: thresholding a continuous variable can create apparent jumps — both give a sudden metric change from smooth underlying change (pp. 7, 19).
- [metaphor] Unpredictable new capabilities at larger LLM scale ↔ computational social science: LLM-based simulation tools whose fidelity may not be forecast from smaller models.

## Questions this raises
- If cross-entropy improves smoothly before a jump, can the loss curve plus some task-specific link function predict the scale at which a metric rises? The paper says its analysis does not show this (p. 7).
- Are the thresholds in Figs. 2–3 stable? Each curve has few model sizes, and families differ in data and architecture. How much of the "critical scale" is really data quality or objective (§5.2)?
- Why are tasks like arithmetic less often emergent than analogical reasoning or word sense disambiguation (pp. 22–23)?
- Which risks might emerge at scale, and how could they be found before deployment (p. 9)?

## Reading notes
- Page numbers: printed = pdf for all pages (offset 0).
- This is a survey. It reports results from prior work, mostly as small plots, some with few points; threshold scales in the text are approximate (marked with ~).
- Inconsistencies seen in the pages:
  - Calibration (P(True)) model: text on p. 5 gives ~$3\cdot10^{23}$ FLOPs and Table 1 gives $2.6\cdot10^{23}$ for the 52B model. Table 2 (p. 26) gives $2.65\cdot10^{22}$ for 52B, below the 12B entry ($6.12\cdot10^{22}$) with the same 850B tokens. This looks like an exponent misprint, but the pages do not say so.
  - Scratchpad: p. 5 and Table 1 say 40M parameters at $8.9\cdot10^{19}$ FLOPs. Table 2 lists $8.90\cdot10^{19}$ for a 57M LaMDA model and has no 40M entry.
  - Instruction-following: Table 1 gives $1.3\cdot10^{23}$ / 68B, while p. 5 says $10^{23}$ / ~100B.
  - Chain-of-thought (math word problems): p. 5 says $10^{23}$ / ~100B, while Table 1 gives $1.3\cdot10^{23}$ / 68B.
  - A.1 says "≤27B params" for small models, but Table 2 lists LaMDA sizes 8.6B, 29B, 69B.
  - Table 2 prints "[sic] 199B" tokens for Chinchilla 7.1B.
  - "Periodic elements" is shown as an emergent generative task in Fig. 7C, but it is listed under "Smoothly increasing" in Appendix E.1.
  - In Fig. 5 (word unscramble), the cross-entropy loss rises again at the largest model, which the "elbow" description does not mention.
  - In Fig. 10, the Chinchilla "Other" panel appears to end higher than Social Science. Fig. 9 seems to show the reverse. I read these only from small plots and could not reconcile them with the text's claim that Social Science is most emergent.
- Fig. 2 caption: A–D are 2-shot. WiC is described as one-shot in the text (p. 4).
- The paper has no equations or exercises.
