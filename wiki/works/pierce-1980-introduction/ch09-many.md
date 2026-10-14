---
id: pierce-1980-introduction/ch09-many
work: pierce-1980-introduction
unit: "9 Many Dimensions"
pages: 166–183
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Many Dimensions (Pierce, Ch. IX)

## L0 — One line
By treating the 2WT samples of a band-limited signal as coordinates of a point in 2WT-dimensional space, and using the fact that most of a high-dimensional sphere's volume lies near its surface, Shannon's channel capacity C = W log(1 + P/N) for a Gaussian noise channel is derived (the counting gives the upper limit; Pierce says Shannon's further argument shows it can be approached).

## L1 — The gist (≤ 120 words)
How many bits per second can be sent over a continuous channel of band width W, with signal power P and white Gaussian noise power N? Pierce builds the answer from geometry. A signal becomes a point in a space with one dimension per sample; squared distance from the origin is energy. Long signals and noise land near the surfaces of hyperspheres. Counting how many noise-spheres fit inside the signal-plus-noise sphere bounds the rate by C = W log(1 + P/N), and, Pierce says, C can be approached. Reaching C generally needs block coding with long noise-like waveforms. Trading band width for power (as FM does) is possible, but such schemes "break" at low signal-to-noise ratio.

**Prerequisites:** Pythagorean distance; powers and logarithms (base 2); sampling theorem (2W samples/s); ergodic source (Ch. III, V); the idea of channel capacity. Terms: hypersphere = sphere in many dimensions; band-limited = no frequencies above W; block coding = coding many symbols together; FM = a radio system that sends the message as changes of frequency.

## L2 — Key ideas (5–10 bullets)
- Mathematicians can define spaces with any number of perpendicular axes. A point is a list of coordinates, and squared distance from the origin is the sum of squared coordinates (pp. 167–169).
- In n dimensions the volume of a sphere scales as $r^n$. A fraction $1/2^n$ lies within half the radius, so in very high dimension nearly all volume lies near the surface (pp. 169–170).
- A band-limited signal of duration T has 2WT samples. Those samples are the coordinates of one point, and its squared distance from the origin is the signal energy (pp. 171–172).
- For stationary, ergodic signals and Gaussian noise, nearly all long messages have almost constant energy. Signal points lie near a sphere of radius $\sqrt{2WTP}$, and the noise displaces the received point by about $\sqrt{2WTN}$ (pp. 172–174).
- Counting non-overlapping noise-spheres in the received sphere gives at most $(1+P/N)^{WT}$ distinguishable messages, hence $C = W\log(1+P/N)$ (eq. 9.3). Pierce says Shannon shows the rate can approach C with arbitrarily few errors (pp. 175–176).
- Approaching C generally needs block coding with long, noise-like waveforms. In one example, sending binary digits one pulse at a time needs about six times the power (p. 177). A special exception is a single short pulse in one of many time positions.
- The same capacity can come from a wide band at low P/N or a narrow band at high P/N. Wide band is the practical route, as in FM (pp. 178–179).
- A topological theorem on mapping between spaces of different dimension implies such schemes "break" at some noise level (pp. 179–181).

## L3 — Walkthrough

**Opening (pp. 166–167).** Pierce recalls *Flatland* (a two-dimensional world) and notes that other "fourth dimensions" exist: time in Einstein's theory, and phase spaces in physics. The point is that nineteenth-century mathematicians generalized geometry to any number of dimensions, even infinitely many (p. 167).

**Coordinates (pp. 167–169).** A point on a line is located by one number $x_p$. A plane needs two, space needs three, and with axes labelled $x_1,\dots,x_5$ a five-dimensional space needs five (pp. 167–168). We cannot lay out five mutually perpendicular lines in our three-dimensional space, but the mathematician can reason about them logically (p. 169).

To make the space Euclidean (like ordinary space), the squared distance of a point from the origin is the sum of squared coordinates. Eq. (9.1) is missing from the text layer; this is the form implied by the next section, which says E is "the square of the distance… as given by 9.1" (reconstructed, p. 169):
$$d^2 = x_{1p}^2 + x_{2p}^2 + x_{3p}^2 + x_{4p}^2 + x_{5p}^2 \tag{9.1}$$

The "volume" of a hypercube is the product of its side lengths: $L^2$, $L^3$, $L^5$, and $L^{99}$ for 99 dimensions (p. 169).

**Spheres in many dimensions (pp. 169–170).**
- A circle of radius 1 has area $\pi$. A concentric circle of radius ½ has area $\pi(1/2)^2 = \pi/4$, so a quarter of the area lies within half the radius (pp. 169–170).
- For spheres the volume is $\tfrac{4}{3}\pi r^3$, so the fraction within half the radius is $(1/2)^3 = 1/8$ (computed from the $r^n$ rule; the text layer is garbled here, p. 170).
- In $n$ dimensions volume is proportional to $r^n$, so the fraction within half the radius is $1/2^n$. For $n=7$ it is $1/128$ (p. 170).
- For a 1,000-dimensional hypersphere, a fraction 0.00004 of the volume lies in a sphere of 0.99 the radius (p. 170).
- Conclusion: for a hypersphere of very high dimension, essentially all the volume lies very near the surface (p. 170).

*Intuition note.* Shrinking the radius a little removes a factor $0.99$ in every one of many dimensions. These factors multiply, so the inner sphere holds almost nothing. A point chosen uniformly at random in the sphere therefore almost surely lies near the outer shell.

Pierce says such ideas are pure, esoteric mathematics unless they are attached to some problem of the physical world. Shannon's use of it for continuous band-limited signals in noise is his example (p. 170).

**Signals as points (pp. 171–172).**
- Energy and power are proportional to the square of the voltage. Doubling the voltage multiplies energy and power by 4 (p. 171).
- A band-limited signal of band width W is fixed by 2W samples per second. Each sample can be chosen freely and independently (p. 171).
- Choosing units so that sample energy equals amplitude squared, the total energy is
$$E = x_1^2 + x_2^2 + x_3^2 + \cdots \tag{9.2}$$
- This is the squared distance from the origin in eq. 9.1. The whole signal is one point in hyperspace, and its squared distance from the origin is its energy (p. 172).

**Ergodic signals concentrate near a sphere (pp. 172–173).**
- The source is assumed stationary and ergodic (Ch. III), and so are the noise and the signal-plus-noise "source" (p. 172).
- Very high- or very low-energy sample runs are possible but very unlikely, like a long run of E's. This is the Ch. V theorem that an ergodic source's messages split into probable and negligible classes (p. 172).
- So long messages have a meaningful average power. For a large number of samples, the energy is nearly the same whichever succession of samples is chosen (p. 173).
- A signal of band width W and duration T has 2WT samples. With average energy P per sample, the total energy is very close to $2WTP$ when 2WT is large (p. 173).
- The signal points therefore lie, within a small fraction of the radius, near the surface of a hypersphere of radius $\sqrt{2WTP}$. This is not surprising given the high dimension (p. 173).

**Noise (pp. 173–174).**
- Shannon's noise is white Gaussian. "White" means all frequencies equally, here up to W cycles/s. "Gaussian" refers to a probability law for the sample amplitudes, which holds for many natural noise sources (pp. 173–174).
- Its 2W samples per second are uncorrelated and independent. With average sample energy N, the total energy of 2WT samples is very nearly $2WTN$ (p. 174).
- The signal-plus-noise point is at distance $\sqrt{2WTN}$ from the signal point. So it lies in a small hypersphere of that radius centred on the signal point (p. 174).
- The total received energy is $2WT(P+N)$, so the received point lies within a hypersphere of radius $\sqrt{2WT(P+N)}$ (p. 174).

**Counting messages (pp. 174–176).**
- The receiver knows the received point, not the signal. It knows only that the signal lies within $\sqrt{2WTN}$ of that point (p. 174).
- Place many non-overlapping little spheres, each of radius a shade larger than $\sqrt{2WTN}$, inside the big sphere. Send only signals at their centres. Each received point then falls in exactly one little sphere, because noise points lie almost on a sphere of radius $\sqrt{2WTN}$. So the signal is identified "infallibly" (pp. 174–175).
- The number of little spheres cannot exceed the ratio of volumes. The space has $n = 2WT$ dimensions and volume scales as $r^n$, so (the simplification to the last form is an added step, p. 175):
$$\left(\frac{\sqrt{2WT(P+N)}}{\sqrt{2WTN}}\right)^{2WT} = \left(\frac{P+N}{N}\right)^{WT} = \left(1+\frac{P}{N}\right)^{WT}$$
- The logarithm of this is the number of bits sendable in time T: $WT\log(1+P/N)$. Dividing by T gives bits per second (p. 175):
$$C = W\log\left(1+\frac{P}{N}\right) \tag{9.3}$$
- The ratio of energy per sample is the same as the ratio of signal power to noise power. So P/N can be read as a power ratio (p. 175).
- So far this shows only that no more than C bits per second can be sent. Pierce says Shannon, by a further geometric argument using the near-surface property, shows that the rate can approach C as closely as desired with as few errors as desired. So C is the capacity of this continuous channel (pp. 175–176).

*Intuition note.* Each distinguishable message needs its own "noise-sized ball" of room. Dividing the volume of the whole received region by the volume of one noise ball gives the maximum number of messages. Taking the log turns that count into bits.

**Link to Nyquist and Hartley (pp. 176–177).**
- Nyquist and Hartley (1928) gave $n\log m$ bits/s, with m symbols and n symbols per second (p. 176).
- With $n = 2W$ independent samples per second, eq. 9.3 becomes $C = (n/2)\log(1+P/N)$. This corresponds to an average number of symbols per sample of $m=\sqrt{1+P/N}$ (p. 176).
- As P/N → 0, capacity goes to 0. It grows large when P/N is large (p. 176).
- Example: for P/N = 24, we can send on average $\sqrt{1+24}=\sqrt{25}=5$ different symbols per sample with negligible error. This cannot be done by sending one of 5 symbols in each single sample (p. 177).
- Efficient signalling generally needs block encoding: a long symbol sequence is encoded in many samples. The set of code waveforms should be long, complicated waves resembling Gaussian noise (p. 177).
- A special exception: with small signal power in large noise, put all power into one short pulse in one of many time positions. Then symbols can be sent one at a time (p. 177).
- Comparison from Ch. VIII: sending binary digits one at a time as positive or negative pulses, with 1 error in 100,000, needs about six times the power that eq. 9.3 requires for the same W and N (p. 177).

**Trading band width and power (pp. 178–179).**
- Example: W = 4 megacycles/s and P/N = 1,000 give C = 40,000,000 bits/s. Table XIII lists other (W, P/N) pairs with the same C; its body is not in the text layer (p. 178).
- Conclusion: the same capacity is reached with broader band and lower P/N, or narrower band and higher P/N (p. 178).
- Early workers were drawn to cutting band width by raising power. Pierce says that needs lots of power, and experience shows it is more useful to widen the band and reduce the power (p. 178).
- FM does this. High-fidelity music of band width 15,000 cps is sent in a 150,000 cps radio band. The received music can then have a higher signal-to-noise ratio than the radio signal. FM is not ideally efficient and does not give the improvement eq. 9.3 would allow (pp. 178–179).
- Pierce reports that two proposed systems claimed to beat eq. 9.3. He knew, as with perpetual motion, that something was wrong, and analysis found the error (p. 179).

**Why such schemes break (pp. 179–181).**
- Sending few message samples as many signal samples means mapping points of a low-dimensional space one-to-one into a higher-dimensional one (p. 179).
- Ch. I proved that a one-to-one mapping of a plane onto a line cannot be continuous. A similar theorem holds for spaces of different dimensionality (p. 179).
- Shannon's example (Fig. IX-3): a single amplitude u is represented by two amplitudes $v_1, v_2$, taken as position in a square. A snaky line crosses the square back and forth, and u is distance along it (p. 180).
- Small noise leaves us in a circle of uncertainty smaller than the gap between loops, so u is found accurately. Larger noise can put us on the wrong loop, and the error in u is then large (pp. 180–181).
- So the output noise first rises gradually and then catastrophically as input noise grows. The system "breaks" at some signal-to-noise level. This is unavoidable in systems of this general type (p. 181).

*Intuition note.* Stretching a short message along a long, folded curve gives noise-resistance only while the folds stay farther apart than the noise. Beyond that, the receiver confuses neighbouring folds. This is why, Pierce says, a system that expands band width to gain signal-to-noise ratio cannot behave well at all noise levels.

**Signal space (p. 181).** Pierce says the geometrical approach is only one way of dealing with continuous signals; Shannon gives another, in his book on communication theory, applicable to all types of signals and noise. Band-limited signals can also be geometrized without samples, as points in a "signal space" or "function space". This allows statements true of all band-limited signals, like statements about all triangles (p. 181).

**Summary (pp. 182–183).** Eq. 9.3 gives the rate at which binary digits can be sent with negligible error. Nyquist knew 2W independent symbols per second could be sent, but not how many symbols per sample are possible at a given P/N for this noise (p. 182). Block coding is needed in general. Wide band with low P/N can carry a narrow-band, high-P/N message, a topic for Chapter X (p. 182). The chapter is also an example of applying a new viewpoint and a powerful branch of mathematics to an engineering problem (pp. 182–183).

## Toy example (ours)
Take W = 1000 Hz, T = 0.01 s, N = 1, P = 15.
- Samples: $2WT = 2\cdot1000\cdot0.01 = 20$, so the space has 20 dimensions.
- Radii: signal sphere $\sqrt{20\cdot15}=\sqrt{300}$; noise sphere $\sqrt{20\cdot1}=\sqrt{20}$; received sphere $\sqrt{20\cdot16}=\sqrt{320}$.
- Radius ratio: $\sqrt{320}/\sqrt{20}=\sqrt{16}=4$.
- Volume ratio (dimension 20): $4^{20}=2^{40}$ messages at most.
- Bits in 0.01 s: $\log_2 2^{40}=40$. Per second: $40/0.01=4000$.
- Check with eq. 9.3: $1000\cdot\log_2(1+15)=1000\cdot4=4000$ bits/s ✓.
- Symbols per sample: $\sqrt{16}=4$, i.e. $\log_2 4=2$ bits per sample. With 2000 samples/s this is 4000 bits/s ✓.

## Concepts
- [[channel-capacity]] — for a Gaussian channel, $C=W\log(1+P/N)$, the highest rate of negligible-error signalling (pp. 175–176)
- [[shannon-hartley-formula]] — eq. 9.3; here derived by sphere counting (p. 175)
- [[noisy-channel]] — a channel with white Gaussian noise of power N added to the signal (pp. 173–174)
- [[typical-set-aep]] — here, for ergodic sources and Gaussian noise, long sequences have energy nearly constant, so they lie near a sphere surface (pp. 172–174); used qualitatively, not stated as AEP
- [[signal-space]] (new) — a signal as a point whose coordinates are its samples; squared distance from the origin is energy (pp. 171–172)
- [[high-dimensional-geometry]] (new) — in n dimensions, volume scales as $r^n$, so nearly all volume of a sphere lies near its surface (p. 170)
- [[block-coding-continuous]] (new) — near-capacity signalling generally needs long noise-like waveforms coding many symbols together (p. 177)
- [[bandwidth-power-tradeoff]] (new) — the same C from wider W and lower P/N or narrower W and higher P/N; FM is an example (pp. 178–179)
- [[threshold-effect]] (new) — noise in a dimension-expanding system grows gradually, then catastrophically ("break") (p. 181)

## Canonical instances
- [[hypersphere-volume-near-surface]] — 1/128 within half radius at n=7; 0.00004 within 0.99 radius at n=1000 (p. 170)
- [[fm-radio]] — 15,000 cps music sent in a 150,000 cps band; trades band width for signal-to-noise ratio (pp. 178–179)
- [[snaky-line-mapping]] — Shannon's example of one amplitude mapped into a square, showing breaking at high noise (pp. 180–181)
- [[bandwidth-4mc-example]] — W = 4 Mc/s, P/N = 1,000, C = 40,000,000 bits/s (p. 178)

## Bridges (candidates)
- [same-math] Sphere counting for $C=W\log(1+P/N)$ ↔ information-theory: the Shannon–Hartley formula in the canon list — the same formula.
- [structural-analogy] Nearly all volume near the surface, so energy of long signals is nearly constant ↔ information-theory: typical set/AEP — both say long sequences concentrate on a "thin" high-probability region.
- [structural-analogy] Block coding with noise-like waveforms ↔ information-theory: source–channel coding theorems, where long blocks are needed to approach limits.
- [metaphor] Pierce's point that theory shows what "can't be accomplished" (like perpetual motion) ↔ physics: conservation limits.

## Questions this raises
- Eq. 9.3 argues "no more than C" by volume counting. What exactly is added in Shannon's argument that rates close to C are achievable?
- Why does the capacity depend on P/N only through $\log(1+P/N)$? What happens to C as W grows for fixed P and noise density? (Pierce defers band-width trade-offs to Ch. X.)
- How does the "breaking" of FM at low signal-to-noise connect with the dimension-mapping theorem, and can any scheme avoid it?
- If the noise is not Gaussian or not white, does the same sphere picture hold?

## Reading notes
- Edition: the source notes say this is the 1961 Harper & Brothers first edition, not the 1980 Dover edition named in the work citation; the running head on these pages reads "Symbols, Signals and Noise". Printed = pdf − 16.
- Only the text layer was available to me. It is garbled in places. Eq. 9.1 is missing and is reconstructed from the context on p. 172.
- The volume-ratio display on p. 175 is garbled. The final form $(1+P/N)^{WT}$ is derived by me from the stated radii and dimension.
- The text layer is also garbled for the 1/8 fraction (p. 170) and for $C=(n/2)\log(1+P/N)$ (p. 176). I wrote both from context.
- Table XIII's body is not in the text layer, so I omit its entries.
- In the text layer the page 177 header reads "111" and the page 181 header reads "1 8 1"; both are OCR errors for 177 and 181.
- The chapter number at the top of p. 166 reads "YV" in the text layer, a scan error for IX.
- The text layer shows some minus signs missing: "+3, +1, −1, −3" appears as "+3, + 1, 1, 3".
