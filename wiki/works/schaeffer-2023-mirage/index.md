---
id: schaeffer-2023-mirage/index
work: schaeffer-2023-mirage
type: work-map
units: [schaeffer-2023-mirage/main]
generated: deterministic
---

# Schaeffer, R., Miranda, B., & Koyejo, S. (2023). *Are Emergent Abilities of Large Language Models a Mirage?* Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2304.15004.

## One digest
This work has a single digest, which is also its work-level summary: [[schaeffer-2023-mirage/main]].

## In one line
Some claimed "emergent abilities" of LLMs may come from the researcher's choice of a nonlinear or discontinuous metric (and from too little test data), not from sudden changes in the models themselves.

## The gist
Earlier work claimed that some abilities appear sharply and unpredictably as language models get larger. The authors ask whether this is caused by how performance is scored. Their simple model assumes per-token loss falls smoothly with scale. Metrics such as exact-match accuracy or multiple-choice grade then produce sharp curves. Linear or continuous metrics on the same outputs give smooth curves. They test this on GPT-3/InstructGPT outputs, on a meta-analysis of BIG-Bench, and by inducing "emergence" in vision networks. They do not claim that LLMs cannot have emergent abilities. The work matters because emergence claims feed AI-safety worries about sudden new capabilities.

**Prerequisites:** powers and exponentials; probability of independent events (multiply); cross-entropy as −log p of the correct token; linear-log plots; the idea of a scaling law.
