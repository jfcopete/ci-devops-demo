from hello import h2, resta, suma, mult, div

def test_h2():
    assert h2() == "Hello, World!!"
def test_suma():
    assert suma(2, 3) == 5
def test_resta():
    assert resta(3, 2) == 1
def test_mult():
    assert mult(3, 2) == 6
def test_div():
    assert div(6, 2) == 3
    