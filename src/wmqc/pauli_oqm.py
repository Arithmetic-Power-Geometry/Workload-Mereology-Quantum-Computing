from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Iterable

@dataclass(frozen=True)
class PauliEdge:
    u:int
    v:int
    axis:str
    weight:float

def gaussian_rate(left:Iterable[int],right:Iterable[int],terms:Iterable[PauliEdge])->float:
    """OQM Gaussian rate for orthogonal two-body XX/YY/ZZ Pauli terms.
    With H/sqrt(d), distinct Pauli strings are Hilbert-Schmidt orthonormal.
    Projection onto A+A' removes terms wholly within either factor, leaving
    cross-factor terms. Thus tau_s^{-2} is the sum of squared crossing
    coefficients, independent of Pauli axis.
    """
    l,r=set(left),set(right)
    if l&r: raise ValueError("Partition factors must be disjoint")
    sq=0.0
    for e in terms:
        if e.axis not in {"X","Y","Z"}: raise ValueError("axis must be X, Y, or Z")
        if (e.u in l and e.v in r) or (e.v in l and e.u in r):
            sq+=e.weight**2
    return math.sqrt(sq)
