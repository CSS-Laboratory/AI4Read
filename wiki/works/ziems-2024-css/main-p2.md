---
id: ziems-2024-css/main-p2
work: ziems-2024-css
unit: "paper (part 2/2): end of the generation results, Section 7 Discussion, references"
pages: 265–291
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Ziems et al. (2024), part 2: generation results, recommendations, limits

## L0 — One line
Prompted LLMs match human-level explanation quality on several CSS generation tasks and are decent annotators, but the authors conclude they should augment, not replace, human labelling, with human validation throughout.

## L1 — The gist (≤ 120 words)
This part finishes the evaluation of zero-shot text generation for computational social science (CSS). Expert ratings and the authors' pairwise rankings show the best models (davinci-003, GPT-3.5) reach roughly human-gold quality, while automatic reference-based metrics fail. The Discussion then asks how to use LLMs. Its answers: put LLMs in the loop of human annotation; prefer open-source models for classification and gpt-3.5-turbo for generation; expect trouble with conversations, long documents, large label sets and time shifts; and treat bias, proprietary opacity, data leakage and the lack of causal grounding as open risks. Simulation and new evaluation methods are flagged as future directions.

**Prerequisites:** zero-shot prompting; instruction-tuned and RLHF models; Likert ratings; pseudo-labels versus gold labels; basic idea of bias in an estimator (for the toy example).

## L2 — Key ideas
- Expert Likert ratings: the best models match or beat the fine-tuned baseline and gold references on faithfulness, relevance, coherence and fluency in several tasks. Scale matters; small models are unfaithful (Table 6, p. 265).
- In pairwise ranking, the best model on each task beats the gold explanation 38.9%–68.2% of the time. The authors read this as near parity, and as a sign that human feedback (RLHF) seems to help generation systematically (Table 7, p. 266).
- Automatic metrics (BLEU, BERTScore, BLEURT) gave uninterpretable scores. Reference-based scoring becomes an "invalid construct" once models approach the gold references. Reference-free expert evaluation is costly and hard to reproduce (pp. 266–267).
- Labels are rarely the end goal. Plain averaging of even accurate LLM labels gives biased estimates; the DSL method of Egami et al. gives confidence intervals with >86% correct coverage with only 25 gold labels (p. 267).
- The authors advocate LLMs integrated with human annotation, not wholesale replacement. LLMs act as one labeller among several and as a "flywheel" for data collection (p. 268).
- Model choice: open-source FLAN for classification if GPUs exist; gpt-3.5-turbo for generation. LLMs struggle most with conversations, full documents and cross-document reasoning (p. 269).
- LLMs may blur supervised and unsupervised CSS paradigms and enable simulated populations, but simulations have limited predictive power and show higher opinion homogeneity than humans (p. 270).
- Open challenges: expert vocabulary, big label spaces, structured outputs, temporal grounding (p. 271); bias and proprietary-model risks (p. 272); data leakage and the lack of causal explanation (pp. 272–273).

## L3 — Walkthrough

*Where this part starts:* mid-paragraph in the results on generation tasks. The previous page is not in this unit. The section number for these results is not visible here (it is probably Section 6, since Section 7 follows).

### Generation results (continued)

**Expert scoring (Table 6, p. 265).**
- Setup per the caption: expert annotators score generations on 1–5 Likert scales (a 1-to-5 rating scale) for faithfulness, relevance, coherence and fluency. Five tasks are covered: CovidET, MRF, FLUTE, SBIC and Reframing. "Baseline" is a fine-tuned model; "Human" is the gold reference. A + or − marks a score significantly better or worse than human at P < .05 by paired bootstrap (resampling test) (p. 265).
- The caption says the leading models (davinci-003, GPT 3.5) can match or exceed the fine-tuned baseline and gold references (p. 265). The text says the best models reach "gold-standard levels" and again outperform the fine-tuned baseline (p. 265).
- Examples from the table:
  - CovidET: GPT 3.5 gets 3.9+/3.5+/3.8+/4.5+, against Human 2.8/2.6/2.8/3.8.
  - SBIC: GPT 3.5 and GPT 4 are marked + on all four scores, e.g. GPT 4 gets 4.1+/3.8+/4.2+/4.6+ against Human 2.9/3.0/3.1/2.6.
  - MRF: davinci-002 gets 3.9+/4.1+/4.3+/4.9+.
  - Reframing: davinci-003 gets 4.4/4.5+/4.2/4.6+ against Human 4.2/4.2/4.1/4.2.
- Not every cell favours the models. On FLUTE, GPT 3.5 and GPT 4 have faithfulness 2.1 (marked −) against Human 2.8 (p. 265).
- Scale matters. Smaller models fail to give faithful explanations and summaries, the text singles out CovidET, FLUTE and SBIC, where text-ada-001 averages below 2 out of 5 on faithfulness (p. 265). See Reading notes on the SBIC figure.
- The Table 6 panel "Annotator Backgrounds" lists, per task, the annotators' education and profession (p. 265).
- Author's conclusion: with scale, LLMs can generate useful, relevant, coherent and fluent explanations and summaries of underlying social science constructs (p. 265).

*Intuition note.* Judged by experts on four quality scales, big prompted models write explanations about as good as the human-written reference, sometimes better. Small models do not: they often fail to stay faithful to the task specification.

**Human ranking evaluation (Table 7, p. 266).**
- Table 7 gives the share of pairwise rankings where the authors unanimously preferred the model's generation to the dataset's gold explanation (p. 266).
- Best entries per task:
  - MRF: davinci-003, 38.9%.
  - FLUTE: GPT 4, 51.5%.
  - SBIC: GPT 3.5, 65.9%.
  - Reframing: GPT 3.5, 56.1%.
  - CovidET: GPT 3.5, 68.2%.
  - Fine-tuned Baseline: 31.2%, 4.6%, 16.5%, 45.0%, 37.5% (same task order).
  - text-ada-001 on Reframing: 0.0% (p. 266).
- The text says generations outrank gold at least 38% of the time. This is true of the best model on each task (lowest is 38.9%), not of every model (p. 266).
- The best models "approach parity with humans", a near 50–50 coin toss (p. 266).
- Both RLHF models (gpt-3.5-turbo, text-davinci-003) show significant benefits. Unlike classification (Section 5.2), the generation tasks "seem to systematically benefit from human feedback" (p. 266).
- No model substantially outperforms human annotation. The authors take this to suggest that current LLMs cannot fully replace human analysis (p. 266).
- Human-AI collaboration suggestion. Instead of writing summary explanations from scratch, researchers could lightly edit model outputs. The authors say Table 7 suggests that, for every five generations, 2 to 3 would need no extra annotator effort (p. 266). The authors leave the real plausibility and the reduction of annotators' cognitive load to future HCI work (p. 266).
- Footnote 9: machine explanations may be limited in diversity, and human validation may not be able to add novel edits or perspectives (p. 266).

*Intuition note.* In head-to-head comparisons the best models' text wins roughly as often as it loses. A researcher could therefore start from machine drafts and fix them, rather than writing everything.

**The evaluation burden (pp. 266–267).**
- Trade-off: with LLM efficiency comes the burden of manually validating generative outputs (p. 266).
- Automatic metrics are known to fail to capture human preferences (Goyal et al. 2022; Liang et al. 2022). BLEU, BERTScore and BLEURT, which compare with human-written ground truth, "all produced uninterpretable scores" here (p. 266).
- As zero-shot models approach or beat the gold references, reference-based scoring becomes an invalid construct for measuring true utility, even if semantic-similarity metrics were ideal (pp. 266–267).
- This motivates the authors' reference-free expert evaluation, which asks which generation is more accurate for the input. It is limited by cost and reproducibility, and new metrics and procedures for CSS are needed (p. 267).

### 7. Discussion (p. 267)

- Main summary: LLMs "can augment but not entirely replace the traditional CSS research pipeline" (p. 267).
- Four recommendations (p. 267):
  1. Integrate LLMs-in-the-loop to transform large-scale data labelling.
  2. Prioritize open-source LLMs for classification.
  3. For generation, prioritize faithfulness, relevance, coherence and fluency by choosing larger instruction-tuned models that have learned human preferences.
  4. Investigate in the long term how LLMs produce new CSS paradigms.

#### 7.1 How annotation fits into CSS (p. 267)
- Social scientists seldom want labels for their own sake. Labels feed downstream inferential statistics such as regression (p. 267).
- Valid downstream inference needs estimators that are asymptotically unbiased (bias vanishing as data grows) and allow valid confidence intervals (p. 267).
- Egami et al. (2023, a follow-up study) show that even the most accurate LLM annotations give biased estimates and invalid confidence intervals when they are merely averaged (p. 267).
- They propose DSL, which computes unbiased estimators for prevalence estimation on each of the 17 classification tasks. With FLAN-UL2 pseudo-labels (model-made labels) and a handful of gold labels, unbiased regressions are possible even where UL2 has low accuracy (p. 267).
- With only 25 gold annotations, DSL gives confidence intervals with >86% correct coverage on all 17 tasks, including the worst-performing ones (p. 267).

*Intuition note.* Counting LLM labels and treating the result as truth distorts conclusions, because the resulting estimates are biased. A small human-labelled sample can be used to correct that.

#### 7.2 How LLMs can augment annotation (pp. 268–269)
- Section 5.1 shows fair to strong agreement with humans on 12 of 17 classification tasks. LLMs reduce the need for human labour on some tasks (p. 268).
- LLMs are not a wholesale replacement. Even the best show unusably low performance on some tasks (p. 268).
- Ensembling does not fix this label corruption. LLMs show high internal agreement even when inaccurate (Gilardi et al. 2023) (p. 268).
- Unchecked overconfident models distort CSS conclusions and mislead policy. The authors say human validation is key to avoiding a replication crisis in CSS caused by LLM hallucinations and inaccuracies (p. 268).
- **Advocated design (Figure 5, p. 268).** Use an LLM that matches human agreement levels as one of several labellers.
  - Figure example: the claim "Persimmon kills coronavirus…". Traditional: two humans disagree (✓ vs ✗) and the label stays unresolved ("?").
  - LLM-augmented: the LLM says ✗, one human ✓, one human ✗, and the final label is ✗.
  - Caption: the LLM scales up annotation and reduces variance in gold labels; humans validate (p. 268).
- Such methods can produce unbiased estimators. Chaganty et al. (2018) give provably optimal estimators with 7–13% monetary savings from LLM pseudo-labels (p. 268).
- **Flywheel.** Prompted LLMs perform significantly better than chance and give imperfect labels cheaply. Schemes that improve imperfect data by iteration (weak supervision, targeted data cleaning, active learning) let human validation refine the model. This creates a "virtuous cycle" that focuses human expertise where it is most needed (p. 268).
- Generation: the authors say LLMs are "even stronger" there, rated superior to gold over 38% of the time in all 5 tasks (p. 268). This repeats the best-model figure from Table 7 (see above).
- Human curation of LLM generations has already been used to build datasets, including the FLUTE benchmark used here (pp. 268–269).
- Recommendation: use LLMs as the foundation of annotation procedures, and measure in future whether efficiency improves "as we suspect" (p. 269).
- If efficiency is achieved, savings should be reinvested in training expert annotators, reversing the trend of replacing experts with crowdworkers because of cost (p. 269).

#### 7.3 When to use what LLM (pp. 269–270)
- **Classification.** Open-source models like FLAN are as capable as state-of-the-art closed OpenAI models. Researchers with suitable GPUs should prefer them (p. 269).
  - Benefits: low marginal cost for continuous monitoring or enormous-scale analysis; the option to fine-tune on labelled data and to constrain outputs programmatically. Not all OpenAI instruction-tuned models can currently be fine-tuned (p. 269).
- **Without hardware.** Proprietary APIs appear cost-efficient. Per the authors' cloud-pricing sources, hardware for FLAN-T5-XXL costs $170 per day, equal to processing about 50 million words with gpt-3.5-turbo. In most cases gpt-3.5-turbo is more cost-efficient with lower overhead for hardware-constrained groups (p. 269).
- **Generation.** The results are "clear-cut" (p. 269):
  - Even the largest open-source models failed to generate meaningful responses.
  - The best proprietary models consistently beat fine-tuned baselines and approach gold parity "when evaluated by crowdworkers" (p. 269; see Reading notes).
  - gpt-3.5-turbo is the clear leader by price and performance.
  - Explanations are not causal, and errors and hallucinations are risks (p. 269).
- **Weak spots.** All LLMs struggle most with conversational and full-document data. They lack clear cross-document reasoning, which limits common applications like topic modeling (p. 269).
  - Subfields studying these discourse types (sociology, literature, psychology) face major limitations. the authors judge that LLMs are unlikely to have major immediate impact there (p. 269).
  - NLP researchers should study conversations, long documents and cross-document reasoning (pp. 269–270).

#### 7.4 Blending CSS paradigms (p. 270)
- Few- and zero-shot abilities blur the line between supervised and unsupervised methods (p. 270).
  - Supervised: labelled data guided by theory trains a model that classifies text at scale to gather evidence on causal effects.
  - Unsupervised (e.g. topic modeling): condenses information to help discover relationships that develop or refine theory (p. 270).
- **Author's belief:** one tool could both develop working hypotheses (from generated and summarized data) and test them (by flexible low-cost labelling). Researchers should use LLM multi-functionality to build new research paradigms (p. 270).
- **Simulation.** Rule-based utility functions are limited by their expressiveness. LLMs hold great potential for more powerful simulations, since they replicate human biases without explicit conditioning. Cited work simulates social computing systems, communities and their members' interactions, public opinion, and subjective experience descriptions (p. 270).
- Dangers (p. 270):
  - Social systems evolve unpredictably, so simulated samples inherently have limited predictive and explanatory power.
  - Utility-based simulations have similar limits, but their assumptions are explicit, unlike the opaque human-behaviour model inside an LLM.
  - Current models show higher homogeneity of opinion than humans.
  - Combining LLMs with true human samples is essential, the authors say, to avoid an algorithmic monoculture, which could lead to fragile findings covering only the limited perspectives represented.

#### 7.5 The need for a new evaluation paradigm (pp. 270–271)
- Accuracy metrics suit fixed-taxonomy classification. Word-overlap metrics suit generation with a well-defined gold reference, such as translation (p. 270).
- Open-ended coding and CSS explanation follow neither a predefined taxonomy nor a regular output template (p. 271).
- For topic modeling, held-out likelihood measured predictive power. But predictiveness does not always correlate with explainability, and such metrics proved at odds with human quality judgments (p. 271).
- Human evaluations can be unreliable. The authors observe that crowd work seems to give unreliable quality metrics for FLUTE, a nuanced generative task. New metrics are needed for the semantic validity of free-form coding with LLMs as explanation generators (p. 271).

#### 7.6 CSS challenges for LLMs (p. 271)
1. **Expert taxonomies.** They use technical or nonstandard terms (e.g. copula omission; the persuasive "scarcity" strategy; "white grievance" in implicit hate). LLMs may lack representations for them, as they may be absent from pretraining data. Teaching LLMs such constructs deserves attention, especially for novel constructs defined jointly with LLMs (p. 271).
2. **Large label spaces.** Some CSS tasks have upwards of 72 classes (character tropes, Section 3.3.4). This challenges transformer LLMs with relatively limited memory, finite processing windows and quadratic space complexity (p. 271).
3. **Label dependencies and structured outputs.** Hierarchies and constrained schemas (as in event argument extraction) are hard for zero-shot prompting, because prompted models often give inconsistent outputs. The Table 1 prompting practices help, but the challenge is not fully solved (p. 271).
4. **Temporal grounding.** Language, norms, beliefs and political structures change over time. LLMs need an extremely high level of temporal grounding: signals to orient an analysis in a particular place and time. This is hard for breaking events, and frequent updating by continual training may be prohibitively expensive, more so as models scale (p. 271).

#### 7.7 Bias and fairness (p. 272)
- **Bias.** LLMs are known to amplify social biases and stereotypes and viewpoint biases in subjective domains. These can appear in open-ended generation (explanation, paraphrasing). Classification and parsing performance may vary systematically with demographic variation in the target population (p. 272).
- The authors could not run a systematic bias analysis with the available datasets, and urge researchers to consider these risks (p. 272).
- **Proprietary LLMs.** Details of corpus selection, filtering and formatting are often unavailable. Consequences (p. 272):
  - One risk the authors name is that bias and social harm cannot be decomposed into their sources, so targeted mitigation is hard.
  - Unattributed biases may escape human review, since humans tend to falsely attribute factuality to authoritative-sounding text, a style proprietary LLMs have largely mastered.
  - Black-box APIs may not allow fine-tuning for mitigation.
  - Closed-API users may face more privacy and intellectual-property risks, since proprietary models are known to replicate copyrighted material and sensitive personal information.

#### 7.8 Limitations (pp. 272–273)
- **Task selection.** The tasks are not exhaustive. Sensitive domains (mental health; cultural studies needing community knowledge) are largely out of scope. LLMs should not be used for legal or medical advice, diagnosis, or interfering with democratic processes. Available data are dominated by standard dialects and WEIRD populations (Western, Educated, Industrial, Rich, Democratic). Cross-cultural CSS needs separate study (p. 272).
- **Data leakage.** Test data may have been seen in pretraining, which would inflate scores, especially for closed models. Suggested mitigations, left to future work: prompts forcing the model to "forget" the test set, and custom test sets built from perturbations of existing data (p. 272).
- **Causality and explanations.** This work explored predictive power, not causal explanation. Predictions expose latent phenomena that become structured features for later causal analysis (p. 273).
  - This "may not be sufficient": social scientists often seek causal or at least contrastive ("why P instead of Q") explanations. LLMs are not grounded in a causal model of the world, so on their own they are not reliable tools for mining causal relationships in text. Left to future work (p. 273).

### Back matter (pp. 273–291)
Acknowledgments (p. 273, after the end of §7.8) and the reference list (pp. 273–291). Not digested.

## Toy example (ours, not from the text)
Aim: show why raw LLM labels need human correction, and how a small gold sample can fix it. This is a simple difference correction, not Egami et al.'s DSL.

- A corpus has 1,000 posts. An LLM labels 400 of them "misinformation". Naive prevalence estimate: 400 / 1000 = 0.40.
- We draw 25 posts at random and have humans label them (gold). On those 25, the LLM says "misinformation" for 10 (10 / 25 = 0.40). Humans say "misinformation" for 7 (7 / 25 = 0.28).
- Estimated LLM bias = gold rate − LLM rate on the sample = 0.28 − 0.40 = −0.12.
- Corrected estimate = naive estimate + estimated bias = 0.40 + (−0.12) = 0.28.
- With only 25 gold labels this correction is noisy, so a confidence interval must account for the sample size. That is what methods like DSL do properly (p. 267).

Second small check, from Table 7 (p. 266): if a model's output is preferred over gold in about 50% of pairs, then of 5 generations about 5 × 0.5 = 2.5 need no edit. This matches the text's "2 to 3".

## Concepts
- [[zero-shot-few-shot-prompting]] — specifying a task with an instruction (zero-shot) or a few examples (few-shot); the paper says this blurs supervised and unsupervised paradigms (p. 270).
- [[rlhf]] — human-feedback-tuned models (gpt-3.5-turbo, text-davinci-003); here they benefit generation tasks significantly (p. 266).
- [[silicon-sample]] — LLMs used as simulated sample populations in CSS; the authors stress limited predictive power and higher opinion homogeneity than humans (p. 270).
- [[llm-pseudo-labels]] (new) — cheap, imperfect labels produced by a prompted LLM, used with a few gold labels (pp. 267–268).
- [[human-ai-annotation-loop]] (new) — the LLM is one labeller among several, with humans validating; a "flywheel" for data collection (p. 268).
- [[design-based-semi-supervised-learning]] (new) — DSL (Egami et al.): unbiased estimators and confidence intervals with >86% coverage in the reported tests, from LLM pseudo-labels plus a few gold labels (p. 267).
- [[reference-free-evaluation]] (new) — judging generations against the input rather than a gold reference; needed as models approach gold quality (pp. 266–267).
- [[human-ranking-evaluation]] (new) — pairwise preference of a model output over the gold explanation (Table 7) (p. 266).
- [[algorithmic-monoculture]] (new) — the risk, when LLM opinions are homogeneous and replace human samples, of fragile findings covering limited perspectives (p. 270).
- [[temporal-grounding]] (new) — knowledge and signals to place a text analysis in a particular time and place (p. 271).
- [[data-leakage]] (new) — test data seen during pretraining, inflating scores (p. 272).

## Canonical instances
- [[covidet-task]] — aspect-based summarization of COVID tweets; GPT 3.5 beats human gold on all four expert scores and in 68.2% of rankings (pp. 265–266).
- [[flute-task]] — figurative-language explanation; LLM faithfulness is below human for GPT 3.5/4, and crowd work seems to have given unreliable quality metrics (pp. 265, 271).
- [[sbic-task]] — social bias inference; GPT 3.5 and GPT 4 significantly beat human gold on all four scores (p. 265).
- [[mrf-task]] — implied misinformation explanation; davinci-002 is best on expert scores (p. 265).
- [[positive-reframing-task]] — Reframing in Tables 6–7; davinci-003 scores 4.4/4.5+/4.2/4.6+ (p. 265).
- [[misinformation-annotation-example]] — the persimmon claim in Figure 5, showing an LLM breaking a tie between two disagreeing humans (p. 268).
- [[dsl-egami-2023]] — DSL with FLAN-UL2 pseudo-labels and 25 gold labels gives >86% CI coverage (p. 267).

## Bridges (candidates)
- [structural-analogy] LLM pseudo-labels plus a small gold sample ↔ semi-supervised / prediction-powered inference: a cheap noisy predictor is bias-corrected using a few true labels (the DSL idea, p. 267).
- [structural-analogy] "Flywheel" of LLM labels refined by human validation ↔ active learning and weak supervision, which the authors cite (p. 268).
- [metaphor] LLM simulation of populations (p. 270) ↔ agent-based models with rule-based utilities: both generate hypotheses, but the LLM's assumptions are opaque.
- [structural-analogy] Algorithmic monoculture and homogeneous opinions (p. 270) ↔ reduced variance in samples: using one model as a respondent loses between-person diversity.

## Questions this raises
- How large must the gold sample be for DSL-style correction to give valid intervals on a new, harder task, and how does that cost compare with the 7–13% savings of Chaganty et al.?
- What would a valid reference-free metric for CSS explanations look like, and can it be reproducible without costly expert panels?
- Since 12 of 17 classification tasks show fair to strong agreement, what separates the 5 failing tasks (taxonomy vocabulary, label-space size, discourse type)?
- Can LLM-assisted editing keep the diversity and novelty of human explanations, given footnote 9's warning?

## Reading notes
- **Scope.** This unit is part 2 of the paper: it starts mid-paragraph on printed p. 265 (end of the generation results) and ends at the reference list (p. 291). Apart from the end of §7.8 on p. 273, pages 273–291 are acknowledgments and references and were not digested in detail. Printed page numbers are used throughout and match the pdf pages (pdf 29 = printed 265).
- **Section numbering.** The heading of the generation-results section is not visible in this part; "Section 6" is inferred from the following "7. Discussion".
- **Table text layer.** The extracted text for Table 6 was missing; Table 7 text was extractable. All table values above were checked against the page images. Table 6 cell values are cited only where clearly legible.
- **Possible inconsistency (p. 265 vs Table 6).** The text says text-ada-001 faithfulness is below 2 on CovidET, FLUTE and SBIC. As I read the image, ada-001 faithfulness is 1.8 (CovidET) and 1.4 (FLUTE) but 2.4 (SBIC). The SBIC claim does not match what I read; the fine-tuned Baseline scores 1.9 there.
- **Evaluator wording.** Table 7 is described as authors' rankings (p. 266), while Section 7.3 says parity with gold is reached when the evaluators are crowdworkers (p. 269) and Section 7.5 says crowd work seems unreliable for FLUTE (p. 271). Table 6 is labelled "expert scoring" with an annotator-background panel. How these descriptions fit together is not explained in these pages.
- **The "at least 38%" and "all 5 tasks" claims** (pp. 266, 268) hold for the best model per task in Table 7, not for every model.
- Table 7 rows show only minor alignment variation (e.g. 39.0% for davinci-001 on SBIC); no numerical issues found.
