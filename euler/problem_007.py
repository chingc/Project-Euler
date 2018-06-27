"""https://projecteuler.net/problem=7"""

from problem_003 import is_prime


def nth_prime(nth: int) -> int:
    """Determine the `nth` prime."""
    current = 0
    while nth > 0:
        current += 1
        if is_prime(current):
            nth -= 1
    return current
