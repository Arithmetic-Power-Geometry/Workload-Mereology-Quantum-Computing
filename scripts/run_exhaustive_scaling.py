from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np
from wmqc.exhaustive import classify_joint_optimum, optimum, score_balanced_partitions
from wmqc.partition import Edge

def random_edges(rng, n, density=0.55):
    edges=[]
    for u in range(n):
        for v in range(u+1,n):
            if rng.random()<density:
                edges.append(Edge(u,v,float(rng.uniform(0.05,2.0))))
    return edges or [Edge(0,1,1.0)]

def correlated_task_edges(rng, physical, n, correlation):
    lookup={(e.u,e.v):e.weight for e in physical}
    edges=[]
    for u in range(n):
        for v in range(u+1,n):
            base=lookup.get((u,v),0.0)
            independent=float(rng.uniform(0.0,2.0))
            weight=correlation*base+(1.0-correlation)*independent
            if weight>0.05:
                edges.append(Edge(u,v,float(weight)))
    return edges

def same_partition(a,b):
    return a.left==b.left and a.right==b.right

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="artifacts")
    ap.add_argument("--seed",type=int,default=2026)
    ap.add_argument("--samples",type=int,default=500)
    args=ap.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(args.seed)
    rows=[]
    for n in [4,6,8]:
        for corr in [0.0,0.25,0.5,0.75,1.0]:
            for reuse in [0.1,0.25,0.5,1.0,2.0,4.0,8.0]:
                counts={"physical":0,"task":0,"compromise":0}; conflicts=0
                for _ in range(args.samples):
                    pe=random_edges(rng,n)
                    te=correlated_task_edges(rng,pe,n,corr)
                    scores=score_balanced_partitions(n,pe,te,reuse=reuse,alpha=1.0)
                    p=optimum(scores,"physical"); t=optimum(scores,"task")
                    if not same_partition(p,t): conflicts+=1
                    counts[classify_joint_optimum(scores)]+=1
                rows.append({
                    "n":n,"correlation":corr,"reuse":reuse,"samples":args.samples,
                    "conflict_fraction":conflicts/args.samples,
                    "physical_fraction":counts["physical"]/args.samples,
                    "task_fraction":counts["task"]/args.samples,
                    "compromise_fraction":counts["compromise"]/args.samples,
                })
    with (out/"exhaustive_scaling.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    best=max(rows,key=lambda x:x["compromise_fraction"])
    summary={
        "seed":args.seed,
        "samples_per_parameter_point":args.samples,
        "parameter_points":len(rows),
        "best_observed_compromise_regime":best,
        "any_compromise_observed":any(x["compromise_fraction"]>0 for x in rows),
        "definition":"compromise = joint optimum equals neither physical-only nor task-only optimum",
    }
    (out/"exhaustive_scaling_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
