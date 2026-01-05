from collections.abc import Collection, Iterable

from utils import get_input


def count_zeroes_in_turn(position: int, turn: int, only_zero_end: bool) -> int:
    if only_zero_end:
        return int(position == 0)
    elif turn < 0:
        return (position - 1) // 100 - (position + turn - 1) // 100
    else:
        return (position + turn) // 100 - position // 100


def count_zeroes(position: int, turns: Collection[int], only_zero_end: bool) -> Iterable[int]:
    for turn in turns:
        yield count_zeroes_in_turn(position, turn, only_zero_end)
        position = (position + turn) % 100


turns = [
    int(line[1:]) * {"R": 1, "L": -1}[line[0]]
    for line in get_input(2025, 1)
]
print(sum(count_zeroes(position=50, turns=turns, only_zero_end=True)))
print(sum(count_zeroes(position=50, turns=turns, only_zero_end=False)))
