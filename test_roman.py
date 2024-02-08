import roman

def test_I():
    assert roman.to_decimal("I") == 1

def test_II():
    assert roman.to_decimal("II") == 2

def test_V():
    assert roman.to_decimal("V") == 5