"""Functions to solve Project Euler problems."""

from typing import Dict, Iterator, List, Tuple


def adjacent_digits(n: int, digits: str) -> List[str]:
    """List of all adjacent digits of `n` length in `digits`."""
    adjacents = []
    while len(digits) >= n:
        adjacents.append(digits[:n])
        digits = digits[1:]
    return adjacents

def fibo(nth: int) -> List[int]:
    """Fibonacci numbers up to the `nth` term starting with 0 and 1."""
    fibos = [0, 1]
    for _ in range(nth - 2):  # - 2 because we already have the first two
        fibos.append(fibos[-1] + fibos[-2])
    return fibos

def is_palindrome(s: str) -> bool:
    """Determine if `s` is the same forwards and backwards."""
    return s == s[::-1]

def is_prime(n: int) -> bool:
    """Determine if `n` is prime."""
    if n < 2 or str(n)[-1] in [0, 2, 4, 5, 6, 8]:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):  # n ** 0.5 == sqrt(n)
        if n % divisor == 0:
            return False
    return True

def largest_palindrome(n: int) -> int:
    """Largest palindrome made from the product of two `n`-digit numbers."""
    candidates = []
    start = int("9" * n)
    stop = int((start + 1) / 2)  # don't check entire space these will all be too small
    for i in range(start, stop, -1):
        for j in range(i, stop, -1):
            if is_palindrome(str(i * j)):
                candidates.append(i * j)
    return max(*candidates)

def lcm(*nums: int) -> int:
    """Least Common Multiple of the given `nums`."""
    highest_degrees: Dict[int, int] = {}
    for num in nums:
        factors = prime_factors(num)
        for factor in factors:
            degree = factors.count(factor)
            if factor not in highest_degrees or degree > highest_degrees[factor]:
                highest_degrees[factor] = degree
    ans = 1
    for factor, degree in highest_degrees.items():
        ans *= factor ** degree
    return ans

def nth_prime(nth: int) -> int:
    """Determine the `nth` prime."""
    current = 0
    while nth > 0:
        current += 1
        if is_prime(current):
            nth -= 1
    return current

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

def pythagorean_triples(upper: int, lower: int = 3) -> Iterator[Tuple[int, int, int]]:
    """Pythagorean triples where no side is longer than `upper` bound."""
    for a in range(lower, upper):
        for b in range(lower, upper):
            for c in range(lower, upper):
                if a < b < c and a * a + b * b == c * c:
                    yield (a, b, c)

def square_of_sums(*nums: int) -> int:
    """Square of the sum of `nums`."""
    return sum(nums) ** 2

def sum_of_squares(*nums: int) -> int:
    """Sum of the squares of `nums`."""
    return sum(n * n for n in nums)
