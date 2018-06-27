"""https://projecteuler.net/problem=3"""

from typing import List

import pytest

from euler.problem_003 import is_prime, prime_factors


@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])  # type: ignore
def test_is_prime(num: int) -> None:
    """Expected: True"""
    assert is_prime(num)

@pytest.mark.parametrize("num, factors", [  # type: ignore
    (22, [2, 11]),
    (333, [3, 3, 37]),
    (4444, [2, 2, 11, 101]),
    (55555, [5, 41, 271]),
    (666666, [2, 3, 3, 7, 11, 13, 37]),
    (7777777, [7, 239, 4649]),
    (88888888, [2, 2, 2, 11, 73, 101, 137]),
    (999999999, [3, 3, 3, 3, 37, 333667])
])
def test_prime_factors(num: int, factors: List[int]) -> None:
    """Expected: Correct prime factors"""
    assert prime_factors(num) == factors

def test_003() -> None:
    """Expected: 6857"""
    assert prime_factors(600851475143)[-1] == 6857
