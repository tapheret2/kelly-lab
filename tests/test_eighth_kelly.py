from kelly_lab import eighth_kelly, kelly_fraction, clamp_fraction

def test_eighth_kelly_is_eighth():
    f = kelly_fraction(0.6, 1.0)
    assert abs(eighth_kelly(0.6, 1.0) - 0.125 * f) < 1e-12

def test_clamp_fraction():
    assert clamp_fraction(1.5, 0, 1) == 1.0
    assert clamp_fraction(-0.2, 0, 1) == 0.0
    assert clamp_fraction(0.3, 0, 1) == 0.3
