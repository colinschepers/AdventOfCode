from collections import deque, Iterable
from typing import Tuple

from utils import get_input


def get_neighbors(x: int, y: int, z: int) -> Iterable[Tuple[int, int, int]]:
    yield from ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))


def is_open(coords: Tuple[int, int, int]) -> bool:
    if coords in cache:
        return cache[coords]

    stack, visited = deque([coords]), set()
    while stack:
        coords = stack.popleft()
        if coords not in cubes and coords not in visited:
            if cache.get(coords, False) or not all(limits[d][0] <= coords[d] <= limits[d][1] for d in (0, 1, 2)):
                cache.update({c: True for c in visited})
                return True
            visited.add(coords)
            stack.extend((neighbor for neighbor in get_neighbors(*coords)))
    cache.update({c: False for c in visited})
    return False


cubes = {tuple(map(int, line.split(","))) for line in get_input(year=2022, day=18)}
limits = [[f(cube[d] for cube in cubes) for f in (min, max)] for d in (0, 1, 2)]
cache = {cube: False for cube in cubes}

print(sum(int(neighbor not in cubes) for cube in cubes for neighbor in get_neighbors(*cube)))
print(sum(int(is_open(neighbor)) for cube in cubes for neighbor in get_neighbors(*cube)))
