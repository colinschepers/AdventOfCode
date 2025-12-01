import re
from collections.abc import Iterable

from utils import get_input


def solve(input: str, with_disabling: bool = False) -> Iterable[int]:
    disabled = False
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))", input):
        if match[3]:
            disabled = with_disabling and match[0] == "don't()"
        elif not disabled:
            yield int(match[1]) * int(match[2])


input = "".join(get_input(2024, 3))
print(sum(solve(input)))
print(sum(solve(input, with_disabling=True)))
