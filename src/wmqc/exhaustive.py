from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .partition import Edge, all_balanced_bipartitions, crossing_interaction_weight, task_crossing_weight


@dataclass(frozen=True)
class PartitionScore:
    left: frozenset[int]
    right: frozenset[int]
    physical: float
    task: float
    joint: float


def score_balanced_partitions(
    n: int,
    physical_edges: Iterable[Edge],
    task_edges: Iterable[Edge],
    reuse: float,
    alpha: float = 1.0,
):
    physical_edges = list(physical_edges)
    task_edges = list(task_edges)
    scores = []
    for left, right in all_balanced_bipartitions(n):
        p = crossing_interaction_weight(left, right, physical_edges, squared=True)
        t = task_crossing_weight(left, right, task_edges)
        scores.append(
            PartitionScore(
                left=left,
                right=right,
                physical=p,
                task=t,
                joint=alpha * p + reuse * t,
            )
        )
    return scores


def optimum(scores: Iterable[PartitionScore], key: str) -> PartitionScore:
    scores = list(scores)
    if not scores:
        raise ValueError("No partition scores.")
    return min(scores, key=lambda x: getattr(x, key))


def classify_joint_optimum(scores: Iterable[PartitionScore]) -> str:
    scores = list(scores)
    p = optimum(scores, "physical")
    t = optimum(scores, "task")
    j = optimum(scores, "joint")
    if (j.left, j.right) == (p.left, p.right):
        return "physical"
    if (j.left, j.right) == (t.left, t.right):
        return "task"
    return "compromise"


def partition_label(score: PartitionScore) -> str:
    a = "".join(str(i + 1) for i in sorted(score.left))
    b = "".join(str(i + 1) for i in sorted(score.right))
    return a + "|" + b
