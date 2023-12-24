from typing import Sequence

from utils import get_input


def _extrapolate(sequence: Sequence[int], backwards: bool = False) -> int:
    if all(x == 0 for x in sequence):
        return 0
    diffs = [y - x for x, y in zip(sequence, sequence[1:])]
    if backwards:
        return sequence[0] - _extrapolate(diffs, backwards)
    return sequence[-1] + _extrapolate(diffs, backwards)


sequences = [list(map(int, line.split(" "))) for line in get_input(year=2023, day=9)]

print(sum(_extrapolate(sequence) for sequence in sequences))
print(sum(_extrapolate(sequence, backwards=True) for sequence in sequences))
