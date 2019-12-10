layers = [[list(map(int, open("../input/8.txt").read()))[j + i:j + i + 25] for i in range(0, 25 * 6, 25)] for j in
          range(0, 15000, 25 * 6)]

minl = min(layers, key=lambda x : [i for l in x for i in l].count(0))
print([i1 for l in minl for i1 in l].count(1) * [i2 for l1 in minl for i2 in l1].count(2))

print("\n".join(''.join([[[' ', '#'][pixel[0]] for pixel in row] for row in [
    [[layers[layer][row][col] for layer in range(len(layers)) if layers[layer][row][col] != 2] for col in range(25)]
    for row in range(6)]][i]) for i in range(6)))
