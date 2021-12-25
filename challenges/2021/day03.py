from typing import Sequence, List

from utils import get_input


def to_decimal(bit_array: Sequence[int]) -> int:
    return int("".join(map(str, bit_array)), 2)


def get_most_common_bit(report: Sequence[str], idx: int) -> int:
    return int(sum(int(entry[idx]) for entry in report) >= len(report) / 2)


def get_most_common_bits(report: Sequence[str]) -> List[int]:
    return [get_most_common_bit(report, idx) for idx in range(len(report[0]))]


def rating_filter(report: Sequence[str], idx: int, maximize: bool) -> List[str]:
    bit = get_most_common_bit(report, idx)
    bit = bit if maximize else 1 - bit
    return [line for line in report if int(line[idx]) == bit]


def get_rating(report: Sequence[str], maximize: bool = True) -> int:
    for idx in range(len(report[0])):
        report = rating_filter(report, idx, maximize)
        if len(report) == 1:
            return to_decimal(report[0])
    raise ValueError()


data = get_input(year=2021, day=3)

most_common_bits = get_most_common_bits(data)
gamma = to_decimal(most_common_bits)
epsilon = to_decimal([1 - bit for bit in most_common_bits])
print(gamma * epsilon)

oxygen = get_rating(data)
co2 = get_rating(data, maximize=False)
print(oxygen * co2)
