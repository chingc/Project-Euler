"""https://projecteuler.net/problem=4"""

from euler.main import largest_palindrome


def test_004() -> None:
    """Expected: 906609"""
    assert largest_palindrome(3) == 906609
