import pytest

from wmqc.model import CandidateFactorization, choose_factorization, critical_reuse
from wmqc.multifactor import compromise_example


def test_critical_reuse_formula():
    rc = critical_reuse(
        task_cost_a=10,
        task_cost_b=2,
        scrambling_a=0,
        scrambling_b=1,
        switch_b=2,
        alpha=8,
    )
    assert rc == pytest.approx(10 / 8)


def test_low_and_high_reuse_select_different_candidates():
    p = CandidateFactorization("P", task_cost=10, scrambling=0)
    c = CandidateFactorization("C", task_cost=2, scrambling=1, switch_cost=2)
    assert choose_factorization([p, c], reuse=0.1, alpha=8).name == "P"
    assert choose_factorization([p, c], reuse=10, alpha=8).name == "C"


def test_three_candidate_example_has_intermediate_regime():
    candidates = compromise_example()
    winners = {
        choose_factorization(candidates, reuse=r, alpha=1.0).name
        for r in [0.0, 0.3, 0.6, 1.0, 2.0, 5.0]
    }
    assert "physical" in winners
    assert "mixed" in winners
    assert "computational" in winners
