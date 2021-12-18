from typing import Tuple

from utils import get_input


def to_row_column(line: str) -> Tuple[int, int]:
    row = sum(2 ** x for c, x in zip(line[6::-1], range(7)) if c == 'B')
    col = sum(2 ** x for c, x in zip(line[-1:6:-1], range(4)) if c == 'R')
    return row, col


def to_seat_id(row: int, column: int) -> int:
    return row * 8 + column


seats = list(sorted(to_seat_id(*to_row_column(line)) for line in get_input(year=2020, day=5)))
print(max(seats))
print(next(y for x, y in zip(seats, range(seats[0], seats[-1])) if x != y))
