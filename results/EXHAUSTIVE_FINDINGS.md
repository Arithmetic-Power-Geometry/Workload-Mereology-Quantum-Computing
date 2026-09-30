# Exhaustive Workload–Mereology Findings

Seed: 2026  
Samples per parameter point: 500  
Parameter points: 105  
Total random instances: 52,500

## Interaction-crossing benchmark

For the original finite random-graph benchmark, the largest observed strict-compromise fraction occurs at:

- system size: n = 8
- physical/workload correlation: 0.0
- workload reuse: r = 2.0
- physical/task optimum conflict fraction: 96.8%
- physical endpoint selected: 28.2%
- task endpoint selected: 27.6%
- strict compromise selected: 44.2%

A strict compromise is a joint optimum equal to neither the physical-only optimum nor the task-only optimum.

For n = 8 and zero physical/workload correlation:

| reuse r | physical | task | compromise |
|---:|---:|---:|---:|
| 0.5 | 72.4% | 6.4% | 21.2% |
| 1.0 | 53.6% | 12.2% | 34.2% |
| 2.0 | 28.2% | 27.6% | 44.2% |
| 4.0 | 11.0% | 52.8% | 36.2% |
| 8.0 | 5.6% | 71.8% | 22.6% |

At n = 6, correlation = 0 and r = 2, the observed strict-compromise fraction is 23.6%.

## Interpretation

The benchmark demonstrates a finite-size regime in which independently optimal physical and task partitions frequently disagree and their weighted joint objective can select a third balanced partition. The strict-compromise fraction peaks at intermediate workload pressure in this ensemble.

This interaction-crossing benchmark is complemented by the OQM Gaussian-scrambling and noncommuting Hamiltonian controls elsewhere in the repository. The results do not establish quantum speedup, a new law of quantum mechanics, a thermodynamic phase transition, an asymptotic scaling law, or a complexity-class separation.

## Associated research record

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233
