from __future__ import annotations
import argparse,csv,json,math
from pathlib import Path
import numpy as np
from wmqc.partition import Edge,all_balanced_bipartitions,task_crossing_weight
from wmqc.oqm import gaussian_scrambling_rate_pauli_zz

def random_edges(rng,n,density=0.55):
    out=[]
    for u in range(n):
        for v in range(u+1,n):
            if rng.random()<density:
                out.append(Edge(u,v,float(rng.uniform(0.05,2.0))))
    return out or [Edge(0,1,1.0)]

def correlated_task(rng,physical,n,rho):
    lookup={(e.u,e.v):e.weight for e in physical}; out=[]
    for u in range(n):
        for v in range(u+1,n):
            w=rho*lookup.get((u,v),0.0)+(1-rho)*float(rng.uniform(0,2))
            if w>0.05: out.append(Edge(u,v,float(w)))
    return out

def argmin_index(values):
    return min(range(len(values)),key=values.__getitem__)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="artifacts")
    ap.add_argument("--seed",type=int,default=2026)
    ap.add_argument("--samples",type=int,default=500)
    args=ap.parse_args()
    rng=np.random.default_rng(args.seed); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n in [4,6,8]:
        parts=list(all_balanced_bipartitions(n))
        for rho in [0.0,0.25,0.5,0.75,1.0]:
            for reuse in [0.1,0.25,0.5,1.0,2.0,4.0,8.0]:
                count={"physical":0,"task":0,"compromise":0}; conflict=0
                for _ in range(args.samples):
                    pe=random_edges(rng,n); te=correlated_task(rng,pe,n,rho)
                    s=[gaussian_scrambling_rate_pauli_zz(a,b,pe) for a,b in parts]
                    c=[task_crossing_weight(a,b,te) for a,b in parts]
                    ip=argmin_index(s); it=argmin_index(c)
                    if ip!=it: conflict+=1
                    j=[s[k]+reuse*c[k] for k in range(len(parts))]
                    ij=argmin_index(j)
                    count["physical" if ij==ip else "task" if ij==it else "compromise"]+=1
                rows.append({"n":n,"correlation":rho,"reuse":reuse,"samples":args.samples,
                    "conflict_fraction":conflict/args.samples,
                    "physical_fraction":count["physical"]/args.samples,
                    "task_fraction":count["task"]/args.samples,
                    "compromise_fraction":count["compromise"]/args.samples})
    with (out/"oqm_exhaustive_scaling.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    best=max(rows,key=lambda x:x["compromise_fraction"])
    summary={"criterion":"OQM Gaussian scrambling rate tau_s^{-1}=D(H/sqrt(d),A+A') specialized to Pauli-ZZ bipartitions",
      "seed":args.seed,"samples_per_parameter_point":args.samples,"parameter_points":len(rows),
      "best_observed_compromise_regime":best,
      "any_compromise_observed":any(x["compromise_fraction"]>0 for x in rows)}
    (out/"oqm_exhaustive_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
