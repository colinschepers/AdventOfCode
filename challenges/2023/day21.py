from math import ceil, floor
from typing import Sequence, Tuple, Iterable

from more_itertools import first

from utils import get_input, Coordinate, Grid


def _parse(lines: Sequence[str]) -> Tuple[Coordinate, Grid]:
    return (
        first((r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == "S"),
        [["." if char == "S" else char for char in line] for line in lines]
    )


def _can_go(r: int, c: int, is_infinite: bool = False) -> bool:
    if is_infinite or (0 <= r < len(grid) and 0 <= c < len(grid[r])):
        return grid[r % len(grid)][c % len(grid[0])] == "."
    return False


def _get_neighbors(r: int, c: int, is_infinite: bool = False) -> Iterable[Coordinate]:
    yield from ((r, c) for r, c in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)) if _can_go(r, c, is_infinite))


def _solve(step_count: int, is_infinite: bool = False) -> int:
    count, prev_count, step, size = 1, 0, 0, len(grid)
    border_counts, extrapolation_1, extrapolation_2 = [0] * size, [0] * size, [1] * size
    border, visited = {start}, {start}

    while any(x != 0 for x in extrapolation_2) or step % size > 0:
        border = {n for r, c in border for n in _get_neighbors(r, c, is_infinite) if n not in visited}
        visited.update(border)
        extrapolation_2[step % size] = len(border) - border_counts[step % size] - extrapolation_1[step % size]
        extrapolation_1[step % size] = len(border) - border_counts[step % size]
        border_counts[step % size] = len(border)
        count, prev_count = prev_count + len(border), count
        step += 1

        if step == step_count:
            return count

    final_polarity = step_count % 2
    count = count if final_polarity else prev_count
    steps_left = step_count - step
    for i, (border_count, extrapolation) in enumerate(zip(border_counts, extrapolation_1)):
        repeats = steps_left // size + int(i < steps_left % size)
        if int(i % 2 == final_polarity):
            repeats = ceil(repeats / 2)
            count += (border_count * repeats) + (extrapolation * repeats * repeats)
        else:
            repeats = floor(repeats / 2)
            count += (border_count * repeats) + (extrapolation * repeats * (repeats + 1))

    return count


start, grid = _parse(get_input(year=2023, day=21))
print(_solve(step_count=6 if len(grid) == 11 else 64, is_infinite=False))
print(_solve(step_count=100 if len(grid) == 11 else 26501365, is_infinite=True))
