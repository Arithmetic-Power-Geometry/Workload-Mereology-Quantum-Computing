from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from wmqc.partition import (
    Edge,
    all_balanced_bipartitions,
    crossing_interaction_weight,
    task_crossing_weight,
)


def label(part):
    left, right = part
    return "".join(str(i + 1) for i in sorted(left)) + "|" + "".join(
        str(i + 1) for i in sorted(right)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts")
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--samples", type=int, default=2000)
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    parts = list(all_balanced_bipartitions(4))
    physical_edges = [Edge(0, 1, 1.0), Edge(2, 3, 1.0)]
    task_edges = [Edge(0, 2, 1.0), Edge(1, 3, 1.0)]

    deterministic = []
    for part in parts:
        deterministic.append({
            "partition": label(part),
            "physical_crossing_strength": crossing_interaction_weight(
                *part, physical_edges
            ),
            "task_crossing_cost": task_crossing_weight(*part, task_edges),
        })

    with (out / "partition_comparison.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=deterministic[0].keys())
        writer.writeheader()
        writer.writerows(deterministic)

    rng = np.random.default_rng(args.seed)
    counts = {label(p): 0 for p in parts}
    tradeoff_count = 0
    for _ in range(args.samples):
        # Perturb both physical and workload interaction strengths while
        # preserving their preferred edge patterns.
        pe = [
            Edge(0, 1, max(0.0, rng.normal(1.0, 0.25))),
            Edge(2, 3, max(0.0, rng.normal(1.0, 0.25))),
            Edge(0, 2, max(0.0, rng.normal(0.15, 0.08))),
            Edge(1, 3, max(0.0, rng.normal(0.15, 0.08))),
        ]
        te = [
            Edge(0, 2, max(0.0, rng.normal(1.0, 0.25))),
            Edge(1, 3, max(0.0, rng.normal(1.0, 0.25))),
            Edge(0, 1, max(0.0, rng.normal(0.15, 0.08))),
            Edge(2, 3, max(0.0, rng.normal(0.15, 0.08))),
        ]

        p_phys = min(parts, key=lambda p: crossing_interaction_weight(*p, pe))
        p_task = min(parts, key=lambda p: task_crossing_weight(*p, te))
        counts[label(p_phys)] += 1
        if p_phys != p_task:
            tradeoff_count += 1

    summary = {
        "seed": args.seed,
        "samples": args.samples,
        "physical_optimum_counts": counts,
        "physical_and_task_optima_differ_fraction": tradeoff_count / args.samples,
        "interpretation": (
            "Monte Carlo robustness test of competing physical and workload "
            "interaction graphs; not a quantum-speedup experiment."
        ),
    }
    (out / "partition_robustness.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
