use na::DMatrix;

pub fn create_hashimoto(G: UndirectedCsrGraph<usize>) -> UndirectedCsrGraph<usize> {
    let n_edges = graph.edge_count();
    let mut matrix = DMatrix::zeros(n_edges, n_edges);
    
 
 //    let edge_indices: Vec<EdgeIndex> = graph.edge_indices().collect();
 // 
 //    for (i_idx, i_edge) in edge_indices.iter().enumerate() {
 //        let (i_source, i_target) = graph.edge_endpoints(*i_edge).unwrap();
 // 
 //        for (j_idx, j_edge) in edge_indices.iter().enumerate() {
 //            let (j_source, j_target) = graph.edge_endpoints(*j_edge).unwrap();
 // 
 //            // Check the Hashimoto matrix condition
 //            if i_target == j_source && i_source != j_target {
 //                matrix[(i_idx, j_idx)] = 1;
 //            }
 //        }
 //    }
 
    matrix
}
