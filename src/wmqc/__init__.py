"""Workload–Mereology Quantum Computing reference implementation."""

from .model import CandidateFactorization, choose_factorization, critical_reuse, objective
from .four_qubit import (
    analytic_heisenberg_x1,
    commutator_scrambling,
    physical_scrambling_proxy,
    workload_scrambling_proxy,
)

__all__ = [
    "CandidateFactorization",
    "choose_factorization",
    "critical_reuse",
    "objective",
    "analytic_heisenberg_x1",
    "commutator_scrambling",
    "physical_scrambling_proxy",
    "workload_scrambling_proxy",
]
