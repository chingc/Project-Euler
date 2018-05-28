"""https://projecteuler.net/problem=6"""


def sum_of_squares(*nums: int) -> int:
    """Sum of the squares of `nums`."""
    return sum(n * n for n in nums)

def square_of_sums(*nums: int) -> int:
    """Square of the sum of `nums`."""
    return sum(nums) ** 2

#####

def test_sum_of_squares() -> None:
    """Expected: 385"""
    assert sum_of_squares(*range(1, 11)) == 385

def test_square_of_sums() -> None:
    """Expected: 3025"""
    assert square_of_sums(*range(1, 11)) == 3025

def test_p006() -> None:
    """Expected: 25164150"""
    hundred = range(1, 101)
    assert square_of_sums(*hundred) - sum_of_squares(*hundred) == 25164150
