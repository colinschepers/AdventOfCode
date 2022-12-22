import re
from datetime import datetime
from functools import lru_cache
from typing import Callable, Tuple

from more_itertools import first

from utils import get_input, read_file

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
cube_mapping_input = {
    (0, 1, 2): (2, 3, 0), (0, 1, 3): (3, 3, 0), (0, 2, 0): (2, 2, 2), (0, 2, 1): (1, 2, 2), (0, 2, 3): (0, 0, 3),
    (1, 1, 0): (1, 2, 3), (1, 1, 2): (1, 0, 1), (2, 0, 2): (0, 0, 0), (2, 0, 3): (1, 0, 0), (2, 1, 0): (0, 3, 2),
    (2, 1, 1): (3, 1, 2), (3, 0, 0): (3, 1, 3), (3, 0, 1): (3, 2, 1), (3, 0, 2): (3, 1, 1)
}
cube_mapping_example = {
    (0, 2, 0): (2, 0, 2), (0, 2, 2): (0, 1, 1), (0, 1, 3): (0, 0, 1), (1, 0, 1): (3, 2, 3), (1, 0, 2): (3, 3, 3),
    (1, 0, 3): (3, 2, 1), (1, 1, 1): (2, 1, 0), (1, 1, 3): (0, 1, 0), (1, 2, 0): (1, 3, 1), (2, 2, 1): (2, 0, 3),
    (2, 2, 2): (2, 1, 3), (2, 3, 0): (0, 3, 2), (2, 3, 1): (1, 3, 0), (2, 3, 3): (1, 3, 2)
}


@lru_cache(maxsize=None)
def rotate_face_right(row: int, col: int, dir: int) -> Tuple[int, int, int]:
    dice_row, dice_col, face_row, face_col = row // face_size, col // face_size, row % face_size, col % face_size
    return face_col + face_size * dice_row, (face_size - 1 - face_row) + face_size * dice_col, (dir + 1) % 4


@lru_cache(maxsize=None)
def move_2d(row: int, col: int, dir: int) -> Tuple[int, int, int]:
    beam = (((row + directions[dir][0] * cnt) % len(map), (col + directions[dir][1] * cnt) % len(lines[row]))
            for cnt in range(1, len(lines)))
    r, c = first((r, c) for r, c in beam if map[r][c] != ' ')
    return (r, c, dir) if map[r][c] == '.' else (row, col, dir)


@lru_cache(maxsize=None)
def move_on_cube(row: int, col: int, dir: int) -> Tuple[int, int, int]:
    r, c, d = (row + directions[dir][0]) % size, (col + directions[dir][1]) % size, dir
    if map[r][c] == ' ':
        dice_row, dice_col = row // face_size, col // face_size
        target_row, target_col, target_dir = cube_mapping.get((dice_row, dice_col, dir), (dice_row, dice_col, dir))
        r, c = row + (target_row - dice_row) * face_size, col + (target_col - dice_col) * face_size
        while d != target_dir:
            r, c, d = rotate_face_right(r, c, d)
        r, c = (r + directions[d][0]) % size, (c + directions[d][1]) % size
    return (r, c, d) if map[r][c] == '.' else (row, col, dir)


def get_password(move_func: Callable) -> int:
    (row, col), dir = first((r, c) for r, row in enumerate(map) for c, char in enumerate(row) if map[r][c] == '.'), 0
    for op in operations:
        dir = (dir + int(op == 'R') - int(op == 'L')) % 4
        if isinstance(op, int):
            for _ in range(op):
                row, col, dir = move_func(row, col, dir)
    return 1000 * (row + 1) + 4 * (col + 1) + dir


lines = get_input(year=2022, day=22)
size = max(len(lines) - 2, *(len(row) for row in lines[:-2]))
face_size = min(len(row.strip()) for row in lines[:-2])
map = [[lines[r][c] if r < len(lines) - 2 and c < len(lines[r]) else ' ' for c in range(size)] for r in range(size)]
operations = [int(m[0]) if m[0].isdigit() else m[0] for m in re.finditer(r"\d+|[LR]", lines[-1])]
cube_mapping = cube_mapping_example if face_size == 4 else cube_mapping_input

print(get_password(move_2d))
print(get_password(move_on_cube))
