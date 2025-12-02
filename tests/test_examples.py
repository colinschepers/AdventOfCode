from pathlib import Path
from unittest import mock

import pytest

from utils import get_solution, read_file

examples = [(path.parent.parent.name, path.stem) for path in Path("tests/examples").glob("**/inputs/*.txt")]


@pytest.mark.parametrize("year, example", examples)
def test_example(year: int, example: str):
    with mock.patch(
        'utils.get_input',
        lambda year, day, *args, **kwargs: read_file(f"tests/examples/{year}/inputs/{example}.txt")
    ):
        day = int(example[:2])
        expected = read_file(f"tests/examples/{year}/outputs/{example}.txt")
        actual = get_solution(year, day)
        assert actual == expected
