---
id: wei-2022-emergent/index
work: wei-2022-emergent
type: work-map
units: [wei-2022-emergent/main]
generated: deterministic
---

# Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W. (2022). *Emergent Abilities of Large Language Models*. Transactions on Machine Learning Research. arXiv:2206.07682.

## One digest
This work has a single digest, which is also its work-level summary: [[wei-2022-emergent/main]].

## In one line
The paper surveys abilities that are near-random in smaller language models and well above random in larger ones, so they could not have been predicted by extrapolating smaller models, and it asks whether more scaling will bring more.

## The gist
Scaling language models often improves loss and many tasks in a smooth, predictable way. The authors ask which abilities do not follow this pattern. They call an ability emergent if it is absent in smaller models and present in larger ones. They collect examples from prior work: few-shot tasks, and prompting or finetuning methods that only help at large scale. They discuss possible explanations (task depth, memorization, evaluation metrics), ways to get abilities at smaller scale, emergent risks, and future work. Their analyses give no complete explanation and no way to predict the scale at which emergence occurs. This matters because capabilities of larger future models may be hard to forecast.

**Prerequisites:** what a language model, a benchmark and a scaling curve are; a scaling law (a predictable trend of performance with scale); training compute in FLOPs; cross-entropy loss; exact match (the answer must equal the target exactly); few-shot prompting (Section 3 explains it); BIG-Bench and MMLU (benchmark suites of many tasks or exam topics); GPT-3, LaMDA, Gopher, Chinchilla and PaLM (names of language-model families).
