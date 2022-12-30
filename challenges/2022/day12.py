import heapq
from collections import defaultdict
from typing import Iterable, Callable

from more_itertools import first

from utils import get_input, Coordinate


def get_neighbors(r: int, c: int) -> Iterable[Coordinate]:
    if r < len(heights) - 1 and heights[r + 1][c] >= heights[r][c] - 1:
        yield r + 1, c
    if c < len(heights[r]) - 1 and heights[r][c + 1] >= heights[r][c] - 1:
        yield r, c + 1
    if r > 0 and heights[r - 1][c] >= heights[r][c] - 1:
        yield r - 1, c
    if c > 0 and heights[r][c - 1] >= heights[r][c] - 1:
        yield r, c - 1


def search(start: Coordinate, is_goal: Callable[[Coordinate], bool]) -> Iterable[float]:
    open_set = {start}
    open_heap = [(0.0, start)]
    g_scores = defaultdict(lambda: float('inf'), {start: 0})

    while open_set:
        current = heapq.heappop(open_heap)[1]
        open_set.remove(current)

        if is_goal(current):
            yield g_scores[current]

        for neighbor in get_neighbors(*current):
            g_score = g_scores[current] + 1
            if g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heapq.heappush(open_heap, (g_scores[neighbor], neighbor))


lines = get_input(year=2022, day=12)
heights = [[ord(c.replace('S', 'a').replace('E', 'z')) - ord('a') for c in line] for line in lines]
start = first((r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == 'S')
end = first((r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == 'E')

print(first(search(end, lambda x: x == start)))
print(min(search(end, lambda x: heights[x[0]][x[1]] == 0)))
