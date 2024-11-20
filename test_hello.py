from hello import h2, resta, suma

def test_h2():
    assert h2() == "Hello, World!!"
def test_suma():
    assert suma(2, 3) == 5
def test_resta():
    assert resta(3, 2) == 1
    