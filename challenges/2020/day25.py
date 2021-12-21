from utils import get_input


def transform(subject_nr: int, loop_size: int) -> int:
    val = 1
    for _ in range(loop_size):
        val *= subject_nr
        val %= 20201227
    return val


def get_loop_size(subject_nr: int, pk: int) -> int:
    val, loop_size = 1, 1
    while True:
        val *= subject_nr
        val %= 20201227
        if val == pk:
            return loop_size
        loop_size += 1


pk_card, pk_door = tuple(map(int, get_input(year=2020, day=25)))
ls_card = get_loop_size(7, pk_card)
ls_door = get_loop_size(7, pk_door)
encryption_key = transform(pk_door, ls_card)
assert encryption_key == transform(pk_card, ls_door)
print(encryption_key)
