import math

import pytest

from kelly_lab import expected_log_growth, kelly_fraction, simulate_bankroll


def test_even_money_edge():
    # p=0.6, even money b=1 -> f* = 0.2
    assert abs(kelly_fraction(0.6, 1.0) - 0.2) < 1e-9


def test_no_edge_zero():
    assert kelly_fraction(0.5, 1.0) == 0.0


def test_negative_edge_clipped():
    assert kelly_fraction(0.4, 1.0) == 0.0


def test_growth_positive_at_kelly():
    p, b = 0.55, 1.0
    f = kelly_fraction(p, b)
    assert expected_log_growth(p, b, f) > 0


def test_sim_reproducible():
    a = simulate_bankroll(0.55, 1.0, 0.05, bankroll=1000, n=50, seed=7)
    b = simulate_bankroll(0.55, 1.0, 0.05, bankroll=1000, n=50, seed=7)
    assert a.path == b.path


def test_bad_inputs():
    with pytest.raises(ValueError):
        kelly_fraction(0.0, 1.0)
    with pytest.raises(ValueError):
        kelly_fraction(0.5, 0.0)
