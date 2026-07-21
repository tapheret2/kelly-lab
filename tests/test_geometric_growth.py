from kelly_lab import fractional_kelly, geometric_growth, kelly_fraction, simulate_bankroll

def test_fractional_kelly_half():
    assert abs(fractional_kelly(0.55, 1.0, 0.5) - 0.5 * kelly_fraction(0.55, 1.0)) < 1e-12

def test_geometric_growth_identity():
    res = simulate_bankroll(0.55, 1.0, 0.05, bankroll=100.0, n=20, seed=1)
    g = geometric_growth(res.path)
    assert g == res.final / 100.0
