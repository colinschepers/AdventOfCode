from utils import get_input


def to_int(a: str) -> int:
    return ord(a) % ord('A') + 1


def score(a: int, b: int) -> int:
    return b + (3 if a == b else 0 if (a - b) % 3 == 1 else 6)


def determine(a: int, b: str) -> int:
    if b == 'X':
        return a - 1 if a > 1 else 3
    if b == 'Z':
        return a + 1 if a < 3 else 1
    return a


data = [line.split(" ") for line in get_input(year=2022, day=2)]

print(sum(score(to_int(a), to_int(b)) for a, b in data))
print(sum(score(to_int(a), determine(to_int(a), b)) for a, b in data))
