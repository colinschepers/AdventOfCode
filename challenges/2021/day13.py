from typing import Set

from utils import get_input, split_lines, Coordinate


def fold(coordinates: Set[Coordinate], value: int, is_vertical: bool) -> Set[Coordinate]:
    new_coordinates = set()
    for x, y in list(coordinates):
        if is_vertical and x > value:
            x = value - (x - value)
        if not is_vertical and y > value:
            y = value - (y - value)
        new_coordinates.add((x, y))
    return new_coordinates


def to_ascii(coordinates: Set[Coordinate]) -> str:
    width = max(x for x, y in coordinates) + 1
    height = max(y for x, y in coordinates) + 1
    grid = (('#' if (x, y) in coordinates else '.' for x in range(width)) for y in range(height))
    return '\n'.join(''.join(row) for row in grid)


coordinates, folds = split_lines(get_input(year=2021, day=13))
coordinates = {tuple(int(val) for val in line.split(',')) for line in coordinates}
folds = [line.split('=') for line in folds]
folds = [(int(right), left[-1] == 'x') for left, right in folds]

print(len(fold(coordinates, folds[0][0], folds[0][1])))

for value, is_vertical in folds:
    coordinates = fold(coordinates, value, is_vertical)

print(to_ascii(coordinates))
