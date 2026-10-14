---
id: shiller-2019-narrative/app-applying
work: shiller-2019-narrative
unit: "Appendix: Applying Epidemic Models to Economic Narratives"
pages: 289-300
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
# Appendix: Applying Epidemic Models to Economic Narratives

## L0 — One line
Shiller argues that the Kermack-McKendrick SIR epidemic model, with modifications, is a workable starting framework for how economic narratives spread, peak and fade.

## L1 — The gist (≤ 120 words)
How can economists model the spread of narratives? Shiller adapts the 1927 SIR model: people are susceptible, infective (spreading the story) or recovered (forgotten). Three equations give a hump-shaped path of infectives. The ratio c/r (contagion over recovery) determines how many people are ever reached; with c/r held fixed, a higher c gives a faster epidemic. The epidemic ends on its own, and not everyone is infected. He lists extensions (SIRS, SEIR, co-epidemics, network and broadcast contagion), cites data on investor word of mouth and Internet memes, and links information cascades to random-looking bubbles. He says serious research is still needed.

**Prerequisites:** differential equations (rates of change), exponentials and logarithms, the idea of a model "parameter".

## L2 — Key ideas (5–10 bullets)
- The SIR model splits a constant population into susceptible S, infective I and recovered R. In narratives, "recovered" means having forgotten the story (pp. 289–291).
- Three equations: $S$ falls by new infections, $I$ grows by contagion minus recovery, $R$ grows by recovery. There is no algebraic solution, only approximations (p. 290).
- From a small number of initial infectives, the infectives follow much the same hump pattern. The epidemic ends without any change in $c$ or $r$, and some people never catch it (p. 292).
- The final size $R_\infty$ depends on $c/r$, not on the levels of $c$ and $r$. Higher $c$ with $c/r$ fixed gives a faster epidemic (p. 293).
- Many variants exist: SIRS (immunity fades, so recovereds become susceptible again), SEIR (an extra "exposed" group), co-epidemics (two diseases that affect each other's spread), network models and broadcast contagion (spread by media, not only person to person). Shiller says future narrative models might well benefit from even more compartments (a compartment is a group of people in one state) (pp. 293–297).
- ARIMA models (a standard statistical tool for time series) are, Shiller says, essentially arbitrary: unlike compartmental models they lack a theoretical underpinning. He says ARIMA methods can be improved with epidemic models (p. 295).
- Evidence offered: investor word of mouth (1985 survey) and the SIRS fit to Internet memes (pp. 297–299).
- Information cascades can, in the author's view, produce bubbles or depressions from random causes. He adds that they may not be so important a problem (p. 300).

## L3 — Walkthrough

### A Theory of How Disease Spreads (pp. 289–293)
**Model.** Kermack and McKendrick (1927) proposed the compartmental, or SIR, model (a compartment is a group in one state). $S$, $I$ and $R$ are population shares with $S+I+R=100\%$. The population is constant and nobody dies (p. 289). In a thoroughly mixing population, infective growth is $c\,SI$ minus $rI$, where $c$ is the contagion parameter and $r$ the recovery rate. The number of susceptible-infective meetings is proportional to $SI$ (pp. 289–290).

$$\frac{dS}{dt}=-cSI,\qquad \frac{dI}{dt}=cSI-rI,\qquad \frac{dR}{dt}=rI \tag{A.1}$$

There is no algebraic solution, only approximations (p. 290).

Dividing the second equation by $I$ gives the growth rate of infectives: $\frac{dI/dt}{I}=cS-r$. So the contagion rate is $cS$ and $r$ is the recovery (or forgetting) rate. The epidemic grows only if spreading outpaces recovery (p. 290). The first equation says a susceptible becomes infective with each new infection. The third says an infective becomes recovered, or in narrative terms forgets the story (pp. 290–291).

**Figure A.1.** With $I_0=0.0001\%$, $c=.5$, $r=.05$, almost 100% eventually get infected (p. 291). Attention focuses on the bell-shaped infective curve. New cases follow a similar bell if $r$ is not too far below $c$. For narratives, Shiller compares counts of words and publications to this infective curve (pp. 291–292).

**Hump pattern.** From a small start, infectives rise, then fall, much the same from epidemic to epidemic. If $c$ is small there may be a long lag before the public notices (p. 292). The epidemic ends before everyone is infected, with no change in $c$ or $r$. Escapers face a safer environment as infectives recover. So after a narrative epidemic some people will say they never heard of it, and will be skeptical of its influence even if it mattered (p. 292).

**Size of the epidemic.** The reach $R_\infty$ (the limit of the share ever infected) is strictly less than 1 and is determined by $c/r$ (p. 292). From the first and third equations:

$$\frac{dS}{dR}=-\frac{c}{r}S$$

Given $I_0$, this gives $S=(1-I_0)e^{-(c/r)R}$. Since $I_\infty=0$, $1=S_\infty+R_\infty$, so

$$\frac{c}{r}=R_\infty^{-1}\log\frac{1-I_0}{1-R_\infty} \tag{A.2}$$

Shiller defines "going viral" as $R_\infty>\tfrac12$. A viral event from $I_0$ close to zero happens when $c/r>1.386$ (p. 293). (added step: with $I_0\approx0$ and $R_\infty=\tfrac12$, $c/r=2\log 2\approx1.386$.)

Multiplying both $c$ and $r$ by $a>0$ gives the same equations, solved by $S(at),I(at),R(at)$ (p. 293). Higher $c/r$ means larger $R_\infty$ whatever the levels of $c$ and $r$. Higher $c$ with $c/r$ fixed means a faster epidemic. To start from tiny beginnings with $S$ near 1, $c/r$ must exceed 1. Shiller says fast or slow epidemics reaching 5% or 95% of the population can all have hump-shaped infective patterns that, when rescaled, look something like the heavy line in Figure A.1 (p. 293).

*Intuition note:* How far a story spreads depends on the *ratio* of spreading to forgetting. With the ratio held fixed, a higher contagion rate means a faster story. The story can end without any change in $c$ or $r$: as infectives recover, there are too few new encounters to keep it growing.

### Variations on the SIR Model (pp. 293–298)
- **Variants.** SIRS lets recovereds become susceptible again. SEIR adds an "exposed" group who become infected later. Other versions add partial immunity, births, superspreaders and geography (pp. 293–294).
- **Applications.** A modified SEIR model for influenza, using intercity air-travel data, helps explain spread (Grais et al.). A stochastic SEIHFR model fitted to African Ebola data includes hospitalization and body disposal (p. 294).
- **More compartments.** Shiller suggests future narrative models may need more, e.g. the technological-unemployment narrative split by employment and infection status (p. 294).
- **Co-epidemics.** HIV and tuberculosis are coinfective. Long et al. (2008) allow infection by one to raise the chance of catching and spreading the other. Such models could represent narratives that support one another, or the interaction of a narrative with economic status (pp. 294–295).
- **ARIMA.** Box and Jenkins popularized ARIMA models (1970). Economists use them most. Shiller says their epidemic led to a slightly delayed epidemic of rational-expectations models, peaking about 1990 (per Google Ngrams). He calls ARIMA models essentially arbitrary, without the theoretical underpinning of compartmental models. He proposes combining epidemic theory with simulation and statistical techniques when $c$ and $r$ vary over time (p. 295).
- **Poor fits.** US polio from the late 19th century to 1952 fits badly. Better hygiene should have reduced it. Paradoxically, lower incidence meant fewer infants got maternal antibodies, so severe cases rose (pp. 295–296).
- **Ideas rather than diseases.** Daley and Kendall: infectives may stop spreading after meeting an infective or recovered person, since the story is no longer new. Bartholomew: stopping spreading and forgetting differ, and an old remembered idea may leave "behavioral residue" (p. 296).
- **Networks and choice.** Network economics is large, but behavioral epidemic models are few, and "narrative" does not appear in the *Oxford Handbook of the Economics of Networks*. Some models use network structure instead of random mixing, strategic choice to be infected, or rational calculation from encounters (p. 296; p. 297).
- **Media.** The core model may still apply however people connect. Applying it to narratives may require adding contagion by broadcast. Higher $c$ can represent social media steering stories to likely-interested people (p. 297). Katz and Lazarsfeld (1955) found a two-step flow: news media start change, word of mouth completes it. Zhao et al. (2013) let news media raise analogues of $c$ and $r$ (p. 297).
- **Memes.** Bauckhage finds the SIRS variant fits Google time series on Internet memes (e.g. "O RLY?") reasonably well, with a repeated hump (pp. 297–298).

### Further Reasons to Think That Economic Narratives Have Epidemics (pp. 298–299)
In Pound and Shiller's 1985 survey, respondents recalled their latest stock purchase. Agreement that it began with a systematic search over many stocks was 67% for institutions and 23% for individuals. In a separate survey of investors in rapidly rising, high price-earnings stocks it was 25% and 16%. On average, respondents talked to seven people (institutional random sample) or twenty (active individual investors) about the stock (p. 298). Shiller concludes that people are not generally systematic and are swayed by hearsay, and likely behave this way beyond investing (p. 298). Shiller also cites evidence that people tend to invest in nearby companies, and that epidemics of interest in individual stocks sometimes spread swiftly without infecting a high fraction of people; the SIR model can accommodate this if $c$ and $r$ are both high or the area is small (p. 299). Shiller says the Bitcoin narrative has a geographical distribution; Garrett said most people on Wall Street remain skeptical while Silicon Valley is "all in" (p. 299).

### Idea Epidemics and Information Cascades (pp. 299–300)
Variations of SIR/SEIR can be chaotic: deterministic systems that look random and never repeat (p. 299). Shiller says adding information cascades to the basic model can help explain butterfly effects (a big, apparently unpredictable outcome from a distant, seemingly irrelevant cause). If people treat others' choices as reliable information, the equilibrium can drift in random directions, as in the music-market experiment of chapter 4 (p. 300). In Shiller's taxi example, Ivo Welch follows an empty taxi in the hope it is heading to the hotel. Many such followers could send a flood of taxis to a random place (p. 300).

Shiller says cascades show how speculative bubbles can be rational by economic theory, and how bubbles or depressions can start from random causes among fairly sensible people. He cites Akerlof and Yellen's "near-rational". But cascades "may not be so important a problem", since in reality taxi drivers never seem to follow the leader in driving to destinations, though they may follow others on ambiguous "facts" such as the best restaurant (p. 300). He ends that the movements of taxi drivers, like other economic phenomena, can never be properly understood without some input from narrative economics, and that real progress in narrative economics is a big project for serious future research (p. 300).

## Toy example (ours)
Take $c=0.5$, $r=0.25$, $I_0\approx0$, so $c/r=2$. Setting $R_\infty=R$ in (A.2): $2=\frac1R\log\frac1{1-R}$, i.e. $R=1-e^{-2R}$. Try $R=0.797$: $e^{-1.594}\approx0.2031$, and $1-0.2031=0.7969\approx R$. So about 80% are ever infected, and about 20% never hear the story. Doubling both to $c=1$, $r=0.5$ keeps $c/r=2$: same 80%, twice as fast.

One Euler step of (A.1) from $S=0.99$, $I=0.01$, $R=0$, step size 1:
- $dS=-0.5(0.99)(0.01)=-0.00495$.
- $dI=0.00495-0.25(0.01)=0.00245$.
- $dR=0.25(0.01)=0.0025$.
- Sum: $-0.00495+0.00245+0.0025=0$, so the total stays 1.
- Growth rate of $I$: $0.00245/0.01=0.245=cS-r=0.495-0.25$. ✔

## Concepts
- [[narrative-contagion-sir]] — SIR model with narratives as infection, forgetting as recovery (pp. 289–291)
- [[compartmental-model]] (new) — population divided into states (S, I, R, E…) with flow equations (p. 289)
- [[contagion-vs-recovery-ratio]] (new) — $c/r$ determines the final share ever infected, $R_\infty$; with $c/r$ fixed, higher $c$ gives a faster epidemic (pp. 292–293)
- [[co-epidemic]] (new) — two diseases (or narratives) raising each other's spread (pp. 294–295)
- [[information-cascade]] (new) — people infer information from others' choices, so random paths can arise (p. 300)
- [[rational-expectations]] — mentioned only as a model fashion that followed ARIMA (p. 295)
- [[economic-narrative]] — the thing being modeled (p. 289)

## Canonical instances
- [[kermack-mckendrick-figure-a1]] — hump of infectives, $c=.5$, $r=.05$ (p. 291)
- [[pound-shiller-1985-survey]] — Shiller says investors start to pay attention to a stock through word of mouth (p. 298)
- [[bauckhage-memes]] — SIRS fits meme time series reasonably well (pp. 297–298)
- [[welch-taxi-cascade]] — following a taxi as a cascade (p. 300)
- [[polio-hygiene-paradox]] — epidemic poorly fitted by simple compartments (pp. 295–296)
- [[bitcoin-geography]] — Silicon Valley vs Wall Street (p. 299)

## Bridges (candidates)
- [same-math] SIR rate equations ↔ chemistry: rate equations / consecutive reactions (p. 290) — the text says similar equations appear there.
- [structural-analogy] Information cascades ↔ coordination game / multiple equilibria: random drift between self-fulfilling outcomes.
- [structural-analogy] Narrative recovery by forgetting ↔ adaptive expectations: the state fades without an outside shock.

## Questions this raises
- How can $c$, $r$ and compartment counts be estimated from word counts or publication counts?
- Does broadcast media change only $c$, or also the shape of the curve?
- When do narrative epidemics become cascades that change real economic behavior?
- Can combining ARIMA with epidemic models give better forecasts than either alone?

## Reading notes
- Printed = pdf − 23.
- Figure A.1 (p. 291): the time axis (1–87) has no units. In the image the recovered curve reaches about 92% at step 87 and the infective peak is about 70%. The text says almost 100% are eventually infected.
- Text-layer equations were garbled on pp. 292–293. The formulas above were checked against the page images.
- The 1.386 threshold is the author's. The derivation of it is marked as added.
- Footnote numbers appear in the text but the notes themselves are not in this unit.
