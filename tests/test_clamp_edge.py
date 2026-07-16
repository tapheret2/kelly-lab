import pytest
from kelly_lab import clamp_fraction

def test_clamp_invalid_bounds():
    with pytest.raises(ValueError):
        clamp_fraction(0.5, lo=1.0, hi=0.0)
