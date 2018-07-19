"""Fixtures"""

from pathlib import Path
import pytest


_TEST_FILES = Path(__file__).parent / "test_files"


@pytest.fixture  # type: ignore
def p008() -> str:
    """Problem 008 data."""
    with open(_TEST_FILES / "problem_008.txt", "r") as f:
        return "".join([x.strip() for x in f.readlines()])
