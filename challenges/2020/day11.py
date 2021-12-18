from typing import Set, Sequence

from utils import get_input, get_neighbors, Coordinate


def get_views_for_coordinate(chairs: Set[Coordinate], row: int, col: int) -> Sequence[Coordinate]:
    up_left = ((r, c) for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)) if (r, c) in chairs)
    up = ((r, col) for r in range(row - 1, -1, -1) if (r, col) in chairs)
    up_right = ((r, c) for r, c in zip(range(row - 1, -1, -1), range(col + 1, width)) if (r, c) in chairs)
    right = ((row, c) for c in range(col + 1, width) if (row, c) in chairs)
    down_right = ((r, c) for r, c in zip(range(row + 1, height), range(col + 1, width)) if (r, c) in chairs)
    down = ((r, col) for r in range(row + 1, width) if (r, col) in chairs)
    down_left = ((r, c) for r, c in zip(range(row + 1, height), range(col - 1, -1, -1)) if (r, c) in chairs)
    left = ((row, c) for c in range(col - 1, -1, -1) if (row, c) in chairs)
    return list(filter(bool, (next(up_left, None), next(up, None), next(up_right, None), next(right, None),
                              next(down_right, None), next(down, None), next(down_left, None), next(left, None))))


def solve_part_1(empties: Set[Coordinate], occupied: Set[Coordinate]) -> int:
    to_occupy = {(row, col) for row, col in empties
                 if not any((n_r, n_c) in occupied for n_r, n_c in neighbors[(row, col)])}
    to_empty = {(row, col) for row, col in occupied
                if sum((n_r, n_c) in occupied for n_r, n_c in neighbors[(row, col)]) >= 4}
    if not to_occupy and not to_empty:
        return len(occupied)
    return solve_part_1(empties - to_occupy | to_empty, occupied - to_empty | to_occupy)


def solve_part_2(empties: Set[Coordinate], occupied: Set[Coordinate]) -> int:
    to_occupy = {(row, col) for row, col in empties
                 if not any((n_r, n_c) in occupied for n_r, n_c in views[(row, col)])}
    to_empty = {(row, col) for row, col in occupied
                if sum((n_r, n_c) in occupied for n_r, n_c in views[(row, col)]) >= 5}
    if not to_occupy and not to_empty:
        return len(occupied)
    return solve_part_2(empties - to_occupy | to_empty, occupied - to_empty | to_occupy)


data = get_input(year=2020, day=11)
width, height = len(data[0]), len(data)
chairs = {(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val != '.'}
empties = {(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val == 'L'}
occupied = {(r, c) for r, row in enumerate(data) for c, val in enumerate(row) if val == '#'}
neighbors = {
    (row, col): list(get_neighbors(row, col, width, height, allow_diagonal=True))
    for row in range(height) for col in range(width)
}
views = {
    (row, col): get_views_for_coordinate(chairs, row, col)
    for row in range(height) for col in range(width)
}

print(solve_part_1(empties, occupied))
print(solve_part_2(empties, occupied))
