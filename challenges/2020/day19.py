
r = open('./data/day19.txt').read()
input = r.split('\n\n')

#Part 1
rules = {}
for text in input[0].splitlines():
    data = text.split(': ')
    id, content = data[0], [sub.strip().split(' ') for sub in data[1].split('|')]
    rules[id] = content

messages = input[1].splitlines()

def solve(id, msg, i):
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

results = [len(m) in solve('0', m, 0) for m in messages]
print(sum(x for x in results))


rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42','11','31']]
results = [len(m) in solve('0', m, 0) for m in messages]
print(sum(x for x in results))