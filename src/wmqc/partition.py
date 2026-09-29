from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: float


def crossing_interaction_weight(
    left: Iterable[int],
    right: Iterable[int],
    edges: Iterable[Edge],
    squared: bool = True,
) -> float:
    """Interaction strength crossing a bipartition.

    For orthogonal Pauli interaction terms, the squared-weight sum is
    proportional to the squared Hilbert-Schmidt norm of the crossing
    interaction Hamiltonian (up to a dimension-dependent constant).
    """
    left = set(left)
    right = set(right)
    if left & right:
        raise ValueError("Partition factors must be disjoint.")
    total = 0.0
    for edge in edges:
        crosses = (edge.u in left and edge.v in right) or (
            edge.v in left and edge.u in right
        )
        if crosses:
            total += edge.weight ** 2 if squared else abs(edge.weight)
    return total


def all_balanced_bipartitions(n: int):
    """Unique balanced bipartitions for even n, fixing site 0 on the left."""
    if n % 2:
        raise ValueError("n must be even.")
    half = n // 2
    rest = range(1, n)
    for chosen in combinations(rest, half - 1):
        left = frozenset((0, *chosen))
        right = frozenset(set(range(n)) - set(left))
        yield left, right


def task_crossing_weight(
    left: Iterable[int],
    right: Iterable[int],
    task_edges: Iterable[Edge],
) -> float:
    """Weighted task interactions that cross the candidate factorization."""
    return crossing_interaction_weight(left, right, task_edges, squared=False)
