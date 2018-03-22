"""https://projecteuler.net/problem=7"""

from p003 import is_prime


def nth_prime(nth: int) -> int:
    """Determine the nth prime."""
    current = 0
    while nth > 0:
        current += 1
        if is_prime(current):
            nth -= 1
    return current


def test_nth_prime() -> None:
    """Expected: True"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, value in enumerate(primes):
        assert nth_prime(i + 1) == value

def test_p007() -> None:
    """Expected: 104743"""
    assert nth_prime(10001) == 104743
