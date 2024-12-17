import re
from collections.abc import Sequence, Iterable
from typing import Tuple

from utils import split_lines, get_input


def combo(operand: int, a: int, b: int, c: int) -> int:
    return (0, 1, 2, 3, a, b, c)[operand]


def run(program: Tuple[int], a: int, b: int, c: int) -> Iterable[int]:
    pointer = 0
    while pointer < len(program):
        opcode, operand = program[pointer], program[pointer + 1]

        if opcode == 0:
            a = int(a / 2 ** combo(operand, a, b, c))
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = combo(operand, a, b, c) % 8
        elif opcode == 3:
            if a != 0:
                pointer = operand
                continue
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            yield combo(operand, a, b, c) % 8
        elif opcode == 6:
            b = int(a / 2 ** combo(operand, a, b, c))
        elif opcode == 7:
            c = int(a / 2 ** combo(operand, a, b, c))

        pointer += 2


def solve(program: Tuple[int], _: int, b: int, c: int) -> Sequence[int]:
    matches = [0]

    for level in range(len(program)):
        matches_at_level = []
        level_start = 8 ** level
        for match in matches:
            start = level_start + (match - level_start // 8) * 8
            for a in range(start, start + 8):
                result = tuple(run(program, a, b, c))
                if result == program[-len(result):]:
                    matches_at_level.append(a)
        matches = matches_at_level

    return matches


register_lines, program_lines = split_lines(get_input(2024, 17))
registers = tuple(int(m) for m in re.findall(r"\d+", "".join(register_lines)))
program = tuple(int(m) for m in re.findall(r"\d+", program_lines[0]))

print(",".join(map(str, run(program, *registers))))
print(solve(program, *registers)[0])
