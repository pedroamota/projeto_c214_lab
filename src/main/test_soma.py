from Soma import soma

def test_soma():
    assert soma(1, 2) == 3
    assert soma(-1, -1) == -2
    assert soma(0, 0) == 0