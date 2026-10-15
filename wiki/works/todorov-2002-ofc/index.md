---
id: todorov-2002-ofc/index
work: todorov-2002-ofc
type: work-map
units: [todorov-2002-ofc/main]
generated: deterministic
---

# Todorov, E., & Jordan, M. I. (2002). *Optimal feedback control as a theory of motor coordination*. Nature Neuroscience, 5(11), 1226–1235. https://doi.org/10.1038/nn963

## One digest
This work has a single digest, which is also its work-level summary: [[todorov-2002-ofc/main]].

## In one line
An optimal feedback controller corrects only those deviations that hurt the task, so it lets variability pile up in redundant (task-irrelevant) directions, which, the authors argue, explains many coordination phenomena.

## The gist
Motor behaviour reaches goals reliably, yet movement details vary from trial to trial, mostly in directions that do not matter for the task. Serial "plan a trajectory, then track it" models struggle with this. Todorov and Jordan propose stochastic optimal feedback control, with signal-dependent noise (noise that grows with the command size) and delayed, noisy sensing. They argue that the optimal law follows a "minimal intervention" principle. They show this with a local analysis for a general class of systems. Simulations and five experiments (two are reanalyses) support it. Synergies (coupled control directions), controlled parameters, simplifying rules and discrete coordination modes then emerge without being built in. Redundancy becomes part of the solution, not a problem.

**Prerequisites:** expectation and variance; gradient and Hessian; dynamic programming (cost-to-go); linear systems with a quadratic cost and Kalman filtering; PCA.
