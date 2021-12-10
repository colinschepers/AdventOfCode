from collections import deque
from functools import reduce
from typing import Tuple

from utils import get_input


CHUNKS = {"(": ")", "[": "]", "{": "}", "<": ">"}
ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def get_score(line: str) -> Tuple[int, bool]:
    expected = deque()
    for char in line:
        if char in CHUNKS:
            expected.append(CHUNKS[char])
        elif char != expected.pop():
            return ERROR_SCORES[char], True
    return reduce(lambda score, _: score * 5 + COMPLETION_SCORES[expected.pop()],
                  range(len(expected)), 0), False


data = get_input(day=10)

scores = list(get_score(line) for line in data)
print(sum(score for score, is_error in scores if is_error))

completion_scores = list(sorted(score for score, is_error in scores if score and not is_error))
print(completion_scores[len(completion_scores) // 2])
