---
id: ziems-2024-css/index
work: ziems-2024-css
type: work-map
units: [ziems-2024-css/main-p1, ziems-2024-css/main-p2]
---

# Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). *Can Large Language Models Transform Computational Social Science?* Computational Linguistics, 50(1), 237–291. DOI:10.1162/coli_a_00502.

## In one paragraph
The paper asks whether prompted large language models (LLMs) can work as tools for computational social science (CSS). The authors build a benchmark of 20 classification tasks and 5 generation tasks in English. They test zero-shot FLAN-T5 and OpenAI models against fine-tuned baselines. LLMs rarely beat fine-tuned classifiers, but on about half the tasks they agree moderately well with gold labels. On generation, the best models reach roughly human-level explanation quality, and automatic metrics fail to capture this. The authors conclude that LLMs should augment human annotation, not replace it, and that human validation is needed throughout. This matters because it is a reference point for using LLM labels as surrogates for human labels.

## The path through the work
- [[ziems-2024-css/main-p1]] — Zero-shot prompted large language models (LLMs) usually do not beat fine-tuned classifiers on social-science text labelling, but on about half the tasks they agree with gold labels moderately well, so they may help human annotation teams.
- [[ziems-2024-css/main-p2]] — Prompted LLMs match human-level explanation quality on several CSS generation tasks and are decent annotators, but the authors conclude they should augment, not replace, human labelling, with human validation throughout.

## Big ideas across units
- **Augment, don't replace.** Moderate classification agreement and near-human generation lead to the recommendation of LLMs inside a human annotation loop. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **Zero-shot LLMs versus fine-tuned baselines.** LLMs seldom beat fine-tuned classifiers (RoBERTa), yet they are usable on many tasks. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **What drives performance.** In the OpenAI family, instruction tuning, code pretraining and RLHF matter more than size. FLAN gains about 5 F1 points per ten-fold size increase. RLHF also seems to help generation. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **Task complexity matters more than academic field.** Performance overlaps across fields and may track input and label complexity. Conversations, long documents and big label sets are hard. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **Evaluation is a problem in itself.** Annotator agreement and F1 serve for classification. For generation, reference-based automatic metrics become invalid near gold quality, so expert and pairwise human evaluation are used, at a cost. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **Careful prompt design.** Written guidelines, constrained output and averaging over paraphrases make results more reliable. Unit: [[ziems-2024-css/main-p1]].
- **Labels are not the end goal.** Averaging even accurate LLM labels gives biased estimates; a design-based semi-supervised method fixes this with a few gold labels. Units: [[ziems-2024-css/main-p1]], [[ziems-2024-css/main-p2]].
- **Open risks.** Bias, proprietary opacity, data leakage, temporal shifts and missing causal grounding remain, and simulated populations are limited. Unit: [[ziems-2024-css/main-p2]].

## How to read it
- Both units are essential, and the catalog focus is the task taxonomy and the recommendations.
- [[ziems-2024-css/main-p1]] holds the task taxonomy, prompt design and classification results. Read it first.
- [[ziems-2024-css/main-p2]] continues the evaluation with generation, then gives the recommendations in the Discussion. It depends on the setup and models from part 1.
- The references at the end of part 2 can be skipped on a first pass. So can the detailed error analysis and few-shot results in part 1 (pp. 259–261).
- If short of time, read the L0 and L1 of part 1, then the Discussion in part 2.

## Concepts introduced
- [[zero-shot-few-shot-prompting]] — [[ziems-2024-css/main-p1]]
- [[pretraining-fine-tuning]] — [[ziems-2024-css/main-p1]]
- [[rlhf]] — [[ziems-2024-css/main-p1]]
- [[scaling-law]] — [[ziems-2024-css/main-p1]]
- [[supervised-fine-tuning]] — [[ziems-2024-css/main-p1]]
- [[macro-f1]] — [[ziems-2024-css/main-p1]]
- [[inter-annotator-agreement-kappa]] — [[ziems-2024-css/main-p1]]
- [[prompt-perturbation-averaging]] — [[ziems-2024-css/main-p1]]
- [[constrained-decoding-logit-bias]] — [[ziems-2024-css/main-p1]]
- [[css-prompt-guidelines]] — [[ziems-2024-css/main-p1]]
- [[llm-augmented-annotation]] — [[ziems-2024-css/main-p1]]
- [[design-based-semi-supervised-learning]] — [[ziems-2024-css/main-p1]]
- [[silicon-sample]] — [[ziems-2024-css/main-p2]]
- [[llm-pseudo-labels]] — [[ziems-2024-css/main-p2]]
- [[human-ai-annotation-loop]] — [[ziems-2024-css/main-p2]]
- [[reference-free-evaluation]] — [[ziems-2024-css/main-p2]]
- [[human-ranking-evaluation]] — [[ziems-2024-css/main-p2]]
- [[algorithmic-monoculture]] — [[ziems-2024-css/main-p2]]
- [[temporal-grounding]] — [[ziems-2024-css/main-p2]]
- [[data-leakage]] — [[ziems-2024-css/main-p2]]
