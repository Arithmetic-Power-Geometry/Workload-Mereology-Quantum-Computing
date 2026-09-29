from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CandidateFactorization:
    name: str
    task_cost: float
    scrambling: float = 0.0
    error_cost: float = 0.0
    switch_cost: float = 0.0


def objective(
    candidate: CandidateFactorization,
    reuse: float,
    alpha: float = 1.0,
    beta: float = 1.0,
) -> float:
    return (
        reuse * candidate.task_cost
        + alpha * candidate.scrambling
        + beta * candidate.error_cost
        + candidate.switch_cost
    )


def choose_factorization(
    candidates: Iterable[CandidateFactorization],
    reuse: float,
    alpha: float = 1.0,
    beta: float = 1.0,
) -> CandidateFactorization:
    candidates = list(candidates)
    if not candidates:
        raise ValueError("At least one candidate factorization is required.")
    return min(candidates, key=lambda c: objective(c, reuse, alpha, beta))


def critical_reuse(
    task_cost_a: float,
    task_cost_b: float,
    scrambling_a: float = 0.0,
    scrambling_b: float = 0.0,
    error_a: float = 0.0,
    error_b: float = 0.0,
    switch_a: float = 0.0,
    switch_b: float = 0.0,
    alpha: float = 1.0,
    beta: float = 1.0,
) -> float:
    """Reuse r where candidates a and b have equal total objective.

    Candidate b must have lower task cost.
    """
    delta_c = task_cost_a - task_cost_b
    if delta_c <= 0:
        raise ValueError("Candidate b must have lower task cost than candidate a.")
    delta_penalty = (
        (switch_b - switch_a)
        + alpha * (scrambling_b - scrambling_a)
        + beta * (error_b - error_a)
    )
    return delta_penalty / delta_c
