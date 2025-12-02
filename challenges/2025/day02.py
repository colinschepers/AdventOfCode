import re
from collections.abc import Iterable
from itertools import batched

from utils import get_input


def get_invalid_ids(start: str, stop: str, max_repetitions: int) -> Iterable[int]:
    for significance in range(len(start) // 2, len(stop)):
        repetition_start = int(start[:-significance] or 0)
        repetition_stop = int(stop[:-significance] or 0)
        for repetition in range(repetition_start, repetition_stop + 1):
            for repetition_count in range(2, max_repetitions + 1):
                number = int(str(repetition) * repetition_count)
                if number > int(stop):
                    break
                if number >= int(start):
                    yield number


ranges = list(batched(re.findall(r"\d+", get_input(2025, 2)[0]), 2))
print(sum(set(id for start, stop in ranges for id in get_invalid_ids(start, stop, max_repetitions=2))))
print(sum(set(id for start, stop in ranges for id in get_invalid_ids(start, stop, max_repetitions=len(stop)))))
