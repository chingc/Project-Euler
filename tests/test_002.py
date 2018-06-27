"""https://projecteuler.net/problem=2"""

from euler.problem_002 import fibo


def test_fibo() -> None:
    """Expected: 10 Fibonacci numbers"""
    fibos = fibo(10)
    assert len(fibos) == 10
    assert fibos == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_002() -> None:
    """Expected: 4613732"""
    assert fibo(34)[-1] < 4_000_000
    assert fibo(35)[-1] > 4_000_000
    assert sum([x for x in fibo(34) if x % 2 == 0]) == 4613732
