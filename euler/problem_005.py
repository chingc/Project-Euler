"""https://projecteuler.net/problem=5"""

from typing import Dict

from problem_003 import prime_factors


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
