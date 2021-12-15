from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

import pytest

from utils import get_solution, get_input

days = [int(path.stem[-2:]) for path in Path("challenges").glob("day*.py")]
inputs = {day: get_input(day) for day in days}


def get_input_from_cache(day):
    return inputs[day]


@pytest.mark.parametrize("day", days)
def test_running_time_for_day(day: int):
    with mock.patch('utils.get_input', get_input_from_cache):
        start = datetime.now()
        _ = get_solution(day)
        elapsed = datetime.now() - start
    assert elapsed < timedelta(seconds=1)
