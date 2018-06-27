"""https://projecteuler.net/problem=8"""

from functools import reduce
from operator import mul

from euler.problem_008 import adjacent_digits


def test_adjacent_digits() -> None:
    """Expected: 5832"""
    adjacents = adjacent_digits(4)
    assert adjacents[:5] == ["7316", "3167", "1671", "6717", "7176"]
    assert adjacents[-5:] == ["5296", "2963", "9634", "6345", "3450"]
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 5832

def test_008() -> None:
    """Expected: 23514624000"""
    adjacents = adjacent_digits(13)
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 23514624000
