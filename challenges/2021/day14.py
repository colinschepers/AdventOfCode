from collections import Counter, defaultdict
from math import ceil
from typing import Mapping

from utils import get_input


def solve(pairs: Mapping[str, int], pair_insertions: Mapping[str, str], step_count: int) -> int:
    for step in range(step_count):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            new_pairs[pair[0] + pair_insertions[pair]] += count
            new_pairs[pair_insertions[pair] + pair[1]] += count
        pairs = new_pairs

    counts = defaultdict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count
        counts[pair[1]] += count

    return ceil(max(counts.values()) / 2) - ceil(min(counts.values()) / 2)


lines = get_input(year=2021, day=14)
pairs = Counter(lines[0][i:i + 2] for i in range(len(lines[0]) - 1))
pair_insertions = {line[:2]: line[-1] for line in lines[2:]}

print(solve(pairs, pair_insertions, 10))
print(solve(pairs, pair_insertions, 40))
