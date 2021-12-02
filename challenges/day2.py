from dataclasses import dataclass

from utils import get_input


@dataclass
class Submarine:
    depth: int = 0
    position: int = 0
    aim: int = 0


data = [(command, int(value)) for command, value in map(str.split, get_input(2))]

sub_marine = Submarine()
for command, value in data:
    if command == "forward":
        sub_marine.position += value
    elif command == "down":
        sub_marine.depth += value
    elif command == "up":
        sub_marine.depth -= value
    else:
        raise ValueError(f"Invalid command: {command}")
print(sub_marine.position * sub_marine.depth)

sub_marine = Submarine()
for command, value in data:
    if command == "forward":
        sub_marine.position += value
        sub_marine.depth += sub_marine.aim * value
    elif command == "down":
        sub_marine.aim += value
    elif command == "up":
        sub_marine.aim -= value
    else:
        raise ValueError(f"Invalid command: {command}")
print(sub_marine.position * sub_marine.depth)
