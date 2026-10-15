---
id: wordfish
type: concept
fields: [political-science]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch21-repurposing]
generated_by: build_kg.py
---

# wordfish

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 27): Poisson-IRT scaling, $\lambda_{ij}=\exp(\alpha_i+\psi_j+\beta_j\theta_i)$ [new]
- [[grimmer-2022-textasdata/ch21-repurposing]] (p. 352): Poisson-IRT text scaling, $\lambda_{ij}=\exp(\alpha_i+\psi_j+\mu_j\pi_i)$ [new]

## Instances that use it

- [[wordfish-german-platforms-vs-senate]] — works on party platforms, fails to separate Democrats and Republicans in press releases — from [[grimmer-2013-textasdata/main]]
- [[wordfish-german-platforms]] — ideological dominance holds; separates parties, matches expert assessments — from [[grimmer-2022-textasdata/ch21-repurposing]]
- [[wordfish-senate-press-releases]] — fails to separate parties, but correlates 0.86 with the expressed-agenda scaling — from [[grimmer-2022-textasdata/ch21-repurposing]]

## Candidate bridges

- [structural-analogy] Wordfish's $\alpha_i+\psi_j+\beta_j\theta_i$ ↔ roll-call IRT scaling: discrimination parameter times latent position — same logic applied to words instead of votes. — from [[grimmer-2013-textasdata/main]] (political-science → other)
- [structural-analogy] Wordfish's $\pi_i$ ↔ spatial model of voting: positions in a low-dimensional space inferred from behavior (here word use). — from [[grimmer-2022-textasdata/ch21-repurposing]] (political-science → political-science)
