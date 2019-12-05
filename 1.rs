use std::fs::File;
use std::io::{BufRead, BufReader};


fn get_input() -> Vec<i32> {
    let file = File::open("input1.txt").unwrap();
    BufReader::new(file).lines()
        .map(|line| line.unwrap().parse::<i32>().unwrap())
        .collect()
}

fn fuel1(mass: &i32) -> i32 { mass / 3 - 2 }

fn fuel2(mass: &i32) -> i32 {
    let fuel =  mass / 3 - 2;
    if fuel <= 0 { 0 } else {
        fuel + fuel2(&fuel)
    }
}


fn main() {
    let input = get_input();

    let fuel_sum_1: i32 = input.iter().map(fuel1).sum();
    let fuel_sum_2: i32 = input.iter().map(fuel2).sum();

    print!("{}\n{}", fuel_sum_1, fuel_sum_2);
}


