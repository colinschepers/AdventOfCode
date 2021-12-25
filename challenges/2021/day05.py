import re
from collections import defaultdict
from typing import Sequence

from utils import get_input, Line


def solve(vent_lines: Sequence[Line], allow_diagonal: bool = True) -> int:
    vent_points = defaultdict(int)
    for (x1, y1), (x2, y2) in vent_lines:
        x_step = -1 if x1 > x2 else 1
        x_iter = range(x1, x2 + x_step, x_step)
        y_step = -1 if y1 > y2 else 1
        y_iter = range(y1, y2 + y_step, y_step)
        if y1 == y2:
            for x in x_iter:
                vent_points[(x, y1)] += 1
        elif x1 == x2:
            for y in y_iter:
                vent_points[(x1, y)] += 1
        elif allow_diagonal:
            for x, y in zip(x_iter, y_iter):
                vent_points[(x, y)] += 1
    return sum(cnt > 1 for cnt in vent_points.values())


data = get_input(year=2021, day=5)
data = [
    tuple((int(m[1]), int(m[2])) for m in re.finditer('(\d+),(\d+)', line))
    for line in data
]

print(solve(data, allow_diagonal=False))
print(solve(data, allow_diagonal=True))
