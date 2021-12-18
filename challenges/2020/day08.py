from typing import Tuple

from utils import get_input


def run() -> Tuple[bool, int]:
    i, acc, visited = 0, 0, set()
    while True:
        if i >= len(data):
            return True, acc
        if i in visited:
            return False, acc
        visited.add(i)
        acc += data[i][1] if data[i][0] == 'acc' else 0
        i += data[i][1] if data[i][0] == 'jmp' else 1


def find_broken() -> Tuple[int, int]:
    for i in range(len(data)):
        item = data[i]
        if item[0] == 'nop':
            data[i] = ('jmp', item[1])
            res, acc = run()
            if res:
                return i, acc
        elif data[i][0] == 'jmp':
            data[i] = ('nop', item[1])
            res, acc = run()
            if res:
                return i, acc
        data[i] = item


data = [(s[0], int(s[1])) for s in [x.split(' ') for x in get_input(year=2020, day=8)]]
print(run()[1])
print(find_broken()[1])
