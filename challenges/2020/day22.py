
inputs = open('./data/day22.txt').read().strip().split('\n\n')
player1 = [int(x) for x in inputs[0].split('\n')[1:]]
player2 = [int(x) for x in inputs[1].split('\n')[1:]]

def combat(p1, p2):
    while p1 and p2:
        if p1[0] > p2[0]:
            p1 += p1.pop(0), p2.pop(0)
        else:
            p2 += p2.pop(0), p1.pop(0)
    return p1 or p2

winning_hand = combat(player1.copy(), player2.copy())

print(sum(c * (i+1) for i, c in enumerate(reversed(winning_hand))))


def recursive_combat(p1, p2, d = 0):
    if not p1 or not p2:
        return p1, p2

    transposition_table = set()
    while p1 and p2:
        hash = str(p1) + str(p2)
        if hash in transposition_table:
            return p1 + p2, []
        transposition_table.add(hash)

        c1, c2 = p1.pop(0), p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            _p1, _p2 = recursive_combat(p1[:c1].copy(), p2[:c2].copy())
            p1_win = bool(_p1)
        else:
            p1_win = c1 > c2

        if p1_win:
            p1 += c1, c2
        else:
            p2 += c2, c1
    return p1, p2

p1, p2 = recursive_combat(player1.copy(), player2.copy())

print(sum(c * (i+1) for i, c in enumerate(reversed(p1 or p2))))

