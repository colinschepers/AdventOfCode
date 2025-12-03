import contextlib
import os
import re
from importlib import import_module, reload
from io import StringIO
from itertools import groupby, tee
from pathlib import Path
from typing import Any, Callable, Iterable, List, Sequence, Tuple, TypeVar

import requests_cache

T = TypeVar('T')
Coordinate = Tuple[int, int]
Line = Tuple[Coordinate, Coordinate]
Grid = List[List[T]]

ROOT = Path(__file__).parent
SESSION_COOKIE = os.environ["SESSION_COOKIE"]
session = requests_cache.CachedSession('cache')


def _get_input_from_url(year: int, day: int) -> Sequence[str]:
    response = session.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": SESSION_COOKIE}
    )
    if response.status_code != 200:
        raise Exception(response.text)
    return [line for line in response.text.rstrip().split('\n')]


def _get_input_from_file(year: int, day: int) -> Sequence[str]:
    path = ROOT / "tests" / "examples" / str(year) / "inputs" / f"{day:02}.txt"
    return read_file(str(path))


def get_input(year: int, day: int, from_file: bool = False) -> Sequence[str]:
    return _get_input_from_file(year, day) if from_file else _get_input_from_url(year, day)


def read_file(file_name: str) -> Sequence[str]:
    with open(file_name) as reader:
        return [line for line in reader.read().split('\n')]


def submit_answer(year: int, day: int, level: int, answer: int) -> str:
    return session.post(
        url=f"https://adventofcode.com/{year}/day/{day}/answer",
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


def get_years() -> Sequence[int]:
    return [int(p.name) for p in Path("challenges").iterdir() if re.match(r"\d{4}", p.name)]


def get_days(year: int):
    path = ROOT / "challenges" / str(year)
    return [int(re.search(r'\d+', p.stem).group()) for p in path.glob("day*.py")]


def split_lines(sequence: Sequence[str]) -> Sequence[Sequence[str]]:
    return [list(group) for key, group in groupby(sequence, key=bool) if key]


def get_neighbors(row: int, col: int, width: int, height: int, allow_diagonal: bool = False) \
        -> Iterable[Coordinate]:
    candidates = (
        (row + 1, col + 1), (row + 1, col), (row, col + 1), (row + 1, col - 1), (row - 1, col + 1),
        (row, col - 1), (row - 1, col), (row - 1, col - 1)
    ) if allow_diagonal else (
        (row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)
    )
    for r, c in candidates:
        if 0 <= r < height and 0 <= c < width:
            yield r, c


def iter_grid(grid: Grid, condition: Callable[[T], bool] = None) \
        -> Iterable[Coordinate]:
    return ((row, col) for row in range(len(grid)) for col in range(len(grid[row]))
            if condition is None or condition(grid[row][col]))


def manhattan(a: Tuple, b: Tuple):
    return sum(abs(x - y) for x, y in zip(a, b))


def argmax(data: Sequence[Any]) -> int:
    return max(range(len(data)), key=lambda x: data[x])


def split_on_condition(
    iterable: Iterable[T], condition: Callable[[T], bool]
) -> Tuple[Iterable[T], Iterable[T]]:
    left, right = tee((x, condition(x)) for x in iterable)
    return (x for x, result in left if result), (x for x, result in right if not result)
