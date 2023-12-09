use na::DMatrix;
use graph::prelude::*;

pub fn create_hashimoto(G: &UndirectedCsrGraph<usize>) -> (Vec<(usize, usize)>, DirectedCsrGraph<u32, (), f32>) {
    let n_edges = G.edge_count();
    let mut matrix = DMatrix::zeros(2*n_edges, 2*n_edges);
    let edge_list = build_edge_list(&G);

    for (i_idx, i_edge) in edge_list.iter().enumerate() {
        let (i_source, i_target) = i_edge;

        for (j_idx, j_edge) in edge_list.iter().enumerate() {
            let (j_source, j_target) = j_edge;

            // Check the Hashimoto matrix condition
            if i_target == j_source && i_source != j_target {
                matrix[(i_idx, j_idx)] = 1.0;
            }
        }
    }
    // Create graph from matrix
    let mut new_edges: Vec<(u32, u32, f32)> = Vec::new();
    for i in 0..matrix.nrows() {
        for j in 0..matrix.ncols() {
            if matrix[(i, j)] == 1.0 {
                new_edges.push((i as u32, j as u32, 1.0 as f32));
            }
        }
    }
    let mut hashimoto_graph: DirectedCsrGraph<u32, (), f32> = GraphBuilder::new()
        .csr_layout(CsrLayout::Sorted)
        .edges_with_values(new_edges)
        .build();

    (edge_list, hashimoto_graph)
}

pub fn build_edge_list(G: &UndirectedCsrGraph<usize>) -> Vec<(usize, usize)> {
    let mut edge_list = Vec::new();

    for i in 0..G.node_count() {
        let neighbors = G.neighbors(i);
        for n in neighbors {
            edge_list.push((i, *n));
        }
    }
    edge_list
}


pub fn arange(start: f32, end: f32, step: f32) -> Vec<f32> {
    let mut result = Vec::new();
    let mut current = start;

    while current < end {
        result.push(current);
        current += step;
    }

    result
}
