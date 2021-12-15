from typing import Set

from utils import get_input, iter_grid, get_neighbors, Coordinate


def flash(row: int, col: int, flashed: Set[Coordinate]):
    if (row, col) not in flashed:
        flashed.add((row, col))
        for r, c in get_neighbors(octopuses, row, col, allow_diagonal=True):
            octopuses[r][c] += 1
            if octopuses[r][c] > 9:
                flash(r, c, flashed)


def step() -> int:
    flashed = set()
    for row, col in iter_grid(octopuses):
        octopuses[row][col] += 1
    for row, col in iter_grid(octopuses, lambda x: x > 9):
        flash(row, col, flashed)
    for row, col in iter_grid(octopuses, lambda x: x > 9):
        octopuses[row][col] = 0
    return len(flashed)


data = get_input(day=11)

octopuses = [[int(char) for char in line] for line in data]
print(sum(step() for _ in range(100)))

octopuses = [[int(char) for char in line] for line in data]
octopus_count = len(octopuses) * len(octopuses[0])
print(next(i + 1 for i in range(1000) if step() == octopus_count))
