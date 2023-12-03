import re
from collections import defaultdict
from math import prod
from typing import Iterable, Sequence, Tuple

from utils import get_input, Coordinate


def _get_neighbors(row: int, match: re.Match) -> Iterable[Coordinate]:
    for c in range(match.start() - 1, match.end() + 1):
        yield row - 1, c
        yield row + 1, c
    yield row, match.start() - 1
    yield row, match.end()


def _solve(lines: Sequence[str]) -> Tuple[Sequence[int], Sequence[int]]:
    symbols: dict[Coordinate, str] = defaultdict(str)
    for row, line in enumerate(lines):
        for match in re.finditer(r"[^\w.]", line):
            symbols[(row, match.start())] = match.group()

    part_numbers: list[int] = []
    gear_candidates: dict[Coordinate, list[int]] = defaultdict(list)

    for row, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            neighbor_symbols = [rc for rc in _get_neighbors(row, match) if rc in symbols]
            if any(neighbor_symbols):
                part_numbers.append(int(match.group()))
            neighbor_stars = [rc for rc in neighbor_symbols if symbols[rc] == "*"]
            for r, c in neighbor_stars:
                gear_candidates[(r, c)].append(int(match.group()))

    gear_ratios = [prod(nums) for nums in gear_candidates.values() if len(nums) == 2]

    return part_numbers, gear_ratios


data = get_input(year=2023, day=3)
part_numbers, gear_ratios = _solve(data)

print(sum(part_numbers))
print(sum(gear_ratios))
