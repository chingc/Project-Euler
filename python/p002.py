"""https://projecteuler.net/problem=2"""

from typing import List


def fibo(nth: int) -> List[int]:
    """Fibonacci numbers up to the `nth` term starting with 0 and 1."""
    fibos = [0, 1]
    for _ in range(nth - 2):  # - 2 because we already have the first two
        fibos.append(fibos[-2] + fibos[-1])
    return fibos


def test_fibo() -> None:
    """Expected: 10 Fibonacci numbers"""
    fibos = fibo(10)
    assert len(fibos) == 10
    assert fibos == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_p002() -> None:
    """Expected: 4613732"""
    assert fibo(34)[-1] < 4_000_000
    assert fibo(35)[-1] > 4_000_000
    assert sum([x for x in fibo(34) if x % 2 == 0]) == 4613732
