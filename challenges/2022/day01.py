from utils import get_input
import heapq

data = " ".join(get_input(year=2022, day=1))
data = [sum(map(int, grp.split(" "))) for grp in data.split("  ")]

print(max(data))
print(sum(heapq.nlargest(3, data)))
