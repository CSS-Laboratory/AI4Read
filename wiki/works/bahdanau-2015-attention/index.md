---
id: bahdanau-2015-attention/index
work: bahdanau-2015-attention
type: work-map
units: [bahdanau-2015-attention/main]
generated: deterministic
---

# Bahdanau, D., Cho, K., & Bengio, Y. (2015). *Neural Machine Translation by Jointly Learning to Align and Translate*. ICLR 2015. arXiv:1409.0473.

## One digest
This work has a single digest, which is also its work-level summary: [[bahdanau-2015-attention/main]].

## In one line
Instead of squeezing a source sentence into one fixed vector, let the decoder compute, for every target word, a learned softmax-weighted average of per-word source annotations, so alignment and translation are trained together.

## The gist
Most earlier neural machine translation models encoded a whole source sentence into one fixed-length vector. The authors conjecture that this is a bottleneck, especially for long sentences. Their model encodes the source into a sequence of annotations (one vector per source word). At each target word, the decoder scores all annotations against its previous state, normalises the scores with a softmax, and uses the weighted sum as a fresh context vector. Because this soft alignment is differentiable, it is trained jointly with everything else. On WMT'14 English→French the authors report that the model beats the plain encoder–decoder regardless of sentence length, and RNNsearch-50 shows no deterioration on long sentences. It comes close to a phrase-based system (Moses). Its alignments look linguistically plausible.

**Prerequisites:** RNN hidden states and gating; softmax; conditional probability and the chain rule; matrix shapes; BLEU as a translation score; SGD.
