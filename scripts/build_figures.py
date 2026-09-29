from __future__ import annotations
import csv
from pathlib import Path
import matplotlib.pyplot as plt

OUT=Path("artifacts")

def read(name):
    with (OUT/name).open(encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    for r in rows:
        for k,v in list(r.items()):
            try:r[k]=float(v)
            except (ValueError,TypeError):pass
    return rows

def phase_curve():
    rows=read("noncommuting_controls.csv")
    fig,ax=plt.subplots(figsize=(6.4,4.2))
    for n in [6,8,10]:
        q=sorted([r for r in rows if int(r["n"])==n],key=lambda r:r["lambda"])
        ax.plot([r["lambda"] for r in q],[r["compromise_fraction"] for r in q],marker="o",label=f"n={n}")
    ax.set_xscale("log",base=2)
    ax.set_xlabel("Dimensionless workload pressure λ")
    ax.set_ylabel("Compromise fraction")
    ax.set_title("Noncommuting XX+YY+ZZ workload–mereology transition")
    ax.legend();fig.tight_layout()
    fig.savefig(OUT/"fig_noncommuting_phase.png",dpi=300)
    fig.savefig(OUT/"fig_noncommuting_phase.pdf")
    plt.close(fig)

def outcome_at_equal_pressure():
    rows=read("noncommuting_controls.csv")
    q=sorted([r for r in rows if r["lambda"]==1.0],key=lambda r:r["n"])
    x=[str(int(r["n"])) for r in q]
    fig,ax=plt.subplots(figsize=(6.4,4.2))
    bottom=[0.0]*len(q)
    for key,label in [("physical_fraction","Physical"),("compromise_fraction","Compromise"),("task_fraction","Task")]:
        vals=[r[key] for r in q]
        ax.bar(x,vals,bottom=bottom,label=label)
        bottom=[a+b for a,b in zip(bottom,vals)]
    ax.set_xlabel("Number of qubits n")
    ax.set_ylabel("Selection fraction")
    ax.set_ylim(0,1)
    ax.set_title("Selected factorization at equal normalized pressure (λ=1)")
    ax.legend();fig.tight_layout()
    fig.savefig(OUT/"fig_equal_pressure_outcomes.png",dpi=300)
    fig.savefig(OUT/"fig_equal_pressure_outcomes.pdf")
    plt.close(fig)

if __name__=="__main__":
    phase_curve();outcome_at_equal_pressure()
