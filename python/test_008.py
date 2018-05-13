"""https://projecteuler.net/problem=8"""

from functools import reduce
from operator import mul
from typing import List


def adjacent_digits(num: int, path: str) -> List[str]:
    """List of all adjacent digits of `num` length."""
    adjacents = []
    with open(path, "r") as lines:
        view = ""
        for line in lines:
            view += line.strip()
            while len(view) >= num:
                adjacents.append(view[:num])
                view = view[1:]
    return adjacents


def test_adjacent_digits() -> None:
    """Expected: 5832"""
    adjacents = adjacent_digits(4, "python/test_008.input")
    assert adjacents[:5] == ["7316", "3167", "1671", "6717", "7176"]
    assert adjacents[-5:] == ["5296", "2963", "9634", "6345", "3450"]
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 5832

def test_p008() -> None:
    """Expected: 23514624000"""
    adjacents = adjacent_digits(13, "python/test_008.input")
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 23514624000
