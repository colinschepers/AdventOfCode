from functools import lru_cache
from typing import Mapping

from utils import get_input


def get_diffs() -> Mapping[int, int]:
    diffs = {}
    prev = 0
    for d in data:
        diff = d - prev
        diffs[diff] = diffs.get(diff, 0) + 1
        prev = d
    return diffs


@lru_cache
def count(i: int) -> int:
    if i == len(data) - 1:
        return 1
    cnt = 0
    for j in range(i + 1, i + 4):
        if j < len(data) and 1 <= data[j] - data[i] <= 3:
            cnt += count(j)
    return cnt


data = sorted(map(int, get_input(year=2020, day=10)))
data += [data[-1] + 3]

diffs = get_diffs()
print(diffs[1] * diffs[3])

data = [0] + data
print(count(0))
