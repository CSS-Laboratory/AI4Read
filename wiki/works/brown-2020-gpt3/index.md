---
id: brown-2020-gpt3/index
work: brown-2020-gpt3
type: work-map
units: [brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, brown-2020-gpt3/main-p3]
---

# Brown, T. B., Mann, B., Ryder, N., Subbiah, M., et al. (2020). *Language Models are Few-Shot Learners*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020). arXiv:2005.14165.

## In one paragraph
The paper asks whether a very large language model can learn a new task from an instruction or a few examples in its prompt, with no gradient updates. The authors train eight models of 125M to 175B parameters (GPT-3 is the largest). They test them zero-, one- and few-shot on dozens of benchmarks and new synthetic tasks. Few-shot performance generally improves with model size and is sometimes competitive with fine-tuned state of the art. It stays weak on some tasks, such as NLI and WiC. The authors also audit their results for test-set contamination and discuss limitations, bias, misuse and energy cost. The work matters because it turns task specification into text conditioning, which is the basis of the modern prompting approach.

## The path through the work
- [[brown-2020-gpt3/main-p1]] — Scaling an autoregressive language model to 175B parameters makes it much better at learning a task from instructions or a few examples in its prompt, with no weight updates, though results vary strongly by task.
- [[brown-2020-gpt3/main-p2]] — The authors test whether GPT-3's benchmark scores are inflated by test-set leakage (mostly they are not, with PIQA and Winograd flagged), then list the model's limits, its social risks (bias, misuse, energy) and the technical details behind the work.
- [[brown-2020-gpt3/main-p3]] — This part of the paper shows how each task was formatted as a text prompt with answer options or a target completion (App. G) and lists the zero-, one- and few-shot score of every task for all eight model sizes (App. H).

## Big ideas across units
- **In-context learning as task specification.** The task is given as an instruction and/or K demonstrations in the prompt, with no weight updates. The units show the idea (main-p1), question what it really does (main-p2), and print the exact prompt formats (main-p3). Units: main-p1, main-p2, main-p3.
- **Scale as the main lever.** Validation loss follows a power law in compute, and many few-shot results improve with model size. Arithmetic accuracy jumps between 13B and 175B, and Table H.1 lists every size. Units: main-p1, main-p3.
- **Uneven performance.** Few-shot GPT-3 matches or beats fine-tuned SOTA on some tasks (LAMBADA, TriviaQA) but is weak on "comparison" tasks (WiC, ANLI). Units: main-p1, main-p2, main-p3.
- **Benchmark contamination and how to audit it.** A filtering bug left overlap between training data and benchmarks. The authors audit afterwards with 13-gram "clean" subsets and flag PIQA and Winograd. Units: main-p1, main-p2.
- **Evaluation protocol details matter.** Prompt wording and scoring rules differ by task, for example unconditional-probability normalization, partial evaluation and all-correct scoring. Units: main-p1, main-p3.
- **Generated text and human detection.** Humans scored about 52% (chance is 50%) on news articles written by the 175B model, and the appendices give the experiment details. Units: main-p1, main-p2.
- **Societal and resource costs.** Bias probes, the misuse assessment and training-compute accounting. Units: main-p1 (training recipe), main-p2.

## How to read it
- **Essential:** main-p1 (the zero/one/few-shot framing, approach and main results) and main-p2 (contamination audit, limitations, broader impacts). The catalog recommends the introduction first, then limitations and broader impacts.
- **Skippable on a first pass:** main-p3. It contains no new argument and works as a reference for checking how a task was posed or looking up exact numbers. The appendix material in main-p2 (data filtering, training settings, FLOP counting) can also wait.
- **Dependencies:** main-p2 builds on main-p1, since the contamination bug and the limitation claims refer to its results. main-p3 depends on main-p1 for the prompting setup and on main-p2 for the scoring and contamination context.

## Concepts introduced
- [[in-context-learning]] — main-p1
- [[zero-shot-few-shot-prompting]] — main-p1
- [[pretraining-fine-tuning]] — main-p1
- [[meta-learning]] — main-p1
- [[scaling-law]] — main-p1
- [[language-model]] — main-p1
- [[perplexity]] — main-p1
- [[cross-entropy-log-loss]] — main-p1
- [[tokenization-bpe]] — main-p1
- [[data-contamination]] — main-p1
- [[closed-book-qa]] — main-p1
- [[human-detection-of-generated-text]] — main-p1
- [[benchmark-contamination]] — main-p2
- [[n-gram-overlap-decontamination]] — main-p2
- [[encoder-only / decoder-only]] — main-p2 (id as written in the unit)
- [[symbol grounding]] — main-p2 (id as written in the unit)
- [[nucleus-sampling-temperature]] — main-p2
- [[co-occurrence-bias-probe]] — main-p2
- [[distillation]] — main-p2
- [[fuzzy-deduplication]] — main-p2
- [[quality-filter-classifier]] — main-p2
- [[training-compute-pf-days]] — main-p2
- [[task-prompt-format]] — main-p3
- [[unconditional-probability-normalization]] — main-p3
- [[partial-evaluation]] — main-p3
- [[per-question-all-correct-accuracy]] — main-p3
