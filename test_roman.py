import roman

def test_I():
    assert roman.to_decimal("I") == 1

def test_II():
    assert roman.to_decimal("II") == 2

def test_III():
    assert roman.to_decimal("III") == 3

def test_IV():
    assert roman.to_decimal("IV") == 4

def test_V():
    assert roman.to_decimal("V") == 5

def test_VI():
    assert roman.to_decimal("VI") == 6

def test_L():
    assert roman.to_decimal("L") == 50

def test_X():
    assert roman.to_decimal("X") == 10

def test_C():
    assert roman.to_decimal("C") == 100

def test_M():
    assert roman.to_decimal("M") == 1000

# def test_IX():
#     assert roman.to_decimal("IX") == 9