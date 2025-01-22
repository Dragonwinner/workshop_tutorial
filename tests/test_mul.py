import pytest
from workshop_tutorial import multiply

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12

def test_multiply_positive_and_negative():
    assert multiply(3, -4) == -12

def test_multiply_with_zero():
    assert multiply(3, 0) == 0
    assert multiply(0, 4) == 0

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0
    assert multiply(3, 0.5) == 1.5

def test_multiply_large_numbers():
    assert multiply(100000, 100000) == 10000000000


   
