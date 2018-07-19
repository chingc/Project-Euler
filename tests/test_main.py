"""Test the main module."""

from functools import reduce
from operator import mul
from typing import Sequence

import pytest

from euler.main import adjacent_digits, fibo, is_palindrome, is_prime, largest_palindrome, \
    lcm, nth_prime, prime_factors, pythagorean_triples, square_of_sums, sum_of_squares


def test_adjacent_digits(p008: str) -> None:
    """Expected: 5832"""
    adjacents = adjacent_digits(4, p008)
    assert adjacents[:5] == ["7316", "3167", "1671", "6717", "7176"]
    assert adjacents[-5:] == ["5296", "2963", "9634", "6345", "3450"]
    assert max(map(lambda x: reduce(mul, map(int, list(x))), adjacents)) == 5832

def test_fibo() -> None:
    """Expected: 10 Fibonacci numbers"""
    fibos = fibo(10)
    assert len(fibos) == 10
    assert fibos == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

@pytest.mark.parametrize("word", ["anna", "civic", "kayak", "madam", "wow", "9009", "1234321"])  # type: ignore
def test_is_palindrome(word: str) -> None:
    """Expected: True"""
    assert is_palindrome(word)

@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])  # type: ignore
def test_is_prime(num: int) -> None:
    """Expected: True"""
    assert is_prime(num)

def test_largest_palindrome() -> None:
    """Expected: 9009"""
    assert largest_palindrome(2) == 9009

@pytest.mark.parametrize("nums, ans", [  # type: ignore
    ([2, 5], 10),
    ([6, 21], 42),
    ([48, 180], 720),
    ([4, 7, 12, 21, 42], 84),
    ([11, 26, 31, 47, 52, 69, 72, 81, 99], 3105263304)
])
def test_lcm(nums: Sequence[int], ans: int) -> None:
    """Expected: Correct LCM"""
    assert lcm(*nums) == ans

def test_nth_prime() -> None:
    """Expected: True"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, value in enumerate(primes):
        assert nth_prime(i + 1) == value

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
def test_prime_factors(num: int, factors: Sequence[int]) -> None:
    """Expected: Correct prime factors"""
    assert prime_factors(num) == factors

def test_pythagorean_triples() -> None:
    """Expected: True"""
    for a, b, c in pythagorean_triples(100):
        assert a * a + b * b == c * c

def test_square_of_sums() -> None:
    """Expected: 3025"""
    assert square_of_sums(*range(1, 11)) == 3025

def test_sum_of_squares() -> None:
    """Expected: 385"""
    assert sum_of_squares(*range(1, 11)) == 385
