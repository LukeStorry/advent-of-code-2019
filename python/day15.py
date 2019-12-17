from random import randint

from intcode import IntCode

area = [["▮" for _ in range(100)] for _ in range(50)]
initial_x, initial_y = 50, 20
droid_x, droid_y = 50, 20
next_x, next_y = -1, -1
area[droid_y][droid_x] = "X"
trail = [(droid_x, droid_y)]


def calc_input():
    global next_x, next_y
    direction = randint(1, 4)
    next_x, next_y = next_position[direction]()
    return direction


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

    if status == 0:
        area[next_y][next_x] = "▮"

    else:
        if (next_x, next_y) in trail:
            trail = trail[:trail.index((next_x, next_y)) + 1]
        else:
            trail.append((next_x, next_y))

        area[droid_y][droid_x] = "▯"
        droid_x, droid_y = next_x, next_y

        if status == 2:
            break

for x, y in trail:
    area[y][x] = '#'

print("\n".join(''.join(row) for row in area[::-1]))
print(trail)
print(len(trail)-1)
