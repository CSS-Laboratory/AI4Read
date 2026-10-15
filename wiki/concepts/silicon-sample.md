---
id: silicon-sample
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 3
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [argyle-2023-silicon/main-p1, argyle-2023-silicon/main-p2, ziems-2024-css/main-p2]
canon_spine: [llm]
generated_by: build_kg.py
---

# silicon-sample

## Canon spine entry

- **silicon sample** (llm): LLM outputs conditioned on persona backstories, used as stand-ins for human respondents (grad)

## Definitions in the sources

### llm

- [[argyle-2023-silicon/main-p1]] (p. 3): GPT-3 outputs conditioned on real respondents' backstories, one simulated subject per human participant
- [[argyle-2023-silicon/main-p2]] (pp. 30, 38): GPT-3 outputs conditioned on real respondents' backstories, compared with their human answers
- [[ziems-2024-css/main-p2]] (p. 270): LLMs used as simulated sample populations in CSS; the authors stress limited predictive power and higher opinion homogeneity than humans

## Instances that use it

- [[anes-vote-choice-silicon-sample]] — GPT-3 vote choice conditioned on ANES backstories for 2012, 2016, 2020 — from [[argyle-2023-silicon/main-p1]]

## Candidate bridges

- [structural-analogy] A form-only LM versus real human subgroups ↔ silicon samples / algorithmic fidelity: an LM reproduces distributions of forms that people produced, which the paper describes as a reflection of the speakers' communicative intents and the meaning relation. — from [[bender-2020-octopus/main]] (llm → llm)
- [structural-analogy] interviewing agents ↔ silicon samples and algorithmic fidelity: both use LLM outputs as proxies for human respondents. — from [[park-2023-agents/main]] (llm → llm)
- [structural-analogy] Mode dropping (missing parts of the data) ↔ llm: algorithmic fidelity of silicon samples — both ask whether generated output covers all real subgroups — from [[prince-2023-udl/ch15-generative]] (llm → llm)
- [metaphor] A persona/backstory prompt selecting a subgroup distribution ↔ silicon sample / algorithmic fidelity (conditioning an LM selects a conditional distribution); the paper does not discuss this. — from [[xie-2022-icl/main]] (llm → unspecified)
