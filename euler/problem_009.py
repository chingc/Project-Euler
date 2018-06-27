"""https://projecteuler.net/problem=9"""

from typing import Iterator, Tuple


def pythagorean_triples(upper: int, lower: int = 3) -> Iterator[Tuple[int, int, int]]:
    """Pythagorean triples where no side is longer than `upper` bound."""
    for a in range(lower, upper):
        for b in range(lower, upper):
            for c in range(lower, upper):
                if a < b < c and a * a + b * b == c * c:
                    yield (a, b, c)
