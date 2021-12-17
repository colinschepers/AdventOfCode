from pathlib import Path
from unittest import mock

import pytest

from utils import get_solution, read_file

examples = [path.stem for path in Path("tests/examples").glob("*.in")]


@pytest.mark.parametrize("example", examples)
def test_example_for_day(example: str):
    year, day = map(int, example.split('-')[:2])
    with mock.patch('utils.get_input', lambda year, day: read_file(f"tests/examples/{example}.in")):
        expected = read_file(f"tests/examples/{example}.out")
        assert get_solution(year, day) == expected
