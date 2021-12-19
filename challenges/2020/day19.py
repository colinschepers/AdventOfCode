import re

from utils import get_input, split_lines

rules, messages = split_lines(get_input(year=2020, day=19))
rules = {line.split(": ")[0]: [sub.split(' ') for sub in line.split(": ")[1].split(' | ')] for line in rules}


def solve(id: str, msg: str, i: int):
    rule = rules[id]
    if rule[0][0][0] == '"':
        return {i + 1} if i < len(msg) and rule[0][0][1] == msg[i] else set()

    tail = set()
    for subrule in rule:
        tmp1 = {i}
        for part in subrule:
            tmp2 = set()
            for x in tmp1:
                tmp2 = tmp2 | solve(part, msg, x)
            tmp1 = tmp2
        tail = tail | tmp1
    return tail


print(sum(len(m) in solve('0', m, 0) for m in messages))

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
print(sum(len(m) in solve('0', m, 0) for m in messages))
