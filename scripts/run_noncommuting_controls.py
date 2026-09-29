from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import numpy as np
from wmqc.partition import Edge,all_balanced_bipartitions,task_crossing_weight
from wmqc.pauli_oqm import PauliEdge,gaussian_rate

def hamiltonian(rng,n):
    out=[]
    for u in range(n):
      for v in range(u+1,n):
       if rng.random()<.55:
        # Generic anisotropic Heisenberg-like edge; XX, YY, ZZ generally do not commute globally.
        for axis in "XYZ":
         out.append(PauliEdge(u,v,axis,float(rng.normal(0,1))))
    return out or [PauliEdge(0,1,"X",1.)]

def workload(rng,n):
    out=[]
    for u in range(n):
      for v in range(u+1,n):
       if rng.random()<.55: out.append(Edge(u,v,float(rng.uniform(.05,2))))
    return out or [Edge(0,1,1.)]

def norm01(x):
    lo,hi=min(x),max(x)
    return [0. for _ in x] if hi-lo<1e-12 else [(v-lo)/(hi-lo) for v in x]
def amin(x):return min(range(len(x)),key=x.__getitem__)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",default="artifacts");ap.add_argument("--seed",type=int,default=2029);ap.add_argument("--samples",type=int,default=300)
    a=ap.parse_args();rng=np.random.default_rng(a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=True);rows=[]
    for n in [6,8,10]:
      parts=list(all_balanced_bipartitions(n))
      for lam in [.1,.25,.5,1,2,4,8]:
       c={"physical":0,"task":0,"compromise":0};conf=0
       for _ in range(a.samples):
        h=hamiltonian(rng,n);w=workload(rng,n)
        s=norm01([gaussian_rate(x,y,h) for x,y in parts])
        t=norm01([task_crossing_weight(x,y,w) for x,y in parts])
        ip,it=amin(s),amin(t);conf+=ip!=it
        ij=amin([s[k]+lam*t[k] for k in range(len(parts))])
        c["physical" if ij==ip else "task" if ij==it else "compromise"]+=1
       rows.append({"n":n,"lambda":lam,"samples":a.samples,"conflict_fraction":conf/a.samples,
        "physical_fraction":c["physical"]/a.samples,"task_fraction":c["task"]/a.samples,"compromise_fraction":c["compromise"]/a.samples})
    with (out/"noncommuting_controls.csv").open("w",newline="",encoding="utf-8") as f:
      wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
    best=max(rows,key=lambda z:z["compromise_fraction"])
    (out/"noncommuting_controls_summary.json").write_text(json.dumps({"seed":a.seed,"best":best,"rows":len(rows)},indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
