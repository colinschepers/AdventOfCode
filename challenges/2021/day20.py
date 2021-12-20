from datetime import datetime
from typing import Tuple, Set

from utils import get_input, split_lines, Coordinate

BITS = tuple(1 << i for i in range(9))


def get_neighbors(x, y):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            yield x - dx, y - dy


def get_bounds(image: Set[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    return min(x for x, _ in image), max(x for x, _ in image), \
           min(y for _, y in image), max(y for _, y in image)


def get_next_border(border: Set[Coordinate], x_min: int, x_max: int, y_min: int, y_max: int) -> Set[Coordinate]:
    if 0 in enhancement and not border:
        for x in range(x_min - 2, x_max + 3):
            border.add((x, y_min - 2))
            border.add((x, y_min - 1))
            border.add((x, y_max + 1))
            border.add((x, y_max + 2))
        for y in range(y_min - 2, y_max + 3):
            border.add((x_min - 2, y))
            border.add((x_min - 1, y))
            border.add((x_max + 1, y))
            border.add((x_max + 2, y))
    elif border:
        border = set()
    return border


def evolve(image: Set[Coordinate], x_min: int, x_max: int, y_min: int, y_max: int) -> Set[Coordinate]:
    new_image = set()
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            idx = 0
            for neighbor, bit in zip(get_neighbors(x, y), BITS):
                if neighbor in image:
                    idx += bit
            if idx in enhancement:
                new_image.add((x, y))
    return new_image


def solve(image: Set[Coordinate], turns: int) -> int:
    x_min, x_max, y_min, y_max = get_bounds(image)
    border = set()
    for _ in range(turns):
        x_min, x_max, y_min, y_max = x_min - 1, x_max + 1, y_min - 1, y_max + 1
        image = evolve(image | border, x_min, x_max, y_min, y_max)
        border = get_next_border(border, x_min, x_max, y_min, y_max)
    return len(image)


enhancement, image = split_lines(get_input(year=2021, day=20))
enhancement = {i for i, char in enumerate(''.join(enhancement)) if char == '#'}
image = {(x, y) for y, line in enumerate(image) for x, char in enumerate(line) if char == '#'}

print(solve(image, 2))
print(solve(image, 50))
