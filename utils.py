import contextlib
import os
from importlib import import_module, reload
from io import StringIO
from itertools import groupby
from typing import Iterable, Tuple, Callable, Sequence, TypeVar

import requests_cache

T = TypeVar('T')
Coordinate = Tuple[int, int]
Line = Tuple[Coordinate, Coordinate]
Grid = Sequence[Sequence[T]]

SESSION_COOKIE = os.environ["SESSION_COOKIE"]
session = requests_cache.CachedSession('cache')


def get_input(year: int, day: int) -> Sequence[str]:
    response = session.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": SESSION_COOKIE}
    ).text.strip()
    return [line for line in response.split('\n')]


def read_file(file_name: str) -> Sequence[str]:
    with open(file_name) as reader:
        return [line for line in reader.read().split('\n')]


def submit_answer(day: int, level: int, answer: int) -> str:
    return session.post(
        url=f"https://adventofcode.com/2021/day/{day}/answer",
        cookies={"session": SESSION_COOKIE},
        data={"level": level, "answer": answer}
    ).text


def get_solution(year: int, day: int) -> Sequence[str]:
    f = StringIO()
    with contextlib.redirect_stdout(f):
        module = import_module(f"challenges.{year}")
        file_name = f"day{day:02d}"
        if file_name not in module.__dict__:
            import_module(f"challenges.{year}.{file_name}")
        else:
            reload(module.__dict__[file_name])
    return list(line for line in f.getvalue().split('\n') if line)


def split_lines(sequence: Sequence[str]) -> Sequence[Sequence[str]]:
    return [list(group) for key, group in groupby(sequence, key=bool) if key]


def get_neighbors(grid: Grid, row: int, col: int, allow_diagonal: bool = False) \
        -> Iterable[Coordinate]:
    candidates = (
        (row + 1, col + 1), (row + 1, col), (row, col + 1), (row + 1, col - 1), (row - 1, col + 1),
        (row, col - 1), (row - 1, col), (row - 1, col - 1)
    ) if allow_diagonal else (
        (row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)
    )
    for r, c in candidates:
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            yield r, c


def iter_grid(grid: Grid, condition: Callable[[T], bool] = None) \
        -> Iterable[Coordinate]:
    return ((row, col) for row in range(len(grid)) for col in range(len(grid[row]))
            if condition is None or condition(grid[row][col]))


def manhattan(a: Coordinate, b: Coordinate):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
