#!/usr/bin/env python

from __future__ import annotations
import re
from itertools import combinations


class Xyz:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x, self.y, self.z = x, y, z

    def __add__(self, other: Xyz) -> Xyz:
        return Xyz(self.x + other.x,
                   self.y + other.y,
                   self.z + other.z)

    def __sub__(self, other: Xyz) -> Xyz:
        return Xyz(self.x - other.x,
                   self.y - other.y,
                   self.z - other.z)

    @property
    def abs_sum(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __str__(self) -> str:
        return f"<x={self.x}, y={self.y}, z={self.z}>"

    def __eq__(self, other: Xyz) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z


class Moon:
    def __init__(self, info) -> None:
        self.position = Xyz(*map(int, re.search(r'<x=(.+), y=(.+), z=(.+)>', info).groups()))
        self.velocity = Xyz(0, 0, 0)

    @property
    def total_energy(self) -> int:
        return self.position.abs_sum * self.velocity.abs_sum

    def apply_gravity(self, other: Moon):
        s, o = self.position, other.position
        diff = Xyz(1 if s.x > o.x else -1 if s.x < o.x else 0,
                   1 if s.y > o.y else -1 if s.y < o.y else 0,
                   1 if s.z > o.z else -1 if s.z < o.z else 0)
        self.velocity -= diff
        other.velocity += diff

    def update_position(self):
        self.position += self.velocity

    def __repr__(self) -> str:
        return f"pos={self.position}, vel={self.velocity}"

    def __eq__(self, other: Moon) -> bool:
        return self.position == other.position and self.velocity == other.velocity


initial_state = [Moon(moon) for moon in open('../input/12.txt').read().split('\n')]
moons = [Moon(moon) for moon in open('../input/12.txt').read().split('\n')]

minimum_loop = [0,0,0]

# Part 1
for i in range(1000):
    [moon1.apply_gravity(moon2) for moon1, moon2 in combinations(moons, 2)]
    [moon.update_position() for moon in moons]

print(sum(moon.total_energy for moon in moons))
