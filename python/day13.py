import time
from intcode import IntCode


def run(part, show_screen=False):
    score = 0
    screen = [[0 for _ in range(35)] for _ in range(30)]
    ball_x, paddle_x = 0, 0

    game = IntCode([int(i) for i in open("../input/13.txt").read().split(",")],
                   input_callback=lambda: 1 if ball_x > paddle_x else -1 if ball_x < paddle_x else 0)

    if part == 2:
        game.memory[0] = 2

    while True:
        x, y, tile_id = game.run(), game.run(), game.run()
        if game.halted:
            break

        if x == -1 and y == 0:
            score = tile_id
        else:
            screen[y][x] = tile_id
            if tile_id == 3:
                paddle_x = x
            if tile_id == 4:
                ball_x = x

        if show_screen and paddle_x != 0:
            print(score)
            print("\n".join(''.join([' ', '█', '▧', '▬', '○'][tile] for tile in row) for row in screen))
            time.sleep(0.01)

    if part == 1:
        return sum(sum(1 for x in row if x == 2) for row in screen)

    if part == 2:
        return score


print(run(1))
print(run(2, True))
