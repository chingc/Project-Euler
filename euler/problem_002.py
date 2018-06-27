"""https://projecteuler.net/problem=2"""

from typing import List


def fibo(nth: int) -> List[int]:
    """Fibonacci numbers up to the `nth` term starting with 0 and 1."""
    fibos = [0, 1]
    for _ in range(nth - 2):  # - 2 because we already have the first two
        fibos.append(fibos[-1] + fibos[-2])
    return fibos
