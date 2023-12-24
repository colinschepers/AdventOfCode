from collections import defaultdict
from datetime import datetime
from typing import Iterable, Sequence

from utils import get_input, Coordinate

Edges = list[list[int]]
Weights = list[list[int]]


def _get_neighbors(grid: Sequence[str], row: int, col: int, allow_climbing: bool) -> Iterable[Coordinate]:
    if not allow_climbing and grid[row][col] == "<":
        yield row, col - 1
    elif not allow_climbing and grid[row][col] == ">":
        yield row, col + 1
    elif not allow_climbing and grid[row][col] == "^":
        yield row - 1, col
    elif not allow_climbing and  grid[row][col] == "v":
        yield row + 1, col
    else:
        for r, c in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
            if 0 <= r < len(grid) and 0 <= c < len(grid[row]) and grid[r][c] != "#":
                yield r, c


def _get_intersection_graph(grid: Sequence[str], allow_climbing: bool) -> tuple[Edges, Weights]:
    start, end = (0, 1), (len(grid) - 1, len(grid[0]) - 2)

    intersections = defaultdict(lambda: defaultdict(int))
    stack = [(start, start, start, 0)]
    while stack:
        current, prev, prev_intersection, length = stack.pop()
        neighbors = [(r, c) for r, c in _get_neighbors(grid, *current, allow_climbing)]

        if len(neighbors) > 2 or current == end:
            intersections[prev_intersection][current] = length
            prev = current
            prev_intersection = current
            length = 0

        if current not in intersections:
            stack.extend((n, current, prev_intersection, length + 1) for n in neighbors if n != prev)

    intersections[end] = defaultdict(int)

    mapping = {x: i for i, x in enumerate(intersections)} | {i: x for i, x in enumerate(intersections)}
    edges = [
        [mapping[end]] if end in neighbors else [mapping[neighbor] for neighbor in neighbors]
        for neighbors in intersections.values()
    ]
    weights = [
        [neighbors[mapping[j]] for j in range(len(intersections))]
        for i, neighbors in enumerate(intersections.values())
    ]
    return edges, weights


def _dfs(edges: Edges, weights: Weights, current: int, end: int, total: int, visited: list[bool]) -> int:
    if current == end:
        return total

    maximum = 0
    for neighbor in edges[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            result = _dfs(edges, weights, neighbor, end, total + weights[current][neighbor], visited)
            if result > maximum:
                maximum = result
            visited[neighbor] = False
    return maximum


def _get_longest_path_length(edges: Edges, weights: Weights) -> int:
    return _dfs(edges, weights, 0, len(edges) - 1, 0, [False for _ in edges])


grid = get_input(year=2023, day=23)
print(_get_longest_path_length(*_get_intersection_graph(grid, allow_climbing=False)))
print(_get_longest_path_length(*_get_intersection_graph(grid, allow_climbing=True)))
