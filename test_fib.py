import pytest

from fibonacci import fib

def test_fib_1_equals_1():
    assert fib(1) == [1]

def test_fib_2_equals_2():
    assert fib(2) == [1, 1]

def test_fib_6_equals_6():
    assert fib(6) == [1, 1, 2, 3, 5, 8]

def test_fib_0_equals_0():
    assert fib(0) == 0

