from functools import lru_cache
from typing import Sequence, Tuple

from utils import get_input

Groups = Tuple[int, ...]


def _parse(lines: Sequence[str]) -> Sequence[Tuple[str, Groups]]:
    return [(line.split(" ")[0], tuple(map(int, line.split(" ")[1].split(",")))) for line in lines]


def _expand(line: str, groups: Groups) -> Tuple[str, Groups]:
    return ((line + "?") * 5)[:-1], groups * 5


@lru_cache(maxsize=2096)
def _get_num_arrangements(line: str, groups: Groups, in_group: bool = False) -> int:
    if not line:
        return int(not any(groups))

    num_arrangements = 0

    if line[0] == '?' or line[0] == '#':
        if groups and groups[0] > 0:
            num_arrangements += _get_num_arrangements(line[1:], (groups[0] - 1,) + groups[1:], True)

    if line[0] == '?' or line[0] == '.':
        if not in_group:
            num_arrangements += _get_num_arrangements(line[1:], groups, False)
        elif groups[0] == 0:
            num_arrangements += _get_num_arrangements(line[1:], groups[1:], False)

    return num_arrangements


data = _parse(get_input(year=2023, day=12))
print(sum(_get_num_arrangements(line, groups) for line, groups in data))
print(sum(_get_num_arrangements(*_expand(line, groups)) for line, groups in data))
