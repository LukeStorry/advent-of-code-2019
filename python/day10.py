import math
from collections import defaultdict

asteroids = [(x, y)
             for y, line in enumerate(open('./input.txt').read().split('\n'))
             for x, char in enumerate(line) if char == "#"]


def angle(a, b):
    return -math.atan2(b[0] - a[0], b[1] - a[1])


def detections(a):
    return len(set(angle(a, b) for b in asteroids))


best_location = max(asteroids, key=detections)

print("Part 1: ", detections(best_location))


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


targets = defaultdict(list)
for a in asteroids:
    targets[angle(best_location, a)].append(a)

hits = [
    min(targets[angle], key=lambda a: distance(best_location, a))
    for angle in sorted(targets.keys())
]

print("Part2: ", hits[199][0] * 100 + hits[199][1])
