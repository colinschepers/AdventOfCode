import re
from functools import lru_cache

from utils import get_input


@lru_cache(maxsize=None)
def can_contain(bag: str, target: str) -> bool:
    if bag == target:
        return True
    return any(can_contain(bag, target) for _, bag in bags[bag])


@lru_cache(maxsize=None)
def count(bag: str) -> int:
    return 1 + sum(cnt * count(b) for cnt, b in bags[bag])


bags = {}
for line in get_input(year=2020, day=7):
    match = re.match(r"^(\w+ \w+) bags contain .*$", line)
    matches = re.findall(r"(\d+) (\w+ \w+) bags?", line)
    bags[match[1]] = [(int(bag[0]), bag[1]) for bag in matches]

print(sum([can_contain(b, 'shiny gold') for b in bags]) - 1)
print(count('shiny gold') - 1)
