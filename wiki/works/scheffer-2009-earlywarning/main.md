---
id: scheffer-2009-earlywarning/main
work: scheffer-2009-earlywarning
unit: paper
pages: 53-59
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Early-warning signals for critical transitions

## L0 — One line
Systems approaching many kinds of tipping points recover more slowly from small shocks, and this slowing can show up in data as rising autocorrelation, rising variance and related signals, largely regardless of the system's details.

## L1 — The gist (≤ 120 words)
Sudden shifts (asthma attacks, market crashes, climate jumps, ecosystem collapses) are hard to predict, because models are usually not accurate enough and the state may change little beforehand. The review asks whether generic warning signs exist. Theory says that near a fold bifurcation the system recovers ever more slowly (critical slowing down). In noisy data this can appear as higher lag-1 autocorrelation (similarity of consecutive values) and variance. Skewness, flickering and spatial patterns can also warn. Early evidence comes from climate records, ecosystems, epilepsy and finance. Most signals are relative, can give false positives and negatives, and leave the exact date hard to predict. They may still help judge whether the risk of a transition is rising when one is suspected.

**Prerequisites:** equilibrium and stability of a differential equation; first-order Taylor expansion; mean, variance, autocorrelation; the idea of a bifurcation.

## L2 — Key ideas (5–10 bullets)
- Tipping points correspond, in models, to bifurcations. At catastrophic bifurcations such as the fold (an equilibrium curve folded backwards), once a threshold is exceeded a positive feedback drives the system to a contrasting state, and near the fold points a tiny change can cause a large shift (p. 53, p. 54).
- At a fold bifurcation the dominant eigenvalue (the number that sets the recovery rate near equilibrium) becomes zero, so recovery from small perturbations slows. The authors say this can be proven for any continuous model approaching a fold, and that in models it typically starts far from the threshold (p. 53).
- In a system that is constantly perturbed, slowing is expected to show up as higher autocorrelation and, in models, usually higher variance. Box 3 illustrates this with an AR(1) process (each value is a fraction of the previous one plus random noise) (pp. 53–55).
- Other possible signals are rising skewness (asymmetry of fluctuations), flickering (noise-driven jumps back and forth between two states) and, in spatial systems, rising spatial coherence (units becoming more correlated) and class-specific patterns. There is no "one-size-fits-all" spatial signal (pp. 54–56).
- Empirical support is emerging for climate, vegetation patterns, fish stocks, epileptic seizures and finance; for lakes the text reports experimentally shown alternative attractors, not warning signals (pp. 56–57). Empirical proof of slowing down at bifurcations has been provided by controlled experiments with lasers and neurons (p. 56).
- Signals can fail. False negatives (a transition with no detectable warning) can arise from shifts without a gradual approach, from hard statistics, or from changing noise. False positives (a signal not caused by approaching a bifurcation) may arise from chance or confounding trends (pp. 57–58).
- Most signals should be read in a relative sense, and the exact moment of a transition remains hard to predict. They are one tool among others, but their generic character gives reason for optimism (p. 58).

## L3 — Walkthrough

### Introduction (p. 53)
- Many complex systems have **tipping points**: thresholds where the system shifts abruptly from one state to another. The authors' examples are asthma attacks, epileptic seizures, market crashes, ocean circulation and climate, and shifts in rangelands and fish stocks (p. 53).
- Prediction is hard for two reasons. The state may change little before the tipping point, and models are usually not accurate enough to locate thresholds (p. 53).
- Claim: near a critical point, dynamics have generic properties regardless of system details. So sharp transitions in different systems are related (p. 53).
- In models, critical thresholds correspond to **bifurcations** (our gloss: qualitative changes in dynamics as a parameter varies; the paper does not define the word). Two classes matter (p. 53):
  - "Catastrophic" bifurcations: past the threshold, positive feedback drives the system to a contrasting state.
  - Bifurcations from a stable equilibrium to a cyclic or chaotic attractor.
- Shifts at bifurcations are called **critical transitions** (p. 53).

### Theory: critical slowing down and its symptoms (pp. 53–55)
**Box 1 (p. 54): the fold catastrophe model.**
- The equilibrium state responds to conditions (for example exploitation pressure or temperature). If the equilibrium curve folds backwards, three equilibria can exist for a given condition (p. 54).
- The middle (dashed) branch is unstable: a slight push moves the system away. It marks the border between the basins of attraction of the two stable states on the upper and lower branches (p. 54).
- Near a fold point (F1 or F2), a tiny change in conditions can cause a large shift, and a small perturbation can push the system across the basin border. So these points are tipping points (p. 54).
- Small perturbations can also cause large changes without a true bifurcation, if the system is very sensitive in some range (Box 1b). A sudden large external force can also cause a shift (Box 1a) (p. 54).
- Early-warning signals tend to arise when approaching a bifurcation like Box 1c,d, and also near a non-catastrophic threshold like Box 1b (p. 54).

**Critical slowing down.**
- The authors focus on the fold catastrophe. They say it is now considered to capture the essence of tipping-point shifts in many systems, from cell signalling to ecosystems and climate. Earlier misuse of the classical model caused controversy (p. 53).
- At a fold point the dominant eigenvalue (which gives the rate of change near equilibrium) becomes zero. So recovery from small perturbations becomes increasingly slow (Fig. 1) (p. 53).
- The authors state: "It can be proven that this phenomenon will occur in any continuous model approaching a fold bifurcation." Models show slowing typically starts far from the bifurcation, and recovery rates fall smoothly to zero (p. 53).
- Implication 1: the recovery rate after a small experimental perturbation can indicate closeness to the bifurcation. The perturbation can be too small to risk tipping the system (p. 53).
- In spatially extensive systems, models suggest small-scale probing may suffice. Example: recovery times after local perturbation grow in models of fragmented populations nearing global extinction (p. 53).

**Box 2 (p. 55): a worked example of slower recovery.** With $c>0$ a scaling factor and $a,b$ parameters:
$$\frac{dx}{dt}=c(x-a)(x-b)\tag{1}$$
- Equilibria are $x_1=a$ and $x_2=b$, one stable and one unstable. If $a=b$ they collide and exchange stability (a transcritical bifurcation) (p. 55).
- Assume $x_1$ is the stable one and perturb it: $x=x_1+\epsilon$. Then $\frac{d(x_1+\epsilon)}{dt}=f(x_1+\epsilon)$, with $f$ the right side of (1) (p. 55).
- First-order Taylor expansion: $f(x_1+\epsilon)\approx f(x_1)+\frac{\partial f}{\partial x}\Big|_{x_1}\epsilon$. This simplifies to
$$\frac{d\epsilon}{dt}=\frac{\partial f}{\partial x}\Big|_{x_1}\epsilon=\lambda_1\epsilon\tag{2}$$
- The eigenvalues are
$$\lambda_1=\frac{\partial f}{\partial x}\Big|_a=-c(b-a)\tag{3}$$
$$\lambda_2=\frac{\partial f}{\partial x}\Big|_b=c(b-a)\tag{4}$$
- If $b>a$, $\lambda_1<0$: the perturbation decays exponentially, so $x_1$ is stable. At $b=a$ both rates are zero and perturbations do not recover (p. 55).
- Here the recovery rate depends linearly on the basin size $(b-a)$. For more realistic models this is not necessarily so, but the relation is still monotonic and often nearly linear (p. 55).

*Intuition note:* Near the tipping point the "restoring pull" toward equilibrium weakens, and at the threshold it vanishes. A small push then takes much longer to die out. The slope of $f$ at the equilibrium measures this pull.

**Autocorrelation and variance (Box 3, p. 55).**
- For most natural systems it would be impractical or impossible to test recovery rates systematically by repeated perturbation. But they are constantly perturbed naturally, and then characteristic changes in the pattern of fluctuations are expected (p. 53).
- Prediction: slowing down raises autocorrelation (Fig. 1). The system's state becomes more like its past state, so its "memory" grows. This can be measured from the frequency spectrum, or most simply by lag-1 autocorrelation, which can be read as slowness of recovery (p. 53).
- Simulations with stochastic forcing confirm a marked rise in autocorrelation long before the transition, in simple models and in elaborate, relatively realistic spatial models (Fig. 2d) (pp. 53–54).
- Variance may also rise: as the eigenvalue approaches zero, shocks do not decay, and their accumulation raises the variance. In principle slowing could reduce the system's ability to track fluctuations and so lower the variance. But model analyses show a rise usually occurs well before the transition (Fig. 2) (p. 54).

Box 3 derivation (additive noise after each period $\Delta t$; return to equilibrium approximately exponential with recovery speed $\lambda$; $\sigma$ is the noise standard deviation; $\epsilon_n$ is standard normal noise; $y_n$ is the deviation from equilibrium $\tilde{x}$) (p. 55):
$$x_{n+1}-\tilde{x}=e^{\lambda\Delta t}(x_n-\tilde{x})+\sigma\epsilon_n$$
$$y_{n+1}=e^{\lambda\Delta t}y_n+\sigma\epsilon_n$$
- If $\lambda$ and $\Delta t$ do not depend on $y_n$, this is a first-order autoregressive process, AR(1): $y_{n+1}=a\,y_n+\sigma\epsilon_n$, with autocorrelation $a\equiv e^{\lambda\Delta t}$. It is zero for white noise and close to one for red (autocorrelated) noise (p. 55).
- For $y_{n+1}=c+a\,y_n+\sigma\epsilon_n$ the expectation is
$$E(y_{n+1})=E(c)+aE(y_n)+E(\sigma\epsilon_n)\;\Rightarrow\;\mu=c+a\mu+0\;\Rightarrow\;\mu=\frac{c}{1-a}$$
- For $c=0$ the mean is zero and
$$\mathrm{Var}(y_{n+1})=E(y_n^2)-\mu^2=\frac{\sigma^2}{1-a^2}$$
- Near the critical point $\lambda\to 0$, so $a\to 1$ and the variance tends to infinity (p. 55). (Added step: this needs $\lambda<0$ away from the threshold, so that $a<1$.)

*Intuition note:* If each step keeps a fraction $a$ of the last deviation, near $a=1$ almost nothing is forgotten. Random shocks pile up, so the series is smoother and swings wider. That is why variance and autocorrelation rise together.

**Fig. 1 (p. 54).** Population model: $dX/dt = X(1-X/K) - c\,\dfrac{X^2}{X^2+1}$, with $X$ density, $K=10$ carrying capacity, $c$ maximum harvest rate. For $c=1$ (high resilience) the stochastic series has s.d. 0.016 and lag correlation 0.76. For $c=2.6$ (low resilience) it has s.d. 0.091 and correlation 0.90. The basin of attraction is also smaller (p. 54).

**Fig. 2 (p. 55).** In a harvested-population model driven slowly across a bifurcation, the filtered biomass series shows rising s.d. and rising AR(1) coefficient before the transition, as predicted (p. 55).

Summary of this section: critical slowing down gives three possible signals: slower recovery, higher autocorrelation, higher variance (p. 54).

### Skewness and flickering (pp. 54–55)
- **Skewness** (asymmetry of fluctuations) may increase before a catastrophic bifurcation. The authors say this does not come from slowing down (p. 54).
- Explanation: the unstable equilibrium (the basin border) approaches the attractor from one side. Rates of change are lower near it, so the system stays longer on that side. Skewness is also expected to rise if growing perturbation amplitude drives the system toward the basin boundary (pp. 54–55).
- **Flickering**: strong enough stochastic forcing moves the system back and forth between the two basins as it enters the bistable region before the bifurcation. It is an early warning because the system may shift permanently if conditions keep changing (p. 55).
- Flickering has been shown in models of lake eutrophication and trophic cascades. In the frequency distribution of states it appears as higher variance and skewness and as bimodality (p. 55).

### Indicators in cyclic and chaotic systems (pp. 55–56)
- The principles so far assume the underlying attractor is a stable point. Transitions in cyclic and chaotic systems are less studied (pp. 55–56).
- Bifurcations between stable, cyclic and chaotic regimes: the Hopf bifurcation (stable to oscillatory) is signalled by critical slowing down. Near it, perturbations cause long transient oscillations (p. 56).
- Non-local bifurcations (basin-boundary collisions) have no analytically defined stable or unstable point properties. The authors know of no explicit work on early-warning signals for them. They suggest oscillations may become "stretched" near the basin boundary, implying higher autocorrelation (p. 56).
- Phase locking of coupled oscillators: the bifurcations are associated with critical slowing down, suggesting early-warning signals. Rising variance and flickering occur before epileptic seizures, which are associated with phase locking of neural firing (p. 56).

### Spatial patterns as early-warning signals (p. 56)
- Many systems are coupled units that tend to take the state of connected units: financial markets, peers' attitudes, species in neighbouring habitat patches. Phase transitions may occur, as in ferromagnets (p. 56).
- General pattern near a systemic transition: scale-invariant patch-size distributions, and increased spatial coherence (higher cross-correlation, or resonance among oscillating units) (p. 56).
- Exceptions: in systems governed by local disturbance (for example grazers), power-law structures present over a wide parameter range vanish near the transition (p. 56).
- In systems with self-organized regular patterns, desert-vegetation models show regular patterns that change predictably as a barren-state transition nears: maze-like to spots (Fig. 3). This can be read as an early-warning signal (p. 56).
- Conclusion: it is important to know which class of system is involved. There is no "one-size-fits-all" spatial pattern (p. 56).

### Precursors of transitions in real systems (pp. 56–57)
- Most work uses simple models. Empirical proof of critical slowing down at bifurcations comes from controlled experiments with lasers and neurons. Whether highly complex systems show the expected signals remains open. Results from elaborate climate models with spatial dynamics and chaotic elements suggest some signals may be robust. Picking them up in natural systems is clearly harder than in models (p. 56).

**Climate (p. 56, Fig. 4 p. 57).**
- Past records show occasional sharp regime shifts. Example: about 34 Myr ago the Earth went from a tropical to a colder state with glaciated Antarctica (greenhouse–icehouse transition). Glacial cycles tend to end with abrupt warming (p. 56).
- Reconstructions are uncertain. But sharp shifts and positive feedbacks have led to suggestions that these shifts are critical transitions (p. 56).
- Autocorrelation rose significantly in each of eight analysed examples of abrupt climate change (Fig. 4 shows the greenhouse–icehouse case, AR(1) rising towards the transition) (pp. 56–57).
- One study suggests flickering preceded the end of the Younger Dryas cold period: rapid cold–warm alternations in its later part, then a sharp shift to Holocene conditions (p. 56).
- It has been suggested that rising Pleistocene variability could signal a future transition to a stable state of permanent mid-latitude Northern Hemisphere glaciation. This is a suggestion, not a result (p. 56).

**Ecosystems (p. 57).**
- Alternative attractors are shown experimentally in lakes. Work on early-warning signals in ecology is "just emerging" (p. 57).
- Dry regions: recovery from the barren state may need more rain than preserving the last patches. There is good evidence that a regular spotted pattern signals nearness to catastrophic desertification. Patch-size distributions lose scale-free structure and become truncated power laws near the barren transition, as models predict (p. 57).
- Fish stocks: harvesting tends to raise fluctuations. This is most likely due to higher intrinsic growth rates (older age classes are harvested preferentially, and young fish have higher rates of change). This increases nonlinearity as populations are driven toward a stable-to-cyclic or chaotic transition (p. 57).

**Asthma attacks and epileptic seizures (p. 57, Fig. 5).**
- Asthma: lungs can show a self-organized pattern of bronchoconstriction that might precede respiratory failure, and resembles collapsing desert vegetation patterns (p. 57).
- Seizures occur when neighbouring neurons fire in synchrony. Far-ahead prediction remains very difficult. Minutes before a seizure, EEG variance may increase (Fig. 5). Reduced signal dimensionality up to 25 min before reflects growing synchrony. Hours before, mild energy bursts and small symptomless seizures resemble flickering (p. 57).

**Finance (p. 57).**
- Predictable patterns tend to be eliminated because profit can be made from them. So markets are notoriously hard to predict, though some predictability exists (p. 57).
- Yet market dynamics may contain information presaging major events. Some events are preceded by increased trade volatility (for example the put–call option spread), but a "volatility calm" can also precede an abrupt change (p. 57).
- The VIX ("fear" index) is a prominent volatility-based signal. Systematic relationships in variance and first-order autocorrelation exist, but lead–lag relationships tend to be erratic. Correlation across stock returns rises in a falling market, and options-price patterns may serve as an indicator (p. 57).

### Outlook (pp. 57–58)
- Similar signals appear in very different systems. The authors add that this generic character suggests the transitions may be related to bifurcations, where universal laws of dynamical systems govern the pattern. This is a suggestion (p. 57).
- Theory for simple models is strong. First results from elaborate models suggest similar signals in highly complex systems. More work is needed on robustness under spatial complexity, chaos and stochastic perturbations (p. 57).
- **False negatives** (a transition with no detectable warning) can arise because (pp. 57–58):
  - the shift was not preceded by a gradual approach, for example a rare extreme event pushed a system that stayed at the same distance from the bifurcation;
  - a fast, permanent change of external conditions (Box 1a) cannot be detected from early-warning signals;
  - the signal is statistically hard to pick up, for example autocorrelation may need long time series;
  - the external perturbation regime changes over time and distorts or counteracts the signals.
- **False positives** arise when an apparent signal is not due to approaching a bifurcation: by chance, or from a confounding trend in the system or in the perturbations (p. 58).
- Most indicators signal a broad class of thresholds. The same signals may occur, less pronounced, near non-catastrophic thresholds (Box 1b). This is shown for critical slowing down and "may also be true" for autocorrelation and variance (p. 58).
- Challenges (p. 58):
  - Filtering is needed to raise sensitivity and avoid false positives, but results depend on filter parameters. The authors say it would be useful to build reliable statistical procedures to test significance.
  - Signals should be read in a relative sense: autocorrelation is predicted to approach one at a fold, but measurement noise reduces correlations.
  - Perturbations often trigger a transition well before the bifurcation point, so the moment of transition remains hard to predict.
  - A key practical question is whether a signal appears early enough to act. Spatial signals may allow shorter lead times, since a spatial pattern holds more information than one point in a time series.
- Generic signals are only one tool. Where transitions repeat (lakes, rangelands, physiology) thresholds may be found empirically. Singular systems (climate, ocean circulation) allow little learning from repeated cases, and accurate threshold models are mostly lacking (p. 58).
- Final stance: because the signals largely do not depend on the mechanism, they may be a significant step toward judging whether the probability of a transition is increasing, given reasons to suspect one (p. 58).

## Toy example (ours, not from the text)
Use the Box 2 model with $c=1$, $a=0$, and perturb the stable equilibrium $x_1=a=0$ by $\epsilon_0=0.1$.
- Far from threshold, $b=2$: $\lambda_1=-c(b-a)=-2$. The perturbation decays as $0.1e^{-2t}$. Half-life $=\ln 2/2\approx0.347$.
- Near threshold, $b=0.5$: $\lambda_1=-0.5$. Half-life $=\ln 2/0.5\approx1.386$, four times longer.
- Now add noise as in Box 3, with $\Delta t=1$, $\sigma=1$, so the AR(1) coefficient is $\rho=e^{\lambda\Delta t}$:
  - $b=2$: $\rho=e^{-2}\approx0.135$, variance $=1/(1-\rho^2)=1/(1-0.0183)\approx1.019$.
  - $b=0.5$: $\rho=e^{-0.5}\approx0.607$, variance $=1/(1-0.368)\approx1.582$.
- Closer to the threshold, recovery is slower, lag-1 autocorrelation is higher (0.135 → 0.607) and variance is higher (1.02 → 1.58). Both signals rise as $b-a$ shrinks.

## Concepts
- [[tipping point]] — threshold where a system shifts abruptly to a contrasting state; in models such thresholds correspond to bifurcations (p. 53)
- [[bifurcation]] — our gloss: qualitative change of dynamics at a parameter value; fundamental shifts at bifurcations are called critical transitions (p. 53)
- [[saddle-node (fold) bifurcation]] — equilibrium curve folded backwards; the unstable middle branch marks the basin border; dominant eigenvalue becomes zero at the fold points F1, F2 (p. 53, Box 1 p. 54)
- [[critical slowing down]] — recovery from small perturbations slows as the dominant eigenvalue nears zero (p. 53)
- [[early-warning signals]] — statistical changes (autocorrelation, variance, skewness, flickering, spatial patterns) before a transition (pp. 53–56)
- [[attractor / basin of attraction]] — stable state and the set of states leading to it; the unstable equilibrium is the border (Box 1, p. 54)
- [[fixed point and stability]] — Box 2 shows stability via the sign of $\partial f/\partial x$ at equilibrium (p. 55)
- [[linear stability analysis]] — Box 2 linearizes around an equilibrium; $\lambda$ gives the recovery rate (p. 55)
- [[feedback (positive/negative)]] — positive feedback drives the system past the threshold toward a contrasting state (p. 53)
- [[synchronization]] — phase locking of coupled oscillators, linked here to seizures (p. 56)
- [[scale invariance]] — scale-invariant patch-size distributions near a systemic transition; lost in some systems (p. 56)
- [[heavy tail / power law]] — vegetation patch sizes become truncated power laws near the barren transition (p. 57)
- [[flickering]] (new) — noise-driven jumps between two basins before a permanent shift (p. 55)
- [[lag-1 autocorrelation indicator]] (new) — correlation of consecutive states; rises as recovery slows; AR(1) coefficient $a=e^{\lambda\Delta t}$ (p. 55)
- [[false positive / false negative warnings]] (new) — spurious signals, and transitions without detectable warning (pp. 57–58)

## Canonical instances
- [[harvested population model]] — $dX/dt = X(1-X/K) - cX^2/(X^2+1)$ is the model of Fig. 1 (p. 54), where higher harvest rate c gives lower resilience, larger s.d. and higher correlation; Fig. 2 (p. 55) uses a harvested-population model driven slowly across a bifurcation (ref. 77)
- [[Box 2 quadratic model]] — $dx/dt=c(x-a)(x-b)$; recovery rate $\propto(b-a)$ (p. 55)
- [[greenhouse–icehouse transition]] — AR(1) rises before the 34 Myr shift (Fig. 4, p. 57)
- [[Younger Dryas flickering]] — one study suggests rapid cold–warm alternations preceded the end of the cold period (p. 56)
- [[desert vegetation patterns]] — maze to spots before collapse to barren state (Fig. 3, p. 56)
- [[epileptic seizure EEG variance]] — EEG variance may rise minutes before onset (Fig. 5, p. 57)
- [[VIX]] — volatility "fear" index as a market warning signal (p. 57)

## Bridges (candidates)
- [same-math] AR(1) variance $\sigma^2/(1-a^2)$ with $a\to1$ ↔ time-series analysis: a unit-root process has diverging variance. Same formula; the paper uses it for the signal.
- [structural-analogy] Coupled-unit spatial systems ↔ ferromagnets: the paper says phase transitions may occur much as in ferromagnetic materials (p. 56); it gives no matching equations.
- [structural-analogy] Flickering and bimodality ↔ hysteresis and bistability: noise-induced switching inside the bistable region.
- [metaphor] Market "volatility calm" before a crash ↔ rising variance: a falling-volatility warning runs opposite to the rising-variance logic; the paper reports both without explaining why (p. 57).

## Questions this raises
- How long must a time series be, and how should it be filtered, to tell a real rise in autocorrelation from chance (pp. 57–58)?
- Can warnings arrive early enough to act, especially for singular systems like the climate (p. 58)?
- What early-warning signals exist for basin-boundary collisions, for which the authors know of no explicit work (p. 56)?
- Why do rising and falling volatility both precede market shifts (p. 57)?

## Reading notes
- Printed page numbers are visible on every page. Offset: printed = pdf + 52.
- The text layer of Boxes 2 and 3 is garbled (Greek letters and operators appear as look-alike letters or are dropped, e.g. the tilde on the equilibrium in Box 3). Equations here are reconstructed by checking them against the text and by re-deriving them; page images were available only for pdf 5–7, so Boxes 1–3 and Fig. 1–3 were not checked against images.
- Box 2 is introduced as illustrating slowing toward a catastrophic bifurcation, but its model collides equilibria in a transcritical bifurcation (p. 55).
- In Box 3, the text layer does not state the sign of $\lambda$. $a<1$ requires $\lambda<0$; this is our added step.
- Reference 76 (p. 59) gives "Theor. Ecol. 11, 450–460", the same pages as ref. 28. This looks like a printing oddity; not verified.
- The paper is a review, so the claims about empirical examples rest on cited work, not on analyses in this paper.
