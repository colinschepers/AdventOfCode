from collections.abc import Iterable
from typing import Tuple

from utils import get_input, iter_grid, Grid, Coordinate

CoordinateWithDirection = Tuple[Coordinate, int]

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
OUTSIDE: CoordinateWithDirection = ((-1, -1), -1)


def is_outside(grid: Grid, coordinate: Coordinate) -> bool:
    return not (0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0]))


def is_wall(grid: Grid, coordinate: Coordinate) -> bool:
    return grid[coordinate[0]][coordinate[1]] == "#"


def get_next_coordinate(coordinate: Coordinate, dir: int) -> Coordinate:
    return coordinate[0] + DIRS[dir][0], coordinate[1] + DIRS[dir][1]


def step(
    grid: Grid, guard: CoordinateWithDirection, obstruction: Coordinate | None = None
) -> CoordinateWithDirection:
    coordinate, dir = guard
    next_coordinate = get_next_coordinate(coordinate, dir)
    if is_outside(grid, next_coordinate):
        return OUTSIDE
    elif is_wall(grid, next_coordinate) or next_coordinate == obstruction:
        return coordinate, (dir + 1) % 4
    return next_coordinate, dir


def walk(
    grid: Grid, guard: CoordinateWithDirection, obstruction: Coordinate | None = None
) -> Iterable[CoordinateWithDirection]:
    while guard != OUTSIDE:
        yield guard
        guard = step(grid, guard, obstruction)


def has_cycle(grid: Grid, guard: CoordinateWithDirection, obstruction: Coordinate) -> bool:
    seen: set[CoordinateWithDirection] = set()
    for guard in walk(grid, guard, obstruction):
        if guard in seen:
            return True
        seen.add(guard)
    return False


def get_obstructions(grid: Grid, guard: CoordinateWithDirection) -> Iterable[Coordinate]:
    obstructions: set[Coordinate] = set()
    for guard in walk(grid, guard):
        obstruction = get_next_coordinate(*guard)
        if (
            obstruction not in obstructions
            and not is_outside(grid, obstruction)
            and not is_wall(grid, obstruction)
            and has_cycle(grid, guard, obstruction)
        ):
            yield obstruction
        obstructions.add(obstruction)


grid = [list(row) for row in get_input(2024, 6)]
guard: CoordinateWithDirection = next(iter(iter_grid(grid, lambda x: x == "^"))), 0

print(len(set(coordinate for coordinate, direction in walk(grid, guard))))
print(len(set(get_obstructions(grid, guard))))
