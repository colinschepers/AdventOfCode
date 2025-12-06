import re
from itertools import zip_longest
from math import prod

from utils import get_input, split_lines


*nr_lines, operator_line = get_input(2025, 6)
operators = [{"+": sum, "*": prod}[char] for char in operator_line if char in "+*"]

horizontal_nrs = [list(map(int, re.findall(r"\d+", line))) for line in nr_lines]
horizontal_problems_nrs = list(zip(*horizontal_nrs))
print(sum(operator(problem_nrs) for problem_nrs, operator in zip(horizontal_problems_nrs, operators)))

vertical_nrs = ["".join(char for char in column if char and char.isdigit()) for column in zip_longest(*nr_lines)]
vertical_problem_nrs = [[int(nr) for nr in problem] for problem in split_lines(vertical_nrs)]
print(sum(operator(problem_nrs) for problem_nrs, operator in zip(vertical_problem_nrs, operators)))
