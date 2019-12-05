use std::fs::read_to_string;


fn get_input() -> Vec<usize> {
    read_to_string("input/2.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|int| int.parse().unwrap())
        .collect()
}

fn run_program(input: Vec<usize>, noun: usize, verb: usize) -> usize {
    let mut memory = input;
    memory[1] = noun;
    memory[2] = verb;

    let mut instruction_pointer = 0;
    loop {
        let opcode = memory[instruction_pointer];
        let (parameter_1, parameter_2, parameter_3) = (
            memory[instruction_pointer + 1],
            memory[instruction_pointer + 2],
            memory[instruction_pointer + 3]
        );

        match opcode {
            1 => {
                memory[parameter_3] = memory[parameter_2] + memory[parameter_1];
                instruction_pointer += 4;
            }
            2 => {
                memory[parameter_3] = memory[parameter_2] * memory[parameter_1];
                instruction_pointer += 4;
            }
            99 => {
                break;
            }
            _ => panic!("Unknown opcode")
        }
    }
    memory[0]
}

fn find_values(input: Vec<usize>, wanted: usize) -> (usize, usize) {
    for noun in 0..100 {
        for verb in 0..100 {
            if wanted == run_program((input).clone(), noun, verb) {
                return (noun, verb);
            }
        }
    }
    panic!("no solutions under 99,99 found")
}

pub fn part1() {
    let output = run_program( get_input(), 12, 2);
    print!("Day 2, Part 1: {}\n", output);
}

pub fn part2() {
    let (noun, verb) = find_values( get_input(), 19690720);
    print!("Day 2, Part 2: {}\n", 100 * noun + verb);
}


