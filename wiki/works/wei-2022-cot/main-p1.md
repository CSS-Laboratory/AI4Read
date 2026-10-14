---
id: wei-2022-cot/main-p1
work: wei-2022-cot
unit: paper (part 1/2) — Sections 1–8 and Appendices A–B (Tables 1–7)
pages: 1–23
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (part 1: main text and Appendices A–B)

## L0 — One line
If few-shot prompt examples include the intermediate reasoning steps in natural language, sufficiently large language models solve multi-step reasoning tasks much better, with no finetuning.

## L1 — The gist (≤ 120 words)
The paper asks whether large language models can do multi-step reasoning when their few-shot examples show worked steps instead of bare answers. Each example gets a "chain of thought": a series of natural-language intermediate steps. With models of roughly 100B parameters or more, this improves arithmetic, commonsense and symbolic tasks. Smaller models do not gain, and often get worse. PaLM 540B with eight examples sets a new best on GSM8K. Three ablations (equation only, dots only, reasoning after the answer) do not match the gain on GSM8K, and prompts from different annotators still beat standard prompting by a large margin. It matters because it needs no large training set or finetuning, and one model can serve many tasks.

**Prerequisites:** few-shot prompting (examples placed in the prompt); accuracy as "solve rate"; the idea of model size in parameters; basic arithmetic word problems. Terms used above: finetuning = further training of a model on a task; PaLM = a very large language model; GSM8K = a set of grade-school math word problems; ablation = removing or changing one part of a method to test what it contributes.

## L2 — Key ideas (5–10 bullets)
- **Method.** Prompt exemplars become triples ⟨input, chain of thought, output⟩. The chain of thought is a series of natural-language intermediate steps. The model imitates it on the new question (pp. 2–3).
- **Emergence with scale.** Chain of thought gives gains only at about 100B parameters and up. Smaller models write fluent but illogical chains and do worse than with standard prompting (p. 4).
- **Biggest gains on hard problems.** GSM8K has the lowest baseline. Performance more than doubled for the largest GPT and PaLM models. On one-step problems, gains were negative or very small (p. 5).
- **State of the art.** PaLM 540B with chain of thought reaches 56.9% on GSM8K, against 17.9% with standard prompting and 55% for the prior best finetuned system (pp. 2, 20).
- **Ablations.** Equation-only, dots-only (extra computation) and reasoning-after-answer prompts do not reproduce the gain on GSM8K. The authors suggest that natural-language intermediate steps appear useful (pp. 5–6).
- **Robustness, with caveats.** Different annotators and exemplar sets all still beat standard prompting; results were also relatively stable across exemplar orders and, generally, across exemplar counts. Variance is large in places (coin flip: 99.6% vs 71.4%), and prompt engineering still matters (pp. 6, 18).
- **Breadth.** The method helps on commonsense tasks (small gain on CSQA). It also lets PaLM generalise to longer symbolic inputs than the exemplars show (pp. 7–8).
- **Limits.** The authors leave open whether the model really "reasons". Chains can be wrong, annotation could be costly for finetuning, and serving large models is costly (p. 9).

## L3 — Walkthrough

### Abstract and 1 Introduction (pp. 1–2)
- **Claim.** Generating a chain of thought (a series of intermediate reasoning steps) improves complex reasoning in large language models (LLMs). This ability "emerges naturally" in sufficiently large models via chain-of-thought prompting, where a few demonstrations are given as exemplars (p. 1).
- **Figure 1 example (p. 1).**
  - Both prompts contain the exemplar question about Roger's tennis balls (5 balls, plus 2 cans of 3).
  - The standard exemplar answers with just the number 11. The chain-of-thought exemplar adds: Roger started with 5 balls; 2 cans of 3 is 6 balls; 5 + 6 = 11.
  - On the cafeteria question (23 apples, 20 used, 6 bought), the standard-prompted model outputs 27, which is wrong.
  - The chain-of-thought model writes 23 − 20 = 3, then 3 + 6 = 9, and answers 9, which is correct.
- **Two motivating ideas (p. 2).**
  - (i) Arithmetic reasoning can benefit from natural-language rationales. Earlier work trained from scratch (Ling et al., 2017) or finetuned (Cobbe et al., 2021), or used formal languages.
  - (ii) LLMs allow in-context few-shot learning via prompting. This avoids finetuning a separate checkpoint per task.
- **Limitations of each (p. 2).**
  - Rationale-based training is costly, because high-quality rationales are hard to write at scale.
  - Standard few-shot prompting works poorly on reasoning tasks and often does not improve much with model scale (Rae et al., 2021).
- **Combination (p. 2).** Few-shot prompts made of triples ⟨input, chain of thought, output⟩. A prompting-only approach needs no large training set, and one checkpoint can do many tasks (p. 2).
- **Figure 2 (p. 2), GSM8K solve rate.** The bars read 33 (finetuned GPT-3 175B), 55 (prior best), 18 (PaLM 540B standard prompting), 57 (PaLM 540B chain of thought). The first two are from Cobbe et al. (2021).

> **Intuition note.** The idea joins two things: showing the steps (which helped finetuned models) and giving examples in the prompt (which needs no training). So the model is shown how to think in the prompt, not taught by gradient updates.

### 2 Chain-of-Thought Prompting (pp. 2–3)
- **Definition.** A chain of thought is a coherent series of intermediate reasoning steps leading to the final answer. People do this, e.g. a person might say that after Jane gives 2 flowers to her mom she has 10, then 7 after giving 3 to her dad, so the answer is 7 (p. 2).
- **Claim.** Sufficiently large models can generate chains of thought if the few-shot exemplars demonstrate them (pp. 2–3).
- **Naming (p. 3).** The chain can be read as a solution. The authors call it a chain of thought because it mimics step-by-step thinking, and because solutions or explanations usually come after the answer.
- **Four attractive properties (p. 3).**
  1. In principle it decomposes multi-step problems, so more computation can go to problems needing more steps.
  2. It gives an interpretable window into model behaviour and a chance to debug. Fully characterising the model's computation is still open.
  3. It can be used for math word problems, commonsense and symbolic tasks. It is potentially applicable, at least in principle, to any task humans solve via language.
  4. It can be elicited in sufficiently large off-the-shelf models just by adding such examples to the exemplars.

### 3 Arithmetic Reasoning (pp. 3–7)

**3.1 Experimental setup (pp. 3–4).**
- **Benchmarks (p. 3).** Five math word-problem sets: GSM8K, SVAMP, ASDiv, AQuA (algebraic, multiple choice), MAWPS.
- **Standard prompting (p. 3).** The baseline is few-shot prompting as in Brown et al. (2020): exemplars are question–answer pairs and the model answers directly.
- **Chain-of-thought prompting (pp. 3–4).**
  - Each exemplar is augmented with a chain of thought.
  - The authors manually composed eight exemplars (Appendix Table 20) and used this single set for all benchmarks except AQuA, which got four training-set exemplars (Table 21).
  - These exemplars did not undergo prompt engineering. Robustness is studied in 3.4 and Appendix A.2.
- **Models (p. 4).**
  - GPT-3: text-ada-001, babbage-001, curie-001 and davinci-002, which the authors say "presumably correspond" to 350M, 1.3B, 6.7B and 175B.
  - LaMDA: 422M, 2B, 8B, 68B, 137B.
  - PaLM: 8B, 62B, 540B.
  - UL2 20B, and Codex (code-davinci-002).
- **Decoding (p. 4).** Greedy decoding. LaMDA results are averaged over five seeds, each a different random order of exemplars. Variance was not large, so other models use one exemplar order.

**3.2 Results (pp. 4–5).** Three takeaways:
1. **Emergent ability of scale (p. 4).** Chain of thought does not help small models and gives gains only at about 100B parameters. Smaller models produced fluent but illogical chains, which lowered performance below standard prompting.
2. **Larger gains on harder problems (p. 5).**
   - GSM8K has the lowest baseline. Performance more than doubled for the largest GPT and PaLM models.
   - On SingleOp, the easiest MAWPS subset (one step), improvements were negative or very small.
3. **Competitive with prior state of the art (p. 5).**
   - PaLM 540B sets a new best on GSM8K, SVAMP and MAWPS. Standard prompting had already passed the prior best on SVAMP.
   - On AQuA and ASDiv, PaLM with chain of thought reaches within 2% of the prior best.

Selected numbers (Table 1, p. 20; accuracy %):

| Model | GSM8K standard → CoT | + external calculator |
|---|---|---|
| LaMDA 137B | 6.5 → 14.3 | 17.8 |
| GPT-3 175B | 15.6 → 46.9 | 49.6 |
| Codex | 19.7 → 63.1 | 65.4 |
| PaLM 540B | 17.9 → 56.9 | 58.6 |

- **Scale pattern (Table 2, p. 21).**
  - On GSM8K, LaMDA 420M: 2.6 → 0.4, and 8B: 3.2 → 1.6. PaLM 8B: 4.9 → 4.1.
  - PaLM 62B: 9.6 → 29.9. PaLM 540B: 17.9 → 56.9.
  - Chain of thought hurts small models and helps large ones.
- **Mistakes in chains.**
  - Manual inspection of LaMDA 137B on GSM8K (p. 5). Of 50 random correct-answer examples, all chains were logically and mathematically correct except two that reached the right answer by coincidence.
  - Of 50 random wrong-answer examples, 46% of chains were almost correct, with minor mistakes (calculator error, symbol mapping error, one step missing). The other 54% had major errors in semantic understanding or coherence.
  - A similar analysis of PaLM 62B found that scaling to 540B fixes a large portion of one-step-missing and semantic-understanding errors (details in A.1 below).

> **Intuition note.** Showing steps does not help a model that cannot carry out the steps. Small models write plausible-sounding but broken steps. Only larger models turn the extra text into a better answer.

**3.3 Ablation study (pp. 5–6).** The question is whether other kinds of prompting give the same gains. Figure 5 uses LaMDA 137B and PaLM 540B on GSM8K.
- **Equation only (p. 5).**
  - The model outputs only the equation before the answer.
  - It does not help much on GSM8K. The authors infer that GSM8K semantics are too hard to translate directly into an equation without natural-language steps.
  - For one-step or two-step datasets it does improve performance, since the equation is easily derived.
  - In Table 6 (LaMDA 137B), GSM8K equation-only is 5.4, versus 6.5 standard and 14.3 chain of thought. SVAMP: 35.1, versus 29.5 and 36.7.
- **Variable compute only (p. 6).**
  - The model outputs only dots (. . .), as many as the characters in the equation needed to solve the problem.
  - This performs about the same as the baseline. The authors suggest that variable computation alone is not the reason for success, and that expressing intermediate steps in natural language appears useful.
- **Chain of thought after answer (p. 6).**
  - The chain is given only after the answer. This tests whether the model depends on the produced chain, or whether prompts just help it access knowledge from pretraining.
  - It performs about the same as the baseline. The authors suggest the sequential reasoning in the chain is useful beyond just activating knowledge.

> **Intuition note.** Each ablation tests one possible explanation. Extra tokens alone (dots), computing in equation form alone, or priming knowledge alone do not match the full effect on GSM8K. That suggests the natural-language steps, written in sequence, are doing useful work.

**3.4 Robustness (pp. 6–7).**
- **Background (p. 6).** Few-shot prompting can be sensitive to exemplars. For example, permuting exemplars moves GPT-3 on SST-2 from 54.3% to 93.4% (Zhao et al., 2021).
- **Annotators (p. 6).**
  - Annotator A wrote the original chains. Co-authors B and C independently wrote chains for the same exemplars (Appendix H).
  - A also wrote a more concise version in the style of Cobbe et al. (2021); it merges the original short sentences into fewer ones (footnote 1).
- **Results (Fig. 6, LaMDA 137B).** There is variance among annotations, as expected for exemplar-based prompting. All chain-of-thought prompt sets beat the standard baseline by a large margin. The authors conclude that success does not depend on a particular linguistic style.
- **Independent exemplars (p. 7).**
  - Three sets of eight exemplars were randomly sampled from the GSM8K training set, whose examples already contain reasoning steps written by others.
  - These performed comparably to the manual ones and far above standard prompting.
  - Footnote 2: only examples with ≤ 60 tokens and ≤ 2 solution steps were sampled.
- **Further robustness (p. 7).** Arithmetic chain of thought is also robust to exemplar order and number of exemplars (Appendix A.2).

Selected Table 6 values, LaMDA 137B (p. 23):

| Setting | GSM8K | MAWPS |
|---|---|---|
| Standard | 6.5 | 43.2 |
| Chain of thought | 14.3 | 57.9 |
| Annotator C | 17.6 | 60.1 |
| Concise style | 11.1 | 59.6 |
| GSM8K exemplars (α) | 12.6 | 53.9 |

### 4 Commonsense Reasoning (p. 7)
- **Motivation.** Chain of thought is language-based, so it applies to commonsense problems about physical and human interactions. These presume general background knowledge (p. 7).
- **Benchmarks (p. 7).**
  - CSQA: commonsense questions.
  - StrategyQA: infer a multi-hop strategy.
  - BIG-bench Date Understanding and Sports Understanding (plausible or implausible sentence).
  - SayCan: map an instruction to a sequence of robot actions.
  - Examples with chains are in Figure 3 (p. 4).
- **Prompts (p. 7).**
  - For CSQA and StrategyQA, training-set examples with manually written chains.
  - For the two BIG-bench tasks (no training sets), the first ten evaluation examples serve as exemplars; results are reported on the rest.
  - For SayCan, six training examples from Ahn et al. (2022) with manual chains.
- **Results (Fig. 7, PaLM).**
  - Scaling improved standard prompting on all tasks. Chain of thought gave further gains, appearing largest for PaLM 540B.
  - The text reports StrategyQA 75.6% vs prior best 69.4%, and sports understanding 95.4% vs an unaided sports enthusiast's 84%.
  - The gain was minimal on CSQA. In Table 4 (p. 22), PaLM 540B on CSQA goes 78.1 → 79.9.
  - Table 4 also shows that for GPT-3 175B, chain of thought lowers CSQA (79.5 → 73.5) and StrategyQA (65.9 → 65.4).

> **Intuition note.** The method is not tied to arithmetic. Anything where saying the intermediate facts helps, such as noting that Joao Moutinho is a soccer player and the NFC championship is American football (Figure 3), can use it. The gain depends on the task and model.

### 5 Symbolic Reasoning (p. 8)
- **Tasks (p. 8).**
  - Last-letter concatenation: join the last letters of the words in a name ("Amy Brown" → "yn"). Names come from the top one thousand first and last names in census data.
  - Coin flip: after people flip or do not flip a coin, is it still heads up? (a coin starts heads up, Phoebe flips it and Osvaldo does not; the answer is "no").
  - First-letter concatenation is easier, and models can already do it without a chain. GPT-3 davinci got all but one correct on 10 common names (footnote 3).
- **In-domain vs OOD (p. 8).**
  - In-domain tests have the same number of steps as the exemplars.
  - Out-of-domain (OOD) tests have more steps. Exemplars have 2-word names or 2 flips; tests use 3 and 4 words or flips (footnote 4: for longer names, several first and last names are concatenated).
  - The chains are in Figure 3.
- **Results (Fig. 8; Table 5, p. 22).**
  - PaLM 540B with chain of thought reaches almost 100% in-domain (letters 99.4, coin 100.0). Standard prompting already solves coin flip for PaLM 540B (98.1) but not for LaMDA 137B (49.0 vs 99.6 with chain of thought).
  - The authors call these "toy tasks": the chain already supplies the solution structure, and the model only repeats the steps with new symbols. Even so, small models fail. The ability to do these abstract manipulations on unseen symbols arises only at about 100B parameters.
  - OOD: standard prompting fails on both tasks. With chain of thought, scaling curves go upward, though below in-domain levels.
  - PaLM 540B OOD with chain of thought: letters 94.8 (3 words) and 63.0 (4 words); coin 98.6 (3 flips) and 90.2 (4 flips).
  - The authors conclude that chain of thought facilitates length generalisation beyond seen chains, for models of sufficient scale.

> **Intuition note.** Standard prompting gives the model no steps to copy, so a longer input is just a new problem. With a chain, the model can repeat the same step pattern one more time.

### 6 Discussion (pp. 8–9)
- **Summary (pp. 8–9).** Chain of thought improves arithmetic performance by a large margin, much more than the ablations, and robustly across annotators, exemplars and models. Its linguistic nature gives broad applicability. It facilitates OOD length generalisation in symbolic tasks. No model was finetuned (p. 9).
- **Scaling (p. 9).**
  - For many reasoning tasks where standard prompting has a flat scaling curve, chain of thought gives dramatically increasing curves.
  - The authors say their work underscores that standard prompting only provides a lower bound on LLM capabilities. They add that this likely raises more questions than it answers, for instance: how much more reasoning gain from larger scale, and which other prompting methods could expand the tasks solvable.
- **Limitations (p. 9).**
  1. Emulating human thought processes does not answer whether the network is actually "reasoning". This is left open.
  2. Annotation cost is minimal in the few-shot setting but could be prohibitive for finetuning (possibly solved by synthetic data or zero-shot generalisation).
  3. There is no guarantee of correct reasoning paths, so chains can lead to correct or incorrect answers.
  4. Emergence only at large scale makes serving costly. Inducing reasoning in smaller models is future work.

### 7 Related Work (p. 9)
- **Intermediate steps.** Ling et al. (2017) pioneered natural-language rationales for math word problems. Cobbe et al. (2021) extended this with a larger dataset and finetuning. Nye et al. (2021) had models predict Python program outputs by first predicting line-by-line intermediate results, which performed better than direct prediction.
- **Prompting.** Other approaches improve or augment the input part of the prompt (learned prompts, instructions). This work is orthogonal: it augments the outputs with a chain of thought.

### 8 Conclusions (p. 9)
Chain-of-thought reasoning is described as an emergent property of model scale. It lets sufficiently large LLMs perform reasoning tasks that otherwise have flat scaling curves.

### Checklist (p. 15) and References (pp. 10–14)
The checklist says that the coin flip and last-letter concatenation datasets are the only new assets, given in the supplementary materials, and that inputs, outputs and targets for LaMDA and GPT-3 are also in the supplementary material. References are not digested.

### Appendix A — Frequently Asked Questions (pp. 16–19)

**A.1 Why does scale improve chain of thought? (p. 16)**
- Chain of thought is emergent in the sense that its success cannot be predicted only by extrapolating the performance of small-scale models. It hurts performance for most models smaller than 10B parameters.
- **Error analysis (Fig. 9).** The authors manually read 45 errors of PaLM 62B, in three categories. Scaling to 540B fixed a substantial portion in all three.

| Category | 62B errors | Fixed by 540B |
|---|---|---|
| Semantic understanding | 20 | 6 |
| One step missing | 18 | 12 |
| Other (hallucination, repetition, symbol mapping) | 7 | 4 |

- Figure 10 (p. 17) gives examples. In the wire problem (4 feet cut into 6-inch pieces), 62B computes 4 · 6 = 24, while 540B converts to 48 inches and gets 48/6 = 8.
- This result "appears consistent with" the hypothesis that LMs acquire semantic understanding and logical reasoning skills with scale. Model scale is often conflated with other factors such as training compute.
- **Why small models fail (p. 16).** They fail at easy symbol-mapping tasks (Section 5). They seem to have inherently weaker arithmetic. They often produce no parseable final answer (repetition, or logic that never ends).
- The authors conclude that the phenomenon is complicated, likely involving several emergent abilities. Which pretraining data, architecture and objective causally enable it is left to future work.

**A.2 Role of prompt engineering (pp. 17–18)**
- **Different annotators.** Chain of thought beat the baseline by a large margin for all three annotators on eight datasets (Tables 6–7). Annotators were given no specific writing instructions.
- **Annotators without ML background.** The GSM8K training chains, written by crowd workers, also beat the baseline by a large margin on all four arithmetic datasets (Table 6). The authors conclude it does not depend on a particular annotator set.
- **Different exemplars.** Every GSM8K exemplar set was tested on all four arithmetic datasets. This suggests exemplars need not come from the test distribution.
- **Order.** Standard deviations over orders are relatively minimal in almost all cases. The exception is coin flip, with high deviation. The authors suggest the Zhao et al. (2021) reason: many same-category exemplars in a row bias outputs.
- **Number of exemplars.** Gains generally still held (Figure 11, five datasets). In preliminary experiments, going from 8 to 16 standard-prompting exemplars did not help standard prompting catch up.
- **Different models.** The same prompts improved all three models (LaMDA, GPT-3, PaLM) on all datasets except CSQA and StrategyQA for GPT-3. This incomplete transfer is named a limitation.
- **Prompt engineering still matters.**
  - Coin flip varied from 99.6% (Annotator A) to 71.4% (Annotator C), both above standard prompting (stated as 50.0%).
  - For reversing a list of 5 items, two co-authors could not write a working chain, while a third wrote one that solved it perfectly.
  - A suggested direction is to have an LLM generate chains via prompting, possibly optimised on a validation set.

**A.3 Will it help my task? (pp. 18–19)** The authors' "intuition" is that chain of thought helps most when three conditions are met: (1) the task is challenging and needs multi-step reasoning, (2) a large model is used, (3) the scaling curve is relatively flat. Benefits are smaller when one or more fail. Perhaps supporting evidence (arithmetic results): the largest gain is PaLM 540B on GSM8K. The gain is small on MAWPS subsets SingleOp, SingleEq, AddSub, where PaLM 540B already scores 90% or higher (and there is less headroom). Other tasks such as machine translation are left to future work (p. 19).

**A.4 Why equation-only fails on GSM8K (p. 19).** The authors believe, from qualitative analysis, that GSM8K questions are too semantically challenging to translate directly into one equation. Example (LaMDA 137B): Mike scores 4 points in the first 20 minutes and 25% more in the second 20.
- Equation only: the model writes (4 + 20 * 0.25) = 6 and answers 6 — wrong.
- Chain of thought: 4 × 1.25 = 5 in the second period, so 9 points in total — correct.

> **Intuition note.** The equation must hold the whole problem in one expression. A chain lets the model handle one clause at a time ("25% more" → 4 × 1.25 = 5).

### Appendix B — All experimental results (pp. 20–23)
- **External calculator (p. 20).** Some chains had correct equations but a wrong arithmetic operation. The authors add a Python program (`eval`) as a post-hoc external calculator for all equations in the chain. Results are propagated between equations by string matching. Table 1 shows this boosts performance on most tasks.
- **Table 1 (p. 20), other entries.**
  - Prior best (finetuned): GSM8K 55, SVAMP 57.4, ASDiv 75.3, AQuA 37.9, MAWPS 88.4.
  - PaLM 540B chain of thought: 56.9, 79.0, 73.9, 35.8, 93.3.
  - LaMDA 137B on AQuA: 25.5 → 20.6 (−4.9), a drop.
- **Tables 2–3 (p. 21).** Full scale results for arithmetic and MAWPS subsets. Small models are generally worse with chain of thought. On easy subsets gains are minimal (PaLM 540B SingleOp 94.1 / 94.1). On MultiArith, large models gain much (GPT-3 175B: 33.8 → 91.7).
- **Table 4 (p. 22).** Commonsense results. PaLM 540B: StrategyQA 68.6 → 77.8, Date 49.0 → 65.3, Sports 80.5 → 95.4, SayCan 80.8 → 91.7.
- **Table 5 (p. 22).** Symbolic results (see Section 5 above).
- **Tables 6–7 (p. 23).**
  - Table 6 gives LaMDA 137B ablations and robustness with standard deviations over five exemplar orders.
  - Table 7 gives Date, Sports, SayCan, Concat and Coin (LaMDA 137B, except SayCan on PaLM).
  - Table 7 coin: standard 49.0 ± 2.1, chain of thought 99.6 ± 0.3, Annotator C 71.4 ± 11.1.
  - In Table 7, reasoning-after-answer on Concat is 0.0, below the standard 5.8.

## Toy example (ours, not from the paper)
**Problem:** "A shelf has 4 boxes with 6 pens each. 5 pens are given away. How many pens are left?"

- **Standard exemplar** (Fig. 1 style): "Q: Roger has 5 tennis balls… A: The answer is 11." The model must jump from the numbers 4, 6, 5 straight to a number.
- **Chain-of-thought exemplar:** "A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11."
- **Chain-of-thought output we would hope for:** "There are 4 boxes with 6 pens each, which is 4 × 6 = 24 pens. 5 are given away, so 24 − 5 = 19. The answer is 19."
- **Ablation versions of the exemplar answer:**
  - Equation only: "4*6-5 = 19. The answer is 19."
  - Dots only: the equation "4*6-5" has 5 characters, so the model prints "….." (5 dots), then the answer.
  - After answer: "The answer is 19. 4 × 6 = 24, 24 − 5 = 19." The chain comes too late to guide the answer.
- **Measuring the gain.** Suppose (hypothetical) a model solves 1 of 8 test problems with standard prompting (12.5%) and 4 of 8 with chain of thought (50%). The ratio is 50 / 12.5 = 4, so performance "more than doubled" (ratio above 2).
- **Paper's real numbers (PaLM 540B, GSM8K, Table 1):** 56.9 − 17.9 = 39.0 points. The ratio is 56.9 / 17.9 ≈ 3.18.

## Concepts
- [[chain-of-thought]] — a series of natural-language intermediate reasoning steps leading to the final answer, shown in exemplars and produced by the model (p. 2)
- [[zero-shot-few-shot-prompting]] — here, few-shot prompting: input–output exemplars placed in the prompt before the test question (pp. 2–3)
- [[in-context-learning]] — a model performs a task from prompt examples alone, with no finetuning (p. 2)
- [[emergent-ability]] — chain of thought gives gains only at about 100B parameters and up; its success cannot be predicted only by extrapolating from small models (pp. 4, 16)
- [[pretraining-fine-tuning]] — used as a contrast: the paper's method needs no finetuning, only prompting (pp. 2, 9)
- [[scaling-law]] — used loosely: "scaling curve" is performance against model size. For many reasoning tasks, chain of thought turns flat curves into rising ones (p. 9)
- [[standard-prompting]] (new) — baseline few-shot prompting where exemplars give the answer directly, with no chain (p. 3)
- [[exemplar]] (new) — a worked example in the prompt. Here it is a ⟨input, chain of thought, output⟩ triple (p. 2)
- [[greedy-decoding]] (new) — the decoding method used to sample from the models in these experiments (p. 4)
- [[ood-length-generalization]] (new) — test inputs with more steps than the exemplars (3–4 vs 2 words or flips) (p. 8)
- [[external-calculator]] (new) — post-hoc Python evaluation of equations in a generated chain, so arithmetic slips in the chain are corrected (p. 20)
- [[prompt-sensitivity]] (new) — performance varies with annotator, exemplars and order. Prompt engineering still matters (pp. 6, 18)

## Canonical instances
- [[gsm8k]] (new) — the arithmetic benchmark with the lowest baseline here. PaLM 540B reaches 56.9% with chain of thought, against 17.9% standard (pp. 2, 20)
- [[roger-tennis-balls]] (new) — the Figure 1 exemplar contrasting standard and chain-of-thought answers (p. 1)
- [[palm-540b-gsm8k-sota]] (new) — a new best result from prompting alone, surpassing finetuned GPT-3 with a verifier (pp. 1–2)
- [[coin-flip-task]] (new) — symbolic state tracking; shows length generalisation (p. 8)
- [[last-letter-concatenation]] (new) — symbolic task; PaLM 540B reaches 99.4% in-domain with chain of thought (pp. 8, 22)
- [[sayCan-robot-planning]] (new) — commonsense task mapping an instruction to robot actions (pp. 7, 4)

## Bridges (candidates)
- [structural-analogy] chain-of-thought prompting ↔ llm: scratchpads (Nye et al. 2021, cited here) — both have the model write intermediate steps before the answer (p. 9)
- [structural-analogy] prompt sensitivity across annotators and exemplar order ↔ survey methodology: question-wording and order effects — both are outputs depending on how the instrument is phrased
- [metaphor] chain of thought as extra computation per problem ↔ computation: time spent per instance — the paper says this holds "in principle" (p. 3), and its dots-only test does not support it as a sufficient cause (p. 6)

## Questions this raises
- What exactly makes steps useful beyond more tokens? The dots-only and after-answer ablations rule out some explanations, but the paper admits it does not know whether the model "reasons" (pp. 6, 9).
- Does the written chain faithfully show how the model reached its answer? The paper offers an "interpretable window" but also says a correct answer can come with a wrong path, and fully characterising the computation is open (pp. 3, 9).
- Can smaller models be made to benefit, e.g. by finetuning on chains or synthetic chains? The authors leave this as future work (p. 9).
- How far does the "three conditions" intuition (hard task, big model, flat curve) predict where chain of thought helps? It was tested only on this paper's tasks (p. 18).

## Reading notes
- **Where this part starts and ends.** It covers the whole main text (Sections 1–8, printed pp. 1–9), acknowledgements, references (pp. 10–14), the checklist (p. 15), Appendix A (FAQ, pp. 16–19) and Appendix B (Tables 1–7, pp. 20–23). Appendices C, D, E, G and H are referred to in the text but are not in these pages. The split is at a section boundary, so a second part presumably holds the remaining appendices.
- **Page numbers.** Printed = pdf (offset 0).
- **Text-layer problem.** The arXiv stamp on pdf 1 is garbled in the text layer; the title page image is clear.
- **Number conflicts in the source (checked against the images):**
  - Section 4 text reports PaLM 540B StrategyQA as 75.6% (prior best 69.4%). Table 4 gives 77.8 for chain of thought (68.6 standard).
  - Tables 1 and 2 give LaMDA 137B SVAMP chain of thought as 37.5, while Table 6 gives 36.7 ± 0.4. The other three datasets agree across tables.
  - A.2 gives standard coin flip as 50.0%. Table 7 gives 49.0 ± 2.1.
  - The text says PaLM is "within 2%" of the prior best on AQuA; Table 1 gives 37.9 − 35.8 = 2.1 points (our subtraction). ASDiv gap is 1.4.
  - The Table 6 caption says equation-only lies "in between" standard and chain of thought. On GSM8K it is 5.4, below standard (6.5).
  - A.2 says "large margin" on eight datasets for all three annotators. Table 7 Date values for B and C (27.4, 25.5) are close to the standard 21.5.
- **Typos or artefacts:** "can interpreted" (p. 3); stray quote mark in footnote 1; Figure 9 caption "categorized that"; Figure 10 third example contains "540b model" inside the equation (artefact in image); Section 5 says "these three tasks" though two tasks are described; checklist "we GPT-3 results".
- **Not stated in these pages:** the PaLM numbers behind Figure 5 and the numbers behind Figure 11 are not given in tables on these pages. Figure 11 itself is not in these pages. I give no values for it.
