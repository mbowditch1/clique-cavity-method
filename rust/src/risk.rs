use graph::prelude::*;

pub fn calculate_original_risk(G: UndirectedCsrGraph<usize>, T: f64) -> Vec<f64> {
    let iterations = 500;
    let mut risk = vec![1.0; G.node_count()];
    risk
}
