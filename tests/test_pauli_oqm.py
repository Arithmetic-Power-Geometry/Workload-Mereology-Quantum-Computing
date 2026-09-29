import math
from wmqc.pauli_oqm import PauliEdge,gaussian_rate

def test_xyz_crossing_terms_add_in_quadrature():
    terms=[PauliEdge(0,2,"X",1),PauliEdge(0,2,"Y",2),PauliEdge(1,3,"Z",3)]
    assert math.isclose(gaussian_rate({0,1},{2,3},terms),math.sqrt(14))

def test_local_noncommuting_terms_do_not_cross_factor_algebra():
    terms=[PauliEdge(0,1,"X",1),PauliEdge(0,1,"Z",2),PauliEdge(2,3,"Y",4)]
    assert gaussian_rate({0,1},{2,3},terms)==0.0
