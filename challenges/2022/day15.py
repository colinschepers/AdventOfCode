import re
from typing import Iterable, Tuple

from utils import get_input, Coordinate


def get_x_ranges(row: int) -> Iterable[Tuple[int, int]]:
    for s_x, s_y, b_x, b_y in inputs:
        d_x = abs(s_x - b_x) + abs(s_y - b_y) - abs(s_y - row)
        yield s_x - d_x + int(s_x - d_x == b_x and row == b_y), s_x + d_x - int(s_x + d_x == b_x and row == b_y) + 1


def get_num_no_beacons(row: int) -> int:
    x_ranges = list(sorted(get_x_ranges(row)))
    total, prev_max_x = 0, float('-inf')
    for min_x, max_x in x_ranges:
        if max_x > prev_max_x:
            total += max_x - max(min_x, prev_max_x)
            prev_max_x = max_x
    return total


def get_just_outside_coords() -> Iterable[Coordinate]:
    for s_x, s_y, dist in distances:
        yield from ((s_x + d_x, s_y - (abs(d_x) - dist - 1)) for d_x in range(-dist - 1, dist + 2))
        yield from ((s_x + d_x, s_y + (abs(d_x) - dist - 1)) for d_x in range(-dist - 1, dist + 2))


def get_tuning_frequency(search_space: int) -> int:
    coords = ((x, y) for x, y in get_just_outside_coords() if 0 < x < search_space and 0 < y < search_space)
    for x, y in coords:
        if all(abs(s_x - x) + abs(s_y - y) > dist for s_x, s_y, dist in distances):
            return x * 4000000 + y


inputs = [tuple(map(int, re.findall("-?\\d+", line))) for line in get_input(year=2022, day=15)]
distances = [(s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)) for s_x, s_y, b_x, b_y in inputs]
is_example_input = len(inputs) < 20

print(get_num_no_beacons(10 if is_example_input else 2000000))
print(get_tuning_frequency(20 if is_example_input else 4000000))
