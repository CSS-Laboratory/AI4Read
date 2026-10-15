---
id: recht-2019-tour/index
work: recht-2019-tour
type: work-map
units: [recht-2019-tour/main]
generated: deterministic
---

# Recht, B. (2019). *A Tour of Reinforcement Learning: The View from Continuous Control*. Annual Review of Control, Robotics, and Autonomous Systems, 2, 253–279. https://doi.org/10.1146/annurev-control-053018-023825

## One digest
This work has a single digest, which is also its work-level summary: [[recht-2019-tour/main]].

## In one line
The survey's main view is reinforcement learning as optimal control with unknown dynamics, and on the linear quadratic regulator (LQR, a control problem with linear dynamics and quadratic cost) the author reports that simple model-based design with explicit uncertainty beats model-free methods in samples, reliability and safety.

## The gist
Reinforcement learning (RL) is framed as optimal control when the dynamics are unknown. The survey sorts RL methods into model-based, approximate dynamic programming and direct policy search. It compares them on LQR with unknown dynamics. There, a model-based design that also estimates its own model uncertainty (Coarse-ID control) needs far fewer samples than model-free methods and gives stability guarantees. Model-free methods show high variance in the experiments. The author reports that similar patterns appear on harder simulated robot benchmarks. He closes with open problems: merging perception and control, adaptive control, and humans in the loop. The point is that safe, reliable learning systems need tools from both control and learning.

**Prerequisites:** state-space models $x_{t+1}=Ax_t+Bu_t$; expectation and gradients; least squares; the Bellman/dynamic-programming idea; eigenvalues and stability of a linear system; basic stochastic gradient descent.
