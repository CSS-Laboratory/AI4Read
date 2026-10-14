---
id: murphy-2023-pml2/ch30-graph
work: murphy-2023-pml2
unit: "30 Graph learning"
pages: 1043–1046
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Graph learning (Murphy, ch. 30 — introduction and overview)

## L0 — One line
Probability models can be used for graphs in two ways: explain a known graph with latent variables, or infer an unknown graph from data (structure learning), which is useful for understanding, prediction and causal inference.

## L1 — The gist (≤ 120 words)
The chapter asks how to model graphs probabilistically. In one setting the graph is known and we look for latent structure such as communities (stochastic block model). In the other the graph is unknown: from an N × D data matrix we learn a graph of a probabilistic graphical model (PGM). The printed pages only introduce this and defer methods to online supplementary material. They give three reasons for structure learning: understanding (protein interactions, bird brain wiring), prediction (stock covariance, traffic jams) and causal inference. For causal inference, learned DAGs (directed acyclic graphs) can be used to learn structural causal models (SCMs, directed graphical models with deterministic links except for random root variables), if we make assumptions about confounders. The unit is a map of the topic, not a full treatment.

**Prerequisites:** probabilistic graphical models (directed/undirected), latent variable models, Gaussian covariance, DAGs (directed acyclic graphs), the idea of a structural causal model and of confounders.

## L2 — Key ideas
- Two problems: explain a *known* graph with latent features (§30.2), or infer an *unknown* graph from correlated data (§30.3) (p. 1043).
- Latent variable generative models, e.g. the stochastic blocks model, are used to find clusters or communities in known graphs (p. 1043).
- Structure learning takes an N × D data matrix and returns a directed or undirected graph with N_G nodes; usually N_G = D, but extra latent nodes are possible (p. 1043).
- Understanding: graphical lasso (a method that learns a sparse undirected Gaussian graphical model; sparse = few edges) applied to flow cytometry data yields protein-interaction graphs whose sparsity is controlled by λ (p. 1044).
- Prediction: a learned sparse graph used in a trading strategy can outperform methods that do not exploit sparse graphs, and JamBayes predicts traffic with a directed model whose structure was learned (p. 1044).
- To predict the effects of interventions or to reason counterfactually, we need the structural causal model (SCM); learning DAGs can be a way to learn SCMs, if we make assumptions about (lack of) confounders. This is called causal discovery (p. 1045).
- Methods are not given here; they are in the online supplement (pp. 1043–1045).

## L3 — Walkthrough

### 30.1 Introduction (p. 1043)
Graphs are a common way to represent data, and the chapter covers probability models for them (p. 1043). There are two settings:
- Graph G known (§30.2): "explain" it with meaningful latent features, using latent variable models.
- Graph G unknown (§30.3): infer it from correlated data $x_n \in \mathbb{R}^D$, using probabilistic graphical models with unknown topology (p. 1043).

Graph neural networks, for supervised learning on graph data, are in Section 16.3.6, not here (p. 1043).

### 30.2 Latent variable models for graphs (p. 1043)
Graphs arise in social networks, protein–protein interaction networks and disease transmission patterns. To find "interesting structure" such as clusters or communities, it is common to fit latent variable generative models, such as the stochastic blocks model. Details are in online Supplementary Section 30.1; none are given in this unit (p. 1043).

*Intuition note:* Here the graph is given, and the aim is to explain it with meaningful hidden (latent) features, such as clusters or communities. "Generative" means the model describes how such a graph could be produced.

### 30.3 Graphical model structure learning (p. 1043)
- **Task.** Given sample observations of some or all nodes of a PGM, learn its structure. The input is an N × D data matrix. The output is a graph G (directed or undirected) with $N_G$ nodes. Usually $N_G = D$; the case of learned extra latent nodes is also considered (p. 1043).
- **30.3.1 Methods.** Many methods exist. The author points to a review [VCB22] and to Supplementary Chapter 30 (p. 1043).

### 30.3.2 Applications (pp. 1043–1045)
Three main reasons for structure learning: understanding, prediction, and causal inference (which involves both) (p. 1043).

**Understanding.** Learning sparse PGMs can be useful for gaining an understanding of multiple interacting variables (p. 1044).
- *Protein example.* Phosphorylation status of 11 proteins was measured by flow cytometry [Sac+05]. Graphical lasso (explained in Supplementary Section 30.4.2) produced a sparse undirected Gaussian graphical model. Sparsity is controlled by λ. Figure 30.1 shows λ = 36, 27, 7, 0 (p. 1044). In the figure (read from the image), the λ = 0 graph is nearly fully connected and the λ = 7 graph is denser than those for λ = 36 and 27.
- *Bird example.* [Smi+06] recovered the neural "wiring diagram" of a certain bird from multivariate EEG time series. The structure closely matched the known functional connectivity of that brain part (p. 1044).

**Prediction.** Sometimes the graph is only used for prediction, not interpreted (p. 1044).
- *Finance.* Accurate covariance models for many stocks matter. [CW07] show that learning a sparse graph and building a trading strategy on it can outperform methods that do not exploit sparse graphs (p. 1044).
- *Traffic.* [Hor+05] describe JamBayes, a deployed system for predicting Seattle-area traffic flow. It uses a directed graphical model whose structure was learned from data (p. 1044).

**Causal inference.** Structure learning is also an important pre-requisite for causal inference. To predict the effects of interventions, or to reason counterfactually, we need the structural causal model (SCM) (Section 4.7). An SCM is a directed graphical model whose node relationships are deterministic (functional), except for stochastic root (exogenous) variables. So DAG-learning techniques can be used to learn SCMs, if we make some assumptions about (lack of) confounders. This is called causal discovery (Supplementary Section 30.5) (p. 1045).

*Intuition note:* For prediction, the author says the graph may be used without being interpreted. Predicting the effect of an intervention needs the SCM, and learning it with DAG-learning methods requires assumptions about (lack of) confounders.

## Toy example (ours; not from the text)
Three variables $X_1, X_2, X_3$ are jointly Gaussian with precision matrix (inverse covariance)
$$\Theta=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}.$$
Background we add (not stated in this unit): in a Gaussian graphical model a zero precision entry means no edge. Here $\Theta_{13}=0$, so the graph is the chain $X_1 - X_2 - X_3$ with 2 edges.

- $\det\Theta = 2(4-1) - (-1)(-2-0) + 0 = 6-2 = 4$.
- Covariance $\Sigma=\Theta^{-1}=\begin{pmatrix}0.75&0.5&0.25\\0.5&1&0.5\\0.25&0.5&0.75\end{pmatrix}$.
- Check, first row of $\Sigma\Theta$: $0.75\cdot2+0.5\cdot(-1)=1$; $-0.75+1-0.25=0$; $-0.5+0.5=0$. ✓.
- The correlation of $X_1,X_3$ is $0.25/0.75=1/3\ne0$.

So the covariance is dense while the learned graph is sparse. A method like graphical lasso, given data from this model, would aim to recover the 2-edge graph. In Figure 30.1 the edge count likewise changes with λ.

## Concepts
- [[graph-structure-learning]] (new) — learn a graph (directed or undirected) from an N × D data matrix (p. 1043)
- [[stochastic-block-model]] (new) — latent variable generative model for finding clusters or communities in a known graph (p. 1043)
- [[graphical-lasso]] (new) — method that learns a sparse undirected Gaussian graphical model; sparsity set by λ (p. 1044)
- [[structural-causal-model]] — directed graphical model with deterministic relations except for stochastic exogenous roots (p. 1045)
- [[causal-discovery]] (new) — learning DAG structure as a way to learn SCMs, under assumptions about (lack of) confounders (p. 1045)

## Canonical instances
- [[flow-cytometry-protein-network]] — graphical lasso on phosphorylation data from 11 proteins, λ varied (p. 1044)
- [[bird-eeg-wiring-diagram]] — graph recovered from EEG matched known functional connectivity (p. 1044)
- [[sparse-graph-portfolio]] — sparse stock-covariance graph used in trading [CW07] (p. 1044)
- [[jambayes]] — deployed traffic predictor with learned directed structure (p. 1044)

## Bridges (candidates)
- [structural-analogy] λ controlling graph sparsity in graphical lasso ↔ regularization strength in shrinkage/penalized estimation — a single parameter trades fit against simplicity.
- [structural-analogy] stochastic block model's latent community labels ↔ hierarchical models: latent group-level structure explains observed data.
- [same-math] SCM as a DAG with functional links plus exogenous noise ↔ causal DAG/SCM concepts in the causal-inference field — same object (p. 1045).

## Questions this raises
- How does graphical lasso choose edges, and how should λ be chosen?
- Which confounder assumptions make DAG learning identify an SCM?
- How does structure learning change when latent nodes are added ($N_G > D$)?
- When does a graph that predicts well also have the right causal meaning?

## Reading notes
- Printed = pdf − 34. Pdf 1080 (printed 1046) is blank.
- Page 1044 carries the footer "Probabilistic Machine Learning: Advanced Topics. Online version. December 10, 2025". Page 1045 carries "Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license".
- Almost all substance is deferred to online supplementary sections (30.1, 30.4.2, 30.5, Chapter 30), which are not in these pages.
- "exogeneous" is spelled this way in the source (p. 1045).
- Figure 30.1 is small; node labels are tiny but legible, and I used the image only to judge edge density.
