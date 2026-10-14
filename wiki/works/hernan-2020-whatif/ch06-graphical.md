---
id: hernan-2020-whatif/ch06-graphical
work: hernan-2020-whatif
unit: "6 Graphical representation of causal effects"
pages: 75-90
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Graphical representation of causal effects (Hernán & Robins, ch. 6)

## L0 — One line
A causal diagram (DAG) records our assumptions about who causes whom, and simple path rules then tell us which variables we should expect to be associated, marginally or after conditioning.

## L1 — The gist (≤ 120 words)
How can we write down our causal assumptions so that we can read off which variables will be associated? The chapter introduces causal DAGs: nodes are variables, and an arrow means a direct effect for at least one individual. Two variables are generally associated if one causes the other, if they share a common cause, or if we condition on a common effect (or its descendant). The path rules are called d-separation. Their link to statistical independence needs the causal Markov assumption (one direction) and faithfulness (the other). The chapter also classifies systematic bias by its structural source and shows that DAGs say little about effect modification. Graphs make assumptions explicit before conclusions are drawn.

**Prerequisites:** conditional independence; counterfactual notation $Y^a$ and exchangeability (earlier chapters of the book); idea of stratifying/conditioning; risk difference.

## L2 — Key ideas (5–10 bullets)
- A causal DAG has nodes for variables and arrows for direct causal effects. A missing arrow asserts no direct effect on anyone. Common causes of any pair of variables must be on the graph, even if unmeasured (pp. 75–76).
- Three structures create association: one variable causes the other, a common cause (fork), or conditioning on a common effect (collider) or its descendant. A collider (a common effect) blocks its path unless it, or a descendant of it, is conditioned on (pp. 78–81).
- Conditioning on a non-collider (mediator or common cause) blocks a path (p. 80). Blocking the common-cause path in this way is the graph-based justification for using stratification to achieve exchangeability (p. 80).
- d-separation (all paths between two variables are blocked) formalises these rules. With the causal Markov assumption (given its parents, a variable is independent of its non-descendants), d-separation implies independence. The converse is the faithfulness assumption (independence implies d-separation), which fails e.g. with exactly cancelling effects or with matching (pp. 82–83).
- Graphs cannot show violations of positivity except in special cases, and treatment nodes need well-defined interventions. Nodes such as "obesity" as treatment are generally not acceptable (pp. 82–84).
- Systematic bias means the data cannot identify the causal effect even with infinite data; informally it is structural association between treatment and outcome that does not arise from the causal effect. Lack of exchangeability arises from common causes (confounding) or conditioning on common effects (selection bias under the null) (pp. 85–86).
- Causal diagrams are less helpful for effect modification (the effect varying across levels of $V$): a DAG does not show whether, or in which way, $V$ modifies the effect. A surrogate effect modifier is a variable that is merely associated with the causal effect modifier $V$ (pp. 87–88).

## L3 — Walkthrough

### Chapter introduction (p. 75)
Earlier chapters used simple scenarios, so the causal network did not need to be explicit. As situations become more complex, it becomes crucial to be explicit about what we know and assume. Graphs summarise knowledge and assumptions, with the advice "draw your assumptions before your conclusions" (p. 75).

### 6.1 Causal diagrams (pp. 75–78)
**Setup.** Figure 6.1 has three nodes (random variables) $L, A, Y$ and edges $L\to A$, $L\to Y$, $A\to Y$. Time flows left to right. $L$ = disease severity, $A$ = heart transplant, $Y$ = death (p. 75).

**Meaning of arrows.** An arrow $V\to W$ means we know there is a direct causal effect (not mediated by other variables on the graph) for at least one individual. No arrow means we know $V$ has no direct effect on $W$ for any individual. The diagram does not say whether an effect is harmful or protective. It does not say how two causes of one variable interact (p. 75).

**DAG.** "Directed" = edges have a direction. "Acyclic" = no variable causes itself, directly or through others (p. 75).

**Technical Point 6.1 (formal).**
- Nodes are random variables $V=(V_1,\dots,V_M)$. $PA_m$ are the parents of $V_m$ (nodes with an arrow into it). $V_m$ is a descendant of $V_j$ if following arrows from $V_j$ reaches $V_m$. In Fig. 6.1, $PA_3=(L,A)$ for $V_3=Y$ (p. 76).
- The distribution is *Markov with respect to* $G$ if each $V_j$ is independent of its non-descendants given its parents. This is equivalent to the Markov factorization (p. 76):
$$f(v)=\prod_{j=1}^{M} f(v_j\mid pa_j).$$
- A **causal DAG** satisfies three conditions (p. 76):
  1. A missing arrow $V_j\to V_m$ means no direct causal effect of $V_j$ on $V_m$, relative to the other variables on the graph.
  2. All common causes of any pair of variables on the graph, even unmeasured, are on the graph.
  3. Any variable is a cause of its descendants.
- The **causal Markov assumption** links graph to data. Conditional on its direct causes, a variable is independent of any variable it does not cause. Equivalently, conditional on its parents, $V_j$ is independent of its non-descendants (p. 76).

*Intuition note.* The DAG encodes assumptions about how the joint distribution is built. Under the causal Markov assumption, a variable given its parents is independent of its non-descendants, which is equivalent to the density factoring into one conditional per node. The same assumption implies that common causes of any pair of variables must be on the graph.

**Examples (p. 76).**
- If transplant is randomised with a probability that depends on severity $L$, then $L$ is a common cause of $A$ and $Y$ and must be drawn. Fig. 6.1 is then a *conditionally randomized experiment*.
- If everyone is randomised with the same probability, $L$ is not a common cause. Fig. 6.2 ($A\to Y$) is a *marginally randomized experiment*.
- Fig. 6.1 can also depict an observational study, if we assume $A$ has parent $L$ and no other causes of $Y$. Otherwise those causes, even if unmeasured, must be drawn as common causes of $A$ and $Y$. The next chapter shows this is the graphical translation of conditional exchangeability $Y^a\perp\!\!\!\perp A\mid L$ for all $a$ (p. 76).

**Technical Point 6.2 (counterfactual model behind a DAG; p. 77).** Notation: $V_m^r$ is the counterfactual value of $V_m$ when the set $R$ is set to $r$. A *nonparametric structural equation model* (NPSEM) for $G$ assumes:
- unobserved errors $\epsilon_m$ and unknown deterministic functions $f_m(pa_m,\epsilon_m)$;
- $V_1=f_1(\epsilon_1)$;
- the one-step-ahead counterfactual $V_m^{\bar v_{m-1}}\equiv V_m^{pa_m}=f_m(pa_m,\epsilon_m)$.

Only parents of $V_m$ have a direct effect on it, relative to the other variables on $G$. Any variable can be intervened on. Other counterfactuals are built recursively: $V_3^{v_1}=V_3^{v_1,V_2^{v_1}}$, and $V_3^{v_1,v_4}=V_3^{v_1}$ because $V_4$ is not a direct cause of $V_3$. Robins (1986) called this model FCISTG, and Pearl (2009) showed how to represent it by a DAG. The authors generally assume every variable can be intervened on, though the statistical methods do not require it (p. 77).

**Technical Point 6.3 (independencies; p. 78).**
- The FCISTG alone does not imply the causal Markov assumption. Extra independence assumptions are needed.
- Pearl usually assumed all errors $\epsilon_m$ mutually independent (NPSEM-IE).
- Robins assumed only that the one-step-ahead counterfactuals are jointly independent (FFRCISTG). Robins showed this implies the causal Markov assumption.
- An NPSEM-IE is an FFRCISTG, but not vice versa.
- For Fig. 6.2, an NPSEM-IE implies full exchangeability $(Y^{a=0},Y^{a=1})\perp\!\!\!\perp A$. An FFRCISTG only implies marginal exchangeability $Y^a\perp\!\!\!\perp A$ for $a=0$ and $a=1$.
- Unless told otherwise, a causal DAG is taken to represent an FFRCISTG (p. 78).

**Link to counterfactuals (p. 77).** Each graph has an underlying counterfactual model that justifies the graph rules. Ordinary diagrams do not show counterfactual variables. SWIGs (Single World Intervention Graphs) do; they are deferred to Chapter 7. Causal diagrams represent causation and association at once, and the chapter is an informal, intuition-first introduction to the rules for reading associations (p. 77).

### 6.2 Causal diagrams and marginal independence (pp. 77–79)
**Definitions (margin, p. 78).** A *path* connects two variables by a sequence of edges, visiting no variable twice. A path is *causal* if all arrows point the same way; otherwise it is *noncausal*.

**Fig. 6.2 (aspirin $A$ → heart disease $Y$, randomised).** Two variables linked only by a causal arrow are generally expected to be associated. In an ideal randomised experiment, $\Pr[Y^{a=1}=1]\ne\Pr[Y^{a=0}=1]$ implies $\Pr[Y=1|A=1]\ne\Pr[Y=1|A=0]$, and vice versa. Heuristic: associations flow along paths like pipes. Association is symmetric, so it flows in either direction along a path (p. 78).

**Fig. 6.3 (fork; lighter $A$, lung cancer $Y$, smoking $L$).** $L\to A$ and $L\to Y$; no $A\to Y$ arrow, so $\Pr[Y^{a=1}=1]=\Pr[Y^{a=0}=1]$ (p. 78). A naive investigator studies the lighter–cancer link. Take Hera, who carries a lighter. She is more likely to smoke, so she has a higher than average cancer risk. So $A$ and $Y$ are expected to be associated, $\Pr[Y=1|A=1]\ne\Pr[Y=1|A=0]$, although $A$ has no effect on $Y$. The investigator errs if he infers causation. In graph terms, association flows through the common cause $L$ (p. 79).

**Fig. 6.4 (collider; haplotype $A$, smoking $Y$, heart disease $L$).** $A\to L\leftarrow Y$. $L$ is a *collider* on this path because two arrowheads meet there. Learning that Apollo lacks the haplotype tells us nothing about his smoking, so $\Pr[Y=1|A=1]=\Pr[Y=1|A=0]$ and $A\perp\!\!\!\perp Y$. Causal graph theory says colliders, unlike other variables, block the flow of association on their path (p. 79).

**Summary.** Two variables are (marginally) associated if one causes the other or they share common causes. Otherwise they are (marginally) independent (p. 79).

*Intuition note.* Ask: "does knowing one variable help me predict the other?" A shared cause is a clue that links them. Two causes of a common effect, with no other link, are (marginally) independent: the effect does not by itself link them, although conditioning on it generally does.

### 6.3 Causal diagrams and conditional independence (pp. 80–81)
Boxes around nodes mean conditioning on them.

**Fig. 6.5 (chain; $A\to B\to Y$).** $B$ = platelet aggregation, a mediator. Restrict to $B=0$ (box on $B$). Treatment status adds no information about risk, because aspirin acts only through $B$. So $\Pr[Y=1|A=1,B=b]=\Pr[Y=1|A=0,B=b]$ for all $b$, i.e. $A\perp\!\!\!\perp Y\mid B$, even though $A$ and $Y$ are marginally associated. The box blocks the path $A\to B\to Y$ (p. 80). Margin note: in complete causal diagrams (all arrows present) no conditional independences are expected, so it is often said that "information about associations is in the missing arrows" (p. 80).

**Fig. 6.6 (fork, conditioning on $L$).** Among nonsmokers ($L=0$), carrying a lighter does not help predict cancer, because the prediction relied on lighter carriers being more likely to smoke. So $A\perp\!\!\!\perp Y\mid L$. The box on $L$ blocks $A\leftarrow L\rightarrow Y$. Margin note: this is the graph-based justification for stratification as a way to achieve exchangeability (p. 80).

**Fig. 6.7 (collider, conditioning on $L$).** Restrict to people with heart disease ($L=1$). Lacking haplotype $A$ makes it more likely that another cause of $L$, such as smoking $Y$, is present. So among people with heart disease, smokers are more frequent among those without the haplotype. $A$ and $Y$ are inversely associated given $L=1$. In the extreme, if $A$ and $Y$ were the only causes of $L$, then among the diseased the absence of one would perfectly predict the presence of the other. Conditioning on a collider opens the path $A\to L\leftarrow Y$ (p. 81). The investigator errs if he infers causation from this association (p. 81).

**Fig. 6.8.** A diuretic $C$ is a consequence of heart disease: $L\to C$. Conditioning on $C$, a descendant of the collider, also opens the path. It is blocked if neither the collider nor its consequence is conditioned on (p. 81).

**Three structural reasons for association** (pp. 79–81): one causes the other; they share common causes; they share a common effect and the analysis is restricted to a level of that effect or of its descendants (p. 81). A fourth source, chance, shrinks as the study grows. The chapter assumes a very large (perhaps hypothetical) population until Chapter 10 (p. 81). The arguments given are heuristic but have been formalised and proved (d-separation; Pearl 1995) (p. 81).

*Intuition note.* Conditioning on a common effect "selects" individuals whose causes must jointly explain that effect. If one cause is absent, another is more likely present. Two causes that were independent therefore generally become associated.

### Fine Point 6.1: d-separation (p. 82)
Rules for a path:
1. With no conditioning, a path is blocked if and only if two arrowheads collide at some variable on it. Example: in Fig. 6.1, $L\to A\to Y$ is open; $A\to Y\leftarrow L$ is blocked at the collider $Y$.
2. A non-collider that is conditioned on blocks the path (Fig. 6.5).
3. A collider that is conditioned on does not block the path (Fig. 6.7).
4. A collider with a conditioned-on descendant does not block the path (Fig. 6.8).

Summary: a path is blocked if and only if it contains a conditioned-on non-collider, or a collider that is not conditioned on and has no conditioned-on descendants. Variables are *d-separated* if all paths between them are blocked; otherwise *d-connected*. Sets are d-separated if every variable in one is d-separated from every variable in the other. Examples: $A$ and $L$ in Fig. 6.1 are not d-separated (open path $L\to A$). $A$ and $Y$ in Fig. 6.4 are d-separated (p. 82).

Link to statistics: Pearl (1988) proved that the causal Markov assumption implies the following. For disjoint sets $A,B,C$, if $A$ is d-separated from $B$ given $C$, then $A$ is statistically independent of $B$ given $C$. The converse is a separate assumption, *faithfulness*. Under faithfulness: $A\perp\!\!\!\perp Y\mid B$ in Fig. 6.5; $A$ is not independent of $Y$ given $L$ in Fig. 6.7, nor given $C$ in Fig. 6.8. An equivalent rule set, "moralization", is by Lauritzen et al. (p. 82).

### Fine Point 6.2: Faithfulness (p. 83)
- An arrow $A\to Y$ means $A$ affects $Y$ for at least one individual. We would generally expect a non-null average effect and association. But this is not necessarily true. Example: in the Table 4.1 data, transplant increases death risk in women and decreases it in men. These cancel exactly, so the average causal effect is null, yet Fig. 6.2 is still the correct diagram because $A$ affects every individual.
- *Faithfulness* (formal): for disjoint sets $A,B,C$ ($C$ may be empty), $A$ independent of $B$ given $C$ implies $A$ is d-separated from $B$ given $C$. When it fails, the distribution is "not faithful" to the DAG.
- Exact cancellation is rare, so faithfulness is assumed throughout, and lack of d-separation can almost always be equated with non-zero association.
- *Violation by design (matching).* Fig. 6.9: $L\to A$, $L\to Y$, $A\to Y$, $L\to S$, $A\to S$, with $S$ = selection into the matched cohort, boxed ($S=1$). D-separation gives two open paths $L\to A$ and $L\to S\leftarrow A$, so one would expect $L$ and $A$ associated. Matching ensures they are not. The association via $L\to S\leftarrow A$ has equal magnitude and opposite direction to that via $L\to A$, so they cancel. Matching leads to unfaithfulness.
- *Deterministic relations* between variables can also violate faithfulness: variables may be independent even if some paths are open. Faithfulness is also assumed in causal discovery (p. 83).

### 6.4 Positivity and consistency in causal diagrams (pp. 81–84)
- The Chapter 2 formulas (standardization, IP weighting) can also be derived with graph theory (the do-calculus). So the earlier choice of counterfactual theory did not really privilege one approach, only one notation (p. 82).
- Exchangeability, positivity and consistency are conditions required for causal inference via standardization or IP weighting, in either notation. Exchangeability is translated into graph language in the next sections and chapters (p. 82).
- **Positivity.** Graphs cannot encode violations of positivity except in special cases. Example: $A$ is a deterministic function of pretreatment $L$; then the $L\to A$ arrow is drawn in bold (pp. 82–83). Positivity is implicit in the book's diagrams unless stated.
- **Consistency**, first component (well-defined counterfactuals): the $A\to Y$ arrow corresponds to a possibly hypothetical but relatively unambiguous intervention. It is embedded in the notation because only treatment nodes with relatively well-defined interventions are considered. Positivity concerns arrows into treatment nodes; well-defined interventions concern arrows leaving them (p. 83).
- Treatment nodes thus have a different status. Some authors add decision nodes (influence diagrams, Dawid). The book does not, in this chapter, since interventions are explicit; SWIGs will give treatment nodes a special status. The earlier causal trees, sufficient-cause pies and Chapter 3 discussion also treated treatment variables differently (pp. 83–84).
- The apparently equal status of all nodes may be misleading. A node for "obesity" may be acceptable as an outcome or covariate, but generally not as a treatment (p. 84).
- **Fig. 6.10 (weight loss $A$, mortality $Y$).** Arrows: $L\to A$, $L\to Y$, $Z\to A$, $U\to A$, $U\to Y$ (no $A\to Y$ arrow is drawn in the figure as printed). $Z$ = caloric intake (assumed to affect mortality only through weight loss), $L$ = exercise (can affect mortality by other pathways), $U$ = genetic traits (other pathways, independent of weight loss). Some of the several ways to intervene on $A$ have direct effects on $Y$, so "the effect of $A$ on $Y$" is unclear: reducing weight via $Z$, $L$ or $U$ gives different mortality risks. Identifying variables for exchangeability would also be formidable. Being explicit about the intervention is a step toward a well-defined effect, relevant data and adjustment variables (p. 84).

### Fine Point 6.3: Discovery of causal structure (p. 85)
- *Discovery* = learning causal structure from data. It is sometimes possible under faithfulness, often impossible.
- A strong $B$–$C$ association fits $B\to C$, $C\to B$, a common unmeasured cause, a conditioned-on common effect, and combinations. Time order only rules out one direction.
- Example: $Z, A, Y$ in time order. Suppose, with infinite data, all three are marginally associated and the only conditional independence is $Z\perp\!\!\!\perp Y\mid A$. Under faithfulness, the only consistent DAG is $Z\to A\to Y$, possibly with a common cause $U_1$ of $Z$ and $A$ (in addition to, or in place of, $Z\to A$). A direct $Z$–$Y$ link, a shared cause $U_2$, or a common cause $U_3$ of $A$ and $Y$ would each destroy that independence. So $A\to Y$ must exist.
- Conclusions: $Z$ is not a parent of $Y$; there is no unmeasured common cause of $A$ and $Y$; $E[Y|A=1]-E[Y|A=0]$ identifies the average causal effect because exchangeability holds. The finite-sample case is deferred to Technical Point 10.7 (p. 85).
- If an unmeasured common cause of $A$ and $Y$ existed, no conditional independence would be found, and we could not tell whether $A$ causes $Y$ (p. 85).

### 6.5 A structural classification of bias (pp. 85–87)
- *Systematic bias*: the data are insufficient to identify the causal effect even with infinite sample size. No estimator can then be consistent. Informally: structural association between treatment and outcome that does not arise from the causal effect in the population of interest (p. 85).
- *(Unconditional) bias*: $\Pr[Y^{a=1}=1]-\Pr[Y^{a=0}=1]\ne\Pr[Y=1|A=1]-\Pr[Y=1|A=0]$. This is the case when $Y^a\perp\!\!\!\perp A$ does not hold. Absence of such bias implies that the association measure is a consistent estimate of the corresponding effect measure (p. 86).
- *Bias under the null*: lack of exchangeability makes $A$ and $Y$ associated even when treatment has no effect. In the Table 3.1 observational study the causal risk ratio was 1 and the associational risk ratio 1.26. Any structure that gives bias under the null also gives bias under the alternative; the converse is not true. Margin: conditioning on some variables may cause selection bias off the null but not under the null (Greenland 1977; Hernán 2017) (p. 86).
- *Conditional bias*: $\Pr[Y^{a=1}=1|L=l]-\Pr[Y^{a=0}=1|L=l]$ differs from $\Pr[Y=1|L=l,A=1]-\Pr[Y=1|L=l,A=0]$ for at least one stratum $l$. This is generally the case when $Y^a\perp\!\!\!\perp A\mid L=l$ does not hold for all $a$ and $l$ (p. 86).
- Lack of exchangeability can arise from two structures (p. 86):
  1. Common causes: association measure generally differs from effect measure; epidemiologists often call this *confounding* (Chapter 7).
  2. Conditioning on common effects: what many call *selection bias under the null* (Chapter 8).
- Chapter 9 covers *measurement (information) bias*; some types also cause bias under the null. These biases may arise in randomised experiments as well as observational studies. The earlier idealised randomised experiments (no loss, full adherence, concealed assignment) were a teaching device, "quasi-mythological" (pp. 86–87).

### 6.6 The structure of effect modification (pp. 87–88)
- DAGs are good for finding sources of bias, less helpful for effect modification (p. 87).
- Randomised heart transplant, no bias (Fig. 6.2 valid); association is causation. Investigators suspect the effect varies with hospital care quality $V$ (1 high, 0 normal) and find effect modification on the additive scale. Fig. 6.12 adds $V\to Y$, with no arrow into $A$ (random assignment) (p. 87).
- **Caveat 1.** Fig. 6.12 would still be valid without $V$, since $V$ is not a common cause of $A$ and $Y$. $V$ is included only because the question is the effect within levels of $V$. Other variables along the path from $V$ to $Y$ can also be effect modifiers, e.g. $N$ = "therapy complications" in Fig. 6.13 ($V\to N\to Y$ plus $V\to Y$), which partly mediates $V$'s effect (p. 87).
- **Caveat 2.** The diagram does not show whether $V$ modifies the effect. It does not distinguish three ways: same direction in both strata; opposite direction (qualitative effect modification); effect in one stratum only (e.g. $A$ only kills those with $V=0$) (p. 87).
- *Surrogate effect modifiers* (p. 88): many effect modifiers do not affect the outcome and merely stand in for variables that do. Fig. 6.14: $S$ = treatment cost, caused by $V$ and with no effect on $Y$. Stratifying by $S$ (not $V$) will generally detect modification by $S$. $S$ is a *surrogate* effect modifier; $V$ is a *causal* effect modifier. The concept of effect modification includes both, since they are often indistinguishable in practice. Some prefer "heterogeneity of causal effects". A statement like "cost modifies the effect" might wrongly be read as an argument to raise prices (p. 88).
- A surrogate is any variable associated with the causal effect modifier. The association can come from (p. 88):
  - cause and effect (Fig. 6.14);
  - a common cause: Fig. 6.15, $U$ = place of residence (Greece/Rome) causes both $V$ and $P$ = passport nationality, so $P$ acts as a surrogate;
  - conditioning on a common effect: Fig. 6.16, $W$ = bottled mineral water use affects cost $S$ but not mortality, and $V\to S$. In low-cost hospitals ($S=0$) $W$ is generally associated with $V$. The margin gives the intuition: low-cost hospitals using mineral water must save elsewhere, so $W$ is inversely associated with care quality.
- Causal diagrams are in principle agnostic about interaction between treatments $A$ and $E$. They can encode information about it when augmented with sufficient-component-cause nodes (Chapter 5) with deterministic arrows from the treatments. Because interaction affects the association from conditioning on common effects, these are discussed in Chapter 8 (p. 88).

### Fine Point 6.4: Non-intervention variables revisited (p. 89)
- *Setting.* Drug $Z$, systolic blood pressure $A$ (a state), stroke $Y$. Suppose (i) $Z$ is associated with $A$ and $Y$; (ii) $A$ and $Y$ are associated; (iii) $Z\perp\!\!\!\perp Y\mid A$. Under faithfulness, the only DAG has $A\to Y$, no $Z\to Y$, and no unmeasured common causes of $A,Y$ or $Z,Y$. If $Y^a$ were well defined, we could conclude under faithfulness (a) no unmeasured common cause $U$ of $A$ and $Y$, (b) $Y^a\perp\!\!\!\perp A$, (c) the effect equals $E[Y|A=1]-E[Y|A=0]$, (d) $Z$ or $U_1$ (or both) in Fig. 6.11 affect $Y$ only through $A$. An investigator who doubted $Y^a$ is well defined might take (i)–(iii) as strong empirical evidence for it. If (i)–(iii) hold only given a baseline covariate $L$, then (b) and (c) become the conditional versions.
- *Usual problem.* Typically unmeasured common causes $U_3$ of $A$ and $Y$ remain. Then (iii) fails, because $Z$ and $Y$ are associated given the collider $A$. The $Z\to Y$ arrow cannot be removed, and the data give no empirical support for well-defined $Y^a$.
- *Dose-finding trial* (can still give such evidence, under faithfulness). Individuals are randomised to one of two drugs ($Z=1,2$) and one of two blood-pressure reductions ($A=a_1,a_2$). The daily dose $D$ is raised until the assigned reduction is reached. Assumptions: every individual reaches the assigned reduction, the dose keeps it, and the dose-finding period has no effect on $Y$.
- *Result.* If $E[Y|D=2,A]=E[Y|D=1,A]=E[Y|A]$ and $E[Y|A=a_1]\ne E[Y|A=a_2]$, then under faithfulness (assuming $Y^{d,a}$ and $Y^a$ well defined) $D$ has no direct effect on $Y$ not through $A$. Also $E[Y^{a_1}-Y^{a_2}]$ is identified by $E[Y|A=a_1]-E[Y|A=a_2]$, whether or not unknown common causes $U$ of $A$ and $Y$ exist.
- *Why.* In the standard trial (Fig. 6.17), $Z\to A$, $D\to A$, $U\to A$, $U\to Y$, $A\to Y$, with dotted arrows $Z\to Y$ and $D\to Y$. Because $Y$ and $Z$ are associated given $A$, we cannot tell whether the dotted arrows exist. In the dose-finding trial (Fig. 6.18), $A$ equals the assigned value $A_{ass}$, a deterministic function (bold arrow), so the only arrow into $A$ is from $A_{ass}$. $D$ is determined by $A_{ass}$, $Z$ and $U$. Under faithfulness, independence given $A$ holds if and only if there is no direct effect not through $A$; the text states this for $Z$. Since $E[Y|A=a_1]\ne E[Y|A=a_2]$, an $A\to Y$ arrow must exist. The investigator may take its necessity as strong empirical evidence that $Y^a$ is well defined (p. 89).

Page 90 contains no content (only a running header).

## Toy example (ours, not from the text)
**Collider.** Let $A$ and $Y$ be independent fair coins ($0/1$, each outcome with probability 1/2). Let $L=1$ if $A=1$ or $Y=1$, else $L=0$. So $A\to L\leftarrow Y$. The four $(A,Y)$ combinations each have probability 1/4.
- Marginal: $\Pr[Y=1|A=1]=1/2$ and $\Pr[Y=1|A=0]=1/2$. So $A\perp\!\!\!\perp Y$; the collider blocks the path.
- Condition on $L=1$: the combinations $(0,1),(1,0),(1,1)$ remain, each with probability $(1/4)/(3/4)=1/3$.
  - $\Pr[Y=1|A=1,L=1]=\Pr(1,1)/[\Pr(1,0)+\Pr(1,1)]=(1/3)/(2/3)=1/2$.
  - $\Pr[Y=1|A=0,L=1]=\Pr(0,1)/\Pr(0,1)=1$.
  - Since $1/2\ne1$, $A$ and $Y$ are associated given $L=1$, inversely (absent $A$ makes $Y$ more likely).

**Fork.** $L\in\{0,1\}$ with probability 1/2 each. $\Pr[A=1|L=1]=0.8$, $\Pr[A=1|L=0]=0.2$. $\Pr[Y=1|L=1]=0.9$, $\Pr[Y=1|L=0]=0.1$, with $A,Y$ independent given $L$ (no $A\to Y$ arrow).
- $\Pr[A=1]=0.5(0.8)+0.5(0.2)=0.5$. $\Pr[L=1|A=1]=0.4/0.5=0.8$.
- $\Pr[Y=1|A=1]=0.8(0.9)+0.2(0.1)=0.74$.
- $\Pr[L=1|A=0]=0.1/0.5=0.2$, so $\Pr[Y=1|A=0]=0.2(0.9)+0.8(0.1)=0.26$.
- $0.74\ne0.26$: marginal association with no causal effect. Given $L=l$, both risks equal $0.9$ ($l=1$) or $0.1$ ($l=0$): conditional independence.

## Concepts
- [[causal-dag]] — DAG whose arrows are direct causal effects; no arrow means no direct effect; all common causes included (pp. 75–76)
- [[causal-markov-assumption]] (new) — given its parents, a variable is independent of its non-descendants; links graph to data (p. 76)
- [[structural-causal-model]] — here the NPSEM/FCISTG/FFRCISTG family: parents plus error give one-step-ahead counterfactuals (pp. 77–78)
- [[fork-chain-collider]] — common cause, mediator, common effect; colliders block unless conditioned on (pp. 78–81)
- [[d-separation]] — four path-blocking rules; with causal Markov, d-separation implies independence (p. 82)
- [[faithfulness]] (new) — independence implies d-separation; fails with exact cancellation, matching, deterministic arrows (pp. 82–83)
- [[confounding-vs-selection-bias]] — bias from common causes vs from conditioning on common effects; both are bias under the null (p. 86)
- [[systematic-bias]] (new) — structural association not due to the causal effect; remains with infinite data (p. 85)
- [[bias-under-the-null]] (new) — treatment and outcome associated although there is no causal effect (p. 86)
- [[effect-modification]] (new) — effect varies across levels of $V$; causal versus surrogate modifiers (pp. 87–88)
- [[positivity-and-consistency]] (new) — conditions beyond exchangeability; graphs encode positivity violations only in special cases (pp. 82–83)
- [[assignment-mechanism-ignorability]] — willingness to treat Fig. 6.1 as the diagram of an observational study is the graphic translation of conditional exchangeability given $L$ (p. 76)

## Canonical instances
- [[lighter-lung-cancer-fork]] — $A\leftarrow L\to Y$: association without causation (pp. 78–80)
- [[haplotype-smoking-collider]] — $A\to L\leftarrow Y$: independent marginally, associated given $L$ or its descendant $C$ (pp. 79–81)
- [[aspirin-platelet-chain]] — conditioning on a mediator blocks the path (p. 80)
- [[transplant-sex-cancellation]] — Table 4.1 data: unfaithfulness from exactly cancelling effects (p. 83)
- [[matched-study-unfaithfulness]] — Fig. 6.9, matching cancels two association paths (p. 83)
- [[weight-loss-ill-defined-intervention]] — Fig. 6.10, several ways to intervene on $A$ (p. 84)
- [[dose-finding-trial]] — Fig. 6.18, evidence for well-defined $Y^a$ (p. 89)
- [[surrogate-effect-modifier-examples]] — cost $S$, nationality $P$, mineral water $W$ (p. 88)

## Bridges (candidates)
- [same-math] Markov factorization $f(v)=\prod_j f(v_j\mid pa_j)$ ↔ Bayesian: factorisation of a joint distribution in a directed graphical model (Bayesian network) — same product of conditionals.
- [structural-analogy] Conditioning on a collider creates dependence between causes ↔ Bayesian: "explaining away" in posterior inference — learning the effect couples its independent causes.
- [structural-analogy] Faithfulness (no exact cancellation) ↔ Bayesian: a prior giving probability zero to parameter values that produce exact cancellation — both rely on "generic" parameters.
- [structural-analogy] Matching/selection $S=1$ as conditioning on a collider ↔ Bayesian: conditioning on observed data that depend on several unknowns — the selection event induces dependence.

## Questions this raises
- How exactly are confounding (common causes) and selection bias (conditioning on common effects) removed or avoided in practice (Chapters 7–8)?
- What does a SWIG add that an ordinary DAG lacks, and how does it express exchangeability?
- If graphs cannot encode positivity violations or effect-modification type, what else must be stated outside the graph?
- How reliable is causal discovery with finite samples (Technical Point 10.7)?

## Reading notes
- Printed page = pdf page − 9 (pdf 84 = printed 75). Printed page 90 is blank except for the running header.
- The source is the online revision dated 2026-08-19, not the 2020 print edition (per the unit metadata).
- Equations were checked against the page images; the text layer garbles some superscripts and subscripts in Technical Points 6.2–6.3. As printed, Fig. 6.10 shows no $A\to Y$ arrow. The only displayed equation is the Markov factorization in Technical Point 6.1.
- Fine Point 6.4: the observed independence is stated for $D$ given $A$ and the conclusion is about $D$, but the "Under faithfulness, $Z$ is independent of $Y$ given $A$…" sentence refers to $Z$. I report it as printed; the intended variable is not verified here.
- Fine Point 6.4 refers to "Figure 6.11" with $Z$ and $U_1$ as printed; Fig. 6.11 is drawn on p. 85, beside the start of Section 6.5 (Fine Point 6.3 on that page also refers to it).
- In Fine Point 6.2 the heart-transplant example relies on "Table 4.1" (not in this unit).
