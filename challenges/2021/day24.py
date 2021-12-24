from itertools import groupby
from typing import Iterator

from utils import get_input


def get_z(w: int, z: int, a: int, b: int, c: int) -> int:
    x = int((z % 26) + b != w)
    z //= a
    z *= 25 * x + 1
    return z + (w + c) * x


def solve(set_idx: int = 0, z: int = 0, descending: bool = False) -> Iterator[int]:
    if set_idx == len(instruction_sets):
        if z == 0:
            yield 0
        return

    a, b, c = instruction_sets[set_idx]

    possible_w_s = []
    if a == 1:
        possible_w_s = range(9, 0, -1) if descending else range(1, 10)
    elif a == 26 and 1 <= (z % 26) + b <= 9:
        possible_w_s = [(z % 26) + b]

    for w in possible_w_s:
        solutions = solve(set_idx + 1, get_z(w, z, a, b, c), descending)
        yield from (solution + w * 10 ** (len(instruction_sets) - 1 - set_idx) for solution in solutions)


data = get_input(year=2021, day=24)
instruction_sets = [list(instruction.split() for instruction in list(group))
                    for key, group in groupby(data, key=lambda x: x != "inp w") if key]
instruction_sets = [[int(instruction[i][-1]) for i in (3, 4, 14)] for instruction in instruction_sets]

print(next(solve(descending=True), None))
print(next(solve(), None))
