use std::path::PathBuf;
use rust::get_graph::*;
use graph::prelude::*;
use rust::simulate::{SIR, node_risk};
use rust::utils::*;
use rust::cavity::original_cavity;

fn main() {
    let G = get_simple_graph(6, 4, 900);
    // let G = get_erdos_renyi(900, 6);
    let trans = arange(0.0, 1.0, 0.005);
    original_cavity(&G, &trans);
    let trans = arange(0.0, 1.0, 0.01);
    node_risk(&G, &trans);
}

