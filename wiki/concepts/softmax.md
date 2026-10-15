---
id: softmax
type: concept
fields: [llm, information-theory]
n_sources: 16
tiers: [reference, deep, core]
grounding: digests
sources: [bahdanau-2015-attention/main, bengio-2003-nplm/main, devlin-2019-bert/main, geva-2021-ffn/main, mackay-2003-information/ch44-supervised, mikolov-2013-compositionality/main, mikolov-2013-efficient/main, prince-2023-udl/ch05-loss, prince-2023-udl/ch08-measuring, prince-2023-udl/ch10-convolutional, prince-2023-udl/ch12-transformers, prince-2023-udl/ch13-graph, prince-2023-udl/ch15-generative, prince-2023-udl/ch19-reinforcement, prince-2023-udl/ch23-probability, vaswani-2017-transformer/main]
canon_spine: llm
generated_by: build_kg.py
---

# softmax

## Canon spine entry

- **softmax** (llm): turns real-valued scores into a probability distribution (UG)

## Definitions in the sources

### llm

- [[bahdanau-2015-attention/main]] (p. 3): turns alignment scores $e_{ij}$ into weights $\alpha_{ij}$ that sum to 1 over source positions
- [[bengio-2003-nplm/main]] (p. 1142): output layer, guaranteeing positive probabilities that sum to 1
- [[devlin-2019-bert/main]] (p. 4174–4177): used over the vocabulary at masked positions, over labels from $C$, over start/end positions, and over SWAG choices
- [[geva-2021-ffn/main]] (pp. 5485, 5487): used to turn $v\cdot E$ into a vocabulary distribution, and in neural memory
- [[mikolov-2013-compositionality/main]] (p. 3): eq. 2; cost proportional to vocabulary size $W$
- [[mikolov-2013-efficient/main]] (p. 3): here, normalization over the vocabulary; its cost is cut by hierarchical softmax
- [[prince-2023-udl/ch05-loss]] (p. 68): maps K arbitrary scores to K non-negative numbers summing to one
- [[prince-2023-udl/ch08-measuring]] (p. 120): turns scores into probabilities; pre-softmax activations driven to extreme values explain the increasing confidence
- [[prince-2023-udl/ch10-convolutional]] (pp. 167, 176): final map from activations to class probabilities
- [[prince-2023-udl/ch12-transformers]] (p. 210): applied per column of $\mathbf K^T\mathbf Q$ to make attention weights
- [[prince-2023-udl/ch13-graph]] (p. 260): normalises attention scores over neighbours
- [[prince-2023-udl/ch15-generative]] (p. 291): gives class probabilities in the ACGAN discriminator
- [[prince-2023-udl/ch19-reinforcement]] (p. 392): turns network outputs into action probabilities in REINFORCE
- [[prince-2023-udl/ch23-probability]]: are not defined in this unit.
- [[vaswani-2017-transformer/main]] (pp. 4–5): turns compatibility scores into attention weights and output probabilities

### information-theory

- [[mackay-2003-information/ch44-supervised]] (p. 530): output layer $y_i=e^{a_i}/\sum e^{a_{i'}}$, coupled outputs summing to one [new]

## Instances that use it

- [[parameter-parallel-softmax]] — output units split across CPUs; about 99.7% of the compute is in the output layer — from [[bengio-2003-nplm/main]]
- [[categorical-softmax]] — softmax from the exponential-family form of the categorical — from [[murphy-2023-pml2/ch02-probability-p2]]
- [[gumbel-softmax-temperature-figure]] — $K=7$ states at several $\tau$ — from [[murphy-2023-pml2/ch06-optimization-p1]]
- [[poisson-categorical-cmgf]] — Poisson and softmax likelihood moments for CMGF — from [[murphy-2023-pml2/ch08-gaussian-p2]]
- [[multiclass-cross-entropy]] — categorical with softmax, eq. 5.24; includes predicting which word follows a sentence — from [[prince-2023-udl/ch05-loss]]

## Candidate bridges

- [same-math] temperature in sampling ↔ language models: scaling next-token scores before the softmax (canon link; the source describes it only in words). — from [[argyle-2023-silicon/main-p2]] (llm → llm)
- [same-math] $c_i=\sum_j\alpha_{ij}h_j$ with softmax weights ↔ probability: an expectation of $h_j$ under a distribution over positions (the paper's own "expected annotation" reading) — from [[bahdanau-2015-attention/main]] (llm → other)
- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$) — from [[bengio-2003-nplm/main]] (llm → llm)
- [same-math] Energy $E$ normalized by $e^{-E}/\sum e^{-E}$ ↔ softmax: a softmax over scores $-E$ — from [[bengio-2003-nplm/main]] (llm → other)
- [structural-analogy] Responsibilities $r_n$ as a normalized probability vector (margin note: Boltzmann/Gibbs) ↔ softmax: normalizing positive scores into a distribution. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [same-math] Speaker softmax $e^{\alpha U}$ with $\alpha=1$ ↔ theory of mind (canon): Boltzmann rationality — the same exponentiated-utility choice rule. — from [[frank-2012-rsa/main]] (theory-of-mind → theory-of-mind)
- [same-math] Transform (19.5), $e^{\psi_l}/\sum e^{\psi}$ ↔ machine learning: softmax — the same function turns free reals into shares summing to 1. — from [[gelman-2013-bda3/ch19-parametric]] (bayesian → other)
- [structural-analogy] $\mathrm{softmax}(xK^\top)V$ (Eq. 2) ↔ attention: weighted average of value vectors with query–key weights. Here keys and values are fixed parameters and no scaling is shown. — from [[geva-2021-ffn/main]] (llm → other)
- [same-math] soft-min responsibilities (20.7) ↔ softmax / Gibbs distribution $p\propto\exp(-\beta\,\text{energy})$ — same exponential-normalized form — from [[mackay-2003-information/ch20-example]] (information-theory → unspecified)
- [same-math] softmax basis (23.33) ↔ machine learning: softmax output layer of a classifier — same normalized-exponential map. — from [[mackay-2003-information/ch23-useful]] (information-theory → other)
- [metaphor] log-domain softmax $\ln\sum e^{l_i}$ ↔ information-theory: log-sum-exp as a soft maximum. — from [[mackay-2003-information/ch26-exact]] (information-theory → information-theory)
- [same-math] Akaike weights ↔ machine learning: softmax of $-\tfrac12\text{dWAIC}$ — the same normalized-exponential formula. — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (bayesian → other)
- [structural-analogy] Hierarchical softmax over a Huffman tree ↔ information theory: short codes for frequent items reduce average work — from [[mikolov-2013-efficient/main]] (llm → information-theory)
- [same-math] Bernoulli/categorical mean from natural parameters (2.173, 2.184) ↔ machine learning: logistic and softmax functions — from [[murphy-2023-pml2/ch02-probability-p2]] (bayesian → other)
- [structural-analogy] InfoNCE (32.16) ↔ softmax cross-entropy: positive is the correct "class" among $M+1$ candidates. — from [[murphy-2023-pml2/ch32-representation]] (bayesian → other)
- [same-math] Multiclass cross-entropy, eq. 5.24 ↔ llm: next-token loss, a softmax over the vocabulary and the negative log-probability of the true token — the chapter names next-word prediction as a K-class case (p. 67). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [structural-analogy] Graph attention ↔ transformer self-attention: both give softmax-weighted sums of transformed inputs. The graph version masks to the adjacency pattern. — from [[prince-2023-udl/ch13-graph]] (llm → llm)
- [same-math] Softmax policy for discrete actions (p. 392) ↔ llm: softmax over vocabulary logits. — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
