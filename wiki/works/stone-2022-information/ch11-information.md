---
id: stone-2022-information/ch11-information
work: stone-2022-information
unit: "11 Information As Nature's Currency"
pages: 217-240
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Information As Nature's Currency

## L0 — One line
Information theory gives an absolute scale (bits) for judging how well engineered and biological systems, such as TV links, genomes and neurons, handle information, and the neural systems studied look close to the limits it sets.

## L1 — The gist (≤ 120 words)
The chapter asks what information theory says about real systems. First, TV and audio compression fit a 1.5 Gb/s source into a 19.2 Mb/s channel by removing redundancy and invisible detail. Next, MacKay's model suggests sex lets a genome gain up to about √N bits per generation, against about one bit without sex. DNA holds at most about 6 billion bits, far too few to specify about 10^15 synapses, so brains must learn. Finally, neurons, Laughlin's fly cells and the retina's colour channels appear to encode close to optimally. Without bits, such efficiency could not be measured.

**Prerequisites:** entropy and bits; binary-channel capacity; cdf and pdf; correlation vs independence; logarithms base 2.

## L2 — Key ideas (5–10 bullets)
- TV and audio compression combine four stages: remove redundancy, discard imperceptible frequencies, recode symbols to be equiprobable, then add a little error-correcting redundancy. Together they give a compression factor of about 78 (p. 218–220).
- Lossy compression discards information, but it can be invisible to human perception (p. 219–220).
- The author treats natural selection as transferring information from environment to genome, and each individual gives at most one bit about relative fitness (p. 220–221).
- In MacKay's model a sexual population can gain information at up to √N bits/generation, and it tolerates mutation rates about √N times higher than an asexual one (p. 223–224).
- The genome holds at most about 6×10^9 bits, far fewer than the roughly 10^15 synapses, so the brain must learn (p. 225–227).
- A neuron's spike-train entropy and its mutual information with its input give absolute figures: an estimated 4.32 bits/spike, and a coding efficiency of about 0.5 for cricket neurons (p. 228–231).
- Laughlin found fly LMC responses match the cdf of environmental contrast, the entropy-maximising encoder (p. 232–234).
- Sum–difference recoding of cone outputs appears to use the optic-nerve bottleneck efficiently, and the author concludes sensory systems operate near physical limits (p. 235–237).

## L3 — Walkthrough

### 11.1 Introduction
The chapter surveys applications of information theory in linguistics, communications, computing, neuroscience, genetics and evolution (p. 217).

### 11.2 Satellite TVs, MP3 and All That
- **The problem.** A TV camera is a source producing about 1.5 Gb/s. Colour images have 1920×1080 elements and three colour pixels each, so $3 \times 1920 \times 1080 = 6{,}220{,}800$ pixels per image. With 256 intensity levels, each needs $\log 256 = 8$ binary digits. This gives 49,766,400 binary digits per image, so about 1,500 million binary digits/s at 30 images/s (p. 217–218).
- The satellite channel carries only 19.2 million binary digits/s. For a noiseless channel this is a capacity of exactly 19.2 million bits/s (p. 218).
- **Four processing stages** (p. 218):
  1. Squeeze out redundant data. This includes spatial redundancy (similar adjacent pixels) and temporal redundancy (similar pixels in consecutive images).
  2. Remove components almost invisible to the eye.
  3. Recode so all symbols occur equally often (e.g. Huffman coding).
  4. Add a small amount of error-correcting redundancy.
- **MPEG and the cosine transform.** MPEG is the standard set of methods for removing spatial and temporal redundancy. They rely on the cosine transform, which splits data into features of different sizes, i.e. spatial and temporal frequencies. Large or persistent features have low frequencies (p. 218–219).
- **Discarding frequencies.** Throwing frequencies away reduces the quantity of data (good) and of information (bad). The author says it is 'not so bad, after all' if only frequencies we cannot see are lost. These are fine details (high spatial frequency), too-fast changes (high temporal frequency) and very low spatial/temporal frequencies (p. 219).
- **Colour recoding.** The eye is sensitive to luminance but relatively insensitive to fine colour gradations. Recoding to high-resolution intensity and low-resolution colour saves 50% of the binary digits for colour and intensity (p. 219).
- **Result.** The compression factor is about $1500/19.2 \approx 78$. It must be somewhat better, because stereo sound shares the channel; sound uses the same cosine-transform idea (MP3) (p. 219–220).
- **Lossy and lossless.** Lossy compression throws information away. Lossless compression keeps all of it. Most practical systems are lossy (p. 220).
- The added error-correcting redundancy is small, but enough to recover from all but the most catastrophic electrical interference (p. 220).

*Intuition note.* The channel is about 78 times too small for the raw data, but most raw data is predictable or invisible. Remove those parts, then protect the rest with a little redundancy.

### 11.3 Does Sex Accelerate Evolution?
- **Framing (the author's view).** Mathematics cannot usually settle biological questions, but it can exclude some answers and yield testable hypotheses. Evolution is "essentially" a process by which natural selection transfers information from environment to the species' collective genome (p. 220).
- Each individual is a "question" asked of the environment. The answer is fitness, measured as offspring reared to breeding age. Fitness information is crude (whole numbers) and noisy (chance matters). It is assigned to the whole individual, not to particular genes. Since an individual lives or dies before reproducing, its genome provides a maximum of one bit about its relative fitness (p. 221).
- **Holland (1992).** Holland proved the schema theorem. A gene increases in frequency at a rate exponentially related to the extra fitness it confers. His results make no explicit claim about information theory, but the author says it seems likely to be relevant (p. 221–222).
- **MacKay's model (2003).** One nucleotide is identified with one bit. Each nucleotide is simplified to a good or bad state. Fitness is the number of good nucleotides in a genome of $N$. Normalised fitness is the proportion of good ones, and the excess above 50% is $\delta f$, called "fitness" (p. 222–223).
- Figure 11.1 simulates sexual and asexual populations with $N=1000$ and initial fitness 500. The sexual curve rises faster and plateaus higher (p. 222).
- **Results as reported:**
  - A well-adapted sexual population, whose genome is near optimal, acquires one bit every two generations (p. 223).
  - If the environment changes, MacKay proves a genome of $N$ nucleotides can accumulate information from the environment at up to
  $$\sqrt{N}\ \text{bits/generation}. \tag{11.1}$$
  The text gives 540,000 bits/generation for $N=3\times10^9$ (see Reading notes) (p. 223).
  - An asexual population (e.g. aphids) acquires one bit per generation under similar circumstances (p. 223).
  - Mutation rate is the probability that a gene is altered between generations. In theory, the largest tolerable rate is about $1/N$ for asexual and $1/\sqrt N$ for sexual populations. Example: $N=100$ gives 0.01 vs $1/\sqrt{100}=0.1$ (p. 223–224).
- **Trade-off.** A large genome speeds evolution but lowers mutation tolerance. The author suggests evolution should have found a "happy medium" size (p. 224).
- **Summary of the analysis.** A sexual population accumulates information about $\sqrt N$ times faster than an asexual one, and tolerates a mutation rate about $\sqrt N$ times higher. Toy genome: $N=10{,}000$, asexual 10 bits/generation gives $10\times\sqrt{10{,}000}\approx 1{,}000$ bits/generation sexual (p. 224).
- **Candidate "law of life".** Between generations, the collective genome should maximise Shannon information acquired about its environment per joule of energy expended. The author calls this an extension of the efficient coding hypothesis for brains (p. 224–225).
- MacKay also argues that faulty DNA transcription smooths a rugged fitness landscape and speeds evolution. This is an example of the Baldwin effect, which is traditionally thought to rely on within-lifetime learning (p. 225).

*Intuition note.* In this model, asexual populations gain about one bit per generation. Sexual populations can gain up to $\sqrt N$ bits; the text reports this result without giving a mechanism here. The result is a model-based claim, with a size-versus-mutation trade-off.

### 11.4 The Human Genome: How Much Information?
DNA has a 4-letter alphabet (A, G, T, C). A message of $N$ letters has $m=4^N$ possibilities, so the maximum information is $H=\log 4^N = N\log 4 = 2N$ bits. For $N=3\times10^9$, $H = 6\times10^9$ bits. This is an upper bound, since the code is partly redundant and some regions seem not to code for anything. It fits in about 6 billion binary digits, almost one gigabyte ($8\times10^9$ binary digits), less than a basic DVD's 8 billion (p. 225).

### 11.5 Enough DNA to Wire Up a Brain?
- About $10^{11}$ neurons with about $10^4$ synapses each give about $10^{15}$ synapses (p. 226).
- Conservative bound: if each of the $3\times10^9$ nucleotides specified one synapse, with one bit per synapse strength, DNA could cover only about $10^9$ synapses, i.e. $10^9/10^{15}=10^{-6}$ of them. This leaves no DNA for the rest of the body. We would need about a million times more DNA (p. 226).
- **Conclusion (author).** Information theory answers "no": the genome cannot specify every connection. Hence the brain must learn, using environmental information to fix the correct set of synapses. That we do learn does not by itself imply we must learn in order to develop (p. 226–227).

### 11.6 Are Brains Good at Processing Information?
- **Setting.** The author says neurons essentially communicate information, and that natural selection has made them about as perfect as they can be. He supports this with information-theoretic work in computational neuroscience (p. 227). Barlow's efficient coding hypothesis says data from the eye should be encoded as efficiently as possible before reaching the brain (p. 227).

**Information in spiking neurons** (based on Rieke et al. 1997; MacKay and McCulloch (1952) made one of the first applications of information theory to neuroscience) (p. 227–228).
- A neuron is a binary channel: in each bin of width $\Delta t$ a spike is present or not. With $\Delta t = 0.001$ s, capacity is $C=1/\Delta t = 1{,}000$ bits/s, an upper bound (p. 228).
- **Entropy estimate**, assuming independent spikes and a simpler approximation than Rieke's. With firing rate $r$:
$$p = r\,\Delta t, \tag{11.2}$$
and $q=1-p$. The average information per bin is
$$H = h(p)+h(q) \tag{11.3}$$
$$\;\;= p\log(1/p) + q\log(1/q)\ \text{bits}. \tag{11.4}$$
- For small $\Delta t$, $p$ is low and $q\approx1$, so $h(q)\approx 0$ and $H\approx p\log(1/p)$. Then
$$H \approx r\,\Delta t \log\frac{1}{r\,\Delta t}\ \text{bits}. \tag{11.5}$$
- Dividing by $\Delta t$ gives the rate $R$ (approximation symbol dropped):
$$R = H/\Delta t \tag{11.6}$$
$$\;\;= r\log\frac{1}{r\,\Delta t}\ \text{bits/s}. \tag{11.7}$$
- Example, $r=50$ spikes/s, $\Delta t=0.001$ s:
$$R = 50\log\frac{1}{50\times0.001} = 216\ \text{bits/s}, \tag{11.8}$$
$$216/50 = 4.32\ \text{bits/spike}. \tag{11.9}$$
(p. 229)
- Why more than 1 bit per spike: on average 1 in 20 bins has a spike. A set of 20 bins has about 20 equally probable states, so entropy of about $\log 20 = 4.32$ bits per set, with one spike per set (p. 230).
- Temporal precision $\Delta t$ bounds the capacity, both for observers and for downstream neurons (p. 229).

*Intuition note.* A spike is rare in time, so its timing is surprising. Rare and precisely timed events carry several bits each.

- **Output entropy is not input information.** Output entropy is an upper bound on mutual information with the input, but gives no guarantee that the output informs about the input (p. 230).
- **Cricket** (Warland et al. 1992): entropy about 600 bits/s, of which about half relates to the input and half is noise. So about 300 bits/s, coding efficiency about 0.5 (p. 230).
- Taken literally, 300 bits in a second would specify the input to one part in $2^{300}\approx 2\times10^{90}$, which the author calls silly. **Rieke et al.'s alternative:** the neuron gives a "running commentary", about 3 bits per 10 ms, i.e. one part in $2^3=8$. Example: for speeds 0–32 degrees/s, one eighth is 4 degrees/s, so "20 ± 2 degrees/s" (p. 230–231).
- **Frog auditory system:** coding efficiency was about 20% with artificial sounds and 90% with naturalistic calls (p. 231).

**Eyes, flies, and information theory.** Laughlin (1981) showed that neurons receiving outputs from the eye communicate about as much information as theoretically possible, in fly eyes, and later work suggests also in human eyes (p. 231). He recorded from fly large monopolar cells (LMCs), which respond to contrast with continuous voltages (p. 231–232).
- **Question 1:** what encoding function would send the most information through a channel with fixed bounds? LMC outputs range from $-20$ to $+20$ mV, rescaled to $[0,1]$. By Section 7.7, the optimal encoder is the cdf of the contrast pdf $p_s(s)$:
$$g^*(s)=\int_{t=-\infty}^{s} p_s(t)\,dt. \tag{11.10}$$
It turns $p_s$ into a uniform $p_x(x)$, a maximum-entropy pdf, so each output value carries as much information as possible. He estimated $p_s$ by a histogram of woodland contrasts and integrated it numerically (p. 233).
- **Question 2:** does the LMC encoding $g$ match $g^*$? He measured mean LMC response to controlled contrasts. It rose slowly, then faster, then tailed off. After rescaling, the match to $g^*$ is "remarkably good" (Figure 11.3) (p. 233–234).
- This is described as one of the first tests of an optimality principle, the efficient coding hypothesis. It has been supported in other organisms (including humans) and senses (olfaction, audition). Friston's free-energy theory assumes behaviour minimises the sum of future surprises (sensory entropy) (p. 234).

*Intuition note.* If the output range is fixed, the best use is to make all output levels equally likely. A cdf-shaped curve does this: it spends many output levels on common contrasts and few on rare ones.

**The colour of information.**
- The eye has about 126 million photoreceptors (120 million rods, 6 million cones). There are three cone types (L, M, S). The L and M tuning curves are very similar. The text calls them red, green and blue (p. 235).
- About 126 million receptors feed one million optic-nerve fibres, a severe bottleneck (p. 235).
- Neighbouring red and green cones give similar outputs, so private fibres would send almost the same message twice, wasting capacity (p. 236).
- **Sum–difference recoding:** one fibre carries $g_{R+G}=r_R+r_G$, another $g_{R-G}=r_R-r_G$. This is also what principal component analysis gives. If cone outputs are Gaussian, it yields independent messages (p. 236–237).
- Evidence: ganglion cells in the retina collate neighbouring photoreceptors. The scatter plot (Figure 11.6b) of sum vs difference covers the plane almost uniformly, which suggests independence. Capacity is fully used only if outputs are also independent over time, and there is evidence for this (p. 237).
- Using separate ganglion cells for red and green "necessarily wastes" some capacity, whereas sum–difference recoding does not (p. 237).

**The brain: an efficient encoder.** The author says these experiments and analyses suggest that the brain's information processing is about as efficient as it possibly can be. He cites Rieke et al.: rates are "very large, close to the physical limits imposed by the spike train entropy" (p. 237). Without information theory we could not measure neural performance in absolute terms (p. 237).

### 11.7 A Very Short History of Information Theory
Shannon built on Boltzmann (1875) and Gibbs (1902) (thermodynamic entropy), Wiener (1927), Nyquist (1928) and Hartley (1928). He alone produced a complete mathematical theory, which may otherwise have taken decades (p. 238).

### 11.8 Summary
The author calls information theory a candidate for Wheeler's "simple idea". He quotes Wheeler's proposal that the universe is made of information, with matter and energy incidental (p. 238). The Further Reading list (pp. 239–240) names textbooks and popular books, including Cover and Thomas, MacKay, Pierce, and Shannon and Weaver.

## Toy example (ours, not from the text)
Laughlin's cdf encoder on a simple contrast distribution. Let contrast $s\in[0,1]$ have pdf $p_s(s)=2s$.
1. The cdf is $g^*(s)=\int_0^s 2t\,dt = s^2$, so the encoder is $x=s^2$.
2. Split the output range $[0,1]$ into four equal bins of width 0.25. The edges $x=0.25,0.5,0.75$ correspond to $s=\sqrt{0.25}=0.5$, $\sqrt{0.5}\approx0.7071$ and $\sqrt{0.75}\approx0.8660$.
3. The probability of each bin is the cdf difference. $P(s\le0.5)=0.5^2=0.25$. $P(0.5<s\le0.7071)=0.7071^2-0.25=0.5-0.25=0.25$. $P(0.7071<s\le0.8660)=0.75-0.5=0.25$. $P(0.8660<s\le1)=1-0.75=0.25$.
4. All four output bins are equally likely, as a uniform $p_x(x)$ requires. Common contrasts (large $s$, where $p_s$ is high) are spread over many output levels, and rare small contrasts are squeezed into a few.

## Concepts
- [[efficient-coding-hypothesis]] (new) — data acquired by the eye should be encoded as efficiently as possible before being sent to the brain (the text also reports tests on other senses) (p. 227)
- [[entropy]] — average Shannon information; applied to spike trains as the log of the number of possible trains (p. 228–229)
- [[bit]] — here also identified with one nucleotide in MacKay's model; the author notes bit and binary digit are used loosely (p. 218, 222)
- [[channel-capacity]] — for a noiseless binary channel, $C=1/\Delta t$ bits/s; 19.2 Mb/s for the satellite link (p. 218, 228)
- [[redundancy]] — spatial and temporal similarity in images, removed to compress; small redundancy re-added for error protection (p. 218, 220)
- [[mutual-information]] — information the neuron's output carries about its input, bounded by output entropy (p. 230)
- [[maximum-entropy-principle]] — a uniform pdf has maximum entropy, so a cdf encoder maximises information per output value (p. 233)
- [[error-correcting-code]] — a small amount of redundancy added to compressed TV data (p. 218, 220)
- [[huffman-arithmetic-coding]] — Huffman coding is the text's example of recoding so that symbols occur equally often (p. 218)
- [[lossy-vs-lossless-compression]] (new) — lossy discards information, lossless keeps all (p. 220)
- [[sum-difference-recoding]] (new) — sending sum and difference of correlated signals; gives independent messages for Gaussian cone outputs (p. 236)
- [[cdf-optimal-encoding]] (new) — optimal encoder for a bounded channel is the cdf of the input pdf (p. 233)

## Canonical instances
- [[tv-satellite-compression]] — 1.5 Gb/s into 19.2 Mb/s, compression factor about 78 (p. 218–219)
- [[mackay-sex-model]] — information gain of up to $\sqrt N$ vs one bit per generation (p. 223)
- [[genome-information-bound]] — $H=2N=6\times10^9$ bits (p. 225)
- [[dna-vs-synapses]] — $10^9$ vs $10^{15}$; brain must learn (p. 226)
- [[spike-train-entropy]] — 216 bits/s, 4.32 bits/spike at 50 spikes/s (p. 229–230)
- [[laughlin-fly-lmc]] — LMC response matches the contrast cdf (p. 232–234)
- [[cone-sum-difference]] — red/green recoding in ganglion cells (p. 236–237)

## Bridges (candidates)
- [same-math] cdf encoder $g^*(s)=\int p_s$ giving uniform output ↔ statistics: probability integral transform / histogram equalisation — the same transformation of a variable into a uniform one.
- [same-math] sum–difference recoding ↔ statistics: principal component analysis — the source says the recoding is also obtained by PCA.
- [structural-analogy] 126 million receptors into 1 million fibres ↔ information bottleneck — compress while keeping what matters.
- [structural-analogy] genome gaining bits from selection ↔ Kelly criterion/doubling rate — both treat growth as information gained about an environment (the source does not make this link).
- [metaphor] "Universe is made of information" (Wheeler) ↔ Landauer's principle — information treated as physically fundamental.

## Questions this raises
- How robust is MacKay's $\sqrt N$ result to changes in his stripped-down good/bad nucleotide model?
- How is coding efficiency (such as 0.5 for cricket, 20% vs 90% in frogs) measured in practice, and why does it depend on the stimulus?
- If cone outputs are not Gaussian, does sum–difference recoding still give independence, or only decorrelation?
- Does the "maximise information per joule" law for genomes have direct empirical tests?

## Reading notes
- Printed = pdf − 16 (pdf 233 = printed 217). I used printed numbers.
- Likely numerical error on p. 223: $\sqrt{3\times10^9}\approx 54{,}800$, but the text says 540,000 bits/generation. I report the text's value as printed and flag it. The "$\approx1{,}000$" toy value on p. 224 is correct.
- Section 11.4: "almost one gigabyte" is stated as in the text (6×10^9 / 8×10^9 binary digits ≈ 0.75 GB).
- Typo on p. 237: "using ... using". Several source numbers are rounded ($10^9$ synapses; 216 bits/s).
- Figure 11.1: I read the sexual curve as plateauing near 930 and the asexual near 710 in the image. The text gives no values.
- This unit has no exercises. Pp. 239–240 are a Further Reading list, summarised in one line.
