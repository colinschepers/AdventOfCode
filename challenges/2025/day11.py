import re
from functools import cache

from utils import get_input


@cache
def count_paths(current: str, fft: bool, dac: bool) -> int:
    if current == "out":
        return int(fft and dac)
    return sum(
        count_paths(device, fft | (current == "fft"), dac | (current == "dac"))
        for device in devices[current]
    )


lines = [re.findall(r"\w+", line) for line in get_input(2025, 11)]
devices = {start: ends for start, *ends  in lines}

print(count_paths("you", fft=True, dac=True))
print(count_paths("svr", fft=False, dac=False))
