from typing import Sequence

from numba import jit

from utils import get_input


def iterate(next_cup: Sequence[int], current: int = 1):
    for i in range(len(next_cup) - 1):
        yield current
        current = next_cup[current]


@jit
def simulate(cups: Sequence[int], turns: int):
    cup_count = len(cups)
    next_cup = [0] * (cup_count + 1)
    current = cups[0]
    for i in range(1, len(cups)):
        next_cup[current] = cups[i]
        current = next_cup[current]
    next_cup[current] = cups[0]

    current = cups[0]
    for _ in range(turns):
        first = next_cup[current]
        second = next_cup[first]
        third = next_cup[second]

        target = current - 1 if current > 1 else cup_count
        while target in (first, second, third):
            target = target - 1 if target > 1 else cup_count

        next_cup[current] = next_cup[third]
        next_cup[third] = next_cup[target]
        next_cup[target] = first

        current = next_cup[current]

    return next_cup


cups = [int(char) for char in get_input(year=2020, day=23)[0]]
next_cup = simulate(cups, 100)
print(''.join(map(str, iterate(next_cup)))[1:])

cups += [x for x in range(len(cups) + 1, 1000001)]
next_cup = simulate(cups, 10000000)
print(next_cup[1] * next_cup[next_cup[1]])
