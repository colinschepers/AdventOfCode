import heapq
from collections import defaultdict
from collections.abc import Sequence
from typing import Tuple

from utils import get_input, Grid, Coordinate, iter_grid

Path = Tuple[Coordinate, ...]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def a_star(grid: Grid) -> Tuple[int, Sequence[Path]]:
    start = next(iter(iter_grid(grid, lambda x: x == "S")))
    end = next(iter(iter_grid(grid, lambda x: x == "E")))

    open_heap = [(0, start, 0, (start,))]
    scores = defaultdict(lambda: 9999999999, {(start, 0): 0})

    best_score = 9999999999
    best_paths: list[Path] = []

    while open_heap:
        score, coordinate, direction, path = heapq.heappop(open_heap)

        if score > best_score:
            continue

        if coordinate == end:
            best_score = score
            best_paths.append(path)
            continue

        for rotation in (-1, 0, 1):
            next_dir = (direction + rotation) % 4
            next_coord = (coordinate[0] + DIRS[next_dir][0], coordinate[1] + DIRS[next_dir][1])
            next_state = (next_coord, next_dir)
            next_score = score + 1 + (1000 if rotation else 0)

            if not grid[next_coord[0]][next_coord[1]] != "#" or next_score > scores[next_state]:
                continue

            scores[next_state] = next_score
            heapq.heappush(open_heap, (next_score, next_coord, next_dir, path + (next_coord,)))

    return best_score, best_paths


grid = [[char for char in line] for line in get_input(2024, 16)]
score, paths = a_star(grid)
print(score)
print(len({coordinate for path in paths for coordinate in path}))
