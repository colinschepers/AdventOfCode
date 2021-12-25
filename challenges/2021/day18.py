import functools
import re
from itertools import combinations
from typing import Optional

from utils import get_input

re_digit = re.compile(r'\d+')
re_double_digit = re.compile(r'\d{2,}')
re_pair = re.compile(r'\[(\d+),(\d+)\]')


def add(snail: str, other: str) -> str:
    return reduce(f"[{snail},{other}]")


def reduce(snail: str) -> str:
    if idx := find_explode_idx(snail):
        return reduce(explode(snail, idx))
    if idx := find_split_idx(snail):
        return reduce(split(snail, idx))
    return snail


def find_explode_idx(snail: str) -> Optional[int]:
    depth = 0
    for idx, char in enumerate(snail):
        if char == '[':
            depth += 1
            if depth == 5:
                return idx
        elif char == ']':
            depth -= 1


def find_split_idx(snail: str) -> Optional[int]:
    if match := re_double_digit.search(snail):
        return match.span()[0]


def explode(snail: str, idx: int) -> str:
    match = re_pair.search(snail, pos=idx)
    left_val, right_val = map(int, match.groups())
    if right_match := re_digit.search(snail, pos=match.span()[1] + 1):
        l, r = right_match.span()
        snail = snail[:l] + str(int(right_match.group()) + right_val) + snail[r:]
    snail = snail[:match.span()[0]] + str(0) + snail[match.span()[1]:]
    left_matches = list(re_digit.finditer(snail, endpos=match.span()[0]))
    if left_matches:
        l, r = left_matches[-1].span()
        snail = snail[:l] + str(int(left_matches[-1].group()) + left_val) + snail[r:]
    return snail


def split(snail: str, idx: int) -> str:
    value = int(re_double_digit.search(snail, pos=idx).group(0))
    return snail[:idx] + f"[{value // 2},{(value + 1) // 2}]" + snail[idx + 2:]


def get_magnitude(snail: str) -> int:
    while '[' in snail:
        snail, _ = re_pair.subn(lambda m: str(int(m.group(1)) * 3 + int(m.group(2)) * 2), snail)
    return int(snail)


snails = [line for line in get_input(year=2021, day=18)]
print(get_magnitude(functools.reduce(lambda a, b: add(a, b), snails)))
print(max(max(get_magnitude(add(a, b)), get_magnitude(add(b, a))) for a, b in combinations(snails, 2)))
