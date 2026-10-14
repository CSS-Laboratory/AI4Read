---
id: kahneman-1979-prospect/main
work: kahneman-1979-prospect
unit: paper
pages: 263-291
fields: [decision-game-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Prospect Theory: An Analysis of Decision under Risk (Kahneman & Tversky, 1979)

## L0 — One line
People evaluate gains and losses relative to a reference point, using an S-shaped value function and decision weights that replace probabilities, and the authors propose this to account for systematic violations of expected utility theory.

## L1 — The gist (≤ 120 words)
Expected utility theory was the standard model of choice under risk. The paper asks whether people's choices actually obey it. Using questionnaire problems, the authors show systematic violations: sure outcomes are overweighted (certainty effect), shared components are ignored (isolation effect), and risk attitudes flip between gains and losses (reflection effect). They propose prospect theory: choices are edited, then evaluated with a value function on gains and losses (usually concave for gains, often convex for losses, steeper for losses) and decision weights that replace probabilities. It accounts for Allais-type patterns (a sure gain is chosen, but the choice reverses when both options' chances are scaled down), insurance and gambling, and reference-point shifts.

**Prerequisites:** expected utility; concave and convex functions; basic inequalities and ratios; the idea of a preference relation (indifference vs. strict preference).

## L2 — Key ideas (5–10 bullets)
- **Expected utility fails descriptively.** Majorities choose in ways that no single utility function can produce, e.g. in Allais-type pairs (Problems 1–4) (pp. 265–266).
- **Certainty effect and reflection effect.** Certain outcomes are overweighted relative to merely probable ones. This favors risk aversion for gains and risk seeking for losses; preferences between negative prospects mirror those between positive ones (pp. 268–269).
- **Isolation effect and framing.** People drop components shared by all options. Equivalent problems framed differently (two-stage game; bonus problems) get different choices, which suggests that value attaches to changes rather than to final wealth (pp. 271–273).
- **Two phases.** Editing (coding, combination, segregation, cancellation, simplification, dominance detection) precedes evaluation. Editing can make preferences depend on context (pp. 274–275).
- **Value function.** $V=\pi(p)v(x)+\pi(q)v(y)$ for regular prospects (those with a chance of nothing, or with outcomes of opposite sign), with a different rule (eq. 2) for strictly positive or negative ones (all outcomes positive, or all negative). $v$ is defined on gains and losses, usually concave for gains, often convex for losses, steeper for losses (pp. 276–279).
- **Weighting function.** $\pi$ is not a probability. The authors hypothesize that it overweights low $p$, is subadditive for small $p$ ($\pi(rp)>r\pi(p)$) and subproportional (for a fixed ratio of probabilities, the ratio of weights is closer to 1 when probabilities are low), and say the evidence suggests subcertainty, $\pi(p)+\pi(1-p)<1$. It is not well-behaved near 0 and 1 (pp. 280–283).
- **Risk attitudes depend on $v$ and $\pi$ jointly.** The theory implies Allais-type violations when the $v$-ratio of the two outcomes is bounded by the matching $\pi$-ratios, a preference for regular over probabilistic insurance (provided the probability of loss is overweighted), and both gambling and insurance for small probabilities (pp. 284–286).
- **Reference point matters.** Not having adapted to a loss increases risk seeking in some situations. Final-asset framing essentially eliminates risk seeking, except for gambling with low probabilities. The authors suggest that paying for a gamble is not equivalent to accepting it (pp. 286–288).
- **Axiomatics sketched.** In the authors' sketch, additive conjoint measurement (representing a preference order by a sum of two scales) plus a distributivity axiom yields the bilinear form (a sum of $\pi\cdot v$ terms) (pp. 289–290).

## L3 — Walkthrough

### Abstract and 1. Introduction (p. 263)
- The paper criticises expected utility theory as a *descriptive* model of choice under risk and proposes prospect theory (p. 263).
- The abstract states that decision weights are generally lower than the corresponding probabilities, except in the range of low probabilities, and that overweighting of low probabilities may contribute to the attractiveness of both insurance and gambling (p. 263).
- Expected utility is widely accepted as a normative model. The common assumption is that reasonable people would want to obey its axioms and that most people mostly do (p. 263).
- The authors claim preferences systematically violate the axioms in several classes of problems (p. 263).

### 2. Critique (pp. 263–273)

**Setup and the three tenets (pp. 263–264).**
- A *prospect* $(x_1,p_1;\dots;x_n,p_n)$ is a contract paying $x_i$ with probability $p_i$, $\sum p_i=1$. $(x,p)$ means $(x,p;0,1-p)$. $(x)$ is a sure outcome. Only objective ("standard") probabilities are considered (p. 263).
- (i) Expectation: $U(x_1,p_1;\dots;x_n,p_n)=p_1u(x_1)+\dots+p_nu(x_n)$ (p. 263).
- (ii) Asset integration: a prospect is acceptable at asset position $w$ iff $U(w+x_1,p_1;\dots;w+x_n,p_n)>u(w)$. The domain of $u$ is final states, not gains and losses (p. 264).
- (iii) Risk aversion: $u$ is concave ($u''<0$). A person is risk averse if he prefers the sure prospect $(x)$ to any risky prospect with expected value $x$. In the theory, risk aversion is equivalent to concavity (p. 264).

**Method (pp. 264–265).**
- Students and faculty answered hypothetical, anonymous questionnaire problems (≤ 12 per booklet, orders varied, left–right positions reversed). Outcomes are in Israeli pounds; median family income is about 3,000 per month (p. 264).
- Some of the problems were also given to groups at Stockholm and Michigan, with essentially identical results (pp. 264–265).
- Justification: field studies cannot measure probabilities and utilities well. Laboratory studies use contrived small-stakes gambles with many repetitions. If people predict their own choices reasonably well, common and systematic violations in hypothetical problems are presumptive evidence against the theory (p. 265).

**Certainty, probability, possibility (pp. 265–267).** The certainty effect is that outcomes considered certain are overweighted relative to merely probable ones (p. 265).

| Problem | Choice (% choosing) | N |
|---|---|---|
| 1 | A: (2,500,.33; 2,400,.66; 0,.01) [18] vs B: (2,400) [82]* | 72 |
| 2 | C: (2,500,.33) [83]* vs D: (2,400,.34) [17] | 72 |
| 3 | A: (4,000,.80) [20] vs B: (3,000) [80]* | 95 |
| 4 | C: (4,000,.20) [65]* vs D: (3,000,.25) [35] | 95 |
| 5 | A: 50% chance of a three-week tour of England, France, Italy [22] vs B: a one-week tour of England for sure [78]* | 72 |
| 6 | C: 5% chance of the three-week tour [67]* vs D: 10% chance of the one-week tour [33] | 72 |
| 7 | A: (6,000,.45) [14] vs B: (3,000,.90) [86]* | 66 |
| 8 | C: (6,000,.001) [73]* vs D: (3,000,.002) [27] | 66 |

(pp. 265–267; * = significant at .01)

- In Problems 1–2, 61% made the modal choice in both. With $u(0)=0$, the Problem 1 preference implies $u(2{,}400)>.33u(2{,}500)+.66u(2{,}400)$, i.e. $.34u(2{,}400)>.33u(2{,}500)$. The Problem 2 preference implies the reverse inequality (p. 266).
- Problem 2 is Problem 1 with a .66 chance of 2,400 removed from both prospects. The removal hurts more when it turns a sure gain into a probable one than when both prospects are already uncertain (p. 266).
- Problems 3–4: choosing B implies $u(3{,}000)/u(4{,}000)>4/5$; choosing C implies the reverse. $C=(A,.25)$ and $D=(B,.25)$. The substitution axiom says that if $B$ is preferred to $A$, then $(B,p)$ must be preferred to $(A,p)$. Subjects did not obey it. Over half the respondents violated expected utility in every problem pair of this section (p. 266).
- Problems 7–8 show a different violation: with substantial probabilities people pick the more probable win; with minuscule probabilities (winning possible, not probable) they pick the larger prize (p. 267).
- Empirical generalisation: if $(y,pq)$ is equivalent to $(x,p)$, then $(y,pqr)$ is preferred to $(x,pr)$, $0<p,q,r<1$. This is built into the theory (p. 267).

> **Intuition note.** Cutting a probability from 1.0 to .25 seems to cost more than cutting it from .8 to .2, although the ratio is the same. Expected utility cannot allow this, because it treats equal ratios of probability alike.

**The reflection effect (pp. 268–269).** Table I reverses the signs of outcomes (p. 268):

| Positive | % | Negative | % |
|---|---|---|---|
| 3: (4,000,.80) < (3,000) | 20 / 80* | 3′: (−4,000,.80) > (−3,000) | 92* / 8 |
| 4: (4,000,.20) > (3,000,.25) | 65* / 35 | 4′: (−4,000,.20) < (−3,000,.25) | 42 / 58 |
| 7: (3,000,.90) > (6,000,.45) | 86* / 14 | 7′: (−3,000,.90) < (−6,000,.45) | 8 / 92* |
| 8: (3,000,.002) < (6,000,.001) | 27 / 73* | 8′: (−3,000,.002) > (−6,000,.001) | 70* / 30 |

- Reflecting prospects around 0 reverses the preference order: the *reflection effect* (p. 268).
- Consequences the authors draw (pp. 268–269):
  1. Risk aversion for gains goes with risk seeking for losses. In 3′ most chose a .80 risk of losing 4,000 over a sure loss of 3,000, despite lower expected value. Williams's subjects were indifferent between (100,.65; −100,.35) and (0), but also between (−200,.80) and (−100).
  2. Preferences between negative prospects violate the expectation principle in the same way. The same principle, overweighting of certainty, favors risk aversion for gains and risk seeking for losses.
  3. **Variance-aversion account (Allais, Markowitz, Tobin):** people prefer high expected value and small variance. This could explain the choice of (3,000) in Problem 3. But (−3,000) has both higher expected value and lower variance than (−4,000,.80), so this account predicts the sure loss would be chosen, contrary to the data. The authors conclude that the data are incompatible with the notion that certainty is generally desirable; it appears that certainty "increases the aversiveness of losses as well as the desirability of gains" (p. 269).

> **Intuition note.** The same pull toward the sure thing makes people take sure gains and avoid sure losses. A taste for low variance cannot do both.

**Probabilistic insurance (pp. 269–271).**
- Insurance purchase is often read as evidence that utility is concave. But people often prefer limited coverage with low or zero deductible over higher coverage with higher deductible, contrary to risk aversion (p. 269).
- Problem 9 (95 Stanford students): you are indifferent between insuring and not insuring. Probabilistic insurance costs half the premium. If damage occurs, with 50% you pay the other half and are fully covered, and with 50% your payment is refunded and you bear the loss. 20% would buy it, 80% would not (pp. 269–270).
- Many protective actions (burglar alarm, new tires, stopping smoking) are probabilistic insurance (p. 270). The authors say that, apparently, reducing the probability of loss from $p$ to $p/2$ is less valuable than reducing it from $p/2$ to 0 (p. 270).
- **Expected utility with concave $u$ predicts probabilistic insurance is superior to regular insurance.** If one is indifferent between $(w-x,p;w,1-p)$ and $(w-y)$, one should prefer $(w-x,(1-r)p;w-y,rp;w-ry,1-p)$ to $(w-y)$, $0<r<1$ (p. 270).
- Proof: $pu(w-x)+(1-p)u(w)=u(w-y)$ must imply $(1-r)pu(w-x)+rpu(w-y)+(1-p)u(w-ry)>u(w-y)$. Set $u(w-x)=0$, $u(w)=1$, so $u(w-y)=1-p$. Then one must show
$$rp(1-p)+(1-p)u(w-ry)>1-p \quad\text{or}\quad u(w-ry)>1-rp,$$
which the authors say holds if and only if $u$ is concave (p. 270).
- (added step) Concavity gives it: $w-ry=(1-r)w+r(w-y)$, so $u(w-ry)\ge(1-r)\cdot1+r(1-p)=1-rp$, strictly for strictly concave $u$.
- The result is puzzling because probabilistic insurance looks riskier than regular insurance. So concavity of $u$ does not capture intuitive risk (p. 270).
- Authors' conjecture: *contingent insurance* (certain coverage for one specified risk) will generally be more attractive than probabilistic insurance when the probabilities of unprotected loss are equated. Equivalent prospects can then differ in value by formulation (pp. 270–271).

**The isolation effect (pp. 271–273).** People simplify choice by disregarding shared components and focusing on distinguishing ones. A pair of prospects can be decomposed in more than one way, and different decompositions can give different preferences (p. 271).
- **Problem 10 (N=141):** a two-stage game. Stage 1: .75 chance the game ends with nothing, .25 chance of stage 2. At stage 2 the choice is (4,000,.80) vs (3,000), made before the game starts. In final outcomes this is $(4{,}000,.25\times.80=.20)$ vs $(3{,}000,.25\times1.0=.25)$, as in Problem 4. Yet 78% chose the latter, contrary to the modal preference in Problem 4. Subjects ignored stage 1 and treated it as Problem 3 (p. 271).
- Figures 1 and 2 are decision trees (squares = decision nodes, circles = chance nodes). The difference is the location of the decision node and a dependency between events: "not winning 3,000" is included in "not winning 4,000" in the sequential form, but the two events are independent in the standard form. So 3,000 gets a certainty advantage in the sequential form (pp. 271–272).
- This reversal violates the supposition that choices depend only on probabilities of final states. An example: a venture with a choice of a fixed return or a share of earnings if it succeeds is most likely seen in sequential form. The isolation effect implies, per the authors, that the contingent certainty of the fixed return enhances that option's attractiveness (p. 272).
- **Problems 11–12 (varying outcome representation):** Problem 11 (N=70): given 1,000 extra, choose A (1,000,.50) [16] or B (500) [84]*. Problem 12 (N=68): given 2,000 extra, choose C (−1,000,.50) [69]* or D (−500) [31]. In final states $A=(2{,}000,.50;1{,}000,.50)=C$ and $B=(1{,}500)=D$. Problem 12 is Problem 11 with 1,000 added to the bonus and subtracted from all outcomes (p. 273).
- The majority chose B, then C: subjects did not integrate the bonus, which was common to both options. In expected utility the utility of a wealth of $100,000 does not depend on whether it was reached from 95,000 or 105,000 (p. 273).
- Conclusion: the carriers of value are changes of wealth, not final asset positions. This is the cornerstone of the alternative theory (p. 273).

> **Intuition note.** What you currently own is common to all your options, so people tend to cancel it and look only at the changes. Moving the starting point then moves choices, even though final wealth is the same.

### 3. Theory (pp. 274–284)

**Overview and editing (pp. 274–275).** Prospect theory is developed for simple monetary prospects with stated probabilities. It has two phases: *editing* (a preliminary analysis that simplifies the prospects) and *evaluation* (the edited prospect of highest value is chosen) (p. 274). Editing operations (pp. 274–275):
- **Coding:** outcomes are perceived as gains and losses relative to a reference point, usually the current asset position. The reference point can shift with formulation and with the decision maker's expectations (p. 274).
- **Combination:** probabilities of identical outcomes are merged, e.g. $(200,.25;200,.25)\to(200,.50)$ (p. 274).
- **Segregation:** a riskless component is separated. $(300,.80;200,.20)$ becomes a sure 200 plus $(100,.80)$. $(-400,.40;-100,.60)$ becomes a sure loss of 100 plus $(-300,.40)$ (p. 274).
- **Cancellation** (applied to a set of prospects): shared components are discarded. This includes the first stage of Problem 10, the bonus in Problems 11–12, and common outcome–probability pairs. Example: $(200,.20;100,.50;-50,.30)$ vs $(200,.20;150,.50;-100,.30)$ reduces to $(100,.50;-50,.30)$ vs $(150,.50;-100,.30)$ (pp. 274–275).
- **Simplification** (rounding, e.g. $(101,.49)\to$ an even chance of 100; discarding extremely unlikely outcomes) and **detection of dominance** (dominated options rejected without evaluation) (p. 275).
- Editing is assumed to be done whenever possible. The order of operations can matter: $(500,.20;101,.49)$ appears to dominate $(500,.15;99,.51)$ if the second constituents are both simplified to $(100,.50)$. The paper treats only cases where the edited form is unambiguous (p. 275).
- Some anomalies come from editing: isolation effects from cancellation, and some intransitivities from simplification that removes small differences. Preference order need not be invariant across contexts (p. 275).

**Evaluation: definitions (pp. 275–276).**
- Overall value $V$ is expressed through two scales. $\pi(p)$ is a *decision weight* reflecting the impact of $p$ on the prospect's value; $\pi$ is not a probability measure, and $\pi(p)+\pi(1-p)$ is typically less than 1. $v(x)$ is the subjective value of outcome $x$, measured from the reference point (zero) (p. 275).
- A simple prospect $(x,p;y,q)$ has at most two non-zero outcomes. It is *strictly positive* if $x,y>0$ and $p+q=1$, *strictly negative* if all its outcomes are negative, and *regular* otherwise (pp. 275–276).
- **Eq. (1).** If $(x,p;y,q)$ is regular (either $p+q<1$, or $x\ge0\ge y$, or $x\le0\le y$), then
$$V(x,p;y,q)=\pi(p)v(x)+\pi(q)v(y)\tag{1}$$
with $v(0)=0$, $\pi(0)=0$, $\pi(1)=1$. $V$ is defined on prospects and $v$ on outcomes; they coincide for sure prospects: $V(x,1.0)=V(x)=v(x)$ (p. 276).
- Eq. (1) generalises expected utility by relaxing the expectation principle. The Appendix sketches conditions ensuring a unique $\pi$ and a ratio-scale $v$ (p. 276).
- **Eq. (2).** Strictly positive and negative prospects are segregated into a riskless component (the minimum certain gain or loss) and a risky component. If $p+q=1$ and either $x>y>0$ or $x<y<0$, then
$$V(x,p;y,q)=v(y)+\pi(p)[v(x)-v(y)]\tag{2}$$
Example: $V(400,.25;100,.75)=v(100)+\pi(.25)[v(400)-v(100)]$. The weight applies to the risky part only (p. 276).
- The right side of (2) equals $\pi(p)v(x)+[1-\pi(p)]v(y)$, so (2) reduces to (1) if $\pi(p)+\pi(1-p)=1$. The authors say this is not generally satisfied (p. 276).
- Related work noted by the authors: Markowitz (utility on gains and losses, but expectation principle retained), Edwards (weights replacing probabilities), Fellner and van Dam (p. 276–277).
- The theory keeps a bilinear form but assumes values attach to changes and weights differ from probabilities. The authors state that these departures must lead to normatively unacceptable consequences (inconsistency, intransitivity, dominance violations). Decision makers usually correct them when they notice, but often have no chance to notice, and then the anomalies are expected to occur (p. 277).

**The value function (pp. 277–280).**
- Perception responds to changes relative to an adaptation level (brightness, loudness, temperature, and also health, prestige, wealth) (p. 277).
- Strictly, value is a function of two arguments (the asset position and the change): a "book" with one page per asset position. The pages are likely to become more linear as assets rise. Since preference order is not greatly altered by small or moderate variations in asset position (the certainty equivalent of $(1{,}000,.50)$ lies between 300 and 400 for most people over a wide range), one argument is a satisfactory approximation (pp. 277–278).
- Many sensory dimensions show a concave response to physical change (e.g. a 3° vs 6° room-temperature change is easier to tell apart than 13° vs 16°). The authors propose that this applies to money: the difference between gains of 100 and 200 appears greater than between 1,100 and 1,200, and likewise for losses (unless the larger loss is intolerable). Hypothesis: $v''(x)<0$ for $x>0$ and often $v''(x)>0$ for $x<0$ (p. 278).
- **Problems 13, 13′:** $(6{,}000,.25)$ vs $(4{,}000,.25;2{,}000,.25)$: 18% / 82%* (N=68). Negated: $(-6{,}000,.25)$ vs $(-4{,}000,.25;-2{,}000,.25)$: 70%* / 30% (N=64). By (1), the modal choices give $\pi(.25)v(6{,}000)<\pi(.25)[v(4{,}000)+v(2{,}000)]$ and $\pi(.25)v(-6{,}000)>\pi(.25)[v(-4{,}000)+v(-2{,}000)]$. Hence $v(6{,}000)<v(4{,}000)+v(2{,}000)$ and $v(-6{,}000)>v(-4{,}000)+v(-2{,}000)$, in accord with concavity for gains and convexity for losses (p. 278).
- Special circumstances (e.g. needing $60,000 for a house) can create convex regions for gains and concave regions for losses. The latter may be more common since large losses often force changes of life style (pp. 278–279).
- **Loss aversion.** "Losses loom larger than gains." Most people find symmetric bets $(x,.50;-x,.50)$ distinctly unattractive, and the aversiveness generally grows with the stake: if $x>y\ge0$, then $(y,.50;-y,.50)$ is preferred to $(x,.50;-x,.50)$. By (1) (the common factor $\pi(.50)$ cancels, added step) (p. 279):
$$v(y)+v(-y)>v(x)+v(-x)\quad\text{and}\quad v(-y)-v(-x)>v(x)-v(y).$$
Setting $y=0$ gives $v(x)<-v(-x)$. Letting $y$ approach $x$ gives $v'(x)<v'(-x)$, provided $v'$ exists. So the value function for losses is steeper than for gains (p. 279).
- Summary: $v$ is (i) defined on deviations from the reference point, (ii) generally concave for gains and commonly convex for losses, (iii) steeper for losses. Figure 3 shows an S-shaped curve, steepest at the reference point, unlike Markowitz's function, which is shallow there (p. 279).
- Decision weights can produce risk aversion and risk seeking even with a linear $v$, so scaling $v$ is harder than in utility theory (p. 280).
- Support: Fishburn and Kochenberger analysed von Neumann–Morgenstern utility functions of 30 decision makers (five studies). Most were concave for gains and convex for losses; only three were risk averse for both; with one exception, utility was steeper for losses (p. 280).

> **Intuition note.** The first 100 gained or lost matter more than 100 added far from the reference point (the authors compare 100→200 with 1,100→1,200), and a loss hurts more than an equal gain pleases. This gives an S-shaped curve that is steepest at the reference point and steeper for losses.

**The weighting function (pp. 280–284).**
- Decision weights are inferred from choices (as in the Ramsey–Savage approach to subjective probability) but do not obey the probability axioms and are not degrees of belief. For a fair coin toss for 1,000, the probability is .50 by any reasonable test, but $\pi(.50)$ is likely smaller than .50. The two scales coincide ($\pi(p)=p$) if the expectation principle holds, but not otherwise (p. 280).
- Here $\pi$ is a function of the *stated* probability; elsewhere weights could depend on other factors such as ambiguity. $\pi$ is increasing, $\pi(0)=0$, $\pi(1)=1$ (p. 280).
- **Subadditivity for small $p$:** $\pi(rp)>r\pi(p)$ for $0<r<1$. From Problem 8, $\pi(.001)v(6{,}000)>\pi(.002)v(3{,}000)$, so
$$\frac{\pi(.001)}{\pi(.002)}>\frac{v(3{,}000)}{v(6{,}000)}>\frac12\quad\text{by the concavity of }v.$$
Problem 8′ gives the same conclusion. Problems 7 and 7′ suggest subadditivity need not hold for large $p$ (pp. 280–281).
- **Overweighting of low probabilities:** $\pi(p)>p$ for small $p$. Problem 14 (N=72): $(5{,}000,.001)$ [72]* vs $(5)$ [28]. Problem 14′: $(-5{,}000,.001)$ [17] vs $(-5)$ [83]*. Preferring the lottery implies $\pi(.001)v(5{,}000)>v(5)$, hence $\pi(.001)>v(5)/v(5{,}000)>.001$, assuming $v$ concave for gains. Paying the "premium" in 14′ gives the same conclusion, assuming $v$ convex for losses (p. 281).
- Overweighting (a property of decision weights) differs from overestimation of rare events, which does not arise here because subjects adopt the stated $p$. In real life both may operate (p. 281).
- **Subcertainty:** for all $0<p<1$, $\pi(p)+\pi(1-p)<1$ (the authors say evidence suggests this). From Problems 1 and 2 via (1):
$$v(2{,}400)>\pi(.66)v(2{,}400)+\pi(.33)v(2{,}500),\ \text{i.e. } [1-\pi(.66)]v(2{,}400)>\pi(.33)v(2{,}500),$$
$$\pi(.33)v(2{,}500)>\pi(.34)v(2{,}400);\ \text{hence } 1-\pi(.66)>\pi(.34),\ \text{or } \pi(.66)+\pi(.34)<1.$$
Allais's original example gives $\pi(.89)+\pi(.11)<1$; MacCrimmon and Larsson data imply it for other $p$ (pp. 281–282).
- Subcertainty means $\pi$ is *regressive*: preferences are less sensitive to probability changes than the expectation principle requires. Weights of complementary events sum to less than the weight of the certain event (p. 282).
- **Subproportionality.** The violation rule is: if $(x,p)$ is equivalent to $(y,pq)$, then $(x,pr)$ is not preferred to $(y,pqr)$ (printed range $0<p,q,r\le1$). By (1), $\pi(p)v(x)=\pi(pq)v(y)$ implies $\pi(pr)v(x)\le\pi(pqr)v(y)$, hence
$$\frac{\pi(pq)}{\pi(p)}\le\frac{\pi(pqr)}{\pi(pr)}.$$
For a fixed probability ratio, the ratio of weights is closer to unity when probabilities are low. This holds if and only if $\log\pi$ is a convex function of $\log p$ (p. 282).
- Subproportionality plus overweighting of small probabilities implies subadditivity there: if $\pi(p)>p$ and subproportionality holds, then $\pi(rp)>r\pi(p)$, $0<r<1$, provided $\pi$ is monotone and continuous on $(0,1)$ (p. 282).
- Figure 4: a hypothetical $\pi$ with overweighting and subadditivity at small $p$, subcertainty and subproportionality. It is relatively shallow in the interior and changes abruptly near 0 and 1. The authors offer two readings of this: a limit on how small a weight can be, and a "quantum of doubt" capping weights below 1, perhaps reflecting the certainty/uncertainty distinction. Editing may also lead people to discard very unlikely events or treat very likely ones as certain. So $\pi$ is not well-behaved near the endpoints (pp. 282–283).
- **Zeckhauser's Russian roulette:** most people would pay much more to remove the one bullet (1/6 → 0) than to cut four to three (4/6 → 3/6). Economic considerations would favour paying more in the latter case, because money is worth less when one may not live to enjoy it (p. 283).
- **Objection 1:** the prospects $(x,p;x,q)$ and $(x,p';x,q')$ with $p+q=p'+q'<1$ are surely indifferent, which would imply $\pi(p)+\pi(q)=\pi(p')+\pi(q')$ and hence $\pi$ linear. **Reply:** invalid in this theory, since probabilities of identical outcomes are combined in editing (p. 283).
- **Objection 2 (dominance):** let $x>y>0$, $p>p'$, $p+q=p'+q'<1$, so $(x,p;y,q)$ dominates $(x,p';y,q')$. If preference obeys dominance, then $\pi(p)v(x)+\pi(q)v(y)>\pi(p')v(x)+\pi(q')v(y)$, or
$$\frac{\pi(p)-\pi(p')}{\pi(q')-\pi(q)}>\frac{v(y)}{v(x)}.$$
As $y\to x$, $\pi(p)-\pi(p')$ approaches $\pi(q')-\pi(q)$. Since $p-p'=q'-q$, $\pi$ must be essentially linear or dominance must be violated (pp. 283–284).
- **Reply:** direct violations are prevented by detecting and removing dominated options before evaluation. Indirect violations are permitted, e.g. $A\succ B$, $B\succ C$, and $C$ dominates $A$ (Raiffa's example) (p. 284).
- Bids vs. choices: Lichtenstein and Slovic found pairs with $A$ preferred to $B$ in choice but $B$ bid higher. Confirmed in several studies. So it cannot generally be assumed that preference is recoverable from bids; the authors base $v$ and $\pi$ on choices between specified prospects, which makes measurement harder (p. 284).

> **Intuition note.** The weight $\pi(p)$ measures the impact of $p$ on a prospect's desirability, not just how likely people think the event is. In the authors' hypothetical curve it is inflated for tiny $p$, fairly flat in the middle, and changes abruptly near 0 and 1. Because $\pi(p)+\pi(1-p)<1$, a sure outcome gets relatively more weight than a merely probable one, which is how Allais-type choices follow.

### 4. Discussion (pp. 284–289)

**Risk attitudes (pp. 284–286).**
- The Allais pattern (Problems 1–2) follows from the theory iff
$$\frac{\pi(.33)}{\pi(.34)}>\frac{v(2{,}400)}{v(2{,}500)}>\frac{\pi(.33)}{1-\pi(.66)}.$$
The violation of independence is attributed to subcertainty, i.e. $\pi(.34)<1-\pi(.66)$. An Allais-type violation occurs whenever the $v$-ratio of the two non-zero outcomes is bounded by the corresponding $\pi$-ratios (pp. 284–285).
- Problems 3–8 share this structure. For Problems 7–8 the observed choices follow iff
$$\frac{\pi(.001)}{\pi(.002)}>\frac{v(3{,}000)}{v(6{,}000)}>\frac{\pi(.45)}{\pi(.90)}.$$
Here the violation of substitution is attributed to subproportionality of $\pi$. The same analysis applies to other violations of substitution, in positive and negative domains (p. 285).
- **Probabilistic insurance under prospect theory** (provided the probability of loss is overweighted). Claim: if $(-x,p)$ is indifferent to $(-y)$, then $(-y)$ is preferred to $(-x,p/2;-y,p/2;-y/2,1-p)$. Define $f(x)=-v(-x)$ for $x\ge0$. Since $v$ is convex for losses, $f$ is concave. Using the natural extension of eq. (2), show that $\pi(p)f(x)=f(y)$ implies
$$f(y)\le f(y/2)+\pi(p/2)[f(y)-f(y/2)]+\pi(p/2)[f(x)-f(y/2)]=\pi(p/2)f(x)+\pi(p/2)f(y)+[1-2\pi(p/2)]f(y/2).$$
Substitute $f(x)=f(y)/\pi(p)$ and use concavity of $f$ (added step: with $f(0)=0$, concavity gives $f(y/2)\ge f(y)/2$). It suffices to show
$$f(y)\le\frac{\pi(p/2)}{\pi(p)}f(y)+\pi(p/2)f(y)+f(y)/2-\pi(p/2)f(y),$$
i.e. $\pi(p)/2\le\pi(p/2)$, which follows from the subadditivity of $\pi$ (p. 285).
- Attitudes to risk are determined jointly by $v$ and $\pi$. For the gamble $(x,p)$ with $x>0$ versus its expected value $(px)$: risk seeking is implied whenever $\pi(p)>v(px)/v(x)$, which exceeds $p$ if $v$ is concave for gains. So overweighting is necessary but not sufficient for risk seeking for gains. The same condition is necessary but not sufficient for risk aversion when $x<0$. Hence risk seeking for gains and risk aversion for losses are restricted to small probabilities, where overweighting is expected (p. 285).
- Those are the typical conditions under which lottery tickets and insurance are sold. Overweighting of small probabilities favours both gambling and insurance; the S-shaped value function tends to inhibit both (p. 286).
- Caveats: the authors say the analysis falls short of a full account. Insurance is often bought in the medium range of probabilities, small disaster probabilities are sometimes ignored, and minor formulation changes affect insurance attractiveness. A full theory should include the value of security, social norms of prudence, and other factors (p. 286).

**Shifts of reference (pp. 286–288).**
- The reference point is usually the status quo, but gains and losses may be coded against an expectation or aspiration level (an unexpected tax withdrawal is felt as a loss; a firm doing better than rivals may see a small loss as a gain) (p. 286).
- Incomplete adaptation to recent losses: a person who has lost 2,000 and chooses between a sure gain of 1,000 and an even chance of 2,000 or nothing may code it as $(-2{,}000,.50)$ vs $(-1{,}000)$ instead of $(2{,}000,.50)$ vs $(1{,}000)$. The former induces more adventurous choices (p. 286).
- **Proposition:** if the risky prospect $(x,p;-y,1-p)$ is just acceptable, then $(x-z,p;-y-z,1-p)$ is preferred to $(-z)$ for $x,y,z>0$ with $x>z$ (a negative translation increases risk seeking in some situations) (p. 287).
- Proof (p. 287): $V(x,p;-y,1-p)=0$ iff $\pi(p)v(x)=-\pi(1-p)v(-y)$. Then
$$\begin{aligned}V(x-z,p;-y-z,1-p)&=\pi(p)v(x-z)+\pi(1-p)v(-y-z)\\&>\pi(p)v(x)-\pi(p)v(z)+\pi(1-p)v(-y)+\pi(1-p)v(-z)\quad\text{(properties of }v)\\&=-\pi(1-p)v(-y)-\pi(p)v(z)+\pi(1-p)v(-y)+\pi(1-p)v(-z)\quad\text{(substitution)}\\&=-\pi(p)v(z)+\pi(1-p)v(-z)\\&>v(-z)[\pi(p)+\pi(1-p)]\quad\text{since }v(-z)<-v(z)\\&>v(-z)\quad\text{by subcertainty.}\end{aligned}$$
- The authors cite the betting-day observation (long-shot betting rises during the day) as some support. Similarly, someone who expects to buy insurance may code paying premium $y$ against loss $x$ as $(-x+y,p;y,1-p)$ vs $(0)$ instead of $(-x,p)$ vs $(-y)$; insurance is more attractive in the former coding (p. 287).
- Formulating the problem in final assets sets the reference point at zero on the wealth scale; $v$ is then likely concave everywhere. This essentially eliminates risk seeking except for gambling with low probabilities, and is perhaps the most effective way to eliminate risk seeking for losses (p. 287).
- **Buying a gamble.** Standard theories treat paying 10 for $(1{,}000,.01)$ as accepting $(990,.01;-10,.99)$. The authors suggest people evaluate the gamble and its cost separately and buy if the combined value is positive, e.g. $\pi(.01)v(1{,}000)+v(-10)>0$. Then, if one is indifferent between $(x(1-p),p;-px,1-p)$ and $(0)$, one will not pay $px$ for $(x,p)$. People should show more risk seeking in accepting a fair gamble than in buying a gamble for a fair price (p. 288).

**Extensions (pp. 288–289).**
- Eqs. (1)–(2) extend straightforwardly to prospects with any number of outcomes. How compound prospects are reduced is yet to be investigated (p. 288).
- The theory should apply to other attributes (quality of life, lives lost or saved): outcomes coded as gains or losses against a neutral reference point, losses loom larger (p. 288).
- Without explicit probabilities, weights attach to events. For complementary events $A,B$, neither certain, $\pi(A)+\pi(B)<1$ is expected, as the analogue of subcertainty (p. 288).
- Weights depend mainly on perceived likelihood (possibly biased) and also on ambiguity. Ellsberg's and Fellner's work implies vagueness reduces weights, so subcertainty should be more pronounced for vague than for clear probabilities (p. 289).
- Two themes: editing, and the evaluation of gains, losses and uncertain outcomes (p. 289).

### Appendix: axiomatic sketch (pp. 289–290)
- Only an outline is given for regular prospects $(x,p;y,q)$ with $p+q<1$. The preference relation is stated to be "connected, symmetric and transitive"; indifference is $\approx$. Also $(x,p;y,q)\approx(y,q;x,p)$, $(x,p;0,q)\approx(x,p;0,r)$ and $(x,p;y,0)\approx(x,p;z,0)$: the null outcome and impossible event act as a multiplicative zero (p. 289).
- Because (1) is additive over probability–outcome pairs, additive conjoint measurement gives a scale $V$ and interval scales $f,g$ with $V(x,p;y,q)=f(x,p)+g(y,q)$. Key axioms (p. 289):
  - *Independence:* $(x,p;y,q)\succeq(x,p;y',q')$ iff $(x',p';y,q)\succeq(x',p';y',q')$.
  - *Cancellation:* if $(x,p;y',q')\succeq(x',p';y,q)$ and $(x',p';y'',q'')\succeq(x'',p'';y',q')$, then $(x,p;y'',q'')\succeq(x'',p'';y,q)$.
  - *Solvability:* if $(x,p;y,q)\succeq(z,r)\succeq(x,p;y',q')$ for some $z,r$, there exist $y'',q''$ with $(x,p;y'',q'')\approx(z,r)$.
- These suffice for the additive representation if the order is Archimedean. Symmetry plus $q=0$ gives $f=g$ (p. 289).
- For single non-zero outcomes, $V(x,p)=\pi(p)v(x)$ (multiplicative model). It needs the same axioms, plus sign dependence, and solvability must be weakened to bounded solvability (p. 289).
- Combining: $V(x,p;y,q)=f[\pi(p)v(x)]+f[\pi(q)v(y)]$. New *distributivity* axiom: $(x,p;y,p)\approx(z,p)$ iff $(x,q;y,q)\approx(z,q)$ (p. 290).
- With $\pi(q)<\pi(p)$ (without loss of generality), $\alpha=\pi(p)v(x)$, $\beta=\pi(p)v(y)$, $\gamma=\pi(p)v(z)$, $\theta=\pi(q)/\pi(p)$: $f(\alpha)+f(\beta)=f(\gamma)$ implies $f(\theta\alpha)+f(\theta\beta)=f(\theta\gamma)$ for all $0<\theta<1$. Since $f$ is strictly monotonic, $\gamma=f^{-1}[f(\alpha)+f(\beta)]$, so $\theta f^{-1}[f(\alpha)+f(\beta)]=f^{-1}[f(\theta\alpha)+f(\theta\beta)]$ (p. 290).
- The solution of this functional equation (Aczél) is $f(\alpha)=k\alpha^c$. So $V=k[\pi(p)v(x)]^c+k[\pi(q)v(y)]^c$, for some $k,c>0$. Redefining $\pi$, $v$, $V$ absorbs $k$ and $c$, giving the bilinear form (p. 290).

## Toy example (our own; numbers are illustrative, not estimates)
Goal: show how eq. (1) can reproduce the Allais pattern (Problems 1–2) that expected utility cannot.

Take $v(x)=x$ (linear, to isolate the role of $\pi$). Choose weights $\pi(.33)=.31$, $\pi(.34)=.32$, $\pi(.66)=.58$. Subcertainty holds: $\pi(.66)+\pi(.34)=.58+.32=.90<1$.

- Problem 1 (regular prospect, $p+q=.99<1$). $V(A)=\pi(.33)\cdot2500+\pi(.66)\cdot2400=.31\cdot2500+.58\cdot2400=775+1392=2167$. $V(B)=v(2400)=2400$. So $B\succ A$.
- Problem 2. $V(C)=.31\cdot2500=775$. $V(D)=.32\cdot2400=768$. So $C\succ D$.
- Check against the author's condition: $\pi(.33)/\pi(.34)=.31/.32=.969>v(2400)/v(2500)=.96>\pi(.33)/(1-\pi(.66))=.31/.42=.738$. ✓.
- Expected utility with $u$ linear and true probabilities gives $.34\cdot2400=816$ vs $.33\cdot2500=825$. This favours $C$ in Problem 2, and in Problem 1 $EU(A)=825+1584=2409>2400$, so it would favour $A$. So it cannot produce the modal pair (B, C). This holds for any $u$: B needs $.34u(2400)>.33u(2500)$, C needs the reverse (p. 266).

## Concepts
- [[expected utility]] — $U=\sum p_iu(x_i)$, tenet (i) of the theory under attack (p. 263)
- [[independence axiom]] — called the *substitution axiom* here: if $B\succ A$ then $(B,p)\succ(A,p)$; violated in Problems 3–8 (p. 266)
- [[risk aversion]] — preferring a sure $x$ to any risky prospect with expected value $x$; in expected utility equivalent to concave $u$ (p. 264)
- [[utility function]] — here defined on final asset positions (asset integration, tenet ii) (p. 264)
- [[preference relation]] — appendix prints the preference relation as "connected, symmetric and transitive" (p. 289)
- [[reference dependence]] — outcomes coded as gains or losses against a reference point, usually the status quo, but possibly an expectation or aspiration level (pp. 274, 286)
- [[loss aversion]] — losses loom larger than gains: $v(x)<-v(-x)$, and $v'(x)<v'(-x)$ if the derivative exists (p. 279)
- [[probability weighting]] — decision weights $\pi(p)$ replace probabilities: overweight low $p$, subcertain, not probabilities (pp. 275, 280–282)
- [[framing effect]] — equivalent problems get different choices (two-stage game; bonus problems); the authors also conjecture contingent insurance is more attractive than probabilistic insurance (pp. 271–273)
- [[risk vs. ambiguity]] — weights may also be affected by vagueness; the work of Ellsberg and Fellner implies vagueness reduces weights, per the authors (pp. 280, 289)
- [[certainty-effect]] (new) — outcomes obtained with certainty are overweighted relative to merely probable ones (p. 265)
- [[isolation-effect]] (new) — shared components of prospects are discarded, giving inconsistent preferences across formulations (p. 271)
- [[reflection-effect]] (new) — preferences between negative prospects mirror those between positive ones (p. 268)
- [[prospect-theory-value-function]] (new) — $v$ on gains and losses, $v(0)=0$; usually concave for gains, often convex for losses, steeper for losses (p. 279)
- [[subcertainty]] (new) — $\pi(p)+\pi(1-p)<1$ (p. 281)
- [[subproportionality]] (new) — $\pi(pq)/\pi(p)\le\pi(pqr)/\pi(pr)$; holds iff $\log\pi$ is convex in $\log p$ (p. 282)
- [[editing-phase]] (new) — coding, combination, segregation, cancellation, simplification, dominance detection before evaluation (pp. 274–275)
- [[probabilistic-insurance]] (new) — insurance that reduces but does not eliminate the loss probability; unattractive in the data (p. 269)

## Canonical instances
- [[allais-example]] — Problems 1–2 (and the Problems 3–4 version): certainty effect, violation of independence/substitution (pp. 265–266)
- [[problem-9-probabilistic-insurance]] — 80% reject it, although concave-$u$ expected utility predicts it beats regular insurance (pp. 269–270)
- [[two-stage-game-problem-10]] — same final-outcome distribution as Problem 4, opposite modal choice (p. 271)
- [[bonus-problems-11-12]] — identical in final states, opposite risk attitudes (p. 273)
- [[russian-roulette-zeckhauser]] — illustrates the hypothesized nonlinearity of $\pi$ (p. 283)
- [[long-shot-betting-day]] — cited as some support for the hypothesis that failure to adapt to losses induces risk seeking (p. 287)

## Bridges (candidates)
- [structural-analogy] $\pi(p)$ overweighting small $p$ and compressing mid-range $p$ ↔ decision-game-theory: probability weighting in cumulative/rank-dependent models — a nonlinear map from stated to effective probability.
- [structural-analogy] Editing by cancellation of shared components ↔ decision-game-theory: sure-thing principle — both concern what to do with components common to all options; here the theory says people cancel them in a way that depends on framing.
- [metaphor] Reference point as an adaptation level ↔ perception psychophysics: adaptation level in sensory judgment (the paper itself draws this parallel, p. 277).
- [structural-analogy] Subproportionality of $\pi$ ↔ decision-game-theory: common-ratio effect (Allais-type violations of independence).

## Questions this raises
- The theory fits Problems 1–14 by choosing $\pi$ and $v$ to satisfy inequalities; how would one estimate $v$ and $\pi$ from choice data, given the authors' warning that scaling is hard and that bids are unreliable (pp. 280, 284)?
- How are editing operations ordered, and when is the edited form unambiguous? The authors say it depends on structure and display and leave it open (p. 275).
- The theory permits indirect dominance violations (p. 284). Is that acceptable, and what forms of the weighting function avoid it?
- How should decision weights be attached to events when probabilities are not given, and how do ambiguity and perceived likelihood interact (pp. 288–289)?

## Reading notes
- Page offset: the file begins with a JSTOR cover page (pdf 1, no printed number). Printed = pdf − 1 for pdf 2–30 (printed 263–291). The JSTOR cover lists the article as pp. 263–292, while the last printed page here is 291 (references).
- Facts printed on these pages: Econometrica, Vol. 47, No. 2, March 1979 (p. 263 header and JSTOR cover); authors' affiliations (University of British Columbia and Stanford University) and manuscript dates (received November 1977, final revision March 1978) (p. 289).
- OCR: in the text layer, the caption of Figure 1 reads "FIGURE 2" twice. The image shows Figure 1 (Problem 4, standard) and Figure 2 (Problem 10, sequential) (p. 272). Several equations on pp. 281–285 were garbled in the text layer. Pages 281–283 and 285 were checked in the images, but p. 284 (including the Allais iff condition) was only available as text, so that condition was verified by re-deriving it from Problems 1–2. The text layer of p. 270 shows "p12" for $p/2$.
- Appendix wording: the preference relation is printed as "connected, symmetric and transitive". Since the same page then says $(x,p;y,q)\approx(y,q;x,p)$ separately, it is unclear from these pages whether "symmetric" is intended; the digest records the wording as printed.
- On p. 285 the probabilistic-insurance proof substitutes $f(y/2)\ge f(y)/2$ into a term with coefficient $[1-2\pi(p/2)]$. The author does not state that this coefficient must be non-negative for the substitution to be valid.
- The subproportionality rule is stated slightly differently on p. 267 ("$(y,pqr)$ is preferred to $(x,pr)$") and p. 282 ("$(x,pr)$ is not preferred to $(y,pqr)$"). The digest keeps both.
- No exercises appear in this unit, so no Exercises section.
