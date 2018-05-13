"""https://projecteuler.net/problem=5"""

from typing import Dict, List

import pytest

from test_003 import prime_factors


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


@pytest.mark.parametrize("nums, ans", [
    ([2, 5], 10),
    ([6, 21], 42),
    ([48, 180], 720),
    ([4, 7, 12, 21, 42], 84),
    ([11, 26, 31, 47, 52, 69, 72, 81, 99], 3105263304)
])
def test_lcm(nums: List[int], ans: int) -> None:
    """Expected: Correct LCM"""
    assert lcm(*nums) == ans

def test_p005() -> None:
    """Expected: 232792560"""
    assert lcm(*range(1, 21)) == 232792560
