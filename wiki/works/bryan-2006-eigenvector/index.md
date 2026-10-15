---
id: bryan-2006-eigenvector/index
work: bryan-2006-eigenvector
type: work-map
units: [bryan-2006-eigenvector/main]
generated: deterministic
---

# Bryan, K., & Leise, T. (2006). The $25,000,000,000 eigenvector: The linear algebra behind Google. *SIAM Review*, 48(3), 569–581. https://doi.org/10.1137/050623280

## One digest
This work has a single digest, which is also its work-level summary: [[bryan-2006-eigenvector/main]].

## In one line
PageRank scores are the unique positive, sum-one eigenvector (eigenvalue 1) of the column-stochastic matrix $M=(1-m)A+mS$ (for $0<m\le1$), and power iteration finds it.

## The gist
How can a search engine rate the importance of every web page? The authors let each page split one vote among its outgoing links, weighted by its own score. This gives the eigenvector problem $Ax=x$. The problem can fail: if the web splits into disconnected parts, the eigenspace has dimension above 1 and the ranking is not unique. Mixing $A$ with the all-$1/n$ matrix $S$ gives a positive matrix $M$ (for $m>0$). For positive column-stochastic matrices, the eigenspace for eigenvalue 1 has dimension exactly one and its vectors are strictly positive or strictly negative. Power iteration converges to this eigenvector geometrically, and each step is cheap because $A$ is sparse.

**Prerequisites:** eigenvalues and eigenvectors; linear independence, dimension and subspaces; matrix–vector multiplication; triangle inequality; vector norms; proof by contradiction. Terms used above: *column-stochastic* = all entries $\ge0$ and every column sums to 1; *positive matrix* = all entries $>0$; *eigenspace* = all eigenvectors for one eigenvalue (with 0); *power iteration* = repeatedly multiplying a start vector by the matrix; *sparse* = mostly zero entries; *1-norm* = sum of absolute values of the entries; *zero-sum subspace* = vectors whose entries sum to 0.
