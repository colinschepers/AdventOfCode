from collections.abc import Iterable
from functools import cache

from utils import get_input


def blink(stone: int) -> Iterable[int]:
    if stone == 0:
        yield 1
    elif len(stone_str := str(stone)) % 2 == 0:
        mid = len(stone_str) // 2
        yield int(stone_str[mid:])
        yield int(stone_str[:mid])
    else:
        yield stone * 2024


@cache
def stone_count(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    return sum(stone_count(new_stone, blinks - 1) for new_stone in blink(stone))


stones = [int(stone) for line in get_input(2024, 11) for stone in line.split(" ")]
print(sum(stone_count(stone, blinks=25) for stone in stones))
print(sum(stone_count(stone, blinks=75) for stone in stones))
