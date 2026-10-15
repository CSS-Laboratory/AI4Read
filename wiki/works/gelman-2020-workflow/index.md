---
id: gelman-2020-workflow/index
work: gelman-2020-workflow
type: work-map
units: [gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p2, gelman-2020-workflow/main-p3]
---

# Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., Kennedy, L., Gabry, J., Bürkner, P.-C., & Modrák, M. (2020). *Bayesian Workflow*. arXiv:2011.01808.

## In one paragraph
The paper argues that applied Bayesian analysis is more than computing the posterior p(θ|y). It is an iterative, tangled workflow of building, fitting, checking, changing and comparing many models, and most of them will be flawed or discarded. Simulation from the prior, fake-data tests, computational diagnostics and predictive checks help find problems early. Computational trouble is often a sign of a modelling problem, so it should be investigated rather than worked around. Models are expanded step by step. They are compared in order to understand them, not only to pick a winner. Two case studies, golf putting and planetary motion, show the cycle in practice. The authors also admit the risks, such as using the data twice, and say that every workflow has holes.

## The path through the work
- [[gelman-2020-workflow/main-p1]] — Applied Bayesian analysis is a tangled, iterative workflow of building, checking, fixing and comparing many models, in which simulation, simpler models and quick approximate fits help to find problems early.
- [[gelman-2020-workflow/main-p2]] — After a model is fit, the workflow is a loop of fixing computation (often by adding prior information), checking the fit, expanding the model step by step, and comparing many fitted models to understand them rather than to pick one winner.
- [[gelman-2020-workflow/main-p3]] — The authors argue that Bayesian modeling is best done by building models step by step, using simple or fake-data versions and predictive checks to understand each failure, rather than fitting one fixed model and trusting the defaults.

## Big ideas across units
- **Workflow is bigger than inference.** Bayesian inference is the formulation and computation of the posterior. Workflow adds model building, checking, improvement and comparison. Units: main-p1, main-p2, main-p3.
- **Simulate before and around the data.** Prior predictive checks show what a prior implies. Fake-data simulation and simulation-based calibration check that known parameters can be recovered. Simple or fake-data versions of a model also explain failures. Units: main-p1, main-p2, main-p3.
- **Computational problems are modelling clues (the "folk theorem").** Poor mixing can be traced to difficult posterior geometry and weakly informative data. Debug by simplifying and by plotting. The golf misfit and the planetary multimodality were both diagnosed this way. Units: main-p1, main-p2, main-p3.
- **Computation is part of the model.** Approximate algorithms are approximations to a fuller workflow. Early on, "fail fast" is sensible. Later, accurate MCMC is needed. Starting points and slow runs carry information. Units: main-p1, main-p3.
- **Check models in layers.** Posterior predictive checks can reveal misfit but can be over-optimistic. Cross validation, LOO-PIT and prior-sensitivity tools add less optimistic checks. Units: main-p1, main-p2, main-p3.
- **Expand models step by step and compare them to understand them.** The authors use the topology of models, multiverse analysis, and stacking or projection predictive selection instead of picking one winner. Golf's error term is an example of such an expansion. Units: main-p2, main-p3.
- **Priors need real information, and a budget.** Substantive prior knowledge can fix computation, but it must not be tweaking until the sampler runs. There is a ladder from weakly informative to informative priors, and priors often must tighten as models grow. Units: main-p1, main-p2.
- **Iteration has costs, and every workflow has holes.** Using the data for checks creates a post-selection problem. The authors respond by building one richer model, and say bigger data need bigger models. Units: main-p2, main-p3.

## How to read it
- **Essential:** main-p1 sets the framework (Fig. 1 overview, prior predictive checks, generative models, fake-data simulation, the folk theorem). main-p2 is the core toolkit for checking, expanding and comparing models. Together they carry most of the conceptual content.
- **Read after the others:** main-p3 mostly shows the ideas at work in two case studies. It also holds the discussion, which covers post-selection inference, big data and the limits of workflow. The discussion is worth reading even if you skim the planetary example.
- **Dependencies:** main-p2 assumes the p1 ideas (HMC, divergences, funnels, stacking, the folk theorem). main-p3 assumes the earlier sections: predictive checks, convergence diagnostics and the start of the golf example from main-p2.
- **Can be skimmed on a first pass:** this is a judgment from the digests, not a statement in them. The software-development material (version control, testing) in main-p2 and the ODE details of the planetary example in main-p3 are the most self-contained parts.
- **Prerequisites listed in the digests:** prior, likelihood and posterior; basic MCMC (chains, mixing, R̂); regression; hierarchical models; leave-one-out cross validation.

## Concepts introduced
Ids are listed as given in the units. Some ids look like variants of one concept and are noted as such.

From main-p1:
- [[bayesian-workflow]] — main-p1
- [[bayesian-inference-vs-workflow]] — main-p1
- [[meta-workflow-codification]] — main-p1
- [[modular-model-construction]] — main-p1
- [[prior-predictive-check]] — main-p1
- [[generative-model]] — main-p1
- [[improper-prior-as-placeholder]] — main-p1
- [[markov-chain-monte-carlo-mcmc]] — main-p1 (main-p3 uses the variant id [[markov-chain-monte-carlo]])
- [[hamiltonian-monte-carlo-hmc-nuts]] — main-p1
- [[warmup]] — main-p1
- [[convergence-diagnostics-r-hat-ess-divergences]] — main-p1 (main-p2 and main-p3 use [[convergence-diagnostics]])
- [[approximate-algorithm-as-approximate-model]] — main-p1
- [[variational-inference-elbo]] — main-p1
- [[fit-fast-fail-fast]] — main-p1
- [[fake-data-simulation]] — main-p1
- [[simulation-based-calibration]] — main-p1
- [[folk-theorem-of-statistical-computing]] — main-p1 (main-p3 uses the variant [[folk-theorem-statistical-computing]])
- [[stacking]] — main-p1
- [[typical-set]] — main-p1
- [[partial-pooling-shrinkage]] — main-p1 (main-p3 uses the variant [[partial-pooling]])

From main-p2:
- [[posterior-predictive-check]] — main-p2
- [[cross-validation-loo-waic]] — main-p2
- [[loo-pit]] — main-p2
- [[funnel-geometry]] — main-p2
- [[reparameterization]] — main-p2
- [[marginalization-for-sampling]] — main-p2
- [[weakly-informative-prior-ladder]] — main-p2
- [[information-budget]] — main-p2
- [[static-sensitivity-analysis]] — main-p2
- [[topology-of-models]] — main-p2
- [[multiverse-analysis]] — main-p2
- [[projection-predictive-selection]] — main-p2
- [[convergence-diagnostics]] — main-p2

From main-p3:
- [[model-expansion]] — main-p3
- [[fudge-factor-error-term]] — main-p3
- [[likelihood]] — main-p3
- [[multimodal-posterior]] — main-p3
- [[post-selection-inference]] — main-p3
- [[garden-of-forking-paths]] — main-p3
- [[poststratification]] — main-p3
