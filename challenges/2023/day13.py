from typing import Sequence

from more_itertools import first

from utils import split_lines, get_input


def _solve_horizontally(grid: Sequence[str], diff: int = 0) -> int:
    return first((
        split for split in range(1, len(grid))
        if sum(a != b for l1, l2 in zip(reversed(grid[:split]), grid[split:]) for a, b in zip(l1, l2)) == diff
    ), default=0)


def _solve(grid: Sequence[str], diff: int = 0) -> int:
    return _solve_horizontally(grid, diff) * 100 + _solve_horizontally(list(zip(*grid)), diff)


grids = split_lines(get_input(year=2023, day=13))
print(sum(_solve(grid) for grid in grids))
print(sum(_solve(grid, 1) for grid in grids))
