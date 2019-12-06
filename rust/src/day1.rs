use std::fs::read_to_string;

fn get_input() -> Vec<i32> {
    read_to_string("../input/1.txt")
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

pub fn part1() {
    let total_fuel_needed: i32 = get_input().iter().map(calc_fuel_part1).sum();
    print!("Day 1, Part 1: {}\n", total_fuel_needed);
}

pub fn part2() {
    let total_fuel_needed: i32 = get_input().iter().map(calc_fuel_part2).sum();
    print!("Day 1, Part 2: {}\n", total_fuel_needed);
}


