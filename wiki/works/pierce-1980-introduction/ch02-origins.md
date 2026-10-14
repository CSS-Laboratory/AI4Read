---
id: pierce-1980-introduction/ch02-origins
work: pierce-1980-introduction
unit: "2 The Origins of Information Theory"
pages: 19-44
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# The Origins of Information Theory

## L0 — One line
Pierce argues that Shannon's theory of communication grew out of practical problems of telegraphy and telephony (Morse, Nyquist, Hartley), not out of statistical mechanics, although the two "entropies" are mathematically analogous.

## L1 — The gist (≤ 120 words)
Where does information theory come from? Pierce's answer: from electrical communication. Morse's code gave short symbols to common letters. Later inventors added current levels, which sped up sending but made signals more exposed to noise and distortion. Fourier analysis and the linearity of circuits supplied the maths. Nyquist related speed to the logarithm of the number of current values and to bandwidth. Hartley defined information as a logarithm of the number of possible sequences. Wiener and Kolmogoroff solved estimating a signal in noise. Shannon asked how best to encode a given kind of message for a given noisy channel. Knowing the origins can help to show what the theory's real content is.

**Prerequisites:** logarithms to base 2 (what $2^M$ means); the idea of a sine wave; what a telegraph signal is (on/off current).

## L2 — Key ideas (5–10 bullets)
- Pierce holds that communication theory evolved from electrical communication problems; its "entropy" is named by mathematical analogy with the entropy of statistical mechanics, and the two are used for different purposes (p. 21, p. 24).
- Morse's code gave short symbols to frequent letters. Pierce says modern theory shows only about 15 per cent more speed was possible, so how a message is translated into signals matters greatly (p. 25).
- More current values (directions, intensities) carry more information per symbol, but noise, intersymbol interference and power limits make fine distinctions hard (pp. 28–29).
- Fourier analysis plus linearity makes circuits analysable: a linear circuit only attenuates and delays each sine component, so each can be treated separately (pp. 31–34).
- Nyquist: speed $W = K\log m$ for $m$ current values; the number of signal elements per second is twice the bandwidth (pp. 36–39, p. 44).
- Hartley defined the information of a message as $H = n\log s$, acceptable in today's light, Pierce says, only if symbols are chosen independently and are equally likely (p. 40).
- Wiener and Kolmogoroff estimate a signal from signal-plus-noise; Shannon instead chooses how to encode messages for a noisy channel (pp. 41–42).

## L3 — Walkthrough

### Why study history (pp. 19–21)
- Pierce says history teaches at least two things (p. 19).
  1. General discoveries often come from studying man-made devices, because machines simplify and order phenomena. Examples: the steam engine and thermodynamics (Carnot), and aerodynamics, hydrodynamics and electricity, which came mainly from artifacts (pp. 19–20). Shannon's theory has its roots in telegraphy (p. 20).
  2. Understanding is won with difficulty. Newton's laws now seem simple but were once undreamed of, and Maxwell's treatise is cluttered with lesser matters, so a naive reader might search long for the novel step (p. 20). We must not credit earlier people with a conclusion just because they stated its ingredients side by side (p. 20).
- To see an idea's real content we must trace the actual course of discovery and see problems as people then saw them (pp. 20–21).

**Intuition note.** Simple machines make good teachers: telegraphy was a simple, orderly case in which the basic problems of communication showed up clearly.

### Two entropies (pp. 21–24)
- Pierce warns against concluding that communication theory grew out of statistical mechanics. One reason for that guess is Szilard's 1929 use of an information idea to resolve a physical paradox (p. 21). He calls the guess easy but misleading (p. 21).
- Communication theory's entropy was named by mathematical analogy, and it is relevant chiefly to quite different problems (p. 21).
- **Physics entropy**:
  - It depends on a gas's temperature, volume, mass and kind of gas (p. 21).
  - Slow expansion with no heat flow is reversible, and entropy stays constant while energy changes (p. 21).
  - So entropy indicates reversibility (pp. 21–22).
  - Irreversible phenomena always involve an increase of entropy (p. 22).
  - Example: a partition vanishes and gas fills the whole cylinder. Thermal energy is unchanged but entropy rises, and we can no longer get mechanical energy from the gas. Heat flowing from hot to cold is similar (p. 22).
  - So an increase of entropy means a decrease of available energy (p. 22).
  - Statistical mechanics reads entropy increase as decrease in order. When we ask what order means, we must in some way equate it with knowledge: disorder is unpredictability from lack of knowledge of molecular positions and velocities (p. 22).
  - More detailed knowledge of a system means less uncertainty and less entropy (p. 23).
- **Communication entropy**:
  - A source (writer, speaker) may produce any one of many messages (p. 23).
  - Information conveyed grows with the uncertainty about which message will be produced. One message out of a million conveys more than one out of ten (p. 23).
  - The entropy is a measure of this uncertainty, and so of the information conveyed. The more we know about what the source will produce, the less the entropy and the less the information (p. 23).
- The two ideas are quite different and each is fully useful without the other, yet both can be described in terms of uncertainty, in similar mathematics (pp. 23–24).
- Some physicists and mathematicians want to show that communication theory is very important to statistical mechanics. Pierce calls this matter still confused and confusing. The confusion is sometimes made worse when more than one meaning of "information" creeps in, e.g. its popular association with knowledge rather than with uncertainty and its resolution (p. 24).
- Pierce defers the relation to Chapter X. He says attempts to marry the two have so far been of more interest than benefit, and have not produced important new results or understanding (p. 24).

**Intuition note.** Both entropies can be described in terms of uncertainty, but physics ties entropy to how much thermal energy can still become mechanical energy, while communication theory ties it to how much information a message conveys.

### Morse and the telegraph (pp. 24–25)
- Morse began in 1832; his first system drew lines on paper and sent numbers standing for words in a code book finished in 1837 (p. 24).
- With Vail, he arrived at the dots-dashes-spaces code by 1838. Space = no current, dot = short current, dash = longer current (pp. 24–25).
- E, the most frequent English letter, gets one dot. In general, short combinations go to frequent letters and long ones to rare letters (p. 25).
- The frequencies were not counted from text. They were estimated by counting type in a printer's type box (p. 25).
- Pierce says modern theory shows another assignment could gain only about 15 per cent in speed. Lesson: it matters profoundly how a message is translated into electrical signals, and this is at the heart of communication theory (p. 25).

### Speed limits, more current values, noise (pp. 25–30)
- In 1843 Congress funded a Washington–Baltimore line. Morse's underground wire caused trouble, so he used poles (p. 25).
- Circuits that carry steady current equally well are not equally good for communication. Sent too fast, dots and dashes run together at the far end (Figs. II-1, II-2) (pp. 25–26).
- Longer elements follow the sent signal better but slow transmission. So each circuit has a limiting speed for dots and spaces. It is very slow for submarine cables and fast enough not to bother telegraphers for pole wires (p. 26).
- **Double-current telegraphy**:
  - A dash takes three times as long as a dot (p. 27).
  - Current into the wire = dot, current out of the wire = dash, no current = space (p. 27).
  - Single current offers two elements (1, 0). Double current offers three ($+1, 0, -1$) (p. 27).
- **Edison, 1874 (quadruplex)**:
  - He used two intensities and two directions of current (p. 27).
  - Changes in intensity, regardless of direction, carry one message. Changes of direction, regardless of intensity, carry another (p. 27).
  - The four values are $+3, +1, -1, -3$, and Table I gives the receiver's reading (the table body is not in the extracted text) (pp. 27–28).
  - Fig. II-3 shows two simultaneous independent messages on four values (p. 28).
- Information sent depends on the rate of symbols and on how many different symbols are available (p. 28). With four values we send two independent choices per symbol, so twice as many letters per minute as with two values (pp. 28–29).
- **Costs of many values**:
  - Intersymbol interference (overlap of neighbouring symbols) makes a two-way choice easier and surer than a four-way choice (p. 29).
  - Noise is always present, e.g. magnetic storms and minute thermal currents akin to Brownian motion (p. 29).
  - More power helps, but a large enough voltage can destroy cable insulation. It is likely that this caused the failure of the 1858 transatlantic cable (p. 29).
- Early telegraphists understood intuitively a good deal about these limits. An exact mathematical analysis was needed (p. 30).

**Intuition note.** More distinguishable signal levels means more information per symbol. But noise and smearing make it hard to tell many alternative levels apart (our gloss: packing more levels into a fixed range leaves smaller gaps between them).

### Fourier analysis (pp. 30–34)
- Mathematics came early: Thomson (1855) computed the received current for a dot on a submarine cable. After Bell's telephone (1875), Poincaré, Heaviside, Pupin and Campbell are named as prominent contributors. They extended Fourier's heat-flow work (p. 30).
- **Sine wave** (p. 31):
  - It has no beginning or end, and it is not just any wiggly curve.
  - It is fully described by three quantities: *amplitude* (maximum height), *phase* (time of the maximum), and *period* $T$ (time between maxima).
  - The *frequency* $f$ is the reciprocal of the period. If $T = 1/100$ s, then $f = 100$ cycles per second (cps) (p. 31).
- **Fourier's theorem** (as Pierce states it): any variation of a quantity with time can be accurately represented as a sum of sinusoidal variations of different amplitudes, phases and frequencies (pp. 31–32). Fig. II-5 shows a periodic curve as the sum of two sine curves (p. 32).
- This is more than a trick because of two physical facts: transmission circuits do not change with time, and they are *linear* (p. 32).
- **Linearity**:
  - If input 1 gives output 1 and input 2 gives output 2, then the sum of the inputs gives the sum of the outputs (p. 32).
  - Signals in a linear circuit act as if present independently and do not interact. This is the criterion for a linear circuit (p. 33).
  - Resistor–capacitor–inductor circuits, telegraph lines and cables are linear. Circuits that include vacuum tubes, transistors or diodes are the exceptions, though even these are sometimes substantially linear (p. 33).
  - Consequence: two telegraph signals can travel in opposite directions on one wire without interference. Linearity is not universal; trains on one track interfere (p. 33).
- **Sine waves through linear circuits**:
  - It can be shown (not here) that a sine wave in gives a sine wave of the same frequency out (p. 33).
  - Attenuation = weaker amplitude; phase shift or delay = later peak. Both depend on frequency, and some frequencies may not be transmitted at all (pp. 33–34).
  - An input made of several sine components gives an output of the same frequencies with changed relative amplitudes and delays. So the shape generally changes (p. 34).
  - A circuit with the same attenuation and delay at all frequencies is *distortionless* (p. 34). Fig. II-6: component $b$ passes unchanged, $c$ is attenuated and delayed, so the sum has a different shape (p. 34).
- Fourier analysis lets us study a linear circuit for all signals through its effect on sine waves of each frequency (p. 34).

**Intuition note.** Because circuits treat each sine wave independently, one can break a messy signal into sine waves, handle each separately, and add the results.

### Nyquist (pp. 34–39)
- Early telegraphists invented many signal shapes with claimed merits, often with poor mathematics and wrong arguments (pp. 34–35).
- Nyquist came to AT&T in 1917 after his Ph.D. at Yale, and published "Certain Factors Affecting Telegraph Speed" in 1924 (p. 35).
- **Nyquist's 1924 relation.** For symbols sent at a constant rate, the speed of transmission $W$ and the number $m$ of available current values are related by
$$W = K\log m$$
  where $K$ depends on how many successive current values are sent each second (p. 36).
- Logarithm: with base 2, $\log x$ is the number such that $2^{\log x} = x$. Taking the logarithm of both sides gives $\log 2^{\log x} = \log x$. Writing $M = \log x$ gives
$$\log 2^{M} = M \tag{p. 36}$$
  Table II lists $\log m$ for various $m$ (values not in the extracted text) (p. 36).
- **Why a logarithm** (pp. 36–38):
  - Two independent 0-or-1 choices give 4 combinations (Table III), three give 8 (Table IV), four give 16, and $M$ give $2^M$.
  - If we can specify $M$ independent 0-or-1 choices at once, we can send $M$ independent messages at once, so speed should be proportional to $M$.
  - That needs $2^M$ different symbols, and $\log 2^M = M$. So the logarithm of the number of symbols equals the number of independent 0-or-1 choices per symbol.
- **Consequences** (p. 38):
  - Going from off–on to three values ($+1, 0, -1$) raises speed by 60 per cent.
  - Four values ($+3,+1,-1,-3$) doubles it, as in Edison's quadruplex.
  - Eight values should allow "four times as fast" as two values, according to the text (see Reading notes on this number).
  - Nyquist recognised that fluctuating attenuation, noise and power limits make many values difficult.
- **Line speed** was defined by Nyquist as half the number of signal elements per second. Pierce says we will find this definition particularly appropriate, for reasons Nyquist did not give in that early paper (p. 38).
- Telephony uses frequencies above 150 cps. Nyquist showed how to shape telegraph signals to avoid audible components. He noted line speed is proportional to the band width, the width of the frequency band used (p. 38).
- He found one proposed signal contained a steady sinusoidal component of constant amplitude. It was predictable and could be supplied at the receiver, so it conveyed no intelligence. He called it *redundant* (pp. 38–39).
- **1928, "Certain Topics in Telegraph Transmission Theory"** (p. 39):
  - If $2N$ different current values per second are sent, all sinusoidal components with frequency greater than $N$ are redundant. They are not needed to deduce the succession of values sent.
  - A signal can be built with no frequencies above $N$ cps from which the sent values are easy to deduce.
  - Pierce says this paper is more quantitative and exact than the first.

**Intuition note.** Nyquist says speed grows with the log of the number of levels. It also grows with how many symbols per second the band can carry, which is twice the bandwidth.

### Hartley (pp. 39–40)
- R. V. L. Hartley published "Transmission of Information" in 1928 (p. 39).
- **Hartley's view.** The sender mentally selects symbol after symbol from a set, producing a sequence. A chance event, such as balls rolling into pockets, could generate such a sequence equally well (p. 39).
- He defined the information $H$ of the message as the logarithm of the number of possible sequences, and showed
$$H = n\log s \tag{p. 40}$$
  with $n$ the number of symbols selected and $s$ the number of different symbols in the set (p. 40).
- Pierce's caveat: this is acceptable in the light of present information theory only if successive symbols are chosen independently and each of the $s$ symbols is equally likely (p. 40).
- Hartley then treated encoding primary symbols (letters) into secondary symbols (dots, dashes, spaces). He observed that restrictions on selection (E more often than Z) should govern the lengths of the secondary symbols if messages are to go fastest. Morse knew this, but Hartley stated it in a form open to mathematical attack. He also suggested extending the ideas to continuous signals (p. 40).
- Hartley stated, in accord with Nyquist, that transmissible information is proportional to band width times time. Pierce notes this leaves open how to count the allowable current values (p. 40).

### Wartime, Wiener, Kolmogoroff, Shannon (pp. 40–43)
- After Nyquist and Hartley, communication theory appears to have had a long, quiet period. The art of building systems grew complicated in World War II, but no broad principles were laid down (pp. 40–41).
- **The radar problem.** Predict an aircraft's future position from noisy radar data. If signal and noise have different dominant frequencies, a filter can favour the signal. The question is which circuits best predict the true signal a few seconds ahead (p. 41).
  - It involves an ensemble of possible signals (possible courses) and unpredictable noise (p. 41).
  - It was solved by Kolmogoroff in Russia and independently by Wiener in the US. Wiener's wartime document was nicknamed "the yellow peril" (p. 41).
- In 1948 Wiener published *Cybernetics* and Shannon published, in two parts, a paper now regarded as the base of modern communication theory (pp. 41–42).
- Both consider any signal drawn from an ensemble. There was free interchange among workers before publication, and similar ideas appear in both, though Shannon's interpretation appears to be distinctive (p. 42).
- **Wiener's problem**:
  - The signal ensemble and the noise are not of our choosing.
  - We estimate the present or future signal value despite noise (p. 42).
- **Shannon's problem**:
  - The message ensemble (e.g. English text) and the channel (e.g. a noisy cable) are given, but we may choose how to represent messages as signals: how many current values, how many per second.
  - The problem is what signal to send to convey messages of a given type best over a given noisy circuit (p. 42).
- Efficient encoding and its consequences form the chief substance of information theory (p. 42).
- Pierce also mentions Gabor (1946), whose paper missed noise, and Tuller (1949), who in part parallels Shannon (p. 43).

**Intuition note.** Wiener asks how to clean up what arrives. Shannon asks what to send, and how to encode it, so that messages get through a noisy channel.

### Chapter summary (pp. 43–44)
- Pierce restates the chain: Morse's efficient encoding → more current values and noise → need for mathematics (Fourier) → linear circuits and sine waves (pp. 43–44).
- Nyquist showed that the number of distinct current values sent per second is twice the band width, so the rate of sending letters is proportional to band width. Nyquist and Hartley showed it is proportional to the logarithm of the number of current values (p. 44).
- Shannon's question: how can messages from a source be encoded as signals for the fastest possible transmission over a noisy channel, and how fast can a given type of message be sent over a given channel without error? (p. 44)

## Toy example (ours, not from the text)
Take $m=2$ levels and $m=4$ levels, with $K=100$ symbols/s in $W=K\log_2 m$ (illustrative $K$).
- $m=2$: $W = 100\times\log_2 2 = 100\times 1 = 100$.
- $m=4$: $W = 100\times\log_2 4 = 100\times 2 = 200$. Check by counting: the pair (message 1 bit, message 2 bit) has $2\times 2 = 4$ combinations, and each combination can be one of the four levels $+3,+1,-1,-3$.
- $m=3$: $W = 100\times\log_2 3 \approx 100\times 1.585 = 158.5$, i.e. about 60% more than 100.
- Hartley: $s=8$ equally likely symbols, $n=4$ chosen independently. The number of sequences is $8^4 = 4096$ and $H=\log_2 4096 = 12$. Also $n\log_2 s = 4\times 3 = 12$. ✓.

## Concepts
- [[entropy-communication-sense]] (new) — measure of uncertainty about which message a source will produce; more uncertainty means more information conveyed (p. 23).
- [[entropy-thermodynamic]] (new) — physics entropy: constant in reversible processes, rises in irreversible ones, lowers available energy; related to disorder as lack of knowledge (pp. 21–23).
- [[bit]] — here an independent "0-or-1 choice"; $\log_2$ of the number of symbols counts them (pp. 37–38).
- [[redundancy]] — Nyquist's sense: a signal component that conveys no intelligence because it is predictable at the receiver (p. 39).
- [[noisy-channel]] — a circuit that is subject to unwanted extraneous currents ("noise") (p. 29).
- [[intersymbol-interference]] (new) — overlap of smeared adjacent symbols at the receiver (p. 29).
- [[fourier-analysis]] (new) — representing any signal as a sum of sine waves of different amplitudes, phases, frequencies (pp. 31–32).
- [[linear-circuit]] (new) — circuit whose output for a sum of inputs is the sum of outputs; signals do not interact (pp. 32–33).
- [[bandwidth]] (new) — the range (band) of frequencies used; speed is proportional to it (p. 38).
- [[nyquist-relation]] (new) — $W = K\log m$ (p. 36).
- [[hartley-information]] (new) — $H = n\log s$ for independent, equiprobable symbols (p. 40).

## Canonical instances
- [[morse-code]] — short codes for frequent letters; early efficient encoding (p. 25).
- [[edison-quadruplex]] — four current values carry two independent messages (pp. 27–29).
- [[first-transatlantic-cable-1858]] — failure likely due to the high transmitting voltage (p. 29).
- [[radar-prediction-problem]] — estimating a plane's course from noisy data; the Wiener/Kolmogoroff problem (pp. 41–42).
- [[gas-expansion-partition]] — entropy increases though energy is constant (p. 22).

## Bridges (candidates)
- [structural-analogy] Pierce's "order = knowledge" reading of entropy ↔ statistical physics: entropy as uncertainty about microstate — both link entropy to missing knowledge (pp. 22–24).
- [same-math] Nyquist's $\log m$ for $m$ symbols ↔ information theory: bits per symbol for equiprobable symbols — same counting argument as $\log_2$ of the number of outcomes (pp. 37–38).
- [structural-analogy] Wiener filtering of signal in noise ↔ signal processing: choose a circuit that best estimates a signal from a mixture.
- [metaphor] Linearity as non-interaction of signals ↔ social systems: independent additive influences (Pierce's train example, p. 33).

## Questions this raises
- If Hartley's formula holds only for independent, equally likely symbols, what replaces it when symbols have unequal probabilities?
- How many levels can a noisy circuit support before they cannot be told apart, i.e. what determines the limit that Nyquist only hints at?
- Is the analogy between the two entropies deeper than the shared mathematics (Chapter X is promised)?
- What exactly does Shannon's goal of fastest possible, error-free transmission over a noisy channel look like?

## Reading notes
- Printed page = pdf page − 16 (pdf 35 = p. 19). All cited numbers are printed numbers.
- Edition: the page images and running headers read *Symbols, Signals and Noise*, as in the unit metadata's warning about the 1961 first edition. The title page is not among these pages, so I could not verify edition details here.
- Tables I–IV (and the values in Table II) are blank in the extracted text. Only Fig. II-1/II-2 were seen as images (p. 26). The contents of Table I are not reproduced; I give only the principle stated in the prose (p. 27).
- Text-layer garbling: minus signs are lost (e.g. "+3, +1, 1, 3" means $+3,+1,-1,-3$). "2 log x = x" is $2^{\log x}=x$ (p. 36). "no frequencies about N cps" (p. 39) is presumably "above N".
- Probable error in the source: p. 38 says eight current values allow "four times as fast" sending as two. By the author's own relation $W=K\log m$, $\log_2 8 = 3$, so the factor would be three. The list of eight values on p. 38 is also garbled in the text layer.
- The text layer reads "Wfener" for Wiener (p. 44); this is most likely an OCR error, and I could not check it against the page image.
