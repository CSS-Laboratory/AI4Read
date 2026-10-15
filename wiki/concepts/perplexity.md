---
id: perplexity
type: concept
fields: [llm, bayesian]
n_sources: 12
tiers: [core, deep, reference]
grounding: digests
sources: [bengio-2003-nplm/main, brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p3, devlin-2019-bert/main, hoffmann-2022-chinchilla/main, mikolov-2013-efficient/main, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch20-generative, radford-2019-gpt2/main, vaswani-2017-transformer/main, wei-2022-emergent/main, xie-2022-icl/main]
canon_spine: information-theory
generated_by: build_kg.py
---

# perplexity

## Canon spine entry

- **perplexity** (information-theory): 2^{cross-entropy}: the effective number of equally likely choices a model faces per token (UG)

## Definitions in the sources

### llm

- [[bengio-2003-nplm/main]] (p. 1141): geometric average of $1/\hat P(w_t \mid w_1^{t-1})$, the exponential of the average negative log-likelihood
- [[brown-2020-gpt3/main-p1]] (pp. 11–12): used for zero-shot PTB (20.5) and LAMBADA ppl (3.00 / 3.35 / 1.92)
- [[brown-2020-gpt3/main-p3]] (p. 63): LAMBADA is reported both as accuracy and as ppl in Table H.1
- [[devlin-2019-bert/main]] (p. 4179): masked-LM perplexity on held-out training data is reported for each model size
- [[hoffmann-2022-chinchilla/main]] (p. 10): reported for Wikitext103, 7.16 vs 7.75
- [[mikolov-2013-efficient/main]] (p. 3): used only in the Huffman-tree output count
- [[radford-2019-gpt2/main]] (pdf 4): scaled or exponentiated average negative log-probability per canonical unit; used to compare LMs on datasets
- [[vaswani-2017-transformer/main]] (p. 9): reported per word-piece in Table 3
- [[wei-2022-emergent/main]] (p. 8): here, language-model perplexity on WikiText103, used as an alternative x-axis for emergence
- [[xie-2022-icl/main]] (p. 10): pretraining (validation) loss; in GINC, same loss with different ICL accuracy

### bayesian

- [[murphy-2023-pml2/ch05-information-p1]] (p. 237): $2^{\mathbb H_{ce}}$ [new]
- [[murphy-2023-pml2/ch20-generative]] (p. 783): $2^H$, with $H$ the NLL/cross entropy [new]

## Instances that use it

- [[brown-corpus-experiment]] — test-perplexity difference of about 24% from the best n-gram — from [[bengio-2003-nplm/main]]
- [[ap-news-experiment]] — test-perplexity difference of about 8% from the best n-gram, with a $n=6$ network — from [[bengio-2003-nplm/main]]
- [[lambada]] — long-context last-word prediction; 8.63 perplexity, 63.24% accuracy with a stop-word filter — from [[radford-2019-gpt2/main]]
- [[wikitext103-perplexity]] — alternative x-axis to scale for MMLU emergence — from [[wei-2022-emergent/main]]

## Candidate bridges

- [structural-analogy] Train/test split and generalization ↔ held-out perplexity for language models. — from [[prince-2023-udl/ch02-supervised]] (llm → unspecified)
- [structural-analogy] Negative log-likelihood / cross-entropy ↔ llm: canon's "cross-entropy / log-loss" and "perplexity (exp of cross-entropy)" — perplexity is the exponential of this loss (canon link; not stated in this unit). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [same-math] Test likelihood ↔ llm: held-out log-loss / perplexity — perplexity is the exponential of held-out cross-entropy. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [structural-analogy] IS exponentiates an average KL divergence ↔ llm: perplexity exponentiates an average log-loss — both turn an information measure into an "effective number". — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [same-math] "Entropy $n$ bits ≈ $2^n$ equiprobable states" ↔ language modelling: perplexity $=2^{\text{entropy}}$ — the effective number of choices. — from [[stone-2022-information/ch10-thermodynamic]] (information-theory → llm)
