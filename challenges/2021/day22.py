import re
from collections import defaultdict
from math import prod
from typing import Sequence, Tuple, Optional

from utils import get_input

Bounds = Tuple[int, ...]


def size(bounds: Bounds) -> int:
    return prod(max_value - min_value + 1 for min_value, max_value in zip(bounds[::2], bounds[1::2]))


def get_intersection(a: Bounds, b: Bounds) -> Optional[Bounds]:
    x_min, x_max = max(a[0], b[0]), min(a[1], b[1])
    y_min, y_max = max(a[2], b[2]), min(a[3], b[3])
    z_min, z_max = max(a[4], b[4]), min(a[5], b[5])
    if x_min <= x_max and y_min <= y_max and z_min <= z_max:
        return x_min, x_max, y_min, y_max, z_min, z_max


def process(input_data: Sequence[Tuple[bool, Bounds]]) -> int:
    weights = defaultdict(int)
    for turn_on, bounds in input_data:
        for other_bounds, other_weight in list(weights.items()):
            if intersection := get_intersection(bounds, other_bounds):
                weights[intersection] -= other_weight
        if turn_on:
            weights[bounds] += 1
        weights = defaultdict(int, {cube: weight for cube, weight in weights.items() if weight != 0})
    return sum(weight * size(bounds) for bounds, weight in weights.items())


data = [(line[:2] == 'on', tuple(map(int, re.findall(r"-?\d+", line)))) for line in get_input(year=2021, day=22)]
print(process([(turn_on, bounds) for turn_on, bounds in data if all(-50 <= value <= 50 for value in bounds)]))
print(process(data))
