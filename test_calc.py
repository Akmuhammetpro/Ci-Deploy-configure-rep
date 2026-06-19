import pytest
from calc import add, divide

def test_add():
    assert add(2, 3) == 5

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)