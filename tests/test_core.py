import pytest
from numtools.core import factorial, fib

def test_factorial_small():
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_fib_small():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

def test_bad_inputs():
    import math
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.14)
    with pytest.raises(ValueError):
        fib(-2)