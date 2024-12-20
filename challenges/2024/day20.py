from collections.abc import Iterable, Set
from typing import Tuple

from utils import get_input, iter_grid, Coordinate


def get_neighbors(row: int, col: int, delta: int = 1) -> Iterable[Coordinate]:
    return (row + delta, col), (row, col + delta), (row - delta, col), (row, col - delta)


def get_path(current: Coordinate, end: Coordinate, walls: Set[Coordinate]) -> Iterable[Coordinate]:
    ignore = set(walls)

    yield current
    while current != end:
        ignore.add(current)
        current = next(iter(n for n in get_neighbors(*current) if n not in ignore))
        yield current


def get_saved_times_2ps(
    path: Tuple[Coordinate, ...], walls: Set[Coordinate], min_saved_time: int
) -> Iterable[int]:
    times_to_end = {coord: len(path) - 1 - i for i, coord in enumerate(path)}
    for current, time_to_end in times_to_end.items():
        for n1, n2 in zip(get_neighbors(*current), get_neighbors(*current, delta=2)):
            if n1 in walls and n2 in times_to_end:
                saved_time = time_to_end - times_to_end[n2] - 2
                if saved_time >= min_saved_time:
                    yield saved_time


def get_saved_times(
    path: Tuple[Coordinate, ...], min_saved_time: int, max_cheat_time: int
) -> Iterable[int]:
    times_to_end = {coord: len(path) - 1 - i for i, coord in enumerate(path)}

    for i in range(0, len(path) - min_saved_time):
        cheat_from = path[i]
        j = i + min_saved_time
        while j < len(path):
            cheat_to = path[j]

            cheat_time = abs(cheat_from[0] - cheat_to[0]) + abs(cheat_from[1] - cheat_to[1])
            if cheat_time <= max_cheat_time:
                j += 1
            else:
                j += cheat_time - max_cheat_time
                continue

            saved_time = times_to_end[cheat_from] - times_to_end[cheat_to] - cheat_time
            if saved_time >= min_saved_time:
                yield saved_time


grid = [[char for char in line] for line in get_input(2024, 20)]
start = next(iter(iter_grid(grid, lambda x: x == "S")))
end = next(iter(iter_grid(grid, lambda x: x == "E")))
walls = set(iter_grid(grid, lambda x: x == "#"))
path = tuple(get_path(start, end, walls))
is_example = len(path) < 100
min_saved_time = 50 if is_example else 100

print(len(list(get_saved_times_2ps(path, walls, min_saved_time))))
print(len(list(get_saved_times(path, min_saved_time, max_cheat_time=20))))
