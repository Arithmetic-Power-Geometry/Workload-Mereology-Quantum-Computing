# OQM Gaussian-Scrambling Validation

Reproducibility run: 36589754647  
Artifact SHA-256: 33ec32066f859bd317021459171fe1273d99a07df6228959195b626d6c0b356f  
Seed: 2026  
Samples per parameter point: 500  
Parameter points: 105  
Total random instances: 52,500

## Criterion

This experiment replaces the squared interaction-crossing surrogate by the Operational Quantum Mereology short-time Gaussian scrambling rate

tau_s^{-1} = D(H/sqrt(d), A + A').

For the Pauli-ZZ Hamiltonian ensemble used here, orthogonality of Pauli strings gives

tau_s^{-1}(F) = sqrt(sum_cross J_ij^2).

The joint objective is

J(F) = tau_s^{-1}(F) + r C_T(F).

## Main result

The largest observed compromise fraction occurred at:

- n = 8
- physical/workload correlation = 0.0
- reuse r = 0.5
- physical/task optimum conflict fraction = 0.968
- physical endpoint selected = 0.266
- task endpoint selected = 0.316
- compromise partition selected = 0.418

A compromise partition is a joint optimum equal to neither the OQM physical optimum nor the task-only optimum.

## Comparison with the earlier squared-strength surrogate

Earlier peak compromise fraction: 0.442.
OQM Gaussian-rate peak compromise fraction: 0.418.
Absolute peak reduction: 0.024.

The location in r shifts because sqrt(sum J^2), rather than sum J^2, changes the relative scale of the physical term. The important qualitative result survives: an intermediate joint optimum is common in the n=8 independent-graph ensemble.

## Interpretation

This is evidence for robustness of the workload–mereology compromise under the published OQM short-time subsystem-selection criterion, specialized to Pauli-ZZ Hamiltonians.

It is not evidence of quantum speedup, a new law of quantum mechanics, or a complexity-class separation. Further controls should vary Hamiltonian operator families, graph ensembles, normalization of task cost, and system size.
