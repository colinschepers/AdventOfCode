from itertools import accumulate, islice

from more_itertools import chunked

from utils import get_input

lines = get_input(year=2022, day=10)
adds = [value for line in lines for value in ([0, int(line.split(" ")[1])] if line.startswith("addx") else [0])]
print(sum(c * x for c, x in enumerate(accumulate(adds, initial=1), start=1) if c in {20, 60, 100, 140, 180, 220}))

pixels = ("#" if abs(i % 40 - x) <= 1 else "." for i, x in enumerate(accumulate(adds, initial=1)))
print("\n".join("".join(row) for row in chunked(islice(pixels, 240), 40)))
