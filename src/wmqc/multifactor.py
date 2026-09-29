from __future__ import annotations

from typing import Iterable

from .model import CandidateFactorization, choose_factorization


def sweep_reuse(
    candidates: Iterable[CandidateFactorization],
    reuses: Iterable[float],
    alpha: float = 1.0,
    beta: float = 1.0,
):
    candidates = list(candidates)
    return [
        (float(r), choose_factorization(candidates, float(r), alpha, beta).name)
        for r in reuses
    ]


def compromise_example():
    """Three candidates with a genuine intermediate optimal regime."""
    return [
        CandidateFactorization("physical", task_cost=10.0, scrambling=0.0),
        CandidateFactorization("mixed", task_cost=6.0, scrambling=2.0),
        CandidateFactorization("computational", task_cost=2.0, scrambling=8.0),
    ]
