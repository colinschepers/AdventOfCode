from operator import add, sub, mul, truediv

from utils import get_input

operators = {'+': add, '-': sub, '*': mul, '/': truediv}


def resolve(monkey: str = 'root') -> float:
    if isinstance(monkeys[monkey], int):
        return monkeys[monkey]
    left, operator, right = monkeys[monkey]
    return operator(resolve(left), resolve(right))


def binary_search() -> int:
    range = (0, 100000000000000)
    monkeys['root'] = (monkeys['root'][0], sub, monkeys['root'][2])
    monkeys['humn'] = 0
    zero_val = resolve()
    while val := resolve():
        range = (monkeys['humn'] + 1, range[1]) if (val < 0) == (zero_val < 0) else (range[0], monkeys['humn'])
        monkeys['humn'] = (range[0] + range[1]) // 2
    return monkeys['humn']


monkeys = {s[0].rstrip(':'): int(s[1]) if len(s) == 2 else (s[1], operators[s[2]], s[3])
           for s in map(lambda line: line.split(' '), get_input(year=2022, day=21))}
print(int(resolve()))
print(binary_search())
