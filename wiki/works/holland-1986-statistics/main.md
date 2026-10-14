---
id: holland-1986-statistics/main
work: holland-1986-statistics
unit: paper
pages: 945–960
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Statistics and Causal Inference (Holland 1986)

## L0 — One line
Causal effects are defined as the difference between a unit's two potential responses (one per cause), only one of which can ever be observed, so every causal inference rests on untestable assumptions.

## L1 — The gist (≤ 120 words)
Can statistics say anything about causation? Holland uses Rubin's model. Each unit has two potential responses, one per cause. The causal effect on a unit is their difference. Only one response can be observed per unit (the Fundamental Problem), so causal inference needs untestable assumptions. The "scientific" solution assumes homogeneity or stability. The "statistical" solution estimates an average effect, with randomization making the needed independence assumption plausible. Holland then uses the model to read, and in places criticize, Hume, Mill, Suppes, Cox, Fisher, Neyman, Koch, Hill, Granger and path-diagram modelers. His conclusions: study effects of causes, not causes of effects; an effect is always relative to another cause; attributes of units are never causes.

**Prerequisites:** populations as sets of units; averages and conditional averages (conditional expectation); independence and conditional independence; the idea of a randomized experiment.

## L2 — Key ideas (5–10 bullets)
- Association is descriptive. It concerns the joint distribution of variables over a population, where "probability" is just a proportion of units (pp. 945–946).
- Causation needs more structure. Each unit must be potentially exposable to each cause, and the response has two versions, $Y_t$ and $Y_c$. Only $Y_S$ (the response under the cause $S$ that the unit actually received) is observed (pp. 946–948).
- The Fundamental Problem: $Y_t(u)$ and $Y_c(u)$ cannot both be observed on one unit. It does not make causal inference impossible; it makes it depend on untestable assumptions (pp. 947, 959).
- Two solutions: the scientific one (assumptions of stability, transience or unit homogeneity, which let one measure both responses on one unit or treat two units as identical) and the statistical one (estimate $T=E(Y_t)-E(Y_c)$). The prima facie effect $T_{PF}$ (the raw difference between the average observed responses of the $t$ group and the $c$ group) equals $T$ under independence, which randomization makes plausible (pp. 947–949).
- Hume, Mill, Suppes, Granger and Hill all fit partly into the model. Holland says Hume lacks the idea of an effect relative to another cause (Mill comes closer to it), and that Suppes's and Granger's genuine causes stay open to revision; for Hill, some factors map onto the model and others do not (pp. 950–958).
- Multiple versions of the response were already used by Kempthorne, Cox and Neyman. The Fisher–Neyman dispute is about null hypotheses: zero effect on every unit versus zero average effect (pp. 953–954).
- Holland takes the position that only things that could in principle be treatments in an experiment are causes, so attributes are not (his motto: "NO CAUSATION WITHOUT MANIPULATION") (pp. 954–955, 959).
- Holland holds that some path diagrams are meaningful and some are not (an attribute pointing to a response is meaningless); the meaningful ones can be read in terms of causes and responses in the model (p. 958).

## L3 — Walkthrough

### 1. Introduction (p. 945)
- Many statisticians react to causation talk by denying that statistics can contribute. Holland cites Barnard, who says that correlation not being causation is perhaps the first thing that must be said, as an example of this reaction (p. 945).
- Holland replies that randomized experiments are a powerful aid to causal investigation, and their early proponents founded modern statistics (p. 945).
- Thesis: statistics has much to say about certain causal problems. Models for causal inference differ distinctly from models for association (p. 945).
- Several different questions hide under "causation": the meaning of the notion, the causes of a given effect, and causal mechanisms. Holland stresses the **effects of causes**, because this seems to be a place where statistics, which is concerned with measurement, has contributions to make. He says this emphasis directly opposes more traditional analyses (p. 945).

### 2. Model for associational inference (pp. 945–946)
- **Units** form a population $U$ (people, equipment, households, plots). A **variable** is a real-valued function defined on every unit. Units and variables are primitives (p. 945).
- $Y$ is the *response variable*, the variable to be explained. $A$ is an *attribute*. Logically $A$ and $Y$ are on an equal footing (p. 945).
- All probabilities, distributions and expectations are computed over $U$. A probability is a proportion of units. An expected value is an average over $U$. A conditional expectation is an average over a subset of units (p. 945). This is why these are "population models".
- For associational inference, time only helps define the population or the operational meaning of a variable; in causal inference its role is greater (pp. 945–946).
- Joint distribution: $\Pr(Y=y, A=a)$ = proportion of $u$ with $Y(u)=y$ and $A(u)=a$. Conditional distribution: $\Pr(Y=y\mid A=a)=\Pr(Y=y,A=a)/\Pr(A=a)$. A typical associational parameter is the regression $E(Y\mid A=a)$ (p. 946).
- Associational inference means estimates, tests and posterior distributions about such parameters from data on units of $U$. It is "simply descriptive statistics" (p. 946).

### 3. Rubin's model for causal inference (pp. 946–948)
- Holland draws on the language of experiments because an experiment is the simplest setting for causation. He does not claim it is the only one (p. 946). The model is a simplified, population-level version of Rubin's (Rubin 1974 onward) (p. 946).
- The effect of a cause is always relative to another cause. "A causes B" almost always means relative to a cause including "not A". Holland therefore uses *treatment* ($t$) versus *control* ($c$) (p. 946).
- Each unit must be **potentially exposable** to any of the causes, even if this is impracticable. Schooling can be a cause of test performance. Race or gender cannot (p. 946).
- $S$ indicates the cause to which a unit is exposed. In a controlled study the experimenter constructs $S$. In an uncontrolled study, factors beyond control partly determine $S$. In both, $S(u)$ *could have been different*. By contrast, an attribute $A(u)$ could not have been different (p. 946).
- Variables split into **pre-exposure** (determined before exposure) and **post-exposure**. The response $Y$ measures the effect, so it is post-exposure. Hence there are two potential responses $Y_t(u)$ and $Y_c(u)$, the values observed if $u$ were exposed to $t$, or on the same unit to $c$ (p. 946).
- Notation: a post-exposure measurement applies to the pair $(u,t)$ or $(u,c)$, so $Y_t(u)=Y(u,t)$ and $Y_c(u)=Y(u,c)$ (p. 947).
- **Causal effect** of $t$ (relative to $c$) on $u$, as measured by $Y$:
$$Y_t(u)-Y_c(u). \tag{1}$$
 Equivalently: $t$ causes the effect $Y_t(u)-Y_c(u)$ on $u$ (relative to $c$) (p. 947), written (2).
- **Fundamental Problem of Causal Inference:** it is impossible to observe $Y_t(u)$ and $Y_c(u)$ on the same unit, hence impossible to observe the effect of $t$ on $u$. The emphasis is on *observe* (p. 947).
- Examples: a fourth grader given a new versus standard arithmetic program (only one can be observed). A light switch ($t$ = flick, $c$ = do not): one may believe both are known, but only because of plausible assumptions. If the light was flickering by itself, the belief fails (p. 947).
- This does not mean knowledge is absent or causal inference impossible. There are two general solutions (p. 947).
- **Scientific solution:** use homogeneity or invariance assumptions. A scientist may believe an earlier $Y_c(u)$ equals the current $Y_c(u)$, then expose $u$ to $t$ and measure $Y_t(u)$. The assumption is untestable. Careful work can convince people but never give certainty. Everyday causal inference works this way (p. 947).
- **Statistical solution:** the **average causal effect** over $U$ is
$$E(Y_t-Y_c)=T, \tag{3}$$
$$T=E(Y_t)-E(Y_c). \tag{4}$$
 By (4), units exposed to $t$ inform $E(Y_t)$ and units exposed to $c$ inform $E(Y_c)$. How units are chosen for $t$ or $c$ is very important and involves all the usual considerations of experimental design. The impossible-to-observe unit effect is replaced by the possible-to-estimate average effect (p. 947).
- The usefulness of each solution depends on the truth of its own set of untestable assumptions (p. 947).
- **Observed response:** $S(u)=t$ means $Y_t(u)$ is observed, and $S(u)=c$ means $Y_c(u)$ is observed. So the observed response on $u$ is $Y_{S(u)}(u)$, and the observed response variable is $Y_S$. The model has three variables $S, Y_t, Y_c$, but observation involves only $(S, Y_S)$ (pp. 947–948).
- Holland separates (a) the measurement process $Y$, (b) the two versions $Y_t, Y_c$ in terms of which effects are defined, and (c) the observed $Y_S$. This is rarely done in discussions of causation. The distinctions never arise in simple association but are crucial for causation (p. 948).
- Side by side. Both models have a population $U$ and two observable variables: $(A,Y)$ for association and $(S,Y_S)$ for causation. For causation, two or more causes must be exposable to all units, and $Y$ must be post-exposure. Causal inference concerns $Y_t(u)-Y_c(u)$ on individual units. It starts from observed $(S,Y_S)$ plus usually untestable assumptions. It does not necessarily involve statistical inference, whereas associational inference almost always does (p. 948).

*Intuition note.* Each unit carries two "what-if" outcomes, but the world shows us only one of them. Averaging over many units, under suitable assumptions such as independence, lets us estimate the average difference, even though the unit-level difference stays hidden.

### 4. Some special cases of causal inference (pp. 948–949)

**4.1 Temporal stability and causal transience (p. 948).**
- Scientific solution, version 1. (a) *Temporal stability*: $Y_c(u)$ does not depend on when the sequence of applying $c$ to $u$ and then measuring $Y$ occurs. (b) *Causal transience*: the effect of $c$ and its measurement is transient and does not change $u$ enough to affect $Y_t(u)$ measured later.
- If both are plausible, expose $u$ to $c$ then $t$, measuring $Y$ after each. This is routine for physical devices (the light switch) (p. 948).

**4.2 Unit homogeneity (p. 948).**
- Assume $Y_t(u_1)=Y_t(u_2)$ and $Y_c(u_1)=Y_c(u_2)$ for two units. The causal effect is then taken to be $Y_t(u_1)-Y_c(u_2)$.
- Careful preparation so units "look" identical cannot prove homogeneity but can make it plausible (p. 948).

**4.3 Independence (pp. 948–949).**
- Statistical solution: the population is "large". The data are $(S,Y_S)$. The data can only inform
$$E(Y_S\mid S=t)=E(Y_t\mid S=t) \tag{5}$$
$$E(Y_S\mid S=c)=E(Y_c\mid S=c). \tag{6}$$
- $E(Y_t)$ and $E(Y_t\mid S=t)$ are not in general equal. The first averages over all of $U$, the second only over units exposed to $t$. Example: if $S(u)=t$ for all units with small $Y_t(u)$, then $E(Y_t\mid S=t)$ is smaller than $E(Y_t)$ (p. 948).
- **Independence assumption:** under correct physical randomization it is plausible that $S$ is statistically independent of $Y_t$, $Y_c$ and all other variables over $U$ (p. 948). Then
$$E(Y_t)=E(Y_t\mid S=t) \tag{7}$$
$$E(Y_c)=E(Y_c\mid S=c) \tag{8}$$
$$T=E(Y_S\mid S=t)-E(Y_S\mid S=c). \tag{9}$$
 So $T$ is estimated by the difference of observed averages in the two groups. If randomization is possible, $T$ can always be estimated, with high accuracy if $U$ is large (p. 949).
- **Prima facie causal effect** (named after Suppes):
$$T_{PF}=E(Y_t\mid S=t)-E(Y_c\mid S=c), \tag{10}$$
$$T_{PF}=E(Y_S\mid S=t)-E(Y_S\mid S=c). \tag{11}$$
 It is an associational parameter of the joint distribution of $(Y_S,S)$. In general $T\neq T_{PF}$. Independence gives $T=T_{PF}$, which is (9) (p. 949).

*Intuition note.* The raw difference of group averages ($T_{PF}$) compares different units. Randomization makes the two groups alike on average, so that raw difference estimates the causal effect.

**4.4 Constant effect (p. 949).**
- $T$ is an average and has the usual drawbacks. If effects $Y_t(u)-Y_c(u)$ vary a lot, $T$ may represent a specific unit $u_0$ poorly, however carefully estimated (p. 949).
- **Constant effect** (called *additivity* in statistical models for experiments): 
$$T=Y_t(u)-Y_c(u)\quad\text{for all }u\in U. \tag{12}$$
 Then $T$ is relevant to every unit (p. 949).
- Partial check: split $U$ into subpopulations $U_i$, estimate $T_i$ on each. If the $T_i$ vary, constant effect cannot hold. If they do not vary, it may be plausible (p. 949).
- Unit homogeneity implies constant effect, so constant effect is a weakening of unit homogeneity (p. 949).
- Constant effect alone does not let us conclude that $T_{PF}=T$. Under it, $Y_t(u)=Y_c(u)+T$ (13), so $E(Y_t\mid S=t)=T+E(Y_c\mid S=t)$ (14), and
$$T_{PF}=T+\{E(Y_c\mid S=t)-E(Y_c\mid S=c)\}. \tag{15}$$
 The braces term is not 0 in general, i.e. if independence fails. Unit homogeneity does imply $T=T_{PF}$ ("easy to show") (p. 949).

**4.5 Nonrandomized observational studies (p. 949).** Beyond the article's scope. Holland refers the reader to Rubin, Rosenbaum and Rubin, and Holland and Rubin. Their emphasis is on using pre-exposure variables to replace independence by weaker conditional independence assumptions, one called "strong ignorability" (p. 949).

### 5. Comments on selected philosophers (pp. 949–953)
- Aristotle's four causes (material, formal, efficient, final). Efficient cause is the relevant one. Locke's definition of cause and effect suggests only that the model is not out of line with an ancient philosophical tradition. Aristotle stresses causes of things; Locke seems a little more even-handed (pp. 949–950).

**5.1 Hume (p. 950).**
- Hume: causation is a relation between experiences. It is not empirically verifiable that the cause produces the effect, only that the cause-event is invariably followed by the effect-event. Holland sees this as sympathetic to statistics inferring unobserved quantities from observed facts. Hume was clear about untestable assumptions (p. 950).
- Hume's criteria: (a) spatial/temporal contiguity, (b) temporal succession, (c) constant conjunction ($A$ and $B$ always occur or do not occur together) (p. 950).
- In the model: contiguity is met because cause and effect act on a common unit. Temporal succession is built into the definition of a response variable. An effect preceding a cause is meaningless in the model, and apparently also to Hume (p. 950).
- Constant conjunction can fail in two ways: measurement error in causes or response, and (more fundamentally) failure of constant effect, i.e. effects $Y_t(u)-Y_c(u)$ vary with $u$. Disregarding measurement error, Hume's third criterion requires the constant effect assumption in the model. Hume would probably say that weakening it admits cases he would not call causation (p. 950).
- Holland's criticisms: Hume lacks the notion that an effect is relative to another cause, does not delineate causes (anything can be a cause for him), and does not link experiments to causation (p. 950).

**5.2 Mill (pp. 950–951).** Mill (1843) favored experiments. Holland's reading of four methods:
- *Concomitant variation*: Mill's statement that a co-varying phenomenon is a cause, an effect, or connected through causation runs against Holland's distinction between association and causation. Holland thinks most scientists would agree that correlational smoke is likely to mean causational fire, but most would not go as far as Mill's statement. The correlation of $Y_S$ and $S$ is just another expression of $T_{PF}$. Applied to attributes, the method can give nonsense (pp. 950–951).
- *Difference*: Holland calls it almost an exact statement of causal effect. Take $Y=1$ (0) if the phenomenon occurs (not), $t$ = circumstance present, $c$ = absent, same unit to model all other circumstances being equal. Then $Y_t(u)=1$, $Y_c(u)=0$, and the effect is 1 (p. 951).
- *Residues*: let $a$ be antecedents with known effect and $b$ the rest. The residue is the causal effect of $ab$ relative to $a$, $Y_{ab}(u)-Y_a(u)$. Holland regards it as a nearly explicit, early statement of causal effect (p. 951).
- *Agreement*: it really only rules out possible causes. If the phenomenon occurs under both $t$ and $c$, then $Y_t(u)=1=Y_c(u)$ and $Y_t-Y_c=0$: $t$ is a cause with a **null effect**. Holland notes that every effect having a cause does not imply that every cause has an effect, since experiments fail (p. 951).
- Conclusion: Mill, driven by an experimental model, is close to the model and to relativity of effects, unlike Hume. Like Hume he places no restriction on what can be a cause and does not seriously consider variation (unit inhomogeneity or variable effects) (p. 951).

**5.3 Suppes (pp. 951–953).**
- Suppes (1970) aims to improve on Hume's constant conjunction. Causes and effects are only restricted to be events in time, formalized with stochastic processes. Roughly: the first event is a cause if it is followed with high probability by the second and no third event factors out the relationship (p. 951).
- Suppes's definitions (all conditioning events have positive probability) (p. 952):
 - (S1) For $r<s$, $C_r$ is a **prima facie cause** of $E_s$ if $\Pr(E_s\mid C_r)>\Pr(E_s)$. (16)
 - (S2) $C_r$ is a **spurious cause** of $E_s$ if it is a prima facie cause and for some $q<r<s$ there is an event $D_q$ with
 $$\Pr(E_s\mid C_r,D_q)=\Pr(E_s\mid D_q) \tag{17}$$
 and
 $$\Pr(E_s\mid C_r,D_q)\ge\Pr(E_s\mid C_r). \tag{18}$$
 - (S3) $C_r$ is a **genuine cause** if prima facie and not spurious.
- Holland's critique: Suppes defines the cause of an effect, not the effect of a cause. Units are buried in the probability space. His model describes average, not individual, behavior. A genuine cause is a correlation that will not vanish by "partialling out" competing causes. So, in a sense, genuine causes are only temporarily so, awaiting a cleverer conditioning event. Holland says that, although this may describe much informal scientific practice, it does not appear to him to get to the heart of causation, which he believes Rubin's model does (p. 952).
- Translation into the model. $T_{PF}$ (19) is the association between $Y_S$ and $S$. It is a causal effect under conditions common in science, but not always, hence "prima facie" (p. 952).
- Spurious cause in a randomized experiment. Let $Y$ be 0/1, $\{Y_S=1\}$ play $E_s$, $\{S=t\}$ play $C_r$, and $D_q$ be an event determined by pre-exposure variables. (17) reads
$$\Pr(Y_S=1\mid S=t,D_q)=\Pr(Y_S=1\mid D_q). \tag{20}$$
 By the usual conditional-probability rules, (20) is equivalent to
$$\{\Pr(Y_t=1\mid S=t,D_q)-\Pr(Y_c=1\mid S=c,D_q)\}\times\Pr(S=c\mid D_q)=0. \tag{21}$$
 (added step: $\Pr(Y_S=1\mid D_q)$ is a mixture over $S$, so the left side of (20) minus the right side equals the braces term times $\Pr(S=c\mid D_q)$.) So either
$$\Pr(S=t\mid D_q)=1 \tag{22}$$
 or
$$\Pr(Y_t=1\mid S=t,D_q)=\Pr(Y_c=1\mid S=c,D_q). \tag{23}$$
- Assume independence and
$$0<\Pr(S=t)<1. \tag{24}$$
 Then (22) cannot hold, and (17) reduces to
$$\Pr(Y_t=1\mid D_q)=\Pr(Y_c=1\mid D_q), \tag{25}$$
 i.e.
$$T(D_q)=E(Y_t-Y_c\mid D_q)=0, \tag{26}$$
 the average causal effect over units for which $D_q$ occurs. So (17) becomes $T(D_q)=0$ (27) (p. 952).
- Inequality (18) is equivalent to $\Pr(Y_S=1\mid S=t,D_q)\ge\Pr(Y_S=1\mid S=t)$ (28). Under randomization it becomes $\Pr(Y_t=1\mid D_q)\ge\Pr(Y_t=1)$ (29) (p. 953).
- Holland's conclusion: in a randomized experiment, $t$ is a spurious cause if and only if it has a positive average causal effect but a subpopulation can be identified from pre-exposure variables on which (a) the average effect is 0 and (b) the response under $t$ is more likely than over all of $U$. Holland thinks part (a) is better described as a null effect in the subpopulation, and (b) is unrelated to cause. This is nonconstant conjunction in Hume's sense, called an *interaction* by most statisticians (p. 953).

*Intuition note.* In an experiment, Suppes's "spurious cause" does not mean the treatment has no effect. It means (given a positive overall effect) that the effect is zero in some subgroup identifiable from pre-exposure variables, on which the response under $t$ is also more likely than over all of $U$. Holland notes that most statisticians would call a null-effect subgroup with a positive overall effect an interaction.

### 6. Comments from a few statisticians (pp. 953–954)
- Holland looks for earlier statements of multiple versions of the response. The idea is never stated explicitly, so he does "detective work" and hopes not to misread others (p. 953).
- **Kempthorne (1952)**, randomized block designs (blocks divided into plots, treatments applied at random to plots). He writes $y_{ijk}$ for the yield of treatment $k$ on plot $j$ of block $i$. In Holland's translation: units are plots $u_{ij}$; $y_{ijk}=Y_k(u_{ij})$; randomization picks $S(u_{ij})=k$; observed yield $y_{ijS(u_{ij})}=Y_{S(u_{ij})}(u_{ij})$. With $j_k$ the plot of block $i$ receiving $k$, $y_{ik}=Y_k(u_{ij_k})$ (p. 953).
- **Cox (1958)** defines true treatment effects as the difference between the observation obtained when $T_1$ is applied and the one that would have been observed had $T_2$ been applied (Cox's page 15, quoted on p. 953). So he appears to accept $Y_t(u)$ and $Y_c(u)$. He also assumes constant effect, apparently for technical rather than conceptual reasons. He does not reject variable effects (p. 953).
- **Fisher** never dealt directly with multiple versions of the response. His 1926 question, asking what reason there is to think the manured acre would not still have given the higher yield without manure, makes it fairly clear that he could consider the yield under no manure being the same. He came closest in discussing the null hypothesis and randomization (p. 953).
- **Neyman (1935)**: the earliest explicit reference Holland found. Neyman's "true yield" $X_{ij}(k)=Y_k(u_{ij})$ (ignoring his "technical errors"). The average over plots $X_{\cdot\cdot}(k)=E(Y_k)$. By then the idea was established, but it is not part of standard notation of many writers (pp. 953–954).
- **Fisher–Neyman controversy**: Fisher quotes Neyman as saying that a bias vanishes when the objects compared react to differences in soil fertility in exactly the same manner, which Neyman adds is not always true. Fisher replies that it was true in the case required, when the hypothesis tested was true. Neyman then says his interest is in comparing average yields over the whole field and that effects on separate plots are "uninteresting and academic". Fisher: "It may be foolish, but that is what the z test was designed for" (p. 954).
- Holland's reading: Neyman's null hypothesis is zero average causal effect, $E(Y_t-Y_c)=0$. Fisher's is zero causal effect for all units, $Y_t(u)-Y_c(u)=0$ for all $u\in U$ (p. 954).

### 7. What can be a cause? (pp. 954–955)
- Holland's position, stated "as bluntly and as contentiously as possible": causes are only things that could, in principle, be treatments in experiments. "In principle" allows hypothetical experiments when practical or ethical issues stop real ones (p. 954).
- Holland believes that experiments and observational studies share the same notion of cause. The difference is the degree of control over $S$. In the model this is expressed by the joint distribution of $S$ with $Y_t, Y_c$. Total control can make $S$ independent of $Y_t, Y_c$ (p. 954).
- Holland uses "experiment" in a restricted sense. Chemical analysis or synthesis often lacks clearly identifiable units, treatments and responses. In his view the Aristotelian *material* cause is often more relevant there than *efficient* cause, so such experiments are not concerned with the notion of cause discussed in this article (p. 954).
- Three exam statements (p. 954): (A) she did well because she is a woman; (B) because she studied; (C) because she was coached by her teacher.
 - (A): the "cause" is an attribute. An attribute cannot be a cause in an experiment, because potential exposability does not apply. Its value can only change if the unit changes. "Causation" statements with attributes are statements of association across units. In (A) it means that women's performance exceeds men's in some sense (p. 955).
 - (C): easily interpreted. Had she not been coached, she would not have done as well. It implies a comparison of two causes (p. 955).
 - (B): applicability is unclear. Studying is voluntary, and it is not clear that we could expose someone to studying or not. Preventing her would shift (B) toward (C), and defining studying as hours "nose in book" only defines a measurable attribute. Holland calls it problematical and not easily resolved (p. 955).
- Examples of confusion: Saris and Stronkhorst's causal hypothesis that scholastic achievement affects the choice of secondary school treats an attribute as a cause, in Holland's reading. Kempthorne: "epistemological nonsense" to say one trait of an individual causes another (p. 955).
- Smoking and lung cancer: the debate is partly whether smoking is an attribute or a cause. Doll and Hill's data are purely associational. Fisher (1957) argued smoking might only indicate genetic differences related to lung cancer, though he thought a good prima facie case for further investigation had been made. McCurdy's replies (dose-response; lower rates among those who stopped) emphasize the causal aspect, since one can smoke more or less, or stop (p. 955).

### 8. Causal inference in various disciplines (pp. 955–958)

**8.1 Medicine (pp. 955–957).**
- *Koch's postulates* (as quoted from Yerushalmy and Palmer): I. the organism must be found in all cases of the disease; II. it must be isolated from patients and grown in pure culture; III. the pure culture inoculated into susceptible animals or man must reproduce the disease (pp. 955–956).
 - I is Mill's method of agreement: it ensures no data support a null effect. If there were bona fide cases without the organism alongside cases with it, then under unit homogeneity we would have an estimate of zero effect (p. 956).
 - III is like the light switch. It rests on an unstated assumption that without inoculation the disease would not be expected. "Susceptible" deals presumably with non-constant conjunction (p. 956).
 - II concerns good technique, i.e. minimizing measurement error in the treatment (p. 956).
- *Hill (1965)*: nine factors for judging whether an association is causal. Holland discusses them in his own order (p. 956).
 - Temporality: Hill asks "Which is the cart and which the horse?" Temporal succession is a given for Hill (p. 956).
 - Experiment (natural experiments such as preventative actions) and biological gradient (disease rate rises with exposure): both emphasize the causal nature of the agent, as in Section 7 (p. 956).
 - Plausibility, coherence, analogy: these reflect prior scientific knowledge and do not translate directly into the model. Hill warned against undue emphasis on them when biological knowledge is poor (p. 956).
 - Hill felt these six are the least significant on his list. The three most important are strength, consistency and specificity (p. 956).
 - Strength: acceptance of Mill's concomitant variation in practical terms, or of the utility of $T_{PF}$. There is no guarantee, but a larger $T_{PF}$ is often more likely than a smaller one to hold up in a controlled study. Cornfield et al. (1959) give an inequality bounding the influence of unmeasured factors on relative risk (p. 956).
 - Consistency: generality across populations, which might be viewed as a weakened constant conjunction. An association present in one population and absent in another suggests variable effects. Holland sees a scientists' bias against calling variable effects "causal", though those who deal with heterogeneous units such as humans generally agree it is usually too much to expect constant effects (p. 956).
 - Specificity: related to the believability of the independence assumption. A lack of association with other causes of death supports independence (but does not prove it). Since independence implies $T_{PF}=T$, specificity together with strong association may well be convincing evidence. Lack of specificity does not disprove independence in many cases, which explains why Hill does not treat it as serious (pp. 956–957).

**8.2 Granger causation in economics (pp. 957–958).**
- Granger (1969) built causality on prediction in time series. Holland says the essential ideas do not require the time series setting and restates them for variables on a population. He uses the time ordering to separate variables determined before, at, or after a time. He follows later writers in using noncausality and replaces Granger's least-squares predictor by conditional independence (p. 957).
- $X$ and $Y$ are **conditionally independent given $Z$** if
$$\Pr(Y=y\mid X=x,Z=z)=\Pr(Y=y\mid Z=z). \tag{30}$$
 $X$ is *not a Granger cause* of $Y$ (relative to $Z$) if $X,Y$ are conditionally independent given $Z$, where $Y$ is determined at time $s$ and $X,Z$ at or before $r<s$. Holland says this is stronger than Granger's noncausality and very like Suppes's spurious cause (p. 957).
- Identification with Rubin's model: Granger's $Y\to Y_S$, $X\to S$, $Z\to$ a set of pre-exposure variables $Z$ (p. 957). The condition $\Pr(Y_S=y\mid S=t,Z)=\Pr(Y_S=y\mid Z)$ reduces to
$$0=\{\Pr(Y_t=y\mid S=t,Z)-\Pr(Y_c=y\mid S=c,Z)\}\times\Pr(S=c\mid Z). \tag{31}$$
- In a randomized experiment $\Pr(S=c\mid Z)=\Pr(S=c)$, assumed strictly in $(0,1)$. So (31) gives
$$\Pr(Y_t=y\mid S=t,Z)=\Pr(Y_c=y\mid S=c,Z). \tag{32}$$
 Since $S$ is independent of $Y_t,Y_c,Z$, this becomes
$$\Pr(Y_t=y\mid Z)=\Pr(Y_c=y\mid Z), \tag{33}$$
 which implies
$$E(Y_t\mid Z)=E(Y_c\mid Z). \tag{34}$$
 With $T(z)=E(Y_t-Y_c\mid Z=z)$ (35), non-Granger-causality gives $T(z)=0$ for all $z$. So in a randomized experiment Granger noncausality implies zero average effect on every subpopulation defined by $Z$. Conversely ("easy to see"), if $t$ has a null effect on all units, then in a randomized experiment $S$ is not a Granger cause of $Y_S$ relative to any pre-exposure $Z$ (pp. 957–958).
- Holland's verdict: Granger causes are only temporarily so. More information (changing $Z$) may show a Granger cause to be spurious, as with Suppes. In his opinion it fails to reach the heart of causality (p. 958).

**8.3 Causal models in social science (p. 958).**
- Little work relates Rubin's model to causal modeling. Rosenbaum (1984b) relates the average causal effect to coefficients in linear path models. Holland only "hints" at points of contact (p. 958).
- Path diagrams: $X\to Y$ (36). $A\to Y$ with $A$ an attribute (37) is meaningless in Holland's view. $S\to Y_S$ (38) is meaningful (p. 958).
- Third variable cases:
 - $A$ an attribute, pre-exposure: time flow $A\ S\to Y_S$ with no arrow from $A$ (39). If $A$ is post-exposure, $A$ must be subscripted $A_t, A_c$. The diagram (40) shows $S$ changing both $A$ and $Y$ (Rosenbaum 1984b) (diagram (40) is not legible in the text layer) (p. 958).
 - A second cause indicator $R$ (causes $t'$, $c'$) acting at the same time: combine into $(R,S)$ and write $Y_{RS}$, diagram $(R,S)\to Y_{RS}$ (41). This says the $R$ causes do not affect exposure to the $S$ causes, and vice versa (p. 958).
 - If $R$ acts earlier and affects exposure to $S$, then $S$ is subscripted: $S_{t'}(u)$, $S_{c'}(u)$ (42). Diagram (43) says $R$ changes $S$ and $Y$, and $S$ changes $Y$. So $R$ has potentially a direct and an indirect effect on $Y$ (p. 958).
 - Example: encouragement to study ($R$: $t'$, $c'$), whether the student studied ($S$: $t$, $c$), test score $Y$. The hypothesis that encouragement has no direct effect on scores is
$$Y_{t's}(u)-Y_{c's}(u)=0\quad\text{for all }u\in U,\ s=t\text{ or }c. \tag{44}$$
- Holland's point: diagrams are easily interpreted in the model when they are not causally meaningless. He says the causal modeling literature has not been careful in separating meaningful from meaningless statements (pp. 958–959).

### 9. Summary (p. 959)
- Three ideas from experiments: (1) begin with the effects of causes, not the cause of a given effect. Holland says looking for causes is worthwhile but not the proper theoretical perspective. The "cause" is always subject to revision (bacteria, then toxins, then chemical reactions…). (2) Effects of causes are relative to other causes ("it takes two causes to define an effect"). Experiments without control comparisons are not experiments. (3) Not everything can be a cause; attributes of units are never causes (p. 959).
- That every phenomenon has a cause does not imply that everything can be a cause. Rubin and Holland's motto: **"NO CAUSATION WITHOUT MANIPULATION"** (p. 959).
- Why attributes are not causes: unless both $Y_a(u)$ and $Y_b(u)$ can be defined, in principle, $Y_a(u)-Y_b(u)$ cannot be defined. An attribute function takes one value per unit, so $Y_a(u)-Y_b(u)$ cannot be defined for any unit (p. 959).
- Two consequences of the model: the difference between the model $(S,Y_t,Y_c)$ and the process of observation $(S,Y_S)$, and the Fundamental Problem. Holland says they are really the same thing said in different ways. What is impossible is causal inference *without untested assumptions*, not causal inference itself. The model's strength is that it makes the assumptions explicit, so one can look for ways to test them at least partly (p. 959).

## Toy example (ours, not from the text)
Four units; both potential responses are listed, although in reality only one per unit is observable.

| unit | $Y_c$ | $Y_t$ |
|---|---|---|
| $u_1$ | 6 | 8 |
| $u_2$ | 4 | 6 |
| $u_3$ | 2 | 4 |
| $u_4$ | 0 | 2 |

- Effects $Y_t-Y_c$: 2, 2, 2, 2 (constant effect). $E(Y_t)=(8+6+4+2)/4=5$, $E(Y_c)=(6+4+2+0)/4=3$, so $T=5-3=2$ by (4).
- **Non-random assignment** (the high-$Y_c$ units get $t$): $S=t$ for $u_1,u_2$; $S=c$ for $u_3,u_4$. Observed $Y_S$: 8, 6, 2, 0. $E(Y_S\mid S=t)=7$, $E(Y_S\mid S=c)=1$, so $T_{PF}=6\ne T$. Check with (15): $E(Y_c\mid S=t)=(6+4)/2=5$, $E(Y_c\mid S=c)=(2+0)/2=1$, and $2+(5-1)=6$ ✓.
- **Random assignment** (two of four units get $t$; six equally likely choices). Difference of group means of $Y_S$:
 - $\{u_1,u_2\}$: $7-1=6$.
 - $\{u_1,u_3\}$: $6-2=4$.
 - $\{u_1,u_4\}$: $5-3=2$.
 - $\{u_2,u_3\}$: $5-3=2$.
 - $\{u_2,u_4\}$: $4-4=0$.
 - $\{u_3,u_4\}$: $3-5=-2$.
- The average is $(6+4+2+2+0-2)/6=12/6=2=T$ ✓. Any single randomization can miss $T$, but on average over the randomization the raw difference equals $T$. This illustrates $T_{PF}=T$ under independence (9) and the failure of $T_{PF}=T$ without it.

## Concepts
- [[potential-outcomes]] — each unit has $Y_t(u)$ and $Y_c(u)$; the effect is their difference (p. 946–947)
- [[fundamental-problem-of-causal-inference]] — $Y_t(u)$ and $Y_c(u)$ cannot both be observed on one unit (p. 947)
- [[assignment-mechanism-ignorability]] — $S$ decides exposure. Independence of $S$ from $Y_t,Y_c$ gives $T=T_{PF}$. Conditional versions are mentioned as "strong ignorability" (p. 948–949)
- [[causal-dag]] — path diagrams; Holland finds some meaningful (e.g. $S\to Y_S$) and some meaningless (e.g. attribute $\to$ response) (p. 958)
- [[average-causal-effect]] (new) — $T=E(Y_t-Y_c)=E(Y_t)-E(Y_c)$ over $U$ (p. 947)
- [[prima-facie-causal-effect]] (new) — $T_{PF}=E(Y_S\mid S=t)-E(Y_S\mid S=c)$, associational; borrowed from Suppes (p. 949)
- [[unit-homogeneity]] (new) — assumes $Y_t(u_1)=Y_t(u_2)$ and $Y_c(u_1)=Y_c(u_2)$ for two units; the scientific solution (p. 948)
- [[constant-effect]] (new) — $Y_t(u)-Y_c(u)=T$ for all $u$; also called additivity; weaker than unit homogeneity (p. 949)
- [[temporal-stability-causal-transience]] (new) — assumptions for measuring $Y_c$ and $Y_t$ on one unit in sequence (p. 948)
- [[no-causation-without-manipulation]] (new) — Holland's position: causes must be things that could in principle be treatments; attributes are not causes (p. 954, 959)
- [[suppes-spurious-cause]] (new) — a prima facie cause whose effect is screened off by an earlier event, per (S1)–(S3) (p. 952)
- [[granger-noncausality]] (new) — $X$ and $Y$ conditionally independent given $Z$, as restated by Holland (p. 957)
- [[mills-methods]] (new) — difference, residues, agreement (null effect), concomitant variation, read in the model (pp. 950–951)

## Canonical instances
- [[light-switch-example]] — believing one knows both $Y_t$ and $Y_c$ rests on plausible assumptions (p. 947)
- [[kempthorne-randomized-block]] — plots as units, $y_{ijk}=Y_k(u_{ij})$, an early multiple-response notation (p. 953)
- [[fisher-neyman-null-hypothesis]] — zero effect on every unit versus zero average effect (p. 954)
- [[smoking-lung-cancer-debate]] — attribute versus cause, Fisher versus McCurdy (p. 955)
- [[exam-because-examples]] — statements (A), (B), (C) and their different causal status (pp. 954–955)
- [[koch-postulates]] — in the model: I is the method of agreement, III is like the light switch (pp. 955–956)
- [[hill-nine-factors]] — Hill's guidelines mapped to the model (pp. 956–957)
- [[encouragement-design]] — path diagram (43) and condition (44) (p. 958)

## Bridges (candidates)
- [same-math] Holland's $(Y_t, Y_c)$ and $T=E(Y_t-Y_c)$ ↔ bayesian/causal canon: potential outcomes and the average treatment effect — same definitions.
- [same-math] Independence of $S$ from $(Y_t,Y_c)$ giving (7)–(9) ↔ ignorability under a randomized assignment mechanism — same condition.
- [structural-analogy] "Strong ignorability" (p. 949, only named there) and conditional independence given pre-exposure $Z$ (eq. 30–35, a Granger-type condition) ↔ conditional ignorability given covariates — similar idea, but not the same condition.
- [structural-analogy] $T_{PF}$ versus $T$ and eq. (15) ↔ confounding versus selection bias: the braces term in (15) is the baseline difference between groups.
- [structural-analogy] Path diagrams (36)–(43) ↔ causal DAG: arrows read as exposure-to-response, but meaningful only for manipulable causes.
- [structural-analogy] Granger and Suppes screening-off ↔ d-separation: both express "no predictive value given $Z$".
- [metaphor] The Fundamental Problem ↔ missing-data problem: each unit has one unobserved potential outcome.

## Questions this raises
- If the independence assumption in (7)–(8) is not guaranteed by randomization, how can pre-exposure variables replace it (conditional independence, §4.5)?
- Holland says the constant effect assumption can only be partly checked by subpopulation estimates $T_i$. What stronger checks exist, and what do variable effects mean for policy decisions about a single unit?
- How should causal statements about voluntary actions (example B) or non-manipulable features be treated? Is "no causation without manipulation" too strict, or just a definition?
- Can the Hill factors that do not translate into the model (plausibility, coherence, analogy) be given a formal role?

## Reading notes
- Printed page = pdf page + 943 (pdf 2 = p. 945). The pdf 1 page is the publisher's cover sheet and carries no article page number. The article ends on p. 960 with the references; there are no exercises.
- The text layer is garbled in places: on p. 946 (pdf 3) the sentence about the values of $Y(u)$ and $A(u)$ reads "are all u in U" in both the text layer and the page image (presumably "for all u" is meant); subscripts such as $Y_t$, $Y_c$ are often mangled; p. 955 "Sans and Stronkhorst" corresponds to "Saris, W., and Stronkhorst, H. (1984)" in the reference list (no image of p. 955 was supplied, so I could not check which spelling is printed in the body).
- Path diagrams (40) and (43) on p. 958 are blank in the text layer, and no image of that page was supplied; I described them from Holland's prose. Diagrams (36)–(39) and (41) are visible in the text layer.
- Minor: p. 947 says "on unit U" (capital) in the sentence after (1). On p. 951 the method-of-agreement passage speaks of the cause $t$ not occurring, then adds $c$; the page image shows the same wording, apparently a slip.
- The comments by Glymour and Granger mentioned in the author's footnote (p. 945) are not part of these pages.
