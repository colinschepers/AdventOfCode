from typing import Iterable, List, Sequence

from utils import get_input, Coordinate


def move(direction: str, x: int, y: int) -> Coordinate:
    return (x + 1 if direction == 'R' else x - 1 if direction == 'L' else x,
            y + 1 if direction == 'U' else y - 1 if direction == 'D' else y)


def follow(hx: int, hy: int, tx: int, ty: int) -> Coordinate:
    if abs(tx - hx) > 1 or abs(ty - hy) > 1:
        tx += 1 if hx - tx > int(ty == hy) else -1 if hx - tx < int(ty == hy) else 0
        ty += 1 if hy - ty > int(tx == hx) else -1 if hy - ty < int(tx == hx) else 0
    return tx, ty


def simulate(directions: Sequence[str], rope_length: int) -> Iterable[List[Coordinate]]:
    rope = [(0, 0) for _ in range(rope_length)]
    for direction in directions:
        rope[0] = move(direction, *rope[0])
        for i in range(1, len(rope)):
            rope[i] = follow(*rope[i - 1], *rope[i])
        yield rope


dirs = [line[0] for line in get_input(year=2022, day=9) for _ in range(int(line.split(" ")[1]))]
print(len(set(rope[-1] for rope in simulate(dirs, 2))))
print(len(set(rope[-1] for rope in simulate(dirs, 10))))
