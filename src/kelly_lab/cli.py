from __future__ import annotations

import argparse
import json
import sys

from .kelly import expected_log_growth, kelly_fraction, simulate_bankroll


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kelly-lab", description="Kelly criterion lab")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_frac = sub.add_parser("fraction", help="Compute Kelly fraction")
    p_frac.add_argument("--p", type=float, required=True, help="Win probability")
    p_frac.add_argument("--odds", type=float, required=True, help="Decimal odds (e.g. 2.0)")
    p_frac.add_argument("--fraction", type=float, default=1.0, help="Kelly multiplier (0.5 = half Kelly)")

    p_sim = sub.add_parser("sim", help="Simulate bankroll path")
    p_sim.add_argument("--p", type=float, required=True)
    p_sim.add_argument("--odds", type=float, required=True)
    p_sim.add_argument("--bankroll", type=float, default=1000.0)
    p_sim.add_argument("--n", type=int, default=200)
    p_sim.add_argument("--fraction", type=float, default=0.5, help="Kelly multiplier")
    p_sim.add_argument("--seed", type=int, default=None)
    p_sim.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    b = args.odds - 1.0
    full = kelly_fraction(args.p, b)
    f = full * args.fraction

    if args.cmd == "fraction":
        g = expected_log_growth(args.p, b, f) if f < 1 else float("nan")
        print(f"full_kelly={full:.6f}")
        print(f"applied_f={f:.6f} (multiplier={args.fraction})")
        print(f"E_log_growth={g:.6f}")
        return 0

    if args.cmd == "sim":
        res = simulate_bankroll(args.p, b, f, bankroll=args.bankroll, n=args.n, seed=args.seed)
        if args.json:
            print(json.dumps({
                "final": res.final,
                "max_drawdown": res.max_drawdown,
                "peak": res.peak,
                "steps": len(res.path) - 1,
                "path_tail": res.path[-10:],
            }, indent=2))
        else:
            print(f"start={args.bankroll:.2f} final={res.final:.2f} peak={res.peak:.2f}")
            print(f"max_drawdown={res.max_drawdown:.2%} steps={len(res.path)-1} f={f:.4f}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
