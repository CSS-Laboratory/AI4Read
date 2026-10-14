---
id: fama-1970-efficient/main
work: fama-1970-efficient
unit: paper
pages: 383–417
fields: [economics-finance]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 22
pipeline_version: 0.1
---
# Efficient Capital Markets: A Review of Theory and Empirical Work

## L0 — One line
A market is "efficient" if prices fully reflect available information. This becomes testable only through an expected-return ("fair game") model, and Fama concludes that the evidence he reviews supports it, with a few exceptions.

## L1 — The gist (≤ 120 words)
Fama asks whether security prices "fully reflect" available information, and how this can be tested. He argues that the idea needs a model of equilibrium expected returns. Efficiency then means that excess returns are a "fair game" with respect to the information set. Random walks and martingales are special cases. He sorts the evidence by information set: past prices (weak form), obviously public information (semi-strong form) and monopolistic information (strong form). Fama contends weak and semi-strong tests show no important evidence against efficiency. Strong-form tests document deviations only for specialists and corporate insiders. On average, mutual funds studied do not beat a risk-adjusted benchmark. The results always test efficiency jointly with an expected-return model.

**Prerequisites:** expected value, conditional expectation, covariance and correlation, simple regression, the mean–variance (Sharpe–Lintner) idea of beta, the normal distribution and the Central Limit Theorem.

## L2 — Key ideas (5–10 bullets)
- The idea that prices fully reflect information has no testable content by itself. It becomes testable when equilibrium is stated through expected returns conditional on an information set $\Phi_t$ (p. 384).
- Efficiency means that excess returns $z$ form a "fair game" with respect to $\Phi_t$. No trading system based only on $\Phi_t$ can have expected profits or returns above the equilibrium expected ones (p. 385).
- The submartingale and the random walk are special cases of the fair-game model. Independence of returns is a superfluous extra assumption, so tests of fair-game properties support the model more than tests of pure independence do (pp. 386–387).
- Tests are classified by information set: weak (past prices), semi-strong (obviously public information), strong (monopolistic access). This lets Fama pinpoint the level of information at which the hypothesis breaks down (p. 388).
- Weak-form evidence: serial correlations are tiny, filter rules lose to buy-and-hold after minimal costs, and the remaining dependence does not seem important enough, economically, to reject efficiency (pp. 393–396, 414).
- Semi-strong evidence (splits, earnings, secondary offerings, new issues, discount rate changes) shows fast adjustment to public information (pp. 405–409).
- Strong-form evidence finds exceptions only for specialists and corporate insiders. Jensen finds no evidence of mutual-fund skill against a Sharpe–Lintner benchmark, though his evidence is not precise enough to show that special information never exists (pp. 409–413, 415).
- All tests are joint tests of efficiency and an expected-return model, so progress needs better models of equilibrium expected returns (pp. 384, 414, 416).

## L3 — Walkthrough

### I. Introduction (p. 383)
The capital market's primary role is allocating ownership of the economy's capital stock. The ideal is a market where prices give accurate signals for allocation. A market in which prices always "fully reflect" available information is called efficient (p. 383). The paper reviews theory first. It then reviews empirical work in rough historical order: weak form tests (information = historical prices), semi-strong form tests (obviously public information such as earnings or splits) and strong form tests (whether some investors have monopolistic access to relevant information) (p. 383). Fama says the efficient markets model "stands up well", with a few exceptions (p. 383). He notes that the empirical work largely preceded the theory (p. 383).

### II. The theory of efficient markets

**A. Expected return or "fair game" models (pp. 384–385).** The statement that prices fully reflect information is too general to have testable implications. The price-formation process must be specified (p. 384). One option is the two-parameter Sharpe–Lintner world. Most work only assumes that market equilibrium can be stated in terms of expected returns (p. 384). Such theories differ mainly in how "risk" is defined (p. 384). Notation, with $\Phi_t$ the information assumed fully reflected at $t$ and tildes marking random variables:

$$E(\tilde p_{j,t+1}\mid\Phi_t)=[1+E(\tilde r_{j,t+1}\mid\Phi_t)]\,p_{jt}\tag{1}$$

Here $r_{j,t+1}=(p_{j,t+1}-p_{jt})/p_{jt}$, and $p_{j,t+1}$ includes reinvested intermediate cash income (p. 384). Equation (1) says that $\Phi_t$ is fully used in forming equilibrium expected returns. This is the sense in which $\Phi_t$ is "fully reflected" in $p_{jt}$ (p. 384).

Fama stresses a limit. Expected value is just one summary of a distribution, and efficiency per se does not give it special status. Test results therefore depend partly on the validity of this assumption as well as on market efficiency. But some such assumption is the "unavoidable price" of empirical content (p. 384).

The two assumptions are (i) equilibrium can be stated in expected returns and (ii) $\Phi_t$ is fully used. Together they rule out trading systems based only on $\Phi_t$ with expected profits above equilibrium (p. 385). Define

$$x_{j,t+1}=p_{j,t+1}-E(\tilde p_{j,t+1}\mid\Phi_t)\tag{2}$$
$$E(\tilde x_{j,t+1}\mid\Phi_t)=0\tag{3}$$

By definition, (3) says $\{x_{jt}\}$ is a "fair game" with respect to $\{\Phi_t\}$. Equivalently,

$$z_{j,t+1}=r_{j,t+1}-E(\tilde r_{j,t+1}\mid\Phi_t)\tag{4}$$
$$E(\tilde z_{j,t+1}\mid\Phi_t)=0\tag{5}$$

Economically, $x$ is the excess market value of the security at $t+1$ and $z$ is the return in excess of the equilibrium expected return (p. 385). A trading system $\alpha(\Phi_t)=[\alpha_1(\Phi_t),\dots,\alpha_n(\Phi_t)]$ gives the funds invested in each of $n$ securities at $t$. Its total excess market value is

$$V_{t+1}=\sum_{j=1}^{n}\alpha_j(\Phi_t)\,[r_{j,t+1}-E(\tilde r_{j,t+1}\mid\Phi_t)],$$

and by (5)

$$E(\tilde V_{t+1}\mid\Phi_t)=\sum_{j=1}^{n}\alpha_j(\Phi_t)E(\tilde z_{j,t+1}\mid\Phi_t)=0 .$$

Footnote 2 says the fair-game properties are implications of assumptions (i) and (ii). Mandelbrot [27] and Samuelson [38] first studied the role of fair-game models rigorously (p. 385).

*Intuition note:* If everything useful in $\Phi_t$ is already priced, then no rule built only on $\Phi_t$ can have expected profit above what the model's equilibrium expected returns give. Surprises relative to the model's expectation average out to zero.

**B. The submartingale model (p. 386).** Suppose that for all $t$ and $\Phi_t$

$$E(\tilde p_{j,t+1}\mid\Phi_t)\ge p_{jt},\quad\text{equivalently}\quad E(\tilde r_{j,t+1}\mid\Phi_t)\ge 0.\tag{6}$$

The price sequence is then a submartingale with respect to $\{\Phi_t\}$. If (6) holds with equality, prices follow a martingale (p. 386). Implication: "one security and cash" mechanical rules, which say when to hold the security, sell it short or hold cash, based only on $\Phi_t$, cannot have greater expected profits than buy-and-hold (p. 386). Footnote 3 stresses that the general fair-game model does not itself rule out cash beating a security. Equilibrium expected returns may be negative, as in the Sharpe–Lintner model for a security that moves opposite to the market (p. 386, fn. 3).

**C. The random walk model (pp. 386–387).** In early treatments, the statement that prices fully reflect information was assumed to imply that successive price changes (more usually, returns) are independent, and usually also identically distributed (p. 386):

$$f(r_{j,t+1}\mid\Phi_t)=f(r_{j,t+1})\tag{7}$$

with the same density $f$ for all $t$ (p. 386). Footnote 4 says the terminology is loose. Strictly, i.i.d. price changes (not returns) give a random walk, with drift if expected changes are non-zero (p. 386, fn. 4). If expected return is constant, then

$$E(\tilde r_{j,t+1}\mid\Phi_t)=E(\tilde r_{j,t+1}).\tag{8}$$

This restricts only the mean. Equation (7) says the whole distribution is independent of $\Phi_t$ (p. 387). Footnote 5 adds that the random walk does not say past information is useless, because past returns are the best source about a stationary distribution. It does say that the order of past returns is of no consequence for assessing distributions of future returns (p. 387, fn. 5).

Fama's reading: the random walk is an extension of the fair-game model that says more about the economic environment. A random walk arises when tastes and information flow combine so that return distributions repeat through time (p. 387). So tests of fair-game properties support the model more strongly than tests of the extra independence assumption. It is "perhaps equally surprising" that evidence against independence is as weak as it is (p. 387).

**D. Market conditions consistent with efficiency (pp. 387–388).** Sufficient conditions for efficiency are: (i) no transaction costs, (ii) all information costlessly available to all, (iii) agreement on what current information implies for prices (p. 387). These are sufficient but not necessary. Efficiency may hold even with large transaction costs, if transactors take account of all available information. It may also hold if "sufficient numbers" of investors have ready access to the information. Disagreement among investors implies inefficiency only if some investors consistently evaluate information better than market prices do (pp. 387–388). Transaction costs, costly information and disagreement are potential sources of inefficiency, not necessarily actual ones. Measuring their effects is the main goal of the empirical work (p. 388).

### III. The evidence (p. 388)
The efficient markets model is described as "an extreme null hypothesis" that is not expected to be literally true. The three-way classification pinpoints where it breaks down (p. 388). Fama's thesis: no important evidence against it in weak and semi-strong tests, and only limited evidence in strong form tests (p. 388).

#### A. Weak form tests

**1. Random walks and fair games: historical background (pp. 389–391).**
- The impetus for theory came from evidence in the mid-1950s and early 1960s that speculative prices behave like random walks. Rigorous fair-game theory (Samuelson 1965, Mandelbrot 1966) came later, so a body of results existed "in search of a rigorous theory" (p. 389).
- Bachelier (1900) stated the first random-walk test. His fundamental principle was that speculation is a fair game, which implies a martingale (p. 389). Footnote 6 notes the Mandelbrot–Samuelson derivation for futures: if the futures price at $t$ is the expected spot price at termination, the futures price is a martingale. Fama says (1) is a simpler formalisation (fn. 6, p. 389).
- Kendall (1953) examined weekly changes in 19 British industrial share indices and in cotton and wheat spot prices. His serial-correlation analysis suggested a wandering series (p. 390). Working had suggested the same earlier, and Roberts later underlined its implications. Fama says early rationales (Alexander, Cootner) usually implied a fair game, and that Cootner's last sentence seems to point to a fair game rather than a random walk (p. 390).
- Fama quotes his own 1965 paper (ref. [10]). The trader's practical criterion is that past price changes cannot raise expected gains above naive buy-and-hold. Fama notes that this is met by the submartingale model and "hardly requires a random walk" (p. 391).

**2. Tests in the random walk literature (pp. 391–396).**

*Serial covariances.* If $x_t$ is a fair game, its unconditional mean is zero and its serial covariance is

$$E(\tilde x_{t+\tau}\tilde x_t)=\int_{x_t}x_t\,E(\tilde x_{t+\tau}\mid x_t)f(x_t)\,dx_t=0$$

because $E(\tilde x_{t+\tau}\mid x_t)=0$ (p. 391). Footnote 9 shows this holds for any $\Phi'_t\subset\Phi_t$. Write $\Phi_t=(\Phi'_t,\Phi''_t)$ and integrate the conditional expectation over $\Phi''_t$; the inner integral is $E(\tilde x_{t+1}\mid\Phi_t)=0$ (p. 391, fn. 9). So a fair-game variable is linearly independent over time (p. 392). Footnote 10 says the converse fails: zero serial covariances do not imply a fair game. Example: $x$ takes values $\pm1$ and $x_{t+2}=\text{sign}(x_tx_{t+1})$, with uniform probabilities. All pairwise covariances are zero, but $E(\tilde x_{t+2}\mid x_{t+1},x_t)\neq0$, so $(x_{t+1},x_t)$ could support a profitable system (p. 392, fn. 10).

But the fair-game model does not imply that serial covariances of *returns* are zero. The weak-form fair-game variable is

$$z_{j,t}=r_{j,t}-E(\tilde r_{j,t}\mid r_{j,t-1},r_{j,t-2},\dots)\tag{9}$$

and the covariance between $r_{jt}$ and $r_{j,t+1}$ is

$$\int_{r_{jt}}[r_{jt}-E(\tilde r_{jt})]\,[E(\tilde r_{j,t+1}\mid r_{jt})-E(\tilde r_{j,t+1})]f(r_{jt})\,dr_{jt}$$

and (9) does not imply $E(\tilde r_{j,t+1}\mid r_{jt})=E(\tilde r_{j,t+1})$ (p. 392). Footnote 11: if the *level* of returns followed a martingale, successive returns would be correlated. The random walk literature assumes a stationary distribution and so uses deviations from the overall sample mean. This is a gross approximation, but it does not seem to affect covariance tests much for common stocks (p. 392). Footnote 12 says the reason is probably that changes in equilibrium expected returns over a day, week or month are trivial relative to other variation. Fama says this is not true for one-week Treasury bill returns (p. 392, fn. 12).

*Table 1 (from [10]; pp. 392–394).* First-order serial correlations of changes in $\log_e$ price for the 30 Dow Jones Industrials, mostly late 1957 to 26 Sept. 1962, with one-, four-, nine- and sixteen-day differencing intervals (p. 393). Findings:
- Results are typical of other covariance and spectral studies. There is no evidence of substantial linear dependence, and the measured correlations are always close to zero (p. 394).
- For daily returns, 11 of 30 coefficients exceed twice their standard error, and 22 of 30 are positive. For four- and nine-day intervals, 21 and 24 coefficients are negative (p. 394).
- With $N\approx1200$–$1700$ daily observations, the standard error is approximated as $(1/(N-1))^{1/2}$, so a correlation of .06 is "significant". But $.06^2=.0036$, so the lagged change explains only about .36% of the variation, probably economically insignificant (p. 394).
- Footnote 14: fat tails mean this standard error understates sampling dispersion. Also, a common market factor can produce a predominance of one sign in sample correlations even if all population serial correlations are zero (p. 394, fn. 14).

*Filter tests.* A $y\%$ filter works as follows. Buy and hold when the price rises at least $y\%$ from a low. Sell and go short when it falls at least $y\%$ from a subsequent high. Cover and buy when it rises $y\%$ above a subsequent low. Smaller moves are ignored. It is a one-security-and-cash rule, so it bears on the submartingale model (pp. 394–395). Alexander tested filters of 1–50% on daily index data, 1897–1959. His final paper advises practical readers who pay commissions to look elsewhere for ways to beat buy-and-hold (p. 395). Fama and Blume [13] tested filters on the Dow stocks.

Fama's reading: the failure of filters to beat buy-and-hold supports the submartingale model, even though some of Alexander's evidence goes against independence (p. 395). Very small filters (1% in Alexander; .5, 1.0, 1.5% in Fama–Blume) do outperform buy-and-hold on average, ignoring commissions. Profits per transaction are tiny, but trades are frequent (p. 395). This is consistent with slight positive dependence in very short-term price movements (p. 395). Footnote 15 adds a runs test: actual runs fall short of expected runs for 26 of 30 stocks. The average serial correlation is .026 and the runs deviation is about 3% of the expected number (p. 395, fn. 15). But floor traders pay about .1% per turnaround, and Fama–Blume show that this wipes out the small filters' advantage (p. 396). Whatever their statistical significance, the departures are economically so small that it seems hardly justified to use them to declare the market inefficient (p. 396).

**3. Other tests of independence (pp. 396–399).** Violations of pure independence are to be expected, and they can give insight into the market environment (p. 396).
- Large daily price changes tend to be followed by large changes of random sign. This denies the random walk but not efficiency. Fama speculates (as a possibility) that new information cannot always be evaluated precisely, so prices over- or under-adjust. If the following signs are random, the initial change is an unbiased adjustment, which suffices for the fair-game model (p. 396).
- **Niederhoffer and Osborne [32]** find that price reversals are two to three times as likely as continuations. Continuations are slightly more likely after a continuation than after a reversal (pp. 396–397). Their explanation is the structure of limit orders (buy limit, sell limit, market orders) held in the specialist's book. Bunching of unexecuted limit orders could produce the reversals. For the continuations, they contend that limit orders concentrate at integers, halves, quarters and odd eighths in descending order of preference (p. 397).
- Fama's view: these dependences do not imply inefficiency. The reversal tendency seems to be a direct result of limit orders, and this negative dependence in itself does not imply profitable rules. The pattern of order placement is a fact about investor behaviour (p. 398).
- But the specialist alone sees the full book, which is information about likely future prices. Niederhoffer and Osborne report that the specialist sells above his last purchase on 83% of his sales and buys below his last sale on 81% of his purchases, with 24% of market volume. Fama concludes this is strong-form inefficiency (p. 398). The economic question is whether market making could be done more economically by a non-monopolistic mechanism (pp. 398–399; fn. 22 imagines a computer system).

**4. Distributional evidence (pp. 399–400).** Fama says the weight of the evidence is such that economists would generally agree that whatever dependence exists in historical returns cannot be used for profitable prediction. For returns over a day or longer, little evidence would reject the random walk as a good first approximation (p. 399). The "last burning issue" is the distribution of price changes, which matters for choosing statistical tools and interpreting results (p. 399).
- Bachelier assumed i.i.d. transaction-to-transaction changes with finite variance. If transactions are fairly uniformly spread across time and very numerous per day, week or month, the Central Limit Theorem leads us to expect changes over those intervals to be normal (p. 399).
- Osborne, Moore and Kendall found normality plausible but saw high tails (more large observations than normal). Mandelbrot proposed dropping the finite-variance assumption, so that limiting distributions could be any member of the stable class, which includes the normal and has fatter tails otherwise (p. 399).
- Fama [10] concludes that non-normal stable distributions describe daily common-stock returns better than the normal. Blume agrees, and Roll extends this to Treasury Bills (p. 399).
- Economists were reluctant because normal-theory tools are richer (pp. 399–400). Footnote 23: Press's mixtures of normals give long tails but finite variance. Then longer-interval changes should converge to normal, and [10] saw no such convergence (p. 399, fn. 23).
- Footnote 25: Alexander's early filter tests assumed exact execution at $y\%$. With stable distributions, price jumps make this assumption bias profits upward. His later tests, which allow for discontinuities, lower filter profitability (p. 401, fn. 25).

**5. Fair-game models in the Treasury bill market (pp. 400–401).** Roll's work is the first weak-form work consciously in the fair-game tradition (p. 400). For common stocks, the expected return can safely be estimated by the sample mean. For Treasury bills this fails, so testing needs an explicit theory of how expected returns evolve (p. 400). Roll uses the pure expectations hypothesis and two market-segmentation hypotheses, one of which is liquidity preference (p. 400). The rate $r_{jt}$, observed at $t$ for a one-week loan beginning at $t+j-1$, satisfies

$$r_{jt}=E(\tilde r_{0,t+j-1}\mid\Phi_t)+L_{jt}$$

where $L_{jt}$ is a liquidity premium (positive or negative) (p. 401). In all three theories

$$E(\tilde r_{jt}\mid\Phi_{t-1})=r_{j+1,t-1}+E(L_{jt}\mid\Phi_{t-1})-L_{j+1,t-1}$$

and the theories differ only in the values given to the $L$'s. Under liquidity preference, premiums are always positive. Under pure expectations they are all zero, so $E(\tilde r_{jt}\mid\Phi_{t-1})=r_{j+1,t-1}$ (p. 401).

Roll concludes that the segmentation hypotheses fit better than pure expectations, with perhaps a slight edge for liquidity preference. He also concludes that the T-bill market is efficient as far as his tests go: with the best term-structure model, $z_{jt}$ seems serially independent. Assuming normality instead would have weakened the support (p. 401).

**6. Tests of a multiple-security expected-return model (pp. 401–404).** The evidence so far consists of single-security tests. Judging whether average returns across securities are "appropriate" needs an equilibrium theory. The only fully developed one is Sharpe–Lintner (p. 401):

$$E(\tilde r_{j,t+1}\mid\Phi_t)=r_{f,t+1}+\Big[E(\tilde r_{m,t+1}\mid\Phi_t)-r_{f,t+1}\Big]\frac{\operatorname{cov}(\tilde r_{j,t+1},\tilde r_{m,t+1}\mid\Phi_t)}{\sigma^2(\tilde r_{m,t+1}\mid\Phi_t)}\tag{11}$$

Here $r_f$ is the return on a riskless asset, $m$ is the market portfolio (all assets, value-weighted), and (14)–(16) below are a rearrangement of (11). The text says (11) was derived as a one-period model. A multiperiod justification is in [11], and an extension to stable distributions is in [12] (p. 402). The risk premium is the market price of risk $[E(\tilde r_m)-r_f]/\sigma(\tilde r_m)$, the same for all securities, times $\operatorname{cov}(\tilde r_j,\tilde r_m)/\sigma(\tilde r_m)$. This is the security's contribution to the market portfolio's standard deviation (p. 402). No published tests of this model existed yet (p. 402).

Related work: Kendall found high cross-correlation of simultaneous returns across securities. King found that about 50% of a stock's variance is explained by a market factor and at most 10% more by industry factors (p. 402). FFJR and Blume test the "market model":

$$r_{j,t+1}=\alpha_j+\beta_j r_{M,t+1}+u_{j,t+1}\tag{12}$$

with $M$ a market index. They find $\alpha_j,\beta_j$ fairly constant over long periods, $r_M$ and $\hat u_j$ close to serially independent, and $u_j$ independent of $r_M$ (p. 403). Hence

$$E(\tilde r_{j,t+1})=\alpha_j+\beta_jE(\tilde r_{M,t+1}).\tag{13}$$

Rewriting (11):

$$E(\tilde r_{j,t+1}\mid\Phi_t)=\alpha_j(\Phi_t)+\beta_j(\Phi_t)E(\tilde r_{m,t+1}\mid\Phi_t)\tag{14}$$
$$\alpha_j(\Phi_t)=r_{f,t+1}[1-\beta_j(\Phi_t)]\tag{15}$$
$$\beta_j(\Phi_t)=\frac{\operatorname{cov}(\tilde r_{j,t+1},\tilde r_{m,t+1}\mid\Phi_t)}{\sigma^2(\tilde r_{m,t+1}\mid\Phi_t)}\tag{16}$$

If the covariance and variance in (16) are the same for all $t$, then $\beta_j(\Phi_t)$ corresponds to $\beta_j$ in (12)–(13). If also $r_f$ is constant and the index $M$ approximates $m$, the "only missing link" is whether

$$\alpha_j=r_f(1-\beta_j)\tag{17}$$

(p. 403). Neither FFJR nor Blume tests this directly. Some of Blume's evidence is at least promising: his estimates of $\alpha_j$ are always close to zero, as they should be with monthly data, which is roughly consistent with (17) (p. 404). Footnote 27: Blume applies the model to wealth relatives $R=1+r$. The slope is the same, but the intercept is $\alpha'_j=1-\beta_j+\alpha_j$. His finding that $\alpha'_j+\beta_j\approx1$ for almost all securities implies $\alpha_j\approx0$ (p. 404, fn. 27).

Fama's caution: the market model is only a statistical description. It is somewhat consistent with Sharpe–Lintner, and probably with other equilibrium models. Since $r_f$ varies over time, (15) predicts non-stationary $\alpha$, but this variation is probably trivial relative to other monthly stock-return variation. So the market-model results are "somewhat consistent" with (11), and only a direct test could give strong conclusions about it (p. 404).

*Intuition note:* The market model gives a statistical recipe for "normal" returns: a stock's return is a constant plus its beta times the market return plus noise. Later event studies use this recipe to define what is abnormal.

#### B. Tests of martingale models of the semi-strong form (pp. 404–409)
Each test examines adjustment to one kind of information-generating event, so evidence accumulates piecemeal. The available evidence supports the model but covers few event types (p. 404).

**1. Splits and adjustment of prices (pp. 405–408).** A split in itself only multiplies the number of shares, so FFJR presume splits may often be associated with more fundamental information. For month 0 (the split month), relative to which all events are dated, the market-model residuals are averaged over $N$ splits:

$$\bar u_m=\frac1N\sum_{j=1}^N u_{jm},\qquad U_m=\sum_{k=-29}^{m}\bar u_k .$$

$\bar u_m$ is the average deviation of split stocks from their normal market relationship in month $m$, and $U_m$ is the cumulative deviation. Variants $\bar u^\pm_m,U^\pm_m$ cover splits followed by dividend "increases" (+) or "decreases" (−). An increase means the split share's dividend change in the following year exceeds the NYSE-wide percentage change (p. 405). The sample is all 940 NYSE splits, 1927–59, of at least five new shares for four old, with the security listed for at least 12 months before and after (p. 405). Results (Figure 1; pp. 405–408):
- For all three dividend categories, $U_m$ rises over the 29 months before the split, and average residuals are uniformly positive (p. 406). The rise cannot be attributed to the splitting process, since the time between announcement and split exceeds four months in only about 10% of cases. Fama's reading: it seems that firms tend to split in "abnormally" good times (p. 406).
- Footnote 28: this drift cannot be used for profit. For individual securities, successive residuals look independent, but most have a few abnormally large positive months. The timing differs across securities, which explains the uniformly positive average (p. 407, fn. 28).
- After the split month there is almost no movement in $U_m$ for all splits. This is striking because 71.5% (672 of 940) of splits saw greater dividend increases than the NYSE average (p. 407).
- FFJR's interpretation: a split is a signal that directors expect earnings to sustain higher dividends, and the market reads it correctly. So post-split behaviour should differ by dividend outcome (p. 407). The "increases" group drifts up only slightly. The "decreases" group rises before the split, then falls sharply after it. After a year it is back near its level five months before the split, about when reliable information about a split reaches the market (p. 407).
- For all splits together there is no net movement after the split. So, apparently, the market makes unbiased forecasts of the dividend implications, fully reflected in prices by the end of the split month (p. 408). FFJR conclude that the evidence supports the efficiency of the market with respect to the information in a split (p. 408).

*Intuition note:* The "increase" and "decrease" cases behave differently after the split month, yet all splits together show no net movement. FFJR read this as the market having made unbiased forecasts.

**2. Other studies of public announcements (pp. 408–409).**
- **Ball and Brown [4]:** 261 firms, 1946–66, annual earnings announcements. Cumulative average residuals rise through the year before the announcement for earnings "increases" and fall for "decreases". They conclude that no more than about 10–15% of the information in the announcement has not been anticipated by the announcement month (p. 408).
- **Waud [45]:** Federal Reserve discount-rate announcements, using daily S&P 500 returns. There is a statistically significant announcement effect on the first trading day but small (never exceeding .5%). If anything, the market anticipates the announcement, shown by non-random sign patterns just before it (p. 408).
- **Scholes [39]:** large secondary offerings are associated on average with a 1–2% decline in cumulative average residual returns. The decline is unrelated to issue size, so Scholes concludes it is not "selling pressure" but negative information implied by a large block being sold (pp. 408–409). The largest declines occur when the vendor is the corporation or one of its officers, with investment companies a distant second. Vendor identity is not generally known at the time, and insiders must report to the S.E.C. only within six days, by which time residuals behave randomly (p. 409). Fama's reading: this supports the semi-strong form, but also shows that insiders sometimes have information not yet public, which is strong-form evidence against the model (p. 409).
- **Scholes, new issues (preliminary):** 696 issues, 1926–66. Cumulative average residuals rise before the offering and behave randomly after it (p. 409).

All semi-strong evidence is consistent with the model. Its strength is consistency, not quantity (p. 409).

#### C. Strong form tests (pp. 409–413)
Strong form tests ask whether anyone has higher expected trading profits because of monopolistic access to information. Niederhoffer–Osborne's specialists and Scholes' corporate insiders apparently already contradict the model (pp. 409–410). Fama therefore asks how far down the investment community the deviations go. Only mutual-fund managements have been studied in depth, and he summarises Jensen's work (p. 410). These are not strictly strong-form tests, because fund outperformance could come from monopolistic information or from better evaluation of public information (p. 410).

**1. Theoretical framework (pp. 410–412).** The main problem is a norm for performance that assumes prices fully reflect information. If investors are risk averse, one must also define risk and judge each fund against a norm at its chosen risk level (p. 410). Jensen uses Sharpe–Lintner. From (14)–(16):

$$E(\tilde r_{j,t+1}\mid\Phi_t)=r_{f,t+1}[1-\beta_j(\Phi_t)]+E(\tilde r_{m,t+1}\mid\Phi_t)\,\beta_j(\Phi_t)\tag{18}$$

This is ex ante. For an ex post norm, replace the expected market return with the realised $r_{m,t+1}$ (p. 411):

$$E(\tilde r_{j,t+1}\mid\Phi_t,r_{m,t+1})=r_{f,t+1}[1-\beta_j(\Phi_t)]+r_{m,t+1}\beta_j(\Phi_t)\tag{19}$$

Footnote 31 states the assumption that $\tilde r_{j,t+1}=r_{f,t+1}[1-\beta_j]+r_{m,t+1}\beta_j+\tilde u_{j,t+1}$ with $E(\tilde u_{j,t+1}\mid r_{m,t+1})=0$ (p. 411, fn. 31). Equation (19) is a linear function of risk $\beta_j$ (Figure 2, the "market line"). A fund whose realised return and risk plot above the line (point a) did better than expected for its risk. One below the line (point b) did worse (p. 411).

The line also shows mixtures of the riskless asset and market portfolio. For a portfolio $c$ with $\alpha$ in the riskless asset,

$$r_{c,t+1}=\alpha r_{f,t+1}+(1-\alpha)r_{m,t+1},\qquad \beta_c(\Phi_t)=\frac{\operatorname{cov}((1-\alpha)\tilde r_m,\tilde r_m\mid\Phi_t)}{\sigma^2(\tilde r_m\mid\Phi_t)}=1-\alpha .$$

For $1>\alpha>0$ this gives points between $r_f$ and $m$. For $\alpha<0$ (borrowing at the lending rate) it gives the extension through $m$ (pp. 411–412). So the market line is the result of a naive strategy that an investor who thinks prices reflect all information might follow (p. 412).

**2. Empirical results (pp. 412–413).** Jensen studies 115 mutual funds over 1955–64. Return is the nominal ten-year rate with continuous compounding. Risk is estimated from one-year rates, and the S&P 500 proxies for the market portfolio (p. 412).

| Question | Funds below the market line | Average deviation of ten-year return |
|---|---|---|
| Net returns to investors | 89 of 115 | −14.6% (p. 412) |
| Ignoring loading charges | 72 of 115 | −8.9% (p. 412) |
| Also adding back all other published expenses | 58 of 115 | −2.5% (p. 413) |

The last row is not corrected for brokerage commissions. Estimating them from average portfolio turnover (1953–58) and adding them back moves the average deviation from −2.5% to .09%, which is still not indicative of special information (p. 413). On average a fund investor ends with about 15% less wealth after ten years than on the market line (p. 412).

Individual funds: above-norm returns in one subperiod are not associated with above-norm returns in other subperiods. The number of funds with large positive deviations is below what chance would give with 115 funds if managers had no talent (p. 413). Footnote 32: Scholes' data suggest investment companies may occasionally have special information (their secondaries cause the next-largest price falls after insiders). Fama adds that Jensen's evidence is also not precise enough to conclude that such information never exists. That would need exact data on unavoidable expenses (p. 413, fn. 32). **Jensen's view:** the results do not show that the strong form holds for all investors and all time. But because these analysts are very well endowed yet are apparently unable to forecast accurately enough to recover their research and transaction costs, he calls this strong evidence for the hypothesis, at least as far as the information available to these analysts is concerned (p. 413).

### IV. Summary and conclusions (pp. 413–416)
- The theory has empirical content only within a model of market equilibrium. All available empirical work assumes that equilibrium can be stated in expected returns (p. 414).
- Strong-form efficiency is an extreme model, best used as a benchmark. Weak-form tests are the most voluminous, and Fama says it seems fair to say the results are strongly in support (p. 414).
- Daily returns show consistent positive dependence of a form that can be the basis of marginally profitable rules, but systems that try to exploit it generate so many trades that even minimum floor-trader commissions would absorb the expected profits. There is little evidence against fair game over longer periods. Weekly returns show small negative serial correlations (Cootner, Moore; also in Fama's four-day returns), but runs tests do not show them, and no profitable rules emerge (pp. 414–415).
- Large changes followed by large changes of unpredictable sign, and the Niederhoffer–Osborne reversals, give insight into price formation but do not refute the fair-game model. Niederhoffer and Osborne do refute the random walk for transaction-to-transaction changes (p. 415).
- Semi-strong tests (splits, earnings, new issues, block secondaries) support efficiency. Only a few event types were studied, but they are among the more important (p. 415).
- Strong form: the only two documented groups with monopolistic access are specialists and corporate insiders. There is no evidence that deviations permeate further. "For the purposes of most investors" the model seems a good first and second approximation (p. 416).
- Contradictory evidence is sparse, but not all issues are closed. The most pressing future work is developing and testing models of market equilibrium under uncertainty, which would allow more sophisticated inter-security tests (p. 416).

## Toy example (ours, not from the text)
*Setup.* A stock has return $r_t=+4\%$ or $-4\%$ each period. The equilibrium model says the expected next return is half of today's return, $E(r_{t+1}\mid r_t)=0.5\,r_t$.

*Fair game.* After an up day the model's expected return is $+2\%$. Probabilities $p$ of $+4\%$ and $1-p$ of $-4\%$ solve $0.04p-0.04(1-p)=0.02$, so $p=0.75$. Check: $0.75(0.04)+0.25(-0.04)=0.03-0.01=0.02$. After a down day the expectation is $-2\%$ and $p=0.25$. Define $z_{t+1}=r_{t+1}-0.5\,r_t$. After an up day $z=+2\%$ with prob. .75 or $-6\%$ with prob. .25, so $E(z)=0.015-0.015=0$. After a down day $z=+6\%$ with prob. .25 or $-2\%$ with prob. .75, so $E(z)=0.015-0.015=0$. So $z$ is a fair game given $r_t$.

*No profitable rule.* Take a rule that invests \$50 after an up day and \$20 after a down day. Expected excess value is $50\times0=0$ after an up day and $20\times0=0$ after a down day. Total is 0, as (5) implies.

*Serial covariance is nonzero anyway.* Unconditionally $r_t=\pm4\%$ is symmetric (mean 0). $E[r_{t+1}r_t]=0.5(0.04)(0.02)+0.5(-0.04)(-0.02)=0.0004+0.0004=0.0008$. The variance is $0.0016$, so the serial correlation is $0.5$. A fair game can thus coexist with strongly correlated returns. This is the point made on p. 392, where the conditional expectation itself depends on the observed return.

## Concepts
- [[efficient market hypothesis (weak/semi-strong/strong)]] — prices at any time "fully reflect" an information set: past prices (weak), obviously public information (semi-strong), all information including monopolistic (strong) (pp. 383, 388)
- [[joint-hypothesis problem]] — test results depend on efficiency and on the assumed expected-return model together; the term is not used in the text (pp. 384, 400 fn. 24)
- [[fair-game-martingale]] (new) — excess return or price surprise has conditional mean zero given $\Phi_t$; the submartingale allows a non-negative expected change (pp. 385–386)
- [[random-walk-model]] (new) — successive returns are i.i.d. A fair game plus a special environment; stronger than efficiency needs (pp. 386–387)
- [[mean-variance optimization]] — in the Sharpe–Lintner model, risk is a security's contribution to the standard deviation of the market portfolio (pp. 401–402)
- [[CAPM & beta]] — Sharpe–Lintner expected return $=r_f+\beta\,[E(r_m)-r_f]$, with $\beta=\operatorname{cov}(r_j,r_m)/\sigma^2(r_m)$ (eqs. 11, 14–16, pp. 402–403)
- [[market-model-regression]] (new) — $r_{jt}=\alpha_j+\beta_jr_{Mt}+u_{jt}$; residuals measure abnormal returns (p. 403)
- [[event-study-residual-analysis]] (new) — average and cumulative average residuals around event dates test price adjustment (p. 405)
- [[filter-rule]] (new) — a mechanical $y\%$ buy/sell/short rule used to test whether past prices give profits (pp. 394–395)
- [[fat tails & volatility clustering]] — high tails in price changes, modelled by stable distributions; large changes tend to follow large changes (pp. 396, 399)
- [[stable-paretian-distribution]] (new) — a family including the normal, with fatter tails otherwise; used for returns because variance may be infinite (p. 399)
- [[market failure / externality]] — the specialist's monopoly over order-book information as a source of strong-form inefficiency (p. 398)

## Canonical instances
- [[kendall-1953-serial-correlation]] — weekly changes in British share indices and in cotton and wheat prices look like a random walk (p. 390)
- [[table-1-dow-serial-correlations]] — tiny, mixed-sign serial correlations for the 30 Dow stocks (p. 393)
- [[alexander-filter-tests]] — filters fail to beat buy-and-hold except very small ones, which are wiped out by costs (pp. 394–396)
- [[niederhoffer-osborne-specialist]] — reversals from limit orders; the specialist profits from a private book (pp. 396–398)
- [[roll-treasury-bills]] — fair-game test needs a term-structure model; the bill market appears efficient (pp. 400–401)
- [[ffjr-stock-splits]] — cumulative residuals rise before splits, then show no net drift (pp. 405–408)
- [[ball-brown-earnings]] — most earnings information is anticipated before the announcement (p. 408)
- [[scholes-secondary-offerings]] — price falls reflect information, with insider vendors showing the largest falls (pp. 408–409)
- [[jensen-mutual-funds]] — 115 funds, 1955–64, no evidence of skill after risk adjustment (pp. 412–413)

## Bridges (candidates)
- [structural-analogy] Fair-game excess return (eqs. 2–5) ↔ economics-finance (no-arbitrage & risk-neutral pricing): expected value of the surprise is zero given the information set; the underlying measure differs.
- [same-math] Market-model slope $\beta_j$ and eq. (16) ↔ CAPM: if the covariance and variance in (16) are constant over time, $\beta_j(\Phi_t)$ corresponds to the slope $\beta_j$ in (12), whose least-squares estimate is the sample covariance over the sample variance (p. 403).
- [structural-analogy] Filter rules and costs ↔ limits to arbitrage: small predictable patterns can persist if exploiting them costs more than they pay.
- [metaphor] Prices fully reflect information ↔ price as signal: prices carry information, but this paper defines it through expected returns, not through knowledge transmission.

## Questions this raises
- Since efficiency can be tested only jointly with an expected-return model, how should a rejection be interpreted: as inefficiency or as a wrong model of equilibrium returns?
- How large must a deviation be, after realistic trading costs, to count as "economically" important? Fama uses minimum costs as a yardstick, but costs differ by trader.
- Does the semi-strong evidence from a handful of event types (splits, earnings, offerings) generalise to other news?
- If the market model fits well but $\alpha_j=r_f(1-\beta_j)$ (eq. 17) is untested, what would a direct test of Sharpe–Lintner show?

## Reading notes
- Printed page = pdf page + 381 (pdf 2 = p. 383). pdf 1 is the JSTOR cover sheet and has no printed number.
- The text layer is badly garbled throughout (spaces dropped, equations broken). Page images were provided only for pdf 4, 10, 11, 12, 30 and 36 (printed 385, 391, 392, 393, 411, 417). I checked eqs. (2)–(5), (9), fn. 9–10, Table 1 and eq. (19) with Figure 2 against these images. Equations on other pages (1, 6–8, 10–18) were reconstructed from the garbled text layer. I confirmed them using the author's verbal descriptions and the algebra of (14)–(16). Check them against the original before reuse.
- The Roll liquidity-premium subscripts on p. 401 (e.g. $j+1,\,t-1$) are garbled in the text layer. I reconstructed them from the surrounding definition and the pure-expectations case.
- Footnote 27 (p. 404): the text layer prints $\alpha'_j$ in a garbled way. I gave the relation as $1-\beta_j+\alpha_j$.
- p. 413: the text layer reads ".09%o". I gave it as .09%, assuming the stray "o" is an OCR artefact.
- Reference numbers in square brackets are the paper's own list. Note that [12] (Fama's 1968 report, Risk, Return and Equilibrium) is distinct from equation (12).
- The page 391 block quote is from the author's own earlier paper, ref. [10] (The Behavior of Stock Market Prices, 1965).
- Table 1 values are not reproduced here beyond the counts Fama reports.
