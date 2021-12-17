from collections import Iterable
from typing import Sequence

from utils import get_input, split_lines


class Board:
    def __init__(self):
        self.rows = [set() for _ in range(5)]
        self.cols = [set() for _ in range(5)]
        self.index = {}

    def check(self, number: int) -> bool:
        if number in self.index:
            row, col = self.index[number]
            self.rows[row].remove(number)
            self.cols[col].remove(number)
            return not self.rows[row] or not self.cols[col]
        return False

    def is_win(self) -> bool:
        return not all(self.rows + self.cols)

    def get_score(self, last_number: int) -> int:
        return sum(nr for row in self.rows for nr in row) * last_number

    @classmethod
    def from_lines(cls, lines: Sequence[str]) -> "Board":
        board = Board()
        for row, line in enumerate(lines):
            for col, number in enumerate(line.split()):
                number = int(number)
                board.rows[row].add(number)
                board.cols[col].add(number)
                board.index[number] = (row, col)
        return board


def load_boards(lines: Sequence[str]) -> Iterable[Board]:
    for group in split_lines(lines):
        yield Board.from_lines(group)


def solve_part_1(data: Sequence[str]):
    numbers = list(map(int, data[0].split(',')))
    boards = list(load_boards(data[1:]))
    for number in numbers:
        for board in boards:
            if board.check(number):
                return board.get_score(number)
    raise ValueError()


def solve_part_2(data: Sequence[str]):
    numbers = list(map(int, data[0].split(',')))
    boards = list(load_boards(data[1:]))
    for number in numbers:
        if len(boards) > 1:
            boards = [board for board in boards if not board.check(number)]
        elif boards[0].check(number):
            return boards[0].get_score(number)
    raise ValueError()


print(solve_part_1(get_input(year=2021, day=4)))
print(solve_part_2(get_input(year=2021, day=4)))
