from typing import List, Tuple

from utils import split_lines, get_input


def combat(player1: List[int], player2: List[int]) -> Tuple[List[int], List[int]]:
    while player1 and player2:
        if player1[0] > player2[0]:
            player1 += player1.pop(0), player2.pop(0)
        else:
            player2 += player2.pop(0), player1.pop(0)
    return player1, player2


def recursive_combat(player1: List[int], player2: List[int]) -> Tuple[List[int], List[int]]:
    if not player1 or not player2:
        return player1, player2

    transposition_table = set()
    while player1 and player2:
        hash = (tuple(player1), tuple(player2))
        if hash in transposition_table:
            return player1 + player2, []
        transposition_table.add(hash)

        card_p1, card_p2 = player1.pop(0), player2.pop(0)
        if len(player1) >= card_p1 and len(player2) >= card_p2:
            p1, p2 = player1[:card_p1], player2[:card_p2]
            p1_win = max(p1) > max(p2) or recursive_combat(p1, p2)[0]
        else:
            p1_win = card_p1 > card_p2

        if p1_win:
            player1 += card_p1, card_p2
        else:
            player2 += card_p2, card_p1

    return player1, player2


player1, player2 = split_lines(get_input(year=2020, day=22))
player1 = [int(x) for x in player1[1:]]
player2 = [int(x) for x in player2[1:]]

p1, p2 = combat(player1.copy(), player2.copy())
print(sum(c * (i + 1) for i, c in enumerate(reversed(p1 or p2))))

p1, p2 = recursive_combat(player1.copy(), player2.copy())
print(sum(c * (i + 1) for i, c in enumerate(reversed(p1 or p2))))
