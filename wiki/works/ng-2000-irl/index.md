---
id: ng-2000-irl/index
work: ng-2000-irl
type: work-map
units: [ng-2000-irl/main]
generated: deterministic
---

# Ng, A. Y., & Russell, S. (2000). *Algorithms for Inverse Reinforcement Learning*. Proceedings of the 17th International Conference on Machine Learning (ICML 2000), 663–670.

## One digest
This work has a single digest, which is also its work-level summary: [[ng-2000-irl/main]].

## In one line
Observed optimal behaviour in a Markov decision process (a model of states, actions, random transitions and rewards) fits a whole set of reward functions, which in the finite case is described by linear inequalities; the paper suggests heuristics, solved by linear programming, to help choose among them.

## The gist
Inverse reinforcement learning (IRL) asks: if an agent is seen acting optimally in a Markov decision process (a model with states, actions, random transitions and rewards), which reward function is it optimizing? For finite state spaces, the paper describes all reward functions that make a given policy optimal, as linear inequalities. That set contains degenerate members such as R = 0, so the authors suggest heuristics: prefer rewards that make the observed policy better than single-step deviations, optionally penalizing large rewards. These can be written as linear programs (optimization with linear objective and linear constraints). Extensions cover large state spaces with linear basis functions and policies seen only through sampled trajectories. Simple experiments recover rewards that explain behaviour fairly well.

**Prerequisites:** Markov decision processes (states, actions, transition matrices, discount factor); value function and Bellman equation; vector/matrix notation; linear programming basics; Monte Carlo averaging.
