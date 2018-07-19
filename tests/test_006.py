"""https://projecteuler.net/problem=6"""

from euler.main import square_of_sums, sum_of_squares


def test_006() -> None:
    """Expected: 25164150"""
    hundred = range(1, 101)
    assert square_of_sums(*hundred) - sum_of_squares(*hundred) == 25164150
