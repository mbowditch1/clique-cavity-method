use std::path::PathBuf;
use rust::get_graph::*;
use graph::prelude::*;
use rust::simulate::{SIR, node_risk};
use rust::utils::*;
use rust::cavity::original_cavity;

fn main() {
    // First do original approach (not considering cliques) 
    // let G = get_simple_graph(3, 3, 900);
    let G = get_erdos_renyi(900, 6);
    let trans = arange(0.0, 1.0, 0.01);
    original_cavity(&G, &trans);
    node_risk(&G, &trans);
}

