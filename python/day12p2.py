# #!/usr/bin/env python

import re
from itertools import combinations
from functools import reduce
from math import gcd

iterations = [0, 0, 0]
moons = [[int(x) for x in re.search(r'<x=(.+), y=(.+), z=(.+)>', moon_info).groups()]
                     for moon_info in open('../input/12.txt').read().split('\n')]

initial_velocities = [0 for _ in moons]

for i in (range(3)):
    current_plane_positions = [moon[i] for moon in moons]
    initial_plane = [moon[i] for moon in moons]
    current_plane_velocities = initial_velocities[:]

    while True:
        for moon1, moon2 in combinations(range(len(current_plane_positions)), 2):
            gravity = (current_plane_positions[moon1] > current_plane_positions[moon2]) - (current_plane_positions[moon1] < current_plane_positions[moon2])
            current_plane_velocities[moon1] -= gravity
            current_plane_velocities[moon2] += gravity

        for moon in range(len(current_plane_positions)):
            current_plane_positions[moon] += current_plane_velocities[moon]

        iterations[i] += 1

        if current_plane_positions == initial_plane and current_plane_velocities == initial_velocities:
            break

print(reduce(lambda a, b: a * b // gcd(a, b), iterations))
