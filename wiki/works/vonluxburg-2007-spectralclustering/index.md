---
id: vonluxburg-2007-spectralclustering/index
work: vonluxburg-2007-spectralclustering
type: work-map
units: [vonluxburg-2007-spectralclustering/main]
generated: deterministic
---

# von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing*, 17(4), 395–416. https://doi.org/10.1007/s11222-007-9033-z

## One digest
This work has a single digest, which is also its work-level summary: [[vonluxburg-2007-spectralclustering/main]].

## In one line
Spectral clustering re-represents data by the first k eigenvectors of a graph Laplacian and runs k-means there. It is explained in three ways: as a relaxed graph cut, as a random-walk statement, and as a perturbation of the ideal block-diagonal case.

## The gist
How can data with pairwise similarities be clustered, and why does an eigenvector-based method work? The tutorial builds a similarity graph, defines three graph Laplacians, and states three algorithms (unnormalized, Shi–Malik, Ng–Jordan–Weiss). It explains them in three ways: as relaxations of RatioCut and Ncut, as random walks that rarely switch clusters, and as perturbations of the ideal case with k connected components (Davis–Kahan). It then discusses practical choices. The author recommends the k-nearest-neighbour graph and the normalized $L_{\rm rw}$. The graph-cut relaxation carries no quality guarantee. The author says the method can be quite sensitive to graph parameters.

**Prerequisites:** eigenvalues/eigenvectors of symmetric matrices; positive semi-definiteness; Rayleigh quotient / trace minimization; basic probability (Markov chains); k-means.
