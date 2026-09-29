import math
import numpy as np

from wmqc.four_qubit import (
    analytic_heisenberg_x1,
    commutator_scrambling,
    heisenberg_x1,
    physical_scrambling_proxy,
    workload_scrambling_proxy,
)


def test_numeric_matches_analytic_heisenberg_evolution():
    for J in [0.3, 1.0, 2.0]:
        for t in [0.0, 0.1, 0.37, 1.1]:
            err = np.linalg.norm(
                heisenberg_x1(J, t) - analytic_heisenberg_x1(J, t), "fro"
            )
            assert err < 1e-10


def test_scrambling_proxy_matches_commutator():
    for t in np.linspace(0.0, 2.0, 17):
        assert math.isclose(
            workload_scrambling_proxy(1.0, float(t)),
            commutator_scrambling(1.0, float(t)),
            rel_tol=1e-10,
            abs_tol=1e-10,
        )


def test_physical_factorization_proxy_is_zero():
    assert physical_scrambling_proxy(3.0, 100.0) == 0.0
