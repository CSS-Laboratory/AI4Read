---
id: pearl-2016-primer/ch02-graphical
work: pearl-2016-primer
unit: "2 Graphical Models and Their Applications"
pages: 35-51
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Graphical Models and Their Applications

## L0 — One line
The shape of a causal graph alone tells us which variables are independent, given which others (via chains, forks, colliders and d-separation), so data can test the graph (assuming the error terms are independent).

## L1 — The gist (≤ 120 words)
The chapter asks how a causal graph links to patterns of independence in data. Three building blocks are examined: chains and forks, where conditioning on the middle node blocks dependence, and colliders, where conditioning on the common effect (or its descendant) creates dependence. Definition 2.4.1 (d-separation) combines these into a rule for any graph. Since d-separation uses only the graph, not the functions or error distributions, it gives local, nonparametric tests of a causal model. It also shows that graphs with the same skeleton and v-structures cannot be told apart by such tests. This lets us reason from data back to candidate models.

**Prerequisites:** conditional probability and independence; DAG and SCM basics from Chapter 1; simple linear regression.

## L2 — Key ideas (5–10 bullets)
- Any SCM (structural causal model: equations plus error terms) with a given graph shares the same independencies, whatever its functions; this holds when the error terms are independent (pp. 36, 39–40).
- Chain and fork: the variables at the ends are typically dependent. They become independent once we condition on the middle node (Rules 1–2, pp. 39–40).
- Collider: two causes are independent, but become dependent when we condition on their common effect or any of its descendants (Rule 3, p. 44).
- Conditioning is "filtering by value"; this explains the collider effect (p. 41), which the scholarship, coins-and-bell and Monty Hall examples illustrate (pp. 41–43).
- d-separation: a path is blocked by a conditioned chain/fork middle, or by an unconditioned collider with no conditioned descendant. Two nodes are d-separated if all paths are blocked (p. 46).
- d-connected variables (nodes with at least one unblocked path) are only likely dependent: intransitive cases (where $X\to Y\to Z$ but $X$ and $Z$ vary independently) are exceptions (pp. 38, 46).
- Each d-separation implies a testable conditional independence, e.g. a vanishing regression coefficient. A failed test refutes the model and points to where it is wrong (p. 49).
- Compared with global fit tests, d-separation tests are nonparametric (they use only the graph, not specific functions) and local (p. 50).
- Graphs sharing a skeleton (same edges, ignoring direction) and v-structures (colliders whose parents are not adjacent) are indistinguishable by these tests, which enables causal search from data (p. 50).

## L3 — Walkthrough

### 2.1 Connecting models to data (p. 35)
Chapter 1 treated probabilities, graphs and structural equations separately. Here, independence (defined algebraically) is expressed through DAGs. A researcher with an SCM can predict independence patterns from the graph alone, without the equations or error distributions. Conversely, observed independencies say something about whether a hypothesised model is correct (p. 35). Chapter 3 will use this to predict intervention results (p. 35).

### 2.2 Chains and forks (pp. 35–40)
A causal model is a mechanism that generates data. Even a purely graphical model (we know which variables are functions of which, not the functions) fixes independencies true of every data set from that structure (p. 36).

**Three SCMs, one graph (Figure 2.1: X → Y → Z, each with its own U).** Each U stands for unknown or random effects (p. 36).
- SCM 2.2.1 (school funding X, SAT score Y, college acceptance Z): $X=U_X$, $Y = x/3 + U_Y$, $Z = y/16 + U_Z$ (p. 36).
- SCM 2.2.2 (switch, circuit, bulb): logical functions. $Y$ = Closed if ($X$=Up and $U_Y=0$) or ($X$=Down and $U_Y=1$), else Open. $Z$ = On if ($Y$=Closed and $U_Z=0$) or ($Y$=Open and $U_Z=1$), else Off (p. 36).
- SCM 2.2.3 (work hours X, training Y, race time Z): $Y = 84 - x + U_Y$, $Z = 100/y + U_Z$ (p. 37).

They share no functions, yet their data share these properties (p. 37):
1. $Z$ and $Y$ are likely dependent: for some $z,y$, $P(Z=z|Y=y)\ne P(Z=z)$.
2. $Y$ and $X$ are likely dependent.
3. $Z$ and $X$ are likely dependent.
4. $Z$ and $X$ are independent conditional on $Y$: for all $x,y,z$, $P(Z=z|X=x,Y=y)=P(Z=z|Y=y)$.

*Why.* Variables joined by an arrow are likely dependent, because the child's value is a function of the parent's (p. 38). Dependence of $Z$ on $X$ follows from the two links, with exceptions. **SCM 2.2.4** is the exception, an *intransitive* case: $Y$ takes $a$ or $b$ depending on $X$, but $Z$ responds to $Y$ only when $Y=c$. So $X$ has no effect on $Z$ (p. 38). The author says such cases are a small minority (p. 38). Footnote 1 (attached to the claim that $Y$ and $X$, joined by an arrow, are likely dependent) gives a different pathological case: $X$ and $U_Y$ fair coins, $Y=1$ iff $X=U_Y$. Then $P(Y=1|X=1)=P(Y=1|X=0)=P(Y=1)=1/2$. This needs exact probabilities, so it is rare and can be ignored in practice (p. 38).

*Conditioning on $Y$.* Conditioning means filtering the data into groups by the value of $Y$. Within the group $Y=a$, choosing different $x$ changes $U_Y$ so as to keep $Y=a$. But $Z$ depends only on $Y$ and $U_Z$, not on $U_Y$, so $Z$ is unaffected. Hence $X \perp Z \mid Y$ for every value of $Y$ (p. 38).

A **chain** is three nodes with one edge into and one out of the middle node (p. 38).

**Rule 1 (chains).** Two variables $X$ and $Y$ are conditionally independent given $Z$ if there is only one unidirectional path between them and $Z$ is any set of variables that intercepts that path (p. 39). It holds only if the error terms are independent. If $U_X$ caused $U_Y$, conditioning on $Y$ would not necessarily make $X$ and $Z$ independent (p. 39).

**Forks (Figure 2.2: $Y \leftarrow X \rightarrow Z$).** Examples: SCM 2.2.5 (temperature $X$, ice cream sales $Y$, crime $Z$): $Y=4x+U_Y$, $Z=x/10+U_Z$. SCM 2.2.6 (one switch, two bulbs), with logical functions (p. 39). Assuming independent errors, the shared properties are (p. 40):
1. $X,Y$ likely dependent; 2. $X,Z$ likely dependent; 3. $Z,Y$ likely dependent (likely, "though not certain"); 4. $Y\perp Z\mid X$: for all $x,y,z$, $P(Y=y|Z=z,X=x)=P(Y=y|X=x)$.

Given $X$, the values of $Y$ and $Z$ change only in response to $U_Y$ and $U_Z$, which are independent (p. 40). The middle node $X$ is the *common cause* (p. 40).

**Rule 2 (forks).** If $X$ is a common cause of $Y$ and $Z$, and there is only one path between $Y$ and $Z$, then $Y\perp Z\mid X$ (p. 40).

*Intuition note.* Conditioning on a middle node freezes the only thing linking the two ends. What is left over comes from independent errors.

### 2.3 Colliders (pp. 40–45)
A **collider** is a node receiving edges from two other nodes (Figure 2.3: $X\rightarrow Z\leftarrow Y$) (p. 40). With independent $U_X,U_Y,U_Z$ the shared properties are (p. 41):
1. $X,Z$ likely dependent; 2. $Y,Z$ likely dependent;
3. $X$ and $Y$ are independent: for all $x,y$, $P(X=x|Y=y)=P(X=x)$;
4. $X$ and $Y$ are likely dependent conditional on $Z$: for some $x,y,z$, $P(X=x|Y=y,Z=z)\ne P(X=x|Z=z)$.

Point 3: $X$ and $Y$ respond only to independent errors, and there is no causal mechanism associating them (p. 41). Point 4: among cases with the same $Z$, a change in $X$ must be compensated by a change in $Y$, otherwise $Z$ would change (p. 41). Simplest case: $Z=X+Y$. Knowing $X=3$ says nothing about $Y$; but if $Z=10$ is known, then $X=3$ implies $Y=7$ (p. 41).

**Scholarship example.** Musical talent and grades are independent in the population. Among scholarship holders, lacking musical talent makes high grades likely (pp. 41–42).

**Coins and bell (numerical).** Two independent fair coins $X,Y$; a bell $Z=1$ rings if at least one lands heads (p. 42). Table 2.1 gives $P(X,Y,Z)$ = 0.25 for each of HH→1, HT→1, TH→1, TT→0 (p. 42). Then $P(X=H|Y=H)=P(X=T|Y=T)=1/2$, so $X\perp Y$ (p. 42). Conditional on $Z=1$ (Table 2.2), the three possible outcomes HH, HT, TH each have probability 0.333 and TT has 0. So
$$P(X=H|Z=1)=\tfrac13+\tfrac13=\tfrac23,\qquad P(X=H|Y=H,Z=1)=\tfrac12 .$$
So given $Z=1$, learning $Y=H$ moves the probability of $X=H$ from $2/3$ to $1/2$ (p. 42). Given $Z=0$, both coins are known to be tails (Table 2.2, pp. 42–43).

**Monty Hall.** Your initial choice and the car's location are the parents. The door Monty opens is the collision node (p. 43). They are independent (you pick the car with probability $1/3$). Conditional on Monty's door, they are dependent: the car is behind Door B in $1/3$ of all cases, but in $2/3$ of the cases where you chose A and Monty opened C (p. 43).

**Descendants of a collider.** Add a witness $W$ who reports the bell, but falsely says it rang in 50% of the cases where it did not (p. 43). Table 2.3 gives $P(X,Y,W)$: HH,1: 0.25; HT,1: 0.25; TH,1: 0.25; TT,1: 0.125; TT,0: 0.125 (p. 44). Then
$$P(X=H|Y=H)=P(X=H)=\tfrac12,\quad P(X=H|W=1)=\frac{0.25+0.25}{0.25+0.25+0.25+0.125}=\frac{0.5}{0.875},$$
$$P(X=H|Y=H,W=1)=\frac{0.25}{0.25+0.25}=0.5<\frac{0.5}{0.875}.$$
Thus $X$ and $Y$ are independent before the witness report is read and dependent afterwards (p. 44).

**Rule 3 (colliders).** If $Z$ is the collision node between $X$ and $Y$, and there is only one path between them, then $X$ and $Y$ are unconditionally independent but dependent conditional on $Z$ and any descendants of $Z$ (p. 44). The author says it is key for testing models, for discovering models, and for resolving Simpson's Paradox (p. 44).

**Remark (pp. 44–45).** People tend to assume that statistical dependence needs a causal mechanism (one variable causes the other, or a third causes both). A collider creates dependence "in a third way", violating the assumption of "no correlation without causation" (p. 45).

*Intuition note.* Selecting cases by an effect links its causes. If the effect is held fixed, a change in one cause must be compensated by a change in the other (p. 41).

Study question 2.3.1 (Figures 2.5, 2.6) (p. 45): see Exercises.

### 2.4 d-separation (pp. 45–48)
Most graphs have many paths per pair, each crossing chains, forks and colliders (p. 45). **d-separation** ("d" for "directional") is a criterion that works for any graph. d-separated nodes are definitely independent. d-connected nodes are possibly, or most likely, dependent (footnote 2: d-connected variables are dependent for almost all functions on the arrows, except intransitive cases) (p. 46). Two nodes are d-separated if every path between them is *blocked*. One unblocked path makes them d-connected (pipe analogy: dependence is water, and one blocked point stops a pipe) (p. 46). With no conditioning, only colliders block paths (p. 46).

**Definition 2.4.1 (d-separation).** A path $p$ is blocked by a set $Z$ if and only if (p. 46):
1. $p$ contains a chain $A\to B\to C$ or fork $A\leftarrow B\rightarrow C$ whose middle node $B$ is in $Z$; or
2. $p$ contains a collider $A\to B\leftarrow C$ such that $B$ is not in $Z$ and no descendant of $B$ is in $Z$.

If $Z$ blocks every path between $X$ and $Y$, they are d-separated conditional on $Z$, hence independent conditional on $Z$ (p. 47). The rule follows from Rules 1–3, considering one path at a time (p. 46).

**Figure 2.7** ($Z\to W\leftarrow X\to Y$, and $W\to U$) (p. 47). The only path between $Z$ and $Y$ has collider $W$ and fork $X$.
- Empty set: $Z$, $Y$ d-separated (blocked by $W$).
- Conditioning on $W$: d-connected; $U$, a descendant of the collider, gives the same.
- Conditioning on $\{W,X\}$: d-separated, because the fork node $X$ blocks the path even though $W$ is unblocked (p. 47).

**Figure 2.8** adds a fork path $Z\leftarrow T\rightarrow Y$ (p. 47). Now $Z$ and $Y$ are unconditionally dependent. Conditioning on $T$ blocks that path. $\{T,W\}$ re-connects them via $Z\to W\leftarrow X\to Y$. $\{T,W,X\}$ separates them again (p. 47).
- d-connected given: $W$, $U$, $\{W,U\}$, $\{W,T\}$, $\{U,T\}$, $\{W,U,T\}$, $\{W,X\}$, $\{U,X\}$, $\{W,U,X\}$.
- d-separated given: $T$, $\{X,T\}$, $\{W,X,T\}$, $\{U,X,T\}$, $\{W,U,X,T\}$ (p. 48).

$T$ is in every separating set, since it lies on the only path that is unblocked without conditioning (p. 48).

*Intuition note.* To read independence off a graph, check each path. Conditioning closes the middle of chains and forks, but opens colliders (and their descendants). One closed point is enough to close a whole path.

Study question 2.4.1 (Figure 2.9): see Exercises.

### 2.5 Model testing and causal search (pp. 48–50)
d-separation gives testable implications. If $G$ implies $A\perp B\mid C$ but the data suggest otherwise, $G$ can be rejected as a causal model for the data (p. 49).

**Example (Figure 2.9).** $X$ d-separates $W$ from $Z_1$. Regress $W$ on $X$ and $Z_1$: $w=r_X x + r_1 z_1$. If $r_1\neq 0$, then $W$ depends on $Z_1$ given $X$, so the model is wrong. The true model must have a path between $W$ and $Z_1$ not d-separated by $X$ (p. 49). For acyclic models with independent errors (Verma and Pearl 1990), if every d-separation condition matches a conditional independence in the data, no further test can refute the model. For any such data one can find functions and error probabilities that generate the data exactly (p. 49).

**Global testing alternative.** One estimates parameters and tests the likelihood of the whole model; this can be done approximately for linear Gaussian models (Bollen 1989) (p. 49). Problems (pp. 49–50):
1. If any parameter cannot be estimated (e.g. correlated errors or unobserved variables, see Section 3.8.3), the model cannot be tested.
2. A bad fit gives no hint of which edges to change.
3. With many noisy variables the test is unreliable.

**Advantages of d-separation** (p. 50): it is nonparametric (graph only) and local. Local tests find flawed areas, and still give partial information if one coefficient is not identifiable.

**Equivalence class.** Graphs $G_1,G_2$ are in the same equivalence class if they share a *skeleton* (same edges ignoring direction) and the same *v-structures* (colliders whose parents are not adjacent). Then they have identical d-separation conditions and testable implications (p. 50). So testing can narrow the field to a set of models, not a single model (p. 50). This allows search from data back to models (p. 50). Other search methods are beyond the book's scope (p. 50).

### Bibliographical notes (p. 51)
Chains/forks are credited to Simon (1953) and Reichenbach (1956), colliders to Pigou (1911). Colliders appear as "selection bias"/"Berkson paradox" in epidemiology and as "explaining away" in AI. d-separation was introduced in Pearl (1986) and proved in Verma and Pearl (1988) (p. 51).

## Toy example (ours)
Let $X,Y$ be independent fair bits (0 or 1) and $Z=X+Y$ (a collider). The four equally likely outcomes $(X,Y,Z)$ are $(0,0,0),(0,1,1),(1,0,1),(1,1,2)$, each $1/4$.
- Unconditional: $P(X=1)=1/4+1/4=1/2$. $P(X=1|Y=1)=P(1,1)/P(Y=1)=(1/4)/(1/2)=1/2$. So $X\perp Y$.
- Condition on $Z=1$: only $(0,1,1)$ and $(1,0,1)$ remain, each $(1/4)/(1/2)=1/2$. So $P(X=1|Z=1)=1/2$.
- Add $Y=1$ and $Z=1$: only $(0,1,1)$ remains, so $P(X=1|Y=1,Z=1)=0\ne 1/2$.
Conditioning on the common effect has made $X$ and $Y$ dependent (Rule 3). By Definition 2.4.1, $\{Z\}$ unblocks the path $X\to Z\leftarrow Y$, matching this result.

## Concepts
- [[d-separation]] — graph criterion: a path is blocked by a conditioned chain/fork middle node, or by an unconditioned collider without conditioned descendants; separation implies independence (p. 46)
- [[fork-chain-collider]] — the three elementary three-node path structures; conditioning on the middle blocks chains/forks but opens colliders (pp. 38–44)
- [[causal-dag]] — graph of which variables cause which; here read for independencies (p. 36)
- [[structural-causal-model-scm]] — functions plus exogenous errors; graph-implied independencies hold for any functions if errors are independent (pp. 36, 39)
- [[conditional-independence]] (new) — $P(Z|X,Y)=P(Z|Y)$ for all values; conditioning is "filtering" by value (p. 38)
- [[intransitive-case]] (new) — a pathological SCM where $X\to Y\to Z$ but $X$ and $Z$ vary independently (p. 38)
- [[v-structure]] (new) — collider whose parents are not adjacent (p. 50)
- [[equivalence-class]] (new) — graphs with the same skeleton and v-structures, hence the same testable implications (p. 50)
- [[testable-implications]] (new) — conditional independencies a graph requires, checked with data, e.g. vanishing regression coefficient (pp. 48–49)
- [[simpsons-paradox]] — only mentioned: Rule 3 will help resolve it in later chapters (p. 44)
- [[confounding-vs-selection-bias]] — only in the bibliographical notes: colliders linked to "selection bias" and "Berkson paradox" (p. 51)

## Canonical instances
- [[two-coins-and-bell]] — conditioning on a common effect makes independent coins dependent (pp. 42–43)
- [[scholarship-collider]] — talent and grades independent in general, dependent among scholarship holders (pp. 41–42)
- [[monty-hall-problem]] — the opened door is a collider; $1/3$ becomes $2/3$ given the choice of A and Monty opening C (p. 43)
- [[unreliable-witness]] — a descendant of a collider also opens the path (pp. 43–44)

## Bridges (candidates)
- [structural-analogy] Collider conditioning ↔ Bayesian inference: "explaining away" of one cause given the effect (named on p. 51) — the posterior over causes becomes dependent.
- [same-math] d-separation ↔ conditional independence in probabilistic graphical models: the graph reads off $P(A|B,C)=P(A|C)$ for the product decomposition (cited as (1.29), p. 51).
- [structural-analogy] Testing a graph by vanishing partial regression coefficients ↔ posterior predictive checks: derive a checkable implication, compare with data.
- [metaphor] Filtering data by a conditioning value ↔ Bayesian conditioning as restricting the sample space.

## Questions this raises
- If dependence can arise by conditioning on a collider, how do we pick adjustment variables without opening such paths (the promised Simpson's Paradox resolution)?
- How strong is the "likely dependent" claim: how rare are intransitive or cancelling cases in real data?
- How do we run the conditional-independence tests when variables are non-Gaussian or nonlinear, rather than a regression coefficient?
- Which edge directions can be determined from observational data, given equivalence classes?

## Exercises worth doing
- Study question 2.3.1 (p. 45) — practise independence given conditioning sets in chains, colliders and descendants (Figs 2.5, 2.6); parts (e)–(f) link to regression coefficients — difficulty: easy
- Study question 2.4.1 (p. 48) — apply d-separation to Figure 2.9: separating sets, minimal sets, prediction of $Y$ and $Z_2$ — difficulty: medium
- Study question 2.4.1(g) (p. 48) — does adding $W$ improve prediction of $Z_2$ from $Z_3$? Tests understanding of d-separation — difficulty: medium
- Study question 2.5.1(a)–(c) (p. 50) — equivalence classes for Figure 2.9 and which arrows are identifiable — difficulty: medium
- Study question 2.5.1(d)–(g) (pp. 50–51) — write regressions whose nonzero coefficients refute the model, and count the tests needed — difficulty: hard

## Reading notes
- Printed = pdf − 20. Pages pdf 55–71 carry text; pdf 72 (printed 52) is blank.
- The text layer is clean apart from the "k" markers. I checked the equations and tables against the page images.
- p. 46 says d-separated means "there exists no such path", but the definition that follows uses *blocked* paths, not no path. I follow the definition.
- p. 40: the fork point 3 says $Z$ and $Y$ are likely dependent. The explanation just below the list says "likely (though not certain)".
- p. 43: Table 2.3 comes from the figure's witness, who sometimes falsely reports. The stated 50% false-report chance gives the 0.125 + 0.125 split.
- Figure 2.9's edges are only visible in the image; I did not use them beyond the exercises.
