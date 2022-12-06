from itertools import islice

from more_itertools import first, chunked

from utils import get_input


def to_priority(c: str) -> int:
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27


data = [list(map(to_priority, line)) for line in get_input(year=2022, day=3)]
compartments = ((islice(x, 0, len(x) // 2), islice(x, len(x) // 2, len(x))) for x in data)

print(sum(first(set(l).intersection(r)) for l, r in compartments))
print(sum(first(set(a).intersection(b).intersection(c)) for a, b, c in chunked(data, 3)))
