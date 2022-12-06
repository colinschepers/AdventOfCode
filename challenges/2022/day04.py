from typing import Tuple

from utils import get_input


def fully_contains(a: Tuple, b: Tuple) -> bool:
    return a[0] <= b[0] and a[1] >= b[1]


def overlaps(a: Tuple, b: Tuple) -> bool:
    return a[0] <= b[1] and a[1] >= b[0]


data = [tuple(tuple(map(int, e.split('-'))) for e in line.split(',')) for line in get_input(year=2022, day=4)]

print(sum(1 if fully_contains(a, b) or fully_contains(b, a) else 0 for a, b in data))
print(sum(1 if overlaps(a, b) else 0 for a, b in data))
