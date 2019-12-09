use std::fs::read_to_string;

fn get_puzzle_input() -> Vec<i64> {
    read_to_string("../input/9.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|int| int.parse().unwrap())
        .collect()
}

fn expand_memory(input: &mut Vec<i64>) {
    let mut extra_memory = vec![0 as i64; 99999];
    input.append(&mut extra_memory);
}

#[derive(PartialEq)]
enum Mode {
    Position,
    Immediate,
    Relative,
}

impl From<i64> for Mode {
    fn from(i: i64) -> Self {
        print!("{}\n", i);
        match i {
            0 => Mode::Position,
            1 => Mode::Immediate,
            2 => Mode::Relative,
            _ => panic!("Unknown mode type"),
        }
    }
}

fn get(memory: &[i64], location: i64, mode: Mode) -> i64 {
    match mode {
        Mode::Position => memory[memory[location as usize] as usize],
        Mode::Immediate => memory[location as usize],
        Mode::Relative => memory[location as usize],
    }
}

fn set(memory: &mut [i64], location: i64, value: i64) {
    memory[memory[location as usize] as usize] = value;
}

fn run_program(_memory: Vec<i64>, _input: &[i64]) -> Vec<i64> {
    let mut memory = _memory;
    let mut extra_memory =
    let mut input_iter = _input.iter();
    let mut output = Vec::new();
    let mut instruction_pointer: i64 = 0;
    let mut relative_base: i64 = 0;
    loop {
        let current_instruction = memory[instruction_pointer as usize];
        print!("\n{}\n", current_instruction);
        let opcode = current_instruction % 100;
        let p1_mode = Mode::from((current_instruction / 100) % 10);
        let p2_mode = Mode::from((current_instruction / 1000) % 10);
        let p3_mode = Mode::from((current_instruction / 10000) % 10);

        match opcode {
            1 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                let parameter3 = if p3_mode == Mode::Relative {
                    print!(".");
                    instruction_pointer + 3 + relative_base
                } else { instruction_pointer + 3 };
                set(&mut memory, parameter3, parameter2 + parameter1);
                instruction_pointer += 4;
            }
            2 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                let parameter3 = if p3_mode == Mode::Relative { instruction_pointer + 3 + relative_base } else { instruction_pointer + 3 };
                set(&mut memory, parameter3, parameter2 * parameter1);
                instruction_pointer += 4;
            }
            3 => {
                let parameter1 = if p3_mode == Mode::Relative { instruction_pointer + 1 + relative_base } else { instruction_pointer + 1 };
                set(&mut memory, parameter1, *input_iter.next().unwrap());
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
                    instruction_pointer = parameter2;
                } else {
                    instruction_pointer += 3;
                }
            }
            6 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                if parameter1 == 0 {
                    instruction_pointer = parameter2;
                } else {
                    instruction_pointer += 3;
                }
            }
            7 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                let parameter3 = if p3_mode == Mode::Relative { instruction_pointer + 3 + relative_base } else { instruction_pointer + 3 };
                set(&mut memory, parameter3, (parameter1 < parameter2) as i64);
                instruction_pointer += 4;
            }
            8 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                let parameter2 = get(&memory, instruction_pointer + 2, p2_mode);
                let parameter3 = if p3_mode == Mode::Relative { instruction_pointer + 3 + relative_base } else { instruction_pointer + 3 };
                set(&mut memory, parameter3, (parameter1 == parameter2) as i64);
                instruction_pointer += 4;
            }
            9 => {
                let parameter1 = get(&memory, instruction_pointer + 1, p1_mode);
                relative_base = parameter1;
                instruction_pointer += 1;
            }
            99 => {
                break;
            }
            _ => panic!("Unknown opcode")
        }
        // print!("{:?}\n", memory);
    }
    print!("{:?}\n", output);
    output
}


pub fn part1() {
//    let mut mem = get_puzzle_input();
 let mut mem = vec![109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99];
// let mut mem = vec![1102,34915192,34915192,7,4,7,99,0];
//     let mut mem = vec![104,1125899906842624,99];

    expand_memory(&mut mem);
    run_program(mem, &[1]);
}

//pub fn part2() {
//    let part2 = run_program(get_puzzle_input(), &[5]);
//    print!("Day 9, Part 2: {:?}\n", *part2.last().unwrap());
//}

