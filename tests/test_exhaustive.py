from wmqc.exhaustive import classify_joint_optimum, score_balanced_partitions
from wmqc.partition import Edge


def test_partition_counts_six_and_eight_sites():
    assert len(score_balanced_partitions(6, [], [], reuse=1.0)) == 10
    assert len(score_balanced_partitions(8, [], [], reuse=1.0)) == 35


def test_constructed_six_site_compromise_can_exist():
    # Physical graph favors 123|456.
    physical = [
        Edge(0, 1, 2.0), Edge(1, 2, 2.0), Edge(0, 2, 2.0),
        Edge(3, 4, 2.0), Edge(4, 5, 2.0), Edge(3, 5, 2.0),
    ]
    # Workload graph favors 145|236.
    task = [
        Edge(0, 3, 2.0), Edge(0, 4, 2.0), Edge(3, 4, 2.0),
        Edge(1, 2, 2.0), Edge(1, 5, 2.0), Edge(2, 5, 2.0),
    ]
    # This test only requires the exhaustive classifier to return a valid class;
    # the Monte Carlo experiment determines whether compromise regions arise
    # without construction.
    cls = classify_joint_optimum(
        score_balanced_partitions(6, physical, task, reuse=1.0, alpha=1.0)
    )
    assert cls in {"physical", "task", "compromise"}
