from utils import get_input


def get_spoken_number(turns: int) -> int:
    prev = data[-1]
    memory = {x: i for i, x in enumerate(data[:-1])}
    for i in range(len(data), turns):
        shoutout = 0 if prev not in memory else (i - 1 - memory[prev])
        memory[prev] = i - 1
        prev = shoutout
    return prev


data = list(map(int, get_input(year=2020, day=15)[0].split(',')))
print(get_spoken_number(2020))
print(get_spoken_number(30000000))
