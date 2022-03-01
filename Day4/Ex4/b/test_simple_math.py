from simple_math import *
import numpy as np

def test_simple_add():
    assert simple_add(2, 1) == 3

def test_simple_sub():
    assert simple_sub(4, 2) == 2

def test_simple_mult():
    assert simple_mult(4, 3) == 12

def test_simple_div():
    assert simple_div(1, 1) == 1.0

def test_poly_first():
    assert all(poly_first(np.array([1, 2, 3]), 1, 1) == np.array([2, 3, 4]))

def test_poly_second():
    assert all(poly_second(np.array([1, 2, 3]), 1, 1, 1) == np.array([3, 7, 13]))