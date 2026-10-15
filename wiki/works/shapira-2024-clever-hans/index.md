---
id: shapira-2024-clever-hans/index
work: shapira-2024-clever-hans
type: work-map
units: [shapira-2024-clever-hans/main]
generated: deterministic
---

# Shapira, N., Levy, M., Alavi, S. H., Zhou, X., Choi, Y., Goldberg, Y., Sap, M., & Shwartz, V. (2024). Clever Hans or neural theory of mind? Stress testing social reasoning in large language models. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 2257–2273). St. Julian's, Malta: ACL. doi:10.18653/v1/2024.eacl-long.138

## One digest
This work has a single digest, which is also its work-level summary: [[shapira-2024-clever-hans/main]].

## In one line
Across six ToM datasets, 15 LLMs show some ToM-like success but no robust ability: performance varies by dataset, probing method and small adversarial changes, which suggests shallow heuristics rather than general reasoning.

## The gist
Do large language models (LLMs) have a robust neural theory of mind (N-ToM)? Earlier papers disagreed, and some rested on a few anecdotes. The authors test 15 LLMs on six ToM datasets and compare probing methods. They also build two expert-made sets, ToMi′ and Adv-CSFB, that focus on adversarial examples. Some datasets are nearly solved, but no model does well on all. Results change with the probing method, and small variations of the original tasks (a transparent container, "in" changed to "on") sharply lower the performance of the best models. The authors conclude the abilities are limited and not robust, and they warn against anecdotes, small benchmarks and human-designed psychological tests applied to models.

**Prerequisites:** false-belief tasks (Sally–Anne); accuracy and majority-class baselines; prompting LLMs (zero-shot, multiple-choice, chain-of-thought); the idea of spurious correlation.
