from typing import List

from utils import get_input


def get_grove_coordinates(numbers: List[int], num_rounds: int = 1) -> List[int]:
    indices = list(range(len(numbers)))
    for _ in range(num_rounds):
        for i, x in enumerate(numbers):
            idx = indices.index(i)
            indices.insert((idx + x) % (len(numbers) - 1), indices.pop(idx))
    result = [numbers[idx] for idx in indices]
    return sum(result[(result.index(0) + i) % len(result)] for i in (1000, 2000, 3000))


input = list(map(int, get_input(year=2022, day=20)))
print(get_grove_coordinates(input))
print(get_grove_coordinates([x * 811589153 for x in input], 10))
