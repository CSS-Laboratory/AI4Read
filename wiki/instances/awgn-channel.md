---
id: awgn-channel
type: instance
fields: [information-theory]
n_sources: 7
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel]
raw_ids: [AWGN channel]
generated_by: build_kg.py
---

# awgn-channel

## Descriptions in the sources

### information-theory

- [[polyanskiy-2025-information/ch04-mutual]] (p. 48): $I=\frac12\log(1+\mathrm{SNR})$ for Gaussian input
- [[polyanskiy-2025-information/ch05-variational]] (p. 68): Gaussian Q upper-bounds $I(X;Y)$ by $\frac12\log(1+\sigma^2)$
- [[polyanskiy-2025-information/ch06-extremization]] (pp. 98, 100): $I(X;X+Z)$ with $Z$ Gaussian; $C=\frac12\log(1+\sigma_X^2/\sigma_N^2)$ [new]
- [[polyanskiy-2025-information/ch21-channel]] (p. 372): non-discrete, stationary memoryless, additive-noise example [as `AWGN channel`]
- [[polyanskiy-2025-information/ch23-capacity]] (pp. 410–412): $E_b/N_0=-1.59$ dB
- [[polyanskiy-2025-information/ch24-strong]] (p. 427, 437): strong converse holds (Ex. IV.33); dispersion $\frac{P(P+2)}{2(P+1)^2}\log^2e$
- [[polyanskiy-2025-information/ch25-channel]] (pp. 457–459): Elias and Schalkwijk–Kailath schemes under an expected power constraint
