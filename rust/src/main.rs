use std::path::PathBuf;
use rust::get_graph::get_simple_graph;
use graph::prelude::*;

fn main() {
    // First do original approach (not considering cliques) 
    let graph = get_simple_graph(3, 3, 900);
    for i in 0..graph.node_count() {
        println!("Node {} has degree {}", i, graph.degree(i));
    }
}

