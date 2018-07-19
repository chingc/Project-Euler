"""https://projecteuler.net/problem=7"""

from euler.main import nth_prime


def test_007() -> None:
    """Expected: 104743"""
    assert nth_prime(10001) == 104743
