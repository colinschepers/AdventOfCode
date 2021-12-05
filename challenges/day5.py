import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Sequence, Tuple

from utils import get_input

Line = Tuple["Coordinate", "Coordinate"]


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


def solve(vent_lines: Sequence[Line], allow_diagonal: bool = True):
    vent_points = defaultdict(int)
    for c1, c2 in vent_lines:
        x_step = -1 if c1.x > c2.x else 1
        x_iter = range(c1.x, c2.x + x_step, x_step)
        y_step = -1 if c1.y > c2.y else 1
        y_iter = range(c1.y, c2.y + y_step, y_step)
        if c1.y == c2.y:
            for x in x_iter:
                vent_points[Coordinate(x, c1.y)] += 1
        elif c1.x == c2.x:
            for y in y_iter:
                vent_points[Coordinate(c1.x, y)] += 1
        elif allow_diagonal:
            for x, y in zip(x_iter, y_iter):
                vent_points[Coordinate(x, y)] += 1
    return sum(cnt > 1 for cnt in vent_points.values())


data = get_input(5)
data = [
    tuple(Coordinate(int(m[1]), int(m[2])) for m in re.finditer('(\d+),(\d+)', line))
    for line in data
]

print(solve(data, allow_diagonal=False))
print(solve(data, allow_diagonal=True))
