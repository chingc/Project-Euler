"""https://projecteuler.net/problem=2"""

from euler.main import fibo


def test_002() -> None:
    """Expected: 4613732"""
    assert fibo(34)[-1] < 4_000_000
    assert fibo(35)[-1] > 4_000_000
    assert sum([x for x in fibo(34) if x % 2 == 0]) == 4613732
