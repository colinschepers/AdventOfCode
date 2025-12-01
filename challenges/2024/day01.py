from collections import Counter

from utils import get_input

input = [line.split() for line in get_input(2024, 1)]

left, right = sorted(int(a) for a, _ in input), sorted(int(b) for _, b in input)
print(sum(abs(a - b) for a, b in zip(left, right)))

right_counts = Counter(right)
print(sum(a * right_counts.get(a, 0) for a in left))
