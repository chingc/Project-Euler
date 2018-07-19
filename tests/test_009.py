"""https://projecteuler.net/problem=9"""

from euler.main import pythagorean_triples


def test_009() -> None:
    """Expected: 31875000"""
    for a, b, c in pythagorean_triples(500, 200):
        if a + b + c == 1000:
            triple = (a, b, c)
            break
    assert triple[0] * triple[1] * triple[2] == 31875000
