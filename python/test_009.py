"""https://projecteuler.net/problem=9"""

from typing import Generator


def pythagorean_triples(upper: int, lower: int = 2) -> Generator:
    """Generate Pythagorean triples where no side is longer than `upper` bound."""
    for a in range(lower, upper):
        for b in range(lower, upper):
            for c in range(lower, upper):
                if a < b < c and a * a + b * b == c * c:
                    yield (a, b, c)

#####

def test_pythagorean_triples() -> None:
    """Expected: True"""
    for a, b, c in pythagorean_triples(100):
        assert a * a + b * b == c * c

def test_p009() -> None:
    """Expected: 31875000"""
    for a, b, c in pythagorean_triples(500, 200):
        if a + b + c == 1000:
            triple = (a, b, c)
            break
    assert triple[0] * triple[1] * triple[2] == 31875000
