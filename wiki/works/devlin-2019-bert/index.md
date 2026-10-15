---
id: devlin-2019-bert/index
work: devlin-2019-bert
type: work-map
units: [devlin-2019-bert/main]
generated: deterministic
---

# Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. Proceedings of NAACL-HLT 2019, Vol. 1, 4171–4186. DOI:10.18653/v1/N19-1423.

## One digest
This work has a single digest, which is also its work-level summary: [[devlin-2019-bert/main]].

## In one line
A Transformer encoder pre-trained to predict randomly masked tokens from both left and right context (plus next-sentence prediction) can be fine-tuned with one extra output layer to set new state-of-the-art results on eleven NLP tasks.

## The gist
Standard language models are unidirectional (they condition on context from one side only), which the authors argue limits pre-trained representations, especially when fine-tuning for token-level tasks like question answering. This paper proposes BERT, a Transformer encoder pre-trained on unlabeled text with a masked-word objective (predict hidden tokens from both sides) plus next-sentence prediction. The same pre-trained model is then fine-tuned on each task with one extra output layer. The authors report new best results on eleven tasks (benchmarks and datasets such as GLUE, SQuAD and SWAG). Their ablations indicate that bidirectionality and the two pre-training tasks matter, and that bigger models help even on small tasks. The central claim is that one pre-trained model can serve many tasks with minimal architecture change.

**Prerequisites:** Transformer self-attention and encoder layers; softmax and cross-entropy; the idea of pre-training then fine-tuning; vectors and dot products; basic NLP metrics (accuracy, F1).
