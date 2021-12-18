from typing import Sequence, Tuple

from utils import get_input


def solve_part_1(data: Sequence[Tuple[str, int]]) -> int:
    x, y, dir = 0, 0, 90
    for action, value in data:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            dir -= value
        elif action == 'R':
            dir += value
        elif action == 'F':
            if dir == 0:
                y += value
            elif dir == 180:
                y -= value
            elif dir == 90:
                x += value
            elif dir == 270:
                x -= value
        dir %= 360

    return abs(x) + abs(y)


def solve_part_2(data: Sequence[Tuple[str, int]]) -> int:
    def rotate(wx: int, wy: int, deg: int):
        for x in range(deg % 360 // 90):
            wx, wy = wy, -wx
        return wx, wy

    x, y, wx, wy = 0, 0, 10, 1
    for action, value in data:
        if action == 'N':
            wy += value
        elif action == 'S':
            wy -= value
        elif action == 'E':
            wx += value
        elif action == 'W':
            wx -= value
        elif action == 'L':
            wx, wy = rotate(wx, wy, -value)
        elif action == 'R':
            wx, wy = rotate(wx, wy, value)
        elif action == 'F':
            x += wx * value
            y += wy * value

    return abs(x) + abs(y)


data = [(line[0], int(line[1:])) for line in get_input(year=2020, day=12)]
print(solve_part_1(data))
print(solve_part_2(data))
