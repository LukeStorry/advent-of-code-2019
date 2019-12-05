use std::fs::read_to_string;

fn get_puzzle_input() -> Vec<i32> {
    read_to_string("input/5.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|int| int.parse().unwrap())
        .collect()
}

fn get(memory: &Vec<i32>, location: i32) -> i32{
    *memory.get(location as usize).unwrap()
}

fn run_program(_memory: Vec<i32>, _input: &[i32]) -> Vec<i32> {
    let mut memory = _memory;
    let mut input_iter = _input.iter();
    let mut output = Vec::new();
    let mut instruction_pointer = 0;
    loop {
        let current_instruction = get(&memory, instruction_pointer);
        let opcode = current_instruction % 100;
        let p1_pos_mode: bool = ((current_instruction / 100) % 10) == 0;
        let p2_pos_mode: bool = ((current_instruction / 1000) % 10) == 0;

        let (mut parameter1, mut parameter2, parameter3) = (
            get(&memory, instruction_pointer + 1),
            get(&memory, instruction_pointer + 2),
            get(&memory, instruction_pointer + 3)
        );
        match opcode {
            1 => {
                parameter1 = if p1_pos_mode { get(&memory, parameter1) } else { parameter1 };
                parameter2 = if p2_pos_mode { get(&memory, parameter2) } else { parameter2 };
                memory[parameter3 as usize] = parameter2 + parameter1;
                instruction_pointer += 4;
            }
            2 => {
                parameter1 = if p1_pos_mode { get(&memory, parameter1) } else { parameter1 };
                parameter2 = if p2_pos_mode { get(&memory, parameter2) } else { parameter2 };
                memory[parameter3 as usize] = parameter2 * parameter1;
                instruction_pointer += 4;
            }
            3 => {
                memory[parameter1 as usize] = *input_iter.next().unwrap();
                instruction_pointer += 2;
            }
            4 => {
                parameter1 = if p1_pos_mode { get(&memory, parameter1) } else { parameter1 };
                output.push(parameter1);
                instruction_pointer += 2;
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
    let output = run_program(get_puzzle_input(), &[1]);
    print!("Day 5, Part 1: {:?}\n", *output.last().unwrap());
}


