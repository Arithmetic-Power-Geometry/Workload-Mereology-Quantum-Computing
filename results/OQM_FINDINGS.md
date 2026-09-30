# OQM Gaussian-Scrambling Validation

## Criterion

The physical-cost control uses the Operational Quantum Mereology short-time Gaussian scrambling rate

[
\tau_s^{-1}=D(H/\sqrt d,\mathcal A+\mathcal A').
]

For the Pauli-ZZ Hamiltonian ensemble, Hilbert-Schmidt orthogonality gives

[
\tau_s^{-1}(F)=\sqrt{\sum_{\mathrm{cross}}J_{ij}^2}.
]

The joint finite-size benchmark combines this physical cost with workload task cost.

## Validated result

In the final OQM control reported with the research record, the largest observed strict-compromise fraction is **38.4%** at:

- system size: n = 8
- physical/workload correlation: 0.0
- workload pressure: r = 0.25

A strict compromise is a joint optimum equal to neither the OQM physical-only optimum nor the task-only optimum.

## Interpretation

The result shows that the intermediate-factorization regime persists when physical cost is evaluated using the OQM Gaussian scrambling criterion rather than only a squared interaction-crossing surrogate.

This is a finite-size result for the tested random ensembles. It does not establish quantum speedup, a new law of quantum mechanics, a thermodynamic phase transition, an asymptotic scaling law, or a complexity-class separation.

## Associated research record

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233
