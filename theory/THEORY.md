# Workload–Mereology Competition Theory

## 1. Setting

Let `H` be a finite-dimensional Hilbert space and let `F` range over candidate generalized tensor-product structures or computational factorizations. A factorization determines which operations are treated as local for both task execution and physical information flow.

The theory does not assume that a physically natural factorization and a computationally useful factorization coincide.

## 2. Cost components

For workload `T` and factorization `F`:

- `C_T(F) >= 0`: task execution cost.
- `S_H(F,t) >= 0`: scrambling/physical incompatibility cost.
- `E(F,t) >= 0`: error or implementation cost.
- `W(F,F') >= 0`: refactorization cost.

Define

`J(F;r,t) = r C_T(F) + alpha S_H(F,t) + beta E(F,t) + W(F_old,F)`.

## 3. Competition identity

For candidates `F_a,F_b`, let

`Delta C = C_T(F_a)-C_T(F_b) > 0`,

`Delta S = S_H(F_b,t)-S_H(F_a,t)`,

`Delta E = E(F_b,t)-E(F_a,t)`,

`Delta W = W(F_old,F_b)-W(F_old,F_a)`.

Then `J(F_b) < J(F_a)` iff

`r Delta C > Delta W + alpha Delta S + beta Delta E`.

Therefore, when the numerator is nonnegative,

`r_c(t) = [Delta W + alpha Delta S + beta Delta E] / Delta C`.

This is a comparison identity, not a computational-complexity separation.

## 4. Four-qubit benchmark

Take

`H = J (Z1 Z2 + Z3 Z4)`

and

`F_P=(12)|(34)`, `F_C=(13)|(24)`.

Heisenberg evolution gives

`X1(t)=X1 cos(2Jt)-Y1 Z2 sin(2Jt)`.

Relative to `F_P`, both terms are supported inside factor `(12)`. Relative to `F_C`, the `Y1 Z2` term spans both factors. The reference cross-factor support proxy is

`S(F_P,t)=0`,

`S(F_C,t)=sin^2(2Jt)`.

If `C_T(F_P)=10` and `C_T(F_C)=2`, then

`r_c(t)=[W + alpha sin^2(2Jt) + beta Delta E]/8`.

At short time, `sin^2(2Jt)=4J^2t^2+O(t^4)`.

## 5. Multi-factorization model

For candidates `F_1,...,F_m`, choose

`F*(r,t)=argmin_F J(F;r,t)`.

The lower envelope partitions parameter space into optimal-factorization regions. With at least three candidates, an intermediate factorization may become optimal even when it is neither the minimum-scrambling nor minimum-task-cost endpoint. This is a hypothesis to test, not an assumption.

## 6. Dynamic sequence

For tasks `T_1,...,T_N`, choose a sequence `F_t` minimizing

`sum_t [C_Tt(F_t)+alpha S_H(F_t,t)+beta E(F_t,t)] + lambda sum_t W(F_{t-1},F_t)`.

Generic service-plus-switching-cost optimization is established in online optimization. The quantum-specific question here is the subsystem algebra/factorization being traded against scrambling and workload cost.

## 7. Falsification criteria

The framework loses distinctiveness if the joint workload-plus-mereology objective is already standard; if every effect reduces exactly to ordinary fixed-logical-qubit placement; if realistic scrambling/noise removes all advantageous regimes after adaptation cost; or if a simpler established model predicts the same results without subsystem refactorization.

## 8. Claims deliberately not made

No claim is made of a new law of quantum mechanics, a new qubit, computation beyond BQP, inherent quantum speedup, novelty of generalized tensor-product structures, novelty of mereological phase transitions, or novelty of routing/code switching.

Current research claim: **quantum subsystem naturalness and workload utility can be studied in explicit competition through a joint cost functional.**
