from functools import cache

from more_itertools import first

from utils import get_input, iter_grid


@cache
def count_timelines(row: int, col: int) -> int:
    if row >= height or col >= width:
        return 1
    if (row, col) in splitters:
        splits.add((row, col))
        return count_timelines(row, col - 1) + count_timelines(row, col + 1)
    return count_timelines(row + 1, col)


lines = get_input(2025, 7)
width, height = len(lines[0]), len(lines)
start = first(iter_grid(lines, condition=lambda x: x == "S"))
splitters = set(iter_grid(lines, condition=lambda x: x == "^"))

splits = set()
timeline_count = count_timelines(*start)

print(len(splits))
print(timeline_count)
