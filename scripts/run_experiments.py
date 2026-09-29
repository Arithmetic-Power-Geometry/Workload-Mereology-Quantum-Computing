from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from wmqc.four_qubit import (
    analytic_heisenberg_x1,
    commutator_scrambling,
    heisenberg_x1,
    physical_scrambling_proxy,
    workload_scrambling_proxy,
)
from wmqc.model import choose_factorization, critical_reuse
from wmqc.multifactor import compromise_example


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts")
    parser.add_argument("--J", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=8.0)
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--switch-cost", type=float, default=2.0)
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    rows = []
    max_operator_error = 0.0
    for t in np.linspace(0.0, np.pi, 401):
        t = float(t)
        s_p = physical_scrambling_proxy(args.J, t)
        s_c = workload_scrambling_proxy(args.J, t)
        s_comm = commutator_scrambling(args.J, t)
        rc = critical_reuse(
            task_cost_a=10.0,
            task_cost_b=2.0,
            scrambling_a=s_p,
            scrambling_b=s_c,
            switch_a=0.0,
            switch_b=args.switch_cost,
            alpha=args.alpha,
            beta=args.beta,
        )
        err = np.linalg.norm(
            heisenberg_x1(args.J, t) - analytic_heisenberg_x1(args.J, t),
            "fro",
        )
        max_operator_error = max(max_operator_error, float(err))
        rows.append({
            "t": t,
            "scrambling_physical": s_p,
            "scrambling_workload": s_c,
            "commutator_scrambling": s_comm,
            "critical_reuse": rc,
        })

    with (out / "four_qubit_sweep.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    candidates = compromise_example()
    phase_rows = []
    for r in np.linspace(0.0, 5.0, 501):
        r = float(r)
        winner = choose_factorization(candidates, reuse=r, alpha=1.0)
        phase_rows.append({"reuse": r, "winner": winner.name})

    with (out / "three_factorization_phase.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=phase_rows[0].keys())
        writer.writeheader()
        writer.writerows(phase_rows)

    summary = {
        "model": "four-qubit ZZ workload-mereology benchmark",
        "J": args.J,
        "alpha": args.alpha,
        "beta": args.beta,
        "switch_cost": args.switch_cost,
        "max_analytic_operator_error": max_operator_error,
        "critical_reuse_min": min(row["critical_reuse"] for row in rows),
        "critical_reuse_max": max(row["critical_reuse"] for row in rows),
        "compromise_factorization_observed": any(row["winner"] == "mixed" for row in phase_rows),
        "claims": {
            "new_quantum_mechanics": False,
            "beyond_BQP": False,
            "quantum_speedup_demonstrated": False,
        },
    }

    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (out / "RESULTS.md").write_text(
        "# Reproducibility Results\n\n"
        + f"- Maximum numerical-vs-analytic operator error: `{max_operator_error:.3e}`\n"
        + f"- Critical reuse range: `{summary['critical_reuse_min']:.6f}` to `{summary['critical_reuse_max']:.6f}`\n"
        + f"- Intermediate compromise factorization observed: `{summary['compromise_factorization_observed']}`\n\n"
        + "These outputs are benchmark results, not evidence of quantum speedup.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
