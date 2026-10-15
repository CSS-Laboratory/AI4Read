---
id: bengio-2003-nplm/index
work: bengio-2003-nplm
type: work-map
units: [bengio-2003-nplm/main]
generated: deterministic
---

# Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). *A Neural Probabilistic Language Model*. Journal of Machine Learning Research, 3, 1137–1155.

## One digest
This work has a single digest, which is also its work-level summary: [[bengio-2003-nplm/main]].

## In one line
A language model that learns a real-valued vector for each word, together with a neural network that predicts the next word from those vectors, generalizes to unseen word sequences better than smoothed n-gram models.

## The gist
Language models must assign probabilities to word sequences that never appeared in training. N-gram models cope by gluing short seen fragments, which ignores long context and word similarity. The authors learn a distributed feature vector for every word and, jointly, a neural network that maps the context vectors to a softmax distribution over the next word. Similar words are expected to get nearby vectors, so one training sentence also raises the probability of many similar sentences. Training is costly, so they parallelize it across CPUs. On Brown and AP News, test perplexity differs by about 24% and 8% in favour of the network. The paper shows that learned embeddings plus neural next-word prediction work at scale.

**Prerequisites:** conditional probability and the chain rule; perplexity (exponential of the average negative log-likelihood; lower is better); n-gram model (next-word probabilities from the last $n-1$ words) with back-off and interpolation (falling back to shorter contexts when the long context is unseen); softmax (turns scores into positive probabilities summing to 1); tanh hidden layer; softmax and log-likelihood; a one-hidden-layer network trained by stochastic gradient ascent; matrix–vector shapes.
