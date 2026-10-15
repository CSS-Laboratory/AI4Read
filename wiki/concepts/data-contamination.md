---
id: data-contamination
type: concept
fields: [llm, theory-of-mind]
fields_strong: [llm, theory-of-mind]
n_sources: 5
n_works: 5
tiers: [deep, core]
grounding: digests
sources: [brown-2020-gpt3/main-p1, kosinski-2024-llm-tom/main, shapira-2024-clever-hans/main, strachan-2024-llm-humans/main, ullman-2023-trivial-alterations/main]
raw_ids: [data contamination]
canon_spine: [theory-of-mind]
generated_by: build_kg.py
---

# data-contamination

## Canon spine entry

- **data contamination** (theory-of-mind): test items, or close variants, appearing in a model's training data (UG)

## Definitions in the sources

### theory-of-mind

- [[kosinski-2024-llm-tom/main]] (§ "Introduction", § "Methodological Notes"): tasks seen in training; handled by bespoke tasks and pre-publication model selection [as `data contamination`; work fields: theory-of-mind, llm]
- [[shapira-2024-clever-hans/main]] (p. 2265, 2273): possible training on test data or related material; cannot be quantified without open training data [as `data contamination`; work fields: theory-of-mind, llm]
- [[strachan-2024-llm-humans/main]] (§ "Performance across theory of mind tests"): novel items written to control for test items being in training data [as `data contamination`; work fields: theory-of-mind, llm]
- [[ullman-2023-trivial-alterations/main]] (p. 9): a benchmark or generator may be absorbed in training [work fields: theory-of-mind, llm]

### llm

- [[brown-2020-gpt3/main-p1]] (pp. 6, 9): test or dev content inadvertently present in the pre-training corpus; assessed in §4, with asterisks on some results [new]

## Candidate bridges

- [structural-analogy] Data contamination of benchmarks ↔ train–test leakage / measurement validity in empirical social science (pp. 6, 9) — from [[brown-2020-gpt3/main-p1]] (llm → unspecified)
