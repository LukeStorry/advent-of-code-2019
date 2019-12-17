import time
from random import randint

from intcode import IntCode

area = [["▣" for _ in range(100)] for _ in range(50)]
initial_x, initial_y = 50, 20
droid_x, droid_y = 50, 20
next_x, next_y = -1, -1
area[droid_y][droid_x] = "X"


def calc_input():
    global next_x, next_y
    direction = randint(1, 4)
    next_x, next_y = next_position[direction]()
    return direction

    # for direction, calc_position in next_position.items():
    #     next_x, next_y = calc_position()
    #     if area[next_y][next_x] == " ":
    #         return direction
    # for direction, calc_position in next_position.items():
    #     next_x, next_y = calc_position()
    #     if area[next_y][next_x] == "▯":
    #         return direction


d = {
    1: "N",
    4: "E",
    2: "S",
    3: "W",
}

# north (1), east (4), south (2), west (3)
next_position = {
    1: lambda: (droid_x, droid_y + 1),
    4: lambda: (droid_x + 1, droid_y),
    2: lambda: (droid_x, droid_y - 1),
    3: lambda: (droid_x - 1, droid_y),
}

program = IntCode([int(i) for i in open("../input/15.txt").read().split(",")],
                  input_callback=calc_input)

for i in range(10000000000000):
    status = program.run()

    if program.halted:
        print("HALT")
        break

    if status == 0:  # wall
        area[next_y][next_x] = "■"

    else:  # move
        area[droid_y][droid_x] = "□"
        droid_x, droid_y = next_x, next_y
        area[droid_y][droid_x] = "○"

        if status == 2:
            print("status 2")
            break

area[initial_y][initial_x] = "X"
print("\n".join(''.join(row) for row in area[::-1]))
