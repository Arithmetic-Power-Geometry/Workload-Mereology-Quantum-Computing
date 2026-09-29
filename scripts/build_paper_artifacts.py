from __future__ import annotations
import csv,json,math
from pathlib import Path

def wilson(k,n,z=1.959963984540054):
    p=k/n; den=1+z*z/n
    cen=(p+z*z/(2*n))/den
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return cen-half,cen+half

def summarize_csv(path, key="compromise_fraction"):
    rows=list(csv.DictReader(path.open(encoding="utf-8")))
    for r in rows:
        for f in list(r):
            try:r[f]=float(r[f])
            except (ValueError,TypeError):pass
    best=max(rows,key=lambda r:r[key])
    n=int(best["samples"]);k=round(best[key]*n)
    lo,hi=wilson(k,n)
    return {"best":best,"count":k,"wilson95":[lo,hi]}

def main():
    out=Path("artifacts")
    result={}
    for name in ["dimensionless_controls","noncommuting_controls"]:
        p=out/f"{name}.csv"
        if p.exists():result[name]=summarize_csv(p)
    (out/"paper_claims.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    lines=["# Frozen paper-facing claims",""]
    for name,d in result.items():
        b=d["best"];lines += [f"## {name}",f"- Best compromise fraction: {b['compromise_fraction']:.6f}",
          f"- Count: {d['count']}/{int(b['samples'])}",
          f"- Wilson 95% CI: [{d['wilson95'][0]:.6f}, {d['wilson95'][1]:.6f}]",
          f"- Parameters: "+", ".join(f"{k}={v}" for k,v in b.items() if k not in {"physical_fraction","task_fraction","compromise_fraction","samples"}),""]
    (out/"PAPER_CLAIMS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
if __name__=="__main__":main()
