use std::fs::read_to_string;

fn get_input() -> Vec<i32> {
    read_to_string("input1.txt")
        .unwrap()
        .trim()
        .split('\n')
        .map(|int| int.parse().unwrap())
        .collect()
}

fn calc_fuel_part1(mass: &i32) -> i32 {
    mass / 3 - 2
}

fn calc_fuel_part2(mass: &i32) -> i32 {
    let fuel = mass / 3 - 2;
    fuel + (if fuel <= 0 { 0 } else { calc_fuel_part2(&fuel) })
}

fn main() {
    let input = get_input();

    let total_fuel_part1: i32 = input.iter().map(calc_fuel_part1).sum();
    let total_fuel_part2: i32 = input.iter().map(calc_fuel_part2).sum();

    print!("{}\n{}", total_fuel_part1, total_fuel_part2);
}


