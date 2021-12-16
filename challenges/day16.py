from enum import Enum
from itertools import islice
from math import prod
from typing import Iterable, Tuple, Iterator

from utils import get_input


class PacketTypes(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER = 5
    SMALLER = 6
    EQUAL = 7


def evaluate(packet_type: PacketTypes, values: Iterable[int]) -> int:
    if packet_type == PacketTypes.SUM:
        return sum(values)
    elif packet_type == PacketTypes.PRODUCT:
        return prod(values)
    elif packet_type == PacketTypes.MINIMUM:
        return min(values)
    elif packet_type == PacketTypes.MAXIMUM:
        return max(values)
    elif packet_type == PacketTypes.GREATER:
        return int(next(values) > next(values))
    elif packet_type == PacketTypes.SMALLER:
        return int(next(values) < next(values))
    elif packet_type == PacketTypes.EQUAL:
        return int(next(values) == next(values))
    raise ValueError(f"Invalid packet type: {packet_type}")


def split(msg: str, idx: int) -> Tuple[int, str]:
    return int(msg[:idx], 2), msg[idx:]


def parse(msg: str) -> Iterator[Tuple[int, int, str]]:
    if not msg or int(msg, 2) == 0:
        return

    version, msg = split(msg, 3)
    type_id, msg = split(msg, 3)
    packet_type = PacketTypes(type_id)
    if packet_type == PacketTypes.LITERAL:
        bit, literal, msg = int(msg[0], 2), msg[1:5], msg[5:]
        while bit == 1:
            bit, literal_part, msg = int(msg[0], 2), msg[1:5], msg[5:]
            literal += literal_part
        yield int(literal, 2), version, msg
    else:
        length_type, msg = split(msg, 1)
        if length_type == 0:
            total_length, msg = split(msg, 15)
            results = list(parse(msg[:total_length]))
            values = (val for val, _, _ in results)
            versions = (ver for _, ver, _ in results)
            msg = msg[total_length:]
            yield evaluate(packet_type, values), version + sum(versions), msg
        elif length_type == 1:
            sub_packet_count, msg = split(msg, 11)
            results = list(islice(parse(msg), sub_packet_count))
            values = (val for val, _, _ in results)
            versions = (ver for _, ver, _ in results)
            msg = results[-1][-1]
            yield evaluate(packet_type, values), version + sum(versions), msg

    yield from parse(msg)


data = get_input(day=16)
binary = ''.join(f"{int(x):04b}" if x.isdigit() else f"{ord(x) - 55:b}" for x in data[0])

result, version_sum, remainder = next(parse(binary))
print(version_sum)
print(result)
