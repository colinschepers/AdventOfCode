from typing import Sequence

from utils import get_input


def solve_part_1(data: Sequence[int]) -> int:
    i, j = 0, len(data) - 1
    while i < j:
        sum = data[i] + data[j]
        if sum == 2020:
            return data[i] * data[j]
        elif sum < 2020:
            i += 1
        else:
            j -= 1


def solve_part_2(data: Sequence[int]) -> int:
    for i in range(len(data) - 2):
        for j in range(i + 1, len(data) - 1):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]


data = sorted(int(line) for line in get_input(year=2020, day=1))
print(solve_part_1(data))
print(solve_part_2(data))
