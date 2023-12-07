use std::path::PathBuf;
use graph::prelude::*;


pub fn get_simple_graph(n: usize, m: usize, N: usize) -> UndirectedCsrGraph<usize> {
    let file_name = format!("simple_clique_graph_{}_{}_{}.el", n.to_string().as_str(), m.to_string().as_str(), N.to_string().as_str());
    let path = [env!("CARGO_MANIFEST_DIR"), "resources", file_name.as_str()]
        .iter()
        .collect::<PathBuf>();

    let graph: UndirectedCsrGraph<usize> = GraphBuilder::new()
        .csr_layout(CsrLayout::Sorted)
        .file_format(EdgeListInput::default())
        .path(path)
        .build()
        .expect("loading failed");

    return graph;
}
