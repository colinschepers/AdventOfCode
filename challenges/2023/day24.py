import re
from itertools import combinations, chain
from typing import Sequence, Tuple

from sympy import solve_poly_system, Symbol

from utils import get_input


def _has_intersection_2d(hailstone1: Tuple[int, ...], hailstone2: Tuple[int, ...]) -> bool:
    x1, y1, _, vx1, vy1, _ = hailstone1
    x2, y2, _, vx2, vy2, _ = hailstone2
    a1, a2 = (vy1 / vx1), (vy2 / vx2)
    is_parallel = a1 == a2
    if not is_parallel:
        b1, b2 = y1 - x1 * a1, y2 - x2 * a2
        intersect_x = round((b1 - b2) / (a2 - a1), 10)
        intersect_y = round(a1 * intersect_x + b1, 10)
        is_future = (intersect_x - x1) * vx1 > 0 and (intersect_x - x2) * vx2 > 0
        is_inside = min_value <= intersect_x <= max_value and min_value <= intersect_y <= max_value
        return is_future and is_inside
    return False


def _get_rock_position(hailstones: Sequence[Tuple[int, ...]]) -> Tuple[int, int, int] | None:
    xi, yi, zi, vxi, vyi, vzi = list(map(Symbol, ["x", "y", "z", "vx", "vy", "vz"]))
    times = [Symbol(f"t{i}") for i in range(len(hailstones))]
    equations = list(chain.from_iterable(
        [
            xi + vxi * t - (x + vx * t),
            yi + vyi * t - (y + vy * t),
            zi + vzi * t - (z + vz * t)
        ]
        for (x, y, z, vx, vy, vz), t in zip(hailstones, times)
    ))
    variables = [xi, yi, zi, vxi, vyi, vzi] + times
    return solve_poly_system(equations, variables)[0][:3]


hailstones = [tuple(map(int, re.findall(r"-?\d+", line))) for line in get_input(year=2023, day=24)]
min_value = 7 if len(hailstones) == 5 else 2E14
max_value = 29 if len(hailstones) == 5 else 4E14

print(sum(1 for hs1, hs2 in combinations(hailstones, 2) if _has_intersection_2d(hs1, hs2)))
print(sum(_get_rock_position(hailstones[:4])))
