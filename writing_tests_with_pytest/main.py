import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 9

def test_sub():
    assert addition.sub(4, 5) == -1

# python -m pytest main.py
# python -m pytest main.py::test_add