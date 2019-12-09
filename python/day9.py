memory = [int(i) for i in open("../input/9.txt").read().split(",")]
_input = iter([2])
relative_base = 0


def write(addr, val):
    global memory
    if addr >= len(memory):
        memory += [0] * (addr - len(memory) + 10)
    memory[addr] = val


def read(addr):
    if addr < len(memory):
        return memory[addr]
    else:
        return 0


def address(addr, mode):
    if mode == 1:
        return addr
    elif mode == 2:
        return relative_base + read(addr)
    else:
        return read(addr)


instruction_pointer = 0
while True:
    current_operation = read(instruction_pointer)
    opcode = current_operation % 100

    if opcode in (1, 2, 4, 5, 6, 7, 8, 9):
        p1 = read(address(instruction_pointer + 1, (current_operation // 100) % 10))
    if opcode in (1, 2, 5, 6, 7, 8):
        p2 = read(address(instruction_pointer + 2, (current_operation // 1000) % 10))
    if opcode in (1, 2, 7, 8):
        p3 = address(instruction_pointer + 3, (current_operation // 10000) % 10)

    if opcode == 1:
        write(p3, p1 + p2)
        instruction_pointer += 4

    elif opcode == 2:
        write(p3, p1 * p2)
        instruction_pointer += 4

    elif opcode == 3:
        write(address(instruction_pointer + 1, (current_operation // 100) % 10), next(_input))
        instruction_pointer += 2

    elif opcode == 4:
        print(p1)
        instruction_pointer += 2

    elif opcode == 5:
        if p1 != 0:
            instruction_pointer = p2
        else:
            instruction_pointer += 3

    elif opcode == 6:
        if p1 == 0:
            instruction_pointer = p2
        else:
            instruction_pointer += 3

    elif opcode == 7:
        write(p3, int(p1 < p2))
        instruction_pointer += 4

    elif opcode == 8:
        write(p3, int(p1 == p2))
        instruction_pointer += 4

    elif opcode == 9:
        relative_base += p1
        instruction_pointer += 2

    elif opcode == 99:
        break
