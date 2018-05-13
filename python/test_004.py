"""https://projecteuler.net/problem=4"""

import pytest


def is_palindrome(string: str) -> bool:
    """String is the same forwards and backwards."""
    return string == string[::-1]

def largest_palindrome(num: int) -> int:
    """Largest palindrome made from the product of two `num`-digit numbers."""
    candidates = []
    start = int("9" * num)
    stop = int((start + 1) / 2)  # don't bother checking entire space
    for i in range(start, stop, -1):
        for j in range(i, stop, -1):
            if is_palindrome(str(i * j)):
                candidates.append(i * j)
    return max(*candidates)


@pytest.mark.parametrize("word", ["anna", "civic", "kayak", "madam", "wow", "9009", "1234321"])
def test_is_palindrome(word: str) -> None:
    """Expected: True"""
    assert is_palindrome(word)

def test_largest_palindrome() -> None:
    """Expected: 9009"""
    assert largest_palindrome(2) == 9009

def test_p004() -> None:
    """Expected: 906609"""
    assert largest_palindrome(3) == 906609
