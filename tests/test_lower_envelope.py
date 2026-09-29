import math

def crossover(c1,s1,c2,s2):
    return (s2-s1)/(c1-c2)

def objective(c,s,lam):
    return s+lam*c

def test_strict_intermediate_hull_vertex_has_open_optimal_interval():
    # physical -> compromise -> task
    P=(1.0,0.0)
    C=(0.45,0.25)
    T=(0.0,1.0)
    l_pc=crossover(*P,*C)
    l_ct=crossover(*C,*T)
    assert l_pc < l_ct
    mid=(l_pc+l_ct)/2
    vals=[objective(*x,mid) for x in (P,C,T)]
    assert vals[1] < vals[0] and vals[1] < vals[2]

def test_collinear_intermediate_has_no_unique_open_interval():
    P=(1.0,0.0)
    C=(0.5,0.5)
    T=(0.0,1.0)
    l_pc=crossover(*P,*C)
    l_ct=crossover(*C,*T)
    assert math.isclose(l_pc,l_ct)

def test_point_above_endpoint_chord_never_beats_both_endpoints():
    P=(1.0,0.0)
    C=(0.5,0.7)
    T=(0.0,1.0)
    for lam in [0.01,0.1,0.5,1,2,10,100]:
        vc=objective(*C,lam)
        assert vc >= min(objective(*P,lam),objective(*T,lam))
