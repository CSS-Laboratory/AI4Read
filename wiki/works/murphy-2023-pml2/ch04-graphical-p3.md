---
id: murphy-2023-pml2/ch04-graphical-p3
work: murphy-2023-pml2
unit: "4 Graphical models (part 3/3): §4.4.3.2 to §4.7.4"
pages: 194-218
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Graphical models, part 3: directed vs undirected, extensions, structural causal models

## L0 — One line
Directed and undirected graphical models represent different sets of conditional independences, can be converted into each other at a cost, and can be extended (factor graphs, relational and open-universe models, programs) and given a causal reading as structural causal models, which support intervention and counterfactual questions.

## L1 — The gist (≤ 120 words)
This part asks how directed (DPGM) and undirected (UPGM) graphical models compare. Neither is strictly more expressive. Each can be converted to the other, but the result may encode fewer independences. Conditional (discriminative) versions differ: locally normalized directed chains suffer "label bias", while globally normalized CRFs (undirected conditional models) do not. The text then extends the framework: factor graphs, probabilistic circuits, relational and open-universe models, and probabilistic programs. It ends with structural causal models. These model interventions with the do operator and graph surgery. They answer counterfactual questions by abduction, intervention and prediction. This matters because the same graphical language covers prediction, relational data and causal reasoning.

**Prerequisites:** conditional independence and d-separation; DAG and Markov random field (MRF) definitions and CRFs from earlier in the chapter; Gaussian precision matrices; basic first-order logic; conditional probability tables.

## L2 — Key ideas (5–10 bullets)
- DPGMs and UPGMs are perfect maps for different families of distributions. Only chordal (decomposable, tree-like) graphs are representable by both (pp. 194–195).
- A DPGM becomes a UPGM by moralization (linking parents that share a child) and dropping arrows. A UPGM becomes a DPGM by adding dummy child nodes fixed ("clamped") to an observed value. Both conversions are safe but may lose independences (p. 196–197).
- In the conditional setting, locally normalized directed models (MEMMs) block backward information flow (label bias). Globally normalized CRFs (undirected conditional models) avoid this, but need the full input before normalizing and are slower to train (p. 198).
- Factor graphs (bipartite or Forney) give a finer-grained, unifying representation of factorizations (pp. 202–205).
- Relational probability models and Markov logic networks are templates that are unrolled over objects. Open-universe models drop the fixed-object (closed-world) assumption; probabilistic programs define possible worlds as execution traces (pp. 206–212).
- A structural causal model is deterministic functions plus exogenous (external, unmodeled) noise, usually assumed independent. Its linear-Gaussian special case is the structural equation model (SEM) (pp. 212–214).
- Interventions are graph surgery, $p(\cdot|do(\cdot))$, or an augmented DAG with action nodes. In general $p(X|do(Z{=}z))\neq p(X|Z{=}z)$ (p. 215).
- Counterfactuals need abduction (inferring the hidden noise from what was seen), intervention and prediction, and strictly more assumptions than interventions. Potential outcomes (what would have happened under another action) and SCMs are mathematically equivalent, per the author (pp. 216–217).

## L3 — Walkthrough

### 4.4.3.2 General CRF (p. 194)
A CRF is $p(y|x;\theta)=\exp(f(x,y;\theta))/Z(x;\theta)$, where $Z(x;\theta)=\sum_{y'}\exp(f(x,y';\theta))$ and $f$ is a score (negative energy), high for probable configurations.
$$p(y|x;\theta)=\frac{\exp(f(x,y;\theta))}{Z(x;\theta)}=\frac{\exp(f(x,y;\theta))}{\sum_{y'}\exp(f(x,y';\theta))}\tag{4.147}$$
$$\nabla_\theta \ell(\theta)=\frac1N\sum_{n=1}^N\big[\nabla_\theta f(x_n,y_n;\theta)-\nabla_\theta\log Z(x_n;\theta)\big]\tag{4.148}$$
$\nabla\log Z$ is tractable if the needed expectations can be computed (Sec. 4.3.9.2). It must be computed for every training example. This is slower than for an MRF, where $\log Z$ is one constant independent of the observed data (p. 194).

### 4.4.4 Other structured-prediction approaches (p. 194)
Alternatives named: max-margin Markov networks and structural SVMs (non-probabilistic alternatives to CRFs), and structured prediction energy networks, which predict with $\hat y(x)=\arg\min_y \mathcal E(x,y)$. Graph neural networks and sequence-to-sequence transformers are also common (p. 194).

### 4.5 Comparing directed and undirected PGMs
**4.5.1 CI properties (pp. 194–195).**
- $G$ is an I-map of $p$ if $I(G)\subseteq I(p)$. $G$ is a **perfect map** if $I(G)=I(p)$: it represents all and only the CI properties (p. 194).
- DPGMs and UPGMs are perfect maps for different sets of distributions (Fig. 4.36). Neither is more powerful as a representation language (p. 194).
- **Directed but not undirected:** the v-structure $A\to C\leftarrow B$ asserts $A\perp B$ and $A\not\perp B|C$. Dropping arrows gives $A-C-B$, which asserts $A\perp B|C$ and $A\not\perp B$. No UPGM represents exactly the v-structure's two statements (pp. 194–195).
- UPGM CI is monotonic: if $A\perp B|C$ then $A\perp B|(C\cup D)$. DPGM CI can be non-monotonic, since extra conditioning can destroy independences through explaining away (p. 195).
- **Undirected but not directed:** the 4-cycle of Fig. 4.37(a) with $A\perp C|B,D$. Fig. 4.37(b) gets that right but wrongly asserts $B\perp D|A$. Fig. 4.37(c) also gets it right but wrongly asserts $B\perp D$. No DPGM works (p. 195).
- Distributions representable by both give decomposable (**chordal**) graphs. Roughly: collapsing each maximal clique into a "mega-variable" yields a tree. Trees and chains are already chordal (p. 195).

*Intuition note:* Directed graphs can say "independent, but dependent once the common child is seen." Undirected graphs can say "separated by a cut set", as in a 4-cycle. Neither language covers all of the other's patterns (only chordal cases overlap).

**4.5.2 Conversion (pp. 196–197).** Conversion is safe if the graph may encode fewer CI properties than hold (p. 196).
- *DPGM→UPGM (4.5.2.1):* **moralization** adds an edge between "unmarried" parents of a common child, then drops arrows. This keeps CI properties matched and gives a clique that can store each family's CPD (p. 196).
- Student network example:
$$P(C,D,I,G,S,L,J,H)=P(C)P(D|C)P(I)P(G|I,D)P(S|I)P(L|G)P(J|L,S)P(H|G,J)\tag{4.149–4.150}$$
One potential per CPD:
$$p=\psi_C(C)\psi_D(D,C)\psi_I(I)\psi_G(G,I,D)\psi_S(S,I)\psi_L(L,G)\psi_J(J,L,S)\psi_H(H,G,J)\tag{4.151–4.152}$$
The potentials are locally normalized (they are CPDs), so $Z=1$ (p. 196).
- Moralization edges added: D–I, G–J, L–S (Fig. 4.38) (p. 196). (added step) These come from the parent pairs $\{I,D\}$ of $G$, $\{L,S\}$ of $J$, and $\{G,J\}$ of $H$ in Eq. 4.150.
- *UPGM→DPGM (4.5.2.2):* for each potential $\psi_c(x_c;\theta_c)$ create a dummy node $Y_c$ clamped to $y_c^*$, with $p(Y_c=y_c^*|x_c)=\psi_c(x_c;\theta_c)$. Then $p_{\rm undir}(x)\propto p_{\rm dir}(x,y^*)$ (p. 197).
- Example (Fig. 4.39): $p(A,B,C,D)=\psi(A,B,C,D)/Z$ becomes a dummy child $E$ of all four, with $E=1$ and $p(E=1|A,B,C,D)\propto\psi$. Conditioning on the observed child makes the parents dependent, as in the UGM (p. 197).

**4.5.3 Conditional models and label bias (pp. 197–198).**
- Compare the CRF (Fig. 4.40a) with the directed chain called a maximum entropy Markov model (MEMM, Fig. 4.40b). The MEMM has the **label bias** problem: local features at time $t$ do not influence earlier states, since $y_{t-1}\perp x_t|y_t$. This blocks backward information flow (p. 198).
- Example: "banks" could be a verb or a noun. Later evidence ("fishing") cannot flow back in an MEMM to disambiguate it. The CRF does not have this problem (p. 198).
- Cause: directed models are *locally normalized* (each CPD sums to 1). MRFs and CRFs are *globally normalized*: the partition function $Z$ makes the model valid, so local factors need not sum to 1 (p. 198).
- Price: a CRF gives no valid distribution over $y_{1:T}$ until the whole sentence is seen. So CRFs are less useful than DPGMs for online or real-time inference. $Z$ depends on all parameters, which makes CRFs less modular and much slower to train (p. 198).

*Intuition note:* If every step must "spend" its probability locally, later evidence cannot reopen earlier choices. Normalizing once at the end allows that, but you must wait until the end.

**4.5.4 Combining directed and undirected (pp. 198–200).**
- *Chain graph (4.5.4.1):* a PGM with directed and undirected edges but no directed cycles. Fig. 4.41 gives
$$p(x_{1:D},y_{1:D})=p(x_{1:D})\,p(y_{1:D}|x_{1:D})=\Big[\tfrac1Z\prod_{i\sim j}\psi_{ij}(x_i,x_j)\Big]\Big[\prod_{i=1}^D p(y_i|x_i)\Big]\tag{4.153}$$
an undirected prior with a directed factorized likelihood (p. 199).
- A **PDAG** decomposes into a directed graph of *chain components*, whose nodes are linked internally only by undirected edges. The joint is $\prod_i p(C_i|\mathrm{pa}(C_i))$, with each CPD a CRF. For Fig. 4.42:
$$p(A,\dots,I)=p(A)p(B)p(C,D,E|A,B)p(F,G|C,D)p(H)p(I|C,E,H)\tag{4.154}$$
$$p(C,D,E|A,B)=\tfrac{1}{Z(A,B)}\phi(A,C)\phi(B,E)\phi(C,D)\phi(D,E)\tag{4.155}$$
$$p(F,G|C,D)=\tfrac{1}{Z(C,D)}\phi(F,C)\phi(G,D)\phi(F,G)\tag{4.156}$$
(p. 199).
- *ADMGs (4.5.4.2):* the author reports that every latent-variable DPGM can be rewritten so each latent is a root with exactly two observed children (the "projection"), observationally indistinguishable from the original. Each such latent induces dependence between its two children, drawn as a bidirected arc. The result is an **acyclic directed mixed graph** (Fig. 4.43) (pp. 199–200).
- **m-separation** is d-separation after replacing each $Y_i\leftrightarrow Y_j$ by $Y_i\leftarrow X_{ij}\rightarrow Y_j$ with $X_{ij}$ hidden. The most common ADMG case is linear-Gaussian, the structural equation model (Sec. 4.7.2) (p. 200).

**4.5.5 Gaussian PGMs (pp. 200–202).**
- Directed GGMs correspond to sparse regression matrices, undirected GGMs to sparse precision matrices (p. 200).
- DAG advantage: the regression weights $\mathbf W$, hence $\Sigma$, can depend on covariates with no positive-definiteness worry. Disadvantage: dependence on variable order, though time series have a natural order (p. 200).
- A (Gaussian) chain graph combines both. A VAR process of order 2 (second-order Markov chain, $x_t\in\mathbb R^D$):
$$p(x_t|x_{t-1},x_{t-2},\theta)=\mathcal N(x_t|A_1x_{t-1}+A_2x_{t-2},\Sigma)\tag{4.157}$$
The time axis is most naturally modeled by a DPGM. If $\Sigma^{-1}$ is sparse, within-slice correlation is most naturally modeled by a UPGM (p. 200).
- Example (4.158–4.159), shapes $5\times5$ (p. 201):
$A_1=\begin{pmatrix}3/5&0&1/5&0&0\\0&3/5&0&-1/5&0\\2/5&1/3&3/5&0&0\\0&0&0&-1/2&1/5\\0&0&1/5&0&2/5\end{pmatrix}$,
$A_2=\begin{pmatrix}0&0&-1/5&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&1/5&0&1/3\\0&0&0&0&-1/5\end{pmatrix}$,
$\Sigma^{-1}=\begin{pmatrix}2.13&-1.47&-1.2&0&0\\-1.47&2.13&1.2&0&0\\-1.2&1.2&1.8&0&0\\0&0&0&1&0\\0&0&0&0&1\end{pmatrix}$
($\Sigma$ has top block $\begin{pmatrix}1&1/2&1/3\\1/2&1&-1/3\\1/3&-1/3&1\end{pmatrix}$ and identity elsewhere). Zeros in $A_1,A_2$ are absent directed arcs from $x_{t-1},x_{t-2}$ into $x_t$. Zeros in $\Sigma^{-1}$ are absent undirected arcs within $x_t$ (Fig. 4.44) (p. 201).
- *Covariance graphs (4.5.5.1):* a sparse covariance matrix is drawn as a bidirected graph. Unconnected nodes are unconditionally independent, e.g. $Y_1\perp Y_3$ in Fig. 4.45(a), so $\Sigma_{1,3}=\Sigma_{3,1}=0$. An undirected model of the same shape would instead give $Y_1\perp Y_3|Y_2$ and $\Lambda_{1,3}=\Lambda_{3,1}=0$, with $\Lambda=\Sigma^{-1}$ (p. 201). A bidirected graph converts to a latent-variable DAG by replacing each bidirected edge with a hidden common cause (confounder). Then d-separation applies (p. 202).

### 4.6 PGM extensions
**4.6.1 Factor graphs (pp. 202–205).** A factor graph unifies directed and undirected models (p. 202).
- *Bipartite (4.6.1.1):* round variable nodes, square factor nodes, an edge from each variable to each factor mentioning it. For the MRF of Fig. 4.46 with one potential per maximal clique:
$$f(x_1,\dots,x_4)=f_{124}(x_1,x_2,x_4)f_{234}(x_2,x_3,x_4)\tag{4.160}$$
Factor graphs are more fine-grained: one potential per edge gives
$$f=f_{14}(x_1,x_4)f_{12}(x_1,x_2)f_{34}(x_3,x_4)f_{23}(x_2,x_3)f_{24}(x_2,x_4)\tag{4.161}$$
(p. 202).
- A DPGM converts by making one factor per CPD, connected to the variables that use it. Fig. 4.47:
$$f=f_1(x_1)f_2(x_2)f_{123}(x_1,x_2,x_3)f_{34}(x_3,x_4)f_{35}(x_3,x_5)\tag{4.162}$$
with $f_{123}=p(x_3|x_1,x_2)$, etc. If every node has at most one parent (chain or simple tree), there is one factor per edge, and root priors can be absorbed into children's factors. Such models equal pairwise MRFs (pp. 202, 204).
- *Forney factor graphs (4.6.1.2):* nodes are factors, edges are variables (like neural-network or circuit diagrams). Example $f=f_a(x_1)f_b(x_1,x_2)f_c(x_2,x_3,x_4)f_d(x_4,x_5)$ (4.163). $x_3$ and $x_5$ are half-edges, since each is in only one factor. Edge directions are a mnemonic and let messages be named uniquely. FFGs support hierarchical (blackbox) construction, e.g. $f=f_{\rm prior}(x_1,\dots,x_4)f_{\rm lik}(x_4,x_5)$ (4.164) (p. 204).
- A variable in more than 2 factors needs an equality-constraint node:
$$f_=(x,x_1,x_2)=\delta(x-x_1)\delta(x-x_2)\tag{4.165}$$
(Dirac delta if continuous, Kronecker if discrete): a "wire splitter". Fig. 4.49(a) is equivalent to
$$f(x,y_1,y_2)=f_x(x)f_{y|x}(y_1,x)f_{y|x}(y_2,x)\tag{4.166}$$
Using the same $f_{y|x}$ twice is parameter tying (p. 205).

**4.6.2 Probabilistic circuits (pp. 205–206).** These support efficient exact inference. They include arithmetic circuits and sum-product networks (SPNs). An SPN is a directed tree-structured model. Terminal nodes are univariate distributions. Inner nodes are weighted sums (convex combinations) and products. SPNs use context-specific independence, so exact inference takes time proportional to the number of links, rather than depending on treewidth. They are useful for missing-data imputation. Einsum networks are a recent extension (pp. 205–206).

**4.6.3 Directed relational PGMs (pp. 206–208).**
- Plates cannot express many models (not even a simple HMM). Relational probability models (RPMs) handle several object types and relations, using constant, function and predicate symbols with type signatures (p. 206).
- Book-review example: $H$onest: Customer→{T,F}; $K$indness, $Q$uality, $R$ecommendation ∈ {1,…,5} (4.167–4.170). With $C$ customers and $B$ books, ground terms such as $H(C_1)$, $Q(B_1)$, $R(C_1,B_2)$ are the random variables. Root priors: $H(c)\sim\mathrm{Cat}(0.99,0.01)$, $K(c)\sim\mathrm{Cat}(0.1,0.1,0.2,0.3,0.3)$, $Q(b)\sim\mathrm{Cat}(0.05,0.2,0.4,0.2,0.15)$ (4.171–4.173). $R(c,b)\sim\mathrm{RecCPD}(H(c),K(c),Q(b))$ (4.174). As a table this has $2\times5\times5=50$ rows of 5 entries (pp. 206–207).
- A template (Fig. 4.50a) is "unrolled" into a ground network. There are $C\times B+2C+B$ variables and $2^C5^{C+B+BC}$ possible worlds. For specific queries, relevant pieces can be unrolled dynamically (p. 207).
- Predicting missing $R(c,b)$ is a simplified recommender system, solvable with standard inference (Chapter 9) (p. 207).
- *Identity (relational) uncertainty:* if it is unknown which edition $C_1$ reviewed, all candidate referents become parents of $R$. A variable $L(c)$ selects the referent:
$$R(c,b)\sim\mathrm{RecCPT}(H(c),K(c),Q(b'))\ \text{ where } b'=L(c)\tag{4.175}$$
The CPD acts as a multiplexer (Fig. 4.51). Entity resolution / record linkage is the task of mapping strings to objects (p. 208).

**4.6.4 Undirected relational PGMs (pp. 208–211).** These are analogous, and especially useful in discriminative settings (p. 208).
- *Collective classification (4.6.4.1):* classify university web pages using content and link structure. Specify a template CRF with tied parameters and unroll it over the web graph (pp. 208–209).
- *Markov logic networks (4.6.4.2):* relational UGMs specified in first-order logic. "Smoking causes cancer" and "friends of a smoker smoke":
$$\forall x.\,Sm(x)\Rightarrow Ca(x)\tag{4.176}$$
$$\forall x\forall y.\,Fr(x,y)\wedge Sm(x)\Rightarrow Sm(y)\tag{4.177}$$
In clausal (CNF) form: $\neg Sm(x)\vee Ca(x)$ (4.178), $\neg Fr(x,y)\vee\neg Sm(x)\vee Sm(y)$ (4.179) (p. 209).
- With two people A, B there are 8 binary variables ($Sm$, $Ca$ for each person; $Fr(x,y)$ for 4 pairs), hence $2^8$ possible worlds (Table 4.5). The footnote says $Fr$ is not forced symmetric and $x\neq y$ is not enforced (p. 209).
- A hard rule becomes a potential, equal to 1 if the clause is true and 0 if false (4.180). Fig. 4.52 shows the ground UGM. Soft rules use weights, with $w>0$ controlling how strongly the rule is enforced:
$$\Psi=\begin{cases}e^w&\text{if clause true}\\ e^0&\text{if false}\end{cases}\tag{4.181}$$
$$p(x)=\frac{1}{Z(w)}\exp\Big(\sum_i w_i n_i(x)\Big)\tag{4.182}$$
where $n_i(x)$ is the number of true instances of clause $i$ in $x$ (p. 210).
- Ground models are often huge, so **lifted inference** avoids building them. Hinge-loss MRFs relax the discrete problem to a continuous one, with exact inference by convex optimization. Their template language, probabilistic soft logic, is less expressive than MLNs (p. 210). MLNs have been combined with deep learning (GNN inference; evidence fusion of DNN predictions) (p. 211).
- Subtlety: in undirected models, the size of the unrolled model can change inference even with no data on the new objects. Doubling a hidden chain from $T$ to $2T$ with no new evidence gives $p(z_t|y_{1:T},M_1)\neq p(z_t|y_{1:T},M_2)$ because of different partition functions. This does not happen with a directed chain, since the new nodes marginalize out (locally normalized, modular) (p. 211).

**4.6.5 Open-universe models (p. 211).** RPMs make a closed-world assumption (fixed object set). It is unrealistic in many real problems, e.g. tracking an unknown number of objects, monitoring seismic events for the nuclear test-ban treaty, and citation matching. Open-universe probability models (OUPMs) generate new objects and properties. BLOG was the first formal language; it used slow general MCMC. Multi-entity Bayesian networks are another. The Bean Machine library supports more efficient inference (p. 211).

**4.6.6 Programs as probability models (p. 212).** In a probabilistic programming language (PPL), possible worlds are execution traces of a program with random choices (procedural, vs the declarative OUPMs). Per the quoted definition, probabilistic programs add (1) random draws, which define $p(z,y)$, and (2) conditioning on observations, which is $p(z|y)$. Examples: Gen, Pyro, Turing. Inference is often by SMC (Chapter 13) (p. 212).

### 4.7 Structural causal models
**Definition (p. 212).** An SCM is a triple $M=(U,V,F)$. $U=\{U_i\}$ are exogenous "noise" inputs. $V=\{V_i\}$ are endogenous variables. $F=\{f_i\}$ are deterministic functions $V_i=f_i(V_{pa_i},U_i)$. The equations are recursive, so the dependency graph is a DAG. The model is assumed causally sufficient: $V$ and $U$ contain all causally relevant factors, though not all are observed. The author calls this the "causal Markov assumption" (p. 212).
- Unmodeled variables are lumped into the noise. A distribution $p(U)$ pushed through the functions induces $p(V)$. SCMs make stronger assumptions than PGMs (p. 212).
- Usually $p(U)$ factorizes (independent $U_i$): a Markovian SCM. If some $U_i$ are dependent, extra hidden parents (drawn as bidirected or undirected edges) give a semi-Markovian SCM (pp. 212–213).

**4.7.1 Education and wealth (p. 213).** $X$ = education (0 = high school, 1 = college, 2 = graduate), $Y$ = wealth, $Z$ = debt. Edges $X\to Y$, $X\to Z$ (more education, more debt in general), $Z\to Y$ (more debt, less wealth in general).
$$X=f_X(U_x),\quad Z=f_Z(X,U_z),\quad Y=f_Y(X,Z,U_y)\tag{4.183–4.185}$$
with some prior $p(U_x,U_y,U_z)$. Fig. 4.53b draws the noises explicitly, making clear they are a priori independent (p. 213).

**4.7.2 Structural equation models (p. 214).** An SEM (path diagram) is an SCM with all functions linear and Gaussian noise. It is used widely in economics and social science: causal interpretation and computational tractability.
$$X=U_x,\quad Z=c_z+w_{xz}X+U_z,\quad Y=c_y+w_{xy}X+w_{zy}Z+U_y\tag{4.186–4.188}$$
With Gaussian noises this is the Gaussian DGM
$$p(X)=\mathcal N(X|\mu_x,\sigma_x^2),\ p(Z|X)=\mathcal N(Z|c_z+w_{xz}X,\sigma_z^2),\ p(Y|X,Z)=\mathcal N(Y|c_y+w_{xy}X+w_{zy}Z,\sigma_y^2)\tag{4.189–4.191}$$
Relaxing linearity and Gaussianity gives "nonparametric SEMs", equivalent to SCMs (p. 214).

**4.7.3 Do operator and augmented DAGs (pp. 214–215).**
- A *perfect intervention* $do(X_i=x_i)$ clamps $X_i$. Its incoming edges are cut ("graph surgery") (p. 215).
- Education example (Fig. 4.54a): setting $Z=0$ by paying off all student debt. $p(X|do(Z=z))\neq p(X|Z=z)$. Seeing zero debt suggests no higher education, so $p(X\ge1|Z=0)$ is small. After paying off everyone's loans, $p(X\ge1|do(Z=0))=p(X\ge1)$ (p. 215).
- *Additive intervention:* shift the mechanism, e.g. $\Delta=-10{,}000$ (p. 215).
- *Augmented DAG:* add a parent action node (square) to each variable whose mechanism may change. With $A_z\in\{0,1\}$:
$$Z=f'_Z(X,U_x,A_z)=\begin{cases}f_Z(X,U_x)&A_z=0\\ f_Z(X,U_x)+\Delta&A_z=1\end{cases}\tag{4.192}$$
Then $p(Q|do(A_z=a),E=e)=p(Q|A_z=a,E=e)$, because $A_z$ has no parents to cut. Surgery gives a simpler graph and is less general than the augmented DAG (p. 215).

*Intuition note:* Observing a value is evidence about its causes. Forcing a value breaks the link to its causes, so it says nothing about them.

**4.7.4 Counterfactuals (pp. 215–217).**
- Effects of causes (choose an action) can use Bayesian decision theory. Causes of effects ask counterfactual questions ("had I not taken aspirin…?"), important for legal reasoning, explainability and fairness (pp. 215–216).
- Counterfactual reasoning needs strictly more assumptions than interventions. Pearl's causal hierarchy (Table 4.6) has three levels, each more powerful but with stronger assumptions: association $p(Y|a)$ (seeing); intervention $p(Y|do(a))$ (doing); counterfactuals $p(Y^a|do(a'),y')$ (imagining) (p. 216).
- Counterfactual queries have the form $p(Y^{a'}|do(a),y)$: the distribution of $Y$ had I done $a'$, given I did $a$ and saw $y$. $Y^{a'}$ is a potential outcome. $p(Y^{a'}=y)=p(Y=y|do(a'))$ is interventional, not counterfactual (p. 216).
- Potential outcomes as an SCM (Fig. 4.55). Each unit $i$ has hidden noise $U_i$ that maps deterministically to $Y_i^0,Y_i^1$. Only the outcome for the chosen action is seen. Not seeing both is the "fundamental problem of causal inference" (p. 217).
- Assumptions (p. 217): (i) independent noise sources, called SUTVA by the author (it fails if treatment on $j$ affects $i$); (ii) the same mechanism, shared parameter $\theta$, for all units; (iii) noise unaffected by actions ("ceteris paribus").
- Procedure for an individual unit (p. 217): (1) **abduction**: infer $p(U_i|A_i=a,Y_i=y_i)$. (2) **intervention**: replace $A_i=a$ by $A_i=a'$ to get $G_{a'}$. (3) **prediction**: propagate that posterior through $G_{a'}$ to get $p(Y_i^{a'}|A_i=a,Y_i=y_i)$.
- A **twin network** clones the deterministic variables with noise shared between branches. The SWIG is a related formalism (p. 217).
- Per the author, potential outcomes are mathematically equivalent to SCMs but do not use graph notation. SCMs are more popular in computer science, potential outcomes in economics. Footnote 17 defines abduction/induction/deduction as estimating the hidden input/function/output of $y=f(x)$ (p. 217).

*Intuition note:* A counterfactual first asks "which hidden circumstances produced what I saw?", then replays the same circumstances with a different action.

## Toy example (ours, not from the text)
SCM: $X\sim\text{Bernoulli}(0.5)$ (higher education), $U_z\sim\text{Bernoulli}(0.8)$ independent, $Z=X\wedge U_z$ (debt present).
- $P(Z{=}0|X{=}1)=1-0.8=0.2$ and $P(Z{=}0|X{=}0)=1$.
- $P(Z{=}0)=0.5\cdot0.2+0.5\cdot1=0.6$.
- **Seeing:** $P(X{=}1|Z{=}0)=\dfrac{0.5\cdot0.2}{0.6}=\dfrac{1}{6}\approx0.167$.
- **Doing:** cut the edge $X\to Z$ and set $Z=0$. $X$ keeps its own mechanism, so $P(X{=}1|do(Z{=}0))=0.5$. This differs from 0.167, as in the text's argument (p. 215).
- **Counterfactual:** observe $X=1$, $Z=1$. Abduction: $Z=X\wedge U_z$ forces $U_z=1$. Intervention: set $X=0$. Prediction: $Z=0\wedge1=0$. So "had this person not gone to college, they would have had no debt" with probability 1 in this model.

## Concepts
- [[perfect-map]] (new) — graph $G$ with $I(G)=I(p)$: represents all and only the CI properties of $p$ (p. 194)
- [[chordal-graph]] (new) — decomposable graph representable perfectly by both DPGM and UPGM (p. 195)
- [[moralization]] (new) — marrying co-parents, then dropping arrows, to turn a DPGM into a UPGM (p. 196)
- [[conditional-random-field]] (new) — $p(y|x)=\exp f/Z(x)$, normalized per input $x$ (p. 194)
- [[label-bias-problem]] (new) — locally normalized chains (MEMMs) block backward flow of evidence (p. 198)
- [[local-vs-global-normalization]] (new) — CPDs sum to 1 vs one partition function over joint configurations (p. 198)
- [[chain-graph]] (new) — PGM with directed and undirected edges, no directed cycles; PDAG of chain components (p. 199)
- [[admg]] (new) — mixed graph with bidirected edges for latent common causes; m-separation (p. 200)
- [[factor-graph]] (new) — bipartite or Forney graph displaying a function's factorization (pp. 202–204)
- [[probabilistic-circuit]] (new) — SPN-type models giving exact inference linear in the number of links (p. 205)
- [[relational-probability-model]] (new) — template over typed objects, unrolled into a ground network (p. 206)
- [[markov-logic-network]] (new) — weighted first-order clauses defining $p(x)\propto\exp(\sum w_in_i)$ (p. 210)
- [[open-universe-probability-model]] (new) — model where the number of objects is uncertain (p. 211)
- [[probabilistic-programming]] (new) — worlds are execution traces; random draws plus conditioning (p. 212)
- [[structural-causal-model]] — $(U,V,F)$: deterministic mechanisms plus exogenous noise (p. 212)
- [[structural-equation-model]] (new) — linear-Gaussian SCM (p. 214)
- [[do-operator]] — clamp a variable and cut incoming edges; differs from conditioning (p. 215)
- [[augmented-dag]] (new) — DAG with action parents encoding mechanism changes (p. 215)
- [[potential-outcomes]] — $Y^{a'}$: outcome had action $a'$ been taken (p. 216)
- [[fundamental-problem-of-causal-inference]] — only one potential outcome per unit is seen (p. 217)
- [[sutva]] — here: independent noise across units (no interference) (p. 217)
- [[ladder-of-causation]] — association, intervention, counterfactuals (p. 216)
- [[counterfactual-abduction-action-prediction]] (new) — three-step counterfactual procedure (p. 217)
- [[d-separation]] — graphical CI rule; used via m-separation for ADMGs (p. 200)

## Canonical instances
- [[v-structure-vs-4-cycle]] — CI patterns only a DPGM or only a UPGM can represent (pp. 194–195)
- [[student-network-moralization]] — adds D–I, G–J, L–S edges (p. 196)
- [[pos-tagging-banks-fishing]] — label bias illustrated (p. 198)
- [[var2-chain-graph]] — Gaussian chain graph with matrices $A_1,A_2,\Sigma^{-1}$ (pp. 200–201)
- [[book-review-rpm]] — Honest/Kindness/Quality/Recommendation template, identity uncertainty (pp. 206–208)
- [[smoking-mln]] — Smoking/Friends/Cancer Markov logic network (pp. 209–210)
- [[education-wealth-scm]] — $X,Z,Y$ SCM and $do(Z=0)$ (pp. 213–215)
- [[aspirin-headache]] — causal hierarchy example (p. 216)

## Bridges (candidates)
- [same-math] SCM ↔ potential outcomes (causal inference): the author says the two frameworks are mathematically equivalent.
- [same-math] Abduction step ↔ Bayesian inference: the posterior over latent noise $p(U_i|\text{evidence})$ is ordinary Bayesian conditioning, then propagated forward.
- [same-math] MLN joint $\exp(\sum_i w_in_i)/Z$ ↔ log-linear (exponential-family) MRF: it is an MRF with feature counts $n_i$.
- [structural-analogy] Augmented DAG action nodes ↔ reinforcement learning: the author says the same influence-diagram formalism is used in MDPs.
- [structural-analogy] Local vs global normalization ↔ Bayesian modularity: directed chains marginalize out unseen nodes, undirected ones depend on $Z$.
- [metaphor] Forney factor graph ↔ circuit or neural-network diagram: signals flow along edges, modified by nodes.

## Questions this raises
- When is an interventional quantity $p(Y|do(a))$ computable from observational data and a graph (identifiability, footnote 16)?
- How does lifted inference avoid grounding a Markov logic network?
- Why do counterfactuals need stronger assumptions than interventions, beyond the three assumptions listed?
- How do I choose between a CRF and a directed model when I need online inference?

## Reading notes
- This is part 3/3 of Chapter 4. It starts mid-section at §4.4.3.2 (printed p. 194) and ends at the end of §4.7.4 (p. 217). Printed p. 218 is blank. The split is at a section boundary.
- Page labels give printed numbers (pdf − 34 = printed).
- Eq. 4.148 has no explicit brackets in print. The $\log Z(x_n)$ term is placed inside the sum because it carries index $n$.
- Misprints visible in the images:
  - p. 214: the second and third Gaussian noise terms read $\mathcal N(U_x|0,\sigma_z^2)$ and $\mathcal N(U_x|0,\sigma_y^2)$, where $U_z$, $U_y$ are meant.
  - p. 214: $X=U_x$ with $U_x$ zero-mean (4.186), but Eq. 4.189 has mean $\mu_x$.
  - p. 215: the additive intervention writes $f'_z(Z,U_z)=f_z(Z,U_z)+\Delta$, though $Z$'s mechanism takes $X$.
  - p. 215, Eq. 4.192: uses $U_x$ in place of $U_z$.
  - Table 4.6: $p(Y^a|do(a'),y')$, whereas the text uses $p(Y^{a'}|do(a),y)$.
  - p. 206: "Kindess" in Eq. 4.168.
  - p. 209, footnote 14: refers to nodes "$Fr(A)$, $Fr(B)$", meaning $Fr(A,A)$, $Fr(B,B)$.
  - p. 213: "Figure 4.53b(a)" should read 4.53(a).
- "SUTVA" is described here only as independent noise sources. The text does not mention single-version treatments.
- The unit contains no exercises.
