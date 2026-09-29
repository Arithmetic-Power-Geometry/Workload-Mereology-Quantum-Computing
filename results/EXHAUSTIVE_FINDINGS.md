# Exhaustive Workload–Mereology Findings

Reproducibility run: 36588275996  
Seed: 2026  
Samples per parameter point: 500  
Parameter points: 105  
Total random instances: 52,500

## Main observed regime

The largest observed compromise fraction occurred at:

- system size: n = 8
- physical/workload correlation: 0.0
- workload reuse: r = 2.0
- physical/task optimum conflict fraction: 0.968
- physical endpoint selected by joint objective: 0.282
- task endpoint selected by joint objective: 0.276
- compromise partition selected: 0.442

A compromise partition is defined strictly as a joint optimum that equals neither the physical-only optimum nor the task-only optimum.

## Scaling evidence

The effect is not confined to the four-site construction. At n = 6, correlation = 0 and r = 2, the observed compromise fraction was 0.236. At n = 8 under the same correlation and reuse, it rose to 0.442.

For n = 8 and correlation = 0:

| reuse r | physical | task | compromise |
|---:|---:|---:|---:|
| 0.5 | 0.724 | 0.064 | 0.212 |
| 1.0 | 0.536 | 0.122 | 0.342 |
| 2.0 | 0.282 | 0.276 | 0.442 |
| 4.0 | 0.110 | 0.528 | 0.362 |
| 8.0 | 0.056 | 0.718 | 0.226 |

This gives a reproducible finite-size pattern in which the compromise fraction peaks at intermediate workload pressure for this ensemble.

## Interpretation boundary

This result establishes a property of the defined finite random-graph benchmark:

1. independently optimal physical and task partitions frequently disagree;
2. minimizing their weighted joint objective can select a third balanced partition;
3. this third-partition regime can be substantial and can increase from n=6 to n=8 in the tested ensemble.

It does not establish quantum speedup, a new law of quantum mechanics, a thermodynamic phase transition, or a complexity-class separation.

The next validation target is replacement of the interaction-crossing surrogate by the published algebraic-OTOC/Gaussian scrambling functional, followed by larger-size and alternative-ensemble controls.
