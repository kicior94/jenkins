from math_package.functions import add, subtract

def test_add():
    assert add(1,3) == 4
    assert add(5,4) == 9

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(2,1) == 1