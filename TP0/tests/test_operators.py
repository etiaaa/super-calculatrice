import pytest
from calculate.operators import Operators

def test_addition():
    assert Operators().addition("2+2") == 4

def test_division_by_zero():
    assert Operators().division("5/0") is None

def test_invalid_input():
    assert Operators().addition("2++2") is None