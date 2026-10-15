---
id: language-model
type: concept
fields: [llm, political-science]
fields_strong: [llm, political-science]
n_sources: 13
n_works: 10
tiers: [core, deep, reference]
grounding: digests
sources: [argyle-2023-silicon/main-p1, bender-2020-octopus/main, bengio-2003-nplm/main, brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, grimmer-2022-textasdata/ch06-multinomial, mahowald-2024-dissociating/main, mikolov-2013-efficient/main, piantadosi-2022-meaning/main, prince-2023-udl/ch01-introduction, prince-2023-udl/ch05-loss, prince-2023-udl/ch12-transformers, radford-2019-gpt2/main]
raw_ids: [language model]
canon_spine: [llm]
generated_by: build_kg.py
---

# language-model

## Canon spine entry

- **language model** (llm): a probability distribution over token sequences, usually factored as next-token prediction p(x_t | x_<t) (UG)

## Definitions in the sources

### llm

- [[argyle-2023-silicon/main-p1]] (p. 3): here, a conditional distribution $p(x_n\mid x_1,\dots,x_{n-1})$ over tokens, sampled iteratively
- [[bender-2020-octopus/main]] (p. 5185): here, any system trained only on string prediction, at any granularity and in any order
- [[bengio-2003-nplm/main]] (p. 1138): a joint probability over word sequences, factored as a product of next-word conditionals [as `language model`]
- [[brown-2020-gpt3/main-p1]] (pp. 1, 8): here an autoregressive transformer (GPT-2 architecture, alternating dense and sparse attention) with $n_{\text{ctx}} = 2048$
- [[brown-2020-gpt3/main-p2]] (p. 33): here, autoregressive models only; the authors avoid bidirectional or denoising models [as `language model`]
- [[mahowald-2024-dissociating/main]] (p. 6, 16): here, a model trained on word-in-context prediction; "large" refers to parameters and training data
- [[mikolov-2013-efficient/main]] (pp. 3–4): here, NNLM and RNNLM, which predict a word from history
- [[piantadosi-2022-meaning/main]] (pdf 1): here, a system trained to predict words from surrounding context
- [[prince-2023-udl/ch01-introduction]] (p. 8): here only (the text says "generative model of text data"; the term "language model" does not appear): a model that assigns a probability to every output string and can be sampled; no next-token factoring is given
- [[prince-2023-udl/ch05-loss]] (p. 67): not defined here; the chapter's K-class example of predicting the next word is one case [weak: not really used in this unit]
- [[prince-2023-udl/ch12-transformers]] (p. 223): autoregressive factorisation of joint token probability (Eq. 12.15) [as `language model`]
- [[radford-2019-gpt2/main]] (pdf 2): a model of $p(x)=\prod p(s_n\mid s_1..s_{n-1})$ over symbol sequences, Eq. (1) [as `language model`]

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 118): model giving a probability to a token sequence (here an unordered set) given parameters [new]

## Instances that use it

- [[cascaded-text-to-image]] — 64→256→1024 pixel cascade conditioned on a language-model caption embedding — from [[prince-2023-udl/ch18-diffusion]]

## Candidate bridges

- [same-math] temperature in sampling ↔ language models: scaling next-token scores before the softmax (canon link; the source describes it only in words). — from [[argyle-2023-silicon/main-p2]] (llm → llm)
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] Bird-watcher missing species ↔ smoothing in language models: unseen events get nonzero probability — avoids zero-probability errors. — from [[mcgrayne-2011-theory/ch07-tool]] (bayesian → llm)
- [structural-analogy] Guessing the next letter (Shannon's experiment) ↔ next-token prediction by language models: both measure how predictable text is, in bits per symbol. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → llm)
- [structural-analogy] Digram- and trigram-based generation of music ↔ n-gram language models: generating from short-context probabilities gives locally plausible but globally wandering output. — from [[pierce-1980-introduction/ch13-information]] (information-theory → llm)
- [structural-analogy] Shannon's k-th order Markov language model (p. 110) ↔ language modelling: n-gram and neural language models. — from [[polyanskiy-2025-information/ch07-tensorization]] (information-theory → llm)
- [structural-analogy] Train/test split and generalization ↔ held-out perplexity for language models. — from [[prince-2023-udl/ch02-supervised]] (llm → unspecified)
- [structural-analogy] Text conditioning via a language-model embedding ↔ LLM: an LLM acts as a text encoder for another model (p. 367–368). — from [[prince-2023-udl/ch18-diffusion]] (llm → llm)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [metaphor] Bayes' rule posterior ↔ language models: Bayesian reading of conditioning on a prompt (canon link; not stated here). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [structural-analogy] Ancestral sampling ↔ language models: autoregressive generation draws each token given earlier ones, like the chain in C.32. — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [structural-analogy] next-letter prediction with $N-1$ letters of context ↔ language-model next-token prediction: uncertainty left after a context is measured the same way. — from [[shannon-1951-prediction/main]] (information-theory → other:language-model-next-token)
