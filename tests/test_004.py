"""https://projecteuler.net/problem=4"""

import pytest

from euler.problem_004 import is_palindrome, largest_palindrome


@pytest.mark.parametrize("word", ["anna", "civic", "kayak", "madam", "wow", "9009", "1234321"])  # type: ignore
def test_is_palindrome(word: str) -> None:
    """Expected: True"""
    assert is_palindrome(word)

def test_largest_palindrome() -> None:
    """Expected: 9009"""
    assert largest_palindrome(2) == 9009

def test_004() -> None:
    """Expected: 906609"""
    assert largest_palindrome(3) == 906609
