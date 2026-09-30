# Workload–Mereology Competition Theory

## 1. Setting

Let \(\mathcal H\) be a finite-dimensional Hilbert space and let \(F\) range over a finite family of candidate generalized tensor-product structures or computational factorizations. A factorization determines which operations are local with respect to both physical information flow and task execution.

A physically natural factorization and a computationally useful factorization need not coincide.

## 2. Cost components

For workload \(T\) and factorization \(F\):

- \(C_T(F)\ge 0\): task cost;
- \(S_H(F,t)\ge 0\): scrambling or physical incompatibility cost;
- \(E(F,t)\ge 0\): error or implementation cost;
- \(W(F,F')\ge 0\): refactorization cost.

A general objective is

[
J(F;r,t)=rC_T(F)+\alpha S_H(F,t)+\beta E(F,t)+W(F_{\mathrm{old}},F).
]

## 3. Pairwise transition identity

For candidates \(F_a,F_b\), define

[
\Delta C=C_T(F_a)-C_T(F_b)>0,
]

[
\Delta S=S_H(F_b,t)-S_H(F_a,t),
]

[
\Delta E=E(F_b,t)-E(F_a,t),
]

and

[
\Delta W=W(F_{\mathrm{old}},F_b)-W(F_{\mathrm{old}},F_a).
]

Then \(J(F_b)<J(F_a)\) exactly when

[
r\Delta C>\Delta W+\alpha\Delta S+\beta\Delta E.
]

When the numerator is nonnegative, the break-even workload pressure is

[
r_c(t)=\frac{\Delta W+\alpha\Delta S+\beta\Delta E}{\Delta C}.
]

This is a cost-comparison identity, not a computational-complexity separation.

## 4. Four-qubit construction

Take

[
H=J(Z_1Z_2+Z_3Z_4),
]

with

[
F_P=(12)|(34),\qquad F_C=(13)|(24).
]

Heisenberg evolution gives

[
X_1(t)=X_1\cos(2Jt)-Y_1Z_2\sin(2Jt).
]

Relative to \(F_P\), both terms remain within factor \((12)\). Relative to \(F_C\), the \(Y_1Z_2\) term crosses the two factors. For the reference cross-factor support proxy,

[
S(F_P,t)=0,\qquad S(F_C,t)=\sin^2(2Jt).
]

If \(C_T(F_P)=10\) and \(C_T(F_C)=2\), then

[
r_c(t)=\frac{W+\alpha\sin^2(2Jt)+\beta\Delta E}{8}.
]

At short time,

[
\sin^2(2Jt)=4J^2t^2+O(t^4).
]

## 5. Dimensionless OQM objective

For each instance, physical and task costs are normalized across the candidate family:

[
\widehat S(F)=\frac{S(F)-S_{\min}}{S_{\max}-S_{\min}},
\qquad
\widehat C_T(F)=\frac{C_T(F)-C_{\min}}{C_{\max}-C_{\min}}.
]

The dimensionless workload–mereology objective is

[
J_\lambda(F)=\widehat S_{\mathrm{OQM}}(F)+\lambda\widehat C_T(F),
\qquad \lambda>0.
]

For the OQM Gaussian criterion,

[
\tau_s^{-1}(H,\mathcal A)=D(H/\sqrt d,\mathcal A+\mathcal A').
]

For the Pauli-ZZ bipartition experiments, Hilbert-Schmidt orthogonality reduces the squared Gaussian scrambling rate to the sum of squared coefficients of crossing terms.

## 6. Lower-convex-envelope theorem

For a finite candidate family \(\mathcal F\), associate each factorization \(F\) with

[
P_F=(C_F,S_F),
]

where \(C_F\) and \(S_F\) are normalized task and physical costs. Define

[
J_\lambda(F)=S_F+\lambda C_F.
]

### Theorem: exposed-factorization criterion

A factorization \(F\) is the unique minimizer of \(J_\lambda\) for some \(\lambda>0\) if and only if \(P_F\) is an exposed point of the lower convex hull of \(\{P_G:G\in\mathcal F\}\) with a supporting line of negative slope.

**Proof.** Minimizing \(S+\lambda C\) is equivalent to minimizing the linear functional \(\langle(\lambda,1),(C,S)\rangle\). A point is the unique minimizer of a linear functional exactly when it is exposed by the corresponding supporting line. Since \(\lambda>0\), the supporting line \(S+\lambda C=k\) has slope \(-\lambda<0\). Conversely, any lower-hull exposed point with a negative-slope supporting line supplies a positive \(\lambda\) for which that factorization uniquely minimizes the objective. \(\square\)

### Corollary: strict-compromise interval

Let \(F_P\) minimize physical cost and \(F_T\) minimize task cost. A third factorization \(F_C\notin\{F_P,F_T\}\) is uniquely optimal on a nonempty open interval of workload pressures when its point is a strict intermediate vertex of the lower convex hull.

For three hull vertices ordered by decreasing task cost,

[
P_P=(C_P,S_P),\quad P_C=(C_C,S_C),\quad P_T=(C_T,S_T),
]

with \(C_P>C_C>C_T\) and \(S_P<S_C<S_T\), the transition pressures are

[
\lambda_{P\to C}=\frac{S_C-S_P}{C_P-C_C},
\qquad
\lambda_{C\to T}=\frac{S_T-S_C}{C_C-C_T}.
]

The strict compromise occupies a nonempty interval exactly when

[
\lambda_{P\to C}<\lambda_{C\to T}.
]

The geometric statement is independent of the four-qubit construction; the quantum content enters through the physical-cost functional.

## 7. Noncommuting extension

For

[
H=\sum_{ij}\left(J^x_{ij}X_iX_j+J^y_{ij}Y_iY_j+J^z_{ij}Z_iZ_j\right),
]

overlapping two-body Pauli terms with different axes are generally noncommuting. Distinct Pauli strings remain Hilbert-Schmidt orthogonal, so for a candidate bipartition the OQM Gaussian cost is determined by the crossing Pauli terms.

The finite-size noncommuting experiments retain substantial strict-compromise selection, including 177/300 instances at n = 10 and lambda = 1.

## 8. Scope

The framework is a variational theory of task-dependent quantum subsystem organization. It does not introduce a new qubit or modify quantum mechanics, and it does not establish quantum speedup, computation beyond BQP, an asymptotic scaling law, or a complexity-class separation.

## Associated research record

Akhtar, M. A. K. (2026). *Workload–Mereology Quantum Computing: When Computational Demand Changes the Preferred Quantum Subsystem Structure* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23053233
