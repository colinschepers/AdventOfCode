from collections import Counter
from typing import Mapping, Sequence

from utils import get_input

CARD_MAP = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
HAND_TYPES = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
JOKER = "1"


def _get_hand_type_rank(hand: str) -> int:
    hand_without_joker = hand.replace(JOKER, "")
    card_counts = list(sorted(Counter(hand_without_joker).values(), reverse=True)) or [0]
    card_counts[0] += sum(card == JOKER for card in hand)
    return HAND_TYPES.index(card_counts)


def _solve(lines: Sequence[str], card_map: Mapping[str, str]) -> int:
    hands = ["".join(card_map.get(char, char) for char in line.split(" ")[0]) for line in lines]
    hand_type_ranks = list(map(_get_hand_type_rank, hands))
    bets = [int(line.split(" ")[1]) for line in lines]
    return sum(bet * (i + 1) for i, (_, _, bet) in enumerate(sorted(zip(hand_type_ranks, hands, bets))))


lines = get_input(year=2023, day=7)

print(_solve(lines, CARD_MAP))
print(_solve(lines, CARD_MAP | {"J": JOKER}))
