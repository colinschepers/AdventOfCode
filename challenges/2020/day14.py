import re
from typing import Callable, Set, Dict

from utils import get_input

 
def apply_mask(value: int, mask: str) -> int:
    result = value
    for i, bitValue in enumerate(mask):
        idx = len(mask)-1-i
        if bitValue == '0':
            result &= ~(1 << idx)
        elif bitValue == '1':
            result |= 1 << idx
    return result


def get_addresses(address: int, mask: str) -> Set[int]:
    for i in range(len(mask)):
        if mask[len(mask)-1-i] == '1':
            address |= 1 << i
    addresses = {address}
    for i in [i for i in range(len(mask)) if mask[len(mask)-1-i] == 'X']:
        addresses.update([a & ~(1 << i) for a in addresses])
        addresses.update([a | 1 << i for a in addresses])
    return addresses


def solve(write_func: Callable[[Dict[int, int], int, int, str], None]) -> int:
    mask, mem = '', {}
    for line in data:
        match = re.match('^mask = ([X01]+)$', line)
        if match:
            mask = match.group(1)
            continue
        match = re.match('^mem\[(\d+)\] = (\d+)$', line)
        if match:
            address = int(match.group(1))
            value = int(match.group(2))
            write_func(mem, address, value, mask)
            continue
        raise ValueError()
    return sum([v for v in mem.values()])


def write1(mem: Dict[int, int], address: int, value: int, mask: str):
    mem[address] = apply_mask(value, mask)


def write2(mem: Dict[int, int], address: int, value: int, mask: str):
    for a in get_addresses(address, mask):
        mem[a] = value


data = get_input(year=2020, day=14)
print(solve(write1))
print(solve(write2))
