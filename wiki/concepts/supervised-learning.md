---
id: supervised-learning
type: concept
fields: [llm, political-science]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [grimmer-2022-textasdata/ch19-classifying, prince-2023-udl/ch01-introduction, prince-2023-udl/ch02-supervised]
generated_by: build_kg.py
---

# supervised-learning

## Definitions in the sources

### llm

- [[prince-2023-udl/ch01-introduction]] (p. 1, 5): learn an input→output mapping from labelled input/output pairs [new]
- [[prince-2023-udl/ch02-supervised]] (p. 17): learning a mapping from inputs to outputs using input/output training pairs [new]

### political-science

- [[grimmer-2022-textasdata/ch19-classifying]] (p. 318): fit a model to labelled training texts, then predict labels for unlabelled texts (p. 318) (new)

## Candidate bridges

- [metaphor] Training $\tilde\mu(x,r)$ to imitate an expert ↔ supervised learning/imitation: regression onto good actions (p. 39). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → other)
- [metaphor] "Seeing itself" in bidirectional conditioning ↔ target leakage in supervised learning — the model gets the answer through its input. — from [[devlin-2019-bert/main]] (llm → unspecified)
- [structural-analogy] Dictionary score $\pi_i$ ↔ supervised learning: a linear function of normalized word counts, but with weights set by hand rather than learned (p. 283 describes this contrast). — from [[grimmer-2022-textasdata/ch16-word]] (political-science → other)
- [structural-analogy] train/test split for measurement ↔ supervised learning: held-out evaluation guards against overfitting to the selection process (p. 356). — from [[grimmer-2022-textasdata/ch21-repurposing]] (political-science → other)
- [same-math] Rescorla–Wagner update (14.2–14.3) ↔ supervised learning: the LMS/Widrow–Hoff rule — the text calls them essentially the same, with the differences noted in footnote 3. — from [[sutton-2018-rl/ch14-psychology]] (control-theory → other)
