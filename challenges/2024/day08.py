from collections import defaultdict
from collections.abc import Iterable
from itertools import combinations

from utils import get_input, iter_grid, Grid, Coordinate

Antennas = dict[str, list[Coordinate]]


def is_inside(grid: Grid, coordinate: Coordinate) -> bool:
    return 0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0])


def get_antennas(grid: Grid) -> Antennas:
    antennas: Antennas = defaultdict(list)
    for row, col in iter_grid(grid, lambda x: x != "."):
        antennas[grid[row][col]].append((row, col))
    return antennas


def get_antinodes_for(
    grid: Grid, a: Coordinate, b: Coordinate, updated_model: bool
) -> Iterable[Coordinate]:
    diff = (a[0] - b[0], a[1] - b[1])
    coordinate = (a[0] + diff[0], a[1] + diff[1])

    if updated_model:
        yield a
        while is_inside(grid, coordinate):
            yield coordinate
            coordinate = (coordinate[0] + diff[0], coordinate[1] + diff[1])
    elif is_inside(grid, coordinate):
        yield coordinate


def get_antinodes(grid: Grid, antennas: Antennas, updated_model: bool) -> Iterable[Coordinate]:
    for coordinates in antennas.values():
        for a, b in combinations(coordinates, 2):
            yield from get_antinodes_for(grid, a, b, updated_model)
            yield from get_antinodes_for(grid, b, a, updated_model)


grid = [[char for char in line] for line in get_input(2024, 8)]
antennas = get_antennas(grid)

print(len(set(get_antinodes(grid, antennas, updated_model=False))))
print(len(set(get_antinodes(grid, antennas, updated_model=True))))
