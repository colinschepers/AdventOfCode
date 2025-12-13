import re

from utils import get_input, split_lines


*present_lines, region_lines = split_lines(get_input(2025, 12))
present_sizes = [sum(char == "#" for line in lines for char in line) for lines in present_lines]
regions = [list(map(int, re.findall(r"\d+", line)))  for line in region_lines]

print(sum(
    sum(count * size for count, size in zip(counts, present_sizes)) <= width * height
    for width, height, *counts in regions
))
