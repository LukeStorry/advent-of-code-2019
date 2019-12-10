import math
from collections import defaultdict

asteroids = [(x, y) for y, line in enumerate(open('../input/10.txt').read().split('\n')) for x, char in enumerate(line)
             if char == "#"]

# Part 1
print(max(map(lambda a: len(set(math.atan2(a[1] - y, a[0] - x) for x, y in asteroids)), asteroids)))


# Part 2
def angle(a, b): return -math.atan2(b[0] - a[0], b[1] - a[1])

location = max(asteroids, key=lambda a: len(set(angle(a, b) for b in asteroids)))
hits = [min(asts, key=lambda a: math.sqrt((location[0] - a[0]) ** 2 + (location[1] - a[1]) ** 2))
        for angle, asts in sorted(defaultdict(list, [(angle(location, a), [a]) for a in asteroids]).items())]
print(hits[199][0] * 100 + hits[199][1])
