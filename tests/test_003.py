"""https://projecteuler.net/problem=3"""

from euler.main import prime_factors


def test_003() -> None:
    """Expected: 6857"""
    assert prime_factors(600851475143)[-1] == 6857
