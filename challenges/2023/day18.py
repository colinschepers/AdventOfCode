from itertools import accumulate
from typing import Sequence, Tuple

from utils import get_input, manhattan, Coordinate

DIRS = {"R": (0, 1), "0": (0, 1), "D": (1, 0), "1": (1, 0), "L": (0, -1), "2": (0, -1), "U": (-1, 0), "3": (-1, 0)}


def _get_corners(plan: Sequence[Tuple[Tuple[int, int], int]]) -> Sequence[Coordinate]:
    return list(accumulate(plan, lambda prev, x: (prev[0] + x[0][0] * x[1], prev[1] + x[0][1] * x[1]), initial=(0, 0)))


def _solve(corners: Sequence[Coordinate]) -> int:
    shoe_lace = abs(sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in zip(corners, corners[1:]))) // 2
    circumference = sum(manhattan(a, b) for a, b in zip(corners, corners[1:]))
    return shoe_lace + circumference // 2 + 1


lines = get_input(year=2023, day=18)
print(_solve(_get_corners([(DIRS[line[0]], int(line.split(" ")[1])) for line in lines])))
print(_solve(_get_corners([(DIRS[line[-2]], int(line.split("#")[1][:5], 16)) for line in lines])))
