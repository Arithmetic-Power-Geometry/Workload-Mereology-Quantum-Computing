from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import numpy as np
from wmqc.partition import Edge,all_balanced_bipartitions,task_crossing_weight
from wmqc.oqm import gaussian_scrambling_rate_pauli_zz

def edges(rng,n,dist):
    out=[]
    for u in range(n):
        for v in range(u+1,n):
            if rng.random()<0.55:
                if dist=="uniform": w=rng.uniform(0.05,2.0)
                elif dist=="lognormal": w=np.clip(rng.lognormal(-0.1,0.65),0.05,4.0)
                else: w=np.clip(abs(rng.normal(1.0,0.55)),0.05,3.0)
                out.append(Edge(u,v,float(w)))
    return out or [Edge(0,1,1.0)]

def task_edges(rng,n,dist):
    return edges(rng,n,dist)

def amin(x): return min(range(len(x)),key=x.__getitem__)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",default="artifacts");ap.add_argument("--seed",type=int,default=2027);ap.add_argument("--samples",type=int,default=300)
    a=ap.parse_args();rng=np.random.default_rng(a.seed);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n in [6,8,10]:
      parts=list(all_balanced_bipartitions(n))
      for dist in ["uniform","normal","lognormal"]:
       for r in [0.25,0.5,1.0,2.0]:
        c={"physical":0,"task":0,"compromise":0}
        for _ in range(a.samples):
          pe=edges(rng,n,dist);te=task_edges(rng,n,dist)
          s=[gaussian_scrambling_rate_pauli_zz(x,y,pe) for x,y in parts]
          # normalize task crossing by total task weight to remove trivial scale changes
          total=max(sum(abs(e.weight) for e in te),1e-12)
          t=[task_crossing_weight(x,y,te)/total for x,y in parts]
          ip,it=amin(s),amin(t);ij=amin([s[k]+r*t[k] for k in range(len(parts))])
          c["physical" if ij==ip else "task" if ij==it else "compromise"]+=1
        rows.append({"n":n,"distribution":dist,"reuse":r,"samples":a.samples,
          "physical_fraction":c["physical"]/a.samples,"task_fraction":c["task"]/a.samples,"compromise_fraction":c["compromise"]/a.samples})
    with (out/"oqm_controls.csv").open("w",newline="",encoding="utf-8") as f:
      w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    best=max(rows,key=lambda z:z["compromise_fraction"])
    (out/"oqm_controls_summary.json").write_text(json.dumps({"seed":a.seed,"best":best,"rows":len(rows)},indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
