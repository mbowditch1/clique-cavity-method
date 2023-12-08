use graph::prelude::*;
use rand::Rng;
use crate::utils::arange;
use std::fs::File;
use std::error::Error;
use csv::Writer;

pub fn SIR_step(G: &UndirectedCsrGraph<usize>, I: &mut Vec<usize>, R: &mut Vec<usize>, stats: &mut Vec<(usize, usize, usize)>, T: f64) {
    let mut rng = rand::thread_rng();

    // Recover infected nodes
    for i in I.iter() {
        R.push(*i);
    }

    // For each infected node, infect its neighbors with probability T
    let mut new_infected: Vec<usize> = Vec::new();
    for i in I.iter() {
        let neighbors = G.neighbors(*i);
        for n in neighbors {
            if !I.contains(&n) && !R.contains(&n) && !new_infected.contains(&n) {
                if rng.gen::<f64>() < T {
                    new_infected.push(*n);
                }
            }
        }
    }

    // Add new infected nodes to infected list
    *I = new_infected.clone();
    stats.push((G.node_count() - I.len() - R.len(), I.len(), R.len()));
}


pub fn SIR(G: &UndirectedCsrGraph<usize>, T: f64, initial_infected: usize) -> (Vec<(usize, usize, usize)>, Vec<usize>) {
    let mut rng = rand::thread_rng();

    let mut I: Vec<usize> = Vec::new();
    let mut R: Vec<usize> = Vec::new();
    let mut stats: Vec<(usize, usize, usize)> = Vec::new();
    for mut x in 0..initial_infected {
        let i = rng.gen_range(0..G.node_count());
        if !I.contains(&i) {
            I.push(i);
        } else {
            x -= 1;
        }
    }

    stats.push((G.node_count() - I.len() - R.len(), I.len(), R.len()));
    while I.len() > 0 {
        SIR_step(G, &mut I, &mut R, &mut stats, T);
    }

    (stats, R)
}


pub fn node_risk(G: &UndirectedCsrGraph<usize>) -> Result<(), Box<dyn Error>> {
    let trans = arange(0.0, 1.0, 0.01);
    let mut node_risk = vec![vec![0.0; G.node_count()]; trans.len()].to_vec();
    let iterations = 1000;
    for t in 0..trans.len() {
        for _ in 0..iterations {
            let (stats, R) = SIR(G, trans[t], 1);
            for r in R.iter() {
                node_risk[t][*r] += 1.0 / (iterations as f64);
            }
        }
    }

    // Write node risks to file
    let file_path = "/home/mbowditch/Documents/cavity_method/code/python/data/output.csv";
    let mut writer = Writer::from_path(file_path)?;

    // Write tuples to the CSV file
    for t in 0..trans.len() {
        let string_risk: Vec<String> = node_risk[t].iter().map(|&x| x.to_string()).collect();
        writer.write_record(string_risk)?;
    }

    // Close the CSV file
    writer.flush()?;
    Ok(())
}
