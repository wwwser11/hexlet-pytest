import pytest
from fill_ex import fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


def test_fill1(collection):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']

def test_fill2(collection):
    fill(collection, '*', 4)
    assert collection == [1, 2, 3, 4]

def test_fill3(collection):
    fill(collection, '*', 0, 10)
    assert collection == ['*', '*', '*', '*']