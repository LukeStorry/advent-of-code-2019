from enum import Enum


class Op(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


memory = [int(i) for i in open("../input/5.txt").read().split(",")]


def get_mem(location, mode):
    if mode is Mode.IMMEDIATE:
        return memory[location]
    else:
        return memory[memory[location]]


def run_program(_input):
    instruction_pointer = 0
    output = []
    while True:
        current_operation = memory[instruction_pointer]
        operation = Op(current_operation // 10 % 10 * 10 + current_operation % 10)

        modes = list(
            map(Mode, [current_operation // 100 % 10,
                       current_operation // 1000 % 10,
                       current_operation // 10000 % 10]
                ))

        if operation is Op.ADD:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            memory[memory[instruction_pointer + 3]] = parameter_1 + parameter_2
            instruction_pointer += 4

        elif operation is Op.MULTIPLY:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            memory[memory[instruction_pointer + 3]] = parameter_1 * parameter_2
            instruction_pointer += 4

        elif operation is Op.INPUT:
            memory[memory[instruction_pointer + 1]] = next(_input)
            instruction_pointer += 2

        elif operation is Op.OUTPUT:
            output.append(memory[memory[instruction_pointer + 1]])
            instruction_pointer += 2

        elif operation is Op.JUMP_IF_TRUE:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            if parameter_1 != 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3

        elif operation is Op.JUMP_IF_FALSE:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            if parameter_1 == 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3

        elif operation is Op.LESS_THAN:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            memory[memory[instruction_pointer + 3]] = 1 if parameter_1 < parameter_2 else 0
            instruction_pointer += 4

        elif operation is Op.EQUALS:
            parameter_1 = get_mem(instruction_pointer + 1, modes[0])
            parameter_2 = get_mem(instruction_pointer + 2, modes[1])
            memory[memory[instruction_pointer + 3]] = 1 if parameter_1 == parameter_2 else 0
            instruction_pointer += 4

        elif operation is Op.HALT:
            break

    return output


print(run_program(iter([5])))
