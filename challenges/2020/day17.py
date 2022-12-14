from typing import Set, Tuple, Sequence, Iterable

from utils import get_input


def get_neighbors_1(x: int, y: int, z: int) -> Iterable[Tuple[int, int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not (i == 0 and j == 0 and k == 0):
                    yield x + i, y + j, z + k


def get_neighbors_2(x: int, y: int, z: int, w: int) -> Iterable[Tuple[int, int, int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0 and l == 0):
                        yield x + i, y + j, z + k, w + l


def get_bounds_1(active: Set[Tuple[int, int, int]]) -> Tuple[int, int, int, int, int, int]:
    return min(x for x, _, _ in active), max(x for x, _, _ in active), \
           min(y for _, y, _ in active), max(y for _, y, _ in active), \
           min(z for _, _, z in active), max(z for _, _, z in active)


def get_bounds_2(active: Set[Tuple[int, int, int, int]]) -> Tuple[int, int, int, int, int, int, int, int]:
    return min(x for x, _, _, _ in active), max(x for x, _, _, _ in active), \
           min(y for _, y, _, _ in active), max(y for _, y, _, _ in active), \
           min(z for _, _, z, _ in active), max(z for _, _, z, _ in active), \
           min(w for _, _, _, w in active), max(w for _, _, _, w in active)


def run_cycles_1(data: Sequence[str], n: int):
    active = {(x, y, 0) for y, line in enumerate(data) for x, val in enumerate(line) if val == '#'}
    for _ in range(n):
        old_active = set(active)
        x_min, x_max, y_min, y_max, z_min, z_max = get_bounds_1(old_active)
        for z in range(z_min - 1, z_max + 2):
            for y in range(y_min - 1, y_max + 2):
                for x in range(x_min - 1, x_max + 2):
                    coord = (x, y, z)
                    is_active = coord in old_active
                    cnt = sum((nx, ny, nz) in old_active for nx, ny, nz in get_neighbors_1(x, y, z))
                    if is_active and not (2 <= cnt <= 3):
                        active.remove(coord)
                    elif not is_active and cnt == 3:
                        active.add(coord)
    return active


def run_cycles_2(data: Sequence[str], n: int):
    active = {(x, y, 0, 0) for y, line in enumerate(data) for x, val in enumerate(line) if val == '#'}
    for _ in range(n):
        old_active = set(active)
        x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max = get_bounds_2(old_active)
        for w in range(w_min - 1, w_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for y in range(y_min - 1, y_max + 2):
                    for x in range(x_min - 1, x_max + 2):
                        coord = (x, y, z, w)
                        is_active = coord in old_active
                        cnt = sum((nx, ny, nz, nw) in old_active for nx, ny, nz, nw in get_neighbors_2(x, y, z, w))
                        if is_active and not (2 <= cnt <= 3):
                            active.remove(coord)
                        elif not is_active and cnt == 3:
                            active.add(coord)
    return active


data = get_input(year=2020, day=17)
print(len(run_cycles_1(data, 6)))
print(len(run_cycles_2(data, 6)))
