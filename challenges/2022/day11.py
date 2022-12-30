import heapq
import re
from collections import namedtuple, deque
from math import prod
from typing import List

from more_itertools import chunked

from utils import get_input

Monkey = namedtuple("Monkey", "id items operation divisible_by true_monkey false_monkey")


def get_monkeys() -> List[Monkey]:
    return [Monkey(
        int(re.search(r"\d+", chunk[0])[0]),
        deque(map(int, re.findall(r"\d+", chunk[1]))),
        eval("lambda old: " + re.search(r'new = (.*)', chunk[2])[1]),
        int(re.search(r'\d+', chunk[3])[0]), int(re.search(r'\d+', chunk[4])[0]), int(re.search(r'\d+', chunk[5])[0])
    ) for chunk in chunked(get_input(year=2022, day=11), 7)]


def get_inspection_sums(monkeys: List[Monkey], num_rounds: int, relief_factor: int) -> List[int]:
    sums = [0 for _ in monkeys]
    worry_cap = prod(m.divisible_by for m in monkeys)
    for _ in range(num_rounds):
        for monkey in monkeys:
            sums[monkey.id] += len(monkey.items)
            while monkey.items:
                worry_level = monkey.operation(monkey.items.popleft()) // relief_factor % worry_cap
                throw_monkey = monkey.true_monkey if worry_level % monkey.divisible_by == 0 else monkey.false_monkey
                monkeys[throw_monkey].items.append(worry_level)
    return sums


print(prod(heapq.nlargest(2, get_inspection_sums(get_monkeys(), 20, 3))))
print(prod(heapq.nlargest(2, get_inspection_sums(get_monkeys(), 10000, 1))))
