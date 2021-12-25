from typing import Set, Tuple

from utils import get_input, Coordinate


def step(east: Set[Coordinate], south: Set[Coordinate]) -> Tuple[bool, Set[Coordinate], Set[Coordinate]]:
    moved, new_east, new_south = False, set(), set()

    for r, c in east:
        target = (r, (c + 1) % width)
        if target not in east and target not in south:
            new_east.add(target)
            moved = True
        else:
            new_east.add((r, c))

    for r, c in south:
        target = ((r + 1) % height, c)
        if target not in new_east and target not in south:
            new_south.add(target)
            moved = True
        else:
            new_south.add((r, c))

    return moved, new_east, new_south


def solve(east: Set[Coordinate], south: Set[Coordinate]) -> int:
    for i in range(1000):
        moved, east, south = step(east, south)
        if not moved:
            return i + 1


data = get_input(year=2021, day=25)
east = {(r, c) for r, line in enumerate(data) for c, char in enumerate(line) if char == '>'}
south = {(r, c) for r, line in enumerate(data) for c, char in enumerate(line) if char == 'v'}
height, width = len(data), len(data[0])

print(solve(east, south))
