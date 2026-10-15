---
id: generalization
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch01-introduction, prince-2023-udl/ch02-supervised, prince-2023-udl/ch08-measuring, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# generalization

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (p. 261): a model's predictive quality on unseen data [new]
- [[deisenroth-2020-mml/ch01-introduction]] (pp. 11, 13): performing well on unseen data, not merely on training data [new]
- [[strang-2023-introduction/ch10-learning]] (p. 371): accuracy of F on unseen test data from a statistically similar population [new]

### llm

- [[prince-2023-udl/ch02-supervised]] (p. 18): performance on test data not seen in training [new]
- [[prince-2023-udl/ch08-measuring]] (p. 133): how well performance is maintained on new test data [new]

## Instances that use it

- [[great-fantastic-sentiment]] — automatic generalization to unseen words — from [[grimmer-2022-textasdata/ch08-distributed]]
- [[mcallester-generalization-bound]] — Theorem 4.16 — from [[polyanskiy-2025-information/ch05-variational]]
- [[keynes-generalization]] — Keynes's probability increases with a priori logical probability — from [[popper-1959-logic/ch10-corroboration]]
- [[tufa-word-learning]] — a few examples of a novel object word; generalization modelled as inference over a tree (Fig. 1) — from [[tenenbaum-2011-grow/main]]
- [[horse-generalization]] — why "horse" extends to all and only horses — from [[tenenbaum-2011-grow/main]]

## Candidate bridges

- [structural-analogy] adding basis functions until test error rises ↔ model selection generally: complexity versus generalization. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other:statistics)
- [structural-analogy] Training and held-out validation ↔ statistics: fitting a model on one sample and testing on another to check generalization — the same logic, but the chapter gives no shared formalism. — from [[grimmer-2022-textasdata/ch17-overview]] (political-science → other:statistics)
- [same-math] Supervised misclassification error (Ch. 19–20 measurement) ↔ prediction error: the same held-out estimate of generalization error (pp. 384–385) — from [[grimmer-2022-textasdata/ch23-prediction]] (political-science → other:prediction-error)
- [structural-analogy] Symbolic generalizations as part law, part definition ↔ analytic/synthetic distinction: Kuhn calls definitions "tautologies" and says their force shifts over time (p. 183). — from [[kuhn-1962-structure/postscript-1969]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] Online-to-batch conversion ($nR_n^*\le C_n\le\sum R_t^*$) ↔ machine learning: relation between online regret and batch generalization — the same cumulative-versus-last-step logic. — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → llm)
- [structural-analogy] Popper's penny-toss rival laws and constructed predicates ↔ underdetermination and "gruesome"-type predicates: any finite data fit incompatible generalizations. — from [[popper-1959-logic/appvii-untitled-2]] (analytic-philosophy → analytic-philosophy)
- [structural-analogy] Train/test split and generalization ↔ held-out perplexity for language models. — from [[prince-2023-udl/ch02-supervised]] (llm → unspecified)
- [metaphor] Grokking as weight norm falling into the Goldilocks zone ↔ llm: delayed generalization during long pretraining — from [[prince-2023-udl/ch20-does]] (llm → llm)
- [structural-analogy] "Read between the lines" generalization ↔ framing: audiences interpret a message within a wider schema. — from [[slovic-1987-perception/main]] (communication-theory → communication-theory)
- [structural-analogy] Robustness to trivial alterations ↔ ML evaluation: out-of-distribution/adversarial testing of generalization — both probe whether a model learned the rule or surface correlations. — from [[ullman-2023-trivial-alterations/main]] (theory-of-mind → llm)
