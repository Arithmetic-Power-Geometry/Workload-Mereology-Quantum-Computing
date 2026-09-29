import pytest

from wmqc.partition import (
    Edge,
    all_balanced_bipartitions,
    crossing_interaction_weight,
    task_crossing_weight,
)


def test_four_qubit_physical_and_workload_partitions():
    physical_edges = [Edge(0, 1, 1.0), Edge(2, 3, 1.0)]
    task_edges = [Edge(0, 2, 1.0), Edge(1, 3, 1.0)]

    fp = ({0, 1}, {2, 3})
    fc = ({0, 2}, {1, 3})

    assert crossing_interaction_weight(*fp, physical_edges) == 0.0
    assert crossing_interaction_weight(*fc, physical_edges) == 2.0
    assert task_crossing_weight(*fp, task_edges) == 2.0
    assert task_crossing_weight(*fc, task_edges) == 0.0


def test_balanced_four_qubit_has_three_unique_pairings():
    parts = list(all_balanced_bipartitions(4))
    assert len(parts) == 3


def test_overlap_is_rejected():
    with pytest.raises(ValueError):
        crossing_interaction_weight({0, 1}, {1, 2}, [Edge(0, 2, 1.0)])
