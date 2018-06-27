"""https://projecteuler.net/problem=6"""


def square_of_sums(*nums: int) -> int:
    """Square of the sum of `nums`."""
    return sum(nums) ** 2

def sum_of_squares(*nums: int) -> int:
    """Sum of the squares of `nums`."""
    return sum(n * n for n in nums)
