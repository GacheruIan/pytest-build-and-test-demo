from calc import *

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10,5) == 2


def test_world():
    assert word("world") == "Hello, world"

def test_modulo():
    assert modulo(6,2) == 0
