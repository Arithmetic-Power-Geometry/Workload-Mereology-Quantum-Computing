from __future__ import annotations
import math
from typing import Iterable
from .partition import Edge

def gaussian_scrambling_rate_pauli_zz(
    left: Iterable[int],
    right: Iterable[int],
    edges: Iterable[Edge],
) -> float:
    """OQM Gaussian scrambling rate for a Pauli-ZZ Hamiltonian.

    H = sum_e J_e Z_u Z_v on n qubits and a tensor-product bipartition.
    For a factor algebra A=L(H_L) tensor I_R and commutant A',
    tau_s^{-1}=D(H/sqrt(d), A+A').

    Distinct Pauli strings are Hilbert-Schmidt orthogonal and
    ||P/sqrt(d)||_2=1. Therefore only cross-boundary ZZ terms survive
    the orthogonal projection and

        tau_s^{-2} = sum_cross J_e^2.

    Hence tau_s^{-1}=sqrt(sum_cross J_e^2).
    """
    left, right = set(left), set(right)
    if left & right:
        raise ValueError("Partition factors must be disjoint.")
    sq=0.0
    for e in edges:
        if (e.u in left and e.v in right) or (e.v in left and e.u in right):
            sq += e.weight * e.weight
    return math.sqrt(sq)

def gaussian_scrambling_rate_squared_pauli_zz(left, right, edges) -> float:
    rate=gaussian_scrambling_rate_pauli_zz(left,right,edges)
    return rate*rate
