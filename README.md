# Workload–Mereology Quantum Computing

A research software and reproducibility repository for **workload-dependent quantum subsystem selection**, where computational task locality competes with dynamical naturalness measured through quantum scrambling.

The framework studies candidate generalized tensor-product structures using the dimensionless objective

[
J_\lambda(F)=\widehat S_{\mathrm{OQM}}(F)+\lambda\widehat C_T(F),
]

where \(\widehat S_{\mathrm{OQM}}\) is normalized physical cost derived from the Gaussian scrambling criterion of Operational Quantum Mereology and \(\widehat C_T\) is normalized task cost.

## Scientific scope

A physically natural factorization and a task-optimal factorization need not coincide. For a finite candidate family, workload-dependent optima are characterized geometrically by exposed points of the lower convex hull in physical-cost/task-cost space. A strict intermediate lower-hull vertex can therefore become uniquely optimal over a nonempty interval of workload pressure.

The repository contains:

- analytic four-qubit constructions;
- lower-convex-envelope theory;
- Operational Quantum Mereology scrambling calculations;
- exhaustive balanced-bipartition experiments;
- commuting Pauli-ZZ controls across multiple coupling distributions;
- generic noncommuting anisotropic XX+YY+ZZ controls;
- fixed-seed tests, experiment scripts, numerical summaries, and figure-generation code.

The framework does not modify quantum mechanics and does not claim quantum speedup, computation beyond BQP, or a complexity-class separation.

## Four-qubit construction

For

[
H=J(Z_1Z_2+Z_3Z_4),
]

consider the physical grouping \(F_P=(12)|(34)\) and workload grouping \(F_C=(13)|(24)\). Heisenberg evolution gives

[
X_1(t)=X_1\cos(2Jt)-Y_1Z_2\sin(2Jt).
]

Relative to \(F_P\), support remains within subsystem \((12)\); relative to \(F_C\), the second term crosses factors. With task costs 10 and 2, the corresponding transition condition can be written

[
r_c(t)=\frac{W+\alpha\sin^2(2Jt)+\beta\Delta E}{8}.
]

## Reproducible results

Under the dimensionless OQM objective, the \(n=10\), \(\lambda=1\) Pauli-ZZ experiments select a strict compromise factorization in **61.33%** of 300 instances for uniform couplings, **60.67%** for normal couplings, and **61.33%** for lognormal couplings.

For generic noncommuting anisotropic XX+YY+ZZ Hamiltonians at \(\lambda=1\), the strict-compromise fraction is **21.33%** at \(n=6\), **41.33%** at \(n=8\), and **59.00%** at \(n=10\). At \(n=10\), this corresponds to **177/300** instances; the physical-only and task-only optima differ in **99.0%** of instances.

The OQM Gaussian-scrambling control reaches a **38.4%** compromise fraction at \(n=8\), zero physical/workload correlation, and workload pressure \(r=0.25\).

These are finite-size computational results for the tested ensembles; they do not establish an asymptotic scaling law.

## Reproduction

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
python scripts/run_experiments.py --out artifacts
```

GitHub Actions executes the reproducibility workflow and publishes the resulting numerical bundle as a workflow artifact.

## Citation

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233

DOI: https://doi.org/10.5281/zenodo.23053233

Citation metadata are also provided in `CITATION.cff`.

## License

The research software is released under the Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
