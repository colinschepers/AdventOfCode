import os
from collections import Sequence

import requests_cache

SESSION_COOKIE = os.environ["SESSION_COOKIE"]

session = requests_cache.CachedSession('cache')


def get_input(day) -> Sequence[str]:
    response = session.get(
        url=f"https://adventofcode.com/2021/day/{day}/input",
        cookies={"session": SESSION_COOKIE}
    ).text
    return [line for line in response.split('\n') if line]


def submit_answer(day, level, answer) -> str:
    return session.post(
        url=f"https://adventofcode.com/2021/day/{day}/answer",
        cookies={"session": SESSION_COOKIE},
        data={"level": level, "answer": answer}
    ).text
