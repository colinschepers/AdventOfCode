from utils import get_input

data = list(map(int, get_input(1)))

answer = sum(data[i] < data[i + 1] for i in range(len(data) - 1))
print(answer)

sums = [data[i] + data[i + 1] + data[i + 2] for i in range(len(data) - 2)]
answer = sum(sums[i] < sums[i + 1] for i in range(len(sums) - 1))
print(answer)
