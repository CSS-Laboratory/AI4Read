---
id: pierce-1980-introduction/ch10-information
work: pierce-1980-introduction
unit: "10 Information Theory and Physics"
pages: 184-207
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Information Theory and Physics

## L0 — One line
Heat sets an unavoidable noise floor of kT watts per hertz, which (for ideal encoding) fixes a minimum energy of 0.693 kT joule per bit, and that same energy equals the most work a one-molecule engine could gain, so the engine does not beat the second law.

## L1 — The gist (≤ 120 words)
Pierce asks how physics limits communication, and how physics relates to information theory. Hot bodies emit thermal (Johnson) noise of power N = kTW. Put into the Gaussian-channel capacity formula, it gives, for ideal encoding, a minimum cost of 0.693 kT joule per bit. Pierce applies this to a Mars radio link, then notes that quantum limits are not yet worked out. He then shows that a one-molecule engine, a Maxwell's-demon relative, gains at most 0.693 kT of work per bit of information, which costs at least that much energy to transmit. He believes the same balance holds for any message about a system's state. To him the entropy debate seems "a tempest in a teapot."

**Prerequisites:** logarithms (base 2 and e); the idea of a bit and of source entropy; the Gaussian-channel capacity formula from the previous chapter; temperature as average molecular energy; the idea of a "second law."

## L2 — Key ideas (5–10 bullets)
- Any body above absolute zero radiates electromagnetic noise (p. 207). Johnson noise gives mean-square voltage $4kTRW$ and maximum available power $kTW$ (pp. 188–189). It is a minimum noise that other sources only worsen (p. 190).
- Receiver quality is expressed as an equivalent noise temperature $T_n$ (Johnson noise that would equal the receiver's added noise). Smaller is better (pp. 190–191).
- Combining capacity and $N=kTW$, as bandwidth grows the capacity tends to a limit. This means at least $0.693\,kT$ joule per bit, for ideal long-block encoding (p. 192).
- Mars example: ideally about 0.003 W suffices for 60 words/min. A realistic system might need roughly 1000× more, and a directive transmitting antenna would cut the power again (pp. 193–194).
- Quantum effects usually become important when $hf$ is comparable to or larger than $kT$. Exact quantum limits on communication were not yet known; Pierce is sure only that things will be somewhat worse than in the classical case (pp. 196–197).
- In the one-molecule engine, the most work per cycle is $0.693\,kT$. One bit must be learned, and sending it costs at least $0.693\,kT$, so there is no net gain (pp. 200–202).
- Pierce's general argument, which he states as his belief: information that cuts statistical-mechanical entropy raises free energy by exactly the minimum energy to transmit it. The price is always just high enough that a perpetual-motion machine of the second kind is impossible (pp. 205–206).

## L3 — Walkthrough

### Opening: why physics matters (pp. 184–185)
Communication theory grew out of electrical communication. Codes for sending letters as on/off currents led to general ideas of encoding (p. 184). Some noise can be reduced with careful design, directional antennas and frequency filtering. Some noise always remains: even if lightning were abolished, noise would persist while there is heat in the universe (pp. 184–185).

### Heat, radiation and thermal equilibrium (pp. 185–188)
- **Brownian motion.** Brown saw pollen grains dance in a liquid. Surrounding molecules, which are always in random motion, push them. This motion *is* heat. In gas, liquid and solid the average energy from heat is proportional to the temperature above absolute zero (p. 185).
- **Radiation.** Vibrating charges in hot matter can generate electromagnetic waves (radio, heat, light), called radiation (pp. 185–186).
- **Absorption and emission go together.** At a given frequency and temperature, a substance's emission is proportional to the fraction of incident radiation it absorbs rather than reflects (p. 186).
- **Argument by closed furnace.** Suppose one body reflected well but emitted strongly and another absorbed well but emitted poorly. Both start at the same temperature, and the second would become hotter than the first. This does not happen: all bodies reach the wall temperature. This can be so only if the ability to absorb and the ability to emit radiation go together, as they always do in nature (pp. 186–187).
- **Equilibrium radiation.** Radiation in an enclosure reaches equilibrium when the walls absorb as much as they emit. Its intensity depends only on the wall temperature, not on whether the walls are shiny or dull. Otherwise a hole between two such enclosures at the same temperature would give a net flow of radiation, which never happens (p. 187).
- Signals on wires can be seen as voltage and current or as electromagnetic waves. So heat should generate electrical signals (pp. 187–188).

*Intuition note.* A hot object cannot be a good absorber without also being a good emitter. If it could, objects in one hot box would settle at different temperatures. So the radiation filling an enclosure in equilibrium depends only on the temperature, not on the material of the walls.

### Johnson (thermal) noise (pp. 188–190)
J. B. Johnson found and measured voltage fluctuations across a resistor. Nyquist then derived their size using statistical mechanics (p. 188).

$$\overline{V^2} = 4kTRW \tag{10.1}$$

Here $\overline{V^2}$ is the mean-square noise voltage, $k = 1.37\times10^{-23}$ joule/degree is Boltzmann's constant, $T$ is the temperature in kelvin (absolute zero is $-273$ °C), $R$ is the resistance in ohms, and $W$ is the bandwidth in cycles per second (p. 188). $W$ depends on the measuring device. A TV receiver (bandwidth of several million cycles per second) sees more noise than a radio receiver (several thousand) (p. 188).

A second resistor connected to the hot one receives power. The most noise power the hot resistor can supply is

$$N = kTW \tag{10.2}$$

Pierce finds this form more satisfactory in some ways: $R$ has disappeared, and its form suits somewhat different situations (p. 189).

- **Radio telescope.** Pointed at things, it receives noise of power given by 10.2, with $T$ the temperature of the object. Leafy trees give about 290 K. The moon gives about the same, corresponding to a temperature a fraction of an inch below its surface (pp. 189–190).
- **Sun.** At about 10 million cycles/s the noise corresponds to about a million kelvin (the corona). At about 10 billion cycles/s it corresponds to about 8,000 K, a little above the visible surface. Why the corona is hotter is "not known" (p. 190).
- **Sky.** Above a few billion cycles/s it corresponds to 2–4 K. At lower frequencies it is greater. Because the heavens are not at a uniform temperature, 10.2 does not apply to them (p. 190).
- Johnson noise is a minimum that other sources only worsen; its fundamental nature has led to its use as a standard for measuring receivers (p. 190).

**Noise temperature.** $T_n$ is the temperature of Johnson noise which, amplified, would just equal the noise the receiver adds. Equivalently, an ideal noiseless receiver with the same gain and bandwidth, with Johnson noise of temperature $T_n$ added to its input, would give the same signal-to-noise ratio as the actual receiver. A smaller $T_n$ is better (pp. 190–191).

**Noise figure.** Defined for use on earth, where noise corresponds to about 293 K. It is the ratio of total output noise (amplified 293 K Johnson noise plus receiver noise) to the amplified Johnson noise alone. In terms of $T_n$ it is $NF = 1 + T_n/293$ (this formula is reconstructed from the garbled text layer, p. 191).

**Table XIV (p. 191).** Equivalent noise temperature in kelvin:

| Receiver | $T_n$ (K) |
|---|---|
| Radio or TV receiver | 30,000 |
| 6,000,000,000 cycle/s receiver with maser amplifier | 20 |
| Good 6,000,000,000 cycle/s receiver without maser | 3,000 |

### Noise and the power needed to send messages (p. 192)
Johnson noise is Gaussian, so the capacity formula of the previous chapter (9.3) applies. Ideally, to send $C$ bits per second we need signal power $P$ and noise power $N$ with

$$C = W\log_2\!\left(1+\frac{P}{N}\right) \tag{10.3}$$

Using 10.2 for $N$:

$$C = W\log_2\!\left(1+\frac{P}{kTW}\right) \tag{10.4}$$

(10.3 and 10.4 are reconstructed from garbled text; the passage's own description fits them.) For fixed $P$, a very small $W$ gives a very small $C$. Making $W$ larger does not raise $C$ without limit: it approaches a limiting value. When $P/kTW$ is very small compared with unity, 10.4 becomes (10.5) $C \approx P/(0.693\,kT)$. (added step: this uses $\log_2(1+x)\approx x/\ln 2$ for small $x$, with $\ln 2 = 0.693$.) Equivalently

$$P = 0.693\,kTC \tag{10.6}$$

So even with very wide bandwidth, at least $0.693\,kT$ joule per second is needed to send one bit per second, that is, on average $0.693\,kT$ joule per bit. This holds only for ideal encoding, in which many characters are encoded together into a long stretch of signal. Practical systems need much more energy per bit (p. 192).

*Intuition note.* Noise power grows with bandwidth, so extra bandwidth eventually stops helping. What remains is a floor set only by temperature: about $0.693\,kT$ joule for each bit. The floor is reached only with ideal encoding of many characters together; practical systems need more.

### Example: sending text from near Mars (pp. 192–194)
- Ideal text rate: about 1 binary digit per letter, or 5.5 per word. At 60 words per minute (1 word per second), $C = 5.5$ bits/s (pp. 192–193).
- Cold space at microwave frequencies: $T \approx 4$ K. From 10.6, the required received power is $P_R = 2\times10^{-22}$ watts (p. 193).
- Transmitted power spreads evenly over a sphere of surface $4\pi L^2$. A parabolic receiving antenna of diameter $D$ has area $\pi D^2/4$. So

$$\frac{P_T}{P_R} = \frac{4\pi L^2}{\pi D^2/4} = \frac{16L^2}{D^2} \tag{10.7}$$

(reconstructed). With $L = 1.5\times10^{11}$ ft (30 million miles) and $D = 150$ ft: $P_T/P_R = 1.6\times10^{19}$. So $P_T \approx 0.003$ watt (p. 193).

**Practical penalties (p. 194):**
- 5 binary digits per letter: ×5.
- A maser receiver ($T_n \approx 20$) instead of the sky's 4 K: another ×5.
- Sending digits one at a time by turning a transmitter on and off: perhaps another ×40.

Pierce says an actual system might call for about 1000 times the ideal, i.e. 3 W. Without a maser it might need another ×10, to 30 W.

**Ship in front of the sun.** The sun's temperature is about 2,000 times that of the cold sky. Ideal power is about 6 W, and practical power several hundred watts (p. 194).

**Directive transmitting antenna.** A large directive antenna at the transmitter would cut the power to perhaps a ten-thousandth to a millionth of the figures above. Even television between Mars and earth would be possible (p. 194). Pierce stresses that the gap between nature's limit and present encoding and receivers is wide, and worth narrowing for space work (p. 194).

### Wave-guide modes and quantum limits (pp. 195–197)
- **Modes.** Waves of wavelength smaller than about twice the pipe diameter can travel in a wave guide. When the wavelength is much smaller than the diameter, they travel in many spatial patterns (modes). In principle each carries an independent message. In practice imperfections make the modes interact, and it is best to use the mode with the least attenuation and get rid of the rest (p. 195).
- **Image analogy.** If a picture is placed across the guide, the strengths of the modes beyond it represent its light and dark. Forming an image with light is thus related to sending information through many independent channels (p. 195).
- **Classical equations fail for light.** 10.1 and 10.2 are classical, and are very inaccurate for light (about 500 million megacycles per second) (pp. 195–196). Radiation comes in quanta of energy

$$E = hf \tag{10.8}$$

with $h = 6.63\times10^{-34}$ joule·second. Quantum effects usually matter when $hf$ is comparable to or larger than $kT$. The frequency above which the classical expressions are clearly in error is

$$f = 2.07\times10^{10}\,T \tag{10.9}$$

(reconstructed). Pierce gives: at 3 K, about 60,000 megacycles/s (microwave range). At 300 K, 6 million megacycles/s (wavelength 0.005 cm, long infrared). Visible light is about 500 million megacycles/s, with wavelength about $6\times10^{-5}$ cm (p. 196).

- **What quantum theory changes.** Classically, noise is a smooth unpredictable quantity added to a smooth signal. Quantum theory makes a signal somewhat unpredictable even with no noise added. We cannot send less than one quantum, and by Heisenberg's principle we cannot specify both its frequency and its arrival time exactly (pp. 196–197).
- **Results Pierce gives, without interfering thermal quanta (p. 197):**
  - On average, an unlimited number of bits per quantum can be sent if enough time is allowed. The sender chooses among very many time intervals or frequencies, with complicated encoding to handle occasional quantum errors.
  - The power per bit can be made as small as we like, by sending many bits per quantum and by using low frequency. At very low frequencies, 10.6 applies in the quantum case too, since quantum behaviour approaches classical behaviour there.
- **What is not known.** There are no exact expressions for high-frequency signals mixed with noise. Pierce is sure only that things will be somewhat worse than the classical Johnson-noise case, and how much worse is not yet known (p. 197). Pierce notes that physicists have not yet given a complete answer (p. 196).

Pierce adds that the most interesting link of physics to information theory is evaluating unavoidable physical limits. These include Johnson noise, quantum effects, and also atmospheric turbulence and ionosphere fluctuations, which distort a signal rather than add noise to it (p. 198).

### Perpetual motion and Maxwell's demon (pp. 198–200)
Szilard in 1929 proposed using information transmission to show that a perpetual-motion machine of the second kind is impossible (p. 198). Machines of the first kind create energy, which violates the first law (conservation of energy). Machines of the second kind turn disorganised heat at one temperature into ordered energy such as a flywheel's rotation. The second law is stated variously: heat does not flow from cold to hot without organised energy, or the entropy of a system never decreases (p. 198).

- **Maxwell's demon** operates a door between two chambers. He lets fast molecules into his side and slow ones out, so his side becomes hot and the other cool (p. 199).
- **Pierce's general objection.** The demon's surroundings are at thermal equilibrium, so the only light present is random thermal radiation. It is too chaotic for him to see which molecules are coming (p. 199).
- **Spring door.** The proposal is that it would pass molecules in only one direction. Pierce's objection: a strong spring will not open for a molecule, while with a weak spring thermal energy keeps the door flapping, mostly open. Physicists are "pretty well agreed" that such mechanical devices cannot violate the second law (pp. 199–200).

### The one-molecule heat engine (pp. 200–202)
Pierce believes this machine, though ridiculous and inoperable in practice, is "not physically impossible" in the physicist's special sense (p. 200).

**Setup (Fig. X-3).** A cylinder holds one molecule $M$. A frictionless piston with a door in it moves left or right, raising one pan and lowering the other. The whole device is at temperature $T$ (p. 200).

**Cycle (pp. 200–201):**
1. Center the piston with the door open, clamp it, and close the door.
2. Observe which side of the piston the molecule is on.
3. Put a weight from the low shelf onto the pan on that side and unclamp the piston.
4. The molecule's impacts raise the weight to the high shelf. Move it there, open the door, re-center, and repeat.

So organised work is done from disorganised thermal energy (p. 201).

**Work.** The average force on the piston is

$$F = \frac{kT}{L} \tag{10.10}$$

(reconstructed), where $L$ is the distance from the piston to the end on the molecule's side. If the molecule slowly drives the piston until $L$ is doubled, the most work it can do is

$$W = 0.693\,kT \tag{10.11}$$

For a constant weight the work is less, so 10.11 is a limit (p. 201).

**The price.** Knowing which pan to load requires one bit, because the molecule is equally likely in either half. Transmitting one bit at temperature $T$ takes at least $0.693\,kT$ joule (from 10.6). This is just equal to the most the machine can produce, and it holds in the quantum case for very low frequencies (p. 201). So all the machine's output is used up in obtaining the information to run it. Pierce adds that even at the very best the machine does not come out ahead (p. 202); the page's wording appears to contain a slip (see Reading notes).

*Intuition note.* One bit of knowledge about where the molecule is lets a machine extract up to $0.693\,kT$ of work. Transmitting that bit against thermal noise costs at least the same amount. The gain and the cost cancel exactly at the best possible case.

### Two entropies (pp. 202–204)
- **Communication-theory entropy.** It measures uncertainty about which message a source will produce. For $m$ equally probable messages it is $\log_2 m$ bits per message. More generally it is the average number of binary digits needed to transmit the source's messages (p. 202).
- **Statistical-mechanics entropy.** It is the uncertainty about which state a physical system is in. All states of a given total energy are assumed equally probable. The entropy is Boltzmann's constant times the natural logarithm of the number of possible states. The free energy is

$$F.E. = E - HT \tag{10.12}$$

with $E$ the total energy, $H$ the entropy and $T$ the temperature. Free energy is the part of the energy that can ideally be turned into organised energy (p. 202).

- **System and state (p. 203).** A system is considered at equilibrium (uniform temperature, all changes complete). Its state is as complete a description of particle positions and velocities as physics allows. Classical mechanics gives an uncountably infinite number of states, which Pierce likens to continuous-signal theory. Quantum mechanics gives a countable infinity of states, like discrete signals.
- **Entropy of an ideal gas (pp. 203–204).** Larger volume gives more energy levels in a given energy range, so more states and more entropy. Higher temperature means more combinations of levels are available, so entropy increases. If the gas expands against a slowly moving piston with no heat added, the temperature drops just enough that the number of states and the entropy stay the same.
- **Small volume.** For a given temperature, a gas confined to a small volume has less entropy than the same gas in a larger volume. For the one-molecule gas of Fig. X-3 the entropy is less with the door closed, at least if we know which side of the piston the molecule is on (p. 204).
- **One-molecule gas.** Halving the volume halves the number of states, so the entropy changes by
$$k\log_e \tfrac12 = -0.693\,k$$
The change in free energy is $-T$ times that, that is $+0.693\,kT$. This is just the work obtainable by halving the volume and letting the molecule expand against the piston until the volume is doubled. So computing the free-energy change is another way of obtaining 10.11 (p. 204).

**Reviewing the engine (pp. 204–205).** Transmitting one bit against noise at temperature $T$ takes $0.693\,kT$ joule. Once we know which side the molecule is on, the entropy is $0.693\,k$ less than if we were uncertain. This corresponds to an increase in free energy of $0.693\,kT$. Letting the piston move to the unoccupied end brings the entropy back to its original value. The work obtained equals the minimum energy needed to transmit the information.

### The general case (pp. 205–206)
- A system has $m$ states in total, divided into $n$ equal groups of $m/n$ states each. Take "which group contains the state" as a message source with $n$ equally likely outcomes. Its entropy is $\log_2 n$ bits (p. 205).
- Transmitting this at temperature $T$ needs at least $0.693\,kT\log_2 n = kT\ln n$ joule. So the energy needed is proportional to the communication-theory entropy of the source (p. 205).
- Statistical-mechanical entropy:
  - Knowing only that the system is in one of $m$ states: $k\ln m$.
  - Knowing it is in one group of $m/n$ states: $k\ln(m/n)$.
  - Change from the information: $-k\ln n$.
  - Corresponding free-energy increase: $kT\ln n$.
  
  This is just the least energy needed to transmit the information (pp. 205–206).
- **Pierce's conclusion.** A process that tells us something about a system's state is a message source. Its messages reduce physical entropy and raise free energy, by an amount equal to the minimum energy needed to transmit them. That minimum is proportional to the communication-theory entropy (p. 206). Pierce says he believes this is the relation between the two entropies: one pays a price for information that reduces physical entropy. The price is proportional to the source's entropy, and it is always just high enough that a perpetual-motion machine of the second kind is impossible (p. 206).
- **Caveats (p. 206).** Sources about physical states are a peculiar kind of source. Relating the entropy of English text or speech to physical entropy seems irrelevant, except perhaps via the energy to transmit a bit under idealised conditions. Pierce says the whole concern seems to him "a tempest in a teapot"; no one doubts the second law. He adds that it would be worthwhile if it led physicists to find the quantum analog of 10.4, which he calls a conspicuously missing part of communication theory (p. 206).

### Summary (p. 207)
- Noise limits the rate at which information can be sent at given power and bandwidth.
- Thermal noise is simple, universal and unavoidable, and the classical expression fails at high frequency and low temperature.
- No general quantum formulation was available.
- As far as Pierce knows, physicists have not found anything very useful or startling in using information theory in statistical mechanics.

## Toy example (ours, not from the text)
Take a receiver at room temperature $T = 290$ K and a band $W = 10^6$ Hz.

- $kT = 1.37\times10^{-23}\times290 = 3.973\times10^{-21}$ J.
- Johnson noise power (10.2): $N = kTW = 3.973\times10^{-21}\times10^6 = 3.97\times10^{-15}$ W.
- Across $R = 1000\ \Omega$ (10.1): $\overline{V^2} = 4\times3.973\times10^{-21}\times10^3\times10^6 = 1.59\times10^{-11}\ \mathrm{V}^2$. The rms voltage is $\sqrt{1.59\times10^{-11}} \approx 4.0\times10^{-6}$ V (4 µV).
- Minimum energy per bit (10.6): $0.693\times3.973\times10^{-21} = 2.75\times10^{-21}$ J.
- So an ideal wide-band link at 1 Mbit/s needs at least $2.75\times10^{-21}\times10^6 = 2.75\times10^{-15}$ W. (This is a lower bound. At $W=10^6$ Hz the ratio $P/kTW$ is about 0.69, not small, so the bound is only approached as $W$ grows.)
- Engine link (10.11): one such bit lets a one-molecule engine at 290 K lift at most $0.693\,kT = 2.75\times10^{-21}$ J. This equals the cost of learning that bit, so the net gain is zero.

## Concepts
- [[thermal-noise]] (new) — Johnson noise, electrical noise from heat in any body above absolute zero; $N=kTW$ (pp. 188–189)
- [[noise-temperature]] (new) — the temperature of Johnson noise equal to a receiver's added noise; smaller is better (pp. 190–191)
- [[channel-capacity]] — here the Gaussian-channel result $C=W\log_2(1+P/N)$, used with $N=kTW$ (p. 192)
- [[shannon-hartley-formula]] — the formula 10.3/10.4; Pierce says it holds only for ideal encoding (p. 192)
- [[bit]] — here also the unit of the entropy of a message source (p. 202)
- [[entropy]] — communication-theory entropy: uncertainty about which message; average number of binary digits needed (p. 202)
- [[thermodynamic-entropy]] (new) — $k$ times the natural log of the number of equally probable states (p. 202)
- [[free-energy]] (new) — $F.E.=E-HT$, the part of the total energy that can ideally become organised energy (p. 202)
- [[maxwells-demon]] (new) — fictional being who sorts molecules by speed to break the second law (p. 199)
- [[quantum-limits-on-communication]] (new) — $E=hf$; usually important when $hf \gtrsim kT$; exact limits not yet known (pp. 196–197)

## Canonical instances
- [[mars-radio-link]] — ideal 0.003 W for 60 words/min; a practical system might need ≈ 1000× more; sun in line, ×2000 (pp. 193–194)
- [[one-molecule-engine]] — cylinder with piston and one molecule; the work gained, $0.693\,kT$ per bit, equals the minimum transmission energy (pp. 200–202)
- [[maxwells-demon]] — divided box with a door-keeper; the objection is that thermal light is too chaotic to see by (pp. 199–200)
- [[radio-telescope-noise-temperatures]] — trees ≈ 290 K, sky 2–4 K, sun 8,000 K to a million K depending on frequency (pp. 189–190)

## Bridges (candidates)
- [structural-analogy] minimum energy $0.693\,kT$ per bit (10.6) ↔ information theory/physics: Landauer's principle ($kT\ln 2$ per bit); the same numerical bound, though this unit derives it from capacity, not from erasure.
- [structural-analogy] one-molecule engine's bit-for-work trade ↔ Kelly criterion: side information has a measurable, bounded value (it raises growth by its mutual information).
- [structural-analogy] number of equally likely states, $\log_2 m$ bits ↔ source entropy: the same counting idea behind both entropies (p. 202).
- [metaphor] receiver noise temperature as a "price of quality" ↔ rational inattention: limited ability to absorb a signal.

## Questions this raises
- How exactly does the quantum analog of 10.4 look, and how much worse than classical is it when $hf$ is large?
- Does the balance in the one-molecule engine hold for every possible sensing device, or only for the thermal-noise channel Pierce uses?
- Why is the ideal bound unreachable in practice, and what codes get closest (the ×5 and ×40 penalties)?
- If an information source is not about a physical state (English text), does its entropy carry any physical meaning?

## Reading notes
- **Edition.** The scan is the 1961 Harper & Brothers *Symbols, Signals and Noise*, not the 1980 Dover edition named in the work citation. The chapter is numbered "X" in the printed text (with equation labels 10.x). Printed page = pdf page − 16. Running headers read "Symbols, Signals and Noise" and "Information Theory and Physics."
- **No page images** were supplied. The text layer is garbled for equations 10.3–10.5, 10.7, 10.9, 10.10, the noise figure, and some symbols. I reconstructed these from context and checked them numerically against Pierce's own figures ($P_R = 2\times10^{-22}$ W; $P_T/P_R = 1.6\times10^{19}$; 60,000 megacycles at 3 K).
- **Constants and signs.** The text layer gives $k=1.37\times10^{-23}$; the minus signs of "−273" and "−459" appear garbled as spaces. The wavelength at 3 K is garbled as "% centimeter"; I read it as about ½ cm but did not cite it.
- **Likely misprint or OCR slip.** The text layer reads "even at the very best we could do more than break even" (p. 202). The surrounding argument suggests the intended meaning is that at best we cannot do more than break even. Also, in the closed-furnace passage (pp. 186–187) the text layer reads "shiny, reflecting little radiation and absorbing much"; the argument requires shiny bodies to reflect much and absorb little.
- Equation "9.3" is cited from the previous chapter; it is not in this unit.
