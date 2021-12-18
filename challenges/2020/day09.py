from typing import Sequence

from utils import get_input


def has_sum(lst: Sequence[int], sum: int) -> bool:
    secs = set()
    for x in lst:
        if sum - x in secs:
            return True
        secs.add(x)
    return False


def find_first_wrong(preamble: int) -> int:
    lst = []
    for d in data:
        if len(lst) < preamble:
            lst.append(d)
        elif has_sum(lst, d):
            lst.append(d)
            lst.pop(0)
        else:
            return d


def find_encryption_weakness(value: int) -> int:
    total, window = 0, []
    for d in data:
        if total < value:
            total += d
            window.append(d)
        while total > value:
            total -= window.pop(0)
        if total == value:
            return min(window) + max(window)


data = list(map(int, get_input(year=2020, day=9)))
first_wrong = find_first_wrong(25)
print(first_wrong)
print(find_encryption_weakness(first_wrong))
