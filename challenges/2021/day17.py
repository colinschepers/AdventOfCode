import math
import re

from utils import get_input


def get_trajectory(x, y, v_x, v_y):
    while x <= target_x_max and y >= target_y_min:
        yield x, y
        x, y, v_x, v_y = x + v_x, y + v_y, max(v_x - 1, 0), v_y - 1


def get_trajectories():
    for v_x in range(math.floor(math.sqrt(target_x_min * 2)), target_x_max + 1):
        for v_y in range(target_y_min, abs(target_y_min) + 1):
            trajectory = list(get_trajectory(0, 0, v_x, v_y))
            x_final, y_final = trajectory[-1]
            if target_x_min <= x_final <= target_x_max and target_y_min <= y_final <= target_y_max:
                yield trajectory


target_x_min, target_x_max, target_y_min, target_y_max = map(int, re.findall(r"-?\d+", get_input(year=2021, day=17)[0]))
trajectories = list(get_trajectories())

print(max(y for trajectory in trajectories for x, y in trajectory))
print(len(trajectories))
