---
id: hoffmann-2022-chinchilla/index
work: hoffmann-2022-chinchilla
type: work-map
units: [hoffmann-2022-chinchilla/main]
generated: deterministic
---

# Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). *Training Compute-Optimal Large Language Models*. arXiv:2203.15556. Published at NeurIPS 2022 under the title "An Empirical Analysis of Compute-Optimal Large Language Model Training".

## One digest
This work has a single digest, which is also its work-level summary: [[hoffmann-2022-chinchilla/main]].

## In one line
For a fixed compute budget, the authors estimate that model size and number of training tokens should grow in roughly equal proportion, which implies that the large models of the time were over-sized and under-trained, and they test this with Chinchilla (70B parameters, 1.4T tokens).

## The gist
Given a fixed training-compute budget, how large should a language model be, and on how many tokens should it train? The authors estimate the best split with three methods, all based on training many models (over 400 runs in total). All three suggest that model size and training tokens should grow in roughly equal proportion with compute, unlike the earlier Kaplan et al. recommendation. They test this by training Chinchilla (70B parameters, 1.4T tokens) with Gopher's compute budget. Chinchilla outperforms the 280B Gopher and other larger models on most evaluations. The authors conclude that the large models of the time were over-sized and under-trained, and that larger, high-quality datasets will play a key role in further scaling.

**Prerequisites:** power laws and log-log plots; minimizing a function under a constraint (derivative = 0); the idea of training loss, learning-rate schedules, and 0/5-shot evaluation. Terms: FLOPs = floating-point operations (a measure of compute); token = a unit of text; Gopher = an earlier 280B-parameter model trained on 300B tokens; IsoFLOP = compared at equal FLOPs; epoch = one pass over the training data; MMLU and Winogender = benchmarks (a multi-subject exam test and a pronoun-resolution test).
