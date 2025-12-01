import re
from math import prod
from typing import Sequence, Tuple

from utils import get_input


def _parse(lines: Sequence[str]) -> Sequence[Tuple[int, int]]:
    times = [int(m.group()) for m in re.finditer(r"\d+", lines[0])]
    distances = [int(m.group()) for m in re.finditer(r"\d+", lines[1])]
    return list(zip(times, distances))


def _binary_search(time: int, distance: int) -> int:
    left, right = 0, time + 1
    while left < right:
        hold_button = (left + right) // 2
        if hold_button * (time - hold_button) > distance:
            right = hold_button
        else:
            left = hold_button + 1
    return time - (2 * left) + 1


lines = get_input(year=2023, day=6)
print(prod(_binary_search(time, distance) for time, distance in _parse(lines)))

merged_time, merged_distance = _parse([line.replace(" ", "") for line in lines])[0]
print(_binary_search(merged_time, merged_distance))
