---
id: scaling-law
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 10
n_works: 8
tiers: [core, deep]
grounding: digests
sources: [brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, brown-2020-gpt3/main-p3, hoffmann-2022-chinchilla/main, kaplan-2020-scaling/main, radford-2019-gpt2/main, schaeffer-2023-mirage/main, wei-2022-cot/main-p1, wei-2022-emergent/main, ziems-2024-css/main-p1]
raw_ids: [scaling law]
canon_spine: [llm]
generated_by: build_kg.py
---

# scaling-law

## Canon spine entry

- **scaling law** (llm): loss falling as a power law in parameters, data or compute (grad)

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p1]] (pp. 8, 10–11): validation loss follows an approximate power law in compute; the paper's Fig. 3.1 fit is $L = 2.57\,C^{-0.048}$
- [[brown-2020-gpt3/main-p2]] (p. 39): smooth power-law loss trend with scale; this work finds it largely continues [as `scaling law`]
- [[brown-2020-gpt3/main-p3]] (p. 63): Table H.1 provides raw per-size scores across eight sizes; these pages state no law
- [[hoffmann-2022-chinchilla/main]] (pp. 3–4, 6): here, a power law of the optimal $N$ and $D$ in compute $C$ (and, for the loss in $N$, $D$, a power-law-plus-constant form, Eq. 2)
- [[kaplan-2020-scaling/main]] (p. 4, p. 6): loss falls as a power law in parameters, data or compute; here $L(X)\propto1/X^{\alpha_X}$
- [[radford-2019-gpt2/main]] (pdf 1): here only an empirical trend: performance improves with model size (the abstract says "log-linear"), with no formula fitted in the text [as `scaling law`]
- [[schaeffer-2023-mirage/main]] (p. 3–4): power-law decline of test loss with parameters, data or compute; here assumed, not required in exact form
- [[wei-2022-cot/main-p1]] (p. 9): used loosely: "scaling curve" is performance against model size. For many reasoning tasks, chain of thought turns flat curves into rising ones
- [[wei-2022-emergent/main]] (p. 1): consistent, predictable performance improvement with scale, e.g. cross-entropy curves over 7+ orders of magnitude
- [[ziems-2024-css/main-p1]] (pp. 262–263): FLAN mean F1 grows nearly log-linearly with parameters, about 5.0 points per tenfold increase; the GPT-3 001 models do not scale monotonically and GPT-4 gives little over GPT-3.5-turbo

## Candidate bridges

- [structural-analogy] Bubeck & Sellke: smooth interpolation needs ~D× more parameters ↔ llm: scaling laws, where loss falls as parameters grow — both tie capacity to quality — from [[prince-2023-udl/ch20-does]] (llm → llm)
- [structural-analogy] FLAN near-log-linear scaling (5.0 F1 points per decade) ↔ llm: power-law scaling laws — the paper says the trend roughly matches Kaplan et al.'s prediction. — from [[ziems-2024-css/main-p1]] (llm → llm)
