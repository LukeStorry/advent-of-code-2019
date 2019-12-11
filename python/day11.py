from enum import Enum
from intcode import IntCode


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


move = {
    Direction.UP: lambda x, y: (x, y + 1),
    Direction.RIGHT: lambda x, y: (x + 1, y),
    Direction.DOWN: lambda x, y: (x, y - 1),
    Direction.LEFT: lambda x, y: (x - 1, y),
}

turn = {
    0: lambda d: Direction((d.value + 3) % 4),
    1: lambda d: Direction((d.value + 5) % 4)
}


def run(part):
    robot = IntCode([int(i) for i in open("../input/11.txt").read().split(",")])
    hull = [[0 for _ in range(80)] for _ in range(80)]
    coords = (20, 20)
    direction = Direction.UP
    painted = set()

    if part == 2:
        hull[coords[1]][coords[0]] = 1

    while True:
        robot.input(hull[coords[1]][coords[0]])
        out = robot.run()
        if out is None:
            break
        painted.add(coords)
        hull[coords[1]][coords[0]] = out
        direction = turn[robot.run()](direction)
        coords = move[direction](*coords)

    if part == 1:
        return len(painted)
    else:
        return '\n'.join([''.join(
            [[' ', '#'][panel] for panel in row]) for row in hull[::-1] if 1 in row])


print(run(1))
print(run(2))
