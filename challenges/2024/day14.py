import re
from collections import Counter
from collections.abc import Collection, Sequence
from typing import Tuple

from utils import get_input

Robot = Tuple[int, ...]

robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in get_input(2024, 14)]
is_example = len(robots) < 15
width, height = (11, 7) if is_example else (101, 103)


def to_str(robots: Collection[Robot]) -> str:
    counter = Counter((x, y) for x, y, _, _ in robots)
    rows = ("".join(str(counter.get((x, y), ".")) for x in range(width)) for y in range(height))
    return "\n".join(rows) + "\n"


def step(robots: Collection[Robot]) -> Sequence[Robot]:
    return [((x + dx) % width, (y + dy) % height, dx, dy) for x, y, dx, dy in robots]


def safety_factor(robots: Collection[Robot], seconds: int) -> int:
    for _ in range(seconds):
        robots = step(robots)

    return (
        sum(x < width // 2 and y < height // 2 for x, y, _, _ in robots) *
        sum(x < width // 2 and y > height // 2 for x, y, _, _ in robots) *
        sum(x > width // 2 and y < height // 2 for x, y, _, _ in robots) *
        sum(x > width // 2 and y > height // 2 for x, y, _, _ in robots)
    )


def no_overlap(robots: Sequence[Robot]) -> bool:
    counter = Counter((x, y) for x, y, _, _ in robots)
    return all(n == 1 for n in counter.values())


def easter_egg_number(robots: Sequence[Robot]) -> int:
    for i in range(10000):
        if no_overlap(robots):
            return i
        robots = step(robots)


print(safety_factor(robots, seconds=100))
print(easter_egg_number(robots))
