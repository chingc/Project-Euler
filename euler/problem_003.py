"""https://projecteuler.net/problem=3"""

from typing import List


def is_prime(n: int) -> bool:
    """Determine if `n` is prime."""
    if n < 2 or str(n)[-1] in [0, 2, 4, 5, 6, 8]:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):  # n ** 0.5 == sqrt(n)
        if n % divisor == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """Prime factors of `n` in ascending order."""
    if n < 2:
        return []
    if is_prime(n):
        return [n]
    divisor, factors = 2, []
    while True:
        quotient, remainder = divmod(n, divisor)
        if remainder:
            divisor += 1
        else:
            factors.append(divisor)
            n = quotient
            if is_prime(n):
                factors.append(n)
                break
    return factors
