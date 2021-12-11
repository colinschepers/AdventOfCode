import pytest

from utils import get_solution

solutions = {
    1: (7, 5),
    2: (150, 900),
    3: (198, 230),
    4: (4512, 1924),
    5: (5, 12),
    6: (5934, 26984457539),
    7: (37, 168),
    8: (26, 61229),
    9: (15, 1134),
    10: (26397, 288957),
    11: (1656, 195)
}

test_data = (
    (day, part + 1, expected)
    for day in solutions
    for part, expected in enumerate(solutions[day])
)


@pytest.mark.parametrize("day, part, expected", test_data)
def test_example(day, part, expected):
    assert get_solution(day, part) == expected
