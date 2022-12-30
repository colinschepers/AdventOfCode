from collections import defaultdict
from collections import defaultdict
from datetime import datetime
from functools import lru_cache, reduce
from typing import Set, Dict

from more_itertools import first, last

from utils import get_input, Coordinate

DIRECTIONS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def get_next_state(state: Dict[Coordinate, str]) -> Dict[Coordinate, str]:
    new_state = defaultdict(str)
    for (row, col), blizzards in state.items():
        for blizzard_dir in blizzards:
            new_row = (row - 1 + DIRECTIONS[blizzard_dir][0]) % (height - 2) + 1
            new_col = (col - 1 + DIRECTIONS[blizzard_dir][1]) % (width - 2) + 1
            new_state[(new_row, new_col)] += blizzard_dir
    return new_state


@lru_cache(maxsize=None)
def get_state(minute: int) -> Dict[Coordinate, str]:
    if minute <= 0:
        return initial_state
    return get_next_state(get_state(minute - 1))


@lru_cache(maxsize=None)
def get_empty_coordinates(minute: int) -> Set[Coordinate]:
    return {c for c in coordinates if c not in get_state(minute)}


@lru_cache(maxsize=None)
def get_neighbors(position: Coordinate):
    return [(position[0] + direction[0], position[1] + direction[1]) for direction in DIRECTIONS.values()] + [position]


@lru_cache(maxsize=None)
def solve(start: Coordinate, end: Coordinate, start_minute: int = 0) -> int:
    open_set, minute = {start}, start_minute
    while end not in open_set and (minute := minute + 1) < 100000:
        open_set = get_empty_coordinates(minute).intersection((np for p in open_set for np in get_neighbors(p)))
    return minute


lines = get_input(year=2022, day=24)
height, width = len(lines), len(lines[0])
walls = set((r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == '#')
coordinates = [(r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char != '#']
initial_state = {(r, c): lines[r][c] for r, c in coordinates if lines[r][c] in DIRECTIONS}
start = first((r, c) for r, c in coordinates if lines[r][c] == '.')
end = last((r, c) for r, c in coordinates if lines[r][c] == '.')

print(solve(start, end))
print(reduce(lambda minutes, path: solve(*path, minutes), [(start, end), (end, start), (start, end)], 0))
