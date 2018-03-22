"""https://projecteuler.net/problem=9"""

from typing import Generator


def pythagorean_triples(upper: int, lower: int = 2) -> Generator:
    """Generate Pythagorean triples where no side is longer than `upper` bound."""
    for i in range(lower, upper):
        for j in range(lower, upper):
            for k in range(lower, upper):
                if i < j < k and i * i + j * j == k * k:
                    yield (i, j, k)


def test_pythagorean_triples() -> None:
    """Expected: True"""
    for i, j, k in pythagorean_triples(100):
        assert i * i + j * j == k * k

def test_p009() -> None:
    """Expected: 31875000"""
    for i, j, k in pythagorean_triples(500, 200):
        if i + j + k == 1000:
            triple = (i, j, k)
            break
    assert triple[0] * triple[1] * triple[2] == 31875000
