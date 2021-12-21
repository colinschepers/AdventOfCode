from functools import lru_cache

from utils import get_input


@lru_cache(maxsize=None)
def get_offspring_count(day: int, max_day: int):
    count = 0
    for d in range(day, max_day, 7):
        count += 1 + get_offspring_count(d + 9, max_day)
    return count


data = get_input(year=2021, day=6)
fishes = list(map(int, data[0].split(',')))

print(sum(1 + get_offspring_count(fish, 80) for fish in fishes))
print(sum(1 + get_offspring_count(fish, 256) for fish in fishes))
