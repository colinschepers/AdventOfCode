from functools import lru_cache

from utils import get_input

DIRAC_TRIPLE_ROLL_COUNTS = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))


def solve_part_1(pos_player, pos_opponent, score_player=0, score_opponent=0, die=1):
    if score_opponent >= 1000:
        return (die - 1) * score_player

    roll = (die + 1) * 3
    new_pos = ((pos_player - 1 + roll) % 10) + 1
    return solve_part_1(pos_opponent, new_pos, score_opponent, score_player + new_pos, die + 3)


@lru_cache(maxsize=None)
def solve_part_2(pos_player, pos_opponent, score_player=0, score_opponent=0):
    if score_opponent >= 21:
        return 0, 1

    player_wins_total = opponent_wins_total = 0
    for roll, count in DIRAC_TRIPLE_ROLL_COUNTS:
        new_pos = ((pos_player - 1 + roll) % 10) + 1
        opponent_wins, player_wins = solve_part_2(pos_opponent, new_pos, score_opponent, score_player + new_pos)
        player_wins_total += count * player_wins
        opponent_wins_total += count * opponent_wins
    return player_wins_total, opponent_wins_total


data = get_input(year=2021, day=21)
pos_1, pos_2 = int(data[0][-1]), int(data[1][-1])

print(solve_part_1(pos_1, pos_2))
print(max(solve_part_2(pos_1, pos_2)))
