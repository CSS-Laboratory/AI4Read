---
id: hernan-2020-whatif/ch19-time
work: hernan-2020-whatif
unit: "19 Time-varying treatments"
pages: 255-266
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Time-varying treatments (Chapter 19)

## L0 — One line
With treatments that change over time, a causal effect is only defined as a contrast between named treatment strategies, and estimating it validly requires some form of sequential exchangeability (plus sequential positivity and consistency).

## L1 — The gist (≤ 120 words)
What does "the causal effect" mean when treatment can change every month, and when can data identify it? The chapter says there is no single effect. Each pair of treatment strategies (rules assigning treatment at each time, possibly depending on the patient's evolving covariates) defines one effect. These effects are identified if sequential exchangeability, sequential positivity and consistency hold. Sequentially randomized experiments are expected to satisfy them. Observational studies can satisfy sequential exchangeability if treatment depends only on measured history. Single-world intervention graphs (SWIGs) show that some strategies can be identified while others cannot. With time-varying confounders most adjustment methods may be biased; g-methods (next chapter) are appropriate.

**Prerequisites:** counterfactual outcomes; conditional exchangeability, positivity, consistency for a fixed treatment; causal DAGs, backdoor paths, d-separation; SWIGs (Ch. 7).

## L2 — Key ideas (5–10 bullets)
- With treatment $A_k$ at months $k=0,\dots,K$, the effect is a contrast of mean counterfactual outcomes under two treatment strategies, so it is "not uniquely defined" (p. 256).
- Strategies can be static (same treatment sequence for everyone) or dynamic (treatment depends on evolving covariates $\bar L_k$, e.g. CD4 count). A dynamic strategy cannot be written as a single fixed vector $\bar a$ (pp. 256–257).
- A sequentially randomized experiment randomizes treatment at each time with probabilities depending only on past treatment and measured covariates. It can be represented by Figure 19.1 or 19.2, but not by 19.3, where unmeasured $U$ affects treatment (pp. 259–260).
- Sequential exchangeability for $Y^g$ is the time-varying analogue of conditional exchangeability. It holds if no arrows go from unmeasured $U$ into treatment; with sequential positivity and consistency it identifies $E[Y^g]$ (p. 260).
- Positivity and consistency also need sequential versions. Positivity need only hold for histories compatible with the strategy of interest (p. 261).
- SWIGs plus d-separation show that identification can hold for static but not dynamic strategies (Figure 19.6), for all strategies (19.5), or for none (19.3, 19.11) (pp. 260, 263–264).
- A measured covariate $L_k$ can be a "confounder" although the real common cause is unmeasured $U$; when $L_k$ affects later treatment and shares unmeasured causes with $Y$ at several times, the $\bar L_k$ are time-varying confounders (p. 265).
- Whether measured covariates suffice for sequential exchangeability can never be answered with certainty, and we cannot empirically confirm that all confounders are measured. Even when all confounders are measured, most adjustment methods may be biased, which motivates g-methods (pp. 265–266).

## L3 — Walkthrough

### Introduction and 19.1 The causal effect of time-varying treatments (pp. 255–256)
- Parts I–II dealt with time-fixed treatments. Part III extends them to treatments that can take different values for a single individual over time (p. 255). The author calls this one of the most technical chapters (p. 255).
- Setup (HIV example). A dichotomous treatment $A_k$ (antiretroviral therapy in month $k$, 1 = yes) for $k=0,1,\dots,K$ with $K=59$. $Y$ is health status at month $K+1=60$; higher is better. Provisionally no loss to follow-up or death, and perfect measurement. $A_{-1}=0$ for everyone (pp. 255–256).
- Notation: treatment history $\bar A_k=(A_0,\dots,A_k)$; $\bar A=\bar A_K$. "Always treated" is $\bar a=\bar 1=(1,\dots,1)$; "never treated" is $\bar 0$. Most people have mixed histories (p. 255–256).
- For a fixed treatment, $E[Y^{a=1}]-E[Y^{a=0}]$ needs no reference to time. With time-varying treatment, the contrast $E[Y^{a_k=1}]-E[Y^{a_k=0}]$ only quantifies the effect of $A_k$ at one time $k$, not of the whole history (p. 256).
- So the effect must be a contrast between two strategies involving treatment at all times $0,\dots,K$. Hence the average causal effect "is not uniquely defined" (p. 256).

*Intuition note:* "Treat or not?" is no longer one decision but a whole schedule of decisions. A causal question must say which two schedules are being compared.

### 19.2 Treatment strategies (pp. 256–257)
- A **treatment strategy** (plan, policy, protocol, regime) is a rule assigning treatment at each time $k$ (p. 256).
- Static example: $E[Y^{\bar a=\bar 1}]-E[Y^{\bar a=\bar 0}]$ ("always treat" vs "never treat") (p. 256).
- Another contrast: $E[Y^{\bar a}]-E[Y^{\bar a'}]$ with $\bar a=(1,0,1,0,\dots)$ ("every other month") vs $\bar a'=(0,1,1,1,\dots)$ (treat at all months except the first) (p. 256).
- The author says there are "at least $2^K$" static strategies, since there are $2^K$ combinations $(a_0,\dots,a_K)$ of a dichotomous $a_k$ (p. 256). They do not exhaust all strategies.
- **Dynamic strategy:** treatment $a_k$ depends on the evolution of the individual's covariates $\bar L_k$. Example: $L_k=1$ if CD4 count is low (bad prognosis), else 0; $L_0=0$ for all. Strategy: "do not treat while $L_k=0$, start when $L_k=1$, treat continuously afterwards." It cannot be written as one $\bar a$ giving everyone the same $a_k$ at each $k$ (p. 256).
- Strategies with no dependence on covariates are **static** (non-dynamic) (p. 257).
- The effect is well defined only if the strategies are specified: $E[Y^{\bar a}]-E[Y^{\bar a'}]$, or $E[Y^{\bar a}]-E[Y^{g}]$ with $g$ e.g. treating only after the CD4 count has become low. $g$ denotes any static or dynamic strategy; for a static one one may write $Y^{g=\bar a}$ (p. 257).
- Even with only treat/not-treat at each time, there are as many effects as pairs of strategies (p. 257).

**Fine Point 19.1 (p. 257).**
- A deterministic dynamic strategy is $g=[g_0(\bar a_{-1},l_0),\dots,g_K(\bar a_{K-1},\bar l_K)]$, where $g_k(\bar a_{k-1},\bar l_k)$ is the treatment assigned at $k$ given past history. A deterministic static strategy has $g_k(\bar a_{k-1})$ not depending on $\bar l_k$ (p. 257).
- Random strategies assign a probability of treatment (static, e.g. treat with probability 0.3 each month; or dynamic, e.g. treat only those with low CD4 with probability 0.3) (p. 257).
- The optimal strategy maximizes $E[Y^g]$ (when higher is better). For a drug the optimal strategy will almost always be dynamic (toxicity). No random strategy can ever be preferred to the optimal deterministic one, but randomized trials remain necessary because before the trial it is unknown which deterministic strategy is optimal (p. 257).
- In the text $g$ means a deterministic strategy unless noted (p. 257).

**Technical Point 19.1 (p. 258).** Each strategy $g$ depending on past treatment and covariates is associated with a strategy $g'=[g'_0(\bar l_0),\dots,g'_K(\bar l_K)]$ depending only on covariate history. By consistency, an individual has the same treatment, covariate and outcome history under $g$ and $g'$, so $Y^g=Y^{g'}$ and $\bar L^g(K)=\bar L^{g'}(K)$. The definition is recursive: $g'_0(l_0)=g_0(\bar a_{-1}=0,l_0)$ and $g'_k(\bar l_k)=g_k[g'_k(\bar l_{k-1}),\bar l_k]$ (notation as printed; the inner term is the treatment history that $g'$ assigns through $k-1$). An individual followed $g$ through $t$ ($A_k=g_k(\bar A_{k-1},\bar L_k)$ for $k\le t$) if and only if they followed $g'$ through $t$ ($A_k=g'_k(\bar L_k)$) (p. 258).

*Intuition note:* A dynamic strategy is a policy (for example: if your CD4 is low, treat). Different people then get different treatment sequences, but all follow the same rule.

### 19.3 Sequentially randomized experiments (pp. 257–259)
- Figures 19.1–19.3 show three situations. $A_k$ is treatment, $L_k$ measured variables, $U_k$ unmeasured common causes, $Y$ outcome. Only $k=0,1$ are drawn; all participants adhere to assigned treatment (pp. 257–258).
- In the HIV example, CD4 count $L_k$ is a consequence of unmeasured immune damage $U_k$; more damage means lower $L_k$ and worse $Y$ (p. 258).
- **Figure 19.1:** no arrows from $\bar L_k$ or $\bar U_k$ into $A_k$. **Figure 19.2:** arrows from $\bar L_k$ but not $\bar U_k$ into $A_k$. **Figure 19.3:** arrows from both (p. 258).
- Figure 19.1 could be a randomized trial whose assignment probability depends only on prior treatment, e.g. probability 0.5 if $A_{k-1}=0$ and 1 if $A_{k-1}=1$ (p. 258).
- For static strategies Figure 19.1 is the proper generalization of no confounding: $E[Y^{\bar a}]=E[Y\mid\bar A=\bar a]$ (p. 258).
- This is not true for dynamic strategies. $E[Y^g]$ equals the mean outcome among those who followed $g$ only if the probability of $A_k=1$ is exactly 0.5 at all times when treatment depends on $L_k$. Otherwise g-methods are needed under Figure 19.1 or 19.2 (p. 258).
- Figure 19.2 could be an experiment with probabilities depending on prior treatment and measured covariates, e.g. 0.4 for untreated with high CD4, 0.8 for untreated with low CD4, 0.5 for previously treated. There is confounding by measured, not unmeasured, variables (pp. 258–259; see Reading notes on the coding of $L_k$).
- A **sequentially randomized experiment** randomizes treatment at each time for each individual. Figures 19.1 and 19.2 could represent one. Figure 19.3 cannot, because investigators cannot use unmeasured $U$ to assign treatment (p. 259).
- Observational studies are typically represented by Figure 19.2 or 19.3. If real-world treatment decisions depended on $(\bar A_{k-1},\bar L_k)$ and no unmeasured variables, the study is like Figure 19.2: it differs from a sequentially randomized experiment only in that the assignment probabilities are unknown (but estimable). It is impossible to show empirically whether Figure 19.2 or 19.3 applies (p. 259).
- Such experiments are not frequently used in practice, but the concept helps to understand the key conditions (p. 259).

### 19.4 Sequential exchangeability (pp. 259–261)
- For fixed treatments, $Y^a\perp\!\!\!\perp A\mid L$ is expected in conditionally randomized experiments (p. 259). For time-varying treatments we need conditional exchangeability at each time (p. 259–260).
- Two time points: $Y^g\perp\!\!\!\perp A_0\mid L_0$ and $Y^g\perp\!\!\!\perp A_1\mid A_0=g(L_0),L_0,L_1$. In general, **sequential exchangeability for $Y^g$** is
$$Y^{g}\perp\!\!\!\perp A_k\mid \bar A_{k-1}=g(\bar A_{k-2},\bar L_{k-1}),\ \bar L_k\quad\text{for all strategies } g \text{ and } k=0,1,\dots,K$$
(p. 260).
- A sequentially randomized experiment implies it: at each $k$, the treated and untreated are exchangeable for $Y^g$ given $\bar L_k$ and any observed history compatible with $g$ (p. 260).
- It holds in any causal graph with no arrows from unmeasured $U$ into the treatments $A$ (like Figure 19.2). So it holds in sequentially randomized experiments and observational studies where treatment depends on $(\bar A_{k-1},\bar L_k)$ and, given that history, not on unmeasured causes of the outcome (p. 260).
- Consequences: under Figure 19.2, $E[Y^g]$ is identified for all $g$; under Figure 19.3, for no $g$; under other diagrams, the text says for some but not all $g$ (p. 260); the later examples show diagrams where all, only static, or no strategies are identified (pp. 263–264).
- Example, Figure 19.4: an unmeasured $W_0$ (say an unrecorded clinic visit at time 0) causes both $A_0$ and the error-prone measured $L_1$ (with $U_1$ the true CD4 count). $E[Y^g]$ is still identified under every static $g=\bar a$, but not under any dynamic $g$ depending on $L_1$ (p. 260).
- Identification also needs sequential positivity and consistency, expected to hold in sequentially randomized experiments (and assumed below). Under all three conditions $E[Y^g]$ can be identified as long as we use methods that appropriately adjust for $(\bar A_{k-1},\bar L_k)$, such as the g-formula (standardization), IP weighting and g-estimation (p. 260).

**Technical Point 19.2 (p. 261).**
- Sequential positivity:
$$\text{If } f_{\bar A_{k-1},\bar L_k}(\bar a_{k-1},\bar l_k)\neq 0,\ \text{then } f_{A_k\mid\bar A_{k-1},\bar L_k}(a_k\mid\bar a_{k-1},\bar l_k)>0\ \text{for all } \bar a_k,\bar l_k.$$
It holds in a sequentially randomized experiment if randomization probabilities are never 0 or 1 whatever the past. For a particular $g$, it need only hold for histories compatible with $g$, i.e. $a_k=g(\bar a_{k-1},\bar l_k)$ (p. 261).
- Sequential consistency: $Y^{\bar a}=Y^{\bar a^*}$ if $\bar a^*=\bar a$; $Y^{\bar a}=Y$ if $\bar A=\bar a$; $\bar L_k^{\bar a}=\bar L_k^{\bar a^*}$ if $\bar a^*_{k-1}=\bar a_{k-1}$; $\bar L_k^{\bar a}=\bar L_k$ if $\bar A_{k-1}=\bar a_{k-1}$ (p. 261).
- Weaker consistency suffices technically: if $\bar A=\bar a$ then $Y^{\bar a}=Y$ is enough for static strategies; if $A_k=g_k(\bar A_{k-1},\bar L_k)$ at each $k$ then $Y^g=Y$ is enough for dynamic ones. The stronger version is a natural condition the author always accepts (p. 261).
- If the two interventions on $A_k$ (treat or do not treat in month $k$) are well defined at all times, then all static and dynamic strategies involving $A_k$ are similarly well defined (p. 261).

*Intuition note:* At every month, among people with the same past (treatment and covariates), those treated and untreated must be comparable for their future outcomes. Randomizing each month with probabilities depending only on the past implies this; in observational data it holds if treatment decisions depend only on the measured past, but no form of it is guaranteed and it cannot be checked from the data.

### 19.5 Identifiability under some but not all treatment strategies (pp. 261–264)
- A generalized backdoor criterion exists: for static strategies, a sufficient condition for identification is that at each $k$ all backdoor paths into $A_k$ not going through any future treatment are blocked. But it uses DAGs without counterfactuals and does not show the link to sequential exchangeability. SWIGs, which contain counterfactual outcomes, are an alternative check and are especially helpful here (p. 261).
- Figures 19.5 and 19.6 are simplified versions of 19.2 and 19.4: $U_0$, $L_0$ and the arrow $A_0\to U_1$ are omitted, and $L_1\to Y$ is absent. They differ in whether $A_k$ and later $L_t$ share a cause $W_k$ (19.6 has $W_0$) (p. 261).
- **SWIG construction** (Figure 19.7, for static strategy $(a_0,a_1)$ in the world of 19.5): split each treatment node. The right side is the value under intervention; the left side is the value observed when intervening on all previous treatments, so the left of $A_0$ is $A_0$ and the left of $A_1$ is $A_1^{a_0}$. Arrows into a treatment go to its left side; arrows out start from its right side. The outcome is $Y^{a_0,a_1}$, and $L_1$ becomes $L_1^{a_0}$ (not $L_1^{a_0,a_1}$, since a future intervention cannot affect earlier $L_1$) (p. 262).
- In Figure 19.7, d-separation gives $Y^{a_0,a_1}\perp\!\!\!\perp A_0$ and $Y^{a_0,a_1}\perp\!\!\!\perp A_1^{a_0}\mid A_0,L_1^{a_0}$ for any static $(a_0,a_1)$. The apparently open path $A_1^{a_0}\leftarrow a_0\to L_1^{a_0}\leftarrow U_1\to Y^{a_0,a_1}$ is blocked, because $a_0$ is a constant and constants are implicitly conditioned on (p. 263; Fine Point 19.2).
- By consistency ($L_1^{a_0}=L_1$ and $A_1^{a_0}=A_1$ when $A_0=a_0$), $Y^{a_0,a_1}\perp\!\!\!\perp A_1\mid A_0=a_0,L_1$ holds under Figure 19.5 (p. 263).
- With many time points: **static sequential exchangeability for $Y^{\bar a}$** is $Y^{\bar a}\perp\!\!\!\perp A_k\mid\bar A_{k-1}=\bar a_{k-1},\bar L_k$ for $k=0,\dots,K$. It is weaker than sequential exchangeability for $Y^g$ and sufficient to identify the mean under any static strategy (p. 263).
- Figure 19.6 (SWIG in 19.8): static sequential exchangeability also holds, so means under static strategies are identified (p. 263).
- Variations on Figure 19.5: if the arrow $L_1\to A_1$ were missing, sequential unconditional exchangeability holds, and static means are identified without data on $L_1$. If an arrow $U_1\to A_1$ were added, no form of sequential exchangeability holds and no counterfactual mean is identified (p. 263).
- **Dynamic strategy SWIG** (Figure 19.9, world of 19.5, $g=[g_0,g_1(L_1)]$): $A_1$ is assigned $g_1(L_1^g)$. Example: do not treat at time 0, and treat at time 1 only if CD4 is low. The SWIG gets an arrow $L_1^g\to g_1(L_1^g)$ that is not in the original graph (drawn differently, treated like any arrow for d-separation). d-separation gives $Y^g\perp\!\!\!\perp A_0$ and $Y^g\perp\!\!\!\perp A_1^g\mid A_0=g_0,L_1^g$ for any $g$. So sequential exchangeability for $Y^g$ holds and all $E[Y^g]$ are identified (p. 263).
- **Figure 19.10** (world of 19.6, dynamic $g$): $Y^g\perp\!\!\!\perp A_0$ fails because of the open path $A_0\leftarrow W_0\to L_1^g\to g_1(L_1^g)\to Y^g$. So sequential exchangeability for $Y^g$ fails. $E[Y^g]$ for these dynamic strategies is not identified (p. 264).
- **Summary (p. 264).** Under Figure 19.5 (observational or sequentially randomized), static and dynamic effects can be validly estimated. Under 19.6, only static ones. The reason: in the SWIG of 19.10, the distribution of $Y^g$ depends on that of $L_1^g$, which is not identifiable because of the path $A_0\leftarrow W_0\to L_1^g$.
- **Figure 19.11** (= 19.6 plus $L_1\to Y$; SWIG 19.12): neither sequential exchangeability for $Y^g$ nor static sequential exchangeability holds, so no strategy's effect can be validly estimated (p. 264).

| Diagram | Static strategies | Dynamic strategies |
|---|---|---|
| 19.5 / 19.2 | identified | identified |
| 19.6 / 19.4 | identified | not identified |
| 19.3, 19.11 | not identified | not identified |

(Compiled from pp. 260, 263–264.)

*Intuition note:* A hidden variable such as $W_0$ may hurt only the strategies that "listen" to the contaminated covariate $L_1$. A static strategy ignores $L_1$, so it can still be identified.

**Technical Point 19.3 (p. 262).**
- In a sequentially randomized experiment the SWIG gives $(Y^{\bar a},\underline L^{\bar a}_{k+1})\perp\!\!\!\perp A_k^{\bar a_{k-1}}\mid\bar A_{k-1}^{\bar a_{k-2}},\bar L_k^{\bar a_{k-1}}$, where $\underline L^{\bar a}_{k+1}$ is the counterfactual covariate history from $k+1$ to the end. By consistency this becomes $(Y^{\bar a},\underline L^{\bar a}_{k+1})\perp\!\!\!\perp A_k\mid\bar A_{k-1}=\bar a_{k-1},\bar L_k$. When this holds for all $\bar a$, the text calls it sequential exchangeability (p. 262).
- Although stated only for static strategies, it is equivalent to the stronger-looking $(Y^g,\underline L^g_{k+1})\perp\!\!\!\perp A_k\mid\bar A_{k-1}=g(\bar A_{k-1},\bar L_k),\bar L_k$ for all $g$. With positivity it identifies the outcome and covariate distribution under any static or dynamic $g$ (Robins 1986). For dynamic strategies it does not follow from the separate independences of $Y^{\bar a}$ and of $\underline L^{\bar a}_{k+1}$ from $A_k$ (p. 262).
- Stronger independences expected in sequentially randomized experiments cannot be read from SWIGs and are not necessary for identification. Example: $\{Y^{\bar a},\underline L^{\bar a}_{k+1};\text{all }\bar a\}\perp\!\!\!\perp A_k\mid\bar A_{k-1},\bar L_k$. The strongest is **full sequential exchangeability**, $(Y^{\mathcal A},\bar L^{\mathcal A})\perp\!\!\!\perp A_k\mid\bar A_{k-1},\bar L_k$, with $\mathcal A$ the set of all $2^K$ static strategies (p. 262).

**Fine Point 19.2 (p. 264).**
- SWIGs keep arrows out of intervention nodes $a$ although $a$ is a constant. Otherwise SWIGs of two DAGs (Figure 7.14, and the same plus a direct $A\to Y$ arrow) would coincide, and one could not tell that the effect is identified by the front-door formula in the first but not the second. In d-separation on a SWIG, all paths through an intervention node are blocked even without conditioning on $a$ in the notation (p. 264).
- For a deterministic strategy $g_0(L_0)$, conditioning on $L_0$ makes $g_0(L_0)$ constant, so we need not condition on it, and consistency turns $Y^g\perp\!\!\!\perp A_1^g\mid A_0,L_0,L_1^g$ into $Y^g\perp\!\!\!\perp A_1\mid A_0=g(L_0),L_0,L_1$ (p. 264).
- For a random strategy assigning $A_0^{+,g}$ from a distribution depending on $L_0$, $A_0^{+,g}$ must appear in the SWIG and in the conditioning set. Richardson and Robins (2013) showed that $Y^g\perp\!\!\!\perp A_1^g\mid A_0,A_0^{+,g},L_0,L_1^g$ is necessary for identifiability by the g-formula for such a strategy. Strategies depending on the natural value of treatment are called "modified treatment policies" (p. 264).

### 19.6 Time-varying confounding and time-varying confounders (pp. 265–266)
- No form of sequential exchangeability is guaranteed in observational studies. Expert knowledge guides measuring the relevant $\bar L_k$ (HIV: CD4 count, viral load, symptoms). Whether the measured covariates suffice for sequential exchangeability can never be answered with certainty; expert knowledge is used to organize our beliefs and represent them in causal diagrams (p. 265).
- In Figure 19.5, for the effect of $A_1$ on $Y$: backdoor path $A_1\leftarrow L_1\leftarrow U\to Y$ cannot be blocked by $U$ (unmeasured) but is blocked by measured $L_1$. So $L_1$ is called a **confounder** although the actual common cause is $U$. Conditioning on collider $L_1$ opens a second backdoor path $A_1\leftarrow A_0\to L_1\leftarrow U\to Y$, which can be blocked by conditioning on prior treatment $A_0$ (margin note, p. 265).
- A confounder need not be a direct cause of the outcome ($L_1\to Y$ is absent in 19.5) (p. 265).
- In a long diagram where $L_k$ affects later treatments and shares unmeasured causes $U_k$ with $Y$, blocking backdoor paths between $A_k$ and $Y$ needs $\bar L_k$ together with $\bar A_{k-1}$. No unmeasured confounding for the effect of $\bar A$ then requires data on $\bar L_k$, and the $\bar L_k$ are **time-varying confounders** (also called time-dependent confounders) (p. 265).
- We cannot empirically confirm that all confounders are measured, i.e. cannot distinguish Figure 19.2 from 19.3. Even if all confounders were correctly measured and modeled, most adjustment methods may still give biased estimates when comparing treatment strategies. The next chapter explains why g-methods are appropriate (pp. 265–266).

**Fine Point 19.3 (p. 266).**
- Without selection bias, there is confounding for effects involving $E[Y^{\bar a}]$ if $E[Y^{\bar a}]\neq E[Y\mid\bar A=\bar a]$.
- Confounding is solely time-fixed if $E[Y^{\bar a}\mid L_0]=E[Y\mid\bar A=\bar a,L_0]$ (e.g. only $A_0$ and $L_0$ point into $A_1$ in Figure 19.2).
- If the identifiability conditions hold but $E[Y^{\bar a}\mid L_0]\neq E[Y\mid\bar A=\bar a,L_0]$, time-varying confounding is present. If the conditions fail (Figure 19.3), there is unmeasured confounding.
- A sufficient condition for no time-varying confounding is unconditional sequential exchangeability, $Y^{\bar a}\perp\!\!\!\perp A_k\mid\bar A_{k-1}=\bar a_{k-1}$, as in Figure 19.1.
- Figure 19.1 can be simplified: $L_1$ is not a common cause of two nodes, so omit it. Then $L_0$ and $U_1$, then $U_0$, can be omitted too, leaving $A_0,A_1,Y$ (p. 266).

## Toy example (ours, not from the text)
Four patients, two times ($k=0,1$), $A_0=0$ for everyone under the strategies below. Invented counterfactual table, with $L_1^{0}$ the CD4 indicator (1 = low) after $a_0=0$:

| Patient | $L_1^{0}$ | $Y^{0,0}$ | $Y^{0,1}$ |
|---|---|---|---|
| 1 | 1 | 2 | 6 |
| 2 | 1 | 3 | 7 |
| 3 | 0 | 5 | 5 |
| 4 | 0 | 6 | 4 |

- Static "never treat" $(0,0)$: $E[Y^{0,0}]=(2+3+5+6)/4=16/4=4$.
- Static $(0,1)$: $E[Y^{0,1}]=(6+7+5+4)/4=22/4=5.5$.
- Dynamic $g$: "$a_0=0$; $a_1=1$ if $L_1^{0}=1$, else 0". Patients 1, 2 get $a_1=1$ and patients 3, 4 get $a_1=0$, so $Y^g=6,7,5,6$ and $E[Y^g]=24/4=6$.
- Contrasts: $E[Y^g]-E[Y^{0,0}]=6-4=2$; $E[Y^{0,1}]-E[Y^{0,0}]=5.5-4=1.5$. Different strategy pairs give different "effects", and $g$ is not any single $\bar a$ (patients get different $a_1$).
- With two time points there are $2\times2=4$ static strategies: $(0,0),(0,1),(1,0),(1,1)$.

## Concepts
- [[time-varying-treatment]] (new) — treatment $A_k$ that can take different values for one individual over time (p. 255).
- [[treatment-strategy]] (new) — rule assigning treatment at each time; effects are contrasts between strategies (p. 256).
- [[dynamic-treatment-strategy]] (new) — strategy whose treatment at $k$ depends on evolving covariates $\bar L_k$; static ones do not (pp. 256–257).
- [[sequentially-randomized-experiment]] (new) — treatment randomized at each time with probability depending only on past treatment and measured covariates (pp. 259–260).
- [[sequential-exchangeability]] (new) — $Y^g\perp\!\!\!\perp A_k\mid\bar A_{k-1}=g(\cdot),\bar L_k$ at every $k$; "static" version covers only $g=\bar a$ (pp. 260, 263).
- [[sequential-positivity-consistency]] (new) — time-varying versions of positivity and consistency (p. 261).
- [[swig]] (new) — single-world intervention graph; node splitting lets d-separation check counterfactual independences (p. 262).
- [[time-varying-confounding]] (new) — covariates $\bar L_k$ that affect later treatment and share unmeasured causes with the outcome are time-varying confounders (p. 265); Fine Point 19.3 says time-varying confounding is present when the identifiability conditions hold but $E[Y^{\bar a}\mid L_0]\neq E[Y\mid\bar A=\bar a,L_0]$ (p. 266).
- [[g-methods]] (new) — named as the appropriate approach to adjust for time-varying confounders (pp. 258, 266); the text lists the g-formula, IP weighting and g-estimation as methods that adjust for treatment and covariate history (p. 260).
- [[assignment-mechanism-ignorability]] — the sequential version replaces ordinary conditional exchangeability (p. 259).
- [[causal-dag]], [[d-separation]], [[back-door-front-door-criterion]] — used in the generalized backdoor criterion and SWIG checks (p. 261).
- [[potential-outcomes]] — counterfactual $Y^g$ indexed by strategy (p. 256).
- [[confounding-vs-selection-bias]] — chapter drawn without selection bias to isolate confounding (p. 265).

## Canonical instances
- [[hiv-art-cd4-example]] (new) — monthly antiretroviral therapy $A_k$, CD4 count $L_k$, unmeasured immune damage $U_k$, health outcome $Y$ at month 60 (pp. 255–258).
- [[figures-19-1-to-19-12]] (new) — DAG/SWIG catalogue showing which strategies are identified under which diagram (pp. 258–264).

## Bridges (candidates)
- [structural-analogy] dynamic treatment strategy ↔ reinforcement learning: a policy mapping history to action — the optimal strategy maximizes expected outcome (p. 257).
- [structural-analogy] sequential exchangeability ↔ sequential/adaptive Bayesian experimentation: assignment may depend on observed past but not on unobserved outcome drivers.
- [metaphor] SWIG node splitting ↔ conditioning vs intervening in Bayesian networks: separate the value "as observed" from the value "set by the analyst".

## Questions this raises
- How exactly do the g-formula, IP weighting and g-estimation compute $E[Y^g]$, and why do ordinary regression adjustments fail for time-varying confounders?
- How does the framework extend to censoring, time-varying outcomes and failure-time outcomes (the text points to Technical Point 21.8)?
- How could one assess sensitivity to unmeasured confounding when sequential exchangeability cannot be tested?
- How should one choose among the very many possible strategy contrasts for a real study?

## Reading notes
- Printed page = pdf page − 9 (pdf 264–275 = printed 255–266). The page labels give the printed numbers.
- The source is an online revision (per the metadata note), not necessarily the 2020 print edition; cross-references to later chapters (e.g. Technical Points 21.8, 21.10, Chapter 21) refer to material not in this unit.
- Possible slip on p. 256: the text says "at least $2^K$" static strategies and "$2^K$ combinations $(a_0,\dots,a_K)$", but $k=0,\dots,K$ has $K+1$ entries, which would give $2^{K+1}$. The digest follows the text.
- Inconsistent coding on p. 259 (image checked): $L_k=1$ is defined as low CD4 on p. 256, but p. 259 describes untreated people with high CD4 count as $(A_{k-1}=0, L_k=1)$ (probability 0.4) and those with low CD4 count as $L_k=0$ (probability 0.8). The digest reports the verbal labels and flags the mismatch.
- On p. 264 the Figure 19.10 paragraph says the mean cannot be identified for any strategy $g$ (there $g=[g_0,g_1(L_1)]$ is dynamic), while the summary later on that page says static strategies can be validly estimated under Figure 19.6. The digest reads the first statement as being about dynamic strategies, following the summary.
- Equations and figures were checked against the page images; no unreadable parts.
- The acronym SWIG is not expanded on these pages; the expansion used here (single-world intervention graph) is not taken from this unit.
- In Technical Point 19.1 the recursion for $g'_k$ is printed with the inner term written as $g'_k(\bar l_{k-1})$; the digest keeps this notation.
