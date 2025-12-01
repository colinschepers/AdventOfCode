import re
from collections import defaultdict
from math import prod
from typing import Mapping

from utils import get_input


def _get_max_dict(line: str) -> Mapping[str, int]:
    max_dict = defaultdict(int)
    for match in re.finditer(r"(\d+) (\w+)", line):
        value, color = match.groups()
        max_dict[color] = max(max_dict[color], int(value))
    return max_dict


def _is_feasible(max_dict: Mapping[str, int]) -> bool:
    return max_dict["red"] <= 12 and max_dict["green"] <= 13 and max_dict["blue"] <= 14


data = list(map(_get_max_dict, get_input(year=2023, day=2)))

print(sum(i for i, max_dict in enumerate(data, start=1) if _is_feasible(max_dict)))
print(sum(prod(max_dict.values()) for max_dict in data))
