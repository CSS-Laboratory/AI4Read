---
id: prince-2023-udl/ch13-graph
work: prince-2023-udl
unit: "Chapter 13 — Graph neural networks"
pages: 240–268
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Graph neural networks

## L0 — One line
Because node order in a graph is arbitrary, each layer of a graph neural network must be permutation-equivariant; a layer that updates every node from its neighbours with shared parameters satisfies this, and the same network body serves graph-, node- and edge-level tasks.

## L1 — The gist (≤ 120 words)
Graph neural networks (GNNs) process graphs. These have variable topology, can be huge, and may exist as a single graph, and their node order is arbitrary. The chapter asks how to build layers that cope with these difficulties. A graph is encoded by an adjacency matrix $\mathbf{A}$ and node embeddings $\mathbf{X}$. Graph convolutional layers update each node from its neighbours with shared weights, and the example layer is equivariant to reordering of nodes. Graph-level tasks pool the node embeddings; node tasks use each embedding and edge tasks combine two. A single large graph (the transductive setting) can be batched by neighbourhood sampling or graph partitioning. This matters because social networks, molecules and citation networks are graphs.

**Prerequisites:** matrix–vector products; sigmoid and binary cross-entropy; convolution and receptive field (ch. 10); self-attention (ch. 12); SGD and mini-batches.

## L2 — Key ideas
- A graph is encoded by $\mathbf{A}$ ($N\times N$), $\mathbf{X}$ ($D\times N$) and optionally $\mathbf{E}$ ($D_E\times E$); powers $\mathbf{A}^L$ count walks of length $L$ (pp. 243–245).
- Node indexing is arbitrary, so layers must be equivariant to permutations (permuting the input node indices permutes the output columns in the same way): $\mathbf{H}_{k+1}\mathbf{P}=\mathbf{F}[\mathbf{H}_k\mathbf{P},\mathbf{P}^T\mathbf{A}\mathbf{P},\phi_k]$. Graph-level outputs must be invariant (unchanged by node order) (pp. 245, 249).
- Tasks are graph-level (pool node embeddings), node-level (classify each node) or edge prediction (combine two node embeddings, e.g. dot product) (pp. 246–248).
- The basic GCN layer sums neighbour embeddings, transforms them and the current node with shared weights, and applies a nonlinearity: $\mathbf{H}_{k+1}=\mathbf{a}[\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{A}+\mathbf{I})]$ (pp. 249–251).
- Batches of small graphs are treated as disjoint parts of one big graph, with mean pooling done per graph (p. 252).
- Inductive problems learn a rule from many labelled graphs. Transductive problems label the unknown nodes of one partly labelled graph (pp. 252–253).
- With many layers and a densely connected graph, a batch may not shrink at all (the graph expansion problem). Neighbourhood sampling and graph partitioning tackle it (pp. 254–256).
- Layer variants change how the current node and neighbours are combined and how neighbours are aggregated (mean, Kipf normalisation by neighbour counts, max, attention). Edge embeddings are handled via the edge graph (pp. 257–261).

## L3 — Walkthrough

### Introduction (p. 240)
CNNs handle regular arrays and transformers handle variable-length sequences. GNNs handle graphs, which raise three challenges (p. 240):
1. The topology varies, so it is hard to design a network that is both sufficiently expressive and able to cope with that variation.
2. Graphs may be enormous (a social network may have a billion nodes).
3. There may be only one monolithic graph, so the usual train-on-many/test-on-new protocol does not always fit.

### 13.1 What is a graph? (pp. 240–243)
A graph is a set of nodes (vertices) with pairs joined by edges (links). Graphs are typically sparse: only a small subset of possible edges is present (p. 240).
- Natural graphs: road networks, molecules (atoms and bonds), electrical circuits (p. 240).
- Datasets that can be graphs: social networks (people, friendships), literature (papers, citations), Wikipedia (articles, hyperlinks), programs (syntax tokens), point clouds (nodes linked to nearby points), protein interactions (p. 241).
- A set can be treated as a graph in which every member connects to every other. An image can be treated as a graph with regular topology: each pixel links to adjacent pixels (p. 241).

**13.1.1 Types of graphs.**
- Undirected edges are symmetric (friendship). Directed edges are one-way (citation) (p. 241).
- A knowledge graph is a directed heterogeneous multigraph. Heterogeneous: nodes are of different entity types. Multigraph: several edges of different types may join two nodes (p. 241).
- A point set becomes a geometric graph by linking each point to its $K$ nearest neighbours, each node carrying a 3D position (p. 243).
- A hierarchical graph has graphs (room, table, light) as nodes of a larger graph (p. 243).
- All types can be processed with deep learning; this chapter focuses on undirected graphs (p. 243).

### 13.2 Graph representation (pp. 243–245)
Information attached to nodes is a node embedding; information on edges is an edge embedding (p. 243). A graph with $N$ nodes and $E$ edges is encoded by three matrices (p. 243–244):
- Adjacency matrix $\mathbf{A}$, $N\times N$: entry $(m,n)$ is 1 if nodes $m,n$ are joined, else 0. It is always symmetric for undirected graphs. Large sparse graphs can be stored as a list of connections (p. 244).
- Node data $\mathbf{X}$, $D\times N$: columns are embeddings $\mathbf{x}^{(n)}$ of length $D$ (p. 244).
- Edge data $\mathbf{E}$, $D_E\times E$: columns are edge embeddings $\mathbf{e}^{(e)}$ (p. 244).

Edge embeddings are set aside until section 13.9 (p. 244).

**13.2.1 Properties of the adjacency matrix.** A one-hot column vector is all zeros except a 1 at position $n$. Pre-multiplying it by $\mathbf{A}$ extracts column $n$: ones at the neighbours of node $n$. Pre-multiplying again gives the number of walks of length two from $n$ to every node (pp. 244–245). In general, entry $(m,n)$ of $\mathbf{A}^L$ is the number of unique walks of length $L$ from $m$ to $n$. This is not the number of paths, since walks may revisit nodes. A non-zero entry still indicates that the distance from $m$ to $n$ must be at most $L$ (p. 245). Figure 13.4 shows an eight-node example: from node six one can reach nodes five, seven and eight in one move, and return to node six in two moves in three ways (p. 244).

*Intuition note:* Multiplying by $\mathbf{A}$ means "collect from my neighbours". Repeating it spreads information one hop further each time, which is why stacked layers see farther.

**13.2.2 Permutation of node indices.** Node indexing is arbitrary. Permuting the indices permutes the columns of $\mathbf{X}$ and both rows and columns of $\mathbf{A}$, but the graph is unchanged. This differs from images or text, where permuting pixels or words changes the object (p. 245). A permutation matrix $\mathbf{P}$ has exactly one 1 in each row and column. If entry $(m,n)$ is 1, node $m$ becomes node $n$. The re-indexed data are

$$\mathbf{X}'=\mathbf{X}\mathbf{P},\qquad \mathbf{A}'=\mathbf{P}^T\mathbf{A}\mathbf{P}.\tag{13.1}$$

Post-multiplying by $\mathbf{P}$ permutes columns. Pre-multiplying by $\mathbf{P}^T$ permutes rows. Any processing of the graph should be indifferent to these permutations, otherwise results depend on the arbitrary indexing (p. 245).

### 13.3 Graph neural networks, tasks, and loss functions (pp. 245–248)
A GNN takes $\mathbf{X}$ and $\mathbf{A}$ and passes them through $K$ layers. The embeddings are updated into hidden representations $\mathbf{H}_k$ and finally output embeddings $\mathbf{H}_K$. At the input each column describes only its node. At the output each column includes the node and its context in the graph. The author compares this to word embeddings becoming contextual meanings in a transformer (p. 245).

**13.3.1 Tasks and loss functions.** Supervised graph problems usually fall into three categories (p. 246).

*Graph-level tasks.* The network labels or estimates values for the whole graph, e.g. a molecule's liquid temperature (regression) or toxicity (classification). Output node embeddings are combined (e.g. averaged) and mapped by a linear map or network to a fixed-size vector. Regression uses least squares. Binary classification uses a sigmoid and binary cross-entropy:

$$Pr(y=1|\mathbf{X},\mathbf{A})=\mathrm{sig}\left[\beta_K+\boldsymbol{\omega}_K\mathbf{H}_K\mathbf{1}/N\right]\tag{13.2}$$

Here $\beta_K$ is a scalar and $\boldsymbol{\omega}_K$ is a $1\times D$ learned vector. Multiplying $\mathbf{H}_K$ by the ones vector $\mathbf{1}$ sums the embeddings. Dividing by $N$ gives the average: mean pooling (p. 246). For multi-class output, figure 13.6a uses a softmax (p. 247).

*Node-level tasks.* Each node gets a label or values, e.g. wing versus fuselage for a point-cloud graph. Losses are as above, applied independently at each node (p. 248):

$$Pr(y^{(n)}=1|\mathbf{X},\mathbf{A})=\mathrm{sig}\left[\beta_K+\boldsymbol{\omega}_K\mathbf{h}_K^{(n)}\right]\tag{13.3}$$

*Edge prediction.* This is binary classification of whether an edge should exist between nodes $m$ and $n$. One possibility is a dot product of the two embeddings through a sigmoid (p. 248):

$$Pr(y^{(mn)}=1|\mathbf{X},\mathbf{A})=\mathrm{sig}\left[\mathbf{h}^{(m)T}\mathbf{h}^{(n)}\right]\tag{13.4}$$

### 13.4 Graph convolutional networks (pp. 248–251)
The chapter focuses on spatial-based convolutional GNNs (GCNs). They are convolutional because each node is updated by aggregating information from nearby nodes. This induces a relational inductive bias (prioritising neighbours' information). They are spatial because they use the original graph, unlike spectral methods, which convolve in the Fourier domain (p. 248). Each layer is a function $\mathbf{F}[\bullet]$ with parameters $\phi_k$:

$$\mathbf{H}_1=\mathbf{F}[\mathbf{X},\mathbf{A},\phi_0],\ \ \mathbf{H}_2=\mathbf{F}[\mathbf{H}_1,\mathbf{A},\phi_1],\ \dots,\ \mathbf{H}_K=\mathbf{F}[\mathbf{H}_{K-1},\mathbf{A},\phi_{K-1}]\tag{13.5}$$

**13.4.1 Equivariance and invariance.** Each layer must be equivariant to permutations: if the node indices are permuted, the embeddings at each stage are permuted in the same way (p. 249):

$$\mathbf{H}_{k+1}\mathbf{P}=\mathbf{F}[\mathbf{H}_k\mathbf{P},\mathbf{P}^T\mathbf{A}\mathbf{P},\phi_k]\tag{13.6}$$

For node classification and edge prediction the output should also be equivariant. For graph-level tasks the final layer aggregates over the graph, so the output is invariant. The output layer of eq. 13.2 achieves this (p. 249):

$$y=\mathrm{sig}[\beta_K+\boldsymbol{\omega}_K\mathbf{H}_K\mathbf{1}/N]=\mathrm{sig}[\beta_K+\boldsymbol{\omega}_K\mathbf{H}_K\mathbf{P}\mathbf{1}/N]\tag{13.7}$$

For images, conv and pooling layers only partially achieve equivariance to translation and there is no known way to guarantee these properties exactly for more general transformations. For graphs, networks can be defined that ensure equivariance or invariance to permutations (p. 249).

**13.4.2 Parameter sharing.** A model with separate parameters per node would need to learn the meaning of connections at each position, and training would require many graphs with the same topology. Instead the same parameters are used at every node, as with convolution. A convolution can be seen as neighbours sending messages that the node aggregates. In a graph, each node may have a different number of neighbours and there are no consistent spatial relationships (nothing is "above" or "below"), so neighbours cannot be weighted by position (pp. 249–250).

**13.4.3 Example GCN layer** (figure 13.7). Aggregate neighbours by summing, then transform the current node and the aggregate with the same $\Omega_k$ (p. 250):

$$\mathbf{agg}[n,k]=\sum_{m\in\mathrm{ne}[n]}\mathbf{h}_k^{(m)}\tag{13.8}$$
$$\mathbf{h}_{k+1}^{(n)}=\mathbf{a}\left[\boldsymbol{\beta}_k+\Omega_k\cdot\mathbf{h}_k^{(n)}+\Omega_k\cdot\mathbf{agg}[n,k]\right]\tag{13.9}$$

Post-multiplying $\mathbf{H}_k$ ($D\times N$) by $\mathbf{A}$ gives $\mathbf{agg}[n,k]$ as column $n$. With $\mathbf{1}$ an $N\times1$ ones vector (p. 251):

$$\mathbf{H}_{k+1}=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k+\Omega_k\mathbf{H}_k\mathbf{A}\right]=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{A}+\mathbf{I})\right]\tag{13.10}$$

The author says this layer is equivariant to permutations, copes with any number of neighbours, gives a relational inductive bias and shares parameters across the graph (p. 251).

*Intuition note:* Each node adds its own embedding to the sum of its neighbours', then applies one weight matrix. Reordering the nodes only reorders the columns of the result, because the same operation is applied everywhere.

### 13.5 Example: graph classification (pp. 251–252)
Task: classify molecules as toxic or harmless. $\mathbf{A}\in\mathbb{R}^{N\times N}$ comes from the molecular structure. Columns of $\mathbf{X}\in\mathbb{R}^{118\times N}$ are one-hot vectors over the 118 elements. $\Omega_0\in\mathbb{R}^{D\times118}$ maps them to size $D$ (p. 251).

$$\mathbf{H}_1=\mathbf{a}[\boldsymbol\beta_0\mathbf{1}^T+\Omega_0\mathbf{X}(\mathbf{A}+\mathbf{I})],\ \ \mathbf{H}_2=\mathbf{a}[\boldsymbol\beta_1\mathbf{1}^T+\Omega_1\mathbf{H}_1(\mathbf{A}+\mathbf{I})],\ \dots$$
$$\mathbf{H}_K=\mathbf{a}[\boldsymbol\beta_{K-1}\mathbf{1}^T+\Omega_{K-1}\mathbf{H}_{K-1}(\mathbf{A}+\mathbf{I})],\qquad \mathrm{f}[\mathbf{X},\mathbf{A},\Phi]=\mathrm{sig}[\beta_K+\boldsymbol\omega_K\mathbf{H}_K\mathbf{1}/N]\tag{13.11}$$

**13.5.1 Training with batches.** Given $I$ graphs $\{\mathbf{X}_i,\mathbf{A}_i\}$ with labels $y_i$, the parameters $\Phi=\{\boldsymbol\beta_k,\Omega_k\}_{k=0}^K$ are learned by SGD with binary cross-entropy (p. 251). Each graph may have a different number of nodes, so $\mathbf{X}_i$ and $\mathbf{A}_i$ differ in size and cannot be concatenated into 3D tensors. The trick is to treat the batch as disjoint components of one large graph and run the network once. Mean pooling is done only within each graph, giving one representation per graph for the loss (p. 252).

### 13.6 Inductive vs. transductive models (pp. 252–253)
- Inductive models use labelled training data to learn a rule from inputs to outputs and apply it to new data (all models earlier in the book) (p. 252).
- A transductive model considers labelled and unlabelled data together. It produces a labelling of the unknowns, not a rule. This is sometimes called semi-supervised learning. Advantage: it can use patterns in the unlabelled data. Disadvantage: it must be retrained when more unlabelled data are added (p. 253).
- Both occur for graphs. Many labelled molecules give an inductive problem. One citation graph with field labels on some papers gives a transductive one, where training and test data are "irrevocably connected" (p. 253).
- Graph-level tasks occur only in the inductive setting. Node-level and edge tasks can occur in either. In the transductive case the loss compares output and truth only where truth is known. Predictions at unknown nodes come from the forward pass (p. 253).

### 13.7 Example: node classification (pp. 253–256)
A binary node classification task in a transductive setting, on a graph with millions of nodes. The body is as in eq. 13.11, with the final layer producing a $1\times N$ vector (p. 253):

$$\mathrm{f}[\mathbf{X},\mathbf{A},\Phi]=\mathrm{sig}\left[\beta_K\mathbf{1}^T+\boldsymbol\omega_K\mathbf{H}_K\right]\tag{13.12}$$

This is a vectorised version of eq. 13.3. Binary cross-entropy is applied only at labelled nodes (p. 253). Two problems arise:
1. Storing embeddings at every layer needs several times the graph's size, which may be impractical.
2. With one graph, forming SGD batches is not obvious (p. 253).

**13.7.1 Choosing batches.** Choose a random subset of labelled nodes per step. Each node depends on its neighbours in the previous layer, and so on, so each node has a receptive field, called its $k$-hop neighbourhood (figure 13.9). A step can use the union of the $k$-hop neighbourhoods of the batch nodes (p. 254). With many layers and a densely connected graph, every input node may lie in the receptive field of every output, so the graph may not shrink at all. This is the graph expansion problem (p. 254).

- **Neighbourhood sampling:** work back from the batch nodes, randomly sampling a fixed number of neighbours in the previous layer, then of their neighbours, and so on. The graph still grows with each layer, but in a more controlled way. Sampling is redone for each batch, which is reminiscent of dropout and adds some regularisation (p. 254).
- **Graph partitioning:** cluster the graph into disjoint subgraphs using standard algorithms that maximise internal links. Subgraphs can each be a batch, or random combinations can be joined, reinstating the original edges between them (figure 13.11) (pp. 254–256).

With either method, the labelled nodes can be split into train, test and validation sets, so the transductive problem is effectively converted to an inductive one. Inference computes predictions from the $k$-hop neighbourhood. It needs no stored intermediate representations, so it is much more memory-efficient (p. 256).

*Intuition note:* A node's output depends only on its $k$-hop neighbourhood, so one can train on pieces of the graph. Sampling or partitioning keeps those pieces small enough for memory.

### 13.8 Layers for graph convolutional networks (pp. 256–260)
Two design choices vary: (i) how the current embedding is combined with the aggregated neighbours, and (ii) how neighbours are aggregated (p. 256).

**13.8.1 Combining current node and neighbours.** The basic layer is $\mathbf{H}_{k+1}=\mathbf{a}[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{A}+\mathbf{I})]$ (13.13). *Diagonal enhancement* multiplies the current node by $(1+\epsilon_k)$, with $\epsilon_k$ a learned scalar per layer (p. 257):

$$\mathbf{H}_{k+1}=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{A}+(1+\epsilon_k)\mathbf{I})\right]\tag{13.14}$$

A related variant uses a separate linear transform $\Psi_k$ for the current node (p. 257):

$$\mathbf{H}_{k+1}=\mathbf{a}[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k\mathbf{A}+\Psi_k\mathbf{H}_k]=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\begin{bmatrix}\Omega_k&\Psi_k\end{bmatrix}\begin{bmatrix}\mathbf{H}_k\mathbf{A}\\\mathbf{H}_k\end{bmatrix}\right]=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k'\begin{bmatrix}\mathbf{H}_k\mathbf{A}\\\mathbf{H}_k\end{bmatrix}\right]\tag{13.15}$$

with $\Omega_k'=\begin{bmatrix}\Omega_k&\Psi_k\end{bmatrix}$.

**13.8.2 Residual connections.** The aggregated neighbour representation is transformed and passed through the activation before being summed or concatenated with the current node. For concatenation (p. 257):

$$\mathbf{H}_{k+1}=\begin{bmatrix}\mathbf{a}[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k\mathbf{A}]\\\mathbf{H}_k\end{bmatrix}\tag{13.16}$$

**13.8.3 Mean aggregation.** Averaging neighbours instead of summing may be superior if embedding information matters more than structural information, since the magnitude of the neighbour contribution then does not depend on the number of neighbours (p. 257):

$$\mathbf{agg}[n]=\frac{1}{|\mathrm{ne}[n]|}\sum_{m\in\mathrm{ne}[n]}\mathbf{h}_m\tag{13.17}$$

With the diagonal $N\times N$ degree matrix $\mathbf{D}$ (entries are neighbour counts; $\mathbf{D}^{-1}$ holds the denominators) (p. 258):

$$\mathbf{H}_{k+1}=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{A}\mathbf{D}^{-1}+\mathbf{I})\right]\tag{13.18}$$

**13.8.4 Kipf normalization.** Normalises the neighbour sum by both nodes' neighbour counts, with the author's stated logic that information from nodes with very many neighbours should be down-weighted because there are many connections and it is less unique (p. 258):

$$\mathbf{agg}[n]=\sum_{m\in\mathrm{ne}[n]}\frac{\mathbf{h}_m}{\sqrt{|\mathrm{ne}[n]||\mathrm{ne}[m]|}}\tag{13.19}$$
$$\mathbf{H}_{k+1}=\mathbf{a}\left[\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k(\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}+\mathbf{I})\right]\tag{13.20}$$

**13.8.5 Max pooling aggregation.** Also permutation-invariant (p. 258):

$$\mathbf{agg}[n]=\max_{m\in\mathrm{ne}[n]}[\mathbf{h}_m]\tag{13.21}$$

where max is element-wise over the neighbour vectors.

**13.8.6 Aggregation by attention.** In graph attention layers the weights depend on the node data (pp. 258–260). First a linear transform:

$$\mathbf{H}_k'=\boldsymbol\beta_k\mathbf{1}^T+\Omega_k\mathbf{H}_k\tag{13.22}$$

Similarity of node $m$ to node $n$ concatenates the pair, takes a dot product with learned vector $\boldsymbol\phi_k$, and applies an activation:

$$s_{mn}=\mathbf{a}\left[\boldsymbol\phi_k^T\begin{bmatrix}\mathbf{h}_m'\\\mathbf{h}_n'\end{bmatrix}\right]\tag{13.23}$$

These fill an $N\times N$ matrix $\mathbf{S}$. As in dot-product self-attention, softmax makes the weights positive and sum to one, but only the node itself and its neighbours contribute (p. 260):

$$\mathbf{H}_{k+1}=\mathbf{a}\left[\mathbf{H}_k'\cdot\mathrm{Softmask}[\mathbf{S},\mathbf{A}+\mathbf{I}]\right]\tag{13.24}$$

Softmask applies softmax to each column of $\mathbf{S}$ after setting entries where $\mathbf{A}+\mathbf{I}$ is zero to negative infinity, so attention to non-neighbours is zero (p. 260). Versus transformer self-attention: (i) keys, queries and values are the same, (ii) the similarity measure differs, (iii) attention is masked to the node and its neighbours. Multiple heads can be used (p. 260; figure 13.12, p. 259).

*Intuition note:* A plain GCN weights neighbours by graph structure alone. Dot-product attention weights by data alone. Graph attention uses both: the data decide the weights, but the graph decides who may be attended to.

### 13.9 Edge graphs (pp. 260–261)
To process edge embeddings, use the edge graph (also called adjoint or line graph). Each original edge becomes a node, and two edges sharing a node in the original graph become connected nodes (figure 13.13). In general a graph can be recovered from its edge graph, so the two representations are interchangeable (p. 260). Then the same techniques apply. When both node and edge embeddings exist, one can translate back and forth. Four updates are possible (nodes→nodes, nodes→edges, edges→nodes, edges→edges), alternated as desired or, with minor modifications, nodes can be updated from both at once (pp. 260–261).

### 13.10 Summary (p. 261)
Graphs have nodes and edges with embeddings. Node order is arbitrary, so layers must be equivariant. Spatial GCNs aggregate neighbours to update nodes. The transductive setting with one large partly labelled graph motivates sampling and partitioning algorithms. The edge graph lets GNNs update edge embeddings (p. 261).

### Notes (pp. 262–266; other authors' work, compressed)
- **Early GNNs.** Gori et al. (2005) and Scarselli et al. (2008) introduced GNNs as a generalisation of recursive neural networks, with the iterative update $\mathbf{h}_n\leftarrow\mathbf{f}[\mathbf{x}_n,\mathbf{x}_{m\in\mathrm{ne}[n]},\mathbf{e}_{e\in\mathrm{nee}[n]},\mathbf{h}_{m\in\mathrm{ne}[n]},\phi]$ (13.25). For convergence $\mathbf{f}$ must be a contraction mapping. Unrolled for $K$ steps with different $\phi_k$ it becomes similar to a GCN (p. 262).
- **Spectral vs. spatial.** Bruna et al. (2013) applied convolution in the Fourier domain, using eigenvectors of the graph Laplacian $\mathbf{L}=\mathbf{D}-\mathbf{A}$. Disadvantages: filters are not localised and the decomposition is prohibitively expensive for large graphs. Kipf & Welling (2017) used 1-hop filters, bridging spectral and spatial methods (p. 262). Spectral methods rest on the Laplacian, so a changed graph requires retraining, which spurred spatial methods (p. 262).
- **Power.** Xu et al. (2019) argue a GNN should distinguish different graph structures. They show structures that GCN and GraphSAGE cannot distinguish. Their graph isomorphism network has the same discriminative power as the Weisfeiler–Lehman test, with aggregation $\mathbf{h}_{k+1}^{(n)}=\mathrm{mlp}[(1+\epsilon_k)\mathbf{h}_k^{(n)}+\sum_{m\in\mathrm{ne}[n]}\mathbf{h}_k^{(m)}]$ (13.26) (p. 264).
- **Batching.** Kipf & Welling used full-batch gradient descent. Later methods fall into node sampling (GraphSAGE, PinSAGE), layer sampling (FastGCN etc.) and subgraph sampling (GraphSAINT, Cluster GCN) (p. 264).
- **Regularisation.** DropEdge randomly drops edges, similar to dropout but also like augmentation (p. 265).
- **Depth.** GCNs did not, until recently, benefit much from depth. Proposed causes are over-smoothing, an information bottleneck (Alon & Yahav) and "suspended animation" (gradients no longer propagate). Xu et al. prove that one node's influence on another is proportional to the probability of reaching it in a $K$-step random walk, which approaches the stationary distribution as $K$ grows. Residual connections now allow deeper networks, up to over 1000 layers in Li et al. (2021a) using an invertible network (pp. 265–266).
- **Other topics listed:** pooling (DiffPool), multi-relational graphs, geometric graphs (MoNet), higher-order convolutions, and Graph-BERT, which uses position embeddings such as hop distance instead of adjacency (pp. 263, 265).

## Toy example (ours, not from the text)
Path graph with 3 nodes, edges 1–2 and 2–3. Scalar embeddings ($D=1$): $\mathbf{X}=[1\ 2\ 3]$. Take $\Omega=1$, $\beta=0$, ReLU.

$\mathbf{A}=\begin{bmatrix}0&1&0\\1&0&1\\0&1&0\end{bmatrix}$, so $\mathbf{A}+\mathbf{I}=\begin{bmatrix}1&1&0\\1&1&1\\0&1&1\end{bmatrix}$.

$\mathbf{X}(\mathbf{A}+\mathbf{I})$ is the row vector times the matrix:
- column 1: $1\cdot1+2\cdot1+3\cdot0=3$
- column 2: $1+2+3=6$
- column 3: $1\cdot0+2\cdot1+3\cdot1=5$

So $\mathbf{H}_1=\mathrm{ReLU}[3,6,5]=[3,6,5]$. Each node's new value is its own value plus its neighbours' values: node 1 gets $1+2$, node 2 gets $1+2+3$, node 3 gets $2+3$.

Equivariance check: swap nodes 1 and 3. Then $\mathbf{X}'=[3,2,1]$ and $\mathbf{A}'=\mathbf{A}$ (this path is symmetric under the swap). $\mathbf{X}'(\mathbf{A}+\mathbf{I})$: column 1 $=3+2=5$; column 2 $=3+2+1=6$; column 3 $=2+1=3$. Result $[5,6,3]$, which is $[3,6,5]$ with columns 1 and 3 swapped, as eq. 13.6 requires.

Invariance check: mean pooling gives $(3+6+5)/3=14/3$ before the swap and $(5+6+3)/3=14/3$ after, so a graph-level output (eq. 13.7) does not depend on node order.

## Concepts
- [[graph-neural-network]] (new) — model taking node embeddings $\mathbf{X}$ and adjacency $\mathbf{A}$ through $K$ layers (p. 245)
- [[adjacency-matrix]] (new) — $N\times N$ binary matrix of edges; $\mathbf{A}^L$ counts walks of length $L$ (pp. 244–245)
- [[permutation-equivariance]] (new) — permuting node indices permutes layer outputs identically; graph-level outputs must be invariant (pp. 245, 249)
- [[graph-convolutional-network]] (new) — spatial GNN that updates each node by aggregating neighbours with shared parameters (p. 248)
- [[message-aggregation]] (new) — sum, mean, Kipf-normalised, max or attention-weighted combination of neighbours (pp. 250, 257–258)
- [[mean-pooling]] (new) — averaging output node embeddings into one graph vector (p. 246)
- [[transductive-learning]] (new) — labelling unknown nodes of one partly labelled graph; no reusable rule (pp. 252–253)
- [[receptive-field-graph]] (new) — the $k$-hop neighbourhood that influences a node's output (p. 254)
- [[neighborhood-sampling]] (new) — sampling a fixed number of neighbours per layer to limit the graph per batch (p. 254)
- [[graph-partitioning]] (new) — splitting a graph into subgraphs, used as batches (p. 254)
- [[edge-graph]] (new) — graph with a node per original edge, linked when edges share a node (p. 260)
- [[graph-attention-network]] (new) — GNN whose neighbour weights come from node data, masked by $\mathbf{A}+\mathbf{I}$ (p. 260)
- [[attention]] — here, weights over neighbours via softmax, masked to the node's neighbourhood (p. 260)
- [[self-attention]] — transformer analogue; in graph attention keys, queries and values are identical (p. 260)
- [[softmax]] — normalises attention scores over neighbours (p. 260)

## Canonical instances
- [[molecule-toxicity-classification]] — graph-level binary task with one-hot atom-type embeddings (p. 251)
- [[citation-graph-node-labelling]] — transductive node classification of paper fields (p. 253)
- [[social-network-edge-prediction]] — predicting whether two people know and like each other, to suggest they connect (p. 248)
- [[point-cloud-graph]] — airplane points linked by $K$ nearest neighbours; wing versus fuselage nodes (pp. 243, 248)
- [[knowledge-graph]] — directed heterogeneous multigraph (p. 241)

## Bridges (candidates)
- [structural-analogy] GCN layer ↔ CNN convolution (ch. 10): same weights at every position, neighbours send messages, but no fixed spatial layout.
- [structural-analogy] Graph attention ↔ transformer self-attention: both give softmax-weighted sums of transformed inputs. The graph version masks to the adjacency pattern.
- [structural-analogy] Neighbourhood sampling ↔ dropout: the author calls it "reminiscent of dropout" (p. 254).
- [metaphor] Node classification on a social network ↔ social-science inference of unobserved attributes from observed ties: an unlabelled person is labelled using their connected neighbours.

## Questions this raises
- Sum, mean and max aggregation treat neighbours differently. Which structural facts about a graph does each lose, and when does that matter?
- Why do deeper GNNs often not improve, given the competing explanations in the Notes (over-smoothing, bottleneck, suspended animation)?
- How should transductive models be evaluated fairly when training and test nodes share one graph?
- Could attention over a complete graph reproduce a transformer, and what then does the adjacency mask add?

## Exercises worth doing
- Ex. 13.3 (p. 266) — count the walks of three and seven steps between two nodes (cf. section 13.2.1) — difficulty: medium
- Ex. 13.4 (p. 266) — explain why the diagonal of $\mathbf{A}^2$ gives each node's edge count — difficulty: easy
- Ex. 13.6 (p. 266) — prove mean-pooled output is invariant to permutation (eq. 13.27) — difficulty: easy
- Ex. 13.7 (pp. 266–267) — prove a simple GNN layer is permutation-equivariant (eq. 13.29) — difficulty: medium
- Ex. 13.9 (p. 267) — compute the GraphSAGE mean aggregation in matrix form using $\mathbf{A}$ and $\mathbf{D}$ — difficulty: medium
- Ex. 13.13 (p. 268) — relate the adjacency matrix of a graph to that of its edge graph — difficulty: hard

## Reading notes
- Printed page = pdf − 14 (pdf 254 = printed 240). Printed numbers are visible on the page labels.
- Pages carry the running footer "Draft: please send errata to udlbookmail@gmail.com." and the CC-BY-NC-ND / MIT Press line. This suggests a draft-version text.
- In eq. 13.11 the last body line prints $\mathbf{H}_{k-1}$ with lowercase $k$. It presumably means $\mathbf{H}_{K-1}$ (as in eq. 13.5). In the text of 13.4 the parameters are written both $\Phi$ and $\phi_k$.
- Figure 13.4 is the eight-node example. Its caption says nodes five, seven and eight are reachable in one move from node six. The image text of the $\mathbf{A}$ rows is small, so I did not re-derive the matrices.
- Problems 13.1–13.14 (pp. 266–268) are listed without solutions in these pages. Problem figures 13.14–13.15 were not analysed.
- The chapter's Notes section (pp. 262–266) is summarised only at headline level. Most claims there are citations of other authors' work.
