from itertools import chain
from typing import Tuple, Iterable

from utils import get_input

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def _in_bounds(row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def _next_dirs(row: int, col: int, dir: int) -> Iterable[int]:
    horizontal = (dir == 0 or dir == 2)
    if (horizontal and grid[row][col] == "|") or (not horizontal and grid[row][col] == "-"):
        yield (dir + 1) % 4
        yield (dir - 1) % 4
    elif (horizontal and grid[row][col] == "/") or (not horizontal and grid[row][col] == "\\"):
        yield (dir - 1) % 4
    elif (horizontal and grid[row][col] == "\\") or (not horizontal and grid[row][col] == "/"):
        yield (dir + 1) % 4
    else:
        yield dir


def _step(row: int, col: int, dir: int) -> Iterable[Tuple[int, int, int]]:
    yield from ((row + DIRS[d][0], col + DIRS[d][1], d) for d in _next_dirs(row, col, dir))


def _solve(row: int, col: int, dir: int) -> int:
    visited = set()
    beams = [(row, col, dir)]
    while beams:
        current = beams.pop()
        visited.add(current)
        beams.extend(nxt for nxt in _step(*current) if _in_bounds(nxt[0], nxt[1]) and nxt not in visited)
    return len({(row, col) for row, col, _ in visited})


grid = get_input(year=2023, day=16)
starts = list(chain(
    ((r, 0, 0) for r in range(len(grid))),
    ((r, len(grid[0]) - 1, 2) for r in range(len(grid))),
    ((0, c, 1) for c in range(len(grid[0]))),
    ((len(grid) - 1, c, 3) for c in range(len(grid[0])))
))

print(_solve(0, 0, 0))
print(max(_solve(r, c, d) for r, c, d in starts))
