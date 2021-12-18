import re

from utils import get_input

data = [re.search(r"(\d+)-(\d+)\s+(\w):\s+(\w+)", line).groups() for line in get_input(year=2020, day=2)]
print(sum(int(low) <= password.count(char) <= int(high) for low, high, char, password in data))
print(sum((password[int(low) - 1] == char) ^ (password[int(high) - 1] == char) for low, high, char, password in data))
