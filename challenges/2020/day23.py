import time


cups = [int(x) for x in open('./data/day23.txt').read().strip()]


class Cup(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)


def iterate(head):
    yield head
    curr = head.next
    while curr != head:
        yield curr
        curr = curr.next 


def print_cups(head):
    print(list(iterate(head)))


def simulate(cups, n):
    max_val = max(cups)
    cups = [Cup(x) for x in cups]
    for i, cup in enumerate(cups):
        cup.prev, cup.next = cups[i-1], cups[(i+1) % max_val]
    lookup = {c.val: c for c in cups}
    head = cups[0]

    for _ in range(n):
        first, second, last = head.next, head.next.next, head.next.next.next

        target_val = head.val - 1 if head.val > 1 else max_val
        while target_val == first.val or target_val == second.val or target_val == last.val:
            target_val = target_val - 1 if target_val > 1 else max_val

        head.next = last.next
        head = head.next

        target = lookup[target_val]
        last.next = target.next
        target.next.prev = last
        target.next = first
        first.prev = target.next

        # print_cups(head)

    return lookup[1]

start_time = time.time()
head = simulate(cups, 100)
print(''.join(str(cup.val) for cup in iterate(head)).strip('1'), f"\t{time.time() - start_time}s")

cups += [x for x in range(max(cups) + 1, 1000000 + 1)]
start_time = time.time()
head = simulate(cups, 10000000)
print(head.next.val * head.next.next.val, f"\t{time.time() - start_time}s")