from kelly_lab.kelly import ruin_probability


def test_ruin_higher_with_full_kelly_edge_case():
    # Unfavorable edge → more ruin risk than tiny f
    p, b = 0.45, 1.0  # negative edge
    high = ruin_probability(p, b, f=0.2, bankroll=100, n=50, trials=200, seed=1)
    low = ruin_probability(p, b, f=0.01, bankroll=100, n=50, trials=200, seed=1)
    assert 0.0 <= low <= 1.0
    assert 0.0 <= high <= 1.0
    assert high >= low


def test_zero_fraction_no_ruin_if_threshold_zero():
    pr = ruin_probability(0.55, 1.0, f=0.0, bankroll=100, n=20, trials=50, seed=0)
    assert pr == 0.0
