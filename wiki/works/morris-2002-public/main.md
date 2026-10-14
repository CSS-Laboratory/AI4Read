---
id: morris-2002-public/main
work: morris-2002-public
unit: paper
pages: 1521-1534
fields: [economics-finance]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Social Value of Public Information (Morris & Shin, 2002)

## L0 — One line
When agents want to match each other's actions as well as the true state, they overweight a public signal relative to the social optimum, so more precise public information can lower welfare if private information is already good.

## L1 — The gist (≤ 120 words)
The paper asks whether better public disclosure always helps when people care about the fundamentals and also about coordinating with others. In a beauty-contest model (agents want to match the state and each other) with a unique equilibrium, public information helps if agents have no private information. More precise private information always raises welfare. With private information, a more precise public signal can lower welfare when the coordination motive is strong ($r>0.5$) and the private signal is precise enough relative to the public one. Agents "overreact" to the public signal because they weight it too heavily, which magnifies its noise. The overreaction does not need irrationality. It matters for central-bank and regulatory disclosure policy.

**Prerequisites:** Normal distributions and precision (1/variance); Bayesian updating of a normal mean; best responses and Nash equilibrium; partial derivatives; geometric series.

## L2 — Key ideas (5–10 bullets)
- Public information has a dual role: it informs about fundamentals and serves as a focal point (a shared reference point) for beliefs. Its welfare effect must account for both (p. 1522).
- Payoffs combine a quadratic loss from the state with a zero-sum "beauty contest" term (a penalty for being far from others' actions). Social welfare depends only on the distance between actions and the state (p. 1524).
- With only public information, equilibrium is $a_i=y$ and welfare is $-\sigma_\eta^2$, so more precision always helps (p. 1525).
- With public and private signals the equilibrium is unique and linear. The weight on the public signal exceeds the weight that would be efficient for the social planner (pp. 1522, 1526–1528).
- Welfare rises in private precision $\beta$ always. Its derivative in public precision $\alpha$ is $\ge0$ if and only if $\beta/\alpha \le 1/[(2r-1)(1-r)]$; a harmful range exists only when $r>0.5$ (pp. 1528–1529).
- Mechanism: the average-expectations operator (the average across agents of their expectations) breaks the law of iterated expectations. Higher-order expectations (expectations of others' expectations) drift toward the public signal (pp. 1526, 1530).
- Overreaction also appears in a two-realization-signal example, and the authors say normality is not essential. With strategic substitutes (the best reply falls when others act more) the overreaction is to private information instead (pp. 1530–1531).
- Policy: disclosure must weigh timeliness against noise. Private and public information may become substitutes (pp. 1522–1523, 1532–1533).

## L3 — Walkthrough

### Introduction (pp. 1521–1524)
- The authors open by noting that more information, public or private, is generally beneficial for a decision maker acting in isolation (p. 1521). When decisions are linked, public information is "double-edged": it conveys fundamentals and also acts as a focal point (p. 1521). The sunspots literature stresses the second role. Policy makers (Basel disclosure pillar, central banks) stress the first (pp. 1521–1522).
- Authors' results: **(i)** with no private information, more public precision always raises welfare. **(ii)** With some private information, it need not. The more precise the private information, the more likely a precision increase lowers welfare (p. 1522).
- Cause: the coordination motive makes agents put too much weight on the public signal relative to the planner's weights, so noise in it is magnified. This "overreaction" needs no irrationality (p. 1522).
- Policy examples: the debate on publishing preliminary GDP figures in Japan; Australia's move from monthly to quarterly trade figures; flawed UK earnings data blamed for unjustifiably tight credit in 1998 (p. 1523). The authors argue central-bank disclosure matters more under interest-rate targeting, where policy works through market expectations (p. 1523).
- Related work is distinguished: herding/cascades (Banerjee; Bikhchandani et al.), Hirshleifer 1971, and strategic settings where uncertainty helps. The "global games" literature studies binary-action games. Here equilibrium is unique for all parameters, giving cleaner welfare statements (pp. 1523–1524).

### I. Model (pp. 1524–1528)
There is a continuum of agents $i\in[0,1]$, each choosing $a_i\in\mathbb R$. Payoff, with $0<r<1$:
$$u_i(a,\theta)=-(1-r)(a_i-\theta)^2-r(L_i-\bar L)\tag{1}$$
$$L_i=\int_0^1 (a_j-a_i)^2\,dj,\qquad \bar L=\int_0^1 L_j\,dj.$$
The first term is the loss from missing the state. The second is the "beauty contest" term, which rewards being close to others. It is zero-sum, since $\int (L_i-\bar L)\,di=0$ (added step). Social welfare is
$$W(a,\theta)=\frac{1}{1-r}\int_0^1 u_i\,di=-\int_0^1 (a_i-\theta)^2\,di,$$
so the planner wants all actions close to $\theta$ (p. 1524).
The first-order condition is
$$a_i=(1-r)E_i(\theta)+rE_i(\bar a),\qquad \bar a=\int_0^1 a_j\,dj.\tag{2}$$
If $\theta$ is common knowledge, $a_i=\theta$ for all $i$, which maximizes welfare. There is then no conflict between private and social optimum (p. 1525).

**A. Public-information benchmark.** The prior on $\theta$ is improper uniform. Everyone sees $y=\theta+\eta$, with $\eta\sim N(0,\sigma_\eta^2)$ independent of $\theta$ (eq. 3). Given $y$, $\theta\sim N(y,\sigma^2_\eta)$. The best reply is $a_i(y)=(1-r)E(\theta|y)+r\int E(a_j|y)\,dj$ (eq. 5). Since $E(\theta|y)=y$ and strategies depend only on $y$, the unique equilibrium is
$$a_i(y)=y,\tag{6}$$
and $E(W|\theta)=-E[(y-\theta)^2|\theta]=-\sigma_\eta^2$ (p. 1525).
*Intuition note:* With only a public signal, everyone shares the same belief and no one can be wrong about others. So the game adds nothing, and better public information helps.

**B. Private and public information.** Agent $i$ also sees $x_i=\theta+\varepsilon_i$, with $\varepsilon_i\sim N(0,\sigma^2_\varepsilon)$ independent across agents (eq. 7). Precisions: $\alpha=1/\sigma_\eta^2$ and $\beta=1/\sigma^2_\varepsilon$ (eq. 9). The information set is $I_i=(y,x_i)$ and
$$E_i(\theta)=\frac{\alpha y+\beta x_i}{\alpha+\beta}.\tag{10}$$
(pp. 1525–1526)

**C. Linear equilibrium.** Suppose all use $a_j=\kappa x_j+(1-\kappa)y$ (eq. 11). Then
$$E_i(\bar a)=\frac{\kappa\beta}{\alpha+\beta}x_i+\Bigl(1-\frac{\kappa\beta}{\alpha+\beta}\Bigr)y.$$
Plugging into (2) gives the coefficient on $x_i$:
$$\frac{\beta(r\kappa+1-r)}{\alpha+\beta}\tag{12}$$
Setting this equal to $\kappa$, so $\kappa=\beta(r\kappa+1-r)/(\alpha+\beta)$, gives $\kappa=\beta(1-r)/[\beta(1-r)+\alpha]$. Hence
$$a_i(I_i)=\frac{\alpha y+\beta(1-r)x_i}{\alpha+\beta(1-r)}.\tag{13}$$
(p. 1526) *Intuition note:* Private information is weighted less than its precision alone would justify (the factor $1-r$), because an agent also wants to be close to others, and others' beliefs are tied to $y$.

**D. Uniqueness.** Iterating (2) gives
$$a_i=(1-r)\sum_{k=0}^\infty r^kE_i(\bar E^k(\theta)),\tag{14}$$
where $\bar E(\theta)=\int E_i(\theta)\,di$. Higher-order expectations approach the public signal as the order $n$ grows (p. 1526).
**Lemma 1.** With $\mu=\beta/(\alpha+\beta)$: $\bar E^k(\theta)=(1-\mu^k)y+\mu^k\theta$ and $E_i(\bar E^k(\theta))=(1-\mu^{k+1})y+\mu^{k+1}x_i$.
*Proof* (p. 1527): induction on $k$. For $k=1$ it follows from (15), $E_i(\theta)=(\alpha y+\beta x_i)/(\alpha+\beta)$, and $\bar E(\theta)=(\alpha y+\beta\theta)/(\alpha+\beta)$. If it holds for $k-1$, then $E_i(\bar E^{k-1}(\theta))=(1-\mu^k)y+\mu^kx_i$, so $\bar E^k(\theta)=(1-\mu^k)y+\mu^k\theta$. Taking $E_i$ of this gives $(1-\mu^k)y+\mu^kE_i(\theta)=(1-\mu^{k+1})y+\mu^{k+1}x_i$.
Substituting into (14):
$$a_i=(1-r)\sum_k r^k[(1-\mu^{k+1})y+\mu^{k+1}x_i]=\Bigl(1-\frac{\mu(1-r)}{1-r\mu}\Bigr)y+\frac{\mu(1-r)}{1-r\mu}x_i=\frac{\alpha y+\beta(1-r)x_i}{\alpha+\beta(1-r)},$$
exactly (13). So the linear equilibrium is the unique equilibrium (p. 1527).

**E. Lucas–Phelps island economy.** Island $i$ has supply $y_i^s=b[a_i-E_i(\bar a)]$ and demand $y_i^d=c[E_i(\theta)-a_i]$, where $a_i$ is the price and $\theta$ the money supply. Market clearing gives (2) with $r=b/(b+c)$. Phelps (1983) asked how information on the money supply ties prices to fundamentals. The authors say their analysis formally answers that question. The island economy has no clear counterpart of the welfare function, so they work in the beauty-contest setting (pp. 1527–1528).

### II. Welfare effect of public information (pp. 1528–1530)
Substituting the signals into (13):
$$a_i=\theta+\frac{\alpha\eta+\beta(1-r)\varepsilon_i}{\alpha+\beta(1-r)}.\tag{16}$$
With $r=0$ the noise terms get weights equal to their relative precisions. With $r>0$ the public noise gets more weight and private noise less, and the effect grows with $r$ (p. 1528). Using $\alpha^2\sigma_\eta^2=\alpha$ and $\beta^2\sigma_\varepsilon^2=\beta$:
$$E[W|\theta]=-\frac{\alpha^2E(\eta^2)+\beta^2(1-r)^2E(\varepsilon_i^2)}{[\alpha+\beta(1-r)]^2}=-\frac{\alpha+\beta(1-r)^2}{[\alpha+\beta(1-r)]^2}.\tag{17}$$
Derivatives (p. 1529):
$$\frac{\partial E(W|\theta)}{\partial\beta}=\frac{(1-r)[(1+r)\alpha+(1-r)^2\beta]}{[\alpha+\beta(1-r)]^3}>0\tag{18}$$
$$\frac{\partial E(W|\theta)}{\partial\alpha}=\frac{\alpha-(2r-1)(1-r)\beta}{[\alpha+\beta(1-r)]^3}\tag{19}$$
(I re-derived (18) and (19) from (17); the page images for these pages were not supplied.)
$$\frac{\partial E(W|\theta)}{\partial\alpha}\ge0\iff\frac{\beta}{\alpha}\le\frac{1}{(2r-1)(1-r)}.\tag{20}$$
Reading of (20): this has bite only for $r>0.5$. For $r\le 0.5$ the numerator in (19) is positive (added step). For $r>0.5$ there are parameter ranges where more public precision is harmful. If agents are already very well informed (high $\beta$), any increase in public precision is harmful (p. 1529).
*Intuition note:* Private precision always helps. When $r>0.5$, public precision helps only when private information is not too precise relative to it. Agents put too much weight on the public signal and too little on private information (pp. 1528–1530).

Further points (p. 1529):
- Rule of thumb: when the private sector is well informed, officials should withhold extra information unless it is very precise.
- If precision is capped at $\bar\alpha$ and free, the optimum is "bang-bang": $\alpha=0$ or $\alpha=\bar\alpha$.
- Figure 1 shows welfare contours in $(\alpha,\beta)$-space. For $\beta>\alpha/[(2r-1)(1-r)]$ they slope upward, meaning welfare falls in $\alpha$. (Figure not visible in the pages supplied.)

**Intuition via (13).** Equation (13) can be rewritten as
$$a_i=\frac{\alpha y+\beta x_i}{\alpha+\beta}+(y-x_i)\Bigl(\frac{\alpha}{\alpha+\beta}\Bigr)\Bigl(\frac{\beta r}{\alpha+\beta(1-r)}\Bigr).\tag{21}$$
The first term is the Bayesian estimate of $\theta$. The extra term is positive in $y$ and negative in $x_i$. So agents overreact to the public signal and suppress the private one, and the noise $\eta$ gets more impact than it deserves (pp. 1529–1530).

**Higher-order expectations.** The operator $\bar E$ violates the law of iterated expectations:
$$\bar E(\theta)\neq\bar E(\bar E(\theta)),\qquad E_i(\bar E(\theta))\neq E_i(\theta).\tag{22}$$
If equality held, all higher orders would collapse to the first. Then (14) would give $E_i(\theta)\,(1-r)\sum_k r^k=E_i(\theta)$, the socially efficient action. The failure of iterated expectations creates strategic uncertainty and causes the overreaction (p. 1530). The authors link this to Phelps's emphasis on shared knowledge and to Woodford (2001), who attributes macro persistence to inertia of higher-order beliefs (p. 1530).

### III. Extensions and variations (pp. 1530–1532)
- A two-realization-signal example (online Appendix) shows overreaction to public information. Higher-order expectations converge to the expectation given public information only, a robust feature of differential-information economies (Samet 1998). Normality and the improper prior are not essential (p. 1530).
- **Strategic substitutes.** Let $a_i=E_i(\theta)-\rho E_i(\bar a)$ with $\rho>0$. Then
$$a_i=\frac{1}{1+\rho}\Bigl(\frac{\beta(1+\rho)}{\alpha+\beta(1+\rho)}x_i+\frac{\alpha}{\alpha+\beta(1+\rho)}y\Bigr).\tag{23}$$
The symmetric-information benchmark ($a_i=a_j$, so $a_i=E_i(\bar a)$) is
$$a_i=\frac{1}{1+\rho}\Bigl(\frac{\beta x_i+\alpha y}{\beta+\alpha}\Bigr).\tag{24}$$
Comparing (23) and (24), agents overreact to private information, to differentiate their actions. Radner's (1962) team loss $(a_1-\theta)^2+(a_2-\theta)^2+2q(a_1-\theta)(a_2-\theta)$ and Townsend's Cournot model are examples (pp. 1530–1531).
- **Aggregate objective.** Suppose the principal minimizes $\bigl(\tfrac1n\sum_ja_j-\theta\bigr)^2$ and agents use $a_i=\kappa x_i+(1-\kappa)y$. The expected loss at $\theta$ is
$$E\Bigl[\Bigl(\tfrac{\kappa}{n}\sum_j\varepsilon_j+(1-\kappa)\eta\Bigr)^2\Big|\theta\Bigr]=\frac{\kappa^2}{n\beta}+\frac{(1-\kappa)^2}{\alpha},$$
minimized at $\kappa=n\beta/(\alpha+n\beta)$. For large $n$ the principal wants little weight on $y$: private noise averages out, while $\eta$ does not (p. 1531). The authors call this example simplistic because it relies on i.i.d. noise (pp. 1531–1532).
- **Correlated private noise.** With $x_i=\theta+\xi+\varepsilon_i$ (common $\xi$), the Appendix gives alternative welfare functions and conditions for public information to be harmful. In a two-player, multi-signal, multivariate-normal version, correlated noise gives qualitatively similar effects (p. 1532).

### IV. Concluding remarks (pp. 1532–1533)
- Public information is effective at moving actions of strategic complements, but too effective, so mistaken disclosures can do great damage. Underweighting private information may devalue its ex ante value and the incentive to acquire it if costly (p. 1532).
- Krugman (2001) suggests $r$ may have grown, as firms emulate financial investors. In the model this vulnerability is individually rational but socially inefficient (p. 1532).
- Because markets watch officials closely, the authors say private sources "may actually crowd out" public information by making it detrimental. If the provider anticipates this, it may reduce public precision, so private and public information become substitutes, not cumulative (pp. 1532–1533).

## Toy example (ours)
Take $r=0.9$ and $\beta=100$ ($\sigma_\varepsilon^2=0.01$). The condition in (20) is $\beta/\alpha\le 1/[(0.8)(0.1)]=12.5$. For $\alpha<8$, $\beta/\alpha>12.5$ (condition (20) fails), so welfare falls in $\alpha$ (the derivative is zero at $\alpha=8$).
- $\alpha=1$ ($\sigma_\eta^2=1$): $D=\alpha+\beta(1-r)=1+10=11$. $E(W|\theta)=-[1+100(0.01)]/121=-2/121\approx-0.0165$. Check with weights: public noise weight $1/11$, so $(1/11)^2(1)=0.00826$; private noise weight $10/11$, so $(10/11)^2(0.01)=0.00826$; sum $0.0165$.
- $\alpha=2$ ($\sigma_\eta^2=0.5$): $D=12$. $E(W|\theta)=-3/144\approx-0.0208$. Check: $(1/6)^2(0.5)=0.01389$; $(5/6)^2(0.01)=0.00694$; sum $0.02083$. Welfare is lower.
- $\alpha=0$: $D=10$. $E(W|\theta)=-1/100=-0.01$, the best of the three. This illustrates the bang-bang result.
- Weight on $y$ in equilibrium is $\alpha/D=1/11\approx0.091$ at $\alpha=1$. The efficient Bayesian weight is $\alpha/(\alpha+\beta)=1/101\approx0.0099$, so the public signal is overweighted about nine-fold.

## Concepts
- [[beauty contest / higher-order beliefs]] — agents' payoff depends on matching others' actions, so expectations of expectations matter (p. 1524, 1530)
- [[social value of public information]] — welfare effect of public signal precision; may be negative when private information is precise (pp. 1522, 1529)
- [[coordination game / multiple equilibria]] — here a coordination motive exists, but equilibrium is unique for all parameters (p. 1524)
- [[Nash equilibrium]] — the linear strategy (13) is the unique equilibrium (pp. 1526–1527)
- [[common knowledge vs public information]] — public signal $y$ is common knowledge; it is a focal point for beliefs (pp. 1521, 1525)
- [[market failure / externality]] — the zero-sum second-guessing term is a socially inefficient spillover (p. 1524)
- [[rational expectations]] — agents are rational Bayesians; overreaction needs no irrationality (p. 1522)
- [[strategic complementarity / substitutability]] (new) — best reply rises (falls) in others' expected action; complements cause overweighting of public, substitutes of private information (pp. 1530–1531)
- [[overreaction to public information]] (new) — equilibrium weight on $y$ exceeds the Bayesian or planner weight (p. 1528)
- [[average expectations operator and failed iterated expectations]] (new) — $\bar E$ violates the law of iterated expectations, creating strategic uncertainty (p. 1530)
- [[bang-bang disclosure]] (new) — with capped, costless precision, the optimum is $\alpha=0$ or $\alpha=\bar\alpha$ (p. 1529)

## Canonical instances
- [[keynes-beauty-contest]] — the model's basis (p. 1524)
- [[lucas-phelps-island-economy]] — supply/demand model yields the same best-reply equation (pp. 1527–1528)
- [[radner-team-decision]] — strategic substitutes in team loss (p. 1531)
- [[central-bank-disclosure]] — policy application, incl. Japan GDP, Australia trade data, UK earnings data (p. 1523)

## Bridges (candidates)
- [structural-analogy] Overweighting of public signal ↔ economics-finance: herding/information cascades — both lose valuable private information (p. 1523), but via different mechanisms.
- [structural-analogy] Higher-order expectations anchored on public signal ↔ Keynesian beauty contest / conventional expectations — the focal public signal fixes what others are expected to do.
- [metaphor] Noise amplified by coordination ↔ narrative contagion — a widely shared story has outsized impact whether or not it is accurate.

## Questions this raises
- How would the result change if agents could choose how much private information to buy (the paper notes devalued incentives, p. 1532)?
- What if the public signal's noise is correlated with private noise, or the discloser has strategic motives?
- Is the weighted-welfare function ($W=-\int(a_i-\theta)^2$) the right criterion when policy cares about aggregates (p. 1531)?
- How strongly does empirical behaviour of markets reflect a high $r$ (Krugman's conjecture, p. 1532)?

## Reading notes
- Printed page = pdf page + 1520 (labels give printed numbers: 1521–1534).
- The text layer loses Greek letters and math symbols. I checked pages 5, 6, 7, 11 and 14 against images. For pages 8–10 (eqs. 16–22, Figure 1) no image was supplied, so I verified (17)–(21) by re-deriving them. Figure 1 could not be inspected.
- On page 9 the text layer shows "a 2 (2r−1)(1−r)b" in (19). I read it as $\alpha-(2r-1)(1-r)\beta$ and confirmed by differentiation.
- In the strategic-substitutes section the text layer prints the constant as "r", while the page image of p. 1531 shows $\rho$. I use $\rho$.
- The online Appendix is referred to but not part of this unit. Reference list (pp. 1533–1534) was not digested.
