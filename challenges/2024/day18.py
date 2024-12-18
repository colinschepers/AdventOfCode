import heapq
from collections import defaultdict
from collections.abc import Sequence, Iterable, Set
from typing import Tuple

from utils import get_input, manhattan, Coordinate

Path = Tuple[Coordinate, ...]


def get_neighbors(
    row: int, col: int, height: int, width: int, blocked: Set[Coordinate]
) -> Iterable[Coordinate]:
    return (
        (nr, nc)
        for nr, nc in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1))
        if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in blocked
    )


def a_star(
    height: int, width: int, blocked: Set[Coordinate], path_hint: Path = tuple()
) -> Path | None:
    start = (0, 0)
    end = (height - 1, width - 1)
    open_set = {start}
    open_heap: list[Tuple[int, Coordinate, Path]] = [(0, start, (start,))]
    g_scores = defaultdict(lambda: 9999999999, {start: 0})
    f_scores = defaultdict(lambda: 9999999999, {start: manhattan(start, end)})
    priority_coords = set(path_hint)

    while open_heap:
        score, current, path = heapq.heappop(open_heap)
        open_set.remove(current)

        if current == end:
            return path

        for neighbor in get_neighbors(current[0], current[1], width, height, blocked):
            g_score = g_scores[current] + 1
            if g_score < g_scores[neighbor]:
                f_score = 0 if neighbor in priority_coords else g_score + manhattan(neighbor, end)
                g_scores[neighbor] = g_score
                f_scores[neighbor] = f_score
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heapq.heappush(open_heap, (f_score, neighbor, path + (neighbor,)))

    return None


def get_doom_coordinate(
    height: int, width: int, corrupted: Sequence[Coordinate]
) -> Coordinate | None:
    path = a_star(height, width, blocked=set())
    for i in range(len(corrupted)):
        if corrupted[i] in path:
            path = a_star(height, width, blocked=set(corrupted[:i + 1]), path_hint=path)
            if not path:
                return corrupted[i]
    return None


corrupted = [(int(s[0]), int(s[1])) for line in get_input(2024, 18) if (s := line.split(","))]
height, width = max(r for r, c in corrupted) + 1, max(c for r, c in corrupted) + 1
is_example = height == 7

print(len(a_star(height, width, set(corrupted[:12 if is_example else 1024]))) - 1)
print(",".join(map(str, get_doom_coordinate(height, width, corrupted))))
