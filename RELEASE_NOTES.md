# Workload–Mereology Quantum Computing v1.0.0

This release provides the research software, theory implementation, computational experiments, tests, and reproducibility materials for workload-dependent quantum subsystem selection.

The framework combines the Gaussian scrambling criterion of Operational Quantum Mereology with computational task cost. Candidate tensor-product structures are represented in normalized physical-cost/task-cost space, and workload-dependent optima are characterized by exposed points of the lower convex hull.

The release includes an analytic four-qubit construction, exhaustive balanced-bipartition studies, dimensionless controls, multiple coupling distributions, and generic noncommuting anisotropic XX+YY+ZZ Hamiltonian experiments.

At equal normalized pressure (lambda = 1), the n = 10 Pauli-ZZ experiments select a strict compromise factorization in 61.33% of 300 instances for uniform couplings, 60.67% for normal couplings, and 61.33% for lognormal couplings. In the generic noncommuting n = 10 experiment, 177 of 300 instances select a strict compromise factorization (59.00%), while the physical-only and task-only optima differ in 99.0% of instances.

The results concern finite-size workload-dependent subsystem selection in the tested ensembles. They do not establish quantum speedup, a new law of quantum mechanics, an asymptotic scaling law, or a complexity-class separation.

Reproducibility materials include fixed-seed workflows, raw numerical outputs, statistical summaries, tests, dependencies, experiment scripts, and figure-generation routines.

## Associated research record

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233

Copyright © 2026 Mohammad Amir Khusru Akhtar.  
Licensed under the Apache License, Version 2.0.
