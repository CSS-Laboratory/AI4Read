---
id: argyle-2023-silicon/index
work: argyle-2023-silicon
type: work-map
units: [argyle-2023-silicon/main-p1, argyle-2023-silicon/main-p2]
---

# Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). *Out of One, Many: Using Language Models to Simulate Human Samples*. Political Analysis, 31(3), 337–351. DOI:10.1017/pan.2023.2.

## In one paragraph
The paper asks whether a language model can stand in for human survey respondents. The authors treat GPT-3's "bias" as many demographically specific response distributions rather than one uniform bias. They call the accuracy of those distributions *algorithmic fidelity* and propose four criteria for it. They then condition GPT-3 on first-person backstories taken from real survey respondents, which they call "silicon sampling". In three U.S. politics studies (partisan word lists, vote choice, associations among survey items), the output closely matches human subgroups. The main exception is pure independents. The authors suggest using silicon samples to pilot studies cheaply before collecting human data. They warn that the evidence covers only U.S. politics and that the method could be misused. This is the founding paper of LLM-based respondent simulation.

## The path through the work
- [[argyle-2023-silicon/main-p1]] — The authors argue that GPT-3, conditioned on first-person demographic backstories from real survey respondents, produces "silicon samples" whose response patterns closely match those of matching human subgroups in U.S. politics (which they call *algorithmic fidelity*).
- [[argyle-2023-silicon/main-p2]] — The appendices document how GPT-3 "silicon samples" of respondents to the American National Election Studies (ANES, a US election survey) were built and scored in Studies 2 and 3, and add agreement tables, an ablation (dropping inputs to see the effect), a model comparison, Study 3 checks and costs.

## Big ideas across units
- **Bias as a mixture of distributions, summarised as algorithmic fidelity.** The model's outputs are treated as coming from many conditional distributions, and fidelity is how well these match human subgroups. Introduced in main-p1 and tested in the appendix material of main-p2.
- **Four minimal criteria for fidelity.** Turing test, backward continuity, forward continuity and pattern correspondence, with no numeric thresholds. Support must be repeated across data sources, measures and groups. Units: main-p1.
- **Silicon sampling with real backstories.** Backstories come from a representative human sample (ANES). This corrects the model's skewed backstory distribution, provided P(V|B) is right. main-p2 shows how the backstories were built. Units: main-p1, main-p2.
- **Evidence is aggregate, not individual.** Study 3 compares patterns of association (Cramér's V), not individual answers. Units: main-p1, main-p2.
- **Independents are the weak spot.** Whole-sample tetrachoric correlations are 0.90–0.94, but 2020 independents are near zero (0.02). Strong partisans are near-perfect. Units: main-p1, main-p2.
- **Implementation choices matter.** Study 2 reads next-token probabilities with synonym tokens collapsed, so temperature is irrelevant. Study 3 samples text at temperature 0.7, which gave the smallest differences of the three tried. Units: main-p1, main-p2.
- **Several agreement measures and robustness checks.** The main text reports tetrachoric correlation and Cramér's V. The appendix adds Cohen's κ, ICC and raw agreement, plus an ablation, a model comparison and a synthetic-only check. Units: main-p1, main-p2.
- **Cheap piloting, with stated limits.** Costs are $29, $75 and $1,428 for Studies 1–3. The authors warn of misinformation, manipulation and fraud, and note that the evidence covers only U.S. politics. Units: main-p1, main-p2.

## How to read it
- Read [[argyle-2023-silicon/main-p1]] first. It is essential. Start with the algorithmic-fidelity definition and the four criteria, then the three studies and the caveats.
- [[argyle-2023-silicon/main-p2]] is the appendix and depends on main-p1, since it documents how Studies 2 and 3 were built and scored. On a first pass you can skip most of it.
- Still worth reading in main-p2: the subgroup results (independents), the Study 3 logic, and the differences from humans (descriptive statistics, missing data).
- Read the rest of main-p2 (scoring statistics, ablation, model comparison, temperature checks) when you want to replicate the method or judge its robustness.

## Concepts introduced
- [[algorithmic-fidelity]] — main-p1
- [[silicon-sample]] — main-p1
- [[silicon-sampling]] — main-p1
- [[language-model]] — main-p1
- [[conditioning-context]] — main-p1
- [[zero-shot-few-shot-prompting]] — main-p1
- [[social-science-turing-test]] — main-p1
- [[backward-forward-continuity]] — main-p1
- [[pattern-correspondence]] — main-p1
- [[sampling-temperature]] — main-p1 (main-p2 links the related [[temperature-sampling]])
- [[tetrachoric-correlation]] — main-p1
- [[cramers-v]] — main-p1
- [[backstory-template]] — main-p2
- [[token-set-collapsing]] — main-p2
- [[temperature-sampling]] — main-p2
- [[cohens-kappa]] — main-p2
- [[intraclass-correlation]] — main-p2
- [[proportion-agreement]] — main-p2
- [[ablation-study]] — main-p2
- [[target-factor]] — main-p2
