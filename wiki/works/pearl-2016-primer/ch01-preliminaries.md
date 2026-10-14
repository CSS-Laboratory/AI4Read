---
id: pearl-2016-primer/ch01-preliminaries
work: pearl-2016-primer
unit: "1 Preliminaries: Statistical and Causal Models"
pages: xvii–34 (chapter text pp. 1–33)
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
# Preliminaries: Statistical and Causal Models

## L0 — One line
The same numbers can demand opposite readings depending on the causal story that generated them, so statistics needs a formal language for causal assumptions: structural causal models and their graphs.

## L1 — The gist (≤ 120 words)
Why can't ordinary statistics tell us whether a drug helps? The unit shows, through Simpson's paradox, that identical tables can need opposite readings (aggregate data, pooled over everyone, versus segregated data, split by a third variable) depending on the causal story behind them, and that this story cannot be read from the data or written in contingency tables. It then reviews the probability, regression and graph tools needed and introduces structural causal models, whose acyclic graphs let a joint distribution be written as a product of child-given-parents terms. This sets up the book's plan: state causal assumptions formally, link them to data, then draw causal conclusions.

**Prerequisites:** basic fractions and percentages; summation notation $\sum$; reading a scatter plot; a little calculus (area under a curve) is helpful.

## L2 — Key ideas
- Simpson's paradox: an association in a whole population can reverse in every subpopulation, and the data alone do not say which version to trust (pp. 1–2).
- Identical numbers (gender drug example vs. blood-pressure example) need different readings: segregated data in one, aggregate data in the other. The reason is the causal story, e.g. a common cause (a variable that causes both treatment and outcome) versus a mediator (a variable on the path from treatment to outcome) (pp. 3–4).
- Causal assumptions cannot be represented in contingency tables (tables of counts) or tested in the data alone. Extra-statistical tools are needed (p. 5).
- The probability toolkit includes conditioning as filtering, independence, the law of total probability, Bayes' rule, expectation, variance and covariance, and regression. Bayes' rule needs a prior (a probability distribution over the hypotheses before the evidence), which is controversial when it is a subjective belief (pp. 8–24).
- The Monty Hall problem shows that beliefs should depend on the process that generated the evidence, not only on the facts observed (pp. 14–15).
- Regression of $Y$ on $X$ differs from regression of $X$ on $Y$. Partial regression coefficients (slopes with a third variable held constant) can have the opposite sign to the simple slope, which is Simpson's paradox in regression form (pp. 22–23).
- A structural causal model (SCM) has exogenous variables $U$ (external to the model, left unexplained), endogenous variables $V$ (determined inside the model) and functions $f$. $X$ is a direct cause of $Y$ if $X$ appears in $Y$'s function. Each SCM has a graph (pp. 26–27).
- For an acyclic graph (no directed cycles), the joint distribution is the product of $P(\text{child}\mid\text{parents})$. This cuts table size and improves estimation (pp. 29–31).

## L3 — Walkthrough

### 1.1 Why study causation (p. 1)
- We study causation to make sense of data, guide actions and policies, and learn from successes and failures. Examples are smoking and lung cancer, education and salaries, and carbon emissions and climate. We also want to know *how and why* causes act, e.g. whether malaria comes from mosquitoes or "mal-air" (p. 1).
- Author's claim: causation is not merely an aspect of statistics but an enrichment of it. None of the problems above can be articulated in the standard language of statistics (p. 1).

### 1.2 Simpson's paradox (pp. 1–7)
- **Definition.** Data in which a statistical association holding in an entire population is reversed in every subpopulation. Reversals may continue as more attributes are considered (pp. 1–2).
- **Example 1.2.1** (Table 1.1, 700 patients, 350 chose the drug, 350 did not) (p. 2):

| | Drug | No drug |
|---|---|---|
| Men | 81/87 (93%) | 234/270 (87%) |
| Women | 192/263 (73%) | 55/80 (69%) |
| Combined | 273/350 (78%) | 289/350 (83%) |

  The drug looks better in each gender but worse overall (p. 2). The author calls the apparent conclusion (prescribe the drug if the gender is known, but not if it is unknown) ridiculous (p. 2).
- **Causal story (hypothetical extra facts).**
  - Suppose estrogen lowers recovery regardless of the drug, and women are much more likely to take the drug. Then drug takers are more often women and so less likely to recover (p. 3).
  - Being a woman is a *common cause* of drug taking and of failure to recover. Given this story, to assess the drug we must compare subjects of the same gender, so we use the segregated data and conclude the drug helps (p. 3).
- **Continuous version** (Figs 1.1, 1.2, p. 3–4). Within each age group, more exercise goes with lower cholesterol. Pooled, more exercise goes with higher cholesterol. If older people exercise more and have higher cholesterol regardless, age is a common cause of exercise (treatment) and cholesterol (outcome). So use the age-segregated data (p. 3).
- **Segregation is not always right.** Table 1.2 has the same numbers as Table 1.1 with the column labels switched. The strata are now posttreatment blood pressure (BP):

| | No drug | Drug |
|---|---|---|
| Low BP | 81/87 (93%) | 234/270 (87%) |
| High BP | 192/263 (73%) | 55/80 (69%) |
| Combined | 273/350 (78%) | 289/350 (83%) |

  - Here the drug acts partly by lowering BP and also has a toxic effect. Since BP is one mechanism through which treatment affects recovery, separating by BP "makes no sense". Use the aggregate data and recommend the drug (p. 4).
  - The author notes that if BP had been measured *before* treatment and BP affected treatment, it would be a different story (p. 4).
  - Result: same numbers, but the correct answer is in the segregated data for gender and in the aggregate data for BP (p. 4).
- **Lesson (p. 5).**
  - Nothing that decided the case (timing, treatment affecting BP, BP affecting recovery) was in the data. Correlation is not causation, and no statistical method can determine the causal story from the data alone (p. 5).
  - The paradox in the gender case comes from our strong conviction that treatment cannot affect sex. That assumption cannot be tested in the data or represented in standard statistics. No causal information can be represented in contingency tables (p. 5).
  - The book will offer extra-statistical methods: a "calculus of causation" to express causal assumptions and answer such questions (p. 5).
- **Four needs** (p. 5):
  1. a working definition of causation;
  2. a way to formalise causal assumptions (causal models);
  3. a way to link model structure to data features;
  4. a way to draw conclusions from model plus data.
- **Working definition:** "A variable X is a cause of a variable Y if Y in any way relies on X for its value" (p. 5). Metaphor: $Y$ "listens to" $X$ and sets its value in response. This is refined in §1.5.1 (p. 26).
- Readers who know probability, statistics and graph theory may skip to §1.5 (p. 6).
- **Study questions 1.2.1–1.2.4** (pp. 6–7): faulty causal claims; a baseball batting-average reversal; aggregate versus segregated data for kidney stones and two surgeons; a lollipop story with a Simpson reversal in a randomized experiment.

> **Intuition note.** A table shows only who recovered, not why. In these two examples, whether to split the data depends on whether the splitting variable causes both treatment and outcome (split) or sits on the path from treatment to outcome (don't split). The author says no statistical method can read the causal story from the data alone, so the story has to come from outside the data.

### 1.3 Probability and Statistics (pp. 7–24)
Probability is the language for the uncertainty in most causal statements (e.g. careless driving causes accidents but need not produce one) (p. 7).

**1.3.1 Variables (pp. 7–8).**
- A variable is a property that can take multiple values, like a question whose answer is the value. $P(X=x)$ is often shortened to $P(x)$. $P(X=38)$ means the probability that a randomly selected individual is aged 38 (p. 7).
- Discrete variables take finitely or countably many values. Continuous variables take values on a continuous scale (p. 8).

**1.3.2 Events (p. 8).** An event is any assignment of a value or set of values to variables, e.g. "$X=1$ or $Y=3$". Any declarative statement is an event. This differs from the everyday sense, which requires some change (p. 8). Study question 1.3.1: find variables and events in the lollipop story.

**1.3.3 Conditional probability (pp. 8–9).**
- $P(X=x\mid Y=y)$ is the probability of $X=x$ given that we know $Y=y$ (p. 8). Conditioning can be seen as *filtering* a data set.
- Voter example (Table 1.3, thousands: 18–29: 20,539; 30–44: 30,756; 45–64: 52,013; 65+: 29,641; total 132,948):
  $P(\text{Age}<45)=\frac{20{,}539+30{,}756}{132{,}948}=\frac{51{,}295}{132{,}948}$, which the author gives as $0.38$ (p. 8).
- Filtering to ages over 29 (Table 1.4, total 112,409): $P(\text{Age}<45\mid \text{Age}>29)=\frac{30{,}756}{112{,}409}=0.27$ (p. 9).
- Conditional probabilities play an important role in causal questions, because we often want to compare how the probability (risk) of an outcome changes under different filtering, or exposure, conditions (p. 9). Study question 1.3.2 (Table 1.5) asks for simple probabilities from a gender × education table (pp. 9–10).

**1.3.4 Independence (pp. 10–11).**
- Events $A$, $B$ are independent if
  $$P(A\mid B)=P(A) \tag{1.1}$$
  Dependence and independence are symmetric: if $P(A|B)=P(A)$ then $P(B|A)=P(B)$ (p. 10).
- $A$, $B$ are conditionally independent given $C$ if
  $$P(A\mid B,C)=P(A\mid C) \tag{1.2}$$
  and $P(B|A,C)=P(B|C)$. Example: "smoke detector on" depends on "fire nearby" but may become independent given "smoke nearby" (p. 10). In data, this means independence in the table filtered on $C$. Independence in the unfiltered data is called marginal independence (p. 10).
- Variables $X$, $Y$ are independent if for every $x,y$
  $$P(X=x\mid Y=y)=P(X=x) \tag{1.3}$$
  Otherwise they are dependent (pp. 10–11).

**1.3.5 Probability distributions (p. 11).**
- A distribution assigns a probability to each value. Probabilities lie between 0 and 1 and sum to 1 (p. 11).
- A continuous variable has a density $f$. $P(a<X<b)=\int_a^b f(x)\,dx$ and $\int_{-\infty}^{\infty} f(x)\,dx=1$ (p. 11).
- A joint distribution gives probabilities for each combination of values of a set of variables. Example: $P(X{=}1,Y{=}1)=0.2$, $P(1,2)=0.1$, $P(2,1)=0.5$, $P(2,2)=0.2$ (p. 11).

**1.3.6 Law of total probability (pp. 11–13).**
- For mutually exclusive $A$, $B$:
  $$P(A \text{ or } B)=P(A)+P(B) \tag{1.4}$$
- For any $A$, $B$:
  $$P(A)=P(A,B)+P(A,\text{“not }B\text{”}) \tag{1.5}$$
- For a *partition* $B_1,\dots,B_n$ (exhaustive, mutually exclusive; exactly one is true):
  $$P(A)=P(A,B_1)+P(A,B_2)+\cdots+P(A,B_n) \tag{1.6}$$
  Summing like this is *marginalizing over* $B$, and $P(A)$ is the marginal probability (pp. 11–12).
- Multiplication rule:
  $$P(A,B)=P(A\mid B)P(B) \tag{1.7}$$
  The division rule $P(A|B)=P(A,B)/P(B)$ is formally a definition. It is justified by filtering: the filtered rows summed to $P(B)$, so each is multiplied by $1/P(B)$ to sum to 1 (p. 12).
- Independence means $P(A,B)=P(A)P(B)$ (p. 12).
- Using (1.7) and $P(A,B)=P(B,A)$ gives **Bayes' rule**:
  $$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)} \tag{1.8}$$
- Total probability as a weighted sum ("conditionalizing on $B$"):
  $$P(A)=P(A\mid B_1)P(B_1)+\cdots+P(A\mid B_k)P(B_k) \tag{1.9}$$
  It is useful because conditional probabilities tied to a context are often easier to assess than $P(A)$ itself (p. 12).
- *Gadget example:* factory A makes 30% (1 in 5000 defective), factory B makes 70% (1 in 10,000 defective).
  $P(\text{defective})=\frac{0.30}{5000}+\frac{0.70}{10{,}000}=\frac{1.30}{10{,}000}=0.00013$ (pp. 12–13).
- *Two dice:* $P(\text{Roll 2}>\text{Roll 1})=\sum_{i=1}^{6}P(\text{Roll 2}>i)\cdot\frac16=\left(\frac56+\frac46+\frac36+\frac26+\frac16+\frac06\right)\frac16=\frac5{12}$ (p. 13).

**1.3.7 Using Bayes' rule (pp. 13–15).**
- Loosely, $A$ is the "hypothesis" and $B$ the "evidence". We often know $P(B|A)$ easily but want $P(A|B)$. To use the rule this way, we treat each hypothesis as an event and assign a probability distribution over all the hypotheses of the situation, called a *prior* (p. 13).
- *Casino example:* a dealer shouts "11". In the story, the only two games at the casino that would occasion an 11 are craps and roulette, and there are exactly as many craps games as roulette games, so $P(\text{craps})=\tfrac12$.
  - $P(\text{“11”}|\text{craps})=\frac{2}{36}=\frac1{18}$ and $P(\text{“11”}|\text{roulette})=\frac1{38}$.
  - $P(\text{“11”})=\frac12\cdot\frac1{18}+\frac12\cdot\frac1{38}=\frac7{171}$.
  - $P(\text{craps}\mid\text{“11”})=\frac{(1/18)(1/2)}{7/171}=0.679$ (pp. 13–14).
- *Monty Hall:* three doors, one car. You pick $A$. Monty, who may not reveal the car, opens $C$ (a goat). Switch to $B$ or stay with $A$?
  - **Common first reaction:** the car's location is independent of your first choice, so $A$ and $B$ are equally likely (p. 14).
  - **Author's answer:** switching to $B$ wins twice as often as staying. The reasoning often given for this is: your first pick had probability $\tfrac13$. Monty always opens a goat door whether you chose the car or not, so you learned nothing new about $A$. It keeps $\tfrac13$, and the remaining $\tfrac23$ sits on $B$ (p. 14).
  - Formal statement: variables $X$ (door chosen), $Y$ (car door), $Z$ (door opened). One must show $P(Y=B|X=A,Z=C)>P(Y=A|X=A,Z=C)$. The proof is left to the reader (Study question 1.3.5) (p. 14).
  - A 100-door version (Monty opens 98 goat doors) makes switching obvious (p. 14).
  - *Why $C$ opening is evidence:* Monty could not open $A$ but could have opened $B$. His not doing so makes it more likely that he opened $C$ because he was forced, which supports $B$. General theme: a hypothesis that has withstood a test of refutation becomes more likely (p. 15).
  - The explanation uses counterfactual wording ("could have opened"). The author says what makes the Monty Hall example unique among probability puzzles is its critical dependence on the data-generating process: our beliefs should depend not merely on the facts observed but also on the process that led to them. The fact that the car is not behind Door $C$ does not by itself describe the problem; we must also know what options the host had. Chapter 4 will give a theory of counterfactuals for this (p. 15).
- *Controversy:* often $P(A)$ cannot be computed from frequencies, and one substitutes a *subjective belief*. The author raises questions rather than answers them: how do we know the assigned $P(A)$ summarises our information? Should we reduce all arguments to one number? Why update subjective beliefs like frequencies? Some experiments suggest people do not update by Bayes' rule, but many believe they should. The author says the debate continues, yet Bayes' rule is a powerful tool used throughout the book (p. 15).
- Study questions 1.3.3–1.3.5 (pp. 15–16): casino variants (the source text says "Section 1.3.6" but the example is in §1.3.7); the three-cards problem; the Monty Hall proof.

> **Intuition note.** Bayes' rule turns a question that is often easy to answer (how likely is this evidence if the hypothesis is true?) into the one we usually want (how likely is the hypothesis given this evidence?), but only if you supply a prior. In Monty Hall, the host's *rules* decide what his action tells you.

**1.3.8 Expected values (pp. 16–17).**
$$E(X)=\sum_x x\,P(X=x) \tag{1.10}$$
$$E[g(X)]=\sum_x g(x)P(x) \tag{1.11}$$
$$E(Y\mid X=x)=\sum_y y\,P(Y=y\mid X=x) \tag{1.13}$$
- Die: $E(X)=3.5$. With prize $g(X)=X^2$: $E[g(X)]=\frac{1+4+9+16+25+36}{6}=15.17$ (1.12) (pp. 16–17).
- "Best guess" result: $g=E(X)$ minimizes the expected squared error $E(g-X)^2$. Likewise $g=E(Y|X=x)$ minimizes $E[(g-Y)^2|X=x]$ (p. 17).
- Voter ages (using midpoints 23.5, 37, 54.5, 70 and proportions 0.16, 0.23, 0.39, 0.22; assuming ages uniform within groups and a maximum age of 75):
  $E(\text{Age})=48.9$.
  $$E[\text{Age}\mid \text{Age}<45]=23.5\times0.40+37\times0.60=31.6 \tag{1.14}$$
- Expectation as a best guess presumes roughly symmetric distributions. For highly skewed ones the median may be better (it minimizes $E(|g-X|)$) (p. 17).

**1.3.9 Variance and covariance (pp. 17–20).**
$$\mathrm{Var}(X)=E\big((X-\mu)^2\big) \tag{1.15}$$
- The standard deviation $\sigma_X=\sqrt{\mathrm{Var}(X)}$ has the same units as $X$ (p. 18).
- Under-45 voters (source arithmetic): $(23.5-31.5)^2(0.41)+(37-31.5)^2(0.59)=26.24+17.85$, which the source states as $43.09\ \text{years}^2$. This gives $\sigma_X=6.56$ years (p. 18). (The sum 26.24 + 17.85 is 44.09; see Reading notes.)
- For a normal variable, about two-thirds of values lie within one standard deviation of the mean and about 95% within two (p. 18).
- Covariance:
  $$\sigma_{XY}\triangleq E[(X-E(X))(Y-E(Y))] \tag{1.16}$$
  It measures how far $X$ and $Y$ *linearly* covary.
- Correlation coefficient:
  $$\rho_{XY}=\frac{\sigma_{XY}}{\sigma_X\sigma_Y} \tag{1.17}$$
  It is dimensionless, between $-1$ and $1$, and represents the slope of the best-fit line after normalizing both variables by their standard deviations (p. 18).
- Author's statements: $\rho_{XY}$ is one iff one variable predicts the other linearly, and zero whenever linear prediction is no better than a random guess. Both $\sigma_{XY}$ and $\rho_{XY}$ vanish when $X$, $Y$ are independent. Nonlinear relationships need the full $P(Y=y|X=x)$ (p. 18).
- Study questions 1.3.6–1.3.8 (pp. 19–20): prove covariance vanishes under independence; two-coin payoffs; craps measures with Table 1.6 (12 rolls of two dice).

**1.3.10 Regression (pp. 20–22).**
- The best prediction of $Y$ from $X$ (in mean squared error) is $E[Y|X=x]$ if the joint distribution is known. *Regression* instead predicts directly from data with a (usually linear) formula (p. 20).
- The least squares line $y=\alpha+\beta x$ minimizes
  $$\sum_i (y_i-y_i')^2=\sum_i (y_i-\alpha-\beta x_i)^2 \tag{1.18}$$
  The sample line (from the 12 craps rolls, Fig. 1.4, dashed) differs from the population line (sample size to infinity, solid) through sampling variation (pp. 20–21).
- *Dice:* the population line for the sum $Y$ on Die 1 ($X$) is
  $$y=3.5+1.0x \tag{1.19}$$
  because $E[Y|X=x]=E[\text{Die 2}+X\mid X=x]=E[\text{Die 2}]+x=3.5+1.0x$ (p. 21).
- *Reverse regression:* with $Y=X+Z$,
  $$E[X\mid Y=y]=E[Y-Z\mid Y=y]=1.0y-E[Z\mid Y=y] \tag{1.20}$$
  The added term depends on $y$, so the slope is below 1. By symmetry $E[X|Y=y]=E[Z|Y=y]$, so $E[X|Y=y]=0.5y$. (Added step: substituting gives $E[X|Y=y]=y-E[X|Y=y]$, so $2E[X|Y=y]=y$.) Each die contributes equally on average; if $Y=10$, best estimates are $X=5$, $Z=5$ (p. 22).
- For $y=a+bx$ (1.21), with $b$ denoted $R_{YX}$:
  $$b=R_{YX}=\frac{\sigma_{XY}}{\sigma_X^2} \tag{1.22}$$
  So generally $R_{YX}\neq R_{XY}$; the author says they are equal only when $\mathrm{Var}(X)=\mathrm{Var}(Y)$ (see Reading notes). Positive slope means positive correlation, negative slope means negative correlation, zero means no *linear* correlation. Correlated variables are dependent (p. 22).

> **Intuition note.** The slope of $Y$ on $X$ is the covariance divided by the variance of the *predictor*, so swapping the roles of $X$ and $Y$ changes the slope. With dice, the sum rises one-for-one with Die 1, but Die 1 rises only half a unit per unit of the sum.

**1.3.11 Multiple regression (pp. 22–24).**
- Regressing $Y$ on $\{X,Z\}$ gives the plane
  $$y=r_0+r_1x+r_2z \tag{1.23}$$
  Slices along $Z$ give slope $r_1$; slices along $X$ give $r_2$ (p. 23).
- The slope of $Y$ on $X$ holding $Z$ constant is the *partial regression coefficient* $R_{YX\cdot Z}$. $R_{YX}$ can be positive while $R_{YX\cdot Z}$ is negative (as in Fig. 1.1). This is Simpson's paradox: overall positive association that becomes negative when conditioning on a third variable (p. 23).
- **Orthogonality principle.** If
  $$Y=r_0+r_1X_1+\cdots+r_kX_k+\epsilon \tag{1.24}$$
  then, regardless of the underlying distribution, the best least-squares coefficients are obtained when $\epsilon$ is uncorrelated with each regressor: $\mathrm{Cov}(\epsilon,X_i)=0$, $i=1,\dots,k$ (p. 23).
- *Use:* best estimate of $X=\text{Die 1}$ given $Y=\text{Die 1}+\text{Die 2}$. Write
  $$X=\alpha+\beta Y+\epsilon \tag{1.25a}$$
  Taking expectations, with $E[\epsilon]=0$ without loss of generality:
  $$E[X]=\alpha+\beta E[Y] \tag{1.25b}$$
  Multiplying (1.25a) by $Y$ and taking expectations:
  $$E[XY]=\alpha E[Y]+\beta E[Y^2]+E[Y\epsilon] \tag{1.26}$$
  The principle gives $E[Y\epsilon]=0$. Two equations in two unknowns yield
  $\alpha=E(X)-E(Y)\frac{\sigma_{XY}}{\sigma_Y^2}$ and $\beta=\frac{\sigma_{XY}}{\sigma_Y^2}$ (p. 23).
  (Added step, checking $\beta$: since $E[XY]=\sigma_{XY}+E[X]E[Y]$ and $E[Y^2]=\sigma_Y^2+E[Y]^2$, subtracting $E[Y]\times$(1.25b) from (1.26) gives $\sigma_{XY}=\beta\sigma_Y^2$.) This is a general method for slopes in two or more dimensions (p. 23).
- For $Z=\alpha+\beta_YY+\beta_XX+\epsilon$ one multiplies by $Y$ and $X$ as well, imposes $E[\epsilon Y]=E[\epsilon X]=0$, and solves three equations (p. 24):
  $$\beta_Y=R_{ZY\cdot X}=\frac{\sigma_X^2\sigma_{ZY}-\sigma_{ZX}\sigma_{XY}}{\sigma_Y^2\sigma_X^2-\sigma_{YX}^2} \tag{1.27}$$
  $$\beta_X=R_{ZX\cdot Y}=\frac{\sigma_Y^2\sigma_{ZX}-\sigma_{ZY}\sigma_{YX}}{\sigma_Y^2\sigma_X^2-\sigma_{YX}^2} \tag{1.28}$$
- In practice slopes come from least-squares software. An exception is predicting *before data* whether a slope is zero, which Section 3.8 says is handled efficiently with causal graphs (p. 24). Study question 1.3.9: prove (1.22) via orthogonality; compute the partial coefficients for craps (p. 24).

### 1.4 Graphs (pp. 24–26)
- Graph theory is introduced as the mathematical language in which the causal story behind the data can be conveyed (p. 24).
- A graph is a collection of nodes (vertices) and edges. Two nodes are *adjacent* if an edge joins them. A *complete* graph has an edge between every pair. A *path* is a sequence of nodes, each joined to the next by an edge (Fig. 1.5) (p. 25).
- Edges may be directed (arrowhead) or undirected. A directed graph has only directed edges (Fig. 1.6: $X\to Y\to Z$). The tail node is the *parent* and the head node the *child* (p. 25).
- A path is *directed* if it can be traced along the arrows (no node on the path has two path-edges into it or two out of it). If a directed path joins two nodes, the first is an *ancestor* and the later nodes are *descendants* (p. 25).
- A directed path from a node to itself makes the graph *cyclic*. A directed graph without cycles is *acyclic* (Fig. 1.7(a) acyclic, 1.7(b) cyclic) (p. 25).
- Study question 1.4.1 (Fig. 1.8) asks for parents, ancestors, children, descendants and paths (p. 26).

### 1.5 Structural Causal Models (pp. 26–31)

**1.5.1 Modeling causal assumptions (pp. 26–28).**
- An SCM describes how nature assigns values to variables. It consists of two sets of variables $U$ and $V$ and a set of functions $f$, one assigning each variable in $V$ a value from other variables (p. 26).
- **Expanded definition of causation:** $X$ is a *direct cause* of $Y$ if $X$ appears in the function that assigns $Y$'s value. $X$ is a *cause* of $Y$ if it is a direct cause of $Y$ or of any cause of $Y$ (p. 26).
- $U$ are *exogenous* (external; we choose not to explain their causes). $V$ are *endogenous*. Every endogenous variable descends from at least one exogenous variable. Exogenous variables have no ancestors and are root nodes. If all exogenous values are known, the functions fix every endogenous value with certainty (p. 27).
- *Asthma example:* treatment $X$ and lung function $Y$ are endogenous. Air pollution $Z$ is treated as exogenous because we assume it is an external factor that cannot be caused by treatment or lung function (p. 27).
- **Graphical model.** One node per variable. A directed edge $Y\to X$ exists if $f_X$ contains $Y$. The book deals mainly with DAGs. Graphical definition: a child's parent is a *direct cause*. A descendant's ancestor is a *potential cause* (rare intransitive cases, to be discussed in Part Two) (p. 27).
- **SCM 1.5.1** (Salary): $U=\{X,Y\}$, $V=\{Z\}$, $F=\{f_Z\}$, $f_Z: Z=2X+3Y$. $X$ is years of schooling, $Y$ is years in the profession and $Z$ is salary. $X$ and $Y$ are direct causes of $Z$ (Fig. 1.9) (p. 27).
- The graph shows that $X$, $Y$ cause $Z$ but not *how* (the function) (p. 28).
- Why use graphs? Our causal knowledge is usually qualitative, not quantitative. Example of a partial SCM, **SCM 1.5.2**: $V=\{\text{Height, Sex, Performance}\}$, $U=\{U_1,U_2,U_3\}$; Sex $=U_1$; Height $=f_1(\text{Sex},U_2)$; Performance $=f_2(\text{Height},\text{Sex},U_3)$. The $U$'s are unmeasured "error terms" or "omitted factors" (p. 28). The author says graphs convey the same information more quickly (p. 28).
- Study question 1.5.1 (SCM 1.5.3: $X=U_X$, $Y=X/3+U_Y$, $Z=Y/16+U_Z$) asks for graphs and best guesses (pp. 28–29).

**1.5.2 Product decomposition (pp. 29–31).**
- A joint table over 10 binary variables needs 1024 rows. A fully specified SCM is more compact but is not always available (p. 29).
- **Rule of product decomposition.** For any model whose graph is acyclic,
  $$P(x_1,x_2,\dots,x_n)=\prod_i P(x_i\mid pa_i) \tag{1.29}$$
  where $pa_i$ are the values of $X_i$'s parents. The author says this follows from certain independencies that always hold among the variables, to be discussed in the next chapter (p. 29).
- Chain $X\to Y\to Z$: $P(x,y,z)=P(x)P(y|x)P(z|y)$ (p. 29). We need only three small tables, and estimation counts frequencies of $x$, $(y|x)$, $(z|y)$, trading a "high-dimensional" estimation problem for several low-dimensional ones. Without knowledge of the graph, estimation becomes impossible for many variables and moderate data (the "curse of dimensionality") (p. 30).
- *Weather chain* $X\to Y\to Z\to W$ (clouds, rain, wet pavement, slippery pavement). Judging $P(\text{clouds, no rain, dry pavement, slippery pavement})$ directly is hard. With the rule, the author's rough guesses are $0.5\times0.75\times0.9\times0.05=0.0169$ (p. 30).
- *Estimation example:* a joint table for four binary variables has $16-1=15$ free cells. With 45 observations, about three per cell, and some empty. With the decomposition, samples are pooled into 2 cells for $P(x)$ and 4 cells each for $P(y|x)$, $P(z|y)$, $P(w|z)$. This gives more accurate frequencies (pp. 30–31).
- Study questions 1.5.2–1.5.4 (pp. 31–32): syndrome–drug model and a Simpson reversal; a binary chain; the structural model of Monty Hall.

> **Intuition note.** Each variable depends directly only on its parents, so you only need to learn one small "recipe" per variable. These small tables multiply to the big joint table, which makes estimation from limited data easier and more accurate.

### Bibliographical notes (pp. 32–33)
The notes point to Pearl (2009, 2014b) for the history of Simpson's paradox, and to Lindley (2014) and Pearl (1988) for the Bayesian approach to probability. Monty Hall is said to be mathematically equivalent to the "Three Prisoners Dilemma". The product rule became the semantic basis of Bayesian networks (DAGs for probabilistic knowledge, not necessarily causal), and its validity for SCMs was shown in Pearl and Verma (1991) (pp. 32–33).

## Toy example (ours, not from the text)
Eighty patients, with severity measured *before* treatment (severity $Z$ causes both treatment choice and recovery):

| | Drug | No drug |
|---|---|---|
| Severe | 12/30 recovered (40%) | 3/10 (30%) |
| Mild | 9/10 (90%) | 24/30 (80%) |
| Combined | 21/40 (52.5%) | 27/40 (67.5%) |

- Within each stratum the drug is better ($40>30$, $90>80$). Pooled, it is worse ($52.5<67.5$).
- Why: the pooled rate is a weighted average of the stratum rates (law of total probability, 1.9), and the weights differ.
  - Drug: $0.4\times\frac{30}{40}+0.9\times\frac{10}{40}=0.30+0.225=0.525$.
  - No drug: $0.3\times\frac{10}{40}+0.8\times\frac{30}{40}=0.075+0.60=0.675$.
  - Severe patients, who recover less, dominate the drug group (75%) but only 25% of the no-drug group.
- Since severity precedes treatment and affects both, the causal story of §1.2 says to use the *stratified* data and conclude the drug helps. If $Z$ were instead a posttreatment mediator, the pooled rows would be the ones to use. The numbers could be identical, and only the story differs.
- Product decomposition check for the graph $Z\to X\to Y$ with $Z\to Y$ (as in Fig. 1.10): $P(Z{=}\text{severe})=\frac{40}{80}=0.5$; $P(\text{drug}\mid\text{severe})=\frac{30}{40}=0.75$; $P(\text{recover}\mid\text{drug, severe})=\frac{12}{30}=0.4$. Product: $0.5\times0.75\times0.4=0.15$, which equals the direct count $\frac{12}{80}=0.15$.

## Concepts
- [[simpsons-paradox]] — an association in a whole population reverses in every subpopulation; which version is right depends on the causal story (p. 1)
- [[confounding-vs-selection-bias]] — here only the common-cause case appears: a variable (gender, age) causing both treatment and outcome, so compare within levels (p. 3)
- [[causation-definition-listening]] (new) — $X$ causes $Y$ if $Y$ relies on $X$ for its value; formally, $X$ appears in $Y$'s function (pp. 5, 26)
- [[conditional-probability]] (new) — $P(A|B)$ = probability of $A$ after filtering the data to cases where $B$ holds (p. 8)
- [[independence-conditional-independence]] (new) — $P(A|B)=P(A)$; conditional version $P(A|B,C)=P(A|C)$ (p. 10)
- [[law-of-total-probability]] (new) — $P(A)=\sum_i P(A|B_i)P(B_i)$ over a partition; "conditionalizing on $B$" (p. 12)
- [[bayes-theorem]] — $P(A|B)=P(B|A)P(A)/P(B)$, from (1.7) and symmetry of $P(A,B)$ (p. 12)
- [[prior-distribution]] — probability distribution assigned to hypotheses before the evidence (p. 13)
- [[subjective-probability]] — a prior that is a personal belief, not computable from frequencies; controversial (p. 15)
- [[expected-value-best-guess]] (new) — $E(X)=\sum x P(x)$; the squared-error-minimizing guess (pp. 16–17)
- [[variance-covariance-correlation]] (new) — spread, linear co-variation and its normalized form $\rho_{XY}$ (p. 18)
- [[linear-regression-slope]] (new) — least squares line; slope $R_{YX}=\sigma_{XY}/\sigma_X^2$, not symmetric in $X,Y$ (pp. 20–22)
- [[partial-regression-coefficient]] (new) — slope of $Y$ on $X$ holding $Z$ constant, $R_{YX\cdot Z}$; may differ in sign from $R_{YX}$ (p. 23)
- [[orthogonality-principle]] (new) — best least-squares coefficients make the error uncorrelated with the regressors (p. 23)
- [[causal-dag]] — directed acyclic graph with nodes as variables and an edge from each variable in a function to the variable it determines (pp. 25, 27)
- [[structural-causal-model]] — exogenous $U$, endogenous $V$, functions $f$ assigning each $V$ from other variables (p. 26)
- [[exogenous-endogenous-variables]] (new) — exogenous: unexplained root variables; endogenous: determined inside the model (p. 27)
- [[product-decomposition]] (new) — for acyclic graphs $P(x_1,\dots,x_n)=\prod_i P(x_i|pa_i)$ (p. 29)
- [[curse-of-dimensionality]] (new) — estimating a high-dimensional joint distribution without structural knowledge is impossible with moderate data (p. 30)

## Canonical instances
- [[simpson-gender-drug-table]] — Table 1.1: drug better in each gender, worse overall; gender is a common cause (p. 2)
- [[simpson-bp-drug-table]] — Table 1.2: same numbers; BP is a mediator, so use pooled data (p. 4)
- [[simpson-exercise-cholesterol]] — continuous reversal with age as common cause (pp. 3–4)
- [[monty-hall]] — switching wins with probability $\tfrac23$; evidence depends on the host's options (p. 14)
- [[casino-craps-roulette-11]] — Bayes' rule, $P(\text{craps}|\text{“11”})=0.679$ (p. 14)
- [[two-dice-regression]] — slope 1.0 for sum on Die 1, but 0.5 for Die 1 on sum (pp. 21–22)
- [[salary-scm]] — SCM 1.5.1, $Z=2X+3Y$ (p. 27)
- [[weather-chain-product-rule]] — clouds→rain→wet→slippery, product rule estimate 0.0169 (p. 30)

## Bridges (candidates)
- [same-math] Bayes' rule with prior ↔ Bayesian inference: posterior ∝ likelihood × prior — same formula (1.8), with the hypothesis as $A$ and the evidence as $B$.
- [same-math] Law of total probability (1.9) ↔ marginal likelihood: averaging a conditional probability over a distribution of the conditioning variable.
- [same-math] Product decomposition (1.29) ↔ Bayesian network factorization: the book itself says it became the semantic basis of Bayesian networks (p. 33).
- [structural-analogy] Slope $E[X|Y=y]=0.5y$ below 1 (§1.3.10) ↔ shrinkage/partial pooling: the prediction is pulled toward the mean because the predictor is noisy as a signal of $X$.
- [structural-analogy] Monty Hall: evidence depends on how it was generated ↔ likelihoods depend on the data-collection or selection process (e.g. a posterior predictive model of the sampling).
- [metaphor] "$Y$ listens to $X$" ↔ conditional dependence in a generative model: parents determine children's distributions.

## Questions this raises
- If no statistical method can recover the causal story from data alone, how much can data *test* about a causal model, and how do we link graph structure to testable dependencies (the author promises "universally true independencies" in the next chapter)?
- When the prior is subjective, how sensitive are conclusions drawn with Bayes' rule, and how should one report them?
- The Monty Hall answer rests on counterfactual terms ("he could have opened B"). How will Chapter 4 formalise them?
- Regression gives $R_{YX}\ne R_{XY}$ and $R_{YX\cdot Z}$ may differ in sign from $R_{YX}$. Which regressors should be chosen for a given purpose? The author says Section 3.8 handles the task of predicting which slopes are zero, using causal graphs.

## Exercises worth doing
- Ex. 1.2.2 (p. 6) — build a Simpson reversal from batting averages in a table — difficulty: easy
- Ex. 1.2.3 (p. 6) — decide aggregate vs segregated data from the causal story (kidney stones, surgeons) — difficulty: medium
- Ex. 1.3.4 (p. 16) — three-card problem; intuition versus Bayes' theorem — difficulty: medium
- Ex. 1.3.5 (p. 16) — prove the Monty Hall result with Bayes' theorem — difficulty: medium
- Ex. 1.3.9 (p. 24) — derive (1.22) via orthogonality; partial coefficients for craps — difficulty: hard
- Ex. 1.5.2 (p. 31) — joint distributions from the product rule; find parameters giving Simpson's reversal — difficulty: hard
- Ex. 1.5.4 (p. 32) — write the structural model of Monty Hall — difficulty: hard

## Reading notes
- Source pages: pdf 17–54 = printed xvii–34 (chapter text starts on printed p. 1 = pdf 21; offset for body pages: printed = pdf − 20). pdf 17 is the companion-website page (website URL only). pdf 19–20 are the book's contents pages; the label for pdf 20 says xx, but the page image shows the header "viii". The contents also list Chapters 2–4, which were not part of this unit. pdf 18 and 54 are blank; p. 33 holds the end of the bibliographical notes.
- Misprints and arithmetic slips visible in the page images:
  - p. 8: the first fraction uses denominator 132,448,000, while the others use 132,948,000 (the table total). Also $51{,}295/132{,}948\approx0.386$, whereas the text gives 0.38.
  - p. 17: proportions 0.16/0.23/0.39/0.22 are rounded from the table (the first is closer to 0.155).
  - p. 18: variance example: $26.24+17.85$ is $44.09$, not $43.09$. The mean 31.5 and weights 0.41/0.59 also differ from the 31.6, 0.40/0.60 of Eq. (1.14).
  - p. 18: the statement that $\rho_{XY}$ is one if and only if one variable predicts the other linearly. Since $\rho$ ranges from $-1$ to $1$, this presumably refers to perfect (positive) linear prediction.
  - p. 22: "covariate $\sigma_{XY}$" should read covariance.
  - p. 22: the parenthetical says $R_{YX}=R_{XY}$ only when the variances are equal. From (1.22) and its mirror image $\sigma_{XY}/\sigma_Y^2$ (the text says $\beta$ follows by reversing $X$ and $Y$), the two slopes are also equal when $\sigma_{XY}=0$ (both zero).
  - p. 15: Study question 1.3.3 refers to "Section 1.3.6", but the casino problem is in §1.3.7.
  - p. 2: "than do men are not taking the drug" (garbled wording).
- Study questions are printed without solutions. Equations were checked against the page images; the text layer renders some Greek letters as garbled symbols, but all were readable in the images.
