---
id: kalman-1960-filtering/index
work: kalman-1960-filtering
type: work-map
units: [kalman-1960-filtering/main]
generated: deterministic
---

# Kalman, R. E. (1960). *A New Approach to Linear Filtering and Prediction Problems*. Journal of Basic Engineering, 82(1), 35–45. https://doi.org/10.1115/1.3662552

## One digest
This work has a single digest, which is also its work-level summary: [[kalman-1960-filtering/main]].

## In one line
If a random signal is modelled as a linear state system driven by white gaussian noise, the optimal linear estimate is a recursive filter whose gain follows from a nonlinear difference equation for the error covariance, and this problem is the dual of the noise-free optimal regulator.

## The gist
Wiener's solution to estimating a random signal from noisy data was specified by an impulse response (its output after a single unit pulse). It was hard to synthesize or compute, and awkward for nonstationary or growing data. Kalman models the signal as a linear state system driven by white gaussian noise (independent random shocks). He then projects the unknown state orthogonally onto the observations. This gives a recursive linear filter. Its gain comes from a nonlinear difference equation for the error covariance (Theorem 3). The same equations, with time reversed and matrices transposed, solve the noise-free optimal regulator, a control problem with no randomness (Theorem 4). One derivation covers stationary, nonstationary, growing-memory and infinite-memory cases. It ties estimation to control.

**Prerequisites:** matrix algebra (transpose, inverse, positive definite); expectation, covariance, conditional expectation; vector spaces with an inner product (orthogonality, projection); difference equations; the gaussian distribution.
