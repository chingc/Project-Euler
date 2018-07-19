"""https://projecteuler.net/problem=5"""

from euler.main import lcm


def test_005() -> None:
    """Expected: 232792560"""
    assert lcm(*range(1, 21)) == 232792560
