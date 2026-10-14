---
id: keynes-1936-general/ch20-employment
work: keynes-1936-general
unit: "Chapter 20. The Employment Function"
pages: "not printed in source (HTML); cited by section and paragraph"
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# The Employment Function

## L0 — One line
Keynes recasts the supply curve as an "employment function" in wage-units, so that effective demand splits between output and price, and, apart from two practical qualifications, employment rises only until full employment, after which more spending raises only money values (prices, money-wages, profits) in proportion.

## L1 — The gist (≤ 120 words)
Question: how does employment respond to a change in effective demand (total spending), for one industry and for industry as a whole? Keynes inverts the aggregate supply function into an employment function measured in wage-units. He defines elasticities (percentage responses) of employment and output. He shows that the elasticities of price and output sum to one. He then argues that the pattern and timing of demand matter, that stock depletion shapes the employment path, that rentier (money-fixed income) redistribution affects the money needed, and that beyond full employment, in strict equilibrium, output stays fixed while money wages and prices rise in proportion to expenditure. This matters because it links employment, prices and the quantity theory of money.

**Prerequisites:** elasticity as a log-derivative; aggregate supply and effective demand from earlier chapters; basic calculus; the idea of a wage-unit (the unit in which spending and prices are measured here; the chapter does not define it); propensity to consume (share of income spent on consumption).

## L2 — Key ideas (5–10 bullets)
- The employment function is the inverse of the aggregate supply function and uses only wage-units, which Keynes regards as having no doubtful quantitative character (§ I, paras. 1–2).
- Assuming the propensity to consume is given, it is reasonable to assume that each level of aggregate demand has a unique distribution across industries, so industry employment functions add up (§ I, paras. 4–5).
- The elasticity of output $e_o$ determines, if price equals marginal prime cost, how extra demand divides between expected profit and marginal prime cost (§ I, para. 7).
- Effective demand is spent partly on output and partly on price: $e'_p + e_o = 1$ (§ I, paras. 11–12).
- The money-terms equation linking the elasticities of money-prices, output and money-wages is, Keynes says, a first step to a generalised quantity theory of money (§ I, paras. 14–16).
- The assumption that employment depends solely on aggregate demand is, if more than one way of spending extra income is admitted, no better than a first approximation. Composition and timing of demand matter, as do periods of production and stocks (§ II).
- Once no surplus labour is available at the existing real wage, strict equilibrium requires further spending to raise money-wages, prices and profits in proportion, leaving output and employment unchanged, subject to two practical qualifications (§ III).
- The apparent asymmetry between inflation and deflation merely reflects that labour can refuse work at a low real wage but cannot insist on being offered work (§ IV).

## L3 — Walkthrough

### I. Definition and elasticities
**Definition.** The aggregate supply function is $Z=f(N)$ (ch. 3). The employment function is its inverse, defined in wage-units. If effective demand $D_{wr}$ (in wage-units) directed to industry $r$ calls forth employment $N_r$, then $N_r=F_r(D_{wr})$. If $D_{wr}$ is a unique function of total demand $D_w$, then $N_r=F_r(D_w)$ (§ I, para. 1).

**Why use it.** It uses only the chosen units. It also suits industry as a whole better than the ordinary supply curve (§ I, para. 2). Ordinary demand curves depend on assumed incomes and supply curves on assumed aggregate output. Studying how industries respond to aggregate employment would therefore need two families of curves (§ I, para. 3).

**Additivity.** Assume the propensity to consume is given and employment changes with investment. Then each level of effective demand matches a given aggregate employment, a given split between consumption and investment, and a given income distribution. It is reasonable to assume a unique distribution of demand across industries. The functions are then additive (§ I, paras. 4–5):
$$F_r(D_w)=N=\sum N_r=\sum F_r(D_w).$$

**Elasticities** (§ I, paras. 6–7):
$$e_{er}=\frac{dN_r}{dD_{wr}}\cdot\frac{D_{wr}}{N_r},\qquad e_e=\frac{dN}{dD_w}\cdot\frac{D_w}{N},\qquad e_{or}=\frac{dO_r}{dD_{wr}}\cdot\frac{D_{wr}}{O_r}.$$
The source prints $N_r$ in the denominator of $e_e$, probably a misprint for $N$. The output elasticity needs a satisfactory measure of output.

If price equals marginal prime cost, with $P_r$ the expected profit (§ I, para. 7):
$$\Delta D_{wr}=\frac{1}{1-e_{or}}\,\Delta P_r .$$
If $e_{or}=0$, all extra demand is expected to become profit. If $e_{or}=1$, none does: it is all absorbed by marginal prime cost. If output is $f(N_r)$ and $p_{wr}$ is the expected price in wage-units (§ I, para. 8):
$$\frac{1-e_{or}}{e_{er}}=-\frac{N_r f''(N_r)}{p_{wr}\{f'(N_r)\}^2}.$$
So $e_{or}=1$ means $f''(N_r)=0$, i.e. constant returns to employment.

*Intuition note.* $e_o$ measures how readily output (rather than price or profit) responds when more wage-unit spending arrives. If price equals marginal prime cost and output cannot respond ($e_o=0$), all the extra spending is expected to become profit.

**Classical theory, as Keynes reports it** (§ I, para. 9). Insofar as classical theory assumes that real wages always equal the marginal disutility of labour, and that this rises with employment, it assumes that in practice it is impossible to increase expenditure in wage-units. Keynes says that if this were true, the concept of elasticity of employment would have no application. Employment also could not be raised by money expenditure, since money-wages would rise in proportion. If the assumption fails, money spending can raise employment until real wages equal the marginal disutility of labour. At that point there is full employment, by definition. Ordinarily $e_{or}$ lies between 0 and 1. How far prices rise (real wages fall) therefore depends on $e_{or}$ (§ I, para. 10).

**Price and output.** Let $e'_{pr}=\frac{dp_{wr}}{dD_{wr}}\cdot\frac{D_{wr}}{p_{wr}}$. Since $O_r\,p_{wr}=D_{wr}$ (§ I, para. 11):
$$\frac{dO_r}{dD_{wr}}\cdot\frac{D_{wr}}{O_r}+\frac{dp_{wr}}{dD_{wr}}\cdot\frac{D_{wr}}{p_{wr}}=1,\quad\text{i.e. } e'_{pr}+e_{or}=1.$$
*(added step: differentiate $O_rp_{wr}=D_{wr}$ to get $p\,dO/dD+O\,dp/dD=1$; multiply by $D/(Op)=1$.)* Effective demand "spends itself" partly on output and partly on price (§ I, para. 12). The same holds for industry as a whole, $e'_p+e_o=1$, if output as a whole can be measured (§ I, para. 13).

**In money terms** (§ I, para. 14). Let $W$ be the money-wage and $p$ the expected money price. Let $e_p=\frac{D\,dp}{p\,dD}$ and $e_w=\frac{D\,dW}{W\,dD}$. The text layer prints "$e_p=1=e_o(1-e_w)$", which is garbled. The following sentence implies $e_p=1$ when $e_o=0$ or $e_w=1$, which is consistent with $e_p=1-e_o(1-e_w)$ (our reconstruction). If $e_o=0$ or $e_w=1$, output is unchanged and prices rise in the same proportion as money demand. Otherwise they rise less (§ I, para. 16). Keynes calls this the first step to a generalised quantity theory of money (next chapter) (§ I, para. 15).

*Intuition note.* Spending's growth must show up either as more output or as higher prices. The split depends on how elastic output is and how money-wages move.

### II. Composition and timing of demand
Aggregate expenditure changes will not, in general, spread proportionally across industries, for two reasons. As incomes rise, buyers will not raise purchases of every product in the same proportion. Prices also respond differently (§ II, para. 1). The assumption used so far, that changes in employment depend solely on changes in aggregate demand in wage-units, is therefore "no better than a first approximation", if we admit more than one way in which an increase of income can be spent (§ II, para. 2). More demand for high-elasticity products raises employment more. A shift of demand toward low-elasticity products can reduce employment with no change in aggregate demand (§§ II, paras. 2–3).

This matters most for unforeseen short-period changes. Products that take time to make show low elasticity of employment if demand arrives without notice, though with enough notice it may approach one (§ II, para. 4). Keynes finds the main significance of the *period of production* here. A product has period of production $n$ if $n$ time-units of notice are needed for it to offer maximum elasticity of employment (§ II, para. 5). Keynes says consumption goods taken together "obviously" have the longest period in this sense, being the last stage of every productive process. If the first impulse comes from consumption, initial employment elasticity is further below its equilibrium level than if it comes from investment. If demand goes to low-elasticity products, a larger share of it goes to entrepreneurs' incomes, with the possible result of somewhat less favourable repercussions on expenditure, since entrepreneurs are likely to save more of extra income than wage-earners. Keynes warns that the distinction between the consumption-led and investment-led cases must not be over-stated, since much of the reaction is the same in both (§ II, para. 5).

Even with long notice, the initial elasticity from an investment increase cannot equal its equilibrium value unless there are surplus stocks and capacity at every stage (§ II, para. 6). Depletion of stocks offsets the rise in investment. If surpluses exist initially, the elasticity may start near unity. It falls once stocks are absorbed but before earlier stages supply enough, then rises again toward unity. This is qualified by rent factors absorbing more expenditure or by a rising rate of interest. Hence perfect price stability is impossible in a changing economy, unless some peculiar mechanism produces just the right fluctuations in the propensity to consume. Such price movements give a windfall to entrepreneurs who happen to hold products at an advanced stage. An entrepreneur who lacks specialised resources of the right kind cannot do anything to attract it, so such price instability does not give the kind of profit stimulus liable to bring excess capacity. Keynes thinks this has been overlooked in some discussions of price-stabilising policy (§ II, para. 6). Such a price-stabilising policy cannot be perfectly successful in a changing society, but it does not follow that every small temporary departure from stability sets up cumulative disequilibrium (§ II, para. 7).

### III. Beyond full employment
When demand is deficient, unemployed men would work for less than the existing real wage. As demand rises, employment rises at a real wage equal to or below the existing one, until no more labour is available unless money-wages rise faster than prices (§ III, para. 1). Until then, diminishing returns to labour were offset by labour accepting a falling real wage. Afterwards, extra labour would need more product as inducement but yield less. Strict equilibrium then requires wages, prices and profits to rise in the same proportion as expenditure. Output and employment stay unchanged. The crude quantity theory (with income-velocity) is then fully satisfied: prices rise in exact proportion to $MV$ (§ III, para. 2).

*Intuition note.* Past the full-employment point, strict equilibrium requires that more spending buys no more output. It only raises the money amounts attached to the same output.

Two practical qualifications (§ III, para. 3):
1. For a time at least, rising prices may mislead entrepreneurs into employing beyond the profit-maximising level, by underestimating marginal user cost.
2. Rentier income is fixed in money, so rising prices shift income from rentiers to entrepreneurs. This process will have been making steady progress all the time that expenditure was increasing, not beginning only at full employment. If the rentier is less prone to spend than the entrepreneur (first hypothesis), full employment is reached with a smaller increase in money and a smaller fall in the interest rate than under the opposite hypothesis. After full employment, if the first hypothesis continues to hold, the interest rate must rise somewhat to stop prices rising indefinitely, and money grows less than in proportion to expenditure. Under the second hypothesis the opposite holds. A change-over from first to second may occur, before or after full employment.

### IV. The inflation–deflation asymmetry
Deflation below the full-employment level reduces employment and prices. Inflation above it affects only prices. Keynes says this reflects that labour can refuse work at a real wage below the marginal disutility of that employment. It cannot insist on being offered work at a real wage not above that disutility (§ IV, para. 1).

## Toy example (ours)
Let $O=D^{0.75}$ and $p=D^{0.25}$, so $Op=D$.
- Take $D=16$: $O=16^{0.75}=8$ and $p=16^{0.25}=2$. Check: $8\times2=16$.
- Elasticity of output: $\frac{dO}{dD}\cdot\frac{D}{O}=0.75D^{-0.25}\cdot\frac{D}{D^{0.75}}=0.75$.
- Elasticity of price: $0.25D^{-0.75}\cdot\frac{D}{D^{0.25}}=0.25$. Sum: $0.75+0.25=1$.
- Check with a numeric step: $D=81$ gives $O=27$, $p=3$, and $27\times3=81$. Demand rose about 5-fold ($81/16=5.0625$). Output rose 3.375-fold ($27/8$), and price rose 1.5-fold ($3/2$). Their product is $5.0625$, which equals $81/16$.
- Under Keynes's price = marginal prime cost condition, $\Delta D=\Delta P/(1-0.75)=4\,\Delta P$: a quarter of extra demand would be expected profit.

## Concepts
- [[employment-function]] (new) — inverse of aggregate supply function in wage-units: employment $N_r=F_r(D_w)$ (§ I, para. 1)
- [[effective-demand]] (new) — expected spending directed to output, measured in wage-units or money (§ I, para. 1)
- [[wage-unit]] (new) — unit in which demand is measured, chosen to avoid units of dubious quantitative character; not defined in this chapter (§ I, para. 2)
- [[elasticity-of-employment]] (new) — % response of employment to % change in wage-unit demand (§ I, para. 6)
- [[elasticity-of-output]] (new) — same for output; if price equals marginal prime cost, determines the profit share of extra demand (§ I, para. 7)
- [[period-of-production]] (new) — notice needed for a product to reach maximum employment elasticity (§ II, para. 5)
- [[quantity-theory-of-money]] (new) — beyond full employment, in strict equilibrium, the crude quantity theory holds: prices rise in proportion to $MV$ (§ III, para. 2)
- [[rentier-entrepreneur-redistribution]] (new) — rising prices shift income from money-fixed rentiers to entrepreneurs (§ III, para. 3)

## Canonical instances
- [[price-output-split]] (new) — $e'_p+e_o=1$: demand divides between price and output (§ I, para. 12)
- [[inflation-deflation-asymmetry]] (new) — deflation below full employment reduces employment and prices; inflation above it merely affects prices (§ IV, para. 1)

## Bridges (candidates)
- [same-math] $e'_p+e_o=1$ ↔ macroeconomics: nominal output = price × real output, in growth-rate form — it is a log-derivative identity.
- [structural-analogy] Period of production and low initial elasticity ↔ supply-side lags and bottlenecks: output cannot respond instantly to unforeseen demand.
- [structural-analogy] Labour can refuse low wages but cannot insist on work ↔ downward rigidity and one-sided constraints in markets.

## Questions this raises
- How exactly does the equation for $e_p$ in money terms lead to the generalised quantity theory promised for the next chapter?
- How reliable is the assumption of a unique distribution of demand among industries, given Section II's own caveats?
- Which of the two rentier hypotheses is likelier in practice, and how would it change the money required for full employment?
- How would one measure aggregate output so that $e_o$ becomes usable?

## Reading notes
- The source is HTML with no page numbers. Citations use section numeral and my own paragraph count within each section (as the text appears).
- The metadata says "Chapter 12, 'The State of Long-Term Expectation'". That does not match this unit (Chapter 20). The unit text is the employment function.
- Equations are garbled in the text layer (fractions, Greek letters, "ee", "eo"). The $e_e$ denominator reads $N_r$, probably a misprint for $N$. The money-terms equation "ep = 1 = eo(1−ew)" is garbled and has been reconstructed (flagged above). No images were available.
- Typos in source: "spends itsell", "ormer" (former).
- Section III's "first hypothesis" means: the rentier is less prone to spend than the entrepreneur.
