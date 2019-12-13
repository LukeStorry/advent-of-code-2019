class IntCode:
    def __init__(self, memory, input_callback=None):
        self.memory = memory[:]
        self.inputs = []
        self.input_callback = input_callback
        self.relative_base = 0
        self.instruction_pointer = 0
        self.halted = False

    def input(self, i):
        self.inputs.append(i)
        return self

    def read(self, addr):
        if addr < len(self.memory):
            return self.memory[addr]
        else:
            return 0

    def write(self, addr, val):

        if addr >= len(self.memory):
            self.memory.extend([0] * (addr - len(self.memory) + 10))
        self.memory[addr] = val

    def address(self, addr, mode):
        if mode == 1:
            return addr
        elif mode == 2:
            return self.relative_base + self.read(addr)
        else:
            return self.read(addr)

    def run(self):
        while True:
            current_operation = self.read(self.instruction_pointer)
            opcode = current_operation % 100

            if opcode in (1, 2, 4, 5, 6, 7, 8, 9):
                p1 = self.read(
                    self.address(self.instruction_pointer + 1,
                                 (current_operation // 100) % 10))
            if opcode in (1, 2, 5, 6, 7, 8):
                p2 = self.read(
                    self.address(self.instruction_pointer + 2,
                                 (current_operation // 1000) % 10))
            if opcode in (1, 2, 7, 8):
                p3 = self.address(self.instruction_pointer + 3,
                                  (current_operation // 10000) % 10)

            if opcode == 1:
                self.write(p3, p1 + p2)
                self.instruction_pointer += 4

            elif opcode == 2:
                self.write(p3, p1 * p2)
                self.instruction_pointer += 4

            elif opcode == 3:
                next_input = self.inputs.pop(0) if self.inputs else self.input_callback()

                self.write(
                    self.address(self.instruction_pointer + 1,
                                 (current_operation // 100) % 10), next_input)
                self.instruction_pointer += 2

            elif opcode == 4:
                self.instruction_pointer += 2
                return p1

            elif opcode == 5:
                if p1 != 0:
                    self.instruction_pointer = p2
                else:
                    self.instruction_pointer += 3

            elif opcode == 6:
                if p1 == 0:
                    self.instruction_pointer = p2
                else:
                    self.instruction_pointer += 3

            elif opcode == 7:
                self.write(p3, int(p1 < p2))
                self.instruction_pointer += 4

            elif opcode == 8:
                self.write(p3, int(p1 == p2))
                self.instruction_pointer += 4

            elif opcode == 9:
                self.relative_base += p1
                self.instruction_pointer += 2

            elif opcode == 99:
                self.halted = True
                return None
