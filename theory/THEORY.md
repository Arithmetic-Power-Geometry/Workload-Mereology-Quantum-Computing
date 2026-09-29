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


## Lower-envelope theorem for workload–mereology selection

For a finite candidate family \(\mathcal F\), associate each factorization \(F\) with

\[
P_F=(C_F,S_F),
\]

where \(C_F\) is normalized task cost and \(S_F\) is normalized physical/OQM scrambling cost. For \(\lambda>0\), define

\[
J_\lambda(F)=S_F+\lambda C_F.
\]

### Theorem (exposed-factorization criterion)

A factorization \(F\) is the unique minimizer of \(J_\lambda\) for some \(\lambda>0\) if and only if \(P_F\) is an exposed point of the lower convex hull of \(\{P_G:G\in\mathcal F\}\) with a supporting line of negative slope.

Proof. Minimizing \(S+\lambda C\) is minimizing the linear functional \(\langle(\lambda,1),(C,S)\rangle\). A point is the unique minimizer of a linear functional exactly when it is exposed by the corresponding supporting line. Since \(\lambda>0\), the supporting line \(S+\lambda C=k\) has slope \(-\lambda<0\). Conversely, any lower-hull exposed point with negative-slope supporting line supplies a positive \(\lambda\) for which that factorization uniquely minimizes the objective. \(\square\)

### Corollary (genuine compromise interval)

Let \(F_P\) minimize physical cost and \(F_T\) minimize task cost. A third factorization \(F_C\notin\{F_P,F_T\}\) is optimal on a nonempty open interval of workload pressures if its point is a strict intermediate vertex of the lower convex hull.

For three hull vertices ordered by decreasing task cost,
\[
P_P=(C_P,S_P),\quad P_C=(C_C,S_C),\quad P_T=(C_T,S_T),
\]
with \(C_P>C_C>C_T\) and \(S_P<S_C<S_T\), the two transition pressures are

\[
\lambda_{P\to C}=\frac{S_C-S_P}{C_P-C_C},
\qquad
\lambda_{C\to T}=\frac{S_T-S_C}{C_C-C_T}.
\]

The compromise occupies a nonempty interval precisely when

\[
\lambda_{P\to C}<\lambda_{C\to T}.
\]

This result is geometric and does not depend on the particular four-qubit construction. The quantum content enters through the definition of \(S_F\), for example the OQM Gaussian scrambling rate.
