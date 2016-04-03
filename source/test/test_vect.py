import pytest
#import scripts in parent directory
from Vect2 import Vect2
import copy

def test_init():
    t = Vect2()
    assert t.x == 0 and t.y == 0, "Default constructor should create zero 2d vector"
def test_init2():
    t = Vect2(5, 2)
    assert t.x ==5 and t.y == 2, "Constructor should define x and y"

def test_addition():
    t1 = Vect2(1, 0)
    t2 = Vect2(0, 1)
    t1 += t2
    assert t1.x == 1 and t1.y == 1, "Addition between vectors should work"

def test_subtraction():
    t1 = Vect2(1, 1)
    t2 = Vect2(0, 1)
    t1 -= t2
    assert t1.x == 1 and t1.y == 0, "Subtraction should work between vectors"

def test_multiplication():
    t1 = Vect2(1, 1)
    t2 = 0
    t1 *= t2
    assert t1.x == 0 and t1.y == 0, "Multiplication by zero should be zero"

def test_multiplication2():
    t1 = Vect2(1, 1)
    tb = copy.copy(t1)
    t2 = 1
    t1 *= t2
    assert t1.x == tb.x and t1.y == tb.y, "Multiplication by one should equal 1"
