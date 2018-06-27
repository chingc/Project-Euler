"""https://projecteuler.net/problem=7"""

from euler.problem_007 import nth_prime


def test_nth_prime() -> None:
    """Expected: True"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, value in enumerate(primes):
        assert nth_prime(i + 1) == value

def test_007() -> None:
    """Expected: 104743"""
    assert nth_prime(10001) == 104743
