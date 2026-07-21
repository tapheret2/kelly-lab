from kelly_lab.kelly import edge

def test_edge_positive_when_good_odds():
    assert edge(0.6, 1.0) > 0
    assert edge(0.4, 1.0) < 0
