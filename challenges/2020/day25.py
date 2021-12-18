import math
import time


input = open('./data/day25.txt').read().strip().split('\n')
pk_card, pk_door = int(input[0]), int(input[1])


def transform(subject_nr, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= subject_nr
        val %=  20201227
    return val

def get_loop_size(subject_nr, pk):
    val, loop_size = 1, 1
    while True:
        val *= subject_nr
        val %= 20201227
        if val == pk:
            return loop_size
        loop_size += 1


start_time = time.time()
ls_card = get_loop_size(7, pk_card)
print(f'ls_card={ls_card}')
ls_door = get_loop_size(7, pk_door)
print(f'ls_door={ls_door}')
encryption_key = transform(pk_card, ls_door)
print(encryption_key, f"\t{time.time() - start_time}s")
encryption_key2 = transform(pk_door, ls_card)
assert(encryption_key == encryption_key2)