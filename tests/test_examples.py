from pathlib import Path
from unittest import mock

import pytest

from utils import get_solution, read_file

examples = [(path.parent.parent.name, path.stem) for path in Path("tests/examples").glob("**/inputs/*.txt")]


@pytest.mark.parametrize("year, example", examples)
def test_example_for_day(year: int, example: str):
    day = int(example[:2])
    with mock.patch('utils.get_input', lambda year, day: read_file(f"tests/examples/{year}/inputs/{example}.txt")):
        expected = read_file(f"tests/examples/{year}/outputs/{example}.txt")
        actual = get_solution(year, day)
        assert actual == expected
