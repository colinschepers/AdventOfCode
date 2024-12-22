from collections import defaultdict
from collections.abc import Sequence
from itertools import pairwise, accumulate
from typing import Tuple

from utils import get_input


def step(secret: int) -> int:
    secret = secret ^ (secret * 64) % 16777216
    secret = secret ^ (secret // 32) % 16777216
    return secret ^ (secret * 2048) % 16777216


def get_best_price(buyer_secrets: Sequence[Sequence[int]]) -> int:
    sell_options: dict[Tuple[int, ...], int] = defaultdict(int)

    for secrets in buyer_secrets:
        changes_seen: set[Tuple[int, ...]] = set()
        last_4_changes: Tuple[int, ...] = tuple()
        for prev_secret, secret in pairwise(secrets):
            last_4_changes = (*last_4_changes[-3:], secret % 10 - prev_secret % 10)
            if len(last_4_changes) == 4 and last_4_changes not in changes_seen:
                sell_options[last_4_changes] += secret % 10
            changes_seen.add(last_4_changes)

    return max(sell_options.values())


buyer_secrets = tuple(
    tuple(accumulate(range(2000), lambda s, _: step(s), initial=int(secret)))
    for secret in get_input(2024, 22)
)
print(sum(secrets[-1] for secrets in buyer_secrets))
print(get_best_price(buyer_secrets))
