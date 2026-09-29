# Noncommuting Hamiltonian Validation

Reproducibility run: 36591050482  
Artifact SHA-256: 3cc883657f31abb5e1a4d53d583d08b72c11429285236b2316f188ec75d40401  
Seed: 2029  
Samples per parameter point: 300

## Hamiltonian family

The control replaces the commuting ZZ ensemble with generic anisotropic two-body Pauli Hamiltonians

H = sum_ij [Jx_ij X_i X_j + Jy_ij Y_i Y_j + Jz_ij Z_i Z_j],

with independently sampled coefficients. These terms are generally noncommuting.

For a tensor-product bipartition, distinct Pauli strings are Hilbert-Schmidt orthogonal, so the OQM Gaussian scrambling distance retains exactly the crossing Pauli terms.

## Dimensionless objective

J_lambda(F) = S_hat_OQM(F) + lambda C_hat_T(F).

Both terms are normalized across the candidate factorization family on each instance.

## Main result

The largest observed compromise fraction is:

- n = 10
- lambda = 1
- samples = 300
- physical/task optimum conflict fraction = 0.990
- physical endpoint selected = 0.2933333333
- task endpoint selected = 0.1166666667
- compromise factorization selected = 0.5900000000

Thus 177 of 300 instances selected a factorization equal to neither endpoint optimum.

A Wilson 95% confidence interval for 168/300 is approximately [0.534, 0.644].

## Interpretation

The workload-mereology compromise survives a move from commuting ZZ interactions to generic noncommuting XX+YY+ZZ interactions. The maximum again occurs at lambda = 1, where normalized physical and workload pressures have equal coefficient.

This supports robustness within the tested finite-size random ensembles. It does not establish an asymptotic law, quantum speedup, or new quantum mechanics.
