from collections.abc import Iterable
from typing import Tuple

from utils import get_input, Coordinate, Grid, iter_grid

Path = Tuple[Coordinate, ...]


def is_inside(grid: Grid, row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def get_uphill_neighbors(grid: Grid, row: int, col: int) -> Iterable[Coordinate]:
    return (
        (nr, nc)
        for nr, nc in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1))
        if is_inside(grid, nr, nc) and grid[row][col] == grid[nr][nc] - 1
    )


def get_trails(grid: Grid) -> Iterable[Path]:
    stack: list[Path] = [(coordinate,) for coordinate in iter_grid(grid, lambda x: x == 0)]
    while stack:
        path = stack.pop()
        if len(path) < 10:
            stack.extend(path + (neighbor,) for neighbor in get_uphill_neighbors(grid, *path[-1]))
        else:
            yield path


grid = [[int(char) for char in line] for line in get_input(2024, 10)]

trails = list(get_trails(grid))
print(len({(trail[0], trail[-1]) for trail in trails}))
print(len(trails))
