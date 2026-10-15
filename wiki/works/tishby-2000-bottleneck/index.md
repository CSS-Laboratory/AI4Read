---
id: tishby-2000-bottleneck/index
work: tishby-2000-bottleneck
type: work-map
units: [tishby-2000-bottleneck/main]
generated: deterministic
---

# Tishby, N., Pereira, F. C., & Bialek, W. (2000). *The information bottleneck method*. arXiv:physics/0004057.

## One digest
This work has a single digest, which is also its work-level summary: [[tishby-2000-bottleneck/main]].

## In one line
Compress a signal X into a short code X̃ that keeps as much information as possible about a second variable Y; the "distortion" then comes out of the joint statistics, as a KL divergence.

## The gist
Rate distortion theory needs a distortion function chosen in advance, and that choice fixes which features of X count as relevant. The authors instead pick a relevance variable Y. They minimise $I(\tilde X;X)-\beta I(\tilde X;Y)$ over stochastic encoders $p(\tilde x|x)$ (random maps from x to codewords x̃). This gives exact self-consistent equations in which the effective distortion is $D_{KL}[p(y|x)\|p(y|\tilde x)]$, which is not assumed beforehand. A Blahut–Arimoto-style alternating iteration (the known way to compute rate distortion solutions) solves them. It converges, but the convergence proof does not show that the solution is unique. Varying β traces curves in an "information plane" (the plane of $I(X;\tilde X)$ against $I(\tilde X;Y)$), with phase-transition-like bifurcations.

**Prerequisites:** mutual information; KL divergence; Lagrange multipliers and functional derivatives; Markov chains; basic rate distortion idea.
