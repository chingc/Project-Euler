"""https://projecteuler.net/problem=5"""

from typing import List

import pytest

from euler.problem_005 import lcm


@pytest.mark.parametrize("nums, ans", [  # type: ignore
    ([2, 5], 10),
    ([6, 21], 42),
    ([48, 180], 720),
    ([4, 7, 12, 21, 42], 84),
    ([11, 26, 31, 47, 52, 69, 72, 81, 99], 3105263304)
])
def test_lcm(nums: List[int], ans: int) -> None:
    """Expected: Correct LCM"""
    assert lcm(*nums) == ans

def test_005() -> None:
    """Expected: 232792560"""
    assert lcm(*range(1, 21)) == 232792560
