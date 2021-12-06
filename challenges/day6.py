from functools import lru_cache
from typing import Sequence

from utils import get_input

data = get_input(6)
fishes = list(map(int, data[0].split(',')))


def get_next_fishes(fishes: Sequence[int]):
    fishes += [9] * fishes.count(0)
    return [fish - 1 if fish > 0 else 6 for fish in fishes]


def get_fishes(fishes: Sequence[int], days_left: int):
    return fishes if days_left == 0 else \
        get_fishes(get_next_fishes(fishes), days_left - 1)


@lru_cache()
def get_offspring_count(day: int, max_day: int):
    count = 0
    for d in range(day, max_day, 7):
        count += 1 + get_offspring_count(d + 9, max_day)
    return count


print(len(get_fishes(fishes, 80)))
print(sum(1 + get_offspring_count(fish, 256) for fish in fishes))
