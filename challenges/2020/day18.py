import re 


path = './data/day18.txt'
with open(path, encoding = 'utf-8') as f:
    lines = [l.strip().replace(' ', '') for l in f.readlines()]

def solve(input):
    while '(' in input:
        input = re.sub(r'\(([^\(\)]+)\)', lambda m: str(solve(m.group(1))), input)
    while m := re.match('(\d+)([\+\*])(\d+)', input):
        a, b, op = solve(m.group(1)), solve(m.group(3)), m.group(2)
        val = a + b if op == '+' else  a * b
        input = str(val) + input[len(m.group(0)):]
    return int(input)
        

solutions = [solve(x) for x in lines]
print(sum(solutions))


def solve(input):
    while '(' in input:
        input = re.sub(r'\(([^\(\)]+)\)', lambda m: str(solve(m.group(1))), input)
    while '+' in input:
        input = re.sub('(\d+)\+(\d+)', lambda m: str(solve(m.group(1)) + solve(m.group(2))), input)
    while '*' in input:
        input = re.sub('(\d+)\*(\d+)', lambda m: str(solve(m.group(1)) * solve(m.group(2))), input)
    return int(input)


solutions = [solve(x) for x in lines]
print(sum(solutions))