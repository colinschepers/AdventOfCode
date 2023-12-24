import re
from typing import Sequence, Tuple, Iterable

from utils import get_input

Coordinate = Tuple[int, int, int]
Brick = Tuple[Coordinate]


def _parse(lines: Sequence[str]) -> Iterable[Brick]:
    for line in lines:
        x1, y1, z1, x2, y2, z2 = map(int, re.findall(r"\d+", line))
        yield tuple((x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1))


def _fall(bricks: Sequence[Brick]) -> Tuple[list[Brick], int]:
    new_bricks, occupied, fell = [], set(), set()
    for idx, brick in enumerate(bricks):
        while all(z > 1 and (x, y, z - 1) not in occupied for x, y, z in brick):
            fell.add(idx)
            brick = tuple((x, y, z - 1) for x, y, z in brick)
        new_bricks.append(brick)
        occupied.update(brick)
    return new_bricks, len(fell)


bricks, _ = _fall(sorted(_parse(get_input(year=2023, day=22)), key=lambda b: min(z for _, _, z in b)))
fall_numbers = [_fall(bricks[:i] + bricks[i + 1:])[1] for i in range(len(bricks))]

print(sum(x == 0 for x in fall_numbers))
print(sum(fall_numbers))
