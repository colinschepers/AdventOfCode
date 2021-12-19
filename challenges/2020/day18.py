import re

from utils import get_input


def evaluate_1(input: str) -> int:
    while '(' in input:
        input = re.sub(r'\(([^\(\)]+)\)', lambda m: str(evaluate_1(m.group(1))), input)
    while m := re.match(r'(\d+)([\+\*])(\d+)', input):
        a, b, op = evaluate_1(m.group(1)), evaluate_1(m.group(3)), m.group(2)
        val = a + b if op == '+' else a * b
        input = str(val) + input[len(m.group(0)):]
    return int(input)


def evaluate_2(input: str) -> int:
    while '(' in input:
        input = re.sub(r'\(([^\(\)]+)\)', lambda m: str(evaluate_2(m.group(1))), input)
    while '+' in input:
        input = re.sub(r'(\d+)\+(\d+)', lambda m: str(evaluate_2(m.group(1)) + evaluate_2(m.group(2))), input)
    while '*' in input:
        input = re.sub(r'(\d+)\*(\d+)', lambda m: str(evaluate_2(m.group(1)) * evaluate_2(m.group(2))), input)
    return int(input)


data = get_input(year=2020, day=18)
print(sum(evaluate_1(line.replace(' ', '')) for line in data))
print(sum(evaluate_2(line.replace(' ', '')) for line in data))
