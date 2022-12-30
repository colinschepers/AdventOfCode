from datetime import datetime, timedelta
from unittest import mock

import pytest

from utils import get_solution, get_input, get_years, get_days

challenges = [(year, day) for year in get_years() for day in get_days(year)
              if year <= 2021]
inputs = {(year, day): get_input(year, day) for year, day in challenges}


@pytest.mark.parametrize("year, day", challenges)
def test_running_time(year: int, day: int):
    with mock.patch('utils.get_input', lambda year, day: inputs[(year, day)]):
        start = datetime.now()
        solution = get_solution(year, day)
        elapsed = datetime.now() - start
    assert solution
    assert elapsed < timedelta(seconds=10)
