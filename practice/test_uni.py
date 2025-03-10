import pytest
from calculator import add # type: ignore

def test_():
    assert add(1,3)==4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_str():
    with pytest.raises(TypeError):
        sum("cat") 