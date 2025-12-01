from collections.abc import Sequence

from utils import get_input, split_lines

KEY_BITS = (1 << 5) - 1


def to_int(schematic: Sequence[str]) -> int:
    chars = (char for row in schematic for char in row)
    return sum((char == "#") << significance for significance, char in enumerate(chars))


schematics = [to_int(schematic) for schematic in split_lines(get_input(2024, 25))]
locks = [bits for bits in schematics if not (bits & KEY_BITS)]
keys = [bits for bits in schematics if (bits & KEY_BITS)]

print(sum(not (lock & key) for lock in locks for key in keys))
