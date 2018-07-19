"""https://projecteuler.net/problem=8"""

from functools import reduce
from operator import mul

from euler.main import adjacent_digits


def test_008(p008: str) -> None:
    """Expected: 23514624000"""
    adjacents = adjacent_digits(13, p008)
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 23514624000
