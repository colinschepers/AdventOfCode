from utils import get_input, split_lines

data = split_lines(get_input(year=2020, day=6))

print(sum(len(set([c for p in group for c in p])) for group in data))
print(sum(len(list(set.intersection(*map(set, [set(c for c in p) for p in group])))) for group in data))
