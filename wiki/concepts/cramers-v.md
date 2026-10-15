---
id: cramers-v
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [argyle-2023-silicon/main-p1, argyle-2023-silicon/main-p2]
generated_by: build_kg.py
---

# cramers-v

## Definitions in the sources

### llm

- [[argyle-2023-silicon/main-p1]] (p. 12): association measure for categorical variables that accounts for base-rate differences [new]
- [[argyle-2023-silicon/main-p2]] (p. 43): 0–1 association measure for categorical variables, based on chi-squared [new]

## Instances that use it

- [[anes-cramers-v-comparison]] — interview-style conditioning, with Cramér's V compared between ANES and GPT-3 for 2016 — from [[argyle-2023-silicon/main-p1]]
- [[study3-virtual-interview]] — Study 3: mock ANES interview, one answer sampled; associations compared via Cramér's V — from [[argyle-2023-silicon/main-p2]]

## Candidate bridges

- [same-math] Cramér's V ↔ statistics: chi-squared test of independence, rescaled to 0–1; for 2×2 tables it equals |φ|. — from [[argyle-2023-silicon/main-p2]] (llm → other:statistics)
