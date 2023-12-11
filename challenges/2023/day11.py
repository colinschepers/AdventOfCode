from itertools import combinations, accumulate
from typing import Sequence

from utils import Coordinate, manhattan, get_input


def _get_galaxies(lines: Sequence[str], expansion: int) -> Sequence[Coordinate]:
    row_idx = accumulate(1 if any(x == "#" for x in line) else expansion for line in lines)
    col_idx = list(accumulate(1 if any(x == "#" for x in line) else expansion for line in zip(*lines)))
    return [(row, col) for row, line in zip(row_idx, lines) for col, char in zip(col_idx, line) if char == '#']


lines = get_input(year=2023, day=11)
print(sum(manhattan(a, b) for a, b in combinations(_get_galaxies(lines, 2), 2)))
print(sum(manhattan(a, b) for a, b in combinations(_get_galaxies(lines, 1000000), 2)))
