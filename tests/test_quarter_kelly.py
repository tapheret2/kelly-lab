from kelly_lab import kelly_fraction, quarter_kelly

def test_quarter_kelly():
    f = kelly_fraction(0.6, 1.0)
    assert abs(quarter_kelly(0.6, 1.0) - 0.25 * f) < 1e-12
