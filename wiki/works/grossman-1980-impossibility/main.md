---
id: grossman-1980-impossibility/main
work: grossman-1980-impossibility
unit: paper
pages: 393-408
fields: [economics-finance]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# On the Impossibility of Informationally Efficient Markets (Grossman & Stiglitz, 1980)

## L0 — One line
If information is costly, prices cannot fully reflect it, because then nobody would be paid for gathering it; the equilibrium has a degree of informativeness at which informed and uninformed traders do equally well.

## L1 — The gist (≤ 120 words)
The paper asks whether a competitive market can be perfectly arbitraged when gathering information costs resources. It builds a model with informed traders, uninformed traders and noisy asset supply. Uninformed traders learn from the price, but only partly. Informativeness of the price depends on the share of traders who are informed, and that share is itself determined in equilibrium. With constant absolute risk aversion (CARA) utility and normal variables, the authors solve the model. If prices were fully informative, equilibrium would not exist. Markets whose prices reveal a lot are also likely to be thin, because beliefs are very similar. The authors say this redefines the efficient-markets notion rather than destroying it.

**Prerequisites:** expected utility; normal distribution and conditional expectation/variance of jointly normal variables; exponential (CARA) utility; basic idea of rational expectations and market clearing.

## L2 — Key ideas
- Perfect arbitrage and costly arbitrage are inconsistent: if prices reflected all information, informed traders would earn nothing from paying for it (p. 393).
- The model has an "equilibrium degree of disequilibrium": prices reveal informed traders' information only partially, and the fraction informed ($\lambda$) is endogenous (pp. 393–394). (Notation: $\theta$ = the part of the risky return that informed traders observe, at cost $c$; $a$ = risk-aversion coefficient; $n=\sigma_\theta^2/\sigma_\epsilon^2$ = quality of the informed trader's information; $x$ = per capita supply of the risky asset, the source of noise; $\rho_\theta^2$ = squared correlation of price with $\theta$, p. 399.)
- Under CARA utility and normality, price is informationally equivalent to $w_\lambda=\theta-\frac{a\sigma_\epsilon^2}{\lambda}(x-Ex^*)$, i.e. $\theta$ plus noise (Theorem 1, p. 397).
- Overall equilibrium requires $\gamma(\lambda)=1$, the expected-utility ratio (informed/uninformed) being one. $\gamma$ is strictly increasing in $\lambda$, so among price equilibria monotone in $w_\lambda$ the overall equilibrium is unique (Theorems 2–3, Corollary 1, pp. 398–399).
- At an interior equilibrium, price informativeness depends only on $c$, $n$ and $a$: $1-\rho_\theta^2=(e^{2ac}-1)/n$. A change in noise is exactly offset by a change in $\lambda$ (eq. 19b, Theorem 4, pp. 399–400).
- If information is perfect, no equilibrium ever exists; with no noise, none exists when $e^{ac}<\sqrt{1+n}$ (Theorem 5; for no noise the theorem is stated "if (and only if)" $e^{ac}<\sqrt{1+n}$) (p. 401).
- When $c$ is large or small, or $n\to\infty$, mean and variance of trade go to zero. Markets whose prices reveal a lot are thin because beliefs are similar (Theorem 6, pp. 402–403).
- Costless information is sufficient but, the authors argue, also necessary for fully revealing prices. Adding as many securities as states of nature would break equilibrium, so a limited number of markets is needed for equilibrium (p. 404).

## L3 — Walkthrough

### Introduction (p. 393)
- **Authors' question:** if competitive equilibrium means no arbitrage profits, can an economy always be in equilibrium? They answer no: arbitrageurs would earn nothing for a costly activity. Assumptions that all markets, including that for information, are always in equilibrium and perfectly arbitraged are inconsistent when arbitrage is costly (p. 393).
- **Their proposal:** prices reflect informed traders' information only partially, so informed traders are compensated. Informativeness depends on the number informed, and that number is endogenous. The authors call the imperfection of transmission "perhaps lucky", since were it perfect, no equilibrium would exist (p. 393).

### I. The Model (pp. 393–395)
- Two assets: a safe asset with return $R$, and a risky asset with return $u$ (p. 393):
$$u=\theta+\epsilon \tag{1}$$
 $\theta$ is observable at cost $c$; $\epsilon$ is not. Informed traders observe $\theta$; uninformed traders observe only price (p. 393). Ex ante all individuals are identical; they differ only in whether they paid $c$ (p. 393).
- Uninformed traders have rational expectations: they learn the relationship between the distribution of return and price and use it (p. 394). Let $x$ be the supply of the risky asset. Uninformed traders do not observe $x$, so they cannot tell price moves caused by $\theta$ from those caused by $x$. The price therefore reveals only part of $\theta$ (p. 394).
- Adjustment of $\lambda$: if informed expected utility (net of $c$) exceeds uninformed, people switch to being informed, and conversely. Overall equilibrium needs equal expected utilities (p. 394).
- As $\lambda$ rises, the informed's relative advantage falls, for two reasons (p. 394):
  - (a) the price becomes more informative, so the information gap, and hence the magnitude of the informed's gain relative to the uninformed, is reduced; the informed gain from trading with the uninformed, buying when "underpriced" and selling when "overpriced";
  - (b) per capita gains from trading with the uninformed shrink as their ratio grows.
- **Conjectures (the authors could not prove them in general; pp. 394–395):**
  1. More informed individuals → more informative price.
  2. More informed → lower ratio of informed to uninformed expected utility.
  3. Higher cost of information → smaller equilibrium percentage informed.
  4. Better quality of $\theta$ makes the price more informative. The equilibrium proportion informed may rise or fall, because being uninformed also becomes more valuable.
  5. More noise → less informative price and lower uninformed utility, so in equilibrium a larger proportion is informed.
  6. With no noise prices convey all information, so the only possible equilibrium has no one informed. But if all are uninformed, it pays someone to become informed. So no competitive equilibrium exists.
  7. Markets are thinner when $\lambda$ is near zero or near one (very little noise; or very low information cost).
- Footnote 5: informational equilibria may not exist in general (Green 1977), but with the utility chosen here equilibrium does exist (p. 395).

### II. Constant Absolute Risk-Aversion Model (pp. 395–398)

**A–B. Securities and individual maximization (pp. 395–396).** Trader $i$ holds $\bar M_i$ of the riskless asset (price 1) and $\bar X_i$ of the risky asset (price $P$):
$$PX_i+M_i=W_{0i}\equiv \bar M_i+P\bar X_i \tag{2}$$
$$W_{1i}=RM_i+uX_i \tag{3}$$
Utility is $V(W_{1i})=-e^{-aW_{1i}}$, $a>0$ (coefficient of absolute risk aversion). $\theta,\epsilon$ are multivariate normal with
$$E\epsilon=0 \tag{4}$$
$$E\theta\epsilon=0 \tag{5}$$
$$Var(u^*|\theta)=Var\,\epsilon^*\equiv\sigma_\epsilon^2>0 \tag{6}$$
$W_{1i}$ is normal given $\theta$, so for an informed trader
$$E(V(W_{1i}^*)|\theta)=-\exp\!\Big(-a\Big\{E[W_{1i}^*|\theta]-\tfrac a2 Var[W_{1i}^*|\theta]\Big\}\Big)=-\exp\!\Big(-a\Big[RW_{0i}+X_I(\theta-RP)-\tfrac a2X_I^2\sigma_\epsilon^2\Big]\Big) \tag{7}$$
Maximizing over $X_I$:
$$X_I(P,\theta)=\frac{\theta-RP}{a\sigma_\epsilon^2} \tag{8}$$
Demand does not depend on wealth (p. 396).

For the uninformed, with $P^*(\cdot)$ some price function such that $u^*$ and $P^*$ are jointly normal:
$$E(V(W_{1i}^*)|P^*)=-\exp\Big[-a\Big\{RW_{0i}+X_U(E[u^*|P^*]-RP)-\tfrac a2X_U^2Var[u^*|P^*]\Big\}\Big] \tag{7'}$$
$$X_U(P;P^*)=\frac{E[u^*|P^*(\theta,x)=P]-RP}{a\,Var[u^*|P^*(\theta,x)=P]} \tag{8'}$$
The only noise is per capita supply $x$ (p. 396).

> Intuition note: with CARA utility and normal returns, each trader's demand is (expected excess return) ÷ (risk aversion × variance). The informed know $\theta$; the uninformed use their best guess of $u$ from the price.

**C. Equilibrium price distribution (p. 396).** For a fraction $\lambda$ informed, an equilibrium price function $P_\lambda(\theta,x)$ clears the market for all $(\theta,x)$:
$$\lambda X_I(P_\lambda(\theta,x),\theta)+(1-\lambda)X_U(P_\lambda(\theta,x);P_\lambda^*)=x \tag{9}$$
It is a "statistical equilibrium": after traders learn the joint distribution of $(u^*,P^*_\lambda)$ from many realizations, that distribution persists (p. 396).

**D. Existence and characterization (p. 397).** Define
$$w_\lambda(\theta,x)=\theta-\frac{a\sigma_\epsilon^2}{\lambda}(x-Ex^*)\quad(\lambda>0) \tag{10a}$$
$$w_0(\theta,x)=x\quad\text{for all }(\theta,x) \tag{10b}$$
**Theorem 1.** If $(\theta^*,\epsilon^*,x^*)$ has a nondegenerate joint normal distribution with $\theta^*,\epsilon^*,x^*$ mutually independent, a solution to (9) exists of the form $P_\lambda=\alpha_1+\alpha_2w_\lambda(\theta,x)$ with $\alpha_2>0$ ($\alpha_1,\alpha_2$ may depend on $\lambda$). If $\lambda=0$, price contains no information about $\theta$. The exact form is (A10) in Appendix B (p. 397).

So $P^*_\lambda$ is informationally equivalent to $w^*_\lambda$, a "mean-preserving spread" of $\theta$: $E[w_\lambda^*|\theta]=\theta$ and
$$Var[w_\lambda^*|\theta]=\frac{a^2\sigma_\epsilon^4}{\lambda^2}Var\,x^* \tag{11}$$
The noise is inversely proportional to $\lambda$ and proportional to $\sigma_\epsilon^2$. $Var[w^*_\lambda|\theta]=0$ means observing $w$ is equivalent to observing $\theta$. A large value means a given $w$ says little about $\theta$ (p. 397; fn. 7 links smaller variance to more informative in Blackwell's sense).

> Intuition note: the price is "$\theta$ plus a random error coming from supply". The error shrinks when risk aversion is low, information is precise, or many traders are informed, because informed demand then moves strongly with $\theta$ and supply shocks matter less.

**E. Equilibrium in the information market (p. 398).** An overall equilibrium is a pair $(\lambda,P^*_\lambda)$ where expected utilities are equal if $0<\lambda<1$; $\lambda=0$ if informed utility is lower than uninformed at $P_0^*$; $\lambda=1$ if informed utility is higher at $P_1^*$. End-of-period wealths:
$$W^\lambda_{Ii}\equiv R(W_{0i}-c)+[u-RP_\lambda(\theta,x)]X_I(P_\lambda(\theta,x),\theta) \tag{12a}$$
$$W^\lambda_{Ui}\equiv RW_{0i}+[u-RP_\lambda(\theta,x)]X_U(P_\lambda(\theta,x);P_\lambda^*) \tag{12b}$$
A trader does not know which $\theta$ he will see when he pays $c$; expected utility averages over $\theta^*,\epsilon^*,x^*,W_{0i}$ (p. 398).

**Theorem 2.** Under Theorem 1's assumptions, and if $\bar X_i$ is independent of $(u^*,\theta^*,x^*)$,
$$\frac{EV(W^\lambda_{Ii})}{EV(W^\lambda_{Ui})}=e^{ac}\sqrt{\frac{Var(u^*|\theta)}{Var(u^*|w_\lambda)}} \tag{13}$$
(proof in Appendix B below; p. 398).

**F. Existence of overall equilibrium (pp. 398–399).** Define
$$\frac{EV(W^\lambda_{Ii})}{EV(W^\lambda_{Ui})}=e^{ac}\sqrt{\frac{Var(u^*|\theta)}{Var(u^*|w_\lambda)}}\equiv\gamma(\lambda) \tag{14}$$
Equilibrium with $0<\lambda<1$ requires
$$\gamma(\lambda)=1 \tag{15}$$
**Theorem 3.** If $0\le\lambda\le1$, $\gamma(\lambda)=1$ and $P^*_\lambda$ is given by (A10), then $(\lambda,P^*_\lambda)$ is an overall equilibrium. If $\gamma(1)<1$, $(1,P_1^*)$ is one; if $\gamma(0)>1$, $(0,P_0^*)$ is one. For all price equilibria monotone in $w_\lambda$ there is a unique overall equilibrium. Uniqueness follows from monotonicity of $\gamma$ ((A11), (14)) (p. 398).

**Corollary 1.** $\gamma(\lambda)$ is strictly increasing in $\lambda$. This looks paradoxical, but utility is negative, so a higher ratio means informed utility is lower relative to uninformed (pp. 398–399). Also $\gamma(0)=e^{ac}(Var(u^*|\theta)/Var\,u^*)^{1/2}$. Figure 1 assumes $\gamma(0)<1<\gamma(1)$ (p. 399).

**G. Characterization (p. 399).** Define
$$m=\Big(\frac{a\sigma_\epsilon^2}{\lambda}\Big)^2\frac{\sigma_x^2}{\sigma_\theta^2}\tag{16a}$$
$$n=\frac{\sigma_\theta^2}{\sigma_\epsilon^2}\tag{16b}$$
$m$ is inversely related to price informativeness, since the squared correlation between $P^*_\lambda$ and $\theta^*$ is
$$\rho_\theta^2=\frac1{1+m}\tag{17}$$
and $n/(1+n)$ is the squared correlation between $\theta^*$ and $u^*$. From (1), (A11) and (16):
$$\frac{Var(u^*|\theta)}{Var(u^*|w_\lambda)}=\frac{1+m}{1+m+nm}=\Big(1+\frac{nm}{1+m}\Big)^{-1}\tag{18}$$
Substituting into (14) and using (15), for $0<\lambda<1$ in equilibrium:
$$m=\frac{e^{2ac}-1}{1+n-e^{2ac}}\tag{19a}$$
$$1-\rho_\theta^2=\frac{e^{2ac}-1}{n}\tag{19b}$$
(added step: $\gamma=1$ gives $(1+m)e^{2ac}=1+m+nm$, i.e. $e^{2ac}-1=m(1+n-e^{2ac})$.) (19) holds for $\gamma(0)<1<\gamma(1)$, which insures that equilibrium $\lambda$ lies between 0 and 1. Equilibrium informativeness is determined entirely by $c$, $n$ and $a$ (p. 399).

> Intuition note: in equilibrium the cost of information fixes how much better informed than the market an informed trader must be. That fixes how informative the price is. The share $\lambda$ then adjusts to deliver this informativeness.

**H. Comparative statics (pp. 399–400).** From (19b):
1. Higher $n$ → more informative price.
2. Lower $c$ → more informative price.
3. Lower risk aversion → larger positions → more informative price.

Other parameter changes that keep $n,a,c$ fixed leave informativeness unchanged. They change only $\lambda$, by exactly enough to offset:
4. More noise ($\sigma_x^2$) raises $\lambda$. At a given $\lambda$, more noise lowers informativeness, but raises returns to information. The two effects "exactly offset each other" (pp. 399–400). In Figure 1: from (16a) higher $\sigma_x^2$ raises $m$, which lowers $Var(u^*|\theta)/Var(u^*|w_\lambda)$, shifting $\gamma$ down and raising equilibrium $\lambda$ (p. 400).
5. Higher $\sigma_u^2$ with $n$ constant raises $\lambda$ the same way; informativeness is unchanged (p. 400).
6. Raising $\sigma_\theta^2$ with $\sigma_u^2$ fixed (so $\sigma_\epsilon^2$ falls) raises $n$, so informativeness rises. $m$ and $nm$ both fall, so $\gamma$ may shift up or down depending on $c,a,n$. Better information raises the benefit of being informed, but some of it reaches the uninformed via a more informative price (p. 400).
   - Footnote 8: $\lambda$ rises iff $nm/(1+m)$ rises, and
$$\text{sgn}\frac{d}{d\sigma_\theta^2}\Big(\frac{nm}{1+m}\Big)=\text{sgn}\Big[m\frac{n+1}{n}-1\Big]=\text{sgn}\Big[\Big(\frac{\gamma}{n-\gamma}\Big)\Big(\frac{n+1}{n}\Big)-1\Big]$$
 with $\gamma\equiv e^{2ac}-1$ (here a symbol reused). For $n$ very large the derivative is negative ($\lambda$ falls); for $n$ sufficiently small it is positive ($\lambda$ rises) (p. 400, fn. 8).
7. Higher $c$ shifts $\gamma$ up and lowers the percentage informed (p. 400).

**Theorem 4** (for $0<\lambda<1$; p. 400): (A) $\rho_\theta^2$ rises if $n$ rises, $c$ falls, or $a$ falls. (B) $\rho_\theta^2$ is unchanged if $\sigma_x^2$ changes, or if $\sigma_u^2$ changes with $n$ fixed. (C) $\lambda$ rises if $\sigma_x^2$ rises, $\sigma_u^2$ rises for fixed $n$, or $c$ falls. (D) If $\bar n$ satisfies $\frac{e^{2ac}-1}{\bar n-(e^{2ac}-1)}=\frac{\bar n}{\bar n+1}$, then $n>\bar n$ ($n<\bar n$) implies $\lambda$ falls (rises) when $n$ increases. A–C are proved by the remarks above; D by fn. 8.

### I. Price cannot fully reflect costly information (pp. 400–401)
Limiting cases (the source prints $\gamma(0)\le1\le\gamma(1)$ here):
1. As $c\to0$, price becomes more informative, but at a positive $\hat c$ all traders are informed, where $e^{a\hat c}\sqrt{Var(u^*|\theta)/Var(u^*|w_1)}=1$ (pp. 400–401).
2. As $n\to\infty$ ($\sigma_\epsilon^2\to0$, $\sigma_\theta^2\to\sigma_u^2$ fixed), price becomes perfectly informative and $\lambda\to0$. Equilibrium needs $nm/(1+m)$ constant. $m$ falls by (19b) and (17), so $nm$ must fall, but $nm$ must not go to zero (or $nm/(1+m)$ would not be constant). Since $nm=(a/\lambda)^2\sigma_\epsilon^2\sigma_x^2$, $\lambda$ must go to zero (p. 401).
3. As $\sigma_x^2\to0$, $\lambda\to0$ and, since (19a) has no $\sigma_x^2$, $m$ and informativeness are unchanged (p. 401).

Suppose $c$ is small enough that it pays to be informed when no one else is. If $\sigma_x^2=0$ or $\sigma_\epsilon^2=0$, no competitive equilibrium exists, because the utility ratio is discontinuous at $\lambda=0$ (p. 401). At $\lambda=0$, $Var(u^*|w_0)=Var\,u^*$, so
$$\frac{EV(W^0_{Ii})}{EV(W^0_{Ui})}=e^{ac}\sqrt{\frac{\sigma_\epsilon^2}{\sigma_\epsilon^2+\sigma_\theta^2}}=e^{ac}\sqrt{\frac1{1+n}}\tag{20}$$
For $\lambda>0$, by (18) the ratio is $e^{ac}\sqrt{1/(1+n\frac m{m+1})}$. If $\sigma_x^2=0$ or $\sigma_\epsilon^2=0$ then $m=0$, $nm=0$ for $\lambda>0$, so
$$\lim_{\lambda\to0}\frac{EV(W^\lambda_{Ii})}{EV(W^\lambda_{Ui})}=e^{ac}\tag{21}$$

**Theorem 5.** (a) If there is no noise ($\sigma_x^2=0$), an overall equilibrium does not exist if (and only if) $e^{ac}<\sqrt{1+n}$. (b) If information is perfect ($\sigma_\epsilon^2=0$, $n=\infty$), an equilibrium never exists (p. 401).
- Proof (a) key step: by (20) and (21), $\gamma(0)<1$ but $\gamma(\lambda)>1$ for $\lambda>0$. So neither $\lambda=0$ nor $\lambda>0$ is an equilibrium.
- Proof (b): $nm=0$ for $\lambda>0$, so $\gamma>1$ by (21); $\gamma(0)=0<1$.

> Intuition note: with no noise, any informed trader sees that the price already carries all information, so he would drop out. With no one informed, the price carries nothing, so (if $c$ is low enough, $e^{ac}<\sqrt{1+n}$) it pays to become informed. Neither state can persist, so no equilibrium exists.

### III. On the Thinness of Speculative Markets (pp. 402–403)
- Trade needs differences in endowments, preferences or beliefs. Section III drops preference differences as an explanation, citing Grossman's earlier argument that they are not a major factor (p. 402).
- Argument: operating a market has fixed costs. If traders have identical endowments and beliefs, competitive equilibrium leaves them at their endowments, so they would not enter. The authors say they will show continuity: with identical endowments and slightly different beliefs, the equilibrium allocation is only slightly different from the endowment, so the gain from entering is slight (p. 402).
- The authors note that one might have conjectured that markets are thin when almost all traders are informed or almost all uninformed, but this is not obvious (a single trader's trade may depend on $\lambda$, and a few active traders can do the job of many small ones); in their model "there is a sense" in which the conjecture is correct (p. 402).
- Per capita net trade is normal. With $x̄=Ex^*$, $\bar\theta=E\theta^*$, an informed trader's net trade is (footnote 10, pp. 402–403; $h$ as printed)
$$X_I-x=\frac{(1-\lambda)\big[(nm+\tfrac{ah}{\lambda})(x-\bar x)+[(m+1)n-1](\theta-\bar\theta)+\bar x nm\big]}{(1+m+\lambda nm)n}$$
- Mean of total informed trade:
$$E\lambda(X_I-x)=\frac{(1-\lambda)\lambda m\bar x}{1+m+\lambda nm}\tag{23}$$
- Its variance:
$$\sigma_\theta^2(1-\lambda)^2\lambda^2\Big[[(m+1)n-1]^2+\Big(nm+\frac{a\sigma_\epsilon^2}{\lambda}\Big)^2\frac{\sigma_x^2}{\sigma_\theta^2}\Big]\div(1+m+\lambda nm)^2n^2\tag{24}$$
- Mean and variance go to zero as $\lambda\to0$. This is not trivial: when $\lambda\to0$ because $n\to\infty$, informed demand $X_I$ goes to infinity at most prices (p. 403).

**Theorem 6** (as printed): (a) For sufficiently large or small $c$, the mean and variance of trade are zero. (b) As $n\to\infty$ they go to zero (p. 403).
- (a) Small $c$: $\lambda=1$ if $c\le\hat c$, so (23)–(24) are zero. Large $c$: for some $c^0$, $\gamma(0)=1$ so $\lambda=0$. As $c\uparrow c^0$, $\lambda\to0$ and $nm/(1+m)$ has a finite positive limit, so (22) and (24) go to zero (p. 403).
- (b) $nm/(1+m)$ is constant as $n\to\infty$, and $\lambda\to0$ (remark 2, p. 401), so (23)–(24) go to zero.
- (c) (in the proof, not in the printed statement) As $\sigma_x^2\to0$, $m$ is constant and $\lambda\to0$; in (24), $(nm+a\sigma_\epsilon^2/\lambda)^2\sigma_x^2/\sigma_\theta^2=(nm\sigma_x/\sigma_\theta+m^{1/2})^2$ by (16a), so variance goes to zero (p. 403).

Since $\lambda(X_I-x)+(1-\lambda)(X_U-x)=0$, no trade occurs as $\lambda\to1$. The authors read the incompatibility of competitive equilibrium with informationally efficient markets as meaning: speculative markets where prices reveal a lot of information will be very thin, because traders have very similar beliefs (p. 403).

> Intuition note: markets where almost everybody is informed, or almost nobody, have few belief differences to trade on. In this model trade goes to zero as $\lambda\to0$ (Theorem 6) and as $\lambda\to1$; the authors say this is not obvious in general (p. 402).

### IV. On the Possibility of Perfect Markets (pp. 403–405)
- Price gives uninformed traders $\theta$ to within noise $(a\sigma_\epsilon^2/\lambda)(x-Ex^*)$ with variance $(a\sigma_\epsilon^2/\lambda)^2Var\,x^*$, so in general it does not reveal all information about the "true value" $\theta$ (pp. 403–404).
- **Efficient-markets claim (as the authors report it):** Fama says "at any time prices fully reflect all available information" (p. 404). The authors say that if so, informed traders could earn no return. They say efficient-markets theorists seem aware that costless information is sufficient for fully reflecting prices, but not that it is necessary. This is a reductio, since price systems matter only when information is costly (Hayek) (p. 404).
- "We are attempting to redefine the Efficient Markets notion, not destroy it." With very cheap information or very precise signals, equilibrium exists and prices reveal most of the informed traders' information, but such markets are likely thin (p. 404).
- **Endogenous markets:** where differences in beliefs are not completely arbitraged, there is an incentive to create a market (Grossman's futures-market model). Because beliefs are endogenous, creating markets removes the differences that gave rise to them, so those markets disappear. Costless market creation would mean equilibrium never exists (p. 404).
- **Example:** add a security paying $z=1$ if $u>E\theta^*$, $0$ otherwise. Market clearing is $\lambda y_I(q,p,\theta)+(1-\lambda)y_u(q,p)=0$. Under weak assumptions $q$ and $p$ convey all information about $\theta$, so the market is noiseless and no equilibrium exists (p. 404).
- **Conclusion:** the authors say one could argue that, once the conventional perfect-capital-markets assumptions are modified to allow even slight information imperfection and a slight cost of information, the traditional theory becomes untenable. There cannot be as many securities as states of nature. Equilibrium exists only because costly transactions limit the number of markets (pp. 404–405).
- **Closing:** there is a fundamental conflict between the efficiency of spreading information and the incentive to acquire it. Social welfare of the equilibrium is not examined (p. 405).

### Appendix A (p. 405)
For jointly normal $X^*,Y^*$:
$$E[X^*|Y^*=Y]=EX^*+\frac{Cov(X^*,Y^*)}{Var(Y^*)}\{Y-EY^*\}\tag{A1}$$
$$Var[X^*|Y^*=Y]=Var(X^*)-\frac{[Cov(X^*,Y^*)]^2}{Var(Y^*)}\tag{A2}$$
$$E\{E[X^*|Y^*=Y]\}=EX^*\tag{A3}$$
(A2) does not depend on $Y$. (A4), (A5) are two properties of iterated conditional expectation with $F(\cdot)$ a function of $X^*$.

### Appendix B: proof of Theorem 1 (pp. 405–406)
- (a) $\lambda=0$: define $P_0(\theta,x)\equiv(E\theta^*-ax\sigma_u^2)/R$ (A7). It is uncorrelated with $u^*$, so $E[u^*|P_0^*]=Eu^*=E\theta^*$ and $Var[u^*|P_0^*]=Var\,u^*$ (A8). Then $X_U=(E\theta^*-RP_0)/(a\,Var\,u)$ (A9), which equals $x$ after substituting (A7).
- (b) $0<\lambda\le1$: 
$$P_\lambda(\theta,x)=\frac{\dfrac{\lambda w_\lambda}{a\sigma_\epsilon^2}+\dfrac{(1-\lambda)E[u^*|w_\lambda]}{a\,Var[u^*|w_\lambda]}-Ex^*}{R\Big[\dfrac{\lambda}{a\sigma_\epsilon^2}+\dfrac{1-\lambda}{a\,Var[u^*|w_\lambda]}\Big]}\tag{A10}$$
With (A11a–c): $E(u^*|w_\lambda)=E\theta^*+\frac{\sigma_\theta^2}{Var\,w_\lambda}(w_\lambda-E\theta^*)$, $Var(u^*|w_\lambda)=\sigma_\theta^2+\sigma_\epsilon^2-\frac{\sigma_\theta^4}{Var\,w_\lambda}$, $Var\,w_\lambda=\sigma_\theta^2+(a\sigma_\epsilon^2/\lambda)^2Var\,x^*$.
- $P_\lambda$ is linear in $w_\lambda$, so conditioning on $P_\lambda$ equals conditioning on $w_\lambda$. Market clearing then requires the identity
$$\lambda\frac{\theta-RP_\lambda}{a\sigma_\epsilon^2}+(1-\lambda)\frac{E[u^*|w_\lambda]-RP_\lambda}{a\,Var[u^*|w_\lambda]}=x\tag{A12}$$
 It holds identically in $(\theta,x)$ by (10) (p. 406).

### Appendix B: proof of Theorem 2 (pp. 406–407)
(a) *Informed utility.* Given $(\bar X_i,\theta,x)$, $W^\lambda_{Ii}$ is normal, so with (8), (12):
$$E[W^\lambda_{Ii}|\bar X_i,\theta,x]=R(W_{0i}-c)+\frac{(E[u^*|\theta]-RP_\lambda)^2}{a\sigma_\epsilon^2}\tag{A14a}$$
$$Var[W^\lambda_{Ii}|\bar X_i,\theta,x]=\frac{(E[u^*|\theta]-RP_\lambda)^2}{a^2\sigma_\epsilon^2}\tag{A14b}$$
Substituting into (A13) (the normal-utility formula):
$$E[V(W^\lambda_{Ii})|\bar X_i,\theta,x]=-\exp\Big[-aR(W_{0i}-c)-\frac1{2\sigma_\epsilon^2}(E[u^*|\theta]-RP_\lambda)^2\Big]\tag{A15}$$
By (A5), $E(E[V|\bar X_i,\theta,x]|P_\lambda,\bar X_i)=E[V(W_{Ii}^\lambda)|P_\lambda,\bar X_i]$ (A16). Define
$$h_\lambda\equiv Var(E[u^*|\theta]|w_\lambda)=Var(\theta|w_\lambda)\tag{A18}$$
$$Z\equiv\frac{E[u^*|\theta]-RP_\lambda}{\sqrt{h_\lambda}}\tag{A19}$$
Then (A17)–(A20) give
$$E[V(W^\lambda_{Ii})|P_\lambda,\bar X_i]=e^{ac}V(RW_{0i})E\Big[\exp\Big(-\frac{h_\lambda}{2\sigma_\epsilon^2}Z^2\Big)\Big|w_\lambda\Big]$$
since $\bar X_i$ and $w_\lambda$ are independent. Given $w_\lambda$, $Z^2$ is noncentral chi-square with moment generating function, for $t>0$,
$$E[e^{-tZ^2}|w_\lambda]=\frac1{\sqrt{1+2t}}\exp\Big[\frac{-(E[Z|w_\lambda])^2t}{1+2t}\Big]\tag{A21}$$
Also $E[E[u^*|\theta]|w_\lambda]=E[u^*|w_\lambda]=E\theta^*+\frac{\sigma_\theta^2}{Var\,w_\lambda}(w_\lambda-E\theta^*)$ (A22), so $E[Z|w_\lambda]=(E[u^*|w_\lambda]-RP_\lambda)/\sqrt{h_\lambda}$ (A23), and $Var(u^*|w_\lambda)=\sigma_\epsilon^2+h_\lambda$ (A24). Nondegeneracy gives $h_\lambda>0$. Setting $t=h_\lambda/2\sigma_\epsilon^2$ in (A21):
$$E\Big[\exp\Big(-\frac{h_\lambda}{2\sigma_\epsilon^2}Z^2\Big)\Big|w_\lambda\Big]=\sqrt{\frac{Var(u^*|\theta)}{Var(u^*|w_\lambda)}}\exp\Big(\frac{-(E(u^*|w_\lambda)-RP_\lambda)^2}{2Var(u^*|w_\lambda)}\Big)\tag{A25}$$
(b) *Uninformed utility*, by parallel calculations to (A13)–(A25):
$$E[V(W^\lambda_{Ui})|w_\lambda,\bar X_i]=V(RW_{0i})\exp\Big(\frac{-(E(u^*|w_\lambda)-RP_\lambda)^2}{2Var(u^*|w_\lambda)}\Big)\tag{A26}$$
Hence
$$E[V(W^\lambda_{Ii})|w_\lambda,\bar X_i]-E[V(W^\lambda_{Ui})|w_\lambda,\bar X_i]=\Big[e^{ac}\sqrt{\tfrac{Var(u^*|\theta)}{Var(u^*|w_\lambda)}}-1\Big]E[V(W^\lambda_{Ui})|w_\lambda,\bar X_i]\tag{A27}$$
and taking expectations gives (A28), from which (13) follows immediately (p. 407).

> Intuition note: after the algebra, informed and uninformed utilities differ by a single constant factor: the cost penalty $e^{ac}$ times the square root of how much information the informed have beyond the price.

**Skip path:** carry forward (13)–(15) and (19b).

## Toy example (ours, not from the text)
Take $a=1$, $\sigma_\theta^2=5$, $\sigma_\epsilon^2=1$ (so $n=5$), and choose $c$ so that $e^{2ac}=2$. Let supply variance be $\sigma_x^2=0.8$.
- (19a): $m=(2-1)/(1+5-2)=1/4$.
- (17), (19b): $\rho_\theta^2=1/(1+0.25)=0.8$, and $1-\rho_\theta^2=(2-1)/5=0.2$. ✓
- (16a) solved for $\lambda$: $m=\sigma_x^2/(5\lambda^2)=0.8/(5\lambda^2)=1/4$ gives $\lambda^2=0.64$, so $\lambda=0.8$.
- Check $\gamma(\lambda)=1$: by (18), $(1+m)/(1+m+nm)=1.25/(1.25+1.25)=0.5$, so $\gamma^2=2\times0.5=1$ ✓.
- Check interior: $\gamma(0)=e^{ac}/\sqrt{1+n}=\sqrt2/\sqrt6<1$. At $\lambda=1$: $m=0.8/5=0.16$ and $\gamma(1)^2=2(1.16)/(1.16+0.8)=1.18>1$ ✓.
- Cut noise to $\sigma_x^2=0.2$: $m$ must stay $1/4$, so $\lambda^2=4(0.2)/5=0.16$, $\lambda=0.4$. Informativeness $\rho_\theta^2=0.8$ is unchanged; only $\lambda$ halved (Theorem 4 B–C).
- Limit $\sigma_x^2\to0$: $\lambda\to0$, but at $\sigma_x^2=0$ exactly $e^{ac}=\sqrt2<\sqrt{1+n}=\sqrt6$, so by Theorem 5(a) no equilibrium exists.

## Concepts
- [[grossman-stiglitz-paradox]] — fully informative prices would remove the incentive to acquire information, so no equilibrium exists (pp. 393, 401)
- [[efficient-market-hypothesis]] — author: "prices fully reflect all available information" (Fama) is, with costly information, inconsistent with competitive equilibrium (p. 404)
- [[rational-expectations]] — uninformed traders know the joint distribution of price and return and use it (p. 394)
- [[price-as-signal]] — the price transmits informed traders' information to the uninformed, but only partially (p. 393)
- [[noise-traders]] — canon concept; here the noise is random per capita asset supply $x$, not irrational traders (p. 396)
- [[asymmetric-information]] — informed observe $\theta$; uninformed see only price (p. 393)
- [[equilibrium]] — overall equilibrium = equal expected utility of informed and uninformed (p. 398)
- [[equilibrium-degree-of-disequilibrium]] (new) — price only partially reflects information so informed are compensated; $\lambda$ is endogenous (p. 393)
- [[price-informativeness]] (new) — $\rho_\theta^2=1/(1+m)$, squared correlation of price with $\theta$ (p. 399)
- [[thin-markets-from-homogeneous-beliefs]] (new) — trade goes to zero when $\lambda\to0$ or $1$ because beliefs are nearly identical (p. 403)
- [[cara-normal-model]] (new) — exponential utility with normal returns, giving demand (8) and closed-form equilibrium (pp. 395–396)

## Canonical instances
- [[cara-normal-noisy-rational-expectations-model]] — the paper's worked example in which conjectures 1–7 can be checked (pp. 395–400)
- [[arrow-security-example]] — the extra security $z$ whose price reveals $\theta$ and destroys equilibrium (p. 404)
- [[storable-commodity-futures-market]] — Grossman's (1977) example, summarised in a parenthesis, where a futures market reveals information and removes noise (p. 404)

## Bridges (candidates)
- [same-math] CARA-normal demand $X=(E[u]-RP)/(a\,Var[u])$ ↔ economics-finance: mean-variance optimization — expected utility is a mean-variance expression with risk-aversion weight $a$ (the paper does not itself name mean-variance).
- [structural-analogy] Price as noisy signal of informed traders' information ↔ Hayek's dispersed knowledge (cited p. 404) — prices carry local knowledge to others.
- [structural-analogy] Equal-payoff condition fixing $\lambda$ ↔ equilibrium mix in a game — the share informed adjusts until the two options pay the same.
- [metaphor] Thin market with homogeneous beliefs ↔ social value of public information — an informative price removes the disagreement that trade needs.

## Questions this raises
- Does the "exact offset" of noise by $\lambda$ survive without CARA utility and normality? The authors prove none of the conjectures in general (p. 395).
- Is the equilibrium degree of informativeness socially optimal? The authors defer welfare analysis (p. 405).
- What happens if traders differ in risk aversion or endowments are informative about $x$? Both are set aside (p. 402, fn. 9).
- How should empirical tests of efficiency change if prices are only partially informative by design?

## Reading notes
- Printed page = pdf page + 392 (pdf 1 = p. 393).
- The text layer is garbled in many equations. I used the page images for (1)–(24) and the appendix. Eq. (22) on p. 402 is hard to read even in the image; I give the net-trade expression from footnote 10 and the mean/variance (23)–(24), not (22).
- The symbol $h$ appears on p. 402 (footnote 10, $ah$) and in (A18) on p. 406 (including a line "$h_0\equiv\ldots\equiv h$"). In (A18) the image reads $h_\lambda\equiv Var(E[u^*|\theta]|w_\lambda)=Var(\theta|w_\lambda)$, $h_0\equiv\sigma_\epsilon^2\equiv h$, so there $h$ is printed as $\sigma_\epsilon^2$ (as printed). On p. 402 $h$ appears to stand for $\sigma_\epsilon^2$ as well, since $X_I=(\theta-RP)/(a\sigma_\epsilon^2)$.
- Theorem 6 as printed has parts (a) and (b); the proof also contains part (c), on $\sigma_x^2\to0$.
- Footnote 8 reuses $\gamma$ for $e^{2ac}-1$, different from $\gamma(\lambda)$ in (14).
- Possible slip (my own check): the exponent in (12a) and (A17) is $-aR(W_{0i}-c)$, which gives a factor $e^{aRc}$, whereas (A20) and (13) print $e^{ac}$. This is consistent only if $R=1$ or $c$ is measured in end-of-period dollars. I follow the paper's $e^{ac}$.
- Theorem 4 B is printed as "if $\sigma_x^2$ changes, or if $\sigma_u^2$ changes with $n$ fixed". Text-layer symbols for the sigmas are unreliable, so I read these from the images.
- References include Fama (1970), Hayek (1945), Green (1973, 1977), Grossman (1975–78), Kihlstrom–Mirman, Lucas (1972), Stiglitz (1971, 1974), as printed on pp. 407–408.
