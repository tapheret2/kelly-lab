from kelly_lab.kelly import american_odds_to_prob, fractional_stake


def test_american_odds_to_prob():
    assert abs(american_odds_to_prob(-110) - (110 / 210)) < 1e-9
    assert abs(american_odds_to_prob(150) - (100 / 250)) < 1e-9


def test_fractional_stake():
    assert fractional_stake(1000, 0.25) == 250
    assert fractional_stake(1000, 2) == 1000
    assert fractional_stake(1000, -1) == 0
