"""https://projecteuler.net/problem=10"""

from p003 import is_prime


def test_p010() -> None:
    """Expected: 142913828922"""
    assert sum(x for x in range(2, 2_000_000) if is_prime(x)) == 142913828922
