
path = './data/day17.txt'
with open(path, encoding = 'utf-8') as f:
    lines = [l.strip() for l in f.readlines()]


def init():
    active = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0))
    return active

def get_neighbors(x, y, z):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not(i == 0 and j == 0 and k == 0):
                    yield [x+i, y+j, z+k]

def get_bounds(active):
    return [
        (min(x for x, _, _ in iter(active)), 
         max(x for x, _, _ in iter(active))),
        (min(y for _, y, _ in iter(active)), 
         max(y for _, y, _ in iter(active))),
        (min(z for _, _, z in iter(active)), 
         max(z for _, _, z in iter(active)))
    ]

def run_cycle(active):
    old_active = set(active)
    bounds = get_bounds(old_active)
    for z in range(bounds[2][0] - 1, bounds[2][1] + 2):
        for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
            for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
                coord = (x, y, z)
                is_active = coord in old_active
                cnt = sum((nx, ny, nz) in old_active for nx, ny, nz in get_neighbors(x, y, z))
                if is_active and not(2 <= cnt <= 3):
                    active.remove(coord)
                elif not is_active and cnt == 3:
                    active.add(coord)

def run_cycles(active, n):
    for _ in range(n):
        run_cycle(active)

def print_space():
    bounds = get_bounds(active)
    for z in range(bounds[2][0], bounds[2][1] + 1):
        print(f'z={z}')
        for y in range(bounds[1][0], bounds[1][1] + 1):
            print(''.join('#' if (x, y, z) in active else '.' for x in range(bounds[0][0], bounds[0][1] + 1)))
        print()
    print()

active = init()
run_cycles(active, 6)
# print_space()
print(len(active))




def init():
    active = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0, 0))
    return active

def get_neighbors(x, y, z, w):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not(i == 0 and j == 0 and k == 0 and l == 0):
                        yield [x+i, y+j, z+k, w+l]

def get_bounds(active):
    return [
        (min(x for x, _, _, _ in iter(active)), 
         max(x for x, _, _, _ in iter(active))),
        (min(y for _, y, _, _ in iter(active)), 
         max(y for _, y, _, _ in iter(active))),
        (min(z for _, _, z, _ in iter(active)), 
         max(z for _, _, z, _ in iter(active))),
        (min(w for _, _, _, w in iter(active)), 
         max(w for _, _, _, w in iter(active)))
    ]

def run_cycle(active):
    old_active = set(active)
    bounds = get_bounds(old_active)
    for w in range(bounds[3][0] - 1, bounds[3][1] + 2):
        for z in range(bounds[2][0] - 1, bounds[2][1] + 2):
            for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
                for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
                    coord = (x, y, z, w)
                    is_active = coord in old_active
                    cnt = sum((nx, ny, nz, nw) in old_active for nx, ny, nz, nw in get_neighbors(x, y, z, w))
                    if is_active and not(2 <= cnt <= 3):
                        active.remove(coord)
                    elif not is_active and cnt == 3:
                        active.add(coord)

def run_cycles(active, n):
    for i in range(n):
        run_cycle(active)

def print_space():
    bounds = get_bounds(active)
    for w in range(bounds[3][0], bounds[3][1] + 1):
        for z in range(bounds[2][0], bounds[2][1] + 1):
            print(f'z={z}, w={w}')
            for y in range(bounds[1][0], bounds[1][1] + 1):
                print(''.join('#' if (x, y, z, w) in active else '.' for x in range(bounds[0][0], bounds[0][1] + 1)))
            print()
        print()
    print()

active = init()
# print_space()
run_cycles(active, 6)
# print_space()
print(len(active))

