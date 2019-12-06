mod day1;
mod day2;
mod day5;
mod day6;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day: u8 =
        if args.len() == 1 {
            0
        } else {
            args[1].parse::<u8>().expect("Invalid day number")
        };

    match day {
        0 => {
            day1::part1();
            day1::part2();
            day2::part1();
            day2::part2();
            day5::part1();
            day5::part2();
            day6::part1();
            day6::part2();
        }
        1 => {
            day1::part1();
            day1::part2();
        }
        2 => {
            day2::part1();
            day2::part2();
        }
        5 => {
            day5::part1();
            day5::part2();
        }
        6 => {
            day6::part1();
            day6::part2();
        }

        _ => eprintln!("Nothing for this day"),
    };
}
