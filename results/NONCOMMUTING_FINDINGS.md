# Noncommuting Hamiltonian Validation

Seed: 2029  
Samples per parameter point: 300

## Hamiltonian family

The noncommuting control uses generic anisotropic two-body Pauli Hamiltonians

[
H=\sum_{ij}\left(J^x_{ij}X_iX_j+J^y_{ij}Y_iY_j+J^z_{ij}Z_iZ_j\right),
]

with independently sampled coefficients. Overlapping terms with different Pauli axes are generally noncommuting.

For a tensor-product bipartition, distinct Pauli strings are Hilbert-Schmidt orthogonal, so the OQM Gaussian scrambling distance retains the crossing Pauli terms.

## Dimensionless objective

[
J_\lambda(F)=\widehat S_{\mathrm{OQM}}(F)+\lambda\widehat C_T(F).
]

Both terms are normalized across the candidate factorization family for each instance.

## Results

At \(\lambda=1\), the strict-compromise fraction is:

| system size | strict compromise |
|---:|---:|
| n = 6 | 21.33% |
| n = 8 | 41.33% |
| n = 10 | 59.00% |

For n = 10:

- samples: 300
- physical/task optimum conflict fraction: 99.0%
- physical endpoint selected: 29.33%
- task endpoint selected: 11.67%
- strict compromise selected: 59.00%
- strict compromise count: 177/300

The Wilson 95% confidence interval for 177/300 is approximately 53.4%–64.4%.

## Interpretation

Strict compromise selection remains substantial after replacing the commuting Pauli-ZZ family with generic noncommuting XX+YY+ZZ Hamiltonians. Within the tested ensembles, the result supports robustness of workload-dependent subsystem selection beyond the commuting construction.

The result is finite-size evidence and does not establish an asymptotic law, quantum speedup, new quantum mechanics, or a complexity-class separation.

## Associated research record

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233
