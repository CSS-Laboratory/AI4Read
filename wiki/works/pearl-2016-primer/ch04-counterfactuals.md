---
id: pearl-2016-primer/ch04-counterfactuals
work: pearl-2016-primer
unit: "4 Counterfactuals and Their Applications"
pages: 89–126
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Counterfactuals and Their Applications

## L0 — One line
A counterfactual $Y_x(u)$ is the value $Y$ takes in unit $u$'s world after the equation for $X$ is replaced by $X=x$. This lets one compute and, under conditions, estimate individual-level and self-selected-group causal quantities (treatment on the treated, necessity, mediation) that the do-operator cannot express.

## L1 — The gist (≤ 120 words)
How can we state and compute what would have happened had X been different for a particular unit, when do-expressions only describe whole populations? The chapter defines $Y_x(u)$ as the solution for $Y$ in the surgically modified model $M_x$. It computes counterfactuals in three steps: abduction, action, prediction. They can be read from graphs and estimated from data under conditions such as back-door adjustment, monotonicity or no confounding. Applications: effect of treatment on the treated, additive interventions, probabilities of necessity and sufficiency, and natural direct and indirect effects. These matter because policy, legal and personal questions often concern individuals or self-selected groups.

**Prerequisites:** structural equations and the do-operator (surgery on a model); back-door criterion and the adjustment formula; d-separation and colliders; conditional probability; simple linear models.

## L2 — Key ideas (5–10 bullets)
- **Why do-notation is not enough.** Expressions like $E(Y_1\mid X=0,Y=1)$ mix two "worlds", so they need subscript notation; neither randomized trials nor do-expressions deliver them directly (pp. 90–91).
- **Fundamental law (Eq. 4.5).** $Y_x(u)=Y_{M_x}(u)$. Every fully specified structural model gives a definite value to every counterfactual, and these values obey the consistency rule (pp. 92–94).
- **Three-step computation.** Abduction (update $U$ from evidence), action (replace the equation for $X$), prediction. It also works with probabilities over $U$, and cross-world probabilities come from summing over rows of a table (pp. 96–98).
- **Graphical reading.** Back-door sets render $Y_x$ independent of $X$ given $Z$ (Theorem 4.3.1), which recovers the adjustment formula. Conditioning on a collider explains why education matters for salary within a skill level (pp. 101–103).
- **Linear models.** Theorem 4.3.2 turns population slopes into individual-level counterfactuals. In linear models the effect of treatment on the treated equals the average effect (pp. 106–107).
- **Treatment on the treated and additive interventions.** When a back-door set $Z$ exists, the effect of treatment on the treated (ETT) is estimable (Eq. 4.21), and so are additive interventions (Eq. 4.22), though neither is a do-expression (pp. 108–111).
- **Probabilities of causation.** The probabilities of necessity (PN), of sufficiency (PS), and of necessity and sufficiency (PNS) formalize the legal "but for" test, regret, and being both necessary and sufficient. Under monotonicity (the outcome never decreases when $X$ goes from 0 to 1, i.e. $Y_1(u)\ge Y_0(u)$ for all $u$), PN is identified from experimental plus observational data. Without monotonicity, bounds (Eq. 4.30) hold (pp. 112–120).
- **Mediation.** The total effect (TE), controlled direct effect (CDE), natural direct effect (NDE) and natural indirect effect (NIE) are defined by nested counterfactuals. Conditions A-1 to A-4 are sufficient to identify the natural effects; without confounding they reduce to the mediation formulas (pp. 121–124).

## L3 — Walkthrough

### 4.1 Counterfactuals (pp. 89–91)
- **Freeway story.** The author took Sepulveda ($X=0$) instead of the freeway ($X=1$) and the drive took 1 hour. his regret means: on that same day, with the same driving habits, the freeway time would have been lower than the actual time (p. 89).
- **Terms.** A *counterfactual* is an "if" statement whose "if" part is unrealized. The "if" part is the *antecedent*. Knowing the actual outcome matters: the observed 1 hour is evidence about that day's conditions, so the retrospective estimate differs from the prospective one (p. 89).
- **Why do fails.** Writing $E(\text{driving time}\mid do(\text{freeway}),\text{driving time}=1\text{ hour})$ clashes: the same variable would be both hypothetical and observed. The do-operator separates two probabilities, $P(\cdot\mid do(\text{freeway}))$ and $P(\cdot\mid do(\text{Sepulveda}))$, but not the two variables themselves (p. 90).
- **Subscript notation.** Let $Y_{X=1}$ (or $Y_1$) be freeway time and $Y_{X=0}$ (or $Y_0$) Sepulveda time. The target quantity is
$$E(Y_{X=1}\mid X=0,\,Y=Y_0=1)\tag{4.1}$$
- **Contrast with interventions.** $E[Y\mid do(X=x)]$ (Eq. 4.2) could be written $E[Y_{X=x}]$, because all variables are in one world. In (4.1), $Y_{X=1}$ and $X=0$ refer to different "worlds" (p. 90).
- **Consequences.** (4.1) cannot be reduced to a do-expression. A randomized trial gives only $E[Y_1]$ and $E[Y_0]$, because one cannot take both roads at once. Measuring another day or another driver gives only an approximation. Approximations can estimate a target but should not define it, so we need subscripts, with $Y_1$ the "would-be" time at that juncture (p. 91).
- **Preview.** Structural models can compute counterfactuals for fully specified models and estimate them from data when functions are unknown or some variables are unmeasured. Promised uses: job training, additive interventions, individual cancer decisions, discrimination, direct and indirect effects (p. 91).

### 4.2 Defining and computing counterfactuals

#### 4.2.1 Structural interpretation (pp. 91–93)
- In a fully specified deterministic model, each assignment $U=u$ determines all variables in $V$. So $u$ stands for one "unit" or "situation": $X(u)$ is Joe's salary, $Y(u)$ is the yield of lot $u$ (p. 92).
- The sentence $Y$ would be $y$ had $X$ been $x$ in situation $u$ is written $Y_x(u)=y$. The phrase had $X$ been $x$ is read as a minimal modification of the model: replace the equation for $X$ by the constant $x$, i.e. an external $do(X=x)$, not necessarily by a human. This keeps the equations consistent even if $x\neq X(u)$ (p. 92).
- Example model:
$$X=aU\tag{4.3}$$
$$Y=bX+U\tag{4.4}$$
  - $M_x$ replaces the first equation by $X=x$, so $Y_x(u)=bx+u$.
  - For $X_y(u)$, replace the second equation by $Y=y$; then $X_y(u)=au$. $X$ is unchanged by "had $Y$ been $y$", reflecting that hypothesizing future events does not alter the past (p. 93).
- **Table 4.1** ($U\in\{1,2,3\}$, $a=b=1$) gives $X(u)=u$, $Y(u)=2u$, $Y_x(u)=x+u$, $X_y(u)=u$. Example: $Y_2(2)=2+2=4$. Rows are $u=1,2,3$, and $Y_1=2,3,4$; $Y_2=3,4,5$; $Y_3=4,5,6$ (p. 93).
- **Counterfactual versus do.** Here we computed the actual value $Y_x(u)$ for each unit. The do-operator is defined on distributions and always returns probabilistic results such as $E[Y\mid do(x)]$ (it deletes the factor $P(x_i\mid pa_i)$ from Eq. 1.29). So do describes a population under intervention, while $Y_x(u)$ describes a specific individual. This gap allows definitions of credit, blame and regret (p. 93).

#### 4.2.2 The fundamental law (pp. 93–94)
- Let $M_x$ be $M$ with the equation of $X$ replaced by $X=x$:
$$Y_x(u)=Y_{M_x}(u)\tag{4.5}$$
  The counterfactual in $M$ is the solution for $Y$ in the "surgically modified" submodel $M_x$. This also holds for sets $X$ and $Y$, replacing all equations of members of $X$ (p. 94).
- The many counterfactual values are not arbitrary; they must cohere with one underlying model. Example: if $X(u)=1$ and $Y(u)=0$, then $Y_{X=1}(u)=0$ (p. 94).
- **Consistency rule:**
$$\text{if } X=x \text{ then } Y_x=Y\tag{4.6}$$
  For binary $X$: $Y=XY_1+(1-X)Y_0$. Computing through (4.5) satisfies these automatically (p. 94).

*Intuition note.* A model is a recipe for the world. Asking what would happen if $X$ were $x$ means changing one ingredient and rerunning the recipe for the same unit. The answer is a definite number, not a probability.

#### 4.2.3 From population data to individual behaviour (pp. 94–96)
- **Model 4.1** (encouragement design; standardized variables with mean 0 and variance 1; the $U$'s independent; Figure 4.1):
$$X=U_X,\quad H=aX+U_H,\quad Y=bX+cH+U_Y$$
  $X$ is time in a remedial program, $H$ homework, $Y$ exam score, with $a=0.5$, $b=0.7$, $c=0.4$ (coefficients estimable from population data) (pp. 94–95).
- **Joe:** $X=0.5$, $H=1$, $Y=1.5$. Query: Joe's score had he doubled his homework?
  - The $U$'s capture all variation among individuals and do not change under hypothetical actions, so they can be recovered from the evidence: $U_X=0.5$, $U_H=1-0.5\cdot0.5=0.75$, $U_Y=1.5-0.7\cdot0.5-0.4\cdot1=0.75$ (p. 95).
  - Replace the equation for $H$ by $H=2$ (Figure 4.2):
$$Y_{H=2}(U_X{=}0.5,U_H{=}0.75,U_Y{=}0.75)=0.5\cdot0.7+2.0\cdot0.4+0.75=1.90$$
  - Joe's score would be 1.9 instead of 1.5 standard deviations above the mean (p. 96).

#### 4.2.4 The three steps (pp. 96–98)
- **Deterministic counterfactual:** (i) *Abduction*: use evidence $E=e$ to determine $U$. (ii) *Action*: replace the equations of the variables in $X$ by $X=x$, giving $M_x$. (iii) *Prediction*: use $M_x$ and $U$ to compute $Y$. Temporally: explain the past, bend history minimally, predict the future (p. 96).
- Counterfactuals are thus derived properties of structural equations. (Some frameworks take them as primitives: Holland 1986; Rubin 1974.) *Probabilistic* counterfactuals concern a class of units, e.g. students with $Y<2$ doubling homework. Unlike do-interventions, they restrict who is intervened upon (p. 96).
- **Probabilistic version.** With evidence on only some variables, Joe belongs to a class of units with different $u$. Nondeterminism enters through $P(U=u)$, which induces $P(v)$ and joint distributions of observed and counterfactual variables, e.g. $P(Y_x=y,Z_w=z,X=x')$, where $w$ or $x'$ may conflict with $x$ (p. 97).
- A typical query is $E[Y_{X=x}\mid E=e]$, where $e$ may conflict with $X=x$. The three steps become: (i) update $P(U)$ to $P(U\mid E=e)$; (ii) same action step; (iii) compute the expectation of $Y$ in $M_x$ under $P(U\mid E=e)$ (p. 97).
- The same procedure covers some interventions where each unit's action depends on its own current $X$. Examples: adding 5 mg/l insulin to everyone (final level varies, so not a do-expression), or sending students with $H\le H_0$ to the program ($X=1$). The latter cannot be done by simply setting $X=1$ when $H$ is low, because $X$ causes $H$. It is $E[Y_{X=1}\mid H\le H_0]$ (pp. 97–98).

### 4.3 Nondeterministic counterfactuals

#### 4.3.1 Probabilities of counterfactuals (pp. 98–101)
- Give the three types of Table 4.1 probabilities $P(U=1)=\tfrac12$, $P(U=2)=\tfrac13$, $P(U=3)=\tfrac16$. Probability of any counterfactual condition = sum of probabilities of the rows where it holds (p. 98).
  - $P(Y_2=3)=\tfrac12$, $P(Y_1=4)=\tfrac16$, $P(Y_1=3)=\tfrac13$, $P(Y_2>3)=\tfrac12$.
  - Cross-world events: $P(Y_2>3,Y_1<4)=\tfrac13$ (only $U=2$), $P(Y_1<4,\,Y-X>1)=\tfrac13$, $P(Y_1<Y_2)=1$.
  - $P(Y_3>Y\mid Y>2)=\tfrac13/\tfrac12=\tfrac23$.
  - $Y_{x+1}-Y_x$ is independent of $x$: the causal effect does not vary across types, as in all linear models (pp. 98–99).
- Joint probabilities of several counterfactual worlds, $P(Y_1=y_1,Y_2=y_2)$, cannot be written with do, which gives one probability per intervention (p. 99).
- **Education–skill–salary model** (Figure 4.3):
$$X=U_1,\quad Z=aX+U_2,\quad Y=bZ\tag{4.7}$$
  $X=1$ is college, $U_2=1$ professional experience, $Z$ skill, $Y$ salary. Target: $E[Y_{X=1}\mid Z=1]$, the salary of people at skill 1 had they gone to college (p. 99).
  - $E[Y\mid do(X=1),Z=1]$ is different. It describes people who all went to college and then reached skill 1, so conditioning on $Z$ cuts the effect of $X$. It leaves out current-$Z{=}1$ people who skipped college and would have gained skill from it:
$$E[Y\mid do(X=1),Z=1]\neq E[Y_{X=1}\mid Z=1]\tag{4.8}$$
  - Further check: $E[Y\mid do(X=1),Z=1]=E[Y\mid do(X=0),Z=1]$, but $E[Y_{X=1}\mid Z=1]\ne E[Y_{X=0}\mid Z=1]$ (p. 99).
- **Translation.** $E[Y\mid do(X=1),Z=1]$ equals $E[Y_{X=1}\mid Z_{X=1}=1]$, marking $Z=1$ as postintervention. By Bayes' rule, $P(y\mid do(X=1),z)=P(y,z\mid do(X=1))/P(z\mid do(X=1))$. If $Z$ is a preintervention variable (like age), $Z_{X=1}=Z$ and (4.8) becomes an equality (p. 100).
- **Table 4.2** (rows $(u_1,u_2)$: (0,0), (0,1), (1,0), (1,1)): $Z(u)=0,1,a,a+1$; $Y_0=0,b,0,b$; $Y_1=ab,(a+1)b,ab,(a+1)b$; $Z_0=0,1,0,1$; $Z_1=a,a+1,a,a+1$ (p. 100).
  - From it:
$$E[Y_1\mid Z=1]=(a+1)b\tag{4.9}$$
$$E[Y_0\mid Z=1]=b\tag{4.10}$$
$$E[Y\mid do(X=1),Z=1]=b\tag{4.11}$$
$$E[Y\mid do(X=0),Z=1]=b\tag{4.12}$$
  - So $E[Y_1-Y_0\mid Z=1]=ab\neq0$, even though $Z$ separates $X$ from $Y$ in the graph. Footnote 2 says (4.11) is strictly undefined, since $Z=1$ is impossible after $do(X=1)$; one imagines an error term (p. 100).
  - Reason: salary at $Z=1$ depends only on skill, but those at $Z=1$ would have had different salaries with a different past. This "unrealized past" is not visible in Figure 4.3 (pp. 100–101).
- **Role of probabilities.** For $a\neq0,1$, $Z=1$ occurs only at $(u_1,u_2)=(0,1)$, so $P(u_1),P(u_2)$ do not matter. For $a=1$, $Z=1$ occurs at (0,1) and (1,0):
$$E[Y_{X=1}\mid Z=1]=b\left(1+\frac{P(u_1{=}0)P(u_2{=}1)}{P(u_1{=}0)P(u_2{=}1)+P(u_1{=}1)P(u_2{=}0)}\right)\tag{4.13}$$
$$E[Y_{X=0}\mid Z=1]=b\left(\frac{P(u_1{=}0)P(u_2{=}1)}{P(u_1{=}0)P(u_2{=}1)+P(u_1{=}1)P(u_2{=}0)}\right)\tag{4.14}$$
  The first is larger. Reason given: a nonzero fraction at $Z=1$ had no college and would have reached $Z_1=2$, salary $2b$ (p. 101).
- Study question 4.3.1 (Gaussian $U_1,U_2$; show $E[Y_x\mid Z=z]=abx+bz/(1+a^2)$) is listed under Exercises (p. 101).

*Intuition note.* Within a group defined by a current outcome, people differ in what would have happened under another past. Such "cross-world" quantities are computed by listing units with their counterfactual values and summing probabilities, though do-notation cannot express them.

#### 4.3.2 Graphical representation (pp. 101–103)
- By Eq. (4.5), the node $Y$ in the modified graph $M_x$ (arrows into $X$ removed) acts as a surrogate for $Y_x$, valid only under the modification (Figure 4.4) (p. 101).
- Variation in $Y_x$ comes from variables that influence $Y$ when $X$ is held fixed: parents of $Y$ and parents of nodes on paths from $X$ to $Y$. In Figure 4.4(b) these are $\{Z_3,W_2,U_3,U_Y\}$. A set that blocks a path to these parents blocks that path to $Y_x$. A back-door set $Z$ therefore makes $X$ and $Y_x$ independent in each stratum (p. 102).
- **Theorem 4.3.1 (Counterfactual interpretation of back-door).** If $Z$ satisfies the back-door condition relative to $(X,Y)$, then for all $x$:
$$P(Y_x\mid X,Z)=P(Y_x\mid Z)\tag{4.15}$$
- Consequently $P(Y_x=y)$ is identified by the adjustment formula:
$$P(Y_x=y)=\sum_z P(Y_x=y\mid Z=z)P(z)=\sum_z P(Y_x=y\mid Z=z,X=x)P(z)=\sum_z P(Y=y\mid Z=z,X=x)P(z)\tag{4.16}$$
  Line 2 uses Theorem 4.3.1; line 3 uses consistency (4.6). The derivation is purely algebraic once $Z$ satisfies the criterion. Eq. (4.15) is sometimes called "conditional ignorability"; the theorem lets us test whether it holds in a model (pp. 102–103).
- **Education–salary revisited.** $Y_x$ can be identified with $U_2$, the only parent of nodes on the causal path. $Z$ is a collider between $X$ and $U_2$, so $X$ and $Y_x$ are not d-separated given $Z$. Hence $E[Y_x\mid X,Z]\neq E[Y_x\mid Z]$, although $E[Y\mid X,Z]=E[Y\mid Z]$. The method needs no linearity. "Twin networks" are another visualization (Pearl 2000, pp. 213–215) (p. 103).

*Intuition note.* Holding $X$ fixed leaves only the other causes of $Y$ driving $Y_x$. If conditioning on $Z$ blocks the routes between $X$ and these causes, $X$ tells us nothing more about $Y_x$. A collider has the opposite effect: conditioning on it links $X$ to $U_2$.

#### 4.3.3 Experimental settings (pp. 103–105)
- **Table 4.3**: ten participants (Joe is #1) with $U$'s uniform on $[0,1]$. The model fills in observed $X,Y,H$ and potential outcomes $Y_0,Y_1,H_0,H_1$ and more (e.g. $Y_{00}$). Joe's row: $Y_0=1.05$, $Y_1=1.95$, $H_0=0.75$, $H_1=1.25$. With the complete table, any counterfactual probability could be found by counting rows (p. 104).
- This table cannot be seen in practice. Without a parametric model, the only link between $\{Y_1,Y_0\}$ and observed data is consistency (4.6). Most individual counterfactuals stay unobserved, but population-level expectations can be learned (p. 104).
- **Table 4.4** (randomized trial; participants 1, 5, 6, 8, 10 get $X=0$): each unit shows only one potential outcome. The study average treatment effect is 0.68, against the true 0.90 (every unit has $Y_1-Y_0=0.9$ in Table 4.3). Randomization scatters the unobserved entries independently of $Y_0,Y_1$, so the difference of group means converges to $E(Y_1-Y_0)=0.9$. Randomization makes $X$ independent of all other causes of $Y$, so (4.16) applies with $Z=\{\}$: $E[Y_x]=E[Y\mid X=x]$ (p. 105).

#### 4.3.4 Linear models (pp. 106–107)
- In nonparametric models, $E[Y_{X=x}\mid Z=z]$ may not be identifiable even with experiments. In fully linear models, every counterfactual is identifiable when the model parameters are. Parameters are experimentally identifiable, so every counterfactual is experimentally identifiable. Any $E[Y_{X=x}\mid e]$ is identified whenever $E[Y\mid do(X=x)]$ is (Pearl 2000, p. 389) (p. 106).
- **Theorem 4.3.2.** Let $\tau=E[Y\mid do(x+1)]-E[Y\mid do(x)]$ be the slope of the total effect of $X$ on $Y$. Then for any evidence $Z=e$:
$$E[Y_{X=x}\mid Z=e]=E[Y\mid Z=e]+\tau\,(x-E[X\mid Z=e])\tag{4.17}$$
  Take the best estimate of $Y$ given the evidence, then add the change expected when $X$ moves from its current best estimate to $x$ (p. 106).
- **Effect of treatment on the treated:**
$$ETT=E[Y_1-Y_0\mid X=1]\tag{4.18}$$
  Substituting $e=\{X=1\}$ into (4.17): $ETT=E[Y\mid X=1]-E[Y\mid X=1]+\tau(1-E[X\mid X=1])-\tau(0-E[X\mid X=1])=\tau=b+ac=0.9$. In linear systems, $E[Y_{x+1}-Y_x\mid e]=\tau$ for any evidence (p. 106). (The text also writes the evidence of Figure 4.2 as $Y=1$ here, where p. 95 has $Y=1.5$; see Reading notes.)
- With a multiplicative interaction (arrow $X\to H$ reversed and $Y=bX+cH+\delta XH+U_Y$, Eq. 4.19), $\tau$ differs from ETT; the author states $\tau-ETT=\delta a/(1+a^2)$ and leaves it as Study question 4.3.2(c) (p. 107).

*Intuition note.* In a linear model, a shift in $X$ has the same effect on everyone. So the counterfactual for a person is their best-guess outcome plus the slope times the shift in $X$.

### 4.4 Practical uses of counterfactuals (pp. 107–116)

#### 4.4.1 Recruitment to a program (pp. 107–109)
- **Example 4.4.1.** A pilot randomized trial shows a job training program works. After open enrollment, the hiring rate among graduates is even higher. **Critics** say there is no proof the program works for those who enroll voluntarily, because self-enrollees are, they say, more resourceful and more likely to have found a job regardless of training. They want the effect of training on the trained (pp. 107–108):
$$ETT=E[Y_1-Y_0\mid X=1]\tag{4.20}$$
  Again a clash of worlds: $E[Y_0\mid X=1]$ asks about trained people had they not been trained. Despite the clash, it is reducible to estimable expressions in many, though not all, situations (p. 108).
- **Back-door case.** If $Z$ satisfies the back-door criterion:
$$P(Y_x=y\mid X=x')=\sum_z P(Y=y\mid X=x,Z=z)\,P(Z=z\mid X=x')\tag{4.21}$$
  Proof: $P(Y_x=y\mid x')=\sum_z P(Y_x=y\mid z,x')P(z\mid x')$. Theorem 4.3.1 allows replacing $x'$ by $x$, and (4.6) removes the subscript. Compared with the standard adjustment, $P(Z=z\mid X=x')$ replaces $P(Z=z)$ as weights (p. 108).
- Hence $ETT=E[Y\mid X=1]-\sum_z E[Y\mid X=0,Z=z]P(Z=z\mid X=1)$, using consistency for $E[Y_1\mid X=1]=E[Y\mid X=1]$ (p. 109).
- ETT is also identifiable for binary $X$ when both experimental and observational data exist, and when a front-door mediator exists. In each case the graph tells whether and how ETT is estimable (p. 109).
- Study question 4.4.1 is listed under Exercises (p. 109).

#### 4.4.2 Additive interventions (pp. 109–111)
- **Example 4.4.2.** Adding 5 mg/l of insulin to patients with varying levels, without disabling the other causes of insulin. A unit at $X=x'$ moves to $x=x'+q$, with outcome $Y_{x'+q}$. Averaged over units at $x'$ this is $E[Y_x\mid x']$, an ETT expression (pp. 109–110).
- With a back-door set $Z$, the effect of this policy, $add(q)$, is estimable:
$$E[Y\mid add(q)]-E[Y]=\sum_{x'}E[Y_{x'+q}\mid X=x']P(X=x')-E[Y]=\sum_{x'}\sum_z E[Y\mid X=x'+q,Z=z]P(Z=z\mid X=x')P(X=x')-E[Y]\tag{4.22}$$
  $Z$ may contain age, weight, genetic disposition, if measured and satisfying the back-door condition. Estimability holds in all other cases where ETT is identifiable (p. 110).
- **Why not just run a trial?** The text answers that counterfactuals are needed because $E[Y\mid add(q)]$ cannot be reduced to do-expressions, in which scientists report results. A specially designed experiment could estimate it. The scientific quantity $E[Y\mid do(X=x+q)]-E[Y\mid do(X=x)]$ is invariant across populations. The additive policy depends on $P(X=x)$ in the population, which creates a mismatch between science and policy (p. 110).
- **Why not average the do-effect?** $\sum_x [E[Y\mid do(X=x+q)]-E[Y\mid do(X=x)]]P(X=x)$ does not equal the policy effect. People at level $x$ by free choice may react differently from people assigned $x$ by experiment. In counterfactual terms:
$$E[Y\mid add(q)]=\sum_x E[Y_{x+q}\mid x]P(x)\neq\sum_x E[Y_{x+q}]P(x)$$
  Equality holds only when $Y_x$ is independent of $X$ (nonconfounding) (p. 111).
- Study question 4.4.2 (Joe deciding to smoke) is listed under Exercises (p. 111).

#### 4.4.3 Personal decision making (pp. 111–113)
- **Example 4.4.3.** Ms Jones chose lumpectomy plus irradiation and is alive after 10 years. She asks whether she owes her life to irradiation. Mrs Smith had lumpectomy alone, her tumor recurred, and she regrets not choosing irradiation. A randomized 20-year trial (Fisher et al., NEJM, 2002) found fewer recurrences with irradiation (14% vs 39%). These are population results (pp. 111–112).
- With $Y=1$ remission and $X=1$ irradiation:
$$PN=P(Y_0=0\mid X=1,Y=1)\tag{4.23}$$
  the *probability of necessity*: remission would not have occurred without irradiation, given that she was irradiated and remission occurred.
$$PS=P(Y_1=1\mid X=0,Y=0)\tag{4.24}$$
  the *probability of sufficiency*, for Mrs Smith's regret. Together they are "probabilities of causation", used in attribution (legal, personal). In general they are not estimable from observational or experimental data alone, but they are under certain conditions when both are available (p. 112).
- **Why compute them?** The author argues that regret and success are involved in adaptive learning: confirming or refuting a decision strategy helps improve it (p. 112).
- **Ms Daily** reasons that irradiation is worthwhile only if her tumor remits with treatment and recurs without:
$$PNS=P(Y_1=1,Y_0=0)\tag{4.25}$$
  probability that irradiation is necessary and sufficient. Experiments alone cannot give PNS, but with *monotonicity* (irradiation cannot cause a recurrence of a tumor that was about to remit), experimental data suffice (Section 4.5.1, Eq. 4.42):
$$PNS=P(Y=1\mid do(X=1))-P(Y=1\mid do(X=0))\tag{4.26}$$
  With Fisher et al.: $PNS=0.86-0.61=0.25$, a 25% chance that her tumor remits under irradiation and recurs without it (p. 113).

#### 4.4.4 Discrimination in hiring (p. 114)
- **Example 4.4.4.** Mary sues XYZ International, alleging that she was not hired because she said she is gay (p. 113). The court test quoted: whether the employer would have taken the same action had the employee been of a different race, sex, etc., everything else the same. This is an individual-level, counterfactual criterion (p. 114).
- It is the probability of sufficiency $PS=P(Y_1=1\mid X=0,Y=0)$, with $Y$ hiring and $X$ the interviewer's *perception* of Mary's orientation. Perception is chosen because we can imagine she never mentioned it. The text says it will show (referring to "4.5.2") that discrimination cannot be proved in individual cases, but its probability can be determined and may sometimes approach certitude (p. 114).

#### 4.4.5 Mediation and path-disabling interventions (pp. 114–116)
- **Example 4.4.5.** A policy maker compares making hiring gender-blind (direct effect of gender) with educational reform (indirect effect via qualification). These disable processes, not set values, so do cannot express them. The antecedent is the end result: all female applicants are treated as male (p. 115).
- The hiring status of a woman with qualification $q$ treated as male is $Y_{X=1,Q=q}$. Averaging over female ($X=0$) and male qualification distributions and subtracting gives the *natural indirect effect* (NIE):
$$\sum_q E[Y_{X=1,Q=q}]\,[P(Q=q\mid X=0)-P(Q=q\mid X=1)]$$
  Qualification varies naturally, unlike the controlled direct effect of Chapter 3, where the mediator is held constant (p. 115).
- Without confounding (Pearl 2001):
$$NIE=\sum_q E[Y\mid X=1,Q=q][P(Q=q\mid X=0)-P(Q=q\mid X=1)]$$
  This is the *mediation formula*; it measures how much of the effect of $X$ on $Y$ is explained by its effect on the mediator (pp. 115–116).

### 4.5 Mathematical tool kits (p. 116)
Recurring patterns: ETT $E[Y_x\mid X=x']$; the probability of necessity (attribution, legal liability); and the nested expression $E[Y_{x,M_{x'}}]$ for mediation (p. 116).

#### 4.5.1 Attribution and probabilities of causation (pp. 116–120)
- For binary $X$ (values $x$, $x'$) and $Y$ (values $y$, $y'$), the English target is the probability that, had $X$ been $x'$, $Y$ would be $y'$, given that in reality $X$ is $x$ and $Y$ is $y$:
$$PN(x,y)=P(Y_{x'}=y'\mid X=x,Y=y)\tag{4.27}$$
  This is the legal "but for" criterion: judgment for the plaintiff if and only if it is more probable than not that the damage would not have occurred but for the defendant's action (Robertson 1997) (p. 117).
- **Theorem 4.5.1.** If $Y$ is monotonic relative to $X$, i.e. $Y_1(u)\ge Y_0(u)$ for all $u$, then $PN$ is identifiable whenever $P(y\mid do(x))$ is identifiable, and
$$PN=\frac{P(y)-P(y\mid do(x'))}{P(x,y)}\tag{4.28}$$
  Substituting $P(y)=P(y\mid x)P(x)+P(y\mid x')(1-P(x))$:
$$PN=\frac{P(y\mid x)-P(y\mid x')}{P(y\mid x)}+\frac{P(y\mid x')-P(y\mid do(x'))}{P(x,y)}\tag{4.29}$$
  (added step: $P(y)-P(y\mid x')=P(x)[P(y\mid x)-P(y\mid x')]$ and $P(x,y)=P(y\mid x)P(x)$, which splits (4.28) into the two terms.)
  - The first term is the *excess risk ratio* (ERR), used in court without experimental data (it is also the attributable risk fraction among the exposed).
  - The second is the *confounding factor* (CF), a correction when $P(y\mid do(x'))\neq P(y\mid x')$. Car example: if buyers of the manufacturer's cars drive faster, CF corrects for that bias (p. 117).
- Without monotonicity, (4.28) is a lower bound (Tian and Pearl 2000):
$$\max\left\{0,\frac{P(y)-P(y\mid do(x'))}{P(x,y)}\right\}\le PN\le\min\left\{1,\frac{P(y'\mid do(x'))-P(x',y')}{P(x,y)}\right\}\tag{4.30}$$
- In terms of ERR, CF and $q$:
$$LB=ERR+CF,\qquad UB=ERR+q+CF\tag{4.31}$$
$$CF\triangleq[P(y\mid x')-P(y_{x'})]/P(x,y)\tag{4.32}$$
$$ERR\triangleq1-1/RR=1-P(y\mid x')/P(y\mid x)\tag{4.33}$$
$$q\triangleq P(y'\mid x)/P(y\mid x)\tag{4.34}$$
  (pp. 117–118)
- Figure 4.5 shows three features: (i) the width $UB-LB$ is constant and depends on one observable, $P(y'\mid x)/P(y\mid x)$; (ii) CF may lift the lower bound above $\tfrac12$ when ERR alone does not; (iii) the rise in both bounds is CF, the only quantity needed from the experiment ($P(y_x)-P(y_{x'})$ is not needed). Under monotonicity the bounds coincide, not because $q=0$ but because of the shift to (4.28) (p. 118).
- **Example 4.5.1 (legal).** Plaintiff and manufacturer argue about drug $x$ and the death of Mr A, who took it by choice. Manufacturer: experimental data show only minor effects. **Plaintiff:** the trial's subjects took the drug by protocol; observational data on self-choosers show lower death rates. Table 4.5 (hypothetical, sampling variability ignored): experimental $do(x)$: 16 deaths, 984 survivals; $do(x')$: 14, 986; nonexperimental $x$: 2, 998; $x'$: 28, 972 (p. 119).
  - $P(y\mid do(x))=0.016$, $P(y\mid do(x'))=0.014$, $P(y)=30/2000=0.015$, $P(x,y)=2/2000=0.001$, $P(y\mid x)=0.002$, $P(y\mid x')=0.028$ (Eqs. 4.35–4.40) (p. 119).
  - Assuming the drug can only cause death (monotonicity):
$$PN=\frac{0.002-0.028}{0.002}+\frac{0.028-0.014}{0.001}=-13+14=1\tag{4.41}$$
  - The observational ERR is $-13$, but the correction $+14$ gives $PN=1$. The lower bound in (4.30) equals 1, so $PN=1$ even without monotonicity. Barring sampling error, the data give the plaintiff certainty (p. 120).
- Under monotonicity (Eq. 4.42):
$$PNS=P(Y_x=1,Y_{x'}=0)=P(Y_x=1)-P(Y_{x'}=1)$$
  PS and PNS can be bounded similarly (Pearl 2000, ch. 9; Tian and Pearl 2000) (p. 120).
- Study question 4.5.1 is listed under Exercises (p. 120).

*Intuition note.* PN asks how likely it is that a harmed exposed person would have been fine without the exposure. Exposed people differ from unexposed ones, so the raw risk ratio can mislead, even in sign (here $-13$ versus $PN=1$). The confounding term uses experimental data to repair this.

#### 4.5.2 A tool kit for mediation (pp. 120–124)
- **Canonical model:**
$$t=f_T(u_T),\quad m=f_M(t,u_M),\quad y=f_Y(t,m,u_Y)\tag{4.43}$$
  $f_T,f_M,f_Y$ arbitrary, $U=(U_T,U_M,U_Y)$ omitted factors. In Figure 4.6(a) the $U$'s are independent; in 4.6(b) dashed arcs allow dependence (p. 120).
- **Four effects** for $T=0\to1$ (expectations over $U_M,U_Y$; population level) (p. 121):
$$TE=E[Y_1-Y_0]=E[Y\mid do(T=1)]-E[Y\mid do(T=0)]\tag{4.44}$$
$$CDE(m)=E[Y_{1,m}-Y_{0,m}]=E[Y\mid do(T=1,M=m)]-E[Y\mid do(T=0,M=m)]\tag{4.45}$$
$$NDE=E[Y_{1,M_0}-Y_{0,M_0}]\tag{4.46}$$
$$NIE=E[Y_{0,M_1}-Y_{0,M_0}]\tag{4.47}$$
  - TE: mediator tracks $T$ naturally.
  - CDE: mediator set to $m$ for everyone.
  - NDE: mediator at the value each unit would have under $T=0$.
  - NIE: $T$ held at 0 while $M$ changes to the value it would have under $T=1$; the part explained by mediation alone, disabling $Y$'s response to $T$.
- **Decomposition** (with $NIE_r$ the NIE for the reverse transition $T=1\to0$):
$$TE=NDE-NIE_r\tag{4.48}$$
  So NIE is identifiable whenever NDE and TE are. In linear systems, $TE=NDE+NIE$. TE and CDE are do-expressions, but NDE and NIE need new assumptions (p. 122).
- **Conditions A-1 to A-4** (sufficient): there exists a measured set $W$ such that A-1 no member of $W$ is a descendant of $T$; A-2 $W$ blocks all back-door paths from $M$ to $Y$ (after removing $T\to M$ and $T\to Y$); A-3 the $W$-specific effect of $T$ on $M$ is identifiable; A-4 the $W$-specific joint effect of $\{T,M\}$ on $Y$ is identifiable (p. 122).
- **Theorem 4.5.2.** Under A-1 and A-2, NDE is experimentally identifiable:
$$NDE=\sum_m\sum_w\big[E[Y\mid do(T{=}1,M{=}m),W{=}w]-E[Y\mid do(T{=}0,M{=}m),W{=}w]\big]\,P(M{=}m\mid do(T{=}0),W{=}w)P(W{=}w)\tag{4.49}$$
  The do-terms are identifiable by A-3 and A-4 (back-door or front-door criteria).
- **Corollary 4.5.1.** If $W$ also deconfounds the relations in A-3 and A-4:
$$NDE=\sum_m\sum_w\big[E[Y\mid T{=}1,M{=}m,W{=}w]-E[Y\mid T{=}0,M{=}m,W{=}w]\big]P(M{=}m\mid T{=}0,W{=}w)P(W{=}w)\tag{4.50}$$
  With no confounding (Figure 4.6a):
$$NDE=\sum_m\big[E[Y\mid T{=}1,M{=}m]-E[Y\mid T{=}0,M{=}m]\big]P(M{=}m\mid T{=}0)\tag{4.51}$$
  and, from (4.48) and $TE=E[Y\mid T{=}1]-E[Y\mid T{=}0]$:
$$NIE=\sum_m E[Y\mid T{=}0,M{=}m]\,[P(M{=}m\mid T{=}1)-P(M{=}m\mid T{=}0)]\tag{4.52}$$
  (4.51)–(4.52) are the mediation formulas. NDE is a weighted average of CDE; NIE has no such reading (pp. 122–123).
- **Response fractions:** $NDE/TE$ is the fraction transmitted directly with $M$ frozen; $NIE/TE$ the fraction that may be transmitted through $M$ with $Y$ blinded to $X$; $(TE-NDE)/TE$ the fraction necessarily due to $M$ (p. 123).
- **Numerical example** (binary; randomized trial; no mediator–outcome confounding). $T=1$ enhanced training, $Y=1$ passing, $M=1$ more than 3 hours of homework per week. Table 4.6: $E(Y\mid T,M)=0.80$ for (1,1), 0.40 for (1,0), 0.30 for (0,1), 0.20 for (0,0). Table 4.7: $E(M\mid T=0)=0.40$, $E(M\mid T=1)=0.75$ (p. 123). Results (p. 124):
$$NDE=(0.40-0.20)(1-0.40)+(0.80-0.30)\,0.40=0.32$$
$$NIE=(0.75-0.40)(0.30-0.20)=0.035$$
$$TE=0.80\times0.75+0.40\times0.25-(0.30\times0.40+0.20\times0.60)=0.46$$
$$NIE/TE=0.07,\quad NDE/TE=0.696,\quad 1-NDE/TE=0.304$$
  The author concludes that the program raised the success rate by 46%, that 30.4% of this is due to the program stimulating homework, and that only 7% can be explained by stimulated homework alone (p. 124).
- Study questions 4.5.2–4.5.4 are listed under Exercises (pp. 124–125).

*Intuition note.* NDE asks what the treatment does when the mediator is kept at each person's untreated value. NIE asks what happens when only the mediator moves to its treated value. In nonlinear settings the two need not add up to the total effect.

### Ending remarks and bibliographical notes (pp. 125–126)
- **Author's view:** conditions A-1 to A-4 are hard to judge without the graph. With a causal diagram, path-tracing replaces much of the human judgment, and constructing the diagram needs only judgments about causal relations among realizable variables and their disturbances (p. 125).
- **History as told by the author:** (4.5) was introduced by Balke and Pearl (1994a,b). Lewis (1973) defined counterfactuals via similarity among possible worlds. Neyman (1923) devised $Y_x(u)$ for potential response in randomized trials. Rubin (1974) made $Y_x$ a random variable linked to observations by consistency. The author says the three formalisms are logically equivalent (Pearl 2000, ch. 7), and the structural framework derives independence conditions from graphs where potential outcomes state them as "ignorability" assumptions (p. 126).

## Toy example (ours, not from the text)
Model: $X=U_X$, $Y=2X+U_Y$. $U_X\in\{0,1\}$ and $U_Y\in\{0,2\}$ are independent and each uniform (probability ½).

**Deterministic.** Observe $X=1$, $Y=5$ (a unit outside the support above; fine for the three steps). Query: $Y$ had $X$ been 3?
1. Abduction: $U_Y=Y-2X=5-2\cdot1=3$.
2. Action: replace $X=U_X$ by $X=3$.
3. Prediction: $Y_{X=3}=2\cdot3+3=9$.
Consistency check: setting $X=1$ gives $Y_{X=1}=2+3=5=Y$.

**Probabilistic.** Observe only $Y=0$. Then $2X+U_Y=0$ forces $X=0,U_Y=0$ (the other three combinations $(0,2),(1,0),(1,2)$ give $Y=2,2,4$). So $P(U\mid Y=0)$ is a point mass.
- $E[Y_{X=1}\mid Y=0]=2\cdot1+0=2$.
- $E[Y\mid do(X=1)]=2+E[U_Y]=2+\tfrac12(0)+\tfrac12(2)=3$.
The values differ (2 versus 3) because the evidence $Y=0$ tells us this unit has the low value of $U_Y$. This is the abduction step, and do alone ignores it.

## Concepts
- [[counterfactual]] — a statement about what an outcome would be in a unit had a variable taken a value that conflicts with what happened; written $Y_x(u)$ (new) (p. 89, p. 92)
- [[structural-causal-model]] — equations, one per variable, with exogenous $U$; here also the source of counterfactual values (p. 92)
- [[do-operator]] — $do(X=x)$ replaces the equation for $X$; defined on distributions, so population-level only (p. 93)
- [[potential-outcomes]] — $Y_x(u)$ as a unit's response under treatment $x$; the author says it is equivalent to the structural account (p. 125–126)
- [[fundamental-problem-of-causal-inference]] — in a trial only one of $Y_0,Y_1$ is observed per unit (Table 4.4) (p. 105)
- [[surgical-modification-law]] — $Y_x(u)=Y_{M_x}(u)$, Eq. 4.5 (new) (p. 94)
- [[consistency-rule]] — if $X=x$ then $Y_x=Y$; for binary $X$, $Y=XY_1+(1-X)Y_0$ (new) (p. 94)
- [[abduction-action-prediction]] — the three-step procedure for computing counterfactuals (new) (p. 96)
- [[cross-world-probability]] — probability of events about different antecedents, found by summing rows (new) (p. 98)
- [[conditional-ignorability]] — $P(Y_x\mid X,Z)=P(Y_x\mid Z)$ (Eq. 4.15), implied by a back-door set (p. 102–103)
- [[back-door-front-door-criterion]] — graphical conditions that make $Y_x$ independent of $X$ given $Z$ and identify effects (p. 102)
- [[d-separation]] — used to test independence of $Y_x$ from $X$ given $Z$ via the node $U_2$ and collider $Z$ (p. 103)
- [[fork-chain-collider]] — $Z$ as a collider between $X$ and $U_2$ explains the education–salary result (p. 103)
- [[effect-of-treatment-on-the-treated]] — $E[Y_1-Y_0\mid X=1]$; estimated via the modified adjustment formula (new) (p. 106, p. 108)
- [[additive-intervention]] — adding $q$ to each unit's current $X$; $E[Y\mid add(q)]$ (new) (p. 109–110)
- [[probability-of-necessity]] — $PN=P(Y_{x'}=y'\mid x,y)$; "but for" (new) (p. 112, p. 117)
- [[probability-of-sufficiency]] — $PS=P(Y_1=1\mid X=0,Y=0)$ (new) (p. 112)
- [[probability-of-necessity-and-sufficiency]] — $PNS=P(Y_1=1,Y_0=0)$ (new) (p. 113)
- [[monotonicity]] — $Y_1(u)\ge Y_0(u)$ for all $u$; identifies PN and PNS (new) (p. 113, p. 117)
- [[excess-risk-ratio-confounding-factor]] — the two terms of PN in Eq. 4.29 (new) (p. 117)
- [[controlled-direct-effect]] — $E[Y_{1,m}-Y_{0,m}]$, mediator fixed at $m$ for all (new) (p. 121)
- [[natural-direct-effect]] — $E[Y_{1,M_0}-Y_{0,M_0}]$ (new) (p. 121)
- [[natural-indirect-effect]] — $E[Y_{0,M_1}-Y_{0,M_0}]$ (new) (p. 121)
- [[mediation-formula]] — Eqs. 4.51–4.52 for natural effects without confounding (new) (p. 122–123)
- [[confounding-vs-selection-bias]] — here CF corrects confounding bias in PN, and conditioning on a collider opens a path (p. 117, p. 103)

## Canonical instances
- [[freeway-vs-sepulveda]] — a retrospective counterfactual that do cannot express (p. 89)
- [[linear-model-x-equals-au]] — $X=aU$, $Y=bX+U$ with Table 4.1 (p. 92)
- [[joe-encouragement-design]] — Model 4.1; abduction–action–prediction gives 1.90 (pp. 94–96)
- [[college-skill-salary]] — $E[Y_{X=1}\mid Z=1]\ne E[Y\mid do(X=1),Z=1]$ (p. 99)
- [[jobs-training-recruitment]] — ETT and self-selection (p. 107)
- [[insulin-additive-intervention]] — $add(q)$ cannot be written with do (p. 109)
- [[irradiation-jones-smith-daily]] — PN, PS, PNS (pp. 111–113)
- [[mary-discrimination-case]] — discrimination as PS (p. 113)
- [[drug-x-mr-a-legal-attribution]] — PN $=1$ from combined data (pp. 119–120)
- [[homework-mediation-numbers]] — NDE $=0.32$, NIE $=0.035$, TE $=0.46$ (pp. 123–124)

## Bridges (candidates)
- [structural-analogy] Abduction step (update $P(U)$ by evidence) ↔ Bayesian inference: posterior over latent variables given data, then prediction from it. Updating the latent $U$ from evidence and then predicting uses the same logic as posterior-then-predictive, but with an intervention step in between.
- [same-math] $P(U\mid E=e)$ in step (i) ↔ Bayes' theorem: conditioning the distribution of the latent exogenous variables on evidence (p. 97).
- [structural-analogy] Adjustment formula (4.16) and weights $P(z\mid x')$ in (4.21) ↔ marginalization over a confounder with different weights (standardization versus within-group weighting).
- [same-math] Potential outcomes with consistency ↔ potential outcomes framework in canon: $Y_x(u)$ and $Y=XY_1+(1-X)Y_0$.
- [structural-analogy] Table 4.4 randomization (missing entries independent of potential outcomes) ↔ missing-data view of causal inference: unobserved potential outcomes missing at random.

## Questions this raises
- Counterfactual probabilities such as PN depend on the structural model, not only on the distribution of observables. How sensitive are answers to model misspecification beyond monotonicity?
- When bounds on PN (Eq. 4.30) are wide, what extra data or assumptions narrow them most cheaply?
- NDE and NIE need A-1 to A-4. What can be said if the mediator–outcome relation is confounded (Figure 4.6b)? The text only points to later work.
- Are counterfactuals "derived" from structural equations (this chapter) or primitives (as the text says some frameworks treat them)? Does the choice change which problems can be solved?

## Exercises worth doing
- Ex. 4.3.1 (p. 101) — compute $E[Y_x\mid Z=z]$ in the Gaussian education–skill–salary model and show the skill-specific effect is constant — difficulty: hard
- Ex. 4.3.2 (p. 107) — (a) estimate $a,b,c$ from observational data; (b) effect of education for people with $Y=1$ via Theorem 4.3.2; (c) $\tau$ and ETT with an interaction term — difficulty: medium
- Ex. 4.4.1 (p. 109) — show ETT is estimable from observational plus experimental data when $X$ is binary, then apply to the Simpson's story data — difficulty: medium
- Ex. 4.4.2 (p. 111) — formulate Joe's smoking decision as ETT and estimate it from given data — difficulty: easy
- Ex. 4.5.1 (p. 120) — update Ms Jones's PN estimate with the bounds of Eq. 4.30 and an observational study — difficulty: medium
- Ex. 4.5.2 (p. 124) — find TE, NDE, NIE in a linear model, with and without correlated errors — difficulty: medium

## Reading notes
- Printed page numbers are visible in the page labels; printed = pdf − 20.
- **Evidence mismatch:** Section 4.2.3 gives Joe's evidence as $Y=1.5$ (also computing $U_Y=0.75$ with 1.5); Section 4.3.4 (p. 106) writes $e=\{X=0.5,H=1,Y=1\}$. The earlier value (1.5) fits the computation.
- **Variable names:** p. 104 writes $Y_{X=0.5,Z=2.0}$ for a quantity computed for Joe from Figure 4.2; Figure 4.2 intervenes on $H$ (setting it to 2), so $Z$ looks like a slip for $H$.
- **Equation reference:** p. 116 refers to Eqs. (4.21) and (4.8) for the estimands of ETT and additive interventions; the additive result is (4.22), and (4.8) is an inequality.
- **Section reference:** p. 114 says the discrimination result will be shown "in 4.5.2"; the attribution tools (PN, PS) are in 4.5.1, and 4.5.2 covers mediation.
- **Company name:** the example uses "XYZ International"; Study question 4.5.4 says "ABC International".
- **NIE conventions:** the NIE in 4.4.5 (hold $X=1$, vary $Q$ from the distribution under $X=0$ to that under $X=1$ with sign reversed) uses a different reference point from NIE in Eq. 4.47 (hold $T=0$, move $M$ from its $T=0$ to $T=1$ distribution). Do not equate the two formulas term by term.
- **Rounding:** $NIE/TE=0.035/0.46\approx0.076$; the text prints 0.07. Also $NDE+NIE=0.355\neq TE=0.46$, as expected in a nonlinear case (see 4.48).
- **Phrasing:** p. 124 says the program increased the success rate by 46%; TE is $0.46$ in probability units (percentage points).
- Eq. (4.31)'s upper bound has no explicit cap at 1; the min in (4.30) caps it. Text-layer equations were checked against the page images; no unreadable passages.
