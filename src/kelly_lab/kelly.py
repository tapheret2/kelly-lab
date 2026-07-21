"""Kelly criterion math — educational implementation."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass


def kelly_fraction(p: float, b: float) -> float:
    """Full Kelly fraction for a binary even-money-style bet.

    Args:
        p: Probability of winning in (0, 1).
        b: Net decimal odds (decimal_odds - 1). Profit per unit stake if win.
    """
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")
    if b <= 0:
        raise ValueError("b (net odds) must be > 0")
    q = 1.0 - p
    f = (p * b - q) / b
    return max(0.0, f)


def expected_log_growth(p: float, b: float, f: float) -> float:
    """E[log growth] for fraction f of bankroll each bet."""
    if f < 0 or f >= 1:
        raise ValueError("f must be in [0, 1)")
    if f == 0:
        return 0.0
    q = 1.0 - p
    return p * math.log(1 + f * b) + q * math.log(1 - f)


@dataclass
class SimResult:
    final: float
    path: list[float]
    max_drawdown: float
    peak: float


def simulate_bankroll(
    p: float,
    b: float,
    f: float,
    bankroll: float = 1000.0,
    n: int = 100,
    seed: int | None = None,
) -> SimResult:
    """Monte Carlo path of bankroll under repeated independent bets."""
    if bankroll <= 0:
        raise ValueError("bankroll must be > 0")
    if n < 1:
        raise ValueError("n must be >= 1")
    if f < 0 or f >= 1:
        raise ValueError("f must be in [0, 1)")

    rng = random.Random(seed)
    path = [bankroll]
    peak = bankroll
    max_dd = 0.0
    br = bankroll
    for _ in range(n):
        stake = br * f
        if rng.random() < p:
            br = br + stake * b
        else:
            br = br - stake
        if br <= 0:
            br = 0.0
            path.append(br)
            break
        path.append(br)
        peak = max(peak, br)
        dd = (peak - br) / peak if peak > 0 else 0.0
        max_dd = max(max_dd, dd)
    return SimResult(final=br, path=path, max_drawdown=max_dd, peak=peak)


def ruin_probability(
    p: float,
    b: float,
    f: float,
    bankroll: float = 1000.0,
    n: int = 100,
    trials: int = 500,
    ruin_threshold: float = 0.0,
    seed: int | None = 0,
) -> float:
    """Estimate P(bankroll hits ruin_threshold) over `trials` simulated paths.

    Educational Monte Carlo — not a closed-form gambler's-ruin solution.
    """
    if trials < 1:
        raise ValueError("trials must be >= 1")
    if ruin_threshold < 0:
        raise ValueError("ruin_threshold must be >= 0")
    ruined = 0
    base = 0 if seed is None else int(seed)
    for i in range(trials):
        res = simulate_bankroll(p, b, f, bankroll=bankroll, n=n, seed=base + i)
        if res.final <= ruin_threshold:
            ruined += 1
    return ruined / trials


def half_kelly(p: float, b: float) -> float:
    """Convenience: 0.5 × full Kelly fraction."""
    return 0.5 * kelly_fraction(p, b)


def quarter_kelly(p: float, b: float) -> float:
    """Conservative 0.25 × full Kelly fraction."""
    return 0.25 * kelly_fraction(p, b)

def eighth_kelly(p: float, b: float) -> float:
    """Conservative sizing: 0.125 × full Kelly."""
    return 0.125 * kelly_fraction(p, b)


def clamp_fraction(f: float, lo: float = 0.0, hi: float = 1.0) -> float:
    """Clamp a bet fraction into [lo, hi]."""
    if lo > hi:
        raise ValueError("lo must be <= hi")
    return max(lo, min(hi, float(f)))


def geometric_growth(path: list[float]) -> float:
    """Terminal / initial bankroll ratio from a simulation path."""
    if not path or path[0] <= 0:
        return 0.0
    return float(path[-1]) / float(path[0])


def fractional_kelly(p: float, b: float, fraction: float = 0.5) -> float:
    """Scale full Kelly by an arbitrary fraction in (0, 1]."""
    if not 0.0 < fraction <= 1.0:
        raise ValueError("fraction must be in (0, 1]")
    return fraction * kelly_fraction(p, b)


def edge(p: float, b: float) -> float:
    """Expected edge per unit stake: p*b - (1-p)."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")
    if b <= 0:
        raise ValueError("b must be > 0")
    return p * b - (1.0 - p)
