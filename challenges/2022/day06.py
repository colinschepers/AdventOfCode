from collections import defaultdict

from utils import get_input


def get_marker_idx(signal: str, length: int) -> int:
    buff = defaultdict(int)
    for i, c in enumerate(signal):
        buff[c] += 1
        if i >= length:
            buff[signal[i - length]] -= 1
            if buff[signal[i - length]] == 0:
                del buff[signal[i - length]]
        if len(buff) == length:
            return i


signal = get_input(year=2022, day=6)[0]
print(get_marker_idx(signal, 4) + 1)
print(get_marker_idx(signal, 14) + 1)
