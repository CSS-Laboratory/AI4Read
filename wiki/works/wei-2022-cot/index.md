---
id: wei-2022-cot/index
work: wei-2022-cot
type: work-map
units: [wei-2022-cot/main-p1, wei-2022-cot/main-p2]
---

# Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). arXiv:2201.11903.

## In one paragraph
The paper shows that a large language model reasons much better when its few-shot examples include the intermediate steps, written in natural language, between the question and the answer. This is called chain-of-thought prompting. It needs no finetuning. The gain appears only in models of about 100B parameters or more, and it is largest on hard multi-step problems. PaLM 540B reached 56.9% on GSM8K, against 17.9% with standard prompting. The method also helps on commonsense and symbolic tasks. The appendices check by hand that correct answers usually rest on sound reasoning, and they classify how wrong chains fail. The authors say the generated reasoning has no guarantee of being coherent or factual.

## The path through the work
- [[wei-2022-cot/main-p1]] — If few-shot prompt examples include the intermediate reasoning steps in natural language, sufficiently large language models solve multi-step reasoning tasks much better, with no finetuning.
- [[wei-2022-cot/main-p2]] — The appendices place chain-of-thought prompting among related work, check by hand that its reasoning chains are mostly sound when answers are right, show how they fail when answers are wrong, and print every prompt used.

## Big ideas across units
- **Showing the steps in the prompt improves reasoning.** Exemplars become ⟨input, chain of thought, output⟩ triples, and the model imitates them. Units: main-p1, main-p2.
- **The gain depends on model scale.** It appears only at about 100B parameters and above. Smaller models write fluent but illogical chains. Units: main-p1.
- **Harder problems gain more.** GSM8K gains are largest, and one-step problems gain little or nothing. Units: main-p1.
- **Natural-language steps appear to matter.** Equation-only, dots-only and answer-first variants do not match the gain on GSM8K. Units: main-p1.
- **The result is fairly robust, but not fully.** It holds across annotators, exemplar orders and exemplar counts, yet variance and prompt engineering still matter. Units: main-p1, main-p2.
- **Chains are not guaranteed to be faithful.** Manual inspection finds nearly all correct GSM8K chains sound, and errors in wrong chains vary. The authors say there is no guarantee of coherence or factuality, and the question of whether the model really "reasons" stays open. Units: main-p1, main-p2.
- **Prompting alone replaces finetuning for intermediate steps.** Prior work mostly needed annotated or synthetic training data, while chain of thought is elicited from off-the-shelf models. Units: main-p1, main-p2.
- **Possible fixes for errors.** A Python calculator gives a small gain, and verifier-based scoring of sampled paths is named as a remedy. Units: main-p1, main-p2.

## How to read it
- **Essential:** [[wei-2022-cot/main-p1]]. It holds the method, the scale result, the GSM8K state of the art, the ablations and the stated limits.
- **Read second:** [[wei-2022-cot/main-p2]], if you care about how far the chains can be trusted. Its error analysis (49 of 50 correct chains sound; breakdown of 50 wrong ones) is the most useful part.
- **Can skip on a first pass:** the related-work comparison, the dataset and compute details, and the printed prompts (Tables 20–28). They matter mainly for reproduction.
- **Dependencies:** main-p2 assumes the chain-of-thought method and few-shot prompting from main-p1.

## Concepts introduced
- [[chain-of-thought]] — main-p1
- [[zero-shot-few-shot-prompting]] — main-p1
- [[in-context-learning]] — main-p1
- [[emergent-ability]] — main-p1
- [[pretraining-fine-tuning]] — main-p1
- [[scaling-law]] — main-p1
- [[standard-prompting]] — main-p1
- [[exemplar]] — main-p1
- [[greedy-decoding]] — main-p1
- [[ood-length-generalization]] — main-p1
- [[external-calculator]] — main-p1
- [[prompt-sensitivity]] — main-p1
- [[supervised-fine-tuning]] — main-p2
- [[cot-error-taxonomy]] — main-p2
- [[correct-by-chance]] — main-p2
- [[verifier-reranking]] — main-p2
