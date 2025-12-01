from collections import Counter
from typing import Set, Tuple, Generator, Optional

from utils import get_input, Coordinate

directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
propositions = [((-1, -1), (-1, 0), (-1, 1)), ((1, 1), (1, 0), (1, -1)),
                ((1, -1), (0, -1), (-1, -1)), ((-1, 1), (0, 1), (1, 1))]


def is_free(row: int, col: int, directions: Tuple[Coordinate, ...], elves: Set[Coordinate]) -> bool:
    for dr, dc in directions:
        if (row + dr, col + dc) in elves:
            return False
    return True


def get_next(row: int, col: int, elves: Set[Coordinate]) -> Optional[Coordinate]:
    if not is_free(row, col, directions, elves):
        for proposition in propositions:
            if is_free(row, col, proposition, elves):
                return row + proposition[1][0], col + proposition[1][1]
    return row, col


def solve(elves: Set[Coordinate]) -> Generator:
    round, new_elves = 0, elves
    while round == 0 or elves != new_elves:
        elves = new_elves
        if round == 10:
            rows, cols = zip(*elves)
            yield (max(rows) + 1 - min(rows)) * (max(cols) + 1 - min(cols)) - len(elves)

        new_locations = [get_next(r, c, elves) for r, c in elves]
        new_location_counts = Counter(new_locations)
        new_elves = {ne if new_location_counts[ne] == 1 else e for e, ne in zip(elves, new_locations)}
        propositions.append(propositions.pop(0))
        round += 1
    yield round


elves = {(r, c) for r, line in enumerate(get_input(year=2022, day=23)) for c, char in enumerate(line) if char == '#'}
solutions = solve(elves)
print(next(solutions))
print(next(solutions))
