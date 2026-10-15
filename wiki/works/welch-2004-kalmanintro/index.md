---
id: welch-2004-kalmanintro/index
work: welch-2004-kalmanintro
type: work-map
units: [welch-2004-kalmanintro/main]
generated: deterministic
---

# Welch, G., & Bishop, G. (1995; updated 2004). *An Introduction to the Kalman Filter*. Technical Report TR 95-041, Department of Computer Science, University of North Carolina at Chapel Hill.

## One digest
This work has a single digest, which is also its work-level summary: [[welch-2004-kalmanintro/main]].

## In one line
The Kalman filter estimates a hidden state recursively by alternating a model-based prediction with a measurement correction weighted by the gain $K$, and the extended version handles nonlinear systems by linearizing.

## The gist
The paper asks how to estimate the state of a noisy process from noisy measurements without reprocessing all past data. The answer is a two-step cycle. A time update predicts the state and its error covariance. A measurement update corrects the prediction with the residual (measurement minus predicted measurement), weighted by a gain that balances prediction uncertainty against sensor noise. The extended Kalman filter (EKF) applies the same cycle to nonlinear systems by linearizing with Jacobians, at the price of being only approximate. A worked example estimates a constant voltage and shows how the assumed measurement noise $R$ tunes the filter. The filter has been the subject of extensive research and application, particularly in navigation.

**Prerequisites:** matrices and transposes; expectation, variance and covariance matrices; normal distribution; partial derivatives (Jacobian); the idea of a state vector.
