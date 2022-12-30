import numpy as np
from numba import njit

from utils import get_input


@njit
def get_spoken_number(numbers: np.array, turns: int) -> int:
    prev = numbers[-1]
    memory = [-1] * turns
    for i, shoutout in enumerate(numbers[:-1]):
        memory[shoutout] = i
    for i in range(len(numbers), turns):
        shoutout = 0 if memory[prev] == -1 else (i - 1 - memory[prev])
        memory[prev] = i - 1
        prev = shoutout
    return prev


data = np.array(get_input(year=2020, day=15)[0].split(','), dtype=np.int32)
print(get_spoken_number(data, 2020))
print(get_spoken_number(data, 30000000))
