from functools import lru_cache
from math import prod
from typing import Sequence, Set, Tuple, Iterable

from utils import get_input

Coordinate = Tuple[int, int]


def get_neighbors(row: int, col: int) -> Iterable[Coordinate]:
    if row > 0:
        yield row - 1, col
    if row < len(grid) - 1:
        yield row + 1, col
    if col > 0:
        yield row, col - 1
    if col < len(grid[row]) - 1:
        yield row, col + 1


@lru_cache
def get_low_points() -> Sequence[Coordinate]:
    return [(row, col) for row in range(len(grid)) for col in range(len(grid[row]))
            if all(grid[row][col] < grid[r][c] for r, c, in get_neighbors(row, col))]


def get_basin_sizes() -> Sequence[int]:
    def _get_basin_size(row: int, col: int, basin: Set[Coordinate]) -> int:
        basin.add((row, col))
        return 1 + sum(_get_basin_size(r, c, basin) for r, c in get_neighbors(row, col)
                       if grid[row][col] <= grid[r][c] < 9 and (r, c) not in basin)

    return [_get_basin_size(row, col, set()) for row, col in get_low_points()]


data = get_input(day=9)
grid = [[int(char) for char in line] for line in data]

print(sum(grid[row][col] + 1 for row, col in get_low_points()))
print(prod(sorted(get_basin_sizes(), reverse=True)[:3]))
