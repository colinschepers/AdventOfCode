import os
from collections import Sequence
from itertools import groupby

import requests_cache

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


def split_lines(sequence: Sequence[str]) -> Sequence[Sequence[str]]:
    return [list(group) for key, group in groupby(sequence, key=bool) if key]
