from collections import defaultdict
from collections.abc import Sequence, Mapping, Set

from utils import get_input, split_lines, split_on_condition

Rules = Mapping[int, Set[int]]
Update = Sequence[int]


def parse_rules(rule_lines: Sequence[str]) -> Rules:
    rule_dict = defaultdict(set)
    for line in rule_lines:
        before, after = line.split("|")
        rule_dict[int(before)].add(int(after))
    return rule_dict


def is_correct(update: Update, rules: Rules) -> bool:
    seen = set()
    for nr in update:
        if seen & rules[nr]:
            return False
        seen.add(nr)
    return True


def fix_update(update: Update, rules: Rules) -> Update:
    fixed_update = []
    for nr in update:
        for idx, other in enumerate(fixed_update):
            if other in rules[nr]:
                fixed_update.insert(idx, nr)
                break
        else:
            fixed_update.append(nr)
    return fixed_update


rule_lines, update_lines = split_lines(get_input(2024, 5))
rules = parse_rules(rule_lines)
updates = (list(map(int, line.split(","))) for line in update_lines)
correct, incorrect = split_on_condition(updates, lambda x: is_correct(x, rules))

print(sum(update[len(update) // 2] for update in correct))
print(sum(fix_update(update, rules)[len(update) // 2] for update in incorrect))
