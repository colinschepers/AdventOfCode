from collections.abc import Set
from itertools import cycle
from math import lcm
from typing import Sequence

from utils import get_input


def _get_cycle_number(node: str, ends: Set[str]) -> int:
    for i, direction in enumerate(cycle(directions)):
        if node in ends:
            return i
        node = instructions[node][direction]


def _solve(starts: Sequence[str], ends: Set[str]) -> int:
    return lcm(*(_get_cycle_number(start, ends) for start in starts))


lines = get_input(year=2023, day=8)
directions = ["LR".index(char) for char in lines[0]]
instructions = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}

print(_solve(["AAA"], {"ZZZ"}))
print(_solve([x for x in instructions if x[-1] == "A"], {x for x in instructions if x[-1] == "Z"}))
