import math
from wmqc.oqm import gaussian_scrambling_rate_pauli_zz
from wmqc.partition import Edge

def test_oqm_four_qubit_physical_factorization_zero():
    edges=[Edge(0,1,2.0),Edge(2,3,2.0)]
    assert gaussian_scrambling_rate_pauli_zz({0,1},{2,3},edges)==0.0

def test_oqm_four_qubit_cross_factorization():
    edges=[Edge(0,1,2.0),Edge(2,3,2.0)]
    rate=gaussian_scrambling_rate_pauli_zz({0,2},{1,3},edges)
    assert math.isclose(rate, math.sqrt(8.0))

def test_oqm_rate_is_sqrt_of_previous_crossing_squared_strength():
    edges=[Edge(0,1,0.7),Edge(0,2,1.3),Edge(1,3,0.4)]
    rate=gaussian_scrambling_rate_pauli_zz({0,1},{2,3},edges)
    assert math.isclose(rate*rate,1.3**2+0.4**2)
