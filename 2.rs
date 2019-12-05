use std::fs::read_to_string;


fn get_input() -> Vec<usize> {
    read_to_string("input2.txt")
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

    let mut instruction_counter = 0;
    loop {
        let opcode = memory[instruction_counter];
        let (m_1, m_2, m_3) = (memory[instruction_counter + 1], memory[instruction_counter + 2], memory[instruction_counter + 3]);

        match opcode {
            1 => {
                memory[m_3] = memory[m_2] + memory[m_1];
            }
            2 => {
                memory[m_3] = memory[m_2] * memory[m_1];
            }
            99 => {
                break;
            }
            _ => panic!("Unknown opcode")
        }
        instruction_counter += 4;
    }
    memory[0]
}

fn main() {
    print!("{}", run_program(get_input(), 12, 2))
}


