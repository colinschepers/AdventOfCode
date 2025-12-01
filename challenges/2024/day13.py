import re
from typing import Tuple

from sympy import symbols, Eq, solve

from utils import get_input, split_lines

Machine = Tuple[int, ...]


def solution(machine: Machine, correction: int = 0) -> int:
    ax, ay, bx, by, px, py = machine
    n, m = symbols('n m', integer=True)
    eq1 = Eq(ax * n + bx * m, px + correction)
    eq2 = Eq(ay * n + by * m, py + correction)
    solution = solve((eq1, eq2), (n, m))
    return solution[n] * 3 + solution[m] if solution else 0


machines = [
    tuple(map(int, re.findall(r"\d+", " ".join(triplet))))
    for triplet in split_lines(get_input(2024, 13))
]

print(sum(solution(machine) for machine in machines))
print(sum(solution(machine, correction=10000000000000) for machine in machines))
