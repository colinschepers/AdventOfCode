from copy import deepcopy
from typing import Tuple, List

from utils import get_input


def rearrange_9000(stacks: List[List[str]], moves: List[Tuple]) -> List[List[str]]:
    stacks = deepcopy(stacks)
    for num, src, dest in moves:
        for _ in range(num):
            stacks[dest - 1].append(stacks[src - 1].pop())
    return stacks


def rearrange_9001(stacks: List[List[str]], moves: List[Tuple]) -> List[List[str]]:
    stacks = deepcopy(stacks)
    for num, src, dest in moves:
        stacks[dest - 1] += stacks[src - 1][-num:]
        stacks[src - 1] = stacks[src - 1][:-num]
    return stacks


lines = get_input(year=2022, day=5)
height = sum('[' in line for line in lines)
num_stacks = max(int(c) for c in lines[height] if c.isdigit())
moves = [tuple(int(x) for x in line.split(' ') if x.isdigit()) for line in lines[height+2:]]
stacks = [[lines[h][s] for h in range(height - 1, -1, -1) if lines[h][s].strip()] for s in range(1, num_stacks * 4, 4)]

print("".join(stack[-1] for stack in rearrange_9000(stacks, moves)))
print("".join(stack[-1] for stack in rearrange_9001(stacks, moves)))
