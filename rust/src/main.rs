use std::path::PathBuf;
use rust::get_graph::get_simple_graph;
use graph::prelude::*;
use rust::simulate::{SIR, node_risk};

fn main() {
    // First do original approach (not considering cliques) 
    let graph = get_simple_graph(3, 3, 900);
    node_risk(&graph);
}

