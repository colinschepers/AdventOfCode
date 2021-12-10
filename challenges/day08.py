from typing import Sequence, Set

from utils import get_input


def solve(inputs: Sequence[Set], outputs: Sequence[Set]):
    digits = dict()
    digits[1] = next(x for x in inputs if len(x) == 2)
    digits[4] = next(x for x in inputs if len(x) == 4)
    digits[7] = next(x for x in inputs if len(x) == 3)
    digits[8] = next(x for x in inputs if len(x) == 7)
    digits[2] = next(x for x in inputs if len(x) == 5 and len(x & digits[1]) == 1 and len(x & digits[4]) == 2)
    digits[3] = next(x for x in inputs if len(x) == 5 and len(x & digits[1]) == 2)
    digits[5] = next(x for x in inputs if len(x) == 5 and len(x & digits[1]) == 1 and len(x & digits[4]) == 3)
    digits[0] = next(x for x in inputs if len(x) == 6 and len(x & digits[1]) == 2 and len(x & digits[4]) == 3)
    digits[6] = next(x for x in inputs if len(x) == 6 and len(x & digits[1]) == 1)
    digits[9] = next(x for x in inputs if len(x) == 6 and len(x & digits[1]) == 2 and len(x & digits[4]) == 4)
    lookup = {''.join(sorted(chars)): str(digit) for digit, chars in digits.items()}
    return int(''.join(lookup[''.join(sorted(output))] for output in outputs))


data = get_input(day=8)
data = [(list(map(set, left.split())), list(map(set, right.split())))
        for (left, right) in (line.split(' | ') for line in data)]

print(sum(len(output) in {2, 3, 4, 7} for _, outputs in data for output in outputs))
print(sum(solve(inputs, outputs) for inputs, outputs in data))
