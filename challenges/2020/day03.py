from functools import reduce

from utils import get_input

data = get_input(year=2020, day=3)

print(sum(line[(i * 3) % len(line)] == '#' for i, line in enumerate(data)))

solution2 = [0] * 5
for i, line in enumerate(data):
    if line[i % len(line)] == '#':
        solution2[0] += 1
    if line[(i * 3) % len(line)] == '#':
        solution2[1] += 1
    if line[(i * 5) % len(line)] == '#':
        solution2[2] += 1
    if line[(i * 7) % len(line)] == '#':
        solution2[3] += 1
    if i % 2 == 0:
        if line[i // 2 % len(line)] == '#':
            solution2[4] += 1

print(reduce((lambda x, y: x * y), solution2))
