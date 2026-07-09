from kelly_lab import half_kelly, kelly_fraction

def test_half_kelly_is_half():
    f = kelly_fraction(0.6, 1.0)
    assert abs(half_kelly(0.6, 1.0) - 0.5 * f) < 1e-12
