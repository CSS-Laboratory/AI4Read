---
id: policy-gradient
type: concept
fields: [control-theory, llm]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p4, prince-2023-udl/ch19-reinforcement, recht-2019-tour/main]
generated_by: build_kg.py
---

# policy-gradient

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p4]] (p. 408): minimize expected cost over policy parameters $r$ by gradient steps on $E\{J_{\tilde\mu(r)}(i_0)\}$ [new]
- [[recht-2019-tour/main]] (p. 10): REINFORCE on a probabilistic policy; the gradient is not an explicit function of the dynamics [new]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (pp. 389–391): gradient ascent on expected return via $\nabla\log\pi$ [new]

## Instances that use it

- [[policy-gradient-discounted-dp]] — Example 3.5.1, trajectory score $\sum_m\nabla\log p(u_m\mid i_m;r)$ with no transition model — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[two-state-policy-gradient-local-minima]] — $J_\alpha(r)$ with local minima at $r=0,1$ — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]

## Candidate bridges

- [structural-analogy] REINFORCE with $\partial\log\pi$ weighted by return ↔ llm: maximum-likelihood next-token training, but weighted by reward and using sampled sequences (the text compares policy-gradient smoothness to maximum likelihood in classification, p. 389). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
