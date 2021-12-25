import heapq
from collections import defaultdict

from utils import get_input, Grid, manhattan


def expand_grid(grid: Grid, count: int) -> Grid:
    new_grid = [[(x + i) % 9 + 1 for x in row] for i in range(-1, count - 1) for row in grid]
    for idx, row in enumerate(new_grid):
        new_grid[idx] += [(x + i) % 9 + 1 for i in range(count - 1) for x in row]
    return new_grid


def a_star(grid: Grid) -> float:
    start = (0, 0)
    end = (len(grid) - 1, len(grid) - 1)
    open_set = {start}
    open_heap = [(0.0, start)]
    g_scores = defaultdict(lambda: float('inf'), {start: 0})
    f_scores = defaultdict(lambda: float('inf'), {start: manhattan(start, end)})

    def _get_neighbors_fast(r, c):
        if r < len(grid) - 1:
            yield r + 1, c
        if c < len(grid) - 1:
            yield r, c + 1
        if r > 0:
            yield r - 1, c
        if c > 0:
            yield r, c - 1

    while open_set:
        current = heapq.heappop(open_heap)[1]
        open_set.remove(current)

        if current == end:
            return g_scores[end]

        for neighbor in _get_neighbors_fast(*current):
            g_score = g_scores[current] + grid[neighbor[0]][neighbor[1]]
            if g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_scores[neighbor] = g_score + manhattan(neighbor, end)
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heapq.heappush(open_heap, (f_scores[neighbor], neighbor))

    return float('inf')


grid = [[int(x) for x in line] for line in get_input(year=2021, day=15)]

print(a_star(grid))
print(a_star(expand_grid(grid, 5)))
