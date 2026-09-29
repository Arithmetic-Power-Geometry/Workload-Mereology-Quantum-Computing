# Workload–Mereology Quantum Computing

A reproducible research software project for studying **competition between physically natural quantum subsystem structure and workload-optimal computational subsystem structure**.

The project tests a narrow hypothesis: a quantum processor may face a trade-off between **physical naturalness** (scrambling/interaction cost), **computational utility** (task cost), **error**, and **refactorization cost**.

It does **not** claim new quantum mechanics, computation beyond BQP, or a demonstrated quantum speedup.

## Core objective

For factorization `F`,

`J(F) = r C_T(F) + alpha S(F) + beta E(F) + W(F_old,F)`.

For two candidates `F_a,F_b`, if `F_b` reduces task cost by `Delta C > 0`, the break-even reuse level is

`r_c = (Delta W + alpha Delta S + beta Delta E) / Delta C`.

## Four-qubit benchmark

Reference Hamiltonian:

`H = J (Z1 Z2 + Z3 Z4)`.

Candidates:
- physical: `F_P = (12)|(34)`
- workload: `F_C = (13)|(24)`

For Heisenberg evolution of `X1`,

`X1(t) = X1 cos(2 J t) - Y1 Z2 sin(2 J t)`.

Relative to `F_P`, support stays within factor `(12)`; relative to `F_C`, the second term crosses factors. The benchmark uses

`S_P(t)=0`, `S_C(t)=sin^2(2 J t)`.

With task costs 10 and 2,

`r_c(t) = [W + alpha sin^2(2 J t) + beta Delta E] / 8`.

## Research scope

The software tests four questions: whether workload-optimal and dynamics-optimal factorizations differ; whether an intermediate compromise factorization emerges with three or more candidates; whether results survive established scrambling metrics; and whether benefits remain after all adaptation costs are charged.

## Prior-art boundary

This repository does not claim novelty for generalized tensor-product structures, minimal-scrambling subsystem selection, mereological quantum phase transitions, quantum code switching, workload-aware qubit placement/routing, or adaptive quantum hardware. The candidate contribution is the **joint competition between workload cost and quantum subsystem naturalness**.

## Run

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
python scripts/run_experiments.py --out artifacts
```

GitHub Actions runs the tests and publishes the generated result bundle as a workflow artifact.

## License

Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.


## Current validated result

The current reproducible benchmark includes commuting Pauli-ZZ and generic noncommuting anisotropic XX+YY+ZZ Hamiltonian ensembles. Under the dimensionless objective

`J_lambda(F) = S_hat_OQM(F) + lambda C_hat_T(F)`,

the noncommuting n=10 experiment selected a strict compromise factorization in 177/300 instances (59.0%) at lambda=1 (seed 2029). The physical and task-only optima differed in 99.0% of those instances. See `results/NONCOMMUTING_FINDINGS.md`.

The result is a finite-size computational finding about workload-dependent subsystem selection. It is not a claim of quantum speedup, a new law of quantum mechanics, or a complexity-class separation.


## Reproducible benchmark summary

Under the dimensionless OQM objective, the n=10 Pauli-ZZ control at lambda=1 selects a strict compromise factorization in 61.33% of 300 instances for uniform and lognormal coupling ensembles and 60.67% for the normal ensemble. In the generic noncommuting anisotropic XX+YY+ZZ control, the strict-compromise fraction at lambda=1 is 21.33% for n=6, 41.33% for n=8, and 59.00% for n=10.

These are finite-size reproducibility results from fixed-seed workflow artifacts. They do not establish an asymptotic scaling law, quantum speedup, or new quantum mechanics.
