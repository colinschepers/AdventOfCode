import re

from utils import get_input

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
regex = f"(?=({'|'.join(digits.keys())}|{'|'.join(digits.values())}))"


def _get_number(line: str) -> int:
    result = [digits.get(m.group(1), m.group(1)) for m in re.finditer(regex, line)]
    return int(result[0] + result[-1])


print(sum(map(_get_number, get_input(year=2023, day=1))))
