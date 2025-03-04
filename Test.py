"""import pytest # type: ignore
from calculator import square

def test_positive():
    assert square(2)== 4
    assert square(3)== 9

def test_negative():
    assert square(-2)== 4
    assert square(-3)== 9

def test_zero():
    assert square(0)== 0

def test_str():
    with pytest.raises(TypeError):
        square("cat") """


from hello import hello

def test_default():
    hello() == "hello, world"
def test_argument():
     for name in ["Hermione", "Harry", "Ron"]:
       assert hello(name) == f"hello, {name}"
