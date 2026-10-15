---
id: eckart-1936-lowrank/index
work: eckart-1936-lowrank
type: work-map
units: [eckart-1936-lowrank/main]
generated: deterministic
---

# Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika*, 1(3), 211–218. https://doi.org/10.1007/BF02288367

## One digest
This work has a single digest, which is also its work-level summary: [[eckart-1936-lowrank/main]].

## In one line
The best rank-$r$ least-squares approximation of a matrix is found by writing it in canonic form (diagonal multipliers between two orthogonal matrices) and keeping only the $r$ largest multipliers.

## The gist
Factor theory assumes that an $n\times N$ score matrix can be approximated by a matrix of lower rank $r$. The paper asks which rank-$r$ matrix is closest to a given matrix, when closeness is the sum of squared element differences. The answer: write $\alpha=u'\lambda U$ with orthogonal $u,U$ and non-negative diagonal $\lambda$. Keep the $r$ largest diagonal entries and set the rest to zero. The squared error is then the sum of the squares of the discarded entries. The solution is unique unless $\lambda_r=\lambda_{r+1}$. The best rank-$r$ approximation $\beta$ also gives, through $\beta\beta'$ and $\beta'\beta$, the best rank-$r$ approximations to the two correlation matrices. In modern terms this is truncated-SVD low-rank approximation (canon link; the paper itself does not use that name).

**Prerequisites:** matrix transpose and product; orthogonal matrices ($uu'=1$); rank; diagonal matrices; symmetric and skew-symmetric matrices; minimising a function by setting its variation to zero.
