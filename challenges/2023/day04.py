import re
from typing import Iterable, Sequence

from utils import get_input


def _get_match_counts(lines: Sequence[str]) -> Iterable[int]:
    for i, line in enumerate(lines):
        winning, own = [
            {int(m.group()) for m in re.finditer(r"\d+", part)}
            for part in line.split(":")[1].split("|")
        ]
        yield len(winning & own)


def _get_scores(match_counts: Sequence[int]) -> Iterable[int]:
    for match_count in match_counts:
        yield 2 ** (match_count - 1) if match_count else 0


def _get_copies(match_counts: Sequence[int]) -> Iterable[int]:
    copies = [1] * len(match_counts)
    for i, match_count in enumerate(match_counts):
        for j in range(i + 1, min(len(copies), i + 1 + match_count)):
            copies[j] += copies[i]
    return copies


match_counts = list(_get_match_counts(get_input(year=2023, day=4)))

print(sum(_get_scores(match_counts)))
print(sum(_get_copies(match_counts)))
