import re
from copy import deepcopy
from typing import Iterable

from more_itertools import chunked

from utils import get_input, Coordinate, Grid


def get_rocks(lines: Iterable[str]) -> Iterable[Coordinate]:
    for line in lines:
        coords = list(chunked((int(m[0]) for m in re.finditer(r"\d+", line)), 2))
        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    yield x, y


def get_grid(rocks: Iterable[Coordinate]) -> Grid:
    height = max(y for _, y in rocks) + 2
    x_range, y_range = range(500 - height - 1, 500 + height + 1), range(0, height)
    return [['#' if (x, y) in rocks else '.' for x in x_range] for y in y_range]


def solve(grid: Grid, x: int, y: int, endless: bool) -> int:
    if endless and y == len(grid):
        grid.clear()
    elif grid and y < len(grid) and grid[y][x] == '.':
        grid[y][x] = 'o'
        return solve(grid, x, y + 1, endless) + solve(grid, x - 1, y + 1, endless) + \
               solve(grid, x + 1, y + 1, endless) + bool(grid)
    return 0


grid = get_grid(set(get_rocks(get_input(year=2022, day=14))))
print(solve(deepcopy(grid), len(grid) + 1, 0, True))
print(solve(grid, len(grid) + 1, 0, False))
