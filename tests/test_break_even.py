from kelly_lab.kelly import break_even_prob, stake_for_target_profit

def test_break_even_even_money():
    assert abs(break_even_prob(1.0) - 0.5) < 1e-12

def test_break_even_plus_odds():
    assert abs(break_even_prob(2.0) - 1/3) < 1e-12

def test_stake_for_target():
    assert abs(stake_for_target_profit(100.0, 1.0) - 100.0) < 1e-12
    assert abs(stake_for_target_profit(100.0, 2.0) - 50.0) < 1e-12
