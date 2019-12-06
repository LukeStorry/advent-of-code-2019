use std::fs::read_to_string;
use std::str::FromStr;
use std::string::ParseError;
use std::collections::HashMap;

#[derive(Debug)]
struct Orbit {
    parent: String,
    child: String,
}

impl FromStr for Orbit {
    type Err = ParseError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let split: Vec<&str> = s.split(')').collect();
        Ok(Orbit { parent: split[0].to_string(), child: split[1].to_string() })
    }
}

fn get_puzzle_input() -> Vec<Orbit> {
    read_to_string("../input/6.txt")
        .unwrap()
        .trim()
        .split('\n')
        .map(|line| line.parse().unwrap())
        .collect()
}

fn create_graph(orbits: Vec<Orbit>) -> HashMap<String, Vec<String>> {
    let mut universe = HashMap::new();
    for orbit in orbits {
        let children = universe.entry(orbit.parent).or_insert_with(Vec::new);
        children.push(orbit.child);
    }
    universe
}

//    fn sum_orbits(map: &HashMap<&str, Vec<&str>>, name: &str, depth: u32) -> u32 {
//        let mut result = depth as u32;
//        if let Some(list) = map.get(name) {
//            for entry in list.iter() {
//                result += checksum(map, entry, depth + 1);
//            }
//        }
//        result
//    }

pub fn part1() {
    print!("{:?}", create_graph(get_puzzle_input()).get("COM"));
}


pub fn part2() {}

