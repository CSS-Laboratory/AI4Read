---
id: markowitz-1952-portfolio/main
work: markowitz-1952-portfolio
unit: paper
pages: 77–91
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Portfolio Selection (Markowitz, 1952)

## L0 — One line
The paper proposes that investors choose portfolios from the "efficient" set (least variance of return for a given expected return or more, and most expected return for a given variance or less), because the expected-return rule never implies that a diversified portfolio is better than all non-diversified ones.

## L1 — The gist (≤ 120 words)
Choosing a portfolio has two stages: forming beliefs about securities, then choosing weights. The paper treats only the second. Maximising (discounted) expected return is rejected, because it puts everything into one security, yet diversification is observed and sensible. The paper proposes an expected return–variance (E–V) rule. Security returns are too intercorrelated for diversification to remove all variance, and portfolio variance depends on covariances (how returns move together). The paper shows geometrically, for 3 and 4 securities, how the efficient portfolios form connected line segments. It argues that E–V implies diversification across dissimilar industries, and suggests uses in theory and in practice.

**Prerequisites:** expected value, variance, correlation; linear equations in two variables; the equation of a line and an ellipse.

## L2 — Key ideas (5–10 bullets)
- Maximising discounted expected return puts all funds in the security with the greatest discounted value (if several tie, any mix of them is as good), so it never ranks a diversified portfolio above all non-diversified ones (ignoring market imperfections). Hence it is rejected (pp. 77–78).
- "Diversify across all maximum-expected-return securities" fails because the law of large numbers does not apply: returns are too intercorrelated (p. 79).
- Portfolio variance depends on covariances: $V=\sum_i\sum_j\sigma_{ij}X_iX_j$ (pp. 80–83).
- The E–V rule selects efficient portfolios: minimum variance $V$ for a given expected return $E$ or more, maximum $E$ for a given $V$ or less (p. 82).
- With 3 securities, isomean lines (equal $E$) are typically parallel lines and isovariance lines (equal $V$) are typically concentric ellipses. The efficient set is built from the critical line (the line of minimum-$V$ portfolios for each $E$) and the boundary of the attainable set (pp. 84–85).
- The efficient set is a chain of connected line segments for any $N$. The efficient $(E,V)$ curve is a chain of parabola segments (p. 87).
- E–V implies diversification for "the right reason": avoiding high covariances, not just holding many securities (p. 89).
- E–V suits investment better than speculation (pp. 87, 90). The third moment $M_3$ (the average cubed deviation from $E$) may be connected with a propensity to gamble: with a utility that depends on $M_3$, some fair bets would be accepted (pp. 90–91).

## L3 — Walkthrough

**Introduction (p. 77).** Portfolio selection has two stages. Stage 1: observation → beliefs about future performance. Stage 2: beliefs → portfolio choice. The paper treats only stage 2 (pp. 77, 91). Footnote 7 says the paper does not treat how investors form beliefs (p. 81).

**1. The expected-returns rule is rejected (pp. 77–79).**
- The rule: maximise discounted (capitalised) expected returns. Variants let "anticipated" returns include a risk allowance (Hicks), or let discount rates vary with risk (p. 77).
- Ignoring market imperfections, the rule never implies that a diversified portfolio beats all non-diversified ones. This holds however returns are formed or discounted, assuming returns and discount rates do not depend on the investor's portfolio (pp. 77–78, fn. 3).
- Proof. Let $r_{it}$ be the anticipated return at time $t$ per dollar in security $i$. Let $d_{it}$ be the rate at which its return is discounted back to the present, and let $X_i\ge 0$ the share invested (no short sales). Then (p. 78):
$$R=\sum_{t=1}^{\infty}\sum_{i=1}^{N}d_{it}r_{it}X_i=\sum_{i=1}^{N}X_i\Big(\sum_{t=1}^{\infty}d_{it}r_{it}\Big),\qquad R_i=\sum_{t=1}^{\infty}d_{it}r_{it}.$$
So $R=\sum X_iR_i$, with $R_i$ independent of $X_i$. Since $X_i\ge0$ and $\sum X_i=1$, $R$ is a weighted average of the $R_i$. To maximise it, set $X_i=1$ for the $i$ with maximum $R_i$. If $K$ securities tie at the maximum, any allocation with $\sum_{a=1}^{K}X_{a}=1$ over them is optimal. In no case is a diversified portfolio preferred to all non-diversified ones (p. 78).
- With short sales allowed, an infinite amount would go into the highest-$r$ security (fn. 4, p. 78).
- The static version replaces the time series by a "flow of returns" $r_i$ and gives the same result (pp. 78–79).
- A rule implying both diversification and maximum expected return: diversify among all securities with maximum expected return, relying on the law of large numbers. It is a special case of E–V: it assumes one portfolio has both maximum $E$ and minimum $V$ (p. 79).
- The author rejects this. Security returns are too intercorrelated, so diversification cannot eliminate all variance. The maximum-$E$ portfolio is not necessarily the minimum-$V$ one. There is a rate at which expected return can be traded for variance (p. 79).
- Scope limits: no analytic $n$-security derivation (only 3 and 4 securities, geometrically), and static probability beliefs (p. 79).

*Intuition note.* A weighted average is never larger than its largest term, so the expected-return rule gives no reason to split money. The E–V rule, which also looks at variance, can favour splitting.

**2. Statistics needed (pp. 79–81).**
- For a random variable $Y$ with values $y_k$ and probabilities $p_k$: $E=p_1y_1+\dots+p_Ny_N$, and $V=p_1(y_1-E)^2+\dots+p_N(y_N-E)^2$. $V$ is the average squared deviation. Also $\sigma=\sqrt V$ and the coefficient of variation is $\sigma/E$ (p. 80).
- For $R=a_1R_1+\dots+a_nR_n$, $E(R)=a_1E(R_1)+\dots+a_nE(R_n)$ (p. 80). Proofs are left to a standard text (p. 80).
- Covariance: $\sigma_{ij}=E\{[R_i-E(R_i)][R_j-E(R_j)]\}$, and $\sigma_{ij}=\rho_{ij}\sigma_i\sigma_j$ (p. 80). The variance of a weighted sum is "not as simple" (p. 80). Using $\sigma_{ii}=V(R_i)$ it can be written as a double sum, as in (2) below (pp. 80–81).
- Portfolio: $R_i$ are random, the $X_i$ are fixed by the investor, $\sum X_i=1$, and $X_i\ge0$ (p. 81). Then (p. 83, eqs. 1–4):
$$E=\sum_{i}X_i\mu_i\tag{1}$$
$$V=\sum_i\sum_jX_iX_j\sigma_{ij}\tag{2}$$
$$\sum_iX_i=1\tag{3}$$
$$X_i\ge0\tag{4}$$
- The investor is assumed to act as if he had (partly subjective, roughly consistent) probability beliefs (fn. 7, p. 81).

**3. The E–V rule (p. 82).** For fixed beliefs $(\mu_i,\sigma_{ij})$, the investor chooses among $(E,V)$ combinations. The rule: choose an efficient portfolio, i.e. minimum $V$ for given $E$ or more, and maximum $E$ for given $V$ or less (p. 82).

*Intuition note.* "Efficient" means no other attainable portfolio is at least as good on both counts and better on one. Among efficient portfolios, more return costs more variance.

Techniques exist for computing the efficient portfolios and $(E,V)$ combinations but are not presented; the paper illustrates the efficient surfaces for small $N$, and says such calculation "might possibly be of practical use" (p. 82). Practical use needs at least two conditions: the investor wants to follow E–V, and reasonable $\mu_i,\sigma_{ij}$ can be found (pp. 82–83).

**4. Three-security geometry (pp. 83–87).**
- Substituting $X_3=1-X_1-X_2$ (3′) gives (1′): $E=\mu_3+X_1(\mu_1-\mu_3)+X_2(\mu_2-\mu_3)$. Footnote 8 gives
$$V=X_1^2(\sigma_{11}-2\sigma_{13}+\sigma_{33})+X_2^2(\sigma_{22}-2\sigma_{23}+\sigma_{33})+2X_1X_2(\sigma_{12}-\sigma_{13}-\sigma_{23}+\sigma_{33})+2X_1(\sigma_{13}-\sigma_{33})+2X_2(\sigma_{23}-\sigma_{33})+\sigma_{33}.$$
- The attainable set is the triangle $abc$ defined by $X_1\ge0$, $X_2\ge0$, $1-X_1-X_2\ge0$ (pp. 83–84).
- An isomean curve is the set of portfolios with a given $E$. An isovariance line is the set with a given $V$ (p. 84).
- If $\mu_2\ne\mu_3$, (1′) becomes
$$X_2=\frac{E-\mu_3}{\mu_2-\mu_3}-\frac{\mu_1-\mu_3}{\mu_2-\mu_3}X_1.$$
The slope is $-(\mu_1-\mu_3)/(\mu_2-\mu_3)$ and the intercept is $(E_0-\mu_3)/(\mu_2-\mu_3)$. Changing $E$ changes the intercept only, so the isomean lines are parallel. If $\mu_1=\mu_2=\mu_3$, all portfolios have the same $E$ and the investor picks minimum variance (fn. 9, p. 84).
- The isovariance curves are "typically" concentric ellipses (p. 84). The author confirms this "by a somewhat less simple application of analytic geometry" and shows no steps (p. 84). Their centre $\hat X$ minimises $V$, with values $\hat E,\hat V$. Variance rises as you move outward (p. 84). Footnote 12 says that to draw the isovariance curves as ellipses it is both necessary and sufficient to assume that no two distinct portfolios have perfectly correlated returns (fn. 12, p. 89).
- **Case: $\hat X$ inside the attainable set (Fig. 4).** $\hat X$ is efficient. No portfolio with $E<\hat E$ is efficient, since $\hat X$ has higher $E$ and lower $V$ (p. 84).
- For each $E$, the minimum-$V$ portfolio $\hat X(E)$ is where the isomean line is tangent to an isovariance curve. As $E$ varies this traces the **critical line** $l$, a straight line. The author states this follows from "algebraic considerations (which we omit here)". It passes through $\hat X$, and $V$ rises moving away from $\hat X$ along it (p. 85).
- The efficient set is the critical-line segment from $\hat X$ to the boundary, then the boundary segment ($d$ to $b$) up to $b$, the point of maximum attainable $E$ (p. 85).
- **Case: $\hat X$ outside but the critical line cuts the set (Fig. 3).** The efficient line starts at the minimum-variance attainable point on the boundary. It moves toward $b$ to the critical line, along it to a boundary, then along the boundary to $b$ (p. 85).
- Other cases left to the reader: (1) $\hat X$ outside and the critical line misses the set, so some security enters no efficient portfolio; (2) two securities with equal $\mu_i$, where the efficient maximum-$E$ portfolio may be diversified; (3) only one efficient portfolio (p. 87).
- With 4 securities, and for $N$ securities, the efficient set is a series of connected line segments from minimum variance to maximum $E$ (p. 87). Footnote 10 sketches the 4-security case in a tetrahedron. It describes subspaces $S_{a_1\ldots a_k}$ with critical lines $l_{a_1\ldots a_k}$, and the efficient line turns at intersections (p. 87).
- In $(E,V)$ space, for 3 securities: $E$ is a plane and $V$ a paraboloid over the portfolio set. Over the efficient set, $E$ is connected line segments and $V$ connected parabola segments. $V$ against $E$ gives connected parabola segments, for any number of securities (p. 87).

*Intuition note.* In the 3-security case, equal-return portfolios typically lie on a straight line and equal-risk portfolios typically lie on an ellipse around the safest portfolio. The best choice for a given return is where the line just touches an ellipse.

**5. Why E–V is plausible (pp. 87–91).**
- E–V implies diversification for a wide range of $\mu_i,\sigma_{ij}$ (p. 89). This does not mean it never implies an undiversified portfolio: it is conceivable that one security has an extremely higher yield and lower variance than all others, so much so that one undiversified portfolio gives maximum $E$ and minimum $V$ (p. 89). For a large, presumably representative range of parameters, almost all efficient portfolios are diversified (p. 89).
- It implies the "right kind" of diversification. Sixty railway securities are less diversified than a mix of railroad, utility, mining and manufacturing, because firms in one industry more often do badly together. Low variance needs avoiding high covariances, not merely holding many securities (p. 89).
- "Yield" and "risk" in financial writing correspond roughly to expected return and variance. Using $\sigma$ or $\sigma/E$ instead of $V$ still leaves the choice in the efficient set (p. 89).
- Diversifying between two portfolios $P'$ and $P''$ with equal variance: $P=\lambda P'+(1-\lambda)P''$ lies on the line joining them (Fig. 7) and typically has lower variance than either. Variance is never increased, and not decreased only if the two are perfectly correlated (fn. 12, p. 89; p. 90).
- E–V fits investment better than speculation (p. 90). Footnote 13 defines the third moment $M_3=\sum p_i(r_i-E)^3$. If $U=U(E,V)$ with $\partial U/\partial E>0$ and $\partial U/\partial V<0$ (misprint noted below), the investor never accepts an actuarially fair bet. If $U=U(E,V,M_3)$ and $\partial U/\partial M_3\ne0$, some fair bets would be accepted (pp. 90–91).
- The author says "Perhaps" E–V efficiency is "reasonable as a working hypothesis and a working maxim" for institutions that like yield, dislike risk and avoid gambling (p. 91).

**6. Uses (p. 91).** In theory: effects of changed beliefs, changed tastes for $E$ versus $V$, or changed supply. The $X_i$ may be aggregates, with care about aggregation (p. 91). In practice: the author's own view is that statistics and judgment of practical men should set tentative $\mu_i,\sigma_{ij}$, then judgment adjusts them. Then compute the efficient $(E,V)$ set, let the investor choose, and find the portfolio. Past observed values are one suggestion, though better methods are believed possible. The author believes what is needed is essentially a "probabilistic" reformulation of security analysis (p. 91).

## Toy example (ours, not from the text)
Two securities: $\mu_1=0.10$, $\mu_2=0.06$; $\sigma_{11}=0.04$, $\sigma_{22}=0.01$, $\sigma_{12}=0$. Let $X$ be the share in security 1.
- Expected-return rule: $E=0.10X+0.06(1-X)$, which is largest at $X=1$ ($E=0.10$, $V=0.04$). It never diversifies.
- Variance: $V=0.04X^2+0.01(1-X)^2$, so $dV/dX=0.08X-0.02(1-X)=0.10X-0.02=0$ gives $X=0.2$ (added step).
- At $X=0.2$: $V=0.04(0.04)+0.01(0.64)=0.0016+0.0064=0.008$ and $E=0.02+0.048=0.068$.
- $X=0$ gives $E=0.06$, $V=0.01$. It is dominated by $X=0.2$ (higher $E$, lower $V$), so it is not efficient.
- $X=0.5$ gives $E=0.08$, $V=0.25(0.04)+0.25(0.01)=0.0125$. It is efficient, as any $X\in[0.2,1]$ is.
- Efficient set: $X\in[0.2,1]$, running from minimum variance to maximum $E$. It is diversified except at the endpoint $X=1$.

## Concepts
- [[mean-variance-optimization]] — choosing weights by expected return $E$ and variance $V$ (the "E–V rule") (p. 82)
- [[diversification-covariance]] — variance depends on covariances; spread across dissimilar industries (pp. 80, 89)
- [[efficient-frontier]] — the efficient set: minimum $V$ for given $E$ or more, maximum $E$ for given $V$ or less (p. 82)
- [[expected-return-rule]] (new) — maximise discounted expected return; never implies a diversified portfolio is preferable to all non-diversified ones (pp. 77–78)
- [[isomean-isovariance]] (new) — sets of portfolios with equal $E$ (typically lines) or equal $V$ (typically ellipses) in the 3-security case (p. 84)
- [[critical-line]] (new) — locus of minimum-$V$ portfolios for each $E$; a straight line in the 3-security case (p. 85)
- [[covariance]] (new) — $\sigma_{ij}=\rho_{ij}\sigma_i\sigma_j$, how two returns move together (p. 80)

## Canonical instances
- [[sixty-railway-securities]] — many holdings are not enough; industry matters (p. 89)
- [[two-dice-sum]] — sum of two dice as an example of a weighted sum of random variables (p. 80)
- [[two-investment-companies]] — buying shares of two investment companies as diversifying among portfolios (p. 89)
- [[actuarially-fair-bet]] — E–V utility refuses fair bets; adding $M_3$ can allow some (pp. 90–91)

## Bridges (candidates)
- [same-math] Portfolio variance $\sum\sum\sigma_{ij}X_iX_j$ ↔ statistics: variance of a linear combination of random variables — the same formula.
- [structural-analogy] Efficient set ↔ economics: Pareto-undominated choices — nothing is better on both criteria.
- [metaphor] E–V trade-off ↔ risk–return in CAPM discussions (canon link; not stated in this unit).

## Questions this raises
- How should reasonable $\mu_i$ and $\sigma_{ij}$ be estimated, since the author calls this "another story" (p. 91)?
- How is the efficient set computed for large $N$, since the techniques are not given (p. 82)?
- Which utility functions, beyond $U(E,V)$, justify E–V efficiency, and what role does $M_3$ play (pp. 90–91)?
- What happens when probability beliefs change over time, since the paper assumes static beliefs (p. 79)?

## Reading notes
- The page labels give printed numbers "?" for pdf 1–6 and 1–9 for pdf 7–15. The images and text layer show journal pages 77–91 (for example "78", "80", "83", "84", "90"). Page references here use printed = pdf + 76.
- The text layer for p. 81 (variance equations) was garbled and no image of that page was given. Those equations are written from the verbatim statement of (2) on p. 83.
- Figures 1–6 (pp. 82, 85, 86, 88) were not shown as page images and are described only from the text layer.
- The printed condition "$\partial U/\partial E<0$" (p. 90) is apparently a misprint for $\partial U/\partial V<0$ (the digest reads it that way because the investor is treated as disliking variance).
- Page 78 image shows "$X$" with its subscript lost in the double sum. It is read as $X_i$, matching the next line.
- Footnote 12 appears on p. 89 and covers p. 84's "isovariance" assumptions.
