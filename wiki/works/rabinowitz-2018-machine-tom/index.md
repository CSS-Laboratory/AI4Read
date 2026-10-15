---
id: rabinowitz-2018-machine-tom/index
work: rabinowitz-2018-machine-tom
type: work-map
units: [rabinowitz-2018-machine-tom/main]
generated: deterministic
---

# Rabinowitz, N. C., Perbet, F., Song, H. F., Zhang, C., Eslami, S. M. A., & Botvinick, M. (2018). Machine theory of mind. In *Proceedings of the 35th International Conference on Machine Learning* (PMLR, Vol. 80, pp. 4218–4227).

## One digest
This work has a single digest, which is also its work-level summary: [[rabinowitz-2018-machine-tom/main]].

## In one line
A neural "observer" (the ToMnet) can meta-learn, from behaviour alone and with weak assumptions, a prior over agents plus a fast agent-specific posterior, and in gridworlds this is enough to pass a Sally-Anne-style false-belief test.

## The gist
How can an observer learn by itself to model other agents from few observations, without a hand-built model of rational planning? The authors build the ToMnet (a "Theory of Mind network", a neural observer), which meta-learns (learns to learn) across many agents. Its weights act as a general prior, and an embedding computed from one agent's past behaviour acts as an agent-specific posterior. In gridworlds it approximates Bayes-optimal inference for random agents, infers goals, models deep-RL agents, and predicts that agents act on false beliefs when changes happen out of their sight. A further variant reports beliefs explicitly. The authors stress that the experiments are simple, and scaling is open.

**Prerequisites:** POMDPs (tasks where the agent sees only part of the state) and policies; gridworlds (grid-shaped toy environments); embeddings (learned vector summaries); Bayesian posterior/prior; Dirichlet distribution; value iteration; KL and Jensen-Shannon divergence; basic deep learning (embeddings, LSTM).
