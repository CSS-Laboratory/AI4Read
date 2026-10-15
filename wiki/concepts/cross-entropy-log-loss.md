---
id: cross-entropy-log-loss
type: concept
fields: [llm]
n_sources: 18
tiers: [reference, deep, core]
grounding: digests
sources: [bahdanau-2015-attention/main, bengio-2003-nplm/main, brown-2020-gpt3/main-p1, devlin-2019-bert/main, hoffmann-2022-chinchilla/main, kaplan-2020-scaling/main, ouyang-2022-instructgpt/main-p1, prince-2023-udl/ch05-loss, prince-2023-udl/ch08-measuring, prince-2023-udl/ch12-transformers, prince-2023-udl/ch14-unsupervised, prince-2023-udl/ch15-generative, prince-2023-udl/ch16-normalizing, prince-2023-udl/ch23-probability, radford-2019-gpt2/main, schaeffer-2023-mirage/main, wei-2022-emergent/main, xie-2022-icl/main]
raw_ids: [cross-entropy / log-loss]
canon_spine: llm
generated_by: build_kg.py
---

# cross-entropy-log-loss

## Canon spine entry

- **cross-entropy / log-loss** (llm): the average negative log-probability the model assigns to the true next token; the quantity LMs minimize (UG)

## Definitions in the sources

### llm

- [[bahdanau-2015-attention/main]] (p. 9, 14): training maximises the conditional log-probability of correct translations (NLL in Table 2)
- [[bengio-2003-nplm/main]] (p. 1142): here the average log-likelihood $L$ is maximized, plus regularization [as `cross-entropy / log-loss`]
- [[brown-2020-gpt3/main-p1]] (pp. 4, 10): validation loss tracked across sizes; the paper says it correlates well with many downstream tasks
- [[devlin-2019-bert/main]] (p. 4174–4175): loss at the masked positions and for classification [as `cross-entropy / log-loss`]
- [[hoffmann-2022-chinchilla/main]] (pp. 24–25): the expected log-loss risk $L(f)$ (Eq. 6); its minimum (the Bayes risk) is also called the entropy of natural text
- [[kaplan-2020-scaling/main]] (p. 6): loss in nats averaged over a 1024-token context; the paper's main metric
- [[ouyang-2022-instructgpt/main-p1]] (p. 8): the RM is trained with a cross-entropy loss over pairwise comparisons [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch05-loss]] (p. 72): in this chapter, the negative log-likelihood, shown equivalent to minimizing KL divergence to the empirical distribution
- [[prince-2023-udl/ch08-measuring]] (p. 120): multiclass loss; test loss rises when wrong predictions grow more confident [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch12-transformers]] (pp. 220–224): multiclass/binary cross-entropy used for masking, next-token and fine-tuning losses [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch14-unsupervised]] (p. 270): here the summed negative log-likelihood of the data, eq. 14.1 [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch15-generative]] (p. 278): binary form is the discriminator loss [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch16-normalizing]] (p. 307): negative log-likelihood training objective [as `cross-entropy / log-loss`]
- [[prince-2023-udl/ch23-probability]]: are not defined in this unit.
- [[radford-2019-gpt2/main]] (pdf 4): the average negative log probability per canonical prediction unit, before scaling or exponentiation; LM results are commonly reported as a scaled or exponentiated version of it [as `cross-entropy / log-loss`]
- [[schaeffer-2023-mirage/main]] (p. 4): per-token loss $-\log\hat p_N(v^*)$ with a one-hot target; assumed to fall smoothly
- [[wei-2022-emergent/main]] (pp. 7, 19): loss used in scaling laws. It can improve at scales where accuracy, exact match or BLEU stay near random
- [[xie-2022-icl/main]] (p. 23): multiclass logistic risk $L_{CE}$ used with the calibration function $g$ to turn KL bounds into 0-1 bounds

## Candidate bridges

- [structural-analogy] Negative log-likelihood / cross-entropy ↔ llm: canon's "cross-entropy / log-loss" and "perplexity (exp of cross-entropy)" — perplexity is the exponential of this loss (canon link; not stated in this unit). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [same-math] Eq. 14.1, summed negative log-likelihood ↔ llm: cross-entropy / log-loss — the same quantity up to dividing by the number of examples. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [structural-analogy] ELBO gap equals KL to posterior ↔ llm (cross-entropy / log-loss): both are likelihood-based training objectives, here approximated by a bound. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
