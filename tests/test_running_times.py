from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

import pytest

from utils import get_solution, get_input

challenges = [(int(folder.name), int(file.stem[-2:]))
              for folder in Path("challenges").glob("**/") for file in folder.glob("day*.py")]
inputs = {(year, day): get_input(year, day) for year, day in challenges}


@pytest.mark.parametrize("year, day", challenges)
def test_running_time(year: int, day: int):
    with mock.patch('utils.get_input', lambda year, day: inputs[(year, day)]):
        start = datetime.now()
        solution = get_solution(year, day)
        elapsed = datetime.now() - start
    assert solution
    assert elapsed < timedelta(seconds=10)
