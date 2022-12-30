from typing import Iterable

from utils import get_input

mapping = {-2: '=', -1: '-', '=': -2, '-': -1}


def _to_snafu(remainder: int, power: int = 1) -> Iterable[str]:
    if remainder != 0:
        factor = (remainder // power + 2) % 5 - 2
        yield from _to_snafu(remainder - factor * power, power * 5)
        yield str(mapping.get(factor, factor))


def to_snafu(decimal: int) -> str:
    return ''.join(_to_snafu(decimal))


def to_decimal(snafu: str) -> int:
    return sum(int(mapping.get(char, char)) * 5 ** i for i, char in enumerate(reversed(snafu)))


print(to_snafu(sum(map(to_decimal, get_input(year=2022, day=25)))))
