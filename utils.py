import contextlib
import os
from functools import lru_cache
from io import StringIO
from itertools import groupby
from typing import Iterable, Tuple, Any, Callable, Sequence, TypeVar

import requests_cache

T = TypeVar('T')

SESSION_COOKIE = os.environ["SESSION_COOKIE"]
session = requests_cache.CachedSession('cache')


def get_input(day: int) -> Sequence[str]:
    response = session.get(
        url=f"https://adventofcode.com/2021/day/{day}/input",
        cookies={"session": SESSION_COOKIE}
    ).text.strip()
    return [line for line in response.split('\n')]


def get_input_from_file(file_name: str) -> Sequence[str]:
    with open(file_name) as reader:
        return [line for line in reader.read().split('\n')]


def submit_answer(day: int, level: int, answer: int) -> str:
    return session.post(
        url=f"https://adventofcode.com/2021/day/{day}/answer",
        cookies={"session": SESSION_COOKIE},
        data={"level": level, "answer": answer}
    ).text


def get_solution(day: int) -> Sequence[str]:
    f = StringIO()
    with contextlib.redirect_stdout(f):
        __import__(f"challenges.day{day:02d}")
    return list(line for line in f.getvalue().split('\n') if line)


def split_lines(sequence: Sequence[str]) -> Sequence[Sequence[str]]:
    return [list(group) for key, group in groupby(sequence, key=bool) if key]


def get_neighbors(array: Sequence[Sequence[Any]], row: int, col: int, allow_diagonal: bool = False) \
        -> Iterable[Tuple[int, int]]:
    candidates = (
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1), (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ) if allow_diagonal else (
        (row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)
    )
    for r, c in candidates:
        if 0 <= r < len(array) and 0 <= c < len(array[r]):
            yield r, c


def iter_2d_array(array: Sequence[Sequence[T]], condition: Callable[[T], bool] = None) \
        -> Iterable[Tuple[int, int]]:
    return ((row, col) for row in range(len(array)) for col in range(len(array[row]))
            if condition is None or condition(array[row][col]))
