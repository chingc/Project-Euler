"""https://projecteuler.net/problem=1"""


def test_p001() -> None:
    """Expected: 233168"""
    assert sum(x for x in range(3, 1000) if x % 3 == 0 or x % 5 == 0) == 233168
