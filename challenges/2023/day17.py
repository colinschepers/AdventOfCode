import heapq
from collections import defaultdict
from typing import Tuple, Iterable

from utils import get_input, manhattan

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3


def _get_neighbors(
    row: int, col: int, dir: int, dir_len: int, min_dir: int, max_dir: int
) -> Iterable[Tuple[int, int, int, int]]:
    if col < len(grid[row]) - 1 and (dir_len < max_dir - 1 if dir == RIGHT else dir_len >= min_dir - 1) and dir != LEFT:
        yield row, col + 1, 0, dir_len + 1 if dir == 0 else 0
    if row < len(grid) - 1 and (dir_len < max_dir - 1 if dir == DOWN else dir_len >= min_dir - 1) and dir != UP:
        yield row + 1, col, 1, dir_len + 1 if dir == 1 else 0
    if col > 0 and (dir_len < max_dir - 1 if dir == LEFT else dir_len >= min_dir - 1) and dir != RIGHT:
        yield row, col - 1, 2, dir_len + 1 if dir == 2 else 0
    if row > 0 and (dir_len < max_dir - 1 if dir == UP else dir_len >= min_dir - 1) and dir != DOWN:
        yield row - 1, col, 3, dir_len + 1 if dir == 3 else 0


def _a_star(min_dir: int = 4, max_dir: int = 10) -> float:
    start = (0, 0)
    start_right = start + (RIGHT, 0)
    start_down = start + (DOWN, 0)
    end = (len(grid) - 1, len(grid) - 1)
    distance = manhattan(start, end)
    open_set = {start_right, start_down}
    open_heap = [(0.0, start_right), (0.0, start_down)]
    g_scores = defaultdict(lambda: float('inf'), {start_right: 0, start_down: 0})
    f_scores = defaultdict(lambda: float('inf'), {start_right: distance, start_down: distance})

    while open_set:
        current = heapq.heappop(open_heap)[1]
        open_set.remove(current)

        if (current[0], current[1]) == end:
            return min(g for (row, col, _, _), g in g_scores.items() if (row, col) == end)

        for neighbor in _get_neighbors(*current, min_dir, max_dir):
            row, col, _, _ = neighbor
            g_score = g_scores[current] + grid[row][col]
            if g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_scores[neighbor] = g_score + manhattan((row, col), end)
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heapq.heappush(open_heap, (f_scores[neighbor], neighbor))

    return float('inf')


grid = [list(map(int, line)) for line in get_input(year=2023, day=17)]
print(_a_star(min_dir=0, max_dir=3))
print(_a_star(min_dir=4, max_dir=10))
