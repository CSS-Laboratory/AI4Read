---
id: kaplan-2020-scaling/index
work: kaplan-2020-scaling
type: work-map
units: [kaplan-2020-scaling/main]
generated: deterministic
---

# Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). *Scaling Laws for Neural Language Models*. arXiv:2001.08361.

## One digest
This work has a single digest, which is also its work-level summary: [[kaplan-2020-scaling/main]].

## In one line
Transformer language-model loss falls as a smooth power law in model size, data and compute, so a fixed compute budget is best spent on a very large model trained on modest data and stopped well before convergence.

## The gist
The paper asks how the cross-entropy test loss of Transformer language models depends on model size N (non-embedding parameters), dataset size D, and training compute C. It finds that, when not bottlenecked by the other two factors, loss follows a power law in each, over many orders of magnitude, while depth versus width matters little. Simple fitted equations describe overfitting and training curves, and from them the authors derive how to split a fixed compute budget: mostly into a larger model, with modest data growth, stopping well before convergence. This matters because it makes performance at larger scale predictable, though the authors stress the laws lack a theoretical explanation and must break down eventually.

**Prerequisites:** cross-entropy loss; power laws and log-log plots; partial derivatives (for Appendix B); what a batch, a training step and early stopping are.
