use std::fs::read_to_string;

fn get_puzzle_input() -> Vec<i32> {
    read_to_string("input/5.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|int| int.parse().unwrap())
        .collect()
}

enum Mode {
    Position,
    Immediate,
}

fn get(memory: &[i32], location: usize, mode: Mode) -> i32 {
    match mode {
        Mode::Position => memory[memory[location] as usize],
        Mode::Immediate => memory[location],
    }
}

fn set(memory: &mut [i32], location: usize, value: i32) {
    memory[memory[location] as usize] = value;
}

fn run_program(_memory: Vec<i32>, _input: &[i32]) -> Vec<i32> {
    let mut memory = _memory;
    let mut input_iter = _input.iter();
    let mut output = Vec::new();
    let mut instruction_pointer = 0;
    loop {
        let current_instruction = memory[instruction_pointer];
        let opcode = current_instruction % 100;
        let p1_mode = if ((current_instruction / 100) % 10) == 0 { Mode::Position } else { Mode::Immediate };
        let p2_mode = if ((current_instruction / 1000) % 10) == 0 { Mode::Position } else { Mode::Immediate };

        match opcode {
            1 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                set(&mut memory, instruction_pointer + 3, parameter2 + parameter1);
                instruction_pointer += 4;
            }
            2 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                set(&mut memory, instruction_pointer + 3, parameter2 * parameter1);
                instruction_pointer += 4;
            }
            3 => {
                set(&mut memory, instruction_pointer + 1, *input_iter.next().unwrap());
                instruction_pointer += 2;
            }
            4 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                output.push(parameter1);
                instruction_pointer += 2;
            }
            5 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                if parameter1 != 0 {
                    instruction_pointer = parameter2 as usize;
                } else {
                    instruction_pointer += 3;
                }
            }
            6 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                if parameter1 == 0 {
                    instruction_pointer = parameter2 as usize;
                } else {
                    instruction_pointer += 3;
                }
            }
            7 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                set(&mut memory, instruction_pointer + 3, (parameter1 < parameter2) as i32);
                instruction_pointer += 4;
            }
            8 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                set(&mut memory, instruction_pointer + 3, (parameter1 == parameter2) as i32);
                instruction_pointer += 4;
            }
            99 => {
                break;
            }
            _ => panic!("Unknown opcode")
        }
    }
    output
}


pub fn part1() {
    let part1 = run_program(get_puzzle_input(), &[1]);
    print!("Day 5, Part 1: {:?}\n", *part1.last().unwrap());
}

pub fn part2() {
    let part2 = run_program(get_puzzle_input(), &[5]);
    print!("Day 5, Part 2: {:?}\n", *part2.last().unwrap());
}


