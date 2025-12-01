import re

from utils import get_input


def is_valid(
    test: int, numbers: list[int], allow_concat: bool = False, value: int = 0, idx: int = 0
) -> bool:
    if idx == len(numbers) or value > test:
        return value == test
    if idx == 0:
        return is_valid(test, numbers, allow_concat, numbers[0], idx + 1)
    return (
        is_valid(test, numbers, allow_concat, value * numbers[idx], idx + 1) or
        is_valid(test, numbers, allow_concat, value + numbers[idx], idx + 1) or (
            allow_concat and
            is_valid(test, numbers, allow_concat, int(str(value) + str(numbers[idx])), idx + 1)
        )
    )


equations = [
    (int(numbers[0]), [int(nr) for nr in numbers[1:]])
    for line in get_input(2024, 7)
    if (numbers := re.findall(r"\d+", line))
]

print(sum(test for test, numbers in equations if is_valid(test, numbers)))
print(sum(test for test, numbers in equations if is_valid(test, numbers, allow_concat=True)))
