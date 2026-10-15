---
id: geva-2021-ffn/index
work: geva-2021-ffn
type: work-map
units: [geva-2021-ffn/main]
generated: deterministic
---

# Geva, M., Schuster, R., Berant, J., & Levy, O. (2021). *Transformer Feed-Forward Layers Are Key-Value Memories*. Proceedings of EMNLP 2021, 5484–5495. DOI:10.18653/v1/2021.emnlp-main.446.

## One digest
This work has a single digest, which is also its work-level summary: [[geva-2021-ffn/main]].

## In one line
The feed-forward layers of a transformer language model behave like key-value memories: keys detect input patterns, values (mostly in the upper layers) push probability toward likely next tokens, and layer outputs are mixtures of many memories refined through the residual connections.

## The gist
Feed-forward layers hold about two-thirds of a transformer's parameters, but their role was little studied. The authors note that such a layer has the same form as a key-value neural memory, except for the non-linearity. They test this in a 16-layer language model trained on WikiText-103. Keys fire on human-recognisable patterns: lower layers tend to show shallow ones (such as a shared last word), upper layers more semantic ones. In upper layers, values tend to assign higher probability to the token that follows the key's patterns. Each layer's output is usually a composition of many memories, not one dominant memory. The residual connections then refine the prediction layer by layer.

**Prerequisites:** matrix–vector products; softmax; ReLU; residual connections and layer normalisation in transformers; the idea of an output embedding matrix.
