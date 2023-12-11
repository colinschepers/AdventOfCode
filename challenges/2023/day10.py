from collections.abc import Set
from typing import Sequence, Iterable, Tuple

from more_itertools import first

from utils import get_input, Coordinate, get_neighbors

NORTH = {"|", "L", "J", "S"}
SOUTH = {"|", "7", "F", "S"}
WEST = {"-", "7", "J", "S"}
EAST = {"-", "F", "L", "S"}


def _get_next_pipe(path: Sequence[Coordinate]) -> Coordinate:
    row, col = path[-1]
    previous = path[-2] if len(path) > 1 else (-1, -1)
    if col < len(grid[0]) - 1 and (row, col + 1) != previous and grid[row][col] in EAST and grid[row][col + 1] in WEST:
        return row, col + 1
    if row < len(grid) - 1 and (row + 1, col) != previous and grid[row][col] in SOUTH and grid[row + 1][col] in NORTH:
        return row + 1, col
    if col > 0 and (row, col - 1) != previous and grid[row][col] in WEST and grid[row][col - 1] in EAST:
        return row, col - 1
    if row > 0 and (row - 1, col) != previous and grid[row][col] in NORTH and grid[row - 1][col] in SOUTH:
        return row - 1, col


def _get_rhs_coordinates(current_coordinate: Coordinate, next_coordinate: Coordinate) -> Iterable[Coordinate]:
    row, col = current_coordinate
    next_row, next_col = next_coordinate
    if grid[row][col] == "|" and next_row < row:
        yield row, col + 1
    elif grid[row][col] == "|" and next_row > row:
        yield row, col - 1
    elif grid[row][col] == "-" and next_col < col:
        yield row - 1, col
    elif grid[row][col] == "-" and next_col > col:
        yield row + 1, col
    elif grid[row][col] == "J" and next_col == col:
        yield row + 1, col
        yield row, col + 1
    elif grid[row][col] == "L" and next_row == row:
        yield row + 1, col
        yield row, col - 1
    elif grid[row][col] == "F" and next_col == col:
        yield row - 1, col
        yield row, col - 1
    elif grid[row][col] == "7" and next_row == row:
        yield row - 1, col
        yield row, col + 1


def _in_grid(coordinate: Coordinate) -> bool:
    return 0 < coordinate[0] < len(grid) and 0 < coordinate[1] < len(grid[0])


def _solve() -> Tuple[Set[Coordinate], Set[Coordinate]]:
    start = first((r, c) for r, line in enumerate(grid) for c, char in enumerate(line) if char == "S")

    path = [start]
    rhs_coordinates = set()
    while (next_pipe := _get_next_pipe(path)) != path[0]:
        path.append(next_pipe)
        rhs_coordinates.update(c for c in _get_rhs_coordinates(path[-2], path[-1]) if _in_grid(c))

    path = set(path)
    rhs_coordinates -= set(path)

    expanded = {0}
    while expanded:
        expanded = {
            neighbor
            for row, col in rhs_coordinates
            for neighbor in get_neighbors(row, col, len(grid[0]), len(grid))
            if neighbor not in path and neighbor not in rhs_coordinates
        }
        rhs_coordinates.update(expanded)

    return path, rhs_coordinates


grid = get_input(year=2023, day=10)
path, enclosed = _solve()

print(len(path) // 2)
print(len(enclosed))
