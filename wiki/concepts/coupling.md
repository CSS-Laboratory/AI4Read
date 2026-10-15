---
id: coupling
type: concept
fields: [control-theory, information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch04-machine, polyanskiy-2025-information/ch08-f-p1]
generated_by: build_kg.py
---

# coupling

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch04-machine]] (p. 49): joining machines by making one's parameters functions of another's states or outputs (new)

### information-theory

- [[polyanskiy-2025-information/ch08-f-p1]] (p. 122): joint law with given marginals; TV is the minimal $P[X\ne Y]$ [new]

## Instances that use it

- [[cattle-herd-loose-coupling]] — loosely coupled systems and the D/T boundary — from [[ashby-1956-cybernetics/ch13-regulating]]
- [[uniform-coupling-counterexample]] — same chain, two couplings, coalescence time 1 versus infinity — from [[mackay-2003-information/ch32-exact]]
- [[ising-lattice-phase-transition]] — samples clump as coupling rises; $J_c\approx0.44$ for the square lattice — from [[murphy-2023-pml2/ch04-graphical-p2]]
- [[two-moons-spline-coupling-flow]] — masked coupling flow of rational quadratic splines fit to two moons — from [[murphy-2023-pml2/ch23-normalizing]]
- [[marton-divergence]] — $f=(1-x)_+^2$ with a coupling inf-form — from [[polyanskiy-2025-information/ch08-f-p2]]
- [[sinkhorn-coupling]] — for P_{X,Y}>0 and marginals without zeros, minimiser has form A(x)P(x,y)B(y) — from [[polyanskiy-2025-information/ch17-information]]
- [[glow-model]] — multi-scale coupling flow with $1\times1$ LU convolutions for faces — from [[prince-2023-udl/ch16-normalizing]]

## Candidate bridges

- [structural-analogy] coupling by setting the parameter as a function of the other machine's state ↔ control-theory: feedback law (state or output feedback) — the loop is closed by making input depend on state. — from [[ashby-1956-cybernetics/ch04-machine]] (control-theory → control-theory)
- [structural-analogy] power of veto ↔ control-theory: homeostasis through ultrastable coupling — part B blocks equilibria unacceptable to it. — from [[ashby-1956-cybernetics/ch05-stability]] (control-theory → control-theory)
- [same-math] TV coupling form (7.20) ↔ optimal transport: Wasserstein distance with Hamming cost. — from [[polyanskiy-2025-information/ch08-f-p1]] (information-theory → other)
- [structural-analogy] Near-decomposability ↔ complex-systems: time-scale separation between fast within-module and slow between-module dynamics — block-structured coupling gives two time scales (pp. 474–475). — from [[simon-1962-architecture/main]] (complex-systems → complex-systems)
- [structural-analogy] two-oscillator phase locking with compromise frequency ω* ↔ complex-systems: Kuramoto synchronization — sine-coupled phases lock when coupling beats frequency spread. — from [[strogatz-2024-nonlinear/ch08-bifurcations-p2]] (complex-systems → complex-systems)
